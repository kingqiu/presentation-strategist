# Slide Idea Skill Market Scan

Date: 2026-06-12

## Research Question

Is there an existing "Slide Idea Skill" category focused on presentation thinking, story logic, audience-fit, and slide-by-slide argument design rather than visual slide generation?

## Short Answer

There are many AI presentation generators and several agent skills that include presentation planning. The gap is a standalone, interaction-first skill whose primary job is to help a human clarify the message, argument, evidence, audience, and slide logic before any design or deck generation happens.

## Findings

### 1. Existing AI presentation tools optimize for generation speed

Tools such as SlideSpeak, Beautiful.ai, Canva, Adobe Express, Gamma-like products, and other deck builders emphasize turning a topic, document, or prompt into slides quickly. SlideSpeak's outline tool frames the workflow as "enter topic -> AI builds outline -> refine/export", with sections, titles, bullets, and summaries. Beautiful.ai explicitly mentions reviewing a slide-by-slide outline before high-fidelity design.

Implication: The market already understands that outline review matters, but most products still treat it as a pre-generation convenience, not the core product.

Sources:
- https://slidespeak.co/free-tools/ai-presentation-outline-generator
- https://www.beautiful.ai/presentation-maker
- https://www.canva.com/create/ai-presentations/
- https://www.adobe.com/express/create/ai/presentation

### 2. Open-source slide agents mostly generate decks end to end

Open-source projects and indexes show a crowded field of deck builders. Common pipelines include: collect prompt/materials, generate outline, create slide content, apply design, export as PPTX/HTML/Marp, then QA.

Examples:
- proyecto26/slides-ai-plugin has a `slide-design` skill that starts with content discovery, creates `slide-outline.md`, plans structure by duration, tags slide types, then proceeds to generation.
- mblode/agent-skills `presentation-creator` covers narrative arc, slide copy, visual design, speaker notes, and QA.
- iuiaoin/agent-skills has `/deck --plan`, which runs guided Q&A, synthesizes a deck brief, confirms it, and expands it into `PLANNING.md`.
- embabel/decker starts from a YAML definition, decides key points, does research, generates Markdown slide content, then converts with Marp.
- AI Presentation Builders Index tracks open/self-hosted/agent-driven builders and was last updated April 2026.

Implication: There is prior art for the mechanics, but the center of gravity is "make me a deck." Slide Idea Skill should deliberately stop before visual production unless the user asks for handoff.

Sources:
- https://github.com/proyecto26/slides-ai-plugin/blob/main/skills/slide-design/SKILL.md
- https://github.com/mblode/agent-skills/blob/main/skills/presentation-creator/SKILL.md
- https://github.com/iuiaoin/agent-skills
- https://github.com/embabel/decker
- https://github.com/danielrosehill/AI-Presentation-Builders-Index

### 3. Consulting-style communication frameworks are still the strongest logic layer

The Pyramid Principle remains the most relevant baseline for business presentations: lead with the answer, group supporting arguments, support each argument with evidence, and avoid making executives wait for the conclusion. Think-cell's guide frames the same pattern as conclusion first, then supporting arguments, data, and facts.

Implication: Slide Idea Skill should not invent a purely aesthetic deck taxonomy. It should encode business communication logic: audience, decision, recommendation, proof, objections, and next action.

Sources:
- https://winningpresentations.com/pyramid-principle-presentations/
- https://www.think-cell.com/en/resources/content-hub/using-the-pyramid-principle-to-build-better-powerpoint-presentations

## Opportunity

Position the skill as "the thinking layer before PPT":

- It does not promise beautiful slides.
- It helps the user avoid empty but polished decks.
- It asks structured questions, diagnoses the real communication job, and produces a slide-by-slide reasoning plan.
- It can hand off cleanly to visual PPT skills later.

## Differentiation

| Existing category | Typical promise | Weakness | Slide Idea Skill angle |
| --- | --- | --- | --- |
| AI deck generator | Prompt to full deck | Fast but generic, often shallow | Slow down before generation; clarify argument |
| Outline generator | Topic to sections/bullets | Often topic-summary shaped, not decision-shaped | Audience and decision first |
| PPT design skill | Better visual slides | Does not ensure the content is meaningful | Logic before aesthetics |
| Consulting framework | Strong thinking model | Not packaged as an agent workflow | Turn framework into guided Q&A and artifacts |

## Design Principle

The skill should behave like a senior presentation strategist:

1. First understand what the presentation must change in the audience.
2. Then clarify the one message the room must remember.
3. Then design the argument and evidence.
4. Then map that argument into slides.
5. Only then hand off to a visual/deck generation skill.

