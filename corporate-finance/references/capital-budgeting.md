# Capital Budgeting

Comprehensive framework for evaluating and selecting long-term investment projects to maximize shareholder value.

---

## Investment Decision Framework

### Capital Budgeting Process

**Step 1: Project Identification**
- Strategic alignment assessment
- Preliminary feasibility analysis
- Resource requirements estimation

**Step 2: Cash Flow Estimation**
- Project revenues
- Operating costs
- Capital expenditures
- Working capital changes
- Terminal value

**Step 3: Risk Assessment**
- Identify key uncertainties
- Estimate probability distributions
- Determine appropriate discount rate

**Step 4: Financial Analysis**
- Calculate NPV, IRR, Payback
- Conduct sensitivity analysis
- Perform scenario analysis

**Step 5: Decision**
- Compare to acceptance criteria
- Rank competing projects
- Make go/no-go decision

**Step 6: Implementation & Monitoring**
- Execute project
- Track actual vs. projected performance
- Conduct post-implementation review

---

## Cash Flow Estimation

### Incremental Cash Flow Principle

Only include cash flows that occur **because of** the project.

**Include**:
- Incremental revenues
- Incremental operating costs
- Incremental capital expenditures
- Changes in net working capital
- Opportunity costs
- Side effects (cannibalization, complementary effects)

**Exclude**:
- Sunk costs (already incurred, irrelevant)
- Allocated overhead (unless truly incremental)
- Financing costs (captured in discount rate)

### Cash Flow Components

**Initial Investment (Year 0)**:
```
Initial Investment = Capital Expenditure
                   + Increase in NWC
                   + Opportunity Costs
                   - After-tax Salvage Value of Replaced Assets
```

**Operating Cash Flows (Years 1 to n)**:
```
Operating CF = (Revenue - Operating Costs - Depreciation) × (1 - Tax Rate)
             + Depreciation
             - Change in NWC

Or simplified:
Operating CF = EBIT × (1 - Tax Rate) + Depreciation - Change in NWC
```

**Terminal Cash Flow (Year n)**:
```
Terminal CF = After-tax Salvage Value
            + Recovery of NWC
```

### Working Capital Considerations

**Net Working Capital (NWC)**:
```
NWC = Current Assets - Current Liabilities
    = (Cash + Accounts Receivable + Inventory) - Accounts Payable
```

**Change in NWC**:
- Increase in NWC = Cash outflow (investment)
- Decrease in NWC = Cash inflow (recovery)
- At project end, NWC is typically recovered

**Example**:
- Year 0: Invest $100K in inventory → Cash outflow of $100K
- Year 5: Project ends, sell inventory → Cash inflow of $100K

### Depreciation and Taxes

**Depreciation Tax Shield**:
```
Tax Shield = Depreciation × Tax Rate
```

Depreciation is non-cash but reduces taxable income, creating value.

**Common Depreciation Methods**:

*Straight-Line*:
```
Annual Depreciation = (Cost - Salvage Value) / Useful Life
```

*MACRS (US Tax Code)*:
- Accelerated depreciation
- Higher tax shields in early years
- Increases NPV compared to straight-line

**After-Tax Salvage Value**:
```
After-tax Salvage = Salvage Value - Tax on Gain

Where:
Tax on Gain = (Salvage Value - Book Value) × Tax Rate
```

---

## Net Present Value (NPV) Analysis

### NPV Formula

```
NPV = Σ [CFt / (1 + r)^t] - Initial Investment

Where:
- CFt = cash flow in period t
- r = discount rate (typically WACC)
- t = time period
```

**Decision Rule**:
- NPV > 0: Accept (creates value)
- NPV < 0: Reject (destroys value)
- NPV = 0: Indifferent (breakeven)

### Why NPV is Superior

1. **Uses all cash flows**: Considers entire project life
2. **Time value of money**: Properly discounts future cash flows
3. **Additive**: NPVs of independent projects can be summed
4. **Consistent with value maximization**: Directly measures value creation

### NPV Calculation Example

**Project Details**:
- Initial investment: $1,000,000
- Annual cash flows: $300,000 for 5 years
- Discount rate: 10%

