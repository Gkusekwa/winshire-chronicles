"""Build the Book 1 audiobook scripts from the manuscript and the annotations.

    python3 build.py                     # standard SSML + performance scripts + guide + lexicons
    python3 build.py --check             # also verify every spoken word matches the manuscript
    python3 build.py --variant google    # SSML with names respelt inline (<sub alias>), for engines without lexicons
    python3 build.py --variant azure --voice en-GB-RyanNeural   # SSML wrapped in an Azure <voice> element

Inputs:  Book 1/Chapters/*.md, Book 1/audiobook/annotations/chNN.json, Tools/audiobook/names.py, Tools/atlas/plan_data.py
Outputs: Book 1/audiobook/Scripts/*.ssml            (standard variant)
         Book 1/audiobook/Performance/*.json        (segment-by-segment script with speaker, delivery and pauses)
         Book 1/audiobook/Pronunciation_Guide.md, Lexicon_IPA.pls, Lexicon_Alias.pls
         Book 1/audiobook/Variants/<variant>/*.ssml (other variants)
"""
import json, os, re, sys, html
from xml.dom import minidom

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from segment import chapter_files, segment, REPO
from check_annotations import parse_span
from names import NAMES
sys.path.insert(0, os.path.join(REPO, "Tools", "atlas"))
from plan_data import PARTS

AB = os.path.join(REPO, "Book 1", "audiobook")
ANN = os.path.join(AB, "annotations")
TITLE, SERIES, AUTHOR, NEXT = "The Watch Below", "The Winshire Chronicles", "Goodluck Kusekwa", "The Hunt Beneath"

# ---- pauses (ms); every break is 3 s or less so all engines accept it ----
P_PARA, P_SCENE, P_AFTER_PART, P_AFTER_NUM, P_AFTER_TITLE, P_HEAVY = 500, 1600, 2000, 800, 1800, 800

# ---- delivery: how each span type is rendered in SSML (standard SSML 1.1 prosody/emphasis) ----
SPAN_PROSODY = {
    "bond": {"rate": "94%", "volume": "-2dB"},       # mind to mind: closer, a touch slower
    "thought": {"rate": "97%", "volume": "-4dB"},    # inside the head: quieter still
    "verse": {"rate": "90%"},                        # songs, rhymes, prophecy
    "written": {"rate": "95%"},                      # read off a page or stone
    "remembered": {"volume": "-3dB"},                # words heard again in memory
}
MOOD_PROSODY = {
    "quiet": {"rate": "95%"}, "tender": {"rate": "95%"}, "grief": {"rate": "94%"}, "reflective": {"rate": "96%"},
    "tension": {"rate": "97%"}, "dread": {"rate": "96%"}, "awe": {"rate": "95%"},
    "action": {"rate": "104%"}, "urgent": {"rate": "105%"},
}
HEAVY_MOODS = {"grief", "dread", "awe", "tension"}   # a little more silence after these
HOW_SOFT = re.compile(r"whisper|murmur|breath|very quiet|quietly|softly|low|hush", re.I)
HOW_LOUD = re.compile(r"shout|yell|roar|bellow|scream|cr(y|ied)|call(ed)? out", re.I)

NUM = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
TENS = "_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()


def words(n):
    if n < 20: return NUM[n]
    t, u = divmod(n, 10)
    return TENS[t] + ("-" + NUM[u] if u else "")


def slug(n, title):
    return f"{n:02d}_Chapter_{n:02d}_" + re.sub(r"[^A-Za-z0-9]+", "_", title).strip("_")


# ---------------- text ----------------
def clean(t):
    """Markdown to speakable text. Words are never changed; only marks and case of shouted capitals."""
    t = t.replace("**", "")
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"\1", t)
    t = t.replace("...", "\u2026")
    # curly quotes and apostrophes, as the ebook has them
    t = t.replace("'", "\u2019")
    t = re.sub(r"(^|[\s(\[\u2014])\u2019", "\\1\u2018", t)
    t = re.sub(r'"(?=\w|\u2018|\u2026|[\[(])', "\u201c", t)
    t = t.replace('"', "\u201d")
    return t


