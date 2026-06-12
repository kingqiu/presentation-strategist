# Presentation Strategist Implementation Sequence

Date: 2026-06-12
Status: Case research and design synthesis completed

## Principle

Do not implement `SKILL.md` first.

The correct sequence is:

```text
architecture -> case research -> design synthesis -> skill implementation -> scenario tests
```

## Step 1: Architecture

Already captured in:

- `design/presentation-strategist-architecture.md`

This defines:

- vertical six layers
- horizontal five forces
- iteration loop
- initial case library
- non-negotiable quality bar

## Step 2: Case Research

Completed in:

- `research/case-research-plan.md`
- `research/case-study-analysis.md`

The research should gather and analyze public cases across:

- strategic sales narratives
- startup and investor pitches
- product launches
- internal alignment and culture decks
- decision memos and non-PPT systems
- crisis and risk communication
- executive business reviews

## Step 3: Design Synthesis

Completed in:

- `design/skill-design-spec.md`

This defines:

- skill positioning
- trigger language
- core workflow
- diagnostic dimensions
- questioning strategy
- scenario presets
- output formats
- QA rubric
- handoff behavior
- boundaries and ethics

## Step 4: Skill Implementation

Only after `skill-design-spec.md` is stable, create the actual skill:

```text
presentation-strategist/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── strategic-communication-principles.md
│   ├── business-scenarios.md
│   ├── classic-frameworks.md
│   ├── case-library.md
│   ├── qa-rubric.md
│   └── handoff-schema.md
└── templates/
    ├── presentation-brief.md
    ├── ai-ppt-generation-brief.md
    ├── slide-plan.yaml
    └── logic-review.md
```

## Step 5: Scenario Tests

Forward-test the skill with representative prompts:

- boss-facing resource request
- customer sales proposal
- investor pitch
- product launch
- business review
- crisis/risk briefing
- training or knowledge-sharing deck

These are tests of generalization, not templates to memorize.
