---
name: apple-search-ads-campaign-management
description: "Manage Apple Search Ads campaigns for iOS app promotion on the App Store. Use for creating search results ads, Today tab ads, Search tab ads, and product page ads; setting up campaign structures with brand, category, competitor, and discovery campaigns; configuring targeting by demographics, location, device type, and customer type; implementing CPT and CPA bidding strategies; optimizing keywords with exact match, broad match, and Search Match; managing custom product pages; and analyzing campaign performance for app install acquisition."
---

# Apple Search Ads Campaign Management

Manage comprehensive Apple Search Ads campaigns to promote iOS apps across App Store placements with advanced targeting and bidding strategies.

## Overview

Apple Search Ads enables app developers and marketers to promote iOS apps directly within the App Store through multiple ad placements. This skill covers campaign structure, all ad formats and placements, targeting options, bidding strategies, keyword management, custom product pages, and performance optimization for both Apple Search Ads Basic and Advanced.

## Ad Placements and Formats

| Placement | Description | Best For | Device Support |
|-----------|-------------|----------|----------------|
| **Search Results** | Ads at top of search queries (expanding to multiple positions in 2026) | High-intent users actively searching | iPhone, iPad |
| **Today Tab** | Prominent ads on App Store front page | Brand awareness, first impressions, reaching 800M+ weekly users | iPhone (iOS 17.1+) |
| **Search Tab** | Ads in "Suggested" section before user searches | Early discovery, capturing search intent | iPhone, iPad |
| **Product Pages** | Ads in "You might also like" on competitor app pages | Competitive conquest, engaged users evaluating alternatives | iPhone, iPad |

### Search Results Ads
- Blue background with ad disclosure icon
- Use default App Store product page or custom product page
- Multiple ad positions available (2026 expansion)
- Placement determined by relevance + bid amount (not selectable)
- Support CPT and CPA bidding

### Today Tab Ads
- Display app icon, name, and subtitle
- Background animates with custom product page assets
- **Always require custom product page** as tap destination
- Available on iPhone iOS 17.1+ only (not iPad)
- Ideal for seasonal promotions, new content launches, special events
- Support deep links on iOS 18+

### Search Tab Ads
- Appear before users type search queries
- High impression potential (most users use search)
- Can utilize custom product pages
- Capture users at beginning of discovery journey

### Product Page Ads
- Shown on similar/competitor app listing pages
- Target users actively evaluating alternatives
- High engagement from users already in consideration phase

## Campaign Structure Framework

Organize campaigns into four strategic types for optimal performance and bid management:

### 1. Brand Campaigns
**Target:** Keywords related to app name, brand, or publisher
**Purpose:** Protect brand searches, prevent competitor conquest
**Performance:** High conversion rates, lower CPIs
**Match Type:** Exact match (primary), broad match (secondary)
**Bidding:** Aggressive bids to maintain top position

### 2. Category Campaigns (Generic)
**Target:** Non-branded keywords related to app features/category
**Purpose:** Reach broader audience interested in app category
**Performance:** Moderate conversion rates, wider reach
**Match Type:** Exact match for proven keywords, broad match for discovery
**Bidding:** Moderate bids, adjust based on keyword performance
**Structure:** Organize ad groups by keyword theme

### 3. Competitor Campaigns
**Target:** Keywords associated with rival apps
**Purpose:** Attract users exploring alternatives
**Performance:** Higher CPI but potentially higher LTV users
**Match Type:** Exact match for specific competitor names
**Bidding:** Competitive bids, monitor ROI closely
**Note:** Relevance is critical—ads won't show if app isn't relevant

### 4. Discovery Campaigns
**Target:** Broad match keywords + Search Match
**Purpose:** Identify new relevant keywords, expand reach
**Performance:** Variable, used for keyword research
**Match Type:** Broad match, Search Match
**Bidding:** Moderate bids, monitor for irrelevant traffic
**Optimization:** Move high-performing keywords to specific campaigns

## Targeting Options

### Demographics
- **Age:** Target specific age ranges
- **Gender:** Male, female, or all

### Location
- **Geographic:** Countries, regions, cities, zip codes
- **Use Cases:** Market-specific launches, seasonal promotions, regional campaigns

### Device Type
- **iPhone:** Target iPhone users specifically
- **iPad:** Target iPad users specifically
- **Strategy:** Separate campaigns if app performance differs by device

### Customer Type
| Customer Type | Description | Use Case |
|---------------|-------------|----------|
| **All Users** | Everyone on App Store | General acquisition |
| **New Users** | Never downloaded the app | New user acquisition |
| **Returning Users** | Previously had app (deleted, on other device, or currently have) | Re-engagement, cross-device |
| **Users of Other Apps** | Users who have advertiser's other apps | Cross-promotion |

## Keyword Match Types

