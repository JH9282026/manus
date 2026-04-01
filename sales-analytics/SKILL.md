---
name: "sales-analytics"
description: "Build comprehensive sales analytics using KPIs, dashboards, forecasting models, and AI-powered insights. Use for: tracking sales performance, building executive dashboards, improving forecast accuracy, analyzing pipeline health, identifying trends, optimizing sales processes, and making data-driven decisions."
---

# Sales Analytics

Build data-driven sales operations with comprehensive KPI frameworks, pipeline analytics, forecasting models, and executive dashboards that drive performance and predictability.

## Overview

Sales analytics transforms raw CRM data into actionable insights that improve win rates, forecast accuracy, and rep productivity. This skill covers the full analytics stack — from defining the right KPIs through building predictive forecasting models and designing executive dashboards that drive decisions.

## KPI Framework by Role

| KPI | SDR/BDR | AE | Sales Manager | VP Sales |
|-----|---------|-----|---------------|----------|
| Activities (calls, emails) | ✅ Primary | — | ✅ Team aggregate | — |
| Meetings booked | ✅ Primary | — | ✅ Team aggregate | — |
| Pipeline generated ($) | ✅ Primary | ✅ Self-sourced | ✅ Team total | ✅ Company total |
| Win rate | — | ✅ Primary | ✅ Team average | ✅ Company average |
| Avg deal size | — | ✅ Primary | ✅ Team average | ✅ Segment view |
| Sales cycle length | — | ✅ Primary | ✅ Team average | ✅ Trend |
| Quota attainment | ✅ Meetings | ✅ Revenue | ✅ Team % | ✅ Company % |
| Forecast accuracy | — | ✅ Own deals | ✅ Team forecast | ✅ Company forecast |
| Revenue (closed-won) | — | ✅ Primary | ✅ Team total | ✅ Company total |
| CAC / LTV ratio | — | — | — | ✅ Strategic |

## Pipeline Health Analysis

### Pipeline Coverage Model

| Stage | Probability | Weighted Value | Required Coverage |
|-------|------------|----------------|-------------------|
| Discovery | 10–20% | Deal × 0.15 | 5–6x quota |
| Qualification | 20–40% | Deal × 0.30 | 3–4x quota |
| Solution/Demo | 40–60% | Deal × 0.50 | 2–2.5x quota |
| Proposal | 60–80% | Deal × 0.70 | 1.5–2x quota |
| Negotiation | 80–95% | Deal × 0.85 | 1.2–1.5x quota |
| Closed-Won | 100% | Deal × 1.00 | 1x quota |

**Healthy pipeline rule:** Total weighted pipeline should be **3–4x** the remaining quota for the period.

### Pipeline Velocity Formula

**Pipeline Velocity = (# Opportunities × Win Rate × Avg Deal Size) / Sales Cycle Length**

Improving any single variable by 10% increases velocity by 10%. Focus on the weakest variable first.

| Variable | How to Improve | Impact |
|----------|---------------|--------|
| # Opportunities | Better prospecting, more channels | Linear |
| Win Rate | Better qualification, sales methodology | Highest leverage |
| Avg Deal Size | Multi-threading, solution selling, upsell | Compounding |
| Sales Cycle Length | Better process, champion access, urgency | Time-value |

## Forecasting Methodologies

| Method | Accuracy | Effort | Best For |
|--------|----------|--------|----------|
| Rep judgment (bottom-up) | Low (50–60%) | Low | Early-stage companies |
| Stage-weighted pipeline | Medium (65–75%) | Low | Standard forecasting |
| Historical conversion rates | Medium (70–80%) | Medium | Stable businesses |
| Multi-variable regression | High (80–85%) | High | Data-rich organizations |
| AI/ML predictive | Very high (85–95%) | Medium (once built) | Enterprise, 12+ months data |
| Blended (AI + judgment) | Highest (88–95%) | Medium | Best practice for 2026 |

### Forecast Category Framework

| Category | Definition | Confidence | Count Toward Forecast |
|----------|-----------|------------|----------------------|
| Closed | Signed contract, payment received | 100% | Full amount |
| Commit | Verbal/written confirmation, in legal | 90–95% | 95% |
| Best Case | Strong signals, decision pending | 60–75% | 50% |
| Pipeline | Qualified but early stage | 20–40% | 0% (upside only) |
| Omitted | Excluded from forecast | 0% | 0% |

## Dashboard Design Framework

### Executive Dashboard (VP/CRO)
| Widget | Visualization | Refresh |
|--------|--------------|--------|
| Revenue vs. quota (MTD/QTD) | Progress bar + trend | Daily |
| Forecast vs. target | Waterfall chart | Weekly |
| Pipeline coverage by segment | Stacked bar | Daily |
| Win/loss rate trend | Line chart (12-week) | Weekly |
| Top 10 deals at risk | Table with health score | Real-time |
| New pipeline created | Bar chart (weekly) | Daily |

### Manager Dashboard
| Widget | Visualization | Refresh |
|--------|--------------|--------|
| Rep quota attainment | Leaderboard | Daily |
| Activity metrics by rep | Heat map | Daily |
| Pipeline by stage by rep | Funnel chart | Daily |
| Deal aging (stuck deals) | Scatter plot | Daily |
| Win rate by lead source | Bar chart | Weekly |
| Forecast accuracy trend | Line chart | Monthly |

## Conversion & Funnel Analysis

| Funnel Stage | Benchmark Conversion | Red Flag Below |
|-------------|---------------------|----------------|
| Lead → MQL | 15–30% | <10% |
| MQL → SQL | 30–50% | <20% |
| SQL → Opportunity | 50–70% | <40% |
| Opportunity → Proposal | 40–60% | <30% |
| Proposal → Closed Won | 20–35% | <15% |
| **Lead → Closed Won** | **1–5%** | **<0.5%** |

## Best Practices

1. **Standardize data entry** — Analytics are only as good as the CRM data; enforce required fields and validation rules
2. **Measure what you can act on** — Every metric should have a clear "so what" and owner
3. **Separate leading from lagging indicators** — Activities and pipeline are leading; revenue is lagging
4. **Review metrics at the right cadence** — Daily (activities), weekly (pipeline), monthly (forecasts), quarterly (strategy)
5. **Triangulate forecasts** — Use at least two independent methods and reconcile discrepancies
6. **Benchmark externally** — Compare metrics against industry data to identify improvement opportunities

## Using the Reference Files

### When to Read Each Reference

**`/references/kpi-framework-guide.md`** — Read when defining or refining sales KPIs, building scorecards, or aligning metrics across sales roles.

**`/references/dashboard-design-templates.md`** — Read when building sales dashboards in Salesforce, Looker, Tableau, or other BI tools, including layout templates and query patterns.

**`/references/forecasting-methodologies.md`** — Read when implementing or improving sales forecasting, selecting models, or training managers on forecast discipline.

**`/references/pipeline-analytics.md`** — Read when analyzing pipeline health, diagnosing conversion bottlenecks, or building pipeline coverage reports.

**`/references/ai-powered-insights.md`** — Read when implementing AI/ML-based forecasting, anomaly detection, or automated insight generation for sales data.
