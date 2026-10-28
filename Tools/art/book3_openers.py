"""Winshire Chronicles, Book 3: abstract chapter-opener art (86 chapters).
Same brush and vocabulary as Book 1 (winshire_art.py, chapter_openers.py).
Usage: python3 book3_openers.py OUTDIR   -> OUTDIR/chapter_NN.svg for every chapter

POV signs (small, always drawn by sign(); the same everywhere in the book):
  S  Maren Ashdown   the single ring              (as Books 1-2)
  F  Calder Fenn     the three-dot triad          (as Books 1-2)
  R  Idony Vael      the tide-glass: two arcs meeting at a waist, capped top and bottom
  G  Ilse Rowan      the blade: an upright stroke with a short crossguard and a pommel dot
  C  Arn Varr        the pouring cup: a bowl on a short stem ("Who pours?")
  U  Tobin           the hand's block: a small open square (a hand's work, one stone)
  M  Kit Merrin      the sail: a mast, a three-cornered sail and a short hull
"""
import math, os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import winshire_art as A
from winshire_art import Canvas, GROUND

BOOK = 3
PI = math.pi

# (n, pov, title) from Book 3/Chapter_Plan.md (titles match Book 3/Chapters/)
CHAPTERS = [
    (1, "S", "The Fallen Hill"), (2, "F", "Bel's Table"), (3, "R", "Davin's Hand"),
    (4, "S", "Liss's Kitchen"), (5, "C", "The Chair Between"), (6, "F", "Toll Gates"),
    (7, "S", "Stonehorns"), (8, "U", "Wages"), (9, "F", "The Houses' Table"),
    (10, "G", "Marshal"), (11, "S", "The Border"), (12, "F", "The Clock"),
    (13, "M", "Never Sleep Ashore"), (14, "S", "Salt on the Tongue"), (15, "F", "Chain Money"),
    (16, "R", "Far-Stone"), (17, "S", "The Reef Channel"), (18, "C", "The Breeding Pens"),
    (19, "F", "The Bell Comes In"), (20, "M", "The Berths"), (21, "S", "Unsalted"),
    (22, "F", "Pour With Me"), (23, "G", "The Candle Downs"), (24, "S", "The Drowned Road"),
    (25, "M", "The Last Milestone"), (26, "F", "The Pilot"), (27, "S", "The Lit Shore"),
    (28, "F", "The Shatters"), (29, "M", "Ashore"), (30, "S", "What She Showed"),
    (31, "R", "The Script in the Light"), (32, "F", "The Shrine"), (33, "U", "The Works"),
    (34, "S", "The Hall of Light"), (35, "F", "Two Hands"), (36, "R", "What the Ring Answers"),
    (37, "S", "Consent"), (38, "C", "Empty Pens"), (39, "F", "The Crossroads"),
    (40, "S", "Under the Sea"), (41, "G", "The Wend Camp"), (42, "F", "Homeward"),
    (43, "S", "The Saltings"), (44, "M", "Salt Debts"), (45, "F", "Three Hills"),
    (46, "G", "Banners"), (47, "S", "Kin"), (48, "U", "Night Shift"),
    (49, "F", "Fire in the Forest"), (50, "S", "Antlers"), (51, "F", "Plates"),
    (52, "R", "Where the Breath Went"), (53, "S", "The Middle of the World"), (54, "F", "Wren's Question"),
    (55, "G", "The Ring Plan"), (56, "S", "Black Ice"), (57, "R", "A Visitor"),
    (58, "F", "The Floating Market"), (59, "S", "The Warm Water"), (60, "M", "Barges"),
    (61, "F", "Eve"), (62, "U", "Watches"), (63, "S", "Noon"),
    (64, "F", "The First Day"), (65, "G", "The Line"), (66, "S", "Orrun"),
    (67, "C", "Night Flights"), (68, "F", "The Second Day"), (69, "R", "The Stage"),
    (70, "S", "The Hour"), (71, "U", "The Battery"), (72, "F", "Smoke"),
    (73, "G", "On the Gate"), (74, "S", "The Coal"), (75, "F", "Where the Island Was"),
    (76, "M", "The Masthead"), (77, "S", "Six Roads"), (78, "F", "The Top Field"),
    (79, "M", "No Price"), (80, "S", "The Count"), (81, "F", "Deep Sight"),
    (82, "R", "Breaths"), (83, "S", "The Threshold"), (84, "F", "First Light"),
    (85, "C", "Who Pours"), (86, "S", "The Watch"),
]
POV = {n: p for n, p, _ in CHAPTERS}


# ------------------------------------------------------------------ POV signs
def tideglass(c, x, y, s=30, w=4.5):
    for k in (-1, 1):
        c.brush([(x + k * s * 0.6, y - s), (x + k * s * 0.22, y - s * 0.45), (x, y),
                 (x + k * s * 0.22, y + s * 0.45), (x + k * s * 0.6, y + s)], w, taper=0.15, wobble=0.6)
    c.line(x - s * 0.7, y - s, x + s * 0.7, y - s, w, taper=0.3)
    c.line(x - s * 0.7, y + s, x + s * 0.7, y + s, w, taper=0.3)


def blade(c, x, y, s=40, w=5):
    c.brush([(x, y + s * 0.6), (x, y - s * 0.4), (x, y - s)], w, taper=0.6, wobble=0.5)
    c.line(x - s * 0.38, y + s * 0.45, x + s * 0.38, y + s * 0.45, w, taper=0.3)
    c.dot(x, y + s * 0.82, w * 1.2)


def cup(c, x, y, s=34, w=5):
    c.arc(x, y - s * 0.35, s * 0.62, 0.0, PI, w, taper=0.15, wob=0.01)
    c.line(x - s * 0.66, y - s * 0.35, x + s * 0.66, y - s * 0.35, w * 0.8, taper=0.3)
    c.line(x, y + s * 0.27, x, y + s * 0.6, w, taper=0.1)
    c.line(x - s * 0.32, y + s * 0.62, x + s * 0.32, y + s * 0.62, w, taper=0.3)


def block(c, x, y, s=34, w=5):
    h = s / 2
    c.brush([(x - h, y - h), (x + h, y - h), (x + h, y + h), (x - h, y + h), (x - h, y - h * 0.35)], w, taper=0.05, wobble=0.5)


def sail(c, x, y, s=40, w=4.5):
    c.line(x, y + s * 0.55, x, y - s, w, taper=0.2)
    c.brush([(x + 6, y - s * 0.85), (x + s * 0.6, y + s * 0.3), (x + 6, y + s * 0.3), (x + 6, y - s * 0.85)], w * 0.8, taper=0, wobble=0.4)
    c.arc(x, y - s * 0.6, s * 1.15, PI * 0.36, PI * 0.64, w, taper=0.3, wob=0.005)


def sign(c, pov, x, y, k=1.0):
    if pov == "S":
        c.ring(x, y, 22 * k, 5)
    elif pov == "F":
        c.triad(x, y, r=8 * k, spread=22 * k)
    elif pov == "R":
        tideglass(c, x, y, 30 * k)
    elif pov == "G":
        blade(c, x, y, 40 * k)
    elif pov == "C":
        cup(c, x, y, 34 * k)
    elif pov == "U":
        block(c, x, y, 34 * k)
    elif pov == "M":
        sail(c, x, y, 40 * k)


# ------------------------------------------------------------------ helpers (Book 3)
def boat(c, x, y, s=1.0, w=7):
    c.arc(x, y - 60 * s, 110 * s, PI * 0.25, PI * 0.75, w, taper=0.3)
    c.line(x - 60 * s, y - 20 * s, x + 60 * s, y - 20 * s, max(w * 0.55, 2), taper=0.6)


def ketch(c, x, y, s=1.0, w=6):
    """A boat with a mast and one sail."""
    boat(c, x, y, s, w)
    c.line(x, y - 22 * s, x, y - 200 * s, w * 0.7, taper=0.2)
    c.brush([(x + 8 * s, y - 190 * s), (x + 95 * s, y - 40 * s), (x + 8 * s, y - 40 * s), (x + 8 * s, y - 190 * s)], w * 0.6, taper=0)


