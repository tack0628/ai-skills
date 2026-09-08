---
name: story-to-manga
description: Convert user-provided stories, firsthand accounts, folklore, historical or primary-source material, and explanatory text into a source-faithful manga blueprint with adaptation notes, character sheets, page and panel breakdowns, dialogue/narration guidance, and image-generation directions. Use when the user asks to manga-ize, comic-adapt, storyboard, panelize, or visually dramatize supplied prose, or invokes $story-to-manga.
---

# Story to Manga

Turn supplied prose into a manga-production blueprint while preserving what the source actually supports.

This skill defaults to **planning and adaptation**, not final image generation. Produce a usable manga blueprint that can be handed to an illustrator or image-generation workflow.

## Supported modes

Infer the best mode from the source unless the user specifies one.

- **Horror / kaidan** — emphasize silence, negative space, delayed reveals, page turns, sound, and viewpoint.
- **Firsthand account / essay manga** — preserve the narrator's perspective and uncertainty; favor readable chronology and lived detail.
- **Primary-source / documentary** — prioritize factual fidelity, provenance, dates, places, and explicit separation of reconstruction from recorded fact.
- **Explainer / manual** — prioritize sequence, clarity, visual demonstration, labels, and error prevention.
- **Folklore / urban legend** — preserve variants and attribution; do not collapse rumor, tradition, and verified history into one factual layer.
- **General narrative** — adapt supplied prose into a coherent visual sequence without inventing unsupported plot.

## Required input

At minimum:
- Source text, notes, transcript, or a source-grounded summary.

Useful optional inputs:
- Desired page count or panel count
- Reading direction
- Target format: vertical scroll, standard manga page, 4-koma, short comic, etc.
- Audience
- Tone and visual mood
- Whether dialogue should be minimal or narration-heavy
- Character appearance references
- Historical period, location, props, or costume constraints
- Whether the user wants only a name/storyboard or also image-generation directions
- Source citations, URLs, dates, or document labels when provenance matters

If critical details are absent, choose conservative defaults and label them as adaptation choices rather than facts.

## Core principles

1. **Source fidelity before drama.**
   Do not alter the meaning of supplied material merely to make it more cinematic.

2. **Separate fact, recollection, inference, and staging.**
   A panel may visually reconstruct an event without claiming that every depicted detail is documented.

3. **Visual economy.**
   Prefer panels that each perform a clear narrative or explanatory function.

4. **Continuity.**
   Stabilize recurring character appearance, clothing, props, environment, time of day, and spatial relationships.

5. **Page-turn logic.**
   In page-based manga, reserve major reveals, reversals, and uncanny images for positions where the page turn strengthens them.

6. **Uncertainty preservation.**
   If the source says “I think,” “apparently,” “it was said,” or otherwise expresses uncertainty, retain that uncertainty.

## Workflow

### 1. Classify the source

Identify:
- source type;
- likely adaptation mode;
- narrator or point of view;
- temporal order;
- key factual anchors;
- uncertain or disputed elements;
- the emotional or explanatory spine.

Do not silently resolve contradictions.

### 2. Build a source ledger

Before panelization, list the most important source-grounded elements.

Use labels when useful:
- **FACT** — explicitly supported by the supplied source;
- **RECOLLECTION** — narrator memory or testimony;
- **CLAIM** — a claim attributed to a person or source;
- **INFERENCE** — reasonable but not explicit;
- **ADAPTATION** — a visual or structural choice introduced for readability;
- **UNKNOWN** — unresolved.

For casual fictional or user-authored stories, keep this lightweight. For primary-source or documentary material, make it explicit.

### 3. Define adaptation constraints

State the working assumptions:
- target length;
- manga format;
- tone;
- degree of compression;
- dialogue policy;
- visual style direction;
- any historically sensitive or source-sensitive constraints.

### 4. Create continuity sheets

For every recurring person or entity, define only what is supported or deliberately chosen.

Include:
- role;
- age range if known;
- silhouette;
- hair;
- clothing;
- distinguishing features;
- carried objects;
- emotional baseline;
- continuity notes.

For important locations, define:
- layout;
- lighting;
- fixed objects;
- entrances/exits;
- spatial relationships;
- period-specific details.

Clearly mark invented visual details as **ADAPTATION**.

### 5. Compress into beats

Turn the source into a short beat sheet.

