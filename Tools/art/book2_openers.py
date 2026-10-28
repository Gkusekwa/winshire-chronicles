"""Winshire Chronicles, Book 2 (The Hunt Beneath): abstract chapter-opener art, 88 chapters.
Same hand as Book 1 (winshire_art.Canvas): black ink brushwork on white, 1500 x 1000.

POV signs (the same everywhere in the book):
  S  Maren   - a single small ring (c.ring), as in Book 1.
  F  Calder  - the three-dot triad (c.triad), as in Book 1.
  R  Idony   - a small tide-glass: two arcs meeting at a waist between a top and a bottom cap
               (tideglass() below). Never drawn for anything else.

Usage: python3 book2_openers.py OUTDIR      (writes chapter_01.svg .. chapter_88.svg)
"""
import math, os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import winshire_art as A
from winshire_art import Canvas, GROUND
from chapter_openers import door, boat, tracks, flames

BOOK = 2

# (n, pov, title) from Book 2/Chapter_Plan.md (revision 5); POVs checked against the drafted chapters.
CHAPTERS = [
    (1, "S", "The Reeds"), (2, "F", "The Ferry House"), (3, "R", "The Glasses"), (4, "S", "The Black Book"),
    (5, "F", "The Herald"), (6, "S", "Sour Water"), (7, "F", "The Drover's Way"), (8, "R", "Second Ring"),
    (9, "S", "The Titan's Road"), (10, "F", "Arn's Yard"), (11, "S", "The Scarfell's Edge"), (12, "F", "The Empty Chair"),
    (13, "S", "The Thornwood"), (14, "F", "Cotter's Cross"), (15, "S", "The Hallow Plains"), (16, "R", "Sleepwood"),
    (17, "F", "The Ledger"), (18, "S", "The Hollow Ring"), (19, "F", "Skarrow"), (20, "S", "Midsummer Night"),
    (21, "F", "The Roosts"), (22, "R", "The Surge"), (23, "S", "Under the Stones"), (24, "F", "The Black Tarn"),
    (25, "S", "The Moot"), (26, "F", "Westward"), (27, "R", "The Drain"), (28, "S", "The Tusker Road"),
    (29, "R", "Home Water"), (30, "F", "Wendmouth"), (31, "R", "The Oldest Roll"), (32, "S", "Door-Keeper"),
    (33, "F", "The Iron Fells"), (34, "S", "What the Bird Remembers"), (35, "F", "Starwatch"), (36, "R", "The Great Binding"),
    (37, "S", "Glasswater"), (38, "F", "The Library Hill"), (39, "R", "The Long Library"), (40, "S", "Cinders"),
    (41, "F", "The Milestones"), (42, "S", "The Iron Road"), (43, "F", "The Flood"), (44, "R", "Heartstones"),
    (45, "S", "The Scald"), (46, "F", "The Crown's Square"), (47, "R", "The Chain-Ends"), (48, "S", "Chilled Water"),
    (49, "F", "Corsa"), (50, "R", "Envoys"), (51, "S", "Midwinter"), (52, "F", "Wren's Letter"),
    (53, "S", "The Basin Floor"), (54, "F", "The Song"), (55, "S", "The Sun Road"), (56, "F", "Blackwater"),
    (57, "S", "The Unicorn"), (58, "R", "The Grace"), (59, "F", "The Coast"), (60, "S", "The Sun Stair"),
    (61, "R", "The Collar"), (62, "F", "The Young Ones"), (63, "S", "Solenne"), (64, "F", "The Reef"),
    (65, "S", "The Map"), (66, "F", "Two Roads"), (67, "S", "Hallowmere"), (68, "F", "The Tide Council"),
    (69, "S", "Greyhold"), (70, "F", "Gullhaven"), (71, "R", "The Ship"), (72, "S", "The Marches"),
    (73, "F", "The Bell"), (74, "S", "One Hour of Light"), (75, "F", "Marked Roofs"), (76, "R", "The Eddy"),
    (77, "S", "The Old Stair"), (78, "F", "Ashes on the Saltings"), (79, "S", "The Last Crossing"), (80, "F", "The Trap"),
    (81, "S", "Below the Chains"), (82, "F", "Fire Underground"), (83, "R", "The Cellars"), (84, "S", "The Held Breath"),
    (85, "F", "Up Through the Rock"), (86, "S", "The Hill"), (87, "R", "The Last Chart"), (88, "F", "The Account"),
]


# ------------------------------------------------------------------ helpers (all built from brush/line/arc/disc/dot)

def tideglass(c, x, y, s=1.0, w=4):
    """Idony's sign: a tide-glass, two arcs meeting at a waist between two caps."""
    hw, hh = 17 * s, 28 * s
    c.line(x - hw - 3 * s, y - hh, x + hw + 3 * s, y - hh, w, taper=0.2)
    c.line(x - hw - 3 * s, y + hh, x + hw + 3 * s, y + hh, w, taper=0.2)
    for k in (-1, 1):
        c.brush([(x + k * hw, y - hh), (x + k * hw * 0.55, y - hh * 0.45), (x + k * 2.5 * s, y),
                 (x + k * hw * 0.55, y + hh * 0.45), (x + k * hw, y + hh)], w * 0.8, taper=0.1, wobble=0.6)


def sign(c, pov, x, y, s=1.0):
    if pov == "S":
        c.ring(x, y, 26 * s, 5)
    elif pov == "F":
        c.triad(x, y, r=9 * s, spread=24 * s)
    else:
        tideglass(c, x, y, s)


def sea(c, y0=480, y1=960, n=16, opacity=0.8, amp=6):
    for i in range(n):
        yy = y0 + (y1 - y0) * i / max(n - 1, 1)
        c.wave(c.rng.uniform(20, 140), c.rng.uniform(1360, 1480), yy, amp, 0.008 + 0.003 * c.rng.random(),
               c.rng.uniform(0, 6), c.rng.uniform(1.8, 3.4), taper=0.9, opacity=opacity)


def house(c, x, base, wd=90, ht=70, roof=45, w=6):
    r = wd / 2
    c.brush([(x - r, base), (x - r, base - ht), (x, base - ht - roof), (x + r, base - ht), (x + r, base)], w, taper=0.05)


def smoke(c, x, y, h=260, drift=60, n=3, w=3, opacity=0.6):
    for i in range(n):
        dx = (i - (n - 1) / 2) * 10
        c.brush([(x + dx, y), (x + dx + drift * 0.3, y - h * 0.4), (x + dx + drift, y - h)], w, taper=0.9, wobble=5, opacity=opacity)


def stones(c, cx, cy, rx, ry, n=13, h=60, w=10, skip=(), opacity=1.0):
    """A ring of standing stones seen in low perspective."""
    for i in range(n):
        if i in skip:
            continue
        a = 2 * math.pi * i / n + 0.2
        x, y = cx + rx * math.cos(a), cy + ry * math.sin(a)
        hh = h * (0.75 + 0.25 * (math.sin(a) + 1) / 2)
        c.line(x, y, x + c.rng.normal(0, 3), y - hh, w * (0.8 + 0.2 * math.sin(a)), taper=0.15, opacity=opacity)


def lamp(c, x, base, h=260, lit=True, w=4, op=1.0):
    c.line(x, base, x, base - h, w, taper=0.1, opacity=op)
    if lit:
        c.disc(x, base - h - 16, 14)
        c.rays(x, base - h - 16, 10, 26, 54, 2)
    else:
        c.disc(x, base - h - 16, 12, 0.25)


