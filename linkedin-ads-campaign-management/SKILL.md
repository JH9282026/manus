---
name: linkedin-ads-campaign-management
description: "Programmatic campaign creation and management for LinkedIn advertising using LinkedIn Marketing API. Covers campaign structure (Account → Campaign Group → Campaign → Creative), objectives (awareness, consideration, conversions), budget management, bidding strategies, and API authentication. Use for: automating LinkedIn ad campaigns, creating campaign hierarchies via API, managing budgets programmatically, implementing bidding strategies, scheduling campaigns, batch operations, and MCP/browser control integration for LinkedIn advertising."
---

# LinkedIn Ads Campaign Management

Programmatic campaign creation and management on LinkedIn using the LinkedIn Marketing API for automated B2B advertising deployment.

## Overview

Master the LinkedIn Marketing API to automate advertising campaigns on the world's largest professional network. This skill covers the four-tier campaign structure, OAuth 2.0 authentication, budget management, bidding strategies, and automation workflows for agentic AI deployment.

## Campaign Hierarchy

| Level | Purpose | Key Parameters |
|-------|---------|----------------|
| **Ad Account** | Top container | Billing, currency |
| **Campaign Group** | Budget grouping | Total budget, schedule |
| **Campaign** | Objective & targeting | Objective, audience, bid |
| **Creative** | Ad content | Format, copy, media |

## API Authentication

### OAuth 2.0 Setup
```python
import requests

# Authorization URL
auth_url = f"https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id={client_id}&redirect_uri={redirect_uri}&scope=r_ads%20rw_ads%20r_ads_reporting"

# Exchange code for token
token_url = "https://www.linkedin.com/oauth/v2/accessToken"
payload = {
    "grant_type": "authorization_code",
    "code": authorization_code,
    "redirect_uri": redirect_uri,
    "client_id": client_id,
    "client_secret": client_secret
}

response = requests.post(token_url, data=payload)
access_token = response.json()["access_token"]
```

### API Endpoints
- **Base URL**: `https://api.linkedin.com/rest/`
- **Version**: LinkedIn Marketing API v2

## Campaign Objectives

| Category | Objectives | Use Case |
|----------|-----------|----------|
| **Awareness** | BRAND_AWARENESS | Brand exposure |
| **Consideration** | WEBSITE_VISITS, ENGAGEMENT, VIDEO_VIEWS | Traffic, engagement |
| **Conversions** | LEAD_GENERATION, WEBSITE_CONVERSIONS, JOB_APPLICANTS | Leads, sales, hiring |

## Campaign Group Creation

### Create Campaign Group
```python
import requests

url = "https://api.linkedin.com/rest/adCampaignGroupsV2"

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
    "X-Restli-Protocol-Version": "2.0.0",
    "LinkedIn-Version": "202403"
}

data = {
    "account": f"urn:li:sponsoredAccount:{account_id}",
    "name": "Q2 2026 Campaigns",
    "status": "DRAFT",
    "runSchedule": {
        "start": 1711929600000,  # Unix timestamp in milliseconds
        "end": 1719705600000
    },
    "totalBudget": {
        "amount": "5000",
        "currencyCode": "USD"
    }
}

response = requests.post(url, headers=headers, json=data)
campaign_group_id = response.json()["id"]
```

## Campaign Creation

### Create Campaign
```python
url = "https://api.linkedin.com/rest/adCampaignsV2"

data = {
    "account": f"urn:li:sponsoredAccount:{account_id}",
    "campaignGroup": campaign_group_id,
    "name": "Tech Decision Makers - US",
    "type": "SPONSORED_UPDATES",  # or SPONSORED_INMAILS, TEXT_ADS, DYNAMIC_ADS
    "costType": "CPM",  # or CPC
    "objectiveType": "LEAD_GENERATION",
    "offsiteDeliveryEnabled": False,
    "status": "DRAFT",
    "targetingCriteria": {
        "include": {
            "and": [
                {
                    "or": {
                        "urn:li:adTargetingFacet:titles": ["urn:li:title:100"]  # CTO
                    }
                },
                {
                    "or": {
                        "urn:li:adTargetingFacet:locations": ["urn:li:geo:103644278"]  # US
                    }
                }
            ]
        }
    },
    "dailyBudget": {
        "amount": "100",
        "currencyCode": "USD"
    }
}

response = requests.post(url, headers=headers, json=data)
campaign_id = response.json()["id"]
```

