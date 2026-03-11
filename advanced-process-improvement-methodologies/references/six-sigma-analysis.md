# Six Sigma Statistical Analysis

Statistical methods for Six Sigma projects.

---

## Statistical Process Control (SPC)

### Control Chart Types
| Chart | Application |
|-------|-------------|
| X-bar and R | Process mean and range |
| P-chart | Proportion defective |
| C-chart | Count of defects |
| I-MR | Individual measurements |

### Interpretation Rules
- Points outside control limits = special cause
- Runs, trends, patterns = process shift
- Process in control = only common cause variation

---

## Hypothesis Testing

### Common Tests
| Test | When to Use |
|------|-------------|
| t-test | Compare two group means |
| ANOVA | Compare multiple group means |
| Chi-Square | Categorical data relationships |
| Regression | Variable relationships |
| F-test | Compare variances |

### Process
1. State H₀ (null) and H₁ (alternative)
2. Select significance level (α = 0.05 typical)
3. Choose appropriate test
4. Calculate test statistic and p-value
5. Draw conclusion

---

## Design of Experiments (DOE)

### Concepts
- **Factors**: Input variables tested
- **Levels**: Different values of each factor
- **Response**: Output measured
- **Main Effects**: Individual factor impacts
- **Interactions**: Combined factor effects

### Types
- **Full Factorial**: All combinations (comprehensive)
- **Fractional Factorial**: Subset (efficient)
- **Taguchi Methods**: Focus on robustness

---

## Process Capability Analysis

### Metrics
- **Cp**: Compares spec width to process width (potential)
- **Cpk**: Accounts for centering (actual)
- **Pp/Ppk**: Overall variation (performance)

### Formulas
```
Cp = (USL - LSL) / 6σ

Cpk = MIN[(USL - μ) / 3σ, (μ - LSL) / 3σ]
```

---

## Root Cause Analysis Tools

### 5 Whys Example
1. Machine stopped (Problem)
2. Why? Overloaded, fuse blew
3. Why? Bearing not lubricated
4. Why? Pump not working
5. Why? Shaft worn
6. Why? No strainer (Root Cause)

### Fishbone Categories (6 M's)
- Man
- Machine
- Method
- Material
- Measurement
- Mother Nature (Environment)
