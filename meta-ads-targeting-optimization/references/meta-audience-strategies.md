# Meta Audience Strategies

Strategic frameworks for building and optimizing Meta advertising audiences.

---

## Audience Funnel Framework

### Cold Audiences (Prospecting)

**Objective**: Reach new people

**Targeting Options**:
1. **Broad Interest Targeting**
   - 2-5 related interests
   - Age/gender/location only
   - Let Meta optimize

2. **Lookalike Audiences**
   - 1-2% of best customers
   - Website visitors (top 25%)
   - High-value purchasers

3. **Advantage+ Audience**
   - Minimal constraints
   - Location + age only
   - Full AI optimization

**Budget Allocation**: 40-60% of total

### Warm Audiences (Consideration)

**Objective**: Re-engage interested users

**Targeting Options**:
1. **Website Visitors**
   - All visitors (30-90 days)
   - Specific pages (product, pricing)
   - Time on site (>2 minutes)

2. **Engagement Audiences**
   - Video viewers (50%+)
   - Instagram/Facebook engagers
   - Lead form openers (didn't submit)

3. **Lookalike of Engagers**
   - 1-3% of video viewers
   - 1-3% of page engagers

**Budget Allocation**: 20-30% of total

### Hot Audiences (Conversion)

**Objective**: Convert high-intent users

**Targeting Options**:
1. **Cart Abandoners**
   - Added to cart, no purchase (7 days)
   - Initiated checkout (3 days)

2. **Product Viewers**
   - Viewed specific products (14 days)
   - Viewed multiple products (7 days)

3. **Past Purchasers**
   - Exclude recent buyers (<30 days)
   - Cross-sell (60-90 days)
   - Replenishment (based on product cycle)

**Budget Allocation**: 20-40% of total

---

## Lookalike Audience Optimization

### Source Audience Quality

**Best Sources** (in order):
1. High-value customers (top 25% LTV)
2. Recent purchasers (90 days)
3. All purchasers (365 days)
4. Add to cart (30 days)
5. Website visitors (top 25% time on site)

**Minimum Size**: 100 people (1,000+ recommended)

### Percentage Strategy

**1% Lookalike**
- Most similar to source
- Smallest audience
- Best for: High-value products, niche markets
- Expected performance: Highest conversion rate, higher CPA

**2-3% Lookalike**
- Balanced similarity and scale
- Best for: Most campaigns
- Expected performance: Good conversion rate, moderate CPA

**4-10% Lookalike**
- Broader reach
- Best for: Awareness, large budgets
- Expected performance: Lower conversion rate, lower CPA

### Stacked Lookalikes

**Strategy**: Create tiered lookalikes

```
Campaign: Lookalike Prospecting
├── Ad Set: LAL 0-1%
├── Ad Set: LAL 1-2%
├── Ad Set: LAL 2-3%
└── Ad Set: LAL 3-5%
```

**Benefits**:
- Test different similarity levels
- Avoid audience overlap
- Scale based on performance

### Multi-Source Lookalikes

**Strategy**: Combine multiple source audiences

```python
# Create combined source
source_audiences = [
    high_value_customers_id,
    recent_purchasers_id,
    engaged_users_id
]

# Meta will combine and create lookalike
```

---

## Retargeting Funnel

### 30-Day Retargeting Ladder

**Day 0-7: Hot Retargeting**
- Cart abandoners
- Checkout initiators
- Product viewers
- Message: Urgency, scarcity, discount
- Budget: High

**Day 8-14: Warm Retargeting**
- Category browsers
- Multiple page visitors
- Video viewers (75%+)
- Message: Benefits, social proof
- Budget: Medium

**Day 15-30: Cool Retargeting**
- All website visitors
- Video viewers (25%+)
- Page engagers
- Message: Awareness, education
- Budget: Low

### Exclusion Strategy

**Always Exclude**:
- Recent purchasers (7-30 days)
- Current customers (if not cross-selling)
- Employees (email list)

**Example**:
```python
targeting = {
    "custom_audiences": [{"id": cart_abandoners_id}],
    "excluded_custom_audiences": [
        {"id": recent_purchasers_id},
        {"id": employees_id}
    ]
}
```

---

## Scaling Strategies

### Vertical Scaling

**Method**: Increase budget on winning ad sets

**Best Practices**:
- Increase max 20% every 3 days
- Monitor CPA closely
- Pause if CPA increases >30%

**Example**:
```
Day 1: $50/day, CPA $25
Day 4: $60/day (+20%), CPA $27 ✓
Day 7: $72/day (+20%), CPA $26 ✓
Day 10: $86/day (+20%), CPA $35 ✗ (rollback)
```

### Horizontal Scaling

**Method**: Duplicate winning ad sets with new audiences

**Strategies**:
1. **Geographic Expansion**
   - Start: US only
   - Expand: CA, UK, AU
   - Then: EU countries

2. **Lookalike Expansion**
   - Start: 1% LAL
   - Add: 2-3% LAL
   - Then: 4-5% LAL

3. **Interest Expansion**
   - Start: Core interest
   - Add: Related interests
   - Then: Broader categories

### Campaign Budget Optimization (CBO) Scaling

**Strategy**: Let Meta distribute budget

**Setup**:
```
Campaign: CBO Prospecting ($500/day)
├── Ad Set: LAL 1% (Meta allocates)
├── Ad Set: LAL 2-3% (Meta allocates)
├── Ad Set: Interest A (Meta allocates)
└── Ad Set: Interest B (Meta allocates)
```

**Benefits**:
- Automatic optimization
- Faster learning
- Better overall performance

**When to Use**:
- 3+ ad sets
- Similar audiences
- Scaling phase

---

## Audience Testing Framework

### A/B Test Structure

**Test 1: Audience Type**
```
Campaign: Audience Test
├── Ad Set A: Interest targeting
├── Ad Set B: Lookalike 1%
└── Ad Set C: Advantage+ Audience
```

**Test 2: Lookalike Percentage**
```
Campaign: LAL Test
├── Ad Set A: LAL 1%
├── Ad Set B: LAL 2-3%
└── Ad Set C: LAL 4-5%
```

**Test 3: Retargeting Window**
```
Campaign: Retargeting Test
├── Ad Set A: Website visitors 7d
├── Ad Set B: Website visitors 14d
└── Ad Set C: Website visitors 30d
```

### Testing Methodology

**Requirements**:
- Same creative across ad sets
- Equal budgets
- Minimum 1,000 impressions per ad set
- Run for 7+ days

**Success Metrics**:
- CPA (primary)
- ROAS (for e-commerce)
- CTR (secondary)
- Conversion rate (secondary)

---

## Advanced Audience Tactics

### Audience Layering

**Strategy**: Combine multiple targeting criteria

**Example 1: High-Intent B2B**
```python
targeting = {
    "interests": [{"id": "marketing_id"}],
    "behaviors": [{"id": "small_business_owner_id"}],
    "job_title": "Marketing Manager"
}
```

**Example 2: Affluent Shoppers**
```python
targeting = {
    "interests": [{"id": "luxury_goods_id"}],
    "behaviors": [{"id": "high_income_id"}],
    "geo_locations": {"zips": high_income_zips}
}
```

### Audience Exclusion Optimization

**Strategy**: Improve efficiency by excluding low-performers

**Common Exclusions**:
1. Job seekers (for B2C)
2. Students (for high-ticket items)
3. Competitors' employees
4. Low-engagement users

### Seasonal Audience Shifts

**Strategy**: Adjust targeting by season

**Example: Fitness Product**
- **January**: New Year's resolution seekers
- **May**: Summer body preparation
- **September**: Back-to-routine
- **November**: Holiday gift buyers

---

## Audience Performance Benchmarks

### By Audience Type

| Audience Type | Expected CTR | Expected CPA | Scale Potential |
|---------------|--------------|--------------|------------------|
| **Cart Abandoners** | 2-4% | Low | Limited |
| **Website Visitors** | 1.5-3% | Medium | Medium |
| **LAL 1%** | 1-2% | Medium | Medium |
| **LAL 2-5%** | 0.8-1.5% | Medium-High | High |
| **Interest Targeting** | 0.8-1.5% | Medium-High | High |
| **Advantage+ Audience** | 1-2% | Medium | Very High |

### Optimization Triggers

**Pause if**:
- CPA > target by 50%+
- Spend > $100 with 0 conversions
- Frequency > 4

**Scale if**:
- CPA < target by 20%+
- ROAS > 3x
- Consistent performance 7+ days
