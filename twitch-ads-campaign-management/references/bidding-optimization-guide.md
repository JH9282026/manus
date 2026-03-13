# Twitch Ads Bidding & Optimization Guide

Comprehensive strategies for bidding, budget management, and campaign optimization on Twitch through Amazon DSP.

---

## Bidding Strategy Framework

### Fixed Bids

**How It Works:**
- Set a default bid amount
- Bid remains constant regardless of conversion likelihood
- No automatic adjustments by Amazon's algorithm
- Predictable spend and impression delivery

**When to Use:**
- New product launches (visibility priority)
- Brand awareness campaigns (reach over efficiency)
- Budget certainty required
- Testing baseline performance
- Limited historical data available

**Advantages:**
- Predictable budget management
- Consistent impression delivery
- Simple to understand and manage
- Good for awareness goals
- Stable CPM costs

**Disadvantages:**
- May overpay for low-intent impressions
- Fewer conversions per dollar spent
- Misses optimization opportunities
- Less efficient for performance campaigns
- No algorithmic learning

**Recommended Bid Range:**
- Start with $10-15 CPM for standard inventory
- $20-30 CPM for premium placements (First Impression Takeover)
- $5-10 CPM for testing/broad reach

**Optimization Tips:**
- Monitor CPM vs. industry benchmarks
- Adjust bids weekly based on delivery pace
- Increase bids if under-delivering impressions
- Decrease bids if overspending without results

---

### Dynamic Bidding – Down Only

**How It Works:**
- Amazon automatically lowers bids up to 100% when conversion unlikely
- Never increases bids above your set amount
- Algorithm analyzes real-time conversion probability
- Reduces wasted spend on low-intent impressions

**When to Use:**
- First campaigns on Twitch (recommended starting point)
- Testing new audiences or creatives
- Budget-conscious campaigns
- Learning phase (first 2-4 weeks)
- Optimizing for efficiency over volume

**Advantages:**
- Cost-effective, reduces wasted spend
- Better conversion rates per dollar
- Lower risk than "Up and Down"
- Recommended for beginners
- Builds algorithmic learning

**Disadvantages:**
- Potentially lower impression volume
- May miss some conversion opportunities
- Slower delivery pace
- Less aggressive reach

**Recommended Bid Range:**
- Start with $12-18 CPM (allows room for algorithm to reduce)
- Monitor actual CPM (will be lower than bid)
- Adjust base bid if under-delivering

**Optimization Tips:**
- Run for minimum 2 weeks before evaluating
- Compare actual CPM to bid amount (should be 20-40% lower)
- If delivery too slow, increase base bid by 10-20%
- Monitor conversion rate improvement over time
- Transition to "Up and Down" once performance stabilizes

**Amazon Recommendation:**
- Start with "Down Only" for 2 weeks
- Gather performance data
- Switch to "Up and Down" if campaign performing well
- Keep "Down Only" if budget constraints critical

---

### Dynamic Bidding – Up and Down

**How It Works:**
- Amazon adjusts bids up or down by up to 100%
- Increases bids for high-probability conversion impressions
- Decreases bids for low-probability impressions
- Real-time algorithmic optimization
- Most aggressive bidding strategy

**When to Use:**
- Proven campaigns with good performance history
- Maximizing conversions (not efficiency)
- Sufficient budget flexibility
- After 2+ weeks of "Down Only" success
- Scaling winning campaigns
- Managing excess inventory

**Advantages:**
- Maximizes conversion potential
- Captures high-intent moments
- Scales successful campaigns
- Leverages Amazon's ML algorithms
- Can significantly boost results

**Disadvantages:**
- Less predictable budget spend
- Higher average CPM
- Can overspend quickly
- Requires budget flexibility
- May inflate costs without proportional returns

**Recommended Bid Range:**
- Start with $15-25 CPM (algorithm will adjust up to $50 CPM)
- Monitor actual CPM closely (can be 50-100% higher than bid)
- Set daily budget caps to control spend

