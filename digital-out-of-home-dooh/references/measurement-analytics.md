# DOOH Measurement and Analytics

## Introduction

Measurement and attribution have historically been challenges for out-of-home advertising, but Digital Out-of-Home (DOOH) has dramatically improved the ability to track performance, measure impact, and attribute business outcomes. Through advanced technologies including sensors, mobility data, device ID matching, and sophisticated analytics, DOOH now offers measurement capabilities that rival other digital channels.

This guide covers the complete spectrum of DOOH measurement and analytics, from impression tracking and audience measurement to attribution methodologies and performance optimization.

## Fundamental Metrics

### Impressions

**Definition**: The number of times an ad is displayed and potentially viewed.

**Measurement Methods**:

**Play-Based Counting**: Recording each time an ad is displayed on a screen. This is the most basic measurement—confirming the ad ran as scheduled.

**Traffic-Based Estimation**: Using traffic counts (vehicle or pedestrian) and visibility factors to estimate how many people had the opportunity to see the ad.

**Sensor-Based Measurement**: Using in-screen cameras or sensors to detect and count actual viewers, providing more accurate impression counts.

**Mobility Data**: Using anonymized mobile device location data to estimate how many devices (and thus people) were in proximity to screens when ads were displayed.

**Standards**: The OAAA and Geopath have established measurement standards for OOH impressions, including methodologies for counting and verification.

**Limitations**: Impressions indicate potential exposure but don't guarantee the ad was seen or noticed.

### Reach

**Definition**: The estimated number of unique individuals exposed to a campaign.

**Calculation**: Reach is estimated using statistical models that account for:
- Total impressions delivered
- Audience circulation patterns
- Frequency of exposure
- Duplication across placements

**Importance**: Reach indicates how many different people saw your campaign, as opposed to total impressions which may include multiple exposures to the same individuals.

**Measurement**: Mobility data providers can estimate reach by identifying unique device IDs near screens during campaign periods.

### Frequency

**Definition**: The average number of times each person in the reached audience was exposed to the campaign.

**Calculation**: Frequency = Total Impressions ÷ Reach

**Importance**: Understanding frequency helps optimize campaigns—too low and the message may not register; too high and you risk ad fatigue and wasted impressions.

**Optimal Frequency**: Research suggests 3-10 exposures is often optimal for DOOH, though this varies by objective, message complexity, and campaign duration.

**Management**: Programmatic DOOH platforms can implement frequency caps to control exposure levels.

### Dwell Time

**Definition**: The average amount of time viewers spend in front of or near a DOOH screen.

**Measurement**: Sensors or cameras can track how long individuals remain in viewing proximity.

**Importance**: Longer dwell times enable more complex messaging and higher engagement. Place-based media typically has longer dwell times than roadside billboards.

**Application**: Use dwell time data to inform creative strategy—shorter dwell times require simpler messages, longer dwell times enable more detailed content.

### Attention

**Definition**: The degree to which viewers actively look at and engage with DOOH ads.

**Measurement**: 
- **Gaze Tracking**: Computer vision technology analyzes where viewers are looking
- **Dwell Time**: Longer time near screen suggests higher attention
- **Engagement Actions**: QR code scans, mobile interactions indicate active attention

**Importance**: Attention is a stronger indicator of ad effectiveness than impressions alone.

**Emerging Standard**: Industry organizations are working to establish attention-based measurement standards for DOOH.

## Audience Measurement

### Demographic Measurement

**Methods**:

**Census Data**: Using census information about geographic areas to estimate demographics of audiences in those locations.

**Mobility Data**: Analyzing anonymized mobile device data to infer demographics based on device behavior patterns and visit history.

**Computer Vision**: In-screen cameras with AI analyze viewers to estimate age and gender (in aggregate, anonymized form).

**Survey-Based**: Conducting surveys of audiences in specific locations to understand demographics.

**Metrics**:
- Age distribution
- Gender composition
- Income levels
- Education levels
- Household composition

