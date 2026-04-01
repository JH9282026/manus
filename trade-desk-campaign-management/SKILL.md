---
name: trade-desk-campaign-management
description: "Plan and manage programmatic advertising campaigns on The Trade Desk DSP platform. Use for: campaign setup, audience targeting strategy, bid optimization, creative management, inventory selection, frequency capping, performance reporting, and cross-channel programmatic buying across display, video, CTV, audio, and native."
---

# Trade Desk Campaign Management

Plan, launch, and optimize programmatic advertising campaigns on The Trade Desk (TTD) demand-side platform across display, video, CTV, audio, and native channels.

## Overview

The Trade Desk is the largest independent DSP, providing access to 600+ billion daily ad impressions across every digital channel. Unlike walled garden platforms (Google, Meta), TTD offers objective, cross-channel buying with full transparency into inventory sources, audience data, and bidding mechanics. This skill covers campaign planning, audience strategy, bid optimization, creative management, and performance analysis using TTD's platform.

## Campaign Planning Framework

| Decision | Options | Considerations | Reference |
|----------|---------|---------------|-----------|
| Channel | Display, Video, CTV, Audio, Native, DOOH | Match channel to campaign objective and audience behavior | `/references/campaign-setup-guide.md` |
| Objective | Awareness (CPM), Consideration (CPC/CPCV), Conversion (CPA) | Determines bid strategy and optimization | `/references/campaign-setup-guide.md` |
| Budget | Daily or lifetime, per campaign | Min $50/day recommended for learning | `/references/bidding-strategies.md` |
| Flight dates | Start/end dates, always-on | Seasonal vs. evergreen | `/references/campaign-setup-guide.md` |
| Frequency cap | Impressions per user per day/week/campaign | 3–5/day display, 1–2/day video typical | `/references/campaign-setup-guide.md` |
| Geography | Country, region, DMA, city, postal code | Layer with audience for precision | `/references/targeting-strategies.md` |

## Channel Selection Guide

| Channel | Inventory | Ad Format | Avg. CPM | Best For | Reference |
|---------|-----------|-----------|----------|----------|-----------|
| Display | Websites, apps | Banner, rich media | $2–$8 | Retargeting, reach, prospecting | `/references/campaign-setup-guide.md` |
| Online Video | Pre/mid-roll on web | 15s/30s video | $10–$25 | Brand awareness, product demos | `/references/creative-management.md` |
| CTV | Streaming apps (Hulu, Peacock, Pluto) | 15s/30s non-skip | $20–$40 | Brand awareness, reach at scale | `/references/campaign-setup-guide.md` |
| Audio | Spotify, podcasts, streaming radio | 15s/30s audio + companion | $8–$15 | Brand awareness, commuter reach | `/references/campaign-setup-guide.md` |
| Native | In-feed content recommendations | Headline + image + URL | $3–$10 | Content marketing, lead gen | `/references/creative-management.md` |
| DOOH | Digital billboards, screens | Static or video | $5–$15 | Local awareness, event targeting | `/references/campaign-setup-guide.md` |

## Audience Strategy

### Data Source Hierarchy

| Data Source | Quality | Scale | Cost | Example |
|------------|---------|-------|------|---------|
| 1st party (your data) | Highest | Limited | Free | CRM uploads, website visitors, app users |
| 2nd party (partner data) | High | Medium | Negotiated | Data marketplace deals |
| 3rd party (data providers) | Variable | Largest | CPM surcharge | Oracle/BlueKai, Lotame, LiveRamp |
| Contextual | Good proxy | Very large | Low–Medium | IAB category, keyword targeting |
| Lookalike/modeled | Medium–High | Large | Varies | TTD-built similar audiences |

### Audience Layering Strategy

| Layer | Purpose | Example |
|-------|---------|---------|
| Base: Demo/Geo | Broad audience foundation | US, 25–54, HHI $75K+ |
| Add: Behavioral | Refine by interests and actions | In-market for enterprise software |
| Add: Contextual | Target relevant content environments | Pages about cloud computing |
| Add: 1st party | Highest-intent audiences | Visited pricing page in last 30 days |
| Exclude: Converters | Don't waste budget on existing customers | Exclude CRM customer list |
| Exclude: Low-quality | Remove non-human or mismatched traffic | Brand safety + fraud filters |

## Bid Strategy Selection

