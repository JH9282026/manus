---
name: tiktok-ads-api-management
description: Build and manage TikTok advertising campaigns programmatically through the TikTok Marketing API, covering campaign creation, audience targeting, creative management, and performance reporting. Use for TikTok Ads API integration, TikTok campaign automation, Spark Ads implementation, TikTok Pixel setup, TikTok audience management, TikTok ad creative tools, TikTok Ads reporting API, and TikTok catalog and Shopping ads management.
---

# TikTok Ads API Management

Programmatically create, manage, and optimize TikTok advertising campaigns using the TikTok Marketing API.

## Overview

The TikTok Marketing API (part of TikTok for Business API) provides programmatic access to TikTok Ads Manager for campaign management, creative tools, audience targeting, catalog management, and reporting. The API follows a campaign hierarchy of Advertiser → Campaign → Ad Group → Ad and supports batch operations for managing campaigns at scale.

## API Access Setup

| Step | Action | Details |
|------|--------|--------|
| 1 | Register TikTok for Business account | business.tiktok.com |
| 2 | Apply for developer access | developers.tiktok.com → My Apps |
| 3 | Create application | Specify name, redirect URL, permissions scope |
| 4 | Request approval | Review takes 2-3 business days |
| 5 | Authorize advertiser accounts | Advertiser grants access via OAuth flow |
| 6 | Generate access token | Exchange `auth_code` + `secret` + `app_id` for token |

### Permission Scopes

| Scope | Access Level |
|-------|-------------|
| Ad Account Management | Read/write ad accounts |
| Campaign Management | Create/update campaigns, ad groups, ads |
| Audience Management | Custom Audiences, Lookalike Audiences |
| Creative Management | Upload images, video; manage creative tools |
| Reporting | Pull performance metrics and reports |
| Catalog Management | Product feeds and Shopping ads |

## Campaign Hierarchy and API Endpoints

| Level | Endpoint | Key Parameters |
|-------|----------|----------------|
| Campaign | `/campaign/create/` | `advertiser_id`, `campaign_name`, `objective_type`, `budget`, `budget_mode` |
| Ad Group | `/adgroup/create/` | `campaign_id`, `placement_type`, `targeting`, `budget`, `schedule`, `optimization_goal`, `bid_type` |
| Ad | `/ad/create/` | `adgroup_id`, `ad_name`, `creative_type`, `creatives` |
| Batch read | `/campaign/get/`, `/adgroup/get/`, `/ad/get/` | `advertiser_id`, `filtering`, `page`, `page_size` (max 1000) |

## Campaign Objectives

| Objective | Optimization Goals | Best For |
|-----------|-------------------|----------|
| REACH | Impressions | Brand awareness |
| TRAFFIC | Clicks | Website visits |
| VIDEO_VIEWS | Video views (6s/15s) | Content engagement |
| LEAD_GENERATION | Lead form submissions | B2B/service leads |
| COMMUNITY_INTERACTION | Followers, profile visits | Account growth |
| APP_PROMOTION | App installs, events | Mobile app growth |
| CONVERSIONS | Purchase, add-to-cart, sign-up | E-commerce, direct response |
| PRODUCT_SALES | Catalog-driven conversions | Shopping/catalog ads |

## Ad Format Guide

| Format | Aspect Ratio | Duration | Specs |
|--------|-------------|----------|-------|
| In-Feed Video | 9:16, 1:1, 16:9 | 5-60s (9-15s optimal) | MP4/MOV; ≤500MB; ≥720p |
| Spark Ads | Organic post format | Varies | Boost existing TikTok posts |
| Image Ad | 9:16, 1:1 | N/A | JPG/PNG; ≤100KB for thumbnail |
| Carousel Ad | 1:1 | 2-35 images | Shopping/catalog format |
| Playable Ad | 9:16 | Interactive | HTML5; ≤2MB; for app installs |
| Collection Ad | 9:16 video + product cards | 5-60s | Product catalog required |

## Targeting Options

| Category | Options | API Parameter |
|----------|---------|---------------|
| Location | Country, state, city, DMA | `location_ids` |
| Age | 13-17, 18-24, 25-34, 35-44, 45-54, 55+ | `age_groups` |
| Gender | Male, Female, Unlimited | `gender` |
| Language | User interface language | `languages` |
| Interest | 15+ interest categories with subcategories | `interest_category_ids` |
| Behavior | Video interaction, creator interaction, hashtag | `action_categories` |
| Device | OS, device model, carrier, connection type | `operating_systems`, `device_models` |
| Custom Audience | CRM uploads, pixel retargeting, app activity | `audience_ids` |
| Lookalike Audience | Based on Custom Audience seed | `audience_ids` (lookalike type) |

## Spark Ads Implementation

Spark Ads boost organic TikTok content as paid ads, preserving engagement metrics:

1. **Creator posts video** on their TikTok account
2. **Creator generates authorization code** via TikTok Creator Tools → Ad Settings
3. **Advertiser submits code** via API: `POST /tt_video/authorize/` with `auth_code`
4. **Create ad** using authorized video as creative material
5. **All engagement** (likes, comments, shares) attributes back to original post

## Reporting API

```
POST /reports/integrated/get/
  advertiser_id, report_type: "BASIC",
  data_level: "AUCTION_AD",
  dimensions: ["ad_id", "stat_time_day"],
  metrics: ["spend", "impressions", "clicks", "conversions",
            "cpc", "cpm", "ctr", "conversion_rate", "cost_per_conversion"],
  start_date, end_date,
  page, page_size
```

## Performance Benchmarks

| Metric | TikTok Benchmark | Notes |
|--------|-----------------|-------|
| CPM | $3-10 | Lower for broad targeting |
| CPC | $0.30-1.50 | In-feed video clicks |
| CTR | 0.5-1.5% | Higher with UGC-style creative |
| CVR | 1-3% | E-commerce conversion rate |
| Video view rate (6s) | 15-30% | Short hooks critical |
| Spark Ads engagement | 2-4× vs standard | Due to organic authenticity |

## Creative Best Practices

1. **Hook in first 2 seconds** — movement, text overlay, or direct address to camera
2. **Use trending sounds/music** — licensed audio from TikTok Commercial Music Library
3. **UGC-style outperforms polished** — authentic, creator-like content gets higher engagement
4. **Vertical 9:16 only** — full-screen vertical is the only format that performs well
5. **Include strong CTA** — text overlay + verbal CTA in final 3 seconds
6. **Refresh every 7-14 days** — TikTok creative fatigue is faster than other platforms
7. **Use Spark Ads when possible** — 2-4× engagement lift; preserves social proof

## Using the Reference Files

### When to Read Each Reference

**`/references/tiktok-ads-api-overview.md`** — Read when setting up API access, understanding authentication flows, or reviewing available endpoints and capabilities.

**`/references/tiktok-campaign-automation.md`** — Read when building automated campaign workflows, implementing batch operations, or managing campaign lifecycle programmatically.
