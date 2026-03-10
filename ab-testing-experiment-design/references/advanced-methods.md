# Advanced Experimentation Methods

Bayesian approaches, sequential testing, and bandits for sophisticated experimentation.

---

## Bayesian A/B Testing

### Frequentist vs Bayesian

| Aspect | Frequentist | Bayesian |
|--------|-------------|----------|
| Probability of | Data given hypothesis | Hypothesis given data |
| Prior beliefs | Not incorporated | Explicitly modeled |
| Output | P-value, CI | Posterior distribution |
| Interpretation | Indirect | Direct probability statements |
| Sample size | Fixed in advance | Can be flexible |

### Bayesian Framework
```
Posterior ∝ Likelihood × Prior

P(θ|data) ∝ P(data|θ) × P(θ)

Where θ = conversion rate
```

### Beta-Binomial Model
For conversion rate testing:
```
Prior: θ ~ Beta(α, β)
Likelihood: x ~ Binomial(n, θ)
Posterior: θ|x ~ Beta(α + x, β + n - x)

Common prior: Beta(1, 1) = Uniform
Weakly informative: Beta(0.5, 0.5)
```

### Probability to Beat Control
```
P(Treatment > Control) = 
  ∫∫ I(θT > θC) × P(θT) × P(θC) dθT dθC

Computed via Monte Carlo sampling:
1. Draw 10,000 samples from each posterior
2. Count proportion where Treatment > Control
3. Report as "95% probability B beats A"
```

### Decision Rules
| P(B > A) | Decision |
|----------|----------|
| > 95% | Ship B |
| 5% - 95% | Continue testing |
| < 5% | Ship A (or continue) |

### Advantages of Bayesian
- Can peek at results
- Direct probability statements
- Incorporates prior knowledge
- Natural for sequential decisions

### Disadvantages
- Requires choosing priors
- Computationally intensive
- Less standardized
- Prior can influence results

---

## Sequential Testing

### The Peeking Problem
Looking at results repeatedly inflates Type I error.
```
If you peek daily for 20 days at α=0.05:
- True α ≈ 20-25% (not 5%)
```

### Sequential Probability Ratio Test (SPRT)
Tests hypotheses as data accumulates.

```
Likelihood ratio: Λ = P(data|H1) / P(data|H0)

Boundaries:
- Upper: A = (1-β)/α
- Lower: B = β/(1-α)

Decision:
- If Λ > A: Reject H0 (B wins)
- If Λ < B: Accept H0 (A wins)
- If B < Λ < A: Continue testing
```

### Group Sequential Methods

#### O'Brien-Fleming Boundaries
Very conservative early, relaxed later.
```
Analysis | Z-boundary | Cumulative α
---------|------------|-------------
25%      | 4.05       | 0.0001
50%      | 2.86       | 0.004
75%      | 2.34       | 0.019
100%     | 2.02       | 0.05
```

#### Pocock Boundaries
Constant boundary across analyses.
```
Analysis | Z-boundary | Cumulative α
---------|------------|-------------
25%      | 2.36       | 0.009
50%      | 2.36       | 0.019
75%      | 2.36       | 0.030
100%     | 2.36       | 0.05
```

### Alpha Spending Functions
Flexible allocation of Type I error across analyses.
```
Options:
- Pocock-like: Linear spending
- O'Brien-Fleming-like: Exponential spending
- Custom: Specify your own function
```

### Implementing Sequential Tests
1. Define maximum sample size
2. Choose spending function
3. Specify analysis schedule (e.g., weekly)
4. Calculate boundaries for each analysis
5. Stop when boundary crossed or max reached

---

## Multi-Armed Bandits

### Concept
Balance exploration (learning) vs exploitation (winning).

### Algorithms

#### Epsilon-Greedy
```python
def epsilon_greedy(epsilon=0.1):
    if random() < epsilon:
        return random_arm()  # Explore
    else:
        return best_arm()    # Exploit
```
Simple but suboptimal.

#### Thompson Sampling
```python
def thompson_sampling(successes, failures):
    samples = [beta_sample(s+1, f+1) 
               for s, f in zip(successes, failures)]
    return argmax(samples)
```
Optimal for binary outcomes.