def mountains(c, x0, x1, base, peaks, w=6, opacity=1.0):
    """peaks: list of (x, height). A single ridge line."""
    pts = [(x0, base)]
    for i, (x, h) in enumerate(peaks):
        pts.append((x, base - h))
        if i < len(peaks) - 1:
            nx = peaks[i + 1][0]
            pts.append(((x + nx) / 2, base - min(h, peaks[i + 1][1]) * 0.45))
    pts.append((x1, base))
    c.brush(pts, w, taper=0.5, wobble=1, opacity=opacity)


def wing(c, x, y, span=420, lift=0.4, w=18, k=1):
    """A single wing, drawn from the shoulder (x, y); k=1 to the right, -1 to the left."""
    c.brush([(x, y), (x + k * span * 0.45, y - span * lift), (x + k * span, y - span * lift * 0.6)], w, taper=0.8)
    for i in range(4):
        t = 0.35 + 0.17 * i
        sx, sy = x + k * span * t, y - span * lift * (1.2 - t * 0.6)
        c.line(sx, sy, sx - k * 20, sy + 70 + 25 * i, 3, taper=0.8, opacity=0.7)


def stair(c, x, y, steps, dx, dy, w=6):
    pts = [(x, y)]
    for _ in range(steps):
        x += dx
        pts.append((x, y))
        y += dy
        pts.append((x, y))
    c.brush(pts, w, taper=0.1)
    return x, y


def tusker(c, x, base, s=1.0):
    c.arc(x, base, 90 * s, math.pi * 1.05, math.pi * 1.95, 12 * s, taper=0.3)
    c.arc(x - 92 * s, base - 30 * s, 34 * s, math.pi * 0.2, math.pi * 1.0, 5 * s, taper=0.7)
    c.line(x - 60 * s, base, x - 60 * s, base + 4, 8 * s, taper=0.1)


def page(c, x0, y0, x1, y1, w=6):
    c.brush([(x0, y0), (x1, y0 + 4), (x1 - 4, y1), (x0 + 3, y1 - 2), (x0, y0)], w, taper=0)


def egg(c, x, y, s=1.0, w=6):
    a = np.linspace(0, 2 * math.pi, 60)
    c.brush(np.c_[x + 50 * s * np.cos(a), y + 68 * s * np.sin(a) - 8 * s * np.cos(a) ** 2], w, taper=0.0, wobble=0.6)


# ------------------------------------------------------------------ compositions
COMPS = {}
def comp(n):
    def deco(f):
        COMPS[n] = f
        return f
    return deco


@comp(1)   # The Reeds: two held lines and nobody moving
def _(c):
    c.ground(y=700)
    for i in range(40):
        x = 110 + i * 11 + c.rng.normal(0, 2)
        c.line(x, 700, x + c.rng.normal(0, 2), 520 + (i % 3) * 14, 3, taper=0.3)
    for _ in range(90):
        x = c.rng.uniform(980, 1400)
        h = c.rng.uniform(120, 300)
        c.brush([(x, 700), (x + c.rng.normal(0, 8), 700 - h * 0.6), (x + c.rng.normal(0, 30), 700 - h)], c.rng.uniform(2, 5), taper=0.8)
    c.wave(560, 900, 700, 3, 0.03, 0, 2, taper=0.9, opacity=0.4)
    sign(c, "S", 1180, 330)


@comp(2)   # The Ferry House: the wing that won't lift
def _(c):
    c.river(y=830, band=110, n=6, opacity=0.7)
    c.ground(y=700, x0=200, x1=1300)
    c.brush([(560, 690), (720, 520), (830, 610), (1080, 470)], 20, taper=0.6)
    c.brush([(830, 610), (900, 660)], 6, taper=0.7)
    for i in range(4):
        c.line(700 + i * 90, 560 - i * 20, 690 + i * 90, 640 - i * 10, 3, taper=0.8, opacity=0.6)
    c.disc(560, 690, 26)
    sign(c, "F", 1250, 210)


@comp(3)   # The Glasses: every glass climbing off its scale
def _(c):
    c.ground(y=760, w=4)
    for i, x in enumerate(np.linspace(300, 1200, 10)):
        c.line(x - 16, 760, x - 16, 380, 3.5, taper=0.05)
        c.line(x + 16, 760, x + 16, 380, 3.5, taper=0.05)
        lvl = 640 - i * 20 - c.rng.uniform(0, 60)
        c.line(x - 14, lvl, x + 14, lvl, 6, taper=0.3)
    for _ in range(70):
        c.dot(c.rng.uniform(260, 1240), c.rng.uniform(200, 360), c.rng.uniform(1.2, 3.5), 0.7)
    sign(c, "R", 160, 180)


@comp(4)   # The Black Book: the lock's sentence, lit, in rings
def _(c):
    cx, cy = 750, 470
    for k, r in enumerate((70, 130, 190, 250)):
        n = int(2 * math.pi * r / 34)
        for i in range(n):
            a = 2 * math.pi * i / n + k * 0.3
            ln = c.rng.uniform(0.25, 0.7) * 34 / r
            c.arc(cx, cy, r, a, a + ln, 4, taper=0.3, opacity=0.9)
    c.disc(cx, cy, 22)
    sign(c, "S", 1230, 820)


@comp(5)   # The Herald: two roads from one landing
def _(c):
    c.river(y=880, band=90, n=5, opacity=0.6)
    c.line(700, 790, 800, 790, 8, taper=0.1)
    for i in range(9):
        t = (i + 1) / 10
        c.dot(750 - t * 520, 760 - t * 520 + 10 * (i % 2), 5)
        c.dot(750 + t * 560, 760 - t * 380 + 10 * (i % 2), 5, 0.7)
    sign(c, "F", 1330, 320)


@comp(6)   # Sour Water: the split in the inner wall
def _(c):
    xs = (330, 1170)
    for j, y in enumerate(range(200, 840, 64)):
        off = 30 * (j % 2)
        x = xs[0] + off
        while x < xs[1]:
            gap = abs(x - 760 - 10 * math.sin(y / 70)) < 50
            if not gap:
                c.line(x, y, x + 84, y + c.rng.normal(0, 1.5), 3, taper=0.4, opacity=0.6)
            x += 120
    c.brush([(740, 180), (770, 330), (745, 480), (780, 640), (755, 860)], 12, taper=0.3)
    sign(c, "S", 790, 560, 0.8)


@comp(7)   # The Drover's Way: the copper on the bare shrine-ledge
def _(c):
    c.brush([(80, 760), (750, 700), (1420, 760)], 5, taper=0.7)
    c.brush([(760, 980), (750, 700), (745, 520)], 5, taper=0.7)
    c.brush([(870, 700), (870, 470), (900, 440), (960, 440), (990, 470), (990, 700)], 9, taper=0.05)
    c.line(860, 560, 1000, 560, 7, taper=0.1)
    c.disc(930, 545, 9)
    sign(c, "F", 300, 300)


@comp(8)   # Second Ring: the ferry on still water, a tin serpent at the prow
def _(c):
    for i in range(7):
        c.line(80, 600 + i * 40, 1420, 600 + i * 40 + c.rng.normal(0, 2), 2, taper=0.95, opacity=0.45)
    c.brush([(420, 560), (520, 600), (980, 600), (1080, 560)], 9, taper=0.1)
    c.line(520, 600, 980, 600, 4, taper=0.2)
    t = np.linspace(0, 2.6 * math.pi, 60)
    c.brush(np.c_[1080 + 4 * t * np.cos(t), 520 + 4 * t * np.sin(t)], 3, taper=0.6)
    c.figure(700, 594, 120, 8)
    sign(c, "R", 1250, 200)


