"""Book 2 (The Hunt Beneath): the chapter-end maps.

Every chapter ends on a page like Book 1's: the whole of Winshire on top, a close-up below centred on the chapter's
"Ends at" place (Book 2/Chapter_Plan.md, checked against the drafted chapters), and what's new beside it.
Chapter 0 is the front-matter page: everything known at the end of Book 1.
Positions are leagues (x east, y south). Places named here that world.py doesn't have, and every event, are
working proposals; NOTES.md lists the places with their reasons.
"""
import math
import world as Wd
import marches_items as MI
from bookdata import Book, MARCHES as M

B = Book(2, "Book Two")
B.start_from_book1(MI)
item, line, place, chapter = B.item, B.line, B.place, B.chapter

# ---------------- what Book 1 leaves on the land ----------------
_KEEP1 = {"ferriby", "penfold", "littleweir", "kettle", "ramshead", "roosts", "mill", "shrine", "weirs", "eelweir",
          "skarrow16", "hobshole", "teosford", "knowe67", "gallowsoak", "moot", "shrine_rr"}
for _it in MI.ITEMS:
    if _it["id"] in _KEEP1:
        _c = dict(_it, ch=0, realm=False, until=None, size=1.0, carry=True, views=None, weight=1.0, head=True, pov=None)
        _c["keep"] = True
        B.ITEMS.append(_c)
# The hatching caves: on Coldtarn's bowl, across the tarn from the crag where the hall is (Book 3 ch 59, 85),
# six leagues from Varrhold (Book 2 ch 12, 52): "above Coldtarn", as Book 1 has it. Book 1's map uses the same point.
item("caves", "The hatching caves", "cave", 189.6, 89.9, 0,
     "The Clan's old hatching caves on Coldtarn's eastern rim, warm rock round a spring that never freezes. The Fenns winter here.", carry=True, keep=True, dx=0.3)

B.KINGDOM_LABEL_AT = {"isvaren": (176.0, 24.5), "wyldmarch": (268.0, 31.0)}
B.LINGER = 10                     # events fade from the map ten chapters on; deaths, houses, walls, roads, the Titan's road and the sleepers stay
B.LASTING_KINDS = ("death", "house", "wall", "road", "sea", "track", "sleeper", "cave")   # clear of Vael and the Long Library, which Book 1 never named
B.HIDE["oldruin"] = 0          # the island and the Ruin went into the river at the end of Book 1
place("eddy", "where the island was", "landmark", "marches", 175.8, 103.5, 0,
      "Where the Old Ruin's island stood until the night of the locks: the river turns there now in a slow, wide eddy over the drowned stones, opposite cracked Redwatch, three and a half leagues above Greyhold.",
      scope="marches", ldx=1.6, ldy=-1.0)

