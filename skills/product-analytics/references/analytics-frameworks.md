# Product Analytics Frameworks

Comprehensive guide to selecting and implementing product analytics frameworks that align measurement with business objectives.

---

## AARRR Framework (Pirate Metrics)

Developed by Dave McClure (500 Startups), AARRR provides a funnel-based view of the customer journey from discovery to advocacy.

### Framework Structure

**1. Acquisition**
- **Definition:** How users discover your product
- **Key Questions:**
  - Which channels drive the most traffic?
  - What is the cost per visitor by channel?
  - Which sources convert best to signups?
- **Example Metrics:**
  - Unique visitors by source
  - Click-through rate (CTR) from ads
  - Organic vs. paid traffic ratio
  - Landing page conversion rate

**2. Activation**
- **Definition:** Users complete meaningful first actions
- **Key Questions:**
  - What is the "aha moment" for new users?
  - How many users reach it?
  - How long does it take?
- **Example Metrics:**
  - Signup to first action time
  - Onboarding completion rate
  - Percentage reaching activation milestone
  - Time to value (TTV)

**3. Retention**
- **Definition:** Users return and continue engaging
- **Key Questions:**
  - What percentage of users return after Day 1, 7, 30?
  - Which features drive retention?
  - How do cohorts compare?
- **Example Metrics:**
  - D1, D7, D30 retention rates
  - Monthly Active Users (MAU)
  - Churn rate
  - Feature usage frequency

**4. Revenue**
- **Definition:** Monetization and profitability
- **Key Questions:**
  - How do we generate revenue from users?
  - What is the customer lifetime value?
  - Is acquisition cost sustainable?
- **Example Metrics:**
  - Monthly Recurring Revenue (MRR)
  - Average Revenue Per User (ARPU)
  - Customer Lifetime Value (CLV)
  - CLV:CAC ratio

**5. Referral**
- **Definition:** Users recommend the product to others
- **Key Questions:**
  - How many users refer others?
  - What is the viral coefficient?
  - Which referral mechanisms work best?
- **Example Metrics:**
  - Net Promoter Score (NPS)
  - Referral rate
  - Viral coefficient (K-factor)
  - Referrals per user

### When to Use AARRR

- **Startups and growth-stage companies** optimizing for rapid growth
- **Product teams** focused on conversion optimization
- **Marketing teams** aligning product metrics with acquisition efforts
- **Revenue-focused organizations** tracking business outcomes

### AARRR Limitations

- Less emphasis on user experience quality
- May not capture nuanced feature-level insights
- Can oversimplify complex user journeys
- Limited focus on user satisfaction

---

## HEART Framework

Developed by Google, HEART measures user experience quality through five dimensions, using a Goals-Signals-Metrics process.

### Framework Structure

**1. Happiness**
- **Definition:** User attitudes and satisfaction
- **Measurement Methods:**
  - Surveys (CSAT, NPS, CES)
  - In-app feedback
  - App store ratings
  - Social sentiment analysis
- **Example Metrics:**
  - Net Promoter Score (NPS)
  - Customer Satisfaction Score (CSAT)
  - 5-star rating average
  - Sentiment score

**2. Engagement**
- **Definition:** Level of user involvement
- **Measurement Methods:**
  - Event tracking
  - Session analytics
  - Feature usage logs
- **Example Metrics:**
  - Sessions per user per week
  - Time spent in product
  - Actions per session
  - Feature adoption rate

**3. Adoption**
- **Definition:** New users or feature uptake
- **Measurement Methods:**
  - Conversion tracking
  - Feature flags and rollout analytics
  - Upgrade tracking
- **Example Metrics:**
  - New user signups
  - Feature adoption rate (% of users using new feature)
  - Upgrade conversion rate
  - Time to first use of feature

**4. Retention**
- **Definition:** Rate of returning users
- **Measurement Methods:**
  - Cohort analysis
  - Churn tracking
  - Renewal monitoring
- **Example Metrics:**
  - 7-day, 30-day retention rates
  - Churn rate
  - Renewal rate
  - Active user trends

**5. Task Success**
- **Definition:** Efficiency and effectiveness of user goals
- **Measurement Methods:**
  - Completion tracking
  - Error monitoring
  - Time-on-task measurement
- **Example Metrics:**
  - Task completion rate
  - Error rate
  - Time to complete task
  - Search success rate

### Goals-Signals-Metrics Process

HEART uses a structured approach to define what to measure:

**Goals:** High-level objectives from user perspective
- Example: "Users can quickly find relevant content"

**Signals:** User behaviors indicating goal achievement
- Example: "Users complete searches and click results"

**Metrics:** Quantifiable measurements of signals
- Example: "Search success rate: % of searches with click within 10 seconds"

### HEART Framework Example: Email Product

| Dimension | Goal | Signal | Metric |
|-----------|------|--------|--------|
| **Happiness** | Users are satisfied with email experience | Survey responses, ratings | NPS score, 4+ star rating % |
| **Engagement** | Users actively use email daily | Email opens, sends, reads | Emails sent per day, time in app |
| **Adoption** | New users start using email | Account creation, first email sent | % new users sending email in 24h |
| **Retention** | Users continue using email over time | Return visits, ongoing activity | 7-day retention rate |
| **Task Success** | Users efficiently compose and send emails | Email sent without errors | % emails sent successfully, time to send |

### When to Use HEART

- **UX-focused teams** prioritizing user experience quality
- **Product-led growth companies** where user satisfaction drives growth
- **Feature teams** measuring success of specific capabilities
- **Enterprise products** where task efficiency matters

