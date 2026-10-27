"""Build every atlas output from world.py: maps (SVG and PNG), Atlas.md, and the interactive page."""
import json, math, os, html
import cairosvg
import world as Wd
import marches_items as MI
from render import render

OUT = "out"
os.makedirs(OUT, exist_ok=True)

KINGDOM_TEXT = {
    "hearthmere": dict(
        land="Green, rich and well watered: chalk downs, wheat and orchards around the Mere, oak woods in the north, the Wend on its eastern border. "
             "Magic is licensed and plentiful here, more than anywhere else, and the land feels it: harvests come early, lamps burn without oil in the better streets.",
        build="Grey ragstone and slate. Towns of timber-framed houses with jettied upper floors; manor houses with walled gardens; a chapel in every village. "
              "The knightly orders build fortress-schools, chapter-houses and patrol towers along the river, square and plain, with gold-painted rolls of honour inside.",
        people="Soft-spoken, older names (Maren, Osric, Liss, Edric). Pride in the charter and in fairness, kept more on the gate than in practice."),
    "saltreach": dict(
        land="Long southern coast of bays, salt marsh and shingle; scrubland and sheep hills inland; the Marches farmland along the Wend; the Scarfell moors in the north where the Dragon Clan lives.",
        build="Ports of tarred timber and painted shutters, warehouses on stilts, chains across harbour mouths. Inland: river-stone farmhouses with turf roofs, longhouses with the byre under one roof. "
              "The Dragon Clan builds in black stone inside turf ramparts, with eyries cut into cliffs.",
        people="A league of port-cities ruled by the Tide Council at Corsa, with no king, though everyone calls it a kingdom. No knights. Trading houses, pirate captains, sellswords and outlaws in the south; farmers and drovers in the Marches; the Clan in the hills. Short, hard names in the Clan (Varr, Dag, Arn)."),
    "kessmoor": dict(
        land="Cold north-west: moorland, coal and iron in the Iron Fells, the Coldrun valley cut with canals, and the dead glass basin of the Scald where Orrin stood.",
        build="Brick and iron. Foundry chimneys, canal locks, lift-bridges, glass-roofed workshops, clock towers. Streets lit by alchemical lamps in green glass.",
        people="Guild-ranked engineers and artisans. Magic is a crime; bonded people are registered or exiled. Practical, proud, and quietly ashamed of the Scald."),
    "sarovel": dict(
        land="Warm west and south-west: vineyards and olive terraces in the Sunward Hills, the Gilt valley, the Elderwood, a sunlit coast around Solenne's bay.",
        build="White limestone, domes and colonnades; noble houses with stables for bonded beasts grander than the houses themselves; bond-crests carved over doors. The unchosen live in mud-brick quarters below the city walls.",
        people="A bond-monarchy. Status follows the bond; the unbonded are 'the unchosen'. Ornate manners, long names, beast-lords who breed and train mounts."),
    "isvaren": dict(
        land="High, cold north under the Iron Fells and the High Crown: snowfields, glacier lakes like Glasswater, the headwaters of the Wend, observatory peaks.",
        build="Slender towers of blue-grey slate joined by covered bridges; libraries cut into hillsides; each college with its own colour of lamp. Excavations everywhere, roped off and labelled.",
        people="Ruled by the high colleges. Rank follows learned magic; bond gifts are 'wild power' to be registered. College Wardens enforce the law."),
    "wyldmarch": dict(
        land="The wild east: the Thornwood's deep forest, the Hallow Plains' grass and standing stones, Lake Ysse, and the Worldsend mountains at the edge of the world.",
        build="No cities. Roundhouses of wattle and thatch, tree-platforms in the Thornwood, seasonal camps, standing stones and burial mounds. Kethra's Moot fills with tents each midsummer and empties after.",
        people="Clans under councils of elders. Beasts are kin; hunting or trading them is forbidden. Keepers protect beasts and people. Stories of Titans at the world's edge."),
}

