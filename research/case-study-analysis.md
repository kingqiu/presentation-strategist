# Presentation Strategist Case Study Analysis

Date: 2026-06-12
Status: Research synthesis for skill design

## 1. Research Scope

This document analyzes public business communication cases to calibrate the `presentation-strategist` skill architecture.

It intentionally covers multiple communication forms:

- sales decks and category narratives
- startup fundraising decks
- IPO and investor roadshows
- product launches
- internal culture and alignment documents
- decision memos and non-PPT systems
- annual letters and business reviews
- crisis and risk communication
- failure cases where presentation format damaged judgment

The research does not try to copy slide sequences. It extracts reusable communication logic through the agreed architecture:

```text
Vertical six layers + horizontal five forces + iteration loop
```

## 2. Case Coverage Matrix

| # | Case | Category | Main communication task | Primary lesson for the skill |
| --- | --- | --- | --- | --- |
| 1 | Zuora sales narrative | Strategic sales | Sell / persuade | Sell the customer's changed world before selling the product. |
| 2 | Drift strategic pitch | Strategic sales | Sell / reframe | A pitch can work by naming a new market reality and forcing urgency. |
| 3 | Salesforce "No Software" | Category creation | Reframe / sell | A strong enemy can be an old operating model, not a competitor. |
| 4 | HubSpot inbound marketing | Category creation | Teach / sell | Category creation requires educating the market before asking it to buy. |
| 5 | Airbnb early pitch deck | Fundraising | Persuade / fundraise | Early decks win through problem clarity, validation, and simple market logic. |
| 6 | UberCab early pitch deck | Fundraising | Persuade / fundraise | A deck can make an unfamiliar model credible by anchoring it to a familiar pain. |
| 7 | LinkedIn Series B deck | Fundraising | Persuade / fundraise | Weak present metrics can be reframed through prior promises kept and future concept logic. |
| 8 | Buffer seed deck | Fundraising | Persuade / fundraise | Traction-first storytelling can substitute for grand strategic theater. |
| 9 | Sequoia business plan framework | Fundraising meta | Decide / invest | Investor logic repeatedly asks purpose, problem, why now, market, product, team, financials. |
| 10 | YC Demo Day guidance | Fundraising meta | Compress / persuade | Extreme field constraints force ruthless message selection. |
| 11 | Toutiao 2013 business plan | Fundraising China | Persuade / fundraise | Technical advantage must be translated into user behavior, growth, and market potential. |
| 12 | Alibaba 2014 IPO roadshow | IPO roadshow | Persuade / de-risk | At IPO scale, the task is to turn a complex ecosystem into an investable story. |
| 13 | Xiaomi IPO / Mi ecosystem story | IPO roadshow | Persuade / explain | Ecosystem businesses need a structure that connects hardware, services, users, and margins. |
| 14 | Apple iPhone 2007 launch | Product launch | Reframe / excite | Category redefinition works by recombining familiar objects into a new mental model. |
| 15 | Tesla Secret Master Plan | Strategy narrative | Align / persuade | A strategic memo can justify today's constraints through a staged future path. |
| 16 | Xiaomi SU7 launch | Product launch China | Reframe / sell | Founder trust, product proof, ecosystem meaning, and pricing all carry the persuasion. |
| 17 | OpenAI DevDay 2023 | Developer launch | Mobilize / enable | Developer launches need demos, lower adoption friction, and a clear new capability map. |
| 18 | Netflix Culture Deck / Memo | Internal alignment | Align / select | Culture communication defines tradeoffs, not just values. |
| 19 | Amazon six-page narratives | Decision system | Decide / align | Better decisions may require replacing slides with written argument. |
| 20 | Amazon PR/FAQ | Product decision | Align / validate | Start from a future customer outcome, then force objections before building. |
| 21 | Bezos / Amazon shareholder letters | Investor narrative | Align / explain | Annual communication can turn operating principles into a long-term investor contract. |
| 22 | Stripe annual letters | Investor / ecosystem narrative | Explain / build trust | Business updates can use ecosystem-level evidence to frame company progress. |
| 23 | NVIDIA quarterly investor presentations | Business review | Explain / de-risk | Financial presentations must bind numbers to a durable market thesis. |
| 24 | Microsoft AI annual report narrative | Strategic investor communication | Reframe / assure | Incumbents must explain why a platform shift strengthens rather than threatens them. |
| 25 | NASA Columbia PowerPoint failure | Risk communication failure | Warn / decide | Slide compression can bury uncertainty and weaken judgment. |
| 26 | Johnson & Johnson Tylenol crisis | Crisis communication | Warn / repair trust | In crisis, trust and ethical action precede persuasion. |
| 27 | Toyota 2010 recall testimony | Crisis communication | Repair / explain | Defensive framing can worsen trust when accountability is the needed task. |

