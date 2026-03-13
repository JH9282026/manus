# Bidding Strategy Selection Guide

Comprehensive guide to choosing and optimizing Google Ads bidding strategies for Search campaigns.

---

## Bidding Strategy Overview

### Available Strategies for Search Campaigns

| Strategy | Goal | Control Level | Min Conversions/Month | Best For |
|----------|------|---------------|----------------------|----------|
| **Manual CPC** | Traffic control | Full | 0 | Testing, small budgets, full control |
| **Enhanced CPC** | Improve conversions | Moderate | 0 | Transition to automation |
| **Maximize Clicks** | Maximum traffic | Low | 0 | Traffic goals, awareness |
| **Target CPA** | Cost-efficient leads | Low | 30+ | Lead generation, consistent CPA |
| **Target ROAS** | Revenue efficiency | Low | 50+ | E-commerce, value optimization |
| **Maximize Conversions** | Conversion volume | Low | 15+ | Flexible CPA, maximize volume |
| **Maximize Conversion Value** | Revenue maximization | Low | 30+ | Flexible ROAS, maximize revenue |

---

## Manual CPC

**When to Use**:
- New campaigns (testing phase)
- Small budgets (<$1,000/month)
- Need full bid control
- Insufficient conversion data for automation

**Setup**:
- Set keyword-level or ad group-level bids
- Optional: Enable Enhanced CPC for automatic bid adjustments

**Pros**:
- Full control over bids
- No learning period
- Predictable costs

**Cons**:
- Time-intensive management
- Misses optimization opportunities
- Requires constant monitoring

---

## Target CPA (Cost Per Acquisition)

**When to Use**:
- Lead generation campaigns
- 30+ conversions per month minimum
- Consistent target cost per lead/sale
- Stable conversion rates

**Setup**:
1. Enable conversion tracking
2. Accumulate 30+ conversions in 30 days
3. Calculate target CPA: Total Cost / Total Conversions
4. Set Target CPA 10-20% below current CPA
5. Allow 2-4 week learning period

**Optimization**:
- Start with current CPA, gradually lower by 10% every 2 weeks
- Monitor conversion volume (shouldn't drop >20%)
- Increase target CPA if volume drops significantly

---

## Target ROAS (Return on Ad Spend)

**When to Use**:
- E-commerce campaigns
- 50+ conversions per month minimum
- Variable order values
- Revenue optimization priority

**Setup**:
1. Enable conversion tracking with values
2. Accumulate 50+ conversions in 30 days
3. Calculate current ROAS: Revenue / Cost
4. Set Target ROAS 20-30% below current ROAS initially
5. Allow 4-6 week learning period

**ROAS Calculation**:
- Current ROAS = $10,000 revenue / $2,000 cost = 500%
- Target ROAS = 400% (conservative start)
- Gradually increase to 500-600% over 2-3 months

---

## Maximize Conversions

**When to Use**:
- Flexible CPA tolerance
- Want maximum conversion volume
- 15+ conversions per month
- Daily budget is the constraint

**Setup**:
- Set daily budget (Google will spend up to 2x on high-performing days)
- Optional: Set Target CPA for cost control
- Allow 2-4 week learning period

**Best Practices**:
- Use when you want volume over efficiency
- Monitor CPA closely (can fluctuate)
- Set Target CPA if costs exceed acceptable range

---

## Conversion Tracking Requirements

All automated bidding strategies require proper conversion tracking:

1. **Google Ads Conversion Tracking** or **Google Analytics 4 Goals**
2. **Minimum 15-30 conversions per month** for learning
3. **Consistent conversion actions** (don't change definitions frequently)
4. **Accurate conversion values** (for ROAS strategies)

---

## Learning Period Management

**What is Learning Period?**
- Time for Google's algorithm to optimize bids
- Typically 1-6 weeks depending on strategy
- Performance may fluctuate during this time

**Best Practices During Learning**:
- Don't make major changes (budget, targeting, bids)
- Allow at least 2 weeks before judging performance
- Expect CPA/ROAS to be 20-30% worse initially
- Monitor daily but don't panic

---

## Bidding Strategy Comparison

### Performance Benchmarks

| Metric | Manual CPC | Target CPA | Target ROAS | Maximize Conversions |
|--------|-----------|-----------|-------------|---------------------|
| **Avg CPA** | Baseline | -15% to -25% | -10% to -20% | +10% to +20% |
| **Conversion Volume** | Baseline | -5% to -10% | -10% to -20% | +20% to +40% |
| **Time Investment** | High | Low | Low | Low |
| **Predictability** | High | Medium | Medium | Low |

---

## When to Switch Strategies

### From Manual CPC to Target CPA
- **Trigger**: 30+ conversions per month
- **Process**: Enable Target CPA at current CPA, monitor for 2 weeks

### From Target CPA to Target ROAS
- **Trigger**: Variable conversion values, need revenue optimization
- **Process**: Calculate current ROAS, set target 20% below, monitor for 4 weeks

### From Maximize Conversions to Target CPA
- **Trigger**: CPA too high or unpredictable
- **Process**: Set Target CPA at acceptable level, monitor volume

---

## Troubleshooting Bidding Strategies

### Issue: "Limited by Budget"
- **Cause**: Target CPA/ROAS too aggressive for budget
- **Fix**: Increase budget by 20-50% or relax target

### Issue: Conversion Volume Dropped
- **Cause**: Target too aggressive
- **Fix**: Increase Target CPA by 15-20% or lower Target ROAS

### Issue: CPA Increased Significantly
- **Cause**: Learning period or market changes
- **Fix**: Wait 2 weeks, then adjust target or switch strategies

### Issue: "Learning" Status for Weeks
- **Cause**: Insufficient conversion volume
- **Fix**: Increase budget, broaden targeting, or switch to Maximize Conversions

---

## Advanced Bidding Tactics

### Portfolio Bid Strategies
- Share one bid strategy across multiple campaigns
- Useful for managing overall account CPA/ROAS
- Requires 50+ conversions per month across all campaigns

### Seasonality Adjustments
- Inform Google of expected conversion rate changes
- Use for sales, holidays, promotions
- Prevents algorithm from over-correcting

### Data-Driven Attribution
- Use with Target CPA/ROAS for better credit assignment
- Requires 3,000+ clicks and 300+ conversions in 30 days
- Improves bidding accuracy by 10-20%
