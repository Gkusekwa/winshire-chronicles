# Continuity Sweep, October 2026

*All three books' chapters, checked against `World.md`, `Atlas.md`, `Tools/atlas/world.py` (plus the map item files), and the three Chapter Plans. Nothing has been edited. The fixes below are proposals only.*

## Applied (Oct 2026)

All the real errors are fixed, with the smallest change each:
- **Bonds:** Wynn's bonded hound is Sorrow (Book 1 ch 51); Callis isn't called bonded (ch 33); Calder hears Orrun only through Lisska (Book 3 ch 12).
- **Calendar:** the night of the mill is under the "old moon" (Book 2 ch 35); "starlight" at dusk on day 65 (Book 1 ch 39); "three days" with Ide (ch 59). Book 2 ch 37's field already reads 172–177.
- **Distances:** the hatching caves are six leagues from Varrhold by the moor path (Book 2 chs 12, 52; Book 3 ch 42 notes; World.md; two tales). At six leagues Aurveth's voice reaches Calder as "more feeling than word" (Book 2 ch 12), inside the range rule. Ferriby and Penfold moved on the map and every map rebuilt. **Hollin Knowe was a false alarm:** a later override in `marches_items.py` already puts it at (174.0, 102.6), two leagues west of the river.
- **Deaths and names:** Aurveth lay on Coldtarn's shore "a year" (Book 3 ch 85); Wynn is "his" (ch 85); Ash is "her" throughout (Book 3 ch 10).
- **Bible:** World.md now has Teo's single-night pyre, Ulric's burning at Skarrow, the riders burned at the mill, Gunna and Tamsin's Thornwood pour, one road allowance (about a quarter, as the Atlas table uses) and the Titan-class flying time.
- **Optional ones taken:** Arn's "one bolt… that started it" (Book 2 ch 24). The stale reef note in Book 3 ch 24 is replaced.
- **Housekeeping:** the 29 Plan `Days` rows are widened to match their chapters.

## Method and counts

- **Days.** Scripts pulled every dated reference: 1,504 of them ("day 65", "night 143", "the hundred-and-tenth day") from the notes and prose of all 253 chapters. Each Book 2 and Book 3 `Days:` field was compared with its Plan row and with its neighbours. Each prose day number was compared with its chapter's range. Every moon phase and season word was checked against the calendar. The scripts found most of the problems below; reading the passages decided whether each one was a real error.
- **Distances.** Scripts found 434 league references and 39 travel-time phrases, measured each named pair on the atlas coordinates, and flagged anything off by more than about 40%.
- **Deaths.** 37 named deaths were checked. A script found every later mention of each dead name (about 280), and each was read for whether the person is alive on the page or only remembered. Funeral scenes were compared with World.md.
- **Knowledge and bonds.** The major reveals were spot-checked by search. Every line of italic mind-speech (about 860) was tagged with its speaker and its chapter's POV character, to catch a human hearing a beast they aren't bonded to.

**Result:** 16 real errors (6 serious, 10 minor or data), 17 defensible points, and 29 housekeeping mismatches in the Plans. These came out clean: the moon cycle in Book 1, the relic-to-waking intervals, every "N days from now" check in the notes, the dead appearing alive later (none do), and leaks of the sampled reveals (none found).

---

## 1. Bond rules (most serious)

### 1.1 Wynn outlives his bonded hound Ash (real error, serious)
- Book 1 ch 33: "Two passed knights from the gate, Callis and Wynn, both bonded, both with hounds trotting at their stirrups."
- Book 1 ch 51: "Nothing like the thing Haverly had with Kesh, or **Wynn with Ash**, or her father with his hound."
- Book 3 ch 73, day 319: "Ash hadn't. 'I had to,' said Wynn." (He kills Ash, or lets Ash die, in the smoke.)
- Book 3 ch 85, day 325–328: Wynn is alive at the pour. He says "Her name was Ash," and the notes list "Wynn and Sorrow".

