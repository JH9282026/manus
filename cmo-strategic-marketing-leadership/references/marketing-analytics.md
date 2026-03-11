# Marketing Analytics and Attribution

Measure marketing effectiveness and optimize performance through data-driven insights.

---

## Attribution Models

### Common Models

| Model | Logic | Best For | Limitation |
|---|---|---|---|
| First touch | 100% credit to first interaction | Understanding top-of-funnel | Ignores nurture journey |
| Last touch | 100% credit to last interaction | Understanding conversion drivers | Ignores awareness building |
| Linear | Equal credit to all touchpoints | Balanced view | Over-simplifies |
| Time decay | More credit to recent interactions | Sales-focused analysis | Under-values awareness |
| U-shaped | 40% first, 40% last, 20% middle | Balanced first/last emphasis | Arbitrary weighting |
| W-shaped | 30% first, 30% lead creation, 30% opportunity, 10% rest | B2B with clear funnel stages | Complex to implement |
| Algorithmic/ML | Data-driven credit allocation | Organizations with sufficient data | Requires large datasets, less transparent |

### Multi-Touch Attribution Implementation

1. Define the customer journey stages and key conversion events
2. Collect touchpoint data across all channels (UTM parameters, cookies, CRM)
3. Select attribution model aligned to business questions
4. Implement tracking infrastructure (CDP, marketing analytics platform)
5. Build attribution reporting dashboard
6. Validate with incrementality testing (holdout groups, geo-tests)

---

## Marketing Dashboard Design

### Executive Dashboard Metrics

| Metric | Definition | Target Setting |
|---|---|---|
| Marketing-sourced pipeline | Pipeline from marketing-generated leads | 40-60% of total pipeline |
| Marketing-influenced revenue | Revenue where marketing touched any stage | 70-80% of closed revenue |
| Customer acquisition cost (CAC) | (Marketing spend + sales cost) / new customers | < 1/3 of first-year CLV |
| CAC payback period | CAC / monthly gross margin per customer | < 12 months |
| Marketing ROI | (Revenue attributed - marketing cost) / marketing cost | 5:1 or higher |
| Pipeline-to-close ratio | Closed deals / qualified pipeline | 20-30% |

### Channel Performance Reporting

Report weekly/monthly by channel:
- Spend and budget utilization
- Impressions, clicks, engagement
- Leads generated (MQLs, SQLs)
- Pipeline created and influenced
- Revenue attributed
- Cost per lead, cost per opportunity, cost per customer
- Return on ad spend (ROAS)
