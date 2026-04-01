---
name: spotify-ads-api-automation
description: "Automate Spotify advertising using the Spotify Ads API for programmatic campaign management, audience creation, and reporting. Use for API authentication, creating audio ad campaigns via API, managing ad sets and creatives programmatically, implementing first-party audience targeting, conversion measurement setup, real-time reporting automation, and building custom Spotify ad tools."
---

# Spotify Ads API Automation

Automate Spotify advertising using the Spotify Ads API for programmatic campaign management and reporting.

## Overview

The Spotify Ads API provides programmatic access to campaign management, audience targeting, and performance reporting for audio and podcast advertising on the Spotify platform.

## API Authentication

### OAuth 2.0 Setup
```python
import requests
import base64

# Step 1: Get client credentials
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
credentials = f"{client_id}:{client_secret}"
encoded_credentials = base64.b64encode(credentials.encode()).decode()

# Step 2: Request access token
token_url = "https://accounts.spotify.com/api/token"
headers = {
    "Authorization": f"Basic {encoded_credentials}",
    "Content-Type": "application/x-www-form-urlencoded"
}
data = {
    "grant_type": "client_credentials"
}
response = requests.post(token_url, headers=headers, data=data)
access_token = response.json()["access_token"]
```

## API Structure

### Hierarchy
- **Businesses** > **Ad Accounts** > **Campaigns** > **Ad Sets** > **Ads** > **Assets**

### Base URL
```
https://api.spotify.com/v1/ads
```

## Campaign Management

### Create Campaign
```python
url = f"https://api.spotify.com/v1/ads/accounts/{ad_account_id}/campaigns"
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}
payload = {
    "name": "Spring Audio Campaign",
    "objective": "REACH",
    "status": "ACTIVE"
}
response = requests.post(url, json=payload, headers=headers)
campaign_id = response.json()["id"]
```

### Create Ad Set
```python
url = f"https://api.spotify.com/v1/ads/accounts/{ad_account_id}/adsets"
payload = {
    "name": "Women 25-34 | Workout Playlists",
    "campaign_id": campaign_id,
    "start_time": "2026-03-15T00:00:00Z",
    "end_time": "2026-04-15T23:59:59Z",
    "budget": {
        "amount": 1000.00,
        "currency": "USD"
    },
    "bid": {
        "amount": 15.00,
        "type": "CPM"
    },
    "targeting": {
        "age": ["25-34"],
        "gender": ["FEMALE"],
        "geo": {
            "countries": ["US"]
        },
        "contexts": ["workout", "fitness"]
    }
}
response = requests.post(url, json=payload, headers=headers)
adset_id = response.json()["id"]
```

### Create Ad
```python
url = f"https://api.spotify.com/v1/ads/accounts/{ad_account_id}/ads"
payload = {
    "name": "Workout Gear Audio Ad",
    "adset_id": adset_id,
    "audio_asset_id": audio_asset_id,
    "image_asset_id": image_asset_id,
    "advertiser_name": "Your Brand",
    "tagline": "Gear Up for Success",
    "call_to_action": "LEARN_MORE",
    "clickthrough_url": "https://example.com/workout-gear"
}
response = requests.post(url, json=payload, headers=headers)
```

## Asset Management

### Upload Audio Asset
```python
# Step 1: Create asset
url = f"https://api.spotify.com/v1/ads/accounts/{ad_account_id}/assets/audio"
payload = {
    "name": "30s Audio Ad",
    "duration": 30
}
response = requests.post(url, json=payload, headers=headers)
asset_id = response.json()["id"]
upload_url = response.json()["upload_url"]

# Step 2: Upload file
with open("audio-ad.mp3", "rb") as f:
    requests.put(upload_url, data=f)

# Step 3: Confirm upload
confirm_url = f"https://api.spotify.com/v1/ads/accounts/{ad_account_id}/assets/audio/{asset_id}/confirm"
requests.post(confirm_url, headers=headers)
```

### Upload Image Asset
```python
url = f"https://api.spotify.com/v1/ads/accounts/{ad_account_id}/assets/image"
payload = {
    "name": "Companion Image",
    "aspect_ratio": "1:1"
}
response = requests.post(url, json=payload, headers=headers)
image_asset_id = response.json()["id"]
upload_url = response.json()["upload_url"]

with open("companion-image.jpg", "rb") as f:
    requests.put(upload_url, data=f)
```

## Audience Management

### Create Custom Audience
```python
url = f"https://api.spotify.com/v1/ads/accounts/{ad_account_id}/audiences"
payload = {
    "name": "Customer Email List",
    "type": "CUSTOMER_LIST",
    "data": {
        "emails": [
            "user1@example.com",
            "user2@example.com"
        ]
    }
}
response = requests.post(url, json=payload, headers=headers)
audience_id = response.json()["id"]
```

### Create Lookalike Audience
```python
payload = {
    "name": "Lookalike - High Value Customers",
    "type": "LOOKALIKE",
    "seed_audience_id": seed_audience_id,
    "country": "US",
    "size": 0.01  # 1% lookalike
}
response = requests.post(url, json=payload, headers=headers)
```

## Targeting Specifications

