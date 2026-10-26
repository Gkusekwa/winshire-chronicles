# A3 — Bible and plans consistency audit

Scope: `Bible/{World,Story,Characters,Bestiary,Atlas,Magic,Series_Outline}.md`, `Book 1/Chapter_Plan.md`, `Book 1/Notes/*.md`, `Book 2/Outline.md`, `README.md`, `Style_Guide.md`, `Publishing.md`. Book 1 prose (`Book 1/Chapters/`, 79 files) was grepped to settle disputes. Nothing under `/home/claude/work` was edited.

Line numbers are the file's own line numbers as of this audit. Files whose fixes must be made at their generator: **`Book 1/Chapter_Plan.md` is generated from `Tools/plan/plan_data.py`**, and **`Bible/Atlas.md` is generated from `Tools/atlas/world.py` and `marches_items.py`** (Atlas.md line 3; `Tools/atlas/README.md`). Edit the data files and rebuild, or the fixes will be overwritten.

Note: `Book 3/Outline.md` (19,000 words, provisional) appeared in the tree during this audit (timestamp 08:24). It wasn't in the brief. I skimmed it only for README and open-question purposes.

---

## 1. Health summary

**Overall: fair. Book 1 itself is in good shape, but the Bible hasn't caught up with the post-Book 1 decisions.**

- **What's clean.** Chapter titles in the plan match the 79 chapter files and Ruling 20 (only cosmetic: the plan has "Why Me?" and the filename has "Why Me"). There are no live uses of Gunna Marrow, Ilse Marrow, Tam Brask, Keeper Idony or Coldrun Vale-as-disaster; each survives only in a ruling or a struck-through question that records the change. Orrin/the Scald is consistent everywhere. Orrun's multiplication is consistent across Story, Bestiary, Magic and the Book 2 outline (glimpses in Book 1, then one duplicate at a time, then 3–4 by the end of Book 2, each as strong as Orrun). Idony Vael (a man, a tide-reader of the College of Tides at Vael, survives) is consistent wherever he appears. The Book 1 day-timeline (days 0–144) agrees across Story, World, Magic §10a, the Decisions logs and the prose. So do Aurveth's partner arithmetic (Ragnald 61 years ago, Sigrun 17 + 59 = 76) and Merrow's and Hale's ages.
- **What's broken.**
  1. `World.md` still opens its magic section with the pre-Deep "two distinct sources" model.
  2. `Magic.md` §10 rule 2 contradicts its own six-discipline list.
  3. The settled rule that Maren and Calder don't cast in Book 1 is contradicted by the drafted prose (Maren says the settling-word and the stanching-word in Ch 5 and Ch 19/21).
  4. `README.md` doesn't list `Magic.md`, `Book 2/` or `Book 3/`, and says nothing about the Deep or the third POV. It also describes art outputs that don't exist in this copy.
  5. `Series_Outline.md` still describes a two-POV series of 100–120k-word books, and calls Book 1 a year long.
  6. Several duplicated facts disagree. Greyharts are grey deer in one section of `Bestiary.md` and white war-mounts in another. Pell's wyvern is "wild" in four docs, but the prose says it was a tamed, bonded company wyvern. Distances in `Atlas.md` disagree with its own gazetteer and with the prose. The Book 2 outline calls the control relic "the seventh relic", while canon calls it "the sixth".
- **Counts.** 3 Critical, 22 Major and 27 Minor findings (Minor includes a few marked "check"). Section 4 lists about 60 open questions: about 20 are now answered and about 40 are still open.

---

## 2. Findings

Format: **ID — file:line (section)** · exact quote · conflicting source · fix.

### Critical

**C1 — `Bible/World.md`:13–18 ("Magic and bonds")**
Quote: "Magic has two distinct sources: 1. **Learned magic** is studied and practiced… 2. **Bond gifts** come from a magical beast…"
Conflicts with the settled author decision (the Deep is canon: all magic is borrowed from the Titans), `Magic.md`:5, 9–11, `Series_Outline.md`:232.
Fix: replace lines 15–18 with:
> *All magic in Winshire is borrowed from the Titans* (canon; see `Magic.md`). What people work is **the Deep**, the breath of the Titans sleeping under every kingdom, through six **disciplines**: charms, runes, drawing, shaping, tide-reading and binding. Two other powers are not disciplines: **bond gifts**, which come from a beast through the bond and can't be taught, and **old magic**, which only the elder Titans ever worked.

Also replace line 20's "The exact rules, limits, costs, and prevalence of learned magic and bond gifts remain open" with "Rules, limits and costs: see `Magic.md` (§2–§4, §10)."

**C2 — `Bible/Magic.md`:272 (§10, rule 2)**
Quote: "People work the Deep only through the disciplines: words, runes, drawing, shaping, or a bond."
Conflicts with `Magic.md`:39–41 and the settled decision: there are six disciplines (charms, runes, drawing, shaping, tide-reading, binding), and bond gifts and old magic aren't disciplines. Rule 2 drops tide-reading and binding and counts a bond as a discipline. It also contradicts §2's "A bonded person doesn't draw from the Deep" (line 57).
Fix:
> 2. People work the Deep only through the six disciplines: charms, runes, drawing, shaping, tide-reading (which only reads it) and binding (forbidden). Bond gifts come through a bond, not the Deep, and are not a discipline. Only the elder Titans worked old magic, with nothing in between.

**C3 — `Bible/Magic.md`:286–287 (§10a) vs Book 1 prose**
Quote: "Maren and Calder are not magic users." / "no casting in Book 1 (only bond gifts…)"
Conflicts with the prose, which is the final authority for Book 1 events:
- Ch 5:55, "Maren leaned down and said the settling-word in his ear, the one every child on the river learns for a horse".
- Ch 19 notes: "Maren's stanching-word does nothing on the bridge pier, with running water all round".
- Ch 21:50, "She said the stanching-word over it again, on dry ground this time, and the arm stopped seeping… or she wanted it to."

