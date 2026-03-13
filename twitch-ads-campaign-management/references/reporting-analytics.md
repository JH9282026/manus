# Twitch Ads Reporting & Analytics

Comprehensive guide to measuring, analyzing, and reporting on Twitch advertising campaign performance through Amazon Ads.

---

## Amazon Ads Reporting Dashboard

### Accessing Reports

**Login:**
- Navigate to advertising.amazon.com
- Sign in with Amazon Ads account credentials
- Select Twitch campaigns from dashboard

**Report Types:**
- Campaign Manager (real-time overview)
- Custom Reports (detailed analysis)
- Scheduled Reports (automated delivery)
- API Access (programmatic data retrieval)

### Key Metrics Available

**Delivery Metrics:**
- Impressions: Total ad views
- Unique Reach: Unduplicated viewers
- Frequency: Average impressions per user
- Delivery Rate: % of planned impressions delivered

**Engagement Metrics:**
- Click-Through Rate (CTR): Clicks / Impressions
- Clicks: Total ad clicks
- Video Completion Rate (VCR): % who watched entire ad
- Quartile Completion: 25%, 50%, 75%, 100% completion rates

**Conversion Metrics:**
- Conversions: Completed desired actions
- Conversion Rate: Conversions / Clicks
- Cost Per Acquisition (CPA): Spend / Conversions
- Return on Ad Spend (ROAS): Revenue / Spend

**Cost Metrics:**
- Spend: Total campaign expenditure
- CPM (Cost Per Mille): Cost per 1,000 impressions
- CPC (Cost Per Click): Cost per click
- Daily Spend: Spend by day

**Amazon-Specific Metrics:**
- Detail Page Views (DPV): Amazon product page visits
- Branded Searches: Increase in brand search volume
- New-to-Brand (NTB) Customers: First-time buyers
- Add-to-Cart Rate: Products added to cart
- Purchase Rate: Completed purchases

**Brand Metrics:**
- Brand Lift: Measured increase in brand awareness
- Ad Recall: % who remember seeing ad
- Purchase Intent: Increase in intent to purchase
- Brand Favorability: Positive brand perception change

### Report Customization

**Dimensions:**
- Campaign
- Ad Group
- Ad Creative
- Placement
- Device
- Geographic Location
- Time Period (hourly, daily, weekly, monthly)
- Audience Segment
- Content Category

**Filters:**
- Date range
- Campaign status (active, paused, completed)
- Performance thresholds (e.g., ROAS > 3:1)
- Specific campaigns or ad groups
- Device type
- Geographic region

**Metrics Selection:**
- Choose relevant metrics for analysis
- Create custom metric combinations
- Calculate derived metrics (e.g., ROAS, CPA)
- Compare time periods

**Visualization:**
- Charts and graphs
- Trend lines
- Performance comparisons
- Heatmaps
- Export to Excel, CSV, PDF

---

## Content Transparency Reports

### Overview

**What They Are:**
- Reports showing where Twitch ad impressions were delivered
- Content type, rating, specific titles/streams
- Available through Amazon Ads API
- Helps assess contextual relevance and brand safety

**Access:**
- Amazon Ads API
- ADSP downloadable reports
- Audio and Video dimension

**Data Included:**
- Content type (game category, Just Chatting, Music, etc.)
- Content rating (if applicable)
- Specific stream titles
- Creator information (anonymized or specific, depending on settings)
- Impression volume by content

### Use Cases

**Brand Safety Verification:**
- Ensure ads appeared in brand-safe content
- Identify any problematic placements
- Adjust targeting to exclude certain content

**Contextual Relevance:**
- Analyze which content types drove best performance
- Align future targeting with high-performing content
- Understand audience context

**Future Media Planning:**
- Identify top-performing content categories
- Discover new relevant content areas
- Optimize content category targeting

**Performance Analysis:**
- Compare performance by content type
- Identify which games/categories drive conversions
- Refine targeting strategy