**Optimization Tips:**
- Monitor daily spend closely (can accelerate quickly)
- Set maximum daily budget limits
- Compare ROAS to "Down Only" performance
- Reduce base bid if CPM too high without ROAS improvement
- Use for proven winners, not testing

**Risk Management:**
- Start with 50% of budget on "Up and Down", 50% on "Down Only"
- Gradually shift more budget as performance proves out
- Set campaign lifetime budget caps
- Monitor hourly during first 24-48 hours
- Have pause triggers ready (e.g., CPA exceeds $X)

---

### Rule-Based Bidding (Advanced)

**How It Works:**
- Set specific ROAS (Return on Ad Spend) targets
- Create custom "if/then" rules for bid adjustments
- Amazon adjusts bids to stay within ROAS target
- Highly granular control over performance
- Requires significant data and expertise

**When to Use:**
- Experienced advertisers with clear ROAS goals
- Mature campaigns with 4+ weeks of data
- Complex product catalogs with varying margins
- Performance-driven campaigns (not awareness)
- Multiple campaign objectives requiring different strategies

**Example Rules:**

**Rule 1: ROAS Target**
- IF campaign ROAS < 3:1
- THEN decrease bids by 20%
- ELSE IF campaign ROAS > 5:1
- THEN increase bids by 30%

**Rule 2: Time-Based**
- IF time is 6pm-10pm (peak hours)
- THEN increase bids by 40%
- ELSE IF time is 2am-6am (low traffic)
- THEN decrease bids by 50%

**Rule 3: Device-Based**
- IF device is mobile
- AND conversion rate > 2%
- THEN increase bids by 25%

**Rule 4: Audience-Based**
- IF audience is "Recent Gaming Purchasers"
- THEN increase bids by 50%
- ELSE IF audience is "Broad Reach"
- THEN decrease bids by 30%

**Setup Requirements:**
- Minimum 1,000 impressions per rule segment
- At least 50 conversions for ROAS-based rules
- 4+ weeks of campaign data
- Clear performance benchmarks
- Dedicated monitoring and adjustment

**Advantages:**
- Precise control over performance
- Automated optimization at scale
- Aligns spend with business goals
- Handles complex scenarios
- Maximizes efficiency for experienced advertisers

**Disadvantages:**
- Complex to set up and manage
- Requires significant data volume
- Can over-optimize and limit reach
- Needs ongoing monitoring and adjustment
- Steep learning curve

**Optimization Tips:**
- Start with simple rules (1-2 conditions)
- Add complexity gradually as data accumulates
- Review rule performance weekly
- Adjust ROAS targets based on business goals
- Don't over-constrain (allow algorithm some flexibility)

---

## Budget Management Strategies

### Budget Sizing

**Minimum Recommended Budgets:**

**Testing Phase:**
- $2,000-5,000 total budget
- Run for 2-4 weeks
- Test 2-3 audience segments
- Test 2-3 creative variations
- Gather baseline performance data

**Optimization Phase:**
- $5,000-15,000 total budget
- Run for 4-8 weeks
- Focus on proven segments
- Refine targeting and creative
- Build algorithmic learning

**Scaling Phase:**
- $15,000+ total budget
- Ongoing campaigns
- Expand to lookalike audiences
- Increase frequency and reach
- Maximize proven strategies

**Managed Service (Twitch Sales Team):**
- $35,000-50,000 minimum (varies by region)
- Access to premium placements
- White-glove support
- Custom influencer partnerships

### Budget Allocation Framework

**60/30/10 Rule:**

**60% - Proven Winners**
- Allocate to best-performing campaigns
- Highest ROAS segments
- Winning creative variations
- Established audience segments
- Focus: Maximize returns

**30% - Optimization**
- Test new audience segments
- Try new ad formats
- Experiment with messaging
- Explore new content categories
- Focus: Find new winners

