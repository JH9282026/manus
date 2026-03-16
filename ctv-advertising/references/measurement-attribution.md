# CTV Measurement & Attribution

Comprehensive guide to measuring and attributing Connected TV advertising performance.

---

## Key Performance Metrics

### Delivery Metrics

**Impressions**
- Total number of times ad was served
- Counted when ad begins playing
- Standard metric across all platforms

**Reach**
- Unique households that saw the ad
- Measured at household level (not device level)
- Typically reported as absolute number or % of target audience

**Frequency**
- Average number of times each household saw the ad
- Calculated as: Impressions ÷ Reach
- Optimal range: 3-5 impressions per household per week

**CPM (Cost Per Thousand Impressions)**
- Cost to reach 1,000 impressions
- Calculated as: (Total Spend ÷ Impressions) × 1,000
- Benchmark: $20-$65 depending on platform and targeting

### Engagement Metrics

**Completion Rate (VCR - Video Completion Rate)**
- Percentage of viewers who watched entire ad
- Calculated as: (Completed Views ÷ Impressions) × 100
- Benchmark: 85%+ is good; 90%+ is excellent
- Strong indicator of creative quality and placement

**Quartile Completion**
- 25% complete, 50% complete, 75% complete, 100% complete
- Identifies where viewers drop off
- Useful for creative optimization

**Interactive Engagement**
- QR code scans
- Click-through rate (for interactive ads)
- Voice command usage
- Shoppable ad interactions

### Business Outcome Metrics

**Website Visits**
- Visits to advertiser website post-ad exposure
- Measured via pixel tracking or attribution platforms
- Typically measured within 1-7 day window

**Conversions**
- Desired actions (purchases, sign-ups, downloads)
- Attributed to CTV ad exposure
- Measured via conversion pixels or attribution platforms

**Cost Per Acquisition (CPA)**
- Cost to acquire one customer/conversion
- Calculated as: Total Spend ÷ Conversions
- Varies significantly by industry and product

**Return on Ad Spend (ROAS)**
- Revenue generated per dollar spent
- Calculated as: Revenue ÷ Ad Spend
- Benchmark: 3:1 to 5:1 for most industries

**Brand Lift**
- Increase in brand awareness, consideration, or purchase intent
- Measured via surveys comparing exposed vs. control groups
- Typical lift: 5-15% for awareness; 3-10% for consideration

---

## Attribution Methodologies

### Pixel-Based Attribution

**How It Works**
- Place tracking pixel on advertiser website
- Match CTV ad exposure to website visits
- Use household IP matching or device graphs
- Track conversions within attribution window (1-30 days)

**Implementation**
- Install platform-specific pixels (Roku OneView, Amazon Attribution, etc.)
- Or use third-party attribution platforms (iSpot, TVSquared, etc.)
- Set attribution window (typically 7 days)
- Define conversion events (page views, purchases, sign-ups)

**Pros**
- Direct measurement of website impact
- Can track full conversion funnel
- Works across devices (CTV exposure → mobile/desktop conversion)

**Cons**
- Requires sufficient website traffic for statistical significance
- Privacy limitations (iOS, cookie restrictions)
- May undercount conversions due to matching limitations

**Best For**
- E-commerce advertisers
- Lead generation campaigns
- Direct response objectives

### QR Code Tracking

**How It Works**
- Display unique QR code in CTV ad
- Track scans via QR platform (Bitly, QR Code Generator, etc.)
- Measure scan-to-conversion rate
- Attribute all QR-driven traffic to CTV campaign

**Implementation**
- Generate unique QR code per campaign/creative
- Link to campaign-specific landing page
- Add UTM parameters for tracking (utm_source=ctv&utm_medium=qr)
- Display QR for minimum 5 seconds in ad
- Track scans and downstream conversions

**Pros**
- 100% accurate attribution (direct response)
- Easy to implement
- Provides clear ROI measurement
- Works across all platforms

**Cons**
- Requires viewer action (lower response rate)
- Only captures direct response, not brand impact
- Scan rates vary (typically 2-5% of viewers)

**Best For**
- Direct response campaigns
- Offer-driven campaigns
- Measuring immediate engagement

### Promo Code Attribution

**How It Works**
- Display unique promo code in CTV ad
- Track redemptions via e-commerce platform or POS system
- Attribute all promo code usage to CTV campaign
- Measure incremental sales driven by campaign

**Implementation**
- Create unique promo code for CTV campaign
- Display prominently in ad (minimum 5 seconds)
- Mention in voiceover
- Track redemptions in e-commerce or POS system
- Calculate incremental revenue and ROAS

