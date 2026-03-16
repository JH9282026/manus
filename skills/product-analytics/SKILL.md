---
name: product-analytics
description: "Implement product analytics frameworks, define metrics and KPIs, select and configure analytics platforms, and build data-driven product strategies. Use for: measuring product performance, tracking user behavior, analyzing funnels and retention, implementing event tracking, choosing analytics tools (Mixpanel, Amplitude, etc.), defining north star metrics, building dashboards, and optimizing product-market fit through quantitative insights."
---

# Product Analytics

Implement comprehensive product analytics systems to measure user behavior, track key metrics, and drive data-informed product decisions.

## Overview

Product analytics transforms user interactions into actionable insights by tracking events, analyzing patterns, and measuring outcomes. This skill covers framework selection (AARRR, HEART), metric definition, platform implementation, and analysis techniques that connect product usage to business objectives.

## Framework Selection Guide

| Use Case | Framework | Primary Focus | Best For |
|----------|-----------|---------------|----------|
| Growth optimization, conversion tracking | AARRR (Pirate Metrics) | Business outcomes across funnel | Startups, growth teams, revenue focus |
| UX quality, feature success | HEART | User experience and satisfaction | Product-led growth, UX teams |
| Comprehensive view | AARRR + HEART hybrid | Both business and UX metrics | Mature products, enterprise |
| Specific feature analysis | Custom framework | Targeted objectives | Specialized use cases |

## Core Metrics Categories

### Acquisition Metrics
- Traffic sources and channel performance
- Cost per acquisition (CPA) by channel
- Conversion rate from visitor to signup
- Attribution modeling (first-touch, last-touch, multi-touch)

### Activation Metrics
- Time to first value (aha moment)
- Onboarding completion rate
- Feature adoption in first session
- Setup completion percentage

### Retention Metrics
- Day 1, Day 7, Day 30 retention rates
- Cohort retention analysis
- Stickiness ratio (DAU/MAU)
- Resurrection rate (returning churned users)

### Revenue Metrics
- Monthly Recurring Revenue (MRR) and growth rate
- Average Revenue Per User (ARPU)
- Customer Lifetime Value (CLV)
- CLV:CAC ratio (target >3:1)

### Referral Metrics
- Net Promoter Score (NPS)
- Viral coefficient (K-factor)
- Referral conversion rate
- Share/invite actions per user

## Analytics Platform Selection

| Platform | Strengths | Pricing Model | Best For |
|----------|-----------|---------------|----------|
| **Mixpanel** | Funnel analysis, flexible data governance, Metric Trees | Event-based (20M free events/mo) | Startups, B2C, agile teams |
| **Amplitude** | Advanced ML reports, autocapture, experimentation suite | MTU-based (10K free MTUs) | Enterprise, B2B, data-mature orgs |
| **PostHog** | Open-source, session replay, feature flags | Self-hosted or cloud | Privacy-focused, full control |
| **Heap** | Autocapture, retroactive analysis | Event/session-based | Quick setup, non-technical teams |
| **Google Analytics 4** | Free, web analytics, marketing integration | Free (with limits) | Content sites, marketing focus |

## Implementation Process

### 1. Define Measurement Strategy
- Identify north star metric (single metric that predicts success)
- Map user journey and key touchpoints
- Define events taxonomy (naming conventions, properties)
- Establish Goals-Signals-Metrics framework

### 2. Instrument Event Tracking
- Implement SDK or tracking code
- Define event schema with consistent naming
- Add user properties and context
- Set up identity resolution (anonymous → identified users)
- Validate data accuracy in development

### 3. Build Analysis Framework
- Create core dashboards (acquisition, engagement, retention, revenue)
- Set up automated reports and alerts
- Define cohorts for segmentation
- Establish baseline metrics and targets

### 4. Iterate and Optimize
- Review metrics weekly/monthly
- Conduct funnel analysis to identify drop-offs
- Run cohort comparisons to test hypotheses
- Refine tracking based on insights

## Event Tracking Best Practices

**Naming Conventions:**
- Use verb-noun format: `Button Clicked`, `Video Played`, `Purchase Completed`
- Be specific but not overly granular
- Maintain consistent casing (Title Case or snake_case)

**Event Properties:**
- Include contextual data: `video_duration`, `button_location`, `plan_type`
- Capture user properties: `signup_date`, `user_segment`, `subscription_tier`
- Add timestamps and session IDs automatically

**Data Governance:**
- Document all events in a tracking plan
- Use tools like Mixpanel Lexicon or Amplitude Taxonomy
- Regular audits to deprecate unused events
- Version control for schema changes

## Analysis Techniques

### Funnel Analysis
Identify conversion rates and drop-off points across multi-step flows (signup, onboarding, checkout).

### Cohort Analysis
Group users by shared characteristics (signup date, acquisition channel) to compare behavior over time.

### Retention Curves
Visualize how different cohorts retain over days/weeks to identify product-market fit signals.

### Path Analysis
Uncover common user journeys and unexpected navigation patterns.

### Segmentation
Compare metrics across user segments (power users vs. casual, paid vs. free) to identify opportunities.

## Connecting Analytics to Business Outcomes

**North Star Metric Examples:**
- Slack: Messages sent by teams
- Airbnb: Nights booked
- Spotify: Time spent listening
- Notion: Collaborative documents created

**Metric Trees:**
Decompose north star metric into contributing inputs:
```
North Star: Weekly Active Users
├── New User Activation
│   ├── Signup Conversion Rate
│   └── Onboarding Completion Rate
├── Retention
│   ├── Day 7 Retention
│   └── Feature Engagement
└── Resurrection
    └── Win-back Campaign Success
```

## Common Pitfalls to Avoid

- **Vanity metrics:** Focus on actionable metrics, not just impressive numbers
- **Analysis paralysis:** Start with core metrics, expand gradually
- **Poor data quality:** Validate tracking before making decisions
- **Ignoring context:** Consider external factors (seasonality, marketing campaigns)
- **Siloed analytics:** Integrate with qualitative research for complete picture

## Using the Reference Files

### When to Read Each Reference

**`/references/analytics-frameworks.md`** — Read when selecting or implementing AARRR, HEART, or custom frameworks. Covers Goals-Signals-Metrics methodology and framework combinations.

**`/references/metrics-kpis.md`** — Read when defining metrics for SaaS products, calculating retention/churn, or establishing benchmarks. Includes formulas and industry standards.

**`/references/tools-platforms.md`** — Read when evaluating analytics platforms, comparing Mixpanel vs. Amplitude, or planning tool implementation. Covers features, pricing, and integration.

**`/references/implementation-guide.md`** — Read when setting up event tracking, building dashboards, or establishing data governance. Includes code examples and best practices.