**10% - Innovation**
- Test emerging formats (Vertical Video)
- Try influencer partnerships
- Experiment with interactive ads
- Explore new targeting strategies
- Focus: Future opportunities

**Rebalance Monthly:**
- Move successful tests from 30% to 60%
- Promote innovations from 10% to 30%
- Cut underperformers from all buckets
- Maintain ratio for sustainable growth

### Pacing Strategies

**Even Pacing (Standard)**
- Spreads budget evenly across campaign duration
- Prevents early budget depletion
- Consistent daily delivery
- Best for: Most campaigns, steady awareness

**Accelerated Pacing**
- Spends budget as quickly as possible
- Maximizes immediate reach
- Risk of early depletion
- Best for: Time-sensitive campaigns, product launches, events

**Dayparting (Time-Based)**
- Concentrates spend during specific hours/days
- Aligns with peak viewing times
- More efficient use of budget
- Best for: Performance campaigns, known high-conversion windows

**Recommended Dayparting for Twitch:**
- **Peak Hours:** 6pm-12am (40% of budget)
- **Secondary Hours:** 12pm-6pm (30% of budget)
- **Off-Peak:** 6am-12pm (20% of budget)
- **Late Night:** 12am-6am (10% of budget)

**Weekend vs. Weekday:**
- **Weekends:** 40% of weekly budget (longer sessions, tournaments)
- **Weekdays:** 60% of weekly budget (consistent traffic)

### Budget Monitoring & Adjustment

**Daily Monitoring (First Week):**
- Check spend vs. budget pace
- Monitor CPM and CPC trends
- Track conversion rate
- Identify delivery issues
- Adjust bids if under/over-delivering

**Weekly Monitoring (Ongoing):**
- Review ROAS by campaign
- Analyze CPA trends
- Compare segment performance
- Reallocate budget to winners
- Pause underperformers

**Monthly Monitoring:**
- Comprehensive performance review
- Budget reallocation (60/30/10)
- Strategic adjustments
- Quarterly planning
- Competitive analysis

**Adjustment Triggers:**

**Increase Budget When:**
- ROAS exceeds target by 20%+
- Impression share limited by budget
- High-converting segments under-delivering
- Seasonal opportunity (tournaments, holidays)

**Decrease Budget When:**
- ROAS below target for 2+ weeks
- CPA exceeds acceptable threshold
- Low engagement/conversion rates
- Better opportunities identified elsewhere

**Pause Campaign When:**
- ROAS below 1:1 for 2+ weeks
- CPA 50%+ above target with no improvement
- Creative fatigue (declining CTR/VCR)
- Budget needed for higher-priority campaigns

---

## Placement Bidding Strategies

### Bid Adjustments by Placement

**Premium Video (Pre-Roll/Mid-Roll):**
- Base bid: $15-20 CPM
- High visibility, unskippable
- Strong completion rates (80%+)
- Best for: Brand awareness, product demos

**First Impression Takeover:**
- Base bid: $25-35 CPM (premium pricing)
- Exclusive, high impact
- First view of the day
- Best for: Major launches, exclusive announcements

**Vertical Video:**
- Base bid: $12-18 CPM
- Mobile-optimized
- Skippable on mobile
- Best for: Mobile campaigns, younger demographics

**Stream Display Ads:**
- Base bid: $8-12 CPM
- Integrated into stream experience
- Clickable, direct response
- Best for: Website traffic, conversions

**Mid-Feed Ads:**
- Base bid: $10-15 CPM
- Mobile-only, full-screen
- Native feed integration
- Best for: Mobile app installs, mobile commerce

**Super Leaderboard / Medium Rectangle:**
- Base bid: $6-10 CPM
- Standard display inventory
- Lower engagement than video
- Best for: Retargeting, supplemental reach

### Device Bid Adjustments

**Desktop/PC:**
- Baseline (100%)
- Longer sessions, higher engagement
- Chat participation
- Best for: Detailed messaging, complex CTAs

