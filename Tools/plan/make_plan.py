import os, sys
import plan_data as P

POVN = {"S": "Maren", "F": "Calder"}
TURNS = [
    ("Teo Varr is killed; the Clan's civil war begins", 14), ("The threefold bond", 18), ("First encounter with the lion", 19),
    ("Maren fails the trial", 23), ("Calder frees the beasts at Gallows Quay", 36), ("The river freezes; the lion saves Maren", 41),
    ("The Restoration exposes Hearthmere's secret", 45), ("Hale confirms the chains", 49), ("Calder finally speaks: the chain", 50),
    ("Maren breaks her oath", 63), ("The twins are revealed; Calder overhears", 68), ("The first war breaks out", 69),
    ("The lion bond forms", 73), ("One twin dies; the seal opens", 77), ("Maren and Calder meet", 78), ("The Last Titan flies", 79),
]

L = []
L.append("# Winshire — Book 1 Chapter Plan (working draft)\n")
L.append("*The full-length plan for Book 1, built from the established canon in the other notes. Every beat that isn't established canon is a working proposal. Each chapter's draft status is kept in its own file's notes (Status:).*\n")
L.append("## Shape\n")
L.append("- **79 chapters in six parts, across one year:** late summer to the next summer's war. **No upper word limit**; chapters run as long as their scenes need, roughly 3,500–5,000 words, so the book will land somewhere above **300,000 words**.")
L.append("- **Strictly alternating chapters** *(established)*: odd chapters follow Maren (S), even chapters Calder (F).")
L.append("- **Echoes** *(established)*: each chapter picks up something from the other's story (the Echo column). The reader always knows more than either protagonist, until they meet.")
L.append("- **The arcs converge only at the end:** they meet underground after the seal opens (chapter 78).")
L.append("- **Room to breathe:** the length comes from people and place, not padding: Teo and the three warriors alive before they die; Bel and Joss; Tam, Tobin, Haverly and Pell; Hale's slow trust; a whole winter on a frozen river; the lion earned one meeting at a time.\n")
L.append("## The major turns\n")
L.append("| Turn | Chapter |\n|---|---|")
for t, n in TURNS:
    L.append(f"| {t} | {n} ({P.C[n-1]['pov']}) |")
L.append("")
L.append("---\n")
for name, season, a, b in P.PARTS:
    L.append(f"## {name} (chapters {a}–{b})\n")
    L.append(f"*{season}.*\n")
    L.append("| Ch | POV | Working title | What happens | Echo of the other's story |\n|---|---|---|---|---|")
    for c in P.C[a-1:b]:
        L.append(f"| {c['n']} | {c['pov']} | {c['title']} | {c['beats']} | {c['echo']} |")
    L.append("")