def hump(c, x, base, wd, ht, w=10, fill=False, opacity=1.0, plates=0):
    """A Titan's back or a lion-hill: a low long arch of the land."""
    t = np.linspace(0, PI, 60)
    xs = x - wd / 2 + wd * t / PI
    ys = base - ht * np.sin(t) ** 0.8
    if fill:
        pts = list(zip(xs, ys)) + [(x + wd / 2, base), (x - wd / 2, base)]
        d = "M" + " L".join(f"{a:.1f},{b:.1f}" for a, b in pts) + " Z"
        op = f' fill-opacity="{opacity:.2f}"' if opacity < 1 else ""
        c.items.append(f'<path d="{d}" fill="{A.INK}"{op}/>')
    else:
        c.brush(np.c_[xs, ys], w, taper=0.5, opacity=opacity)
    for i in range(plates):
        u = (i + 1) / (plates + 1)
        tt = PI * (0.12 + 0.76 * u)
        px, py = x - wd / 2 + wd * tt / PI, base - ht * math.sin(tt) ** 0.8
        c.line(px, py - 4, px + 10, py - 30 - 10 * math.sin(tt), w * 0.5, taper=0.6)


def milestone(c, x, base, h=70, w=6):
    c.brush([(x - h * 0.18, base), (x - h * 0.14, base - h * 0.8), (x, base - h), (x + h * 0.14, base - h * 0.8), (x + h * 0.18, base)], w, taper=0.05)


def clock(c, x, y, r, w=8, h1=-PI / 2, h2=-PI / 2 + 0.9, ticks=True):
    c.ring(x, y, r, w, gap=0.0001)
    if ticks:
        for i in range(12):
            a = i * PI / 6
            c.line(x + r * 0.82 * math.cos(a), y + r * 0.82 * math.sin(a), x + r * 0.92 * math.cos(a), y + r * 0.92 * math.sin(a), max(w * 0.45, 2), taper=0.2)
    c.line(x, y, x + r * 0.7 * math.cos(h1), y + r * 0.7 * math.sin(h1), w * 0.7, taper=0.5)
    c.line(x, y, x + r * 0.5 * math.cos(h2), y + r * 0.5 * math.sin(h2), w, taper=0.5)
    c.dot(x, y, w * 0.9)


def tent(c, x, base, s=40, w=5):
    c.brush([(x - s, base), (x, base - s * 1.1), (x + s, base)], w, taper=0.1)
    c.line(x, base - s * 1.1, x, base, w * 0.5, taper=0.2, opacity=0.6)


def chair(c, x, base, s=80, w=7):
    c.line(x - s * 0.35, base, x - s * 0.35, base - s * 1.4, w, taper=0.1)
    c.line(x - s * 0.35, base - s * 0.55, x + s * 0.4, base - s * 0.55, w, taper=0.1)
    c.line(x + s * 0.4, base - s * 0.55, x + s * 0.4, base, w, taper=0.1)


def cart(c, x, base, s=1.0, w=5):
    c.brush([(x - 70 * s, base - 30 * s), (x + 70 * s, base - 30 * s), (x + 60 * s, base - 6 * s), (x - 60 * s, base - 6 * s), (x - 70 * s, base - 30 * s)], w, taper=0)
    c.ring(x - 38 * s, base + 6 * s, 14 * s, w * 0.8, gap=0.0001)
    c.ring(x + 38 * s, base + 6 * s, 14 * s, w * 0.8, gap=0.0001)


def stonehorn(c, x, y, s=1.0):
    c.disc(x, y, 13 * s)
    c.brush([(x - 6 * s, y - 10 * s), (x - 16 * s, y - 26 * s), (x - 8 * s, y - 34 * s)], 4 * s, taper=0.6)
    c.brush([(x + 6 * s, y - 10 * s), (x + 16 * s, y - 26 * s), (x + 8 * s, y - 34 * s)], 4 * s, taper=0.6)


def lamp(c, x, y, r=7):
    c.disc(x, y, r)
    c.rays(x, y, 8, r * 1.8, r * 3.4, 1.6)


def eye(c, x, y, wd, w=8):
    r = wd * 0.75
    h = math.sqrt(max(r * r - (wd / 2) ** 2, 1))
    a = math.asin((wd / 2) / r)
    c.arc(x, y + h, r, -PI / 2 - a, -PI / 2 + a, w, taper=0.5, wob=0.004)
    c.arc(x, y - h, r, PI / 2 - a, PI / 2 + a, w, taper=0.5, wob=0.004)


def tally(c, x, y, groups, w=4, h=46, gap=16, opacity=1.0):
    for g in range(groups):
        x0 = x + g * (gap * 5 + 22)
        for i in range(4):
            c.line(x0 + i * gap + c.rng.normal(0, 1.5), y, x0 + i * gap + c.rng.normal(0, 1.5), y - h, w, taper=0.3, opacity=opacity)
        c.line(x0 - 8, y - h * 0.25, x0 + 3 * gap + 8, y - h * 0.75, w, taper=0.3, opacity=opacity)


def sea(c, y0, y1, n=12, x0=40, x1=1460, amp=6, opacity=0.8, w=2.6):
    for i in range(n):
        yy = y0 + (y1 - y0) * i / max(n - 1, 1)
        c.wave(c.rng.uniform(x0, x0 + 140), c.rng.uniform(x1 - 140, x1), yy, amp, 0.008 + 0.003 * c.rng.random(),
               c.rng.uniform(0, 6), w * c.rng.uniform(0.6, 1.2), taper=0.9, opacity=opacity)


def snow(c, n, x0=60, x1=1440, y0=60, y1=940, rmax=3.2, op=0.55):
    for _ in range(n):
        c.dot(c.rng.uniform(x0, x1), c.rng.uniform(y0, y1), c.rng.uniform(1, rmax), op)


def smoke(c, cx, cy, n=9, wd=900, ht=260, opacity=0.35):
    for _ in range(n):
        x = cx + c.rng.normal(0, wd * 0.2)
        y = cy + c.rng.normal(0, ht * 0.3)
        r = c.rng.uniform(60, 170)
        c.arc(x, y, r, PI * c.rng.uniform(0.9, 1.1), PI * c.rng.uniform(1.7, 2.1), c.rng.uniform(2, 5), taper=0.8, opacity=opacity)


# ------------------------------------------------------------------ compositions
COMP = {}


def comp(n):
    def deco(f):
        COMP[n] = f
        return f
    return deco


@comp(1)   # The Fallen Hill: the lintel held over the salvage crew
def _(c):
    c.ground(y=760)
    c.brush([(160, 760), (300, 600), (420, 650), (560, 520), (700, 560), (860, 470), (1010, 590), (1160, 560), (1340, 760)], 6, taper=0.4, opacity=0.75)
    c.brush([(560, 330), (980, 290)], 34, taper=0.08)
    for x in (680, 760, 840):
        c.figure(x + c.rng.normal(0, 6), 755, 90, 6)
    for i in range(5):
        c.dot(770 + c.rng.normal(0, 60), 390 + i * 26, 2.2, 0.5)
    sign(c, "S", 420, 250)


@comp(2)   # Bel's Table: the hearth-word, fire up to the cave roof
def _(c):
    c.arc(750, 860, 560, PI * 1.08, PI * 1.92, 16, taper=0.4)
    c.ground(y=860, x0=220, x1=1280)
    flames(c, 650, 850, 860, 26, 220, 520)
    c.arc(750, 860, 545, PI * 1.38, PI * 1.62, 5, taper=0.7, opacity=0.6)
    c.line(690, 860, 810, 860, 14, taper=0.3)
    sign(c, "F", 1270, 200)


def flames(c, x0, x1, base, n=18, hmin=120, hmax=320):
    for _ in range(n):
        x = c.rng.uniform(x0, x1)
        h = c.rng.uniform(hmin, hmax)
        c.brush([(x, base), (x + c.rng.normal(0, 20), base - h * 0.5), (x + c.rng.normal(0, 40), base - h)], c.rng.uniform(4, 10), taper=0.9)


@comp(3)   # Davin's Hand: an old chart, the tide pulled east, one rising in the margin
def _(c):
    c.brush([(260, 200), (1240, 210), (1250, 800), (250, 790), (260, 200)], 7, taper=0)
    c.line(420, 205, 415, 795, 3, taper=0.1, opacity=0.6)
    for i in range(9):
        y = 270 + i * 58
        xs = np.linspace(470, 1200, 40)
        ys = y - (xs - 470) * 0.06 + 6 * np.sin(xs * 0.02 + i)
        c.brush(np.c_[xs, ys], 2.5, taper=0.9, opacity=0.55)
    c.brush([(300, 740), (325, 700), (340, 640), (350, 600)], 6, taper=0.5)
    c.ring(342, 590, 18, 3, gap=1.0, opacity=0.8)
    sign(c, "R", 1360, 880)


