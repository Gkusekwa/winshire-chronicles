"""Winshire Chronicles, Book 1: abstract chapter-opening art.
Black ink brush marks, one composition per chapter. Odd chapters (Maren)
are built around the single circle; even chapters (Calder) around three.
Usage: python3 winshire_art.py OUTDIR
"""
import math, sys, os
import numpy as np

W, H = 1500, 1000
INK = "#161616"
GROUND = 640  # shared horizon line


class Canvas:
    def __init__(self, seed):
        self.rng = np.random.default_rng(seed)
        self.items = []

    # ---------- primitives ----------
    def noise(self, n, scale=1.0, smooth=6):
        r = self.rng.normal(0, 1, n + smooth * 2)
        k = np.ones(smooth) / smooth
        r = np.convolve(r, k, mode="same")[smooth:smooth + n]
        return r * scale

    def brush(self, pts, w=8, taper=0.5, wobble=1.5, opacity=1.0, rough=0.18):
        pts = np.asarray(pts, float)
        if len(pts) < 2:
            return
        # resample densely
        seg = np.sqrt(((pts[1:] - pts[:-1]) ** 2).sum(1))
        L = seg.sum()
        if L < 1:
            return
        n = max(int(L / 3), 8)
        cum = np.concatenate([[0], np.cumsum(seg)])
        t = np.linspace(0, L, n)
        x = np.interp(t, cum, pts[:, 0])
        y = np.interp(t, cum, pts[:, 1])
        # smooth
        for _ in range(2):
            x[1:-1] = (x[:-2] + 2 * x[1:-1] + x[2:]) / 4
            y[1:-1] = (y[:-2] + 2 * y[1:-1] + y[2:]) / 4
        dx, dy = np.gradient(x), np.gradient(y)
        nl = np.hypot(dx, dy) + 1e-9
        nx, ny = -dy / nl, dx / nl
        x = x + nx * self.noise(n, wobble)
        y = y + ny * self.noise(n, wobble)
        u = np.linspace(0, 1, n)
        prof = np.ones(n)
        if taper > 0:
            prof = np.clip(np.minimum(u, 1 - u) / (taper / 2 + 1e-9), 0, 1) ** 0.6
            prof = 0.15 + 0.85 * prof
        wid = w * prof * (1 + self.noise(n, rough, 10))
        wid = np.clip(wid, 0.4, None) / 2
        lx, ly = x + nx * wid, y + ny * wid
        rx, ry = x - nx * wid, y - ny * wid
        poly = list(zip(lx, ly)) + list(zip(rx[::-1], ry[::-1]))
        d = "M" + " L".join(f"{a:.1f},{b:.1f}" for a, b in poly) + " Z"
        op = f' fill-opacity="{opacity:.2f}"' if opacity < 1 else ""
        self.items.append(f'<path d="{d}" fill="{INK}"{op}/>')

    def line(self, x0, y0, x1, y1, w=6, **k):
        self.brush([(x0, y0), (x1, y1)], w, **k)

    def arc(self, cx, cy, r, a0, a1, w=6, wob=0.02, **k):
        n = max(int(abs(a1 - a0) * r / 4), 12)
        a = np.linspace(a0, a1, n)
        rr = r * (1 + self.noise(n, wob, 12))
        self.brush(np.c_[cx + rr * np.cos(a), cy + rr * np.sin(a)], w, **k)

    def ring(self, cx, cy, r, w=6, gap=0.25, start=None, **k):
        s = self.rng.uniform(0, 2 * math.pi) if start is None else start
        self.arc(cx, cy, r, s, s + 2 * math.pi - gap, w, **k)

    def dot(self, cx, cy, r, opacity=1.0):
        n = 24
        a = np.linspace(0, 2 * math.pi, n, endpoint=False)
        rr = r * (1 + self.noise(n, 0.12, 3))
        d = "M" + " L".join(f"{cx + q * math.cos(b):.1f},{cy + q * math.sin(b):.1f}" for q, b in zip(rr, a)) + " Z"
        op = f' fill-opacity="{opacity:.2f}"' if opacity < 1 else ""
        self.items.append(f'<path d="{d}" fill="{INK}"{op}/>')

    def disc(self, cx, cy, r, opacity=1.0):
        self.dot(cx, cy, r, opacity)

    def wave(self, x0, x1, y, amp=8, freq=0.01, phase=0, w=3, **k):
        xs = np.linspace(x0, x1, 120)
        ys = y + amp * np.sin(xs * freq + phase) + amp * 0.5 * np.sin(xs * freq * 2.3 + phase * 1.7)
        self.brush(np.c_[xs, ys], w, **k)

    # ---------- motifs ----------
    def river(self, y=GROUND + 120, band=150, n=9, x0=60, x1=1440, w=3, amp=7, opacity=1.0):
        for i in range(n):
            yy = y - band / 2 + band * i / max(n - 1, 1)
            a = self.rng.uniform(x0, x0 + 160)
            b = self.rng.uniform(x1 - 160, x1)
            self.wave(a, b, yy, amp, 0.008 + 0.002 * self.rng.random(), self.rng.uniform(0, 6),
                      w * self.rng.uniform(0.6, 1.2), taper=0.9, opacity=opacity)

    def ground(self, y=GROUND, x0=90, x1=1410, w=5):
        self.brush([(x0, y + self.rng.normal(0, 3)), ((x0 + x1) / 2, y), (x1, y + self.rng.normal(0, 3))], w, taper=0.8)

    def triad(self, cx, cy, r=26, spread=70, rot=-math.pi / 2, fill=True, w=5):
        out = []
        for i in range(3):
            a = rot + i * 2 * math.pi / 3
            x, y = cx + spread * math.cos(a), cy + spread * math.sin(a)
            out.append((x, y))
            if fill:
                self.disc(x, y, r)
            else:
                self.ring(x, y, r, w)
        return out

    def embers(self, cx, cy, n=60, sx=200, sy=160, rmax=6, rise=True):
        for _ in range(n):
            x = cx + self.rng.normal(0, sx / 2)
            y = cy - abs(self.rng.normal(0, sy)) if rise else cy + self.rng.normal(0, sy / 2)
            self.dot(x, y, self.rng.uniform(1.2, rmax), self.rng.uniform(0.4, 1))

    def figure(self, x, y, h=150, w=10, lean=0.0):
        self.brush([(x, y), (x + lean * h * 0.5, y - h * 0.55), (x + lean * h, y - h)], w, taper=0.5)
        self.disc(x + lean * h * 1.05, y - h - w * 1.6, w * 1.3)

    def bars(self, x0, x1, y0, y1, n, w=7, skip=(), bend=None):
        for i in range(n):
            x = x0 + (x1 - x0) * i / (n - 1)
            if i in skip:
                continue
            if bend is not None and i == bend:
                self.brush([(x, y0), (x + 30, (y0 + y1) / 2), (x + 70, y1 - 40)], w, taper=0.2)
            else:
                self.line(x, y0, x + self.rng.normal(0, 2), y1, w, taper=0.15)

    def chain(self, pts, size=34, w=5, broken=None):
        pts = np.asarray(pts, float)
        seg = np.sqrt(((pts[1:] - pts[:-1]) ** 2).sum(1))
        cum = np.concatenate([[0], np.cumsum(seg)])
        L = cum[-1]
        k = int(L / (size * 1.25))
        for i in range(k):
            if broken is not None and i in broken:
                continue
            t = (i + 0.5) * L / k
            x, y = np.interp(t, cum, pts[:, 0]), np.interp(t, cum, pts[:, 1])
            j = min(np.searchsorted(cum, t) - 1, len(pts) - 2)
            ang = math.atan2(*(pts[j + 1] - pts[j])[::-1])
            self.link(x, y, size, ang + (math.pi / 2 if i % 2 else 0), w, thin=(i % 2 == 1))

    def link(self, x, y, size, ang, w=5, thin=False):
        n = 40
        a = np.linspace(0, 2 * math.pi, n)
        rx, ry = size * 0.62, size * 0.32
        px = rx * np.cos(a)
        py = ry * np.sin(a)
        if thin:
            py *= 0.35
        c, s = math.cos(ang), math.sin(ang)
        self.brush(np.c_[x + px * c - py * s, y + px * s + py * c], w, taper=0.0, wobble=0.5)

    def arch(self, cx, base, wd, ht, w=7, broken=False):
        r = wd / 2
        self.line(cx - r, base, cx - r, base - ht + r, w, taper=0.1)
        if broken:
            self.arc(cx, base - ht + r, r, math.pi, math.pi * 1.55, w, taper=0.3)
            self.line(cx + r, base, cx + r, base - ht * 0.55, w, taper=0.3)
        else:
            self.arc(cx, base - ht + r, r, math.pi, 2 * math.pi, w, taper=0.1)
            self.line(cx + r, base - ht + r, cx + r, base, w, taper=0.1)

    def ruin(self, cx, base, scale=1.0, broken=(1,)):
        for i, dx in enumerate((-120, 0, 120)):
            self.arch(cx + dx * scale, base, 80 * scale, (190 - abs(dx) * 0.4) * scale, 7, broken=i in broken)
        self.line(cx - 190 * scale, base, cx + 190 * scale, base, 6, taper=0.4)

    def rays(self, cx, cy, n, r0, r1, w=4, a0=0, a1=2 * math.pi, jitter=0.0):
        for i in range(n):
            a = a0 + (a1 - a0) * (i + 0.5) / n + self.rng.normal(0, jitter)
            q = r1 * self.rng.uniform(0.75, 1.0)
            self.line(cx + r0 * math.cos(a), cy + r0 * math.sin(a), cx + q * math.cos(a), cy + q * math.sin(a), w, taper=0.9)

    def glyphs(self, x0, y0, x1, rows=4, gap=36, w=4, mark=None):
        for r in range(rows):
            x = x0
            y = y0 + r * gap
            k = 0
            while x < x1:
                ln = self.rng.uniform(18, 70)
                op = 1.0 if mark == (r, k) else 0.55
                ww = w * 2.2 if mark == (r, k) else w
                self.line(x, y + self.rng.normal(0, 1.5), min(x + ln, x1), y + self.rng.normal(0, 1.5), ww, taper=0.3, opacity=op)
                x += ln + self.rng.uniform(10, 26)
                k += 1

    def svg(self):
        body = "\n".join(self.items)
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">\n'
                f'{body}\n</svg>\n')