# ---------------- the chapters ----------------
# n, POV, title, Ends at (the plan's column), (centre), scale (M = the Marches view; else px per league), cartouche title, cartouche subtitle
T = 20     # a town and its country
N = 12     # a district
R = 7      # a kingdom
W = 5.5    # half the realm
chapter(0, "", "", "Before the story begins", (179.0, 104.0), M, "The Marches", "As Book One ends")
_CH = [
    (1, "S", "The Reeds", "The reeds below Redwatch", (175.0, 104.0), M, "The Marches", "The reeds below Redwatch"),
    (2, "F", "The Ferry House", "Liss's ferry house, Greyhold landing", (174.3, 106.8), M, "The Marches", "Liss's ferry house, Greyhold landing"),
    (3, "R", "The Glasses", "Vael, the Long Library", (151.5, 37.0), T, "Vael", "The Long Library"),
    (4, "S", "The Black Book", "Greyhold; the cavern", (174.3, 106.0), M, "The Marches", "Greyhold and the cavern below"),
    (5, "F", "The Herald", "Greyhold landing", (174.3, 106.8), M, "The Marches", "Greyhold landing"),
    (6, "S", "Sour Water", "Greyhold; the Wend at night", (174.6, 106.4), M, "The Marches", "Greyhold and the Wend at night"),
    (7, "F", "The Drover's Way", "The Drover's Way; Ewe Hollow", (179.5, 103.5), M, "The Marches", "The Drover's Way and Ewe Hollow"),
    (8, "R", "Second Ring", "Vael; the road to the Wyldmarch", (192.0, 45.0), R, "Isvaren", "Vael and the road east"),
    (9, "S", "The Titan's Road", "The Fellwood, Saltreach bank", (181.5, 101.5), M, "The Marches", "The Fellwood, on the Saltreach bank"),
    (10, "F", "Arn's Yard", "Varrhold", (184.4, 95.5), M, "The Scarfell", "Varrhold"),
    (11, "S", "The Scarfell's Edge", "The Scarfell's edge", (185.6, 97.0), M, "The Scarfell", "The Scarfell's edge, above the Fellwood"),
    (12, "F", "The Empty Chair", "The Drover's Way south", (181.5, 104.5), M, "The Marches", "The Drover's Way south"),
    (13, "S", "The Thornwood", "The Thornwood", (252.0, 62.0), N, "The Wyldmarch", "The Thornwood"),
    (14, "F", "Cotter's Cross", "Cotter's Cross", (180.5, 112.0), M, "The Marches", "Cotter's Cross"),
    (15, "S", "The Hallow Plains", "The Hallow Plains", (246.0, 84.0), N, "The Wyldmarch", "The Hallow Plains"),
    (16, "R", "Sleepwood", "The Hollow Ring", (260.0, 67.0), T, "The Thornwood", "The Hollow Ring"),
    (17, "F", "The Ledger", "Varrhold; the hatching caves", (186.5, 93.0), M, "The Scarfell", "Varrhold and the hatching caves"),
    (18, "S", "The Hollow Ring", "The Hollow Ring", (260.0, 67.0), T, "The Thornwood", "The Hollow Ring"),
    (19, "F", "Skarrow", "Skarrow", (188.5, 96.0), M, "The Scarfell", "Skarrow"),
    (20, "S", "Midsummer Night", "The Hollow Ring", (260.0, 67.0), T, "The Thornwood", "The Hollow Ring, midsummer night"),
    (21, "F", "The Roosts", "The Roosts", (185.8, 93.5), M, "The Scarfell", "The Roosts"),
    (22, "R", "The Surge", "Lake Ysse", (254.0, 84.0), N, "The Wyldmarch", "Lake Ysse"),
    (23, "S", "Under the Stones", "Under the Hollow Ring", (260.0, 67.0), T, "The Thornwood", "Under the Hollow Ring"),
    (24, "F", "The Black Tarn", "Coldtarn", (187.0, 92.5), M, "The Scarfell", "Coldtarn"),
    (25, "S", "The Moot", "Kethra's Moot, Lake Ysse", (252.5, 81.5), T, "The Wyldmarch", "Kethra's Moot, Lake Ysse"),
    (26, "F", "Westward", "Harrow's End, the Fenn top field", (179.0, 101.5), M, "The Marches", "Harrow's End, the Fenn top field"),
    (27, "R", "The Drain", "The Wyldmarch, riding west", (210.0, 82.0), W, "The North", "The Wyldmarch, riding west"),
    (28, "S", "The Tusker Road", "Vael's gate, under the High Crown", (165.0, 36.0), N, "Isvaren", "Vael's gate, under the High Crown"),
    (29, "R", "Home Water", "Vael; Glasswater", (150.5, 40.5), T, "Vael", "Vael and Glasswater"),
    (30, "F", "Wendmouth", "Wendmouth; the Halloran mint", (184.0, 192.0), T, "Wendmouth", "The Halloran mint"),
    (31, "R", "The Oldest Roll", "The Long Library", (151.5, 37.0), 24, "Vael", "The Long Library"),
    (32, "S", "Door-Keeper", "The Long Library", (151.5, 37.0), 24, "Vael", "The Long Library"),
    (33, "F", "The Iron Fells", "The Iron Fells", (162.0, 50.0), N, "The Iron Fells", "The hunters' pass"),
    (34, "S", "What the Bird Remembers", "The Long Library", (151.5, 37.0), 24, "Vael", "The Long Library"),
    (35, "F", "Starwatch", "Starwatch", (157.0, 44.0), T, "Isvaren", "Starwatch"),
    (36, "R", "The Great Binding", "Vael; the Undercroft", (150.5, 39.5), 24, "Vael", "The Undercroft"),
    (37, "S", "Glasswater", "Glasswater; lower Vael", (150.5, 41.0), 24, "Vael", "Glasswater and lower Vael"),
    (38, "F", "The Library Hill", "The Library hill", (151.5, 38.0), 24, "Vael", "The Library hill"),
    (39, "R", "The Long Library", "The Long Library", (151.5, 37.0), 24, "Vael", "The Long Library"),
    (40, "S", "Cinders", "The Library steps", (151.5, 37.0), 24, "Vael", "The Library steps"),
    (41, "F", "The Milestones", "The Glasswater shore", (150.5, 41.0), 24, "Vael", "The Glasswater shore"),
    (42, "S", "The Iron Road", "The Coldrun canals; the Scald cordon", (96.0, 52.0), R, "Kessmoor", "The Coldrun canals and the Scald"),
    (43, "F", "The Flood", "The Wend in flood; Greyhold landing", (170.0, 84.0), 8.5, "The Wend", "The Wend in flood"),
    (44, "R", "Heartstones", "Kessmoor's engine-houses", (94.0, 68.0), 12, "Kessmoor", "The Scald's engine-houses"),
    (45, "S", "The Scald", "The Scald", (94.0, 68.0), 12, "Kessmoor", "The Scald"),
    (46, "F", "The Crown's Square", "Hallowmere", (130.0, 108.0), T, "Hearthmere", "Hallowmere"),
    (47, "R", "The Chain-Ends", "The Scald", (94.0, 68.0), 12, "Kessmoor", "The Scald"),
    (48, "S", "Chilled Water", "The Scald cordon", (94.0, 68.0), 12, "Kessmoor", "The Scald cordon"),
    (49, "F", "Corsa", "Corsa", (250.0, 184.0), T, "Saltreach", "Corsa"),
    (50, "R", "Envoys", "The Scald; the envoys' camp", (93.0, 68.0), 12, "Kessmoor", "The Scald and the envoys' camp"),
    (51, "S", "Midwinter", "Orrin's ruins", (94.0, 67.0), 12, "Kessmoor", "Orrin's ruins"),
    (52, "F", "Wren's Letter", "The hatching caves, Varrhold", (187.0, 92.5), M, "The Scarfell", "The hatching caves"),
    (53, "S", "The Basin Floor", "Under the Scald", (94.0, 68.0), 12, "Kessmoor", "Under the Scald"),
    (54, "F", "The Song", "Varrhold", (183.5, 99.0), M, "The Marches", "Varrhold and the Cotter's Cross road"),
    (55, "S", "The Sun Road", "The Sun Road; Solenne", (72.0, 130.0), R, "Sarovel", "The Sun Road to Solenne"),
    (56, "F", "Blackwater", "Blackwater", (292.0, 180.0), T, "Saltreach", "Blackwater"),
    (57, "S", "The Unicorn", "The Elderwood", (50.0, 156.0), T, "Sarovel", "The Elderwood"),
    (58, "R", "The Grace", "Solenne, the palace", (50.0, 172.0), 24, "Solenne", "The palace"),
    (59, "F", "The Coast", "The Drowned Bell reef", (218.0, 192.0), 12, "Saltreach", "The Drowned Bell reef"),
    (60, "S", "The Sun Stair", "The Sun Stair", (50.0, 174.0), 24, "Solenne", "The Sun Stair"),
    (61, "R", "The Collar", "Solenne, the royal stair", (50.0, 174.0), 24, "Solenne", "The royal stair"),
    (62, "F", "The Young Ones", "The hatching caves, Varrhold", (187.0, 92.5), M, "The Scarfell", "The hatching caves"),
    (63, "S", "Solenne", "Solenne; Sorrel Isle", (52.0, 178.0), T, "Solenne", "Solenne and Sorrel Isle"),
    (64, "F", "The Reef", "Gullhaven", (217.0, 191.0), 12, "Saltreach", "Gullhaven"),
    (65, "S", "The Map", "Sorrel Isle lighthouse", (54.0, 180.0), 24, "Solenne", "Sorrel Isle lighthouse"),
    (66, "F", "Two Roads", "Gullhaven", (217.0, 191.0), 12, "Saltreach", "Gullhaven"),
    (67, "S", "Hallowmere", "Hallowmere", (110.0, 128.0), 9, "Hearthmere", "Hallowmere"),
    (68, "F", "The Tide Council", "Corsa", (255.0, 184.0), T, "Saltreach", "Corsa"),
    (69, "S", "Greyhold", "Greyhold", (174.5, 105.5), M, "The Marches", "Greyhold"),
    (70, "F", "Gullhaven", "Gullhaven", (218.0, 192.0), 12, "Saltreach", "Gullhaven"),
    (71, "R", "The Ship", "The Saltings (Corvin's ship)", (240.0, 186.0), 7.5, "Saltreach", "The Saltings"),
    (72, "S", "The Marches", "The Marches; Greyhold landing", (175.0, 103.0), M, "The Marches", "The Marches, Greyhold landing"),
    (73, "F", "The Bell", "The Drowned Bell reef", (218.0, 193.0), 12, "Saltreach", "The Drowned Bell reef"),
    (74, "S", "One Hour of Light", "Greyhold landing", (174.5, 105.0), M, "The Marches", "Greyhold landing"),
    (75, "F", "Marked Roofs", "Gullhaven spit", (217.0, 197.0), 24, "Gullhaven", "The spit"),
    (76, "R", "The Eddy", "The eddy where the island was", (175.8, 103.8), M, "The Marches", "The eddy where the island was"),
    (77, "S", "The Old Stair", "The older stair", (174.0, 105.5), M, "The Marches", "The older stair"),
    (78, "F", "Ashes on the Saltings", "The Saltings; the flight home", (200.0, 150.0), W, "Saltreach", "The Saltings and the flight home"),
    (79, "S", "The Last Crossing", "Greyhold landing", (174.5, 106.0), M, "The Marches", "Greyhold landing"),
    (80, "F", "The Trap", "Greyhold's hill and the river", (174.8, 105.5), M, "The Marches", "Greyhold's hill and the river"),
    (81, "S", "Below the Chains", "The cavern under the river", (175.0, 105.0), M, "The Marches", "The cavern under the river"),
    (82, "F", "Fire Underground", "The cavern", (175.0, 105.0), M, "The Marches", "The cavern"),
    (83, "R", "The Cellars", "The Greyhold cellars", (174.3, 106.0), M, "The Marches", "The Greyhold cellars"),
    (84, "S", "The Held Breath", "The deepest vault", (174.6, 105.5), M, "The Marches", "The deepest vault"),
    (85, "F", "Up Through the Rock", "The river; up through the rock", (175.0, 106.0), M, "The Marches", "The river, and up through the rock"),
    (86, "S", "The Hill", "Liss's ferry house", (174.5, 106.5), M, "The Marches", "Liss's ferry house"),
    (87, "R", "The Last Chart", "Liss's ferry house", (177.0, 103.5), M, "The Marches", "Liss's ferry house"),
    (88, "F", "The Account", "The Scarfell; the hatching caves", (186.0, 93.0), M, "The Scarfell", "The Scarfell and the hatching caves"),
]
for _c in _CH:
    chapter(*_c)

