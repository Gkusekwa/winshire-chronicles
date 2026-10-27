"""Winshire world data. Coordinates are in leagues (x east, y south).
One league is about three miles, roughly an hour's walk.
Everything here is a working proposal unless marked established in the bible.
"""

# ---------------- land, sea, kingdoms ----------------

COAST = [  # mainland outline, clockwise from the north-west cape
    (12, 30), (22, 16), (42, 10), (60, 17), (78, 9), (100, 13), (122, 6), (146, 11),
    (170, 4), (196, 10), (220, 5), (246, 11), (270, 6), (292, 13), (308, 24),
    (314, 42), (320, 64), (311, 84), (318, 108), (312, 132), (319, 152), (308, 168),
    (303, 176), (297, 182), (301, 190), (288, 193), (276, 197), (266, 199),
    (257, 196), (248, 191), (237, 196), (226, 202), (214, 201), (205, 205),
    (194, 207), (185, 211), (178, 213), (170, 207), (160, 205), (150, 209),
    (142, 205), (130, 208), (120, 203), (110, 199), (98, 201), (86, 195),
    (76, 187), (66, 191), (56, 183), (48, 177), (44, 181), (36, 177), (30, 168),
    (34, 158), (24, 151), (12, 141), (18, 128), (26, 118), (19, 104), (28, 94),
    (21, 78), (13, 66), (19, 57), (11, 50), (16, 40),
]

ISLANDS = [
    [(236, 210), (243, 208), (247, 212), (240, 216)],   # Bell Reef
    [(36, 190), (44, 188), (46, 194), (38, 196)],       # Sorrel Isle (Sarovel)
]

KINGDOMS = {
    "kessmoor":  {"name": "Kessmoor",   "label": (62, 30),  "status": "established"},
    "isvaren":   {"name": "Isvaren",    "label": (178, 34), "status": "established"},
    "wyldmarch": {"name": "The Wyldmarch", "label": (262, 30), "status": "established"},
    "sarovel":   {"name": "Sarovel",    "label": (52, 128), "status": "established"},
    "hearthmere": {"name": "Hearthmere", "label": (128, 150), "status": "established"},
    "saltreach": {"name": "Saltreach",  "label": (240, 160), "status": "established"},
}

BORDERS = [
    [(16, 90), (40, 92), (70, 94), (96, 88)],                      # Kessmoor / Sarovel
    [(96, 88), (110, 80), (128, 72), (150, 68), (172, 67)],        # Kessmoor+Isvaren / Hearthmere
    [(108, 6), (112, 25), (116, 45), (122, 62), (128, 72)],        # Kessmoor / Isvaren
    [(96, 88), (101, 115), (104, 140), (112, 170), (118, 204)],    # Sarovel / Hearthmere
    [(180, 66), (196, 63), (208, 60)],                             # Isvaren / Saltreach (Clan north)
    [(214, 6), (213, 30), (210, 48), (208, 60)],                   # Isvaren / Wyldmarch
    [(208, 60), (214, 85), (226, 112), (248, 138), (276, 152), (300, 160), (315, 162)],  # Saltreach / Wyldmarch
]
# The Wend itself is the Hearthmere / Saltreach border from about league 67 to the sea.

# ---------------- water ----------------

WEND = [  # the border river, source to sea
    (186, 24), (183, 34), (179, 44), (177, 54), (176, 62), (177, 70),
    (179, 78), (176, 86), (178, 94), (176.5, 100), (176, 103.5), (174.6, 106.5),
    (174.8, 110), (176.5, 114), (175.5, 120), (178, 130), (176, 142),
    (180, 156), (177, 170), (180, 184), (178, 196), (180, 209),
]

RIVERS = {
    "The Coldrun": [(104, 30), (92, 38), (78, 40), (62, 48), (44, 50), (28, 54), (15, 56)],
    "The Gilt":    [(88, 104), (82, 120), (72, 136), (62, 152), (52, 170), (48, 178)],
    "The Meryl":   [(132, 126), (136, 145), (134, 165), (140, 182), (141, 204)],
    "The Ysse":    [(304, 64), (290, 80), (272, 96), (258, 108), (250, 118), (256, 140), (262, 160), (262, 194)],
    "Hollow Beck": [(196, 76), (191, 86), (186.4, 92.6), (182.6, 97.0), (179.6, 101.0), (177.8, 102.7), (176.3, 103.1)],  # Clan hills to the Wend
}

