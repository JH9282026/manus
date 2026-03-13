# Apple Search Ads API Automation Examples

Practical code examples for automating Apple Search Ads campaign management, bid optimization, keyword discovery, and reporting using the Campaign Management API v5.

---

## Setup and Authentication

### Basic API Client

```python
import requests
import json
from typing import Dict, List, Optional

class AppleSearchAdsClient:
    def __init__(self, cert_path: str, key_path: str, org_id: str):
        self.base_url = 'https://api.searchads.apple.com/api/v5'
        self.cert = (cert_path, key_path)
        self.headers = {
            'Authorization': f'orgId={org_id}',
            'Content-Type': 'application/json'
        }
    
    def _request(self, method: str, endpoint: str, data: Optional[Dict] = None) -> Dict:
        url = f'{self.base_url}/{endpoint}'
        
        if method == 'GET':
            response = requests.get(url, cert=self.cert, headers=self.headers)
        elif method == 'POST':
            response = requests.post(url, cert=self.cert, headers=self.headers, json=data)
        elif method == 'PUT':
            response = requests.put(url, cert=self.cert, headers=self.headers, json=data)
        elif method == 'DELETE':
            response = requests.delete(url, cert=self.cert, headers=self.headers)
        
        response.raise_for_status()
        return response.json()
    
    def get_campaigns(self) -> List[Dict]:
        return self._request('GET', 'campaigns')['data']
    
    def create_campaign(self, campaign_data: Dict) -> Dict:
        return self._request('POST', 'campaigns', campaign_data)['data']
    
    def get_campaign_report(self, campaign_id: int, start_date: str, end_date: str) -> Dict:
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
            }
        }
        return self._request('POST', 'reports/campaigns', report_data)

# Initialize client
client = AppleSearchAdsClient(
    cert_path='/path/to/certificate.pem',
    key_path='/path/to/private.key',
    org_id='1234567'
)
```

---

## Campaign Management Automation

### Create Complete Campaign Structure

```python
def create_complete_campaign(
    client: AppleSearchAdsClient,
    app_id: int,
    campaign_name: str,
    daily_budget: float,
    countries: List[str],
    ad_groups_config: List[Dict]
) -> Dict:
    """
    Creates a complete campaign with multiple ad groups and keywords.
    
    Args:
        client: API client instance
        app_id: App Store app ID
        campaign_name: Name for the campaign
        daily_budget: Daily budget amount
        countries: List of country codes
        ad_groups_config: List of ad group configurations
    
    Returns:
        Dictionary with campaign and ad group IDs
    """
    # Create campaign
    campaign_data = {
        'name': campaign_name,
        'dailyBudgetAmount': {'amount': str(daily_budget), 'currency': 'USD'},
        'adamId': app_id,
        'countriesOrRegions': countries,
        'supplySources': ['APPSTORE_SEARCH_RESULTS'],
        'status': 'ENABLED'
    }
    
    campaign = client.create_campaign(campaign_data)
    campaign_id = campaign['id']
    print(f'Created campaign: {campaign_id}')
    
    # Create ad groups
    ad_group_ids = []
    for ag_config in ad_groups_config:
        ad_group_data = {
            'name': ag_config['name'],
            'defaultBidAmount': {'amount': str(ag_config['default_bid']), 'currency': 'USD'},
            'cpaGoal': {'amount': str(ag_config['cpa_goal']), 'currency': 'USD'},
            'status': 'ENABLED',
            'automatedKeywordsOptIn': ag_config.get('search_match', False)
        }
        
        ad_group = client._request(
            'POST',
            f'campaigns/{campaign_id}/adgroups',
            ad_group_data
        )['data']
        ad_group_id = ad_group['id']
        ad_group_ids.append(ad_group_id)
        print(f'Created ad group: {ad_group_id}')
        
        # Add keywords if provided
        if 'keywords' in ag_config:
            keywords_data = [
                {
                    'text': kw['text'],
                    'matchType': kw['match_type'],
                    'bidAmount': {'amount': str(kw.get('bid', ag_config['default_bid'])), 'currency': 'USD'},
                    'status': 'ACTIVE'
                }
                for kw in ag_config['keywords']
            ]
            
            client._request(
                'POST',
                f'campaigns/{campaign_id}/adgroups/{ad_group_id}/targetingkeywords/bulk',
                keywords_data
            )
            print(f'Added {len(keywords_data)} keywords to ad group {ad_group_id}')
    
    return {
        'campaign_id': campaign_id,
        'ad_group_ids': ad_group_ids
    }

# Example usage
config = [
    {
        'name': 'Brand - Exact Match',
        'default_bid': 2.0,
        'cpa_goal': 5.0,
        'keywords': [
            {'text': 'my fitness app', 'match_type': 'EXACT'},
            {'text': 'myfitnessapp', 'match_type': 'EXACT'}
        ]
    },
    {
        'name': 'Category - Broad Match',
        'default_bid': 1.5,
        'cpa_goal': 8.0,
        'search_match': True,
        'keywords': [
            {'text': 'fitness app', 'match_type': 'BROAD'},
            {'text': 'workout tracker', 'match_type': 'BROAD'}
        ]
    }
]

result = create_complete_campaign(
    client=client,
    app_id=123456789,
    campaign_name='Fitness App - US - Q1 2026',
    daily_budget=100.0,
    countries=['US'],
    ad_groups_config=config
)
```

