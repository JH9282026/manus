# Experimental Design Methods

## Factorial Designs

### Full Factorial
Run all possible combinations of factor levels.
- 2 factors × 2 levels = 2² = 4 runs
- 3 factors × 2 levels = 2³ = 8 runs
- k factors × 2 levels = 2^k runs

**Advantages**: Estimates all main effects and interactions
**Disadvantages**: Run count grows exponentially with factors

### Fractional Factorial (2^(k-p) designs)
Run a carefully selected fraction of the full factorial.
- Use when full factorial is too expensive
- Confounds (aliases) higher-order interactions with main effects
- Resolution III: Main effects clear of each other, confounded with 2-way interactions
- Resolution IV: Main effects clear of 2-way interactions
- Resolution V: 2-way interactions clear of each other

### Plackett-Burman Designs
Screening designs for identifying important factors from many candidates.
- Efficient: Test k factors in k+1 runs (nearest multiple of 4)
- Only estimates main effects (no interactions)
- Use as first step, then follow up with factorial on important factors

---

## Blocking Strategies

### Randomized Complete Block Design (RCBD)
- Group experimental units into blocks based on known variability source
- Run all treatments within each block
- Reduces error variance by accounting for block-to-block differences
- Example: Test 4 marketing messages, blocked by customer segment

### Incomplete Block Designs
- When blocks are too small to include all treatments
- Balanced Incomplete Block Design (BIBD): Every pair of treatments appears together equally often
- Use when physical or practical constraints limit block size

---

## Response Surface Methodology (RSM)

### Central Composite Design (CCD)
For optimizing a response variable with continuous factors:
1. Start with factorial or fractional factorial (corner points)
2. Add center points (replicated for pure error estimate)
3. Add axial/star points (extend the design space)
4. Fit second-order polynomial model
5. Find optimal settings using response surface plots

### Box-Behnken Design
Alternative to CCD:
- No extreme corner points (good when factor extremes are impractical)
- Fewer runs than CCD for 3+ factors
- Estimates all quadratic and interaction terms

---

## Sequential Experimentation

### Strategy
1. **Screening phase**: Test many factors with fractional factorial or Plackett-Burman
2. **Characterization phase**: Full factorial on important factors, study interactions
3. **Optimization phase**: Response surface methods to find optimal settings
4. **Confirmation phase**: Verify optimal settings with replication

### Adaptive Designs
- **Group sequential**: Analyze data at predetermined interim looks
- **Bayesian adaptive**: Update probability model as data accumulates
- **Multi-armed bandit**: Allocate more traffic to winning variants during test
- Trade-off: Faster decisions vs. classical statistical guarantees

---

## Sample Size Calculation

### For Comparing Two Means
n per group = 2(Z_α/2 + Z_β)² × σ² / δ²

Where:
- Z_α/2 = critical value for significance level (1.96 for α=0.05)
- Z_β = critical value for power (0.84 for 80% power)
- σ = standard deviation of outcome
- δ = minimum detectable difference

### For Comparing Two Proportions
n per group = (Z_α/2 √(2p̄(1-p̄)) + Z_β √(p₁(1-p₁)+p₂(1-p₂)))² / (p₁-p₂)²

### Power Analysis Tools
- G*Power (free software)
- R: `pwr` package
- Python: `statsmodels.stats.power`
- Online calculators (Evan Miller, Optimizely)
