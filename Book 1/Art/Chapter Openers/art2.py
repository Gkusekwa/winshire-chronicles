"""Chapter-opener art for the 79-chapter plan. Reuses the 41 original compositions under their new numbers
and adds 38 new ones. Odd chapters (Maren) build on the single circle; even (Calder) on three.
Usage: python3 art2.py OUTDIR"""
import math, os, sys
import numpy as np
sys.path.insert(0, "/home/claude/atlas")
import winshire_art as A
from winshire_art import Canvas, GROUND
from plan_data import C as PLAN

def boat(c, x, y, w=160):
    c.arc(x, y - 60, 110, math.pi * 0.25, math.pi * 0.75, 7, taper=0.3)
    c.line(x - 60, y - 20, x + 60, y - 20, 4, taper=0.6)

def door(c, x, base, w=160, h=300, wt=8):
    r = w / 2
    c.line(x - r, base, x - r, base - h + r, wt, taper=0.05)
    c.arc(x, base - h + r, r, math.pi, 2 * math.pi, wt, taper=0.05)
    c.line(x + r, base - h + r, x + r, base, wt, taper=0.05)
    c.disc(x + r * 0.55, base - h * 0.42, 8)

def scale_shape(c, x, y, s=90):
    c.brush([(x, y - s), (x + s * 0.7, y - s * 0.1), (x, y + s * 0.9), (x - s * 0.7, y - s * 0.1), (x, y - s)], 8, taper=0)
    for i in range(1, 4):
        c.arc(x, y + s * 0.9, s * 0.45 * i, math.pi * 1.3, math.pi * 1.7, 2.5, taper=0.5, opacity=0.6)

def tracks(c, pts, r=7, big=False):
    for (x, y) in pts:
        c.disc(x, y, r * (1.8 if big else 1))
        for dx, dy in ((-1.6, -1.6), (0, -2.3), (1.6, -1.6)):
            c.disc(x + dx * r, y + dy * r, r * (0.7 if big else 0.45))

def flames(c, x0, x1, base, n=18, hmin=120, hmax=320):
    for _ in range(n):
        x = c.rng.uniform(x0, x1)
        h = c.rng.uniform(hmin, hmax)
        c.brush([(x, base), (x + c.rng.normal(0, 20), base - h * 0.5), (x + c.rng.normal(0, 40), base - h)], c.rng.uniform(4, 10), taper=0.9)

NEW = {}
def comp(n):
    def deco(f):
        NEW[n] = f
        return f
    return deco

@comp(3)   # The Ferry
def _(c):
    c.river(y=640, band=260, n=11)
    c.line(80, 470, 1420, 470, 2.5, taper=0.1, opacity=0.7)
    boat(c, 760, 600)
    c.line(760, 520, 760, 470, 3, taper=0.1)
    c.ring(720, 545, 20, 5)
    c.brush([(1150, 760), (1260, 720), (1380, 735), (1300, 780), (1150, 760)], 10, taper=0)

@comp(4)   # The Chain
def _(c):
    c.ground()
    c.chain([(380, 420), (760, 400), (1000, 420)], 60, 7)
    c.link(1100, 440, 60, 0.4, 7)
    c.embers(750, 600, 70, 700, 120, 4)
    c.triad(1250, 230, r=9, spread=24)

@comp(8)   # Coldtarn
def _(c):
    c.ground(y=700)
    c.disc(750, 760, 230, 0.92)
    c.figure(560, 520, 200, 14, -0.06)
    c.figure(940, 520, 200, 14, 0.06)
    c.figure(750, 520, 140, 9)
    for _ in range(90):
        c.dot(750 + c.rng.normal(0, 140), 640 - abs(c.rng.normal(0, 200)), c.rng.uniform(1.5, 4), 0.6)
    c.triad(1250, 250, r=9, spread=24)

@comp(9)   # Pell's Lesson
def _(c):
    c.ground()
    c.figure(560, GROUND - 6, 260, 15)
    for i in range(3):
        c.line(600, 420 + i * 22, 660, 410 + i * 22, 6, taper=0.4)
    c.ring(1000, 480, 90, 10, gap=0.3)
    c.line(660, 430, 900, 470, 4, taper=0.8, opacity=0.6)

@comp(12)  # Harvest
def _(c):
    c.ground()
    for x in np.linspace(250, 1250, 9):
        for k in range(-3, 4):
            c.line(x + k * 6, GROUND - 6, x + k * 14, GROUND - 120 - abs(k) * 4, 3, taper=0.6)
    c.embers(750, GROUND - 120, 160, 260, 260, 5)
    c.triad(750, 220, r=10, spread=26)

