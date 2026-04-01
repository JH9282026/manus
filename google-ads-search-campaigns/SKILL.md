---
name: google-ads-search-campaigns
description: "Create and optimize Google Ads Search campaigns including Responsive Search Ads, Dynamic Search Ads, and Call-Only Ads. Use for keyword research and targeting, ad copy creation with multiple headlines and descriptions, bid strategy selection (Manual CPC, Target CPA, Target ROAS, Maximize Conversions), campaign structure design, quality score optimization, negative keyword management, ad extensions setup, and search partner network configuration."
---

# Google Ads Search Campaigns

Create high-performing search advertising campaigns on Google Search Network with optimized targeting, bidding, and ad formats.

## Overview

This skill covers the complete Google Ads Search campaign lifecycle: campaign structure, keyword targeting, Responsive Search Ads creation, bidding strategies, quality score optimization, and API-based automation. Use it for driving traffic, leads, and sales through Google Search, Maps, and Search Partner sites.

## Campaign Type Selection

| Business Goal | Campaign Type | Bidding Strategy | Best For |
|---------------|---------------|------------------|----------|
| Drive website traffic | Standard Search | Maximize Clicks | New campaigns, traffic goals |
| Generate leads | Standard Search | Target CPA | Lead generation, form fills |
| Maximize sales value | Standard Search | Target ROAS | E-commerce, revenue optimization |
| Phone call conversions | Call-Only | Maximize Conversions | Service businesses, local |
| Dynamic inventory | Dynamic Search Ads | Target CPA | Large catalogs, e-commerce |

## Responsive Search Ads (RSA) Structure

### Asset Requirements
- **Headlines**: 3-15 unique headlines (max 30 characters each)
- **Descriptions**: 2-4 unique descriptions (max 90 characters each)
- **Display URLs**: Up to 2 path fields (15 characters each)
- **Final URL**: Landing page destination

### Best Practices
1. **Provide 15 headlines** for maximum optimization potential
2. **Pin strategically** - only pin when brand/legal requirements demand it
3. **Include keywords** in at least 5 headlines for relevance
4. **Vary message types**: features, benefits, CTAs, questions, offers
5. **Use Dynamic Keyword Insertion** sparingly: `{KeyWord:Default Text}`

### Ad Strength Optimization

| Ad Strength | Requirements | Performance Impact |
|-------------|--------------|--------------------|
| Excellent | 10+ unique headlines, 4 descriptions, no pins | +15-20% CTR potential |
| Good | 8-9 headlines, 3-4 descriptions, minimal pins | +10-15% CTR potential |
| Average | 5-7 headlines, 2-3 descriptions | Baseline performance |
| Poor | <5 headlines, repetitive copy | -10-20% CTR |

## Keyword Targeting Strategy

### Match Types

| Match Type | Syntax | When to Use | Control Level |
|------------|--------|-------------|---------------|
| Exact | `[keyword]` | High-intent, specific terms | Highest |
| Phrase | `"keyword phrase"` | Moderate intent, phrase variations | Medium |
| Broad | `keyword` | Discovery, broad reach | Lowest |

### Keyword Research Process
1. **Seed keywords** - Start with 10-20 core business terms
2. **Expand** - Use Keyword Planner API for suggestions
3. **Analyze intent** - Categorize by funnel stage (awareness, consideration, decision)
4. **Estimate volume** - Target 100-1000 monthly searches for most keywords
5. **Assess competition** - Balance volume with competition level

### Negative Keyword Management
- **Campaign-level negatives**: Broad exclusions (e.g., "free", "jobs", "DIY")
- **Ad group-level negatives**: Specific exclusions to prevent overlap
- **Shared negative lists**: Reusable lists across campaigns
- **Search term mining**: Weekly review of search terms report

## Bidding Strategies

### Manual vs. Automated

| Strategy | Control | Learning Period | Best For |
|----------|---------|-----------------|----------|
| Manual CPC | Full control | None | Testing, small budgets |
| Enhanced CPC | Moderate | 1-2 weeks | Transition to automation |
| Maximize Clicks | Low | 1-2 weeks | Traffic goals |
| Target CPA | Low | 2-4 weeks | Lead generation (30+ conversions/month) |
| Target ROAS | Low | 4-6 weeks | E-commerce (50+ conversions/month) |
| Maximize Conversions | Low | 2-4 weeks | Flexible CPA, maximize volume |
| Maximize Conversion Value | Low | 4-6 weeks | Flexible ROAS, maximize revenue |

### Bid Adjustment Factors
- **Device**: -100% to +900% (mobile, desktop, tablet)
- **Location**: -90% to +900% (geographic performance)
- **Ad schedule**: -90% to +900% (day/hour performance)
- **Audience**: -90% to +900% (remarketing, in-market)

## Quality Score Optimization

### Components (1-10 scale)
1. **Expected CTR** (40% weight) - Historical ad performance
2. **Ad Relevance** (30% weight) - Keyword-to-ad alignment
3. **Landing Page Experience** (30% weight) - Page quality and relevance

### Improvement Tactics

| Low Component | Fix Strategy | Expected Impact |
|---------------|--------------|------------------|
| Expected CTR | Improve ad copy, add emotional triggers | +1-2 QS points |
| Ad Relevance | Tighter ad groups (5-20 keywords), keyword in headlines | +1-3 QS points |
| Landing Page | Improve load speed, match ad message, clear CTA | +1-2 QS points |

## Campaign Structure Best Practices

### Single Keyword Ad Groups (SKAGs)
- **Structure**: 1 keyword per ad group (all match types)
- **Pros**: Maximum relevance, granular control
- **Cons**: High maintenance, many ad groups
- **Best for**: High-value keywords, exact control needed

