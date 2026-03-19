# Meta Ads Insights and Reporting API

This comprehensive guide covers the Meta Ads Insights API, which provides access to performance data, analytics, and reporting capabilities for Meta advertising campaigns.

## Overview of Insights API

The Meta Ads Insights API is a critical component for performance marketers, providing programmatic access to advertising performance data across Facebook, Instagram, Messenger, and WhatsApp.

### Purpose and Capabilities

**Primary Functions**
- Access performance metrics and KPIs
- Generate custom reports
- Analyze campaign effectiveness
- Track conversions and ROI
- Monitor ad delivery and engagement
- Compare performance across campaigns

**Data Availability**
- Over 70 performance metrics
- Multiple attribution windows
- Granular breakdowns by dimensions
- Historical data access
- Real-time and aggregated data

### API Structure

The Insights API follows the Graph API structure with specific endpoints for different object levels.

**Endpoint Format**
```
GET /{object_id}/insights
```

**Object Levels**
- Ad Account: `/act_{AD_ACCOUNT_ID}/insights`
- Campaign: `/{CAMPAIGN_ID}/insights`
- Ad Set: `/{AD_SET_ID}/insights`
- Ad: `/{AD_ID}/insights`

## Core Metrics and Fields

### Delivery Metrics

**Impressions**
- Field: `impressions`
- Definition: Number of times ads were displayed
- Use: Measure reach and visibility
- Type: Integer

**Reach**
- Field: `reach`
- Definition: Number of unique people who saw ads
- Use: Measure audience size
- Type: Integer

**Frequency**
- Field: `frequency`
- Definition: Average number of times each person saw ads
- Calculation: Impressions / Reach
- Use: Monitor ad fatigue
- Type: Float

**Spend**
- Field: `spend`
- Definition: Total amount spent
- Currency: Account currency
- Type: String (formatted as decimal)

### Engagement Metrics

**Clicks**
- Field: `clicks`
- Definition: Total number of clicks
- Includes: All click types
- Type: Integer

**Link Clicks**
- Field: `inline_link_clicks`
- Definition: Clicks on links to destinations
- Excludes: Social actions, reactions
- Type: Integer

**Click-Through Rate (CTR)**
- Field: `ctr`
- Definition: (Clicks / Impressions) × 100
- Format: Percentage
- Type: String

**Link Click-Through Rate**
- Field: `inline_link_click_ctr`
- Definition: (Link Clicks / Impressions) × 100
- Format: Percentage
- Type: String

**Social Actions**
- Likes: `actions` (action_type: "like")
- Comments: `actions` (action_type: "comment")
- Shares: `actions` (action_type: "post")
- Page Likes: `actions` (action_type: "page_engagement")

### Cost Metrics

**Cost Per Click (CPC)**
- Field: `cpc`
- Definition: Spend / Clicks
- Currency: Account currency
- Type: String

**Cost Per Mille (CPM)**
- Field: `cpm`
- Definition: (Spend / Impressions) × 1000
- Currency: Account currency
- Type: String

**Cost Per Link Click**
- Field: `cost_per_inline_link_click`
- Definition: Spend / Link Clicks
- Currency: Account currency
- Type: String

**Cost Per Action**
- Field: `cost_per_action_type`
- Definition: Spend / Actions (by type)
- Breakdown: By action type
- Type: Array of objects

### Conversion Metrics

**Conversions**
- Field: `conversions`
- Definition: Number of conversion events
- Breakdown: By conversion type
- Type: Array of objects

**Conversion Value**
- Field: `conversion_values`
- Definition: Total value of conversions
- Currency: Account currency
- Type: Array of objects

**Purchase ROAS (Return on Ad Spend)**
- Field: `purchase_roas`
- Definition: Conversion Value / Spend
- Format: Ratio
- Type: Array of objects

**Website Purchases**
- Field: `actions` (action_type: "offsite_conversion.fb_pixel_purchase")
- Definition: Purchase events tracked via pixel
- Type: Integer

**Lead Generation**
- Field: `actions` (action_type: "lead")
- Definition: Lead form submissions
- Type: Integer

### Video Metrics

