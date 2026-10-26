"""The Marches, lived in. Every item carries `ch`: the chapter in which it first appears in Book 1.
The chapter-end map for chapter N shows everything with ch <= N, and rings what is new in N.
Chapter 0 is the bare map in the book's front matter.
Positions are leagues (x east, y south). Plot-event placements follow Book 1/Chapter_Plan.md and are working proposals.
"""

# When existing places from world.py first appear
REVEAL = {
    "greyhold": 1, "oldruin": 1, "millbrook": 1, "ferrylanding": 1,
    "harrowsend": 2, "calderfarm": 2, "hollowbeck": 2, "upperrush": 2, "tollysstaithe": 2, "varrhold": 2, "cotterscross": 2,
    "northwatch": 3, "redwatch": 3, "brackenwood": 3,
    "scarfell": 4, "ewehollow": 4, "reedmarsh": 5, "coldtarn": 4,
    "catacombs": 27,
}

ROAD_REVEAL = {"The River Road": 1, "The River Road (south)": 1, "The King's Road": 3, "The Drover's Way": 2, "ONEROAD": 9}

LABEL_REVEAL = {"River Wend": 1, "HEARTHMERE": 1, "SALTREACH": 2, "the Oneroad": 9, "the Drover's Way": 2,
                "the River Road": 1, "the King's Road": 3}

# Ambient farmsteads: unnamed, they make the land look lived in. Hearthmere side with Maren (ch 1),
# Saltreach side with Calder (ch 2).
AMBIENT = [
    # Hearthmere bank
    (170.2, 88.5, 1), (172.4, 90.6, 1), (170.6, 95.2, 1), (171.8, 97.4, 1), (169.4, 101.2, 1), (171.2, 103.2, 1),
    (170.0, 109.4, 1), (171.6, 115.6, 1), (170.4, 118.2, 1), (172.8, 120.6, 1), (168.4, 116.0, 1), (169.0, 121.6, 1),
    # Saltreach bank
    (179.4, 88.0, 2), (180.6, 91.2, 2), (182.4, 99.2, 2), (183.6, 102.4, 2), (181.2, 104.8, 2), (179.0, 106.4, 2),
    (182.4, 108.2, 2), (184.6, 110.6, 2), (179.4, 117.0, 2), (183.0, 116.4, 2), (186.8, 107.4, 4), (188.4, 104.6, 4),
    (184.8, 89.2, 4), (190.0, 96.8, 4),
]

ITEMS = []
def item(id, name, kind, x, y, ch, desc, label=True, path=None, dx=0.0, dy=0.0):
    ITEMS.append(dict(id=id, name=name, kind=kind, x=x, y=y, ch=ch, desc=desc, label=label, path=path, dx=dx, dy=dy))

# ---------- Chapter 1: The Unchosen Yard (Maren) ----------
item("dragons1", "Clan dragons, flying south", "dragon", 177.4, 92.0, 1,
     "Seven Clan dragons follow the river south past Greyhold just before noon.", dx=0.6)
item("fires1", "Fires on the far bank", "fire", 178.0, 98.7, 1,
     "Three fires seen from Greyhold's river wall at dusk. Not stubble.", label=False)
item("toashford", "to Ashford, 18 leagues", "arrow_w", 165.4, 106.3, 1, "The King's Road runs west to Ashford and Hallowmere.")

# ---------- Chapter 2: Across the River (Calder) ----------
item("mill", "Harrow mill", "mill", 177.7, 103.2, 2, "Hob's mill on Hollow Beck. His prices are how he says hello.", label=False)
item("shrine", "Crossroads shrine", "shrine", 177.8, 103.3, 2, "A stone shrine to the gods where the Drover's Way meets the river lane.", label=False)
item("weirs", "Eel weirs", "weir", 175.0, 108.0, 2, "Tolly's Staithe's eel traps, staked across the shallows.", label=False)
item("pyre", "Pyre smoke over Varrhold", "smoke", 185.2, 92.6, 2, "The old chief's funeral pyre burns for three days.", label=False)
item("burnedrush", "Upper Rush, burned", "fire", 178.0, 98.7, 2, "Raided at night for its beasts, then burned. Harrow's End blames the Clan's quarrel.", label=False)

