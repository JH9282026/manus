# Marketing Mix Modeling Case Studies

Real-world examples of MMM implementation across industries, demonstrating methodologies, challenges, results, and lessons learned.

---

## Consumer Packaged Goods (CPG)

### Case Study 1: Health Food Company (Suntory Wellness, Taiwan)

**Company Background**
Suntory Wellness is a health food company operating in Taiwan with diverse online and offline marketing channels.

**Business Challenge**
- Complex marketing mix across multiple channels
- Need to understand which channels drive the most incremental sales
- Optimize budget allocation for maximum ROI
- Measure long-term brand-building vs. short-term performance

**MMM Approach**
- Partnered with Mutinex and Google
- Implemented time-varying Marketing Mix Model
- Analyzed both online and offline channels
- Used Bayesian methodology for robust estimates
- Incorporated adstock and saturation effects

**Channels Analyzed**
- Google AI-powered solutions (Performance Max, Demand Gen)
- YouTube (in-stream and other formats)
- Other digital channels
- Traditional media

**Key Findings**
- Google's AI-powered ad solutions (Performance Max and Demand Gen) drove the largest contribution with best-in-class cost per incremental acquisition
- YouTube showed the longest adstock among digital media, indicating sustained impact on consumer purchase behavior
- High return on ad spend (ROAS) for Google media was achieved when YouTube in-stream campaigns were run alongside other Google channels
- Synergistic effects between YouTube and other digital channels

**Business Impact**
- Optimized budget allocation toward highest-performing channels
- Increased investment in Google AI-powered solutions
- Strategic use of YouTube for long-term brand building
- Plans to utilize Google's open-source MMM tool (Meridian) for comprehensive ongoing analysis

**Lessons Learned**
- Time-varying coefficients capture changing market dynamics
- Measuring adstock reveals long-term brand-building effects
- Channel synergies are critical for optimization
- AI-powered advertising solutions can deliver superior performance

---

### Case Study 2: Plant-Based Meat Company (Beyond Meat)

**Company Background**
Beyond Meat is a plant-based meat company selling through retail channels.

**Business Challenge**
- Verify outcomes from another MMM provider
- Understand what marketing efforts truly drive retail sales
- Optimize media mix for growth
- Measure effectiveness of upper-funnel vs. lower-funnel tactics

**MMM Approach**
- Conducted by M-Squared
- Data harmonization across multiple retail channels
- Preliminary analysis to understand data patterns
- Ran thousands of model iterations for different retail groupings
- Resulted in four primary retail sales channel models
- Used regression with adstock and saturation transformations

**Channels Analyzed**
- Upper-funnel media (TV, display, video)
- Lower-funnel media (paid search, social)
- Retail promotions
- Distribution expansion

**Key Findings**
- Media drives nearly 10% of sales incrementally
- Overall media ROAS: $4.00 (for every $1 spent, $4 in sales)
- Upper-funnel tactics: Average ROAS of 4.85
- Lower-funnel tactics: Average ROAS of 2.6
- Significant opportunity for growth through increased media investment

**Optimization Recommendations**
- Nearly double the media budget
- Shift allocation toward upper-funnel tactics (higher ROAS)
- Optimize mix within upper-funnel (TV, video, display)
- Expected outcome: 26% growth in retail sales

**Business Impact**
- Data-driven budget increase justification
- Strategic shift toward brand-building (upper-funnel)
- Clear roadmap for sales growth
- Validated previous MMM findings with independent analysis

**Lessons Learned**
- Upper-funnel brand-building can have higher ROI than lower-funnel performance marketing
- Retail sales require different modeling approach than direct-to-consumer
- Independent validation builds stakeholder confidence
- Significant growth opportunities often exist in increasing total budget, not just reallocation

---

## Retail and E-Commerce

### Case Study 3: Retail Market Leader

**Company Background**
A leading retail company traditionally focused on short-term sales tactics.

**Business Challenge**
- Historically focused only on short-term sales effects
- Need to understand long-term brand-building impact
- Optimize media mix for both short-term and long-term goals
- Justify marketing investments to finance team

