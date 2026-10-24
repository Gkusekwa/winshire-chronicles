"""Draw Winshire maps from world.py.
render(view, style, secrets) -> svg string
  view: "realm" or "marches"; style: "color" or "ink"; secrets: include temples and catacombs
"""
import math, random, re
import numpy as np
import world as Wd
import marches_items as MI

FONT = "'IM Fell English', 'IM FELL English', Georgia, serif"
FONT_SC = "'IM Fell English SC', 'IM FELL English SC', Georgia, serif"

VIEWS = {
    "realm":   dict(x0=-14, y0=-12, x1=334, y1=230, s=4.6),
    "marches": dict(x0=165, y0=84, x1=193, y1=124, s=30.0),
}

PAL = {
    "color": dict(sea="#c9d6d2", sea2="#b4c6c2", land="#efe4c8", ink="#3b2f22", water="#6f8f94",
                  wfill="#b9cfcd", mount="#5a4733", forest="#5f6f45", forestfill="#cfd3a6",
                  road="#8a5a34", border="#8b2f2f", label="#2c231a", secret="#a3262b", marsh="#6f8f94",
                  kingdomlabel="#6b5536", plain="#b49a63"),
    "ink":   dict(sea="#ffffff", sea2="#ffffff", land="#ffffff", ink="#111111", water="#111111",
                  wfill="#ffffff", mount="#111111", forest="#111111", forestfill="#ffffff",
                  road="#111111", border="#111111", label="#111111", secret="#111111", marsh="#111111",
                  kingdomlabel="#333333", plain="#555555"),
}