# Gullhaven's shingle spit and the Drowned Bell's reef are in world.py's coastline now (canon, Oct 2026)
B.EXTRA_ISLANDS = []
item("reef", "The Drowned Bell's reef", "rubble", 217.5, 202.6, 59, "A long low black reef two leagues off the spit's end, dry at low springs; at the lowest tides a sound like a bell comes off it.",
     label=False, size=0.8, carry=True)

# ---------------- places Book 2 names that world.py doesn't have ----------------
place("coldrunlocks", "Coldrun Locks", "town", "kessmoor", 92.0, 38.0, 42,
      "The lock-town at the head of Kessmoor's canals, where the Coldrun is canalised down to Ironhythe: brick lock-houses, iron lift-bridges, green alchemical lamps, and the guild-house where beasts are papered.",
      scope="local")
place("orrin", "Orrin's ruins", "landmark", "kessmoor", 93.6, 65.4, 45,
      "The north end of the old town of Orrin, outside the cordon's bank where the fused glass stops: roofless stone houses, a chapel with a hearthstone, a well.",
      scope="local")
place("wendhead", "Wendhead", "village", "isvaren", 171.6, 61.0, 43,
      "Where Glasswater's valley comes down to the Wend: a stone bridge and a mill at the valley's foot.", scope="local")
place("craysford", "Cray's Ford", "village", "isvaren", 176.0, 64.6, 43, "A ford-village on the upper Wend, Isvaren side.", scope="local")
place("lowfold", "Lowfold", "village", "isvaren", 176.6, 66.9, 43, "The last Isvaren village on the upper Wend.", scope="local")
place("brookend", "Brookend", "village", "hearthmere", 175.4, 76.0, 43, "A Hearthmere river village on the middle Wend.", scope="local")
place("sallowlock", "Sallow Lock", "village", "hearthmere", 174.9, 84.0, 43, "A Hearthmere river village with a lock, on the middle Wend.", scope="local")
place("scarfelledge", "The Scarfell's edge", "landmark", "saltreach", 186.4, 97.3, 11,
      "The escarpment along the Fellwood's northern side. Here the old drove track tops it, three leagues south-east of Varrhold and two east of the Way, with the falls on Hollow Beck and the Way in sight below.",
      scope="marches", ldx=0.4, ldy=0.6)

# ---------------- the whole of Winshire: when names first appear in Book 2 ----------------
B.REALM_REVEAL.update(vael=3, longlibrary=3, thornwood=8, worldsend=13, hallowplains=13, candledowns=14, kethra=22,
                      corsa=30, fellscamp=33, starwatch=33, scald=41, ironhythe=42, gearmouth=42, solenne=47,
                      gullhaven=49, saltings=49, highcrest=55, blackwater=56, sorrel=63, stillhaven=68)
B.SECRET_REVEAL.update(catacombs=0, hollowring=20, isv_temple=36, kess_temple=41, sar_temple=41, drownedbell=54)
B.REALM_LABEL_REVEAL.update({"The High Crown": 8, "Ysse": 22, "The Iron Fells": 33, "Coldrun": 42, "Gilt": 47,
                             "The Ashlings": 14, "The Western Deep": 50, "Sunward Hills": 55, "Elderwood": 57, "Meryl": 68,
                             "The Greenwold": B.LATER, "The Saltings": 49, "The Hallow Plains": 13, "The Thornwood": 8,
                             "The Candle Downs": 14, "The Fellwood": 0, "The Wendwood": 0, "The Brackenwood": 0,
                             "The Worldsend": 13})
B.REALM_ROAD_REVEAL.update({"The Vael Pass": 28, "The Iron Road": 42, "The Sun Road": 55})
B.HIDE["greyhold"] = 85
place("greyholdfallen", "Greyhold, fallen", "ruin", "hearthmere", 174.0, 106.6, 85,
      "Greyhold's hill fell in on the afternoon of day 355, when the cavern under it collapsed: the north tower, the yard and the split inner wall went down into the hill, and the river wall slid into the Wend.",
      scope="both", ldx=-1)

# ---------------- the Last Titan's road ----------------
TR = "The Last Titan's road"
def titan(id, ch, pts, desc, name=TR, label=False, **kw):
    return line(id, name, "track", ch, pts, desc, realm=True, label=label, carry=False, **kw)

titan("t01", 9, [(175.8, 103.5), (179.5, 100.6), (183.5, 97.6), (187.5, 94.5)],
      "Sunrise, day 0: the Titan flew low north-east out of the river, laying the Fellwood flat in a league-wide swath.", label=True)
titan("t02", 13, [(187.5, 94.5), (205, 84), (228, 70), (248, 60), (259, 66.6)],
      "It lay down on the Hollow Ring, the clans' sacred stones deep in the Thornwood, and didn't move all spring.")
titan("t03", 20, [(259, 66.6), (250, 66.0)], "Midsummer night: it rose with the Ring's relic and flew west, low over the Thornwood.", name="It flew west", label=True)
titan("t04", 27, [(250, 66.0), (236, 55), (214, 60), (196, 53), (174, 46.5), (151.5, 42.3)],
      "Two weeks west and wandering; then north-west, and down on Glasswater under Vael (days 98-118).")
titan("t05", 37, [(151.5, 42.3), (138, 34), (118, 30)], "Dawn, day 173: up off the broken ice and west along the snow-line.", name="It flew west", label=True)
titan("t06", 42, [(118, 30), (103, 33), (97, 41), (105, 47), (99, 57), (94.5, 66.5)],
      "Circling over the Coldrun's head and the moors; south on day 197; down on the Scald on day 201.")
titan("t07", 45, [(94.5, 66.5), (72, 62), (44, 60)], "Day 233: up off the Scald with the egg in its back, west toward the Western Deep.")
titan("t08", 50, [(44, 60), (18, 63), (-3, 66), (-7, 74), (-1, 79), (2, 71)],
      "Out past Gearmouth over the Western Deep, circling, as if waiting for something to grow in it.", name="Circling the Western Deep", label=True)
titan("t09", 58, [(2, 71), (-1, 100), (9, 138), (30, 156), (50.5, 166.5)],
      "Day 287 it swung in toward the south-west coast; day 290 it came in over Sarovel; then it lay on the hills above Solenne's palace.")
titan("t10", 61, [(50.5, 166.5), (49.5, 173.5), (43, 160), (35, 150)], "Noon, day 315: down through the palace onto the Sun Stair for the egg, then up off the cliff and away north-west.")
titan("t11", 71, [(208, 128), (222, 160), (231, 180), (224, 198), (219.5, 206)],
      "Day 345: over the Saltings from the north, low, and out to sea; it lay down beyond the reef's breakers to wait for the tide.", name="Over the Saltings", label=True)
titan("t12", 75, [(217.6, 203.1), (223, 199.5), (229, 186), (216, 150), (205, 128)],
      "Day 349: up out of the sea by the Saltings and away north over the Ashlings. Going home.")
titan("t13", 78, [(205, 128), (186, 124), (166, 123)], "It lay down on the downs south-west of the Marches, over the river.")
titan("t14", 80, [(166, 123), (170.5, 112), (174.7, 105.4)], "Sunrise, day 355: down onto the Wend half a league above Greyhold.", name="It came down", label=True)
titan("t15", 82, [(174.7, 105.4), (175.4, 104.4), (175.8, 103.6)], "Free of the cage, it walked back up the river to the eddy and went down into it.")
titan("t16", 87, [(175.8, 103.5), (181, 98), (186, 93), (190.2, 88.8)], "Up out of the Ruin's end of the cavern and onto the Scarfell above the hatching caves.")
titan("t17", 88, [(190.2, 88.8), (215, 86), (250, 84), (288, 82)], "Day 362: the six went up together off the Scarfell and flew east toward the Worldsend.",
      name="The six flew east", label=True, weight=1.3)
