---
name: meta-ads-targeting-optimization
description: "Advanced audience targeting and campaign optimization for Meta advertising including demographics, interests, behaviors, custom audiences, lookalike audiences, Advantage+ targeting, conversion optimization, and automated rules. Use for: implementing demographic targeting, creating interest-based audiences, building custom audiences from customer data, generating lookalike audiences, setting up retargeting campaigns, optimizing for conversions, implementing automated rules, and analyzing audience performance on Meta platforms."
---

# Meta Ads Targeting & Optimization

Advanced audience targeting strategies and optimization techniques for Meta advertising using the Marketing API for programmatic audience management.

## Overview

Comprehensive guide to Meta's targeting capabilities including core audiences, custom audiences, lookalike audiences, Advantage+ targeting, conversion optimization, and automated performance optimization.

## Targeting Overview

| Targeting Type | Description | Use Case |
|----------------|-------------|----------|
| **Core Audiences** | Demographics, interests, behaviors | Prospecting |
| **Custom Audiences** | Your data (email, phone, website, app) | Retargeting |
| **Lookalike Audiences** | Similar to your customers | Scaling |
| **Advantage+ Audience** | AI-powered broad targeting | Performance max |

## Core Audience Targeting

### Demographics
```python
targeting = {
    "age_min": 25,
    "age_max": 45,
    "genders": [1],  # 1=male, 2=female, omit for all
    "relationship_statuses": [1],  # 1=single, 2=in relationship, 3=married, 4=engaged
    "education_statuses": [1, 2, 3],  # 1=high school, 2=undergrad, 3=alum, etc.
    "life_events": [
        {"id": "6002714398372", "name": "Recently moved"},
        {"id": "6003054104172", "name": "New job"}
    ]
}
```

### Location Targeting
```python
# Country
targeting = {
    "geo_locations": {
        "countries": ["US", "CA", "GB"]
    }
}

# State/Region
targeting = {
    "geo_locations": {
        "regions": [
            {"key": "3847", "name": "California"},
            {"key": "3875", "name": "Texas"}
        ]
    }
}

# City
targeting = {
    "geo_locations": {
        "cities": [
            {"key": "2418779", "name": "Los Angeles", "radius": 25, "distance_unit": "mile"}
        ]
    }
}

# ZIP Code
targeting = {
    "geo_locations": {
        "zips": [
            {"key": "US:90210"},
            {"key": "US:10001"}
        ]
    }
}

# Exclude locations
targeting = {
    "geo_locations": {
        "countries": ["US"],
        "location_types": ["home", "recent"]  # or "travel_in"
    },
    "excluded_geo_locations": {
        "regions": [{"key": "3847"}]  # Exclude California
    }
}
```

### Interest Targeting
```python
# Search for interests
url = f"https://graph.facebook.com/v19.0/search"
params = {
    "access_token": access_token,
    "type": "adinterest",
    "q": "fitness",
    "limit": 10
}

response = requests.get(url, params=params)
interests = response.json()["data"]

# Apply interests
targeting = {
    "interests": [
        {"id": "6003139266461", "name": "Fitness and wellness"},
        {"id": "6003107902433", "name": "Physical fitness"},
        {"id": "6003020834693", "name": "Yoga"}
    ]
}
```

### Behavior Targeting
```python
# Search behaviors
url = f"https://graph.facebook.com/v19.0/search"
params = {
    "access_token": access_token,
    "type": "adTargetingCategory",
    "class": "behaviors",
    "q": "travel"
}

response = requests.get(url, params=params)
behaviors = response.json()["data"]

# Apply behaviors
targeting = {
    "behaviors": [
        {"id": "6002714895372", "name": "Frequent travelers"},
        {"id": "6015559470583", "name": "Commuters"},
        {"id": "6003808923172", "name": "Small business owners"}
    ]
}
```

### Device & Platform Targeting
```python
targeting = {
    "user_device": ["iPhone", "Android_Smartphone"],
    "user_os": ["iOS", "Android"],
    "wireless_carrier": ["WiFi"],  # or specific carriers
    "device_platforms": ["mobile", "desktop"]  # or "mobile" only
}
```

## Custom Audiences

