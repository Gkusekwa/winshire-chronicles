"""Hear a name said several ways, to choose its respelling: reads test sentences with each candidate spelling, in
the book's narrator voice, and reports what the recogniser heard for each.

    names.py --book DIR Maren                      # the name as written, its current respelling, and a few variants
    names.py --book DIR Maren Mairen Mare-en Marren   # or the spellings to try

Writes <book>/audiobook/out/names_<Name>.mp3: for each candidate, "Number one.", a pause, then the test sentences
with that spelling. Listen, pick the one that sounds right, and put it in the Respelling column of Lexicon.csv
(or clear the Respelling if the name as written sounds right). Chapters that use the name are made again on the
next build.
"""
import os, re, subprocess, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import config as cfg      # noqa: E402
import render as R        # noqa: E402

SENTENCES = ["{X}.", "At the door, {X} stopped.", "\"Where were you, {X}?\" said Wren.", "{X} didn't answer. {X}'s hands were cold."]
ORDINALS = "one two three four five six seven eight".split()


def variants(name, current):
    """A few likely spellings, from the Say guide in the lexicon (e.g. MAIR-en) and simple rewrites."""
    out = [name, current] if current else [name]
    say = ""
    for row in open(cfg.NAMES, encoding="utf-8").read().splitlines() if cfg.NAMES and cfg.NAMES.endswith(".csv") else []:
        cells = row.split(",")
        if cells and cells[0] == name and len(cells) > 2:
            say = cells[2]
    if say:
        parts = [p.lower() for p in say.split("-")]
        out.append("-".join(p.capitalize() if i == 0 else p for i, p in enumerate(parts)))     # Mair-en
        out.append("".join(parts).capitalize())                                            # Mairen
    low = name.lower()
    if re.search(r"a[^aeiou]", low[:3]):
        out.append(name[:1] + name[1:].replace("a", "ai", 1))                              # Maren -> Mairen
        out.append(name[:1] + name[1:].replace("a", "aw", 1))                              # Calder -> Cawlder
    seen, res = set(), []
    for v in out:
        if v and v.lower() not in seen:
            seen.add(v.lower()); res.append(v)
    return res[:8]


def main():
    args = [a for a in sys.argv[1:]]
    if not args:
        sys.exit("Name the name to test, e.g.  names.py --book \"Book 1\" Maren")
    name, tries = args[0], args[1:]
    current = dict(R.name_pairs()).get(name, "")
    cands = tries or variants(name, current)
    import numpy as np, torch
    from chatterbox.tts import ChatterboxTTS
    from faster_whisper import WhisperModel
    device = "cuda" if torch.cuda.is_available() else ("mps" if torch.backends.mps.is_available() else "cpu")
    model = ChatterboxTTS.from_pretrained(device=device)
    model.prepare_conditionals(cfg.NARRATOR, exaggeration=0.5)
    asr = WhisperModel(os.environ.get("WORDCHECK_MODEL", "small.en"), device="cpu", compute_type="int8")
    SR = model.sr
    say = lambda t: model.generate(t, exaggeration=0.5, cfg_weight=0.5).squeeze(0).cpu().numpy().astype(np.float32)
    gap = lambda s: np.zeros(int(SR * s), dtype=np.float32)
    parts, report = [], []
    for i, c in enumerate(cands):
        parts += [say(f"Number {ORDINALS[i]}."), gap(0.8)]
        heard = []
        for sent in SENTENCES:
            a = say(sent.replace("{X}", c))
            parts += [a, gap(0.6)]
            x = np.interp(np.arange(0, len(a), SR / 16000), np.arange(len(a)), a).astype(np.float32)
            x = np.concatenate([np.zeros(8000, np.float32), x, np.zeros(8000, np.float32)])
            segs, _ = asr.transcribe(x, language="en", beam_size=5, condition_on_previous_text=False)
            heard.append(" ".join(s.text.strip() for s in segs))
        parts.append(gap(1.5))
        tag = " (as written)" if c == name else (" (the current respelling)" if c == current else "")
        report.append(f"  {i + 1}. {c}{tag}\n     heard: " + " | ".join(heard))
        print(f"\r{i + 1}/{len(cands)}", end="", flush=True)
        if device == "mps":
            torch.mps.empty_cache()
    os.makedirs(cfg.OUT, exist_ok=True)
    out = os.path.join(cfg.OUT, f"names_{re.sub(r'[^A-Za-z0-9]+', '_', name)}.mp3")
    tmp = out + ".f32"
    np.concatenate(parts).tofile(tmp)
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", tmp,
                    "-af", "loudnorm=I=-19:TP=-3", "-ar", "44100", "-b:a", "128k", out], check=True)
    os.remove(tmp)
    print(f"\n{name}: {len(cands)} spellings, in {os.path.relpath(out, cfg.BOOK)}")
    print("\n".join(report))
    print(f"\nPick the one that sounds right and put it in the Respelling column for {name} in "
          f"{os.path.relpath(cfg.NAMES, cfg.BOOK)} (empty = read as written).")


if __name__ == "__main__":
    main()