@comp(9)   # The Titan's Road: a league-wide swath of laid-down wood
def _(c):
    c.ground(y=760, w=4)
    for x in np.arange(110, 1400, 26):
        jx = x + c.rng.normal(0, 4)
        if 480 < jx < 1000:
            c.line(jx, 752, jx + 120, 720 + c.rng.normal(0, 8), 4, taper=0.6)
        else:
            h = c.rng.uniform(170, 260)
            c.line(jx, 760, jx + c.rng.normal(0, 4), 760 - h, 4, taper=0.5)
    sign(c, "S", 740, 300)


@comp(10)  # Arn's Yard: the bone knitting under the setting-song
def _(c):
    c.line(240, 520, 690, 470, 16, taper=0.4)
    c.line(800, 470, 1260, 420, 16, taper=0.4)
    for i in range(7):
        x = 680 + i * 20
        c.line(x, 440, x + 12, 510, 3, taper=0.5)
    for k in range(4):
        c.arc(745, 700, 260 + k * 40, math.pi * 1.25, math.pi * 1.75, 2.5, taper=0.7, opacity=0.5)
    sign(c, "F", 1270, 820)


@comp(11)  # The Scarfell's Edge: the smoke three leagues off, not gone to
def _(c):
    c.brush([(80, 560), (500, 545), (760, 560), (900, 640), (960, 900)], 7, taper=0.4)
    c.ground(y=430, x0=1100, x1=1460, w=3)
    smoke(c, 1300, 428, 180, 30, 2, 2, 0.5)
    c.disc(380, 530, 7)
    sign(c, "S", 220, 470)
    for i in range(5):
        c.dot(260 - i * 30, 520 - i * 4, 3, 0.6)


@comp(12)  # The Empty Chair: a high-backed chair, empty, alone on the ground
def _(c):
    c.ground(y=760)
    c.line(690, 760, 690, 300, 10, taper=0.05)
    c.line(690, 560, 840, 560, 10, taper=0.05)
    c.line(840, 560, 840, 760, 9, taper=0.05)
    c.line(690, 300, 720, 300, 8, taper=0.2)
    sign(c, "F", 1240, 230)


@comp(13)  # The Thornwood: the graves of the old lions
def _(c):
    c.ground(y=740)
    for i, x in enumerate((360, 620, 900, 1150)):
        c.arc(x, 742, 90 - 10 * (i % 2), math.pi * 1.05, math.pi * 1.95, 7, taper=0.3)
    for _ in range(70):
        x, y = c.rng.uniform(120, 1380), c.rng.uniform(140, 420)
        a = c.rng.uniform(0, math.pi)
        ln = c.rng.uniform(30, 90)
        c.line(x, y, x + ln * math.cos(a), y + ln * math.sin(a), 2.5, taper=0.7, opacity=0.7)
    sign(c, "S", 760, 600)


@comp(14)  # Cotter's Cross: the muster at the crossroads
def _(c):
    c.brush([(100, 900), (750, 600), (1400, 300)], 6, taper=0.6)
    c.brush([(100, 300), (750, 600), (1400, 900)], 6, taper=0.6)
    for _ in range(140):
        x = c.rng.normal(1000, 110)
        y = 470 + c.rng.normal(0, 40) + (x - 1000) * -0.15
        c.line(x, y, x + 6, y - c.rng.uniform(70, 120), 2.5, taper=0.5, opacity=0.85)
    sign(c, "F", 300, 660)


@comp(15)  # The Hallow Plains: the Keepers burning their own groves
def _(c):
    c.ground(y=700, x0=60, x1=1440)
    for gx in (300, 760, 1200):
        for _ in range(9):
            x = gx + c.rng.normal(0, 40)
            c.brush([(x, 700), (x + c.rng.normal(0, 4), 590)], 4, taper=0.4)
        flames(c, gx - 60, gx + 60, 600, 8, 50, 140)
        smoke(c, gx, 470, 300, 200, 3, 2.5, 0.45)
    sign(c, "S", 760, 860)


@comp(16)  # Sleepwood: the stir; the stone ring full, the wood round it dead
def _(c):
    stones(c, 750, 600, 300, 90, n=15, h=110, w=14)
    for _ in range(46):
        x = c.rng.uniform(80, 1420)
        if abs(x - 750) < 380:
            continue
        y = c.rng.uniform(640, 820)
        c.line(x, y, x + c.rng.normal(0, 5), y - c.rng.uniform(150, 300), 3, taper=0.5, opacity=0.3)
    sign(c, "R", 750, 230)


@comp(17)  # The Ledger: one name against one payment
def _(c):
    page(c, 260, 220, 740, 780)
    page(c, 760, 220, 1240, 780)
    c.glyphs(310, 290, 690, rows=12, gap=38, w=3)
    c.glyphs(810, 290, 1190, rows=12, gap=38, w=3, mark=(7, 1))
    sign(c, "F", 1340, 860)


@comp(18)  # The Hollow Ring: ten paces, and a knot that pulls
def _(c):
    c.ground(y=720)
    c.disc(1040, 860, 300, 0.92)
    stones(c, 1040, 720, 260, 40, n=11, h=70, w=10)
    sign(c, "S", 330, 690)
    xs = np.linspace(360, 760, 40)
    c.brush(np.c_[xs, 690 - 10 * np.sin(xs / 25)], 2.5, taper=0.6, wobble=2)


@comp(19)  # Skarrow: two burned steadings, one set of boots between
def _(c):
    c.ground(y=740)
    house(c, 260, 740, 120, 80, 60)
    house(c, 1240, 740, 120, 80, 60)
    smoke(c, 260, 600, 300, 90)
    smoke(c, 1240, 600, 300, -90)
    for i in range(10):
        x = 380 + i * 76
        c.disc(x, 790 + 16 * (i % 2), 7)
        c.disc(x + 14, 790 + 16 * (i % 2), 5)
    sign(c, "F", 750, 220)


@comp(20)  # Midsummer Night: the great chain staked across the ring
def _(c):
    c.ground(y=760)
    pts = []
    for i, x in enumerate(np.linspace(150, 1350, 7)):
        c.line(x, 770, x + 30, 680, 10, taper=0.2)
        pts.append((x + 30, 690))
        if i < 6:
            pts.append((x + 100, 610))
    c.chain(pts, 34, 4)
    c.river(y=880, band=60, n=4, x0=700, x1=1440, opacity=0.6)
    sign(c, "S", 1260, 240)


@comp(21)  # The Roosts: smoke on the wind across the ledges
def _(c):
    for (x0, y, ln) in ((160, 300, 300), (420, 420, 380), (200, 560, 260), (560, 650, 420), (260, 780, 330)):
        c.brush([(x0, y), (x0 + ln, y + 4), (x0 + ln + 20, y + 40)], 8, taper=0.1)
        c.line(x0, y, x0 - 10, y + 50, 4, taper=0.6)
    for i in range(14):
        c.wave(600, 1440, 200 + i * 40, 16, 0.009, i * 0.7, 2.5, taper=0.9, opacity=0.4)
    sign(c, "F", 1250, 860)


@comp(22)  # The Surge: the reading going off the scale
def _(c):
    c.line(220, 140, 220, 860, 4, taper=0.1)
    for i in range(12):
        y = 860 - i * 60
        c.line(205, y, 240, y, 3, taper=0.3, opacity=0.7)
    xs = np.linspace(240, 1320, 80)
    ys = 800 - 18 * np.sin(xs / 60) - np.exp((xs - 240) / 170) * 1.0
    ys = np.maximum(ys, 120)
    c.brush(np.c_[xs, ys], 6, taper=0.4)
    sign(c, "R", 1300, 820)


