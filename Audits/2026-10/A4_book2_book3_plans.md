# A4: Story-editor audit of the Book 2 and Book 3 chapter plans

**Scope.** I read `Book 2/Chapter_Plan.md` (rev. 4, 88 ch.) and `Book 3/Chapter_Plan.md` (rev. 1, 90 ch.) in full. I checked them against `README.md`; `Bible/Series_Outline.md`, `Magic.md`, `Characters.md` and `Atlas.md` (with spot checks of `World.md` and `Bestiary.md`); `Book 1/Notes/Rulings_41-79.md`; and Book 1 chs 68–79 read in full, with greps of earlier chapters. I ignored both `Outline.md` files. Nothing under the repo was edited.

**Method.** I checked the POV rotation and duplicate titles with a script; both rotations pass. Every finding below cites the plan text. Items marked **check** are likely problems that depend on a reading of the plan, or on a fact the plans don't settle.

Day numbers: "B2 d.N" means Book 2's own day count and "B3 d.N" Book 3's. "B1 ch" means a Book 1 chapter.

---

## 1. Health summary

### Book 2: *The Hunt Beneath* (88 ch.; S 35, F 35, R 18)
**Overall: sound spine, but the mechanics are loose. Needs a revision pass before drafting.**

- **Canon is mostly honoured.** The plan has:
  - the carvings of six as the first clue (23);
  - five wakings, and the control relic taken under Hearthmere (84–85);
  - the archive-bird killed by Corvin's hunters (39), and Hearthmere's history told (34);
  - the Clan united (24), Corvin surviving, and Idony surviving;
  - Orrun's shadows reaching 3–4, each as strong as he is (83), and costly, limited castings.
- **Rotation is clean.** S and F alternate strictly, R never comes twice in a row, the book opens on S and ends on F, and there are no duplicate titles inside the book.
- **The weaknesses are in the plumbing:**
  - The control relic is called "the seventh relic", against canon.
  - One meeting (11) exists because it's convenient.
  - The magic rules are applied inconsistently: dead ground, running water, charm range, and when the surge happens.
  - Lisska is an all-purpose courier at impossible ranges.
  - Several echoes come before the events they echo.
  - The Restoration's *war* (canon: "the war continues") is barely on the page.
  - Calder's canon want ("why me?") stalls for the whole book.
  - Maren is passive at her own climax.
- **Pacing:** strong Parts One, Two, Six and Seven. It sags in Part Four (Maren idles about 50 days at the Scald) and in Calder's procedural ledger chapters in Parts Two and Three.

### Book 3: *The Titan War* (90 ch.; S 28, F 27, R 8, G 7, C 6, U 6, M 8)
**Overall: ambitious, with an ending true to canon. Several settled-rule problems and one structural risk.**

- **Strengths:**
  - Saltreach is properly explored: salt-oaths, unsalting, chain money, the Far Berths.
  - The far shore and its "never sleep ashore" rule keep the ending from becoming an escape.
  - The canon last pages are in the right order, and the Council of Immortals is never named.
  - Rotation passes (no two non-S/F chapters in a row; opens and closes on S).
- **Problems:**
  - Stacked hints that Titans survive.
  - Calder's crossing doesn't come through Saltreach people.
  - Two or three meetings are there for convenience.
  - The season labels are shifted a whole season.
  - Kessmoor's betrayal is over-signposted and depends on characters keeping silent with no reason given.
  - The heroes kill every destroyer, which softens "the Titans win".
  - Book 3's casting model (bond-driven, works on dead ground) contradicts Book 2's.
  - The gods' cults have no setup.
  - Parts Four and Five (43–66) sag under councils and rehearsal set pieces.

---

## 2. Findings

### CRITICAL (breaks a settled author rule or core canon)

**C1. B3: too many hints that Titans survive.**
- *Where:* chs 78, 80, 86, 87, plus §"The land beyond the sea" and the reveal rules.
- *Quotes:*
  - ch 80: Kit "can't say whether they died";
  - ch 86: Idony "can't tell whether they went out or only went too deep to read";
  - Threads: the verse's "*it will not sleep again*, stands over 87 as a seed: the Last Titan lies under the stone, and the verse says it won't sleep";
  - Land beyond the sea: "the old ones who didn't answer (34) are still out there, as far as anyone knows."
- *Problem:* README: "At the end of Book 3, no Titans appear to remain … Don't reveal in Books 1–3 that some Titans survived." Three separate chapters stress the Bell and the Lady's unknown fate. The verse line is pinned over the Last Titan's grave. Elder Titans (README: "Titans who transcended the physical") are said to be still out there. Taken together, that is a reveal, and it undercuts "no Titans appear to remain".
- *Fix:*
  - Keep at most one quiet ambiguity: Kit's distant sighting (80).
  - In 86, have the Bell's and the Lady's breaths go out on Idony's glass like the others.
  - Drop "it will not sleep again" from 87's staging.
  - In 34, the silent old ones have "gone out", not "gone too far into the light". Delete the "still out there" seed line.

