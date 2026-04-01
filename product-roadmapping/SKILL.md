---
name: product-roadmapping
description: 'Create and manage product roadmaps using prioritization frameworks like RICE, MoSCoW, and Value vs. Effort. Use for: strategic planning, feature prioritization, stakeholder alignment, release planning, communicating product vision, balancing short-term and long-term goals, managing resources effectively, and ensuring development efforts focus on highest-value initiatives.'
---

# Product Roadmapping

Create strategic product roadmaps that align stakeholders, prioritize initiatives by impact, and communicate product vision across the organization.

## Overview

A product roadmap is a strategic communication tool — not a project plan. It visualizes the direction, priorities, and progress of a product over time. Effective roadmaps balance stakeholder needs, resource constraints, and strategic goals while remaining flexible enough to adapt to new information. This skill covers roadmap types, prioritization frameworks, stakeholder communication, and maintenance best practices.

## Roadmap Format Selection Guide

| Format | Best For | Audience | Time Horizon | Flexibility |
|--------|----------|----------|-------------|-------------|
| Now / Next / Later | Agile teams, high uncertainty | Engineering, product team | Rolling (no dates) | Very high |
| Quarterly theme-based | Mid-stage products | Executives, cross-functional | 4–6 quarters | High |
| Timeline with milestones | Enterprise, regulated industries | Executives, board, customers | 12–18 months | Medium |
| Kanban-style | Continuous delivery teams | Engineering team | Continuous | Very high |
| Outcome-based | OKR-driven organizations | All stakeholders | Quarterly aligned | High |
| Feature-based | Sales-driven organizations | Sales, customers | Specific releases | Low |

### Format Decision Guide

- **High uncertainty + internal audience** → Now / Next / Later
- **OKR-driven organization** → Outcome-based
- **Enterprise customers demanding dates** → Timeline with milestones (but with caveats)
- **Continuous deployment** → Kanban-style
- **Board/investor communication** → Quarterly theme-based

## Prioritization Frameworks

### Framework Comparison

| Framework | Best For | Inputs Required | Objectivity | Effort |
|-----------|----------|----------------|-------------|--------|
| RICE | Quantitative ranking | Reach, Impact, Confidence, Effort | High | Medium |
| MoSCoW | Release scoping | Stakeholder input | Medium | Low |
| Value vs. Effort (2×2) | Quick visual prioritization | Rough estimates | Low-Medium | Low |
| WSJF (Weighted Shortest Job First) | SAFe/Lean environments | CoD, Job Duration | High | Medium |
| Kano Model | Customer satisfaction optimization | User research data | Medium | High |
| ICE | Fast scoring | Impact, Confidence, Ease | Medium | Low |
| Opportunity Scoring | Jobs-to-be-Done alignment | Customer survey data | High | High |

### RICE Scoring (Most Common)

**Score = (Reach × Impact × Confidence) / Effort**

| Parameter | Definition | Scale |
|-----------|-----------|-------|
| Reach | # of users/accounts affected per quarter | Actual number |
| Impact | Effect on individual user (goal achievement) | 3 = massive, 2 = high, 1 = medium, 0.5 = low, 0.25 = minimal |
| Confidence | How sure you are about estimates | 100% = high, 80% = medium, 50% = low |
| Effort | Person-months required | Actual estimate |

### MoSCoW for Release Scoping

| Category | Definition | Rule of Thumb |
|----------|-----------|---------------|
| **Must** | Release fails without it | ≤60% of capacity |
| **Should** | Important but workaround exists | 20% of capacity |
| **Could** | Nice to have, easy wins | 20% of capacity |
| **Won't** | Explicitly out of scope (this time) | Document for future |

## Stakeholder Communication

### Audience-Specific Roadmap Views

| Audience | What They Need | Format | Update Frequency | Detail Level |
|----------|---------------|--------|------------------|--------------|
| Board/Investors | Strategic direction, market positioning | High-level themes | Quarterly | Low |
| Executives (C-suite) | Business outcomes, resource allocation | Quarterly themes + OKRs | Monthly | Medium |
| Sales/CS | Upcoming features for customer conversations | Timeline with features | Bi-weekly | High |
| Engineering | Technical scope, dependencies, sequencing | Sprint-level details | Weekly | Very high |
| Customers | Directional vision (no promises) | Now/Next/Later | Quarterly | Low |