**Applications**: 
- Validate audience alignment with target demographics
- Optimize placement selection
- Inform creative strategy
- Compare performance across demographic segments

### Behavioral Measurement

**Methods**:

**Mobility Patterns**: Analyzing device location history to understand behaviors:
- Where people go (work, home, shopping, entertainment)
- When they go (commute times, weekend patterns)
- How often they visit locations
- What types of places they frequent

**Purchase Behavior**: Integrating with loyalty card data or credit card data (aggregated, anonymized) to understand purchase patterns.

**App Usage**: Analyzing app usage patterns to infer interests and behaviors.

**Metrics**:
- Commuter vs. resident
- Shopping frequency and preferences
- Entertainment and dining habits
- Fitness and wellness behaviors
- Travel patterns

**Applications**:
- Target audiences based on behaviors
- Understand audience mindset and context
- Optimize messaging relevance
- Measure behavioral changes after exposure

### Psychographic Measurement

**Methods**:

**Interest Inference**: Using location visit patterns to infer interests (e.g., frequent gym visits suggest fitness interest).

**Lifestyle Segmentation**: Classifying audiences into lifestyle segments based on behaviors and demographics.

**Survey Integration**: Combining DOOH exposure data with survey responses to understand attitudes and values.

**Metrics**:
- Interest categories (sports, arts, technology, etc.)
- Lifestyle segments (urban professionals, suburban families, etc.)
- Values and priorities

**Applications**:
- Refine targeting beyond demographics
- Develop more resonant messaging
- Identify high-value audience segments

## Attribution Methodologies

### Footfall Attribution

**Description**: Measuring store visits among audiences exposed to DOOH advertising.

**How It Works**:
1. Identify mobile device IDs near DOOH screens when ads are displayed (exposed group)
2. Create control group of similar devices not exposed to ads
3. Track both groups' subsequent visits to advertiser's physical locations
4. Compare visit rates between exposed and control groups
5. Calculate lift in store visits attributable to DOOH exposure

**Metrics**:
- **Visit Rate**: Percentage of exposed audience that visited store
- **Visit Lift**: Increase in visit rate vs. control group
- **Attributed Visits**: Number of visits attributable to DOOH campaign
- **Cost Per Visit**: Campaign cost divided by attributed visits
- **Visit-to-Purchase Rate**: Percentage of visitors who made purchases (if measurable)

**Requirements**:
- Mobility data provider (PlaceIQ, Cuebiq, Foursquare, Near)
- Sufficient campaign scale for statistical significance
- Defined store locations
- Attribution window (typically 7-30 days)

**Best Practices**:
- Use appropriate attribution windows (longer for considered purchases)
- Ensure control group is properly matched to exposed group
- Account for baseline visit rates
- Consider seasonality and external factors
- Validate with other measurement methods

**Limitations**:
- Requires opt-in location data
- Probabilistic matching (not 100% accurate)
- Can't measure visits by people without tracked devices
- Privacy regulations may limit availability in some regions

### Online Action Attribution

**Description**: Measuring website visits, app activity, or online searches among DOOH-exposed audiences.

**How It Works**:
1. Capture device IDs exposed to DOOH ads (via programmatic ad serving)
2. Match those device IDs with subsequent online activity
3. Compare online action rates between exposed and control groups
4. Calculate lift attributable to DOOH exposure

**Metrics**:
- **Website Visit Rate**: Percentage of exposed audience that visited website
- **Website Visit Lift**: Increase vs. control group
- **Branded Search Lift**: Increase in branded search volume
- **App Download Rate**: Percentage who downloaded app
- **Engagement Metrics**: Time on site, pages viewed, actions taken

**Requirements**:
- Device ID passback from programmatic DOOH
- Web analytics platform
- Attribution partner or platform
- Tracking pixels or SDKs

**Best Practices**:
- Extend attribution windows (14-30 days)
- Use multi-touch attribution to credit DOOH appropriately
- Segment by device type, location, and time
- Compare to other channel performance
- Track both direct and assisted conversions

