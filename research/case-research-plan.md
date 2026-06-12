# Presentation Strategist Case Research Plan

Date: 2026-06-12
Status: Research plan before skill implementation

## 1. Why This Research Is Needed

`presentation-strategist` should not be built from the user's personal examples alone.

Personal examples are useful for taste calibration, but they cannot provide enough coverage for a general-purpose communication strategy skill.

The skill should be built from:

```text
core communication atoms
+ public historical business cases
+ reusable scenario patterns
+ failure cases
+ non-PPT communication systems
```

The goal is not to copy famous decks. The goal is to extract the communication logic behind them and make that logic usable by an agent.

## 2. Research Questions

The case research should answer:

1. What communication tasks appear repeatedly across business history?
2. What audience-state changes do successful presentations create?
3. How do different scenarios alter argument, narrative, proof, and page structure?
4. What role do power, trust, resistance, field constraints, and ethics play?
5. What patterns separate a strong business presentation from a beautiful but weak deck?
6. What failure modes should the skill explicitly guard against?

## 3. Case Categories To Research

### A. Strategic Sales Narratives

Purpose:

Understand how business presentations sell change before selling a product.

Initial cases:

- Zuora sales deck, analyzed by Andy Raskin
- Drift sales narrative
- modern B2B category-creation decks

What to extract:

- changed world
- old game vs new game
- winners and losers
- promised land
- product as path, not hero
- executive vs practitioner audience differences

### B. Startup And Investor Pitch Decks

Purpose:

Understand how founders convert uncertainty into investable belief.

Initial cases:

- Sequoia Capital pitch deck framework
- YC Demo Day pitch guidance
- Airbnb pitch deck
- Uber pitch deck
- LinkedIn / YouTube / Buffer style early decks
- Toutiao / ByteDance 2013 Series B business plan
- Alibaba IPO roadshow
- Xiaomi IPO / ecosystem company roadshows where public material is available

What to extract:

- company purpose
- problem
- why now
- market size
- traction
- business model
- team credibility
- risk handling
- investor-specific proof

### C. Product Launch And Category Redefinition

Purpose:

Understand how a presentation changes how the audience understands a product category.

Initial cases:

- Apple iPhone 2007 launch
- Steve Jobs-era Apple keynotes
- Xiaomi SU7 launch
- Lei Jun annual speeches and product launches

What to extract:

- category reframing
- tension before reveal
- demo as proof
- product meaning before feature list
- familiar-to-new transition
- founder persona and trust base

### D. Internal Alignment And Culture Presentations

Purpose:

Understand how presentations define organizational beliefs, constraints, and operating systems.

Initial cases:

- Netflix Culture Deck
- Amazon leadership principles and narrative memo culture
- Huawei-style business review / operating analysis patterns where reliable public material exists

What to extract:

- values as operating logic
- who belongs and who does not
- tradeoffs made explicit
- alignment vs persuasion
- power and psychological resistance

### E. Decision Memos And Non-PPT Communication Systems

Purpose:

Avoid overfitting the skill to slide decks. Some of the best business communication happens before slides.

Initial cases:

- Amazon PR/FAQ
- Amazon six-page narrative memo
- Jeff Bezos shareholder letters
- strategy memos and read-ahead decision documents

What to extract:

- writing as thinking
- decision-quality argument
- FAQ as objection handling
- customer-backward reasoning
- when slides are the wrong medium

### F. Crisis And Risk Communication

Purpose:

Understand how communication changes when truth, urgency, risk, and trust matter more than persuasion.

Initial cases:

- Johnson & Johnson Tylenol crisis communication
- Toyota recall crisis communication
- NASA Columbia / Boeing PowerPoint failure

What to extract:

- risk visibility
- uncertainty disclosure
- responsibility and trust repair
- why polished slides can bury danger
- ethical constraints under pressure

### G. Executive Business Reviews And Operating Meetings

Purpose:

Understand non-glamorous but common business presentations: reviews, forecasts, variance analysis, and resource decisions.

Initial cases:

- management business review structures
- Huawei-style operating analysis patterns where reliable public material exists
- public investor relations decks and quarterly earnings presentations

What to extract:

- target vs actual
- variance and root cause
- forecast and risk
- next action
- resource request
- accountability loop

## 4. Analysis Template For Each Case

Each case should be analyzed through the agreed architecture:

```yaml
case:
  name:
  type:
  source:
  audience:
  communication_goal:
  communication_task:
  business_scenario:
  audience_current_state:
  audience_desired_state:
  stakes:
  central_judgment:
  evidence_strategy:
  narrative_pattern:
  slide_or_document_structure:
  power_relationship:
  trust_base:
  psychological_resistance:
  field_constraint:
  ethical_boundary:
  iteration_or_feedback_mechanism:
  reusable_lesson:
  anti_pattern_to_avoid:
```

## 5. Expected Skill Design Output After Research

After research, the skill design should include:

1. Trigger description and naming.
2. Diagnostic workflow based on communication atoms, not scenario templates.
3. Scenario presets as shortcuts, not the core engine.
4. Question strategy that distinguishes communication goal from communication task.
5. Argument builder that forces central judgment, evidence, objections, and risk.
6. Narrative selector that chooses frameworks based on task and audience resistance.
7. Slide planner that turns logic into page roles and action titles.
8. QA rubric covering logic, evidence, audience, power, trust, resistance, field, and ethics.
9. Handoff schema for downstream PPT generation skills.
10. Case-library reference notes that the agent can consult when relevant.

## 6. Design Direction Already Implied

The skill should not be implemented as:

```text
if boss report -> use boss report template
if sales deck -> use sales deck template
if training -> use training template
```

It should be implemented as:

```text
1. Identify concrete communication goal.
2. Infer or confirm communication task.
3. Diagnose business scenario and field.
4. Map audience current state, desired state, stakes, and ask.
5. Scan power, trust, resistance, field, and ethics.
6. Build argument and evidence map.
7. Select narrative and expression pattern.
8. Convert into slide-by-slide structure.
9. Run QA and identify assumptions needing feedback.
```

Scenario presets can accelerate the process, but they must not replace diagnosis.

