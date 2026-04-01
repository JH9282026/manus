---
name: property-valuation-appraisal
description: "The Property Valuation & Appraisal skill enables comprehensive real estate valuation using professional appraisal methodologies including the income approach (direct capitalization and discounted cash flow), sales comparison approach, and cost approach."
---

# Property Valuation & Appraisal

## Overview

This skill provides comprehensive guidance and best practices for this domain.

## Skill Description and Purpose

The Property Valuation & Appraisal skill enables comprehensive real estate valuation using professional appraisal methodologies including the income approach (direct capitalization and discounted cash flow), sales comparison approach, and cost approach. This skill encompasses highest and best use analysis, market value determination, reconciliation of value indications, and appraisal report preparation in compliance with Uniform Standards of Professional Appraisal Practice (USPAP) and International Valuation Standards (IVS).

This skill serves as the authoritative valuation capability for real estate assets, providing credible, defensible value conclusions for various purposes including acquisitions, financing, financial reporting, litigation, and portfolio management. It applies rigorous analytical methodologies and professional standards to deliver valuation outputs suitable for institutional use.

**Core Value Proposition:**
- Provides credible, defensible property valuations using multiple approaches
- Ensures compliance with professional appraisal standards (USPAP, IVS)
- Delivers valuations suitable for lending, acquisition, and financial reporting purposes
- Reconciles multiple value indications into supportable conclusions
- Documents assumptions and methodology for transparency and auditability

**When to Use This Skill:**
- Determining market value for property acquisition or disposition
- Supporting financing with appraisal-based valuations
- Conducting valuations for financial reporting (GAAP fair value, IFRS)
- Performing valuations for litigation or dispute resolution
- Evaluating highest and best use for development or repositioning
- Mass appraisal for portfolio valuation or tax assessment
- Special purpose property valuation (hotels, healthcare, self-storage)

## Required Inputs/Parameters

### Subject Property Inputs
| Parameter | Format | Description |
|-----------|--------|-------------|
| `property_identification` | JSON/Structured | Legal description, address, parcel information, and property rights being appraised |
| `physical_description` | Document/JSON | Site characteristics, building specifications, condition assessment, and improvements |
| `income_data` | Structured Data | Current rent roll, lease terms, operating statements, and historical income/expense |
| `ownership_interest` | Text | Fee simple, leased fee, leasehold, or other property rights being valued |

### Market Data Inputs
| Parameter | Format | Description |
|-----------|--------|-------------|
| `comparable_sales` | List/JSON | Recent sales of similar properties with details (price, size, date, cap rate, adjustments needed) |
| `comparable_rentals` | List/JSON | Comparable lease transactions with rental rates, terms, and concessions |
| `market_conditions` | Document | Current market conditions including supply/demand, cap rate trends, and absorption |
| `cost_data` | Structured | Construction cost estimates, land sales, and depreciation factors |

### Valuation Parameters
| Parameter | Format | Description |
|-----------|--------|-------------|
| `valuation_purpose` | Text | Intended use (lending, acquisition, financial reporting, litigation, tax assessment) |
| `value_definition` | Text | Type of value being estimated (market value, investment value, liquidation value) |
| `effective_date` | Date | Date of value for the appraisal |
| `scope_of_work` | Document | Extent of research, analysis, and reporting appropriate for assignment |

### External Requirements
| Parameter | Format | Description |
|-----------|--------|-------------|
| `zoning_information` | Document | Current zoning, permitted uses, and development potential |
| `tax_assessment` | Data | Current assessed value and real estate tax information |
| `environmental_status` | Report | Environmental condition summary if applicable |
| `regulatory_factors` | Document | Rent control, historic designation, or other regulatory impacts |

## Expected Outputs/Deliverables

### Income Approach Outputs
- **Direct Capitalization Analysis:** NOI calculation, cap rate selection with market support, and indicated value via direct cap
- **Discounted Cash Flow Model:** Multi-year cash flow projections, discount rate derivation, terminal value calculation, and DCF value indication
- **Income Approach Reconciliation:** Weighting of direct cap and DCF indications with reasoning

### Sales Comparison Approach Outputs
- **Comparable Sales Grid:** Detailed adjustment grid with quantitative and qualitative adjustments
- **Adjustment Support:** Market-derived support for each adjustment category
- **Sales Comparison Value Indication:** Reconciled value from comparable sales analysis

### Cost Approach Outputs
- **Land Valuation:** Separate land value estimate using comparable land sales
- **Replacement Cost Estimate:** Detailed cost estimate using Marshall & Swift, RS Means, or contractor estimates
- **Depreciation Analysis:** Physical, functional, and external obsolescence calculations
- **Cost Approach Value Indication:** Land plus depreciated improvements value

### Reconciliation and Final Value
- **Value Reconciliation:** Analysis of all approach indications with weighting rationale
- **Final Value Conclusion:** Point estimate or value range with effective date
- **Extraordinary Assumptions and Limiting Conditions:** Documentation of any assumptions affecting value

### Appraisal Reports
- **Summary Appraisal Report:** Concise report format with essential analysis and conclusions
- **Self-Contained Appraisal Report:** Comprehensive narrative report with full analysis detail
- **Restricted Appraisal Report:** Limited report for client-only use with summary conclusions

**Quality Standards:**
- All valuations must comply with USPAP standards (or IVS for international properties)
- Market data must be verified with sources documented
- Adjustments must be market-derived and supportable
- Reconciliation must provide clear rationale for approach weighting
- Reports must include all required certifications and limiting conditions

## Example Use Cases

### Use Case 1: Office Building Acquisition Appraisal
**Scenario:** A lender requires independent appraisal for a Class A office building acquisition loan, requiring all three approaches to value with emphasis on income approach.