@comp(23)  # Under the Stones: a stair down to a plinth with an empty hollow
def _(c):
    x, y = stair(c, 200, 180, 8, 60, 60)
    c.brush([(x, y), (1240, y)], 6, taper=0.4)
    c.line(900, y, 900, y - 140, 8, taper=0.05)
    c.line(1080, y, 1080, y - 140, 8, taper=0.05)
    c.line(880, y - 140, 1100, y - 140, 8, taper=0.1)
    c.arc(990, y - 140, 50, 0.05, math.pi - 0.05, 6, taper=0.2)
    sign(c, "S", 200, 120, 0.8)


@comp(24)  # The Black Tarn: two hands pouring together
def _(c):
    c.disc(750, 820, 200, 0.92)
    c.figure(470, 760, 230, 14, 0.06)
    c.figure(1030, 760, 230, 14, -0.06)
    c.brush([(500, 620), (650, 560), (740, 560)], 8, taper=0.4)
    c.brush([(1000, 620), (850, 560), (760, 560)], 8, taper=0.4)
    c.brush([(750, 570), (752, 640), (750, 690)], 2.5, taper=0.5)
    sign(c, "F", 750, 200)


@comp(25)  # The Moot: tent-lanes on the lake, and the beasts all running one way
def _(c):
    c.river(y=840, band=140, n=7, opacity=0.6)
    for row, y in enumerate((520, 680)):
        for i in range(7):
            x = 300 + i * 150 + row * 60
            c.brush([(x - 36, y), (x, y - 60), (x + 36, y)], 5, taper=0.1)
    for _ in range(220):
        y = c.rng.choice([600, 760]) + c.rng.normal(0, 18)
        x = c.rng.uniform(80, 1420)
        c.line(x, y, x - c.rng.uniform(10, 26), y, c.rng.uniform(2, 4), taper=0.6, opacity=0.8)
    sign(c, "S", 1270, 220)


@comp(26)  # Westward: the herd turning off the field after its lead
def _(c):
    c.ground(y=760)
    t = np.linspace(0, 1, 220)
    for k in range(220):
        u = c.rng.random()
        x = 1400 - u * 900
        y = 600 + 60 * math.sin(u * 2) + c.rng.normal(0, 26) * (1 - u * 0.6)
        c.dot(x, y, c.rng.uniform(2, 5), 0.8)
    c.brush([(500, 640), (420, 560), (360, 430)], 7, taper=0.6)
    c.arc(380, 400, 40, math.pi * 0.9, math.pi * 1.9, 5, taper=0.5)
    sign(c, "F", 1250, 220)


@comp(27)  # The Drain: a grassland thinning to nothing
def _(c):
    c.ground(y=700)
    for x in np.arange(120, 1400, 12):
        p = (x - 120) / 1280
        if c.rng.random() > p:
            continue
        h = 40 + 120 * p
        c.line(x, 700, x + c.rng.normal(0, 8), 700 - h * c.rng.uniform(0.6, 1), 2.5, taper=0.6, opacity=0.8)
    sign(c, "R", 300, 400)


@comp(28)  # The Tusker Road: under the High Crown with the herd
def _(c):
    mountains(c, 60, 1440, 420, [(250, 160), (480, 260), (760, 200), (1020, 300), (1260, 170)], 5, 0.7)
    c.ground(y=780)
    for i, x in enumerate((420, 640, 860, 1080)):
        tusker(c, x, 780, 1.0 - 0.1 * (i % 2))
    sign(c, "S", 1260, 700)


@comp(29)  # Home Water: the hill lit white over a dimming lower city
def _(c):
    c.arc(750, 760, 340, math.pi * 1.08, math.pi * 1.92, 9, taper=0.3)
    c.rays(750, 760, 24, 380, 620, 2.5, math.pi * 1.1, math.pi * 1.9)
    for x in np.linspace(140, 1360, 14):
        if abs(x - 750) < 330:
            continue
        lamp(c, x, 780, 70, lit=False, w=3, op=0.6)
    c.river(y=880, band=70, n=5, opacity=0.5)
    sign(c, "R", 160, 160)


@comp(30)  # Wendmouth: the new silver with the ring of six on the rim
def _(c):
    cx, cy = 680, 480
    c.ring(cx, cy, 190, 10, gap=0.0001)
    for i in range(6):
        a = i * math.pi / 3 - math.pi / 2
        c.disc(cx + 150 * math.cos(a), cy + 150 * math.sin(a), 13)
    for i in range(7):
        c.line(1050, 820 - i * 22, 1230, 816 - i * 22, 9, taper=0.1)
    sign(c, "F", 1140, 240)


@comp(31)  # The Oldest Roll: a roll opened, its chain-words kept
def _(c):
    for x in (240, 1260):
        t = np.linspace(0, 3 * math.pi, 80)
        c.brush(np.c_[x + 3 * t * np.cos(t), 330 + 3 * t * np.sin(t)], 3, taper=0.4)
        c.line(x, 300, x, 700, 8, taper=0.05)
    c.line(250, 300, 1250, 300, 5, taper=0.2)
    c.line(250, 700, 1250, 700, 5, taper=0.2)
    c.glyphs(330, 370, 1170, rows=8, gap=40, w=3, mark=(5, 4))
    sign(c, "R", 750, 860)


@comp(32)  # Door-Keeper: an old door, and the one who keeps it at its threshold
def _(c):
    c.ground(y=760)
    door(c, 900, 760, 260, 520, 11)
    sign(c, "S", 900, 720, 1.1)
    c.brush([(1180, 300), (1200, 290), (1220, 300)], 4, taper=0.5)


@comp(33)  # The Iron Fells: a fire in a pass
def _(c):
    c.brush([(60, 120), (420, 420), (700, 780)], 8, taper=0.4)
    c.brush([(1440, 160), (1060, 460), (800, 780)], 8, taper=0.4)
    c.line(700, 780, 800, 780, 6, taper=0.4)
    c.embers(750, 760, 40, 50, 80, 4)
    c.disc(750, 768, 8)
    for _ in range(80):
        c.dot(c.rng.uniform(80, 1420), c.rng.uniform(60, 980), 1.6, 0.35)
    sign(c, "F", 750, 200)


@comp(34)  # What the Bird Remembers: three hundred years back, fire, and a great cat driven off
def _(c):
    c.ground(y=760)
    flames(c, 1000, 1250, 760, 22, 160, 460)
    c.brush([(880, 740), (700, 726), (480, 740)], 30, taper=0.6, opacity=0.9)
    c.disc(880, 716, 30, 0.9)
    for i in range(16):
        c.dot(160 + i * 50, 300 + i * 6, 4 - i * 0.15, 0.7)
    sign(c, "S", 260, 560)


@comp(35)  # Starwatch: the steps, and one star with three
def _(c):
    stair(c, 140, 900, 12, 52, -44, 5)
    for _ in range(140):
        c.dot(c.rng.uniform(300, 1440), c.rng.uniform(40, 420), c.rng.uniform(1.2, 3.2), 0.6)
    c.disc(1100, 230, 10)
    sign(c, "F", 1100, 230, 1.6)


@comp(36)  # The Great Binding: a hundred voices on the hill, and one place empty
def _(c):
    c.arc(750, 1100, 620, math.pi * 1.15, math.pi * 1.85, 8, taper=0.3)
    for i in range(46):
        a = math.pi * (1.2 + 0.6 * i / 45)
        if i == 30:
            continue
        x, y = 750 + 620 * math.cos(a), 1100 + 620 * math.sin(a) - 4
        c.figure(x, y, 46, 4)
        c.line(x, y - 56, 750, 180, 1.4, taper=0.9, opacity=0.35)
    c.disc(750, 180, 12)
    sign(c, "R", 1300, 860)