The settled decision says they don't cast in Book 1. Calder doesn't cast ("Calder only talks", Ch 4 notes).
Fix (author's choice):
- (a) Keep the prose and narrow the rule. In §10a: "Maren and Calder are not magic users. Like most people, Maren knows a household charm or two (the river settling-word, a stanching-word, Ch 5, 19, 21) and can't tell whether they work. Neither of them *casts* in any real sense in Book 1." Make the same change in `Series_Outline.md`:236, and retitle Book 2's table "first castings" (Book 2 outline line 246) as "first workings through the bond".
- (b) Cut those three uses in revision.

### Major

**M1 — `README.md`:5–19 ("What's here")**
Missing: `Bible/Magic.md`, `Book 2/Outline.md`, `Book 3/Outline.md`, `Book 1/Notes/Rulings_41-79.md` (as the rulings record) and `Chapters_before_magic/`. Line 16 says `Book 1/Art/` holds "chapter-opener art (79 pieces) and the maps: bare front-matter maps, the 79 chapter-end map pages, full maps, and the interactive atlas page". In this copy `Book 1/Art/` holds only `Chapter Openers/art2.py` and `winshire_art.py`; there is no `Maps/` folder. `Style_Guide.md`:169–172 and `Atlas.md`:3, 187 point at the same missing paths.
Fix: add these lines:
> - **[Bible/Magic.md](Bible/Magic.md):** the Deep, the six disciplines, the toll, rings, imbued objects, bindings, Kessmoor's engines, magic in battle, the researcher.
> - **[Book 2/Outline.md](Book%202/Outline.md):** the provisional Book 2 chapter outline (three POVs; not approved).
> - **[Book 3/Outline.md](Book%203/Outline.md):** the provisional Book 3 chapter outline (not approved).
> - **[Book 1/Notes/Rulings_41-79.md](Book%201/Notes/Rulings_41-79.md):** rulings from the Chapters 41–79 review.

Change line 16 to "…chapter-opener art and the map pages, generated by `Tools/` (rebuild if missing)". Either regenerate the outputs or say they live outside the repo. Decide whether `Chapters_before_magic/` stays (see section 5).

**M2 — `README.md`:23–31 ("Core canon")**
Line 27: "The story follows two protagonists on a shared timeline, in alternating chapters." Nothing in Core canon mentions the Deep, the disciplines, the third POV, the post-Book 1 travel rule, Book 3's POVs, Saltreach or the land beyond the sea. These are all settled (`Series_Outline.md`:228–239, `Magic.md` §1, §10a, §11).
Fix: append a paragraph:
> **Settled after Book 1:** all magic is borrowed from the Titans (the Deep; six disciplines, not counting bond gifts or old magic; see `Magic.md`). Book 1 has few magic users; Maren and Calder don't cast in Book 1, begin limited casting in Book 2, and are untrained but capable in Book 3. From Book 2 a third POV joins: **Idony Vael**, a man, a tide-reader of the College of Tides at Vael in Isvaren, who survives the series. After Book 1, Maren and Calder don't travel together; they meet only out of necessity, each with a separate task. Orrun multiplies: glimpses in Book 1, one duplicate at a time, three or four by the end of Book 2, each as strong as he is. Some Book 1 warriors and leaders get POV chapters in Book 3. Book 3 explores Saltreach, where they meet the people who take Maren and Calder to the land beyond the sea, where other Titans are found. Books 2 and 3 are provisional until the author settles their open questions.

**M3 — `README.md`:58, `Bible/Story.md`:93, `Bible/Series_Outline.md`:60–61 (the twins' fates)**
Quotes: README "while his brother leads the charge at another location"; Story "while his brother leads the charge at another location"; Series "while **the other twin leads the charge at another location**, the second lock" and "the farmer… fights at the other lock against the twin leading the charge there".
Conflicts with the prose and `Story.md`:236. Corvin is *at the Ruin's lock*, turning it, with Calder's hand on his wrist (Ch 74, 76, 77). The man who led the charge into Greyhold was **Cassian**: Callis opened the river gate and "Cassian came in off the river with three hundred" (Ch 75 notes, line 12).
Fix (all three): "…while his brother, Corvin, turns the other lock under the Old Ruin at the same moment."

**M4 — `README.md`:74; `Book 1/Chapter_Plan.md`:113 (Ch 51), 151 (Ch 75), 192 (answer 5)**
Quotes: "the dying Warden Hale gives her the cellar key"; "Hale takes Maren to the locked cellar door"; "Hale, dying, gives her the cellar key".
Conflicts with the prose (Ch 75:269: "The long black key. Iron, as long as a forearm"; the black door is at the end of the archive, Ch 35/51), `Story.md`:170, Ruling 14, `World.md`:234.
Fix: "the long black key to the black door at the end of Greyhold's archive". Make the Chapter_Plan edits in `Tools/plan/plan_data.py`.

**M5 — `Book 1/Chapter_Plan.md`:124 (Ch 55)**
Quote: "The river breaks up with a noise like cannon."
Conflicts with `World.md`:219 ("There are no cannon in this world"; "River people never say the ice breaks") and Ch 55's own notes, line 11. The same stale beat is in Ch 55's notes line 6 and `Decisions_Ch51-60.md`:81.
Fix: "The river goes out all at once, with a noise like a city wall coming down. The lion lets Maren close enough to touch…" Edit `Tools/plan/plan_data.py`, which contains the string.

**M6 — `Bible/Bestiary.md`:91, 101 vs 184 (greyharts)**
Quotes: line 91 "**Greyharts** *(Hearthmere)*: tall grey deer, royal game."; line 101 "tall grey deer of the Brackenwood with antlers like bare winter trees. Royal game. Poaching one is a hanging offence".
Conflicts with line 184 "White war-mounts, 9 ft. The crown breeds them", `World.md`:202, `Decisions_Ch21-30.md`:88, and the prose (Ch 27:31: "White, both of them… the crown's war-mounts… nine feet at the shoulder"; Ch 30; Ch 33 "a breeding pair of greyharts kept for the crown").
Fix: line 91: "**Greyharts** *(Hearthmere)*: white, elk-like, nine feet at the shoulder; bred by the crown as knights' war-mounts. Wild herds in the Brackenwood are royal game." Line 101: "**Greyharts:** the crown's white war-mounts, bred for the orders; wild ones in the Brackenwood are royal game, and poaching one is a hanging offence (the Gallows Oak remembers)."

**M7 — Pell's wyvern: `Bible/Bestiary.md`:160, 170; `Bible/Characters.md`:138; `Book 1/Chapter_Plan.md`:50 (Ch 9)**
Quotes: "a wild wyvern on the Saltreach road *(settled)*"; "Pell's fingers were taken by a wild wyvern on the Saltreach road."; "two fingers lost to a wild wyvern on the Saltreach road"; "the wild wyvern on the Saltreach road that took his fingers".
Conflicts with the prose, Ch 9:81–95. It was one of a Saltreach company's two tamed wyverns. It "got loose" onto "the coast road below Stillhaven" (a Hearthmere port), and "It was bonded" to a pirate girl of fifteen. `Bestiary.md`:34 and `Characters.md`:152 already follow the prose. Pell even says "A wild wyvern doesn't bond."
Fix: replace "a wild wyvern on the Saltreach road" with "a Saltreach company's tamed wyvern, the rare bonded one, loose on the coast road below Stillhaven" in all four places. Also correct the "Settled" entry at Bestiary:170.

**M8 — `Book 2/Outline.md`:98, 205, 206, 214, 223, 238, 367 ("the seventh relic")**
Quotes: "The seventh relic is beneath Hearthmere"; "Corvin's hand is on the seventh relic first"; "the seventh's place at 65".
Conflicts with canon, which counts the control relic as **the sixth**: `README.md`:31, 61 ("the sixth relic gives it control"), `Series_Outline.md`:10, 113–114, `World.md`:50–53. Seven relics existed originally, but six remain, and canon's "sixth" is the term in use. Line 186's "a seventh thing held over all six" is fine as an in-world image (six sleepers on the carving).
Fix: "the control relic" everywhere (or "the sixth relic"). Ch 65 (line 205): "six ends, and the control relic 'beyond the first chains'".

**M9 — `Bible/Atlas.md`:8 vs 96, 174 (Harrow's End to the Ruin)**
Quote (line 8): "**Harrow's End is 2 leagues** from the Ruin across the water."
Conflicts with lines 96 and 174 ("a league and a half across the water from the Old Ruin"), `Decisions_Ch11-20.md`:77, and the prose (Ch 22:415, "a league and a half off"; Ch 42, 44, 66). The map point (177.3, 103.0) is 1.77 leagues from the Ruin (175.6, 103.5), and line 8 rounds that up.
Fix: move `harrowsend` in `Tools/atlas/world.py` about 0.3 league toward the Ruin, or have line 8 read "about a league and a half". Then rebuild.

**M10 — `Bible/Atlas.md`:31 vs 84, 181 (Millbrook)**
Quote (table): "Greyhold | Millbrook | 6 | 8 | 1 day | half a day | 45 minutes".
Conflicts with lines 84 and 181 ("two leagues downstream of Greyhold"), the prose (Ch 31:26 "it was two leagues downstream"; Ch 45:87 "to Millbrook… two leagues"), and the map point (172.3, 112.6), which is 6.2 leagues from Greyhold (174.0, 106.6).
Fix: move `millbrook` in `world.py` to about (173.4, 108.6), roughly two leagues downstream, and rebuild. Check that the Kettle, the caged-beast and Little Weir items in `marches_items.py` move with it.

**M11 — `Bible/Atlas.md`:30 vs 97, 169 (Varrhold)**
Quotes: table "Harrow's End | Varrhold | 11 | 13.5 | … | 1.4 hours" and line 8 "Varrhold is 11 leagues"; gazetteer "ten leagues north-east of Harrow's End… under a quarter of an hour by dragon."
The figures disagree: 11 vs 10 leagues, and 1.4 hours vs a quarter of an hour by dragon (80 leagues a day can't do 11 leagues in 15 minutes). The prose route (Ch 14 notes) has the ford "two leagues below Varrhold, about eight up the Drover's Way", which totals about 10 by road.
Fix: in `world.py` set the gazetteer text to "eleven leagues north-east of Harrow's End… under an hour and a half by dragon", or change the dragon pace. Check the prose for any dragon flight times to Varrhold first.

**M12 — `Bible/Series_Outline.md`:22 ("Format")**
Quote: "each book alternates point-of-view chapters between the student and the farmer, converging once they meet. Aim for about 100,000–120,000 words per book."
Conflicts with the third POV from Book 2 (line 230; `Magic.md` §11), the extra Book 3 POVs (line 237), and Book 1's actual length (about 311,000 words of prose across 79 chapters; `Style_Guide.md`:141 estimates 280–400k). The Book 2 outline estimates 310–440k.
Fix:
> **Format:** Book 1 alternates strictly between the student and the farmer (79 chapters, about 311,000 words in first draft). From Book 2 a third POV, Idony Vael, slots between them, and in Book 3 some Book 1 warriors and leaders add POV chapters. No upper word limit; each book is one ebook volume.

**M13 — `Bible/Series_Outline.md`:38, 45; `Book 1/Chapter_Plan.md`:7, 139 (Book 1's span)**
Quotes: "79 chapters, six parts, one year"; "Part Six: The First War (spring into summer, 67–79)"; "79 chapters in six parts, across one year: late summer to the next summer's war"; "*Spring into summer.*"
Conflicts with the drafted timeline: day 0 is the harvest fair at the end of summer, and the Titan flies at sunrise on day 144 (`Story.md`:199, 230; `Magic.md` §10a; Ch 79 notes). The thaw is night 119, "early spring". Book 1 covers about five months.
Fix: "79 chapters in six parts, across about five months (days 0–144): late summer to spring." Part Six: "*Spring* (days 131–144)." Edit `Tools/plan/plan_data.py` for the Chapter_Plan lines.

**M14 — Calendar arithmetic across books (check)**
`Story.md`:199 puts midwinter (full moon) at day 88, 88 days after the end-of-summer fair. `Book 2/Outline.md` starts at Book 1's day 144 ("Late spring, days 0–25", line 109), puts midsummer at days 25–60 (line 128) and midwinter at about day 170 (Part Four, days 125–200, ch 51), and ends "a year after the flight" in "Early summer" (line 229). These spacings don't fit a 365-day year: midwinter to midsummer is about 80–115 days in Book 1→2, then midsummer to midwinter is about 130 days in Book 2. A spring flight should also come round to spring, not early summer, a year later. No Bible file defines the year.
Fix: add a short "Calendar" note to `World.md` (year length, season boundaries in days). Then either re-label Book 2's part seasons, or accept a compressed in-world year and say so.

**M15 — `Bible/Magic.md`:311 (§11, "Where he joins the others")**
Quote: "with Maren and Calder at Vael when they come to the archive-bird; then sometimes with them, sometimes on his own errands".
Conflicts with the settled decision that Maren and Calder don't travel together (`Series_Outline.md`:235). The Book 2 outline also has Idony meet Maren first at the Hollow Ring (ch 18), and has Calder reach Vael separately, chasing Corvin (ch 38).
Fix:
> **Where he joins the others** *(see the Book 2 outline)*: alone in Vael at first; he meets Maren at the Hollow Ring and travels with her on the Titan's road; he crosses Calder's separate road at Vael and again at the end.

**M16 — `Bible/Bestiary.md`:19 and `Bible/Magic.md`:205 (what a binding is)**
Quote: "a **binding**: coercion by old magic, chains and pain that imitates a bond from the outside."
Conflicts with `Magic.md`:64 ("**Old magic**… is not a discipline. It is what the elder Titans did themselves… People can't do it."), `Magic.md`:82 ("A **binding** is, at bottom, a greater shaping done on a beast's self"), and §2's list of binding as a (forbidden) discipline.
Fix: "coercion by the forbidden discipline of binding (honey-smoke, words, will and collar), chains and pain, imitating a bond from the outside."

**M17 — Binder gone vs binder dead: `Bible/World.md`:224 vs `Bible/Bestiary.md`:19, `Bible/Magic.md`:211**
World: "When a binder is gone, the beast doesn't wake: it goes slack and follows any hand… Whether it comes back is unknown (52)." Bestiary: "If the binder dies, the beast is simply free." Magic's reconciliation: if the binder is gone but alive, the beast goes slack; if the binder dies, it's free. In Ch 52 the handler *runs*, he doesn't die (`Decisions_Ch51-60.md`:35), and Ruling 6 says Old Grey "may slowly half-wake".
Fix, World:224: "When a binder *flees* (is gone but alive), the bound beast doesn't wake… (52; Ruling 6). If the binder dies, the beast is free (`Bestiary.md`; `Magic.md` §6)."

**M18 — `Bible/Characters.md`:177 vs Book 1 prose (Maren's years) — check**
Quote: "She joined the river watch at 17 and has been at Greyhold two years; she is a second-year."
The prose disagrees with this and with itself:
- Ch 1:31 and Ch 3:59: "four winters on the river watch".
- Ch 13:167: "the habit of four years".
- Ch 11:91: Rowan says "You haven't been for four years", which contradicts "two years at Greyhold".
- Ch 15:24: "On the river watch she'd heard horns… eight years ago".
- Ch 3:71: "since I was seventeen".

So joining at 17 plus four winters doesn't reach 27 with two years at Greyhold.
Fix: the author picks one arithmetic, and a prose pass follows. One option that keeps most of the prose: "Joined the river watch at 17 (Ch 3) and served on the boats out of Northwatch and Redwatch; her last four winters were on the patrol boats (Ch 1, 3); at Greyhold two years." Then change Ch 11:91 to "for two years", and check Ch 13:20 and 167.

**M19 — `Bible/Characters.md`:131, `Bible/Series_Outline.md`:25, `Bible/Magic.md`:159, `Book 2/Outline.md`:371 ("the Unbound")**
Characters says "*(Avoid 'the Unbound': it is Book 1's working title.)*", and Series lists Book 1's working title as "*The Unbound*". But Magic names the seventh ring "**The Unbound**", and the Book 2 outline (with Book 3's dependency 33) builds a reveal on that ring name.
Fix: the author picks one. Either rename the seventh ring (for example "**the Open Hand**" or "**the Unringed**") and update Book 2:371, or retire *The Unbound* as Book 1's title and delete Characters' parenthesis. Either way, check the chosen title against the rule that titles must not reveal twists.

**M20 — `Bible/Series_Outline.md`:26 (Book 2 working title)**
Quote: "Book 2: *The Hunt Beneath* or *The Six Who Sleep*".
Conflicts with the rule that titles must not reveal twists, and with `Book 2/Outline.md`:7 ("*The Six Who Sleep* would give the sleepers away before chapter 23 does"). The same option survives as Book 2 open question 27 (line 439).
Fix: "Book 2: *The Hunt Beneath* (*The Six Who Sleep* retired: it gives away the sleepers)." Drop it from Book 2's question 27.

**M21 — `Book 2/Outline.md`:305 vs `Bible/Magic.md`:174 and §10 rule 5 (Haverly's edge on dead ground)**
Quote: "Haverly's edge still works, because runes hold as long as their material (Magic §6)."
Conflicts with Magic §5, "Feeding: … In dead ground an imbued object weakens and finally fails"; rule 5, "dead ground breaks everything"; §8 wards "Fail in dead ground"; and Book 2's own ch 5 echo, "Maren… sharpening Haverly's sword, and its runes staying dark". The citation is also wrong: rule 6 is in §10, not §6.
Fix: "Haverly's edge is dark on Hearthmere's dead ground (5) and wakes on living ground (20, 37); runes hold as long as their material *and their feeding* (Magic §10, rule 6)."

**M22 — `Bible/Series_Outline.md`:78 (Book 2 "Two home kingdoms, two threads")**
Quote: "The student's chapters stay rooted in Hearthmere, the farmer's in Saltreach."
Superseded by the settled separate-tasks rule as worked out in `Book 2/Outline.md`:23–30: Maren takes the Titan's road through the Wyldmarch, Isvaren, Kessmoor and Sarovel; Calder's road runs through Saltreach, Vael and Hallowmere.
Fix: "From Book 2 the two protagonists have separate tasks and roads (see `Book 2/Outline.md`, provisional). Hearthmere and Saltreach stay the anchor kingdoms."

### Minor

**m1 — `Style_Guide.md`:88–91, 150–158 (POV and reveals)**: Book 1 only. Add a "Books 2–3" block:
> From Book 2: three POVs; S and F keep strict alternation with each other; R (Idony) chapters slot between, never two in a row (proposal, `Book 2/Outline.md`); Idony's chapters "think in measurements" (`Magic.md` §11). Magic on the page follows `Magic.md` §10 ("magic tips fights; steel and beasts win them"). Terms: the Deep, the toll, dead ground, the six disciplines (charms, runes, drawing, shaping, tide-reading, binding); a *binding* is never a *bond*. Kept-on-purpose near-names: Orrin/Orrun, Idony Vael/the Vales/the city of Vael.

**m2 — `Style_Guide.md`:141 (Length)**: "Book 1 is planned as **79 chapters in six parts**… roughly 280,000–400,000 words." Fix: "Book 1 is drafted: 79 chapters in six parts, about 311,000 words (first draft, about 3,900 a chapter)."

**m3 — `Publishing.md`:202 (step 1)**: "**Finish the draft** of Book 1." This is done (79 chapters, all "Status: first draft"). Fix: "1. ~~Finish the draft~~ (done: first draft, about 311,000 words)." Also note against line 185 that the print ceiling of 200,000–225,000 words means the simplified print text has to cut about 30% of the current draft.

**m4 — `Bible/World.md`:86 and 166 (Kessmoor)**: "A magical disaster within living memory may have led to the ban… The relationship… needs definition" / "the site of Kessmoor's possible disaster". This is answered: Orrin, the Scald, about 40 years ago (`Magic.md` §7, `Atlas.md`:117, 270). Fix: "**Settled:** the disaster was at **Orrin**, now the Scald (see `Magic.md` §7)." At line 166: "the Scald, where Orrin stood".

**m5 — `Bible/World.md`:105, 107, 116, 118 (seal proposals now answered)**:
- 105: "*(Working proposal: this happens in Book 1…)*" is answered by Ch 45 (the paper) and Ch 49 (Hale).
- 107: "Hearthmere's knightly orders **may** have begun as the catacombs' wardens" is answered by Hale in Ch 49 ("The orders began as its wardens", `Story.md`:202).
- 116: "The seal is weakening… may" is answered: the lamps fail from night 90 (`World.md`:220).
- 118: "The knights' oath **may** itself be part of the binding" is answered (Ch 49; `Magic.md` §5).

Fix: mark each "*(answered in Book 1: ch 45/49)*" and delete "may".

**m6 — `Bible/Magic.md`:263 (§9, history table)**: "The first archivist cuts the pages about the closing *(canon)*." In the prose this is only Hale's belief (Ch 49:174, "I've always thought it was him"), and the prose never says "for the crown". Fix: "*(Hale's belief, Ch 49)*". Book 2 open question 15 (line 427) wrongly says "Book 1's drafts say only that they were cut"; correct it to "Hale believes the first archivist cut them (Ch 49)".

**m7 — `Bible/Magic.md`:76 vs 135 (Hearthmere's drawers)**: "Hearthmere licensed a handful for siege-work and had none left that anyone knew of by Book 1" vs "the licensed (… a few siege drawers)". Fix line 135 to "(and, formerly, a few siege drawers)".

**m8 — `Bible/Magic.md`:238 (§8, battle-words)**: "Licensed in Hearthmere *(canon: Hearthmere knights 'subdue, don't kill')*". The cited canon doesn't support the claim. Fix: "*(canon: Pell's licensed horse-standing word, Ch 9; the gate knights' staunching-word, Ch 33)*".

**m9 — `Bible/Magic.md`:198 vs `Book 2/Outline.md`:299 (relics' look)**: "each different, each of its kingdom's oldest stone" vs "the sleep relics are hollow eggs of grey catacomb stone… each carved with its sleeper". Pick one. Suggested for Magic: "alike in form, hollow eggs of grey old-realm stone, each carved with its own sleeper (proposal, Book 2 outline)".

**m10 — `Bible/Story.md`:11**: "They may be underestimated where bonds bring status" is a leftover from the gender-neutral draft. Fix: "She may be underestimated…".

**m11 — `Bible/Story.md`:27, 33, 58 (stale "open" statements in established sections)**:
- 27: "The school's name and location… remain open… how the student first encounters it… remains to be developed." Answered: Greyhold (`Characters.md`:103); through Tam, Tobin and the island hunters (`Story.md`:138).
- 33: "Its name, origin, multiplication rules, gift… remain undecided." Answered (line 140).
- 58: "Exact appearances, histories, and gifts are open." Partly answered: sizes, eyes and mark colours (`Characters.md`:180; `Decisions_Ch11-20.md`:28).

Fix: replace each with a pointer to the answer.

**m12 — `Bible/Story.md`:48 (overhearing proposal)**: "*(Working proposal: he overhears it while hiding from Restoration hunters, or the Far-Seer leads him close enough to listen.)*" Answered at line 129 (under a beam in the Ruin's tower, night 141, Ch 68). Delete the proposal.

**m13 — `Bible/Series_Outline.md`:63; `Book 1/Chapter_Plan.md`:155 (Ch 79)**: "As it leaves, Hearthmere's magic begins to fail" / "Hearthmere's magic begins to fail." In the prose the magic has been failing since night 90 and goes out completely when the Titan flies (Ch 79; `World.md`:233; `Magic.md`:28). Fix: "…Hearthmere's magic, failing since midwinter, goes out for good."

**m14 — `Bible/Series_Outline.md`:176 vs 222; `Bible/Story.md`:144 (near-Titans)**: "How the protagonists become near-Titans and survive *(established)*" is followed by the open question "How exactly do the student and the farmer become near-Titans…?" Fix: mark line 176 "*(established in outline; details open)*" and reword line 222 to "What does immortality cost them?"

**m15 — `Bible/Series_Outline.md`:136 vs Book 2 and Book 3 outlines (the plotting kingdom; proposal drift)**: Series: "Sarovel is the strongest candidate." The Book 2 outline (line 357) keeps Tobin in Sarovel as "the likeliest home of the kingdom that plots". The Book 3 outline makes **Kessmoor** the traitor (its open question 3). Not a canon conflict, but the three docs point different ways. Fix: when the author answers Book 3's question 3, update Series:136 and Book 2's Tobin rationale.

**m16 — `Bible/Characters.md`:141 and `Book 1/Chapter_Plan.md`:198 (names "open/proposed")**: "**the Darrow girl** (name open)" is answered: **Ide Darrow** (`Characters.md`:220). The plan's "Supporting names still proposed: Tobin, Pell, Hob, Rook, Captain Idris Vey, the Darrow girl" is stale: Rook is established (README:72) and all of these are in the drafted book. Fix: Characters 141 becomes "**Ide Darrow**". Plan 198 becomes "All supporting names are as drafted in Book 1 (see `Characters.md`); only kingdom names other than Saltreach remain working names."

**m17 — `Bible/Characters.md`:82 (Aurveth's partners)**: "has outlived two earlier partners". Before Calder she had three partners (Ennis, Ragnald, Sigrun: lines 86, 179). The line means "before Sigrun". Fix: "has outlived three partners (Ennis, Ragnald, Sigrun)".

**m18 — Bonded-pair counts: `Bible/Characters.md`:199, `Bible/Bestiary.md`:183, 201, `Bible/Story.md`:222**: "About a dozen pairs" / "The Clan keeps hundreds; about a dozen are bonded" / "the eleven bonded pairs" (the prose, Ch 48:217, says "Eleven pairs"). With Sigrun, Dag and Imra, that's fourteen before the mill. Fix: "fourteen bonded pairs before the mill; eleven after (Ch 48)."

**m19 — `Bible/Bestiary.md`:123 (Sarovel secret)**: "*(proposal for Book 2)*… the royal line's 'unicorn bond' is a lie". The same file's line 19 says "*(settled)*… what Sarovel's royal line does to its unicorns, is a **binding**", and `Magic.md`:214 says "(canon)". Fix: "*(settled: the royal 'bonds' are bindings; revealed in Book 2)*".

**m20 — `Bible/Bestiary.md`:129 vs 204 (ironbacks) — check**: "**Ironbacks:** armoured, boar-like beasts of the Iron Fells" (north, between Kessmoor and Isvaren, `Atlas.md`:47). Line 204 (prose Ch 74:60, Aurveth): "I've seen them. In the south. A long time ago." Fix: add to line 129: "once also in the south (Aurveth's memory, Ch 74)". Or change Aurveth's line in revision.

**m21 — `Bible/Bestiary.md`:207 vs `World.md`:41 (Titan size)**: "the size of a hill" vs "mountain-sized **Titans**". The prose of Ch 79 also says "a mountain in the sky, then a hill". Leave it, but add to the Titans row: "(the Last Titan, as first seen, is hill-sized, still diminished by chains)". Or let the author decide.

**m22 — `Bible/Atlas.md`:175 vs 28 (Greyhold to the Ruin)**: "about three leagues upriver of Greyhold" vs "Greyhold | The Old Ruin | 3.5". Fix in `world.py` text: "about three and a half leagues upriver of Greyhold".

**m23 — `Bible/Atlas.md`:3 and ferry scale (check)**: "The maps and this file are generated from one data file, so they always agree." The hand-written blurbs disagree with the generated table (M9–M11, m22). Separately, in `world.py` the Ashdown Ferry landing (173.4, 109.0) and Tolly's Staithe (177.2, 108.6) are 3.8 leagues apart. That makes the guide-rope ferry about 11 miles long, while Ruling 18 says the ferry house is "at the stone jetty right under Greyhold's wall". Fix: soften line 3 to "The table is computed from the map; check gazetteer text against it". Check the river width at the ferry in `world.py`.

**m24 — `Bible/Atlas.md`:96–97 duplicated by 169, 174, 176, 181, 182**: Harrow's End, Varrhold, Greyhold, Millbrook and Cotter's Cross each have two identical gazetteer entries (one under the kingdom, one under the Marches). Not contradictory now, but they're doubled maintenance. Fix in `build.py`: emit each place once, with a cross-reference in the other list.

**m25 — `Book 2/Outline.md`:82–83 (major-turns table order)**: the row "Orrun makes two shadows at once for the first time | 48" sits between ch 25 and ch 26. Move it after ch 47.

**m26 — `Book 2/Outline.md`:286 and 139 (directions) — check**: "the Hollow Ring lies almost exactly north-east of the Old Ruin". On the map (Ruin 175.6, 103.5; Hollow Ring 262, 54) the bearing is about 30° north of east, closer to east-north-east. Ch 20 has "flies north-west" from the Ring to Vael (150, 36), which is mostly west (about 9° north of west). Either adjust the Atlas points or say "east-north-east" and "west".

**m27 — Name collisions (check)**:
- "Keeper" is used for Wyldmarch Keepers, `Magic.md`:158's Sixth ring "Keeper of the Script", Book 2 ch 32 "The Keeper", and the suggested name for the archive-bird (Book 2 line 437).
- "Warden" is used for Hearthmere's inner-circle rank (`Characters.md`:104) and for Isvaren's law-enforcers (`World.md`:78; Magic §2a).
- Two Brasks: Coll Brask, the sellsword (Ch 54), and "the sergeant of the tower, a heavy man called Brask" (Ch 33:229).
- "Marrow" is a Wendmouth trading house (Ch 34 notes; `Decisions_Ch31-40.md`:65), although Gunna was renamed away from Marrow for being too close to Morrow and Merrow (Ruling 19).

Fix: decide which collisions are deliberate. At minimum, rename the Ch 33 sergeant and don't call the bird "the Keeper".

---

## 3. Stale statements in notes (low cost to fix)

- `Book 1/Notes/Decisions_Ch21-30.md`:87: "**Ada's seventh verse:**" should be "**Ada's third verse:**" (`Story.md`:181, 210; Ch 46:99 "There's a third verse").
- `Book 1/Notes/Decisions_Ch11-20.md`:22: "Who fired it is still open." Answered: one of Delling's crossbowmen, paid by the Restoration (Ch 68; `Story.md`:153).
- `Book 1/Notes/Voice_Samples.md`:3: "Names like Greyhold and Lucan Haverly are still proposals." Now established.
- `Book 1/Chapters/Chapter 01` and `Chapter 02` notes: "POV: The student" / "POV: The farmer". Every other file says Maren or Calder. (Outside my scope to edit; flagged.)
- Ch 55 notes line 6, and `Decisions_Ch51-60.md`:81: "a noise like cannon" (see M5).
- `Book 2/Outline.md`:423, 424, 426: questions 11, 12 (the survival half) and 14 are settled. Move them out of "Open questions" into a "Settled" list.

---

## 4. Open questions: status

**A = answered** (where). **P = answered only by a proposal in a provisional outline.** **O = still open.**

### `Bible/World.md`:181–189 (Open world questions)
1. How common are beasts and bonds; are there Titans beyond the six and the elders? **A in part.** The Clan keeps hundreds of dragons, with 14 bonded pairs before the mill (Ch 48); the Long Barn holds 31 bonded beasts (Ch 27); other Titans exist in the land beyond the sea (`Series_Outline.md`:228, 239). How common bonds are kingdom by kingdom: **O**.
2. Limits and costs of learned magic and bond gifts. **A**: `Magic.md` §2–§4, §10 (proposals resting on the canon Deep).
3. Which landscapes and legendary places belong to each kingdom. **A**: `Atlas.md` (proposal).
4. How the Clan breeds and controls dragons, and how dragons experience it. **O** (Book 3 outline proposes opening the pens).
5. Where the elder Titans are; what faiths say. **P**: the land beyond the sea (`Series_Outline.md`:228); "the Lit Shore" in the Book 3 outline.
6. Is the seal weakening before Book 1's end? **A**: yes; the lamps fail from night 90 (Ch 46–47; `World.md`:220).
7. Where are the catacomb entrances, and who guards them? **A**: the black door at the end of Greyhold's archive, under the north tower (two keys: archivist and Watch-captain; Ruling 14); the stair under the Ruin's tower; the older stair Corvin knew; the lion's pit (Ch 49–53, 75–78; `World.md`:231).

Also in World: line 20 (rules of magic, A: `Magic.md`), 37 (Clan breeding, O), 86 (Kessmoor disaster, A: Orrin), 179 (layout of the Marches, A: `Atlas.md`).

### `Bible/Story.md`:124–144 (Open story questions)
- Names (126), effects of the threefold bond (128), where he overhears (129), Aurveth's survival (132, a hedged answer in Ch 70), the General (133), the twins' names and origin (134), the reveal (135), how they differ (136), the Restoration's plan (137), involvement (138), the meeting (139), the lion (140): all **A** in Book 1 as annotated.
- 127, why Calder can sustain three: **O** (Series proposal at line 176).
- 130, what the alliance costs the uncle and nephew: **P** (Book 2 outline ch 24).
- 131, the warriors: **A**.
- 141, how the lion's Titan-growth changes Maren: **O**.
- 142, the dragons' Titan-growth and Calder: **O**.
- 143, how Corvin dies: **P** (Book 3 outline question 5).
- 144, near-Titans and the cost: **O**.
- Lines 191–194 and 241–244 (Open after Book 1): all **A** (Imra's shooter, Ch 68; the seal-carrier, Callis; Aurveth's cut, Ch 70; Davin, Ch 69; day 0's season, answered by the author). Old Grey: begun in Ch 69, **P** for Book 2.

### `Bible/Series_Outline.md`:209–226 (Open series questions)
- How the Restoration expected to capture the Titan: **A** (Ch 68; `Story.md`:137). Whether a protagonist is partly responsible: **A in part** (Calder's hand on Corvin's wrist, `Story.md`:236).
- How the Clan comes to believe the farmer: **P** (Book 2 outline line 321).
- What sacrifice forms the lion's bond: **A** (Ch 73).
- What each relic looks like: **P** (Book 2 line 299; conflicts with `Magic.md`:198, see m9).
- When Hearthmere chained its Titan: **A in part** (about 300 years ago: Ch 49, 57; Ruling 3). Full history **P** (Book 2 ch 34).
- Which brother the student kills: **A** (Cassian).
- How the surviving twin dies, and redemption: **P** (Book 3 question 5).
- Who the elder Titans are: **P** (Book 3 question 9).
- Cost of becoming Titans: **O**.
- Which kingdom plots: **P**, with conflicting proposals (m15).
- Which Titans survive Book 3: **O** (Book 3 question 14).
- How they become near-Titans and the cost: **O** (see m14).
- The destroyers' end: **P/O** (Book 3 question 14).
- What elementals are: **O**.
- Whether the Age of Elementals gets its own books or games: **O**.
- Does the student change as the lion grows: **O**.
- Line 228, beyond the sea (which sea, what it's called, whether people live there): **P** (Book 3 question 8).

### `Bible/Bestiary.md`:172–174
- Do tuskers and olifants have a language or remember the old realm? **O**.
- Is the grey cat a duskcat? **O**.

### `Bible/Atlas.md`:277–281
- Kingdom and place names are working names: **O** (README:52, Style_Guide:151).
- Where the old realm's capital stood: **O** (Book 2 makes the Ruin's bridge the hub, "the middle of the world", but not a capital).
- Which temple the Titan reaches first: **P** (the Hollow Ring, Book 2 ch 8–20).

### `Bible/Magic.md`:315
- Does Idony stay unbonded through Book 3? **P** (Book 3 question 20: he stays unbonded).

### `Bible/Characters.md`
- Line 3 says personalities, flaws and voices are proposals: **A in practice** by the drafts. No other open items beyond m16.

### `Book 1/Chapter_Plan.md`:184–201
- Answers 2 and 6 "remain working proposals". Both are now **A** in the drafts (Ch 3, 11; Ch 78).
- Line 172, the seal-rider "proposed payoff… (69 or 75)": **A** (Callis opens the river gate, night 143, Ch 75).
- "Open" (196–201): names **A** (m16); chapter length is by the scenes; the review pass is still to come (**O**, process).

### `Book 1/Notes/Rulings_41-79.md`:28
- Day 0's season: **A** (`Story.md`:244).
- Whether Rook's report (Arn threw Gunna out, Ulric listened) is Book 2 setup: **P** (Book 2 ch 10, 12).
- How much Aurveth hedges in Ch 70: **A** (drafted with "I think", `Story.md`:132).

### `Publishing.md`:184, 226–232
- What "simplified" means for the text: **O**.
- KDP Select or wide: **O**.
- What goes into print, and when: **O**.
- Editor and cover designer: **O**.
- Own name or pen name, and imprint: **O**.
- Release Book 1 alone or wait for Book 2: **O**.

### `Book 2/Outline.md`:411–439 (27 questions)
- 11, 14 and 12's survival half: **A** (settled).
- 15 can be answered from Ch 49 (m6).
- 27: drop *The Six Who Sleep* (M20).
- 1–10, 13, 16–26 and the rest of 12: **O**, awaiting the author. The whole outline stays provisional.

### `Book 3/Outline.md`:605–633 (27 questions)
- All **O** (not audited in depth). Question 17 in its dependency list says "Her first partner's face is cut from Book 2", but Book 1 Ch 70 already restored Ennis's face and name. Check that wording.

### Consolidated list of questions still open (O, or P only)

| # | Question | Lives in |
|---|---|---|
| 1 | Kingdom names other than Saltreach; all place names confirmed? | README:52, Style_Guide:151, World:71, Atlas:279 |
| 2 | How the Clan breeds and controls dragons; the dragons' experience | World:37, 186 |
| 3 | How common bonds are, kingdom by kingdom | World:183 |
| 4 | Where the elder Titans are; what faiths say (far shore proposed) | World:187; Series:218, 228; Book 3 Q8–9 |
| 5 | Why Calder could survive three bonds | Story:127; Series:176 |
| 6 | What the uncle–nephew alliance costs each | Story:130; Book 2 ch 24 (P) |
| 7 | How the lion's and dragons' Titan-growth changes Maren and Calder and their bonds | Story:141–142; Series:219, 226 |
| 8 | How Corvin dies; any redemption | Story:143; Series:217; Book 3 Q5 |
| 9 | How they become near-Titans; what immortality costs | Story:144; Series:222 |
| 10 | How the Clan comes to believe Calder | Series:212; Book 2:321 (P) |
| 11 | What each relic looks like | Series:214; Magic:198; Book 2:299 (P) |
| 12 | Full history of the chaining | Series:215; Book 2 ch 34 (P) |
| 13 | Who the elder Titans are, and why they help | Series:218; Book 3 Q9 |
| 14 | Which kingdom plots to be supreme | Series:220, 136; Book 2:357; Book 3 Q3 |
| 15 | Which Titans survive; what happens to the destroyers | Series:221, 223; Book 3 Q14 |
| 16 | What elementals are; do they get books or games | Series:224–225 |
| 17 | The land beyond the sea: which sea, name, people | Series:228; Book 3 Q8 |
| 18 | Tusker and olifant language and memory | Bestiary:173 |
| 19 | Is the grey cat a duskcat | Bestiary:174 |
| 20 | Where the old realm's capital stood | Atlas:280 |
| 21 | Which temple first (Hollow Ring proposed) | Atlas:281; Book 2 ch 8–20 |
| 22 | Does Idony stay unbonded through Book 3 | Magic:315; Book 3 Q20 |
| 23 | Old Grey's recovery | Story:243; Book 2 (P) |
| 24 | Simplified print text: what and when; Select or wide; editor and designer; name and imprint; release timing | Publishing:184, 228–232 |
| 25 | Book 2 outline questions 1–10, 12 (state at end), 13, 16–26 | Book 2:413–437 |
| 26 | Book 3 outline questions 1–27 | Book 3:607–633 |
| 27 | Calendar: year length and season boundaries (new; see M14) | none yet (add to World) |
| 28 | Maren's river-watch years (new; see M18) | Characters:177 vs prose |
| 29 | The seventh ring's name vs Book 1's title "The Unbound" (new; see M19) | Characters:131; Magic:159; Series:25 |

---

## 5. Stale, duplicate or unused files and sections to remove or merge

1. **`Chapters_before_magic/`** (79 files, 1.9 MB): a pre-magic snapshot of Book 1. 75 of the 79 files differ from `Book 1/Chapters/`. It's unlisted in README and is a trap for anyone grepping (it contains the same chapter titles and older text). Archive it outside the repo, or rename it `Archive/Book1_before_magic/` and list it in README as read-only.
2. **The "Added while drafting…" appendices** in `World.md` (193–234), `Story.md` (146–244), `Characters.md` (168–268) and `Bestiary.md` (176–207): merge each into the body section it amends, then delete the appendix. Do the conflicting ones first: World magic (C1); greyharts and Pell (M6, M7); binder (M17); Kessmoor (m4).
3. **`Book 1/Notes/Decisions_Ch11-20/21-30/31-40.md`**: their "To update" lists (11-20:53–71, 21-30:97–113, 31-40:102–117) have been carried into the Bible. Mark each file "Merged into the Bible; historical record". The 41–79 logs duplicate the chapter notes blocks verbatim ("Extracted from each chapter's notes block"), so they're double maintenance (for example, the cannon beat lives in both). Keep the notes blocks as the source and treat the logs as frozen.
4. **`Book 1/Notes/Voice_Samples.md`**: the choice is made (Style_Guide:93). Keep it as reference, but drop or mark samples A, B and C as superseded. They contain facts that now contradict canon (B: "held the river watch through four winters"; C: "four hundred years"; A: "The Holm girl's hawk").
5. **`Bible/Atlas.md` duplicate gazetteer entries** (m24): emit each place once.
6. **`Bible/Story.md` "The series" (100–110)**: duplicates `Series_Outline.md`:7–18 and README:31. Replace it with a two-line pointer.
7. **`Bible/Characters.md` "Alternatives" columns** (80–166): every name is now established by the drafts. Drop the alternatives columns, or move them to a "Names considered" appendix.
8. **`Book 1/Chapter_Plan.md` "Answers to the open questions" and "Open" (184–201)**: all answered except the review pass. Collapse them to a short "Settled" list (in `Tools/plan/plan_data.py`).
9. **`Bible/Series_Outline.md`** "Working titles" (24–28), "Format" (22) and the Book 2 "two threads" proposal (77–84): superseded (M12, M20, M22). Also, the "Settled by the author (after Book 1)" block (234–239) is the most current canon in the Bible and is buried at the end. Move it to the top, or to README Core canon (M2).
10. **`Book 2/Outline.md`** settled questions 11, 12 and 14 and their struck-through text: move them to a "Settled" note.
