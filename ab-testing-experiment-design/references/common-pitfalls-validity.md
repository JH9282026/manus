# Common Pitfalls & Validity Threats

Guide to avoiding mistakes and ensuring valid experiment results.

---

## Validity Threats

### Internal Validity Threats

| Threat | Description | Detection | Mitigation |
|--------|-------------|-----------|------------|
| Selection Bias | Non-random sample | Covariate imbalance | Proper randomization |
| Sample Ratio Mismatch | Unequal assignment | Chi-square test | Fix assignment bugs |
| Instrumentation | Tracking differences | AA tests | Verify logging parity |
| Interference | Units affect each other | Network analysis | Cluster randomization |
| Attrition | Differential dropout | Compare drop rates | Intent-to-treat analysis |
| Novelty Effect | Temporary curiosity | Time-based analysis | Longer duration |
| Hawthorne Effect | Awareness changes behavior | Blind experiments | Minimize awareness |

### External Validity Threats

| Threat | Description | Mitigation |
|--------|-------------|------------|
| Population | Sample doesn't represent target | Verify eligibility criteria |
| Temporal | Time-specific effects | Replicate across periods |
| Scale | Effect changes at scale | Gradual rollout verification |
| Context | Platform/market differences | Cross-context replication |

---

## Sample Ratio Mismatch (SRM)

### What is SRM?

When observed assignment ratio differs significantly from expected ratio.

**Example:** Expected 50/50 split, observed 51.5/48.5 with p < 0.001

### SRM Causes and Fixes

| Cause | How to Detect | Fix |
|-------|---------------|-----|
| Assignment bug | Code review | Fix randomization logic |
| Redirect failures | Check 3xx rates | Fix redirect handling |
| Bot traffic | Bot rate by variant | Filter bots |
| Browser crashes | Device analysis | Fix compatibility |
| Logging failures | Compare assignment vs exposure | Fix logging |
| Performance impact | Latency by variant | Address performance |
| Opt-out differences | Consent rates | Investigate opt-out |

### SRM Response Protocol

1. **Stop**: Do not trust results if SRM detected
2. **Investigate**: Find root cause
3. **Fix**: Address underlying issue
4. **Restart**: May need to restart experiment
5. **Validate**: Confirm SRM resolved

---

## Common Statistical Mistakes

### Mistake 1: Peeking at Results

**Problem:** Checking results before reaching sample size inflates Type I error.

**Impact:**
- 5 peeks → actual α ≈ 14%
- Continuous monitoring → actual α ≈ 40%

**Solution:**
- Pre-specify analysis time
- Use sequential testing methods
- Lock yourself out until complete

### Mistake 2: Multiple Testing Without Correction

**Problem:** Testing many variants or metrics without adjustment.

**Impact:** With 20 tests at α=0.05, expect 1 false positive by chance.

**Solution:**
- Apply Bonferroni, Holm, or FDR correction
- Pre-specify primary metric
- Treat additional analyses as exploratory

### Mistake 3: Stopping Early on Significance

**Problem:** Stopping when p < 0.05 at any sample size.

**Impact:** Biased effect size estimates, inflated false positive rate.

**Solution:**
- Run to pre-specified sample size
- Use sequential testing if early stopping needed
- Pre-register stopping rules

### Mistake 4: Ignoring Practical Significance

**Problem:** Focusing only on statistical significance.

**Impact:** Shipping changes with negligible real-world impact.

**Solution:**
- Define minimum detectable effect based on business value
- Report effect sizes with confidence intervals
- Evaluate against practical thresholds

### Mistake 5: Segmentation Without Correction

**Problem:** Analyzing many segments and reporting significant ones.

**Impact:** Most "significant" segments are false positives.

**Solution:**
- Pre-specify segments of interest
- Apply multiple testing correction
- Require larger effect sizes for segments
- Validate in follow-up experiments

### Mistake 6: Survivorship Bias

**Problem:** Analyzing only users who completed a flow.

**Impact:** Miss effect on users who dropped out.

**Solution:**
- Use intent-to-treat analysis
- Include all randomized users
- Analyze dropout rates separately