**MMM Approach**
- Conducted by Nepa, a marketing intelligence agency
- Ran two separate models:
  1. Short-term sales effects model
  2. Long-term brand effects model
- Integrated both models for holistic view
- Tested multiple budget scenarios

**Channels Analyzed**
- TV advertising
- Digital media (search, display, social)
- Print advertising
- Radio
- In-store promotions

**Key Findings**
- Current media mix was sub-optimal
- Significant opportunity to increase sales without increasing budget
- Conservative optimization: 15% sales increase with same budget
- Aggressive optimization: 25% sales increase with 15% budget increase
- Long-term brand-building tactics were underinvested

**Optimization Recommendations**

*Conservative Approach (Chosen)*
- Reallocate existing budget toward higher-ROI channels
- Increase investment in brand-building tactics
- Reduce spend on saturated channels
- Expected: 15% sales increase, no budget increase

*Aggressive Approach*
- Increase total budget by 15%
- Optimize allocation across all channels
- Expected: 25% sales increase

**Business Impact**
- Client chose conservative approach
- Achieved better-than-expected results (exceeded 15% target)
- Shifted organizational mindset to include long-term brand effects
- Secured buy-in for future budget increases based on success

**Lessons Learned**
- Separating short-term and long-term effects provides clearer insights
- Conservative recommendations can build trust for future aggressive moves
- Demonstrating results without budget increase is powerful for stakeholder buy-in
- Retail companies often underinvest in brand-building

---

### Case Study 4: Sleep-Enhancing Products (Cura of Sweden)

**Company Background**
Cura of Sweden sells sleep-enhancing products with plans for international expansion.

**Business Challenge**
- Long purchase cycles made multi-touch attribution insufficient
- Need privacy-compliant measurement solution
- Optimize marketing mix for international expansion
- Measure effectiveness across diverse channels

**MMM Approach**
- Leveraged Cassandra MMM platform
- Bayesian regression methodology
- Incorporated adstock for long purchase cycles
- Analyzed both online and offline channels
- Continuous model updates for agility

**Channels Analyzed**
- Paid search
- Social media advertising
- Display advertising
- Content marketing
- Influencer partnerships
- Traditional media

**Key Results**
- 86% increase in orders from paid media
- 16% decrease in cost per conversion
- 52% increase in marketing budget invested (due to proven ROI)
- Identified optimal channel mix for international markets

**Optimization Actions**
- Reallocated budget from low-performing to high-performing channels
- Increased investment in channels with headroom (below saturation)
- Reduced spend on saturated channels
- Tailored channel mix for different international markets

**Business Impact**
- Dramatic improvement in marketing efficiency
- Confidence to increase marketing investment
- Successful international expansion supported by data-driven insights
- Shift from attribution to MMM as primary measurement tool

**Lessons Learned**
- MMM is superior to attribution for long purchase cycles
- Privacy-compliant measurement is achievable and effective
- Continuous model updates enable agile optimization
- Proven ROI justifies budget increases

---

## Gaming and Entertainment

### Case Study 5: Video Game Company (Nexon, South Korea)

**Company Background**
Nexon is the publisher of FC Online, a popular video game in South Korea.

**Business Challenge**
- Complex media mix with many channels
- Need to understand direct and synergistic impacts
- Optimize marketing investment for player acquisition
- Measure effectiveness of brand vs. performance channels

**MMM Approach**
- Conducted by Analytic Edge in collaboration with Google
- Enhanced MMM with causal inference and machine learning
- Analyzed both direct effects and channel synergies
- Used advanced statistical methods to handle multicollinearity
- Incorporated interaction terms for synergy measurement

**Channels Analyzed**
- Google Display Network
- YouTube
- Paid search
- Social media
- Traditional media (TV)
- Influencer marketing

**Key Findings**
- Google Display Network had the highest ROI among digital channels
- YouTube played a key role in indirectly improving performance of other media channels
- Significant synergistic effects between YouTube and other digital channels
- Upper-funnel channels (YouTube, Display) amplified lower-funnel effectiveness

