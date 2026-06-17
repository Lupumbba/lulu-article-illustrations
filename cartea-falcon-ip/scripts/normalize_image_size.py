#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Literal

from PIL import Image


FitMode = Literal["cover", "contain"]


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Normalize an image to an exact pixel size with cover or contain fitting."
    )
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--width", required=True, type=int)
    parser.add_argument("--height", required=True, type=int)
    parser.add_argument("--fit", required=True, choices=["cover", "contain"])
    return parser.parse_args()


def validate_dimensions(width: int, height: int) -> None:
    if width <= 0:
        raise ValueError("width must be greater than zero")
    if height <= 0:
        raise ValueError("height must be greater than zero")


def resize_cover(image: Image.Image, width: int, height: int) -> Image.Image:
    source_width, source_height = image.size
    scale = max(width / source_width, height / source_height)
    resized_width = round(source_width * scale)
    resized_height = round(source_height * scale)
    resized = image.resize((resized_width, resized_height), Image.Resampling.LANCZOS)
    left = (resized_width - width) // 2
    top = (resized_height - height) // 2
    return resized.crop((left, top, left + width, top + height))


def resize_contain(image: Image.Image, width: int, height: int) -> Image.Image:
    source_width, source_height = image.size
    scale = min(width / source_width, height / source_height)
    resized_width = round(source_width * scale)
    resized_height = round(source_height * scale)
    resized = image.resize((resized_width, resized_height), Image.Resampling.LANCZOS)
    canvas = Image.new("RGB", (width, height), "white")
    left = (width - resized_width) // 2
    top = (height - resized_height) // 2
    canvas.paste(resized, (left, top))
    return canvas


def normalize_image(input_path: Path, output_path: Path, width: int, height: int, fit: FitMode) -> None:
    validate_dimensions(width, height)
    if not input_path.exists():
        raise FileNotFoundError(f"input image does not exist: {input_path}")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    image = Image.open(input_path).convert("RGB")
    if fit == "cover":
        normalized = resize_cover(image, width, height)
    elif fit == "contain":
        normalized = resize_contain(image, width, height)
    else:
        raise ValueError(f"unsupported fit mode: {fit}")
    normalized.save(output_path, format="PNG", optimize=True)


def main() -> None:
    arguments = parse_arguments()
    normalize_image(
        input_path=Path(arguments.input),
        output_path=Path(arguments.output),
        width=arguments.width,
        height=arguments.height,
        fit=arguments.fit,
    )


if __name__ == "__main__":
    main()
