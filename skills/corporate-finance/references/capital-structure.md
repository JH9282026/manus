# Capital Structure

Comprehensive guide to optimizing the mix of debt and equity financing to maximize firm value while managing financial risk.

---

## Theoretical Foundations

### Modigliani-Miller (MM) Theorem

**Proposition I (No Taxes)**:
In perfect capital markets, firm value is independent of capital structure.

```
V_L = V_U

Where:
- V_L = value of levered firm
- V_U = value of unlevered firm
```

**Proposition I (With Corporate Taxes)**:
Debt creates value through tax shields.

```
V_L = V_U + (Tc × D)

Where:
- Tc = corporate tax rate
- D = market value of debt
- (Tc × D) = present value of tax shield
```

**Proposition II (No Taxes)**:
Cost of equity increases linearly with leverage.

```
Re = Ru + (Ru - Rd) × (D/E)

Where:
- Re = cost of equity
- Ru = cost of equity for unlevered firm
- Rd = cost of debt
- D/E = debt-to-equity ratio
```

**Proposition II (With Taxes)**:
```
Re = Ru + (Ru - Rd) × (D/E) × (1 - Tc)
```

The tax shield reduces the rate at which cost of equity increases with leverage.

### Trade-off Theory

Firms balance the benefits and costs of debt to find optimal capital structure.

**Benefits of Debt**:
1. **Tax Shield**: Interest payments are tax-deductible
   - Annual tax benefit = Interest Expense × Tax Rate
   - PV of tax shield = Tc × D (if perpetual debt)

2. **Discipline Effect**: Debt commitments reduce free cash flow available for wasteful spending

3. **Lower Cost**: Debt is cheaper than equity (less risky for investors, tax-deductible)

**Costs of Debt**:
1. **Financial Distress Costs**:
   - Direct: Legal fees, bankruptcy costs, restructuring expenses
   - Indirect: Lost customers, supplier concerns, employee departures, fire-sale asset prices

2. **Agency Costs**:
   - Asset substitution (risk-shifting): Equity holders take excessive risks
   - Underinvestment: Firm passes up positive NPV projects because benefits go to debt holders
   - Debt overhang: Existing debt makes new financing difficult

3. **Loss of Financial Flexibility**: Limited ability to respond to opportunities or crises

**Optimal Capital Structure**: Point where marginal benefit of debt equals marginal cost

### Pecking Order Theory

Firms prefer financing sources in this order:
1. **Internal financing** (retained earnings)
2. **Debt**
3. **Equity** (last resort)

**Rationale**: Information asymmetry
- Managers know more about firm value than outside investors
- Issuing equity signals overvaluation
- Debt issuance is less negative signal
- Internal funds avoid information asymmetry entirely

**Implications**:
- Profitable firms use less debt (more retained earnings)
- Firms maintain financial slack for future investments
- No single optimal capital structure

### Market Timing Theory

Firms issue equity when stock prices are high and repurchase when low.

**Evidence**:
- Firms issue equity after stock price run-ups
- Capital structure reflects cumulative timing decisions
- Challenges notion of target capital structure

---

## Calculating Weighted Average Cost of Capital (WACC)

### WACC Formula

```
WACC = (E/V) × Re + (D/V) × Rd × (1 - Tc) + (P/V) × Rp

Where:
- E = market value of equity
- D = market value of debt
- P = market value of preferred stock
- V = E + D + P (total firm value)
- Re = cost of equity
- Rd = cost of debt
- Rp = cost of preferred stock
- Tc = corporate tax rate
```

### Step-by-Step WACC Calculation

**Step 1: Determine Market Values**

*Equity*:
```
Market Value of Equity = Share Price × Shares Outstanding
```

*Debt*:
- Use market value if bonds are traded
- If not traded, estimate using present value of future payments at current market rates
- Include all interest-bearing debt (bonds, bank loans, leases)

*Preferred Stock*:
```
Market Value = Preferred Share Price × Preferred Shares Outstanding
```

**Step 2: Calculate Cost of Equity (Re)**

*Method 1: Capital Asset Pricing Model (CAPM)*
```
Re = Rf + β × (Rm - Rf)

Where:
- Rf = risk-free rate (10-year Treasury yield)
- β = stock's beta (systematic risk)
- Rm = expected market return
- (Rm - Rf) = equity risk premium (historical average ~6-8%)
```

*Method 2: Dividend Discount Model (DDM)*
```
Re = (D1 / P0) + g

Where:
- D1 = expected dividend next year
- P0 = current stock price
- g = constant dividend growth rate
```

*Method 3: Bond Yield Plus Risk Premium*
```
Re = Rd + Risk Premium

Where:
- Risk Premium = typically 3-5% above firm's bond yield
```

**Step 3: Calculate Cost of Debt (Rd)**

*Method 1: Yield to Maturity (YTM)*
- Use YTM on firm's traded bonds
- Weight by market value if multiple bonds outstanding

*Method 2: Credit Rating Approach*
- Determine firm's credit rating
- Use average yield for that rating class

