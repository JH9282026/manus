---
name: competitive-analysis-&-intelligence
description: "The Competitive Analysis & Intelligence skill transforms an agentic AI into a world-class competitive intelligence analyst capable of conducting systematic, comprehensive analysis of competitive landscapes across any industry."
---

---
name: Competitive Analysis & Intelligence
description: A comprehensive competitive intelligence skill enabling deep competitive analysis across all business dimensions, delivering actionable insights through strategic frameworks, market analysis, and real-time monitoring for strategic decision-making.
---

# Competitive Analysis & Intelligence


## Overview

This section provides an overview of the skill.

## 1. Skill Description and Purpose

### Overview

The Competitive Analysis & Intelligence skill transforms an agentic AI into a world-class competitive intelligence analyst capable of conducting systematic, comprehensive analysis of competitive landscapes across any industry. This skill encompasses the full spectrum of competitive intelligence activities—from initial competitor identification through strategic framework application to continuous monitoring and actionable recommendations.

### Core Capabilities

This skill enables the agent to perform **sixteen interconnected competitive intelligence functions**:

**Competitor Intelligence & Profiling**: Systematically identify and profile all competitor types—direct, indirect, potential, substitute, emerging, and geographic competitors. Build comprehensive profiles including company overview, leadership, business model, organizational structure, ownership, culture, and strategic positioning. Map competitive landscapes visually and track competitors continuously with change detection and historical trend analysis.

**Strategic Framework Application**: Execute rigorous strategic analysis using industry-standard frameworks including SWOT Analysis (internal strengths/weaknesses and external opportunities/threats), Porter's Five Forces (competitive rivalry, supplier power, buyer power, substitutes, new entrants), PESTEL Analysis (political, economic, social, technological, environmental, legal factors), Value Chain Analysis (primary and support activities), BCG Matrix (stars, cash cows, question marks, dogs), Ansoff Matrix (market penetration, product development, market development, diversification), Blue Ocean Strategy (ERRC grid, strategy canvas), GE-McKinsey Matrix (industry attractiveness vs. competitive strength), and Competitive Advantage Analysis (cost leadership, differentiation, focus).

**Market Positioning Analysis**: Analyze current and desired market positions, create perceptual maps on key dimensions (price vs. quality, features vs. ease of use), develop positioning statements, evaluate differentiation strategies, assess unique value propositions (UVPs), identify sustainable competitive advantages, and analyze brand positioning including perception, associations, personality, and equity.

**Market Share Analysis**: Estimate market sizes (TAM, SAM, SOM), calculate market share by revenue, units, and segments, analyze share of voice across channels, track market growth rates and CAGR, assess market penetration rates, measure market concentration using HHI and concentration ratios, and perform detailed market segmentation analysis.

**Product/Service Comparison**: Build comprehensive feature comparison matrices, analyze product portfolios for breadth and depth, compare service offerings, benchmark quality and performance, track innovation and R&D activities, gather product roadmap intelligence, and assess product lifecycle stages for each competitor.

**Pricing Intelligence**: Decode competitor pricing strategies (cost-plus, value-based, competitive, penetration, skimming, freemium, dynamic), analyze price positioning, compare pricing models (subscription, tiered, usage-based, per-user, hybrid), track discounts and promotions, perform value-based pricing analysis, estimate price elasticity, and compare pricing tiers across competitors.

**Marketing Strategy Analysis**: Evaluate marketing channel mix and effectiveness, analyze content strategies, assess social media presence and engagement, conduct SEO/SEM competitive analysis, decode brand positioning and messaging, estimate advertising spend, analyze campaign effectiveness, review email marketing approaches, and track influencer partnerships.

**Sales & Distribution Analysis**: Map sales channels (direct, indirect, online, offline), analyze distribution networks, track partnerships and alliances, assess geographic coverage, understand sales processes and methodologies, evaluate sales team structures, and calculate customer acquisition costs (CAC) with comparisons.

**Financial Analysis**: Analyze revenue and profitability metrics, track funding and investments, compare valuations, assess financial health through liquidity, solvency, profitability, and efficiency ratios, dissect cost structures, compare financial ratios, and evaluate burn rate and runway for startups.

