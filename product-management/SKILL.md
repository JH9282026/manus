---
name: product-management
description: 'Lead product development using frameworks like Lean Startup, Agile, Design Thinking, and Jobs-to-be-Done. Use for: defining product strategy, prioritizing features, conducting user research, creating product roadmaps, managing stakeholders, making data-driven decisions, balancing customer needs with business goals, and delivering successful products from ideation to launch.'
---

# Product Management

Lead product development from strategy to execution using proven frameworks for discovery, prioritization, and delivery to build products customers love and businesses need.

## Overview

Product management sits at the intersection of user desirability, business viability, and technical feasibility. This skill provides the frameworks, processes, and decision-making tools a product manager needs to define strategy, discover customer needs, prioritize ruthlessly, and ship products that deliver measurable outcomes.

## Product Management Framework Selection

| Framework | Best For | Phase | Core Idea | When to Use |
|-----------|----------|-------|-----------|-------------|
| Lean Startup | New products, high uncertainty | Discovery | Build → Measure → Learn | 0-to-1 products, validating assumptions |
| Design Thinking | User experience problems | Discovery | Empathize → Define → Ideate → Prototype → Test | Complex user problems, innovation |
| Jobs-to-be-Done | Understanding customer motivation | Discovery | Customers "hire" products for a job | Positioning, feature prioritization |
| Dual Track Agile | Balanced discovery + delivery | Discovery + Delivery | Parallel discovery and delivery tracks | Growth-stage products |
| Shape Up | 6-week project scoping | Delivery | Shape → Bet → Build | Basecamp-style, small teams |
| SAFe | Enterprise-scale Agile | Delivery | Lean-Agile at scale | Large organizations (50+ developers) |
| OKR Framework | Goal alignment | Strategy | Objectives + Key Results | Aligning teams to outcomes |

## Product Strategy Canvas

| Element | Question to Answer | Output |
|---------|-------------------|--------|
| Vision | Where are we going in 3–5 years? | Vision statement |
| Mission | Why does this product exist? | Mission statement |
| Target Customer | Who are we building for (and who not)? | Persona(s) + anti-persona(s) |
| Customer Problem | What pain are we solving? | Problem statement(s) |
| Value Proposition | Why choose us over alternatives? | Positioning statement |
| Key Differentiators | What makes us defensible? | Competitive moat analysis |
| Business Model | How do we make money? | Revenue model + unit economics |
| Key Metrics | How do we measure success? | North Star metric + supporting KPIs |
| Strategic Bets | What are we betting on this quarter? | 3–5 strategic themes |

## Discovery Process

### User Research Methods

| Method | Best For | Sample Size | Duration | Cost |
|--------|----------|-------------|----------|------|
| User interviews | Deep understanding of needs/pain | 5–15 users | 30–60 min each | Low |
| Surveys | Quantitative validation | 100–1,000+ | 5–10 min each | Low |
| Usability testing | Evaluating specific flows | 5–8 users | 30–60 min each | Medium |
| A/B testing | Validating design/copy decisions | 1,000+ per variant | 1–4 weeks | Medium |
| Analytics review | Understanding behavior patterns | All users | Ongoing | Low |
| Diary studies | Longitudinal behavior tracking | 10–20 users | 1–4 weeks | Medium |
| Card sorting | Information architecture | 15–30 users | 20–30 min each | Low |
| Competitive analysis | Market positioning | 5–10 competitors | 1–2 days | Low |

### Hypothesis-Driven Development

**Template:** "We believe that [doing X] for [persona Y] will achieve [outcome Z]. We'll know we're right when [measurable signal]."

| Hypothesis Type | Example | Validation Method |
|----------------|---------|-------------------|
| Problem hypothesis | "SMB owners spend >5hrs/week on invoicing" | User interviews + surveys |
| Solution hypothesis | "Automated invoicing will reduce time by 80%" | Prototype testing |
| Business hypothesis | "Users will pay $49/mo for this" | Pricing page test, fake door |
| Growth hypothesis | "Users will invite colleagues via sharing" | Feature flag + analytics |

## Prioritization Decision Tree

