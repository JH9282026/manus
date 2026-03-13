# Apple Search Ads API Reporting Guide

Comprehensive guide to generating, analyzing, and visualizing Apple Search Ads performance reports using the Campaign Management API v5.

---

## Report Types Overview

| Report Type | Granularity | Use Case |
|-------------|-------------|----------|
| **Campaign-Level** | Campaign performance | Overall campaign health, budget pacing |
| **Ad Group-Level** | Ad group performance | Targeting effectiveness, bid strategy |
| **Keyword-Level** | Keyword performance | Keyword optimization, bid management |
| **Search Term-Level** | Search query performance | Keyword discovery, negative keyword mining |

---

## Campaign-Level Reporting

### Basic Campaign Report

```python
from datetime import datetime, timedelta

def get_campaign_performance(
    client,
    campaign_id: int,
    days: int = 30,
    granularity: str = 'DAILY'
) -> dict:
    """
    Get campaign performance report.
    
    Args:
        client: API client
        campaign_id: Campaign ID
        days: Number of days to report
        granularity: HOURLY, DAILY, MONTHLY, or TOTAL
    
    Returns:
        Report data dictionary
    """
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    
    report_data = {
        'startTime': start_date.strftime('%Y-%m-%d'),
        'endTime': end_date.strftime('%Y-%m-%d'),
        'granularity': granularity,
        'selector': {
            'conditions': [{
                'field': 'campaignId',
                'operator': 'EQUALS',
                'values': [str(campaign_id)]
            }]
        },
        'returnRowTotals': True,
        'returnRecordsWithNoMetrics': False
    }
    
    return client._request('POST', 'reports/campaigns', data=report_data)

# Example usage
report = get_campaign_performance(client, campaign_id=123456, days=30, granularity='DAILY')

# Access data
for row in report['data']['reportingDataResponse']['row']:
    print(f"Date: {row['metadata']['date']}")
    print(f"Impressions: {row['total']['impressions']}")
    print(f"Taps: {row['total']['taps']}")
    print(f"Installs: {row['total']['installs']}")
    print(f"Spend: ${row['total']['localSpend']['amount']}")
    print(f"CPA: ${row['total']['avgCPA']['amount']}")
    print()

# Access totals
if 'grandTotals' in report['data']['reportingDataResponse']:
    totals = report['data']['reportingDataResponse']['grandTotals']
    print(f"Total Impressions: {totals['impressions']}")
    print(f"Total Installs: {totals['installs']}")
    print(f"Total Spend: ${totals['localSpend']['amount']}")
```

### Multi-Campaign Comparison

```python
import pandas as pd

def compare_campaigns(
    client,
    campaign_ids: list,
    days: int = 30
) -> pd.DataFrame:
    """
    Compare performance across multiple campaigns.
    
    Returns:
        DataFrame with campaign comparison
    """
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')
    
    comparison_data = []
    
    for campaign_id in campaign_ids:
        report = get_campaign_performance(client, campaign_id, days, 'TOTAL')
        
        if not report['data']['reportingDataResponse']['row']:
            continue
        
        row = report['data']['reportingDataResponse']['row'][0]
        
        comparison_data.append({
            'Campaign ID': campaign_id,
            'Campaign Name': row['metadata']['campaignName'],
            'Impressions': row['total']['impressions'],
            'Taps': row['total']['taps'],
            'Installs': row['total']['installs'],
            'TTR': f"{row['total']['ttr'] * 100:.2f}%",
            'Conv Rate': f"{row['total']['conversionRate'] * 100:.2f}%",
            'Spend': float(row['total']['localSpend']['amount']),
            'CPA': float(row['total']['avgCPA']['amount']),
            'CPT': float(row['total']['avgCPT']['amount'])
        })
    
    df = pd.DataFrame(comparison_data)
    
    # Sort by spend descending
    df = df.sort_values('Spend', ascending=False)
    
    return df

# Example usage
campaign_ids = [123456, 123457, 123458]
comparison = compare_campaigns(client, campaign_ids, days=30)
print(comparison.to_string(index=False))
```

### Campaign Performance by Dimension

```python
def get_campaign_performance_by_country(
    client,
    campaign_id: int,
    days: int = 30
) -> pd.DataFrame:
    """
    Get campaign performance grouped by country.
    """
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')
    
    report_data = {
        'startTime': start_date,
        'endTime': end_date,
        'granularity': 'TOTAL',
        'selector': {
            'conditions': [{
                'field': 'campaignId',
                'operator': 'EQUALS',
                'values': [str(campaign_id)]
            }]
        },
        'groupBy': ['countryOrRegion'],
        'returnRowTotals': True
    }
    
    report = client._request('POST', 'reports/campaigns', data=report_data)
    
    data = []
    for row in report['data']['reportingDataResponse']['row']:
        data.append({
            'Country': row['metadata'].get('countryOrRegion', 'Unknown'),
            'Impressions': row['total']['impressions'],
            'Taps': row['total']['taps'],
            'Installs': row['total']['installs'],
            'Spend': float(row['total']['localSpend']['amount']),
            'CPA': float(row['total']['avgCPA']['amount'])
        })
    
    return pd.DataFrame(data).sort_values('Spend', ascending=False)

# Example usage
country_performance = get_campaign_performance_by_country(client, 123456, days=30)
print(country_performance.to_string(index=False))
```

---

## Keyword-Level Reporting

### Keyword Performance Analysis

```python
def analyze_keyword_performance(
    client,
    campaign_id: int,
    days: int = 30,
    min_impressions: int = 100
) -> pd.DataFrame:
    """
    Analyze keyword performance with filtering.
    
    Args:
        client: API client
        campaign_id: Campaign ID
        days: Number of days to analyze
        min_impressions: Minimum impressions to include
    
    Returns:
        DataFrame with keyword analysis
    """
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetim