# Scenario and Sensitivity Analysis

Comprehensive guide to building scenario analysis, sensitivity analysis, and probabilistic modeling in financial models.

---

## Scenario Analysis

### Overview

Scenario analysis evaluates how a financial model's outputs change under different sets of assumptions representing plausible future states.

### Scenario Types

#### Base Case Scenario

**Definition**: Most likely outcome based on reasonable assumptions

**Characteristics**:
- Realistic and achievable
- Based on historical trends
- Management's best estimate

**Probability**: Typically 50-60%

#### Upside (Optimistic) Case

**Definition**: Favorable outcome with optimistic but plausible assumptions

**Characteristics**:
- Better than expected performance
- Favorable market conditions
- Successful execution of strategy

**Probability**: Typically 20-30%

#### Downside (Pessimistic) Case

**Definition**: Unfavorable outcome with pessimistic but plausible assumptions

**Characteristics**:
- Worse than expected performance
- Adverse market conditions
- Execution challenges

**Probability**: Typically 20-30%

### Implementation Methods

#### Method 1: Scenario Columns

Create separate columns for each scenario with side-by-side comparison.

#### Method 2: Scenario Switch with CHOOSE Function

Use dropdown to select scenario with CHOOSE function switching between assumption sets.

**Example**:
```excel
=CHOOSE($A$1, Base_Assumption, Upside_Assumption, Downside_Assumption)
```

#### Method 3: Scenario Manager (Excel Tool)

Use built-in Excel Scenario Manager to define scenarios and generate summary reports.

### Scenario Outputs

**Key Outputs to Compare**:
- Revenue and EBITDA
- Free cash flow
- Enterprise and equity value
- Debt/EBITDA ratios
- IRR and returns

---

## Sensitivity Analysis

### Overview

Sensitivity analysis examines how changes in individual input variables affect model outputs.

### One-Way Sensitivity Analysis

**Definition**: Vary one input variable while holding all others constant.

**Data Table Method**:
- Create output formula
- Create input range
- Use Excel Data Table feature

**Tornado Chart**:
- Visual representation showing relative impact of multiple variables
- Sorted by impact (largest at top)
- Identifies key value drivers

### Two-Way Sensitivity Analysis

**Definition**: Vary two input variables simultaneously.

**Common Combinations**:
- WACC vs. Terminal Growth Rate
- Revenue Growth vs. EBITDA Margin
- Entry Multiple vs. Exit Multiple

**Example: WACC vs. Terminal Growth Rate**

|  | Terminal Growth Rate |
|---|---|
| WACC | 1.5% | 2.0% | 2.5% | 3.0% |
| 8.5% | $32.50 | $34.80 | $37.50 | $40.80 |
| 9.0% | $30.20 | $32.30 | $34.70 | $37.60 |
| 9.5% | $28.10 | $30.00 | $32.20 | $34.80 |
| 10.0% | $26.20 | $28.00 | $30.00 | $32.40 |

### Break-Even Analysis

**Definition**: Identify the value of an input variable where output reaches a specific threshold.

**Common Break-Even Analyses**:
- Break-even revenue
- Break-even price
- Break-even volume

**Calculation Methods**:
- Goal Seek (Excel)
- Formula-based calculation

### Sensitivity Analysis Best Practices

**Variable Selection**:
- Focus on key value drivers
- Include variables with uncertainty
- Typically 5-10 variables for tornado chart

**Range Selection**:
- Use reasonable ranges
- Based on historical volatility
- Consider realistic scenarios

**Presentation**:
- Use visual aids (charts, color coding)
- Highlight base case
- Show range of outcomes

---

## Monte Carlo Simulation

### Overview

Monte Carlo simulation runs thousands of scenarios by randomly sampling from probability distributions for input variables, producing a distribution of possible outcomes.

### When to Use Monte Carlo

**Appropriate Situations**:
- High uncertainty in multiple variables
- Complex interdependencies
- Need for probability distribution of outcomes
- Risk quantification required

### Implementation

**Steps**:
1. Identify key uncertain variables
2. Define probability distributions for each
3. Run simulation (1,000-10,000 iterations)
4. Analyze output distribution

**Tools**:
- Excel add-ins (Crystal Ball, @RISK)
- Python (NumPy, SciPy)
- R statistical software

### Output Analysis

**Key Statistics**:
- Mean (expected value)
- Median
- Standard deviation
- Percentiles (5th, 25th, 75th, 95th)
- Probability of outcomes

**Visualization**:
- Histogram of outcomes
- Cumulative probability curve
- Confidence intervals

---

## Best Practices

**Scenario and Sensitivity Analysis**:
- Test key assumptions systematically
- Document all assumptions
- Present range of outcomes
- Focus on key value drivers
- Use multiple analytical approaches

**Communication**:
- Visual presentation of results
- Clear explanation of scenarios
- Highlight key sensitivities
- Provide actionable insights
