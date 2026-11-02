"""Render Book 1 audiobook passages with Chatterbox (Resemble AI, MIT licence): free, offline after the first
model download, and able to act. Use it to compare with the Kokoro cast, passage for passage.

How it reads the scripts (`Book 1/audiobook/Performance/NN.json`):
- The narrator reads everything, in Emma's voice, cloned from a short reference clip of Kokoro's Emma
  (`Book 1/audiobook/Chatterbox/refs/Narrator.wav`, made with `render_kokoro.py --refs --cast`), so the two engines
  can be compared on the same voice. With --cast, each character speaks in their own cloned voice instead.
- Each line's mood and "how" note set Chatterbox's emotion intensity (exaggeration) and pacing (cfg weight).
- Names are respelt from `Lexicon_Alias.pls`, since Chatterbox reads text, not phonemes.
- Chatterbox adds an inaudible Perth watermark to its output (Resemble AI's responsible-AI marker).

Setup on a Mac: `bash Tools/audiobook/chatterbox_mac.sh` (Python 3.11, chatterbox-tts 0.1.7, the model from Hugging Face).

Use:
    python3 render_chatterbox.py --audition      # the same passages as the Kokoro audition -> out/audition.mp3
    python3 render_chatterbox.py 1               # chapter 1 -> out/01.mp3
    python3 render_chatterbox.py 1-79 --skip-done

Output: `Book 1/audiobook/Chatterbox/out/` (ignored by git; never commit the audio).
"""
import hashlib, json, os, re, subprocess, sys, xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import render_kokoro as rk   # shared: the audition picks, paragraphs, kinds of words  # noqa: E402
import cast as castmap        # noqa: E402

AB = rk.AB
REPO = rk.REPO
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
    t = " ".join(rk.clean(s["text"]) for s in segs if s["text"].strip())
    t = t.replace("’", "'")
    for rx, a in subs:
        t = rx.sub(a, t)
    return t


def chunks(text, limit=260):
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


def main():
    args = sys.argv[1:]
    use_cast = "--cast" in args   # default: the narrator (Emma) reads everything
    import numpy as np, torch
    from chatterbox.tts import ChatterboxTTS
    device = "cuda" if torch.cuda.is_available() else ("mps" if torch.backends.mps.is_available() else "cpu")
    print("device:", device)
    model = ChatterboxTTS.from_pretrained(device=device)
    SR = model.sr
    subs = aliases()
    os.makedirs(OUT, exist_ok=True)
    conds = {}

    def ref_for(role):
        p = os.path.join(REFS, role.replace(" ", "_") + ".wav")
        return p if os.path.exists(p) else os.path.join(REFS, "Narrator.wav")

    def say(text, role, exaggeration, cfg):
        key = role
        if key not in conds:
            model.prepare_conditionals(ref_for(role), exaggeration=exaggeration)
            conds[key] = model.conds
        model.conds = conds[key]
        wav = model.generate(text, exaggeration=exaggeration, cfg_weight=cfg)
        return wav.squeeze(0).cpu().numpy().astype(np.float32)

    def tempo(audio, f):
        if abs(f - 1) < 0.01:
            return audio
        r = subprocess.run(["ffmpeg", "-loglevel", "error", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "pipe:0",
                            "-af", f"atempo={f:.4f}", "-f", "f32le", "pipe:1"],
                           input=audio.tobytes(), capture_output=True, check=True)
        return np.frombuffer(r.stdout, dtype=np.float32)

    def runs(group):
        out = []
        for s in group:
            role = (castmap.role_of(s["speaker"]) if use_cast and s.get("speaker") and rk.kind(s) in ("speech", "bond")
                    else "Narrator")
            if out and out[-1][0] == role and rk.kind(out[-1][1][-1]) == rk.kind(s):
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
                style = rk.kind(segs[0])
                ex, cfg = MOOD.get(segs[0].get("mood"), MOOD[None])
                gain = GAIN.get(style, 0.0)
                how = " ".join(s.get("how") or "" for s in segs).lower()
                for word, dex, dg in HOW:
                    if word in how:
                        ex += dex; gain += dg; how = how.replace(word, "")
                ex = max(0.25, min(1.0, ex))
                pieces = rk.title_pieces(text) if style == "title" else chunks(text)
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

    if not os.path.exists(os.path.join(REFS, "Narrator.wav")):
        sys.exit("No reference clips: run  render_kokoro.py --refs --cast  first (kokoro_mac.sh refs does it).")

    if "--audition" in args:
        write(render(rk.audition(), "audition"), os.path.join(OUT, "audition_cast.mp3" if use_cast else "audition.mp3"))
        return

    chapters = []
    for a in args:
        if re.fullmatch(r"\d+-\d+", a):
            lo, hi = map(int, a.split("-")); chapters += range(lo, hi + 1)
        elif a.isdigit():
            chapters.append(int(a))
    man_path = os.path.join(OUT, "manifest.json")
    try:
        manifest = json.load(open(man_path))
    except Exception:
        manifest = {}
    for n in chapters:
        src = os.path.join(AB, "Performance", f"{n:02d}.json")
        digest = hashlib.sha1(open(src, "rb").read() + open(__file__, "rb").read()).hexdigest()
        mp3 = os.path.join(OUT, f"{n:02d}.mp3")
        if "--skip-done" in args and os.path.exists(mp3) and manifest.get(f"{n:02d}") == digest:
            print(f"{n:02d}: up to date, skipped"); continue
        groups = []
        for s in json.load(open(src, encoding="utf-8"))["segments"]:
            if groups and s.get("para") and groups[-1][-1].get("para") == s["para"]:
                groups[-1].append(s)
            else:
                groups.append([s])
        write(render(groups, f"chapter {n}"), mp3)
        manifest[f"{n:02d}"] = digest
        json.dump(manifest, open(man_path, "w"), indent=1)


if __name__ == "__main__":
    main()
