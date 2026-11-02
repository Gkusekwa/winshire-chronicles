"""Make the reading scripts from the chapter files (Markdown), one `NN.json` per chapter in `<book>/audiobook/scripts/`.

Chapters: every file matching the pattern in the chapters folder (default `Chapters/*.md`), numbered by the first
number in the file name (`Chapter 07 - Title.md` -> 7) or, failing that, by sorted order. Up to 98 chapters
(00 and 99 are the credits).

From each chapter it takes:
- the title, from the first `# ` heading ("# Chapter 7: The Ferry" -> "Chapter Seven." then "The Ferry."), or the
  file name;
- a part title where a new part begins, from a `Part:` line in an HTML-comment notes block, if the book has them
  ("Part: Part One: Two Banks" -> "Part One. Two Banks.");
- the text: paragraphs separated by blank lines; HTML comments, YAML front matter, headings and Markdown markup
  removed; scene breaks (`***`, `* * *`, `---`, `#`) become a longer pause; a paragraph wholly in quotation marks is
  speech, one wholly in italics is thought (read a little quieter and slower); everything else is narration;
- proper names: capitalised words that aren't at the start of a sentence, so the word check doesn't count a
  misspelt name as an error.

It rebuilds a chapter's script only when the chapter file has changed. Nothing is made when book.json names a
folder of ready-made scripts.
"""
import glob, hashlib, json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import config as cfg  # noqa: E402

ONES = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
TENS = "_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()
P_PARA, P_SCENE, P_PART, P_NUM, P_TITLE = 500, 1600, 2000, 800, 1800
SCENE = re.compile(r"^\s*(\*\s*\*\s*\*|-{3,}|_{3,}|#|⁂|~{3,})\s*$")
WORDS_EN = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10}


def say_number(n):
    if n < 20:
        return ONES[n]
    if n < 100:
        return TENS[n // 10] + ("" if n % 10 == 0 else "-" + ONES[n % 10])
    return str(n)


def chapter_files():
    files = sorted(glob.glob(os.path.join(cfg.CHAPTERS, cfg.C["pattern"])))
    files = [f for f in files if not os.path.basename(f).lower().startswith(("readme", "notes", "plan"))]
    out, used = {}, set()
    for k, f in enumerate(files, 1):
        m = re.search(r"\d+", os.path.basename(f))
        n = int(m.group()) if m else k
        if n in used or not 1 <= n <= 98:
            n = max(used | {0}) + 1
        used.add(n)
        out[n] = f
    return dict(sorted(out.items()))


def clean_inline(t):
    t = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", t)              # images
    t = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", t)          # links -> their text
    t = re.sub(r"(\*\*|__|\*|_|`)", "", t)                    # emphasis and code marks
    t = t.replace("\\", "")
    return re.sub(r"\s+", " ", t).strip()


def proper_names(paragraphs):
    """Likely names: capitalised words not at a sentence start that never appear in lower case in the chapter."""
    lower = {w.replace("’", "").replace("'", "") for p in paragraphs for w in re.findall(r"\b[a-z][a-z’']*", p)}
    names = set()
    for p in paragraphs:
        for m in re.finditer(r"(?<![.!?\"“”:;—–]\s)(?<![“\"‘(—–])(?<!^)\b([A-Z][a-z’']+)", p):
            w = m.group(1)
            if w.lower() not in {"i", "i'm", "i’m", "i'd", "i’d", "i'll", "i’ll"}:
                names.add(re.sub(r"[’']s$", "", w).lower().replace("’", "").replace("'", ""))
    return sorted(w for w in names if w not in lower and len(w) > 2)


def build(n, path, last_part):
    raw = open(path, encoding="utf-8").read()
    notes = " ".join(re.findall(r"<!--(.*?)-->", raw, flags=re.S))
    part = re.search(r"^\s*Part:\s*(.+)$", notes, flags=re.M)
    part = part.group(1).strip() if part else None
    text = re.sub(r"<!--.*?-->", "", raw, flags=re.S)
    text = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)           # YAML front matter
    lines = text.split("\n")
    head = next((l for l in lines if l.startswith("# ")), None)
    title = None
    if head:
        h = head[2:].strip()
        m = re.match(r"(?i)chapter\s+([\w-]+)\s*[:.\-–—]\s*(.+)", h)
        title = (m.group(2) if m else h).strip()
    if not title:
        title = re.sub(r"^[\d\s._-]*(chapter\s*\d+\s*[-–—:]\s*)?", "", os.path.splitext(os.path.basename(path))[0], flags=re.I).strip() or f"Chapter {n}"
    segs = []

    def seg(t, typ, pause, para=""):
        segs.append({"seq": len(segs) + 1, "para": para, "type": typ, "text": t, "pause_after_ms": pause})

    if part and part != last_part:
        seg(re.sub(r"\s*:\s*", ". ", part).rstrip(".") + ".", "title", P_PART)
    seg(f"Chapter {say_number(n).capitalize()}.", "title", P_NUM)
    seg(clean_inline(title).rstrip(".") + ".", "title", P_TITLE)

    paras, cur = [], []
    for l in lines:
        if l.startswith("#") and not SCENE.match(l):
            continue
        if SCENE.match(l):
            if cur: paras.append(" ".join(cur)); cur = []
            paras.append(None)                        # scene break
        elif not l.strip():
            if cur: paras.append(" ".join(cur)); cur = []
        else:
            cur.append(l.strip())
    if cur:
        paras.append(" ".join(cur))
    plain = []
    for k, p in enumerate(paras):
        if p is None:
            if segs and segs[-1]["type"] != "title":
                segs[-1]["pause_after_ms"] = P_SCENE
            continue
        raw_p = p.strip()
        t = clean_inline(raw_p)
        if not t:
            continue
        plain.append(t)
        pid = f"p{len(plain)}"
        if re.fullmatch(r"\*[^*].*[^*]\*|_[^_].*[^_]_", raw_p):
            seg(t, "thought", P_PARA, pid)
        elif re.fullmatch(r"[\"“][^\"“”]*[\"”]", t):
            seg(t, "speech", P_PARA, pid)
        else:
            # keep quoted speech as its own segments (the renderer still reads the paragraph as one)
            pos = 0
            for m in re.finditer(r"[\"“][^\"“”]*[\"”]?", t):
                if m.start() > pos and t[pos:m.start()].strip():
                    seg(t[pos:m.start()].strip(), "narration", 0, pid)
                seg(m.group().strip(), "speech", 0, pid)
                pos = m.end()
            if t[pos:].strip():
                seg(t[pos:].strip(), "narration", 0, pid)
            segs[-1]["pause_after_ms"] = P_PARA
    return {"chapter": n, "title": title, "source": os.path.relpath(path, cfg.BOOK),
            "names": proper_names(plain), "segments": segs}, part or last_part


