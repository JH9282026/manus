---
name: feature-prioritization
description: 'Prioritize product features using frameworks like RICE, MoSCoW, Kano Model, ICE, and Opportunity Scoring. Use for: evaluating feature requests, making objective prioritization decisions, balancing stakeholder needs, maximizing ROI, understanding customer satisfaction drivers, managing product backlogs, and ensuring development resources focus on highest-impact work.'
---

# Feature Prioritization

Make objective, data-driven feature prioritization decisions using proven frameworks that balance user value, business impact, and development effort.

## Overview

Feature prioritization is the most consequential activity in product management — it determines what gets built, what gets deferred, and what never ships. This skill provides a toolkit of frameworks for different prioritization contexts, scoring methodologies, stakeholder alignment techniques, and backlog management practices.

## Framework Selection Guide

| Framework | Best For | Objectivity | Effort to Apply | Stakeholder Buy-In | Data Required |
|-----------|----------|-------------|-----------------|-------------------|---------------|
| RICE | Quantitative ranking of backlog | Very high | Medium | High (numbers-based) | Reach + effort estimates |
| ICE | Quick scoring, early-stage | Medium | Low | Medium | Rough estimates |
| MoSCoW | Release scoping, fixed deadline | Medium | Low | High (collaborative) | Stakeholder input |
| Kano Model | Customer satisfaction optimization | High | High | Medium | User survey data |
| Value vs. Effort (2×2) | Quick visual sort | Low | Very low | High (intuitive) | Gut + discussion |
| WSJF | SAFe / Lean environments | High | Medium | High (economic) | Cost of Delay data |
| Opportunity Scoring | JTBD-aligned prioritization | High | High | High | Customer survey data |
| Story Mapping | User journey-based priority | Medium | Medium | High (visual) | User research |

## RICE Framework (Deep Dive)

### Scoring Formula
**RICE Score = (Reach × Impact × Confidence) / Effort**

| Parameter | What It Measures | How to Estimate | Scale |
|-----------|-----------------|-----------------|-------|
| Reach | Users/accounts affected per quarter | Analytics, funnel data, segment size | Actual number (e.g., 5,000) |
| Impact | Effect on individual user | Research, prototypes, comparable features | 3=massive, 2=high, 1=medium, 0.5=low, 0.25=minimal |
| Confidence | Certainty in your estimates | Evidence quality assessment | 100%=high, 80%=medium, 50%=low |
| Effort | Person-months to implement | Engineering estimates, t-shirt sizing | Actual number (e.g., 2.5) |

### RICE Scoring Example

| Feature | Reach (Q) | Impact | Confidence | Effort (PM) | RICE Score | Rank |
|---------|----------|--------|-----------|-------------|-----------|------|
| In-app onboarding wizard | 8,000 | 2 | 80% | 3 | 4,267 | 1 |
| Bulk CSV export | 2,000 | 1 | 100% | 0.5 | 4,000 | 2 |
| Dark mode | 10,000 | 0.5 | 100% | 2 | 2,500 | 3 |
| AI writing assistant | 5,000 | 3 | 50% | 8 | 938 | 4 |
| Custom dashboards | 1,000 | 2 | 80% | 6 | 267 | 5 |

## Kano Model (Deep Dive)

### Category Definitions

| Category | User Expectation | When Present | When Absent | Strategic Action |
|----------|-----------------|-------------|-------------|------------------|
| Must-Be (Basic) | Expected, taken for granted | Neutral satisfaction | High dissatisfaction | Must implement — non-negotiable |
| Performance (Linear) | More is better | Proportional satisfaction | Proportional dissatisfaction | Invest proportionally to competition |
| Attractive (Delighter) | Not expected | High delight | No impact | Strategic differentiator — invest selectively |
| Indifferent | Don't care either way | No impact | No impact | Don't build — save resources |
| Reverse | Actively unwanted | Dissatisfaction | Satisfaction | Avoid or make optional |

### Running a Kano Survey

1. **For each feature, ask two questions:**
   - Functional: "If [feature] were available, how would you feel?" (Like, Expect, Neutral, Tolerate, Dislike)
   - Dysfunctional: "If [feature] were NOT available, how would you feel?" (Same scale)

2. **Map responses to categories using the evaluation table:**