### Bulk Campaign Status Management

```python
def pause_all_campaigns(client: AppleSearchAdsClient) -> int:
    """Pauses all active campaigns."""
    campaigns = client.get_campaigns()
    paused_count = 0
    
    for campaign in campaigns:
        if campaign['status'] == 'ENABLED':
            client._request(
                'PUT',
                f'campaigns/{campaign["id"]}',
                {'campaign': {'status': 'PAUSED'}}
            )
            paused_count += 1
            print(f'Paused campaign: {campaign["name"]}')
    
    return paused_count

def enable_campaigns_by_name_pattern(client: AppleSearchAdsClient, pattern: str) -> int:
    """Enables campaigns matching a name pattern."""
    campaigns = client.get_campaigns()
    enabled_count = 0
    
    for campaign in campaigns:
        if pattern.lower() in campaign['name'].lower() and campaign['status'] == 'PAUSED':
            client._request(
                'PUT',
                f'campaigns/{campaign["id"]}',
                {'campaign': {'status': 'ENABLED'}}
            )
            enabled_count += 1
            print(f'Enabled campaign: {campaign["name"]}')
    
    return enabled_count

# Example: Pause all campaigns for maintenance
paused = pause_all_campaigns(client)
print(f'Paused {paused} campaigns')

# Example: Enable only brand campaigns
enabled = enable_campaigns_by_name_pattern(client, 'brand')
print(f'Enabled {enabled} brand campaigns')
```

---

## Automated Bid Management

### Performance-Based Bid Optimization