### HEART Limitations

- Lacks explicit acquisition and revenue focus
- Can be complex to implement across all dimensions
- Requires both quantitative and qualitative data collection
- May need customization for specific product types

---

## Combining AARRR and HEART

Many teams use hybrid approaches to capture both business outcomes and user experience quality.

### Integration Strategy

**Use AARRR as the primary funnel framework:**
- Track overall business health and conversion
- Identify major drop-off points
- Align with revenue and growth goals

**Apply HEART to specific stages or features:**
- Measure activation quality with Task Success
- Track retention drivers with Engagement and Happiness
- Evaluate feature launches with full HEART analysis

### Example: SaaS Onboarding

**AARRR View:**
- Acquisition: 10,000 signups/month
- Activation: 40% complete onboarding
- Retention: 60% return Day 7

**HEART Deep Dive on Activation:**
- Happiness: CSAT score 4.2/5 for onboarding
- Engagement: Average 3 features tried during onboarding
- Adoption: 75% of users complete profile setup
- Retention: 80% of activated users return Day 7 (vs. 60% overall)
- Task Success: 85% complete onboarding without errors, avg 8 minutes

**Insight:** High task success but moderate activation rate suggests onboarding is clear but not compelling enough to drive completion.

---

## Other Analytics Frameworks

### North Star Framework

**Concept:** Single metric that best predicts long-term success

**Structure:**
- One north star metric (e.g., "Weekly Active Users")
- 3-5 input metrics that drive the north star
- Leading indicators that predict input metrics

**Example: Spotify**
- North Star: Time Spent Listening
- Inputs: New user activation, playlist creation, social sharing
- Leading Indicators: Songs added to library, follows, search queries

### Product-Market Fit (PMF) Framework

**Sean Ellis Test:**
- Survey: "How would you feel if you could no longer use this product?"
- Target: >40% respond "Very disappointed"

**Metrics Indicating PMF:**
- Retention curve flattening (not trending to zero)
- High organic growth rate
- Low churn among engaged users
- Strong NPS (>50)

### Jobs-to-be-Done (JTBD) Metrics

**Concept:** Measure how well product helps users accomplish their "jobs"

**Metrics:**
- Job completion rate
- Time to job completion
- Satisfaction with job outcome
- Frequency of job execution

---

## Framework Selection Decision Tree

**Start Here: What is your primary objective?**

1. **Optimize growth and conversion** → AARRR
2. **Improve user experience quality** → HEART
3. **Align entire org on one metric** → North Star
4. **Validate product-market fit** → PMF Framework
5. **Understand user motivations** → JTBD Metrics
6. **Comprehensive view** → AARRR + HEART hybrid

**Consider your team maturity:**
- **Early-stage startup:** Start with simplified AARRR (focus on Activation and Retention)
- **Growth-stage:** Full AARRR + selective HEART for key features
- **Enterprise/mature:** Comprehensive framework with custom additions

**Consider your product type:**
- **B2C, high-volume:** AARRR with emphasis on viral growth
- **B2B SaaS:** AARRR for funnel + HEART for retention and satisfaction
- **Marketplace:** Two-sided AARRR (supply and demand)
- **Content platform:** Engagement-focused HEART

---

## Implementing Your Chosen Framework

### Step 1: Define Your Metrics

For each framework stage/dimension:
1. List 3-5 candidate metrics
2. Evaluate based on:
   - **Actionability:** Can you influence this metric?
   - **Accessibility:** Can you measure it reliably?
   - **Alignment:** Does it reflect true success?
3. Select 1-2 primary metrics per stage

### Step 2: Set Baselines and Targets

- Measure current performance (baseline)
- Research industry benchmarks
- Set realistic improvement targets (e.g., +10% retention in 3 months)
- Define success criteria

### Step 3: Build Dashboards

- Create overview dashboard with all framework metrics
- Build detailed views for each stage/dimension
- Set up automated reporting (weekly/monthly)
- Configure alerts for significant changes

### Step 4: Establish Review Cadence

- **Daily:** Monitor critical metrics (uptime, errors)
- **Weekly:** Review growth metrics, identify anomalies
- **Monthly:** Deep dive into trends, cohort analysis
- **Quarterly:** Framework effectiveness review, adjust metrics

### Step 5: Iterate and Refine

- Test hypotheses based on metric insights
- Adjust metrics as product evolves
- Add/remove metrics based on relevance
- Continuously validate data accuracy

---

## Framework Metrics Cheat Sheet

### AARRR Quick Reference

| Stage | Primary Metric | Secondary Metrics |
|-------|----------------|-------------------|
| Acquisition | Unique visitors | Traffic by channel, CPA, conversion rate |
| Activation | % reaching aha moment | Time to value, onboarding completion |
| Retention | D7/D30 retention | MAU, churn rate, stickiness (DAU/MAU) |
| Revenue | MRR growth | ARPU, CLV, CLV:CAC ratio |
| Referral | NPS | Viral coefficient, referral rate |

### HEART Quick Reference

| Dimension | Primary Metric | Secondary Metrics |
|-----------|----------------|-------------------|
| Happiness | NPS | CSAT, app rating, sentiment score |
| Engagement | Sessions/user/week | Time in app, actions/session |
| Adoption | New user % | Feature adoption rate, upgrade rate |
| Retention | 7-day retention | Churn rate, renewal rate |
| Task Success | Completion rate | Error rate, time to complete |
