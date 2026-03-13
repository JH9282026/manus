# Apple Search Ads Campaign Setup Checklist

Comprehensive step-by-step checklist for setting up Apple Search Ads campaigns from initial account setup through launch and optimization.

---

## Pre-Launch Preparation

### Account Setup
- [ ] Create Apple Ads account at ads.apple.com
- [ ] Link to App Store Connect account
- [ ] Verify app is published on App Store
- [ ] Set up payment method
- [ ] Configure user roles and permissions (if team)
- [ ] Review and accept Apple Advertising Policies

### App Store Optimization (ASO) Foundation
- [ ] Optimize app title with primary keywords
- [ ] Write compelling subtitle (30 characters)
- [ ] Fill keyword field (100 characters) strategically
- [ ] Select accurate primary and secondary categories
- [ ] Create high-quality app icon
- [ ] Design compelling screenshots (all required sizes)
- [ ] Create app preview videos (recommended)
- [ ] Write clear, benefit-focused description
- [ ] Encourage positive ratings and reviews
- [ ] Localize for target markets

### Custom Product Pages (If Using)
- [ ] Create custom product pages in App Store Connect
- [ ] Design unique screenshots for each variation
- [ ] Create app preview videos for variations
- [ ] Write promotional text (170 characters)
- [ ] Set up deep links (iOS 18+) if needed
- [ ] Submit for approval
- [ ] Wait for approval before creating Today Tab ads
- [ ] Test deep links functionality

### Keyword Research
- [ ] Identify brand keywords (app name, publisher, variations)
- [ ] Research category keywords (features, use cases, benefits)
- [ ] Compile competitor keywords (rival app names)
- [ ] Use App Store search suggestions for ideas
- [ ] Analyze competitor app metadata
- [ ] Review App Store Connect Search Ads suggestions
- [ ] Organize keywords by theme/intent
- [ ] Identify negative keywords to exclude

### Budget Planning
- [ ] Define overall monthly budget
- [ ] Allocate budget across campaign types:
  - Brand: 30-40% (protect brand searches)
  - Category: 40-50% (growth and scale)
  - Competitor: 10-20% (conquest)
  - Discovery: 10-20% (research)
- [ ] Set daily budgets for each campaign
- [ ] Plan for seasonal adjustments
- [ ] Define target CPA/CPI goals
- [ ] Calculate acceptable ROAS thresholds

---

## Campaign Creation

### Campaign Level Settings

#### Brand Campaign
- [ ] **Campaign Name:** "Brand - [App Name] - [Region]" (use consistent naming convention)
- [ ] **Ad Placements:** Select placements (Search Results recommended for brand)
- [ ] **Locations:** Select target countries/regions
- [ ] **Daily Budget:** Set based on budget allocation plan
- [ ] **Campaign Status:** Set to active or paused (activate after full setup)

#### Category Campaign
- [ ] **Campaign Name:** "Category - [Theme] - [Region]"
- [ ] **Ad Placements:** Select placements (Search Results, Search Tab, Product Pages)
- [ ] **Locations:** Select target countries/regions
- [ ] **Daily Budget:** Set based on budget allocation plan
- [ ] **Campaign Status:** Set to active or paused

#### Competitor Campaign
- [ ] **Campaign Name:** "Competitor - [Competitor Name] - [Region]"
- [ ] **Ad Placements:** Select placements (Search Results, Product Pages recommended)
- [ ] **Locations:** Select target countries/regions
- [ ] **Daily Budget:** Set based on budget allocation plan
- [ ] **Campaign Status:** Set to active or paused

#### Discovery Campaign
- [ ] **Campaign Name:** "Discovery - Broad - [Region]"
- [ ] **Ad Placements:** Select placements (all recommended)
- [ ] **Locations:** Select target countries/regions
- [ ] **Daily Budget:** Set based on budget allocation plan
- [ ] **Campaign Status:** Set to active or paused

