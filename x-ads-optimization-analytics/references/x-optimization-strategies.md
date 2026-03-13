# X Ads Optimization Strategies

Advanced optimization techniques for X advertising campaigns.

---

## Bid Optimization

### Dynamic Bid Adjustment

```python
def calculate_optimal_bid(current_stats, target_metrics):
    """
    Adjust bids based on performance vs targets.
    """
    current_cpa = current_stats['spend'] / current_stats['conversions']
    target_cpa = target_metrics['cpa']
    
    # Calculate adjustment factor
    if current_cpa > target_cpa * 1.2:
        # Too expensive, reduce bid
        adjustment = 0.80
    elif current_cpa > target_cpa:
        # Slightly expensive, small reduction
        adjustment = 0.95
    elif current_cpa < target_cpa * 0.7:
        # Very efficient, increase bid to scale
        adjustment = 1.20
    elif current_cpa < target_cpa:
        # Efficient, moderate increase
        adjustment = 1.10
    else:
        # On target
        adjustment = 1.0
    
    new_bid = int(current_stats['bid_amount'] * adjustment)
    
    # Apply min/max constraints
    min_bid = 500000  # $0.50
    max_bid = 10000000  # $10
    
    return max(min_bid, min(new_bid, max_bid))
```

### Time-Based Bidding

```python
def adjust_bid_by_hour(base_bid, hour_performance):
    """
    Increase bids during high-performing hours.
    """
    hour_multipliers = {
        9: 1.2,   # Morning peak
        12: 1.15, # Lunch
        18: 1.3,  # Evening peak
        22: 0.8   # Late night
    }
    
    current_hour = datetime.now().hour
    multiplier = hour_multipliers.get(current_hour, 1.0)
    
    return int(base_bid * multiplier)
```

---

## Creative Optimization

### Multi-Armed Bandit Testing

```python
import numpy as np

class CreativeOptimizer:
    def __init__(self, creative_ids):
        self.creatives = {cid: {'impressions': 0, 'conversions': 0} for cid in creative_ids}
    
    def select_creative(self, epsilon=0.1):
        """Epsilon-greedy selection."""
        if np.random.random() < epsilon:
            # Explore: random selection
            return np.random.choice(list(self.creatives.keys()))
        else:
            # Exploit: best performer
            best = max(self.creatives.items(), 
                      key=lambda x: x[1]['conversions'] / max(x[1]['impressions'], 1))
            return best[0]
    
    def update(self, creative_id, conversions, impressions):
        self.creatives[creative_id]['conversions'] += conversions
        self.creatives[creative_id]['impressions'] += impressions
```

### Creative Fatigue Detection

```python
def detect_creative_fatigue(creative_stats, window_days=7):
    """
    Identify creatives with declining performance.
    """
    recent = creative_stats[-window_days:]
    older = creative_stats[-window_days*2:-window_days]
    
    recent_ctr = sum(s['clicks'] for s in recent) / sum(s['impressions'] for s in recent)
    older_ctr = sum(s['clicks'] for s in older) / sum(s['impressions'] for s in older)
    
    decline = (older_ctr - recent_ctr) / older_ctr
    
    if decline > 0.2:  # 20% decline
        return True, f"CTR declined {decline:.1%}"
    return False, "Performance stable"
```

---

## Audience Optimization

### Lookalike Expansion

```python
def expand_to_lookalikes(high_performing_audiences):
    """
    Create lookalike audiences from converters.
    """
    for audience in high_performing_audiences:
        if audience['conversion_rate'] > 0.05:  # 5%+
            # Create lookalike
            lookalike_data = {
                "name": f"Lookalike - {audience['name']}",
                "list_type": "LOOKALIKE",
                "source_audience_id": audience['id']
            }
            
            create_tailored_audience(lookalike_data)
```

### Negative Audience Refinement

