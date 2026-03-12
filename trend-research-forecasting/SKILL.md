---
name: trend-research-forecasting
description: "Trend Research & Forecasting is a strategic intelligence capability that systematically identifies, analyzes, and projects emerging patterns, developments, and discontinuities that may significantly impact industries, markets, technologies, or societies."
---

---
name: Trend Research & Forecasting
description: Systematic methodologies for identifying emerging trends, conducting foresight analysis, and forecasting future developments across industries.
---

# Trend Research & Forecasting


## Overview

This section provides an overview of the skill.

## Skill Description and Purpose

Trend Research & Forecasting is a strategic intelligence capability that systematically identifies, analyzes, and projects emerging patterns, developments, and discontinuities that may significantly impact industries, markets, technologies, or societies. This skill combines environmental scanning, pattern recognition, analytical frameworks, and forecasting methodologies to help organizations anticipate change and make future-ready decisions.

The fundamental purpose is to reduce uncertainty about the future by transforming weak signals and emerging patterns into actionable strategic insights. Unlike prediction, which claims to know what will happen, trend research and forecasting maps possibility spaces, identifies drivers of change, and develops scenarios that enable adaptive strategy-making.

Core methodological approaches include:
- **Horizon Scanning**: Systematic monitoring of environments for emerging issues
- **Weak Signals Detection**: Identifying early indicators of potential trends
- **Trend Analysis Frameworks**: STEEP, PESTLE, and domain-specific analytical lenses
- **Scenario Planning**: Developing alternative future narratives
- **Forecasting Methods**: Delphi, time series analysis, regression, simulation
- **Trend Mapping**: Visual representation of trend landscapes and interconnections

Deploy this skill when:
- Developing long-term strategic plans (3-10 year horizons)
- Identifying market opportunities before competitors
- Assessing strategic risks and potential disruptions
- Informing product roadmap and innovation portfolios
- Understanding changing customer behaviors and expectations
- Anticipating regulatory and policy changes
- Making major capital investment decisions
- Developing organizational resilience capabilities

## Required Inputs/Parameters

### Primary Inputs

| Parameter | Format | Description | Required |
|-----------|--------|-------------|----------|
| `research_domain` | Object | Industry, sector, technology, or phenomenon to analyze | Yes |
| `time_horizon` | Object | Near-term (1-2 years), medium-term (3-5 years), long-term (5-10+ years) | Yes |
| `geographic_scope` | Array | Regions or markets of interest | Yes |
| `strategic_context` | Object | Organization's strategic priorities and decision context | Yes |
| `key_questions` | Array | Specific strategic questions to address | Yes |

### Framework Selection Parameters

| Parameter | Format | Description | Required |
|-----------|--------|-------------|----------|
| `analysis_framework` | Enum | "STEEP", "PESTLE", "three_horizons", "custom" | Yes |
| `forecasting_methods` | Array | Methods to apply (Delphi, time series, scenarios, etc.) | Yes |
| `scenario_count` | Integer | Number of scenarios to develop (typically 3-4) | Conditional |
| `quantitative_targets` | Array | Specific metrics requiring numerical forecasts | No |

### Data Source Parameters

| Parameter | Format | Description | Required |
|-----------|--------|-------------|----------|
| `primary_sources` | Array | Databases, publications, expert networks to monitor | Yes |
| `secondary_sources` | Array | News, social media, patents, academic literature | Yes |
| `expert_access` | Object | Access to subject matter experts for Delphi or interviews | Conditional |
| `historical_data` | Object | Time series data for quantitative forecasting | Conditional |

### STEEP/PESTLE Category Specifications

- **Social**: Demographics, lifestyles, values, consumer behavior, social movements
- **Technological**: Innovations, R&D, digital transformation, emerging tech
- **Economic**: GDP, inflation, employment, trade, investment patterns
- **Environmental**: Climate, sustainability, resources, regulations
- **Political**: Government policies, regulations, geopolitical dynamics
- **Legal**: Legislation, litigation, compliance requirements

## Expected Outputs/Deliverables

### Primary Deliverables

1. **Trend Landscape Report** (40-80 pages)
   - Executive summary with strategic implications
   - Environmental scan findings organized by STEEP/PESTLE categories
   - Trend identification with evidence assessment and maturity staging
   - Trend interconnections and reinforcing/balancing dynamics
   - Weak signals inventory with monitoring recommendations
   - Implications analysis specific to client context
   - Strategic recommendations prioritized by impact and certainty

2. **Trend Database** (Structured data file)
   - Individual trend profiles with standardized attributes:
     - Trend name and description
     - Category classification
     - Evidence sources and strength assessment
     - Maturity stage (emerging, growing, peaking, declining)
     - Geographic relevance
     - Impact potential (scale: 1-5)
     - Certainty level (scale: 1-5)
     - Time to mainstream adoption estimate
   - Tagging for cross-referencing and filtering
   - Links to source documentation

3. **Scenario Set** (Narrative and visual)
   - 3-4 distinct, plausible future scenarios
   - Scenario narratives (5-10 pages each) with:
     - Scenario title and defining characteristics
     - Key driving forces and their evolution
     - Timeline of developments
     - Implications for industry and organization
     - Early warning indicators
   - Scenario comparison matrix
   - Strategy robustness testing across scenarios

### Forecasting Deliverables

4. **Quantitative Forecasts** (if applicable)
   - Point forecasts with confidence intervals
   - Multiple model comparison (time series, regression, etc.)
   - Forecast accuracy metrics and validation
   - Sensitivity analysis on key assumptions
   - Visual forecast charts with historical context

