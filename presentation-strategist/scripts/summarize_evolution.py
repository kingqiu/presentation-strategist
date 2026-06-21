#!/usr/bin/env python3
"""Summarize presentation-strategist self-improvement history."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def fmt_score(value: object) -> str:
    if isinstance(value, int | float):
        return f"{value:.2f}"
    return "n/a"


def summarize(skill_dir: Path, limit: int) -> str:
    evaluation = skill_dir / "evaluation"
    rows = read_jsonl(evaluation / "evolution_log.jsonl")
    accepted = read_jsonl(evaluation / "accepted_edits.jsonl")
    rejected = read_jsonl(evaluation / "rejected_edits.jsonl")

    shown = rows[-limit:] if limit and len(rows) > limit else rows
    tag_counts = Counter(tag for row in rows for tag in row.get("selected_failure_tags", []))
    accepted_count = sum(1 for row in rows if row.get("accepted"))
    rejected_count = len(rows) - accepted_count

    lines = [
        "# Presentation Strategist Evolution Report",
        "",
        f"- Total gated rounds: {len(rows)}",
        f"- Accepted: {accepted_count}",
        f"- Rejected: {rejected_count}",
        f"- Accepted edit records: {len(accepted)}",
        f"- Rejected edit records: {len(rejected)}",
    ]

    if rows:
        first = rows[0]
        latest = rows[-1]
        lines.extend(
            [
                f"- First recorded round: {first.get('timestamp', 'n/a')}",
                f"- Latest recorded round: {latest.get('timestamp', 'n/a')}",
                f"- Latest average delta: {fmt_score(latest.get('average_delta'))}",
            ]
        )

    if tag_counts:
        lines.extend(["", "## Top Failure Tags", ""])
        for tag, count in tag_counts.most_common(10):
            lines.append(f"- `{tag}`: {count}")

    lines.extend(["", f"## Recent Rounds ({len(shown)})", ""])
    if not shown:
        lines.append("No evolution rounds recorded yet.")
    else:
        for row in shown:
            status = "accepted" if row.get("accepted") else "rejected"
            blockers = row.get("blocker_summary", {})
            blocker_bits = []
            for key, value in blockers.items():
                if value:
                    blocker_bits.append(f"{key}={value}")
            blocker_text = ", ".join(blocker_bits) if blocker_bits else "none"
            tags = ", ".join(f"`{tag}`" for tag in row.get("selected_failure_tags", [])) or "none"
            lines.extend(
                [
                    f"### {row.get('candidate_run', 'unknown')} ({status})",
                    "",
                    f"- Time: {row.get('timestamp', 'n/a')}",
                    f"- Current run: `{row.get('current_run', 'n/a')}`",
                    f"- Current average: {fmt_score(row.get('current_average'))}",
                    f"- Candidate average: {fmt_score(row.get('candidate_average'))}",
                    f"- Delta: {fmt_score(row.get('average_delta'))}",
                    f"- Selected failure tags: {tags}",
                    f"- Blockers: {blocker_text}",
                    "",
                ]
            )

    lines.extend(["", "## Suggested Next Step", ""])
    if not rows:
        lines.append("Run validation, score outputs, propose a candidate edit, then gate the candidate to create the first evolution record.")
    elif rejected_count and rejected_count >= accepted_count:
        lines.append("Review rejected blockers first. If most candidates fail on average score, improve candidate generation or add stronger validation samples before widening edit scope.")
    else:
        lines.append("Inspect accepted edits and run a fresh validation round to confirm the improvement persists.")

    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skill-dir", default=".", help="Path to presentation-strategist skill directory.")
    parser.add_argument("--limit", type=int, default=10, help="Number of recent rounds to include.")
    parser.add_argument("--out", help="Optional markdown output path.")
    args = parser.parse_args()

    skill_dir = Path(args.skill_dir).resolve()
    report = summarize(skill_dir, args.limit)
    if args.out:
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(report, encoding="utf-8")
    else:
        print(report, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