LAKES = {
    "The Mere":       ((130, 117), 14, 8),
    "Lake Ysse":      ((253, 112), 9, 5),
    "Glasswater":     ((150, 44), 6, 3.5),
    "Coldtarn":       ((196, 74), 2.4, 1.6),
}

# ---------------- terrain ----------------

MOUNTAINS = {  # name: (polyline, half-width in leagues, density)
    "The Worldsend": ([(300, 22), (304, 50), (301, 90), (304, 130), (298, 160)], 8, 1.2),
    "The Iron Fells": ([(100, 14), (110, 26), (120, 38), (128, 52), (134, 64)], 6, 1.0),
    "The High Crown": ([(40, 20), (90, 18), (140, 19), (200, 18), (260, 19)], 4, 0.9),
    "The Scarfell": ([(183, 72), (188, 80), (192, 88), (196, 97)], 4.0, 0.8),
    "Sunward Hills": ([(62, 100), (74, 106), (86, 114)], 4, 0.45),
}

FORESTS = {
    "The Thornwood": [(222, 22), (262, 18), (292, 26), (296, 56), (276, 78), (246, 80), (226, 64)],
    "The Brackenwood": [(160, 100), (168, 98), (171, 104), (168, 112), (161, 112)],
    "The Greenwold": [(140, 76), (162, 74), (168, 86), (152, 92), (138, 88)],
    "Elderwood": [(40, 110), (60, 104), (64, 122), (46, 130), (34, 122)],
    "The Ashlings": [(200, 120), (214, 116), (218, 134), (204, 140)],
    "The Fellwood": [(178.4, 100.2), (181.0, 97.8), (185.5, 98.0), (187.0, 101.5), (185.0, 105.0), (181.0, 106.0), (178.6, 104.6)],
    "The Wendwood": [(178.0, 116), (183, 117), (184, 135), (186, 155), (185, 175), (186, 192), (182, 197), (181, 184), (179, 170), (182, 156), (179, 142), (180, 130), (177.5, 120)],
}

MARSHES = {
    "The Saltings": [(214, 168), (246, 164), (252, 184), (224, 190)],
    "The Reedmarsh": [(178, 115), (186, 115), (187, 124), (179, 125)],
}

PLAINS = {
    "The Hallow Plains": [(232, 92), (296, 96), (300, 140), (262, 146), (236, 124)],
    "The Candle Downs": [(108, 140), (160, 136), (166, 180), (120, 186)],
}

# ---------------- roads ----------------

ROADS = {
    "The King's Road": [(141, 201), (138, 176), (134, 150), (128, 128), (128, 108), (142, 106), (155, 105), (166, 106), (174.0, 106.6)],
    "The River Road": [(174.0, 106.6), (172.6, 100), (174, 92), (175, 84), (174, 74), (172, 68)],
    "The River Road (south)": [(174.0, 106.6), (172.3, 112), (173, 120), (174, 135), (173, 155), (175, 175), (176, 196), (176, 206)],
    "The Iron Road": [(62, 45), (78, 58), (96, 72), (112, 90), (128, 108)],
    "The Sun Road": [(48, 172), (60, 150), (70, 120), (90, 112), (110, 110), (128, 108)],
    "The Vael Pass": [(150, 38), (146, 52), (140, 66), (136, 82), (130, 100)],
    "The Drover's Way": [(184.4, 94.8), (181.2, 98.6), (178.6, 102.0), (177.6, 103.2), (178.4, 106), (180.5, 113), (181, 130), (182, 150), (182, 175), (183, 204)],
    "The Coast Road": [(183, 204), (200, 202), (216, 198), (232, 196), (248, 194), (262, 193), (280, 186), (295, 178)],
    "The Saltreach Track": [(181, 130), (200, 140), (222, 156), (248, 176), (262, 193)],
}

