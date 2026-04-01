---
name: microsoft-ads-api-integration
description: "Integrate with the Microsoft Advertising API (Bing Ads) for programmatic campaign management, reporting, and automation. Use for: Microsoft Ads API setup, Bing Ads campaign creation, keyword management, audience targeting, automated bidding, performance reporting, bulk operations, and Universal Event Tracking implementation."
---

# Microsoft Ads API Integration

Programmatically manage Microsoft Advertising (Bing Ads) campaigns through the Microsoft Advertising API for automation, reporting, and optimization at scale.

## Overview

The Microsoft Advertising API enables full programmatic control over search, shopping, and audience campaigns across Bing, Yahoo, AOL, and partner networks. This skill covers API authentication (OAuth 2.0), campaign CRUD operations, bulk management, reporting endpoints, Universal Event Tracking (UET), and SDK implementation. Microsoft Ads reaches 40%+ of US desktop search volume and often delivers 20–30% lower CPCs than Google Ads.

## API Setup & Authentication

### Prerequisites Checklist
1. ☐ Microsoft Advertising account (advertiser or agency)
2. ☐ Developer token (request via Microsoft Advertising portal)
3. ☐ Azure AD application registration (for OAuth 2.0)
4. ☐ Client ID and client secret from Azure AD
5. ☐ Redirect URI configured in Azure AD app

### Authentication Flow

| Step | Endpoint | Purpose |
|------|----------|---------|
| 1. Authorization | `https://login.microsoftonline.com/common/oauth2/v2.0/authorize` | Get authorization code |
| 2. Token exchange | `https://login.microsoftonline.com/common/oauth2/v2.0/token` | Exchange code for access/refresh tokens |
| 3. API calls | `https://campaign.api.bingads.microsoft.com/Api/Advertiser/CampaignManagement/v13/` | Use access token in header |
| 4. Token refresh | Same as step 2 | Use refresh token before expiry |

### SDK Options

| SDK | Language | Installation | Reference |
|-----|----------|-------------|-----------|
| BingAds Python SDK | Python | `pip install bingads` | `/references/sdk-implementation-guide.md` |
| BingAds .NET SDK | C# | NuGet package | `/references/sdk-implementation-guide.md` |
| BingAds Java SDK | Java | Maven package | `/references/sdk-implementation-guide.md` |
| BingAds PHP SDK | PHP | Composer package | `/references/sdk-implementation-guide.md` |
| REST API (no SDK) | Any | Direct HTTP calls | `/references/authentication-setup-guide.md` |

## Campaign Management API

### Object Hierarchy

```
Customer Account
  └── Campaign (budget, location targeting, network settings)
       └── Ad Group (default bid, audience signals)
            ├── Keyword (match type, bid)
            ├── Ad (RSA, DSA, multimedia)
            └── Ad Extension (sitelink, callout, structured snippet)
```

### Core API Operations

| Operation | Service | Method | Key Parameters |
|-----------|---------|--------|----------------|
| Create campaign | CampaignManagement | AddCampaigns | Name, budget, bid strategy, time zone |
| Create ad group | CampaignManagement | AddAdGroups | CampaignId, name, default bid, start/end date |
| Add keywords | CampaignManagement | AddKeywords | AdGroupId, text, match type, bid |
| Create RSA | CampaignManagement | AddAds | Headlines (3–15), descriptions (2–4), final URL |
| Add extensions | CampaignManagement | AddAdExtensions | AccountId, extension type, content |
| Set targeting | CampaignManagement | SetAdGroupCriterions | Location, age, gender, audience, device |
| Get performance | Reporting | SubmitGenerateReport | Report type, date range, columns |

### Bid Strategy Options

| Strategy | Goal | When to Use | Automation Level |
|----------|------|-------------|-----------------|
| Enhanced CPC | Balanced clicks + conversions | Starting out, testing | Semi-auto |
| Maximize Clicks | Maximum traffic | Awareness, new campaigns | Full auto |
| Maximize Conversions | Most conversions in budget | Mature campaigns with conversion data | Full auto |
| Target CPA | Specific cost per acquisition | 30+ conversions/month | Full auto |
| Target ROAS | Specific return on ad spend | E-commerce, revenue tracking | Full auto |
| Manual CPC | Full bid control | Granular optimization | Manual |

## Reporting API

