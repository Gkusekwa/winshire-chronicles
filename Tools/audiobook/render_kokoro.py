"""Render Book 1 audiobook chapters with Kokoro (open source, Apache 2.0), free and offline.

Reads the same per-chapter performance scripts as the ElevenLabs kit (`Book 1/audiobook/Performance/NN.json`),
says names exactly as `Lexicon_IPA.pls` gives them, and follows the Narration Guide: one narrator voice, with pace and
level set by the kind of words (narration, speech, bond speech, thought, written words and verse) and the
scripted pause after every segment.

Setup (once):
    pip install kokoro-onnx soundfile
    # model files, from https://github.com/thewh1teagle/kokoro-onnx/releases/tag/model-files-v1.0
    #   kokoro-v1.0.onnx and voices-v1.0.bin, into a folder given by --models (default: ~/kokoro)

Use:
    python3 render_kokoro.py 1                 # chapter 1 with the default voice
    python3 render_kokoro.py 1 2 3 --voice bm_george
    python3 render_kokoro.py 1 --limit 20      # first 20 segments only (a quick sample)
    python3 render_kokoro.py 1-79 --skip-done  # a range; skip chapters already rendered (resume after a stop)
    python3 render_kokoro.py --all             # every chapter
    python3 render_kokoro.py --voices          # list the voices

Output: `Book 1/audiobook/Kokoro/out/NN_<voice>.mp3` (ignored by git; never commit the audio).
"""
import json, os, re, subprocess, sys, xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
AB = os.path.join(REPO, "Book 1", "audiobook")
SR = 24000

# Pace (Kokoro speed) and level (dB) by kind of words, from the Narration Guide.
STYLE = {
    "title":     (0.90, 0.0),
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
    ipa = ipa.replace("r", "ɹ").replace("æ", "a").replace("ɡ", "ɡ").replace(".", "")
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
        out.append(ph + (("s" if ph[-1] in "ptkfθ" else "z") if m.group(2) else ""))
        pos = m.end()
    if pos < len(text):
        out.append(k.tokenizer.phonemize(text[pos:], lang))
    return re.sub(r"\s+", " ", " ".join(x.strip() for x in out if x.strip())).replace(" ,", ",").replace(" .", ".")


def kind(seg):
    t = seg.get("type", "narration")
    return t if t in STYLE else "narration"


def main():
    args = sys.argv[1:]
    models = os.path.expanduser(args[args.index("--models") + 1]) if "--models" in args else os.path.expanduser("~/kokoro")
    voice = args[args.index("--voice") + 1] if "--voice" in args else "bf_emma"
    lang = "en-us" if voice.startswith("a") else "en-gb"
    limit = int(args[args.index("--limit") + 1]) if "--limit" in args else None
    from kokoro_onnx import Kokoro
    import numpy as np
    k = Kokoro(os.path.join(models, "kokoro-v1.0.onnx"), os.path.join(models, "voices-v1.0.bin"))
    if "--voices" in args:
        print(" ".join(sorted(k.get_voices()))); return
    skip = {a for i, a in enumerate(args) if i and args[i - 1] in ("--models", "--voice", "--limit")}
    chapters = []
    for a in args:
        if a in skip or a.startswith("--"):
            continue
        if re.fullmatch(r"\d+-\d+", a):
            lo, hi = map(int, a.split("-")); chapters += range(lo, hi + 1)
        elif a.isdigit():
            chapters.append(int(a))
    if "--all" in args:
        chapters = sorted(int(f[:2]) for f in os.listdir(os.path.join(AB, "Performance")) if f[:2].isdigit() and 1 <= int(f[:2]) <= 98)
    if "--skip-done" in args:
        chapters = [n for n in chapters if not os.path.exists(os.path.join(AB, "Kokoro", "out", f"{n:02d}_{voice}.mp3"))]
    lex = lexicon()
    out_dir = os.path.join(AB, "Kokoro", "out")
    os.makedirs(out_dir, exist_ok=True)
    for n in chapters:
        perf = json.load(open(os.path.join(AB, "Performance", f"{n:02d}.json"), encoding="utf-8"))
        segs = perf["segments"][:limit] if limit else perf["segments"]
        # Read whole paragraphs, not line by line: Kokoro phrases a sentence well only when it sees all of it.
        # A paragraph takes a special style (bond speech, thought, verse...) only when all of it is that kind.
        paras = []
        for s in segs:
            if paras and s.get("para") and paras[-1][0] == s["para"]:
                paras[-1][1].append(s)
            else:
                paras.append((s.get("para") or None, [s]))
        parts = []
        for i, (_, group) in enumerate(paras):
            text = " ".join(t for t in (clean(s["text"]) for s in group) if t)
            kinds = {kind(s) for s in group}
            style = kinds.pop() if len(kinds) == 1 else "narration"
            # Titles: "Part One. Two Banks." is said as two lines with a beat between them.
            pieces = [x for x in re.split(r"(?<=\.)\s+", text)] if style == "title" else [text]
            for j, piece in enumerate(pieces):
                if not piece:
                    continue
                speed, db = STYLE[style]
                audio, sr = k.create(phonemes(k, piece, lang, lex), voice=voice, speed=speed, lang=lang, is_phonemes=True)
                parts.append(np.asarray(audio, dtype=np.float32) * (10 ** (db / 20)))
                if j < len(pieces) - 1:
                    parts.append(np.zeros(int(SR * 1.0), dtype=np.float32))
            parts.append(np.zeros(int(SR * group[-1].get("pause_after_ms", 300) / 1000), dtype=np.float32))
            print(f"\rchapter {n}: {i + 1}/{len(paras)}", end="", flush=True)
        wav = np.concatenate(parts)
        tmp = os.path.join(out_dir, f"{n:02d}_{voice}.f32")
        wav.tofile(tmp)
        mp3 = os.path.join(out_dir, f"{n:02d}_{voice}{'_sample' if limit else ''}.mp3")
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", tmp,
                        "-af", "loudnorm=I=-19:TP=-3:LRA=11", "-ar", "44100", "-b:a", "128k", mp3], check=True)
        os.remove(tmp)
        print(f"\n{os.path.relpath(mp3, REPO)}: {len(wav) / SR / 60:.1f} min")


if __name__ == "__main__":
    main()