for _i, (_a, _b) in enumerate([((236, 76), (193.5, 88.0)), ((166, 64), (187.0, 86.5)), ((142, 92), (186.2, 89.8)),
                                ((192, 136), (190.2, 91.6)), ((214, 132), (192.0, 91.0))]):
    line(f"five{_i}", "The five came" if _i == 0 else "", "track", 88, [_a, _b], "Days 360-361: out of five quarters, the five came to the Last Titan on the Scarfell.",
         realm=True, label=_i == 0, weight=0.6, until=88)

# where each sleeper woke (sleep relic taken, then the waking)
def sleeper(id, name, x, y, ch, desc, **kw):
    return item(id, name, "sleeper", x, y, ch, desc, realm=True, **kw)
sleeper("antlered", "The Antlered rose", 252.5, 78.6, 25,
        "Day 105: the Thornwood's sleeper rose at the forest's southern edge north of the Moot, antlered like a winter wood, and the forest walked with it.")
sleeper("coil", "The Pale Coil rose", 151.0, 44.6, 37, "Day 177: Glasswater's sleeper, a serpent of cold, rose through the ice and went down the valley in fog, and the lake went after it.")
sleeper("furnace", "The Furnace rose, and was caged", 95.6, 69.2, 48, "Day 238: the Scald's sleeper came up molten through the glass, and Kessmoor's cage closed on it.")
sleeper("hornedsun", "The Horned Sun rose", 46.0, 178.2, 61, "Day 317: the palace cliff broke into the bay and the sleeper under the Sun Stair rose, white-gold, horned like a unicorn the size of a hill.")
sleeper("bell", "The Bell rose", 220.0, 205.5, 75, "Day 349: the reef was its back. It rose out of the drained bay and went down into the deep water, and the wave came.")

# ---------------- the travellers ----------------
def route(id, pov, ch, pts, desc, name="", label=False, realm=True, **kw):
    return line(id, name, "route", ch, pts, desc, realm=realm, label=label, pov=pov, **kw)

# Maren
route("m06", "S", 6, [(174.3, 106.9), (175.0, 107.3)], "Night 8: Liss ferries the Fenns over in the dark; the greys and the lion swim.", realm=False)
route("m09", "S", 9, [(175.0, 107.3), (177.8, 105.2), (180.0, 103.6), (182.6, 101.4), (184.6, 99.6)],
      "North through the Fellwood by the charcoal-burners' tracks, two leagues east of the Way.", name="Maren's road north", label=True)
route("m11", "S", 11, [(184.6, 99.6), (185.7, 98.3), (186.4, 97.3)], "Out of the trees and up the old drove track onto the moor.")
route("m13", "S", 13, [(186.4, 97.3), (200, 96), (222, 94), (233, 86), (240, 72), (240.5, 64.5)],
      "East off the Scarfell, over the moor and the Hallow Plains (day 24), into the Thornwood (day 31) and the Barrows.", name="Maren's road east", label=True)
route("m15", "S", 15, [(240.5, 64.5), (236.5, 82.5)], "Out to the Speaking Stones for the elders (day 45).")
route("m18", "S", 18, [(236.5, 82.5), (245, 77.5), (252, 72.5), (256.5, 69), (259.4, 67.3)], "Into the grey from the south along a stream (days 69-74).")
route("m22", "S", 22, [(260, 67), (257.5, 73), (254.5, 77.5), (252.5, 80.8)], "South with Idony and Hesper to warn the clans at the Moot (days 102-103).", name="To the Moot", label=True)
route("m28", "S", 28, [(252, 81.4), (240, 76.5), (223, 68), (212, 42), (198, 31), (176, 29), (160, 32), (151.2, 39.8)],
      "West over the dead Plains, north into the foothills, then with the tusker herd along the High Crown's flank to Vael's lake gate (days 111-135).",
      name="The tusker road", label=True)
route("m42", "S", 42, [(150.2, 40.5), (141, 38), (121, 31), (104, 33), (92, 38), (78, 41), (62.5, 45.5), (79, 57.5), (93.4, 67.0)],
      "West round Glasswater, over the Fells' western saddle to Coldrun Locks, down the canals to Ironhythe, then down the Scald Cut (days 178-205).",
      name="The canal road", label=True)
route("m55", "S", 55, [(94.5, 69), (101, 80), (95, 95), (74, 116), (70, 122), (60, 150), (49, 171)],
      "South by the Iron Road, south-west over Hearthmere's dead downs to Highcrest, and down the Sun Road to Solenne (days 287-300).",
      name="Maren's road to Solenne", label=True)
route("m57", "S", 57, [(48.5, 171), (49.5, 163), (50.2, 157.5)], "A day north up the Gilt valley's west side into the Elderwood.")
route("m67", "S", 67, [(48.5, 171.5), (60, 150), (70, 120), (90, 112), (110, 110), (126.5, 108.2)],
      "North-east up the Sun Road out of drained Sarovel and by the King's Road to Hallowmere (days 323-334).", name="Maren's road home", label=True)
route("m69", "S", 69, [(129, 108), (142, 106), (155, 105), (166, 106), (173.4, 106.5)], "Down the King's Road and the River Road to Greyhold (days 336-338).")
# Calder
route("c02", "F", 2, [(174.8, 103.8), (173.2, 104.8), (173.4, 106.2), (174.2, 107.0)], "The afternoon walk down the River Road from the reeds to Greyhold landing, Aurveth on three legs.", realm=False)
route("c07", "F", 7, [(175.0, 107.3), (176.7, 105.6), (177.3, 103.6), (178.8, 101.8), (180.8, 99.2)],
      "Days 6-10: from the Staithe up the bank track to Harrow's End and up the Way to the Ram's Head, walking Aurveth.", name="Calder's walk up the Way", label=True, realm=False)
route("c10", "F", 10, [(180.8, 99.2), (181.4, 98.5), (182.8, 96.7), (184.2, 95.2)], "Days 11-12: past Teo's ford and the falls on Hollow Beck to the hold.", realm=False)
route("c12", "F", 12, [(184.4, 94.8), (182.3, 97.8), (180.5, 101.5), (181.0, 107), (182.2, 111.2)],
      "Dawn, day 25: south on Kharrak for the first time, down the Way toward Cotter's Cross.", name="Calder flies south", label=True)
route("c19", "F", 19, [(184.4, 94.8), (187.8, 95.6), (190.7, 95.1)], "Day 56: to Skarrow with the book.", realm=False)
route("c30", "F", 30, [(184.4, 94.8), (182, 120), (182.5, 160), (183.3, 198.5)], "Days 115-116: south down the Wend to Wendmouth on Kharrak, with Lisska.",
      name="Calder's flight to Wendmouth", label=True)
route("c33", "F", 33, [(186, 199), (180, 160), (178, 115), (172, 80), (168.6, 52.5)], "Days 130-141: north over the scrub and the hills to the Iron Fells, and the hunters' pass.")
route("c35", "F", 35, [(167.6, 51.2), (163, 49.5), (158.6, 47.6)], "West along the Fells to Starwatch's peak.", realm=False)
route("c38", "F", 38, [(167.6, 51.6), (160, 57), (155.5, 54.6), (152.5, 50.5), (151.2, 46.0), (151.5, 39.0)],
      "Night 176: after the hunters' flight round the Fells' end; then north up the drowned valley and the lake to the Library hill.", name="After the hunters", label=True, realm=False)
