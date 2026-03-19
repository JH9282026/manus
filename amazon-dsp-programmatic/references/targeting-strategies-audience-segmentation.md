# Advanced Targeting Strategies and Audience Segmentation in Amazon DSP

## Introduction to DSP Targeting

Targeting is the foundation of successful Amazon DSP campaigns. Unlike traditional display advertising that relies heavily on demographic assumptions, Amazon DSP leverages actual shopping behavior, making targeting more precise and effective. This guide covers advanced targeting strategies and audience segmentation techniques.

## Core Targeting Methodologies

### 1. Audience Targeting

Audience targeting uses Amazon's first-party data to reach specific customer segments based on their shopping and streaming behavior.

#### Amazon Audiences

**In-Market Audiences:**
- Shoppers actively researching or purchasing in specific categories
- Based on recent search and browse behavior
- High purchase intent
- Refreshed regularly to maintain relevance

*Example Categories:*
- Electronics > Laptops
- Home & Kitchen > Coffee Makers
- Beauty > Skincare
- Sports & Outdoors > Fitness Equipment

**Lifestyle Audiences:**
- Segments based on long-term purchase patterns
- Reflect customer interests and life stages
- Broader reach than in-market
- Useful for brand awareness

*Example Segments:*
- Fitness Enthusiasts
- Pet Owners
- Home Improvement DIYers
- Tech Early Adopters
- Eco-Conscious Shoppers

**Life Event Audiences:**
- Customers experiencing major life changes
- High-value targeting opportunities
- Time-sensitive relevance

*Example Events:*
- New Parents
- Recent Movers
- College Students
- Wedding Planning
- New Homeowners

**Demographic Audiences:**
- Age ranges
- Gender
- Household income
- Education level
- Marital status

**Streaming Audiences:**
- Prime Video viewers by genre
- Twitch viewers by game/category
- Music listeners by genre
- Podcast listeners

#### Custom Audiences

**Pixel-Based Audiences:**
- Website visitors (all or specific pages)
- Cart abandoners
- Product page viewers
- Converters (for exclusion or upsell)

*Implementation:*
```html
<!-- Amazon DSP Pixel -->
<script>
!function(e,i){if(!e.pixie){var n=e.pixie=function(e,i,a){n.actionQueue.push({action:e,actionValue:i,params:a})};n.actionQueue=[];var a=i.createElement("script");a.async=!0,a.src="//aax-us-east.amazon-adsystem.com/s/iu3?d=amazon-adsystem.com&pid=ADVERTISER_ID&tag=1";var t=i.getElementsByTagName("script")[0];t.parentNode.insertBefore(a,t)}}
(window,document);
pixie('event', 'PageView');
</script>
```

**ASIN Remarketing:**
- Shoppers who viewed specific products
- Purchasers of specific products
- Category viewers
- Brand page visitors

**Brand Remarketing:**
- Searched for your brand
- Viewed your brand's products
- Purchased from your brand
- Engaged with your brand content

**Uploaded Audiences:**
- Customer email lists (hashed)
- CRM data integration
- Loyalty program members
- First-party data activation

*Data Requirements:*
- Minimum 1,000 matched users
- Hashed email addresses (SHA-256)
- Compliance with privacy regulations
- Customer consent for advertising

#### Lookalike Audiences

**Seed Audience Options:**
- Past purchasers
- High-value customers
- Website converters
- Engaged users
- Custom uploaded lists

**Expansion Strategies:**
- Similar shopping behavior
- Comparable demographic profiles
- Matching lifestyle indicators
- Parallel browsing patterns

**Optimization Tips:**
- Use high-quality seed audiences (1,000+ users)
- Test different similarity thresholds
- Combine with contextual targeting
- Monitor performance vs. seed audience

### 2. Contextual Targeting

Contextual targeting places ads based on page content, ensuring relevance without relying on user data.

#### Category Contextual

**Amazon Category Targeting:**
- Place ads on specific category pages
- Target shoppers browsing related products
- Capture high-intent moments

*Example Strategy:*
- Selling coffee makers → Target "Coffee & Espresso" category
- Selling yoga mats → Target "Yoga" category

**Third-Party Category Targeting:**
- IAB content categories
- Publisher-defined categories
- Vertical-specific placements

#### Keyword Contextual

**Page-Level Keywords:**
- Target pages containing specific keywords
- Broad match, phrase match, exact match
- Negative keywords for exclusion

**Semantic Targeting:**
- AI-powered content understanding
- Topic-based targeting
- Brand safety considerations

### 3. Product Targeting

Product targeting allows precise placement on specific product detail pages or targeting users who interacted with those products.

#### ASIN Targeting

**Competitive Targeting:**
- Target competitor product pages
- Capture consideration-stage shoppers
- Offer alternative solutions

*Strategy:*
1. Identify top competitor ASINs
2. Analyze their traffic and reviews
3. Create compelling comparison messaging
4. Bid competitively for placement

