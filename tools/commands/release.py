from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


def _run(cmd: list[str], cwd: Path) -> None:
    print("+", " ".join(cmd))
    subprocess.run(cmd, cwd=cwd, check=True)


def run(args: argparse.Namespace, root: Path) -> int:
    _run(["npm", "run", "build"], root)
    _run(["git", "status", "--short"], root)
    print("\nRelease checks passed.")
    print("No commit, push or deployment was performed automatically.")
    return 0


def register(subparsers) -> None:
    parser = subparsers.add_parser(
        "release",
        help="Run safe pre-release checks.",
    )
    parser.set_defaults(func=run)
