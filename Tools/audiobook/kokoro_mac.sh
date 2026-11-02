#!/bin/bash
# Render the Book 1 audiobook with Kokoro on this Mac (free, offline after setup).
# Run from Terminal:   bash "Tools/audiobook/kokoro_mac.sh" audition  (the audition set first)
#                      bash "Tools/audiobook/kokoro_mac.sh"           (all chapters)
#                      bash "Tools/audiobook/kokoro_mac.sh" 2-10      (a range)
# Safe to stop with Ctrl-C and run again: finished, up-to-date chapters are skipped.
# Another voice: VOICE=bm_george bash "Tools/audiobook/kokoro_mac.sh" audition
# The audio lands in "Book 1/audiobook/Kokoro/out/" (ignored by git: never commit it).
set -e
cd "$(dirname "$0")/../.."
K="$HOME/kokoro"
mkdir -p "$K"
if ! command -v ffmpeg >/dev/null; then
  if command -v brew >/dev/null; then brew install ffmpeg
  else echo "Install ffmpeg first (https://brew.sh, then: brew install ffmpeg)"; exit 1; fi
fi
# kokoro-onnx 0.6.1 needs Python 3.10-3.13; the Mac's default python3 may be newer, so pick a supported one.
PY=""
for v in 3.12 3.13 3.11 3.10; do
  for c in "python$v" "/opt/homebrew/bin/python$v" "/usr/local/bin/python$v"; do
    if command -v "$c" >/dev/null 2>&1; then PY="$c"; break 2; fi
  done
done
if [ -z "$PY" ]; then
  if command -v brew >/dev/null; then brew install python@3.12; PY="$(brew --prefix)/bin/python3.12"
  else echo "Install Python 3.12 first (https://brew.sh, then: brew install python@3.12)"; exit 1; fi
fi
if [ ! -x "$K/venv/bin/python" ] || ! "$K/venv/bin/python" -c 'import sys; sys.exit(not (3,10) <= sys.version_info[:2] <= (3,13))'; then
  rm -rf "$K/venv"
  "$PY" -m venv "$K/venv"
  "$K/venv/bin/pip" install -q --upgrade pip
fi
"$K/venv/bin/pip" install -q "kokoro-onnx==0.6.1" "soundfile==0.14.0"
for f in kokoro-v1.0.onnx voices-v1.0.bin; do
  [ -s "$K/$f" ] || curl -L --fail -o "$K/$f" "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/$f"
done
if [ "$1" = "audition" ]; then
  caffeinate -i "$K/venv/bin/python" Tools/audiobook/render_kokoro.py --audition --models "$K" --voice "${VOICE:-bf_emma}"
else
  caffeinate -i "$K/venv/bin/python" Tools/audiobook/render_kokoro.py "${1:---all}" --skip-done --models "$K" --voice "${VOICE:-bf_emma}"
fi
