---
name: financial-modeling
description: "Build comprehensive financial models including three-statement models, DCF valuations, scenario analysis, and sensitivity analysis using Excel and best practices. Use for: creating integrated financial statements, performing discounted cash flow analysis, building valuation models, conducting scenario and sensitivity analysis, forecasting financial performance, evaluating investment opportunities, supporting M&A analysis, and making data-driven financial decisions."
---

# Financial Modeling

Build robust, professional financial models for valuation, forecasting, and strategic decision-making.

## Overview

This skill provides methodologies, techniques, and best practices for building financial models in Excel. It covers three-statement modeling, DCF valuation, scenario analysis, sensitivity analysis, and model design principles. Use these techniques to create accurate, transparent, and flexible financial models that support investment decisions, strategic planning, and business analysis.

## Model Type Selection Guide

| Purpose | Model Type | Complexity | Reference |
|---------|-----------|------------|----------|
| Forecast financial statements | Three-Statement Model | Medium | `/references/modeling-fundamentals.md` |
| Value a company or investment | DCF Valuation Model | High | `/references/valuation-methods.md` |
| Evaluate multiple outcomes | Scenario Analysis | Medium | `/references/scenario-analysis.md` |
| Test assumption sensitivity | Sensitivity Analysis | Medium | `/references/scenario-analysis.md` |
| Evaluate acquisition | M&A Model | High | `/references/valuation-methods.md` |
| Assess leveraged buyout | LBO Model | High | `/references/valuation-methods.md` |

## Financial Modeling Fundamentals

### Core Principles

**Accuracy**: Correct formulas, proper accounting treatment, validated assumptions, error checking

**Transparency**: Clear structure, documented assumptions, visible logic, easy to follow

**Flexibility**: Easy to update, scenario capability, modular design, scalable

**Efficiency**: Minimal manual inputs, reusable formulas, optimized calculations

### Model Design Best Practices

**Formatting Conventions** (Industry Standard):
- **Blue**: Hard-coded inputs and assumptions
- **Black**: Formulas and calculations
- **Green**: Links to other worksheets
- **Red**: Links to external files

**Consistency**:
- Units: Consistent scale (thousands, millions)
- Decimals: One for numbers, two for per-share, three for shares
- Column widths: Uniform across model
- Headers: Consistent labeling

**Formula Best Practices**:
- Simple and transparent (break complex calculations into steps)
- Avoid hard-coding numbers in formulas
- Use named ranges for key inputs
- IFERROR for error handling
- Consistent cell references

## Three-Statement Model

### Overview

The three-statement model integrates income statement, balance sheet, and cash flow statement to forecast financial performance. It's the foundation for most financial models.

### Key Components

**Income Statement**:
- Revenue forecast (top-down or bottom-up)
- COGS and gross margin
- Operating expenses (S&M, R&D, G&A)
- EBITDA
- Depreciation and amortization (from schedules)
- EBIT
- Interest expense (from debt schedule)
- Taxes
- Net income

**Balance Sheet**:
- Current assets (cash, AR, inventory)
- PP&E (from PP&E schedule)
- Current liabilities (AP, accrued expenses)
- Debt (from debt schedule)
- Shareholders' equity (retained earnings flow from income statement)
- Balance check: Assets = Liabilities + Equity

**Cash Flow Statement**:
- Operating activities (net income + adjustments - change in NWC)
- Investing activities (CapEx, acquisitions)
- Financing activities (debt, equity, dividends)
- Net change in cash

### Supporting Schedules

**PP&E Schedule**:
- Beginning PP&E + CapEx - Disposals = Ending PP&E
- Depreciation calculation
- Links to balance sheet and income statement

**Debt Schedule**:
- Beginning debt + borrowings - repayments = Ending debt
- Interest expense = Average debt × Interest rate
- Revolver as plug for cash shortfalls

**Working Capital Schedule**:
- AR = (Revenue / 365) × DSO
- Inventory = (COGS / 365) × DIO
- AP = (COGS / 365) × DPO

## DCF Valuation

### Overview

DCF analysis values a company based on present value of projected future cash flows. It's a fundamental valuation method.

### DCF Steps

**Step 1: Project Free Cash Flows**

Unlevered Free Cash Flow (UFCF):
```
UFCF = EBIT × (1 - Tax Rate) + D&A - CapEx - Change in NWC
```

