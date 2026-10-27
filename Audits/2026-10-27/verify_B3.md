# Verification: Book 3 Critical and Major findings

Verifier: independent pass over `findings/B3_*.md`. I re-opened every cited line, plus the Atlas (`Bible/Atlas.md`) and `Tools/atlas/world.py`, and checked Books 1–2 wherever a fix might touch them. No repo file was edited.

**Totals (54 Critical and Major findings):** 35 CONFIRMED, 17 ADJUSTED, 2 REJECTED (B3-24-a, B3-45-b).

## The root cause behind the geography findings

Book 3, Parts One to Four, are drafted on a **mirrored map**. In the drafts, Hearthmere (the Greenwold, the Candle Downs, Hallowmere) lies *east* of the Marches, between the Wend and the Plains. The Atlas puts it the other way round, and so does canon in Books 1–2:

- Book 1 ch 49:28: "Hallowmere lies to the west."
- Book 2 ch 14:146 and ch 43:24: the Restoration crosses the Wend and goes *west* to the Candle Downs.
- The Atlas: Saltreach, the Marches and the Clan all lie east of the Wend.

The same mistake shows up again and again in the drafts:

- the Ysse is made Hearthmere's border (chs 4–11);
- Greyhold to Hallowmere is called "north and east" (10:43);
- Hallowmere is evacuated "west toward Greyhold" (ch 23);
- the glass line runs Thornwood, Greenwold, Downs, camp (ch 52);
- from Coldtarn, Aurveth looks "east" to the Mere (42:473, 45:63, 237, 259).

Fix these as **one pass** with one rule: going east from the Wend, you are in Saltreach.

Parts Five to Seven have a separate problem. They **compress the Marches**: the lower Wend is 12 leagues, Harrow's End is put up on the moor, and Coldtarn is reached overnight.

---

## Systemic geography maps

### 1. The Ysse treated as Hearthmere's border (B3-07-a, plus 10-a, 10-b)

Chapters that need changes:

| Ch | Lines | What the draft says |
|---|---|---|
| 4 | notes 13, 14, 16, 18; prose 290, 334, 346 | Maren walks "east... away from the river" without crossing the Wend; at dusk she looks back at "The Saltreach bank beyond" |
| 7 | notes 12, 15, 18, 19, 20; prose 26–32, 196, 362, 378–400, 428 | "Hearthmere on this side"; "into Hearthmere"; the crown's knights and the scout on "the Hearthmere bank" |
| 10 | notes 12, 14, 17; prose 43, 137–141, 151, 311 | "the Hearthmere bank of the Ysse"; "the eastern march, between the Ysse and the oaks"; "down toward the Ysse valley"; "North and east" |
| 11 | notes 12; prose 25 | "the eastern march... a hundred leagues of downs" |
| 23 | notes 12 | "across the eastern march south of the Greenwold" |
| Ledger | `Notes/Part1_Ledger.md` 8, 9, 21 | the same claims |

Mentions that need no change: chs 17, 21, 30, 40 and 43 ("the Ysse fords", "the ridge at the Ysse"), 11:37 and 11:419. These still hold if the Ysse is the Plains' river.

**Recommendation: fix the prose. Moving the Atlas isn't possible.** To make the Ysse Hearthmere's border, Hearthmere would have to swallow the Marches, the Scarfell and Saltreach's north. That would break Books 1–2 on every page: Harrow's End and the Clan are on the Saltreach bank, and Hallowmere is west of Greyhold. The Greenwold appears nowhere in the prose of Books 1–2, so its Atlas spot (just west of the upper Wend) is free to use for the shut border.

### 2. The lower Wend at 12 leagues (B3-58-a, B3-68-a)

The canon distance from the hub to Wendmouth is about 100 leagues:

- world.py: the hub at (175.6, 103.5), Wendmouth at (183, 204);
- Book 1 ch 32:298: "a hundred leagues south";
- Book 1 ch 38:291: the "man in two places" plot depends on Wendmouth being a hundred leagues from Ferriby;
- Book 1 ch 50:58: 120 leagues "on the drove road".