**Technology & Innovation Tracking**: Analyze technology stacks, track patents and intellectual property, monitor innovation pipelines, assess digital transformation maturity, identify technology partnerships, evaluate API and integration capabilities, compare mobile and web platforms, and assess cybersecurity and data privacy postures.

**Customer Analysis**: Compare customer bases, analyze customer satisfaction and reviews, track Net Promoter Scores (NPS), evaluate customer acquisition strategies, measure retention and churn rates, calculate customer lifetime value (CLV), profile customer demographics and psychographics, identify customer pain points, and map customer journeys.

**Competitive Benchmarking**: Conduct performance benchmarking against KPIs, identify industry and competitor best practices, perform gap analysis (performance, capability, resource, strategic gaps), assess capability maturity, benchmark operational efficiency, quality, processes, functions, and strategic positioning.

**Real-Time Competitive Monitoring**: Implement automated competitor tracking with alerts, monitor news and press releases, track social media activity, detect website changes, analyze job postings for strategic signals, track conferences and events, monitor product launches, and capture partnership, acquisition, and leadership announcements.

### Strategic Value

This skill delivers transformative value for strategic decision-making:

- **Market Entry Decisions**: Comprehensive landscape analysis to inform go-to-market strategies
- **Product Strategy**: Feature gap identification and roadmap prioritization based on competitive positioning
- **Pricing Optimization**: Data-driven pricing decisions based on competitive intelligence
- **Marketing Differentiation**: Clear messaging based on competitive positioning analysis
- **Investment Decisions**: Due diligence support with thorough competitive context
- **M&A Analysis**: Target identification and competitive impact assessment
- **Strategic Planning**: Foundation for annual strategic planning cycles
- **Sales Enablement**: Battlecards and competitive positioning for sales teams

### When to Use This Skill

Deploy this skill when the user requires:
- Comprehensive competitive landscape analysis for strategic planning
- Deep-dive analysis of specific competitors
- Market entry feasibility assessment
- Product positioning or repositioning guidance
- Pricing strategy development or optimization
- Investment due diligence with competitive context
- Ongoing competitive monitoring and alerting
- Sales battlecard development
- Strategic framework application to competitive dynamics
- Industry trend analysis through a competitive lens

---

## 2. Required Inputs/Parameters

### Primary Inputs

**Target Company Information** (if analyzing for a specific company):
- Company name and website URL
- Industry and market segment
- Current products/services offered
- Geographic markets served
- Business model (B2B, B2C, B2B2C)
- Company size and stage (startup, growth, enterprise)
- Known competitors (if any)

**Analysis Scope Parameters**:
- `analysis_depth`: `quick_scan` | `standard` | `comprehensive` | `deep_dive`
- `competitor_count`: Number of competitors to analyze (recommended: 3-10)
- `time_horizon`: Historical period and forward-looking timeframe
- `geographic_scope`: `local` | `regional` | `national` | `international` | `global`
- `industry_vertical`: Specific industry classification (NAICS, SIC, or descriptive)

**Framework Selection**:
- `strategic_frameworks`: Array of frameworks to apply
  - `SWOT` - Strengths, Weaknesses, Opportunities, Threats
  - `porters_five_forces` - Industry competitive dynamics
  - `PESTEL` - Macro-environmental factors
  - `value_chain` - Activity-based cost and value analysis
  - `BCG_matrix` - Portfolio growth-share analysis
  - `ansoff_matrix` - Growth strategy options
  - `blue_ocean` - Value innovation and uncontested markets
  - `GE_McKinsey` - Portfolio attractiveness-strength matrix
  - `competitive_advantage` - Cost leadership, differentiation, focus

**Analysis Dimensions**:
- `include_product_analysis`: Boolean - Feature comparison and portfolio analysis
- `include_pricing_analysis`: Boolean - Pricing strategy and tier comparison
- `include_marketing_analysis`: Boolean - Channel, content, and brand analysis
- `include_financial_analysis`: Boolean - Revenue, funding, and ratio analysis
- `include_technology_analysis`: Boolean - Tech stack, patents, innovation
- `include_customer_analysis`: Boolean - Satisfaction, retention, demographics

