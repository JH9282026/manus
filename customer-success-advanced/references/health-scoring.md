# Customer Health Scoring

Comprehensive guide to building, implementing, and optimizing customer health scoring models for proactive risk management and expansion identification.

## Health Scoring Fundamentals

### What is Customer Health Scoring?

Customer health scoring is a quantitative framework that aggregates multiple data points to assess the overall "health" of a customer relationship. A health score predicts:
- **Retention Risk:** Likelihood of churn or non-renewal
- **Expansion Potential:** Readiness for upsell, cross-sell, or growth
- **Engagement Level:** Depth and quality of customer relationship
- **Value Realization:** Degree to which customer achieves desired outcomes

### Why Health Scoring Matters

**Proactive Risk Management:**
- Identify at-risk customers before they churn
- Prioritize intervention efforts on highest-risk accounts
- Allocate CS resources efficiently
- Improve retention rates and reduce churn

**Expansion Opportunity Identification:**
- Surface accounts ready for upsell or cross-sell
- Prioritize expansion efforts on highest-potential accounts
- Increase expansion revenue and NRR
- Optimize sales and CS collaboration

**Data-Driven Decision Making:**
- Replace gut feel with objective metrics
- Standardize account assessment across team
- Track trends and patterns over time
- Measure impact of CS interventions

**Scalability:**
- Monitor hundreds or thousands of accounts systematically
- Automate alerts and workflows based on health changes
- Enable tech-touch and low-touch CS models
- Focus human effort on highest-value activities

## Building a Health Scoring Model

### Step 1: Define Health Score Objectives

Clarify what you want your health score to predict:

**Primary Objectives:**
- **Churn Prediction:** Identify accounts likely to cancel or not renew
- **Expansion Readiness:** Surface accounts ready for growth
- **Engagement Quality:** Measure relationship strength and satisfaction
- **Value Realization:** Assess customer success and ROI achievement

**Success Criteria:**
- Health score correlates with actual renewal/churn outcomes
- Score changes trigger appropriate actions
- Team trusts and uses health scores in decision-making
- Scores improve over time as CS interventions succeed

### Step 2: Identify Health Score Components

Select metrics across multiple dimensions that predict customer health:

#### Dimension 1: Product Usage (Typically 30-40% of total score)

**Why It Matters:** Product usage is the strongest predictor of retention. Customers who actively use your product are less likely to churn.

**Key Metrics:**

**Login Frequency:**
- **What:** Number of user logins over time period
- **Measurement:** Daily Active Users (DAU), Weekly Active Users (WAU), Monthly Active Users (MAU)
- **Scoring:**
  - Green: >80% of licensed users active monthly
  - Yellow: 50-80% active
  - Red: <50% active

**Feature Adoption:**
- **What:** Breadth (number of features used) and depth (frequency of use)
- **Measurement:** Percentage of available features used, frequency of core feature usage
- **Scoring:**
  - Green: Using 70%+ of core features regularly
  - Yellow: Using 40-70% of core features
  - Red: Using <40% of core features

**Stickiness (DAU/MAU Ratio):**
- **What:** Percentage of monthly users who use product daily
- **Measurement:** DAU / MAU × 100%
- **Scoring:**
  - Green: >40% (highly sticky)
  - Yellow: 20-40% (moderate stickiness)
  - Red: <20% (low stickiness)

**Power User Development:**
- **What:** Percentage of users demonstrating advanced usage patterns
- **Measurement:** Users who have completed advanced training, use advanced features, or exceed usage thresholds
- **Scoring:**
  - Green: >20% power users
  - Yellow: 10-20% power users
  - Red: <10% power users

**Usage Trends:**
- **What:** Direction of usage over time (increasing, stable, declining)
- **Measurement:** Month-over-month or quarter-over-quarter usage change
- **Scoring:**
  - Green: Usage increasing or stable at high level
  - Yellow: Flat usage or slight decline
  - Red: Significant usage decline (>20% drop)

