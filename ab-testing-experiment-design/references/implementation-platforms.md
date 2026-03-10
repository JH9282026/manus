# Implementation & Platforms

Guide to experimentation infrastructure, platforms, and monitoring.

---

## Experimentation Platforms

### Platform Comparison

| Platform | Type | Best For | Pricing Model |
|----------|------|----------|---------------|
| Optimizely | Full-stack | Enterprise web/product | Per MAU |
| LaunchDarkly | Feature flags | Developer-centric | Per seat/MAU |
| Google Optimize | Web testing | Marketing tests | Free/360 |
| VWO | Web testing | Conversion optimization | Per MAU |
| Amplitude Experiment | Analytics-native | Product analytics users | Per MTU |
| Statsig | Full-stack | Fast-moving teams | Per MAU |
| Eppo | Warehouse-native | Data warehouse users | Per seat |
| Split | Feature flags | Enterprise DevOps | Per seat |
| AB Tasty | Web testing | Marketing teams | Per traffic |
| Custom | Build your own | Full control needed | Development cost |

### Platform Selection Criteria

| Criterion | Questions to Ask |
|-----------|------------------|
| Integration | Works with existing stack? SDK quality? |
| Statistics | What methods supported? Sequential testing? |
| Scale | Handle your traffic volume? Latency? |
| Features | Feature flags? Segments? Holdouts? |
| Analytics | Built-in analysis? Data export? |
| Governance | Approval workflows? Audit trails? |
| Support | Documentation? Customer support? |
| Cost | Per-user vs per-seat? Scale economics? |

---

## Assignment Architecture

### Client-Side Assignment

**Architecture:**
```
User Request → Page Load → JS SDK → Assignment → Render Variant
```

**Pros:**
- Easy implementation
- No backend changes
- Visual editor support

**Cons:**
- Flicker effect possible
- Limited to UI changes
- Blocked by ad blockers

### Server-Side Assignment

**Architecture:**
```
User Request → Server → SDK Assignment → Build Response → Render
```

**Pros:**
- No flicker
- Backend logic testing
- Not blocked by ad blockers
- More reliable

**Cons:**
- Backend integration required
- Slower initial implementation

### Edge Assignment

**Architecture:**
```
User Request → CDN/Edge → Assignment → Route to Origin
```

**Pros:**
- Low latency
- Works without origin change
- Can modify requests/responses

**Cons:**
- Limited edge capabilities
- Complex debugging

---

## Assignment Implementation

### Hash-Based Assignment

```python
import hashlib

def get_variant(user_id: str, experiment_id: str, traffic_pct: float = 100) -> str:
    """Deterministic variant assignment using hashing."""
    hash_input = f"{user_id}:{experiment_id}"
    hash_value = int(hashlib.md5(hash_input.encode()).hexdigest(), 16)
    bucket = hash_value % 10000  # 0-9999 for 0.01% granularity
    
    # Check if user is in experiment
    if bucket >= traffic_pct * 100:
        return None  # Not in experiment
    
    # Assign to variant (50/50 split)
    if bucket % 2 == 0:
        return "control"
    return "treatment"
```

### Assignment Best Practices

1. **Consistent hashing**: Same user always gets same variant
2. **Experiment isolation**: Different salt per experiment
3. **Sticky assignment**: Cache assignment for session
4. **Logging**: Log assignment at time of assignment
5. **Exposure logging**: Log when user actually sees variant

---

## Event Tracking

### Required Events

| Event Type | Purpose | Example |
|------------|---------|----------|
| Assignment | Record variant assignment | `experiment_assigned` |
| Exposure | Record variant seen | `experiment_exposed` |
| Conversion | Primary metric events | `purchase_completed` |
| Engagement | Secondary metrics | `button_clicked` |
| Guardrail | Health monitoring | `error_occurred` |

### Event Schema

```json
{
  "event_type": "experiment_exposed",
  "timestamp": "2024-01-15T10:30:00Z",
  "user_id": "user_123",
  "session_id": "sess_456",
  "experiment_id": "checkout_redesign_v2",
  "variant": "treatment",
  "properties": {
    "page": "checkout",
    "device": "mobile"
  }
}
```

### Exposure Logging

Log exposure at the moment user actually experiences the variant:

| Scenario | When to Log Exposure |
|----------|---------------------|
| Page variant | Page load complete |
| Feature flag | Feature rendered |
| Algorithm | Recommendation shown |
| Backend logic | Action processed |

---

## Monitoring Dashboard

### Essential Metrics to Monitor

| Metric | Purpose | Alert Threshold |
|--------|---------|----------------|
| Sample Ratio | Assignment balance | >1% deviation |
| Sample Size | Progress tracking | Behind schedule |
| Primary Metric | Early signal | Guardrail breach |
| Error Rates | Health check | Significant increase |
| Latency | Performance impact | P99 degradation |

### Sample Ratio Mismatch (SRM)

Critical health check: Compare expected vs actual assignment ratio.

```python
from scipy import stats

def check_srm(control_n: int, treatment_n: int, expected_ratio: float = 0.5) -> tuple:
    """Check for Sample Ratio Mismatch."""
    total = control_n + treatment_n
    expected_control = total * expected_ratio
    expected_treatment = total * (1 - expected_ratio)
    
    chi2, p_value = stats.chisquare(
        [control_n, treatment_n],
        [expected_control, expected_treatment]
    )
    
    srm_detected = p_value < 0.001
    return srm_detected, p_value
```

**SRM Causes:**
- Assignment bugs
- Bot traffic differences
- Redirect failures
- Browser compatibility
- Logging failures

---

## Feature Flag Integration

### Feature Flag vs Experiment

| Aspect | Feature Flag | Experiment |
|--------|--------------|------------|
| Purpose | Control rollout | Measure impact |
| Assignment | Usually % rollout | Random split |
| Analysis | Optional | Required |
| Duration | Can be permanent | Temporary |
| Metrics | Not primary concern | Core purpose |

### Using Flags for Experiments

1. Create flag with experiment configuration
2. Define variant payloads
3. Enable random assignment
4. Configure exposure logging
5. Run experiment
6. Analyze and decide
7. Graduate flag to permanent or remove

---

## Data Pipeline

### Experiment Data Flow

```
Assignment Events → Event Stream → Data Warehouse → Metric Calculation → Analysis
         ↓                                    ↓
    Exposure Events                    Experiment Results
         ↓                                    ↓
    Outcome Events                      Dashboard/Reports
```

### Metric Calculation Approaches

| Approach | Latency | Flexibility | Complexity |
|----------|---------|-------------|------------|
| Pre-aggregated | Low | Low | Low |
| Query-time | Medium | High | Medium |
| Streaming | Real-time | Medium | High |

---

## Holdout Groups

### Purpose

Measure cumulative impact of all experiments over time.

### Implementation

1. Randomly assign 1-5% of users to holdout
2. Holdout users get control for ALL experiments
3. Compare holdout vs non-holdout periodically
4. Measures combined effect of shipped changes

### Holdout Design

| Parameter | Recommendation |
|-----------|----------------|
| Size | 1-5% of traffic |
| Duration | 6-12 months |
| Rotation | Optional refresh |
| Scope | Global or product-specific |
