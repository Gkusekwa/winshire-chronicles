# Chapter-end maps, Books 2 and 3: notes

Built with `Tools/atlas` (`python3 build.py --book 2|3 --out DIR`). Book 1's outputs were unchanged by this work: a full default rebuild matched the 87 checksums taken before any edit (79 chapter pages, front matter, the realm and Marches maps, `Atlas.md`, the atlas page).

Coordinates are leagues, x east and y south, as in `world.py`. The places below were positioned for the maps because nothing in `world.py` or the Bible fixed them. The author settled them as drawn (Oct 2026).

## Places positioned for the maps *(settled as drawn, Oct 2026)*

### Series-wide (in `world.py`)

- **The Glasswater's outflow** (`RIVERS`): a stream from the lake's south end (151, 47) down a valley to the Wend at Wendhead (176, 63). Book 2's meltflood comes down "the valley that heads the Wend". Every book's maps draw it (see the contradictions below).

### Book 2 (`book2_items.py`)

- **Where the island was** (175.8, 103.5): the eddy left where the Old Ruin's island stood. Same point as the island, so the river bend matches.
- **Coldrun Locks** (92, 38): the lock-town at the head of Kessmoor's canals, on the Coldrun upstream of Ironhythe (ch 42).
- **Orrin's ruins** (93.6, 65.4): the north end of the old town, just outside the Scald's cordon, a little north of the Temple of the Scald (ch 45, 51).
- **Wendhead, Cray's Ford, Lowfold, Brookend, Sallow Lock** (171.6, 61), (176, 64.6), (176.6, 66.9), (175.4, 76), (174.9, 84): the upper-Wend villages of the ch 43 flood, in the prose's downstream order, on the river's line and on the bank each chapter names.
- **The Scarfell's edge** (186.4, 97.3): where Maren's drove track tops the escarpment, three leagues south-east of Varrhold (ch 11). See contradictions.
- **Greyhold, fallen** (174, 106.6): Greyhold's own point. From ch 85 it replaces Greyhold on both maps.
- **The hatching caves** (189.6, 89.9): on Coldtarn's eastern rim, in every book. See contradictions.
- **The Antlered rising** (252.5, 78.6): the Thornwood's edge just north of the Moot. See contradictions.
- **The Titan on the Sunward Hills** (50.5, 166.5): on the ridge above Solenne's palace.
- **The Drowned Bell** (217.5, 202.6): two leagues east-south-east of the end of Gullhaven's spit. See contradictions.
- **The Titan's road** (dotted track, 17 legs plus the five converging in ch 88): drawn from each chapter's place names, between world.py positions.

### Book 3 (`book3_items.py`)

- **The Greenwold road and its ford** (177, 84): the old road east from Hallowmere through the Greenwold's oaks, meeting the upper Wend under the last of the trees (ch 10–11). It is on the river itself, two leagues east of Book 2's Sallow Lock.
- **Sallow Bar** (201, 201.6): the toll-gate town where the Coast Road crosses a tidal creek, between Wendmouth and Gullhaven (ch 6).
- **The Ysse fords** (256.4, 128.2): drove fords on the Ysse below the lake, where the Plains meet Saltreach's scrub (ch 7).
- **Beacon Ridge** (136.5, 118.5): the last chalk ridge south-east of Hallowmere, across the Stillhaven arm of the King's Road (ch 23).
- **The Vintner's Gate** (87.5, 112.8): where the Sun Road leaves the Sunward Hills for Hallowmere (ch 53).
- **Redshank** (219.4, 197): stilt huts at the Saltings' western edge, where Orrun comes ashore (ch 43).
- **Eskby, Otterholt, Trimley** (175.2, 92.4), (178, 89.6), (175, 87.2): the upper-Wend villages of the black ice (ch 56). Eskby sits about twelve leagues above the hub, as the text says.
- **The Sheepford** (175, 112): the drovers' ford eight leagues below the hub, where the barges load (ch 58, 60).
- **The Accord's camp** (177.8, 109.4): three leagues below Greyhold's fallen hill on the Saltreach bank (ch 41). From ch 53 it is the camp at the eddy, six leagues upriver, as ch 53 says.
- **Liss's new ferry house and rope** (174.85, 103.05): at the eddy on the Hearthmere bank, from ch 53. The old house at Greyhold's jetty is drawn until then.
- **The ramparts** (172.6–175.15 and 176.55–179.4, y ≈ 104.3): a league of wall on each bank across the Vale's floor (ch 53).
- **The Ferry Flat, the jibs and the Bridle** (175.0, 103.65): the water-meadow at the eddy's edge (ch 55, 62).
- **The Kingfisher Shallows** (175.75, 105.4): gravel flats a league below the eddy (ch 68).
- **The five at the line** (ch 63): the Last Titan two leagues west of the Hearthmere wall's end; the Coil a league above the line; the Bell two leagues below; the Furnace on the downs toward the western end; the Horned Sun a league south of the Saltreach wall's east end. All from the ch 63 distances.
- **The hall under Coldtarn** (186.5, 91.5): under the crag on the tarn's western side, across the bowl from the caves (ch 54, 59).
- **Where Lisska, Aurveth, Orrun, Kharrak and the others died**: on the tarn, across Hollow Beck's mouth, at the door, and on the Fenn top field, each as its chapter describes.
- **Varrhold, under the slip** (184.4, 94.8): Varrhold's own point. From ch 85 it replaces Varrhold on both maps.
- **The drowned road and the far shore (the Lit Shore)**: all off the edge of Winshire. Nothing in `world.py` or `World.md` placed them, so they were positioned here, and are settled as drawn:
  - The road runs south-west from the Drowned Bell's reef (217.5, 202.6). Milestone 41 ("two days out of Blackwater") is at (211, 209), with one pier every 2.2 leagues on bearing (−0.72, 0.69), so milestone 1 lands at (147.5, 269.9), about 90 leagues off the coast.
  - The city on the sand (144.6, 272.7) sits at the landfall, behind a shelf about three leagues out. The Needle is the gap by the last pier.
  - The Grey Mother's hill (136.7, 280.3) is two days up the paved road.
  - The Hall of Light (133.5, 289) is where the road crosses the ridge.
  - The crossroads (130.5, 296) is half a day inland of the south bay (131.6, 302).
  - The coast runs north-west to south-east through the city, then turns west at the south bay.
  - The far coast appears from ch 25, when the Kittiwake first raises it. The label "The Lit Shore" appears from ch 27.