# ---------- Chapter 3: Roads and Roadblocks (Maren) ----------
item("ferriby", "Ferriby", "hamlet", 171.0, 99.4, 3, "A Hearthmere hamlet of a dozen houses and a smithy, a league inland from Redwatch.")
item("roadblock", "Roadblock", "roadblock", 173.4, 95.4, 3, "A Restoration roadblock on the River Road. Travellers talk of a leader seen in two places in one day.")
item("charcoal", "Charcoal burners", "camp_plain", 167.2, 103.4, 3, "Charcoal burners' clearing in the Brackenwood, licensed by the crown.", dy=-0.2)
item("boar", "Boar", "beast", 166.6, 108.8, 3, "Wild boar in the Brackenwood, big enough that the patrol goes round.")
item("penfold", "Penfold", "hamlet", 169.4, 92.6, 3, "Shepherds' hamlet on the high ground west of the River Road.")
item("shrine_rr", "Wayside shrine", "shrine", 173.0, 93.4, 3, "A roadside shrine on the River Road, hung with ribbons for the drowned.", label=False)

# ---------- Chapter 4: The Uncle and the Sons (Calder) ----------
item("roosts", "The Roosts", "eyrie", 186.2, 93.0, 4, "Dragon eyries cut into the cliff above Varrhold, black at the mouths.", dx=0.2)
item("ramshead", "The Ram's Head", "inn", 180.9, 99.0, 4, "Drovers' inn on the Drover's Way, halfway between Harrow's End and Varrhold.", dx=0.2)
item("dragons4", "Dragons at the Roosts", "dragon", 187.8, 91.0, 4, "Dozens of Clan dragons on the cliffs and in the air above the hold.", label=False)
item("tocoldtarn", "to Coldtarn", "arrow_n", 191.6, 85.0, 4, "Hollow Beck rises at Coldtarn, where the Clan burns its dead.")

# ---------- Chapter 5: The Caged Beast (Maren) ----------
item("kettle", "The Kettle", "inn", 173.4, 109.3, 5, "Millbrook's tavern, where Saltreach boatmen drink and sell.", dx=-0.1, dy=0.4)
item("cagedbeast", "Caged beast", "beast", 174.3, 108.6, 5, "At Millbrook jetty, Saltreach poachers have a young beast in a cage. Maren frees it.", dx=0.2, dy=0.4)
item("littleweir", "Little Weir", "hamlet", 174.2, 111.2, 5, "A hamlet at the weir below Millbrook; flour barges wait here for the water.")
item("gallowsoak", "Gallows Oak", "landmark_pt", 170.6, 115.0, 5, "A crossroads oak where Hearthmere hanged poachers until fifty years ago. Children still won't climb it.", label=False)

# ---------- Chapter 6: Whispers in the Hold (Calder) ----------
item("moot", "Moot-stone", "shrine", 183.4, 93.6, 6, "The standing stone outside Varrhold's rampart where the Clan settles disputes.", label=False)

# ---------- Chapter 7: The Trial (Maren) ----------
item("ruinisland", "Ruin Island", "area_small", 176.0, 102.2, 7, "The wooded island where the Wend splits. Nobody lands there.", dx=-2.6, dy=-0.5)
item("boathouse", "Redwatch boathouse", "pier", 174.0, 99.4, 7, "The river watch's patrol boats. Maren takes one out to the island.", label=False)

# ---------- Chapter 8: The Younger Son (Calder) ----------
item("teofell", "Where Teo Varr fell", "death", 183.0, 96.0, 8, "The chief's younger son found dead at the ford of Hollow Beck, apparently by the uncle's men.", dx=0.2)

# ---------- Chapter 9: The Old Ruin (Maren) ----------
item("verse", "The carved verse", "verse", 175.7, 103.2, 9, "A verse about Winshire, carved under the tower arch.", label=False)
item("huntcamp", "Hunters' camp", "camp", 175.9, 104.4, 9, "Signs of hunters on the island: cold fires, cut chains, beast traps.", dx=0.4, dy=0.2)

