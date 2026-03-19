# Microsoft Ads API SDK Implementation Guide

## Introduction

Microsoft provides official Software Development Kits (SDKs) for the Bing Ads API in multiple programming languages, simplifying integration and reducing development time. This guide covers SDK installation, configuration, and implementation patterns for Python and C#, the two most popular languages for Microsoft Ads API development.

## SDK Overview

### Supported Languages

Microsoft offers official SDKs for:

1. **.NET (C#)**: Full-featured SDK for .NET applications
2. **Java**: Comprehensive Java SDK
3. **PHP**: PHP SDK for web applications
4. **Python**: Python SDK for scripting and automation

### SDK Benefits

**Simplified Development:**
- Pre-built proxy classes for all API services
- Automatic OAuth authentication handling
- Built-in error handling and retry logic
- Type-safe operations

**High-Level Abstractions:**
- **BulkServiceManager**: Simplified bulk operations
- **ReportingServiceManager**: Easy report generation and download
- **ServiceClient**: Unified interface for all services

**Reduced Boilerplate:**
- No manual SOAP envelope construction
- Automatic serialization/deserialization
- Built-in token refresh management

### SDK Architecture

```
Application Code
    ↓
SDK High-Level Managers (BulkServiceManager, ReportingServiceManager)
    ↓
SDK Service Clients (ServiceClient)
    ↓
SDK Core (Authentication, HTTP, Serialization)
    ↓
Microsoft Advertising API (SOAP Web Services)
```

## Python SDK

### Installation

#### Requirements

- Python 3.3 or higher
- pip package manager

#### Install via pip

```bash
pip install bingads
```

#### Verify Installation

```python
import bingads
print(bingads.__version__)  # Should print version number (e.g., 13.0.x)
```

### Python SDK Structure

**Core Modules:**
- `bingads`: Main package
- `bingads.authorization`: OAuth authentication classes
- `bingads.service_client`: Service client for API calls
- `bingads.v13.bulk`: Bulk service operations
- `bingads.v13.reporting`: Reporting service operations
- `bingads.v13.campaignmanagement`: Campaign management objects
- `bingads.v13.customermanagement`: Customer management objects

### Authentication Setup

#### OAuth Configuration

```python
from bingads import AuthorizationData, OAuthWebAuthCodeGrant
from bingads.service_client import ServiceClient

# OAuth credentials
CLIENT_ID = 'your_client_id'
CLIENT_SECRET = 'your_client_secret'
REDIRECT_URI = 'https://your-app.com/callback'
DEVELOPER_TOKEN = 'your_developer_token'

# Create OAuth provider
oauth = OAuthWebAuthCodeGrant(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirection_uri=REDIRECT_URI
)

# First-time authorization
if not oauth.refresh_token:
    # Get authorization URL
    auth_url = oauth.get_authorization_endpoint()
    print(f"Visit this URL to authorize: {auth_url}")
    
    # User visits URL and authorizes
    # You receive authorization code via redirect
    auth_code = input("Enter authorization code: ")
    
    # Exchange code for tokens
    oauth.request_oauth_tokens_by_authorization_code(auth_code)
    
    # Save refresh token for future use
    with open('refresh_token.txt', 'w') as f:
        f.write(oauth.refresh_token)
else:
    # Load saved refresh token
    with open('refresh_token.txt', 'r') as f:
        oauth.refresh_token = f.read().strip()

# Create authorization data
authorization_data = AuthorizationData(
    account_id='your_account_id',
    customer_id='your_customer_id',
    developer_token=DEVELOPER_TOKEN,
    authentication=oauth
)
```

#### Token Refresh Handling

```python
def get_authorization_data():
    """Get authorization data with automatic token refresh."""
    oauth = OAuthWebAuthCodeGrant(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirection_uri=REDIRECT_URI
    )
    
    # Load refresh token
    try:
        with open('refresh_token.txt', 'r') as f:
            oauth.refresh_token = f.read().strip()
    except FileNotFoundError:
        raise Exception("No refresh token found. Please authenticate first.")
    
    authorization_data = AuthorizationData(
        account_id=ACCOUNT_ID,
        customer_id=CUSTOMER_ID,
        developer_token=DEVELOPER_TOKEN,
        authentication=oauth
    )
    
    return authorization_data
```

### Service Client Usage

#### Creating Service Clients

```python
from bingads.service_client import ServiceClient

# Campaign Management Service
campaign_service = ServiceClient(
    service='CampaignManagementService',
    version=13,
    authorization_data=authorization_data
)

# Customer Management Service
customer_service = ServiceClient(
    service='CustomerManagementService',
    version=13,
    authorization_data=authorization_data
)

# Reporting Service
reporting_service = ServiceClient(
    service='ReportingService',
    version=13,
    authorization_data=authorization_data
)
```

#### Making API Calls

```python
# Get campaigns
campaigns = campaign_service.GetCampaignsByAccountId(
    AccountId=authorization_data.account_id,
    CampaignType='Search Shopping'
)

for campaign in campaigns['Campaign']:
    print(f"Campaign: {campaign.Name}, ID: {campaign.Id}")
```

### Working with Data Objects

#### Creating Campaigns

```python
from bingads.v13.campaignmanagement import (
    Campaign,
    ManualCpcBiddingScheme,
    DailyBudgetStandard
)

# Create campaign object
campaign = Campaign(
    Name="Python SDK Test Campaign",
    Description="Campaign created via Python SDK",
    BudgetType='DailyBudgetStandard',
    DailyBudget=50.00,
    TimeZone='EasternTimeUSCanada',
    CampaignType='Search',
    Status='Paused',
    Languages=['English'],
    BiddingScheme=ManualCpcBiddingScheme()
)

# Add campaign
response = campaign_service.AddCampaigns(
    AccountId=authorization_data.account_id,
    Campaigns=[campaign]
)

campaign_id = response.CampaignIds['long'][0]
print(f"Created campaign with ID: {campaign_id}")
```

#### Creating Ad Groups

```python
from bingads.v13.campaignmanagement import AdGroup

ad_group = AdGroup(
    Name="Python SDK Ad Group",
    CampaignId=campaign_id,
    CpcBid=1.50,
    Language='English',
    Network='OwnedAndOperatedAndSyndicatedSearch',
    Status='Paused'
)

response = campaign_service.AddAdGroups(
    CampaignId=campaign_id,
    AdGroups=[ad_group]
)

ad_group_id = response.AdGroupIds['long'][0]
print(f"Created ad group with ID: {ad_group_id}")
```

#### Creating Keywords

```python
from bingads.v13.campaignmanagement import Keyword

keywords = [
    Keyword(
        Text='microsoft advertising api',
        MatchType='Exact',
        Bid=2.00,
        Status='Active'
    ),
    Keyword(
        Text='bing ads sdk',
        MatchType='Phrase',
        Bid=1.75,
        Status='Active'
    )
]

response = campaign_service.AddKeywords(
    AdGroupId=ad_group_id,
    Keywords=keywords
)

keyword_ids = response.KeywordIds['long']
print(f"Created {len(keyword_ids)} keywords")
```

#### Creating Responsive Search Ads

```python
from bingads.v13.campaignmanagement import (
    ResponsiveSearchAd,
    AssetLink,
    TextAsset
)

# Create headlines
headlines = [
    AssetLink(Asset=TextAsset(Text="Microsoft Advertising API")),
    AssetLink(Asset=TextAsset(Text="Bing Ads SDK")),
    AssetLink(Asset=TextAsset(Text="Automate Your Campaigns")),
    AssetLink(Asset=TextAsset(Text="Python Integration")),
]

# Create descriptions
descriptions = [
    AssetLink(Asset=TextAsset(Text="Powerful API for campaign automation and management.")),
    AssetLink(Asset=TextAsset(Text="Easy integration with Python SDK. Get started today.")),
]

# Create responsive search ad
rsa = ResponsiveSearchAd(
    Headlines=headlines,
    Descriptions=descriptions,
    Path1='api',
    Path2='python',
    FinalUrls=['https://example.com/api'],
    Status='Active'
)

response = campaign_service.AddAds(
    AdGroupId=ad_group_id,
    Ads=[rsa]
)

ad_id = response.AdIds['long'][0]
print(f"Created ad with ID: {ad_id}")
```

### Bulk Operations with BulkServiceManager

#### Setup

```python
from bingads.v13.bulk import BulkServiceManager, BulkDownloadEntity

bulk_service_manager = BulkServiceManager(
    authorization_data=authorization_data,
    poll_interval_in_milliseconds=5000,
    environment='production'
)
```

#### Download Campaigns

```python
import os

# Define download parameters
download_parameters = {
    'DataScope': ['EntityData', 'QualityScoreData'],
    'DownloadEntities': [
        BulkDownloadEntity.Campaigns,
        BulkDownloadEntity.AdGroups,
        BulkDownloadEntity.Keywords,
        BulkDownloadEntity.Ads
    ],
    'FileType': 'Csv',
    'LastSyncTimeInUTC': None,
    'PerformanceStatsDateRange': None
}

# Download
file_path = bulk_service_manager.download_file(
    download_parameters=download_parameters,
    result_file_directory='downloads',
    result_file_name='bulk_download.csv',
    overwrite_result_file=True,
    timeout_in_milliseconds=3600000  # 1 hour
)

print(f"Downloaded to: {file_path}")
```

#### Upload Campaigns

```python
from bingads.v13.bulk import BulkCampaign, BulkAdGroup, BulkKeyword

# Create bulk entities
bulk_campaign = BulkCampaign()
bulk_campaign.campaign = Campaign(
    Name="Bulk Upload Campaign",
    BudgetType='DailyBudgetStandard',
    DailyBudget=100.00,
    TimeZone='EasternTimeUSCanada',
    CampaignType='Search',
    Status='Paused',
    Languages=['English']
)

# Write to file
from bingads.v13.bulk import BulkFileWriter

with BulkFileWriter('uploads/bulk_upload.csv') as writer:
    writer.write_entity(bulk_campaign)

# Upload
upload_parameters = {
    'ResponseMode': 'ErrorsAndResults',
    'OverwriteResultFile': True
}

file_path = bulk_service_manager.upload_file(
    upload_parameters=upload_parameters,
    file_path='uploads/bulk_upload.csv',
    result_file_directory='uploads',
    result_file_name='bulk_upload_results.csv',
    timeout_in_milliseconds=3600000
)

print(f"Upload results: {file_path}")
```

### Reporting with ReportingServiceManager

```python
from bingads.v13.reporting import ReportingServiceManager
from bingads.v13.reporting import (
    CampaignPerformanceReportRequest,
    ReportFormat,
    ReportAggregation,
    CampaignPerformanceReportColumn,
    AccountThroughCampaignReportScope,
    ReportTime,
    ReportTimePeriod
)

# Create reporting service manager
reporting_service_manager = ReportingServiceManager(
    authorization_data=authorization_data,
    poll_interval_in_milliseconds=5000,
    environment='production'
)

# Define report request
report_request = CampaignPerformanceReportRequest(
    Format=ReportFormat.Csv,
    ReportName='Campaign Performance Report',
    ReturnOnlyCompleteData=False,
    Aggregation=ReportAggregation.Daily,
    Columns=[
        CampaignPerformanceReportColumn.TimePeriod,
        CampaignPerformanceReportColumn.CampaignName,
        CampaignPerformanceReportColumn.Impressions,
        CampaignPerformanceReportColumn.Clicks,
        CampaignPerformanceReportColumn.Spend,
        CampaignPerformanceReportColumn.Conversions,
    ],
    Scope=AccountThroughCampaignReportScope(
        AccountIds=[authorization_data.account_id],
        Campaigns=None
    ),
    Time=ReportTime(
        PredefinedTime=ReportTimePeriod.LastSevenDays
    )
)

# Submit and download report
report_file_path = reporting_service_manager.download_file(
    report_request=report_request,
    result_file_directory='reports',
    result_file_name='campaign_performance.csv',
    overwrite_result_file=True,
    timeout_in_milliseconds=3600000
)

print(f"Report downloaded to: {report_file_path}")
```

### Python SDK with Suds

The Python SDK uses the `suds-jurko` library as a SOAP client.

#### Common Suds Considerations

**Namespace Prefixes:**

If you encounter errors like `(ClassGoesHere) not-found`, use namespace prefixes:

```python
# Print SOAP client to see namespaces
print(campaign_service.soap_client)

# Use namespace prefix
from suds import WebFault
try:
    # Your API call
    pass
except WebFault as e:
    print(f"SOAP Fault: {e}")
```

**Dictionary Objects vs. Factory:**

For better performance, use dictionary objects when possible:

```python
# Using dictionary (faster)
campaign_dict = {
    'Name': 'Test Campaign',
    'BudgetType': 'DailyBudgetStandard',
    'DailyBudget': 50.00
}

# Using factory (required for derived types)
campaign = campaign_service.factory.create('Campaign')
campaign.Name = 'Test Campaign'
```

**Non-Primitive Elements:**

Specify all elements, even if read-only (set to `None`):

```python
campaign = campaign_service.factory.create('Campaign')
campaign.Id = None  # Read-only, but must be specified
campaign.Name = 'Test Campaign'
```

## C# SDK

### Installation

#### NuGet Package

```bash
Install-Package Microsoft.BingAds.SDK
```

Or via .NET CLI:

```bash
dotnet add package Microsoft.BingAds.SDK
```

### C# SDK Structure

**Namespaces:**
- `Microsoft.BingAds`: Core SDK classes
- `Microsoft.BingAds.V13.CampaignManagement`: Campaign management service
- `Microsoft.BingAds.V13.CustomerManagement`: Customer management service
- `Microsoft.BingAds.V13.Reporting`: Reporting service
- `Microsoft.BingAds.V13.Bulk`: Bulk service

### Authentication Setup

```csharp
using Microsoft.BingAds;
using Microsoft.BingAds.V13.CampaignManagement;

// OAuth credentials
var clientId = "your_client_id";
var clientSecret = "your_client_secret";
var redirectUri = new Uri("https://your-app.com/callback");
var developerToken = "your_developer_token";

// Create OAuth provider
var oAuthWebAuthCodeGrant = new OAuthWebAuthCodeGrant(
    clientId,
    clientSecret,
    redirectUri
);

// First-time authorization
if (string.IsNullOrEmpty(oAuthWebAuthCodeGrant.RefreshToken))
{
    var authorizationUrl = oAuthWebAuthCodeGrant.GetAuthorizationEndpoint();
    Console.WriteLine($"Visit: {authorizationUrl}");
    
    Console.Write("Enter authorization code: ");
    var authCode = Console.ReadLine();
    
    await oAuthWebAuthCodeGrant.RequestAccessAndRefreshTokensAsync(authCode);
    
    // Save refresh token
    File.WriteAllText("refresh_token.txt", oAuthWebAuthCodeGrant.RefreshToken);
}
else
{
    // Load refresh token
    oAuthWebAuthCodeGrant.RefreshToken = File.ReadAllText("refresh_token.txt");
}

// Create authorization data
var authorizationData = new AuthorizationData
{
    Authentication = oAuthWebAuthCodeGrant,
    DeveloperToken = developerToken,
    AccountId = long.Parse("your_account_id"),
    CustomerId = long.Parse("your_customer_id")
};
```

### Service Client Usage

```csharp
using (var campaignService = new ServiceClient<ICampaignManagementService>(
    authorizationData))
{
    // Get campaigns
    var request = new GetCampaignsByAccountIdRequest
    {
        AccountId = authorizationData.AccountId,
        CampaignType = CampaignType.Search | CampaignType.Shopping
    };
    
    var response = await campaignService.CallAsync(
        (s, r) => s.GetCampaignsByAccountIdAsync(r),
        request
    );
    
    foreach (var campaign in response.Campaigns)
    {
        Console.WriteLine($"Campaign: {campaign.Name}, ID: {campaign.Id}");
    }
}
```

### Creating Campaigns

```csharp
var campaign = new Campaign
{
    Name = "C# SDK Test Campaign",
    Description = "Campaign created via C# SDK",
    BudgetType = BudgetLimitType.DailyBudgetStandard,
    DailyBudget = 50.00,
    TimeZone = "EasternTimeUSCanada",
    CampaignType = CampaignType.Search,
    Status = CampaignStatus.Paused,
    Languages = new[] { "English" },
    BiddingScheme = new ManualCpcBiddingScheme()
};

using (var campaignService = new ServiceClient<ICampaignManagementService>(
    authorizationData))
{
    var request = new AddCampaignsRequest
    {
        AccountId = authorizationData.AccountId,
        Campaigns = new[] { campaign }
    };
    
    var response = await campaignService.CallAsync(
        (s, r) => s.AddCampaignsAsync(r),
        request
    );
    
    var campaignId = response.CampaignIds[0];
    Console.WriteLine($"Created campaign with ID: {campaignId}");
}
```

### Bulk Operations

```csharp
using Microsoft.BingAds.V13.Bulk;
using Microsoft.BingAds.V13.Bulk.Entities;

var bulkServiceManager = new BulkServiceManager(
    authorizationData,
    ApiEnvironment.Production
);

// Download
var downloadParameters = new DownloadParameters
{
    DataScope = DataScope.EntityData,
    DownloadEntities = new[]
    {
        DownloadEntity.Campaigns,
        DownloadEntity.AdGroups,
        DownloadEntity.Keywords
    },
    FileType = DownloadFileType.Csv,
    ResultFileDirectory = "downloads",
    ResultFileName = "bulk_download.csv",
    OverwriteResultFile = true
};

var filePath = await bulkServiceManager.DownloadFileAsync(downloadParameters);
Console.WriteLine($"Downloaded to: {filePath}");
```

### Reporting

```csharp
using Microsoft.BingAds.V13.Reporting;

var reportingServiceManager = new ReportingServiceManager(
    authorizationData,
    ApiEnvironment.Production
);

var reportRequest = new CampaignPerformanceReportRequest
{
    Format = ReportFormat.Csv,
    ReportName = "Campaign Performance Report",
    ReturnOnlyCompleteData = false,
    Aggregation = ReportAggregation.Daily,
    Columns = new[]
    {
        CampaignPerformanceReportColumn.TimePeriod,
        CampaignPerformanceReportColumn.CampaignName,
        CampaignPerformanceReportColumn.Impressions,
        CampaignPerformanceReportColumn.Clicks,
        CampaignPerformanceReportColumn.Spend
    },
    Scope = new AccountThroughCampaignReportScope
    {
        AccountIds = new[] { authorizationData.AccountId },
        Campaigns = null
    },
    Time = new ReportTime
    {
        PredefinedTime = ReportTimePeriod.LastSevenDays
    }
};

var reportFilePath = await reportingServiceManager.DownloadFileAsync(
    reportRequest,
    "reports",
    "campaign_performance.csv",
    true,
    3600000
);

Console.WriteLine($"Report downloaded to: {reportFilePath}");
```

## Error Handling

### Python Error Handling

```python
from bingads.exceptions import OAuthTokenRequestException, FaultException
from suds import WebFault

try:
    campaigns = campaign_service.GetCampaignsByAccountId(
        AccountId=authorization_data.account_id
    )
except OAuthTokenRequestException as e:
    print(f"OAuth error: {e.error_description}")
    # Re-authenticate
except FaultException as e:
    print(f"API Fault: {e.message}")
    print(f"Error Code: {e.error_code}")
except WebFault as e:
    print(f"SOAP Fault: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

### C# Error Handling

```csharp
using Microsoft.BingAds;

try
{
    var response = await campaignService.CallAsync(
        (s, r) => s.GetCampaignsByAccountIdAsync(r),
        request
    );
}
catch (OAuthTokenRequestException ex)
{
    Console.WriteLine($"OAuth error: {ex.Details.Description}");
    // Re-authenticate
}
catch (FaultException<Microsoft.BingAds.V13.CampaignManagement.AdApiFaultDetail> ex)
{
    Console.WriteLine($"API Fault: {ex.Detail.Errors[0].Message}");
}
catch (Exception ex)
{
    Console.WriteLine($"Unexpected error: {ex.Message}");
}
```

## Best Practices

### Token Management

1. **Always save refresh tokens**: Persist to secure storage
2. **Handle token expiration**: Implement automatic refresh
3. **Secure storage**: Never commit tokens to version control
4. **Monitor expiration**: Refresh tokens expire after 90 days of inactivity

### Performance Optimization

1. **Use bulk operations**: For large-scale changes
2. **Batch API calls**: Reduce network overhead
3. **Implement caching**: Cache frequently accessed data
4. **Parallel processing**: Use async/await for concurrent operations

### Error Handling

1. **Implement retry logic**: Exponential backoff for transient errors
2. **Log errors**: Comprehensive error logging
3. **Graceful degradation**: Handle partial failures
4. **Monitor rate limits**: Respect API quotas

### Code Organization

1. **Separate concerns**: Authentication, API calls, business logic
2. **Use configuration files**: Externalize credentials and settings
3. **Implement logging**: Track API usage and errors
4. **Write tests**: Unit and integration tests

## Conclusion

The Microsoft Ads API SDKs for Python and C# significantly simplify integration by providing high-level abstractions, automatic authentication handling, and built-in error management. By leveraging the BulkServiceManager for large-scale operations and ReportingServiceManager for performance data, developers can build robust, efficient advertising automation solutions. Following best practices for token management, error handling, and code organization ensures reliable, maintainable API integrations that scale with business needs.
