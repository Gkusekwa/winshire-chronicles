# Winshire — Publishing Plan

**Established:** the Winshire books are self-published **digitally only**, as ebooks, through **Amazon KDP**, each book as **one complete text, never split** *(author, Oct 2026: final decision, digital publication only)*, in three cover editions, Bone, Night and Band, which share the text (`Covers/README.md`). Self-publishing keeps control of the books and of all other rights, including game and screen rights.

*Everything below is a working plan. Platform terms change, so check each service's current rules before relying on them. This is not legal advice.*

## One complete text *(established, Oct 2026)*

- **Every book is published complete, in one volume, never split**, with all the chapter-opener art and every chapter-end map.
- **Every chapter** *(established)*: it opens with its abstract picture and closes with the updated map. The bare map opens the book.
- **Front and back matter** *(settled by the author, Nov 2026)*: each book opens with the title, copyright, contents and the bare map, and ends with Places and words (`Book N/Back_Matter.md`). The story so far and the Who's who are published separately as the Guides to the Winshire books (`Guides/`).
- **One text only.** Each book has one text, unabridged. The Bone, Night and Band editions carry the same text and differ only in their covers.

## Where the books go

- **Amazon KDP** *(established)*: the ebook in the Kindle store.
  - **The choice:** **KDP Select** (exclusive to Amazon in 90-day terms, enrolled in Kindle Unlimited, which pays by pages read and suits long fantasy series) or **wide** (also sold on Kobo, Apple Books, Google Play and others, directly or through an aggregator).
- **ISBNs:** a Kindle ebook doesn't need one; an ebook sold in other stores usually does. If you go wide, get your own from your country's ISBN agency so the books list your imprint.

## Ebook practicalities

- **Images:** about 160 images in Book 1 (79 openers and 79 maps, plus front matter), about 177 in Book 2 and 173 in Book 3 (their 88 and 86 openers and maps, plus front matter). Keep them lean: greyscale PNG or JPEG about 1,600 px wide, because many readers use black-and-white e-ink screens.
- **Delivery fee:** under KDP's 70% royalty option, Amazon charges a delivery fee per megabyte of the ebook file, so compress every image and check the file size before upload. (Check current rates.)
- **Preview** on an e-ink Kindle, a phone and a tablet before release.
- **The ebooks are built** *(Nov 2026)*: an EPUB for the stores and a PDF with page numbers (for proofreading and advance review copies) for every book in every edition, in `Book N/{Bone,Night,Band}/`. Books 2 and 3 were rebuilt on 2 November 2026 after the last text fixes. **Upload the Kindle copies:** the full-size EPUBs are 23–27 MB, mostly images, and KDP's delivery fee is charged per megabyte, so each book also has `Book N/Kindle/`, one compressed EPUB per edition (about 9–10 MB; made by `Tools/ebook/kindle_compress.py`, checked with epubcheck). Upload those to KDP; keep the full-size files for other stores and your archive. All three books were rebuilt on 3 November 2026 with the corrected maps (no overlapping names).

## From draft to published book

1. ~~**Finish the drafts.**~~ *(Done: all three books are drafted, 253 chapters, audited and fixed, Oct 2026; now close to final draft.)*
2. **Revise them yourself,** then share them with a few **beta readers** who read epic fantasy.
3. **Developmental edit:** a professional editor checks structure, pacing, characters and the POV balance. This is the most valuable paid step.
4. **Copyedit, then proofread:** line-level corrections, then a final typo pass on the formatted ebook.
5. ~~**Cover.**~~ *(Done: covers for all three books in three editions, Bone, Night and Band, each with its own art, Oct 2026. See `Covers/README.md`.)*
6. ~~**Formatting.**~~ *(Done in-house, Nov 2026: EPUB and PDF for every book and edition, with the opener art and chapter-end maps placed as images. Still to do: compress the images before upload, and preview on devices.)*
7. **Metadata:** title, subtitle ("Winshire, Book 1"), description, categories and keywords.
8. **Upload** to KDP (and the other stores if going wide), and preview on several devices before release.

