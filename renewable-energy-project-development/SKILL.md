---
name: renewable-energy-project-development
description: "The Renewable Energy Project Development skill enables comprehensive development and analysis of renewable energy projects including solar photovoltaic, wind (onshore and offshore), and hydroelectric facilities."
---

# Renewable Energy Project Development

## Overview

This skill provides comprehensive guidance and best practices for this domain.

## Skill Description and Purpose

The Renewable Energy Project Development skill enables comprehensive development and analysis of renewable energy projects including solar photovoltaic, wind (onshore and offshore), and hydroelectric facilities. This skill encompasses project finance and capital structure, Power Purchase Agreement (PPA) negotiation, Levelized Cost of Energy (LCOE) analysis, grid integration and interconnection, regulatory incentives (ITC, PTC, tax credits), site selection and resource assessment, environmental permitting, construction and commissioning, and operations and maintenance (O&M) strategy.

This skill serves as the integrated development capability for renewable energy projects, transforming project concepts into financeable, constructible assets that deliver reliable clean energy generation. It applies industry-standard development practices, financial modeling techniques, and regulatory expertise to deliver professional-grade renewable project development outputs.

**Core Value Proposition:**
- Transforms project opportunities into bankable development packages
- Optimizes project economics through intelligent structuring and incentive capture
- Navigates complex regulatory and permitting requirements efficiently
- Secures long-term offtake through competitive PPA positioning
- Ensures project success through rigorous technical and financial analysis

**When to Use This Skill:**
- Evaluating new renewable energy project opportunities
- Developing project finance structures and securing capital
- Negotiating Power Purchase Agreements with offtakers
- Analyzing project economics and investment returns
- Planning grid interconnection and managing queue positions
- Identifying and capturing regulatory incentives and tax credits
- Conducting site selection and resource assessment
- Managing environmental permitting and regulatory approvals
- Planning construction execution and commissioning
- Developing O&M strategies for operating assets

## Required Inputs/Parameters

### Project Definition Inputs
| Parameter | Format | Description |
|-----------|--------|-------------|
| `technology_type` | Text | Project technology (solar PV, onshore wind, offshore wind, hydro, storage) |
| `project_size` | Numerical | Nameplate capacity (MW) and expected generation (MWh/year) |
| `site_information` | JSON/Document | Site location, acreage, land control status, and physical characteristics |
| `development_stage` | Text | Current development stage (greenfield, permitted, shovel-ready, construction-ready) |

### Resource and Technical Inputs
| Parameter | Format | Description |
|-----------|--------|-------------|
| `resource_data` | Time Series | Solar irradiance (GHI, DNI) or wind data (speed, direction) with temporal granularity |
| `technical_specifications` | JSON | Equipment specifications (panels, inverters, turbines) and system design |
| `grid_information` | Document | Interconnection point, transmission capacity, and queue status |
| `performance_estimates` | Numerical | Capacity factor, degradation rates, and availability assumptions |

### Financial and Market Inputs
| Parameter | Format | Description |
|-----------|--------|-------------|
| `capital_costs` | Structured | Development, EPC, and equipment cost estimates |
| `operating_costs` | Structured | O&M, insurance, land lease, and administrative cost estimates |
| `financing_assumptions` | JSON | Debt/equity mix, interest rates, loan terms, and tax equity parameters |
| `market_prices` | Time Series | Wholesale power prices and PPA pricing benchmarks |

### Regulatory and Incentive Inputs
| Parameter | Format | Description |
|-----------|--------|-------------|
| `incentive_eligibility` | Document | Applicable incentives (ITC, PTC, state programs, RECs) |
| `permitting_requirements` | Document | Required permits, environmental studies, and regulatory approvals |
| `interconnection_requirements` | Document | Utility interconnection standards and requirements |
| `tax_structure` | JSON | Federal and state tax rates, depreciation schedules, and tax credit parameters |

## Expected Outputs/Deliverables

### Project Development Plans
- **Development Schedule:** Comprehensive project timeline with milestones, critical path, and dependencies
- **Risk Register:** Development risks with probability, impact, and mitigation strategies
- **Site Selection Report:** Site evaluation with ranking, resource assessment, and development constraints
- **Development Budget:** Development phase costs including land, permitting, studies, and interconnection deposits

