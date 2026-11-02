"""Make a book's reading scripts from its chapters: the annotations, the Performance scripts and the lexicon.

Everything is made in `<book>/audiobook/`, and each step leaves files you can open and correct:

1. annotations/chNN.json: what kind of words every quote and italic is (speech, bond speech, thought, remembered,
   written, verse, emphasis), who says it and how, and a mood for the paragraphs that need one. Made by the kit where
   missing (marked "auto": true; see directions.py for how it decides). Correct them freely: take out the "auto" line
   and the kit keeps your file, filling in only quotes or italics added since.
2. Lexicon.csv: the names, one per line: Name, Respelling (what the narrator reads; empty if the spelling reads
   right), Say (a guide like OR-veth), IPA, Notes. The kit adds names it finds in the chapters that aren't listed yet;
   it never changes a line that's there. Fill in a respelling for any name the narrator says wrongly.
3. Performance/NN.json: each chapter as the narrator reads it: titles, then every paragraph as segments with their
   type, speaker, delivery, mood and pause. Remade whenever its chapter, annotations or this script change. To change
   the reading, change the annotations; if you edit a Performance file by hand, the kit keeps it until its chapter
   or annotations change, and then tells you.
   00 and 99 are the opening and closing credits, from book.json (title, series, author, next, copyright).

Chapters: every file matching the pattern in the chapters folder (default `Chapters/*.md`), numbered by the first
number in its name. Its title comes from the first `# ` heading ("# Chapter 7: The Ferry"); a part title is read where
a new part begins, from a `Part:` line in the chapter's notes (an HTML comment), e.g. "Part: Part One: Two Banks".
Paragraphs are separated by blank lines; `---`, `***` or `* * *` alone on a line is a scene break.

Use:  prepare.py [--book DIR] [--check]     (--check: also confirm every word of every chapter is in its script)
"""
import glob, hashlib, json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import config as cfg      # noqa: E402
import directions         # noqa: E402

VERSION = "prepare 2 / " + directions.GENERATOR
ONES = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
TENS = "_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()
P_PARA, P_SCENE, P_PART, P_NUM, P_TITLE, P_HEAVY = 500, 1600, 2000, 800, 1800, 800
HEAVY = {"grief", "dread", "awe", "tension"}       # a little more silence after these
SCENE = re.compile(r"^\s*(-{3,}|\*\s*\*\s*\*|_{3,}|⁂|~{3,}|#)\s*$")
ITALIC = re.compile(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])")
ANN = os.path.join(cfg.AUDIO, "annotations")
LEXICON = os.path.join(cfg.AUDIO, "Lexicon.csv")