route("c43", "F", 43, [(151.4, 47.5), (156.5, 55.2), (168.5, 60.3), (176.1, 62.8), (177.4, 72), (176.6, 86), (176.6, 96), (174.6, 106.5)],
      "Days 178-182: down the drowned valley and the Wend a day ahead of the flood, landing in every town.", name="Ahead of the flood", label=True)
route("c46", "F", 46, [(184.4, 94.8), (172, 103), (155, 106), (130.5, 107.8)], "Day 205: six hours south and west over the Marches and the dead country to Hallowmere.",
      name="Calder flies to Hallowmere", label=True)
route("c49", "F", 49, [(184.4, 94.8), (190.5, 95.2), (204, 130), (213, 194), (232, 186), (259, 192.5)],
      "Days 232-239: down to Corsa with Aurveth, slowly, resting at Skarrow, a cape above Gullhaven and the Saltings.", name="Down the coast with Aurveth", label=True)
route("c56", "F", 56, [(184.4, 94.8), (176, 104.5), (174.6, 107.0), (200, 140), (250, 162), (293.5, 177.5)],
      "Days 291-296: by Greyhold landing to Blackwater, with Gunna Tarne and six riders of the ledges.", name="To Blackwater", label=True)
route("c59", "F", 59, [(293.5, 178.5), (262, 193.5), (232, 196), (217.2, 199.4)], "Day 301: west along the coast to Gullhaven.")
route("c64", "F", 64, [(186.5, 92.5), (195, 130), (216.5, 197.8)], "Day 318: back down to Gullhaven with Ada in a basket.", realm=False)
route("c68", "F", 68, [(217, 198.5), (240, 194.5), (260, 193)], "Day 330: to Corsa, summoned.")
route("c78", "F", 78, [(216.5, 199), (200, 203), (184, 202), (182, 170), (181, 130), (177.5, 112), (175.4, 107.6)],
      "Days 352-354: west along the coast and up the Wend's valley with Aurveth, racing the Titan home.", name="The flight home", label=True)
# Idony
route("i08", "R", 8, [(150.5, 37.5), (170, 30.5), (196, 31), (222, 40), (246, 50)], "Day 20: east under the High Crown with Dane's Wardens and the binding-lamps.",
      name="The Wardens' road", label=True)
route("i16", "R", 16, [(246, 50), (253, 59), (259.3, 65.6)], "Into the Thornwood by the northern path; the grey on day 61.")
route("i27", "R", 27, [(252.5, 81), (238, 77.5), (221, 70), (203, 41), (176, 33), (152, 37.5)],
      "Days 110-121: west across the dead Wyldmarch measuring the drain, then up the High Crown road to Vael on foot.", name="Idony rides west", label=True)
route("i71", "R", 71, [(49, 175.5), (70, 196), (115, 207), (160, 213), (205, 213), (250, 204), (284, 186.5), (291.5, 180.5), (275, 194), (246, 194), (235.5, 185.5)],
      "Days 318-338 on Corvin's ship: east along the coast to a cove by Blackwater for Callis, then back west into the Saltings' channels.",
      name="Corvin's ship", label=True)
route("i76", "R", 76, [(235.5, 185.5), (218, 150), (196, 124), (171, 109.5), (174.9, 103.4)],
      "Days 348-352: north by bound wyvern over the Saltings and the Ashlings to the Brackenwood, then down to the eddy.", name="By wyvern to the eddy", label=True)
B.finish_routes()

# ---------------- the close-ups: chapter by chapter ----------------
# Part One: After the Lamps
item("reeds", "The reeds below Redwatch", "area_small", 175.0, 104.4, 1, "Sunrise, day 0: a lion and three dragons in the reeds below cracked Redwatch, and Rowan's forty knights on the bank above. Nobody moves.", dx=0.3)
item("rowan1", "Rowan's knights", "watchers", 174.1, 103.9, 1, "Thirty-eight knights and students on greyharts, hounds at heel, the crown's chain on its wain. \"Not today.\"", label=False)
item("armybreaks", "The Restoration's army breaks up", "camp", 178.3, 103.9, 1, "On the hill above Harrow's End the army comes apart by itself, unled, men walking off north and south in twos and threes.", dx=0.3)
item("ferryhouse", "Liss's ferry house", "house", 174.15, 107.25, 2, "A long low stone house at the foot of Greyhold's jetty, with a smoke-house, a net-loft and the ferry on its slip.", carry=True, keep=True, dx=-0.3, until=86)
item("gallery", "The Gallery of Glasses", "house", 150.4, 35.7, 3, "The College of Tides' long east gallery: 312 tide-glasses, and at midnight on the night of the locks every one breaks at once.")
item("graves4", "Greyhold's dead", "death", 172.9, 106.0, 4, "Day 1: fifty-three graves on the hill west of the walls, beasts beside their partners.")
item("gate4", "Cassian's body on the gate", "chain", 173.55, 107.0, 4, "Day 3: the crown hangs the leader's body in chains under the charter on Greyhold's gate, \"the Restoration's leader\".", dx=-0.5, until=75)
item("held4", "The held breath", "lock", 174.25, 106.05, 4, "Below the cavern where the chains were, something shut, \"like a breath held\". The knight's lock still burns white.", keep=True, until=84)
item("herald5", "The herald's proclamation", "scroll", 174.45, 107.55, 5, "Saltreach refugees to go back over the river within ten days; the farmer outlawed, a hundred crowns alive.", label=False)
item("swim5", "Aurveth swims the Wend", "route", 174.4, 107.2, 5, "Dawn, day 6: the old dragon swims the spring current to Tolly's Staithe with Kharrak under her chest.",
     path=[(174.4, 107.15), (174.8, 107.3), (175.1, 107.4)], label=False, until=7)
item("well6", "Millbrook's sweet well, sour", "landmark_pt", 173.6, 109.0, 6, "The spring under its carved hood, a licensed word cut in it, brown and smelling of iron and eggs.", dx=-0.4)
item("granary6", "The granary wall opened", "lion", 174.05, 106.35, 6, "Night 8: Orrun opens the split in the inner wall from the river side and Maren brings the Fenns out.", size=0.6)
item("ewe7", "Deserters turned at Ewe Hollow", "roadblock", 176.6, 105.5, 7, "Day 7: sixteen deserters with Ewe Hollow's sheep; Coll Brask talks them down.", dx=0.3)
item("rams7", "The Ram's Head, sacked", "fire", 181.15, 99.35, 7, "The sign hanging by one chain, the barrels stove, the charm-board in the mud.", label=False)
item("dane8", "The Council of Colleges", "house", 149.0, 35.0, 8, "Day 12: \"The Hearthmere draw is not a subject for study.\"", label=False)
item("swath9", "The Titan's swath", "band", 176.8, 102.6, 9, "Where the Titan flew low at sunrise on day 0: a league wide, every tree laid flat pointing north-east.",
     path=[(176.6, 102.8), (179.8, 100.5), (183.6, 97.6), (186.8, 95.2)], dx=0.3, until=12)