### Technical Analysis Outputs
- **Resource Assessment Report:** Detailed resource analysis with P50/P90 generation estimates and uncertainty quantification
- **Preliminary Engineering:** System design, equipment selection, and layout optimization
- **Grid Integration Study:** Interconnection feasibility, upgrade requirements, and cost allocation
- **Energy Production Estimate:** Annual generation forecast with degradation, losses, and availability adjustments

### Financial Analysis Deliverables
- **Financial Model:** Comprehensive project pro forma with detailed cash flows, returns, and sensitivities
- **LCOE Analysis:** Levelized cost calculation with component breakdown and competitive benchmarking
- **Investment Returns Analysis:** IRR, NPV, MOIC calculations for equity investors
- **Tax Equity Model:** Tax credit monetization analysis with investor returns and flip structures

### Commercial Documentation
- **PPA Term Sheet:** Proposed offtake terms including price, tenor, structure, and commercial terms
- **PPA Negotiation Strategy:** Positioning strategy with buyer analysis and negotiation approach
- **Offtake Market Analysis:** Assessment of PPA market, buyer landscape, and pricing dynamics
- **REC Strategy:** Renewable energy credit monetization approach and market analysis

### Regulatory and Permitting
- **Permitting Plan:** Required permits, responsible agencies, timeline, and cost estimates
- **Environmental Assessment:** Environmental impact summary with mitigation requirements
- **Incentive Optimization Plan:** Strategy for maximizing tax credits and incentive capture
- **Regulatory Compliance Framework:** Ongoing compliance requirements and monitoring approach

### Construction and Operations
- **EPC Strategy:** Contracting approach, contractor qualification, and risk allocation
- **Construction Schedule:** Construction timeline with milestones and commissioning plan
- **O&M Plan:** Operations strategy, maintenance program, and performance monitoring
- **Asset Management Framework:** Long-term asset management approach and value optimization

**Quality Standards:**
- All resource assessments must use industry-standard methodologies with uncertainty quantification
- Financial models must include detailed assumptions documentation and sensitivity analysis
- Development plans must be realistic with contingency provisions
- PPA terms must reflect current market conditions and competitive positioning

## Example Use Cases

### Use Case 1: Utility-Scale Solar Development
**Scenario:** A developer has secured site control for a 200 MW solar project in ERCOT and requires comprehensive development strategy from current greenfield status through financial close.

**Application:**
- Conduct preliminary site assessment including solar resource, topography, and access
- Analyze grid interconnection options and submit interconnection application
- Develop preliminary system design with equipment selection and layout optimization
- Prepare environmental assessment and identify permitting requirements
- Build financial model with capital costs, operating costs, and revenue assumptions
- Analyze PPA market and develop offtake strategy
- Structure tax equity financing with ITC monetization
- Calculate project returns under various scenarios
- Develop detailed development schedule and budget
- Prepare project prospectus for financing discussions

**Deliverables:** Site assessment report, interconnection application, preliminary engineering, environmental assessment, financial model, PPA strategy, tax equity structure analysis, development schedule and budget, investor presentation.

### Use Case 2: Offshore Wind Project Finance
**Scenario:** An offshore wind developer with fully permitted 800 MW project requires comprehensive project finance structuring to achieve financial close.

**Application:**
- Validate project assumptions including resource, costs, and schedule
- Develop detailed financial model suitable for lender review
- Structure capital stack with construction debt, term debt, and tax equity
- Analyze ITC election versus PTC and optimize tax structure
- Model debt sizing and coverage ratios
- Prepare lender presentation and information memorandum
- Develop due diligence document checklist
- Structure sponsor guarantees and credit support package
- Analyze interest rate and currency hedging requirements
- Model sensitivity analysis for lender scenarios

**Deliverables:** Bankable financial model, financing term sheet, lender presentation, information memorandum, due diligence checklist, sponsor support package, hedge strategy.

### Use Case 3: Corporate PPA Negotiation
**Scenario:** A renewable developer is negotiating a 15-year corporate PPA with a Fortune 500 company for a 100 MW wind project and requires comprehensive negotiation support.

