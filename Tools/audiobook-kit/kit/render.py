"""Render audiobook chapters with Chatterbox (Resemble AI, MIT licence): free, and offline after the first download.
Part of the audiobook kit: run it through `audiobook.sh`, which sets things up and offers the menu.

It reads the reading scripts (`<book>/audiobook/Performance/NN.json`, made from the chapters by prepare.py, or a folder of
ready-made scripts named in book.json) and writes `<book>/audiobook/out/NN.mp3`.
- One narrator reads everything, cloned from a short reference clip (book.json "narrator"; default the kit's
  voices/narrator.wav). Each paragraph is read whole; long ones are split at sentence ends (about 200 characters).
- Where a script gives a mood or a "how" note, it sets Chatterbox's emotion intensity; thought, bond speech and verse
  are read a little quieter and slower.
- Names are respelt from the book's pronunciation file (book.json "names": a .pls lexicon or a name,respelling .csv).
- Automatic checks on every take, before it is kept: its length against its text, no silence over two seconds inside
  it, and its words (Whisper transcribes the take and it is compared word for word with the script; names count as
  matching). A take that fails is made again, up to three tries (six for a line of three words or fewer). Each finished chapter is checked for loudness, true
  peak, clipping and noise floor, and gets PASS, FAIL (with reasons) or UNCHECKED (--no-verify) in out/NN_check.txt
  and out/manifest.json. --skip-done skips chapters that passed with unchanged inputs.
- None of this replaces listening: names, emphasis and feeling need an ear, starting with STILL DOUBTFUL passages.
- Chatterbox adds an inaudible Perth watermark to its output (Resemble AI's responsible-AI marker).

Use:  render.py 7 | 2-10 | 2,5,9 | --all   [--no-verify] [--skip-done] [--audition] [--book DIR]
"""
import hashlib, json, os, re, subprocess, sys, xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import config as cfg          # noqa: E402
import prepare                 # noqa: E402

REPO = cfg.BOOK
AB = cfg.AUDIO
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
    files = sorted(f for f in os.listdir(cfg.SCRIPTS) if f.endswith(".json") and f[:2].isdigit() and f[:2] not in ("00", "99"))
    groups = []
    for f in files:
        segs = json.load(open(os.path.join(cfg.SCRIPTS, f), encoding="utf-8"))["segments"]
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
OUT = cfg.OUT

# mood -> (exaggeration, cfg_weight). Higher exaggeration = more feeling; lower cfg = slower, more deliberate.
MOOD = {
    None: (0.50, 0.50), "tension": (0.60, 0.50), "dread": (0.60, 0.40), "grief": (0.70, 0.30),
    "quiet": (0.40, 0.45), "reflective": (0.45, 0.45), "tender": (0.50, 0.40), "humour": (0.60, 0.50),
    "anger": (0.80, 0.40), "awe": (0.60, 0.35), "urgent": (0.75, 0.55), "action": (0.70, 0.55),
}
HOW = [("shout", 0.25, 3), ("roar", 0.30, 4), ("loud", 0.15, 2), ("whisper", -0.15, -6), ("very quiet", -0.10, -5),
       ("quiet", -0.05, -3), ("soft", -0.05, -2.5), ("low", -0.05, -2), ("faint", -0.10, -5), ("weak", -0.10, -4),
       ("cracking", 0.20, -1), ("shaking", 0.15, -1), ("eager", 0.15, 0), ("urgent", 0.15, 0.5),
       ("called", 0.10, 1), ("sharp", 0.10, 1), ("hoarse", 0.0, -1.5), ("rasp", 0.0, -1.5), ("gentl", -0.05, -2),
       ("small", -0.05, -3)]
GAIN = {"bond": -3.0, "thought": -4.5, "remembered": -4.5, "written": -1.0, "verse": -1.0}
TEMPO = {"bond": 0.95, "thought": 0.97, "remembered": 0.97, "verse": 0.94, "written": 0.95, "title": 0.95}


