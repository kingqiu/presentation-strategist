# Presentation Strategist Evaluation

This directory supports a self-improvement loop for the `presentation-strategist` skill.

## Contents

- `feedback/records.schema.json`: schema for real usage feedback records.
- `feedback/records.jsonl`: append-only feedback log. Start empty and add one JSON object per skill use.
- `scoring-rubric.md`: machine-scorable rubric derived from the human QA rubric.
- `validation_set.jsonl`: held-out validation prompts for regression testing candidate skill edits.
- `runs/`: generated validation runs, model outputs, score reports, and candidate edit proposals.
- `evolution_log.jsonl`: append-only ledger of every candidate gate decision.
- `accepted_edits.jsonl`: accepted candidate edits and score deltas.
- `rejected_edits.jsonl`: rejected candidate edits and blocker reasons.

## Self-Improvement Loop

Run the loop in five steps:

1. Generate or execute validation tasks:
   `scripts/run_validation.py --skill-dir . --run-name current`
2. Put one model output per sample into `evaluation/runs/current/outputs/<sample-id>.md`, or pass `--agent-command` to execute automatically.
3. Score outputs:
   `scripts/score_outputs.py --skill-dir . --run-name current`
4. Propose a bounded candidate edit:
   `scripts/propose_candidate_edit.py --skill-dir . --run-name current`
5. After producing and scoring a candidate run, compare it:
   `scripts/gate_candidate.py --skill-dir . --current-run current --candidate-run candidate`

## What Gets Recorded

Each evolution round records both detailed artifacts and a compact ledger entry.

Per-run artifacts:

- `evaluation/runs/<run>/manifest.json`: samples, run name, timestamp, and execution mode.
- `evaluation/runs/<run>/prompts/<sample-id>.md`: prompt used for each validation sample.
- `evaluation/runs/<run>/outputs/<sample-id>.md`: model output for each sample.
- `evaluation/runs/<run>/scores.json`: per-sample scores, average score, failure tags, scenario scores, and output lengths.
- `evaluation/runs/<current-run>/candidate_edit_proposal.json`: failure tags selected for improvement, target sections, edit type, and candidate skill path when created.
- `evaluation/runs/<candidate-run>/gate_decision.json`: accept/reject decision, score delta, and blocker details.

Cross-round ledgers:

- `evaluation/evolution_log.jsonl`: one line per gate decision, including current/candidate averages, selected failure tags, blocker summary, and artifact links.
- `evaluation/accepted_edits.jsonl`: accepted candidates, score deltas, tags, and candidate skill paths.
- `evaluation/rejected_edits.jsonl`: rejected candidates, tags, and full blocker reasons.

Use `evolution_log.jsonl` as the first place to inspect progress over time. Use the per-run artifacts when you need to audit why a specific round was accepted or rejected.

## Improvement Policy

Use validation results to propose small candidate edits only.

- Keep each edit under 5-10% of the touched file.
- Apply edits to a candidate copy before touching the deployed skill.
- Accept only edits that improve the validation set without worsening high-risk cases.
- Record rejected edits so future proposals avoid repeated mistakes.
