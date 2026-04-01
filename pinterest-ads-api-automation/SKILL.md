---
name: pinterest-ads-api-automation
description: "Automate Pinterest advertising using the Pinterest Ads API for programmatic campaign management, bulk operations, and integration. Use for API authentication, creating campaigns via API, managing ad groups and ads programmatically, uploading creatives, audience management, conversion tracking, reporting automation, and building custom Pinterest ad tools."
---

# Pinterest Ads API Automation

Automate Pinterest advertising campaigns using the Pinterest Ads API for programmatic management and integration.

## Overview

The Pinterest Ads API enables developers and advertisers to programmatically manage campaigns, upload creatives, target audiences, track conversions, and generate reports. This skill covers authentication, core API operations, and automation strategies.

## API Authentication

### OAuth 2.0 Flow

Pinterest uses OAuth 2.0 for API authentication.

**Steps**:
1. Register app at developers.pinterest.com
2. Obtain client ID and secret
3. Request authorization code
4. Exchange code for access token
5. Use access token for API requests
6. Refresh token when expired

**Access Token Request**:
```python
import requests

token_url = "https://api.pinterest.com/v5/oauth/token"
data = {
    "grant_type": "authorization_code",
    "code": authorization_code,
    "redirect_uri": redirect_uri
}
headers = {
    "Authorization": f"Basic {base64_credentials}"
}
response = requests.post(token_url, data=data, headers=headers)
access_token = response.json()["access_token"]
```

## Campaign Management

### Create Campaign

```python
import requests

url = "https://api.pinterest.com/v5/ad_accounts/{ad_account_id}/campaigns"
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}
payload = {
    "name": "Spring Sale 2026",
    "status": "ACTIVE",
    "objective_type": "AWARENESS",
    "daily_spend_cap": 5000  # in cents
}
response = requests.post(url, json=payload, headers=headers)
campaign = response.json()
```

### Create Ad Group

```python
url = f"https://api.pinterest.com/v5/ad_accounts/{ad_account_id}/ad_groups"
payload = {
    "name": "Women 25-34 | Home Decor",
    "campaign_id": campaign_id,
    "billable_event": "CLICKTHROUGH",
    "bid_in_micro_currency": 100000,  # $0.10
    "budget_in_micro_currency": 1000000,  # $10 daily
    "start_time": 1710000000,
    "targeting_spec": {
        "GENDER": ["FEMALE"],
        "AGE_BUCKET": ["25-34"],
        "INTEREST": ["home_decor"]
    }
}
response = requests.post(url, json=payload, headers=headers)
```

### Create Ad

```python
url = f"https://api.pinterest.com/v5/ad_accounts/{ad_account_id}/ads"
payload = {
    "ad_group_id": ad_group_id,
    "creative_type": "REGULAR",
    "pin_id": pin_id,
    "name": "Blue Sofa Ad",
    "status": "ACTIVE",
    "destination_url": "https://example.com/product/blue-sofa"
}
response = requests.post(url, json=payload, headers=headers)
```

## Creative Management

### Upload Image

```python
import requests

# Step 1: Register image
url = f"https://api.pinterest.com/v5/media"
payload = {
    "media_type": "image"
}
response = requests.post(url, json=payload, headers=headers)
media_id = response.json()["media_id"]
upload_url = response.json()["upload_url"]

# Step 2: Upload to S3
with open("product-image.jpg", "rb") as f:
    requests.put(upload_url, data=f)

# Step 3: Create Pin with media
pin_url = f"https://25265714.fs1.hubspotusercontent-eu1.net/hubfs/25265714/Different-types-of-Pinterest-pins.jpg"
pin_payload = {
    "media_source": {
        "source_type": "image_url",
        "url": "https://m.media-amazon.com/images/I/81KrwbONtYL._AC_UF894,1000_QL80_.jpg"
    },
    "link": "https://example.com/product",
    "title": "Blue Sofa",
    "description": "Modern blue sofa for living room"
}
pin_response = requests.post(pin_url, json=pin_payload, headers=headers)
pin_id = pin_response.json()["id"]
```

## Audience Management

### Create Customer List Audience

```python
url = f"https://api.pinterest.com/v5/ad_accounts/{ad_account_id}/customer_lists"
payload = {
    "name": "Email List - March 2026",
    "records": "email1@example.com,email2@example.com",  # CSV format
    "list_type": "EMAIL"
}
response = requests.post(url, json=payload, headers=headers)
```

### Create Actalike Audience

```python
url = f"https://api.pinterest.com/v5/ad_accounts/{ad_account_id}/audiences"
payload = {
    "name": "Lookalike - High Value Customers",
    "audience_type": "ACTALIKE",
    "seed_id": customer_list_id,
    "similarity": 0.01  # 1% lookalike
}
response = requests.post(url, json=payload, headers=headers)
```

## Conversion Tracking

### Create Conversion Event

```python
url = f"https://api.pinterest.com/v5/ad_accounts/{ad_account_id}/conversion_tags/{tag_id}/events"
payload = {
    "event_name": "Purchase",
    "action_source": "web",
    "event_time": 1710000000,
    "user_data": {
        "em": ["hashed_email"],
        "ph": ["hashed_phone"]
    },
    "custom_data": {
        "value": 79.99,
        "currency": "USD",
        "order_id": "ORDER123"
    }
}
response = requests.post(url, json=payload, headers=headers)
```

## Reporting and Analytics

### Get Campaign Analytics

```python
url = f"https://api.pinterest.com/v5/ad_accounts/{ad_account_id}/campaigns/analytics"
params = {
    "campaign_ids": [campaign_id],
    "start_date": "2026-03-01",
    "end_date": "2026-03-31",
    "columns": ["SPEND_IN_DOLLAR", "IMPRESSION_1", "CLICKTHROUGH_1", "TOTAL_CLICKTHROUGH"],
    "granularity": "DAY"
}
response = requests.get(url, params=params, headers=headers)
analytics = response.json()
```

## Bulk Operations

### Bulk Create Ads

```python
url = f"https://api.pinterest.com/v5/ad_accounts/{ad_account_id}/ads"
ads = []
for product in products:
    ads.append({
        "ad_group_id": ad_group_id,
        "creative_type": "REGULAR",
        "pin_id": product["pin_id"],
        "name": product["name"],
        "status": "ACTIVE"
    })

# Create in batches of 100
for i in range(0, len(ads), 100):
    batch = ads[i:i+100]
    response = requests.post(url, json=batch, headers=headers)
```

## Error Handling

```python
def make_api_request(url, method="GET", **kwargs):
    try:
        if method == "GET":
            response = requests.get(url, **kwargs)
        elif method == "POST":
            response = requests.post(url, **kwargs)
        
        response.raise_for_status()
        return response.json()
    
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 429:
            # Rate limit - wait and retry
            time.sleep(60)
            return make_api_request(url, method, **kwargs)
        elif e.response.status_code == 401:
            # Refresh token
            refresh_access_token()
            return make_api_request(url, method, **kwargs)
        else:
            raise
```

## Rate Limits

- **Default**: 1000 requests per hour per access token
- **Burst**: 200 requests per minute
- **Best Practice**: Implement exponential backoff

## Using the Reference Files

**`/references/pinterest-api-endpoints.md`** — Read when implementing specific API operations or looking up endpoint documentation.

**`/references/pinterest-api-examples.md`** — Read when building automation scripts or integrating Pinterest ads into applications.

**`/references/pinterest-api-best-practices.md`** — Read when optimizing API usage, handling errors, or scaling automation.

## References

- [Pinterest Api Endpoints](references/pinterest-api-endpoints.md)