### Exact Match
- Shows ads for precise keyword matches or close variations
- **Pros:** High control, high relevance, best conversion rates
- **Cons:** Limited reach
- **Bidding:** Aggressive bids (core performance drivers)
- **Best For:** Brand keywords, proven high-performers
- **Structure:** Separate ad groups from broad match

### Broad Match
- Ads appear for related phrases, synonyms, variations
- **Pros:** Wider reach, keyword discovery
- **Cons:** Less control, potential irrelevant traffic
- **Bidding:** Moderate bids
- **Best For:** Category keywords, discovery
- **Structure:** Separate ad groups from exact match

### Search Match
- Automatically matches ads to relevant searches based on app metadata, category, similar apps
- **Pros:** Excellent for discovering new keywords, minimal setup
- **Cons:** Requires monitoring for irrelevant traffic
- **Bidding:** Moderate bids
- **Best For:** New campaigns, keyword research
- **Optimization:** Review search terms report, add negatives, promote winners to exact match

## Negative Keywords

**Purpose:** Exclude irrelevant search terms to control costs and improve efficiency

**Levels:**
- **Campaign-level:** Apply to all ad groups in campaign
- **Ad group-level:** Apply to specific ad groups

**Strategy:**
1. Review search terms report regularly
2. Identify terms with high spend, low conversions
3. Add as negative keywords (exact or broad match)
4. Prevent ads from showing for unlikely-to-convert searches

## Bidding Strategies

### Apple Search Ads Basic
- **Model:** Cost-Per-Install (CPI)
- **Budget Cap:** $10,000/month per app
- **Automation:** Automatic keyword selection, bid optimization, creative generation
- **Best For:** Beginners, limited resources, simple campaigns

### Apple Search Ads Advanced - Manual Bidding

#### Cost-Per-Tap (CPT)
- Set maximum amount willing to pay per tap
- Often pay less than max CPT due to auction dynamics
- **Starting Point:** Use Apple's suggested bid based on app characteristics and market data

#### Cost-Per-Acquisition (CPA) Goal
- Available for search result placements
- Set target CPA (maximum acceptable cost per conversion)
- **Formula:** CPA Cap × Tap-Through Conversion Rate = Bid Ceiling
- System optimizes CPT bids to meet CPA target

### Bidding Best Practices

**Initial Setup:**
1. Start with strong max CPT bid using Apple's suggestions
2. Use bid recommendations from "Recommendations" page
3. Set aggressive bids for exact match keywords
4. Set moderate bids for broad match and Search Match
5. Separate ad groups/campaigns for different match types

**Raise Bids When:**
- Discovery campaigns identify high-performing terms
- Keywords deliver conversions below target acquisition cost
- Popular keywords show low impressions (likely outbid)
- Seasonal opportunities arise

**Lower/Reevaluate Bids When:**
- Keywords show low conversions at high acquisition cost
- High taps but poor conversion efficiency
- Budget constraints require reallocation

**Advanced Strategies:**
- **LTV-Based Bidding:** Align bids with expected user lifetime value
  - Calculate keyword-level ROAS
  - Set max CPT = (LTV × Conversion Rate) / Target ROAS
- **Predictive Bid Adjustment:** Use historical data for seasonal trends
- **Device Segmentation:** Adjust bids based on iPhone vs iPad performance
- **iOS Version Targeting:** Optimize for specific iOS versions

### Maximize Conversions (API 5.5 - February 2026)
- **Automated bid strategy** optimizing for highest conversion volume at target CPA
- Uses automated ad group with Search Match
- Automatically discovers and bids on relevant keywords
- Best for campaigns with sufficient conversion data

## Budget Management

### Daily Budget
- Set daily budget for average monthly spending control
- System optimizes spending on high-opportunity days
- **Monthly spend ≤ Daily Budget × 30.4 days**
- Campaigns auto-extend monthly unless paused/ended

### Total Budget
- Set lifetime budget for campaign
- Campaign ends when budget exhausted
- Useful for time-limited promotions

### Optimization
- Monitor budget availability regularly
- Reallocate budget to high-performing campaigns
- Adjust daily budgets based on performance trends
- Increase budgets during seasonal peaks

## Custom Product Pages

### Overview
- Create up to 35 custom product pages in App Store Connect
- Tailor screenshots, app previews, promotional text to specific audiences
- **Required for Today Tab ads**
- Optional for other placements

### Components (Customizable)
- **Screenshots:** Up to 10 unique screenshots
- **App Previews:** Up to 3 videos
- **Promotional Text:** Up to 170 characters, localized
- **Deep Links:** iOS 18+ support for specific in-app destinations

### Components (Consistent Across All Pages)
- App name, icon, subtitle
- Rating, reviews
- In-app purchase information
- Privacy details