Chapters that need changes:

| Ch | Lines | What the draft says |
|---|---|---|
| 58 | notes 12; prose 28, 36, 218, 424, 474 | "twelve leagues"; the market is towed to the Staithe and counted "two days later" |
| 63 | notes 15 | fine as written |
| 68 | notes 15; prose 153 | "twelve leagues off, at the Wend's mouth" |
| 70 | 311, 323, 337 | the shadow at the mouth "all morning"; fine at a Titan's run |
| 74 | 9, 23, 437, 527–537 | the mouth seen from the hub |
| 75 | 194, 204, 486 | "the sea lit at the mouth", seen from the hub |
| 76 | notes 12–17; prose 27, 67, 113, 279–319 | Kit at the Staithe, "four leagues to the mouth", watches the Bell and the Lady from the masthead |

Ch 60's "eight leagues" from the Staithe to the hub can stay. So can ch 56's Eskby, "twelve leagues above the hub".

**Recommendation: fix the prose. The Atlas can't move,** because Books 1 and 2 fix Wendmouth at a hundred leagues.

The reviewer's rescale is incomplete. It leaves out ch 76, which is the hardest chapter: Kit has to be near the mouth to see the Bell and the Lady go down. Either she goes down to Wendmouth rather than the Staithe, or the sighting changes. It also leaves out the sightings of the mouth from the hub in chs 74–75, which must become Orrun's or Aurveth's far-sense.

One of the reviewer's changes isn't needed. Calder's daily flight to the mouth and back can stay: Titan-class dragons fly about 70 leagues "in a morning" (49:52).

### 3. The Candle Downs and the Greenwold placed between the Thornwood and the Wend (B3-49-a)

Chapters that need changes:

| Ch | Lines |
|---|---|
| 49 | 30, 52 |
| 50 | notes 20; prose 447 |
| 51 | 207 |
| 52 | notes; prose 54–56, 64, 98–104, 158 |
| 53 | notes 12–13; prose 33, 99–101; also `Notes/Part4_Ledger.md`:9 |
| 45 | 259 ("Over the Wend... Over the Candle Downs... To the Mere") |
| 23 | Downs "east of Hallowmere" |
| 62 | 138 (Tobin on "the empty Candle Downs") |
| 64 | notes 9; prose 349 ("the Candle Downs side" at the hub) |

**Recommendation: do both.**

- **Prose for chs 49–53.** Prose is the only fix here, because the breath runs Thornwood, stations 2–4, then the camp in time order. Every station before the camp must lie east of the Wend.
- **Optional small Atlas change** that fixes chs 23, 45, 62 and 64 for free: extend the Candle Downs polygon north-east from the Mere to the Wend's west bank below the Brackenwood. The Atlas text currently says "south of the Mere"; it would read "south and east of the Mere". Books 1–2 don't contradict this. Book 2 has the downs west of Greyhold (Book 2 ch 14:146, ch 74:75), so the change agrees with them.

### 4. Liss's ferry house at the eddy (B3-53-a, B3-57-a)

Canon puts the ferry house under Greyhold's wall:

- Ruling 18;
- Atlas.md:177;
- world.py ferry at (174.2, 107.3);
- Book 2 ch 86;
- Book 3 ch 1:366–368 and ch 3:30.

The eddy (where the island was) is 3.5 leagues upriver.

Chapters that treat the house as standing at the eddy: 51, 52, 53, 55, 57, 58, 59, 60, 61, 62, 63, 65, 67, 68, 69, 73, 74, 75, 82, 84. The anchors are:

- 53:371 and 53:377 ("as it always had");
- 55:44–46 and notes 12 (the Ferry Barn);
- 57:38–40 ("his old room");
- 62:210;
- the Part 7 ledger line 16.

