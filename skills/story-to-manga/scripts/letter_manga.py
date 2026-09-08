#!/usr/bin/env python3
"""Apply deterministic speech balloons and lettering to manga page images."""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path
from typing import Any

try:
    from PIL import Image, ImageColor, ImageDraw, ImageFont
except ImportError as exc:  # pragma: no cover - exercised only without Pillow
    raise SystemExit(
        "Pillow is required. Install it in the active Python environment with "
        "`python -m pip install pillow`."
    ) from exc


DEFAULT_FONT_CANDIDATES = (
    "/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc",
    "/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc",
    "/System/Library/Fonts/Hiragino Sans GB.ttc",
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
    "/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc",
    "C:/Windows/Fonts/YuGothM.ttc",
    "C:/Windows/Fonts/meiryo.ttc",
)

VERTICAL_ROTATE = frozenset("ー―—‐＝…‥")


class PlanError(ValueError):
    """Raised when the lettering plan is invalid."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Add speech balloons, captions, and Japanese lettering to manga pages."
    )
    parser.add_argument("plan", type=Path, help="Path to lettering-plan.json")
    parser.add_argument(
        "--font",
        type=Path,
        help="Default font file. Overrides the plan default and auto-detection.",
    )
    parser.add_argument(
        "--base-dir",
        type=Path,
        help="Resolve page paths relative to this directory instead of the plan directory.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate the plan, inputs, fonts, and text fit without writing outputs.",
    )
    return parser.parse_args()


def load_plan(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise PlanError(f"Plan not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise PlanError(f"Invalid JSON in {path}: {exc}") from exc
    if not isinstance(data, dict) or not isinstance(data.get("pages"), list):
        raise PlanError("The plan must be an object containing a `pages` array.")
    return data


def resolve_font(explicit: Path | None, configured: str | None, base_dir: Path) -> Path:
    if explicit:
        requested = explicit.expanduser()
        if not requested.is_file():
            raise PlanError(f"Font passed with --font was not found: {requested}")
        return requested.resolve()
    if configured:
        configured_path = Path(configured).expanduser()
        requested = configured_path if configured_path.is_absolute() else base_dir / configured_path
        if not requested.is_file():
            raise PlanError(f"Configured font was not found: {requested}")
        return requested.resolve()
    for candidate in (Path(value) for value in DEFAULT_FONT_CANDIDATES):
        if candidate.is_file():
            return candidate.resolve()
    raise PlanError(
        "No usable Japanese font was found. Pass `--font /path/to/font.ttf` or set "
        "`defaults.font` in the lettering plan."
    )


def color(value: Any, field: str) -> tuple[int, ...]:
    try:
        return ImageColor.getcolor(str(value), "RGBA")
    except ValueError as exc:
        raise PlanError(f"Invalid color for {field}: {value}") from exc


def normalized_box(value: Any, width: int, height: int, element_id: str) -> tuple[int, int, int, int]:
    if not isinstance(value, list) or len(value) != 4:
        raise PlanError(f"{element_id}: `box` must be [left, top, right, bottom].")
    try:
        left, top, right, bottom = (float(item) for item in value)
    except (TypeError, ValueError) as exc:
        raise PlanError(f"{element_id}: box coordinates must be numbers.") from exc
    if not (0 <= left < right <= 1 and 0 <= top < bottom <= 1):
        raise PlanError(f"{element_id}: box coordinates must be normalized to 0..1.")
    return (
        round(left * width),
        round(top * height),
        round(right * width),
        round(bottom * height),
    )


def normalized_point(value: Any, width: int, height: int, field: str) -> tuple[int, int]:
    if not isinstance(value, list) or len(value) != 2:
        raise PlanError(f"{field} must be [x, y].")
    try:
        x, y = (float(item) for item in value)
    except (TypeError, ValueError) as exc:
        raise PlanError(f"{field} coordinates must be numbers.") from exc
    if not (0 <= x <= 1 and 0 <= y <= 1):
        raise PlanError(f"{field} coordinates must be normalized to 0..1.")
    return round(x * width), round(y * height)


def inset_box(box: tuple[int, int, int, int], padding: int) -> tuple[int, int, int, int]:
    left, top, right, bottom = box
    inner = left + padding, top + padding, right - padding, bottom - padding
    if inner[0] >= inner[2] or inner[1] >= inner[3]:
        raise PlanError("Padding leaves no room for lettering.")
    return inner


def font_for(path: Path, size: int) -> ImageFont.FreeTypeFont:
    try:
        return ImageFont.truetype(str(path), size=size)
    except OSError as exc:
        raise PlanError(f"Unable to load font {path}: {exc}") from exc


def horizontal_lines(
    draw: ImageDraw.ImageDraw,
    text: str,
    font: ImageFont.FreeTypeFont,
    max_width: int,
) -> list[str]:
    lines: list[str] = []
    for paragraph in text.splitlines() or [""]:
        if not paragraph:
            lines.append("")
            continue
        current = ""
        for char in paragraph:
            candidate = current + char
            bbox = draw.textbbox((0, 0), candidate, font=font)
            if current and bbox[2] - bbox[0] > max_width:
                lines.append(current)
                current = char
            else:
                current = candidate
        lines.append(current)
    return lines


def horizontal_layout_fits(
    draw: ImageDraw.ImageDraw,
    text: str,
    font: ImageFont.FreeTypeFont,
    box: tuple[int, int, int, int],
    line_gap: int,
) -> tuple[bool, list[str], int]:
    width = box[2] - box[0]
    height = box[3] - box[1]
    lines = horizontal_lines(draw, text, font, width)
    line_height = max(1, font.getbbox("国Ag")[3] - font.getbbox("国Ag")[1])
    total_height = len(lines) * line_height + max(0, len(lines) - 1) * line_gap
    return total_height <= height, lines, line_height


def vertical_columns(text: str, rows: int) -> list[str]:
    columns: list[str] = []
    for explicit_column in text.splitlines() or [""]:
        chars = list(explicit_column)
        if not chars:
            columns.append("")
            continue
        columns.extend("".join(chars[i : i + rows]) for i in range(0, len(chars), rows))
    return columns


def vertical_layout_fits(
    text: str,
    size: int,
    box: tuple[int, int, int, int],
    char_gap: int,
    column_gap: int,
) -> tuple[bool, list[str], int]:
    width = box[2] - box[0]
    height = box[3] - box[1]
    advance = size + char_gap
    rows = max(1, (height + char_gap) // advance)
    columns = vertical_columns(text, rows)
    total_width = len(columns) * size + max(0, len(columns) - 1) * column_gap
    return total_width <= width, columns, rows


def draw_rotated_glyph(
    image: Image.Image,
    char: str,
    font: ImageFont.FreeTypeFont,
    center: tuple[float, float],
    fill: tuple[int, ...],
) -> None:
    size = font.size * 2
    tile = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    tile_draw = ImageDraw.Draw(tile)
    bbox = tile_draw.textbbox((0, 0), char, font=font)
    tile_draw.text(
        ((size - (bbox[2] - bbox[0])) / 2 - bbox[0], (size - (bbox[3] - bbox[1])) / 2 - bbox[1]),
        char,
        font=font,
        fill=fill,
    )
    tile = tile.rotate(90, expand=False, resample=Image.Resampling.BICUBIC)
    image.alpha_composite(tile, (round(center[0] - size / 2), round(center[1] - size / 2)))


def draw_horizontal_text(
    image: Image.Image,
    text: str,
    font_path: Path,
    requested_size: int,
    min_size: int,
    box: tuple[int, int, int, int],
    fill: tuple[int, ...],
    line_gap_ratio: float,
) -> int:
    draw = ImageDraw.Draw(image)
    for size in range(requested_size, min_size - 1, -1):
        font = font_for(font_path, size)
        line_gap = max(1, round(size * line_gap_ratio))
        fits, lines, line_height = horizontal_layout_fits(draw, text, font, box, line_gap)
        if not fits:
            continue
        total_height = len(lines) * line_height + max(0, len(lines) - 1) * line_gap
        y = box[1] + (box[3] - box[1] - total_height) / 2
        for line in lines:
            bbox = draw.textbbox((0, 0), line, font=font)
            line_width = bbox[2] - bbox[0]
            x = box[0] + (box[2] - box[0] - line_width) / 2 - bbox[0]
            draw.text((x, y - bbox[1]), line, font=font, fill=fill)
            y += line_height + line_gap
        return size
    raise PlanError("Horizontal text does not fit its box at the minimum font size.")


def draw_vertical_text(
    image: Image.Image,
    text: str,
    font_path: Path,
    requested_size: int,
    min_size: int,
    box: tuple[int, int, int, int],
    fill: tuple[int, ...],
    char_gap_ratio: float,
    column_gap_ratio: float,
) -> int:
    for size in range(requested_size, min_size - 1, -1):
        char_gap = max(0, round(size * char_gap_ratio))
        column_gap = max(1, round(size * column_gap_ratio))
        fits, columns, _ = vertical_layout_fits(text, size, box, char_gap, column_gap)
        if not fits:
            continue
        font = font_for(font_path, size)
        draw = ImageDraw.Draw(image)
        total_width = len(columns) * size + max(0, len(columns) - 1) * column_gap
        x = box[0] + (box[2] - box[0] + total_width) / 2 - size / 2
        advance = size + char_gap
        for column in columns:
            column_height = len(column) * size + max(0, len(column) - 1) * char_gap
            y = box[1] + (box[3] - box[1] - column_height) / 2
            for char in column:
                center = x, y + size / 2
                if char in VERTICAL_ROTATE:
                    draw_rotated_glyph(image, char, font, center, fill)
                else:
                    bbox = draw.textbbox((0, 0), char, font=font)
                    glyph_width = bbox[2] - bbox[0]
                    glyph_height = bbox[3] - bbox[1]
                    draw.text(
                        (x - glyph_width / 2 - bbox[0], center[1] - glyph_height / 2 - bbox[1]),
                        char,
                        font=font,
                        fill=fill,
                    )
                y += advance
            x -= size + column_gap
        return size
    raise PlanError("Vertical text does not fit its box at the minimum font size.")


def draw_tail(
    draw: ImageDraw.ImageDraw,
    tail: dict[str, Any],
    width: int,
    height: int,
    fill: tuple[int, ...],
    stroke: tuple[int, ...],
    stroke_width: int,
    element_id: str,
) -> None:
    anchor = normalized_point(tail.get("anchor"), width, height, f"{element_id}.tail.anchor")
    tip = normalized_point(tail.get("tip"), width, height, f"{element_id}.tail.tip")
    requested_width = float(tail.get("width", 0.025))
    if not 0 < requested_width <= 0.25:
        raise PlanError(f"{element_id}: tail width must be between 0 and 0.25.")
    pixel_width = requested_width * min(width, height)
    dx, dy = tip[0] - anchor[0], tip[1] - anchor[1]
    length = math.hypot(dx, dy) or 1
    px, py = -dy / length * pixel_width / 2, dx / length * pixel_width / 2
    points = [
        (round(anchor[0] + px), round(anchor[1] + py)),
        tip,
        (round(anchor[0] - px), round(anchor[1] - py)),
    ]
    draw.polygon(points, fill=fill, outline=stroke)
    if stroke_width > 1:
        draw.line(points + [points[0]], fill=stroke, width=stroke_width, joint="curve")


def draw_element(
    image: Image.Image,
    element: dict[str, Any],
    defaults: dict[str, Any],
    cli_font: Path | None,
    base_dir: Path,
) -> dict[str, Any]:
    element_id = str(element.get("id") or "unnamed-element")
    text = element.get("text")
    if not isinstance(text, str) or not text.strip():
        raise PlanError(f"{element_id}: `text` must be a non-empty string.")
    box = normalized_box(element.get("box"), image.width, image.height, element_id)
    kind = str(element.get("kind", "speech"))
    shape = str(element.get("shape", "ellipse" if kind == "speech" else "rounded-rectangle"))
    fill = color(element.get("fill", defaults.get("fill", "#FFFFFF")), f"{element_id}.fill")
    stroke = color(element.get("stroke", defaults.get("stroke", "#111111")), f"{element_id}.stroke")
    text_fill = color(
        element.get("text_fill", defaults.get("text_fill", "#111111")),
        f"{element_id}.text_fill",
    )
    stroke_width = int(element.get("stroke_width", defaults.get("stroke_width", 4)))
    if stroke_width < 0:
        raise PlanError(f"{element_id}: stroke_width cannot be negative.")
    draw = ImageDraw.Draw(image)

    tail = element.get("tail")
    if tail is not None:
        if shape == "none" or not isinstance(tail, dict):
            raise PlanError(f"{element_id}: `tail` requires a drawable shape and object value.")
        draw_tail(draw, tail, image.width, image.height, fill, stroke, stroke_width, element_id)

    if shape == "ellipse":
        draw.ellipse(box, fill=fill, outline=stroke, width=stroke_width)
    elif shape == "rounded-rectangle":
        radius = int(element.get("radius", defaults.get("radius", 24)))
        draw.rounded_rectangle(box, radius=radius, fill=fill, outline=stroke, width=stroke_width)
    elif shape == "rectangle":
        draw.rectangle(box, fill=fill, outline=stroke, width=stroke_width)
    elif shape != "none":
        raise PlanError(f"{element_id}: unsupported shape `{shape}`.")

    font_path = resolve_font(cli_font, element.get("font", defaults.get("font")), base_dir)
    requested_size = int(element.get("font_size", defaults.get("font_size", 42)))
    min_size = int(element.get("min_font_size", defaults.get("min_font_size", 18)))
    if requested_size < min_size or min_size < 8:
        raise PlanError(f"{element_id}: invalid font-size range.")
    padding = int(element.get("padding", defaults.get("padding", round(requested_size * 0.55))))
    if padding < 0:
        raise PlanError(f"{element_id}: padding cannot be negative.")
    text_box = inset_box(box, padding)
    direction = str(element.get("direction", defaults.get("direction", "vertical")))
    if direction == "horizontal":
        actual_size = draw_horizontal_text(
            image,
            text,
            font_path,
            requested_size,
            min_size,
            text_box,
            text_fill,
            float(element.get("line_gap", defaults.get("line_gap", 0.25))),
        )
    elif direction == "vertical":
        actual_size = draw_vertical_text(
            image,
            text,
            font_path,
            requested_size,
            min_size,
            text_box,
            text_fill,
            float(element.get("char_gap", defaults.get("char_gap", 0.08))),
            float(element.get("column_gap", defaults.get("column_gap", 0.35))),
        )
    else:
        raise PlanError(f"{element_id}: direction must be `vertical` or `horizontal`.")

    return {
        "id": element_id,
        "font": str(font_path),
        "font_size": actual_size,
        "direction": direction,
    }


def resolve_page_path(value: Any, base_dir: Path, field: str) -> Path:
    if not isinstance(value, str) or not value:
        raise PlanError(f"Page `{field}` must be a non-empty path string.")
    path = Path(value).expanduser()
    return path if path.is_absolute() else base_dir / path


def process_page(
    page: dict[str, Any],
    defaults: dict[str, Any],
    base_dir: Path,
    cli_font: Path | None,
    dry_run: bool,
) -> dict[str, Any]:
    if not isinstance(page, dict):
        raise PlanError("Each page entry must be an object.")
    page_id = str(page.get("id") or "unnamed-page")
    input_path = resolve_page_path(page.get("input"), base_dir, "input")
    output_path = resolve_page_path(page.get("output"), base_dir, "output")
    if input_path.resolve() == output_path.resolve():
        raise PlanError(f"{page_id}: input and output must differ; lettering is non-destructive.")
    if not input_path.is_file():
        raise PlanError(f"{page_id}: input image not found: {input_path}")
    suffix = output_path.suffix.lower()
    if suffix not in {".png", ".jpg", ".jpeg"}:
        raise PlanError(f"{page_id}: output must use a .png, .jpg, or .jpeg extension.")
    elements = page.get("elements")
    if not isinstance(elements, list) or not elements:
        raise PlanError(f"{page_id}: `elements` must be a non-empty array.")

    with Image.open(input_path) as source:
        image = source.convert("RGBA")
    rendered = [draw_element(image, item, defaults, cli_font, base_dir) for item in elements]
    if not dry_run:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        if output_path.exists():
            raise PlanError(f"{page_id}: refusing to overwrite existing output: {output_path}")
        output_format = "JPEG" if suffix in {".jpg", ".jpeg"} else "PNG"
        output_image = image.convert("RGB") if output_format == "JPEG" else image
        output_image.save(output_path, format=output_format)
    return {
        "id": page_id,
        "input": str(input_path),
        "output": str(output_path),
        "size": [image.width, image.height],
        "elements": rendered,
    }


def main() -> int:
    args = parse_args()
    try:
        plan = load_plan(args.plan)
        base_dir = (args.base_dir or args.plan.parent).expanduser().resolve()
        defaults = plan.get("defaults", {})
        if not isinstance(defaults, dict):
            raise PlanError("`defaults` must be an object when provided.")
        report = [
            process_page(page, defaults, base_dir, args.font, args.dry_run)
            for page in plan["pages"]
        ]
    except PlanError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    print(json.dumps({"dry_run": args.dry_run, "pages": report}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
