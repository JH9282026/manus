---
name: amazon-dsp-programmatic
description: "Create programmatic display and video advertising campaigns using Amazon DSP (Demand-Side Platform) for reaching audiences on and off Amazon. Use for display advertising, video ads, audio ads, audience targeting, retargeting, lookalike audiences, programmatic buying, CPM bidding, and multi-channel brand awareness beyond Amazon marketplace."
---

# Amazon DSP Programmatic Advertising

Create programmatic display, video, and audio advertising campaigns across Amazon and third-party sites using Amazon DSP.

## Overview

This skill covers Amazon DSP campaign creation, audience targeting, creative formats, and programmatic optimization. Use it for brand awareness, consideration, and retargeting campaigns both on Amazon properties and across the open web.

## Amazon DSP vs. Sponsored Ads

| Feature | Sponsored Ads | Amazon DSP |
|---------|---------------|------------|
| **Inventory** | Amazon only | Amazon + third-party sites |
| **Billing** | CPC (cost-per-click) | CPM (cost-per-impression) |
| **Min Budget** | None | $10,000+ (managed service) |
| **Access** | Self-service | Self-service or managed |
| **Ad Formats** | Text, product ads | Display, video, audio |
| **Targeting** | Keywords, products | Audiences, contextual |

## Ad Formats

### Display Ads

**Sizes**:
- 300x250 (Medium Rectangle)
- 728x90 (Leaderboard)
- 160x600 (Wide Skyscraper)
- 300x600 (Half Page)
- 970x250 (Billboard)

**Placements**:
- Amazon.com (product pages, search results)
- IMDb, Twitch, Fire TV
- Third-party websites (programmatic)

### Video Ads

**Formats**:
- In-stream (pre-roll, mid-roll)
- Out-stream (in-feed, in-article)

**Specifications**:
- Length: 15-30 seconds
- Resolution: 1920x1080 (HD)
- File size: <500MB

**Placements**:
- Amazon.com
- IMDb, Twitch, Fire TV
- Third-party video sites

### Audio Ads

**Specifications**:
- Length: 10-30 seconds
- Format: MP3, 192kbps

**Placements**:
- Amazon Music (ad-supported tier)
- Third-party audio platforms

## Audience Targeting

### Amazon Audiences

| Audience Type | Description | Use Case |
|---------------|-------------|----------|
| **In-Market** | Users actively shopping for products | Conversion campaigns |
| **Lifestyle** | Interests and behaviors | Awareness |
| **Life Events** | Major life changes (moving, marriage) | Relevant products |
| **Remarketing** | Visited your products/Store | Re-engagement |

### Custom Audiences

**Pixel-Based**:
- Website visitors
- Product viewers
- Cart abandoners
- Past purchasers

**Lookalike Audiences**:
- Similar to your customers
- Similar to converters
- Similar to high-value customers

## Campaign Strategy

### Upper Funnel (Awareness)

**Objective**: Brand awareness, reach

**Targeting**:
- Lifestyle audiences
- Contextual (topics, categories)
- Broad demographics

**Creative**: Brand-focused, storytelling

**KPIs**: Impressions, reach, viewability

### Mid Funnel (Consideration)

**Objective**: Product consideration, engagement

**Targeting**:
- In-market audiences
- Competitor product viewers
- Category shoppers

**Creative**: Product benefits, comparisons

**KPIs**: CTR, engagement rate, Store visits

### Lower Funnel (Conversion)

**Objective**: Drive purchases

**Targeting**:
- Remarketing (product viewers, cart abandoners)
- Lookalike audiences (converters)
- High-intent in-market

**Creative**: Product-focused, offers, urgency

**KPIs**: ROAS, conversions, ACOS

## Bidding & Optimization

### Bidding Strategies

| Strategy | Goal | Use Case |
|----------|------|----------|
| **Fixed CPM** | Consistent cost | Brand awareness |
| **Dynamic CPM** | Optimize for conversions | Performance campaigns |

### Optimization Tactics

1. **Frequency Capping**: Limit impressions per user (3-5/day)
2. **Dayparting**: Show ads during high-performance hours
3. **Device Targeting**: Optimize by device performance
4. **Placement Optimization**: Exclude low-performing sites

## Performance Benchmarks

| Metric | Good Benchmark | Excellent |
|--------|----------------|-----------|
| **CTR** | 0.1-0.3% | >0.3% |
| **Viewability** | >60% | >70% |
| **ROAS** | 2-4x | >4x |
| **CPM** | $5-$15 | <$5 |

## Using the Reference Files

**`/references/amazon-dsp-setup.md`** — Read when setting up Amazon DSP campaigns, including account access, creative requirements, and audience configuration.

**`/references/dsp-audience-strategies.md`** — Read when building audience targeting strategies, including remarketing, lookalikes, and funnel-based targeting.

## References

- [Campaign Optimization Measurement](references/campaign-optimization-measurement.md)
- [Dsp Fundamentals Platform Overview](references/dsp-fundamentals-platform-overview.md)
- [Full Funnel Strategy Integration](references/full-funnel-strategy-integration.md)
- [Targeting Strategies Audience Segmentation](references/targeting-strategies-audience-segmentation.md)