## Contradictions, and how they were settled *(Oct 2026)*

Each was settled for every book, and `Bible/World.md` records the ruling. Book 1's maps and `Bible/Atlas.md` were rebuilt where the ruling changes them.

- **Glasswater's outflow.** It is canon in every book: the lake drains south through the Iron Fells to the upper Wend at Wendhead, "the valley that heads the Wend". It is in `world.py`'s `RIVERS`, so Book 1's maps draw it too.
- **The hatching caves.** Book 1's prose says "above Coldtarn", which fits Books 2 and 3. Every book's maps now put them on Coldtarn's eastern rim (189.6, 89.9); Book 1's item moved there from (194, 76).
- **Kethra's Moot, Lake Ysse and the Hollow Ring.** Lake Ysse moved to the Thornwood's southern edge (254, 86), with the Ysse running through it, and the Moot sits on its north shore (252, 81.4) with the forest a league behind and the Plains in front, as Book 2 chs 22–27 and Book 3 ch 7 describe. The Hollow Ring moved to (260, 66), deep in the Thornwood and two days' walk north of the Moot (Book 2 ch 22). The Antlered rose at the forest's edge just north of the Moot.
- **The Scarfell's edge.** Not a contradiction: the edge is the escarpment along the Fellwood's northern side. The Way tops it above Teo's ford, eight to ten leagues by road from Harrow's End; Maren's drove track tops it three leagues south-east of Varrhold (Book 2 ch 11).
- **The Drowned Bell.** The prose is consistent: two leagues off the end of Gullhaven's spit, east-south-east. The spit is now part of `world.py`'s coastline, and the reef and the temple point are at (217.5, 202.6). The far-off "Bell Reef" island is gone. Book 3's drowned road starts there.
- **The Sunward Hills.** They now run from Highcrest's vineyards down the Sun Road to the ridge above Solenne's palace, as Book 2 has them.
- **The Fellwood.** Book 2 ch 26 now turns the elk cow north along the Fenn top wall into the Fellwood, which lies east of the village and above it, as in Book 1.
- **Teo's ford.** Not a contradiction: the prose gives road distances, and the maps measure straight lines. The Way winds up Hollow Beck, so road distances run about a third longer.
- **The Vael Pass road.** It now goes round Glasswater's western shore.
- **The catacombs.** Book 1 shows "the catacombs (below)" under Greyhold. Book 2 keeps the label. Book 3 drops it, because the cavern fell in with the hill at Book 2 ch 85.
- **Varrhold.** It is drawn until Book 3 ch 84. From ch 85, "Varrhold, under the slip" replaces it.
- **The far shore** lies off Winshire's map. Those close-ups run past the edge (`free`). On the Winshire map those chapters get an arrow at the bottom edge instead of a box, and the far coast isn't drawn before ch 25.

## How the pages work