def name_pairs():
    """(name, respelling) pairs from the book's pronunciation file: a .pls lexicon with aliases, or a .csv."""
    p = cfg.NAMES
    pairs = []
    if p and os.path.exists(p):
        if p.lower().endswith(".pls"):
            ns = {"p": "http://www.w3.org/2005/01/pronunciation-lexicon"}
            for lx in ET.parse(p).getroot().findall("p:lexeme", ns):
                g, al = lx.find("p:grapheme", ns), lx.find("p:alias", ns)
                if g is not None and g.text:
                    pairs.append((g.text, al.text if al is not None and al.text else ""))
        else:
            import csv
            for row in csv.reader(open(p, encoding="utf-8")):
                if row and row[0].strip() and not row[0].startswith("#") and row[0].strip() != "Name":
                    pairs.append((row[0].strip(), row[1].strip() if len(row) > 1 else ""))
    return pairs


def aliases():
    pairs = sorted(((g, a) for g, a in name_pairs() if a), key=lambda x: -len(x[0]))
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
    # contractions spelt out and possessives dropped, so "would've" and "would have", "Haverly's" and "Haverly"
    # compare equal (a recogniser writes them either way)
    text = re.sub(r"\bwon't\b", "will not", text)
    text = re.sub(r"\bcan't\b", "can not", text)
    text = re.sub(r"\bshan't\b", "shall not", text)
    text = re.sub(r"n't\b", " not", text)
    # the words hidden in a contraction are optional ("~"): "he'd decided" matches "he had decided", "he would
    # decide" and "he decided" (a recogniser often drops them, and "'d" can be had or would)
    for c, full in (("'ve", " ~have"), ("'ll", " ~will"), ("'re", " ~are"), ("'m", " ~am"), ("'d", " ~d")):
        text = re.sub(re.escape(c) + r"\b", full, text)
    text = re.sub(r"'s\b", "", text)
    text = re.sub(r"\balright\b", "all right", text)
    text = re.sub(r"(^|\s)'?til\b", r"\1till", text)
    text = re.sub(r"\bokay\b", "ok", text)
    words = [w.replace("'", "") for w in re.findall(r"~?[a-z']+", text) if w.replace("'", "").strip("~")]
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


_SOUND_ALIKE = [set(x.split()) for x in ("to two too", "for four fore", "there their theyre", "no know", "right write",
                                            "hear here", "by buy bye", "one won", "eight ate", "new knew", "so sew sow",
                                            "whole hole", "would wood", "through threw", "sea see", "son sun", "way weigh",
                                            "allowed aloud", "mist missed", "past passed", "board bored", "court caught",
                                            "knight night", "knights nights", "rode road rowed", "reined rained reigned",
                                            "tail tale", "wait weight", "bear bare", "flour flower", "mail male")]


def same_word(a, b):
    """Equal, or near enough to be a spelling variant (Ottery's / Otterys / Otteries): same first letter and at
    most one edit per three letters; or words that sound the same (two / to). Short words must match exactly."""
    if a == b:
        return True
    if a.startswith("~") or b.startswith("~"):          # an optional word from a contraction
        x, y = (a, b) if a.startswith("~") else (b, a)
        return y.lstrip("~") in ({"would", "had", "did"} if x == "~d" else {x[1:]})
    if any(a in g and b in g for g in _SOUND_ALIKE):
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


# What changes the sound of a chapter, besides its script, its respellings and the narrator: bump this only when a
# change to the renderer would make finished chapters sound different (the model, its settings, the pauses, the
# levelling, how text is cut into pieces). Changes to the checks or the number of retakes don't: a chapter that
# passed the checks of its day, or that someone listened to and accepted, is kept. (The renderer's own file isn't used: a fix to
# the checks or the menu must not make days of finished chapters look out of date.)
RENDER_VERSION = "chatterbox 0.1.7 / render 3"


def name_words():
    """Names (and their respellings) from the pronunciation file, and the author's name: a recogniser can't be
    expected to spell them, so they count as matching whatever word was heard in their place. Each chapter's script
    adds its own names."""
    words = set()
    for g, a in name_pairs():
        words.update(norm_words(g)); words.update(norm_words(a))
    words.update(norm_words(cfg.AUTHOR or ""))
    return words


def join_split(hyp, ref):
    """A recogniser often writes one word as two ("Goodluck" as "good luck", "hearthstone" as "hearth stone"): join
    two heard words whose letters make a word of the script."""
    want, out, i = set(ref), [], 0
    while i < len(hyp):
        if i + 1 < len(hyp) and hyp[i] + hyp[i + 1] in want:
            out.append(hyp[i] + hyp[i + 1]); i += 2
            continue
        w = hyp[i]
        # and the other way: one heard word for two written ("goodnight" for "good knight")
        if w not in want and len(w) >= 6:
            for k in range(2, len(w) - 1):
                a, b = w[:k], w[k:]
                ok = lambda x: x in want or any(x in g and g & want for g in _SOUND_ALIKE)
                if ok(a) and ok(b):
                    out += [a, b]; break
            else:
                out.append(w)
        else:
            out.append(w)
        i += 1
    return out