**Why it conflicts:** one life between two. In Book 1 the bonded die on the third day (Ide, ch 39; Morrow, ch 62). Wynn is alive six to nine days later, and none of the three ways in World.md applies to him. Ch 73 can stand on its own, because the bonded knights there are hours from their beasts' deaths. Ch 85 can't.
**Smallest fix:** make Sorrow his bonded hound. In Book 1 ch 51, change "Wynn with Ash" to **"Wynn with Sorrow"**. Ch 73 already reads that way: "Sorrow… Come back through the smoke to its knight."

### 1.2 Callis outlives his hound Grip (real error, serious)
- Book 1 ch 33: Callis is "bonded"; Grip is "Callis's own" (ch 63).
- Book 3 ch 33, night 137: "Grip died in the winter. In the snow. On the road. I've nobody." Callis lives on to ch 74.

**Smallest fix:** in Book 1 ch 33, change "Callis and Wynn, both bonded, both with hounds" to **"Callis and Wynn, both with hounds"**. Characters.md never calls Callis bonded, and Wynn's bond is set in ch 51.

### 1.3 Calder hears Orrun directly (real error)
- Book 3 ch 12, Calder POV: "*I told him about the chain,* she said… **\*I believed her,\* said Orrun.**"

**Why:** "Humans hear only their own bonded" (World.md, Rulings 5 and 13). Everywhere else, Orrun's words reach Calder, or Lisska's reach Maren, only through a stated relay ("through Orrun", "Through Lisska": Book 3 chs 49, 59, 63, 66).
**Smallest fix:** change it to **"*He says he believed me,* said Lisska."**

### 1.4 Bond: defensible
- Book 2 ch 83 (Idony POV): "*The door,* said Orrun. He heard that. Everyone did. She said it aloud." On a first reading Idony seems to hear Orrun. The sense is right. Optional: "She said it aloud, and he heard that. Everyone did."
- Book 3 chs 70–73: bonded knights stand on the gate with their hounds dead. This works because they die within the day or don't appear again. Keep it that way in any revision.
- Bindings: none of the binding scenes sampled lets a binder share a bound beast's death or mind-speech. Bond-speech never appears after Book 3 ch 83.

---

## 2. Calendar and seasons

### 2.1 The conjunction "on the harvest's last full moon" is the night of the mill (real error, serious)
- Book 2 ch 35 (notes and prose): "The night of the harvest's last full moon. A night in the autumn… **It was the night of the mill.**"
- Book 1 ch 17: "It was black under the trees, **no moon, the new moon only six days off**." Book 1 ch 18, same night (day 8): "It was black outside, no moon."

**Why:** Book 1's moons are exact: new moon on days −15, 14 and 43; full on day 88 (midwinter) and day 117. Day 8 falls under a waning crescent.
**Smallest fix:** "last full moon" → **"old moon"**, in both places in ch 35.

### 2.2 Book 2 ch 37's `Days:` field (real error, minor)
The field reads **"Days: 172"**, but the chapter's own notes run "Night 172 to dusk 177", and the prose reaches the "hundred-and-seventy-sixth day". The Plan gives 172–177. **Fix:** change the field to `Days: 172–177`.

### 2.3 Moonlight at dusk on day 65 (real error, minor)
Book 1 ch 39 (notes and Haverly: "Very high. In the moonlight."): three dragons are seen at dusk on day 65. Day 65 is about seven days past the full moon of day 58, so the moon rises near midnight. **Fix:** "In the moonlight" → **"In the starlight"** (in both the notes and the dialogue).

### 2.4 "Three nights" with Ide (real error, minor)
Book 1 ch 59, Rowan: "You sat with Ide Darrow for **three nights**." Ch 39 has the landing at dawn on day 63 and Ide's death at dusk on day 65, which is two nights, and Maren spent the second on the island. Ch 57 has it right: "Ide, three days, in the infirmary." **Fix:** "three nights" → **"three days"**.