item("beck9", "Two deserters killed", "death", 183.0, 100.6, 9, "Day 13: at a beck in the Fellwood; Orrun is past her before she has moved. \"You are not my hand.\"", dx=0.3)
item("setters10", "The setters' ledge", "landmark_pt", 185.3, 93.6, 10, "Where the ledges sing the setting-song over Aurveth's wing.", label=False)
item("handover11", "The Fenns handed to the ledges", "meet", 186.2, 97.0, 11, "Day 15: Gunna Tarne and Tamsin take the Fenns, the greys and Old Grey up to the hatching caves.", label=False)
item("muster12", "Corvin's muster", "camp", 181.1, 113.6, 12, "The unpaid companies gathering at Cotter's Cross under the ring of six, Reede's bills on every door.", dx=0.3)
# Part Two: Midsummer
item("barrows", "The Lions' Barrows", "landmark_pt", 240.6, 64.6, 13, "Grass mounds under black pines, each with a grey stone, two days into the Thornwood. Orrun lies down where there's a space.")
item("ring13", "The Hollow Ring", "stones", 260.0, 66.0, 13, "The clans' sacred stones deep in the Thornwood; the Titan has lain on them since the morning after the river.", until=19, realm=True, size=0.8)
item("titanring", "The Titan on the stones", "titan", 260.6, 65.4, 13, "Lion-kin the size of a hill, grey as old stone, chain-ends on its forelegs, breathing eleven in, nineteen out.", size=0.45, until=20)
item("contract14", "Ten thousand for the lion", "scroll", 180.2, 112.6, 14, "The Tide Council's contract on the beast-pen gate: the great beast of the Marches, alive.", dx=-0.4)
item("gully14", "Kharrak's gully", "landmark_pt", 182.3, 111.4, 14, "A dry gully in the Ashlings two leagues north-east of the Cross, where the red dragon lies up.", label=False)
item("stones15", "The Speaking Stones", "stones", 236.5, 82.5, 15, "Seven tall stones in a horseshoe on the Plains a day west of the Thornwood's edge. They hum for Orrun.", realm=True, size=0.8)
item("groves15", "Sleepwood groves burned", "fire", 244.0, 70.0, 15, "Night 57: the Keepers burn their own groves so no binder can cook honey-smoke from them.", dx=0.3)
item("groves15b", "", "fire", 252.5, 63.5, 15, "Sleepwood burning.", label=False)
item("rowan15", "Rowan's chain", "route", 228, 88, 15, "Day 51: Rowan's company over the Plains with the great chain on six wains.", path=[(222, 92), (234, 86), (248, 74), (257, 67.5)], label=True, pov="rowan")
line("grey16", "The grey", "sea", 16, [(260 + math.cos(a) * 1.0, 66 + math.sin(a) * 1.0) for a in [i * math.pi / 12 for i in range(25)]],
     "A league of dead ground round the Ring: grey trees, dead birds that don't rot, the stones \"full like a cup\".", realm=False, label=True, until=21, at=(261.1, 67.2))
item("wardens16", "The Wardens' rise", "camp", 260.0, 64.7, 16, "Dane's Wardens on the rise north of the Ring, with the binding-lamps.", dx=0.3)
item("knights16", "The knights' stakes", "camp", 258.6, 66.3, 16, "Rowan's stakes in two curved lines toward the forelegs, from the west.", dx=-0.6)
item("knot18", "The finding-knot", "bond", 260.3, 66.7, 18, "Day 85: tied with a hair of Orrun's mane; on the grey it's string, through him it pulls.", label=False)
item("caves17", "Rook's ledger read", "scroll", 189.9, 90.4, 17, "At the cave mouth, by Ada's hearth-fire: \"the hedge at the bottom of the Fenn field, one bolt, the Sallow rider\".", label=False)
item("steadings19", "Two steadings burned", "fire", 182.6, 99.4, 19, "Day 64: an Arn steading and an Ulric steading, half a league apart, each left with the other's colour. Wendmouth boots.", dx=0.3)
item("capture20", "The capture", "battle", 260.4, 66.6, 20, "Midsummer night: Rowan's chain, the Wardens on the stones, Corvin's smoke; Maren takes the Wardens off the stones.", dx=0.3)
item("sink20", "The Ring falls in", "rubble", 259.7, 66.0, 20, "The Titan rose with the relic and the ring went down into the temple after it.", label=False)
item("roosts21", "Corvin's raid on the Roosts", "battle", 186.6, 92.4, 21, "Midsummer night: honey-smoke on the wind; four young dragons taken.", dx=0.3)
item("tor21", "Where Tor and Skell died", "death", 186.0, 93.5, 21, "Hallam's grandson and his young blue, together on the Choosing Ledge.", label=False)
item("taken21", "Four young dragons taken", "route", 188, 96, 21, "They flew south-east over the moor after the wyverns, into the dark.",
     path=[(186.6, 93.0), (190.0, 95.5), (194.0, 99.0)], label=True)
item("moot22", "The clans gather at the Moot", "camp", 251.2, 81.6, 22, "Hundreds of roundhouses and hide tents for the month of midsummer.", label=False)
item("temple23", "Six sleepers carved", "scroll", 261.0, 67.2, 23, "Under the stones: six great beasts lying in a ring, asleep, and shapes of light over them. Sleep, six times. Here the breath is kept.", dx=0.3)
item("pyre24", "Tor Brecc's pyre", "fire_plain", 187.4, 91.9, 24, "Day 101: one pyre for all of them, red thread and grey. Next morning Arn and Ulric pour together.", dx=0.3)
item("lanes25", "The lanes held", "battle", 252.5, 81.0, 25, "Day 105: the beast-flood down the Moot's seven lanes; two lions in two lanes at once.", dx=0.3)
item("hesper25", "Where Hesper and Hush died", "death", 253.3, 80.3, 25, "In the seventh lane by the forest's edge, singing.", label=False)
item("elk26", "The elk herd turned", "route", 181, 100, 26, "Day 112: Lisska drives the lead cow down to him; the herd-charm turns her, and the herd follows her off the field.",
     path=[(184.5, 97.0), (181.5, 99.6), (179.3, 101.2), (178.4, 100.4)], label=True)
item("topfield26", "The Fenn top field", "landmark_pt", 178.75, 101.45, 26, "Above the village, between the herd and the houses: Calder's first casting.", carry=True)
item("drain27", "The Wyldmarch gone dead", "label", 262.0, 100.0, 27, "Behind the Antlered the Wyldmarch goes dead for a hundred leagues: a stir, a flood, and then a famine.", realm=True, until=40)
# Part Three: The Long Library
item("milestone28", "An old milestone", "landmark_pt", 182.0, 29.6, 28, "On the tuskers' road, by a meadow that was once water: a leaning milestone of the old realm, hooked marks worn away.", dx=0.3)
item("passstone", "The pass-stone", "landmark_pt", 147.5, 38.2, 28, "Above the Vael Pass, where the old cow lays her trunk and the herd will go no further.", label=False)
item("titanlake", "The Titan on the lake", "titan", 150.0, 42.4, 29, "Day 116 on: lying on Glasswater a mile out from the quays, grey, like an island that breathes.", size=0.45, until=36)
item("cup29", "The cup's edge", "label", 148.8, 38.6, 29, "The line across the city where the lamps go from brown to white: Candle Row.", label=False)
item("mint30", "The Halloran mint", "house", 183.7, 202.7, 30, "In a cellar under the Halloran counting-house on Mint Lane: the silver with the ring of six on the rim, and the mint-book.", dx=0.3)
item("quay30", "Gallows Quay, the cages opened", "cage", 182.8, 204.0, 30, "Dawn, day 121: Calder lets everything out along the quay, as he did in the autumn.", dx=-0.5)
item("warehouse30", "The Halloran warehouse burned", "fire", 184.3, 204.6, 30, "Kharrak burns it to the waterline.", label=False)
item("shingle31", "Orrun on the shingle", "lion", 148.4, 40.2, 31, "Below the lower city at the end of the old fish-quay, as close to the island as dry land lets him.", size=0.6, until=36)
item("perch32", "The Old Reader's perch", "landmark_pt", 154.0, 32.7, 32, "At the hill end of the Long Library, half a league from the door, where the stone hums loudest.", dx=0.3)
item("camp33", "The hunters' camp", "camp", 168.0, 51.0, 33, "A bowl under a cornice: twenty hunters, four binders, the four young dragons on chains in honey-smoke.", dx=0.3)
item("tasso33", "Tasso warmed", "fire_plain", 166.4, 49.6, 33, "Below the pass after the storm: the hearth-word with Kharrak's heat, and it takes too hard.", label=False)
item("guard35", "The guardhouse roof", "rubble", 158.6, 48.4, 35, "Kharrak takes the roof off the Wardens' guardhouse at the foot of the six hundred steps. Not one hurt.", label=False)
item("binding36", "The great binding", "battle", 151.3, 36.4, 36, "Noon, day 172: a hundred magisters barefoot on the humming terrace, and the Titan held one breath.", dx=0.3)
item("bluetower", "The Blue tower falls", "rubble", 149.4, 36.8, 36, "The Titan comes down on the hill on the Blue College's side and puts its head into the hill.", dx=-0.4)
item("ice36", "Ice on Glasswater", "ice", 151.6, 43.4, 36, "The Coil's cold skins the lake with ice in late summer.", label=False)
item("wall37", "The lion's wall", "wall", 148.6, 39.7, 37, "Across Dye Street behind the fish-market: old-realm footing-stone raised the height of a house, and the hold rune cut into the crack.",
     path=[(148.0, 39.9), (149.2, 39.5)], label=True)