@comp(4)   # Liss's Kitchen: "into the light", west over the sea
def _(c):
    c.line(80, 600, 1420, 600, 3, taper=0.9, opacity=0.8)
    c.arc(260, 600, 110, PI, 2 * PI, 10, taper=0.3)
    c.rays(260, 600, 13, 140, 290, 3, PI * 1.03, PI * 1.97)
    for i in range(18):
        t = i / 17
        c.dot(1180 - t * 780, 640 + 120 * math.sin(t * PI) * 0.6, 4, 0.75 - 0.4 * t)
    c.ring(1220, 640, 22, 5)
    door_ = [(1300, 600), (1300, 470), (1350, 430), (1400, 470), (1400, 600)]
    c.brush(door_, 6, taper=0.05)


@comp(5)   # The Chair Between: two tables, the empty chair in the gap
def _(c):
    c.ground(y=700)
    c.line(150, 560, 600, 560, 12, taper=0.1)
    c.line(900, 560, 1350, 560, 12, taper=0.1)
    for x in (190, 560, 940, 1310):
        c.line(x, 560, x, 700, 6, taper=0.1)
    chair(c, 750, 700, 110, 9)
    sign(c, "C", 260, 230)


@comp(6)   # Toll Gates: the Coast Road, a pole across it every town
def _(c):
    c.ground(y=700, x0=60, x1=1440, w=4)
    for i, x in enumerate((330, 700, 1070)):
        c.line(x - 10, 700, x - 10, 470, 8, taper=0.05)
        c.line(x - 10, 520, x + 230, 520 + (12 if i == 1 else 0), 9, taper=0.1)
        c.line(x + 230, 700, x + 230, 560, 5, taper=0.1)
    for i in range(26):
        x = 80 + i * 9.5
        c.dot(x, 685 - c.rng.uniform(0, 18), c.rng.uniform(3, 6), 0.8)
    sign(c, "F", 1300, 230)


@comp(7)   # Stonehorns: the herds breast the Ysse ford in a line
def _(c):
    c.river(y=560, band=280, n=12, opacity=0.7)
    for i in range(9):
        t = i / 8
        stonehorn(c, 260 + t * 980, 590 - t * 110 + 16 * math.sin(i * 1.7), 1.0 + 0.3 * (i % 3 == 1))
    c.ring(1300, 210, 22, 5)


@comp(8)   # Wages: three thousand hands walking north for bread
def _(c):
    for i in range(70):
        t = i / 69
        x = 1250 - t * 820 + c.rng.normal(0, 26 * (1 - t) + 4)
        y = 900 - t * 760
        h = 60 * (1 - t) + 8
        c.line(x, y, x + 2, y - h, 2 + 5 * (1 - t), taper=0.4, opacity=0.9)
    sign(c, "U", 240, 820)


@comp(9)   # The Houses' Table: the Council's bench, one high chair
def _(c):
    for i in range(15):
        a = PI * (1.12 + 0.76 * i / 14)
        x, y = 750 + 520 * math.cos(a), 760 + 380 * math.sin(a)
        if i == 7:
            c.line(x, y + 30, x, y - 80, 9, taper=0.1)
            c.disc(x, y - 100, 13)
        else:
            c.disc(x, y, 11)
    c.line(420, 800, 1080, 800, 8, taper=0.3)
    sign(c, "F", 750, 880, 0.9)
    c.brush([(1250, 220), (1280, 200), (1310, 220)], 4, taper=0.5)
    c.brush([(1190, 260), (1215, 243), (1240, 260)], 3, taper=0.5)


@comp(10)  # Marshal: a chapel, someone sitting in it, not praying
def _(c):
    c.ground(y=760)
    c.arch(750, 760, 300, 520, 9)
    c.brush([(745, 760), (742, 680), (760, 640)], 9, taper=0.4)
    c.brush([(745, 700), (800, 702), (805, 760)], 7, taper=0.3)
    c.disc(768, 618, 13)
    sign(c, "G", 1200, 330)


@comp(11)  # The Border: two keepers of the gap, the clans pouring through
def _(c):
    c.ground(y=700)
    c.figure(600, 694, 230, 14)
    c.figure(900, 694, 230, 14, 0.02)
    for _ in range(320):
        x = c.rng.uniform(80, 1420)
        spread = 40 + abs(x - 750) * 0.45
        y = 650 + c.rng.normal(0, spread * 0.25) if abs(x - 750) > 150 else 650 + c.rng.normal(0, 25)
        if abs(x - 750) > 150 and x < 750:
            pass
        if 560 < x < 640 or 860 < x < 940:
            continue
        if x > 950:
            continue
        c.dot(x, min(y, 690), c.rng.uniform(1.5, 4.5), c.rng.uniform(0.5, 1))
    c.ring(600, 320, 22, 5)


@comp(12)  # The Clock: the Hall of Measures, two doors out
def _(c):
    clock(c, 750, 300, 170, 9, h1=-PI / 2 + 0.05, h2=-PI / 2 + 2.7)
    c.ground(y=820, x0=200, x1=1300)
    door_small(c, 420, 820)
    door_small(c, 1080, 820)
    c.figure(470, 815, 90, 6)
    c.figure(1030, 815, 90, 6)
    sign(c, "F", 1300, 600)


def door_small(c, x, base, w=110, h=200, wt=7):
    r = w / 2
    c.line(x - r, base, x - r, base - h + r, wt, taper=0.05)
    c.arc(x, base - h + r, r, PI, 2 * PI, wt, taper=0.05)
    c.line(x + r, base - h + r, x + r, base, wt, taper=0.05)


@comp(13)  # Never Sleep Ashore: the ketch anchored off a dark shore
def _(c):
    sea(c, 640, 900, 10, opacity=0.6)
    c.brush([(60, 520), (260, 470), (420, 520), (520, 600), (560, 640)], 9, taper=0.3)
    ketch(c, 1040, 650, 1.1)
    c.line(1040, 640, 960, 800, 2, taper=0.2, opacity=0.6)
    c.dot(300, 490, 6)
    sign(c, "M", 1340, 220)


@comp(14)  # Salt on the Tongue: a pinch of salt, the contract
def _(c):
    for i in range(70):
        y = 220 + i * 6.2
        c.dot(760 + c.rng.normal(0, 3 + i * 0.05), y, c.rng.uniform(1.2, 2.8), 0.85)
    for _ in range(160):
        x = 760 + c.rng.normal(0, 55)
        c.dot(x, 700 - max(0, 55 - abs(x - 760)) * 0.9 * c.rng.random() - c.rng.uniform(0, 4), c.rng.uniform(1.2, 3.4), 0.9)
    c.line(560, 710, 960, 712, 5, taper=0.5)
    sign(c, "S", 360, 300)


@comp(15)  # Chain Money: the harbour chain, one copper
def _(c):
    sea(c, 640, 920, 10, opacity=0.55)
    c.line(150, 640, 150, 300, 12, taper=0.05)
    c.line(1350, 640, 1350, 300, 12, taper=0.05)
    c.chain([(160, 340), (520, 520), (750, 560), (980, 520), (1340, 340)], 34, 5)
    c.ring(750, 650, 26, 6, gap=0.0001)
    c.line(744, 650, 756, 650, 4, taper=0)
    c.line(750, 590, 750, 624, 2, taper=0.2)
    sign(c, "F", 1190, 180)


@comp(16)  # Far-Stone: blocks of old stone that hum
def _(c):
    c.ground(y=760)
    for (x, y, wd, ht) in ((520, 760, 210, 120), (760, 760, 250, 120), (640, 640, 220, 110)):
        c.brush([(x - wd / 2, y), (x - wd / 2, y - ht), (x + wd / 2, y - ht), (x + wd / 2, y)], 7, taper=0)
        for r in range(2):
            c.line(x - wd / 2 + 30, y - ht + 35 + r * 30, x - wd / 2 + 30 + c.rng.uniform(40, 120), y - ht + 35 + r * 30, 3, taper=0.3, opacity=0.6)
    for i in range(5):
        c.arc(650, 650, 230 + i * 50, PI * 1.1, PI * 1.9, 2.5, taper=0.8, opacity=0.55 - i * 0.08)
    sign(c, "R", 1180, 600)


