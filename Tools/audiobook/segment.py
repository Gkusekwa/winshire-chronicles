"""Split the Book 1 manuscript into paragraphs and spans for the audiobook build.

Each chapter becomes a list of paragraphs. Each paragraph lists its spans:
  q  = quoted speech  ("...")
  i  = italic text    (*...*): bond speech, thought, verse, written words, emphasis
Paragraph and span ids are stable for a given text: p1, p2, ... and s1, s2, ...
The annotation files (Book 1/audiobook/annotations/chNN.json) key on these ids.
"""
import glob, re, os

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
ITALIC = re.compile(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])")


def chapter_files(book="Book 1"):
    out = {}
    for f in glob.glob(f"{REPO}/{book}/Chapters/*.md"):
        n = int(re.search(r"Chapter (\d+)", os.path.basename(f)).group(1))
        out[n] = f
    return dict(sorted(out.items()))


def read_chapter(path):
    t = open(path, encoding="utf-8").read()
    head, body = t.split("\n", 1)
    title = re.match(r"# Chapter \d+: (.+)$", head).group(1).strip()
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
    return title, body


def spans_of(text):
    """Return a list of (kind, start, end, inner_text) for quotes and italics, in order."""
    spans = []
    # quotes: pair them up; an unclosed last quote runs to the end of the paragraph
    qs = [m.start() for m in re.finditer('"', text)]
    for k in range(0, len(qs), 2):
        a = qs[k]
        b = qs[k + 1] + 1 if k + 1 < len(qs) else len(text)
        spans.append(("q", a, b, text[a:b]))
    for m in ITALIC.finditer(text):
        spans.append(("i", m.start(), m.end(), m.group(1)))
    spans.sort(key=lambda s: (s[1], -s[2]))
    return spans


def segment(path):
    title, body = read_chapter(path)
    blocks = [b.strip() for b in re.split(r"\n\s*\n", body.strip())]
    blocks = [b for b in blocks if b]
    paras, sid, pid, scene = [], 0, 0, False
    while blocks and blocks[0] == "---":
        blocks.pop(0)
    for b in blocks:
        if b == "---":
            scene = True
            continue
        text = " ".join(l.strip() for l in b.split("\n"))
        pid += 1
        sp = []
        for kind, a, e, inner in spans_of(text):
            sid += 1
            sp.append({"id": f"s{sid}", "kind": kind, "start": a, "end": e, "text": inner})
        paras.append({"id": f"p{pid}", "text": text, "scene_break_before": scene, "spans": sp})
        scene = False
    return title, paras


def sheet(n, path):
    """A plain-text sheet for annotators."""
    title, paras = segment(path)
    L = [f"# Chapter {n}: {title}", ""]
    for p in paras:
        if p["scene_break_before"]:
            L.append("------ scene break ------")
        L.append(f"[{p['id']}] {p['text']}")
        for s in p["spans"]:
            tag = "QUOTE" if s["kind"] == "q" else "ITALIC"
            L.append(f"    {s['id']} {tag}: {s['text'][:140]}")
        L.append("")
    return "\n".join(L)


if __name__ == "__main__":
    import sys
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    tq = ti = tp = 0
    for n, f in chapter_files().items():
        open(f"{out}/ch{n:02d}.txt", "w", encoding="utf-8").write(sheet(n, f))
        _, paras = segment(f)
        tp += len(paras)
        for p in paras:
            for s in p["spans"]:
                tq += s["kind"] == "q"; ti += s["kind"] == "i"
    print("paragraphs", tp, "quotes", tq, "italics", ti)
