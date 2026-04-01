---
name: snapchat-ads-api-automation
description: "Automate Snapchat advertising using the Snapchat Marketing API for programmatic campaign management, creative automation, and reporting. Use for API authentication, creating campaigns and ad squads via API, managing AR Lens campaigns programmatically, audience targeting automation, conversion measurement, real-time reporting, and building custom Snapchat ad tools."
---

# Snapchat Ads API Automation

Automate Snapchat advertising using the Snapchat Marketing API for programmatic campaign management.

## Overview

The Snapchat Marketing API (Ads API) enables programmatic management of Snapchat advertising, including campaign creation, AR Lens deployment, audience targeting, and performance measurement.

## API Authentication

### OAuth 2.0 Setup
```python
import requests

# Step 1: Get authorization code (manual, one-time)
auth_url = "https://accounts.snapchat.com/login/oauth2/authorize"
params = {
    "client_id": client_id,
    "redirect_uri": redirect_uri,
    "response_type": "code",
    "scope": "snapchat-marketing-api"
}

# Step 2: Exchange code for access token
token_url = "https://accounts.snapchat.com/login/oauth2/access_token"
data = {
    "grant_type": "authorization_code",
    "code": authorization_code,
    "client_id": client_id,
    "client_secret": client_secret,
    "redirect_uri": redirect_uri
}
response = requests.post(token_url, data=data)
access_token = response.json()["access_token"]
refresh_token = response.json()["refresh_token"]
```

## Campaign Management

### Create Campaign
```python
url = f"https://adsapi.snapchat.com/v1/adaccounts/{ad_account_id}/campaigns"
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}
payload = {
    "campaigns": [{
        "name": "Spring Campaign 2026",
        "ad_account_id": ad_account_id,
        "status": "ACTIVE",
        "objective": "WEBSITE_CONVERSIONS",
        "daily_budget_micro": 10000000  # $10
    }]
}
response = requests.post(url, json=payload, headers=headers)
campaign_id = response.json()["campaigns"][0]["campaign"]["id"]
```

### Create Ad Squad
```python
url = f"https://adsapi.snapchat.com/v1/campaigns/{campaign_id}/adsquads"
payload = {
    "adsquads": [{
        "name": "Women 18-24 | Beauty",
        "campaign_id": campaign_id,
        "type": "SNAP_ADS",
        "status": "ACTIVE",
        "billing_event": "IMPRESSION",
        "bid_micro": 500000,  # $0.50 CPM
        "daily_budget_micro": 5000000,  # $5
        "start_time": "2026-03-15T00:00:00.000Z",
        "optimization_goal": "SWIPES",
        "placement_v2": {
            "config": "AUTOMATIC"
        },
        "targeting": {
            "geos": [{"country_code": "us"}],
            "demographics": [{
                "min_age": 18,
                "max_age": 24,
                "gender": "FEMALE"
            }],
            "interests": [{"id": "DLXS_1"}]  # Beauty
        }
    }]
}
response = requests.post(url, json=payload, headers=headers)
```

### Create Ad
```python
url = f"https://adsapi.snapchat.com/v1/adsquads/{adsquad_id}/ads"
payload = {
    "ads": [{
        "name": "Product Ad 1",
        "ad_squad_id": adsquad_id,
        "creative_id": creative_id,
        "status": "ACTIVE",
        "type": "SNAP_AD"
    }]
}
response = requests.post(url, json=payload, headers=headers)
```

## Creative Management

### Upload Media
```python
# Step 1: Create media
url = f"https://adsapi.snapchat.com/v1/adaccounts/{ad_account_id}/media"
payload = {
    "media": [{
        "name": "Product Video",
        "ad_account_id": ad_account_id,
        "type": "VIDEO"
    }]
}
response = requests.post(url, json=payload, headers=headers)
media_id = response.json()["media"][0]["media"]["id"]

# Step 2: Upload file
upload_url = response.json()["media"][0]["media"]["upload_url"]
with open("video.mp4", "rb") as f:
    requests.put(upload_url, data=f)
```