**Output Preferences**:
- `output_format`: `executive_summary` | `detailed_report` | `dashboard` | `battlecard` | `all`
- `visualization_preference`: `minimal` | `standard` | `rich`
- `update_frequency`: `one_time` | `weekly` | `monthly` | `quarterly`

### Secondary Inputs

**Competitor Specification** (optional—agent can identify if not provided):
- Direct competitor list with websites
- Indirect competitor list
- Emerging/potential competitors to monitor

**Data Source Preferences**:
- `primary_sources`: Array of preferred data sources
- `excluded_sources`: Sources to avoid
- `data_recency_requirement`: Maximum age of data to consider

**Industry-Specific Parameters**:
- For SaaS: Include integrations, API ecosystem, developer relations
- For E-commerce: Include fulfillment, returns, marketplace presence
- For Financial Services: Include regulatory compliance, risk metrics
- For Healthcare: Include outcomes data, accreditations, specialties

**Prioritization Criteria**:
- `key_dimensions`: Ranked list of most important competitive dimensions
- `decision_context`: Strategic decision this analysis will inform
- `stakeholder_audience`: Who will consume this analysis (C-suite, product, sales, investors)

---

## 3. Expected Outputs/Deliverables

### Primary Deliverables

**Comprehensive Competitive Analysis Report**:
- **Executive Summary** (2-3 pages): Key findings, strategic implications, prioritized recommendations
- **Market Overview** (5-10 pages): Industry dynamics, market size and growth, key trends, regulatory landscape
- **Competitor Profiles** (3-5 pages each): Detailed profiles for each competitor including company overview, business model, product portfolio, market position, strengths/weaknesses, strategic direction
- **Strategic Framework Analysis** (10-15 pages): Complete application of selected frameworks with visualizations and insights
- **Comparative Analysis** (10-15 pages): Side-by-side comparisons across all dimensions—product, pricing, marketing, sales, financial, technology, customer
- **Strategic Recommendations** (5-10 pages): Prioritized, actionable recommendations with implementation considerations

**Competitive Intelligence Artifacts**:

| Artifact | Format | Description |
|----------|--------|-------------|
| Competitor Profiles | PDF/Markdown | 1-pager and detailed profiles for each competitor |
| Feature Comparison Matrix | Spreadsheet/Table | Comprehensive feature-by-feature comparison |
| Pricing Comparison | Table/Visual | Pricing models, tiers, and positioning |
| SWOT Matrices | Visual/Table | Individual and comparative SWOT analysis |
| Positioning Map | Visual | 2D perceptual map on key dimensions |
| Market Share Analysis | Chart/Table | Revenue and unit share by competitor |
| Technology Stack Comparison | Table | Tech platforms and capabilities comparison |
| Funding/Financial Summary | Table | Investment history and key financials |

**Strategic Framework Outputs**:

- **Porter's Five Forces Analysis**: Visual diagram with force strength ratings (1-5), detailed narrative for each force, overall industry attractiveness score, strategic implications
- **SWOT Analysis**: Quadrant matrices for target company and each competitor, comparative SWOT identifying relative advantages
- **PESTEL Analysis**: Factor-by-factor analysis with impact ratings, trend direction, and strategic implications
- **BCG Matrix**: Portfolio plot with recommended strategies for each quadrant
- **Value Chain Analysis**: Activity mapping with cost and value contribution, competitive comparison
- **Positioning Maps**: 2D plots on key dimensions with competitor clustering and white space identification

**Monitoring & Alerting Outputs** (for ongoing engagements):
- **Weekly Intelligence Brief**: Summary of competitor activities, news, and changes
- **Competitive Dashboard**: Real-time metrics and KPI tracking
- **Alert Notifications**: Triggered updates for significant competitor moves
- **Quarterly Competitive Review**: Comprehensive update on landscape evolution

### Quality Standards

All deliverables must meet these standards:
- **Data Currency**: All data points sourced within specified recency requirements
- **Source Attribution**: Every claim supported by identifiable, verifiable sources
- **Quantification**: Metrics and estimates with confidence levels where applicable
- **Actionability**: Every insight linked to potential strategic action
- **Visual Clarity**: Charts and diagrams following data visualization best practices
- **Executive Readability**: Clear hierarchy enabling quick comprehension at any level
- **Competitive Neutrality**: Objective analysis without bias toward any competitor

