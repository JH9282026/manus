# A/B Test Fundamentals

Core concepts and setup procedures for controlled experiments.

---

## Hypothesis Formation

### Structure
```
If we [make this change],
then we expect [this outcome],
because [this reasoning].
```

### Good vs Bad Hypotheses

| Bad | Good |
|-----|------|
| "The new design is better" | "If we increase CTA button size from 40px to 60px, conversion will increase by 5% because it improves visibility" |
| "Users will like this" | "If we add social proof badges, checkout completion will increase because it reduces purchase anxiety" |

### Hypothesis Checklist
- [ ] Specific change identified
- [ ] Measurable outcome defined
- [ ] Causal mechanism explained
- [ ] Falsifiable (can be proven wrong)

---

## Sample Size Calculation

### Key Inputs
1. **Baseline conversion rate**: Current performance
2. **Minimum Detectable Effect (MDE)**: Smallest meaningful change
3. **Statistical significance (α)**: Usually 0.05 (5%)
4. **Statistical power (1-β)**: Usually 0.80 (80%)

### Formula (Two-Sample Proportion Test)
```
n = 2 × [(Z_α/2 + Z_β)² × p(1-p)] / (MDE)²

Where:
- Z_α/2 = 1.96 for α=0.05 (two-tailed)
- Z_β = 0.84 for power=0.80
- p = baseline proportion
- MDE = absolute minimum detectable effect
```

### Practical Calculation Example
```
Baseline: 5% conversion
MDE: 0.5% absolute (10% relative lift)
α: 0.05, Power: 0.80

n = 2 × [(1.96 + 0.84)² × 0.05 × 0.95] / (0.005)²
n = 2 × [7.84 × 0.0475] / 0.000025
n = 2 × 14,893
n ≈ 30,000 per variant
```

### Sample Size Tables

#### For Binary Metrics (Conversion)
| Baseline | 5% Relative MDE | 10% Relative MDE | 20% Relative MDE |
|----------|-----------------|------------------|------------------|
| 1% | 1,520,000 | 380,000 | 96,000 |
| 2% | 740,000 | 186,000 | 47,000 |
| 5% | 280,000 | 70,000 | 18,000 |
| 10% | 130,000 | 33,000 | 8,400 |
| 25% | 45,000 | 11,400 | 2,900 |

#### For Continuous Metrics (Revenue)
Requires estimate of standard deviation. Use historical data or pilot test.

---

## Test Duration

### Calculating Duration
```
Duration = Required Sample Size / Daily Traffic per Variant

Example:
- Need 30,000 per variant
- Site gets 10,000 visitors/day
- 50% traffic in test
- Duration = 30,000 / (10,000 × 0.5 / 2) = 12 days
```

### Minimum Duration Rules
- **1 full business cycle**: Capture day-of-week effects
- **2+ weeks recommended**: Account for weekly patterns
- **Avoid major events**: Holidays, sales, launches

### Maximum Duration Considerations
- Opportunity cost of not shipping
- Potential for external changes
- User base evolution
- Technical debt of test code

---

## Randomization

### Requirements
1. **Random assignment**: Each user has equal chance of each variant
2. **Consistent assignment**: User always sees same variant
3. **Independent**: One user's assignment doesn't affect others

### Implementation Methods

#### Cookie-Based
```javascript
function assignVariant(userId) {
  const hash = md5(userId + experimentId + salt);
  const bucket = parseInt(hash.slice(0, 8), 16) % 100;
  return bucket < 50 ? 'control' : 'treatment';
}
```

#### Server-Side Assignment
- More reliable than client-side
- Prevents flicker
- Works for logged-out users via device ID

### Stratified Randomization
When important to balance on known variables:
```
1. Segment users by key attribute (e.g., device type)
2. Randomize within each segment
3. Ensures balance across segments
```

---

## Traffic Allocation

### Allocation Strategies
| Strategy | Use Case | Pros | Cons |
|----------|----------|------|------|
| 50/50 | Standard test | Fastest results | Maximum exposure to risk |
| 90/10 | Risky changes | Limited downside | Slower, less power |
| 80/20 | Cautious launch | Moderate speed/risk | Needs larger sample |

### Ramp-Up Protocol
```
Day 1-2: 1% of traffic (smoke test)
Day 3-5: 10% of traffic (initial results)
Day 6+: 50% of traffic (full test)
```

### Traffic Allocation Math
```
If site has 100,000 daily visitors:
- 50/50 split: 50,000 per variant
- 90/10 split: 90,000 control, 10,000 treatment
- With 10% in experiment: 5,000 per variant
```

---

## A/B/n Testing

### When to Use
- Testing 3+ variations
- Exploring design space
- Don't know which direction is better

### Sample Size Adjustment
More variants = need more total sample
```
Bonferroni correction: α' = α / number of comparisons
With 3 variants and α=0.05:
- 3 pairwise comparisons
- Adjusted α = 0.05/3 = 0.017
```

### Comparison Strategy
| Approach | Description | When to Use |
|----------|-------------|-------------|
| All vs Control | Compare each treatment to control only | Clear baseline exists |
| Pairwise | Compare all pairs | Finding best overall |
| Best vs Rest | Winner takes all | Speed over precision |

---

## Experiment Documentation

### Pre-Registration Template
```markdown
## Experiment: [Name]
### Date: [Planned start]
### Owner: [Name]

## Hypothesis
[Structured hypothesis statement]

## Design
- Type: A/B / A/B/n / MVT
- Traffic: [%] of [segment]
- Duration: [X] days
- Sample size: [N] per variant

## Metrics
### Primary
- [Metric name]: [Definition]
- Success threshold: [X%] lift

### Secondary
- [Metric name]: [Definition]

### Guardrails
- [Metric name]: Must not decrease by more than [X%]

## Variants
### Control (A)
[Description]

### Treatment (B)
[Description]

## Analysis Plan
[How results will be analyzed]

## Decision Criteria
- Ship if: [Criteria]
- Iterate if: [Criteria]
- Kill if: [Criteria]
```

---

## QA Checklist

### Before Launch
- [ ] Both variants render correctly
- [ ] Tracking events fire on both variants
- [ ] Randomization working properly
- [ ] No performance differences between variants
- [ ] Mobile/desktop both working
- [ ] Edge cases handled (logged out, ad blockers)

### After Launch (24 hours)
- [ ] Traffic split is correct (within 1%)
- [ ] No sample ratio mismatch
- [ ] Events logging as expected
- [ ] No error rate increase
- [ ] Page load times comparable

### Sample Ratio Mismatch (SRM)
If variant proportions differ significantly from expected:
1. Do NOT trust results
2. Investigate technical issues
3. Fix and restart experiment
