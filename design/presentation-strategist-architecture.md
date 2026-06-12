# Presentation Strategist Core Architecture

Date: 2026-06-12
Status: Agreed design foundation

## 1. Core Positioning

`presentation-strategist` is not a PPT beautification skill and not a generic slide outline generator.

It is a communication strategy skill that helps users design the logic behind a presentation before visual production begins.

Its job is to help users clarify:

- who the presentation must affect
- what state the audience is in now
- what state the audience should reach after the presentation
- what decision, belief, understanding, or action should change
- what argument and evidence can support that change
- what narrative structure fits the context
- how the logic should become a page-by-page PPT framework

Product-level summary:

> First define the audience change, then design the judgment, proof, narrative, and slide structure that can create that change.

## 2. Foundational Model

The skill is built on four parts:

```text
Vertical Six Layers
+ Horizontal Five Forces
+ Iteration Loop
+ Case Library
```

This model should guide all future `SKILL.md`, references, templates, and examples.

## 3. Vertical Six Layers

The vertical model answers:

> How does this presentation become logically valid and communicatively useful?

### Layer 0: Human Communication Atoms

At the deepest level, a presentation is one person or group trying to change another person's state.

Core atoms:

- who is speaking
- who is listening
- why this is being said now
- what the audience already knows
- what the audience currently believes
- what the audience cares about
- what the audience fears or resists
- what trust exists between speaker and audience
- what stakes the topic has for the audience
- what the audience should know, believe, decide, or do afterward

This layer is not about PPT. It is about human communication.

### Layer 1: Communication Task

Not every presentation is persuasion. The skill must first diagnose the actual communication task.

Important distinction:

```text
Communication goal = the specific audience change the user wants.
Communication task = the abstract type of communication needed to create that change.
```

Examples:

- Goal: get the boss to approve 2 headcount and 300k budget.
  Task: decide / persuade.
- Goal: get product, sales, and delivery teams to agree on serving priority customer segment A next quarter.
  Task: align.
- Goal: get a customer to enter PoC and schedule a technical review.
  Task: sell.
- Goal: make leadership understand project delay risk and decide whether to cut low-priority scope this week.
  Task: warn / decide.
- Goal: help new hires learn a reusable customer interview method.
  Task: teach.

The skill should usually ask for the concrete goal first, then infer or confirm the communication task.

Common tasks:

- inform: make the audience aware of facts
- explain: help the audience understand causes or mechanisms
- align: create shared understanding across people or teams
- decide: help decision-makers choose
- persuade: move the audience toward belief or support
- mobilize: make a team willing to act
- sell: create purchase or adoption intent
- teach: help the audience gain a transferable capability
- review: help an organization learn from facts
- warn: make the audience take risk seriously

This layer determines where the force of the presentation should go.

### Layer 2: Business Scenario

The scenario changes the strategy even when the communication task is similar.

Common scenarios:

- boss-facing update
- project proposal
- product introduction
- company introduction
- fundraising pitch
- customer sales deck
- training or knowledge sharing
- strategy announcement
- business review
- technical review
- crisis or risk briefing

Example distinction:

- A boss-facing update optimizes for judgment speed, risk clarity, and resource allocation.
- A customer sales deck optimizes for perceived value, trust, and low-risk adoption.

### Layer 3: Business Argument

This layer answers:

> Why should the audience believe this?

It must be separated from narrative. A presentation can be emotionally compelling and still fail commercially if its argument cannot survive scrutiny.

Core questions:

- What is the central judgment?
- What reasons support it?
- What evidence supports each reason?
- What counterexamples or objections exist?
- What alternatives were considered?
- Why is this conclusion better than other possible conclusions?
- What risks remain?
- What tradeoffs, constraints, costs, and benefits matter?

Relevant methods include:

- Pyramid Principle
- MECE decomposition
- hypothesis-driven thinking
- evidence mapping
- objection handling
- risk and tradeoff analysis

### Layer 4: Narrative And Expression

This layer answers:

> How do we make the audience willing to follow the argument?

It is not a substitute for proof. It shapes attention, tension, meaning, trust, and emotional movement.

Common narrative patterns:

- hero / obstacle / success
- protagonist / resistance / transformation
- current world / changed world
- problem / cost / solution / proof / action
- SCQA: situation, complication, question, answer
- what is / what could be
- strategic narrative and promised land
- ethos / pathos / logos

The audience should usually be treated as the protagonist. The speaker is the guide, strategist, or proof-provider.

### Layer 5: Slide Structure

This is the final layer, not the starting point.

It answers:

- How many pages are needed?
- What job does each page do?
- What is the action title of each page?
- Which page creates problem awareness?
- Which page states the core judgment?
- Which page proves each claim?
- Which page handles objections or risks?
- Which page moves the audience toward action?
- What evidence, example, chart, diagram, or demo should each page use?

The slide plan must be page-native but not decoration-driven. Each page should have one logical role.

## 4. Horizontal Five Forces

The horizontal forces answer:

> Will real people in a real context accept, resist, distort, or act on this message?

