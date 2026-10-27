# Verification: Book 1 findings (Critical and Major)

Scope: every Critical and Major finding in `findings/B1_*.md`. None of the six files has any Critical findings, so this covers the 22 Major ones. I re-read every cited chapter line, the canon files and the Atlas coordinates (`Tools/atlas/world.py`, `marches_items.py`: x runs west to east, y runs north to south, one unit is about one league).

Tally: **CONFIRMED 9 · ADJUSTED 10 · REJECTED 3**

---

## B1_01-15

### [B1-05-a] Rowan's reply confirms an Ashford licence in under an hour
- **Verdict:** ADJUSTED
- **Reason:** The problem is real. Ashford is 24 leagues from Greyhold by road (Atlas:32), so no answer from its magistrate can come back while Kesh is away. The proposed wording has its own timing slip, though. The licence is "dated three days ago" (5:129), so Greyhold can't have received the magistrate's copy "three days ago": a copy needs about 1.5 days on horseback to cover 24 leagues.
- **Corrected fix (5:217):** "The licence is genuine. Greyhold had the magistrate's copy yesterday, under his seal, issued at the request of the Millbrook carriers' guild, and the men holding it are guild road wardens. We're to let them be."
- **Other places:** None. "Carriers' guild" and "road wardens" appear only here. *Check, not part of the fix:* the roadblock is a league short of Northwatch (Northwatch is at y 91 and Greyhold at y 106.6), so Kesh's round trip is about 29 leagues in "most of an hour" plus the drovers' talk. That is fast even for a falcon. If it matters, change 5:139 to "most of two hours".

### [B1-14-a] Teo's own men never arrive, then turn up at dusk
- **Verdict:** ADJUSTED
- **Reason:** The mismatch is mostly between the notes and the prose. The notes say Teo's six would follow "at mid-morning" (14:11), but the ford is empty at an hour before noon (14:48). The prose never says where his six were, and Teo had set "six on each side" (10:128), so a reader may wonder. The proposed line has two problems. "Found the ford empty but for the dead" is wrong, because Calder and Hob are still sitting with the body. And "brought Teo up to the hold at dusk" can't work as an arrival time: Varrhold is six leagues up the Way, and the men are carrying a hurdle.
- **Corrected fix:** In notes line 11, change it to "His six were told noon." In prose line 248, change it to: "His own six came down from the hold in the afternoon, at the hour he'd given them, too late. They took him up the Way at dusk on a hurdle, walking beside it, with his bay behind and the reins over the saddle." Line 230 ("somebody from the hold would come for him") already sets this up.
- **Other places:** Ch 14 draft notes, line 10 ("They wait with the body until Teo's men come") already agree with the fix.

---

## B1_16-26

