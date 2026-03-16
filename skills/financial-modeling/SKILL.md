---
name: financial-modeling
description: "Build financial models for valuation, forecasting, and decision-making. Use for: DCF analysis, scenario planning, financial projections, valuation models, budget forecasting, investment analysis, sensitivity analysis, and business case development."
---

# Financial Modeling

Build comprehensive financial models for valuation, forecasting, and strategic decision-making.

## Overview

Financial modeling is the process of creating mathematical representations of a company's financial performance to support decision-making, valuation, and planning. Models range from simple budget forecasts to complex discounted cash flow (DCF) valuations. This skill covers model types, building techniques, valuation methods, scenario analysis, and best practices for creating robust, flexible financial models.

## Model Types

### Three-Statement Model

**Components**:
1. **Income Statement**: Revenue, expenses, profit
2. **Balance Sheet**: Assets, liabilities, equity
3. **Cash Flow Statement**: Operating, investing, financing cash flows

**Purpose**: Foundation for most financial models
**Use Cases**: Company valuation, financial planning, credit analysis
**Time Horizon**: Typically 3-5 years

**Key Linkages**:
- Net income flows to retained earnings (balance sheet)
- Retained earnings affects equity (balance sheet)
- Changes in balance sheet items affect cash flow statement
- All three statements must balance

### Discounted Cash Flow (DCF) Model

**Purpose**: Determine intrinsic value of company or project

**Components**:
1. **Free Cash Flow Projection**: 5-10 years
2. **Terminal Value**: Value beyond projection period
3. **Discount Rate**: WACC (Weighted Average Cost of Capital)
4. **Present Value Calculation**: Discount all cash flows to today

**Formula**:
```
Enterprise Value = PV(Projected FCF) + PV(Terminal Value)

Terminal Value = Final Year FCF × (1 + g) / (WACC - g)
where g = perpetual growth rate
```

**Use Cases**: M&A valuation, investment decisions, fairness opinions

### Budget Model

**Purpose**: Plan and track financial performance

**Components**:
- Revenue forecast by product/segment
- Operating expenses by department
- Capital expenditures
- Cash flow projections
- Variance analysis (actual vs. budget)

**Time Horizon**: Annual, broken down monthly or quarterly
**Use Cases**: Annual planning, resource allocation, performance management

### Scenario and Sensitivity Analysis

**Purpose**: Understand impact of changing assumptions

**Scenario Analysis**:
- Base case (most likely)
- Best case (optimistic)
- Worst case (pessimistic)
- Custom scenarios

**Sensitivity Analysis**:
- One-way: Change one variable, observe impact
- Two-way: Change two variables simultaneously
- Data tables in Excel
- Tornado charts to show sensitivity

**Use Cases**: Risk assessment, strategic planning, investment decisions

### LBO Model (Leveraged Buyout)

**Purpose**: Analyze private equity acquisition

**Components**:
- Purchase price and financing structure
- Debt schedule and repayment
- Operating projections
- Exit assumptions
- Returns calculation (IRR, MOIC)

**Use Cases**: Private equity, M&A, leveraged transactions

## Building Financial Models

### Model Structure

**Best Practice Layout**:

**Tab 1: Assumptions**
- All key inputs in one place
- Clearly labeled and color-coded
- Organized by category
- Source documentation

**Tab 2: Historical Financials**
- 3-5 years of historical data
- Income statement, balance sheet, cash flow
- Basis for projections

**Tab 3: Projections**
- Forecast period (typically 5 years)
- Linked to assumptions
- Three financial statements
- Supporting schedules

**Tab 4: Valuation**
- DCF analysis
- Comparable company analysis
- Precedent transactions
- Valuation summary

**Tab 5: Sensitivity Analysis**
- Data tables
- Scenario comparisons
- Charts and graphs

**Tab 6: Executive Summary**
- Key outputs and conclusions
- Charts and visualizations
- Investment recommendation

### Excel Best Practices

**Formatting**:
- **Blue font**: Hard-coded inputs
- **Black font**: Formulas and calculations
- **Green font**: Links to other sheets/files
- Consistent number formatting
- Clear headers and labels

**Formula Best Practices**:
- Use cell references, not hard-coded numbers in formulas
- Keep formulas simple and auditable
- Use named ranges for key inputs
- Avoid circular references
- Document complex formulas with comments

**Structure**:
- One calculation per row when possible
- Consistent time periods across columns
- Use Excel tables for dynamic ranges
- Protect input cells from accidental changes
- Version control and change tracking

### Key Assumptions

**Revenue Drivers**:
- Unit volume and price
- Market size and share
- Growth rates
- Seasonality
- Customer acquisition and retention

**Cost Drivers**:
- Cost of goods sold (% of revenue or per unit)
- Operating expenses (fixed vs. variable)
- Headcount and compensation
- Marketing and sales expenses
- R&D spending

**Balance Sheet Assumptions**:
- Working capital (days sales outstanding, inventory turns, payables)
- Capital expenditures (% of revenue or specific projects)
- Depreciation and amortization
- Debt and interest rates

**Other Assumptions**:
- Tax rate
- Discount rate (WACC)
- Terminal growth rate
- Inflation rate

## Valuation Methods

### Discounted Cash Flow (DCF)

**Step 1: Project Free Cash Flow**
```
Free Cash Flow = EBIT × (1 - Tax Rate)
                 + Depreciation & Amortization
                 - Capital Expenditures
                 - Change in Net Working Capital
```

**Step 2: Calculate Terminal Value**
```
Terminal Value = Final Year FCF × (1 + g) / (WACC - g)

Or using exit multiple:
Terminal Value = Final Year EBITDA × Exit Multiple
```

