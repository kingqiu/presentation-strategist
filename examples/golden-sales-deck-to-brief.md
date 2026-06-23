# Golden Example: Sales Deck To AI PPT Brief

## User Input

```text
我们要给一家制造业客户做销售提案。客户觉得我们的系统太贵，希望这次汇报能让他们愿意先做一个PoC。我们没有正式客户案例，只有两个试点线索和一些内部测算。帮我设计sales deck逻辑，并整理成AI PPT brief。
```

## Human-Readable Strategy Framework

### Delivery Mode

`standard_framework`

### Input Convergence

| Type | Content | Slide Implication |
| --- | --- | --- |
| Confirmed facts | Manufacturing customer; price resistance; goal is PoC; no formal case studies | Do not lead with feature list or fake case studies |
| Reasonable assumptions | Customer needs risk reduction before purchase | Use low-risk PoC as the ask |
| High-impact unknowns | Customer's exact pain, budget cycle, decision maker, baseline KPI | Use discovery placeholders |
| Confidence | Medium-low | Recommend a pilot proposal rather than full purchase |

### Communication Diagnosis

Audience: buyer or buying committee at a manufacturing company.

Current state: sees the system as expensive and may doubt ROI.

Desired state: believes a bounded PoC is a low-risk way to test value.

Communication task: sell without overselling.

### Core Judgment

The deck should not prove a full purchase; it should make a limited PoC feel like the safest next step to test whether inventory pressure and delivery visibility can improve.

### Recommended Storyline

1. **贵不贵不能只看系统报价，要看当前不可见成本是否正在扩大**
   - Reframe price resistance around hidden operational cost.
   - Evidence needed: customer's inventory, delay, exception-handling pain.

2. **制造业交付问题通常不是缺系统，而是缺跨环节可视化判断**
   - Teach the buying criteria before selling the product.
   - Evidence needed: typical process map, pain points from discovery.

3. **我们的系统先解决一个可验证问题：[PoC场景]**
   - Narrow the scope.
   - Evidence needed: chosen line, plant, SKU group, or process.

4. **PoC只验证3个指标，不要求客户一次性押注**
   - Lower perceived risk.
   - Evidence needed: baseline placeholders and measurement plan.

5. **现有证据支持先试点，但还不足以承诺全面ROI**
   - Handle evidence honestly.
   - Evidence needed: internal model, pilot leads, assumptions.

6. **建议以[周期]完成PoC，结束后按数据决定是否扩大**
   - Make the next step easy.
   - Evidence needed: timeline, roles, success threshold.

## AI PPT Generation Brief

### Deck-Level Instructions

- Audience: manufacturing customer evaluating an expensive system
- Goal: win agreement for a bounded PoC, not a full purchase
- Tone: credible, consultative, risk-aware
- Length: 6 slides
- Do not invent customer logos, success stories, ROI numbers, or external case studies
- Use `[placeholder]` where proof is missing

### Slide-Level Brief

```yaml
slides:
  - slide: 1
    role: "Reframe price objection"
    action_title: "贵不贵不能只看系统报价，要看当前不可见成本是否正在扩大"
    key_message: "Price should be compared with operational waste and decision delay."
    content_blocks:
      - "Current visible objection: price"
      - "Possible hidden costs: [inventory pressure], [delivery delay], [manual exception handling]"
      - "Need customer validation: [baseline data]"
    suggested_visual: "Cost iceberg diagram"
    speaker_intent: "Shift the discussion from software price to business cost."
  - slide: 2
    role: "Teach buying criteria"
    action_title: "制造业交付问题通常不是缺系统，而是缺跨环节可视化判断"
    key_message: "The buying question is whether the system improves visibility and decisions."
    content_blocks:
      - "Planning, production, warehouse, delivery touchpoints"
      - "Where visibility usually breaks: [placeholder]"
      - "What better decision-making should look like"
    suggested_visual: "Process chain with visibility gaps"
    speaker_intent: "Make the customer evaluate the right problem."
  - slide: 3
    role: "Narrow PoC scope"
    action_title: "我们的系统先解决一个可验证问题：[PoC场景]"
    key_message: "A focused PoC is safer than a broad rollout."
    content_blocks:
      - "Recommended PoC scope: [line / plant / SKU group / process]"
      - "Why this scope is measurable"
      - "What is explicitly out of scope"
    suggested_visual: "PoC scope boundary box"
    speaker_intent: "Reduce perceived risk."
  - slide: 4
    role: "Measurement plan"
    action_title: "PoC只验证3个指标，不要求客户一次性押注"
    key_message: "The pilot will produce decision evidence."
    content_blocks:
      - "Metric 1: [baseline and target placeholder]"
      - "Metric 2: [baseline and target placeholder]"
      - "Metric 3: [baseline and target placeholder]"
    suggested_visual: "Three-metric scorecard"
    speaker_intent: "Make success criteria concrete without inventing numbers."
  - slide: 5
    role: "Evidence calibration"
    action_title: "现有证据支持先试点，但还不足以承诺全面ROI"
    key_message: "Be honest about proof strength."
    content_blocks:
      - "Available evidence: internal model, two pilot leads"
      - "Missing proof: validated customer baseline, formal case study"
      - "Why PoC is the right proof-building step"
    suggested_visual: "Evidence ladder from assumptions to validated proof"
    speaker_intent: "Build trust by not overstating."
  - slide: 6
    role: "Ask"
    action_title: "建议以[周期]完成PoC，结束后按数据决定是否扩大"
    key_message: "Ask for a small, reversible next step."
    content_blocks:
      - "PoC duration: [placeholder]"
      - "Customer resources needed: [placeholder]"
      - "Decision after PoC: expand / adjust / stop"
    suggested_visual: "Pilot timeline with decision gate"
    speaker_intent: "Move the customer to a concrete next action."
```