# ---------- Chapter 10: Three Deaths (Calder) ----------
item("threefell", "Where three warriors fell", "battle", 178.6, 103.4, 10, "The Clan's battle spills onto the Fenn fields. Sigrun Holm, Dag Rorke and Imra Sallow die here, and their dragons come to Calder.", dx=0.3, dy=0.6)

# ---------- Chapter 11: The Roar (Maren) ----------
item("lion11", "The lion", "lion", 176.3, 102.4, 11, "The ancient lion wakes on Ruin Island.", dx=0.5, dy=-0.4)

# ---------- Chapter 13: Wounded (Maren) ----------
item("chained13", "Where the lion was chained", "chain", 175.5, 104.8, 13, "Restoration hunters chain the lion at the island's south tip. Maren breaks a chain and lets it go.", label=False)

# ---------- Chapter 14 and 16: Hunted, Why Me? (Calder) ----------
item("flight", "Calder's flight", "path", 177.7, 102.6, 14, "Calder flees the village with the dragons, up into the hills.",
     path=[(177.7, 102.6), (179.6, 103.2), (182.0, 102.4), (184.8, 100.8)], label=False)
item("hunters14", "Dragon hunters", "camp", 181.4, 106.2, 14, "Sellswords and strangers paid in Restoration coin, tracking the dragons.", dx=0.3)
item("hobshole", "Crow Scar", "cave", 184.8, 100.8, 16, "A cave at Crow Scar in the hills east of Harrow's End, where Calder hides with three dragons and asks them why.", dx=0.3)

# ---------- Chapter 18: The Village Burns (Calder) ----------
item("burn18", "Harrow's End burns", "fire", 178.0, 101.3, 18, "The civil war reaches the village again. Calder uses the dragons to save people for the first time.", label=False)
item("knights18", "Knights on the far bank", "watchers", 174.4, 100.6, 18, "Knights watch from the Hearthmere bank and don't cross.", label=False)

# ---------- Chapter 19: The Leader (Maren) ----------
item("raid19", "Raid on Ferriby", "battle", 171.0, 99.4, 19, "On patrol, Maren glimpses the Restoration's leader at a raid on Ferriby: one man, calm and persuasive.", label=False)

# ---------- Chapter 20: The Leader, Again (Calder) ----------
item("towendmouth", "to Wendmouth, 100 leagues", "arrow_s", 176.4, 123.0, 20, "Calder hears the leader speak in Wendmouth, on the same day Maren saw him at Ferriby.")

# ---------- Chapter 21: Without Words (Maren) ----------
item("liongrnd", "The lion's ground", "lion", 175.6, 103.6, 21, "Maren keeps returning. The lion tolerates her at a distance.", label=False)

# ---------- Chapter 24: Crossing the River (Calder) ----------
item("crossing24", "Calder's crossing", "path", 178.6, 102.3, 24, "Calder reaches the Old Ruin, hiding the dragons, and narrowly misses Maren and the lion.",
     path=[(184.8, 100.8), (181.6, 101.6), (179.2, 102.2), (177.4, 103.0), (176.4, 103.4)], label=False)

# ---------- Chapter 25: The Accusation (Maren) ----------
item("procl", "The Restoration's proclamation", "scroll", 172.8, 107.6, 25, "Proclamations nailed to Greyhold's gate and Millbrook's jetty: Hearthmere keeps a Titan in chains.", label=False)

# ---------- Chapter 27: Confession (Maren) ----------
# the catacombs (world.py) appear here

# ---------- Chapter 28: The Gathering (Calder) ----------
item("muster1", "Restoration muster", "camp", 183.4, 90.6, 28, "Restoration forces gathering in the Marches.", dx=0.3)
item("muster2", "", "camp", 185.6, 87.8, 28, "Restoration forces gathering in the Marches.", label=False)
item("muster3", "", "camp", 182.0, 86.6, 28, "Restoration forces gathering in the Marches.", label=False)

# ---------- Chapter 30: Two Sides of a War (Calder) ----------
item("uncle", "Ulric's camp", "camp", 186.6, 96.0, 30, "The uncle's war camp below Varrhold.", dx=0.2)
item("arn", "Arn's camp", "camp", 181.8, 94.6, 30, "The elder son's camp, across Hollow Beck from his uncle's.", dx=-2.8, dy=-0.2)

