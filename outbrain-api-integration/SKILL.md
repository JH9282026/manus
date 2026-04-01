---
name: outbrain-api-integration
description: "Integrate with Outbrain Amplify API for programmatic campaign management. Use for: authenticating with Outbrain API (token-based auth), managing Marketer/Budget/Campaign/PromotedLink entities via API, creating and updating promoted links programmatically, retrieving performance data, automating campaign operations, and building systems for Outbrain advertising automation."
---

# Outbrain API Integration

Programmatic access to Outbrain Amplify API for automated campaign management.

## Overview

The Outbrain Amplify API provides RESTful endpoints for managing content promotion campaigns. This skill covers authentication, entity management (Marketer, Budget, Campaign, PromotedLink), and performance reporting.

## API Basics

**Base URL:** `https://api.outbrain.com/amplify/v0.1`

**Authentication:** Token-based
- Generate token via web interface or API
- Token valid for 30 days
- Include in `OB-TOKEN-V1` header

## Core Entities

- **Marketer**: Customer account
- **Budget**: Money allocation
- **Campaign**: Collection of promoted links
- **PromotedLink**: Individual content
- **PerformanceBy**: Analytics metrics

## Key Operations

**List Campaigns:**
```bash
GET /marketers/{marketer_id}/campaigns
```

**Create Campaign:**
```bash
POST /marketers/{marketer_id}/campaigns
```

**Create Promoted Link:**
```bash
POST /campaigns/{campaign_id}/promotedLinks
```

**Get Performance:**
```bash
GET /reports/marketers/{marketer_id}/periodicContent
```

## Rate Limits

- Authentication: 2 requests/hour
- Token usage: 30 requests/second
- Performance API: 10 requests/minute
- Realtime API: 50 requests/minute

## Using the Reference Files

**`/references/api-authentication.md`** — Read when implementing authentication or managing tokens.

**`/references/campaign-operations.md`** — Read when building campaign management workflows.

**`/references/promoted-links-management.md`** — Read when creating or managing promoted links via API.

**`/references/reporting-analytics.md`** — Read when extracting performance data or building dashboards.

## References

- [Api Authentication](references/api-authentication.md)
- [Campaign Operations](references/campaign-operations.md)
- [Promoted Links Management](references/promoted-links-management.md)
- [Reporting Analytics](references/reporting-analytics.md)
