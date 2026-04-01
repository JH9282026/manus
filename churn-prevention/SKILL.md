---
name: "churn-prevention"
description: "Implement predictive churn prevention using analytics, early warning systems, and intervention playbooks. Use for: identifying at-risk customers, predicting churn probability, triggering proactive interventions, analyzing churn patterns, automating retention workflows, and reducing voluntary and involuntary churn."
---

# Churn Prevention

Build predictive churn models and automated intervention systems that identify at-risk customers early and trigger targeted retention actions before cancellation.

## Overview

Churn prevention combines predictive analytics, early warning signals, and systematic intervention playbooks to reduce customer attrition. In 2026, ML models can predict churn 60–90 days in advance with 80%+ accuracy, giving teams time to intervene. This skill covers the full prevention pipeline from signal identification through automated response.

## Churn Type Classification

| Churn Type | Definition | Typical Causes | Prevention Approach |
|-----------|-----------|----------------|--------------------|
| Voluntary — Active | Customer deliberately cancels | Poor fit, competitor switch, budget cuts | Value reinforcement, save offers |
| Voluntary — Passive | Customer drifts away (doesn't renew) | Low engagement, forgotten product | Re-engagement campaigns, usage nudges |
| Involuntary | Payment failure, card expiry | Failed billing, expired payment method | Dunning automation, payment recovery |
| Contractual | Customer doesn't renew at term end | Unmet expectations, stakeholder change | QBR program, multi-threading |
| Downgrade | Customer reduces spend (revenue churn) | Partial value realization, budget pressure | Value expansion, ROI demonstration |

## Early Warning Signal Matrix

| Signal | Risk Level | Detection Method | Response Time | Intervention |
|--------|-----------|-----------------|---------------|-------------|
| Login frequency drops >50% | High | Product analytics | 48 hours | CSM outreach + usage review |
| Support tickets spike (3x normal) | High | Ticketing system | 24 hours | Escalation + root cause analysis |
| Executive sponsor leaves | Critical | CRM monitoring / LinkedIn | Same day | New champion identification |
| NPS drops below 6 | High | Survey automation | 48 hours | Detractor recovery playbook |
| Feature usage flatlines | Medium | Product analytics | 1 week | Adoption workshop |
| Invoice dispute filed | High | Billing system | 24 hours | Finance + CSM joint call |
| Competitor evaluation detected | Critical | Intent data / sales intel | Same day | Executive engagement + value recap |
| No login for 14+ days | Medium | Product analytics | 3 days | Automated re-engagement email |
| Contract utilization <40% | Medium | License tracking | 1 week | Rightsizing conversation + training |

## Predictive Churn Model Architecture

### Feature Engineering

| Feature Category | Example Features | Predictive Power |
|-----------------|------------------|------------------|
| Usage metrics | DAU/MAU ratio, session duration, feature count | Very high |
| Engagement trends | Week-over-week usage delta, login streak | High |
| Support interactions | Ticket volume, sentiment trend, resolution time | High |
| Financial signals | Payment delays, discount requests, downsell inquiries | Medium-high |
| Relationship health | NPS, CSAT, executive engagement frequency | Medium |
| External factors | Company layoffs, M&A activity, competitor funding | Medium |
| Contractual | Time to renewal, contract length, multi-year vs. annual | Medium |

### Model Selection Guide

| Model Type | Accuracy | Interpretability | Best For |
|-----------|----------|-------------------|----------|
| Logistic Regression | Good (70–80%) | High | Baseline, stakeholder buy-in |
| Random Forest | Very good (80–85%) | Medium | Feature importance analysis |
| XGBoost/LightGBM | Excellent (85–90%) | Low-medium | Production prediction |
| Survival Analysis | Good for timing | High | Predicting WHEN churn happens |
| Deep Learning (LSTM) | Excellent (85–92%) | Low | Large datasets with sequential patterns |

## Intervention Playbooks

### Tier 1: Automated (Score 60–70)
| Step | Timing | Action | Channel |
|------|--------|--------|---------|
| 1 | Day 0 | Trigger usage nudge email | Email |
| 2 | Day 3 | In-app notification with feature suggestion | In-app |
| 3 | Day 7 | Personalized video from CSM (automated) | Email |
| 4 | Day 14 | Escalate to Tier 2 if no improvement | Internal |

### Tier 2: CSM-Led (Score 40–59)
| Step | Timing | Action | Owner |
|------|--------|--------|-------|
| 1 | Day 0 | CSM calls customer, conducts discovery | CSM |
| 2 | Day 1 | Create remediation plan with specific milestones | CSM |
| 3 | Day 7 | Follow-up check on remediation progress | CSM |
| 4 | Day 14 | Re-score; if improved, move to monitoring | CSM |
| 5 | Day 14 | If not improved, escalate to Tier 3 | CSM → Manager |

### Tier 3: Executive (Score <40)
| Step | Timing | Action | Owner |
|------|--------|--------|-------|
| 1 | Day 0 | VP/C-level reaches out to customer executive | Executive |
| 2 | Day 2 | Joint recovery plan with SLA commitments | CS + Product |
| 3 | Day 7 | Daily monitoring of health score signals | CS Ops |
| 4 | Day 14 | Executive check-in on progress | Executive |
| 5 | Day 30 | Save/loss decision and post-mortem | Leadership |

## Involuntary Churn: Dunning Automation

| Retry Attempt | Timing | Action | Recovery Rate |
|--------------|--------|--------|---------------|
| 1st retry | Day 1 after failure | Silent retry (different time) | 30–40% |
| 2nd retry | Day 3 | Retry + email notification | 15–20% |
| 3rd retry | Day 5 | Retry + SMS/push notification | 10–15% |
| 4th retry | Day 7 | Email with update payment link | 8–12% |
| Final notice | Day 10 | "Account will be paused" warning | 5–10% |
| Account paused | Day 14 | Pause (not cancel) + recovery email | 3–5% |

**Total involuntary churn recovery with proper dunning: 60–75%**

## Churn Analysis Metrics

| Metric | Formula | Benchmark |
|--------|---------|----------|
| Monthly churn rate | Customers lost / Starting customers | <2% (SaaS) |
| Annual churn rate | 1 − (1 − monthly rate)^12 | <15% |
| Revenue churn | MRR lost / Starting MRR | <1% monthly |
| Net revenue retention | (Start MRR + Expansion − Churn) / Start MRR | >110% |
| Save rate | Customers saved / Customers flagged at-risk | >30% |
| Time to churn | Average days from first risk signal to cancellation | Monitor trend |
| Churn reason distribution | % by reason category | Use for prioritization |

## Best Practices

1. **Predict, don't react** — Build models that flag risk 60+ days before renewal, not after cancellation request
2. **Segment interventions by value** — High-ACV accounts get white-glove treatment; low-ACV gets automated sequences
3. **Fix involuntary churn first** — It's the easiest win with the highest ROI (dunning automation recovers 60–75%)
4. **Conduct churn post-mortems** — Every lost customer should generate learnings; categorize and trend reasons
5. **Monitor leading indicators, not lagging** — Usage decline predicts churn; churn rate is the result
6. **Close the product feedback loop** — Share churn reasons with product team monthly to fix root causes

## Using the Reference Files

### When to Read Each Reference

**`/references/predictive-analytics-models.md`** — Read when building or tuning churn prediction models, selecting features, or evaluating model performance.

**`/references/early-warning-systems.md`** — Read when configuring alert thresholds, integrating data sources for signal detection, or building real-time monitoring dashboards.

**`/references/intervention-playbooks.md`** — Read when designing tiered intervention workflows, creating save offer frameworks, or training CSMs on at-risk customer engagement.

**`/references/churn-analysis-techniques.md`** — Read when conducting churn post-mortems, building cohort analyses, or segmenting churn by reason, segment, or time period.

**`/references/retention-automation.md`** — Read when implementing automated retention workflows, dunning sequences, or re-engagement campaigns.