#### Upper Confidence Bound (UCB)
```python
def ucb(means, counts, t):
    exploration = sqrt(2 * log(t) / counts)
    return argmax(means + exploration)
```
Theoretically motivated, good performance.

### Bandits vs A/B Tests

| Aspect | A/B Test | Bandit |
|--------|----------|--------|
| Goal | Statistical inference | Maximize reward |
| Traffic split | Fixed | Adaptive |
| Regret | Higher | Lower |
| Statistical power | Standard | Reduced |
| Best for | Learning | Optimizing |

### When to Use Bandits
- Continuous optimization (no "end")
- Personalization
- High opportunity cost of testing
- Many variants to test quickly
- Recommendation systems

### When NOT to Use Bandits
- Need statistically valid inference
- Want to understand effect sizes
- Regulatory/compliance requirements
- Results will inform future decisions

---

## Contextual Bandits

### Concept
Personalize treatment based on user features.

```
For user x:
  Choose arm a = argmax E[reward | x, a]
```

### Algorithms
- **LinUCB**: Linear reward model + UCB
- **Neural bandits**: Deep learning for reward
- **Thompson Sampling with context**: Bayesian approach

### Use Cases
- Content personalization
- Product recommendations
- Dynamic pricing
- Ad targeting

---

## Causal Inference Methods

### Difference-in-Differences
When randomization isn't possible.
```
Effect = (Treatment_after - Treatment_before) - 
         (Control_after - Control_before)
```

### Propensity Score Matching
Match treated/untreated users by probability of treatment.
```
1. Model P(treatment | X) 
2. Match treated to untreated with similar scores
3. Compare outcomes in matched pairs
```

### Regression Discontinuity
When treatment assigned by threshold.
```
Users just above/below threshold are similar,
so compare outcomes near the cutoff.
```

### Synthetic Control
Create artificial control group from weighted combination.
```
Used for aggregate outcomes where individual
randomization isn't possible (e.g., city-level).
```

---

## Experiment Platforms

### Build vs Buy
| Factor | Build | Buy |
|--------|-------|-----|
| Customization | Full | Limited |
| Time to deploy | Months | Days |
| Maintenance | Ongoing | Included |
| Cost | Engineering time | Subscription |
| Scale | Design for needs | Usually sufficient |

### Key Platform Features
- Randomization infrastructure
- Metric logging integration
- Statistical analysis engine
- Sequential testing support
- Segment analysis
- Experiment management UI

### Major Platforms
| Platform | Strengths | Best For |
|----------|-----------|----------|
| Optimizely | Full-featured, enterprise | Large orgs |
| LaunchDarkly | Feature flags + experiments | Dev teams |
| Amplitude Experiment | Analytics integration | Product teams |
| Statsig | Modern, fast iteration | Tech companies |
| Eppo | Warehouse-native | Data teams |
| Custom | Full control | Unique needs |

---

## Advanced Topics

### Network Effects / Interference
When one user's treatment affects another's outcome.
```
Solutions:
- Cluster randomization (by geography, network)
- Graph cluster randomization
- Ego-network designs
```

### Switchback Experiments
Alternate treatment over time periods.
```
Good for:
- Marketplace experiments
- When interference is high
- Operational experiments
```

### Long-Term Effects
Measuring impacts beyond test window.
```
Approaches:
- Extended holdouts
- Surrogate metrics
- Long-term modeling
```

### Experimentation Culture
Building organizational capabilities:
1. Centralized platform team
2. Self-serve for simple experiments
3. Statistical review for complex ones
4. Knowledge sharing system
5. Experimentation metrics (velocity, impact)

---

## Method Selection Guide

```
Start: What's your goal?

├─ Learn causal effect with certainty
│   └─ A/B test (frequentist or Bayesian)
│
├─ Need to stop early if winning
│   └─ Sequential testing or Bayesian
│
├─ Maximize conversions during test
│   └─ Multi-armed bandit
│
├─ Personalize based on user attributes
│   └─ Contextual bandit
│
├─ Can't randomize individuals
│   ├─ Can randomize clusters → Cluster RCT
│   └─ No randomization → Quasi-experimental
│
└─ Test many variants quickly
    └─ Bandit for screening, A/B for validation
```