**Application:**
- Conduct property inspection and gather current rent roll, leases, and operating history
- Analyze highest and best use confirming current office use as maximally productive
- Income Approach: Calculate stabilized NOI, select market cap rate from recent transactions, apply direct capitalization; develop 10-year DCF model with market-derived discount rate
- Sales Comparison: Identify and verify 5-7 comparable office sales, apply adjustments for location, size, age, quality, and market conditions
- Cost Approach: Estimate land value from comparable sales, calculate replacement cost less depreciation
- Reconcile approaches with primary weight to income approach given income-producing property type
- Prepare self-contained appraisal report meeting lender requirements

**Deliverables:** Self-contained appraisal report with all three approaches, DCF model (Excel), comparable sales writeups, certification and limiting conditions.

### Use Case 2: Highest and Best Use Analysis
**Scenario:** A redevelopment site in a transitional urban area requires highest and best use analysis to determine optimal development program and land value.

**Application:**
- Analyze legally permissible uses under current zoning and potential rezoning
- Assess physical characteristics affecting development (topography, size, shape, access)
- Evaluate financially feasible alternatives through residual land value analysis
- Model alternative development scenarios (residential, mixed-use, commercial)
- Calculate implied land value under each scenario
- Determine maximally productive use based on highest residual value
- Value land based on concluded highest and best use

**Deliverables:** Highest and best use analysis, development scenario models, residual land value calculations, land value conclusion.

### Use Case 3: Portfolio Valuation for Financial Reporting
**Scenario:** A REIT requires quarterly fair value estimates for 50-property portfolio for GAAP financial reporting purposes.

**Application:**
- Develop standardized valuation templates by property type
- Gather updated income data and market metrics for each property
- Apply appropriate valuation methodology (primarily income approach with direct cap)
- Update cap rates based on current market transactions
- Document material changes from prior quarter
- Prepare valuation summary with aggregate portfolio value
- Document Level 2/Level 3 fair value hierarchy classification
- Provide quarterly and year-over-year value change analysis

**Deliverables:** Individual property valuation summaries (50), portfolio valuation summary, fair value hierarchy documentation, quarterly comparison analysis.

### Use Case 4: Litigation Support Valuation
**Scenario:** A condemnation proceeding requires expert valuation opinion on just compensation for partial taking of retail property by state transportation department.

**Application:**
- Value property "before" taking using all applicable approaches
- Analyze impact of partial taking on remaining property (severance damages)
- Consider any benefits to remainder from improved infrastructure
- Calculate just compensation (value taken plus severance damages less benefits)
- Prepare detailed narrative appraisal suitable for legal proceedings
- Document all assumptions and methodology for expert testimony
- Prepare exhibits and demonstratives for trial presentation

**Deliverables:** Before/after appraisal report, just compensation analysis, trial exhibits, expert report suitable for legal filing.

### Use Case 5: Automated Valuation Model Development
**Scenario:** A tax assessment authority requires mass appraisal model for annual property tax valuations across residential property universe.

**Application:**
- Compile comprehensive property database with characteristics and sales data
- Develop stratified sampling and market area delineation
- Build multiple regression models relating property characteristics to sales prices
- Calibrate models by property type and submarket
- Validate models using holdout samples and ratio studies
- Apply models to entire property universe
- Generate mass appraisal valuations with confidence intervals
- Document methodology for assessment appeal defense

**Deliverables:** AVM model documentation, ratio study results, property valuations database, methodology report for public disclosure.

## Prerequisites or Dependencies

### Technical Requirements
- **Valuation Software:** Access to valuation tools (Argus Enterprise for DCF, CoStar for market data, Marshall & Swift for cost)
- **Statistical Tools:** Regression analysis capabilities for mass appraisal and market extraction
- **Document Preparation:** Professional report formatting and presentation capabilities
- **Database Management:** Property data management for portfolio valuations

### Knowledge Prerequisites
- **Appraisal Theory:** Mastery of three approaches to value, reconciliation principles, and value concepts
- **Professional Standards:** Comprehensive knowledge of USPAP, IVS, and specialized standards (FIRREA for lending)
- **Market Analysis:** Proficiency in real estate market analysis and economic principles
- **Property Types:** Specialized knowledge for specific property types (commercial, residential, special purpose)
- **Financial Analysis:** Strong capabilities in DCF modeling, risk analysis, and financial mathematics

### Data Dependencies
- **Property Data:** Complete property information including legal, physical, and income characteristics
- **Sales Data:** Verified comparable sales with complete transaction details
- **Market Data:** Current market metrics including cap rates, rent levels, and vacancy rates
- **Cost Data:** Current construction cost data and land sales information

### Professional Requirements
- **Competency:** Demonstrated competency in specific property type and geographic area
- **Independence:** Compliance with independence requirements for intended use
- **Licensing:** Adherence to state licensing requirements where applicable
- **Continuing Education:** Current with professional development requirements

### Integration Requirements
- **Data Sources:** Integration with MLS, CoStar, public records, and other data providers
- **Cost Services:** Access to Marshall & Swift, RS Means, or equivalent cost data
- **GIS/Mapping:** Integration with mapping tools for location analysis
- **Document Systems:** Integration with client document management and delivery systems

## Using the Reference Files

- [Factors Affecting Value](./references/factors_affecting_value.md): Factors Affecting Value
- [Residential Vs Commercial](./references/residential_vs_commercial.md): Residential Vs Commercial
- [Standards Best Practices](./references/standards_best_practices.md): Standards Best Practices
- [Valuation Fundamentals Overview](./references/valuation_fundamentals_overview.md): Valuation Fundamentals Overview
- [Valuation Methods Techniques](./references/valuation_methods_techniques.md): Valuation Methods Techniques
