# DCF and Comparable Company Analysis

## DCF Model Construction

### Step 1: Project Free Cash Flow (5-10 years)

**Unlevered Free Cash Flow (UFCF)**
UFCF = EBIT × (1 - Tax Rate) + D&A - CapEx - Δ Net Working Capital

### Step 2: Calculate WACC

WACC = (E/V) × Re + (D/V) × Rd × (1 - t)

**Cost of Equity (CAPM)**
Re = Rf + β × (Rm - Rf) + Size Premium (optional)

| Input | Source | Typical Range |
|---|---|---|
| Risk-free rate (Rf) | 10-year Treasury yield | 3-5% |
| Equity risk premium (Rm-Rf) | Damodaran, Duff & Phelps | 5-7% |
| Beta (β) | Bloomberg, comparable companies | 0.5-2.0 |
| Size premium | Duff & Phelps | 0-5% for small caps |

**Cost of Debt**
Rd = Weighted average interest rate on outstanding debt, or yield on comparable rated bonds

### Step 3: Calculate Terminal Value

**Perpetuity Growth Method**
TV = UFCF_terminal × (1 + g) / (WACC - g)
- g = long-term sustainable growth rate (2-3% typical)
- Terminal value typically = 60-80% of total DCF value

**Exit Multiple Method**
TV = EBITDA_terminal × Selected EV/EBITDA Multiple

### Step 4: Discount and Bridge to Equity

1. Discount all FCFs and TV to present value using WACC
2. Sum = Enterprise Value
3. Enterprise Value - Net Debt - Preferred - Minority Interest = Equity Value
4. Equity Value / Diluted Shares = Implied Share Price

### DCF Sensitivity Table
Create two-variable data table:
- Rows: WACC range (±1-2%)
- Columns: Terminal growth rate range (1-4%)
- Values: Implied share price at each combination

---

## Trading Comparable Analysis

### Step 1: Select Comparable Companies
- Same industry sub-sector
- Similar business model and revenue mix
- Similar size (0.3x-3.0x revenue)
- Similar growth profile and margin structure
- Publicly traded with available data

### Step 2: Calculate Multiples

| Multiple | Formula | When to Use |
|---|---|---|
| EV/Revenue | Enterprise Value / Revenue | Pre-profit companies, SaaS |
| EV/EBITDA | Enterprise Value / EBITDA | Most common, operating comparison |
| EV/EBIT | Enterprise Value / EBIT | CapEx-intensive businesses |
| P/E | Stock Price / EPS | Profitable, stable companies |
| P/B | Stock Price / Book Value per Share | Financial institutions |
| EV/Subscriber | Enterprise Value / Subscribers | Subscription businesses |

### Step 3: Apply Multiples to Target
- Use median (or mean) of comparable set
- Apply premium/discount based on relative quality
- Premium for: Faster growth, higher margins, market leadership
- Discount for: Slower growth, lower margins, smaller scale

---

## Precedent Transaction Analysis

### Step 1: Identify Relevant Transactions
- Same or adjacent industry
- Similar deal size
- Recent (last 3-5 years preferred)
- Similar deal dynamics (strategic vs financial buyer)

### Step 2: Calculate Transaction Multiples
- EV/Revenue, EV/EBITDA at time of transaction
- Premium to unaffected share price (1-day, 30-day prior)

### Step 3: Interpret Premiums
- Average control premium: 25-40%
- Higher premiums for: Strategic synergies, competitive bidding
- Lower premiums for: Financial buyers, distressed targets
