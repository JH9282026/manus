#!/usr/bin/env python3
"""
Generate comprehensive reference files for Batch 2 skills
"""

import os
from pathlib import Path

# Batch 2 skills (excluding amazon-dsp-programmatic which is already done)
BATCH2_SKILLS = [
    "amazon-sponsored-brands",
    "amazon-sponsored-products", 
    "angular-framework",
    "brand-strategy",
    "competitive-analysis-&-intelligence",
    "conversion-optimization",
    "el-toro-ip-targeting",
    "email-marketing",
    "explainable-ai",
    "feature-engineering",
    "git-version-control",
    "google-ads-api-automation",
    "google-ads-performance-max",
    "google-ads-shopping-video"
]

# Reference file content templates
REFERENCE_CONTENT = {
    "amazon-sponsored-brands": {
        "campaign-setup-formats.md": """# Amazon Sponsored Brands: Campaign Setup and Ad Formats

## Introduction

Amazon Sponsored Brands is a powerful advertising solution that helps brands increase visibility, drive traffic to Brand Stores or product listings, and build customer loyalty. This guide covers campaign setup, ad formats, and best practices for maximizing Sponsored Brands performance.

## Eligibility Requirements

### Brand Registry Enrollment

**Mandatory Requirement:**
- Must be enrolled in Amazon Brand Registry
- Verifies trademark ownership
- Unlocks advanced advertising features
- Provides brand protection tools

**Eligible Users:**
- Professional sellers with Brand Registry
- Vendors (1P sellers)
- Book vendors
- Kindle Direct Publishing (KDP) authors
- Authorized agencies representing brands

### Product Eligibility

**Eligible Products:**
- Products in active, buyable status
- Products with valid images
- Products meeting Amazon's advertising policies
- Products in approved categories

**Ineligible Products:**
- Adult products
- Used or refurbished products
- Products in closed categories
- Products violating advertising policies

## Campaign Setup Process

### Step 1: Campaign Creation

**Access Campaign Manager:**
1. Log in to Amazon Advertising console
2. Navigate to Campaign Manager
3. Click "Create campaign"
4. Select "Sponsored Brands"

**Campaign Settings:**
- **Campaign Name:** Use descriptive, organized naming convention
  - Example: `SB_BrandAwareness_Q1_2026`
- **Start Date:** Campaign launch date
- **End Date:** Optional (recommended to leave open for always-on campaigns)
- **Daily Budget:** Minimum $1, recommended $50+ for meaningful data

### Step 2: Campaign Goal Selection

Amazon offers three goal-based campaign controls:

#### Drive Page Visits (DPV)

**Objective:** Increase traffic to Brand Stores and product detail pages

**Best For:**
- New product launches
- Brand Store promotion
- Driving consideration
- Building awareness

**Optimization:** Focuses on maximizing clicks

**Metrics to Track:**
- Clicks
- Click-through rate (CTR)
- Detail page views
- Cost per click (CPC)

#### Grow Brand Impression Share (BIS)

**Objective:** Maximize brand visibility and top-of-search presence

**Best For:**
- Brand awareness campaigns
- Competitive defense
- Market share growth
- New market entry

**Optimization:** Focuses on top-of-search impression share

**Metrics to Track:**
- Impressions
- Top-of-search impression share
- Reach
- Brand lift

#### Acquire New Customers

**Objective:** Target shoppers who haven't purchased from your brand in 12 months

**Best For:**
- Customer acquisition
- Market expansion
- New brand growth
- Competitive conquest

**Optimization:** Uses New-to-Brand (NTB) targeting

**Metrics to Track:**
- New-to-brand orders
- New-to-brand sales
- New customer acquisition cost
- NTB percentage

### Step 3: Ad Format Selection

Choose from three primary ad formats based on campaign objectives.

## Ad Format Deep Dive

### 1. Product Collection

**Description:**
Showcase multiple products (minimum 1, maximum 3) alongside your brand logo and custom headline.

**Components:**
- Brand logo (registered trademark)
- Custom headline (up to 50 characters)
- 1-3 product ASINs
- Optional: Lifestyle image or video

**Landing Page Options:**

**Brand Store:**
- Directs to your custom Brand Store homepage
- Encourages brand exploration
- Showcases full product catalog
- Best for brand awareness and consideration

**Simple Landing Page:**
- Auto-generated page with advertised products
- Quick setup, no Brand Store required
- Product-focused experience

**Custom Landing Page:**
- Specific Brand Store sub-page
- Curated product collections
- Themed shopping experiences
- Campaign-specific destinations

**Features:**
- **Automatic Product Optimization:** Amazon can automatically select relevant products based on shopping queries
- **Promotional CTAs:** Display deal badges and promotional messaging
- **Mobile Optimization:** Responsive design for all devices

**Best Practices:**
- Use high-quality product images (minimum 1000x1000 pixels)
- Select complementary products that tell a story
- Write benefit-oriented headlines
- Test different product combinations
- Link to relevant Brand Store pages

**Example Use Cases:**
- "Complete Your Home Office" - desk, chair, lamp
- "Summer Fitness Essentials" - yoga mat, water bottle, resistance bands
- "Gourmet Coffee Experience" - coffee maker, beans, grinder

### 2. Store Spotlight

**Description:**
Showcase up to three Brand Store sub-pages directly within the ad, driving traffic to curated brand experiences.

**Requirements:**
- Must have an active Brand Store
- Brand Store must have at least 3 sub-pages
- Each sub-page must feature a unique product

**Components:**
- Brand logo
- Custom headline (up to 50 characters)
- 3 Brand Store sub-page tiles
- Each tile includes:
  - Custom image
  - Custom label (up to 30 characters)
  - Link to specific sub-page

**AI-Powered Features:**
- Headline suggestions based on brand and products
- Performance predictions
- Optimization recommendations

**Best Practices:**
- Create visually distinct sub-page images
- Use clear, descriptive labels
- Organize sub-pages by category, use case, or customer segment
- Ensure sub-pages are well-designed and up-to-date
- Test different sub-page combinations

**Example Sub-Page Themes:**
- "New Arrivals" - Latest product launches
- "Best Sellers" - Top-performing products
- "Gift Ideas" - Curated gift selections
- "Sale Items" - Promotional products

**Strategic Advantages:**
- Showcases brand breadth
- Encourages deeper exploration
- Builds brand affinity
- Increases time on site

### 3. Sponsored Brands Video

**Description:**
Auto-playing video ads (6-45 seconds) that appear in shopping results, showcasing products in action.

**Video Specifications:**

**Length:**
- Minimum: 6 seconds
- Maximum: 45 seconds
- Optimal: 15-30 seconds for lasting impact

**Aspect Ratios:**
- Vertical: 9:16 (mobile-optimized)
- Horizontal: 16:9 (desktop and tablet)

**File Requirements:**
- Format: MP4 or MOV
- Resolution: Minimum 1280x720 (720p)
- File size: Maximum 500 MB
- Frame rate: 23.976 to 60 fps

**Audio:**
- Auto-plays muted by default
- Must include closed captions
- Design for sound-off viewing

**Content Guidelines:**
- Show product in first 2 seconds
- Demonstrate product function in first 5 seconds
- Include brand logo throughout
- Clear call-to-action
- No third-party logos or trademarks

**Landing Page:**
- Product detail page
- Brand Store

**Creative Best Practices:**

**First 2 Seconds:**
- Show the product clearly
- Grab attention immediately
- Establish brand presence

**First 5 Seconds:**
- Demonstrate key product feature
- Show product in use
- Communicate primary benefit

**Throughout Video:**
- Maintain visual interest
- Show multiple use cases
- Include lifestyle context
- Display brand logo

**Final Frame:**
- Strong call-to-action
- Product image
- Brand logo
- Key benefit or offer

**Video Production Options:**

**Amazon Video Creative Services:**
- Professional video production
- Editing and optimization
- Multiple video variations
- Performance-optimized formats

**Self-Produced:**
- Use existing video assets
- Follow Amazon's creative guidelines
- Optimize for mobile viewing
- Test multiple variations

**Performance Advantages:**
- Higher engagement rates than static ads
- Better storytelling capability
- Demonstrates product functionality
- Builds emotional connection

## Targeting Strategies

### Keyword Targeting

**How It Works:**
Ads appear when shopper search queries match your selected keywords.

**Match Types:**

**Broad Match:**
- Widest reach
- Matches variations, synonyms, related terms
- Keywords can appear in any order
- Example: "running shoes" matches "shoes for running", "athletic footwear"

**Phrase Match:**
- Moderate reach
- Matches search terms containing keyword phrase in order
- Includes plural forms
- Example: "running shoes" matches "best running shoes", "running shoes for women"

**Exact Match:**
- Narrowest reach, highest relevance
- Matches exact keyword or close variants
- Includes plural forms
- Example: "running shoes" matches "running shoes", "running shoe"

**Keyword Research:**
- Use Amazon's suggested keywords
- Analyze search term reports from Sponsored Products
- Include branded keywords (brand defense)
- Include category keywords (awareness)
- Include competitor keywords (conquest)
- Include long-tail keywords (specific intent)

**Keyword Organization:**
- Group related keywords in ad groups
- Separate branded vs. non-branded campaigns
- Create themed ad groups (e.g., "coffee makers", "espresso machines")
- Minimum 25 keywords recommended for optimal reach

**Bid Strategy by Match Type:**
- Exact match: Highest bids (most relevant)
- Phrase match: Medium bids
- Broad match: Lowest bids (testing and discovery)

### Product Targeting

**How It Works:**
Ads appear on specific product detail pages or within product categories.

**Targeting Options:**

**Individual Products (ASINs):**
- Target specific competitor products
- Target complementary products
- Target your own products (cross-sell, upsell)

**Categories:**
- Target entire product categories
- Refine by:
  - Brand (include or exclude)
  - Price range
  - Star rating (e.g., 4+ stars)
  - Prime eligibility

**Strategic Use Cases:**

**Competitive Targeting:**
- Identify top competitor ASINs
- Target their product detail pages
- Offer alternative or superior solution
- Capture consideration-stage shoppers

**Complementary Targeting:**
- Target products that pair with yours
- Example: Sell coffee → Target coffee maker ASINs
- Cross-sell opportunities

**Own-Product Targeting:**
- Target your own product pages
- Upsell to premium versions
- Cross-sell related products
- Defend against competitor ads

### Negative Targeting

**Purpose:**
Prevent ads from appearing for irrelevant keywords or on unsuitable product pages.

**Negative Keywords:**
- Exclude irrelevant search terms
- Improve targeting precision
- Reduce wasted spend
- Increase ROAS

**Negative Products:**
- Exclude specific ASINs or categories
- Avoid appearing on competitor pages (if desired)
- Exclude low-performing placements

**Implementation:**
- Add during campaign setup
- Continuously refine based on search term reports
- Use negative exact and negative phrase match

### Theme Targeting (Beta)

**How It Works:**
Dynamic, model-based targeting that bundles and optimizes keywords using Amazon's machine learning.

**Options:**

**Keywords Related to Your Brand:**
- Promotes brand impressions
- Captures branded search traffic
- Defends brand presence

**Keywords Related to Your Landing Page:**
- Drives traffic to Brand Store or product pages
- Optimizes for relevance
- Continuously updated by Amazon's algorithms

**Advantages:**
- Automated keyword discovery
- Continuous optimization
- Reduced manual management
- Scales with performance data

## Pricing Models

### Cost-Per-Click (CPC)

**How It Works:**
- Pay only when a shopper clicks your ad
- Set maximum bid per click
- Actual cost often lower than max bid (second-price auction)

**Best For:**
- Traffic and sales-focused campaigns
- Performance marketing
- Direct response objectives

**Bidding Strategies:**
- Start with Amazon's suggested bid
- Adjust based on performance (ACOS, ROAS)
- Increase bids for high-performing keywords
- Decrease bids for low-performing keywords

### Cost Per 1,000 Viewable Impressions (vCPM)

**How It Works:**
- Pay for every 1,000 viewable impressions
- Viewable = 50% of ad on screen for 1+ second
- Optimizes for reach and visibility

**Best For:**
- Brand awareness campaigns
- Maximizing reach
- Top-of-funnel objectives
- New product launches

**Bidding Strategies:**
- Set vCPM bid based on awareness goals
- Monitor reach and frequency
- Optimize for cost-efficient impressions

### Reserve Share of Voice

**How It Works:**
- Secure top-of-search placement for branded keywords
- Fixed, upfront pricing
- Minimum spend commitment
- Guaranteed placement

**Best For:**
- Brand protection
- High-value branded keywords
- Competitive defense
- Major product launches

## Budget Management

### Setting Daily Budgets

**Minimum:** $1 per day (not recommended for meaningful results)
**Recommended:** $50-$100+ per day for sufficient data

**Calculation:**
```
Daily Budget = (Monthly Budget / 30) × 1.2
```
(1.2 factor allows for day-to-day flexibility)

### Budget Pacing

**Even Pacing (Default):**
- Spreads budget evenly throughout the day
- Prevents early depletion
- Consistent delivery

**Considerations:**
- Monitor pacing in first week
- Adjust if consistently under or over-pacing
- Increase budget if running out early
- Decrease if underspending

### Portfolio Budgets

**Feature:**
- Share budget across multiple campaigns
- Automatically reallocates to top performers
- Simplifies budget management

**Best Practices:**
- Group related campaigns in portfolios
- Set portfolio-level budget caps
- Monitor individual campaign performance
- Adjust allocation based on goals

## Creative Best Practices

### Logo Guidelines

**Requirements:**
- Use registered trademark logo
- Clear, high-resolution image
- Minimum 400x400 pixels
- Transparent or white background
- No additional text or graphics

### Headline Best Practices

**Character Limit:** 50 characters

**Effective Headlines:**
- Lead with benefits, not features
- Use action words
- Create urgency when appropriate
- Include brand name
- Be specific and clear

**Examples:**
- "Premium Coffee Makers - Free Shipping"
- "Upgrade Your Home Office Today"
- "Eco-Friendly Products for Sustainable Living"
- "Award-Winning Skincare - Shop Now"

**AI-Powered Suggestions:**
- Amazon provides headline recommendations
- Based on product data and performance
- Test multiple variations

### Image Best Practices

**Product Images:**
- High resolution (minimum 1000x1000 pixels)
- Clear product visibility
- Professional photography
- White or neutral background
- Multiple angles if possible

**Lifestyle Images:**
- Show product in use
- Relatable context
- Aspirational but authentic
- Diverse representation
- Emotional connection

### Call-to-Action (CTA)

**Effective CTAs:**
- "Shop Now"
- "Learn More"
- "Discover"
- "Explore"
- "Get Yours Today"

**Placement:**
- Prominent in creative
- Clear and actionable
- Aligned with campaign objective

## A/B Testing Framework

### What to Test

**Creative Elements:**
- Headlines (benefit vs. feature)
- Images (product vs. lifestyle)
- Product selection
- CTAs

**Targeting:**
- Keyword match types
- Product targeting vs. keyword targeting
- Broad vs. narrow audiences

**Landing Pages:**
- Brand Store vs. product detail page
- Different Brand Store sub-pages
- Simple vs. custom landing pages

**Ad Formats:**
- Product Collection vs. Store Spotlight
- Static vs. video
- Horizontal vs. vertical video

### Testing Methodology

**Structure:**
1. Identify variable to test
2. Create 2-3 variations
3. Allocate equal budget initially
4. Run for minimum 2 weeks
5. Analyze statistical significance
6. Scale winner, pause losers

**Sample Size:**
- Minimum 1,000 impressions per variation
- Minimum 100 clicks per variation
- 95% confidence level for conclusions

**Documentation:**
- Record test hypothesis
- Track results systematically
- Document learnings
- Apply insights to future campaigns

## Key Takeaways

1. Brand Registry enrollment is mandatory for Sponsored Brands
2. Three campaign goals align with different marketing objectives
3. Three ad formats serve different strategic purposes
4. Keyword and product targeting offer complementary approaches
5. CPC and vCPM pricing models suit different campaign goals
6. Creative quality significantly impacts performance
7. Continuous testing and optimization are essential
8. Budget management ensures consistent delivery
9. Landing page strategy affects conversion rates
10. Integration with Brand Stores maximizes brand-building impact

## Campaign Setup Checklist

- [ ] Verify Brand Registry enrollment
- [ ] Ensure products are eligible and in stock
- [ ] Create or update Brand Store (for Store Spotlight)
- [ ] Select campaign goal (DPV, BIS, or Acquire New Customers)
- [ ] Choose ad format (Product Collection, Store Spotlight, or Video)
- [ ] Prepare creative assets (logo, images, video)
- [ ] Write compelling headlines
- [ ] Conduct keyword research
- [ ] Set up targeting (keywords, products, or themes)
- [ ] Add negative targeting
- [ ] Select pricing model (CPC or vCPM)
- [ ] Set daily budget
- [ ] Configure bid strategy
- [ ] Review and launch campaign
- [ ] Schedule performance review (1 week post-launch)
""",
        "targeting-optimization.md": """# Amazon Sponsored Brands: Targeting and Optimization Strategies

## Introduction

Effective targeting and continuous optimization are critical for Sponsored Brands success. This guide covers advanced targeting techniques, performance analysis, and systematic optimization approaches to maximize campaign ROI.

## Advanced Keyword Targeting

### Keyword Research Methodology

**Sources for Keyword Discovery:**

1. **Amazon's Suggested Keywords:**
   - Provided during campaign setup
   - Based on product data and category
   - Pre-vetted for relevance

2. **Sponsored Products Search Term Reports:**
   - Analyze high-performing search terms
   - Identify converting keywords
   - Discover long-tail opportunities

3. **Amazon Auto-Complete:**
   - Type product terms in Amazon search
   - Note suggested completions
   - Indicates popular search patterns

4. **Competitor Analysis:**
   - Identify competitor brand names
   - Note their product positioning keywords
   - Find category-defining terms

5. **Third-Party Tools:**
   - Helium 10
   - Jungle Scout
   - Sellics
   - Perpetua

**Keyword Categories:**

**Branded Keywords:**
- Your brand name
- Your product names
- Misspellings of your brand
- Purpose: Brand defense, capture existing demand

**Category Keywords:**
- Generic product category terms
- "coffee makers", "yoga mats", "wireless headphones"
- Purpose: Awareness, new customer acquisition

**Competitor Keywords:**
- Competitor brand names
- Competitor product names
- Purpose: Competitive conquest, market share growth

**Long-Tail Keywords:**
- Specific, detailed search terms
- "stainless steel french press coffee maker"
- Purpose: High-intent traffic, lower competition

**Feature-Based Keywords:**
- Specific product attributes
- "BPA-free water bottle", "noise-canceling headphones"
- Purpose: Qualified traffic, feature-focused shoppers

### Match Type Strategy

**Strategic Framework:**

**Exact Match Campaigns:**
- Highest bids (most relevant, highest conversion)
- Proven high-performers from broad/phrase campaigns
- Tight control over spend
- Maximum ROAS

**Phrase Match Campaigns:**
- Medium bids
- Balance of reach and relevance
- Captures variations while maintaining intent
- Good for scaling proven keywords

**Broad Match Campaigns:**
- Lowest bids
- Keyword discovery and testing
- Maximum reach
- Mine search term reports for new exact/phrase keywords

**Campaign Structure Example:**
```
Portfolio: Coffee Makers - Sponsored Brands
├── Campaign: Exact Match - High Performers
│   ├── Ad Group: Branded Exact
│   │   └── Keywords: [brand name] coffee maker (exact)
│   └── Ad Group: Category Exact
│       └── Keywords: french press coffee maker (exact)
├── Campaign: Phrase Match - Scaling
│   └── Ad Group: Category Phrase
│       └── Keywords: "coffee maker", "french press"
└── Campaign: Broad Match - Discovery
    └── Ad Group: Category Broad
        └── Keywords: coffee maker, french press
```

### Keyword Harvesting Process

**Weekly Workflow:**

1. **Download Search Term Report:**
   - Campaign Manager → Reports → Search Term Report
   - Last 7-30 days of data

2. **Identify High Performers:**
   - Filter for search terms with:
     - 5+ clicks
     - ACOS below target
     - 1+ conversions

3. **Add to Exact/Phrase Campaigns:**
   - Add high-performing terms as exact match keywords
   - Set competitive bids
   - Monitor performance

4. **Identify Negative Keywords:**
   - Filter for search terms with:
     - 10+ clicks, 0 conversions
     - ACOS above acceptable threshold
     - Irrelevant to products

5. **Add Negative Keywords:**
   - Add to campaign or ad group level
   - Use negative exact or negative phrase
   - Prevent future wasted spend

6. **Document and Repeat:**
   - Track keywords added/negated
   - Review impact in following weeks
   - Continuously refine

### Bid Management Strategies

**Initial Bid Setting:**
- Start with Amazon's suggested bid
- Or calculate based on target ACOS:
  ```
  Max CPC = (Product Price × Target ACOS) / 100
  ```
  Example: $50 product, 20% target ACOS
  Max CPC = ($50 × 20) / 100 = $10

**Bid Adjustment Rules:**

**Increase Bids (+10-20%) When:**
- ACOS below target
- High conversion rate
- Low impression share
- Losing top-of-search placement

**Decrease Bids (-10-20%) When:**
- ACOS above target
- Low conversion rate
- High spend, low return
- Excessive impression share

**Pause Keywords When:**
- 50+ clicks, 0 conversions
- ACOS consistently 2x+ target
- Irrelevant despite negative keywords

**Bid by Placement:**

**Top of Search:**
- Highest visibility
- Highest conversion rates
- Justify 50-200% bid increases
- Monitor ACOS closely

**Rest of Search:**
- Moderate visibility
- Good conversion rates
- 0-50% bid increases

**Product Pages:**
- Contextual relevance
- Variable conversion rates
- 0-100% bid increases
- Test and optimize

## Product Targeting Strategies

### Competitive Targeting

**Identifying Competitor ASINs:**

1. **Direct Competitors:**
   - Similar products, similar price points
   - Same category and use case
   - Target their top sellers

2. **Research Methods:**
   - Amazon Best Sellers lists
   - Category browsing
   - Sponsored Products search term reports
   - Third-party tools (Helium 10, Jungle Scout)

**Targeting Strategy:**

**High-Value Targets:**
- Competitor best sellers
- Products with 100+ reviews
- Products with 4+ star ratings
- Products in your price range

**Creative Messaging:**
- Highlight your differentiation
- Emphasize superior features
- Showcase better value
- Include social proof (reviews, ratings)

**Bid Strategy:**
- Competitive bids to win placement
- Monitor ACOS carefully
- Test different competitor ASINs
- Scale winners, pause losers

### Complementary Product Targeting

**Strategy:**
Target products that are frequently purchased together with yours.

**Examples:**
- Sell coffee → Target coffee makers
- Sell phone cases → Target popular phone models
- Sell yoga mats → Target yoga blocks, straps
- Sell printer ink → Target printer models

**Benefits:**
- High relevance
- Cross-sell opportunities
- Captures shoppers in buying mode
- Often lower competition than direct competitors

**Implementation:**
1. Identify complementary products
2. Target individual ASINs or categories
3. Create relevant ad creative
4. Emphasize compatibility or pairing

### Own-Product Targeting

**Use Cases:**

**Upselling:**
- Target your entry-level product pages
- Advertise premium versions
- Highlight additional features and benefits

**Cross-Selling:**
- Target your popular products
- Advertise complementary items from your catalog
- Create bundles or sets

**Defensive:**
- Target your own product pages
- Prevent competitor ads from appearing
- Maintain brand presence

**Strategy:**
- Lower bids than competitive targeting
- Focus on incremental sales
- Test impact on overall sales (not just ad-attributed)

### Category Targeting with Refinements

**Broad Category Targeting:**
- Target entire product categories
- Maximum reach
- Lower relevance

**Refined Category Targeting:**

**By Price Range:**
- Match your product's price tier
- Example: $50-$100 for mid-range products
- Improves relevance and conversion

**By Star Rating:**
- Target 4+ star products
- Ensures quality context
- Better brand association

**By Brand:**
- Include specific competitor brands
- Exclude your own brand (avoid cannibalization)
- Focus on target competitors

**By Prime Eligibility:**
- Target Prime-eligible products
- Reach Prime members
- Higher conversion rates

**Example Refined Target:**
- Category: Coffee Makers
- Price: $50-$150
- Rating: 4+ stars
- Prime: Yes
- Exclude: [Your Brand]

## Performance Analysis

### Key Metrics and Benchmarks

**Impressions:**
- Indicates reach and visibility
- Low impressions → Increase bids, expand targeting
- High impressions, low clicks → Improve creative

**Click-Through Rate (CTR):**
- Benchmark: 0.3-0.5% (varies by category)
- Measures ad relevance and appeal
- Low CTR → Improve headline, image, or targeting

**Clicks:**
- Engagement metric
- Drives traffic to Brand Store or product pages
- Monitor cost per click (CPC)

**Detail Page View Rate (DPVR):**
- Percentage of clicks that result in product page views
- Benchmark: 80-95%
- Low DPVR → Check landing page relevance

**Purchases:**
- Ultimate conversion metric
- Track total purchases and new-to-brand purchases

**Sales:**
- Total revenue attributed to ads
- Includes all products purchased, not just advertised

**Advertising Cost of Sales (ACOS):**
- Formula: (Ad Spend / Ad Sales) × 100
- Benchmark: 15-30% (varies by margin and goals)
- Lower ACOS = higher profitability

**Return on Ad Spend (ROAS):**
- Formula: Ad Sales / Ad Spend
- Inverse of ACOS
- Benchmark: 3:1 to 6:1
- Higher ROAS = better efficiency

**New-to-Brand (NTB) Metrics:**
- Orders from first-time customers (last 12 months)
- NTB sales
- NTB percentage
- Critical for growth and customer acquisition

**Cost Per Acquisition (CPA):**
- Formula: Ad Spend / Total Orders
- Benchmark: Should be below customer lifetime value
- Varies significantly by product and margin

### Report Analysis

**Campaign Report:**
- Overall campaign performance
- Budget pacing
- High-level metrics
- Use for: Budget allocation decisions

**Keyword Report:**
- Performance by keyword
- Impressions, clicks, sales, ACOS
- Use for: Bid adjustments, keyword optimization

**Search Term Report:**
- Actual customer search queries
- Identifies new keyword opportunities
- Reveals irrelevant terms for negative targeting
- Use for: Keyword harvesting, negative keyword discovery

**Advertised Product Report:**
- Performance by advertised ASIN
- Identifies top-performing products
- Use for: Product selection optimization

**Placement Report:**
- Performance by ad placement (top of search, rest of search, product pages)
- Use for: Placement bid adjustments

**Performance Over Time Report:**
- Trend analysis
- Day-of-week and time-of-day patterns
- Use for: Identifying seasonality, optimal timing

### Segmentation Analysis

**By Campaign Goal:**
- Compare DPV vs. BIS vs. Acquire New Customers
- Assess goal achievement
- Reallocate budget to best-performing goals

**By Ad Format:**
- Product Collection vs. Store Spotlight vs. Video
- Engagement and conversion rates
- Creative performance insights

**By Targeting Type:**
- Keyword vs. Product targeting
- Branded vs. non-branded keywords
- Competitive vs. complementary product targeting

**By Device:**
- Desktop vs. Mobile vs. Tablet
- Conversion rate differences
- Bid adjustment opportunities

**By Match Type:**
- Exact vs. Phrase vs. Broad
- Efficiency and scale trade-offs
- Budget allocation optimization

## Optimization Workflows

### Daily Optimization (First 2 Weeks)

**Time Required:** 15-30 minutes

**Tasks:**
1. **Check Budget Pacing:**
   - Are campaigns spending as expected?
   - Adjust budgets if over/under-pacing

2. **Review Delivery:**
   - Are ads getting impressions?
   - Increase bids if low delivery

3. **Monitor Early Signals:**
   - CTR trends
   - Early conversion data
   - Any errors or issues

4. **Quick Adjustments:**
   - Pause non-delivering campaigns
   - Increase budgets for fast-spending campaigns
   - Address any approval issues

### Weekly Optimization (Ongoing)

**Time Required:** 1-2 hours

**Tasks:**

1. **Performance Review:**
   - [ ] Download all reports (campaign, keyword, search term, placement)
   - [ ] Calculate week-over-week changes
   - [ ] Identify top and bottom performers

2. **Keyword Optimization:**
   - [ ] Harvest high-performing search terms
   - [ ] Add as exact/phrase match keywords
   - [ ] Identify and add negative keywords
   - [ ] Adjust bids based on ACOS and conversion rate

3. **Budget Reallocation:**
   - [ ] Increase budgets for high-ROAS campaigns (+20-30%)
   - [ ] Decrease budgets for low-ROAS campaigns (-20-30%)
   - [ ] Pause consistently poor performers

4. **Bid Adjustments:**
   - [ ] Increase bids for below-target ACOS keywords
   - [ ] Decrease bids for above-target ACOS keywords
   - [ ] Adjust placement bids based on performance

5. **Creative Testing:**
   - [ ] Review CTR by creative
   - [ ] Launch new creative tests
   - [ ] Pause low-performing creatives

6. **Competitive Monitoring:**
   - [ ] Check competitor ad presence
   - [ ] Adjust bids for competitive keywords
   - [ ] Identify new competitor targets

7. **Documentation:**
   - [ ] Record key changes made
   - [ ] Note insights and hypotheses
   - [ ] Update optimization log

### Monthly Strategic Review

**Time Required:** 2-4 hours

**Tasks:**

1. **Comprehensive Performance Analysis:**
   - Month-over-month trends
   - Goal achievement vs. targets
   - Budget utilization
   - ROAS and ACOS trends

2. **Deep Dive by Segment:**
   - Campaign goal performance
   - Ad format effectiveness
   - Targeting type analysis
   - Device and placement performance

3. **Keyword Portfolio Review:**
   - Top 20 keywords by sales
   - Bottom 20 keywords by ACOS
   - Keyword coverage gaps
   - Competitive keyword performance

4. **Creative Performance:**
   - CTR trends over time
   - Creative fatigue indicators
   - A/B test results
   - Plan creative refreshes

5. **Competitive Landscape:**
   - Competitor ad activity changes
   - Market share shifts
   - New competitor entrants
   - Adjust strategy accordingly

6. **Strategic Planning:**
   - Set next month's goals and KPIs
   - Plan new tests and initiatives
   - Adjust budget allocation
   - Identify growth opportunities

7. **Stakeholder Reporting:**
   - Prepare monthly performance report
   - Highlight wins and challenges
   - Present recommendations
   - Align on priorities

## Advanced Optimization Techniques

### Dayparting Analysis

**Process:**
1. Download Performance Over Time report
2. Analyze conversion rate by hour of day
3. Identify peak performance windows
4. Adjust bids or budgets accordingly

**Note:** Sponsored Brands doesn't support automatic dayparting, but you can:
- Manually adjust budgets at different times
- Use third-party tools for automation
- Focus optimization on high-performing days/times

### Seasonal Optimization

**Seasonal Patterns:**
- Q4 holiday shopping surge
- Back-to-school (July-August)
- New Year's resolutions (January)
- Category-specific seasons

**Optimization Actions:**
- Increase budgets during peak seasons
- Create seasonal creative and messaging
- Adjust keyword strategy for seasonal terms
- Plan campaigns 4-6 weeks in advance

### Audience Layering (via Product Targeting)

**Strategy:**
Combine product targeting with specific audience characteristics.

**Example:**
- Target: Coffee Maker category
- Refine: Price $100-$200, 4+ stars, Prime
- Result: High-quality, mid-to-premium segment

**Benefits:**
- Increased relevance
- Better conversion rates
- More efficient spend

### Cross-Campaign Optimization

**Sponsored Brands + Sponsored Products:**
- Use Sponsored Products for keyword discovery
- Promote top performers with Sponsored Brands
- Coordinate messaging and creative
- Measure combined impact

**Sponsored Brands + Sponsored Display:**
- Sponsored Brands for awareness and consideration
- Sponsored Display for remarketing
- Sequential messaging strategy

**Sponsored Brands + DSP:**
- DSP for off-Amazon awareness
- Sponsored Brands for on-Amazon conversion
- Unified brand messaging

### Portfolio-Level Optimization

**Portfolio Benefits:**
- Shared budget across campaigns
- Automatic reallocation to top performers
- Simplified budget management
- Holistic performance view

**Best Practices:**
- Group campaigns by objective or product line
- Set portfolio budget caps
- Monitor individual campaign performance
- Adjust allocation based on strategic priorities

## Common Optimization Challenges

### Challenge: Low Impressions

**Possible Causes:**
- Bids too low
- Targeting too narrow
- Budget too low
- Low search volume for keywords

**Solutions:**
- Increase bids by 20-50%
- Expand keyword targeting (add broad match)
- Increase daily budget
- Research higher-volume keywords
- Check campaign approval status

### Challenge: High Impressions, Low Clicks (Low CTR)

**Possible Causes:**
- Weak creative (headline, image)
- Irrelevant targeting
- Uncompetitive pricing
- Poor product reviews

**Solutions:**
- Refresh creative assets
- Test new headlines
- Refine targeting (add negative keywords)
- Improve product detail pages
- Ensure competitive pricing

### Challenge: High Clicks, Low Conversions

**Possible Causes:**
- Misleading ad creative
- Poor landing page experience
- Uncompetitive pricing
- Out of stock
- Poor product reviews

**Solutions:**
- Ensure ad matches landing page
- Optimize Brand Store or product pages
- Review pricing strategy
- Maintain inventory
- Improve product listings (images, descriptions, A+ content)
- Encourage positive reviews

### Challenge: High ACOS

**Possible Causes:**
- Bids too high
- Low conversion rate
- Targeting too broad
- Competitive market

**Solutions:**
- Decrease bids by 10-20%
- Add negative keywords
- Focus on exact match, high-intent keywords
- Improve conversion rate (landing page, pricing)
- Adjust target ACOS expectations

### Challenge: Budget Running Out Early

**Possible Causes:**
- Budget too low for bid levels
- High-volume keywords
- Competitive bidding environment

**Solutions:**
- Increase daily budget
- Decrease bids slightly
- Implement more negative keywords
- Focus on higher-converting keywords

### Challenge: Underspending Budget

**Possible Causes:**
- Bids too low
- Targeting too narrow
- Low search volume

**Solutions:**
- Increase bids
- Expand targeting (more keywords, broader match types)
- Add product targeting
- Research new keyword opportunities

## Optimization Best Practices

### 1. Data-Driven Decision Making

- Wait for statistical significance (minimum 100 clicks)
- Don't make changes too frequently (allow 7-14 days)
- Use reports, not gut feelings
- Document changes and results

### 2. Systematic Testing

- Test one variable at a time
- Use control groups when possible
- Run tests for sufficient duration
- Apply learnings systematically

### 3. Continuous Improvement

- Never "set and forget"
- Weekly optimization minimum
- Stay updated on Amazon Ads features
- Learn from competitors

### 4. Holistic Approach

- Consider full customer journey
- Coordinate across ad types
- Optimize product listings, not just ads
- Balance short-term ROAS with long-term growth

### 5. Strategic Patience

- Allow learning phase (2-4 weeks)
- Don't panic over short-term fluctuations
- Focus on trends, not daily variations
- Balance efficiency with growth

## Key Takeaways

1. Keyword harvesting is essential for continuous improvement
2. Match type strategy balances reach and efficiency
3. Product targeting offers complementary opportunities to keywords
4. Regular performance analysis identifies optimization opportunities
5. Systematic workflows ensure consistent optimization
6. Bid management directly impacts ACOS and ROAS
7. Creative quality significantly affects CTR and conversions
8. Negative targeting is as important as positive targeting
9. Cross-campaign coordination amplifies results
10. Patience and data-driven decisions lead to long-term success

## Optimization Checklist

- [ ] Weekly keyword harvesting from search term reports
- [ ] Negative keyword additions
- [ ] Bid adjustments based on ACOS/ROAS
- [ ] Budget reallocation to top performers
- [ ] Creative performance review
- [ ] Placement bid optimization
- [ ] Competitive monitoring
- [ ] New keyword/product target testing
- [ ] Landing page optimization
- [ ] Monthly strategic review
- [ ] Stakeholder reporting
- [ ] Documentation of changes and learnings
"""
    }
}

def create_reference_files():
    """Create all reference files for Batch 2 skills"""
    
    base_path = Path("/home/ubuntu/github_repos/manus")
    files_created = 0
    
    for skill in BATCH2_SKILLS:
        skill_path = base_path / skill / "references"
        skill_path.mkdir(parents=True, exist_ok=True)
        
        # Get reference content for this skill
        if skill in REFERENCE_CONTENT:
            for filename, content in REFERENCE_CONTENT[skill].items():
                file_path = skill_path / filename
                file_path.write_text(content)
                files_created += 1
                print(f"Created: {file_path}")
    
    return files_created

if __name__ == "__main__":
    print("Generating Batch 2 reference files...")
    count = create_reference_files()
    print(f"\nTotal files created: {count}")