This gives 27 cases across the required scene categories, exceeding the minimum of 20.

## 3. Source Notes

Primary and close-to-primary sources were preferred where available. Some famous early pitch decks are mainly available through secondary repositories and teardown sites; those are used only to extract communication structure, not to treat every slide as authoritative.

Key sources:

- Zuora / Andy Raskin: https://medium.com/the-mission/the-greatest-sales-deck-ive-ever-seen-4f4ef3391ba0 and https://www.zuora.com/resource/best-sales-deck-ever/
- Drift / Andy Raskin: https://www.linkedin.com/pulse/best-sales-pitch-ive-seen-all-year-andy-raskin
- Sequoia: https://sequoiacap.com/article/writing-a-business-plan/
- YC Demo Day: https://www.ycombinator.com/blog/guide-to-demo-day-pitches/
- Airbnb early deck: https://www.slideshare.net/slideshow/airbnb-first-pitch-deck-editable/45768374 and https://slidebean.com/blog/airbnb-pitch-deck
- UberCab early deck: https://www.failory.com/pitch-deck/uber and https://slidebean.medium.com/the-uber-pitch-deck-used-to-raise-funding-in-2008-a7fe121fe72b
- LinkedIn Series B: https://www.reidhoffman.org/linkedin-pitch-to-greylock/ and https://www.businessinsider.com/reid-hoffman-startup-advice-and-linkedin-series-b-pitch-deck-2013-10
- Buffer seed deck: https://www.failory.com/pitch-deck/buffer and https://upmetrics.co/pitch-deck-examples/buffer
- Toutiao 2013 plan: https://www.scribd.com/document/856591865/%E4%BB%8A%E6%97%A5%E5%A4%B4%E6%9D%A12013%E5%B9%B4B%E8%BD%AE%E8%9E%8D%E8%B5%84%E5%95%86%E4%B8%9A%E8%AE%A1%E5%88%92%E4%B9%A6 and https://zhuanlan.zhihu.com/p/409365164
- Alibaba IPO roadshow: https://www.slideshare.net/slideshow/alibaba-roadshow-presentation/39177754 and https://imagination.com/work/alibaba-international-roadshow/
- Xiaomi IPO: https://cnbj1.fds.api.xiaomi.com/company/financial/en-US/IPO.pdf and https://ir.mi.com/
- Apple iPhone 2007: https://www.apple.com/newsroom/2007/01/09Apple-Reinvents-the-Phone-with-iPhone/ and transcript mirrors such as https://singjupost.com/wp-content/uploads/2014/07/Steve-Jobs-iPhone-2007-Presentation-Full-Transcript.pdf
- Tesla Master Plan: https://www.tesla.com/secret-master-plan
- Xiaomi SU7 public launch context: https://autonews.gasgoo.com/articles/ev/lei-jun-new-generation-xiaomi-su7-set-for-official-launch-this-month-2032435814632423425 and public launch coverage
- OpenAI DevDay 2023: https://www.youtube.com/watch?v=U9mJuUkhUzk and https://community.openai.com/t/openai-dev-day-2023-live-reactions/475167
- Netflix culture: https://jobs.netflix.com/culture and https://about.netflix.com/news/sharing-our-latest-culture-memo
- Amazon six-page narratives: https://www.aboutamazon.com/news/company-news/2017-letter-to-shareholders
- Amazon Working Backwards / PRFAQ: https://www.aboutamazon.com/news/workplace/an-insider-look-at-amazons-culture-and-processes and https://workingbackwards.com/resources/working-backwards-pr-faq/
- Stripe annual letters: https://stripe.com/annual-updates/2023 and https://stripe.com/annual-updates/2024
- NVIDIA investor presentations: https://investor.nvidia.com/events-and-presentations/presentations/default.aspx and https://investor.nvidia.com/financial-info/quarterly-results/default.aspx
- Microsoft annual reports: https://www.microsoft.com/investor/reports/ar24/index.html and https://www.microsoft.com/investor/reports/ar25/index.html
- NASA Columbia / Tufte: https://www.edwardtufte.com/notebook/powerpoint-does-rocket-science-and-better-techniques-for-technical-reports/ and https://ehss.energy.gov/deprep/archive/documents/0308_caib_report_volume1.pdf
- Tylenol crisis: https://knowledge.wharton.upenn.edu/article/tylenol-and-the-legacy-of-jjs-james-burke/ and https://business.rice.edu/wisdom/features/how-can-companies-survive-crisis
- Toyota recall: https://www.cbsnews.com/news/akio-toyoda-congressional-testimony-i-am-deeply-sorry-full-text/ and crisis analyses such as https://www.finn.agency/crisis-communication-case-toyota-gm-product-recall/