- **The Winshire map** shows only what is known by the chapter's end. Kingdoms, places, roads and labels appear from the chapter that names them. Secret places (temples, the Hollow Ring, the Undercroft, the Drowned Bell) appear only from the chapter that reveals them.
- **The Titans' roads** are drawn as a heavy dotted track. A traveller's journey is a dashed route with an arrowhead. A route stays until that traveller's next journey appears.
- **Events fade.** Battles, sightings and the like leave the map eight chapters after they happen in Book 3, ten in Book 2. Deaths, houses, walls, roads and the Titans' roads stay. Anything new this chapter is ringed.
- **The close-up** has its own scale:
  - Marches scale (30 px a league, the Book 1 Marches map moved to the chapter's centre) for the Marches;
  - the Vale (45 px a league) for the battle at the eddy;
  - 20–24 px for a town;
  - 12 for a district;
  - 5–7 for a kingdom or the sea.

  It slides inward from the map's edge when its centre is near one. The far-shore chapters are the exception.
- **"New on the map"** lists the chapter's new places, labels and marked events, up to 16.

## Chapter by chapter

Each line gives the close-up's centre and scale, then what's new. "Slid" means the centre moved inward so the close-up stays on the map.

### Book Two

- **Front matter**: ends at Before the story begins. Close-up on (179, 104), Marches scale, 30 px/league. New: front-matter page, everything known when the book opens.
- **01 The Reeds**: ends at The reeds below Redwatch. Close-up on (175, 104), Marches scale, 30 px/league. New: The reeds below Redwatch; Rowan's knights; The Restoration's army breaks up.
- **02 The Ferry House**: ends at Liss's ferry house, Greyhold landing. Close-up on (174.3, 106.8), Marches scale, 30 px/league. New: Liss's ferry house.
- **03 The Glasses**: ends at Vael, the Long Library. Close-up on (151.5, 37), 20 px/league. New: Vael; The Long Library; The Gallery of Glasses.
- **04 The Black Book**: ends at Greyhold; the cavern. Close-up on (174.3, 106), Marches scale, 30 px/league. New: Greyhold's dead; Cassian's body on the gate; The held breath.
- **05 The Herald**: ends at Greyhold landing. Close-up on (174.3, 106.8), Marches scale, 30 px/league. New: The herald's proclamation; Aurveth swims the Wend.
- **06 Sour Water**: ends at Greyhold; the Wend at night. Close-up on (174.6, 106.4), Marches scale, 30 px/league. New: Millbrook's sweet well, sour; The granary wall opened.
- **07 The Drover's Way**: ends at The Drover's Way; Ewe Hollow. Close-up on (179.5, 103.5), Marches scale, 30 px/league. New: Calder's walk up the Way; Deserters turned at Ewe Hollow; The Ram's Head, sacked.
- **08 Second Ring**: ends at Vael; the road to the Wyldmarch. Close-up on (192, 45), 7 px/league, slid to (192.0, 73.7) to stay on the map. New: The Thornwood; The Wardens' road; The Council of Colleges.
- **09 The Titan's Road**: ends at The Fellwood, Saltreach bank. Close-up on (181.5, 101.5), Marches scale, 30 px/league. New: The Last Titan's road; Maren's road north; The Titan's swath; Two deserters killed.
- **10 Arn's Yard**: ends at Varrhold. Close-up on (184.4, 95.5), Marches scale, 30 px/league. New: The setters' ledge.
- **11 The Scarfell's Edge**: ends at The Scarfell's edge. Close-up on (185.6, 97), Marches scale, 30 px/league. New: The Scarfell's edge; The Fenns handed to the ledges.
- **12 The Empty Chair**: ends at The Drover's Way south. Close-up on (181.5, 104.5), Marches scale, 30 px/league. New: Calder flies south; Corvin's muster.
- **13 The Thornwood**: ends at The Thornwood. Close-up on (252, 62), 12 px/league. New: The Worldsend; The Hallow Plains; The Last Titan's road; Maren's road east; The Lions' Barrows; The Hollow Ring; The Titan on the stones.
- **14 Cotter's Cross**: ends at Cotter's Cross. Close-up on (180.5, 112), Marches scale, 30 px/league. New: The Candle Downs; Ten thousand for the lion; Kharrak's gully.
- **15 The Hallow Plains**: ends at The Hallow Plains. Close-up on (246, 84), 12 px/league. New: The Speaking Stones; Sleepwood groves burned; Rowan's chain.
- **16 Sleepwood**: ends at The Hollow Ring. Close-up on (260, 67), 20 px/league. New: The grey; The Wardens' rise; The knights' stakes.
- **17 The Ledger**: ends at Varrhold; the hatching caves. Close-up on (186.5, 93), Marches scale, 30 px/league. New: Rook's ledger read.
- **18 The Hollow Ring**: ends at The Hollow Ring. Close-up on (260, 67), 20 px/league. New: The finding-knot.
- **19 Skarrow**: ends at Skarrow. Close-up on (188.5, 96), Marches scale, 30 px/league. New: Two steadings burned.
- **20 Midsummer Night**: ends at The Hollow Ring. Close-up on (260, 67), 20 px/league. New: The Hollow Ring; It flew west; The capture; The Ring falls in.
- **21 The Roosts**: ends at The Roosts. Close-up on (185.8, 93.5), Marches scale, 30 px/league. New: Corvin's raid on the Roosts; Where Tor and Skell died; Four young dragons taken.
- **22 The Surge**: ends at Lake Ysse. Close-up on (254, 84), 12 px/league. New: Kethra's Moot; To the Moot; The clans gather at the Moot.
- **23 Under the Stones**: ends at Under the Hollow Ring. Close-up on (260, 67), 20 px/league. New: Six sleepers carved.
- **24 The Black Tarn**: ends at Coldtarn. Close-up on (187, 92.5), Marches scale, 30 px/league. New: Tor Brecc's pyre.
- **25 The Moot**: ends at Kethra's Moot, Lake Ysse. Close-up on (252.5, 81.5), 20 px/league. New: The Antlered rose; The lanes held; Where Hesper and Hush died.
- **26 Westward**: ends at Harrow's End, the Fenn top field. Close-up on (179, 101.5), Marches scale, 30 px/league. New: The elk herd turned; The Fenn top field.
- **27 The Drain**: ends at The Wyldmarch, riding west. Close-up on (210, 82), 5.5 px/league, slid to (210.0, 97.1) to stay on the map. New: The Last Titan's road; Idony rides west; The Wyldmarch gone dead.
- **28 The Tusker Road**: ends at Vael's gate, under the High Crown. Close-up on (165, 36), 12 px/league, slid to (165.0, 38.0) to stay on the map. New: The tusker road; An old milestone; The pass-stone.
- **29 Home Water**: ends at Vael; Glasswater. Close-up on (150.5, 40.5), 20 px/league. New: The Titan on the lake; The cup's edge.
- **30 Wendmouth**: ends at Wendmouth; the Halloran mint. Close-up on (184, 192), 20 px/league. New: Corsa; Calder's flight to Wendmouth; The Halloran mint; Gallows Quay, the cages opened; The Halloran warehouse burned.
- **31 The Oldest Roll**: ends at The Long Library. Close-up on (151.5, 37), 24 px/league. New: Orrun on the shingle.
- **32 Door-Keeper**: ends at The Long Library. Close-up on (151.5, 37), 24 px/league. New: The Old Reader's perch.
- **33 The Iron Fells**: ends at The Iron Fells. Close-up on (162, 50), 12 px/league. New: The hunters' camp; Starwatch; Tasso warmed.
- **34 What the Bird Remembers**: ends at The Long Library. Close-up on (151.5, 37), 24 px/league. New: nothing.
- **35 Starwatch**: ends at Starwatch. Close-up on (157, 44), 20 px/league. New: The guardhouse roof.
- **36 The Great Binding**: ends at Vael; the Undercroft. Close-up on (150.5, 39.5), 24 px/league. New: The Undercroft; The great binding; The Blue tower falls; Ice on Glasswater.
- **37 Glasswater**: ends at Glasswater; lower Vael. Close-up on (150.5, 41), 24 px/league. New: It flew west; The Pale Coil rose; The lion's wall; The meltflood.
- **38 The Library Hill**: ends at The Library hill. Close-up on (151.5, 38), 24 px/league. New: After the hunters; Fight on the Library hill.
- **39 The Long Library**: ends at The Long Library. Close-up on (151.5, 37), 24 px/league. New: Where the bird was killed.
- **40 Cinders**: ends at The Library steps. Close-up on (151.5, 37), 24 px/league. New: The bird's pyre.
- **41 The Milestones**: ends at The Glasswater shore. Close-up on (150.5, 41), 24 px/league. New: The Scald; Temple of the Scald; The Sun Stair; The frost-map; The six ends.
- **42 The Iron Road**: ends at The Coldrun canals; the Scald cordon. Close-up on (96, 52), 7 px/league, slid to (96.0, 73.7) to stay on the map. New: Ironhythe; Gearmouth; Coldrun Locks; The Last Titan's road; The canal road; Pike's cage.
- **43 The Flood**: ends at The Wend in flood; Greyhold landing. Close-up on (170, 84), 8.5 px/league. New: Wendhead; Cray's Ford; Lowfold; Brookend; Sallow Lock; Ahead of the flood; Water coming; The ferry driven onto the jetty; The Eelweir, lost.
- **44 Heartstones**: ends at Kessmoor's engine-houses. Close-up on (94, 68), 12 px/league. New: The north-quarter engine-house.
- **45 The Scald**: ends at The Scald. Close-up on (94, 68), 12 px/league. New: Orrin's ruins; The Last Titan's road; The egg taken; The labourers pulled out.
- **46 The Crown's Square**: ends at Hallowmere. Close-up on (130, 108), 20 px/league. New: Calder flies to Hallowmere; The Crown's Square.
- **47 The Chain-Ends**: ends at The Scald. Close-up on (94, 68), 12 px/league. New: Solenne.
- **48 Chilled Water**: ends at The Scald cordon. Close-up on (94, 68), 12 px/league. New: The Furnace rose, and was caged; Three lions on three banks.
- **49 Corsa**: ends at Corsa. Close-up on (250, 184), 20 px/league. New: Gullhaven; The Saltings; Down the coast with Aurveth; The Tidehall; Rusk flees.
- **50 Envoys**: ends at The Scald; the envoys' camp. Close-up on (93, 68), 12 px/league. New: Circling the Western Deep; The envoys' camp.
- **51 Midwinter**: ends at Orrin's ruins. Close-up on (94, 67), 12 px/league. New: Midwinter in Orrin.
- **52 Wren's Letter**: ends at The hatching caves, Varrhold. Close-up on (187, 92.5), Marches scale, 30 px/league. New: nothing.
- **53 The Basin Floor**: ends at Under the Scald. Close-up on (94, 68), 12 px/league. New: The Furnace's tunnel.
- **54 The Song**: ends at Varrhold. Close-up on (183.5, 99), Marches scale, 30 px/league. New: The Drowned Bell; The Restoration's army breaks.
- **55 The Sun Road**: ends at The Sun Road; Solenne. Close-up on (72, 130), 7 px/league. New: Highcrest; Maren's road to Solenne; Stage-chapels to the Sun on the Stair.
- **56 Blackwater**: ends at Blackwater. Close-up on (292, 180), 20 px/league. New: Blackwater; To Blackwater; The boathouse fight; Where the bronze was killed.
- **57 The Unicorn**: ends at The Elderwood. Close-up on (50, 156), 20 px/league. New: The unicorns' clearing.
- **58 The Grace**: ends at Solenne, the palace. Close-up on (50, 172), 24 px/league. New: The Last Titan's road; The Titan on the hills; The hands' hall.
- **59 The Coast**: ends at The Drowned Bell reef. Close-up on (218, 192), 12 px/league, slid to (218.0, 180.0) to stay on the map. New: The Drowned Bell's reef; Aurveth's deep sight; The Clan's baskets.
- **60 The Sun Stair**: ends at The Sun Stair. Close-up on (50, 174), 24 px/league. New: The egg taken.
- **61 The Collar**: ends at Solenne, the royal stair. Close-up on (50, 174), 24 px/league. New: The Last Titan's road; The Horned Sun rose; Where the Bond-King died.
- **62 The Young Ones**: ends at The hatching caves, Varrhold. Close-up on (187, 92.5), Marches scale, 30 px/league. New: nothing.
- **63 Solenne**: ends at Solenne; Sorrel Isle. Close-up on (52, 178), 20 px/league. New: Sorrel Isle; Idony taken; Boats to Sorrel Isle; Where Mother Ysa drowned.
- **64 The Reef**: ends at Gullhaven. Close-up on (217, 191), 12 px/league, slid to (217.0, 180.0) to stay on the map. New: Four hundred and twelve roofs marked.
- **65 The Map**: ends at Sorrel Isle lighthouse. Close-up on (54, 180), 24 px/league. New: The lighthouse.
- **66 Two Roads**: ends at Gullhaven. Close-up on (217, 191), 12 px/league, slid to (217.0, 180.0) to stay on the map. New: nothing.
- **67 Hallowmere**: ends at Hallowmere. Close-up on (110, 128), 9 px/league. New: Maren's road home; The chapel off the corn exchange.
- **68 The Tide Council**: ends at Corsa. Close-up on (255, 184), 20 px/league. New: Stillhaven; The Clan over Corsa.
- **69 Greyhold**: ends at Greyhold. Close-up on (174.5, 105.5), Marches scale, 30 px/league. New: The cage's anchors.
- **70 Gullhaven**: ends at Gullhaven. Close-up on (218, 192), 12 px/league, slid to (218.0, 180.0) to stay on the map. New: The Strand fleet; Hull-runes burning.
- **71 The Ship**: ends at The Saltings (Corvin's ship). Close-up on (240, 186), 7.5 px/league, slid to (240.0, 150.0) to stay on the map. New: Over the Saltings; Corvin's ship; Corvin's ship in the reeds.
- **72 The Marches**: ends at The Marches; Greyhold landing. Close-up on (175, 103), Marches scale, 30 px/league. New: Ferriby's beasts taken; Binders turned at Penfold; The ferry runs night and day.
- **73 The Bell**: ends at The Drowned Bell reef. Close-up on (218, 193), 12 px/league, slid to (218.0, 180.0) to stay on the map. New: Vey's fleet on the reef; Where Vey died.
- **74 One Hour of Light**: ends at Greyhold landing. Close-up on (174.5, 105), Marches scale, 30 px/league. New: One hour of light.
- **75 Marked Roofs**: ends at Gullhaven spit. Close-up on (217, 197), 24 px/league. New: The Last Titan's road; The Bell rose; The wave.
- **76 The Eddy**: ends at The eddy where the island was. Close-up on (175.8, 103.8), Marches scale, 30 px/league. New: By wyvern to the eddy; Cassian's pyre.
- **77 The Old Stair**: ends at The older stair. Close-up on (174, 105.5), Marches scale, 30 px/league. New: The older stair.
- **78 Ashes on the Saltings**: ends at The Saltings; the flight home. Close-up on (200, 150), 5.5 px/league, slid to (200.0, 120.9) to stay on the map. New: The Last Titan's road; The flight home; The drowned burned on the shingle.
- **79 The Last Crossing**: ends at Greyhold landing. Close-up on (174.5, 106), Marches scale, 30 px/league. New: Seventy go into the cellars.
- **80 The Trap**: ends at Greyhold's hill and the river. Close-up on (174.8, 105.5), Marches scale, 30 px/league. New: It came down; The second cage; The last of the Restoration's war.
- **81 Below the Chains**: ends at The cavern under the river. Close-up on (175, 105), Marches scale, 30 px/league. New: The shut place.
- **82 Fire Underground**: ends at The cavern. Close-up on (175, 105), Marches scale, 30 px/league. New: The Last Titan's road; The eyes tear out.
- **83 The Cellars**: ends at The Greyhold cellars. Close-up on (174.3, 106), Marches scale, 30 px/league. New: The cellars.
- **84 The Held Breath**: ends at The deepest vault. Close-up on (174.6, 105.5), Marches scale, 30 px/league. New: The control relic taken.
- **85 Up Through the Rock**: ends at The river; up through the rock. Close-up on (175, 106), Marches scale, 30 px/league. New: Greyhold, fallen; The lion comes up.
- **86 The Hill**: ends at Liss's ferry house. Close-up on (174.5, 106.5), Marches scale, 30 px/league. New: The envoys' table.
- **87 The Last Chart**: ends at Liss's ferry house. Close-up on (177, 103.5), Marches scale, 30 px/league. New: The Last Titan's road; The Last Titan on the Scarfell.
- **88 The Account**: ends at The Scarfell; the hatching caves. Close-up on (186, 93), Marches scale, 30 px/league. New: The six flew east; The five came; The account begun.

### Book Three

- **Front matter**: ends at Before the story begins. Close-up on (179, 104), Marches scale, 30 px/league. New: front-matter page, everything known when the book opens.
- **01 The Fallen Hill**: ends at Greyhold's fallen hill. Close-up on (174.4, 106.2), Marches scale, 30 px/league. New: The six over the Worldsend; The dig; The lintel held.
- **02 Bel's Table**: ends at The hatching caves above Coldtarn. Close-up on (187, 92), Marches scale, 30 px/league. New: nothing.
- **03 Davin's Hand**: ends at Liss's ferry house. Close-up on (174.6, 106.4), Marches scale, 30 px/league. New: Davin writes for Idony.
- **04 Liss's Kitchen**: ends at Liss's ferry house; the road east. Close-up on (196, 104), 9 px/league. New: The six came down.
- **05 The Chair Between**: ends at Varrhold. Close-up on (184.6, 95.5), Marches scale, 30 px/league. New: The empty chair.
- **06 Toll Gates**: ends at The Coast Road; a toll gate. Close-up on (198, 190), 20 px/league. New: Sallow Bar; Calder's road to the coast; The toll gate at Sallow Bar; Gullhaven's families in the top field.
- **07 Stonehorns**: ends at The Hallow Plains; the Ysse fords. Close-up on (256, 122), 12 px/league. New: The six together; Maren's road east; The Ysse fords; The ridge of stone.
- **08 Wages**: ends at Solenne's low city; the road north. Close-up on (60, 120), 7 px/league. New: Tobin's road north.
- **09 The Houses' Table**: ends at Corsa. Close-up on (258, 186), 12 px/league, slid to (258.0, 180.0) to stay on the map. New: The Bell went to its sea.
- **10 Marshal**: ends at Hallowmere; the Greenwold road. Close-up on (152, 96), 12 px/league. New: The Greenwold road's ford; The Greenwold road; Rowan's road.
- **11 The Border**: ends at The Hearthmere border. Close-up on (177, 86), 20 px/league. New: The six divided; The clans' road west.
- **12 The Clock**: ends at Ironhythe, the Hall of Measures. Close-up on (64, 47), 12 px/league. New: To the Accord; The Accord of Ironhythe.
- **13 Never Sleep Ashore**: ends at Blackwater. Close-up on (292, 182), 12 px/league, slid to (292.0, 180.0) to stay on the map. New: The Merrin house; The reef-stone.
- **14 Salt on the Tongue**: ends at Blackwater. Close-up on (293, 181), 12 px/league, slid to (293.0, 180.0) to stay on the map. New: To Blackwater on the lion.
- **15 Chain Money**: ends at Corsa harbour. Close-up on (262, 188), 12 px/league, slid to (262.0, 180.0) to stay on the map. New: The hulks on the ropewalk terrace; The low harbour.
- **16 Far-Stone**: ends at Blackwater, the Merrins' salvage hold. Close-up on (294, 180), 12 px/league. New: The drowned road.
- **17 The Reef Channel**: ends at The Merrins' reef channel. Close-up on (293, 182), 12 px/league, slid to (293.0, 180.0) to stay on the map. New: The reef-stone lifted.
- **18 The Breeding Pens**: ends at Varrhold, the breeding pens. Close-up on (184.6, 95), Marches scale, 30 px/league. New: The pens opened.
- **19 The Bell Comes In**: ends at Corsa. Close-up on (258, 186), 12 px/league, slid to (258.0, 180.0) to stay on the map. New: The Bell came in; Corsa's chain snaps; Where Ulric died.
- **20 The Berths**: ends at Blackwater. Close-up on (292, 182), 12 px/league, slid to (292.0, 180.0) to stay on the map. New: The Far Berths.
- **21 Unsalted**: ends at Blackwater's harbour mouth. Close-up on (284, 192), 12 px/league. New: Into the light, 41; The Kittiwake sails; The boom broken.
- **22 Pour With Me**: ends at Coldtarn. Close-up on (187, 92), Marches scale, 30 px/league. New: Ulric's ashes poured.
- **23 The Candle Downs**: ends at The Candle Downs. Close-up on (136, 118), 12 px/league. New: Beacon Ridge; The Last Titan's road; The ward on Beacon Ridge; The Mere boils.
- **24 The Drowned Road**: ends at The drowned road (milestone two). Close-up on (172, 244), 5 px/league. New: Into the light, 11; The Bell on the road; Where Hal Merrin drowned.
- **25 The Last Milestone**: ends at The last milestone and the reef. Close-up on (145, 270), 12 px/league. New: Into the light, 1; The shelf; The Needle; The Bell at the road's end; Two lions in the Needle.
- **26 The Pilot**: ends at Blackwater; out over the Shatters. Close-up on (258, 212), 6 px/league. New: nothing.
- **27 The Lit Shore**: ends at The Lit Shore. Close-up on (139, 279), 12 px/league. New: The city on the sand; The Grey Mother's hill; The Kittiwake's anchorage; The mountain on the hill.
- **28 The Shatters**: ends at The Shattered Sea (pier eleven). Close-up on (168, 252), 7 px/league. New: Over the Shatters; The Berths fleet lost.
- **29 Ashore**: ends at The Lit Shore, the Kittiwake's anchorage. Close-up on (143, 274), 20 px/league. New: Where Sim slept.
- **30 What She Showed**: ends at The hills of the Lit Shore. Close-up on (138, 282), 20 px/league. New: What she showed.
- **31 The Script in the Light**: ends at The hills of the Lit Shore. Close-up on (138, 282), 20 px/league. New: The Hall of Light; The script in the light.
- **32 The Shrine**: ends at The crossroads on the far shore's south coast. Close-up on (132, 294), 20 px/league. New: The crossroads; The south bay; The Wayfarer; Piers Calloway.
- **33 The Works**: ends at Ironhythe, the works. Close-up on (63, 46), 12 px/league. New: The Bridle.
- **34 The Hall of Light**: ends at The Hall of Light. Close-up on (134, 287), 20 px/league. New: Four elders.
- **35 Two Hands**: ends at The Hall of Light. Close-up on (134, 287), 20 px/league. New: nothing.
- **36 What the Ring Answers**: ends at The Hall of Light. Close-up on (134, 287), 20 px/league. New: nothing.
- **37 Consent**: ends at The Lit Shore (the Hall's ridge). Close-up on (134, 287), 20 px/league. New: The lion becomes a Titan.
- **38 Empty Pens**: ends at The Saltreach coast. Close-up on (232, 150), 7 px/league, slid to (232.0, 144.3) to stay on the map. New: Rocs over the Saltings; Lost in the Bell's surf.
- **39 The Crossroads**: ends at The crossroads on the far shore. Close-up on (132, 294), 20 px/league. New: Three dragons become Titan-class.
- **40 Under the Sea**: ends at Under the Shattered Sea; the Drowned Bell's reef. Close-up on (178, 238), 5 px/league. New: Under the sea; The Lady keeps pace.
- **41 The Wend Camp**: ends at The Accord's camp behind the Wend. Close-up on (177, 107), Marches scale, 30 px/league. New: The Pale Coil; The Horned Sun; Kessmoor turned the Furnace; The Antlered; The Accord's camp; Kessmoor's pontoon.
- **42 Homeward**: ends at The hatching caves. Close-up on (187, 92), Marches scale, 30 px/league. New: Calder flies home.
- **43 The Saltings**: ends at The Saltings. Close-up on (224, 186), 12 px/league, slid to (224.0, 180.0) to stay on the map. New: Redshank; Orrun comes ashore; The sea-wall rebuilt by hand.
- **44 Salt Debts**: ends at Blackwater. Close-up on (292, 182), 12 px/league, slid to (292.0, 180.0) to stay on the map. New: The Lamp came ashore; The Kittiwake home.
- **45 Three Hills**: ends at The hatching caves. Close-up on (187.5, 92), Marches scale, 30 px/league. New: The three hills.
- **46 Banners**: ends at The Accord's muster, the Marches. Close-up on (177, 107), Marches scale, 30 px/league. New: The lion comes home; The Lady in the Wend; The Lamp at the muster.
- **47 Kin**: ends at The muster. Close-up on (177, 107), Marches scale, 30 px/league. New: nothing.
- **48 Night Shift**: ends at Ironhythe, the works. Close-up on (63, 46), 12 px/league. New: The harvest sheds.
- **49 Fire in the Forest**: ends at The Thornwood. Close-up on (232, 58), 12 px/league. New: Fire in the forest; Where Gunna and Tamsin died.
- **50 Antlers**: ends at The Thornwood. Close-up on (229, 56), 12 px/league. New: The Antlered killed.
- **51 Plates**: ends at The Thornwood field; the Accord's council. Close-up on (215, 78), 7 px/league. New: Kessmoor's carts at the plates.
- **52 Where the Breath Went**: ends at The Accord's camp. Close-up on (196, 92), 5.5 px/league, slid to (196.0, 97.1) to stay on the map. New: The five turned to the hub; The glass-line.
- **53 The Middle of the World**: ends at The eddy where the island was. Close-up on (175.8, 104), Marches scale, 30 px/league. New: The Vintner's Gate; The Sun turned back; Maren's road home; The ramparts; Liss's ferry house; Liss's rope over the eddy; The camp at the eddy.
- **54 Wren's Question**: ends at Coldtarn. Close-up on (187, 92), Marches scale, 30 px/league. New: The hall under Coldtarn; The hall under the tarn.
- **55 The Ring Plan**: ends at The war council. Close-up on (175.8, 104), the Vale, 45 px/league. New: The Ferry Flat; The jibs.
- **56 Black Ice**: ends at The upper Wend. Close-up on (176, 93.5), Marches scale, 30 px/league. New: Eskby; Otterholt; Trimley; The Pale Coil came down the Wend; Black ice; The Lady drives the Coil back.
- **57 A Visitor**: ends at The Accord's camp. Close-up on (175.8, 104), the Vale, 45 px/league. New: Corvin's visit.
- **58 The Floating Market**: ends at Wendmouth; the Saltreach bank. Close-up on (180, 160), 5.5 px/league, slid to (180.0, 120.9) to stay on the map. New: The Sheepford; The floating market lifted.
- **59 The Warm Water**: ends at Coldtarn. Close-up on (187, 92), Marches scale, 30 px/league. New: The hall's door opened.
- **60 Barges**: ends at The Wend. Close-up on (176, 108), Marches scale, 30 px/league. New: Six thousand and twelve.
- **61 Eve**: ends at The eddy, on Liss's ferry. Close-up on (175.8, 104), the Vale, 45 px/league. New: Eve, on the ferry.
- **62 Watches**: ends at The hub, where the island was. Close-up on (175.8, 104), the Vale, 45 px/league. New: The Bridle comes down the Iron Road; The Bridle set.
- **63 Noon**: ends at The line across the Vale. Close-up on (175.8, 104), the Vale, 45 px/league. New: The Last Titan; The Pale Coil; The Bell; The Furnace; The Horned Sun; Two wards.
- **64 The First Day**: ends at Over the Vale. Close-up on (175.8, 104), the Vale, 45 px/league. New: Stone lions in the wall; Kharrak against the Horned Sun.
- **65 The Line**: ends at The line. Close-up on (175.8, 104), the Vale, 45 px/league. New: The Furnace quenched.
- **66 Orrun**: ends at The river. Close-up on (175.8, 104), the Vale, 45 px/league. New: A league of bank stopped.
- **67 Night Flights**: ends at The Scarfell. Close-up on (182, 97), Marches scale, 30 px/league. New: The wounded flown out.
- **68 The Second Day**: ends at The eddy. Close-up on (175.8, 104), the Vale, 45 px/league. New: "We've got it."; The Kingfisher Shallows.
- **69 The Stage**: ends at The Bridle's stage. Close-up on (175.6, 104), the Vale, 45 px/league. New: The Bridle's stage.
- **70 The Hour**: ends at The Last Titan's back. Close-up on (175.8, 104), the Vale, 45 px/league. New: The hour.
- **71 The Battery**: ends at The hub battery. Close-up on (175.6, 104), the Vale, 45 px/league. New: Where Tobin died.
- **72 Smoke**: ends at The gap. Close-up on (176, 104), the Vale, 45 px/league. New: A road of fire.
- **73 On the Gate**: ends at The gap. Close-up on (175.6, 104), the Vale, 45 px/league. New: Where Rowan fell.
- **74 The Coal**: ends at The Last Titan's back. Close-up on (175.8, 104), the Vale, 45 px/league. New: Where Corvin died.
- **75 Where the Island Was**: ends at Where the island was. Close-up on (177, 104), Marches scale, 30 px/league. New: The middle of the world breaks; The herd-charm.
- **76 The Masthead**: ends at The lower Wend below the Sheepford. Close-up on (176, 110), Marches scale, 30 px/league. New: Where the Lady and the Bell went down; The Kittiwake aground.
- **77 Six Roads**: ends at Six roads north. Close-up on (178.2, 102.8), the Vale, 45 px/league. New: Six roads north; Orrun across the Way.
- **78 The Top Field**: ends at Harrow's End, the Fenn top field. Close-up on (178.2, 102.8), the Vale, 45 px/league. New: Where Kharrak died.
- **79 No Price**: ends at The hall's mouth, Coldtarn. Close-up on (187, 92), Marches scale, 30 px/league. New: Salt on the tongue, nothing owed; Where Gannet died.
- **80 The Count**: ends at The hall under Coldtarn. Close-up on (187, 92), Marches scale, 30 px/league. New: Four hundred and seventy-three.
- **81 Deep Sight**: ends at Coldtarn. Close-up on (187, 92), Marches scale, 30 px/league. New: Where Lisska fell; Where Aurveth lay down.
- **82 Breaths**: ends at The hall under Coldtarn. Close-up on (187, 92), Marches scale, 30 px/league. New: Breaths going out.
- **83 The Threshold**: ends at The door under Coldtarn. Close-up on (187, 92), Marches scale, 30 px/league. New: The door kept; Where Orrun died.
- **84 First Light**: ends at The hall under Coldtarn. Close-up on (187, 92), Marches scale, 30 px/league. New: The bond went quiet.
- **85 Who Pours**: ends at Coldtarn. Close-up on (186, 93), Marches scale, 30 px/league. New: Varrhold, under the slip; Empty hands poured.
- **86 The Watch**: ends at The fallen door. Close-up on (187, 92), Marches scale, 30 px/league. New: The first fire; Something small, of stone.