**Limitations**:
- Requires programmatic buying with device ID passback
- Cross-device tracking challenges (DOOH exposure on mobile, conversion on desktop)
- Privacy considerations

### Sales Lift Measurement

**Description**: Connecting DOOH exposure to actual purchases.

**How It Works**:

**Method 1: Loyalty Card Data**
1. Match device IDs exposed to DOOH with loyalty card holders
2. Track purchases among exposed vs. control groups
3. Calculate sales lift attributable to DOOH

**Method 2: Credit Card Data**
1. Use aggregated, anonymized credit card transaction data
2. Compare purchase patterns between exposed and control groups
3. Measure sales lift

**Method 3: E-commerce Integration**
1. Track device IDs exposed to DOOH
2. Match with online purchases
3. Measure conversion and revenue lift

**Metrics**:
- **Purchase Rate**: Percentage of exposed audience that purchased
- **Purchase Lift**: Increase vs. control group
- **Revenue Per Exposed User**: Average revenue from exposed audience
- **Return on Ad Spend (ROAS)**: Revenue generated divided by campaign cost
- **Incremental Revenue**: Additional revenue attributable to DOOH

**Requirements**:
- Data partnerships (loyalty programs, credit card companies, e-commerce platforms)
- Sufficient scale for statistical significance
- Privacy-compliant data handling
- Attribution modeling

**Best Practices**:
- Use appropriate attribution windows (30-60+ days for considered purchases)
- Account for baseline purchase rates and seasonality
- Segment by customer type (new vs. existing)
- Measure both immediate and long-term impact
- Validate with incrementality testing

**Limitations**:
- Data partnerships can be expensive or difficult to establish
- Privacy regulations may limit availability
- Requires significant campaign scale
- Attribution complexity for multi-touch journeys

### Brand Lift Studies

**Description**: Survey-based measurement of changes in brand awareness, perception, consideration, or purchase intent among DOOH-exposed audiences.

**Methodology**:

**Exposed vs. Control Design**:
1. Identify audiences exposed to DOOH campaign (via mobility data or geo-fencing)
2. Create matched control group not exposed
3. Survey both groups on brand metrics
4. Compare responses to measure lift

**Pre/Post Design**:
1. Survey target audience before campaign
2. Run DOOH campaign
3. Survey same or similar audience after campaign
4. Measure changes in brand metrics

**Metrics Measured**:
- **Brand Awareness**: Aided and unaided recall of brand name
- **Ad Recall**: Memory of seeing the specific ad
- **Message Recall**: Memory of key messages or offers
- **Brand Perception**: Favorability, trust, quality perceptions
- **Consideration**: Likelihood to consider brand for purchase
- **Purchase Intent**: Stated intention to purchase
- **Brand Attributes**: Association with specific attributes (innovative, trustworthy, etc.)

**Sample Sizes**: Typically 300-500 respondents per group for statistical significance

**Timing**: Surveys typically fielded during or immediately after campaign

**Providers**: 
- Podsights (Spotify)
- Lucid
- Dynata
- Custom research firms

**Best Practices**:
- Use standardized questions for comparability
- Ensure control group is properly matched
- Field surveys at appropriate times
- Combine with behavioral metrics for complete picture
- Track brand lift over time for long-term impact assessment

**Limitations**:
- Additional cost ($5,000-$25,000+ depending on scope)
- Requires sufficient campaign scale
- Self-reported data may not perfectly predict behavior
- Doesn't directly measure sales impact

### Conversion Tracking

**Description**: Tracking specific actions taken in response to DOOH ads.

**Methods**:

**QR Codes**: Include QR codes in DOOH creative and track scans
- Measure scan rate
- Track subsequent actions (website visits, purchases, sign-ups)
- Attribute conversions to specific placements