@comp(15)  # Signs
def _(c):
    c.ground(y=740)
    tracks(c, [(300 + i * 160, 700 - (i % 2) * 70) for i in range(7)], r=12, big=True)
    c.ring(1260, 320, 28, 5)

@comp(16)  # The Ford
def _(c):
    c.river(y=760, band=120, n=7)
    for k in range(-5, 6):
        c.line(750 + k * 30, 560, 750 + k * 8, 300, 5, taper=0.4)
    c.embers(750, 300, 90, 180, 220, 5)
    c.brush([(100, 600), (700, 600)], 6, taper=0.6)
    c.brush([(800, 600), (1400, 600)], 6, taper=0.6)

@comp(17)  # Night on the Island
def _(c):
    c.disc(750, 480, 330, 0.95)
    c.disc(690, 440, 9, 1.0)
    c.disc(810, 440, 9, 1.0)
    c.chain([(200, 860), (520, 820), (760, 880)], 34, 4)
    c.bars(980, 1260, 700, 900, 6, w=6)
    c.ring(1320, 280, 22, 4)

@comp(22)  # Wren
def _(c):
    c.ground()
    c.ring(760, 560, 30, 6)
    c.arc(760, 640, 330, math.pi * 1.05, math.pi * 1.95, 18, taper=0.6)
    c.arc(760, 640, 380, math.pi * 1.1, math.pi * 1.6, 5, taper=0.8, opacity=0.6)
    c.triad(1260, 240, r=9, spread=24)

@comp(27)  # The Stables
def _(c):
    c.ground()
    for i, x in enumerate(np.linspace(260, 1240, 6)):
        c.arch(x, GROUND - 6, 130, 230, 6)
        c.disc(x, GROUND - 70, 14 + 4 * (i % 3))
    c.ring(750, 220, 30, 6)

@comp(28)  # Aurveth
def _(c):
    t = np.linspace(0, 4.5 * math.pi, 360)
    r = 30 + 26 * t
    c.brush(np.c_[750 + r * np.cos(t), 470 + r * np.sin(t) * 0.7], 4, taper=0.9)
    c.disc(750, 470, 46)
    c.ring(440, 300, 30, 3, gap=1.2, opacity=0.5)
    c.ring(1060, 660, 30, 3, gap=1.2, opacity=0.5)

@comp(31)  # Tam
def _(c):
    c.ground(y=760)
    c.brush([(560, 760), (600, 620), (900, 620), (940, 560), (980, 620), (940, 680), (900, 760), (560, 760)], 9, taper=0)
    c.rays(760, 560, 18, 40, 260, 3, math.pi * 1.1, math.pi * 1.9)
    c.ring(1220, 420, 30, 6)
    c.glyphs(240, 300, 420, rows=4, gap=26, w=3)

@comp(32)  # Sellswords
def _(c):
    c.ground()
    c.arc(750, GROUND, 170, math.pi, 2 * math.pi, 14, taper=0.2)
    c.triad(750, GROUND - 70, r=14, spread=36)
    for i in range(22):
        a = math.pi * (1.05 + 0.9 * i / 21)
        c.line(750 + 700 * math.cos(a), GROUND + 500 * math.sin(a) * 0.9, 750 + 260 * math.cos(a), GROUND + 200 * math.sin(a), 4, taper=0.9)

@comp(35)  # The Mentor
def _(c):
    c.ground(y=780)
    door(c, 750, 780, 220, 460, 10)
    c.figure(470, 780, 220, 12)
    c.figure(1030, 780, 180, 10, -0.04)

@comp(36)  # Gallows Quay
def _(c):
    c.ground(y=760)
    for x0 in (300, 640, 980):
        c.bars(x0, x0 + 200, 520, 760, 5, w=6, skip=(2,))
        c.line(x0, 520, x0 + 200, 520, 6, taper=0.1)
    for _ in range(30):
        c.dot(c.rng.uniform(250, 1300), c.rng.uniform(260, 480), c.rng.uniform(3, 8), 0.8)
    c.triad(1300, 640, r=10, spread=26)

@comp(38)  # The Long Road North
def _(c):
    c.ground(y=820)
    c.brush([(700, 980), (740, 600), (760, 300), (770, 120)], 6, taper=0.7)
    c.brush([(800, 980), (780, 600), (770, 300), (772, 120)], 6, taper=0.7)
    for (x, y) in ((560, 520), (980, 430), (620, 300), (900, 230)):
        c.brush([(x - 22, y + 16), (x, y - 20), (x + 22, y + 16), (x - 22, y + 16)], 4, taper=0)
    c.figure(700, 800, 120, 8)
    c.disc(800, 760, 32)
    c.triad(1250, 200, r=8, spread=22)

