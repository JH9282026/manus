# Amazon Ads API Guide for Twitch Advertising

Access Twitch advertising inventory programmatically through Amazon Ads API for campaign management, reporting, and optimization.

## API Access & Authentication

**Requirements:**
- Amazon Ads account with Twitch access
- API credentials (Client ID, Client Secret)
- OAuth 2.0 authorization
- Approved API access tier

**Authentication Flow:**
1. Register for Amazon Ads API access
2. Obtain OAuth credentials
3. Request access token
4. Use token in API requests
5. Refresh tokens before expiration

**Base URL:** `https://advertising-api.amazon.com`

## Campaign Management

**Create Campaign:** POST `/v2/sp/campaigns`
**Update Campaign:** PUT `/v2/sp/campaigns`
**Get Campaigns:** GET `/v2/sp/campaigns`
**Archive Campaign:** DELETE `/v2/sp/campaigns/{campaignId}`

**Key Parameters:**
- Campaign name, budget, dates
- Targeting parameters
- Bid strategy
- Placement preferences

## Reporting API

**Request Report:** POST `/v2/reports`
**Get Report Status:** GET `/v2/reports/{reportId}`
**Download Report:** GET report download URL

**Available Metrics:**
- Impressions, clicks, conversions
- Spend, CPM, CPC, CPA, ROAS
- Video completion rates
- Device, placement, audience breakdowns

## Automation Examples

**Python SDK:**
```python
from ad_api.api import sponsored_products

# Initialize client
client = sponsored_products.Campaigns(
    account="ENTITY_ID",
    marketplace=Marketplaces.US,
    access_token="ACCESS_TOKEN"
)

# Create campaign
campaign = client.create_campaigns(
    name="Twitch Campaign",
    budget=1000,
    start_date="2024-01-01"
)
```

**Bid Optimization:**
```python
def optimize_bids(campaigns):
    for campaign in campaigns:
        if campaign.roas > 5.0:
            increase_bid(campaign.id, 0.20)
        elif campaign.roas < 2.0:
            decrease_bid(campaign.id, 0.20)
```
