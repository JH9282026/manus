---
name: nextdoor-ads-campaign-management
description: "Manage Nextdoor advertising campaigns for hyperlocal targeting and neighborhood marketing. Create image, video, carousel, and lead generation ads in Newsfeed, For Sale & Free, and Right Hand Rail placements. Use for: local business advertising, neighborhood targeting, demographic and interest-based campaigns, custom audience retargeting, lead generation, conversion tracking with Nextdoor Pixel/CAPI, and optimizing campaigns for local customer acquisition."
---

# Nextdoor Ads Campaign Management

Manage hyperlocal advertising campaigns on Nextdoor to reach neighbors and local communities with targeted ads.

## Overview

Nextdoor Ads Manager enables businesses to advertise to verified neighbors in specific neighborhoods. The platform offers powerful local targeting, multiple ad formats, and tools for lead generation and conversion tracking. Approximately 1 in 3 US households use Nextdoor, with 90%+ being primary household shoppers and 77% homeowners.

**Key Capabilities:**
- Hyperlocal targeting (neighborhood-level precision)
- Multiple ad formats (Image, Video, Carousel, Lead Gen)
- Custom audiences (retargeting, lookalikes, exclusions)
- Nextdoor Pixel and Conversion API (CAPI) tracking
- AI-powered optimization (Click and Conversion Optimization)
- Geo-personalization and weather targeting

## Ad Format Selection

| Format | Placements | Best For | Specs |
|--------|-----------|----------|-------|
| Image Ad | Newsfeed, For Sale & Free, Right Hand Rail | Brand awareness, promotions, local offers | 1200x628 or 1200x1200, max 150MB |
| Video Ad | Newsfeed | Engagement, storytelling, product demos | 2-120s, 16:9 or 1:1, max 500MB |
| Carousel Ad | Newsfeed | Multiple products, features, storytelling | 2-10 images, 1200x1200, max 150MB each |
| Lead Gen Ad | Newsfeed | Lead capture, contact collection, sign-ups | Image or video + form (2-11 fields) |

Read `/references/ad-format-specifications.md` for complete technical specs.

## Targeting Options

**Nextdoor Audience Models:**
- Pre-built audiences for optimal performance
- Based on platform behavior and demographics

**Demographic Targeting:**
- Homeownership status
- Household income levels
- Age ranges
- Gender

**Interest Targeting:**
- Home & Garden, Real Estate, Professional Services
- Food & Beverage, Retail, Medical & Dental
- Personal Care, Health & Wellness, Pet Care, Family Care

**Custom Audiences:**
- Retarget past customers (upload customer lists)
- Exclude existing customers
- Lookalike audiences (find similar neighbors)

**Geographic Targeting:**
- Neighborhood-level precision
- City, ZIP code, or radius targeting
- Up to 50-mile radius

Read `/references/targeting-strategies.md` for advanced targeting tactics.

## Campaign Setup

**Campaign Objectives:**
- Increase website visits
- Promote sales or events
- Increase direct messages/leads
- Drive foot traffic

**Ad Group Configuration:**
- Select placements (Newsfeed, For Sale & Free, Right Hand Rail)
- Define target audience
- Set bid amount (CPM or CPC)
- Configure daily budget
- Set campaign duration and schedule

**Creative Development:**
- Follow Nextdoor creative best practices
- Sound like a neighbor (conversational tone)
- Localize content (use {{neighborhood}} or {{city}})
- Feature local imagery and personas
- Minimize text in images (<25% coverage)
- Clear call-to-action

Read `/references/campaign-setup-guide.md` for step-by-step instructions.

## Bidding & Optimization

**Bidding Strategies:**
- CPM (Cost Per Mille): Pay per 1,000 impressions
- CPC (Cost Per Click): Pay per click (with Click Optimization)

**AI-Powered Optimization:**
- Click Optimization: Automatically optimize for higher CTR (134% avg lift)
- Conversion Optimization: Optimize for lower CPA (35% avg improvement)

**Budget Management:**
- Daily budgets starting as low as $5
- Campaign lifetime budgets
- Automated pacing
- Performance-based reallocation

**Optimization Tactics:**
- Monitor CTR and adjust creative when it drops 20%
- Reallocate budget to high-ROAS segments
- Test multiple creative variations
- Use geo-personalization (17% CTR increase)
- Leverage weather targeting for relevant campaigns

Read `/references/optimization-guide.md` for detailed optimization strategies.

## Conversion Tracking

**Nextdoor Pixel:**
- JavaScript pixel for website tracking
- Track page views, add-to-cart, purchases
- Retargeting capabilities
- Easy implementation

**Conversion API (CAPI):**
- Server-to-server tracking
- More accurate than pixel (bypasses ad blockers)
- Offline conversion tracking
- Requires Nextdoor Click ID (ndclid)

**Measurement:**
- Conversion attribution
- Brand lift studies
- Foot traffic analysis
- Integration with measurement partners

Read `/references/conversion-tracking.md` for implementation details.

## Using the Reference Files

**`/references/ad-format-specifications.md`** — Read when creating ads to understand technical requirements for each format and placement.

**`/references/targeting-strategies.md`** — Read when setting up audience targeting, creating custom audiences, or optimizing reach.

**`/references/campaign-setup-guide.md`** — Read when launching new campaigns for step-by-step setup instructions.

**`/references/optimization-guide.md`** — Read when analyzing performance and implementing optimization tactics.

**`/references/conversion-tracking.md`** — Read when implementing Nextdoor Pixel or Conversion API for tracking and attribution.

## References

- [Ad Format Specifications](references/ad-format-specifications.md)
- [Campaign Setup Guide](references/campaign-setup-guide.md)
- [Targeting Strategies](references/targeting-strategies.md)
