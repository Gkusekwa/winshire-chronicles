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

Book 1's maps were rebuilt in October 2026.

## Books 2 and 3

The chapter-end maps for Books 2 and 3 are built from their own data modules; plain `python3 build.py` still builds only Book 1, unchanged.

- `bookdata.py`: the `Book` class (chapter table, reveals, places a book adds, story items, routes and tracks)
- `book2_items.py`, `book3_items.py`: each book's chapters (n, POV, title, Ends at, close-up centre and scale) and what's new on the map in each
- `closeup.py`: the close-up for chapters that don't end in the Marches (any centre, any scale)
- `world.py` `LATER_RIVERS`: the Glasswater's outflow to the Wend, drawn only in Books 2 and 3

Build one book's pages (SVG and 1800 px greyscale PNG per chapter, the front-matter pages and a contact sheet):

    python3 build.py --book 2 --out DIR
    python3 build.py --book 3 --out DIR --chapters 1,5,9-12 --jobs 2