# ------------------------------------------------------------------
# Compositions. S = Maren (the one), F = Calder (the three).
# ------------------------------------------------------------------

def c01(c):  # The Unchosen Yard
    c.ground()
    for i in range(6):
        for j in range(3):
            x, y = 330 + i * 150, 240 + j * 120
            if (i, j) == (4, 2):
                continue
            c.ring(x, y, 34, 4)
            c.disc(x, y, 11)
    c.ring(930, 560 - 20, 44, 7, gap=0.5)


def c02(c):  # Across the River
    c.river(y=760, band=160)
    c.ring(750, 300, 150, 8, gap=0.15)
    for i in range(6):
        a = math.pi * (0.15 + 0.7 * i / 5)
        c.disc(750 + 230 * math.cos(a), 300 + 230 * math.sin(a) - 30, 15)
    c.triad(1220, 560, r=10, spread=26)


def c03(c):  # Roads and Roadblocks
    for k in (-1, 1):
        c.brush([(750 + k * 40, 330), (750 + k * 260, 640), (750 + k * 620, 960)], 6, taper=0.6)
    c.line(430, 560, 1070, 545, 22, taper=0.1)
    c.disc(380, 250, 14)
    c.disc(1120, 250, 14)
    c.wave(380, 1120, 250, 4, 0.02, 0, 2, taper=0.9, opacity=0.4)
    c.ring(750, 470, 30, 5)