**Pros**
- 100% accurate attribution
- Measures actual sales impact
- Easy to implement
- Works for online and offline purchases

**Cons**
- Only captures direct response
- Requires viewer to remember and enter code
- May cannibalize full-price sales
- Redemption rates vary (typically 1-3% of viewers)

**Best For**
- E-commerce campaigns
- Promotional campaigns
- Measuring direct sales impact

### Brand Lift Studies

**How It Works**
- Survey exposed and control groups
- Measure difference in brand metrics (awareness, consideration, intent)
- Calculate lift percentage
- Platforms conduct studies automatically (Roku, Hulu, YouTube)

**Implementation**
- Work with platform to set up study (often free for campaigns over $10K-$25K)
- Define metrics to measure (awareness, consideration, purchase intent, etc.)
- Platform serves surveys to exposed and control groups
- Receive results after campaign (typically 2-4 weeks)

**Metrics Measured**
- **Ad Recall**: "Do you recall seeing an ad for [brand]?"
- **Brand Awareness**: "Which of these brands have you heard of?"
- **Consideration**: "Which brands would you consider purchasing?"
- **Purchase Intent**: "How likely are you to purchase [brand]?"
- **Message Association**: "Which brand do you associate with [message]?"

**Pros**
- Measures brand impact, not just direct response
- Statistically rigorous methodology
- Often free from platforms
- Provides competitive benchmarking

**Cons**
- Requires large sample size (typically 10,000+ impressions)
- Results delayed (2-4 weeks post-campaign)
- Doesn't measure actual sales
- Survey fatigue can affect accuracy

**Best For**
- Brand awareness campaigns
- Upper-funnel objectives
- Measuring brand health

### Foot Traffic Attribution

**How It Works**
- Match CTV ad exposure to mobile device IDs
- Track mobile location data to measure store visits
- Compare store visit rates: exposed vs. control groups
- Calculate incremental store visits driven by CTV campaign

**Implementation**
- Work with attribution partner (Placed, Cuebiq, Foursquare, etc.)
- Define store locations (addresses or geofences)
- Set attribution window (typically 7-14 days)
- Match CTV exposure to mobile devices
- Measure store visits among exposed vs. control

**Pros**
- Measures offline impact
- Works for retail, QSR, automotive, healthcare
- Provides incremental visit measurement
- Can calculate cost per visit and visit-to-sale rate

**Cons**
- Requires mobile location data (privacy concerns)
- Matching rates vary (typically 30-50% of households)
- Delayed results (2-4 weeks post-campaign)
- Requires sufficient store traffic for statistical significance

**Best For**
- Retail advertisers
- QSR (quick-service restaurants)
- Automotive dealerships
- Healthcare providers

### Cross-Device Attribution

**How It Works**
- Use device graphs to connect CTV, mobile, desktop, and tablet
- Track user journey across devices
- Attribute conversions to CTV touchpoint
- Measure multi-touch attribution

**Implementation**
- Work with attribution platform (LiveRamp, Neustar, Tapad, etc.)
- Implement tracking across all devices
- Define attribution model (last-touch, first-touch, multi-touch)
- Set attribution window
- Analyze cross-device conversion paths

**Attribution Models**
- **Last-Touch**: 100% credit to last touchpoint before conversion
- **First-Touch**: 100% credit to first touchpoint (CTV)
- **Linear**: Equal credit to all touchpoints
- **Time Decay**: More credit to recent touchpoints
- **Position-Based**: More credit to first and last touchpoints
- **Data-Driven**: Algorithmic credit based on actual conversion patterns

**Pros**
- Captures full customer journey
- Accounts for multi-device behavior
- Provides holistic view of CTV impact
- Can optimize across channels

**Cons**
- Complex implementation
- Requires significant data and scale
- Matching rates vary
- Privacy limitations

**Best For**
- Multi-channel campaigns
- Understanding customer journey
- Optimizing channel mix

---

## Platform-Specific Measurement

### Roku OneView Attribution

**Capabilities**
- Website visit tracking
- Conversion tracking
- Cross-device attribution
- Household-level measurement

**Implementation**
- Install Roku OneView pixel on website
- Define conversion events
- Set attribution window (1-30 days)
- Roku matches ad exposure to website visits

**Metrics Provided**
- Impressions, reach, frequency
- Completion rate
- Website visits (total and incremental)
- Conversions (total and incremental)
- Cost per visit, cost per conversion
- ROAS

**Best Practices**
- Use 7-day attribution window for most campaigns
- Extend to 14-30 days for longer purchase cycles
- Segment by audience, creative, daypart
- Compare to control group for incrementality

