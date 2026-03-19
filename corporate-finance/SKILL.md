---
name: corporate-finance
description: "Master corporate finance principles including capital structure optimization, capital budgeting decisions, working capital management, and corporate governance frameworks. Use for: evaluating investment projects using NPV/IRR/payback methods, optimizing debt-equity mix and cost of capital, managing cash conversion cycles and liquidity, analyzing dividend policies, structuring mergers and acquisitions, assessing financial risk and leverage, implementing governance best practices, and making strategic financing decisions for corporations."
---

# Corporate Finance

Master the financial decision-making framework for corporations including capital structure, investment analysis, and value creation strategies.

## Overview

Corporate finance focuses on how corporations make financial decisions to maximize shareholder value. This skill covers the three core areas: capital budgeting (investment decisions), capital structure (financing decisions), and working capital management (short-term financial operations). It provides frameworks for evaluating projects, optimizing financing mix, managing liquidity, and implementing governance structures that align management incentives with shareholder interests.

## Core Corporate Finance Framework

Corporate finance decisions follow a hierarchical structure:

| Decision Type | Key Question | Primary Tools | Time Horizon |
|--------------|--------------|---------------|-------------|
| Capital Budgeting | Which projects to invest in? | NPV, IRR, Payback Period | Long-term (3-10+ years) |
| Capital Structure | How to finance operations? | WACC, Debt/Equity ratios, MM Theorem | Medium-term (1-5 years) |
| Working Capital | How to manage daily operations? | Cash Conversion Cycle, Current Ratio | Short-term (days to 1 year) |
| Dividend Policy | How to return value to shareholders? | Payout ratios, Residual dividend model | Ongoing |

## Capital Budgeting Decision Framework

### Investment Evaluation Methods

**Net Present Value (NPV)** — The gold standard for investment decisions. Accept projects with NPV > 0.

```
NPV = Σ [Cash Flow_t / (1 + r)^t] - Initial Investment

Where:
- Cash Flow_t = expected cash flow in period t
- r = discount rate (typically WACC)
- t = time period
```

**Internal Rate of Return (IRR)** — The discount rate that makes NPV = 0. Accept projects where IRR > required return.

**Payback Period** — Time to recover initial investment. Simple but ignores time value of money and cash flows beyond payback.

**Profitability Index (PI)** — NPV per dollar invested. Useful for capital rationing: PI = (PV of future cash flows) / Initial Investment

### When to Use Each Method

| Scenario | Recommended Method | Rationale |
|----------|-------------------|----------|
| Single independent project | NPV | Most theoretically sound |
| Mutually exclusive projects | NPV (not IRR) | Avoids scale and timing issues |
| Capital rationing | Profitability Index | Maximizes value per dollar |
| Quick screening | Payback Period | Fast but use as preliminary filter only |
| Non-conventional cash flows | NPV (not IRR) | IRR can give multiple solutions |

## Capital Structure Optimization

### The Trade-off Theory

Optimal capital structure balances:
- **Benefits of Debt**: Tax shields (interest is tax-deductible), discipline on management
- **Costs of Debt**: Financial distress costs, agency costs, loss of financial flexibility

### Weighted Average Cost of Capital (WACC)

```
WACC = (E/V) × Re + (D/V) × Rd × (1 - Tc)

Where:
- E = market value of equity
- D = market value of debt
- V = E + D (total firm value)
- Re = cost of equity
- Rd = cost of debt
- Tc = corporate tax rate
```

### Cost of Equity Estimation

**Capital Asset Pricing Model (CAPM)**:
```
Re = Rf + β × (Rm - Rf)

Where:
- Rf = risk-free rate
- β = systematic risk (beta)
- Rm = expected market return
- (Rm - Rf) = market risk premium
```

**Dividend Discount Model (DDM)** for stable dividend-paying firms:
```
Re = (D1 / P0) + g

Where:
- D1 = expected dividend next period
- P0 = current stock price
- g = constant growth rate
```

## Working Capital Management

### Cash Conversion Cycle (CCC)

Measures how long cash is tied up in operations:

```
CCC = DIO + DSO - DPO

Where:
- DIO = Days Inventory Outstanding = (Inventory / COGS) × 365
- DSO = Days Sales Outstanding = (Accounts Receivable / Revenue) × 365
- DPO = Days Payable Outstanding = (Accounts Payable / COGS) × 365
```

**Goal**: Minimize CCC while maintaining operational efficiency
- Reduce DIO: Improve inventory turnover
- Reduce DSO: Accelerate collections
- Increase DPO: Negotiate better payment terms (without damaging supplier relationships)

### Liquidity Management

| Ratio | Formula | Healthy Range | Interpretation |
|-------|---------|---------------|----------------|
| Current Ratio | Current Assets / Current Liabilities | 1.5 - 3.0 | Ability to pay short-term obligations |
| Quick Ratio | (Current Assets - Inventory) / Current Liabilities | 1.0 - 2.0 | Liquidity without selling inventory |
| Cash Ratio | Cash / Current Liabilities | 0.5 - 1.0 | Most conservative liquidity measure |

## Dividend Policy Framework

### Dividend Policy Types

| Policy Type | Description | Best For |
|------------|-------------|----------|
| Stable Dollar | Fixed dollar amount per share | Mature, stable cash flow companies |
| Constant Payout Ratio | Fixed % of earnings | Companies with volatile earnings |
| Residual Dividend | Pay dividends from leftover cash after funding projects | Growth companies with variable investment needs |
| Low Regular + Extra | Base dividend plus special dividends | Companies with cyclical cash flows |

### Dividend vs. Share Repurchase

**Dividends**:
- Commit to ongoing payments
- Signal financial strength and stability
- Preferred by income-focused investors
- Less flexible (cutting dividends sends negative signal)