ONEROAD = [  # the broken road of the old realm, mostly ruin
    (60, 130), (80, 118), (104, 112), (126, 106), (152, 104), (175.6, 103.5),
    (190, 104), (212, 102), (236, 98), (262, 90), (280, 70), (264, 50),
]

FERRIES = [((174.2, 107.3), (176.6, 108.3), "Ashdown Ferry")]

# Underground (author's map only)
CATACOMBS = [(174.0, 106.6), (174.5, 105.6), (175.1, 104.4), (175.6, 103.5)]

# ---------------- places ----------------
# kind: capital, city, town, village, fortress, ruin, landmark, temple, hold, farm, tower
# secret=True: the author's map only (protects Book 1 and Book 2 reveals)

P = []
def place(id, name, kind, kingdom, x, y, desc, scope="realm", secret=False, label_dx=0, label_dy=0, canon=""):
    P.append(dict(id=id, name=name, kind=kind, kingdom=kingdom, x=x, y=y, desc=desc,
                  scope=scope, secret=secret, ldx=label_dx, ldy=label_dy, canon=canon))

# ---- Hearthmere ----
place("hallowmere", "Hallowmere", "capital", "hearthmere", 128, 108,
      "The royal city on the north shore of the Mere. Grey stone and slate, built up the slope in terraces so that every street looks down on the water. "
      "The palace is less a castle than a long hall of chapter-houses where the knightly orders sit in council with the crown. "
      "Lamps burn without oil in the better streets, licensed magic and the city's quiet pride. No one asks where that much magic comes from.")
place("mere", "The Mere", "landmark", "hearthmere", 130, 119,
      "A broad, shallow lake that gives the kingdom its name. Reed beds, eel weirs and fishing villages on stilts along the south shore. "
      "In still weather it shows the sky so cleanly that the songs call it the hearth of heaven.", label_dy=2)
place("ashford", "Ashford", "town", "hearthmere", 155, 105,
      "A market town at the ford where the King's Road crosses the Ash Brook, eighteen leagues west of the border. "
      "Timber-framed houses leaning over the street, a horse fair every autumn, and three fencing masters who charge more than they should. Lucan Haverly trained here.")
place("stillhaven", "Stillhaven", "city", "hearthmere", 141, 201,
      "Hearthmere's only sea port, at the mouth of the Meryl. Walled harbour, customs house, a fleet of grain cogs. "
      "Saltreach privateers are a constant nuisance; the harbour chain is raised every night.")
place("candledowns", "The Candle Downs", "landmark", "hearthmere", 136, 162,
      "Rolling chalk farmland south of the Mere: wheat, sheep and orchards, villages around green squares, a chapel in every one. The breadbasket of Hearthmere, and of the Marches when harvests fail.")

# ---- The Marches (shown on both maps; detailed on the Marches map) ----
place("greyhold", "Greyhold", "fortress", "hearthmere", 174.0, 106.6,
      "The knight school on the Hearthmere bank, where the Wend bends. A quarry, then a fort, then a school: curtain walls of grey ragstone, a sanded yard over the old quarry floor, "
      "stables, a chapel, an armoury, and the river wall broad enough to walk two abreast. "
      "The charter over the gate says the bonded and the unbonded serve as equals. The cellars are locked and always have been.",
      scope="both", canon="Chapter 1", label_dx=-1)
place("oldruin", "The Old Ruin", "ruin", "marches", 175.6, 103.5,
      "Broken arches and a squat round tower on a wooded island where the Wend splits, about three and a half leagues upriver of Greyhold. "
      "It was a bridge-fort on the Oneroad, the old realm's highway, and the stumps of the bridge piers still break the water at low summer. "
      "A verse about Winshire is carved under the tower arch. River folk on both banks leave it alone.",
      scope="both", canon="established (island in the border river)", label_dx=-1, label_dy=0.9)
