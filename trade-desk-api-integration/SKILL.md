---
name: trade-desk-api-integration
description: "Integrate with The Trade Desk API for programmatic campaign automation. Use for: authenticating with TTD API, managing Partner/Advertiser/Campaign/AdGroup entities programmatically, automating campaign creation and updates, retrieving cross-channel performance data, implementing custom bid logic, and building systems for programmatic advertising automation at scale."
---

# The Trade Desk API Integration

Programmatic access to The Trade Desk API for automated campaign management.

## Overview

The Trade Desk API provides comprehensive endpoints for managing programmatic advertising campaigns across multiple channels. This skill covers authentication, campaign hierarchy management, automated operations, and cross-channel reporting.

## API Basics

**Base URL:** `https://api.thetradedesk.com/v3`

**Documentation:** `https://api.thetradedesk.com/v3/portal/api/doc`

**Authentication:** API credentials from account manager

## Campaign Hierarchy

- **Partner**: `/partner/{partnerId}`
- **Advertiser**: `/advertiser/{advertiserId}`
- **Campaign**: `/campaign/{campaignId}`
- **Ad Group**: `/adgroup/{adGroupId}`

## Key Operations

**Get Campaign:**
```bash
GET /campaign/{campaignId}
```

**Create Campaign:**
```bash
POST /advertiser/{advertiserId}/campaign
```

**Get Ad Group:**
```bash
GET /adgroup/{adGroupId}
```

**Create Ad Group:**
```bash
POST /campaign/{campaignId}/adgroup
```

## Automation Use Cases

- Campaign creation with default settings
- Bulk campaign updates
- Automated bid adjustments
- Performance-based optimization
- Cross-channel budget allocation
- Custom reporting dashboards

## Using the Reference Files

**`/references/api-authentication.md`** — Read when implementing API authentication or managing credentials.

**`/references/campaign-operations.md`** — Read when building campaign automation workflows.

**`/references/reporting-analytics.md`** — Read when extracting performance data or building cross-channel dashboards.

**`/references/automation-patterns.md`** — Read when implementing advanced automation or optimization algorithms.

## References

- [Api Authentication](references/api-authentication.md)
- [Automation Patterns](references/automation-patterns.md)
- [Campaign Operations](references/campaign-operations.md)
- [Reporting Analytics](references/reporting-analytics.md)