Each beat should identify:
- what changes;
- what the reader learns;
- the intended emotional or explanatory effect;
- whether the beat is indispensable.

Delete repetition unless repetition itself is meaningful.

### 6. Allocate pages and panels

For each page, specify:
- page purpose;
- panel count;
- panel size emphasis;
- viewpoint;
- action;
- narration/dialogue;
- sound effects when useful;
- continuity notes;
- source status for reconstructed details when necessary.

Use fewer panels for:
- dread;
- shock;
- emotional weight;
- complex visual explanation.

Use more panels for:
- procedural sequences;
- fast action;
- incremental realization;
- comic timing.

### 7. Write dialogue and narration guidance

Prefer concise, drawable text.

Never:
- invent quotations and present them as source text;
- turn paraphrase into quotation;
- give historical figures undocumented exact dialogue as fact.

When exact wording is unavailable, use narration, indirect speech, or label dialogue as dramatized.

### 8. Add image-generation directions

When requested or useful, create a compact visual direction for each page or key panel.

Include:
- recurring character continuity;
- composition;
- camera distance and angle;
- lighting;
- environment;
- expression and pose;
- important props;
- negative constraints;
- text placement zones.

Do not overload prompts with every minor source detail. Put global continuity in a shared section and page-specific differences in page directions.

## Mode-specific rules

### Horror / kaidan

Prefer:
- anticipatory panels before the reveal;
- empty space;
- off-panel sound;
- repeated framing with one changed detail;
- obscured or partial forms before full disclosure;
- page turns for major visual reveals.

Do not insert a visible monster merely because the source is frightening. If the source never identifies what was present, preserve ambiguity.

### Firsthand account

Keep the narrator's knowledge limited to what they could reasonably know at that point.

Avoid omniscient panels that accidentally convert later inference into contemporaneous fact.

### Primary-source / documentary

At the beginning of the output, include a brief **Adaptation fidelity note**.

If a visual must be reconstructed:
- mark it **RECONSTRUCTION** or **ADAPTATION** in planning notes;
- distinguish documented environment/details from generic period-appropriate fill;
- preserve dates, named entities, sequence, and attributed claims;
- do not fabricate archival-looking evidence.

If multiple sources disagree, show the disagreement rather than selecting one silently.

### Explainer / manual

Optimize for successful completion of the procedure.

Each step should show:
- starting state;
- action;
- result;
- common mistake or warning when relevant.

Do not let dramatic composition obscure the action the reader needs to perform.

## Copyright-aware handling

When the source may be copyrighted:
- adapt through summary, structure, and transformation;
- avoid reproducing long passages verbatim;
- avoid copying distinctive dialogue unnecessarily;
- preserve the user's ideas and facts without imitating a living artist's exact style.

If the user supplies their own text, it may be transformed directly while still avoiding needless verbatim duplication in the planning output.

## Default output

Use this order unless the user asks for something narrower:

1. **Adaptation summary**
   - selected mode;
   - target length;
   - point of view;
   - core hook;
   - fidelity risks.

2. **Source ledger**
   - important facts, recollections, claims, uncertainties, and adaptation choices.

3. **Character / location continuity**
   - recurring visual anchors.

4. **Beat sheet**
   - compressed narrative or explanatory beats.

5. **Page-by-page manga name**
   - page purpose;
   - panel breakdown;
   - framing/action;
   - narration/dialogue;
   - SFX;
   - page-turn notes.

6. **Image-generation directions**
   - global continuity block;
   - page or key-panel directions.

7. **Human-check items**
   - details that should be verified before final art.

## Compact output option

If the user asks for a quick conversion, return only:
- premise;
- character continuity;
- beat sheet;
- page/panel breakdown.

## Guardrails

- Do not invent source facts.
- Do not erase uncertainty for dramatic convenience.
- Do not add supernatural explanations that the source does not establish.
- Do not add gore, sexualization, or shock elements merely to increase impact.
- Do not change identities, dates, places, or causal relationships without labeling the change.
- Do not require a fixed page count when the material clearly needs more or fewer pages; state the tradeoff.
- Do not generate filler panels that contribute nothing to story, atmosphere, continuity, or explanation.
- Keep visual continuity explicit enough for downstream image generation.
- When factual fidelity and cinematic effect conflict, preserve fidelity and explain the adaptation compromise.
