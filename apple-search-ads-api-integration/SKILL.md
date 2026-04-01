---
name: apple-search-ads-api-integration
description: "Integrate with Apple Search Ads Campaign Management API v5 for programmatic campaign automation. Use for authenticating with OAuth 2, managing campaigns and ad groups via API, creating and updating keywords programmatically, generating performance reports, implementing automated bid management, building custom dashboards, integrating with business intelligence systems, and developing agentic AI automation for Apple Search Ads at scale."
---

# Apple Search Ads API Integration

Programmatically manage Apple Search Ads campaigns using the Campaign Management API v5 for automation, reporting, and integration with external systems.

## Overview

The Apple Search Ads Campaign Management API enables developers, agencies, and third-party platforms to programmatically manage ad campaigns on the App Store. This skill covers API authentication, campaign and ad group management, keyword operations, reporting capabilities, and automation strategies for building scalable Apple Search Ads solutions.

## API Version Information

**Current Version:** API 5 (Released May 2024)

**Latest Updates:**
- **5.5 (February 2026):** Maximize Conversions automated bid strategy
- **5.4 (December 2025):** App Store preorder reporting metrics
- **5.3 (August 2025):** Enhanced budget order endpoints
- **5.2 (March 2025):** App details endpoints, custom product pages support
- **5.1 (October 2024):** Deep link support in ProductPageDetail
- **5.0 (May 2024):** View-through reporting, suggested bid amounts

**Deprecated:** All Creative Sets endpoints (unavailable in API 5)

**Previous Versions:**
- API 4: Available but superseded
- API 3: No longer supported (as of June 2023)
- API 2: No longer supported
- API 1: No longer supported

## Authentication

### OAuth 2.0 Setup

Apple Search Ads API uses OAuth 2.0 for authentication with client certificates.

**Prerequisites:**
- Active Apple Ads account
- Account Admin or API user role
- Access to Apple Ads account settings

### Creating API Credentials

**Step 1: Assign API Role**
1. Account Admin signs into Apple Ads account
2. Navigate to **Account Settings** > **User Management**
3. Edit existing user or invite new user
4. Assign API role:
   - **API Account Manager:** Full read/write access
   - **API Account Read Only:** Read-only access
   - **Limited Access API Read & Write:** Restricted read/write
   - **Limited Access API Read Only:** Restricted read-only

**Step 2: Generate API Certificate**
1. API user signs into Apple Ads account
2. Navigate to **Account Settings** > **API**
3. Click **Create API Client**
4. Follow documentation steps to generate certificate
5. Download certificate files:
   - **PEM file:** Public certificate
   - **Key file:** Private key
6. Store securely (certificate expires after 24 months)

**Step 3: Obtain Organization ID (orgId)**
- Found in Account Settings or via `Get User ACL` API call
- Required in header of all API requests
- Equivalent to campaign group
- Allows managing multiple clients or restricting access

### Authentication Flow

**Two-Way SSL Authentication:**
```python
import requests

# Load certificate and key
cert_file = 'path/to/certificate.pem'
key_file = 'path/to/private.key'

# API endpoint
base_url = 'https://api.searchads.apple.com/api/v5'

# Make authenticated request
headers = {
    'Authorization': 'orgId={YOUR_ORG_ID}',
    'Content-Type': 'application/json'
}

response = requests.get(
    f'{base_url}/campaigns',
    cert=(cert_file, key_file),
    headers=headers
)
```

**Required Headers:**
- `Authorization: orgId={YOUR_ORG_ID}` (required for all requests)
- `Content-Type: application/json` (for POST/PUT requests)

### Third-Party Access

**Granting Access:**
1. Account Admin or Campaign Group Manager grants access
2. Third-party signs in with Apple ID (secure sign-in)
3. Access can be reviewed and revoked anytime via API tab

**Managing Access:**
- Review active API clients in Account Settings > API
- Revoke access for specific clients
- Monitor API usage and activity

## Core API Capabilities

### Campaign Management

**Available Operations:**
- **Create Campaign:** Set up new campaigns with targeting and budget
- **Find Campaigns:** Search campaigns with filters and pagination
- **Get Campaign:** Retrieve specific campaign details
- **Update Campaign:** Modify campaign settings
- **Delete Campaign:** Remove campaigns (use with caution)

**Key Fields:**
- `name`: Campaign name
- `budgetAmount`: Total campaign budget (optional, API 5.2.1+)
- `dailyBudgetAmount`: Daily budget (required for new campaigns, API 5.0+)
- `adamId`: App ID from App Store
- `countriesOrRegions`: Target locations
- `supplySources`: Ad placements (APPSTORE_SEARCH_RESULTS, APPSTORE_SEARCH_TAB, APPSTORE_TODAY_TAB, APPSTORE_PRODUCT_PAGE)
- `status`: ENABLED or PAUSED
- `servingStatus`: Read-only serving status
- `servingStateReasons`: Reasons if not serving