def word_errors(ref, hyp, wild):
    """Word-level edit distance between the script (ref) and what was heard (hyp); script words in `wild` (names)
    match any one heard word. Returns (errors, details) where details lists what went wrong."""
    n, m = len(ref), len(hyp)
    dc = [0 if w.startswith("~") else 1 for w in ref]      # optional words cost nothing to leave out
    ic = [0 if w.startswith("~") else 1 for w in hyp]
    d = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        d[i][0] = d[i - 1][0] + dc[i - 1]
    for j in range(1, m + 1):
        d[0][j] = d[0][j - 1] + ic[j - 1]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            same = same_word(ref[i - 1], hyp[j - 1]) or ref[i - 1] in wild
            d[i][j] = min(d[i - 1][j] + dc[i - 1], d[i][j - 1] + ic[j - 1], d[i - 1][j - 1] + (0 if same else 1))
    # walk back for a short list of what differed
    i, j, out = n, m, []
    while i > 0 or j > 0:
        same = i > 0 and j > 0 and (same_word(ref[i - 1], hyp[j - 1]) or ref[i - 1] in wild)
        if i > 0 and j > 0 and d[i][j] == d[i - 1][j - 1] + (0 if same else 1):
            if not same:
                out.append(f"'{ref[i - 1]}'->'{hyp[j - 1]}'")
            i, j = i - 1, j - 1
        elif i > 0 and d[i][j] == d[i - 1][j] + dc[i - 1]:
            if dc[i - 1]:
                out.append(f"missing '{ref[i - 1]}'")
            i -= 1
        else:
            if ic[j - 1]:
                out.append(f"extra '{hyp[j - 1]}'")
            j -= 1
    return d[n][m], list(reversed(out))

BOOK_TITLE, BOOK_AUTHOR = cfg.TITLE, cfg.AUTHOR
SCRIPT_OF = cfg.script_path
ALL_CHAPTERS = cfg.chapter_numbers


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


def word_doubt(reason):
    """True for a failure about the words (which a listener can overrule), not a technical one (loudness, true peak,
    clipping, a measurement that failed), which needs fixing, not accepting."""
    return bool(re.search(r"passage\(s\) still doubtful|place\(s\) where the words differ|accepted after listening", reason))


def accept(args):
    """--accept 7 | 2-10: after listening to a chapter's doubtful lines and finding them right, mark it PASS, so a
    resumed build keeps it. Rendering it again (or changing its script) clears this."""
    man_path = os.path.join(OUT, "manifest.json")
    try:
        manifest = json.load(open(man_path))
    except Exception:
        manifest = {}
    for n in sorted(set(chapter_list(args))):
        e = manifest.get(f"{n:02d}")
        if not isinstance(e, dict) or not os.path.exists(os.path.join(OUT, f"{n:02d}.mp3")):
            print(f"{n:02d}: not built yet, nothing to accept"); continue
        if e.get("status") == "UNCHECKED":
            print(f"{n:02d}: built without verifying (a draft); build it verified, or verify it (option 7), first"); continue
        technical = [r for r in e.get("reasons", []) if not word_doubt(r)]
        if technical:
            print(f"{n:02d}: not accepted: it fails a technical check ({', '.join(technical)}), which listening can't"
                  " overrule. Build it again."); continue
        e.update(status="PASS", reasons=["accepted after listening"] + [r for r in e.get("reasons", []) if r != "accepted after listening"])
        manifest[f"{n:02d}"] = e
        import datetime
        note = (f"ACCEPTED after listening ({datetime.date.today().isoformat()}): the chapter now counts as PASS."
                " The report below is from the automatic check, kept as it was.\n\n")
        for rep_name in (f"{n:02d}_check.txt", f"{n:02d}_verify.txt"):
            rp = os.path.join(OUT, rep_name)
            if os.path.exists(rp):
                old = open(rp, encoding="utf-8").read()
                if not old.startswith("ACCEPTED"):
                    open(rp, "w", encoding="utf-8").write(note + old)
        print(f"{n:02d}: accepted (PASS); a resumed build will keep it")
    json.dump(manifest, open(man_path, "w"), indent=1)