### Amazon Attribution

**Capabilities**
- Amazon product page visits
- Add-to-cart events
- Purchase conversions
- New-to-brand customers
- ROAS measurement

**Implementation**
- Set up Amazon Attribution account
- Create attribution tags for Fire TV campaigns
- Track Amazon and non-Amazon conversions
- Analyze performance in Amazon Attribution dashboard

**Metrics Provided**
- Detail page views
- Add-to-cart rate
- Purchase rate
- Total sales
- New-to-brand sales
- ROAS
- Cross-device conversions

**Best Practices**
- Track both Amazon and off-Amazon conversions
- Segment by product category
- Compare Fire TV to other channels
- Use for e-commerce optimization

### Samsung Ads Measurement

**Capabilities**
- Website visit attribution
- Foot traffic attribution
- Brand lift studies
- Cross-device tracking

**Implementation**
- Work with Samsung Ads team
- Implement tracking pixels or work with attribution partner
- Define KPIs and measurement approach
- Receive custom reporting

**Metrics Provided**
- Impressions, reach, frequency
- Completion rate
- Website visits
- Store visits (via partners)
- Brand lift (via surveys)

### Hulu Measurement

**Capabilities**
- Website visit tracking
- Conversion tracking
- Brand lift studies
- Hulu Audience Insights

**Implementation**
- Install Hulu tracking pixel
- Define conversion events
- Set up brand lift study (for qualifying campaigns)
- Access reporting in Hulu Ads Manager

**Metrics Provided**
- Impressions, reach, frequency
- Completion rate
- Website visits
- Conversions
- Brand lift (awareness, consideration, intent)
- Audience insights (demographics, interests)

### YouTube TV / Google Measurement

**Capabilities**
- Google Analytics integration
- Conversion tracking
- Brand lift studies (free for $10K+ campaigns)
- Cross-device attribution

**Implementation**
- Link Google Ads to Google Analytics
- Set up conversion tracking
- Enable brand lift measurement
- Use Google Attribution for multi-touch analysis

**Metrics Provided**
- Impressions, reach, frequency
- View rate (completion rate)
- Website visits
- Conversions
- Brand lift (ad recall, awareness, consideration, intent)
- Cross-device conversions
- Multi-touch attribution

---

## Third-Party Attribution Platforms

### iSpot.tv

**Capabilities**
- Real-time CTV measurement
- Competitive intelligence
- Creative effectiveness analysis
- Business outcome attribution

**Use Cases**
- Track CTV campaign delivery across all platforms
- Benchmark against competitors
- Measure website visits and conversions
- Analyze creative performance

**Pricing**
- Custom pricing based on spend and features
- Typically $2,000-$10,000+ per month

### TVSquared (Innovid)

**Capabilities**
- Cross-platform TV attribution
- Real-time optimization
- Website and app attribution
- Incremental measurement

**Use Cases**
- Measure CTV + linear TV together
- Optimize campaigns in real-time
- Attribute website visits and conversions
- Calculate incremental impact

**Pricing**
- Custom pricing based on spend
- Typically percentage of media spend or flat fee

### EDO (Engagement Data Outcomes)

**Capabilities**
- Real-time engagement measurement
- Search lift attribution
- Competitive benchmarking
- Creative effectiveness

**Use Cases**
- Measure search lift from CTV ads
- Optimize creative in real-time
- Benchmark against competitors
- Predict business outcomes

**Pricing**
- Custom pricing based on spend and features

### Placed (Foursquare)

**Capabilities**
- Foot traffic attribution
- Store visit measurement
- Incremental visit calculation
- Competitive store visit analysis

**Use Cases**
- Measure store visits from CTV campaigns
- Calculate cost per visit
- Measure incremental visits vs. control
- Analyze competitive store traffic

**Pricing**
- Custom pricing based on campaign size
- Typically $5,000-$20,000+ per campaign

---

## Measurement Best Practices

### Set Clear KPIs Before Launch

**Upper-Funnel Campaigns**
- Primary: Brand awareness lift, ad recall
- Secondary: Reach, frequency, completion rate
- Tertiary: Website visits

**Mid-Funnel Campaigns**
- Primary: Consideration lift, website visits
- Secondary: Engagement rate, time on site
- Tertiary: Conversions

**Lower-Funnel Campaigns**
- Primary: Conversions, ROAS
- Secondary: Cost per acquisition
- Tertiary: Website visits, engagement

### Use Control Groups