| | Like (Functional) | Expect | Neutral | Tolerate | Dislike |
|---|---|---|---|---|---|
| **Like (Dysfunctional)** | Questionable | Attractive | Attractive | Attractive | Performance |
| **Expect** | Reverse | Indifferent | Indifferent | Indifferent | Must-Be |
| **Neutral** | Reverse | Indifferent | Indifferent | Indifferent | Must-Be |
| **Tolerate** | Reverse | Indifferent | Indifferent | Indifferent | Must-Be |
| **Dislike** | Reverse | Reverse | Reverse | Reverse | Questionable |

3. **Aggregate across respondents** — The majority classification wins for each feature.

## Opportunity Scoring (Jobs-to-be-Done)

### Formula
**Opportunity Score = Importance + max(Importance − Satisfaction, 0)**

Survey users on 1–10 scale: "How important is [outcome]?" and "How satisfied are you with current solutions?"

| Score Range | Interpretation | Action |
|------------|----------------|--------|
| >15 | Underserved — high opportunity | Prioritize immediately |
| 12–15 | Moderately underserved | Strong candidate |
| 10–12 | Appropriately served | Maintain, don't over-invest |
| <10 | Overserved | De-prioritize or remove |

## Stakeholder Alignment Techniques

| Technique | When to Use | How It Works |
|-----------|-------------|-------------|
| Buy-a-feature | Multiple stakeholders with competing needs | Give each stakeholder fake money; they "buy" features they want |
| Dot voting | Quick group consensus | 3 dots per person, place on preferred items |
| Stack ranking | Forced tradeoffs | Each stakeholder ranks all items; average ranks |
| Priority poker | Agile teams | Like planning poker but for priority (1=low, 5=critical) |
| Impact mapping | Connecting features to goals | Goal → Actor → Impact → Deliverable |

## Backlog Management Best Practices

| Practice | Description | Frequency |
|----------|-------------|----------|
| Grooming / Refinement | Review and re-score top 20–30 items | Weekly |
| Pruning | Archive items untouched for 6+ months | Monthly |
| Re-scoring | Update RICE scores with new data | Quarterly |
| Stakeholder sync | Review priorities with key stakeholders | Bi-weekly |
| Data refresh | Update reach/impact with latest analytics | Monthly |
| Theme alignment | Ensure backlog items map to strategic themes | Quarterly |

## Common Prioritization Pitfalls

| Pitfall | Description | Fix |
|---------|-------------|-----|
| HiPPO effect | Highest Paid Person's Opinion wins | Use framework scores; make tradeoffs explicit |
| Recency bias | Last customer request gets top priority | Aggregate signals across customers before scoring |
| Sunk cost fallacy | "We've already started, so let's finish" | Evaluate remaining effort vs. remaining value |
| Feature parity trap | "Competitor has it, so we need it" | Validate with YOUR users; differentiate instead |
| Squeaky wheel | Loudest stakeholder gets their way | Weight by data, not volume of requests |
| Analysis paralysis | Over-scoring, never deciding | Set a time box; "good enough" scoring is fine |

## Best Practices

1. **Use frameworks as guides, not gospels** — Scoring creates informed discussion; the score is input, not the decision
2. **Combine multiple frameworks** — Use RICE for the backlog, Kano for customer research, MoSCoW for release scoping
3. **Score collaboratively** — Having PM, engineering, and design score together reduces bias
4. **Document your reasoning** — Future-you will forget why something was prioritized; write it down
5. **Re-prioritize regularly** — Scores change as you learn; stale priorities lead to building the wrong things
6. **Make tradeoffs visible** — "Adding X means dropping Y" clarifies the real cost of decisions

## Using the Reference Files

### When to Read Each Reference

**`/references/prioritization-frameworks-comparison.md`** — Read when selecting which framework to use, understanding the nuances of RICE vs. ICE vs. WSJF, or teaching your team about prioritization approaches.

**`/references/implementation-best-practices.md`** — Read when setting up a prioritization process for the first time, building scoring templates, or integrating prioritization into existing Agile workflows.

**`/references/stakeholder-alignment.md`** — Read when navigating conflicting stakeholder priorities, running alignment workshops, or communicating prioritization decisions to leadership.
