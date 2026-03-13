# Google Ads API Campaign Setup

Complete guide to creating and managing Search campaigns programmatically using Google Ads API v23+.

---

## Authentication & Setup

### OAuth 2.0 Configuration
1. **Create Google Cloud Project**
   - Navigate to Google Cloud Console
   - Enable Google Ads API
   - Create OAuth 2.0 credentials (Desktop app or Web app)

2. **Generate Refresh Token**
   ```python
   from google.oauth2.credentials import Credentials
   from google_auth_oauthlib.flow import InstalledAppFlow
   
   SCOPES = ['https://www.googleapis.com/auth/adwords']
   flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', SCOPES)
   credentials = flow.run_local_server(port=0)
   refresh_token = credentials.refresh_token
   ```

3. **Configure google-ads.yaml**
   ```yaml
   developer_token: YOUR_DEVELOPER_TOKEN
   client_id: YOUR_CLIENT_ID
   client_secret: YOUR_CLIENT_SECRET
   refresh_token: YOUR_REFRESH_TOKEN
   login_customer_id: MANAGER_ACCOUNT_ID
   ```

### API Client Initialization
```python
from google.ads.googleads.client import GoogleAdsClient

client = GoogleAdsClient.load_from_storage('google-ads.yaml')
customer_id = 'INSERT_CUSTOMER_ID_HERE'  # Without hyphens
```

---

## Campaign Creation

### Step 1: Create Campaign Budget
```python
def create_campaign_budget(client, customer_id, budget_amount_micros):
    campaign_budget_service = client.get_service('CampaignBudgetService')
    campaign_budget_operation = client.get_type('CampaignBudgetOperation')
    
    campaign_budget = campaign_budget_operation.create
    campaign_budget.name = f'Search Campaign Budget {uuid.uuid4()}'
    campaign_budget.delivery_method = client.enums.BudgetDeliveryMethodEnum.STANDARD
    campaign_budget.amount_micros = budget_amount_micros  # e.g., 50000000 = $50
    
    response = campaign_budget_service.mutate_campaign_budgets(
        customer_id=customer_id,
        operations=[campaign_budget_operation]
    )
    
    return response.results[0].resource_name
```

### Step 2: Create Search Campaign
```python
def create_search_campaign(client, customer_id, budget_resource_name):
    campaign_service = client.get_service('CampaignService')
    campaign_operation = client.get_type('CampaignOperation')
    
    campaign = campaign_operation.create
    campaign.name = f'Search Campaign {uuid.uuid4()}'
    campaign.advertising_channel_type = client.enums.AdvertisingChannelTypeEnum.SEARCH
    campaign.status = client.enums.CampaignStatusEnum.PAUSED  # Start paused
    campaign.campaign_budget = budget_resource_name
    
    # Bidding strategy - Target CPA
    campaign.target_cpa.target_cpa_micros = 10000000  # $10 target CPA
    
    # Network settings
    campaign.network_settings.target_google_search = True
    campaign.network_settings.target_search_network = True  # Search partners
    campaign.network_settings.target_content_network = False  # No Display
    campaign.network_settings.target_partner_search_network = False
    
    # Start and end dates (optional)
    campaign.start_date = '20260315'
    # campaign.end_date = '20261231'
    
    response = campaign_service.mutate_campaigns(
        customer_id=customer_id,
        operations=[campaign_operation]
    )
    
    return response.results[0].resource_name
```

### Alternative Bidding Strategies

#### Maximize Clicks
```python
campaign.maximize_clicks.target_spend_micros = 50000000  # Optional max CPC
```

#### Target ROAS
```python
campaign.target_roas.target_roas = 4.0  # 400% ROAS target
```

#### Maximize Conversions
```python
campaign.maximize_conversions.target_cpa_micros = 15000000  # Optional target
```

#### Manual CPC
```python
campaign.manual_cpc.enhanced_cpc_enabled = True  # Enable ECPC
```

---

## Ad Group Creation

```python
def create_ad_group(client, customer_id, campaign_resource_name, ad_group_name, cpc_bid_micros):
    ad_group_service = client.get_service('AdGroupService')
    ad_group_operation = client.get_type('AdGroupOperation')
    
    ad_group = ad_group_operation.create
    ad_group.name = ad_group_name
    ad_group.campaign = campaign_resource_name
    ad_group.status = client.enums.AdGroupStatusEnum.ENABLED
    ad_group.type_ = client.enums.AdGroupTypeEnum.SEARCH_STANDARD
    
    # CPC bid (for Manual CPC or as max for automated strategies)
    ad_group.cpc_bid_micros = cpc_bid_micros  # e.g., 2000000 = $2
    
    response = ad_group_service.mutate_ad_groups(
        customer_id=customer_id,
        operations=[ad_group_operation]
    )
    
    return response.results[0].resource_name
```