@comp(37)  # Glasswater: a wall against the flood, the crack held by a cut rune
def _(c):
    sea(c, 160, 900, 18, 0.55, 14)
    c.brush([(820, 120), (980, 120), (990, 940), (810, 940), (820, 120)], 12, taper=0)
    c.brush([(880, 420), (910, 500), (870, 560), (920, 640)], 5, taper=0.3)
    c.line(860, 520, 940, 520, 5, taper=0.3)
    c.line(900, 470, 900, 580, 5, taper=0.3)
    sign(c, "S", 1220, 520)


@comp(38)  # The Library Hill: the long house on the hill, the great window
def _(c):
    c.arc(750, 1240, 760, math.pi * 1.2, math.pi * 1.8, 8, taper=0.4)
    for x in np.linspace(470, 1030, 8):
        c.arch(x, 520, 46, 120, 5)
    c.line(420, 400, 1080, 400, 8, taper=0.1)
    c.ring(750, 300, 70, 8, gap=0.0001)
    for k in range(6):
        a = k * math.pi / 3
        c.line(750, 300, 750 + 68 * math.cos(a), 300 + 68 * math.sin(a), 3, taper=0.2)
    c.embers(980, 340, 50, 300, 160, 4)
    sign(c, "F", 220, 220)


@comp(39)  # The Long Library: the hall, its far window broken
def _(c):
    vx, vy = 750, 470
    for k in (-1, 1):
        for i in range(7):
            x0 = vx + k * (720 - i * 30)
            c.line(x0, 60 + i * 30, vx + k * 60, vy - 40, 2.5, taper=0.6, opacity=0.6)
            c.line(x0, 940 - i * 30, vx + k * 60, vy + 40, 2.5, taper=0.6, opacity=0.6)
    c.brush([(690, 410), (810, 410), (810, 530), (690, 530), (690, 410)], 6, taper=0)
    for _ in range(22):
        x, y = 750 + c.rng.normal(0, 40), 470 + c.rng.normal(0, 40)
        a = c.rng.uniform(0, math.pi)
        c.line(x, y, x + 20 * math.cos(a), y + 20 * math.sin(a), 2.5, taper=0.5)
    sign(c, "R", 1360, 860)


@comp(40)  # Cinders: a pyre on the steps at nightfall
def _(c):
    for i in range(7):
        y = 900 - i * 44
        w2 = 560 - i * 50
        c.line(750 - w2, y, 750 + w2, y, 5, taper=0.4)
    c.brush([(650, 590), (850, 590)], 18, taper=0.2)
    c.embers(750, 560, 160, 300, 260, 5)
    sign(c, "S", 1200, 180)


@comp(41)  # The Milestones: nineteen to the bridge, drawn in frost
def _(c):
    for _ in range(260):
        c.dot(c.rng.uniform(60, 1440), c.rng.uniform(560, 960), c.rng.uniform(1, 2.6), 0.45)
    for i in range(19):
        t = i / 18
        x = 160 + t * 1120
        y = 860 - 300 * math.sin(t * math.pi * 0.9)
        s = 1.3 - t * 0.7
        c.brush([(x - 10 * s, y), (x - 10 * s, y - 36 * s), (x, y - 46 * s), (x + 10 * s, y - 36 * s), (x + 10 * s, y)], 5 * s, taper=0)
    sign(c, "F", 1300, 220)


@comp(42)  # The Iron Road: canals in sleet
def _(c):
    for k in (-1, 1):
        for j in range(2):
            c.brush([(750 + k * (130 + j * 70), 380), (750 + k * (600 + j * 400), 980)], 4, taper=0.2)
    c.line(80, 380, 1420, 380, 3, taper=0.8, opacity=0.6)
    for _ in range(170):
        x, y = c.rng.uniform(80, 1420), c.rng.uniform(60, 360)
        c.line(x, y, x - 14, y + 34, 1.6, taper=0.6, opacity=0.5)
    c.brush([(705, 640), (795, 640), (785, 700), (715, 700), (705, 640)], 6, taper=0)
    sign(c, "S", 750, 560, 0.7)


@comp(43)  # The Flood: one roof and a man on it
def _(c):
    sea(c, 520, 980, 20, 0.75, 9)
    c.brush([(620, 530), (750, 420), (880, 530)], 12, taper=0.1)
    c.figure(750, 420, 90, 7)
    sign(c, "F", 1260, 200)


@comp(44)  # Heartstones: the racks of crystal hearts
def _(c):
    for j in range(4):
        y = 300 + j * 140
        c.line(300, y + 50, 1200, y + 50, 5, taper=0.2)
        for i in range(10):
            x = 350 + i * 90 + (j % 2) * 20
            s = 22 + c.rng.normal(0, 3)
            c.brush([(x, y - s), (x + s * 0.7, y), (x, y + s * 1.2), (x - s * 0.7, y), (x, y - s)], 3, taper=0)
    sign(c, "R", 1340, 180)


@comp(45)  # The Scald: a basin of fused glass, ringed by moths
def _(c):
    c.arc(750, 300, 600, math.pi * 0.28, math.pi * 0.72, 10, taper=0.3)
    for _ in range(26):
        x, y = c.rng.uniform(420, 1080), c.rng.uniform(720, 860)
        a = c.rng.uniform(0, math.pi)
        c.line(x, y, x + 60 * math.cos(a), y + 20 * math.sin(a), 2.5, taper=0.4, opacity=0.6)
    for i in range(24):
        a = 2 * math.pi * i / 24
        x, y = 750 + 460 * math.cos(a), 470 + 170 * math.sin(a)
        c.brush([(x - 9, y - 6), (x, y + 2), (x + 9, y - 6)], 2.5, taper=0.3)
    sign(c, "S", 750, 360)


@comp(46)  # The Crown's Square: dead lamps at the corners, the crowd round the edge
def _(c):
    q = [(260, 820), (520, 420), (980, 420), (1240, 820)]
    c.brush(q + [q[0]], 4, taper=0, opacity=0.8)
    for (x, y) in q:
        lamp(c, x, y, 160, lit=False, w=4)
    for _ in range(240):
        t = c.rng.random()
        side = c.rng.integers(0, 4)
        (x0, y0), (x1, y1) = q[side], q[(side + 1) % 4]
        x, y = x0 + (x1 - x0) * t, y0 + (y1 - y0) * t
        c.dot(x + c.rng.normal(0, 14), y + c.rng.normal(0, 10) + 14, c.rng.uniform(2, 4.5), 0.8)
    sign(c, "F", 750, 620, 1.3)


@comp(47)  # The Chain-Ends: two broken links, their runes still lit
def _(c):
    c.chain([(80, 480), (560, 520)], 70, 8)
    c.chain([(940, 520), (1420, 480)], 70, 8)
    for x in (600, 900):
        c.link(x, 520, 80, 0, 9)
        c.rays(x, 520, 14, 60, 110, 2)
    sign(c, "R", 750, 820)


@comp(48)  # Chilled Water: the cage's canals round the Scald
def _(c):
    for i in range(6):
        c.ring(750, 520, 120 + i * 60, 3.5, gap=0.05, opacity=0.8)
    for i in range(24):
        a = 2 * math.pi * i / 24
        c.line(750 + 470 * math.cos(a), 520 + 470 * math.sin(a), 750 + 500 * math.cos(a), 520 + 500 * math.sin(a), 6, taper=0.1)
    c.disc(750, 520, 90, 0.95)
    sign(c, "S", 1330, 860)


