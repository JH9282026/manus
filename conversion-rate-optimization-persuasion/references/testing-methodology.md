# Testing Methodology

A/B testing design, execution, and analysis.

---

## Hypothesis Development

### Structure
```
IF we [make this change],
THEN [this metric] will [improve by X%],
BECAUSE [evidence-based reason].
```

### Example
```
IF we reduce checkout form from 12 to 6 fields,
THEN checkout completion rate will increase by 15%,
BECAUSE users abandon due to form friction
(evidenced by 28% drop-off at shipping info step).
```

---

## Sample Size Calculation

### Factors
- Baseline conversion rate
- Minimum detectable effect (MDE)
- Statistical significance (typically 95%)
- Statistical power (typically 80%)

### Quick Reference
| Baseline | MDE 10% | MDE 15% | MDE 20% |
|----------|---------|---------|--------|
| 1% | 19,000 | 8,500 | 4,800 |
| 2% | 9,500 | 4,200 | 2,400 |
| 5% | 3,800 | 1,700 | 950 |
| 10% | 1,900 | 850 | 480 |

*Per variation, 95% confidence, 80% power*

---

## Test Types

### A/B Test
- Two variations
- Single variable change
- Clearest results

### Multivariate Test
- Multiple variables
- Tests combinations
- Requires more traffic

### Split URL Test
- Different pages entirely
- Major redesigns
- Technical simplicity

---

## Test Execution

### Pre-Test
1. Document hypothesis
2. Calculate sample size
3. Define success metric
4. Set test duration
5. QA all variations

### During Test
- Don't peek at results
- Monitor for errors
- Track all variations
- Document changes

### Post-Test
1. Verify statistical significance
2. Check segment performance
3. Document learnings
4. Implement winner
5. Plan follow-up tests