### [B1-17-a] Maren watches Harrow's End burn from the west shore, which faces Hearthmere
- **Verdict:** ADJUSTED
- **Reason:** The geography is confirmed. The island sits at x 175–176.5, Redwatch on the Hearthmere bank at x 174.3, and Harrow's End and the mill at x 177.1–177.7. The skiff is hidden in the west channel (15:110), and the lion's stream and the old bridge are on the west shore (19:59, 21:60). So the mill fire lies behind her, across the wooded island. The fix is correct in kind, but it covers too few lines. The ch 19 encounter is set on the west shore, so the minimal fix keeps her there and turns every "far bank opposite" view into a glow over the trees.
- **Other places the fix must touch:**
  - **Ch 17:** line 277 (cut "Figures. Small, black, many, running in the light. Horses."; the shouting and the horn can stay faint); line 283 (cut "she could see the whole far bank lit up as if by day: the village, the lanes, the green… people running across it"; the jet of fire in the sky can stay, since it's high enough to be seen over the oaks); line 289 ("watched the dragons burn the far bank" becomes "watched the sky over the trees"). Line 273 can stay if it becomes "the sky to the east was on fire".
  - **Ch 19:** line 29 (the mill as "a single great torch… its wheel standing black" can't be seen through a wooded island; make it the glow and the fire on the hill above it); line 41 ("the fire across the water crackling" can't be heard over the island; cut it); lines 61–62 (the lion goes to the west shore, so "Toward the fire" is wrong; keep "Toward the water. Toward her."); line 91; line 107 ("across the river and up the far bank" becomes "out over the island and the river"); line 209 and line 221 ("light from the far bank" and "the fire on the far bank" become the glow over the trees).
  - **Notes:** 17:16; 19:11 ("toward the sound and the fire") and 19:12 ("glow off the far bank").

### [B1-21-a] Rook "crosses the water" from the Eelweir, which is already on the farmer's bank
- **Verdict:** CONFIRMED
- **Reason:** The Eelweir is Harrow's End's landing on the Saltreach bank (Atlas item `eelweir`, x 176.6; Characters.md:147), and the farmer's field is above it, so Rook has no water to cross. Maren's "gone across the river" (21:168) is fine because she is on the island. The Captain's "Swim" (21:152) is also fine, because it is said on the island.
- **Other places:** Ch 21 notes line 14 ("went across the river late that morning") should become "went off after the farmer". Bible/Characters.md:187 ("crossed to the farmer once word of the bonds reached the far bank") should become "went after the farmer once word of the bonds reached the Eelweir".

### [B1-26-a] The ferry gossip knows what Maren said only to Rowan
- **Verdict:** ADJUSTED (and it reads more like a Minor)
- **Reason:** A1 C6 deliberately made Rue's "like robbing it" the channel through which Calder learns Maren's reason. APPLIED_21-40:56 kept Rue's echo because it adds new facts (the stables, "a hay wain"), and chs 26:270, 34:275 and 36:434 all depend on "*Like robbing it,* Rue had said." The leak of the reason is therefore a settled choice. What's left is the itemised list of three attacks (shore, stream, tower), which only Rowan heard (23:358). DECISIONS.md:32 asks for a distortion in exactly this kind of echo.
- **Corrected fix:** Keep line 96 as it is, or drop "to her way of thinking" if you want it looser. At line 84, use the reviewer's distortion: "…it went for her a dozen times, and she never once struck it back. Had a sword, Weir's boy says, and never used it…"
- **Other places:** **26:106** "Three times. And she'd stood there with a sword in her hand and never struck it back." The reviewer missed this one. It must become "A dozen times, Rue said. And she'd stood there…" Also ch 26 notes line 15 ("three times").

### [B1-24-a] Sigrun is called "Ulric's champion", but Ulric is the champion
- **Verdict:** CONFIRMED
- **Reason:** Ch 8 notes line 9 says "the chief's brother (the Clan's champion)". Ch 8:73 has "The champion pours". Ch 16:202 says Sigrun is war-leader and follows "the champion". Characters.md:177 calls her a war-leader. Grepping "champion" turns up no other uses in Book 1.
- **Other places:** Ch 24 notes line 13 ("the champion's place" becomes "the war-leader's place"). Nothing else.

---

## B1_27-38

### [B1-32-a] Ch 32's internal day count gets Calder to Wendmouth on day 51, not 49
- **Verdict:** ADJUSTED
- **Reason:** The arithmetic is confirmed. The night after a burning belongs to the next day (compare the mill night 8, then dawn on day 9 in ch 21), so his night at home is night 43, and as written the prose lands him in Wendmouth on day 51. The fix also squares 33:25 ("three days after Holloway burned" gives day 49 only if Holloway burned on night 46) and 35:67. But it leaves one more ordinal unchanged.
- **Other places the fix must touch:** **32:82** "By the second morning there were two great wooden machines". Under the fix that is day 45, the same morning as the parley, and it clashes with the notes, which put the machines on day 44. Change it to "By evening there were two great wooden machines". Also update ch 32 notes lines 12 and 14 and Decisions_Ch31-40.md:10 and :12, as the reviewer says.

### [B1-31-a] Tam couldn't have walked from Millbrook in time to see the dragons arrive
- **Verdict:** CONFIRMED
- **Reason:** Millbrook is at (173.9, 108.7). The bank opposite Harrow's End is near (174.5, 103), about 5.7 leagues away in a straight line and more by road. That is five hours or more on foot. The dragons arrive in the middle of the night (30:35), and the roof rescue comes early (30:127–137), so Tam couldn't have seen it. Redwatch is opposite the island, about a league above that bank (Ruling 7), so the fix works. No other text has Millbrook men walking up.
- **Other places:** Ch 31 notes line 13 ("with the Millbrook men who walked up to watch") becomes "with Millbrook men who were at Redwatch that night".

### [B1-38-a] Aurveth points out a milestone she can't see
- **Verdict:** CONFIRMED
- **Reason:** Under World.md:23 and Ruling 1, live sight isn't shared unless it is pushed on purpose, and the push goes from the one who sees. Calder took the stone for a gatepost, so he had nothing to push. The proposed "I know this place" fits Aurveth, who walked the Oneroad with her first partner (Decisions_Ch31-40.md:80), and fits her slow voice.
- **Other places:** None.

### [B1-33-a] The Callis plant doesn't fit the ride it implies, and sits in the wrong place
- **Verdict:** ADJUSTED
- **Reason:** This is the A1 M6 plant, and it doesn't hold up. The rider "came along the bank at dusk" and "stopped at every post" from Redwatch to Millbrook, about five leagues (33:211). Callis is back at Ferriby, a league inland, "when the lamps were lit". The line also interrupts the moment at 33:57–61. The reviewer's version has two problems of its own. It still has the rider at the tower "at dusk", which leaves Callis about half an hour to ride a league inland and be at Ferriby for lamp-light. And it adds a second rider network that nothing else uses.
- **Corrected fix (smaller):** Use A1 M6's own alternative. Cut 33:59 entirely. In 71:165, Tobin says: "The friend. With the seal. The one whose paper cleared the river for the barges, and whose men rode it." Leave Ottery's account (33:211) as it is. Callis as the seal-*holder* (Characters.md:124, "the seal-carrier") still stands.
- **Other places:** Characters.md:124 could say "seal-holder" instead of "seal-carrier", but it doesn't have to.

---

## B1_39-52

### [B1-45-a] Is the farmer on the paper or not?
- **Verdict:** ADJUSTED
- **Reason:** Confirmed. Ch 45:153 says "Not on the paper", but 46:49–51 quotes the printed smaller part, and 47:202, 48:51, 49:200, 50:374 and 59:200 all treat it as printed. The reviewer's fix has two faults. It puts the smaller part *above* "One again", while 46:49 has it "at the bottom, under the two words". And by changing line 153 to "At the bottom" it would make the island girl part of the print too, but 46:51 prints only the farmer. 45:39 ("She didn't take in all of it") already explains why Maren missed the bottom part at dawn.
- **Corrected fix:** At 45:57, change it to: "At the bottom, two words. *One again.* Under them something smaller, that she didn't read." At 45:153, change it to: "There's more," he said. "At the bottom. Something you've all heard of." Before the island part (45:159), add: "And something that isn't on the paper," said Reede. "Something I've seen." Ch 45's notes (line 18) list the girl among the paper's claims; trim that to the farmer only.
- **Other places:** None. Ada's and Liss's "put your/his name" (46:199, 47:202) can stay as loose talk.

### [B1-46-a] Ada sings the verse on night 89, but the lights go out on night 90
- **Verdict:** ADJUSTED
- **Reason:** Confirmed. Ch 46 runs from noon on day 89 (line 31) through dusk and supper to the verse with no break in time, and 47:20 and Story.md:174 put the lamps on night 90. The reviewer's "By the next dark" works, but it clashes with ch 46 notes line 11 ("By nightfall [day 89] every house… has heard it"). A cleaner place for the skip is the supper.
- **Corrected fix:** Keep line 57. At line 65, change it to: "'Calder,' said Bel, at supper the next night. She hadn't looked at him all day."
- **Other places:** None.

### [B1-43-a] Maren's "first lie" comes after she has already lied to Ottery
- **Verdict:** CONFIRMED
- **Reason:** 41:209 and 41:255 are plain lies to a river-watch sergeant and a boy, and 51:69 calls one of them back. "She'd never lied to the orders in her life" can't sit straight after that. The proposed fix is acceptable.
- **Other places:** None. (Arguably this is Minor.)

---

## B1_53-65

### [B1-56-a] Lisska reports the touch at dawn as if it were new
- **Verdict:** REJECTED
- **Reason:** The chapter's own sight rule explains the timing. At night, two leagues off and in rain, Lisska "can't see faces from there in the dark… only shapes" (56 notes line 11; prose around line 157). After the touch the lantern goes out (55:226). A hand in a mane is a detail she can make out only in grey light, and Maren is still asleep with her hand there at dawn (55:234). Lisska's "She's put her hand on it" is her seeing the touch at first light. It reads as a discovery, and it is the better beat for Calder. The notes block placing the touch earlier is a plan-against-prose difference, and the chapter is canon. Reviewer finding B1-56-c, in the same file, makes the same visibility point. Optional half-line: "*I can see now. She's put her hand on it.*"
- **Other places:** None.

### [B1-56-b] Wren is promised Lisska's reports directly
- **Verdict:** ADJUSTED
- **Reason:** The canon breach is confirmed (Bestiary.md:44; Rulings 5 and 13; 64:112 has it right). The reviewer's main fix is awkward ("send it down with Lisska's eyes") and still has a dragon reporting to a child. Calder does come down again later (Ada and Fisk's paper, ch 62), so the simplest fix routes the reports through him.
- **Corrected fix (56:379–385):** "And you'll tell me about the lion-woman?" / He looked up at the crag. *Will you watch her?* / *Yes,* said Lisska. *Every night. Everything I see.* A pause. *She'll make you say it twice.* / "Yes," he said to Wren. "When I come down. Everything. Twice."
- **Other places:** Ch 56 notes line 18 already says "Lisska does [tell him]". It's fine.

### [B1-58-a] On day 126 the tents are already "over the hills behind Harrow's End"
- **Verdict:** CONFIRMED
- **Reason:** It clashes with 62:153–161 (day 133: the first company is "Far. The other side of the moor"), with 63:296 and with 65:291 (the first fires behind Harrow's End on dusk 139). The black road itself, which is the subject of 58:262 (Atlas `road54`), can stay. Only the tents move back.
- **Other places:** None.

### [B1-54-a] "Eleven" dead, but the tally given lists eight
- **Verdict:** CONFIRMED
- **Reason:** 1 + 5 + 2 = 8 men, and the dogs are counted separately. Brask is taken alive (54:12, 192). Adding three spearmen keeps "eleven" in 54:94, 54:380, 56:241 and the notes. The other option is to change all four to "eight".
- **Other places:** None beyond those already listed.

### [B1-64-a] Calder has "never stood this close" to Greyhold
- **Verdict:** CONFIRMED
- **Reason:** 64:68 says he has been to the Staithe "a hundred times", and Ruling 18 puts the Staithe directly across from Greyhold. The fix is minimal and in voice.
- **Other places:** None.

### [B1-59-a] Rowan has "known since the night of the lamps"
- **Verdict:** REJECTED
- **Reason:** The finding misses 47:118. On the night of the lamps Maren "knew it was true, all of it, every word on the paper… from a black door… from Hale's face… from twenty-nine beasts". Hale's confession on night 96 only confirmed what she already knew. Rowan's "for a month" is about Hale's guilty looks, not about when Rowan herself knew. The line holds.
- **Other places:** None.

---

## B1_66-79

### [B1-72-a] Lisska at Hollin Knowe is inside word range, but Calder feels "nothing"
- **Verdict:** ADJUSTED
- **Reason:** Confirmed against World.md:24 (feeling "carries much further"), Ruling 16 and 17 (Lisska at the Brackenwood edge, two leagues west of the river) and 70:338 (feeling still there past four leagues). "Nothing" breaks the canon. The reviewer's fix has Calder order her to "stay hidden". That changes Ruling 16's settled reason ("too frightened to go down"), and it makes the plot hole worse: once they speak, Calder could simply ask her what she sees on the knowe. World.md:23 allows a partner to keep a thought to herself, so her silence can be her own.
- **Corrected fix (72:37):** "Not a fire through a wall now. A spark, far off and west, small and frightened, and no words in it. She'd gone where he sent her, and she didn't speak. He felt the space she'd left, cold, where she always was, at the edge of everything, chattering." Leave 73:285 as it is ("She's sorry. She says it over and over."), which now pays this off.
- **Other places:** 76:287 ("going further and further until it was nearly nothing") still works. No other changes.

### [B1-76-a] Corvin escapes from the centre of a dropping disc
- **Verdict:** CONFIRMED
- **Reason:** 76:45 and 76:111 put him kneeling on the central boss, with Calder's hand on his wrist. 74:150 makes the disc "as wide as a threshing floor", and 76:123 has it drop whole. 76:241 then says "a step from the edge", which contradicts all of that. The beat the reviewer proposes is needed. It is worth adding half a clause so that Calder's not following him makes sense, for example "…and Calder, held by the grinding in the stone, couldn't get up off his knees to follow."
- **Other places:** Ch 76 notes, if they describe Corvin's escape. Nothing else in the prose.

### [B1-71-a] Check: the barricade ward works across a street, against touch range
- **Verdict:** REJECTED
- **Reason:** The finding misses a canon line. Magic.md:244 lists **many-voice workings** whose reach goes well past touch range: "a ward over a whole wall, a fog over a river, the noon oath". Magic.md:295 also puts the **surge** on nights 142–143 ("charms take too hard, wards blaze"), and this is night 142. A hundred voices turning a single stand-word aside down one village street fits that canon. As for the geography, 71:29 has the knights "coming down at" the barricades along the River Road, and 71:33 has them checking at the bottom of the street. That is the same approach seen from two points, not a muddle.
- **Other places:** None.

---

## Minor findings

### Minor findings that may be Major (worth verifying)
- **B1-59-c** (pre-dawn crossings on days 124 and 125 straight after the hedge-meeting): if the walking distances are right, this is a logistics break a careful reader would hit, which makes it Major.
- **B1-14-b** (Ulric comes over the near rise and then rides "up the Way toward the hold"): if Ulric was living at Varrhold, his approach and his retreat both run backwards in the chapter that starts the war, which makes it Major.
- **B1-68-a** (the twins' plan to take the gate on day 142 against Callis opening it on night 143): this is a plot-logic gap in the climax, more than a slip.
- **B1-67-a** (Maren on the knowe "in the first grey" minutes after leaving the island): it is tied to the hand-off between 65, 66 and 67, which the reader sees from both POVs.

### Minor findings that are clearly wrong
- **B1-53-a:** 53:55 itself defines "since the trial" as "Since the long bare room at the top of the north tower… Rowan writing something in the margin". That *is* the ch 23 report. There's no slip.
- **B1-26-c** is not wrong, but it is cosmetic. Filenames often drop a "?", so only the plan row really needs to be made to match the heading.
