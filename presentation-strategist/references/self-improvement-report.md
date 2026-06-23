# Self-Improvement Report Template

Use this when a user asks to run, inspect, or understand a `presentation-strategist` self-improvement cycle.

## Reader Goal

The report should tell a non-technical user:

- what was tested
- whether outputs are still missing
- what the current score says, if scoring has run
- which failure patterns matter most
- whether a candidate edit was proposed or gated
- what the safest next action is

Do not make the user inspect raw run folders unless they ask.

## Report Shape

```markdown
# Self-Improvement Report

Run: `<run-name>`
Mode: `<report-only | candidate | auto-gate>`
Status: `<waiting_for_outputs | scored | candidate_created | gated | completed>`

## What Happened

- Samples selected: `<n>`
- Outputs found: `<n>`
- Outputs missing: `<n>`
- Scoring: `<not run | deterministic | judge | deterministic fallback>`
- Candidate edit: `<none | proposed | created | gated>`

## Current Signal

- Average score: `<score or n/a>`
- Strongest scenarios: `<scenario list or n/a>`
- Weakest scenarios: `<scenario list or n/a>`
- Top failure tags: `<tag list or n/a>`

## Interpretation

Explain the result in plain language. Focus on whether the skill is struggling with scope, real-goal diagnosis, evidence handling, action titles, handoff briefs, or output length.

## Recommended Next Action

Choose one:

- Add missing outputs, then rerun the same run.
- Keep report-only; no edit is needed yet.
- Create a bounded candidate edit.
- Score the candidate run.
- Gate the candidate.
- Reject or revise the candidate because it harms high-risk cases.

## Audit Pointers

- Manifest: `evaluation/runs/<run>/manifest.json`
- Prompts: `evaluation/runs/<run>/prompts/`
- Outputs: `evaluation/runs/<run>/outputs/`
- Scores: `evaluation/runs/<run>/scores.json`
- Candidate proposal: `evaluation/runs/<run>/candidate_edit_proposal.json`
```

## Tone

Use direct, calm language. Avoid saying the skill "improved" unless the gate has accepted a candidate or scores show a clear positive change without high-risk regressions.

