# Apple Search Ads API Endpoints Reference

Comprehensive reference for all Apple Search Ads Campaign Management API v5 endpoints with detailed parameters, request/response formats, and examples.

---

## Base URL

```
https://api.searchads.apple.com/api/v5
```

---

## Campaign Endpoints

### Create a Campaign

**Endpoint:** `POST /campaigns`

**Description:** Creates a new campaign.

**Request Body:**
```json
{
  "name": "Brand Campaign - US",
  "budgetAmount": {
    "amount": "1000.00",
    "currency": "USD"
  },
  "dailyBudgetAmount": {
    "amount": "50.00",
    "currency": "USD"
  },
  "adamId": 123456789,
  "countriesOrRegions": ["US"],
  "supplySources": ["APPSTORE_SEARCH_RESULTS"],
  "status": "ENABLED",
  "billingEvent": "TAPS",
  "displayStatus": "RUNNING"
}
```

**Required Fields:**
- `name`: Campaign name (string)
- `dailyBudgetAmount`: Daily budget (object with amount and currency) - Required in API 5.0+
- `adamId`: App Store app ID (integer)
- `countriesOrRegions`: Array of country codes (e.g., ["US", "CA"])

**Optional Fields:**
- `budgetAmount`: Total campaign budget (API 5.2.1+)
- `supplySources`: Ad placements (default: all available)
- `status`: ENABLED or PAUSED (default: PAUSED)
- `billingEvent`: TAPS (default)
- `displayStatus`: RUNNING or ON_HOLD

**Supply Sources:**
- `APPSTORE_SEARCH_RESULTS`: Search results ads
- `APPSTORE_SEARCH_TAB`: Search tab ads
- `APPSTORE_TODAY_TAB`: Today tab ads
- `APPSTORE_PRODUCT_PAGE`: Product page ads

**Response:**
```json
{
  "data": {
    "id": 123456,
    "orgId": 7654321,
    "name": "Brand Campaign - US",
    "budgetAmount": {
      "amount": "1000.00",
      "currency": "USD"
    },
    "dailyBudgetAmount": {
      "amount": "50.00",
      "currency": "USD"
    },
    "adamId": 123456789,
    "countriesOrRegions": ["US"],
    "supplySources": ["APPSTORE_SEARCH_RESULTS"],
    "status": "ENABLED",
    "servingStatus": "RUNNING",
    "servingStateReasons": null,
    "creationTime": "2026-03-12T10:00:00.000",
    "modificationTime": "2026-03-12T10:00:00.000"
  },
  "pagination": null,
  "error": null
}
```

### Find Campaigns

**Endpoint:** `GET /campaigns`

**Description:** Retrieves campaigns with optional filtering.

**Query Parameters:**
- `limit`: Number of results per page (max 1000)
- `offset`: Starting index for pagination

**Request Body (Optional Selector):**
```json
{
  "conditions": [
    {
      "field": "status",
      "operator": "EQUALS",
      "values": ["ENABLED"]
    },
    {
      "field": "countriesOrRegions",
      "operator": "CONTAINS_ANY",
      "values": ["US", "CA"]
    }
  ],
  "orderBy": [
    {
      "field": "modificationTime",
      "sortOrder": "DESCENDING"
    }
  ],
  "pagination": {
    "offset": 0,
    "limit": 100
  }
}
```

**Filterable Fields:**
- `id`: Campaign ID
- `name`: Campaign name
- `status`: ENABLED or PAUSED
- `countriesOrRegions`: Target countries
- `modificationTime`: Last modified date
- `servingStatus`: Serving status

**Response:**
```json
{
  "data": [
    {
      "id": 123456,
      "name": "Brand Campaign - US",
      "status": "ENABLED",
      ...
    },
    {
      "id": 123457,
      "name": "Category Campaign - US",
      "status": "ENABLED",
      ...
    }
  ],
  "pagination": {
    "totalResults": 2,
    "startIndex": 0,
    "itemsPerPage": 100
  },
  "error": null
}
```

### Get a Campaign

**Endpoint:** `GET /campaigns/{campaignId}`

**Description:** Retrieves a specific campaign by ID.

**Path Parameters:**
- `campaignId`: Campaign ID (integer)

**Response:** Same as Create Campaign response

### Update a Campaign

**Endpoint:** `PUT /campaigns/{campaignId}`

**Description:** Updates an existing campaign.

**Path Parameters:**
- `campaignId`: Campaign ID (integer)