**Share Repurchases**:
- More flexible (no commitment)
- Tax-efficient for shareholders (capital gains vs. dividend income)
- Signal management believes stock is undervalued
- Can be used to adjust capital structure

## Mergers & Acquisitions Framework

### Valuation Methods for M&A

| Method | Approach | Best Used When |
|--------|----------|----------------|
| DCF Analysis | Discount projected cash flows | Target has predictable cash flows |
| Comparable Companies | Multiple-based (P/E, EV/EBITDA) | Similar public companies exist |
| Precedent Transactions | Multiples from past deals | Recent comparable transactions available |
| Asset-Based | Sum of asset values | Target is asset-heavy or distressed |

### Synergy Analysis

**Revenue Synergies**:
- Cross-selling opportunities
- Market expansion
- Pricing power

**Cost Synergies**:
- Economies of scale
- Elimination of duplicate functions
- Improved procurement

**Financial Synergies**:
- Lower cost of capital
- Tax benefits
- Increased debt capacity

### Deal Structure Considerations

| Structure | Payment Method | Tax Treatment | Risk Allocation |
|-----------|---------------|---------------|------------------|
| Stock-for-Stock | Acquirer shares | Tax-deferred for target shareholders | Shared (target shareholders become owners) |
| Cash | Cash payment | Taxable event | Acquirer bears all risk |
| Mixed | Cash + Stock | Partially taxable | Balanced |

## Financial Risk Management

### Types of Financial Risk

**Market Risk**: Changes in market prices (interest rates, FX, commodities)
**Credit Risk**: Counterparty default
**Liquidity Risk**: Inability to meet short-term obligations
**Operational Risk**: Internal process failures

### Leverage Metrics

| Metric | Formula | Interpretation |
|--------|---------|----------------|
| Debt-to-Equity | Total Debt / Total Equity | Financial leverage |
| Debt-to-Assets | Total Debt / Total Assets | Asset financing structure |
| Interest Coverage | EBIT / Interest Expense | Ability to service debt |
| Debt Service Coverage | Operating Cash Flow / Total Debt Service | Cash available for debt payments |

**Financial Distress Signals**:
- Interest coverage < 2.0x
- Debt-to-equity > 2.0x (varies by industry)
- Negative operating cash flow
- Declining current ratio
- Increasing CCC

## Corporate Governance Principles

### Agency Problem Framework

Conflict between:
- **Principals** (shareholders) want: Maximize firm value
- **Agents** (managers) may want: Job security, perks, empire building

### Governance Mechanisms

| Mechanism | How It Works | Effectiveness |
|-----------|--------------|---------------|
| Board of Directors | Independent oversight and strategic guidance | High if truly independent |
| Executive Compensation | Align pay with performance (stock options, bonuses) | Moderate (can be gamed) |
| Market for Corporate Control | Threat of takeover disciplines management | High but disruptive |
| Large Shareholders | Active monitoring and engagement | High for institutional investors |
| Debt Covenants | Restrict management actions | High but can limit flexibility |

### Best Practices

1. **Board Independence**: Majority of directors should be independent
2. **Separation of CEO/Chairman**: Reduces concentration of power
3. **Executive Compensation**: Tie to long-term performance metrics
4. **Transparency**: Regular, detailed financial reporting
5. **Shareholder Rights**: Enable proxy voting, shareholder proposals
6. **Audit Committee**: Independent financial oversight

## Valuation Fundamentals

### Enterprise Value vs. Equity Value

```
Enterprise Value (EV) = Market Cap + Debt - Cash
Equity Value = Market Capitalization = Share Price × Shares Outstanding
```

**Use EV** for operating comparisons (EV/EBITDA, EV/Revenue)
**Use Equity Value** for shareholder-specific metrics (P/E, P/B)

### Key Valuation Multiples

| Multiple | Formula | Best For |
|----------|---------|----------|
| P/E Ratio | Price / Earnings per Share | Profitable companies |
| EV/EBITDA | Enterprise Value / EBITDA | Cross-company comparison |
| P/B Ratio | Price / Book Value per Share | Asset-heavy businesses |
| P/S Ratio | Price / Sales | Unprofitable growth companies |
| PEG Ratio | (P/E) / Earnings Growth Rate | Growth companies |

## Financial Planning & Analysis

### Scenario Analysis Framework

| Scenario | Assumptions | Probability | NPV Impact |
|----------|-------------|-------------|------------|
| Base Case | Most likely outcomes | 50-60% | Baseline |
| Best Case | Optimistic assumptions | 15-20% | +30-50% |
| Worst Case | Pessimistic assumptions | 15-20% | -30-50% |

**Expected NPV** = Σ (Probability × NPV for each scenario)

### Sensitivity Analysis

Test how changes in key variables affect outcomes:
- Revenue growth rate
- Operating margin
- Discount rate
- Terminal growth rate
- Capital expenditure requirements

**Identify**: Which variables have the largest impact? Focus management attention there.

## Using the Reference Files

### When to Read Each Reference

**`/references/capital-structure.md`** — Read when optimizing debt-equity mix, calculating WACC, evaluating financing alternatives, analyzing the impact of leverage on firm value, or making decisions about issuing debt vs. equity.

**`/references/capital-budgeting.md`** — Read when evaluating investment projects, conducting NPV/IRR analysis, comparing mutually exclusive projects, dealing with capital rationing, or analyzing real options in project valuation.

**`/references/working-capital.md`** — Read when managing cash conversion cycles, optimizing inventory levels, improving accounts receivable collection, negotiating payment terms, or addressing liquidity challenges.

**`/references/corporate-governance.md`** — Read when designing governance structures, addressing agency problems, structuring executive compensation, evaluating board effectiveness, or implementing best practices for shareholder protection and transparency.
