"""Book 3 (The Titan War): the chapter-end maps.

Same page as Books 1 and 2: Winshire on top, a close-up below centred on the chapter's "Ends at" place
(Book 3/Chapter_Plan.md, checked against the drafted chapters), what's new beside it.
Chapter 0 is the front-matter page: everything known at the end of Book 2.
The far shore (the Lit Shore) lies off the edge of Winshire, about ninety leagues south-west over the Shattered Sea
along the drowned road; its coast and places here are working proposals built from the chapters (see NOTES.md).
"""
import math
import world as Wd
import book2_items
from bookdata import Book, MARCHES as M

B2 = book2_items.B
B = Book(3, "Book Three")
B.start_from(B2)
B.CATACOMBS_CH = B.LATER          # the cavern fell in with Greyhold's hill (Book 2 ch 85)
B.KINGDOM_LABEL_AT = dict(B2.KINGDOM_LABEL_AT)
B.LINGER = 8                      # events fade from the map eight chapters on; deaths, houses, walls and roads stay
B.LASTING_KINDS = ("death", "house", "wall", "road", "sea")
B.EXTRA_ISLANDS = list(B2.EXTRA_ISLANDS)
item, line, place, chapter = B.item, B.line, B.place, B.chapter

# ---------------- the drowned road and the far shore ----------------
U = (-0.722, 0.692)                     # the road's bearing, south-west from the Drowned Bell's reef
P41 = (211.0, 209.0)                    # "into the light, forty-one", two days out of Blackwater
def pier(k):
    t = (41 - k) * 2.2
    return (round(P41[0] + U[0] * t, 2), round(P41[1] + U[1] * t, 2))
L = (144.6, 272.7)                      # the road's landfall: the city on the sand at the lagoon
def along(p, d, v=U):
    return (round(p[0] + v[0] * d, 2), round(p[1] + v[1] * d, 2))
MH = (136.7, 280.3)                     # the Grey Mother's hill, two days inland
HALL = (133.5, 289.0)                   # the Hall of Light, where the road crosses the ridge
CROSS = (130.5, 296.0)                  # the crossroads, half a day inland of the south bay
BAY = (131.6, 302.2)                    # the south bay
B.EXTRA_LAND = [[(116, 247), (126, 255), (134, 262), (139.6, 267.6), (143.0, 271.0), (145.6, 273.6), (149.0, 277.0),
                 (151.8, 281.5), (151.0, 288.5), (147.0, 295.5), (141.0, 300.5), (135.2, 303.2), (130.6, 302.2),
                 (126.0, 304.6), (114.0, 307.0), (98.0, 318.0), (80.0, 336.0), (60.0, 360.0), (30.0, 360.0),
                 (20.0, 300.0), (40.0, 258.0), (80.0, 244.0)]]
B.EXTRA_LAND_CH = [25]                # nobody has seen the far shore until the Kittiwake raises it (ch 25)
B.EXTRA_SEAS = {}
B.EXTRA_LABELS = {"THE LIT SHORE": (122.0, 284.0, -44), "the Shatters": (232.0, 216.0, 0)}
B.REALM_LABEL_REVEAL.update({"THE LIT SHORE": 27, "the Shatters": 21})

