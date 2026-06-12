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

## 4. Depth Levels

Adjust output depth to urgency and stakes.

```yaml
fast:
  use_when: deadline is near, user is inexperienced, or input is vague
  output: assumptions -> 3 questions -> likely goal/task -> starter structure -> 3-minute talk track -> evidence checklist

standard:
  use_when: normal strategy planning or scattered materials
  output: diagnosis -> argument -> storyline -> evidence map -> slide plan -> risks -> validation questions

high_stakes:
  use_when: board, investors, executive committee, regulator, public crisis, major budget, layoffs, safety, legal, financial forecast, high-risk technical decision
  output: standard + explicit five-force scan + pre-wire plan + memo/appendix recommendation + risk/ethics QA
```

Prefer `fast` for vague one-sentence needs unless the field or stakes imply high stakes.

## 5. Vertical Six Layers

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
evidence_map:
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

## 6. Horizontal Five Forces

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

## 7. Memo Before Slides Rule

Recommend a memo, read-ahead, appendix, or pre-wire conversation when:

- evidence is complex
- risk is high
- assumptions need scrutiny
- legal, technical, or financial nuance matters
- the audience will read asynchronously
- slide compression would hide uncertainty

## 8. Iteration Loop

Treat each plan as a hypothesis:

```text
Hypothesis -> Expression -> Feedback -> Revision
```

Identify which assumptions need validation and who should preview key claims before the formal presentation.

## 9. Pre-Wire Principle

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