def c04(c):  # The Uncle and the Sons
    c.ground()
    c.figure(560, GROUND - 6, 330, 22, -0.08)
    c.figure(900, GROUND - 6, 220, 13, 0.06)
    c.figure(1010, GROUND - 6, 190, 10, 0.02)
    c.triad(1250, 230, r=9, spread=24)


def c05(c):  # The Caged Beast
    c.ground(y=780)
    c.line(420, 220, 1080, 220, 10, taper=0.1)
    c.bars(440, 1060, 220, 780, 9, w=9, skip=(6,), bend=5)
    c.disc(1230, 560, 46)
    c.rays(1230, 560, 9, 70, 120, 3, math.pi * 0.6, math.pi * 1.4)
    c.ring(260, 600, 30, 5)


def c06(c):  # Whispers in the Hold
    c.ground()
    xs = np.linspace(220, 1280, 15)
    for i, x in enumerate(xs):
        if i == 10:
            c.ring(x, GROUND - 120, 22, 4)
            c.line(x, GROUND - 95, x + 6, GROUND - 4, 3, taper=0.3, opacity=0.6)
        else:
            c.figure(x + c.rng.normal(0, 4), GROUND - 4, 150 + c.rng.normal(0, 14), 9, c.rng.normal(0, 0.03))
    c.triad(750, 220, r=8, spread=22)


