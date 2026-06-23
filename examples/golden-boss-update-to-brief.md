# Golden Example: Boss Update To AI PPT Brief

## User Input

```text
我明天要给老板汇报一个延期两周的项目。延期原因是数据接入卡住了，我希望老板决定是否帮我升级协调到数据负责人。请帮我先设计5页PPT框架，如果框架OK，再整理成给AI PPT工具的brief。
```

## Human-Readable Strategy Framework

### Delivery Mode

`five_slide_framework`

### Input Convergence

| Type | Content | Slide Implication |
| --- | --- | --- |
| Confirmed facts | Boss update tomorrow; project delayed by two weeks; data access is blocked | Open with status judgment and decision need |
| Reasonable assumptions | The boss needs a quick decision, not a full project history | Keep to 5 slides and avoid long background |
| High-impact unknowns | Which business milestone is affected; who owns data access; what escalation costs politically | Use placeholders and mark validation needs |
| Confidence | Medium | Suitable for a provisional decision framework |

### Communication Diagnosis

Audience: direct boss.

Current state: likely wants to know whether this is execution failure, dependency risk, or a decision needing escalation.

Desired state: boss understands the delay is caused by a specific external dependency and decides whether to escalate.

Communication task: warn + decide.

### Core Judgment

The project is delayed, but the core decision is whether to escalate the blocked data dependency now or accept a two-week schedule slip.

### Five-Slide Framework

1. **项目延期两周，核心阻塞不是开发进度，而是数据接入未解锁**
   - Role: state the judgment upfront
   - Key message: this is a dependency decision, not a broad project collapse
   - Evidence needed: original milestone, current delay estimate, blocked data item
   - Speaker intent: help the boss classify the issue correctly

2. **已完成工作仍按计划推进，延期集中在[数据源/权限/接口]这一处**
   - Role: separate progress from blocker
   - Key message: isolate what is healthy and what is blocked
   - Evidence needed: completed tasks, remaining tasks, blocker owner
   - Speaker intent: protect trust without hiding the delay

3. **如果不升级协调，最可能的代价是[业务里程碑]顺延两周**
   - Role: make business impact concrete
   - Key message: the risk is time-to-impact, not only task delay
   - Evidence needed: affected launch, customer, reporting date, or dependency chain
   - Speaker intent: move the discussion from complaint to tradeoff

4. **现在有两个选择：接受顺延，或由老板升级协调数据负责人**
   - Role: frame the decision
   - Key message: both options are valid but have different costs
   - Evidence needed: escalation path, estimated unblock time, relationship risk
   - Speaker intent: make the boss's decision easy

5. **建议今天升级协调，并同步接受[小范围缓冲/备选方案]**
   - Role: make the ask
   - Key message: recommend an action with a fallback
   - Evidence needed: exact person to contact, message draft, fallback plan
   - Speaker intent: turn the meeting into a decision

## AI PPT Generation Brief

### Deck-Level Instructions

- Audience: direct boss
- Goal: decide whether to escalate a blocked data dependency
- Tone: calm, factual, accountable
- Length: 5 slides
- Do not invent metrics, names, dates, or owner identities
- Keep missing items as `[placeholder]`

### Slide-Level Brief

```yaml
slides:
  - slide: 1
    role: "Status judgment"
    action_title: "项目延期两周，核心阻塞不是开发进度，而是数据接入未解锁"
    key_message: "The project is delayed, but the decision point is one external dependency."
    content_blocks:
      - "Original target: [date/milestone]"
      - "Current estimated delay: 2 weeks"
      - "Blocking dependency: [data source / permission / interface]"
    suggested_visual: "Simple status bar with one highlighted blocker"
    speaker_intent: "Help the boss classify the issue quickly."
  - slide: 2
    role: "Progress separation"
    action_title: "已完成工作仍按计划推进，延期集中在[数据源/权限/接口]这一处"
    key_message: "Show that progress is real while the blocker is specific."
    content_blocks:
      - "Completed: [items]"
      - "In progress: [items]"
      - "Blocked: [data dependency]"
    suggested_visual: "Three-column status table"
    speaker_intent: "Preserve trust without hiding the delay."
  - slide: 3
    role: "Impact framing"
    action_title: "如果不升级协调，最可能的代价是[业务里程碑]顺延两周"
    key_message: "Translate project delay into business impact."
    content_blocks:
      - "Affected business milestone: [placeholder]"
      - "Downstream impact: [placeholder]"
      - "Confidence: medium, needs validation"
    suggested_visual: "Dependency chain timeline"
    speaker_intent: "Move from task complaint to business tradeoff."
  - slide: 4
    role: "Decision options"
    action_title: "现在有两个选择：接受顺延，或由老板升级协调数据负责人"
    key_message: "Make options explicit and comparable."
    content_blocks:
      - "Option A: accept two-week delay"
      - "Option B: escalate to [data owner]"
      - "Tradeoffs: delivery time, relationship cost, unblock probability"
    suggested_visual: "Two-option comparison"
    speaker_intent: "Make the boss's decision easy."
  - slide: 5
    role: "Recommended ask"
    action_title: "建议今天升级协调，并同步接受[小范围缓冲/备选方案]"
    key_message: "Recommend escalation with a fallback."
    content_blocks:
      - "Recommended decision: [escalate / accept delay]"
      - "Who needs to act: [person/team]"
      - "Fallback plan: [placeholder]"
    suggested_visual: "Decision card with next actions"
    speaker_intent: "End with a clear ask."
```