**Video Views**
- Field: `video_views`
- Definition: Number of video views
- Threshold: 3 seconds or more
- Type: Integer

**Video View Rate**
- Field: `video_view_rate`
- Definition: Video Views / Impressions
- Format: Percentage
- Type: String

**ThruPlay**
- Field: `video_thruplay_watched_actions`
- Definition: Videos watched to completion or 15 seconds
- Type: Array of objects

**Video Completion Rates**
- 25% viewed: `video_p25_watched_actions`
- 50% viewed: `video_p50_watched_actions`
- 75% viewed: `video_p75_watched_actions`
- 95% viewed: `video_p95_watched_actions`
- 100% viewed: `video_p100_watched_actions`

**Average Video Watch Time**
- Field: `video_avg_time_watched_actions`
- Definition: Average time spent watching
- Unit: Milliseconds
- Type: Array of objects

### Quality and Relevance Metrics

**Quality Ranking**
- Field: `quality_ranking`
- Values: ABOVE_AVERAGE, AVERAGE, BELOW_AVERAGE
- Definition: Perceived quality compared to competing ads

**Engagement Rate Ranking**
- Field: `engagement_rate_ranking`
- Values: ABOVE_AVERAGE, AVERAGE, BELOW_AVERAGE
- Definition: Expected engagement compared to competing ads

**Conversion Rate Ranking**
- Field: `conversion_rate_ranking`
- Values: ABOVE_AVERAGE, AVERAGE, BELOW_AVERAGE
- Definition: Expected conversion rate compared to competing ads

## Making Insights API Requests

### Basic Request Structure

**Endpoint**
```
GET https://graph.facebook.com/v18.0/{object_id}/insights
  ?fields={fields}
  &date_preset={date_preset}
  &access_token={access_token}
```

**Required Parameters**
- `access_token`: Valid access token with ads_read permission

**Common Parameters**
- `fields`: Comma-separated list of metrics
- `date_preset`: Predefined date range
- `time_range`: Custom date range
- `level`: Aggregation level (account, campaign, adset, ad)
- `breakdowns`: Dimensions for data segmentation
- `filtering`: Filter criteria
- `time_increment`: Time granularity

### Example Requests

**Basic Campaign Insights**
```bash
curl -X GET \
  "https://graph.facebook.com/v18.0/123456789/insights" \
  -d "fields=impressions,reach,spend,clicks,ctr" \
  -d "date_preset=last_30d" \
  -d "access_token=YOUR_ACCESS_TOKEN"
```

**Ad Account Insights with Breakdown**
```bash
curl -X GET \
  "https://graph.facebook.com/v18.0/act_123456789/insights" \
  -d "fields=impressions,spend,actions,cost_per_action_type" \
  -d "date_preset=last_7d" \
  -d "level=campaign" \
  -d "breakdowns=age,gender" \
  -d "access_token=YOUR_ACCESS_TOKEN"
```

**Conversion Tracking**
```bash
curl -X GET \
  "https://graph.facebook.com/v18.0/123456789/insights" \
  -d "fields=spend,actions,conversions,conversion_values,purchase_roas" \
  -d "date_preset=last_30d" \
  -d "action_attribution_windows=['7d_click','1d_view']" \
  -d "access_token=YOUR_ACCESS_TOKEN"
```

## Date Ranges and Time Increments

### Date Presets

Predefined date ranges for common reporting periods.

**Available Presets**
- `today`: Current day
- `yesterday`: Previous day
- `this_week_sun_today`: Sunday to today
- `this_week_mon_today`: Monday to today
- `last_week_sun_sat`: Previous week (Sunday-Saturday)
- `last_week_mon_sun`: Previous week (Monday-Sunday)
- `last_7d`: Last 7 days
- `last_14d`: Last 14 days
- `last_28d`: Last 28 days
- `last_30d`: Last 30 days
- `last_90d`: Last 90 days
- `this_month`: Current month to date
- `last_month`: Previous month
- `this_quarter`: Current quarter to date
- `last_3d`: Last 3 days
- `lifetime`: All time

**Example**
```
date_preset=last_30d
```

### Custom Time Ranges

