# Ratio Analysis

Comprehensive guide to calculating, interpreting, and applying financial ratios for evaluating company performance and financial health.

---

## Ratio Analysis Framework

### Purpose of Ratio Analysis

**Key Objectives**:
- Assess financial performance and position
- Compare companies of different sizes
- Identify trends over time
- Benchmark against peers and industry
- Support investment and credit decisions
- Diagnose operational problems

**Limitations**:
- Based on historical data
- Affected by accounting policies
- Industry-specific norms vary
- Ratios alone don't tell full story
- Can be manipulated (window dressing)
- Ignore qualitative factors

### Ratio Analysis Process

**Step 1: Calculate Ratios**
- Use consistent data sources
- Ensure comparability (same accounting methods)
- Calculate multiple periods for trends

**Step 2: Compare**
- Historical trends (3-5 years)
- Peer companies
- Industry averages
- Target benchmarks

**Step 3: Interpret**
- Identify strengths and weaknesses
- Understand drivers of performance
- Consider industry context
- Look for red flags

**Step 4: Investigate**
- Dig deeper into unusual ratios
- Read financial statement notes
- Consider qualitative factors
- Develop hypotheses about causes

**Step 5: Conclude**
- Synthesize findings
- Make recommendations
- Identify areas for further analysis

---

## Liquidity Ratios

### Current Ratio

```
Current Ratio = Current Assets / Current Liabilities
```

**Components**:
- *Current Assets*: Cash, marketable securities, accounts receivable, inventory, prepaid expenses
- *Current Liabilities*: Accounts payable, short-term debt, accrued expenses, current portion of long-term debt

**Interpretation**:
- **> 2.0**: Strong liquidity, may indicate excess working capital
- **1.5 - 2.0**: Adequate liquidity for most industries
- **1.0 - 1.5**: Acceptable but monitor closely
- **< 1.0**: Liquidity concerns, may struggle to pay obligations

**Industry Variations**:
- Retail: Often 1.5-2.0 (fast inventory turnover)
- Manufacturing: Often 2.0-3.0 (longer production cycles)
- Services: Can be lower (fewer current assets)

**Limitations**:
- Doesn't consider quality of current assets
- Inventory may not be easily liquidated
- Doesn't show timing of cash flows
- Can be manipulated near period-end

**Example Analysis**:

| Company | Current Assets | Current Liabilities | Current Ratio | Assessment |
|---------|---------------|---------------------|---------------|------------|
| A | $500M | $200M | 2.5 | Strong liquidity |
| B | $300M | $280M | 1.07 | Tight liquidity |
| C | $800M | $150M | 5.3 | Excess working capital? |

### Quick Ratio (Acid-Test Ratio)

```
Quick Ratio = (Current Assets - Inventory - Prepaid Expenses) / Current Liabilities

Or:
Quick Ratio = (Cash + Marketable Securities + Accounts Receivable) / Current Liabilities
```

**Rationale**: Excludes inventory (least liquid current asset) and prepaid expenses (not convertible to cash).

**Interpretation**:
- **> 1.5**: Very strong liquidity
- **1.0 - 1.5**: Good liquidity
- **0.5 - 1.0**: Adequate but monitor
- **< 0.5**: Liquidity concerns

**When Quick Ratio is More Useful**:
- Companies with slow-moving inventory
- Industries where inventory can become obsolete
- Distressed situations
- Seasonal businesses (off-season analysis)

**Quick vs. Current Ratio**:

```
If Quick Ratio << Current Ratio → Heavy reliance on inventory for liquidity
If Quick Ratio ≈ Current Ratio → Minimal inventory, strong liquid position
```

### Cash Ratio

```
Cash Ratio = (Cash + Marketable Securities) / Current Liabilities
```

**Interpretation**:
- **> 1.0**: Can pay all current liabilities immediately
- **0.5 - 1.0**: Strong cash position
- **0.2 - 0.5**: Adequate for most companies
- **< 0.2**: Low cash reserves

**Most Conservative**: Only includes most liquid assets.

**Use Cases**:
- Credit analysis (lender perspective)
- Distressed company analysis
- Companies in crisis
- Highly cyclical industries

### Working Capital Ratios

