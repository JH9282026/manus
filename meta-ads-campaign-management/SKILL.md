---
name: meta-ads-campaign-management
description: "Programmatic campaign creation and management for Meta (Facebook/Instagram) advertising using Meta Marketing API. Covers campaign structure (Campaign → Ad Set → Ad), objectives (awareness, traffic, engagement, leads, sales), budget optimization (CBO), bidding strategies, placement options, and API authentication. Use for: automating Meta ad campaigns, creating campaign hierarchies via API, implementing Campaign Budget Optimization, managing ad sets programmatically, scheduling campaigns, batch operations, and MCP/browser control integration for Meta advertising platforms."
---

# Meta Ads Campaign Management

Programmatic campaign creation and management for Meta platforms (Facebook, Instagram, Messenger, Audience Network) using the Meta Marketing API.

## Overview

Master the Meta Marketing API to automate advertising across Facebook and Instagram. This skill covers the three-tier campaign structure, Graph API authentication, Campaign Budget Optimization (CBO), bidding strategies, and automation workflows for agentic AI deployment.

## Campaign Hierarchy

| Level | Purpose | Key Parameters |
|-------|---------|----------------|
| **Campaign** | Objective & budget | Objective, CBO settings, status |
| **Ad Set** | Targeting & schedule | Audience, placement, bid strategy, budget |
| **Ad** | Creative | Image/video, copy, CTA, link |

## API Authentication

### Access Token Generation
```python
import requests

# App-level token (for testing)
access_token = "YOUR_ACCESS_TOKEN"

# User access token via OAuth
# Redirect user to:
auth_url = f"https://www.facebook.com/v19.0/dialog/oauth?client_id={app_id}&redirect_uri={redirect_uri}&scope=ads_management,ads_read"

# Exchange code for token
token_url = f"https://graph.facebook.com/v19.0/oauth/access_token?client_id={app_id}&client_secret={app_secret}&redirect_uri={redirect_uri}&code={code}"
```

### API Endpoints
- **Base URL**: `https://graph.facebook.com/v19.0/`
- **Ad Account**: `act_{ad_account_id}`

## Campaign Objectives

| Category | Objectives | Use Case |
|----------|-----------|----------|
| **Awareness** | BRAND_AWARENESS, REACH | Brand exposure |
| **Traffic** | LINK_CLICKS, LANDING_PAGE_VIEWS | Website visits |
| **Engagement** | POST_ENGAGEMENT, PAGE_LIKES, EVENT_RESPONSES | Social engagement |
| **Leads** | LEAD_GENERATION, MESSAGES | Lead capture |
| **Sales** | CONVERSIONS, PRODUCT_CATALOG_SALES | Purchases, app installs |

## Campaign Creation

### Create Campaign
```python
import requests

url = f"https://graph.facebook.com/v19.0/act_{ad_account_id}/campaigns"

params = {
    "access_token": access_token,
    "name": "Spring Sale 2026",
    "objective": "OUTCOME_SALES",  # Updated objective format
    "status": "PAUSED",
    "special_ad_categories": []  # Required field
}

response = requests.post(url, params=params)
campaign_id = response.json()["id"]
```

### Campaign Budget Optimization (CBO)
```python
params = {
    "name": "CBO Campaign",
    "objective": "OUTCOME_SALES",
    "status": "PAUSED",
    "daily_budget": 5000,  # $50 (in cents)
    "bid_strategy": "LOWEST_COST_WITHOUT_CAP",
    "special_ad_categories": []
}
```

## Ad Set Creation

### Basic Ad Set
```python
url = f"https://graph.facebook.com/v19.0/act_{ad_account_id}/adsets"

params = {
    "access_token": access_token,
    "name": "US Adults 25-45",
    "campaign_id": campaign_id,
    "daily_budget": 2000,  # $20
    "billing_event": "IMPRESSIONS",
    "optimization_goal": "LINK_CLICKS",
    "bid_amount": 150,  # $1.50 bid cap
    "targeting": json.dumps({
        "geo_locations": {"countries": ["US"]},
        "age_min": 25,
        "age_max": 45
    }),
    "status": "PAUSED"
}

response = requests.post(url, params=params)
adset_id = response.json()["id"]
```

### Placement Options
```python
"targeting": json.dumps({
    "publisher_platforms": ["facebook", "instagram"],
    "facebook_positions": ["feed", "right_hand_column", "instant_article", "marketplace"],
    "instagram_positions": ["stream", "story", "explore", "reels"]
})
```

## Budget Management

### Budget Types

| Type | Level | Description |
|------|-------|-------------|
| **Campaign Budget Optimization** | Campaign | Meta distributes budget across ad sets |
| **Ad Set Budget** | Ad Set | Manual budget per ad set |
| **Daily Budget** | Campaign/Ad Set | Spend per day |
| **Lifetime Budget** | Campaign/Ad Set | Total spend over date range |

### Update Budget
```python
url = f"https://graph.facebook.com/v19.0/{campaign_id}"

params = {
    "access_token": access_token,
    "daily_budget": 10000  # $100
}

requests.post(url, params=params)
```

