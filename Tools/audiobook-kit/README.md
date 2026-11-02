# Audiobook kit

Narrate a book with **Chatterbox** (Resemble AI, MIT licence), free, on your own Mac. Copy this folder next to a book's chapters, run one script, choose from a menu.

## Use

```
My Book/
    Chapters/           the chapters, as Markdown files (Chapter 01 - Title.md, …)
    audiobook-kit/      this folder, copied in
```

```
bash "My Book/audiobook-kit/audiobook.sh"
```

```
  1) Build one chapter and verify
  2) Build one chapter without verifying
  3) Build several chapters and verify
  4) Build several chapters without verifying
  5) Build the entire book and verify
  6) Build the entire book without verifying
  7) Verify chapters already built (no rendering)
  8) Audition: hear the voice on every kind of passage
  9) Setup only
 10) Put the chapter titles into chapters already built
```

Or give the choice directly: `audiobook.sh 1 7` (chapter 7, verified), `audiobook.sh 3 2-10` or `audiobook.sh 3 2,5,9` (several), `audiobook.sh 5` (the whole book), `audiobook.sh 7 all` (verify everything built).

- **Verified:** every take is checked, and retaken up to three times if a check fails. The checks are its length against its text, no long silences inside it, and its **words**: Whisper transcribes the take and compares it with the script, with names counting as matching. Each finished chapter is also checked for loudness, true peak, clipping and noise floor, and gets **PASS** or **FAIL** in `audiobook/out/NN_check.txt`.
- **Not verified:** one take per passage, no checks, faster. Chapters are marked UNCHECKED (drafts).
- **Verify chapters already built (7):** transcribes the finished MP3s and lists every place the words differ from the script, with its time in the file, plus the loudness checks; PASS or FAIL in `audiobook/out/NN_verify.txt`. Nothing is re-rendered.
- **Resuming:** several chapters and the whole book skip chapters that already passed with unchanged inputs, so stop with Ctrl-C and run the same command again.
- **Listening:** the checks find likely skips, repeats and garbles; they can't judge names, emphasis or feeling. Listen to every chapter, starting with the passages the reports flag.

The first run sets everything up (ffmpeg, Python 3.11 or 3.12, Chatterbox and Whisper in `~/chatterbox`), and the models download the first time they're used (about 3 GB and 500 MB). One setup serves every book.

## What it makes

Everything goes in `My Book/audiobook/`:

| | |
|---|---|
| `book.json` | The settings, made on the first run from what the kit can work out. Edit freely (below). |
| `reading_scripts/NN.json` | The reading script for each chapter, made from the chapter files and refreshed when a chapter changes. `00` and `99` are opening and closing credits, which say the book is read by a digital voice. |
| `out/NN.mp3` | The finished chapters (44.1 kHz MP3, loudness-normalised to about -19 LUFS), tagged with the chapter's title ("Chapter 7: The Ferry"), the book, the author and the track number, so players and stores show each chapter by name. Option 10 tags chapters built before tagging existed. |
| `out/NN_check.txt`, `out/NN_verify.txt` | The check reports. |
| `out/manifest.json` | What was built from what, and each chapter's status. |

## How chapters are read

- **Chapters:** every file matching the pattern in the chapters folder, numbered by the first number in the file name (up to 98 chapters).
- **Titles:** from the first `# ` heading ("# Chapter 7: The Ferry" is read as "Chapter Seven." … "The Ferry."). Where a new part begins, the kit also reads a part title taken from a `Part:` line inside an HTML-comment notes block.
- **Text:**
  - Paragraphs are separated by blank lines.
  - Comments, front matter, headings and Markdown marks are left out.
  - Scene breaks (`***`, `---`, `#`) get a longer pause.
  - A paragraph wholly in italics is read a little quieter and slower, as thought.
- **Names:** capitalised words that never appear in lower case count as names for the word check. For pronunciations, give a respelling file.

## book.json

```json
{
 "title": "My Book",
 "author": "A. Writer",
 "series": "",
 "chapters": "Chapters",
 "pattern": "*.md",
 "scripts": "",
 "names": "audiobook/names.csv",
 "narrator": "",
 "output": "audiobook/out",
 "credits": true
}
```

- **title**, **author** and **series** (e.g. "The Winshire Chronicles, Book Two"): read in the opening credits and written into each chapter's tags. Set them before building; the first run guesses the title from the folder's name.
- **names**: pronunciations, as a `.csv` with one `Name,Respelling` per line (e.g. `Aurveth,Orveth`), or a `.pls` lexicon with aliases. The respelling is what the narrator reads.
- **narrator**: the narrator's voice, as a clean 8–15-second WAV of one person reading plainly. The default is `audiobook-kit/voices/narrator.wav`. Keep it unchanged for a whole book: a different clip means a different narrator.
- **scripts**: a folder of ready-made reading scripts to use instead of building them from the chapters. Each script lists segments with a type, text, pause and optional mood and "how" note, which are what give the read its shaping.
- **credits**: false leaves out the opening and closing credits.

Chatterbox adds an inaudible watermark to its output (Resemble AI's Perth). Stores that accept AI narration still ask you to disclose it; the credits do, and tick the store's synthetic-narration option too.
