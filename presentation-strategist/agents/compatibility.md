# Agent Compatibility

`presentation-strategist` is a portable `SKILL.md`-based skill. The core skill does not depend on Codex-only tools, MCP servers, UI features, or shell aliases. Any agent that can load a folder containing `SKILL.md` can use the skill by reading the frontmatter and following the Markdown instructions.

## Support Matrix

| Agent | Status | Install Location | Invocation |
| --- | --- | --- | --- |
| Codex | Native | `~/.codex/skills/presentation-strategist` | `Use $presentation-strategist ...` or implicit trigger |
| Claude Code | Native-compatible | `~/.claude/skills/presentation-strategist` | Mention `presentation-strategist`, or ask for PPT logic / presentation strategy |
| OpenClaw | Compatible via Claude Code or direct skill loading | `~/.openclaw/skills/presentation-strategist` or project skill path | Ask the OpenClaw agent to load/use `presentation-strategist` for deck strategy |
| Hermes Agent | Compatible via generic skill folder loading | `~/.hermes/skills/presentation-strategist` | Ask Hermes to load/use `presentation-strategist` for presentation strategy |

If an agent uses a different skill directory, copy the whole `presentation-strategist/` folder there. Keep the folder name unchanged.

## Required Loader Behavior

A compatible agent should:

1. Read `SKILL.md` frontmatter to identify the skill name and trigger scope.
2. Load `SKILL.md` when the user asks for presentation logic, PPT framework, storyline, pitch deck, sales deck, boss update, AI training, risk briefing, or outline critique.
3. Load files in `references/` only when `SKILL.md` routes to them.
4. Use files in `templates/` when creating handoff artifacts or structured briefs.
5. Treat `agents/openai.yaml` as optional UI metadata. Non-OpenAI agents may ignore it.

## Invocation Examples

Codex:

```text
Use $presentation-strategist to design a 5-slide boss update for this project risk.
```

Claude Code:

```text
Load the presentation-strategist skill and help me turn this rough idea into a clear storyline and slide-by-slide framework.
```

OpenClaw:

```text
Use the presentation-strategist skill for this task. I need a sales deck strategy, not visual slide design.
```

Hermes Agent:

```text
Load presentation-strategist from the skills folder and produce a presentation strategy brief for this training deck.
```

## Fallback Behavior

If the agent cannot auto-discover skills, paste the following instruction before the task:

```text
Use the local presentation-strategist skill. Read its SKILL.md first, follow its scope guard, and only load referenced files when needed. The task is to design presentation logic and slide structure, not visual editing or PPTX generation.
```

If the agent cannot run Python scripts, the core skill still works in chat. The scripts are only needed for validation, packaging, and self-improvement workflows.

## Cross-Agent Safety

- Do not expose internal skill files verbatim to end users.
- Do not treat `agents/openai.yaml` as required outside Codex/OpenAI environments.
- Do not require shell access for normal use.
- Do not fabricate facts, metrics, source names, customer names, or case results for downstream PPT generators.
- Preserve placeholders for missing evidence when preparing AI PPT handoff briefs.