```python
def build_negative_audiences(campaign_stats):
    """
    Exclude low-quality segments.
    """
    negative_segments = []
    
    for segment in campaign_stats['segments']:
        if segment['cpa'] > target_cpa * 2:
            negative_segments.append(segment['id'])
    
    return negative_segments
```

---

## Budget Optimization

### Portfolio Budget Optimization

```python
def optimize_portfolio_budgets(campaigns, total_budget):
    """
    Allocate budget based on marginal ROAS.
    """
    # Calculate efficiency scores
    scores = []
    for camp in campaigns:
        roas = camp['revenue'] / camp['spend']
        scores.append({
            'id': camp['id'],
            'roas': roas,
            'current_budget': camp['budget']
        })
    
    # Sort by ROAS
    scores.sort(key=lambda x: x['roas'], reverse=True)
    
    # Allocate budget
    allocations = {}
    remaining = total_budget
    
    for i, camp in enumerate(scores):
        if i < len(scores) - 1:
            # Top performers get more
            allocation = int(total_budget * 0.3 * (0.5 ** i))
        else:
            # Last campaign gets remainder
            allocation = remaining
        
        allocations[camp['id']] = allocation
        remaining -= allocation
    
    return allocations
```

### Dayparting Optimization

```python
def optimize_dayparting(hourly_stats):
    """
    Identify best hours to advertise.
    """
    hour_performance = {}
    
    for hour in range(24):
        hour_data = [s for s in hourly_stats if s['hour'] == hour]
        
        if hour_data:
            avg_cpa = sum(s['spend'] for s in hour_data) / sum(s['conversions'] for s in hour_data)
            hour_performance[hour] = avg_cpa
    
    # Find best hours (lowest CPA)
    best_hours = sorted(hour_performance.items(), key=lambda x: x[1])[:8]
    
    return [h[0] for h in best_hours]
```

---

## Automated Rules

### Performance-Based Pausing

```python
def auto_pause_rules(line_items, min_spend=100, max_cpa=50):
    """
    Automatically pause poor performers.
    """
    for item in line_items:
        stats = get_line_item_stats(item['id'])
        
        if stats['spend'] > min_spend:
            cpa = stats['spend'] / stats['conversions']
            
            if cpa > max_cpa:
                pause_line_item(item['id'])
                send_alert(f"Paused {item['name']}: CPA ${cpa:.2f}")
```

### Budget Pacing

```python
def check_budget_pacing(campaign, days_remaining):
    """
    Ensure even budget spend.
    """
    total_budget = campaign['total_budget']
    spent = campaign['total_spend']
    
    expected_spend = (total_budget / campaign['total_days']) * (campaign['total_days'] - days_remaining)
    
    if spent > expected_spend * 1.2:
        # Overspending, reduce daily budget
        new_daily = campaign['daily_budget'] * 0.8
        update_campaign_budget(campaign['id'], new_daily)
    elif spent < expected_spend * 0.8:
        # Underspending, increase daily budget
        new_daily = campaign['daily_budget'] * 1.2
        update_campaign_budget(campaign['id'], new_daily)
```

---

## Machine Learning Approaches

### Conversion Prediction

```python
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

def train_conversion_model(historical_data):
    """
    Predict conversion likelihood.
    """
    df = pd.DataFrame(historical_data)
    
    features = ['hour', 'day_of_week', 'device_type', 'age_group', 'gender']
    X = pd.get_dummies(df[features])
    y = df['converted']
    
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X, y)
    
    return model

def predict_conversion_rate(model, user_features):
    X = pd.get_dummies(pd.DataFrame([user_features]))
    return model.predict_proba(X)[0][1]
```

### Bid Recommendation

```python
def ml_bid_recommendation(features, target_position=1):
    """
    Use ML to recommend optimal bid.
    """
    # Features: competition_level, time_of_day, audience_quality, etc.
    # Train model on historical bid → position data
    
    predicted_bid = model.predict([features])[0]
    return int(predicted_bid * 1_000_000)  # Convert to micro
```