*Method 3: Synthetic Rating*
If no rated debt:
1. Calculate interest coverage ratio = EBIT / Interest Expense
2. Map to credit rating using standard tables
3. Use yield for that rating

**Step 4: Calculate Cost of Preferred Stock (Rp)**
```
Rp = Dp / P0

Where:
- Dp = preferred dividend per share
- P0 = current preferred stock price
```

**Step 5: Determine Weights**
```
Weight of Equity = E / V
Weight of Debt = D / V
Weight of Preferred = P / V

Where V = E + D + P
```

**Step 6: Apply Tax Rate**
- Use marginal corporate tax rate
- Only debt gets tax benefit (interest is deductible)

### WACC Example Calculation

**Given**:
- Market value of equity: $500 million
- Market value of debt: $200 million
- Cost of equity (CAPM): 12%
- Cost of debt (YTM): 6%
- Tax rate: 25%

**Calculation**:
```
V = $500M + $200M = $700M
E/V = $500M / $700M = 71.4%
D/V = $200M / $700M = 28.6%

WACC = (0.714 × 0.12) + (0.286 × 0.06 × 0.75)
     = 0.0857 + 0.0129
     = 0.0986 or 9.86%
```

---

## Optimal Capital Structure Analysis

### Factors Influencing Optimal Leverage

**Industry Characteristics**:
- **High leverage industries**: Utilities, real estate, telecommunications (stable cash flows, tangible assets)
- **Low leverage industries**: Technology, pharmaceuticals, consulting (volatile cash flows, intangible assets)

**Firm-Specific Factors**:

| Factor | Effect on Optimal Debt Level |
|--------|-----------------------------|
| Profitability | Negative (pecking order) / Positive (more tax shields) |
| Asset Tangibility | Positive (collateral value) |
| Growth Opportunities | Negative (underinvestment problem) |
| Firm Size | Positive (lower distress costs) |
| Cash Flow Volatility | Negative (higher distress risk) |
| Tax Rate | Positive (greater tax shield value) |
| Credit Rating | Positive (lower cost of debt) |

### Debt Capacity Analysis

**Step 1: Estimate Sustainable Debt Level**

Calculate maximum debt where firm can still service obligations:

```
Debt Capacity = (EBITDA × Coverage Multiple) / Interest Rate

Where:
- Coverage Multiple = minimum acceptable interest coverage ratio (typically 2.0-3.0x)
```

**Step 2: Stress Test**

Model debt service under adverse scenarios:
- Revenue decline of 20-30%
- Margin compression
- Recession conditions

**Step 3: Compare to Industry Benchmarks**

| Metric | Formula | Industry Comparison |
|--------|---------|--------------------|
| Debt/EBITDA | Total Debt / EBITDA | Compare to industry median |
| Debt/Equity | Total Debt / Total Equity | Compare to industry median |
| Interest Coverage | EBIT / Interest Expense | Should exceed 2.0x minimum |

### Target Capital Structure Framework

**Step 1: Analyze Current Structure**
- Calculate current leverage ratios
- Determine current WACC
- Assess financial flexibility

**Step 2: Benchmark Against Peers**
- Identify comparable companies
- Calculate median leverage ratios
- Understand industry norms

**Step 3: Evaluate Strategic Considerations**
- Growth plans and capital needs
- Acquisition strategy
- Dividend policy
- Cyclicality of business

**Step 4: Model Alternative Structures**

For each potential D/E ratio:
1. Calculate new WACC
2. Estimate firm value = FCF / WACC (simplified)
3. Assess financial distress probability
4. Evaluate financial flexibility

**Step 5: Select Target**
- Choose structure that maximizes firm value
- Ensure adequate financial flexibility
- Consider management risk tolerance

---

## Financing Decisions

### Debt vs. Equity Issuance Decision

**Issue Debt When**:
- Current leverage is below target
- Tax rate is high (maximize tax shield)
- Cash flows are stable and predictable
- Stock price is perceived as undervalued
- Maintaining control is important
- Interest rates are low

**Issue Equity When**:
- Current leverage is above target
- Financial distress risk is high
- Cash flows are volatile or uncertain
- Stock price is perceived as overvalued
- Debt covenants are restrictive
- Major growth opportunities require flexibility

### Types of Debt Instruments

| Instrument | Characteristics | Best Used When |
|------------|----------------|----------------|
| Bank Loans | Flexible, relationship-based, covenants | Smaller amounts, need flexibility |
| Corporate Bonds | Fixed terms, public markets, less flexible | Large amounts, established firms |
| Convertible Bonds | Lower coupon, converts to equity | Growth firms, uncertain outlook |
| Preferred Stock | Fixed dividend, no tax benefit, hybrid | Need flexibility, avoid dilution |
| Asset-Backed Securities | Secured by specific assets | Have quality receivables/assets |
| Mezzanine Debt | High yield, subordinated, warrants | Leveraged buyouts, growth capital |

### Debt Maturity Structure

**Short-Term Debt**:
- *Advantages*: Lower interest rates, flexibility
- *Disadvantages*: Refinancing risk, rollover risk
- *Best for*: Financing working capital, stable firms with good credit