@comp(17)  # The Reef Channel: the stone lifted out of the channel
def _(c):
    c.brush([(80, 760), (500, 730), (900, 770), (1420, 740)], 6, taper=0.6)
    c.brush([(80, 880), (520, 900), (940, 870), (1420, 900)], 6, taper=0.6)
    for i in range(4):
        c.wave(200, 1300, 790 + i * 22, 4, 0.012, i, 2, taper=0.9, opacity=0.5)
    c.dot(760, 330, 120)
    for k in (-1, 0, 1):
        c.line(760 + k * 60, 470, 760 + k * 80, 700, 3, taper=0.8, opacity=0.5)
    sign(c, "S", 1250, 260)


@comp(18)  # The Breeding Pens: one freed dragon comes down to one man
def _(c):
    c.ground(y=760)
    for i, x in enumerate(np.linspace(150, 650, 5)):
        c.arch(x, 760, 80, 150, 5)
    c.figure(1060, 754, 170, 10)
    pts = [(1320, 120), (1260, 260), (1170, 380), (1100, 480)]
    for i, (x, y) in enumerate(pts):
        c.dot(x, y, 3 + i, 0.4 + 0.15 * i)
    c.disc(1110, 520, 16)
    sign(c, "C", 300, 250)


@comp(19)  # The Bell Comes In: a back like weather, coming at the chain
def _(c):
    sea(c, 560, 940, 14, opacity=0.55)
    for i in range(5):
        c.arc(1100, 1250, 460 + i * 60, PI * 1.25, PI * 1.75, 16 - i * 3, taper=0.6, opacity=1 - i * 0.15)
    c.chain([(60, 470), (330, 520), (600, 470)], 28, 4)
    c.line(60, 470, 60, 360, 9, taper=0.05)
    c.line(600, 470, 600, 360, 9, taper=0.05)
    sign(c, "F", 330, 220)


@comp(20)  # The Berths: the fleet in a row fitting out; one small boat turned away
def _(c):
    sea(c, 690, 900, 8, opacity=0.5)
    for i in range(7):
        boat(c, 200 + i * 145, 700, 0.6, 5)
        c.line(200 + i * 145, 685, 200 + i * 145, 500, 3.5, taper=0.2)
    ketch(c, 1330, 740, 0.55)
    sign(c, "M", 1300, 260)


@comp(21)  # Unsalted: through the broken boom at night
def _(c):
    sea(c, 620, 940, 12, opacity=0.6)
    c.chain([(40, 560), (380, 600), (640, 610)], 30, 5)
    c.chain([(880, 610), (1160, 600), (1460, 560)], 30, 5)
    ketch(c, 760, 780, 0.9)
    c.disc(1240, 200, 26, 0.9)
    c.ring(560, 300, 22, 5)


@comp(22)  # Pour With Me: ash into the tarn; a pull from the south-west
def _(c):
    c.disc(470, 760, 210, 0.92)
    c.brush([(470, 120), (472, 300), (470, 500)], 3, taper=0.6, opacity=0.8)
    for _ in range(30):
        c.dot(470 + c.rng.normal(0, 6), c.rng.uniform(140, 520), c.rng.uniform(1, 3), 0.6)
    for i in range(3):
        a = PI * 0.75
        c.line(1050 + i * 70, 260 + i * 30, 1050 + i * 70 + 140 * math.cos(a), 260 + i * 30 + 140 * math.sin(a), 3, taper=0.9, opacity=0.6)
    sign(c, "F", 1200, 230, 1.1)


@comp(23)  # The Candle Downs: a ward an hour long against a mountain coming
def _(c):
    c.ground(y=760)
    c.arc(640, 760, 330, PI, 2 * PI, 6, taper=0.2)
    for i in range(3):
        c.arc(640, 760, 300 - i * 30, PI * 1.05, PI * 1.95, 2, taper=0.6, opacity=0.4)
    for i in range(18):
        c.line(430 + i * 24, 760, 432 + i * 24, 720, 3, taper=0.4)
    hump(c, 1190, 760, 460, 360, fill=True, opacity=0.92)
    sign(c, "G", 220, 280)


@comp(24)  # The Drowned Road: milestones walking out into the sea
def _(c):
    sea(c, 380, 960, 20, opacity=0.5)
    for i in range(9):
        t = i / 8
        s = 1 - 0.85 * t
        milestone(c, 300 + t * 900, 900 - t * 480, 110 * s + 10, 7 * s + 2)
    sign(c, "S", 1300, 200)


@comp(25)  # The Last Milestone: one stone on the reef, the far shore's lights
def _(c):
    c.line(60, 520, 1440, 520, 2.5, taper=0.95, opacity=0.6)
    for i in range(11):
        c.dot(900 + i * 38 + c.rng.normal(0, 6), 512 - c.rng.uniform(0, 8), 2.6, 0.8)
    sea(c, 560, 900, 9, opacity=0.5)
    milestone(c, 400, 800, 300, 12)
    sign(c, "M", 1300, 820)


@comp(26)  # The Pilot: low over the masts, reading the stones
def _(c):
    sea(c, 700, 940, 9, opacity=0.5)
    for i in range(6):
        x = 260 + i * 210
        milestone(c, x, 780, 40 - i * 3, 4)
    c.brush([(120, 600), (500, 470), (900, 420), (1380, 300)], 2, taper=0.9, opacity=0.5)
    c.triad(1050, 380, r=24, spread=56, rot=-PI / 2 - 0.25)
    c.dot(1040, 300, 5)
    c.triad(260, 220, r=8, spread=22)


@comp(27)  # The Lit Shore: a white city half under the sand; light on the hills
def _(c):
    c.ground(y=700)
    c.brush([(500, 700), (700, 560), (900, 520), (1100, 560), (1420, 640)], 4, taper=0.6, opacity=0.6)
    for x in (900, 1180):
        c.rays(x, 520, 9, 30, 90, 2, PI * 1.1, PI * 1.9)
    for i, x in enumerate((250, 350, 450)):
        c.line(x - 40, 700, x - 40, 640 - i * 10, 6, taper=0.1)
        c.arc(x, 640 - i * 10, 40, PI, 2 * PI, 6, taper=0.1)
        c.line(x + 40, 640 - i * 10, x + 40, 700, 6, taper=0.1)
    for i in range(8):
        c.wave(100, 700, 720 + i * 14, 3, 0.02, i, 1.6, taper=0.9, opacity=0.35)
    sign(c, "S", 620, 300)


@comp(28)  # The Shatters: wind held over two boats
def _(c):
    for _ in range(36):
        x, y = c.rng.uniform(80, 1420), c.rng.uniform(560, 940)
        if abs(x - 750) < 220 and y < 760:
            continue
        a = c.rng.uniform(-0.5, 0.5)
        ln = c.rng.uniform(60, 180)
        c.line(x, y, x + ln * math.cos(a), y + ln * math.sin(a), c.rng.uniform(3, 8), taper=0.8)
    boat(c, 680, 720, 0.55, 5)
    boat(c, 820, 730, 0.55, 5)
    for i in range(4):
        c.arc(750, 760, 260 + i * 30, PI * 1.12, PI * 1.88, 5 - i, taper=0.5, opacity=0.8)
    sign(c, "F", 750, 220)


@comp(29)  # Ashore: light on the land, one line of steps off the boat
def _(c):
    c.line(60, 560, 760, 560, 5, taper=0.5)
    for i in range(13):
        a = PI * (0.25 + 0.5 * i / 12)
        c.line(380 + 260 * math.cos(a) * 0.4, 120, 380 + 520 * math.cos(a), 540, 2, taper=0.9, opacity=0.5)
    sea(c, 600, 900, 8, x0=500, opacity=0.5)
    ketch(c, 1100, 700, 0.8)
    for i in range(9):
        c.dot(1000 - i * 52, 690 - i * 15, 3.5, 0.8 - i * 0.06)
    sign(c, "M", 1340, 220)


@comp(30)  # What She Showed: the mountain looking at the lion
def _(c):
    c.ground(y=740)
    hump(c, 920, 740, 900, 480, w=14)
    for i in range(3):
        hump(c, 920, 740, 820 - i * 120, 420 - i * 90, w=3, opacity=0.45)
    hump(c, 330, 740, 160, 60, fill=True)
    sign(c, "S", 330, 560)


@comp(31)  # The Script in the Light: words written on the air
def _(c):
    c.ground(y=840)
    c.glyphs(380, 300, 1120, rows=4, gap=60, w=3, mark=(2, 3))
    for i in range(16):
        a = PI * (1.05 + 0.9 * i / 15)
        c.line(750 + 520 * math.cos(a), 760 + 520 * math.sin(a), 750 + 600 * math.cos(a), 760 + 600 * math.sin(a), 2.5, taper=0.9, opacity=0.5)
    sign(c, "R", 750, 760)


