# Covers

*Settled by the author, Oct 2026.* The trilogy is released in **three editions**, and each edition has its own art. All of the art is kept. Which edition goes out first is to be decided later.

| Edition | Look | Book 1 *The Watch Below* | Book 2 *The Hunt Beneath* | Book 3 *The Titan War* |
|---|---|---|---|---|
| **Bone** | Black ink on bone; the title above the art | the island and its tower stump inside the broken seal, the spined back asleep under the river | the great shape high in the east, its road falling west, one temple lit, beasts fleeing | six chains rising into the light from a back in the sea, the third broken |
| **Night** | Bone ink on black; the title below the art, gold rule | a crescent moon on the river, ridges just breaking the water, one watcher with a lamp | the stars put out where the shape passes, a ruin burning, beasts streaming west | a great chain standing out of the sea, its middle link split open, camp fires on both shores |
| **Band** | A colour band per book with the title reversed out; ink on bone below | the broken ring with the bars inside it, one bar bent out | one temple gate lit inside, the road across the sky behind it, beasts pouring through | the ring of six joined by chain, one broken, Maren's ring and Calder's triad together at the centre |

Band colours: Book 1 `#1F3D3B` (river green), Book 2 `#6B2A1A` (ember), Book 3 `#222B45` (deep blue). Type is IM Fell English SC throughout; the author line reads *Goodluck Kusekwa*.

Every cover carries Maren's ring (west) and Calder's triad (east), as the chapter openers do.

## Files

- `Bone/`, `Night/`, `Band/`: the finished covers, 1600 × 2560 JPG, ready for upload to the ebook stores.
- `Art/bone`, `Art/night`, `Art/band`: the cover art alone, as SVG (1600 × 1760 panels).
- `Art/archive`: the first Night proofs, which used the Bone art in bone ink. They are kept, not used.
- `contact_sheet.png`: all nine side by side.

## Rebuilding

The art comes from `Tools/art/covers.py`; the layouts are in `Tools/art/cover_layouts/` (also on the covers canvas, *Winshire Chronicles covers: three editions*).

```
python3 Tools/art/covers.py Covers/Art
npm i @fontsource/im-fell-english @fontsource/im-fell-english-sc playwright
node Tools/art/cover_layouts/render.js
```

The Bone art in `covers.py` is the approved art: change it only on purpose.