**Request Body (Partial Update):**
```json
{
  "campaign": {
    "dailyBudgetAmount": {
      "amount": "75.00",
      "currency": "USD"
    },
    "status": "ENABLED"
  }
}
```

**Note:** Only include fields you want to update.

**Response:** Updated campaign object

### Delete a Campaign

**Endpoint:** `DELETE /campaigns/{campaignId}`

**Description:** Deletes a campaign.

**Path Parameters:**
- `campaignId`: Campaign ID (integer)

**Response:**
```json
{
  "data": null,
  "pagination": null,
  "error": null
}
```

---

## Ad Group Endpoints

### Create an Ad Group

**Endpoint:** `POST /campaigns/{campaignId}/adgroups`

**Description:** Creates a new ad group within a campaign.

**Path Parameters:**
- `campaignId`: Campaign ID (integer)

**Request Body:**
```json
{
  "name": "Brand - Exact Match",
  "cpaGoal": {
    "amount": "5.00",
    "currency": "USD"
  },
  "defaultBidAmount": {
    "amount": "1.50",
    "currency": "USD"
  },
  "startTime": "2026-03-12T00:00:00.000",
  "endTime": null,
  "status": "ENABLED",
  "targetingDimensions": {
    "age": {
      "included": [
        {"minAge": 18, "maxAge": 65}
      ]
    },
    "gender": {
      "included": ["M", "F"]
    },
    "deviceClass": {
      "included": ["IPHONE", "IPAD"]
    },
    "locality": {
      "included": [
        {"id": 1, "displayName": "United States"}
      ]
    },
    "adminArea": {
      "included": []
    },
    "country": {
      "included": ["US"]
    },
    "appDownloaders": {
      "included": ["NEW_USERS"],
      "excluded": []
    }
  },
  "automatedKeywordsOptIn": false
}
```

**Required Fields:**
- `name`: Ad group name
- `defaultBidAmount`: Default max CPT bid

**Optional Fields:**
- `cpaGoal`: Target CPA
- `startTime`: Start date/time (ISO 8601)
- `endTime`: End date/time (ISO 8601)
- `status`: ENABLED or PAUSED
- `targetingDimensions`: Targeting criteria
- `automatedKeywordsOptIn`: Enable Search Match (boolean)

**Targeting Dimensions:**

*Age:*
```json
"age": {
  "included": [{"minAge": 18, "maxAge": 65}]
}
```

*Gender:*
```json
"gender": {
  "included": ["M", "F"]  // M, F, or both
}
```

*Device Class:*
```json
"deviceClass": {
  "included": ["IPHONE", "IPAD"]
}
```

*App Downloaders (Customer Type):*
```json
"appDownloaders": {
  "included": ["NEW_USERS"],  // NEW_USERS, RETURNING_USERS, or ALL_USERS
  "excluded": []
}
```

*Location (Country):*
```json
"country": {
  "included": ["US", "CA"]
}
```

**Response:**
```json
{
  "data": {
    "id": 234567,
    "campaignId": 123456,
    "name": "Brand - Exact Match",
    "cpaGoal": {
      "amount": "5.00",
      "currency": "USD"
    },
    "defaultBidAmount": {
      "amount": "1.50",
      "currency": "USD"
    },
    "status": "ENABLED",
    "servingStatus": "RUNNING",
    "targetingDimensions": {...},
    "automatedKeywordsOptIn": false,
    "creationTime": "2026-03-12T10:00:00.000",
    "modificationTime": "2026-03-12T10:00:00.000"
  },
  "pagination": null,
  "error": null
}
```

### Find Ad Groups

**Endpoint:** `GET /campaigns/{campaignId}/adgroups`

**Description:** Retrieves ad groups for a campaign.

**Path Parameters:**
- `campaignId`: Campaign ID (integer)

**Query Parameters:**
- `limit`: Number of results per page
- `offset`: Starting index

**Note:** API 5.1+ only accepts EQUALS operator in selector

**Response:** Array of ad group objects

### Get an Ad Group

**Endpoint:** `GET /campaigns/{campaignId}/adgroups/{adGroupId}`

**Description:** Retrieves a specific ad group.

**Path Parameters:**
- `campaignId`: Campaign ID
- `adGroupId`: Ad group ID

**Response:** Ad group object

### Update an Ad Group

**Endpoint:** `PUT /campaigns/{campaignId}/adgroups/{adGroupId}`

**Description:** Updates an existing ad group.

