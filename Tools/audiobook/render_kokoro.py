"""Render Book 1 audiobook chapters offline with Kokoro, free.

Licences, by component: the Kokoro-82M model is Apache 2.0; the kokoro-onnx wrapper and espeakng-loader are MIT;
the espeak-ng phonemizer they load is GPL-3.0 (it is a tool here: it doesn't change the licence of the audio).
Kokoro-onnx 0.6.1 needs Python 3.10 to 3.13.

Reads the same per-chapter performance scripts as the ElevenLabs kit (`Book 1/audiobook/Performance/NN.json`),
says names exactly as `Lexicon_IPA.pls` gives them, and follows the Narration Guide as far as Kokoro can: one
narrator voice, whole paragraphs at a time, pace and level set by the kind of words (narration, speech, bond
speech, thought, written words, verse) and the scripted pause after every paragraph. With --cast, each character speaks
in their own voice (kokoro_cast.py: Kokoro voices, blends and pitch), and mood and "how" notes set pace and level.
Kokoro has no true emotion control: feeling comes only from pace, level and pauses (Chatterbox is the route for that).

Setup: `bash Tools/audiobook/kokoro_mac.sh` on a Mac, or by hand:
    python3.12 -m venv ~/kokoro/venv && ~/kokoro/venv/bin/pip install kokoro-onnx==0.6.1 soundfile
    # model files, from https://github.com/thewh1teagle/kokoro-onnx/releases/tag/model-files-v1.0
    #   kokoro-v1.0.onnx and voices-v1.0.bin, into a folder given by --models (default: ~/kokoro)

Use:
    python3 render_kokoro.py --audition                    # audition set: every kind of passage, across the book
    python3 render_kokoro.py --audition --voice bm_george  # the same passages in another voice
    python3 render_kokoro.py 1                             # chapter 1 (00 = opening credits, 99 = closing)
    python3 render_kokoro.py 1-79 --skip-done              # a range, skipping chapters already rendered and current
    python3 render_kokoro.py --all --skip-done             # every chapter, with the opening and closing credits
    python3 render_kokoro.py --audition --cast             # the same passages with the full cast (kokoro_cast.py)
    python3 render_kokoro.py 1 --cast                      # chapter 1 with the full cast -> out/01_cast.mp3
    python3 render_kokoro.py --refs --cast                 # reference clips for Chatterbox, one per cast voice
    python3 render_kokoro.py --voices                      # list the voices

Output: `Book 1/audiobook/Kokoro/out/NN_<voice>.mp3` (ignored by git; never commit the audio). Each file is written
under a temporary name and renamed only when complete. `out/manifest.json` records, for each file, the script it
was made from; --skip-done skips a chapter only if its file exists and its script hasn't changed since.
"""
import hashlib, json, os, re, subprocess, sys, xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
AB = os.path.join(REPO, "Book 1", "audiobook")
SR = 24000

# Pace (Kokoro speed) and level (dB) by kind of words, from the Narration Guide.
STYLE = {
    "title":     (1.00, 0.0),
    "narration": (1.00, 0.0),
    "speech":    (1.00, 0.0),
    "bond":      (0.90, -3.0),   # closer and quieter than speech, slightly slow
    "thought":   (0.92, -4.5),   # quieter still
    "remembered": (0.92, -4.5),
    "written":   (0.88, -1.0),   # slower, plainer
    "verse":     (0.86, -1.0),
}


VOWELS = set("aeiouyæɑɒɔəɛɜɪʊʌɐ")


def to_kokoro(ipa):
    """Standard IPA from Lexicon_IPA.pls -> the phoneme style Kokoro's British voices were trained on."""
    # æ -> a: Kokoro's British voices use "a" for the TRAP vowel (its G2P writes "cat" as kˈat in en-gb, as
    # espeak does: see "Raske" -> ɹˈask). Keeping æ would give the American vowel in a British voice.
    ipa = ipa.replace("r", "ɹ").replace("æ", "a").replace(".", "")
    out, pending = [], ""
    for ch in ipa:                      # stress marks go right before the stressed vowel (mˈɛəɹən)
        if ch in "ˈˌ":
            pending = ch
        elif pending and ch in VOWELS:
            out.append(pending + ch); pending = ""
        else:
            out.append(ch)
    return "".join(out)


