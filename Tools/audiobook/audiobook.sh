#!/bin/bash
# The Watch Below audiobook: build chapters with Chatterbox, with or without verification.
#
# Menu:            bash Tools/audiobook/audiobook.sh
# Or directly:     bash Tools/audiobook/audiobook.sh <choice> [chapters]
#   1  one chapter, verified            e.g.  ... 1 7
#   2  one chapter, not verified        e.g.  ... 2 7
#   3  several chapters, verified       e.g.  ... 3 2-10      or  ... 3 2,5,9
#   4  several chapters, not verified   e.g.  ... 4 2-10
#   5  the whole book, verified         e.g.  ... 5
#   6  the whole book, not verified     e.g.  ... 6
#
# Verified: every take is checked (length, silences, and the words, by Whisper) and retaken up to three times;
# each chapter ends PASS or FAIL in Book 1/audiobook/Chatterbox/out/NN_check.txt.
# Not verified: one take per passage, no checks, faster; chapters are marked UNCHECKED (drafts).
# Several chapters and the whole book resume: chapters that already PASSED with unchanged inputs are skipped.
set -e
cd "$(dirname "$0")/../.."
choice="$1"; chapters="$2"

if [ -z "$choice" ]; then
  echo "The Watch Below audiobook (Chatterbox)"
  echo "  1) Build one chapter and verify"
  echo "  2) Build one chapter without verifying"
  echo "  3) Build several chapters and verify"
  echo "  4) Build several chapters without verifying"
  echo "  5) Build the entire book and verify"
  echo "  6) Build the entire book without verifying"
  read -r -p "Choose 1-6: " choice
fi

case "$choice" in
  1|2)
    [ -n "$chapters" ] || read -r -p "Chapter number (1-79; 0 = opening credits, 99 = closing): " chapters
    [[ "$chapters" =~ ^[0-9]+$ ]] || { echo "One chapter number, please (e.g. 7)."; exit 1; } ;;
  3|4)
    [ -n "$chapters" ] || read -r -p "Chapters (e.g. 2-10, or 2,5,9, or 1-3,7): " chapters
    [[ "$chapters" =~ ^[0-9,-]+$ ]] || { echo "Chapters like 2-10 or 2,5,9, please."; exit 1; } ;;
  5|6) chapters="--all" ;;
  *) echo "Choose 1 to 6."; exit 1 ;;
esac

args=("$chapters")
case "$choice" in 2|4|6) args+=("--no-verify") ;; esac
case "$choice" in 3|4|5|6) args+=("--skip-done") ;; esac

echo "==> Building: ${args[*]}"
bash Tools/audiobook/chatterbox_mac.sh "${args[@]}"