def retag(args):
    """--retag 1 | 2-10 | --all: put the titles into chapters already built, without rendering them again."""
    prepare.main(quiet=True)          # the titles come from the reading scripts: make them first
    nums = sorted(set(ALL_CHAPTERS() if "--all" in args else chapter_list(args)))
    if not ALL_CHAPTERS():
        sys.exit(f"No reading scripts in {cfg.SCRIPTS}, so there are no titles to write. Check the chapters folder in {cfg.CONF}.")
    done = 0
    for n in nums:
        mp3 = os.path.join(OUT, f"{n:02d}.mp3")
        if not os.path.exists(mp3):
            continue
        if n != "audition" and not os.path.exists(SCRIPT_OF(n)):
            print(f"{n:02d}: no reading script for this chapter, so its title is unknown; left as it is"); continue
        print(f"{n:02d}: {tag_mp3(mp3, n)}"); done += 1
    print(f"Tagged {done} file(s) in {OUT}.")


def main():
    args = sys.argv[1:]
    if "--retag" in args:
        return retag([a for a in args if a != "--retag"])
    if "--accept" in args:
        return accept([a for a in args if a != "--accept"])
    use_cast = False              # one narrator reads everything
    prepare.main(quiet=True)      # make or refresh the scripts from the chapters
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
                     "Fix it (bash audiobook-kit/audiobook.sh sets it up), or build without verifying (menu options 2, 4, 6).")
    else:
        print("verify: OFF (--no-verify): one take per passage, no word check; chapters are marked UNCHECKED (a draft)")
    BASE_NAMES = name_words()
    WILD = set(BASE_NAMES)
    MAX_WER = 0.12   # more than about 1 word in 8 wrong (names excluded) -> another take
    SR = model.sr
    subs = aliases()
    os.makedirs(OUT, exist_ok=True)
    conds = {}
    checks = []
    stats = {"takes": 0, "passages": 0, "flat": 0}

    narrator_ref = args[args.index("--narrator-ref") + 1] if "--narrator-ref" in args else None

    def ref_for(role):
        if narrator_ref:
            return narrator_ref if os.path.isabs(narrator_ref) else os.path.join(cfg.BOOK, narrator_ref)
        return cfg.NARRATOR

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

    def heard(audio, short=False):
        """What the recogniser hears in a take (16 kHz for Whisper). A short take gets half a second of silence at
        each end and a more careful search: on a clip of a second or so, Whisper otherwise often mishears."""
        x = np.interp(np.arange(0, len(audio), SR / 16000), np.arange(len(audio)), audio).astype(np.float32)
        if short:
            pad = np.zeros(8000, dtype=np.float32)
            x = np.concatenate([pad, x, pad])
        segs, _ = asr.transcribe(x, language="en", beam_size=5 if short else 1, vad_filter=False,
                                 condition_on_previous_text=False)
        return " ".join(sg.text for sg in segs)

    def word_problem(audio, text):
        """Compare the words heard with the words written. Returns (why or None, error rate, details)."""
        if asr is None:
            return None, 0.0, []
        ref = norm_words(text)
        hyp = join_split(norm_words(heard(audio, short=len(ref) <= 3)), ref)
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
        # very short lines (three words or fewer) are the ones that go wrong most: up to six tries for those
        tries = TRIES if TRIES == 1 or len(norm_words(text)) > 3 else 2 * TRIES
        for attempt in range(tries):
            wav = model.generate(text, exaggeration=exaggeration, cfg_weight=cfg)
            audio = wav.squeeze(0).cpu().numpy().astype(np.float32)
            # Chatterbox's own take, before any volume change: flat tops (three or more samples in a row at full
            # scale) are real distortion. (Loud lines are turned up later in floating point and levelled down
            # again, which can't distort, so they aren't counted.)
            flat = 0
            hot = np.abs(audio) >= 0.999
            if hot.any():
                runs = np.diff(np.concatenate(([0], hot.astype(np.int8), [0])))
                lengths = np.flatnonzero(runs == -1) - np.flatnonzero(runs == 1)
                flat = int(np.sum(lengths >= 3))
            why = problem(audio, text)          # length and silence
            rate = 0.0
            if why is None:
                why, rate, _ = word_problem(audio, text)   # the words themselves
            takes.append((why, rate, audio, flat))
            stats["takes"] += 1
            if why is None:
                break
        expect = len(text) / CHARS_PER_SEC
        why, rate, audio, flat = min(takes, key=lambda t: (t[0] is not None, t[1], abs(len(t[2]) / SR - expect)))
        stats["flat"] += flat              # only the take that goes into the chapter counts
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
            role = "Narrator"
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
        if not lufs or not peak:
            notes.append("loudness or true peak couldn't be measured  <- FAIL: check the file plays")
            fails.append("not measurable")
        if lufs:
            v = float(lufs.group(1))
            notes.append(f"loudness {v:.1f} LUFS" + ("" if -23 <= v <= -18 else "  <- FAIL: outside -23..-18"))
            if not -23 <= v <= -18: fails.append("loudness")
        if peak:
            v = float(peak.group(1))
            notes.append(f"true peak {v:.1f} dBFS" + ("" if v <= -3 else "  <- FAIL: above -3"))
            if v > -3: fails.append("true peak")
        # clipping: in the finished file (decoded), and flat tops in Chatterbox's own takes
        raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", mp3, "-ac", "1", "-f", "f32le", "-"],
                             capture_output=True, check=True).stdout
        clipped = int(np.sum(np.abs(np.frombuffer(raw, dtype=np.float32)) >= 0.999))
        flat = stats.get("flat", 0)
        notes.append(f"clipped samples in the finished file: {clipped}; flat-topped peaks in the takes: {flat}"
                     + ("" if clipped < 10 and flat < 5 else "  <- FAIL: listen for distortion"))
        if clipped >= 10 or flat >= 5: fails.append("clipping")
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

    if not os.path.exists(ref_for("Narrator")):
        sys.exit(f"Missing the narrator's reference clip: {ref_for('Narrator')} (set \"narrator\" in {cfg.CONF}).")

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
        chapters = cfg.chapter_numbers()
    chapters = sorted(set(chapters))
    if not chapters:
        sys.exit("No chapters given: e.g. 1, 2-10, 2,5,9 or --all")
    man_path = os.path.join(OUT, "manifest.json")
    try:
        manifest = json.load(open(man_path))
    except Exception:
        manifest = {}
    for n in chapters:
        src = cfg.script_path(n)
        if not os.path.exists(src):
            print(f"{n:02d}: no script (no such chapter), skipped"); continue
        # everything that changes the sound, and nothing else: the script's segments, the name respellings, the
        # narrator clip, the renderer's sound version and the run's options. (Not the files themselves: the kit
        # adds bookkeeping to scripts and new names to the lexicon, and those mustn't make a chapter look changed.)
        h = hashlib.sha1()
        h.update(json.dumps(json.load(open(src, encoding="utf-8"))["segments"], sort_keys=True, ensure_ascii=False).encode())
        h.update(json.dumps(sorted([g, a] for g, a in name_pairs() if a), ensure_ascii=False).encode())
        h.update(open(ref_for("Narrator"), "rb").read())
        h.update(json.dumps({"cast": use_cast, "narrator_ref": narrator_ref, "render": RENDER_VERSION}).encode())
        digest = h.hexdigest()
        mp3 = os.path.join(OUT, f"{n:02d}.mp3")
        prev = manifest.get(f"{n:02d}")
        prev = prev if isinstance(prev, dict) else {"digest": prev, "status": "UNKNOWN"}
        if "--skip-done" in args and os.path.exists(mp3) and prev.get("digest") == digest and prev.get("status") == "PASS":
            print(f"{n:02d}: up to date and passed, skipped"); continue
        script = json.load(open(src, encoding="utf-8"))
        WILD.clear(); WILD.update(BASE_NAMES | set(script.get("names", [])))
        if n in (0, 99):          # the credits: the book's own title and series are names here
            WILD.update(norm_words(cfg.TITLE + " " + cfg.SERIES))
        groups = []
        for s in script["segments"]:
            if groups and s.get("para") and groups[-1][-1].get("para") == s["para"]:
                groups[-1].append(s)
            else:
                groups.append([s])
        checks.clear(); stats.update(takes=0, passages=0, flat=0)
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