```python
from datetime import datetime, timedelta

def optimize_keyword_bids(
    client: AppleSearchAdsClient,
    campaign_id: int,
    target_cpa: float,
    min_conversions: int = 5,
    bid_adjustment_factor: float = 0.2
) -> Dict:
    """
    Adjusts keyword bids based on performance vs target CPA.
    
    Args:
        client: API client
        campaign_id: Campaign ID
        target_cpa: Target cost per acquisition
        min_conversions: Minimum conversions required for adjustment
        bid_adjustment_factor: Percentage to adjust bids (0.2 = 20%)
    
    Returns:
        Summary of bid adjustments
    """
    # Get keyword performance for last 7 days
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
    
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
        'returnRowTotals': False
    }
    
    report = client._request('POST', f'reports/campaigns/{campaign_id}/keywords', report_data)
    
    adjustments = {
        'increased': [],
        'decreased': [],
        'unchanged': []
    }
    
    for row in report['data']['reportingDataResponse']['row']:
        keyword_id = row['metadata']['keywordId']
        keyword_text = row['metadata']['keyword']
        installs = row['total'].get('installs', 0)
        
        # Skip if insufficient data
        if installs < min_conversions:
            adjustments['unchanged'].append(keyword_text)
            continue
        
        current_cpa = float(row['total']['avgCPA']['amount'])
        current_bid = float(row['metadata'].get('bidAmount', {}).get('amount', 0))
        
        # Calculate new bid
        if current_cpa < target_cpa * 0.8:  # Performing well (20% below target)
            new_bid = current_bid * (1 + bid_adjustment_factor)  # Increase bid
            action = 'increased'
        elif current_cpa > target_cpa * 1.2:  # Underperforming (20% above target)
            new_bid = current_bid * (1 - bid_adjustment_factor)  # Decrease bid
            action = 'decreased'
        else:
            adjustments['unchanged'].append(keyword_text)
            continue
        
        # Update keyword bid
        ad_group_id = row['metadata']['adGroupId']
        update_data = [{
            'id': keyword_id,
            'bidAmount': {'amount': f'{new_bid:.2f}', 'currency': 'USD'}
        }]
        
        client._request(
            'PUT',
            f'campaigns/{campaign_id}/adgroups/{ad_group_id}/targetingkeywords/bulk',
            update_data
        )
        
        adjustments[action].append({
            'keyword': keyword_text,
            'old_bid': current_bid,
            'new_bid': new_bid,
            'cpa': current_cpa
        })
        
        print(f'{action.capitalize()} bid for "{keyword_text}": ${current_bid:.2f} -> ${new_bid:.2f} (CPA: ${current_cpa:.2f})')
    
    return adjustments

# Example usage
adjustments = optimize_keyword_bids(
    client=client,
    campaign_id=123456,
    target_cpa=5.0,
    min_conversions=5,
    bid_adjustment_factor=0.2
)

print(f"\nSummary:")
print(f"Increased: {len(adjustments['increased'])} keywords")
print(f"Decreased: {len(adjustments['decreased'])} keywords")
print(f"Unchanged: {len(adjustments['unchanged'])} keywords")
```

### Automated Budget Reallocation

```python
def reallocate_budget_by_roas(
    client: AppleSearchAdsClient,
    total_daily_budget: float,
    min_budget_per_campaign: float = 10.0
) -> Dict:
    """
    Reallocates budget across campaigns based on ROAS.
    
    Args:
        client: API client
        total_daily_budget: Total daily budget to allocate
        min_budget_per_campaign: Minimum budget per campaign
    
    Returns:
        Budget allocation summary
    """
    # Get all campaigns
    campaigns = client.get_campaigns()
    
    # Get performance for each campaign (last 30 days)
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
    
    campaign_performance = []
    
    for campaign in campaigns:
        if campaign['status'] != 'ENABLED':
            continue
        
        report = client.get_campaign_report(campaign['id'], start_date, end_date)
        
        if not report['data']['reportingDataResponse']['row']:
            continue
        
        row = report['data']['reportingDataResponse']['row'][0]
        spend = float(row['total']['localSpend']['amount'])
        installs = row['total'].get('installs', 0)
        
        # Calculate ROAS (assuming $10 LTV per install for example)
        ltv_per_install = 10.0
        revenue = installs * ltv_per_install
        roas = revenue / spend if spend > 0 else 0
        
        campaign_performance.append({
            'id': campaign['id'],
            'name': campaign['name'],
            'roas': roas,
            'spend': spend,
            'installs': installs
        })
    
    # Calculate budget allocation based on ROAS
    total_roas = sum(c['roas'] for c in campaign_performance)
    
    if total_roas == 0:
        print('No ROAS data available for budget allocation')
        return {}
    
    allocations = []
    
    for campaign in campaign_performance:
        # Allocate budget proportionally to ROAS
        allocated_budget = (campaign['roas'] / total_roas) * total_daily_budget
        
        # Ensure minimum budget
        allocated_budget = max(allocated_budget, min_budget_per_campaign)
        
        # Update campaign budget
        client._request(
            'PUT',
            f'campaigns/{campaign["id"]}',
            {
                'campaign': {
                    'dailyBudgetAmount': {'amount': f'{allocated_budget:.2f}', 'currency': 'USD'}
                }
            }
        )
        
        allocations.append({
            'campaign': campaign['name'],
            'roas': campaign['roas'],
            'new_budget': allocated_budget
        })
        
        print(f'{campaign["name"]}: ${allocated_budget:.2f} (ROAS: {campaign["roas"]:.2f}x)')
    
    return allocations

# Example usage
allocations = reallocate_budget_by_roas(
    client=client,
    total_daily_budget=500.0,
    min_budget_per_campaign=10.0
)
```