### Create Creative
```python
url = f"https://adsapi.snapchat.com/v1/adaccounts/{ad_account_id}/creatives"
payload = {
    "creatives": [{
        "name": "Spring Sale Creative",
        "ad_account_id": ad_account_id,
        "type": "SNAP_AD",
        "brand_name": "Your Brand",
        "headline": "Shop Spring Sale",
        "shareable": True,
        "call_to_action": "SHOP_NOW",
        "top_snap_media_id": media_id,
        "web_view_properties": {
            "url": "https://example.com/spring-sale"
        }
    }]
}
response = requests.post(url, json=payload, headers=headers)
creative_id = response.json()["creatives"][0]["creative"]["id"]
```

## AR Lens Campaigns

### Create Lens Campaign
```python
# Campaign for AR Lens
url = f"https://adsapi.snapchat.com/v1/adaccounts/{ad_account_id}/campaigns"
payload = {
    "campaigns": [{
        "name": "AR Lens Campaign",
        "ad_account_id": ad_account_id,
        "status": "ACTIVE",
        "objective": "ENGAGEMENT"
    }]
}
response = requests.post(url, json=payload, headers=headers)

# Ad Squad for Lens
adsquad_payload = {
    "adsquads": [{
        "name": "Lens Ad Squad",
        "campaign_id": campaign_id,
        "type": "LENS",
        "billing_event": "IMPRESSION",
        "bid_micro": 1000000,  # $1 CPM
        "optimization_goal": "USES",
        "placement_v2": {
            "platforms": ["SNAPCHAT"],
            "placements": ["CAMERA"]  # AR Lens placement
        }
    }]
}
```

## Audience Management

### Create Snap Pixel Audience
```python
url = f"https://adsapi.snapchat.com/v1/adaccounts/{ad_account_id}/segments"
payload = {
    "segments": [{
        "name": "Website Visitors - Last 30 Days",
        "ad_account_id": ad_account_id,
        "source_type": "PIXEL",
        "retention_in_days": 30,
        "pixel_id": pixel_id
    }]
}
response = requests.post(url, json=payload, headers=headers)
```

### Create Lookalike Audience
```python
payload = {
    "segments": [{
        "name": "Lookalike - Purchasers",
        "ad_account_id": ad_account_id,
        "source_type": "LOOKALIKE",
        "seed_segment_id": seed_segment_id,
        "country": "US",
        "lookalike_type": "SIMILARITY"
    }]
}
response = requests.post(url, json=payload, headers=headers)
```

## Conversion Tracking

### Create Pixel
```python
url = f"https://adsapi.snapchat.com/v1/adaccounts/{ad_account_id}/pixels"
payload = {
    "pixels": [{
        "name": "Website Pixel",
        "ad_account_id": ad_account_id
    }]
}
response = requests.post(url, json=payload, headers=headers)
pixel_id = response.json()["pixels"][0]["pixel"]["id"]
pixel_code = response.json()["pixels"][0]["pixel"]["pixel_javascript"]
```

## Reporting

### Get Campaign Stats
```python
url = f"https://adsapi.snapchat.com/v1/campaigns/{campaign_id}/stats"
params = {
    "granularity": "DAY",
    "start_time": "2026-03-01T00:00:00.000Z",
    "end_time": "2026-03-31T23:59:59.000Z",
    "fields": "impressions,swipes,spend,conversion_purchases"
}
response = requests.get(url, params=params, headers=headers)
stats = response.json()
```

## Rate Limits
- **Default**: 1000 requests per hour
- **Burst**: 100 requests per minute
- **Best Practice**: Implement exponential backoff

## Using the Reference Files

**`/references/snapchat-api-endpoints.md`** — Read when implementing specific API operations.

**`/references/snapchat-api-examples.md`** — Read when building automation scripts.

**`/references/snapchat-api-best-practices.md`** — Read when optimizing API usage or scaling automation.

## References

- [Snapchat Api Endpoints](references/snapchat-api-endpoints.md)