**Calculation**:
```
NPV = -$1,000,000 + $300,000/(1.10)^1 + $300,000/(1.10)^2 + ... + $300,000/(1.10)^5
    = -$1,000,000 + $272,727 + $247,934 + $225,394 + $204,904 + $186,277
    = -$1,000,000 + $1,137,236
    = $137,236
```

**Decision**: Accept (NPV > 0)

### NPV Profile

Graph showing NPV at different discount rates.

**Key Points**:
- Y-intercept: Sum of undiscounted cash flows minus initial investment
- X-intercept: Internal Rate of Return (IRR)
- Slope: Negative (higher discount rate → lower NPV)

**Uses**:
- Visualize sensitivity to discount rate
- Compare projects with different risk profiles
- Identify crossover rate for mutually exclusive projects

---

## Internal Rate of Return (IRR)

### IRR Definition

The discount rate that makes NPV = 0.

```
0 = Σ [CFt / (1 + IRR)^t] - Initial Investment
```

**Decision Rule**:
- IRR > Required Return: Accept
- IRR < Required Return: Reject

### IRR Calculation

No closed-form solution; requires iterative methods:
- Trial and error
- Financial calculator
- Excel: `=IRR(values)` function
- Python: `numpy.irr()` or `scipy.optimize`

### IRR Limitations

**Problem 1: Multiple IRRs**

Projects with non-conventional cash flows (multiple sign changes) can have multiple IRRs.

*Example*:
- Year 0: -$1,000
- Year 1: +$3,000
- Year 2: -$2,000

This can yield two IRRs, making interpretation ambiguous.

**Solution**: Use NPV instead.

**Problem 2: Scale Differences**

IRR ignores project size.

*Example*:
- Project A: Invest $100, IRR = 50%, NPV = $20
- Project B: Invest $1,000, IRR = 30%, NPV = $200

IRR favors A, but B creates more value.

**Solution**: Use NPV for mutually exclusive projects.

**Problem 3: Timing Differences**

IRR assumes reinvestment at IRR (unrealistic).

*Example*:
- Project A: Early cash flows, IRR = 25%
- Project B: Late cash flows, IRR = 20%

If reinvestment rate < 25%, Project A's advantage is overstated.

**Solution**: Use NPV (assumes reinvestment at WACC, more realistic).

### Modified IRR (MIRR)

Addresses reinvestment rate assumption.

```
MIRR = [(Terminal Value / Initial Investment)^(1/n)] - 1

Where:
Terminal Value = Σ [CFt × (1 + r)^(n-t)]
```

**Advantages**:
- Single solution
- Realistic reinvestment assumption (at WACC)
- Better for comparing projects

---

## Payback Period

### Payback Period Definition

Time required to recover initial investment.

```
Payback Period = Year before full recovery + (Unrecovered cost / Cash flow in recovery year)
```

**Decision Rule**:
- Payback < Target: Accept
- Payback > Target: Reject

### Payback Calculation Example

**Project Cash Flows**:
- Year 0: -$10,000
- Year 1: $3,000
- Year 2: $4,000
- Year 3: $5,000

**Cumulative Cash Flows**:
- Year 1: -$7,000
- Year 2: -$3,000
- Year 3: +$2,000

**Payback Period**:
```
Payback = 2 + ($3,000 / $5,000) = 2.6 years
```

### Discounted Payback Period

Uses present value of cash flows.

**Advantages over Simple Payback**:
- Accounts for time value of money
- More conservative

**Still Ignores**:
- Cash flows after payback
- Overall profitability

### When to Use Payback

**Appropriate**:
- Quick screening tool
- High uncertainty environments
- Liquidity-constrained firms
- Short-lived industries (fashion, technology)

**Not Appropriate**:
- As primary decision criterion
- For long-term strategic investments
- When comparing projects of different lives

---

## Profitability Index (PI)

### PI Definition

```
PI = PV of Future Cash Flows / Initial Investment
   = (NPV + Initial Investment) / Initial Investment
   = 1 + (NPV / Initial Investment)
```

**Decision Rule**:
- PI > 1: Accept (equivalent to NPV > 0)
- PI < 1: Reject

### PI for Capital Rationing

