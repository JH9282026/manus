# Python SDK Guide for Apple Search Ads API

Guide to using community-developed Python libraries and SDKs for Apple Search Ads Campaign Management API, including installation, setup, and common usage patterns.

---

## Community Python Libraries

### phiture/searchads_api

**GitHub:** https://github.com/phiture/searchads_api

**Description:** Non-official Python library for Apple Search Ads API developed by Phiture. Provides high-level methods for campaign, ad group, keyword, and creative set management, as well as reporting.

**Status:** Community-maintained, supports API v3/v4 (may need updates for API v5)

#### Installation

```bash
pip install searchads-api
```

#### Basic Setup

```python
from searchads_api import SearchAdsAPI

# Initialize API client
api = SearchAdsAPI(
    org_id='YOUR_ORG_ID',
    cert_path='/path/to/certificate.pem',
    key_path='/path/to/private.key'
)
```

#### Campaign Management

```python
# Get all campaigns
campaigns = api.get_campaigns()

for campaign in campaigns:
    print(f"Campaign: {campaign['name']} (ID: {campaign['id']})")

# Get specific campaign
campaign = api.get_campaign(campaign_id=123456)

# Create campaign
new_campaign = api.create_campaign(
    name='New Campaign',
    budget_amount=1000.0,
    daily_budget_amount=50.0,
    adam_id=123456789,
    countries=['US']
)

# Update campaign
api.update_campaign(
    campaign_id=123456,
    daily_budget_amount=75.0,
    status='ENABLED'
)

# Delete campaign
api.delete_campaign(campaign_id=123456)
```

#### Ad Group Management

```python
# Get ad groups for campaign
ad_groups = api.get_ad_groups(campaign_id=123456)

# Create ad group
new_ad_group = api.create_ad_group(
    campaign_id=123456,
    name='Brand - Exact Match',
    default_bid_amount=2.0,
    cpa_goal=5.0
)

# Update ad group
api.update_ad_group(
    campaign_id=123456,
    ad_group_id=234567,
    default_bid_amount=2.5
)
```

#### Keyword Management

```python
# Get keywords for ad group
keywords = api.get_keywords(
    campaign_id=123456,
    ad_group_id=234567
)

# Create keywords
api.create_keywords(
    campaign_id=123456,
    ad_group_id=234567,
    keywords=[
        {'text': 'fitness app', 'match_type': 'EXACT', 'bid_amount': 2.5},
        {'text': 'workout tracker', 'match_type': 'BROAD', 'bid_amount': 1.5}
    ]
)

# Update keyword bid
api.update_keyword(
    campaign_id=123456,
    ad_group_id=234567,
    keyword_id=345678,
    bid_amount=3.0
)

# Delete keyword
api.delete_keyword(
    campaign_id=123456,
    ad_group_id=234567,
    keyword_id=345678
)
```

#### Negative Keywords

```python
# Get campaign negative keywords
negatives = api.get_campaign_negative_keywords(campaign_id=123456)

# Create campaign negative keywords
api.create_campaign_negative_keywords(
    campaign_id=123456,
    keywords=[
        {'text': 'free', 'match_type': 'EXACT'},
        {'text': 'android', 'match_type': 'BROAD'}
    ]
)

# Get ad group negative keywords
ad_group_negatives = api.get_ad_group_negative_keywords(
    campaign_id=123456,
    ad_group_id=234567
)

# Create ad group negative keywords
api.create_ad_group_negative_keywords(
    campaign_id=123456,
    ad_group_id=234567,
    keywords=[{'text': 'cheap', 'match_type': 'EXACT'}]
)
```

#### Reporting