---

## Design Mistakes

### Mistake: Contamination Between Variants

**Problem:** Users in one variant are exposed to another.

**Causes:**
- Multiple devices
- Shared accounts
- Word-of-mouth
- Cache issues

**Solution:**
- User-level (not session) randomization
- Clear cookies/cache on variant changes
- Consider household-level randomization

### Mistake: Inconsistent Treatment

**Problem:** Treatment changes during experiment or varies by context.

**Impact:** Effect dilution, inconsistent experience.

**Solution:**
- Lock treatment at first exposure
- Version control treatments
- Monitor treatment fidelity

### Mistake: Wrong Randomization Unit

**Problem:** Using session randomization when user-level needed (or vice versa).

**Impact:**
- Session-level: Same user gets different experiences
- User-level: Missed data without identity

**Solution:** Match unit to:
- Experience consistency needs
- Metric aggregation level
- Identity availability

### Mistake: Testing Too Many Changes

**Problem:** Large "redesign" experiments with many changes.

**Impact:** Cannot attribute effect to specific changes.

**Solution:**
- Isolate changes when possible
- Use multivariate testing for interactions
- Accept attribution limitations for large changes

---

## Analysis Mistakes

### Mistake: Ratio Metric Errors

**Problem:** Incorrect variance estimation for ratio metrics.

**Example:** Revenue per user = Total Revenue / Total Users

**Solution:**
- Use delta method for variance
- Consider linearization techniques
- Bootstrap for complex ratios

### Mistake: Not Accounting for Novelty

**Problem:** Measuring only initial response, not long-term effect.

**Detection:**
- Effect decreases over experiment duration
- New users show different effect than returning

**Solution:**
- Run experiments longer (4+ weeks)
- Compare effect by user tenure
- Compare early vs late experiment periods

### Mistake: Ignoring Network Effects

**Problem:** User-level randomization when users interact.

**Examples:**
- Marketplace (buyers/sellers interact)
- Social features (sharing affects others)
- Supply-constrained (showing different prices)

**Solution:**
- Cluster randomization (geographic, time)
- Synthetic control methods
- Carefully model interference

---

## Process Mistakes

### Mistake: No Pre-Registration

**Problem:** Defining hypothesis after seeing results (HARKing).

**Impact:** Inflated false positive rate, confirmation bias.

**Solution:**
- Document hypothesis before data collection
- Lock analysis plan in versioned document
- Separate confirmatory from exploratory

### Mistake: Insufficient Power

**Problem:** Running underpowered experiments that cannot detect realistic effects.

**Impact:** False negatives, wasted time, incorrect conclusions.

**Solution:**
- Calculate required sample size before starting
- Use variance reduction techniques
- Accept longer duration or larger MDE

### Mistake: Not Documenting Decisions

**Problem:** No record of why decisions were made.

**Impact:** Cannot learn from past, repeat mistakes.

**Solution:**
- Maintain experiment repository
- Document all decisions and rationale
- Review past experiments before new ones

---

## Pre-Experiment Checklist

### Before Launch

- [ ] Hypothesis clearly stated and pre-registered
- [ ] Primary metric defined with calculation spec
- [ ] Sample size calculated with realistic assumptions
- [ ] Experiment duration planned
- [ ] Randomization unit appropriate for use case
- [ ] Assignment implementation tested
- [ ] Exposure logging verified
- [ ] Guardrail metrics identified
- [ ] Stopping rules defined
- [ ] Stakeholders aligned on decision criteria

### During Experiment

- [ ] Check SRM daily
- [ ] Monitor guardrail metrics
- [ ] Track sample size progress
- [ ] Avoid peeking at primary metric
- [ ] Document any issues

### Before Analysis

- [ ] Confirm no SRM
- [ ] Verify minimum sample reached
- [ ] Check for data quality issues
- [ ] Review pre-registered analysis plan

### Before Decision

- [ ] Results match pre-specified primary metric
- [ ] Confidence intervals reported
- [ ] Guardrails checked
- [ ] Validity threats assessed
- [ ] Practical significance evaluated
- [ ] Decision documented with rationale
