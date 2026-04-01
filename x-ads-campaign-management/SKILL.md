---
name: x-ads-campaign-management
description: "Programmatic campaign creation and management for X (Twitter) advertising using X Ads API. Covers campaign hierarchy (Account → Campaign → Line Item → Promoted Tweet), objectives (awareness, consideration, conversion), budget management, scheduling, bidding strategies, and API authentication. Use for: automating X ad campaigns, setting up campaign structures via API, managing budgets programmatically, implementing bidding strategies, scheduling campaigns, batch campaign operations, and MCP/browser control integration for X advertising."
---

# X (Twitter) Ads Campaign Management

Programmatic campaign creation and management on X (formerly Twitter) using the X Ads API for automated ad deployment and optimization.

## Overview

Master the X Ads API to programmatically manage advertising campaigns across X platform. This skill covers the complete four-tier campaign hierarchy, OAuth 2.0 authentication, budget management, bidding strategies, and automation workflows for agentic AI deployment.

## Campaign Hierarchy

| Level | Purpose | Key Parameters |
|-------|---------|----------------|
| **Ad Account** | Top container | Funding instruments, timezone |
| **Campaign** | Objective grouping | Objective, budget, schedule |
| **Line Item** | Targeting & bidding | Bid amount, placements, optimization |
| **Promoted Tweet** | Ad creative | Tweet ID, status |

## API Authentication

### OAuth 2.0 Setup
```python
import requests

# Token endpoint
auth_url = "https://api.twitter.com/2/oauth2/token"

# Credentials
payload = {
    "grant_type": "client_credentials"
}

response = requests.post(
    auth_url,
    auth=(client_id, client_secret),
    data=payload
)

access_token = response.json()["access_token"]
```

### API Endpoints
- **Production**: `https://ads-api.x.com/12/`
- **Sandbox**: `https://ads-api-sandbox.x.com/12/`

## Campaign Objectives

| Category | Objectives | Use Case |
|----------|-----------|----------|
| **Awareness** | REACH, VIDEO_VIEWS | Brand awareness, video content |
| **Consideration** | ENGAGEMENT, FOLLOWERS, WEBSITE_CLICKS, APP_INSTALLS | Engagement, growth, traffic |
| **Conversion** | WEBSITE_CONVERSIONS, APP_INSTALLS (with tracking) | Sales, app downloads |

## Campaign Creation Workflow

### 1. Create Campaign
```python
campaign_data = {
    "name": "Q2 Product Launch",
    "funding_instrument_id": "funding_id",
    "daily_budget_amount_local_micro": 50000000,  # $50
    "currency": "USD",
    "objective": "WEBSITE_CLICKS",
    "start_time": "2026-04-01T00:00:00Z",
    "end_time": "2026-06-30T23:59:59Z",
    "standard_delivery": True
}

response = requests.post(
    f"https://ads-api.x.com/12/accounts/{account_id}/campaigns",
    headers={"Authorization": f"Bearer {token}"},
    json=campaign_data
)
```

### 2. Create Line Item (Ad Group)
```python
line_item_data = {
    "name": "Tech Enthusiasts - Desktop",
    "campaign_id": campaign_id,
    "bid_amount_local_micro": 2000000,  # $2
    "bid_type": "MAX",
    "bid_unit": "IMPRESSION",
    "placements": ["ALL_ON_TWITTER"],
    "objective": "WEBSITE_CLICKS",
    "optimization": "WEBSITE_CLICKS"
}
```

### 3. Promote Tweet
```python
promoted_tweet_data = {
    "line_item_id": line_item_id,
    "tweet_ids": ["1234567890123456789"]
}
```

## Budget Management

### Budget Types
- **Daily Budget**: `daily_budget_amount_local_micro` (in micros: 1M = $1)
- **Total Budget**: `total_budget_amount_local_micro` (lifetime cap)

### Pacing
- **Standard Delivery**: Even distribution over time
- **Accelerated**: Spend as fast as possible

## Bidding Strategies

| Strategy | Type | Description |
|----------|------|-------------|
| **MAX** | Manual | Maximum bid per unit |
| **TARGET** | Auto | Target cost per action |
| **AUTO** | Auto | Automatic optimization |

### Bid Units
- `IMPRESSION`: CPM (cost per 1000 impressions)
- `ENGAGEMENT`: Cost per engagement
- `LINK_CLICK`: Cost per click
- `APP_CLICK`: Cost per app click

## Placements

- `ALL_ON_TWITTER`: All X placements
- `PUBLISHER_NETWORK`: X Audience Platform
- `TWITTER_TIMELINE`: Home timeline
- `TWITTER_PROFILE`: Profile pages
- `TWITTER_SEARCH`: Search results

## Status Management

### Campaign Status
- `ACTIVE`: Running
- `PAUSED`: Temporarily stopped
- `DRAFT`: Not launched

### Update Status
```python
requests.put(
    f"https://ads-api.x.com/12/accounts/{account_id}/campaigns/{campaign_id}",
    headers=headers,
    json={"entity_status": "PAUSED"}
)
```

## Batch Operations

Create multiple campaigns in sequence:
```python
campaigns = [
    {"name": "Campaign 1", "objective": "REACH", ...},
    {"name": "Campaign 2", "objective": "ENGAGEMENT", ...}
]

for camp in campaigns:
    response = requests.post(endpoint, headers=headers, json=camp)
```

## Rate Limits

- **Standard**: 1,000 requests per 15 minutes per account
- **Best Practice**: Implement exponential backoff for 429 errors

## Automation Workflows

### Budget Optimizer
```python
def optimize_budgets(account_id, campaigns):
    for campaign in campaigns:
        stats = get_campaign_stats(campaign["id"])
        
        if stats["ctr"] > 2.0:
            # Increase budget 20%
            new_budget = int(campaign["daily_budget"] * 1.2)
            update_campaign_budget(campaign["id"], new_budget)
```

## Using the Reference Files

**`/references/x-ads-api-reference.md`** — Read for complete API endpoint documentation, request/response schemas, error codes, and advanced features like conversion tracking and audience targeting.

**`/references/x-ads-automation-patterns.md`** — Read when implementing automated campaign management workflows, optimization rules, performance monitoring, and integration with MCP servers or browser control systems.

**`/references/x-ads-best-practices.md`** — Read for campaign structure recommendations, budget allocation strategies, bidding optimization techniques, and troubleshooting common API issues.

## References

- [Ad Formats And Creative Strategies](references/ad-formats-and-creative-strategies.md)
- [Budgeting Bidding And Optimization](references/budgeting-bidding-and-optimization.md)
- [Fundamentals And Core Concepts](references/fundamentals-and-core-concepts.md)
- [Targeting And Audience Strategies](references/targeting-and-audience-strategies.md)
- [Tools Platforms And Api](references/tools-platforms-and-api.md)