place("harrowsend", "Harrow's End", "village", "saltreach", 177.1, 103.1,
      "Calder's village on the Saltreach bank: thirty-odd houses of river stone and tarred timber with turf roofs, a mill on Hollow Beck, a shrine to the gods at the crossroads, "
      "and barley and flax fields running down to the water. It sits near the mouth of Hollow Beck, a league and a half across the water from the Old Ruin, which you can see from every field. Its fishing landing is the Eelweir. The Drover's Way passes through on its way to Varrhold.",
      scope="both", canon="name proposed")
place("varrhold", "Varrhold", "hold", "saltreach", 184.4, 94.8,
      "The Dragon Clan's hold, eleven leagues north-east of Harrow's End in the Scarfell. A ring of black-stone longhouses inside a turf rampart, "
      "the chief's hall roofed with dragon-scale shingles shed over generations, and above it the Roosts: dragon eyries cut into the cliff, scorched black at the mouths. "
      "Two days by grain cart from Harrow's End, one on horseback; about an hour and a half by dragon at a steady pace.",
      scope="both", canon="name proposed")
place("millbrook", "Millbrook", "village", "hearthmere", 173.9, 108.7,
      "A Hearthmere river village two leagues downstream of Greyhold: a water mill, a tavern called the Kettle, and a jetty where Saltreach boats tie up without asking. Poachers sell here.",
      scope="both", canon="named in Chapter 1; the caged beast in Chapter 7", label_dx=-1)
place("cotterscross", "Cotter's Cross", "town", "saltreach", 180.5, 113,
      "A rough market town on the Saltreach bank where the Drover's Way meets the Saltreach Track. Inns, a beast pen, a hiring yard where sellswords wait for contracts. "
      "Nobody keeps the peace here except whoever paid most recently.", scope="both")
place("scarfell", "The Scarfell", "landmark", "saltreach", 189.5, 86.5,
      "Bare, high moorland and broken crags north and east of the Marches: heather, scree and wind. Dragon country. Sheep, if you're brave.", scope="marches")

# Marches-only detail
place("calderfarm", "Fenn farm", "farm", "saltreach", 178.2, 101.9,
      "Calder's farm on the slope above Harrow's End: a stone longhouse with the byre under one roof, a barn, a kitchen garden, two fields of barley and one of flax, "
      "and the beck pasture below. The Fellwood begins a mile above the top field. The Clan's battle in Chapter 18 spills across these fields.", scope="marches", canon="Calder's home")
place("ferrylanding", "Ashdown Ferry", "landmark", "hearthmere", 174.3, 107.0,
      "Liss Ashdown's ferry: a flat-bottomed boat on a guide rope between Greyhold landing and the Saltreach jetty at Tolly's Staithe. Thirty years of crossings.",
      scope="marches", canon="Chapter 1")
place("tollysstaithe", "Tolly's Staithe", "village", "saltreach", 175.0, 107.2,
      "A huddle of fishermen's huts and drying racks at the Saltreach end of the ferry. Smoked eel, river gossip, and everyone's cousin.", scope="marches")
place("upperrush", "Upper Rush", "village", "saltreach", 177.3, 101.0,
      "A hamlet of four farms in a hollow above the Saltreach bank, two leagues upriver of Harrow's End. Its barns are the fires Maren sees from the river wall in Chapter 1: raided at night for beasts, then burned. Harrow's End blames the Clan's quarrel.",
      scope="marches", canon="Chapters 1 and 2")
place("ewehollow", "Ewe Hollow", "village", "saltreach", 181.4, 107.0,
      "Sheep folk in a fold of the hills east of Harrow's End: a dozen crofts, a wool barn, and a lot of dogs.", scope="marches")
place("northwatch", "Northwatch", "tower", "hearthmere", 174.4, 91,
      "A patrol tower on the River Road, manned by the river watch. Signal fires on the roof. Maren served here.", scope="marches")
place("redwatch", "Redwatch", "tower", "hearthmere", 174.6, 103.4,
      "The watch tower nearest the Old Ruin, red sandstone, half a league from the bank. The river watch's patrol boats are kept in its boathouse.", scope="marches", label_dx=-1, label_dy=-0.9)
place("brackenwood", "The Brackenwood", "landmark", "hearthmere", 168, 111.2,
      "Old oak and bracken west of Greyhold, a royal hunting ground. Deer, boar, and the beasts the knights pretend aren't there.", scope="marches")
