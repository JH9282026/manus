# Instagram Ads Insights API and Reporting

## Overview

The Instagram Ads Insights API is a powerful component of Meta's Marketing API that enables programmatic access to comprehensive performance data for Instagram advertising campaigns. This API allows developers and marketers to extract, analyze, and report on ad performance at any level of the campaign hierarchy, providing the foundation for data-driven optimization and custom reporting solutions.

## Insights API Fundamentals

### What is the Insights API?

The Ads Insights API is the reporting interface within Meta's Marketing API that provides access to performance metrics and analytics for Instagram (and Facebook) advertising campaigns. It enables:

- **Programmatic Data Access**: Retrieve performance data via API calls
- **Custom Reporting**: Build tailored reports beyond Ads Manager capabilities
- **Real-Time Analytics**: Access near real-time performance data
- **Historical Analysis**: Pull data up to 37 months back
- **Automated Optimization**: Feed data into custom optimization systems
- **Multi-Account Reporting**: Consolidate data across multiple ad accounts

### API Hierarchy and Scope

Insights can be retrieved at multiple levels of the campaign hierarchy:

1. **Ad Account Level**: Overall account performance
2. **Campaign Level**: Performance by campaign
3. **Ad Set Level**: Performance by ad set
4. **Ad Level**: Individual ad performance

**Flexibility**: Query at any level to get aggregated or granular data as needed.

## Core Capabilities

### 1. Performance Metrics

The Insights API provides access to over 70 performance metrics, including:

#### Reach and Impressions
- **Reach**: Unique users who saw ads
- **Impressions**: Total number of times ads were displayed
- **Frequency**: Average number of times each user saw ads

#### Engagement Metrics
- **Likes**: Post likes
- **Comments**: Post comments
- **Shares**: Content shares
- **Saves**: Content saves
- **Clicks**: Link clicks, CTA clicks
- **Video Views**: 3-second, 10-second, ThruPlay views
- **Video Percentage Watched**: 25%, 50%, 75%, 95%, 100%

#### Conversion Metrics
- **Conversions**: Total conversions by type
- **Conversion Value**: Revenue from conversions
- **Cost Per Conversion**: Average cost per conversion
- **Conversion Rate**: Percentage of clicks that convert

#### Financial Metrics
- **Spend**: Total amount spent
- **CPM (Cost Per Mille)**: Cost per 1,000 impressions
- **CPC (Cost Per Click)**: Cost per link click
- **CPA (Cost Per Acquisition)**: Cost per conversion
- **ROAS (Return on Ad Spend)**: Revenue / Spend

#### Audience Metrics
- **Demographics**: Age, gender distribution
- **Geographic**: Country, region, city performance
- **Device**: Mobile, desktop, tablet breakdown
- **Placement**: Performance by placement (Feed, Stories, Reels, Explore)

### 2. Custom Date Ranges

The Insights API allows flexible date range specifications:

**Date Range Options**:
- **Preset Ranges**: Today, yesterday, last 7 days, last 30 days, this month, last month
- **Custom Ranges**: Specify exact start and end dates
- **Historical Data**: Access data up to 37 months back
- **Real-Time**: Near real-time data (typically 15-30 minute delay)

**Date Range Parameters**:
```
time_range: {
  since: 'YYYY-MM-DD',
  until: 'YYYY-MM-DD'
}
```

**Best Practices**:
- Use appropriate date ranges for analysis type
- Consider attribution windows when analyzing conversions
- Account for time zone differences
- Be aware of data freshness delays

### 3. Time Increments

Break down performance data by time periods:

**Available Increments**:
- **Daily**: Day-by-day performance
- **Weekly**: Week-by-week aggregation
- **Monthly**: Month-by-month summary
- **All Time**: Total aggregated performance

**Use Cases**:
- **Daily**: Identify day-of-week patterns, detect anomalies
- **Weekly**: Smooth out daily volatility, track weekly trends
- **Monthly**: Long-term trend analysis, monthly reporting
- **All Time**: Overall campaign performance summary

**Parameter**:
```
time_increment: 1  // Daily
time_increment: 7  // Weekly
time_increment: 'monthly'  // Monthly
time_increment: 'all_days'  // All time
```

### 4. Breakdowns

Segment performance data by various dimensions:

#### Demographic Breakdowns
- **Age**: Performance by age group
- **Gender**: Performance by gender
- **Age and Gender**: Combined demographic breakdown

#### Geographic Breakdowns
- **Country**: Performance by country
- **Region**: Performance by state/province
- **DMA (Designated Market Area)**: US metro areas
- **City**: City-level performance

