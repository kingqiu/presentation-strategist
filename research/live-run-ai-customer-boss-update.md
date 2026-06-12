# Live Run: AI Customer Service Boss Update

Date: 2026-06-12
Status: First full live-run simulation

## 1. Simulated User Input

```text
我明天要跟老板汇报一下当前项目进度。项目是一个 AI 客服上线项目，目前整体延期两周，主要卡在知识库质量和客服团队验收，老板之前比较关注能不能按期上线。我希望老板能帮我协调客服负责人一起确定验收标准。
```

## 2. Expected Skill Mode

```yaml
mode: Structure
scenario: boss-facing update
subtype: risk_update + resource/coordination request
communication_task: review / warn / decide
```

The user gave enough context to move beyond pure Diagnose mode. The skill should not ask many questions before helping.

## 3. Simulated Skill Response

下面我先按“向老板做 AI 客服上线项目进度汇报”来处理。你这次不是普通进度同步，核心其实是：

> 项目已延期两周，但真正需要老板介入的不是所有问题，而是协调客服负责人尽快确定验收标准，否则延期会继续扩大。

我会先给你一版可直接改成 PPT 的汇报逻辑，同时保留 3 个需要你补充的数据点。

### 1. 我的临时假设

- 听众：直属老板或项目 sponsor。
- 老板当前关注：能不能按期上线，以及延期是否可控。
- 你的目标：让老板理解延期原因不是单纯执行慢，而是“验收标准未对齐”导致上线无法闭环；希望老板协调客服负责人一起定标准。
- 沟通任务：`review + warn + decide`。
- 场景：向上项目进度汇报，带一个明确协调请求。
- 风险：如果讲成“我们延期了”，容易被老板理解为团队执行问题；如果讲成“客服团队没配合”，又可能制造部门对立。

### 2. 沟通诊断

```yaml
communication_goal: 让老板协调客服负责人，在本周内确定 AI 客服上线验收标准
communication_task: review / warn / decide
business_scenario: boss-facing update
field_constraint: 明天现场或会议汇报，老板时间有限
audience_current_state: 关注能否按期上线，可能首先追问为什么延期
audience_desired_state: 认可当前最大阻塞是验收标准未定，并愿意出面协调
stakes: 若验收标准继续不清，项目可能继续延期，且上线质量和客服团队接受度都会受影响
ask: 请老板协调客服负责人，在本周完成验收标准确认
evidence_strength: 中等；已有延期事实和阻塞判断，但需要补充里程碑、缺陷数据、验收争议点
```

### 3. 核心判断

> AI 客服项目当前延期两周，但主要风险已经从技术开发转向知识库质量和客服验收标准未对齐；如果本周能由老板协调确认验收标准，项目仍有机会把延期控制在可管理范围内。

### 4. 推荐叙事结构

用“结论先行 + 风险聚焦 + 协调请求”的结构：

```text
当前结论
-> 已完成进展
-> 延期原因拆解
-> 真正阻塞点
-> 两个处理选项
-> 推荐动作和老板需要支持的事项
```

不要按“项目背景、项目目标、项目计划、项目问题、总结”讲。老板最关心的不是背景，而是：

```text
延期是否失控？
为什么延期？
谁需要做什么？
我现在要不要介入？
```

### 5. 证据地图

| 关键主张 | 已有证据 | 需要补充 | 可能反对意见 | 处理方式 |
| --- | --- | --- | --- | --- |
| 项目整体延期两周 | 当前排期与原计划对比 | 原计划上线日期、当前预计上线日期 | 为什么现在才说？ | 说明发现验收标准问题后的时间线 |
| 延期主因不是开发，而是知识库质量和验收标准 | 你对阻塞点的判断 | 缺陷数量、知识库命中率、未通过验收项 | 是不是技术团队没做好？ | 区分技术完成、知识库质量、业务验收三个环节 |
| 需要老板协调客服负责人 | 客服验收标准未定 | 哪些标准未定、谁能拍板 | 为什么你自己不能协调？ | 说明这是跨部门标准确认，不是单项目组能单方决定 |
| 本周定标准能控制延期 | 当前剩余工作可排期 | 标准确定后预计修复/验收周期 | 定了标准也可能延期 | 给出两种情景：本周定/下周仍未定 |

### 6. 页面级框架

#### Slide 1: 项目延期两周，但当前最大风险已经从开发进度转向验收标准未对齐

Role: thesis / status judgment  
Key message: 先把老板从“是不是全面失控”的担心拉到“关键阻塞点是什么”。  
Visual: 红黄绿状态条 + 一句话结论。  
Speaker intent: 直接承认延期，同时说明风险边界。

#### Slide 2: 核心功能已进入上线前阶段，但知识库质量和客服验收仍未闭环

