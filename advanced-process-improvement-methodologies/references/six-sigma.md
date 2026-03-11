# Six Sigma Methodology

Comprehensive guide to Six Sigma principles, DMAIC, and statistical tools.

---

## Six Sigma Philosophy

### Core Principles

- **Customer Focus**: Define quality from customer's perspective
- **Data-Driven**: Base decisions on statistical analysis
- **Process Focus**: Improve processes for consistent results
- **Variation Reduction**: Minimize variation to reduce defects
- **Root Cause Analysis**: Address underlying causes

### Sigma Levels

| Sigma Level | DPMO | Yield |
|-------------|------|-------|
| 1 | 691,462 | 30.85% |
| 2 | 308,538 | 69.15% |
| 3 | 66,807 | 93.32% |
| 4 | 6,210 | 99.38% |
| 5 | 233 | 99.977% |
| 6 | 3.4 | 99.99966% |

---

## DMAIC Methodology

### Define Phase

**Objectives**:
- Identify problem and project goals
- Define customer requirements (Voice of Customer)
- Create project charter
- Map high-level process (SIPOC)

**Deliverables**:
- Project charter with scope, timeline, team
- SIPOC diagram
- Problem statement (quantified)
- Business case

### Measure Phase

**Objectives**:
- Identify critical-to-quality (CTQ) metrics
- Develop data collection plan
- Validate measurement system
- Establish baseline

**Deliverables**:
- Data collection plan
- Measurement System Analysis (Gage R&R)
- Baseline metrics
- Detailed process maps

### Analyze Phase

**Objectives**:
- Identify potential root causes
- Conduct statistical analysis
- Validate root causes with data
- Prioritize causes by impact

**Tools**:
- 5 Whys
- Fishbone (Ishikawa) diagram
- Hypothesis testing
- Regression analysis

### Improve Phase

**Objectives**:
- Generate potential solutions
- Evaluate and select best solutions
- Pilot on small scale
- Implement full-scale

**Deliverables**:
- Solution designs
- Pilot results
- Implementation plan
- Validated improvements

### Control Phase

**Objectives**:
- Develop control plan
- Implement statistical process control
- Document procedures
- Hand off to process owner

**Deliverables**:
- Control plan
- Updated SOPs
- Training documentation
- Control charts

---

## Statistical Tools

### Hypothesis Testing

**Common Tests**:
- **t-test**: Compare means of two groups
- **ANOVA**: Compare means of multiple groups
- **Chi-Square**: Test categorical data relationships
- **Regression**: Test relationships between variables

**Process**:
1. State null hypothesis (H0) and alternative (H1)
2. Select significance level (typically alpha = 0.05)
3. Calculate test statistic and p-value
4. Compare p-value to significance level
5. Draw conclusion

### Process Capability

**Key Metrics**:
- **Cp**: Process potential capability
- **Cpk**: Actual capability (accounts for centering)
- **Pp/Ppk**: Performance indices (overall variation)

**Interpretation**:
- Cpk >= 1.33: Process is capable
- Cpk = 1.0: Just meets specifications
- Cpk < 1.0: Not capable

---

## Root Cause Analysis

### 5 Whys

Ask "why" repeatedly to drill to root cause:

1. Machine stopped - Why?
2. Fuse blew - Why?
3. Bearing not lubricated - Why?
4. Pump not working - Why?
5. Shaft worn from metal scrap - ROOT CAUSE

### Fishbone Diagram

Categories (6Ms for Manufacturing):
- Man
- Machine
- Method
- Material
- Measurement
- Mother Nature (Environment)

---

## Design of Experiments (DOE)

### Concepts

- **Factors**: Input variables being tested
- **Levels**: Different values of each factor
- **Response**: Output being measured
- **Main Effects**: Impact of individual factors
- **Interactions**: Combined effects of factors

### Types

- **Full Factorial**: All combinations (comprehensive)
- **Fractional Factorial**: Subset (efficient)
- **Taguchi Methods**: Focus on robustness

---

## Belt System

| Belt | Role | Training |
|------|------|----------|
| Yellow | Team member | 1-2 days |
| Green | Part-time project leader | 2-3 weeks |
| Black | Full-time project leader | 4 weeks |
| Master Black | Program leader, coach | Additional training |
| Champion | Executive sponsor | Overview |