```python
from datetime import datetime, timedelta

# Get campaign report
end_date = datetime.now()
start_date = end_date - timedelta(days=7)

campaign_report = api.get_campaign_report(
    campaign_id=123456,
    start_date=start_date.strftime('%Y-%m-%d'),
    end_date=end_date.strftime('%Y-%m-%d'),
    granularity='DAILY'
)

for row in campaign_report['rows']:
    print(f"Date: {row['date']}")
    print(f"Impressions: {row['impressions']}")
    print(f"Taps: {row['taps']}")
    print(f"Installs: {row['installs']}")
    print(f"Spend: ${row['spend']}")
    print(f"CPA: ${row['cpa']}")
    print()

# Get keyword report
keyword_report = api.get_keyword_report(
    campaign_id=123456,
    start_date=start_date.strftime('%Y-%m-%d'),
    end_date=end_date.strftime('%Y-%m-%d')
)

# Get search terms report
search_terms_report = api.get_search_terms_report(
    campaign_id=123456,
    start_date=start_date.strftime('%Y-%m-%d'),
    end_date=end_date.strftime('%Y-%m-%d')
)
```

---

## Building a Custom Python SDK

If community libraries don't meet your needs or aren't updated for API v5, build a custom SDK:

### Base Client Class

```python
import requests
import json
import time
from typing import Dict, List, Optional, Any
import logging

logger = logging.getLogger(__name__)

class AppleSearchAdsClient:
    """Apple Search Ads Campaign Management API v5 Client."""
    
    def __init__(
        self,
        org_id: str,
        cert_path: str,
        key_path: str,
        api_version: str = 'v5'
    ):
        self.org_id = org_id
        self.cert = (cert_path, key_path)
        self.base_url = f'https://api.searchads.apple.com/api/{api_version}'
        self.headers = {
            'Authorization': f'orgId={org_id}',
            'Content-Type': 'application/json'
        }
    
    def _request(
        self,
        method: str,
        endpoint: str,
        data: Optional[Dict] = None,
        params: Optional[Dict] = None,
        max_retries: int = 3
    ) -> Dict[str, Any]:
        """Make API request with retry logic."""
        url = f'{self.base_url}/{endpoint}'
        
        for attempt in range(max_retries):
            try:
                if method == 'GET':
                    response = requests.get(
                        url,
                        cert=self.cert,
                        headers=self.headers,
                        params=params
                    )
                elif method == 'POST':
                    response = requests.post(
                        url,
                        cert=self.cert,
                        headers=self.headers,
                        json=data
                    )
                elif method == 'PUT':
                    response = requests.put(
                        url,
                        cert=self.cert,
                        headers=self.headers,
                        json=data
                    )
                elif method == 'DELETE':
                    response = requests.delete(
                        url,
                        cert=self.cert,
                        headers=self.headers
                    )
                
                # Handle rate limiting
                if response.status_code == 429:
                    wait_time = 2 ** attempt
                    logger.warning(f'Rate limited. Waiting {wait_time}s before retry...')
                    time.sleep(wait_time)
                    continue
                
                response.raise_for_status()
                return response.json()
            
            except requests.exceptions.HTTPError as e:
                if attempt == max_retries - 1:
                    logger.error(f'API request failed: {e}')
                    logger.error(f'Response: {e.response.text}')
                    raise
                time.sleep(2 ** attempt)
            
            except Exception as e:
                logger.error(f'Unexpected error: {e}')
                raise
        
        raise Exception('Max retries exceeded')
    
    def _paginate(
        self,
        method: str,
        endpoint: str,
        data: Optional[Dict] = None,
        limit: int = 1000
    ) -> List[Dict]:
        """Handle pagination for list endpoints."""
        all_results = []
        offset = 0
        
        while True:
            if data:
                data['selector'] = data.get('selector', {})
                data['selector']['pagination'] = {'offset': offset, 'limit': limit}
                response = self._request(method, endpoint, data=data)
            else:
                params = {'offset': offset, 'limit': limit}
                response = self._request(method, endpoint, params=params)
            
            results = response.get('data', [])
            all_results.extend(results)
            
            pagination = response.get('pagination', {})
            total_results = pagination.get('totalResults', 0)
            
            if offset + limit >= total_results:
                break
            
            offset += limit
        
        return all_results
```

### Campaign Methods