**Recommendation: fix the prose with one explanatory beat. The Atlas can't move,** because Books 1–2 fix the house under Greyhold. Have Liss move scow, rope and household up to a house above the eddy after the hill fell. Then:

- 53:371 and 53:377 change;
- 57:38–40 becomes "Or its twin...";
- every later "ferry house" refers to the new one and can stay.

### 5. Harrow's End and Cotter's Cross (B3-59-a, B3-78-a, Minor B3-54-d)

The fixed points are:

- **Harrow's End** is 1.5 leagues from the island, on the Vale floor, with fields down to the water (Atlas.md:8, 96).
- **Cotter's Cross** lies about 10 leagues *south* of Harrow's End on the Way to Wendmouth (Atlas.md:61; world.py (180.5, 113); Book 1 ch 16; Book 2 ch 12:436).
- **The Scarfell's edge** lies above the Fellwood, "three leagues south-east of Varrhold" (Book 2 ch 11 notes), about 8–10 leagues up the Way from Harrow's End.

Chapters that need changes:

| Ch | Lines | What the draft says |
|---|---|---|
| 54 | 192 | "Through Cotter's Cross, through Harrow's End" |
| 56 | notes 20; prose 477, 485, 489 | |
| 59 | 38 | |
| 67 | notes 17; prose 380 | |
| 77 | notes 13, 18; prose 76–80, 102, 294 | "Scarfell's foot at dawn... lip a day off"; "the lip at Harrow's End" |
| 78 | notes 13, 22; prose 38–40, 46–50, 478 | the roads converge "above the Scarfell's foot"; Harrow's End sits a day above it; "Two leagues off" |
| 79 | 27 | "over the lip... At Harrow's End" |

Ch 78's own references to Cotter's Cross (notes 14; prose 92, 124, 210) are **correct** on the Atlas: the Sun comes up the Way from the south. Leave them.

**Recommendation: fix the prose. Harrow's End and Cotter's Cross are pinned by Books 1–2.**

- Replace the northern "Cotter's Cross" with Teo's ford or the Ram's Head (54, 56, 59, 67).
- In 77–79, let the column climb out of the Vale *through* Harrow's End and the top field. The "lip" becomes the Scarfell's edge above the Fellwood, a day on.
- The reviewer's suggestion to cut the river at 78:64 is the wrong way round; see B3-78-a.

### 6. Coldtarn timing (B3-79-a, B3-79-b; also 85:324)

world.py puts Coldtarn at (196, 74). That is 24 leagues from Varrhold and about 35 from Harrow's End.

Book 3 itself treats Coldtarn as much closer:

- 79:309: Varrhold is "half a day" below it;
- 67 notes 13: "two hours' flying" from the hub;
- 80:277: "twenty leagues" from the Vale.

Books 1–2 agree with the closer placing:

- Book 1 ch 8:23: "Two days up into the Scarfell";
- Book 1 ch 8:51: "above the hold";
- Book 2 ch 43:438: "to the hold and past it, up to the caves above Coldtarn".

**Recommendation: move the Atlas data.** It is cheap and safe. Put Coldtarn about 4–5 leagues above Varrhold, for example at (188, 91), and shorten Hollow Beck's source to match. Books 1–2 and most of Book 3 fit better that way.

The prose still needs two changes:

- **79:** the lip to Coldtarn can't be done overnight by wagon. Fly the old and the hurt up in the Clan's baskets, with Tam's empty wagons coming after, or give the wagons a night and a day.
- **85:324:** "four leagues off" becomes "a long day's walk off" (about 15 leagues).

---

## Findings by ID

### B3_01-13

