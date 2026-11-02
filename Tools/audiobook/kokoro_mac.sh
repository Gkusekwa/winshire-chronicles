#!/bin/bash
# Render the Book 1 audiobook with Kokoro on this Mac (free, offline after setup).
# Run from Terminal:   bash "Tools/audiobook/kokoro_mac.sh"           (all chapters)
#                      bash "Tools/audiobook/kokoro_mac.sh" 2-10      (a range)
# Safe to stop with Ctrl-C and run again: finished chapters are skipped.
# The audio lands in "Book 1/audiobook/Kokoro/out/" (ignored by git: never commit it).
set -e
cd "$(dirname "$0")/../.."
K="$HOME/kokoro"
mkdir -p "$K"
if ! command -v ffmpeg >/dev/null; then
  if command -v brew >/dev/null; then brew install ffmpeg
  else echo "Install ffmpeg first (https://brew.sh, then: brew install ffmpeg)"; exit 1; fi
fi
if [ ! -x "$K/venv/bin/python" ]; then
  python3 -m venv "$K/venv"
  "$K/venv/bin/pip" install -q --upgrade pip
  "$K/venv/bin/pip" install -q kokoro-onnx soundfile
fi
for f in kokoro-v1.0.onnx voices-v1.0.bin; do
  [ -s "$K/$f" ] || curl -L --fail -o "$K/$f" "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/$f"
done
caffeinate -i "$K/venv/bin/python" Tools/audiobook/render_kokoro.py "${1:---all}" --skip-done --models "$K" --voice "${VOICE:-bf_emma}"