class Map:
    def __init__(self, view, style, secrets, seed=7, chapter=None, interactive=False, subtitle=None, bare=False):
        self.bare = bare
        self.chapter, self.interactive, self.subtitle = chapter, interactive, subtitle
        self.prog = (chapter is not None) or (interactive and view == "marches") or (interactive and view == "realm")
        self.fs = (1.25 if view == "marches" else 1.7) if chapter is not None else 1.0
        self.v = VIEWS[view]
        self.view, self.style, self.secrets = view, style, secrets
        self.c = PAL[style]
        self.rng = random.Random(seed)
        self.np = np.random.default_rng(seed)
        self.out = []
        v = self.v
        self.W = (v["x1"] - v["x0"]) * v["s"]
        self.H = (v["y1"] - v["y0"]) * v["s"]

    # coordinates
    def P(self, x, y):
        v = self.v
        return ((x - v["x0"]) * v["s"], (y - v["y0"]) * v["s"])

    def inside(self, x, y, pad=0):
        v = self.v
        return v["x0"] - pad <= x <= v["x1"] + pad and v["y0"] - pad <= y <= v["y1"] + pad

    # fractal subdivision for natural lines
    def roughen(self, pts, rough=0.25, depth=5, closed=False):
        pts = [tuple(p) for p in pts]
        if closed:
            pts = pts + [pts[0]]
        for d in range(depth):
            new = [pts[0]]
            for a, b in zip(pts[:-1], pts[1:]):
                mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
                L = math.hypot(b[0] - a[0], b[1] - a[1])
                nx, ny = -(b[1] - a[1]), b[0] - a[0]
                n = math.hypot(nx, ny) or 1
                off = self.rng.gauss(0, rough * L * 0.5)
                new += [(mx + nx / n * off, my + ny / n * off), b]
            pts = new
            rough *= 0.62
        return pts

    def smooth_path(self, pts, closed=False):
        sp = [self.P(*p) for p in pts]
        d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in sp)
        return d + (" Z" if closed else "")

    def G(self, ch, s, new_xy=None):
        """Gate content by the chapter it first appears in (Marches progression)."""
        if not self.prog:
            return s
        if self.interactive:
            ring = ""
            if new_xy:
                X, Y = new_xy
                ring = f'<circle class="newring" cx="{X:.1f}" cy="{Y:.1f}" r="20" fill="none" stroke="{self.c["secret"]}" stroke-width="2" stroke-dasharray="4 3"/>'
            return f'<g class="rv" data-ch="{ch}">{ring}{s}</g>'
        if ch > self.chapter:
            return ""
        if new_xy and ch == self.chapter and ch > 0:
            X, Y = new_xy
            s = f'<circle cx="{X:.1f}" cy="{Y:.1f}" r="22" fill="none" stroke="{self.c["secret"]}" stroke-width="2.2" stroke-dasharray="5 3"/>' + s
        return s

    def add(self, s):
        if not s:
            return
        # cairo ignores paint-order; emit a halo copy under any haloed text
        if '<text' in s and 'paint-order="stroke"' in s:
            def dup(m):
                t = m.group(0)
                halo = t.replace('paint-order="stroke"', '')
                halo = re.sub(r' fill="[^"]*"', ' fill="none"', halo, count=1)
                plain = re.sub(r' stroke="[^"]*" stroke-width="[^"]*" paint-order="stroke"', '', t)
                return halo + plain
            s = re.sub(r'<text[^>]*paint-order="stroke"[^>]*>[^<]*</text>', dup, s)
        self.out.append(s)

    # ---------------- layers ----------------
    def sea(self):
        c = self.c
        self.add(f'<rect width="{self.W:.0f}" height="{self.H:.0f}" fill="{c["sea"]}"/>')

    def land(self):
        c = self.c
        self.coast = self.roughen(Wd.COAST, 0.35, 6, closed=True)
        d = self.smooth_path(self.coast, True)
        # coastal ripple lines
        for i, w in enumerate((14, 9, 5)):
            op = 0.10 + 0.08 * i
            self.add(f'<path d="{d}" fill="none" stroke="{c["water"]}" stroke-width="{w * self.v["s"] / 5:.1f}" stroke-opacity="{op:.2f}" stroke-linejoin="round"/>')
        self.add(f'<path d="{d}" fill="{c["land"]}" stroke="{c["ink"]}" stroke-width="{1.6 if self.view == "realm" else 2.2}" stroke-linejoin="round"/>')
        for isl in Wd.ISLANDS:
            r = self.roughen(isl, 0.3, 4, closed=True)
            self.add(f'<path d="{self.smooth_path(r, True)}" fill="{c["land"]}" stroke="{c["ink"]}" stroke-width="1.4"/>')

    def plains(self):
        c = self.c
        for name, poly in Wd.PLAINS.items():
            xs = [p[0] for p in poly]; ys = [p[1] for p in poly]
            for _ in range(int((max(xs) - min(xs)) * (max(ys) - min(ys)) / 9)):
                x = self.rng.uniform(min(xs), max(xs)); y = self.rng.uniform(min(ys), max(ys))
                if not point_in(poly, x, y) or not self.inside(x, y):
                    continue
                X, Y = self.P(x, y)
                self.add(f'<path d="M{X-3:.1f},{Y:.1f} l2,-3 M{X:.1f},{Y:.1f} l0,-4 M{X+3:.1f},{Y:.1f} l-2,-3" stroke="{c["plain"]}" stroke-width="0.8" fill="none"/>')

    def marshes(self):
        c = self.c
        sc = self.v["s"]
        for name, poly in Wd.MARSHES.items():
            xs = [p[0] for p in poly]; ys = [p[1] for p in poly]
            step = 2.2 if self.view == "realm" else 0.55
            y = min(ys)
            while y < max(ys):
                x = min(xs)
                while x < max(xs):
                    xx = x + self.rng.uniform(-step / 3, step / 3)
                    yy = y + self.rng.uniform(-step / 3, step / 3)
                    if point_in(poly, xx, yy) and self.inside(xx, yy):
                        X, Y = self.P(xx, yy)
                        L = 5 if self.view == "realm" else 9
                        self.add(f'<path d="M{X-L/2:.1f},{Y:.1f} h{L}" stroke="{c["marsh"]}" stroke-width="0.9"/>'
                                 f'<path d="M{X:.1f},{Y:.1f} v-{L*0.5:.1f}" stroke="{c["marsh"]}" stroke-width="0.7"/>')
                    x += step
                y += step

    def water(self):
        c = self.c
        sc = self.v["s"]
        k = sc / 5
        def river(pts, w0, w1):
            r = self.roughen(pts, 0.18, 4)
            n = len(r)
            # draw in segments with widening stroke
            seg = max(n // 12, 2)
            for i in range(0, n - 1, seg):
                part = r[i:i + seg + 1]
                w = w0 + (w1 - w0) * i / n
                self.add(f'<path d="{self.smooth_path(part)}" fill="none" stroke="{c["water"]}" stroke-width="{w:.2f}" stroke-linecap="round" stroke-linejoin="round"/>')
                if self.style == "ink" and w > 3:
                    inner.append((part, w - 2.4))
        inner = []
        wend_w = (1.2, 4.0) if self.view == "realm" else (8, 12)
        river(Wd.WEND, *wend_w)
        for name, pts in Wd.RIVERS.items():
            if self.view == "realm":
                river(pts, 0.8, 2.4)
            else:
                river(pts, 3, 5)
        for part, w in inner:
            self.add(f'<path d="{self.smooth_path(part)}" fill="none" stroke="#ffffff" stroke-width="{w:.2f}" stroke-linecap="round" stroke-linejoin="round"/>')
        for name, ((x, y), rx, ry) in Wd.LAKES.items():
            pts = [(x + rx * math.cos(a), y + ry * math.sin(a)) for a in np.linspace(0, 2 * math.pi, 14, endpoint=False)]
            r = self.roughen(pts, 0.25, 4, closed=True)
            self.add(f'<path d="{self.smooth_path(r, True)}" fill="{c["wfill"]}" stroke="{c["water"]}" stroke-width="{1.2 * max(1, k / 2):.1f}"/>')
        if self.view == "marches":
            # the river splits around the Old Ruin's island
            west = [(176.6, 101.6), (175.3, 102.2), (174.8, 103.6), (175.0, 104.9), (175.4, 105.6)]
            east = [(176.6, 101.6), (176.9, 102.6), (176.8, 104.2), (176.2, 105.2), (175.4, 105.6)]
            isl = [(176.2, 102.2), (176.4, 103.4), (176.1, 104.6), (175.5, 104.9), (175.3, 103.8), (175.6, 102.6)]
            for ch in (west, east):
                rr = self.roughen(ch, 0.1, 3)
                self.add(f'<path d="{self.smooth_path(rr)}" fill="none" stroke="{c["water"]}" stroke-width="9" stroke-linecap="round"/>')
                if self.style == "ink":
                    self.add(f'<path d="{self.smooth_path(rr)}" fill="none" stroke="#ffffff" stroke-width="6.6" stroke-linecap="round"/>')
            ri = self.roughen(isl, 0.12, 3, closed=True)
            self.add(f'<path d="{self.smooth_path(ri, True)}" fill="{c["land"]}" stroke="{c["ink"]}" stroke-width="1.2"/>')
            for (x, y) in ((175.7, 103.0), (175.9, 104.2), (175.6, 104.5)):
                X, Y = self.P(x, y)
                self.add(f'<circle cx="{X:.1f}" cy="{Y:.1f}" r="5" fill="{c["forestfill"]}" stroke="{c["forest"]}" stroke-width="0.8"/>')

    def mountains(self):
        c = self.c
        sc = self.v["s"]
        for name, (line, hw, dens) in Wd.MOUNTAINS.items():
            line = np.array(line, float)
            seg = np.sqrt(((line[1:] - line[:-1]) ** 2).sum(1)); cum = np.r_[0, np.cumsum(seg)]
            spacing = 2.0 if self.view == "realm" else 0.9
            n = int(cum[-1] * dens / spacing * (hw / 3.5))
            pts = []
            for _ in range(n):
                t = self.rng.uniform(0, cum[-1])
                x = np.interp(t, cum, line[:, 0]); y = np.interp(t, cum, line[:, 1])
                off = self.rng.gauss(0, hw / 2)
                pts.append((x + self.rng.uniform(-1, 1), y + off))
            pts.sort(key=lambda p: p[1])
            for x, y in pts:
                if not self.inside(x, y, 2) or not point_in(Wd.COAST, x, y):
                    continue
                X, Y = self.P(x, y)
                h = (self.rng.uniform(11, 19) if self.view == "realm" else self.rng.uniform(22, 34)) * (1.25 if name == "The Worldsend" else 1)
                if name == "Sunward Hills" or (self.view == "marches" and name == "The Scarfell"):
                    h *= 0.6
                w = h * self.rng.uniform(0.9, 1.3)
                pk = X + self.rng.uniform(-w * 0.15, w * 0.15)
                self.add(f'<path d="M{X-w/2:.1f},{Y:.1f} L{pk:.1f},{Y-h:.1f} L{X+w/2:.1f},{Y:.1f} Z" fill="{c["land"]}" stroke="none"/>'
                         f'<path d="M{X-w/2:.1f},{Y:.1f} L{pk:.1f},{Y-h:.1f} L{X+w/2:.1f},{Y:.1f}" fill="none" stroke="{c["mount"]}" stroke-width="1.1" stroke-linejoin="round"/>'
                         f'<path d="M{pk:.1f},{Y-h:.1f} L{X+w*0.12:.1f},{Y-h*0.35:.1f} M{pk+w*0.12:.1f},{Y-h*0.7:.1f} l{w*0.14:.1f},{h*0.18:.1f} M{pk+w*0.2:.1f},{Y-h*0.45:.1f} l{w*0.12:.1f},{h*0.16:.1f}" fill="none" stroke="{c["mount"]}" stroke-width="0.7"/>')

    def forests(self):
        c = self.c
        for name, poly in Wd.FORESTS.items():
            xs = [p[0] for p in poly]; ys = [p[1] for p in poly]
            step = 2.6 if self.view == "realm" else 0.6
            trees = []
            y = min(ys)
            while y < max(ys):
                x = min(xs)
                while x < max(xs):
                    xx = x + self.rng.uniform(-step / 2, step / 2)
                    yy = y + self.rng.uniform(-step / 2, step / 2)
                    if point_in(poly, xx, yy) and self.inside(xx, yy, 1):
                        trees.append((xx, yy))
                    x += step
                y += step
            trees.sort(key=lambda p: p[1])
            r = 4.2 if self.view == "realm" else 8
            for xx, yy in trees:
                X, Y = self.P(xx, yy)
                rr = r * self.rng.uniform(0.8, 1.2)
                self.add(f'<path d="M{X:.1f},{Y+rr*1.1:.1f} v{rr*0.7:.1f}" stroke="{c["forest"]}" stroke-width="0.9"/>'
                         f'<circle cx="{X:.1f}" cy="{Y:.1f}" r="{rr:.1f}" fill="{c["forestfill"]}" stroke="{c["forest"]}" stroke-width="0.9"/>')

    def borders(self):
        c = self.c
        for line in Wd.BORDERS:
            r = self.roughen(line, 0.15, 3)
            self.add(self.G(MI.BORDER_REVEAL, f'<path d="{self.smooth_path(r)}" fill="none" stroke="{c["border"]}" stroke-width="{1.4 if self.view == "realm" else 2.5}" stroke-dasharray="6 3 1.5 3" stroke-opacity="0.7"/>'))

    def roads(self):
        c = self.c
        for name, line in Wd.ROADS.items():
            r = self.roughen(line, 0.08, 3)
            rch = MI.ROAD_REVEAL.get(name, 1) if self.view == "marches" else MI.REALM_ROAD_REVEAL.get(name, MI.LATER)
            self.add(self.G(rch, f'<path d="{self.smooth_path(r)}" fill="none" stroke="{c["road"]}" stroke-width="{1.2 if self.view == "realm" else 2.6}" stroke-dasharray="{"4 3" if self.view == "realm" else "9 5"}"/>'))
        r = self.roughen(Wd.ONEROAD, 0.06, 3)
        self.add(self.G(MI.ROAD_REVEAL["ONEROAD"], f'<path d="{self.smooth_path(r)}" fill="none" stroke="{c["ink"]}" stroke-width="{1.0 if self.view == "realm" else 2.2}" stroke-dasharray="1 4" stroke-linecap="round" stroke-opacity="0.75"/>'))
        if self.view == "marches":
            for (a, b, name) in Wd.FERRIES:
                A, B = self.P(*a), self.P(*b)
                self.add(self.G(1, f'<path d="M{A[0]:.1f},{A[1]:.1f} L{B[0]:.1f},{B[1]:.1f}" stroke="{c["ink"]}" stroke-width="1.6" stroke-dasharray="3 3"/>'))
            # field strips around Harrow's End and farms
            for (cx, cy, n, fch) in ((179.4, 101.6, 9, 2), (181.4, 99.6, 7, 2), (171.0, 110.6, 6, 1), (171.6, 104.0, 5, 1), (170.6, 97.0, 5, 3), (182.6, 104.4, 5, 2), (171.0, 117.6, 6, 5)):
                fields = []
                for i in range(n):
                    x = cx + self.rng.uniform(-1.4, 1.4); y = cy + self.rng.uniform(-1.2, 1.2)
                    X, Y = self.P(x, y)
                    w, h = self.rng.uniform(18, 34), self.rng.uniform(10, 18)
                    rot = self.rng.uniform(-30, 30)
                    fields.append(f'<rect x="{X-w/2:.1f}" y="{Y-h/2:.1f}" width="{w:.1f}" height="{h:.1f}" fill="none" stroke="{c["plain"]}" stroke-width="0.8" transform="rotate({rot:.0f} {X:.1f} {Y:.1f})"/>'
                              + "".join(f'<path d="M{X-w/2+k*w/5:.1f},{Y-h/2:.1f} v{h:.1f}" stroke="{c["plain"]}" stroke-width="0.4" transform="rotate({rot:.0f} {X:.1f} {Y:.1f})"/>' for k in range(1, 5)))
                self.add(self.G(fch, "".join(fields)))

    def secrets_layer(self):
        c = self.c
        if self.prog:
            r = self.roughen(Wd.CATACOMBS, 0.05, 3)
            self.add(self.G(27, f'<path d="{self.smooth_path(r)}" fill="none" stroke="{c["secret"]}" stroke-width="5" stroke-opacity="0.35" stroke-linecap="round"/>'
                     f'<path d="{self.smooth_path(r)}" fill="none" stroke="{c["secret"]}" stroke-width="1.6" stroke-dasharray="2 4"/>'))
            return
        if not self.secrets:
            return
        if self.view == "marches":
            r = self.roughen(Wd.CATACOMBS, 0.05, 3)
            self.add(f'<g class="secret"><path d="{self.smooth_path(r)}" fill="none" stroke="{c["secret"]}" stroke-width="5" stroke-opacity="0.35" stroke-linecap="round"/>'
                     f'<path d="{self.smooth_path(r)}" fill="none" stroke="{c["secret"]}" stroke-width="1.6" stroke-dasharray="2 4"/></g>')

    # ---------------- symbols ----------------
    def glyph(self, p):
        c = self.c
        X, Y = self.P(p["x"], p["y"])
        k = 1 if self.view == "realm" else 2
        ink = c["secret"] if p["secret"] else c["ink"]
        kind = p["kind"]
        g = []
        if kind == "capital":
            g.append(f'<circle cx="{X:.1f}" cy="{Y:.1f}" r="{5*k}" fill="{c["land"]}" stroke="{ink}" stroke-width="1.6"/><circle cx="{X:.1f}" cy="{Y:.1f}" r="{2.2*k}" fill="{ink}"/>')
        elif kind == "city":
            g.append(f'<circle cx="{X:.1f}" cy="{Y:.1f}" r="{3.8*k}" fill="{ink}" stroke="{c["land"]}" stroke-width="1"/>')
        elif kind in ("town", "village"):
            r = (2.8 if kind == "town" else 2.2) * k
            g.append(f'<circle cx="{X:.1f}" cy="{Y:.1f}" r="{r}" fill="{c["land"]}" stroke="{ink}" stroke-width="1.4"/>')
        elif kind in ("fortress", "hold"):
            s = 4.2 * k
            g.append(f'<path d="M{X-s:.1f},{Y+s*0.7:.1f} v{-s*1.3:.1f} h{s*0.5:.1f} v{s*0.4:.1f} h{s*0.5:.1f} v{-s*0.4:.1f} h{s*0.5:.1f} v{s*0.4:.1f} h{s*0.5:.1f} v{-s*0.4:.1f} h{s*0.5:.1f} v{s*0.4:.1f} h{s*0.5:.1f} v{-s*0.4:.1f} v{s*1.3:.1f} Z" fill="{c["land"]}" stroke="{ink}" stroke-width="1.4"/>')
        elif kind == "tower":
            s = 3 * k
            g.append(f'<path d="M{X-s*0.5:.1f},{Y+s:.1f} v{-s*1.8:.1f} h{s:.1f} v{s*1.8:.1f} Z" fill="{c["land"]}" stroke="{ink}" stroke-width="1.3"/>')
        elif kind == "ruin":
            s = 4 * k
            g.append(f'<path d="M{X-s:.1f},{Y+s*0.6:.1f} v{-s:.1f} a{s*0.45:.1f},{s*0.45:.1f} 0 0 1 {s*0.9:.1f},0 v{s*0.4:.1f} M{X+s*0.3:.1f},{Y+s*0.6:.1f} v{-s*0.7:.1f} a{s*0.35:.1f},{s*0.35:.1f} 0 0 1 {s*0.7:.1f},0" fill="none" stroke="{ink}" stroke-width="1.5"/>')
        elif kind == "farm":
            s = 3 * k
            g.append(f'<path d="M{X-s:.1f},{Y+s*0.5:.1f} v{-s*0.8:.1f} l{s:.1f},{-s*0.7:.1f} l{s:.1f},{s*0.7:.1f} v{s*0.8:.1f} Z" fill="{c["land"]}" stroke="{ink}" stroke-width="1.3"/>')
        elif kind == "temple":
            s = 4.4 * k
            g.append(f'<circle cx="{X:.1f}" cy="{Y:.1f}" r="{s:.1f}" fill="none" stroke="{ink}" stroke-width="1.4"/>'
                     f'<path d="M{X:.1f},{Y-s*1.6:.1f} v{s*3.2:.1f} M{X-s*1.6:.1f},{Y:.1f} h{s*3.2:.1f}" stroke="{ink}" stroke-width="1"/>'
                     f'<circle cx="{X:.1f}" cy="{Y:.1f}" r="{s*0.35:.1f}" fill="{ink}"/>')
        else:  # landmark: small diamond only on marches view
            return ""
        return "".join(g)

    def places(self, interactive=False):
        c = self.c
        for p in Wd.P:
            if p["secret"] and not self.secrets and not (self.prog and p["id"] == "catacombs"):
                continue
            if self.prog and p["id"] == "catacombs":
                continue  # drawn as the catacomb line and label instead
            if self.view == "realm" and (p["scope"] == "marches" or p["id"] in REALM_HIDE):
                continue
            if self.view == "marches" and p["scope"] == "realm":
                continue
            if not self.inside(p["x"], p["y"]):
                continue
            X, Y = self.P(p["x"], p["y"])
            gl = self.glyph(p)
            if self.view == "realm" and p["id"] in REALM_LABEL:
                p = dict(p, ldx=REALM_LABEL[p["id"]][0], ldy=REALM_LABEL[p["id"]][1])
            elif self.view == "realm":
                p = dict(p, ldx=p["ldx"] if p["kind"] == "landmark" else 0, ldy=p["ldy"] if p["kind"] == "landmark" else 0)
            k = self.fs if self.view == "realm" else 1.9 * self.fs
            size = {"capital": 15, "city": 12.5, "town": 11, "village": 10, "fortress": 12, "hold": 12,
                    "ruin": 11.5, "temple": 10.5, "tower": 9.5, "farm": 9.5, "landmark": 12}[p["kind"]] * k
            ital = p["kind"] in ("landmark",)
            col = c["secret"] if p["secret"] else c["label"]
            if p["kind"] == "landmark":
                # area labels: centred, italic, letterspaced
                lx, ly = X + p["ldx"] * self.v["s"], Y + p["ldy"] * self.v["s"]
                label = (f'<text x="{lx:.1f}" y="{ly:.1f}" font-family="{FONT}" font-style="italic" font-size="{size:.1f}" '
                         f'text-anchor="middle" fill="{col}" letter-spacing="0.5" stroke="{c["land"]}" stroke-width="3" paint-order="stroke">{p["name"]}</text>')
            else:
                anchor = "start"
                lx = X + (7 * k) + p["ldx"] * self.v["s"]
                ly = Y + size * 0.35 + p["ldy"] * self.v["s"]
                if p["ldx"] < 0:
                    anchor = "end"; lx = X - 7 * k + (p["ldx"] + 1) * self.v["s"]
                fam = FONT_SC if p["kind"] == "capital" else FONT
                label = (f'<text x="{lx:.1f}" y="{ly:.1f}" font-family="{fam}" font-size="{size:.1f}" text-anchor="{anchor}" '
                         f'fill="{col}" stroke="{c["land"]}" stroke-width="3" paint-order="stroke">{p["name"]}</text>')
            hit = (f'<circle cx="{X:.1f}" cy="{Y:.1f}" r="{12*k:.0f}" fill="transparent"/>' if interactive else "")
            attrs = f' class="place{" secret" if p["secret"] else ""}" data-id="{p["id"]}" tabindex="0" role="button" aria-label="{p["name"]}"' if interactive else ""
            body = f'<g{attrs}>{hit}{gl}{label}</g>'
            if self.view == "marches":
                body = self.G(MI.REVEAL.get(p["id"], 1), body, (X, Y))
            else:
                body = self.G(MI.LATER if p["secret"] else MI.REALM_REVEAL.get(p["id"], MI.LATER), body, (X, Y))
            self.add(body)

    def labels(self):
        c = self.c
        v = self.v
        if self.view == "realm":
            for kid, k in Wd.KINGDOMS.items():
                X, Y = self.P(*k["label"])
                self.add(self.G(MI.KINGDOM_REVEAL.get(kid, MI.LATER), f'<text x="{X:.1f}" y="{Y:.1f}" font-family="{FONT_SC}" font-size="{26*min(self.fs, 1.35):.1f}" letter-spacing="7" text-anchor="middle" fill="{c["kingdomlabel"]}" fill-opacity="0.85" stroke="{c["land"]}" stroke-width="4" paint-order="stroke">{k["name"].upper()}</text>'))
            for name, (x, y) in Wd.SEAS.items():
                X, Y = self.P(x, y)
                rot = -90 if x < 10 else 0
                self.add(self.G(MI.REALM_LABEL_REVEAL.get(name, MI.LATER), f'<text x="{X:.1f}" y="{Y:.1f}" font-family="{FONT}" font-style="italic" font-size="{19*min(self.fs,1.4):.1f}" letter-spacing="5" text-anchor="middle" fill="{c["water"]}" transform="rotate({rot} {X:.1f} {Y:.1f})">{name}</text>'))
            # range and region names
            for name, (x, y, rot) in {"The Iron Fells": (114, 33, 55), "The High Crown": (70, 16, 0),
                                       "The Scarfell": (204, 82, 55), "Sunward Hills": (76, 112, 25)}.items():
                X, Y = self.P(x, y)
                self.add(self.G(MI.REALM_LABEL_REVEAL.get(name, MI.LATER), f'<text x="{X:.1f}" y="{Y:.1f}" font-family="{FONT}" font-style="italic" font-size="{12*self.fs:.1f}" letter-spacing="2" text-anchor="middle" fill="{c["mount"]}" stroke="{c["land"]}" stroke-width="3" paint-order="stroke" transform="rotate({rot} {X:.1f} {Y:.1f})">{name}</text>'))
            for name, (x, y) in {"The Greenwold": (152, 82), "Elderwood": (48, 116), "The Ashlings": (210, 128),
                                  "The Hallow Plains": (272, 132), "The Candle Downs": (136, 172), "The Saltings": (232, 186)}.items():
                if name in ("The Hallow Plains", "The Candle Downs", "The Saltings"):
                    continue  # placed as landmarks already
                X, Y = self.P(x, y)
                self.add(self.G(MI.REALM_LABEL_REVEAL.get(name, MI.LATER), f'<text x="{X:.1f}" y="{Y:.1f}" font-family="{FONT}" font-style="italic" font-size="{12*self.fs:.1f}" text-anchor="middle" fill="{c["forest"]}" stroke="{c["land"]}" stroke-width="3" paint-order="stroke">{name}</text>'))
            # the Marches
            X, Y = self.P(188, 116)
            self.add(self.G(MI.REALM_LABEL_REVEAL["THE MARCHES"], f'<text x="{X:.1f}" y="{Y:.1f}" font-family="{FONT_SC}" font-size="{15*self.fs:.1f}" letter-spacing="4" text-anchor="middle" fill="{c["border"]}" stroke="{c["land"]}" stroke-width="3" paint-order="stroke" transform="rotate(-78 {X:.1f} {Y:.1f})">THE MARCHES</text>'))
            # river labels
            for name, (x, y, rot) in {"Wend": (181.5, 150, -82), "Coldrun": (50, 47, -10), "Gilt": (64, 142, -55), "Meryl": (139, 160, -80), "Ysse": (263, 150, -85)}.items():
                X, Y = self.P(x, y)
                self.add(self.G(MI.REALM_LABEL_REVEAL.get(name, MI.LATER), f'<text x="{X:.1f}" y="{Y:.1f}" font-family="{FONT}" font-style="italic" font-size="{11*self.fs:.1f}" text-anchor="middle" fill="{c["water"]}" stroke="{c["land"]}" stroke-width="3" paint-order="stroke" transform="rotate({rot} {X:.1f} {Y:.1f})">{name}</text>'))
            X, Y = self.P(118, 98)
            self.add(self.G(MI.REALM_LABEL_REVEAL["the Oneroad"], f'<text x="{X:.1f}" y="{Y:.1f}" font-family="{FONT}" font-style="italic" font-size="{10*self.fs:.1f}" fill="{c["ink"]}" fill-opacity="0.75" stroke="{c["land"]}" stroke-width="3" paint-order="stroke">the Oneroad</text>'))
        else:
            for name, (x, y, rot, sz) in {"River Wend": (177.5, 90.5, -72, 22), "HEARTHMERE": (170.2, 92.5, 0, 26), "SALTREACH": (186.5, 108, 0, 26),
                                          "the Oneroad": (170, 103.2, -2, 14), "the Drover's Way": (181.6, 119, -88, 13),
                                          "the River Road": (173.0, 96, -84, 13), "the King's Road": (168.5, 106.3, 2, 13)}.items():
                X, Y = self.P(x, y)
                fam = FONT_SC if name.isupper() else FONT
                col = c["water"] if "Wend" in name else (c["kingdomlabel"] if name.isupper() else c["road"])
                self.add(self.G(MI.LABEL_REVEAL.get(name, 1), f'<text x="{X:.1f}" y="{Y:.1f}" font-family="{fam}" font-style="{"normal" if name.isupper() else "italic"}" font-size="{sz*self.fs:.1f}" letter-spacing="{6 if name.isupper() else 1}" text-anchor="middle" fill="{col}" stroke="{c["land"]}" stroke-width="4" paint-order="stroke" transform="rotate({rot} {X:.1f} {Y:.1f})">{name}</text>'))
            if self.prog:
                X, Y = self.P(174.4, 104.6)
                self.add(self.G(27, f'<text x="{X:.1f}" y="{Y:.1f}" font-family="{FONT}" font-style="italic" font-size="{13*self.fs:.1f}" text-anchor="end" fill="{c["secret"]}" stroke="{c["land"]}" stroke-width="3" paint-order="stroke">the catacombs (below)</text>'))
            elif self.secrets:
                X, Y = self.P(174.4, 104.6)
                self.add(f'<g class="secret"><text x="{X:.1f}" y="{Y:.1f}" font-family="{FONT}" font-style="italic" font-size="13" text-anchor="end" fill="{c["secret"]}" stroke="{c["land"]}" stroke-width="3" paint-order="stroke">the catacombs (below)</text></g>')

    def furniture(self):
        c = self.c
        # scale bar
        if self.view == "realm":
            leagues, step = 100, 25
        else:
            leagues, step = 10, 2
        s = self.v["s"]
        x0, y0 = 40, self.H - 40
        if self.view == "marches":
            x0, y0 = 40, self.H - 40
        L = leagues * s
        for i in range(leagues // step):
            fill = c["ink"] if i % 2 == 0 else c["land"]
            self.add(f'<rect x="{x0 + i*step*s:.1f}" y="{y0-6}" width="{step*s:.1f}" height="6" fill="{fill}" stroke="{c["ink"]}" stroke-width="1"/>')
        for i in range(0, leagues + 1, step * 2 if self.view == "realm" else step):
            self.add(f'<text x="{x0 + i*s:.1f}" y="{y0+14}" font-family="{FONT}" font-size="12" text-anchor="middle" fill="{c["ink"]}">{i}</text>')
        self.add(f'<text x="{x0:.1f}" y="{y0-12}" font-family="{FONT_SC}" font-size="13" letter-spacing="2" fill="{c["ink"]}">Leagues</text>')
        # compass
        cx, cy = self.W - 70, self.H - 80 if self.view == "realm" else 90
        if self.view == "marches":
            cx, cy = self.W - 70, self.H - 100
        r = 34
        self.add(f'<g stroke="{c["ink"]}" fill="{c["land"]}" stroke-width="1.2">'
                 f'<circle cx="{cx}" cy="{cy}" r="{r*0.55:.1f}" fill="none"/>'
                 f'<path d="M{cx},{cy-r} L{cx+6},{cy} L{cx},{cy+r} L{cx-6},{cy} Z"/>'
                 f'<path d="M{cx-r},{cy} L{cx},{cy+6} L{cx+r},{cy} L{cx},{cy-6} Z"/>'
                 f'<path d="M{cx},{cy-r} L{cx+6},{cy} L{cx},{cy} Z" fill="{c["ink"]}"/></g>'
                 f'<text x="{cx}" y="{cy-r-6}" font-family="{FONT_SC}" font-size="15" text-anchor="middle" fill="{c["ink"]}">N</text>')
        # cartouche
        if self.view == "realm":
            title, sub = "Winshire", ("Before the story begins" if self.bare else "The Six Kingdoms, as they stand in the Age of Beasts")
            tx, ty = self.W * 0.12, self.H - 70
            tx, ty = 220, 150 * 5 + 300
        else:
            title, sub = "The Marches", self.subtitle or "Greyhold, the Old Ruin, and the Wend between"
        if self.view == "realm":
            tx, ty = self.P(132, 221)
            self.add(f'<text x="{tx}" y="{ty-18}" font-family="{FONT_SC}" font-size="44" letter-spacing="10" text-anchor="middle" fill="{c["ink"]}">{title.upper()}</text>'
                     f'<text x="{tx}" y="{ty+6}" font-family="{FONT}" font-style="italic" font-size="15" text-anchor="middle" fill="{c["ink"]}">{sub}</text>')
        else:
            tx, ty = 210, 60
            self.add(f'<rect x="{tx-180}" y="{ty-46}" width="360" height="74" fill="{c["land"]}" stroke="{c["ink"]}" stroke-width="1.4"/>'
                     f'<rect x="{tx-174}" y="{ty-40}" width="348" height="62" fill="none" stroke="{c["ink"]}" stroke-width="0.6"/>'
                     f'<text x="{tx}" y="{ty-8}" font-family="{FONT_SC}" font-size="30" letter-spacing="6" text-anchor="middle" fill="{c["ink"]}">{title.upper()}</text>'
                     f'<text x="{tx}" y="{ty+14}" font-family="{FONT}" font-style="italic" font-size="14" text-anchor="middle" fill="{c["ink"]}">{sub}</text>')
        # frame
        self.add(f'<rect x="6" y="6" width="{self.W-12:.0f}" height="{self.H-12:.0f}" fill="none" stroke="{c["ink"]}" stroke-width="2"/>'
                 f'<rect x="12" y="12" width="{self.W-24:.0f}" height="{self.H-24:.0f}" fill="none" stroke="{c["ink"]}" stroke-width="0.7"/>')

    # ---------------- the lived-in Marches ----------------
    def ambient(self):
        c = self.c
        for (x, y, ch) in MI.AMBIENT:
            X, Y = self.P(x, y)
            s = 5.5
            g = (f'<path d="M{X-s:.1f},{Y+s*0.5:.1f} v{-s*0.9:.1f} l{s:.1f},{-s*0.8:.1f} l{s:.1f},{s*0.8:.1f} v{s*0.9:.1f} Z" fill="{c["land"]}" stroke="{c["ink"]}" stroke-width="1"/>'
                 f'<path d="M{X+s*1.4:.1f},{Y+s*0.5:.1f} v{-s*0.6:.1f} h{s*1.2:.1f} v{s*0.6:.1f}" fill="none" stroke="{c["ink"]}" stroke-width="0.8"/>')
            self.add(self.G(ch, g))

    def item_glyph(self, it):
        c = self.c
        X, Y = self.P(it["x"], it["y"])
        ink, red = c["ink"], c["secret"]
        k = it["kind"]
        s = 7 * self.fs
        if k == "hamlet":
            return f'<circle cx="{X:.1f}" cy="{Y:.1f}" r="{s*0.55:.1f}" fill="{c["land"]}" stroke="{ink}" stroke-width="1.3"/>'
        if k == "mill":
            spokes = "".join(f'<path d="M{X:.1f},{Y:.1f} l{s*math.cos(a):.1f},{s*math.sin(a):.1f}" stroke="{ink}" stroke-width="1"/>' for a in np.linspace(0, math.pi * 2, 6, endpoint=False))
            return f'<circle cx="{X:.1f}" cy="{Y:.1f}" r="{s:.1f}" fill="{c["land"]}" stroke="{ink}" stroke-width="1.2"/>' + spokes
        if k in ("shrine", "landmark_pt"):
            return f'<path d="M{X:.1f},{Y-s:.1f} L{X+s*0.7:.1f},{Y+s*0.5:.1f} L{X-s*0.7:.1f},{Y+s*0.5:.1f} Z" fill="{c["land"]}" stroke="{ink}" stroke-width="1.2"/><circle cx="{X:.1f}" cy="{Y:.1f}" r="1.6" fill="{ink}"/>'
        if k == "weir":
            return "".join(f'<path d="M{X-s+i*s*0.5:.1f},{Y-s*0.5:.1f} v{s:.1f}" stroke="{ink}" stroke-width="1.4"/>' for i in range(5))
        if k == "smoke":
            return "".join(f'<path d="M{X+i*6:.1f},{Y:.1f} q-6,-8 0,-16 t0,-16" fill="none" stroke="{ink}" stroke-width="1" stroke-opacity="0.6"/>' for i in range(3))
        if k == "fire":
            pts = []
            for i in range(14):
                a = -math.pi / 2 + i * math.pi * 2 / 14
                rr = s * (1.25 if i % 2 == 0 else 0.55)
                pts.append(f"{X + rr*math.cos(a):.1f},{Y + rr*math.sin(a):.1f}")
            return f'<polygon points="{" ".join(pts)}" fill="{red}" fill-opacity="0.85" stroke="{ink}" stroke-width="0.8"/>'
        if k == "roadblock":
            return f'<path d="M{X-s*1.2:.1f},{Y:.1f} h{s*2.4:.1f}" stroke="{ink}" stroke-width="4"/><path d="M{X-s*0.9:.1f},{Y-s*0.6:.1f} l{s*0.5:.1f},{s*1.2:.1f} M{X:.1f},{Y-s*0.6:.1f} l{s*0.5:.1f},{s*1.2:.1f} M{X+s*0.9:.1f},{Y-s*0.6:.1f} l{-s*0.5:.1f},{s*1.2:.1f}" stroke="{ink}" stroke-width="1.2"/>'
        if k in ("camp", "camp_plain"):
            col = red if k == "camp" else ink
            return f'<path d="M{X-s:.1f},{Y+s*0.6:.1f} L{X:.1f},{Y-s*0.9:.1f} L{X+s:.1f},{Y+s*0.6:.1f} Z M{X:.1f},{Y-s*0.9:.1f} v{s*1.5:.1f}" fill="{c["land"]}" stroke="{col}" stroke-width="1.4"/>'
        if k == "beast":
            return (f'<ellipse cx="{X:.1f}" cy="{Y+2:.1f}" rx="{s*0.5:.1f}" ry="{s*0.42:.1f}" fill="{ink}"/>'
                    + "".join(f'<circle cx="{X+dx*s:.1f}" cy="{Y+dy*s:.1f}" r="{s*0.2:.1f}" fill="{ink}"/>' for dx, dy in ((-0.55, -0.45), (-0.2, -0.75), (0.2, -0.75), (0.55, -0.45))))
        if k == "lion":
            mane = "".join(f'<path d="M{X:.1f},{Y:.1f} l{s*1.3*math.cos(a):.1f},{s*1.3*math.sin(a):.1f}" stroke="{red}" stroke-width="1.2"/>' for a in np.linspace(0, math.pi * 2, 14, endpoint=False))
            return mane + f'<circle cx="{X:.1f}" cy="{Y:.1f}" r="{s*0.7:.1f}" fill="{red}" stroke="{ink}" stroke-width="1"/>'
        if k == "dragon":
            return (f'<path d="M{X-s*1.6:.1f},{Y-s*0.4:.1f} Q{X-s*0.6:.1f},{Y-s*0.2:.1f} {X:.1f},{Y+s*0.5:.1f} Q{X+s*0.6:.1f},{Y-s*0.2:.1f} {X+s*1.6:.1f},{Y-s*0.4:.1f}" fill="none" stroke="{ink}" stroke-width="2"/>'
                    f'<path d="M{X+s*0.4:.1f},{Y+s*1.6:.1f} Q{X+s*1.2:.1f},{Y+s*1.5:.1f} {X+s*1.6:.1f},{Y+s*2.2:.1f} Q{X+s*2.0:.1f},{Y+s*1.5:.1f} {X+s*2.8:.1f},{Y+s*1.6:.1f}" fill="none" stroke="{ink}" stroke-width="1.5"/>'
                    f'<path d="M{X-s*1.8:.1f},{Y+s*1.2:.1f} Q{X-s*1.2:.1f},{Y+s*1.2:.1f} {X-s*0.8:.1f},{Y+s*1.8:.1f} Q{X-s*0.4:.1f},{Y+s*1.2:.1f} {X+s*0.2:.1f},{Y+s*1.2:.1f}" fill="none" stroke="{ink}" stroke-width="1.5"/>')
        if k == "eyrie":
            return "".join(f'<path d="M{X-s+i*s:.1f},{Y:.1f} a{s*0.4:.1f},{s*0.5:.1f} 0 0 1 {s*0.8:.1f},0 Z" fill="{ink}"/>' for i in range(3))
        if k == "inn":
            return f'<rect x="{X-s*0.7:.1f}" y="{Y-s*0.6:.1f}" width="{s*1.4:.1f}" height="{s*1.2:.1f}" fill="{c["land"]}" stroke="{ink}" stroke-width="1.2"/><path d="M{X+s*0.7:.1f},{Y-s*0.6:.1f} v{-s*0.8:.1f} h{s*0.8:.1f} v{s*0.5:.1f} h{-s*0.8:.1f}" fill="{ink}" stroke="{ink}" stroke-width="1"/>'
        if k == "pier":
            return f'<path d="M{X:.1f},{Y:.1f} h{s*1.6:.1f} M{X+s*0.4:.1f},{Y:.1f} v{s*0.6:.1f} M{X+s*1.2:.1f},{Y:.1f} v{s*0.6:.1f}" stroke="{ink}" stroke-width="1.6"/>'
        if k == "death":
            return f'<path d="M{X:.1f},{Y-s:.1f} v{s*2:.1f} M{X-s*0.6:.1f},{Y-s*0.4:.1f} h{s*1.2:.1f}" stroke="{red}" stroke-width="2.2"/>'
        if k == "battle":
            return f'<path d="M{X-s:.1f},{Y-s:.1f} L{X+s:.1f},{Y+s:.1f} M{X+s:.1f},{Y-s:.1f} L{X-s:.1f},{Y+s:.1f}" stroke="{red}" stroke-width="2.6"/><path d="M{X-s*1.1:.1f},{Y-s*0.6:.1f} l{s*0.5:.1f},{-s*0.5:.1f} M{X+s*1.1:.1f},{Y-s*0.6:.1f} l{-s*0.5:.1f},{-s*0.5:.1f}" stroke="{red}" stroke-width="1.6"/>'
        if k == "chain":
            return "".join(f'<ellipse cx="{X+i*s*0.9:.1f}" cy="{Y:.1f}" rx="{s*0.55:.1f}" ry="{s*0.3:.1f}" fill="none" stroke="{red}" stroke-width="1.4"/>' for i in range(-1, 2))
        if k == "verse":
            return "".join(f'<path d="M{X-s:.1f},{Y-s*0.5+i*s*0.5:.1f} h{s*(2 - (i%2)*0.6):.1f}" stroke="{ink}" stroke-width="1.2"/>' for i in range(3))
        if k == "cave":
            return f'<path d="M{X-s:.1f},{Y+s*0.6:.1f} a{s:.1f},{s:.1f} 0 0 1 {s*2:.1f},0 Z" fill="{ink}"/>'
        if k == "watchers":
            return "".join(f'<circle cx="{X+i*s*0.8:.1f}" cy="{Y:.1f}" r="{s*0.28:.1f}" fill="{ink}"/>' for i in range(-2, 3))
        if k == "scroll":
            return f'<rect x="{X-s*0.6:.1f}" y="{Y-s*0.8:.1f}" width="{s*1.2:.1f}" height="{s*1.6:.1f}" fill="{c["land"]}" stroke="{red}" stroke-width="1.3"/>' + "".join(f'<path d="M{X-s*0.35:.1f},{Y-s*0.4+i*s*0.4:.1f} h{s*0.7:.1f}" stroke="{red}" stroke-width="0.9"/>' for i in range(3))
        if k == "lock":
            return f'<circle cx="{X:.1f}" cy="{Y:.1f}" r="{s:.1f}" fill="{c["land"]}" stroke="{red}" stroke-width="2"/><circle cx="{X:.1f}" cy="{Y-s*0.2:.1f}" r="{s*0.3:.1f}" fill="{red}"/><path d="M{X:.1f},{Y:.1f} v{s*0.55:.1f}" stroke="{red}" stroke-width="2"/>'
        if k == "bond":
            return f'<circle cx="{X-s*0.45:.1f}" cy="{Y:.1f}" r="{s*0.8:.1f}" fill="none" stroke="{red}" stroke-width="1.8"/><circle cx="{X+s*0.45:.1f}" cy="{Y:.1f}" r="{s*0.8:.1f}" fill="none" stroke="{red}" stroke-width="1.8"/>'
        if k == "meet":
            return f'<circle cx="{X:.1f}" cy="{Y:.1f}" r="{s*0.45:.1f}" fill="{red}"/><path d="M{X-s*1.6:.1f},{Y:.1f} h{s*0.9:.1f} M{X+s*1.6:.1f},{Y:.1f} h{-s*0.9:.1f}" stroke="{red}" stroke-width="1.8"/>'
        if k == "titan":
            rays = "".join(f'<path d="M{X+s*1.2*math.cos(a):.1f},{Y+s*1.2*math.sin(a):.1f} L{X+s*(3.4 if i%2==0 else 2.4)*math.cos(a):.1f},{Y+s*(3.4 if i%2==0 else 2.4)*math.sin(a):.1f}" stroke="{red}" stroke-width="2"/>' for i, a in enumerate(np.linspace(0, math.pi*2, 16, endpoint=False)))
            return rays + f'<circle cx="{X:.1f}" cy="{Y:.1f}" r="{s:.1f}" fill="{red}" fill-opacity="0.7" stroke="{ink}" stroke-width="1.2"/>'
        if k == "area_small":
            return ""
        if k.startswith("arrow"):
            d = {"arrow_w": (-1, 0), "arrow_s": (0, 1), "arrow_n": (0, -1), "arrow_ne": (0.7, -0.7)}[k]
            L = s * 3
            ex, ey = X + d[0] * L, Y + d[1] * L
            px, py = -d[1], d[0]
            return (f'<path d="M{X:.1f},{Y:.1f} L{ex:.1f},{ey:.1f}" stroke="{ink}" stroke-width="1.8"/>'
                    f'<path d="M{ex:.1f},{ey:.1f} L{ex - d[0]*s*0.8 + px*s*0.5:.1f},{ey - d[1]*s*0.8 + py*s*0.5:.1f} L{ex - d[0]*s*0.8 - px*s*0.5:.1f},{ey - d[1]*s*0.8 - py*s*0.5:.1f} Z" fill="{ink}"/>')
        return ""

    def items(self):
        c = self.c
        for it in MI.ITEMS:
            X, Y = self.P(it["x"], it["y"])
            parts = []
            if it["kind"] == "path":
                pts = it["path"]
                d = self.smooth_path(pts)
                (x1, y1), (x2, y2) = pts[-2], pts[-1]
                A, B = self.P(x1, y1), self.P(x2, y2)
                ang = math.atan2(B[1] - A[1], B[0] - A[0])
                hx, hy = B
                head = f'<path d="M{hx:.1f},{hy:.1f} L{hx - 12*math.cos(ang - 0.45):.1f},{hy - 12*math.sin(ang - 0.45):.1f} L{hx - 12*math.cos(ang + 0.45):.1f},{hy - 12*math.sin(ang + 0.45):.1f} Z" fill="{c["secret"]}"/>'
                parts.append(f'<path d="{d}" fill="none" stroke="{c["secret"]}" stroke-width="2" stroke-dasharray="6 4"/>' + head)
            else:
                parts.append(self.item_glyph(it))
            is_event = it["kind"] in EVENT_KINDS
            stale = (not self.interactive) and self.chapter is not None and is_event and it["ch"] < self.chapter
            if it["label"] and it["name"] and not stale:
                size = 13.5 * self.fs * (1.25 if it["kind"] in ("hamlet", "area_small") else 1)
                lx = X + 14 * self.fs + it["dx"] * self.v["s"]
                ly = Y + size * 0.35 + it["dy"] * self.v["s"]
                anchor = "start"
                if it["kind"] == "arrow_w":
                    anchor, lx, ly = "start", X - 10, Y - 12
                if it["kind"] == "arrow_s":
                    lx, ly = X + 12, Y + 4
                if it["dx"] < 0:
                    anchor = "end"; lx = X - 14 * self.fs + (it["dx"] + 3.4) * self.v["s"] if it["dx"] < -2 else X - 14 * self.fs
                    if it["dx"] < -2:
                        anchor = "end"; lx = X - 16 * self.fs
                style = "normal" if it["kind"] in ("hamlet", "inn", "mill", "cave", "area_small") else "italic"
                cls = ' class="evlabel"' if is_event else ''
                parts.append(f'<g{cls}><text x="{lx:.1f}" y="{ly:.1f}" font-family="{FONT}" font-style="{style}" font-size="{size:.1f}" text-anchor="{anchor}" fill="{c["label"]}" stroke="{c["land"]}" stroke-width="3" paint-order="stroke">{html_esc(it["name"])}</text></g>')
            body = "".join(parts)
            if self.interactive:
                body = (f'<g class="place item" data-item="{it["id"]}" tabindex="0" role="button" aria-label="{html_esc(it["name"] or it["desc"][:40])}">'
                        f'<circle cx="{X:.1f}" cy="{Y:.1f}" r="16" fill="transparent"/>{body}</g>')
            self.add(self.G(it["ch"], body, (X, Y)))

    def svg(self, interactive=False):
        self.sea()
        if self.view == "marches":
            # marches is all land: fill whole canvas
            self.add(f'<rect width="{self.W:.0f}" height="{self.H:.0f}" fill="{self.c["land"]}"/>')
        else:
            self.land()
        self.plains()
        self.marshes()
        self.forests()
        self.water()
        if not self.bare:
            self.borders() if self.view == "realm" else None
            self.roads()
        self.mountains()
        if self.bare:
            self.furniture()
            body = "\n".join(self.out)
            return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.W:.0f} {self.H:.0f}" width="{self.W:.0f}" height="{self.H:.0f}">\n{body}\n</svg>\n')
        self.secrets_layer()
        self.labels()
        if self.prog and self.view == "marches":
            self.ambient()
            self.items()
        self.places(interactive)
        self.furniture()
        body = "\n".join(self.out)
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.W:.0f} {self.H:.0f}" width="{self.W:.0f}" height="{self.H:.0f}">\n{body}\n</svg>\n')


