"""The Book 1 cast for a multi-voice production: who gets a voice of their own, and how the
speaker names in the annotations map to those voices. Every speaker without a role of their
own falls back to a shared voice by kind (man, woman, child), or to the narrator.

Edit freely; rebuild to regenerate Cast.md and the ElevenLabs voice map template.
"""
import re, zlib

# role, gender, age, voice note, aliases (speaker names used in the annotations)
ROLES = [
    ("Narrator", "-", "-", "British English, warm and unhurried, intimate rather than announcer-like; the backbone of the book. Reads all narration, written words and anything without a voice of its own.", []),
    # leads
    ("Maren", "F", "27", "Measured, precise, few words; dry humour at her own expense. Formal with superiors, blunt with peers. Under pressure her sentences get shorter, never louder. A river-watch Hearthmere voice: plain, not posh.", ["Maren Ashdown"]),
    ("Calder", "M", "32", "Plain and earthy, a Saltreach farmer; wry, tired humour; swears mildly. Talks to animals like friends and argues with the dragons out loud.", ["Calder Fenn", "Cal"]),
    # beasts (bond speech)
    ("Orrun", "M", "ancient", "The great lion. Slow and deep, like stone settling, with grief underneath. Few words. Must stay intelligible: deep, not processed.", ["the lion", "the Grey Mane"]),
    ("Aurveth", "F", "300+", "The oldest dragon. Long, measured, precise sentences; patient; guides rather than commands. An old woman's authority, never frail.", []),
    ("Kharrak", "M", "dragon", "Broad, scarred, battle-trained. Short, hard bursts; fragments. Fierce, protective. Rough but not a monster voice.", []),
    ("Lisska", "F", "dragon", "Lean, quick, restless; questions and teasing; jokes to avoid grief. Lighter and faster than the others.", []),
    # Calder's people
    ("Wren", "F", "9", "Calder's daughter. A real child's voice: clear, direct, curious. Must sound nine.", []),
    ("Ada", "F", "older", "Calder's mother. Knows the old songs; steady, dry, practical; can be sharp.", ["Ada Fenn"]),
    ("Bel", "F", "younger than Calder", "Calder's younger sister at Upper Rush. Quick, blunt; grief turns hard in her.", []),
    ("Joss", "M", "adult", "Bel's husband; breeds dray-beasts. Easy, practical.", []),
    ("Hob", "M", "older", "Harrow's End miller. Prices are how he says hello; wheedling, shrewd.", []),
    ("Fisk", "M", "old", "Old Fisk of the Eelweir; river man, sparing with words.", ["Old Fisk"]),
    ("Wat Garrow", "M", "adult", "Harrow's End farmer; blunt, neighbourly.", ["Wat", "Garrow", "old Garrow"]),
    # Greyhold
    ("Hale", "M", "past sixty", "Warden Osric Hale. Kind, tired, carrying a secret; a scholar's care with words.", ["Osric Hale", "Warden Hale"]),
    ("Pell", "M", "older", "Weapons instructor. Grey, laconic, dry. 'Subdue. Don't kill.'", ["Instructor Pell"]),
    ("Rowan", "F", "adult", "Knight-Captain Ilse Rowan. Clipped, commanding, cold under pressure.", ["Ilse Rowan", "Captain Rowan"]),
    ("Thorne", "F", "adult", "Captain Marta Thorne of the Watch. Hard, plain-spoken.", ["Marta Thorne"]),
    ("Haverly", "M", "21", "Lucan Haverly, the bonded rival. Gifted, certain, well-born; not cruel.", ["Lucan", "Lucan Haverly"]),
    ("Tobin", "M", "19", "Maren's friend. All elbows; loud about being unchosen; warm.", []),
    ("Grieve", "M", "older", "Master of Stables. Gruff.", []),
    ("Ottery", "M", "older", "Maren's old river-watch sergeant. Unhurried, gravelly, fond under it.", ["Sergeant Ottery"]),
    ("Liss", "F", "older", "Maren's mother, the ferrywoman. Tells the river's stories; warm, weathered, knowing.", ["Liss Ashdown"]),
    ("Tam", "M", "19", "Maren's brother, a smith's apprentice. Eager, easily fired up.", ["Tam Ashdown"]),
    # the Clan
    ("Teo", "M", "young", "Teo Varr, the younger son. Warm and well liked.", ["Teo Varr"]),
    ("Arn", "M", "young", "Arn Varr, the elder son. Proud, sharp, grieving.", ["Arn Varr"]),
    ("Ulric", "M", "older", "Ulric Varr, the uncle and warrior. Big, confident, dangerous.", ["Ulric Varr"]),
    ("Hallam", "M", "old", "Hallam Brecc, oldest rider on the ledges. Slow, grave.", ["Hallam Brecc"]),
    ("Sigrun", "F", "76", "Sigrun Holm, Aurveth's rider. An old war-leader.", ["Sigrun Holm"]),
    ("Imra", "F", "adult", "Imra Sallow, Lisska's rider. Quick and laughing.", ["Imra Sallow"]),
    # the Restoration and others
    ("Rook", "M", "adult", "A forgettable, pleasant voice that never rises; quietly menacing.", []),
    ("Corvin", "M", "adult", "Corvin Vale. Still, patient, never raises his voice. Same timbre as Cassian, colder.", ["Corvin Vale", "the thin man"]),
    ("Cassian", "M", "adult", "Cassian Vale, the public face. Same timbre as Corvin, warm and open: a speaker who wins crowds.", ["Cassian Vale", "Vale"]),
    ("the Captain", "M", "adult", "Leader of the island hunters. Saltreach voice; curt.", []),
    ("Coll Brask", "M", "adult", "Wendmouth sellsword. Mercenary candour.", ["Brask"]),
    ("Gannet", "M", "adult", "Saltreach boatman and poacher; a smile that arrives first.", []),
]