---

## Keyword Discovery Automation

### Search Terms Mining

```python
def mine_search_terms(
    client: AppleSearchAdsClient,
    campaign_id: int,
    days: int = 7,
    min_installs_for_exact: int = 5,
    max_cpa_for_exact: float = 10.0,
    min_spend_for_negative: float = 50.0
) -> Dict:
    """
    Mines search terms report to identify new keywords and negatives.
    
    Args:
        client: API client
        campaign_id: Campaign ID
        days: Number of days to analyze
        min_installs_for_exact: Minimum installs to add as exact match
        max_cpa_for_exact: Maximum CPA to add as exact match
        min_spend_for_negative: Minimum spend with zero installs for negative
    
    Returns:
        Dictionary with new keywords and negatives
    """
    # Get search terms report
    end_time = datetime.now()
    start_time = end_time - timedelta(days=days)
    
    report_data = {
        'startTime': start_time.strftime('%Y-%m-%dT%H:%M:%S.000'),
        'endTime': end_time.strftime('%Y-%m-%dT%H:%M:%S.999'),
        'timeZone': 'America/New_York',
        'granularity': 'TOTAL',
        'selector': {
            'pagination': {'offset': 0, 'limit': 1000}
        },
        'returnRowTotals': False
    }
    
    report = client._request(
        'POST',
        f'reports/campaigns/{campaign_id}/searchterms',
        report_data
    )
    
    new_exact_keywords = []
    new_broad_keywords = []
    new_negatives = []
    
    for row in report['data']['reportingDataResponse']['row']:
        search_term = row['metadata']['searchTermText']
        installs = row['total'].get('installs', 0)
        spend = float(row['total']['localSpend']['amount'])
        cpa = float(row['total']['avgCPA']['amount']) if installs > 0 else 0
        
        # High performers -> add as exact match
        if installs >= min_installs_for_exact and cpa <= max_cpa_for_exact:
            new_exact_keywords.append({
                'text': search_term,
                'matchType': 'EXACT',
                'bidAmount': {'amount': f'{cpa * 1.2:.2f}', 'currency': 'USD'},
                'status': 'ACTIVE',
                'performance': {'installs': installs, 'cpa': cpa}
            })
        
        # Medium performers -> add as broad match
        elif installs >= 2 and cpa <= max_cpa_for_exact * 1.5:
            new_broad_keywords.append({
                'text': search_term,
                'matchType': 'BROAD',
                'bidAmount': {'amount': f'{cpa:.2f}', 'currency': 'USD'},
                'status': 'ACTIVE',
                'performance': {'installs': installs, 'cpa': cpa}
            })
        
        # Non-converters with spend -> add as negative
        elif installs == 0 and spend >= min_spend_for_negative:
            new_negatives.append({
                'text': search_term,
                'matchType': 'EXACT',
                'status': 'ACTIVE',
                'wasted_spend': spend
            })
    
    return {
        'exact_keywords': new_exact_keywords,
        'broad_keywords': new_broad_keywords,
        'negative_keywords': new_negatives
    }

# Example usage
mined_data = mine_search_terms(
    client=client,
    campaign_id=123456,
    days=7,
    min_installs_for_exact=5,
    max_cpa_for_exact=10.0,
    min_spend_for_negative=50.0
)

print(f"Found {len(mined_data['exact_keywords'])} new exact match keywords")
print(f"Found {len(mined_data['broad_keywords'])} new broad match keywords")
print(f"Found {len(mined_data['negative_keywords'])} new negative keywords")

# Add keywords to appropriate ad groups
for keyword in mined_data['exact_keywords']:
    print(f"Exact: {keyword['text']} (CPA: ${keyword['performance']['cpa']:.2f}, Installs: {keyword['performance']['installs']})")
```

### Automated Negative Keyword Addition