def say_number(n):
    if n < 20:
        return ONES[n]
    if n < 100:
        return TENS[n // 10] + ("" if n % 10 == 0 else "-" + ONES[n % 10])
    return str(n)


def sha(*parts):
    h = hashlib.sha1()
    for p in parts:
        h.update(p if isinstance(p, bytes) else json.dumps(p, sort_keys=True, ensure_ascii=False).encode())
    return h.hexdigest()


# ---------------- chapters ----------------
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


def read_chapter(path, n):
    raw = open(path, encoding="utf-8").read()
    notes = " ".join(re.findall(r"<!--(.*?)-->", raw, flags=re.S))
    part = re.search(r"^\s*Part:\s*(.+)$", notes, flags=re.M)
    text = re.sub(r"\A---\n.*?\n---\n", "", raw, flags=re.S)       # YAML front matter
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    lines = text.split("\n")
    title, k = None, 0
    for k, l in enumerate(lines):
        if l.startswith("# "):
            h = l[2:].strip()
            m = re.match(r"(?i)chapter\s+[\w-]+\s*[:.\-–—]\s*(.+)", h)
            title = (m.group(1) if m else h).strip()
            lines = lines[k + 1:]
            break
    if not title:
        title = re.sub(r"^[\d\s._-]*(chapter\s*\d+\s*[-–—:]\s*)?", "", os.path.splitext(os.path.basename(path))[0],
                       flags=re.I).strip() or f"Chapter {n}"
    return title, (part.group(1).strip() if part else None), "\n".join(lines)


def spans_of(text):
    """Quotes ("…" or “…”; an unclosed last quote runs to the paragraph's end) and italics (*…*), in order."""
    spans = []
    if "“" in text or "”" in text:
        for m in re.finditer(r"“[^“”]*(”|$)", text):
            spans.append(("q", m.start(), m.end(), m.group()))
    else:
        qs = [m.start() for m in re.finditer('"', text)]
        for k in range(0, len(qs), 2):
            a = qs[k]
            b = qs[k + 1] + 1 if k + 1 < len(qs) else len(text)
            spans.append(("q", a, b, text[a:b]))
    for m in ITALIC.finditer(text):
        spans.append(("i", m.start(), m.end(), m.group(1)))
    spans.sort(key=lambda s: (s[1], -s[2]))
    return spans


def segment(body):
    """Paragraphs with stable ids (p1, p2, …) and their quotes and italics (s1, s2, … through the chapter)."""
    blocks = [b.strip("\n") for b in re.split(r"\n\s*\n", body.strip())]
    paras, sid, scene = [], 0, False
    for b in blocks:
        b = "\n".join(l for l in b.split("\n") if not (l.startswith("#") and not SCENE.match(l)))
        if not b.strip():
            continue
        if SCENE.match(b.strip()):
            scene = bool(paras)
            continue
        quoted = all(l.lstrip().startswith(">") for l in b.split("\n") if l.strip())
        lines = [re.sub(r"^\s*>\s?", "", l).strip() for l in b.split("\n")]
        text = " ".join(l for l in lines if l)
        sp = []
        for kind, a, e, inner in spans_of(text):
            sid += 1
            sp.append({"id": f"s{sid}", "kind": kind, "start": a, "end": e, "text": inner})
        paras.append({"id": f"p{len(paras) + 1}", "text": text, "scene_break_before": scene, "spans": sp,
                      "lines": len([l for l in lines if l]), "blockquote": quoted})
        scene = False
    return paras


def clean(t):
    """Markdown to speakable text. Words are never changed; only marks, and quotes made curly as in the ebook."""
    t = t.replace("**", "").replace("__", "")
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"\1", t)
    t = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", t)
    t = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", t)
    t = t.replace("`", "").replace("\\", "")
    t = t.replace("...", "\u2026")
    t = t.replace("'", "\u2019")
    t = re.sub(r"(^|[\s(\[\u2014])\u2019", "\\1\u2018", t)
    t = re.sub(r'"(?=\w|\u2018|\u2026|[\[(])', "\u201c", t)
    return t.replace('"', "\u201d")


def parse_span(v):
    v, _, how = v.partition("|")
    t, _, who = v.partition(":")
    spk, _, to = who.partition(">")
    return t.strip(), spk.strip(), to.strip(), how.strip()


