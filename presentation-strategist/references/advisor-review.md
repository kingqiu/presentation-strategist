# Optional Advisor Review

Use this reference only when the presentation is high-value, high-risk, strategically ambiguous, or the user explicitly asks for an extra review layer.

This is not the core workflow. The core remains:

```text
six layers -> five forces -> argument -> storyline -> slide structure
```

Advisor review is a second-pass critique after the initial strategy or slide framework exists.

## When To Use

Use advisor review for:

- board, investor, executive committee, regulator, crisis, major budget, or major customer presentations
- sales or partnership decks where trust, proof, and next step are fragile
- fundraising, career pitch, strategic proposal, AI transformation, or company repositioning decks
- situations with goal conflict, such as "sell without seeming to sell" or "warn without seeming defensive"
- critique requests where the user wants sharper business judgment, not only slide structure

Do not use it for:

- simple low-stakes updates
- ordinary training decks
- quick first drafts unless the user asks
- visual beautification
- cases where it would make the answer longer without improving the decision

## Review Lenses

Translate Six Advisors-style thinking into functional lenses. Do not roleplay famous people unless the user explicitly asks.

Use only 2-4 lenses by default. Select based on the scenario.

| Lens | Core Question | Use When |
| --- | --- | --- |
| Customer Value | Does this presentation make the audience's real outcome clearer and more valuable? | sales, proposal, product/company introduction, training |
| Narrative Experience | Is there a memorable before/after journey instead of a list of points? | product launch, pitch, executive story, training |
| Clarity & Simplicity | What should be removed so the main judgment becomes easier to see? | scattered materials, overloaded decks, technical topics |
| Risk & Bias | What assumption, incentive, missing proof, or failure path could break the argument? | high-stakes decision, risk briefing, forecast, investment |
| Strategic Fit | Is this ask consistent with long-term positioning, capability, and what should be refused? | strategy, investment, major customer, partnership |
| Minimum Action | What is the smallest credible next step that turns uncertainty into evidence? | PoC, pilot, transformation, early-stage opportunity |

## Lens Selection Defaults

```yaml
sales_or_customer_pitch:
  default_lenses: [Customer Value, Risk & Bias, Minimum Action]

fundraising_or_investor:
  default_lenses: [Customer Value, Strategic Fit, Risk & Bias]

boss_or_executive_decision:
  default_lenses: [Strategic Fit, Risk & Bias, Minimum Action]

product_or_company_introduction:
  default_lenses: [Customer Value, Narrative Experience, Clarity & Simplicity]

training_or_enablement:
  default_lenses: [Customer Value, Narrative Experience, Clarity & Simplicity]

risk_or_crisis_briefing:
  default_lenses: [Risk & Bias, Clarity & Simplicity, Minimum Action]

career_or_personal_pitch:
  default_lenses: [Customer Value, Narrative Experience, Risk & Bias]
```

## Output Format

Keep advisor review compact.

```yaml
advisor_review:
  use_reason:
  selected_lenses:
    - lens:
      one_line_judgment:
      concern:
      required_proof:
      slide_implication:
      next_action:
  key_conflict:
  synthesis:
  smallest_validation_action:
  acceptance_criteria:
```

## Arbitration Rules

When lenses disagree, resolve in this order:

1. Audience value before speaker preference.
2. Material risk before narrative drama.
3. Trust before persuasion pressure.
4. Strategic fit before short-term excitement.
5. Minimum credible action before large unsupported asks.

## Quality Bar

Advisor review should improve the deck by changing at least one of:

- the central judgment
- the ask
- the evidence standard
- the storyline
- the page order
- the next validation action

If it only adds commentary, omit it.