**Approaching Limits:**
- **What:** Proximity to plan limits (users, volume, features)
- **Measurement:** Current usage as percentage of plan limit
- **Scoring:**
  - Green: 80-100% of limit (expansion opportunity)
  - Yellow: 50-80% of limit
  - Red: <50% of limit (underutilization)

#### Dimension 2: Customer Engagement (Typically 25-35% of total score)

**Why It Matters:** Engaged customers who actively interact with your team are more likely to renew and expand.

**Key Metrics:**

**CSM Interaction Quality:**
- **What:** Frequency and quality of interactions with Customer Success Manager
- **Measurement:** Meeting attendance, responsiveness to outreach, proactive engagement
- **Scoring:**
  - Green: Attends all scheduled meetings, responds promptly, proactively engages
  - Yellow: Attends most meetings, occasionally unresponsive
  - Red: Frequently misses meetings, unresponsive, disengaged

**Support Ticket Activity:**
- **What:** Volume, severity, and resolution of support tickets
- **Measurement:** Number of tickets, critical vs. minor issues, time to resolution, satisfaction ratings
- **Scoring:**
  - Green: Low volume, minor issues, high satisfaction
  - Yellow: Moderate volume, some critical issues, mixed satisfaction
  - Red: High volume, frequent critical issues, low satisfaction, unresolved tickets

**Training and Enablement Participation:**
- **What:** Engagement with training resources and programs
- **Measurement:** Webinar attendance, certification completion, resource downloads
- **Scoring:**
  - Green: High participation, multiple certifications, active learning
  - Yellow: Moderate participation, some training completed
  - Red: Minimal participation, no certifications, low engagement

**Community and Content Engagement:**
- **What:** Participation in user community, forums, and content consumption
- **Measurement:** Forum posts, peer interactions, content views, event attendance
- **Scoring:**
  - Green: Active community member, regular content consumption
  - Yellow: Occasional community participation
  - Red: No community engagement, minimal content consumption

**Executive Sponsorship:**
- **What:** Engagement and advocacy from customer leadership
- **Measurement:** Executive participation in QBRs, strategic planning, advocacy activities
- **Scoring:**
  - Green: Active executive sponsor, participates in strategic discussions
  - Yellow: Executive aware but not actively engaged
  - Red: No executive sponsorship or awareness

#### Dimension 3: Business Outcomes (Typically 15-25% of total score)

**Why It Matters:** Customers who achieve their business goals and realize ROI are most likely to renew and expand.

**Key Metrics:**

**Goal Achievement:**
- **What:** Progress toward stated business objectives and KPIs
- **Measurement:** Percentage of goals achieved, milestone completion
- **Scoring:**
  - Green: Achieving or exceeding stated goals
  - Yellow: Making progress but behind targets
  - Red: Not achieving goals, significant gaps

**ROI Realization:**
- **What:** Documented return on investment and value delivered
- **Measurement:** ROI calculations, value assessments, business case validation
- **Scoring:**
  - Green: Documented positive ROI, clear value realization
  - Yellow: Some value realized, ROI unclear or marginal
  - Red: No documented ROI, value questioned

**Time-to-Value:**
- **What:** Speed of achieving first meaningful outcome
- **Measurement:** Days from onboarding to first value milestone
- **Scoring:**
  - Green: Achieved first value within target timeframe
  - Yellow: Delayed but eventually achieved
  - Red: Significantly delayed or not yet achieved

**Business Impact:**
- **What:** Measurable business improvements attributed to product
- **Measurement:** Revenue increase, cost reduction, efficiency gains, risk mitigation
- **Scoring:**
  - Green: Significant, measurable business impact
  - Yellow: Some impact, not fully quantified
  - Red: Minimal or no measurable impact

#### Dimension 4: Sentiment and Satisfaction (Typically 10-20% of total score)

**Why It Matters:** Customer sentiment and satisfaction are leading indicators of retention and advocacy.

**Key Metrics:**