### Customer List Audience
```python
# Create custom audience
url = f"https://graph.facebook.com/v19.0/act_{ad_account_id}/customaudiences"

audience_data = {
    "access_token": access_token,
    "name": "Customer Email List",
    "subtype": "CUSTOM",
    "description": "Q1 2026 customers",
    "customer_file_source": "USER_PROVIDED_ONLY"
}

response = requests.post(url, params=audience_data)
audience_id = response.json()["id"]

# Upload users
import hashlib

def hash_data(data):
    return hashlib.sha256(data.lower().strip().encode()).hexdigest()

users = [
    {
        "email": hash_data("user1@example.com"),
        "phone": hash_data("+12025551234"),
        "fn": hash_data("john"),
        "ln": hash_data("doe"),
        "ct": hash_data("new york"),
        "st": hash_data("ny"),
        "zip": hash_data("10001"),
        "country": hash_data("us")
    }
]

url = f"https://graph.facebook.com/v19.0/{audience_id}/users"
params = {
    "access_token": access_token,
    "payload": json.dumps({"schema": ["EMAIL", "PHONE", "FN", "LN", "CT", "ST", "ZIP", "COUNTRY"], "data": [[u["email"], u["phone"], u["fn"], u["ln"], u["ct"], u["st"], u["zip"], u["country"]] for u in users]})
}

requests.post(url, params=params)
```

### Website Custom Audience
```python
# Pixel-based audience
audience_data = {
    "access_token": access_token,
    "name": "Website Visitors 30d",
    "subtype": "WEBSITE",
    "rule": json.dumps({
        "inclusions": {
            "operator": "or",
            "rules": [
                {
                    "event_sources": [{"id": pixel_id, "type": "pixel"}],
                    "retention_seconds": 2592000,  # 30 days
                    "filter": {
                        "operator": "and",
                        "filters": [
                            {"field": "event", "operator": "eq", "value": "PageView"}
                        ]
                    }
                }
            ]
        }
    }),
    "prefill": True
}

response = requests.post(
    f"https://graph.facebook.com/v19.0/act_{ad_account_id}/customaudiences",
    params=audience_data
)
```

### Engagement Custom Audience
```python
# Video viewers
audience_data = {
    "access_token": access_token,
    "name": "Video Viewers 95%",
    "subtype": "ENGAGEMENT",
    "rule": json.dumps({
        "inclusions": {
            "operator": "or",
            "rules": [
                {
                    "event_sources": [{"id": video_id, "type": "video"}],
                    "retention_seconds": 365,
                    "filter": {
                        "operator": "and",
                        "filters": [
                            {"field": "event", "operator": "eq", "value": "video_view"},
                            {"field": "percent", "operator": "gte", "value": 95}
                        ]
                    }
                }
            ]
        }
    })
}

# Instagram/Facebook engagers
audience_data = {
    "name": "Page Engagers 365d",
    "subtype": "ENGAGEMENT",
    "rule": json.dumps({
        "inclusions": {
            "operator": "or",
            "rules": [
                {
                    "event_sources": [{"id": page_id, "type": "page"}],
                    "retention_seconds": 31536000,  # 365 days
                    "filter": {
                        "operator": "and",
                        "filters": [
                            {"field": "event", "operator": "eq", "value": "page_engaged"}
                        ]
                    }
                }
            ]
        }
    })
}
```

## Lookalike Audiences

### Create Lookalike
```python
url = f"https://graph.facebook.com/v19.0/act_{ad_account_id}/customaudiences"

lookalike_data = {
    "access_token": access_token,
    "name": "Lookalike 1% - Customers",
    "subtype": "LOOKALIKE",
    "origin_audience_id": source_audience_id,
    "lookalike_spec": json.dumps({
        "type": "similarity",
        "ratio": 0.01,  # 1% (0.01 to 0.20)
        "country": "US"
    })
}

response = requests.post(url, params=lookalike_data)
lookalike_id = response.json()["id"]
```

### Multi-Country Lookalike
```python
lookalike_data = {
    "name": "Lookalike 2% - Multi-Country",
    "subtype": "LOOKALIKE",
    "origin_audience_id": source_audience_id,
    "lookalike_spec": json.dumps({
        "type": "similarity",
        "ratio": 0.02,  # 2%
        "country": ["US", "CA", "GB", "AU"]
    })
}
```

### Value-Based Lookalike
```python
# Requires customer value data in source audience
lookalike_data = {
    "name": "Lookalike 1% - High Value",
    "subtype": "LOOKALIKE",
    "origin_audience_id": high_value_customer_audience_id,
    "lookalike_spec": json.dumps({
        "type": "similarity",
        "ratio": 0.01,
        "country": "US",
        "starting_ratio": 0.0,  # Top tier
        "conversion_type": "total_value"
    })
}
```

## Advantage+ Audience

