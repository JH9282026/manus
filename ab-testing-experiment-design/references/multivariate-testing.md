# Multivariate Testing

Designing and analyzing experiments with multiple factors.

---

## MVT vs A/B Testing

| Aspect | A/B Test | Multivariate Test |
|--------|----------|-------------------|
| Factors | 1 | Multiple |
| Variants | 2+ | Many (factorial) |
| Sample needed | Moderate | Large |
| Insights | Single effect | Main effects + interactions |

---

## Factorial Design

### Full Factorial
Test all possible combinations:
- 2 factors × 2 levels = 4 variants
- 3 factors × 2 levels = 8 variants
- 4 factors × 2 levels = 16 variants

### Fractional Factorial
Test subset of combinations:
- Reduces sample requirements
- May confound some interactions
- Good for screening many factors

---

## Factor Selection

### Good MVT Candidates
- Headlines and CTAs
- Images and colors
- Layout variations
- Copy variations

### Poor MVT Candidates
- Highly dependent elements
- Low-traffic pages
- Factors with many levels

---

## Analysis Approach

### Main Effects
Individual impact of each factor.

### Interaction Effects
Combined impact when factors work together.

### Example Analysis
```
Conversion Rate Results:
- Headline A: 5.2%
- Headline B: 5.8%
- CTA A: 5.0%
- CTA B: 6.0%
- Headline B + CTA B: 7.5% (interaction boost)
```

---

## Sample Size Considerations

MVT requires substantially more traffic:
- Account for all combinations
- Maintain statistical power per cell
- Consider sequential elimination

---

## Best Practices

1. Limit factors (2-4 maximum)
2. Start with full factorial when possible
3. Test factors with expected interactions together
4. Run longer to achieve adequate sample
5. Prioritize main effects interpretation
