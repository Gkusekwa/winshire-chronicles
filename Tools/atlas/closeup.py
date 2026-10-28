"""Close-up maps for the chapter-end pages of Books 2 and 3.

A close-up is 840 x 1200 px, centred on a chapter's "Ends at" place, at a scale that fits the action:
  scale 30 px/league is the Marches look (Book 1's close-up), 20 a town and its country, 12 a district,
  7 a kingdom, 5 a sea crossing or half the realm.
Close-ups inside the Marches at the Marches scale use render.py's own "marches" view, moved to the new centre,
so they look exactly like Book 1's. Everything else is drawn here, in the same ink style.
"""
import math, random
import numpy as np
import world as Wd
from render import Map, FONT, FONT_SC, PAL, point_in, html_esc, LINE_KINDS

CW, CH = 840, 1200


def close_box(cx, cy, s):
    return dict(x0=cx - CW / 2 / s, x1=cx + CW / 2 / s, y0=cy - CH / 2 / s, y1=cy + CH / 2 / s, s=s)


def lerp_s(s, a, b):
    """Interpolate a size between the realm map (s=4.6) and the Marches map (s=30), on a log scale."""
    t = (math.log(s) - math.log(4.6)) / (math.log(30) - math.log(4.6))
    t = max(0.0, min(1.0, t))
    return a + (b - a) * t


RANGE_LABELS = {"The Iron Fells": (114, 33, 55), "The High Crown": (70, 16, 0), "The Scarfell": (204, 82, 55),
                "Sunward Hills": (76, 112, 25), "The Worldsend": (311, 120, -90)}
AREA_LABELS = {"The Greenwold": (152, 82), "Elderwood": (48, 116), "The Ashlings": (210, 128),
               "The Fellwood": (183.6, 103.4), "The Wendwood": (182, 160)}   # the Thornwood, the Plains, the Downs and the Saltings are places
RIVER_NAMES = {"Wend": None, "The Coldrun": "Coldrun", "The Gilt": "Gilt", "The Meryl": "Meryl", "The Ysse": "Ysse", "Hollow Beck": "Hollow Beck"}


