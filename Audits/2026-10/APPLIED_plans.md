# Applied: Book 2 and Book 3 chapter plans

Scope: only `work/Book 2/Chapter_Plan.md` (now revision 5) and `work/Book 3/Chapter_Plan.md` (now revision 2) were edited. The Bible was read but not edited; another agent is working on it. Sources were A4 (all findings), A3 (M8, M21, m6, m9, m25, m26, §3), A2 (the "Book 1 text vs Book 2 Outline" table and "setups still open"), DECISIONS.md, Rulings 1–39, `Magic.md`, README, Atlas, and Book 1 chs 68–79 (checked by grep).

Method: surgical string replacements, plus whole-row rewrites where a beat changed. Book 2 keeps its 88 chapters. Book 3 was edited in its old numbering, then cut to 86 chapters and renumbered by script. The script masks Book 1 and Book 2 references, day numbers, Magic §§, prices and the Days column, and the "Depends on Book 2" list, the open questions and the revision note were written by hand in the new numbering. Every renumbered number was reviewed in the script's change log. A first-pass bug (numbers followed by a comma were skipped) was caught and fixed by a second pass that changed 33 more numbers; one skipped table row was fixed by hand.

**Final counts.** Book 2: 88 chapters (S 35, F 35, R 18). Book 3: 86 chapters (S 27, F 26, R 8, G 7, C 5, U 5, M 8).

**Verification** (script: `scratchpad/check.py`):
- Both books number their chapters 1..N with no gaps.
- S and F strictly alternate with each other.
- No two non-S/F chapters fall in a row.
- Book 2 opens on S and closes on F; Book 3 opens and closes on S.
- No title repeats inside a book.
- No title repeats across Books 1–3 (comparison ignores a leading "The").

**Book 3 renumbering map** (old → new):
- 1–51 unchanged.
- 52 merged into 51.
- 53–55 → 52–54.
- 56 cut (folded into 53).
- 57 folded into 62.
- 58 folded into 58.
- 59–90 → 55–86.

## Critical

| ID | Applied how |
|---|---|
| C1 | **B3:** Kit's distant sighting (76) is kept as the only ambiguity. At 82 the Lady's and the Bell's breaths go out on Idony's glass like the others. The "it will not sleep again" seed over the door is dropped from the threads and the reveal rules. At 34 the silent old ones "have gone out"; the elder-faction note says the same. The "still out there" seed is deleted. The reveal rules and question 1 are rewritten to match. |
| C2 | **B3 26** (retitled "The Pilot"): in Blackwater, Jory slips the Council's guard and comes to Calder to save the Berths passengers. The Lit Shore can't be found from the air, only by the drowned road's milestones, which only a Merrin reads. Jory guides him from the start on Aurveth's back (28, 32, 42). The Saltreach people, "Who goes", the premise and the major turns are updated. |
| C3 | **B2 11** (retitled "The Scarfell's Edge"): Maren hands the Fenns, the greys and Old Grey to Gunna Tarne and the ledges at the moor's edge (Calder sent Gunna, 10) and turns east without going the last three leagues. Wren gives Calder a stone from her (12). The fathers / Senna / one-life talk moves to his first letter (51) and to B3 35 ("for the first time in two books"). The "Where they meet" tables in both books, the B2 major turns, the threads (missions, letters, Wren, Maren's arc) and B3 dependency 20 are updated. |
| C4 | **B3 68:** a task, not a reunion. Only Aurveth's deep sight sees the coal, and the elders hear only two bonds together, so Calder lands beside the lion and the Lamp is guided by both. **59:** Arn and Tam at the tarn, not Calder; Calder is told by letter. **83:** Calder is at the door because he's bringing the last climbers in (81 ends on it). The "Where they meet" table lists 12, 34–35, 61, 68 and 83, with a "Not a meeting" note for 59. |
| C5 | **B2:** "the control relic" or "the sixth relic" throughout (major turns, 65, 66, 67, 76, 84, reveal rules). 53's "seventh thing" is now "a ring with six hollows". "Seventh ring" (Isvaren's rank) is kept, since it isn't the relic. Settled list: "never seventh". **B3** already complied. |
| C6 | **B3:** the Titans visibly win the field at 75 (the Last Titan and its three rise over the broken Vale). The Antlered's death (50, feeding the master, 52) and the Furnace quenched in the glimpse (65, "the last the alliance will kill") are kept. After 75 no hero kills anything. Kharrak (78) shields the column and doesn't kill the Horned Sun. Aurveth (81) lies across Hollow Beck's mouth, taking the Coil's cold. Lisska spends her wind on the storm. Orrun brings the mountain down to shield the hall (83). The Horned Sun, the Pale Coil, the Bell and the Lady burn out in the surge and go out on the glass (82). The Last Titan's breath, under the stone, is the last (83). The campaign table, the lion-and-dragons table (with a "shielding, not killing" note), the destroyers paragraph, the deaths table, the major turns and the pacing notes are all updated. |

