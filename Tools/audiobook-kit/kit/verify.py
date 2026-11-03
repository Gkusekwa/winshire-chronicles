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
    dc = [0 if w.startswith("~") else 1 for w in ref]      # optional words (from contractions) cost nothing
    ic = [0 if w.startswith("~") else 1 for w in hyp]
    prev = [0] * (m + 1)
    for j in range(1, m + 1):
        prev[j] = prev[j - 1] + ic[j - 1]
    back = [bytearray(m + 1) for _ in range(n + 1)]   # 0 diag, 1 up (del), 2 left (ins)
    for j in range(1, m + 1):
        back[0][j] = 2
    for i in range(1, n + 1):
        cur = [prev[0] + dc[i - 1]] + [0] * m
        back[i][0] = 1
        r = ref[i - 1]
        rw = r in wild
        for j in range(1, m + 1):
            diag = prev[j - 1] + (0 if (rw or rc.same_word(r, hyp[j - 1])) else 1)
            up = prev[j] + dc[i - 1]
            left = cur[j - 1] + ic[j - 1]
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
            ops.append((i - 1, None, "del" if dc[i - 1] else "ok")); i -= 1
        else:
            ops.append((None, j - 1, "ins" if ic[j - 1] else "ok")); j -= 1
    return list(reversed(ops))


def lcs(ref, hyp, wild):
    """How many of the script's words are heard, in order (names match anything)."""
    prev = [0] * (len(hyp) + 1)
    for r in ref:
        cur = [0]
        for j, h in enumerate(hyp):
            cur.append(prev[j] + 1 if (r in wild or rc.same_word(r, h)) else max(prev[j + 1], cur[j]))
        prev = cur
    return prev[-1]


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
    asr = cfg.whisper_model(model_name)
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
        if sdata.get("chapter") in (0, 99):        # the credits: the book's own title and series are names here
            wild = wild | set(rc.norm_words(cfg.TITLE + " " + cfg.SERIES))
        joined = rc.join_split(heard, ref)
        if len(joined) != len(heard):              # keep a time for each joined word
            t2, i = [], 0
            for w in joined:
                t2.append(times[i]); i += 1 if w == heard[i] else 2
            heard, times = joined, t2
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
        second = 0
        for p in places:
            a, b = p[0], p[-1]
            ref_words = [ref[ops[k][0]] for k in range(a, b + 1) if ops[k][0] is not None]
            hyp_words = [heard[ops[k][1]] for k in range(a, b + 1) if ops[k][1] is not None]
            errs = sum(1 for k in p)
            big = errs >= 2 or len(ref_words) >= 3 and not hyp_words
            if big:
                # A second listen: transcribing a whole chapter, a recogniser sometimes drops or merges a sentence.
                # Cut out just this stretch and transcribe it alone; if the script's words are there, it's minor.
                t0 = max(0.0, tline[a] - 1.5)
                t1 = t0 + max(6.0, len(ref_words) / 2.0 + 4.0)
                clip = audio16[int(t0 * SR):int(t1 * SR)]
                s2, _ = asr.transcribe(clip, language="en", beam_size=5, condition_on_previous_text=False, vad_filter=False)
                again = rc.join_split(rc.norm_words(" ".join(x.text for x in s2)), ref_words)
                needed = [w for w in ref_words if not w.startswith("~")]
                found = lcs(needed, again, wild)
                if found >= len(needed) - (1 if len(needed) > 5 else 0):
                    big = False; second += 1
                    hyp_words = hyp_words + ["(a second listen heard it: " + " ".join(again[:12]) + ("…" if len(again) > 12 else "") + ")"]
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
                     f"({rate:.1%}), in {len(places)} place(s), {serious} worth checking"
                     f"{f' ({second} more cleared by a second listen)' if second else ''}.\n"
                     "Names count as matching. 'minor' is usually the recogniser mishearing one word; 'CHECK' is a likely\n"
                     "skip, repeat or garble. Listen at each CHECK time.\n\n"
                     "Finished file:\n" + "\n".join("- " + x for x in notes) + "\n\n"
                     "Places:\n" + ("\n".join(report) if report else "(none)") + "\n")
        prev = manifest.get(f"{n:02d}")
        prev = prev if isinstance(prev, dict) else {"digest": prev}
        if "accepted after listening" in prev.get("reasons", []) and status == "FAIL":
            rp = os.path.join(OUT, f"{n:02d}_verify.txt")
            report_text = open(rp, encoding="utf-8").read()          # read before rewriting
            if all(rc.word_doubt(f) for f in fails):
                # someone listened and accepted this chapter: the word check's doubts are reported, the acceptance
                # stands. (A technical failure, such as loudness, peaks or clipping, is never overridden.)
                status, fails = "PASS", ["accepted after listening"] + fails
                open(rp, "w", encoding="utf-8").write("ACCEPTED after listening: the chapter counts as PASS. The report"
                                                      " below is from the automatic check.\n\n" + report_text)
            else:
                open(rp, "w", encoding="utf-8").write("Accepted after listening earlier, but it now fails a technical check"
                                                      " (not the words), so it counts as FAIL.\n\n" + report_text)
        prev.update(status=status, reasons=fails, verified="built file")
        manifest = cfg.save_manifest_entry(f"{n:02d}", prev)
        print(f"{n:02d}: {status}" + (f" ({', '.join(fails)})" if fails else "") +
              f"; {total} word differences ({rate:.1%}), {serious} to check; " + "; ".join(notes) +
              f"\n    report: {os.path.relpath(os.path.join(OUT, f'{n:02d}_verify.txt'), REPO)}")


if __name__ == "__main__":
    main()