**[B3-07-a] CONFIRMED.** The Ysse can't be Hearthmere's border on the Atlas, and option (a) would break Books 1–2.
- Take option (b) only.
- **Also touch:** all of map 1. That means ch 7:378–400 (the knight-captain's scene and the scout on "the Hearthmere bank" must go, or be watched from the Wend post), ch 7:428, and 10:43 (Minor B3-10-b: Hallowmere is *west*).
- 11:375 needs no change: Dickon only met a courier at the Wend crossing.

**[B3-02-a] ADJUSTED.** Calder was at the caves, not at the river. But the proposed "the night before" puts the lights on night 3, and they first came on night 4 (ch 1:332; ch 2 notes 19).
- **Fix:** cut "He'd seen them from the river on the night the six went up. A glow." and write "From the moor, on the fourth night, they were more than a glow."

**[B3-02-b] CONFIRMED.** The lintel was held on day 3; Lisska came at dusk on day 4, and Orrun was lying in the road.
- The fix (pass the picture on as the lion's) is good.
- **Also touch:** ch 2 notes line 9 (the echo: "digging... beside three lions").

**[B3-04-a] CONFIRMED.** "Two days ago" can't be right: the descent was dawn of day 9, and the ride is about 100 leagues.
- Prefer the reviewer's second option. The rider was sent when the lights first came (about day 4). Cut "They came down two days ago" and "We saw them come down". The running west becomes "getting ready to run". Idony's glasses give the descent that dawn.
- That keeps chs 4–7's days as they are.

**[B3-06-a] CONFIRMED.** Wendmouth to Harrow's End is about 100 leagues.
- The fix is fine.
- **Also touch:** none. Ch 6 notes 19 has no figure.

**[B3-07-b] CONFIRMED.** The toll lasts four days (days 22 to 26).
- The second fix ("For a few days. It's coming back." / "Only that?") is the cheaper one.
- **Also touch:** ch 7 notes 8 and 21, and Chapter_Plan.md:393 ("for a day").

**[B3-08-a] CONFIRMED.** Moss contradicts himself: 8:130 "When they come down" against 8:224 "The clans are running west".
- The fix is fine.
- **Also touch:** ch 8 notes 15.

**[B3-10-a] CONFIRMED.** From the Ysse to Hallowmere is about 122 leagues in 3 days. Under 07-a(b), Crale's post is at the Greenwold's edge by the upper Wend, about 47 leagues from Hallowmere, so day 24 to day 27 then works.
- Crale must report from his outriders or a falcon, not from his own sighting. Drop "It looked at me" or give it to an outrider.
- **Also touch:** 10:137–141, and ch 10 notes 12 and 14.

**[B3-11-a] CONFIRMED.** Ch 4:144 already had six breaths on day 9.
- The fix is fine.
- **Also touch:** ch 11 notes 15 ("breathe in six now").

**[B3-11-b] ADJUSTED.** Dickon can't be Liss's grandson. But the proposed "Old Tolly" invents a person whose name is too close to the envoy Tolley (ch 1).
- **Fix:** 11:251 "A boy from the Staithe. Twelve."; 11:255 "Liss wrote it."
- **Also touch:** ch 11 notes 15 and 17, and Part1_Ledger.

**[B3-12-a] ADJUSTED.** Arn can read. The proposed "without reading it again" collides with the clause that follows, "and didn't ask anyone to read it again".
- **Fix:** "Arn signed without reading it, because he'd read it the night before, and didn't ask anyone to read it again."

**[B3-12-b] CONFIRMED.** Nothing explains Wren at Ironhythe.
- The fix (cut her from the line) is the cheapest.

### B3_14-27

**[B3-22-a] ADJUSTED.** The title does name a death, against the plan's own sentence (Chapter_Plan.md:570). But the same plan lists "Ulric's Pour" (line 168), and the chapter comes after the death.
- **Severity:** Major, author's call; not Critical.
- If it's renamed, "The Black Stone" isn't used anywhere in the three books.

**[B3-27-a] CONFIRMED.** By night 126 there are ten ships, not fourteen. "Ten days off" can't be seen.
- The fix is fine. B3-28-b is the same finding.

**[B3-27-b] ADJUSTED.** The 540 people and 600 gold are from after she sailed, so they're wrong. Maren could plausibly have heard about Ostrey's pilots and Hal's charts from Kit on the voyage, though ch 20:229 was said to Jory. The proposed "without a Merrin" is wrong: Jory is the fleet's requisitioned pilot.
- **Fix:** "Four hundred people and more, at five hundred gold a head... Sailing at night through the Shatters with pilots reading paper."

**[B3-25-a] CONFIRMED.** In her own POV Kit says "My father didn't [know why]", but her father told her the story (29:103).
- The interior line is a good fix.

**[B3-23-a] ADJUSTED.** The direction error is real (Book 1 ch 49:28: Hallowmere lies west of Greyhold), and the east and west gates contradict each other. But the reviewer's fix breaks ch 41: ch 41:12, 41:43–45 and the ledger have the sixty thousand from Hallowmere crossing at Liss's ferry, so "toward Greyhold" must stay. The King's Road south also runs into the Downs, where the Titan is.
- **Fix:** keep the destination and reverse the compass.
  - 62 and 448: "east toward Greyhold"; 76: the east gate; 334: "east"; 442: "east of the boiling Mere"; notes 22: "east".
  - The Titan comes from the south-east across the Downs, so Beacon Ridge (92) is "south-east of the city" across the Stillhaven arm of the King's Road. Columns leaving the east gate pass behind it to the north (122).
  - Notes 12: the Titan crosses the Wend below the Marches.
- The Downs extension in map 3 makes "Downs east of Hallowmere" hold as written.

**[B3-23-b] CONFIRMED.** Corsa to Hallowmere is more than 150 leagues in a day.
- The fix (day 99, cut 434's first sentence) is fine.
- **Also touch:** ch 23 notes 21 ("d.89").

**[B3-16-a] CONFIRMED.** The chart is 200 years old (3:188, 4:42), so it can't be older than the split.
- The fix is fine.
- **Also touch:** 12:290 (Minor B3-12-d).

**[B3-24-a] REJECTED.** The approved plan says the causeway "ran past the Drowned Bell's temple" (Chapter_Plan.md:419), and Q29 settled the d.104 pass as drafted. The drowned road isn't drawn in world.py, so nothing fixes its course. It can pass the reef off Gullhaven and be joined from Blackwater after the reef-maze. Ch 17's "home, to where it slept" (the Saltings) doesn't contradict it.
- The only real clash is in notes: ch 13 notes 16 has the reef-stone in Blackwater's channel falling "off the road's last standing pier near the Bell's temple", about 80 leagues off. Fix that note.

**[B3-22-b] CONFIRMED.** Calder had left the *Merry Agnes* on day 90, and Corsa to Blackwater is 36 leagues.
- The fix (Lisska leaves from Skarrow on day 94) works.
- **Also touch:** ch 22 notes 13 and Part2_Ledger (Lisska "on 92").

**[B3-26-a] ADJUSTED.** The double booking is real. But the proposed carrier "one of Arn's twenty" isn't possible: they arrive with Arn on day 117.
- **Fix:** "Calder had sent Kharrak to Varrhold with a letter on the hundred-and-twelfth." That works on time: Kharrak is back on the ledge by night 116.
- Keep the reviewer's change to Lisska's "after the first few stones".

**[B3-14-a] ADJUSTED.** Line 173 already explains the change of build ("He looked older. Heavier."), and missing earrings aren't a contradiction. Only the coat is wrong.
- **Fix:** 14:171 "A student in Greyhold blue." Also ch 13:333 (Minor B3-13-a).
- **Severity:** Minor.

### B3_28-43

**[B3-35-a] CONFIRMED.** The control relic is called "the seventh" (35:271, 36:45), and 36:111 runs the relic into the Unbound "seventh ring".
- The fixes are good.
- **Also touch:** ch 30:186, "And a seventh stone, over them all," which the reviewer missed. Change it to "And one stone more, over them all" (this echoes 35:269). Also ch 44 notes 16 (Minor B3-44-a).

**[B3-28-a] CONFIRMED.** Ten ships, but eleven are tallied as lost.
- The fix is fine.
- **Also touch:** ch 28 notes 19 ("nine of the eleven").

**[B3-28-b] CONFIRMED.** This duplicates B3-27-a. Apply one fix.

**[B3-38-a] CONFIRMED.** "Twenty in each basket" makes forty, not nine.
- Keep the nine and change 224.

**[B3-39-a] CONFIRMED.** All three dragons are at the hall on days 143–144.
- The fix is fine.
- **Also touch:** ch 39 notes 12 ("with the dragons awake around them") and Part3_Ledger:15.

**[B3-39-b] ADJUSTED.** Correct, and the separate lagoon road is the right fix. The reviewer left out three lines.
- 39:30: "Up the western road" must become "Up the northern road".
- Ch 39 notes 12 must match ("Jory back... on Aurveth with Calder").
- 37:28–38 needs Calder to go by the lagoon first.

**[B3-39-c] CONFIRMED.** Ch 40:35 and 40:111 have the lion at the lagoon at dusk 147 and into the sea at dusk 148.
- The fix is fine.

**[B3-40-a] CONFIRMED.** Going home the count should run up from One (32:32, 42:101–113).
- The fix is fine, including notes 16.

**[B3-41-a] ADJUSTED.** Line 49 is ambiguous rather than wrong: it can read "when the Titan had lain down and didn't get up". The proposed Antlered clause is wrong: the Antlered is about 100 leagues east, so "the oaks were too near it" makes no sense.
- **Fix:** "Tova had brought them out of the Greenwold on the hundred-and-twentieth, when it was plain the Titan wasn't getting up out of the Mere, and the oaks were too near it."
- **Severity:** Minor. 41:139's "ninety-fifth" can stay (ch 23 notes: days 94–95).

**[B3-42-a] CONFIRMED.** From Corsa the Wend is west; the flight passes east of the camp.
- The fixes are fine.

**[B3-42-b] CONFIRMED.** From Coldtarn the Mere is south-west, about 79 leagues off.
- The fix is fine.
- **Also touch:** 45:63, 237, 239 ("At the middle of everything") and 259 (Minor B3-45-c). This is part of the mirrored-map pass.

**[B3-43-a] CONFIRMED.** The coast was emptied on day 150, and Calder came home at dusk 149.
- The fixes are fine.
- **Also touch:** ch 43 notes 14. B3-45-a is the same finding.

### B3_44-56

**[B3-52-a] CONFIRMED (Check-level).** "As grass comes up out of a burned field" and "Not while one of them's left to take it" give in advance a mechanism for ch 86's creature. The plan says these creatures are never explained.
- The fix is minimal and right.
- Separately, 52:210's "three hundred years. Not since the six were laid down" mixes up the chaining (300 years ago) with the laying-down (at the split). Make it "Not in all the College's records."

**[B3-45-a] CONFIRMED.** This duplicates B3-43-a's second half.

**[B3-45-b] REJECTED.** Ch 45:323 itself says the lion "feels it... knows it's there. He can't see where." Ch 43:374 gives exactly that: a sense of a burning thing among the eggs, with no position. What only Aurveth has is the exact place, and ch 68 needs nothing more. No change is needed.

**[B3-46-a] ADJUSTED.** The two-day barge is impossible: the warrant arrives on day 192, and the run is about 225 leagues. The proposed fix contradicts itself: Lisska sets Idony "down at the camp on the way" on days 187–188, yet he comes "off the green one's neck" on day 196. Blackwater to Coldtarn also doesn't pass the camp.
- **Fix:** Idony rides Lisska from Blackwater to Coldtarn when she brings Jory home on day 187. He comes in with the three on day 196: 46:57–59 becomes "He came off the green one's neck before her wings were still."
- Ch 44:318–333 becomes a farewell on day 187, and the day-194 barge carries Nye, Corrie and the fish, arriving about day 204.
- Move Kit's second barge (46:417) to about day 212.
- **Also touch:** ch 44 notes 18.

**[B3-46-b] CONFIRMED.** A Lamp coming from the east and crossing from the east bank can't end up on the camp's (eastern) meadow. Orrun also comes up the "west bank" from Wendmouth, which is on the east bank.
- Either of the reviewer's fixes works. The second (no crossing; Saltreach-bank downs; it walks down the river on the light) is cheaper.

**[B3-49-a] CONFIRMED.** See map 3.
- The fix is fine for chs 49–53. Choose station names that lie on the line from the Thornwood to the camp, for example: the Wyldmarch border, Skarrow on the Scarfell's east side, and Varrhold's gate.
- 52:56 "Carried east" becomes "Carried out along the road".

**[B3-53-a] ADJUSTED.** The ferry-house problem is real; see map 4. But the camp-move distance needn't change. Ch 41:27's prose gives no figure ("below Greyhold's fallen hill"); only the notes and ledger say "three leagues below".
- Read the old camp as lying opposite Greyhold's hill, and keep "three leagues" at 53:419 and 55:26. Fix ch 41 notes 12 and Part3_Ledger:23 instead.
- Keep the reviewer's 53:371 and 53:377 changes and the "Or its twin" line for ch 57.

### B3_57-71

**[B3-58-a] ADJUSTED.** Correct, but the scope given is incomplete; see map 2.
- Add ch 76, the blocker: Kit must be near the mouth, or the sighting changes. Add chs 74–75's sightings of the mouth from the hub.
- Calder's daily flight can stay: Titan-class speed (49:52).
- The market can still be towed to the Staithe (8 leagues below the hub), if 58:474's "two days later" becomes about "ten days later". Ch 60 starts on day 295, so there is room.

**[B3-61-a] ADJUSTED.** Both errors are real:
- Calder was on the Scarfell on the night the six went up;
- the links came "out of the ash... the first night" (Book 2 ch 2:225), not "the morning after".

The reviewer's "envoys' table" is an invented label.
- **Fix:** 61:256 "Since the last night before he flew up to the caves, when everyone left Liss's table and he'd gone back in for his coat and found them there."
- 61:264: "the night of the raid".
- Add one line saying Maren took the bundle off Liss's table after Book 2 ch 2. No Book 2 scene shows her carrying it.

**[B3-63-a] ADJUSTED.** The Sun stands south-east: 64:239 says so, and the Saltreach side is east. Changing 63:131, 63:153, 64:79 and 64:169 is right.
- Leave 61:196 alone. Calder's contingency on day 316 ("if the Sun comes up the Sun Road side") was made while the Sun lay in the Sunward Hills, which are west. It's correct as written.
- For 64:79, say the code was agreed after the Sun came round, or change it to "Five for the south-east".

**[B3-68-a] CONFIRMED.** The Bell moves from a league below the line to the mouth with nothing to explain it.
- Use the first fix (one line saying it went back down in the night).
- Reject the "simpler alternative": the plan fixes the Lady holding the Bell *at the Wend's mouth* (Chapter_Plan.md:344; chs 74, 76).

**[B3-59-a] CONFIRMED.** Cotter's Cross is south of Harrow's End (Atlas.md:61; Book 1 ch 16:216; Book 2 ch 12:436).
- The Teo's ford fix is fine.
- **Also touch:** map 5's list (54:192; 56 notes 20 and prose 485; 67 notes 17).

**[B3-57-a] CONFIRMED.** This is the same issue as B3-53-a. Use the "Or its twin" fix once the move is set in ch 53.

### B3_72-86

**[B3-79-a] CONFIRMED.** Ch 78 makes Tam's wagons the tail; Tam is on the first box, then the last, then the first again.
- The fix is fine and fits 79-b.

**[B3-79-b] CONFIRMED.** The lip to Coldtarn overnight is impossible on the Atlas.
- See map 6. Move Coldtarn to about 4–5 leagues above Varrhold (cheap; agrees with Book 1 ch 8 and Book 3 79:309).
- Fly the wagons' old and hurt up in baskets.
- 85:324 becomes "a long day's walk off".

**[B3-78-a] ADJUSTED.** Harrow's End is misplaced (Atlas.md:8). But the proposed minimal fix, cutting the river at 78:64, would move Harrow's End *further* from canon. The Eelweir by the drained Wend is correct.
- **Fix:** keep Harrow's End on the Vale floor.
  - 78:38: the roads come together "at Harrow's End".
  - 77:76–80: the "Scarfell's foot" at dawn becomes the Vale's edge at Harrow's End; the "lip" becomes the Scarfell's edge above the Fellwood, a day on (as Book 2 ch 11 has it).
  - In ch 78, Kharrak holds until the last wagon is up past the top field into the Fellwood, rather than "over the lip". 78:478's "two leagues" then fits: the lion lies at the Vale end of the roads.
- Ch 78's Cotter's Cross lines are correct and stay.

**[B3-74-a] CONFIRMED.** The Sun has been up and on the Saltreach bank since 72:202–210, so "getting up" in "the shallows" is wrong. The Coil has gone back into the water near the gap and the eddy (73:482), not "north, in the channel".
- The fix is fine.

**[B3-81-a] CONFIRMED.** "When either dies, the other usually dies too. Exceptions are extremely rare" (Bestiary.md:19). Three casual survivals wear the rule down before 81:410 and 83:458. Ch 84:149's riderless dragon also breaks 83:44's "twenty... And twenty".
- The fixes are fine.

**[B3-82-a] ADJUSTED.** Keeping the door east is right (79:73; 84:221–229). But the glasses' triangle in 82:37 is broken: "toward the door" (east), "the hall's dark back" (west) and "against the western wall" (also west) give two glasses on the same side. The reviewer's 211 fix ("back glass and the western glass together") points west, not south. Their 391–393 fix ("East. Toward the door") would point the Last Titan the wrong way: it is coming from the Vale, to the south-west.
- **Fix:**
  - 82:37: "One against the southern wall."
  - 82:211: "South. Far. The south glass, and the door glass after it."
  - 82:391–393: "South. / Toward the south wall."
  - Notes 12 and Part7_Ledger:16: "door/east, back/west, south wall".

---

## Minor findings that should be Major

- **B3-10-b** (Greyhold to Hallowmere "north and east") and **B3-45-c** (Aurveth looking "east" and the wrong distance from Coldtarn): both are part of the mirrored-map error and belong in the same pass as 07-a and 42-b.
- **B3-54-d** (Cotter's Cross on the road north): systemic; see map 5. Its evidence is wrong, though. Harrow's End is 1.5 leagues from the *island*, not from Cotter's Cross, which is about 10.5 leagues away. The direction and the fix still stand.
- **B3-60-a** (fifty a barge, then "five hundred" on Kit's barge): a contradiction inside the chapter that any careful reader will see.
- **B3-13-a** and **B3-14-a**: one Gannet error with two IDs; fix both together (Greyhold blue, the day before the fair).

## Minor findings that are clearly wrong, or need changing

- **B3-54-d**: the distance in its evidence is wrong, as above. The finding itself stands.
- **B3-41-a**, filed as Major: the proposed Antlered fix is wrong (see above).

## Extra issues found during verification

- Ch 30:186: "a seventh stone" for the control relic (add to 35-a).
- Ch 52:210: "three hundred years... since the six were laid down" (see 52-a).
- Ch 13 notes 16: the reef-stone falls "near the Bell's temple" (see 24-a).
- Ch 82:37: the glasses' triangle is broken (see 82-a).
- Ch 40:27 and 45:353: Gannet "half running" behind a lion with half-league strides for a day. This bears on Minor B3-45-d's scale point.