They cut across all six vertical layers.

### Force 1: Power Relationship

Presentations happen inside power structures.

The skill should consider:

- who has decision power
- who has veto power
- who influences the decision
- who is affected but absent
- who may support publicly but resist privately
- whose face, authority, or ownership must be protected

### Force 2: Trust Base

Logic only works when the audience gives the speaker, data, or institution enough trust.

The skill should consider:

- Does the audience trust the speaker?
- Does the audience trust the data?
- Does the audience trust the organization behind the message?
- Does the audience suspect a hidden motive?
- Has the speaker been reliable in the past?
- Does the presentation need credibility before it needs argument?

### Force 3: Psychological Resistance

Audiences are not empty containers. They have interests, identity, fear, and prior commitments.

The skill should detect whether the presentation asks the audience to admit:

- their past decision was wrong
- their department has a problem
- they need to give up resources
- they must accept more risk
- they must change a habit
- they must trust a new person, team, or method

Many presentations fail not because they are unclear, but because they trigger defense.

### Force 4: Field Constraint

The same content behaves differently in different communication fields.

Important constraints:

- formal vs informal
- synchronous vs asynchronous
- public vs private
- high-pressure vs exploratory
- first-time audience vs long-term relationship
- live speech vs read-ahead document
- executive meeting vs workshop vs sales conversation

The field changes density, tone, evidence format, pacing, and directness.

### Force 5: Ethical Boundary

The skill should improve clarity and persuasiveness without helping users manipulate the audience or hide truth.

It should not help:

- fabricate evidence
- disguise uncertainty as fact
- exaggerate urgency
- hide important risk
- use narrative to override material truth
- make weak evidence look stronger than it is

The skill should mark assumptions, weak claims, and missing proof clearly.

## 5. Iteration Loop

Presentations are not one-shot artifacts. They should be calibrated through feedback.

Core loop:

```text
Hypothesis -> Expression -> Feedback -> Revision
```

The skill should:

- form explicit assumptions about the audience, goal, resistance, and evidence
- create a first logic plan
- identify which assumptions need validation
- suggest who should preview key claims before the formal presentation
- revise the argument, narrative, and page plan based on feedback

## 6. Case Library

The skill should learn from positive examples, negative examples, and non-PPT communication systems.

Initial reference cases:

### Zuora Sales Narrative

Use as a reference for strategic narrative and B2B sales persuasion.

Key lesson:

> Do not start with the product. Start with the change in the customer's world.

Relevant concepts:

- changed world
- winners and losers
- promised land
- product as path, not hero

### Amazon PR/FAQ And Six-Page Memo

Use as a reference for thinking before presentation.

Key lesson:

> Good presentation begins with clear thinking, customer definition, risk, objections, and written reasoning.

Relevant concepts:

- working backwards from customer value
- narrative memo before slides
- decision-quality writing
- objections and FAQ as part of the argument

### Apple iPhone 2007 Launch

Use as a reference for category redefinition and product launch narrative.

Key lesson:

> A powerful launch can change how the audience understands a category, not merely describe a product.

Relevant concepts:

- familiar objects recombined into a new category
- suspense and reveal
- demo as proof
- product meaning before feature list

### Netflix Culture Deck

Use as a reference for internal alignment and organizational belief.

Key lesson:

> Some presentations are not meant to please everyone; they define what an organization believes and what tradeoffs it accepts.

Relevant concepts:

- values as operating system
- freedom with responsibility
- alignment and selection
- culture as strategic constraint

### NASA Columbia / PowerPoint Failure

Use as a negative reference for high-risk communication.

Key lesson:

> Poor presentation structure can bury risk, weaken evidence, and contribute to bad decisions.

Relevant concepts:

- risk must be explicit
- uncertainty must not be hidden
- evidence hierarchy matters
- slides are not always the right medium for complex technical judgment

## 7. Design Implications For The Skill

The skill should not ask first:

> How many slides do you want?

It should ask first:

> Who needs to change what after seeing this presentation?

Default execution order:

1. Diagnose communication task and business scenario.
2. Identify audience state, desired state, stakes, and ask.
3. Scan horizontal five forces.
4. Build central judgment and evidence map.
5. Choose narrative and expression pattern.
6. Convert the logic into a page-by-page slide framework.
7. Run logic, evidence, audience, and ethics QA.
8. Identify assumptions that need feedback and revision.

## 8. Non-Negotiable Quality Bar

A strong output must be:

- audience-changing, not merely information-listing
- scenario-aware, not template-driven
- evidence-aware, not claim-heavy
- power-aware, not naive about real organizations
- trust-aware, not assuming logic alone persuades
- resistance-aware, not ignoring what the audience may fear or lose
- field-aware, not using the same density and tone everywhere
- ethically clear, not persuasive at the cost of truth
- slide-native only at the final layer

Bad output looks like:

- a generic table of contents
- a school essay broken into slides
- a product feature list with no customer change
- a strategy deck with no decision or ask
- a beautiful deck hiding weak evidence
- a dramatic story with no business proof
- a risk briefing that buries uncertainty
