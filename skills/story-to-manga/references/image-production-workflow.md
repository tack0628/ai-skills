# Image production workflow

Read this reference when `$story-to-manga` will generate actual images. It governs the handoff from an approved production script and manga name to reference art, pre-lettering pages or panels, and fully lettered final pages.

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
Lettering zones: <low-detail areas reserved for later balloon/caption/SFX placement>
Constraints: <source facts and visual invariants>
Avoid: <drift, extra characters/objects, speech balloons, captions, SFX, watermark, accidental text, unsupported reveal>
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

## 6. Pre-lettering art contract

Generated pages and panels are artwork plates, not finished lettered pages.

- Include an explicit instruction in every page or panel prompt: no dialogue text, captions, SFX, speech balloons, labels, signatures, or watermark.
- Reserve the planned lettering areas as low-detail negative space without placing blank bubbles there.
- Do not put essential faces, hands, clues, period evidence, or action inside a reserved lettering area.
- If the model produces accidental text or bubbles, repair or regenerate the artwork plate before typesetting.
- Keep exact dialogue, narration, labels, and SFX only in the production script and lettering plan until the deterministic composition step.

## 7. Sequential generation loop

For each asset:

1. Select the manga-name entry and its continuity IDs.
2. Attach the approved master references.
3. Generate one asset.
4. Inspect source fidelity, identity, clothing, handedness when relevant, props, spatial state, anatomy, panel order, accidental text, and unwanted additions.
5. Accept, make one targeted edit, or regenerate with a concise correction.
6. Record the selected output and any unresolved limitation in the manifest.

Use a bounded repair loop. After two focused retries for the same defect, change strategy—for example, simplify the page, split into panels, or leave lettering separate—instead of repeating the same prompt indefinitely.

## 8. Balloon and lettering composition

Read [lettering-workflow.md](lettering-workflow.md), build `lettering-plan.json`, validate it with `scripts/letter_manga.py --dry-run`, and then render the final pages. The script, not the image model, owns exact wording, balloon geometry, and final text placement.

If the required font or Pillow is unavailable, report that concrete blocker and preserve the production script, lettering plan, and pre-lettering art. Do not label the unlettered pages final.

## 9. Output persistence and delivery

For preview-only work, render generated images inline. For project-bound work, preserve selected outputs in the workspace using a stable structure such as:

```text
output/story-to-manga/<story-slug>/
  script.md
  lettering-plan.json
  references/
  panels/
  pages/art/
  pages/lettered/
  manifest.md
```

Do not overwrite an existing selected asset unless the user explicitly requests replacement; use a versioned sibling filename. Keep art plates and lettered pages separate. Return fully lettered images in reading order and identify the selected files or tool results. Distinguish final selections from discarded variants.

## 10. Final QA checklist

- Every requested page or panel exists.
- Reading order and page-turn reveal match the name.
- Recurring character silhouette, face anchors, clothing, and props remain recognizable.
- Location geometry and object state change only when the story calls for it.
- No image asserts an unsupported fact or removes documented uncertainty.
- No accidental watermark, generated gibberish text, extra limb, duplicate character, or merged panel remains.
- Every final string exactly matches the production script and remains inside its balloon or caption.
- Balloon tails clearly identify the intended speaker and do not obscure essential art.
- The manifest maps outputs to page/panel numbers and continuity IDs.