# ---------------- the chapters ----------------
T, N, R, W, V = 20, 12, 7, 5.5, "V"
chapter(0, "", "", "Before the story begins", (179.0, 104.0), M, "The Marches", "As Book Two ends")
_CH = [
    (1, "S", "The Fallen Hill", "Greyhold's fallen hill", (174.4, 106.2), M, "The Marches", "Greyhold's fallen hill"),
    (2, "F", "Bel's Table", "The hatching caves above Coldtarn", (187.0, 92.0), M, "The Scarfell", "The hatching caves above Coldtarn"),
    (3, "R", "Davin's Hand", "Liss's ferry house", (174.6, 106.4), M, "The Marches", "Liss's ferry house"),
    (4, "S", "Liss's Kitchen", "Liss's ferry house; the road east", (196.0, 104.0), 9, "Saltreach", "The road east from the ferry"),
    (5, "C", "The Chair Between", "Varrhold", (184.6, 95.5), M, "The Scarfell", "Varrhold"),
    (6, "F", "Toll Gates", "The Coast Road; a toll gate", (198.0, 190.0), T, "Saltreach", "The Coast Road and Sallow Bar"),
    (7, "S", "Stonehorns", "The Hallow Plains; the Ysse fords", (256.0, 122.0), N, "The Wyldmarch", "The Ysse fords"),
    (8, "U", "Wages", "Solenne's low city; the road north", (60.0, 120.0), R, "Sarovel", "The road north from Solenne"),
    (9, "F", "The Houses' Table", "Corsa", (258.0, 186.0), N, "Saltreach", "Corsa"),
    (10, "G", "Marshal", "Hallowmere; the Greenwold road", (152.0, 96.0), N, "Hearthmere", "Hallowmere and the Greenwold road"),
    (11, "S", "The Border", "The Hearthmere border", (177.0, 86.0), T, "The Border", "The Greenwold road's ford"),
    (12, "F", "The Clock", "Ironhythe, the Hall of Measures", (64.0, 47.0), N, "Kessmoor", "Ironhythe, the Hall of Measures"),
    (13, "M", "Never Sleep Ashore", "Blackwater", (292.0, 182.0), N, "Saltreach", "Blackwater"),
    (14, "S", "Salt on the Tongue", "Blackwater", (293.0, 181.0), N, "Blackwater", "The inlet"),
    (15, "F", "Chain Money", "Corsa harbour", (262.0, 188.0), N, "Corsa", "The harbour"),
    (16, "R", "Far-Stone", "Blackwater, the Merrins' salvage hold", (294.0, 180.0), N, "Blackwater", "The Merrins' salvage hold"),
    (17, "S", "The Reef Channel", "The Merrins' reef channel", (293.0, 182.0), N, "Blackwater", "The Merrins' reef channel"),
    (18, "C", "The Breeding Pens", "Varrhold, the breeding pens", (184.6, 95.0), M, "The Scarfell", "Varrhold, the breeding pens"),
    (19, "F", "The Bell Comes In", "Corsa", (258.0, 186.0), N, "Saltreach", "Corsa"),
    (20, "M", "The Berths", "Blackwater", (292.0, 182.0), N, "Saltreach", "Blackwater"),
    (21, "S", "Unsalted", "Blackwater's harbour mouth", (284.0, 192.0), N, "The Shattered Sea", "Blackwater's mouth and the reefs", True),
    (22, "F", "Pour With Me", "Coldtarn", (187.0, 92.0), M, "The Scarfell", "Coldtarn"),
    (23, "G", "The Candle Downs", "The Candle Downs", (136.0, 118.0), N, "Hearthmere", "The Candle Downs"),
    (24, "S", "The Drowned Road", "The drowned road (milestone two)", (172.0, 244.0), 5.0, "The Drowned Road", "Milestone two", True),
    (25, "M", "The Last Milestone", "The last milestone and the reef", (145.0, 270.0), N, "The Lit Shore", "The last milestone", True),
    (26, "F", "The Pilot", "Blackwater; out over the Shatters", (258.0, 212.0), 6.0, "The Shattered Sea", "Blackwater and the Shatters", True),
    (27, "S", "The Lit Shore", "The Lit Shore", (139.0, 279.0), N, "The Lit Shore", "The city on the sand", True),
    (28, "F", "The Shatters", "The Shattered Sea (pier eleven)", (168.0, 252.0), R, "The Shattered Sea", "Pier eleven", True),
    (29, "M", "Ashore", "The Lit Shore, the Kittiwake's anchorage", (143.0, 274.0), T, "The Lit Shore", "The Kittiwake's anchorage", True),
    (30, "S", "What She Showed", "The hills of the Lit Shore", (138.0, 282.0), T, "The Lit Shore", "The Grey Mother's hill", True),
    (31, "R", "The Script in the Light", "The hills of the Lit Shore", (138.0, 282.0), T, "The Lit Shore", "The Grey Mother's hill", True),
    (32, "F", "The Shrine", "The crossroads on the far shore's south coast", (132.0, 294.0), T, "The Lit Shore", "The crossroads", True),
    (33, "U", "The Works", "Ironhythe, the works", (63.0, 46.0), N, "Ironhythe", "The works"),
    (34, "S", "The Hall of Light", "The Hall of Light", (134.0, 287.0), T, "The Lit Shore", "The Hall of Light", True),
    (35, "F", "Two Hands", "The Hall of Light", (134.0, 287.0), T, "The Lit Shore", "The Hall of Light", True),
    (36, "R", "What the Ring Answers", "The Hall of Light", (134.0, 287.0), T, "The Lit Shore", "The Hall of Light", True),
    (37, "S", "Consent", "The Lit Shore (the Hall's ridge)", (134.0, 287.0), T, "The Lit Shore", "The ridge of the Hall of Light", True),
    (38, "C", "Empty Pens", "The Saltreach coast", (232.0, 150.0), R, "Saltreach", "The coast emptied"),
    (39, "F", "The Crossroads", "The crossroads on the far shore", (132.0, 294.0), T, "The Lit Shore", "The crossroads", True),
    (40, "S", "Under the Sea", "Under the Shattered Sea; the Drowned Bell's reef", (178.0, 238.0), 5.0, "The Shattered Sea", "Under the sea, on the drowned road", True),
    (41, "G", "The Wend Camp", "The Accord's camp behind the Wend", (177.0, 107.0), M, "The Marches", "The Accord's camp behind the Wend"),
    (42, "F", "Homeward", "The hatching caves", (187.0, 92.0), M, "The Scarfell", "The hatching caves"),
    (43, "S", "The Saltings", "The Saltings", (224.0, 186.0), N, "Saltreach", "The Saltings"),
    (44, "M", "Salt Debts", "Blackwater", (292.0, 182.0), N, "Saltreach", "Blackwater"),
    (45, "F", "Three Hills", "The hatching caves", (187.5, 92.0), M, "The Scarfell", "Coldtarn's rim"),
    (46, "G", "Banners", "The Accord's muster, the Marches", (177.0, 107.0), M, "The Marches", "The Accord's muster"),
    (47, "S", "Kin", "The muster", (177.0, 107.0), M, "The Marches", "The muster"),
    (48, "U", "Night Shift", "Ironhythe, the works", (63.0, 46.0), N, "Ironhythe", "The works and the harvest sheds"),
    (49, "F", "Fire in the Forest", "The Thornwood", (232.0, 58.0), N, "The Wyldmarch", "The Thornwood's western edge"),
    (50, "S", "Antlers", "The Thornwood", (229.0, 56.0), N, "The Wyldmarch", "The Thornwood"),
    (51, "F", "Plates", "The Thornwood field; the Accord's council", (215.0, 78.0), 7.0, "The Wyldmarch", "The Thornwood field and the Wend"),
    (52, "R", "Where the Breath Went", "The Accord's camp", (196.0, 92.0), W, "The Glass-Line", "From the Thornwood to the Mere"),
    (53, "S", "The Middle of the World", "The eddy where the island was", (175.8, 104.0), M, "The Marches", "The eddy where the island was"),
    (54, "F", "Wren's Question", "Coldtarn", (187.0, 92.0), M, "The Scarfell", "Coldtarn"),
    (55, "G", "The Ring Plan", "The war council", (175.8, 104.0), V, "The Vale", "The line across the Vale"),
    (56, "S", "Black Ice", "The upper Wend", (176.0, 93.5), M, "The Marches", "The upper Wend"),
    (57, "R", "A Visitor", "The Accord's camp", (175.8, 104.0), V, "The Vale", "The camp at the eddy"),
    (58, "F", "The Floating Market", "Wendmouth; the Saltreach bank", (180.0, 160.0), W, "The Lower Wend", "Wendmouth to the hub"),
    (59, "S", "The Warm Water", "Coldtarn", (187.0, 92.0), M, "The Scarfell", "Coldtarn, the hall's door"),
    (60, "M", "Barges", "The Wend", (176.0, 108.0), M, "The Marches", "The Wend, from the Sheepford up"),
    (61, "F", "Eve", "The eddy, on Liss's ferry", (175.8, 104.0), V, "The Vale", "The eddy, on Liss's ferry"),
    (62, "U", "Watches", "The hub, where the island was", (175.8, 104.0), V, "The Vale", "The hub, where the island was"),
    (63, "S", "Noon", "The line across the Vale", (175.8, 104.0), V, "The Vale", "The line across the Vale"),
    (64, "F", "The First Day", "Over the Vale", (175.8, 104.0), V, "The Vale", "Over the Vale"),
    (65, "G", "The Line", "The line", (175.8, 104.0), V, "The Vale", "The line"),
    (66, "S", "Orrun", "The river", (175.8, 104.0), V, "The Vale", "The river"),
    (67, "C", "Night Flights", "The Scarfell", (182.0, 97.0), M, "The Scarfell", "Night flights to the Scarfell"),
    (68, "F", "The Second Day", "The eddy", (175.8, 104.0), V, "The Vale", "The eddy"),
    (69, "R", "The Stage", "The Bridle's stage", (175.6, 104.0), V, "The Vale", "The Bridle's stage"),
    (70, "S", "The Hour", "The Last Titan's back", (175.8, 104.0), V, "The Vale", "The hour"),
    (71, "U", "The Battery", "The hub battery", (175.6, 104.0), V, "The Vale", "The hub battery"),
    (72, "F", "Smoke", "The gap", (176.0, 104.0), V, "The Vale", "The gap"),
    (73, "G", "On the Gate", "The gap", (175.6, 104.0), V, "The Vale", "The gap"),
    (74, "S", "The Coal", "The Last Titan's back", (175.8, 104.0), V, "The Vale", "The Last Titan's back"),
    (75, "F", "Where the Island Was", "Where the island was", (177.0, 104.0), M, "The Marches", "Where the island was"),
    (76, "M", "The Masthead", "The lower Wend below the Sheepford", (176.0, 110.0), M, "The Marches", "Below the Sheepford"),
    (77, "S", "Six Roads", "Six roads north", (178.2, 102.8), V, "The Marches", "Six roads north"),
    (78, "F", "The Top Field", "Harrow's End, the Fenn top field", (178.2, 102.8), V, "The Marches", "The Fenn top field"),
    (79, "M", "No Price", "The hall's mouth, Coldtarn", (187.0, 92.0), M, "The Scarfell", "The hall's mouth, Coldtarn"),
    (80, "S", "The Count", "The hall under Coldtarn", (187.0, 92.0), M, "The Scarfell", "The hall under Coldtarn"),
    (81, "F", "Deep Sight", "Coldtarn", (187.0, 92.0), M, "The Scarfell", "Coldtarn"),
    (82, "R", "Breaths", "The hall under Coldtarn", (187.0, 92.0), M, "The Scarfell", "The hall under Coldtarn"),
    (83, "S", "The Threshold", "The door under Coldtarn", (187.0, 92.0), M, "The Scarfell", "The door under Coldtarn"),
    (84, "F", "First Light", "The hall under Coldtarn", (187.0, 92.0), M, "The Scarfell", "The hall under Coldtarn"),
    (85, "C", "Who Pours", "Coldtarn", (186.0, 93.0), M, "The Scarfell", "Coldtarn and Varrhold"),
    (86, "S", "The Watch", "The fallen door", (187.0, 92.0), M, "The Scarfell", "The fallen door"),
]
for _c in _CH:
    chapter(*_c)

