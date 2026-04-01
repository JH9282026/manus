---
name: x-ads-optimization-analytics
description: "Advanced analytics, performance optimization, and conversion tracking for X advertising campaigns. Covers metrics analysis (impressions, engagement, CTR, conversions), A/B testing, bid optimization, audience insights, conversion pixel implementation, attribution models, and automated reporting via X Ads API. Use for: analyzing campaign performance, implementing conversion tracking, optimizing bids programmatically, conducting creative A/B tests, generating automated reports, setting up performance alerts, analyzing audience demographics, and building optimization workflows for X advertising."
---

# X Ads Optimization & Analytics

Advanced performance analytics and automated optimization for X advertising campaigns using the Ads API for data-driven decision making.

## Overview

Comprehensive analytics and optimization framework for X advertising including conversion tracking, performance metrics analysis, automated bid optimization, A/B testing, and reporting workflows for agentic AI deployment.

## Key Performance Metrics

| Metric | API Field | Description |
|--------|-----------|-------------|
| **Impressions** | `impressions` | Ad views |
| **Engagements** | `engagements` | Clicks, likes, retweets, replies |
| **CTR** | Calculated | (clicks / impressions) × 100 |
| **CPC** | Calculated | spend / clicks |
| **CPE** | Calculated | spend / engagements |
| **Conversions** | `conversions` | Tracked actions |
| **CPA** | Calculated | spend / conversions |
| **Video Views** | `video_views` | 50%+ in-view for 2+ seconds |
| **App Installs** | `mobile_conversion_installs` | Tracked app downloads |

## Analytics API Endpoints

### Campaign Stats
```python
import requests
from datetime import datetime, timedelta

# Date range
end_date = datetime.now()
start_date = end_date - timedelta(days=7)

params = {
    "entity": "CAMPAIGN",
    "entity_ids": campaign_id,
    "start_time": start_date.strftime("%Y-%m-%dT%H:%M:%SZ"),
    "end_time": end_date.strftime("%Y-%m-%dT%H:%M:%SZ"),
    "granularity": "DAY",
    "metric_groups": "ENGAGEMENT,BILLING,VIDEO,MOBILE_CONVERSION",
    "placement": "ALL_ON_TWITTER"
}

response = requests.get(
    f"https://ads-api.x.com/12/stats/accounts/{account_id}",
    headers={"Authorization": f"Bearer {access_token}"},
    params=params
)

stats = response.json()["data"]
```

### Line Item Stats
```python
params = {
    "entity": "LINE_ITEM",
    "entity_ids": ",".join(line_item_ids),
    "metric_groups": "ENGAGEMENT,BILLING"
}
```

### Promoted Tweet Stats
```python
params = {
    "entity": "PROMOTED_TWEET",
    "entity_ids": promoted_tweet_id
}
```

## Metric Groups

| Group | Metrics Included |
|-------|------------------|
| **ENGAGEMENT** | impressions, engagements, likes, retweets, replies, follows |
| **BILLING** | billed_charge_local_micro |
| **VIDEO** | video_views, video_views_25/50/75/100, video_cta_clicks |
| **MOBILE_CONVERSION** | mobile_conversion_installs, mobile_conversion_purchases |
| **WEB_CONVERSION** | conversion_purchases, conversion_sign_ups, conversion_site_visits |
| **MEDIA** | media_views, media_engagements |

## Conversion Tracking

### 1. Create Conversion Event
```python
conversion_data = {
    "name": "Purchase Completed",
    "post_view_attribution_window": "30_DAY",
    "post_engagement_attribution_window": "30_DAY",
    "type": "PURCHASE"
}

response = requests.post(
    f"https://ads-api.x.com/12/accounts/{account_id}/conversion_events",
    headers=headers,
    json=conversion_data
)

conversion_event_id = response.json()["data"]["id"]
pixel_code = response.json()["data"]["pixel_code"]
```

