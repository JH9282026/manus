---
name: outbrain-api-integration
description: "Integrate with the Outbrain Amplify API for programmatic native advertising management. Use for: Outbrain API authentication, campaign CRUD operations, promoted link management, budget automation, performance reporting, audience targeting via API, and building automated native advertising workflows."
---

# Outbrain API Integration

Programmatically manage Outbrain Amplify native advertising campaigns through the Outbrain API for automation, reporting, and optimization at scale.

## Overview

The Outbrain Amplify API provides RESTful endpoints for managing native advertising campaigns across Outbrain's publisher network. It enables programmatic campaign creation, promoted link management, bid/budget automation, and performance reporting. This skill covers authentication, core API operations, reporting endpoints, and common automation patterns for building scalable native advertising workflows.

## API Setup & Authentication

### Prerequisites
1. ☐ Outbrain Amplify account (advertiser or agency)
2. ☐ API access enabled (request through account manager)
3. ☐ API credentials (username and password or token)

### Authentication Flow

| Step | Method | Endpoint | Details |
|------|--------|----------|---------|
| 1. Get token | GET | `/amplify/v2/login` | Basic Auth header with credentials |
| 2. Store token | — | — | Token returned in response, valid for session |
| 3. Use token | All requests | All endpoints | `OB-TOKEN-V1` header on every request |
| 4. Refresh | GET | `/amplify/v2/login` | Re-authenticate when token expires |

### Base URL and Headers

| Item | Value |
|------|-------|
| Base URL | `https://api.outbrain.com` |
| Auth header | `OB-TOKEN-V1: {your_token}` |
| Content-Type | `application/json` |
| Rate limits | Varies by endpoint, ~100 requests/minute |

## API Object Hierarchy

```
Marketer (Advertiser Account)
  └── Budget
       └── Campaign
            └── Promoted Link (Ad)
                 └── Promoted Link Sections (Targeting overrides)
```

## Core API Operations

| Operation | Method | Endpoint | Key Parameters | Reference |
|-----------|--------|----------|---------------|-----------|
| List campaigns | GET | `/amplify/v2/marketers/{id}/campaigns` | marketer_id, fetch type | `/references/campaign-operations.md` |
| Create campaign | POST | `/amplify/v2/marketers/{id}/campaigns` | name, budget, CPC, targeting | `/references/campaign-operations.md` |
| Update campaign | PUT | `/amplify/v2/campaigns/{id}` | Any campaign field | `/references/campaign-operations.md` |
| Pause/resume campaign | PUT | `/amplify/v2/campaigns/{id}` | enabled: true/false | `/references/campaign-operations.md` |
| Get promoted links | GET | `/amplify/v2/campaigns/{id}/promotedLinks` | campaign_id | `/references/promoted-links-management.md` |
| Create promoted link | POST | `/amplify/v2/campaigns/{id}/promotedLinks` | URL, title, image | `/references/promoted-links-management.md` |
| Update promoted link | PUT | `/amplify/v2/promotedLinks/{id}` | title, CPC, image URL | `/references/promoted-links-management.md` |
| Get performance | GET | `/amplify/v2/reports/marketers/{id}/periodic` | date range, breakdown | `/references/reporting-analytics.md` |
| Manage budgets | POST/PUT | `/amplify/v2/marketers/{id}/budgets` | amount, pacing, dates | `/references/campaign-operations.md` |

## Campaign Configuration Options

### Campaign Settings

| Setting | Options | Default | Notes |
|---------|---------|---------|-------|
| Objective | Traffic, Conversions, Awareness | Traffic | Determines optimization algorithm |
| CPC bid | $0.01–$10.00+ | — | Minimum varies by geo |
| Daily budget | $10+ | — | Per campaign |
| Targeting - Geo | Country, region, DMA, city | All | ISO country codes |
| Targeting - Platform | Desktop, Mobile, Tablet | All | Separate or combined |
| Targeting - OS | iOS, Android, Windows, Mac | All | Within platform |
| Targeting - Browser | Chrome, Safari, Firefox, Edge | All | Within platform |
| Publisher blocking | Block specific publisher IDs | None | Exclude poor performers |
| Schedule | Start/end dates, day-parting | Always on | UTC timestamps |

### Promoted Link (Ad) Structure