# ---------- Chapter 31: Orders (Maren) ----------
item("trap31", "The orders' trap", "roadblock", 174.4, 102.6, 31, "The inner circle orders Maren to lure the lion here. She refuses.", label=False)

# ---------- Chapter 32: Before the Storm (Calder) ----------
item("flee32", "Harrow's End flees", "path", 177.3, 103.0, 32, "The village packs carts and goes south down the Drover's Way.",
     path=[(178.0, 101.6), (178.4, 105.0), (179.4, 109.0), (180.4, 112.4)], label=False)

# ---------- Chapter 34: Two Men (Calder) ----------
item("twins34", "The twins' camp", "camp", 177.2, 104.8, 34, "Right before the battle, two men where everyone saw one.", dx=0.3)

# ---------- Chapter 35: War (Maren) ----------
item("war1", "War", "battle", 174.2, 111.0, 35, "The Restoration's first open war breaks out across the Marches.", dx=-0.2)
item("war2", "", "battle", 175.6, 97.0, 35, "Fighting along the river.", label=False)
item("war3", "", "battle", 172.4, 112.8, 71, "Millbrook burns.", label=False)
item("war4", "", "fire", 172.3, 112.2, 71, "Millbrook burns.", label=False)

# ---------- Chapter 36: The Second Lock (Calder) ----------
item("lock_ruin", "The Ruin's lock", "lock", 175.8, 103.8, 36, "One of the two locks of the seal, beneath the Old Ruin.", dx=-3.6, dy=0.4)
item("lock_school", "The school's lock", "lock", 173.9, 106.2, 36, "The other lock, deep beneath Greyhold.", dx=-3.6, dy=-0.4)
item("farseer", "The Far-Seer's flight", "path", 176.0, 103.6, 36, "Calder sends the Far-Seer to warn whoever is at the other lock.",
     path=[(176.2, 103.4), (175.6, 104.6), (174.6, 105.8), (174.0, 106.6)], label=False)

# ---------- Chapter 37: The Sacrifice (Maren) ----------
item("bond37", "Where the bond formed", "bond", 171.6, 104.4, 37, "Bond-forcers trap the lion at the edge of the Brackenwood. Maren offers her life into the binding, and the bond forms.", dx=-0.2, dy=0.8)

# ---------- Chapter 38: Fire at the Ruin (Calder) ----------
item("fire38", "Fire at the Ruin", "fire", 176.4, 104.0, 38, "Calder and the dragons fight Corvin Vale at the Ruin's lock, and can't stop it opening.", label=False)

# ---------- Chapter 39: The Lock Gives Way (Maren) ----------
item("cassian", "Where Cassian Vale fell", "death", 173.6, 106.9, 39, "Beneath the school, Maren kills Cassian Vale as his lock gives way.", dx=-0.4, dy=0.9)

# ---------- Chapter 40: Underground (Calder) ----------
item("meet40", "They meet", "meet", 174.9, 104.9, 40, "Coming from opposite ends beneath the border, Maren and Calder meet for the first time.", dx=0.4, dy=0.3)

# ---------- Chapter 41: The Last Titan (Maren) ----------
item("titan41", "Where the Last Titan rose", "titan", 174.9, 105.0, 41, "The Last Titan tears free of its chains and flies. Hearthmere's magic flickers and fails.", dx=0.9, dy=-1.6)
item("titanflight", "It flew east", "arrow_ne", 189.6, 86.6, 41, "Its path, as the two of them watched it go.")


# ---------------- the whole of Winshire ----------------
# When realm-scale names first appear in Book 1. 99 = not in Book 1 (later books).
LATER = 99
REALM_REVEAL = {
    "ashford": 1, "greyhold": 1, "oldruin": 1, "harrowsend": 2, "varrhold": 2, "cotterscross": 2,
    "wendmouth": 20, "hallowmere": 25, "mere": 25,
}
KINGDOM_REVEAL = {"hearthmere": 1, "saltreach": 1, "kessmoor": 3, "sarovel": 3, "isvaren": 3, "wyldmarch": 3}
BORDER_REVEAL = 3
REALM_LABEL_REVEAL = {
    "The Shattered Sea": 2, "The Western Deep": LATER, "The Scarfell": 2, "THE MARCHES": 1, "Wend": 1, "the Oneroad": 9,
}
REALM_ROAD_REVEAL = {
    "The King's Road": 1, "The River Road": 1, "The River Road (south)": 1, "The Drover's Way": 2,
    "The Coast Road": 20, "The Saltreach Track": 20,
}