def caps(text, loud):
    """Capitals words (LOOK, ENEMY) would be spelt out by some engines; speak them as words, stressed in speech."""
    def f(m):
        w = m.group(0)
        if w == "I": return w
        word = w.capitalize()
        return f'<emphasis level="moderate">{word}</emphasis>' if loud else word
    return re.sub(r"\b[A-Z]{2,}\b", f, text)


def esc(t):
    return html.escape(t, quote=False)


def attrs(d):
    return " ".join(f'{k}="{v}"' for k, v in d.items())


# ---------------- names ----------------
NAME_RX = None


def name_rx():
    global NAME_RX
    alias = [(n, a) for n, _, _, a, _ in NAMES if a]
    alias.sort(key=lambda x: -len(x[0]))
    NAME_RX = (re.compile(r"\b(" + "|".join(re.escape(n) for n, _ in alias) + r")\b"), dict(alias))
    return NAME_RX


def inline_names(ssml_text):
    rx, amap = NAME_RX or name_rx()
    # only touch text outside tags
    parts = re.split(r"(<[^>]+>)", ssml_text)
    for i, p in enumerate(parts):
        if not p.startswith("<"):
            parts[i] = rx.sub(lambda m: f'<sub alias="{amap[m.group(1)]}">{m.group(1)}</sub>', p)
    return "".join(parts)


# ---------------- per chapter ----------------
def load_ann(n):
    f = os.path.join(ANN, f"ch{n:02d}.json")
    return json.load(open(f, encoding="utf-8"))


def top_level(spans):
    """Drop spans nested inside another span (an italic inside a quote) but remember them as inner."""
    out = []
    for s in spans:
        if out and s["start"] >= out[-1]["start"] and s["end"] <= out[-1]["end"]:
            out[-1].setdefault("inner", []).append(s)
        else:
            out.append(dict(s))
    return out


def para_runs(p, ann):
    """Split a paragraph into runs: (kind, speaker, listener, how, text_markdown, inner_spans)."""
    runs, pos, text = [], 0, p["text"]
    for s in top_level(p["spans"]):
        if s["start"] > pos:
            runs.append(("narration", "", "", "", text[pos:s["start"]], []))
        t, spk, to, how = parse_span(ann["spans"][s["id"]])
        runs.append((t, spk, to, how, text[s["start"]:s["end"]], [(x, parse_span(ann["spans"][x["id"]])) for x in s.get("inner", [])], ))
        pos = s["end"]
    if pos < len(text):
        runs.append(("narration", "", "", "", text[pos:], []))
    # merge adjacent narration and term/emphasis runs into the surrounding narration for the SSML text
    return runs


def run_ssml(kind, how, md, inner, base):
    """Render one run. inner = nested spans (usually emphasis inside speech)."""
    if inner:
        # mark nested emphasis spans in the markdown before cleaning
        pieces, pos = [], 0
        for s, (t, *_rest) in inner:
            a, e = s["start"] - base, s["end"] - base
            pieces.append(esc(clean(md[pos:a])))
            inner_txt = esc(clean(md[a:e]))
            if t in SPAN_PROSODY:
                pieces.append(f"<prosody {attrs(SPAN_PROSODY[t])}>{inner_txt}</prosody>")
            elif t == "emphasis":
                pieces.append(f'<emphasis level="moderate">{inner_txt}</emphasis>')
            else:
                pieces.append(inner_txt)
            pos = e
        pieces.append(esc(clean(md[pos:])))
        body = "".join(pieces)
    else:
        body = esc(clean(md))
    loud = kind in ("speech", "bond") and bool(re.search(r"\b[A-Z]{2,}\b", md))
    body = caps(body, loud)
    if kind in SPAN_PROSODY:
        pr = dict(SPAN_PROSODY[kind])
        if how and HOW_SOFT.search(how): pr["volume"] = "-6dB"
        body = f"<prosody {attrs(pr)}>{body}</prosody>"
    elif kind == "speech" and how:
        if HOW_SOFT.search(how): body = f'<prosody volume="-5dB">{body}</prosody>'
        elif HOW_LOUD.search(how): body = f'<prosody volume="+3dB">{body}</prosody>'
    elif kind == "emphasis":
        body = f'<emphasis level="moderate">{body}</emphasis>'
    return body


