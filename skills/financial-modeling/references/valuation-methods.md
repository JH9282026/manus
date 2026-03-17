# Valuation Methods

Comprehensive guide to DCF valuation, comparable company analysis, precedent transactions, and other valuation methodologies.

---

## Discounted Cash Flow (DCF) Valuation

### Overview

DCF analysis is a fundamental valuation method that estimates the intrinsic value of an investment based on its projected future cash flows, discounted to present value. It's based on the principle that an asset's value equals the present value of all future cash flows it will generate.

### DCF Methodology

#### Step 1: Project Free Cash Flows

**Unlevered Free Cash Flow (UFCF)** - Preferred Method:

**Formula**:
```
UFCF = EBIT × (1 - Tax Rate)
       + Depreciation & Amortization
       - Capital Expenditures
       - Change in Net Working Capital
```

**Alternative Calculation**:
```
UFCF = NOPAT
       + Depreciation & Amortization
       - Capital Expenditures
       - Change in Net Working Capital
```

Where NOPAT = Net Operating Profit After Tax = EBIT × (1 - Tax Rate)

**Why Unlevered?**:
- Independent of capital structure (debt/equity mix)
- Represents cash available to all investors (debt and equity)
- Allows valuation of operations separately from financing
- Consistent with WACC as discount rate

**Forecast Period**:
- Typically 5-10 years
- Long enough to reach steady state
- Short enough to forecast reasonably
- Industry and company-specific

#### Step 2: Calculate Discount Rate (WACC)

**Weighted Average Cost of Capital**:

**Formula**:
```
WACC = (E/V) × Re + (D/V) × Rd × (1 - Tc)
```

**Where**:
- E = Market value of equity
- D = Market value of debt
- V = E + D (total enterprise value)
- Re = Cost of equity
- Rd = Cost of debt
- Tc = Corporate tax rate

**Cost of Equity (Re) - CAPM**:

**Capital Asset Pricing Model**:
```
Re = Rf + β × (Rm - Rf)
```

**Components**:

**Risk-Free Rate (Rf)**:
- 10-year Treasury yield (most common)
- Current market rate
- Typically 3-5% (varies with market conditions)

**Beta (β)**:
- Measure of systematic risk
- Volatility relative to market
- Sources: Bloomberg, Capital IQ, Yahoo Finance
- Industry average if company-specific not available
- Typical range: 0.5-2.0

**Market Risk Premium (Rm - Rf)**:
- Expected return of market above risk-free rate
- Historical average: 5-7%
- Long-term equity premium
- Can vary by geography

**Example**:
- Rf = 4%
- β = 1.2
- Market Risk Premium = 6%
- Re = 4% + 1.2 × 6% = 11.2%

#### Step 3: Calculate Terminal Value

**Purpose**: Capture value beyond explicit forecast period

**Typically Represents**: 60-80% of total enterprise value

**Method 1: Perpetuity Growth Method** (Preferred):

**Formula**:
```
Terminal Value = FCFn × (1 + g) / (WACC - g)
```

**Where**:
- FCFn = Free cash flow in final forecast year
- g = Perpetual growth rate
- WACC = Discount rate

**Perpetual Growth Rate (g)**:
- Long-term sustainable growth rate
- Typically 2-3%
- Should not exceed long-term GDP growth
- Conservative assumption is prudent

#### Step 4: Calculate Present Values

**Present Value of Forecast Cash Flows**:

**Formula**:
```
PV(FCF) = Σ [FCFt / (1 + WACC)^t]
```

For t = 1 to n (forecast period)

**Present Value of Terminal Value**:

**Formula**:
```
PV(TV) = TV / (1 + WACC)^n
```

**Enterprise Value**:
```
Enterprise Value = PV(Forecast Cash Flows) + PV(Terminal Value)
```

#### Step 5: Calculate Equity Value

**Bridge from Enterprise Value to Equity Value**:

```
Equity Value = Enterprise Value
               - Net Debt
               + Non-Operating Assets
               - Minority Interests
               - Preferred Stock
```

**Net Debt**:
```
Net Debt = Total Debt - Cash and Cash Equivalents
```

**Value Per Share**:

```
Value Per Share = Equity Value / Fully Diluted Shares Outstanding
```

### DCF Best Practices

**Assumptions**:
- Base on thorough analysis
- Use historical trends
- Consider industry benchmarks
- Be conservative
- Document rationale

**Common Pitfalls**:
- Overly optimistic growth assumptions
- Terminal growth rate too high
- Incorrect WACC calculation
- Mismatched cash flows and discount rate
- Ignoring working capital requirements
- Unrealistic terminal value

---

## Comparable Company Analysis

### Overview

Comparable company analysis values a company based on valuation multiples of similar publicly traded companies.

### Methodology

#### Step 1: Select Comparable Companies

**Selection Criteria**:
- Same or similar industry
- Similar size
- Similar geography
- Similar growth profile
- Similar profitability

**Number of Comparables**: Typically 5-15 companies

#### Step 2: Calculate Valuation Multiples

**Enterprise Value Multiples**:

**EV/Revenue**:
```
EV/Revenue = Enterprise Value / Revenue
```

**EV/EBITDA**:
```
EV/EBITDA = Enterprise Value / EBITDA
```

**Equity Value Multiples**:

**Price/Earnings (P/E)**:
```
P/E = Market Cap / Net Income
```

#### Step 3: Apply Multiples to Target Company

**Valuation Calculation**:

**Using EV/EBITDA**:
```
Implied EV = Target EBITDA × Comparable EV/EBITDA Multiple
```

**Bridge to Equity Value**:
```
Equity Value = Implied EV - Net Debt + Non-Operating Assets
```

---

## Other Valuation Methods

### Precedent Transaction Analysis

Values a company based on multiples paid in recent acquisitions of similar companies.

### Leveraged Buyout (LBO) Analysis

Values a company based on returns required by financial sponsors in a leveraged buyout.

### Sum-of-the-Parts (SOTP) Valuation

Values a diversified company by valuing each business segment separately and summing them.