**Mobile:**
- +20% to +40% (if mobile performance strong)
- Shorter sessions, frequent checks
- Vertical video performs well
- Best for: Simple CTAs, app installs

**Tablet:**
- +10% to +20%
- Medium sessions
- Hybrid behavior
- Best for: Visual storytelling

**Console:**
- -20% to -40% (limited interactivity)
- No clickable ads
- Awareness only
- Best for: Brand awareness, video storytelling

**Streaming TV:**
- -10% to +10%
- Big screen, lean-back
- Family/group viewing
- Best for: Brand awareness, high-impact video

---

## Performance Optimization Tactics

### Creative Optimization

**A/B Testing Framework:**

**Test 1: Video Length**
- Variation A: 15-second video
- Variation B: 30-second video
- Metric: Video Completion Rate (VCR)
- Winner: Higher VCR with acceptable CTR

**Test 2: Messaging Approach**
- Variation A: Humorous, self-aware
- Variation B: Informative, feature-focused
- Metric: CTR and conversion rate
- Winner: Higher conversion rate

**Test 3: CTA Placement**
- Variation A: CTA at beginning and end
- Variation B: CTA at end only
- Metric: Click-through rate
- Winner: Higher CTR

**Test 4: Visual Style**
- Variation A: UGC-style, authentic
- Variation B: Polished, professional
- Metric: Engagement rate, brand lift
- Winner: Better brand perception + engagement

**Creative Refresh Schedule:**
- Monitor CTR weekly
- Refresh creative when CTR drops 20%+ from baseline
- Typical refresh cycle: Every 3-4 weeks
- Maintain 2-3 active creative variations
- Retire underperformers, introduce new tests

### Frequency Capping

**Recommended Frequency Caps:**

**Awareness Campaigns:**
- 3-5 impressions per user per day
- 15-20 impressions per user per week
- Goal: Reach without annoyance

**Consideration Campaigns:**
- 2-3 impressions per user per day
- 10-15 impressions per user per week
- Goal: Reinforce message, drive consideration

**Conversion Campaigns:**
- 1-2 impressions per user per day
- 5-10 impressions per user per week
- Goal: Timely reminders without fatigue

**Retargeting Campaigns:**
- 1 impression per user per day
- 3-5 impressions per user per week
- Goal: Re-engage without overwhelming

**Monitoring Frequency Fatigue:**
- Track CTR by frequency bucket (1st, 2nd, 3rd+ impression)
- If CTR drops 50%+ at 3rd impression, reduce frequency cap
- Monitor negative feedback/ad blocking rates
- Adjust caps based on campaign performance

### Audience Optimization

**Segment Performance Analysis:**

**Weekly Review:**
1. Export performance data by audience segment
2. Calculate ROAS, CPA, CTR for each segment
3. Rank segments by ROAS (high to low)
4. Identify top 20% and bottom 20%

**Optimization Actions:**
- **Top 20% (Winners):** Increase budget by 30-50%, create lookalikes, expand reach
- **Middle 60% (Moderate):** Maintain budget, test creative variations, refine targeting
- **Bottom 20% (Underperformers):** Reduce budget by 50% or pause, analyze why failing

**Lookalike Expansion:**
- Create 1% lookalike from top 20% converters
- Test with 20% of budget
- If ROAS within 80% of seed audience, scale
- Expand to 5% lookalike for broader reach

**Exclusion List Management:**
- Exclude converters from acquisition campaigns (add to retention campaigns)
- Exclude bottom 20% performers after 2 weeks
- Exclude irrelevant content categories
- Update exclusion lists weekly

---

## Advanced Optimization Strategies

### Sequential Messaging

**Campaign Structure:**

**Phase 1: Awareness (Days 1-7)**
- Objective: Introduce brand/product
- Creative: Brand story, product overview
- Frequency: 3-5 impressions per user
- Audience: Broad reach, cold audiences