## 4. Pattern Analysis By Category

### A. Strategic Sales Narratives

Cases:

- Zuora
- Drift
- Salesforce "No Software"
- HubSpot inbound marketing

Observed pattern:

```text
changed world -> old approach breaks -> winners/losers -> new operating belief -> product as path -> proof
```

Skill implication:

For sales and category-creation presentations, the skill should not start with features. It should first ask:

- What has changed in the customer's world?
- What old assumption is now dangerous?
- What cost does the audience pay if they stay still?
- What new success state becomes possible?
- Why is the user's offer a credible path?

Horizontal forces:

- Power: economic buyer, technical evaluator, and end user often need different arguments.
- Trust: proof must appear before aggressive claims.
- Resistance: customers resist admitting their current system is obsolete.
- Field: sales decks are often forwarded internally, so action titles must stand alone.
- Ethics: avoid inventing a false market shift merely to create urgency.

### B. Startup And Investor Pitches

Cases:

- Airbnb
- UberCab
- LinkedIn
- Buffer
- Sequoia framework
- YC Demo Day
- Toutiao

Observed pattern:

```text
purpose -> painful problem -> unique solution -> why now -> proof/traction -> market scale -> business model -> team -> ask
```

But actual ordering depends on evidence strength:

- Airbnb emphasizes simple problem and market validation.
- LinkedIn uses concept-driven reasoning because early revenue was weak.
- Buffer leans on traction and clarity.
- YC Demo Day compresses the argument into a high-density spoken pitch.
- Toutiao translates technical personalization into user engagement and growth.

Skill implication:

The skill must diagnose evidence strength before choosing structure:

- If traction is strong, lead with traction sooner.
- If traction is weak but concept is strong, lead with market logic, why-now, and team credibility.
- If product is hard to understand, demonstrate the workflow before financial projections.
- If investor trust is low, explain why this team has unfair insight.

Horizontal forces:

- Power: investors can say no quickly; the pitch must earn attention early.
- Trust: team credibility and prior commitments matter.
- Resistance: investors fear category risk, founder risk, market timing risk, and weak differentiation.
- Field: pitch time limits force omission discipline.
- Ethics: do not inflate TAM or traction; mark assumptions.

### C. IPO And Public Investor Communication

Cases:

- Alibaba IPO roadshow
- Xiaomi IPO
- NVIDIA investor presentations
- Microsoft annual report AI narrative
- Stripe annual letters
- Bezos / Amazon shareholder letters

Observed pattern:

```text
market shift -> company position -> operating model -> proof metrics -> risk/forward view -> long-term thesis
```

IPO and public investor communications differ from seed decks:

- Investors already expect scale and governance.
- The task is de-risking as much as excitement.
- Complex businesses need a simple mental model.
- Forward-looking claims must be tied to disclosed facts, non-GAAP caveats, and risk boundaries.

Skill implication:

For investor-facing mature-company materials, the skill should force:

- business model simplification
- segment-level evidence
- margin and growth logic
- risk and regulatory caveats
- long-term thesis
- clear distinction between historical fact and forward-looking belief

Horizontal forces:

- Power: investors and analysts challenge assumptions; regulators constrain language.
- Trust: credibility comes from consistent reporting and transparent caveats.
- Resistance: public investors resist complexity and unclear unit economics.
- Field: read-ahead materials matter as much as live delivery.
- Ethics: financial communication must not obscure risk.

### D. Product Launch And Category Redefinition

Cases:

- Apple iPhone 2007
- Tesla Master Plan
- Xiaomi SU7
- OpenAI DevDay 2023

Observed pattern:

```text
familiar world -> unresolved friction -> new category / new capability -> demonstration -> proof -> adoption path
```

Case-specific lessons:

- Apple recombined familiar categories into a new object and used reveal timing as narrative proof.
- Tesla justified a premium first product as the first step in a long path toward mass affordability.
- Xiaomi SU7 needed to overcome trust barriers as a phone company entering automobiles; founder credibility, engineering proof, ecosystem logic, and pricing carried the launch.
- OpenAI DevDay had a developer field constraint: show capabilities, reduce implementation friction, and make the new platform programmable.

Skill implication:

For product launches, the skill should decide whether the core task is:

- introduce a product
- redefine a category
- prove technical credibility
- drive adoption
- restore trust after skepticism

The slide structure should then balance:

- meaning before feature list
- demo as proof
- adoption path
- pricing / packaging if purchase is immediate
- objections and constraints

Horizontal forces:

- Power: press, customers, partners, developers, and internal sales teams all receive the message.
- Trust: founder, brand, and demo reliability are central.
- Resistance: audiences compare against incumbents and prior expectations.
- Field: live launches use suspense; developer launches need operational clarity.
- Ethics: demos must not overstate product readiness.

### E. Internal Alignment And Decision Systems

Cases:

- Netflix Culture Deck / Memo
- Amazon six-page narratives
- Amazon PR/FAQ

Observed pattern:

```text
principle / customer outcome -> tradeoffs -> operating implications -> objections -> decision or behavior standard
```

Case-specific lessons:

- Netflix culture communication is strong because it states real tradeoffs: freedom with responsibility, high talent density, less process.
- Amazon six-page narratives show that the right communication medium may be prose, not slides, when the goal is decision quality.
- Amazon PR/FAQ starts from a future customer experience and forces hard questions before committing resources.

Skill implication:

The skill must sometimes recommend:

> Do not make a slide deck yet; write a narrative brief first.

For internal decisions and alignment, it should ask:

- What behavior or decision norm is being changed?
- What tradeoff must the organization accept?
- Which objections should be handled before the meeting?
- Is this a live presentation or a read-ahead decision document?

Horizontal forces:

- Power: internal politics and ownership are often the hidden issue.
- Trust: teams need to believe the process is fair, not just logical.
- Resistance: culture and strategy decks threaten identity and status.
- Field: memo meetings and slide meetings create different thinking behavior.
- Ethics: culture decks should describe actual operating principles, not aspirational slogans.

### F. Crisis, Risk, And Failure Cases

Cases:

- NASA Columbia PowerPoint failure
- Johnson & Johnson Tylenol crisis
- Toyota 2010 recall testimony

Observed pattern:

```text
facts -> risk / harm -> uncertainty -> responsibility -> action -> monitoring -> trust repair
```

Case-specific lessons:

- NASA Columbia shows how slide compression can bury uncertainty and weaken technical judgment.
- Tylenol shows that visible ethical action can restore trust more powerfully than defensive messaging.
- Toyota shows the risk of delayed or defensive framing when public accountability is expected.

Skill implication:

For risk and crisis presentations, the skill must prioritize:

- fact clarity
- risk visibility
- uncertainty disclosure
- responsibility
- decision needed now
- audience-specific action

It should actively avoid:

- burying uncertainty in bullets
- using persuasive narrative to soften material risk
- over-designing visuals when a technical appendix or memo is needed

Horizontal forces:

- Power: regulators, public, executives, and affected users may have conflicting needs.
- Trust: speed, accountability, and evidence matter more than polish.
- Resistance: organizations resist admitting harm.
- Field: public testimony and internal risk briefings have different constraints.
- Ethics: truth outranks persuasion.

### G. Operating Reviews And Business Updates

Cases:

- NVIDIA quarterly investor presentation
- Microsoft AI annual report narrative
- Stripe annual letters
- Amazon shareholder letters

Observed pattern:

```text
context -> performance facts -> variance / drivers -> strategic interpretation -> risks -> next period priorities
```

Skill implication:

For business reviews, the skill should not turn updates into generic summaries. It should force:

- target vs actual
- key drivers
- what changed vs prior belief
- what management wants the audience to infer
- risks and counter-signals
- actions or resource decisions

Horizontal forces:

- Power: the audience often judges management competence.
- Trust: consistent metrics and caveats build credibility.
- Resistance: audiences notice cherry-picked numbers.
- Field: financial readers scan; action titles and tables must carry the message.
- Ethics: distinguish fact, interpretation, and forecast.

## 5. Case-By-Case Calibration Notes

These notes are intentionally compact. They are not meant to become templates; they show how each case calibrates the diagnostic engine.

| Case | Audience state change | Argument / proof lesson | Narrative lesson | Horizontal force lesson | Skill calibration |
| --- | --- | --- | --- | --- | --- |
| Zuora sales narrative | From seeing billing as back office to seeing subscription revenue as strategic change | Proof must show that subscription businesses need a different operating model | Changed world before product | Customers resist admitting their current systems are obsolete | For sales decks, ask "what changed in the customer's world?" before features. |
| Drift strategic pitch | From accepting forms and lead capture to seeing conversational marketing as the new buyer expectation | Evidence should connect buyer behavior shift to revenue process change | Name the new game and show old-game losers | Marketing and sales stakeholders need aligned urgency | For category sales, identify old belief, new belief, and internal buyer split. |
| Salesforce "No Software" | From accepting installed enterprise software to believing cloud delivery is a better model | Argument converts technical delivery model into business agility | Old enemy is software ownership burden, not another vendor | IT trust and buyer fear of control loss are central | Let "enemy" be an operating model, not necessarily a company. |
| HubSpot inbound marketing | From outbound interruption to attraction-based customer acquisition | Teach the market enough to make the product category legible | Education as selling | Buyers may not know they have the named problem yet | For category creation, include teaching slides before product slides. |
| Airbnb early deck | From "strangers renting rooms is odd" to "event-driven budget lodging is validated" | Use simple pain, market validation, and transaction model | Ordinary travel frustration becomes a marketplace opportunity | Investor trust is fragile because the behavior feels socially unusual | For novel marketplaces, prove behavior before market size. |
| UberCab early deck | From taxi status quo to mobile on-demand premium car as plausible | Anchor new model in familiar taxi inefficiencies and target cities | Familiar pain plus aspirational service | Operational and regulatory risk sit under the pitch | For early models, show constrained beachhead before grand scale. |
| LinkedIn Series B | From weak revenue concern to trust in concept and execution trajectory | Prior promise kept can become proof when current numbers are incomplete | Concept-driven pitch can bridge early data gaps | Founder credibility carries more weight than polished slides | If data is weak, check whether credibility and prior milestones can carry the ask. |
| Buffer seed deck | From "small social tool" to "clear traction and disciplined team" | Traction and transparency can be stronger than large claims | Simple, focused progression | Investor resistance drops when numbers are direct | Prefer traction-first structure when evidence is clean. |
| Sequoia business plan framework | From scattered startup story to investor decision logic | Purpose, problem, why now, market, product, team, financials form a repeatable proof chain | Framework as investor mental model | Investors scan for missing standard proof | Use as checklist, not as universal slide order. |
| YC Demo Day guidance | From broad explanation to compressed fundable claim | Extreme time limit forces proof and clarity per sentence | One-minute urgency | Field constraint dominates structure | In short pitches, remove all context that does not move the decision. |
| Toutiao 2013 business plan | From "news app" to "personalized content engine with growth potential" | Technical differentiation must become user engagement and growth evidence | Data/algorithm as hidden engine behind user value | Investors need to believe technical moat and consumer habit | Translate technology into behavior, retention, and market logic. |
| Alibaba IPO roadshow | From fragmented view of China e-commerce to investable ecosystem thesis | Scale, ecosystem role, monetization, and growth metrics de-risk complexity | Founder/platform story plus numbers | Global investors need trust in governance and China context | For complex ecosystems, build a simple mental model before segments. |
| Xiaomi IPO / Mi ecosystem | From hardware company to internet-enabled ecosystem company | Need to connect devices, users, services, and margin logic | Ecosystem as flywheel | Investors resist hardware margin pressure | Force the business model bridge when a company spans categories. |
| Apple iPhone 2007 | From phone/iPod/internet as separate devices to one new category | Demo is proof; familiar categories make novelty understandable | Suspense, recombination, reveal | Brand and founder trust allow theatrical pacing | For launch decks, decide whether the task is product intro or category redefinition. |
| Tesla Master Plan | From expensive sports car skepticism to staged path toward affordable EVs | Today's premium product is justified by future cost curve and mission | Roadmap as moral and strategic journey | Skepticism about feasibility and economics is high | For strategy narratives, connect current constraint to future path. |
| Xiaomi SU7 launch | From phone-company skepticism to EV contender credibility | Engineering proof, ecosystem, price, and delivery capability all matter | Founder commitment and product proof | Trust barrier is higher when entering a new industry | For cross-category launches, lead with credibility gaps and proof plan. |
| OpenAI DevDay 2023 | From AI curiosity to developer action on new platform capabilities | Lower cost, better models, APIs, demos, and tooling are proof | Capability map plus live examples | Developers resist unclear implementation paths | For developer launches, include adoption path and friction reduction. |
| Netflix Culture Deck / Memo | From generic values to explicit operating contract | Tradeoffs prove seriousness: freedom requires responsibility and talent density | Culture as selection mechanism | Psychological resistance is expected; not everyone should agree | Internal culture decks should state real tradeoffs, not slogans. |
| Amazon six-page narratives | From presentation performance to decision-quality written reasoning | Narrative prose exposes weak logic that slides can hide | Medium choice is part of strategy | Power shifts from presenter charisma to argument quality | Recommend memo when complexity or decision risk is high. |
| Amazon PR/FAQ | From idea-first product planning to customer-backward validation | FAQ forces objections before building | Future press release makes desired customer outcome concrete | Internal stakeholders can challenge assumptions earlier | Use PR/FAQ when product proposals are uncertain or customer value is unclear. |
| Amazon shareholder letters | From quarterly numbers to long-term operating philosophy | Repeated principles build investor trust over time | Shareholder letter as strategic contract | Investor patience depends on trust and consistency | For long-term updates, connect facts to principles and prior commitments. |
| Stripe annual letters | From company update to broader internet economy thesis | Company metrics gain meaning through ecosystem-scale context | Annual letter as market readout | Trust comes from concrete scale signals and reliability claims | For ecosystem businesses, frame company progress through user progress. |
| NVIDIA investor presentations | From quarterly results to AI infrastructure thesis | Segment metrics must support durable demand narrative | Numbers plus platform thesis | Investors resist bubble and supply-chain risk | Business reviews need both metric truth and market interpretation. |
| Microsoft AI annual report narrative | From incumbent risk to platform-shift reinvention | Historical capability and current AI/cloud results support continuity | Reinvention as repeated company pattern | Stakeholders watch for disruption risk | For incumbents, address "why won't this shift hurt you?" directly. |
| NASA Columbia PowerPoint failure | From technical concern to under-communicated fatal risk | Evidence hierarchy and uncertainty must not be compressed away | Narrative polish is dangerous in risk contexts | Organizational pressure suppressed curiosity | For risk briefings, recommend memo/appendix and explicit uncertainty. |
| Johnson & Johnson Tylenol crisis | From public fear to trust restored through visible action | Ethical action is stronger proof than messaging | Safety-first action narrative | Public trust depends on values under cost pressure | In crisis, lead with harm, responsibility, action, and monitoring. |
| Toyota 2010 recall testimony | From loyalty to safety doubt and accountability demand | Defensive explanation is weak when accountability is expected | Apology must be paired with concrete corrective system | Public, regulator, and customer fields collide | In crisis, avoid over-defending; answer trust damage first. |