### Ad Group Management

**Available Operations:**
- **Create Ad Group:** Set up ad groups within campaigns
- **Find Ad Groups:** Search ad groups (EQUALS operator only, API 5.1+)
- **Get Ad Group:** Retrieve specific ad group details
- **Update Ad Group:** Modify ad group settings
- **Delete Ad Group:** Remove ad groups

**Key Fields:**
- `name`: Ad group name
- `cpaGoal`: Target cost-per-acquisition (optional)
- `defaultBidAmount`: Default max CPT bid
- `startTime`: Ad group start date/time
- `endTime`: Ad group end date/time (optional)
- `status`: ENABLED or PAUSED
- `servingStatus`: Read-only serving status
- `targetingDimensions`: Targeting criteria (demographics, location, device, customer type)
- `automatedKeywordsOptIn`: Enable Search Match (boolean)

**Automated Ad Groups (API 5.5+):**
- Used with Maximize Conversions bid strategy
- Automatically discovers and bids on relevant keywords
- Requires Search Match enabled

### Keyword Management

**Targeting Keywords:**
- **Create Keywords:** Add keywords to ad groups
- **Find Keywords:** Search keywords with filters
- **Get Keyword:** Retrieve specific keyword details
- **Update Keywords:** Modify bids and match types

**Negative Keywords:**
- **Campaign-Level:** Apply to all ad groups in campaign
  - Create, Get, Update, Delete operations
- **Ad Group-Level:** Apply to specific ad group
  - Create, Get, Update, Delete operations

**Key Fields:**
- `text`: Keyword text
- `matchType`: EXACT or BROAD
- `bidAmount`: Max CPT bid for this keyword
- `status`: ACTIVE or PAUSED

**Keyword Recommendations (API 5.0+):**
- `suggestedBidAmount`: Replaces deprecated `bidMin` and `bidMax`
- Provides single recommended bid for keyword

### Reporting

**Available Reports:**

| Report Type | Endpoint | Granularity |
|-------------|----------|-------------|
| **Campaign-Level** | `GET /reports/campaigns` | Campaign performance |
| **Ad Group-Level** | `GET /reports/campaigns/{campaignId}/adgroups` | Ad group performance |
| **Keyword-Level** | `GET /reports/campaigns/{campaignId}/keywords` | Keyword performance |
| **Search Term-Level** | `GET /reports/campaigns/{campaignId}/searchterms` | Search term performance |
| **Creative Set-Level** | Deprecated in API 5 | N/A |

**Report Parameters:**
- `startTime`: Report start date (ISO 8601 format, required)
- `endTime`: Report end date (ISO 8601 format, required)
- `granularity`: HOURLY, DAILY, MONTHLY, or TOTAL
- `selector`: Filter and pagination
- `groupBy`: Dimension grouping
- `timeZone`: Timezone for report (required for search term reports, API 5.0+)
- `returnRowTotals`: Include row totals (boolean)
- `returnRecordsWithNoMetrics`: Include zero-metric rows (boolean)

**Key Metrics (SpendRow and ExtendedSpendRow):**

*Standard Metrics:*
- `impressions`: Ad views
- `taps`: Ad clicks
- `installs`: App installs
- `newDownloads`: First-time installs
- `redownloads`: Re-installs
- `latOnInstalls`: Installs from users who limited ad tracking
- `latOffInstalls`: Installs from users who allowed ad tracking
- `ttr`: Tap-through rate
- `avgCPA`: Average cost per acquisition
- `avgCPT`: Average cost per tap
- `localSpend`: Spend in local currency
- `conversionRate`: Install rate (installs / taps)

*View-Through Metrics (API 5.0+):*
- `viewInstalls`: Installs after viewing ad (without tapping)
- `viewNewDownloads`: New downloads from views
- `viewRedownloads`: Redownloads from views

*Preorder Metrics (API 5.4+):*
- `tapPreOrdersPlaced`: Preorders from taps
- `viewPreOrdersPlaced`: Preorders from views
- `totalPreOrdersPlaced`: Total preorders

### App Information

**Get App Details (API 5.2+):**
- Retrieve app information by Adam ID
- Returns app metadata, categories, supported devices

**Get Localized App Details (API 5.2+):**
- Retrieve localized app information
- Returns localized name, description, screenshots

**Find App Assets (API 5.2+):**
- Search for app creative assets
- Enhanced in API 5.2 for custom product pages

**Find Ad Creative Rejection Reasons (API 5.2+):**
- Retrieve reasons for ad creative rejections
- Enhanced in API 5.2

