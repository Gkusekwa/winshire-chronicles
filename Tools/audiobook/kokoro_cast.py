"""The Book 1 cast for Kokoro: a voice for every role in Cast.md (roles come from cast.role_of), plus how
mood and the scripts' "how" notes shape pace and level. Edit freely: change a voice, a blend or a pitch and
re-render.

Voice: a Kokoro voice name, or a blend "bf_alice*0.6+bf_emma*0.4" (style vectors mixed in those proportions).
Pitch: semitones (negative is deeper), applied after rendering without changing the pace.
Speed: multiplies the pace set by the kind of words and the mood. Gain: dB.
"""

# role: (voice, pitch, speed, gain)
CAST = {
    "Narrator":   ("bf_emma", 0, 1.00, 0),
    # leads
    "Maren":      ("bf_isabella", 0, 1.00, 0),
    "Calder":     ("bm_george", 0, 1.00, 0),
    # beasts (their bond speech is closer and quieter on top of this)
    "Orrun":      ("bm_daniel*0.7+bm_george*0.3", -4, 0.86, 1),
    "Aurveth":    ("bf_alice*0.7+bf_emma*0.3", -2.5, 0.90, 0),
    "Kharrak":    ("bm_lewis", -2.5, 1.02, 1),
    "Lisska":     ("bf_lily", 1, 1.08, 0),
    # Calder's people
    "Wren":       ("bf_lily", 4, 1.02, 0),
    "Ada":        ("bf_alice", -1.5, 0.96, 0),
    "Bel":        ("bf_isabella*0.5+bf_lily*0.5", 0.5, 1.04, 0),
    "Joss":       ("bm_fable", 0, 1.00, 0),
    "Hob":        ("bm_lewis*0.5+bm_george*0.5", -1, 1.03, 0),
    "Fisk":       ("bm_daniel", -1.5, 0.92, 0),
    "Wat Garrow": ("bm_fable*0.5+bm_george*0.5", -0.5, 1.00, 0),
    # Greyhold
    "Hale":       ("bm_daniel", -0.5, 0.95, 0),
    "Pell":       ("bm_lewis", -1, 0.95, 0),
    "Rowan":      ("bf_alice*0.5+bf_isabella*0.5", 0, 1.00, 0),
    "Thorne":     ("bf_isabella*0.7+bf_alice*0.3", -0.5, 1.00, 0),
    "Haverly":    ("bm_fable", 1, 1.03, 0),
    "Tobin":      ("bm_fable*0.5+bm_lewis*0.5", 1.5, 1.06, 0),
    "Grieve":     ("bm_george", -1.5, 0.97, 0),
    "Ottery":     ("bm_daniel*0.5+bm_george*0.5", -0.5, 0.97, 0),
    "Liss":       ("bf_alice*0.7+bf_lily*0.3", -1, 0.98, 0),
    "Tam":        ("bm_lewis", 1.5, 1.05, 0),
    # the Clan
    "Teo":        ("bm_fable", 2, 1.04, 0),
    "Arn":        ("bm_george*0.5+bm_fable*0.5", 0.5, 1.00, 0),
    "Ulric":      ("bm_george", -2, 0.98, 1),
    "Hallam":     ("bm_daniel", -2, 0.92, 0),
    "Sigrun":     ("bf_alice", -2.5, 0.92, 0),
    "Imra":       ("bf_isabella", -0.5, 1.02, 0),
    # the Restoration and others
    "Rook":       ("bm_lewis*0.6+bm_daniel*0.4", -0.5, 0.98, 0),
    "Corvin":     ("bm_daniel*0.6+bm_fable*0.4", 0, 0.94, 0),
    "Cassian":    ("bm_george*0.6+bm_lewis*0.4", 0.5, 1.00, 0),
    "the Captain": ("bf_isabella*0.6+bf_alice*0.4", -1, 1.00, 0),
    "Coll Brask": ("bm_lewis", -1, 1.00, 0),
    "Gannet":     ("bm_fable", -0.5, 1.03, 0),
    # shared voices for everyone without a role of their own
    "Man 1":      ("bm_george*0.5+bm_daniel*0.5", 0, 1.00, 0),
    "Man 2":      ("bm_lewis*0.5+bm_fable*0.5", 0.5, 1.00, 0),
    "Man 3":      ("bm_fable*0.5+bm_daniel*0.5", -1, 1.00, 0),
    "Woman 1":    ("bf_lily*0.5+bf_alice*0.5", 0, 1.00, 0),
    "Woman 2":    ("bf_isabella*0.5+bf_lily*0.5", -0.5, 1.00, 0),
    "Child":      ("bf_lily", 4.5, 1.03, 0),
}

# mood (from the scripts' directions): (speed, gain dB)
MOOD = {
    "tension": (0.97, 0), "dread": (0.93, -1), "grief": (0.90, -1.5), "quiet": (0.94, -2),
    "reflective": (0.95, -0.5), "tender": (0.94, -1.5), "humour": (1.02, 0), "anger": (1.03, 1.5),
    "awe": (0.92, -0.5), "urgent": (1.07, 1), "action": (1.05, 0.5),
}

# words in a line's "how" note: (speed, gain dB), applied in order, each at most once
HOW = [
    ("whisper", 0.95, -6), ("very quiet", 0.94, -5), ("very soft", 0.94, -5), ("very low", 0.92, -4),
    ("very small", 0.95, -5), ("quiet", 0.96, -3), ("soft", 0.97, -2.5), ("low", 0.96, -2), ("faint", 0.95, -5),
    ("weak", 0.92, -4), ("gently", 0.96, -2), ("shout", 1.04, 3), ("roar", 1.0, 4), ("loud", 1.02, 2.5),
    ("slow", 0.88, 0), ("halting", 0.88, 0), ("eager", 1.08, 0.5), ("tumbling", 1.08, 0), ("urgent", 1.06, 0.5),
    ("cracking", 0.93, -1), ("shaking", 0.94, -1), ("hoarse", 0.96, -1), ("rasp", 0.95, -1), ("steady", 0.97, 0),
    ("calm", 0.96, -0.5), ("singing", 0.90, -1),
]


def voice_for(role):
    return CAST.get(role) or CAST["Narrator"]


def shaping(mood, how):
    speed, gain = MOOD.get(mood or "", (1.0, 0.0))
    how = (how or "").lower()
    for word, s, g in HOW:
        if word in how:
            speed *= s; gain += g
            how = how.replace(word, "")
    return speed, gain