def c07(c):  # The Trial
    c.river(y=640, band=260, n=12)
    c.arc(1025, 700, 230, math.pi * 1.18, math.pi * 1.82, 16, taper=0.5)
    c.arc(1025, 560, 230, math.pi * 0.22, math.pi * 0.78, 6, taper=0.6, opacity=0.7)
    c.ring(1025, 400, 50, 5, gap=0.8)
    c.ring(270, 300, 30, 6)
    for i in range(14):
        t = i / 13
        c.dot(300 + t * 690, 330 + t * 150 + 30 * math.sin(t * 6), 4, 0.8)


def c08(c):  # The Younger Son
    c.ground()
    c.figure(520, GROUND - 6, 260, 16, -0.05)
    c.figure(980, GROUND - 6, 260, 16, 0.05)
    c.brush([(640, GROUND - 22), (760, GROUND - 26), (860, GROUND - 18)], 15, taper=0.4)
    c.disc(880, GROUND - 24, 18)
    for _ in range(40):
        c.dot(750 + c.rng.normal(0, 90), GROUND + 20 + abs(c.rng.normal(0, 40)), c.rng.uniform(1, 5), 0.7)


def c09(c):  # The Old Ruin
    c.river(y=760, band=140, n=8, opacity=0.8)
    c.ruin(750, 680, 1.4, broken=(2,))
    c.glyphs(590, 420, 910, rows=3, gap=30, w=3, mark=(1, 2))
    for x in (1150, 1190, 1240):
        c.line(x, 700, x + 60, 690, 3, taper=0.5)


def c10(c):  # Three Deaths
    c.ground(y=780)
    end = (1080, 650)
    for i, sx in enumerate((300, 640, 980)):
        c.brush([(sx, 130), (sx + 120 + i * 40, 380), end], 14, taper=0.7)
        c.ring(sx, 120, 26, 4, gap=1.4)
    for i in range(3):
        c.arc(end[0], end[1], 50 + i * 28, -math.pi * 0.9, -math.pi * 0.1, 4, taper=0.5)
    c.disc(*end, 18)
    c.embers(1080, 620, 50, 260, 160, 5)