**Format**
```json
{
  "time_range": {
    "since": "2024-01-01",
    "until": "2024-01-31"
  }
}
```

**Date Format**
- Format: YYYY-MM-DD
- Timezone: Account timezone
- Inclusive: Both since and until dates included

**Example**
```bash
curl -X GET \
  "https://graph.facebook.com/v18.0/123456789/insights" \
  -d "fields=impressions,spend" \
  -d "time_range={'since':'2024-01-01','until':'2024-01-31'}" \
  -d "access_token=YOUR_ACCESS_TOKEN"
```

### Time Increments

Break down data by time periods.

**Available Increments**
- `1`: Daily (1 day)
- `7`: Weekly (7 days)
- `14`: Bi-weekly (14 days)
- `28`: 4-week periods
- `monthly`: Calendar months
- `all_days`: No time breakdown (default)

**Example**
```
time_increment=1
```

**Response Structure**
```json
{
  "data": [
    {
      "date_start": "2024-01-01",
      "date_stop": "2024-01-01",
      "impressions": "10000",
      "spend": "100.00"
    },
    {
      "date_start": "2024-01-02",
      "date_stop": "2024-01-02",
      "impressions": "12000",
      "spend": "120.00"
    }
  ]
}
```

## Breakdowns and Dimensions

Breakdowns segment data by specific dimensions.

### Available Breakdowns

**Demographic Breakdowns**
- `age`: Age ranges (18-24, 25-34, 35-44, 45-54, 55-64, 65+)
- `gender`: Male, Female, Unknown
- `country`: Country codes
- `region`: Geographic regions
- `dma`: Designated Market Areas (US)

**Placement Breakdowns**
- `publisher_platform`: Facebook, Instagram, Audience Network, Messenger
- `platform_position`: Feed, Story, Right Column, etc.
- `device_platform`: Mobile, Desktop, Unknown
- `impression_device`: iPhone, Android, iPad, Desktop, etc.

**Time Breakdowns**
- `hourly_stats_aggregated_by_advertiser_time_zone`: Hourly data
- `hourly_stats_aggregated_by_audience_time_zone`: Hourly by audience timezone

**Product Breakdowns** (for Dynamic Ads)
- `product_id`: Individual product IDs

**Example with Multiple Breakdowns**
```bash
curl -X GET \
  "https://graph.facebook.com/v18.0/123456789/insights" \
  -d "fields=impressions,spend,actions" \
  -d "date_preset=last_7d" \
  -d "breakdowns=age,gender,publisher_platform" \
  -d "access_token=YOUR_ACCESS_TOKEN"
```

### Breakdown Limitations

**Considerations**
- Each breakdown multiplies number of result rows
- More breakdowns = larger response size
- May impact API performance
- Some breakdowns cannot be combined
- Rate limits apply to data volume

**Best Practices**
- Request only necessary breakdowns
- Use filtering to reduce data volume
- Consider pagination for large datasets
- Cache results when appropriate

## Attribution Windows

Attribution windows define how conversions are counted relative to ad interactions.

### Click Attribution Windows

**Available Windows**
- `1d_click`: 1 day after click
- `7d_click`: 7 days after click (default)
- `28d_click`: 28 days after click

**Definition**
- Conversions occurring within X days of clicking ad
- Most common for direct response campaigns

### View Attribution Windows

**Available Windows**
- `1d_view`: 1 day after impression
- `7d_view`: 7 days after impression
- `28d_view`: 28 days after impression

**Definition**
- Conversions occurring within X days of viewing ad
- Useful for brand awareness impact

### Specifying Attribution Windows

**Parameter**
```
action_attribution_windows=['7d_click','1d_view']
```

**Example**
```bash
curl -X GET \
  "https://graph.facebook.com/v18.0/123456789/insights" \
  -d "fields=actions,conversions,purchase_roas" \
  -d "date_preset=last_30d" \
  -d "action_attribution_windows=['7d_click','1d_view']" \
  -d "access_token=YOUR_ACCESS_TOKEN"
```

### Choosing Attribution Windows

**Considerations**
- Sales cycle length
- Industry standards
- Campaign objectives
- Historical conversion patterns