def credits():
    t, a = cfg.TITLE, cfg.AUTHOR
    opening = [f"{t}.", f"Written by {a}." if a else None, "This audiobook is read by a digital voice."]
    closing = [f"This has been {t}." + (f" Written by {a}." if a else ""), "Read by a digital voice."]
    mk = lambda n, name, lines: {"chapter": n, "title": name, "names": [], "segments": [
        {"seq": i + 1, "para": "", "type": "title", "text": l, "pause_after_ms": 1200} for i, l in enumerate(x for x in lines if x)]}
    return mk(0, "Opening credits", opening), mk(99, "Closing credits", closing)


def main(quiet=False):
    if not cfg.BUILT_SCRIPTS:
        if not quiet:
            print(f"Using the ready-made scripts in {os.path.relpath(cfg.SCRIPTS, cfg.BOOK)}.")
        return
    os.makedirs(cfg.SCRIPTS, exist_ok=True)
    files = chapter_files()
    if not files:
        sys.exit(f"No chapter files in {cfg.CHAPTERS} matching {cfg.C['pattern']}: set 'chapters' in {cfg.CONF}.")
    made, last_part = 0, None
    for n, path in files.items():
        data, last_part = build(n, path, last_part)
        data["source_sha1"] = hashlib.sha1(open(path, "rb").read()).hexdigest()
        out = cfg.script_path(n)
        if os.path.exists(out):
            old = json.load(open(out, encoding="utf-8"))
            if old.get("source_sha1") == data["source_sha1"] and old.get("segments") == data["segments"]:
                continue
        json.dump(data, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        made += 1
    if cfg.C.get("credits", True):
        for d in credits():
            p = cfg.script_path(d["chapter"])
            if not os.path.exists(p) or json.load(open(p, encoding="utf-8")).get("segments") != d["segments"]:
                json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    if not quiet or made:
        print(f"Scripts: {len(files)} chapters in {os.path.relpath(cfg.SCRIPTS, cfg.BOOK)} ({made} new or changed).")


if __name__ == "__main__":
    main()
