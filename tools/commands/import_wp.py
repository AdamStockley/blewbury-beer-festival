from __future__ import annotations

import argparse
from pathlib import Path


def run(args: argparse.Namespace, root: Path) -> int:
    print("WordPress import tooling is scaffolded but not implemented yet.")
    print("Planned scope: inventory pages/posts/media and prepare migration data.")
    return 0


def register(subparsers) -> None:
    parser = subparsers.add_parser(
        "import-wordpress",
        help="Import or inventory content from the legacy WordPress site.",
    )
    parser.set_defaults(func=run)
