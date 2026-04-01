# YouTube Ads & Google API: Implementation Guide

## Overview

The Google Ads API provides programmatic access to manage Google Ads campaigns, including those serving on YouTube. This guide covers API setup, authentication, campaign creation, and best practices for implementing YouTube advertising solutions through the API.

## Getting Started with Google Ads API

### Prerequisites

**Required Accounts and Access**:

1. **Google Ads Account**
   - Active Google Ads account (manager or standard)
   - Billing information configured
   - Compliance with Google Ads policies

2. **Google Ads Manager Account** (Recommended)
   - Centralized management of multiple accounts
   - Required for managing client accounts
   - Access to API features and reporting

3. **Developer Token**
   - Obtained from Google Ads API Center
   - Unique identifier for API access
   - Different access levels (test, basic, standard)

4. **OAuth 2.0 Credentials**
   - Client ID and Client Secret
   - Created in Google Cloud Console
   - Used for user authentication

### Access Levels

#### Test Access (Default)
- Immediate access upon token generation
- Limited to test accounts only
- Cannot access production accounts
- No spending limits
- Ideal for development and testing

#### Basic Access
- Request through API Center
- Access to production accounts
- $15,000 USD spending limit (90 days)
- Suitable for small-scale operations
- Approval typically within 24 hours

#### Standard Access
- Application required with detailed use case
- Unlimited spending
- Required for large-scale operations
- Approval process can take several days
- Must demonstrate API compliance and best practices

### Setting Up API Access

#### Step 1: Create Google Cloud Project

