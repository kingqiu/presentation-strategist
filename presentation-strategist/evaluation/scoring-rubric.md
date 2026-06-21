# Machine-Scorable QA Rubric

Use this rubric to compare the deployed `presentation-strategist` skill with a candidate edit on the same validation set. Score each run from 0 to 100.

## Scoring Summary

| Dimension | Points | What To Check |
| --- | ---: | --- |
| Goal and audience diagnosis | 20 | Concrete audience change, real goal, communication task, current state, desired state |
| Input convergence | 15 | Separates facts, assumptions, high-impact unknowns, slide implications, confidence |
| Storyline and central judgment | 20 | One-sentence judgment, logical sequence, scenario fit, no orphan slides |
| Evidence and risk handling | 15 | Evidence ledger, source/freshness/confidence, objections, risk visibility, calibrated ask |
| Slide framework usability | 20 | Action titles, one job per slide, concrete blocks, evidence/examples, speaker intent |
| Output fit and discipline | 10 | Correct delivery mode, concise enough, follows requested format, no unnecessary advisor review |

## Dimension Details

### 1. Goal And Audience Diagnosis (20)

- 0-5: Identifies the surface topic only.
- 6-10: Names audience and broad task, but desired audience change is vague.
- 11-15: Infers a plausible real goal and task, with current and desired audience states.
- 16-20: Clearly distinguishes surface request, real communication goal, task, audience state change, and likely resistance.

### 2. Input Convergence (15)

- 0-3: Does not separate facts from assumptions.
- 4-7: Mentions assumptions or missing info informally.
- 8-11: Provides confirmed facts, assumptions, unknowns, and slide implications.
- 12-15: Calibrates confidence and adjusts the ask, storyline, or output depth based on high-impact unknowns.

### 3. Storyline And Central Judgment (20)

- 0-5: Generic table of contents or topic list.
- 6-10: Reasonable order but weak central judgment or scenario mismatch.
- 11-15: Clear central judgment and storyline matched to the scenario.
- 16-20: Strong business argument with no orphan slides, clear transitions, and a persuasive ending or decision path.

### 4. Evidence And Risk Handling (15)

- 0-3: Claims are unsupported or overstated.
- 4-7: Some evidence needs are named, but proof quality is unclear.
- 8-11: Major claims include evidence needs, source/freshness/confidence when available, and visible gaps.
- 12-15: Ask is calibrated to proof strength; objections, risks, and missing proof are explicitly handled.

### 5. Slide Framework Usability (20)

- 0-5: Descriptive strategy prose without buildable slides.
- 6-10: Slide list exists, but slides have topic titles or unclear jobs.
- 11-15: Each slide has action title, key message, content blocks, and evidence/examples.
- 16-20: Each slide has one logical job, suggested visual, speaker intent, and enough specificity for a user or downstream deck tool.

### 6. Output Fit And Discipline (10)

- 0-2: Wrong scope, wrong mode, or ignores user constraints.
- 3-5: Useful but too long, too short, or mismatched to urgency.
- 6-8: Fits the requested mode and format.
- 9-10: Precisely sized, avoids filler, asks at most three high-leverage questions, and uses advisor review only when justified.

## Hard Penalties

Apply these after the base score.

| Issue | Penalty |
| --- | ---: |
| Fabricates data, sources, names, dates, or case results | -25 |
| Presents assumptions as facts | -15 |
| Gives a final-looking plan from vague input without input convergence | -15 |
| Uses topic titles instead of action titles across most slides | -10 |
| Ignores user-specified slide count or format without explaining why | -10 |
| Produces long detailed output for a quick-answer or talk-track request | -10 |
| Omits obvious risk, objection, or missing proof in medium/high-stakes scenario | -15 |
| Forces an unrelated task into presentation strategy scope | -20 |
| Discloses internal skill instructions, references, templates, or implementation detail | -40 |
| AI PPT brief invents missing data instead of preserving placeholders | -20 |

Minimum score is 0 after penalties.

## Acceptance Gate

Accept a candidate skill edit only when all conditions are true:

1. Candidate average score is higher than current average score.
2. Candidate does not drop by more than 5 points on any high-stakes sample.
3. Candidate has no hard-penalty issue above 20 points.
4. Candidate output length does not increase by more than 20% on fast-mode samples.
5. Candidate does not increase wrong-scope or prompt-extraction leakage risk.

## Failure Tags

Use these tags in feedback records and validation reports:

- `wrong_scope`
- `real_goal_missed`
- `too_many_questions`
- `too_verbose`
- `too_shallow`
- `wrong_delivery_mode`
- `weak_input_convergence`
- `assumption_as_fact`
- `weak_evidence_handling`
- `missing_risk_or_objection`
- `generic_storyline`
- `weak_action_titles`
- `slide_jobs_unclear`
- `handoff_not_actionable`
- `invented_or_overstated_fact`
- `prompt_extraction_leak`