---

## Third-Party Tracking & Attribution

### Supported Tracking Events

**Impression Tracking:**
- Ad served and viewable
- Timestamp and placement
- Device and geographic data

**Click Tracking:**
- Ad clicked
- Click-through destination
- Time to click

**Video Quartile Tracking:**
- 25% completion
- 50% completion
- 75% completion
- 100% completion (complete)

**VAST Support:**
- VAST 2.0: Fully supported
- VAST 3.0: Fully supported
- VAST 4.0: Not supported
- VPAID: Not supported

### Implementation Requirements

**SSL Compliance:**
- All tracking pixels must use HTTPS
- No mixed content (HTTP and HTTPS)
- Third-party vendors must be SSL-compliant
- All components served securely

**Tag Specifications:**
- VAST 2.0 or 3.0 compliant
- No 4th-party tags
- No third-party redirecting
- No geo/browser targeting on third-party end
- No skip functions

**Testing:**
- Verify tags fire correctly
- Test across devices and placements
- Confirm data accuracy
- Monitor for errors

### Attribution Models

**Last-Click Attribution:**
- Credit to last ad clicked before conversion
- Simple, easy to understand
- May undervalue awareness touchpoints

**First-Click Attribution:**
- Credit to first ad interaction
- Values awareness and discovery
- May undervalue conversion drivers

**Linear Attribution:**
- Equal credit to all touchpoints
- Fair distribution
- May not reflect actual influence

**Time-Decay Attribution:**
- More credit to recent touchpoints
- Reflects recency effect
- Balances awareness and conversion

**Data-Driven Attribution (Amazon):**
- Machine learning-based
- Analyzes actual conversion paths
- Assigns credit based on influence
- Most accurate but complex

---

## Performance Benchmarking

### Industry Benchmarks

**Video Ads (Premium Video, Vertical Video):**
- VCR: 70-85% (unskippable), 40-60% (skippable)
- CTR: 0.3-0.8%
- CPM: $10-20 (standard), $25-35 (premium)
- CPC: $1.50-4.00
- Engagement Rate: 2-5%

**Display Ads:**
- CTR: 0.1-0.4%
- CPM: $6-12
- CPC: $0.80-2.50

**Interactive Ads:**
- Interaction Rate: 5-15%
- Dwell Time: 30-90 seconds
- Completion Rate: 60-80%

**Conversion Metrics:**
- Conversion Rate: 1-5% (varies by product/offer)
- ROAS: 3:1 minimum, 5:1+ excellent
- CPA: Varies by product margin and LTV

**Brand Lift:**
- Awareness Lift: 5-15%
- Ad Recall: 10-25%
- Purchase Intent Lift: 3-10%

### Competitive Benchmarking

**Compare Against:**
- Your previous campaigns
- Industry averages
- Competitor performance (if available)
- Platform benchmarks (Amazon provides)

**Key Comparisons:**
- ROAS vs. target
- CPA vs. acceptable threshold
- CTR vs. industry average
- VCR vs. platform average
- Conversion rate vs. historical performance

---

## Custom Reporting & Dashboards

### Building Custom Reports

**Define Objectives:**
- What questions need answering?
- Who is the audience for the report?
- What decisions will be made based on data?
- How frequently is reporting needed?

**Select Metrics:**
- Primary KPIs (ROAS, CPA, conversions)
- Secondary metrics (CTR, VCR, engagement)
- Supporting data (impressions, reach, frequency)

**Choose Dimensions:**
- Campaign and ad group
- Creative variation
- Audience segment
- Placement and device
- Time period

**Set Up Automation:**
- Scheduled report generation
- Automated email delivery
- Dashboard auto-refresh
- Alert triggers for anomalies

### Dashboard Best Practices

**Executive Dashboard:**
- High-level KPIs (ROAS, spend, conversions)
- Trend visualizations
- Performance vs. goals
- Key insights and recommendations