@comp(49)  # Corsa: masts in the harbour and three over it
def _(c):
    c.river(y=820, band=120, n=7, opacity=0.6)
    for i, x in enumerate(np.linspace(180, 1320, 15)):
        h = 260 + 80 * ((i * 7) % 3)
        c.line(x, 760, x, 760 - h, 4, taper=0.1)
        c.line(x - 40, 760 - h * 0.7, x + 40, 760 - h * 0.7, 3, taper=0.3)
    sign(c, "F", 750, 160, 1.3)


@comp(50)  # Envoys: a line of watchers at a caged thing
def _(c):
    c.ground(y=760)
    c.arc(1050, 760, 250, math.pi, 2 * math.pi, 10, taper=0.1)
    for i in range(9):
        a = math.pi * (1 + (i + 0.5) / 9)
        c.line(1050 + 250 * math.cos(a), 760 + 250 * math.sin(a), 1050 + 250 * math.cos(a), 760, 5, taper=0.1)
    for i in range(9):
        c.figure(200 + i * 52, 760, 110 + c.rng.normal(0, 6), 7)
    sign(c, "R", 300, 220)


@comp(51)  # Midwinter: three in a dead town, keeping the watch
def _(c):
    c.ground(y=740)
    for x, h in ((240, 220), (420, 120), (1100, 260), (1280, 140)):
        c.line(x, 740, x + c.rng.normal(0, 3), 740 - h, 18, taper=0.1)
        c.line(x - 18, 740 - h, x + 18, 740 - h + 10, 5, taper=0.3)
    for i, x in enumerate((700, 760, 820)):
        c.figure(x, 740, 130 - 10 * (i == 2), 8)
    for _ in range(120):
        c.dot(c.rng.uniform(80, 1420), c.rng.uniform(60, 700), c.rng.uniform(1, 2.6), 0.5)
    sign(c, "S", 760, 420)


@comp(52)  # Wren's Letter: a child in a cave-mouth, sitting with an empty-eyed one
def _(c):
    c.ground(y=780)
    c.arc(750, 780, 380, math.pi, 2 * math.pi, 26, taper=0.15)
    c.figure(640, 780, 110, 8)
    c.brush([(1000, 778), (900, 720), (820, 700), (780, 730)], 16, taper=0.5)
    c.disc(780, 728, 18)
    sign(c, "F", 1300, 220)


@comp(53)  # The Basin Floor: the shaft down through the glass
def _(c):
    c.ground(y=480, w=4)
    a = np.linspace(0, 2 * math.pi, 80)
    c.brush(np.c_[750 + 200 * np.cos(a), 520 + 50 * np.sin(a)], 8, taper=0)
    c.line(560, 530, 600, 960, 7, taper=0.2)
    c.line(940, 530, 900, 960, 7, taper=0.2)
    for i in range(8):
        y = 600 + i * 46
        c.line(600, y, 900, y, 2, taper=0.9, opacity=0.4)
    for _ in range(10):
        x = c.rng.uniform(700, 800)
        c.brush([(x, 450), (x + c.rng.normal(0, 30), 330), (x + c.rng.normal(0, 50), 200)], 2.5, taper=0.9, wobble=5, opacity=0.5)
    sign(c, "S", 1220, 240)


@comp(54)  # The Song: an army coming apart
def _(c):
    c.ground(y=780)
    for _ in range(260):
        x = c.rng.uniform(150, 1350)
        p = (x - 150) / 1200
        if c.rng.random() < p * 0.85:
            continue
        lean = c.rng.normal(0, 0.05 + 0.9 * p)
        h = c.rng.uniform(90, 150)
        y = 780 + c.rng.normal(0, 10 + 50 * p)
        c.line(x, y, x + h * math.sin(lean), y - h * math.cos(lean), 2.5, taper=0.5)
    sign(c, "F", 1150, 230)


@comp(55)  # The Sun Road: a pilgrim road climbing to a sun
def _(c):
    c.brush([(200, 940), (500, 760), (740, 600), (920, 470), (1080, 360)], 5, taper=0.5)
    for x, y in ((420, 810), (650, 660), (860, 515)):
        c.arch(x, y, 46, 80, 5)
    c.rays(1180, 260, 22, 80, 170, 4)
    sign(c, "S", 300, 940 - 120, 0.9)


@comp(56)  # Blackwater: a stilt town over dark water, smoke
def _(c):
    for i in range(16):
        c.wave(60, 1440, 780 + i * 12, 4, 0.01, i, 5, taper=0.95)
    for x in np.linspace(340, 1160, 7):
        c.line(x - 40, 780, x - 40, 640, 4, taper=0.1)
        c.line(x + 40, 780, x + 40, 640, 4, taper=0.1)
        house(c, x, 640, 100, 70, 40, 5)
    smoke(c, 880, 520, 360, 200, 5, 3, 0.4)
    sign(c, "F", 220, 220)


@comp(57)  # The Unicorn: a horn between the trunks
def _(c):
    for x in np.linspace(120, 1380, 16):
        if 700 < x < 860:
            continue
        c.line(x + c.rng.normal(0, 8), 980, x + c.rng.normal(0, 8), 20, c.rng.uniform(5, 12), taper=0.1, opacity=0.85)
    c.line(700, 640, 860, 300, 11, taper=0.9)
    for i in range(6):
        t = 0.1 + i * 0.13
        x, y = 700 + 160 * t, 640 - 340 * t
        c.line(x - 10, y + 4, x + 10, y - 6, 3, taper=0.5)
    sign(c, "S", 780, 820, 0.9)


@comp(58)  # The Grace: the chosen above stairs, the hands below doing the work
def _(c):
    c.line(140, 480, 1360, 480, 9, taper=0.1)
    for x in (480, 760, 1040):
        c.figure(x, 470, 230, 13)
    for i in range(22):
        x = 180 + i * 54 + c.rng.normal(0, 6)
        c.figure(x, 760, 80, 5, c.rng.normal(0, 0.15))
    c.ground(y=760, x0=140, x1=1360, w=3)
    sign(c, "R", 1300, 200)


@comp(59)  # The Coast: something breathing under the reef
def _(c):
    c.brush([(80, 470), (600, 440), (900, 450), (1440, 480)], 9, taper=0.5)
    for i in range(7):
        c.arc(750, 1250, 300 + i * 70, math.pi * 1.15, math.pi * 1.85, 3, taper=0.6, opacity=0.25 + 0.08 * i)
    c.figure(700, 445, 50, 5)
    sign(c, "F", 820, 380, 0.8)


@comp(60)  # The Sun Stair: a stair cut up a cliff
def _(c):
    c.brush([(980, 980), (1000, 600), (980, 300), (1020, 60)], 14, taper=0.2)
    x, y = 960, 920
    pts = []
    for i in range(9):
        nx = x - 160 if i % 2 == 0 else x + 160
        pts += [(x, y), (nx, y - 80)]
        x, y = nx, y - 80
    c.brush(pts, 5, taper=0.2)
    c.ring(1220, 180, 54, 3, gap=0.0001, opacity=0.6)
    c.rays(1220, 180, 16, 70, 130, 2.5)
    sign(c, "S", 300, 220)


@comp(61)  # The Collar: an open collar written over
def _(c):
    cx, cy = 750, 470
    c.arc(cx, cy, 230, -math.pi * 0.35, math.pi * 1.35, 30, taper=0.15)
    for i in range(14):
        a = -math.pi * 0.3 + i * math.pi * 1.6 / 13
        r0 = 275
        c.line(cx + r0 * math.cos(a), cy + r0 * math.sin(a), cx + (r0 + 22) * math.cos(a), cy + (r0 + 22) * math.sin(a), 3, taper=0.3)
    c.brush([(750 + 230 * math.cos(-math.pi * 0.35), 470 + 230 * math.sin(-math.pi * 0.35)), (900, 330), (960, 230)], 2, taper=0.8, opacity=0.6)
    sign(c, "R", 750, 470, 1.1)


