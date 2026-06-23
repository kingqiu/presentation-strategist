# Golden Example: AI Training To AI PPT Brief

## User Input

```text
我要给公司中层做一场90分钟生成式AI普及培训。听众不是技术背景，而且有人担心AI会替代他们。目标不是讲技术细节，而是让他们愿意在自己的部门先试3个工作场景。请帮我设计培训型PPT结构，并整理成AI PPT brief。
```

## Human-Readable Strategy Framework

### Delivery Mode

`standard_framework`

### Input Convergence

| Type | Content | Slide Implication |
| --- | --- | --- |
| Confirmed facts | 90-minute training; middle managers; non-technical audience; replacement anxiety | Start with reassurance and managerial relevance |
| Reasonable assumptions | They need a safe first step more than a technical lecture | Use examples, decision rules, and experiments |
| High-impact unknowns | Company policy, tool access, data security constraints, target departments | Keep tools and metrics as placeholders |
| Confidence | Medium | Suitable for a practical enablement deck |

### Communication Diagnosis

Audience: middle managers who influence departmental adoption.

Current state: curious but anxious; may see AI as either hype or threat.

Desired state: willing to select three safe work scenarios for team-level experiments.

Communication task: teach + mobilize.

### Core Judgment

This training should shift AI from an abstract threat to a controlled management experiment.

### Recommended Training Arc

1. **AI不是替代中层判断，而是放大可被清晰描述的工作流程**
   - Role: reduce fear and set the frame
   - Evidence needed: simple before/after workflow examples

2. **先不要问“AI能不能做我的工作”，先问“哪些环节重复、耗时、可验证”**
   - Role: teach selection criteria
   - Evidence needed: work-task classification examples

3. **最适合先试的3类场景：写作整理、信息分析、流程辅助**
   - Role: give practical entry points
   - Evidence needed: department-specific examples

4. **不适合先试的场景：高风险决策、未授权数据、不可验证输出**
   - Role: establish safety boundary
   - Evidence needed: company policy placeholders

5. **部门试点不是上系统，而是跑一个两周学习闭环**
   - Role: lower adoption burden
   - Evidence needed: experiment rhythm, roles, review points

6. **每个部门今天带走一个3场景清单和一个试点负责人**
   - Role: mobilize action
   - Evidence needed: workshop template

## AI PPT Generation Brief

### Deck-Level Instructions

- Audience: non-technical middle managers
- Goal: make each department choose three safe AI trial scenarios
- Tone: practical, calm, non-hype, respectful of anxiety
- Length: 6 core sections; can expand with exercises for 90 minutes
- Do not claim fixed productivity improvements without data
- Keep company policy, tool names, and metrics as `[placeholder]`

### Slide-Level Brief

```yaml
slides:
  - slide: 1
    role: "Reframe fear"
    action_title: "AI不是替代中层判断，而是放大可被清晰描述的工作流程"
    key_message: "Managers remain responsible for judgment, priority, and quality."
    content_blocks:
      - "What AI can help with: drafting, summarizing, comparing, checking"
      - "What managers still own: goal, context, decision, accountability"
      - "Anxiety to acknowledge: replacement concern"
    suggested_visual: "Human judgment + AI workflow support diagram"
    speaker_intent: "Lower defensiveness before teaching methods."
  - slide: 2
    role: "Teach selection criteria"
    action_title: "先不要问“AI能不能做我的工作”，先问“哪些环节重复、耗时、可验证”"
    key_message: "Good first use cases are repetitive, time-consuming, and checkable."
    content_blocks:
      - "Good candidate: repeatable task"
      - "Good candidate: clear input and output"
      - "Good candidate: human can verify result"
    suggested_visual: "Three-part selection filter"
    speaker_intent: "Give managers a reusable decision rule."
  - slide: 3
    role: "Entry scenarios"
    action_title: "最适合先试的3类场景：写作整理、信息分析、流程辅助"
    key_message: "Start where value is visible and risk is controllable."
    content_blocks:
      - "Writing and synthesis: meeting notes, reports, emails"
      - "Information analysis: compare options, extract patterns"
      - "Workflow assistance: checklist, draft SOP, follow-up planning"
    suggested_visual: "Three scenario cards"
    speaker_intent: "Move from concept to practical examples."
  - slide: 4
    role: "Safety boundary"
    action_title: "不适合先试的场景：高风险决策、未授权数据、不可验证输出"
    key_message: "Clear boundaries make adoption safer."
    content_blocks:
      - "Do not use: confidential data without authorization"
      - "Do not use: final high-stakes decisions"
      - "Do not use: outputs no one can verify"
    suggested_visual: "Red/yellow/green use-case matrix"
    speaker_intent: "Prevent reckless experimentation."
  - slide: 5
    role: "Experiment design"
    action_title: "部门试点不是上系统，而是跑一个两周学习闭环"
    key_message: "A small experiment is enough to learn."
    content_blocks:
      - "Week 1: pick scenarios and try prompts"
      - "Week 2: compare output quality and time saved"
      - "Review: keep, adjust, or stop"
    suggested_visual: "Two-week loop"
    speaker_intent: "Make adoption feel manageable."
  - slide: 6
    role: "Action"
    action_title: "每个部门今天带走一个3场景清单和一个试点负责人"
    key_message: "End with a concrete departmental commitment."
    content_blocks:
      - "Department: [placeholder]"
      - "Three scenarios: [placeholder]"
      - "Owner and review date: [placeholder]"
    suggested_visual: "Fill-in action worksheet"
    speaker_intent: "Convert training into action."
```

