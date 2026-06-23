# Downstream PPT Tool Handoff Adapters

Use this after `references/handoff-schema.md` when the user names a downstream tool or asks for a brief tailored to a specific PPT generator.

The strategic content stays the same. Only the packaging changes.

## Universal Rules

- Keep action titles.
- Preserve placeholders for missing facts, metrics, dates, names, and customer proof.
- Separate visible slide content from speaker intent.
- State the target tool explicitly.
- Include constraints that prevent the downstream tool from inventing proof.
- Keep one logical job per slide.

## Gamma

Best for: narrative business decks, quick polished drafts, web-first sharing.

Format:

```markdown
# Gamma Brief

Audience:
Goal:
Tone:
Slide count:
Visual style:
Do not invent:

## Slides

### 1. <action title>
Purpose:
Visible content:
- ...
Suggested visual:
Speaker intent:
Placeholder / risk:
```

Adapter notes:

- Use clear section headings.
- Keep bullets concise.
- Include `Do not invent` near the top.
- Use `[placeholder]` for unknown metrics or examples.

## Canva

Best for: visually polished decks where the user may manually edit layouts.

Format:

```yaml
tool: Canva
deck:
  audience:
  goal:
  tone:
  visual_style:
  constraints:
slides:
  - slide:
    page_intent:
    headline:
    body_text:
    visual_suggestion:
    layout_hint:
    speaker_note:
    placeholders:
```

Adapter notes:

- Emphasize page intent, headline, and visual suggestion.
- Avoid dense YAML if the user wants to paste into Canva manually; use markdown cards instead.
- Name visual forms: comparison, timeline, matrix, scorecard, flow, proof ladder.

## Marp

Best for: markdown-native decks, developer audiences, version-controlled slides.

Format:

```markdown
---
marp: true
title: <deck title>
---

# <action title>

- Visible bullet
- Visible bullet

<!-- speaker intent: ... -->
<!-- placeholder: ... -->
```

Adapter notes:

- Keep slide text short.
- Put speaker intent and placeholders in HTML comments when useful.
- Avoid complex layout instructions unless the user has a Marp theme.

## Guizang PPT Skill

Best for: stylized HTML slides, magazine-like or Swiss-style web PPT.

Format:

```markdown
# Guizang PPT Brief

Recommended style: <magazine | swiss | ask user>
Deck purpose:
Audience:
Narrative rhythm:
Theme constraints:

## Slide Plan

1. Action title:
   Role:
   Key message:
   Content blocks:
   Suggested layout:
   Suggested image:
   Speaker intent:
```

Adapter notes:

- Provide narrative rhythm and suggested visual mood.
- Keep layout suggestions high-level unless the user has chosen a specific Guizang style.
- Do not invent image assets or factual screenshots.

## Baoyu Slide Deck

Best for: image-based slide generation and PPTX/PDF assembly from content.

Format:

```markdown
# Baoyu Slide Deck Brief

Audience:
Goal:
Slide count:
Style suggestion:
Language:
Evidence constraints:

## Outline

### Slide 1: <action title>
Core message:
Visible content:
Image/prompt direction:
Do not show as fact:
```

Adapter notes:

- Include style suggestion only as a recommendation.
- Keep image/prompt direction separate from evidence.
- Explicitly list claims that must remain placeholders.

## Generic AI PPT Tools

Use the schema in `references/handoff-schema.md` when the target is unknown.