**Geo-Based Holdouts**
- Exclude 10-20% of DMAs from campaign
- Compare business outcomes: exposed vs. control markets
- Measure incremental impact

**Audience-Based Holdouts**
- Exclude 10-20% of target audience from campaign
- Compare outcomes: exposed vs. control audiences
- More precise than geo-based

**Benefits**
- Proves incrementality
- Isolates CTV impact from other factors
- Strengthens business case for CTV investment

### Implement Multi-Touch Attribution

**Why It Matters**
- CTV rarely drives conversions alone
- Customers interact with multiple touchpoints
- Single-touch attribution undervalues CTV

**Approach**
- Track all marketing touchpoints (CTV, display, search, social, email)
- Use attribution platform to connect touchpoints
- Apply appropriate attribution model
- Optimize budget allocation based on insights

### Monitor Frequency

**Optimal Frequency**
- 3-5 impressions per household per week
- Higher frequency = diminishing returns
- Lower frequency = insufficient impact

**Frequency Management**
- Set platform-level frequency caps
- Coordinate across platforms (use household graphs)
- Monitor frequency distribution reports
- Adjust if >20% of households see 10+ impressions

### Analyze by Segment

**Segmentation Dimensions**
- Platform (Roku vs. Hulu vs. Samsung, etc.)
- Creative version
- Audience segment
- Daypart (morning, afternoon, evening, late night)
- Day of week
- Geography (DMA, state)

**Insights to Extract**
- Which platforms drive best performance?
- Which creative resonates most?
- Which audiences convert best?
- When should we advertise?
- Where should we focus geographically?

### Test and Learn

**Testing Framework**
- Test one variable at a time
- Run tests for minimum 2 weeks
- Ensure statistical significance
- Implement learnings, test next variable

**Variables to Test**
- Platform mix
- Audience targeting
- Creative approach
- Ad duration (15s vs. 30s)
- Daypart
- Frequency caps
- Attribution window

---

## Reporting Framework

### Weekly Reporting

**Delivery Metrics**
- Impressions delivered vs. goal
- Reach and frequency
- CPM
- Pacing (% of budget spent)

**Engagement Metrics**
- Completion rate by platform and creative
- QR code scans (if applicable)
- Interactive engagement

**Optimization Actions**
- Budget shifts by platform
- Creative rotations
- Targeting adjustments

### Campaign-End Reporting

**Executive Summary**
- Campaign objectives and KPIs
- Total investment and impressions
- Key results vs. benchmarks
- Recommendations for future campaigns

**Delivery Performance**
- Impressions by platform
- Reach and frequency
- CPM by platform
- Completion rate by creative

**Business Outcomes**
- Website visits (total and incremental)
- Conversions (total and incremental)
- Cost per visit, cost per conversion
- ROAS
- Brand lift (if measured)
- Store visits (if measured)

**Insights & Learnings**
- Top-performing platforms
- Top-performing creatives
- Top-performing audiences
- Optimal dayparts
- Frequency analysis

**Recommendations**
- Budget allocation for next campaign
- Creative refresh priorities
- Targeting refinements
- New platforms to test
- Measurement enhancements

---

## Common Measurement Challenges

### Challenge: Low Matching Rates
**Problem**: Only 30-50% of CTV households match to website visitors
**Solutions**:
- Use multiple attribution methods (pixel + QR + promo code)
- Work with attribution platforms with better device graphs
- Focus on incremental measurement vs. absolute numbers
- Use brand lift studies for upper-funnel campaigns

### Challenge: Long Purchase Cycles
**Problem**: Conversions happen weeks or months after ad exposure
**Solutions**:
- Extend attribution window (30-90 days)
- Track mid-funnel actions (email sign-ups, brochure downloads)
- Use brand lift to measure consideration and intent
- Implement multi-touch attribution

### Challenge: Offline Conversions
**Problem**: Sales happen in-store or via phone, not online
**Solutions**:
- Use foot traffic attribution
- Implement promo codes for in-store purchases
- Use brand lift studies
- Conduct econometric modeling (marketing mix modeling)

### Challenge: Small Sample Sizes
**Problem**: Insufficient data for statistical significance
**Solutions**:
- Increase campaign budget and duration
- Expand geographic targeting
- Use platform-provided measurement (larger sample)
- Focus on directional insights vs. precise numbers

### Challenge: Privacy Limitations
**Problem**: iOS restrictions, cookie deprecation limit tracking
**Solutions**:
- Use first-party data and customer matching
- Implement server-side tracking
- Use privacy-compliant attribution platforms
- Focus on household-level measurement (less affected by privacy changes)