# ---------------- places Book 3 names ----------------
place("greenwoldford", "The Greenwold road's ford", "tower", "hearthmere", 177.0, 84.0, 10,
      "The crown's post where the Greenwold road crosses the upper Wend under the last of the oaks: a barricade of felled oaks, a ditch, sixty crown men.", scope="both")
place("sallowbar", "Sallow Bar", "village", "saltreach", 201.0, 201.6, 6, "A fishing town of forty houses on a gravel bar where the Coast Road crosses a tidal creek, and a toll gate on the bridge.", scope="local")
place("beaconridge", "Beacon Ridge", "landmark", "hearthmere", 136.5, 118.5, 23, "The last chalk ridge south-east of Hallowmere, across the Stillhaven arm of the King's Road, where the ward held for an hour.", scope="local")
place("vintnersgate", "The Vintner's Gate", "landmark", "sarovel", 87.5, 112.8, 53, "The league-long defile where the Sun Road comes out of the Sunward Hills for Hallowmere.", scope="local")
place("redshank", "Redshank", "village", "saltreach", 219.4, 197.0, 43, "A fishing village of a dozen huts on stilts at the Saltings' western edge.", scope="local")
place("sheepford", "The Sheepford", "village", "hearthmere", 175.0, 112.0, 58,
      "The drovers' summer ford eight leagues below the hub, with a ford-and-landing village: the barges called it the Staithe until Kit named it again.", scope="local", ldx=-1)
place("eskby", "Eskby", "village", "hearthmere", 175.2, 92.4, 56, "A ferry village on the Hearthmere bank twelve leagues above the hub.", scope="marches", ldx=-1)
place("otterholt", "Otterholt", "village", "saltreach", 178.0, 89.6, 56, "Eel-weirs on the Saltreach bank of the upper Wend.", scope="marches")
place("trimley", "Trimley", "village", "hearthmere", 175.0, 87.2, 56, "A mill village on the Hearthmere bank of the upper Wend.", scope="marches", ldx=-1)
place("hall", "The hall under Coldtarn", "temple", "saltreach", 186.5, 91.5, 54,
      "An old-realm hall cut in the rock under the crag on Coldtarn's western side: two rows of pillars, three hundred and twelve sleeping-places, warm from the Deep under the tarn.",
      scope="marches", ldx=-1)
# the far shore
place("litcity", "The city on the sand", "ruin", "farshore", L[0], L[1], 27, "Old-realm stone half under white sand at the road's landfall: column-tops, a wall going down to the water, a great flight of steps. No people, no bones.",
      scope="local")
place("motherhill", "The Grey Mother's hill", "landmark", "farshore", MH[0], MH[1], 27, "A hill two days inland up the paved road, where a mountain shaped like a great cat lies in the light.", scope="local", ldy=1.2)
place("halloflight", "The Hall of Light", "temple", "farshore", HALL[0], HALL[1], 31, "A roofless hall of grey columns where the road crosses the ridge, a long pool down its middle, the lock's sentence over its arch.",
      scope="local")
place("crossroads", "The crossroads", "landmark", "farshore", CROSS[0], CROSS[1], 32, "A paved square of four milestones where the southern road crosses the western road; the Wayfarer stands in it.", scope="local", ldy=-1.0)
place("southbay", "The south bay", "landmark", "farshore", BAY[0], BAY[1] + 1.2, 32, "A bay on the far shore's south coast where a second paved road comes down to the sea.", scope="local")

B.REALM_LABEL_REVEAL.update({"The Greenwold": 10})
B.HIDE["varrhold"] = 85
place("varrholdburied", "Varrhold, under the slip", "ruin", "saltreach", 184.4, 94.8, 85,
      "The night the mountain came down at Coldtarn, the Scarfell's western shoulder moved and a slip came down over the hold, the byres, the pens and the ledges.", scope="both")

# ---------------- roads and lines that stay ----------------
line("greenwoldroad", "The Greenwold road", "road", 10, [(128.5, 107.5), (139, 97), (152, 89), (165, 85), (177, 84)],
     "The old road east from Hallowmere through the oak woods of the Greenwold to the ford on the upper Wend.", realm=True, label=True, carry=True)
line("drownedroad", "The drowned road", "sea", 16, [(217.5, 202.6), P41, pier(30), pier(20), pier(10), pier(1), along(L, -1.0)],
     "The old-realm causeway's broken piers south-west over the Shatters, island to island, every one with a milestone counting into the light.",
     realm=True, label=True, weight=1.8, at=(205, 214.8))
for _k in (41, 30, 20, 12, 11, 9, 5, 2, 1):
    item(f"pier{_k}", f"Into the light, {_k}" if _k in (41, 11, 1) else "", "landmark_pt", *pier(_k), {41: 21, 1: 25}.get(_k, 24),
         f"A square column of old grey stone standing out of the sea, broken at twice a mast's height, with a milestone on its top: into the light, {_k}.",
         size=0.7, label=_k in (41, 11, 1))
line("shelf", "The shelf", "sea", 25, [along(along(L, -3.0), -9, (0.692, 0.722)), along(L, -3.0), along(along(L, -3.0), 8, (0.692, 0.722)), (151.5, 286.5), (147.0, 298.5), (138.0, 305.2)],
     "The road's landfall shallows: old-realm causeway stone broken under a fathom of clear water, white along its seaward edge.", realm=False, label=False, weight=1.4)
item("needle", "The Needle", "landmark_pt", *along(pier(1), 0.6), 25, "The gap in the shelf by the last pier, passable at the top of the flood only.", size=0.7, dx=0.3)
line("litroad", "", "road", 27, [L, MH], "The paved road inland from the city on the sand to the hills.", realm=False)
line("litroad2", "", "road", 31, [MH, HALL], "The paved road on south-west from the hills to the ridge.", realm=False)
line("litroad3", "", "road", 32, [HALL, CROSS], "The paved road on from the ridge to the crossroads.", realm=False)
line("southroad", "", "road", 32, [BAY, CROSS, (137.5, 290.0), (143.0, 281.0), L], "The southern road, from the south bay north through the crossroads to the lagoon.", realm=False)

