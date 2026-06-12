# Slide Idea Skill Design Proposal

Date: 2026-06-12
Status: Draft for discussion

## 1. Working Name

`slide-idea`

Alternative names:
- `presentation-thinking`
- `deck-logic`
- `slide-strategist`
- `ppt-storyline`

Recommendation: use `slide-idea` because it is short, memorable, and captures the current market gap. The description should make clear that it means "presentation idea and logic design", not visual slide design.

## 2. Positioning

Slide Idea Skill is the logic layer before presentation production.

It helps users turn rough intent, notes, documents, meeting context, or scattered opinions into a clear presentation strategy and slide-by-slide reasoning plan.

It does not generate a polished PPT by default. It creates the thinking artifacts needed before visual slide generation:

- presentation brief
- audience and decision diagnosis
- core message
- storyline
- evidence map
- slide-by-slide outline
- open questions and missing proof
- handoff brief for PPT/Marp/HTML slide generation

## 3. Target Users

Primary:
- workplace professionals making internal reports, project updates, proposals, training decks, client decks, or boss-facing summaries
- sales, consultants, founders, trainers, product managers, students

Best initial niche:
- Chinese workplace users who can create visually acceptable slides but struggle with "what should this deck actually say?"
- users who already use AI to make PPT but find the content generic

## 4. Jobs To Be Done

When I need to make a presentation, I want AI to help me think through the audience, message, argument, evidence, and slide sequence so that the final deck is not just good-looking but persuasive and useful.

Common scenarios:

| Scenario | User input | Output |
| --- | --- | --- |
| Boss update | rough notes, project facts | answer-first status deck logic |
| Sales proposal | client background, pain points | problem-solution-value storyline |
| Training | topic, audience level, duration | learning path and slide sequence |
| Product pitch | idea, user, value prop | demo/pitch storyline |
| Research sharing | articles, notes, PDFs | argument map and teaching structure |
| Investor pitch | startup notes | narrative and evidence gaps |

## 5. Non-Goals

MVP should not:
- generate final PPTX/HTML slides
- spend time on visual design systems
- create charts or infographics
- pretend to know missing facts
- produce long generic presentation theory

It can later hand off to:
- Guizang PPT skill
- Presentations plugin
- Marp/RevealJS skill
- custom PPTX generator

## 6. Core Workflow

### Phase 0: Mode Selection

Detect or ask which mode applies:

1. `diagnose`: user only has a vague topic; run guided questions.
2. `structure`: user has notes/materials; create storyline and outline.
3. `critique`: user has an existing outline/deck; review logic and suggest fixes.
4. `handoff`: user approved the logic; produce generation-ready brief for another slide skill.

Default to `diagnose` if the user has only a topic.

### Phase 1: Intake

Collect only the minimum context needed:

- audience: who will listen/read
- setting: live talk, meeting, report, sales pitch, training, async doc
- goal: what should the audience decide, believe, remember, or do
- duration/page count
- current materials
- stakes: low, medium, high
- constraints: language, tone, format, deadline

Rule: ask at most 3 questions at a time. If the user wants speed, make assumptions and mark them.

### Phase 2: Communication Diagnosis

Classify the presentation job:

| Type | Best structure |
| --- | --- |
| Decision / recommendation | answer first -> 3 reasons -> risks -> ask |
| Update / report | status -> variance -> drivers -> risks -> next actions |
| Sales / proposal | client pain -> cost of inaction -> solution -> proof -> next step |
| Training / teaching | learner problem -> concept ladder -> examples -> practice -> recap |
| Research / insight | surprising finding -> why it matters -> evidence -> implications |
| Product / demo | user pain -> product promise -> workflow -> proof -> adoption path |
| Fundraising / pitch | opportunity -> insight -> product -> traction -> business -> ask |

Output:
- recommended structure
- why this structure fits
- what would make the deck fail

### Phase 3: Core Message

Force a one-sentence thesis:

Template:

> For `[audience]`, this presentation should make them `[decision/action/belief]` because `[main reason]`.

Quality checks:
- Can it be said in one breath?
- Is it audience-facing rather than presenter-facing?
- Does it imply a decision or change?
- Can the opposite be meaningfully argued?

### Phase 4: Storyline

Build one of several storyline patterns:

1. Pyramid: answer -> reasons -> evidence
2. Problem/Solution: pain -> cost -> solution -> proof -> action
3. Before/After: current state -> desired state -> bridge -> plan
4. Tension/Resolution: contradiction -> insight -> new model -> implications
5. Teaching Ladder: known -> new concept -> example -> application
6. Demo Arc: scenario -> workflow -> result -> value

