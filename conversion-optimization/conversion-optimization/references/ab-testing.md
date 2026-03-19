# A/B Testing Guide

Comprehensive guide to designing, running, and analyzing A/B tests.

## A/B Testing Fundamentals

A/B testing (split testing) compares two versions to determine which performs better. Visitors are randomly assigned to control (A) or variation (B).

## Test Design

**Strong Hypothesis Template:**
```
Changing [variable]
from [current state]
to [new state]
will increase [metric]
because [reasoning based on data/research].
```

## Sample Size Calculation

For a 5% baseline conversion rate detecting a 1% improvement requires approximately 3,800 visitors per variation at 95% confidence and 80% power.

## Test Duration

- Minimum 1 full week (captures weekly patterns)
- At least 2 business cycles for B2B
- Until required sample size reached

## Statistical Significance

- P-value < 0.05 indicates significance
- Don't peek at results early
- Run for planned duration even if significance reached early

## Common Pitfalls

1. **Peeking**: Checking results before significance
2. **Early Stopping**: Stopping when significance reached
3. **Multiple Comparisons**: Testing too many variations
4. **Ignoring Seasonality**: Not accounting for patterns
5. **Selection Bias**: Not randomly assigning users

## Resources

- Evan Miller A/B Tools: https://www.evanmiller.org/ab-testing/
- Optimizely Stats Engine: https://www.optimizely.com/stats-engine/
- VWO SmartStats: https://vwo.com/why-us/technology/smartstats/