## Bidding Strategies

| Strategy | Description | Use Case |
|----------|-------------|----------|
| **LOWEST_COST_WITHOUT_CAP** | Automatic bidding | Maximum volume |
| **LOWEST_COST_WITH_BID_CAP** | Bid cap | Control costs |
| **COST_CAP** | Target cost | Stable CPA |
| **LOWEST_COST_WITH_MIN_ROAS** | Minimum ROAS | Profitability focus |

### Bid Strategy Implementation
```python
# Bid cap
"bid_strategy": "LOWEST_COST_WITH_BID_CAP",
"bid_amount": 200  # $2 max bid

# Cost cap
"bid_strategy": "COST_CAP",
"bid_amount": 500  # $5 target CPA

# Min ROAS
"bid_strategy": "LOWEST_COST_WITH_MIN_ROAS",
"bid_amount": 250  # 2.5x ROAS minimum
```

## Scheduling

### Campaign Schedule
```python
import datetime

start_time = datetime.datetime(2026, 4, 1, 0, 0, 0)
end_time = datetime.datetime(2026, 6, 30, 23, 59, 59)

params = {
    "start_time": start_time.isoformat(),
    "end_time": end_time.isoformat(),
    "lifetime_budget": 500000  # $5000 total
}
```

### Ad Set Dayparting
```python
# Run ads only on weekdays, 9 AM - 5 PM
adset_schedule = [
    {"day": 1, "start_minute": 540, "end_minute": 1020},  # Monday
    {"day": 2, "start_minute": 540, "end_minute": 1020},  # Tuesday
    {"day": 3, "start_minute": 540, "end_minute": 1020},  # Wednesday
    {"day": 4, "start_minute": 540, "end_minute": 1020},  # Thursday
    {"day": 5, "start_minute": 540, "end_minute": 1020}   # Friday
]

params = {
    "adset_schedule": json.dumps(adset_schedule)
}
```

## Status Management

### Status Values
- `ACTIVE`: Running
- `PAUSED`: Stopped
- `DELETED`: Archived
- `ARCHIVED`: Permanently removed

### Update Status
```python
# Pause campaign
requests.post(
    f"https://graph.facebook.com/v19.0/{campaign_id}",
    params={"access_token": access_token, "status": "PAUSED"}
)

# Activate ad set
requests.post(
    f"https://graph.facebook.com/v19.0/{adset_id}",
    params={"access_token": access_token, "status": "ACTIVE"}
)
```

## Batch Operations

### Batch API Request
```python
batch_requests = [
    {"method": "POST", "relative_url": f"act_{ad_account_id}/campaigns", "body": "name=Campaign1&objective=OUTCOME_SALES&status=PAUSED"},
    {"method": "POST", "relative_url": f"act_{ad_account_id}/campaigns", "body": "name=Campaign2&objective=OUTCOME_TRAFFIC&status=PAUSED"}
]

response = requests.post(
    "https://graph.facebook.com/v19.0/",
    params={
        "access_token": access_token,
        "batch": json.dumps(batch_requests)
    }
)
```

## Optimization Goals

| Goal | Description | Billing Event |
|------|-------------|---------------|
| **LINK_CLICKS** | Website clicks | IMPRESSIONS or LINK_CLICKS |
| **LANDING_PAGE_VIEWS** | Page loads | IMPRESSIONS |
| **IMPRESSIONS** | Ad views | IMPRESSIONS |
| **REACH** | Unique users | IMPRESSIONS |
| **OFFSITE_CONVERSIONS** | Pixel events | IMPRESSIONS |
| **LEAD_GENERATION** | Lead form submissions | IMPRESSIONS |
| **VALUE** | Purchase value | IMPRESSIONS |

## Rate Limits

- **Ad Account**: 200 calls per hour per account
- **User**: 200 calls per hour per user
- **App**: 200 calls per hour per app

**Best Practice**: Use batch API for multiple operations

## Automation Workflows

### Auto-Scale Winners
```python
def scale_top_performers(ad_account_id, min_roas=2.0):
    # Get all active ad sets
    adsets = get_adsets(ad_account_id, status="ACTIVE")
    
    for adset in adsets:
        insights = get_adset_insights(adset["id"])
        
        roas = insights["purchase_roas"][0]["value"]
        
        if float(roas) > min_roas:
            # Increase budget 20%
            current_budget = int(adset["daily_budget"])
            new_budget = int(current_budget * 1.2)
            
            update_adset_budget(adset["id"], new_budget)
```

## Using the Reference Files

**`/references/meta-api-reference.md`** — Read for complete Marketing API documentation, all endpoints, request/response formats, error codes, and advanced features like dynamic creative and automated rules.

**`/references/meta-campaign-structure-guide.md`** — Read for campaign architecture best practices, CBO vs ad set budgets, objective selection, and scaling strategies.

**`/references/meta-automation-patterns.md`** — Read when implementing automated campaign management, performance-based optimization, budget reallocation, and MCP integration workflows.
