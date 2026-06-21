# Changelog

## Unreleased

### Added

- Added `summarize_evolution.py` to produce a readable report from evolution ledgers.
- Added `improve_once.py`, a one-command wrapper for normal users to run report-only, candidate, or auto-gate self-improvement cycles.
- Added self-improvement `--agent-command` examples to the evaluation documentation.
- Expanded the validation set from 30 to 60 samples, including complex material inputs, English presentation scenarios, handoff targets, quick talk tracks, and adversarial/safety cases.
- Added optional `--judge-command` support to `score_outputs.py` for LLM-based semantic judging with deterministic fallback.

### Changed

- Improved candidate edit generation to apply targeted section-level calibration patches instead of one centralized calibration block.
- Updated package validation to require the evolution summary script.

## 0.1.0

Initial public-ready skill package for `presentation-strategist`.

### Added

- Core `presentation-strategist` skill for presentation logic, storyline, evidence handling, slide planning, critique, rewrite, and AI PPT handoff.
- Scenario references for boss updates, sales decks, fundraising pitches, product and company introductions, business reviews, technical reviews, risk briefings, AI literacy training, and related presentation contexts.
- Templates for human-readable presentation briefs, logic reviews, AI PPT generation briefs, and YAML slide plans.
- Codex interface metadata in `agents/openai.yaml`.
- Evaluation assets:
  - `evaluation/validation_set.jsonl` with 30 validation samples.
  - `evaluation/scoring-rubric.md` with a 100-point scoring rubric and hard penalties.
  - `evaluation/feedback/records.schema.json` for future usage feedback records.
- Self-improvement engine scripts:
  - `run_validation.py`
  - `score_outputs.py`
  - `propose_candidate_edit.py`
  - `gate_candidate.py`
- Release tooling:
  - `validate_skill_package.py`
  - `package_skill.py`
  - package cleanup rules for runtime logs and generated files.

### Notes

- The self-improvement loop is agent-command driven. It can generate validation prompts by itself, but model outputs require either manual placement under `evaluation/runs/<run>/outputs/` or an external agent command passed through `--agent-command`.
- Runtime logs and feedback records are intentionally excluded from release packages.
