---
name: oil-gas-industry-analysis
description: "The Oil & Gas Industry Analysis skill enables comprehensive analysis across the entire oil and gas value chain including upstream exploration and production (E&P), midstream transportation and storage, and downstream refining and marketing."
---

# Oil & Gas Industry Analysis

## Overview

This skill provides comprehensive guidance and best practices for this domain.

## Skill Description and Purpose

The Oil & Gas Industry Analysis skill enables comprehensive analysis across the entire oil and gas value chain including upstream exploration and production (E&P), midstream transportation and storage, and downstream refining and marketing. This skill encompasses reserves analysis and classification (1P, 2P, 3P), production economics and breakeven analysis, refining margins and crack spreads, energy transition and decarbonization strategies, commodity price forecasting (WTI, Brent), regulatory and environmental compliance, and industry trends analysis.

This skill serves as the integrated analytical capability for understanding and evaluating oil and gas investments, operations, and strategic positioning within the context of global energy markets and the energy transition. It applies industry-standard methodologies, financial analysis techniques, and market expertise to deliver professional-grade oil and gas analysis.

**Core Value Proposition:**
- Provides comprehensive industry analysis across the entire oil and gas value chain
- Enables rigorous evaluation of E&P assets and reserves
- Delivers actionable insights on production economics and breakeven analysis
- Supports strategic decision-making in the context of energy transition
- Integrates technical, financial, and market perspectives for holistic analysis

**When to Use This Skill:**
- Analyzing upstream E&P assets and acquisition opportunities
- Evaluating reserves and resource potential
- Conducting production economics and breakeven analysis
- Assessing midstream infrastructure investments
- Analyzing downstream refining economics and margins
- Forecasting crude oil and refined product prices
- Evaluating energy transition strategies and decarbonization pathways
- Assessing regulatory and environmental compliance requirements
- Analyzing industry trends and competitive dynamics

## Required Inputs/Parameters

### Upstream Analysis Inputs
| Parameter | Format | Description |
|-----------|--------|-------------|
| `asset_information` | JSON/Document | Field/basin characteristics, acreage, working interest, and net revenue interest |
| `reserves_data` | Structured | Reserves estimates (1P, 2P, 3P) by category with supporting engineering data |
| `production_data` | Time Series | Historical production volumes (oil, gas, NGLs) with decline curve data |
| `cost_data` | Structured | Lease operating expenses, capital costs, and well economics |

### Midstream Analysis Inputs
| Parameter | Format | Description |
|-----------|--------|-------------|
| `infrastructure_data` | JSON | Pipeline, storage, and processing facility characteristics and capacities |
| `contract_information` | Document | Throughput agreements, fee structures, and contract terms |
| `volume_data` | Time Series | Historical throughput volumes and utilization rates |
| `regulatory_information` | Document | FERC regulations, tariff structures, and permitting status |

### Downstream Analysis Inputs
| Parameter | Format | Description |
|-----------|--------|-------------|
| `refinery_configuration` | JSON | Refinery capacity, complexity, and process unit specifications |
| `crude_slate` | Structured | Input crude types, quality specifications, and sourcing |
| `product_yields` | Numerical | Product output percentages and specifications |
| `operating_metrics` | Structured | Utilization rates, turnaround schedules, and efficiency measures |

### Market and Financial Inputs
| Parameter | Format | Description |
|-----------|--------|-------------|
| `commodity_prices` | Time Series | Historical and forward prices (WTI, Brent, Henry Hub, refined products) |
| `financial_data` | Structured | Company financial statements and capital structure |
| `industry_benchmarks` | Document | Peer company metrics and industry averages |
| `macroeconomic_data` | Data | Global oil supply/demand, OPEC policy, and economic indicators |

## Expected Outputs/Deliverables

### Upstream Analysis Outputs
- **Reserves Evaluation Report:** Comprehensive reserves assessment with 1P/2P/3P classification, PV-10 valuation, and supporting documentation
- **Production Forecast:** Field-level production projections with decline curve analysis and type curve development
- **Breakeven Analysis:** Full-cycle and half-cycle breakeven calculations by play/basin with sensitivity analysis
- **E&P Asset Valuation:** Net asset value (NAV) analysis with multiple valuation methodologies

