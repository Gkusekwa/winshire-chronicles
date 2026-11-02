#!/bin/bash
# Render Book 1 audiobook passages with Chatterbox on this Mac (free; the model downloads once from Hugging Face).
# Run from Terminal:   bash "Tools/audiobook/chatterbox_mac.sh"            (the audition set, to compare with Kokoro)
#                      bash "Tools/audiobook/chatterbox_mac.sh" 1          (chapter 1)
#                      bash "Tools/audiobook/chatterbox_mac.sh" 1-79 --skip-done
# Uses the Mac's graphics chip (MPS) when it can. The audio lands in "Book 1/audiobook/Chatterbox/out/"
# (ignored by git: never commit it).
set -e
cd "$(dirname "$0")/../.."
C="$HOME/chatterbox"
mkdir -p "$C"
if ! command -v ffmpeg >/dev/null; then
  if command -v brew >/dev/null; then brew install ffmpeg
  else echo "Install ffmpeg first (https://brew.sh, then: brew install ffmpeg)"; exit 1; fi
fi
# chatterbox-tts 0.1.7 pins torch 2.6 and numpy < 2: use Python 3.11 or 3.12.
PY=""
for v in 3.11 3.12; do
  for c in "python$v" "/opt/homebrew/bin/python$v" "/usr/local/bin/python$v"; do
    if command -v "$c" >/dev/null 2>&1; then PY="$c"; break 2; fi
  done
done
if [ -z "$PY" ]; then
  if command -v brew >/dev/null; then brew install python@3.11; PY="$(brew --prefix)/bin/python3.11"
  else echo "Install Python 3.11 first (https://brew.sh, then: brew install python@3.11)"; exit 1; fi
fi
if [ ! -x "$C/venv/bin/python" ]; then
  "$PY" -m venv "$C/venv"
  "$C/venv/bin/pip" install -q --upgrade pip
fi
"$C/venv/bin/pip" install -q "chatterbox-tts==0.1.7" "setuptools<81"   # Chatterbox's watermarker needs pkg_resources
# Reference clips (the Kokoro cast reading the same lines), so both engines use the same voices.
if [ ! -s "Book 1/audiobook/Chatterbox/refs/Narrator.wav" ]; then
  bash Tools/audiobook/kokoro_mac.sh refs
fi
export PYTORCH_ENABLE_MPS_FALLBACK=1
if [ $# -eq 0 ]; then set -- --audition; fi
caffeinate -i "$C/venv/bin/python" Tools/audiobook/render_chatterbox.py "$@"