**Net Working Capital**:
```
NWC = Current Assets - Current Liabilities
```

**Working Capital Ratio**:
```
WC Ratio = Net Working Capital / Total Assets
```

**Interpretation**:
- Positive NWC: Company can cover short-term obligations
- Negative NWC: Potential liquidity issues (or efficient model like Dell)
- Increasing NWC: May indicate growing business or deteriorating collections
- Decreasing NWC: May indicate efficiency improvements or financial stress

**Working Capital Turnover**:
```
WC Turnover = Revenue / Average Net Working Capital
```

**Interpretation**: Higher ratio indicates more efficient use of working capital.

---

## Solvency Ratios

### Debt-to-Equity Ratio

```
Debt-to-Equity = Total Debt / Total Equity

Or:
Debt-to-Equity = (Short-term Debt + Long-term Debt) / Shareholders' Equity
```

**Interpretation**:
- **< 0.5**: Conservative capital structure
- **0.5 - 1.0**: Moderate leverage
- **1.0 - 2.0**: High leverage (industry-dependent)
- **> 2.0**: Very high leverage, increased financial risk

**Industry Benchmarks**:

| Industry | Typical D/E Range | Rationale |
|----------|------------------|----------|
| Utilities | 1.0 - 2.0 | Stable cash flows, capital intensive |
| Technology | 0.0 - 0.5 | Volatile cash flows, intangible assets |
| Real Estate | 1.5 - 3.0 | Asset-backed, stable rental income |
| Retail | 0.5 - 1.5 | Moderate capital needs |
| Manufacturing | 0.5 - 1.5 | Varies by sub-sector |

**Variations**:

*Total Debt-to-Equity*: Includes all interest-bearing debt
*Long-term Debt-to-Equity*: Excludes short-term debt
*Net Debt-to-Equity*: (Total Debt - Cash) / Equity

### Debt-to-Assets Ratio

```
Debt-to-Assets = Total Debt / Total Assets
```

**Interpretation**:
- **< 0.3**: Low leverage
- **0.3 - 0.6**: Moderate leverage
- **> 0.6**: High leverage

**Advantage**: Shows proportion of assets financed by debt (easier to interpret than D/E).

**Relationship to D/E**:
```
If D/A = 0.5, then D/E = 1.0
If D/A = 0.6, then D/E = 1.5
If D/A = 0.75, then D/E = 3.0
```

### Equity Multiplier

```
Equity Multiplier = Total Assets / Total Equity
```

**Interpretation**:
- **1.0**: No debt (all equity financing)
- **2.0**: Half debt, half equity
- **> 3.0**: High leverage

**Use**: Component of DuPont ROE analysis.

### Interest Coverage Ratio

```
Interest Coverage = EBIT / Interest Expense

Or:
Times Interest Earned (TIE) = EBIT / Interest Expense
```

**Interpretation**:
- **> 5.0**: Very strong ability to service debt
- **3.0 - 5.0**: Adequate coverage
- **2.0 - 3.0**: Acceptable but monitor
- **1.5 - 2.0**: Weak coverage, financial stress
- **< 1.5**: High distress risk, not covering interest

**Variations**:

*EBITDA Coverage*:
```
EBITDA Coverage = EBITDA / Interest Expense
```
More generous (adds back depreciation and amortization).

*Fixed Charge Coverage*:
```
Fixed Charge Coverage = (EBIT + Lease Payments) / (Interest + Lease Payments)
```
Includes lease obligations.

### Debt Service Coverage Ratio (DSCR)

```
DSCR = Operating Cash Flow / Total Debt Service

Where:
Total Debt Service = Principal Repayments + Interest Payments
```

**Interpretation**:
- **> 2.0**: Strong cash flow to service debt
- **1.5 - 2.0**: Adequate coverage
- **1.2 - 1.5**: Acceptable minimum
- **< 1.2**: Insufficient cash flow

**Lender Perspective**: Often require DSCR > 1.25 for loan approval.

**Advantage over Interest Coverage**: Includes principal repayments (actual cash requirement).

---

## Profitability Ratios

### Margin Analysis

**Gross Profit Margin**:
```
Gross Margin = (Revenue - COGS) / Revenue × 100%
            = Gross Profit / Revenue × 100%
```