### Handling Roadmap Requests

| Request Type | Response Framework |
|-------------|-------------------|
| "Can you add feature X?" | "Thank you — let me run it through our prioritization framework and share where it lands." |
| "When will Y ship?" | "We're targeting [quarter/timeframe]. I'll share updates as we get closer." |
| "Customer Z needs this by [date]" | "Let me understand the business impact and evaluate against current priorities." |
| "Why isn't my team's request on the roadmap?" | "Here's how we scored it: [RICE score]. Here's what it would displace." |
| "The roadmap needs to change" | "What new information do we have? Let's re-evaluate using our framework." |

## Roadmap Building Process

| Step | Action | Inputs | Output | Duration |
|------|--------|--------|--------|----------|
| 1. Gather inputs | Collect feedback, data, strategy docs | Customer feedback, analytics, strategy | Prioritized input list | 1–2 weeks |
| 2. Define themes | Group inputs into strategic themes | Company OKRs, product vision | 3–5 quarterly themes | 1 day |
| 3. Score initiatives | Apply RICE/chosen framework to each item | Initiative details, estimates | Ranked list | 1–2 days |
| 4. Capacity check | Validate against available resources | Team capacity, dependencies | Feasible scope | 1 day |
| 5. Build roadmap | Create visual roadmap in chosen format | Scored list + capacity | Draft roadmap | 1 day |
| 6. Review & align | Share with stakeholders, gather feedback | Stakeholder input | Aligned roadmap | 1 week |
| 7. Publish & communicate | Share appropriate views with each audience | Final roadmap | Published roadmap | 1 day |

## Roadmap Tools

| Tool | Best For | Key Feature | Price |
|------|----------|-------------|-------|
| Productboard | Customer-driven product teams | Customer feedback portal | $$$ |
| Aha! | Enterprise product management | Strategy → execution linkage | $$$ |
| Linear | Engineering-focused teams | Roadmap ↔ issue tracker | $$ |
| Jira Product Discovery | Atlassian ecosystem teams | Jira integration | $$ |
| Notion | Flexible, custom workflows | Template flexibility | $ |
| Airfocus | Prioritization-focused | Built-in scoring frameworks | $$ |

## Common Anti-Patterns

| Anti-Pattern | Problem | Fix |
|-------------|---------|-----|
| Date-driven roadmap | Creates false precision, erodes trust | Use timeframes (Now/Next/Later) or quarters |
| Feature factory | Shipping features without measuring outcomes | Tie every item to an OKR or metric |
| Stakeholder-driven | Loudest voice wins, no framework | Implement scoring; make tradeoffs visible |
| Set-and-forget | Roadmap becomes outdated artifact | Review and update monthly |
| Over-committed | >100% capacity allocated | Always leave 20% buffer for unplanned work |

## Best Practices

1. **Roadmaps are about outcomes, not outputs** — Frame items as problems to solve, not features to build
2. **Maintain multiple views** — Same roadmap, different detail levels for different audiences
3. **Review monthly, rebuild quarterly** — Roadmaps should evolve with new information
4. **Never commit to dates you can't control** — Use timeframes and confidence levels instead
5. **Make tradeoffs explicit** — "If we add X, we delay Y" helps stakeholders make informed decisions
6. **Keep a parking lot** — Explicitly capture and revisit deferred items so stakeholders feel heard

## Using the Reference Files

### When to Read Each Reference

**`/references/prioritization-frameworks.md`** — Read when applying RICE, MoSCoW, WSJF, or other scoring methods to rank features and initiatives for the roadmap.

**`/references/roadmap-creation-management.md`** — Read when building a roadmap from scratch, choosing a format, selecting tools, or establishing a roadmap review cadence.

**`/references/stakeholder-communication.md`** — Read when preparing roadmap presentations, handling pushback, managing expectations, or creating audience-specific roadmap views.