**Request Body (Partial Update):**
```json
{
  "adGroup": {
    "defaultBidAmount": {
      "amount": "2.00",
      "currency": "USD"
    },
    "status": "ENABLED"
  }
}
```

**Response:** Updated ad group object

### Delete an Ad Group

**Endpoint:** `DELETE /campaigns/{campaignId}/adgroups/{adGroupId}`

**Description:** Deletes an ad group.

**Response:** Success confirmation

---

## Keyword Endpoints

### Create Targeting Keywords

**Endpoint:** `POST /campaigns/{campaignId}/adgroups/{adGroupId}/targetingkeywords/bulk`

**Description:** Creates multiple targeting keywords.

**Request Body:**
```json
[
  {
    "text": "fitness app",
    "matchType": "EXACT",
    "bidAmount": {
      "amount": "2.50",
      "currency": "USD"
    },
    "status": "ACTIVE"
  },
  {
    "text": "workout tracker",
    "matchType": "BROAD",
    "bidAmount": {
      "amount": "1.50",
      "currency": "USD"
    },
    "status": "ACTIVE"
  }
]
```

**Required Fields:**
- `text`: Keyword text
- `matchType`: EXACT or BROAD

**Optional Fields:**
- `bidAmount`: Keyword-specific bid (overrides ad group default)
- `status`: ACTIVE or PAUSED

**Response:**
```json
{
  "data": [
    {
      "id": 345678,
      "adGroupId": 234567,
      "text": "fitness app",
      "matchType": "EXACT",
      "bidAmount": {
        "amount": "2.50",
        "currency": "USD"
      },
      "status": "ACTIVE"
    },
    ...
  ],
  "error": null
}
```

### Find Targeting Keywords

**Endpoint:** `GET /campaigns/{campaignId}/adgroups/{adGroupId}/targetingkeywords`

**Description:** Retrieves targeting keywords for an ad group.

**Response:** Array of keyword objects

### Get a Targeting Keyword

**Endpoint:** `GET /campaigns/{campaignId}/adgroups/{adGroupId}/targetingkeywords/{keywordId}`

**Description:** Retrieves a specific keyword.

**Response:** Keyword object

### Update Targeting Keywords

**Endpoint:** `PUT /campaigns/{campaignId}/adgroups/{adGroupId}/targetingkeywords/bulk`

**Description:** Updates multiple keywords.

**Request Body:**
```json
[
  {
    "id": 345678,
    "bidAmount": {
      "amount": "3.00",
      "currency": "USD"
    },
    "status": "ACTIVE"
  }
]
```

**Response:** Updated keyword objects

---

## Negative Keyword Endpoints

### Create Campaign Negative Keywords

**Endpoint:** `POST /campaigns/{campaignId}/negativekeywords/bulk`

**Description:** Creates campaign-level negative keywords.

**Request Body:**
```json
[
  {
    "text": "free",
    "matchType": "EXACT",
    "status": "ACTIVE"
  },
  {
    "text": "android",
    "matchType": "BROAD",
    "status": "ACTIVE"
  }
]
```

**Response:** Created negative keyword objects

### Create Ad Group Negative Keywords

**Endpoint:** `POST /campaigns/{campaignId}/adgroups/{adGroupId}/negativekeywords/bulk`

**Description:** Creates ad group-level negative keywords.

**Request Body:** Same as campaign negative keywords

**Response:** Created negative keyword objects

---

## Reporting Endpoints

### Get Campaign-Level Reports

**Endpoint:** `POST /reports/campaigns`

**Description:** Generates campaign performance report.

**Request Body:**
```json
{
  "startTime": "2026-03-01",
  "endTime": "2026-03-12",
  "granularity": "DAILY",
  "selector": {
    "conditions": [
      {
        "field": "campaignId",
        "operator": "IN",
        "values": ["123456", "123457"]
      }
    ],
    "orderBy": [
      {
        "field": "localSpend",
        "sortOrder": "DESCENDING"
      }
    ],
    "pagination": {
      "offset": 0,
      "limit": 1000
    }
  },
  "groupBy": ["countryOrRegion"],
  "returnRowTotals": true,
  "returnRecordsWithNoMetrics": false
}
```

**Required Fields:**
- `startTime`: Start date (YYYY-MM-DD)
- `endTime`: End date (YYYY-MM-DD)

**Optional Fields:**
- `granularity`: HOURLY, DAILY, MONTHLY, or TOTAL (default: DAILY)
- `selector`: Filtering and pagination
- `groupBy`: Dimension grouping
- `returnRowTotals`: Include totals (boolean)
- `returnRecordsWithNoMetrics`: Include zero rows (boolean)

