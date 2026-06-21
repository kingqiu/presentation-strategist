#!/usr/bin/env python3
"""Validate presentation-strategist as a shareable skill package.

This script intentionally uses only the Python standard library so it can run
in clean environments where PyYAML or other packages are unavailable.
"""

from __future__ import annotations

import argparse
import ast
import json
import re
import sys
from pathlib import Path


REQUIRED_FILES = [
    "SKILL.md",
    "VERSION",
    "agents/compatibility.md",
    "agents/openai.yaml",
    "evaluation/README.md",
    "evaluation/scoring-rubric.md",
    "evaluation/validation_set.jsonl",
    "evaluation/feedback/records.schema.json",
]

FORBIDDEN_PATTERNS = [
    "__pycache__",
    ".DS_Store",
    ".pyc",
    "evaluation/runs",
    "evaluation/evolution_log.jsonl",
    "evaluation/accepted_edits.jsonl",
    "evaluation/rejected_edits.jsonl",
    "evaluation/feedback/records.jsonl",
]


def error(errors: list[str], message: str) -> None:
    errors.append(message)


def parse_frontmatter(skill_md: str, errors: list[str]) -> dict[str, str]:
    if not skill_md.startswith("---\n"):
        error(errors, "SKILL.md must start with YAML frontmatter.")
        return {}
    parts = skill_md.split("---", 2)
    if len(parts) < 3:
        error(errors, "SKILL.md frontmatter must be closed with ---.")
        return {}
    frontmatter = parts[1]
    values: dict[str, str] = {}
    for raw in frontmatter.splitlines():
        line = raw.strip()
        if not line or ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def validate_required_files(root: Path, errors: list[str]) -> None:
    for rel in REQUIRED_FILES:
        if not (root / rel).is_file():
            error(errors, f"Missing required file: {rel}")


def validate_forbidden_files(root: Path, errors: list[str], allow_runtime: bool) -> None:
    if allow_runtime:
        return
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(root).as_posix()
        if any(pattern in rel for pattern in FORBIDDEN_PATTERNS):
            error(errors, f"Forbidden runtime/generated file in package: {rel}")


def validate_skill_md(root: Path, errors: list[str]) -> None:
    path = root / "SKILL.md"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    values = parse_frontmatter(text, errors)
    if values.get("name") != "presentation-strategist":
        error(errors, "SKILL.md frontmatter name must be presentation-strategist.")
    description = values.get("description", "")
    if len(description) < 40:
        error(errors, "SKILL.md description is too short for reliable triggering.")
    if "presentation" not in description.lower() and "ppt" not in description.lower():
        error(errors, "SKILL.md description should mention presentation or PPT scope.")
    if "not visual editing" not in description.lower():
        error(errors, "SKILL.md description should preserve the not-visual-editing boundary.")


def validate_openai_yaml(root: Path, errors: list[str]) -> None:
    path = root / "agents" / "openai.yaml"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    for field in ["display_name", "short_description", "default_prompt"]:
        if not re.search(rf"^\s*{field}\s*:", text, re.M):
            error(errors, f"agents/openai.yaml missing interface.{field}.")
    if "$presentation-strategist" not in text:
        error(errors, "agents/openai.yaml default_prompt should mention $presentation-strategist.")


def validate_agent_compatibility(root: Path, errors: list[str]) -> None:
    path = root / "agents" / "compatibility.md"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    required_terms = [
        "Codex",
        "Claude Code",
        "OpenClaw",
        "Hermes Agent",
        "SKILL.md",
        "agents/openai.yaml",
    ]
    for term in required_terms:
        if term not in text:
            error(errors, f"agents/compatibility.md should mention {term}.")
    for install_path in [
        "~/.codex/skills/presentation-strategist",
        "~/.claude/skills/presentation-strategist",
        "~/.openclaw/skills/presentation-strategist",
        "~/.hermes/skills/presentation-strategist",
    ]:
        if install_path not in text:
            error(errors, f"agents/compatibility.md missing install path: {install_path}")


def validate_json_files(root: Path, errors: list[str]) -> None:
    json_file = root / "evaluation" / "feedback" / "records.schema.json"
    if json_file.exists():
        try:
            json.loads(json_file.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            error(errors, f"Invalid JSON in {json_file.relative_to(root)}: {exc}")

    jsonl = root / "evaluation" / "validation_set.jsonl"
    if jsonl.exists():
        ids: set[str] = set()
        rows = []
        for index, line in enumerate(jsonl.read_text(encoding="utf-8").splitlines(), start=1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as exc:
                error(errors, f"Invalid JSONL at validation_set.jsonl:{index}: {exc}")
                continue
            rows.append(row)
            sample_id = row.get("id")
            if not sample_id:
                error(errors, f"validation_set.jsonl:{index} missing id.")
            elif sample_id in ids:
                error(errors, f"Duplicate validation sample id: {sample_id}")
            ids.add(sample_id)
            for field in ["scenario", "stakes", "user_input", "expected_delivery_mode"]:
                if field not in row:
                    error(errors, f"validation_set.jsonl:{index} missing {field}.")
        if len(rows) < 20:
            error(errors, "validation_set.jsonl should contain at least 20 samples.")


def validate_scripts(root: Path, errors: list[str]) -> None:
    scripts_dir = root / "scripts"
    if not scripts_dir.exists():
        error(errors, "Missing scripts directory.")
        return
    expected = {
        "run_validation.py",
        "score_outputs.py",
        "propose_candidate_edit.py",
        "gate_candidate.py",
        "improve_once.py",
        "summarize_evolution.py",
        "check_agent_compatibility.py",
        "validate_skill_package.py",
        "package_skill.py",
    }
    found = {p.name for p in scripts_dir.glob("*.py")}
    missing = expected - found
    for name in sorted(missing):
        error(errors, f"Missing script: scripts/{name}")
    for path in scripts_dir.glob("*.py"):
        try:
            ast.parse(path.read_text(encoding="utf-8"))
        except SyntaxError as exc:
            error(errors, f"Python syntax error in {path.relative_to(root)}: {exc}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("skill_dir", nargs="?", default=".", help="Skill directory to validate.")
    parser.add_argument("--allow-runtime", action="store_true", help="Allow local runtime logs while validating source tree structure.")
    args = parser.parse_args()

    root = Path(args.skill_dir).resolve()
    errors: list[str] = []

    validate_required_files(root, errors)
    validate_forbidden_files(root, errors, args.allow_runtime)
    validate_skill_md(root, errors)
    validate_openai_yaml(root, errors)
    validate_agent_compatibility(root, errors)
    validate_json_files(root, errors)
    validate_scripts(root, errors)

    if errors:
        print("Skill package validation failed:")
        for item in errors:
            print(f"- {item}")
        return 1

    print(f"Skill package is share-ready: {root}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
