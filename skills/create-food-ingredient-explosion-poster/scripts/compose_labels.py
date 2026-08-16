#!/usr/bin/env python3
"""Create an exact-ratio food poster and add deterministic CJK labels.

The input should be a text-free generated food image. Layout is controlled by a
JSON specification; see references/label-spec.example.json.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw, ImageFont


DEFAULT_FONT_CANDIDATES = (
    "/System/Library/Fonts/STHeiti Light.ttc",
    "/System/Library/Fonts/PingFang.ttc",
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
    "/usr/share/fonts/opentype/noto/NotoSansCJKsc-Regular.otf",
    "C:/Windows/Fonts/msyh.ttc",
    "C:/Windows/Fonts/simhei.ttf",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Pad/crop a food image to a fixed canvas and add exact labels."
    )
    parser.add_argument("--input", required=True, type=Path, help="Text-free input image")
    parser.add_argument("--output", required=True, type=Path, help="Labeled PNG output")
    parser.add_argument("--spec", required=True, type=Path, help="JSON label specification")
    parser.add_argument(
        "--unlabeled-output",
        type=Path,
        help="Optional exact-size text-free PNG produced before labels",
    )
    parser.add_argument(
        "--validate-only",
        action="store_true",
        help="Validate the spec and source without writing output",
    )
    return parser.parse_args()


def color(value: str, alpha: int = 255) -> tuple[int, int, int, int]:
    raw = value.strip().lstrip("#")
    if len(raw) == 6:
        return tuple(int(raw[i : i + 2], 16) for i in (0, 2, 4)) + (alpha,)
    if len(raw) == 8:
        return tuple(int(raw[i : i + 2], 16) for i in (0, 2, 4, 6))
    raise ValueError(f"Expected #RRGGBB or #RRGGBBAA, got {value!r}")


def resolve_font(spec: dict[str, Any]) -> Path:
    requested = spec.get("font_path")
    if requested:
        path = Path(requested).expanduser()
        if path.is_file():
            return path
        raise FileNotFoundError(f"Configured font does not exist: {path}")

    for candidate in DEFAULT_FONT_CANDIDATES:
        path = Path(candidate)
        if path.is_file():
            return path

    raise FileNotFoundError(
        "No CJK font found. Set font_path in the JSON specification."
    )


def fit_to_canvas(
    image: Image.Image,
    width: int,
    height: int,
    background: tuple[int, int, int, int],
    mode: str,
) -> Image.Image:
    src = image.convert("RGBA")
    if mode not in {"pad", "crop"}:
        raise ValueError("canvas.fit must be 'pad' or 'crop'")

    if mode == "pad":
        scale = min(width / src.width, height / src.height)
    else:
        scale = max(width / src.width, height / src.height)

    resized_width = max(1, round(src.width * scale))
    resized_height = max(1, round(src.height * scale))
    resized = src.resize((resized_width, resized_height), Image.Resampling.LANCZOS)

    if mode == "pad":
        canvas = Image.new("RGBA", (width, height), background)
        x = (width - resized_width) // 2
        y = (height - resized_height) // 2
        canvas.alpha_composite(resized, (x, y))
        return canvas

    left = max(0, (resized_width - width) // 2)
    top = max(0, (resized_height - height) // 2)
    return resized.crop((left, top, left + width, top + height))


def validate_spec(spec: dict[str, Any]) -> None:
    canvas = spec.get("canvas")
    if not isinstance(canvas, dict):
        raise ValueError("spec.canvas must be an object")

    width = int(canvas.get("width", 1440))
    height = int(canvas.get("height", 1920))
    if width <= 0 or height <= 0:
        raise ValueError("Canvas dimensions must be positive")

    labels = spec.get("labels")
    if not isinstance(labels, list) or not labels:
        raise ValueError("spec.labels must be a non-empty array")

    names: set[str] = set()
    for index, item in enumerate(labels):
        if not isinstance(item, dict):
            raise ValueError(f"labels[{index}] must be an object")
        name = item.get("name")
        if not isinstance(name, str) or not name.strip():
            raise ValueError(f"labels[{index}].name must be a non-empty string")
        if name in names:
            raise ValueError(f"Duplicate label name: {name}")
        names.add(name)

        if item.get("side") not in {"left", "right"}:
            raise ValueError(f"labels[{index}].side must be 'left' or 'right'")

        target = item.get("target")
        if not isinstance(target, list) or len(target) != 2:
            raise ValueError(f"labels[{index}].target must be [x, y]")

        x, y = int(target[0]), int(target[1])
        if not (0 <= x < width and 0 <= y < height):
            raise ValueError(f"labels[{index}].target is outside the canvas")

        label_y = int(item.get("y", -1))
        elbow_x = int(item.get("elbow_x", -1))
        if not 0 <= label_y < height:
            raise ValueError(f"labels[{index}].y is outside the canvas")
        if not 0 <= elbow_x < width:
            raise ValueError(f"labels[{index}].elbow_x is outside the canvas")


def draw_label(
    draw: ImageDraw.ImageDraw,
    item: dict[str, Any],
    style: dict[str, Any],
    font_path: Path,
    width: int,
) -> None:
    name = item["name"]
    note = item.get("note", "")
    side = item["side"]
    y = int(item["y"])
    target = tuple(int(value) for value in item["target"])
    elbow_x = int(item["elbow_x"])

    name_size = int(item.get("name_size", style.get("name_size", 42)))
    note_size = int(item.get("note_size", style.get("note_size", 24)))
    margin_x = int(style.get("margin_x", 64))
    note_offset_y = int(style.get("note_offset_y", 43))
    line_width = int(style.get("line_width", 3))
    font_index = int(style.get("font_index", 0))

    name_font = ImageFont.truetype(str(font_path), name_size, index=font_index)
    note_font = ImageFont.truetype(str(font_path), note_size, index=font_index)

    line_color = color(style.get("line_color", "#DAB056"), 245)
    name_color = color(style.get("name_color", "#FCF4DE"))
    note_color = color(style.get("note_color", "#CDB37E"))
    shadow = color(style.get("shadow_color", "#000000"), 210)
    dot_fill = color(style.get("dot_fill", "#14110C"))

    text_x = margin_x if side == "left" else width - margin_x
    anchor = "lm" if side == "left" else "rm"
    bbox = draw.textbbox((text_x, y), name, font=name_font, anchor=anchor, stroke_width=1)
    gap = int(style.get("line_gap", 22))
    line_start = (bbox[2] + gap, y) if side == "left" else (bbox[0] - gap, y)

    draw.line([line_start, (elbow_x, y), target], fill=line_color, width=line_width, joint="curve")
    tx, ty = target
    outer_radius = int(style.get("dot_outer_radius", 7))
    inner_radius = int(style.get("dot_inner_radius", 3))
    draw.ellipse(
        (tx - outer_radius, ty - outer_radius, tx + outer_radius, ty + outer_radius),
        fill=line_color,
    )
    draw.ellipse(
        (tx - inner_radius, ty - inner_radius, tx + inner_radius, ty + inner_radius),
        fill=dot_fill,
    )

    draw.text(
        (text_x + 2, y + 3),
        name,
        font=name_font,
        anchor=anchor,
        fill=shadow,
        stroke_width=2,
        stroke_fill=shadow,
    )
    draw.text(
        (text_x, y),
        name,
        font=name_font,
        anchor=anchor,
        fill=name_color,
        stroke_width=1,
        stroke_fill=color("#1E160A", 230),
    )

    if note:
        note_y = y + note_offset_y
        draw.text(
            (text_x + 1, note_y + 2),
            note,
            font=note_font,
            anchor=anchor,
            fill=shadow,
            stroke_width=2,
            stroke_fill=shadow,
        )
        draw.text(
            (text_x, note_y),
            note,
            font=note_font,
            anchor=anchor,
            fill=note_color,
            stroke_width=1,
            stroke_fill=color("#14100A", 210),
        )


def main() -> None:
    args = parse_args()
    spec = json.loads(args.spec.read_text(encoding="utf-8"))
    validate_spec(spec)
    font_path = resolve_font(spec)

    source = Image.open(args.input)
    source.load()
    canvas_spec = spec["canvas"]
    width = int(canvas_spec.get("width", 1440))
    height = int(canvas_spec.get("height", 1920))
    background = color(canvas_spec.get("background", "#000000"))
    mode = canvas_spec.get("fit", "pad")
    canvas = fit_to_canvas(source, width, height, background, mode)

    if args.validate_only:
        print(f"OK: {len(spec['labels'])} labels, {width}x{height}, font={font_path}")
        return

    if args.unlabeled_output:
        args.unlabeled_output.parent.mkdir(parents=True, exist_ok=True)
        canvas.convert("RGB").save(args.unlabeled_output, format="PNG", optimize=True)

    draw = ImageDraw.Draw(canvas)
    style = spec.get("style", {})
    for item in spec["labels"]:
        draw_label(draw, item, style, font_path, width)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    canvas.convert("RGB").save(args.output, format="PNG", optimize=True)
    print(args.output.resolve())


if __name__ == "__main__":
    main()
