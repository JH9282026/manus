# Meta Marketing API Reference

Complete reference for Meta (Facebook/Instagram) Marketing API.

---

## Base URL

`https://graph.facebook.com/v19.0/`

**Current Version**: v19.0 (as of March 2026)

---

## Authentication

### Access Token Types

1. **User Access Token** (recommended for ads)
   - Permissions: `ads_management`, `ads_read`
   - Expires: 60 days (can be extended)

2. **System User Token**
   - For server-to-server
   - Never expires
   - Requires Business Manager

3. **App Access Token**
   - Limited functionality
   - For testing only

### Token Debugging
```python
url = f"https://graph.facebook.com/v19.0/debug_token?input_token={token}&access_token={app_token}"
response = requests.get(url)
print(response.json())
```

---

## Campaign Endpoints

### Create Campaign
**POST** `/act_{ad_account_id}/campaigns`

**Parameters**:
- `name` (string, required)
- `objective` (enum, required): OUTCOME_AWARENESS, OUTCOME_TRAFFIC, OUTCOME_ENGAGEMENT, OUTCOME_LEADS, OUTCOME_APP_PROMOTION, OUTCOME_SALES
- `status` (enum): ACTIVE, PAUSED
- `special_ad_categories` (array): CREDIT, EMPLOYMENT, HOUSING, ISSUES_ELECTIONS_POLITICS, ONLINE_GAMBLING_AND_GAMING, NONE
- `daily_budget` (int): Amount in cents
- `lifetime_budget` (int): Amount in cents
- `bid_strategy` (enum): LOWEST_COST_WITHOUT_CAP, LOWEST_COST_WITH_BID_CAP, COST_CAP

**Response**:
```json
{
  "id": "120123456789",
  "success": true
}
```

### Get Campaign
**GET** `/{campaign_id}`

**Fields**: `id,name,objective,status,daily_budget,lifetime_budget,created_time,updated_time`

### Update Campaign
**POST** `/{campaign_id}`

### Delete Campaign
**DELETE** `/{campaign_id}`

---

## Ad Set Endpoints

### Create Ad Set
**POST** `/act_{ad_account_id}/adsets`

**Parameters**:
- `name` (string, required)
- `campaign_id` (string, required)
- `daily_budget` or `lifetime_budget` (int, required)
- `billing_event` (enum): IMPRESSIONS, LINK_CLICKS, POST_ENGAGEMENT
- `optimization_goal` (enum): LINK_CLICKS, LANDING_PAGE_VIEWS, IMPRESSIONS, REACH, OFFSITE_CONVERSIONS, LEAD_GENERATION, VALUE
- `bid_amount` (int): Bid in cents
- `targeting` (JSON object, required)
- `start_time` (datetime)
- `end_time` (datetime)
- `status` (enum): ACTIVE, PAUSED

**Targeting Structure**:
```json
{
  "geo_locations": {
    "countries": ["US"],
    "regions": [{"key": "3847"}],
    "cities": [{"key": "2418779", "radius": 10, "distance_unit": "mile"}]
  },
  "age_min": 18,
  "age_max": 65,
  "genders": [1],
  "interests": [{"id": "6003139266461", "name": "Movies"}],
  "behaviors": [{"id": "6002714895372", "name": "Frequent travelers"}],
  "custom_audiences": [{"id": "123456789"}],
  "excluded_custom_audiences": [{"id": "987654321"}]
}
```

---

## Ad Endpoints

### Create Ad
**POST** `/act_{ad_account_id}/ads`

**Parameters**:
- `name` (string, required)
- `adset_id` (string, required)
- `creative` (JSON object, required)
- `status` (enum): ACTIVE, PAUSED

**Creative Structure**:
```json
{
  "creative_id": "120123456789"
}
```

Or inline creative:
```json
{
  "object_story_spec": {
    "page_id": "123456789",
    "link_data": {
      "image_hash": "abc123",
      "link": "https://example.com",
      "message": "Check out our new product!",
      "name": "Product Name",
      "description": "Product description",
      "call_to_action": {
        "type": "LEARN_MORE",
        "value": {"link": "https://example.com"}
      }
    }
  }
}
```

---

## Batch API

### Batch Request
**POST** `/`

**Parameters**:
- `batch` (JSON array): Array of requests

**Example**:
```python
batch = [
    {
        "method": "POST",
        "relative_url": f"act_{ad_account_id}/campaigns",
        "body": "name=Campaign1&objective=OUTCOME_SALES&status=PAUSED"
    },
    {
        "method": "GET",
        "relative_url": f"{campaign_id}?fields=name,status"
    }
]

response = requests.post(
    "https://graph.facebook.com/v19.0/",
    params={
        "access_token": access_token,
        "batch": json.dumps(batch)
    }
)
```

**Limits**: 50 requests per batch

---

## Error Codes

| Code | Type | Description |
|------|------|-------------|
| 100 | Invalid parameter | Check parameter format |
| 190 | Access token error | Token expired or invalid |
| 200 | Permission denied | Missing required permission |
| 368 | Temporarily blocked | Rate limit exceeded |
| 2635 | Duplicate ad | Ad with same creative exists |

---

## Rate Limits

### Ad Account Level
- 200 API calls per hour per ad account
- Resets every hour

### User Level
- 200 API calls per hour per user

### App Level
- 200 API calls per hour per app

**Rate Limit Headers**:
```
X-Business-Use-Case-Usage: {"ad_account_id":[{"call_count":50,"total_cputime":25,"total_time":50}]}
X-App-Usage: {"call_count":10,"total_cputime":5,"total_time":10}
```

---

## Webhooks

Subscribe to real-time updates for campaigns, ad sets, and ads.

### Setup
1. Configure webhook URL in App Dashboard
2. Subscribe to `ads_insights` topic
3. Verify webhook endpoint

### Event Types
- Campaign status change
- Ad set budget exhausted
- Ad rejected
- Billing event
