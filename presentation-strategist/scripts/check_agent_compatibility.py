#!/usr/bin/env python3
"""Check cross-agent compatibility metadata for presentation-strategist."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


AGENTS = {
    "Codex": "~/.codex/skills/presentation-strategist",
    "Claude Code": "~/.claude/skills/presentation-strategist",
    "OpenClaw": "~/.openclaw/skills/presentation-strategist",
    "Hermes Agent": "~/.hermes/skills/presentation-strategist",
}


def check(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    compatibility = skill_dir / "agents" / "compatibility.md"
    openai = skill_dir / "agents" / "openai.yaml"

    if not skill_md.is_file():
        errors.append("Missing SKILL.md")
    if not compatibility.is_file():
        errors.append("Missing agents/compatibility.md")
    if not openai.is_file():
        errors.append("Missing agents/openai.yaml")

    if skill_md.is_file():
        text = skill_md.read_text(encoding="utf-8")
        for term in ["presentation-strategist", "not visual editing", "PPT", "presentation"]:
            if term not in text:
                errors.append(f"SKILL.md missing compatibility trigger term: {term}")

    if compatibility.is_file():
        text = compatibility.read_text(encoding="utf-8")
        for agent, install_path in AGENTS.items():
            if agent not in text:
                errors.append(f"agents/compatibility.md missing agent: {agent}")
            if install_path not in text:
                errors.append(f"agents/compatibility.md missing install path: {install_path}")
        for term in ["SKILL.md", "references/", "templates/", "agents/openai.yaml"]:
            if term not in text:
                errors.append(f"agents/compatibility.md missing loader guidance: {term}")

    if openai.is_file():
        text = openai.read_text(encoding="utf-8")
        for term in ["display_name", "short_description", "default_prompt", "$presentation-strategist"]:
            if term not in text:
                errors.append(f"agents/openai.yaml missing field or trigger: {term}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("skill_dir", nargs="?", default=".", help="Skill directory to check.")
    args = parser.parse_args()

    errors = check(Path(args.skill_dir).resolve())
    if errors:
        print("Agent compatibility check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Agent compatibility check passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