ROAD_TEXT = {
    "The King's Road": "Stillhaven to Hallowmere to Greyhold. Paved near the capital, gravel beyond Ashford, with milestones every league and inns every six.",
    "The River Road": "The Hearthmere bank of the Wend, patrolled by the river watch and the knight schools, with towers every few leagues.",
    "The Iron Road": "Ironhythe to Hallowmere: a canal-side road with steam wagons in Kessmoor, ordinary carts once it crosses into Hearthmere.",
    "The Sun Road": "Solenne to Hallowmere through the Sunward Hills: a pilgrim and wine road, with beast-stables at every stage.",
    "The Vael Pass": "Vael to Hallowmere over the Iron Fells. Closed by snow for three months a year.",
    "The Drover's Way": "Varrhold through Harrow's End and Cotter's Cross to Wendmouth: a sheep and grain road on the Saltreach bank, rutted and unpoliced.",
    "The Coast Road": "Wendmouth, Gullhaven, Corsa and Blackwater along Saltreach's southern shore. Toll gates at every town, run by whoever holds the town.",
    "The Saltreach Track": "Cotter's Cross across the scrubland to Corsa. Two hard days without water if you miss the wells.",
    "The Oneroad": "The highway of the old realm before the split, mostly broken now: paving under turf, bridge piers in rivers, mile-stones carved in a script few can read. "
                   "It crossed the Wend at the Old Ruin. The Restoration treats it as proof that Winshire was once whole.",
}


def dist(a, b):
    return math.hypot(a["x"] - b["x"], a["y"] - b["y"])


def by(id):
    return next(p for p in Wd.P if p["id"] == id)


PAIRS = [
    ("greyhold", "oldruin"), ("greyhold", "harrowsend"), ("harrowsend", "varrhold"), ("greyhold", "millbrook"),
    ("greyhold", "ashford"), ("greyhold", "hallowmere"), ("hallowmere", "stillhaven"), ("greyhold", "wendmouth"),
    ("hallowmere", "vael"), ("hallowmere", "ironhythe"), ("hallowmere", "solenne"), ("wendmouth", "corsa"),
    ("corsa", "kethra"), ("oldruin", "hollowring"), ("varrhold", "vael"), ("solenne", "corsa"),
]


def travel_rows():
    rows = []
    for a, b in PAIRS:
        A, B = by(a), by(b)
        d = dist(A, B) * 1.25  # roads wind
        d = max(round(d * 2) / 2, 0.5)
        foot = d / Wd.TRAVEL["On foot"]
        horse = d / Wd.TRAVEL["Horse (steady)"]
        dragon_h = dist(A, B) / Wd.TRAVEL["Dragon"] * 10  # ten flying hours a day
        rows.append((A["name"], B["name"], d, foot, horse, dragon_h, round(dist(A, B) * 2) / 2))
    return rows


def fmt_days(x):
    if x < 0.2:
        h = x * 10
        return f"{max(1, round(h))} hour" + ("s" if round(h) > 1 else "")
    if x < 0.75:
        return "half a day"
    d = round(x * 2) / 2
    return (f"{d:g} day" + ("s" if d != 1 else ""))


def fmt_hours(h):
    if h < 1:
        m = round(h * 60 / 5) * 5
        return f"{max(m, 5)} minutes"
    return f"{h:.1f} hours".replace(".0 ", " ")


from plan_data import C as _PC
TITLES = [""] + [c["title"] for c in _PC]


def inner(svg):
    return svg[svg.index(">", svg.index("<svg")) + 1: svg.rindex("</svg>")]


def new_in(n):
    names = []
    for kid, ch in MI.KINGDOM_REVEAL.items():
        if ch == n: names.append(Wd.KINGDOMS[kid]["name"])
    for pid, ch in list(MI.REALM_REVEAL.items()) + list(MI.REVEAL.items()):
        if ch == n:
            nm = by(pid)["name"]
            if nm not in names: names.append(nm)
    for it in MI.ITEMS:
        if it["ch"] == n and it["name"] and it["name"] not in names: names.append(it["name"])
    return names


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;")


