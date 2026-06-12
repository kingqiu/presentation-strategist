# Business Scenarios

Use scenarios as presets, not templates. Always override based on the concrete communication goal, evidence strength, audience resistance, and field.

## Boss-Facing Update

```yaml
default_task: decide / align / warn
likely_audience_state: busy, needs judgment efficiency, may distrust long background
typical_resistance: unclear ask, risk hidden, too much process detail
proof_standard: facts, variance, options, cost, risk, recommended decision
recommended_structure: answer first -> context -> drivers -> options -> risks -> ask
common_failure_modes: no decision request, too much background, unclear resource implication
```

Subtypes:

```yaml
normal_progress_sync:
  likely_goal: make the boss understand current status and stay confident
  structure: status judgment -> completed milestones -> variance -> next milestones -> watch items
  action_title_style: "项目总体按计划推进，但下周的 X 是唯一需要提前关注的变量"

risk_update:
  likely_goal: make the boss understand risk and decide mitigation
  structure: status judgment -> risk facts -> impact -> options -> recommendation -> decision needed
  action_title_style: "项目不是全面延期，真正会影响交付的是 X 资源缺口"

resource_request:
  likely_goal: get approval for budget, people, priority, or coordination
  structure: answer first -> business need -> current gap -> options -> recommended ask -> ROI/risk
  action_title_style: "新增 2 人可以把交付瓶颈从 6 周压缩到 2 周"

decision_request:
  likely_goal: get the boss to choose between alternatives
  structure: decision needed -> criteria -> options -> tradeoffs -> recommendation -> next step
  action_title_style: "现在需要决定是保范围延期，还是砍范围保上线"
```

For a vague input such as "明天要跟老板汇报项目进度", start with `normal_progress_sync` but check whether it is actually `risk_update`, `resource_request`, or `decision_request`.

## Project Proposal

```yaml
default_task: persuade / decide
likely_audience_state: interested but worried about cost, execution, and priority
typical_resistance: "why now", "why this team", "what if it fails"
proof_standard: problem size, expected benefit, feasibility, resources, risk controls
recommended_structure: problem -> stakes -> recommendation -> plan -> economics -> risks -> decision
common_failure_modes: solution before problem, no tradeoff, weak implementation plan
```

## Product Introduction

```yaml
default_task: explain / persuade / sell
likely_audience_state: does not yet understand why the product matters
typical_resistance: feature fatigue, incumbent comparison, unclear value
proof_standard: use case, pain, demo, differentiator, outcome proof
recommended_structure: user pain -> new capability -> workflow/demo -> proof -> adoption path
common_failure_modes: feature list, no target user, no proof of value
```

## Company Introduction

```yaml
default_task: build trust / explain / persuade
likely_audience_state: low knowledge, evaluating credibility and fit
typical_resistance: unclear differentiation, generic claims, no proof
proof_standard: mission, capability, customer proof, differentiation, cooperation logic
recommended_structure: who we serve -> why we matter -> what we do -> proof -> why partner now
common_failure_modes: history dump, slogan-heavy, no audience-specific reason to care
```

## Fundraising Pitch

```yaml
default_task: persuade / de-risk
likely_audience_state: skeptical, pattern-matching quickly, seeking asymmetric upside
typical_resistance: market timing, founder risk, weak traction, unclear moat
proof_standard: problem, why now, traction or insight, market, model, team, use of funds
recommended_structure: purpose -> problem -> why now -> solution -> proof -> market -> model -> team -> ask
common_failure_modes: inflated TAM, vague moat, too much product detail, no investor-specific ask
```

## Career / Personal Pitch

```yaml
default_task: persuade / de-risk / differentiate
likely_audience_state: evaluating fit, evidence, risk, and role relevance
typical_resistance: generic self-introduction, unclear role fit, unsupported claims
proof_standard: target role need, fit thesis, proof stories, measurable outcomes, learning ability, next-step ask
recommended_structure: role need -> fit thesis -> 2-3 proof stories -> risk reduction -> contribution plan -> next step
common_failure_modes: autobiography, credential list, no employer problem, no proof of impact
```

## Customer Sales Deck

```yaml
default_task: sell / reframe / de-risk
likely_audience_state: aware of pain but unsure whether change is worth it
typical_resistance: switching cost, trust, budget, internal alignment
proof_standard: changed world, cost of status quo, solution path, proof, adoption risk control
recommended_structure: changed world -> old approach breaks -> promised land -> product as path -> proof -> next step
common_failure_modes: product-first, false urgency, no economic buyer logic
```

## Training / Knowledge Sharing

```yaml
default_task: teach / mobilize
likely_audience_state: mixed prior knowledge, needs practical transfer
typical_resistance: abstract concepts, low relevance, no practice path
proof_standard: learner gap, concept ladder, examples, practice, transfer checklist
recommended_structure: learner problem -> concept ladder -> example -> practice -> recap -> application
common_failure_modes: encyclopedia content, no practice, no behavior change
```

## Strategy Announcement

```yaml
default_task: align / mobilize
likely_audience_state: uncertain about meaning and impact
typical_resistance: fear of loss, unclear tradeoffs, hidden politics
proof_standard: why change, decision principles, tradeoffs, operating implications, next rhythm
recommended_structure: changed context -> strategic choice -> tradeoffs -> implications -> operating rhythm
common_failure_modes: slogans, no tradeoffs, no behavior implications
```

## Business Review

```yaml
default_task: review / explain / decide
likely_audience_state: wants performance truth and next action
typical_resistance: cherry-picked metrics, vague root cause, no accountability
proof_standard: target vs actual, variance, drivers, risks, actions
recommended_structure: status -> variance -> drivers -> risks -> next actions -> decision/resource asks
common_failure_modes: metric dump, no "so what", no owner or action
```

## Technical Review

```yaml
default_task: decide / de-risk
likely_audience_state: needs confidence under constraints
typical_resistance: hidden assumptions, overclaiming, implementation risk
proof_standard: criteria, options, tradeoffs, recommendation, validation plan
recommended_structure: decision criteria -> options -> tradeoffs -> recommendation -> risks -> validation plan
common_failure_modes: advocacy without criteria, buried tradeoffs, no rollback plan
```

## Crisis / Risk Briefing

```yaml
default_task: warn / decide / repair trust
likely_audience_state: worried, accountability-seeking, time-sensitive
typical_resistance: organization may want to minimize bad news
proof_standard: facts, harm/risk, uncertainty, responsibility, action, monitoring
recommended_structure: facts -> risk/harm -> uncertainty -> action -> decision needed -> monitoring
common_failure_modes: burying uncertainty, defensive tone, no owner, no decision
```

## Investor Relations / Earnings Update

```yaml
default_task: explain / de-risk / assure
likely_audience_state: scanning for performance, durability, risk, and guidance credibility
typical_resistance: complexity, unclear unit economics, forward-looking uncertainty
proof_standard: segment metrics, drivers, thesis, risks, caveats
recommended_structure: market context -> performance facts -> drivers -> strategic interpretation -> risks -> outlook
common_failure_modes: numbers without thesis, thesis without numbers, hidden caveats
```