@comp(39)  # First Frost
def _(c):
    c.ring(750, 470, 170, 12, gap=0.2)
    c.arc(750, 470, 120, math.pi * 0.5, math.pi * 1.5, 30, taper=0.2)
    for i in range(8):
        a = i * math.pi / 4
        c.line(1200 + 30 * math.cos(a), 250 + 30 * math.sin(a), 1200 + 70 * math.cos(a), 250 + 70 * math.sin(a), 3, taper=0.6)
    c.ring(350, 780, 24, 5)

@comp(41)  # The Freeze
def _(c):
    for i in range(14):
        c.line(80, 380 + i * 28, 1420, 380 + i * 28 + c.rng.normal(0, 3), 2.5, taper=0.95, opacity=0.6)
    c.brush([(300, 520), (480, 560), (600, 500), (760, 590), (900, 530), (1100, 600)], 7, taper=0.3)
    c.ring(760, 640, 24, 5)
    c.arc(760, 1100, 420, math.pi * 1.25, math.pi * 1.75, 20, taper=0.5)

@comp(43)  # Footprints
def _(c):
    c.ground(y=780)
    for i in range(9):
        c.dot(220 + i * 80, 740 - (i % 2) * 30, 7, 0.8)
    scale_shape(c, 1050, 470, 140)

@comp(46)  # The Forbidden Verse
def _(c):
    c.glyphs(330, 230, 1170, rows=6, gap=40, w=4, mark=(5, 2))
    c.ground(y=560)
    c.ring(750, 760, 60, 6, gap=0.6, opacity=0.7)
    c.triad(1260, 820, r=9, spread=24)

@comp(47)  # Lamps
def _(c):
    c.ground(y=700)
    for i, x in enumerate(np.linspace(220, 1280, 7)):
        c.line(x, 700, x, 400, 4, taper=0.1)
        if i in (2, 5):
            c.ring(x, 380, 22, 4)
        else:
            c.disc(x, 380, 18)
            c.rays(x, 380, 10, 28, 56, 2)

@comp(50)  # Bel
def _(c):
    c.ground()
    c.figure(640, GROUND - 6, 240, 14, 0.12)
    c.chain([(700, 360), (820, 420), (960, 400)], 50, 7)
    c.ring(1150, 300, 20, 4)
    c.triad(260, 240, r=9, spread=24)

@comp(51)  # The Door
def _(c):
    c.ground(y=700)
    door(c, 750, 700, 240, 480, 11)
    c.rays(750, 820, 22, 140, 260, 3, math.pi * 0.1, math.pi * 0.9)
    c.ring(750, 560, 26, 6)

@comp(52)  # Kharrak
def _(c):
    c.ground(y=780)
    c.bars(500, 1000, 520, 780, 8, w=7, bend=3)
    flames(c, 420, 1080, 780, 26, 160, 520)
    c.triad(1290, 220, r=10, spread=26)

@comp(55)  # Thaw
def _(c):
    for _ in range(14):
        x, y = c.rng.uniform(150, 1350), c.rng.uniform(420, 820)
        w, h = c.rng.uniform(80, 180), c.rng.uniform(40, 90)
        c.brush([(x, y), (x + w, y + c.rng.normal(0, 10)), (x + w * 0.8, y + h), (x - 10, y + h * 0.9), (x, y)], 3, taper=0)
    c.ring(640, 260, 40, 7)
    c.ring(820, 260, 110, 14, gap=0.3)

@comp(56)  # Wren and the Far-Seer
def _(c):
    c.ground(y=860)
    c.arc(750, 600, 520, math.pi * 1.1, math.pi * 1.9, 14, taper=0.7)
    c.disc(750, 120, 9)
    c.river(y=930, band=40, n=3, opacity=0.6)
    c.triad(250, 780, r=8, spread=22)

@comp(57)  # Tobin
def _(c):
    c.ground()
    c.figure(750, GROUND - 6, 230, 14)
    for _ in range(60):
        x = c.rng.uniform(250, 1250)
        if abs(x - 750) < 120:
            continue
        c.dot(x, GROUND + 30 + abs(c.rng.normal(0, 50)), c.rng.uniform(4, 8), 0.8)
    for i in range(6):
        a = i * math.pi / 3
        c.dot(750 + 140 * math.cos(a), 260 + 60 * math.sin(a), 8)
    c.ring(1300, 300, 26, 5)

@comp(58)  # The Stranger
def _(c):
    c.ground()
    xs = np.linspace(220, 1280, 13)
    for i, x in enumerate(xs):
        if i == 4:
            c.ring(x, GROUND - 120, 24, 4)
        else:
            c.figure(x, GROUND - 4, 150 + c.rng.normal(0, 12), 9)
    c.triad(1250, 230, r=9, spread=24)

