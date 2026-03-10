# Multivariate Testing (MVT)

Testing multiple variables simultaneously to understand interactions.

---

## MVT vs A/B Testing

| Aspect | A/B Test | Multivariate Test |
|--------|----------|-------------------|
| Variables | 1 | 2+ |
| Combinations | 2 | 2^n or more |
| Sample required | Lower | Higher |
| Insights | Single effect | Effects + interactions |
| Complexity | Simple | Complex |

### When to Use MVT
- Testing related elements that may interact
- Page redesigns with multiple changes
- Optimizing complex components
- Have sufficient traffic

### When NOT to Use MVT
- Low traffic websites
- Need quick results
- Testing unrelated changes
- Limited resources for analysis

---

## Full Factorial Design

### Concept
Test ALL possible combinations of variables.

### Example: 2 Variables, 2 Levels Each
```
Variable A: Headline (Original, New)
Variable B: Image (Original, New)

Combinations = 2 × 2 = 4
1. Original Headline + Original Image
2. Original Headline + New Image
3. New Headline + Original Image
4. New Headline + New Image
```

### Sample Size Impact
```
Variables × Levels = Combinations

2 variables × 2 levels = 4 combinations
3 variables × 2 levels = 8 combinations
4 variables × 2 levels = 16 combinations
3 variables × 3 levels = 27 combinations
```

Each combination needs full A/B test sample size.

### Advantages
- Tests all interactions
- Complete data
- Clear winner identification

### Disadvantages
- Requires large sample
- Many combinations to manage
- Longer test duration

---

## Fractional Factorial Design

### Concept
Test a SUBSET of combinations using statistical methods.

### When to Use
- Too many combinations for full factorial
- Want to screen many variables
- Interactions less important than main effects

### Resolution Levels
| Resolution | What's Confounded | Use When |
|------------|-------------------|----------|
| III | Main effects with 2-way interactions | Screening |
| IV | 2-way interactions with each other | Most MVT |
| V | 2-way with 3-way interactions | Detailed analysis |

### Example: 8 Variables with Resolution III
Instead of 2^8 = 256 combinations:
- Fractional design: 16 combinations
- Identifies main effects
- Some interaction confounding

### Design Tables
Use orthogonal arrays to select which combinations to test.

---

## Analyzing MVT Results

### Main Effects
The individual impact of each variable, averaged across all other conditions.

```
Main effect of Headline = 
  Average(all New Headline conditions) - 
  Average(all Original Headline conditions)
```

### Interaction Effects
When the effect of one variable depends on the level of another.

```
If:
- New Headline alone: +2%
- New Image alone: +3%
- Both together: +10%

Interaction = 10% - (2% + 3%) = +5%
Synergy between the two changes!
```

### ANOVA for MVT
```
Total variance = Main effect A + Main effect B + 
                 Interaction A×B + Error

F-ratio tests significance of each component.
```

### Interpreting Results Table
| Source | SS | df | MS | F | p |
|--------|----|----|----|----|-----|
| Headline | 120 | 1 | 120 | 15.0 | 0.001 |
| Image | 80 | 1 | 80 | 10.0 | 0.003 |
| H × I | 40 | 1 | 40 | 5.0 | 0.028 |
| Error | 480 | 60 | 8 | | |

All effects significant if p < 0.05.

---

## MVT Implementation

### Planning Phase
1. Identify variables to test
2. Define levels for each variable
3. Calculate total combinations
4. Determine if full or fractional design
5. Calculate sample size per combination
6. Estimate test duration

### Sample Size for MVT
```
Per combination = Standard A/B sample size
Total = Per combination × Number of combinations

Example:
- Need 10,000 per combination
- 8 combinations (2×2×2)
- Total needed: 80,000
```

### Traffic Allocation
```
Equal allocation across all combinations:
- 8 combinations = 12.5% each
- Ensures balanced comparison
```

### Technical Setup
1. Create all variant combinations
2. QA each combination
3. Set up tracking for each
4. Verify randomization across combinations
5. Monitor for implementation errors

---

## Taguchi Method

### Overview
Fractional factorial approach focusing on robust design.

### Key Concepts
- **Signal-to-noise ratio**: Optimize for consistency
- **Robust design**: Find settings that work across conditions
- **Quality loss function**: Minimize deviation from target

### When to Use
- Process optimization
- Manufacturing settings
- When variability matters

### Limitations for Web MVT
- Assumes deterministic relationships
- Web behavior is noisier
- Full factorial often more appropriate online

---

## MVT Tools and Platforms

| Platform | Full Factorial | Fractional | Analysis |
|----------|---------------|------------|----------|
| Google Optimize | Yes | No | Basic |
| Optimizely | Yes | Yes | Advanced |
| VWO | Yes | No | Moderate |
| Adobe Target | Yes | Yes | Advanced |
| Custom | Flexible | Flexible | Depends |

### Analysis Software
- **R**: Full statistical capabilities
- **Python (scipy, statsmodels)**: ANOVA, effect calculations
- **JMP**: Designed for DOE
- **Minitab**: Industrial MVT

---

## Best Practices

### Variable Selection
1. Focus on high-impact elements
2. Choose independent variables when possible
3. Limit to 3-4 variables for manageability
4. Ensure each variable is meaningful to test

### Level Selection
1. Make levels sufficiently different
2. Include current version as a level
3. Avoid extreme outliers
4. Consider practical implementation

### Analysis Guidelines
1. Always check for interactions first
2. Don't assume additivity of effects
3. Consider practical significance, not just statistical
4. Report effect sizes with confidence intervals

### Common Mistakes
| Mistake | Impact | Solution |
|---------|--------|----------|
| Too many variables | Underpowered test | Limit to 3-4 |
| Ignoring interactions | Missing insights | Always analyze interactions |
| Premature stopping | Invalid results | Commit to sample size |
| Testing correlated changes | Confounded effects | Choose independent variables |

---

## MVT Decision Framework

```
Step 1: Count variables
  - If 1 variable → Standard A/B
  - If 2-4 variables → Consider MVT
  - If 5+ variables → Fractional or sequential A/B

Step 2: Assess traffic
  - Calculate: (sample per combo) × (num combinations)
  - If feasible within 4 weeks → Proceed
  - If not → Reduce variables or use fractional

Step 3: Choose design
  - Interactions critical? → Full factorial
  - Screening phase? → Fractional factorial
  - Very limited traffic? → Sequential A/B tests

Step 4: Analyze
  - Check main effects AND interactions
  - Report winning combination
  - Document insights for future tests
```