---

## 4. Example Use Cases

### Use Case 1: B2B SaaS Competitive Analysis

**Scenario**: A Series B project management software company wants to understand its competitive position against Asana, Monday.com, Notion, and ClickUp to inform product roadmap and positioning strategy.

**Execution Approach**:

1. **Competitor Profiling**: Build comprehensive profiles for each competitor—company history, funding ($500M+ for Asana, $275M for Monday.com), leadership teams, employee counts (2,000+ for Asana), organizational structure, and recent strategic moves.

2. **Product Analysis**: Create detailed feature comparison matrix across 150+ features including task management, project views (Gantt, Kanban, Calendar, Timeline), collaboration features, automation capabilities, reporting/analytics, integrations (Asana: 200+, Monday.com: 50+), mobile apps, and API robustness.

3. **Pricing Intelligence**: Map pricing tiers—Asana Premium ($10.99/user/month), Monday.com Standard ($10/user/month), Notion Plus ($8/user/month), ClickUp Unlimited ($7/user/month). Analyze free tier limitations, enterprise pricing opacity, discount patterns.

4. **Market Positioning**: Create perceptual map plotting competitors on ease-of-use vs. feature depth. Identify Monday.com positioning as "Work OS," Notion as "connected workspace," Asana as "enterprise work management."

5. **Strategic Framework Application**: Apply Porter's Five Forces revealing high competitive rivalry, low supplier power, moderate buyer power (low switching costs), threat from vertical-specific solutions (substitutes), and moderate entry barriers (network effects, integration ecosystems).

6. **Customer Analysis**: Aggregate G2 and Capterra reviews—Asana (4.3/5, 9,500+ reviews), Monday.com (4.7/5, 8,000+ reviews). Extract common praise and complaints. Calculate NPS estimates from public data.

7. **Recommendations**: Prioritized strategic recommendations for differentiation—vertical specialization opportunity, AI-powered automation gap, enterprise security/compliance positioning.

### Use Case 2: E-commerce Market Entry Analysis

**Scenario**: A European fashion retailer evaluating U.S. market entry needs competitive landscape analysis of online fashion retail including Nordstrom, ASOS, Revolve, and emerging DTC brands.

**Execution Approach**:

1. **Market Sizing**: Calculate TAM ($200B+ U.S. online apparel), SAM (target demographic segment), SOM (realistic capture rate based on comparable market entries).