**Interpretation**:
- Measures profitability before operating expenses
- Higher margin indicates pricing power or cost efficiency
- Compare to peers and historical trends

**Industry Variations**:
- Software: 70-90% (low COGS)
- Retail: 20-40% (high COGS)
- Manufacturing: 30-50% (moderate COGS)

**Operating Profit Margin**:
```
Operating Margin = Operating Income / Revenue × 100%
                 = EBIT / Revenue × 100%
```

**Interpretation**:
- Measures profitability from core operations
- Excludes interest and taxes
- Best for comparing operational efficiency

**Net Profit Margin**:
```
Net Margin = Net Income / Revenue × 100%
```

**Interpretation**:
- Bottom-line profitability
- Includes all expenses, interest, and taxes
- Most comprehensive profitability measure

**Margin Waterfall Analysis**:

| Margin Type | Company A | Company B | Insight |
|-------------|-----------|-----------|----------|
| Gross Margin | 40% | 35% | A has better pricing or lower COGS |
| Operating Margin | 15% | 12% | A has better operational efficiency |
| Net Margin | 10% | 8% | A has better overall profitability |

**Margin Trends**:
- **Expanding margins**: Improving efficiency, pricing power, or scale
- **Contracting margins**: Competitive pressure, rising costs, or inefficiency

### Return on Assets (ROA)

```
ROA = Net Income / Total Assets × 100%

Or:
ROA = Net Income / Average Total Assets × 100%
```

**Interpretation**:
- Measures profit generated per dollar of assets
- Higher ROA indicates more efficient asset utilization
- Compare to industry peers

**Typical Ranges**:
- **> 10%**: Excellent
- **5-10%**: Good
- **< 5%**: Poor (or capital-intensive industry)

**Industry Context**:
- Asset-light businesses (software, consulting): High ROA (15-30%)
- Capital-intensive businesses (utilities, manufacturing): Lower ROA (3-8%)

**ROA Decomposition**:
```
ROA = Net Margin × Asset Turnover
    = (Net Income / Revenue) × (Revenue / Assets)
```

This shows ROA is driven by:
- **Profitability** (Net Margin)
- **Efficiency** (Asset Turnover)

### Return on Equity (ROE)

```
ROE = Net Income / Shareholders' Equity × 100%

Or:
ROE = Net Income / Average Shareholders' Equity × 100%
```

**Interpretation**:
- Measures return to shareholders
- Key metric for equity investors
- Compare to cost of equity and peer ROEs

**Typical Ranges**:
- **> 20%**: Excellent
- **15-20%**: Good
- **10-15%**: Acceptable
- **< 10%**: Poor

**ROE vs. ROA**:
```
ROE = ROA × Equity Multiplier
    = ROA × (Assets / Equity)
```

Higher leverage increases ROE (but also risk).

### DuPont Analysis

**Three-Factor DuPont**:
```
ROE = Net Margin × Asset Turnover × Equity Multiplier
    = (Net Income/Revenue) × (Revenue/Assets) × (Assets/Equity)
```

**Five-Factor DuPont**:
```
ROE = (Net Income/EBT) × (EBT/EBIT) × (EBIT/Revenue) × (Revenue/Assets) × (Assets/Equity)
    = Tax Burden × Interest Burden × Operating Margin × Asset Turnover × Equity Multiplier
```

**DuPont Example**:

| Component | Company A | Company B | Insight |
|-----------|-----------|-----------|----------|
| Net Margin | 10% | 5% | A is more profitable |
| Asset Turnover | 1.5x | 3.0x | B is more efficient |
| Equity Multiplier | 2.0x | 2.0x | Same leverage |
| **ROE** | **30%** | **30%** | Same ROE, different drivers |

**Interpretation**:
- Company A: High-margin, low-turnover strategy (e.g., luxury goods)
- Company B: Low-margin, high-turnover strategy (e.g., discount retail)

### Return on Invested Capital (ROIC)

```
ROIC = NOPAT / Invested Capital × 100%

Where:
NOPAT = Net Operating Profit After Tax = EBIT × (1 - Tax Rate)
Invested Capital = Total Debt + Total Equity - Cash
                 = Operating Assets - Operating Liabilities
```

