---
name: nextdoor-ads-api-integration
description: "Integrate with Nextdoor Ads API and Conversion API (CAPI) for programmatic campaign management and server-side conversion tracking. Use for: automating Nextdoor ad operations, creating/updating campaigns and ad groups at scale, building custom reporting dashboards, implementing server-side conversion tracking, integrating offline conversions, and developing agentic AI automation for hyperlocal advertising campaigns."
---

# Nextdoor Ads API Integration

Programmatic access to Nextdoor advertising through Ads API and Conversion API (CAPI) for automated campaign management and conversion tracking.

## Overview

Nextdoor provides two primary APIs: Ads API for campaign management and Conversion API (CAPI) for server-side conversion tracking. The Ads API uses GraphQL and enables creation/management of campaigns, ad groups, and ads at scale. CAPI provides accurate conversion tracking independent of browser limitations.

**Key Capabilities:**
- Create and update campaigns, ad groups, ads programmatically
- Manage sub-advertiser accounts
- Configure targeting options via API
- Schedule automated performance reports
- Server-side conversion tracking (CAPI)
- Offline and in-app conversion attribution

## API Access

**Application Process:**
1. Apply for API access at developer.nextdoor.com
2. Receive client ID upon approval
3. Obtain access token (1-year expiration)
4. Use GraphQL endpoint for campaign operations

**Authentication:**
- OAuth 2.0 access tokens
- Token expiration: 1 year
- Secure token storage required

**GraphQL Endpoint:**
`https://ads.nextdoor.com/graphql`

Read `/references/api-authentication.md` for detailed auth setup.

## Campaign Management API

**Create Campaign:**
```graphql
mutation {
  createCampaign(input: {
    name: "Local Business Campaign"
    objective: WEBSITE_VISITS
    budget: 1000
    startDate: "2024-01-01"
  }) {
    id
    name
    status
  }
}
```

**Create Ad Group:**
```graphql
mutation {
  createAdGroup(input: {
    campaignId: "campaign_id"
    name: "Neighborhood Targeting"
    targeting: {
      neighborhoods: ["neighborhood_id_1", "neighborhood_id_2"]
      demographics: {
        age: [AGE_25_34, AGE_35_44]
        homeownership: HOMEOWNER
      }
    }
    bid: 10.00
    dailyBudget: 100
  }) {
    id
    name
  }
}
```

**Create Ad:**
```graphql
mutation {
  createAd(input: {
    adGroupId: "ad_group_id"
    format: IMAGE
    creative: {
      headline: "Special Offer for {{neighborhood}} Neighbors"
      bodyText: "Visit our {{city}} location today!"
      imageUrl: "https://example.com/image.jpg"
      ctaText: "Learn More"
      destinationUrl: "https://example.com/landing"
    }
  }) {
    id
    status
  }
}
```

Read `/references/campaign-api-reference.md` for complete API documentation.

## Conversion API (CAPI)

**Why CAPI:**
- Bypasses ad blockers and browser limitations
- Tracks offline conversions (phone calls, in-store visits)
- More accurate than pixel-only tracking
- Resilient to connectivity issues

**Implementation:**
1. Capture Nextdoor Click ID (ndclid) from URL
2. Store ndclid with user session
3. Send conversion events server-to-server
4. Hash customer information for privacy

**Send Conversion Event:**
```python
import requests
import hashlib

def send_conversion(ndclid, event_name, value, email):
    url = "https://ads.nextdoor.com/v1/conversion"
    
    # Hash email for privacy
    hashed_email = hashlib.sha256(email.encode()).hexdigest()
    
    payload = {
        "ndclid": ndclid,
        "event_name": event_name,
        "event_time": int(time.time()),
        "value": value,
        "currency": "USD",
        "user_data": {
            "email": hashed_email
        }
    }
    
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    response = requests.post(url, json=payload, headers=headers)
    return response.json()
```

Read `/references/conversion-api-guide.md` for CAPI implementation details.

## Reporting API

**Request Performance Report:**
```graphql
query {
  campaignPerformance(
    campaignIds: ["campaign_id"]
    startDate: "2024-01-01"
    endDate: "2024-01-31"
    metrics: [IMPRESSIONS, CLICKS, CONVERSIONS, SPEND, CTR, CPA, ROAS]
  ) {
    campaignId
    impressions
    clicks
    conversions
    spend
    ctr
    cpa
    roas
  }
}
```

**Automated Reporting:**
- Schedule daily/weekly/monthly reports
- Export to CSV, JSON
- Integration with BI tools
- Real-time performance monitoring

Read `/references/reporting-api.md` for reporting capabilities.

## Automation Examples

**Bid Optimization:**
```python
def optimize_nextdoor_bids(api_client, target_cpa=50):
    ad_groups = api_client.get_ad_groups()
    
    for ad_group in ad_groups:
        performance = api_client.get_performance(ad_group.id)
        current_cpa = performance.spend / performance.conversions
        
        if current_cpa > target_cpa * 1.2:
            # CPA too high, decrease bid
            new_bid = ad_group.bid * 0.85
            api_client.update_ad_group(ad_group.id, bid=new_bid)
        elif current_cpa < target_cpa * 0.8:
            # CPA low, increase bid to scale
            new_bid = ad_group.bid * 1.15
            api_client.update_ad_group(ad_group.id, bid=new_bid)
```

**Creative Rotation:**
```python
def rotate_underperforming_creatives(api_client):
    ads = api_client.get_all_ads()
    
    for ad in ads:
        metrics = api_client.get_ad_performance(ad.id)
        
        if metrics.ctr < ad.baseline_ctr * 0.8:
            # CTR dropped 20%, pause and alert
            api_client.pause_ad(ad.id)
            send_alert(f"Ad {ad.id} needs creative refresh")
```

Read `/references/automation-examples.md` for more code samples.

## Using the Reference Files

**`/references/api-authentication.md`** — Read when setting up API access, OAuth authentication, and token management.

**`/references/campaign-api-reference.md`** — Read when implementing campaign, ad group, and ad creation/management via API.

**`/references/conversion-api-guide.md`** — Read when implementing server-side conversion tracking with CAPI.

**`/references/reporting-api.md`** — Read when building custom reporting solutions or integrating with analytics platforms.

**`/references/automation-examples.md`** — Read when developing automated bid management, budget optimization, or agentic AI systems.