**Complementary Targeting:**
- Target products that pair with yours
- Cross-sell opportunities
- Bundle suggestions

*Example:*
- Selling phone cases → Target popular phone ASINs
- Selling coffee → Target coffee maker ASINs

**Own-Product Targeting:**
- Target your own product pages
- Upsell to premium versions
- Cross-sell related products
- Defend against competitors

#### Category Targeting

**Broad Category:**
- Reach all products in a category
- Maximum scale
- Lower precision

**Refined Category:**
- Filter by price range
- Filter by review rating
- Filter by brand
- Filter by Prime eligibility

*Example Refinement:*
- Category: Laptops
- Price: $800-$1,500
- Rating: 4+ stars
- Prime: Yes

### 4. Geographic Targeting

#### Country-Level
- Target specific countries
- Align with product availability
- Consider language and cultural factors

#### State/Province-Level
- Regional campaigns
- State-specific promotions
- Seasonal geographic strategies

#### DMA (Designated Market Area)
- TV market-based targeting
- Local business advertising
- Event-based geographic targeting

#### Postal Code Targeting
- Hyper-local campaigns
- Store proximity targeting
- Neighborhood-level precision

### 5. Device and Platform Targeting

#### Device Type
- Desktop
- Mobile (smartphone)
- Tablet
- Connected TV / Fire TV
- Kindle devices

#### Operating System
- iOS
- Android
- Windows
- macOS
- Fire OS

#### Browser
- Chrome
- Safari
- Firefox
- Edge

**Strategy Considerations:**
- Mobile users: shorter attention, on-the-go context
- Desktop users: research mode, longer sessions
- CTV users: lean-back experience, brand awareness

### 6. Dayparting and Scheduling

#### Time-of-Day Targeting

**Morning (6 AM - 12 PM):**
- Commuters on mobile
- Early shoppers
- B2B decision-makers

**Afternoon (12 PM - 6 PM):**
- Peak browsing hours
- Lunch break shopping
- Highest competition

**Evening (6 PM - 12 AM):**
- Leisure browsing
- CTV viewing
- Highest conversion rates for many categories

**Late Night (12 AM - 6 AM):**
- Lower CPMs
- Niche audiences
- International time zones

#### Day-of-Week Targeting

**Weekdays:**
- B2B targeting
- Routine shopping
- Consistent traffic

**Weekends:**
- Leisure shopping
- Higher engagement
- Family decision-making

**Strategic Dayparting:**
- Analyze historical performance by hour/day
- Adjust bids based on conversion rates
- Allocate budget to peak performance windows

## Advanced Audience Strategies

### Audience Layering

Combine multiple targeting criteria for precision:

**Example 1: High-Intent Fitness Buyer**
- In-market: Fitness Equipment
- + Lifestyle: Fitness Enthusiasts
- + Viewed: Competitor ASINs
- + Device: Mobile

**Example 2: Premium Home Decor Prospect**
- Lifestyle: Home Improvement
- + Demographic: Household Income $100K+
- + Contextual: Home & Garden categories
- + Geographic: Urban areas

**Example 3: Cart Abandoner Re-engagement**
- Pixel: Cart abandoners (last 7 days)
- + Exclude: Converters (last 30 days)
- + Frequency cap: 3 impressions per day
- + Creative: Urgency messaging with offer

### Audience Exclusions

**Strategic Exclusions:**
- Recent converters (avoid ad waste)
- Existing customers (for acquisition campaigns)
- Low-value segments (based on historical data)
- Competitor brand loyalists (low conversion probability)

**Frequency Management:**
- Exclude users who've seen ads X times
- Prevent ad fatigue
- Optimize budget efficiency

### Sequential Messaging

Deliver different messages based on user journey stage:

**Stage 1: Awareness (Days 1-3)**
- Audience: Broad in-market
- Message: Brand introduction, problem identification
- Creative: Video, lifestyle imagery

**Stage 2: Consideration (Days 4-7)**
- Audience: Engaged with Stage 1 ads
- Message: Product benefits, differentiation
- Creative: Product features, comparisons

**Stage 3: Conversion (Days 8-14)**
- Audience: Engaged with Stage 2, visited website
- Message: Offer, urgency, social proof
- Creative: Dynamic e-commerce ads, reviews

**Stage 4: Retention (Post-purchase)**
- Audience: Recent purchasers
- Message: Cross-sell, upsell, loyalty
- Creative: Complementary products, subscription offers

### Audience Testing Framework

**Test Structure:**
1. Control group (broad audience)
2. Test group 1 (refined audience A)
3. Test group 2 (refined audience B)
4. Test group 3 (refined audience C)

**Variables to Test:**
- Audience size (broad vs. narrow)
- Audience type (in-market vs. lifestyle)
- Layering combinations
- Lookalike similarity thresholds

**Success Metrics:**
- Reach and scale
- Cost per acquisition (CPA)
- Return on ad spend (ROAS)
- Conversion rate
- New-to-brand rate

