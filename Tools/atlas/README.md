# Atlas

Builds every map, the interactive atlas page and the gazetteer. `build.py` generates `Atlas.md` (in `out/`, with the maps), and that file is `Bible/Atlas.md`: never edit it by hand. To change the Atlas, edit the data or the text here and rebuild.

- `world.py`: geography and places
- `marches_items.py`: what appears in which chapter (Marches detail and whole-Winshire names)
- `plan_data.py`: Book 1's chapter numbers, POVs and titles
- `build.py`: the Atlas.md text, the maps and the page

Rebuild every map and Atlas.md:

    pip install cairosvg numpy
    python3 build.py

Needs the IM Fell English fonts installed for PNG labels.

Book 1's maps were rebuilt in October 2026. Books 2 and 3 have no chapter-end maps yet: they need their own entries in `marches_items.py` (and `plan_data.py`) when their art is made.