@comp(62)  # The Young Ones: three heads down in the dark of the caves, a child talking
def _(c):
    c.arc(750, 1100, 700, math.pi * 1.1, math.pi * 1.9, 40, taper=0.1)
    c.ground(y=800, x0=160, x1=1340)
    for x in (560, 760, 960):
        c.brush([(x + 90, 790), (x + 30, 740), (x - 20, 760)], 16, taper=0.6)
        c.disc(x - 24, 762, 13)
    c.figure(380, 800, 110, 8)
    sign(c, "F", 1300, 200)


@comp(63)  # Solenne: the boats off the low city, the lighthouse on its isle
def _(c):
    sea(c, 560, 960, 14, 0.6, 6)
    c.brush([(1100, 560), (1180, 520), (1320, 525), (1380, 560)], 8, taper=0.2)
    c.brush([(1225, 525), (1235, 300), (1265, 300), (1275, 525)], 7, taper=0.05)
    c.rays(1250, 280, 8, 30, 90, 2, math.pi * 0.85, math.pi * 1.35)
    for i in range(9):
        x = 160 + i * 100 + c.rng.normal(0, 10)
        y = 640 + (i % 3) * 70
        c.arc(x, y - 50, 70, math.pi * 0.25, math.pi * 0.75, 4, taper=0.3)
    sign(c, "S", 300, 260)


@comp(64)  # The Reef: the salt pans, and a cup poured back
def _(c):
    for j in range(3):
        for i in range(6):
            x, y = 220 + i * 150, 560 + j * 110
            c.brush([(x, y), (x + 130, y), (x + 130, y + 90), (x, y + 90), (x, y)], 3, taper=0, opacity=0.7)
    sea(c, 820, 960, 4, 0.5)
    c.brush([(1180, 470), (1250, 470), (1240, 530), (1190, 530), (1180, 470)], 5, taper=0)
    for i in range(6):
        c.dot(1260 + i * 4, 540 + i * 30, 3, 0.8)
    sign(c, "F", 1250, 220)


@comp(65)  # The Map: six ends from a bridge, and one going down
def _(c):
    cx, cy = 750, 470
    for i in range(6):
        a = i * math.pi / 3 + 0.3
        c.brush([(cx + 30 * math.cos(a), cy + 30 * math.sin(a)), (cx + 330 * math.cos(a), cy + 300 * math.sin(a))], 4, taper=0.6, opacity=0.7)
    c.line(cx, cy + 20, cx, cy + 260, 9, taper=0.8)
    c.disc(cx, cy, 14)
    lamp(c, 1240, 860, 120, lit=True, w=3)
    sign(c, "S", 250, 220)


@comp(66)  # Two Roads: a straight coast road, and one turning west
def _(c):
    c.brush([(80, 760), (750, 740), (1420, 760)], 6, taper=0.6)
    c.brush([(750, 740), (600, 560), (380, 380), (140, 260)], 4, taper=0.7, opacity=0.7)
    sea(c, 820, 960, 4, 0.5)
    c.brush([(300, 300), (330, 280), (360, 300), (390, 280), (420, 300)], 4, taper=0.6)
    sign(c, "F", 900, 660)


@comp(67)  # Hallowmere: a city of dark lamps, one hearth
def _(c):
    c.ground(y=760)
    for i, x in enumerate(np.linspace(180, 1320, 9)):
        house(c, x, 760, 100, 60 + 30 * (i % 3), 50, 5)
    for x in np.linspace(240, 1260, 6):
        lamp(c, x, 860, 140, lit=False, w=3)
    c.embers(750 + 140, 700, 18, 30, 30, 3, rise=False)
    sign(c, "S", 750, 220)


@comp(68)  # The Tide Council: a horseshoe of seats
def _(c):
    for k in range(3):
        r = 260 + k * 110
        n = 9 + k * 4
        for i in range(n):
            a = math.pi * (0.1 + 0.8 * i / (n - 1))
            x, y = 750 + r * math.cos(a) * 1.4, 300 + r * math.sin(a)
            c.line(x - 14, y, x + 14, y, 7, taper=0.1)
    c.disc(750, 380, 10)
    sign(c, "F", 750, 160)


@comp(69)  # Greyhold: anchors driven into the drained wall
def _(c):
    c.brush([(980, 60), (1000, 500), (970, 940)], 60, taper=0.1, opacity=0.95)
    for y in (260, 520, 780):
        c.line(980, y, 640, y + 20, 8, taper=0.1)
        c.chain([(640, y + 20), (200, y + 60)], 30, 4)
    c.brush([(1010, 120), (990, 300), (1015, 470), (995, 620)], 3, taper=0.3)
    sign(c, "S", 1260, 860)


@comp(70)  # Gullhaven: hull-runes smoking in the bay
def _(c):
    c.brush([(80, 600), (500, 560), (880, 600), (1200, 700), (1420, 760)], 9, taper=0.3)
    sea(c, 660, 960, 10, 0.5)
    for i in range(6):
        x = 300 + i * 170
        y = 780 + 40 * (i % 2)
        c.arc(x, y - 50, 70, math.pi * 0.25, math.pi * 0.75, 5, taper=0.3)
        smoke(c, x, y - 10, 140, 40, 2, 2, 0.6)
    sign(c, "F", 1250, 220)


@comp(71)  # The Ship: a hull coasting east
def _(c):
    sea(c, 620, 960, 12, 0.6)
    c.brush([(300, 520), (400, 640), (1100, 640), (1240, 500)], 12, taper=0.1)
    c.line(700, 600, 700, 120, 7, taper=0.1)
    c.line(560, 220, 840, 220, 4, taper=0.2)
    c.line(580, 400, 820, 400, 4, taper=0.2)
    sign(c, "R", 1280, 240)


@comp(72)  # The Marches: a road east over the river, full of people
def _(c):
    c.river(y=820, band=120, n=7, opacity=0.6)
    c.brush([(600, 740), (900, 500), (1200, 300), (1420, 220)], 5, taper=0.6)
    for _ in range(150):
        t = c.rng.random()
        x = 600 + t * 800 + c.rng.normal(0, 10)
        y = 740 - t * 520 + c.rng.normal(0, 10)
        c.dot(x, y - 10, c.rng.uniform(2, 4.5), 0.85)
    sign(c, "S", 260, 300)


@comp(73)  # The Bell: a bell on the reef at low tide
def _(c):
    sea(c, 640, 960, 10, 0.5)
    c.brush([(560, 650), (600, 420), (660, 350), (750, 330), (840, 350), (900, 420), (940, 650)], 12, taper=0.05)
    c.line(520, 650, 980, 650, 8, taper=0.2)
    for x, y in ((220, 260), (1300, 240), (300, 520)):
        c.line(x, y, x + (750 - x) * 0.35, y + (500 - y) * 0.35, 3, taper=0.8)
    sign(c, "F", 1250, 520)


@comp(74)  # One Hour of Light: every dead window lit
def _(c):
    c.ground(y=780)
    for i, x in enumerate(np.linspace(140, 1360, 16)):
        h = 60 + 40 * ((i * 5) % 3)
        c.brush([(x - 34, 780), (x - 34, 780 - h), (x + 34, 780 - h), (x + 34, 780)], 4, taper=0.05)
        c.disc(x, 780 - h * 0.5, 5)
        c.rays(x, 780 - h * 0.5, 8, 10, 26, 1.6)
    sign(c, "S", 750, 220)


