---
name: gallery-poster-maker
description: Transform uploaded photos into premium minimalist 3:4 editorial posters with a photographic upper half and an abstract geometric lower half. Use when the user asks to turn one or more uploaded photos into luxury, gallery-style, architectural, editorial, or minimalist posters, or invokes $gallery-poster-maker.
---

# Gallery Poster Maker

Transform each uploaded photo into one independent premium minimalist poster.

## Inputs

Require at least one user-provided image.

If multiple images are provided:
- Treat each image as a separate poster.
- Do not combine them into a collage unless the user explicitly asks for one.

Optional user inputs may include:
- title text;
- year;
- preferred mood;
- preferred typography direction;
- background tone;
- whether text should be omitted.

## Core composition

Use a strict 3:4 vertical poster.

Divide the poster into two equal horizontal regions:
- Upper half: 50% of the canvas.
- Lower half: 50% of the canvas.

Do not let either region visually dominate the other.

## Upper half

Preserve the uploaded photo as the visual source.

Maintain:
- the subject's proportions and structure;
- realistic material texture;
- natural light and shadow;
- the existing color atmosphere.

Apply only restrained professional color grading suitable for:
- editorial photography;
- gallery presentation;
- architectural publishing;
- premium brand imagery.

The surrounding ceiling, floor, sky, wall, or environmental background may be naturally extended to fit the layout.

Never stretch, warp, reshape, or materially alter the main subject merely to fit the composition.

## Lower half

Create an abstract interpretation of the main subject.

Extract its most recognizable:
- silhouette;
- structural geometry;
- proportions;
- signature features.

Render the abstraction using:
- simple geometric shapes;
- flat color fields;
- thin line work;
- generous negative space.

Avoid realistic illustration and excessive detail.

The abstract form should remain recognizable at a glance.

Derive the lower-half palette primarily from the source photo.

Small horizontal lines, vertical lines, grids, or abstract environmental elements may be added when they improve the composition.

## Overall art direction

Follow the detailed visual rules in `references/style-guide.md`.

Aim for:
- premium;
- contemporary;
- quiet;
- restrained;
- art-directed;
- internationally legible design.

## Text treatment

Use only a small amount of text.

Prefer:
- concise English title;
- year;
- short style or series label.

Typography should support the composition rather than dominate it.

If the user supplies text, preserve its wording unless they ask for editing.

## Guardrails

Do not:
- create a collage unless explicitly requested;
- distort the subject;
- turn the lower half into a realistic illustration;
- add cartoon-like styling;
- add glossy or cheap template effects;
- introduce strong electronic or cyberpunk aesthetics unless requested;
- overcrowd the poster;
- add decorative elements without compositional purpose.

## Execution

When an image-generation or image-editing tool is available, use it to create the final poster.

For multiple uploaded images, produce one poster per image. Generate in batches of at most 3 source images per pass by default; for larger sets, state that the request is high-load and continue in small batches rather than attempting the whole set in one burst.

If examples or style clarification are needed, read `references/style-guide.md`.