---

## Keyword Insertion

### Add Keywords to Ad Group
```python
def add_keywords(client, customer_id, ad_group_resource_name, keywords_list):
    """
    keywords_list: List of tuples [(keyword_text, match_type), ...]
    match_type: 'EXACT', 'PHRASE', 'BROAD'
    """
    ad_group_criterion_service = client.get_service('AdGroupCriterionService')
    operations = []
    
    for keyword_text, match_type in keywords_list:
        operation = client.get_type('AdGroupCriterionOperation')
        criterion = operation.create
        criterion.ad_group = ad_group_resource_name
        criterion.status = client.enums.AdGroupCriterionStatusEnum.ENABLED
        
        # Keyword settings
        criterion.keyword.text = keyword_text
        criterion.keyword.match_type = getattr(
            client.enums.KeywordMatchTypeEnum, match_type
        )
        
        # Optional: Set custom bid
        # criterion.cpc_bid_micros = 3000000  # $3
        
        operations.append(operation)
    
    response = ad_group_criterion_service.mutate_ad_group_criteria(
        customer_id=customer_id,
        operations=operations
    )
    
    return [result.resource_name for result in response.results]

# Example usage
keywords = [
    ('running shoes', 'EXACT'),
    ('running shoes', 'PHRASE'),
    ('best running shoes', 'PHRASE'),
    ('buy running shoes online', 'BROAD')
]
add_keywords(client, customer_id, ad_group_resource_name, keywords)
```

### Add Negative Keywords
```python
def add_negative_keywords(client, customer_id, campaign_resource_name, negative_keywords):
    campaign_criterion_service = client.get_service('CampaignCriterionService')
    operations = []
    
    for keyword_text, match_type in negative_keywords:
        operation = client.get_type('CampaignCriterionOperation')
        criterion = operation.create
        criterion.campaign = campaign_resource_name
        criterion.negative = True
        
        criterion.keyword.text = keyword_text
        criterion.keyword.match_type = getattr(
            client.enums.KeywordMatchTypeEnum, match_type
        )
        
        operations.append(operation)
    
    response = campaign_criterion_service.mutate_campaign_criteria(
        customer_id=customer_id,
        operations=operations
    )
    
    return response

# Example usage
negatives = [
    ('free', 'BROAD'),
    ('cheap', 'BROAD'),
    ('diy', 'PHRASE')
]
add_negative_keywords(client, customer_id, campaign_resource_name, negatives)
```

---

## Responsive Search Ad Creation

```python
def create_responsive_search_ad(client, customer_id, ad_group_resource_name, 
                                  headlines, descriptions, final_urls, path1='', path2=''):
    """
    headlines: List of strings (3-15 headlines, max 30 chars each)
    descriptions: List of strings (2-4 descriptions, max 90 chars each)
    final_urls: List of URLs (at least 1)
    """
    ad_group_ad_service = client.get_service('AdGroupAdService')
    ad_group_ad_operation = client.get_type('AdGroupAdOperation')
    
    ad_group_ad = ad_group_ad_operation.create
    ad_group_ad.ad_group = ad_group_resource_name
    ad_group_ad.status = client.enums.AdGroupAdStatusEnum.ENABLED
    
    # Responsive Search Ad
    rsa = ad_group_ad.ad.responsive_search_ad
    
    # Add headlines
    for headline_text in headlines:
        headline = client.get_type('AdTextAsset')
        headline.text = headline_text[:30]  # Enforce 30 char limit
        # Optional: Pin headline to position
        # headline.pinned_field = client.enums.ServedAssetFieldTypeEnum.HEADLINE_1
        rsa.headlines.append(headline)
    
    # Add descriptions
    for description_text in descriptions:
        description = client.get_type('AdTextAsset')
        description.text = description_text[:90]  # Enforce 90 char limit
        rsa.descriptions.append(description)
    
    # Final URLs and display path
    ad_group_ad.ad.final_urls.extend(final_urls)
    rsa.path1 = path1[:15]  # Max 15 chars
    rsa.path2 = path2[:15]
    
    response = ad_group_ad_service.mutate_ad_group_ads(
        customer_id=customer_id,
        operations=[ad_group_ad_operation]
    )
    
    return response.results[0].resource_name

# Example usage
headlines = [
    'Premium Running Shoes',
    'Free Shipping & Returns',
    'Shop Top Brands',
    'Save Up To 40% Off',
    'Lightweight & Comfortable',
    'Expert Fitting Available',
    'Trusted Since 1995',
    'Wide Selection In Stock',
    'Order Today, Ship Tomorrow',
    'Best Price Guarantee',
    'Running Shoes For All',
    'Marathon Ready Footwear',
    'Trail & Road Options',
    'Men & Women Sizes',
    'Customer Rated 4.8 Stars'
]

descriptions = [
    'Find the perfect running shoes for your training. Shop top brands with free shipping.',
    'Expert staff ready to help. Visit our store or shop online today.',
    'Huge selection of running shoes. All sizes and widths available.',
    'Get fitted by experts. Free returns within 60 days. Shop now.'
]

create_responsive_search_ad(
    client, customer_id, ad_group_resource_name,
    headlines, descriptions, 
    ['https://example.com/running-shoes'],
    path1='Running', path2='Shoes'
)
```