# ---------------- the Titans ----------------
def titan(id, ch, pts, desc, name="", label=False, weight=1.0, until=None, **kw):
    return line(id, name, "track", ch, pts, desc, realm=True, label=label, weight=weight, until=until, **kw)
def mark(id, name, x, y, ch, desc, kind="sleeper", until=None, realm=True, **kw):
    return item(id, name, kind, x, y, ch, desc, realm=realm, until=until, **kw)

mark("six1", "The six over the Worldsend", 299.0, 92.0, 1, "Lights over the Worldsend like a second dawn in the wrong place: the six drinking out of the mountains.", until=6, dx=-1)
titan("t3a", 4, [(299, 92), (290, 108), (281, 118)], "Dawn, day 9: the six came down off the Worldsend onto the Hallow Plains.", name="The six came down", label=True, until=12)
mark("six7", "The six together", 274.0, 121.0, 7, "Dusk, day 18: all six moving west across the burning Plains, a day east of the clans.", kind="titan", size=0.45, until=11)
titan("t3bell", 9, [(274, 122), (262, 148), (246, 176), (232, 190)], "Day 25: the Bell left the others and dragged itself south-west across the dead country to the sea.", name="The Bell went to its sea", label=True, until=19, weight=0.7)
for _i, (_d, _nm) in enumerate([((200, 52), "north, to Isvaren"), ((236, 132), "west, to Kessmoor"), ((238, 144), "south-west, to Sarovel"),
                                ((285, 80), "east, to the Thornwood"), ((242, 122), "west, to Hearthmere")]):
    if _i == 4:
        continue
    titan(f"t3div{_i}", 11, [(270, 122), along((270, 122), 18, ((_d[0] - 270) / math.hypot(_d[0] - 270, _d[1] - 122), (_d[1] - 122) / math.hypot(_d[0] - 270, _d[1] - 122)))],
          f"Day 41: the six divided, each to the ground it slept under: {_nm}.", name="The six divided" if _i == 0 else "", label=_i == 0, until=22, weight=0.6)
titan("t3last", 23, [(270, 122), (246, 126), (215, 128), (192, 126), (178, 124), (160, 123), (140, 120), (133, 113), (130.5, 117.5)],
      "West across Saltreach's moor and over the Wend below the Marches onto the Candle Downs; through Hallowmere, and down into the Mere (days 41-95).",
      name="The Last Titan's road", label=True, weight=1.2, keep=True)
titan("t3bell2", 19, [(222, 196), (240, 186), (258, 191.5)], "Day 88: the Bell came out of the west across the Saltings and broke Corsa's chain.", name="The Bell came in", label=True, until=26, weight=0.7)
titan("t3bell3", 20, [(262, 196), (285, 200), (290, 210), (276, 218)], "Days 89-90: east past Blackwater's mouth, then south out over the Shatters.", until=26, weight=0.7)
mark("coil41", "The Pale Coil", 151.0, 46.0, 41, "Vael silent: the lake ice in summer, the Coil coiled round it.", until=55, size=0.8)
mark("sun41", "The Horned Sun", 56.0, 160.0, 41, "Solenne emptied to Sorrel Isle when it came up the Gilt again.", until=52, size=0.8)
item("furnace41", "Kessmoor turned the Furnace", "battle", 21.5, 57.0, 41, "Day 126 at the Gearmouth foundries: engines on rails, bolt-throwers, chilled canals. The only kingdom to turn a Titan.", realm=True, until=52)
mark("antlered41", "The Antlered", 240.0, 50.0, 41, "Holding what's left of the Wyldmarch.", until=49, size=0.8)
mark("lamp44", "The Lamp came ashore", 298.0, 168.0, 44, "Dawn, day 195: a shape of white-gold light walking up out of the sea's light under the mountains' end.", kind="lamp", until=46)
item("killed50", "The Antlered killed", "death", 229.5, 56.0, 50, "Day 228: four lions on its antlers, the earth closed on the bone between their roots. The first Titan killed.", realm=True, dx=0.3)
for _i, (_a, _b) in enumerate([((151, 48), (166, 66)), ((60, 150), (85, 128)), ((94, 70), (120, 84)), ((236, 196), (200, 202)), ((131, 118), (150, 112))]):
    titan(f"t3turn{_i}", 52, [_a, _b], "Days 239-240: all five turned from their kingdoms toward the hub, where the Oneroad's six ends meet.",
          name="The five turned to the hub" if _i == 0 else "", label=_i == 0, until=62, weight=0.6)
titan("t3sun53", 53, [(70, 124), (86, 113.5)], "Day 243: the Horned Sun came up the Sun Road behind Sarovel's column into the Vintner's Gate.", until=56, weight=0.7)
item("gate53", "The Sun turned back", "battle", 88.3, 112.0, 53, "Orrun and a shadow across the road; then the Lamp came down, and the Sun lowered its horn and went back.", realm=True, until=60, dx=0.3)
titan("t3coil56", 56, [(176.4, 66), (178.6, 80), (176.6, 92.5)], "Night 271: the Coil came down the upper Wend under black ice to below Eskby.", name="The Pale Coil came down the Wend", label=True, until=62, weight=0.7)
item("market58", "The floating market lifted", "flood", 183.4, 203.0, 58, "Day 285: the Bell came up the Wend's mouth and the stilt-warehouses went; five thousand two hundred lifted and towed upriver.", realm=True, until=63, dx=0.3)

# ---------------- the travellers ----------------
def route(id, pov, ch, pts, desc, name="", label=False, realm=True, **kw):
    return line(id, name, "route", ch, pts, desc, realm=realm, label=label, pov=pov, **kw)
route("m3a", "S", 7, [(175.0, 107.3), (190, 110), (215, 114), (238, 124), (253.8, 128.6), (264, 124)],
      "Days 10-18: over the Wend on Liss's rope, east by drove tracks across Saltreach's scrub and moor, over the Ysse at an old drove ford, to the clans.", name="Maren's road east", label=True)
route("m3b", "S", 11, [(253.6, 128.2), (236, 112), (206, 96), (178, 84.6)], "Days 26-47: west with ten thousand people and their herds at four leagues a day, to the ford under the Greenwold's oaks.",
      name="The clans' road west", label=True)
route("m3c", "S", 12, [(176, 84), (150, 80), (110, 66), (64.5, 46.5)], "To Ironhythe for the Accord.")
route("m3d", "S", 14, [(64, 47), (96, 72), (128, 104), (172, 107), (174.6, 107.4), (176, 150), (183, 196), (215, 197), (240, 178), (265, 187), (293, 178.5)],
      "Days 65-76: down the canal road, by Liss's ferry for Idony, down the Wend, along the coast and round Corsa to Blackwater, on Orrun's back.", name="To Blackwater on the lion", label=True)