@comp(32)  # The Shrine: a crossroads, three faces of light
def _(c):
    c.brush([(100, 960), (750, 620), (1400, 960)], 5, taper=0.7)
    c.brush([(260, 560), (750, 620), (1240, 560)], 3, taper=0.8, opacity=0.6)
    c.line(750, 620, 750, 400, 9, taper=0.1)
    for k, a in enumerate((PI * 1.0, PI * 1.5, PI * 0.0)):
        x, y = 750 + 46 * math.cos(a), 350 + 30 * math.sin(a)
        c.ring(x, y, 24, 4, gap=1.2, start=a + 0.6)
    c.rays(750, 350, 18, 90, 200, 2)
    sign(c, "F", 1260, 220)


@comp(33)  # The Works: the great chain coming off the anvils
def _(c):
    c.ground(y=800)
    c.chain([(500, 60), (620, 300), (700, 520), (720, 700)], 58, 7)
    c.brush([(620, 800), (650, 720), (820, 720), (870, 700), (820, 760), (790, 800)], 9, taper=0)
    c.embers(830, 690, 70, 300, 200, 4)
    sign(c, "U", 1250, 300)


@comp(34)  # The Hall of Light: a roofless hall, a long pool, the two signs at its end
def _(c):
    for k in (-1, 1):
        for i in range(7):
            t = i / 6
            x = 750 + k * (620 - 520 * t)
            yb = 940 - 380 * t
            h = 360 - 260 * t
            c.line(x, yb, x, yb - h, 7 - 4 * t, taper=0.1)
    c.brush([(560, 940), (720, 570), (780, 570), (940, 940)], 3, taper=0, opacity=0.5)
    c.ring(718, 470, 18, 4)
    c.triad(785, 470, r=6, spread=16)
    c.rays(750, 470, 12, 70, 140, 2)


@comp(35)  # Two Hands: two curves facing, the two signs between
def _(c):
    c.arc(1140, 500, 520, PI * 0.86, PI * 1.14, 18, taper=0.5)
    c.arc(360, 500, 520, -PI * 0.14, PI * 0.14, 18, taper=0.5)
    c.ring(700, 500, 24, 5)
    c.triad(800, 500, r=8, spread=22)
    c.glyphs(560, 170, 940, rows=2, gap=30, w=3)


@comp(36)  # What the Ring Answers: a coal that answers a breath
def _(c):
    c.disc(900, 500, 34)
    for i in range(5):
        a = -PI / 2 + i * 2 * PI / 5
        c.ring(900 + 120 * math.cos(a), 500 + 120 * math.sin(a), 22, 4, gap=0.0001)
    for i in range(5):
        y = 380 + i * 60
        c.brush([(140, y + 20), (360, y), (580, y + 30 - i * 8), (740, 500 + (y - 500) * 0.4)], 2.5, taper=0.9, opacity=0.55)
    sign(c, "R", 1290, 830)


@comp(37)  # Consent: light coming down through the ring into the ground
def _(c):
    c.ground(y=780)
    for i in range(15):
        x = 750 + (i - 7) * 56
        c.line(x, 80, 750 + (i - 7) * 6, 620, 2.5, taper=0.9, opacity=0.45)
    c.ring(750, 660, 28, 6)
    hump(c, 750, 780, 360, 70, w=8)


@comp(38)  # Empty Pens: a row of empty stalls
def _(c):
    c.ground(y=720)
    for x in np.linspace(240, 1260, 7):
        c.arch(x, 720, 120, 220, 6)
    for i in range(5):
        c.brush([(1180 - i * 90, 260 - i * 20), (1200 - i * 90, 240 - i * 20), (1220 - i * 90, 260 - i * 20)], 3, taper=0.5, opacity=0.7)
    sign(c, "C", 200, 240)


@comp(39)  # The Crossroads: one light dividing three ways
def _(c):
    c.brush([(750, 60), (750, 260), (750, 400)], 12, taper=0.4)
    for k, ang in ((-1, 0.65), (0, 0.0), (1, -0.65)):
        x1 = 750 - math.sin(ang) * 520
        y1 = 400 + math.cos(ang) * 420
        c.brush([(750, 400), (750 - math.sin(ang) * 260, 400 + math.cos(ang) * 220), (x1, y1)], 6, taper=0.7)
        c.disc(x1, y1 + 22, 26)
    c.rays(750, 400, 20, 30, 90, 2)
    sign(c, "F", 1300, 180)


@comp(40)  # Under the Sea: the stone opening ahead and closing behind
def _(c):
    sea(c, 80, 380, 12, opacity=0.5)
    c.brush([(60, 440), (1440, 430)], 9, taper=0.6)
    for _ in range(110):
        c.dot(c.rng.uniform(80, 1420), c.rng.uniform(470, 960), c.rng.uniform(1.5, 4), 0.45)
    c.arc(820, 700, 80, PI * 0.6, PI * 1.4, 10, taper=0.4)
    c.arc(820, 700, 80, -PI * 0.4, PI * 0.4, 4, taper=0.6, opacity=0.5)
    c.ring(820, 700, 18, 5)
    tally(c, 120, 900, 2, w=3, h=36, gap=12, opacity=0.6)
    c.line(330, 885, 360, 872, 3, taper=0.4, opacity=0.4)


@comp(41)  # The Wend Camp: tents behind the river; a great ring of chain on the horizon
def _(c):
    c.river(y=820, band=110, n=6, opacity=0.6)
    c.ground(y=700)
    for i in range(9):
        tent(c, 200 + i * 80, 700, 30 + (i % 3) * 6, 4)
    c.chain([(1250 + 120 * math.cos(a), 520 + 120 * math.sin(a)) for a in np.linspace(0, 2 * PI, 40)], 26, 4)
    sign(c, "G", 760, 280)


@comp(42)  # Homeward: a day and a night over the sea
def _(c):
    sea(c, 760, 960, 8, opacity=0.5)
    c.arc(750, 1200, 760, PI * 1.12, PI * 1.88, 3, taper=0.9, opacity=0.6)
    c.disc(1200, 230, 30)
    c.ring(320, 230, 30, 3, gap=0.0001, opacity=0.7)
    boat(c, 980, 850, 0.4, 4)
    sign(c, "F", 260, 600)


@comp(43)  # The Saltings: a hill comes out of the sea with a woman on its head
def _(c):
    sea(c, 760, 960, 8, opacity=0.5)
    c.ground(y=740, x0=60, x1=1440)
    hump(c, 620, 740, 760, 330, fill=True, opacity=0.95)
    c.ring(820, 340, 18, 4)
    for i in range(4):
        x = 1120 + i * 80
        c.brush([(x - 20, 740), (x - 20, 712), (x, 692), (x + 20, 712), (x + 20, 740)], 4, taper=0.05)


@comp(44)  # Salt Debts: the ledger's columns
def _(c):
    for k in range(4):
        x = 360 + k * 170
        n = (9, 6, 12, 4)[k]
        for i in range(n):
            c.arc(x, 760 - i * 26, 58, PI * 0.15, PI * 0.85, 5, taper=0.2, wob=0.01)
            c.arc(x, 760 - i * 26 - 48, 58, PI * 0.2, PI * 0.8, 2, taper=0.6, wob=0.01, opacity=0.4)
    c.line(220, 800, 1000, 800, 6, taper=0.4)
    sign(c, "M", 1250, 560, 1.2)


@comp(45)  # Three Hills: too big for the yard
def _(c):
    c.ground(y=760)
    for x, wd, ht in ((420, 380, 260), (760, 300, 200), (1080, 420, 300)):
        hump(c, x, 760, wd, ht, w=11)
    door_small(c, 260, 760, 50, 70, 5)
    c.figure(320, 756, 50, 4)
    sign(c, "F", 1300, 190)


@comp(46)  # Banners: every banner leaning toward the light
def _(c):
    c.ground(y=780)
    c.disc(200, 420, 40)
    c.rays(200, 420, 20, 60, 160, 2.5)
    for i in range(10):
        x = 500 + i * 85
        lean = -0.18 - 0.03 * i
        top = (x + lean * 360, 780 - 360)
        c.line(x, 780, *top, 4, taper=0.2)
        c.brush([top, (top[0] + 46, top[1] + 12), (top[0] + 6, top[1] + 50)], 3, taper=0.1, opacity=0.8)
    sign(c, "G", 1330, 240)


