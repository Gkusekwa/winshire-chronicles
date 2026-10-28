"""Render the Book 1 audiobook with ElevenLabs, chapter by chapter, from the performance scripts.

    export ELEVENLABS_API_KEY=...            # never commit the key
    python3 render_elevenlabs.py --estimate                  # characters (about the credits) per chapter; no API calls
    python3 render_elevenlabs.py --chapters 1 --cast single  # one narrator for everything
    python3 render_elevenlabs.py --chapters 1-5 --cast full  # a voice per role from voices.json
    python3 render_elevenlabs.py --all --model eleven_v3     # expressive model with audio tags
    python3 render_elevenlabs.py --chapters 1 --cast full --model eleven_v3 --dialogue   # multi-voice turns in one request

Reads   Book 1/audiobook/Performance/NN.json and Book 1/audiobook/ElevenLabs/voices.json
Writes  Book 1/audiobook/ElevenLabs/out/NN_Chapter_NN_Title.mp3 (loudness-normalised, silence-padded)
Caches  every paid request under ElevenLabs/cache/ (keyed by text, voice, model and settings), so a re-run
        after a failure or an edit only pays for what changed.  ffmpeg must be installed.

Delivery:
  * scene, title and heavy pauses, and every change of voice, are real silence from the script; within one voice's run of
    ordinary paragraphs the model's own paragraph pause is used (break tags destabilise long requests);
  * names are respelt inline from names.py aliases before sending (works on every model);
  * eleven_v3 gets audio tags ([softly], [whispers] ...) from the annotations; other models get none.
"""
import argparse, hashlib, json, os, re, subprocess, sys, tempfile, time, urllib.request, urllib.error

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from segment import REPO
from cast import role_of
from names import NAMES

AB = os.path.join(REPO, "Book 1", "audiobook")
EL = os.path.join(AB, "ElevenLabs")
API = "https://api.elevenlabs.io/v1"

# ---- v3 audio tags: edit to taste ----
TYPE_TAG = {"bond": "softly", "thought": "quietly", "remembered": "quietly", "verse": "slowly", "written": None}
MOOD_TAG = {"tension": "tense", "dread": "hushed", "quiet": "quietly", "tender": "tenderly", "grief": "sadly",
            "humour": "dryly", "anger": "angry", "urgent": "urgently", "awe": "in awe", "reflective": "thoughtful", "action": None}
MAX_CHARS = 2400          # per request; keeps v2 and v3 well inside their limits
MID_PARA_GAP = 120        # ms of silence when the voice changes inside a paragraph


def alias_rx():
    al = sorted([(n, a) for n, _, _, a, _ in NAMES if a], key=lambda x: -len(x[0]))
    return re.compile(r"\b(" + "|".join(re.escape(n) for n, _ in al) + r")\b"), dict(al)


RX, AMAP = alias_rx()


def speakable(t):
    return RX.sub(lambda m: AMAP[m.group(1)], t)


def chapter_files():
    out = {}
    for f in sorted(os.listdir(os.path.join(AB, "Performance"))):
        if f.endswith(".json"):
            out[int(f[:2])] = os.path.join(AB, "Performance", f)
    return out


def voice_for(seg, cast):
    if cast == "single" or seg["type"] in ("narration", "title", "written", "term"):
        return "Narrator"
    if seg["type"] == "verse" and not seg.get("speaker"):
        return "Narrator"
    return role_of(seg.get("speaker", ""))


def tag_for(seg, v3, first_in_para=True):
    if not v3:
        return ""
    tags = []
    how = seg.get("how", "")
    if how and len(how.split()) <= 4:
        tags.append(how)
    elif seg["type"] in TYPE_TAG and TYPE_TAG[seg["type"]]:
        tags.append(TYPE_TAG[seg["type"]])
    m = MOOD_TAG.get(seg.get("mood", "")) if first_in_para else None
    if m and not tags:
        tags.append(m)
    return "".join(f"[{t}] " for t in tags)


