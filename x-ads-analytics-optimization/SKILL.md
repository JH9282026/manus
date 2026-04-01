---
name: x-ads-analytics-optimization
description: Analyze and optimize X (formerly Twitter) advertising campaigns using the X Ads API, covering campaign analytics, performance metrics, audience insights, and optimization strategies. Use for X Ads API analytics integration, Twitter ad campaign reporting, X ads performance optimization, X conversion tracking setup, X promoted tweets management, X audience analytics, X ads bid optimization, and X ads A/B testing frameworks.
---

# X Ads Analytics & Optimization

Analyze performance and optimize X (formerly Twitter) advertising campaigns using the X Ads API.

## Overview

The X Ads API provides programmatic access to create, manage, and analyze advertising campaigns on the X platform. This skill focuses on the analytics and optimization layer: pulling performance data, interpreting metrics, optimizing bids and targeting, A/B testing, and implementing conversion tracking for measurable results.

## X Ads API Access Tiers

| Tier | Monthly Cost | Ads API Access | Rate Limits |
|------|-------------|---------------|-------------|
| Free | $0 | No | 500 posts/month; minimal read |
| Basic | $200 | Limited | Higher request rates |
| Pro | $5,000 | Full | Robust rate limits |
| Enterprise | $42,000+ | Full + priority | Custom limits |

**Ads API access requires an approved Ads API developer application** with an active ad account.

## Campaign Structure

```
Funding Instrument (payment method)
└── Campaign (objective, budget, status)
    └── Line Item (targeting, bid, placement, creative type)
        └── Promoted Tweet / Creative (the ad content)
```

## Core Analytics Endpoints

| Endpoint | Method | Purpose |
|----------|--------|--------|
| `/stats/accounts/{id}` | GET | Account-level metrics |
| `/stats/campaigns/{id}` | GET | Campaign performance |
| `/stats/line_items/{id}` | GET | Line item (ad group) metrics |
| `/stats/promoted_tweets/{id}` | GET | Individual ad metrics |
| Async analytics | POST+GET | Segmented/bulk analytics jobs |

### Analytics Request Best Practices

1. **Always include `start_time` and `end_time`** — required for all stats requests
2. **Use `HOUR` granularity** — allows flexible aggregation; roll up to daily/weekly as needed
3. **Request `ALL_ON_TWITTER` placement** — ensures data for all placements is captured
4. **Avoid pulling data older than 7 days** — fresher data is more reliable and faster to retrieve
5. **Use async endpoints for segmented data** — synchronous endpoints don't support breakdowns

## Key Performance Metrics

| Metric | Definition | Good Benchmark |
|--------|-----------|----------------|
| Impressions | Times ad shown | Volume indicator |
| Engagements | Likes, retweets, replies, clicks | 1-3% engagement rate |
| Link clicks | Clicks to external URL | 0.5-1.5% CTR |
| CPE | Cost per engagement | $0.30-1.50 |
| CPC | Cost per link click | $0.50-3.00 |
| CPM | Cost per 1,000 impressions | $5-12 |
| Video views | 3s+ video views | 15-30% view rate |
| CPCV | Cost per completed video view | $0.02-0.08 |
| Conversion rate | Conversions / clicks | 1-3% |
| ROAS | Revenue / ad spend | 3-5× target |

## Campaign Objectives and Optimization

| Objective | Optimize For | Bid Type | Key Metric |
|-----------|-------------|----------|------------|
| Reach | Max impressions | CPM / Auto | CPM, Reach |
| Engagements | Max engagements | CPE / Auto | Engagement rate, CPE |
| Traffic | Link clicks | CPC / Auto | CTR, CPC |
| Video Views | Video views | CPV / Auto | View rate, CPCV |
| App Installs | Installs | CPI / Target CPA | CPI, Install rate |
| Conversions | Website conversions | CPA / Auto | Conversion rate, ROAS |
| Followers | New followers | CPF / Auto | Cost per follower |

## Conversion Tracking Setup

### X Pixel Implementation
1. **Install base pixel** on all website pages via `<script>` tag
2. **Configure event codes** for key actions (Purchase, AddToCart, Lead, SignUp)
3. **Verify pixel fires** using X Pixel Helper browser extension
4. **Create website tags** in Ads Manager to associate events with campaigns

### Conversions API (Server-Side)
1. **Generate Events API Key** in X Ads Manager
2. **Send events server-to-server** with hashed user data (email, phone)
3. **Include click ID** (`twclid`) for attribution matching
4. **Deduplicate** browser pixel + server events using `event_id`

## Optimization Strategies

### Bid Optimization
| Scenario | Action |
|----------|--------|
| Underspending with good results | Increase bid 10-20% to win more auctions |
| Overspending with poor results | Switch to manual bid with cap |
| Good CTR but low conversions | Check landing page; tighten audience |
| High CPM, low reach | Broaden targeting or increase bid |
| Strong results, want to scale | Increase budget 20% every 3-4 days |

### Audience Optimization
1. **Use Tailored Audiences** — upload CRM lists for retargeting (hashed email/device IDs)
2. **Follower Lookalikes** — target users similar to your followers or competitors' followers
3. **Conversation targeting** — reach users discussing specific topics (unique to X)
4. **Keyword targeting** — target based on recent tweets and searches
5. **Event targeting** — real-time targeting around live events and trends

### Creative Optimization
1. **Test 3-5 tweet variations per line item** — X auto-optimizes to best performer
2. **Use conversational copy** — questions and polls drive 2-3× engagement
3. **Include media always** — tweets with video get 10× engagement; images get 3×
4. **Keep copy concise** — 70-100 characters optimal; leave room for engagement
5. **Test Trend Takeover** — premium placement for major launches/events

## A/B Testing Framework

| Element | How to Test | Duration |
|---------|------------|----------|
| Creative | Multiple promoted tweets in one line item | 7-14 days |
| Audience | Separate line items with different targeting | 7-14 days |
| Bid strategy | Auto vs manual bid in parallel line items | 5-7 days |
| Objective | Separate campaigns with different objectives | 14-21 days |
| Landing page | Same ad, different destination URLs | 7-14 days |

## Using the Reference Files

### When to Read Each Reference

**`/references/01-x-ads-fundamentals.md`** — Read when setting up X Ads API access, understanding the campaign structure, or reviewing available ad formats.

**`/references/02-x-ads-key-metrics-kpis.md`** — Read when defining measurement frameworks, selecting KPIs for campaign goals, or benchmarking performance.

**`/references/03-x-ads-optimization-strategies.md`** — Read when optimizing underperforming campaigns, implementing bid adjustments, or refining audience targeting.

**`/references/04-x-ads-analytics-tools.md`** — Read when integrating X analytics with external tools, building dashboards, or implementing automated reporting.

**`/references/05-x-ads-advanced-strategies.md`** — Read when implementing advanced tactics like event targeting, trend exploitation, or multi-platform attribution.
