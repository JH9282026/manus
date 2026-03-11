# Financial Modeling

Frameworks for financial analysis and modeling.

---

## Model Types

### Three-Statement Model

**Components**:
- Income Statement
- Balance Sheet
- Cash Flow Statement

**Linkages**:
- Net income flows to retained earnings
- CapEx appears on cash flow and accumulates on balance sheet
- Working capital changes link income statement to cash flow

### DCF Model

**Structure**:
1. Project free cash flows (5-10 years)
2. Calculate terminal value
3. Discount to present value
4. Calculate enterprise value
5. Bridge to equity value

**Key Inputs**:
| Input | Considerations |
|-------|----------------|
| Revenue Growth | Historical, market, competitive |
| Margins | Operating leverage, mix shift |
| CapEx | Maintenance vs growth |
| Working Capital | Turnover ratios |
| WACC | Risk-adjusted discount rate |
| Terminal Growth | Long-term sustainable growth |

### LBO Model

**Purpose**: PE perspective on acquisition returns

**Key Components**:
- Sources and uses of funds
- Debt schedule and paydown
- Operating projections
- Exit valuation
- Returns analysis (IRR, MOIC)

---

## Forecasting Approaches

### Revenue Forecasting

| Approach | Method |
|----------|--------|
| Top-Down | Market size × share = revenue |
| Bottom-Up | Units × price = revenue |
| Historical | Growth rates from history |
| Driver-Based | Key drivers × metrics |

### Cost Forecasting

| Cost Type | Modeling Approach |
|-----------|-------------------|
| Fixed | Flat or step-function |
| Variable | Percentage of revenue |
| Semi-Variable | Base + variable component |
| Headcount-Driven | FTEs × cost per FTE |

---

## Valuation Methodologies

### Comparable Company Analysis

**Process**:
1. Select peer companies
2. Gather trading data
3. Calculate multiples
4. Apply to target metrics

**Common Multiples**:
| Multiple | Calculation |
|----------|-------------|
| EV/Revenue | Enterprise value / Revenue |
| EV/EBITDA | Enterprise value / EBITDA |
| P/E | Price / Earnings per share |
| P/S | Price / Sales |

### Precedent Transactions

**Process**:
1. Identify relevant transactions
2. Calculate deal multiples
3. Adjust for market conditions
4. Apply to target

**Considerations**:
- Control premium (typically 20-40%)
- Synergy assumptions
- Market conditions at deal time

---

## Scenario Analysis

### Three-Case Framework

| Case | Assumptions |
|------|-------------|
| Base | Most likely outcome |
| Upside | Favorable assumptions |
| Downside | Adverse assumptions |

### Sensitivity Analysis

**Purpose**: Show impact of key variable changes

**Format**: Data tables showing output across input ranges

**Key Variables**:
- Revenue growth
- Margin assumptions
- Discount rate
- Exit multiple
- Terminal growth

---

## Model Best Practices

### Structure

| Practice | Application |
|----------|-------------|
| Separate tabs | Inputs, calculations, outputs |
| Color coding | Inputs (blue), formulas (black), links (green) |
| Clear labeling | Descriptive names, units |
| Version control | Date and version in filename |

### Formula Guidelines

- One formula per row/column
- Avoid hardcoding values
- Use named ranges for key inputs
- Document assumptions
- Build error checks
