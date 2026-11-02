"""Predict where narration is likely to go wrong, before rendering: reads a book's reading scripts the way the
renderer will (respellings applied, long paragraphs cut into pieces) and lists the pieces most likely to need
retakes or to end up doubtful.

What tends to fail (seen in rendering):
- very short lines: two or three words said alone ("Tell Pell.", "Part One.") give the voice too little to go on;
- rare words: words that occur once or twice in the whole series (Unchosen, mantrap), which a voice may misread;
- coined compounds: hyphenated words made for the book (hearth-lost, bond-place);
- respelled names next to each other or to a possessive ("Mairen and Orveth's");
- capitals, digits and symbols, which a voice may spell out or skip;
- a single sentence too long to cut, which a voice may rush or garble.

Use:  scan.py --book DIR
Writes <book>/audiobook/out/risk_scan.txt and prints a summary.
"""
import collections, glob, json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import config as cfg      # noqa: E402
import prepare as P       # noqa: E402
import render as R        # noqa: E402

COMMON = set("""a an the and or but if of to in on at by for with from up down out off over under as is was were be been
being am are it its it's i you he she we they me him her us them my your his our their this that these those there here
not no yes so then than too very just only all any some each every one two three four five six seven eight nine ten""".split())


def pieces(script, subs):
    """The pieces the renderer reads, in order: (text, kind, para)."""
    groups = []
    for s in script["segments"]:
        if groups and s.get("para") and groups[-1][-1].get("para") == s["para"]:
            groups[-1].append(s)
        else:
            groups.append([s])
    out = []
    for g in groups:
        text = R.text_of(g, subs)
        if not text:
            continue
        kinds = {R.kind(x) for x in g}
        style = kinds.pop() if len(kinds) == 1 else "narration"
        for piece in (R.title_pieces(text) if style == "title" else R.chunks(text)):
            out.append((piece, style, g[0].get("para", "")))
    return out


# measured on Book 1 chapter 1 (142 pieces): how often a piece needed a retake, and how often it stayed doubtful
RATES = {"1-3 words": (0.42, 0.17), "4-8 words": (0.07, 0.0), "9+ words": (0.02, 0.0)}


def bucket(words):
    return "1-3 words" if words <= 3 else ("4-8 words" if words <= 8 else "9+ words")


def main():
    P.main(quiet=True)
    subs = R.aliases()
    respelt = sorted({a for g, a in R.name_pairs() if a}, key=len, reverse=True)
    pair_rx = re.compile(r"\b(" + "|".join(map(re.escape, respelt)) + r")\b[’']?s?\s+(and\s+)?\b(" + "|".join(map(re.escape, respelt)) + r")\b") if respelt else None
    count, retry, doubt = collections.Counter(), collections.Counter(), collections.Counter()
    per_ch, listen = collections.defaultdict(lambda: [0, 0.0, 0.0]), []
    shorts = []
    for n in cfg.chapter_numbers():
        script = json.load(open(cfg.script_path(n), encoding="utf-8"))
        for text, style, para in pieces(script, subs):
            w = len(re.findall(r"[A-Za-z’'-]+", text))
            b = bucket(w)
            r, d = RATES[b]
            count[b] += 1; retry[b] += r; doubt[b] += d
            per_ch[n][0] += 1; per_ch[n][1] += r; per_ch[n][2] += d
            if b == "1-3 words":
                shorts.append(f"{n:02d} {para or 'title':5s} {text}")
            why = []
            if re.search(r"\b[A-Z]{2,}\b|\d|[&%/#@]", text):
                why.append("capitals, digits or symbols")
            if len(text) > 230 and not re.search(r"[.!?…]\s", text[:-1]):
                why.append("one long sentence (may be rushed)")
            if pair_rx and pair_rx.search(text):
                why.append("two respelled names together")
            if why:
                listen.append(f"{n:02d} {para or 'title':5s} [{'; '.join(why)}]  {text[:110]}")
    total = sum(count.values())
    exp_retry, exp_doubt = sum(retry.values()), sum(doubt.values())
    fail_ch = sum(1 for v in per_ch.values() if v[2] >= 1)
    os.makedirs(cfg.OUT, exist_ok=True)
    path = os.path.join(cfg.OUT, "risk_scan.txt")
    lines = [f"Risk scan of {cfg.TITLE}: {total} pieces in {len(per_ch)} scripts.",
             f"Expected: about {exp_retry:.0f} retakes, and about {exp_doubt:.0f} lines still doubtful after three tries,",
             f"which would mark about {fail_ch} chapters FAIL (any doubtful line fails a chapter).",
             "(Rates measured on Book 1 chapter 1; nearly all the doubtful lines are very short ones.)", "",
             "By length:"] + [f"  {b}: {count[b]} pieces, expect about {retry[b]:.0f} retakes and {doubt[b]:.0f} doubtful"
                              for b in RATES] + ["", "Chapters most likely to have doubtful lines:"] + \
            [f"  chapter {n}: {v[0]} pieces, about {v[2]:.1f} doubtful" for n, v in
             sorted(per_ch.items(), key=lambda kv: -kv[1][2])[:15]] + \
            ["", "Worth a listen once built (not counted above):"] + (listen or ["  (none)"]) + \
            ["", "Every very short line (chapter, paragraph, text):"] + shorts
    open(path, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print("\n".join(lines[:4 + 1 + len(RATES) + 1]))
    print(f"  full list: {os.path.relpath(path, cfg.BOOK)}")


if __name__ == "__main__":
    main()
