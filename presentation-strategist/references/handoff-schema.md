# Handoff Schema

Use this when the user approves the logic and wants a downstream generator, AI PPT tool, PPT skill, HTML slide skill, Marp deck, or production brief.

## Two Output Versions

### Human-Readable Slide Framework

Use before approval.

Purpose:

- help the user judge the logic
- keep the structure readable
- show page roles, action titles, key content, evidence, and risks

### AI PPT Generation Brief

Use after approval or when the user asks for a detailed version for AI PPT tools.

Purpose:

- provide structured, low-ambiguity instructions for AI PPT generation
- include deck-level guidance and slide-level content
- be usable as markdown, YAML, or pasted prompt input for external AI PPT tools

## Handoff Brief

```yaml
deck_purpose:
audience:
speaker:
communication_goal:
communication_task:
business_scenario:
field_constraint:
audience_current_state:
audience_desired_state:
stakes:
ask:
input_convergence:
delivery_mode:
tone:
slide_count:
storyline:
central_judgment:
evidence_sources:
evidence_ledger:
material_triage:
gap_analysis:
slide_plan:
open_questions:
design_constraints:
handoff_target:
```

## Slide Plan Item

```yaml
slide:
role:
action_title:
key_message:
content_blocks:
supporting_points:
evidence_or_examples:
suggested_visual:
speaker_intent:
risk_or_weakness:
```

## Logic Review Item

```yaml
issue:
severity:
slide_or_section:
why_it_matters:
recommended_fix:
```

## Handoff Notes

Always include:

- assumptions made
- confirmed facts, assumptions, high-impact unknowns, and slide implications
- missing proof
- evidence ledger for major claims
- material triage when source material exists
- gap analysis with decision impact
- weak claims
- unresolved objections
- risks that must not be hidden
- any recommendation to create memo or appendix before final deck

Potential handoff targets:

- Guizang PPT skill
- Presentations plugin
- Marp / RevealJS
- PPTX generator
- HTML slide skill
- external AI PPT tools that accept outline, markdown, prompt, or structured brief input

## AI PPT Tool Compatibility Rules

When writing for general AI PPT tools:

- Use explicit slide numbers.
- Use action titles, not topic titles.
- Include suggested layout, but avoid relying on a specific design system unless provided.
- Keep one main idea per slide.
- Name recommended visual forms: matrix, timeline, comparison table, funnel, roadmap, architecture diagram, quote card, case snapshot, KPI card.
- Include content blocks with concise bullets.
- Include speaker intent separately from visible slide text.
- Mark optional appendix slides.
- Do not include hidden reasoning or unsupported claims.
- Clearly label missing data as placeholder or assumption.
- Do not let assumptions become visible facts in generated slides.

## AI PPT Generation Brief Shape

```yaml
deck:
  title:
  purpose:
  audience:
  communication_goal:
  desired_audience_change:
  tone:
  duration:
  slide_count:
  language:
  visual_style:
  constraints:
  storyline:
  central_judgment:
  key_messages:
  evidence_sources:
  input_convergence:
  open_questions:
slides:
  - slide:
    title:
    role:
    objective:
    visible_content:
      headline:
      bullets:
      callouts:
    evidence_or_examples:
    suggested_visual:
    layout_intent:
    speaker_intent:
    notes_for_ai_ppt_tool:
    risk_or_placeholder:
appendix:
  - slide:
    title:
    purpose:
```
