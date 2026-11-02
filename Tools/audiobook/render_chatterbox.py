"""Render Book 1 audiobook passages with Chatterbox (Resemble AI, MIT licence): free, offline after the first
model download, and able to act. The audiobook's narration route.

How it reads the scripts (`Book 1/audiobook/Performance/NN.json`, part titles and chapter
numbers included):
- The narrator reads everything, in Emma's voice, cloned from a short reference clip
  (`Book 1/audiobook/Chatterbox/refs/Narrator.wav`: a 9.6-second clip of Emma, 24 kHz mono, made with the
  Kokoro-82M model's voice bf_emma; see the audiobook README for its fingerprint). With --cast, characters with a clip of their own in refs/
  speak in that voice.
- Automatic checks on every take, before it is kept:
  1. length: does it take about as long as its text should? (too short = skipped words; too long = repeats, babble)
  2. silence: no gap over two seconds inside it (the model lost its place)
  3. words: Whisper (faster-whisper, run locally) transcribes the take and it is compared word for word with the
     script; more than about 1 word in 8 wrong means another take. Invented names count as matching, since a
     recogniser can't spell them. Skip it with --no-verify (one take, no checks); choose the Whisper model with WORDCHECK_MODEL.
  A take that fails is made again, up to three tries, and the best one kept; anything still doubtful is listed in
  out/NN_check.txt, with the words that differed.
- Checks on each finished chapter, also in out/NN_check.txt: loudness (about -19 LUFS), true peak (below -3 dBFS),
  clipping, and the noise floor between words.
- Each chapter gets a status in out/NN_check.txt and out/manifest.json: PASS (no doubtful passages; loudness, peak
  and clipping within limits), FAIL (with the reasons), or UNCHECKED (rendered with --no-verify, a draft). The word
  check is required: if Whisper can't load, rendering stops unless --no-verify is given. --skip-done skips only
  chapters that PASSED and whose inputs haven't changed; FAIL and UNCHECKED chapters are rendered again.
- None of this replaces listening: names, emphasis and feeling need a human ear, starting with the STILL DOUBTFUL
  passages.
- Higher emotion intensity can also make Chatterbox speak faster: check pacing as well as feeling when listening.
- Resume: out/manifest.json fingerprints each chapter's inputs (script, renderer, name respellings, cast map, narrator
  clip, options); --skip-done re-renders a chapter whenever any of them changed.
- Each line's mood and "how" note set Chatterbox's emotion intensity (exaggeration) and pacing (cfg weight).
- Names are respelt from `Lexicon_Alias.pls`, since Chatterbox reads text, not phonemes.
- Chatterbox adds an inaudible Perth watermark to its output (Resemble AI's responsible-AI marker).

Setup on a Mac: `bash Tools/audiobook/chatterbox_mac.sh` (Python 3.11, chatterbox-tts 0.1.7, the model from Hugging Face).

Use:
    python3 render_chatterbox.py --audition      # passages of every kind from across the book -> out/audition.mp3
    python3 render_chatterbox.py 1               # chapter 1 -> out/01.mp3
    python3 render_chatterbox.py 1-79 --skip-done
    python3 render_chatterbox.py 2,5,9                 # a list (ranges and lists can mix: 1-3,7)
    python3 render_chatterbox.py --all                 # the whole book: credits 00 and 99 and every chapter
    python3 render_chatterbox.py 1 --no-verify         # faster draft: one take per passage, no checks -> UNCHECKED
    python3 render_chatterbox.py 1 --narrator-ref Other.wav             # another narrator clip from refs/

Output: `Book 1/audiobook/Chatterbox/out/` (ignored by git; never commit the audio).
"""
import hashlib, json, os, re, subprocess, sys, xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import cast as castmap        # noqa: E402

REPO = os.path.dirname(os.path.dirname(HERE))
AB = os.path.join(REPO, "Book 1", "audiobook")
KINDS = {"title", "narration", "speech", "bond", "thought", "remembered", "written", "verse"}


def clean(text):
    text = re.sub(r"[*_]", "", text)
    return text.replace("‘", "'").replace("“", '"').replace("”", '"').strip()