def c11(c):  # The Roar
    cx, cy = 1350, 470
    for i in range(10):
        r = 90 + i * 85
        c.arc(cx, cy, r, math.pi * 0.62, math.pi * 1.38, 16 - i, taper=0.4)
    c.figure(230, 760, 210, 12)
    c.ground(y=760, x0=120, x1=520)


def c12(c):  # Three Voices
    centers = [(560, 420), (900, 380), (760, 640)]
    for k, (x, y) in enumerate(centers):
        for i in range(7):
            c.ring(x, y, 40 + i * 42, 3.2 - i * 0.25, gap=0.6 + 0.2 * k, opacity=0.85)
        c.disc(x, y, 14)


def c13(c):  # Wounded
    pts = [(80, 400), (500, 470), (900, 450), (1420, 380)]
    c.chain(pts, 46, 6, broken={9, 10})
    for _ in range(18):
        c.dot(760 + c.rng.normal(0, 30), 560 + abs(c.rng.normal(0, 120)), c.rng.uniform(2, 7), 0.85)
    c.ring(1200, 700, 55, 6, gap=0.9)


def c14(c):  # Hunted
    c.river(y=800, band=120, n=7, x0=600, x1=1440)
    cx, cy = 1050, 500
    for i in range(14):
        a = math.pi * (0.55 + 0.9 * i / 13)
        c.line(cx + 700 * math.cos(a), cy + 520 * math.sin(a) * 0.6, cx + 160 * math.cos(a), cy + 110 * math.sin(a) * 0.6, 4, taper=0.9)
    c.triad(cx + 40, cy, r=20, spread=44, fill=True)
    c.brush([(1120, 520), (1260, 640), (1380, 800)], 5, taper=0.8, opacity=0.6)


def c15(c):  # Empty-Handed
    c.arc(700, 360, 260, math.pi * 0.15, math.pi * 0.85, 18, taper=0.5)
    pts = [(860, 560), (980, 470), (1100, 420), (1240, 300), (1320, 180)]
    c.brush(pts, 3, taper=0.9, wobble=6)
    c.brush([(p[0] + 18, p[1] + 10) for p in pts], 2, taper=0.9, wobble=6, opacity=0.6)
    c.ring(700, 820, 30, 5)


def c16(c):  # Why Me?
    cx, cy = 750, 470
    t = np.linspace(0, 5.2 * math.pi, 400)
    r = 30 + 22 * t
    c.brush(np.c_[cx + r * np.cos(t), cy + r * np.sin(t) * 0.75], 4, taper=0.9)
    for k in range(3):
        a = k * 2 * math.pi / 3 + 0.5
        c.disc(cx + 300 * math.cos(a), cy + 230 * math.sin(a), 20)
    c.ring(cx, cy, 16, 4)


def c17(c):  # Disgrace
    c.ground(y=800)
    c.brush([(980, 60), (920, 400), (830, 700)], 34, taper=0.4)
    c.ring(700, 760, 30, 6)
    c.brush([(260, 60), (380, 380), (640, 700)], 2.5, taper=0.8, opacity=0.8)


def c18(c):  # The Village Burns
    c.ground(y=760)
    for i, x in enumerate(np.linspace(330, 1170, 7)):
        hh = 70 + 20 * (i % 3)
        c.brush([(x - 45, 760), (x - 45, 760 - hh), (x, 760 - hh - 45), (x + 45, 760 - hh), (x + 45, 760)], 6, taper=0.05)
    c.embers(750, 600, 140, 900, 260, 6)
    for k, x in enumerate((420, 750, 1080)):
        c.arc(x, 420, 170, math.pi * 1.1, math.pi * 1.9, 12, taper=0.6)


def c19(c):  # The Leader
    c.ground()
    c.figure(750, GROUND - 6, 260, 15)
    for i in range(3):
        c.ring(750, GROUND - 290, 60 + i * 34, 3, gap=0.3, start=math.pi * 0.5)
    for _ in range(46):
        x = c.rng.uniform(200, 1300)
        if abs(x - 750) < 140:
            continue
        c.dot(x, GROUND + 30 + abs(c.rng.normal(0, 60)), c.rng.uniform(4, 8), 0.8)