Forecast period: Typically 5-10 years

**Step 2: Calculate Discount Rate (WACC)**

```
WACC = (E/V) × Re + (D/V) × Rd × (1 - Tc)
```

Cost of Equity (CAPM):
```
Re = Rf + β × (Rm - Rf)
```

**Step 3: Calculate Terminal Value**

Perpetuity Growth Method:
```
Terminal Value = FCFn × (1 + g) / (WACC - g)
```

Where g = perpetual growth rate (typically 2-3%)

**Step 4: Calculate Present Values**

```
PV(FCF) = Σ [FCFt / (1 + WACC)^t]
PV(TV) = TV / (1 + WACC)^n
Enterprise Value = PV(FCF) + PV(TV)
```

**Step 5: Calculate Equity Value**

```
Equity Value = Enterprise Value - Net Debt + Non-Operating Assets
Value per Share = Equity Value / Fully Diluted Shares
```

### DCF Best Practices

- Use realistic, defensible assumptions
- Terminal value should be 60-80% of EV
- Perpetual growth rate should not exceed GDP growth
- Conduct sensitivity analysis on WACC and terminal growth
- Compare to comparable company valuations
- Document all assumptions

## Comparable Company Analysis

### Overview

Values a company based on valuation multiples of similar publicly traded companies.

### Methodology

**Step 1: Select Comparables** (5-15 companies)
- Same industry and business model
- Similar size and geography
- Similar growth and profitability

**Step 2: Calculate Multiples**

Enterprise Value Multiples:
- EV/Revenue
- EV/EBITDA (most common)
- EV/EBIT

Equity Value Multiples:
- P/E (Price/Earnings)
- P/B (Price/Book)

**Step 3: Apply to Target**

```
Implied EV = Target EBITDA × Comparable EV/EBITDA Multiple
Equity Value = Implied EV - Net Debt + Non-Operating Assets
```

## Scenario and Sensitivity Analysis

### Scenario Analysis

Evaluate model outputs under different assumption sets:

**Base Case**: Most likely outcome (50-60% probability)
**Upside Case**: Favorable outcome (20-30% probability)
**Downside Case**: Unfavorable outcome (20-30% probability)

**Implementation**: Use CHOOSE function or scenario columns

### Sensitivity Analysis

**One-Way Sensitivity**: Vary one input, observe output impact
- Create data tables
- Tornado charts show relative impact

**Two-Way Sensitivity**: Vary two inputs simultaneously
- Common: WACC vs. Terminal Growth Rate
- Creates matrix of values

**Break-Even Analysis**: Find input value where output reaches threshold

## Model Quality Assurance

### Error Checking

**Balance Sheet Check**: Assets = Liabilities + Equity (should equal zero)
**Cash Flow Check**: Ending cash from CF statement = Cash on balance sheet
**Reasonableness Checks**: Margins, growth rates, ratios within industry norms

### Model Testing

- Test multiple scenarios
- Test extreme values
- Verify formulas (trace precedents/dependents)
- Historical validation
- Peer review

### Documentation

- Document all assumptions (source, rationale, date)
- Provide model instructions
- Version control (file naming, change log)
- Clear labeling throughout

## Using the Reference Files

### When to Read Each Reference

**`/references/modeling-fundamentals.md`** — Read when building three-statement models, setting up model structure, or learning fundamental modeling techniques. Contains detailed guidance on building integrated financial statements, working capital modeling, supporting schedules, and handling circularity.

**`/references/valuation-methods.md`** — Read when performing DCF valuations, comparable company analysis, precedent transaction analysis, or other valuation techniques. Includes comprehensive DCF methodology, WACC calculation, terminal value estimation, and multiple valuation approaches.

**`/references/scenario-analysis.md`** — Read when building scenario analysis, sensitivity analysis, or Monte Carlo simulations. Covers scenario design, implementation techniques, sensitivity tables, tornado charts, and probabilistic modeling.

**`/references/model-best-practices.md`** — Read when designing model structure, establishing formatting standards, or ensuring model quality. Provides detailed best practices for model design, formatting conventions, formula construction, error checking, and documentation standards.

## References

- [Model Best Practices](references/model-best-practices.md)
- [Modeling Fundamentals](references/modeling-fundamentals.md)
- [Scenario Analysis](references/scenario-analysis.md)
- [Valuation Methods](references/valuation-methods.md)