## Major

| ID | Applied how |
|---|---|
| M1 / A3 M21 | **B2:** Haverly's edge is dark on dead ground (4, 5, 20, 84) and wakes only in Vael's surge (37). "Magic in the action" now says "runes hold as long as their material *and their feeding* (Magic §10 rule 6)". The castings rules note is updated to match. |
| M2 | **B2 16, 18, 20:** the ring-stones are the only live ground in the dead league, so the Wardens must stand on them, and getting them off is Maren's target (20). The finding-knot is string in her hand and works only through Orrun (18). A "Live ground at the Ring" bullet is added. |
| M3 | The **stir** (the Last Titan sitting on a temple and drawing; old stone over the temple fills while the land round it dies) now comes before the **surge** (after the relic is taken). It's defined in B2's temple section as a proposal for Magic §1. 16, 29, 33, 36, 44, 58, 60, 70 and 74 are labelled stir; 22, 36–37, 45–47, 60–61 and 73 surge. The temple table has new Stir and Surge columns. 59 is relabelled as Calder sensing the Bell's sleeper breathing, not a surge. Idony's sentence becomes "a stir, a flood and then a famine". |
| M4 | **B2 26:** the herd-charm lands on the lead cow by touch, and the herd follows her. **43:** the wind-word fails (dead ground and running water), Lisska does it alone, and the casting table marks it **Fails**. **70:** Saltreach sea-charms are settled as runes cut into hulls and oars. Touch-range examples are added to "Magic in the action". |
| M5 | **B2 37:** Idony cuts the *hold* strokes with Haverly's woken edge (Third-ring work, and he's Second-ring; in a surge it answers), while Orrun's earth goes through Maren's hand on the block. The castings and shadows tables are updated. |
| M6 | **B3 "Magic in the war"** is rewritten. Casting is Book 2's words and runes said untaught with a beast's power behind them: huge, crude, needing live ground, touch range, and broken by running water. Only bond gifts work on dead ground. Chs 1 and 7 are relabelled as bond gifts. Ch 2 becomes Ada's hearth-word with Kharrak behind it. Three Book 2 workings return: the stand-word at the line (66), the herd-charm on the road north (75, heard on the six roads, 77) and the *hold* rune in the hall's roof (80; Idony says the strokes, Tam cuts, Maren carries Orrun's earth). Dependency 18 is updated. |
| M7 | **B3 55, 63, 65:** two wards, one per bank, never across the Wend, fed by the Lamp's and the Lady's light (the Vale is the Last Titan's dead ground). **23:** the Candle Downs ward is fed from a Kessmoor heartstone wagon. "Everyone else's magic" is updated. |
| M8 | **B2 82:** Corvin's last bound beasts are a wyvern pair. Lisska's kin-voice gets no answer, because a wyvern isn't kin, and Kharrak drives them off. The Wren thread now reads "Lisska tries the same… and a bound wyvern doesn't answer". **B3** dependency 15 is fixed. |
| M9 | **B2 38–41** now run day 177 into the night, and Calder leaves at dawn on day 178. 43 says he's under two days ahead by dragon (the flood takes about five by water). The bird is burned and Idony's ring is broken at the pyre that night (40). The Part Three and Part Four headers are adjusted. |
| M10 | **B2 26** is re-dated to d.112–114: the Thornwood's beasts have streamed west since the stir began, and the waking turned the stream into a flood. 27 becomes d.108–118. |
| M11 | **B2:** a dated "Lisska's flights" table (six flights, every three or four weeks, with dragon pace). Every "through Lisska" echo was checked. Where she wasn't there, it's replaced with rumour, a letter or Idony's glass (13, 15, 17, 19, 20, 22, 23, 24, 25, 52, 53, 62, 64, 66, 72, 74, 88). The "physically present" uses are tagged with their flight numbers. 64's out-of-range bond echo is removed, and 66's extra flight is folded into flight 6. |
| M12 | **B2 19, 49, 62, 74:** 19's and 62's echoes are replaced. 49 is re-dated to d.240–248, after the cage closes. 74's echo is now a river sign. |
| M13 | **B2 2:** "the first day in three hundred years the bell itself is silent". |
| M14 | **B3 parts:** One spring (0–65); Two late spring into summer; Three high summer; Four autumn; Five early winter into midwinter; Six deep winter; Seven late winter. The season scheme is stated in Shape. Black Ice (56) reads "weeks before the river would freeze". The old 58 echo went with the merge. |
| M15 | **B3 26:** sets out d.118 with the fleet at its pace. **28:** the wreck. **42:** home at d.148–150, the day after the gift. 41 is re-dated to 145–150 and its "hill out of the sea" line is cut, since Orrun is still underground. 42's echo is now Aurveth's sight of him under the sea. |
| M16 | **B3 2:** Calder's reasons on d.3 are Gullhaven's survivors, the Council's contract on his dragons, and Idony's reading that each of the six will go home to its own ground. |
| M17 | **B3** Part One and Part Two are re-dated: the fords d.18–26, the border d.44–50 (about six leagues a day with herds), the Accord d.60–65, Blackwater d.76–80, Corsa falls d.88, and the rest follow. Shape states Orrun's pace (about twenty leagues a day). |
| M18 | **B3:** five hints remain: 12, 41, 46, 57, 62. Removed: 9's resin, 36's "an engine breathes" pun (the reading moves to the reveal at 69), 44's and 60's Gearmouth, 46's packet echo, 48's iron-hand man, and the six hollows (one dim line now). The resin (58) and the plates (51) are relabelled as open, approved fallback. Tobin writes to Rowan about Callis (33) and Pike explains him away (41). Tobin keeps quiet to everyone else because Pike holds his crews' wages and bread. Idony reports the hand and Pike explains it as Gallows Quay work (57). Rowan's acceptance is called part of her cost. |
| M19 | B3 48 "Six Hollows" → "Night Shift", with one dim line about the ring. |
| M20 | **B2 plants:** the Lady-token on Nessa's ferry (8) and salt over the prow (29); Vey's Drowned Lady oath at Corsa (49) and Gullhaven's brine-cup (64); the Sun on the Stair liturgy on the pilgrim road (55) and in the palace chapel (60); the hearthstone and hearth-mother in a Hallowmere chapel (67). Added as a thread, a reveal-rule line and B3 dependency 38; the B3 elder table cites them. |
| M21 | **B2:** a "Restoration's war" thread with a front and an end. The army is gathered at Cotter's Cross (12, 14, with Reede). Steadings are burned to keep the Varrs at war (19). It moves into dead Hearthmere (Ashford, the Candle Downs) and Rowan fights it with steel (43, 46). It's paid by the Halloran mint (30) until the house falls (49), breaks at Cotter's Cross (54, a new major turn), drifts to the river as bands (72), and its last band breaks at the landing (80). Also in the parts' headers, the antagonists row, the deaths table and B3 dependency 31. |
| M22 | **B2:** "why me?" beats: the bird on Aurveth's survivals (34), Starwatch's "one comes with three" as the first real clue (35), and Aurveth asking him at 59. Added as a thread. |
| M23 | **B2 83:** Maren chooses to send Orrun and every shadow to the cellars, giving up the door. **84:** she's alone at the vault with a dark sword. **B3 83** says "this time the door is kept". The thread, major turn and open question are updated. |
| M24 | **B2:** the Titan's path is now on Idony's glasses in every Part Four–Five R chapter (44 the Scald's stir, 47, 50 out over the Western Deep, 58 the Sunward Hills stir). Maren's Scald stay has a task (53): the temple under fused glass is reachable only down the cooled Furnace shaft, and Corvin's agents try to buy their way down first. |
| M25 | **B3** Parts Four–Five go from 25 to 21 chapters: 51+52 merged into F "Plates"; the Sun Road skirmish (56) cut and folded into 53 (with Pell's restraint); Resin (58) folded into Wendmouth (58); Engine-Trains (57) folded into Watches (62); Black Ice kept (56). Gunna's death moves to the Thornwood (49), and 67 no longer has a named death. The book is renumbered to 86, with every cross-reference updated. |

## Minor

| ID | Applied how |
|---|---|
| m1 | B2 71 and 81: "badly set and weak", no splints. B3 dependency 8 is updated. |
| m2 | B2: Calder leaves at dawn on day 6 (5). 4's echo now shows Aurveth failing to lift; "Where they meet" reads 1–5, days 0–6. |
| m3 | "Anticlockwise", with the route spelled out. |
| m4 | Dwell times: about three months, seven weeks, a month, two weeks, a day. Wakings: about a week, then five days, three, one or two, then within the day. 75 "at once" → "within the day". |
| m5 | Aurveth's absence is respected: 34 "Two. The glass says three", 37 "Two dragons", 47 "the three-dragon stir whole again". Aurveth rejoins at Corsa (49). |
| m6 | B2 85: Idony goes up through the rock with Maren and Orrun. |
| m7 | B2 83: Idony sees and counts her ten breaths. |
| m8 | B2 80/86: the envoys came to watch the second cage spring. The ferry house stands cracked under the fallen wall. |
| m9 | B2 87: Calder stays two days to write for Idony, and Maren has gone down the River Road. The 88 echo comes via Lisska from the river; Wren is at the caves. |
| m10 | Fleeing **east over the Wend**, away from the binders on the Hearthmere bank: 72, the 78 echo, and 86 (the Drover's Way and the Saltreach bank full). |
| m11 | B2 17: "the hedge at the bottom of the Fenn field" (B1 68). |
| m12 | B2 45: Tobin walks in "from the east", from Millbrook. |
| m13 | B2 57: "Liss says come home." |
| m14 | B2 rotation note now gives the real R densities per part. |
| m15 / m18 / A2 setup 6 | B2 4: the lock is old magic, so dead ground doesn't touch it. B2 81: Idony reads the sentence aloud, carved again over the vault. Proposed wording: "One hand shut it. Two hands open it together. What is opened together is kept together, or it is not kept." It's left as Book 2 open question 1, and B3 34 quotes it. |
| m16 | B2 29 "high summer" and the Coil's cold on the lake; 36 "the Coil's cold has skinned Glasswater with ice in late summer"; 38 "surge-frost"; 41 "the frost the Coil's surge has laid"; 42 "autumn sleet". |
| m17 | B2 Part Five: "Deep winter, after midwinter". Part Six: "Late winter". |
| m19 | B3 86: Maren writes the rest in Hale's black book. Added as a thread. |
| m20 | B3 55: Maren gives Rowan Haverly's edge. 73: it's dark on the gate, only steel. Added as a thread; open question 22 is settled. |
| m21 | B3: Fisk is in the remnant (80) and tells it after (86), with a "not chosen" line and a thread. |
| m22 | B3 14: Maren comes "on Calder's word at Ironhythe". 12 cites his Blackwater raid. Brask's entry is corrected. |
| m23 | B3 7's echo is now a horse-clan scout's sighting. |
| m24 | B3 1: digging out the dead and the salvage, not survivors. |
| m25 | "Book 3 may reveal it" is relabelled as a World.md proposal (premise, major turns, 31, reveal rules). Kit's POV is relabelled "canon: Saltreach people take them over; proposal: a POV". |
| m26 | Titles renamed. **B3:** 9 Corsa → The Houses' Table; 14 Blackwater → Salt on the Tongue; 49 The Thornwood → Fire in the Forest; 87 The Door → The Threshold (new 83); 46 The Muster → Banners; 62 Wendmouth → The Floating Market (new 58); 26 The Far Berths → The Pilot; 8 Hands → Wages; 37 Stone → Consent; 78 Kneeling → The Coal (new 74); 30 The Grey Mother → What She Showed. "The Pour" disappears in the merge. **B2:** 74 The Lamps → One Hour of Light; 32 The Keeper → Door-Keeper (A3 m27). Kept: B3 "The Hour" and B3 "The Watch" (it echoes B1 "Keep the Watch" without matching it). |
| m27 | B3 density notes now match the counts. |
| m28 | B3 13: the feather's origin is unspoken; "from the far shore" is dropped. |
| m29 | B3 86: Old Grey looks at Wren kindly and doesn't understand. |
| m30 | B3 Shape: "from the morning the six go up". |
| m31 | B3 33: Tam forges one link to fail, with Odo's mark inside it. At 74 the Bridle fails on Idony's stroke and Tam's link. Thread and open question added. |

## The user's additional items

| Item | Applied how |
|---|---|
| Lock lit on dead ground; read at 81 | See m15. |
| B2 12 "two" | The crown hung Cassian's body on Greyhold's gate (added at 4), and the companies have seen Corvin alive. A reveal-rule line is added. |
| Corvin keeps the roll after 85 | B2 85; B3 dependency 7. |
| Control relic into the Titan's back | B2 84, with sleep relics shown sinking in at 45 and 60. The relic note is updated, and the stone matches Magic ("grey old-realm stone", A3 m9). |
| Boy heir in Sarovel | B2 63, carried to Sorrel Isle with the tribunes ruling in his name; B3 8 and dependency 26. |
| "The Unbound" | Planted at B2 34 (the bird says it once). The Ruling 38 conflict stays open (B2 question 11). |
| College complicity told to the envoys | B2 86: Idony tells the table and Isvaren's magister doesn't deny it. B3 dependency 29. |
| Corvin's key (DECISIONS 9) | B2 76: their father found the older stair and the hooked-bow key digging a drain under the grooms' yard (proposal). 77: the stair's head is under the grooms' burial ground. This also answers A2 setup 3. B2 question 5. |
| Other DECISIONS | Rowan at Redwatch at dusk is consistent with B2 1. Rook's ledger in Delling's chest is cited at 14. The Fellow is dead (nothing in the plans contradicted it). Halloran's drawer: no plan beat touches her. |
| B2 questions 11, 12, 14, 15, 27 | 11, 12 (survival) and 14 are now in a "Settled" list. 15 is corrected (Hale's belief, B1 ch 49; the bird confirms it at 34). *The Six Who Sleep* is dropped from question 27 and marked retired at the top. A3 m25 (turn-table order) was already correct. A3 m26: "east-north-east" for the Ring; the flight to Vael is "west" (20, 27, 28). |
| Open questions | Both lists are rewritten with the most important first, plus "Settled" sections. |
| Depends on Book 2 | All 37 items are rechecked against revision 5 and marked; four new items are added (38 cults, 39 stir, 40 key and stair, 41 beasts). |
| Revision notes | B2 revision 5 and B3 revision 2 each get a summary paragraph. |

## Coordinator direction: beast-oriented, not dragon-oriented

The dragon-centred beats were rebalanced without touching canon (the dragons becoming Titan-class, the lion becoming a Titan, the ending).

**Book 2:**
- 1: the knights on greyharts with hounds and falcons, whose bonds still hold on dead ground.
- 25: stonehorns, wolves, bears and duskcats holding the Moot's lanes.
- 37: the tusker herd and the Wardens' snow lynx in drowned Vael.
- 48: the harvested ironbacks in the cage.
- 63: the olifant wall and the bond-steeds at Solenne.
- 70: reefwyrms and gull-hawks.
- 73: Vey's wyverns Sable and Hask (B1 32).
- 75: Vey's leaderless wyvern company at Gullhaven.
- 80: hounds and greyharts at the landing.
- A new "Every kingdom's beasts" thread.

**Book 3:**
- A new "The beasts of the war" paragraph, with the air shared by the Clan's dragons, Wyldmarch rocs, Isvaren stormkite-riders and Saltreach wyvern companies.
- Arn's C role is "the air front, shared", not "the dragon front".
- Beasts written into 7, 8, 9, 10, 15, 23, 38, 46, 49, 50, 53, 55, 56, 58, 64, 65, 67, 70 (the smoke opens every beast, not just the allied Titans), 71, 73, 77, 79, 80, 84 (every bonded pair, not just the Clan's) and 85.
- A "Saltreach's beasts" paragraph.
- The remnant includes beasts.

The flier names follow `Bestiary.md`'s new "The sky" section, which landed during this pass (Worldsend roc-riders, a handful per clan; stormkite-riders as light scouts; Saltreach wyvern companies; no riders of the air in Kessmoor, Hearthmere or Sarovel). B3 38 was adjusted to match.

## Skipped or partial, and why

- **A4 M4 (43), first option:** the jetty is on Greyhold's dead ground, so the word couldn't work there. I used A4's other option (the word fails; Lisska alone).
- **A4 M3's Magic.md change**, the "stir" in §1: not made, because the Bible is out of scope. It's flagged in both plans' open questions.
- **A4 m26, "The Hour" (B3 70):** kept. Two of the three leaning titles were softened (The Coal, The Threshold), which is what A4 asked ("consider softening one").
- **Near-duplicate titles across books that aren't exact:** B1 "The Ferry" / B2 "The Ferry House", and B1 "Keep the Watch" / B3 "The Watch". Left as echoes, since they aren't exact duplicates.
