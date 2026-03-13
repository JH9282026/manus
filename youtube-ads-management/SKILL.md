---
name: youtube-ads-management
description: "YouTube advertising through Google Ads API including TrueView ads, bumper ads, non-skippable ads, and discovery ads. Covers video ad formats, targeting options, bidding strategies, and YouTube-specific campaign management. Use for: creating YouTube ad campaigns, implementing video advertising, targeting YouTube audiences, and managing video ad performance via Google Ads API."
---

# YouTube Ads Management

YouTube advertising campaign management through Google Ads API for video advertising at scale.

## Overview

Comprehensive guide to YouTube advertising through Google Ads API. This skill covers all YouTube ad formats, targeting options, bidding strategies, and automation workflows for video advertising.

## API Authentication

### OAuth 2.0
```python
from google.ads.googleads.client import GoogleAdsClient

# Load credentials
client = GoogleAdsClient.load_from_storage("google-ads.yaml")
```

## YouTube Ad Formats

### TrueView In-Stream (Skippable)
- **Duration**: Any length
- **Skip**: After 5 seconds
- **Billing**: CPV (cost per view after 30 seconds or interaction)
- **Use Case**: Awareness, consideration

### TrueView Discovery
- **Placement**: Search results, related videos, homepage
- **Billing**: CPC (cost per click)
- **Use Case**: Discovery, consideration

### Bumper Ads
- **Duration**: 6 seconds
- **Skip**: Non-skippable
- **Billing**: CPM
- **Use Case**: Brand awareness, reach

### Non-Skippable In-Stream
- **Duration**: 15-20 seconds
- **Skip**: Non-skippable
- **Billing**: CPM
- **Use Case**: Brand awareness, guaranteed views

## Campaign Creation

### Create Video Campaign
```python
from google.ads.googleads.client import GoogleAdsClient

campaign_operation = client.get_type("CampaignOperation")
campaign = campaign_operation.create

campaign.name = "YouTube Video Campaign"
campaign.advertising_channel_type = client.enums.AdvertisingChannelTypeEnum.VIDEO
campaign.status = client.enums.CampaignStatusEnum.PAUSED
campaign.bidding_strategy_type = client.enums.BiddingStrategyTypeEnum.TARGET_CPM

# Budget
campaign.campaign_budget = f"customers/{customer_id}/campaignBudgets/{budget_id}"

# Video ad settings
campaign.video_brand_safety_suitability = client.enums.BrandSafetySuitabilityEnum.EXPANDED_INVENTORY

response = campaign_service.mutate_campaigns(
    customer_id=customer_id,
    operations=[campaign_operation]
)
```

## Targeting Options

### Demographics
- Age
- Gender
- Parental status
- Household income

### Interests & Affinity
- Affinity audiences
- In-market audiences
- Custom intent audiences

### Placements
- Specific YouTube channels
- Specific videos
- YouTube search results

### Topics & Keywords
- Video topics
- Keyword targeting

## Video Creative Specs

### Recommended Specs
- **Resolution**: 1920 x 1080 (Full HD)
- **Aspect Ratio**: 16:9 (horizontal), 9:16 (vertical for Shorts)
- **Format**: MP4, MOV, AVI
- **Max File Size**: 256 GB
- **Max Length**: 12 hours (varies by format)

## Using the Reference Files

**`/references/youtube-api-reference.md`** — Read for complete Google Ads API documentation for video campaigns.

**`/references/youtube-creative-guide.md`** — Read for video best practices, format selection, and performance optimization.