def lexicon():
    """Names -> Kokoro phonemes, from the IPA lexicon (exact), longest names first."""
    ns = {"p": "http://www.w3.org/2005/01/pronunciation-lexicon"}
    names = {}
    for lx in ET.parse(os.path.join(AB, "Lexicon_IPA.pls")).getroot().findall("p:lexeme", ns):
        g, ph = lx.find("p:grapheme", ns), lx.find("p:phoneme", ns)
        if g is not None and ph is not None and ph.text:
            names[g.text] = to_kokoro(ph.text)
    order = sorted(names, key=len, reverse=True)
    rx = re.compile(r"\b(" + "|".join(re.escape(n) for n in order) + r")(['’]s)?\b")
    return names, rx


def clean(text):
    text = re.sub(r"[*_]", "", text)
    return text.replace("‘", "'").replace("“", '"').replace("”", '"').strip()


def phonemes(k, text, lang, lex):
    """Phonemize text, putting each lexicon name in as its exact IPA."""
    names, rx = lex
    out, pos = [], 0
    for m in rx.finditer(text):
        if m.start() > pos:
            out.append(k.tokenizer.phonemize(text[pos:m.start()], lang))
        ph = names[m.group(1)]
        if m.group(2):  # possessive: /ɪz/ after a sibilant (Kesh's), /s/ after a voiceless sound, else /z/
            ph += "ɪz" if re.search(r"(s|z|ʃ|ʒ|tʃ|dʒ)$", ph) else ("s" if ph[-1] in "ptkfθ" else "z")
        out.append(ph)
        pos = m.end()
    if pos < len(text):
        out.append(k.tokenizer.phonemize(text[pos:], lang))
    return re.sub(r"\s+", " ", " ".join(x.strip() for x in out if x.strip())).replace(" ,", ",").replace(" .", ".")


def gentle_trim(audio, keep=0.12):
    """Kokoro's own trim clips the last consonant ("Two Bank"). Render untrimmed, then cut only true silence,
    keeping a margin either side."""
    import numpy as np
    e = np.abs(audio)
    loud = np.where(e > e.max() * 0.01)[0] if len(e) else []
    if not len(loud):
        return audio
    m = int(SR * keep)
    return audio[max(0, loud[0] - m): loud[-1] + m]


TITLE_BEAT = 1.0   # seconds between "Part One" and "Two Banks", "Chapter One" and "The Unchosen Yard"


def title_pieces(text):
    """A title line is said as separate lines with a beat between: "Part One" / "Two Banks"."""
    return [p.strip() for p in re.split(r"(?<=\.)\s+", text) if p.strip()]


def kind(seg):
    t = seg.get("type", "narration")
    return t if t in STYLE else "narration"


