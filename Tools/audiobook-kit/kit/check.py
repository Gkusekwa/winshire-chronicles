"""Check a book's annotations against its chapters: every quote and italic annotated, with an allowed type, and the
paragraph moods allowed. Use after editing annotations by hand.

Use:  check.py --book DIR [7 | 2-10 | all] [--strict]
      --strict also asks for a speaker on speech, bond, thought and remembered words, a listener on bond speech,
      and a point of view for the chapter (the standard of a hand-directed book).
"""
import json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import config as cfg      # noqa: E402
import prepare as P       # noqa: E402

TYPES = {"speech", "bond", "thought", "remembered", "written", "verse", "emphasis", "term"}
NEEDS_NAME = {"speech", "bond", "thought", "remembered"}
MOODS = {"action", "tension", "dread", "quiet", "reflective", "tender", "grief", "humour", "anger", "urgent", "awe"}


def check(n, path, strict):
    f = os.path.join(P.ANN, f"ch{n:02d}.json")
    if not os.path.exists(f):
        return [f"ch{n}: no annotation file"]
    try:
        a = json.load(open(f, encoding="utf-8"))
    except Exception as e:
        return [f"ch{n}: not valid JSON: {e}"]
    _, _, body = P.read_chapter(path, n)
    paras = P.segment(body)
    ids = [s["id"] for p in paras for s in p["spans"]]
    pids = {p["id"] for p in paras}
    got = a.get("spans", {})
    errs = []
    miss = [i for i in ids if i not in got]
    extra = sorted(set(got) - set(ids), key=lambda x: int(x[1:]) if x[1:].isdigit() else 0)
    if miss: errs.append(f"ch{n}: missing spans {miss[:20]}{' …' if len(miss) > 20 else ''}")
    if extra: errs.append(f"ch{n}: spans that aren't in the chapter {extra[:20]}")
    for k, v in got.items():
        t, spk, to, how = P.parse_span(v)
        if t not in TYPES: errs.append(f"ch{n} {k}: unknown type {v!r}")
        elif strict and t in NEEDS_NAME and not spk: errs.append(f"ch{n} {k}: {t} needs a speaker ({v!r})")
        elif strict and t == "bond" and not to: errs.append(f"ch{n} {k}: bond needs Speaker>Listener ({v!r})")
    for k, v in a.get("paragraphs", {}).items():
        if k not in pids: errs.append(f"ch{n}: unknown paragraph {k}")
        m = v.partition("|")[0].strip()
        if m not in MOODS: errs.append(f"ch{n} {k}: unknown mood {v!r}")
    if strict and not a.get("pov"): errs.append(f"ch{n}: no pov")
    return errs


def main():
    args = sys.argv[1:]
    files = P.chapter_files()
    nums = P_list(args)
    todo = sorted(files) if not nums or "all" in args else [n for n in nums if n in files]
    errs = []
    for n in todo:
        errs += check(n, files[n], "--strict" in args)
    print("\n".join(errs) if errs else f"OK: {len(todo)} chapter(s)")
    sys.exit(1 if errs else 0)


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