### 2. Install Pixel
```html
<!-- Place before </head> -->
<script>
!function(e,t,n,s,u,a){e.twq||(s=e.twq=function(){s.exe?s.exe.apply(s,arguments):s.queue.push(arguments);
},s.version='1.1',s.queue=[],u=t.createElement(n),u.async=!0,u.src='https://static.ads-twitter.com/uwt.js',
a=t.getElementsByTagName(n)[0],a.parentNode.insertBefore(u,a))}(window,document,'script');
twq('config','PIXEL_ID');
</script>
```

### 3. Track Events
```javascript
// Page view (automatic)
twq('event', 'tw-PIXEL_ID-EVENT_ID', {});

// Purchase with value
twq('event', 'tw-PIXEL_ID-PURCHASE_EVENT_ID', {
  value: 99.99,
  currency: 'USD',
  num_items: 2
});

// Sign up
twq('event', 'tw-PIXEL_ID-SIGNUP_EVENT_ID', {});
```

## Attribution Windows

| Window | Description |
|--------|-------------|
| **Post-View** | User saw ad, converted later (1/7/14/30 days) |
| **Post-Engagement** | User clicked ad, converted later (1/7/14/30 days) |

## Bid Optimization

### Automated Bid Adjuster
```python
def optimize_bids(account_id, line_items):
    for item in line_items:
        stats = get_line_item_stats(item["id"])
        
        ctr = stats["clicks"] / stats["impressions"]
        target_ctr = 0.02  # 2%
        
        if ctr < target_ctr * 0.5:
            # Poor performance, decrease bid 20%
            new_bid = int(item["bid_amount"] * 0.8)
        elif ctr > target_ctr * 1.5:
            # Great performance, increase bid 20%
            new_bid = int(item["bid_amount"] * 1.2)
        else:
            continue
        
        # Update bid
        requests.put(
            f"https://ads-api.x.com/12/accounts/{account_id}/line_items/{item['id']}",
            headers=headers,
            json={"bid_amount_local_micro": new_bid}
        )
```

### Target CPA Optimization
```python
def optimize_for_cpa(target_cpa, current_stats):
    actual_cpa = current_stats["spend"] / current_stats["conversions"]
    
    if actual_cpa > target_cpa * 1.2:
        # Too expensive, lower bid
        return current_bid * 0.85
    elif actual_cpa < target_cpa * 0.8:
        # Room to scale, increase bid
        return current_bid * 1.15
    else:
        return current_bid
```

## A/B Testing Framework

### Creative Testing
```python
# Create test variants
variants = [
    {"tweet_id": "variant_a", "line_item_id": line_item_id},
    {"tweet_id": "variant_b", "line_item_id": line_item_id},
    {"tweet_id": "variant_c", "line_item_id": line_item_id}
]

for variant in variants:
    requests.post(
        f"https://ads-api.x.com/12/accounts/{account_id}/promoted_tweets",
        headers=headers,
        json=variant
    )

# After 1000+ impressions per variant
def analyze_test(variants):
    results = []
    for v in variants:
        stats = get_promoted_tweet_stats(v["id"])
        results.append({
            "variant": v["tweet_id"],
            "ctr": stats["clicks"] / stats["impressions"],
            "cpe": stats["spend"] / stats["engagements"]
        })
    
    winner = max(results, key=lambda x: x["ctr"])
    return winner
```

### Audience Testing
```python
# Create separate line items for each audience
audiences = [
    {"interests": ["15"]},  # Technology
    {"interests": ["127"]},  # Consumer electronics
    {"keywords": [{"keyword": "AI"}]}
]

for audience in audiences:
    line_item = create_line_item(
        campaign_id=campaign_id,
        targeting=audience,
        bid_amount=2000000
    )
```

## Audience Insights