place("reedmarsh", "The Reedmarsh", "landmark", "saltreach", 182.5, 120,
      "Reed beds and channels on the Saltreach bank below Cotter's Cross. Wildfowlers, smugglers, and beast poachers who know the channels.", scope="marches")
place("hollowbeck", "Hollow Beck", "landmark", "saltreach", 182.4, 95.4,
      "The stream that runs down from Coldtarn in the Scarfell, past Varrhold and Harrow's End, into the Wend opposite the Old Ruin.", scope="marches")
place("coldtarn", "Coldtarn", "landmark", "saltreach", 196, 74,
      "A black mountain lake above Varrhold. The Clan's dead are burned on its shore.", scope="marches")

# ---- Kessmoor ----
place("ironhythe", "Ironhythe", "capital", "kessmoor", 62, 45,
      "Kessmoor's capital and largest foundry city, on the Coldrun where the canals begin. Brick, iron and smoke; locks and lift-bridges; "
      "streets lit by alchemical lamps in green glass. The Assembly of Guildmasters meets in the Hall of Measures, under a clock that has never been wrong.")
place("gearmouth", "Gearmouth", "city", "kessmoor", 20, 55,
      "Port at the mouth of the Coldrun. Dry docks, steam cranes, and ships with iron-sheathed hulls built for the Western Deep.")
place("scald", "The Scald", "landmark", "kessmoor", 94, 68,
      "A wide basin of fused, glassy ground near the Hearthmere border where a town called Orrin stood until the disaster within living memory that led Kessmoor to ban magic. "
      "Nothing grows there. Kessmoor keeps a cordon around it and says it is to keep looters out.")
place("kess_temple", "Temple of the Scald", "temple", "kessmoor", 94, 70.5,
      "A temple deep under the Scald, holding one of the five sleep relics. Orrin's disaster began when Kessmoor engineers drilling for ore broke into its outer chambers. "
      "Kessmoor does not know what it found. (Book 2)", secret=True)

# ---- Sarovel ----
place("solenne", "Solenne", "capital", "sarovel", 48, 172,
      "The white city of the bond-monarchy, built of limestone on a curving bay. Domed halls, beast-stables grander than most houses, "
      "and the Bond-King's palace on the cliff, with its long stair down to the sea. Bond-crests over every noble door; the unchosen live below the walls.")
place("highcrest", "Highcrest", "city", "sarovel", 72, 118,
      "A hill city in the Sunward Hills, seat of the beast-lords who breed and train bonded mounts. Vineyards on the slopes, horse-fairs that are really beast-fairs.")
place("sorrel", "Sorrel Isle", "landmark", "sarovel", 41, 192,
      "A small island off Solenne where the unchosen are sent to serve the lighthouse. Or to be forgotten.")
place("sar_temple", "The Sun Stair", "temple", "sarovel", 50, 176,
      "Beneath the Bond-King's palace, below the sea stair, a temple holds a sleep relic. Sarovel's crowned line has worshipped there for centuries as a shrine of the gods and never guessed what it keeps. (Book 2)", secret=True)

# ---- Isvaren ----
place("vael", "Vael", "capital", "isvaren", 150, 36,
      "The city of the high colleges, on the north shore of Glasswater, under the Iron Fells. Slender towers of blue-grey slate, covered bridges between them, snow on the roofs half the year. "
      "Each college has its own colour of lamp, and the city at night looks like a hand of cards.")
place("longlibrary", "The Long Library", "landmark", "isvaren", 153, 33,
      "Isvaren's oldest archive, a single hall half a league long, built into the hillside above Vael. Its keeper is an ancient raven-like beast that learned human speech over centuries of listening to scholars. (Book 2)",
      canon="established (archive and speaking beast)", label_dx=4)
place("starwatch", "Starwatch", "tower", "isvaren", 128, 22,
      "An observatory on a peak of the Iron Fells, reached by six hundred steps cut into the rock. The colleges' astronomers chart the stars and, quietly, the strange lights over the Worldsend.")
