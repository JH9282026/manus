---
name: trade-desk-api-integration
description: "Integrate with The Trade Desk API for programmatic advertising automation. Use for: TTD API authentication, campaign management, audience segment targeting, bid optimization, conversion tracking, reporting API, inventory management, and building automated programmatic advertising workflows."
---

# Trade Desk API Integration

Programmatically manage The Trade Desk programmatic advertising campaigns through the TTD API for automated buying, targeting, and reporting at scale.

## Overview

The Trade Desk (TTD) is the largest independent demand-side platform (DSP), enabling programmatic buying across display, video, CTV, audio, native, and DOOH inventory. The TTD API provides full programmatic control over campaign management, audience targeting, bid strategy, creative management, and performance reporting. This skill covers API authentication, the campaign object hierarchy, core operations, and automation patterns.

## API Setup & Authentication

### Prerequisites
1. ☐ The Trade Desk advertiser or partner account
2. ☐ API access approved (request through TTD account team)
3. ☐ Partner ID or Advertiser ID
4. ☐ API authentication token

### Authentication

| Step | Method | Endpoint | Details |
|------|--------|----------|---------|
| 1. Authenticate | POST | `/v3/authentication` | Send login + password, receive token |
| 2. Use token | All requests | All `/v3/*` endpoints | `TTD-Auth: {token}` header |
| 3. Refresh | POST | `/v3/authentication` | Token expires, re-authenticate |

### Base URL and Headers

| Item | Value |
|------|-------|
| Production URL | `https://api.thetradedesk.com` |
| Sandbox URL | `https://apisb.thetradedesk.com` |
| Auth header | `TTD-Auth: {your_token}` |
| Content-Type | `application/json` |

## Campaign Object Hierarchy

```
Partner (Agency)
  └── Advertiser (Brand)
       └── Campaign (Budget, flight dates, frequency cap)
            └── Ad Group (Targeting, bidding, pacing)
                 └── Creative (Ad unit — display, video, native, audio)
```

## Core API Operations

| Operation | Method | Endpoint | Key Parameters | Reference |
|-----------|--------|----------|----------------|-----------|
| Create campaign | POST | `/v3/campaign` | AdvertiserId, name, budget, dates, frequency | `/references/campaign-operations.md` |
| Update campaign | PUT | `/v3/campaign` | CampaignId + fields to update | `/references/campaign-operations.md` |
| Create ad group | POST | `/v3/adgroup` | CampaignId, targeting, bid list, pacing | `/references/campaign-operations.md` |
| Set targeting | PUT | `/v3/adgroup` | RTBAttributes (geo, device, audience, context) | `/references/campaign-operations.md` |
| Assign creative | POST | `/v3/creative/assign` | AdGroupId, CreativeId | `/references/campaign-operations.md` |
| Get report | POST | `/v3/myreports/reportexecution/query/advertiser` | Date range, dimensions, metrics | `/references/reporting-analytics.md` |
| Audience management | POST | `/v3/thirdpartydata` | Segment selection, audience creation | `/references/campaign-operations.md` |

### Targeting Options

| Targeting Type | API Field | Options |
|---------------|-----------|---------|
| Geographic | GeoTargeting | Country, region, DMA, city, postal code |
| Device | DeviceTypeTargeting | Desktop, Mobile, Tablet, CTV |
| Operating system | OSTargeting | iOS, Android, Windows, macOS, Roku, Fire TV |
| Browser | BrowserTargeting | Chrome, Safari, Firefox, Edge |
| Audience segments | AudienceTargeting | 3rd party data, 1st party uploads, lookalike |
| Contextual | ContextualTargeting | IAB categories, keywords, brand safety |
| Inventory | InventoryTargeting | Deal IDs, exchange, supply source |
| Time of day | DayPartTargeting | Hour blocks, days of week |
| Frequency | FrequencyConfig | Max impressions per user per time period |
| Viewability | ViewabilityTargeting | Minimum viewability threshold |

## Bid Strategy Configuration

