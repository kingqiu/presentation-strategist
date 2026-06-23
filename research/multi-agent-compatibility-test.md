# Multi-Agent Compatibility Smoke Test

Date: 2026-06-23

Skill version: 0.2.0

Commit under test: `508be1e Add multi-agent compatibility checks`

## Purpose

Validate that `presentation-strategist` is no longer only a Codex-oriented skill package. The smoke test checks whether the package has the files, metadata, install locations, and fallback instructions needed for Codex, Claude Code, OpenClaw, and Hermes Agent.

This is a smoke test, not a full quality benchmark. It verifies installability and package readiness. It does not replace scenario-level presentation output evaluation.

## Test Environment

Machine: local macOS environment

Repository path:

```text
/Users/jimqiu/Downloads/ClaudeCode/SlideDecks/presentation-strategist-work
```

Detected agent CLIs:

| Agent | CLI Status | Version / Result |
| --- | --- | --- |
| Codex | Found | `codex-cli 0.142.0` |
| Claude Code | Found | `2.1.126 (Claude Code)` |
| OpenClaw | Not found | `openclaw` command unavailable |
| Hermes Agent | Not found | `hermes` command unavailable |

## Package-Level Checks

Commands run:

```bash
python3 presentation-strategist/scripts/check_agent_compatibility.py presentation-strategist
python3 presentation-strategist/scripts/validate_skill_package.py presentation-strategist --allow-runtime
python3 scripts/package_skill.py --check
python3 presentation-strategist/scripts/package_skill.py --skill-dir presentation-strategist --out /tmp/presentation-strategist-smoke.zip
```

Results:

| Check | Result |
| --- | --- |
| Agent compatibility metadata | Passed |
| Skill package validation | Passed |
| Root multi-platform package check | Passed |
| Zip package smoke build | Passed, 29 files packaged |

## Install Path Checks

| Agent | Recommended Path | Local Status | Result |
| --- | --- | --- | --- |
| Codex | `~/.codex/skills/presentation-strategist` | Already installed | Passed package and compatibility checks |
| Claude Code | `~/.claude/skills/presentation-strategist` | Installed during this test | Passed package and compatibility checks |
| OpenClaw | `~/.openclaw/skills/presentation-strategist` | CLI not installed | Pending target-environment validation |
| Hermes Agent | `~/.hermes/skills/presentation-strategist` | CLI not installed | Pending target-environment validation |

## Codex Smoke Test

Codex CLI was available:

```text
codex-cli 0.142.0
```

The installed Codex skill copy was checked at:

```text
/Users/jimqiu/.codex/skills/presentation-strategist
```

Validation results:

```text
Agent compatibility check passed
Skill package is share-ready
```

Assessment: passed for package discovery readiness and file-level compatibility.

## Claude Code Smoke Test

Claude Code CLI was available:

```text
2.1.126 (Claude Code)
```

The skill was installed to:

```text
/Users/jimqiu/.claude/skills/presentation-strategist
```

Validation results:

```text
Agent compatibility check passed
Skill package is share-ready
claude-skill-files-present
```

Assessment: passed for filesystem install readiness and file-level compatibility.

## OpenClaw Status

The `openclaw` CLI was not available in this local environment. The package includes OpenClaw-compatible guidance in:

```text
presentation-strategist/agents/compatibility.md
README.md
```

Assessment: package-level compatibility passed, but real OpenClaw discovery and invocation remain pending.

Recommended future test:

```text
Install presentation-strategist under the OpenClaw skill root, ask OpenClaw to load the skill, and run one sales deck strategy prompt plus one out-of-scope prompt.
```

## Hermes Agent Status

The `hermes` CLI was not available in this local environment. The package includes Hermes-compatible guidance in:

```text
presentation-strategist/agents/compatibility.md
README.md
```

Assessment: package-level compatibility passed, but real Hermes Agent discovery and invocation remain pending.

Recommended future test:

```text
Install presentation-strategist under the Hermes skill root or tap-compatible path, ask Hermes to load the skill, and run one training deck prompt plus one AI PPT handoff prompt.
```

## Test Prompts For Real Agent Validation

Use the same prompts across agents to compare behavior.

Prompt 1, normal strategy task:

```text
Use presentation-strategist to design a 5-slide boss update. The project is delayed by two weeks because data access is blocked. I need the boss to decide whether to escalate to the data owner.
```

Expected behavior:

- Identify this as a boss-facing decision/update.
- Separate confirmed facts, assumptions, unknowns, and slide implications.
- Produce a concise slide-by-slide framework with action titles.
- Avoid fabricating metrics or names.

Prompt 2, handoff task:

```text
Use presentation-strategist to turn this framework into an AI PPT generation brief. Keep missing data as placeholders.
```

Expected behavior:

- Produce a structured generation brief.
- Preserve placeholders for missing data.
- Avoid visual-only design overreach.

Prompt 3, out-of-scope task:

```text
Use presentation-strategist to recommend nearby restaurants for dinner.
```

Expected behavior:

- Refuse to force-fit the task into the skill.
- Explain that the skill is for presentation strategy.
- Ask only if the user meant a presentation about restaurants or market research.

## Current Conclusion

`presentation-strategist` is ready as a multi-agent-compatible skill package at the file, metadata, and packaging level.

Fully verified:

- Codex local install readiness
- Claude Code local install readiness
- Package-level compatibility checks
- Zip package smoke build

Still pending:

- Real OpenClaw discovery and invocation
- Real Hermes Agent discovery and invocation
- Cross-agent output quality comparison on the same validation prompts

