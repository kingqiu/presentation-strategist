#!/usr/bin/env python3
"""Package the canonical presentation-strategist skill for common agent platforms."""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "presentation-strategist"
DIST = ROOT / "dist"

TARGETS = {
    "codex": DIST / "codex" / "skills" / "presentation-strategist",
    "claude": DIST / "claude" / ".claude" / "skills" / "presentation-strategist",
    "openclaw": DIST / "openclaw" / "presentation-strategist",
    "hermes": DIST / "hermes" / "skills" / "presentation-strategist",
}

REQUIRED_FILES = [
    "SKILL.md",
    "references/business-scenarios.md",
    "references/strategic-communication-principles.md",
    "references/handoff-schema.md",
    "references/qa-rubric.md",
    "templates/ai-ppt-generation-brief.md",
    "templates/presentation-brief.md",
    "templates/slide-plan.yaml",
]


def read_skill_frontmatter() -> tuple[str, str]:
    text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"---\n(.*?)\n---", text, re.S)
    if not match:
        raise ValueError("SKILL.md frontmatter is missing")
    fields = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip().strip('"')
    return fields.get("name", ""), fields.get("description", "")


def validate() -> list[str]:
    errors: list[str] = []
    if not SKILL.exists():
        errors.append("presentation-strategist/ directory is missing")
        return errors

    name, description = read_skill_frontmatter()
    if name != "presentation-strategist":
        errors.append("SKILL.md name must be presentation-strategist")
    if not description:
        errors.append("SKILL.md description is missing")
    if "\n" in description:
        errors.append("SKILL.md description must be one line")
    if len(description) > 160:
        errors.append("SKILL.md description should stay under 160 characters for cross-platform compatibility")

    for rel in REQUIRED_FILES:
        if not (SKILL / rel).exists():
            errors.append(f"required file missing: {rel}")

    return errors


def package(targets: list[str], clean: bool) -> None:
    errors = validate()
    if errors:
        raise SystemExit("\n".join(errors))

    if clean and DIST.exists():
        shutil.rmtree(DIST)

    selected = targets or list(TARGETS)
    for target in selected:
        dest = TARGETS[target]
        if dest.exists():
            shutil.rmtree(dest)
        shutil.copytree(
            SKILL,
            dest,
            ignore=shutil.ignore_patterns(".DS_Store", "__pycache__"),
        )
        print(f"packaged {target}: {dest.relative_to(ROOT)}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Package presentation-strategist for agent platforms.")
    parser.add_argument("--check", action="store_true", help="validate only")
    parser.add_argument("--clean", action="store_true", help="remove dist before packaging")
    parser.add_argument("--target", choices=sorted(TARGETS), action="append", help="package one target; repeatable")
    args = parser.parse_args()

    errors = validate()
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    if args.check:
        print("package check passed")
        return 0

    package(args.target or [], args.clean)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
