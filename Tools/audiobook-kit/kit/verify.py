"""Verify audiobook chapters that are already built, without rendering them again. Part of the audiobook kit: run it
through `audiobook.sh` (option 7).

For each chapter MP3 in `<book>/audiobook/out/` it transcribes the file with Whisper (run locally, with a time for every
word), lines the words up against the chapter's reading script (names count as matching whatever was heard), lists
every place they differ with its time in the file, checks loudness, true peak, clipping and noise floor, and writes
`out/NN_verify.txt` with PASS or FAIL (also recorded in out/manifest.json). It only reports: nothing is re-rendered.

Use:  verify.py 1 | 2-10 | 2,5,9 | --all   [--book DIR]
"""
import json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import render as rc     # shared: norm_words, same_word, name_words  # noqa: E402
import config as cfg     # noqa: E402
import prepare          # noqa: E402

AB, OUT, REPO = cfg.AUDIO, cfg.OUT, cfg.BOOK
SR = 16000


def align(ref, hyp, wild):
    """Word alignment (edit distance; names in `wild` match anything). Returns (ref_i, hyp_j, op) with op in
    'ok', 'sub', 'del' (in the script, not heard) or 'ins' (heard, not in the script)."""
    n, m = len(ref), len(hyp)
    prev = list(range(m + 1))
    back = [bytearray(m + 1) for _ in range(n + 1)]   # 0 diag, 1 up (del), 2 left (ins)
    for j in range(1, m + 1):
        back[0][j] = 2
    for i in range(1, n + 1):
        cur = [i] + [0] * m
        back[i][0] = 1
        r = ref[i - 1]
        rw = r in wild
        for j in range(1, m + 1):
            diag = prev[j - 1] + (0 if (rw or rc.same_word(r, hyp[j - 1])) else 1)
            up = prev[j] + 1
            left = cur[j - 1] + 1
            if diag <= up and diag <= left:
                cur[j] = diag; back[i][j] = 0
            elif up <= left:
                cur[j] = up; back[i][j] = 1
            else:
                cur[j] = left; back[i][j] = 2
        prev = cur
    i, j, ops = n, m, []
    while i > 0 or j > 0:
        b = back[i][j]
        if i > 0 and j > 0 and b == 0:
            ops.append((i - 1, j - 1, "ok" if (ref[i - 1] in wild or rc.same_word(ref[i - 1], hyp[j - 1])) else "sub")); i -= 1; j -= 1
        elif i > 0 and (j == 0 or b == 1):
            ops.append((i - 1, None, "del")); i -= 1
        else:
            ops.append((None, j - 1, "ins")); j -= 1
    return list(reversed(ops))


def clock(t):
    return f"{int(t // 60)}:{t % 60:04.1f}"


