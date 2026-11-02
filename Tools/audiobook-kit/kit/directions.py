"""Directions for the reading: what kind of words each quote or italic is, how a line is said, and each paragraph's
mood. A book can have them written by hand (`<book>/audiobook/annotations/chNN.json`); for anything not written by
hand, this module works them out from the text, and the kit writes them to the same files so they can be read and
corrected.

An annotations file:
    {"chapter": 7, "pov": "Maren", "auto": true,
     "spans": {"s1": "speech:Pell", "s2": "bond:Aurveth>Calder|very quietly", "s3": "thought:Maren", ...},
     "paragraphs": {"p4": "tension", "p9": "grief|after the burial", ...}}
- spans: one entry per quote (s ids in order of the quotes and italics in the chapter), as
  "type[:speaker[>listener]][|how]". Types: speech, bond (mind to mind), thought, remembered, written, verse,
  emphasis, term. The speaker is optional; "how" is a short note on delivery ("whispered", "shouted").
- paragraphs: a mood for the paragraphs that need one, optionally with a note after "|". Moods: action, tension,
  dread, quiet, reflective, tender, grief, humour, anger, urgent, awe.
- "auto": true marks a file the kit made. The kit remakes an auto file when its chapter changes; take the line out
  (or set it to false) once you've corrected a file by hand, and the kit will only fill in what's missing.

How the kit decides, when nobody has:
- Quotes are speech. A "how" note comes from the words around the quote: the verb (whispered, shouted, murmured,
  hissed, called) and any manner (quietly, softly, his voice cracking).
- Italics are emphasis when short and inside a sentence, a term when one word introduced as a name; thought,
  remembered or written words when the sentence says so (she thought; he had said; it read); verse when lines are
  broken; otherwise the book's default for italic speech (book.json "italics": "thought" or "bond").
- A paragraph's mood comes from its words: each mood has a vocabulary (grief: wept, grave, buried, mourned...), and
  a paragraph takes the strongest mood only when the signal is clear. Short, hard sentences tip toward action or
  tension; exclamations toward urgency. A mood carries over a short paragraph between two of the same mood.
  Most paragraphs stay plain narration, as in a well-read book.
"""
import re

GENERATOR = "directions 1"
MOODS = ("action", "tension", "dread", "quiet", "reflective", "tender", "grief", "humour", "anger", "urgent", "awe")

# ---------------- how a line is said ----------------
_VERB_HOW = [
    (r"whisper\w*", "whispered"), (r"breath(ed|ing)", "very quietly"), (r"murmur\w*", "quietly"),
    (r"mutter\w*", "low"), (r"hiss\w*", "low, urgent"), (r"shout\w*", "shouted"), (r"yell\w*", "shouted"),
    (r"bellow\w*", "shouted"), (r"scream\w*", "shouting"), (r"shriek\w*", "shouting"), (r"roar\w*", "roared"),
    (r"called( out)?", "called"), (r"cried( out)?", "shouting"), (r"sobb\w*", "voice cracking"),
    (r"snapp\w*", "sharp"), (r"growl\w*", "low"), (r"croak\w*", "weak"), (r"rasp\w*", "a rasp"),
]
_MANNER_HOW = [
    (r"very quietly|very softly|barely above a whisper|under (his|her|their) breath", "very quietly"),
    (r"quietly", "quietly"), (r"softly|gently", "softly"), (r"loudly|at the top of (his|her|their) voice", "loud"),
    (r"(his|her|their) voice (cracking|cracked|breaking|broke)", "voice cracking"),
    (r"(his|her|their) voice (shaking|shook|trembling|unsteady)", "shaking"),
    (r"faintly|weakly", "faint"), (r"hoarse(ly)?", "hoarse"), (r"urgently", "urgent"), (r"eagerly", "eager"),
]
_SAY = r"(?:said|says|asked|asks|answered|replied|told|went on|added|called|cried|whispered|shouted|murmured|muttered|hissed|breathed|snapped|roared|yelled|screamed|growled|croaked)"


def how_near(before, after):
    """A delivery note from the narration just before and just after a quote, or ''."""
    ctx = (before[-60:] + " | " + after[:80]).lower()
    notes = []
    for rx, note in _MANNER_HOW:
        if re.search(r"\b(" + rx + r")\b", ctx):
            notes.append(note); break
    for rx, note in _VERB_HOW:
        if re.search(r"\b(" + rx + r")\b", ctx) and note not in notes:
            notes.insert(0, note); break
    return ", ".join(notes)


# ---------------- what kind of italics ----------------
def italic_kind(text, s, para_text, inside_quote, default):
    inner = s["text"].strip()
    words = len(re.findall(r"[\w’']+", inner))
    before = para_text[max(0, s["start"] - 70):s["start"]].lower()
    after = para_text[s["end"]:s["end"] + 70].lower()
    if inside_quote:
        return "written" if words >= 7 else "emphasis"
    if "\n" in s.get("raw", "") or s.get("verse"):
        return "verse"
    if re.search(r"\b(read|reads|wrote|written|writes|said the (letter|note|paper|sign|stone|order|notice)|it said|the words|carved|inscri\w+|painted)\b[^.]{0,30}$", before):
        return "written"
    if re.search(r"\b(had said|had told|used to say|remembered|heard (him|her|them|it) say|had once said|always said)\b", before + " " + after[:30]):
        return "remembered"
    if re.search(r"^\W{0,3}(she|he|they|i|[A-Z]\w+)?\s*(thought|wondered|told (him|her)self|thinks)\b", after) or \
       re.search(r"\b(thought|wondered)[,:]?\s*$", before):
        return "thought"
    if words <= 2 and s["start"] > 0 and not re.search(_SAY, before[-20:] + after[:20]):
        # a word stressed in a sentence, or a word introduced as a name ("the shepherds call it *keeping the fence*")
        return "term" if re.search(r"\b(call(ed|s)?|known as|named|the word)\s*$", before) else "emphasis"
    if re.search(r"^\W{0,3}(\w+\s){0,3}" + _SAY + r"\b", after) or re.search(r"\b" + _SAY + r"[,:]?\s*$", before):
        return default if default in ("bond", "speech") else "speech"
    return "thought"