def who_label(runs):
    seen = []
    for kind, spk, to, how, *_ in runs:
        if kind in ("speech", "bond", "thought", "remembered", "verse") and spk:
            lab = {"speech": spk, "bond": f"{spk} (bond, to {to})", "thought": f"{spk} (thought)",
                   "remembered": f"{spk} (remembered)", "verse": f"{spk} (verse)"}[kind]
            if how: lab += f", {how}"
            if not seen or seen[-1] != lab:
                seen.append(lab)
    return seen


def chapter(n, path, variant=None, voice=None):
    title, paras = segment(path)
    ann = load_ann(n)
    starts = {p[2]: p for p in PARTS}
    L = ['<?xml version="1.0" encoding="UTF-8"?>',
         '<speak version="1.1" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="en-GB">']
    if voice: L.append(f'<voice name="{voice}">')
    L.append(f"<!-- {TITLE}, Chapter {n}: {title}. Point of view: {ann['pov']}. -->")
    perf = {"chapter": n, "title": title, "pov": ann["pov"], "segments": []}
    seq = 0

    def seg(kind, text, speaker="", listener="", how="", mood="", pause=0, pid=""):
        nonlocal seq
        seq += 1
        d = {"seq": seq, "para": pid, "type": kind, "text": text}
        if speaker: d["speaker"] = speaker
        if listener: d["listener"] = listener
        if how: d["how"] = how
        if mood: d["mood"] = mood
        if pause: d["pause_after_ms"] = pause
        perf["segments"].append(d)

    if n in starts:
        pname, season, a, b = starts[n]
        label, sub = pname.split(": ", 1)
        L.append(f'<p><s>{esc(label)}.</s> <s>{esc(sub)}.</s></p><break time="{P_AFTER_PART}ms"/>')
        seg("title", f"{label}. {sub}.", pause=P_AFTER_PART)
    L.append(f'<p><s>Chapter {words(n).capitalize()}.</s></p><break time="{P_AFTER_NUM}ms"/>')
    seg("title", f"Chapter {words(n).capitalize()}.", pause=P_AFTER_NUM)
    L.append(f'<p><s>{esc(clean(title))}.</s></p><break time="{P_AFTER_TITLE}ms"/>')
    seg("title", f"{clean(title)}.", pause=P_AFTER_TITLE)

    for i, p in enumerate(paras):
        if p["scene_break_before"]:
            L.append(f'<break time="{P_SCENE}ms"/><!-- scene break -->')
            if perf["segments"]:
                perf["segments"][-1]["pause_after_ms"] = P_SCENE
        mood_v = ann.get("paragraphs", {}).get(p["id"], "")
        mood, _, note = mood_v.partition("|")
        mood, note = mood.strip(), note.strip()
        runs = para_runs(p, ann)
        who = who_label(runs)
        cue = [p["id"]]
        if mood: cue.append(mood + (f": {note}" if note else ""))
        if who: cue.append("; ".join(who))
        # each run's offset in the paragraph (runs are contiguous and in order)
        pos, out_runs = 0, []
        for kind, spk, to, how, md, inner in runs:
            off = p["text"].find(md, pos)
            pos = off + len(md)
            out_runs.append((kind, spk, to, how, md, inner, off))
        ssml = "".join(run_ssml(k, h, md, inner, off) for k, s, t, h, md, inner, off in out_runs)
        if variant == "google":
            ssml = inline_names(ssml)
        if mood in MOOD_PROSODY:
            ssml = f"<prosody {attrs(MOOD_PROSODY[mood])}>{ssml}</prosody>"
        pause = P_PARA + (P_HEAVY - P_PARA if mood in HEAVY_MOODS else 0)
        nxt_scene = i + 1 < len(paras) and paras[i + 1]["scene_break_before"]
        L.append(f"<!-- {' · '.join(cue)} -->" if len(cue) > 1 else f"<!-- {cue[0]} -->")
        L.append(f"<p>{ssml}</p>" + ("" if nxt_scene or i == len(paras) - 1 else f'<break time="{pause}ms"/>'))
        # performance segments: one per run, narration runs merged with neighbouring terms/emphasis
        merged = []
        for k, s, t, h, md, inner, off in out_runs:
            k2 = "narration" if k in ("term", "emphasis") else k
            txt = clean(md)
            if merged and merged[-1][0] == "narration" and k2 == "narration":
                merged[-1][5] += txt
            else:
                merged.append([k2, s, t, h, "", txt])
        for j, (k, s, t, h, _, txt) in enumerate(merged):
            if not txt.strip():
                continue
            seg(k, txt.strip(), s, t, h, mood if mood else "", pause if j == len(merged) - 1 else 0, p["id"])
    L.append(f'<break time="{P_AFTER_TITLE}ms"/>')
    if voice: L.append("</voice>")
    L.append("</speak>")
    return title, "\n".join(L) + "\n", perf


