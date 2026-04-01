---
name: meta-ads-targeting-audiences
description: Build and manage Meta advertising audiences including Custom Audiences, Lookalike Audiences, Saved Audiences, and Advantage+ broad targeting for Facebook and Instagram campaigns. Use for audience creation via the Meta Marketing API, Custom Audience uploads from CRM data, website visitor retargeting with Meta Pixel, Conversions API audience building, Lookalike Audience expansion, detailed interest and demographic targeting, audience exclusion strategies, and audience testing frameworks.
---

# Meta Ads Targeting & Audiences

Build, manage, and optimize audiences for Meta advertising campaigns across Facebook and Instagram.

## Overview

Meta's targeting system offers layered audience capabilities from broad demographic targeting to precise Custom Audiences built from first-party data. This skill covers all audience types, creation methods (UI and API), Pixel and Conversions API integration, Lookalike expansion strategies, and testing frameworks for systematic audience optimization.

## Audience Type Selection

| Audience Type | Source | Size Range | Funnel Stage | Refresh |
|--------------|--------|------------|-------------|--------|
| Custom — CRM | Email/phone list upload | 1,000+ matches | Bottom | Manual or automated |
| Custom — Website | Meta Pixel events | Varies by traffic | Middle-Bottom | Auto (rolling window) |
| Custom — App | App SDK events | Varies by installs | Middle-Bottom | Auto |
| Custom — Engagement | IG/FB interactions | Varies | Middle | Auto (rolling window) |
| Custom — Video | Video view thresholds | Varies | Top-Middle | Auto |
| Custom — Lead Form | Lead Gen Form opens/submits | Varies | Bottom | Auto |
| Lookalike | Based on any Custom Audience | 1-10% of country | Top-Middle | Auto (every 3-7 days) |
| Saved/Core | Demographics + interests + behaviors | Varies | Top | Static criteria |
| Advantage+ Broad | Minimal constraints; AI-optimized | Broadest | All | Dynamic |

## Custom Audience Creation via API

### CRM-Based Custom Audience
```
POST /act_{ad_account_id}/customaudiences
  name: "Q1 Customers"
  subtype: CUSTOM
  customer_file_source: USER_PROVIDED_ONLY

POST /{audience_id}/users
  payload: {
    schema: ["EMAIL", "PHONE", "FN", "LN"],
    data: [[sha256(email), sha256(phone), sha256(fn), sha256(ln)], ...]
  }
```

**Critical:** All PII must be SHA-256 hashed before upload. Lowercase and trim whitespace before hashing.

### Website Custom Audience (Pixel-based)
```
POST /act_{ad_account_id}/customaudiences
  name: "Website Visitors 30d"
  rule: {
    inclusions: {
      operator: "or",
      rules: [{
        event_sources: [{id: "{pixel_id}", type: "pixel"}],
        retention_seconds: 2592000,
        filter: {operator: "and", filters: [{field: "url", operator: "i_contains", value: "/product"}]}
      }]
    }
  }
```

### Lookalike Audience
```
POST /act_{ad_account_id}/customaudiences
  name: "LAL 1% US — Top Customers"
  subtype: LOOKALIKE
  origin_audience_id: "{source_audience_id}"
  lookalike_spec: {
    type: "similarity",
    country: "US",
    ratio: 0.01
  }
```

## Lookalike Audience Strategy

| LAL Size | Audience Character | Best For |
|----------|-------------------|----------|
| 1% | Most similar to source | High-value conversions, ROAS campaigns |
| 1-3% | Strong similarity | Balanced reach and quality |
| 3-5% | Moderate similarity | Scaling proven campaigns |
| 5-10% | Broad similarity | Awareness and reach objectives |

**Source audience quality matters more than size.** A 1,000-person list of best customers outperforms a 50,000-person email blast list.

## Conversions API (CAPI) for Audience Building

Server-side events sent via CAPI create more reliable Custom Audiences than browser-only Pixel:

| Event | Use for Audience | Retention Window |
|-------|-----------------|------------------|
| `Purchase` | Buyer audiences, LAL sources | 180 days max |
| `AddToCart` | High-intent retargeting | 30-60 days |
| `Lead` | Lead nurture sequences | 90 days |
| `ViewContent` | Broad retargeting pools | 14-30 days |
| `PageView` | General website visitors | 7-30 days |

**Always deduplicate** Pixel + CAPI events using the `event_id` parameter to avoid inflated audience counts.

## Targeting Best Practices

1. **Use Advantage+ broad targeting first** — Meta's AI targeting often outperforms manual interest targeting in 2025
2. **Layer exclusions, not inclusions** — exclude converters and existing customers rather than narrowing interests
3. **Minimum 1,000 matches for Custom Audiences** — below this, delivery is unreliable
4. **Source LALs from highest-value customers** — top 20% by LTV, not just all purchasers
5. **Test LAL sizes systematically** — run 1%, 3%, 5% as separate ad sets with equal budget
6. **Refresh CRM audiences monthly** — stale data degrades match rates and performance
7. **Use engagement audiences for warm retargeting** — video viewers 50%+ and IG engagers are high-intent
8. **Keep retention windows tight for retargeting** — 7-14 days for ViewContent; 30 days for AddToCart

## Audience Testing Framework

| Test Type | Setup | What You Learn |
|-----------|-------|---------------|
| LAL size test | 1%, 3%, 5% in separate ad sets | Optimal expansion ratio |
| Source audience test | Purchasers vs leads vs engagers as LAL source | Best seed audience |
| Broad vs targeted | Advantage+ vs detailed targeting ad sets | Whether AI beats manual |
| Exclusion impact | With vs without customer exclusions | Wasted spend on existing buyers |
| Retention window | 7d vs 30d vs 90d website audiences | Recency impact on conversion |

## Using the Reference Files

### When to Read Each Reference

**`/references/audience-types-overview.md`** — Read when selecting which audience type to create or when explaining audience options to a stakeholder.

**`/references/advanced-targeting-strategies.md`** — Read when building complex targeting with boolean logic, layered exclusions, or multi-source audience combinations.

**`/references/pixel-conversions-api-implementation.md`** — Read when setting up Meta Pixel, implementing Conversions API, configuring event deduplication, or debugging tracking issues.

**`/references/audience-testing-optimization.md`** — Read when designing audience split tests, analyzing test results, or scaling winning audiences.

**`/references/campaign-structure-best-practices.md`** — Read when organizing campaigns around audience segments, setting budget allocation across audiences, or implementing Campaign Budget Optimization.