**Net Promoter Score (NPS):**
- **What:** Likelihood to recommend product to others
- **Measurement:** 0-10 scale, categorized as Promoters (9-10), Passives (7-8), Detractors (0-6)
- **Scoring:**
  - Green: Promoter (9-10)
  - Yellow: Passive (7-8)
  - Red: Detractor (0-6)

**Customer Satisfaction (CSAT):**
- **What:** Satisfaction with product, service, or specific interactions
- **Measurement:** 1-5 or 1-7 scale, percentage satisfied
- **Scoring:**
  - Green: Highly satisfied (4-5 on 5-point scale)
  - Yellow: Moderately satisfied (3)
  - Red: Dissatisfied (1-2)

**Sentiment Analysis:**
- **What:** Tone and sentiment in customer communications
- **Measurement:** AI-powered sentiment analysis of emails, tickets, calls
- **Scoring:**
  - Green: Consistently positive sentiment
  - Yellow: Neutral or mixed sentiment
  - Red: Negative sentiment, frustration, complaints

**Renewal Intent:**
- **What:** Expressed intention to renew contract
- **Measurement:** Direct questions about renewal plans, commitment signals
- **Scoring:**
  - Green: Strong commitment to renew, multi-year interest
  - Yellow: Likely to renew but uncertain
  - Red: Unlikely to renew, actively evaluating alternatives

**Advocacy Indicators:**
- **What:** Willingness to provide references, testimonials, referrals
- **Measurement:** Reference requests accepted, case study participation, referrals provided
- **Scoring:**
  - Green: Active advocate, provides references and referrals
  - Yellow: Willing to help occasionally
  - Red: Unwilling to advocate or provide references

### Step 3: Assign Weights to Components

Determine relative importance of each dimension and metric:

**Example Weighting:**

**Product Usage (40%):**
- Login Frequency: 10%
- Feature Adoption: 10%
- Stickiness: 8%
- Power Users: 7%
- Usage Trends: 5%

**Customer Engagement (30%):**
- CSM Interaction: 10%
- Support Activity: 8%
- Training Participation: 7%
- Community Engagement: 5%

**Business Outcomes (20%):**
- Goal Achievement: 8%
- ROI Realization: 7%
- Business Impact: 5%

**Sentiment (10%):**
- NPS: 5%
- CSAT: 3%
- Sentiment Analysis: 2%

**Total: 100%**

**Weighting Considerations:**
- **Product-Led Growth (PLG):** Weight usage more heavily (50-60%)
- **High-Touch Enterprise:** Weight engagement and outcomes more heavily (30-40% each)
- **Early-Stage Customers:** Weight onboarding and time-to-value more heavily
- **Mature Customers:** Weight expansion signals and advocacy more heavily

### Step 4: Define Scoring Scale and Thresholds

Establish scoring methodology and health categories:

**Scoring Scale:**

**100-Point Scale (Recommended):**
- **Green (Healthy): 80-100 points**
  - Low churn risk
  - High expansion potential
  - Strong relationship and satisfaction
  - Action: Pursue expansion, request advocacy

- **Yellow (At-Risk): 60-79 points**
  - Moderate churn risk
  - Requires intervention
  - Some concerns or gaps
  - Action: Increase engagement, address concerns, improve adoption

- **Red (Critical): 0-59 points**
  - High churn risk
  - Urgent intervention required
  - Significant issues or disengagement
  - Action: Executive escalation, recovery plan, save team engagement

**Alternative: Color-Only Scale:**
- Simpler but less granular
- Green, Yellow, Red based on composite assessment
- Easier to communicate but harder to track trends

**Threshold Calibration:**
- Analyze historical data to validate thresholds
- Ensure thresholds correlate with actual churn/renewal outcomes
- Adjust thresholds based on segment (enterprise vs. SMB)
- Regularly review and refine based on performance

### Step 5: Implement and Automate

Build health scoring into your CS technology stack:

**Data Integration:**
- Connect product analytics (usage data)
- Integrate CRM (engagement data)
- Link support system (ticket data)
- Import survey results (sentiment data)
- Aggregate financial data (ARR, expansion, renewals)

**Calculation and Updates:**
- Automate health score calculation
- Update scores daily or weekly
- Track score changes and trends
- Maintain historical scores for analysis

**Alerts and Workflows:**
- Trigger alerts when scores drop below thresholds
- Notify CSMs of at-risk accounts
- Escalate critical accounts to leadership
- Automate intervention workflows

**Visualization and Reporting:**
- Display health scores in CS platform and CRM
- Create dashboards for team and leadership
- Track health score distribution and trends
- Report on correlation with retention and expansion

## Using Health Scores Effectively

### Proactive Risk Management

**Yellow Account Intervention:**

**Immediate Actions (Within 1 Week):**
- Review account details and recent activity
- Identify specific factors driving yellow score
- Reach out to primary contact to check in
- Schedule meeting to discuss concerns

**Intervention Strategies:**
- **Low Usage:** Provide additional training, identify adoption barriers, offer implementation support
- **Low Engagement:** Increase touchpoint frequency, escalate to executive sponsor, offer value-add services
- **Support Issues:** Prioritize ticket resolution, conduct root cause analysis, provide workarounds
- **Sentiment Concerns:** Conduct satisfaction survey, address specific complaints, demonstrate commitment

**Success Criteria:**
- Health score improves to green within 30-60 days
- Specific issues resolved
- Customer engagement and satisfaction increase

**Red Account Recovery:**

**Immediate Actions (Within 24-48 Hours):**
- Notify CS leadership and account team
- Conduct emergency account review
- Develop recovery plan with clear actions and timeline
- Schedule urgent meeting with customer leadership

**Recovery Strategies:**
- **Executive Escalation:** Engage C-level from vendor side
- **Dedicated Resources:** Assign save team or additional support
- **Concessions:** Offer discounts, credits, or additional services
- **Root Cause Resolution:** Address fundamental issues causing dissatisfaction
- **Quick Wins:** Deliver immediate value to rebuild trust

**Success Criteria:**
- Health score improves to yellow within 30 days, green within 90 days
- Customer commits to renewal or extended contract
- Relationship rebuilt and trust restored

### Expansion Opportunity Identification

**Green Account Expansion:**

**Expansion Signals:**
- High health score (85-100)
- Approaching plan limits (80%+ of users, volume, features)
- High engagement and satisfaction
- Expressed interest in additional capabilities
- Organizational growth or new initiatives

**Expansion Strategies:**
- **Upsell:** Upgrade to higher tier with advanced features
- **Cross-Sell:** Introduce complementary products
- **Seat Expansion:** Add more users or licenses
- **Professional Services:** Offer implementation, training, or consulting

**Expansion Process:**
1. Identify expansion opportunity based on health score and signals
2. Validate opportunity with CSM and account team
3. Develop expansion proposal and business case
4. Present expansion opportunity in QBR or dedicated meeting
5. Collaborate with sales on expansion deal
6. Track expansion revenue and impact on health score

### Health Score Reporting and Analysis

**Team Dashboards:**
- **CSM View:** List of assigned accounts with health scores, sorted by risk
- **At-Risk Report:** All yellow and red accounts requiring intervention
- **Expansion Pipeline:** Green accounts with expansion signals
- **Trend Analysis:** Health score changes over time

**Executive Dashboards:**
- **Health Score Distribution:** Percentage of accounts in green, yellow, red
- **Health Score Trends:** Movement between categories over time
- **Churn Correlation:** Relationship between health scores and actual churn
- **Expansion Correlation:** Relationship between health scores and expansion revenue

**Analysis and Optimization:**
- **Predictive Accuracy:** Do health scores accurately predict churn and expansion?
- **Component Analysis:** Which metrics are most predictive?
- **Segment Differences:** Do different segments require different models?
- **Intervention Effectiveness:** Do interventions improve health scores and outcomes?

## Advanced Health Scoring Techniques