route("m3e", "S", 21, [(294, 180), (290, 190), (270, 200), (245, 205), (P41[0] + 1, P41[1] - 1)], "Night 94: out through the broken chain into the Shatters' reef channels.", name="The Kittiwake sails", label=True)
route("m3f", "S", 24, [P41, pier(30), pier(20), pier(10), pier(2)], "Days 97-114: pier to pier south-west by the Merrin book's bearings.", realm=False)
route("m3g", "S", 25, [pier(2), pier(1), along(pier(1), 0.6), along(L, -1.2)], "Day 115: through the Needle at the top of the flood, into the lagoon.", realm=False)
route("m3h", "S", 27, [along(L, 0.3), along(L, 5), MH], "Days 123-125: up the paved road two days inland, awake, to the mountain on the hill.", realm=False)
route("m3i", "S", 34, [MH, (135.2, 285.0), HALL], "Days 137-138: with the Grey Mother south-west along the road to the hall on the ridge.", realm=False)
route("m3j", "S", 40, [along(L, -1.2), pier(1), pier(20), P41, (217.5, 202.6)], "Days 148-180: under the sea along the drowned road, the sea-bed's stone opening ahead of the lion and closing behind.",
      name="Under the sea", label=True)
route("m3k", "S", 46, [(217.5, 202.5), (205, 201), (184, 202), (181.5, 160), (179, 120), (177.5, 109.0)], "Days 181-191: ashore by the Saltings, west along the Coast Road, up the Wend's east bank to the camp.",
      name="The lion comes home", label=True)
route("m3l", "S", 49, [(177.8, 109.0), (190, 102), (205, 88), (222, 70), (228.5, 57.5)], "Days 208-224: with the clans, the lion's steps shortened to a man's, to the Thornwood's western edge.")
route("m3m", "S", 53, [(229, 57), (205, 82), (178, 96), (140, 108), (88.5, 112.5), (130, 109), (174.8, 103.6)],
      "Days 240-248: west over the Wend and across Hearthmere to the Vintner's Gate at the lion's own pace; then home to the eddy.", name="Maren's road home", label=True)
route("c3a", "F", 6, [(184.4, 94.8), (181.5, 130), (183, 195), (214, 197.5), (201, 201), (184.5, 203)], "Days 11-16: down the Wend with half the Clan's flights, west along the Coast Road through the toll gates.",
      name="Calder's road to the coast", label=True)
route("c3b", "F", 9, [(178.6, 101.4), (205, 140), (257.5, 191.0)], "Day 22: from the top field to Corsa.")
route("c3c", "F", 12, [(262, 192), (190, 140), (110, 80), (65, 47.5)], "Days 58-60: two days' flying north-west to the Accord at Ironhythe.", name="To the Accord", label=True)
route("c3d", "F", 15, [(65, 47.5), (130, 95), (200, 150), (260, 190)], "Back to Corsa from Ironhythe (day 67).")
route("c3e", "F", 22, [(262, 192), (210, 140), (191, 95.5), (187.6, 92.0)], "Days 89-98: Ulric's body home to Skarrow; the pour at Coldtarn.")
route("c3f", "F", 26, [(187.6, 92), (215, 140), (260, 186), (291.5, 179.5)], "Day 112: to Blackwater, to stop the Berths fleet.")
route("c3g", "F", 28, [(291, 181), (265, 205), P41, pier(30), pier(12)], "Days 118-127: over the Shatters with the Berths fleet at its pace, Jory on Aurveth's back reading the stones.",
      name="Over the Shatters", label=True)
route("c3h", "F", 32, [pier(12), pier(1), along(pier(1), 2.0, (-0.69, 0.72)), (147.6, 298.5), BAY, CROSS], "Days 128-139: towing two boats pier to pier; south along the shelf to the south bay; inland to the crossroads.", realm=False)
route("c3i", "F", 34, [CROSS, HALL], "Day 142: north-east to the Hall of Light.", realm=False)
route("c3j", "F", 42, [CROSS, along(L, -2), pier(30), P41, (205, 180), (195, 130), (189.4, 90.6)], "Days 149-150: home over the sea in a day and a night, Titan-class, to the hatching caves.",
      name="Calder flies home", label=True)
route("c3k", "F", 49, [(189, 91), (205, 80), (229, 58)], "Day 224: the air leaves the Wend for the Thornwood.")
route("c3l", "F", 58, [(176.0, 104.5), (176.5, 120), (182, 170), (183.5, 201.5)], "Days 278-285: the river watch on the lower Wend, then the lift at Wendmouth.")
route("u3a", "U", 8, [(49, 171), (60, 150), (70, 121), (75, 100), (68, 70), (63.5, 47)], "Days 25-45: three thousand of Sarovel's unchosen north by the Sun Road and the Kessmoor road to Ironhythe's works.",
      name="Tobin's road north", label=True)
route("g3a", "G", 10, [(174.0, 107.4), (155, 105), (129, 108), (139, 97), (152, 89), (165, 85), (176.5, 84.2)], "Days 30-38: to Hallowmere to sign the outlawry; then east by the Greenwold road to take the barricade down.",
      name="Rowan's road", label=True)
route("k3a", "M", 44, [along(L, -1.2), pier(1), pier(20), P41, (250, 205), (292, 181)], "Days 148-172: the Kittiwake home by day-sailing with ninety-three aboard.", name="The Kittiwake home", label=True)
line("bridle62", "The Bridle comes down the Iron Road", "route", 62, [(62.5, 45.5), (78, 58), (96, 72), (112, 90), (128, 108), (155, 105), (166, 106), (174.9, 103.8)],
     "Days 300-310: a hundred and eight flats in twenty-seven strings behind Kessmoor's road-engines, green lamps a league long.", realm=True, label=True, until=64, pov="bridle")
B.finish_routes()

# ---------------- the close-ups ----------------
# Part One: Lights over the Worldsend
item("dig1", "The dig", "rubble", 174.6, 106.1, 1, "Days 2-5: Orrun and two shadows lift the fallen stone off the north side of the heap, slab by slab: Tam's anvil, the yard engine with Dane under it, four iron chests.", dx=0.3)
item("lintel1", "The lintel held", "lion", 173.75, 106.65, 1, "Day 3: a cracked lintel going over the salvage crew; she holds it with nothing but Orrun's stone through her hand.", size=0.5, label=False)
item("ferryhouse3", "Liss's ferry house", "house", 174.15, 107.25, 0, "Cracked and standing at the foot of Greyhold's jetty, under the fallen hill.", dx=-0.3, until=52, keep=True)
item("davin3", "Davin writes for Idony", "scroll", 174.45, 107.65, 3, "Day 6: down the King's Road with the tribunes' letter; he stays and writes.", label=False)
item("crowncourt5", "The empty chair", "landmark_pt", 184.0, 95.5, 5, "Between the red thread's table and the grey's: the chief's chair under its cloth since Teo.", label=False)
item("gate6", "The toll gate at Sallow Bar", "roadblock", 201.0, 201.2, 6, "The Gaffer's gate on the bridge: a copper a head, a silver a cart. He gives the tin cup back for nothing.", dx=0.3)
item("topfield6", "Gullhaven's families in the top field", "camp", 179.2, 101.0, 6, "Days 17-20: the old, the children and the sick flown inland to Harrow's End's fallow farms.", label=False)
item("fords7", "The Ysse fords", "stones", 253.6, 128.2, 7, "Four drove fords from the Plains to the scrub; the lion and one shadow at a time raise sills under the water, and the stonehorns breast the current.", dx=0.3, realm=True, size=0.6)
item("ridge7", "The ridge of stone", "wall", 259.5, 131.5, 7, "Day 22: a ridge a quarter-league long comes up out of the plain and the beast-flood breaks on it.",
     path=[(258.8, 132.4), (260.2, 130.6)], label=True)
