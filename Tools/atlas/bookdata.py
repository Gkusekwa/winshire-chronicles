"""Shared machinery for the chapter-end maps of Books 2 and 3.

A Book holds everything render.py reads from Book 1's marches_items (REVEAL, ITEMS, REALM_REVEAL ...), plus:
  CH            the chapter table: n, POV, title, Ends at, and the close-up (centre, scale, cartouche);
  EXTRA_PLACES  places this book names that world.py doesn't have (positions are working proposals);
  SECRET_REVEAL temples and other secret places, from the chapter that reveals them;
  HIDE          places that stop being drawn from a chapter on (the Old Ruin, Greyhold's fallen hill);
  REALM_ITEMS   True: some items (marked realm=True) are drawn on the whole-Winshire map too.
Chapter 0 is the book's front-matter page: everything known at the end of the book before.
"""
import copy
import world as Wd

MARCHES = "M"          # scale code: the Marches view itself (render.py), 30 px a league


class Book:
    LATER = 999

    def __init__(self, number, name):
        self.BOOK = number
        self.NAME = name
        self.REVEAL, self.ROAD_REVEAL, self.LABEL_REVEAL = {}, {}, {}
        self.AMBIENT, self.ITEMS, self.EXTRA_PLACES = [], [], []
        self.REALM_REVEAL, self.KINGDOM_REVEAL, self.REALM_LABEL_REVEAL, self.REALM_ROAD_REVEAL = {}, {}, {}, {}
        self.SECRET_REVEAL, self.HIDE = {}, {}
        self.BORDER_REVEAL = 0
        self.CATACOMBS_CH = 0
        self.ISLAND = False
        self.EDDY = (175.8, 103.5)
        self.REALM_ITEMS = True
        self.EXTRA_RIVERS = dict(Wd.LATER_RIVERS)
        self.CH = {}
        self.TITLES = [""]

    # ---------------- start state ----------------
    def start_from_book1(self, MI):
        """Book 2 opens on everything Book 1 put on the map. Book 1's events stay in Book 1; its places,
        roads, labels, farmsteads and the lived-in Marches (hamlets, inns, the Roosts, Teo's ford...) carry on."""
        L1 = MI.LATER
        self.REVEAL = {k: 0 for k in MI.REVEAL}
        self.ROAD_REVEAL = {k: 0 for k in MI.ROAD_REVEAL}
        self.LABEL_REVEAL = {k: 0 for k in MI.LABEL_REVEAL}
        self.AMBIENT = [(x, y, 0) for (x, y, c) in MI.AMBIENT]
        self.REALM_REVEAL = {k: 0 for k, v in MI.REALM_REVEAL.items() if v < L1}
        self.KINGDOM_REVEAL = {k: 0 for k, v in MI.KINGDOM_REVEAL.items() if v < L1}
        self.REALM_LABEL_REVEAL = {k: (0 if v < L1 else self.LATER) for k, v in MI.REALM_LABEL_REVEAL.items()}
        self.REALM_ROAD_REVEAL = {k: (0 if v < L1 else self.LATER) for k, v in MI.REALM_ROAD_REVEAL.items()}

    def start_from(self, prev):
        """Book 3 opens on everything Book 2 put on the map (its places and lasting marks, not its events)."""
        last = max(prev.CH)
        def known(d):
            return {k: (0 if v <= last else self.LATER) for k, v in d.items()}
        for name in ("REVEAL", "ROAD_REVEAL", "LABEL_REVEAL", "REALM_REVEAL", "KINGDOM_REVEAL",
                     "REALM_LABEL_REVEAL", "REALM_ROAD_REVEAL", "SECRET_REVEAL"):
            setattr(self, name, known(getattr(prev, name)))
        self.HIDE = {k: 0 for k, v in prev.HIDE.items() if v <= last}
        self.AMBIENT = [(x, y, 0) for (x, y, c) in prev.AMBIENT if c <= last]
        self.EXTRA_PLACES = [dict(p) for p in prev.EXTRA_PLACES if p["id"] not in self.HIDE or True]
        for it in prev.ITEMS:
            if it.get("carry") and it["ch"] <= last and (it.get("until") is None or it["until"] >= last):
                c = dict(it, ch=0, keep=True)
                c.pop("until", None)
                self.ITEMS.append(c)

    # ---------------- builders ----------------
    def place(self, id, name, kind, kingdom, x, y, ch, desc, scope="realm", secret=False, ldx=0, ldy=0, canon=""):
        """A place this book names that world.py doesn't have. scope: realm (both maps), local (close-ups only)."""
        p = dict(id=id, name=name, kind=kind, kingdom=kingdom, x=x, y=y, desc=desc, scope=scope, secret=secret,
                 ldx=ldx, ldy=ldy, canon=canon or f"proposal, Book {self.BOOK}")
        self.EXTRA_PLACES.append(p)
        if secret:
            self.SECRET_REVEAL[id] = ch
        elif scope in ("realm", "both"):
            self.REALM_REVEAL[id] = ch
            self.REVEAL[id] = ch
        else:
            self.REVEAL[id] = ch
        return p

    def item(self, id, name, kind, x, y, ch, desc, label=True, path=None, dx=0.0, dy=0.0, realm=False, until=None,
             size=1.0, keep=False, carry=False, views=None, weight=1.0, head=True, pov=None):
        assert not any(i["id"] == id for i in self.ITEMS), id
        it = dict(id=id, name=name, kind=kind, x=x, y=y, ch=ch, desc=desc, label=label, path=path, dx=dx, dy=dy,
                  realm=realm, until=until, size=size, keep=keep, carry=carry, views=views, weight=weight, head=head, pov=pov)
        self.ITEMS.append(it)
        return it

    def line(self, id, name, kind, ch, pts, desc, realm=True, until=None, label=False, at=None, **kw):
        """A track (the Titan's road), a route (a POV's journey), a wall, a road or a sea-lane."""
        if at is None:
            at = pts[len(pts) // 2]
        return self.item(id, name, kind, at[0], at[1], ch, desc, label=label, path=pts, realm=realm, until=until, **kw)

    def chapter(self, n, pov, title, ends, at, scale, ctitle, sub, free=False):
        """free: the close-up may run off the edge of Winshire (the far shore, the open sea)."""
        self.CH[n] = dict(n=n, pov=pov, title=title, ends=ends, at=at, s=scale, ctitle=ctitle, sub=sub, free=free)
        while len(self.TITLES) <= n:
            self.TITLES.append("")
        self.TITLES[n] = title

    def set(self, id, **kw):
        for it in self.ITEMS:
            if it["id"] == id:
                it.update(kw)
                return it
        raise KeyError(id)

    def finish_routes(self, linger=1):
        """A route stays on the map until the same traveller's next route appears, and a few chapters after."""
        by = {}
        for it in self.ITEMS:
            if it["kind"] == "route" and it.get("pov") and it["until"] is None:
                by.setdefault(it["pov"], []).append(it)
        for pov, its in by.items():
            its.sort(key=lambda i: i["ch"])
            for a, b in zip(its[:-1], its[1:]):
                a["until"] = max(b["ch"] + linger - 1, a["ch"] + 1)
            its[-1]["until"] = its[-1]["ch"] + 3

    # ---------------- what's new ----------------
    def all_places(self):
        return Wd.P + self.EXTRA_PLACES

    def new_in(self, n):
        names = []
        def add(nm):
            if nm and nm not in names:
                names.append(nm)
        for kid, ch in self.KINGDOM_REVEAL.items():
            if ch == n:
                add(Wd.KINGDOMS[kid]["name"])
        byid = {p["id"]: p for p in self.all_places()}
        for d in (self.REALM_REVEAL, self.REVEAL, self.SECRET_REVEAL):
            for pid, ch in d.items():
                if ch == n and pid in byid and not (pid in self.HIDE and self.HIDE[pid] <= n):
                    add(byid[pid]["name"])
        for it in self.ITEMS:
            if it["ch"] == n and it["name"] and not it.get("quiet"):
                add(it["name"])
        return names