**Interpretation**:
- Measures return on all capital (debt + equity)
- Best for comparing companies with different capital structures
- Compare to WACC: ROIC > WACC indicates value creation

**ROIC vs. ROE**:
- ROIC: Unaffected by leverage
- ROE: Increases with leverage
- ROIC better for operational performance comparison

---

## Efficiency Ratios

### Asset Turnover

```
Asset Turnover = Revenue / Average Total Assets
```

**Interpretation**:
- Measures revenue generated per dollar of assets
- Higher ratio indicates more efficient asset utilization
- Varies significantly by industry

**Industry Benchmarks**:

| Industry | Typical Asset Turnover | Rationale |
|----------|----------------------|----------|
| Retail | 2.0 - 3.0x | Low asset base, high sales volume |
| Manufacturing | 0.8 - 1.5x | High fixed assets |
| Utilities | 0.3 - 0.5x | Very capital intensive |
| Software | 0.5 - 1.0x | Intangible assets |

**Fixed Asset Turnover**:
```
Fixed Asset Turnover = Revenue / Net Fixed Assets (PP&E)
```

Measures efficiency of fixed asset utilization.

### Inventory Turnover

```
Inventory Turnover = Cost of Goods Sold / Average Inventory
```

**Interpretation**:
- Number of times inventory is sold and replaced per year
- Higher ratio indicates faster inventory movement
- Lower ratio may indicate obsolete inventory or overstocking

**Days Inventory Outstanding (DIO)**:
```
DIO = 365 / Inventory Turnover
    = (Average Inventory / COGS) × 365
```

**Interpretation**: Average number of days inventory is held.

**Industry Variations**:

| Industry | Inventory Turnover | DIO | Rationale |
|----------|-------------------|-----|----------|
| Grocery | 15-20x | 18-24 days | Perishable goods |
| Auto Manufacturing | 8-12x | 30-45 days | Just-in-time production |
| Jewelry | 1-2x | 180-365 days | Slow-moving luxury items |
| Pharmaceuticals | 2-4x | 90-180 days | Long shelf life, regulatory |

**Red Flags**:
- Declining inventory turnover: Slowing sales or inventory buildup
- Very high turnover: Potential stockouts, lost sales

### Receivables Turnover

```
Receivables Turnover = Revenue / Average Accounts Receivable

Or (more conservative):
Receivables Turnover = Credit Sales / Average Accounts Receivable
```

**Interpretation**:
- Number of times receivables are collected per year
- Higher ratio indicates faster collections

**Days Sales Outstanding (DSO)**:
```
DSO = 365 / Receivables Turnover
    = (Average Accounts Receivable / Revenue) × 365
```

**Interpretation**: Average number of days to collect payment.

**Analysis**:
- Compare DSO to credit terms (e.g., if terms are "net 30", DSO should be ~30-40 days)
- Rising DSO: Collection problems, looser credit standards, or sales growth
- Falling DSO: Improved collections or tighter credit

**DSO Example**:

| Company | DSO | Credit Terms | Assessment |
|---------|-----|--------------|------------|
| A | 35 days | Net 30 | Acceptable |
| B | 65 days | Net 30 | Collection issues |
| C | 25 days | Net 30 | Excellent collections |

### Payables Turnover

```
Payables Turnover = Cost of Goods Sold / Average Accounts Payable

Or:
Payables Turnover = Purchases / Average Accounts Payable
```

**Days Payable Outstanding (DPO)**:
```
DPO = 365 / Payables Turnover
    = (Average Accounts Payable / COGS) × 365
```

**Interpretation**: Average number of days to pay suppliers.

**Analysis**:
- Higher DPO: Company taking longer to pay (using supplier financing)
- Lower DPO: Paying quickly (may be taking discounts or have weak negotiating position)
- Compare to industry norms and supplier terms

### Cash Conversion Cycle (CCC)

```
CCC = DIO + DSO - DPO
```

**Interpretation**:
- Number of days cash is tied up in operations
- Lower (or negative) CCC is better
- Measures working capital efficiency

**CCC Example**:

| Company | DIO | DSO | DPO | CCC | Assessment |
|---------|-----|-----|-----|-----|------------|
| A | 45 | 30 | 60 | 15 | Good |
| B | 90 | 60 | 30 | 120 | Poor - cash tied up |
| C | 5 | 2 | 30 | -23 | Excellent - negative CCC |

**Negative CCC**: Company collects from customers before paying suppliers (e.g., Dell, Amazon).

---

## Market Value Ratios

### Price-to-Earnings (P/E) Ratio

```
P/E Ratio = Stock Price / Earnings Per Share

Or:
P/E Ratio = Market Capitalization / Net Income
```

**Interpretation**:
- How much investors pay for each dollar of earnings
- Higher P/E may indicate growth expectations or overvaluation
- Lower P/E may indicate value opportunity or fundamental problems

**Typical Ranges**:
- **< 10**: Undervalued or distressed
- **10-20**: Fair value (mature companies)
- **20-30**: Growth premium
- **> 30**: High growth expectations or overvaluation

**Trailing vs. Forward P/E**:
- **Trailing P/E**: Based on past 12 months earnings
- **Forward P/E**: Based on estimated future earnings
- Forward P/E typically lower (assumes earnings growth)

**P/E Variations**:

*Normalized P/E*: Uses average earnings over business cycle
*Shiller P/E (CAPE)*: Uses 10-year average inflation-adjusted earnings

**Limitations**:
- Meaningless if earnings are negative
- Affected by accounting policies
- Doesn't consider growth rate
- Varies by industry

### PEG Ratio

```
PEG Ratio = P/E Ratio / Earnings Growth Rate
```

**Interpretation**:
- **< 1.0**: Potentially undervalued relative to growth
- **1.0**: Fair value
- **> 1.0**: Potentially overvalued relative to growth

**Example**:
- Company A: P/E = 30, Growth = 30% → PEG = 1.0 (fair)
- Company B: P/E = 30, Growth = 15% → PEG = 2.0 (expensive)
- Company C: P/E = 15, Growth = 30% → PEG = 0.5 (cheap)

**Limitations**:
- Growth rate estimates are uncertain
- Doesn't work for negative or zero growth
- Ignores risk differences

### Price-to-Book (P/B) Ratio

```
P/B Ratio = Stock Price / Book Value Per Share

Or:
P/B Ratio = Market Capitalization / Shareholders' Equity
```

**Interpretation**:
- **< 1.0**: Trading below book value (potential value)
- **1.0-3.0**: Typical range
- **> 3.0**: High premium to book value

**When P/B is Useful**:
- Asset-heavy businesses (banks, real estate)
- Distressed situations
- Value investing

**Limitations**:
- Book value is historical cost
- Intangible assets often not on balance sheet
- Less relevant for asset-light businesses

**Relationship to ROE**:
```
P/B = P/E × ROE
```

High ROE companies deserve high P/B ratios.

### Price-to-Sales (P/S) Ratio

```
P/S Ratio = Stock Price / Sales Per Share

Or:
P/S Ratio = Market Capitalization / Revenue
```

**Interpretation**:
- **< 1.0**: Low valuation
- **1.0-2.0**: Moderate valuation
- **> 2.0**: High valuation

**When P/S is Useful**:
- Unprofitable companies (P/E not applicable)
- Early-stage growth companies
- Comparing companies with different margins

**Limitations**:
- Ignores profitability
- Revenue doesn't equal value
- Varies widely by industry

### Enterprise Value Multiples

**Enterprise Value (EV)**:
```
EV = Market Cap + Total Debt - Cash
```

**EV/EBITDA**:
```
EV/EBITDA = Enterprise Value / EBITDA
```

**Advantages**:
- Capital structure neutral (includes debt)
- EBITDA is pre-interest, so matches EV
- Useful for comparing companies with different leverage

**Typical Ranges**:
- **< 8x**: Low valuation
- **8-12x**: Moderate valuation
- **> 12x**: High valuation

**EV/Sales**:
```
EV/Sales = Enterprise Value / Revenue
```

Useful for unprofitable companies, similar to P/S but capital structure neutral.

### Dividend Metrics

**Dividend Yield**:
```
Dividend Yield = Annual Dividend Per Share / Stock Price × 100%
```