**C2. B3: Calder isn't taken over the sea by people met in Saltreach.**
- *Where:* chs 20, 26, 28, 42.
- *Quote:* "Calder by air, weeks later … with Jory Merrin piloting from Aurveth's back". Jory is first met when Calder "saves Jory and two boatloads" at sea (28).
- *Problem:* The settled rule (Series_Outline, settled points) says Saltreach "is where Maren and Calder meet the new people who take them to the land beyond the sea." Maren meets Kit in Blackwater, which complies. Calder flies on his own dragons and picks up his guide mid-sea.
- *Fix:* Calder meets Jory in Saltreach before the crossing, in Blackwater or Corsa (19–20 or 26). For example, Jory slips the Council's guard and comes to Calder to save the Berths passengers. Give a reason a dragon-rider needs a pilot at all: the Lit Shore can't be found from the air, only by the milestones of the drowned road, and only a Merrin can read them. Jory then guides him from the start.

**C3. B2 ch 11: a meeting of convenience, with a social scene.**
- *Quote:* "One night at the cave mouth Maren and Calder talk properly: fathers, Senna, one life between two."
- *Problem:* The rule: they "meet only out of necessity; each has a separate task." Ch 6 has Maren take the Fenns north "because the Titan's road runs that way". That is a coincidence, not a necessity, and the long talk is a chosen scene. The plan's own open question 2 already doubts this meeting.
- *Fix:* Maren hands the Fenns to Gunna Tarne and the ledges at the Scarfell's edge and turns east. Calder and Maren don't meet. Move the "fathers / Senna" material into his first letter (51) or into the Hall of Light talk (B3 35).

**C4. B3: a meeting of convenience (72), and one that isn't listed (63).**
- *Quotes:* ch 72: "Calder lands beside the lion, and for a few minutes they stand together on the river. 'We've got it.'" Ch 63: "A brief, practical meeting with Calder at the tarn's edge, and they argue about numbers." This is not in the "Where they meet" table.
- *Problem:* 72 is staged for sentiment ("side by side"). 63 has no need for Calder to be there; Maren opens the hall.
- *Fix:*
  - For 72, give each a task that puts them on the same spot: Aurveth's deep sight must guide the Lamp to the coal in the Last Titan's back while Orrun pins its neck. Calder must be there to relay what she sees.
  - For 63, make it Arn and Tam at the tarn, not Calder, or list it and justify it.
- *Count:* B3 then has 12, 34–35, 65, 72 and 87. Even 87 is chosen rather than needed; consider making Calder come to the door to bring the last climbers in.

**C5. B2: "the seventh relic" contradicts canon's "sixth relic".**
- *Where:* major turns ("The seventh relic is beneath Hearthmere"), chs 65, 66, 67, 76, 84.
- *Problem:* README: "the sixth relic gives it control over them"; "the sixth is the last and hardest to reach". Calling the control relic "seventh" (counting the broken one) will confuse readers and contradicts the series' own term. Book 3 avoids it ("control relic").
- *Fix:* Say "the sixth relic" or "the control relic" throughout. Keep "seventh" only as Idony's aside about the original count, if at all.

**C6. B3: the heroes kill every destroyer, which softens "the Titans win". Author decision.**
- *Where:* §What happens to the destroyers. The Antlered is killed (50), the Furnace quenched (69), the Horned Sun killed by Kharrak (82), the Pale Coil by Aurveth (85), the Bell dragged down by the Lady, and the Last Titan buried by Orrun (87).
- *Problem:* README: "the Titans win … Don't soften it into a hidden victory." When the allies kill all six, the war reads as won at an awful price, and the world was broken by the hub. The Series proposal allows "brought down by the dying lion and dragons", but stacking every kill on the heroes' side turns the Titans' win into a draw.
- *Fix:*
  - Let the Titans visibly win the field at 79: the hub breaks and the five rise over the Vale.
  - Have most of them end as "spent in winning" or destroyed by the hub's surge, as Series_Outline proposes. The lion and dragons die *shielding* people (the canon wording), not killing.
  - Keep at most one heroic kill in Part Seven, and make it costly and futile.

### MAJOR

**Magic-rule consistency**

**M1. B2: Haverly's edge works on dead ground, by a misquote of Magic.**
- *Where:* "Magic in the action"; chs 4, 20, 37.
- *Quote:* "Haverly's edge still works, because runes hold as long as their material (Magic §6)".
- *Problem:* Magic rule 6 says runes hold as long as their material **and their feeding**. Magic §5: "In dead ground an imbued object weakens and finally fails"; rule 5: "dead ground breaks everything." Ch 5's own echo has "its runes staying dark", and ch 20 uses the edge inside the Ring's league of dead ground (16).
- *Fix:* The edge is dark in Hearthmere and at the Ring. It works at Vael (37), in a surge.

**M2. B2 chs 16, 18, 20: working magic inside the Ring's dead ground.**
- *Quotes:* ch 16: "A league of dead ground round the Ring … wards guttering". Ch 20: Dane's Wardens "grounded, holding the binding-lamps' working". Ch 18: the finding-knot works at the Ring.
- *Problem:* Rule 5 and Magic §2a: a drawer on dead ground "pulls from themselves instead and can kill themselves in one release."
- *Fix:* Either make the Ring's *stones* the only live ground ("full like a cup", 16), so the Wardens must stand on them, which gives Maren a clear target; or make the binding fail and Wardens burn out, with the surge from the relic arriving at 22. The finding-knot works through Orrun only, and say so.