### Predictive Health Scoring with Machine Learning

**Traditional vs. Predictive Scoring:**

**Traditional (Rule-Based):**
- Manually defined weights and thresholds
- Static calculation based on current data
- Requires periodic manual adjustment
- Transparent and explainable

**Predictive (ML-Based):**
- Algorithmically determined weights based on historical data
- Learns patterns and correlations automatically
- Continuously improves with more data
- More accurate but less transparent

**Building Predictive Models:**

1. **Gather Historical Data:**
   - Customer attributes and behaviors
   - Health score components over time
   - Actual outcomes (churned, renewed, expanded)

2. **Feature Engineering:**
   - Create derived metrics (trends, ratios, changes)
   - Identify leading indicators
   - Test feature importance

3. **Model Training:**
   - Use classification algorithms (logistic regression, random forest, gradient boosting)
   - Train on historical data with known outcomes
   - Validate on holdout dataset

4. **Model Deployment:**
   - Integrate model into CS platform
   - Generate predictions for current customers
   - Update predictions regularly

5. **Model Monitoring:**
   - Track prediction accuracy
   - Retrain model periodically with new data
   - Adjust features and parameters as needed

**Benefits:**
- Higher predictive accuracy
- Identifies non-obvious patterns
- Adapts to changing customer behaviors
- Scales to large customer bases

**Challenges:**
- Requires significant historical data
- Less transparent and harder to explain
- Needs data science expertise
- Risk of overfitting or bias

### Segment-Specific Health Scores

Different customer segments may require different health scoring models:

**Enterprise vs. SMB:**
- **Enterprise:** Weight engagement and outcomes more heavily (relationship-driven)
- **SMB:** Weight usage and self-service more heavily (product-driven)

**New vs. Mature Customers:**
- **New (<90 days):** Weight onboarding progress and time-to-value
- **Mature (>1 year):** Weight expansion signals and advocacy

**Product Tier:**
- **Basic Tier:** Focus on core feature adoption
- **Advanced Tier:** Focus on advanced feature usage and ROI

**Industry Vertical:**
- Different industries may have different usage patterns and success criteria
- Customize metrics and thresholds by vertical

### Leading vs. Lagging Indicators

**Lagging Indicators (Outcome Metrics):**
- Churn, renewal, expansion (what already happened)
- Useful for reporting but not for prevention
- Examples: Renewal rate, NRR, churn rate

**Leading Indicators (Predictive Metrics):**
- Early warning signs of future outcomes
- Enable proactive intervention
- Examples: Usage decline, engagement drop, sentiment shift

**Health Score Focus:**
- Prioritize leading indicators in health score
- Use lagging indicators to validate health score accuracy
- Balance real-time signals with historical trends

## Common Health Scoring Mistakes

**Mistake 1: Too Many Metrics**
- **Problem:** Overly complex models with 20+ metrics are hard to manage and explain
- **Solution:** Focus on 5-10 most predictive metrics, keep it simple

**Mistake 2: Equal Weighting**
- **Problem:** Not all metrics are equally predictive
- **Solution:** Weight metrics based on correlation with actual outcomes

**Mistake 3: Ignoring Data Quality**
- **Problem:** Garbage in, garbage out; inaccurate data leads to inaccurate scores
- **Solution:** Invest in data quality, validation, and governance

**Mistake 4: Set-It-and-Forget-It**
- **Problem:** Health scores become stale and less accurate over time
- **Solution:** Regularly review, validate, and refine scoring model

**Mistake 5: No Action on Scores**
- **Problem:** Tracking health scores without using them to drive action
- **Solution:** Build workflows, playbooks, and accountability around health scores

**Mistake 6: Lack of Transparency**
- **Problem:** Team doesn't understand how scores are calculated
- **Solution:** Document methodology, train team, make scoring logic visible

**Mistake 7: One-Size-Fits-All**
- **Problem:** Same health score model for all customer segments
- **Solution:** Segment-specific models or adjustments for different customer types
