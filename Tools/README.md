# Tools

Scripts that build the maps and the chapter-opener art. Edit their data files and rebuild; don't edit the outputs by hand.

- **atlas/**: every map and `Bible/Atlas.md`, which `build.py` generates. `world.py` holds the geography and places; `marches_items.py` says what appears on which chapter-end map; `plan_data.py` holds Book 1's chapter numbers, POVs and titles. Run `python3 build.py` (needs `cairosvg`, `numpy` and the IM Fell English fonts). See `atlas/README.md`.
- **art/**: the abstract chapter openers, one per chapter, with no titles. `winshire_art.py` is the brush library and the first 41 compositions; `chapter_openers.py` lays out all 79 for Book 1 (odd chapters build on one circle, even chapters on three). Run `python3 art/chapter_openers.py "Book 1/Art/Chapter Openers/svg"` from the repo root, then convert to PNG.

The chapter plans (`Book 1/Chapter_Plan.md`, `Book 2/Chapter_Plan.md`, `Book 3/Chapter_Plan.md`) are maintained by hand. The old plan generator was retired once Book 1 was drafted: it no longer matched the plan, and it would have overwritten the drafted chapter files.

Book 1's maps and `Bible/Atlas.md` were rebuilt from the updated data in October 2026. Books 2 and 3 are drafted, but their art isn't made yet: they still need their own chapter-opener compositions in `art/` and their chapter-end maps (entries in `atlas/marches_items.py`). Each Book 2 and 3 plan row already names where its chapter-end map should centre (the **Ends at** column).
