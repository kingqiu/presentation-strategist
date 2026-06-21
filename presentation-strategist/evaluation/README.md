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

## Agent Command Examples

`run_validation.py` can either generate prompt files only, or execute an external agent command for each sample.

Prompt-only mode:

```bash
scripts/run_validation.py --skill-dir . --run-name current --limit 3
```

Generic stdin-to-file command template:

```bash
scripts/run_validation.py \
  --skill-dir . \
  --run-name current \
  --agent-command 'your-agent < {prompt_file} > {output_file}'
```

Codex-style template, if your Codex CLI supports non-interactive prompt execution:

```bash
scripts/run_validation.py \
  --skill-dir . \
  --run-name current \
  --agent-command 'codex exec --full-auto --cd {skill_dir} < {prompt_file} > {output_file}'
```

Claude-style template, if your Claude CLI supports print/non-interactive mode:

```bash
scripts/run_validation.py \
  --skill-dir . \
  --run-name current \
  --agent-command 'claude -p "$(cat {prompt_file})" > {output_file}'
```

Treat these as command templates. Adjust flags to match the agent CLI installed in your environment. The placeholders `{prompt_file}`, `{output_file}`, `{sample_id}`, and `{skill_dir}` are filled by `run_validation.py`.

## Scoring Modes

By default, `score_outputs.py` uses a deterministic local scorer. This is dependency-free and stable enough for smoke tests and regression checks.

Default scoring:

```bash
scripts/score_outputs.py --skill-dir . --run-name current
```

For deeper semantic judging, pass a judge command. The judge command receives a prompt file containing the validation sample, output, and rubric. It must return JSON on stdout or write JSON to `{output_file}`.

```bash
scripts/score_outputs.py \
  --skill-dir . \
  --run-name current \
  --judge-command 'your-judge < {prompt_file} > {output_file}'
```

Expected judge JSON:

```json
{
  "dimension_scores": {
    "goal_and_audience": 18,
    "input_convergence": 12,
    "storyline": 17,
    "evidence_and_risk": 13,
    "slide_usability": 16,
    "output_fit": 9
  },
  "hard_penalty": 0,
  "failure_tags": ["weak_evidence_handling"],
  "rationale": "Brief reason for the score."
}
```

If the judge command fails, times out, or returns invalid JSON, the script falls back to deterministic scoring and records `judge_error` on that sample. Use `--no-fallback` when you want judge failures to fail the run.

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

Generate a readable report:

```bash
scripts/summarize_evolution.py --skill-dir . --limit 10
scripts/summarize_evolution.py --skill-dir . --limit 10 --out evaluation/evolution_report.md
```

## Improvement Policy

Use validation results to propose small candidate edits only.

- Keep each edit under 5-10% of the touched file.
- Apply edits to a candidate copy before touching the deployed skill.
- Accept only edits that improve the validation set without worsening high-risk cases.
- Record rejected edits so future proposals avoid repeated mistakes.