**Optimization Recommendations**
- Maintain investment in Google Display Network (highest direct ROI)
- Increase YouTube investment for synergistic benefits
- Coordinate campaigns across channels to maximize synergies
- Time upper-funnel and lower-funnel campaigns for optimal interaction

**Business Impact**
- More informed marketing investment decisions
- Strategic use of YouTube for amplification
- Improved overall marketing efficiency
- Better understanding of channel interactions

**Lessons Learned**
- Synergistic effects can be as important as direct effects
- Upper-funnel channels often have hidden value through amplification
- Machine learning can enhance traditional MMM
- Gaming industry benefits from integrated brand and performance marketing

---

## Airlines and Travel

### Case Study 6: International Airline (Europe)

**Company Background**
A major international airline based in Europe with diverse marketing channels.

**Business Challenge**
- Understand marketing mix effectiveness across channels
- Optimize marketing ROI
- Justify marketing investments to executive leadership
- Navigate competitive and dynamic market

**MMM Approach**
- Conducted by MASS Analytics
- Comprehensive data collection across all marketing channels
- Regression-based MMM with adstock and saturation
- Scenario analysis for optimization
- Validation with business stakeholders

**Channels Analyzed**
- TV advertising
- Digital media (search, display, social, video)
- Radio
- Print
- Sponsorships
- Loyalty program marketing

**Key Results**
- 17% increase in Marketing ROI
- Solid understanding of marketing mix effectiveness
- Clear recommendations for budget reallocation
- Improved forecasting accuracy for sales planning

**Optimization Actions**
- Shifted budget from lower-ROI to higher-ROI channels
- Increased investment in digital channels
- Optimized timing of campaigns around booking patterns
- Reduced spend on saturated traditional channels

**Business Impact**
- Significant ROI improvement
- Executive buy-in for data-driven marketing
- Ongoing use of MMM for annual planning
- Competitive advantage through optimized marketing

**Lessons Learned**
- Airlines have complex seasonality requiring careful modeling
- Booking patterns and lead times affect adstock parameters
- Competitive activity is critical control variable
- Executive stakeholder engagement is key to success

---

## Cross-Industry Insights

### Common Success Factors

**1. Data Quality and Completeness**
- Successful MMMs have comprehensive, accurate data
- 2-3 years of weekly data is minimum
- Include all relevant channels and control variables
- Invest in data infrastructure early

**2. Stakeholder Engagement**
- Involve marketing, finance, and executive leadership early
- Regular communication and validation sessions
- Translate statistical findings into business language
- Demonstrate value through pilot implementations

**3. Methodological Rigor**
- Use appropriate statistical techniques (Bayesian, regularization)
- Validate models thoroughly (in-sample and out-of-sample)
- Test multiple model specifications
- Incorporate domain knowledge and business logic

**4. Actionable Recommendations**
- Provide specific, quantified recommendations
- Prioritize based on impact and feasibility
- Include implementation guidance
- Set realistic expectations

**5. Continuous Improvement**
- Regularly update models with new data
- Incorporate experimental results for calibration
- Adapt to market changes and new channels
- Build institutional knowledge and capabilities

### Common Challenges and Solutions

**Challenge: Multicollinearity**
- Channels often move together (correlated spend)
- Solution: Regularization, Bayesian priors, experimental calibration, combine channels

**Challenge: Limited Data Variation**
- Constant spend makes it hard to estimate effects
- Solution: Longer time periods, geographic variation, intentional spend tests

**Challenge: Stakeholder Skepticism**
- Results may contradict conventional wisdom
- Solution: Validation with business knowledge, pilot tests, transparent communication

**Challenge: Attribution vs. MMM Discrepancies**
- Digital attribution and MMM may show different results
- Solution: Understand methodological differences, use both for complementary insights

**Challenge: New Channels**
- Emerging channels lack historical data
- Solution: Start tracking early, use priors from similar channels, conduct experiments

### Industry-Specific Considerations

