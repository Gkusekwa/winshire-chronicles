"""Cover art for the three Winshire Chronicles books, in the chapter openers' ink-brush hand.

The trilogy is released in three editions, each with its own art:
    Bone   - black ink on bone, title above the art        (book1, book2, book3)
    Night  - bone ink on black, title below the art         (night1, night2, night3)
    Band   - black ink on bone under a colour title band    (band1, band2, band3)
Each cover image is a tall panel (1600 x 1760) that sits with the title on a 1600 x 2560 ebook cover.
    python3 covers.py OUTDIR   -> OUTDIR/{bone,night,band}/bookN.svg
                                  plus OUTDIR/archive/bookN_pale.svg (the first Night proofs: Bone art in bone ink)
"""
import math, os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import winshire_art as A
from winshire_art import Canvas

CW, CH = 1600, 1760


class Panel(Canvas):
    def svg(self, ink="#111111"):
        body = "\n".join(self.items).replace(f'fill="{A.INK}"', f'fill="{ink}"')
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {CW} {CH}" width="{CW}" height="{CH}">\n'
                f'{body}\n</svg>\n')


def mass(c, pts, w=10):
    """A filled ink shape from a closed outline, with a brushed edge."""
    d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts) + " Z"
    c.items.append(f'<path d="{d}" fill="{A.INK}"/>')
    c.brush(list(pts) + [pts[0]], w, taper=0)


def blob(c, cx, cy, rx, ry, n=48, jag=0.12, flat_bottom=False):
    a = np.linspace(0, 2 * math.pi, n, endpoint=False)
    r = 1 + c.noise(n, jag, 4)
    pts = [(cx + rx * q * math.cos(b), cy + ry * q * math.sin(b) * (0.35 if flat_bottom and math.sin(b) > 0 else 1)) for q, b in zip(r, a)]
    mass(c, pts, 6)


def book1(c):
    """The Watch Below: the river, the island with its broken seal, and what sleeps under the water."""
    c.river(y=1180, band=330, n=15, x0=40, x1=1560, w=3.4, amp=9)
    # the island: a low ragged mass of trees, the stump of the tower standing out of it
    blob(c, 800, 1150, 250, 70, jag=0.18, flat_bottom=True)
    for x in np.linspace(600, 1000, 11):
        c.disc(x + c.rng.normal(0, 8), 1100 - abs(c.rng.normal(0, 18)), c.rng.uniform(22, 38))
    c.brush([(780, 1110), (776, 960), (792, 945), (812, 958), (820, 1110)], 10, taper=0)
    mass(c, [(782, 1110), (778, 962), (792, 948), (810, 960), (818, 1110)], 4)
    # the seal around it, broken on the east
    c.arc(800, 1120, 360, math.pi * 1.02, math.pi * 1.86, 6, taper=0.4)
    c.arc(800, 1120, 360, math.pi * 1.96, math.pi * 2.2, 6, taper=0.6)
    # under the river: the long back of something asleep, spine ridges rising from it
    t = np.linspace(math.pi * 1.1, math.pi * 1.9, 220)
    back = np.c_[800 + 640 * np.cos(t), 1720 + 230 * np.sin(t)]
    c.brush(back, 30, taper=0.8, opacity=0.92)
    for i in range(10, 212, 14):
        x, y = back[i]
        c.brush([(x - 10, y - 8), (x, y - 44 - 10 * math.sin(i / 220 * math.pi)), (x + 10, y - 8)], 7, taper=0.4, opacity=0.8)
    # the two banks' signs: Maren's single ring west, Calder's three east
    c.ring(250, 860, 34, 7)
    c.triad(1350, 860, r=11, spread=28)
    for i in range(7):
        c.dot(110 + i * 28, 990, 5)