L.append("---\n")
L.append("## Threads that run the whole book\n")
L.append("- **Calder's chain** (2 → 50): the cut beast chain he pockets on the first night and tells no one about, until Joss is dead. His arc from keeping quiet to choosing is carried by one object.")
L.append("- **Teo** (4, 6, 8, 12 → 14): the reader likes him before he dies, so the civil war hurts.")
L.append("- **The three warriors** (6, 8 → 18): Sigrun, Dag and Imra alive and particular, so their dragons' grief has faces.")
L.append("- **Rook** (10 → 58 → 68 → 72): the stranger in Ulric's hall. Calder suspects him in 58, overhears the truth in 68, and the proof dies with Rook in 72, so the truth must wait for Book 2.")
L.append("- **The two leaders** (5, 33, 34, 57 → 68): Maren sees the precise one (Corvin) at Ferriby; Calder hears the warm one (Cassian) in Wendmouth; Maren hears the warm one in 57 and explains the difference away. Readers who notice are rewarded in 68.")
L.append("- **Tobin** (9, 47, 57 → 71): the unbonded friend the Restoration wins. The unchosen have a real grievance.")
L.append("- **Haverly and Kesh** (1, 9, 27, 61 → 75): rival, then respect; his death shows Maren the one-life bond from the inside just before she goes down to the lock.")
L.append("- **Pell** (1, 5, 9 → 69): subdue, don't kill; he dies doing his duty.")
L.append("- **Liss's ferry** (1, 3, 22, 27, 31 → 64): the only thing that crosses. In 64 it carries Calder's family, so the two stories touch through the mothers before the leads meet.")
L.append("- **Hale** (25, 35, 37, 49, 51 → 75): kindness and the secret; his key gets Maren underground.")
L.append("- **The river** (1, 3, 11 → 41–44 → 55): forbidden island, frozen crossing, thaw.")
L.append("- **The lion** (15, 17, 19, 21, 23, 29, 41, 53, 55 → 73): earned one meeting at a time, by courage and restraint, until the sacrifice.\n")
L.append("## Pacing notes\n")
L.append("- **Mirrors:** 7 and 36 (each frees caged beasts); 18 and 19 (the threefold bond, then the lion's roar); 33 and 34 (each sees one leader); 41 and 42 (each crosses the frozen river); 74 and 77 (each fights at a lock).")
L.append("- **Echoes build to the meeting.** Glimpses in Part One; rumours in Parts Two and Three; footprints and a warm scale in Part Four; the families meet on the ferry in Part Five; the warning, then the meeting, in Part Six.")
L.append("- **Quiet stretches:** Part Three and early Part Five are where the bonds grow. Keep them full of small, specific scenes.")
L.append("- **Maren kills a man in chapter 77.** Subdue-don't-kill training (9), the failed trial (23), Pell's death (69) and Haverly's (75) all lead to the one moment where restraint isn't possible.")
L.append("- **The civil war never resolves** in Book 1: every Calder chapter shows its damage, with no winner.")
L.append("- **Reveal rules:** the leader is one man until chapter 68; the Last Titan is only legend until 45; the gods are only faith; no other Titans; the Restoration's part in Teo's death is only suspicion until 68.\n")
L.append("## Proposed answers to the open questions *(working proposals)*\n")
L.append("1. **Wren** stays with Ada after the bond (22, 24); she is the one person not afraid of the dragons (22, 56); she crosses to Hearthmere on Liss's ferry (64). **Why Calder stays while his family flees (62):** the Restoration is hunting him, so distance is what keeps her safe.")
L.append("2. **Why Maren never set foot on the island:** it's forbidden to the river watch by law and avoided by river folk by custom (3, 11).")
L.append("3. **The killer** was **Rook**, a Restoration agent who joined Ulric's men as a hired hand (10, 58, 68, 72).")
L.append("4. **Who sees the twins:** only Calder (68). **Maren knows there are two** before she kills Cassian. Lisska can't speak to her (no bond), so Calder sends what he can: the cut chain, a strip of cloth with TWO burned into it, and Wren's ribbon, which Maren recognises from her mother's story (64, 65, 70, 73).")
L.append("5. **Climax logistics:** the lion is trapped at the edge of the Brackenwood, a short run from Greyhold (73). Greyhold is breached (75), and the dying Hale gives Maren the cellar key, so a cast-out student gets underground. Calder falls into the catacombs when the Ruin's floor gives way (76). Both reach the meeting from opposite ends (78).")
L.append("6. **They meet** as wary strangers who already owe each other: his warning, her name in the ferrywoman's story.")
L.append("7. **No prologue.** A prologue about the Titan would break the reveal in 45. The book opens on the river.\n")
L.append("## Open\n")
L.append("- Supporting names still proposed (see `Characters.md`): Tobin, Pell, Hob, Rook, Captain Idris Vey, the Darrow girl (Liss, Tam, Bel, Wren and the family names are established).")
L.append("- **Settled:** Maren's rival is **Lucan Haverly**, renamed from Corwin Brandt, which was too close to Corvin Vale.")
L.append("- Exact length of each chapter: set by the scenes, not a target.")
open(sys.argv[1], "w").write("\n".join(L) + "\n")

# chapter scaffolds
out = sys.argv[2]
os.makedirs(out, exist_ok=True)
for c in P.C:
    part = next(p[0] for p in P.PARTS if p[2] <= c["n"] <= p[3])
    fn = f"Chapter {c['n']:02d} - {c['title'].replace('?', '')}.md"
    body = (f"# Chapter {c['n']}: {c['title']}\n\n<!-- notes\nPOV: {POVN[c['pov']]}\nPart: {part}\nBeats: {c['beats']}\n"
            f"Echo of the other's story: {c['echo']}\nStatus: not started\nnotes -->\n\n---\n\n")
    open(os.path.join(out, fn), "w").write(body)
print("ok")