item("hall12", "The Accord of Ironhythe", "house", 62.6, 44.4, 12, "In the Hall of Measures under the clock that has never been wrong: the kingdoms unite, and Kessmoor's clause.", realm=True, dx=0.3)
item("merrin13", "The Merrin house", "house", 296.0, 178.6, 13, "One tall stilt-house with ochre shutters at the inlet's eastern end, a salvage hold under it on the water.", dx=0.3, keep=True)
item("reefstone13", "The reef-stone", "rubble", 293.6, 182.8, 13, "A block of old-realm stone the size of a chapel across the throat of the Merrins' channel, since the Bell woke.", dx=0.3, until=16)
item("terrace15", "The hulks on the ropewalk terrace", "house", 261.4, 190.9, 15, "Days 70-76: forty-one hulks lifted off the low harbour's mud for one copper and set down above the wave-mark.", dx=-0.4, keep=True)
item("lowharbour15", "The low harbour", "area_small", 262.6, 194.0, 15, "Inside the chain behind the deep quays, where Corsa's poor lived on hulks on the mud.", label=False)
item("lift17", "The reef-stone lifted", "lion", 293.3, 183.2, 17, "Night 84: Orrun and two shadows lift it out of the channel and set it on the reef's shoulder.", size=0.5, dx=0.3)
item("pens18", "The pens opened", "landmark_pt", 184.9, 95.6, 18, "Dawn, day 79: the oak bars drawn and burned. Any dragon that flies with the Clan flies by choice.", dx=0.3)
item("chain19", "Corsa's chain snaps", "wave", 262.6, 195.2, 19, "Day 88: the Bell's wall of water breaks the chain like thread; the Tidehall goes, and Ulric on its steps.", dx=0.3)
item("ulric19", "Where Ulric died", "death", 262.0, 194.0, 19, "On the Tidehall's sea-steps, handing a clerk's boy up to the dragons.", label=False)
item("berths20", "The Far Berths", "scroll", 295.6, 177.4, 20, "Posted on the boathouse door: passage to a land without Titans, three hundred gold a head.", dx=0.3)
item("boom21", "The boom broken", "lion", 297.0, 185.0, 21, "Night 94: the Kittiwake's stem parts the lashed join, and a stone lion out of the eastern headland holds the boom open.", size=0.5, dx=0.3)
item("pour22", "Ulric's ashes poured", "fire_plain", 187.4, 91.9, 22, "Day 98: \"Pour with me.\" Then the call: all three dragons turn their heads south-west.", label=False)
item("ward23", "The ward on Beacon Ridge", "battle", 136.6, 117.4, 23, "Noon, day 93: six hundred voices and a heartstone wagon; the ward holds for an hour. A third of Rowan's army dies.", dx=0.3)
item("mere23", "The Mere boils", "flood", 130.5, 117.6, 23, "Days 94-95: it walks through the empty city into the Mere and lies down in it.", dx=0.3)
item("bellroad24", "The Bell on the road", "sleeper", 199.0, 222.0, 24, "Day 104: a league off, a reef that isn't on the chart, going south-west along the road.", realm=False, until=25)
item("hal24", "Where Hal Merrin drowned", "death", *along(pier(9), 0.5, (0.69, 0.72)), 24, "The ninth milestone: Kit drops a pinch of salt in the sea.", label=False)
item("bell25", "The Bell at the road's end", "sleeper", 143.6, 267.2, 25, "It rose at the shelf's edge west of the Needle, and lay there after like an island.", until=40)
item("shadows25", "Two lions in the Needle", "lion", *along(pier(1), 0.6), 25, "Two shadows up out of the drowned causeway, passing the Kittiwake through the gap like a bucket.", size=0.5, label=False)
item("anchor27", "The Kittiwake's anchorage", "ship", *along(L, -1.4), 27, "A league off the shore in the clear lagoon. Never sleep ashore over there.", dx=0.3, until=44)
item("mother27", "The mountain on the hill", "titan", MH[0] + 0.6, MH[1] - 0.4, 27, "A great cat's shape the size of a hill, lying in the light. It knows him.", size=0.45, until=34, label=False)
item("fleet28", "The Berths fleet lost", "wave", *along(pier(12), 1.0, (0.69, 0.72)), 28, "Night 127: the Bell rose under the fleet near pier twelve. Nine ships of ten went down; ninety-four lived.", dx=0.3)
item("sim29", "Where Sim slept", "death", *along(L, 2.0), 29, "A quarter-league up the road: lying on the paving with his eyes open, smiling a little, not breathing.", label=False)
item("showed30", "What she showed", "scroll", MH[0] - 0.8, MH[1] + 0.8, 30, "Through Orrun: the one realm, the binding, the rising, the sleeping, and a young grey lion set at a door.", label=False)
item("script31", "The script in the light", "lamp", MH[0] + 0.6, MH[1] + 1.2, 31, "\"The gods are what is left of Titans who stopped.\"", dx=0.3)
item("wayfarer32", "The Wayfarer", "sleeper", CROSS[0] + 0.5, CROSS[1] + 0.3, 32, "A three-faced shape of light in the crossroads square: the god on Harrow's End's shrine. \"Because you have room.\"", until=39, dx=0.3)
item("piers32", "Piers Calloway", "death", BAY[0] + 1.5, BAY[1] - 0.8, 32, "He slept on the dunes out of contempt, and was found smiling at dawn.", label=False)
item("ring33", "The Bridle", "cage", 63.8, 47.4, 33, "In the Ring Yard: twelve heartstone engines joined by great chain, and a central ring with six hollows. Tam refuses to forge the ring.", dx=0.3, realm=False)
item("hall34", "Four elders", "lamp", HALL[0] + 0.6, HALL[1] - 0.6, 34, "The Grey Mother, the Wayfarer, the Lamp and the Lady. Two hands: the elders hear the two bonds only together.", dx=0.3)
item("gift37", "The lion becomes a Titan", "lion", HALL[0] + 1.2, HALL[1] + 0.4, 37, "Dawn, day 146: the Grey Mother's gift goes through the bond; she goes out like a lamp.", dx=0.3)
item("rocs38", "Rocs over the Saltings", "dragon", 238.0, 182.0, 38, "Yeva's roc-riders carry the Saltings' children inland.", size=0.6, dx=0.3)
item("surf38", "Lost in the Bell's surf", "death", 246.0, 186.0, 38, "Day 145: Ivo Brack and Sunniva and their dragons, caught low over the flats with full baskets.", label=False)
item("gift39", "Three dragons become Titan-class", "dragon", CROSS[0] - 0.4, CROSS[1] + 0.8, 39, "Dawn, day 147: the Wayfarer's gift three ways: white fire, deep sight, wind. The south-east milestone melts.", dx=0.3)
item("lady40", "The Lady keeps pace", "sleeper", 186.0, 222.0, 40, "In the black water beside the moving stone: something long and pale.", until=40)
item("camp41", "The Accord's camp", "camp", 177.8, 109.4, 41, "Three leagues below Greyhold's fallen hill on the Saltreach bank: sixty thousand from Hallowmere, ten thousand clansfolk, the coast.", dx=0.3, until=52, realm=True)
item("pontoon41", "Kessmoor's pontoon", "road", 175.2, 109.0, 41, "The new pontoon across the Wend by the camp.", path=[(174.6, 109.2), (175.8, 109.0)], label=False, until=75)
item("ashore43", "Orrun comes ashore", "lion", 218.6, 199.4, 43, "Day 181: a hill walking out of the sea onto the Coast Road; Redshank runs.", size=0.5, dx=0.3)
item("wall43", "The sea-wall rebuilt by hand", "wall", 219.8, 197.6, 43, "She could drop a cliff, so she does nothing small with the gift: the old woman's wall goes back stone by stone.",
     path=[(219.4, 197.8), (220.2, 197.5)], label=False)
