---
name: microsoft-ads-audience-network
description: "Create and manage native advertising campaigns on the Microsoft Audience Network. Use for: Microsoft native ads, audience targeting with LinkedIn data, responsive ad creation, audience campaign setup, Microsoft Advertising display campaigns, demographic targeting, remarketing on Microsoft network, and cross-device native advertising."
---

# Microsoft Ads Audience Network

Create and optimize native advertising campaigns on the Microsoft Audience Network using LinkedIn profile targeting and AI-powered audience signals.

## Overview

The Microsoft Audience Network (MSAN) delivers native ads across Microsoft properties (MSN, Outlook.com, Microsoft Edge) and premium partner sites. Its unique advantage is access to LinkedIn professional profile data for B2B targeting — the only native ad platform with job title, company, industry, and seniority targeting. MSAN campaigns complement search by reaching users during content consumption rather than active search.

## Campaign Setup Guide

### Campaign Configuration

| Setting | Options | Recommendation | Reference |
|---------|---------|---------------|-----------|
| Campaign type | Audience | Required for MSAN | `/references/01-audience-network-fundamentals.md` |
| Goal | Conversions, Traffic, Brand Awareness | Match to business objective | `/references/01-audience-network-fundamentals.md` |
| Budget | Daily or shared | Start with $50–$100/day for testing | `/references/03-campaign-optimization-best-practices.md` |
| Bid strategy | Enhanced CPC, Maximize Conversions, Target CPA | Enhanced CPC for testing, Target CPA for scale | `/references/03-campaign-optimization-best-practices.md` |
| Location | Country, state, city, radius | Match to business geography | `/references/02-targeting-options-strategies.md` |
| Schedule | All day or specific hours | Start all day, optimize later | `/references/03-campaign-optimization-best-practices.md` |

### Ad Format Options

| Format | Specs | Best For | Reference |
|--------|------|----------|-----------|
| Responsive Ad | Headlines (1–15), descriptions (1–5), images (1–16) | Most campaigns — auto-optimizes layout | `/references/04-native-advertising-creative-strategy.md` |
| Image Ad | Single image + text overlay | Brand awareness, simple message | `/references/04-native-advertising-creative-strategy.md` |
| Feed Ad | Appears in content feeds | Content promotion | `/references/04-native-advertising-creative-strategy.md` |
| Video Ad (limited) | In-feed video placement | Brand storytelling | `/references/04-native-advertising-creative-strategy.md` |

### Responsive Ad Asset Requirements

| Asset | Count | Specifications |
|-------|-------|---------------|
| Short headline | 1–15 | 30 characters max each |
| Long headline | 1–5 | 90 characters max each |
| Description | 1–5 | 90 characters max each |
| Image (landscape) | 1–16 | 1200×628 minimum, 1.91:1 ratio |
| Image (square) | Optional | 1200×1200 minimum, 1:1 ratio |
| Business name | 1 | 25 characters max |
| Final URL | 1 | Landing page URL |

## LinkedIn Profile Targeting

### Available LinkedIn Targeting Dimensions

| Dimension | Granularity | Examples | B2B Value |
|-----------|-------------|---------|-----------|
| Company | Specific companies | Microsoft, Salesforce, HubSpot | Very High — account-based targeting |
| Industry | LinkedIn industry categories | Technology, Financial Services, Healthcare | High — vertical marketing |
| Job Function | Functional area | Marketing, IT, Finance, Engineering | Very High — reach decision makers |
| Seniority | Career level | Entry, Senior, Manager, Director, VP, C-Suite | Critical — target by authority |
| Company Size | Employee count ranges | 1–10, 11–50, 51–200, 201–500, 501–1000, 1001+ | High — filter by segment |

### LinkedIn Targeting Strategies

| Strategy | Targeting Combination | Use Case |
|----------|----------------------|----------|
| Decision-maker targeting | Job Function: IT + Seniority: Director+ | Enterprise software sales |
| Account-based marketing | Company: [target list] + Seniority: Manager+ | ABM campaigns |
| Industry vertical | Industry: Healthcare + Job Function: Operations | Vertical SaaS marketing |
| SMB vs. Enterprise | Company Size: 1–200 vs. 201+ | Segment-specific messaging |
| Hiring signal | Industry + Company Size + Job Function: HR | Recruiting software |