def compose(n):
    """One chapter-end page: all of Winshire on top, the Marches close-up below, what's new beside it."""
    FONT = "'IM Fell English', Georgia, serif"; SC = "'IM Fell English SC', Georgia, serif"
    W, H = 1601, 2400
    realm = render("realm", "ink", False, chapter=n)
    marches = render("marches", "ink", False, chapter=n, subtitle="The Marches, close up" if n else "Before the story begins")
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}"><rect width="{W}" height="{H}" fill="#fff"/>']
    out.append(f'<defs><clipPath id="clipRealm"><rect width="1601" height="1113"/></clipPath><clipPath id="clipMarches"><rect width="840" height="1200"/></clipPath></defs>')
    out.append(f'<g clip-path="url(#clipRealm)">{inner(realm)}</g>')
    # box the Marches on the world map and lead it down to the close-up
    s, x0, y0 = 4.6, -14, -12
    bx0, by0, bx1, by1 = (165 - x0) * s, (84 - y0) * s, (193 - x0) * s, (124 - y0) * s
    ix, iy, iw, ih = 40, 1150, 840, 1200
    out.append(f'<rect x="{bx0:.0f}" y="{by0:.0f}" width="{bx1-bx0:.0f}" height="{by1-by0:.0f}" fill="none" stroke="#111" stroke-width="2.4"/>')
    out.append(f'<path d="M{bx0:.0f},{by1:.0f} L{ix},{iy} M{bx1:.0f},{by1:.0f} L{ix+iw},{iy}" stroke="#111" stroke-width="1" stroke-dasharray="4 4"/>')
    out.append(f'<g transform="translate({ix},{iy})"><g clip-path="url(#clipMarches)">{inner(marches)}</g></g>')
    # caption
    tx = ix + iw + 50
    if n == 0:
        head, sub = "Winshire", "Before the story begins"
    else:
        head, sub = f"After Chapter {n}", TITLES[n]
    out.append(f'<text x="{tx}" y="{iy+60}" font-family="{SC}" font-size="44" letter-spacing="3" fill="#111">{esc(head)}</text>')
    out.append(f'<text x="{tx}" y="{iy+108}" font-family="{FONT}" font-style="italic" font-size="34" fill="#111">{esc(sub)}</text>')
    out.append(f'<path d="M{tx},{iy+140} h{W-tx-50}" stroke="#111" stroke-width="1"/>')
    y = iy + 196
    names = new_in(n)
    if names:
        out.append(f'<text x="{tx}" y="{y}" font-family="{SC}" font-size="24" letter-spacing="3" fill="#444">NEW ON THE MAP</text>')
        y += 52
        for nm in names[:16]:
            words, line, lines = nm.split(), "", []
            for w in words:
                if len(line) + len(w) > 24: lines.append(line); line = w
                else: line = (line + " " + w).strip()
            lines.append(line)
            for i, ln in enumerate(lines):
                out.append(f'<text x="{tx + (0 if i == 0 else 22)}" y="{y}" font-family="{FONT}" font-size="30" fill="#111">{"· " if i == 0 else ""}{esc(ln)}</text>')
                y += 40
            y += 6
    else:
        out.append(f'<text x="{tx}" y="{y}" font-family="{FONT}" font-style="italic" font-size="30" fill="#111">{"Nothing is named yet." if n == 0 else "Nothing new on the map."}</text>')
    out.append('</svg>')
    return "".join(out)


def write_progress():
    d = f"{OUT}/progress"
    os.makedirs(d + "/svg", exist_ok=True); os.makedirs(d + "/png", exist_ok=True)
    fm = f"{OUT}/front_matter"; os.makedirs(fm, exist_ok=True)
    s = render("realm", "ink", False, bare=True)
    open(f"{fm}/winshire_realm_bare.svg", "w").write(s)
    cairosvg.svg2png(bytestring=s.encode(), write_to=f"{fm}/winshire_realm_bare.png", output_width=3600, background_color="white")
    s = compose(0)
    open(f"{fm}/winshire_bare_page.svg", "w").write(s)
    cairosvg.svg2png(bytestring=s.encode(), write_to=f"{fm}/winshire_bare_page.png", output_width=1800, background_color="white")
    for n in range(1, len(TITLES)):
        s = compose(n)
        open(f"{d}/svg/map_after_chapter_{n:02d}.svg", "w").write(s)
        cairosvg.svg2png(bytestring=s.encode(), write_to=f"{d}/png/map_after_chapter_{n:02d}.png", output_width=1800, background_color="white")
    os.system(f'for f in {d}/png/*.png {fm}/*.png; do convert "$f" -colorspace Gray -units PixelsPerInch -density 300 "$f"; done')
    os.system(f'python3 contact.py {d}')