#### Today Tab Campaign (If Using)
- [ ] **Campaign Name:** "Today Tab - [Theme] - [Region]"
- [ ] **Ad Placements:** Today Tab only
- [ ] **Locations:** Select target countries/regions (iPhone only)
- [ ] **Daily Budget:** Set based on budget allocation plan
- [ ] **Custom Product Page:** Select approved custom product page
- [ ] **Campaign Status:** Set to paused (activate after ad approval)

### Ad Group Level Settings

#### For Each Campaign, Create Ad Groups:

**Brand Campaign - Exact Match Ad Group**
- [ ] **Ad Group Name:** "Brand - Exact Match"
- [ ] **CPA Goal:** Set target CPA (optional)
- [ ] **Max CPT Bid:** Set aggressive bid (use Apple's suggestion + 20-50%)
- [ ] **Devices:** All (or separate iPhone/iPad if needed)
- [ ] **Demographics:** All (or refine if data supports)
- [ ] **Customer Type:** All Users (or New Users for acquisition focus)
- [ ] **Keywords:** Add brand keywords with Exact Match
- [ ] **Negative Keywords:** Add competitor names, irrelevant terms

**Brand Campaign - Broad Match Ad Group**
- [ ] **Ad Group Name:** "Brand - Broad Match"
- [ ] **CPA Goal:** Set target CPA (optional)
- [ ] **Max CPT Bid:** Set moderate bid (use Apple's suggestion)
- [ ] **Devices:** All
- [ ] **Demographics:** All
- [ ] **Customer Type:** All Users
- [ ] **Keywords:** Add brand keywords with Broad Match
- [ ] **Negative Keywords:** Add irrelevant terms

**Category Campaign - Ad Groups by Theme**
- [ ] **Ad Group Name:** "Category - [Theme] - Exact Match"
- [ ] **CPA Goal:** Set target CPA
- [ ] **Max CPT Bid:** Set moderate-aggressive bid
- [ ] **Devices:** All (or segment if performance differs)
- [ ] **Demographics:** Refine if target audience is specific
- [ ] **Customer Type:** New Users (for acquisition)
- [ ] **Keywords:** Add category keywords with Exact Match
- [ ] **Negative Keywords:** Add irrelevant terms, competitor names
- [ ] Repeat for each keyword theme (e.g., features, use cases, benefits)

**Category Campaign - Broad Match Ad Group**
- [ ] **Ad Group Name:** "Category - Broad Match"
- [ ] **CPA Goal:** Set target CPA
- [ ] **Max CPT Bid:** Set moderate bid
- [ ] **Devices:** All
- [ ] **Demographics:** All or refined
- [ ] **Customer Type:** New Users
- [ ] **Keywords:** Add category keywords with Broad Match
- [ ] **Negative Keywords:** Add irrelevant terms

**Competitor Campaign - Ad Groups by Competitor**
- [ ] **Ad Group Name:** "Competitor - [Competitor Name] - Exact Match"
- [ ] **CPA Goal:** Set target CPA (may be higher than brand/category)
- [ ] **Max CPT Bid:** Set competitive bid (monitor closely)
- [ ] **Devices:** All
- [ ] **Demographics:** All or refined
- [ ] **Customer Type:** New Users
- [ ] **Keywords:** Add competitor app names with Exact Match
- [ ] **Negative Keywords:** Add own brand name, irrelevant terms
- [ ] Repeat for each major competitor

**Discovery Campaign - Search Match Ad Group**
- [ ] **Ad Group Name:** "Discovery - Search Match"
- [ ] **CPA Goal:** Set target CPA
- [ ] **Max CPT Bid:** Set moderate bid
- [ ] **Devices:** All
- [ ] **Demographics:** All
- [ ] **Customer Type:** New Users
- [ ] **Search Match:** Enable (no keywords needed)
- [ ] **Negative Keywords:** Add known irrelevant terms, competitor names (if not targeting)

**Discovery Campaign - Broad Match Ad Group**
- [ ] **Ad Group Name:** "Discovery - Broad Match"
- [ ] **CPA Goal:** Set target CPA
- [ ] **Max CPT Bid:** Set moderate bid
- [ ] **Devices:** All
- [ ] **Demographics:** All
- [ ] **Customer Type:** New Users
- [ ] **Keywords:** Add broad category keywords with Broad Match
- [ ] **Negative Keywords:** Add irrelevant terms

### Creative Assets

**Default Product Page Ads**
- [ ] Verify default product page is optimized
- [ ] Ensure icon, screenshots, previews are high quality
- [ ] Check that metadata is compelling
- [ ] No additional setup needed (auto-created)

**Custom Product Page Ads**
- [ ] Select approved custom product page for ad group
- [ ] Verify custom product page is localized for target region
- [ ] Test deep link functionality (if using)
- [ ] Ensure compliance with Apple Advertising Policies

**Today Tab Ads**
- [ ] Create ad in Today Tab campaign
- [ ] Select approved custom product page (required)
- [ ] Verify background assets animate correctly
- [ ] Submit ad for Apple approval
- [ ] Wait for approval before activating campaign
- [ ] Monitor ad status in Ads dashboard

---

## Pre-Launch Review

### Campaign Structure Verification
- [ ] All campaigns created (Brand, Category, Competitor, Discovery)
- [ ] Naming convention consistent across campaigns
- [ ] Ad groups organized logically within campaigns
- [ ] Match types separated (Exact vs Broad)
- [ ] Budgets allocated appropriately

### Targeting Verification
- [ ] Locations set correctly for all campaigns
- [ ] Device targeting appropriate (iPhone/iPad)
- [ ] Demographics refined where needed
- [ ] Customer type aligned with goals

### Keyword Verification
- [ ] Brand keywords in Brand campaign
- [ ] Category keywords in Category campaign
- [ ] Competitor keywords in Competitor campaign
- [ ] Search Match enabled in Discovery campaign
- [ ] Match types appropriate for each ad group
- [ ] Negative keywords added at campaign and ad group levels
- [ ] No keyword conflicts between campaigns

### Bidding Verification
- [ ] Max CPT bids set for all ad groups
- [ ] Bids aligned with strategy (aggressive for brand, moderate for category)
- [ ] CPA goals set where appropriate
- [ ] Bids within budget constraints

### Creative Verification
- [ ] Default product page optimized
- [ ] Custom product pages approved (if using)
- [ ] Today Tab ads submitted for approval (if using)
- [ ] All assets comply with Apple Advertising Policies

---

## Launch

### Activation
- [ ] Activate Brand campaign first (protect brand searches)
- [ ] Activate Category campaign
- [ ] Activate Discovery campaign
- [ ] Activate Competitor campaign (monitor closely)
- [ ] Activate Today Tab campaign (after ad approval)
- [ ] Verify all campaigns are serving (check status)

### Initial Monitoring (First 24-48 Hours)
- [ ] Check impression delivery for all campaigns
- [ ] Verify ads are showing for target keywords
- [ ] Monitor initial tap-through rates
- [ ] Check for any ad disapprovals or issues
- [ ] Review search terms report for irrelevant traffic
- [ ] Add negative keywords as needed
- [ ] Verify budget pacing is appropriate

---

## Ongoing Optimization (Weekly)

### Performance Review
- [ ] Review key metrics (impressions, taps, installs, CPT, CPA, TTR, conversion rate)
- [ ] Compare performance across campaigns
- [ ] Identify top-performing keywords
- [ ] Identify underperforming keywords
- [ ] Review search terms report

### Keyword Optimization
- [ ] Add high-performing search terms as exact match keywords
- [ ] Add irrelevant search terms as negative keywords
- [ ] Pause keywords with high spend, low conversions
- [ ] Increase bids on high-performing keywords
- [ ] Decrease bids on underperforming keywords
- [ ] Test new keyword variations

### Bid Optimization
- [ ] Adjust bids based on performance data
- [ ] Increase bids for keywords below target CPA
- [ ] Decrease bids for keywords above target CPA
- [ ] Monitor impression share (raise bids if low)
- [ ] Review bid recommendations from Apple

### Budget Optimization
- [ ] Reallocate budget to high-performing campaigns
- [ ] Increase budgets for campaigns hitting daily caps
- [ ] Decrease budgets for underperforming campaigns
- [ ] Adjust for seasonal trends

### Creative Optimization
- [ ] Test new custom product page variations
- [ ] Update promotional text for seasonal events
- [ ] Refresh screenshots to highlight new features
- [ ] Monitor custom product page performance in App Analytics

### Negative Keyword Management
- [ ] Review search terms report for new irrelevant terms
- [ ] Add negative keywords at campaign and ad group levels
- [ ] Use broad match negatives for broad exclusions
- [ ] Use exact match negatives for specific exclusions

---

## Monthly Review

### Strategic Analysis
- [ ] Review overall campaign performance vs goals
- [ ] Calculate ROAS and LTV metrics
- [ ] Analyze performance by campaign type
- [ ] Identify trends and patterns
- [ ] Assess budget allocation effectiveness

### Competitive Analysis
- [ ] Review competitor keyword performance
- [ ] Identify new competitors to target
- [ ] Adjust competitor campaign strategy
- [ ] Monitor competitor ad activity

### Expansion Opportunities
- [ ] Identify new keyword themes from search terms
- [ ] Test new ad placements (if not using all)
- [ ] Expand to new geographic markets
- [ ] Test new custom product page variations
- [ ] Consider new campaign types or structures

### Reporting
- [ ] Generate performance reports for stakeholders
- [ ] Document key learnings and insights
- [ ] Update strategy based on data
- [ ] Set goals for next month

---

## Troubleshooting Common Issues

### Low Impressions
- [ ] Check if bids are competitive (increase if needed)
- [ ] Verify keywords are relevant to app
- [ ] Ensure app has strong ASO (relevance factor)
- [ ] Check if budget is sufficient
- [ ] Verify campaign and ad group are active
- [ ] Review targeting settings (too narrow?)

### High CPA
- [ ] Review keyword relevance (add negatives)
- [ ] Optimize post-tap conversion (improve product page)
- [ ] Lower bids on expensive keywords
- [ ] Focus budget on high-performing keywords
- [ ] Test different custom product pages
- [ ] Refine targeting to more qualified audience

### Low Conversion Rate
- [ ] Optimize app icon and screenshots
- [ ] Improve app ratings and reviews
- [ ] Test custom product pages
- [ ] Ensure keyword-to-app relevance
- [ ] Check if app description is compelling
- [ ] Verify pricing is competitive

### Ad Disapprovals
- [ ] Review Apple Advertising Policies
- [ ] Check for prohibited content in custom product pages
- [ ] Verify compliance with App Store Review Guidelines
- [ ] Contact Apple Ads support for clarification
- [ ] Revise assets and resubmit

---

## Advanced Optimization Techniques

### Dayparting Analysis
- [ ] Analyze performance by hour of day
- [ ] Identify peak conversion times
- [ ] Consider third-party tools for automated dayparting

### Device Performance Segmentation
- [ ] Compare iPhone vs iPad performance
- [ ] Create separate campaigns if performance differs significantly
- [ ] Adjust bids by device type

### Geographic Performance Analysis
- [ ] Review performance by country/region
- [ ] Create separate campaigns for top-performing regions
- [ ] Adjust bids by geographic performance
- [ ] Localize custom product pages for key markets

### Audience Segmentation
- [ ] Analyze performance by customer type
- [ ] Create separate campaigns for new vs returning users
- [ ] Test different messaging for different audiences
- [ ] Adjust bids based on audience value

### Seasonal Campaign Planning
- [ ] Identify seasonal trends in app category
- [ ] Plan campaigns around key events/holidays
- [ ] Create seasonal custom product pages
- [ ] Adjust budgets and bids for seasonal peaks
- [ ] Prepare seasonal keyword lists in advance