@comp(47)  # Kin: a ring of space around her that nobody steps into
def _(c):
    c.ground(y=GROUND)
    for _ in range(420):
        a = c.rng.uniform(0, 2 * PI)
        r = 230 + abs(c.rng.normal(0, 130))
        x, y = 750 + r * 1.6 * math.cos(a), 520 + r * 0.9 * math.sin(a)
        if 40 < x < 1460 and 60 < y < 960:
            c.dot(x, y, c.rng.uniform(1.5, 4), c.rng.uniform(0.4, 0.9))
    c.ring(750, 520, 26, 6)


@comp(48)  # Night Shift: chain on the flats under work-lamps
def _(c):
    c.line(60, 760, 1440, 760, 4, taper=0.8)
    c.line(60, 790, 1440, 790, 4, taper=0.8)
    for i in range(4):
        x = 260 + i * 300
        c.line(x - 110, 740, x + 110, 740, 7, taper=0.1)
        c.chain([(x - 100, 715), (x + 100, 715)], 24, 3)
        c.line(x + 150, 760, x + 150, 470, 3, taper=0.1)
        lamp(c, x + 150, 450, 7)
    for i in range(40):
        c.dot(c.rng.uniform(100, 1400), c.rng.uniform(80, 340), c.rng.uniform(1, 2.5), 0.5)
    sign(c, "U", 1330, 200)


@comp(49)  # Fire in the Forest: a wood that walks, fire from the sky
def _(c):
    c.ground(y=860)
    for _ in range(30):
        x = c.rng.uniform(200, 1300)
        h = c.rng.uniform(260, 460)
        c.brush([(x, 860), (x + c.rng.normal(0, 30), 860 - h * 0.6), (x + c.rng.normal(0, 50), 860 - h)], c.rng.uniform(3, 7), taper=0.7)
    for i in range(7):
        x = 520 + i * 40
        c.line(x + 220, 110, x - 40, 420, 9 - i * 0.7, taper=0.9)
    c.triad(1080, 160, r=14, spread=34)
    c.triad(260, 160, r=8, spread=22)


@comp(50)  # Antlers: antlers held over opened earth
def _(c):
    c.ground(y=780, x0=90, x1=640)
    c.ground(y=780, x0=860, x1=1410)
    c.brush([(640, 780), (700, 870), (760, 960)], 8, taper=0.4)
    c.brush([(860, 780), (800, 870), (770, 960)], 8, taper=0.4)

    for k in (-1, 1):
        beam = [(750 + k * 30, 650), (750 + k * 140, 560), (750 + k * 260, 420), (750 + k * 300, 240), (750 + k * 260, 120)]
        c.brush(beam, 14, taper=0.6)
        for (bx, by), ln in zip(beam[1:4], (110, 130, 110)):
            c.brush([(bx, by), (bx - k * 18, by - ln * 0.55), (bx - k * 10, by - ln)], 7, taper=0.8)
    c.disc(750, 680, 50)
    sign(c, "S", 1250, 650)


@comp(51)  # Plates: carts carrying plates away
def _(c):
    c.ground(y=780)
    for i in range(4):
        x = 360 + i * 260
        cart(c, x, 760, 1.0, 5)
        for k in (-1, 1):
            c.brush([(x + k * 30, 728), (x + k * 30 + 28, 690), (x + k * 30, 640), (x + k * 30 - 28, 690), (x + k * 30, 728)], 4, taper=0)
    sign(c, "F", 1320, 260)


