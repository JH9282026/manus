---
name: policy-research-analysis
description: "Policy Research & Analysis is a rigorous analytical discipline focused on understanding, evaluating, and forecasting government policies, legislative developments, regulatory frameworks, and their impacts on organizations, industries, and society."
---

---
name: Policy Research & Analysis
description: Systematic methodology for analyzing government policies, legislation, regulatory frameworks, and public policy impacts to inform advocacy and compliance strategies.
---

# Policy Research & Analysis


## Overview

This section provides an overview of the skill.

## Skill Description and Purpose

Policy Research & Analysis is a rigorous analytical discipline focused on understanding, evaluating, and forecasting government policies, legislative developments, regulatory frameworks, and their impacts on organizations, industries, and society. This skill combines political science methodology, economic analysis, legal interpretation, and stakeholder mapping to support evidence-based policy engagement and compliance strategies.

The fundamental purpose is to navigate the complex interface between organizations and government by providing systematic intelligence on policy developments, rigorous analysis of policy impacts, and strategic recommendations for engagement. Policy research transforms complex legislative and regulatory landscapes into actionable intelligence that informs business strategy, risk management, and advocacy efforts.

Core methodological components include:
- **Legislative Analysis**: Tracking and interpreting proposed and enacted legislation
- **Regulatory Analysis**: Understanding agency rulemaking and enforcement patterns
- **Policy Impact Assessment**: Evaluating economic, social, and operational effects
- **Stakeholder Analysis**: Mapping interests, influence, and positions
- **Regulatory Forecasting**: Projecting policy trajectories and regulatory changes
- **Cost-Benefit Analysis**: Quantifying policy impacts and trade-offs
- **Comparative Policy Analysis**: Learning from policy approaches across jurisdictions

Deploy this skill when:
- Monitoring legislative developments affecting business operations
- Assessing regulatory compliance requirements and costs
- Evaluating policy proposals' potential business impact
- Developing government affairs and advocacy strategies
- Supporting policy positions with evidence-based analysis
- Understanding regulatory trends for strategic planning
- Conducting political risk assessment for market entry
- Informing ESG strategy with policy context

## Required Inputs/Parameters

### Primary Inputs

| Parameter | Format | Description | Required |
|-----------|--------|-------------|----------|
| `policy_domain` | Object | Policy area, sector, or issue under analysis | Yes |
| `geographic_scope` | Array | Jurisdictions to analyze (federal, state, local, international) | Yes |
| `analysis_objective` | Enum | "tracking", "impact_assessment", "forecasting", "advocacy_support" | Yes |
| `organization_context` | Object | Organization's operations, interests, and policy exposure | Yes |
| `time_horizon` | Object | Current state analysis and forward projection period | Yes |

### Legislative Tracking Parameters

| Parameter | Format | Description | Required |
|-----------|--------|-------------|----------|
| `bill_keywords` | Array | Terms for identifying relevant legislation | Conditional |
| `committee_focus` | Array | Congressional/parliamentary committees to monitor | No |
| `legislative_sponsors` | Array | Key legislators to track | No |
| `legislative_stage_filter` | Array | Stages of interest (introduced, committee, floor, enacted) | No |

### Regulatory Parameters

| Parameter | Format | Description | Required |
|-----------|--------|-------------|----------|
| `regulatory_agencies` | Array | Agencies whose actions to monitor | Conditional |
| `regulation_types` | Array | Rule types (proposed, final, guidance, enforcement) | No |
| `docket_tracking` | Array | Specific regulatory dockets to follow | No |
| `federal_register_keywords` | Array | Terms for Federal Register monitoring | No |

### Impact Assessment Parameters

| Parameter | Format | Description | Required |
|-----------|--------|-------------|----------|
| `impact_dimensions` | Array | Types of impact to assess (financial, operational, competitive) | Yes |
| `baseline_data` | Object | Current state data for impact comparison | Conditional |
| `affected_stakeholders` | Array | Groups to analyze for impact distribution | No |
| `scenario_assumptions` | Object | Assumptions for forward-looking impact estimates | No |

## Expected Outputs/Deliverables

### Primary Deliverables

1. **Policy Landscape Report** (40-80 pages)
   - Executive summary with key developments and implications
   - Regulatory environment overview and institutional mapping
   - Current policy state documentation
   - Pending legislation summary with probability assessment
   - Regulatory pipeline analysis
   - Stakeholder mapping and position analysis
   - Political dynamics and voting pattern analysis
   - Policy trajectory projections
   - Strategic recommendations with prioritization

2. **Legislative Tracking Database** (Structured data)
   - Comprehensive bill inventory including:
     - Bill number and title
     - Sponsor and co-sponsor list
     - Committee assignment and status
     - Key provisions summary
     - Probability of advancement assessment
     - Potential impact rating
     - Last action and next expected action
   - Amendment tracking and version comparison
   - Vote records and prediction models
   - Alert configuration for status changes

3. **Policy Impact Assessment** (Analytical report)
   - Impact methodology documentation
   - Quantitative impact estimates with ranges:
     - Compliance cost projections
     - Operational change requirements
     - Competitive effect analysis
     - Revenue/market impact estimates
   - Qualitative impact assessment
   - Affected stakeholder analysis
   - Scenario analysis under different policy outcomes
   - Recommendations for impact mitigation

### Regulatory Analysis Deliverables

4. **Regulatory Forecast Report**
   - Regulatory pipeline analysis by agency
   - Unified regulatory agenda interpretation
   - Enforcement trend analysis
   - Regulatory priority projections
   - Timeline estimates for pending rules
   - Comment period opportunities identification