**Granularity Options:**
- `HOURLY`: Hourly breakdown
- `DAILY`: Daily breakdown
- `MONTHLY`: Monthly breakdown
- `TOTAL`: Single total row

**Group By Dimensions:**
- `countryOrRegion`: Group by country
- `adminArea`: Group by state/region
- `locality`: Group by city
- `deviceClass`: Group by device (iPhone/iPad)
- `ageRange`: Group by age range
- `gender`: Group by gender

**Response:**
```json
{
  "data": {
    "reportingDataResponse": {
      "row": [
        {
          "metadata": {
            "campaignId": 123456,
            "campaignName": "Brand Campaign - US",
            "date": "2026-03-12"
          },
          "total": {
            "impressions": 10000,
            "taps": 500,
            "installs": 100,
            "newDownloads": 80,
            "redownloads": 20,
            "ttr": 0.05,
            "conversionRate": 0.20,
            "avgCPT": {
              "amount": "1.50",
              "currency": "USD"
            },
            "avgCPA": {
              "amount": "7.50",
              "currency": "USD"
            },
            "localSpend": {
              "amount": "750.00",
              "currency": "USD"
            }
          },
          "insights": {
            "bidRecommendation": {
              "bidMin": {"amount": "1.00", "currency": "USD"},
              "bidMax": {"amount": "2.00", "currency": "USD"}
            }
          }
        }
      ],
      "grandTotals": {
        "impressions": 10000,
        "taps": 500,
        "installs": 100,
        ...
      }
    }
  },
  "pagination": {
    "totalResults": 1,
    "startIndex": 0,
    "itemsPerPage": 1
  },
  "error": null
}
```

**Available Metrics:**

*Standard Metrics:*
- `impressions`: Ad views
- `taps`: Ad clicks
- `installs`: Total installs
- `newDownloads`: First-time installs
- `redownloads`: Re-installs
- `latOnInstalls`: Installs with LAT on
- `latOffInstalls`: Installs with LAT off
- `ttr`: Tap-through rate
- `conversionRate`: Install rate
- `avgCPT`: Average cost per tap
- `avgCPA`: Average cost per acquisition
- `localSpend`: Total spend

*View-Through Metrics (API 5.0+):*
- `viewInstalls`: Installs from views
- `viewNewDownloads`: New downloads from views
- `viewRedownloads`: Redownloads from views

*Preorder Metrics (API 5.4+):*
- `tapPreOrdersPlaced`: Preorders from taps
- `viewPreOrdersPlaced`: Preorders from views
- `totalPreOrdersPlaced`: Total preorders

### Get Ad Group-Level Reports

**Endpoint:** `POST /reports/campaigns/{campaignId}/adgroups`

**Description:** Generates ad group performance report.

**Request Body:** Same structure as campaign report

**Response:** Similar to campaign report with ad group metadata

### Get Keyword-Level Reports

**Endpoint:** `POST /reports/campaigns/{campaignId}/keywords`

**Description:** Generates keyword performance report.

**Request Body:** Same structure as campaign report

**Response:**
```json
{
  "data": {
    "reportingDataResponse": {
      "row": [
        {
          "metadata": {
            "campaignId": 123456,
            "adGroupId": 234567,
            "keywordId": 345678,
            "keyword": "fitness app",
            "matchType": "EXACT",
            "date": "2026-03-12"
          },
          "total": {
            "impressions": 1000,
            "taps": 50,
            "installs": 10,
            "avgCPA": {"amount": "5.00", "currency": "USD"},
            ...
          },
          "insights": {
            "bidRecommendation": {
              "suggestedBidAmount": {"amount": "2.00", "currency": "USD"}
            }
          }
        }
      ]
    }
  }
}
```

**Note:** API 5.0+ includes `suggestedBidAmount` instead of `bidMin`/`bidMax`

### Get Search Term-Level Reports

**Endpoint:** `POST /reports/campaigns/{campaignId}/searchterms`

**Description:** Generates search term performance report.

**Request Body:**
```json
{
  "startTime": "2026-03-01T00:00:00.000",
  "endTime": "2026-03-12T23:59:59.999",
  "timeZone": "America/New_York",
  "granularity": "DAILY",
  "selector": {
    "pagination": {
      "offset": 0,
      "limit": 1000
    }
  },
  "returnRowTotals": true
}
```