**Recommendations**
- **Short sales cycle** (e-commerce): 1d_click, 7d_click
- **Medium sales cycle** (B2B): 7d_click, 28d_click
- **Long sales cycle** (enterprise): 28d_click
- **Brand awareness**: Include view windows

## Filtering and Sorting

### Filtering Results

**Filter Structure**
```json
[
  {
    "field": "field_name",
    "operator": "EQUAL|NOT_EQUAL|GREATER_THAN|LESS_THAN|IN|NOT_IN|CONTAIN|NOT_CONTAIN",
    "value": "filter_value"
  }
]
```

**Example: Filter by Campaign Status**
```bash
curl -X GET \
  "https://graph.facebook.com/v18.0/act_123456789/insights" \
  -d "fields=campaign_name,impressions,spend" \
  -d "level=campaign" \
  -d "filtering=[{\"field\":\"campaign.effective_status\",\"operator\":\"IN\",\"value\":[\"ACTIVE\"]}]" \
  -d "date_preset=last_7d" \
  -d "access_token=YOUR_ACCESS_TOKEN"
```

**Example: Filter by Spend**
```json
[
  {
    "field": "spend",
    "operator": "GREATER_THAN",
    "value": 100
  }
]
```

### Sorting Results

**Parameter**
```
sort={field}_{direction}
```

**Directions**
- `ascending`: Low to high
- `descending`: High to low

**Example**
```
sort=spend_descending
```

**Full Request**
```bash
curl -X GET \
  "https://graph.facebook.com/v18.0/act_123456789/insights" \
  -d "fields=campaign_name,spend,conversions" \
  -d "level=campaign" \
  -d "date_preset=last_30d" \
  -d "sort=spend_descending" \
  -d "access_token=YOUR_ACCESS_TOKEN"
```

## Pagination

Large datasets are returned in pages.

### Pagination Structure

**Response Format**
```json
{
  "data": [
    // Results
  ],
  "paging": {
    "cursors": {
      "before": "cursor_string",
      "after": "cursor_string"
    },
    "next": "https://graph.facebook.com/v18.0/.../insights?after=cursor_string",
    "previous": "https://graph.facebook.com/v18.0/.../insights?before=cursor_string"
  }
}
```

### Navigating Pages

**Next Page**
- Use `next` URL from paging object
- Or add `after` cursor to original request

**Previous Page**
- Use `previous` URL from paging object
- Or add `before` cursor to original request

**Example Implementation (Python)**
```python
import requests

def get_all_insights(url, access_token):
    all_data = []
    
    while url:
        response = requests.get(url, params={'access_token': access_token})
        data = response.json()
        
        all_data.extend(data.get('data', []))
        
        # Get next page URL
        url = data.get('paging', {}).get('next')
    
    return all_data
```

### Limit Parameter

**Control Page Size**
```
limit=100
```

**Default**: 25
**Maximum**: 100 (for most endpoints)

**Example**
```bash
curl -X GET \
  "https://graph.facebook.com/v18.0/act_123456789/insights" \
  -d "fields=campaign_name,impressions" \
  -d "level=campaign" \
  -d "limit=100" \
  -d "access_token=YOUR_ACCESS_TOKEN"
```

## Asynchronous Insights Requests

For large data requests, use asynchronous reporting.

### When to Use Async

**Scenarios**
- Large date ranges
- Multiple breakdowns
- Account-level reports with many campaigns
- Avoiding timeouts
- Batch reporting

### Async Request Process

**Step 1: Initiate Async Request**
```bash
curl -X POST \
  "https://graph.facebook.com/v18.0/act_123456789/insights" \
  -d "fields=impressions,spend,actions" \
  -d "date_preset=last_90d" \
  -d "level=campaign" \
  -d "breakdowns=age,gender" \
  -d "async=true" \
  -d "access_token=YOUR_ACCESS_TOKEN"
```

**Response**
```json
{
  "report_run_id": "123456789"
}
```

**Step 2: Check Report Status**
```bash
curl -X GET \
  "https://graph.facebook.com/v18.0/123456789" \
  -d "fields=async_status,async_percent_completion" \
  -d "access_token=YOUR_ACCESS_TOKEN"
```

