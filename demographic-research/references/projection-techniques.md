# Demographic Projection Techniques

## Cohort-Component Method

The standard method for demographic projections. Projects each age-sex cohort forward using:

### Three Components

1. **Fertility**: Age-specific fertility rates applied to women of childbearing age (15-49)
   - Produce births by age of mother
   - Apply sex ratio at birth (~105 males per 100 females)
   - Survive births to end of projection interval

2. **Mortality**: Age-sex-specific survival rates
   - Apply life table survival ratios to each cohort
   - Cohort at age x in year t → survivors at age x+n in year t+n
   - Use model life tables or empirical data

3. **Migration**: Age-sex-specific net migration rates or counts
   - Most uncertain component
   - Apply migration at midpoint of interval
   - Domestic + international migration

### Projection Scenarios

| Scenario | Fertility | Mortality | Migration | Purpose |
|---|---|---|---|---|
| Low | Below replacement | Slower improvement | Net negative | Floor estimate |
| Medium | Moderate convergence | Trend continuation | Net moderate | Best estimate |
| High | Above replacement | Faster improvement | Net positive | Ceiling estimate |

---

## Trend Extrapolation Methods

### Linear Extrapolation
- Extend historical growth rate forward
- Simple but assumes constant absolute change
- Useful for short-term (1-5 year) projections

### Exponential Extrapolation
- Extend historical growth rate as percentage
- Assumes constant relative change
- Better for populations with sustained growth

### Logistic Growth Model
- Assumes carrying capacity constraint
- S-curve approach to population ceiling
- Appropriate for bounded geographic areas

---

## Housing Unit Method

Alternative to cohort-component for small areas:

1. Project number of housing units (from permits, construction data)
2. Apply occupancy rates
3. Apply persons-per-household ratios
4. Estimate total population

Best for: Short-term projections in small, fast-changing areas

---

## Validation and Uncertainty

### Backcasting
- Apply projection methodology to historical data
- Compare projected values to actual observed values
- Calculate mean absolute percentage error (MAPE)

### Sensitivity Analysis
- Vary each component independently
- Identify which assumptions drive the most uncertainty
- Document assumption sensitivity in all projection deliverables

### Confidence Intervals
- Use scenario range as rough confidence interval
- Widen intervals for longer projection horizons
- Rule of thumb: accuracy degrades ~1-2% per year of projection horizon

---

## Reporting Projections

Always document:
- Base year data source and vintage
- Methodology selected and rationale
- All assumptions (fertility, mortality, migration) with sources
- Scenario definitions (low, medium, high)
- Limitations and caveats
- Recommended review/update frequency