| Strategy | API Value | Description | Best For |
|----------|-----------|-------------|----------|
| Fixed CPM | FixedBid | Constant bid for all impressions | Direct deals, testing |
| Koa (auto-optimize) | KoaOptimized | TTD's ML-based bid optimization | Most campaigns |
| CPC optimized | CPCOptimized | Optimize toward click outcomes | Traffic campaigns |
| CPA optimized | CPAOptimized | Optimize toward conversion outcomes | Performance campaigns |
| ROAS optimized | ROASOptimized | Optimize toward return on ad spend | E-commerce |
| Viewability optimized | ViewabilityOptimized | Maximize viewable impressions | Brand campaigns |

## Reporting API

### Report Configuration

| Dimension | Metrics Available | Granularity |
|-----------|------------------|-------------|
| Campaign | Impressions, clicks, spend, conversions, video completes | Hourly, daily, weekly |
| Ad group | Same + targeting performance | Hourly, daily |
| Creative | CTR, completion rate, viewability | Daily |
| Site/domain | Publisher-level performance | Daily |
| Geo | Country, DMA, city performance | Daily |
| Device | Device type performance | Daily |
| Audience segment | Segment-level performance | Daily |

### Reporting Workflow
1. **Create report schedule** — POST to `/v3/myreports/reportschedule`
2. **Define dimensions and metrics** — specify breakdowns and KPIs
3. **Set date range** — absolute dates or relative (last 7 days)
4. **Execute report** — POST to `/v3/myreports/reportexecution/query/advertiser`
5. **Download results** — GET report file from provided URL (CSV format)

## Automation Patterns

### Budget Pacing Monitor

| Step | Action | Frequency |
|------|--------|-----------|
| 1. Pull spend data | GET campaign performance for today | Every 4 hours |
| 2. Calculate pacing | Compare actual spend vs. expected (budget × % of day elapsed) | After pull |
| 3. Alert on underpacing | If actual <80% of expected | Immediately |
| 4. Alert on overpacing | If actual >120% of expected | Immediately |
| 5. Adjust bid/budget | Increase/decrease bid modifiers | If pacing off by >20% |

### Audience Refresh Automation

| Step | Action | Trigger |
|------|--------|---------|
| 1. Export CRM segment | Pull latest customer segment from CDP | Weekly |
| 2. Hash identifiers | SHA-256 hash emails/phone numbers | Before upload |
| 3. Upload to TTD | POST first-party data segment | After hashing |
| 4. Update ad group targeting | PUT ad group with refreshed audience | After upload confirms |
| 5. Verify match rate | Check audience size vs. uploaded records | After 24 hours |

## Error Handling

| Error Code | Meaning | Resolution |
|-----------|---------|------------|
| 401 | Token expired | Re-authenticate |
| 403 | Permission denied | Check advertiser/partner access |
| 404 | Resource not found | Verify entity ID |
| 422 | Validation error | Review request body fields |
| 429 | Rate limited | Implement backoff (60 seconds) |
| 500 | Server error | Retry with exponential backoff |

## Best Practices

- **Use sandbox first** — test all API calls against `apisb.thetradedesk.com` before production
- **Leverage Koa optimization** — TTD's ML bidder outperforms manual bidding in most scenarios
- **Implement idempotency** — use unique request IDs to prevent duplicate campaign creation
- **Pull reports off-peak** — schedule report generation during non-business hours for faster processing
- **Monitor match rates** — low first-party data match rates indicate hashing or formatting issues
- **Version your integrations** — TTD updates API versions; plan for migration when new versions release

## Using the Reference Files

**`/references/api-authentication.md`** — Read when setting up API access. Covers authentication flow, token management, sandbox vs. production, and error handling.

**`/references/campaign-operations.md`** — Read when creating or managing campaigns. Covers campaign/ad group CRUD, targeting configuration, creative assignment, and budget management.

**`/references/automation-patterns.md`** — Read when building automated workflows. Covers pacing monitors, bid optimization bots, audience refresh, and creative rotation automation.

**`/references/reporting-analytics.md`** — Read when pulling performance data. Covers report types, scheduling, dimension/metric selection, and data processing patterns.
