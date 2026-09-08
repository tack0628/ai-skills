# Image production workflow

Read this reference when `$story-to-manga` will generate actual images. It governs the handoff from an approved manga name to generated reference art and final pages or panels.

## 1. Choose the production route

Prefer the environment's built-in image-generation tool. Follow its current tool instructions rather than inventing unsupported model, seed, size, or destination parameters.

- Issue one generation call per distinct reference sheet, page, panel, or variant.
- Use image-editing mode for a targeted repair to an existing generated asset.
- If the built-in tool is unavailable, do not silently switch to a paid API or CLI. Return the prompt package and explain the available fallback and its requirements.
- A long manga may be produced in sequential batches, but do not stop after the first batch unless the user requested a sample or the tool reports a real limit.

## 2. Prepare stable visual anchors

Create the following before final pages:

### Character master sheet

One uncluttered sheet should show each recurring character with:

- ID and role in planning notes;
- neutral full-body front view;
- three-quarter or side view;
- face close-up with defining features;
- canonical clothing and important props;
- a small expression range when relevant.

Keep the generated sheet free of dialogue, decorative typography, and story action. If labels are needed for the operator, keep them outside the generated image unless exact text rendering is reliable.

### Location and prop sheets

Generate these only for recurring or continuity-critical elements. Show the stable room geometry, entrances, fixed objects, lighting baseline, scale, and era-specific features. A single-use generic background does not need its own sheet.

Inspect master sheets before continuing. Regenerate or edit them if they contradict source constraints or make recurring identities hard to distinguish.

## 3. Reuse references without compounding drift

- Include the approved character master sheet in every image call containing that character.
- Include the relevant location or prop sheet whenever its geometry or design matters.
- The immediately preceding page may be an additional reference for pose, lighting, damage, weather, or object state.
- Never use a previous generated page as the only character reference; this compounds small deviations.
- Use the smallest reference set that contains every required anchor. State the role of each reference image in the prompt.

If a tool accepts recent conversation images rather than paths, include only enough recent images to cover the required master references and current edit target.

## 4. Prompt contract

Each generation prompt should contain only relevant fields from this structure:

```text
Use case: illustration-story or historical-scene
Asset type: manga character sheet, manga page, or manga panel
Primary request: <the page or panel's narrative job>
Input images: <reference number and role>
Format: <aspect ratio, reading direction, panel count, monochrome/color>
Continuity IDs: <CHAR/LOC/PROP IDs present>
Scene: <place, time, action, state change>
Composition: <panel geometry, camera distance/angle, page-turn emphasis>
Lighting/mood: <only what matters>
Text-safe zones: <balloon/caption/SFX placement or no text>
Constraints: <source facts and visual invariants>
Avoid: <drift, extra characters/objects, watermark, accidental text, unsupported reveal>
```

Repeat critical invariants on edits. Do not rewrite the whole prompt when a single targeted correction is enough.

## 5. Page versus panel generation

Use a full-page call when the page has a simple grid, limited cast, modest action, and tolerant lettering requirements.

Prefer separate panel assets and deterministic composition when any of these applies:

- more than four visually distinct panels;
- exact panel geometry or reading order is essential;
- exact Japanese or other text must be preserved;
- multiple recurring characters interact closely;
- documentary labels, arrows, or procedural detail must be exact;
- a full-page attempt repeatedly merges panels or changes identities.

When no composition tool is available, generate a simpler letter-free page rather than pretending that an unreliable crowded layout is final. Preserve the complete name and lettering map for later assembly.

## 6. Lettering policy

Generated image text is not assumed to be accurate.

- Keep exact dialogue, narration, labels, and SFX in the lettering map.
- By default, ask for clean balloons, captions, or negative-space zones without rendered wording when text accuracy is uncertain.
- If exact lettering is required and a deterministic layout or image-editing tool is available, add text after the art is approved.
- If the user asks for text baked into generation, verify every visible string. Repair misspellings instead of reporting the page as final.
- Do not turn paraphrased or dramatized words into apparent source quotations through lettering.

## 7. Sequential generation loop

For each asset:

1. Select the manga-name entry and its continuity IDs.
2. Attach the approved master references.
3. Generate one asset.
4. Inspect source fidelity, identity, clothing, handedness when relevant, props, spatial state, anatomy, panel order, accidental text, and unwanted additions.
5. Accept, make one targeted edit, or regenerate with a concise correction.
6. Record the selected output and any unresolved limitation in the manifest.

Use a bounded repair loop. After two focused retries for the same defect, change strategy—for example, simplify the page, split into panels, or leave lettering separate—instead of repeating the same prompt indefinitely.

## 8. Output persistence and delivery

For preview-only work, render generated images inline. For project-bound work, preserve selected outputs in the workspace using a stable structure such as:

```text
output/story-to-manga/<story-slug>/
  references/
  panels/
  pages/
  manifest.md
```

Do not overwrite an existing selected asset unless the user explicitly requests replacement; use a versioned sibling filename. Return final images in reading order and identify the selected files or tool results. Distinguish final selections from discarded variants.

## 9. Final QA checklist

- Every requested page or panel exists.
- Reading order and page-turn reveal match the name.
- Recurring character silhouette, face anchors, clothing, and props remain recognizable.
- Location geometry and object state change only when the story calls for it.
- No image asserts an unsupported fact or removes documented uncertainty.
- No accidental watermark, gibberish text, extra limb, duplicate character, or merged panel remains.
- Exact text is either verified in the image or supplied in the lettering map.
- The manifest maps outputs to page/panel numbers and continuity IDs.