## Additional Audience Targeting

| Targeting Type | Description | Source |
|---------------|-------------|--------|
| In-market audiences | Users actively researching products/services | Microsoft AI + search signals |
| Custom audiences | Upload CRM lists for matching | First-party data |
| Remarketing | Target past website visitors | UET tag (Universal Event Tracking) |
| Similar audiences (lookalike) | Find users similar to converters | Microsoft AI |
| Dynamic remarketing | Show products users previously viewed | Product feed + UET |
| Combined audiences | AND/OR logic across audience types | Custom combination |

## Campaign Optimization

### Performance Benchmarks (MSAN-Specific)

| Metric | Below Average | Average | Above Average | Excellent |
|--------|--------------|---------|---------------|-----------|
| CTR | <0.08% | 0.08–0.15% | 0.15–0.30% | >0.30% |
| CPC | >$2.00 | $0.80–$2.00 | $0.40–$0.80 | <$0.40 |
| Conversion rate | <1% | 1–3% | 3–5% | >5% |
| Viewability | <50% | 50–65% | 65–80% | >80% |

### Optimization Checklist

| Week | Action | Focus |
|------|--------|-------|
| Week 1 | Launch with broad targeting, multiple creatives | Volume and data collection |
| Week 2 | Review placement report, block underperformers | Placement quality |
| Week 3 | Analyze audience performance, narrow targeting | Audience refinement |
| Week 4 | A/B test creatives, adjust bids | Creative and bid optimization |
| Monthly | Refresh creatives, expand successful audiences | Scale and sustain |

### Creative Optimization Tips

| Element | Best Practice | Impact |
|---------|--------------|--------|
| Headlines | Test benefit-driven vs. curiosity-driven | +10–25% CTR |
| Images | People > objects > abstract; authentic > stock | +20–40% CTR |
| Descriptions | Include CTA and value proposition | +5–15% CTR |
| Asset count | Provide max assets (15 headlines, 16 images) | Algorithm can optimize more effectively |
| Landing page | Must match ad message; <3s load time | +10–20% conversion |

## MSAN vs. Other Native Platforms

| Factor | MSAN | Outbrain | Taboola |
|--------|------|---------|---------|
| Unique advantage | LinkedIn data targeting | Premium publisher network | Largest content network |
| B2B targeting | Excellent (LinkedIn) | Limited | Limited |
| Inventory | MSN, Outlook, Edge, partners | 7,000+ publishers | 9,000+ publishers |
| Minimum budget | No minimum | $10/day typical | $10/day typical |
| Integration | Part of Microsoft Ads platform | Separate platform | Separate platform |
| Best for | B2B, professional services | Content marketing | Content marketing |

## Best Practices

- **Leverage LinkedIn targeting for B2B** — this is MSAN's unique competitive advantage; no other native platform offers it
- **Provide maximum creative assets** — responsive ads perform best with 10+ headlines and 5+ images
- **Separate MSAN campaigns from search** — don't mix audience and search in one campaign; they need different optimization
- **Use UET for conversion tracking** — install before launching; you need data for bid optimization
- **Test LinkedIn audiences against behavioral** — sometimes in-market audiences outperform LinkedIn targeting
- **Monitor placement quality** — review which sites/apps show your ads and block irrelevant placements

## Using the Reference Files

**`/references/01-audience-network-fundamentals.md`** — Read when setting up a new MSAN campaign. Covers platform overview, campaign creation, ad format details, and placement options.

**`/references/02-targeting-options-strategies.md`** — Read when configuring audience targeting. Covers LinkedIn profile targeting, in-market audiences, remarketing, and audience combination strategies.

**`/references/03-campaign-optimization-best-practices.md`** — Read when optimizing running campaigns. Covers bid strategies, budget management, placement analysis, and performance troubleshooting.

**`/references/04-native-advertising-creative-strategy.md`** — Read when creating or testing ad creatives. Covers responsive ad best practices, image selection, headline writing, and A/B testing methodology.
