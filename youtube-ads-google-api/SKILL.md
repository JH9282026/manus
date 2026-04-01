---
name: youtube-ads-google-api
description: Create and manage YouTube advertising campaigns through the Google Ads API, covering video campaign types, targeting options, creative requirements, and performance measurement. Use for YouTube ad campaign setup via Google Ads API, YouTube video ad formats (TrueView, Bumper, Shorts), YouTube audience targeting and remarketing, YouTube campaign bidding strategies, Video Action Campaigns, YouTube Shorts ads, Google Ads API integration for video, and YouTube ad performance reporting.
---

# YouTube Ads via Google API

Create, manage, and optimize YouTube advertising campaigns programmatically through the Google Ads API.

## Overview

YouTube ads are managed through the Google Ads API as video campaign types. This skill covers all YouTube ad formats, campaign setup via the API, targeting options, bidding strategies, creative requirements, and performance measurement. YouTube reaches over 2 billion logged-in users monthly, making it the primary platform for video advertising at scale.

## YouTube Ad Format Selection

| Format | Skippable | Length | Billing | Best For |
|--------|-----------|--------|---------|----------|
| Skippable In-Stream | Yes (after 5s) | No max (15-60s rec) | CPV (30s view) or CPA | Awareness, consideration, conversions |
| Non-Skippable In-Stream | No | 15s max | CPM | Guaranteed message delivery |
| Bumper Ad | No | 6s max | CPM | Brand recall, reach |
| In-Feed Video Ad | N/A (click to play) | No max | CPC | Discovery, channel growth |
| YouTube Shorts Ad | Skippable | 10-60s vertical | CPV or CPA | Mobile-first, younger audiences |
| Masthead | N/A | 30s autoplay (muted) | Reserved CPD/CPM | Product launches, tentpole events |
| Video Action Campaign | Yes | 15s+ recommended | Target CPA or Max Conv | Direct response, conversions |

## Google Ads API Campaign Setup

### Step 1: Create Campaign
```python
campaign = client.get_type("Campaign")
campaign.name = "YouTube Awareness Q1"
campaign.advertising_channel_type = client.enums.AdvertisingChannelTypeEnum.VIDEO
campaign.campaign_budget = budget_resource_name
campaign.status = client.enums.CampaignStatusEnum.PAUSED
campaign.bidding_strategy_type = client.enums.BiddingStrategyTypeEnum.TARGET_CPM
```

### Step 2: Create Ad Group
```python
ad_group = client.get_type("AdGroup")
ad_group.campaign = campaign_resource_name
ad_group.name = "In-Stream Targeting Group"
ad_group.type_ = client.enums.AdGroupTypeEnum.VIDEO_TRUE_VIEW_IN_STREAM
ad_group.cpc_bid_micros = 100000  # $0.10 in micros
```

### Step 3: Create Video Ad
```python
ad_group_ad = client.get_type("AdGroupAd")
video_ad = ad_group_ad.ad.video_ad
video_ad.video.asset = youtube_video_asset_resource_name
video_ad.in_stream.action_button_label = "Learn More"
video_ad.in_stream.action_headline = "Free Trial Available"
```

## Campaign Type by Objective

| Objective | Campaign Subtype | Bid Strategy | Formats Included |
|-----------|-----------------|-------------|------------------|
| Brand Awareness | Video Reach | Target CPM | Bumper + Non-skip + Skippable |
| Consideration | Video Views | Max CPV | Skippable in-stream + In-feed |
| Conversions | Video Action (VAC) | Target CPA / Max Conversions | Skippable + In-feed + Shorts |
| Product/Brand | Video Reach (Efficient) | Target CPM | Bumper + Skippable |
| App Install | App Campaign (Video) | Target CPI | Auto-placed across YouTube |
| Shopping | Video + Product Feed | Target ROAS / Max Conv Value | Shoppable video ads |

## Targeting Options

