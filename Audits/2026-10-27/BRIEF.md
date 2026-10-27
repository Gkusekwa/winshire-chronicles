# Winshire Chronicles: full audit brief (read this first)

You are one of several reviewers auditing a finished first draft of a fantasy trilogy, *Winshire Chronicles*, by Goodluck Kusekwa. Each reviewer reads one range of chapters closely. **Do not edit any file.** Your only output is one findings file (path given in your task).

The repo copy is at `/home/claude/audit/repo/`. All paths below are relative to it.

## What the books are

- Three books: Book 1 (79 chapters), Book 2 (88), Book 3 (86). Each book is one volume, never split.
- **Beast books, not dragon books.** The lion Orrun, Calder's three dragons (Kharrak, Lisska, Aurveth), hounds, greys, olifants, wyverns, the Titans and more.
- POVs. Book 1 alternates Maren (S) and Calder (F). Book 2 adds Idony (R). Book 3 adds Rowan (G), Arn (C), Tobin (U) and Kit Merrin (M). Each chapter's notes block names its POV.
- The voice is lean and mythic, and should not sound like AI.
- Every chapter file opens with `# Chapter N: Title`, then an HTML comment block of notes: POV, Part, Days, Ends at, Beats, Echo, Status, Draft notes and Magic touches. After that comes `---` and the prose.

## Canon sources

Check the text against these.

- `Bible/` holds the canon:
  - `Series_Outline.md`: the spine, the settled points, and an "Open questions" list. Almost everything there is now settled.
  - `World.md`, `Story.md`, `Characters.md`, `Bestiary.md`, `Magic.md` (the magic rules) and `Atlas.md` (geography and distances; one league is about three miles).
- The chapter plans: `Book 1/Chapter_Plan.md`, `Book 2/Chapter_Plan.md` and `Book 3/Chapter_Plan.md`.
  - The author approved all review questions in Books 2 and 3 as drafted.
  - Where a drafted chapter differs from its plan row, **the chapter is canon**. Report that kind of difference only if it causes a contradiction somewhere else.
- Running facts by part: `Book 2/Notes/Part*_Ledger.md` and `Book 3/Notes/Part*_Ledger.md`.
- Book 1 rulings and decisions: `Book 1/Notes/Rulings_41-79.md`, `Book 1/Notes/Decisions_*.md` and `Audits/2026-10/DECISIONS.md`. The earlier audit reports are also in `Audits/2026-10/`.
- `Style_Guide.md`.
- Day counts start fresh in each book:
  - Book 1: day 0 is the start.
  - Book 2: day 0 is the sunrise of Book 1 ch 79.
  - Book 3: day 0 is dusk on the day the six went up, which is Book 2's day 362. Book 3's days 0–3 overlap Book 2 ch 88's days 362–365.

## Settled rules: flag any breach

1. **Maren and Calder meet only out of necessity** after Book 1. They don't share a road.
2. **Reveal rules.** Check each of these:
   - The Council of Immortals is never named.
   - Nothing suggests that Titans survive the end of Book 3, except Kit's one ambiguous sighting in Book 3 ch 76.
   - Elementals are never named or explained in the prose. The only appearance is the unexplained stone creature in Book 3 ch 86. Idony's "nothing new in the ground; nothing small" in ch 52 is the limit.
   - The control relic is never called "the seventh relic".
   - The prose never mentions "Book 1", "Book 2" or "Book 3".
3. **Magic.**
   - Castings need live ground and touch range.
   - Running water breaks spoken charms.
   - Bond gifts are the only power on dead ground.
   - Every working has a toll (see `Magic.md`).
   - Maren and Calder don't cast in Book 1. In Book 2 their casting is limited. In Book 3 they are untaught but strong.
   - Idony is burned out from Book 2 ch 83 onward: he can read and measure but can't work, and his hands shake.
4. **Titles must not reveal twists.** This covers chapter titles and anything else that acts as a title.
5. **Settled facts that are easy to get wrong:**
   - Book 3's remnant is 555 (473 at dusk in ch 80, 533 by ch 81, 553 with Arn's twenty riders in ch 83, 555 with Maren and Calder in ch 86).
   - Twenty dragons go into the hall, Ildra among them. Thirty grown Clan pairs fly the overflow to Varrhold and are buried by the slip (chs 83, 85).
   - Of the destroyers, the alliance kills the Antlered (B3 ch 50) and the Furnace (65). The Horned Sun, the Pale Coil and the Bell burn out (82). The Last Titan dies last, under the mountain (83). The Lady is an elder, not a destroyer.
   - The old realm's capital stood at "the middle of the world", the island and the hub. It is never named or called a capital in the prose.
   - The Drowned Bell's reef is two leagues off Gullhaven.
   - The kingdom names and "the Restoration" are final.
   - Book 3 ch 86's last line, "She didn't count them.", was written by the author. Don't touch it.
6. **Style rules.** These are checked mechanically elsewhere, so mention them only if you happen to see them:
   - no em dashes;
   - no "the way" similes (use "as");
   - avoid the "It wasn't X. It was Y." pattern;
   - no meta talk.

## How to review your range

1. Read the plan rows and the ledger lines for your range first. Then read **every chapter in your range in full**, notes and prose. Also read the last part of the chapter before your range and the start of the chapter after it, to check the hand-offs.
2. Look for:
   - **Continuity inside your range and against earlier material:**
     - day numbers and time of day;
     - travel times against Atlas distances;
     - who is where, who is alive, and who knows what when;
     - injuries and their persistence (for example, Maren's numb or dead left hand in Book 3);
     - beasts' sizes and abilities;
     - counts, names and spellings, ranks and ages;
     - objects, and who carries what.
   - **Canon breaches** of the rules above, or of the Bible and rulings. Cite the canon file and line.
   - **Notes against prose:** the notes block says one thing and the prose does another.
   - **Plot logic:** motivation gaps, convenient coincidences, a setup with no payoff, or a payoff with no setup (as far as you can see), and people knowing things they couldn't know.
   - **Craft** (keep these few and high-value, **at most 8**): voice drift into generic or AI-sounding prose, repeated tics across chapters, scenes summarised that need dramatising, flat chapter endings, pacing sag, POV slips.
3. **Verify before writing.** Re-open every cited line. If you aren't certain, label it "Check" rather than asserting it. Quote exactly, and keep quotes short.
4. Don't report:
   - differences from the plan where the chapter is the canon, unless they cause a contradiction;
   - matters of taste;
   - things the notes say were deliberately decided, unless they contradict something else.

## Output format

Write a markdown file with these sections:

```
# Findings: Book N, chapters A–B
Reviewer summary: 2–4 sentences.
## Critical   (breaks the story, canon or a settled rule)
## Major      (a continuity or logic error a careful reader would notice)
## Minor      (small slips: a wrong day, a name typo, a count off by one)
## Craft      (at most 8)
```

Write each finding like this:

```
### [B2-17-a] Short title
- Where: Book 2 ch 17, line 212 (and ch 19 line 40)
- Quote: "exact short quote"
- Problem: what is wrong, in one or two sentences.
- Evidence: file:line of the conflicting text or canon.
- Fix: the smallest change that resolves it (prose in the series voice if needed).
```

The ID format is `[B<book>-<chapter>-<letter>]`. Line numbers are from the chapter file (`grep -n` or `cat -n`). When you're done, your final reply should be short: the number of findings in each severity, and your top 3.