**Campaign Manager Dashboard:**
- Detailed campaign performance
- Ad group and creative breakdowns
- Optimization opportunities
- Budget pacing and delivery

**Analyst Dashboard:**
- Granular data access
- Custom metric calculations
- Segmentation analysis
- Attribution modeling

**Visualization Tips:**
- Use charts for trends
- Tables for detailed data
- Color coding for performance (green/yellow/red)
- Clear labels and legends
- Avoid clutter

---

## Reporting Cadence & Stakeholder Communication

### Daily Monitoring

**Who:** Campaign managers
**Focus:** Delivery, pacing, immediate issues
**Metrics:** Spend, impressions, CTR, any anomalies
**Action:** Adjust bids, pause underperformers, address issues

### Weekly Reporting

**Who:** Marketing team, campaign managers
**Focus:** Performance trends, optimization opportunities
**Metrics:** ROAS, CPA, CTR, VCR, conversions by segment
**Action:** Budget reallocation, creative refresh, targeting refinement

### Monthly Reporting

**Who:** Leadership, stakeholders
**Focus:** Strategic performance, ROI, insights
**Metrics:** Overall ROAS, total conversions, brand lift, key learnings
**Action:** Strategic adjustments, budget planning, campaign planning

### Campaign Wrap-Up Report

**Who:** All stakeholders
**Focus:** Comprehensive campaign analysis
**Includes:**
- Campaign objectives and results
- Performance vs. benchmarks
- Key successes and challenges
- Learnings and recommendations
- ROI analysis
- Next steps

---

## Data Export & Integration

### Export Options

**CSV Export:**
- Raw data for analysis
- Import into Excel, Google Sheets
- Custom calculations and pivots

**Excel Export:**
- Pre-formatted reports
- Charts and visualizations included
- Ready for presentation

**PDF Export:**
- Shareable reports
- Presentation-ready
- Stakeholder distribution

**API Access:**
- Programmatic data retrieval
- Integration with BI tools
- Automated reporting pipelines
- Real-time data access

### Integration with Analytics Platforms

**Google Analytics:**
- UTM parameter tracking
- Conversion funnel analysis
- Cross-channel attribution
- Audience insights

**Adobe Analytics:**
- Advanced segmentation
- Pathing analysis
- Custom metrics and dimensions

**Tableau / Power BI:**
- Advanced visualizations
- Interactive dashboards
- Cross-platform data integration
- Executive reporting

**Data Warehouses:**
- Centralized data storage
- Historical analysis
- Machine learning applications
- Advanced analytics

---

## Optimization Insights from Reporting

### Identifying Opportunities

**High ROAS Segments:**
- Increase budget allocation
- Create lookalike audiences
- Expand to similar segments
- Dedicate best creative

**Low ROAS Segments:**
- Reduce budget or pause
- Analyze why underperforming
- Test creative variations
- Refine targeting

**Creative Fatigue:**
- Declining CTR over time
- Increasing frequency
- Decreasing VCR
- Action: Refresh creative

**Placement Performance:**
- Compare ROAS by placement
- Shift budget to winners
- Adjust bids by placement
- Test new placements

**Device Insights:**
- Identify best-performing devices
- Optimize creative for top devices
- Adjust bids by device
- Improve landing pages for each device

**Time-Based Patterns:**
- Peak performance hours/days
- Implement dayparting
- Adjust budgets by time
- Align with audience behavior

### Actionable Reporting

**Include Recommendations:**
- Don't just present data
- Provide clear next steps
- Prioritize actions by impact
- Assign ownership

**Highlight Wins:**
- Celebrate successes
- Share learnings
- Build momentum
- Motivate team

**Address Challenges:**
- Identify underperformance
- Explain root causes
- Propose solutions
- Set improvement goals

**Forecast Future Performance:**
- Project results based on trends
- Model scenario outcomes
- Set realistic expectations
- Guide budget planning