def front_back(voice=None):
    def wrap(body):
        v1, v2 = (f'<voice name="{voice}">', "</voice>") if voice else ("", "")
        return ('<?xml version="1.0" encoding="UTF-8"?>\n'
                '<speak version="1.1" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="en-GB">' + v1 + "\n" + body + "\n" + v2 + "</speak>\n")
    opening = wrap(
        f'<p><s>{TITLE}.</s></p><break time="900ms"/>\n'
        f'<p><s>{SERIES}, Book One.</s></p><break time="900ms"/>\n'
        f'<p><s>Written by {AUTHOR}.</s></p><break time="700ms"/>\n'
        f'<p><s>Narrated by a digital voice.</s></p><break time="2000ms"/>')
    closing = wrap(
        f'<p><s>The End.</s></p><break time="2000ms"/>\n'
        f'<p><s>You have been listening to {TITLE}, {SERIES}, Book One, written by {AUTHOR}, and narrated by a digital voice.</s></p><break time="900ms"/>\n'
        f'<p><s>Copyright 2026 by {AUTHOR}.</s> <s>Production copyright 2026 by {AUTHOR}.</s></p><break time="1200ms"/>\n'
        f'<p><s>The story continues in {NEXT}, {SERIES}, Book Two.</s></p><break time="1500ms"/>')
    return opening, closing


# ---------------- names outputs ----------------
def write_names():
    rows = ["# Pronunciation guide: The Watch Below", "",
            "Every invented name in Book 1 that a synthetic voice may get wrong, with a respelling (stress in capitals), British IPA, and a plain alias spelling for engines that take aliases. "
            "**The author's word is final.** Names marked *confirm* could reasonably be said more than one way; the form given is the working choice until the author settles it. "
            "To change one, edit `Tools/audiobook/names.py` and rebuild; the lexicons are regenerated from it.", "",
            "| Name | Say it | IPA | Alias | |", "|---|---|---|---|---|"]
    for n, say, ipa, alias, st in sorted(NAMES, key=lambda x: x[0]):
        rows.append(f"| **{n}** | {say} | /{ipa}/ | {alias or ''} | {'*confirm*' if st == 'confirm' else ''} |")
    rows += ["", "## Notes", "",
             "- **Kharrak**: the *kh* is a plain hard *k*; the spelling marks the Clan's harder sound, not a throat sound.",
             "- **Staithe** rhymes with *bathe* (voiced *th*), as in northern English *staithe*, a landing stage.",
             "- **Holm** (Ragnald and Sigrun Holm) is said *home*, as the English word *holm* is.",
             "- **Hollin Knowe**: *knowe* is a knoll; said *now*.",
             "- **Oneroad** is *one road* run together.",
             "- Names that read as plain English (Pell, Hale, Rowan, Rook, Grieve, Turnip, Bramble, Sorrel, Tobin, Wren, Tam, Ada, Joss, Hob, Wat) need no entry.",
             "- Load `Lexicon_IPA.pls` (Amazon Polly, Azure) or `Lexicon_Alias.pls` (ElevenLabs pronunciation dictionaries and any engine that accepts PLS aliases). For engines with no lexicon support, build the `google` variant, which writes the aliases into the SSML."]
    open(os.path.join(AB, "Pronunciation_Guide.md"), "w", encoding="utf-8").write("\n".join(rows) + "\n")
    head = ('<?xml version="1.0" encoding="UTF-8"?>\n<lexicon version="1.0" xmlns="http://www.w3.org/2005/01/pronunciation-lexicon" '
            'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.w3.org/2005/01/pronunciation-lexicon '
            'http://www.w3.org/TR/2007/CR-pronunciation-lexicon-20071212/pls.xsd" alphabet="{alpha}" xml:lang="en-GB">\n')
    ipa = [head.format(alpha="ipa")]
    al = [head.format(alpha="ipa")]
    for n, say, p, alias, st in sorted(NAMES, key=lambda x: x[0]):
        ipa.append(f"  <lexeme><grapheme>{n}</grapheme><phoneme>{p}</phoneme></lexeme>\n")
        if alias:
            al.append(f"  <lexeme><grapheme>{n}</grapheme><alias>{alias}</alias></lexeme>\n")
    ipa.append("</lexicon>\n"); al.append("</lexicon>\n")
    open(os.path.join(AB, "Lexicon_IPA.pls"), "w", encoding="utf-8").write("".join(ipa))
    open(os.path.join(AB, "Lexicon_Alias.pls"), "w", encoding="utf-8").write("".join(al))