| Field | Required | Description | Constraints |
|-------|----------|-------------|-------------|
| url | Yes | Landing page URL | Must be accessible, HTTPS preferred |
| text | Yes | Ad headline | 80 characters max, no excessive caps |
| imageUrl | Yes | Thumbnail image URL | Min 400×260, JPEG/PNG |
| enabled | No | Active status | true/false, default true |
| cpc | No | Per-link CPC override | Overrides campaign CPC |
| sectionName | No | Targeting override | Publisher-level targeting |

## Reporting API

### Available Reports

| Report Type | Endpoint | Breakdowns Available |
|------------|----------|---------------------|
| Periodic performance | `/reports/marketers/{id}/periodic` | Daily, weekly, monthly |
| Campaign performance | `/reports/campaigns/{id}/periodic` | By date range |
| Promoted link performance | `/reports/promotedLinks/{id}/periodic` | By date range |
| Publisher performance | `/reports/campaigns/{id}/publishers/periodic` | By publisher site |
| Geo performance | `/reports/campaigns/{id}/geo/periodic` | By country/region |
| Platform performance | `/reports/campaigns/{id}/platforms/periodic` | By device type |

### Key Metrics Available

| Metric | Description | Use Case |
|--------|-------------|----------|
| impressions | Total ad impressions | Reach measurement |
| clicks | Total clicks | Traffic volume |
| spend | Total spend | Budget tracking |
| cpc | Average cost per click | Efficiency metric |
| ctr | Click-through rate | Creative performance |
| conversions | Conversion events (if pixel installed) | ROI measurement |
| cpa | Cost per acquisition | Conversion efficiency |

## Automation Patterns

### Bid Optimization Bot

| Step | Action | Frequency |
|------|--------|-----------|
| 1. Pull performance | GET campaign report for last 7 days | Daily |
| 2. Calculate metrics | Compute CPA, CTR, ROAS per campaign/link | After pull |
| 3. Apply rules | If CPA > target → reduce CPC 10%; If CPA < target × 0.7 → increase CPC 10% | After calculation |
| 4. Update bids | PUT updated CPC values | After rules applied |
| 5. Log changes | Record all bid adjustments with reasons | Every change |

### Creative Rotation Automation

| Step | Action | Trigger |
|------|--------|---------|
| 1. Launch with 5+ promoted links | POST multiple links per campaign | Campaign start |
| 2. Monitor CTR daily | GET promoted link performance | Daily, after 1,000 impressions |
| 3. Pause underperformers | PUT enabled=false on links with CTR <50% of average | After 3 days |
| 4. Add fresh creative | POST new promoted links to replace paused | Weekly |
| 5. Refresh images | PUT new imageUrl on existing links | Every 2 weeks |

### Publisher Optimization

| Action | API Call | Threshold |
|--------|----------|-----------|
| Identify poor publishers | GET publisher report | CPA >2× target or CTR <0.05% |
| Block publisher | PUT campaign with blockedPublishers | After 3 days of poor performance |
| Whitelist top publishers | PUT campaign with allowedPublishers | For high-value campaigns |

## Error Handling

| HTTP Code | Meaning | Action |
|-----------|---------|--------|
| 401 | Authentication expired | Re-authenticate, get new token |
| 403 | Insufficient permissions | Check API access level |
| 404 | Resource not found | Verify ID exists |
| 422 | Validation error | Check request body against API docs |
| 429 | Rate limit exceeded | Implement exponential backoff |
| 500 | Server error | Retry with backoff, contact support if persistent |

## Best Practices

- **Authenticate once per session** — don't re-authenticate on every request; cache the token
- **Use bulk operations** — batch promoted link creation/updates rather than individual calls
- **Implement retry logic** — transient errors (500, 429) should be retried with exponential backoff
- **Pull reports at off-peak hours** — reporting endpoints are slower during business hours
- **Version your automation scripts** — track changes to bid rules and targeting logic in source control
- **Monitor API changes** — Outbrain updates endpoints; subscribe to developer changelog

## Using the Reference Files

**`/references/api-authentication.md`** — Read when setting up API access or troubleshooting authentication. Covers credential management, token lifecycle, and session handling.

**`/references/campaign-operations.md`** — Read when creating or modifying campaigns and budgets. Covers campaign CRUD, budget management, targeting configuration, and scheduling.

**`/references/promoted-links-management.md`** — Read when managing ads (promoted links). Covers link creation, image requirements, headline optimization, and bulk operations.

**`/references/reporting-analytics.md`** — Read when pulling performance data. Covers report types, metric definitions, date handling, and data export patterns.