**Custom URLs**: Use unique URLs for DOOH campaigns
- Track visits to DOOH-specific landing pages
- Measure engagement and conversion
- Use UTM parameters for detailed tracking

**Promo Codes**: Offer DOOH-specific promo codes
- Track redemptions
- Measure conversion rate
- Calculate revenue per impression

**SMS/Text Codes**: Provide text codes for audiences to engage
- Track text responses
- Measure engagement rate
- Build marketing lists

**App Downloads**: Track app downloads among exposed audiences
- Measure download rate
- Compare to control group
- Track in-app behavior

**Metrics**:
- Engagement rate (QR scans, URL visits, code usage)
- Conversion rate
- Cost per action
- Revenue per impression
- Return on ad spend

**Best Practices**:
- Make codes/URLs simple and memorable
- Provide clear instructions
- Offer incentives for action
- Track both immediate and delayed responses
- Use unique codes for different placements to compare performance

## Multi-Touch Attribution

### Attribution Models

**First-Touch Attribution**: Credits DOOH for any customer who was exposed and later converted, regardless of other touchpoints.
- **Pros**: Simple, recognizes DOOH's awareness role
- **Cons**: May overstate DOOH impact, ignores other influences

**Last-Touch Attribution**: Credits the final touchpoint before conversion.
- **Pros**: Simple, recognizes conversion driver
- **Cons**: Undervalues DOOH's awareness and consideration role

**Linear Attribution**: Distributes credit equally across all touchpoints.
- **Pros**: Fair, recognizes all contributions
- **Cons**: Doesn't account for varying touchpoint importance

**Time-Decay Attribution**: Gives more credit to touchpoints closer to conversion.
- **Pros**: Balances awareness and conversion contributions
- **Cons**: May undervalue early awareness touchpoints

**Position-Based (U-Shaped) Attribution**: Gives most credit to first and last touchpoints, less to middle.
- **Pros**: Recognizes both awareness and conversion drivers
- **Cons**: May undervalue middle-funnel touchpoints

**Algorithmic/Data-Driven Attribution**: Uses machine learning to determine optimal credit distribution based on actual conversion patterns.
- **Pros**: Most accurate, based on real data
- **Cons**: Requires significant data volume, complex to implement

**Recommendation for DOOH**: Use time-decay or algorithmic attribution to fairly value DOOH's role in customer journeys, especially for products with longer consideration periods.

### Implementation

**Requirements**:
- Tracking across all marketing channels
- Unified customer data platform or analytics system
- Device ID matching capabilities
- Attribution platform or advanced analytics

**Process**:
1. Implement consistent tracking across all channels (DOOH, display, social, search, email, etc.)
2. Capture device IDs from DOOH exposure (via programmatic)
3. Match device IDs across channels
4. Track customer journey touchpoints
5. Apply attribution model to distribute credit
6. Analyze DOOH's contribution to conversions
7. Optimize budget allocation based on attributed value

**Challenges**:
- Cross-device tracking (DOOH exposure on mobile, conversion on desktop)
- Offline conversions
- Long attribution windows
- Data integration complexity
- Privacy regulations

**Best Practices**:
- Use multiple attribution models to understand different perspectives
- Extend attribution windows for DOOH (30-60+ days)
- Combine with incrementality testing for validation
- Focus on trends and relative performance
- Integrate DOOH data with other channel data

## Marketing Mix Modeling (MMM)

**Description**: Statistical analysis that quantifies the impact of various marketing activities on sales or other business outcomes, accounting for external factors.

**How It Works**: Regression analysis examines historical data on:
- Marketing spend by channel (including DOOH)
- Sales or other business outcomes
- External variables (seasonality, competition, economy, weather, etc.)

The model determines each channel's contribution to business results, controlling for other factors.

**Advantages for DOOH**:
- Holistic view of DOOH's impact alongside other marketing
- Accounts for external factors
- Doesn't require individual-level tracking (privacy-friendly)
- Provides strategic budget allocation guidance
- Measures both short-term and long-term effects