NARRATOR_SPEAKERS = re.compile(r"^(crowd|villagers?|the villagers|students|the knights|the river people|the Clan|the Clan's riders|the Marches|the Saltreach bank|the pedlars|the stall-holders|the instructors|the dragons|all three|Kharrak and Aurveth)$", re.I)
CHILD = re.compile(r"\b(boy|girl|child|Davy|Pip|Nan)\b", re.I)
WOMAN = re.compile(r"\b(woman|wife|widow|mother|girl|fishwife|Rue|Greta|Gunna|Tessa|Senna|Ide|Tamsin|camp woman)\b", re.I)

GENERIC = {"man": ["Man 1", "Man 2", "Man 3"], "woman": ["Woman 1", "Woman 2"], "child": ["Child"]}
GENERIC_NOTES = {
    "Man 1": "Shared voice for minor men (one of three, assigned by name so each minor speaker keeps one voice).",
    "Man 2": "Shared voice for minor men; contrast with Man 1 (age or weight).",
    "Man 3": "Shared voice for minor men; an older or rougher contrast.",
    "Woman 1": "Shared voice for minor women.",
    "Woman 2": "Shared voice for minor women; contrast with Woman 1.",
    "Child": "Shared voice for minor children and boys (Davy, Pip, messenger boys). Different from Wren.",
}

_ALIAS = {}
for r, g, a, note, aliases in ROLES:
    _ALIAS[r.lower()] = r
    for x in aliases:
        _ALIAS[x.lower()] = r


def role_of(speaker):
    """Map an annotation speaker name to a voice role."""
    if not speaker:
        return "Narrator"
    s = speaker.strip()
    if s.lower() in _ALIAS:
        return _ALIAS[s.lower()]
    if NARRATOR_SPEAKERS.match(s):
        return "Narrator"
    kind = "child" if CHILD.search(s) and not re.search(r"woman|mother", s, re.I) else "woman" if WOMAN.search(s) else "man"
    pool = GENERIC[kind]
    return pool[zlib.crc32(s.lower().encode()) % len(pool)]


def all_roles():
    out = [(r, g, a, n) for r, g, a, n, _ in ROLES]
    for k in ("Man 1", "Man 2", "Man 3", "Woman 1", "Woman 2", "Child"):
        out.append((k, "F" if k.startswith("Woman") else "-" if k == "Child" else "M", "-", GENERIC_NOTES[k]))
    return out