**Application:**
- Analyze buyer's energy profile, sustainability goals, and procurement preferences
- Develop pricing analysis with market comparisons and project economics constraints
- Draft term sheet with proposed commercial terms
- Analyze PPA structures (physical, virtual/synthetic, sleeved) and recommend approach
- Model settlement mechanisms and basis risk
- Develop credit support framework appropriate for buyer profile
- Analyze accounting treatment implications for buyer
- Prepare negotiation strategy with priorities and fallback positions
- Model alternative scenarios and walk-away thresholds
- Draft PPA contract markup with key terms

**Deliverables:** Buyer analysis, pricing analysis, term sheet, structure recommendation, settlement analysis, credit framework, negotiation strategy, PPA markup.

### Use Case 4: Portfolio Repowering Analysis
**Scenario:** A wind portfolio owner with aging assets is evaluating repowering opportunities to extend asset life and capture new incentives.

**Application:**
- Assess current portfolio performance and remaining useful life
- Analyze repowering options (full repower, partial repower, technology upgrade)
- Evaluate new turbine technology and performance improvements
- Model repowering economics including capital costs and production uplift
- Analyze PTC eligibility and tax implications of repowering
- Assess interconnection impacts and upgrade requirements
- Evaluate offtake options (existing PPA modification, merchant, new PPA)
- Compare repowering returns to alternative uses of capital
- Develop prioritization framework for portfolio repowering
- Create implementation roadmap

**Deliverables:** Portfolio assessment, repowering options analysis, financial comparison model, PTC eligibility analysis, interconnection assessment, offtake strategy, prioritization matrix, implementation plan.

### Use Case 5: Battery Storage Integration
**Scenario:** A solar developer is evaluating co-location of battery storage with a 150 MW solar project to capture additional value streams and improve grid services.

**Application:**
- Analyze value stacking opportunities (energy arbitrage, capacity, ancillary services, solar smoothing)
- Model optimal battery sizing relative to solar capacity
- Evaluate battery technology options and degradation profiles
- Analyze incremental interconnection costs and benefits
- Model combined project economics with storage revenue streams
- Assess ITC eligibility and standalone storage charging requirements
- Evaluate merchant versus contracted revenue strategies
- Analyze operational complexity and O&M requirements
- Model integrated project returns versus solar-only alternative
- Develop offtake strategy for combined facility

**Deliverables:** Value stack analysis, sizing optimization, technology comparison, interconnection analysis, integrated financial model, ITC analysis, revenue strategy, operational plan.

## Prerequisites or Dependencies

### Technical Requirements
- **Resource Assessment Tools:** Solar resource databases (NSRDB, SolarAnywhere) and wind resource data (AWS Truepower, Vaisala)
- **Design Software:** PVsyst, System Advisor Model (SAM), or equivalent for energy modeling
- **Financial Modeling:** Excel-based project finance modeling with tax equity structures
- **GIS/Mapping Tools:** Site analysis, layout optimization, and environmental screening

### Knowledge Prerequisites
- **Renewable Technology:** Deep understanding of solar, wind, and storage technologies, performance characteristics, and design optimization
- **Project Finance:** Expertise in project finance structures, tax equity, and capital markets for renewable energy
- **Power Markets:** Knowledge of wholesale electricity markets, PPA structures, and merchant dynamics
- **Regulatory Framework:** Understanding of federal (ITC/PTC, FERC) and state (RPS, siting) regulatory requirements
- **Environmental Permitting:** Knowledge of NEPA, endangered species, wetlands, and other environmental requirements

### Data Dependencies
- **Resource Data:** High-quality solar or wind resource data for project location
- **Cost Data:** Current equipment pricing, EPC costs, and operating cost benchmarks
- **Market Data:** Wholesale power prices, PPA pricing, and REC market data
- **Incentive Information:** Current tax credit rates, phase-downs, and eligibility requirements

### Stakeholder Access
- **Landowners:** Relationships for land control and lease negotiation
- **Utilities:** Coordination with interconnecting utility for grid integration
- **Offtakers:** Access to potential PPA counterparties (utilities, C&I buyers)
- **Investors:** Relationships with tax equity providers and project finance lenders
- **Regulators:** Engagement with permitting agencies and regulatory bodies

### Integration Requirements
- **Legal Counsel:** Coordination with renewable energy legal specialists
- **Technical Advisors:** Access to independent engineers for third-party validation
- **Environmental Consultants:** Integration with environmental assessment firms
- **EPC Contractors:** Relationships with qualified EPC contractors for cost estimates