**Interpretation**:
- Income return to shareholders
- Higher yield may indicate value or distress
- Compare to bond yields and peer companies

**Dividend Payout Ratio**:
```
Payout Ratio = Dividends / Net Income × 100%
```

**Interpretation**:
- **< 30%**: Conservative, room to grow dividend
- **30-60%**: Moderate, sustainable
- **> 60%**: High, limited flexibility
- **> 100%**: Unsustainable (paying more than earning)

---

## Integrated Ratio Analysis

### Ratio Relationships

Ratios are interconnected:

```
ROE = ROA × Equity Multiplier
ROA = Net Margin × Asset Turnover
P/B = P/E × ROE
EV/EBITDA ≈ P/E × (1 + Net Debt/Market Cap) / (1 - Tax Rate)
```

### Diagnostic Framework

**Problem: Declining ROE**

Investigate:
1. Net Margin (profitability issue?)
2. Asset Turnover (efficiency issue?)
3. Equity Multiplier (deleveraging?)

**Problem: High P/E Ratio**

Investigate:
1. Growth rate (PEG ratio)
2. ROE (justified by high returns?)
3. Risk (beta, volatility)
4. Peer comparison (industry-wide or company-specific?)

**Problem: Low Current Ratio**

Investigate:
1. Quick ratio (inventory issue?)
2. Cash conversion cycle (working capital efficiency?)
3. Trend (improving or deteriorating?)
4. Industry norms (acceptable for business model?)

### Red Flag Checklist

**Liquidity Red Flags**:
- [ ] Current ratio < 1.0
- [ ] Declining liquidity ratios
- [ ] Negative working capital (unless business model supports)
- [ ] Increasing DSO
- [ ] Decreasing DPO (paying faster, liquidity pressure?)

**Solvency Red Flags**:
- [ ] Interest coverage < 2.0x
- [ ] Debt-to-equity > 2.0x (industry-dependent)
- [ ] Increasing leverage ratios
- [ ] Negative equity
- [ ] Debt covenants at risk

**Profitability Red Flags**:
- [ ] Declining margins
- [ ] ROE < cost of equity
- [ ] ROIC < WACC
- [ ] Negative net income
- [ ] Margins below industry average

**Efficiency Red Flags**:
- [ ] Declining asset turnover
- [ ] Increasing inventory (without sales growth)
- [ ] Rising DSO
- [ ] Lengthening cash conversion cycle

**Market Value Red Flags**:
- [ ] P/E significantly above peers (without justification)
- [ ] Declining stock price despite stable earnings
- [ ] Dividend cuts
- [ ] Payout ratio > 100%

---

## Industry-Specific Considerations

### Banks and Financial Institutions

**Key Ratios**:
- **Net Interest Margin**: (Interest Income - Interest Expense) / Earning Assets
- **Efficiency Ratio**: Non-Interest Expense / (Net Interest Income + Non-Interest Income)
- **Loan-to-Deposit Ratio**: Total Loans / Total Deposits
- **Non-Performing Loan Ratio**: Non-Performing Loans / Total Loans
- **Tier 1 Capital Ratio**: Tier 1 Capital / Risk-Weighted Assets

### Retail

**Key Ratios**:
- **Same-Store Sales Growth**: Growth in stores open >1 year
- **Sales Per Square Foot**: Revenue / Retail Space
- **Inventory Turnover**: Critical for profitability
- **Gross Margin**: Key profitability driver

### Technology/SaaS

**Key Metrics**:
- **Customer Acquisition Cost (CAC)**: Sales & Marketing Expense / New Customers
- **Lifetime Value (LTV)**: Average Revenue Per Customer × Gross Margin % × Average Customer Life
- **LTV/CAC Ratio**: Should be > 3.0
- **Churn Rate**: Customers Lost / Total Customers
- **Rule of 40**: Revenue Growth % + Profit Margin % should exceed 40%

### Manufacturing

**Key Ratios**:
- **Capacity Utilization**: Actual Output / Maximum Possible Output
- **Inventory Turnover**: Critical for working capital
- **Fixed Asset Turnover**: Measures capital efficiency
- **Gross Margin**: Indicates pricing power and cost control
