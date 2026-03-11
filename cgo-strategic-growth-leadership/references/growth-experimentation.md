# Growth Experimentation

Framework for designing and running growth experiments.

---

## Experimentation Framework

### Experiment Types
| Type | Description | Use Case |
|------|-------------|----------|
| A/B Test | Two variants | Clear hypothesis |
| Multivariate | Multiple variables | Complex optimization |
| Sequential | One after another | Limited traffic |
| Holdout | Control group over time | Long-term impact |

### Experiment Process
1. **Observe**: Identify opportunity area
2. **Hypothesize**: Formulate testable hypothesis
3. **Design**: Create experiment plan
4. **Execute**: Run experiment
5. **Analyze**: Evaluate results
6. **Decide**: Implement or iterate

---

## Hypothesis Development

### Hypothesis Structure
```
If we [change], then [metric] will [impact],
because [rationale].
```

**Example:**
"If we add social proof (customer logos) to the pricing page, then conversion rate will increase by 10%, because prospects will have increased trust in our solution."

### ICE Prioritization
| Factor | Description | Scale |
|--------|-------------|-------|
| Impact | Effect if successful | 1-10 |
| Confidence | Belief in success | 1-10 |
| Ease | Implementation effort | 1-10 |

ICE Score = Impact × Confidence × Ease

### RICE Framework
| Factor | Description |
|--------|-------------|
| Reach | How many users affected |
| Impact | Effect per user |
| Confidence | Belief in estimates |
| Effort | Time/resources required |

RICE Score = (Reach × Impact × Confidence) / Effort

---

## Experiment Design

### Sample Size Calculation
| Factor | Impact |
|--------|--------|
| Baseline conversion | Higher = smaller sample |
| Minimum detectable effect | Smaller = larger sample |
| Confidence level (typically 95%) | Higher = larger sample |
| Power (typically 80%) | Higher = larger sample |

### Duration Planning
- Minimum sample size achieved
- At least one full business cycle
- Account for day-of-week effects
- Usually 1-4 weeks minimum

### Traffic Allocation
| Approach | Use Case |
|----------|----------|
| 50/50 | Standard, fastest results |
| 80/20 | Risk mitigation |
| Multi-arm | Multiple variants |
| Ramp up | Start small, increase |

---

## Analysis & Decision

### Statistical Significance
- p-value < 0.05 (95% confidence)
- Effect size meaningful
- Sample size sufficient
- No obvious confounds

### Result Interpretation
| Result | Action |
|--------|--------|
| Winner, significant | Implement |
| Winner, not significant | Extend or iterate |
| Loser, significant | Reject hypothesis |
| Inconclusive | Redesign experiment |

### Documentation
- Hypothesis
- Test design
- Results (with confidence intervals)
- Learnings
- Next steps

---

## Experimentation Culture

### Building a Testing Culture
- Leadership support
- Celebrate learnings, not just wins
- Easy-to-use tools
- Shared knowledge base
- Regular experiment reviews

### Common Pitfalls
| Pitfall | Solution |
|---------|----------|
| Peeking at results | Pre-set analysis times |
| Stopping too early | Commit to sample size |
| Testing too many things | Prioritize ruthlessly |
| Not documenting | Required documentation |
| Ignoring segments | Always check segments |

### Velocity Metrics
| Metric | Description |
|--------|-------------|
| Experiments/month | Volume of testing |
| Win rate | % of experiments that win |
| Velocity | Tests × Win Rate × Impact |
| Learnings captured | Documentation quality |
