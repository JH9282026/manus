---
name: taboola-api-integration
description: "Integrate with the Taboola Backstage API for programmatic native advertising management. Use for: Taboola API authentication, campaign CRUD operations, creative management, performance reporting, audience targeting via API, bid automation, and building automated native advertising workflows on Taboola's platform."
---

# Taboola API Integration

Programmatically manage Taboola Backstage native advertising campaigns through the Taboola API for automation, reporting, and optimization at scale.

## Overview

The Taboola Backstage API provides RESTful endpoints for managing native advertising campaigns across Taboola's content discovery network. It enables programmatic campaign creation, creative management, targeting configuration, bid automation, and performance reporting. This skill covers authentication, the API object model, core operations, reporting, and common automation patterns.

## API Setup & Authentication

### Prerequisites
1. ☐ Taboola Backstage advertiser account
2. ☐ API access approved (request through account manager)
3. ☐ Client ID and client secret credentials

### Authentication Flow (OAuth 2.0)

| Step | Method | Endpoint | Details |
|------|--------|----------|---------|
| 1. Request token | POST | `/backstage/oauth/token` | Client credentials grant, send client_id + client_secret |
| 2. Receive token | — | — | Access token with expiry (typically 1 hour) |
| 3. Use token | All requests | All `/backstage/api/*` endpoints | `Authorization: Bearer {token}` header |
| 4. Refresh token | POST | `/backstage/oauth/token` | Re-authenticate before expiry |

### Base URL and Configuration

| Item | Value |
|------|-------|
| Base URL | `https://backstage.taboola.com` |
| Auth endpoint | `/backstage/oauth/token` |
| API prefix | `/backstage/api/1.0` |
| Content-Type | `application/json` |
| Rate limits | ~100 requests/minute (varies by endpoint) |

## API Object Model

```
Account (Advertiser)
  └── Campaign
       ├── Campaign Item (Ad/Creative)
       └── Targeting Rules
```

## Core API Operations

| Operation | Method | Endpoint | Key Parameters | Reference |
|-----------|--------|----------|----------------|-----------|
| List campaigns | GET | `/backstage/api/1.0/{account_id}/campaigns/` | fetch_level, status filter | `/references/campaign-operations.md` |
| Create campaign | POST | `/backstage/api/1.0/{account_id}/campaigns/` | name, cpc, budget, country, platform | `/references/campaign-operations.md` |
| Update campaign | PUT | `/backstage/api/1.0/{account_id}/campaigns/{id}/` | Any campaign field | `/references/campaign-operations.md` |
| Get campaign items | GET | `/backstage/api/1.0/{account_id}/campaigns/{id}/items/` | campaign_id | `/references/creative-management.md` |
| Create campaign item | POST | `/backstage/api/1.0/{account_id}/campaigns/{id}/items/` | url, title, thumbnail_url | `/references/creative-management.md` |
| Update campaign item | PUT | `/backstage/api/1.0/{account_id}/campaigns/{id}/items/{item_id}/` | title, cpc, status | `/references/creative-management.md` |
| Get performance | GET | `/backstage/api/1.0/{account_id}/reports/campaign-summary/dimensions/campaign_day_breakdown` | start_date, end_date | `/references/reporting-analytics.md` |

## Campaign Configuration

### Required Campaign Fields

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| name | String | Campaign name | "Q3_ContentAmp_US_Desktop" |
| branding_text | String | Displayed as "by [brand]" | "Acme Corporation" |
| cpc | Float | Cost per click bid | 0.35 |
| spending_limit | Float | Daily budget | 100.00 |
| spending_limit_model | String | Budget model | "DAILY" |
| country_targeting | Object | Target countries | {"type": "INCLUDE", "value": ["US"]} |
| platform_targeting | Object | Target devices | {"type": "INCLUDE", "value": ["DESK"]} |

### Optional Campaign Settings

| Setting | Options | Default |
|---------|---------|---------|
| start_date | ISO date string | Immediately |
| end_date | ISO date string | No end (ongoing) |
| bid_strategy | "FIXED", "SMART", "TARGET_CPA" | "FIXED" |
| target_cpa | Float (if using TARGET_CPA) | — |
| publisher_targeting | INCLUDE/EXCLUDE + publisher list | All publishers |
| os_targeting | iOS, Android, Windows, Mac | All |
| browser_targeting | Chrome, Safari, Firefox, Edge | All |
| connection_type_targeting | WIFI, CELLULAR | All |

## Campaign Item (Creative) Structure

| Field | Required | Description | Constraints |
|-------|----------|-------------|-------------|
| url | Yes | Landing page URL | HTTPS, accessible, no redirects through blocked domains |
| title | Yes | Ad headline | 80 characters max, no excessive capitalization |
| thumbnail_url | Yes | Image URL | Min 400×350, JPEG/PNG, high quality |
| description | No | Ad description text | 150 characters max |
| cpc | No | Per-item CPC override | Overrides campaign CPC |
| status | No | Active status | "RUNNING", "PAUSED" |