#### Placement Breakdowns
- **Platform**: Instagram vs. Facebook
- **Placement**: Feed, Stories, Reels, Explore, Search
- **Device Platform**: Mobile, desktop, tablet
- **Publisher Platform**: Instagram, Facebook, Audience Network, Messenger

#### Time Breakdowns
- **Hourly**: Performance by hour of day
- **Day of Week**: Performance by day

#### Other Breakdowns
- **Product ID**: For catalog/DPA campaigns
- **Conversion Device**: Device where conversion occurred
- **Impression Device**: Device where ad was seen

**Parameter**:
```
breakdowns: ['age', 'gender', 'country', 'placement']
```

**Limitations**:
- Not all breakdowns can be combined
- Some breakdowns increase API response time
- Certain breakdowns require minimum data thresholds

## API Request Structure

### Basic Request Format

Insights API requests follow this general structure:

```
GET /{ad-object-id}/insights
  ?fields={fields}
  &time_range={time_range}
  &time_increment={time_increment}
  &breakdowns={breakdowns}
  &level={level}
  &access_token={access_token}
```

### Request Parameters

#### Required Parameters
- **access_token**: OAuth access token for authentication

#### Optional Parameters
- **fields**: Comma-separated list of metrics to retrieve
- **time_range**: Date range for data retrieval
- **time_increment**: Time period granularity
- **breakdowns**: Dimensions for data segmentation
- **level**: Hierarchy level (account, campaign, adset, ad)
- **filtering**: Filter results by specific criteria
- **sort**: Sort results by specific field
- **limit**: Number of results per page

### Field Selection

**Requesting Specific Fields**:
```
fields=impressions,clicks,spend,reach,cpm,cpc,ctr
```

**Benefits of Field Selection**:
- Reduces API response size
- Faster response times
- Lower rate limit consumption
- More efficient data processing

**Best Practice**: Request only the fields you need to minimize API load and improve performance.

### Filtering Results

Filter insights data based on specific criteria:

**Filter Structure**:
```
filtering=[
  {
    "field": "campaign.name",
    "operator": "CONTAIN",
    "value": "Holiday"
  }
]
```

**Available Operators**:
- `EQUAL`
- `NOT_EQUAL`
- `GREATER_THAN`
- `LESS_THAN`
- `IN`
- `NOT_IN`
- `CONTAIN`
- `NOT_CONTAIN`

**Use Cases**:
- Filter by campaign name patterns
- Exclude specific ad sets
- Focus on high-spend campaigns
- Analyze specific time periods

## Asynchronous Reporting

### Why Asynchronous Requests?

For large data sets or complex queries, synchronous API calls may timeout. Asynchronous reporting solves this:

**Benefits**:
- Handle large data volumes
- Avoid timeout errors
- Process complex breakdowns
- Retrieve historical data efficiently

### Asynchronous Request Flow

1. **Initiate Report**:
   ```
   POST /{ad-account-id}/insights
   ```
   Returns: `report_run_id`

2. **Check Status**:
   ```
   GET /{report-run-id}
   ```
   Returns: Status (Job Running, Job Completed, Job Failed)

3. **Retrieve Results**:
   ```
   GET /{report-run-id}/insights
   ```
   Returns: Insights data when job completed

### Polling Best Practices

- **Initial Delay**: Wait 5-10 seconds before first status check
- **Polling Interval**: Check every 10-30 seconds
- **Exponential Backoff**: Increase interval if job is long-running
- **Timeout**: Set maximum wait time (e.g., 10 minutes)
- **Error Handling**: Handle job failures gracefully

## Attribution Windows

### Understanding Attribution

Attribution windows determine how conversions are credited to ads:

**Click Attribution Windows**:
- **1-day click**: Conversions within 1 day of ad click
- **7-day click**: Conversions within 7 days of ad click (default)
- **28-day click**: Conversions within 28 days of ad click

**View Attribution Windows**:
- **1-day view**: Conversions within 1 day of ad impression
- **7-day view**: Conversions within 7 days of ad impression

### Custom Attribution Windows

The Insights API allows pulling raw conversion data with custom attribution windows:

**Benefits**:
- Analyze using specific business logic
- Not limited to Meta's default windows
- Compare different attribution models
- Align with internal attribution standards

**Implementation**:
- Retrieve conversion events with timestamps
- Retrieve ad interaction events with timestamps
- Apply custom attribution logic in post-processing
- Calculate conversions based on business rules

### Attribution Considerations

- **Longer Windows**: Capture more conversions but less direct attribution
- **Shorter Windows**: More direct attribution but may miss delayed conversions
- **Business Cycle**: Align windows with typical customer journey length
- **Comparison**: Use consistent windows when comparing campaigns

## Data Freshness and Availability

### Data Latency

