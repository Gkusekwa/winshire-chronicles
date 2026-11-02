# Audiobook kit

Turn a book's chapters into an audiobook, free, on your own Mac: the kit writes the reading scripts (who says each line, how, and the mood of each paragraph), then narrates them with **Chatterbox** (Resemble AI, MIT licence) and checks every take.

## Use

Point the kit at a book's folder, the one that holds its `Chapters/`:

```
bash Tools/audiobook-kit/audiobook.sh --book "Book 2"
```

Or copy the `audiobook-kit` folder next to a book's `Chapters/` and run `bash "My Book/audiobook-kit/audiobook.sh"`.

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

Or give the choice directly: `... 1 7` (chapter 7, verified), `... 3 2-10` or `... 3 2,5,9` (several), `... 5` (the whole book), `... 7 all` (verify everything built).

- **Verified:** every take is checked, and retaken up to three times if a check fails. The checks are its length against its text, no long silences inside it, and its **words**: Whisper transcribes the take and compares it with the script, with names counting as matching. Each finished chapter is also checked for loudness, true peak, clipping and noise floor, and gets **PASS** or **FAIL** in `audiobook/out/NN_check.txt`.
- **Not verified:** one take per passage, no checks, faster. Chapters are marked UNCHECKED (drafts).
- **Verify chapters already built (7):** transcribes the finished MP3s and lists every place the words differ from the script, with its time in the file, plus the loudness checks; PASS or FAIL in `audiobook/out/NN_verify.txt`. Nothing is re-rendered.
- **Resuming:** several chapters and the whole book skip chapters that already passed with unchanged inputs, so stop with Ctrl-C and run the same command again.
- **Listening:** the checks find likely skips, repeats and garbles; they can't judge names, emphasis or feeling. Listen to every chapter, starting with the passages the reports flag.

The first run sets everything up (ffmpeg, Python 3.11 or 3.12, Chatterbox and Whisper in `~/chatterbox`), and the models download the first time they're used (about 3 GB and 500 MB). One setup serves every book.

To make or refresh the scripts without narrating anything: `python3 Tools/audiobook-kit/kit/prepare.py --book "Book 2" --check` (`--check` confirms every word of every chapter is in its script). Every build does this first.

## What it makes

Everything goes in the book's `audiobook/` folder. The first three are yours to correct; the kit keeps your changes.

| | |
|---|---|
| `book.json` | The settings (below), made on the first run from what the kit can work out. |
| `annotations/chNN.json` | For every quote and italic in the chapter: what kind of words it is, who says it and how. For the paragraphs that need one: a mood. Made by the kit where missing; correct them by hand. |
| `Lexicon.csv` | The names: Name, Respelling (what the narrator reads), Say (a guide such as OR-veth), IPA, Notes. The kit adds names it finds; fill in a respelling for any the narrator gets wrong. |
| `Performance/NN.json` | The reading scripts, one per chapter: the titles, then every paragraph as segments with type, speaker, delivery, mood and pause. Remade whenever a chapter or its annotations change. `00` and `99` are the opening and closing credits. |
| `out/NN.mp3` | The finished chapters (44.1 kHz MP3, loudness-normalised to about -19 LUFS), tagged with the chapter's title ("Chapter 7: The Ferry"), the book, the author and the track number. |
| `out/NN_check.txt`, `out/NN_verify.txt`, `out/manifest.json` | The check reports, and what was built from what with each chapter's status. |

## The chapters

- Every file matching the pattern in the chapters folder is a chapter, numbered by the first number in its name (up to 98).
- **Titles** come from the first `# ` heading: "# Chapter 7: The Ferry" is read "Chapter Seven." then "The Ferry.", with a pause after each. Where a new part begins, its title is read first, from a `Part:` line in the chapter's notes (an HTML comment): `Part: Part One: Two Banks` is read "Part One. Two Banks."
- **Text:** paragraphs are separated by blank lines; comments, front matter, headings and Markdown marks are left out; `---`, `***` or `* * *` alone on a line is a scene break (a longer pause); a paragraph in `>` blockquote is written words.

## Annotations: who, how and what mood

```json
{"chapter": 7, "pov": "Maren", "auto": true,
 "spans": {"s1": "speech:Pell", "s2": "bond:Aurveth>Calder|very quietly", "s3": "thought:Maren", "s4": "emphasis"},
 "paragraphs": {"p4": "tension", "p9": "grief|after the burial"}}
```

