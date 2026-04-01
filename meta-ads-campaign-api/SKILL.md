---
name: meta-ads-campaign-api
description: Create, manage, and automate Meta (Facebook/Instagram) advertising campaigns programmatically through the Meta Marketing API, covering the full campaign lifecycle from creation to reporting. Use for programmatic ad creation at scale, Meta Ads API integration, campaign structure automation, Advantage+ campaign setup, Ads Insights API reporting, budget and bid management via API, bulk ad operations, and Meta Business SDK implementation.
---

# Meta Ads Campaign API

Programmatically create, manage, and optimize Meta advertising campaigns across Facebook and Instagram using the Marketing API.

## Overview

The Meta Marketing API enables full programmatic control over the ad campaign hierarchy: Campaign → Ad Set → Ad. This skill covers API setup, campaign CRUD operations, the Advantage+ unified structure, Insights API for reporting, and automation best practices. All operations require an access token with `ads_management` permission.

## Campaign Object Hierarchy

```
Ad Account (act_{id})
├── Campaign (objective, budget, special_ad_categories)
│   ├── Ad Set (targeting, placement, schedule, optimization)
│   │   ├── Ad (creative + ad set binding)
│   │   └── Ad (creative + ad set binding)
│   └── Ad Set
│       └── Ad
└── Campaign
    └── Ad Set
        └── Ad
```

## API Setup Checklist

| Step | Action | Endpoint/Location |
|------|--------|-------------------|
| 1 | Create Meta Developer account | developers.facebook.com |
| 2 | Create app with "Business" use case | App Dashboard → Create App |
| 3 | Add Marketing API product | App Dashboard → Add Product |
| 4 | Generate System User token | Business Manager → System Users |
| 5 | Grant ad account permissions | `ads_management`, `ads_read`, `business_management` |
| 6 | Complete Business Verification | Required for Advanced Access |
| 7 | Test connection | `GET /me/adaccounts` |

## Core API Operations

### Create Campaign
```
POST /act_{ad_account_id}/campaigns
  name, objective, status, special_ad_categories,
  buying_type (AUCTION|RESERVED)
```

**Objectives (ODAX):** `OUTCOME_AWARENESS`, `OUTCOME_TRAFFIC`, `OUTCOME_ENGAGEMENT`, `OUTCOME_LEADS`, `OUTCOME_APP_PROMOTION`, `OUTCOME_SALES`

### Create Ad Set
```
POST /act_{ad_account_id}/adsets
  campaign_id, name, optimization_goal, billing_event,
  bid_strategy, daily_budget|lifetime_budget,
  targeting, start_time, end_time,
  promoted_object, attribution_spec
```

### Create Ad Creative
```
POST /act_{ad_account_id}/adcreatives
  name, object_story_spec: {
    page_id, link_data|video_data|photo_data
  }
```

### Create Ad
```
POST /act_{ad_account_id}/ads
  adset_id, creative: {creative_id}, name, status
```

## Advantage+ Unified Campaign Structure (2025)

Starting May 2025, Meta unified Advantage+ Shopping (ASC) and Advantage+ App (AAC) campaigns into a single creation flow:

| Aspect | Before (Legacy) | After (Unified) |
|--------|-----------------|------------------|
| Campaign creation | Separate ASC/AAC workflows | Single creation endpoint |
| Advantage+ status | Explicit campaign type | Auto-determined by settings |
| API version | v23.0 supports legacy | v24.0+ requires unified |
| Migration deadline | — | v25.0 (Q1 2026) mandatory |

**Key change:** Set `is_advantage_plus=true` and configure budget, audience, and placement — the system determines optimization automatically.

## Insights API for Reporting

```
GET /{object_id}/insights
  ?fields=impressions,reach,spend,clicks,actions,
    cost_per_action_type,cpm,cpc,ctr,roas
  &date_preset=last_30d
  &breakdowns=age,gender,publisher_platform,platform_position
  &time_increment=1  (daily)
  &level=ad
```

### Available Breakdowns

| Breakdown | Values | Use Case |
|-----------|--------|----------|
| `publisher_platform` | facebook, instagram, messenger, audience_network | Platform performance split |
| `platform_position` | feed, story, reels, right_column, search | Placement optimization |
| `age` | 18-24, 25-34, 35-44, etc. | Demographic analysis |
| `device_platform` | mobile, desktop | Device targeting decisions |
| `country` | ISO country codes | Geo performance analysis |

## Rate Limits and Error Handling

| Tier | Call Volume | How to Qualify |
|------|-----------|----------------|
| Development | 200 calls/hour | Default for new apps |
| Standard | ~200 calls/hour/ad account | Verified Business + active spend |
| Higher tiers | Request via support | Significant spend + API partner |

**Rate limit strategy:**
1. Check `x-business-use-case-usage` header on every response
2. Implement exponential backoff on HTTP 429
3. Batch read operations where possible (`?ids=id1,id2,id3`)
4. Use async reports for large data pulls

## Common Patterns

| Pattern | Implementation |
|---------|---------------|
| Bulk campaign creation | Loop POST with unique names; batch ≤50 per request |
| A/B testing | Create multiple ad sets under one campaign with different targeting |
| Budget optimization | Use Campaign Budget Optimization (CBO) with `daily_budget` at campaign level |
| Automated rules | `POST /act_{id}/adrules_library` for pause/scale based on KPIs |
| Preserve social proof | Reuse `effective_object_story_id` from existing post |

## Using the Reference Files

### When to Read Each Reference

**`/references/api-fundamentals-setup.md`** — Read when configuring API access for the first time, setting up authentication, or troubleshooting token issues.

**`/references/campaign-structure-management.md`** — Read when designing campaign hierarchy, creating ad sets with complex targeting, or implementing Advantage+ campaigns.

**`/references/automation-workflows.md`** — Read when building automated campaign management, implementing rules-based optimization, or scaling bulk operations.

**`/references/insights-reporting-api.md`** — Read when building reporting dashboards, pulling cross-platform breakdowns, or implementing async report jobs.

**`/references/best-practices-troubleshooting.md`** — Read when debugging API errors, handling rate limits, resolving creative rejections, or optimizing delivery.
