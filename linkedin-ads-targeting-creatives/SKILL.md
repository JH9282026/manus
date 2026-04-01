---
name: linkedin-ads-targeting-creatives
description: Build and optimize LinkedIn advertising campaigns with B2B targeting strategies and creative best practices using Campaign Manager and the LinkedIn Marketing API. Use for LinkedIn Sponsored Content, Message Ads, Dynamic Ads, Thought Leader Ads, B2B audience targeting by job title, company, seniority, and industry, LinkedIn ad creative design, Lead Gen Forms, Account-Based Marketing on LinkedIn, and LinkedIn Conversions API integration.
---

# LinkedIn Ads Targeting & Creatives

Design high-performing LinkedIn ad campaigns with precise B2B targeting and optimized creative formats.

## Overview

LinkedIn is the primary platform for B2B advertising, offering unmatched professional targeting by job title, company, seniority, industry, and skills. This skill covers campaign structure, targeting strategy, ad format selection, creative best practices, Lead Gen Forms, and performance optimization through Campaign Manager and the LinkedIn Marketing API.

## Ad Format Selection Guide

| Format | Placement | Best For | Avg CTR | Creative Specs |
|--------|-----------|----------|---------|----------------|
| Single Image Ad | Feed | Brand awareness, thought leadership | 0.4-0.6% | 1200×628px; <150 char intro |
| Video Ad | Feed | Product demos, testimonials | 0.3-0.5% | MP4; 7-15s optimal; <200MB |
| Carousel Ad | Feed | Multi-feature showcase, storytelling | 0.4-0.6% | 2-10 cards; 1080×1080px each |
| Document Ad | Feed | Gated content, whitepapers | 0.5-0.8% | PDF/PPT; up to 10 pages |
| Thought Leader Ad | Feed | Employee advocacy, authenticity | 0.8-1.5% | Boost employee's organic post |
| Message Ad | Messaging | Direct outreach, event invites | 30-50% open rate | <500 char body; 1 CTA |
| Conversation Ad | Messaging | Multi-path nurture flows | 35-55% open rate | Decision tree; 2-5 CTAs |
| Lead Gen Form Ad | Feed/Messaging | Lead capture without landing page | 10-15% form fill | Up to 12 fields; pre-filled |
| Dynamic Ad | Right rail | Personalized follower/content ads | 0.02-0.05% | Auto-generated from profile |
| Event Ad | Feed | Event promotion and RSVPs | 0.3-0.5% | Linked to LinkedIn Event |

## B2B Targeting Strategy

### Primary Targeting Facets

| Facet | Examples | Best For |
|-------|----------|----------|
| Job Title | VP Marketing, CTO, Procurement Director | Reaching specific decision-makers |
| Job Function | Marketing, Engineering, Finance | Broad departmental targeting |
| Seniority | C-Suite, VP, Director, Manager | Filtering by authority level |
| Company Name | Target account lists (ABM) | Account-based marketing |
| Company Size | 1-10, 11-50, 51-200, 201-500, 500+ | SMB vs enterprise segmentation |
| Industry | Technology, Financial Services, Healthcare | Vertical-specific campaigns |
| Skills | Python, Salesforce, Project Management | Reaching practitioners |
| Member Groups | Industry-specific LinkedIn Groups | Interest-based targeting |

### Targeting Rules of Thumb

1. **Start with 50,000-500,000 audience size** — too small limits delivery; too large wastes spend
2. **Layer max 2-3 targeting facets** — over-layering shrinks audience and raises CPM
3. **Use Matched Audiences for ABM** — upload company lists for account-based targeting
4. **Exclude current customers** — upload customer list as exclusion audience
5. **Use Qualified Lead Optimization** — sync CRM data via Conversions API for lead quality signals

## Campaign Budget and Bidding

| Objective | Recommended Bid Strategy | Min Daily Budget | Expected CPC |
|-----------|-------------------------|-----------------|-------------|
| Brand Awareness | Maximum Delivery | $10/day | N/A (CPM: $8-15) |
| Website Visits | Max Delivery or Manual CPC | $10/day | $3-8 |
| Engagement | Maximum Delivery | $10/day | $1-3 per engagement |
| Lead Generation | Max Delivery or Cost Cap | $10/day | $15-60 per lead |
| Conversions | Target Cost or Max Delivery | $10/day | $30-100 per conversion |

## Creative Best Practices

1. **Lead with a clear value proposition** — state the benefit in the first line of ad copy
2. **Use Thought Leader Ads** — boost employee posts for 2-3× higher engagement vs brand posts
3. **Test short-form video (7-15s)** — designed natively for LinkedIn, not repurposed from other platforms
4. **Personalize ad copy** — include industry or role-specific language; personalized ads reduce CPL 20-33%
5. **Strong CTA alignment** — match CTA to funnel stage (Learn More → top; Request Demo → bottom)
6. **Rotate creatives every 4-6 weeks** — personalized ads fatigue faster (~30 days)
7. **Use Document Ads for gated content** — higher engagement than external landing page links
8. **Keep intro text under 150 characters** — truncation kills CTR on mobile

## Lead Gen Forms Configuration

| Field Type | Examples | Notes |
|-----------|----------|-------|
| Pre-filled (recommended) | Name, email, job title, company | Auto-populated from profile; high accuracy |
| Custom questions | Budget range, timeline, use case | Up to 3 custom questions; keep minimal |
| Hidden fields | UTM source, campaign ID | Dynamic URL tracking parameters supported |
| Consent checkbox | Privacy policy, marketing opt-in | Required for GDPR compliance |

## LinkedIn Marketing API Quick Reference

| Endpoint | Method | Purpose |
|----------|--------|--------|
| `/adAccounts` | GET | List ad accounts |
| `/adCampaignGroups` | POST | Create campaign group |
| `/adCampaigns` | POST | Create campaign with targeting |
| `/adCreatives` | POST | Upload creative assets |
| `/adAnalytics` | GET | Pull performance metrics |
| `/conversions` | POST | Send conversion events via CAPI |

## Using the Reference Files

### When to Read Each Reference

**`/references/audience-targeting-strategies.md`** — Read when building audience segments, configuring Matched Audiences for ABM, or setting up Qualified Lead Optimization.

**`/references/creative-best-practices.md`** — Read when designing ad creative, writing copy, selecting imagery, or planning A/B tests across formats.

**`/references/ad-format-specifications.md`** — Read when checking exact pixel dimensions, file size limits, character counts, or format requirements for any LinkedIn ad type.

**`/references/campaign-manager-optimization.md`** — Read when optimizing bids, adjusting budgets, analyzing delivery pacing, or troubleshooting underperforming campaigns.

**`/references/performance-measurement-analytics.md`** — Read when pulling analytics via the API, building dashboards, measuring conversion attribution, or evaluating campaign ROI.