### Report Types and Use Cases

| Report Type | Key Metrics | Use Case |
|-------------|-------------|----------|
| CampaignPerformance | Impressions, clicks, spend, conversions | Overall campaign health |
| KeywordPerformance | Keyword-level metrics, quality score | Keyword optimization |
| AdPerformance | Ad-level CTR, conversion rate | Ad copy testing |
| SearchQuery | Actual search terms triggering ads | Negative keyword discovery |
| AudiencePerformance | Audience segment metrics | Audience optimization |
| GeographicPerformance | Location-level data | Geo-targeting adjustments |
| ShareOfVoice | Impression share, lost IS | Competitive positioning |

### Reporting Workflow
1. **Define report request** — specify report type, columns, date range, and aggregation
2. **Submit request** — call `SubmitGenerateReport` (returns report request ID)
3. **Poll for completion** — call `PollGenerateReport` until status = "Success"
4. **Download report** — retrieve CSV/TSV from the returned URL
5. **Process data** — parse and load into analytics system

## Bulk Operations

| Approach | Best For | Max Records | Speed |
|----------|----------|-------------|-------|
| Standard API | <1,000 entities per call | 1,000 | Real-time |
| Bulk API | 1,000–4M entities | 4,000,000 | Batch (minutes–hours) |
| Google Import | Mirroring Google Ads campaigns | Full account | Automated sync |

### Bulk API Process
1. Download current entities (DownloadCampaignsByAccountIds)
2. Modify CSV file with changes
3. Upload modified file (GetBulkUploadUrl → upload → GetBulkUploadStatus)
4. Review results file for errors

## Universal Event Tracking (UET)

| Event Type | Tracking Method | Use Case |
|------------|----------------|----------|
| Page view | UET tag on all pages | Remarketing, audience building |
| Variable revenue | Custom event with revenue value | E-commerce ROAS tracking |
| Custom event | Event name + category + value | Form submissions, downloads |
| Offline conversions | Bulk upload via API | Call tracking, in-store |

### UET Setup Checklist
1. ☐ Create UET tag in Microsoft Advertising
2. ☐ Install UET JavaScript on all pages
3. ☐ Create conversion goals (destination URL, event, duration, or pages per visit)
4. ☐ Verify tag fires correctly (UET Tag Helper browser extension)
5. ☐ Set conversion window (default 30 days)
6. ☐ Enable auto-tagging for MSCLKID parameter

## API Rate Limits and Error Handling

| Limit Type | Threshold | Action |
|-----------|-----------|--------|
| Calls per minute | 80 per customer | Implement exponential backoff |
| Calls per hour | 3,000 per customer | Queue and throttle requests |
| Bulk upload size | 4M rows per file | Split into multiple uploads |
| Report polling | 1 poll per 30 seconds | Respect polling interval |

### Common Error Codes

| Code | Meaning | Resolution |
|------|---------|------------|
| 106 | Authentication failure | Refresh OAuth token |
| 1001 | Invalid campaign setting | Check required fields |
| 1030 | Budget too low | Increase daily budget |
| 2812 | Keyword limit reached | Remove paused keywords |
| 3220 | Ad policy violation | Review editorial guidelines |

## Best Practices

- **Import from Google Ads** — use the Google Import tool for quick account mirroring, then optimize for Microsoft
- **Leverage lower CPCs** — Microsoft Ads CPCs are typically 20–30% lower; allocate budget for testing
- **Use audience targeting aggressively** — LinkedIn profile targeting is exclusive to Microsoft Ads
- **Schedule reports** — set up automated daily/weekly report downloads for monitoring
- **Handle pagination** — always check for additional pages in API responses
- **Use bulk API for large changes** — avoid hitting rate limits with individual calls

## Using the Reference Files

**`/references/authentication-setup-guide.md`** — Read when setting up API access, OAuth 2.0 flow, or troubleshooting authentication errors.

**`/references/campaign-management-api.md`** — Read when creating or modifying campaigns, ad groups, keywords, or ads programmatically.

**`/references/reporting-automation.md`** — Read when building automated reporting pipelines or performance dashboards.

**`/references/sdk-implementation-guide.md`** — Read when implementing with Python, .NET, Java, or PHP SDKs.

**`/references/best-practices-troubleshooting.md`** — Read when optimizing API performance, handling errors, or debugging integration issues.
