"""Check audiobook annotation files against the manuscript's span ids.

Usage: check_annotations.py [NN ...] [--dir DIR]   (no chapter numbers = all)
"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from segment import chapter_files, segment, REPO

TYPES = {"speech", "bond", "thought", "verse", "written", "remembered", "emphasis", "term"}
NEEDS_NAME = {"speech", "bond", "thought", "remembered"}
MOODS = {"action", "tension", "dread", "quiet", "reflective", "tender", "grief", "humour", "anger", "urgent", "awe"}


def parse_span(v):
    v, _, how = v.partition("|")
    t, _, who = v.partition(":")
    spk, _, to = who.partition(">")
    return t.strip(), spk.strip(), to.strip(), how.strip()


def check(n, path, d):
    f = f"{d}/ch{n:02d}.json"
    if not os.path.exists(f):
        return [f"ch{n}: no annotation file"]
    try:
        a = json.load(open(f, encoding="utf-8"))
    except Exception as e:
        return [f"ch{n}: bad JSON: {e}"]
    _, paras = segment(path)
    ids = {s["id"] for p in paras for s in p["spans"]}
    pids = {p["id"] for p in paras}
    errs = []
    got = a.get("spans", {})
    miss = sorted(ids - set(got), key=lambda x: int(x[1:]))
    extra = sorted(set(got) - ids)
    if miss: errs.append(f"ch{n}: missing spans {miss[:20]}{' ...' if len(miss) > 20 else ''}")
    if extra: errs.append(f"ch{n}: unknown spans {extra[:20]}")
    for k, v in got.items():
        t, spk, to, how = parse_span(v)
        if t not in TYPES: errs.append(f"ch{n} {k}: unknown type {v!r}")
        elif t in NEEDS_NAME and not spk: errs.append(f"ch{n} {k}: {t} needs a speaker")
        elif t == "bond" and not to: errs.append(f"ch{n} {k}: bond needs Speaker>Listener")
    for k, v in a.get("paragraphs", {}).items():
        if k not in pids: errs.append(f"ch{n}: unknown paragraph {k}")
        m = v.partition("|")[0].strip()
        if m not in MOODS: errs.append(f"ch{n} {k}: unknown mood {v!r}")
    if not a.get("pov"): errs.append(f"ch{n}: no pov")
    return errs


if __name__ == "__main__":
    args = sys.argv[1:]
    d = f"{REPO}/Book 1/audiobook/annotations"
    if "--dir" in args:
        i = args.index("--dir"); d = args[i + 1]; del args[i:i + 2]
    chs = chapter_files()
    todo = [int(x) for x in args] or list(chs)
    errs = []
    for n in todo:
        errs += check(n, chs[n], d)
    print("\n".join(errs) if errs else "OK")