### Midstream Analysis Outputs
- **Infrastructure Assessment:** Capacity analysis, utilization forecasts, and expansion opportunities
- **Contract Analysis:** Revenue projections, contract renewal analysis, and counterparty assessment
- **Tariff and Fee Analysis:** Competitive positioning, rate case analysis, and margin projections
- **Midstream Valuation:** EBITDA-based valuation with distribution coverage and growth analysis

### Downstream Analysis Outputs
- **Refining Margin Analysis:** Crack spread analysis, margin forecasting, and capture rate evaluation
- **Operational Assessment:** Utilization optimization, turnaround planning, and efficiency benchmarking
- **Product Market Analysis:** Regional product demand, competitive supply, and pricing dynamics
- **Refining Asset Valuation:** Replacement cost, EBITDA multiple, and sum-of-parts valuation approaches

### Market and Industry Analysis
- **Commodity Price Forecast:** Oil and gas price projections with scenario analysis and key driver documentation
- **Supply/Demand Analysis:** Global and regional supply/demand balances with inventory assessment
- **Industry Trends Report:** Competitive dynamics, consolidation activity, and emerging themes
- **Energy Transition Assessment:** Decarbonization pathways, portfolio positioning, and transition risks

### Strategic Analysis
- **Portfolio Optimization:** Asset portfolio analysis with recommendations for additions and dispositions
- **M&A Analysis:** Target screening, transaction analysis, and synergy assessment
- **ESG and Sustainability Report:** Emissions profile, reduction strategies, and stakeholder reporting
- **Regulatory Compliance Assessment:** Current and emerging regulatory requirements with compliance strategies

**Quality Standards:**
- Reserves estimates must follow SEC/SPE standards with appropriate disclosure
- Price forecasts must include documented assumptions and scenario analysis
- Financial analysis must be grounded in auditable data with clear methodology
- Energy transition analysis must reflect current policy environment and technology trends

## Example Use Cases

### Use Case 1: E&P Acquisition Due Diligence
**Scenario:** A private equity firm is evaluating acquisition of a Permian Basin E&P company with proved reserves of 150 MMBOE and requires comprehensive due diligence support.

**Application:**
- Review and validate third-party reserves report with engineering assessment
- Analyze production data and develop independent decline curve analysis
- Evaluate drilling inventory and undeveloped acreage potential
- Build type curves for key development areas
- Develop production forecast for PDP, PDNP, and PUD categories
- Analyze operating costs and capital requirements
- Build full-cycle economics for development inventory
- Model cash flows and calculate NAV at various price scenarios
- Conduct breakeven analysis to stress test economics
- Assess organizational capabilities and operational risks
- Evaluate environmental liabilities and regulatory compliance

**Deliverables:** Reserves review report, production forecast, type curve analysis, full-cycle economics, financial model, NAV valuation, due diligence findings summary.

### Use Case 2: Refinery Margin Optimization
**Scenario:** An integrated oil company requires comprehensive analysis to optimize refining margins across its refining system in a challenging margin environment.

**Application:**
- Analyze current crude slate and sourcing strategy
- Evaluate crude quality impacts on yields and product values
- Model linear programming optimization for crude selection
- Analyze regional crack spreads and product margin drivers
- Benchmark utilization and operating costs against peers
- Identify capital projects with highest margin uplift potential
- Evaluate secondary unit optimization opportunities
- Assess turnaround scheduling optimization
- Model scenarios for crude price and product demand changes
- Develop margin enhancement action plan with prioritization

**Deliverables:** Crude slate analysis, LP optimization model results, margin benchmarking, capital project screening, turnaround analysis, margin enhancement roadmap.

### Use Case 3: Midstream MLP Valuation
**Scenario:** An investment bank requires comprehensive analysis of a midstream MLP for client advisory engagement involving potential take-private transaction.

**Application:**
- Analyze existing contract portfolio with revenue durability assessment
- Model volume forecasts based on producer activity in service area
- Evaluate re-contracting risk and commodity price sensitivity
- Assess expansion opportunity pipeline with capital requirements
- Analyze distribution coverage and sustainability
- Build DCF valuation with detailed cash flow model
- Apply trading comparables and precedent transaction analysis
- Evaluate take-private premium and financing capacity
- Model management projections versus consensus
- Develop LBO analysis with return sensitivities

**Deliverables:** Contract analysis, volume forecast, DCF model, trading comparables, precedent transactions, LBO model, valuation summary presentation.

