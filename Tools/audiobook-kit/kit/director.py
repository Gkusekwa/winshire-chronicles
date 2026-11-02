"""Write a book's annotations with a free AI model running on your own Mac (Ollama), instead of the kit's rules.

The model reads each chapter a few pages at a time, as an audiobook director would, and decides for every quote and
italic what kind of words it is (speech, bond speech, thought, remembered, written, verse, emphasis), who says it and
how, and for each paragraph whether it needs a mood (tension, grief, tender...). It reads the scene, not just the
words, so it can catch what the rules can't. Nothing leaves the computer.

The results go into `<book>/audiobook/annotations/chNN.json`, marked "auto": true with the model's name, and the
reading scripts are remade from them. Hand-made annotations (no "auto" line) are never touched. Everything the model
says is checked: an answer that isn't one of the allowed types or moods, or a quote it skipped, is filled in by the
kit's rules instead.

Use (audiobook.sh option 11 does this, and sets up Ollama first):
    director.py --book DIR 7 | 2-10 | all  [--model NAME] [--redo]
        writes the annotations for those chapters; --redo also redoes chapters the AI did before
    director.py --book DIR --compare 5 [--model NAME]
        annotates chapter 5 without saving and compares it with the hand-made file: how often the model agrees
        (use it on Book 1 of the Winshire Chronicles, whose annotations are hand-made, before running a whole book)

The model: book.json "model", or --model, or else qwen2.5:14b on a Mac with 24 GB of memory or more and
qwen2.5:7b otherwise (Ollama downloads it the first time: about 9 GB or 4.7 GB).
"""
import json, os, re, subprocess, sys, time, urllib.request, urllib.error

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import config as cfg      # noqa: E402
import directions         # noqa: E402
import prepare as P       # noqa: E402

# The chapters never leave this computer: only an Ollama on this machine is used. (OLLAMA_HOST may name another local
# port; a host anywhere else is refused.)
HOST = os.environ.get("OLLAMA_HOST", "127.0.0.1:11434").strip().rstrip("/")
if not HOST.startswith("http"):
    HOST = "http://" + HOST
_h = re.sub(r"^https?://", "", HOST).split("/")[0]
_h = _h.rsplit(":", 1)[0] if _h.count(":") == 1 or _h.startswith("[") else _h
if _h.strip("[]") not in ("127.0.0.1", "localhost", "::1", "0.0.0.0"):
    sys.exit(f"OLLAMA_HOST is set to {HOST}, which isn't this computer. The kit only sends the book to an AI running"
             " here; unset OLLAMA_HOST (or set it to 127.0.0.1:11434) and try again.")
HOST = HOST.replace("0.0.0.0", "127.0.0.1")
PROMPT_VERSION = "2"
FAMILY = {"action": "tense", "tension": "tense", "dread": "tense", "urgent": "tense", "anger": "tense",
          "quiet": "soft", "reflective": "soft", "tender": "soft", "grief": "soft", "humour": "light", "awe": "awe"}
TYPES = ["speech", "bond", "thought", "remembered", "written", "verse", "emphasis", "term"]
MOODS = list(directions.MOODS)
CHUNK_WORDS = 1400


def default_model():
    if cfg.C.get("model"):
        return cfg.C["model"]
    try:
        mem = int(subprocess.run(["sysctl", "-n", "hw.memsize"], capture_output=True, text=True).stdout.strip())
    except Exception:
        mem = 0
    return "qwen2.5:14b" if mem >= 24 * 2 ** 30 else "qwen2.5:7b"


def call(path, payload=None, timeout=600):
    req = urllib.request.Request(HOST + path, data=json.dumps(payload).encode() if payload is not None else None,
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode())


def ready(model):
    try:
        tags = call("/api/tags", timeout=10)
    except Exception:
        sys.exit(f"Ollama isn't running at {HOST}. Start the Ollama app (or run: ollama serve), then try again.")
    names = {m.get("name") for m in tags.get("models", [])} | {m.get("model") for m in tags.get("models", [])}
    if model not in names and model + ":latest" not in names:
        sys.exit(f"The model {model} isn't downloaded yet. Run: ollama pull {model}")


ITALIC_NOTE = {
    "bond": "In this book, italic words spoken mind to mind (between a bonded beast and a person, or two bonded people)"
            " are type bond, with the listener after '>'.",
    "thought": "",
}

