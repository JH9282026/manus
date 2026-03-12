---
name: social-media-digital-research
description: "Social Media & Digital Research is a systematic approach to gathering, analyzing, and interpreting data from social platforms, online communities, and digital channels to understand public opinion, consumer behavior, brand perception, emerging trends, and network dynamics."
---

---
name: Social Media & Digital Research
description: Comprehensive methodology for social listening, sentiment analysis, digital footprint analysis, influencer research, and online community intelligence.
---

# Social Media & Digital Research


## Overview

This section provides an overview of the skill.

## Skill Description and Purpose

Social Media & Digital Research is a systematic approach to gathering, analyzing, and interpreting data from social platforms, online communities, and digital channels to understand public opinion, consumer behavior, brand perception, emerging trends, and network dynamics. This skill transforms the vast stream of user-generated content into actionable intelligence for business, marketing, and strategic decision-making.

The fundamental purpose is to tap into the authentic, unsolicited expressions of opinion, preference, and behavior that occur naturally across digital platforms. Unlike traditional research where participants respond to researcher questions, social media research captures organic conversations, reactions, and interactions that reveal genuine attitudes and emerging phenomena in real-time.

Core methodological components include:
- **Social Listening**: Systematic monitoring of brand, topic, or keyword mentions
- **Sentiment Analysis**: Automated and manual classification of opinion polarity
- **Digital Footprint Analysis**: Tracking online presence and behavioral patterns
- **Influencer Research**: Identifying and evaluating key opinion leaders
- **Network Analysis**: Mapping relationships and information flows
- **Community Analysis**: Understanding group dynamics and engagement patterns
- **Viral Content Tracking**: Monitoring content spread and meme evolution

Deploy this skill when:
- Monitoring brand reputation and crisis early warning
- Understanding customer opinions and pain points
- Tracking competitor activity and market positioning
- Identifying and evaluating potential influencer partnerships
- Researching emerging trends and cultural shifts
- Analyzing campaign performance and audience engagement
- Conducting background research on individuals or organizations
- Understanding online community dynamics and sentiment

## Required Inputs/Parameters

### Primary Inputs

| Parameter | Format | Description | Required |
|-----------|--------|-------------|----------|
| `research_objective` | Object | Clear statement of what insights are needed | Yes |
| `monitoring_targets` | Array | Brands, topics, keywords, hashtags, accounts to track | Yes |
| `platform_scope` | Array | Social platforms to include (Twitter, Facebook, Instagram, LinkedIn, TikTok, Reddit, YouTube, etc.) | Yes |
| `time_period` | Object | Historical analysis period and/or ongoing monitoring duration | Yes |
| `geographic_scope` | Array | Regions and languages to include | Yes |

### Query Configuration

| Parameter | Format | Description | Required |
|-----------|--------|-------------|----------|
| `primary_keywords` | Array | Core terms and phrases to monitor | Yes |
| `boolean_queries` | Array | Complex search queries with operators | No |
| `exclusion_terms` | Array | Terms to filter out irrelevant content | No |
| `hashtag_tracking` | Array | Specific hashtags to monitor | No |
| `account_monitoring` | Array | Specific accounts to track | No |
| `url_tracking` | Array | Specific URLs or domains to monitor for shares | No |

### Analysis Parameters

| Parameter | Format | Description | Required |
|-----------|--------|-------------|----------|
| `sentiment_granularity` | Enum | "binary", "ternary", "scale", "emotion_specific" | Yes |
| `topic_extraction` | Boolean | Whether to perform automated topic modeling | No |
| `influencer_identification` | Boolean | Whether to identify key voices | No |
| `network_analysis` | Boolean | Whether to map relationship networks | No |
| `demographic_analysis` | Boolean | Whether to infer audience demographics | No |

### Competitive Context

| Parameter | Format | Description | Required |
|-----------|--------|-------------|----------|
| `competitor_profiles` | Array | Competitor accounts and keywords | No |
| `industry_benchmarks` | Object | Share of voice and engagement baselines | No |
| `campaign_tracking` | Array | Specific campaigns to measure | No |

## Expected Outputs/Deliverables

### Primary Deliverables

1. **Social Intelligence Report** (30-60 pages)
   - Executive summary with key findings and recommendations
   - Methodology documentation including data sources and limitations
   - Volume and trend analysis over time
   - Sentiment analysis with polarity breakdown
   - Theme and topic analysis with representative examples
   - Audience analysis and demographic insights
   - Platform-specific findings and differences
   - Competitive benchmarking and share of voice
   - Influencer and key opinion leader identification
   - Actionable recommendations

2. **Sentiment Analysis Dashboard** (Interactive or static)
   - Overall sentiment score with trend over time
   - Sentiment breakdown by platform, topic, and demographic
   - Sentiment drivers analysis (what causes positive/negative sentiment)
   - Emotion detection results (anger, joy, fear, surprise, etc.)
   - Real-time alert configuration for sentiment shifts
   - Comparative sentiment against competitors

3. **Topic and Theme Analysis** (Structured data + narrative)
   - Topic model results with coherent theme clusters
   - Topic prevalence and evolution over time
   - Representative posts for each topic
   - Emerging themes and novel conversations
   - Topic-sentiment correlation analysis

### Influencer and Network Deliverables

4. **Influencer Landscape Report**
   - Influencer identification with reach and engagement metrics
   - Influencer profiles including:
     - Audience size and growth trajectory
     - Engagement rates and authenticity indicators
     - Content themes and posting patterns
     - Audience demographics and interests
     - Brand affinity and past collaborations
     - Estimated partnership costs
   - Influencer tier categorization (mega, macro, micro, nano)
   - Recommended partnership targets with rationale