place("isv_temple", "The Undercroft", "temple", "isvaren", 150, 39,
      "Excavated ruins beneath Vael, older than the colleges, which the scholars study as the remains of a pre-split shrine. One sealed chamber they have never opened holds a sleep relic. (Book 2)", secret=True)

# ---- The Wyldmarch ----
place("thornwood", "The Thornwood", "landmark", "wyldmarch", 258, 46,
      "Deep, old forest: oak, black pine and thorn, so dense in places that clans travel by the river. Beasts roam freely. Keepers walk its paths.")
place("hallowplains", "The Hallow Plains", "landmark", "wyldmarch", 268, 120,
      "Wide grassland running east to the Worldsend. Herds, horse clans, and standing stones that the clans say mark where beasts are buried.")
place("kethra", "Kethra's Moot", "town", "wyldmarch", 242, 122,
      "Not a town but a meeting ground on the shore of Lake Ysse, where the clans gather each midsummer under the elders. Hundreds of roundhouses and tents for a month, then empty grass.")
place("worldsend", "The Worldsend", "landmark", "wyldmarch", 300, 100,
      "The great eastern range, higher than any other mountains in Winshire, white all year. The clans say the Titans walked there at the world's edge. No one living has seen one.")
place("hollowring", "The Hollow Ring", "temple", "wyldmarch", 262, 54,
      "A ring of standing stones in a clearing deep in the Thornwood, sacred to the clans. Under the ring a temple holds a sleep relic. The clans guard the ring without knowing what is beneath it. (Book 2)", secret=True)

# ---- Saltreach ----
place("wendmouth", "Wendmouth", "city", "saltreach", 183, 204,
      "A port-city on the east bank at the mouth of the Wend, run by four trading houses who hate one another. Painted warehouses on stilts, a floating market, and the beast market at Gallows Quay, legal and otherwise.")
place("gullhaven", "Gullhaven", "city", "saltreach", 216, 198,
      "A fishing and salt port behind a long shingle spit. Smoke houses, salt pans, the best oysters in the Six Kingdoms and the worst wine.")
place("corsa", "Corsa", "capital", "saltreach", 262, 193,
      "The largest city of the Saltreach League, where the trading houses and pirate captains sit together in the Tide Council. Tall, narrow houses with painted shutters; "
      "chains across the harbour mouth; every second building a counting-house or a tavern. If Saltreach has a capital, this is it.")
place("blackwater", "Blackwater", "town", "saltreach", 295, 178,
      "A smugglers' town in a dark-water inlet under the southern tail of the Worldsend. Outlaws, sellsword companies between contracts, and no questions.")
place("saltings", "The Saltings", "landmark", "saltreach", 232, 178,
      "Salt marsh and tidal flats between Gullhaven and Corsa. Salt pans, wading birds, and a maze of channels that only the locals sail.")
place("drownedbell", "The Drowned Bell", "temple", "saltreach", 217, 203.5,
      "A temple that sank into the sea at the split of the old realm, now a reef pirates use as a landmark. At low spring tides you can hear what sounds like a bell. A sleep relic lies in its drowned hall. (Book 2)", secret=True)

# ---- Hearthmere's temple (beneath the Marches) ----
place("catacombs", "The Catacombs", "temple", "hearthmere", 174.8, 105.0,
      "Beneath Greyhold and running under the border to the Old Ruin: the catacombs where the Last Titan lies chained. Two locks, one under the school and one at the Ruin. "
      "Beyond the chains, in the deepest vault, Hearthmere's temple still holds the control relic, hidden by old magic. Hearthmere broke the Titan's own sleep relic long ago. (Books 1 and 2)",
      scope="both", secret=True, canon="established", label_dx=-2, label_dy=0.3)

# ---- Seas ----
SEAS = {
    "The Shattered Sea": (225, 222),
    "The Western Deep": (2, 110),
}

TRAVEL = {  # leagues per day
    "On foot": 8, "Grain cart or wagon": 7, "Horse (steady)": 14, "Horse (hard riding, one day)": 25,
    "Barge downstream on the Wend": 20, "Ship along the coast": 30, "Dragon": 80,
}
