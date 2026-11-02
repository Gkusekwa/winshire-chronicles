"""Where the book is, and its settings.

The kit lives in a folder next to the book's chapters (for example `My Book/audiobook-kit/`); the book is the folder
that holds the kit. Everything the kit makes goes in `<book>/audiobook/`. Settings are in `<book>/audiobook/book.json`,
created on the first run with what the kit could work out; edit it to change anything.

book.json:
  title        the book's title (spoken in the opening credits)
  author       the author's name (spoken in the opening credits)
  series       the series and number, e.g. "The Winshire Chronicles, Book Two" (spoken after the title; optional)
  chapters     folder of chapter files, relative to the book (default: Chapters)
  pattern      which files are chapters (default: *.md)
  scripts      a folder of ready-made reading scripts (NN.json) to use instead of building them from the chapters
               (empty: the kit builds them in audiobook/reading_scripts; the Winshire Chronicles' Book 1 uses its
               annotated scripts this way)
  names        pronunciation respellings: a .pls lexicon (aliases) or a .csv of name,respelling (optional)
  narrator     the narrator's reference clip (default: the kit's voices/narrator.wav)
  output       where the finished chapters go (default: audiobook/out)
  credits      true: add opening and closing credits (00 and 99) saying the book is read by a digital voice
"""
import glob, json, os, re, sys

KIT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _book_dir():
    for i, a in enumerate(sys.argv):
        if a == "--book" and i + 1 < len(sys.argv):
            book = os.path.abspath(sys.argv[i + 1])
            del sys.argv[i:i + 2]          # so the scripts never read the folder's name as chapter numbers
            return book
    return os.path.dirname(KIT)


BOOK = _book_dir()
AUDIO = os.path.join(BOOK, "audiobook")
CONF = os.path.join(AUDIO, "book.json")


def _guess():
    chapters = next((d for d in ("Chapters", "chapters", "Manuscript", "manuscript", "Text", ".")
                     if glob.glob(os.path.join(BOOK, d, "*.md"))), "Chapters")
    title = os.path.basename(BOOK)
    def respellings(p):     # a names file only counts if it gives respellings (a .pls of IPA phonemes doesn't)
        try:
            return p.endswith(".csv") or "<alias>" in open(p, encoding="utf-8").read()
        except Exception:
            return False
    names = next((os.path.relpath(p, BOOK) for p in sorted(glob.glob(os.path.join(AUDIO, "*.pls")))
                  + glob.glob(os.path.join(AUDIO, "names.csv")) if respellings(p)), "")
    return {"title": title, "author": "", "series": "", "chapters": chapters, "pattern": "*.md", "scripts": "",
            "names": names,
            "narrator": "", "output": "audiobook/out", "credits": True}


def load():
    os.makedirs(AUDIO, exist_ok=True)
    if os.path.exists(CONF):
        conf = {**_guess(), **json.load(open(CONF, encoding="utf-8"))}
    else:
        conf = _guess()
        json.dump(conf, open(CONF, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(f"Made {os.path.relpath(CONF, BOOK)} with the settings below; edit it to change them.")
        for k, v in conf.items():
            print(f"  {k}: {v}")
    return conf


C = load()


def _path(p, default):
    if not p:
        return default
    return p if os.path.isabs(p) else os.path.join(BOOK, p)


CHAPTERS = _path(C["chapters"], os.path.join(BOOK, "Chapters"))
# "reading_scripts", not "scripts": a Mac's disk ignores case, and a book may already have a "Scripts" folder
SCRIPTS = _path(C["scripts"], os.path.join(AUDIO, "reading_scripts"))
BUILT_SCRIPTS = not C["scripts"]          # True: the kit makes the scripts from the chapters
NAMES = _path(C["names"], "")
NARRATOR = _path(C["narrator"], os.path.join(KIT, "voices", "narrator.wav"))
OUT = _path(C["output"], os.path.join(AUDIO, "out"))
TITLE, AUTHOR, SERIES = C["title"], C["author"], C.get("series", "")


def chapter_numbers():
    """Chapters that have a reading script, as numbers (00 and 99 are the credits)."""
    return sorted(int(f[:2]) for f in os.listdir(SCRIPTS) if re.fullmatch(r"\d\d\.json", f)) if os.path.isdir(SCRIPTS) else []


def script_path(n):
    return os.path.join(SCRIPTS, f"{n:02d}.json")