```python
class CampaignMixin:
    """Campaign management methods."""
    
    def get_campaigns(self, status: Optional[str] = None) -> List[Dict]:
        """Get all campaigns, optionally filtered by status."""
        data = None
        if status:
            data = {
                'conditions': [{
                    'field': 'status',
                    'operator': 'EQUALS',
                    'values': [status]
                }]
            }
        return self._paginate('GET', 'campaigns', data=data)
    
    def get_campaign(self, campaign_id: int) -> Dict:
        """Get specific campaign by ID."""
        return self._request('GET', f'campaigns/{campaign_id}')['data']
    
    def create_campaign(
        self,
        name: str,
        daily_budget: float,
        adam_id: int,
        countries: List[str],
        supply_sources: Optional[List[str]] = None,
        total_budget: Optional[float] = None,
        status: str = 'PAUSED'
    ) -> Dict:
        """Create a new campaign."""
        data = {
            'name': name,
            'dailyBudgetAmount': {'amount': str(daily_budget), 'currency': 'USD'},
            'adamId': adam_id,
            'countriesOrRegions': countries,
            'status': status
        }
        
        if total_budget:
            data['budgetAmount'] = {'amount': str(total_budget), 'currency': 'USD'}
        
        if supply_sources:
            data['supplySources'] = supply_sources
        
        return self._request('POST', 'campaigns', data=data)['data']
    
    def update_campaign(
        self,
        campaign_id: int,
        **kwargs
    ) -> Dict:
        """Update campaign fields."""
        update_data = {'campaign': {}}
        
        if 'daily_budget' in kwargs:
            update_data['campaign']['dailyBudgetAmount'] = {
                'amount': str(kwargs['daily_budget']),
                'currency': 'USD'
            }
        
        if 'status' in kwargs:
            update_data['campaign']['status'] = kwargs['status']
        
        if 'name' in kwargs:
            update_data['campaign']['name'] = kwargs['name']
        
        return self._request('PUT', f'campaigns/{campaign_id}', data=update_data)['data']
    
    def delete_campaign(self, campaign_id: int) -> None:
        """Delete a campaign."""
        self._request('DELETE', f'campaigns/{campaign_id}')
```

### Ad Group Methods

```python
class AdGroupMixin:
    """Ad group management methods."""
    
    def get_ad_groups(self, campaign_id: int) -> List[Dict]:
        """Get all ad groups for a campaign."""
        return self._paginate('GET', f'campaigns/{campaign_id}/adgroups')
    
    def get_ad_group(self, campaign_id: int, ad_group_id: int) -> Dict:
        """Get specific ad group."""
        return self._request('GET', f'campaigns/{campaign_id}/adgroups/{ad_group_id}')['data']
    
    def create_ad_group(
        self,
        campaign_id: int,
        name: str,
        default_bid: float,
        cpa_goal: Optional[float] = None,
        search_match: bool = False,
        status: str = 'ENABLED'
    ) -> Dict:
        """Create a new ad group."""
        data = {
            'name': name,
            'defaultBidAmount': {'amount': str(default_bid), 'currency': 'USD'},
            'status': status,
            'automatedKeywordsOptIn': search_match
        }
        
        if cpa_goal:
            data['cpaGoal'] = {'amount': str(cpa_goal), 'currency': 'USD'}
        
        return self._request('POST', f'campaigns/{campaign_id}/adgroups', data=data)['data']
    
    def update_ad_group(
        self,
        campaign_id: int,
        ad_group_id: int,
        **kwargs
    ) -> Dict:
        """Update ad group fields."""
        update_data = {'adGroup': {}}
        
        if 'default_bid' in kwargs:
            update_data['adGroup']['defaultBidAmount'] = {
                'amount': str(kwargs['default_bid']),
                'currency': 'USD'
            }
        
        if 'cpa_goal' in kwargs:
            update_data['adGroup']['cpaGoal'] = {
                'amount': str(kwargs['cpa_goal']),
                'currency': 'USD'
            }
        
        if 'status' in kwargs:
            update_data['adGroup']['status'] = kwargs['status']
        
        return self._request(
            'PUT',
            f'campaigns/{campaign_id}/adgroups/{ad_group_id}',
            data=update_data
        )['data']
```

### Keyword Methods

