"""Share the chapters still to build among several workers (one or more per GPU), so they finish together: the
longest chapters first, each to the worker with the least work so far. Prints one line per worker:
    <worker>\t<book dir>\t<chapters>\t<book dir>\t<chapters>...

Use:  gpu_plan.py WORKERS BOOK_DIR [BOOK_DIR ...]
A chapter that already passed with unchanged inputs (or was accepted after listening) is left out.
"""
import json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))


def chapters_to_build(book):
    """(chapter, characters) for every chapter of `book` that isn't done, using the renderer's own fingerprint."""
    code = r'''
import json, os, re, sys, hashlib
sys.argv = ["x", "--book", sys.argv[1]]
sys.path.insert(0, "%s")
import config as cfg, prepare, render as R
prepare.main(quiet=True)
try:
    m = json.load(open(os.path.join(cfg.OUT, "manifest.json")))
except Exception:
    m = {}
out = []
for n in cfg.chapter_numbers():
    e = m.get(f"{n:02d}")
    segs = json.load(open(cfg.script_path(n), encoding="utf-8"))["segments"]
    size = sum(len(s["text"]) for s in segs)
    done = isinstance(e, dict) and e.get("status") == "PASS" and os.path.exists(os.path.join(cfg.OUT, f"{n:02d}.mp3"))
    out.append((n, size, done))
print(json.dumps(out))
''' % HERE
    r = subprocess.run([sys.executable, "-c", code, book], capture_output=True, text=True)
    if r.returncode:
        sys.exit(f"Couldn't read {book}: {r.stderr.strip()[-500:]}")
    return [(n, size) for n, size, done in json.loads(r.stdout.strip().splitlines()[-1]) if not done]


def main():
    workers = int(sys.argv[1])
    books = [os.path.abspath(b) for b in sys.argv[2:]]
    jobs = []
    for b in books:
        for n, size in chapters_to_build(b):
            jobs.append((size, b, n))
    jobs.sort(reverse=True)
    load = [0] * workers
    plan = [dict() for _ in range(workers)]
    for size, b, n in jobs:
        w = min(range(workers), key=lambda i: load[i])
        load[w] += size
        plan[w].setdefault(b, []).append(n)
    total = sum(load) or 1
    for w in range(workers):
        parts = []
        for b in books:
            if plan[w].get(b):
                parts += [b, ",".join(str(n) for n in sorted(plan[w][b]))]
        print("\t".join([str(w)] + parts))
    sys.stderr.write(f"{len(jobs)} chapters to build, about {total / 14 / 3600:.0f} hours of audio, in {workers} workers.\n")


if __name__ == "__main__":
    main()