item("threehills45", "The three hills", "dragon", 188.8, 91.3, 45, "Kharrak, Aurveth and Lisska on the moor round Coldtarn's rim, too big for the Roosts.", size=0.8, dx=0.3)
item("lady46", "The Lady in the Wend", "sleeper", 175.4, 109.6, 46, "Night 199: up the Wend from the sea; the river at the camp goes pale and stays pale.", until=63, dx=-0.4)
item("lamp46", "The Lamp at the muster", "lamp", 178.4, 108.0, 46, "Dawn, day 200: walking across the Wend on the light on the water; armies kneel.", until=63, dx=0.3)
item("sheds48", "The harvest sheds", "house", 61.0, 47.4, 48, "Where Kessmoor renders the beasts it buys for heartstone; a third of the hands sleep on the towpath instead.", dx=-0.4)
item("air49", "Fire in the forest", "fire", 228.4, 54.0, 49, "Days 225-227: white fire into a walking forest; Lisska's wind turning it back; rocs dropping stones.", dx=0.3)
item("gunna49", "Where Gunna and Tamsin died", "death", 228.6, 58.6, 49, "Under the walking wood, carrying the last Keepers out. Together.", label=False)
item("plates51", "Kessmoor's carts at the plates", "cage", 230.2, 57.2, 51, "Under the Accord's clause: matter, the find, the recovery. Nobody says heartstone. The Wyldmarch walks out.", dx=0.3)
for _i, (_x, _y, _nm) in enumerate([(228.5, 57.5, "the Thornwood"), (210, 72, "the border"), (191, 95, "Skarrow"), (184.4, 95.4, "Varrhold's gate"),
                                    (177.8, 109.4, "the camp"), (174.2, 106.4, "Greyhold's fallen hill"), (133.5, 117.0, "Sallow End on the Mere"), (175.3, 107.6, "the Staithe")]):
    item(f"glass{_i}", "The glass-line" if _i == 0 else "", "lamp", _x, _y, 52, f"A tide-glass logged every quarter-hour at {_nm}.", size=0.5, label=_i == 0, dx=0.3)
line("glassline", "", "sea", 52, [(228.5, 57.5), (210, 72), (191, 95), (184.4, 95.4), (177.8, 109.4), (174.2, 106.4), (133.5, 117.0)],
     "Noon, day 228: the Antlered's breath went down the line of glasses like a wave down a rope, to the one holding the end.", realm=True, until=53)
item("ramparts53", "The ramparts", "wall", 173.9, 104.3, 53, "Days 249-250: a league of grey stone across the Vale's floor on each bank, raised through the lion. Her right hand goes numb.",
     path=[(175.15, 104.45), (174.1, 104.25), (172.6, 104.15)], label=True, carry=True)
item("ramparts53b", "", "wall", 177.6, 104.6, 53, "The Saltreach bank's rampart.", path=[(176.55, 104.5), (177.8, 104.6), (179.4, 104.75)], label=False)
item("newferry53", "Liss's ferry house", "house", 174.85, 103.05, 53, "Above the new landing at the eddy on the Hearthmere bank, with her hay-barn, the Ferry Barn, where the council sits.", dx=-0.4, keep=True)
item("newrope53", "Liss's rope over the eddy", "road", 175.6, 103.1, 53, "Three-strand hemp from the camp's rope-walk, across the eddy.", path=[(175.0, 103.1), (176.6, 103.15)], label=False)
item("hubcamp53", "The camp at the eddy", "camp", 177.4, 105.6, 53, "The Accord moved six leagues up the Wend to the hub: ninety-eight thousand behind the walls.", dx=0.3)
item("hall54", "The hall under the tarn", "lamp", 186.1, 91.0, 54, "Through Aurveth's deep sight: straight lines in the rock under the western crag. Somebody kept something here, once.", label=False)
item("flat55", "The Ferry Flat", "area_small", 175.0, 103.65, 55, "The water-meadow at the eddy's edge, between the rampart's river end and the water: the Bridle's footings, twelve iron beds in a ring.", dx=-0.6)
item("jibs55", "The jibs", "cage", 175.25, 103.55, 55, "Six iron jib-posts on the eddy's edge for the chains to swing out over the water.", label=False, size=0.6)
item("ice56", "Black ice", "ice", 176.3, 90.0, 56, "Night 271: the Wend frozen from the Isvaren border to a little below Eskby in one night.", dx=0.3)
item("lady56", "The Lady drives the Coil back", "sleeper", 176.4, 91.2, 56, "Day 275: serpent and serpent: the first time the elders fight.", until=56, dx=0.3)
item("visitor57", "Corvin's visit", "lock", 174.75, 102.85, 57, "Midwinter night in Idony's back room: a man with a Kessmoor hand, asking for the right stroke.", label=False)
item("door59", "The hall's door opened", "lock", 186.4, 91.35, 59, "Day 295: fifty feet of scree slides into the shallows; a door of old-realm stone opens like a drawer. Three hundred and twelve places, and the floor.", dx=-0.5)
item("barges60", "Six thousand and twelve", "ship", 175.9, 110.0, 60, "Days 295-310: the Merrin barges and the free captains up eight leagues of winter river from the Sheepford, carrying for nothing.", dx=0.3)
item("eve61", "Eve, on the ferry", "meet", 175.8, 103.1, 61, "The night before the battle, mid-eddy on Liss's ferry: where the lion stands, where the dragons fly, where the people go if it fails.", dx=0.3)
item("bridleset62", "The Bridle set", "cage", 175.0, 103.75, 62, "Twelve engines banked and green-lit on the Ferry Flat; the ring in its cradle with its stage; sealed orders in every battery-master's coat.", dx=-0.5, until=75)
# the five arrive (day 317) and the battle (days 318-319)
for _id, _nm, _x, _y, _d, _u in [("lt63", "The Last Titan", 170.4, 104.0, "Two leagues west of the Hearthmere wall's end, lying facing the eddy.", 75),
                              ("coil63", "The Pale Coil", 176.3, 96.0, "Under the ice a league above the line.", 75),
                              ("bell63", "The Bell", 175.6, 112.6, "Two leagues below the line, the river white.", 75),
                              ("furn63", "The Furnace", 170.6, 99.0, "A ridge moving under the downs toward the Hearthmere bank's western end.", 65),
                              ("sun63", "The Horned Sun", 182.0, 107.2, "On the hills a league south of the Saltreach wall's east end, half a league of day.", 75)]:
    item(_id, _nm, "sleeper", _x, _y, 63, f"Day 317: {_d}", until=_u, dx=0.3)