SYSTEM = """You are directing the audiobook of a novel read by one narrator. For a few pages at a time you mark how each
passage should be read. You never change or add words.

For every SPAN (a quote or an italic, listed under its paragraph) give:
- type, one of:
  speech: words said aloud (most quotes).
  bond: words passed mind to mind, without sound (only if the book has this; see the note).
  thought: a character's own unspoken thought.
  remembered: words heard before, recalled now ("Hollin saying *ask your uncle*").
  written: words read off a page, letter, sign, stone or order, or a document read aloud.
  verse: a song, rhyme, oath, vow or prophecy in lines.
  emphasis: a word or two stressed inside a sentence ("she looked at *me*").
  term: a word introduced as a name for something ("the shepherds call it *keeping the fence*").
- speaker: who says, thinks or wrote it, by name if the text makes it clear; "" if unsure. For bond, also listener.
- how: a few words on delivery ONLY when the text says how it is said (whispered, shouted, very quietly, voice
  cracking, called across the yard, flat); otherwise "".

For every PARAGRAPH give a mood and how strongly the reading needs it, or mood "none" with strength 0. Moods:
  action (a fight, a chase, a fall), tension (danger near, waiting, a standoff), dread (something wrong, fear, horror),
  quiet (stillness, rest, low talk), reflective (looking back, thinking it over), tender (love, care, comfort),
  grief (loss, death, mourning), humour (teasing, a joke, comedy, and also dry or deadpan wit: an absurd detail
  told straight, a wry remark, a character being comically stubborn), anger (rage, a fierce quarrel),
  urgent (hurry, alarm, orders shouted), awe (wonder, something vast or ancient).
Strength: 3 = the paragraph is plainly in that mood and a reader would miss it if read flat; 2 = clearly there;
1 = a faint colour only. Most paragraphs are plain narration or plain talk and get "none" and 0: ordinary
description, movement, everyday conversation and exposition are NOT tension or reflective. In a typical chapter only
about one paragraph in five needs a mood at strength 2 or 3. Judge the scene, not single words: a paragraph about a
funeral is grief even if no sad word appears; "she didn't laugh" is not humour. Optionally add a short note on the
mood ("after the burial").

Answer only with JSON in the given shape, with every span and every paragraph listed."""


def sheet(paras, pov_hint):
    L = []
    for p in paras:
        if p["scene_break_before"]:
            L.append("------ scene break ------")
        L.append(f"[{p['id']}] {p['text']}")
        for s in p["spans"]:
            L.append(f"    {s['id']} {'QUOTE' if s['kind'] == 'q' else 'ITALIC'}: {s['text'][:200]}")
        L.append("")
    return "\n".join(L)


def schema(paras):
    sids = [s["id"] for p in paras for s in p["spans"]]
    return {"type": "object", "required": ["pov", "spans", "paragraphs"], "properties": {
        "pov": {"type": "string"},
        "spans": {"type": "array", "items": {"type": "object", "required": ["id", "type", "speaker", "how"], "properties": {
            "id": {"type": "string", "enum": sids or ["none"]}, "type": {"type": "string", "enum": TYPES},
            "speaker": {"type": "string"}, "listener": {"type": "string"}, "how": {"type": "string"}}}},
        "paragraphs": {"type": "array", "items": {"type": "object", "required": ["id", "mood", "strength"], "properties": {
            "id": {"type": "string", "enum": [p["id"] for p in paras]}, "mood": {"type": "string", "enum": MOODS + ["none"]},
            "strength": {"type": "integer", "enum": [0, 1, 2, 3]}, "note": {"type": "string"}}}}}}


def chunks(paras):
    out, cur, words = [], [], 0
    for p in paras:
        w = len(p["text"].split())
        if cur and words + w > CHUNK_WORDS:
            out.append(cur); cur, words = [], 0
        cur.append(p); words += w
    if cur:
        out.append(cur)
    return out


def ask(model, n, title, paras, before, pov):
    note = ITALIC_NOTE.get(cfg.C.get("italics", "thought"), "")
    user = (f"Book: {cfg.TITLE}. Chapter {n}: {title}." + (f" Point of view so far: {pov}." if pov else "") +
            (f"\nNote: {note}" if note else "") +
            ("\n\nWhat came just before (for context only, don't mark it):\n" + before if before else "") +
            "\n\nMark these paragraphs:\n\n" + sheet(paras, pov))
    r = call("/api/chat", {"model": model, "stream": False, "format": schema(paras),
                           "options": {"temperature": 0, "num_ctx": 8192},
                           "messages": [{"role": "system", "content": SYSTEM}, {"role": "user", "content": user}]})
    return json.loads(r["message"]["content"])


