# Financial Modeling Techniques

## Three-Statement Model Architecture

### Income Statement Build
1. **Revenue**: By segment with growth rate assumptions
2. **COGS**: Variable (% of revenue) + fixed components
3. **Gross Profit**: Revenue - COGS
4. **OpEx**: SG&A, R&D, D&A (each with growth assumptions)
5. **Operating Income (EBIT)**: Gross Profit - OpEx
6. **Interest**: Based on debt schedule
7. **Tax**: Effective tax rate × pre-tax income
8. **Net Income**: After interest and taxes

### Balance Sheet Build
1. **Working Capital**: AR (DSO), inventory (DIO), AP (DPO) driven by revenue/COGS
2. **PP&E**: Prior balance + CapEx - depreciation
3. **Intangibles**: Prior balance + acquisitions - amortization
4. **Debt**: Based on debt schedule (draws, repayments)
5. **Equity**: Prior balance + net income - dividends + share issuance

### Cash Flow Build
1. **Operating**: Net income + D&A + working capital changes
2. **Investing**: CapEx + acquisitions + asset sales
3. **Financing**: Debt issuance/repayment + equity + dividends
4. **Net Change**: Sum of all three sections
5. **Ending Cash**: Beginning cash + net change (links to balance sheet)

### Model Integrity Checks
- Balance sheet balances (Assets = Liabilities + Equity)
- Cash flow reconciles to balance sheet cash change
- Circular reference resolution (interest ↔ debt ↔ cash)
- Sensitivity tables function correctly
- All hard-coded assumptions clearly flagged

---

## Scenario Analysis

### Scenario Framework

| Scenario | Revenue Growth | Margin | Assumptions |
|---|---|---|---|
| Bull case | +20-30% | Expanding | Market tailwinds, successful execution |
| Base case | +10-15% | Stable | Management guidance, consensus |
| Bear case | 0-5% | Compressing | Economic headwinds, competitive pressure |
| Stress test | Negative | Declining | Recession, loss of key customer |

### Sensitivity Analysis
Create data tables showing how key outputs change with input variations:
- Revenue growth rate vs operating margin → Net income
- Revenue growth rate vs discount rate → DCF valuation
- Price per unit vs volume → Revenue
- Fixed costs vs variable costs → Break-even point

---

## DCF Valuation Framework

### Free Cash Flow Projection (5-10 years)
FCF = EBIT × (1 - tax rate) + D&A - CapEx - Δ Working Capital

### Terminal Value (Two Methods)
1. **Gordon Growth**: FCF_terminal × (1 + g) / (WACC - g)
   - g = long-term growth rate (typically 2-3%)
2. **Exit Multiple**: EBITDA_terminal × EV/EBITDA exit multiple

### Discount Rate (WACC)
WACC = E/(E+D) × Re + D/(E+D) × Rd × (1-t)
- Re (cost of equity) = Risk-free rate + β × equity risk premium
- Rd (cost of debt) = Weighted average interest rate on debt

### DCF Output
- Enterprise Value = PV of projected FCFs + PV of terminal value
- Equity Value = Enterprise Value - Net Debt
- Implied share price = Equity Value / Diluted shares outstanding