@comp(52)  # Where the Breath Went: every line runs west to one point
def _(c):
    target = (180, 470)
    for i in range(8):
        x, y = 600 + (i % 4) * 230, 200 + (i // 4) * 520 + c.rng.normal(0, 40)
        c.disc(x, y, 6)
        n = 24
        for k in range(n):
            t = k / n
            px = x + (target[0] - x) * t
            py = y + (target[1] - y) * t + 30 * math.sin(t * PI) * (1 if i % 2 else -1)
            c.dot(px, py, 2.2, 0.35 + 0.5 * t)
    c.disc(*target, 28)
    sign(c, "R", 1340, 860)


@comp(53)  # The Middle of the World: six roads to the eddy
def _(c):
    t = np.linspace(0, 3.2 * PI, 220)
    r = 12 + 14 * t
    c.brush(np.c_[750 + r * np.cos(t), 520 + r * np.sin(t) * 0.55], 4, taper=0.9)
    for k in range(6):
        a = k * PI / 3 + 0.2
        for d in (-0.07, 0.07):
            c.brush([(750 + 190 * math.cos(a + d * 0.3), 520 + 120 * math.sin(a + d * 0.3)), (750 + 760 * math.cos(a + d), 520 + 470 * math.sin(a + d))], 3.5, taper=0.7)
    sign(c, "S", 1260, 860)


@comp(54)  # Wren's Question: the tarn, and a hall under it
def _(c):
    c.brush(np.c_[750 + 330 * np.cos(np.linspace(0, 2 * PI, 80)), 230 + 70 * np.sin(np.linspace(0, 2 * PI, 80))], 8, taper=0)
    for i in range(4):
        c.wave(500, 1000, 210 + i * 14, 3, 0.03, i, 1.5, taper=0.9, opacity=0.4)
    for _ in range(60):
        c.dot(c.rng.uniform(200, 1300), c.rng.uniform(380, 900), c.rng.uniform(1, 3), 0.35)
    c.arch(750, 820, 260, 280, 4)
    c.line(560, 820, 940, 820, 4, taper=0.5)
    sign(c, "F", 1260, 160)


@comp(55)  # The Ring Plan: the line across the Vale; a ward on each bank, not across
def _(c):
    xs = np.linspace(0, 1, 50)
    for k in (-1, 1):
        c.brush(np.c_[750 + k * 40 + 18 * np.sin(xs * 9), 60 + xs * 880], 4, taper=0.2)
    c.line(150, 520, 690, 520, 9, taper=0.1)
    c.line(810, 520, 1350, 520, 9, taper=0.1)
    for x in list(np.linspace(170, 670, 6)) + list(np.linspace(830, 1330, 6)):
        c.line(x, 505, x, 535, 4, taper=0.2)
    c.arc(420, 520, 260, PI * 1.02, PI * 1.98, 4, taper=0.4, opacity=0.7)
    c.arc(1080, 520, 260, PI * 1.02, PI * 1.98, 4, taper=0.4, opacity=0.7)
    sign(c, "G", 1280, 830)


@comp(56)  # Black Ice: the river frozen overnight, something pale under it
def _(c):
    for i in range(15):
        c.line(60, 300 + i * 34, 1440, 300 + i * 34 + c.rng.normal(0, 3), 2.4, taper=0.95, opacity=0.55)
    xs = np.linspace(150, 1350, 200)
    c.brush(np.c_[xs, 560 + 70 * np.sin(xs * 0.008 + 1) + 30 * np.sin(xs * 0.021)], 22, taper=0.8, opacity=0.25)
    c.brush([(980, 300), (1010, 420), (1000, 520), (1040, 660), (1030, 800)], 3, taper=0.6)
    c.ring(320, 200, 22, 5)


@comp(57)  # A Visitor: a lamp in a back room, someone in the doorway
def _(c):
    c.brush([(300, 820), (300, 220), (1200, 220), (1200, 820)], 8, taper=0)
    c.line(300, 820, 1200, 820, 6, taper=0.2)
    lamp(c, 520, 520, 12)
    c.line(940, 820, 940, 360, 6, taper=0.05)
    c.line(1100, 820, 1100, 360, 6, taper=0.05)
    c.line(940, 360, 1100, 360, 6, taper=0.05)
    c.figure(1020, 815, 300, 22)
    sign(c, "R", 520, 700)


@comp(58)  # The Floating Market: a market roped together, towed upriver
def _(c):
    c.river(y=720, band=260, n=11, opacity=0.6)
    pts = []
    for i in range(10):
        x = 240 + i * 100
        y = 700 + 30 * math.sin(i * 0.7)
        c.brush([(x - 35, y), (x + 35, y), (x + 30, y + 22), (x - 30, y + 22), (x - 35, y)], 4, taper=0)
        c.line(x - 20, y, x - 20, y - 40, 3, taper=0.2)
        pts.append((x, y))
    c.brush([(1170, 700), (1270, 540), (1320, 380)], 2.5, taper=0.4, opacity=0.8)
    c.triad(1330, 330, r=10, spread=26)


@comp(59)  # The Warm Water: the tarn that never freezes
def _(c):
    for i in range(18):
        y = 360 + i * 28
        c.line(80, y, 1420, y + c.rng.normal(0, 2), 2, taper=0.95, opacity=0.4)
    c.disc(750, 610, 170, 0.95)
    for k in (-60, 0, 60):
        c.brush([(750 + k, 430), (750 + k + 20, 330), (750 + k - 10, 230), (750 + k + 15, 140)], 3, taper=0.9, opacity=0.6)
    sign(c, "S", 1240, 200)


@comp(60)  # Barges: barges going up the river into the distance
def _(c):
    c.brush([(240, 980), (620, 520), (720, 300)], 5, taper=0.6)
    c.brush([(1260, 980), (880, 520), (780, 300)], 5, taper=0.6)
    for i in range(8):
        t = i / 7
        s = 1 - 0.8 * t
        y = 900 - t * 560
        c.brush([(750 - 70 * s, y), (750 + 70 * s, y), (750 + 60 * s, y + 20 * s), (750 - 60 * s, y + 20 * s), (750 - 70 * s, y)], 3 + 3 * s, taper=0)
    sign(c, "M", 1260, 260)


@comp(61)  # Eve: on Liss's ferry mid-eddy; five links passed between
def _(c):
    c.line(40, 380, 1460, 410, 3, taper=0.1)
    sea(c, 520, 900, 11, opacity=0.5)
    c.brush([(560, 560), (940, 560), (920, 600), (580, 600), (560, 560)], 6, taper=0)
    c.line(750, 560, 750, 400, 2, taper=0.2, opacity=0.6)
    c.ring(650, 520, 20, 5)
    c.triad(850, 520, r=7, spread=19)
    c.chain([(700, 250), (800, 250)], 18, 3)


@comp(62)  # Watches: a league of green lamps down the Iron Road
def _(c):
    for i in range(22):
        t = i / 21
        x = 140 + t * 1100
        y = 820 - t * 420
        r = 10 - 7 * t
        lamp(c, x, y, r)
    c.line(120, 860, 1300, 410, 3, taper=0.9, opacity=0.5)
    clock(c, 1250, 760, 60, 4, h1=-PI / 2, h2=-PI / 2 - 0.25)
    sign(c, "U", 260, 260)


@comp(63)  # Noon: the sun overhead, a ward on each bank
def _(c):
    c.disc(750, 120, 34)
    c.rays(750, 120, 16, 50, 100, 2.5)
    c.ground(y=780, x0=80, x1=690)
    c.ground(y=780, x0=810, x1=1420)
    c.wave(700, 800, 800, 4, 0.05, 0, 2, taper=0.9)
    for k, x in ((-1, 400), (1, 1100)):
        c.arc(x, 780, 300, PI * 1.02, PI * 1.98, 6, taper=0.3)
        c.arc(x, 780, 270, PI * 1.1, PI * 1.9, 2, taper=0.6, opacity=0.4)
    sign(c, "S", 400, 700)


@comp(64)  # The First Day: the air full, fire across a league
def _(c):
    for _ in range(24):
        x, y = c.rng.uniform(100, 1400), c.rng.uniform(100, 420)
        s = c.rng.uniform(10, 22)
        c.brush([(x - s, y + s * 0.4), (x, y), (x + s, y + s * 0.4)], 3, taper=0.5, opacity=0.8)
    c.brush([(80, 640), (500, 610), (1000, 620), (1440, 590)], 18, taper=0.9)
    c.ground(y=820)
    c.triad(300, 560, r=12, spread=30)


@comp(65)  # The Line: a wall that holds under a ward
def _(c):
    c.line(80, 700, 1420, 700, 12, taper=0.2)
    for i in range(40):
        x = 120 + i * 32
        c.line(x, 700, x + c.rng.normal(0, 2), 640 - (i % 3) * 8, 4, taper=0.4)
    c.arc(750, 1300, 900, PI * 1.24, PI * 1.76, 6, taper=0.3)
    for i in range(3):
        c.arc(750, 1300, 870 - i * 30, PI * 1.28, PI * 1.72, 2, taper=0.6, opacity=0.4)
    sign(c, "G", 750, 860)


@comp(66)  # Orrun: kin against kin, a hill against a hill
def _(c):
    c.river(y=840, band=120, n=6, opacity=0.6)
    hump(c, 470, 760, 620, 380, fill=True, opacity=0.95)
    hump(c, 1060, 760, 620, 420, w=14, plates=7)
    c.ring(480, 300, 22, 5)


@comp(67)  # Night Flights: the wounded carried north all night
def _(c):
    for i in range(14):
        t = i / 13
        x, y = 200 + t * 1000 + c.rng.normal(0, 40), 820 - t * 620 + c.rng.normal(0, 40)
        s = 26 - 14 * t
        c.brush([(x - s, y + s * 0.5), (x, y), (x + s, y + s * 0.5)], 4 - 2 * t, taper=0.5)
        c.line(x - s * 0.3, y + s * 0.9, x + s * 0.3, y + s * 0.9, 2, taper=0.2, opacity=0.6)
    for i in range(12):
        lamp(c, 760 + i * 50, 900, 4)
    sign(c, "C", 240, 220)


@comp(68)  # The Second Day: the downed back, the coal seen, the two signs together
def _(c):
    c.river(y=860, band=100, n=5, opacity=0.5)
    hump(c, 700, 800, 1100, 330, w=16, plates=11)
    c.disc(760, 560, 16)
    c.rays(760, 560, 12, 26, 60, 2)
    c.brush([(1240, 800), (1220, 640), (1180, 520)], 20, taper=0.4)
    c.ring(1170, 240, 20, 5)
    c.triad(1250, 240, r=7, spread=19)


@comp(69)  # The Stage: a stage on iron legs, a hooded man on it
def _(c):
    c.ground(y=840)
    c.line(560, 840, 640, 420, 7, taper=0.1)
    c.line(940, 840, 860, 420, 7, taper=0.1)
    c.line(600, 630, 900, 630, 4, taper=0.2)
    c.line(560, 420, 940, 420, 10, taper=0.1)
    c.figure(750, 414, 130, 10)
    c.arc(750, 270, 24, PI * 0.8, PI * 2.2, 5, taper=0.2)
    sign(c, "R", 260, 260)


@comp(70)  # The Hour: a watch at noon
def _(c):
    clock(c, 750, 480, 110, 7, h1=-PI / 2, h2=-PI / 2 + 0.02)
    c.arc(750, 340, 24, PI, 2 * PI, 5, taper=0.2)
    c.ring(1220, 820, 22, 5)


@comp(71)  # The Battery: a winch, its chain, a brake
def _(c):
    c.ring(560, 420, 170, 12, gap=0.0001)
    for k in range(6):
        a = k * PI / 3 + 0.2
        c.line(560, 420, 560 + 160 * math.cos(a), 420 + 160 * math.sin(a), 5, taper=0.2)
    c.disc(560, 420, 20)
    c.chain([(730, 420), (1000, 520), (1180, 820)], 34, 5)
    c.brush([(380, 600), (520, 700), (640, 860)], 16, taper=0.2)
    sign(c, "U", 1250, 240)


@comp(72)  # Smoke: holding three above the smoke; a road kept open below
def _(c):
    smoke(c, 750, 640, 26, 1200, 260, 0.35)
    c.brush([(100, 960), (600, 860), (900, 860), (1400, 960)], 4, taper=0.7, opacity=0.8)
    c.triad(750, 240, r=20, spread=50)
    for k in (-1, 0, 1):
        c.line(750 + k * 30, 310, 750 + k * 50, 520, 2, taper=0.9, opacity=0.5)


@comp(73)  # On the Gate: a gate with people standing in it
def _(c):
    c.ground(y=780)
    c.line(420, 780, 420, 300, 14, taper=0.05)
    c.line(1080, 780, 1080, 300, 14, taper=0.05)
    c.line(380, 320, 1120, 310, 14, taper=0.1)
    for i in range(9):
        c.figure(500 + i * 63, 776, 150 + c.rng.normal(0, 8), 7, c.rng.normal(0, 0.02))
    sign(c, "G", 1300, 560)


@comp(74)  # The Coal: the coal among five dark eggs
def _(c):
    c.disc(750, 480, 46)
    c.rays(750, 480, 22, 70, 150, 2.5)
    for i in range(5):
        a = PI / 2 + i * 2 * PI / 5
        c.disc(750 + 250 * math.cos(a), 480 + 210 * math.sin(a), 30, 0.9)
    c.ring(1240, 840, 22, 5)


@comp(75)  # Where the Island Was: the river pouring into the middle; every horizon lit
def _(c):
    c.ground(y=560, x0=60, x1=1440, w=4)
    for x in (130, 420, 1080, 1370):
        c.rays(x, 560, 9, 20, 120, 2, PI * 1.1, PI * 1.9)
    t = np.linspace(0, 4 * PI, 260)
    r = 260 - 19 * t
    c.brush(np.c_[750 + r * np.cos(t), 760 + r * np.sin(t) * 0.45], 5, taper=0.5)
    c.disc(750, 760, 18)
    sign(c, "F", 750, 200)


@comp(76)  # The Masthead: from the masthead, two shapes far down the water
def _(c):
    c.line(240, 980, 240, 140, 10, taper=0.1)
    c.brush([(190, 200), (290, 200), (280, 240), (200, 240), (190, 200)], 5, taper=0)
    c.line(240, 300, 600, 980, 2, taper=0.2, opacity=0.5)
    c.line(80, 560, 1440, 560, 2.5, taper=0.95, opacity=0.7)
    sea(c, 590, 940, 9, x0=400, opacity=0.45)
    c.arc(1080, 590, 70, PI * 1.1, PI * 1.9, 7, taper=0.4)
    c.arc(1210, 595, 50, PI * 1.15, PI * 1.85, 6, taper=0.4)
    sign(c, "M", 520, 220)


@comp(77)  # Six Roads: six roads north, a lion on each
def _(c):
    for k in range(6):
        x0 = 150 + k * 240
        c.brush([(x0, 960), (x0 + (750 - x0) * 0.5, 560), (750, 180)], 4, taper=0.6)
        t = 0.32
        x = x0 + (750 - x0) * t * 1.05
        hump(c, x, 960 - 780 * t + 30, 90, 40, fill=True, opacity=0.75)
    c.ring(750, 150, 20, 5)


@comp(78)  # The Top Field: a wall of fire across the Way below the field
def _(c):
    for i in range(10):
        c.line(220, 160 + i * 22, 1280, 150 + i * 22, 2.4, taper=0.9, opacity=0.5)
    c.brush([(740, 960), (745, 600), (750, 380)], 5, taper=0.6)
    flames(c, 200, 1300, 700, 40, 80, 220)
    c.line(160, 700, 1340, 700, 6, taper=0.6)
    for i in range(8):
        c.dot(750 + c.rng.normal(0, 4), 560 - i * 22, 3, 0.8)
    sign(c, "F", 1300, 860)


@comp(79)  # No Price: salt from a pocket as people climb to the door
def _(c):
    c.brush([(80, 960), (600, 680), (1100, 360), (1380, 230)], 5, taper=0.5)
    c.brush([(1250, 300), (1250, 150), (1300, 115), (1350, 150), (1350, 270)], 6, taper=0.05)
    for i in range(22):
        t = i / 21
        c.figure(250 + t * 950, 900 - t * 600 - 12, 48, 4)
    for _ in range(80):
        x = c.rng.uniform(300, 1100)
        c.dot(x, 920 - (x - 80) * 0.57 + abs(c.rng.normal(0, 30)), c.rng.uniform(1, 2.6), 0.7)
    sign(c, "M", 260, 260)


@comp(80)  # The Count: the count going in at the door
def _(c):
    door(c, 1220, 820, 200, 420, 9)
    c.ground(y=820, x0=60, x1=1440)
    for r in range(4):
        tally(c, 120 + r * 40, 420 + r * 120, 7 - r, w=4, h=56, gap=17)
    c.ring(1220, 560, 22, 5)


def door(c, x, base, w=160, h=300, wt=8):
    r = w / 2
    c.line(x - r, base, x - r, base - h + r, wt, taper=0.05)
    c.arc(x, base - h + r, r, PI, 2 * PI, wt, taper=0.05)
    c.line(x + r, base - h + r, x + r, base, wt, taper=0.05)


@comp(81)  # Deep Sight: an eye that sees through the ice
def _(c):
    eye(c, 750, 260, 360, 9)
    c.disc(750, 260, 30)
    for i in range(10):
        c.line(80, 520 + i * 30, 1420, 520 + i * 30, 2.2, taper=0.95, opacity=0.5)
    c.line(750, 330, 750, 760, 2, taper=0.8, opacity=0.5)
    xs = np.linspace(300, 1200, 120)
    c.brush(np.c_[xs, 840 + 30 * np.sin(xs * 0.012)], 16, taper=0.8, opacity=0.6)
    sign(c, "F", 1300, 200)


@comp(82)  # Breaths: a row of breaths, going out one by one
def _(c):
    n = 7
    for i in range(n):
        x = 220 + i * 180
        op = 0.95 - 0.13 * i if i < n - 1 else 1.0
        if i < n - 1:
            c.ring(x, 480, 34, 5, gap=0.4 + 0.5 * i, opacity=max(op, 0.2))
        else:
            c.disc(x, 480, 30)
    c.line(150, 600, 1350, 600, 3, taper=0.9, opacity=0.6)
    sign(c, "R", 750, 800)


@comp(83)  # The Threshold: the lion lying across the door under the mountain
def _(c):
    c.brush([(60, 900), (380, 520), (620, 260), (760, 120), (900, 260), (1140, 520), (1440, 900)], 10, taper=0.4)
    door(c, 750, 900, 180, 300, 9)
    hump(c, 750, 900, 360, 70, fill=True)
    c.ring(980, 860, 22, 5)


@comp(84)  # First Light: a thin line of light high in the dark door; pairs apart
def _(c):
    c.brush([(560, 900), (560, 260), (940, 260), (940, 900)], 10, taper=0)
    c.line(600, 300, 900, 300, 3, taper=0.3, opacity=0.6)
    for i in range(6):
        x = 200 + i * 220 if i < 3 else 380 + i * 200
        x = (180, 300, 420, 1080, 1200, 1320)[i]
        c.dot(x - 20, 820, 7)
        c.disc(x + 22, 822, 11, 0.6)
    sign(c, "F", 750, 600, 0.9)


@comp(85)  # Who Pours: the cup tipped over the tarn
def _(c):
    c.brush(np.c_[750 + 420 * np.cos(np.linspace(0, 2 * PI, 90)), 780 + 100 * np.sin(np.linspace(0, 2 * PI, 90))], 7, taper=0)
    for i in range(12):
        c.ring(750 + c.rng.normal(0, 200), 780 + c.rng.normal(0, 40), c.rng.uniform(6, 14), 2.5, gap=0.0001, opacity=0.6)
    cx, cy = 900, 260
    a0 = 0.45
    c.arc(cx, cy, 70, a0, a0 + PI, 8, taper=0.15, wob=0.01)
    c.line(cx + 70 * math.cos(a0), cy + 70 * math.sin(a0), cx - 70 * math.cos(a0), cy - 70 * math.sin(a0), 5, taper=0.3)
    sx, sy = cx - 70 * math.cos(a0), cy - 70 * math.sin(a0)
    c.brush([(sx, sy), (sx - 30, sy + 120), (sx - 40, sy + 300), (sx - 44, 690)], 3, taper=0.7, opacity=0.8)
    sign(c, "C", 260, 240)


@comp(86)  # The Watch: new snow at dawn, the door open again, the book, the ring
def _(c):
    snow(c, 220, y0=60, y1=700, op=0.45)
    c.ground(y=760, w=5)
    door(c, 1080, 760, 170, 300, 8)
    c.brush([(770, 712), (720, 690), (650, 700), (660, 735), (728, 726), (770, 745)], 4, taper=0)
    c.brush([(770, 712), (820, 690), (890, 700), (880, 735), (812, 726), (770, 745)], 4, taper=0)
    c.line(770, 712, 770, 745, 3, taper=0.2)
    c.ring(560, 520, 26, 6)


def art_for(n):
    cv = Canvas(10000 * BOOK + n)
    COMP[n](cv)
    return cv.svg()


if __name__ == "__main__":
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    nums = [n for n, _, _ in CHAPTERS]
    assert nums == list(range(1, 87)), "chapter table must be 1..86"
    missing = [n for n in nums if n not in COMP]
    assert not missing, f"no composition for chapters {missing}"
    for n in nums:
        open(os.path.join(out, f"chapter_{n:02d}.svg"), "w").write(art_for(n))
    print("wrote", len(nums))