### Themed Ad Groups
- **Structure**: 5-20 related keywords per ad group
- **Pros**: Easier management, scalable
- **Cons**: Less granular control
- **Best for**: Most campaigns, balanced approach

### Campaign Organization
```
Account
├── Campaign: Brand (Exact Match)
│   ├── Ad Group: Brand Name
│   └── Ad Group: Brand + Product
├── Campaign: Generic (High Intent)
│   ├── Ad Group: Product Category 1
│   └── Ad Group: Product Category 2
├── Campaign: Generic (Broad)
│   └── Ad Group: Discovery Keywords
└── Campaign: Competitors
    └── Ad Group: Competitor Terms
```

## Ad Extensions

| Extension Type | Use Case | Character Limits | Impact |
|----------------|----------|------------------|--------|
| Sitelink | Additional landing pages | 25 char title, 35 char descriptions | +10-20% CTR |
| Callout | Feature highlights | 25 characters each | +5-10% CTR |
| Structured Snippet | Product/service categories | Header + 3-10 values | +5-10% CTR |
| Call | Phone number | Phone + country code | +5-15% call conversions |
| Location | Physical address | Auto-populated from Google My Business | +10% local CTR |
| Price | Product/service pricing | 8 items max, 25 char headers | +5-10% qualified clicks |
| Promotion | Special offers | 20 char occasion, 15 char discount | +10-15% CTR during promos |
| Image | Visual assets | 1.91:1 or 1:1 aspect ratio | +5-10% CTR |

## Dynamic Search Ads (DSA)

### When to Use DSA
- **Large websites** (500+ pages)
- **Frequently changing inventory** (e-commerce)
- **Keyword gap filling** (supplement existing campaigns)
- **New market testing** (discover search terms)

### DSA Targeting Options
1. **All webpages** - Entire website
2. **Specific categories** - Auto-generated from site structure
3. **URL contains** - Pages matching URL patterns
4. **Page title contains** - Pages with specific title keywords
5. **Custom labels** - Pages tagged in feed

### DSA Best Practices
- Use **separate campaigns** for DSA (don't mix with keyword campaigns)
- Set **negative keywords** to prevent overlap with existing campaigns
- Create **multiple ad groups** by category for better control
- Monitor **search terms** weekly to add high-performers as keywords
- Exclude **low-value pages** (checkout, cart, login)

## Call-Only Ads

### Requirements
- **Mobile-only** campaigns (desktop not supported)
- **Phone number** with country code
- **Business verification** required
- **Call reporting** enabled for conversion tracking

### Ad Components
- **Business name**: 25 characters
- **Description lines**: 2 lines, 35 characters each
- **Phone number**: Auto-formatted
- **Verification URL**: Optional display URL

## Network Settings

### Search Network
- **Google Search** - Always included
- **Search Partners** - Optional (Bing, AOL, other partners)
  - Typically 10-20% additional volume
  - Monitor performance separately
  - Disable if CPA >20% higher than Google Search

### Display Network Expansion
- **Display Expansion** - Opt-in for Search campaigns
- Shows ads on Display Network when Search inventory limited
- Typically lower quality traffic
- Recommended: Disable for most Search campaigns

## Performance Monitoring

### Key Metrics

| Metric | Good Benchmark | Optimization Action |
|--------|----------------|---------------------|
| CTR | >3% (Search), >0.5% (Display) | Improve ad copy, test new headlines |
| Conversion Rate | >2-5% (varies by industry) | Optimize landing pages, adjust targeting |
| Quality Score | >7/10 | Improve relevance, CTR, landing page |
| Impression Share | >80% (branded), >50% (generic) | Increase bids or budget |
| CPA | <Target CPA | Adjust bids, improve conversion rate |
| ROAS | >Target ROAS | Optimize for higher-value conversions |

### A/B Testing Framework
1. **Test one variable** at a time (headlines, descriptions, CTAs)
2. **Statistical significance** - Wait for 100+ clicks per variant
3. **Rotation settings** - Use "Optimize" for automated testing
4. **Winner criteria** - 95% confidence level, 10%+ improvement

## Using the Reference Files

### When to Read Each Reference

**`/references/api-campaign-setup.md`** — Read when setting up campaigns programmatically via Google Ads API, including authentication, campaign creation, ad group structure, and keyword insertion.

**`/references/rsa-optimization-guide.md`** — Read when creating or optimizing Responsive Search Ads, including headline formulas, description strategies, pinning best practices, and ad strength improvement.

**`/references/keyword-research-advanced.md`** — Read when conducting comprehensive keyword research, including competitor analysis, search intent mapping, keyword clustering, and forecasting.

**`/references/quality-score-deep-dive.md`** — Read when diagnosing and improving Quality Score issues, including component analysis, landing page optimization, and CTR improvement tactics.

**`/references/bidding-strategy-selection.md`** — Read when choosing or switching bidding strategies, including conversion tracking setup, learning period management, and performance troubleshooting.

**`/references/ad-extensions-complete.md`** — Read when implementing all ad extension types, including setup instructions, best practices, and performance benchmarks for each extension.

**`/references/search-term-mining.md`** — Read when analyzing search term reports to discover new keywords, add negatives, and optimize match type distribution.

## References

- [Ad Extensions Complete](references/ad-extensions-complete.md)
- [Api Campaign Setup](references/api-campaign-setup.md)
- [Bidding Strategy Selection](references/bidding-strategy-selection.md)
- [Keyword Research Advanced](references/keyword-research-advanced.md)
- [Quality Score Deep Dive](references/quality-score-deep-dive.md)
- [Rsa Optimization Guide](references/rsa-optimization-guide.md)
- [Search Term Mining](references/search-term-mining.md)