class CloseMap(Map):
    def __init__(self, cx, cy, s, chapter, mi, title, subtitle, style="ink"):
        super().__init__("close", style, False, chapter=chapter, mi=mi, box=close_box(cx, cy, s), title=title, subtitle=subtitle)
        self.fs = 1.25
        self.s = s
        self.seed0 = int(round(cx * 7 + cy * 13 + s * 3)) % 9973

    def reseed(self, k):
        # every layer gets its own stream, so a coast or a forest looks the same from one chapter to the next
        self.rng = random.Random(1000 + k)

    # ---------------- layers ----------------
    def land(self):
        c = self.c
        self.reseed(1)
        land_ch = getattr(self.mi, "EXTRA_LAND_CH", None) or [0] * len(getattr(self.mi, "EXTRA_LAND", []))
        polys = [Wd.COAST] + [p for p, ch in zip(getattr(self.mi, "EXTRA_LAND", []), land_ch) if ch <= self.cap]
        for i, poly in enumerate(polys):
            rough = self.roughen(poly, 0.35 if i == 0 else 0.25, 6 if i == 0 else 5, closed=True)
            if i == 0:
                self.coast = rough
            d = self.smooth_path(rough, True)
            for j, w in enumerate((14, 9, 5)):
                op = 0.10 + 0.08 * j
                self.add(f'<path d="{d}" fill="none" stroke="{c["water"]}" stroke-width="{w * lerp_s(self.s, 0.92, 1.6):.1f}" stroke-opacity="{op:.2f}" stroke-linejoin="round"/>')
            self.add(f'<path d="{d}" fill="{c["land"]}" stroke="{c["ink"]}" stroke-width="{lerp_s(self.s, 1.6, 2.2):.1f}" stroke-linejoin="round"/>')
        for isl in Wd.ISLANDS + getattr(self.mi, "EXTRA_ISLANDS", []):
            r = self.roughen(isl, 0.3, 4, closed=True)
            self.add(f'<path d="{self.smooth_path(r, True)}" fill="{c["land"]}" stroke="{c["ink"]}" stroke-width="1.4"/>')

    def plains(self):
        c = self.c
        self.reseed(2)
        dens = max(1.0, self.s / 4.6) ** 1.2
        for name, poly in Wd.PLAINS.items():
            xs = [p[0] for p in poly]; ys = [p[1] for p in poly]
            if max(xs) < self.v["x0"] or min(xs) > self.v["x1"] or max(ys) < self.v["y0"] or min(ys) > self.v["y1"]:
                continue
            for _ in range(int((max(xs) - min(xs)) * (max(ys) - min(ys)) / 9 * dens)):
                x = self.rng.uniform(min(xs), max(xs)); y = self.rng.uniform(min(ys), max(ys))
                if not point_in(poly, x, y) or not self.inside(x, y):
                    continue
                X, Y = self.P(x, y)
                self.add(f'<path d="M{X-3:.1f},{Y:.1f} l2,-3 M{X:.1f},{Y:.1f} l0,-4 M{X+3:.1f},{Y:.1f} l-2,-3" stroke="{c["plain"]}" stroke-width="0.8" fill="none"/>')

    def marshes(self):
        c = self.c
        self.reseed(3)
        step = lerp_s(self.s, 2.2, 0.55)
        L = lerp_s(self.s, 5, 9)
        for name, poly in Wd.MARSHES.items():
            xs = [p[0] for p in poly]; ys = [p[1] for p in poly]
            y = min(ys)
            while y < max(ys):
                x = min(xs)
                while x < max(xs):
                    xx = x + self.rng.uniform(-step / 3, step / 3)
                    yy = y + self.rng.uniform(-step / 3, step / 3)
                    if point_in(poly, xx, yy) and self.inside(xx, yy):
                        X, Y = self.P(xx, yy)
                        self.add(f'<path d="M{X-L/2:.1f},{Y:.1f} h{L}" stroke="{c["marsh"]}" stroke-width="0.9"/>'
                                 f'<path d="M{X:.1f},{Y:.1f} v-{L*0.5:.1f}" stroke="{c["marsh"]}" stroke-width="0.7"/>')
                    x += step
                y += step

    def forests(self):
        c = self.c
        self.reseed(4)
        step = lerp_s(self.s, 12.0, 18.0) / self.s
        r = lerp_s(self.s, 4.2, 8.0)
        for name, poly in list(Wd.FORESTS.items()) + list(getattr(self.mi, "EXTRA_FORESTS", {}).items()):
            xs = [p[0] for p in poly]; ys = [p[1] for p in poly]
            if max(xs) < self.v["x0"] - 1 or min(xs) > self.v["x1"] + 1 or max(ys) < self.v["y0"] - 1 or min(ys) > self.v["y1"] + 1:
                continue
            trees = []
            y = max(min(ys), self.v["y0"] - 1)
            while y < min(max(ys), self.v["y1"] + 1):
                x = max(min(xs), self.v["x0"] - 1)
                while x < min(max(xs), self.v["x1"] + 1):
                    rx = random.Random(int(x * 1000) * 31 + int(y * 1000))
                    xx = x + rx.uniform(-step / 2, step / 2)
                    yy = y + rx.uniform(-step / 2, step / 2)
                    if point_in(poly, xx, yy) and self.inside(xx, yy, 1):
                        trees.append((xx, yy, rx.uniform(0.8, 1.2)))
                    x += step
                y += step
            trees.sort(key=lambda p: p[1])
            for xx, yy, k in trees:
                X, Y = self.P(xx, yy)
                rr = r * k
                self.add(f'<path d="M{X:.1f},{Y+rr*1.1:.1f} v{rr*0.7:.1f}" stroke="{c["forest"]}" stroke-width="0.9"/>'
                         f'<circle cx="{X:.1f}" cy="{Y:.1f}" r="{rr:.1f}" fill="{c["forestfill"]}" stroke="{c["forest"]}" stroke-width="0.9"/>')

    def water(self):
        c = self.c
        self.reseed(5)
        inner = []

        def river(pts, w0, w1):
            rr = self.roughen(pts, 0.18, 4)
            n = len(rr)
            seg = max(n // 12, 2)
            for i in range(0, n - 1, seg):
                part = rr[i:i + seg + 1]
                w = w0 + (w1 - w0) * i / n
                self.add(f'<path d="{self.smooth_path(part)}" fill="none" stroke="{c["water"]}" stroke-width="{w:.2f}" stroke-linecap="round" stroke-linejoin="round"/>')
                if self.style == "ink" and w > 3:
                    inner.append((part, w - 2.4))
        river(Wd.WEND, lerp_s(self.s, 1.2, 8), lerp_s(self.s, 4.0, 12))
        for name, pts in list(Wd.RIVERS.items()) + list(getattr(self.mi, "EXTRA_RIVERS", {}).items()):
            river(pts, lerp_s(self.s, 0.8, 3), lerp_s(self.s, 2.4, 5))
        for part, w in inner:
            self.add(f'<path d="{self.smooth_path(part)}" fill="none" stroke="#ffffff" stroke-width="{w:.2f}" stroke-linecap="round" stroke-linejoin="round"/>')
        for name, ((x, y), rx, ry) in list(Wd.LAKES.items()) + list(getattr(self.mi, "EXTRA_LAKES", {}).items()):
            pts = [(x + rx * math.cos(a), y + ry * math.sin(a)) for a in np.linspace(0, 2 * math.pi, 14, endpoint=False)]
            r = self.roughen(pts, 0.25, 4, closed=True)
            self.add(f'<path d="{self.smooth_path(r, True)}" fill="{c["wfill"]}" stroke="{c["water"]}" stroke-width="{lerp_s(self.s, 1.2, 2.4):.1f}"/>')
        if not getattr(self.mi, "ISLAND", True) and self.s >= 12 and self.inside(*self.mi.EDDY):
            self.eddy_mark(*self.mi.EDDY)

    def borders(self):
        c = self.c
        self.reseed(6)
        for line in Wd.BORDERS:
            r = self.roughen(line, 0.15, 3)
            self.add(self.G(self.mi.BORDER_REVEAL, f'<path d="{self.smooth_path(r)}" fill="none" stroke="{c["border"]}" stroke-width="{lerp_s(self.s, 1.4, 2.5):.1f}" stroke-dasharray="6 3 1.5 3" stroke-opacity="0.7"/>'))

    def roads(self):
        c = self.c
        self.reseed(7)
        w = lerp_s(self.s, 1.2, 2.6)
        dash = "4 3" if self.s < 9 else "9 5"
        for name, line in Wd.ROADS.items():
            r = self.roughen(line, 0.08, 3)
            rch = self.mi.REALM_ROAD_REVEAL.get(name, self.mi.LATER)
            self.add(self.G(rch, f'<path d="{self.smooth_path(r)}" fill="none" stroke="{c["road"]}" stroke-width="{w:.1f}" stroke-dasharray="{dash}"/>'))
        r = self.roughen(Wd.ONEROAD, 0.06, 3)
        self.add(self.G(self.mi.ROAD_REVEAL["ONEROAD"], f'<path d="{self.smooth_path(r)}" fill="none" stroke="{c["ink"]}" stroke-width="{lerp_s(self.s, 1.0, 2.2):.1f}" stroke-dasharray="1 4" stroke-linecap="round" stroke-opacity="0.75"/>'))
        if self.s >= 14:
            for (a, b, name) in Wd.FERRIES:
                A, B = self.P(*a), self.P(*b)
                self.add(f'<path d="M{A[0]:.1f},{A[1]:.1f} L{B[0]:.1f},{B[1]:.1f}" stroke="{c["ink"]}" stroke-width="1.6" stroke-dasharray="3 3"/>')

    def mountains(self):
        c = self.c
        self.reseed(8)
        spacing = lerp_s(self.s, 9.2, 27.0) / self.s
        for name, (line, hw, dens) in Wd.MOUNTAINS.items():
            line = np.array(line, float)
            seg = np.sqrt(((line[1:] - line[:-1]) ** 2).sum(1)); cum = np.r_[0, np.cumsum(seg)]
            n = int(cum[-1] * dens / spacing * (hw / 3.5) * 1.5)
            pts = []
            for _ in range(n):
                t = self.rng.uniform(0, cum[-1])
                x = np.interp(t, cum, line[:, 0]); y = np.interp(t, cum, line[:, 1])
                off = self.rng.gauss(0, hw / 2)
                pts.append((x + self.rng.uniform(-1, 1), y + off, self.rng.uniform(0, 1), self.rng.uniform(0.9, 1.3), self.rng.uniform(-0.15, 0.15)))
            pts.sort(key=lambda p: p[1])
            for x, y, hr, wr, pr in pts:
                if not self.inside(x, y, 2) or not point_in(Wd.COAST, x, y):
                    continue
                X, Y = self.P(x, y)
                h = (lerp_s(self.s, 11, 22) + hr * lerp_s(self.s, 8, 12)) * (1.25 if name == "The Worldsend" else 1)
                if name == "Sunward Hills" or (self.s > 14 and name == "The Scarfell"):
                    h *= 0.6
                w = h * wr
                pk = X + pr * w
                self.add(f'<path d="M{X-w/2:.1f},{Y:.1f} L{pk:.1f},{Y-h:.1f} L{X+w/2:.1f},{Y:.1f} Z" fill="{c["land"]}" stroke="none"/>'
                         f'<path d="M{X-w/2:.1f},{Y:.1f} L{pk:.1f},{Y-h:.1f} L{X+w/2:.1f},{Y:.1f}" fill="none" stroke="{c["mount"]}" stroke-width="1.1" stroke-linejoin="round"/>'
                         f'<path d="M{pk:.1f},{Y-h:.1f} L{X+w*0.12:.1f},{Y-h*0.35:.1f} M{pk+w*0.12:.1f},{Y-h*0.7:.1f} l{w*0.14:.1f},{h*0.18:.1f} M{pk+w*0.2:.1f},{Y-h*0.45:.1f} l{w*0.12:.1f},{h*0.16:.1f}" fill="none" stroke="{c["mount"]}" stroke-width="0.7"/>')

    def secrets_layer(self):
        c = self.c
        ch = getattr(self.mi, "CATACOMBS_CH", 27)
        if self.s < 12 or ch > self.cap:
            return
        r = self.roughen(Wd.CATACOMBS, 0.05, 3)
        self.add(f'<path d="{self.smooth_path(r)}" fill="none" stroke="{c["secret"]}" stroke-width="4" stroke-opacity="0.35" stroke-linecap="round"/>'
                 f'<path d="{self.smooth_path(r)}" fill="none" stroke="{c["secret"]}" stroke-width="1.4" stroke-dasharray="2 4"/>')

    # ---------------- names ----------------
    def label_at(self, name, x, y, size, fam, style, col, rot=0, ls=1, ok_pad=70):
        X, Y = self.P(x, y)
        w = len(name) * size * (0.62 if name.isupper() else 0.45) + ls * len(name)
        t = math.radians(rot)
        bw = abs(w * math.cos(t)) + abs(size * math.sin(t))
        bh = abs(w * math.sin(t)) + abs(size * math.cos(t))
        if not (bw / 2 + 14 < X < self.W - bw / 2 - 14 and bh / 2 + 14 < Y < self.H - bh / 2 - 14):
            return False
        self.obs.append((X - bw / 2, Y - bh / 2 - size * 0.3, X + bw / 2, Y + bh / 2 - size * 0.3))
        self.add(f'<text x="{X:.1f}" y="{Y:.1f}" font-family="{fam}" font-style="{style}" font-size="{size:.1f}" letter-spacing="{ls}" text-anchor="middle" '
                 f'fill="{col}" stroke="{self.c["land"]}" stroke-width="4" paint-order="stroke" transform="rotate({rot} {X:.1f} {Y:.1f})">{html_esc(name)}</text>')
        return True

    def river_label(self, name, pts, size):
        """Name a river along a straight-ish stretch of it near the middle of the view."""
        cx, cy = (self.v["x0"] + self.v["x1"]) / 2, (self.v["y0"] + self.v["y1"]) / 2
        best = None
        lakes = list(Wd.LAKES.values()) + list(getattr(self.mi, "EXTRA_LAKES", {}).values())
        for (x0, y0), (x1, y1) in zip(pts[:-1], pts[1:]):
            mx, my = (x0 + x1) / 2, (y0 + y1) / 2
            if not self.inside(mx, my, -3 * 30 / self.s):
                continue
            if any(((mx - lx) / (rx + 1)) ** 2 + ((my - ly) / (ry + 1)) ** 2 < 1 for (lx, ly), rx, ry in lakes):
                continue
            L = math.hypot(x1 - x0, y1 - y0) * self.s
            if L < len(name) * size * 0.5:
                continue
            d = math.hypot(mx - cx, my - cy)
            if best is None or d < best[0]:
                best = (d, mx, my, math.degrees(math.atan2(y1 - y0, x1 - x0)))
        if best is None:
            return
        d, mx, my, ang = best
        if ang > 90: ang -= 180
        if ang < -90: ang += 180
        off = 9 / self.s
        nx, ny = -math.sin(math.radians(ang)), math.cos(math.radians(ang))
        self.label_at(name, mx + nx * off, my + ny * off - 0.0, size, FONT, "italic", self.c["water"], rot=round(ang), ls=1)

    def labels(self):
        c = self.c
        G = lambda ch: ch <= self.cap
        mi = self.mi
        for kid, k in Wd.KINGDOMS.items():
            if G(mi.KINGDOM_REVEAL.get(kid, mi.LATER)):
                x, y = getattr(mi, "KINGDOM_LABEL_AT", {}).get(kid, k["label"])
                X, Y = self.P(x, y)
                if X - len(k["name"]) * 30 * 0.45 < 412 and Y < 98 + 30:
                    continue      # under the cartouche
                self.label_at(k["name"].upper(), x, y, 30, FONT_SC, "normal", c["kingdomlabel"], ls=7)
        for name, (x, y) in list(Wd.SEAS.items()) + list(getattr(mi, "EXTRA_SEAS", {}).items()):
            if G(mi.REALM_LABEL_REVEAL.get(name, mi.LATER)) and self.inside(x, y):
                self.label_at(name, x, y, 24, FONT, "italic", c["water"], rot=-90 if x < 10 else 0, ls=5)
        for name, (x, y, rot) in RANGE_LABELS.items():
            if G(mi.REALM_LABEL_REVEAL.get(name, mi.LATER)):
                self.label_at(name, x, y, 17, FONT, "italic", c["mount"], rot=rot, ls=2)
        for name, (x, y) in AREA_LABELS.items():
            if name in ("The Fellwood", "The Wendwood") and self.s < 10:
                continue
            if G(mi.REALM_LABEL_REVEAL.get(name, mi.LATER)):
                self.label_at(name, x, y, 17, FONT, "italic", c["forest"], ls=1)
        if G(mi.REALM_LABEL_REVEAL["THE MARCHES"]) and self.s < 16:
            self.label_at("THE MARCHES", 186, 112, 19, FONT_SC, "normal", c["border"], rot=-78, ls=4)
        if G(mi.REALM_LABEL_REVEAL.get("Wend", mi.LATER)):
            self.river_label("Wend" if self.s < 14 else "River Wend", Wd.WEND, 17)
        for key, name in RIVER_NAMES.items():
            if key == "Wend":
                continue
            if G(mi.REALM_LABEL_REVEAL.get(name, mi.LATER)) and key in Wd.RIVERS:
                self.river_label(name, Wd.RIVERS[key], 15)
        for name, (x, y, rot) in getattr(mi, "EXTRA_LABELS", {}).items():
            if G(mi.REALM_LABEL_REVEAL.get(name, mi.LATER)):
                self.label_at(name, x, y, 17, FONT, "italic", c["ink"], rot=rot, ls=1)

    def item_visible(self, it):
        # wide close-ups keep to the realm-scale story and this chapter's own marks; the Marches detail needs a close look
        if not super().item_visible(it):
            return False
        if it.get("realm") or self.s >= 14 or it["ch"] == self.chapter:
            return True
        return self.s >= 9 and self.chapter - 3 <= it["ch"]

    def glyph(self, p):
        # the close-ups use the Marches-size symbols
        v = self.view
        self.view = "marches"
        try:
            return super().glyph(p)
        finally:
            self.view = v

    def places(self, interactive=False):
        c = self.c
        mi = self.mi
        sreveal = getattr(mi, "SECRET_REVEAL", {})
        hide = getattr(mi, "HIDE", {})
        for p in Wd.P + getattr(mi, "EXTRA_PLACES", []):
            if p["id"] in hide and self.cap >= hide[p["id"]]:
                continue
            if p["id"] == "catacombs" or p["id"] in getattr(mi, "CLOSE_HIDE", ()):
                continue
            if p["secret"]:
                pch = sreveal.get(p["id"], mi.LATER)
            elif p["scope"] == "marches":
                if self.s < 14:
                    continue
                pch = mi.REVEAL.get(p["id"], mi.LATER)
            else:
                pch = mi.REALM_REVEAL.get(p["id"], mi.REVEAL.get(p["id"], mi.LATER))
            if pch > self.cap or not self.inside(p["x"], p["y"]):
                continue
            if p["kind"] == "landmark" and p["id"] in getattr(mi, "AREA_AS_LABEL", ()):
                continue
            X, Y = self.P(p["x"], p["y"])
            gl = self.glyph(p)
            k = 1.7 * self.fs
            size = {"capital": 15, "city": 12.5, "town": 11, "village": 10, "fortress": 12, "hold": 12,
                    "ruin": 11.5, "temple": 10.5, "tower": 9.5, "farm": 9.5, "landmark": 12}[p["kind"]] * k
            col = c["secret"] if p["secret"] else c["label"]
            new = pch == self.chapter
            if p["kind"] == "landmark":
                lx, ly = X + p["ldx"] * min(self.s, 12), Y + p["ldy"] * min(self.s, 12)
                self.lq.append(dict(X=lx, Y=ly, text=p["name"], size=size, fam=FONT, style="italic", col=col, prio=1 + new * 2, area=True))
            else:
                fam = FONT_SC if p["kind"] == "capital" else FONT
                major = p["kind"] in ("capital", "city", "town", "fortress", "hold", "ruin", "temple")
                self.lq.append(dict(X=X, Y=Y, text=p["name"], size=size, fam=fam, style="normal", col=col,
                                    prio=(3.5 if new else 2.5), pref=("end" if p["ldx"] < 0 else "start"), force=major or new, g=7 * k))
                self.obs.append((X - 9, Y - 9, X + 9, Y + 9))
            self.add(self.G(pch, gl, (X, Y)))

    def place_labels(self):
        # rivers and the cartouche are obstacles for names
        for pts in [Wd.WEND] + list(Wd.RIVERS.values()) + list(getattr(self.mi, "EXTRA_RIVERS", {}).values()):
            for (x0, y0), (x1, y1) in zip(pts[:-1], pts[1:]):
                for t in np.linspace(0, 1, 8):
                    x, y = x0 + (x1 - x0) * t, y0 + (y1 - y0) * t
                    if self.inside(x, y):
                        X, Y = self.P(x, y)
                        self.obs.append((X - 4, Y - 4, X + 4, Y + 4))
        self.hard_obs = [(24, 8, 412, 98), (28, self.H - 72, 330, self.H - 10), (self.W - 112, self.H - 154, self.W - 28, self.H - 58)]
        self.obs.extend(self.hard_obs)
        super().place_labels()

    def furniture(self):
        c = self.c
        s = self.s
        # scale bar about 250-330 px long
        for leagues, step in ((2, 0.5), (5, 1), (10, 2), (20, 5), (25, 5), (50, 10), (100, 25)):
            if leagues * s >= 220:
                break
        x0, y0 = 40, self.H - 40
        for i in range(int(round(leagues / step))):
            fill = c["ink"] if i % 2 == 0 else c["land"]
            self.add(f'<rect x="{x0 + i*step*s:.1f}" y="{y0-6}" width="{step*s:.1f}" height="6" fill="{fill}" stroke="{c["ink"]}" stroke-width="1"/>')
        lab = [0, leagues / 2, leagues] if leagues % 2 == 0 else [0, leagues]
        for i in lab:
            self.add(f'<text x="{x0 + i*s:.1f}" y="{y0+14}" font-family="{FONT}" font-size="12" text-anchor="middle" fill="{c["ink"]}">{i:g}</text>')
        self.add(f'<text x="{x0:.1f}" y="{y0-12}" font-family="{FONT_SC}" font-size="13" letter-spacing="2" fill="{c["ink"]}">Leagues</text>')
        cx, cy, r = self.W - 70, self.H - 100, 34
        self.add(f'<g stroke="{c["ink"]}" fill="{c["land"]}" stroke-width="1.2">'
                 f'<circle cx="{cx}" cy="{cy}" r="{r*0.55:.1f}" fill="none"/>'
                 f'<path d="M{cx},{cy-r} L{cx+6},{cy} L{cx},{cy+r} L{cx-6},{cy} Z"/>'
                 f'<path d="M{cx-r},{cy} L{cx},{cy+6} L{cx+r},{cy} L{cx},{cy-6} Z"/>'
                 f'<path d="M{cx},{cy-r} L{cx+6},{cy} L{cx},{cy} Z" fill="{c["ink"]}"/></g>'
                 f'<text x="{cx}" y="{cy-r-6}" font-family="{FONT_SC}" font-size="15" text-anchor="middle" fill="{c["ink"]}">N</text>')
        title, sub = self.title, self.subtitle
        tx, ty = 210, 60
        tsize = 30 if len(title) <= 15 else 25
        self.add(f'<rect x="{tx-180}" y="{ty-46}" width="360" height="74" fill="{c["land"]}" stroke="{c["ink"]}" stroke-width="1.4"/>'
                 f'<rect x="{tx-174}" y="{ty-40}" width="348" height="62" fill="none" stroke="{c["ink"]}" stroke-width="0.6"/>'
                 f'<text x="{tx}" y="{ty-8}" font-family="{FONT_SC}" font-size="{tsize}" letter-spacing="{6 if tsize == 30 else 4}" text-anchor="middle" fill="{c["ink"]}">{html_esc(title.upper())}</text>'
                 f'<text x="{tx}" y="{ty+14}" font-family="{FONT}" font-style="italic" font-size="14" text-anchor="middle" fill="{c["ink"]}">{html_esc(sub)}</text>')
        self.add(f'<rect x="6" y="6" width="{self.W-12:.0f}" height="{self.H-12:.0f}" fill="none" stroke="{c["ink"]}" stroke-width="2"/>'
                 f'<rect x="12" y="12" width="{self.W-24:.0f}" height="{self.H-24:.0f}" fill="none" stroke="{c["ink"]}" stroke-width="0.7"/>')

    def svg(self, interactive=False):
        self.sea()
        self.land()
        self.plains()
        self.marshes()
        self.forests()
        self.water()
        self.borders()
        self.roads()
        self.mountains()
        self.secrets_layer()
        self.labels()
        self.items()
        self.places()
        self.place_labels()
        self.furniture()
        body = "\n".join(self.out)
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.W:.0f} {self.H:.0f}" width="{self.W:.0f}" height="{self.H:.0f}">\n{body}\n</svg>\n')


def render_close(cx, cy, s, chapter, mi, title, subtitle):
    return CloseMap(cx, cy, s, chapter, mi, title, subtitle).svg()