# ---------------- annotations ----------------
def annotations(n, paras, source_sha):
    """The chapter's annotations: the hand-made file, filled in where it lacks something, or the kit's own."""
    os.makedirs(ANN, exist_ok=True)
    path = os.path.join(ANN, f"ch{n:02d}.json")
    ids = [s["id"] for p in paras for s in p["spans"]]
    made = directions.auto(paras, None, cfg.C.get("italics", "thought"))
    if os.path.exists(path):
        ann = json.load(open(path, encoding="utf-8"))
        by_ai = str(ann.get("generator", "")).startswith("ai:")
        if by_ai and ann.get("source_sha1") != source_sha:
            print(f"  chapter {n}: changed since the local AI annotated it; its annotations are kept and filled in."
                  f" To have the AI do it again: menu option 11 with chapter {n}.")
        if not ann.get("auto") or by_ai or ann.get("source_sha1") == source_sha and ann.get("generator") == directions.GENERATOR:
            missing = [i for i in ids if i not in ann.get("spans", {})]
            extra = [i for i in ann.get("spans", {}) if i not in set(ids)]
            if missing or extra:
                print(f"  chapter {n}: the annotations don't match the chapter's quotes and italics any more"
                      f" ({len(missing)} new, {len(extra)} gone); the kit filled in the new ones. Check {os.path.relpath(path, cfg.BOOK)}.")
                for i in missing:
                    ann.setdefault("spans", {})[i] = made["spans"][i]
            return ann
    ann = {"chapter": n, "pov": "", "auto": True, "generator": directions.GENERATOR, "source_sha1": source_sha,
           "spans": made["spans"], "paragraphs": made["paragraphs"]}
    json.dump(ann, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    return ann


# ---------------- lexicon ----------------
_NOT_NAMES = set("""The And But Both Maybe None Yes No Not Never Nothing Nobody Somebody Someone Everyone Everything
    Still Then There Here This That These Those What When Where Which Who Why How Well Good Oh Ah Please Sorry Thank
    Thanks Surprised Again Once Twice Today Tonight Tomorrow Yesterday Mister Missus Sir Madam Lady Lord Lords King
    Queen Prince Princess Captain Captains Instructor Aunt Uncle Master Mistress Gran Nan Grandad Grandmother Father
    Mother Brother Sister Knight Knights Student Students Reader Warden Wardens Watcher Watch Council Clan Gods God
    Old Upper Lower North South East West Northern Southern Eastern Western Monday Tuesday Wednesday Thursday Friday
    Saturday Sunday January February March April May June July August September October November December""".split())


def proper_names(paragraphs):
    """Likely names: capitalised words seen at least twice inside a sentence and never in lower case."""
    lower = {w.replace("’", "").replace("'", "") for p in paragraphs for w in re.findall(r"\b[a-z][a-z’']*", p)}
    seen = {}
    for p in paragraphs:
        for m in re.finditer(r"(?<![.!?\"“”:;—–]\s)(?<![“\"‘(—–*])(?<!^)\b([A-Z][a-z’']+)", p):
            w = re.sub(r"[’'](s|ll|ve|d|re|m)$", "", m.group(1)).replace("’", "").replace("'", "")
            if w.lower() not in lower and len(w) > 2 and w not in _NOT_NAMES:
                seen[w] = seen.get(w, 0) + 1
    return {w for w, k in seen.items() if k >= 2}


def update_lexicon(found):
    """Add names found in the chapters to Lexicon.csv; existing lines are never changed."""
    import csv
    rows, have = [], set()
    if os.path.exists(LEXICON):
        rows = list(csv.reader(open(LEXICON, encoding="utf-8")))
        have = {r[0].strip() for r in rows if r and not r[0].startswith("#")}
    new = sorted(w for w in found if w not in have)
    if not rows:
        rows = [["Name", "Respelling", "Say", "IPA", "Notes"],
                ["# Respelling is what the narrator reads (e.g. Aurveth,Orveth); leave it empty when the spelling reads right."]]
    if new:
        if os.path.exists(LEXICON):
            rows.append([f"# added by the kit from the chapters: fill in a respelling where the narrator gets one wrong"])
        rows += [[w, "", "", "", ""] for w in new]
        with open(LEXICON, "w", encoding="utf-8", newline="") as fh:
            csv.writer(fh).writerows(rows)
    return new


# ---------------- Performance ----------------
def performance(n, title, part, paras, ann):
    segs = []

    def seg(kind, text, speaker="", listener="", how="", mood="", pause=0, pid=""):
        d = {"seq": len(segs) + 1, "para": pid, "type": kind, "text": text}
        if speaker: d["speaker"] = speaker
        if listener: d["listener"] = listener
        if how: d["how"] = how
        if mood: d["mood"] = mood
        if pause: d["pause_after_ms"] = pause
        segs.append(d)

    if part:
        label, _, sub = part.partition(": ")
        seg("title", f"{label}. {sub}." if sub else f"{label.rstrip('.')}.", pause=P_PART)
    seg("title", f"Chapter {say_number(n).capitalize()}.", pause=P_NUM)
    seg("title", f"{clean(title).rstrip('.')}.", pause=P_TITLE)
    kinds = {"speech", "bond", "thought", "remembered", "written", "verse"}
    for i, p in enumerate(paras):
        if p["scene_break_before"] and segs:
            segs[-1]["pause_after_ms"] = P_SCENE
        mood, _, note = ann.get("paragraphs", {}).get(p["id"], "").partition("|")
        mood = mood.strip()
        text, runs, pos = p["text"], [], 0
        top = []
        for s in p["spans"]:          # spans inside another span (an italic word in a quote) belong to it;
            if top and s["start"] < top[-1]["end"]:      # one that overlaps it is read as plain text
                continue
            top.append(s)
        for s in top:
            if s["start"] > pos:
                runs.append(["narration", "", "", "", text[pos:s["start"]]])
            t, spk, to, how = parse_span(ann["spans"].get(s["id"], "speech"))
            if t not in kinds:
                t = "narration"            # emphasis and terms are read as part of the sentence
            if p["blockquote"] and t == "narration":
                t = "written"
            runs.append([t, spk, to, how, text[s["start"]:s["end"]]])
            pos = s["end"]
        if pos < len(text):
            runs.append(["written" if p["blockquote"] else "narration", "", "", "", text[pos:]])
        merged = []
        for r in runs:
            r[4] = clean(r[4])
            if merged and merged[-1][0] == "narration" and r[0] == "narration":
                merged[-1][4] += r[4]
            else:
                merged.append(r)
        merged = [r for r in merged if r[4].strip()]
        pause = P_HEAVY if mood in HEAVY else P_PARA
        for j, (k, s, t, h, txt) in enumerate(merged):
            seg(k, txt.strip(), s, t, h, mood, pause if j == len(merged) - 1 else 0, p["id"])
    return segs


def credits():
    t, a, sr = cfg.TITLE, cfg.AUTHOR, cfg.SERIES.strip().rstrip(".")
    nxt, year = cfg.C.get("next", "").strip().rstrip("."), str(cfg.C.get("copyright", "")).strip()
    by = f", written by {a}," if a else ","
    opening = [(f"{t}.", 900), (f"{sr}." if sr else None, 900), (f"Written by {a}." if a else None, 700),
               ("Narrated by a digital voice.", 2000)]
    closing = [("The End.", 2000),
               (f"You have been listening to {t}" + (f", {sr}" if sr else "") + f"{by} and narrated by a digital voice.", 900),
               (f"Copyright {year} by {a}. Production copyright {year} by {a}." if year and a else None, 1200),
               (f"The story continues in {nxt}." if nxt else None, 1500)]
    mk = lambda n, name, lines: {"chapter": n, "title": name, "pov": "", "segments": [
        {"seq": i + 1, "para": "", "type": "title", "text": l, "pause_after_ms": ms}
        for i, (l, ms) in enumerate(x for x in lines if x[0])]}
    return mk(0, "Opening", opening), mk(99, "Closing", closing)


def write_script(path, data, inputs):
    """Write a Performance file unless it was edited by hand since the kit made it (then say so and keep it)."""
    data["generator"] = VERSION
    data["inputs_sha1"] = inputs
    if os.path.exists(path):
        old = json.load(open(path, encoding="utf-8"))
        if old.get("inputs_sha1") == inputs:
            return False
        made = old.get("segments_sha1")
        if made and made != sha(old.get("segments")):
            print(f"  {os.path.relpath(path, cfg.BOOK)} was edited by hand, and its chapter or annotations have changed"
                  " since. Kept as it is: move your edits into the annotations, or delete the file to make it again.")
            return False
    data["segments_sha1"] = sha(data["segments"])
    json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return True


def check_words(path, segs, paras, title):
    """Every word of the chapter is in its script, in order (the titles aside)."""
    norm = lambda t: [w.lower() for w in re.findall(r"[\w']+", clean(t).replace("\u2019", "'").replace("\u2018", "'").replace("\u2026", "..."))]
    want = norm(" ".join(p["text"] for p in paras))
    got = norm(" ".join(s["text"] for s in segs if s["type"] != "title"))
    return want == got


def main(quiet=False):
    if not cfg.BUILT_SCRIPTS:
        if not quiet:
            print(f"Using the ready-made scripts in {os.path.relpath(cfg.SCRIPTS, cfg.BOOK)}.")
        return
    os.makedirs(cfg.SCRIPTS, exist_ok=True)
    files = chapter_files()
    if not files:
        sys.exit(f"No chapter files in {cfg.CHAPTERS} matching {cfg.C['pattern']}: set 'chapters' in {cfg.CONF}.")
    made, last_part, found, bad = 0, None, set(), []
    for n, path in files.items():
        raw = open(path, "rb").read()
        title, part, body = read_chapter(path, n)
        paras = segment(body)
        ann = annotations(n, paras, sha(raw))
        part_said = part if part and part != last_part else None
        segs = performance(n, title, part_said, paras, ann)
        last_part = part or last_part
        if "--check" in sys.argv and not check_words(path, segs, paras, title):
            bad.append(n)
        names = proper_names([p["text"] for p in paras])
        found |= names
        data = {"chapter": n, "title": title, "pov": ann.get("pov", ""), "source": os.path.relpath(path, cfg.BOOK),
                "names": sorted(w.lower() for w in names), "segments": segs}
        inputs = sha(raw, ann, VERSION, part_said)
        made += write_script(cfg.script_path(n), data, inputs)
    if cfg.C.get("credits", True):
        for d in credits():
            made += write_script(cfg.script_path(d["chapter"]), d, sha(d["segments"], VERSION))
    new = update_lexicon(found)
    if not quiet or made or new:
        print(f"Scripts: {len(files)} chapters in {os.path.relpath(cfg.SCRIPTS, cfg.BOOK)} ({made} new or changed)"
              + (f"; {len(new)} new names in {os.path.relpath(LEXICON, cfg.BOOK)}" if new else "") + ".")
    if "--check" in sys.argv:
        print("Every word is in its script." if not bad else f"Words differ from the chapter in: {bad}")


if __name__ == "__main__":
    main()
