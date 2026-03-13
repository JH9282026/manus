# Meta Campaign Structure Guide

Best practices for organizing Meta advertising campaigns.

---

## Campaign Hierarchy

```
Ad Account
└── Campaign (Objective, Budget)
    └── Ad Set (Targeting, Placement, Schedule, Bid)
        └── Ad (Creative, Copy, CTA)
```

---

## Campaign Organization Strategies

### 1. By Objective
```
Ad Account
├── Awareness Campaigns
│   ├── Brand Awareness - Video
│   └── Reach - Display
├── Consideration Campaigns
│   ├── Traffic - Blog Content
│   └── Engagement - Social Posts
└── Conversion Campaigns
    ├── Sales - Product Catalog
    └── Leads - Lead Gen Forms
```

### 2. By Funnel Stage
```
Ad Account
├── Top of Funnel (Cold)
│   ├── Awareness - Broad Targeting
│   └── Video Views - Interest Targeting
├── Middle of Funnel (Warm)
│   ├── Traffic - Website Visitors (30 days)
│   └── Engagement - Video Viewers
└── Bottom of Funnel (Hot)
    ├── Conversions - Add to Cart (7 days)
    └── Conversions - Abandoned Checkout
```

### 3. By Product/Service
```
Ad Account
├── Product A Campaigns
│   ├── Product A - Prospecting
│   └── Product A - Retargeting
├── Product B Campaigns
│   ├── Product B - Prospecting
│   └── Product B - Retargeting
```

---

## Campaign Budget Optimization (CBO)

### When to Use CBO

**Advantages**:
- Meta automatically distributes budget to best-performing ad sets
- Simplifies budget management
- Better for scaling
- Reduces manual optimization

**Best For**:
- 3+ ad sets per campaign
- Similar audiences
- Same optimization goal
- Scaling campaigns

### When to Use Ad Set Budgets

**Advantages**:
- Full control over spend per audience
- Testing new audiences
- Protecting budget for specific segments

**Best For**:
- Testing phase
- Very different audiences
- Guaranteed spend per segment
- Dayparting requirements

### CBO Configuration
```python
campaign_params = {
    "name": "CBO Campaign",
    "objective": "OUTCOME_SALES",
    "daily_budget": 10000,  # $100
    "bid_strategy": "LOWEST_COST_WITHOUT_CAP",
    "status": "PAUSED"
}

# Optional: Set ad set spend limits
adset_params = {
    "bid_amount": 500,  # Bid cap per ad set
    "daily_min_spend_target": 1000,  # Min $10/day
    "daily_spend_cap": 3000  # Max $30/day
}
```

---

## Ad Set Structure

### Audience Segmentation

**Option 1: Separate Ad Sets per Audience**
```
Campaign: Product Launch
├── Ad Set: Lookalike 1%
├── Ad Set: Lookalike 2-3%
├── Ad Set: Interest - Competitors
├── Ad Set: Website Visitors 30d
└── Ad Set: Customer List
```

**Option 2: Combined Audiences**
```
Campaign: Product Launch
├── Ad Set: Cold (Lookalikes + Interests)
├── Ad Set: Warm (Website Visitors)
└── Ad Set: Hot (Retargeting)
```

### Placement Strategy

**Automatic Placements** (Recommended)
- Meta optimizes across all placements
- Best performance
- Use for most campaigns

**Manual Placements**
- Specific creative requirements
- Platform-specific campaigns
- Exclude poor performers

```python
# Automatic
"publisher_platforms": ["facebook", "instagram", "messenger", "audience_network"]

# Manual - Instagram only
"publisher_platforms": ["instagram"],
"instagram_positions": ["stream", "story", "explore", "reels"]
```

---

## Scaling Strategies

### Vertical Scaling
Increase budget on existing ad sets.

**Best Practice**:
- Increase max 20% per day
- Wait 3-7 days between increases
- Monitor CPA closely

```python
def vertical_scale(adset_id, current_budget):
    new_budget = int(current_budget * 1.2)
    update_adset_budget(adset_id, new_budget)
```

### Horizontal Scaling
Add new ad sets with similar audiences.

**Strategies**:
- Expand to new interests
- Broader lookalike percentages
- New geographic regions
- Additional placements

```python
# Duplicate winning ad set with new audience
def horizontal_scale(winning_adset, new_targeting):
    new_adset = duplicate_adset(winning_adset)
    update_adset_targeting(new_adset["id"], new_targeting)
```

---

## Testing Framework

### Creative Testing
```
Campaign: Product A - Testing
└── Ad Set: US Adults 25-45
    ├── Ad: Image Variant A
    ├── Ad: Image Variant B
    ├── Ad: Video Variant A
    └── Ad: Carousel Variant A
```

**Rules**:
- 3-5 ads per ad set
- Same audience
- Run until statistical significance
- Pause losers, scale winners

### Audience Testing
```
Campaign: Audience Test
├── Ad Set: Interest A
├── Ad Set: Interest B
├── Ad Set: Lookalike 1%
└── Ad Set: Lookalike 2-3%
```

**Rules**:
- Same creative across ad sets
- Equal budgets
- Minimum 1000 impressions per ad set
- Compare CPA/ROAS

---

## Naming Conventions

### Campaign Names
```
{Objective}_{Product}_{Audience}_{Date}

Examples:
- SALES_ProductA_Prospecting_2026Q2
- TRAFFIC_Blog_Retargeting_Mar2026
```

### Ad Set Names
```
{Audience}_{Placement}_{Age}_{Gender}

Examples:
- LAL1%_AutoPlacement_25-45_All
- Interest-Tech_IG-Only_18-34_M
```

### Ad Names
```
{Format}_{Variant}_{CTA}

Examples:
- Image_A_LearnMore
- Video_B_ShopNow
- Carousel_C_SignUp
```