## 6. Cross-Case Findings

### Finding 1: The audience state change is more fundamental than the deck type.

Across cases, the strongest communication artifacts are designed around a shift:

```text
unaware -> aware
confused -> clear
skeptical -> cautiously convinced
passive -> urgent
fragmented -> aligned
afraid -> trusting
interested -> ready to act
```

Therefore, the skill should ask for or infer current state and desired state before slide count.

### Finding 2: Communication goal and communication task must remain separate.

Examples:

- Goal: get investor term sheets.
  Task: persuade / de-risk.
- Goal: get executives to cut scope this week.
  Task: warn / decide.
- Goal: make developers build with a new API.
  Task: mobilize / enable.

The skill should ask for the goal in concrete language and then classify the task.

### Finding 3: Scenario presets are useful but dangerous.

"Investor pitch" does not always mean the same structure:

- Airbnb: problem and validation.
- LinkedIn: concept and trust in founder promise.
- Buffer: traction and focus.
- Toutiao: technical differentiation translated into growth.

The skill should use scenario presets as shortcuts, then override them based on evidence strength, audience resistance, and field constraints.

### Finding 4: Proof strategy should decide narrative strategy.

If proof is strong, lead with proof earlier. If proof is weak, the deck must either:

- mark the claim as hypothesis
- lean on first-principles logic
- use analogy carefully
- ask for exploration rather than commitment

