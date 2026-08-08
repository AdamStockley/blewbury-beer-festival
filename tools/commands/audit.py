from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


REQUIRED_DOCS = [
    "docs/BRAND_GUIDELINES.md",
    "docs/CONTENT_GUIDE.md",
    "docs/COMPONENT_LIBRARY.md",
    "docs/STYLE_GUIDE.md",
    "docs/DESIGN_DECISIONS.md",
    "docs/ROADMAP.md",
    "docs/DEVELOPER_WORKFLOW.md",
]


def run(args: argparse.Namespace, root: Path) -> int:
    problems: list[str] = []

    print("Documentation:")
    for relative in REQUIRED_DOCS:
        exists = (root / relative).exists()
        print(f"  {'OK' if exists else 'MISSING':7} {relative}")
        if not exists:
            problems.append(f"Missing {relative}")

    print("\nGit:")
    result = subprocess.run(
        ["git", "status", "--short"],
        cwd=root,
        text=True,
        capture_output=True,
        check=True,
    )
    if result.stdout.strip():
        print(result.stdout.rstrip())
    else:
        print("  Clean working tree")

    print("\nSummary:")
    if problems:
        for problem in problems:
            print(f"  - {problem}")
        return 1

    print("  Basic project audit passed.")
    return 0


def register(subparsers) -> None:
    parser = subparsers.add_parser(
        "audit",
        help="Run lightweight repository and documentation checks.",
    )
    parser.set_defaults(func=run)
