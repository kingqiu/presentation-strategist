#!/usr/bin/env python3
"""Compare current and candidate validation scores and accept or reject."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def by_id(report: dict) -> dict[str, dict]:
    return {row["sample_id"]: row for row in report.get("results", [])}


def high_stakes_regressions(current: dict, candidate: dict, max_drop: float) -> list[dict]:
    current_rows = by_id(current)
    candidate_rows = by_id(candidate)
    drops = []
    for sample_id, row in current_rows.items():
        if row.get("stakes") != "high" or sample_id not in candidate_rows:
            continue
        drop = row["score"] - candidate_rows[sample_id]["score"]
        if drop > max_drop:
            drops.append({"sample_id": sample_id, "drop": drop, "current": row["score"], "candidate": candidate_rows[sample_id]["score"]})
    return drops


def severe_penalties(candidate: dict) -> list[dict]:
    return [
        {"sample_id": row["sample_id"], "hard_penalty": row.get("hard_penalty", 0), "failure_tags": row.get("failure_tags", [])}
        for row in candidate.get("results", [])
        if row.get("hard_penalty", 0) > 20
    ]


def fast_mode_length_regressions(current: dict, candidate: dict) -> list[dict]:
    current_rows = by_id(current)
    candidate_rows = by_id(candidate)
    regressions = []
    fast_modes = {"quick_answer", "talk_track", "five_slide_framework", "out_of_scope_response"}
    for sample_id, row in current_rows.items():
        if row.get("expected_delivery_mode") not in fast_modes or sample_id not in candidate_rows:
            continue
        current_len = max(row.get("output_length_words", 1), 1)
        candidate_len = candidate_rows[sample_id].get("output_length_words", 0)
        if candidate_len > current_len * 1.2:
            regressions.append({"sample_id": sample_id, "current_words": current_len, "candidate_words": candidate_len})
    return regressions


def leakage_regressions(current: dict, candidate: dict) -> list[dict]:
    current_rows = by_id(current)
    candidate_rows = by_id(candidate)
    leaks = []
    for sample_id, row in candidate_rows.items():
        candidate_tags = set(row.get("failure_tags", []))
        current_tags = set(current_rows.get(sample_id, {}).get("failure_tags", []))
        if "prompt_extraction_leak" in candidate_tags and "prompt_extraction_leak" not in current_tags:
            leaks.append({"sample_id": sample_id})
    return leaks


def top_tags(report: dict, limit: int = 5) -> list[str]:
    counts = report.get("tag_counts", {})
    return [tag for tag, _ in sorted(counts.items(), key=lambda item: item[1], reverse=True)[:limit]]


def append_jsonl(path: Path, row: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skill-dir", default=".")
    parser.add_argument("--current-run", required=True)
    parser.add_argument("--candidate-run", required=True)
    parser.add_argument("--max-high-stakes-drop", type=float, default=5.0)
    args = parser.parse_args()

    skill_dir = Path(args.skill_dir).resolve()
    current = load(skill_dir / "evaluation" / "runs" / args.current_run / "scores.json")
    candidate = load(skill_dir / "evaluation" / "runs" / args.candidate_run / "scores.json")

    avg_delta = candidate.get("average_score", 0) - current.get("average_score", 0)
    blockers = {
        "average_not_improved": avg_delta <= 0,
        "high_stakes_regressions": high_stakes_regressions(current, candidate, args.max_high_stakes_drop),
        "severe_penalties": severe_penalties(candidate),
        "fast_mode_length_regressions": fast_mode_length_regressions(current, candidate),
        "leakage_regressions": leakage_regressions(current, candidate),
    }
    accepted = not blockers["average_not_improved"] and not blockers["high_stakes_regressions"] and not blockers["severe_penalties"] and not blockers["fast_mode_length_regressions"] and not blockers["leakage_regressions"]

    decision = {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "current_run": args.current_run,
        "candidate_run": args.candidate_run,
        "current_average": current.get("average_score"),
        "candidate_average": candidate.get("average_score"),
        "average_delta": round(avg_delta, 2),
        "accepted": accepted,
        "blockers": blockers,
    }
    decision_path = skill_dir / "evaluation" / "runs" / args.candidate_run / "gate_decision.json"
    decision_path.write_text(json.dumps(decision, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    proposal_path = skill_dir / "evaluation" / "runs" / args.current_run / "candidate_edit_proposal.json"
    tags = []
    proposal = {}
    if proposal_path.exists():
        proposal = load(proposal_path)
        tags = proposal.get("selected_failure_tags", [])

    log_row = {
        "timestamp": decision["created_at"],
        "current_run": args.current_run,
        "candidate_run": args.candidate_run,
        "accepted": accepted,
        "current_average": current.get("average_score"),
        "candidate_average": candidate.get("average_score"),
        "average_delta": round(avg_delta, 2),
        "selected_failure_tags": tags,
        "current_top_failure_tags": top_tags(current),
        "candidate_top_failure_tags": top_tags(candidate),
        "blocker_summary": {
            "average_not_improved": blockers["average_not_improved"],
            "high_stakes_regression_count": len(blockers["high_stakes_regressions"]),
            "severe_penalty_count": len(blockers["severe_penalties"]),
            "fast_mode_length_regression_count": len(blockers["fast_mode_length_regressions"]),
            "leakage_regression_count": len(blockers["leakage_regressions"]),
        },
        "artifacts": {
            "current_scores": f"evaluation/runs/{args.current_run}/scores.json",
            "candidate_scores": f"evaluation/runs/{args.candidate_run}/scores.json",
            "candidate_proposal": f"evaluation/runs/{args.current_run}/candidate_edit_proposal.json" if proposal else None,
            "gate_decision": f"evaluation/runs/{args.candidate_run}/gate_decision.json",
            "candidate_skill_dir": proposal.get("candidate_skill_dir"),
        },
    }
    append_jsonl(skill_dir / "evaluation" / "evolution_log.jsonl", log_row)

    if accepted:
        append_jsonl(skill_dir / "evaluation" / "accepted_edits.jsonl", {
            "timestamp": decision["created_at"],
            "candidate_run": args.candidate_run,
            "tags": tags,
            "average_delta": round(avg_delta, 2),
            "candidate_skill_dir": proposal.get("candidate_skill_dir"),
            "gate_decision": f"evaluation/runs/{args.candidate_run}/gate_decision.json",
        })

    if not accepted:
        append_jsonl(skill_dir / "evaluation" / "rejected_edits.jsonl", {
            "timestamp": decision["created_at"],
            "candidate_run": args.candidate_run,
            "tags": tags,
            "reason": blockers,
        })

    print("accepted" if accepted else "rejected")
    print(json.dumps(decision, ensure_ascii=False, indent=2))
    return 0 if accepted else 1


if __name__ == "__main__":
    raise SystemExit(main())