```python
class KeywordMixin:
    """Keyword management methods."""
    
    def get_keywords(self, campaign_id: int, ad_group_id: int) -> List[Dict]:
        """Get all keywords for an ad group."""
        return self._paginate(
            'GET',
            f'campaigns/{campaign_id}/adgroups/{ad_group_id}/targetingkeywords'
        )
    
    def create_keywords(
        self,
        campaign_id: int,
        ad_group_id: int,
        keywords: List[Dict]
    ) -> List[Dict]:
        """Create multiple keywords.
        
        Args:
            keywords: List of dicts with 'text', 'match_type', and optional 'bid'
        """
        keyword_data = [
            {
                'text': kw['text'],
                'matchType': kw['match_type'],
                'bidAmount': {'amount': str(kw.get('bid', 0)), 'currency': 'USD'} if 'bid' in kw else None,
                'status': 'ACTIVE'
            }
            for kw in keywords
        ]
        
        # Remove None bidAmount
        for kw in keyword_data:
            if kw['bidAmount'] is None:
                del kw['bidAmount']
        
        return self._request(
            'POST',
            f'campaigns/{campaign_id}/adgroups/{ad_group_id}/targetingkeywords/bulk',
            data=keyword_data
        )['data']
    
    def update_keyword_bid(
        self,
        campaign_id: int,
        ad_group_id: int,
        keyword_id: int,
        bid: float
    ) -> Dict:
        """Update keyword bid."""
        data = [{
            'id': keyword_id,
            'bidAmount': {'amount': str(bid), 'currency': 'USD'}
        }]
        
        return self._request(
            'PUT',
            f'campaigns/{campaign_id}/adgroups/{ad_group_id}/targetingkeywords/bulk',
            data=data
        )['data'][0]
```

### Reporting Methods

```python
class ReportingMixin:
    """Reporting methods."""
    
    def get_campaign_report(
        self,
        campaign_id: int,
        start_date: str,
        end_date: str,
        granularity: str = 'DAILY'
    ) -> Dict:
        """Get campaign performance report."""
        data = {
            'startTime': start_date,
            'endTime': end_date,
            'granularity': granularity,
            'selector': {
                'conditions': [{
                    'field': 'campaignId',
                    'operator': 'EQUALS',
                    'values': [str(campaign_id)]
                }]
            },
            'returnRowTotals': True
        }
        
        return self._request('POST', 'reports/campaigns', data=data)
    
    def get_keyword_report(
        self,
        campaign_id: int,
        start_date: str,
        end_date: str,
        granularity: str = 'TOTAL'
    ) -> Dict:
        """Get keyword performance report."""
        data = {
            'startTime': start_date,
            'endTime': end_date,
            'granularity': granularity,
            'returnRowTotals': True
        }
        
        return self._request(
            'POST',
            f'reports/campaigns/{campaign_id}/keywords',
            data=data
        )
    
    def get_search_terms_report(
        self,
        campaign_id: int,
        start_time: str,
        end_time: str,
        timezone: str = 'America/New_York'
    ) -> Dict:
        """Get search terms report.
        
        Args:
            start_time: ISO 8601 datetime string
            end_time: ISO 8601 datetime string
            timezone: IANA timezone
        """
        data = {
            'startTime': start_time,
            'endTime': end_time,
            'timeZone': timezone,
            'granularity': 'TOTAL',
            'returnRowTotals': False
        }
        
        return self._request(
            'POST',
            f'reports/campaigns/{campaign_id}/searchterms',
            data=data
        )
```

### Complete SDK Class

```python
class AppleSearchAdsSDK(
    AppleSearchAdsClient,
    CampaignMixin,
    AdGroupMixin,
    KeywordMixin,
    ReportingMixin
):
    """Complete Apple Search Ads SDK."""
    pass

# Usage
sdk = AppleSearchAdsSDK(
    org_id='1234567',
    cert_path='/path/to/cert.pem',
    key_path='/path/to/key.pem'
)

# Get campaigns
campaigns = sdk.get_campaigns(status='ENABLED')

# Create campaign
new_campaign = sdk.create_campaign(
    name='Test Campaign',
    daily_budget=50.0,
    adam_id=123456789,
    countries=['US']
)

# Get report
report = sdk.get_campaign_report(
    campaign_id=new_campaign['id'],
    start_date='2026-03-01',
    end_date='2026-03-12'
)
```

This custom SDK provides a clean, Pythonic interface to the Apple Search Ads API with built-in error handling, retry logic, and pagination support.