# ---------------- Expanded plan: renumber the 41-chapter tags, then add the new chapters ----------------
# Everything above was tagged with the original 41-chapter numbers (except the two Millbrook items, now 71 in new terms).
from plan_data import OLD_TO_NEW as _O
_NEW_ALREADY = {"war3", "war4"}
def _r(ch):
    return _O.get(ch, ch) if ch < LATER else ch
REVEAL = {k: _r(v) for k, v in REVEAL.items()}
ROAD_REVEAL = {k: _r(v) for k, v in ROAD_REVEAL.items()}
LABEL_REVEAL = {k: _r(v) for k, v in LABEL_REVEAL.items()}
AMBIENT = [(x, y, _r(c)) for (x, y, c) in AMBIENT]
for _it in ITEMS:
    if _it["id"] not in _NEW_ALREADY:
        _it["ch"] = _r(_it["ch"])
REALM_REVEAL = {k: _r(v) for k, v in REALM_REVEAL.items()}
KINGDOM_REVEAL = {k: _r(v) for k, v in KINGDOM_REVEAL.items()}
BORDER_REVEAL = _r(BORDER_REVEAL)
REALM_LABEL_REVEAL = {k: _r(v) for k, v in REALM_LABEL_REVEAL.items()}
REALM_ROAD_REVEAL = {k: _r(v) for k, v in REALM_ROAD_REVEAL.items()}

# adjustments for the new chapters
REVEAL["tollysstaithe"] = 3      # Maren crosses on the ferry in chapter 3
REVEAL["coldtarn"] = 8           # the ashes are scattered on Coldtarn
for _it in ITEMS:
    if _it["id"] == "tocoldtarn":
        _it["ch"] = 8

item("fair", "Harvest fair", "fire_plain", 178.9, 101.9, 12, "Harrow's End's harvest fair and bonfire. Teo Varr dances with Bel's girls and talks of peace.", label=False)
item("ice41", "Where the ice broke", "ice", 175.0, 108.4, 41, "A refugee family tries to walk across the frozen Wend. Maren goes after them; the ice breaks, and something huge pulls her out.", dx=0.3)
item("rcamp50", "Restoration beast camp", "camp", 183.6, 107.0, 50, "The camp that holds Joss's other grey. Joss goes looking for it and is brought back dead.", dx=0.3)
item("burn52", "Kharrak's fire", "fire", 183.6, 107.0, 52, "Calder lets Kharrak burn the camp and free its beasts. The Restoration names him an enemy.", label=False)
item("ford60", "Ambush at the ford", "battle", 183.0, 96.0, 60, "Calder's peace meeting at Teo's ford becomes an ambush.", dx=0.3, dy=0.6)
item("ferry64", "Refugees cross", "path", 174.7, 107.1, 64, "Ada, Wren and Bel's family cross to Hearthmere on Liss Ashdown's ferry.",
     path=[(177.0, 108.5), (175.8, 108.0), (174.6, 107.5)], label=False)
item("pell69", "Where Pell fell", "death", 172.9, 106.2, 69, "Instructor Pell dies holding Greyhold's gate.", dx=-0.3, dy=-0.9)
item("rook72", "Where Rook died", "death", 177.0, 104.4, 72, "Calder corners Rook in the fighting at the Ruin. The proof dies with him.", dx=0.3)
item("brandt75", "Where Haverly and Kesh fell", "death", 174.6, 107.2, 75, "Greyhold is breached. Kesh is killed, and Haverly dies in Maren's arms.", dx=0.4, dy=0.9)


# ---------------- Reconciled with the drafted Chapters 11-40 (new numbering) ----------------
def _set(id, **kw):
    for _it in ITEMS:
        if _it["id"] == id:
            _it.update(kw)
