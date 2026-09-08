# Lettering workflow

Use this workflow after pre-lettering artwork has been generated and approved. Final dialogue, narration, and balloons must be composed deterministically rather than rendered by the image model.

## Requirements

- Python 3
- Pillow in the active Python environment
- A font file containing every required glyph; for Japanese, prefer a Japanese Gothic or Mincho font the user is permitted to use
- One separate pre-lettering image per page

The bundled script searches common macOS, Linux, and Windows Japanese fonts. Pass `--font` when auto-detection is unsuitable or unavailable.

## Production script handoff

Before creating the JSON plan, finalize a human-readable `script.md`. Key every item by page and panel and include:

- scene and action;
- speaker or narration role;
- exact text;
- dialogue, thought, narration, label, or SFX classification;
- reading order;
- intended balloon owner and tail direction;
- source label for quotations or documentary claims;
- continuity IDs.

Copy exact text from this script into the JSON plan. Do not rewrite dialogue during typesetting.

## Lettering plan schema

All `box`, `anchor`, and `tip` coordinates are normalized from `0` to `1` relative to the full page. A box is `[left, top, right, bottom]`.

```json
{
  "defaults": {
    "font": "/path/to/japanese-font.ttc",
    "font_size": 42,
    "min_font_size": 18,
    "direction": "vertical",
    "fill": "#FFFFFF",
    "stroke": "#111111",
    "stroke_width": 4,
    "text_fill": "#111111",
    "padding": 22
  },
  "pages": [
    {
      "id": "PAGE-001",
      "input": "pages/art/page-001.png",
      "output": "pages/lettered/page-001.png",
      "elements": [
        {
          "id": "P001-B01",
          "kind": "speech",
          "shape": "ellipse",
          "box": [0.67, 0.08, 0.91, 0.35],
          "text": "誰かいるの？",
          "direction": "vertical",
          "tail": {
            "anchor": [0.72, 0.31],
            "tip": [0.58, 0.43],
            "width": 0.025
          }
        },
        {
          "id": "P001-C01",
          "kind": "narration",
          "shape": "rounded-rectangle",
          "box": [0.08, 0.05, 0.47, 0.15],
          "text": "午前二時、廊下から足音がした。",
          "direction": "horizontal"
        }
      ]
    }
  ]
}
```

Supported shapes are `ellipse`, `rounded-rectangle`, `rectangle`, and `none`. Use `none` for freestanding text only when the art provides sufficient contrast. A `tail` requires normalized `anchor` and `tip` coordinates. Element values override `defaults`.

## Execution

Run from the story output directory or provide `--base-dir`:

```bash
python path/to/story-to-manga/scripts/letter_manga.py lettering-plan.json --dry-run
python path/to/story-to-manga/scripts/letter_manga.py lettering-plan.json
```

Use `--font /path/to/font.ttf` to override the plan and auto-detection. The dry run validates inputs, fonts, geometry, and text fit without writing outputs.

The script refuses to overwrite an existing output. When revising a page, choose a versioned output filename such as `page-001-v2.png`.

## Placement rules

- Follow manga reading order consistently; for Japanese right-to-left pages, earlier balloons generally sit farther right.
- Place the tail tip toward the speaker's mouth while keeping it out of faces and important gestures.
- Keep dialogue balloons distinct from narration boxes.
- Split overly long dialogue in the production script before shrinking text below a readable size.
- Use vertical text for ordinary Japanese manga dialogue unless the format or user requests horizontal text.
- Keep balloon margins, stroke width, and type scale consistent across a scene.

## Final inspection

Inspect the rendered files, not only the JSON report.

- Compare every character of final copy with `script.md`.
- Check that no glyph is missing, clipped, or outside its shape.
- Check that the balloon belongs to the correct speaker.
- Confirm tails do not cross panel borders or point ambiguously.
- Confirm bubbles and captions do not hide faces, clues, actions, or historically important details.
- Confirm the final page preserves the intended reading order.
