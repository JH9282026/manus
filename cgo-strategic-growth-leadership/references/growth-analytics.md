# Growth Analytics

Metrics, experimentation, and analytics frameworks for growth.

---

## Core Growth Metrics

### Acquisition Metrics

| Metric | Formula | Interpretation |
|--------|---------|---------------|
| CAC | Total Acquisition Cost / New Customers | Efficiency of acquisition |
| CAC by Channel | Channel Cost / Channel Customers | Channel efficiency |
| Conversion Rate | Conversions / Visitors | Funnel efficiency |
| Lead-to-Customer | Customers / Leads | Sales efficiency |
| Cost per Lead | Marketing Spend / Leads | Lead generation efficiency |

### Retention Metrics

| Metric | Formula | Interpretation |
|--------|---------|---------------|
| Churn Rate | Lost Customers / Total Customers | Customer loss rate |
| Retention Rate | 1 - Churn Rate | Customer keeping rate |
| Cohort Retention | % remaining by cohort over time | Retention quality |
| Logo Retention | % of customers retained | Customer count focus |
| Dollar Retention | % of revenue retained | Revenue focus |

### Revenue Metrics

| Metric | Formula | Interpretation |
|--------|---------|---------------|
| MRR | Sum of monthly subscriptions | Recurring revenue |
| ARR | MRR × 12 | Annualized revenue |
| ARPU | Revenue / Users | Revenue per user |
| LTV | ARPU × Gross Margin × Lifetime | Customer value |
| LTV:CAC | LTV / CAC | Unit economics |
| Payback Period | CAC / (ARPU × Gross Margin) | Time to recover CAC |

---

## Attribution Models

### Attribution Types

| Model | Credit Allocation | Best For |
|-------|-------------------|----------|
| First-Touch | 100% to first interaction | Understanding awareness |
| Last-Touch | 100% to last interaction | Direct response |
| Linear | Equal across all touches | Balanced view |
| Time-Decay | More to recent touches | Long sales cycles |
| Position-Based | 40/20/40 first-middle-last | Balanced with emphasis |
| Algorithmic | ML-determined weights | Data-rich environments |

### Attribution Implementation

| Element | Requirement |
|---------|-------------|
| Tracking | UTM parameters, cookies, user IDs |
| Data Integration | Connect marketing and sales data |
| Touchpoint Capture | Record all interactions |
| Conversion Definition | Clear conversion events |
| Reporting | Dashboard visibility |

---

## Experimentation

### A/B Testing Framework

| Step | Activity |
|------|----------|
| Hypothesis | Clear, testable statement |
| Metrics | Primary and secondary metrics |
| Sample Size | Statistical significance calculation |
| Duration | Run time for valid results |
| Segmentation | User segments to include |
| Analysis | Statistical significance, practical significance |
| Decision | Ship, iterate, or kill |

### Test Prioritization

| Framework | Formula |
|-----------|--------|
| ICE | Impact × Confidence × Ease |
| PIE | Potential × Importance × Ease |
| RICE | (Reach × Impact × Confidence) / Effort |

### Statistical Considerations

| Concept | Definition |
|---------|------------|
| Statistical Significance | Confidence that result isn't random |
| Practical Significance | Whether effect size matters |
| Power | Probability of detecting true effect |
| Sample Size | Minimum observations needed |
| Duration | Time needed for valid test |

---

## Cohort Analysis

### Cohort Types

| Type | Grouping | Use Case |
|------|----------|----------|
| Acquisition Cohort | Sign-up date | Retention analysis |
| Behavioral Cohort | Action taken | Feature adoption |
| Revenue Cohort | First purchase date | Revenue retention |
| Segment Cohort | User characteristics | Segment performance |

### Retention Cohort Table

```
| Cohort    | Month 1 | Month 2 | Month 3 | Month 6 | Month 12 |
|-----------|---------|---------|---------|---------|----------|
| Jan 2025  | 100%    | 65%     | 52%     | 38%     | 28%      |
| Feb 2025  | 100%    | 68%     | 55%     | 40%     | --       |
| Mar 2025  | 100%    | 70%     | 58%     | --      | --       |
```

### Cohort Analysis Applications

| Analysis | Purpose |
|----------|--------|
| Retention Trending | Is retention improving over time? |
| Feature Impact | Did feature launch improve cohorts? |
| Acquisition Quality | Which channels bring better cohorts? |
| Payback Validation | Are cohorts hitting payback targets? |

---

## Growth Dashboard

### Dashboard Components

| Section | Metrics |
|---------|--------|
| Acquisition | Traffic, leads, MQLs, SQLs, customers |
| Activation | Activation rate, time to value |
| Revenue | MRR, ARR, new MRR, expansion, churn |
| Retention | Cohort retention, NRR, GRR |
| Unit Economics | CAC, LTV, LTV:CAC, payback |
| Funnel | Conversion rates by stage |

### Visualization Best Practices

| Metric Type | Visualization |
|-------------|---------------|
| Trends | Line charts |
| Composition | Pie/stacked bar |
| Comparison | Bar charts |
| Distribution | Histogram |
| Funnel | Funnel visualization |
| Cohorts | Heat map tables |