---

## Location Targeting

```python
def add_location_targeting(client, customer_id, campaign_resource_name, location_ids):
    """
    location_ids: List of geo target constants (e.g., [1023191] for New York)
    Find IDs: https://developers.google.com/google-ads/api/data/geotargets
    """
    campaign_criterion_service = client.get_service('CampaignCriterionService')
    operations = []
    
    for location_id in location_ids:
        operation = client.get_type('CampaignCriterionOperation')
        criterion = operation.create
        criterion.campaign = campaign_resource_name
        criterion.location.geo_target_constant = f'geoTargetConstants/{location_id}'
        
        operations.append(operation)
    
    response = campaign_criterion_service.mutate_campaign_criteria(
        customer_id=customer_id,
        operations=operations
    )
    
    return response

# Example: Target United States (2840) and Canada (2124)
add_location_targeting(client, customer_id, campaign_resource_name, [2840, 2124])
```

---

## Ad Schedule (Day/Hour Targeting)

```python
def add_ad_schedule(client, customer_id, campaign_resource_name, schedules):
    """
    schedules: List of dicts with day, start_hour, start_minute, end_hour, end_minute
    Example: [{'day': 'MONDAY', 'start_hour': 9, 'start_minute': 0, 'end_hour': 17, 'end_minute': 0}]
    """
    campaign_criterion_service = client.get_service('CampaignCriterionService')
    operations = []
    
    for schedule in schedules:
        operation = client.get_type('CampaignCriterionOperation')
        criterion = operation.create
        criterion.campaign = campaign_resource_name
        
        ad_schedule = criterion.ad_schedule
        ad_schedule.day_of_week = getattr(client.enums.DayOfWeekEnum, schedule['day'])
        ad_schedule.start_hour = schedule['start_hour']
        ad_schedule.start_minute = getattr(client.enums.MinuteOfHourEnum, f"ZERO" if schedule['start_minute'] == 0 else f"FIFTEEN")
        ad_schedule.end_hour = schedule['end_hour']
        ad_schedule.end_minute = getattr(client.enums.MinuteOfHourEnum, f"ZERO" if schedule['end_minute'] == 0 else f"FIFTEEN")
        
        operations.append(operation)
    
    response = campaign_criterion_service.mutate_campaign_criteria(
        customer_id=customer_id,
        operations=operations
    )
    
    return response
```

---

## Conversion Tracking Setup

```python
def create_conversion_action(client, customer_id, conversion_name, value_micros=0):
    conversion_action_service = client.get_service('ConversionActionService')
    conversion_action_operation = client.get_type('ConversionActionOperation')
    
    conversion_action = conversion_action_operation.create
    conversion_action.name = conversion_name
    conversion_action.type_ = client.enums.ConversionActionTypeEnum.WEBPAGE
    conversion_action.category = client.enums.ConversionActionCategoryEnum.PURCHASE
    conversion_action.status = client.enums.ConversionActionStatusEnum.ENABLED
    
    # Value settings
    conversion_action.value_settings.default_value = value_micros  # e.g., 50000000 = $50
    conversion_action.value_settings.always_use_default_value = True
    
    # Counting type
    conversion_action.counting_type = client.enums.ConversionActionCountingTypeEnum.ONE_PER_CLICK
    
    # Attribution model
    conversion_action.attribution_model_settings.attribution_model = client.enums.AttributionModelEnum.DATA_DRIVEN
    
    # Click-through conversion window (1-90 days)
    conversion_action.click_through_lookback_window_days = 30
    
    response = conversion_action_service.mutate_conversion_actions(
        customer_id=customer_id,
        operations=[conversion_action_operation]
    )
    
    return response.results[0].resource_name
```

