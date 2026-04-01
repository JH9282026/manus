---
name: taboola-api-integration
description: "Integrate with Taboola Backstage API for programmatic campaign management. Use for: authenticating with Taboola API (OAuth 2.0), creating and managing campaigns via API, bulk operations, managing Items and Motion Ads programmatically, configuring targeting via API, retrieving performance reports, managing conversion rules and custom audiences, and building automated systems for Taboola advertising."
---

# Taboola API Integration

Programmatic access to Taboola Backstage API for automated campaign management.

## Overview

The Taboola Backstage API provides RESTful endpoints for managing native advertising campaigns programmatically. This skill covers authentication, campaign management, creative operations, targeting, and reporting.

## API Basics

**Base URL:** `https://backstage.taboola.com/backstage/api/1.0`

**Authentication:** OAuth 2.0 Client Credentials
- Get `client_id` and `client_secret` from account manager
- Token expires after 12 hours
- Include as Bearer token in requests

## Key Endpoints

### Campaigns
- `GET /{account_id}/campaigns/` - List campaigns
- `POST /{account_id}/campaigns/` - Create campaign
- `PUT /{account_id}/campaigns/{id}` - Update campaign
- `POST /{account_id}/campaigns/mass-update` - Bulk update

### Items (Creatives)
- `GET /{account_id}/campaigns/{id}/items/` - List items
- `POST /{account_id}/campaigns/{id}/items/` - Create item
- `POST /{account_id}/campaigns/{id}/items/mass-create` - Bulk create

### Reporting
- `GET /{account_id}/reports/campaign-summary/dimensions/{dimension}` - Campaign reports
- `GET /{account_id}/reports/realtime-campaign/dimensions/{dimension}` - Realtime data

## Common Operations

**Create Campaign:**
```json
{
  "name": "Campaign Name",
  "branding_text": "Brand",
  "cpc": 0.50,
  "daily_cap": 100.00,
  "country_targeting": {"type": "INCLUDE", "value": ["US"]}
}
```

**Create Item:**
```json
{
  "url": "https://example.com",
  "thumbnail_url": "https://cdn.example.com/image.jpg",
  "title": "Headline Text"
}
```

## Using the Reference Files

**`/references/api-authentication.md`** — Read when implementing OAuth 2.0 or managing tokens.

**`/references/campaign-operations.md`** — Read when building campaign management workflows.

**`/references/creative-management.md`** — Read when managing Items and Motion Ads via API.

**`/references/reporting-analytics.md`** — Read when extracting performance data or building dashboards.

## References

- [Api Authentication](references/api-authentication.md)
- [Campaign Operations](references/campaign-operations.md)
- [Creative Management](references/creative-management.md)
- [Reporting Analytics](references/reporting-analytics.md)
