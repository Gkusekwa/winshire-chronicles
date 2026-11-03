#!/bin/bash
# Build the audiobooks on a rented machine with one or more NVIDIA GPUs, all of them at once.
#
#   bash Tools/audiobook-kit/gpu.sh start "Book 1" "Book 2" "Book 3"   share the chapters still to build among the GPUs
#                                                                       and build them, verified, in the background
#   bash Tools/audiobook-kit/gpu.sh status                             what each GPU is doing, and the books' progress
#   bash Tools/audiobook-kit/gpu.sh stop                               stop (finished chapters are kept)
#   bash Tools/audiobook-kit/gpu.sh verify "Book 1" "Book 2" "Book 3"  re-check every built chapter (option 7), one
#                                                                       book per GPU
# Options for start:  --per-gpu N   workers on each GPU (default 1; a 24 GB card can usually take 2 or 3)
#
# The builds keep running if you close the terminal or lose the connection. Run start again after a stop, or after
# changing a respelling: chapters that passed are skipped. Logs: ~/audiobook-gpu/worker-N.log
set -e
KIT="$(cd "$(dirname "$0")" && pwd)"
PYV="$HOME/chatterbox/venv/bin/python"
W="$HOME/audiobook-gpu"
mkdir -p "$W"
cmd="$1"; shift || true

setup() {
  if [ ! -x "$PYV" ] || ! "$PYV" -c "import chatterbox, faster_whisper, perth, torch; assert torch.cuda.is_available()" 2>/dev/null; then
    bash "$KIT/setup_linux.sh"
  fi
  [ -f "$HOME/chatterbox/cuda_libs.sh" ] && . "$HOME/chatterbox/cuda_libs.sh"
  NGPU="$(nvidia-smi --list-gpus | wc -l)"
}

case "$cmd" in
  start)
    per=1; books=()
    while [ $# -gt 0 ]; do
      case "$1" in --per-gpu) per="$2"; shift 2 ;; *) books+=("$1"); shift ;; esac
    done
    [ ${#books[@]} -gt 0 ] || { echo "Name the books' folders, e.g.  gpu.sh start \"Book 1\" \"Book 2\""; exit 1; }
    if pgrep -f "audiobook-gpu/worker" >/dev/null; then echo "Workers are already running (gpu.sh status, or gpu.sh stop)."; exit 1; fi
    setup
    for b in "${books[@]}"; do
      [ -f "$KIT/voices/narrator.wav" ] || [ -n "$(python3 -c "import json;print(json.load(open('$b/audiobook/book.json')).get('narrator',''))" 2>/dev/null)" ] \
        || { echo "The narrator's clip is missing: copy narrator.wav into $KIT/voices/ (it isn't in git)."; exit 1; }
    done
    N=$((NGPU * per))
    echo "==> Sharing the work among $N worker(s) on $NGPU GPU(s)"
    "$PYV" "$KIT/kit/gpu_plan.py" "$N" "${books[@]}" > "$W/plan.tsv"
    rm -f "$W"/worker-*.sh
    while IFS=$'\t' read -r w rest; do
      [ -n "$rest" ] || continue
      g=$((w / per))
      f="$W/worker-$w.sh"
      {
        echo "#!/bin/bash"
        echo "export CUDA_VISIBLE_DEVICES=$g PYTHONWARNINGS=ignore TQDM_DISABLE=1 HF_HUB_DISABLE_PROGRESS_BARS=1"
        echo "[ -f \"$HOME/chatterbox/cuda_libs.sh\" ] && . \"$HOME/chatterbox/cuda_libs.sh\""
        IFS=$'\t' read -r -a parts <<< "$rest"
        for ((i = 0; i < ${#parts[@]}; i += 2)); do
          printf '%q %q %q --book %q --skip-done\n' "$PYV" "$KIT/kit/render.py" "${parts[i+1]}" "${parts[i]}"
        done
        echo "echo '==> worker $w finished'"
      } > "$f"
      nohup setsid bash "$f" > "$W/worker-$w.log" 2>&1 < /dev/null &
      echo "  worker $w on GPU $g: $(echo "$rest" | awk -F'\t' '{for(i=1;i<NF;i+=2){n=split($(i+1),a,","); printf "%s%s (%d chapters)", (i>1?", ":""), $i, n}}' | sed "s#$PWD/##g")"
    done < "$W/plan.tsv"
    echo "==> Started. Follow it with:  bash $0 status"
    ;;
  status)
    for f in "$W"/worker-*.log; do
      [ -f "$f" ] || { echo "Nothing started yet."; exit 0; }
      w="$(basename "$f" .log)"
      last="$(tr '\r' '\n' < "$f" | grep -E "^[0-9]{2}: (PASS|FAIL|UNCHECKED)|chapter [0-9]+: [0-9]+/[0-9]+|finished|Error|error" | tail -1)"
      printf '%-10s %s\n' "$w" "${last:-starting…}"
    done
    pgrep -f "audiobook-gpu/worker" >/dev/null && echo "(running)" || echo "(no workers running)"
    nvidia-smi --query-gpu=index,utilization.gpu,memory.used,memory.total --format=csv,noheader | sed 's/^/  GPU /'
    for b in "$@"; do :; done
    ;;
  stop)
    pkill -f "audiobook-gpu/worker" || true
    pkill -f "kit/render.py" || true
    echo "Stopped. Finished chapters are kept; run start again to carry on."
    ;;
  verify)
    [ $# -gt 0 ] || { echo "Name the books' folders, e.g.  gpu.sh verify \"Book 1\" \"Book 2\""; exit 1; }
    setup
    i=0
    for b in "$@"; do
      g=$((i % NGPU))
      CUDA_VISIBLE_DEVICES=$g nohup setsid "$PYV" "$KIT/kit/verify.py" --all --book "$b" > "$W/verify-$i.log" 2>&1 < /dev/null &
      echo "  verifying $b on GPU $g (log: $W/verify-$i.log)"
      i=$((i + 1))
    done
    ;;
  *)
    sed -n '2,15p' "$0"; exit 1 ;;
esac
