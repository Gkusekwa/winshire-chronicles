"""Export the finished chapters for upload, with full names, into <book>/audiobook/release/:

    The Watch Below - 00 - Opening credits.mp3
    The Watch Below - 01 - Chapter 1 - The Unchosen Yard.mp3
    ...
    The Watch Below - 99 - Closing credits.mp3

The working files (out/NN.mp3) stay as they are: the kit's reports and its record of what's done hang off those
numbers. Only chapters marked PASS (by the checks, or accepted after listening) are exported; the rest are listed.
Each exported file carries the same tags as its working file (title, book, author, track). Running it again brings
the folder up to date: chapters rebuilt since are exported again, and files of chapters no longer passing are removed.

Use:  export.py --book DIR [--drafts]    (--drafts also exports chapters not yet passing, marked "DRAFT")
"""
import json, os, re, shutil, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import config as cfg      # noqa: E402
import prepare as P       # noqa: E402
import render as R        # noqa: E402

RELEASE = os.path.join(cfg.AUDIO, "release")


def safe(name):
    name = name.replace(": ", " - ").replace(":", " - ")
    return re.sub(r'[\\/*?"<>|]', "", name).strip()


def main():
    drafts = "--drafts" in sys.argv
    P.main(quiet=True)                       # the titles come from the reading scripts
    try:
        manifest = json.load(open(os.path.join(cfg.OUT, "manifest.json")))
    except Exception:
        manifest = {}
    os.makedirs(RELEASE, exist_ok=True)
    prefix = safe(cfg.TITLE) + " - "
    wanted, missing, failing = {}, [], []
    for n in cfg.chapter_numbers():
        src = os.path.join(cfg.OUT, f"{n:02d}.mp3")
        e = manifest.get(f"{n:02d}")
        status = e.get("status") if isinstance(e, dict) else None
        if not os.path.exists(src):
            missing.append(n); continue
        if status != "PASS":
            failing.append((n, status or "unknown"))
            if not drafts:
                continue
        name = f"{prefix}{n:02d} - {safe(R.chapter_title(n))}" + ("" if status == "PASS" else " (DRAFT)") + ".mp3"
        wanted[name] = src
    # bring the folder up to date: remove the kit's old exports that are no longer wanted
    for f in os.listdir(RELEASE):
        if f.startswith(prefix) and f.endswith(".mp3") and f not in wanted:
            os.remove(os.path.join(RELEASE, f))
    made = 0
    for name, src in sorted(wanted.items()):
        dst = os.path.join(RELEASE, name)
        if os.path.exists(dst) and os.path.getsize(dst) == os.path.getsize(src) and os.path.getmtime(dst) >= os.path.getmtime(src):
            continue
        shutil.copy2(src, dst)
        made += 1
    print(f"Exported {len(wanted)} chapter(s) to {os.path.relpath(RELEASE, cfg.BOOK)} ({made} new or updated).")
    if failing:
        print(("Exported as drafts" if drafts else "Not exported (not passing yet)") + ": "
              + ", ".join(f"{n:02d} ({s})" for n, s in failing))
    if missing:
        print("Not built yet: " + (", ".join(f"{n:02d}" for n in missing) if len(missing) <= 20
                                    else f"{len(missing)} chapters ({missing[0]:02d}–{missing[-1]:02d})"))


if __name__ == "__main__":
    main()