**Requirements**:
- Significant historical data (typically 2+ years)
- Consistent tracking of marketing spend and business outcomes
- Statistical expertise or specialized firm
- Sufficient variation in DOOH spend to measure impact

**Metrics**:
- DOOH contribution to sales
- DOOH ROI or ROAS
- Optimal DOOH budget level
- Synergies with other channels
- Short-term vs. long-term impact

**Limitations**:
- Expensive and complex
- Requires extensive historical data
- Provides aggregate insights, not campaign-level detail
- May not capture short-term tactical optimizations
- Assumes historical patterns continue

**Best Practice**: Use MMM for strategic planning and budget allocation, complemented by campaign-level attribution for tactical optimization.

## Incrementality Testing

**Description**: Controlled experiments that measure the incremental impact of DOOH advertising by comparing outcomes between exposed and unexposed groups.

**Methodologies**:

**Geographic Holdout Tests**:
- Run DOOH campaigns in some markets but not others
- Compare sales or other outcomes between test and control markets
- Isolates DOOH's incremental impact

**Audience Holdout Tests**:
- Expose some audience segments to ads, withhold from others
- Compare conversion rates between exposed and control groups
- Requires programmatic capabilities for audience segmentation

**Time-Based Tests**:
- Run campaigns in specific time periods, pause in others
- Compare performance during on vs. off periods
- Controls for seasonality and trends

**Advantages**:
- Provides causal evidence of DOOH impact
- Measures true incrementality, not just correlation
- Validates attribution models
- Identifies optimal frequency and reach levels

**Requirements**:
- Sufficient scale for statistical significance
- Ability to control exposure (easier with programmatic)
- Comparable test and control groups
- Consistent measurement across groups

**Best Practices**:
- Ensure test and control groups are properly matched
- Run tests for sufficient duration (typically 4-8 weeks)
- Account for external factors and seasonality
- Use appropriate statistical methods
- Validate results with other measurement approaches

**Limitations**:
- May sacrifice short-term performance in control groups
- Complex to design and execute
- External factors can confound results
- Requires significant scale

**Recommendation**: Conduct incrementality tests periodically (annually or for major campaigns) to validate ongoing measurement approaches and optimize strategy.

## Measurement Best Practices

### Implement Comprehensive Measurement

Use multiple measurement methods in combination:
- Impression and reach tracking
- Footfall attribution
- Online action measurement
- Brand lift studies
- Sales lift analysis
- Multi-touch attribution

Triangulate across methods to develop complete understanding of DOOH impact.

### Set Appropriate KPIs

Align KPIs with campaign objectives:
- **Awareness campaigns**: Reach, frequency, brand lift
- **Consideration campaigns**: Website visits, engagement, consideration lift
- **Conversion campaigns**: Store visits, purchases, ROAS
- **Omnichannel campaigns**: Multi-touch attribution, cross-channel lift

### Extend Attribution Windows

DOOH often has delayed impact. Use longer attribution windows:
- 14-30 days for most campaigns
- 30-60+ days for considered purchases
- 60-90 days for long sales cycles

### Establish Baselines

Measure baseline performance before campaigns:
- Store visit rates
- Website traffic
- Brand awareness levels
- Sales volumes

Compare campaign-period performance to baselines to measure lift.

### Use Control Groups

Whenever possible, use control groups not exposed to DOOH to isolate incremental impact.

### Segment Analysis

Analyze performance across dimensions:
- By format (large format, transit, place-based)
- By location (markets, neighborhoods, venues)
- By time (dayparts, days of week)
- By audience segment
- By creative variant

Use insights to optimize.

### Benchmark Against Other Channels

Compare DOOH performance to other marketing channels:
- Cost per impression
- Cost per action
- Return on ad spend
- Brand lift
- Customer lifetime value

Understand DOOH's relative efficiency and effectiveness.

### Invest in Measurement Infrastructure