2. **Competitor Landscape Mapping**: Identify and categorize 50+ competitors—department stores (Nordstrom, Macy's), pure-play e-commerce (ASOS, Revolve), DTC brands (Everlane, Reformation), marketplaces (Amazon Fashion, Poshmark).

3. **Business Model Analysis**: Compare marketplace vs. inventory models, private label strategies, sustainability positioning, membership/loyalty programs (Nordstrom Nordy Club, ASOS Premier).

4. **Pricing and Promotion Analysis**: Track pricing across categories, analyze promotional frequency and depth (ASOS: 20-70% off sales monthly), free shipping thresholds, return policies.

5. **Marketing Channel Analysis**: Evaluate channel mix—Instagram prominence for Revolve, affiliate marketing for ASOS, influencer partnerships, TikTok presence for Gen-Z targeting.

6. **Fulfillment Competitive Analysis**: Compare shipping speeds (Revolve: next-day, ASOS: 2-4 days), fulfillment networks, international shipping capabilities, returns process.

7. **Strategic Framework Application**: Apply Ansoff Matrix recommending market development strategy with existing product assortment, phased geographic expansion (East Coast first), partnership-led entry (wholesale to Nordstrom before DTC).

### Use Case 3: Financial Services Benchmarking

**Scenario**: A regional bank needs competitive benchmarking against national digital banks (Chime, SoFi) and traditional competitors (Chase, Bank of America) for digital transformation strategy.

**Execution Approach**:

1. **Digital Capability Assessment**: Benchmark mobile app features—mobile check deposit, P2P payments, budgeting tools, card controls, digital account opening. Rate capability maturity 1-5.

2. **Product Comparison**: Compare checking/savings accounts, fee structures (Chime: no monthly fees, Chase: $12/month waivable), APYs (SoFi: 4.5%+, traditional banks: 0.01%), overdraft policies.

3. **Technology Stack Analysis**: Research technology investments—Chime's partnership with Bancorp and Stride Bank, SoFi's Galileo acquisition, Chase's $12B annual tech spend.

4. **Customer Experience Analysis**: Analyze app store ratings (Chime: 4.7/5, Chase: 4.8/5), customer complaint data from CFPB database, social media sentiment.

5. **Financial Analysis**: Compare cost-to-income ratios, digital customer acquisition costs ($50-100 for neobanks vs. $200-400 for traditional), customer lifetime value calculations.

6. **Regulatory and Compliance**: Assess charter strategies (Chime: partner bank model, SoFi: bank charter obtained), compliance investments, regulatory risk profiles.

7. **Strategic Recommendations**: Prioritized digital transformation roadmap—mobile-first redesign, fee elimination strategy, fintech partnership opportunities, branch network optimization.

### Use Case 4: Technology Landscape Mapping

**Scenario**: A venture capital firm needs competitive intelligence on the AI/ML infrastructure market to inform investment thesis, mapping competitors like Databricks, Snowflake, AWS SageMaker, and emerging players.

**Execution Approach**:

1. **Market Segmentation**: Map competitive landscape across segments—data platforms, ML training infrastructure, MLOps tools, inference serving, feature stores.

2. **Funding and Valuation Analysis**: Track funding rounds—Databricks ($3.5B raised, $43B valuation), analyze investor profiles, identify funding trends signaling market momentum.

3. **Technology Differentiation**: Compare technical architectures—Databricks Lakehouse vs. Snowflake data cloud, managed vs. self-hosted options, multi-cloud support, open-source strategy (Databricks' Spark contribution).

4. **Customer Base Analysis**: Research customer logos from case studies and press releases, estimate customer counts and revenue (Snowflake: $2B+ ARR, Databricks: $1.5B+ ARR), analyze customer concentration.

5. **Partnership Ecosystem**: Map technology partnerships—cloud provider relationships (AWS, Azure, GCP integrations), ISV partnerships, system integrator alliances.

6. **Patent Analysis**: Search USPTO for patent filings, identify innovation focus areas, assess IP defensibility.

7. **Investment Thesis**: Synthesize findings into investment thesis—market growth (30%+ CAGR), competitive dynamics favoring platform consolidation, white space opportunities in vertical-specific solutions, acquisition targets for strategic buyers.

### Use Case 5: Healthcare Provider Competitive Analysis

**Scenario**: A health system needs competitive intelligence on ambulatory surgery center (ASC) competitors to inform service line expansion strategy.

**Execution Approach**:

1. **Competitor Identification**: Identify ASC competitors within service area—hospital-affiliated, physician-owned, national chains (USPI, AmSurg), specialty-specific centers.

2. **Service Line Analysis**: Compare specialties offered—orthopedics, ophthalmology, GI, pain management. Assess procedure volumes from state databases where available.

3. **Quality Benchmarking**: Compare publicly reported quality metrics—infection rates, complication rates, patient satisfaction scores (CMS data, Healthgrades).

4. **Payer Analysis**: Research payer contracts and in-network status, analyze pricing for common procedures, compare cost to hospital outpatient departments.

5. **Facility and Capacity**: Assess facility locations, operating room counts, equipment (robotic surgery capabilities), expansion plans from permit filings.

6. **Physician Relations**: Analyze physician alignment strategies, ownership structures, referring physician relationships, recruitment activities.

7. **Strategic Recommendations**: Service line prioritization based on competitive gaps, joint venture opportunities, geographic expansion targets, payer negotiation leverage points.

---

## 5. Prerequisites and Dependencies

### Required Data Access

**Web Access**: Unrestricted web browsing for competitor websites, news sources, review platforms, and public databases.

**Financial Data Sources**:
- SEC EDGAR for public company filings (10-K, 10-Q, S-1)
- Crunchbase or PitchBook for private company funding data
- Public earnings call transcripts and investor presentations

**Market Research Access**:
- Industry analyst reports (Gartner, Forrester, IDC)
- Market sizing data (Statista, IBISWorld)
- Trade publication archives

**Social and Review Platforms**:
- LinkedIn for company and employee data
- G2, Capterra, TrustRadius for B2B software reviews
- Glassdoor, Indeed for employee reviews
- Social media platforms for engagement analysis

**SEO/SEM Tools** (API access preferred):
- SEMrush, Ahrefs, or Moz for search analysis
- SimilarWeb for traffic estimates

### Technical Dependencies

**Data Processing**:
- Web scraping capabilities for competitor websites
- PDF extraction for annual reports and filings
- Structured data parsing (JSON, CSV)

**Analysis Tools**:
- Spreadsheet generation for comparison matrices
- Data visualization for charts and positioning maps
- Document generation for reports (Markdown, PDF)

**Monitoring Infrastructure** (for ongoing monitoring):
- Website change detection
- News API integration
- Social media monitoring
- Alert and notification system

### Knowledge Prerequisites

The agent must possess working knowledge of:

**Strategic Frameworks**: Deep understanding of SWOT, Porter's Five Forces, PESTEL, BCG Matrix, Value Chain, Ansoff Matrix, Blue Ocean Strategy, GE-McKinsey Matrix—including when each is appropriate and how to synthesize findings.

**Financial Analysis**: Ability to read and interpret financial statements, calculate and compare financial ratios, understand valuation methodologies, and assess financial health indicators.

**Market Research Methodology**: Understanding of market sizing approaches (top-down, bottom-up), primary vs. secondary research, data validation techniques, and confidence interval estimation.

**Industry Context**: Sufficient domain knowledge to understand industry-specific competitive dynamics, terminology, success factors, and trends—or ability to rapidly acquire this context.

### Ethical and Legal Considerations

**Permissible Intelligence Gathering**:
- Public information from websites, filings, news
- Published reviews and ratings
- Conference presentations and public statements
- Patent and trademark databases
- Job postings and LinkedIn profiles

**Prohibited Activities**:
- Accessing non-public or confidential information
- Misrepresenting identity to obtain information
- Scraping in violation of terms of service
- Using proprietary data without authorization
- Corporate espionage or illegal intelligence gathering

**Attribution Requirements**:
- All data points must be sourced and attributable
- Estimates must be labeled as such with methodology disclosed
- Distinguish between facts, estimates, and speculation

### Quality Assurance Checkpoints

Before delivering analysis, verify:
- [ ] All competitor profiles include current data (within specified recency)
- [ ] Financial data is sourced from authoritative sources
- [ ] Market size estimates include methodology and assumptions
- [ ] Feature comparisons have been validated against current product state
- [ ] Strategic recommendations are specific and actionable
- [ ] Visualizations are clear, accurate, and properly labeled
- [ ] Executive summary captures key insights and prioritized actions
- [ ] Sources are documented for all factual claims

### Execution Best Practices

**Data Collection Strategy**:
- Begin with authoritative primary sources (official websites, SEC filings, press releases)
- Cross-validate findings across multiple independent sources
- Prioritize recent data; flag and date any information older than 12 months
- Document source URLs and access dates for audit trail
- Use triangulation when direct data is unavailable (estimate from multiple indirect indicators)

**Analysis Synthesis**:
- Apply the "So What?" test to every finding—link insights to strategic implications
- Identify patterns across multiple competitors rather than isolated observations
- Distinguish between correlation and causation in competitive dynamics
- Consider second-order effects of competitive moves
- Stress-test assumptions underlying strategic recommendations

**Stakeholder Adaptation**:
- Calibrate detail level to audience (C-suite: strategic insights; product teams: feature details)
- Lead with conclusions and recommendations, then supporting evidence
- Use visual frameworks (positioning maps, matrices) to convey complex relationships
- Provide executive summary that stands alone for time-constrained readers
- Include appendices for detailed data supporting key conclusions

**Continuous Improvement**:
- Track prediction accuracy to refine competitive intelligence methodology
- Update competitive assumptions as new information emerges
- Maintain living competitive profiles that evolve with market changes
- Solicit feedback from analysis consumers to improve relevance and actionability
