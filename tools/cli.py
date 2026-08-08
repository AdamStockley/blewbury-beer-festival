#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

sys.path.insert(0, str(Path(__file__).resolve().parent))

from commands import (  # noqa: E402
    audit,
    docs,
    import_wp,
    optimise_images,
    refactor_homepage,
    release,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="bbf-tools",
        description="Developer utilities for the Blewbury Beer Festival website.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    docs.register(subparsers)
    import_wp.register(subparsers)
    optimise_images.register(subparsers)
    release.register(subparsers)
    audit.register(subparsers)
    refactor_homepage.register(subparsers)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    try:
        return int(args.func(args, ROOT) or 0)
    except KeyboardInterrupt:
        print("\nCancelled.", file=sys.stderr)
        return 130
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
