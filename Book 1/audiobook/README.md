# The Watch Below: audiobook

Production files for the audiobook of *The Watch Below*, Winshire Chronicles Book One: 79 chapters plus opening and closing credits, about 302,000 words (roughly 32 to 34 hours of audio). It is narrated with the audiobook kit (`Tools/audiobook-kit/`), using Chatterbox, with Emma reading everything.

**The reading scripts are generated from the manuscript.** Never edit them by hand. Edit the chapters, the annotations or the names, then rebuild:

```
cd Tools/audiobook
python3 build.py --check      # rebuilds the scripts and confirms every spoken word matches the manuscript
```

If a chapter's text changes, its paragraph and span numbering can shift. `python3 check_annotations.py` lists any spans that need annotating again.

## What's here

| File | What it is |
|---|---|
| `book.json` | The kit's settings for this book: title, author, series, the ready-made scripts in `Performance/`, the names in `Lexicon_Alias.pls`, output in `out/`. |
| `Narration_Guide.md` | How the book is read: the five kinds of words (narration, speech, bond speech, thought, written words and verse), directions, pauses. |
| `Pronunciation_Guide.md` | Invented names with a respelling and IPA. The names that could be said more than one way are marked *settled* (Nov 2026). Use it when listening. |
| `Lexicon_Alias.pls` | The respellings the narrator reads (e.g. Aurveth as Orveth). |
| `annotations/chNN.json` | The source of the performance: the speaker and kind of every quoted or italic span, and a direction where a paragraph needs one. |
| `Performance/NN.json` | Each chapter as a sequence of segments with type, speaker, delivery and pause, titles included. This is what the kit reads. `00` and `99` are the opening and closing credits. |
| `out/` | The finished chapters (`NN.mp3`), check reports and `manifest.json`. Kept out of git. |

## Narrating

From Terminal, in the project folder:

```
bash Tools/audiobook-kit/audiobook.sh --book "Book 1"
```

The menu offers one chapter, several chapters, or the whole book, each **verified** or **not verified**. It can also verify chapters already built (7), play an audition (8), run setup (9) and put the chapter titles into files already built (10). Or give the choice directly: `... --book "Book 1" 1 7` (chapter 7, verified), `... 3 2-10`, `... 5` (the whole book), `... 7 all`. The kit's README (`Tools/audiobook-kit/README.md`) explains the checks, PASS, FAIL and UNCHECKED, resuming and the tags.

- **What Book 1 adds over a plain book:** the annotated scripts. Each paragraph's mood and "how" note set the emotion intensity, and bond speech, thoughts, remembered words, verse and written words are read a little quieter or slower. The names are respelt from `Lexicon_Alias.pls`.
- **The narrator's voice** is `Tools/audiobook-kit/voices/narrator.wav`, a 9.6-second clip of Emma (24 kHz mono; SHA-256 `9223a4ccbd883afe1a20f6e02f68bf6a570cdf10fa7040b632dbba46d8348767`). It was made with the Kokoro-82M model (Apache 2.0, voice `bf_emma`) reading two neutral lines. Every render clones this clip, so keep it unchanged and backed up: a different clip gives a different narrator. Like all audio, it is kept out of git.
- **Listening:** the checks find likely skips, repeats and garbles. They don't replace listening and proofreading: names, emphasis and feeling need an ear, starting with the passages the reports flag.
- Chatterbox adds an inaudible watermark (Resemble AI's Perth) to its output.

## Where it can be published

See `Publishing.md`. In short: Google Play Books and Kobo accept uploaded AI-narrated audio, and so do direct sales. Spotify and INaudio take AI narration only from providers they name. Audible (ACX) doesn't accept AI narration made outside Amazon. Check each one's current terms, exclusivity and AI-disclosure rules before choosing; these routes change often.