# ---------------- maps ----------------
def write_maps():
    for view in ("realm", "marches"):
        for style, secrets, tag in (("color", True, "author"), ("ink", False, "book")):
            svg = render(view, style, secrets)
            open(f"{OUT}/winshire_{view}_{tag}.svg", "w").write(svg)
            width = 3600 if view == "realm" else 1800
            cairosvg.svg2png(bytestring=svg.encode(), write_to=f"{OUT}/winshire_{view}_{tag}.png", output_width=width,
                             background_color="white" if style == "ink" else None)
    os.system(f'for f in {OUT}/*_book.png; do convert "$f" -colorspace Gray -units PixelsPerInch -density 300 "$f"; done')
    os.system(f'for f in {OUT}/*_author.png; do convert "$f" -units PixelsPerInch -density 300 "$f"; done')


# ---------------- atlas markdown ----------------
KIND_WORD = {"capital": "Capital", "city": "City", "town": "Town", "village": "Village", "fortress": "Fortress", "hold": "Hold",
             "ruin": "Ruin", "landmark": "Landmark", "temple": "Temple", "tower": "Tower", "farm": "Farm"}


def write_atlas():
    L = []
    L.append("# Winshire: Atlas\n")
    L.append("*A gazetteer of the world, built with the maps in `Book 1/Art/Maps/`. Everything here is a **working proposal** unless the bible marks it established; established points are noted. "
             "The maps and this file are generated from one data file, so they always agree.*\n")
    L.append("## Scale and travel\n")
    L.append("- **One league is about three miles**, roughly an hour's walk. Winshire is about **300 leagues** from the western capes to the Worldsend, and **200 leagues** from the High Crown to the Shattered Sea.")
    def sl(a, b2):
        return round(dist(by(a), by(b2)) * 2) / 2
    def rd(a, b2):
        return round(dist(by(a), by(b2)) * 1.25 * 2) / 2
    L.append(f"- The Marches, where Book 1 happens, are small. **Greyhold to the Old Ruin is {sl('greyhold','oldruin'):g} leagues** in a straight line (about {rd('greyhold','oldruin'):g} by the River Road and a boat), close enough to see the ruin from the school's river wall on a clear evening. "
             f"**Harrow's End is {sl('harrowsend','oldruin'):g} leagues** from the Ruin across the water. **Varrhold is {sl('harrowsend','varrhold'):g} leagues** north-east of Harrow's End in a straight line, {rd('harrowsend','varrhold'):g} by the Drover's Way: two days by grain cart, one by horse.\n")
    L.append("- **All distances in this atlas come from the map itself.** Straight-line distances are measured between the map points; road distances are straight lines plus a quarter, rounded to the nearest half league.\n")
    L.append("| How | Leagues a day |\n|---|---|")
    for k, v in Wd.TRAVEL.items():
        L.append(f"| {k} | {v} |")
    L.append("")
    L.append("### Distances by road\n")
    L.append("*Road distance is the straight line plus a quarter. Dragons fly the straight line; dragon times assume a steady pace, and a dragon in a hurry is faster.*\n")
    L.append("| From | To | Straight line | By road | On foot | On horseback | By dragon |\n|---|---|---|---|---|---|---|")
    for a, b, d, foot, horse, dh, s in travel_rows():
        L.append(f"| {a} | {b} | {s:g} | {d:g} | {fmt_days(foot)} | {fmt_days(horse)} | {fmt_hours(dh)} |")
    L.append("")

    L.append("## The shape of the land\n")
    L.append("- **Mountains.** The **Worldsend** runs down the whole eastern edge, the highest range in Winshire, white all year; the clans say the Titans walked there. "
             "The **High Crown** closes the north. The **Iron Fells** run south-east from the High Crown between Kessmoor and Isvaren, rich in ore. "
             "The **Scarfell** is the Dragon Clan's moorland north-east of the Marches. The **Sunward Hills** are Sarovel's vineyards.")
    L.append("- **Rivers.** The **Wend** rises in Isvaren's snows and runs south to the Shattered Sea, marking the Hearthmere–Saltreach border for its whole lower course. "
             "The **Coldrun** drains Kessmoor west through Ironhythe to Gearmouth. The **Gilt** waters Sarovel and reaches the sea at Solenne. The **Meryl** carries the Mere south to Stillhaven. "
             "The **Ysse** comes out of the Worldsend, fills Lake Ysse, and reaches the sea at Corsa. **Hollow Beck** runs from Coldtarn past Varrhold and Harrow's End into the Wend opposite the Old Ruin.")
    L.append("- **Lakes.** **The Mere** (Hearthmere's heart, shallow and wide), **Lake Ysse** (where the Wyldmarch clans hold their moot), **Glasswater** (under Vael's towers), **Coldtarn** (a black tarn above Varrhold where the Clan burns its dead).")
    L.append("- **Forests.** The **Thornwood** (the Wyldmarch's deep forest), the **Greenwold** (oak woods north of Hallowmere), the **Brackenwood** (royal hunting ground beside Greyhold), the **Elderwood** (Sarovel), the **Ashlings** (Saltreach scrub woods).")
    L.append("- **Plains, marsh and valley.** The **Hallow Plains** (Wyldmarch grassland and standing stones), the **Candle Downs** (Hearthmere's farmland), the **Saltings** (Saltreach salt marsh), the **Reedmarsh** (poachers' reed beds below Cotter's Cross), and the **Vale of the Wend**, the long river valley that is the Marches.")
    L.append("- **Seas.** The **Shattered Sea** to the south, named for the split of the old realm; the **Western Deep** beyond Kessmoor and Sarovel.\n")

    L.append("## Roads\n")
    for k, v in ROAD_TEXT.items():
        L.append(f"- **{k}.** {v}")
    L.append("")

    L.append("## The kingdoms\n")
    order = ["hearthmere", "saltreach", "kessmoor", "sarovel", "isvaren", "wyldmarch"]
    for kid in order:
        k = Wd.KINGDOMS[kid]
        t = KINGDOM_TEXT[kid]
        L.append(f"### {k['name']} *({k['status']})*\n")
        L.append(f"**Land.** {t['land']}\n")
        L.append(f"**Buildings.** {t['build']}\n")
        L.append(f"**People.** {t['people']}\n")
        ps = [p for p in Wd.P if p["kingdom"] == kid and not p["secret"] and p["scope"] != "marches"]
        if ps:
            L.append("**Places.**\n")
            for p in ps:
                c = f" *({p['canon']})*" if p["canon"] else ""
                L.append(f"- **{p['name']}** ({KIND_WORD[p['kind']].lower()}).{c} {p['desc']}")
            L.append("")

    L.append("## The Marches in detail\n")
    L.append("*Established: the border region is the Marches; a river marks the border; the Old Ruin stands on an island in it; Greyhold is on the Hearthmere bank and Calder's farm and the Clan's lands on the Saltreach side. The river's name, the Wend, and the layout below are proposals.*\n")
    ms = [p for p in Wd.P if p["scope"] in ("both", "marches") and not p["secret"]]
    ms.sort(key=lambda p: (p["y"]))
    for p in ms:
        c = f" *({p['canon']})*" if p["canon"] else ""
        L.append(f"- **{p['name']}** ({KIND_WORD[p['kind']].lower()}).{c} {p['desc']}")
    L.append("")

    L.append("## How the map grows through Book 1\n")
    L.append("*The book opens on bare maps (`front_matter/`). Each chapter closes with the Marches map as it stands after that chapter (`progress/`): everything that has appeared so far, with what is new in that chapter ringed. "
             "Events are labelled in their own chapter, then keep only their mark. Placements of plot events are working proposals tied to `Book 1/Chapter_Plan.md`; when a drafted chapter moves something, update `Tools/atlas/marches_items.py` and rebuild.*\n")
    first = {}
    for pid, ch in MI.REVEAL.items():
        first.setdefault(ch, []).append(by(pid)["name"])
    for it in MI.ITEMS:
        if it["name"]:
            first.setdefault(it["ch"], []).append(it["name"])
    for n in range(1, len(TITLES)):
        if n in first:
            L.append(f"- **Chapter {n}, {TITLES[n]}:** " + "; ".join(first[n]) + ".")
    L.append("")
    L.append("### The lived-in Marches\n")
    for it in MI.ITEMS:
        if it["name"] and it["kind"] in ("hamlet", "inn", "mill", "cave", "eyrie", "camp_plain", "area_small", "beast", "landmark_pt"):
            L.append(f"- **{it['name']}** (from Chapter {it['ch']}). {it['desc']}")
    L.append("")

    L.append("## Author's eyes only: temples and the catacombs\n")
    L.append("*Spoilers for Books 1 and 2. These never appear on a reader's map. Established: six temples, one per kingdom; Hearthmere's lies beyond the chains in the catacombs; each kingdom was founded, unknowing, over a sleeping Titan. Exact sites are proposals.*\n")
    for p in Wd.P:
        if p["secret"]:
            L.append(f"- **{p['name']}** ({Wd.KINGDOMS[p['kingdom']]['name']}). {p['desc']}")
    L.append("")
    L.append("## Open questions\n")
    L.append("- ~~Kingdom names and place names~~ *Settled (Oct 2026), as drafted: the names as used in the drafts of Books 1–3 are final.*")
    L.append("- Where did the old realm's capital stand? The Oneroad's course suggests the Marches; the Restoration believes so.")
    L.append("- ~~Which temple does the Titan reach first in Book 2?~~ *Settled (Oct 2026), as drafted: the Hollow Ring (Book 2 ch 18–20).*")
    open(f"{OUT}/Atlas.md", "w").write("\n".join(L) + "\n")