def title_pieces(text):
    """A title line is said as separate lines with a beat between: "Part One" / "Two Banks"."""
    return [p.strip() for p in re.split(r"(?<=\.)\s+", text) if p.strip()]


def kind(seg):
    t = seg.get("type", "narration")
    return t if t in KINDS else "narration"


def audition():
    """A few minutes that cover every kind of passage, drawn from across the book: plain narration, a long
    paragraph, a very short line, dialogue, bond speech, inner thought, remembered words, grief, tension, verse
    and written words. Same passages for every voice, so voices can be compared like for like."""
    picks, seen = [], set()
    want = [("title", None), ("narration", None), ("long", None), ("short", None), ("speech", None),
            ("bond", None), ("thought", None), ("remembered", None), ("narration", "grief"),
            ("narration", "tension"), ("verse", None), ("written", None), ("bond", "grief")]
    files = sorted(f for f in os.listdir(os.path.join(AB, "Performance")) if f.endswith(".json") and f[:2].isdigit() and f[:2] not in ("00", "99"))
    groups = []
    for f in files:
        segs = json.load(open(os.path.join(AB, "Performance", f), encoding="utf-8"))["segments"]
        cur = []
        for s in segs:
            if cur and s.get("para") and cur[-1].get("para") == s["para"]:
                cur.append(s)
            else:
                if cur: groups.append((f, cur))
                cur = [s]
        if cur: groups.append((f, cur))
    for t, mood in want:
        for i, (f, g) in enumerate(groups):
            if (f in seen and t != "title") or i in [x[0] for x in picks]:
                continue
            kinds = {s["type"] for s in g}
            text = " ".join(s["text"] for s in g)
            m = {s.get("mood") for s in g}
            if t == "long": ok = kinds == {"narration"} and len(text) > 700
            elif t == "short": ok = kinds == {"narration"} and len(text) < 25
            elif t == "speech": ok = "speech" in kinds and "narration" in kinds and len(text) > 120
            elif t == "title": ok = kinds == {"title"} and f == files[0]
            else: ok = t in kinds and (len(kinds) == 1 or t == "bond") and (mood is None or mood in m)
            if ok:
                picks.append((i, g)); seen.add(f)
                if t == "title":   # the whole opening title block
                    j = i + 1
                    while groups[j][1][0]["type"] == "title":
                        picks.append((j, groups[j][1])); j += 1
                break
    out = []
    for _, g in picks:
        if g[0]["type"] == "title":   # the opening titles keep the book's own pauses
            out.append([dict(s) for s in g]); continue
        out.append([dict(s, pause_after_ms=max(s.get("pause_after_ms", 500), 500)) for s in g])
        out[-1][-1]["pause_after_ms"] = 1500   # a clear gap between passages
    return out
OUT = os.path.join(AB, "Chatterbox", "out")
REFS = os.path.join(AB, "Chatterbox", "refs")

# mood -> (exaggeration, cfg_weight). Higher exaggeration = more feeling; lower cfg = slower, more deliberate.
MOOD = {
    None: (0.50, 0.50), "tension": (0.60, 0.50), "dread": (0.60, 0.40), "grief": (0.70, 0.30),
    "quiet": (0.40, 0.45), "reflective": (0.45, 0.45), "tender": (0.50, 0.40), "humour": (0.60, 0.50),
    "anger": (0.80, 0.40), "awe": (0.60, 0.35), "urgent": (0.75, 0.55), "action": (0.70, 0.55),
}
HOW = [("shout", 0.25, 3), ("roar", 0.30, 4), ("loud", 0.15, 2), ("whisper", -0.15, -6), ("very quiet", -0.10, -5),
       ("quiet", -0.05, -3), ("soft", -0.05, -2.5), ("low", -0.05, -2), ("faint", -0.10, -5), ("weak", -0.10, -4),
       ("cracking", 0.20, -1), ("shaking", 0.15, -1), ("eager", 0.15, 0), ("urgent", 0.15, 0.5)]
GAIN = {"bond": -3.0, "thought": -4.5, "remembered": -4.5, "written": -1.0, "verse": -1.0}
TEMPO = {"bond": 0.95, "thought": 0.97, "remembered": 0.97, "verse": 0.94, "written": 0.95, "title": 0.95}