---

## Bulk Operations Best Practices

### Batch Multiple Operations
```python
# Instead of individual calls, batch operations
operations = []
for i in range(100):
    operation = client.get_type('AdGroupCriterionOperation')
    # ... configure operation
    operations.append(operation)

# Single API call for all 100 operations
response = ad_group_criterion_service.mutate_ad_group_criteria(
    customer_id=customer_id,
    operations=operations,
    partial_failure=True  # Continue on errors
)
```

### Error Handling
```python
from google.ads.googleads.errors import GoogleAdsException

try:
    response = campaign_service.mutate_campaigns(
        customer_id=customer_id,
        operations=[campaign_operation]
    )
except GoogleAdsException as ex:
    print(f'Request failed with status {ex.error.code().name}')
    for error in ex.failure.errors:
        print(f'\tError: {error.message}')
        if error.location:
            for field in error.location.field_path_elements:
                print(f'\t\tField: {field.field_name}')
```

---

## Performance Reporting

### Campaign Performance Query
```python
def get_campaign_performance(client, customer_id, date_range='LAST_30_DAYS'):
    ga_service = client.get_service('GoogleAdsService')
    
    query = f"""
        SELECT
            campaign.id,
            campaign.name,
            metrics.impressions,
            metrics.clicks,
            metrics.ctr,
            metrics.average_cpc,
            metrics.cost_micros,
            metrics.conversions,
            metrics.cost_per_conversion,
            metrics.conversion_rate
        FROM campaign
        WHERE segments.date DURING {date_range}
        ORDER BY metrics.impressions DESC
    """
    
    response = ga_service.search_stream(customer_id=customer_id, query=query)
    
    results = []
    for batch in response:
        for row in batch.results:
            results.append({
                'campaign_id': row.campaign.id,
                'campaign_name': row.campaign.name,
                'impressions': row.metrics.impressions,
                'clicks': row.metrics.clicks,
                'ctr': row.metrics.ctr,
                'avg_cpc': row.metrics.average_cpc / 1000000,
                'cost': row.metrics.cost_micros / 1000000,
                'conversions': row.metrics.conversions,
                'cost_per_conversion': row.metrics.cost_per_conversion / 1000000 if row.metrics.conversions > 0 else 0,
                'conversion_rate': row.metrics.conversion_rate
            })
    
    return results
```

### Search Terms Report
```python
def get_search_terms(client, customer_id, campaign_id=None):
    ga_service = client.get_service('GoogleAdsService')
    
    campaign_filter = f"AND campaign.id = {campaign_id}" if campaign_id else ""
    
    query = f"""
        SELECT
            search_term_view.search_term,
            search_term_view.status,
            metrics.impressions,
            metrics.clicks,
            metrics.ctr,
            metrics.cost_micros,
            metrics.conversions
        FROM search_term_view
        WHERE segments.date DURING LAST_30_DAYS
        {campaign_filter}
        ORDER BY metrics.impressions DESC
        LIMIT 1000
    """
    
    response = ga_service.search_stream(customer_id=customer_id, query=query)
    
    results = []
    for batch in response:
        for row in batch.results:
            results.append({
                'search_term': row.search_term_view.search_term,
                'status': row.search_term_view.status.name,
                'impressions': row.metrics.impressions,
                'clicks': row.metrics.clicks,
                'ctr': row.metrics.ctr,
                'cost': row.metrics.cost_micros / 1000000,
                'conversions': row.metrics.conversions
            })
    
    return results
```

---

## Rate Limits & Quotas

- **Standard Access**: 15,000 operations per day
- **Basic Access**: 15,000 operations per day  
- **Standard Access (higher tier)**: 1,000,000+ operations per day
- **Rate limit**: Approximately 1 request per second per account

### Best Practices
1. Use `partial_failure=True` for bulk operations
2. Implement exponential backoff for rate limit errors
3. Cache frequently accessed data (campaign structures)
4. Use `search_stream` instead of `search` for large result sets
5. Batch operations when possible (max 5,000 per request)