# ---------------- cast, ElevenLabs ----------------
def write_cast_and_elevenlabs():
    from cast import all_roles, role_of
    # line counts per role, from the annotations
    counts = {}
    for f in sorted(os.listdir(ANN)):
        for v in json.load(open(os.path.join(ANN, f), encoding="utf-8"))["spans"].values():
            t, spk, to, how = parse_span(v)
            if spk and t in ("speech", "bond", "thought", "remembered", "verse"):
                r = role_of(spk)
                counts[r] = counts.get(r, 0) + 1
    rows = ["# Cast: The Watch Below", "",
            "Voices for a multi-voice production. A single-narrator production uses only **Narrator**, who then carries every line; "
            "the notes still tell the narrator how each character sounds. Lines are counted from the annotations "
            "(speech, bond speech, thoughts, remembered words, verse). Speakers without a role of their own share the Man, Woman and Child voices; "
            "crowds and choruses go to the Narrator. The mapping lives in `Tools/audiobook/cast.py`.", "",
            "**Bond speech** (italics in the book: beast and bonded human, mind to mind) is the book's signature sound. "
            "Keep each beast's voice distinct and keep bond speech a touch closer and quieter than spoken dialogue, so a listener always knows when words are passing through the bond.", "",
            "| Role | Gender | Age | Lines | Voice |", "|---|---|---|---|---|"]
    for r, g, a, note in all_roles():
        rows.append(f"| **{r}** | {g} | {a} | {counts.get(r, '')} | {note} |")
    open(os.path.join(AB, "Cast.md"), "w", encoding="utf-8").write("\n".join(rows) + "\n")
    el = os.path.join(AB, "ElevenLabs")
    os.makedirs(el, exist_ok=True)
    vj = os.path.join(el, "voices.json")
    old = json.load(open(vj, encoding="utf-8")) if os.path.exists(vj) else {}
    roles = old.get("roles", {})
    new = {"_help": "Paste an ElevenLabs voice_id for each role you want voiced (Voice Library or your own voices). "
                    "Roles left empty fall back to Narrator. Per-role 'settings' override 'defaults'. eleven_v3 accepts stability 0.0, 0.5 or 1.0 only.",
           "output_format": old.get("output_format", "mp3_44100_128"),
           "defaults": old.get("defaults", {"stability": 0.5, "similarity_boost": 0.75, "style": 0.0, "use_speaker_boost": True, "speed": 1.0}),
           "roles": {}}
    for r, g, a, note in all_roles():
        new["roles"][r] = roles.get(r, {"voice_id": "", "note": note[:120]})
    json.dump(new, open(vj, "w", encoding="utf-8"), ensure_ascii=False, indent=1)