item("flood37", "The meltflood", "flood", 151.4, 48.6, 37, "The Coil breaks the lake's lip going out and the lake goes after it, down the valley that heads the Wend.", dx=0.3)
item("hill38", "Fight on the Library hill", "battle", 152.4, 35.6, 38, "The hunters' bound dragons on the roofs; the yearling wakes on the ridge.", dx=0.3)
item("bird39", "Where the bird was killed", "death", 153.6, 33.6, 39, "The Old Reader, on the case it kept three hundred and four years. \"Ask, ferryman. Ask everything.\"", dx=0.3)
item("pyre40", "The bird's pyre", "fire_plain", 152.6, 33.9, 40, "Night 177 on the Library steps; Kharrak lights it. Idony's ring is broken there.", dx=-0.4)
item("frost41", "The frost-map", "area_small", 150.9, 41.0, 41, "Night 177 on the drained shore: the Oneroad's six roads drawn in frost, and Idony's tide-chart laid over them.", dx=0.3)
for _i, (_t, _nm) in enumerate([((260, 66), "the Ring"), ((150, 39), "Vael"), ((94, 70.5), "the Scald"), ((50, 176), "the Sun Stair"),
                                 ((217.5, 202.6), "the reef"), ((174.4, 105.6), "the river hill")]):
    line(f"sixends{_i}", "The six ends" if _i == 0 else "", "sea", 41, [(175.8, 103.5), _t],
         f"The frost-map: one of the Oneroad's six roads from the bridge, to {_nm}. The roads are the Deep's tide-lines; the six ends are the sleepers.",
         realm=True, label=_i == 0, until=42, at=(205, 86) if _i == 0 else None)
# Part Four: Iron and Glass
item("cage42", "Pike's cage", "cage", 94.0, 68.2, 42, "Three chilled canals round the Scald basin and two rings of iron pylons: forty years' work, never tested.", dx=0.4, realm=True, size=0.8)
item("towns43", "Water coming", "flood", 177.0, 73.0, 43, "Days 178-180: he writes WATER COMING on the doors of every town's biggest building.", dx=0.3)
item("ferry43", "The ferry driven onto the jetty", "flood", 174.7, 107.9, 43, "Day 182: the guide-rope parts; Lisska empties all her wind to drive the ferry onto the stone.", label=False)
item("eelweirlost", "The Eelweir, lost", "rubble", 176.9, 103.3, 43, "Four houses, the jetty and the boats; Fisk on his roof with a pot of tea.", label=False)
item("engine44", "The north-quarter engine-house", "house", 94.0, 66.3, 44, "A great iron drum ringed with marks, fed with heartstones: six hundred hearts a day while the field is closed.", dx=0.3)
item("egg45", "The egg taken", "titan", 94.3, 68.9, 45, "Day 233: the Titan breaks into the temple under the basin and lays the egg into the plates of its back.", size=0.45, label=False)
item("ditch45", "The labourers pulled out", "battle", 96.2, 68.6, 45, "The Bleed comes up in the ditches and the crews go mad; Maren, Tobin and Orrun get thirty-seven out.", dx=0.3)
item("square46", "The Crown's Square", "landmark_pt", 128.3, 107.4, 46, "Day 205: the outlaw tells the crown, and Davin reads the account aloud to the square.", dx=0.3)
item("banks48", "Three lions on three banks", "lion", 93.7, 66.6, 48, "The cordon's banks slide with the crews on them; Orrun stands on three at once.", size=0.6, dx=-0.4)
item("tidehall", "The Tidehall", "house", 262.4, 193.6, 49, "The Council's great house on Corsa's harbour front, its copper roof gone green.", carry=True, dx=0.3)
item("rusk49", "Rusk flees", "route", 263, 196, 49, "Out of the Tidehall's back door onto a fast black two-master, past the chain on the morning tide.",
     path=[(262.6, 194.0), (264.5, 197.5), (266.5, 202.5)], label=True, realm=False)
item("envoys50", "The envoys' camp", "camp", 91.0, 67.6, 50, "Outside the west gate on the Iron Road: every kingdom comes to look at a caged Titan.", dx=-0.4)
item("midwinter51", "Midwinter in Orrin", "fire_plain", 93.2, 65.0, 51, "A fire in the chapel's hearth; three voices: \"Keep the watch.\"", label=False)
item("tunnel53", "The Furnace's tunnel", "route", 95, 67, 53, "Down through the drained canal-bed and the glass tunnel, four hundred paces, to the temple under the basin.",
     path=[(96.4, 66.6), (95.6, 67.5), (94.6, 68.6)], label=True, realm=False)