@comp(75)  # Marked Roofs: water up to the eaves, a mark on each roof
def _(c):
    sea(c, 640, 980, 16, 0.7, 8)
    for i, x in enumerate(np.linspace(220, 1280, 6)):
        c.brush([(x - 70, 640), (x, 570), (x + 70, 640)], 8, taper=0.1)
        c.line(x - 10, 600, x + 12, 590, 6, taper=0.3)
    sign(c, "F", 750, 220)


@comp(76)  # The Eddy: a burning boat turning on the eddy
def _(c):
    t = np.linspace(0, 5 * math.pi, 400)
    r = 20 + 30 * t
    c.brush(np.c_[750 + r * np.cos(t) * 1.6, 560 + r * np.sin(t) * 0.5], 3, taper=0.9, opacity=0.6)
    boat(c, 760, 600, 140)
    flames(c, 700, 820, 580, 10, 60, 180)
    sign(c, "R", 1300, 200)


@comp(77)  # The Old Stair: graves outside the wall, and a stair under them
def _(c):
    c.ground(y=360)
    for x in (300, 420, 540, 660):
        c.line(x, 360, x, 300, 6, taper=0.1)
        c.line(x - 14, 320, x + 14, 320, 4, taper=0.2)
    stair(c, 660, 400, 9, -40, 60, 6)
    c.line(1180, 360, 1180, 80, 22, taper=0.05)
    sign(c, "S", 1050, 700)


@comp(78)  # Ashes on the Saltings: pyres on the flats
def _(c):
    for i in range(8):
        c.line(80, 700 + i * 30, 1420, 700 + i * 30 + c.rng.normal(0, 2), 2, taper=0.95, opacity=0.4)
    for x in np.linspace(260, 1240, 7):
        c.line(x - 30, 690, x + 30, 690, 10, taper=0.2)
        smoke(c, x, 670, c.rng.uniform(300, 480), 80, 2, 2, 0.55)
    sign(c, "F", 750, 880)


@comp(79)  # The Last Crossing: one ferry on the rope, an anvil left behind
def _(c):
    c.river(y=620, band=260, n=11, opacity=0.6)
    c.line(80, 480, 1420, 470, 2.5, taper=0.1, opacity=0.8)
    c.brush([(620, 560), (900, 560), (880, 600), (640, 600), (620, 560)], 6, taper=0)
    for i in range(6):
        c.figure(660 + i * 40, 558, 60, 5)
    c.brush([(140, 880), (260, 880), (240, 840), (300, 830), (160, 830), (140, 880)], 7, taper=0)
    c.chain([(300, 850), (440, 880)], 24, 3)
    sign(c, "S", 1260, 230)


@comp(80)  # The Trap: chains from the hill across the river
def _(c):
    c.arc(150, 900, 380, math.pi * 1.5, math.pi * 1.95, 9, taper=0.4)
    c.river(y=860, band=100, n=6, x0=520, opacity=0.6)
    for k, (y0, y1) in enumerate(((540, 380), (620, 560), (700, 740))):
        c.chain([(180 + k * 70, y0), (760, (y0 + y1) / 2 + 40), (1380, y1)], 30, 4)
    sign(c, "F", 1250, 200)


@comp(81)  # Below the Chains: the sentence carved again over a shut place
def _(c):
    c.arc(750, 1200, 1000, math.pi * 1.2, math.pi * 1.8, 30, taper=0.2)
    for k, r in enumerate((620, 660, 700)):
        n = 26
        for i in range(n):
            a = math.pi * (1.32 + 0.36 * i / (n - 1))
            c.arc(750, 1200, r, a, a + 0.007, 4, taper=0.3)
    c.line(750, 560, 750, 900, 8, taper=0.2)
    c.river(y=920, band=50, n=3, opacity=0.5)
    sign(c, "S", 330, 760)


@comp(82)  # Fire Underground: flame in a cavern, wings in the dark
def _(c):
    c.brush([(60, 900), (750, 890), (1440, 905)], 46, taper=0.2)
    flames(c, 560, 940, 880, 26, 180, 520)
    wing(c, 300, 420, 280, 0.3, 12, 1)
    wing(c, 1200, 420, 280, 0.3, 12, -1)
    sign(c, "F", 1300, 180)


@comp(83)  # The Cellars: low vaults under heavy rock, people in them
def _(c):
    c.brush([(60, 260), (1440, 240)], 70, taper=0.05, opacity=0.95)
    for x in np.linspace(240, 1260, 6):
        c.arch(x, 820, 170, 300, 7)
        c.figure(x - 20, 820, 70, 5)
        c.figure(x + 24, 820, 60, 5)
    c.ground(y=820)
    sign(c, "R", 750, 910)


@comp(84)  # The Held Breath: one seam in the rock, one small ring before it
def _(c):
    c.brush([(760, 280), (750, 420), (762, 560), (752, 680)], 7, taper=0.3)
    sign(c, "S", 640, 650, 0.8)


@comp(85)  # Up Through the Rock: a fissure climbing out of the dark
def _(c):
    for i in range(30):
        y = 440 + i * 18
        for x0, x1 in ((80, 700 + 20 * math.sin(i)), (800 + 20 * math.cos(i), 1420)):
            c.line(x0 + c.rng.uniform(0, 40), y, x1 - c.rng.uniform(0, 40), y + c.rng.normal(0, 2), c.rng.uniform(3, 7), taper=0.6, opacity=0.85)
    c.ground(y=400, x0=80, x1=1420)
    c.brush([(750, 980), (720, 860), (780, 740), (735, 620), (770, 500), (750, 410)], 4, taper=0.2, opacity=0.6)
    sign(c, "F", 1150, 230)


@comp(86)  # The Hill: one long table, a ring at one end and three at the other
def _(c):
    c.line(220, 560, 1280, 560, 12, taper=0.05)
    for x in (300, 1200):
        c.line(x, 560, x, 760, 7, taper=0.1)
    for x in np.linspace(470, 1030, 7):
        c.figure(x, 540, 90, 6)
    sign(c, "S", 140, 470)
    c.triad(1370, 470, r=8, spread=20)


@comp(87)  # The Last Chart: five readings moving toward one place
def _(c):
    cx, cy = 980, 470
    for i in range(5):
        a = math.pi * (0.55 + 0.9 * i / 4)
        x0, y0 = cx + 760 * math.cos(a), cy + 420 * math.sin(a)
        n = 12
        for j in range(n):
            t = j / n
            c.dot(x0 + (cx - x0) * t, y0 + (cy - y0) * t, 5 - 3 * t, 0.9)
    c.disc(cx, cy, 16)
    sign(c, "R", 1300, 820)


@comp(88)  # The Account: the first line written, barley under it
def _(c):
    page(c, 420, 200, 1080, 640)
    c.line(480, 280, 1000, 284, 7, taper=0.2)
    c.glyphs(480, 340, 1020, rows=6, gap=40, w=2.5)
    c.ground(y=860)
    for x in np.linspace(300, 1200, 7):
        for k in range(-2, 3):
            c.line(x + k * 5, 858, x + k * 12, 760 - abs(k) * 4, 2.5, taper=0.6)
    sign(c, "F", 1240, 200)


def art_for(n):
    cv = Canvas(10000 * BOOK + n)
    COMPS[n](cv)
    return cv.svg()


if __name__ == "__main__":
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    nums = [n for n, _, _ in CHAPTERS]
    assert nums == list(range(1, 89)), "chapter table is not 1..88"
    missing = [n for n in nums if n not in COMPS]
    assert not missing, f"chapters without a composition: {missing}"
    extra = sorted(set(COMPS) - set(nums))
    assert not extra, f"compositions for chapters not in the book: {extra}"
    for n in nums:
        open(os.path.join(out, f"chapter_{n:02d}.svg"), "w").write(art_for(n))
    print("wrote", len(nums))