_set("hobshole", ch=24, x=179.6, y=102.2, desc="Crow Scar: a black crag standing out of the Fellwood two leagues east of the Fenn farm, with a cave three-quarters up its face. Calder hides there with the three dragons (24-32).")
_set("flight", ch=24, path=[(177.7, 102.3), (178.6, 102.0), (179.6, 102.2)])
_set("burn18", x=177.3, y=103.0)
_set("knights18", x=174.9, y=103.2)
_set("fair", x=177.4, y=102.7)
_set("teofell", x=182.9, y=96.6)
_set("ford60", x=182.9, y=96.6)
_set("crossing24", path=[(179.6, 102.2), (178.4, 102.6), (177.3, 103.0), (176.4, 103.2), (175.8, 103.5)])
_set("weirs", desc="Tolly's Staithe's eel traps, staked across the shallows by the ferry.")
item("eelweir", "The Eelweir", "weir", 176.6, 103.1, 2, "Harrow's End's fishing landing at the mouth of Hollow Beck, opposite the Old Ruin. Old Fisk and his sons keep it.", dx=0.2)
item("shieling14", "Burned shieling at the ford", "fire", 183.1, 96.3, 14, "Teo is found dead at the ford; the gorse and the shepherd's shieling are fired.", label=False)
item("huntcamp15", "Hunters' camp", "camp", 175.2, 102.9, 15, "Restoration hunters' cache under a bluff on the island's north-west shore: chains, stakes, a cage.", label=False)
item("skarrow16", "Skarrow", "hamlet", 191.0, 95.0, 16, "Ulric's own steading on the east side of the Scarfell, where he takes most of the fighting men.", dx=0.3)
item("millburn18", "Mill burned", "fire", 177.6, 103.2, 18, "Arn fires Hob's mill and Ulric's flour; the battle spills onto the Fenn fields.", label=False)
item("lowgarth28", "Low Garth, burned", "fire", 181.6, 98.4, 28, "A west-side farm under Hollow Beck, burned by Ulric's men for selling to the hold.", label=False)
item("holloway32", "Holloway, burned", "fire", 171.6, 100.8, 32, "A Hearthmere hamlet near Redwatch, burned; the knights ride out to it on their own bank.", label=False)
item("ferriby33", "Raid on Ferriby", "battle", 171.0, 99.4, 33, "Corvin Vale directs the raid from the smithy roof like a game of stones.", label=False)
item("rcamps38", "Restoration camps", "camp", 180.0, 140.0, 38, "Refugee camps on the drove road up the Wend, with drill fields of bound beasts behind them.", dx=0.3)
item("redwatch39", "Skirmish at Redwatch landing", "battle", 173.6, 99.6, 39, "Raiders with bound hounds try to stave the patrol boats. Bracken is killed.", label=False)
item("hatching40", "Old hatching caves", "cave", 194.0, 76.0, 40, "The Clan's old hatching caves above Coldtarn, unused for a hundred years. The dragons winter there.", dx=0.3)

_set("ruinisland", label=False)
_set("hobshole", keep=True)
_set("eelweir", keep=True, dx=-1)