## Campaign Types

| Type | Description | Use Case |
|------|-------------|----------|
| **SPONSORED_UPDATES** | Native feed ads | Content promotion |
| **SPONSORED_INMAILS** | Direct messages | Personalized outreach |
| **TEXT_ADS** | Right rail ads | Budget-friendly awareness |
| **DYNAMIC_ADS** | Personalized ads | Follower growth, engagement |

## Bidding Strategies

### Cost Types
- **CPM**: Cost per 1000 impressions
- **CPC**: Cost per click
- **CPV**: Cost per view (video)
- **CPS**: Cost per send (InMail)

### Bid Amount
```python
data = {
    "unitCost": {
        "amount": "15.00",  # $15 CPM or CPC
        "currencyCode": "USD"
    }
}
```

### Automated Bidding
```python
data = {
    "optimizationTargetType": "LEAD_GENERATION",  # Let LinkedIn optimize
    "costType": "CPM"
}
```

## Budget Management

### Daily Budget
```python
data = {
    "dailyBudget": {
        "amount": "200",
        "currencyCode": "USD"
    }
}
```

### Total Budget (Campaign Group Level)
```python
data = {
    "totalBudget": {
        "amount": "10000",
        "currencyCode": "USD"
    }
}
```

## Creative Creation

### Sponsored Content (Single Image)
```python
url = "https://api.linkedin.com/rest/adCreativesV2"

data = {
    "campaign": campaign_id,
    "type": "SPONSORED_STATUS_UPDATE",
    "reference": share_urn,  # LinkedIn share URN
    "status": "DRAFT"
}

response = requests.post(url, headers=headers, json=data)
```

### Sponsored InMail
```python
data = {
    "campaign": campaign_id,
    "type": "SPONSORED_INMAIL",
    "variables": {
        "data": {
            "com.linkedin.ads.SponsoredInMailCreativeVariables": {
                "subject": "Exclusive Invitation",
                "body": "Hi {{firstName}}, we'd like to invite you...",
                "callToAction": {
                    "text": "Learn More",
                    "url": "https://example.com"
                }
            }
        }
    }
}
```

## Status Management

### Status Values
- `DRAFT`: Not running
- `ACTIVE`: Running
- `PAUSED`: Temporarily stopped
- `ARCHIVED`: Permanently stopped
- `COMPLETED`: Ended naturally

### Update Status
```python
url = f"https://api.linkedin.com/rest/adCampaignsV2/{campaign_id}"

data = {
    "patch": {
        "$set": {
            "status": "ACTIVE"
        }
    }
}

response = requests.post(url, headers=headers, json=data)
```

## Batch Operations

### Batch Create Campaigns
```python
campaigns = [
    {"name": "Campaign 1", "targetingCriteria": {...}},
    {"name": "Campaign 2", "targetingCriteria": {...}}
]

for camp in campaigns:
    response = requests.post(
        "https://api.linkedin.com/rest/adCampaignsV2",
        headers=headers,
        json=camp
    )
```

## Rate Limits

- **Standard**: 500 requests per day per app
- **Throttle**: 100 requests per minute
- **Best Practice**: Implement exponential backoff

## Automation Workflows

### Budget Optimizer
```python
def optimize_linkedin_budgets(account_id, campaigns):
    for campaign in campaigns:
        stats = get_campaign_analytics(campaign["id"])
        
        if stats["ctr"] > 0.5 and stats["conversion_rate"] > 0.02:
            # High performer, increase budget 20%
            new_budget = float(campaign["dailyBudget"]["amount"]) * 1.2
            update_campaign_budget(campaign["id"], new_budget)
```

## Using the Reference Files

**`/references/linkedin-api-reference.md`** — Read for complete Marketing API documentation, all endpoints, request/response schemas, error codes, and advanced features.

**`/references/linkedin-campaign-structure.md`** — Read for campaign architecture best practices, budget allocation strategies, objective selection, and scaling approaches.

**`/references/linkedin-automation-patterns.md`** — Read when implementing automated campaign management, performance-based optimization, and MCP integration workflows.