**CPG and Retail**
- Strong seasonality and promotional effects
- Distribution and pricing are critical variables
- Retail sales data may have lags
- Competitor activity is highly influential

**E-Commerce and DTC**
- Shorter feedback loops (daily data possible)
- Rich digital data availability
- Attribution models provide complementary insights
- Rapid market changes require frequent updates

**Financial Services**
- Long consideration and purchase cycles
- Regulatory constraints on marketing
- Brand trust and reputation are critical
- Customer lifetime value is key metric

**Travel and Hospitality**
- Extreme seasonality and event-driven demand
- Booking lead times affect adstock
- Economic conditions highly influential
- Competitive pricing is critical

**Gaming and Entertainment**
- Launch events create spikes
- User acquisition and retention both important
- Influencer marketing is significant
- Rapid content and campaign cycles

---

## ROI Benchmarks by Industry and Channel

### Industry Benchmarks

**Consumer Packaged Goods (CPG)**
- Overall Marketing ROI: 1.5 - 3.0
- TV: 1.2 - 2.5
- Digital: 2.0 - 4.0
- Promotions: 0.8 - 1.5

**Retail**
- Overall Marketing ROI: 2.0 - 4.0
- TV: 1.5 - 3.0
- Digital: 2.5 - 5.0
- In-store promotions: 1.0 - 2.0

**E-Commerce / DTC**
- Overall Marketing ROI: 2.5 - 5.0
- Paid Search: 3.0 - 6.0
- Social Media: 2.0 - 4.0
- Display: 1.5 - 3.0

**Financial Services**
- Overall Marketing ROI: 1.0 - 2.5
- TV: 0.8 - 2.0
- Digital: 1.5 - 3.5
- Content Marketing: 2.0 - 4.0

**Travel and Hospitality**
- Overall Marketing ROI: 2.0 - 4.0
- Paid Search: 3.0 - 6.0
- Display: 1.5 - 3.0
- Email: 4.0 - 8.0

**Note**: These are general ranges. Actual ROI varies significantly based on market conditions, competitive intensity, brand strength, and execution quality.

### Channel Benchmarks (Cross-Industry Averages)

**TV Advertising**
- ROI: 1.2 - 2.5
- Adstock decay: 0.3 - 0.7 (moderate to long carryover)
- Best for: Brand building, mass reach, long-term effects

**Paid Search**
- ROI: 2.5 - 5.0
- Adstock decay: 0.0 - 0.2 (very short carryover)
- Best for: Capturing existing demand, direct response

**Social Media Advertising**
- ROI: 2.0 - 4.0
- Adstock decay: 0.2 - 0.5 (moderate carryover)
- Best for: Targeted reach, engagement, brand building

**Display Advertising**
- ROI: 1.5 - 3.0
- Adstock decay: 0.1 - 0.3 (short carryover)
- Best for: Awareness, retargeting, visual storytelling

**Video/YouTube**
- ROI: 1.8 - 3.5
- Adstock decay: 0.3 - 0.6 (moderate to long carryover)
- Best for: Brand building, storytelling, synergistic effects

**Radio**
- ROI: 1.0 - 2.0
- Adstock decay: 0.2 - 0.5 (moderate carryover)
- Best for: Local reach, frequency, commuter audiences

**Print**
- ROI: 0.8 - 1.8
- Adstock decay: 0.4 - 0.7 (long carryover)
- Best for: Credibility, detailed information, older demographics

**Email Marketing**
- ROI: 3.0 - 7.0
- Adstock decay: 0.0 - 0.1 (very short carryover)
- Best for: Customer retention, personalization, low cost

---

## Implementation Best Practices from Case Studies

### Data Collection

**Start Early**
- Begin collecting comprehensive data before starting MMM project
- Ensure consistent tracking across all channels
- Document data sources and definitions

**Centralize Data**
- Create single source of truth for all marketing and sales data
- Use data warehouse or marketing data platform
- Automate data pipelines for ongoing updates

**Include Control Variables**
- Don't focus only on marketing data
- Collect economic indicators, competitor data, weather, etc.
- These improve model accuracy and attribution