# ---------------- Reconciled with the drafted Chapters 41-60 ----------------
_set("ice41", x=176.3, y=102.8, desc="Day 79: the Haddow family try to walk from the Eelweir to the island on the new ice. Maren goes out flat with a rope; the man goes through, she goes in after him, and something huge breaks the ice from above and drags them both onto the island shore.")
_set("crossing24", desc="Night 81: Calder crosses the ice alone from the Eelweir to the Old Ruin, finds the cut chain on the spit and the woman's fire, and backs away from the lion under the oaks.")
_set("procl", desc="Midwinter (day 88): the Restoration's paper is nailed inside Greyhold's river gate and read at the Millbrook frost fair: Hearthmere keeps the Last Titan in chains under Greyhold.")
_set("uncle", x=190.6, y=95.6, label=False, desc="Ulric at Skarrow. Calder flies there on day 96 to ask him to stop the war. He won't, until someone shows him who killed Teo.")
_set("arn", x=184.0, y=95.4, label=False, desc="Arn at Varrhold. Calder lands in the hold's yard on day 93 to ask him to stop. He won't; he wants the knight who sits with monsters.")
_set("rcamp50", x=177.4, y=106.0, name="Ewe Beck camp", desc="The Restoration camp at the mouth of the Ewe Beck, holding Joss's grey. Joss goes in at night to cut him loose and is brought back dead (day 100).")
_set("burn52", x=177.4, y=106.0, desc="Night 103: Kharrak burns the Ewe Beck camp's lines, stores and binding tent; three handlers die; Old Grey comes home empty. Greyhold's bell rings. The Restoration names Calder an enemy.")
_set("muster1", x=181.2, y=99.5, name="The muster at the Ram's Head", desc="From day 106 the Restoration's camps empty into one town of tents at the Ram's Head crossroads: about five thousand men and a quarter-mile of bound beasts.", dx=0.3)
_set("muster2", x=180.6, y=105.0, desc="Companies coming up the river road from Cotter's Cross to the Ram's Head.")
_set("muster3", x=181.6, y=97.6, desc="The Ram's Head camp spills up the hill behind the inn.")
_set("trap31", x=175.3, y=102.6, desc="Day 127: the council's order. A pit-net and the crown's beast-chain on the island's west shore; Maren is to lead the lion onto it. She refuses three times.")
_set("ford60", desc="Day 130: Calder's truce meeting at Teo's ford. He names Rook; Ulric's face changes; then sixty strangers in both sides' colours shoot from the gorse. Hallam Brecc falls.")
item("listen44", "Where Aurveth listened", "ice", 176.6, 100.9, 44, "Midwinter night (day 88): Aurveth lies on the ice with her throat to it a league above the island and touches something vast and chained below.", label=False)
item("frostfair45", "Frost fair riot", "battle", 173.5, 108.3, 45, "Midwinter: Reede reads the paper at the Millbrook frost fair; Callis tries an arrest; the crowd turns.", label=False)
item("riot47", "Millbrook riot", "battle", 173.5, 109.1, 47, "Day 93: the knights arrest Davin the potboy for reading the paper; the town riots.", label=False)
item("flight48", "Calder flies to the Varrs", "path", 179.6, 102.2, 48, "Days 93 and 96: Calder flies openly to Varrhold and to Skarrow to ask Arn and Ulric to stop.",
     path=[(179.6, 102.2), (182.0, 98.6), (184.4, 94.8), (188.0, 94.6), (191.0, 95.0)], label=False)
item("door51", "The black door", "lock", 174.1, 106.4, 51, "Night 102: Hale takes Maren to the black door under the archive. Her hand on it; something far below notices; across the river the lion roars and three dragons answer.", label=False)
item("pit53", "The lion's pit", "area_small", 176.1, 101.8, 53, "At the island's north end the lion has dug down all winter to a course of dressed grey stone running under the river toward Greyhold. It's trying to get down to its kin.", dx=0.3)
item("hill54", "Fight above Upper Rush", "battle", 177.6, 101.4, 54, "Night 105: a hundred men with bound hounds come up the fields for Calder. The dragons drive them off; eleven dead.", label=False)
item("road54", "The road to the river", "path", 181.2, 99.5, 54, "A new road trodden black from the Ram's Head over the hills behind Harrow's End, down to the water opposite the island.",
     path=[(181.2, 99.5), (180.0, 100.6), (178.8, 101.8), (177.8, 102.4), (176.9, 102.7)], label=False)
item("collar55", "The collar struck off", "chain", 175.8, 102.3, 55, "Night 119 the river goes out with Maren on the island. At dawn the lion lays its neck down and she strikes the pin out. Odo Marl's crossed hammers are on the inside.", label=False)
item("hedge57", "Hedge-meeting", "camp", 172.8, 109.6, 57, "Night 123: seven hundred people under the long thorn hedge above Fennick's. Vale speaks, warm; Tobin begs Maren to come over; Tam holds the torch.", dx=-2.6)
item("hallam60", "Where Hallam Brecc fell", "death", 183.2, 96.2, 60, "The old rider of the ledges goes down the slope shouting that the shooters aren't kin, and a bolt takes him. Morrow lies down beside him.", label=False)
item("boats60", "Knights' boats", "pier", 176.3, 103.4, 60, "At dusk on day 130, Greyhold's boats sit at anchor across the mouth of Hollow Beck, watching the ford's dead come down into the Wend. They don't cross.", label=False)
# Redwatch sits on the Hearthmere bank opposite the island, across the west channel (Chs 25-55)
_set("boathouse", x=174.9, y=102.1)
_set("redwatch39", x=175.0, y=103.2)