### Demographics Report
```python
params = {
    "entity": "LINE_ITEM",
    "entity_ids": line_item_id,
    "metric_groups": "ENGAGEMENT",
    "segmentation_type": "GENDER"
}

response = requests.get(
    f"https://ads-api.x.com/12/stats/accounts/{account_id}",
    headers=headers,
    params=params
)

# Segmentation types: GENDER, AGE, LOCATION, PLATFORM, DEVICES
```

## Automated Reporting

### Daily Performance Report
```python
import pandas as pd
from datetime import datetime, timedelta

def generate_daily_report(account_id, campaign_ids):
    yesterday = datetime.now() - timedelta(days=1)
    
    all_stats = []
    for campaign_id in campaign_ids:
        stats = get_campaign_stats(
            account_id,
            campaign_id,
            start_date=yesterday,
            end_date=yesterday
        )
        all_stats.append(stats)
    
    df = pd.DataFrame(all_stats)
    df["CTR"] = (df["clicks"] / df["impressions"] * 100).round(2)
    df["CPC"] = (df["spend"] / df["clicks"]).round(2)
    df["CPA"] = (df["spend"] / df["conversions"]).round(2)
    
    return df
```

### Performance Alerts
```python
def check_performance_alerts(stats, thresholds):
    alerts = []
    
    if stats["ctr"] < thresholds["min_ctr"]:
        alerts.append(f"Low CTR: {stats['ctr']:.2%}")
    
    if stats["cpa"] > thresholds["max_cpa"]:
        alerts.append(f"High CPA: ${stats['cpa']:.2f}")
    
    if stats["daily_spend"] > thresholds["daily_budget"] * 0.8:
        alerts.append(f"Budget 80% spent: ${stats['daily_spend']:.2f}")
    
    return alerts
```

## Optimization Workflows

### Auto-Pause Underperformers
```python
def auto_pause_poor_performers(account_id, min_impressions=1000, min_ctr=0.01):
    line_items = get_all_line_items(account_id)
    
    for item in line_items:
        stats = get_line_item_stats(item["id"])
        
        if stats["impressions"] > min_impressions:
            ctr = stats["clicks"] / stats["impressions"]
            
            if ctr < min_ctr:
                # Pause line item
                requests.put(
                    f"https://ads-api.x.com/12/accounts/{account_id}/line_items/{item['id']}",
                    headers=headers,
                    json={"entity_status": "PAUSED"}
                )
```

### Budget Reallocation
```python
def reallocate_budgets(campaigns, total_budget):
    # Get performance scores
    scores = []
    for camp in campaigns:
        stats = get_campaign_stats(camp["id"])
        score = stats["conversions"] / stats["spend"]  # Conversion efficiency
        scores.append({"id": camp["id"], "score": score})
    
    # Allocate budget proportionally to performance
    total_score = sum(s["score"] for s in scores)
    
    for s in scores:
        new_budget = int((s["score"] / total_score) * total_budget)
        update_campaign_budget(s["id"], new_budget)
```

## Performance Benchmarks

| Metric | Good | Average | Poor |
|--------|------|---------|------|
| **CTR** | >2% | 1-2% | <1% |
| **Engagement Rate** | >3% | 1-3% | <1% |
| **CPC** | <$0.50 | $0.50-$1.50 | >$1.50 |
| **Video View Rate** | >50% | 30-50% | <30% |

## Using the Reference Files

**`/references/x-analytics-api-reference.md`** — Read for complete analytics API documentation, all available metrics, segmentation options, and data export formats.

**`/references/x-conversion-tracking-guide.md`** — Read for detailed conversion pixel implementation, event tracking setup, attribution configuration, and troubleshooting.

**`/references/x-optimization-strategies.md`** — Read for advanced optimization techniques, machine learning approaches, multi-objective optimization, and case studies.

## References

- [X Analytics Api Reference](references/x-analytics-api-reference.md)
- [X Conversion Tracking Guide](references/x-conversion-tracking-guide.md)
- [X Optimization Strategies](references/x-optimization-strategies.md)
