#!/bin/bash
# One-time setup on a Mac (Apple silicon): ffmpeg, Python 3.11 or 3.12, Chatterbox and Whisper, in ~/chatterbox.
# audiobook.sh runs this for you when something is missing. Safe to run again.
set -e
C="$HOME/chatterbox"
mkdir -p "$C"
if ! command -v ffmpeg >/dev/null; then
  if command -v brew >/dev/null; then echo "==> Installing ffmpeg"; brew install ffmpeg
  else echo "Install Homebrew first (https://brew.sh), then run this again."; exit 1; fi
fi
PY=""
for v in 3.11 3.12; do
  for c in "python$v" "/opt/homebrew/bin/python$v" "/usr/local/bin/python$v"; do
    if command -v "$c" >/dev/null 2>&1; then PY="$c"; break 2; fi
  done
done
if [ -z "$PY" ]; then
  if command -v brew >/dev/null; then echo "==> Installing Python 3.11"; brew install python@3.11; PY="$(brew --prefix)/bin/python3.11"
  else echo "Install Python 3.11 first (https://brew.sh, then: brew install python@3.11)"; exit 1; fi
fi
if [ ! -x "$C/venv/bin/python" ] || ! "$C/venv/bin/python" -c 'import sys; sys.exit(not (3,11) <= sys.version_info[:2] <= (3,12))'; then
  echo "==> Making the Python environment in $C/venv"
  rm -rf "$C/venv"
  "$PY" -m venv "$C/venv"
  "$C/venv/bin/pip" install -q --upgrade pip
fi
echo "==> Checking packages (Chatterbox, Whisper); the first time this downloads several hundred MB..."
set -o pipefail
if ! "$C/venv/bin/pip" install --progress-bar on "chatterbox-tts==0.1.7" "setuptools<81" "faster-whisper==1.2.1" \
     | { grep -v "^Requirement already satisfied" || true; }; then
  echo "Setup FAILED: the packages didn't install (see the messages above). Fix the problem and run this again."; exit 1
fi
# setuptools<81: Chatterbox's watermarker needs pkg_resources.
if ! "$C/venv/bin/python" -c "import chatterbox, faster_whisper, perth; assert perth.PerthImplicitWatermarker" 2>/dev/null; then
  echo "Setup FAILED: the packages installed but don't load (Chatterbox, Whisper or the watermarker). Run this again;"
  echo "if it keeps failing, delete $C/venv and run it once more."; exit 1
fi
echo "==> Setup done. (Chatterbox's model, about 3 GB, and Whisper's, about 500 MB, download the first time they're used.)"