@comp(60)  # The Ford Again
def _(c):
    c.river(y=640, band=200, n=10)
    for x in (560, 750, 940):
        c.line(x - 40, 520, x + 40, 600, 7, taper=0.3)
        c.line(x + 40, 520, x - 40, 600, 7, taper=0.3)
    c.triad(750, 300, r=10, spread=26)

@comp(61)  # Haverly
def _(c):
    c.ground()
    c.figure(640, GROUND - 6, 230, 13)
    c.figure(860, GROUND - 6, 250, 15, 0.03)
    c.brush([(830, 280), (870, 255), (900, 280), (930, 255), (970, 280)], 6, taper=0.6)
    c.ring(640, 230, 20, 4)

@comp(64)  # The Ferry (Calder)
def _(c):
    c.river(y=600, band=240, n=10)
    c.line(80, 430, 1420, 430, 2.5, taper=0.1, opacity=0.7)
    boat(c, 760, 560)
    for dx in (-30, 0, 30):
        c.disc(760 + dx, 505, 10)
    c.figure(1260, 840, 120, 8)
    c.triad(1260, 660, r=7, spread=18)

@comp(65)  # Outcast
def _(c):
    c.ground()
    c.brush([(300, GROUND), (300, 300), (900, 300), (900, GROUND)], 10, taper=0)
    c.arch(600, GROUND, 160, 260, 8)
    c.ring(1170, GROUND - 60, 30, 6)

@comp(66)  # The Ruin
def _(c):
    c.river(y=790, band=140, n=7, opacity=0.8)
    c.ruin(750, 700, 1.3, broken=(2,))
    for _ in range(140):
        c.dot(c.rng.uniform(150, 1350), c.rng.uniform(250, 420), c.rng.uniform(2, 5), 0.8)
    c.triad(750, 600, r=8, spread=20)

@comp(67)  # Muster
def _(c):
    c.ground()
    c.brush([(1100, GROUND), (1100, 330), (1350, 330), (1350, GROUND)], 10, taper=0)
    for row in range(4):
        for i in range(14):
            x = 150 + i * 55 + row * 20
            c.line(x, GROUND - row * 40, x + 10, GROUND - 160 - row * 40, 2.5, taper=0.4)
    c.ring(1225, 420, 26, 6)

@comp(71)  # Millbrook Burns
def _(c):
    c.ground(y=760)
    c.brush([(560, 760), (600, 640), (900, 640), (940, 760)], 8, taper=0)
    flames(c, 300, 1200, 760, 20, 140, 420)
    c.figure(380, 760, 200, 12)
    c.figure(1120, 760, 200, 12, -0.05)

@comp(72)  # The Agent
def _(c):
    c.ground()
    c.brush([(650, GROUND - 10), (760, GROUND - 16), (880, GROUND - 6)], 14, taper=0.4)
    c.ring(900, GROUND - 22, 20, 5)
    for k in range(3):
        a = -math.pi / 2 + (k - 1) * 0.7
        c.disc(760 + 300 * math.cos(a), GROUND - 60 + 300 * math.sin(a), 22)

@comp(75)  # Through the Cellars
def _(c):
    x, y = 260, 260
    pts = []
    for i in range(9):
        pts += [(x, y), (x + 110, y)]
        x += 110
        y += 70
        pts.append((x, y))
    c.brush(pts, 6, taper=0.1)
    c.disc(1240, 900, 160, 0.95)
    c.ring(980, 700, 22, 5)
    c.ring(1050, 720, 60, 9, gap=0.3)
    c.brush([(300, 820), (340, 800), (370, 830)], 4, taper=0.5)

@comp(76)  # The Ruin's Lock
def _(c):
    c.ruin(750, 520, 1.4, broken=(0, 2))
    c.arc(750, 520, 330, 0, math.pi, 20, taper=0.4)
    c.disc(750, 640, 120, 0.95)
    c.triad(750, 820, r=12, spread=30)

def art_for(n):
    old = PLAN[n - 1]["old"]
    if old:
        cv = Canvas(1000 + old)
        A.COMPS[old](cv)
    else:
        cv = Canvas(2000 + n)
        NEW[n](cv)
    return cv.svg()

if __name__ == "__main__":
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    missing = [c["n"] for c in PLAN if not c["old"] and c["n"] not in NEW]
    assert not missing, missing
    for c in PLAN:
        open(os.path.join(out, f"chapter_{c['n']:02d}.svg"), "w").write(art_for(c["n"]))
    print("wrote", len(PLAN))