def studio_text(n, perf, name):
    """Plain chapter text for pasting or importing into ElevenLabs Studio (one narrator; voices can be assigned there)."""
    d = os.path.join(AB, "ElevenLabs", "Studio")
    os.makedirs(d, exist_ok=True)
    out, last_para = [], None
    for s in perf["segments"]:
        if s["type"] == "title":
            out.append(s["text"] + "\n\n")
            continue
        if s["para"] != last_para and last_para is not None:
            out.append("\n\n\n" if s.get("_scene") else "\n\n")
        elif last_para == s["para"]:
            out.append(" ")
        out.append(s["text"])
        last_para = s["para"]
    open(os.path.join(d, name + ".txt"), "w", encoding="utf-8").write("".join(out).replace("\n\n \n", "\n\n").strip() + "\n")


# ---------------- check ----------------
def spoken_tokens(ssml):
    s = re.sub(r"<!--.*?-->", "", ssml, flags=re.S)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    return norm(s)


def norm(t):
    t = t.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"').replace("\u2026", "...")
    t = re.sub(r"[*_]", "", t)
    return [w.lower() for w in re.findall(r"[\w']+", t)]


def verify(n, path, ssml):
    title, paras = segment(path)
    want = norm(" ".join(p["text"] for p in paras))
    got = spoken_tokens(ssml)
    # drop the headings
    head = norm(f"Chapter {words(n)} {title}")
    pre = []
    for p in PARTS:
        if p[2] == n: pre = norm(p[0].replace(":", "."))
    got_body = got[len(pre) + len(head):]
    return got_body == want


def main():
    args = sys.argv[1:]
    variant = args[args.index("--variant") + 1] if "--variant" in args else None
    voice = args[args.index("--voice") + 1] if "--voice" in args else None
    if variant == "azure" and not voice:
        sys.exit("--variant azure needs --voice NAME")
    out = os.path.join(AB, "Scripts") if not variant else os.path.join(AB, "Variants", variant)
    os.makedirs(out, exist_ok=True)
    if not variant:
        os.makedirs(os.path.join(AB, "Performance"), exist_ok=True)
        write_names()
    for f in os.listdir(out):
        if f.endswith(".ssml"): os.remove(os.path.join(out, f))
    opening, closing = front_back(voice)
    open(os.path.join(out, "00_Opening.ssml"), "w", encoding="utf-8").write(opening)
    open(os.path.join(out, "99_Closing.ssml"), "w", encoding="utf-8").write(closing)
    if not variant:
        write_cast_and_elevenlabs()
        for num, name, ssml in ((0, "Opening", opening), (99, "Closing", closing)):
            segs = []
            for m in re.finditer(r"<p>(.*?)</p>(?:<break time=\"(\d+)ms\"/>)?", ssml):
                txt = re.sub(r"<[^>]+>", "", m.group(1)).strip()
                segs.append({"seq": len(segs) + 1, "para": "", "type": "title", "text": txt, "pause_after_ms": int(m.group(2) or 0)})
            json.dump({"chapter": num, "title": name, "pov": "", "segments": segs},
                      open(os.path.join(AB, "Performance", f"{num:02d}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    bad, total = [], 0
    for n, path in chapter_files().items():
        title, ssml, perf = chapter(n, path, variant, voice)
        minidom.parseString(ssml.encode("utf-8"))
        if "--check" in args and not verify(n, path, ssml if variant != "google" else re.sub(r'<sub alias="[^"]*">([^<]*)</sub>', r"\1", ssml)):
            bad.append(n)
        open(os.path.join(out, slug(n, title) + ".ssml"), "w", encoding="utf-8").write(ssml)
        if not variant:
            json.dump(perf, open(os.path.join(AB, "Performance", f"{n:02d}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            studio_text(n, perf, slug(n, title))
        total += 1
    print(f"built {total} chapters into {os.path.relpath(out, REPO)}" + (f"; text mismatch in {bad}" if bad else ("; text verified" if "--check" in args else "")))


if __name__ == "__main__":
    main()
