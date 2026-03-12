# Optimization & Simulation

## Linear Programming (LP)

### Standard Form
- **Minimize/Maximize**: cᵀx (objective function)
- **Subject to**: Ax ≤ b (constraints)
- **Where**: x ≥ 0 (non-negativity)

### Applications
| Problem | Decision Variables | Objective |
|---------|-------------------|-----------|
| Production planning | Units to produce | Maximize profit |
| Transportation | Shipment quantities | Minimize cost |
| Portfolio allocation | Investment amounts | Maximize return |
| Scheduling | Time assignments | Minimize makespan |
| Blending | Ingredient proportions | Minimize cost |

### Solution Methods
- **Simplex method**: Exact solution for LP
- **Interior point**: Large-scale LP
- **Branch and bound**: Integer programming
- **Dynamic programming**: Sequential decisions

---

## Integer Programming

### Types
- **Pure IP**: All variables integer
- **Mixed IP (MIP)**: Some integer, some continuous
- **Binary IP**: Variables are 0 or 1

### Common Binary Formulations
- Facility location (open/close)
- Vehicle routing (visit/skip)
- Scheduling (assign/not assign)
- Knapsack (include/exclude)

---

## Monte Carlo Simulation

### Process
1. Define probability distributions for uncertain inputs
2. Sample randomly from distributions (10,000+ iterations)
3. Run model for each sample set
4. Analyze output distribution

### Common Input Distributions
| Distribution | Use Case | Parameters |
|-------------|----------|-----------|
| Normal | Natural variation | Mean, std dev |
| Uniform | Equal probability | Min, max |
| Triangular | Expert estimates | Min, mode, max |
| Lognormal | Right-skewed data | Mean, std dev |
| Poisson | Event counts | Rate (λ) |
| Exponential | Time between events | Rate (λ) |

### Output Analysis
- Mean and confidence intervals
- Percentile values (P10, P50, P90)
- Probability of exceeding thresholds
- Sensitivity tornado diagram
- Correlation analysis between inputs and outputs

---

## Sensitivity Analysis

### One-at-a-Time (OAT)
- Vary one parameter while holding others constant
- Calculate output change per unit input change
- Simple but misses interaction effects

### Global Sensitivity Analysis
- **Sobol indices**: Variance-based decomposition
- **Morris method**: Screening for important factors
- **Latin Hypercube**: Efficient sampling of parameter space

### Reporting Format
| Parameter | Base Value | Range | Output Impact | Rank |
|-----------|-----------|-------|---------------|------|
| Price | $100 | $80-120 | ±$2M revenue | 1 |
| Volume | 10,000 | 8K-12K | ±$1.5M revenue | 2 |
| Cost | $60 | $50-70 | ±$1M revenue | 3 |