## Reporting API

### Available Report Types

| Report | Endpoint Dimension | Breakdowns | Reference |
|--------|-------------------|-----------|-----------|
| Campaign summary | `campaign_day_breakdown` | By date, per campaign | `/references/reporting-analytics.md` |
| Campaign item (creative) | `item_day_breakdown` | By date, per creative | `/references/reporting-analytics.md` |
| Site (publisher) | `site_day_breakdown` | By publisher site | `/references/reporting-analytics.md` |
| Country | `country_day_breakdown` | By country | `/references/reporting-analytics.md` |
| Platform | `platform_day_breakdown` | By device type | `/references/reporting-analytics.md` |

### Available Metrics

| Metric | Description | Calculation |
|--------|-------------|-------------|
| impressions | Total impressions served | Count |
| clicks | Total clicks received | Count |
| spent | Total spend | Sum of CPC × clicks |
| ctr | Click-through rate | clicks / impressions |
| cpc | Average cost per click | spent / clicks |
| conversions | Conversion events | Count (requires pixel) |
| cpa | Cost per acquisition | spent / conversions |
| roas | Return on ad spend | revenue / spent |

### Report Query Parameters

| Parameter | Required | Description | Example |
|-----------|----------|-------------|---------|
| start_date | Yes | Report start date | "2026-01-01" |
| end_date | Yes | Report end date | "2026-01-31" |
| campaign | No | Filter by campaign ID | "campaign_123" |
| include_multi_conversions | No | Include view-through conversions | "true" |

## Automation Patterns

### Bid Optimization Bot

| Step | API Call | Logic |
|------|---------|-------|
| 1. Pull 7-day performance | GET campaign report | Per-campaign breakdown |
| 2. Calculate efficiency | Compute CPA per campaign/item | spent / conversions |
| 3. Adjust bids | PUT campaign/item with new CPC | If CPA > target × 1.2 → decrease CPC 10%; If CPA < target × 0.8 → increase CPC 10% |
| 4. Pause losers | PUT item status = "PAUSED" | If CTR < 0.03% after 10K impressions |
| 5. Log all changes | Record in database/spreadsheet | Track bid history for analysis |

### Creative Testing Pipeline

| Step | Action | Trigger |
|------|--------|---------|
| 1. Upload 5+ items per campaign | POST multiple campaign items | Campaign launch |
| 2. Monitor performance daily | GET item_day_breakdown report | Daily after 24 hours |
| 3. Pause underperformers | PUT status = PAUSED on low CTR items | CTR < 50% of campaign average after 5K impressions |
| 4. Promote winners | Increase CPC on high CTR items | CPC +10% for top performers |
| 5. Refresh creative weekly | POST new items, pause stale ones | Every 7–14 days |

### Publisher Optimization

| Action | Logic | Frequency |
|--------|-------|-----------|
| Pull site report | GET site_day_breakdown | Daily |
| Block poor publishers | PUT campaign with publisher exclusions | Sites with CPA > 3× target after $50+ spend |
| Whitelist top publishers | Create allow-list campaign for best sites | After 2 weeks of data |

## Error Handling

| HTTP Code | Meaning | Resolution |
|-----------|---------|------------|
| 401 | Token expired or invalid | Re-authenticate with OAuth |
| 403 | Insufficient permissions | Check account access level |
| 404 | Resource not found | Verify account/campaign/item IDs |
| 422 | Validation error | Check field constraints (title length, URL format) |
| 429 | Rate limit exceeded | Implement exponential backoff |
| 500 | Server error | Retry with backoff; contact support if persistent |

## Best Practices

- **Use OAuth token caching** — don't re-authenticate on every request; cache token until expiry
- **Implement pagination** — list endpoints may return partial results; always check for next page
- **Batch read operations** — pull full reports rather than making per-entity API calls
- **Handle rate limits gracefully** — implement exponential backoff with jitter
- **Use campaign naming conventions** — `{Quarter}_{Objective}_{Geo}_{Device}` for easy API filtering
- **Test in staging first** — create a small test campaign to validate your integration before scaling

## Using the Reference Files

**`/references/api-authentication.md`** — Read when setting up API access. Covers OAuth 2.0 flow, token management, and authentication troubleshooting.

**`/references/campaign-operations.md`** — Read when creating or managing campaigns. Covers campaign CRUD, targeting configuration, budget management, and bid strategy setup.

**`/references/creative-management.md`** — Read when managing campaign items (ads). Covers creative upload, title/image guidelines, status management, and bulk operations.

**`/references/reporting-analytics.md`** — Read when pulling performance data. Covers report types, available metrics, date handling, filtering, and data export patterns.