def aliases():
    ns = {"p": "http://www.w3.org/2005/01/pronunciation-lexicon"}
    pairs = []
    for lx in ET.parse(os.path.join(AB, "Lexicon_Alias.pls")).getroot().findall("p:lexeme", ns):
        a = lx.find("p:alias", ns)
        if a is not None and a.text:
            pairs.append((lx.find("p:grapheme", ns).text, a.text))
    pairs.sort(key=lambda x: -len(x[0]))
    return [(re.compile(r"\b" + re.escape(g) + r"\b"), a) for g, a in pairs]


def text_of(segs, subs):
    t = " ".join(clean(s["text"]) for s in segs if s["text"].strip())
    t = t.replace("’", "'")
    for rx, a in subs:
        t = rx.sub(a, t)
    return t


def chunks(text, limit=200):
    """Chatterbox reads best in pieces of a sentence or three; split long text at sentence ends."""
    out, cur = [], ""
    for sent in re.split(r"(?<=[.!?…])\s+", text):
        if cur and len(cur) + len(sent) > limit:
            out.append(cur); cur = sent
        else:
            cur = (cur + " " + sent).strip()
    if cur:
        out.append(cur)
    return out


# ---------------- word check (speech recognition) ----------------
_ONES = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
_TENS = "_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()
_ORD = {"first": "one", "third": "three", "fifth": "five", "eighth": "eight", "ninth": "nine", "twelfth": "twelve",
        **{w + "th": w for w in "four six seven ten eleven thirteen fourteen fifteen sixteen seventeen eighteen nineteen hundred thousand".split()},
        **{w[:-1] + "ieth": w for w in "twenty thirty forty fifty sixty seventy eighty ninety".split()}}