def c20(c):  # The Leader, Again
    c.ground()
    c.figure(750, GROUND - 6, 260, 15, lean=0.04)
    for i in range(3):
        c.ring(750 + 12, GROUND - 290, 60 + i * 34, 3, gap=0.3 + 0.9 * (i == 1), start=math.pi * 1.5)
    for _ in range(46):
        x = c.rng.uniform(200, 1300)
        if abs(x - 750) < 140:
            continue
        c.dot(x, GROUND + 30 + abs(c.rng.normal(0, 60)), c.rng.uniform(4, 8), 0.8)
    c.river(y=870, band=60, n=4, opacity=0.6)


def c21(c):  # Without Words
    c.ground()
    c.ring(1050, 470, 150, 12, gap=0.3)
    c.ring(380, 560, 30, 6)
    for i in range(9):
        x = 440 + i * 50
        c.dot(x, 545 - i * 6, 3.5, 0.7)


def c22(c):  # The Verse
    c.brush([(360, 220), (1140, 230), (1150, 700), (350, 690), (360, 220)], 9, taper=0)
    c.glyphs(420, 300, 1080, rows=10, gap=38, w=4, mark=(4, 3))
    c.triad(1240, 820, r=10, spread=26)


def c23(c):  # The Last Titan (legend)
    c.ground(w=6)
    for i in range(6):
        c.arc(750, 1350, 560 + i * 26, math.pi * 1.2, math.pi * 1.8, 3, taper=0.6, opacity=0.35 + 0.08 * i)
    c.figure(700, GROUND - 6, 120, 8)
    c.figure(800, GROUND - 6, 110, 8, -0.05)
    c.ring(750, 220, 24, 4, gap=1.5)


def c24(c):  # Crossing the River
    c.river(y=520, band=320, n=13, opacity=0.75)
    for i in range(16):
        t = i / 15
        c.dot(120 + t * 1100, 860 - t * 640 + 18 * (i % 2), 5)
    for i in range(16):
        t = i / 15
        c.dot(1380 - t * 1100, 200 + t * 640 + 18 * (i % 2), 5, 0.6)
    c.ring(750, 520, 24, 3, gap=2.5)


def c25(c):  # The Accusation
    c.ground(w=8)
    xs = [450, 560, 650, 750, 850, 940, 1050]
    ys = [380, 300, 360, 250, 360, 300, 380]
    c.brush(list(zip(xs, ys)) + [(1050, 470), (450, 470), (450, 380)], 9, taper=0)
    c.line(760, 255, 720, 470, 4, taper=0.2)
    for i in range(5):
        c.arc(750, GROUND + 330, 120 + i * 40, math.pi * 1.15, math.pi * 1.85, 4, taper=0.5, opacity=0.8)
    c.chain([(380, GROUND + 60), (750, GROUND + 160), (1120, GROUND + 60)], 26, 3)


def c26(c):  # The General's Silence
    c.ground(w=6)
    c.disc(750, GROUND + 380, 260, 0.9)
    for i in range(4):
        c.ring(750, GROUND + 380, 290 + i * 30, 3, gap=0.4, opacity=0.6)
    c.ring(1050, 280, 40, 10, gap=0.0001)
    c.dot(980, 300, 8)
    c.dot(1125, 300, 8)


def c27(c):  # Confession
    c.ground(y=300)
    c.line(700, 300, 690, 900, 7, taper=0.1)
    c.line(800, 300, 810, 900, 7, taper=0.1)
    for y in range(360, 860, 70):
        c.line(705, y, 805, y + 4, 3, taper=0.3, opacity=0.6)
    c.chain([(500, 900), (750, 860), (1000, 900)], 30, 4)
    c.figure(760, 290, 120, 8)
    c.figure(950, 290, 140, 9, -0.06)