Role: progress evidence  
Key message: 证明项目不是没有进展，而是卡在上线闭环。  
Visual: 里程碑表：已完成 / 进行中 / 未闭环。  
Evidence needed: 功能开发完成度、知识库构建进度、测试/验收状态。

#### Slide 3: 延期的直接原因是验收口径变化和知识库质量返工，而不是单一开发延期

Role: root cause  
Key message: 帮老板正确归因，避免误判为执行不力。  
Visual: 延期原因拆解：开发 / 知识库 / 业务验收 / 协调。  
Evidence needed: 返工项、验收意见、客服团队反馈。

#### Slide 4: 如果本周不能确定验收标准，项目延期可能从两周扩大到四周以上

Role: risk warning  
Key message: 让老板看到“为什么现在需要介入”。  
Visual: 两条时间线对比：本周定标准 vs 继续悬置。  
Evidence needed: 标准确认后所需修复周期、验收周期估算。  
Risk: 如果没有估算依据，要标成情景假设。

#### Slide 5: 当前有两个选择：继续项目组自行推进，或由老板协调客服负责人本周定标准

Role: option / decision  
Key message: 把问题变成老板可以处理的选择。  
Visual: 选项对比表。  
Option A: 项目组继续沟通，风险是标准反复、延期扩大。  
Option B: 老板协调客服负责人定标准，风险是短期增加会议成本，但能锁定验收口径。

#### Slide 6: 建议本周完成三件事，把延期控制在可管理范围内

Role: ask / next action  
Action title: 请老板支持本周拉齐客服验收标准，并确认上线口径  
Key message: 明确老板要做什么。  
Suggested ask:

1. 请老板协调客服负责人参加一次 30 分钟验收标准会。
2. 会上确认必须达标项、可延期优化项、上线阻断项。
3. 项目组按标准在 X 天内给出修复和二次验收计划。

### 7. 你需要补的 3 个关键事实

1. 原计划上线日期、当前预计上线日期、延期两周的具体口径。
2. 知识库质量问题的数据：命中率、错误率、未覆盖问题数，或至少典型失败案例。
3. 客服团队验收标准到底卡在哪里：没有标准、标准变化、还是不同人标准不一致。

### 8. 这份汇报最容易踩的坑

- 不要把延期讲成流水账。
- 不要暗示客服团队“背锅”，要讲成“跨部门验收口径需要 sponsor 介入”。
- 不要只汇报问题，要给老板一个明确可执行的动作。
- 不要承诺“协调后一定按期”，应该说“可以把延期控制在可管理范围内”。

### 9. 如果只能讲 3 分钟

```text
老板，AI 客服项目目前比原计划延期两周。核心功能不是主要阻塞，真正影响上线的是知识库质量和客服验收标准还没有闭环。如果本周不能确定验收标准，延期可能继续扩大。我的建议是请您协调客服负责人，本周拉一个 30 分钟会，把必须达标项、可延期优化项和上线阻断项定下来。项目组随后按这个标准给出修复和二次验收计划。
```

## 4. QA Evaluation

| Criterion | Result | Notes |
| --- | --- | --- |
| Concrete communication goal | Pass | Goal is boss coordination for validation standards. |
| Communication task | Pass | Correctly classified as review / warn / decide. |
| Audience current/desired state | Pass | Current concern and desired sponsor action are explicit. |
| Five forces | Partial pass | Power and resistance are addressed; trust and field are implied; ethics addressed through no blame/no overclaim. |
| Argument before slides | Pass | Core judgment and evidence map precede slide framework. |
| Action-title slides | Pass | Slide titles are claims rather than topics. |
| Missing proof | Pass | Three key missing facts named. |
| Avoids over-questioning | Pass | Gives useful structure without waiting for answers. |

## 5. Observed Strengths

- The response reframes "project delayed" into "specific cross-functional decision needed".
- It avoids blaming the客服团队 while still naming the organizational blocker.
- The ask is concrete enough for a boss-facing meeting.
- It produces a usable 3-minute verbal version, which is helpful for inexperienced users.

## 6. Gaps Found

### Gap 1: The 3-minute version is useful but not required by the current skill.

The live run naturally produced a concise verbal version. This is valuable for real users, especially when they need to present tomorrow.

Suggested change:

Add "executive talk track" as an optional output for boss-facing updates and high-pressure short meetings.

### Gap 2: Five forces are present but not explicitly formatted.

The simulated response used power/resistance/ethics implicitly. For a full strategy output, a compact five-force scan would make the reasoning more visible.

Suggested change:

For standard mode, include a short "five-force scan" when the situation involves boss, investor, customer, cross-functional, crisis, or interview stakes.

## 7. Recommended Skill Updates

1. Add optional "Executive talk track" to output defaults.
2. Add a compact five-force scan to standard output when stakes are medium/high.
3. Update QA or SKILL.md to mention short spoken version for urgent presentations.