When capital is limited, PI ranks projects by value per dollar invested.

**Example**:

| Project | Initial Investment | NPV | PI | Rank |
|---------|-------------------|-----|----|----- |
| A | $100,000 | $30,000 | 1.30 | 2 |
| B | $200,000 | $50,000 | 1.25 | 3 |
| C | $150,000 | $60,000 | 1.40 | 1 |

**Capital Budget**: $300,000

**Optimal Selection**: Projects C + A (Total NPV = $90,000)

If using NPV alone, might select C + B (Total NPV = $110,000, but requires $350,000)

---

## Comparing Mutually Exclusive Projects

### NPV vs. IRR Conflicts

**Crossover Rate**: Discount rate where NPVs of two projects are equal.

**Decision Rule**:
- If WACC < Crossover Rate: Choose project with higher NPV
- If WACC > Crossover Rate: Choose project with higher NPV (always use NPV)

**Why NPV Wins**:
- Measures absolute value creation
- Consistent with shareholder wealth maximization
- No scale or timing issues

### Equivalent Annual Annuity (EAA)

Compare projects with different lifespans.

**EAA Formula**:
```
EAA = NPV / [(1 - (1 + r)^-n) / r]
    = NPV / Annuity Factor
```

**Decision Rule**: Choose project with higher EAA.

**Example**:

*Project A*:
- Life: 3 years
- NPV: $100,000
- WACC: 10%
- EAA: $100,000 / 2.4869 = $40,211

*Project B*:
- Life: 5 years
- NPV: $150,000
- WACC: 10%
- EAA: $150,000 / 3.7908 = $39,571

**Decision**: Choose Project A (higher EAA)

### Replacement Chain Method

Alternative to EAA: Repeat projects until common life.

**Example**:
- Project A: 3-year life
- Project B: 5-year life
- Common life: 15 years

**Analysis**:
- Repeat Project A five times (3 × 5 = 15)
- Repeat Project B three times (5 × 3 = 15)
- Calculate NPV of each chain
- Choose higher NPV

---

## Risk Analysis in Capital Budgeting

### Sensitivity Analysis

Test how NPV changes with individual variables.

**Process**:
1. Identify key variables (revenue, costs, discount rate, etc.)
2. Vary each variable (e.g., ±10%, ±20%)
3. Calculate NPV for each scenario
4. Identify most sensitive variables

**Example Output**:

| Variable | -20% | -10% | Base | +10% | +20% |
|----------|------|------|------|------|------|
| Revenue | -$50K | $20K | $100K | $180K | $260K |
| Costs | $180K | $140K | $100K | $60K | $20K |
| Discount Rate | $150K | $120K | $100K | $85K | $72K |

**Insight**: NPV is most sensitive to revenue assumptions.

### Scenario Analysis

Evaluate NPV under different comprehensive scenarios.

**Typical Scenarios**:

| Scenario | Probability | Revenue Growth | Margin | Discount Rate | NPV |
|----------|-------------|----------------|--------|---------------|-----|
| Best Case | 20% | 15% | 25% | 8% | $500K |
| Base Case | 50% | 10% | 20% | 10% | $200K |
| Worst Case | 30% | 5% | 15% | 12% | -$50K |

**Expected NPV**:
```
E(NPV) = (0.20 × $500K) + (0.50 × $200K) + (0.30 × -$50K)
       = $100K + $100K - $15K
       = $185K
```

### Monte Carlo Simulation

Use probability distributions for multiple variables simultaneously.

**Process**:
1. Define probability distributions for key variables
2. Randomly sample from distributions
3. Calculate NPV for each iteration
4. Repeat thousands of times
5. Analyze distribution of NPVs

**Output**:
- Mean NPV
- Standard deviation (risk measure)
- Probability of NPV > 0
- Percentile values (e.g., 5th percentile NPV)

**Advantages**:
- Captures interaction effects
- Provides full distribution of outcomes
- Quantifies risk explicitly

### Decision Trees

Model sequential decisions and uncertain outcomes.

**Components**:
- **Decision nodes** (squares): Choices under management control
- **Chance nodes** (circles): Uncertain outcomes
- **Branches**: Possible paths
- **Payoffs**: Terminal values