def main():
    args = sys.argv[1:]
    models = os.path.expanduser(args[args.index("--models") + 1]) if "--models" in args else os.path.expanduser("~/kokoro")
    voice = args[args.index("--voice") + 1] if "--voice" in args else "bf_emma"
    lang = "en-us" if voice.startswith("a") else "en-gb"
    from kokoro_onnx import Kokoro
    import numpy as np
    k = Kokoro(os.path.join(models, "kokoro-v1.0.onnx"), os.path.join(models, "voices-v1.0.bin"))
    if "--voices" in args:
        print(" ".join(sorted(k.get_voices()))); return
    skip = {a for i, a in enumerate(args) if i and args[i - 1] in ("--models", "--voice")}
    chapters = []
    for a in args:
        if a in skip or a.startswith("--"):
            continue
        if re.fullmatch(r"\d+-\d+", a):
            lo, hi = map(int, a.split("-")); chapters += range(lo, hi + 1)
        elif a.isdigit():
            chapters.append(int(a))
    if "--all" in args:
        chapters = sorted(int(f[:2]) for f in os.listdir(os.path.join(AB, "Performance")) if f[:2].isdigit())
    lex = lexicon()
    out_dir = os.path.join(AB, "Kokoro", "out")
    os.makedirs(out_dir, exist_ok=True)
    man_path = os.path.join(out_dir, "manifest.json")
    try:
        manifest = json.load(open(man_path))
    except Exception:
        manifest = {}

    def paragraphs(segs):
        # Read whole paragraphs, not line by line: Kokoro phrases a sentence well only when it sees all of it.
        paras = []
        for s in segs:
            if paras and s.get("para") and paras[-1][0] == s["para"]:
                paras[-1][1].append(s)
            else:
                paras.append((s.get("para") or None, [s]))
        return [g for _, g in paras]

    use_cast = "--cast" in args
    if use_cast:
        import cast as castmap, kokoro_cast as kc
        styles = {}

        def style_vec(spec):
            if spec not in styles:
                vec = None
                for term in spec.split("+"):
                    name, _, w = term.partition("*")
                    v = k.get_voice_style(name.strip()) * float(w or 1)
                    vec = v if vec is None else vec + v
                styles[spec] = vec.astype(np.float32)
            return styles[spec]

        def shift(audio, semitones):
            if not semitones:
                return audio
            f = 2 ** (semitones / 12)
            r = subprocess.run(["ffmpeg", "-loglevel", "error", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "pipe:0",
                                "-af", f"asetrate={SR * f:.0f},aresample={SR},atempo={1 / f:.5f}", "-f", "f32le", "pipe:1"],
                               input=audio.astype(np.float32).tobytes(), capture_output=True, check=True)
            return np.frombuffer(r.stdout, dtype=np.float32)

        def runs(group):
            """Split a paragraph into runs read by one voice: characters speak their own lines (speech and bond
            speech); the narrator reads the rest, thoughts and written words included."""
            out = []
            for sg in group:
                role = castmap.role_of(sg["speaker"]) if sg.get("speaker") and kind(sg) in ("speech", "bond") else "Narrator"
                if out and out[-1][0] == role and kind(out[-1][1][-1]) == kind(sg):
                    out[-1][1].append(sg)
                else:
                    out.append((role, [sg]))
            return out

    def render(groups, label):
        if use_cast:
            return render_cast(groups, label)
        parts = []
        for i, group in enumerate(groups):
            text = " ".join(t for t in (clean(s["text"]) for s in group) if t)
            kinds = {kind(s) for s in group}
            style = kinds.pop() if len(kinds) == 1 else "narration"   # a special style only if the whole paragraph is that kind
            speed, db = STYLE[style]
            pieces = title_pieces(text) if style == "title" else [text]
            for j, piece in enumerate(pieces):
                audio, _ = k.create(phonemes(k, piece, lang, lex), voice=voice, speed=speed, lang=lang, is_phonemes=True,
                                    trim=False)
                parts.append(gentle_trim(np.asarray(audio, dtype=np.float32)) * (10 ** (db / 20)))
                if j < len(pieces) - 1:
                    parts.append(np.zeros(int(SR * TITLE_BEAT), dtype=np.float32))
            parts.append(np.zeros(int(SR * group[-1].get("pause_after_ms", 300) / 1000), dtype=np.float32))
            print(f"\r{label}: {i + 1}/{len(groups)}", end="", flush=True)
        return np.concatenate(parts)

    def render_cast(groups, label):
        parts = []
        for i, group in enumerate(groups):
            rs = runs(group)
            for j, (role, segs) in enumerate(rs):
                text = " ".join(t for t in (clean(x["text"]) for x in segs) if t)
                if not text:
                    continue
                style = kind(segs[0])
                spec, pitch, cspeed, cgain = kc.voice_for(role)
                mspeed, mgain = kc.shaping(segs[0].get("mood"), " ".join(x.get("how") or "" for x in segs))
                base_speed, base_gain = STYLE[style]
                speed = max(0.85, min(1.12, base_speed * cspeed * mspeed))
                gain = max(-6.0, min(2.0, base_gain + cgain + mgain))
                pieces = title_pieces(text) if style == "title" else [text]
                for q, piece in enumerate(pieces):
                    audio, _ = k.create(phonemes(k, piece, "en-gb", lex), voice=style_vec(spec), speed=speed,
                                        lang="en-gb", is_phonemes=True, trim=False)
                    parts.append(shift(gentle_trim(np.asarray(audio, dtype=np.float32)), pitch) * (10 ** (gain / 20)))
                    if q < len(pieces) - 1:
                        parts.append(np.zeros(int(SR * TITLE_BEAT), dtype=np.float32))
                if j < len(rs) - 1:
                    parts.append(np.zeros(int(SR * 0.15), dtype=np.float32))
            parts.append(np.zeros(int(SR * group[-1].get("pause_after_ms", 300) / 1000), dtype=np.float32))
            print(f"\r{label}: {i + 1}/{len(groups)}", end="", flush=True)
        return np.concatenate(parts)

    tag = "cast" if use_cast else voice

    def write(wav, mp3):
        tmp = mp3 + ".f32"
        wav.tofile(tmp)
        partial = mp3[:-4] + ".partial.mp3"
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", tmp,
                        "-af", "loudnorm=I=-19:TP=-3:LRA=11", "-ar", "44100", "-b:a", "128k", partial], check=True)
        os.remove(tmp)
        os.replace(partial, mp3)   # only a finished file gets the real name
        print(f"\n{os.path.relpath(mp3, REPO)}: {len(wav) / SR / 60:.1f} min")

    if "--refs" in args:
        # Reference clips for Chatterbox: each cast voice reading the same neutral lines (about 12 seconds),
        # so Chatterbox clones the Kokoro cast and the two can be compared role for role.
        import kokoro_cast as kc
        if not use_cast:
            sys.exit("--refs needs --cast")
        ref_dir = os.path.join(AB, "Chatterbox", "refs")
        os.makedirs(ref_dir, exist_ok=True)
        line = ("The river ran high that spring, and the ferry crossed twice a day. Nobody on either bank could "
                "remember a quieter year, and nobody trusted it. They said so, too, over the rail.")
        import soundfile as sf
        for role, (spec, pitch, cspeed, cgain) in kc.CAST.items():
            audio, _ = k.create(phonemes(k, line, "en-gb", lex), voice=style_vec(spec), speed=cspeed, lang="en-gb", is_phonemes=True)
            sf.write(os.path.join(ref_dir, role.replace(" ", "_") + ".wav"), shift(np.asarray(audio, dtype=np.float32), pitch), SR)
            print("ref", role)
        return

    if "--audition" in args:
        write(render(audition(), "audition"), os.path.join(out_dir, f"audition_{tag}.mp3"))
        return

    for n in chapters:
        src = os.path.join(AB, "Performance", f"{n:02d}.json")
        key = f"{n:02d}_{tag}"
        digest = hashlib.sha1(open(src, "rb").read() + open(__file__, "rb").read() + (open(os.path.join(HERE, "kokoro_cast.py"), "rb").read() if use_cast else b"")).hexdigest()
        mp3 = os.path.join(out_dir, key + ".mp3")
        if "--skip-done" in args and os.path.exists(mp3) and manifest.get(key) == digest:
            print(f"{key}: up to date, skipped"); continue
        write(render(paragraphs(json.load(open(src, encoding="utf-8"))["segments"]), f"chapter {n}"), mp3)
        manifest[key] = digest
        json.dump(manifest, open(man_path, "w"), indent=1)


def audition():
    """A few minutes that cover every kind of passage, drawn from across the book: plain narration, a long
    paragraph, a very short line, dialogue, bond speech, inner thought, remembered words, grief, tension, verse
    and written words. Same passages for every voice, so voices can be compared like for like."""
    picks, seen = [], set()
    want = [("title", None), ("narration", None), ("long", None), ("short", None), ("speech", None),
            ("bond", None), ("thought", None), ("remembered", None), ("narration", "grief"),
            ("narration", "tension"), ("verse", None), ("written", None), ("bond", "grief")]
    files = sorted(f for f in os.listdir(os.path.join(AB, "Performance")) if f[:2].isdigit() and f[:2] not in ("00", "99"))
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


if __name__ == "__main__":
    main()
