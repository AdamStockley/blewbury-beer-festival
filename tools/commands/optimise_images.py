from __future__ import annotations

import argparse
from pathlib import Path


def run(args: argparse.Namespace, root: Path) -> int:
    image_dir = root / "public" / "images"
    image_dir.mkdir(parents=True, exist_ok=True)

    files = [
        p for p in image_dir.rglob("*")
        if p.is_file() and p.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp", ".avif"}
    ]

    print(f"Found {len(files)} image file(s) in {image_dir.relative_to(root)}.")
    print("Optimisation is scaffolded; no images were modified.")
    return 0


def register(subparsers) -> None:
    parser = subparsers.add_parser(
        "optimise-images",
        help="Inspect and eventually optimise website images.",
    )
    parser.set_defaults(func=run)