### Benefits
- **Average 2.5% increase in conversion rates** (156% improvement vs default pages)
- Increased relevance for specific campaigns
- Seasonal/event-specific messaging
- Feature-specific highlighting
- Audience segmentation

### Best Practices
1. Align visuals and messaging with campaign theme
2. Highlight specific features relevant to target audience
3. Use simple, engaging content with clear CTA
4. Localize in default language of target region
5. Comply with Apple Advertising Policies
6. Monitor performance in App Analytics (App Store Connect)
7. Test different variations for optimization

### Today Tab Specific Requirements
- Must include iPhone assets
- Localized in campaign region's default language
- Background animates using custom product page assets
- Color derived from app icon
- No violent, offensive, sexually explicit, or inappropriate content
- No pricing, offers, or ranking claims

## Performance Optimization

### Key Metrics
- **Impressions:** Ad visibility count
- **Taps:** Number of ad clicks
- **TTR (Tap-Through Rate):** Taps ÷ Impressions
- **Installs:** App downloads from ads
- **Conversion Rate:** Installs ÷ Taps
- **CPT (Cost Per Tap):** Total Spend ÷ Taps
- **CPA (Cost Per Acquisition):** Total Spend ÷ Installs
- **ROAS (Return on Ad Spend):** Revenue ÷ Ad Spend

### View-Through Metrics (API 5.0+)
- **View-Through Installs:** Installs after seeing ad (without tapping)
- **View-Through New Downloads**
- **View-Through Redownloads**
- Useful for measuring brand awareness impact

### Preorder Metrics (API 5.4+)
- **Tap Preorders Placed**
- **View Preorders Placed**
- **Total Preorders Placed**
- Track preorder performance for upcoming app releases

### Optimization Workflow
1. **Monitor Performance:** Review metrics daily/weekly
2. **Identify Winners:** Find high-performing keywords, ad groups, campaigns
3. **Scale Winners:** Increase bids and budgets for top performers
4. **Identify Losers:** Find underperforming elements
5. **Optimize or Pause:** Adjust bids, add negatives, or pause poor performers
6. **Test Creatives:** A/B test custom product pages
7. **Keyword Mining:** Review search terms, add new keywords, add negatives
8. **Seasonal Adjustments:** Adapt to trends, events, seasonality

### A/B Testing
- Test different custom product pages
- Test different keyword themes
- Test different ad copy (promotional text)
- Test different targeting combinations
- Run tests with sufficient data (statistical significance)

## App Store Optimization (ASO) Synergy

Apple Search Ads performance is heavily influenced by ASO:

**Relevance Factor:**
- Ads won't show if app isn't relevant to search query
- High bid doesn't override low relevance
- Strong ASO improves ad eligibility

**Metadata Optimization:**
- App title, subtitle, keyword field affect Search Match
- Category selection influences automatic matching
- Description quality impacts user decision after tap

**Visual Assets:**
- Icon, screenshots, previews affect post-tap conversion
- Ratings and reviews influence install decision
- Optimize for both organic and paid traffic

**Strategy:**
1. Optimize ASO before launching ads
2. Use Search Ads data to inform ASO keyword strategy
3. Align paid and organic keyword targeting
4. Improve conversion elements (icon, screenshots) for both channels

## Compliance and Policies

### Apple Advertising Policies
- No violent, offensive, sexually explicit content
- No misleading claims or false information
- No pricing or ranking claims in Today Tab ads
- Respect user privacy and data protection
- Follow App Store Review Guidelines

### Ad Approval Process
- Ads reviewed by Apple before serving
- Today Tab ads require additional approval
- Custom product pages must be approved in App Store Connect first
- Monitor ad status in Ads dashboard

### Brand Safety
- Use negative keywords to avoid inappropriate placements
- Monitor search terms report for brand safety issues
- Exclude specific questions or topics if needed

## Using the Reference Files

### When to Read Each Reference

**`/references/campaign-setup-checklist.md`** — Read when setting up new Apple Search Ads campaigns from scratch, need step-by-step setup guidance, or want to ensure all configuration elements are properly addressed.

**`/references/keyword-research-strategy.md`** — Read when conducting keyword research for new campaigns, optimizing existing keyword lists, mining search terms reports, or building comprehensive keyword strategies across campaign types.

**`/references/custom-product-pages-guide.md`** — Read when creating custom product pages for campaigns, setting up Today Tab ads, optimizing creative assets for different audiences, or implementing deep linking strategies.

**`/references/performance-benchmarks.md`** — Read when evaluating campaign performance, setting KPI targets, comparing results against industry standards, or justifying budget allocation decisions.

**`/references/troubleshooting-guide.md`** — Read when campaigns have low impressions, high CPA, poor conversion rates, ad approval issues, or other performance problems requiring diagnosis and resolution.