### Use Case 4: Oil Price Scenario Planning
**Scenario:** A national oil company requires comprehensive oil price scenarios to inform budget planning, capital allocation, and strategic planning processes.

**Application:**
- Analyze global oil supply/demand fundamentals
- Assess OPEC+ policy dynamics and compliance
- Evaluate non-OPEC supply response at various price levels
- Model demand scenarios considering economic growth and EV adoption
- Analyze strategic petroleum reserve policies
- Develop three-price scenario set (base, high, low) with narrative
- Quantify key swing factors and their price impacts
- Build price probability distributions
- Map scenarios to corporate financial impacts
- Develop monitoring framework with scenario triggers

**Deliverables:** Supply/demand analysis, scenario documentation (3 scenarios), price probability analysis, corporate impact analysis, monitoring framework.

### Use Case 5: Energy Transition Strategy
**Scenario:** A major integrated oil company requires comprehensive energy transition strategy to position for decarbonization while maintaining shareholder returns.

**Application:**
- Baseline current emissions profile across operations (Scope 1, 2, 3)
- Analyze peer company transition strategies and commitments
- Evaluate low-carbon business opportunities (renewables, hydrogen, CCS, biofuels)
- Assess portfolio resilience under various carbon pricing scenarios
- Model capital allocation scenarios between traditional and transition businesses
- Analyze impact of transition strategies on financial metrics
- Evaluate organizational capabilities required for new businesses
- Develop stakeholder communication strategy
- Create emissions reduction pathway with interim targets
- Design portfolio evolution roadmap

**Deliverables:** Emissions baseline, peer benchmarking, opportunity assessment, scenario analysis, capital allocation framework, emissions reduction pathway, transition roadmap.

## Prerequisites or Dependencies

### Technical Requirements
- **Reserves Software:** Access to reserves estimation tools (ARIES, PHDWin, Harmony) or equivalent
- **Economic Modeling:** Excel-based or specialized economic analysis tools
- **LP Optimization:** Linear programming tools for refining optimization (if downstream analysis)
- **Market Data Platforms:** Access to oil and gas market data (Platts, Argus, EIA, IHS)

### Knowledge Prerequisites
- **Petroleum Engineering:** Understanding of reservoir engineering, decline curve analysis, and production operations
- **Reserves Standards:** Knowledge of SEC reserves definitions and SPE/PRMS classification
- **Refining Operations:** Understanding of refinery processes, crude quality impacts, and margin drivers
- **Energy Markets:** Expertise in crude oil, natural gas, and refined products markets
- **Financial Analysis:** Proficiency in oil and gas company valuation methodologies
- **Energy Transition:** Current understanding of decarbonization technologies, policies, and trends

### Data Dependencies
- **Production Data:** Historical production volumes, operating costs, and capital expenditures
- **Reserves Data:** Third-party reserves reports or engineering data for independent assessment
- **Financial Data:** Company financial statements, guidance, and analyst estimates
- **Market Data:** Commodity prices, crack spreads, and benchmark differentials
- **Industry Data:** EIA, IEA, OPEC, and other official data sources

### Stakeholder Access
- **Technical Teams:** Collaboration with reservoir engineering and operations personnel
- **Commercial Teams:** Coordination with commercial and trading functions
- **Finance Teams:** Integration with financial planning and investor relations
- **External Experts:** Access to independent petroleum engineers, consultants, and industry analysts

### Integration Requirements
- **Production Systems:** Access to production accounting and operations data
- **Financial Systems:** Integration with corporate financial reporting
- **Market Intelligence:** Connection to market data providers and news services
- **Regulatory Databases:** Access to SEC filings, FERC data, and regulatory information

## Using the Reference Files

- [./references/downstream-refining-petrochemicals.md](./references/downstream-refining-petrochemicals.md): Downstream Refining Petrochemicals
- [./references/industry-challenges-future.md](./references/industry-challenges-future.md): Industry Challenges Future
- [./references/market-trends-economics.md](./references/market-trends-economics.md): Market Trends Economics
- [./references/midstream-transportation-storage.md](./references/midstream-transportation-storage.md): Midstream Transportation Storage
- [./references/upstream-exploration-production.md](./references/upstream-exploration-production.md): Upstream Exploration Production