5. **Compliance Analysis**
   - Regulatory requirement mapping
   - Gap analysis against current practices
   - Compliance cost estimation
   - Implementation timeline requirements
   - Enforcement risk assessment

### Advocacy Support Deliverables

6. **Stakeholder Analysis**
   - Stakeholder identification and categorization
   - Interest and position mapping
   - Influence assessment (formal and informal power)
   - Relationship mapping and coalition potential
   - Engagement strategy recommendations

7. **Policy Position Development**
   - Evidence compilation for policy positions
   - Economic impact data and analysis
   - Comparison with other jurisdictions
   - Counter-argument anticipation and response
   - Talking points and messaging frameworks

### Quality Standards

- All legislative tracking must use official government sources
- Impact estimates must document methodology and assumptions
- Probability assessments must provide basis for ratings
- Stakeholder positions must be verified through primary sources
- Forecasts must include uncertainty ranges and scenario variants
- All analysis must be non-partisan and evidence-based

## Example Use Cases

### Use Case 1: Technology Regulation Monitoring

**Scenario**: A technology company needs to monitor and assess data privacy legislation across US states and federal proposals to inform compliance strategy and advocacy priorities.

**Approach**:
- Configure tracking for privacy bills in 50 states and federal Congress
- Monitor FTC, state AG enforcement actions and guidance
- Analyze proposed requirements against current practices
- Estimate compliance costs for key provisions
- Map stakeholder positions (industry, advocates, legislators)
- Provide monthly tracking reports and quarterly strategic assessments

**Outcome**: Early identification of convergent state provisions enabled proactive compliance investment. Impact analysis informed advocacy prioritization, focusing resources on highest-impact provisions.

### Use Case 2: Environmental Policy Impact Assessment

**Scenario**: A manufacturing company faces proposed EPA regulations on emissions standards and needs to understand compliance requirements and costs to inform capital planning and advocacy response.

**Approach**:
- Analyze proposed rule text and regulatory impact analysis
- Model compliance costs for company facilities
- Assess competitive impacts across industry
- Develop comments for regulatory record
- Identify coalition partners for advocacy
- Project final rule timeline and potential modifications

**Outcome**: Compliance cost analysis ($45M over 5 years) informed capital budget planning. Submitted technical comments contributing to final rule modification reducing compliance burden by 20%.

### Use Case 3: Healthcare Policy Landscape

**Scenario**: A healthcare services company expanding into new states needs to understand state regulatory environments, licensure requirements, and policy trends affecting service delivery models.

**Approach**:
- Map state regulatory agencies and requirements for target states
- Analyze licensure and certification requirements
- Track legislation affecting service delivery models (telehealth, scope of practice)
- Assess enforcement patterns and regulatory climate
- Compare policy environments to inform market entry prioritization
- Monitor emerging policy trends affecting business model

**Outcome**: Regulatory analysis identified 3 states with favorable policy environment for market entry. Early identification of scope-of-practice legislation in target state enabled proactive engagement.

### Use Case 4: International Trade Policy Research

**Scenario**: A multinational corporation needs to monitor trade policy developments affecting supply chain and market access across key trading relationships.

**Approach**:
- Track US trade policy including tariffs, export controls, sanctions
- Monitor trade agreement negotiations and implementation
- Analyze other jurisdiction policies affecting market access
- Assess geopolitical risks affecting trade relationships
- Model tariff scenarios on supply chain costs
- Provide quarterly trade policy briefings

**Outcome**: Early warning of tariff changes enabled supply chain restructuring before implementation. Trade agreement analysis identified new market access opportunities worth $50M annually.

## Prerequisites or Dependencies

### Required Tools and Platforms

| Tool Category | Recommended Options | Purpose |
|---------------|---------------------|---------|
| Legislative Tracking | Congress.gov, FiscalNote, Bloomberg Government | Bill monitoring |
| Regulatory Tracking | Regulations.gov, FR.gov, state equivalents | Rule monitoring |
| Policy Research | CRS Reports, think tank publications | Policy analysis |
| Legal Research | Westlaw, LexisNexis | Statutory interpretation |
| News Monitoring | Politico Pro, CQ Roll Call | Political intelligence |
| Data Analysis | Excel, R, Stata | Impact modeling |

### Government Source Access

- Congress.gov for federal legislation
- Regulations.gov for federal rulemaking
- Federal Register for regulatory notices
- State legislature websites for state bills
- Government Accountability Office reports
- Congressional Budget Office analyses
- Agency regulatory agendas and guidance documents

### Domain Expertise Required

- **Policy Process**: Understanding of legislative and regulatory procedures
- **Legal Analysis**: Ability to interpret statutory and regulatory language
- **Economic Analysis**: Impact assessment and cost-benefit methodology
- **Political Analysis**: Understanding of political dynamics and stakeholder interests
- **Industry Knowledge**: Subject matter expertise in relevant policy areas
- **Research Methods**: Qualitative and quantitative policy research techniques

### Analytical Frameworks

- Regulatory Impact Analysis (RIA) methodology
- Cost-benefit analysis frameworks
- Stakeholder analysis and power mapping
- Policy cycle and process models
- Comparative policy analysis methods
- Political feasibility assessment

### Network and Access Requirements

- Government affairs professional networks
- Think tank and research institution relationships
- Industry association memberships
- Congressional staff and agency contact networks
- Lobbyist disclosure database access

### Resource Requirements

- Policy monitoring service subscriptions: $20,000-100,000+ annually
- Analyst time: varies by monitoring scope and depth
- Legal counsel for regulatory interpretation
- Economist support for impact quantification
- Government relations professional guidance
- Travel budget for Washington/capital engagement
