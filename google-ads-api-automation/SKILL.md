---
name: google-ads-api-automation
description: "Automate Google Ads campaign management using Google Ads API v23+ for programmatic control. Use for bulk campaign creation, automated bid adjustments, performance reporting, keyword management, ad creation at scale, budget optimization, conversion tracking setup, and custom automation workflows for agencies and large advertisers."
---

# Google Ads API Automation

Programmatically manage Google Ads campaigns at scale using Google Ads API v23+ for automation and custom integrations.

## Overview

This skill covers Google Ads API authentication, campaign management, bulk operations, reporting, and automation workflows. Use it for managing large accounts, building custom tools, agency automation, and integrating Google Ads with external systems.

## API Access & Authentication

### Requirements
- **Google Ads Account** with API access
- **Developer Token** from Google Ads
- **OAuth 2.0 Credentials** from Google Cloud Console
- **Manager Account** (recommended for agencies)

### Authentication Setup

**OAuth 2.0 Flow**:
1. Create Google Cloud Project
2. Enable Google Ads API
3. Create OAuth 2.0 credentials
4. Generate refresh token
5. Configure google-ads.yaml

### API Client Libraries

| Language | Library | Documentation |
|----------|---------|---------------|
| Python | google-ads | Most popular, comprehensive |
| Java | google-ads-java | Enterprise-grade |
| PHP | google-ads-php | Web integration |
| .NET | google-ads-dotnet | Windows/Azure |
| Ruby | google-ads-ruby | Rails integration |

## Common Automation Use Cases

| Use Case | Complexity | Value |
|----------|------------|-------|
| **Automated Reporting** | Low | High - Daily performance dashboards |
| **Bid Automation** | Medium | High - Real-time bid adjustments |
| **Bulk Campaign Creation** | Medium | High - Launch 100s of campaigns |
| **Keyword Management** | Medium | Medium - Auto-add/pause keywords |
| **Budget Pacing** | High | High - Optimize spend across campaigns |
| **Custom Alerts** | Low | Medium - Performance notifications |

## Key API Operations

### Campaign Management
- Create/update/delete campaigns
- Manage budgets
- Set bidding strategies
- Configure targeting

### Ad Group Operations
- Create ad groups
- Set bids
- Manage keywords
- Add/remove ads

### Reporting
- Performance metrics
- Search terms
- Auction insights
- Custom reports

## Using the Reference Files

**`/references/api-authentication-setup.md`** — Read when setting up API access, including OAuth configuration, client library installation, and authentication troubleshooting.

**`/references/automation-workflows.md`** — Read when building automation scripts, including bid management, reporting automation, and bulk operations.

## References

- [Advanced Use Cases](references/advanced-use-cases.md)
- [Api Fundamentals Authentication](references/api-fundamentals-authentication.md)
- [Bid Management Automation](references/bid-management-automation.md)
- [Campaign Management Automation](references/campaign-management-automation.md)
- [Reporting Analytics Scripts](references/reporting-analytics-scripts.md)
