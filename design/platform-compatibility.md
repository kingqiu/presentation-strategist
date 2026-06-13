# Platform Compatibility Notes

Date: 2026-06-12
Status: Compatibility research for `presentation-strategist`

## 1. Executive Summary

`presentation-strategist` is structurally compatible with the current SKILL.md-style ecosystem used by:

- Codex
- Claude Code / Claude Agent Skills
- OpenClaw
- Hermes Agent

The common denominator is:

```text
skill-folder/
├── SKILL.md
├── references/
├── templates/
├── scripts/      optional
└── assets/       optional
```

Required frontmatter:

```yaml
---
name: presentation-strategist
description: ...
---
```

Main compatibility choice:

> Keep the canonical skill as a plain SKILL.md package with references/templates. Treat platform-specific files such as `agents/openai.yaml` as optional adapters.

## 2. Current Skill Compatibility

Current package:

```text
presentation-strategist/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── business-scenarios.md
│   ├── case-library.md
│   ├── classic-frameworks.md
│   ├── handoff-schema.md
│   ├── qa-rubric.md
│   └── strategic-communication-principles.md
└── templates/
    ├── ai-ppt-generation-brief.md
    ├── logic-review.md
    ├── presentation-brief.md
    └── slide-plan.yaml
```

Compatibility status:

| Platform | Status | Notes |
| --- | --- | --- |
| Codex | Compatible | Native `SKILL.md`; `agents/openai.yaml` is useful and optional. |
| Claude Code | Compatible | Uses filesystem `SKILL.md`; ignores Codex-only `agents/openai.yaml`. |
| Claude API / claude.ai | Mostly compatible | May require zip/upload or API skill upload depending on surface. |
| OpenClaw | Compatible after description shortening | Requires/strongly recommends one-line description under 160 characters. |
| Hermes Agent | Compatible | Supports `references/`, `templates/`, `scripts/`, `assets/`; can install from GitHub/tap or local skills dir. |

## 3. Platform Findings

### Codex

Official docs state:

- A skill is a directory with `SKILL.md` plus optional `scripts/`, `references/`, `assets/`, and `agents/openai.yaml`.
- `SKILL.md` must include `name` and `description`.
- Codex uses progressive disclosure: name/description are available first, full `SKILL.md` is loaded when selected.
- Codex can invoke skills explicitly or implicitly based on the description.

Implication:

- Our structure is native.
- `agents/openai.yaml` should stay.
- Description should be concise and front-loaded.

Source:

- https://developers.openai.com/codex/skills

### Claude Code / Claude Agent Skills

Official docs state:

- Claude Code custom skills are filesystem-based and use directories with `SKILL.md`.
- Every skill requires `name` and `description`.
- Name must be lowercase letters, numbers, and hyphens, max 64 characters.
- Description must be non-empty and max 1024 characters.
- Claude Code surfaces do not automatically sync with claude.ai or Claude API.
- Claude Agent SDK loads skills from `.claude/skills/`, `~/.claude/skills/`, or configured skill paths.

Implication:

- Our `name` is valid.
- Our shortened description is valid.
- For Claude Code project install, copy or symlink to `.claude/skills/presentation-strategist`.
- For claude.ai/API, package/upload separately.

Sources:

- https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- https://code.claude.com/docs/en/agent-sdk/skills

### OpenClaw

Official docs state:

- Skills are directories containing `SKILL.md` with YAML frontmatter and Markdown instructions.
- Required fields: `name`, `description`.
- Naming uses lowercase letters, digits, and hyphens.
- Directory name and frontmatter name should be aligned.
- Description is shown in discovery and should be one line under 160 characters.
- Skills live under OpenClaw skill roots such as `~/.openclaw/workspace/skills/`.
- Can be invoked explicitly with `/skill`.

Implication:

- Our folder and name align.
- The original 685-character description was too long for OpenClaw's recommendation. It has now been shortened.
- Avoid relying on `agents/openai.yaml` for OpenClaw.

Source:

- https://docs.openclaw.ai/tools/creating-skills

### Hermes Agent

Official docs state:

- Hermes skills are compatible with the agentskills.io open standard.
- Skills live in `~/.hermes/skills/` by default and can also be loaded from external directories.
- Directory structures may include `SKILL.md`, `references/`, `templates/`, `scripts/`, and `assets/`.
- Hermes supports installs from GitHub paths/taps; multi-file skills should be published through GitHub/taps rather than single-file direct URL installs.
- Skill taps commonly use a `skills/<skill-name>/SKILL.md` layout.

Implication:

- Our multi-file skill is structurally compatible.
- For Hermes distribution, put it under `skills/presentation-strategist/` in a tap repo or install from a GitHub path.
- Direct single-file URL install would lose references/templates, so avoid that for this skill.

Source:

- https://hermes-agent.nousresearch.com/docs/user-guide/features/skills

## 4. Recommended Cross-Platform Packaging Strategy

Keep one canonical skill package:

```text
presentation-strategist/
```

Then create platform placement adapters:

```text
dist/
├── codex/.agents/skills/presentation-strategist/
├── claude/.claude/skills/presentation-strategist/
├── openclaw/presentation-strategist/
└── hermes/skills/presentation-strategist/
```

All four should contain the same canonical files.

Platform-specific files:

- `agents/openai.yaml`: keep for Codex; harmless for others but not required.
- Avoid platform-only frontmatter in canonical `SKILL.md`.
- If Hermes-specific metadata is later desired, add it in a generated Hermes package rather than canonical source.
- Avoid executable scripts unless truly needed, because security scanning and tool permissions differ by platform.

## 5. Current Changes Made For Compatibility

Changed `SKILL.md` description from a long 685-character trigger description to a shorter cross-platform description:

```yaml
description: Design presentation strategy: PPT逻辑/框架, storyline, pitch/sales/career decks, boss updates, AI training, risk briefings; not visual editing.
```

Why:

- Under Claude's 1024-character limit.
- More compatible with OpenClaw's under-160-character guidance.
- Still front-loads the key trigger ideas for Codex and Claude.

Detailed triggers were moved into the body of `SKILL.md`.

## 6. Remaining Work

Before publishing or installing broadly:

1. Add a packaging script that copies the canonical skill into platform-specific directories.
2. Add a lightweight compatibility check:
   - `SKILL.md` exists
   - frontmatter has `name` and `description`
   - name matches lowercase hyphen rule
   - description is one line and under 160 chars
   - required references/templates exist
3. Optionally create zip packages for Claude surfaces that require upload.
4. Optionally create a Hermes tap-compatible `skills/presentation-strategist/` layout.
5. Test actual discovery on each installed platform before public release.

