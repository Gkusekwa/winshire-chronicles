#!/bin/bash
# Audiobook kit: narrate a book with Chatterbox, free and on your own Mac.
#
# Copy the audiobook-kit folder into your book's folder, next to its chapters:
#     My Book/
#         Chapters/          the chapter files (Markdown: Chapter 01 - Title.md, ...)
#         audiobook-kit/     this kit
# then, from anywhere:
#     bash "My Book/audiobook-kit/audiobook.sh"
# Or keep one kit for several books and name the book's folder:
#     bash audiobook-kit/audiobook.sh --book "My Book" [choice] [chapters]
#
# Menu, or give the choice directly:  audiobook.sh <choice> [chapters]
#   1  one chapter, verified            ... 1 7
#   2  one chapter, not verified        ... 2 7
#   3  several chapters, verified       ... 3 2-10     or  ... 3 2,5,9
#   4  several chapters, not verified   ... 4 2-10
#   5  the whole book, verified         ... 5
#   6  the whole book, not verified     ... 6
#   7  verify chapters already built    ... 7 1        or  ... 7 2-10  or  ... 7 all
#   8  audition: a few minutes of every kind of passage, to hear the voice
#   9  setup only (install or update Chatterbox and Whisper)
#  10  put the chapter titles into chapters already built (tags only)   ... 10 all
# Everything it makes goes in "My Book/audiobook/": scripts/, out/ (the MP3s and check reports) and book.json
# (title, author, where the chapters are, names, narrator clip; made on the first run, edit it freely).
set -e
KIT="$(cd "$(dirname "$0")" && pwd)"
PYV="$HOME/chatterbox/venv/bin/python"
BOOK="$(dirname "$KIT")"
if [ "$1" = "--book" ]; then
  [ -d "$2" ] || { echo "No such book folder: $2"; exit 1; }
  BOOK="$(cd "$2" && pwd)"; shift 2
fi
choice="$1"; chapters="$2"
export PYTHONWARNINGS=ignore TQDM_DISABLE=1 TRANSFORMERS_VERBOSITY=error HF_HUB_DISABLE_PROGRESS_BARS=1

ensure_setup() {
  if [ ! -x "$PYV" ] || ! "$PYV" -c "import chatterbox, faster_whisper, perth; assert perth.PerthImplicitWatermarker" 2>/dev/null; then
    bash "$KIT/setup_mac.sh"
  fi
}

title="$(python3 -c "import json,sys; print(json.load(open(sys.argv[1])).get('title',''))" "$BOOK/audiobook/book.json" 2>/dev/null || true)"
[ -n "$title" ] || title="$(basename "$BOOK")"

if [ -z "$choice" ]; then
  echo "Audiobook: $title"
  echo "  1) Build one chapter and verify"
  echo "  2) Build one chapter without verifying"
  echo "  3) Build several chapters and verify"
  echo "  4) Build several chapters without verifying"
  echo "  5) Build the entire book and verify"
  echo "  6) Build the entire book without verifying"
  echo "  7) Verify chapters already built (no rendering)"
  echo "  8) Audition: hear the voice on every kind of passage"
  echo "  9) Setup only"
  echo " 10) Put the chapter titles into chapters already built"
  read -r -p "Choose 1-10: " choice
fi

case "$choice" in
  1|2)
    [ -n "$chapters" ] || read -r -p "Chapter number (0 = opening credits, 99 = closing): " chapters
    [[ "$chapters" =~ ^[0-9]+$ ]] || { echo "One chapter number, please (e.g. 7)."; exit 1; } ;;
  3|4)
    [ -n "$chapters" ] || read -r -p "Chapters (e.g. 2-10, or 2,5,9, or 1-3,7): " chapters
    [[ "$chapters" =~ ^[0-9,-]+$ ]] || { echo "Chapters like 2-10 or 2,5,9, please."; exit 1; } ;;
  5|6) chapters="--all" ;;
  7)
    [ -n "$chapters" ] || read -r -p "Chapters to verify (e.g. 1, 2-10, 2,5,9, or all): " chapters
    [ "$chapters" = "all" ] && chapters="--all"
    [[ "$chapters" =~ ^([0-9,-]+|--all)$ ]] || { echo "Chapters like 1, 2-10, 2,5,9 or all, please."; exit 1; }
    ensure_setup
    echo "==> Verifying built chapters: $chapters"
    "$PYV" "$KIT/kit/verify.py" "$chapters" --book "$BOOK"
    exit 0 ;;
  8) chapters="--audition" ;;
  9) bash "$KIT/setup_mac.sh"; exit 0 ;;
  10)
    [ -n "$chapters" ] || read -r -p "Chapters to tag (e.g. 1, 2-10, or all): " chapters
    [ "$chapters" = "all" ] && chapters="--all"
    [[ "$chapters" =~ ^([0-9,-]+|--all)$ ]] || { echo "Chapters like 1, 2-10, 2,5,9 or all, please."; exit 1; }
    python3 "$KIT/kit/render.py" --retag "$chapters" --book "$BOOK"
    exit 0 ;;
  *) echo "Choose 1 to 10."; exit 1 ;;
esac

ensure_setup
args=("$chapters" --book "$BOOK")
case "$choice" in 2|4|6) args+=("--no-verify") ;; esac
case "$choice" in 3|4|5|6) args+=("--skip-done") ;; esac
export PYTORCH_ENABLE_MPS_FALLBACK=1
echo "==> Building: ${args[*]}  (loading the models takes a minute)"
caffeinate -i "$PYV" "$KIT/kit/render.py" "${args[@]}"
