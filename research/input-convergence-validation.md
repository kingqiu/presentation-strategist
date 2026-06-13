# Input Convergence Validation

Date: 2026-06-12
Status: Pass after mechanism update

## Purpose

Validate whether `presentation-strategist` can handle incomplete user input without producing a final-sounding deck based on unstated assumptions.

The specific risk being tested:

> The skill may create a polished, professional-looking slide framework while silently treating assumptions as facts.

## Test Prompt

```text
我要做一个产品介绍 PPT，帮我想一下怎么讲。
```

## Expected Behavior

The skill should not immediately produce a generic product deck such as:

```text
产品背景 -> 产品功能 -> 产品优势 -> 客户案例 -> 合作方式
```

It should first separate:

- confirmed facts
- reasonable assumptions
- high-impact unknowns
- slide implications

Then it should ask no more than 3 high-leverage questions and provide only a provisional framework.

## Simulated Output Shape

### Input Convergence

| Type | Item | Impact On Framework | How To Validate |
| --- | --- | --- | --- |
| Confirmed fact | The user needs a product introduction PPT. | We can treat this as a product/company communication task, but not yet as sales, training, launch, or internal alignment. | Already stated by user. |
| Reasonable assumption | The audience may be a potential customer or partner. | Use a trust-building product narrative instead of an internal feature explanation. | Ask who the audience is. |
| Reasonable assumption | The goal may be to create interest and win a next conversation. | End with a low-risk next step, not a purchase decision. | Ask what action the audience should take. |
| High-impact unknown | Audience role and decision power are unknown. | Could change the order: executive value first, technical architecture first, or user workflow first. | Ask who will attend. |
| High-impact unknown | Available proof is unknown. | Case/result slides must use placeholders; do not invent customer names, ROI, or metrics. | Ask what evidence exists. |
| High-impact unknown | Desired next step is unknown. | The final ask may be demo, workshop, PoC, procurement review, or internal alignment. | Ask desired action. |

```yaml
confidence_level: low
safe_next_output: provisional framework + 3 validation questions
```

### Questions

1. 这份产品介绍是讲给客户、老板、投资人、渠道伙伴，还是内部团队？
2. 听完之后，你希望对方做什么：约 demo、进入 PoC、安排评审、理解产品，还是批准采购？
3. 你现在有什么证据：客户案例、数据结果、试点反馈、行业标杆，还是只有功能说明？

### Provisional Framework

1. **先定义客户问题，而不是先介绍产品**  
   Role: establish audience relevance.  
   Evidence: placeholder for pain point, current process friction, or business cost.

2. **说明为什么现有方式不够好**  
   Role: create reason to change.  
   Evidence: placeholder for inefficiency, risk, cost, delay, or missed opportunity.

3. **提出产品的核心判断：它解决的是哪一个关键问题**  
   Role: move from problem to product thesis.  
   Evidence: feature-to-outcome mapping, not a feature list.

4. **展示一个典型使用场景或工作流**  
   Role: make the product concrete.  
   Evidence: demo flow, user journey, before/after.

5. **给出可信证明，但不夸大**  
   Role: build trust.  
   Evidence: customer case, pilot result, benchmark, or clearly labeled placeholder.

6. **提出低风险下一步**  
   Role: turn interest into action.  
   Ask: demo, workshop, PoC, evaluation meeting, or next stakeholder discussion.

## Self-Check

| Check | Result | Notes |
| --- | --- | --- |
| Did it separate facts from assumptions? | Pass | Only the need for a product intro is treated as confirmed. |
| Did it name high-impact unknowns? | Pass | Audience, proof, and desired next step are explicit. |
| Did it avoid a final-sounding answer? | Pass | The framework is labeled provisional. |
| Did it avoid inventing evidence? | Pass | Proof slides use placeholders. |
| Did it keep questions limited? | Pass | Three questions only. |
| Did it still help the user move forward? | Pass | It gives a usable starter structure instead of blocking. |

## Conclusion

The new Input Convergence Gate addresses the biggest current risk: polished output built on hidden assumptions.

The skill should now behave more reliably when users provide sparse input:

- continue working
- show uncertainty
- lower the ask when evidence is weak
- preserve placeholders for AI PPT handoff
- avoid pretending assumptions are facts