**Phase 2: Consideration (Days 8-14)**
- Objective: Highlight benefits, features
- Creative: Product demonstrations, testimonials
- Frequency: 2-3 impressions per user
- Audience: Users who viewed Phase 1 ads

**Phase 3: Conversion (Days 15-21)**
- Objective: Drive action
- Creative: Strong CTA, limited-time offers
- Frequency: 1-2 impressions per user
- Audience: Users who engaged with Phase 2

**Phase 4: Retargeting (Days 22+)**
- Objective: Re-engage non-converters
- Creative: Reminder ads, new angles
- Frequency: 1 impression per user per day
- Audience: Users who didn't convert in Phase 3

### Event-Based Optimization

**Esports Tournament Alignment:**

**Pre-Tournament (1-2 weeks before):**
- Increase bids by 20-30%
- Target fans of participating teams/games
- Awareness-focused creative
- Build anticipation

**During Tournament:**
- Increase bids by 40-60%
- Real-time messaging ("Watch the finals!")
- High-impact placements (First Impression Takeover)
- Maximize reach during peak viewership

**Post-Tournament (1 week after):**
- Maintain elevated bids (+20%)
- Retarget tournament viewers
- Conversion-focused creative
- Capitalize on engagement momentum

**Game Launch Alignment:**

**Pre-Launch (2-4 weeks before):**
- Target fans of similar games
- Build awareness and anticipation
- Teaser creative

**Launch Week:**
- Maximum budget allocation
- Target game category viewers
- Gameplay demos, reviews
- Drive immediate action

**Post-Launch (2-4 weeks after):**
- Retarget engaged users
- Highlight positive reviews, community feedback
- Conversion optimization

### Competitive Conquest

**Strategy:**
- Target viewers of competitor games/products
- Highlight differentiators
- Offer switching incentives

**Targeting:**
- Viewers of competitor game streams
- Amazon purchasers of competitor products
- Followers of competitor creators

**Messaging:**
- Comparative benefits (without direct attacks)
- "If you like [Competitor], you'll love [Your Product]"
- Exclusive offers for switchers

**Caution:**
- Ensure compliance with advertising policies
- Avoid trademark infringement
- Focus on benefits, not disparagement

---

## Troubleshooting Common Issues

### Low Impression Delivery

**Possible Causes:**
- Bids too low
- Audience too narrow
- Budget too small
- Frequency caps too restrictive

**Solutions:**
- Increase bids by 20-30%
- Broaden audience targeting
- Increase daily budget
- Relax frequency caps
- Check campaign status (active, approved)

### High CPM, Low Conversions

**Possible Causes:**
- Bidding "Up and Down" too aggressively
- Targeting misaligned with product
- Creative not resonating
- Landing page issues

**Solutions:**
- Switch to "Down Only" bidding
- Refine audience targeting
- Test new creative variations
- Optimize landing page experience
- Review conversion tracking setup

### High CTR, Low Conversion Rate

**Possible Causes:**
- Misleading ad creative
- Landing page disconnect
- Pricing/offer issues
- Technical conversion tracking problems

**Solutions:**
- Ensure ad and landing page alignment
- Simplify conversion process
- Test different offers
- Verify conversion pixel firing
- Analyze drop-off points in funnel

### Ad Fatigue (Declining CTR)

**Possible Causes:**
- Same creative shown too frequently
- Audience saturation
- Seasonal relevance decline

**Solutions:**
- Refresh creative (new visuals, messaging)
- Expand to new audience segments
- Reduce frequency caps
- Pause campaign temporarily, relaunch with new creative
- Rotate multiple creative variations

### Budget Pacing Issues

**Spending Too Fast:**
- Reduce bids by 15-20%
- Switch from accelerated to even pacing
- Implement stricter frequency caps
- Reduce daily budget

**Spending Too Slow:**
- Increase bids by 20-30%
- Broaden targeting
- Increase frequency caps
- Switch to accelerated pacing
- Expand to additional placements