The skill should never let narrative confidence outrun evidence.

### Finding 5: The hidden work is often power, trust, and resistance.

Cases repeatedly show that failure is rarely just structure:

- Customers resist admitting their old system is obsolete.
- Investors resist uncertainty and vague TAM.
- Internal teams resist identity-threatening culture or strategy changes.
- Executives resist risk visibility when it threatens prior commitments.

The skill needs a quiet diagnostic pass over horizontal forces before giving a slide plan.

### Finding 6: Some situations require a memo before slides.

Amazon and NASA are opposite lessons with the same conclusion:

- High-stakes decisions need enough explanatory bandwidth.
- Slides can support discussion but can also compress evidence dangerously.

The skill should recommend a written brief, appendix, or decision memo when:

- the evidence is complex
- risk is high
- assumptions need scrutiny
- the audience will read asynchronously
- legal, technical, or financial nuance matters

### Finding 7: Action titles are a business thinking tool.

Across strong decks, titles should carry claims, not merely topics.

Weak:

```text
Market Overview
Product Features
Financials
Risks
```

Strong:

```text
Subscription models are shifting revenue control from product launches to customer lifetime value.
Our early retention proves the product solves a repeat pain, not a one-time curiosity.
The main risk is not demand; it is delivery capacity over the next two quarters.
```

The skill should require slide-level action titles in standard outputs.

### Finding 8: Ethical boundaries are design requirements, not afterthoughts.

Crisis and investor cases make this explicit:

- do not hide uncertainty
- do not inflate proof
- do not manufacture urgency
- do not use story to obscure risk
- do not convert assumptions into facts

The skill should label unsupported claims and missing evidence by default.

## 7. Implications For `presentation-strategist`

The case research confirms the agreed architecture and suggests the following design:

1. The skill should be diagnosis-first, not template-first.
2. It should ask for the concrete communication goal before classifying the communication task.
3. It should map audience current state, desired state, stakes, ask, and resistance.
4. It should scan power, trust, psychological resistance, field, and ethics before recommending structure.
5. It should build the business argument before selecting narrative frameworks.
6. It should choose narrative based on task, evidence, audience resistance, and field.
7. It should create slide plans only after the logic is stable.
8. It should produce action-title slides, evidence maps, risks, and missing-proof notes.
9. It should sometimes recommend a memo, read-ahead, appendix, or pre-wire conversation instead of only a deck.
10. It should treat famous cases as calibration references, not templates to copy.