REALM_HIDE = {"millbrook", "catacombs"}
REALM_LABEL = {"hallowmere": (-1, -0.6), "greyhold": (-1, 1.2), "oldruin": (0.5, -1.5), "harrowsend": (0.4, -1.6), "ashford": (-1, -0.2), "cotterscross": (0.3, 0.4)}

def point_in(poly, x, y):
    inside = False
    n = len(poly)
    for i in range(n):
        x1, y1 = poly[i]; x2, y2 = poly[(i + 1) % n]
        if (y1 > y) != (y2 > y):
            xi = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            if x < xi:
                inside = not inside
    return inside


def render(view, style, secrets, interactive=False, chapter=None, subtitle=None, bare=False):
    return Map(view, style, secrets, chapter=chapter, interactive=interactive, subtitle=subtitle, bare=bare).svg(interactive)


if __name__ == "__main__":
    import cairosvg, os
    os.makedirs("out", exist_ok=True)
    for view in ("realm", "marches"):
        s = render(view, "color", True)
        open(f"out/{view}_preview.svg", "w").write(s)
        cairosvg.svg2png(bytestring=s.encode(), write_to=f"out/{view}_preview.png")
    print("ok")


EVENT_KINDS = {"fire", "battle", "death", "camp", "roadblock", "dragon", "beast", "lion", "chain", "scroll", "lock", "bond", "meet", "titan", "watchers", "path", "smoke"}


def html_esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")