**Real-Time Metrics**:
- Impressions, clicks, spend: 15-30 minute delay
- Engagement metrics: 15-30 minute delay

**Conversion Metrics**:
- Pixel conversions: 30-60 minute delay
- Offline conversions: Variable delay based on upload
- CAPI conversions: Near real-time

**Aggregated Metrics**:
- Some metrics require additional processing time
- Breakdowns may have longer delays
- Historical data may be updated retroactively

### Historical Data Access

**Availability**: Up to 37 months of historical data

**Considerations**:
- Older data may have limited breakdown availability
- Deprecated metrics not available for old data
- Data structure changes over time
- API version compatibility

### Data Retention

- **Active Campaigns**: Full data retention
- **Deleted Campaigns**: Data retained for 37 months
- **Deleted Ad Accounts**: Limited data access

## Deprecated Metrics (as of January 8, 2025)

Certain Instagram Insights API metrics were deprecated:

**Deprecated Metrics**:
- `video_views` (for non-Reels content)
- `email_contacts` (time series)
- `profile_views`
- `website_clicks`
- `phone_call_clicks`
- `text_message_clicks`

**Impact**:
- These metrics no longer available via API
- Historical data for these metrics may be limited
- Alternative metrics or approaches needed

**Alternatives**:
- Use Facebook Pixel for website click tracking
- Implement CAPI for comprehensive conversion tracking
- Use UTM parameters for traffic source attribution

## Rate Limiting for Insights API

### Insights-Specific Rate Limits

Insights API has additional rate limit considerations:

**General Limits**:
- Subject to standard 200 requests per hour per user
- Asynchronous reports count toward rate limit
- Complex queries consume more rate limit

**Best Practices**:
- Use asynchronous reporting for large queries
- Request only necessary fields
- Batch multiple date ranges when possible
- Cache frequently accessed data
- Implement exponential backoff

### Optimization Strategies

1. **Field Optimization**: Request only needed metrics
2. **Date Range Batching**: Combine related date ranges
3. **Caching**: Store and reuse static historical data
4. **Scheduling**: Spread API calls throughout the day
5. **Prioritization**: Prioritize critical data retrieval

## Custom Reporting Solutions

### Building Custom Dashboards

**Components**:
1. **Data Extraction**: Pull data via Insights API
2. **Data Processing**: Transform and aggregate data
3. **Data Storage**: Store in database or data warehouse
4. **Visualization**: Create charts and graphs
5. **Automation**: Schedule regular updates

**Benefits**:
- Tailored to specific business needs
- Combine with other data sources
- Custom KPIs and calculations
- Automated reporting workflows

### Multi-Account Reporting

**Agency Use Case**:
- Consolidate data from multiple client accounts
- Standardized reporting across clients
- Comparative performance analysis
- Centralized performance monitoring

**Implementation**:
1. Authenticate with system user tokens for each account
2. Iterate through accounts to pull insights
3. Normalize data structure across accounts
4. Aggregate and compare performance
5. Generate consolidated reports

### Real-Time Monitoring

**Applications**:
- Live campaign performance dashboards
- Automated alerts for performance issues
- Real-time budget pacing
- Immediate optimization opportunities

**Implementation**:
- Scheduled API calls (every 15-30 minutes)
- Compare current performance to benchmarks
- Trigger alerts when thresholds exceeded
- Display on real-time dashboard

## Integration with Business Intelligence Tools

### Data Warehouse Integration

**Process**:
1. Extract data via Insights API
2. Transform data to warehouse schema
3. Load into data warehouse (ETL/ELT)
4. Combine with other business data
5. Analyze with BI tools

**Benefits**:
- Unified data analysis
- Historical trend analysis
- Cross-channel attribution
- Advanced analytics capabilities

### BI Tool Connectors

Many BI tools offer native connectors:

**Popular Integrations**:
- **Tableau**: Meta Marketing API connector
- **Power BI**: Facebook Ads connector
- **Looker**: Custom API integration
- **Google Data Studio**: Facebook Ads connector

**Advantages**:
- Pre-built data models
- Automatic refresh schedules
- Drag-and-drop visualization
- Reduced development time

## Best Practices for Insights API Usage

### 1. Efficient Data Retrieval

- **Request Only Needed Fields**: Reduces response size and processing time
- **Use Appropriate Date Ranges**: Avoid unnecessarily large date ranges
- **Leverage Asynchronous Reporting**: For large or complex queries
- **Implement Caching**: Store and reuse historical data
- **Batch Related Requests**: Combine similar queries when possible

### 2. Error Handling

- **Implement Retry Logic**: Handle temporary failures gracefully
- **Exponential Backoff**: Increase delay between retries
- **Rate Limit Monitoring**: Track usage and adjust accordingly
- **Timeout Handling**: Set appropriate timeout values
- **Error Logging**: Log errors for debugging and monitoring