### 2.5 Calendar: defensible
- **Year length drifts.** Book 1 midwinter (day 88) to Book 2 midwinter (day 281) is 337 days. Book 2 midsummer (98) to midwinter (281) is 183 days. Book 2 midwinter to Book 3 midwinter (ch 57, Book 3 day 276 = Book 2 day 638) is 357 days. World.md fixes no year length, and the moon carries straight across: Book 2 ch 52 has the dark of the moon on day 278, and Book 3 ch 21 has a moonless night on its day 94 (Book 2 day 456, exactly six months later). Acceptable as it stands.
- **Two "ends of the year".** Book 1 ch 47 puts "the turn of the year" at night 81 (midwinter). Book 2 ch 88, Book 3 chs 1–2 and Book 3 ch 84 put "the last day of the year" on Book 2 day 365, in early spring. Both can stand if "the year" in Books 2–3 means the year since the lamps went out, which the ch 88 notes say ("a year from the sunrise of day 0"). Optional: "the last day of the year since the lamps."
- **Account lines.** Book 3 ch 2 puts the account's "second line" on day 3 (Book 2 day 365). Book 2 ch 88 and Book 3 ch 84 put its first line on day 365. Both lines on the same day is consistent.

---

## 3. Distances and travel times

### 3.1 The hatching caves: "four leagues" from Varrhold (real error)
- Book 2 ch 52 (prose): "**Four leagues** up the moor from the hold to the caves above Coldtarn." Book 2 ch 12 notes: "(four leagues…)". Book 3 ch 42 notes: "(four leagues from Varrhold)". World.md says the same.
- But Book 1 ch 8 has "Coldtarn lies about **five leagues** above Varrhold", and World.md puts the caves on Coldtarn's **eastern rim, across the tarn** from the hall. On the map the caves are 7.1 leagues from Varrhold (straight line), Coldtarn's centre 5.2, and the hall 3.9.