**Required Fields (API 5.0+):**
- `startTime`: Start datetime with timezone
- `endTime`: End datetime with timezone
- `timeZone`: IANA timezone (e.g., "America/New_York")

**Response:**
```json
{
  "data": {
    "reportingDataResponse": {
      "row": [
        {
          "metadata": {
            "campaignId": 123456,
            "adGroupId": 234567,
            "keywordId": 345678,
            "keyword": "fitness app",
            "searchTermText": "best fitness app",
            "searchTermSource": "TARGETED",
            "date": "2026-03-12"
          },
          "total": {
            "impressions": 100,
            "taps": 5,
            "installs": 1,
            "avgCPA": {"amount": "5.00", "currency": "USD"},
            ...
          }
        }
      ]
    }
  }
}
```

**Search Term Source:**
- `TARGETED`: From exact or broad match keyword
- `AUTO`: From Search Match

---

## App Information Endpoints

### Get App Details

**Endpoint:** `GET /apps/{adamId}`

**Description:** Retrieves app information by Adam ID (API 5.2+).

**Path Parameters:**
- `adamId`: App Store app ID

**Response:**
```json
{
  "data": {
    "adamId": 123456789,
    "appName": "My Fitness App",
    "developerName": "My Company",
    "primaryCategory": "Health & Fitness",
    "supportedDevices": ["IPHONE", "IPAD"],
    "supportedCountries": ["US", "CA", "GB", ...]
  }
}
```

### Get Localized App Details

**Endpoint:** `GET /apps/{adamId}/localized`

**Description:** Retrieves localized app information (API 5.2+).

**Query Parameters:**
- `locale`: Locale code (e.g., "en_US")

**Response:**
```json
{
  "data": {
    "adamId": 123456789,
    "locale": "en_US",
    "appName": "My Fitness App",
    "description": "Track your fitness...",
    "subtitle": "Workout & Calorie Tracker"
  }
}
```

---

## Budget Order Endpoints

### Get Budget Order

**Endpoint:** `GET /budgetorders/{budgetOrderId}`

**Description:** Retrieves budget order details.

**Response:**
```json
{
  "data": {
    "id": 456789,
    "name": "Q1 2026 Budget",
    "budget": {"amount": "10000.00", "currency": "USD"},
    "spent": {"amount": "2500.00", "currency": "USD"},
    "status": "ACTIVE"
  }
}
```

---

## Geo Location Endpoints

### Search Geo Locations

**Endpoint:** `GET /search/geo`

**Description:** Searches for geographic targeting options.

**Query Parameters:**
- `query`: Search query (e.g., "New York")
- `entity`: GEO_COUNTRY, GEO_ADMIN_AREA, or GEO_LOCALITY
- `countryCode`: Filter by country (e.g., "US")

**Response:**
```json
{
  "data": [
    {
      "id": 1001,
      "entity": "GEO_LOCALITY",
      "displayName": "New York, NY",
      "countryCode": "US"
    }
  ]
}
```

---

## Error Responses

### Common Error Codes

**400 Bad Request:**
```json
{
  "error": {
    "errors": [
      {
        "messageCode": "INVALID_PARAMETER",
        "message": "The dailyBudgetAmount field is required",
        "field": "dailyBudgetAmount"
      }
    ]
  }
}
```

**401 Unauthorized:**
```json
{
  "error": {
    "errors": [
      {
        "messageCode": "UNAUTHORIZED",
        "message": "Invalid authentication credentials"
      }
    ]
  }
}
```

**404 Not Found:**
```json
{
  "error": {
    "errors": [
      {
        "messageCode": "NOT_FOUND",
        "message": "Campaign not found",
        "field": "campaignId"
      }
    ]
  }
}
```

**429 Too Many Requests:**
```json
{
  "error": {
    "errors": [
      {
        "messageCode": "RATE_LIMIT_EXCEEDED",
        "message": "Too many requests. Please retry after some time."
      }
    ]
  }
}
```

---

## Rate Limiting

Apple Search Ads API implements rate limiting to ensure fair usage:

- **Limit:** Not publicly documented (varies by endpoint)
- **Response:** HTTP 429 when limit exceeded
- **Best Practice:** Implement exponential backoff
- **Recommendation:** Batch operations when possible

**Exponential Backoff Example:**
```python
import time

def api_call_with_backoff(func, max_retries=5):
    for attempt in range(max_retries):
        try:
            return func()
        except RateLimitError:
            if attempt == max_retries - 1:
                raise
            wait_time = 2 ** attempt
            time.sleep(wait_time)
```