For business decks, default to Pyramid unless the user is teaching or pitching.

### Phase 5: Evidence Map

For each major claim, identify:

- evidence available
- evidence missing
- likely objection
- confidence level
- whether the slide should show data, example, quote, diagram, demo, or decision table

This is the main quality control layer. A slide idea without evidence should be marked as weak rather than dressed up.

### Phase 6: Slide-By-Slide Plan

Each slide should have:

- slide number
- slide role
- action title
- key message
- supporting points
- needed evidence/source
- suggested visual form
- speaker note intent
- risk/weakness

Example schema:

```yaml
slide: 4
role: evidence
title: "客户流失主要发生在首次价值兑现之前"
message: "问题不在获客，而在用户没有足够快看到结果。"
evidence:
  available: ["activation funnel", "interview quotes"]
  missing: ["segment-level retention"]
visual: "funnel + callout"
speaker_intent: "让团队把注意力从拉新转向激活体验"
risk: "如果没有 cohort 数据，这页只能作为假设"
```

### Phase 7: Critique and Iteration

Run a logic QA pass:

- thesis clear?
- audience-specific?
- one idea per slide?
- every claim has proof or is labeled as hypothesis?
- sequence creates momentum?
- no orphan slides?
- no decorative slides pretending to be content?
- ending has a clear ask or next action?

Output a concise review table:

| Issue | Severity | Slide(s) | Fix |
| --- | --- | --- | --- |

### Phase 8: Handoff

Only after user confirms the logic:

- produce `slide-idea-brief.md`
- optionally produce `slide-outline.yaml`
- recommend the right downstream generator

Handoff should include:
- deck purpose
- audience
- tone
- slide count
- storyline
- slide plan
- evidence files
- design constraints, if known
- unresolved questions

## 7. Proposed Skill Folder Structure

```text
slide-idea/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── deck-types.md
│   ├── storyline-patterns.md
│   ├── qa-rubric.md
│   └── handoff-schema.md
└── templates/
    ├── brief.md
    ├── slide-plan.yaml
    └── critique-table.md
```

Keep `SKILL.md` short. Put examples, patterns, and rubrics in references.

## 8. SKILL.md Trigger Design

Description should trigger on:

- "帮我想 PPT 思路"
- "这个汇报怎么讲"
- "帮我设计 presentation structure"
- "做一个 slide outline"
- "PPT 逻辑"
- "presentation storyline"
- "deck narrative"
- "先别做 PPT，帮我梳理思路"
- "review my outline/deck logic"

It should avoid triggering when the user only wants:

- final PPTX generation
- visual redesign only
- chart styling only
- PowerPoint file editing only

## 9. MVP Scope

MVP should support three commands/workflows through natural language:

1. New deck idea from vague topic
   - Input: topic + rough goal
   - Output: questions, recommended structure, thesis, first outline

2. Structure from notes
   - Input: pasted notes or local source docs
   - Output: storyline + slide-by-slide plan

3. Critique existing outline
   - Input: outline or deck text
   - Output: diagnosis + revised structure

MVP output files:

- `slide-idea-brief.md`
- `slide-plan.yaml`
- `logic-review.md`

## 10. Quality Bar

A good output must be:

- decision-oriented: not a generic topic summary
- audience-specific: says why this audience cares
- evidence-aware: marks assumptions and missing proof
- slide-native: each slide has one job
- handoff-ready: another PPT skill can execute it

A bad output looks like:

- a school essay outline pasted into slides
- a list of generic section titles
- too many "overview / background / conclusion" slides
- beautiful but content-empty
- no explicit ask, decision, or audience change

## 11. Discussion Points

Before implementation, decide:

1. Should the first version be bilingual Chinese-English by default?
2. Should it save artifacts inside the current project, or only print the plan unless asked?
3. Should it include a small deterministic schema validator for `slide-plan.yaml`?
4. Should it integrate directly with Guizang PPT skill later, or stay generator-neutral?
5. Should "critique existing PPT" be MVP or v2?

## 12. Recommended Next Step

Start with a lean skill:

- `SKILL.md` with the 8-phase workflow
- `references/storyline-patterns.md`
- `references/qa-rubric.md`
- `templates/slide-plan.yaml`

Then test it with three real prompts:

1. internal work report
2. sales proposal
3. thought-leadership sharing deck