**Why:** the far side of a tarn that lies five leagues away can't be four leagues away. The map is 78% longer than the prose.
**Smallest fix:** "four" → **"seven"** in Book 2 ch 52's prose and the two sets of notes, and change World.md's "about four leagues" to "about seven". (If "four" must stay, move the caves to the western rim, but World.md says every book's maps put them on the eastern rim.)

### 3.2 Map coordinates that disagree with the prose (real errors, data only)
In `Tools/atlas/marches_items.py`:
- **Ferriby** (171.0, 99.4) is 5.4 leagues from Redwatch. The prose says "a league in from the river, up past Greyhold, by Redwatch" (Book 1 ch 38), and so does Atlas.md. **Fix:** about (173.6, 103.0).
- **Penfold** (169.4, 92.6) is 7.0 leagues from Ferriby. Book 2 ch 72 has "A boy ran up the River Road from Penfold, **a league**". **Fix:** put it about a league down the River Road from the corrected Ferriby.
- **Hollin Knowe** (171.0, 102.3) is about 3.5 leagues from the Hearthmere bank and 5.2 from Greyhold. The prose (Book 1 ch 67) and the Atlas say "two leagues west of the river". **Fix:** about (172.6, 102.5).

The chapter-end maps should then be rebuilt.

### 3.3 Distances: defensible
- **Road allowance.** World.md says road distances run "about a third longer" than the map. Atlas.md, and its table, use "straight line plus a quarter" (14 against 11 is +27%). These are close, but say one thing in both files.
- **Book 1 ch 8:** "Two days up" by cart from Harrow's End to Coldtarn, about 20 road leagues. At 7 leagues a day that's about three days (−30%). World.md has fixed it at two, so leave it.
- **Book 1 ch 38 notes:** "about a hundred and twenty leagues… nine or ten a day at a dray-beast's pace." The table gives 7–8 a day (+20–30%). Within tolerance.
- **Book 3 ch 12 notes:** Corsa to Ironhythe in "two days' flying" is about 250 leagues straight, 125 a day against the table's 80 (+56%). "A dragon in a hurry is faster" (Atlas) covers it, but this is the one travel time at the edge. "Three days' flying" would be safe if the dates allow.
- **Book 1 ch 44 against ch 46:** Greyhold is "four leagues and more downriver" from the hill above the Fenn farm, and "six leagues and more down the river" from Harrow's End. The map gives about 6 and about 4.7 (6 by road). Both lines are hedged with "and more". Leave them.
- **Book 3 ch 41:** the camp is "three leagues below Greyhold". That's 4.7 straight on the map, but the camp is on the far bank and the distance is measured downriver. Fine.
- **World.md:** a Titan-class dragon flies "about seventy leagues in a morning", yet Coldtarn to the hub (17 leagues) takes "about two hours". That would be about one hour. This is Bible-only, because the chapters (Book 3 chs 51, 67) give two hours for ordinary pairs, which is correct.

### 3.4 A stale author note (minor)
Book 3 ch 24 notes: "*note for the author*: the atlas has the Bell's reef ~25 leagues off Gullhaven, the prose 2." The atlas now puts the reef 1.9 leagues off the end of the spit. **Fix:** delete the note.

---

## 4. Deaths and funerals

### 4.1 Aurveth "lain a hundred years" (real error, serious)
- Book 3 ch 85: "the pouring-stone where Aurveth had lain **a hundred years**".
- Book 1 ch 8 notes have Ragnald "dead sixty years; Aurveth lay on Coldtarn's shore **a full year**". Ch 22: "I have lain on the shore of Coldtarn for a year." Ch 26 has the same.

**Fix:** "a hundred years" → **"a year"**.

### 4.2 Teo's pyre against World.md (real error, Bible)
- World.md: "a chief **or a chief's son** is burned in Varrhold's yard on an **eleven-day** pyre."
- Book 1 ch 16 notes: "a single night's burning, **as for a chief's son, not the eleven days of a chief**." Haldor's pyre burns "until the new moon", eleven nights (ch 2, 8).

**Fix (World.md, since the draft wins):** "a chief is burned in Varrhold's yard on an eleven-day pyre, a chief's son for a single night."

### 4.3 Funerals: defensible
- **Ulric** is burned at his own steading. Book 3 ch 22: "They raked the fire on the ninety-seventh. At Skarrow." His ashes are poured at Coldtarn. World.md's two cases (Varrhold's yard; Coldtarn's shore) don't cover him. Add one line to World.md: "a steading's head may burn at home; the pour is always at Coldtarn."
- **Sigrun, Dag and Imra** are burned on the mill field by their own dragons (Book 1 ch 20: "At dusk they burned their riders"), not on Coldtarn's shore. It's an exceptional night and the prose gives the reason. Note it in World.md if wanted.
- **Gunna and Tamsin** are poured in the Thornwood (Book 3 ch 51: "where nobody'd ever poured"). The prose marks it as a break with custom, so it's deliberate.
- Arn, Book 2 ch 24: "He killed the Sallow girl and Sigrun Holm and Dag Rorke at the mill, **with one bolt**." Book 1 ch 24 has Dag taken by Ulric's war-leader in the fighting, so the bolt killed only Imra. It reads as Arn's rhetoric, since the bolt started the fight. Optional: "…with one bolt, bought, out of a hedge, **that started it**."
- Greyhold's customs (the river-shore pyre; the hill burial for the fifty-three) are consistent throughout.

### 4.4 Do the dead come back? None do
All 37 deaths were checked: Teo; the three riders; Merrow; Ide and Bracken; Hallam and Morrow; Pell; Rook; Haverly, Kesh and Hale; Cassian; Tor and Skell; Hesper and Hush; Aurelian; Ysa; Vey; Dane; Orla Marrow; Ulric; Gunna and Tamsin; Tobin; Rowan; Corvin; Callis; Pike; Kharrak; Gannet; Lisska; Aurveth; Orrun. Every later mention is memory, a report, an object ("Haverly's edge"), a funeral, or a roll of names. Corvin, Callis, Pike and Orla are never named after they die. Each death happens once, and the on-page days match the notes. For example, Morrow "died at dusk on the hundred-and-thirty-second day. The third day", after Hallam on day 130; and Vey "died on the reef on the 348th day", which is Book 2 ch 73.

---

## 5. Character knowledge (sampled reveals: no real errors)

| Reveal | Rule | Finding |
|---|---|---|
| The twins | Book 1: one man until ch 68 | Before 68, the twins are named only in author notes (chs 5, 34, 58). Calder overhears in 68. **Defensible:** Maren's "Your brother doesn't" (ch 77) rests on her own "The man in two places" (ch 73) plus Lisska's message through Orrun, "The still one at the tower. The other one under the school", and on seeing the same face. |
| The Titan's chains | Book 1: legend only until 45 | Before 45 there's only the lullaby and Hale stopping short (ch 37). Clean. |
| Other Titans and the sleepers | Book 2: rumour until 23; the sleepers named at 41 | No "Titans" or "sleepers" in Book 2's prose before ch 23 (the carvings). Clean. |
| Hearthmere's history | Calder learns it at Book 2 chs 40–41 | No College of Tides, sleep relic, "woke it" or "Unbound" in Calder's chapters before 40. Clean. |
| The elders were Titans | Book 3: Maren and Idony at 30–31, Calder at 32, public at 46 | First stated by Idony (31), then Calder (35, 42) and Rowan (46). Kit's "didn't know if there were Titans there" (ch 20) is about the far shore, which is fine. Clean. |
| Kessmoor's plot | Never confirmed before Book 3 ch 69 | No line in Book 3 chs 1–68 states it. Clean. |
| "Why me?" | Whole answer at Book 3 ch 81 | "Carry more than one" appears only in ch 81. Clean. |
| The control relic's name | Never "the seventh" | Never used. Clean. |

---

## 6. Names and pronouns (real errors, minor)

- **Wynn is a man** (Characters.md; "his hounds" throughout). In Book 3 ch 85: "The knight with the bandaged arm put **her** hand on **her** hound's head." **Fix:** "his hand on his hound's head."
- **Ash's sex flips.** Book 1 ch 33 has "a big grey **bitch** called Ash", and Book 3 ch 85 has "**Her** name was Ash". Book 3 ch 10 uses "Said a word to **him**", "Ash put **his** nose down", "with **his** tongue out". **Fix:** use "her" in Book 3 ch 10 (four pronouns).

---

## 7. Housekeeping: Plan `Days` columns behind the chapters

The Plans say the chapter wins. These rows should be widened to match the chapter's `Days:` field (chapter first, then Plan):

- **Book 2:**
  - 18: 74–90 / 80–90
  - 24: 99–102 / 102
  - 25: 104–105 / 105
  - 26: 105–114 / 112–114
  - 27: 106–119 / 108–118
  - 28: 111–135 / 115–135
  - 29: 121–135 / 120–135
  - 31: 136–138 / 138
  - 32: 139–140 / 140
  - 33: 131–150 / 135–150
  - 35: 151–156 / 155
  - 41: 177 / 177–178
  - 43: 178–190 / 178–189
  - 51: 265–282 / 281
  - 52: 255–281 / 281
  - 53: 282–283 / 283
  - 55: 287–305 / 290–305
  - 56: 291–300 / 292–300
  - 58: 300–312 / 305–312
  - 60: 312–315 / 315
  - 61: 315–318 / 316–317
  - 63: 315–318 / 318
  - 66: 325–329 / 325–332
  - 67: 323–335 / 335
- **Book 3:**
  - 15: 66–78 / 66–76
  - 28: 119–129 / 125–128
  - 40: 147–180 / 150–180
  - 42: 149–150 / 148–150
  - 76: 319–320 / 320

Book 2 ch 37 goes the other way: there the chapter's field is wrong and the Plan is right (see 2.2).

---

## Summary of fixes, most serious first

1. Book 1 ch 51: "Wynn with Ash" → "Wynn with Sorrow". *(One life between two.)*
2. Book 1 ch 33: delete "both bonded,". *(Callis outlives Grip.)*
3. Book 2 ch 35: "last full moon" → "old moon", ×2.
4. Book 3 ch 12: "*I believed her,* said Orrun" → "*He says he believed me,* said Lisska."
5. Book 3 ch 85: "lain a hundred years" → "lain a year".
6. Book 2 ch 52 (and the notes of Book 2 ch 12 and Book 3 ch 42, plus World.md): caves "four leagues" → "seven".
7. Book 3 ch 85: "her hand on her hound's head" → "his… his"; Book 3 ch 10: Ash "him/his" → "her".
8. Book 2 ch 37: `Days: 172` → `172–177`.
9. Book 1 ch 39: "In the moonlight" → "In the starlight".
10. Book 1 ch 59: "three nights" → "three days".
11. World.md: Teo's single-night pyre; Ulric burning at Skarrow; one wording for the road allowance.
12. `marches_items.py`: move Ferriby, Penfold and Hollin Knowe, then rebuild the maps.
13. Book 3 ch 24: delete the stale note about the reef.