def annotate(n, model, paras, title, progress=None):
    """Annotations for one chapter from the model, checked and filled in by the rules where needed."""
    rules = directions.auto(paras, None, cfg.C.get("italics", "thought"))
    spans, moods, pov, fixed = {}, {}, "", 0
    parts = chunks(paras)
    for k, part in enumerate(parts):
        if progress:
            progress(k, len(parts))          # before each part, so there's always a line saying what it's doing
        before = " ".join(p["text"] for p in (paras[:paras.index(part[0])])[-2:])[-700:]
        for attempt in range(2):
            try:
                got = ask(model, n, title, part, before, pov)
                break
            except (urllib.error.URLError, json.JSONDecodeError, KeyError, TimeoutError) as e:
                got = None
                if attempt:
                    print(f"\n  chapter {n}, part {k + 1}: the model's answer couldn't be used ({e}); the rules fill it in")
        pov = pov or (got or {}).get("pov", "").strip()
        want = {s["id"] for p in part for s in p["spans"]}
        for s in (got or {}).get("spans", []):
            sid, t = s.get("id"), s.get("type")
            if sid in want and t in TYPES:
                v = t
                spk, lis = s.get("speaker", "").strip(), s.get("listener", "").strip()
                if spk and t not in ("emphasis", "term"):
                    v += ":" + spk + (f">{lis}" if lis and t == "bond" else "")
                how = re.sub(r"[|:>]", ",", s.get("how", "").strip())[:60]
                spans[sid] = v + (f"|{how}" if how else "")
        for p in (got or {}).get("paragraphs", []):
            if p.get("mood") in MOODS and p.get("id") in {x["id"] for x in part}:
                note = re.sub(r"\|", ",", p.get("note", "").strip())[:60]
                strength = p.get("strength", 2) if isinstance(p.get("strength", 2), int) else 2
                moods[p["id"]] = (strength, p["mood"] + (f"|{note}" if note else ""))
        if progress:
            progress(k + 1, len(parts))
    for sid, v in rules["spans"].items():
        if sid not in spans:
            spans[sid] = v; fixed += 1
    # Keep only the moods the reading needs: strength 2 or 3, and at most book.json "mood_share" of the chapter's
    # paragraphs (default a quarter, as in a hand-directed book), the strongest first.
    share = float(cfg.C.get("mood_share", 0.25))
    order = {p["id"]: i for i, p in enumerate(paras)}
    strong = sorted(((st, -order[k], k, v) for k, (st, v) in moods.items() if st >= 2), reverse=True)
    moods = {k: v for st, _, k, v in strong[:max(1, round(len(paras) * share))]}
    return {"pov": pov, "spans": dict(sorted(spans.items(), key=lambda kv: int(kv[0][1:]))),
            "paragraphs": dict(sorted(moods.items(), key=lambda kv: int(kv[0][1:])))}, fixed


def compare(n, model):
    path = os.path.join(P.ANN, f"ch{n:02d}.json")
    if not os.path.exists(path):
        sys.exit(f"No annotations for chapter {n} to compare with.")
    hand = json.load(open(path, encoding="utf-8"))
    if hand.get("auto"):
        print(f"Note: chapter {n}'s annotations were made by the kit, not by hand.")
    title, _, body = P.read_chapter(P.chapter_files()[n], n)
    paras = P.segment(body)
    t0 = time.time()
    ai, fixed = annotate(n, model, paras, title, lambda a, b: print(f"\r  reading chapter {n}: {a} of {b} parts done" + ("…" if a < b else " "), end="", flush=True))
    print(f"\r  {model} took {time.time() - t0:.0f} s for chapter {n} ({len(paras)} paragraphs).")
    pt = lambda v: P.parse_span(v)[0]
    ids = list(hand.get("spans", {}))
    same = sum(pt(hand["spans"][i]) == pt(ai["spans"].get(i, "")) for i in ids)
    hm = {k: v.partition("|")[0] for k, v in hand.get("paragraphs", {}).items()}
    am = {k: v.partition("|")[0] for k, v in ai["paragraphs"].items()}
    both = sum(1 for k in am if k in hm)
    exact = sum(1 for k in am if hm.get(k) == am[k])
    close = sum(1 for k in am if k in hm and FAMILY[hm[k]] == FAMILY[am[k]])
    print(f"  quotes and italics: same type as the hand-made file for {same} of {len(ids)} ({same / max(len(ids), 1):.0%})")
    print(f"  moods: hand-made {len(hm)} of {len(paras)} paragraphs; the model {len(am)}; both give one to {both};"
          f" the same mood for {exact}, the same or a close one (same family) for {close}")
    print(f"    of the model's {len(am)} moods, {close} agree with the hand at least closely ({close / max(len(am), 1):.0%});"
          f" of the hand's {len(hm)}, the model found {close} ({close / max(len(hm), 1):.0%})")
    print(f"  (the kit's rules on the same chapter: {len(directions.auto(paras, None, cfg.C.get('italics', 'thought'))['paragraphs'])} moods)")
    for k in list(dict.fromkeys(list(hm) + list(am)))[:12]:
        if hm.get(k) != am.get(k):
            text = next(p["text"] for p in paras if p["id"] == k)
            print(f"    {k}: hand {hm.get(k, '-'):10s} model {am.get(k, '-'):10s}  {text[:90]}…")


