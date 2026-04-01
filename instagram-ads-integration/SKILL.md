---
name: instagram-ads-integration
description: Build and manage Instagram advertising campaigns programmatically through the Meta Marketing API, covering ad creation, audience targeting, creative formats, and performance reporting. Use for Instagram feed ads, Stories ads, Reels ads, Shopping ads, Instagram-specific placement optimization, creative asset management via the API, audience insights for Instagram, and integrating Instagram ad delivery with broader Meta campaign workflows.
---

# Instagram Ads Integration

Create, manage, and optimize Instagram advertising campaigns programmatically using the Meta Marketing API.

## Overview

Instagram ads are managed through the Meta Marketing API as a placement within the Meta advertising ecosystem. This skill covers Instagram-specific ad formats, placement configuration, creative requirements, audience targeting for Instagram users, and reporting on Instagram ad performance. All API operations use the same campaign hierarchy as Meta ads (Campaign → Ad Set → Ad) with Instagram-specific placement and creative considerations.

## Instagram Ad Format Selection

| Format | Placement | Aspect Ratio | Max Duration | Best For |
|--------|-----------|-------------|-------------|----------|
| Image — Feed | Feed | 1:1 or 4:5 | N/A | Product showcases, brand awareness |
| Video — Feed | Feed | 1:1 or 4:5 | 60 min | Storytelling, demonstrations |
| Carousel — Feed | Feed | 1:1 or 4:5 | 10 cards | Multi-product, step-by-step |
| Stories — Image | Stories | 9:16 | 5s display | Flash promotions, swipe-up CTAs |
| Stories — Video | Stories | 9:16 | 120s | Immersive brand experiences |
| Reels | Reels tab | 9:16 | 90s | Trend-driven, UGC-style content |
| Shopping | Feed/Explore | 1:1 or 4:5 | N/A | Direct product tagging |
| Explore | Explore tab | 1:1 or 4:5 | Varies | Discovery and reach |

## API Campaign Setup for Instagram

### Step 1: Create Campaign
```
POST /act_{ad_account_id}/campaigns
objective: OUTCOME_SALES | OUTCOME_LEADS | OUTCOME_AWARENESS | OUTCOME_TRAFFIC
special_ad_categories: [] (or applicable category)
```

### Step 2: Create Ad Set with Instagram Placement
```
POST /act_{ad_account_id}/adsets
targeting: { publisher_platforms: ["instagram"], instagram_positions: ["stream", "story", "reels", "explore"] }
optimization_goal: REACH | LINK_CLICKS | CONVERSIONS | IMPRESSIONS
billing_event: IMPRESSIONS
```

### Step 3: Upload Creative and Create Ad
```
POST /act_{ad_account_id}/adcreatives
object_story_spec: { instagram_actor_id: "{ig_account_id}", ... }
POST /act_{ad_account_id}/ads
adset_id: "{adset_id}"
creative: { creative_id: "{creative_id}" }
```

## Instagram-Specific Targeting

| Targeting Type | Description | API Parameter |
|---------------|-------------|---------------|
| Publisher platform | Restrict to Instagram only | `publisher_platforms: ["instagram"]` |
| Instagram positions | Select feed, stories, reels, explore | `instagram_positions: [...]` |
| Interest targeting | Lifestyle, shopping, entertainment | `interests: [{id, name}]` |
| Custom Audiences | Website visitors, email lists, IG engagers | `custom_audiences: [{id}]` |
| Lookalike Audiences | Similar to existing customers | `custom_audiences: [{id}]` (LAL type) |
| Age/Gender/Location | Standard demographics | `age_min`, `age_max`, `genders`, `geo_locations` |

## Creative Best Practices

1. **Design for mobile-first** — 99% of Instagram users are on mobile; use vertical formats
2. **Capture attention in 3 seconds** — lead with movement, bold visuals, or a hook
3. **Use 9:16 for Stories and Reels** — full-screen vertical maximizes screen real estate
4. **Keep text overlay minimal** — Instagram penalizes heavy text on images
5. **Include sound design for Reels** — trending audio boosts engagement and delivery
6. **Tag products in Shopping ads** — enable direct checkout from the ad creative
7. **A/B test creative variations** — test 3-5 variations per ad set for optimization
8. **Refresh creatives every 2-4 weeks** — combat ad fatigue on high-frequency placements

## Performance Reporting via API

```
GET /{ad_id}/insights?fields=impressions,reach,clicks,spend,actions,
  cost_per_action_type,video_avg_time_watched_actions
  &breakdowns=publisher_platform,platform_position
  &date_preset=last_30d
```

| Metric | Description | Good Benchmark |
|--------|-------------|----------------|
| CPM | Cost per 1,000 impressions | $5-12 (varies by vertical) |
| CTR | Click-through rate | 0.5-1.5% feed; 0.3-0.8% stories |
| CPC | Cost per click | $0.40-1.20 |
| Conversion rate | Actions / clicks | 2-5% (e-commerce) |
| Video completion rate | Reels/Stories watch-through | 15-30% |
| ROAS | Return on ad spend | 3-5× target for e-commerce |

## Common API Errors and Fixes

| Error Code | Meaning | Fix |
|-----------|---------|-----|
| 100 | Invalid parameter | Check field names and value types |
| 1487390 | Ad creative not compatible with placement | Verify aspect ratio matches placement |
| 2446228 | Instagram account not connected | Link IG account in Business Manager |
| 368 | Temporary rate limit | Implement exponential backoff |
| 190 | Access token expired | Refresh token via OAuth flow |

## Using the Reference Files

### When to Read Each Reference

**`/references/meta-marketing-api-fundamentals.md`** — Read when setting up API access, configuring authentication, or understanding the campaign object hierarchy.

**`/references/programmatic-campaign-management.md`** — Read when building automated campaign creation workflows, managing ad sets at scale, or implementing bulk operations.

**`/references/targeting-optimization-strategies.md`** — Read when configuring audience targeting, building Custom or Lookalike Audiences, or optimizing delivery for Instagram placements.

**`/references/insights-api-reporting.md`** — Read when building performance dashboards, pulling Instagram-specific metrics, or setting up automated reporting.

**`/references/authentication-security.md`** — Read when implementing OAuth flows, managing access tokens, or troubleshooting permission errors.