**Step 3: Discount to Present Value**
```
PV = FCF / (1 + WACC)^n
where n = year number
```

**Step 4: Calculate Enterprise and Equity Value**
```
Enterprise Value = Sum of PV(FCF) + PV(Terminal Value)
Equity Value = Enterprise Value - Net Debt + Non-Operating Assets
```

### Comparable Company Analysis (Comps)

**Process**:
1. Identify comparable public companies
2. Calculate valuation multiples
3. Apply median/average multiple to target company

**Common Multiples**:
- EV/Revenue
- EV/EBITDA
- P/E (Price to Earnings)
- P/B (Price to Book)
- EV/EBIT

**Example**:
```
Comparable companies trade at average EV/EBITDA of 10x
Target company EBITDA = $50M
Implied Enterprise Value = $50M × 10 = $500M
```

### Precedent Transaction Analysis

**Process**:
1. Identify similar M&A transactions
2. Calculate transaction multiples
3. Apply to target company

**Considerations**:
- Control premium (typically 20-40%)
- Transaction timing and market conditions
- Strategic vs. financial buyers
- Synergies realized

## Scenario Analysis

### Building Scenarios

**Base Case**:
- Most likely outcome
- Reasonable assumptions
- Management guidance
- Historical trends

**Upside Case**:
- Optimistic but achievable
- Favorable market conditions
- Successful execution
- Typically 20-30% better than base

**Downside Case**:
- Pessimistic but realistic
- Adverse conditions
- Execution challenges
- Typically 20-30% worse than base

### Scenario Comparison

**Key Metrics to Compare**:
- Revenue and EBITDA
- Free cash flow
- Valuation (enterprise and equity value)
- Returns (IRR, ROI)
- Key ratios (margins, ROIC)

**Presentation**:
- Side-by-side comparison table
- Waterfall charts showing drivers
- Probability-weighted average
- Risk assessment

## Sensitivity Analysis

### One-Way Sensitivity

**Process**:
1. Select key variable (e.g., revenue growth rate)
2. Create range of values (e.g., -2% to +2%)
3. Calculate output for each value
4. Present in table or chart

**Example**:
```
Revenue Growth Rate | Enterprise Value
-2%                 | $450M
-1%                 | $475M
Base (0%)           | $500M
+1%                 | $525M
+2%                 | $550M
```

### Two-Way Sensitivity

**Process**:
1. Select two key variables (e.g., revenue growth and EBITDA margin)
2. Create data table with both variables
3. Calculate output for all combinations
4. Format as heat map

**Example Data Table**:
```
                    EBITDA Margin
Revenue Growth  |  15%    20%    25%
5%              | $400M  $450M  $500M
10%             | $450M  $500M  $550M
15%             | $500M  $550M  $600M
```

### Tornado Chart

**Purpose**: Show which variables have greatest impact on output

**Process**:
1. Vary each assumption by same percentage (e.g., ±10%)
2. Calculate impact on output
3. Rank by magnitude of impact
4. Display as horizontal bar chart

**Interpretation**: Focus on variables at top (highest impact) for further analysis and risk mitigation

## Model Validation

### Error Checking

**Balance Sheet Check**:
```
Assets = Liabilities + Equity
```

**Cash Flow Check**:
```
Ending Cash = Beginning Cash + Cash Flow from Operations + Investing + Financing
```

**Circular Reference Check**:
- Identify and resolve circular references
- Use iterative calculation if necessary
- Document circular logic

### Reasonableness Tests

**Growth Rates**:
- Compare to historical performance
- Industry benchmarks
- Market growth rates
- Achievability assessment

**Margins**:
- Gross margin trends
- Operating margin comparison to peers
- Margin expansion/contraction drivers

**Returns**:
- ROIC vs. WACC
- ROE vs. cost of equity
- Payback period reasonableness

### Sensitivity to Assumptions

**Test Key Assumptions**:
- What if revenue growth is 50% of projection?
- What if margins compress by 200 bps?
- What if WACC increases by 100 bps?

**Stress Testing**:
- Recession scenario
- Loss of major customer
- Competitive pressure
- Regulatory changes

## Advanced Techniques

### Monte Carlo Simulation

**Purpose**: Model probability distribution of outcomes

**Process**:
1. Define probability distributions for key variables
2. Run thousands of simulations
3. Analyze distribution of outputs
4. Calculate probability of outcomes

**Tools**: Excel add-ins (e.g., @RISK, Crystal Ball), Python, R

### Real Options Valuation

**Purpose**: Value flexibility and strategic options

**Types of Options**:
- Option to expand
- Option to abandon
- Option to delay
- Option to switch

**Use Cases**: R&D projects, natural resources, strategic investments

### Integrated Financial Planning

**Components**:
- Strategic plan (3-5 years)
- Annual budget
- Rolling forecasts (quarterly updates)
- Scenario planning
- KPI tracking

**Benefits**:
- Alignment across organization
- Continuous planning process
- Faster response to changes
- Better resource allocation

## Using the Reference Files

### When to Read Each Reference

**`/references/dcf-valuation-guide.md`** — Read when building DCF models, calculating WACC, determining terminal value, or performing company valuations.

**`/references/excel-modeling-techniques.md`** — Read when building complex models, learning advanced Excel functions, or optimizing model structure and performance.

**`/references/scenario-analysis-methods.md`** — Read when conducting scenario planning, sensitivity analysis, or risk assessment for investment decisions.

**`/references/valuation-multiples.md`** — Read when performing comparable company analysis, understanding industry-specific multiples, or benchmarking valuations.