### Model Development

**Test Multiple Specifications**
- Don't settle on first model
- Test different adstock and saturation functions
- Compare regularization approaches
- Validate with business stakeholders

**Use Bayesian Methods**
- Incorporate domain knowledge through priors
- Get uncertainty estimates
- Handle limited data better
- Enable experimental calibration

**Validate Rigorously**
- In-sample: Residual analysis, coefficient checks
- Out-of-sample: Hold-out testing, cross-validation
- Business validation: Stakeholder review, benchmark comparison

### Optimization and Recommendations

**Provide Specific Actions**
- Not just "increase digital," but "increase paid search by $X"
- Quantify expected impact
- Prioritize by impact and feasibility

**Offer Multiple Scenarios**
- Conservative, moderate, aggressive options
- Different budget levels
- Allows stakeholders to choose based on risk tolerance

**Include Implementation Guidance**
- How to execute recommendations
- Timeline and milestones
- Responsible parties
- Monitoring and adjustment plan

### Stakeholder Management

**Communicate in Business Language**
- Avoid statistical jargon
- Focus on business impact (revenue, ROI, growth)
- Use visualizations effectively

**Be Transparent About Limitations**
- MMM provides estimates, not perfect truth
- Acknowledge uncertainty
- Explain assumptions and caveats

**Demonstrate Value Quickly**
- Pilot recommendations on small scale
- Track results and share successes
- Build credibility for larger changes

### Ongoing Management

**Regular Updates**
- Weekly/monthly: Update forecasts with latest data
- Quarterly: Re-estimate parameters
- Annually: Comprehensive model rebuild

**Integrate with Experiments**
- Use MMM to identify testing opportunities
- Use experimental results to calibrate MMM
- Create virtuous cycle of measurement

**Build Internal Capabilities**
- Train internal team on MMM concepts
- Develop in-house modeling expertise
- Reduce dependence on external vendors
- Foster data-driven culture

---

## Lessons Learned Across All Case Studies

### What Works

1. **Comprehensive Data**: All successful MMMs had 2-3 years of quality data across all channels
2. **Stakeholder Engagement**: Early and ongoing involvement of marketing, finance, and leadership
3. **Rigorous Validation**: Multiple validation approaches (statistical, out-of-sample, business)
4. **Actionable Insights**: Specific, quantified recommendations with implementation guidance
5. **Continuous Improvement**: Regular model updates and integration with experiments
6. **Bayesian Approaches**: Use of priors and uncertainty quantification improved robustness
7. **Synergy Measurement**: Accounting for channel interactions revealed hidden value
8. **Pilot Testing**: Small-scale implementation of recommendations built confidence

### What Doesn't Work

1. **Insufficient Data**: Less than 2 years or incomplete channel coverage leads to unreliable results
2. **Ignoring Stakeholders**: Building model in isolation leads to lack of adoption
3. **Over-Complexity**: Overly complex models are hard to explain and maintain
4. **One-Time Analysis**: MMM requires ongoing updates to remain relevant
5. **Ignoring Business Logic**: Purely statistical approach without business validation fails
6. **Vague Recommendations**: "Invest more in digital" is not actionable
7. **Unrealistic Expectations**: Treating MMM as perfect truth rather than decision support
8. **Poor Communication**: Statistical jargon alienates business stakeholders

### Key Takeaways for Practitioners

**For Data Scientists**
- Balance statistical rigor with business practicality
- Communicate in business language
- Validate, validate, validate
- Incorporate domain knowledge through priors or constraints
- Be transparent about uncertainty and limitations

**For Marketing Leaders**
- Invest in data infrastructure early
- Engage with MMM process, don't delegate entirely
- Be open to challenging conventional wisdom
- Pilot recommendations before full implementation
- Use MMM as decision support, not sole decision-maker

**For Executives**
- MMM provides directional insights for strategic decisions
- Requires investment in data, tools, and talent
- Value comes from implementation, not just analysis
- Ongoing commitment needed for sustained value
- Complements (doesn't replace) other measurement approaches