Allocate budget for measurement:
- Attribution platforms
- Data partnerships
- Brand lift studies
- Analytics tools
- Expertise and analysis

Typical recommendation: 5-10% of media budget for measurement.

### Validate and Triangulate

Use multiple measurement methods and compare results:
- Do different methods tell consistent stories?
- Where do they diverge and why?
- What's the range of estimated impact?

Triangulation provides more confidence than single-method measurement.

### Focus on Business Outcomes

Ultimately, measure DOOH's impact on business outcomes:
- Sales and revenue
- Customer acquisition
- Market share
- Customer lifetime value
- Brand equity

Connect DOOH metrics to business results.

## Reporting Framework

### Campaign Delivery Report

**Frequency**: Weekly during campaign

**Metrics**:
- Impressions delivered vs. goal
- Reach and frequency
- Delivery by format, location, time
- Budget pacing
- Any delivery issues

**Purpose**: Ensure campaign is delivering as planned

### Performance Report

**Frequency**: Weekly or bi-weekly during campaign

**Metrics**:
- Impressions, reach, frequency
- Engagement metrics (QR scans, website visits)
- Attribution metrics (store visits, conversions)
- Performance by segment
- Comparison to benchmarks

**Purpose**: Monitor campaign performance and identify optimization opportunities

### Optimization Report

**Frequency**: Bi-weekly or monthly during campaign

**Metrics**:
- Performance trends
- Top and bottom performers
- Optimization actions taken
- Impact of optimizations
- Recommendations for further optimization

**Purpose**: Document optimization efforts and guide ongoing improvements

### Post-Campaign Analysis

**Frequency**: After campaign completion

**Metrics**:
- Total campaign results vs. objectives
- ROI and ROAS
- Attribution analysis
- Brand lift results
- Top-performing elements
- Lessons learned
- Recommendations for future campaigns

**Purpose**: Evaluate campaign success and inform future strategy

### Executive Dashboard

**Frequency**: Monthly or quarterly

**Metrics**:
- Total DOOH investment
- Total reach and impressions
- Key business outcomes (store visits, sales, etc.)
- ROI and ROAS
- Comparison to other channels
- Strategic insights and recommendations

**Purpose**: Communicate DOOH value to leadership and secure ongoing investment

## Emerging Measurement Technologies

### Artificial Intelligence

AI is enhancing DOOH measurement:
- **Computer Vision**: More accurate audience detection and demographic analysis
- **Predictive Analytics**: Forecasting campaign performance and optimal strategies
- **Automated Optimization**: Real-time campaign adjustments based on performance
- **Attention Measurement**: Analyzing gaze patterns and attention levels

### Advanced Sensors

Next-generation sensors provide richer data:
- **3D Sensors**: More accurate people counting and tracking
- **Emotion Detection**: Analyzing facial expressions to gauge ad response
- **Gesture Recognition**: Detecting interactions and engagement

### Blockchain

Emerging use of blockchain for:
- Transparent, verifiable impression tracking
- Fraud prevention
- Automated verification and payment

### 5G Connectivity

5G enables:
- Real-time data collection and reporting
- Richer measurement data
- Faster optimization cycles

## Conclusion

DOOH measurement has evolved dramatically, transforming from estimated impressions based on traffic counts to sophisticated, multi-method attribution approaches that connect DOOH exposure to business outcomes. By implementing comprehensive measurement strategies—combining impression tracking, audience measurement, footfall attribution, online action measurement, brand lift studies, and sales lift analysis—marketers can accurately assess DOOH performance, optimize campaigns, and demonstrate clear ROI.

The key to effective DOOH measurement is using multiple methods in combination, extending attribution windows to capture delayed impact, establishing appropriate KPIs aligned with objectives, and continuously refining measurement approaches based on learnings and evolving technology. As measurement technologies continue to advance with AI, advanced sensors, and enhanced data integration, DOOH will offer increasingly precise and actionable performance insights, solidifying its position as a measurable, accountable marketing channel.