```python
def auto_add_negative_keywords(
    client: AppleSearchAdsClient,
    campaign_id: int,
    negative_keywords: List[Dict],
    level: str = 'campaign'
) -> int:
    """
    Automatically adds negative keywords at campaign or ad group level.
    
    Args:
        client: API client
        campaign_id: Campaign ID
        negative_keywords: List of negative keyword dictionaries
        level: 'campaign' or 'adgroup'
    
    Returns:
        Number of negative keywords added
    """
    if level == 'campaign':
        endpoint = f'campaigns/{campaign_id}/negativekeywords/bulk'
    else:
        # For ad group level, you'd need to specify ad_group_id
        raise NotImplementedError('Ad group level not implemented in this example')
    
    # Remove performance data before sending to API
    clean_negatives = [
        {
            'text': nk['text'],
            'matchType': nk['matchType'],
            'status': nk['status']
        }
        for nk in negative_keywords
    ]
    
    if not clean_negatives:
        return 0
    
    result = client._request('POST', endpoint, clean_negatives)
    added_count = len(result.get('data', []))
    
    print(f'Added {added_count} negative keywords to campaign {campaign_id}')
    for nk in negative_keywords:
        print(f'  - "{nk["text"]}" (wasted ${nk.get("wasted_spend", 0):.2f})')
    
    return added_count

# Example: Add negatives from mined data
if mined_data['negative_keywords']:
    auto_add_negative_keywords(
        client=client,
        campaign_id=123456,
        negative_keywords=mined_data['negative_keywords'],
        level='campaign'
    )
```

---

## Reporting Automation

### Daily Performance Email Report

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd

def generate_daily_report(client: AppleSearchAdsClient) -> str:
    """
    Generates daily performance report for all campaigns.
    
    Returns:
        HTML report string
    """
    yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    
    campaigns = client.get_campaigns()
    
    report_data = []
    
    for campaign in campaigns:
        if campaign['status'] != 'ENABLED':
            continue
        
        report = client.get_campaign_report(campaign['id'], yesterday, yesterday)
        
        if not report['data']['reportingDataResponse']['row']:
            continue
        
        row = report['data']['reportingDataResponse']['row'][0]
        
        report_data.append({
            'Campaign': campaign['name'],
            'Impressions': row['total'].get('impressions', 0),
            'Taps': row['total'].get('taps', 0),
            'Installs': row['total'].get('installs', 0),
            'TTR': f"{row['total'].get('ttr', 0) * 100:.2f}%",
            'Conv Rate': f"{row['total'].get('conversionRate', 0) * 100:.2f}%",
            'Spend': f"${row['total']['localSpend']['amount']}",
            'CPA': f"${row['total']['avgCPA']['amount']}"
        })
    
    # Create DataFrame
    df = pd.DataFrame(report_data)
    
    # Generate HTML
    html = f"""
    <html>
    <head>
        <style>
            table {{ border-collapse: collapse; width: 100%; }}
            th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
            th {{ background-color: #4CAF50; color: white; }}
            tr:nth-child(even) {{ background-color: #f2f2f2; }}
        </style>
    </head>
    <body>
        <h2>Apple Search Ads Daily Report - {yesterday}</h2>
        {df.to_html(index=False)}
        <p><strong>Total Spend:</strong> ${df['Spend'].str.replace('$', '').astype(float).sum():.2f}</p>
        <p><strong>Total Installs:</strong> {df['Installs'].sum()}</p>
    </body>
    </html>
    """
    
    return html

def send_email_report(html_content: str, recipients: List[str]):
    """
    Sends HTML email report.
    
    Args:
        html_content: HTML report content
        recipients: List of email addresses
    """
    sender = 'reports@example.com'
    subject = f'Apple Search Ads Daily Report - {datetime.now().strftime("%Y-%m-%d")}'
    
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    
    html_part = MIMEText(html_content, 'html')
    msg.attach(html_part)
    
    # Send email (configure SMTP settings)
    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login('username', 'password')
        server.send_message(msg)
    
    print(f'Report sent to {len(recipients)} recipients')

