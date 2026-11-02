# The Watch Below: audiobook

Production files for the audiobook of *The Watch Below*, Winshire Chronicles Book One: 79 chapters plus opening and closing credits, about 302,000 words (roughly 32 to 34 hours of audio).

**Everything here is generated from the manuscript.** Never edit the scripts by hand. Edit the chapters, the annotations, the names or the cast, then rebuild:

```
cd Tools/audiobook
python3 build.py --check      # rebuilds everything and confirms every spoken word matches the manuscript
```

If a chapter's text changes, its paragraph and span numbering can shift. `python3 check_annotations.py` lists any spans that need annotating again.

## What's here

| File | What it is |
|---|---|
| `Narration_Guide.md` | How to read the book: the five kinds of words (narration, speech, bond speech, thought, written words and verse), directions, pauses. |
| `Cast.md` | Every voiced role, with gender, age, line count and voice notes. A single narrator uses it as character notes. |
| `Pronunciation_Guide.md` | Invented names with a respelling and IPA. The names that could be said more than one way are marked *settled* (Nov 2026). |
| `Lexicon_IPA.pls`, `Lexicon_Alias.pls` | The same names as standard pronunciation lexicons: IPA (Amazon Polly, Azure) and alias spellings (Chatterbox and others). |
| `annotations/chNN.json` | The source of the performance: the speaker and kind of every quoted or italic span, and a direction where a paragraph needs one. |
| `Performance/NN.json` | Each chapter as a sequence of segments with type, speaker, listener, delivery and pause. This is what Chatterbox reads. |
| `Scripts/*.ssml` | Standard SSML 1.1 for one narrator. Bond speech, thoughts, verse and written words get gentle prosody; paragraphs with a direction get a slight rate change; pauses are explicit, never over 3 s. Comments name the speaker of each paragraph. |
| `Variants/google/` | SSML with names respelt inline, for engines without lexicon support. |
| `Variants/azure/` | SSML wrapped in an Azure voice element (rebuild with `--variant azure --voice NAME` to change the voice). |
| `Chatterbox/` | The narration: Chatterbox renders, the narrator's reference clip and the anomaly-check lists (below). |

## Narration: Chatterbox

The audiobook is narrated with **Chatterbox** (Resemble AI, MIT licence), run locally on the author's Mac: free, and offline after the first download. Emma narrates everything.

- **Run it** from Terminal in the project folder: `bash Tools/audiobook/chatterbox_mac.sh` renders the audition set (passages of every kind from across the book); `bash Tools/audiobook/chatterbox_mac.sh 1` renders chapter 1; `bash Tools/audiobook/chatterbox_mac.sh 1-79 --skip-done` renders the book, skipping chapters already done and current. The first run sets up Python 3.11 or 3.12, `chatterbox-tts` 0.1.7 and the model (about 3 GB). It uses the Mac's graphics chip, renders at about a third of real time, and keeps the Mac awake.
- **What it reads:** `Performance/NN.json`, titles included. Each paragraph is read whole, so short quoted lines keep their flow; long paragraphs are split at sentence ends (about 200 characters). Each paragraph's mood and "how" note set the emotion intensity. Names are respelt from `Lexicon_Alias.pls`.
- **The narrator's voice** comes from `Chatterbox/refs/Narrator.wav`, a 9.6-second clip of Emma (24 kHz mono; SHA-256 `9223a4ccbd883afe1a20f6e02f68bf6a570cdf10fa7040b632dbba46d8348767`). It was made with the Kokoro-82M model (Apache 2.0, voice `bf_emma`) reading two neutral lines. Every render clones this clip, so keep it unchanged and backed up: a different clip gives a different narrator. Like all audio, it is kept out of git.
- **Automatic anomaly check:** each take's length is compared with what its text should take, and long silences inside it are looked for. A take that looks wrong (often a skip, a repeat or a stall) is made again, up to three tries, and anything still doubtful is listed in `Chatterbox/out/NN_check.txt`. It can't hear whether the words or names are right: **listening and proofreading are the quality check**, starting with the passages marked STILL DOUBTFUL. Higher emotion intensity can also speed the voice up, so listen for pacing as well as feeling.
- **Resume:** `Chatterbox/out/manifest.json` fingerprints each chapter's inputs (script, renderer, name respellings, cast map, narrator clip, options), so `--skip-done` re-renders a chapter whenever any of them has changed.
- Chatterbox adds an inaudible watermark (Resemble AI's Perth) to its output.
- Audio goes to `Chatterbox/out/`, ignored by git.

## Where it can be published

- **Audible (ACX)** doesn't accept AI narration made outside Amazon. Amazon's own **Virtual Voice** (through KDP) narrates the published ebook itself and doesn't use these files.
- **Spotify** (through Spotify for Authors / Findaway Voices): check whether it accepts AI narration made elsewhere.
- **Google Play Books** accepts uploaded AI-narrated audio.

Check each one's current terms, exclusivity and AI-disclosure rules before choosing. These routes change often.