**Status Values**
- `Job Not Started`
- `Job Started`
- `Job Running`
- `Job Completed`
- `Job Failed`
- `Job Skipped`

**Step 3: Retrieve Results**
```bash
curl -X GET \
  "https://graph.facebook.com/v18.0/123456789/insights" \
  -d "access_token=YOUR_ACCESS_TOKEN"
```

### Polling Best Practices

**Polling Interval**
- Start with 5-10 second intervals
- Increase interval if job takes longer
- Implement exponential backoff

**Timeout Handling**
- Set maximum wait time
- Implement retry logic
- Handle failed jobs gracefully

**Example Polling Logic (Python)**
```python
import time
import requests

def wait_for_async_report(report_run_id, access_token, max_wait=300):
    url = f"https://graph.facebook.com/v18.0/{report_run_id}"
    params = {
        'fields': 'async_status,async_percent_completion',
        'access_token': access_token
    }
    
    start_time = time.time()
    
    while time.time() - start_time < max_wait:
        response = requests.get(url, params=params)
        data = response.json()
        
        status = data.get('async_status')
        
        if status == 'Job Completed':
            return True
        elif status == 'Job Failed':
            return False
        
        time.sleep(5)
    
    return False  # Timeout
```

## Best Practices for Insights API

### Request Optimization

**Request Only Needed Fields**
- Specify exact fields required
- Reduces response size
- Faster processing
- Better rate limit usage

**Use Appropriate Date Ranges**
- Don't request more data than needed
- Consider data freshness requirements
- Balance between detail and performance

**Implement Caching**
- Cache frequently accessed data
- Set appropriate cache expiration
- Reduce redundant API calls
- Improve application performance

### Error Handling

**Common Errors**
- Rate limit exceeded (Error 17, 32)
- Invalid access token (Error 190)
- Insufficient permissions (Error 200)
- Invalid parameters (Error 100)

**Retry Logic**
- Implement exponential backoff
- Respect rate limit headers
- Maximum retry attempts
- Log errors for debugging

**Example Error Handling (Python)**
```python
import time
import requests

def get_insights_with_retry(url, params, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 429:  # Rate limit
                wait_time = 2 ** attempt  # Exponential backoff
                time.sleep(wait_time)
            else:
                raise
    
    raise Exception("Max retries exceeded")
```

### Data Processing

**Handle Missing Data**
- Some metrics may not be available for all objects
- Check for field existence before accessing
- Provide default values
- Document data limitations

**Aggregate Carefully**
- Understand metric calculation methods
- Some metrics cannot be summed (e.g., CTR, frequency)
- Use weighted averages where appropriate
- Validate aggregated results

**Time Zone Considerations**
- Data returned in account time zone
- Be consistent with time zone usage
- Document time zone in reports
- Consider audience time zones for analysis

## Integration with BI Tools

### Data Export

**CSV Export**
- Process API response
- Convert to CSV format
- Schedule regular exports
- Automate data pipeline

**Database Integration**
- Store insights data in database
- Enable historical analysis
- Support complex queries
- Power BI dashboards

### Visualization Platforms

**Supported Platforms**
- Tableau
- Power BI
- Looker
- Google Data Studio
- Custom dashboards

**Integration Methods**
- Direct API connection
- Third-party connectors
- Scheduled data exports
- Real-time data streaming

### Automated Reporting

**Report Scheduling**
- Daily performance summaries
- Weekly trend reports
- Monthly executive dashboards
- Custom alert triggers

**Delivery Methods**
- Email reports
- Slack notifications
- Dashboard updates
- API webhooks

## Conclusion

The Meta Ads Insights API provides comprehensive access to advertising performance data, enabling sophisticated analysis, reporting, and optimization. By understanding the available metrics, properly structuring requests, implementing best practices for pagination and error handling, and integrating with business intelligence tools, advertisers can build powerful analytics solutions that drive data-driven decision making and campaign optimization. The key is to balance data granularity with performance, implement robust error handling, and create scalable data pipelines that support business objectives.