def c28(c):  # The Gathering
    c.ground()
    for _ in range(520):
        x = c.rng.normal(980, 230)
        y = GROUND - abs(c.rng.normal(0, 110)) - 10
        c.dot(x, y, c.rng.uniform(1.5, 5), c.rng.uniform(0.5, 1))
    for i, x in enumerate((250, 330, 410)):
        c.brush([(x - 30, GROUND), (x - 30, GROUND - 50), (x, GROUND - 80), (x + 30, GROUND - 50), (x + 30, GROUND)], 5, taper=0.05)
    c.triad(330, 330, r=9, spread=24)


def c29(c):  # Kin
    c.ground(w=7)
    c.disc(500, GROUND - 90, 60)
    c.ring(1000, GROUND + 180, 130, 10, gap=0.3)
    c.chain([(820, GROUND + 300), (1000, GROUND + 335), (1180, GROUND + 300)], 30, 4)
    c.brush([(500, GROUND - 30), (700, GROUND + 60), (880, GROUND + 140)], 2, taper=0.6, opacity=0.6)
    c.ring(360, GROUND - 50, 18, 4)


def c30(c):  # Two Sides of a War
    c.ground()
    for k, cx in ((-1, 300), (1, 1200)):
        for _ in range(70):
            x = cx + c.rng.normal(0, 90)
            c.line(x, GROUND - 4, x - k * c.rng.uniform(20, 60), GROUND - c.rng.uniform(120, 260), 4, taper=0.5, opacity=0.85)
    c.figure(750, GROUND - 6, 150, 9)
    c.triad(750, 300, r=10, spread=26)


def c31(c):  # Orders
    for i in range(6):
        for j in range(4):
            c.line(300 + i * 110, 200 + j * 120, 380 + i * 110, 200 + j * 120, 7, taper=0.2)
    c.ring(1150, 380, 60, 8, gap=0.4)
    c.line(1070, 620, 1230, 620, 5, taper=0.6)


def c32(c):  # Before the Storm
    c.ground()
    for i in range(10):
        c.wave(100, 1400, 100 + i * 20, 10, 0.006, i, 2, taper=0.9, opacity=0.5)
    for i in range(40):
        t = c.rng.random()
        c.dot(150 + t * 450, GROUND + 40 + c.rng.normal(0, 30) + t * 30, c.rng.uniform(3, 6), 0.4 + 0.6 * (1 - t))
    c.ruin(1150, GROUND - 6, 0.8)
    c.triad(900, GROUND - 120, r=14, spread=34)


def c33(c):  # Broken Oath
    c.arc(690, 480, 200, math.pi * 0.55, math.pi * 1.45, 16, taper=0.2)
    c.arc(810, 520, 200, -math.pi * 0.45, math.pi * 0.45, 16, taper=0.2)
    for _ in range(14):
        c.dot(750 + c.rng.normal(0, 18), 500 + c.rng.normal(0, 100), c.rng.uniform(2, 6))
    c.ring(1250, 820, 26, 5)


def c34(c):  # Two Men
    c.ground()
    c.brush([(750, 150), (750, 300)], 18, taper=0.3)
    c.brush([(750, 300), (640, 470), (590, GROUND - 6)], 14, taper=0.3)
    c.brush([(750, 300), (860, 470), (910, GROUND - 6)], 14, taper=0.3)
    c.disc(750, 120, 24)
    c.triad(260, 520, r=8, spread=20)


def c35(c):  # War
    c.river(y=720, band=180, n=9)
    for _ in range(46):
        x, y = c.rng.uniform(150, 1350), c.rng.uniform(150, 760)
        a = c.rng.uniform(-0.9, -0.3) if c.rng.random() < 0.5 else c.rng.uniform(0.3, 0.9) + math.pi
        ln = c.rng.uniform(80, 260)
        c.line(x, y, x + ln * math.cos(a), y + ln * math.sin(a), c.rng.uniform(4, 14), taper=0.8)
    c.ring(750, 420, 32, 7)