def plan(chapter_json, cast, v3, dialogue=False):
    """Group segments into requests, broken at pauses longer than a paragraph and at MAX_CHARS.
    Normal mode: one voice per request. Dialogue mode (eleven_v3): several voices per request, as a list of turns."""
    segs = json.load(open(chapter_json, encoding="utf-8"))["segments"]
    reqs, cur, last_para = [], None, None
    for s in segs:
        v = voice_for(s, cast)
        first = s.get("para") != last_para
        last_para = s.get("para")
        text = tag_for(s, v3, first) + speakable(s["text"])
        pause = s.get("pause_after_ms", 0)
        size = sum(len(t) for _, t in cur["turns"]) if cur else 0
        joinable = cur and size + len(text) < MAX_CHARS and cur["pause"] <= 600
        if joinable and cur["turns"][-1][0] == v:
            cur["turns"][-1][1] += ("\n\n" if cur["pause"] else " ") + text   # paragraph breaks only; break tags destabilise long requests
            cur["pause"] = pause
        elif joinable and dialogue:
            cur["turns"].append([v, text])
            cur["pause"] = pause
        else:
            if cur:
                reqs.append(cur)
            cur = {"turns": [[v, text]], "pause": pause}
    if cur:
        reqs.append(cur)
    for r in reqs:
        r["gap_ms"] = r["pause"] if r["pause"] else MID_PARA_GAP
        r["voice"] = r["turns"][0][0]
        r["text"] = "\n".join(t for _, t in r["turns"])
    return reqs


def post(url, key, body, accept="audio/mpeg"):
    req = urllib.request.Request(url, data=json.dumps(body).encode(), method="POST",
                                 headers={"xi-api-key": key, "Content-Type": "application/json", "Accept": accept})
    for attempt in range(6):
        try:
            with urllib.request.urlopen(req, timeout=300) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503) and attempt < 5:
                time.sleep(2 ** attempt * 3); continue
            raise SystemExit(f"ElevenLabs error {e.code}: {e.read()[:400].decode(errors='replace')}")
        except urllib.error.URLError:
            if attempt < 5:
                time.sleep(2 ** attempt * 3); continue
            raise


def voice_entry(voices, role):
    v = voices["roles"].get(role) or {}
    if not v.get("voice_id"):
        v = voices["roles"]["Narrator"]
    if not v.get("voice_id"):
        raise SystemExit("voices.json: the Narrator needs a voice_id")
    return v


def render_dialogue(r, voices, key, cache):
    inputs = [{"text": t, "voice_id": voice_entry(voices, role)["voice_id"]} for role, t in r["turns"]]
    body = {"inputs": inputs, "model_id": "eleven_v3",
            "settings": {"stability": voices.get("defaults", {}).get("stability", 0.5)}}
    h = hashlib.sha256(json.dumps(body, sort_keys=True).encode()).hexdigest()[:24]
    path = os.path.join(cache, "d_" + h + ".mp3")
    if not os.path.exists(path):
        audio = post(f"{API}/text-to-dialogue?output_format={voices.get('output_format', 'mp3_44100_128')}", key, body)
        open(path + ".part", "wb").write(audio); os.replace(path + ".part", path)
    return path


def render_request(r, prev_text, next_text, voices, model, key, cache):
    v = voice_entry(voices, r["voice"])
    settings = {**voices.get("defaults", {}), **v.get("settings", {})}
    body = {"text": r["text"], "model_id": model, "voice_settings": settings}
    if not model.startswith("eleven_v3"):
        body["previous_text"], body["next_text"] = prev_text[-600:], next_text[:600]
    h = hashlib.sha256(json.dumps([v["voice_id"], body], sort_keys=True).encode()).hexdigest()[:24]
    path = os.path.join(cache, h + ".mp3")
    if not os.path.exists(path):
        audio = post(f"{API}/text-to-speech/{v['voice_id']}?output_format={voices.get('output_format', 'mp3_44100_128')}", key, body)
        open(path + ".part", "wb").write(audio); os.replace(path + ".part", path)
    return path