# ---------------- moods ----------------
_LEX = {      # strong cues only: a mood is given where the words leave little doubt
    "grief": "grief grieving grieved wept weeping sobbed sobbing mourn mourned mourning funeral keening buried burial "
             "grave graves cairn corpse died dead dying sorry crying tears",
    "dread": "terrible dread dreadful terror terrified horror horrible wrong wrongness nightmare eerie uneasy unease",
    "tension": "careful carefully waited breathe breathless tense tensed tight tightened crouched edged listening",
    "action": "scream screamed screaming hit threw thrown struck lunged charged slammed smashed hurled spear "
              "stabbed slashed parried dodged ducked fighting fought",
    "anger": "anger angry furious fury rage raged raging enraged hate hated hatred seethed seething snarled spat",
    "tender": "tenderly kissed kiss hugged embraced cradled stroked ribbon hello",
    "quiet": "hush hushed peaceful asleep slept dozing dozed murmured",
    "reflective": "remembered memory memories decided realised realized wondered years ago",
    "humour": "laughed laugh laughing laughter grinned grinning joke joked joking teased teasing chuckled snorted",
    "urgent": "hurry hurried quick quickly now run running shouting fast faster go",
    "awe": "enormous immense vast huge towering taller size breadth majestic rising flying hundreds",
}
_LEX = {m: set(w.lower() for w in s.split()) for m, s in _LEX.items()}
_BAR = {"grief": 2.2, "dread": 1.6, "tension": 2.4, "action": 2.4, "anger": 2.0, "tender": 1.8, "quiet": 2.4,
        "reflective": 2.4, "humour": 1.6, "urgent": 3.5, "awe": 2.2}
_MIN = {"urgent": 3}   # cues needed at least this many times


def mood_scores(text):
    words = re.findall(r"[a-z’'-]+", text.lower().replace("’", "'"))
    n = max(len(words), 1)
    sc = {m: 0.0 for m in _LEX}
    for w in words:
        for m, lex in _LEX.items():
            if w in lex:
                sc[m] += 1
    sents = [s for s in re.split(r"(?<=[.!?…])\s+", text) if s.strip()]
    if len(sents) >= 4:
        short = sum(1 for s in sents if len(s.split()) <= 5) / len(sents)
        if short > 0.7:
            sc["tension"] += 1.0
    if text.count("!") >= 2:
        sc["urgent"] += 1.0
    return {m: v * 100 / n for m, v in sc.items()}, n


def paragraph_moods(texts):
    """A mood (or '') for each paragraph's text, with a light carry-over between neighbours."""
    out = []
    for t in texts:
        sc, n = mood_scores(t)
        if n < 12:
            out.append(""); continue
        best = sorted(sc.items(), key=lambda kv: -kv[1])
        (m1, v1), (_, v2) = best[0], best[1]
        hits = v1 * n / 100
        out.append(m1 if v1 >= _BAR[m1] and hits >= _MIN.get(m1, 2) and v1 >= v2 * 1.5 else "")
    for i in range(1, len(out) - 1):          # a short plain paragraph between two of the same mood takes it too
        if not out[i] and out[i - 1] and out[i - 1] == out[i + 1] and len(texts[i].split()) < 40:
            out[i] = out[i - 1]
    return out


def auto(paras, spans_of_para, default_italics="thought"):
    """Directions worked out from the text. paras: [{"id", "text", "spans": [{"id","kind","start","end","text"}]}]."""
    spans, pmood = {}, {}
    for p in paras:
        text = p["text"]
        quotes = [s for s in p["spans"] if s["kind"] == "q"]
        for s in p["spans"]:
            if s["kind"] == "q":
                # only the narration between this quote and its neighbours says how it is said
                prev_end = max([q["end"] for q in quotes if q["end"] <= s["start"]] or [0])
                next_start = min([q["start"] for q in quotes if q["start"] >= s["end"]] or [len(text)])
                how = how_near(text[prev_end:s["start"]], text[s["end"]:next_start])
                spans[s["id"]] = "speech" + (f"|{how}" if how else "")
            else:
                inside = any(q["start"] <= s["start"] and s["end"] <= q["end"] for q in quotes)
                italics = [x for x in p["spans"] if x["kind"] == "i"]
                k = italic_kind(text, s, text, inside, default_italics)
                # three or more italic lines one after another, with nothing between: verse or a vow
                run = [x for x in italics if not text[x["end"]:x["end"] + 3].strip(" ,") or not text[max(0, x["start"] - 3):x["start"]].strip(" ,")]
                if len(italics) >= 3 and s in run and not text.replace("*", "").strip() == "" and \
                        all(not text[a["end"]:b["start"]].strip() for a, b in zip(italics, italics[1:])):
                    k = "verse"
                how = how_near(text[:s["start"]], text[s["end"]:]) if k in ("bond", "speech") else ""
                spans[s["id"]] = k + (f"|{how}" if how else "")
    for p, m in zip(paras, paragraph_moods([p["text"] for p in paras])):
        if m:
            pmood[p["id"]] = m
    return {"spans": spans, "paragraphs": pmood}
