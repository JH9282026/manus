---
name: reddit-ads-management
description: "Programmatic campaign creation and management for Reddit advertising using Reddit Ads API. Covers campaign structure, objectives (awareness, traffic, conversions, video views), community targeting, interest targeting, and API authentication. Use for: automating Reddit ad campaigns, targeting subreddits, implementing interest-based targeting, managing budgets, and MCP/browser control integration for Reddit advertising."
---

# Reddit Ads Management

Programmatic campaign creation and management on Reddit using the Reddit Ads API for community-based advertising.

## Overview

Master the Reddit Ads API to automate advertising campaigns on Reddit's community-driven platform. This skill covers campaign structure, subreddit targeting, interest targeting, and automation workflows.

## API Authentication

### OAuth 2.0
```python
import requests

auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
data = {
    "grant_type": "password",
    "username": username,
    "password": password
}

response = requests.post(
    "https://www.reddit.com/api/v1/access_token",
    auth=auth,
    data=data,
    headers={"User-Agent": "YourApp/1.0"}
)

access_token = response.json()["access_token"]
```

## Campaign Creation

### Create Campaign
```python
url = f"https://ads-api.reddit.com/api/v2.0/accounts/{account_id}/campaigns"

headers = {
    "Authorization": f"Bearer {access_token}",
    "User-Agent": "YourApp/1.0"
}

data = {
    "name": "Spring Campaign 2026",
    "objective": "REACH",  # or TRAFFIC, CONVERSIONS, VIDEO_VIEWS
    "funding_instrument_id": funding_instrument_id,
    "daily_budget": 100.00,
    "total_budget": 3000.00,
    "start_date": "2026-04-01T00:00:00Z",
    "end_date": "2026-04-30T23:59:59Z"
}

response = requests.post(url, headers=headers, json=data)
```

## Subreddit Targeting

### Target Specific Subreddits
```python
ad_group_data = {
    "name": "Tech Subreddits",
    "campaign_id": campaign_id,
    "bid_value": 5.00,
    "targeting": {
        "subreddits": ["technology", "programming", "artificial"]
    }
}
```

## Interest Targeting

### Target by Interests
```python
targeting = {
    "interests": ["technology", "gaming", "fitness"]
}
```

## Using the Reference Files

**`/references/reddit-api-reference.md`** — Read for complete Ads API documentation and targeting options.

**`/references/reddit-targeting-guide.md`** — Read for subreddit selection strategies and community engagement best practices.

## References

- [Reddit Api Reference](references/reddit-api-reference.md)
