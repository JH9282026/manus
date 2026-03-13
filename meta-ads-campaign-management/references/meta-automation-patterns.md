# Meta Ads Automation Patterns

Automation workflows for Meta advertising campaigns.

---

## Automated Rules via API

### Create Rule
```python
url = f"https://graph.facebook.com/v19.0/act_{ad_account_id}/adrules_library"

rule_params = {
    "access_token": access_token,
    "name": "Pause High CPA Ad Sets",
    "evaluation_spec": json.dumps({
        "evaluation_type": "SCHEDULE",
        "filters": [
            {
                "field": "entity_type",
                "operator": "EQUAL",
                "value": "ADSET"
            },
            {
                "field": "cost_per_action_type",
                "operator": "GREATER_THAN",
                "value": 50.00  # $50 CPA
            },
            {
                "field": "impressions",
                "operator": "GREATER_THAN",
                "value": 1000
            }
        ]
    }),
    "execution_spec": json.dumps({
        "execution_type": "PAUSE"
    }),
    "schedule_spec": json.dumps({
        "schedule_type": "DAILY",
        "time": "09:00:00"
    })
}

response = requests.post(url, params=rule_params)
```

### Common Rule Types

**1. Pause Poor Performers**
```python
filters = [
    {"field": "cost_per_action_type", "operator": "GREATER_THAN", "value": target_cpa * 1.5},
    {"field": "spend", "operator": "GREATER_THAN", "value": 100}
]
execution = {"execution_type": "PAUSE"}
```

**2. Increase Budget for Winners**
```python
filters = [
    {"field": "roas", "operator": "GREATER_THAN", "value": 3.0},
    {"field": "spend", "operator": "GREATER_THAN", "value": 500}
]
execution = {
    "execution_type": "CHANGE_BUDGET",
    "execution_options": [{"field": "budget", "operator": "INCREASE_BY", "value": 20}]
}
```

**3. Send Notification**
```python
filters = [
    {"field": "frequency", "operator": "GREATER_THAN", "value": 3.0}
]
execution = {
    "execution_type": "NOTIFICATION",
    "execution_options": [{"field": "notification_mode", "value": "EMAIL"}]
}
```

---

## Custom Automation Scripts

### Budget Optimizer
```python
import requests
from datetime import datetime, timedelta

def optimize_budgets(ad_account_id, access_token):
    # Get all active ad sets
    url = f"https://graph.facebook.com/v19.0/act_{ad_account_id}/adsets"
    params = {
        "access_token": access_token,
        "fields": "id,name,daily_budget,status",
        "filtering": json.dumps([{"field": "adset.effective_status", "operator": "IN", "value": ["ACTIVE"]}])
    }
    
    adsets = requests.get(url, params=params).json()["data"]
    
    # Get insights for each ad set
    for adset in adsets:
        insights_url = f"https://graph.facebook.com/v19.0/{adset['id']}/insights"
        insights_params = {
            "access_token": access_token,
            "fields": "spend,purchase_roas,actions",
            "time_range": json.dumps({
                "since": (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d"),
                "until": datetime.now().strftime("%Y-%m-%d")
            })
        }
        
        insights = requests.get(insights_url, params=insights_params).json()
        
        if insights.get("data"):
            data = insights["data"][0]
            roas = float(data.get("purchase_roas", [{}])[0].get("value", 0))
            
            current_budget = int(adset["daily_budget"])
            
            # Adjust budget based on ROAS
            if roas > 3.0:
                new_budget = int(current_budget * 1.2)  # Increase 20%
            elif roas < 1.5:
                new_budget = int(current_budget * 0.8)  # Decrease 20%
            else:
                continue
            
            # Update budget
            update_url = f"https://graph.facebook.com/v19.0/{adset['id']}"
            requests.post(update_url, params={
                "access_token": access_token,
                "daily_budget": new_budget
            })
```

### Creative Rotation
```python
def rotate_creatives(ad_account_id, access_token, adset_id):
    # Get all ads in ad set
    url = f"https://graph.facebook.com/v19.0/{adset_id}/ads"
    params = {
        "access_token": access_token,
        "fields": "id,name,status"
    }
    
    ads = requests.get(url, params=params).json()["data"]
    
    # Get insights
    for ad in ads:
        insights_url = f"https://graph.facebook.com/v19.0/{ad['id']}/insights"
        insights_params = {
            "access_token": access_token,
            "fields": "impressions,frequency"
        }
        
        insights = requests.get(insights_url, params=insights_params).json()
        
        if insights.get("data"):
            data = insights["data"][0]
            frequency = float(data.get("frequency", 0))
            
            # Pause if frequency > 3 (creative fatigue)
            if frequency > 3.0:
                requests.post(
                    f"https://graph.facebook.com/v19.0/{ad['id']}",
                    params={"access_token": access_token, "status": "PAUSED"}
                )
```

### Bid Optimizer
```python
def optimize_bids(ad_account_id, access_token, target_cpa=25.0):
    # Get ad sets with bid caps
    url = f"https://graph.facebook.com/v19.0/act_{ad_account_id}/adsets"
    params = {
        "access_token": access_token,
        "fields": "id,name,bid_amount,bid_strategy",
        "filtering": json.dumps([{
            "field": "adset.bid_strategy",
            "operator": "EQUAL",
            "value": "LOWEST_COST_WITH_BID_CAP"
        }])
    }
    
    adsets = requests.get(url, params=params).json()["data"]
    
    for adset in adsets:
        # Get CPA
        insights_url = f"https://graph.facebook.com/v19.0/{adset['id']}/insights"
        insights_params = {
            "access_token": access_token,
            "fields": "cost_per_action_type"
        }
        
        insights = requests.get(insights_url, params=insights_params).json()
        
        if insights.get("data"):
            actions = insights["data"][0].get("cost_per_action_type", [])
            purchase_cpa = next((float(a["value"]) for a in actions if a["action_type"] == "purchase"), None)
            
            if purchase_cpa:
                current_bid = int(adset["bid_amount"])
                
                # Adjust bid
                if purchase_cpa > target_cpa * 1.2:
                    new_bid = int(current_bid * 0.9)
                elif purchase_cpa < target_cpa * 0.8:
                    new_bid = int(current_bid * 1.1)
                else:
                    continue
                
                # Update bid
                requests.post(
                    f"https://graph.facebook.com/v19.0/{adset['id']}",
                    params={"access_token": access_token, "bid_amount": new_bid}
                )
```

---

## MCP Integration

Example MCP server for Meta Ads automation:

```python
from mcp import MCPServer, Tool

server = MCPServer("meta-ads")

@server.tool()
def create_campaign(name: str, objective: str, budget: int) -> dict:
    """Create Meta ad campaign."""
    url = f"https://graph.facebook.com/v19.0/act_{AD_ACCOUNT_ID}/campaigns"
    params = {
        "access_token": ACCESS_TOKEN,
        "name": name,
        "objective": objective,
        "daily_budget": budget,
        "status": "PAUSED"
    }
    response = requests.post(url, params=params)
    return response.json()

@server.tool()
def get_campaign_performance(campaign_id: str) -> dict:
    """Get campaign insights."""
    url = f"https://graph.facebook.com/v19.0/{campaign_id}/insights"
    params = {
        "access_token": ACCESS_TOKEN,
        "fields": "impressions,clicks,spend,purchase_roas,actions"
    }
    response = requests.get(url, params=params)
    return response.json()

if __name__ == "__main__":
    server.run()
```