def book2(c):
    """The Hunt Beneath: something vast crossing the sky from the east, its road behind it; temples waking; beasts fleeing west."""
    c.ground(y=1240, x0=40, x1=1560, w=7)
    # the Titan: a great dark shape half out of the frame, high in the east
    blob(c, 1420, 380, 240, 170, jag=0.14)
    for _ in range(26):
        a = c.rng.uniform(math.pi * 0.55, math.pi * 1.45)
        c.line(1420 + 240 * math.cos(a), 380 + 170 * math.sin(a), 1420 + 300 * math.cos(a), 380 + 220 * math.sin(a), 5, taper=0.8)
    # its road: one long falling stroke back across the sky to the west horizon
    road = [(1190, 440), (900, 520), (600, 700), (330, 930), (150, 1160)]
    c.brush(road, 30, taper=0.75)
    c.brush([(x, y + 40) for x, y in road], 4, taper=0.85, opacity=0.6)
    # temples along the horizon under the road; the one it has just passed is lit
    for x, s, lit in ((210, 0.6, False), (520, 0.75, False), (880, 0.9, True), (1260, 0.65, False)):
        c.arch(x, 1240, 80 * s, 170 * s, 7, broken=(x == 210))
        if lit:
            c.rays(x, 1240 - 120 * s, 18, 70, 240, 4, a0=math.pi * 1.04, a1=math.pi * 1.96)
    # beasts streaming west across the plain below
    for _ in range(420):
        x = c.rng.uniform(80, 1520)
        y = 1300 + abs(c.rng.normal(0, 150))
        c.line(x, y, x - c.rng.uniform(16, 46), y + c.rng.normal(0, 3), c.rng.uniform(2.5, 6), taper=0.8, opacity=c.rng.uniform(0.5, 1))
    c.ring(110, 1170, 30, 6)
    c.triad(1480, 1170, r=10, spread=26)


def book3(c):
    """The Titan War: six chains going up into the light, one broken; something rising out of the sea."""
    c.rays(800, -160, 30, 300, 980, 4, a0=math.pi * 0.2, a1=math.pi * 0.8, jitter=0.01)
    c.river(y=1460, band=320, n=13, x0=30, x1=1570, w=3.4, amp=11)
    # the back of something rising out of the sea
    t = np.linspace(math.pi * 1.12, math.pi * 1.88, 120)
    top = [(800 + 640 * math.cos(a), 1700 + 150 * math.sin(a)) for a in t]
    mass(c, top, 6)
    # six chains from its back up into the light; the third is broken
    xs = np.linspace(330, 1270, 6)
    for i, x in enumerate(xs):
        ytop = 470 + abs(i - 2.5) * 80
        yb = 1700 - 150 * math.sqrt(max(0.0, 1 - ((x - 800) / 640) ** 2)) + 6
        broken = [6, 7, 8] if i == 2 else None
        c.chain([(x, yb), (x, ytop)], 52, 8, broken=broken)
    c.link(xs[2] + 34, 980, 52, 1.0, 8)
    c.ring(140, 1330, 30, 6)
    c.triad(1460, 1330, r=10, spread=26)



# ---------------- Night edition: bone ink on black ----------------

def night1(c):
    """The Watch Below, by night: one watcher on the bank, the moon on the river, the ridges just breaking the water."""
    # crescent moon high in the west
    c.arc(420, 330, 120, math.pi * 0.62, math.pi * 1.62, 34, taper=0.7)
    for _ in range(90):
        c.dot(c.rng.uniform(40, 1560), c.rng.uniform(40, 760), c.rng.uniform(1.2, 3.4), c.rng.uniform(0.3, 0.9))
    # far bank and the tower stump, small
    c.ground(y=900, x0=40, x1=1560, w=4)
    c.brush([(1090, 900), (1088, 800), (1100, 790), (1112, 800), (1114, 900)], 8, taper=0)
    for x in np.linspace(980, 1220, 8):
        c.disc(x + c.rng.normal(0, 6), 892 - abs(c.rng.normal(0, 10)), c.rng.uniform(10, 18))
    # the river and the moon's road on it
    c.river(y=1180, band=420, n=16, x0=40, x1=1560, w=2.6, amp=8, opacity=0.8)
    for i in range(16):
        y = 960 + i * 26
        hw = 60 - i * 2.5 + c.rng.normal(0, 6)
        c.line(420 - hw, y, 420 + hw, y + c.rng.normal(0, 2), 6, taper=0.7, opacity=0.95)
    # ridges just breaking the surface, mid-river
    for i in range(6):
        x = 780 + i * 64 + c.rng.normal(0, 6)
        c.brush([(x - 10, 1236), (x + 4, 1204 - 10 * math.sin(i / 5 * math.pi)), (x + 12, 1236)], 6, taper=0.4, opacity=0.6)
    # the near bank and the watcher with a lamp
    c.ground(y=1560, x0=40, x1=1560, w=8)
    c.figure(1240, 1560, h=330, w=20, lean=-0.04)
    c.line(1236, 1370, 1170, 1420, 10, taper=0.3)
    c.line(1170, 1420, 1170, 1450, 4, taper=0)
    c.disc(1170, 1470, 20)
    c.embers(1170, 1460, n=60, sx=80, sy=80, rmax=4)
    c.ring(170, 1660, 32, 7)
    c.triad(1440, 1660, r=11, spread=28)


