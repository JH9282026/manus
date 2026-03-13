---
name: tiktok-ads-management
description: "Programmatic campaign creation and management for TikTok advertising using TikTok Marketing API. Covers campaign structure, objectives (reach, traffic, app installs, conversions, video views), creative formats, targeting options, and API authentication. Use for: automating TikTok ad campaigns, creating video ads, implementing interest targeting, managing budgets, and MCP/browser control integration for TikTok advertising."
---

# TikTok Ads Management

Programmatic campaign creation and management on TikTok using the TikTok Marketing API for short-form video advertising.

## Overview

Master the TikTok Marketing API to automate advertising campaigns on TikTok's viral video platform. This skill covers campaign structure, video creative requirements, targeting, and automation workflows.

## API Authentication

### OAuth 2.0
```python
import requests

# Authorization URL
auth_url = f"https://business-api.tiktok.com/open_api/v1.3/oauth2/authorize/?app_id={app_id}&redirect_uri={redirect_uri}&state={state}"

# Exchange code for token
token_url = "https://business-api.tiktok.com/open_api/v1.3/oauth2/access_token/"

data = {
    "app_id": app_id,
    "secret": app_secret,
    "auth_code": auth_code
}

response = requests.post(token_url, json=data)
access_token = response.json()["data"]["access_token"]
```

## Campaign Creation

### Create Campaign
```python
url = "https://business-api.tiktok.com/open_api/v1.3/campaign/create/"

headers = {
    "Access-Token": access_token
}

data = {
    "advertiser_id": advertiser_id,
    "campaign_name": "Spring Video Campaign",
    "objective_type": "CONVERSIONS",  # or REACH, TRAFFIC, APP_INSTALL, VIDEO_VIEWS
    "budget_mode": "BUDGET_MODE_DAY",
    "budget": 100.00
}

response = requests.post(url, headers=headers, json=data)
```

## Video Creative Specs

### TikTok Video Requirements
- **Aspect Ratio**: 9:16 (vertical), 1:1 (square), 16:9 (horizontal)
- **Resolution**: 720x1280 minimum (9:16), 1080x1920 recommended
- **Duration**: 5-60 seconds (9-15 seconds optimal)
- **File Size**: Max 500 MB
- **Format**: MP4, MOV, MPEG, AVI

## Targeting Options

### Demographics
```python
targeting = {
    "age_groups": ["AGE_18_24", "AGE_25_34"],
    "gender": "GENDER_UNLIMITED",  # or MALE, FEMALE
    "languages": ["en"]
}
```

### Interests
```python
targeting = {
    "interest_category_ids": [10001, 10002, 10003]
}
```

## Using the Reference Files

**`/references/tiktok-api-reference.md`** — Read for complete Marketing API documentation and creative specifications.

**`/references/tiktok-creative-guide.md`** — Read for video best practices, trending formats, and performance optimization.
