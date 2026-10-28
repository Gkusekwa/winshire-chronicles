# AI narration instructions

These files are SSML with additional XML comments labelled `AI CUE`. The comments are performance metadata: read and apply them, but never speak them aloud. Standard `<break time="…"/>` elements are literal silence and must be honored. A 450 ms break marks a prose paragraph boundary; longer existing breaks mark a scene or section transition. Do not add another pause on top of a marked break unless the prose clearly calls for one.

## Reading and reactions

- Aim for relaxed, natural English (UK) narration with clear diction and an unhurried pace.
- Follow the cue attached to each paragraph. Cues are deliberately restrained; use only emotion supported by the text.
- For dialogue, distinguish characters with small changes in rhythm, pitch, or energy. Do not invent accents, caricature, or emotions absent from the scene.
- In action, sharpen timing and consonants without rushing or shouting unless explicitly stated. In suspense, let silence and controlled phrasing carry tension. In reflective passages, soften and slow slightly without becoming sentimental.
- Let punctuation guide sentence phrasing. Questions should sound like questions without a forced lilt. Exclamation marks do not automatically mean shouting.
- Preserve every spoken word exactly. Do not read XML tags or AI comments aloud. Do not add sound effects, breaths, or words that are not in the manuscript.
- Character delivery may vary subtly when context identifies the speaker: Maren measured and observant; Calder earthy and wry; Aurveth patient and deliberate; Kharrak terse; Lisska curious and quick; Orrun slow and deep but intelligible; Wren clear and even. Context overrides this general guide.

Emotion/style tags are comments rather than engine-specific SSML because voice providers support different reaction controls. An AI narration system should translate each cue into its supported controls while retaining the written pause durations.