item("army54", "The Restoration's army breaks", "battle", 182.3, 116.0, 54, "Day 288: the Clan's flights come down on the deserters on the Cotter's Cross road in the Ashlings scrub.", dx=0.3, realm=False)
item("upperrush54", "", "fire", 177.6, 100.6, 54, "Upper Rush burned again by the companies going east.", label=False)
# Part Five: The Sun Stair
item("stages55", "Stage-chapels to the Sun on the Stair", "shrine", 64.5, 140.0, 55, "Every half-day on the pilgrim road: a domed chapel with a gilded sun, and the liturgy at dusk.", dx=0.3)
item("boathouse56", "The boathouse fight", "battle", 296.2, 177.0, 56, "Dawn, day 297: wet vinegar cloths against the honey-smoke; two young dragons brought back to the edge of themselves.", dx=0.3)
item("bronze56", "Where the bronze was killed", "death", 295.6, 177.8, 56, "Its binder put a knife under its jaw rather than lose it.", label=False)
item("clearing57", "The unicorns' clearing", "landmark_pt", 50.2, 157.2, 57, "Where eleven wild unicorns tell Orrun that nine generations of royal bonds were bindings.", dx=0.3)
item("titanhills", "The Titan on the hills", "titan", 51.0, 166.5, 58, "From day 290 on the ridge above the palace; the Grace too bright, collars cracking.", size=0.45, until=60)
item("handshall", "The hands' hall", "house", 47.2, 173.0, 58, "Long vaulted rooms under the palace's west wing, cut into the cliff, where the court's unbonded hands do its workings.", dx=-0.4)
item("reef59", "Aurveth's deep sight", "bond", 217.7, 202.4, 59, "Day 305 at low spring tide: lying on the reef, he feels the Bell's sleeper breathe.", dx=0.3, label=False)
item("lifts59", "The Clan's baskets", "dragon", 214.7, 201.1, 59, "Arn's pairs practising on the spit with war-harness and wicker baskets.", label=False, size=0.6)
item("egg60", "The egg taken", "titan", 50.2, 175.4, 60, "Noon, day 315: down through the palace and the stair into the temple; Orrun stands before the egg and it reaches past him.", size=0.45, label=False)
item("king61", "Where the Bond-King died", "death", 48.6, 172.6, 61, "The unicorn, its collar broken, throws him and puts its horn through him on his own stair.", dx=-0.4)
item("ship63", "Idony taken", "ship", 47.0, 174.4, 63, "Day 318: dragged up the plank of Corvin's ship at the palace's harbour stair; it goes out east past Sorrel Isle.", dx=-0.4)
item("boats63", "Boats to Sorrel Isle", "route", 54, 181, 63, "The low quarter goes over the water to the lighthouse rock.", path=[(50.5, 177.0), (53.5, 181.0), (56.8, 184.6)], label=True, realm=False)
item("ysa63", "Where Mother Ysa drowned", "death", 56.8, 186.2, 63, "The lighthouse keeper's last boat, on the rocks off the island's landing.", label=False)
item("roofs64", "Four hundred and twelve roofs marked", "label", 216.6, 201.4, 64, "A white lime cross on every ridge that will take a dragon's weight.", dx=0.2)
item("lighthouse", "The lighthouse", "lamp", 57.8, 185.2, 65, "Where Maren reads the Sun Stair's carving and decides to go home and keep the door.", dx=0.3, carry=True)
# Part Six: The Drowned Bell
item("chapel67", "The chapel off the corn exchange", "shrine", 129.0, 108.6, 67, "Old women kneeling at the hearthstone: \"Mother, keep the fire.\"", dx=0.3, label=False)
item("clan68", "The Clan over Corsa", "dragon", 260.6, 190.8, 68, "Day 332: forty-odd dragons wheel over the harbour and the Tidehall's copper roof.", size=0.6, dx=0.3)
item("anchors69", "The cage's anchors", "cage", 174.3, 105.9, 69, "Kessmoor engineers drilling the inner wall's drained old stone for the cage's iron eyes.", dx=0.3, until=82)
item("fleet70", "The Strand fleet", "ship", 220.5, 206.0, 70, "Day 341: eleven ships, four Kessmoor engine-barges, Vey's black ship with the wyverns on deck.", dx=0.3)
item("hulls70", "Hull-runes burning", "fire", 216.0, 200.8, 70, "Night 344, the stir: the runes on every hull in Gullhaven glow, then burn.", label=False)
item("reeds71", "Corvin's ship in the reeds", "ship", 235.5, 185.5, 71, "Masts down in a reed-channel two leagues inland of the coast, east of Gullhaven.", dx=0.3, size=0.8)
item("ferriby72", "Ferriby's beasts taken", "beast", 173.4, 102.9, 72, "A band of broken men with three binders walks Ferriby's oxen and dogs north into the Brackenwood, empty-eyed.", dx=-0.3)
item("penfold72", "Binders turned at Penfold", "battle", 172.7, 104.4, 72, "Day 346: driven into a beck, the bound cows come out of the running water themselves.", label=False)
item("ferryrun72", "The ferry runs night and day", "route", 175, 107, 72, "Over the river, everyone, with their beasts, and up the Way: running water stops a binding.",
     path=[(174.4, 107.15), (175.0, 107.35), (176.2, 106.0), (177.1, 104.0)], label=True, realm=False)
item("battle73", "Vey's fleet on the reef", "battle", 218.3, 203.0, 73, "Harpoons, engines, the house drawers on the bare reef; the tide turns and the running water breaks them.", dx=0.3)
item("vey73", "Where Vey died", "death", 217.1, 203.0, 73, "On the reef among his drawers, the last off; the reef cracked across and the sea took him.", label=False)
item("lamps74", "One hour of light", "lamp", 173.5, 107.2, 74, "Night 348: every dead lamp in Hearthmere flares white for an hour. It means it's coming home.", dx=-0.4)
item("wave75", "The wave", "wave", 215.3, 201.75, 75, "Day 349: the sea comes back in a grey wall and takes the spit's seaward half. Three thousand five hundred lifted; two hundred and ninety drowned.", dx=0.3)
item("pyre76", "Cassian's pyre", "fire_plain", 175.3, 103.1, 76, "Night 352: Corvin burns his brother's body on a boat in the eddy. An hour's truce on the shingle bar.", dx=-0.4)
item("stair77", "The older stair", "lock", 173.3, 107.0, 77, "Under the grooms' burial ground by Garran Vale's stone: an older stair, cut in the old stone, made for door-keepers.", dx=-0.4, carry=True)
item("pyres78", "The drowned burned on the shingle", "fire_plain", 213.5, 200.6, 78, "Dusk, day 350, at the spit's root; then Arn and Ulric pour for strangers.", dx=-0.4)
# Part Seven: Under the Hill
item("cellars79", "Seventy go into the cellars", "house", 173.7, 106.3, 79, "The poorest of Millbrook's lower lane, who won't go on the river; Joby Marsh stays with them with a lantern.", label=False)
item("chains80", "The second cage", "cage", 175.1, 105.4, 80, "Six chains over the river from Greyhold's hill to the Saltreach anchors, and heartstone engines roaring.", dx=0.3, until=82)
for _i, (_a, _b) in enumerate([((174.2, 106.2), (176.2, 105.6)), ((174.1, 106.5), (176.1, 106.2)), ((174.3, 105.8), (176.3, 105.0))]):
    line(f"cagechain{_i}", "", "sea", 80, [_a, _b], "One of the second cage's chains.", realm=False, until=81, weight=2.2)
item("band80", "The last of the Restoration's war", "battle", 173.9, 107.6, 80, "A band come to loot the empty landing breaks and runs when Arn's red comes down on it.", dx=-0.4)
item("shut81", "The shut place", "lock", 174.55, 105.75, 81, "Rings of script coming up out of the stone, lit gold: \"One hand shut it. Two hands open it together.\"", dx=0.3, until=83)
item("eyes82", "The eyes tear out", "rubble", 174.0, 106.2, 82, "The chain-runes feed until the empty stone fails; Rowan lets go of the chain.", label=False)
item("cellars83", "The cellars", "rubble", 173.6, 106.6, 83, "The Titan's rage brings the roof down over the cellars; Orrun and four shadows carry the seventy up through the rock.", dx=-0.4)
item("vault84", "The control relic taken", "titan", 174.4, 105.9, 84, "The deepest vault: a ring of grey stone with six hollows; it takes Corvin's hand, and the Titan takes it.", size=0.45, dx=0.3)
item("lion85", "The lion comes up", "lion", 173.4, 109.4, 85, "Dawn, day 356: up out of the hillside above Millbrook's woods, a grey-haired man on his back.", size=0.6, dx=-0.4)
item("envoys86", "The envoys' table", "meet", 174.6, 107.7, 86, "In Liss's cracked ferry house: no single kingdom can stand.", dx=0.3)
item("titanmoor", "The Last Titan on the Scarfell", "titan", 190.2, 88.8, 87, "From the night of 355: on the high moor above the hatching caves, very still, six in its back.", size=0.5, until=88)
item("account88", "The account begun", "scroll", 189.4, 90.6, 88, "Day 365 at Bel's table: \"The dragons came to me in a barley field, and I had never asked them for anything.\"", label=False)

# a lighter pass of names that would clutter a close-up of somewhere else
B.ITEMS.sort(key=lambda i: i["ch"])