# ---------------- interactive page ----------------
def write_html():
    realm = render("realm", "color", True, interactive=True)  # gated by chapter; 42 shows everything
    marches = render("marches", "color", True, interactive=True, subtitle="Book 1, chapter by chapter")
    places = {p["id"]: dict(name=p["name"], kind=KIND_WORD[p["kind"]], kingdom=Wd.KINGDOMS.get(p["kingdom"], {"name": "The Marches"})["name"],
                            desc=p["desc"], canon=p["canon"], secret=p["secret"], x=p["x"], y=p["y"]) for p in Wd.P}
    gh = by("greyhold")
    for p in places.values():
        d = math.hypot(p["x"] - gh["x"], p["y"] - gh["y"])
        p["fromGreyhold"] = round(d * 1.25 * 2) / 2
    kingdoms = [dict(id=k, name=Wd.KINGDOMS[k]["name"], status=Wd.KINGDOMS[k]["status"], **KINGDOM_TEXT[k])
                for k in ["hearthmere", "saltreach", "kessmoor", "sarovel", "isvaren", "wyldmarch"]]
    items = {it["id"]: dict(name=it["name"] or it["desc"].split(".")[0], kind=it["kind"].replace("_", " "), ch=it["ch"], desc=it["desc"]) for it in MI.ITEMS}
    reveal = {pid: ch for pid, ch in MI.REVEAL.items()}
    rows = [dict(a=a, b=b, s=s, d=d, foot=fmt_days(f), horse=fmt_days(h), dragon=fmt_hours(dh)) for a, b, d, f, h, dh, s in travel_rows()]
    tpl = open("page.html").read()
    page = (tpl.replace("%%REALM%%", realm).replace("%%MARCHES%%", marches)
               .replace("%%PLACES%%", json.dumps(places)).replace("%%KINGDOMS%%", json.dumps(kingdoms))
               .replace("%%ROWS%%", json.dumps(rows)).replace("%%ITEMS%%", json.dumps(items)).replace("%%TITLES%%", json.dumps(TITLES)).replace("%%REVEAL%%", json.dumps(reveal)).replace("%%ROADS%%", json.dumps(ROAD_TEXT)))
    open(f"{OUT}/winshire_atlas.html", "w").write(page)


if __name__ == "__main__":
    write_maps()
    write_progress()
    write_atlas()
    if os.path.exists("page.html"):
        write_html()
    print("built")