## Audiobook *(in production, Nov 2026)*

- **All three audiobooks are ready to produce** (`Book N/audiobook/`): every chapter of every book is annotated (who speaks every line, how, and the mood of about a quarter of the paragraphs), and the audiobook kit makes the reading scripts from the annotations, the lexicon and the manuscript, so they stay in step with the text. Book 1's annotations date from October 2026; Books 2 and 3's date from November 2026, made to the same standard, for the author's review. Before narrating Books 2 and 3, check the respellings their lexicons propose for new names. Book 1 runs to roughly 32–34 hours; its narration started on 2 November 2026.
- **Narration: Chatterbox** *(settled by the author, Nov 2026)*: the open-source Chatterbox (MIT), run on the author's Mac through the audiobook kit (`Tools/audiobook-kit/`), with Emma narrating everything. It is free and needs no subscription. The kit checks every take's words with Whisper and each chapter's loudness, and tags each file with its chapter title; each chapter is still listened to and proofread before release.
- **Where an AI-narrated audiobook can go** *(stores' rules as of Sep 2026; check current terms)*:
  - **Google Play Books** and **Kobo Writing Life** accept uploaded AI-narrated audio (mark the narrator as a synthesised voice). So does selling direct (Gumroad, Payhip, your own site).
  - **Spotify** and **INaudio** (formerly Findaway) accept AI narration only from providers they name (Google Play Books, ElevenLabs and a few others); ask before relying on them.
  - **Audible's ACX** does not accept AI narration made elsewhere. Amazon's own *Virtual Voice* narrates the KDP ebook itself.
- **Disclosure:** the opening and closing credits say the book is narrated by a digital voice.

## Rights and the Winshire name

- **Keep all rights.** Don't sign anything that grants exclusive rights to the story, characters or world. Editors, designers and formatting services should work for hire, with you owning the result.
- **Copyright** arises automatically when you write the work in countries that follow the Berne Convention, including Tanzania. Registering it with your national copyright office (in Tanzania, COSOTA) is optional but gives you dated evidence.
- **The name "Winshire"** will span books and games. Consider a trademark search and filing before the first launch.
- **Contracts with editors, designers and translators** should state that you own the finished work.

## Launch and readers

- **Build a reader list before launch:** a simple website and a mailing list, so readers of Book 1 hear about Book 2.
- **Advance readers:** send review copies to early readers so reviews exist on launch day.
- **Release timing:** fantasy series often sell best when the next books follow quickly. All three books are drafted, so they can come out close together.
- **Serializing first** (for example, on Royal Road) can build an audience, but check that it doesn't conflict with KDP Select exclusivity if you choose that route.
- **Winshire Tales** *(settled by the author, Oct 2026; `Tales/Plan.md`)*:
  - A within-Book-1 tale and a before-Book-1 tale go out free with Book 1 as reader magnets (mailing-list sign-up, KDP free days).
  - After each book, its tales are collected and sold as the ebook *Winshire Tales, Volume N*.
  - The first four: Old Grey, The Keeper of the Library, The Bridge Warden, The Drowned Road.
- **Keep the world consistent:** artwork, names and canon stay consistent across the books and anything adapted from them later.

## Open publishing questions

- Exclusive on Amazon (Kindle Unlimited), or wide?
- Which editor?
- Which edition (Bone, Night or Band) goes out first, and how the other two are released *(to be decided later)*.
- Publish under your own name or a pen name, and under what imprint name?
- Release Book 1 alone, or the three close together?
- The audiobook: where to sell it (Google Play Books, Kobo, direct; not Audible). One narrator, Emma, is settled. Book 1's name pronunciations are settled (Nov 2026); Books 2 and 3's proposed respellings are to be checked.
