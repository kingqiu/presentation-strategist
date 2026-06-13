# Scope Guard Validation

Date: 2026-06-13
Status: Pass after scope guard update

## Purpose

Validate whether `presentation-strategist` refuses unrelated tasks even when the user explicitly asks to use the skill.

The risk being tested:

> The skill may over-trigger and force unrelated tasks into a presentation framework.

## Test Cases

### Test 1: Unrelated Word Document

User input:

```text
用这个 skill 帮我生成一份如何养宠物的 Word 文档。
```

Expected behavior:

- Do not create a presentation framework.
- Do not reinterpret it as a pet-care training deck unless the user says so.
- Briefly say it is outside scope.
- Route to document writing / Word generation capability.
- Offer a single bridge only if useful: if the user wants a pet-care training PPT, the skill can help design that presentation.

Expected response shape:

```text
这个需求不属于 presentation-strategist 的范围。这个 skill 主要用于 PPT、汇报、演示、培训或销售 deck 的逻辑框架设计。如何养宠物的 Word 文档更适合文档写作/Word 生成能力处理。

如果你其实想做一份“宠物护理培训 PPT”，我可以帮你设计 presentation 框架。
```

Pass condition:

The response refuses the skill fit and does not generate slide structure.

### Test 2: Explicit Skill Mention For Restaurant Search

User input:

```text
用这个 skill 帮我查一下附近有什么适合吃饭的餐厅。
```

Expected behavior:

- Do not search restaurants through this skill.
- Do not create a restaurant recommendation presentation.
- State that explicit skill mention does not make the task in-scope.
- Route to local search / map / lifestyle recommendation capability.
- Ask a bridge question only if the user may mean a restaurant recommendation presentation or dining market research deck.

Expected response shape:

```text
这个需求不属于 presentation-strategist 的范围。这个 skill 主要用于设计 PPT/汇报/演示/培训/销售 deck 的逻辑框架。附近餐厅推荐更适合本地搜索或生活服务类工具处理。

如果你是要做一份“餐厅推荐汇报”或“餐饮市场调研 presentation”，我可以帮你设计框架。
```

Pass condition:

The response refuses the skill fit even though the user explicitly said "用这个 skill".

### Test 3: Adjacent But In-Scope Reframe

User input:

```text
我要做一份给公司行政团队看的餐厅推荐汇报，比较附近 5 家适合团建聚餐的餐厅。
```

Expected behavior:

- Treat as in scope because it is a presentation / briefing structure task.
- Diagnose audience, decision criteria, constraints, and desired decision.
- Do not perform restaurant search unless separately requested through a suitable search capability.
- Build a comparison presentation framework with placeholders for restaurant facts.

Pass condition:

The skill accepts only after the task is framed as a presentation/briefing.

## Self-Check

| Check | Result | Notes |
| --- | --- | --- |
| Does explicit skill mention override scope? | Pass | The rule says it must not. |
| Does the skill avoid force-fitting unrelated tasks? | Pass | Word document and restaurant search are refused as skill fits. |
| Does the skill provide a useful route instead of a hard dead end? | Pass | It suggests document writing or local search. |
| Does the skill accept adjacent presentation tasks? | Pass | Restaurant comparison briefing is in scope. |

## Conclusion

The updated scope guard reduces over-trigger risk. The skill should now distinguish:

- unrelated tasks that should be routed elsewhere
- adjacent tasks that become valid only when framed as a presentation, briefing, pitch, training, or communication strategy problem