### Advantage+ Targeting
```python
# Minimal targeting, let Meta optimize
adset_data = {
    "name": "Advantage+ Campaign",
    "campaign_id": campaign_id,
    "daily_budget": 10000,
    "billing_event": "IMPRESSIONS",
    "optimization_goal": "OFFSITE_CONVERSIONS",
    "targeting": json.dumps({
        "geo_locations": {"countries": ["US"]},
        "age_min": 18,
        "age_max": 65
    }),
    "targeting_optimization": "expansion_all"  # Advantage+ expansion
}
```

### Advantage+ with Suggestions
```python
# Provide suggestions, Meta can expand
adset_data = {
    "targeting": json.dumps({
        "geo_locations": {"countries": ["US"]},
        "age_min": 25,
        "age_max": 45,
        "interests": [{"id": "6003139266461"}]  # Suggestions
    }),
    "targeting_optimization": "expansion_all"
}
```

## Conversion Optimization

### Pixel Events
```python
# Standard events for optimization
optimization_goals = {
    "OFFSITE_CONVERSIONS": "Purchase, Lead, CompleteRegistration",
    "LANDING_PAGE_VIEWS": "Page load",
    "LINK_CLICKS": "Link clicks",
    "VALUE": "Purchase value",
    "LEAD_GENERATION": "Lead form submissions"
}

# Ad set with conversion optimization
adset_data = {
    "optimization_goal": "OFFSITE_CONVERSIONS",
    "promoted_object": json.dumps({
        "pixel_id": pixel_id,
        "custom_event_type": "PURCHASE"
    })
}
```

### Value Optimization
```python
# Optimize for purchase value
adset_data = {
    "optimization_goal": "VALUE",
    "billing_event": "IMPRESSIONS",
    "bid_strategy": "LOWEST_COST_WITH_MIN_ROAS",
    "bid_amount": 200,  # 2.0x ROAS minimum
    "promoted_object": json.dumps({
        "pixel_id": pixel_id,
        "custom_event_type": "PURCHASE"
    })
}
```

## Automated Rules

### Create Automated Rule
```python
url = f"https://graph.facebook.com/v19.0/act_{ad_account_id}/adrules_library"

rule_data = {
    "access_token": access_token,
    "name": "Pause High CPA Ad Sets",
    "evaluation_spec": json.dumps({
        "evaluation_type": "SCHEDULE",
        "filters": [
            {"field": "entity_type", "operator": "EQUAL", "value": "ADSET"},
            {"field": "cost_per_action_type:offsite_conversion.fb_pixel_purchase", "operator": "GREATER_THAN", "value": 50},
            {"field": "spend", "operator": "GREATER_THAN", "value": 100}
        ]
    }),
    "execution_spec": json.dumps({
        "execution_type": "PAUSE"
    }),
    "schedule_spec": json.dumps({
        "schedule_type": "DAILY",
        "time": "09:00:00"
    })
}

response = requests.post(url, params=rule_data)
```

### Budget Increase Rule
```python
rule_data = {
    "name": "Increase Budget for High ROAS",
    "evaluation_spec": json.dumps({
        "evaluation_type": "SCHEDULE",
        "filters": [
            {"field": "entity_type", "operator": "EQUAL", "value": "ADSET"},
            {"field": "purchase_roas", "operator": "GREATER_THAN", "value": 3.0},
            {"field": "spend", "operator": "GREATER_THAN", "value": 500}
        ]
    }),
    "execution_spec": json.dumps({
        "execution_type": "CHANGE_BUDGET",
        "execution_options": [
            {"field": "budget", "operator": "INCREASE_BY", "value": 20}
        ]
    }),
    "schedule_spec": json.dumps({
        "schedule_type": "DAILY",
        "time": "10:00:00"
    })
}
```

## Audience Insights

### Get Audience Size
```python
url = f"https://graph.facebook.com/v19.0/act_{ad_account_id}/reachestimate"

params = {
    "access_token": access_token,
    "targeting_spec": json.dumps({
        "geo_locations": {"countries": ["US"]},
        "age_min": 25,
        "age_max": 45,
        "interests": [{"id": "6003139266461"}]
    })
}

response = requests.get(url, params=params)
estimate = response.json()["data"]
print(f"Estimated reach: {estimate['users']}")
```

## Using the Reference Files

**`/references/meta-targeting-reference.md`** — Read for complete targeting options catalog, interest/behavior IDs, demographic categories, and targeting combination strategies.

**`/references/meta-audience-strategies.md`** — Read for audience building frameworks, lookalike optimization, retargeting funnels, and scaling strategies.

**`/references/meta-conversion-optimization.md`** — Read for pixel implementation, event optimization, value-based bidding, and automated rule templates.