| Strategy | How It Works | Best For | Data Requirement | Reference |
|----------|-------------|----------|------------------|-----------|
| Fixed CPM | Set price for all impressions | Direct deals, guaranteed inventory | None | `/references/bidding-strategies.md` |
| Koa (ML-optimized) | TTD's AI adjusts bids per impression | Most campaigns | 50+ conversions for CPA optimization | `/references/bidding-strategies.md` |
| CPC-optimized | Bids to maximize clicks | Traffic campaigns | Click data | `/references/bidding-strategies.md` |
| CPA-optimized | Bids to achieve target CPA | Performance campaigns | 50+ conversions in learning period | `/references/bidding-strategies.md` |
| ROAS-optimized | Bids to achieve target return | E-commerce | Revenue tracking implemented | `/references/bidding-strategies.md` |

### Pacing Options

| Pacing Type | Behavior | When to Use |
|------------|----------|-------------|
| Even (ASAP) | Spend evenly through flight | Default for most campaigns |
| Front-loaded | Spend more early in flight | New product launches, time-sensitive |
| Flight-optimized | ML distributes spend for best performance | Longer flights with conversion goals |

## Creative Management

### Creative Specs Quick Reference

| Format | Dimensions | File Type | Max Size | Duration |
|--------|-----------|-----------|----------|----------|
| Display banner | 300×250, 728×90, 160×600, 300×600, 320×50 | JPG, PNG, GIF, HTML5 | 200KB (static), 2MB (HTML5) | — |
| Video (standard) | 16:9 (1920×1080 preferred) | MP4, MOV | 100MB | 15s or 30s |
| CTV | 16:9 (1920×1080) | MP4 | 100MB | 15s or 30s (non-skippable) |
| Audio | — | MP3, WAV | 10MB | 15s or 30s |
| Native | 1200×627 image + headline (90 chars) + description (150 chars) | JPG, PNG | 1MB | — |

### Creative Best Practices
- **Align creative to funnel stage** — awareness uses brand video; retargeting uses product-specific display
- **Version by audience** — different creative for prospecting vs. retargeting
- **Rotate 3–5 creatives** per ad group to prevent fatigue
- **Include clear CTA** — "Learn More", "Shop Now", "Get Demo"
- **CTV creative must work without clicks** — include brand, CTA verbal instruction, QR code optional

## Performance Optimization Workflow

| Week | Focus | Actions | KPIs to Monitor |
|------|-------|---------|-----------------|
| 1 | Launch + learn | All audiences active, broad targeting, full creative set | Impressions, CTR, viewability |
| 2 | Analyze + refine | Review site, audience, creative performance | CTR, CPC, conversion rate |
| 3 | Optimize | Pause underperformers, increase bids on winners | CPA, ROAS, conversion volume |
| 4+ | Scale | Expand winning audiences, test new creative, increase budgets | CPA at scale, total conversions |
| Monthly | Refresh | New creative, updated audiences, competitive review | Trend analysis, fatigue indicators |

## Key Performance Metrics

| Metric | Formula | Benchmark (Display) | Benchmark (Video/CTV) |
|--------|---------|--------------------|-----------------------|
| CTR | Clicks / Impressions | 0.08–0.15% | 0.5–1.5% (video) |
| CPC | Spend / Clicks | $1–$5 | $5–$15 |
| CPM | (Spend / Impressions) × 1,000 | $2–$8 | $20–$40 (CTV) |
| CPA | Spend / Conversions | Varies by vertical | Varies |
| ROAS | Revenue / Spend | 3:1+ for e-commerce | — |
| Viewability | Viewable impressions / Measured impressions | >70% | >80% (video) |
| Completion rate | Video completes / Video starts | — | >70% (CTV), >50% (web video) |

## Best Practices

- **Start with Koa optimization** — TTD's ML bidder outperforms manual bidding in 90%+ of cases
- **Layer audiences, don't isolate** — combine demo + behavioral + contextual for precision
- **Set realistic frequency caps** — 3–5/day for display, 1–2/day for video prevents fatigue and waste
- **Use first-party data first** — highest quality, lowest cost, best performance
- **Separate CTV from web video** — different inventory, different performance patterns
- **Review supply path optimization** — ensure you're buying through the most efficient exchange paths

## Using the Reference Files

**`/references/campaign-setup-guide.md`** — Read when planning a new campaign. Covers campaign structure, channel selection, flight settings, frequency, and budget allocation.

**`/references/targeting-strategies.md`** — Read when building audience targeting. Covers data sources, audience layering, contextual targeting, and geo-targeting strategies.

**`/references/bidding-strategies.md`** — Read when configuring bids and pacing. Covers Koa optimization, CPA/ROAS goals, pacing options, and bid troubleshooting.

**`/references/creative-management.md`** — Read when managing ad creative. Covers specs, A/B testing, creative rotation, dynamic creative optimization, and format-specific best practices.
