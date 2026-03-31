# Reddit Ads API Reporting and Analytics Automation

## Reporting Endpoints

### Campaign Performance
**Endpoint:** `GET /api/v3/accounts/{account_id}/campaigns/performance`

**Metrics Available:**
- Impressions
- Clicks
- CTR (Click-through rate)
- Spend
- CPC (Cost per click)
- CPM (Cost per thousand impressions)
- Conversions
- CPA (Cost per acquisition)

### Ad Group Performance
**Endpoint:** `GET /api/v3/campaigns/{campaign_id}/ad_groups/performance`

**Granularity:**
- Hourly
- Daily
- Weekly
- Monthly
- Custom date ranges

### Ad Performance
**Endpoint:** `GET /api/v3/ad_groups/{ad_group_id}/ads/performance`

## Data Extraction Automation

### Automated Reporting
**Daily Performance Report:**
```python
import requests
from datetime import datetime, timedelta

def fetch_daily_performance(account_id, access_token):
    yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    
    url = f'https://ads-api.reddit.com/api/v3/accounts/{account_id}/campaigns/performance'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    params = {
        'start_date': yesterday,
        'end_date': yesterday,
        'metrics': 'impressions,clicks,spend,conversions'
    }
    
    response = requests.get(url, headers=headers, params=params)
    return response.json()
```

### Data Integration
**Export to Data Warehouse:**
- BigQuery
- Snowflake
- Redshift
- Google Sheets

**Visualization Tools:**
- Looker Studio
- Tableau
- Power BI
- Custom dashboards

## Third-Party Platforms

### Fivetran
- Automated data sync
- Pre-built connectors
- Scheduled updates

### Bright Analytics
- Unified marketing dashboard
- Cross-channel attribution
- Automated reporting

### Power My Analytics
- Data connectors
- Custom reports
- Spreadsheet integration

## Conclusion
Automated reporting and analytics enable real-time insights, data-driven decisions, and efficient campaign optimization.