5. **Network Analysis Visualization**
   - Social network graphs showing relationships
   - Community detection and cluster identification
   - Information flow pathways
   - Key bridge nodes and gatekeepers
   - Influence propagation patterns

### Monitoring Deliverables

6. **Real-Time Monitoring Dashboard**
   - Mention volume tracking with anomaly alerts
   - Sentiment monitoring with threshold notifications
   - Competitive share of voice tracking
   - Viral content detection and alerts
   - Crisis early warning indicators

7. **Viral Content Analysis**
   - Tracking of content spread velocity and reach
   - Meme evolution and variation mapping
   - Engagement pattern analysis
   - Platform cross-pollination tracking
   - Viral potential scoring for owned content

### Quality Standards

- Minimum sample size for sentiment analysis: 500 mentions
- Sentiment classification accuracy: minimum 80% agreement with human coding
- Bot and spam filtering applied to all analyses
- Geographic and demographic representativeness documented
- Platform bias and limitations explicitly addressed
- Privacy-compliant data collection (no private posts without consent)

## Example Use Cases

### Use Case 1: Brand Reputation Monitoring

**Scenario**: A consumer goods company needs continuous monitoring of brand perception and early warning of potential reputation issues across social platforms.

**Approach**:
- Configure monitoring for brand name, products, executives, and key terms
- Deploy sentiment analysis across Twitter, Instagram, Facebook, Reddit, TikTok
- Set up real-time alerts for sentiment drops and volume spikes
- Track competitive share of voice monthly
- Identify emerging themes and consumer pain points
- Provide weekly reports and immediate crisis alerts

**Outcome**: Detected emerging product quality complaints 48 hours before mainstream media pickup, enabling proactive response. Identified recurring customer service themes driving negative sentiment, informing operational improvements.

### Use Case 2: Influencer Partnership Strategy

**Scenario**: A fashion brand wants to identify and evaluate potential influencer partners for an upcoming campaign launch targeting Gen Z consumers.

**Approach**:
- Define target audience profile and platform priorities (TikTok, Instagram)
- Identify 500+ influencers in fashion, beauty, and lifestyle categories
- Analyze engagement rates, audience authenticity, and demographic fit
- Assess brand affinity through historical content analysis
- Evaluate potential partnership conflicts and reputation risks
- Provide tiered recommendations with estimated reach and cost

**Outcome**: Identified 25 high-fit influencers across tiers. Campaign with selected partners achieved 3x engagement versus brand average, with cost-per-engagement 40% below industry benchmark.

### Use Case 3: Crisis Response Intelligence

**Scenario**: A food company faces emerging social media backlash over a viral video showing alleged product contamination. Needs real-time intelligence to guide response.

**Approach**:
- Deploy immediate monitoring across all platforms
- Track viral spread velocity and reach
- Identify key amplifiers and information sources
- Analyze sentiment trajectory and emotional intensity
- Monitor media pickup and cross-platform spread
- Provide hourly situation updates during active crisis

**Outcome**: Real-time intelligence enabled rapid, targeted response. Identified original video source within 2 hours. Tracked sentiment recovery following company statement. Documented that 70% of negative volume came from 5% of accounts (coordinated campaign detection).

### Use Case 4: Competitive Social Intelligence

**Scenario**: A B2B software company wants to understand competitor positioning and customer perceptions across LinkedIn, Twitter, and industry forums.

**Approach**:
- Configure monitoring for 5 key competitors
- Track product mentions, feature discussions, and complaint patterns
- Analyze competitive share of voice and sentiment comparison
- Identify competitor customers expressing dissatisfaction
- Monitor competitor campaign launches and messaging
- Provide monthly competitive intelligence briefings

**Outcome**: Identified competitor's product reliability issues trending in customer discussions. Informed sales team targeting of dissatisfied competitor customers. Detected competitor messaging shift enabling proactive counter-positioning.

## Prerequisites or Dependencies

### Required Tools and Platforms

| Tool Category | Recommended Options | Purpose |
|---------------|---------------------|---------|
| Social Listening | Brandwatch, Sprinklr, Meltwater, Talkwalker | Monitoring and analytics |
| Sentiment Analysis | MonkeyLearn, Lexalytics, IBM Watson NLU | Automated sentiment |
| Influencer Platforms | CreatorIQ, Traackr, Upfluence | Influencer discovery |
| Network Analysis | Gephi, NodeXL, Python (networkx) | Relationship mapping |
| Data Collection | CrowdTangle (Meta), Twitter API, Brandwatch API | Raw data access |
| Visualization | Tableau, Power BI, Python (plotly) | Dashboard creation |

### Platform API Access Requirements

- Twitter API (Essential, Elevated, or Academic Research tier)
- Meta CrowdTangle access for Facebook/Instagram public data
- Reddit API for subreddit monitoring
- YouTube Data API for video and comment analysis
- LinkedIn API (limited availability)
- TikTok Research API or third-party tools

### Analytical Competencies

- Natural Language Processing fundamentals
- Statistical analysis for trend detection
- Network analysis and graph theory basics
- Data visualization best practices
- Qualitative coding for thematic analysis
- Research design for social data

### Data Quality Considerations

- Bot and fake account detection and filtering
- Spam and promotional content filtering
- Sarcasm and irony detection limitations
- Language detection and translation handling
- Platform-specific biases (demographics, content types)
- Sample representativeness versus population

### Ethical and Legal Requirements

- GDPR compliance for EU data subjects
- CCPA compliance for California residents
- Platform Terms of Service compliance
- No scraping of private or protected content
- Appropriate data retention and anonymization
- Disclosure requirements for influencer research

### Resource Requirements

- Social listening platform licensing: $12,000-100,000+ annually
- Analyst time: varies by monitoring scope
- API costs for high-volume data access
- Influencer database subscriptions
- Custom sentiment model training data