def main():
    args = sys.argv[1:]
    model = args[args.index("--model") + 1] if "--model" in args else default_model()
    if "--which-model" in args:
        return print(model)
    ready(model)
    print(f"Loading {model} (the first time after starting the Mac, this takes a minute or so)…", flush=True)
    try:
        call("/api/generate", {"model": model, "prompt": "", "keep_alive": "30m"}, timeout=900)
    except Exception:
        pass
    if "--compare" in args:
        return compare(int(args[args.index("--compare") + 1]), model)
    files = P.chapter_files()
    nums = sorted(files) if "all" in args or "--all" in args else sorted(set(P_list(args)) & set(files))
    if not nums:
        sys.exit("No chapters given: e.g. 7, 2-10 or all")
    gen = f"ai:{model} / prompt {PROMPT_VERSION}"
    os.makedirs(P.ANN, exist_ok=True)
    print(f"Annotating {len(nums)} chapter(s) of {cfg.TITLE} with {model}, on this computer.")
    t_start, done_words, total_words = time.time(), 0, 0
    todo = []
    for n in nums:
        path = os.path.join(P.ANN, f"ch{n:02d}.json")
        old = json.load(open(path, encoding="utf-8")) if os.path.exists(path) else None
        if old is not None and not old.get("auto"):
            print(f"  chapter {n}: annotated by hand; left alone"); continue
        if old is not None and old.get("generator") == gen and "--redo" not in args:
            print(f"  chapter {n}: already done by {model}; left alone (--redo to do it again)"); continue
        title, _, body = P.read_chapter(files[n], n)
        paras = P.segment(body)
        todo.append((n, path, title, paras))
        total_words += sum(len(p["text"].split()) for p in paras)
    for n, path, title, paras in todo:
        words = sum(len(p["text"].split()) for p in paras)

        def prog(a, b, n=n, words=words):
            spent = time.time() - t_start
            frac = (done_words + words * a / b) / max(total_words, 1)
            eta = spent / frac - spent if frac > 0 else 0
            left = f"about {eta / 60:.0f} min left" if frac > 0 else "working out the time left"
            print(f"\r  chapter {n}: {a} of {b} parts done   book {frac:.0%}, {left}   ", end="", flush=True)
        ann, fixed = annotate(n, model, paras, title, prog)
        raw = open(files[n], "rb").read()
        data = {"chapter": n, "pov": ann["pov"], "auto": True, "generator": gen, "source_sha1": P.sha(raw),
                "spans": ann["spans"], "paragraphs": ann["paragraphs"]}
        data["anchors"], data["para_anchors"] = P.anchors(paras)
        json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        done_words += words
        print(f"\r  chapter {n}: {len(ann['paragraphs'])} of {len(paras)} paragraphs with a mood"
              + (f"; {fixed} quote(s) or italic(s) filled in by the rules" if fixed else "") + " " * 30)
    P.main(quiet=False)       # remake the reading scripts from the new annotations


def P_list(args):
    out = []
    for a in args:
        for part in a.split(","):
            if re.fullmatch(r"\d+-\d+", part):
                lo, hi = map(int, part.split("-")); out += range(lo, hi + 1)
            elif part.isdigit():
                out.append(int(part))
    return out


if __name__ == "__main__":
    main()