def assemble(parts, out_mp3, bitrate):
    """parts: list of (mp3_path, gap_ms). Concatenate with silence, normalise loudness for audiobook stores."""
    with tempfile.TemporaryDirectory() as td:
        lst = []
        sil = {}
        for i, (p, gap) in enumerate(parts):
            lst.append(os.path.abspath(p))
            if gap:
                if gap not in sil:
                    sp = os.path.join(td, f"sil_{gap}.mp3")
                    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-f", "lavfi", "-i", "anullsrc=r=44100:cl=mono",
                                    "-t", f"{gap / 1000:.3f}", "-ar", "44100", "-ac", "1", "-b:a", "128k", sp], check=True)
                    sil[gap] = sp
                lst.append(sil[gap])
        # 0.5 s room tone at the start, about 2 s at the end (common store requirements)
        head = os.path.join(td, "head.mp3")
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-f", "lavfi", "-i", "anullsrc=r=44100:cl=mono", "-t", "0.6", "-ar", "44100", "-ac", "1", "-b:a", "128k", head], check=True)
        lst = [head] + lst
        if lst[-1] not in sil.values():
            lst.append(head)
        listfile = os.path.join(td, "list.txt")
        open(listfile, "w").write("".join(f"file '{x}'\n" for x in lst))
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-f", "concat", "-safe", "0", "-i", listfile,
                        "-af", "loudnorm=I=-20:TP=-3:LRA=11", "-ar", "44100", "-ac", "1", "-b:a", bitrate, "-c:a", "libmp3lame",
                        out_mp3], check=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--chapters", help="e.g. 1 or 1-5 or 1,3,7")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--cast", choices=["single", "full"], default="single")
    ap.add_argument("--model", default="eleven_multilingual_v2")
    ap.add_argument("--estimate", action="store_true", help="count characters only; no API calls")
    ap.add_argument("--dialogue", action="store_true", help="eleven_v3 only: voice several speakers per request (text-to-dialogue)")
    ap.add_argument("--bitrate", default="192k")
    a = ap.parse_args()
    chs = chapter_files()
    if a.all or a.estimate and not a.chapters:
        todo = list(chs)
    elif a.chapters:
        todo = []
        for part in a.chapters.split(","):
            x, _, y = part.partition("-")
            todo += list(range(int(x), int(y or x) + 1))
    else:
        ap.error("give --chapters or --all")
    v3 = a.model.startswith("eleven_v3")
    if a.dialogue and not v3:
        ap.error("--dialogue needs --model eleven_v3")
    if a.estimate:
        tot = 0
        for n in todo:
            reqs = plan(chs[n], a.cast, v3, a.dialogue)
            c = sum(len(r["text"]) for r in reqs)
            tot += c
            print(f"chapter {n:2d}: {len(reqs):4d} requests, {c:7,d} characters")
        print(f"total: {tot:,d} characters (about the same number of credits on most plans; check yours)")
        return
    key = os.environ.get("ELEVENLABS_API_KEY") or sys.exit("set ELEVENLABS_API_KEY")
    voices = json.load(open(os.path.join(EL, "voices.json"), encoding="utf-8"))
    cache = os.path.join(EL, "cache"); os.makedirs(cache, exist_ok=True)
    outd = os.path.join(EL, "out"); os.makedirs(outd, exist_ok=True)
    scripts = sorted(os.listdir(os.path.join(AB, "Scripts")))
    for n in todo:
        reqs = plan(chs[n], a.cast, v3, a.dialogue)
        parts = []
        for i, r in enumerate(reqs):
            prev_t = reqs[i - 1]["text"] if i else ""
            next_t = reqs[i + 1]["text"] if i + 1 < len(reqs) else ""
            if len(r["turns"]) > 1:
                parts.append((render_dialogue(r, voices, key, cache), r["gap_ms"]))
            else:
                parts.append((render_request(r, prev_t, next_t, voices, a.model, key, cache), r["gap_ms"]))
            print(f"\rchapter {n}: {i + 1}/{len(reqs)}", end="", flush=True)
        name = next(s for s in scripts if s.startswith(f"{n:02d}_")).replace(".ssml", ".mp3")
        assemble(parts, os.path.join(outd, name), a.bitrate)
        print(f"\rchapter {n}: done -> ElevenLabs/out/{name}")


if __name__ == "__main__":
    main()