**Analysis Method**: Backward induction
1. Start at terminal nodes
2. Calculate expected values at chance nodes
3. Choose optimal decisions at decision nodes
4. Work backward to initial decision

**Example Application**:
- Pilot project decision
- Expansion decision contingent on pilot success
- Abandonment option if pilot fails

---

## Real Options in Capital Budgeting

### Types of Real Options

**Option to Expand**:
- Make initial investment
- Expand if conditions are favorable
- Value: Upside potential with limited downside

**Option to Abandon**:
- Exit project if conditions deteriorate
- Salvage value provides floor
- Value: Limits downside risk

**Option to Delay**:
- Wait for more information
- Invest when uncertainty resolves
- Value: Flexibility to time investment

**Option to Contract**:
- Scale down operations if demand is weak
- Reduces losses in bad scenarios
- Value: Operational flexibility

**Switching Options**:
- Change inputs, outputs, or processes
- Respond to price changes
- Value: Adaptability

### Valuing Real Options

**Qualitative Assessment**:
- Does project create future opportunities?
- Can project be abandoned if unsuccessful?
- Is there value in waiting?

**Quantitative Methods**:

*Decision Tree Analysis*:
- Model option exercise decisions
- Calculate expected value including option value

*Black-Scholes Adaptation*:
- Treat investment as call option
- Underlying asset: PV of project cash flows
- Strike price: Investment cost
- Volatility: Uncertainty in project value

*Binomial Model*:
- Model project value evolution over time
- Calculate option value at each node
- Work backward to present

### Real Options Example: Option to Expand

**Base Project**:
- Initial investment: $10M
- NPV: $2M

**Expansion Option**:
- If successful (60% probability): Invest additional $15M in Year 2
- Expansion NPV (if exercised): $8M
- If unsuccessful (40% probability): No expansion

**Option Value**:
```
Expansion Option Value = 0.60 × $8M / (1.10)^2 = $3.97M

Total Project Value = Base NPV + Option Value
                    = $2M + $3.97M
                    = $5.97M
```

**Decision**: Accept project (positive value including option)

---

## Capital Rationing

### Types of Capital Rationing

**Hard Rationing**: External constraints (limited access to capital markets)
**Soft Rationing**: Internal constraints (management-imposed limits)

### Single-Period Rationing

**Objective**: Maximize total NPV subject to budget constraint.

**Method**: Profitability Index ranking

**Example**:

| Project | Investment | NPV | PI |
|---------|-----------|-----|----|
| A | $5M | $2M | 1.40 |
| B | $3M | $1.5M | 1.50 |
| C | $4M | $1.2M | 1.30 |
| D | $2M | $0.6M | 1.30 |

**Budget**: $10M

**Ranking by PI**: B, A, C/D (tied)

**Optimal Portfolio**: B + A + D = $10M, Total NPV = $4.1M

### Multi-Period Rationing

**Complexity**: Budget constraints in multiple periods.

**Solution Method**: Linear programming

**Objective Function**:
```
Maximize: Σ (NPVi × Xi)

Subject to:
Σ (Investmenti,t × Xi) ≤ Budgett  for all periods t
Xi ∈ {0, 1}  (accept or reject)
```

---

## Post-Implementation Review

### Purpose

- Compare actual vs. projected performance
- Identify estimation biases
- Improve future capital budgeting
- Hold managers accountable

### Key Metrics to Track

| Metric | Projected | Actual | Variance |
|--------|-----------|--------|----------|
| Initial Investment | | | |
| Annual Cash Flows | | | |
| Project Life | | | |
| NPV | | | |
| IRR | | | |
| Payback Period | | | |

### Common Estimation Errors

**Optimism Bias**: Overestimate benefits, underestimate costs
**Strategic Misrepresentation**: Intentional bias to get approval
**Anchoring**: Over-reliance on initial estimates
**Sunk Cost Fallacy**: Continuing bad projects due to past investment

### Corrective Actions

- Require independent reviews
- Use reference class forecasting (base rates from similar projects)
- Implement stage-gate processes
- Tie compensation to actual project performance
- Maintain database of past project performance
