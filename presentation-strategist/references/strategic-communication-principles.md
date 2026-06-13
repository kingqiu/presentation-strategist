# Strategic Communication Principles

Use this reference for the core operating model of `presentation-strategist`.

## 1. The Real Unit Of Work

A presentation is not a container for information. It is an attempt to move an audience from one state to another.

Always identify:

```yaml
audience:
current_state:
desired_state:
stakes:
ask:
```

Audience state changes include:

- unaware -> aware
- confused -> clear
- skeptical -> cautiously convinced
- passive -> urgent
- fragmented -> aligned
- afraid -> trusting
- interested -> ready to act

## 2. Goal Versus Task

Keep these separate:

```text
communication goal = specific audience change the user wants
communication task = abstract communication action needed to create it
```

Examples:

| Concrete goal | Inferred task |
| --- | --- |
| Get the boss to approve 2 headcount and 300k budget | decide / persuade |
| Get a customer to enter PoC and schedule technical review | sell |
| Get product, sales, and delivery teams to prioritize segment A | align |
| Make leadership understand delay risk and cut scope this week | warn / decide |
| Help new hires learn a customer interview method | teach |

Ask for the goal first. Infer the task second. Confirm only if ambiguity matters.

## 3. Surface Request Versus Real Goal

Users often name the format or activity, not the real communication goal.

Detect the likely goal behind the surface request:

| Surface request | Possible real goal |
| --- | --- |
| project progress update | get a decision, warn about risk, request coordination, protect the team, reset expectations |
| product introduction | make the audience believe the product solves a painful problem |
| company introduction | build trust and create a reason to cooperate |
| fundraising deck | turn uncertainty into investor conviction |
| career self-introduction | prove fit and reduce employer risk |
| business review | explain variance and agree on next actions |
| technical comparison | get approval for one option under constraints |

State inferred real goals as assumptions:

```text
You said this is a progress update. I suspect the real goal is to reset expectations and get help removing a cross-functional blocker. I will proceed with that assumption unless you correct it.
```

## 4. Goal Conflict Handling

Some requests contain goals in tension. Do not collapse them into one goal. Name the tension and design around trust.

Examples:

| Tension | Frontstage goal | Backstage goal | Trust constraint | Strategy |
| --- | --- | --- | --- | --- |
| sell without seeming to sell | educate / discuss | create purchase intent | avoid sales pressure | diagnose first, teach criteria, then offer a low-risk path |
| warn without seeming defensive | report risk | force decision | avoid blame or panic | facts -> impact -> options -> decision needed |
| ask for resources without seeming incompetent | update progress | get support | preserve competence | outcome -> gap -> tradeoffs -> resource ask |
| introduce company without sounding generic | present company | win trust/cooperation | avoid brochure tone | audience problem -> relevant capability -> proof -> next action |
| promote self without sounding self-centered | introduce self | win selection | avoid autobiography | role need -> fit thesis -> proof stories -> contribution plan |

Use:

```yaml
frontstage_goal:
backstage_goal:
trust_constraint:
recommended_strategy:
```

## 5. Depth Levels

Adjust output depth to urgency and stakes.

```yaml
fast:
  use_when: deadline is near, user is inexperienced, or input is vague
  output: assumptions -> 3 questions -> likely goal/task -> starter structure -> 3-minute talk track -> evidence checklist

standard:
  use_when: normal strategy planning or scattered materials
  output: diagnosis -> input convergence -> argument -> storyline -> evidence ledger -> slide plan -> risks -> validation questions

high_stakes:
  use_when: board, investors, executive committee, regulator, public crisis, major budget, layoffs, safety, legal, financial forecast, high-risk technical decision
  output: standard + explicit input convergence + five-force scan + pre-wire plan + memo/appendix recommendation + risk/ethics QA
```

Prefer `fast` for vague one-sentence needs unless the field or stakes imply high stakes.

## 6. Input Convergence Gate

When user input is incomplete, do not choose between "ask many questions" and "pretend everything is known." Continue, but make the uncertainty visible.

Before building the slide plan, classify:

```yaml
confirmed_facts:
reasonable_assumptions:
high_impact_unknowns:
slide_implications:
confidence_level:
safe_next_output:
```

Definitions:

- `confirmed_facts`: information explicitly provided by the user or source material
- `reasonable_assumptions`: provisional inferences needed to proceed
- `high_impact_unknowns`: missing information that could change the goal, ask, storyline, proof standard, or slide order
- `slide_implications`: how each assumption or unknown affects the deck
- `confidence_level`: high / medium / low
- `safe_next_output`: full framework, provisional framework, discovery questions, or AI PPT brief with placeholders

Rules:

- Unknown audience + unknown goal means the output must be provisional.
- Unknown evidence strength means the ask must be conservative.
- Unknown decision-maker means include stakeholder validation or pre-wire.
- Unknown proof for a strong claim means label it as a hypothesis or placeholder.
- If high-impact unknowns remain, do not produce a final-sounding AI PPT brief; use placeholders and validation notes.

Example:

```yaml
confirmed_facts:
  - User needs a product introduction deck.
reasonable_assumptions:
  - Audience is a potential enterprise customer.
high_impact_unknowns:
  - decision maker role
  - product proof or customer case
  - desired next step
slide_implications:
  - Use a trust-building sales intro, not a feature catalog.
  - Put proof placeholders into case/result slides.
  - End with discovery or solution review, not purchase commitment.
confidence_level: low
safe_next_output: provisional framework + 3 validation questions
```

## 7. Vertical Six Layers

Use these layers in order.

### Layer 0: Human Communication Atoms