def night2(c):
    """The Hunt Beneath, by night: the stars put out where it passes; a ruin burning; people running west."""
    # stars everywhere except inside the great shape in the east
    cx, cy, rx, ry = 1180, 540, 520, 300
    n = 0
    while n < 1400:
        x, y = c.rng.uniform(30, 1570), c.rng.uniform(30, 1150)
        d = ((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2
        if d < 1 + c.rng.normal(0, 0.06):
            continue
        c.dot(x, y, c.rng.uniform(1.0, 3.2), c.rng.uniform(0.35, 1))
        n += 1
    # its edge: a few hard strokes along the top of the dark, like spines against the sky
    for a in np.linspace(math.pi * 1.08, math.pi * 1.9, 14):
        x0, y0 = cx + rx * math.cos(a), cy + ry * math.sin(a)
        c.line(x0, y0, x0 + 26 * math.cos(a), y0 + 40 * math.sin(a), 5, taper=0.8, opacity=0.8)
    c.ground(y=1240, x0=40, x1=1560, w=7)
    # the ruin on the horizon, burning
    c.ruin(480, 1240, scale=1.6, broken=(0,))
    c.embers(480, 1080, n=260, sx=420, sy=320, rmax=7)
    # beasts streaming west below, lit from behind
    for _ in range(380):
        x = c.rng.uniform(80, 1520)
        y = 1300 + abs(c.rng.normal(0, 150))
        c.line(x, y, x - c.rng.uniform(16, 46), y + c.rng.normal(0, 3), c.rng.uniform(2.5, 6), taper=0.8, opacity=c.rng.uniform(0.4, 0.95))
    c.ring(110, 1170, 30, 6)
    c.triad(1480, 1170, r=10, spread=26)


def night3(c):
    """The Titan War, by night: two camps' fires on two shores, and between them one great broken link standing out of the sea."""
    c.rays(800, 260, 26, 140, 700, 4, a0=math.pi * 1.0, a1=math.pi * 2.0, jitter=0.01)
    c.river(y=1360, band=520, n=18, x0=30, x1=1570, w=2.8, amp=11, opacity=0.85)
    # a great chain standing out of the sea into the light; its middle link split open
    def oval(cx, cy, rx, ry, a0, a1, w, taper=0.15):
        t = np.linspace(a0, a1, 160)
        c.brush(np.c_[cx + rx * np.cos(t), cy + ry * np.sin(t)], w, taper=taper, wobble=0.6)
    oval(800, 440, 105, 220, 0, 2 * math.pi, 26, taper=0)
    oval(800, 820, 150, 260, math.pi * 0.12, math.pi * 1.88, 32)
    oval(800, 1210, 105, 220, math.pi * 1.0, math.pi * 2.0, 26)
    # camp fires on each shore
    c.ground(y=1580, x0=30, x1=560, w=6)
    c.ground(y=1580, x0=1040, x1=1570, w=6)
    for x in (120, 250, 380, 480):
        c.embers(x, 1570, n=26, sx=30, sy=60, rmax=4)
        c.disc(x, 1574, 9)
    for x in (1120, 1240, 1360, 1480):
        c.embers(x, 1570, n=26, sx=30, sy=60, rmax=4)
        c.disc(x, 1574, 9)
    c.ring(300, 1680, 30, 6)
    c.triad(1300, 1680, r=10, spread=26)


# ---------------- Band edition: close emblems under a colour band ----------------

def band1(c):
    """The Watch Below, close: the seal ring broken on the east, the bars inside it, one bent outward."""
    c.arc(800, 900, 640, math.pi * 0.08, math.pi * 1.86, 16, taper=0.3)
    c.arc(800, 900, 600, math.pi * 0.12, math.pi * 1.8, 5, taper=0.5, opacity=0.7)
    c.bars(460, 1140, 470, 1330, 9, w=12, skip=(6,))
    c.brush([(970, 470), (1000, 820), (1110, 1060), (1240, 1180)], 12, taper=0.3)
    c.line(420, 470, 1180, 470, 12, taper=0.2)
    c.line(420, 1330, 1180, 1330, 12, taper=0.2)
    # behind the bars: a long back and its ridges
    t = np.linspace(math.pi * 1.15, math.pi * 1.85, 120)
    back = np.c_[800 + 420 * np.cos(t), 1350 + 260 * np.sin(t)]
    c.brush(back, 26, taper=0.8, opacity=0.9)
    for i in range(8, 112, 12):
        x, y = back[i]
        c.brush([(x - 9, y - 6), (x, y - 40), (x + 9, y - 6)], 7, taper=0.4, opacity=0.8)
    c.river(y=1620, band=160, n=6, x0=60, x1=1540, w=3, amp=8)
    c.ring(170, 1690, 26, 6)
    c.triad(1430, 1690, r=9, spread=24)


def band2(c):
    """The Hunt Beneath, close: one temple gate, the road falling through the sky behind it, beasts pouring through."""
    # the road behind, from the top right corner down to the west
    c.brush([(1600, 60), (1200, 140), (800, 240), (420, 380), (40, 600)], 44, taper=0.7)
    # the gate: two heavy posts and a round head, lit inside
    c.line(470, 1460, 470, 760, 40, taper=0.05)
    c.line(1130, 1460, 1130, 760, 40, taper=0.05)
    c.arc(800, 760, 330, math.pi, 2 * math.pi, 40, taper=0.05)
    c.rays(800, 900, 22, 80, 300, 4, a0=math.pi * 1.06, a1=math.pi * 1.94)
    c.ground(y=1460, x0=40, x1=1560, w=8)
    # beasts streaming through it and away west
    for _ in range(360):
        x = c.rng.uniform(80, 1520)
        y = 1500 + abs(c.rng.normal(0, 110))
        c.line(x, y, x - c.rng.uniform(16, 46), y + c.rng.normal(0, 3), c.rng.uniform(2.5, 6), taper=0.8, opacity=c.rng.uniform(0.5, 1))
    for _ in range(80):
        x = c.rng.uniform(540, 1060)
        y = c.rng.uniform(1100, 1450)
        c.line(x, y, x - c.rng.uniform(16, 40), y, c.rng.uniform(2.5, 5), taper=0.8, opacity=0.8)
    c.ring(110, 1400, 30, 6)
    c.triad(1490, 1400, r=10, spread=26)


def band3(c):
    """The Titan War, close: the ring of six joined by chain, the third ring broken, Maren's and Calder's signs together at the centre."""
    R = 540
    pts = [(800 + R * math.cos(-math.pi / 2 + i * math.pi / 3), 950 + R * math.sin(-math.pi / 2 + i * math.pi / 3)) for i in range(6)]
    for i in range(6):
        a, b = pts[i], pts[(i + 1) % 6]
        mid = [(a[0] + (b[0] - a[0]) * 0.2, a[1] + (b[1] - a[1]) * 0.2), (a[0] + (b[0] - a[0]) * 0.8, a[1] + (b[1] - a[1]) * 0.8)]
        broken = [1, 2] if i in (1, 2) else None
        c.chain(mid, 46, 7, broken=broken)
    for i, (x, y) in enumerate(pts):
        if i == 2:
            c.arc(x, y, 92, math.pi * 0.35, math.pi * 1.6, 18, taper=0.5)
            c.arc(x, y, 92, math.pi * 1.8, math.pi * 2.15, 18, taper=0.7)
        else:
            c.ring(x, y, 92, 18)
    c.ring(700, 950, 70, 12)
    c.triad(920, 950, r=26, spread=70)
    c.river(y=1660, band=140, n=6, x0=60, x1=1540, w=3, amp=9)


EDITIONS = {
    "bone": {1: book1, 2: book2, 3: book3},
    "night": {1: night1, 2: night2, 3: night3},
    "band": {1: band1, 2: band2, 3: band3},
}
SEEDS = {"bone": 30000, "night": 31000, "band": 32000}
PALE = "#EDE6D6"

if __name__ == "__main__":
    out = sys.argv[1]
    for ed, books in EDITIONS.items():
        os.makedirs(os.path.join(out, ed), exist_ok=True)
        for n, f in books.items():
            c = Panel(SEEDS[ed] + n)
            f(c)
            open(os.path.join(out, ed, f"book{n}.svg"), "w").write(c.svg(PALE) if ed == "night" else c.svg())
    # the first Night proofs (Bone art in bone ink), kept
    os.makedirs(os.path.join(out, "archive"), exist_ok=True)
    for n, f in EDITIONS["bone"].items():
        c = Panel(SEEDS["bone"] + n)
        f(c)
        open(os.path.join(out, "archive", f"book{n}_pale.svg"), "w").write(c.svg(PALE))
    print("wrote", sum(len(b) for b in EDITIONS.values()) + 3)
