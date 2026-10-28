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
| `Pronunciation_Guide.md` | Invented names with a respelling and IPA. Names marked *confirm* are the author's to settle. |
| `Lexicon_IPA.pls`, `Lexicon_Alias.pls` | The same names as standard pronunciation lexicons: IPA (Amazon Polly, Azure) and alias spellings (ElevenLabs and others). |
| `annotations/chNN.json` | The source of the performance: the speaker and kind of every quoted or italic span, and a direction where a paragraph needs one. |
| `Performance/NN.json` | Each chapter as a sequence of segments with type, speaker, listener, delivery and pause. This is what a multi-voice pipeline uses. |
| `Scripts/*.ssml` | Standard SSML 1.1 for one narrator. Bond speech, thoughts, verse and written words get gentle prosody; paragraphs with a direction get a slight rate change; pauses are explicit, never over 3 s. Comments name the speaker of each paragraph. |
| `Variants/google/` | SSML with names respelt inline, for engines without lexicon support. |
| `Variants/azure/` | SSML wrapped in an Azure voice element (rebuild with `--variant azure --voice NAME` to change the voice). |
| `ElevenLabs/` | The ElevenLabs production kit (below). |

## ElevenLabs

Two routes.

**No code (ElevenLabs Studio).** Create a Studio project and paste or import the chapters from `ElevenLabs/Studio/*.txt`, one per chapter. These are clean text with the headings spoken as words. Upload `Lexicon_Alias.pls` as the project's pronunciation dictionary, and choose a narrator voice. Studio lets you assign other voices to passages by hand. `Cast.md` says who speaks where, and the comments in `Scripts/*.ssml` name the speaker of every paragraph.

**Scripted (API).** `Tools/audiobook/render_elevenlabs.py` renders whole chapters from `Performance/`:

1. Fill in `ElevenLabs/voices.json`: a voice ID for **Narrator** at least, and for any roles you want voiced. Roles left empty fall back to the Narrator.
2. `export ELEVENLABS_API_KEY=...` Don't put the key in any file in this repository.
3. `python3 render_elevenlabs.py --estimate`: characters per chapter, before spending anything. The whole book is about 1.6 million characters.
4. Try one chapter first: `python3 render_elevenlabs.py --chapters 1 --cast single`, then listen to it.
5. Choose:
   - `--cast single` (one narrator) or `--cast full` (a voice per role);
   - `--model eleven_multilingual_v2` (steady, good for long-form) or `--model eleven_v3` (more expressive; gets the audio tags from the annotations, such as [softly] for bond speech);
   - `--dialogue`, with v3 and full cast, to voice the speakers of a passage together.

   Every request is cached under `ElevenLabs/cache/`, so re-runs and edits only pay for what changed. The finished, loudness-normalised chapters go to `ElevenLabs/out/`. Both folders are ignored by git. ffmpeg is required.

Check ElevenLabs' current plans: commercial use needs a paid plan, and credits per month vary by plan.

## Where it can be published

- **Audible (ACX)** doesn't accept AI narration made outside Amazon. Amazon's own **Virtual Voice** (through KDP) narrates the published ebook itself and doesn't use these files.
- **ElevenReader Publishing** (ElevenLabs' own store), which can also distribute to **Spotify** through Findaway Voices.
- **Spotify for Authors**, which was adding ElevenLabs narration in 2026 and distributes to Google Play Books.
- **Google Play Books** accepts uploaded AI-narrated audio.

Check each one's current terms, exclusivity and AI-disclosure rules before choosing. These routes change often.