### 3. Data Quality

- **Validate Data**: Check for anomalies and inconsistencies
- **Handle Missing Data**: Account for incomplete data sets
- **Understand Metrics**: Know exactly what each metric measures
- **Attribution Awareness**: Understand attribution window impacts
- **Data Freshness**: Account for latency in real-time reporting

### 4. Performance Optimization

- **Parallel Requests**: Make multiple requests concurrently (within rate limits)
- **Pagination**: Handle paginated results efficiently
- **Incremental Updates**: Pull only new data since last update
- **Data Compression**: Use compression for data transfer
- **Optimize Queries**: Structure queries for efficiency

### 5. Security and Compliance

- **Secure Token Storage**: Protect access tokens
- **Token Rotation**: Regularly refresh tokens
- **Access Control**: Limit API access to authorized systems
- **Data Privacy**: Comply with data protection regulations
- **Audit Logging**: Track API usage and data access

## Common Use Cases

### 1. Automated Performance Reporting

**Scenario**: Daily email reports with key metrics

**Implementation**:
1. Schedule daily API call for previous day's data
2. Extract key metrics (spend, ROAS, conversions)
3. Format data into report template
4. Email to stakeholders

### 2. Real-Time Campaign Monitoring

**Scenario**: Dashboard showing live campaign performance

**Implementation**:
1. API calls every 15-30 minutes
2. Update dashboard with latest metrics
3. Alert on performance anomalies
4. Enable quick optimization decisions

### 3. Cross-Campaign Analysis

**Scenario**: Compare performance across multiple campaigns

**Implementation**:
1. Pull insights for all campaigns
2. Normalize metrics for comparison
3. Identify top and bottom performers
4. Analyze patterns and trends

### 4. Attribution Analysis

**Scenario**: Understand conversion attribution across touchpoints

**Implementation**:
1. Pull conversion data with timestamps
2. Pull ad interaction data
3. Apply custom attribution logic
4. Analyze multi-touch attribution

### 5. Budget Pacing

**Scenario**: Ensure campaigns spend budget evenly throughout month

**Implementation**:
1. Pull daily spend data
2. Compare to expected pacing
3. Alert if over/under pacing
4. Adjust budgets programmatically

## Troubleshooting Common Issues

### Issue: Empty or Missing Data

**Possible Causes**:
- Insufficient permissions
- Data not yet available (latency)
- Incorrect date range
- No activity during period

**Solutions**:
- Verify OAuth permissions
- Wait for data freshness
- Check date range parameters
- Confirm campaign was active

### Issue: Rate Limit Errors

**Possible Causes**:
- Too many requests in short period
- Complex queries consuming rate limit
- Multiple systems using same token

**Solutions**:
- Implement exponential backoff
- Reduce request frequency
- Optimize query complexity
- Use separate tokens for different systems

### Issue: Inconsistent Data

**Possible Causes**:
- Attribution window differences
- Data freshness delays
- Metric definition misunderstanding
- Time zone discrepancies

**Solutions**:
- Use consistent attribution windows
- Account for data latency
- Verify metric definitions
- Standardize time zones

### Issue: Slow API Response

**Possible Causes**:
- Large date ranges
- Multiple breakdowns
- Many fields requested
- High API load

**Solutions**:
- Use asynchronous reporting
- Reduce date range size
- Limit breakdowns
- Request fewer fields

## Key Takeaways

1. **Comprehensive Metrics**: Access to 70+ performance metrics across campaign hierarchy
2. **Flexible Querying**: Custom date ranges, time increments, and breakdowns
3. **Asynchronous Reporting**: Essential for large data sets and complex queries
4. **Attribution Windows**: Understand and leverage custom attribution for accurate analysis
5. **Rate Limiting**: Optimize requests to stay within limits and improve efficiency
6. **Data Freshness**: Account for 15-60 minute latency in real-time reporting
7. **Historical Access**: Up to 37 months of historical data available
8. **Custom Reporting**: Build tailored dashboards and reporting solutions
9. **Multi-Account**: Consolidate reporting across multiple ad accounts
10. **Best Practices**: Efficient data retrieval, error handling, and performance optimization

## References

- Meta Marketing API Documentation: https://developers.facebook.com/docs/marketing-api/
- Insights API Reference: https://developers.facebook.com/docs/marketing-api/insights/
- Async Insights: https://developers.facebook.com/docs/marketing-api/insights/best-practices/
- Attribution Windows: https://www.facebook.com/business/help/458681590974355
- Dataddo Instagram Ads Documentation: https://docs.dataddo.com/docs/instagram-ads