1. Navigate to [Google Cloud Console](https://console.cloud.google.com)
2. Create new project or select existing
3. Enable Google Ads API:
   - Go to "APIs & Services" > "Library"
   - Search for "Google Ads API"
   - Click "Enable"

#### Step 2: Create OAuth 2.0 Credentials

1. In Google Cloud Console, go to "APIs & Services" > "Credentials"
2. Click "Create Credentials" > "OAuth client ID"
3. Configure consent screen if prompted
4. Select application type:
   - **Desktop app**: For local scripts and applications
   - **Web application**: For web-based tools
5. Download credentials JSON file
6. Store securely (contains sensitive information)

#### Step 3: Obtain Developer Token

1. Sign in to Google Ads account
2. Navigate to "Tools & Settings" > "Setup" > "API Center"
3. Generate developer token
4. Copy and store securely
5. Request access level upgrade if needed

#### Step 4: Install Client Library

**Python** (Recommended):
```bash
pip install google-ads
```

**Java**:
```xml
<dependency>
  <groupId>com.google.api-ads</groupId>
  <artifactId>google-ads</artifactId>
  <version>LATEST_VERSION</version>
</dependency>
```

**PHP**:
```bash
composer require googleads/google-ads-php
```

**.NET**:
```bash
Install-Package Google.Ads.GoogleAds
```

**Ruby**:
```bash
gem install google-ads-googleads
```

### Authentication Flow

#### OAuth 2.0 Authentication Process

1. **Generate Authentication URL**:
   - Application creates URL with OAuth credentials
   - User is redirected to Google login

2. **User Authorization**:
   - User logs in with Google account
   - Grants permissions to application
   - Google redirects back with authorization code

3. **Exchange Code for Tokens**:
   - Application exchanges authorization code for tokens
   - Receives access token and refresh token
   - Access token used for API requests

4. **Token Refresh**:
   - Access tokens expire (typically 1 hour)
   - Refresh token used to obtain new access token
   - Refresh tokens generally don't expire (unless revoked)

#### Configuration File Setup

**google-ads.yaml** (Python, Ruby, PHP):
```yaml
developer_token: YOUR_DEVELOPER_TOKEN
client_id: YOUR_CLIENT_ID
client_secret: YOUR_CLIENT_SECRET
refresh_token: YOUR_REFRESH_TOKEN
login_customer_id: YOUR_MANAGER_ACCOUNT_ID
```

**App.config** (.NET):
```xml
<GoogleAdsApi>
  <DeveloperToken>YOUR_DEVELOPER_TOKEN</DeveloperToken>
  <OAuth2ClientId>YOUR_CLIENT_ID</OAuth2ClientId>
  <OAuth2ClientSecret>YOUR_CLIENT_SECRET</OAuth2ClientSecret>
  <OAuth2RefreshToken>YOUR_REFRESH_TOKEN</OAuth2RefreshToken>
  <LoginCustomerId>YOUR_MANAGER_ACCOUNT_ID</LoginCustomerId>
</GoogleAdsApi>
```

**ads.properties** (Java):
```properties
api.googleads.developerToken=YOUR_DEVELOPER_TOKEN
api.googleads.clientId=YOUR_CLIENT_ID
api.googleads.clientSecret=YOUR_CLIENT_SECRET
api.googleads.refreshToken=YOUR_REFRESH_TOKEN
api.googleads.loginCustomerId=YOUR_MANAGER_ACCOUNT_ID
```

## API Structure and Core Concepts

### Google Ads Query Language (GAQL)

**Description**: SQL-like query language for retrieving data from Google Ads API.

**Basic Syntax**:
```sql
SELECT field1, field2, field3
FROM resource_name
WHERE condition1 AND condition2
ORDER BY field1 DESC
LIMIT 100
```

**Example - Retrieve Campaign Data**:
```sql
SELECT 
  campaign.id,
  campaign.name,
  campaign.status,
  metrics.impressions,
  metrics.clicks,
  metrics.cost_micros
FROM campaign
WHERE campaign.status = 'ENABLED'
  AND segments.date DURING LAST_30_DAYS
ORDER BY metrics.impressions DESC
LIMIT 50
```

**Key Components**:

- **SELECT**: Specify fields to retrieve
- **FROM**: Resource type (campaign, ad_group, ad, etc.)
- **WHERE**: Filter conditions
- **ORDER BY**: Sort results
- **LIMIT**: Maximum number of results
- **segments.date**: Time-based filtering

### Resources and Services

**Core Resources**:

- **Campaign**: Top-level campaign settings
- **AdGroup**: Targeting and bidding within campaigns
- **Ad**: Individual ad creatives
- **Customer**: Account-level information
- **Asset**: Creative assets (images, videos, text)
- **AssetGroup**: Collections of assets (Performance Max, Demand Gen)

**Key Services**:

- **GoogleAdsService**: Primary service for querying data
- **CampaignService**: Create and manage campaigns
- **AdGroupService**: Manage ad groups
- **AdGroupAdService**: Manage ads
- **AssetService**: Upload and manage assets
- **AssetGroupService**: Manage asset groups
- **DataLinkService**: Link YouTube videos

### Mutate Operations

**Operation Types**:

1. **CREATE**: Add new entities
2. **UPDATE**: Modify existing entities
3. **REMOVE**: Delete entities

**Batch Operations**:
- Multiple operations in single request
- Reduces API calls and improves performance
- All-or-nothing or partial failure modes

**Example - Create Campaign**:
```python
from google.ads.googleads.client import GoogleAdsClient

client = GoogleAdsClient.load_from_storage("google-ads.yaml")
campaign_service = client.get_service("CampaignService")

campaign_operation = client.get_type("CampaignOperation")
campaign = campaign_operation.create

campaign.name = "Performance Max Campaign"
campaign.advertising_channel_type = client.enums.AdvertisingChannelTypeEnum.PERFORMANCE_MAX
campaign.status = client.enums.CampaignStatusEnum.PAUSED
campaign.campaign_budget = f"customers/{customer_id}/campaignBudgets/{budget_id}"

response = campaign_service.mutate_campaigns(
    customer_id=customer_id,
    operations=[campaign_operation]
)
```

## Creating YouTube Ad Campaigns via API

### Important: Video Campaign Limitations

**❌ Traditional Video Campaigns NOT Supported**:
- Cannot create new Video campaigns via API
- Cannot modify existing Video campaigns
- Cannot pause, enable, or change settings
- Cannot add or edit ad groups or ads

**✅ Supported Alternatives**:
- **Performance Max campaigns**: Fully supported
- **Demand Gen campaigns**: Fully supported
- Both can serve video ads on YouTube

**For Traditional Video Campaigns**:
- Use Google Ads UI for manual management
- Use Google Ads Scripts for programmatic management
- API limited to reporting/metrics retrieval only

### Creating Performance Max Campaigns

**Step-by-Step Process**:

#### 1. Create Campaign Budget

```python
budget_service = client.get_service("CampaignBudgetService")
budget_operation = client.get_type("CampaignBudgetOperation")

budget = budget_operation.create
budget.name = "Performance Max Budget"
budget.amount_micros = 5000000  # $5.00 in micros
budget.delivery_method = client.enums.BudgetDeliveryMethodEnum.STANDARD

response = budget_service.mutate_campaign_budgets(
    customer_id=customer_id,
    operations=[budget_operation]
)

budget_resource_name = response.results[0].resource_name
```

#### 2. Create Campaign

```python
campaign_service = client.get_service("CampaignService")
campaign_operation = client.get_type("CampaignOperation")

campaign = campaign_operation.create
campaign.name = "YouTube Performance Max Campaign"
campaign.advertising_channel_type = client.enums.AdvertisingChannelTypeEnum.PERFORMANCE_MAX
campaign.status = client.enums.CampaignStatusEnum.PAUSED
campaign.campaign_budget = budget_resource_name

# Set bidding strategy
campaign.maximize_conversions.target_cpa_micros = 10000000  # $10.00

# Set campaign dates
campaign.start_date = "20260401"
campaign.end_date = "20260430"

response = campaign_service.mutate_campaigns(
    customer_id=customer_id,
    operations=[campaign_operation]
)

campaign_resource_name = response.results[0].resource_name
```

#### 3. Set Conversion Goals

```python
# Configure conversion actions for campaign
campaign_conversion_goal_service = client.get_service(
    "CampaignConversionGoalService"
)

# Set specific conversion actions to optimize for
# (Implementation depends on existing conversion actions)
```

#### 4. Upload Video Assets

```python
asset_service = client.get_service("AssetService")
asset_operation = client.get_type("AssetOperation")

# YouTube video asset
video_asset = asset_operation.create
video_asset.type_ = client.enums.AssetTypeEnum.YOUTUBE_VIDEO
video_asset.youtube_video_asset.youtube_video_id = "YOUR_YOUTUBE_VIDEO_ID"

response = asset_service.mutate_assets(
    customer_id=customer_id,
    operations=[asset_operation]
)

video_asset_resource_name = response.results[0].resource_name
```

#### 5. Create Asset Group

```python
asset_group_service = client.get_service("AssetGroupService")
asset_group_operation = client.get_type("AssetGroupOperation")

asset_group = asset_group_operation.create
asset_group.name = "YouTube Asset Group"
asset_group.campaign = campaign_resource_name
asset_group.status = client.enums.AssetGroupStatusEnum.PAUSED

# Set final URLs
asset_group.final_urls.append("https://www.example.com")

response = asset_group_service.mutate_asset_groups(
    customer_id=customer_id,
    operations=[asset_group_operation]
)

asset_group_resource_name = response.results[0].resource_name
```

#### 6. Link Assets to Asset Group

```python
asset_group_asset_service = client.get_service("AssetGroupAssetService")

# Link video asset
video_operation = client.get_type("AssetGroupAssetOperation")
video_link = video_operation.create
video_link.asset_group = asset_group_resource_name
video_link.asset = video_asset_resource_name
video_link.field_type = client.enums.AssetFieldTypeEnum.YOUTUBE_VIDEO

# Add headlines, descriptions, images, etc.
# (Similar process for other asset types)

response = asset_group_asset_service.mutate_asset_group_assets(
    customer_id=customer_id,
    operations=[video_operation]  # Can batch multiple assets
)
```

#### 7. Set Audience Signals (Optional)

```python
asset_group_signal_service = client.get_service("AssetGroupSignalService")

# Add audience signals to guide optimization
# (Demographics, interests, custom audiences, etc.)
```

#### 8. Enable Campaign

```python
# Update campaign status to ENABLED
campaign_operation = client.get_type("CampaignOperation")
campaign_operation.update.resource_name = campaign_resource_name
campaign_operation.update.status = client.enums.CampaignStatusEnum.ENABLED
campaign_operation.update_mask = client.get_type("FieldMask")
campaign_operation.update_mask.paths.append("status")

response = campaign_service.mutate_campaigns(
    customer_id=customer_id,
    operations=[campaign_operation]
)
```

### Creating Demand Gen Campaigns

**Similar Process with Demand Gen Specifics**:

```python
# Create campaign with Demand Gen type
campaign.advertising_channel_type = client.enums.AdvertisingChannelTypeEnum.DEMAND_GEN

# Demand Gen supports more granular targeting
# Can set audience targeting at campaign or asset group level

# Asset groups work similarly to Performance Max
# Support for product feeds and dynamic assets
```

**Key Differences from Performance Max**:
- More control over placements (YouTube, Discover, Gmail)
- Audience targeting options
- Product feed integration
- Channel-specific controls

## Linking YouTube Videos

### Video Linking Workflow

#### Advertiser-Initiated Link Request

```python
data_link_service = client.get_service("DataLinkService")
data_link_operation = client.get_type("DataLinkOperation")

data_link = data_link_operation.create
data_link.type_ = client.enums.DataLinkTypeEnum.YOUTUBE_VIDEO
data_link.youtube_video.video_id = "YOUR_YOUTUBE_VIDEO_ID"

response = data_link_service.mutate_data_links(
    customer_id=customer_id,
    operations=[data_link_operation]
)

data_link_resource_name = response.results[0].resource_name
```

#### Check Link Status

```python
google_ads_service = client.get_service("GoogleAdsService")

query = f"""
    SELECT
        data_link.resource_name,
        data_link.type,
        data_link.status,
        data_link.youtube_video.video_id
    FROM data_link
    WHERE data_link.resource_name = '{data_link_resource_name}'
"""

response = google_ads_service.search(customer_id=customer_id, query=query)

for row in response:
    print(f"Status: {row.data_link.status}")
    print(f"Video ID: {row.data_link.youtube_video.video_id}")
```

#### Accept Creator-Initiated Request

```python
# List pending invitations
query = """
    SELECT
        data_link.resource_name,
        data_link.status,
        data_link.youtube_video.video_id
    FROM data_link
    WHERE data_link.status = 'PENDING'
"""

response = google_ads_service.search(customer_id=customer_id, query=query)

# Accept invitation
data_link_operation = client.get_type("DataLinkOperation")
data_link_operation.update.resource_name = pending_link_resource_name
data_link_operation.update.status = client.enums.DataLinkStatusEnum.ENABLED
data_link_operation.update_mask.paths.append("status")

response = data_link_service.mutate_data_links(
    customer_id=customer_id,
    operations=[data_link_operation]
)
```

#### Remove Linked Video

```python
data_link_operation = client.get_type("DataLinkOperation")
data_link_operation.remove = data_link_resource_name

response = data_link_service.mutate_data_links(
    customer_id=customer_id,
    operations=[data_link_operation]
)
```

### Common Errors

**DataLinkError.PERMISSION_DENIED**:
- Insufficient permissions to link video
- Video owner hasn't granted access
- Account doesn't have necessary permissions

**DataLinkError.YOUTUBE_VIDEO_ID_INVALID**:
- Invalid YouTube video ID format
- Video doesn't exist
- Video is private or deleted

**Solution**:
- Verify video ID is correct
- Ensure video is public or unlisted
- Confirm account permissions
- Check video ownership

## Retrieving Performance Data

### Campaign Performance Metrics

```python
query = """
    SELECT
        campaign.id,
        campaign.name,
        campaign.advertising_channel_type,
        metrics.impressions,
        metrics.clicks,
        metrics.cost_micros,
        metrics.conversions,
        metrics.video_views,
        metrics.video_view_rate,
        metrics.average_cpv
    FROM campaign
    WHERE campaign.advertising_channel_type IN ('PERFORMANCE_MAX', 'DEMAND_GEN', 'VIDEO')
        AND segments.date DURING LAST_30_DAYS
    ORDER BY metrics.impressions DESC
"""

response = google_ads_service.search_stream(customer_id=customer_id, query=query)

for batch in response:
    for row in batch.results:
        campaign = row.campaign
        metrics = row.metrics
        
        print(f"Campaign: {campaign.name}")
        print(f"Impressions: {metrics.impressions}")
        print(f"Clicks: {metrics.clicks}")
        print(f"Cost: ${metrics.cost_micros / 1_000_000:.2f}")
        print(f"Conversions: {metrics.conversions}")
        print(f"Video Views: {metrics.video_views}")
        print(f"View Rate: {metrics.video_view_rate:.2%}")
        print(f"Avg CPV: ${metrics.average_cpv / 1_000_000:.4f}")
        print("-" * 50)
```

### Video-Specific Metrics

```python
query = """
    SELECT
        campaign.name,
        ad_group.name,
        ad_group_ad.ad.name,
        metrics.video_quartile_p25_rate,
        metrics.video_quartile_p50_rate,
        metrics.video_quartile_p75_rate,
        metrics.video_quartile_p100_rate,
        metrics.video_view_rate,
        metrics.video_views
    FROM ad_group_ad
    WHERE campaign.advertising_channel_type = 'VIDEO'
        AND segments.date DURING LAST_7_DAYS
"""

response = google_ads_service.search(customer_id=customer_id, query=query)

for row in response:
    metrics = row.metrics
    print(f"Ad: {row.ad_group_ad.ad.name}")
    print(f"25% Completion: {metrics.video_quartile_p25_rate:.2%}")
    print(f"50% Completion: {metrics.video_quartile_p50_rate:.2%}")
    print(f"75% Completion: {metrics.video_quartile_p75_rate:.2%}")
    print(f"100% Completion: {metrics.video_quartile_p100_rate:.2%}")
    print(f"View Rate: {metrics.video_view_rate:.2%}")
    print(f"Total Views: {metrics.video_views}")
```

### Audience Performance

```python
query = """
    SELECT
        campaign.name,
        ad_group.name,
        ad_group_criterion.age_range.type,
        ad_group_criterion.gender.type,
        metrics.impressions,
        metrics.clicks,
        metrics.conversions
    FROM ad_group_criterion
    WHERE campaign.advertising_channel_type IN ('PERFORMANCE_MAX', 'DEMAND_GEN')
        AND segments.date DURING LAST_30_DAYS
"""

# Analyze performance by demographic segments
```

## Error Handling and Best Practices

### Common API Errors

#### Authentication Errors

**AUTHENTICATION_ERROR**:
- Invalid or expired access token
- Incorrect OAuth credentials
- Developer token issues

**Solution**:
```python
try:
    response = campaign_service.mutate_campaigns(
        customer_id=customer_id,
        operations=[campaign_operation]
    )
except GoogleAdsException as ex:
    for error in ex.failure.errors:
        if error.error_code.authentication_error:
            print("Authentication error - refresh token")
            # Implement token refresh logic
```

#### Authorization Errors

**AUTHORIZATION_ERROR**:
- Insufficient permissions
- Account access denied
- Manager account issues

**Solution**:
- Verify account access in Google Ads UI
- Check manager account linking
- Ensure proper OAuth scopes

#### Request Errors

**REQUEST_ERROR**:
- Invalid field values
- Missing required fields
- Malformed requests

**Solution**:
```python
try:
    response = campaign_service.mutate_campaigns(
        customer_id=customer_id,
        operations=[campaign_operation]
    )
except GoogleAdsException as ex:
    for error in ex.failure.errors:
        print(f"Error: {error.message}")
        print(f"Field: {error.location.field_path_elements}")
        # Fix specific field issues
```

### Rate Limiting

**API Rate Limits**:
- Requests per second limits
- Daily operation limits
- Varies by access level

**Best Practices**:

1. **Batch Operations**:
```python
# Instead of multiple single operations
operations = []
for item in items:
    operation = create_operation(item)
    operations.append(operation)

# Single batched request
response = service.mutate(
    customer_id=customer_id,
    operations=operations
)
```

2. **Implement Exponential Backoff**:
```python
import time
from google.api_core import retry

@retry.Retry(
    initial=1.0,
    maximum=60.0,
    multiplier=2.0,
    deadline=300.0
)
def make_api_call():
    return service.mutate_campaigns(
        customer_id=customer_id,
        operations=[operation]
    )
```

3. **Monitor Rate Limit Headers**:
- Check response headers for rate limit info
- Adjust request frequency accordingly

### Partial Failure Handling

**Enable Partial Failure Mode**:
```python
response = campaign_service.mutate_campaigns(
    customer_id=customer_id,
    operations=operations,
    partial_failure=True  # Allow some operations to fail
)

# Check for partial failures
if response.partial_failure_error:
    print("Some operations failed:")
    for error in response.partial_failure_error.details:
        print(f"Error: {error}")

# Process successful operations
for result in response.results:
    if result.resource_name:
        print(f"Success: {result.resource_name}")
```

### Logging and Monitoring

**Enable API Logging**:
```python
import logging

logging.basicConfig(level=logging.INFO)
logging.getLogger('google.ads.googleads').setLevel(logging.INFO)
```

**Log Important Events**:
- API requests and responses
- Errors and exceptions
- Performance metrics
- Rate limit warnings

## Further Reading

- Google Ads API Documentation: https://developers.google.com/google-ads/api
- Google Ads API Python Client Library: https://github.com/googleads/google-ads-python
- Google Ads Query Language (GAQL) Guide
- OAuth 2.0 for Google APIs
- Google Ads API Best Practices
- Performance Max Campaign Guide
- Demand Gen Campaign Documentation
