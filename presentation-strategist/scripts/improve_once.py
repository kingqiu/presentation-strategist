#!/usr/bin/env python3
"""Run one user-friendly self-improvement cycle.

This wrapper keeps the individual self-improvement scripts available while
giving normal users one command to start a safe cycle.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


MODES = {"report-only", "candidate", "auto-gate"}


def run(command: list[str], cwd: Path, allow_failure: bool = False) -> subprocess.CompletedProcess:
    printable = " ".join(command)
    print(f"$ {printable}")
    result = subprocess.run(command, cwd=cwd)
    if result.returncode != 0 and not allow_failure:
        raise SystemExit(result.returncode)
    return result


def run_capture(command: list[str], cwd: Path, allow_failure: bool = False) -> subprocess.CompletedProcess:
    printable = " ".join(command)
    print(f"$ {printable}")
    result = subprocess.run(command, cwd=cwd, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout, end="")
    if result.stderr:
        print(result.stderr, end="", file=sys.stderr)
    if result.returncode != 0 and not allow_failure:
        raise SystemExit(result.returncode)
    return result


def read_manifest_samples(skill_dir: Path, run_name: str) -> list[str]:
    manifest = skill_dir / "evaluation" / "runs" / run_name / "manifest.json"
    if not manifest.exists():
        return []
    return json.loads(manifest.read_text(encoding="utf-8")).get("samples", [])


def missing_outputs(skill_dir: Path, run_name: str) -> list[str]:
    outputs_dir = skill_dir / "evaluation" / "runs" / run_name / "outputs"
    return [sample_id for sample_id in read_manifest_samples(skill_dir, run_name) if not (outputs_dir / f"{sample_id}.md").exists()]


def write_summary(skill_dir: Path, run_name: str, mode: str, report_path: Path, status: str, notes: list[str]) -> None:
    summary = {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "run_name": run_name,
        "mode": mode,
        "status": status,
        "report": str(report_path),
        "notes": notes,
    }
    path = skill_dir / "evaluation" / "runs" / run_name / "improve_once_summary.json"
    path.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skill-dir", default=".", help="Path to presentation-strategist skill directory.")
    parser.add_argument("--run-name", help="Run name. Defaults to improve-YYYYMMDD-HHMMSS.")
    parser.add_argument("--limit", type=int, default=10, help="Number of validation samples to run.")
    parser.add_argument("--mode", choices=sorted(MODES), default="report-only")
    parser.add_argument("--agent-command", help="Optional command template to produce validation outputs.")
    parser.add_argument("--judge-command", help="Optional command template for LLM judge scoring.")
    parser.add_argument("--candidate-run", help="Candidate run name for auto-gate mode.")
    parser.add_argument("--max-tags", type=int, default=3, help="Maximum failure tags to use for candidate edits.")
    parser.add_argument("--report-out", help="Optional report output path.")
    args = parser.parse_args()

    skill_dir = Path(args.skill_dir).resolve()
    scripts = skill_dir / "scripts"
    run_name = args.run_name or f"improve-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
    report_path = Path(args.report_out) if args.report_out else skill_dir / "evaluation" / "runs" / run_name / "evolution_report.md"
    if not report_path.is_absolute():
        report_path = skill_dir / report_path

    notes: list[str] = []

    run_validation = [sys.executable, str(scripts / "run_validation.py"), "--skill-dir", str(skill_dir), "--run-name", run_name, "--limit", str(args.limit)]
    if args.agent_command:
        run_validation.extend(["--agent-command", args.agent_command])
    run(run_validation, skill_dir)

    missing = missing_outputs(skill_dir, run_name)
    if missing:
        notes.append(f"{len(missing)} outputs are missing. Fill evaluation/runs/{run_name}/outputs/<sample-id>.md, then rerun with the same run name.")
        run([sys.executable, str(scripts / "summarize_evolution.py"), "--skill-dir", str(skill_dir), "--limit", "10", "--out", str(report_path)], skill_dir)
        write_summary(skill_dir, run_name, args.mode, report_path, "waiting_for_outputs", notes)
        print("\nNext step:")
        print(f"- Add outputs for missing samples under evaluation/runs/{run_name}/outputs/")
        print(f"- Then rerun: scripts/improve_once.py --skill-dir . --run-name {run_name} --mode {args.mode}")
        return 0

    score_command = [sys.executable, str(scripts / "score_outputs.py"), "--skill-dir", str(skill_dir), "--run-name", run_name]
    if args.judge_command:
        score_command.extend(["--judge-command", args.judge_command])
    run(score_command, skill_dir)

    if args.mode in {"candidate", "auto-gate"}:
        propose = [
            sys.executable,
            str(scripts / "propose_candidate_edit.py"),
            "--skill-dir",
            str(skill_dir),
            "--run-name",
            run_name,
            "--max-tags",
            str(args.max_tags),
            "--create-candidate",
        ]
        run(propose, skill_dir)

    if args.mode == "auto-gate":
        if not args.candidate_run:
            notes.append("auto-gate mode needs --candidate-run after candidate outputs have been generated and scored.")
            print("auto-gate skipped: provide --candidate-run after scoring a candidate run.")
        else:
            gate = [
                sys.executable,
                str(scripts / "gate_candidate.py"),
                "--skill-dir",
                str(skill_dir),
                "--current-run",
                run_name,
                "--candidate-run",
                args.candidate_run,
            ]
            run(gate, skill_dir, allow_failure=True)

    run([sys.executable, str(scripts / "summarize_evolution.py"), "--skill-dir", str(skill_dir), "--limit", "10", "--out", str(report_path)], skill_dir)
    status = "completed"
    if args.mode == "report-only":
        notes.append("Report-only mode does not create or gate candidate edits.")
    elif args.mode == "candidate":
        notes.append("Candidate mode created a candidate skill copy but did not gate or accept it.")
    write_summary(skill_dir, run_name, args.mode, report_path, status, notes)

    print("\nSelf-improvement cycle complete.")
    print(f"- Run: {run_name}")
    print(f"- Mode: {args.mode}")
    print(f"- Report: {report_path}")
    for note in notes:
        print(f"- Note: {note}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

