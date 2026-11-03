#!/bin/bash
# One-time setup on a Linux machine with an NVIDIA GPU (a rented cloud GPU, e.g. RunPod or Vast.ai, with an image
# that has the NVIDIA driver: any "PyTorch" or "CUDA" template). Installs ffmpeg, Python 3.11, Chatterbox and Whisper
# in ~/chatterbox. audiobook.sh runs this for you when something is missing. Safe to run again.
set -e
C="$HOME/chatterbox"
mkdir -p "$C"
SUDO=""; [ "$(id -u)" = 0 ] || SUDO="sudo"
if ! command -v nvidia-smi >/dev/null || ! nvidia-smi >/dev/null 2>&1; then
  echo "No NVIDIA GPU found (nvidia-smi doesn't work). Rent a machine with an NVIDIA GPU and its driver, then run this again."
  exit 1
fi
need=""
command -v ffmpeg >/dev/null || need="$need ffmpeg"
PY=""
for v in 3.11 3.12; do command -v "python$v" >/dev/null 2>&1 && { PY="python$v"; break; }; done
if [ -n "$PY" ] && ! "$PY" -c "import venv, ensurepip" 2>/dev/null; then need="$need ${PY}-venv"; fi
if [ -z "$PY" ]; then need="$need python3.11 python3.11-venv"; fi
if [ -n "$need" ]; then
  echo "==> Installing:$need"
  $SUDO apt-get update -qq
  if ! $SUDO apt-get install -y -qq $need; then
    # older Ubuntu has no python3.11 package: add the deadsnakes repository
    $SUDO apt-get install -y -qq software-properties-common && $SUDO add-apt-repository -y ppa:deadsnakes/ppa \
      && $SUDO apt-get update -qq && $SUDO apt-get install -y -qq $need
  fi
  [ -n "$PY" ] || PY=python3.11
fi
if [ ! -x "$C/venv/bin/python" ] || ! "$C/venv/bin/python" -c 'import sys; sys.exit(not (3,11) <= sys.version_info[:2] <= (3,12))'; then
  echo "==> Making the Python environment in $C/venv"
  rm -rf "$C/venv"
  "$PY" -m venv "$C/venv"
  "$C/venv/bin/pip" install -q --upgrade pip
fi
echo "==> Checking packages (Chatterbox, Whisper); the first time this downloads a few GB..."
set -o pipefail
# chatterbox-tts 0.1.7 brings torch 2.6 built for CUDA 12; faster-whisper uses the cuBLAS and cuDNN that come with it
if ! "$C/venv/bin/pip" install --progress-bar on "chatterbox-tts==0.1.7" "setuptools<81" "faster-whisper==1.2.1" \
     | { grep -v "^Requirement already satisfied" || true; }; then
  echo "Setup FAILED: the packages didn't install (see the messages above). Fix the problem and run this again."; exit 1
fi
if ! "$C/venv/bin/python" -c "import chatterbox, faster_whisper, perth, torch; assert perth.PerthImplicitWatermarker; assert torch.cuda.is_available()" 2>/dev/null; then
  echo "Setup FAILED: the packages installed but don't load, or PyTorch can't see the GPU. Run this again; if it keeps"
  echo "failing, delete $C/venv and run it once more."; exit 1
fi
# let faster-whisper find the CUDA libraries PyTorch installed
SITE="$("$C/venv/bin/python" -c 'import site; print(site.getsitepackages()[0])')"
LIBS="$(ls -d "$SITE"/nvidia/*/lib 2>/dev/null | tr '\n' ':')"
echo "export LD_LIBRARY_PATH=\"${LIBS}\${LD_LIBRARY_PATH}\"" > "$C/cuda_libs.sh"
GPUS="$(nvidia-smi --query-gpu=name --format=csv,noheader | sort | uniq -c | sed 's/^ *//' | tr '\n' ';')"
echo "==> Setup done. GPUs: ${GPUS%;}. (Chatterbox's model, about 3 GB, and Whisper's, about 500 MB, download the first time they're used.)"
