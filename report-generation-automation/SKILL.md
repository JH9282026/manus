---
name: report-generation-automation
description: The Report Generation & Automation skill transforms an agentic AI into an expert report automation engineer capable of building end-to-end automated reporting systems.
---

---
name: Report Generation & Automation
description: A comprehensive automated report generation skill that enables programmatic creation, scheduling, and distribution of reports from various data sources including databases, APIs, files, and web scraping, transforming raw data into professionally formatted, timely insights delivered through multiple distribution channels.
---

# Report Generation & Automation Skill

## 1. Skill Description and Purpose

### What This Skill Enables

The Report Generation & Automation skill transforms an agentic AI into an expert report automation engineer capable of building end-to-end automated reporting systems. This skill encompasses the complete lifecycle of automated report generation—from extracting data from diverse sources to delivering polished reports through multiple distribution channels on scheduled or on-demand basis.

### Core Competencies

**Automated Report Generation Fundamentals**

This skill enables programmatic creation of reports from data sources, eliminating manual report creation through automated transformation of raw data into formatted, professional reports. The agent understands the critical distinction between *Report Design* (defining what reports should look like—structure, layout, content, branding) and *Report Generation* (how to automatically create reports—automation workflows, tools, frameworks, scheduling).

Key benefits delivered through this skill include:
- **Time Savings**: Eliminate hours of manual report creation through full automation
- **Consistency**: Standardized formatting with zero human error across all reports
- **Scalability**: Generate hundreds of reports automatically without additional effort
- **Timeliness**: Real-time or scheduled reports ensuring stakeholders receive up-to-date information
- **Accuracy**: Direct data extraction from sources eliminates manual entry errors
- **Reproducibility**: Identical processes produce consistent, verifiable results

**Report Generation Workflow Mastery**

The agent executes the complete report generation workflow:

1. **Data Extraction**: Pull data from databases (SQL, NoSQL), REST/GraphQL APIs, files (CSV, Excel, JSON, XML), and web scraping sources
2. **Data Transformation**: Clean, aggregate, calculate, filter, and join data from multiple sources
3. **Report Creation**: Apply templates, populate dynamic content, and format according to specifications
4. **Report Enhancement**: Add charts, tables, visualizations, and apply styling/branding
5. **Report Distribution**: Deliver via email, cloud storage, web portals, FTP/SFTP, or messaging platforms
6. **Report Archiving**: Store historical reports with version control and retention policies

**Architecture Understanding**

The agent operates across the complete report generation architecture:
- **Data Layer**: SQL databases (PostgreSQL, MySQL, SQL Server, Oracle, SQLite), NoSQL databases (MongoDB, Redis, Cassandra, Neo4j), APIs (REST, GraphQL), files, and web scraping
- **Processing Layer**: ETL operations, data transformation, calculations, aggregations
- **Generation Layer**: Template engines (Jinja2, Mustache, Handlebars), report builders, content formatters
- **Presentation Layer**: PDF, HTML, Excel, PowerPoint, Word document generation
- **Distribution Layer**: Email (SMTP), cloud storage (Google Drive, Dropbox, S3, Azure Blob, SharePoint), web portals, FTP/SFTP, messaging (Slack, Teams)

### When to Use This Skill

Deploy this skill when:
- Building automated reporting pipelines that run on schedules (daily, weekly, monthly, quarterly)
- Creating self-service reporting systems where users can generate parameterized reports on-demand
- Integrating multiple data sources into unified report outputs
- Implementing real-time dashboards and live data reports
- Setting up alert-based exception reports triggered by thresholds or anomalies
- Automating distribution of reports to stakeholders via email, cloud storage, or portals
- Establishing report versioning, archiving, and audit trail systems
- Optimizing existing manual reporting processes for efficiency and consistency

### Value Proposition

This skill transforms manual, error-prone reporting processes into reliable, scalable automated systems. Organizations typically achieve 80-95% reduction in report preparation time, eliminate data entry errors, ensure consistent formatting across all reports, and enable stakeholders to receive timely insights without IT intervention.

---

## 2. Required Inputs/Parameters

### Data Source Specifications

**Database Connections**
| Parameter | Format | Description |
|-----------|--------|-------------|
| `connection_type` | String | Database type: `postgresql`, `mysql`, `sqlserver`, `oracle`, `sqlite`, `mongodb`, `redis` |
| `host` | String | Database server hostname or IP address |
| `port` | Integer | Database port number (e.g., 5432 for PostgreSQL, 3306 for MySQL) |
| `database` | String | Database name to connect to |
| `username` | String | Authentication username |
| `password` | String (secure) | Authentication password (stored securely) |
| `ssl_enabled` | Boolean | Whether to use SSL/TLS encryption |
| `connection_pool_size` | Integer | Number of connections to maintain (default: 5) |

**SQL Query Parameters**
| Parameter | Format | Description |
|-----------|--------|-------------|
| `query` | String | SQL SELECT statement with optional placeholders |
| `parameters` | Object | Named parameters for query placeholders |
| `timeout_seconds` | Integer | Query execution timeout (default: 300) |

**API Connections**
| Parameter | Format | Description |
|-----------|--------|-------------|
| `api_type` | String | `rest` or `graphql` |
| `base_url` | String | API base URL endpoint |
| `endpoint` | String | Specific API endpoint path |
| `method` | String | HTTP method: `GET`, `POST`, `PUT`, `DELETE` |
| `auth_type` | String | `api_key`, `oauth2`, `basic`, `bearer` |
| `auth_credentials` | Object | Authentication credentials based on auth_type |
| `headers` | Object | Custom HTTP headers |
| `query_params` | Object | URL query parameters |
| `request_body` | Object | Request body for POST/PUT requests |
| `pagination_type` | String | `offset`, `cursor`, `page` |
| `pagination_params` | Object | Pagination configuration parameters |

**File Sources**
| Parameter | Format | Description |
|-----------|--------|-------------|
| `file_path` | String | Local file path or URL |
| `file_type` | String | `csv`, `excel`, `json`, `xml`, `log` |
| `encoding` | String | File encoding (default: `utf-8`) |
| `delimiter` | String | CSV delimiter (default: `,`) |
| `sheet_name` | String | Excel sheet name (for Excel files) |
| `parse_dates` | Array | Column names to parse as dates |

**Web Scraping Sources**
| Parameter | Format | Description |
|-----------|--------|-------------|
| `target_url` | String | URL to scrape |
| `scraping_method` | String | `beautifulsoup`, `selenium`, `playwright`, `scrapy` |
| `selectors` | Object | CSS/XPath selectors for data extraction |
| `wait_for_js` | Boolean | Wait for JavaScript rendering |
| `pagination_selector` | String | Selector for next page navigation |

### Report Configuration Parameters

**Template Configuration**
| Parameter | Format | Description |
|-----------|--------|-------------|
| `template_engine` | String | `jinja2`, `mustache`, `handlebars`, `erb` |
| `template_path` | String | Path to template file |
| `template_string` | String | Inline template content |
| `variables` | Object | Variables to inject into template |
| `filters` | Array | Custom template filters |

**Output Format Configuration**
| Parameter | Format | Description |
|-----------|--------|-------------|
| `output_format` | String | `pdf`, `html`, `excel`, `word`, `powerpoint`, `csv`, `json` |
| `output_path` | String | Destination path for generated report |
| `filename_pattern` | String | Dynamic filename pattern (e.g., `Report_{{date}}_{{region}}.pdf`) |
| `page_size` | String | Page size: `letter`, `a4`, `legal` |
| `orientation` | String | `portrait` or `landscape` |
| `margins` | Object | Page margins: `{top, bottom, left, right}` in inches/mm |

**Formatting Parameters**
| Parameter | Format | Description |
|-----------|--------|-------------|
| `number_format` | Object | `{decimals: 2, thousands_sep: ",", currency: "$"}` |
| `date_format` | String | Date format pattern (e.g., `YYYY-MM-DD`, `MM/DD/YYYY`) |
| `timezone` | String | Timezone for date/time values (e.g., `America/New_York`) |
| `conditional_formats` | Array | Rules for conditional formatting |
| `theme` | Object | Color scheme, fonts, branding elements |

**Report Parameters (Dynamic)**
| Parameter | Format | Description |
|-----------|--------|-------------|
| `date_range` | Object | `{start_date: "2024-01-01", end_date: "2024-12-31"}` |
| `filters` | Object | `{region: ["North", "South"], product: "All"}` |
| `grouping` | Array | Fields to group by: `["region", "product"]` |
| `sorting` | Object | `{field: "revenue", order: "desc"}` |
| `aggregations` | Array | `["sum", "avg", "count", "min", "max"]` |

### Scheduling and Distribution Parameters

**Schedule Configuration**
| Parameter | Format | Description |
|-----------|--------|-------------|
| `schedule_type` | String | `cron`, `interval`, `daily`, `weekly`, `monthly` |
| `cron_expression` | String | Cron syntax (e.g., `0 9 * * 1` for Monday 9 AM) |
| `interval_minutes` | Integer | Interval in minutes for recurring generation |
| `timezone` | String | Schedule timezone |
| `start_date` | String | Schedule start date |
| `end_date` | String | Schedule end date (optional) |

**Email Distribution**
| Parameter | Format | Description |
|-----------|--------|-------------|
| `smtp_server` | String | SMTP server hostname |
| `smtp_port` | Integer | SMTP port (587 for TLS, 465 for SSL) |
| `smtp_username` | String | SMTP authentication username |
| `smtp_password` | String (secure) | SMTP authentication password |
| `from_address` | String | Sender email address |
| `to_addresses` | Array | Recipient email addresses |
| `cc_addresses` | Array | CC recipient addresses |
| `bcc_addresses` | Array | BCC recipient addresses |
| `subject_template` | String | Email subject with variables |
| `body_template` | String | Email body (HTML or plain text) |
| `attach_report` | Boolean | Whether to attach the report file |

**Cloud Storage Distribution**
| Parameter | Format | Description |
|-----------|--------|-------------|
| `storage_provider` | String | `google_drive`, `dropbox`, `s3`, `azure_blob`, `sharepoint` |
| `credentials` | Object | Provider-specific authentication credentials |
| `destination_folder` | String | Target folder path |
| `share_settings` | Object | Sharing permissions and access control |

**Archiving Configuration**
| Parameter | Format | Description |
|-----------|--------|-------------|
| `archive_enabled` | Boolean | Enable report archiving |
| `archive_path` | String | Archive storage location |
| `retention_days` | Integer | Number of days to retain archived reports |
| `version_format` | String | Version naming pattern |
| `compression` | Boolean | Compress archived reports |

---

## 3. Expected Outputs/Deliverables

### Primary Report Outputs

**PDF Reports**
- Professional multi-page PDF documents with headers, footers, page numbers
- Embedded charts, tables, and images rendered at print quality (300 DPI minimum)
- Hyperlinked table of contents for navigation
- Bookmarks for section navigation
- Digital signatures for authentication (when configured)
- File size optimized for email distribution (typically under 10MB)

**HTML Reports**
- Responsive HTML documents viewable across devices
- Interactive charts with hover tooltips and drill-down capabilities
- Embedded CSS styling with consistent branding
- Self-contained single-file output or linked assets
- Print-friendly stylesheet included
- Accessibility compliant (WCAG 2.1 AA)

**Excel Reports**
- Multi-worksheet workbooks with organized data tabs
- Formatted tables with headers, borders, and alternating row colors
- Embedded charts linked to data ranges
- Conditional formatting rules applied
- Formulas for calculated fields
- Named ranges for data reference
- Pivot table-ready data structures

**Word Documents**
- Professional document formatting with styles
- Dynamic table of contents
- Headers and footers with page numbers
- Embedded tables and charts
- Track changes disabled for final output
- Compatible with Microsoft Word 2016+

**PowerPoint Presentations**
- Slide deck with consistent template styling
- Data-driven charts and tables
- Speaker notes with context
- Animation-ready structure
- Master slide compliance
- 16:9 aspect ratio standard

### Supporting Outputs

**Generation Logs**
```json
{
  "report_id": "RPT-2024-001234",
  "generation_timestamp": "2024-01-15T09:30:45Z",
  "duration_seconds": 12.5,
  "status": "success",
  "data_sources_accessed": ["sales_db", "inventory_api"],
  "records_processed": 15420,
  "output_file": "/reports/2024/01/sales_report_2024-01-15.pdf",
  "file_size_bytes": 2458632,
  "distribution_status": {
    "email": "sent",
    "recipients": 5,
    "cloud_upload": "completed"
  }
}
```

**Error Reports**
- Detailed error messages with stack traces
- Data validation failure reports
- Missing data indicators
- Recommendations for resolution

**Metadata Files**
- Report manifest with generation parameters
- Data lineage documentation
- Version history tracking
- Checksum for integrity verification

### Quality Standards

| Quality Metric | Standard |
|----------------|----------|
| Data Accuracy | 100% match with source data |
| Formatting Consistency | Zero variation across report runs |
| Generation Time | < 60 seconds for standard reports |
| File Size | Optimized, typically < 10MB for PDF |
| Accessibility | WCAG 2.1 AA compliant for HTML |
| Print Quality | 300 DPI minimum for graphics |
| Error Rate | < 0.1% generation failures |

---

## 4. Example Use Cases

### Use Case 1: Automated Financial Reporting System

**Scenario**: A finance department needs automated generation of monthly financial reports including income statements, balance sheets, and cash flow statements.

**Implementation**:

```python
# Financial Report Automation Configuration
config = {
    "data_sources": [
        {
            "name": "accounting_db",
            "type": "postgresql",
            "query": """
                SELECT account_type, account_name, 
                       SUM(debit) as debits, SUM(credit) as credits,
                       SUM(credit) - SUM(debit) as balance
                FROM general_ledger
                WHERE posting_date BETWEEN %(start_date)s AND %(end_date)s
                GROUP BY account_type, account_name
                ORDER BY account_type, account_name
            """
        }
    ],
    "report_template": "financial_statements.jinja2",
    "output_formats": ["pdf", "excel"],
    "schedule": {
        "type": "monthly",
        "day": 5,  # 5th of each month
        "time": "06:00",
        "timezone": "America/New_York"
    },
    "distribution": {
        "email": {
            "recipients": ["cfo@company.com", "finance-team@company.com"],
            "subject": "Monthly Financial Statements - {{month_year}}",
            "body": "Please find attached the financial statements for {{month_year}}."
        },
        "sharepoint": {
            "folder": "/Finance/Monthly Reports/{{year}}/{{month}}"
        }
    },
    "archiving": {
        "enabled": True,
        "retention_years": 7,
        "path": "/archives/financial/{{year}}/{{month}}"
    }
}
```

**Outputs Delivered**:
- Professional PDF financial statements with company branding
- Excel workbook with detailed transaction data and pivot tables
- Automated email delivery to finance leadership on the 5th of each month
- SharePoint upload for team access
- 7-year archive with audit trail

### Use Case 2: Real-Time Sales Dashboard Automation

**Scenario**: Sales leadership requires daily sales reports with previous day performance, MTD comparisons, and regional breakdowns.

**Implementation**:

```python
# Daily Sales Report Configuration
sales_report_config = {
    "data_sources": [
        {
            "name": "crm_api",
            "type": "rest",
            "base_url": "https://api.salesforce.com",
            "endpoints": [
                "/services/data/v57.0/query?q=SELECT...",
            ],
            "auth": {"type": "oauth2", "credentials_key": "salesforce_oauth"}
        },
        {
            "name": "sales_warehouse",
            "type": "snowflake",
            "query": "SELECT * FROM sales_facts WHERE sale_date = CURRENT_DATE - 1"
        }
    ],
    "transformations": [
        {"aggregate": {"group_by": ["region", "product_category"], "metrics": ["revenue", "units", "deals"]}},
        {"calculate": {"mtd_variance": "(current_mtd - prior_mtd) / prior_mtd * 100"}},
        {"rank": {"by": "revenue", "partition": "region"}}
    ],
    "report_sections": [
        {"name": "Executive Summary", "type": "kpi_cards", "metrics": ["total_revenue", "deals_closed", "avg_deal_size"]},
        {"name": "Regional Performance", "type": "table_with_sparklines", "grouping": "region"},
        {"name": "Top Performers", "type": "ranked_list", "limit": 10},
        {"name": "Pipeline Analysis", "type": "funnel_chart"}
    ],
    "schedule": {
        "type": "daily",
        "time": "07:00",
        "exclude_weekends": True
    },
    "distribution": {
        "email": {"recipients": ["sales-leadership@company.com"]},
        "slack": {"channel": "#sales-daily", "message": "📊 Daily Sales Report Ready"}
    }
}
```

**Outputs Delivered**:
- Interactive HTML dashboard with drill-down capabilities
- PDF summary for mobile viewing
- Slack notification with key metrics preview
- Email with attached reports by 7 AM each business day

### Use Case 3: Marketing Campaign Analytics Automation

**Scenario**: Marketing team needs weekly campaign performance reports aggregating data from Google Analytics, social media platforms, and email marketing systems.

**Implementation**:

```python
# Marketing Analytics Report Configuration
marketing_config = {
    "data_sources": [
        {"name": "google_analytics", "type": "rest", "api": "Google Analytics Data API v1"},
        {"name": "facebook_ads", "type": "rest", "api": "Facebook Marketing API"},
        {"name": "mailchimp", "type": "rest", "api": "Mailchimp Marketing API"},
        {"name": "hubspot", "type": "rest", "api": "HubSpot API"}
    ],
    "metrics_framework": {
        "acquisition": ["sessions", "users", "bounce_rate", "traffic_sources"],
        "engagement": ["page_views", "time_on_site", "social_shares"],
        "conversion": ["goal_completions", "conversion_rate", "revenue"],
        "email": ["open_rate", "click_rate", "unsubscribes"]
    },
    "visualizations": [
        {"type": "line_chart", "metric": "daily_traffic", "comparison": "prior_week"},
        {"type": "pie_chart", "metric": "traffic_by_source"},
        {"type": "bar_chart", "metric": "campaign_performance"},
        {"type": "heatmap", "metric": "engagement_by_hour"}
    ],
    "schedule": {"type": "weekly", "day": "Monday", "time": "09:00"},
    "distribution": {
        "email": {"recipients": ["marketing@company.com"]},
        "google_drive": {"folder": "Marketing/Weekly Reports"}
    }
}
```

### Use Case 4: Operational Inventory and Supply Chain Reporting

**Scenario**: Operations team requires daily inventory status reports with low-stock alerts, reorder recommendations, and supplier performance metrics.

**Implementation**:

```python
# Inventory Operations Report Configuration
inventory_config = {
    "data_sources": [
        {"name": "inventory_db", "type": "mysql", "query": "SELECT * FROM inventory_levels"},
        {"name": "orders_db", "type": "mysql", "query": "SELECT * FROM purchase_orders"},
        {"name": "supplier_api", "type": "rest", "endpoint": "/suppliers/performance"}
    ],
    "alert_thresholds": {
        "low_stock": {"condition": "quantity < reorder_point", "severity": "warning"},
        "critical_stock": {"condition": "quantity < safety_stock", "severity": "critical"},
        "overstock": {"condition": "quantity > max_stock * 1.2", "severity": "info"}
    },
    "conditional_generation": {
        "alert_report": {"trigger": "any_critical_stock", "immediate": True},
        "daily_summary": {"trigger": "scheduled", "time": "06:00"}
    },
    "outputs": [
        {"format": "pdf", "sections": ["summary", "alerts", "reorder_recommendations"]},
        {"format": "excel", "sheets": ["inventory_status", "supplier_scorecard", "reorder_list"]}
    ],
    "distribution": {
        "email": {"recipients": ["operations@company.com", "purchasing@company.com"]},
        "sms": {"critical_alerts": True, "recipients": ["+1234567890"]}
    }
}
```

### Use Case 5: Executive Board Report Automation

**Scenario**: Executive leadership requires monthly board-ready reports with KPIs, strategic metrics, and trend analysis across all business units.

**Implementation**:

```python
# Executive Board Report Configuration
executive_config = {
    "data_sources": [
        {"name": "data_warehouse", "type": "snowflake", "schemas": ["finance", "sales", "hr", "operations"]},
        {"name": "bi_platform", "type": "tableau", "workbooks": ["executive_dashboard"]}
    ],
    "report_structure": {
        "cover_page": {"title": "Monthly Executive Report", "date": "{{report_month}}", "confidential": True},
        "executive_summary": {"type": "narrative", "ai_generated": True, "max_words": 500},
        "financial_highlights": {"kpis": ["revenue", "ebitda", "cash_position", "budget_variance"]},
        "operational_metrics": {"kpis": ["nps", "customer_retention", "employee_satisfaction"]},
        "strategic_initiatives": {"status_tracker": True, "milestone_chart": True},
        "risk_assessment": {"heatmap": True, "mitigation_status": True},
        "appendix": {"detailed_financials": True, "methodology": True}
    },
    "formatting": {
        "template": "board_presentation_template.pptx",
        "branding": "corporate_brand_guide",
        "charts": {"style": "minimal", "colors": "corporate_palette"}
    },
    "schedule": {"type": "monthly", "day": -3, "time": "18:00"},  # 3 days before month end
    "distribution": {
        "email": {"recipients": ["board@company.com"], "encrypted": True},
        "sharepoint": {"folder": "/Board/Monthly Reports", "permissions": "board_members_only"}
    },
    "versioning": {"enabled": True, "approval_workflow": True}
}
```

---

## 5. Prerequisites and Dependencies

### Technical Infrastructure

**Runtime Environment**
- Python 3.9+ with pip package manager
- Node.js 18+ (for JavaScript-based tools)
- R 4.0+ (for R-based reporting)
- Docker (optional, for containerized deployment)

**Database Connectivity**
- Database drivers: `psycopg2` (PostgreSQL), `pymysql` (MySQL), `pyodbc` (SQL Server), `cx_Oracle` (Oracle)
- NoSQL clients: `pymongo` (MongoDB), `redis-py` (Redis)
- Cloud warehouse connectors: `snowflake-connector-python`, `google-cloud-bigquery`

**Required Python Libraries**
```
# Core Data Processing
pandas>=2.0.0
numpy>=1.24.0
sqlalchemy>=2.0.0

# Report Generation
reportlab>=4.0.0
fpdf2>=2.7.0
weasyprint>=59.0
jinja2>=3.1.0
python-docx>=0.8.11
python-pptx>=0.6.21
openpyxl>=3.1.0
xlsxwriter>=3.1.0

# Visualization
matplotlib>=3.7.0
seaborn>=0.12.0
plotly>=5.15.0

# Web Scraping
beautifulsoup4>=4.12.0
selenium>=4.10.0
playwright>=1.35.0
requests>=2.31.0

# Scheduling & Distribution
celery>=5.3.0
apscheduler>=3.10.0
boto3>=1.28.0  # AWS S3
google-api-python-client>=2.90.0  # Google Drive
```

### External Service Access

**API Credentials Required**
- Database connection credentials (host, port, username, password)
- REST/GraphQL API keys and OAuth tokens
- SMTP server credentials for email distribution
- Cloud storage API credentials (AWS, GCP, Azure)
- Third-party service API keys (Salesforce, HubSpot, Google Analytics)

**Network Requirements**
- Outbound HTTPS access to data sources and APIs
- SMTP port access (587/465) for email distribution
- FTP/SFTP access if using file transfer distribution

### Knowledge Prerequisites

**Data Skills**
- SQL query writing (SELECT, JOIN, GROUP BY, aggregations)
- Understanding of data structures (JSON, XML, CSV)
- Basic ETL concepts (extract, transform, load)

**Programming Fundamentals**
- Python scripting for automation
- Template syntax (Jinja2 variables, loops, conditionals)
- Understanding of cron expressions for scheduling

**Report Design Understanding**
- Document structure and layout principles
- Chart type selection for different data types
- Color theory and accessibility considerations

### System Permissions

**File System Access**
- Read access to template directories
- Write access to output directories
- Archive storage write permissions

**Network Access**
- Database network connectivity
- API endpoint accessibility
- Email server connectivity

**Credential Management**
- Secure credential storage (environment variables, secrets manager)
- API key rotation procedures
- OAuth token refresh handling

### Recommended Infrastructure

**Development Environment**
- IDE with Python/SQL support
- Version control (Git) for templates and code
- Testing environment for report validation

**Production Environment**
- Scheduled task execution (Airflow, Celery, cron)
- Monitoring and alerting (report generation failures)
- Log aggregation for troubleshooting
- Backup and disaster recovery for archives

---

## Implementation Checklist

- [ ] Identify all data sources and establish connectivity
- [ ] Design report templates with placeholder variables
- [ ] Configure data extraction queries and API calls
- [ ] Implement data transformation and calculation logic
- [ ] Set up template engine with dynamic content rendering
- [ ] Configure output format generation (PDF, Excel, HTML)
- [ ] Establish scheduling mechanism (cron, Airflow, Celery)
- [ ] Configure distribution channels (email, cloud storage, portals)
- [ ] Implement error handling and logging
- [ ] Set up monitoring and alerting for failures
- [ ] Configure archiving and version control
- [ ] Document report parameters and usage guidelines
- [ ] Create runbooks for troubleshooting common issues
- [ ] Establish testing procedures for report validation