def file_checks(mp3):
    """Loudness, true peak, clipping and noise floor of the finished file (decoded)."""
    import numpy as np
    notes, fails = [], []
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", mp3, "-af", "ebur128=peak=true", "-f", "null", "-"],
                       capture_output=True, text=True)
    tail = r.stderr[r.stderr.rfind("Summary:"):]
    lufs = re.search(r"I:\s+(-?[\d.]+) LUFS", tail)
    peak = re.search(r"Peak:\s+(-?[\d.]+) dBFS", tail)
    if not lufs or not peak:
        notes.append("loudness or true peak couldn't be measured  <- FAIL: check the file plays")
        fails.append("not measurable")
    if lufs:
        v = float(lufs.group(1))
        ok = -23 <= v <= -18
        notes.append(f"loudness {v:.1f} LUFS" + ("" if ok else "  <- FAIL: outside -23..-18"))
        ok or fails.append("loudness")
    if peak:
        v = float(peak.group(1))
        notes.append(f"true peak {v:.1f} dBFS" + ("" if v <= -3 else "  <- FAIL: above -3"))
        v <= -3 or fails.append("true peak")
    raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", mp3, "-ac", "1", "-ar", "44100", "-f", "f32le", "-"],
                         capture_output=True, check=True).stdout
    wav = np.frombuffer(raw, dtype=np.float32)
    clipped = int(np.sum(np.abs(wav) >= 0.999))
    notes.append(f"clipped samples: {clipped}" + ("" if clipped < 10 else "  <- FAIL: check for distortion"))
    clipped < 10 or fails.append("clipping")
    win = 2205
    frames = wav[: len(wav) // win * win].reshape(-1, win)
    rms = np.sqrt(np.mean(frames ** 2, axis=1))
    live = rms[rms > 1e-4]          # leave out the inserted pauses (digital silence, near zero after encoding)
    if len(live):
        quiet = live[live < np.percentile(live, 10) * 1.5]
        floor = 20 * np.log10(max(float(np.median(quiet)), 1e-9))
        notes.append(f"noise floor about {floor:.0f} dBFS" + ("" if floor < -55 else "  <- hiss or hum between words? (listen)"))
    return notes, fails, len(wav) / 44100


def main():
    args = sys.argv[1:]
    import numpy as np
    from faster_whisper import WhisperModel
    model_name = os.environ.get("WORDCHECK_MODEL", "small.en")
    print(f"word check: Whisper {model_name}")
    asr = WhisperModel(model_name, device="cpu", compute_type="int8")
    base_names = rc.name_words()
    prepare.main(quiet=True)

    chapters = []
    for a in args:
        for part in a.split(","):
            if re.fullmatch(r"\d+-\d+", part):
                lo, hi = map(int, part.split("-")); chapters += range(lo, hi + 1)
            elif part.isdigit():
                chapters.append(int(part))
    if "--all" in args:
        chapters = [int(f[:2]) for f in os.listdir(OUT) if re.fullmatch(r"\d\d\.mp3", f)]
    chapters = sorted(set(chapters))
    if not chapters:
        sys.exit("No chapters given: e.g. 1, 2-10, 2,5,9 or --all")

    man_path = os.path.join(OUT, "manifest.json")
    try:
        manifest = json.load(open(man_path))
    except Exception:
        manifest = {}

    for n in chapters:
        mp3 = os.path.join(OUT, f"{n:02d}.mp3")
        if not os.path.exists(mp3):
            print(f"{n:02d}: not built yet ({os.path.relpath(mp3, REPO)} missing), skipped"); continue
        print(f"{n:02d}: transcribing…", flush=True)
        # decode with ffmpeg ourselves (16 kHz mono) rather than letting faster-whisper open the file: its PyAV call
        # breaks with newer PyAV releases
        pcm = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", mp3, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                             capture_output=True, check=True).stdout
        audio16 = np.frombuffer(pcm, dtype=np.float32)
        segs, _ = asr.transcribe(audio16, language="en", beam_size=1, word_timestamps=True,
                                 condition_on_previous_text=False, vad_filter=False)
        heard, times = [], []
        for sg in segs:
            for w in sg.words or []:
                for t in rc.norm_words(w.word):
                    heard.append(t); times.append(w.start)
        sp = cfg.script_path(n)
        if not os.path.exists(sp):
            print(f"{n:02d}: no reading script for this chapter, skipped"); continue
        sdata = json.load(open(sp, encoding="utf-8"))
        script = sdata["segments"]
        wild = base_names | set(sdata.get("names", []))
        ref = [w for s in script for w in rc.norm_words(s["text"])]
        ops = align(ref, heard, wild)

        # group differences into places: a run of differences, allowing two matching words inside a run
        places, cur, gap = [], [], 0
        for k, (i, j, op) in enumerate(ops):
            if op == "ok":
                if cur:
                    gap += 1
                    if gap > 2:
                        places.append(cur); cur, gap = [], 0
                continue
            gap = 0
            cur.append(k)
        if cur:
            places.append(cur)
        report, serious = [], 0
        last_t = 0.0
        tline = [None] * len(ops)
        for k, (i, j, op) in enumerate(ops):     # a time for every step, carried forward over missing words
            if j is not None:
                last_t = times[j]
            tline[k] = last_t
        for p in places:
            a, b = p[0], p[-1]
            ref_words = [ref[ops[k][0]] for k in range(a, b + 1) if ops[k][0] is not None]
            hyp_words = [heard[ops[k][1]] for k in range(a, b + 1) if ops[k][1] is not None]
            errs = sum(1 for k in p)
            big = errs >= 2 or len(ref_words) >= 3 and not hyp_words
            serious += big
            ctx_i = next((ops[k][0] for k in range(a, -1, -1) if ops[k][0] is not None), 0)
            before = " ".join(ref[max(0, ctx_i - 4): ctx_i])
            report.append(f"{'CHECK' if big else 'minor'}  {clock(tline[a])}  script: \"{' '.join(ref_words) or '(nothing)'}\""
                          f"  heard: \"{' '.join(hyp_words) or '(nothing)'}\"   (after: …{before})")
        total = sum(1 for _, _, op in ops if op != "ok")
        rate = total / max(len(ref), 1)
        notes, fails, secs = file_checks(mp3)
        if serious:
            fails = [f"{serious} place(s) where the words differ"] + fails
        status = "PASS" if not fails else "FAIL"
        with open(os.path.join(OUT, f"{n:02d}_verify.txt"), "w", encoding="utf-8") as fh:
            fh.write(f"Chapter {n} verification of the built file: {status}" + (f" ({', '.join(fails)})" if fails else "") + "\n\n"
                     f"Length {clock(secs)}. Script {len(ref)} words; heard {len(heard)}. Differences: {total} "
                     f"({rate:.1%}), in {len(places)} place(s), {serious} worth checking.\n"
                     "Names count as matching. 'minor' is usually the recogniser mishearing one word; 'CHECK' is a likely\n"
                     "skip, repeat or garble. Listen at each CHECK time.\n\n"
                     "Finished file:\n" + "\n".join("- " + x for x in notes) + "\n\n"
                     "Places:\n" + ("\n".join(report) if report else "(none)") + "\n")
        prev = manifest.get(f"{n:02d}")
        prev = prev if isinstance(prev, dict) else {"digest": prev}
        prev.update(status=status, reasons=fails, verified="built file")
        manifest[f"{n:02d}"] = prev
        json.dump(manifest, open(man_path, "w"), indent=1)
        print(f"{n:02d}: {status}" + (f" ({', '.join(fails)})" if fails else "") +
              f"; {total} word differences ({rate:.1%}), {serious} to check; " + "; ".join(notes) +
              f"\n    report: {os.path.relpath(os.path.join(OUT, f'{n:02d}_verify.txt'), REPO)}")


if __name__ == "__main__":
    main()
