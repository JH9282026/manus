---
name: reddit-ads-api-automation
description: Automate Reddit advertising campaigns through the Reddit Ads API including campaign creation, audience targeting by subreddit and interest, bid management, and performance reporting. Use for Reddit ad automation, subreddit targeting strategy, Reddit Ads API integration, Reddit conversion tracking, community-based advertising, interest-based Reddit targeting, Reddit ad creative formats, and programmatic Reddit campaign management.
---

# Reddit Ads API Automation

Programmatically create, manage, and optimize Reddit advertising campaigns through the Reddit Ads API.

## Overview

The Reddit Ads API (base URL: `https://ads-api.reddit.com/api/v3`) provides full CRUD control over ad campaigns, ad groups, ads, audiences, and reporting. Reddit's unique community-driven structure enables powerful subreddit and interest-based targeting that reaches highly engaged niche audiences. This skill covers API authentication, campaign automation workflows, targeting strategies, bid optimization, and reporting.

## API Authentication Setup

| Step | Action | Details |
|------|--------|--------|
| 1 | Register OAuth app | reddit.com/prefs/apps → create "web app" |
| 2 | Obtain client credentials | `client_id` and `client_secret` from app settings |
| 3 | Request authorization | OAuth 2.0 authorization code flow |
| 4 | Required scopes | `ads:read` for GET; `ads:manage` for POST/PATCH/DELETE |
| 5 | Exchange for access token | `POST https://www.reddit.com/api/v1/access_token` |
| 6 | Include in requests | `Authorization: Bearer {access_token}` header |

## Campaign Structure

```
Ad Account
├── Campaign (objective, funding_instrument)
│   ├── Ad Group (targeting, bid, schedule, budget)
│   │   ├── Ad (creative: headline, media, CTA)
│   │   └── Ad
│   └── Ad Group
└── Campaign
```

## Core API Endpoints

| Operation | Method | Endpoint |
|-----------|--------|----------|
| List campaigns | GET | `/accounts/{account_id}/campaigns` |
| Create campaign | POST | `/accounts/{account_id}/campaigns` |
| Update campaign | PATCH | `/accounts/{account_id}/campaigns/{campaign_id}` |
| List ad groups | GET | `/accounts/{account_id}/adgroups` |
| Create ad group | POST | `/accounts/{account_id}/adgroups` |
| Create ad | POST | `/accounts/{account_id}/ads` |
| Get reporting | GET | `/accounts/{account_id}/reports` |
| Manage audiences | POST | `/accounts/{account_id}/custom_audiences` |

## Reddit Ad Formats

| Format | Placement | Specs | Best For |
|--------|-----------|-------|----------|
| Promoted Post — Link | Feed | Headline + thumbnail + URL | Traffic, conversions |
| Promoted Post — Text | Feed | Headline + body text | Community engagement |
| Promoted Post — Image | Feed | Headline + image (1200×628) | Brand awareness |
| Promoted Post — Video | Feed | Headline + video (MP4, ≤30min) | Storytelling, product demos |
| Promoted Post — Carousel | Feed | 2-6 cards with images | Multi-product showcase |
| Conversation Placement | Comments | Native to comment threads | High engagement |

## Targeting Strategy for Reddit

| Targeting Type | Description | Best Practice |
|---------------|-------------|---------------|
| Subreddit targeting | Show ads in specific subreddits | Target 5-15 related subreddits per ad group |
| Interest targeting | Reddit-defined interest categories | Broader reach than subreddit targeting |
| Community targeting | Groups of related subreddits | Balance between reach and relevance |
| Location | Country, state/region, DMA | Required for localized offers |
| Device | Desktop, iOS, Android | Desktop users have higher purchase intent |
| Custom Audiences | Email/device ID lists | Retargeting and CRM-based campaigns |
| Pixel retargeting | Reddit Pixel website visitors | Cart abandoners, page viewers |

### Reddit-Specific Targeting Tips

1. **Research subreddits first** — browse target subreddits to understand tone and content norms
2. **Avoid overly promotional copy** — Reddit users downvote overt sales pitches; use informational/conversational tone
3. **Match creative to subreddit culture** — meme-friendly for casual subs; data-driven for professional subs
4. **Use subreddit + interest layering** — narrow subreddit targeting with interest overlaps
5. **Separate desktop and mobile ad groups** — performance varies significantly by device on Reddit

## Bid and Budget Management

| Objective | Bid Type | Recommended Start |
|-----------|----------|-------------------|
| Brand Awareness | CPM | $3-8 CPM |
| Traffic | CPC | $0.50-2.00 CPC |
| Conversions | CPC or Target CPA | $1.00-5.00 CPC |
| Video Views | CPV | $0.02-0.06 CPV |
| App Installs | CPI | $2.00-6.00 CPI |

**Minimum daily budget:** $5/day per ad group

## Automation Patterns

| Pattern | Implementation |
|---------|---------------|
| Campaign cloning | GET campaign → modify params → POST new campaign |
| Budget pacing | Poll spend via reports API → PATCH budget adjustments |
| Creative rotation | Create multiple ads per ad group; pause underperformers via PATCH |
| Audience refresh | Rebuild custom audiences on schedule via POST |
| Alert on overspend | Poll reports API hourly; trigger alert if spend > threshold |

## API Limitations

| Limitation | Workaround |
|-----------|------------|
| No webhooks | Poll endpoints with 15-60 min intervals |
| Undocumented rate limits | Implement exponential backoff on HTTP 429; check `X-RateLimit-Remaining` |
| Cursor-based pagination | Use `after` parameter; max 100 per page |
| No email invitations | User must accept invite via Reddit notification |

## Performance Benchmarks

| Metric | Reddit Benchmark | Notes |
|--------|-----------------|-------|
| CTR | 0.3-1.0% | Higher in niche subreddits |
| CPC | $0.50-3.00 | Varies by vertical and targeting |
| CPM | $3.00-10.00 | Lower than Meta/LinkedIn |
| Conversion rate | 1-3% | Strong for tech and gaming verticals |
| Video completion | 30-50% | Short-form (<30s) performs best |

## Using the Reference Files

### When to Read Each Reference

**`/references/api-authentication-setup.md`** — Read when configuring OAuth 2.0 credentials, managing access tokens, or troubleshooting authentication errors.

**`/references/campaign-management-automation.md`** — Read when building automated campaign creation workflows, implementing bulk operations, or managing campaign lifecycle.

**`/references/bidding-optimization-automation.md`** — Read when tuning bid strategies, implementing automated budget rules, or optimizing cost efficiency.

**`/references/reporting-analytics-automation.md`** — Read when pulling performance data, building automated reports, or analyzing subreddit-level performance breakdowns.