- who is speaking
- who is listening
- why now
- what the audience knows
- what the audience believes
- what the audience cares about
- what the audience fears or resists
- what trust exists
- what stakes exist
- what should change afterward

### Layer 1: Communication Task

Supported labels:

- inform
- explain
- align
- decide
- persuade
- mobilize
- sell
- teach
- review
- warn

Multiple labels are allowed.

### Layer 2: Business Scenario

Scenario changes defaults for proof, language, and structure. Use `business-scenarios.md` for details.

### Layer 3: Business Argument

Build before narrative:

```yaml
central_judgment:
supporting_reasons:
evidence_ledger:
objections:
risks:
missing_proof:
confidence_level:
```

Rules:

- Keep the central judgment to one sentence.
- Attach evidence to every major claim, or label the claim as hypothesis.
- Surface objections before the audience does.
- Make risks visible if they matter to the decision.
- If evidence is weak, lower the ask: discovery, pilot, PoC, research, or alignment on assumptions.

### Evidence Ledger

For important business claims, keep an evidence ledger:

```yaml
claim:
evidence:
source:
freshness:
confidence:
gap:
decision_impact:
```

Definitions:

- `claim`: the statement the presentation wants the audience to believe
- `evidence`: data, example, quote, case, expert input, customer feedback, benchmark, or operational fact
- `source`: where the evidence came from
- `freshness`: whether the evidence is current enough for the decision
- `confidence`: high / medium / low
- `gap`: what is missing or uncertain
- `decision_impact`: whether this gap affects the ask, timing, or commitment level

Rules:

- Unknown source should be marked as unknown source, not silently omitted.
- Stale evidence should be flagged.
- Unsupported claims should become hypotheses.
- High-impact gaps should appear in the final gap analysis.

### Material Triage

When the user provides many materials, sort before structuring:

```text
T1 Core claim: must appear in the main storyline
T2 Support proof: useful for evidence slides
T3 Appendix: relevant but too detailed for the main flow
T4 Noise / unverified: do not use unless validated
```

Use triage to decide:

- what drives the storyline
- what supports the argument
- what belongs in appendix
- what should be excluded

Do not let the user's materials dictate slide order automatically.

### Strategic Reading Mode

When the user provides an article, report, transcript, case study, notes, or source document, do not merely summarize it.

Read it through the lens of the presentation goal:

```yaml
source:
presentation_goal:
audience:
usable_claims:
usable_evidence:
counterpoints_or_risks:
irrelevant_material:
missing_proof:
recommended_use:
```

Output should answer:

- Which parts help the current presentation?
- Which claims can be used directly?
- Which evidence is strong enough?
- Which parts are interesting but not useful?
- What should be verified before use?
- Should this material be mainline, appendix, or excluded?

### Gap Analysis

Always make important unknowns visible.

Use:

```yaml
gap:
why_it_matters:
impact_on_argument:
how_to_validate:
owner_or_source_to_check:
```

Common gap types:

- missing decision-maker context
- stale customer or market information
- unsupported ROI
- unverified case result
- unclear stakeholder resistance
- absent risk or compliance view
- weak proof for a strong ask

The skill should not hide ignorance. A good presentation can be persuasive while still naming what is not yet known.

### Layer 4: Narrative And Expression

Narrative earns attention and movement. It does not replace proof.

Choose the narrative after the argument is clear.

### Layer 5: Slide Structure

Slides are the final layer. Each slide needs:

```yaml
role:
action_title:
key_message:
evidence:
visual_form:
risk_or_weakness:
```

## 8. Horizontal Five Forces

Scan these before committing to a structure.

### Power Relationship

Ask:

- Who decides?
- Who can veto?
- Who influences?
- Who is affected but absent?
- Who needs face, ownership, or authority protected?

### Trust Base

Ask:

- Does the audience trust the speaker?
- Does the audience trust the data?
- Does the audience suspect hidden motive?
- Is credibility needed before argument?

### Psychological Resistance

Ask whether the presentation forces the audience to admit:

- their past decision was wrong
- their team has a problem
- they need to give up resources
- they must accept more risk
- they must change a habit
- they must trust a new person, team, or method

### Field Constraint

Account for:

- formal vs informal
- synchronous vs asynchronous
- public vs private
- high-pressure vs exploratory
- first-time audience vs long-term relationship
- live speech vs read-ahead document
- executive meeting vs workshop vs sales conversation

### Ethical Boundary

Do not help:

- fabricate data
- hide material risk
- misrepresent evidence
- manufacture false urgency
- attack or deceive an audience
- use story to override truth

## 9. Memo Before Slides Rule

Recommend a memo, read-ahead, appendix, or pre-wire conversation when:

- evidence is complex
- risk is high
- assumptions need scrutiny
- legal, technical, or financial nuance matters
- the audience will read asynchronously
- slide compression would hide uncertainty

## 10. Iteration Loop

Treat each plan as a hypothesis:

```text
Hypothesis -> Expression -> Feedback -> Revision
```

Identify which assumptions need validation and who should preview key claims before the formal presentation.

## 11. Pre-Wire Principle

Many important presentations are won or lost before the formal meeting.

Recommend pre-wire actions when:

- the audience includes a boss, investor, customer, committee, regulator, or cross-functional stakeholder
- the message contains bad news
- the deck asks someone to give resources, accept risk, or admit a prior assumption was wrong
- the presentation depends on another team's data, standard, or approval

Pre-wire output should identify:

```yaml
person_or_group:
claim_to_align:
why_before_meeting:
suggested_action:
```

Example:

```text
Before the boss update, align with the customer service lead on a draft validation standard. Do not let the formal meeting be the first time the conflict appears.
```