# Example usage
html_report = generate_daily_report(client)
send_email_report(html_report, ['manager@example.com', 'team@example.com'])
```

### Scheduled Automation with APScheduler

```python
from apscheduler.schedulers.blocking import BlockingScheduler
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def daily_optimization_job():
    """Runs daily optimization tasks."""
    logger.info('Starting daily optimization job')
    
    try:
        # 1. Optimize bids for all campaigns
        campaigns = client.get_campaigns()
        for campaign in campaigns:
            if campaign['status'] == 'ENABLED':
                optimize_keyword_bids(
                    client=client,
                    campaign_id=campaign['id'],
                    target_cpa=5.0
                )
        
        # 2. Mine search terms and add keywords/negatives
        for campaign in campaigns:
            if campaign['status'] == 'ENABLED':
                mined = mine_search_terms(client, campaign['id'])
                if mined['negative_keywords']:
                    auto_add_negative_keywords(
                        client,
                        campaign['id'],
                        mined['negative_keywords']
                    )
        
        # 3. Send daily report
        html_report = generate_daily_report(client)
        send_email_report(html_report, ['manager@example.com'])
        
        logger.info('Daily optimization job completed successfully')
    
    except Exception as e:
        logger.error(f'Daily optimization job failed: {e}')

def weekly_budget_reallocation_job():
    """Runs weekly budget reallocation."""
    logger.info('Starting weekly budget reallocation')
    
    try:
        reallocate_budget_by_roas(
            client=client,
            total_daily_budget=500.0
        )
        logger.info('Weekly budget reallocation completed')
    
    except Exception as e:
        logger.error(f'Budget reallocation failed: {e}')

# Set up scheduler
scheduler = BlockingScheduler()

# Daily optimization at 9 AM
scheduler.add_job(daily_optimization_job, 'cron', hour=9, minute=0)

# Weekly budget reallocation on Mondays at 10 AM
scheduler.add_job(weekly_budget_reallocation_job, 'cron', day_of_week='mon', hour=10, minute=0)

logger.info('Scheduler started')
scheduler.start()
```

---

## Advanced Automation

### Multi-Campaign Performance Monitoring

```python
import time

def monitor_campaigns_realtime(
    client: AppleSearchAdsClient,
    alert_threshold_cpa: float = 15.0,
    check_interval_minutes: int = 60
):
    """
    Monitors campaigns in real-time and sends alerts for issues.
    
    Args:
        client: API client
        alert_threshold_cpa: CPA threshold for alerts
        check_interval_minutes: How often to check (in minutes)
    """
    while True:
        logger.info('Checking campaign performance...')
        
        today = datetime.now().strftime('%Y-%m-%d')
        campaigns = client.get_campaigns()
        
        alerts = []
        
        for campaign in campaigns:
            if campaign['status'] != 'ENABLED':
                continue
            
            report = client.get_campaign_report(campaign['id'], today, today)
            
            if not report['data']['reportingDataResponse']['row']:
                continue
            
            row = report['data']['reportingDataResponse']['row'][0]
            installs = row['total'].get('installs', 0)
            
            if installs == 0:
                continue
            
            cpa = float(row['total']['avgCPA']['amount'])
            
            # Alert if CPA exceeds threshold
            if cpa > alert_threshold_cpa:
                alerts.append({
                    'campaign': campaign['name'],
                    'cpa': cpa,
                    'threshold': alert_threshold_cpa,
                    'spend': row['total']['localSpend']['amount']
                })
        
        # Send alerts if any
        if alerts:
            alert_message = 'CPA ALERTS:\n\n'
            for alert in alerts:
                alert_message += f"Campaign: {alert['campaign']}\n"
                alert_message += f"CPA: ${alert['cpa']:.2f} (Threshold: ${alert['threshold']:.2f})\n"
                alert_message += f"Spend: ${alert['spend']}\n\n"
            
            logger.warning(alert_message)
            # Send email/SMS alert here
        
        # Wait before next check
        time.sleep(check_interval_minutes * 60)

# Run monitoring (in background thread or separate process)
# monitor_campaigns_realtime(client, alert_threshold_cpa=15.0, check_interval_minutes=60)
```

These automation examples provide a foundation for building sophisticated Apple Search Ads management systems. Combine and customize them based on your specific needs and scale.