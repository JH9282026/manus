# Microsoft Ads API Reporting and Automation Guide

## Introduction

The Microsoft Advertising Reporting Service enables programmatic access to comprehensive performance data for accounts, campaigns, ad groups, keywords, and ads. This guide covers report types, request parameters, automation strategies, and best practices for building robust reporting solutions.

## Reporting Service Overview

### What is the Reporting Service?

The Reporting Service is a SOAP-based web service that allows advertisers to:

- Generate detailed performance reports
- Track financial metrics and ROI
- Analyze ad effectiveness
- Monitor quality scores
- Identify optimization opportunities
- Export data for external analysis
- Automate reporting workflows

### Service Endpoint

**Production:**
```
https://reporting.api.bingads.microsoft.com/Api/Advertiser/Reporting/v13/ReportingService.svc
```

**Sandbox:**
```
https://reporting.api.sandbox.bingads.microsoft.com/Api/Advertiser/Reporting/v13/ReportingService.svc
```

## Report Request Process

### Standard Workflow

```
1. Submit Report Request
   ↓
2. Receive Report Request ID
   ↓
3. Poll for Report Status
   ↓
4. Report Generation Complete
   ↓
5. Download Report from URL
   ↓
6. Unzip and Process Data
```

### Step-by-Step Implementation

#### Step 1: Submit Report Request

```python
from bingads.v13.reporting import (
    CampaignPerformanceReportRequest,
    ReportFormat,
    ReportAggregation,
    CampaignPerformanceReportColumn,
    AccountThroughCampaignReportScope,
    ReportTime,
    ReportTimePeriod
)

# Define report request
report_request = CampaignPerformanceReportRequest(
    Format=ReportFormat.Csv,
    ReportName='Daily Campaign Performance',
    ReturnOnlyCompleteData=False,
    Aggregation=ReportAggregation.Daily,
    Columns=[
        CampaignPerformanceReportColumn.TimePeriod,
        CampaignPerformanceReportColumn.AccountName,
        CampaignPerformanceReportColumn.CampaignName,
        CampaignPerformanceReportColumn.CampaignId,
        CampaignPerformanceReportColumn.Impressions,
        CampaignPerformanceReportColumn.Clicks,
        CampaignPerformanceReportColumn.Ctr,
        CampaignPerformanceReportColumn.Spend,
        CampaignPerformanceReportColumn.Conversions,
        CampaignPerformanceReportColumn.ConversionRate,
        CampaignPerformanceReportColumn.CostPerConversion,
    ],
    Scope=AccountThroughCampaignReportScope(
        AccountIds=[account_id],
        Campaigns=None  # All campaigns
    ),
    Time=ReportTime(
        PredefinedTime=ReportTimePeriod.LastSevenDays
    )
)

# Submit request
report_request_id = reporting_service.SubmitGenerateReport(report_request)
print(f"Report Request ID: {report_request_id}")
```

#### Step 2: Poll for Report Status

```python
import time

def poll_report_status(report_request_id, max_attempts=60, poll_interval=5):
    """Poll report status until complete or timeout."""
    for attempt in range(max_attempts):
        status = reporting_service.PollGenerateReport(report_request_id)
        
        print(f"Attempt {attempt + 1}: Status = {status.ReportRequestStatus}")
        
        if status.ReportRequestStatus == 'Success':
            return status.ReportDownloadUrl
        elif status.ReportRequestStatus == 'Error':
            raise Exception("Report generation failed")
        
        time.sleep(poll_interval)
    
    raise Exception("Report generation timeout")

download_url = poll_report_status(report_request_id)
print(f"Download URL: {download_url}")
```

#### Step 3: Download and Extract Report

```python
import requests
import zipfile
import os

def download_report(download_url, output_dir='reports'):
    """Download and extract report."""
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Download zip file
    response = requests.get(download_url)
    zip_path = os.path.join(output_dir, 'report.zip')
    
    with open(zip_path, 'wb') as f:
        f.write(response.content)
    
    # Extract
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(output_dir)
    
    # Find CSV file
    csv_files = [f for f in os.listdir(output_dir) if f.endswith('.csv')]
    if csv_files:
        csv_path = os.path.join(output_dir, csv_files[0])
        print(f"Report extracted to: {csv_path}")
        return csv_path
    
    raise Exception("No CSV file found in report")

report_path = download_report(download_url)
```

### Using ReportingServiceManager (Simplified)

```python
from bingads.v13.reporting import ReportingServiceManager

# Create manager
reporting_service_manager = ReportingServiceManager(
    authorization_data=authorization_data,
    poll_interval_in_milliseconds=5000,
    environment='production'
)

# One-step download
report_file_path = reporting_service_manager.download_file(
    report_request=report_request,
    result_file_directory='reports',
    result_file_name='campaign_performance.csv',
    overwrite_result_file=True,
    timeout_in_milliseconds=3600000  # 1 hour
)

print(f"Report downloaded to: {report_file_path}")
```

## Report Types

### Performance Reports

#### Account Performance Report

**Purpose**: Long-term account performance and trends

**Key Columns**:
- TimePeriod
- AccountName, AccountId
- Impressions, Clicks, Ctr
- Spend, AveragePosition
- Conversions, Revenue

**Use Cases**:
- Account-level dashboards
- Historical trend analysis
- Budget planning
- Multi-account comparison

#### Campaign Performance Report

**Purpose**: High-level campaign performance and quality

**Key Columns**:
- CampaignName, CampaignId, CampaignType
- Status, BudgetName
- Impressions, Clicks, Ctr
- Spend, CostPerConversion
- QualityScore, ExpectedCtr

**Use Cases**:
- Campaign comparison
- Budget allocation
- Performance monitoring
- Quality score tracking

#### Ad Group Performance Report

**Purpose**: Compare ad group delivery and performance

**Key Columns**:
- AdGroupName, AdGroupId
- CampaignName, CampaignId
- Impressions, Clicks, Spend
- Conversions, ConversionRate
- AverageCpc, AveragePosition

**Use Cases**:
- Ad group optimization
- Bid adjustment
- Performance segmentation

#### Keyword Performance Report

**Purpose**: Identify high and low performing keywords

**Key Columns**:
- Keyword, KeywordId
- MatchType, BidMatchType
- Impressions, Clicks, Ctr
- AverageCpc, Spend
- Conversions, QualityScore
- TopVsOther (top of page vs. other)

**Use Cases**:
- Keyword optimization
- Bid management
- Negative keyword identification
- Match type analysis

**Example Request**:
```python
from bingads.v13.reporting import (
    KeywordPerformanceReportRequest,
    KeywordPerformanceReportColumn
)

keyword_report = KeywordPerformanceReportRequest(
    Format=ReportFormat.Csv,
    ReportName='Keyword Performance',
    Aggregation=ReportAggregation.Summary,
    Columns=[
        KeywordPerformanceReportColumn.Keyword,
        KeywordPerformanceReportColumn.KeywordId,
        KeywordPerformanceReportColumn.MatchType,
        KeywordPerformanceReportColumn.Impressions,
        KeywordPerformanceReportColumn.Clicks,
        KeywordPerformanceReportColumn.Ctr,
        KeywordPerformanceReportColumn.AverageCpc,
        KeywordPerformanceReportColumn.Spend,
        KeywordPerformanceReportColumn.Conversions,
        KeywordPerformanceReportColumn.QualityScore,
    ],
    Scope=AccountThroughAdGroupReportScope(
        AccountIds=[account_id]
    ),
    Time=ReportTime(
        PredefinedTime=ReportTimePeriod.LastThirtyDays
    )
)
```

#### Ad Performance Report

**Purpose**: Identify which ads drive clicks and conversions

**Key Columns**:
- AdTitle, AdDescription
- AdId, AdType
- Impressions, Clicks, Ctr
- Spend, Conversions
- AdRelevance, LandingPageExperience

**Use Cases**:
- Ad copy testing
- Creative optimization
- A/B testing analysis

#### Search Query Performance Report

**Purpose**: Understand actual search queries triggering ads

**Key Columns**:
- SearchQuery
- Keyword, MatchType
- Impressions, Clicks, Ctr
- Spend, Conversions
- SearchQueryMatchType

**Use Cases**:
- Keyword discovery
- Negative keyword identification
- Match type optimization
- Search intent analysis

**Example Request**:
```python
from bingads.v13.reporting import (
    SearchQueryPerformanceReportRequest,
    SearchQueryPerformanceReportColumn
)

search_query_report = SearchQueryPerformanceReportRequest(
    Format=ReportFormat.Csv,
    ReportName='Search Query Analysis',
    Aggregation=ReportAggregation.Summary,
    Columns=[
        SearchQueryPerformanceReportColumn.SearchQuery,
        SearchQueryPerformanceReportColumn.Keyword,
        SearchQueryPerformanceReportColumn.MatchType,
        SearchQueryPerformanceReportColumn.Impressions,
        SearchQueryPerformanceReportColumn.Clicks,
        SearchQueryPerformanceReportColumn.Conversions,
    ],
    Scope=AccountThroughAdGroupReportScope(
        AccountIds=[account_id]
    ),
    Time=ReportTime(
        PredefinedTime=ReportTimePeriod.LastSevenDays
    )
)
```

### Specialized Reports

#### Conversion Performance Report

**Purpose**: Track which campaigns and keywords lead to conversions

**Key Columns**:
- ConversionName, Goal
- CampaignName, AdGroupName, Keyword
- Conversions, Revenue
- Assists, ConversionRate

#### Geographic Performance Report

**Purpose**: Analyze performance by location

**Key Columns**:
- Country, State, City
- MetroArea, LocationType
- Impressions, Clicks, Conversions

#### Budget Summary Report

**Purpose**: Monitor budget pacing and spend

**Key Columns**:
- CampaignName, BudgetName
- MonthlyBudget, DailySpend
- MonthToDateSpend, BudgetRemaining

#### Change History Report

**Purpose**: Track changes to account, campaigns, ad groups, and ads

**Key Columns**:
- DateTime, ChangedBy
- ItemChanged, AttributeName
- OldValue, NewValue
- HowChanged (Added, Updated, Deleted)

**Use Cases**:
- Audit trail
- Change tracking
- Troubleshooting performance changes
- Team accountability

## Report Parameters

### Aggregation Levels

**Available Aggregations**:
- **Summary**: All data aggregated into single row per entity
- **Hourly**: Data broken down by hour
- **Daily**: Data broken down by day (most common)
- **Weekly**: Data broken down by week
- **Monthly**: Data broken down by month
- **Yearly**: Data broken down by year
- **HourOfDay**: Aggregated by hour (0-23) across date range
- **DayOfWeek**: Aggregated by day of week across date range

**Example**:
```python
report_request.Aggregation = ReportAggregation.Daily
```

### Time Periods

**Predefined Time Periods**:
- Today
- Yesterday
- LastSevenDays
- ThisWeek
- LastWeek
- LastFourWeeks
- ThisMonth
- LastMonth
- LastThreeMonths
- LastSixMonths
- ThisYear
- LastYear

**Custom Date Range**:
```python
from datetime import datetime, timedelta

report_request.Time = ReportTime(
    CustomDateRangeStart=datetime(2026, 1, 1),
    CustomDateRangeEnd=datetime(2026, 1, 31)
)
```

### Scope

Define which entities to include in the report.

**Account-Level Scope**:
```python
report_request.Scope = AccountReportScope(
    AccountIds=[account_id]
)
```

**Campaign-Level Scope**:
```python
report_request.Scope = AccountThroughCampaignReportScope(
    AccountIds=[account_id],
    Campaigns=[
        CampaignReportScope(
            AccountId=account_id,
            CampaignId=campaign_id
        )
    ]
)
```

**Ad Group-Level Scope**:
```python
report_request.Scope = AccountThroughAdGroupReportScope(
    AccountIds=[account_id],
    Campaigns=[
        CampaignReportScope(
            AccountId=account_id,
            CampaignId=campaign_id,
            AdGroups=[ad_group_id]
        )
    ]
)
```

### Filters

Apply criteria to filter report data.

**Example - Filter by Device Type**:
```python
report_request.Filter = KeywordPerformanceReportFilter(
    DeviceType=['Computer', 'Smartphone']
)
```

**Example - Filter by Campaign Status**:
```python
report_request.Filter = CampaignPerformanceReportFilter(
    Status=['Active', 'Paused']
)
```

### Format Options

**Available Formats**:
- **Csv**: Comma-separated values (most common)
- **Tsv**: Tab-separated values
- **Xml**: XML format

**Format Version**:
```python
report_request.Format = ReportFormat.Csv
report_request.FormatVersion = '2.0'  # Latest format
```

### ReturnOnlyCompleteData

**Purpose**: Ensure data completeness

**Behavior**:
- `True`: Only return data if fully processed (recommended for historical data)
- `False`: Return available data even if incomplete (for recent data)

**Important**: Cannot be `True` if time period includes current day

```python
report_request.ReturnOnlyCompleteData = True
```

## Report Automation Strategies

### Scheduled Daily Reports

```python
import schedule
import time
from datetime import datetime, timedelta

def generate_daily_report():
    """Generate yesterday's performance report."""
    yesterday = datetime.now() - timedelta(days=1)
    
    report_request = CampaignPerformanceReportRequest(
        Format=ReportFormat.Csv,
        ReportName=f'Daily Report {yesterday.strftime("%Y-%m-%d")}',
        Aggregation=ReportAggregation.Daily,
        Columns=[...],  # Your columns
        Scope=AccountThroughCampaignReportScope(
            AccountIds=[account_id]
        ),
        Time=ReportTime(
            CustomDateRangeStart=yesterday,
            CustomDateRangeEnd=yesterday
        ),
        ReturnOnlyCompleteData=True
    )
    
    # Download report
    report_path = reporting_service_manager.download_file(
        report_request=report_request,
        result_file_directory='daily_reports',
        result_file_name=f'report_{yesterday.strftime("%Y%m%d")}.csv',
        overwrite_result_file=True
    )
    
    # Process report (send email, upload to database, etc.)
    process_report(report_path)
    
    print(f"Daily report generated: {report_path}")

# Schedule daily at 6 AM
schedule.every().day.at("06:00").do(generate_daily_report)

while True:
    schedule.run_pending()
    time.sleep(60)
```

### Multi-Report Automation

```python
def generate_all_reports():
    """Generate multiple report types."""
    reports = [
        ('campaign', create_campaign_report_request()),
        ('keyword', create_keyword_report_request()),
        ('search_query', create_search_query_report_request()),
        ('ad', create_ad_report_request()),
    ]
    
    for report_name, report_request in reports:
        try:
            report_path = reporting_service_manager.download_file(
                report_request=report_request,
                result_file_directory='reports',
                result_file_name=f'{report_name}_report.csv',
                overwrite_result_file=True
            )
            print(f"{report_name} report: {report_path}")
        except Exception as e:
            print(f"Error generating {report_name} report: {e}")
```

### Database Integration

```python
import pandas as pd
import sqlalchemy

def load_report_to_database(report_path, table_name):
    """Load report data into database."""
    # Read CSV
    df = pd.read_csv(report_path, skiprows=10)  # Skip header rows
    
    # Clean column names
    df.columns = df.columns.str.strip().str.replace(' ', '_').str.lower()
    
    # Create database connection
    engine = sqlalchemy.create_engine('postgresql://user:pass@localhost/db')
    
    # Load to database
    df.to_sql(
        table_name,
        engine,
        if_exists='append',
        index=False
    )
    
    print(f"Loaded {len(df)} rows to {table_name}")

# Use in automation
report_path = reporting_service_manager.download_file(...)
load_report_to_database(report_path, 'campaign_performance')
```

### Email Report Distribution

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def email_report(report_path, recipients):
    """Email report as attachment."""
    msg = MIMEMultipart()
    msg['From'] = 'reports@example.com'
    msg['To'] = ', '.join(recipients)
    msg['Subject'] = f'Microsoft Ads Performance Report - {datetime.now().strftime("%Y-%m-%d")}'
    
    body = "Please find attached the latest performance report."
    msg.attach(MIMEText(body, 'plain'))
    
    # Attach report
    with open(report_path, 'rb') as f:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header(
            'Content-Disposition',
            f'attachment; filename={os.path.basename(report_path)}'
        )
        msg.attach(part)
    
    # Send email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('your_email@gmail.com', 'your_password')
    server.send_message(msg)
    server.quit()
    
    print(f"Report emailed to {recipients}")
```

## Best Practices

### Report Request Optimization

1. **Request only needed columns**: Reduces file size and processing time
2. **Use appropriate aggregation**: Daily for most use cases
3. **Set ReturnOnlyCompleteData wisely**: True for historical, False for recent
4. **Limit scope when possible**: Specific campaigns vs. entire account
5. **Use filters**: Reduce data volume

### Performance Considerations

1. **Implement timeout handling**: Reports can take time to generate
2. **Use ReportingServiceManager**: Simplifies polling and download
3. **Schedule during off-peak hours**: Faster generation
4. **Cache reports**: Don't regenerate unnecessarily
5. **Parallel report generation**: Submit multiple requests concurrently

### Error Handling

```python
def robust_report_download(report_request, max_retries=3):
    """Download report with retry logic."""
    for attempt in range(max_retries):
        try:
            report_path = reporting_service_manager.download_file(
                report_request=report_request,
                result_file_directory='reports',
                result_file_name='report.csv',
                overwrite_result_file=True,
                timeout_in_milliseconds=3600000
            )
            return report_path
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                time.sleep(60 * (attempt + 1))  # Exponential backoff
            else:
                raise
```

### Data Processing

1. **Skip header rows**: Microsoft reports have metadata in first ~10 rows
2. **Handle data types**: Convert strings to numbers/dates as needed
3. **Validate data**: Check for completeness and accuracy
4. **Archive reports**: Keep historical copies
5. **Incremental loading**: Only load new data to database

## Conclusion

The Microsoft Ads Reporting Service provides comprehensive programmatic access to performance data across all levels of account hierarchy. By understanding report types, request parameters, and automation strategies, advertisers can build robust reporting solutions that deliver timely insights, enable data-driven decision-making, and integrate seamlessly with business intelligence systems. Effective reporting automation combines appropriate report selection, optimized request parameters, reliable error handling, and efficient data processing to create scalable, maintainable reporting workflows.