def _num_words(n):
    """1 -> one, 42 -> forty two, 1,200 -> one thousand two hundred (recognisers write numbers as digits)."""
    if n < 20:
        return _ONES[n]
    if n < 100:
        return _TENS[n // 10] + ("" if n % 10 == 0 else " " + _ONES[n % 10])
    if n < 1000:
        return _ONES[n // 100] + " hundred" + ("" if n % 100 == 0 else " " + _num_words(n % 100))
    if n < 1000000:
        return _num_words(n // 1000) + " thousand" + ("" if n % 1000 == 0 else " " + _num_words(n % 1000))
    return str(n)


def norm_words(text):
    """Lowercase words without punctuation, numbers spelt out, for comparing what was said with what was written."""
    text = text.lower().replace("\u2019", "'").replace("-", " ").replace("\u2014", " ").replace("\u2013", " ")
    text = re.sub(r"(\d),(\d{3})", r"\1\2", text)
    text = re.sub(r"\d+(st|nd|rd|th)?", lambda m: " " + _num_words(int(re.match(r"\d+", m.group()).group())) + " ", text)
    words = [w.replace("'", "") for w in re.findall(r"[a-z']+", text) if w.replace("'", "")]
    # numbers said in words: ordinals as cardinals (tenth -> ten), no "and" or "a/one" before hundred/thousand,
    # so "the hundred-and-tenth day" and "the 110th day" compare equal
    out = []
    for w in words:
        w = _ORD.get(w, w)
        if w == "second" and out and (out[-1] in _TENS or out[-1] in ("hundred", "thousand")):
            w = "two"      # forty-second -> forty two; "a second" stays a word
        if w == "and" and out and out[-1] in ("hundred", "thousand"):
            continue
        if w in ("hundred", "thousand") and out and out[-1] in ("a", "one"):
            out.pop()
        out.append(w)
    return out


_SIM = {}


def same_word(a, b):
    """Equal, or near enough to be a spelling variant (Ottery's / Otterys / Otteries): same first letter and at
    most one edit per three letters. Short words must match exactly."""
    if a == b:
        return True
    if len(a) < 4 or len(b) < 4 or a[0] != b[0]:
        return False
    key = (a, b)
    if key not in _SIM:
        la, lb = len(a), len(b)
        limit = max(1, min(la, lb) // 3)
        if abs(la - lb) > limit:
            _SIM[key] = False
        else:
            prev = list(range(lb + 1))
            for i in range(1, la + 1):
                cur = [i] + [0] * lb
                for j in range(1, lb + 1):
                    cur[j] = min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (a[i - 1] != b[j - 1]))
                prev = cur
            _SIM[key] = prev[lb] <= limit
    return _SIM[key]


def name_words():
    """Invented names (and their respellings): a recogniser can't be expected to spell them, so they count as
    matching whatever word was heard in their place."""
    words = set()
    ns = {"p": "http://www.w3.org/2005/01/pronunciation-lexicon"}
    for lx in ET.parse(os.path.join(AB, "Lexicon_Alias.pls")).getroot().findall("p:lexeme", ns):
        for tag in ("p:grapheme", "p:alias"):
            e = lx.find(tag, ns)
            if e is not None and e.text:
                words.update(norm_words(e.text))
    try:
        sys.path.insert(0, HERE)
        from names import NAMES
        for n in NAMES:
            words.update(norm_words(n[0]))
            if n[3]:
                words.update(norm_words(n[3]))
    except Exception:
        pass
    return words


def word_errors(ref, hyp, wild):
    """Word-level edit distance between the script (ref) and what was heard (hyp); script words in `wild` (names)
    match any one heard word. Returns (errors, details) where details lists what went wrong."""
    n, m = len(ref), len(hyp)
    d = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        d[i][0] = i
    for j in range(m + 1):
        d[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            same = same_word(ref[i - 1], hyp[j - 1]) or ref[i - 1] in wild
            d[i][j] = min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + (0 if same else 1))
    # walk back for a short list of what differed
    i, j, out = n, m, []
    while i > 0 or j > 0:
        if i > 0 and j > 0 and d[i][j] == d[i - 1][j - 1] + (0 if (same_word(ref[i - 1], hyp[j - 1]) or ref[i - 1] in wild) else 1):
            if not (same_word(ref[i - 1], hyp[j - 1]) or ref[i - 1] in wild):
                out.append(f"'{ref[i - 1]}'->'{hyp[j - 1]}'")
            i, j = i - 1, j - 1
        elif i > 0 and d[i][j] == d[i - 1][j] + 1:
            out.append(f"missing '{ref[i - 1]}'"); i -= 1
        else:
            out.append(f"extra '{hyp[j - 1]}'"); j -= 1
    return d[n][m], list(reversed(out))

BOOK_TITLE, BOOK_AUTHOR = "The Watch Below", "Goodluck Kusekwa"
SCRIPT_OF = lambda n: os.path.join(AB, "Performance", f"{n:02d}.json")
ALL_CHAPTERS = lambda: sorted(int(f[:2]) for f in os.listdir(os.path.join(AB, "Performance")) if re.fullmatch(r"\d\d\.json", f))


# ---------------- tags (what players and stores show) ----------------
def chapter_title(n):
    """"Chapter 7: The Ferry" from the chapter's script; the credits and audition get their own names."""
    if n == "audition":
        return "Audition"
    if n == 0:
        return "Opening credits"
    if n == 99:
        return "Closing credits"
    try:
        t = (json.load(open(SCRIPT_OF(n), encoding="utf-8")).get("title") or "").strip().rstrip(".")
    except Exception:
        t = ""
    return f"Chapter {n}: {t}" if t else f"Chapter {n}"


def tag_mp3(mp3, n):
    """Write the chapter's title, the book, the author and the track number into the MP3 (ID3v2.3), in place.
    Only the tags change; the audio is copied untouched."""
    nums = ALL_CHAPTERS()
    meta = {"title": chapter_title(n), "album": BOOK_TITLE, "artist": BOOK_AUTHOR, "album_artist": BOOK_AUTHOR,
            "genre": "Audiobook", "comment": "Read by a digital voice (Chatterbox)."}
    if n != "audition" and n in nums:
        meta["track"] = f"{nums.index(n) + 1}/{len(nums)}"
    args = []
    for k, v in meta.items():
        if v:
            args += ["-metadata", f"{k}={v}"]
    tmp = mp3[:-4] + ".tagging.mp3"
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", mp3, "-map", "0:a", "-c", "copy", "-map_metadata", "-1",
                    *args, "-id3v2_version", "3", "-write_id3v1", "1", tmp], check=True)
    os.replace(tmp, mp3)
    return meta["title"]


def chapter_list(args):
    out = []
    for a in args:
        for part in a.split(","):
            if re.fullmatch(r"\d+-\d+", part):
                lo, hi = map(int, part.split("-")); out += range(lo, hi + 1)
            elif part.isdigit():
                out.append(int(part))
    return out


def retag(args):
    """--retag 1 | 2-10 | --all: put the titles into chapters already built, without rendering them again."""
    nums = sorted(set(ALL_CHAPTERS() if "--all" in args else chapter_list(args)))
    done = 0
    for n in nums:
        mp3 = os.path.join(OUT, f"{n:02d}.mp3")
        if os.path.exists(mp3):
            print(f"{n:02d}: {tag_mp3(mp3, n)}"); done += 1
    print(f"Tagged {done} file(s) in {OUT}.")


def main():
    args = sys.argv[1:]
    if "--retag" in args:
        return retag([a for a in args if a != "--retag"])
    use_cast = "--cast" in args   # default: the narrator (Emma) reads everything
    import numpy as np, torch
    import perth
    if perth.PerthImplicitWatermarker is None:
        sys.exit("Chatterbox's watermarker didn't load (it needs pkg_resources). Run: ~/chatterbox/venv/bin/pip install 'setuptools<81'")
    from chatterbox.tts import ChatterboxTTS
    device = "cuda" if torch.cuda.is_available() else ("mps" if torch.backends.mps.is_available() else "cpu")
    print("device:", device)
    model = ChatterboxTTS.from_pretrained(device=device)
    asr = None
    no_verify = "--no-verify" in args or "--no-words" in args
    TRIES = 1 if no_verify else 3
    if not no_verify:
        try:
            from faster_whisper import WhisperModel
            asr = WhisperModel(os.environ.get("WORDCHECK_MODEL", "small.en"), device="cpu", compute_type="int8")
            print("word check: on (Whisper", os.environ.get("WORDCHECK_MODEL", "small.en") + ")")
        except Exception as e:
            sys.exit(f"The word check (faster-whisper) didn't load: {e}\n"
                     "Fix it (bash Tools/audiobook/chatterbox_mac.sh installs it), or render without verifying by adding --no-verify.")
    else:
        print("verify: OFF (--no-verify): one take per passage, no word check; chapters are marked UNCHECKED (a draft)")
    WILD = name_words()
    MAX_WER = 0.12   # more than about 1 word in 8 wrong (names excluded) -> another take
    SR = model.sr
    subs = aliases()
    os.makedirs(OUT, exist_ok=True)
    conds = {}
    checks = []
    stats = {"takes": 0, "passages": 0}

    narrator_ref = args[args.index("--narrator-ref") + 1] if "--narrator-ref" in args else None

    def ref_for(role):
        if role == "Narrator" and narrator_ref:
            return narrator_ref if os.path.isabs(narrator_ref) else os.path.join(REFS, narrator_ref)
        p = os.path.join(REFS, role.replace(" ", "_") + ".wav")
        return p if os.path.exists(p) else os.path.join(REFS, "Narrator.wav")

    CHARS_PER_SEC = 14.0   # a steady narrator; used only to spot passages whose length doesn't fit their text

    def problem(audio, text):
        """Why this take looks like a slip, or None. Too short = words skipped; too long = repeats or babble;
        a long silence inside = the model lost its place."""
        secs = len(audio) / SR
        expect = max(len(text) / CHARS_PER_SEC, 0.6)
        if secs < expect * 0.5:
            return f"too short ({secs:.1f}s for ~{expect:.1f}s)"
        if secs > expect * 1.8 + 1.0:
            return f"too long ({secs:.1f}s for ~{expect:.1f}s)"
        env = np.abs(audio)
        win = int(SR * 0.05)
        if len(env) > win * 4:
            frames = env[: len(env) // win * win].reshape(-1, win).max(axis=1)
            quiet = frames < max(frames.max() * 0.02, 1e-4)
            run = best = 0
            for q in quiet[2:-2]:
                run = run + 1 if q else 0
                best = max(best, run)
            if best * 0.05 > 2.0:
                return f"silence of {best * 0.05:.1f}s inside"
        return None

    def heard(audio):
        """What the recogniser hears in a take (16 kHz for Whisper)."""
        x = np.interp(np.arange(0, len(audio), SR / 16000), np.arange(len(audio)), audio).astype(np.float32)
        segs, _ = asr.transcribe(x, language="en", beam_size=1, vad_filter=False, condition_on_previous_text=False)
        return " ".join(sg.text for sg in segs)

    def word_problem(audio, text):
        """Compare the words heard with the words written. Returns (why or None, error rate, details)."""
        if asr is None:
            return None, 0.0, []
        ref, hyp = norm_words(text), norm_words(heard(audio))
        if not ref:
            return None, 0.0, []
        errs, details = word_errors(ref, hyp, WILD)
        rate = errs / len(ref)
        # Short lines (8 words or fewer) must match exactly: one wrong word there can be the whole line. If the
        # recogniser itself is at fault, the line ends up STILL DOUBTFUL and is listened to.
        if (len(ref) <= 8 and errs > 0) or (len(ref) > 8 and rate > MAX_WER):
            return f"words differ ({errs} of {len(ref)}: {', '.join(details[:6])})", rate, details
        return None, rate, details

    def say(text, role, exaggeration, cfg):
        key = role
        if key not in conds:
            model.prepare_conditionals(ref_for(role), exaggeration=exaggeration)
            conds[key] = model.conds
        model.conds = conds[key]
        takes = []
        for attempt in range(TRIES):
            wav = model.generate(text, exaggeration=exaggeration, cfg_weight=cfg)
            audio = wav.squeeze(0).cpu().numpy().astype(np.float32)
            why = problem(audio, text)          # length and silence
            rate = 0.0
            if why is None:
                why, rate, _ = word_problem(audio, text)   # the words themselves
            takes.append((why, rate, audio))
            stats["takes"] += 1
            if why is None:
                break
        expect = len(text) / CHARS_PER_SEC
        why, rate, audio = min(takes, key=lambda t: (t[0] is not None, t[1], abs(len(t[2]) / SR - expect)))
        stats["passages"] += 1
        if len(takes) > 1 or why:
            checks.append(f"{'STILL DOUBTFUL' if why else 'fixed on retry'} ({len(takes)} tries; {why or takes[0][0]}): {text}")
        return audio

    def tempo(audio, f):
        if abs(f - 1) < 0.01:
            return audio
        r = subprocess.run(["ffmpeg", "-loglevel", "error", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "pipe:0",
                            "-af", f"atempo={f:.4f}", "-f", "f32le", "pipe:1"],
                           input=audio.tobytes(), capture_output=True, check=True)
        return np.frombuffer(r.stdout, dtype=np.float32)

    def runs(group):
        """One reading per paragraph when Emma reads everything: Chatterbox garbles a word or two said alone
        (“Again,”), so speech is never split from the narration around it. With --cast, a character's lines
        go to their own voice."""
        if not use_cast:
            return [("Narrator", list(group))]
        out = []
        for s in group:
            role = (castmap.role_of(s["speaker"]) if use_cast and s.get("speaker") and kind(s) in ("speech", "bond")
                    else "Narrator")
            if out and out[-1][0] == role and kind(out[-1][1][-1]) == kind(s):
                out[-1][1].append(s)
            else:
                out.append((role, [s]))
        return out

    def render(groups, label):
        parts = []
        for i, group in enumerate(groups):
            rs = runs(group)
            for j, (role, segs) in enumerate(rs):
                text = text_of(segs, subs)
                if not text:
                    continue
                kinds = {kind(x) for x in segs}
                style = kinds.pop() if len(kinds) == 1 else "narration"   # bond, thought... only if the whole run is
                # mood is set per paragraph in the scripts (no paragraph mixes moods); if one ever did,
                # the mood of the longest stretch of text wins
                weights = {}
                for x in segs:
                    weights[x.get("mood")] = weights.get(x.get("mood"), 0) + len(x["text"])
                ex, cfg = MOOD.get(max(weights, key=weights.get), MOOD[None])
                gain = GAIN.get(style, 0.0)
                how = " ".join(s.get("how") or "" for s in segs).lower()
                for word, dex, dg in HOW:
                    if word in how:
                        ex += dex; gain += dg; how = how.replace(word, "")
                ex = max(0.25, min(1.0, ex))
                pieces = title_pieces(text) if style == "title" else chunks(text)
                for q, piece in enumerate(pieces):
                    audio = tempo(say(piece, role, ex, cfg), TEMPO.get(style, 1.0))
                    parts.append(audio * (10 ** (gain / 20)))
                    if q < len(pieces) - 1:
                        parts.append(np.zeros(int(SR * (1.0 if style == "title" else 0.2)), dtype=np.float32))
                if j < len(rs) - 1:
                    parts.append(np.zeros(int(SR * 0.15), dtype=np.float32))
            parts.append(np.zeros(int(SR * group[-1].get("pause_after_ms", 300) / 1000), dtype=np.float32))
            print(f"\r{label}: {i + 1}/{len(groups)}", end="", flush=True)
        return np.concatenate(parts)

    def write(wav, mp3):
        tmp = mp3 + ".f32"
        wav.astype(np.float32).tofile(tmp)
        partial = mp3[:-4] + ".partial.mp3"
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", tmp,
                        "-af", "loudnorm=I=-19:TP=-3:LRA=11", "-ar", "44100", "-b:a", "128k", partial], check=True)
        os.remove(tmp)
        os.replace(partial, mp3)
        print(f"\n{os.path.relpath(mp3, REPO)}: {len(wav) / SR / 60:.1f} min")
        return file_checks(mp3, wav)   # (notes, failures)

    def file_checks(mp3, wav):
        """Checks on the finished file: loudness and peaks (audiobook stores ask for about -18 to -23 LUFS and
        peaks below -3 dB), clipping in the raw take, the noise floor, and the length."""
        notes, fails = [], []
        r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", mp3, "-af", "ebur128=peak=true", "-f", "null", "-"],
                           capture_output=True, text=True)
        tail = r.stderr[r.stderr.rfind("Summary:"):]
        lufs = re.search(r"I:\s+(-?[\d.]+) LUFS", tail)
        peak = re.search(r"Peak:\s+(-?[\d.]+) dBFS", tail)
        if lufs:
            v = float(lufs.group(1))
            notes.append(f"loudness {v:.1f} LUFS" + ("" if -23 <= v <= -18 else "  <- FAIL: outside -23..-18"))
            if not -23 <= v <= -18: fails.append("loudness")
        if peak:
            v = float(peak.group(1))
            notes.append(f"true peak {v:.1f} dBFS" + ("" if v <= -3 else "  <- FAIL: above -3"))
            if v > -3: fails.append("true peak")
        clipped = int(np.sum(np.abs(wav) >= 0.999))
        notes.append(f"clipped samples in the raw render: {clipped}" + ("" if clipped < 10 else "  <- FAIL: check for distortion"))
        if clipped >= 10: fails.append("clipping")
        # Noise floor: the quiet stretches inside Chatterbox's own takes only. The pauses this script inserts are
        # exact digital silence (zeros) and are left out, so they can't make the floor look quieter than it is.
        win = int(SR * 0.05)
        frames = wav[: len(wav) // win * win].reshape(-1, win)
        live = frames[np.any(frames != 0, axis=1)]
        if len(live):
            rms = np.sqrt(np.mean(live ** 2, axis=1))
            quiet = rms[rms < np.percentile(rms, 10) * 1.5]
            floor = 20 * np.log10(max(float(np.median(quiet)), 1e-9))
            notes.append(f"noise floor about {floor:.0f} dBFS (gaps inside takes)" + ("" if floor < -55 else "  <- hiss or hum between words? (listen)"))
        return notes, fails

    if not os.path.exists(os.path.join(REFS, "Narrator.wav")):
        sys.exit("Missing Book 1/audiobook/Chatterbox/refs/Narrator.wav (the narrator reference clip).")

    if "--audition" in args:
        notes, fails = write(render(audition(), "audition"), os.path.join(OUT, "audition_cast.mp3" if use_cast else "audition.mp3"))
        tag_mp3(os.path.join(OUT, "audition_cast.mp3" if use_cast else "audition.mp3"), "audition")
        print("; ".join(notes))
        for c in checks:
            print(c)
        return

    chapters = []
    for a in args:
        for part in a.split(","):      # 3   2-10   2,5,9   (and mixes: 1-3,7)
            if re.fullmatch(r"\d+-\d+", part):
                lo, hi = map(int, part.split("-")); chapters += range(lo, hi + 1)
            elif part.isdigit():
                chapters.append(int(part))
    if "--all" in args:   # the whole book: opening credits (00), every chapter, closing credits (99)
        chapters = sorted(int(f[:2]) for f in os.listdir(os.path.join(AB, "Performance")) if re.fullmatch(r"\d\d\.json", f))
    chapters = sorted(set(chapters))
    if not chapters:
        sys.exit("No chapters given: e.g. 1, 2-10, 2,5,9 or --all")
    man_path = os.path.join(OUT, "manifest.json")
    try:
        manifest = json.load(open(man_path))
    except Exception:
        manifest = {}
    for n in chapters:
        src = os.path.join(AB, "Performance", f"{n:02d}.json")
        # everything that changes the sound: the script, this renderer, the name respellings, the cast map,
        # the narrator clip and the run's options
        inputs = [src, __file__, os.path.join(AB, "Lexicon_Alias.pls"), os.path.join(HERE, "cast.py"), ref_for("Narrator")]
        h = hashlib.sha1()
        for f in inputs:
            h.update(open(f, "rb").read())
        h.update(json.dumps({"cast": use_cast, "narrator_ref": narrator_ref}).encode())
        digest = h.hexdigest()
        mp3 = os.path.join(OUT, f"{n:02d}" + ("_" + os.path.splitext(os.path.basename(narrator_ref))[0] if narrator_ref else "") + ".mp3")
        prev = manifest.get(f"{n:02d}")
        prev = prev if isinstance(prev, dict) else {"digest": prev, "status": "UNKNOWN"}
        if "--skip-done" in args and os.path.exists(mp3) and prev.get("digest") == digest and prev.get("status") == "PASS":
            print(f"{n:02d}: up to date and passed, skipped"); continue
        groups = []
        for s in json.load(open(src, encoding="utf-8"))["segments"]:
            if groups and s.get("para") and groups[-1][-1].get("para") == s["para"]:
                groups[-1].append(s)
            else:
                groups.append([s])
        checks.clear(); stats.update(takes=0, passages=0)
        notes, fails = write(render(groups, f"chapter {n}"), mp3)
        print(f"{n:02d}: tagged \"{tag_mp3(mp3, n)}\"")
        doubtful = sum("STILL" in c for c in checks)
        if asr is None:
            status = "UNCHECKED"          # rendered with --no-words: a draft, never skipped as done
        elif doubtful or fails:
            status = "FAIL"
        else:
            status = "PASS"
        reasons = ([f"{doubtful} passage(s) still doubtful"] if doubtful else []) + fails + (["no word check"] if asr is None else [])
        with open(os.path.join(OUT, f"{n:02d}_check.txt"), "w", encoding="utf-8") as fh:
            fh.write(f"Chapter {n} quality check: {status}" + (f" ({', '.join(reasons)})" if reasons else "") + "\n\n"
                     f"Word check: {'on' if asr else 'OFF (install faster-whisper)'}. Passages: {stats['passages']}; takes: {stats['takes']}.\n"
                     f"Still doubtful: {doubtful}. Fixed on a retry: {len(checks) - doubtful}.\n\n"
                     "Finished file:\n" + "\n".join("- " + x for x in notes) + "\n\n"
                     "Passages (listen to every STILL DOUBTFUL one; names are not checked by ear-free tools):\n"
                     + "\n".join(checks) + "\n")
        print(f"{n:02d}: {status}" + (f" ({', '.join(reasons)})" if reasons else "") + f"; {doubtful} doubtful, {len(checks) - doubtful} fixed on retry; " + "; ".join(notes))
        manifest[f"{n:02d}"] = {"digest": digest, "status": status, "reasons": reasons}
        json.dump(manifest, open(man_path, "w"), indent=1)


if __name__ == "__main__":
    main()
