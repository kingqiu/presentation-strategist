#!/usr/bin/env python3
"""Create a clean zip package for the presentation-strategist skill."""

from __future__ import annotations

import argparse
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path


EXCLUDE_DIRS = {
    ".git",
    "__pycache__",
    "dist",
    "evaluation/runs",
}

EXCLUDE_FILES = {
    ".DS_Store",
    "evaluation/evolution_log.jsonl",
    "evaluation/accepted_edits.jsonl",
    "evaluation/rejected_edits.jsonl",
    "evaluation/feedback/records.jsonl",
}

EXCLUDE_SUFFIXES = {
    ".pyc",
    ".pyo",
    ".zip",
}


def should_exclude(path: Path, root: Path) -> bool:
    rel = path.relative_to(root).as_posix()
    if path.name in EXCLUDE_FILES or rel in EXCLUDE_FILES:
        return True
    if path.suffix in EXCLUDE_SUFFIXES:
        return True
    parts = rel.split("/")
    for index in range(len(parts)):
        candidate = "/".join(parts[: index + 1])
        if candidate in EXCLUDE_DIRS:
            return True
    if any(part in EXCLUDE_DIRS for part in parts):
        return True
    return False


def run_validator(root: Path, allow_runtime: bool = False) -> None:
    validator = root / "scripts" / "validate_skill_package.py"
    if not validator.exists():
        raise SystemExit("Missing scripts/validate_skill_package.py")
    command = [sys.executable, str(validator), str(root)]
    if allow_runtime:
        command.append("--allow-runtime")
    result = subprocess.run(command)
    if result.returncode != 0:
        raise SystemExit(result.returncode)


def package(root: Path, out: Path) -> int:
    out.parent.mkdir(parents=True, exist_ok=True)
    if out.exists():
        out.unlink()
    base = root.name
    files = sorted(path for path in root.rglob("*") if path.is_file() and not should_exclude(path, root))
    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            archive.write(path, Path(base) / path.relative_to(root))
    return len(files)


def validate_zip(out: Path) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        with zipfile.ZipFile(out) as archive:
            archive.extractall(tmp_path)
        entries = [path for path in tmp_path.iterdir() if path.is_dir()]
        if len(entries) != 1:
            raise SystemExit("Package should contain exactly one top-level skill directory.")
        run_validator(entries[0], allow_runtime=False)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skill-dir", default=".", help="Skill directory to package.")
    parser.add_argument("--out", default="dist/presentation-strategist.zip", help="Output zip path.")
    parser.add_argument("--skip-validation", action="store_true", help="Package without running validation first.")
    args = parser.parse_args()

    root = Path(args.skill_dir).resolve()
    out = Path(args.out)
    if not out.is_absolute():
        out = root / out

    if not args.skip_validation:
        run_validator(root, allow_runtime=True)

    count = package(root, out)
    if not args.skip_validation:
        validate_zip(out)
    print(f"Packaged {count} files: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