# ---------------- Reconciled with the drafted Chapters 61-79 ----------------
_set("flee32", desc="Days 132-137: Harrow's End packs and goes south down the river lane to Tolly's Staithe and Liss Ashdown's ferry. Fisk stays at the Eelweir.",
     path=[(177.3, 103.0), (177.5, 105.0), (177.4, 107.0), (177.2, 108.6)])
_set("twins34", x=175.9, y=102.6, label=False, desc="Night 141: under the arch, Corvin and Cassian Vale stand together: the leader in two places was always two men. Rook tells them how Teo died.")
_set("war1", x=174.6, y=101.7, name="War at Redwatch", desc="Day 142: the Restoration crosses the west channel from the island with ladders and boats against the orders on the bank at Redwatch.", dx=-3.4, dy=-0.4)
_set("war2", x=173.0, y=113.4, desc="Dawn, day 142: the rising burns the refugee camp by Millbrook's water-meadows.")
_set("pell69", x=174.3, y=106.3, desc="Day 142: Pell opens Greyhold's river gate for the refugees, holds the gateway, and dies there at the noon bell with his back to the shut gate.")
_set("farseer", desc="Dawn, day 143: Calder sends Lisska west with the first chain, a strip of shirt burned TWO, and Wren's ribbon on her horn.",
     path=[(178.2, 101.9), (176.6, 101.6), (174.4, 101.7), (172.4, 102.0), (171.1, 102.3)])
item("knowe67", "Hollin Knowe", "area_small", 171.0, 102.3, 67, "A long rise at the Brackenwood's edge, four leagues west of the river, with the old watch's beacon-stones on top. Maren and the lion watch the muster from it.", dx=-3.0)
_set("bond37", x=171.1, y=102.5, label=False, desc="Night 143: bond-forcers ring the lion with honey-smoke on Hollin Knowe. Maren gives herself into the binding in its place, and the lion accepts. Its name is Orrun.")
_set("fire38", desc="Dusk, night 143: Kharrak and Aurveth burn the Restoration's camp on the island; Calder goes down the stair under the tower to the Ruin's lock.")
_set("rook72", x=175.8, y=104.6, desc="Night 143: Calder corners Rook on the spit by the hunters' stake. Rook goes at him with the six-knife so Kharrak will kill him, and Kharrak does. The proof dies with him.")
_set("brandt75", x=174.1, y=106.4, desc="Night 143: Kesh is shot out of the air over the north tower stair, and Haverly dies on the steps in Maren's arms.")
_set("cassian", desc="Midnight, night 143: beneath the school, Maren kills Cassian Vale at the knight's lock; his hand turns the key as he falls.")
_set("meet40", x=175.4, y=103.4, desc="After midnight: at the foot of the fallen Ruin, in the cavern under the river, Maren and Calder meet for the first time.")
_set("titan41", x=176.0, y=102.9, desc="Sunrise, day 144: the Last Titan comes up out of the river where the island was and flies north-east. Hearthmere's lamps go out.")
_set("oldruin", desc="Broken arches and a squat round tower on a wooded island where the Wend splits, about three leagues upriver of Greyhold. It fell into the catacombs at midnight on night 143, when the seal opened.")
_set("knowe67", x=174.0, y=102.6, desc="A long rise at the Brackenwood's edge, two leagues west of the river, with the old watch's beacon-stones on top. Maren and the lion watch the muster from it.")
_set("bond37", x=172.5, y=102.5)
_set("farseer", path=[(178.2, 101.9), (176.6, 101.6), (174.4, 101.7), (172.5, 102.3)])
_set("titan41", dx=2.6, dy=3.4, keep=True)
_set("titanflight", name="It flew north-east")
