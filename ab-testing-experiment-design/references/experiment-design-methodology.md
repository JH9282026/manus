# Experiment Design Methodology

Comprehensive guide to designing controlled experiments for causal measurement.

---

## Hypothesis Formation

### Structure of a Good Hypothesis

Formulate hypotheses using this template:

> "If we [implement change X], then [metric Y] will [increase/decrease] by [expected magnitude], because [theoretical rationale]."

Examples:
- "If we simplify the checkout flow to 2 steps, then conversion rate will increase by 5%, because reduced friction decreases abandonment."
- "If we add social proof badges, then signup rate will increase by 10%, because social validation reduces uncertainty."

### Hypothesis Quality Criteria

| Criterion | Description | Example |
|-----------|-------------|---------|
| Testable | Can be proven false | "Increases conversion" vs "improves experience" |
| Specific | Clear metric and magnitude | "5% relative lift" vs "some improvement" |
| Grounded | Based on theory or data | User research, prior experiments |
| Actionable | Informs a decision | Clear ship/no-ship implication |

---

## Experiment Types

### Classic A/B Test

Split traffic between control (A) and treatment (B) variants.

**Use when:**
- Testing single, well-defined change
- Sufficient traffic for sample requirements
- User-level randomization possible

**Design considerations:**
- 50/50 split recommended for maximum power
- Maintain consistent experience throughout session
- Log assignment at randomization time

### A/B/n Test (Multi-Variant)

Test multiple variants simultaneously against control.

**Use when:**
- Exploring multiple alternatives
- Uncertain about optimal approach
- Sufficient sample for multiple comparisons

**Design considerations:**
- Apply multiple testing correction (Bonferroni, Holm)
- Consider using control as baseline for all comparisons
- Sample size requirement increases with variants

### Multivariate Test (MVT)

Test combinations of multiple factors simultaneously.

**Use when:**
- Multiple elements may interact
- Want to measure interaction effects
- Large traffic volume available

**Design considerations:**
- Full factorial vs fractional factorial design
- Cell sizes decrease rapidly with factors
- Main effects vs interaction effects interpretation

### Multi-Armed Bandit

Dynamic allocation shifting traffic to winning variants.

**Use when:**
- Minimizing opportunity cost important
- Less concern about statistical inference
- Continuous optimization context

**Design considerations:**
- Thompson Sampling or UCB algorithms
- Regret minimization vs inference tradeoff
- May not provide valid p-values

### Geo Experiments

Randomize at geographic region level.

**Use when:**
- Cannot randomize individual users
- Treatment causes spillover effects
- Testing marketing/pricing across regions

**Design considerations:**
- Limited sample size (number of regions)
- Regional heterogeneity complicates analysis
- Synthetic control methods for analysis

### Switchback Experiments

Alternate treatments over time periods.

**Use when:**
- Marketplace with supply-demand dynamics
- Network effects prevent user-level tests
- Limited geographic variation

**Design considerations:**
- Carryover effects between periods
- Washout periods may be needed
- Time-based confounders possible

---

## Randomization Strategies

### Randomization Unit Selection

| Unit | Pros | Cons | Use When |
|------|------|------|----------|
| User ID | Consistent experience | Identity requirements | Product experiments |
| Device ID | Cross-session stability | Multi-device users split | Mobile apps |
| Session | No identity needed | Inconsistent experience | Anonymous traffic |
| Cookie | Web-friendly | Cookie deletion | Web experiments |
| Geographic | Handles spillover | Low sample size | Network effects |
| Time period | Simple implementation | Temporal confounders | Switchback designs |

### Assignment Mechanisms

**Hash-based assignment:**
```
hash(user_id + experiment_id) % 100 < traffic_percentage
```

Benefits:
- Deterministic (same input = same output)
- No storage required
- Consistent across systems

**Stratified randomization:**

Randomize within strata to ensure balance on important covariates.

| Stratification Variable | Benefit |
|------------------------|----------|
| Platform (iOS/Android/Web) | Balance device effects |
| Country/Region | Balance geographic effects |
| User tenure | Balance new vs existing |
| Traffic source | Balance acquisition channel |

---

## Metric Definition

### Primary Metric (OEC)

Overall Evaluation Criterion should be:
- Directly tied to business value
- Sensitive to treatment effect
- Measurable within experiment timeframe
- Robust to manipulation

### Metric Types

| Type | Examples | Considerations |
|------|----------|----------------|
| Rate/Proportion | Conversion rate, CTR | Binomial distribution |
| Mean | Revenue per user, session duration | Often right-skewed |
| Count | Purchases per user | Poisson or negative binomial |
| Ratio | Revenue per click | Variance estimation complex |
| Quantile | Median latency | Bootstrap for inference |

### Secondary Metrics

Include metrics that:
- Explain mechanism of primary metric change
- Capture different aspects of user value
- Have different time horizons

### Guardrail Metrics

Metrics that must not degrade significantly:
- Error rates and system health
- Other business metrics not expected to change
- Long-term engagement proxies

---

## Experiment Duration

### Duration Calculation

Duration = Sample Size Required ÷ Daily Eligible Traffic × Traffic Allocation

### Minimum Duration Rules

| Factor | Minimum Duration |
|--------|------------------|
| Day-of-week effects | 7 days (full week) |
| Business cycle | 14-28 days |
| Purchase cycle | Match typical cycle |
| Novelty effects | 2-4 weeks |
| Learning effects | 4+ weeks |

---

## Pre-Registration

### Required Pre-Registration Elements

1. **Experiment metadata**: Name, owner, dates
2. **Hypothesis**: Clear statement of expected effect
3. **Metrics**: Primary, secondary, guardrails with definitions
4. **Sample size**: Calculation and assumptions
5. **Analysis plan**: Statistical methods, corrections
6. **Decision criteria**: What constitutes success
7. **Stopping rules**: Early termination conditions

Pre-register before seeing any results to prevent p-hacking and HARKing (Hypothesizing After Results Known).
