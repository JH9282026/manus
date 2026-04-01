---
name: outbrain-campaign-management
description: "Create and manage native advertising campaigns on the Outbrain content discovery platform. Use for: Outbrain campaign setup, native ad creation, content recommendation targeting, bid optimization, audience segmentation, publisher network selection, and content marketing amplification through native discovery."
---

# Outbrain Campaign Management

Create, manage, and optimize native advertising campaigns on the Outbrain content discovery network to amplify content and drive qualified traffic.

## Overview

Outbrain is a leading content discovery platform that places native ads (content recommendations) on premium publisher sites like CNN, BBC, The Guardian, and 7,000+ other properties. Unlike search or social ads, Outbrain campaigns leverage curiosity-driven discovery — users encounter your content as recommended articles/videos alongside editorial content. This skill covers campaign structure, targeting strategies, creative optimization, bid management, and performance benchmarks.

## Campaign Structure

| Level | Purpose | Key Settings |
|-------|---------|-------------|
| Campaign | Budget and schedule container | Daily/lifetime budget, start/end dates, objective |
| Section (targeting) | Audience and placement targeting | Location, device, publisher block/allow lists |
| Ad (content) | Individual promoted content pieces | Title, image, landing page URL, CPC bid |

### Campaign Objectives

| Objective | Optimization Goal | Bid Type | Best For |
|-----------|-------------------|----------|----------|
| Traffic | Click volume | CPC | Blog posts, content hubs |
| Conversions | Conversion events | CPA or CPC | Lead gen, signups, purchases |
| Brand Awareness | Impressions | CPM | Brand campaigns, video views |
| App Installs | App store clicks | CPC/CPI | Mobile app promotion |

## Targeting Options

| Targeting Type | Options | Granularity | Reference |
|---------------|---------|-------------|-----------|
| Geographic | Country, region, state/province, DMA, city | Down to city level | `/references/targeting-strategies.md` |
| Device | Desktop, mobile, tablet | Device type | `/references/targeting-strategies.md` |
| Operating system | iOS, Android, Windows, Mac | OS level | `/references/targeting-strategies.md` |
| Browser | Chrome, Safari, Firefox, Edge | Browser level | `/references/targeting-strategies.md` |
| Publisher | Allow-list or block-list specific sites | Individual publisher | `/references/targeting-strategies.md` |
| Interest | IAB categories, Outbrain interest segments | Category level | `/references/targeting-strategies.md` |
| Custom audiences | Pixel-based retargeting, lookalike | Audience segment | `/references/targeting-strategies.md` |
| Time of day | Day-parting by hour and day of week | Hourly | `/references/targeting-strategies.md` |

### Targeting Best Practices
- Start broad, then narrow based on performance data
- Separate mobile and desktop into different campaign sections (behavior differs significantly)
- Use publisher block-lists to remove poor-performing sites (check within first 48 hours)
- Create separate campaigns per geo region for budget control
- Layer interest targeting only after establishing baseline performance

## Creative Best Practices

### Headline Formulas That Work

| Formula | Example | Average CTR Lift |
|---------|---------|-----------------|
| Number + benefit | "7 Ways to Reduce Cloud Costs by 40%" | +25% |
| Question format | "Is Your Data Strategy Missing This Critical Step?" | +20% |
| How-to | "How to Build a Customer Health Score in 30 Minutes" | +18% |
| Curiosity gap | "The Marketing Metric Most CMOs Ignore" | +30% |
| Newsjacking | "What the 2026 Privacy Rules Mean for Your Ads" | +15% |

### Image Guidelines

| Element | Recommendation | Why |
|---------|---------------|-----|
| Image type | People, close-ups, authentic photos | Outperform stock photos by 30–50% |
| Faces | Include human faces, preferably looking at camera | Higher engagement |
| Color | High contrast, bright colors | Stands out in publisher feeds |
| Text overlay | Avoid or minimal | Platform may reject heavy text |
| Size | 1200×800px minimum | Required for HD placements |
| A/B test | 3–5 image variations per ad | Identify winning creative quickly |

### Ad-to-Landing Page Alignment
- Landing page headline must directly address the ad headline's promise
- Above-the-fold content should deliver on curiosity gap immediately
- Include clear CTA within first scroll
- Page load speed <3 seconds (Outbrain traffic is mobile-heavy)
- Avoid interstitials or popups on first visit

## Bid & Budget Management

| Budget Level | Recommended Daily | Testing Phase | Scale Phase |
|-------------|-------------------|---------------|-------------|
| Small test | $50–$100/day | 3–5 days | After winning creative identified |
| Medium campaign | $200–$500/day | 5–7 days | Gradual 20% daily increases |
| Large campaign | $1,000+/day | 7–10 days | Auto-optimize with CPA target |

### Bid Optimization Strategy

| Phase | Duration | Action | KPI Focus |
|-------|----------|--------|-----------|
| Launch | Days 1–3 | Set competitive CPC, broad targeting | Impressions, CTR |
| Learn | Days 4–7 | Review publisher and section performance | CTR, CPC, bounce rate |
| Optimize | Days 8–14 | Block underperformers, increase bids on winners | CPA, conversion rate |
| Scale | Day 15+ | Expand targeting, increase budgets on profitable segments | ROI, total conversions |

## Performance Benchmarks

| Metric | Below Average | Average | Above Average | Excellent |
|--------|--------------|---------|---------------|-----------|
| CTR | <0.10% | 0.10–0.20% | 0.20–0.40% | >0.40% |
| CPC | Varies by geo | $0.15–$0.50 US | $0.08–$0.15 US | <$0.08 |
| Landing page bounce rate | >70% | 50–70% | 35–50% | <35% |
| Avg. time on page | <30s | 30–60s | 60–120s | >120s |
| Conversion rate (lead gen) | <1% | 1–3% | 3–5% | >5% |

## Common Mistakes and Fixes

| Mistake | Impact | Fix |
|---------|--------|-----|
| Not separating mobile/desktop | Budget wasted on low-converting device | Create separate sections per device |
| Ignoring publisher reports | Spend on low-quality sites | Review and block-list within 48 hours |
| Too few creative variations | Slow learning, creative fatigue | Launch with 5+ headline/image combos |
| Clickbait headlines | High CTR but high bounce, low conversion | Match headline promise to landing page |
| Setting CPA too low at launch | Insufficient traffic to learn | Start with CPC, switch to CPA after data |
| Not tracking post-click behavior | Can't optimize for conversions | Implement Outbrain pixel before launch |

## Best Practices

- **Install the Outbrain pixel before launching** — you can't optimize for conversions without tracking
- **Test 5+ creative variations** — Outbrain auto-optimizes toward winners, but needs options
- **Review publisher performance daily** for the first week — block sites with high spend and no conversions
- **Separate mobile and desktop** — they have fundamentally different engagement patterns
- **Match content quality to publisher quality** — your content lives next to premium editorial; make it match
- **Scale gradually** — increase budgets by 20% per day maximum to maintain optimization

## Using the Reference Files

**`/references/campaign-setup-guide.md`** — Read when creating a new Outbrain campaign. Covers account structure, objective selection, budget allocation, and launch checklist.

**`/references/targeting-strategies.md`** — Read when configuring audience targeting. Covers geographic, device, publisher, interest, and custom audience strategies.

**`/references/content-optimization.md`** — Read when creating or testing ad creatives. Covers headline writing, image selection, A/B testing, and landing page alignment.

**`/references/performance-optimization.md`** — Read when optimizing running campaigns. Covers bid management, publisher analysis, scaling strategies, and conversion tracking.
