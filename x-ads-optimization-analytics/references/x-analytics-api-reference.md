# X Ads Analytics API Reference

Complete reference for X Ads analytics endpoints, metrics, and data structures.

---

## Stats API Endpoint

**Base URL**: `https://ads-api.x.com/12/stats/accounts/{account_id}`

### Request Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `entity` | string | Yes | ACCOUNT, FUNDING_INSTRUMENT, CAMPAIGN, LINE_ITEM, PROMOTED_TWEET, MEDIA_CREATIVE, ORGANIC_TWEET |
| `entity_ids` | string | Yes | Comma-separated IDs |
| `start_time` | string | Yes | ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ) |
| `end_time` | string | Yes | ISO 8601 format |
| `granularity` | string | No | HOUR, DAY, TOTAL (default: TOTAL) |
| `metric_groups` | string | No | Comma-separated groups |
| `placement` | string | No | ALL_ON_TWITTER, PUBLISHER_NETWORK |
| `segmentation_type` | string | No | GENDER, AGE, LOCATION, PLATFORM, DEVICES |

### Metric Groups

**ENGAGEMENT**
- impressions
- engagements
- engagement_rate
- likes
- retweets
- replies
- follows
- unfollows
- url_clicks
- user_profile_clicks
- hashtag_clicks

**BILLING**
- billed_charge_local_micro
- billed_engagements

**VIDEO**
- video_total_views
- video_views_25
- video_views_50
- video_views_75
- video_views_100
- video_cta_clicks
- video_content_starts
- video_mrc_views
- video_3s100pct_views
- video_6s_views

**MOBILE_CONVERSION**
- mobile_conversion_installs
- mobile_conversion_purchases
- mobile_conversion_sign_ups
- mobile_conversion_downloads
- mobile_conversion_re_engages
- mobile_conversion_add_to_carts
- mobile_conversion_checkouts_initiated
- mobile_conversion_reservations
- mobile_conversion_tutorials_completed
- mobile_conversion_achievements_unlocked
- mobile_conversion_searches
- mobile_conversion_add_to_wishlists
- mobile_conversion_credits_spent
- mobile_conversion_rated
- mobile_conversion_shares
- mobile_conversion_site_visits
- mobile_conversion_updates

**WEB_CONVERSION**
- conversion_purchases
- conversion_sign_ups
- conversion_site_visits
- conversion_downloads
- conversion_add_to_carts
- conversion_checkouts_initiated
- conversion_custom

**MEDIA**
- media_views
- media_engagements

**LIFE_EVENT**
- qualified_impressions

---

## Response Format

```json
{
  "request": {
    "params": {
      "entity": "CAMPAIGN",
      "entity_ids": ["abc123"],
      "start_time": "2026-03-01T00:00:00Z",
      "end_time": "2026-03-07T23:59:59Z",
      "granularity": "DAY",
      "metric_groups": ["ENGAGEMENT", "BILLING"]
    }
  },
  "data": [
    {
      "id": "abc123",
      "id_data": [
        {
          "segment": null,
          "metrics": {
            "impressions": [1000, 1200, 1100],
            "engagements": [50, 60, 55],
            "billed_charge_local_micro": [5000000, 6000000, 5500000]
          }
        }
      ]
    }
  ],
  "data_type": "analytics",
  "time_series_length": 3
}
```

---

## Calculated Metrics

### Click-Through Rate (CTR)
```python
ctr = (url_clicks / impressions) * 100
```

### Cost Per Click (CPC)
```python
cpc = billed_charge_local_micro / url_clicks / 1_000_000
```

### Cost Per Engagement (CPE)
```python
cpe = billed_charge_local_micro / engagements / 1_000_000
```

### Cost Per Acquisition (CPA)
```python
cpa = billed_charge_local_micro / conversions / 1_000_000
```

### Engagement Rate
```python
engagement_rate = (engagements / impressions) * 100
```

### Video Completion Rate
```python
completion_rate = (video_views_100 / video_total_views) * 100
```

---

## Segmentation

### By Gender
```python
params = {
    "segmentation_type": "GENDER"
}
# Returns: MALE, FEMALE, UNKNOWN
```

### By Age
```python
params = {
    "segmentation_type": "AGE"
}
# Returns: AGE_13_TO_17, AGE_18_TO_24, AGE_25_TO_34, AGE_35_TO_49, AGE_50_AND_UP
```

### By Location
```python
params = {
    "segmentation_type": "LOCATION"
}
# Returns: Country codes (US, GB, etc.)
```

### By Platform
```python
params = {
    "segmentation_type": "PLATFORM"
}
# Returns: IPHONE, ANDROID_PHONE, DESKTOP, etc.
```

---

## Rate Limits

- **Analytics Endpoint**: 10,000 requests per 15 minutes
- **Recommended**: Batch entity_ids (up to 20 per request)

---

## Data Freshness

- **Real-time metrics**: 5-10 minute delay
- **Conversion data**: Up to 24 hours
- **Final billing**: 48-72 hours

---

## Error Codes

| Code | Message | Solution |
|------|---------|----------|
| 400 | Invalid parameters | Check date format, entity IDs |
| 401 | Unauthorized | Refresh OAuth token |
| 404 | Entity not found | Verify entity ID exists |
| 429 | Rate limit exceeded | Implement backoff |