**Long-Term Debt**:
- *Advantages*: Locked-in rates, no refinancing risk, matches asset life
- *Disadvantages*: Higher interest rates, less flexibility
- *Best for*: Financing long-term assets, uncertain credit conditions

**Maturity Matching Principle**:
- Finance long-term assets with long-term debt
- Finance short-term assets with short-term debt
- Reduces refinancing risk and interest rate risk

### Debt Covenants

**Affirmative Covenants** (must do):
- Maintain minimum financial ratios
- Provide regular financial statements
- Maintain insurance
- Pay taxes

**Negative Covenants** (must not do):
- Exceed maximum leverage ratios
- Pay dividends beyond specified limits
- Sell major assets without approval
- Issue additional debt with equal/higher priority

**Financial Covenants**:
- Minimum interest coverage ratio
- Maximum debt-to-EBITDA ratio
- Minimum current ratio
- Maximum capital expenditures

---

## Leverage Buyouts (LBOs)

### LBO Structure

Acquisition financed primarily with debt (typically 60-90% of purchase price).

**Capital Structure**:
1. **Senior Debt** (40-50%): Lowest cost, secured, strict covenants
2. **Subordinated Debt** (10-20%): Higher cost, unsecured
3. **Mezzanine Debt** (10-20%): Highest debt cost, often with warrants
4. **Equity** (10-40%): Sponsor equity, management equity

### LBO Returns Analysis

**Sources of Returns**:
1. **Operational Improvements**: EBITDA growth through revenue growth and margin expansion
2. **Deleveraging**: Debt paydown increases equity value
3. **Multiple Expansion**: Exit at higher valuation multiple than entry

**Return Calculation**:
```
MoIC (Multiple on Invested Capital) = Exit Equity Value / Initial Equity Investment

IRR = [(Exit Value / Entry Value)^(1/Years)] - 1
```

**Example**:
- Purchase price: $1,000M (70% debt, 30% equity = $300M equity)
- Exit after 5 years: $1,500M enterprise value
- Debt paid down to $400M
- Exit equity value: $1,500M - $400M = $1,100M
- MoIC: $1,100M / $300M = 3.7x
- IRR: (3.7)^(1/5) - 1 = 30%

---

## Recapitalization Strategies

### Leveraged Recapitalization

Firm issues debt to repurchase equity or pay special dividend.

**Objectives**:
- Return cash to shareholders
- Increase leverage to target level
- Defend against takeover
- Unlock value in underleveraged firm

**Process**:
1. Issue new debt
2. Use proceeds to repurchase shares or pay dividend
3. Increase leverage ratios
4. Benefit from increased tax shields

**Impact on Shareholders**:
- Immediate cash return
- Increased EPS (fewer shares)
- Higher financial risk
- Potential stock price increase if market views positively

### Deleveraging Strategies

**When to Deleverage**:
- Leverage exceeds target
- Financial distress risk is high
- Credit rating is threatened
- Need flexibility for growth investments

**Methods**:
1. **Debt Paydown**: Use excess cash flow
2. **Equity Issuance**: Dilutive but reduces risk
3. **Asset Sales**: Sell non-core assets
4. **Debt-for-Equity Swap**: Exchange debt for equity (distressed situations)

---

## International Considerations

### Cross-Border Capital Structure

**Factors Affecting International Leverage**:
- Tax rates and tax systems
- Legal and bankruptcy systems
- Financial market development
- Corporate governance standards
- Currency risk

**Subsidiary Capital Structure**:
- **Centralized**: Parent determines all subsidiary capital structures
- **Decentralized**: Each subsidiary optimizes independently
- **Hybrid**: Guidelines with local flexibility

### Currency Considerations

**Natural Hedging**:
- Match debt currency to revenue currency
- Reduces foreign exchange risk
- Example: European operations financed with Euro debt

**Currency Risk in Debt**:
- Foreign currency debt creates FX exposure
- Hedge with currency swaps or forwards
- Consider all-in cost including hedging

---

## Practical Implementation

### Capital Structure Adjustment Process

**Step 1: Determine Target**
- Analyze current structure
- Benchmark peers
- Model optimal structure
- Set target leverage ratios

**Step 2: Develop Transition Plan**
- Timeline for adjustment
- Financing actions required
- Covenant considerations
- Market timing

**Step 3: Execute**
- Issue/retire securities
- Communicate to stakeholders
- Monitor progress

**Step 4: Monitor and Adjust**
- Track leverage ratios
- Reassess target periodically
- Adjust for changing conditions

### Communication Strategy

**Key Stakeholders**:
- **Equity Investors**: Explain value creation rationale
- **Debt Investors**: Reassure on credit quality
- **Rating Agencies**: Provide detailed financial projections
- **Employees**: Address stability concerns
- **Customers/Suppliers**: Maintain confidence

**Disclosure Best Practices**:
- Clear rationale for capital structure decisions
- Detailed financial projections
- Sensitivity analysis
- Covenant compliance projections
- Use of proceeds