### Budget Orders

**Get Budget Order:**
- Retrieve budget order details
- Returns available budget, spend, status

**Get All Budget Orders (API 5.3+):**
- Returns all possible `SupplySource` values by default
- Provides comprehensive budget information

### Geo Locations

**Search Geo Locations:**
- Find available geographic targeting options
- Returns country, region, city options
- Use for populating targeting selectors

## API Request Structure

### Base URL
```
https://api.searchads.apple.com/api/v5
```

### Request Format

**GET Request Example:**
```python
import requests

headers = {
    'Authorization': 'orgId=1234567',
    'Content-Type': 'application/json'
}

response = requests.get(
    'https://api.searchads.apple.com/api/v5/campaigns',
    cert=('certificate.pem', 'private.key'),
    headers=headers
)

data = response.json()
```

**POST Request Example (Create Campaign):**
```python
import requests
import json

headers = {
    'Authorization': 'orgId=1234567',
    'Content-Type': 'application/json'
}

campaign_data = {
    'name': 'Brand Campaign - US',
    'budgetAmount': {'amount': '1000', 'currency': 'USD'},
    'dailyBudgetAmount': {'amount': '50', 'currency': 'USD'},
    'adamId': 123456789,
    'countriesOrRegions': ['US'],
    'supplySources': ['APPSTORE_SEARCH_RESULTS'],
    'status': 'ENABLED'
}

response = requests.post(
    'https://api.searchads.apple.com/api/v5/campaigns',
    cert=('certificate.pem', 'private.key'),
    headers=headers,
    data=json.dumps(campaign_data)
)

result = response.json()
```

### Response Format

**Successful Response:**
```json
{
  "data": {
    "id": 123456,
    "name": "Brand Campaign - US",
    "status": "ENABLED",
    ...
  },
  "pagination": {
    "totalResults": 1,
    "startIndex": 0,
    "itemsPerPage": 1
  }
}
```

**Error Response:**
```json
{
  "error": {
    "errors": [
      {
        "messageCode": "INVALID_PARAMETER",
        "message": "Invalid parameter value",
        "field": "dailyBudgetAmount"
      }
    ]
  }
}
```

### HTTP Response Codes

| Code | Meaning | Action |
|------|---------|--------|
| **200** | Success | Process response data |
| **201** | Created | Resource created successfully |
| **400** | Bad Request | Check request parameters |
| **401** | Unauthorized | Check authentication credentials |
| **403** | Forbidden | Check API permissions |
| **404** | Not Found | Resource doesn't exist |
| **429** | Too Many Requests | Implement rate limiting/backoff |
| **500** | Server Error | Retry with exponential backoff |

### Pagination

**Request Parameters:**
```python
params = {
    'limit': 100,  # Items per page (max 1000)
    'offset': 0    # Starting index
}
```

**Response Pagination:**
```json
{
  "data": [...],
  "pagination": {
    "totalResults": 250,
    "startIndex": 0,
    "itemsPerPage": 100
  }
}
```

**Iterating Through Pages:**
```python
offset = 0
limit = 100
all_campaigns = []

while True:
    response = requests.get(
        f'{base_url}/campaigns',
        cert=(cert_file, key_file),
        headers=headers,
        params={'limit': limit, 'offset': offset}
    )
    data = response.json()
    all_campaigns.extend(data['data'])
    
    if len(data['data']) < limit:
        break
    offset += limit
```

### Selectors and Filters

**Selector Structure:**
```python
selector = {
    'conditions': [
        {
            'field': 'status',
            'operator': 'EQUALS',
            'values': ['ENABLED']
        },
        {
            'field': 'countriesOrRegions',
            'operator': 'CONTAINS_ANY',
            'values': ['US', 'CA']
        }
    ],
    'orderBy': [
        {
            'field': 'name',
            'sortOrder': 'ASCENDING'
        }
    ],
    'pagination': {
        'offset': 0,
        'limit': 100
    }
}
```

**Available Operators:**
- `EQUALS`: Exact match
- `NOT_EQUALS`: Not equal
- `CONTAINS_ANY`: Contains any of values
- `CONTAINS_ALL`: Contains all values
- `GREATER_THAN`: Greater than
- `LESS_THAN`: Less than
- `IN`: In list
- `STARTSWITH`: Starts with

---

**Note:** This file was automatically condensed to meet the 500-line requirement. Additional content has been moved to the references/ folder.

## References

- [Api Endpoints Reference](references/api-endpoints-reference.md)
- [Automation Examples](references/automation-examples.md)
- [Python Sdk Guide](references/python-sdk-guide.md)
- [Reporting Guide](references/reporting-guide.md)