item("wards63", "Two wards", "label", 173.0, 105.4, 63, "Noon: a hundred and six thousand voices, \"Keep the watch\", and two pale domes over the line, one each bank, fed by the elders' light.", dx=0.2)
item("lions64", "Stone lions in the wall", "lion", 172.8, 104.6, 64, "Along a league of the Hearthmere wall's face, hundreds of horse-sized stone lions bracing it against the Furnace's push.", size=0.5, dx=0.3)
item("sunfight64", "Kharrak against the Horned Sun", "fire", 180.4, 106.0, 64, "White fire across a league between the Sun and the Saltreach ward, all day.", dx=0.3)
item("furnace65", "The Furnace quenched", "death", 174.8, 103.9, 65, "Day 318: up under the batteries; the chilled chains hold it and the Lady pulls it into the Wend. The first destroyer of the battle killed.", dx=-0.5)
item("standword66", "A league of bank stopped", "battle", 176.9, 104.1, 66, "Evening: the stand-word into the Saltreach bank with a Titan behind it; then ridges up and the earth open.", dx=0.3)
item("baskets67", "The wounded flown out", "dragon", 181.5, 98.5, 67, "Night 318: eight hundred and sixty to Varrhold and the hatching caves, in a sky in layers.", size=0.6, dx=0.3)
item("glimpse68", "\"We've got it.\"", "meet", 175.9, 103.4, 68, "Day 319: the Last Titan down in the eddy under Orrun's forefoot; Aurveth's sight and Orrun's hold through two bonds; the Lamp's horn at the coal.", dx=0.3)
item("shallows68", "The Kingfisher Shallows", "area_small", 175.75, 105.4, 68, "The gravel flats a league below the eddy, where the Lamp held the Horned Sun down.", dx=0.3)
item("stage69", "The Bridle's stage", "lock", 174.95, 103.6, 69, "On the hour: a man in a grey drover's coat takes off his hood on the stage. Corvin.", label=False)
item("smoke70", "The hour", "smoke", 175.4, 104.3, 70, "Noon, day 319: the packets opened without Rowan's word; the jibs swing, bolts into the Lamp, honey-smoke over the whole line.", dx=0.3)
item("brake71", "Where Tobin died", "death", 174.5, 103.95, 71, "On the hub battery's brake, the forty engines held facing the line.", dx=-0.4)
item("road72", "A road of fire", "fire", 177.3, 103.3, 72, "Kharrak's white fire across the gap, to hold the road north open, not to kill.", dx=0.3)
item("rowan73", "Where Rowan fell", "death", 174.3, 104.9, 73, "Holding the gap with the knights, bonded and unbonded together, Haverly's edge in her hand. On the gate, there is no bond.", dx=-0.4)
item("corvin74", "Where Corvin died", "death", 175.95, 103.7, 74, "On the Last Titan's back at the coal: old magic took him whole, and Callis with him.", dx=0.3)
item("hub75", "The middle of the world breaks", "titan", 175.8, 103.5, 75, "The Last Titan tears the hub open where the island was; the river pours in; every horizon lights.", size=0.6, dx=1.0)
item("herd75", "The herd-charm", "route", 178.4, 102.2, 75, "With three Titan-class dragons behind it: a broken army turns north like a herd behind its lead cow.",
     path=[(177.2, 104.6), (178.0, 103.0), (178.6, 101.8)], label=True)
item("down76", "Where the Lady and the Bell went down", "sleeper", 176.4, 116.0, 76, "Dawn, day 320, seen from the Kittiwake's masthead at the Sheepford: four leagues below, in the sea come up the drained bed.", dx=0.3)
item("aground76", "The Kittiwake aground", "ship", 176.0, 112.4, 76, "Run aground on the Saltreach shingle when the river ran backwards.", dx=0.3)
for _i, _pts in enumerate([[(177.4, 106.0), (178.4, 104.0), (179.0, 101.8)], [(178.6, 106.2), (180.0, 103.6), (179.3, 101.6)],
                           [(176.3, 105.6), (176.9, 104.0), (178.7, 101.9)], [(173.8, 105.2), (175.6, 103.4), (177.0, 103.1), (178.9, 101.7)],
                           [(171.0, 104.0), (175.6, 103.5), (178.8, 101.8)], [(181.5, 107.0), (180.5, 104.0), (179.3, 101.7)]]):
    line(f"sixroads{_i}", "Six roads north" if _i == 0 else "", "route", 77, _pts, "One of the six roads north, a Titan shadow walking beside its people.", realm=False, label=_i == 0, until=78)
item("orrunway77", "Orrun across the Way", "lion", 179.1, 101.5, 77, "At the Fellwood's foot, where the six roads have become one, facing his kin.", size=0.6, dx=0.3)
item("kharrak78", "Where Kharrak died", "death", 178.85, 101.25, 78, "On the Fenn top field, across the Way, holding the Horned Sun off the last wagon. \"I held it.\"", dx=0.3)
item("salt79", "Salt on the tongue, nothing owed", "landmark_pt", 186.6, 91.8, 79, "Kit at the hall's door with the last of her salt: a contract with no price.", label=False)
item("gannet79", "Where Gannet died", "death", 187.0, 92.0, 79, "\"Kit. Catch.\"", label=False)
item("count80", "Four hundred and seventy-three", "label", 185.9, 91.6, 80, "Counted in at dusk, and the hold rune cut into the roof-stone by two hands.", dx=0.2)
item("lisska81", "Where Lisska fell", "death", 188.2, 90.8, 81, "She held the surge-storm off the last climbers with all her wind, then fell into the tarn with Wren's ribbon on her horn.", dx=0.3)
item("aurveth81", "Where Aurveth lay down", "death", 187.2, 92.2, 81, "Across Hollow Beck's mouth, taking the Pale Coil's cold and weight until the climbers were in. \"Ennis.\"", dx=0.3)
item("breaths82", "Breaths going out", "lamp", 186.2, 91.9, 82, "On the hall's floor, three glasses: the Sun, the Coil, the Lady, the Bell. One left.", label=False)
item("door83", "The door kept", "rubble", 186.5, 91.7, 83, "Orrun brings the mountain down on his kin and himself: the last great one lay down below the stone.", dx=-0.4)
item("orrun83", "Where Orrun died", "death", 186.8, 92.2, 83, "Keeping the door.", label=False)
item("firstlight84", "The bond went quiet", "label", 188.6, 93.4, 84, "At first light, every bonded pair at once. Nobody died of it.", dx=0.2)
item("pour85", "Empty hands poured", "landmark_pt", 187.5, 92.4, 85, "From the new shore: everyone holding out empty hands over the black water and turning them over.", dx=0.3)
item("fire86", "The first fire", "fire_plain", 187.2, 92.4, 86, "Tam strikes it with flint on the third strike: no charm, no beast.", label=False)
item("elemental86", "Something small, of stone", "landmark_pt", 186.7, 91.9, 86, "On the scree below the door, a small grey thing moves by itself, changes shape, and is gone. She didn't count them.", dx=-0.4, size=0.6)

B.ITEMS.sort(key=lambda i: i["ch"])