1. **Is it aligned with our current strategy/OKRs?** → No → Parking lot
2. **Does it solve a validated customer problem?** → No → Needs discovery
3. **Score with RICE:**
   - Reach: How many users per quarter?
   - Impact: How much does it move the metric? (3/2/1/0.5/0.25)
   - Confidence: How sure are we? (100/80/50%)
   - Effort: Person-weeks to build?
4. **Compare score against other initiatives** → Rank
5. **Check dependencies and sequencing** → Adjust order if blocked
6. **Capacity check** → Does it fit in the quarter?

## Product Metrics Framework

### North Star Metric by Product Type

| Product Type | North Star Metric | Supporting Metrics |
|-------------|-------------------|-------------------|
| SaaS/B2B | Weekly Active Users or Net Revenue Retention | Feature adoption, NPS, expansion revenue |
| Marketplace | Gross Merchandise Value (GMV) | Liquidity, take rate, repeat purchase |
| Social/Consumer | Daily Active Users (DAU) | Time spent, content created, retention |
| E-commerce | Revenue per Visitor | Conversion rate, AOV, repeat purchase rate |
| Content/Media | Engaged Time | Sessions, pages/session, subscribers |
| Fintech | Assets Under Management or Transactions | Activation, deposit frequency, NPS |

### AARRR (Pirate Metrics) Framework

| Stage | Metric | Example KPI | Benchmark |
|-------|--------|------------|----------|
| **A**cquisition | How do users find us? | Signup rate, CAC | Varies by channel |
| **A**ctivation | Do they have a great first experience? | Onboarding completion, time-to-value | >60% day-1 retention |
| **R**etention | Do they come back? | D7/D30/D90 retention | D30: 20–40% (consumer), 80%+ (SaaS) |
| **R**evenue | Do they pay? | Conversion rate, ARPU, LTV | LTV > 3x CAC |
| **R**eferral | Do they tell others? | Viral coefficient, NPS | NPS >50, k-factor >0.5 |

## Stakeholder Management

### RACI Matrix for Product Decisions

| Decision | Product | Engineering | Design | Data | Sales | Exec |
|----------|---------|-------------|--------|------|-------|------|
| Roadmap priorities | **A/R** | C | C | C | C | I |
| Feature scope | **A/R** | R | R | C | I | I |
| Technical approach | C | **A/R** | I | C | — | I |
| UX design | C | C | **A/R** | C | — | I |
| Pricing | **R** | — | — | C | C | **A** |
| Go-to-market | C | I | C | C | **A/R** | I |

**R** = Responsible | **A** = Accountable | **C** = Consulted | **I** = Informed

## Launch Checklist

| Phase | Tasks | Owner |
|-------|-------|-------|
| Pre-launch (2 weeks) | Feature freeze, QA complete, docs written | Engineering + PM |
| Pre-launch (1 week) | Sales enablement, support training, marketing assets | GTM team |
| Launch day | Feature flag rollout (% ramp), monitoring dashboards live | Engineering + PM |
| Post-launch (week 1) | Daily metrics review, bug triage, customer feedback | PM + Support |
| Post-launch (month 1) | Impact analysis, retrospective, iterate or pivot | PM + Data |

## Best Practices

1. **Fall in love with the problem, not the solution** — Always validate the problem before investing in a solution
2. **Prioritize learning speed** — The faster you learn, the faster you win; optimize for cycle time
3. **Say no more than yes** — The best product managers are defined by what they choose NOT to build
4. **Write it down** — PRDs, one-pagers, strategy docs force clarity and create alignment artifacts
5. **Measure outcomes, not output** — Features shipped means nothing if user behavior doesn't change
6. **Communicate 5x more than you think necessary** — Stakeholders forget; repeat the strategy constantly

## Using the Reference Files

### When to Read Each Reference

**`/references/product-frameworks-methodologies.md`** — Read when selecting a product development methodology, understanding Lean Startup, JTBD, or Dual Track Agile, or training a team on product practices.

**`/references/strategic-planning-execution.md`** — Read when defining product strategy, writing vision documents, setting OKRs, or building the product strategy canvas.

**`/references/stakeholder-user-research.md`** — Read when planning user research, conducting interviews, managing stakeholder relationships, or building a RACI matrix.
