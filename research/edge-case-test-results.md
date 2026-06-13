# Presentation Strategist Edge Case Test Results

Date: 2026-06-12
Status: Edge case test pass

## 1. Purpose

This pass tests difficult situations that can make a presentation strategist behave like a generic outline generator:

- vague company introduction
- conflicting goals
- weak evidence
- high-risk bad-news communication
- career / personal pitch
- AI PPT generation brief after approval

## 2. Evaluation Criteria

The skill should:

- infer the real goal behind surface requests
- separate human-readable framework from AI PPT generation brief
- avoid overclaiming when evidence is weak
- handle conflicting goals explicitly
- recommend pre-wire in medium/high-stakes situations
- produce concrete slide content blocks, not only strategy prose

## 3. Test Cases

### Test 1: Vague Company Introduction

User input:

```text
我要做一个公司介绍 PPT，帮我想一下怎么讲。
```

Expected behavior:

- Treat as low-information user.
- Do not output generic "公司简介 / 产品服务 / 团队介绍 / 联系我们".
- Ask up to 3 questions:
  1. Who is the audience?
  2. What should they do after seeing it?
  3. What proof or cases are available?
- Infer possible real goals:
  - build trust
  - win cooperation
  - attract customers
  - recruit talent
  - get investor interest
- Provide a starter structure with assumptions.

Pass condition:

The output should say company introduction is not one structure; it depends on audience and desired next action.

### Test 2: Conflicting Goal Sales Pitch

User input:

```text
我们要给客户介绍我们的 AI 产品，但又不想让客户觉得我们是在推销。客户现在对 AI 有兴趣，但担心投入太大、看不到效果。
```

Expected behavior:

- Detect goal conflict:
  - surface goal: product introduction
  - real goal: build trust and create low-risk next step
  - constraint: avoid sales pressure
- Recommended narrative:
  customer problem -> risk of wrong investment -> evaluation method -> relevant product capability -> low-risk pilot
- Avoid product-first structure.
- Include "teach-to-sell" or "diagnosis-before-product" strategy.

Pass condition:

The skill should explicitly name the conflict and resolve it through "diagnose first, product second".

### Test 3: Weak Evidence AI Capability Deck

User input:

```text
我们想讲我司 AI 能力很强，但目前没有特别完整的标杆案例，只有一些内部 Demo 和两个小试点。
```

Expected behavior:

- Do not dress weak proof as strong proof.
- Calibrate ask:
  - not "large rollout"
  - ask for discovery, pilot, workshop, or co-creation
- Structure:
  AI capability thesis -> what has been validated -> what is still hypothesis -> pilot plan -> proof to collect
- Evidence map should label internal demo and small pilot as limited proof.

Pass condition:

The skill should lower the ask and mark missing proof.

### Test 4: High-Risk Bad News

User input:

```text
我要向高层汇报一个项目可能失败，已经花了 800 万，但继续做可能还要再花 500 万，而且收益不确定。
```

Expected behavior:

- Use high_stakes mode.
- Task: warn / decide.
- Recommend memo or appendix because financial/risk nuance is high.
- Narrative:
  facts -> sunk cost vs future decision -> options -> recommendation -> decision needed
- Ethical boundary:
  do not hide sunk cost
  distinguish past spend from future decision
- Pre-wire:
  align with finance/project sponsor before formal meeting.

Pass condition:

The output should not try to make the project look good. It should force a decision.

### Test 5: Career / Personal Pitch

User input:

```text
我面试一家 AI 产品负责人岗位，需要做 15 分钟 presentation 介绍自己。我经历很多，但不知道怎么取舍。
```

Expected behavior:

- Real goal: make employer believe candidate is a high-fit, low-risk hire.
- Avoid autobiography.
- Ask for target company, role expectations, and strongest proof stories.
- Structure:
  role need -> fit thesis -> 3 proof stories -> first 90 days contribution -> next step
- Include evidence: product results, team leadership, AI experience, business impact.

Pass condition:

The presentation should be employer-centered, not candidate-centered.

### Test 6: Approved Framework To AI PPT Tool

User input:

```text
我认可刚才的框架，请输出一份给 AI PPT 工具用的详细版本。
```

Expected behavior:

- Switch to Version B: AI PPT Generation Brief.
- Use structured deck-level and slide-level fields.
- Include visible content, suggested visual, layout intent, speaker intent, risk/placeholders.
- Do not add new strategic direction unless necessary.

Pass condition:

The output should be import/paste-friendly for AI PPT tools.

## 4. Findings

### Finding 1: The skill handles weak evidence well in principle.

Existing rules already require:

- label missing proof
- calibrate ask to evidence strength
- avoid making weak evidence look strong

No change required.

### Finding 2: The AI PPT generation brief is now explicit.

Existing `handoff-schema.md` and `ai-ppt-generation-brief.md` cover Version B well.

No change required.

### Finding 3: Goal conflict needs a named rule.

The current skill can infer real goals, but it does not explicitly say how to handle conflicting goals such as:

- sell without seeming to sell
- warn without seeming defensive
- ask for resources without seeming incompetent
- introduce company without sounding generic
- promote self without sounding self-centered

Recommended change:

Add a "Goal Conflict Handling" rule:

```text
When the user has two goals in tension, separate frontstage goal, backstage goal, and trust constraint. Design a structure that earns permission before making the ask.
```

### Finding 4: Company introduction needs a warning.

Company introduction is especially prone to generic output. It should have a rule:

```text
Do not create company intro around company history. Create it around audience reason to trust and next action.
```

This can be added to `business-scenarios.md`.

## 5. Required Changes

1. Add Goal Conflict Handling to `SKILL.md` and `strategic-communication-principles.md`.
2. Add company introduction anti-generic guidance to `business-scenarios.md`.
3. Update QA rubric with conflict check.

