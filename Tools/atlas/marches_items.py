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
item("mill", "Harrow mill", "mill", 179.0, 100.3, 2, "Hob's mill on Hollow Beck. His prices are how he says hello.", label=False)
item("shrine", "Crossroads shrine", "shrine", 178.6, 101.6, 2, "A stone shrine to the gods where the Drover's Way meets the river lane.", label=False)
item("weirs", "Eel weirs", "weir", 176.6, 108.9, 2, "Tolly's Staithe's eel traps, staked across the shallows.", label=False)
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
item("ramshead", "The Ram's Head", "inn", 181.2, 98.0, 4, "Drovers' inn on the Drover's Way, halfway between Harrow's End and Varrhold.", dx=0.2)
item("dragons4", "Dragons at the Roosts", "dragon", 187.8, 91.0, 4, "Dozens of Clan dragons on the cliffs and in the air above the hold.", label=False)
item("tocoldtarn", "to Coldtarn", "arrow_n", 191.6, 85.0, 4, "Hollow Beck rises at Coldtarn, where the Clan burns its dead.")

# ---------- Chapter 5: The Caged Beast (Maren) ----------
item("kettle", "The Kettle", "inn", 171.6, 113.6, 5, "Millbrook's tavern, where Saltreach boatmen drink and sell.", dx=-0.1, dy=0.4)
item("cagedbeast", "Caged beast", "beast", 173.4, 112.4, 5, "At Millbrook jetty, Saltreach poachers have a young beast in a cage. Maren frees it.", dx=0.2, dy=0.4)
item("littleweir", "Little Weir", "hamlet", 173.0, 117.0, 5, "A hamlet at the weir below Millbrook; flour barges wait here for the water.")
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
item("hobshole", "Hob's Hole", "cave", 184.8, 100.8, 16, "A cave in the hills east of Harrow's End where Calder hides with three dragons and asks them why.", dx=0.3)

# ---------- Chapter 18: The Village Burns (Calder) ----------
item("burn18", "Harrow's End burns", "fire", 178.0, 101.3, 18, "The civil war reaches the village again. Calder uses the dragons to save people for the first time.", label=False)
item("knights18", "Knights on the far bank", "watchers", 174.4, 100.6, 18, "Knights watch from the Hearthmere bank and don't cross.", label=False)

# ---------- Chapter 19: The Leader (Maren) ----------
item("raid19", "Raid on Ferriby", "battle", 171.0, 99.4, 19, "On patrol, Maren glimpses the Restoration's leader at a raid on Ferriby: one man, calm and persuasive.", label=False)

# ---------- Chapter 20: The Leader, Again (Calder) ----------
item("towendmouth", "to Wendmouth, 75 leagues", "arrow_s", 176.4, 123.0, 20, "Calder hears the leader speak in Wendmouth, on the same day Maren saw him at Ferriby.")

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
item("flee32", "Harrow's End flees", "path", 178.0, 101.3, 32, "The village packs carts and goes south down the Drover's Way.",
     path=[(178.0, 101.6), (178.4, 105.0), (179.4, 109.0), (180.4, 112.4)], label=False)

# ---------- Chapter 34: Two Men (Calder) ----------
item("twins34", "The twins' camp", "camp", 177.2, 104.8, 34, "Right before the battle, two men where everyone saw one.", dx=0.3)

# ---------- Chapter 35: War (Maren) ----------
item("war1", "War", "battle", 174.2, 111.0, 35, "The Restoration's first open war breaks out across the Marches.", dx=-0.2)
item("war2", "", "battle", 175.6, 97.0, 35, "Fighting along the river.", label=False)
item("war3", "", "battle", 172.4, 112.8, 35, "Millbrook burns.", label=False)
item("war4", "", "fire", 172.3, 112.2, 35, "Millbrook burns.", label=False)

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