**M3. B2: surge timing contradicts Magic §1.**
- *Where:* chs 29, 33, 34–36, 59, 70.
- *Quotes:* ch 33 (d.135–150): "the whole of Vael's hill lit white: the surge". That is weeks before the relic is taken (36, d.172). Ch 59 (d.300–312): Calder "his first sense of a surge" at the Bell, 36 days before its relic (73). Ch 70: "sea-charms going wild a day early".
- *Problem:* Magic §1: "When a sleep relic is taken and its Titan wakes: 1. The surge." At the Ring the plan follows that order (relic 20, surge 22). At Vael and the Bell the surge comes first, and "Idony predicts a waking" from a surge is both trivial and contradictory.
- *Fix:* Define two stages in Magic.md:
  - a **stir**, when the Last Titan sits on a temple and draws (the source of the pre-relic signs, and what Idony learns to read);
  - the **surge**, after the relic is taken.
  Relabel 29, 33, 34–36, 59 and 70 as the stir.

**M4. B2: charms over running water, and at a range they can't reach.**
- *Where:* chs 26, 43, 48, 73.
- *Quotes:* ch 43: "He shouts Fisk's old boatman's wind-word … one gust, and the ferry's driven onto the stone jetty". The ferry is loose in the flooding Wend. Ch 73: "Calder tries a fire-word … it does nothing: running water". Ch 26: a herd-charm swings "a few hundred elk" off a field.
- *Problem:* Rules 4 and 5. Charms reach only touch or a few paces, and running water breaks a spoken charm. Ch 43 breaks the rule that ch 73 then enforces. Ch 26 is range far beyond a charm. B1 ch 70 (Fisk's eel-word "never worked on the river") already sets this up.
- *Fix:*
  - 43: Calder stands on the stone jetty with his hand on the guide-rope post, and the word goes into Lisska's wind *above* the water. Or the word fails and Lisska alone does it, giving him a third casting that fails.
  - 26: the charm lands on the lead cow within a few paces, and the herd follows her.
  - Also settle whether Saltreach's warranted sea-charms are runes cut into hulls. They would have to be, if the sea counts as running water.

**M5. B2 ch 37: Maren cuts a working rune.**
- *Quote:* "she cuts [the *hold* rune] into the cracking block with Haverly's edge … It holds."
- *Problem:* Magic §2: runes "are slow to make and need masters. … A wrong stroke does nothing"; writing runes that answer is Third-ring work. The plan's own rule says neither protagonist reads the script. That's beyond "limited casting".
- *Fix:* Idony cuts the strokes while Orrun's earth goes through Maren's hand on the block. Or Maren re-cuts one damaged stroke of an existing old-realm rune.

**M6. B3: casting that needs no Deep contradicts Book 2, and none of Book 2's castings carry over.**
- *Quotes:* §Magic in the war: "It works on dead ground, because it draws through the beast, not the Deep … After the gifts (37, 39) it needs no words at all."
- *Problem:*
  - Book 2 ties its castings to live ground: "Calder's first workings happen on home ground", and Maren's stand-word fails at 63.
  - Book 3 also turns "magic, but not as trained workers" (Magic §10a) into bond gifts, which Magic §2 says are *not* a discipline.
  - Depends-on-Book-2 item 18 claims Book 3 "grows from" Book 2's castings, but no finding-knot, *hold* rune, stand-word, herd-charm, hearth-word or wind-word appears in Book 3.
- *Fix:* Decide the model. My recommendation:
  - Book 3 casting is the Book 2 words and runes, said untaught with a beast's power behind them. They are huge, crude, and still need live ground, except through the bond-gift channel.
  - Bring back three Book 2 workings at key moments: the stand-word at the line (67–70), the herd-charm on the six roads (81), and the *hold* rune in the Coldtarn hall's roof (84).

**M7. B3 chs 23, 67, 69: many-voice wards on dead ground and across running water.**
- *Quotes:* ch 23: "a many-voice ward that holds for an hour" on Hearthmere's Candle Downs. Ch 67: "the many-voice ward goes up over the line" across the Vale at the hub.
- *Problem:* Hearthmere is dead ground ("A Titan's own former ground is close to dead for a lifetime", Magic §1). The hub is the Last Titan's own ground. A spoken charm across the Wend breaks on running water. The noon ward is a lovely idea, but as staged it breaks two rules.
- *Fix:*
  - Two wards, one per bank, never spanning the river.
  - Power them through the allied Titans' presence: the Lamp's and the Lady's light is the Deep in the open air (§Land beyond the sea). Say so on the page.
  - For the Candle Downs (23), use Kessmoor engines, or a ward fed by heartstone, which is itself a nice clue.

**Continuity with Book 1, and inside Book 2**

**M8. B2 ch 82: Corvin has no bound dragons left.**
- *Quote:* "Lisska's kin-voice reaches Corvin's last bound dragons in the dark".
- *Problem:* All four stolen dragons are accounted for: one freed at Vael (38–40), two recovered at Blackwater (56), one killed there. B3's dependency 15 repeats the error.
- *Fix:* Make it a bound wyvern pair or bound hounds, or set up Corvin buying dragons from Saffery/Gallows Quay in Part Five.

**M9. B2 ch 43: Calder can't be ahead of the flood.**
- *Quotes:* ch 41: "At dawn [d.182] … Calder goes south down the Wend after the flood". Ch 43: "landing in each valley town a day ahead of the water". The flood started d.177 (37).
- *Problem:* The Atlas puts Vael to the Marches at under 100 leagues, so a meltflood that left on d.177 is in the Marches days before Calder leaves Vael.
- *Fix:* Calder leaves on d.177–178 (cutting 40–41 to one night), or an ice-dam of the Coil's cold holds the water until d.182.

**M10. B2 ch 26: the beast-flood covers about 90 leagues in 1–3 days.**
- *Quote:* d.106–108: "The beast-flood comes over the Scarfell's edge." The waking was at the Moot on d.105.
- *Fix:* Use beasts that have been streaming west since the stir (13: "restless beasts"). Or date ch 26 about d.115.

**M11. B2: Lisska as a courier at impossible range.** Maren's chapters lean on "Through Orrun, from Lisska" almost every time.
- *Example:* d.98 at the Roosts (smoke) → d.100–101 the two Varrs' news at the Ring (about 90 leagues) → d.102 Coldtarn → d.105 Lake Ysse → d.106 over the Fenn top field. That's about 400 leagues in 8 days after a honey-smoke attack.
- Ruling 5 limits kin-speech to "within sight"; B1 ch 70 limits Calder's range to 3–4 leagues.
- *Fix:* Make a dated table of Lisska's flights, one every 3–4 weeks as the plan itself says ("every few weeks"). Carry the rest by letters, rumour and Idony's glasses. Reserve "through Orrun, from Lisska" for when she's physically there.

**M12. B2: echoes that come before their events.**
- ch 19 (F, d.50–60): "Lisska: the lion lay down beside its kin". That happens in ch 18 (d.80–90).
- ch 49 (F, d.225–235): "a Titan in a cage in Kessmoor". The cage closes on d.238 (48).
- ch 62 (F, d.305–318): "A captain in from the west: Solenne's palace has fallen into the sea". It falls on d.316–317, and Solenne is over 200 leagues away.
- ch 74 (S, d.348): "Lisska frantic: a wave on the coast". The wave is d.349 (75).
- *Fix:* Re-date, or swap in an echo that is already true by then.

**M13. B2 ch 2: the oath "for the first time in three hundred years".**
- *Quote:* "Greyhold's noon bell doesn't ring. Nobody says the oath, for the first time in three hundred years."
- *Problem:* B1 ch 69: "The bell rang and rang over Greyhold and nobody turned east and nobody said anything at all." The first silence was day 142 of Book 1.
- *Fix:* "the first day the bell itself is silent".

**Calendar and travel**

**M14. B3: the part season labels are shifted a whole season.**
- *Quotes:* calendar: "Midsummer falls about day 90 and midwinter about day 276". The part headers say Part Two "Summer, days 55–125", Part Three "**Autumn**, days 125–180", Part Four "**Early winter**, days 180–250".
- *Problem:* Day 125–180 is high and late summer. Day 180–250 is autumn. The calendar reset wasn't carried through to the headers. Chs 58 and 60 ("weeks before the frost", d.262–275, about two weeks before midwinter) show the same leftover.
- *Fix:* Part Two: late spring into summer. Part Three: high summer. Part Four: autumn. Part Five: early winter into midwinter. In 58 and 60, say "weeks before the river would freeze".

**M15. B3: Calder's crossing takes about 35 days by dragon, and he lingers about 30 days on the far shore.**
- *Where:* chs 26 (d.95–100) → 28 (d.125–128) → 32 (d.135–140); 39 (d.147) → 42 (d.179–180).
- *Problem:* The Atlas gives dragons 80 leagues a day. Ch 42 says Titan-class does the crossing "in a day and a night". Nothing fills his month after the gift.
- *Fix:* Calder sets out about d.118, escorting the fleet at its pace (which C2's fix gives a reason for). After 39, he comes home at once, or the Wayfarer's fading keeps Aurveth unfit to fly for a set time, said on the page.

**M16. B3 ch 2: the Bell is with the six at the Worldsend, yet Calder heads to the coast "where the Bell is".**
- *Quote:* ch 2 (d.3–6): "His task: the Saltreach coast, where the Bell is". But ch 7 (d.20–24): "Maren sees all six together for the first time" on the Hallow Plains. The six divide only by chs 9 and 11.
- *Fix:* Give him a reason that holds on d.3: Gullhaven's survivors, the Council's contract on the dragons, and Idony's prediction that the six will go home to their own ground. Or start him south after ch 9.

**M17. B3 chs 7–11, 14: marches too fast to be plausible (check).**
- About 10,000 clansfolk with herds go from the Ysse fords (d.20–24) to the Hearthmere border (d.35–40). That's well over 100 leagues on foot, about 8–13 leagues a day; the Atlas gives 8 for a fit walker.
- Ironhythe (d.55) to Blackwater (d.62) is over 200 leagues on lion-back in 7 days.
- *Fix:* Lengthen both legs (the Accord can be d.60–65), or state Orrun's sustained pace in Atlas terms.

**Plot logic**

**M18. B3: Kessmoor's plot is over-signposted, and its secrecy depends on silence nobody explains.**
- *Where:* reveal rules list 13 hints (9, 12, 33, 36, 41, 44, 46, 48, 51, 58, 61, 64, 66).
- *Quotes:*
  - ch 33: Tobin sees Callis in the works: "Tobin says nothing";
  - ch 48: "a hooded man with one hand of iron walking the works with Callis. He tells no one";
  - ch 61: Idony "notices the hand is Kessmoor work and assumes Corvin bought it."
- *Problem:* Canon needs readers to "believe, for a few chapters, that the alliance will win" (72). With this density, attentive readers will call the betrayal by Part Four, and two POV characters keep silent about the Restoration's leaders inside the Accord's works for no stated reason.
- *Fix:*
  - Cut to about five hints and spread them out.
  - Give Tobin a reason to stay quiet: Callis saved his crews, or Pike holds his three thousand's wages and bread. He does tell Rowan, and Rowan is reassured, falsely, which is better because it makes her own clause part of the cost.
  - Let Idony report the hand, and have Kessmoor *offer* an explanation (it was bought on Gallows Quay) that Rowan accepts.

**M19. B3 ch 48: the title "Six Hollows" gives the twist away.**
- *Problem:* Readers know from B2 that the control relic is a ring of six hollows (B2 relic note; Magic §5). A title saying Kessmoor's Bridle is cut to six hollows announces that it is built to take the relic. That breaks the title rule.
- *Fix:* Retitle (e.g. "The Stage", "Night Shift"), and keep the six hollows to one dim line in the chapter.

**M20. B3: the elders' cults are paid off but never set up.**
- *Where:* ch 34, and the elder Titans table.
- *Quote:* the Grey Mother is "Hearthmere's hearth-god (the hearthstone in every chapel)"; the Lady is "the sailors' Drowned Lady; the Glasswater ferry-folk's Lady (Idony's family has prayed to her for a hundred years)".
- *Problem:* A grep of the Book 1 chapters finds no "Grey Mother", "Lady" or hearth-god; hearthstones appear only as oath-stones. Book 2 doesn't plant these cults either (its one plant is the three-faced crossroads god, ch 7). The reveal at 30–34 will feel invented.
- *Fix:* Plant them in B2:
  - Nessa touching a Lady-token on the Glasswater ferry (8, 29);
  - the Sun-on-the-Stair liturgy at Solenne (55, 60);
  - a hearthstone prayer in a Hallowmere chapel (67);
  - sailors' "Drowned Lady" oaths at Corsa or Gullhaven (49, 64).

**M21. B2: the Restoration's *war* is almost absent.**
- *Problem:* Series_Outline, Book 2 established: "the war continues", and "The war widens. The Restoration's war spreads beyond the border." The plan shows Corvin's raids, money and binders, but no Restoration campaign, front or defeat. B3's dependency 31 ("No Restoration army survives Book 2 in any strength") has nothing in B2 to rest on.
- *Fix:* Add a Restoration thread:
  - the unpaid army Corvin gathers at Cotter's Cross (12) fights the Clan or Hearthmere (Parts Two–Three);
  - it breaks when the Halloran money stops (30, 49) and the Clan unites;
  - its remnant scatters at Gullhaven or in the Marches (Part Six).

**Arcs**

**M22. B2: Calder's canon want ("why me?") stalls.**
- *Problem:* README: "The farmer's want is to know why the dragons came to him." The phrase and the thread are absent from B2. They resume only in B3 32 and 85.
- *Fix:* Two or three beats: Starwatch's "one comes with three" (35) as the first real clue; the bird on Ennis and Aurveth's survivals (34); Aurveth asking him at 59 why *she* survived three partners.

**M23. B2: Maren is passive at her own climax.**
- *Where:* chs 79–84.
- *Quotes:* 79: "having lost Corvin's party in the dark"; 83 is Idony's POV with Maren "spread across five bodies"; 84: "Maren, half-conscious, sees it through the eyes of the last shadow".
- *Problem:* Her book-long task ("keep the door", 65) ends with her doing nothing decisive.
- *Fix:* Give her the choice. At 83, she decides to send Orrun and his shadows to the cellars instead of holding the vault, knowing it gives up the door. That's her protector arc, a failure she chooses, and it seeds B3 87.

**Pacing and logic**

**M24. B2: Maren and the Titan's timeline sag in Part Four.**
- *Problem:* The Furnace's cage closes on d.238 (48). Maren stays at the Scald and Orrin until d.283 (53) and leaves on about d.290 (55). Meanwhile the Last Titan's whereabouts go untracked from d.238 to d.315; other gaps are d.172→230.
- *Fix:* Have the Titan's path visible on Idony's glasses in every R chapter. Shorten the Scald stay (the midwinter and turn chapters can happen on the road to Sarovel). Or give the stay a task: guarding the cage against Corvin, which pays off his presence at court.

**M25. B3: Parts Four and Five sag (43–66).**
- *Problem:* 24 chapters of return, muster, council (52, 59), plates, ramparts, logistics (57, 58, 64) and three rehearsal skirmishes (56, 60, 62) before the battle. Then Part Six spends 14 chapters on two days of battle, and the named deaths come in a cluster: Gunna (71), Lamp (74), Tobin (75), Rowan (77), Corvin and Callis (78).
- *Fix:*
  - Merge 51 and 52; merge 57 and 66.
  - Cut one of the 56/60/62 skirmishes (keep Black Ice, 60, the mirror of B1).
  - Move Gunna's death earlier (the Thornwood, 49–51) so Part Six's deaths have room.

### MINOR

**Book 2**
- **m1. Callis's splints a year on** (B2 71: "both arms stiff in their splints"; 81: "both his arms useless"). The breaks are B1 ch 63 and ch 77. By B2 d.340 they are healed, badly. Write "badly set, weak" and drop the splints. B3 33 "stiff arms" is fine.
- **m2. When Calder leaves Hearthmere.** Ch 4's echo has him leaving "at dawn" on d.1–4; "Where they meet" says day 4; ch 5 has him there d.4–6, with ch 7 starting d.6. Pick one day.
- **m3. "Clockwise" is wrong** ("Why this order": "it goes clockwise round the old realm"). The route Ring (E/NE) → Vael (N) → Scald (NW) → Sun Stair (SW) → Bell (SE) is anticlockwise.
- **m4. The Titan's dwell times.** "A month at the Ring" vs about d.8–98 (Part One's moving draw stops in the Thornwood by d.10–25). Also, "three days, three days" doesn't match the Sun Stair (1–2 days) or the Bell (1 day).
- **m5. "Three dragons" when Aurveth isn't there.** Chs 34, 37 and 47 have the glass or the sky showing "three dragons", but Aurveth "stays on the ledges to heal" (30) and ch 40 says "one recovered dragon and two of his own".
- **m6. Ch 85 contradicts itself:** "get out by different roads … carrying Idony between them". Pick a road for Idony.
- **m7. Ch 83's POV slips.** It is Idony's chapter but reports "Maren … stops breathing for the space of a count of ten". Move that to 84, or have Idony see it.
- **m8. Ch 86: the envoys of "every kingdom" meet one day after the climax** (Solenne is about 130 leagues away). Say they came to watch the second cage spring, as at the Scald (50). Also, the ferry house stands "right under Greyhold's wall" (Ruling 18) while "Greyhold's hill falls in" (85). Check that it survives.
- **m9. The two of them share Liss's ferry house for days after 86.** In ch 87 (d.357–362) Calder writes for Idony there, while ch 88's echo has Maren on the ferry-house jetty with Wren. Wren lives in the hatching caves (52, 62). Tidy who is where.
- **m10. Ch 72 vs 78 vs 86, the direction people flee.** Maren sends people "over the Wend" (east to Saltreach); 78 has "The Marches emptying west"; 86 has "the River Road full of the people Maren and Liss moved" (the Hearthmere bank). Pick a direction.
- **m11. Ch 17: "the hedge at Fenn's mill" (check).** The mill in B1 18 is Hob's Harrow mill, and B1 68 says "the hedge at the bottom of the field".
- **m12. Ch 45: Tobin "walked in from the west" (check).** He was last at Millbrook (B1 71), east of the Scald.
- **m13. Ch 57's echo, Calder's "Come home."** It reads as calling Maren to him. Rephrase so it is about Liss or the river.
- **m14. The rotation note says R is "one in four" in Part Five;** the actual count is 2 in 12. Adjust the note.
- **m15. The lock's lit sentence never pays off.** The threads promise "Idony reads the whole of it at the end (81)", but ch 81's beat doesn't include it. Add it to 81, or drop it from the threads (open question 16).
- **m16. Calendar leftovers at Vael:** "Vael before the snow" (29, d.120–135, July); "The ice goes" on Glasswater (36, d.172, early September); "draws the road in the snow" (41). Tie the ice and snow explicitly to the Coil's cold stir, or drop them.
- **m17. Part labels:** Part Five "Late winter, days 290–325" is really just after midwinter. Part Six "Early spring, days 325–354" is late winter.
- **m18. Ch 4, check:** the lock's sentence "still burn[s] white" days later on dead ground. Allowed if it is old magic; say so.

**Book 3**
- **m19. Black book and Hale's charge left dangling.** The black book (B2 4, 32) and Hale's "Write the rest, Ashdown. After." (B1 75) never return in B3. Strong payoff: Maren writes the rest in the black book at 90, a counterpart to Calder's account.
- **m20. Haverly's edge left dangling.** Dependency 19 says "not used in this plan after Part One", but it is never used at all. Settle open question 22: Rowan at 77 would make a fine "on the gate" image.
- **m21. Fisk left dangling.** "Somebody's got to. To tell it after." (B1 70; B2 43) is unused. He is the natural voice for the ending's "after", or a named loss.
- **m22. The source of the Blackwater tip.** Ch 12 has Calder tell her ("Blackwater. Ask for a reef-pilot"), but ch 14 says "on Coll Brask's directions", and in B2 Brask is Calder's man. Pick one.
- **m23. Kin-range.** Ch 7's echo, "Through Orrun, very far south, three dragons over the sea", contradicts ch 24's "Beyond kin-range … Maren hears no other beast through Orrun" and Ruling 5 ("within sight").
- **m24. Ch 1: digging out "the last survivors" about ten days after the hill fell** (B2 d.355–356 vs B3 d.2–5). That's implausible. Make it the dead, or salvage.
- **m25. Canon labels that are really proposals.** "(canon: Book 3 may reveal it)" for the gods being Titans is a World.md working proposal ("can be a Book 2 or Book 3 revelation"). Kit's POV "author's direction … one could be a POV" isn't in Series_Outline (check). Relabel both as proposals.
- **m26. Titles.**
  - Exact duplicates across books: "Corsa" (B2 49 / B3 9), "Wendmouth" (B2 30 / B3 62), "Blackwater" (B2 56 / B3 14), "The Thornwood" (B2 13 / B3 49), "The Door" (B1 51 / B3 87), "Muster" / "The Muster" (B1 67 / B3 46), "Lamps" / "The Lamps" (B1 47 / B2 74).
  - Near-duplicates inside B3: "The Berths" / "The Far Berths" (20/26), "Ulric's Pour" / "The Pour" (22/51), "Hands" / "Two Hands" (8/35), "Far-Stone" / "Stone" (16/37).
  - Book 3's titles avoid naming deaths, but "Kneeling" (78), "The Hour" (74) and "The Door" (87) lean hard. Consider softening one.
- **m27. POV density notes don't match.** "Kit is densest in Parts Two and Three", but Part Three has one M chapter (29). "Rowan in Parts Five and Six", but four of her seven are earlier. Adjust the notes.
- **m28. The phoenix feather's origin (check).** It comes "from the far shore" (13), but Bestiary says phoenixes nest in the Worldsend.
- **m29. Ch 90: Old Grey "stands by Wren the way he always has".** Fine, but keep it visibly not understanding, so it doesn't brush README's "don't hint that anyone can still hear beasts". This is the plan's own open question 23.
- **m30. Shape says "from the week after the six fly east"; the calendar says day 0 is the morning they go up.** Ch 1 is days 2–5. Align the two.
- **m31. Tam repeats a Book 2 beat.** In B2 69 and B3 33 he forges chain for a crown with Odo saying which links fail. Give B3 Tam a turn: he sabotages a link, or he is the one who tells Tobin.

---

## 3. Book 3 "Depends on Book 2": all 37 items checked

| # | Item (B3's wording, short) | Status | Note / fix |
|---|---|---|---|
| 1 | Five awake; control relic taken under Hearthmere (84–85) | OK | B2 84–85. B2 calls it "the seventh relic" (C5). |
| 2 | The six go up from the Scarfell, east toward the Worldsend (88) | OK | B2 88. |
| 3 | Relics grown into the Last Titan's back | **Mismatch** | B2's relic note says only *sleep* relics "go into the plates"; no chapter shows it, and the control relic's placement is never stated. Add to B2 84 that the ring goes into its back, and show a sleep relic sink in at 45 or 60. |
| 4 | Destroyers' names, kinds, home kingdoms | OK (partial) | B2's temple table. "Pale Coil" and "Furnace" appear only in the table; name them in 37 and 48. |
| 5 | Kessmoor's cage held the Furnace until the call (48, 85) | OK | |
| 6 | Idony burned out; can't hold a pen (83) | OK | B2 83, 87. |
| 7 | Corvin survives one-handed with Callis; has the roll and chain-words; knows the wrong stroke (71) | OK | B2 never says Corvin keeps the roll after 85. Add a line at 85. |
| 8 | Callis alive, both arms stiff (71, 81, 85) | OK, but fix B2 | B2's splints a year on (m1). |
| 9 | Chain-ends say *hold*; a grip (47, 83) | OK | |
| 10 | Rowan alive; let go (82); speaks at the river (86) | OK | |
| 11 | Arn and Ulric united; Gunna alive and burned, with Tamsin | OK | B2 21, 24, 75. |
| 12 | Tobin alive in Solenne (63, 86) | OK | |
| 13 | Tam and Odo alive; Odo in his chair; "both forged cage-chain" (69) | **Minor mismatch** | In B2 69 Tam forges and Odo advises. B2 doesn't say where they are when Greyhold falls; add it. |
| 14 | Liss, Davin, Fisk alive; the ferry runs (86) | OK | Fisk is unused in B3 (m21). |
| 15 | Recovered dragons: Vael 1, Blackwater 2, one killed, and "the bound ones Lisska woke in the cavern (82)" | **Mismatch** | No bound dragons are left for 82 (M8). Ildra (62) is OK. |
| 16 | Orrun near Aurveth's 20 ft (86); three, then four shadows once (83) | OK | |
| 17 | Aurveth slow; deep sight (59); wound reopened; Ennis (B1 70; B2 34) | OK | |
| 18 | B2's castings; Book 3 "grows from these" | **Mismatch (use)** | The list matches B2's table, but B3 never uses them (M6). |
| 19 | Haverly's edge is Maren's (4); "not used after Part One" | **Mismatch** | B3 never uses it at all (m20). B2's edge should be dark on dead ground (M1). |
| 20 | Apart except 1–2, 11, 38–41, 82–85, 86 | OK (partial) | Also days 0–6 (chs 1–5) and B2 87's shared ferry house (m9). Meeting 11 should go (C3). |
| 21 | Calder in Saltreach: Halloran fall, Rusk fled, pardon refused, Vey dead, Brask his man, Blackwater raid | OK | B2 30, 49, 56, 73. |
| 22 | The Bell sold as a contract (59, 67); Gullhaven's spit gone (75) | OK | |
| 23 | The Gearmouth rumour (50) | OK | |
| 24 | The envoys at Liss's ferry house (86) | OK | Arrival timing needs fixing (m8). |
| 25 | Greyhold gone (85); Hallowmere dead; Dane dead (82) | OK | |
| 26 | Sarovel: Bond-King dead, Grace failed, unchosen hold Solenne, Sorrel Isle, unicorns to the Horned Sun | OK | B3's "boy-king's regency" is new; plant an heir in B2 63. |
| 27 | Isvaren: lower Vael drowned, lamps dead, ring broken, Nessa and Quell alive | OK | |
| 28 | Wyldmarch dead for 100 leagues (27); Hesper dead (25) | OK | |
| 29 | History and College complicity known to the protagonists **and the envoys** | **Mismatch** | B2 never tells the envoys; Idony confronts only Dane at 50. Add a beat at B2 86, or drop "and the envoys". |
| 30 | Archive-bird dead | OK | |
| 31 | No Restoration army survives B2 in strength | **Mismatch (B2 silent)** | B2 never shows the army's fate (M21). |
| 32 | The Oneroad's six ends meet at the hub (41, 65) | OK | |
| 33 | Shapes of light (23, 53); the seventh ring, "the Unbound" | OK (partial) | "The Unbound" is allowed by B2's reveal rules but appears in no B2 chapter. Plant it at 31 or 34. |
| 34 | The lock's lit sentence (4, 32, 81) | **Mismatch** | B2's threads promise 81 but the chapter lacks it (m15). Settle what it says (B2 open question 16). |
| 35 | Honey-smoke: groves burned (15); wet cloths (56) | OK | |
| 36 | Old magic took Corvin's hand (84) | OK | |
| 37 | The Fenns live in the hatching caves above Coldtarn (11, 52, 88) | OK | Atlas places the hatching caves above Coldtarn. B2 88's echo of Wren at the ferry house conflicts (m9). |

**Summary:** 27 OK (several partial), 1 minor mismatch (13), and 9 mismatches (3, 15, 18, 19, 29, 31, 34, and partially 20 and 33) that need a line in Book 2 or a correction in Book 3.

---

## 4. The apart rule: meeting counts

| Book | Meeting | Necessity? |
|---|---|---|
| B2 | 1–5 (d.0–6, aftermath; parting day inconsistent) | Yes (they came up together) |
| B2 | 11 Varrhold | **No:** coincidence plus a social night (C3) |
| B2 | 38–41 Vael (d.177–182) | Mostly. Both are drawn there by their own tasks; the stay could be shorter (M9) |
| B2 | 82–85 cavern | Yes |
| B2 | 86 envoys' table | Yes (witnesses) |
| B2 | 87 ferry house (unlisted co-location) | Unclear (m9) |
| B3 | 12 Accord | Yes |
| B3 | 34–35 Hall of Light | Yes (two hands); the device works well |
| B3 | 63 tarn's edge (**unlisted**) | **No** (C4) |
| B3 | 65 Eve | Yes |
| B3 | 72 the river | **No as written** (C4) |
| B3 | 87 the door | Chosen; acceptable as the book's echo, stronger with a task |

**Travel together:** none outright. Check B2 85: "carrying Idony between them".

---

## 5. Strongest and weakest ideas (reader's view)

**Book 2, strongest**
- The night every tide-glass breaks, and the "walker" mark on Idony's chart (3).
- Idony as a third POV who thinks in numbers.
- The surge and drain as a double disaster at every temple.
- Kessmoor's monstrous cage, which *holds* (48).
- The legend of being in two places moves to Maren through Orrun's shadows (25–26).
- Wren's voice bringing Ildra back (62), echoed by Lisska in the dark (82).
- The false hour of light in every dead lamp (74).
- Idony holding the Titan with the first knights' own words and burning out (83).
- Calder's handwriting growing letter by letter.
- The milestones meeting the tide-lines (41).

**Book 2, weakest**
- Lisska as the post office.
- Calder's Parts Two and Three as a money-trail procedural (14, 17, 19, 30, 35). Starwatch (35) is a detour.
- Maren idling at the Scald.
- "The seventh relic".
- The outlaw winning over the crown in one speech (46).
- The second visit to Corsa (68) repeating 49.

**Book 3, strongest**
- Saltreach as a working system: salt on the tongue, unsalting, chain money, the one-copper harbour contract (15).
- "Never sleep ashore", which forecloses escape.
- The elders hearing only two bonds together.
- Kit's arc from the contract to no price, ending with the salt shared out (83).
- The noon "Keep the watch" ward, a jailer's charm turned into a protector's (needs M7).
- The betrayal hidden in plain sight as a fallback Rowan signed.
- Orrun keeping the door.
- "Who pours?"
- Tam's flint fire.
- Calder writing the account's last page.

**Book 3, weakest**
- A key plot device resting on a pun: Gannet and Kessmoor reading "a breath that is unbound" as "an engine breathes too" (36, 44).
- Too many hints of Kessmoor's plot, and characters who keep silent with no reason given (M18).
- Every destroyer killed by the good side (C6).
- The stacked seeds of survival (C1).
- Elder exposition at 35–36.
- Two months of musters and councils (M25).
- Calder's month-long dragon crossing (M15).

---

## 6. Author decisions that matter most

1. **How Book 3's destroyers end.** Do the Titans visibly win the field (C6), and which, if any, keep an *undetectable* ambiguity for the next series (C1)? Choose one seed at most.
2. **The casting model across Books 2 and 3.** Do Maren's and Calder's workings need live ground, and do Book 2's words survive into Book 3 (M1–M7)? Then update Magic.md §10a, and add the stir/surge distinction to §1 (M3).
3. **Calder's Saltreach guide** (C2): who takes him over, where he meets them, and why a dragon-rider needs a pilot.
4. **The meetings:** cut B2 11; re-task B3 72; remove or justify B3 63 (C3, C4).
5. **The Restoration's war in Book 2** (M21): canon says it continues, so give it a front and an end.
6. **Kessmoor's secrecy** (M18, M19): how many hints, and why Tobin and Idony stay silent. Retitle "Six Hollows".
7. **The relic's name** (C5): "sixth" or "control", never "seventh".
8. **Maren's Book 2 climax choice** (M23), and **Calder's "why me?" beats in Book 2** (M22).
9. **The calendar:** fix B3's part labels (M14), and set travel against Atlas pace (M9, M10, M15, M17).
10. **Setups to plant in Book 2** for Book 3's payoffs: the elders' cults (M20), the control relic in the Titan's back (dependency 3), the lock's sentence (dependency 34), the boy-king heir (dependency 26), and "the Unbound" (dependency 33).