- **spans:** one entry per quote and italic, numbered through the chapter (s1, s2, …), as `type:speaker>listener|how`. Only the type is needed. Types: `speech`, `bond` (mind-to-mind speech), `thought`, `remembered`, `written`, `verse`, `emphasis`, `term`.
- **paragraphs:** a mood for the paragraphs that need one (p1, p2, … in order), with an optional note after `|`. Moods: action, tension, dread, quiet, reflective, tender, grief, humour, anger, urgent, awe. Most paragraphs need none.
- **"auto": true** marks a file the kit made, which it remakes when its chapter changes. Delete that line once you've corrected the file, and the kit keeps it, only filling in quotes or italics added later (and saying so).

**What the kit decides on its own** (`kit/directions.py`):
- Quotes are speech. A **how** note comes from the narration around the quote: the verb (whispered, shouted, murmured, hissed, called) and the manner (quietly, softly, her voice cracking).
- Italics are emphasis when short and inside a sentence; thought, remembered or written words when the sentence says so ("she thought", "he had said", "it read"); verse when several italic lines follow one another; italic lines with "said" are speech, or bond speech when book.json says `"italics": "bond"`; anything else is thought.
- **Moods** are given only where the words leave little doubt (grief: wept, buried, mourned; action: struck, hurled, screamed; humour: laughed, grinned), so most paragraphs stay plain narration. Tested against Book 1 of the Winshire Chronicles, whose annotations are hand-made, the kit types 99% of quotes correctly, but moods only 1 paragraph in 50 (a quarter of them exactly as the hand did). Hand-made moods follow the scene, not just its words, so for a book that deserves the full performance, go through the annotations and add the moods.

## How emotion is carried

Chatterbox has no emotion labels. It copies the tone of the narrator's clip and has two settings: **exaggeration** (how much feeling) and **cfg weight** (lower is slower and more deliberate). Most of the expression comes from the model reading the sentence itself. The scripts add four things:

1. **Mood** sets both settings for the paragraph: none 0.50 / 0.50; quiet 0.40 / 0.45; tender 0.50 / 0.40; tension 0.60 / 0.50; awe 0.60 / 0.35; grief 0.70 / 0.30; urgent 0.75 / 0.55; anger 0.80 / 0.40.
2. **How** notes adjust them: "shouted" adds feeling and 3 dB; "whispered" takes feeling off and 6 dB; "voice cracking" adds feeling, a little quieter. The total stays between 0.25 and 1.0.
3. **The kind of words** changes volume and speed after rendering: thought and remembered words -4.5 dB at 97%; bond speech -3 dB at 95%; written words and verse -1 dB at 94–95%. A paragraph that mixes kinds is read as narration.
4. **Silence:** 0.5 s between paragraphs, 0.8 s after grief, dread, awe and tension, 1.6 s at a scene break.

One voice reads every character; each paragraph is read whole, so dialogue keeps its flow.

## book.json

```json
{
 "title": "My Book",
 "author": "A. Writer",
 "series": "",
 "next": "",
 "copyright": "2026",
 "italics": "thought",
 "chapters": "Chapters",
 "pattern": "*.md",
 "scripts": "",
 "names": "audiobook/Lexicon.csv",
 "narrator": "",
 "output": "audiobook/out",
 "credits": true
}
```

- **title**, **author**, **series** (e.g. "The Winshire Chronicles, Book Two"), **next** (the book that follows) and **copyright** (the year): read in the opening and closing credits, and written into each chapter's tags. Set them before building; the first run guesses the title from the folder's name.
- **italics**: what italic speech with "said" is: `thought`, or `bond` for mind-to-mind speech.
- **names**: the lexicon (`Lexicon.csv`, or a `.pls` lexicon with aliases).
- **narrator**: the narrator's voice, as a clean 8–15-second WAV of one person reading plainly. The default is `audiobook-kit/voices/narrator.wav`. Keep it unchanged for a whole book: a different clip means a different narrator.
- **scripts**: a folder of ready-made reading scripts to read as they are, instead of making `Performance/`.
- **credits**: false leaves out the opening and closing credits.

Chatterbox adds an inaudible watermark to its output (Resemble AI's Perth). Stores that accept AI narration still ask you to disclose it; the credits do ("Narrated by a digital voice"), and tick the store's synthetic-narration option too.