5. **Delphi Study Results** (if applicable)
   - Expert panel composition and credentials
   - Round-by-round convergence analysis
   - Final consensus positions with rationale
   - Dissenting views and minority perspectives
   - Confidence and expertise self-assessments

### Monitoring Deliverables

6. **Horizon Scanning Protocol**
   - Ongoing monitoring framework with source list
   - Key indicator dashboards and alert thresholds
   - Weak signal tracking template
   - Regular update schedule and process

### Quality Standards

- All trends must be supported by minimum 3 independent evidence sources
- Scenarios must be internally consistent, plausible, and strategically relevant
- Quantitative forecasts must include uncertainty quantification
- Expert panels must include minimum 10 qualified participants
- All assumptions must be explicit and testable
- Contradictory evidence must be acknowledged and addressed

## Example Use Cases

### Use Case 1: Future of Work Strategic Planning

**Scenario**: A global professional services firm needs to understand how work patterns, skills requirements, and talent markets will evolve over the next decade to inform workforce strategy.

**Approach**:
- Conduct STEEP analysis focused on labor markets, technology, and organizational behavior
- Identify 35+ trends across categories including AI automation, gig economy, remote work, skill half-lives
- Develop 4 scenarios based on key uncertainties: automation speed × labor market flexibility
- Run Delphi study with 20 HR executives, futurists, and economists
- Map trend interconnections and identify reinforcing loops

**Outcome**: Delivered scenario set ("Augmented Workplace", "Gig Everything", "AI Displacement Crisis", "Human Premium") with distinct strategic implications. Informed $50M learning and development investment.

### Use Case 2: Electric Vehicle Market Forecasting

**Scenario**: An automotive supplier needs 10-year demand forecasts for EV components across key markets to guide manufacturing capacity investments.

**Approach**:
- Collect historical EV sales data across 15 markets (2015-2024)
- Identify demand drivers: policy (subsidies, mandates), technology (battery costs), infrastructure (charging networks)
- Build regression model with policy, economic, and technology variables
- Develop 3 scenarios: accelerated transition, baseline continuation, delayed adoption
- Validate models against analyst forecasts and announced OEM commitments

**Outcome**: Forecasted EV penetration reaching 45-70% of new sales by 2035 depending on scenario. Recommended capacity investment phased across scenarios with optionality.

### Use Case 3: Consumer Behavior Trend Scouting

**Scenario**: A CPG company wants to identify emerging consumer trends that could inform new product development and brand positioning.

**Approach**:
- Monitor 200+ sources including social media, influencers, startup activity, patent filings
- Apply weak signal methodology to detect early-stage behavioral shifts
- Categorize trends by consumer need state and relevance to portfolio
- Assess trend maturity and adoption curve positioning
- Identify "trend bundles" where multiple trends reinforce each other

**Outcome**: Identified 50+ emerging trends, prioritized 8 for immediate action. "Functional indulgence" trend bundle informed product line extension generating $25M in year-one sales.

### Use Case 4: Geopolitical Risk Scenario Analysis

**Scenario**: A multinational manufacturer needs to understand how geopolitical developments could impact global supply chain strategy over the next 5 years.

**Approach**:
- Map key geopolitical uncertainties: US-China relations, trade policy, regional conflicts
- Identify 25 political/economic trends with supply chain implications
- Develop 4 geopolitical scenarios based on globalization degree × great power relations
- Stress-test current supply chain against each scenario
- Identify resilience investments robust across multiple scenarios

**Outcome**: Scenario analysis revealed concentration risk in single-country sourcing. Recommended diversification strategy reducing exposure by 40% with moderate cost increase.

## Prerequisites or Dependencies

### Required Tools and Platforms

| Tool Category | Recommended Options | Purpose |
|---------------|---------------------|---------|
| Horizon Scanning | Feedly, Talkwalker, Meltwater | Source monitoring |
| Trend Databases | CB Insights, PitchBook, Gartner | Structured trend data |
| Forecasting Software | R (forecast package), Python (statsmodels), Tableau | Quantitative analysis |
| Scenario Tools | Futures Platform, Shell Scenarios, custom frameworks | Scenario development |
| Collaboration | Miro, MURAL, Notion | Workshop facilitation |
| Patent Analysis | Lens.org, Google Patents, PatSnap | Technology trends |

### Methodological Expertise Required

- **Environmental Scanning**: Systematic source monitoring and signal detection
- **Trend Analysis**: Pattern recognition, maturity assessment, impact evaluation
- **Scenario Planning**: Uncertainty identification, scenario construction, narrative development
- **Forecasting Techniques**: Time series, regression, Delphi, simulation
- **Systems Thinking**: Understanding interconnections and feedback loops
- **Strategic Analysis**: Translating trends into organizational implications

### Expert Network Requirements

- Access to subject matter experts for Delphi studies
- Industry analyst relationships for validation
- Academic researchers for theoretical grounding
- Practitioners for implementation perspectives
- Diverse geographic representation for global trends

### Data Requirements

- Historical time series data for quantitative forecasting (minimum 5 years)
- Access to premium trend databases and analyst reports
- Social media and news monitoring feeds
- Patent and academic publication databases
- Economic and demographic statistical sources

### Resource Requirements

- Analyst time: 4-12 weeks depending on scope
- Expert incentives for Delphi participation ($200-500 per expert)
- Database and monitoring tool subscriptions ($5,000-50,000 annually)
- Workshop facilitation costs for scenario development
- Ongoing monitoring resource allocation

### Epistemological Considerations

- Acknowledge inherent uncertainty in future projections
- Distinguish between forecasts (probabilistic projections) and predictions (claims of certainty)
- Embrace multiple perspectives and avoid single-point forecasts
- Continuously validate and update based on new information
- Document assumptions and confidence levels transparently