## Modeled and Similar Audiences

As third-party cookies decline, Amazon's modeled audiences become increasingly important:

### Modeled Audience Types

**Purchase-Based Models:**
- Predicted to purchase in category
- Similar purchase patterns to seed audience
- High-value customer models

**Engagement-Based Models:**
- Likely to engage with content
- Video completion probability
- Click-through likelihood

**Behavioral Models:**
- Shopping frequency patterns
- Category affinity predictions
- Brand switching propensity

### Similar Audiences (Beta)

**Functionality:**
- Automatically find users similar to your audience
- Continuous optimization and expansion
- Machine learning-powered matching

**Best Practices:**
- Start with high-quality seed audiences
- Monitor performance vs. original audience
- Adjust similarity threshold based on goals
- Combine with other targeting for precision

## Targeting for Different Campaign Objectives

### Brand Awareness Campaigns

**Recommended Targeting:**
- Broad in-market audiences
- Lifestyle segments
- Contextual category targeting
- Premium inventory (OTT, Prime Video)

**Avoid:**
- Overly narrow audiences (limits reach)
- Heavy remarketing (preaching to converted)

### Consideration Campaigns

**Recommended Targeting:**
- In-market audiences
- Competitor ASIN targeting
- Lookalike audiences
- Engaged website visitors

**Avoid:**
- Recent converters
- Unrelated categories

### Conversion Campaigns

**Recommended Targeting:**
- Cart abandoners
- Product page viewers
- High-intent in-market
- Remarketing with frequency caps

**Avoid:**
- Cold audiences (inefficient for direct conversion)
- Broad contextual (low intent)

### Customer Retention

**Recommended Targeting:**
- Past purchasers
- Loyalty program members
- High lifetime value customers
- Subscription renewal windows

**Avoid:**
- Acquisition-focused messaging
- Competitor targeting

## Measurement and Optimization

### Key Targeting Metrics

**Reach Metrics:**
- Unique reach
- Frequency
- Impression share

**Engagement Metrics:**
- Click-through rate (CTR)
- Video completion rate (VCR)
- Detail page view rate (DPVR)

**Conversion Metrics:**
- Conversion rate
- Cost per acquisition (CPA)
- Return on ad spend (ROAS)
- New-to-brand percentage

### Audience Performance Analysis

**Weekly Review:**
1. Identify top-performing audiences
2. Analyze underperforming segments
3. Adjust bids and budgets
4. Test new audience combinations

**Monthly Deep Dive:**
1. Audience overlap analysis (via AMC)
2. Incremental reach assessment
3. Path-to-conversion by audience
4. Lifetime value by acquisition source

### Optimization Actions

**Scale Winners:**
- Increase budgets for top performers
- Expand to lookalike audiences
- Test broader match types

**Refine Underperformers:**
- Add audience layers for precision
- Adjust creative messaging
- Test different ad formats
- Consider pausing if consistently poor

**Continuous Testing:**
- Always have 20-30% of budget in testing
- Test new Amazon audience releases
- Experiment with audience combinations
- Validate assumptions with data

## Privacy and Compliance

### Data Privacy Considerations

**Amazon's Approach:**
- Privacy-safe audience creation
- No PII shared with advertisers
- Aggregated reporting only
- Compliance with GDPR, CCPA, etc.

**Advertiser Responsibilities:**
- Obtain proper consent for pixel data
- Hash uploaded audience data
- Comply with privacy regulations
- Respect opt-out preferences

### Future-Proofing Targeting

**Cookieless Strategies:**
- Prioritize Amazon's first-party audiences
- Invest in contextual targeting
- Build owned audience data (pixels, uploads)
- Leverage modeled audiences

**First-Party Data Collection:**
- Implement Amazon pixel comprehensively
- Collect email addresses (with consent)
- Build CRM integration
- Create value exchange for data sharing

## Key Takeaways

1. Amazon DSP's targeting strength lies in shopping behavior data
2. Layer multiple targeting criteria for precision and scale
3. Use sequential messaging to guide customers through the funnel
4. Test continuously to discover high-performing audiences
5. Balance reach and precision based on campaign objectives
6. Leverage modeled audiences for cookieless future
7. Measure incrementality, not just last-click attribution
8. Respect privacy while maximizing targeting effectiveness

## Targeting Checklist

- [ ] Define campaign objective and target audience
- [ ] Select primary targeting method (audience, contextual, product)
- [ ] Layer additional targeting for precision
- [ ] Set up audience exclusions
- [ ] Configure geographic targeting
- [ ] Set device and platform preferences
- [ ] Implement dayparting if relevant
- [ ] Install Amazon pixel for remarketing
- [ ] Create lookalike audiences from converters
- [ ] Set frequency caps
- [ ] Plan sequential messaging strategy
- [ ] Define success metrics
- [ ] Schedule regular performance reviews
- [ ] Allocate budget for testing new audiences