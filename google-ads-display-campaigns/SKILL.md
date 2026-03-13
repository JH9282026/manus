---
name: google-ads-display-campaigns
description: "Create and optimize Google Display Network campaigns including Responsive Display Ads, image ads, and remarketing. Use for brand awareness campaigns, audience targeting (affinity, in-market, custom intent), visual ad creation, placement targeting, contextual targeting, remarketing list setup, display ad specifications, and cross-device reach strategies."
---

# Google Ads Display Campaigns

Create visually engaging display advertising campaigns across Google Display Network's 2+ million websites and apps.

## Overview

This skill covers Google Display Network campaign creation: Responsive Display Ads, image ad specifications, audience targeting strategies, placement management, remarketing setup, and performance optimization. Use it for brand awareness, consideration, and remarketing objectives across web and mobile inventory.

## Campaign Type Selection

| Goal | Campaign Type | Targeting Method | Best For |
|------|---------------|------------------|----------|
| Brand awareness | Standard Display | Affinity audiences, topics | Reach, impressions |
| Consideration | Standard Display | In-market audiences, custom intent | Engagement, site visits |
| Remarketing | Standard Display | Remarketing lists | Re-engagement, conversions |
| Dynamic remarketing | Standard Display | Dynamic remarketing | E-commerce, personalized ads |
| Gmail ads | Standard Display | Gmail placements | Email-like ad experience |

## Responsive Display Ads (RDA)

### Asset Requirements

| Asset Type | Quantity | Specifications |
|------------|----------|----------------|
| **Headlines** | 1-5 | Max 30 characters each |
| **Long Headline** | 1 | Max 90 characters |
| **Descriptions** | 1-5 | Max 90 characters each |
| **Images** | 1-15 | Landscape (1.91:1), Square (1:1) |
| **Logos** | 1-5 | Square (1:1), min 128x128px |
| **Videos** | 0-5 | YouTube URLs, landscape/square |

### Image Specifications

| Type | Aspect Ratio | Min Size | Max Size | Recommended |
|------|--------------|----------|----------|-------------|
| Landscape | 1.91:1 | 600x314 | 1200x628 | 1200x628 |
| Square | 1:1 | 300x300 | 1200x1200 | 1200x1200 |
| Logo | 1:1 | 128x128 | 1200x1200 | 512x512 |

### Best Practices
- **Provide 15 images** (mix of landscape and square) for maximum reach
- **Use high-quality images** - Clear, professional, on-brand
- **Avoid text-heavy images** - Google may disapprove >20% text
- **Include logo** - Brand recognition across all ad variations
- **Test multiple headlines** - 5 headlines for optimization

## Uploaded Image Ads

### Standard Display Ad Sizes

| Size (px) | Name | Usage |
|-----------|------|-------|
| 300x250 | Medium Rectangle | Most common, high inventory |
| 336x280 | Large Rectangle | High performance |
| 728x90 | Leaderboard | Desktop, above content |
| 300x600 | Half Page | High engagement |
| 320x100 | Mobile Banner | Mobile-specific |
| 320x50 | Mobile Banner | Mobile, bottom of screen |
| 160x600 | Wide Skyscraper | Desktop, sidebar |
| 970x250 | Billboard | Desktop, premium placements |
| 970x90 | Large Leaderboard | Desktop, top of page |

### Image Ad Requirements
- **File format**: JPG, PNG, GIF (static or animated)
- **File size**: Max 150KB
- **Animation**: Max 30 seconds, must stop
- **Text**: Avoid >20% text coverage

## Audience Targeting

### Affinity Audiences (Awareness)

| Category | Examples | Use Case |
|----------|----------|----------|
| Sports & Fitness | Fitness buffs, running enthusiasts | Athletic products |
| Food & Dining | Foodies, cooking enthusiasts | Food, kitchen products |
| Technology | Tech early adopters, gadget enthusiasts | Electronics, software |
| Travel | Frequent travelers, luxury travelers | Travel services, luggage |

### In-Market Audiences (Consideration)

| Category | Intent Signal | Conversion Potential |
|----------|---------------|---------------------|
| Apparel & Accessories | Actively researching clothing | High |
| Autos & Vehicles | Shopping for cars | Very High |
| Business Services | Researching B2B solutions | High |
| Home & Garden | Planning home improvements | High |

### Custom Intent Audiences

**Create based on**:
- **Keywords**: Users searching for specific terms
- **URLs**: Users visiting specific websites
- **Apps**: Users using specific mobile apps

**Example**:
```
Audience: "Running Shoe Shoppers"
Keywords: running shoes, trail runners, marathon shoes
URLs: runnersworld.com, nike.com/running, brooksrunning.com
Apps: Strava, Nike Run Club, Runkeeper
```

### Remarketing Audiences

| List Type | Definition | Use Case |
|-----------|------------|----------|
| All visitors | Anyone who visited site | General remarketing |
| Product viewers | Viewed specific products | Product-specific ads |
| Cart abandoners | Added to cart, didn't purchase | Conversion recovery |
| Past purchasers | Completed purchase | Upsell, cross-sell |
| Video viewers | Watched YouTube videos | Video engagement |

## Placement Targeting

### Managed Placements

**When to use**:
- Target specific high-performing websites
- Exclude low-quality placements
- Control brand safety

**How to find placements**:
1. Run automatic targeting for 2-4 weeks
2. Review Placements report
3. Add high-performing sites as managed placements
4. Exclude low-performing sites

### Placement Exclusions

**Common exclusions**:
- Parked domains
- Error pages
- Mobile app games (if not relevant)
- Sensitive content categories

## Contextual Targeting

### Topics

| Topic Category | Reach | Precision |
|----------------|-------|----------|
| Broad topics | Very High | Low |
| Mid-level topics | High | Medium |
| Specific topics | Medium | High |

**Example hierarchy**:
- Sports (Broad)
  - Running & Jogging (Mid-level)
    - Marathon Training (Specific)

### Keywords (Contextual)

**How it works**: Ads show on pages containing your keywords

**Best practices**:
- Use 5-50 keywords per ad group
- Focus on themes, not exact match
- Combine with audience targeting for better performance

## Bidding Strategies

| Strategy | Goal | Best For |
|----------|------|----------|
| Target CPA | Cost-efficient conversions | Lead generation, e-commerce |
| Target ROAS | Revenue efficiency | E-commerce with variable values |
| Maximize Conversions | Conversion volume | Flexible CPA, maximize volume |
| Maximize Clicks | Traffic | Awareness, site visits |
| vCPM | Viewable impressions | Brand awareness |

## Performance Benchmarks

| Metric | Good Benchmark | Excellent Benchmark |
|--------|----------------|---------------------|
| CTR | 0.5-1.0% | >1.0% |
| Conversion Rate | 0.5-1.0% | >1.5% |
| CPA | Varies by industry | 30-50% below Search CPA |
| Viewability | >60% | >70% |

## Using the Reference Files

**`/references/rda-asset-optimization.md`** — Read when creating or optimizing Responsive Display Ads, including asset selection, image best practices, and headline/description strategies.

**`/references/audience-targeting-strategies.md`** — Read when setting up audience targeting, including affinity, in-market, custom intent, and remarketing audience creation and optimization.

**`/references/display-ad-creative-specs.md`** — Read when designing uploaded image ads, including all ad sizes, file requirements, design best practices, and approval guidelines.