### Available Targeting Options
```python
targeting = {
    "age": ["18-24", "25-34", "35-44", "45-54", "55-64", "65+"],
    "gender": ["MALE", "FEMALE"],
    "geo": {
        "countries": ["US", "CA", "GB"],
        "regions": ["US-CA", "US-NY"],
        "dmas": [501, 803],  # DMA codes
        "cities": ["New York", "Los Angeles"],
        "postal_codes": ["10001", "90001"]
    },
    "contexts": [
        "workout", "party", "focus", "chill", "cooking", "gaming",
        "commute", "sleep", "romance", "dinner"
    ],
    "genres": [
        "pop", "rock", "hip-hop", "country", "electronic", "jazz",
        "classical", "latin", "r-n-b", "indie"
    ],
    "podcast_topics": [
        "news", "true-crime", "comedy", "business", "sports",
        "health", "technology", "education"
    ],
    "interests": [
        "fitness", "food", "travel", "fashion", "technology",
        "gaming", "sports", "music", "entertainment"
    ],
    "languages": ["en", "es", "fr", "de", "pt", "it"],
    "devices": ["mobile", "desktop", "tablet", "smart-speaker", "tv"]
}
```

## Conversion Measurement

### Create Pixel
```python
url = f"https://api.spotify.com/v1/ads/accounts/{ad_account_id}/pixels"
payload = {
    "name": "Website Pixel",
    "domain": "example.com"
}
response = requests.post(url, json=payload, headers=headers)
pixel_id = response.json()["id"]
pixel_code = response.json()["pixel_code"]
```

### Create Conversion Event
```python
url = f"https://api.spotify.com/v1/ads/accounts/{ad_account_id}/conversions"
payload = {
    "name": "Purchase",
    "pixel_id": pixel_id,
    "event_type": "PURCHASE",
    "attribution_window": {
        "click": 7,  # days
        "view": 1    # days
    }
}
response = requests.post(url, json=payload, headers=headers)
```

### Link Conversion to Ad Set
```python
url = f"https://api.spotify.com/v1/ads/accounts/{ad_account_id}/adsets/{adset_id}"
payload = {
    "conversion_id": conversion_id,
    "optimization_goal": "CONVERSIONS"
}
response = requests.patch(url, json=payload, headers=headers)
```

## Reporting and Analytics

### Get Campaign Performance
```python
url = f"https://api.spotify.com/v1/ads/accounts/{ad_account_id}/campaigns/{campaign_id}/analytics"
params = {
    "start_date": "2026-03-01",
    "end_date": "2026-03-31",
    "metrics": [
        "impressions", "reach", "frequency", "spend",
        "clicks", "ctr", "conversions", "cpa", "roas"
    ],
    "dimensions": ["date", "age", "gender", "geo"],
    "granularity": "DAY"
}
response = requests.get(url, params=params, headers=headers)
analytics = response.json()
```

### Get Ad Set Performance
```python
url = f"https://api.spotify.com/v1/ads/accounts/{ad_account_id}/adsets/analytics"
params = {
    "adset_ids": [adset_id_1, adset_id_2],
    "start_date": "2026-03-01",
    "end_date": "2026-03-31",
    "metrics": ["impressions", "spend", "conversions"]
}
response = requests.get(url, params=params, headers=headers)
```

### Export Report
```python
url = f"https://api.spotify.com/v1/ads/accounts/{ad_account_id}/reports"
payload = {
    "name": "Monthly Performance Report",
    "type": "CAMPAIGN",
    "start_date": "2026-03-01",
    "end_date": "2026-03-31",
    "format": "CSV",
    "metrics": ["impressions", "spend", "conversions", "roas"],
    "dimensions": ["campaign", "adset", "date"]
}
response = requests.post(url, json=payload, headers=headers)
report_id = response.json()["id"]

# Download report when ready
download_url = f"https://api.spotify.com/v1/ads/accounts/{ad_account_id}/reports/{report_id}/download"
report_data = requests.get(download_url, headers=headers)
```

## Bulk Operations

### Bulk Create Ad Sets
```python
url = f"https://api.spotify.com/v1/ads/accounts/{ad_account_id}/adsets/bulk"
payload = {
    "adsets": [
        {
            "name": f"Ad Set {i}",
            "campaign_id": campaign_id,
            "budget": {"amount": 100.00, "currency": "USD"},
            "targeting": {...}
        }
        for i in range(10)
    ]
}
response = requests.post(url, json=payload, headers=headers)
```

### Bulk Update Status
```python
url = f"https://api.spotify.com/v1/ads/accounts/{ad_account_id}/adsets/bulk/status"
payload = {
    "adset_ids": [id1, id2, id3],
    "status": "PAUSED"
}
response = requests.patch(url, json=payload, headers=headers)
```

## Error Handling and Rate Limits

### Rate Limits
- **Default**: 1000 requests per hour
- **Reporting**: Stricter limits (100 requests per hour)
- **Best Practice**: Implement exponential backoff

### Error Handling
```python
import time

def make_api_request(url, method="GET", **kwargs):
    max_retries = 3
    for attempt in range(max_retries):
        try:
            if method == "GET":
                response = requests.get(url, **kwargs)
            elif method == "POST":
                response = requests.post(url, **kwargs)
            
            response.raise_for_status()
            return response.json()
        
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 429:
                # Rate limit - exponential backoff
                wait_time = 2 ** attempt * 60
                time.sleep(wait_time)
            elif e.response.status_code == 401:
                # Refresh token
                refresh_access_token()
            else:
                raise
    
    raise Exception("Max retries exceeded")
```

## API Versioning

- **Current Version**: v3 (as of 2025)
- **Deprecation**: v3 to be deprecated ~Q1 2026, sunset ~Q3 2026
- **Lifecycle**: 3 versions maintained concurrently
- **Migration**: 6-month notice before sunset

## Using the Reference Files

**`/references/spotify-api-endpoints.md`** — Read when implementing specific API operations or looking up endpoint documentation.

**`/references/spotify-api-examples.md`** — Read when building automation scripts or integrating Spotify ads into applications.

**`/references/spotify-api-best-practices.md`** — Read when optimizing API usage, handling errors, or scaling automation.

## References

- [Spotify Api Endpoints](references/spotify-api-endpoints.md)