def c36(c):  # The Second Lock
    c.ring(250, 600, 70, 10, gap=0.0001)
    c.disc(250, 600, 18)
    c.ring(1250, 600, 70, 10, gap=0.0001)
    c.disc(1250, 600, 18)
    c.wave(330, 1170, 600, 6, 0.01, 0, 2, taper=0.2, opacity=0.6)
    c.brush([(680, 300), (720, 270), (750, 300), (780, 270), (820, 300)], 7, taper=0.6)
    for i in range(6):
        c.dot(680 - i * 60, 320 + i * 30, 3, 0.6)


def c37(c):  # The Sacrifice
    c.ring(650, 480, 210, 14, gap=0.2)
    c.ring(850, 480, 210, 14, gap=0.2)
    c.disc(750, 480, 30)
    c.chain([(140, 860), (420, 830)], 32, 4)
    c.chain([(1080, 830), (1360, 860)], 32, 4)


def c38(c):  # Fire at the Ruin
    c.ground(y=740)
    c.ruin(750, 740, 1.5, broken=(0, 2))
    for i in range(22):
        x = c.rng.uniform(450, 1050)
        c.brush([(x, 740), (x + c.rng.normal(0, 20), 600), (x + c.rng.normal(0, 40), 380 + c.rng.uniform(0, 160))], c.rng.uniform(4, 9), taper=0.9)
    for k, x in enumerate((420, 750, 1080)):
        c.arc(x, 300, 150, math.pi * 1.1, math.pi * 1.9, 12, taper=0.6)


def c39(c):  # The Lock Gives Way
    c.arc(750, 480, 170, math.pi * 0.6, math.pi * 1.9, 20, taper=0.3)
    c.rays(750, 480, 26, 200, 520, 4)
    c.brush([(560, 820), (760, 830), (930, 815)], 15, taper=0.5)
    c.disc(950, 815, 17)
    c.disc(750, 480, 30)


def c40(c):  # Underground
    c.brush([(60, 380), (1440, 380)], 4, taper=0.95, opacity=0.6)
    c.brush([(60, 680), (1440, 680)], 4, taper=0.95, opacity=0.6)
    c.brush([(100, 540), (400, 520), (690, 530)], 9, taper=0.3)
    c.brush([(1400, 520), (1100, 545), (810, 530)], 9, taper=0.3)
    c.ring(700, 530, 18, 5)
    c.triad(810, 530, r=7, spread=17, rot=0)
    for _ in range(60):
        c.dot(c.rng.uniform(80, 1420), 380 - abs(c.rng.normal(0, 60)), c.rng.uniform(1, 4), 0.5)


def c41(c):  # The Last Titan
    c.chain([(80, 880), (520, 820)], 40, 5, broken={4})
    c.chain([(980, 820), (1420, 880)], 40, 5, broken={0})
    for k in range(-3, 4):
        c.line(750 + k * 26, 420 + abs(k) * 25, 750 + k * 60, 690 - abs(k) * 30, 3, taper=0.9, opacity=0.55)
    for k in (-1, 1):
        c.brush([(750, 260), (750 + k * 300, 80), (750 + k * 700, 40)], 22, taper=0.8)
    c.disc(750, 300, 50)
    c.ring(700, 760, 13, 4)
    c.triad(800, 762, r=6, spread=14)


COMPS = {i: globals()[f"c{i:02d}"] for i in range(1, 42)}

if __name__ == "__main__":
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    for i, f in COMPS.items():
        c = Canvas(1000 + i)
        f(c)
        open(os.path.join(out, f"chapter_{i:02d}.svg"), "w").write(c.svg())
    print("wrote", len(COMPS))