| Category | Options | API Resource |
|----------|---------|-------------|
| Demographics | Age, gender, parental status, household income | `DemographicCriteria` |
| Affinity Audiences | Lifestyle interests (e.g., Tech Enthusiasts) | `UserInterestInfo` |
| In-Market Audiences | Active purchase intent (e.g., Auto Buyers) | `UserInterestInfo` |
| Custom Audiences | Keyword + URL + app-based custom segments | `CustomAudienceInfo` |
| Remarketing | YouTube channel viewers, website visitors | `UserListInfo` |
| Customer Match | CRM email/phone lists (hashed) | `CustomerMatchUserListInfo` |
| Placement | Specific YouTube channels, videos, websites | `PlacementInfo` |
| Topic | Content topic categories | `TopicInfo` |
| Keyword (Content) | Videos containing specific keywords | `KeywordInfo` |

## Bidding Strategy Guide

| Strategy | When to Use | Min Budget Rec |
|----------|------------|----------------|
| Target CPM | Awareness/reach campaigns | $20/day |
| Maximum CPV | Consideration; pay per view | $10/day |
| Target CPA | Conversion campaigns with history | $50/day (10× target CPA ideal) |
| Maximize Conversions | New conversion campaigns | $50/day |
| Target ROAS | Shopping/revenue campaigns | $50/day (mature data needed) |

## Creative Requirements and Best Practices

### Video Specs
| Spec | Requirement |
|------|------------|
| File format | MP4 (recommended), MOV, AVI, WMV |
| Resolution | 1920×1080 (16:9) or 1080×1920 (9:16 for Shorts) |
| Max file size | 256GB |
| Audio | AAC-LC; stereo recommended |

### Creative Best Practices
1. **Hook in first 5 seconds** — before skip becomes available; lead with brand, problem, or question
2. **Include brand early and often** — logo watermark + verbal mention in first 5s
3. **Design for sound-off viewing** — use captions/text overlays; 30%+ watch muted
4. **End with clear CTA** — action button text + verbal call-to-action
5. **Optimize for Shorts** — vertical 9:16; fast-paced; 15-30s duration; trending style
6. **Create multiple lengths** — 6s (bumper), 15s (non-skip), 30s (skippable) from one asset
7. **Use companion banner** — 300×60 banner alongside in-stream ads for brand reinforcement

## Performance Metrics and Reporting

```python
query = """
  SELECT campaign.name, metrics.impressions, metrics.video_views,
         metrics.video_view_rate, metrics.average_cpv,
         metrics.conversions, metrics.cost_per_conversion,
         metrics.cost_micros
  FROM video
  WHERE segments.date DURING LAST_30_DAYS
  ORDER BY metrics.cost_micros DESC
"""
response = ga_service.search_stream(customer_id=customer_id, query=query)
```

| Metric | Definition | Benchmark |
|--------|-----------|----------|
| View Rate | Views / Impressions | 15-30% (skippable) |
| CPV | Cost per video view | $0.03-0.10 |
| CPM | Cost per 1,000 impressions | $4-12 |
| Watch time | Avg seconds watched | 11-15s for 30s ads |
| Earned actions | Free likes/shares from paid views | 5-15% bonus |
| Conversion rate | Conversions / interactions | 1-3% (VAC) |
| View-through conversions | Conversions after ad view (no click) | Track separately |

## Using the Reference Files

### When to Read Each Reference

**`/references/fundamentals-and-core-concepts.md`** — Read when setting up Google Ads API access, understanding account hierarchy, or reviewing YouTube's ad ecosystem.

**`/references/campaign-types-and-strategies.md`** — Read when selecting campaign types, configuring subtype-specific settings, or planning multi-format video strategies.

**`/references/google-ads-api-implementation.md`** — Read when writing API integration code, handling authentication, or implementing batch operations.

**`/references/targeting-and-optimization.md`** — Read when building audience segments, configuring remarketing lists, or optimizing targeting for better performance.

**`/references/best-practices-and-compliance.md`** — Read when reviewing ad policies, ensuring compliance with YouTube guidelines, or troubleshooting ad disapprovals.
