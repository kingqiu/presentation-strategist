# Presentation Strategist Forward Test Results

Date: 2026-06-12
Status: First forward test pass

## 1. Test Purpose

This test checks whether `presentation-strategist` behaves like a communication strategist rather than a generic PPT outline generator.

Special focus:

- vague, low-information users
- users with no presentation experience
- goal vs task distinction
- argument before narrative
- evidence and risk visibility
- horizontal five forces
- action-title slide planning

## 2. Evaluation Criteria

Each test is evaluated against:

1. Does it ask or infer the concrete communication goal?
2. Does it classify the communication task?
3. Does it diagnose audience current state and desired state?
4. Does it consider power, trust, resistance, field, and ethics where relevant?
5. Does it build central judgment and evidence before slide structure?
6. Does it produce action-title slide roles rather than topic headings?
7. Does it surface missing proof and next validation questions?
8. Does it avoid over-questioning inexperienced users?

## 3. Test Cases

### Test 1: Low-Information Boss Update

User input:

```text
我明天要跟老板汇报一下我当前这个项目的进度。
```

Expected behavior:

- Trigger Diagnose mode.
- Do not ask "how many slides" first.
- Recognize this as boss-facing update.
- Infer possible tasks: review / align / warn / decide, depending on project status.
- Make temporary assumptions and produce a usable first structure.
- Ask no more than 3 clarifying questions.

Good response shape:

```text
我先按“向老板做项目进度汇报”处理。现在信息还少，我会先给你一个可用框架，同时问 3 个关键问题。

临时假设：
- 听众：直属老板
- 目标：让老板快速知道项目是否按计划推进、风险在哪里、是否需要他决策或协调资源
- 任务：review + align；如果有风险，则 warn / decide

3 个问题：
1. 项目目前是正常、延期、超预算，还是有关键风险？
2. 你希望老板听完后只是了解，还是要做某个决定/给资源？
3. 你手里有什么事实：进度、里程碑、数据、问题、风险？

建议汇报逻辑：
1. 当前结论：项目总体状态是 X，最需要老板关注的是 Y。
2. 进展事实：已完成什么，和计划相比如何。
3. 关键变化：哪些地方超预期或低于预期。
4. 风险/阻塞：如果不处理，会影响什么。
5. 需要老板做什么：决策、协调、资源、还是仅同步。

页面框架：
1. 项目总体处于 X 状态，当前最重要的不是进度本身，而是 Y。
2. 已完成的 A/B/C 证明项目主线仍然成立。
3. 当前偏差主要来自 Y，而不是团队执行不足。
4. 如果本周不处理 Z，下一个里程碑会受到影响。
5. 需要老板今天确认/支持/知悉的事项是...
```

Pass / fail:

```text
Pass if the skill provides a first useful scaffold plus 3 questions.
Fail if it only says "请提供背景信息" or outputs generic pages like 背景/进度/问题/总结.
```

### Test 2: Boss-Facing Resource Request

User input:

```text
我要向老板申请两个人和 30 万预算，材料很散，帮我想 PPT 怎么讲。
```

Expected behavior:

- Goal: get approval for headcount and budget.
- Task: decide / persuade.
- Scenario: boss-facing proposal.
- Argument: resource gap blocks business outcome; request has ROI and risk control.
- Narrative: answer first -> business need -> gap -> options -> recommendation -> risk -> ask.
- Missing proof: workload, ROI, alternatives, timeline impact.

Pass condition:

The output should make the ask explicit and not bury it at the end.

### Test 3: Customer Sales Proposal

User input:

```text
我们要给一个制造业客户讲 AI 质检方案，客户现在觉得自己已有系统够用。
```

Expected behavior:

- Goal: get customer to see current system risk or opportunity and enter next step.
- Task: sell / reframe / de-risk.
- Scenario: customer sales deck.
- Resistance: customer believes status quo is enough.
- Narrative: changed quality/compliance/labor world -> old system blind spots -> cost of inaction -> AI path -> proof -> low-risk pilot.
- Ethical note: do not invent defect or ROI numbers.

Pass condition:

The deck should sell change before product features.

### Test 4: Fundraising Pitch

User input:

```text
帮我梳理一个早期 AI 工具的融资路演逻辑，目前有用户增长但收入还少。
```

Expected behavior:

- Goal: make investors believe this is fundable despite low revenue.
- Task: persuade / de-risk.
- Scenario: fundraising.
- Argument: user growth is proof of pain or pull; revenue weakness must be explained honestly.
- Narrative: problem -> why now -> product -> user growth proof -> monetization hypothesis -> market -> team -> ask.
- Missing proof: retention, usage frequency, willingness to pay, CAC, segment.

Pass condition:

The skill should not hide low revenue. It should reframe the ask around validation and funding next proof.

### Test 5: Career / Personal Pitch

User input:

```text
我要面试一家目标公司，需要做一个介绍自己的 presentation，想证明我适合这个岗位。
```

Expected behavior:

- Goal: make employer believe the candidate is a strong, low-risk fit.
- Task: persuade / de-risk / differentiate.
- Scenario: career / personal pitch.
- Narrative: role need -> fit thesis -> proof stories -> risk reduction -> contribution plan -> next step.
- Avoid autobiography.
- Ask for role, company, and strongest proof stories.

Pass condition:

The structure should be employer-centered, not self-centered.

### Test 6: Product Launch / Category Redefinition

User input:

```text
我们要发布一款新硬件，想让用户觉得它不是普通升级，而是一个新品类。
```

Expected behavior:

- Goal: reframe audience mental category.
- Task: reframe / excite / persuade.
- Narrative: familiar world -> unresolved friction -> new category -> demo -> proof -> adoption.
- Proof: real use cases, demo, differentiator, ecosystem, adoption risk.

Pass condition:

The output should not become feature list.

### Test 7: Business Review

User input:

```text
我要做季度经营复盘，收入达标但利润没达标，管理层要知道下一步怎么调。
```

Expected behavior:

- Goal: explain variance and get agreement on adjustments.
- Task: review / explain / decide.
- Narrative: status -> variance -> drivers -> implications -> options -> next actions.
- Argument: revenue quality, cost structure, margin drivers, corrective actions.
- Missing proof: segment margin, cost bridge, forecast.

Pass condition:

The structure should focus on "so what" and action, not metric dump.

### Test 8: Crisis / Risk Briefing

User input:

```text
项目可能延期 6 周，我要给管理层做风险预警，不能粉饰太平。
```

Expected behavior:

- Goal: make leadership understand risk and decide mitigation.
- Task: warn / decide.
- Narrative: facts -> impact -> uncertainty -> options -> recommendation -> decision needed.
- Ethical boundary: make uncertainty visible.
- Recommend memo/appendix if evidence is complex.

Pass condition:

The skill should not soften risk into optimistic storytelling.

### Test 9: Technical Review

User input:

```text
我要向架构委员会比较三种方案，希望他们批准其中一个。
```

Expected behavior:

- Goal: get one option approved.
- Task: decide / de-risk.
- Narrative: decision criteria -> options -> tradeoffs -> recommendation -> risks -> validation plan.
- No forced hero story.
- Ask for criteria, constraints, and options.

Pass condition:

The structure should present criteria before options.

## 4. Findings

### Finding 1: The skill needs an explicit low-information behavior rule.

Current `SKILL.md` says Diagnose mode handles vague topics and asks at most 3 questions, but it does not explicitly say to produce a useful provisional structure when the user provides only one sentence.

Risk:

An agent may over-question an inexperienced user or produce a generic outline.

Fix:

Add a "Low-information user behavior" section to `SKILL.md`:

```text
When the user gives only a vague one-sentence need, do not stop at questions. Provide:
1. a brief assumption set
2. 3 high-leverage questions
3. a provisional communication diagnosis
4. a starter structure with action-title examples
5. what evidence to collect next
```

### Finding 2: Boss-facing status update deserves a more specific preset.

The current Boss-Facing Update preset includes decide / align / warn, but it does not distinguish:

- normal progress sync
- risk update
- resource request
- decision request

Fix:

Add subtypes under Boss-Facing Update.

### Finding 3: The skill should define "starter structure" for low-information cases.

Without this, a response may either be too abstract or too complete.

Fix:

Add a small starter output pattern:

```text
Assumptions -> 3 questions -> likely goal/task -> starter storyline -> evidence checklist
```

### Finding 4: Career pitch coverage is now present and should be tested.

The scenario exists in `business-scenarios.md`; keep it in forward tests.

## 5. Required Changes

1. Update `presentation-strategist/SKILL.md` with low-information behavior.
2. Update `presentation-strategist/references/business-scenarios.md` with boss-facing update subtypes.
3. Optionally update `design/skill-design-spec.md` so design docs match the implementation.

