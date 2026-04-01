---
name: report-generation-automation
description: "Automate the creation and distribution of business reports from data sources. Use for: automated report generation, template-based reporting, scheduled report delivery, data pipeline integration, PDF/Excel/HTML report creation, dashboard snapshots, and report distribution workflows."
---

# Report Generation Automation

Automate the creation, formatting, and distribution of business reports from raw data sources using templates, scheduling, and delivery pipelines.

## Overview

Manual report generation is time-consuming, error-prone, and unsustainable at scale. This skill covers building automated reporting pipelines that pull data from sources, transform it into formatted reports (PDF, Excel, HTML, email), and deliver them on schedule to stakeholders. It addresses template systems, data processing, visualization embedding, and distribution automation across common technology stacks.

## Report Type Selection Guide

| Report Type | Format | Audience | Frequency | Automation Approach | Reference |
|-------------|--------|----------|-----------|-------------------|-----------|
| Executive dashboard | PDF or HTML email | C-suite | Weekly/Monthly | Template + data injection | `/references/template-systems.md` |
| Operational metrics | Excel with charts | Managers | Daily/Weekly | Data pull + Excel generation | `/references/data-processing.md` |
| Client deliverable | Branded PDF | External clients | Monthly/Quarterly | Template + branding layer | `/references/template-systems.md` |
| Ad-hoc analysis | Jupyter/HTML | Analysts | On-demand | Parameterized notebook | `/references/data-processing.md` |
| Compliance/audit | PDF with appendices | Regulators | Quarterly/Annual | Structured template + data | `/references/template-systems.md` |
| Email digest | HTML email | Team-wide | Daily | Data summary + email API | `/references/distribution-automation.md` |

## Automation Architecture

### Pipeline Components

| Component | Purpose | Tools/Technologies |
|-----------|---------|-------------------|
| Data source connector | Pull raw data | SQL queries, API calls, file imports |
| Data transformation | Clean, aggregate, calculate | Python (pandas), SQL, dbt |
| Template engine | Define report layout | Jinja2, LaTeX, DOCX templates, HTML/CSS |
| Visualization generator | Create charts and graphs | Matplotlib, Plotly, Chart.js, Excel charts |
| Report assembler | Combine data + template + visuals | WeasyPrint, ReportLab, python-docx, openpyxl |
| Distribution engine | Deliver to recipients | Email (SMTP/API), S3/SharePoint, Slack |
| Scheduler | Trigger on schedule | cron, Airflow, Celery, cloud schedulers |

### Pipeline Flow
```
Data Sources → Extract → Transform → Template Render → Format Output → Distribute
     ↓              ↓           ↓              ↓               ↓            ↓
  SQL/API      Validation   Aggregation   Jinja2/HTML     PDF/Excel    Email/S3
```

## Template System Design

### Template Technology Selection

| Technology | Output Format | Complexity | Best For | Reference |
|-----------|---------------|------------|----------|-----------|
| Jinja2 + HTML/CSS | HTML, PDF (via WeasyPrint) | Low–Medium | Web-style reports, email digests | `/references/template-systems.md` |
| python-docx | DOCX | Medium | Word document reports | `/references/template-systems.md` |
| openpyxl / XlsxWriter | XLSX | Medium | Excel reports with formulas | `/references/template-systems.md` |
| LaTeX | PDF | High | Academic, technical, compliance | `/references/template-systems.md` |
| ReportLab | PDF | Medium–High | Custom PDF layouts, watermarks | `/references/template-systems.md` |
| Google Slides API | PPTX/PDF | Medium | Presentation-format reports | `/references/template-systems.md` |

### Template Design Principles
- **Separate data from presentation** — templates should contain zero hardcoded values
- **Use placeholder variables** — `{{ total_revenue }}`, `{{ chart_image_path }}`
- **Include conditional sections** — `{% if monthly_churn > 5% %}⚠️ Alert{% endif %}`
- **Version control templates** — track changes to report format in git
- **Test with edge cases** — empty data, extreme values, missing fields

## Data Processing Patterns

| Pattern | Use Case | Implementation |
|---------|----------|---------------|
| Snapshot comparison | "This month vs. last month" | Pull current + previous period, compute deltas |
| Rolling aggregation | "Last 30 days average" | Window functions or date-filtered queries |
| Threshold alerting | "Highlight metrics above/below target" | Conditional formatting in template |
| Cohort grouping | "Performance by customer segment" | Group-by aggregation |
| Trend calculation | "MoM growth rate" | Percentage change formula |
| Top-N ranking | "Top 10 products by revenue" | Sort + limit in query |

### Data Validation Checklist
- ☐ Row counts match expected ranges
- ☐ No null values in required fields
- ☐ Dates fall within expected range
- ☐ Numerical values within reasonable bounds
- ☐ Totals reconcile with source system
- ☐ Previous period data available for comparison

## Visualization Integration

| Chart Type | When to Use | Python Library | Embedding Method |
|-----------|-------------|----------------|------------------|
| Line chart | Trends over time | Matplotlib, Plotly | Save as PNG, embed in HTML/PDF |
| Bar chart | Category comparison | Matplotlib, Altair | Save as PNG or SVG |
| KPI card | Single metric highlight | HTML/CSS template | Inline HTML |
| Table | Detailed data | pandas to_html(), tabulate | HTML table or Excel sheet |
| Heatmap | Correlation or density | Seaborn, Plotly | Save as image |
| Sparkline | Inline trend indicator | matplotlib (small figure) | Inline image |

## Distribution Automation

| Channel | Technology | Best For | Reference |
|---------|-----------|----------|-----------|
| Email (attachment) | SMTP, SendGrid, SES | PDF/Excel reports to executives | `/references/distribution-automation.md` |
| Email (inline HTML) | HTML email templates | Daily digests, alert summaries | `/references/distribution-automation.md` |
| Cloud storage | S3, Google Drive, SharePoint | Report archive, team access | `/references/distribution-automation.md` |
| Slack/Teams | Webhook or bot API | Team notifications with highlights | `/references/distribution-automation.md` |
| Web dashboard | Hosted HTML page | Self-serve, always-current view | `/references/distribution-automation.md` |
| Scheduled notebook | Papermill + Jupyter | Technical audiences, ad-hoc | `/references/data-processing.md` |

### Scheduling Options

| Tool | Environment | Cron-Like | Dependencies | Monitoring |
|------|-------------|-----------|-------------|------------|
| cron / systemd timer | Linux server | Yes | No | Log files |
| Airflow | Self-hosted or cloud | Yes | Yes (DAGs) | Web UI |
| Celery Beat | Python app | Yes | Via task chains | Flower UI |
| AWS EventBridge + Lambda | AWS | Yes | Step Functions | CloudWatch |
| GitHub Actions (scheduled) | GitHub | Yes | Workflow steps | Actions UI |
| Google Cloud Scheduler | GCP | Yes | Pub/Sub triggers | Cloud Monitoring |

## Error Handling and Monitoring

| Failure Point | Detection | Recovery |
|--------------|-----------|----------|
| Data source unavailable | Connection timeout | Retry with backoff, use cached data |
| Empty dataset | Row count check | Send "no data" report or skip |
| Template rendering error | Try-except block | Send error notification, attach logs |
| Distribution failure | Delivery receipt/API response | Retry, fall back to alternate channel |
| Stale report (scheduler missed) | Heartbeat monitoring | Alert ops team, manual trigger |

## Best Practices

- **Idempotent generation** — running the same report twice for the same period should produce identical output
- **Include metadata** — report footer should show generation timestamp, data freshness, and version
- **Test the full pipeline** — don't just test components; run end-to-end before deploying to production
- **Archive every generated report** — store in versioned cloud storage for audit trail
- **Separate config from code** — recipients, schedules, and thresholds should be in config files
- **Monitor delivery** — track email opens or file access to confirm reports are actually being read

## Using the Reference Files

**`/references/template-systems.md`** — Read when designing report templates. Covers Jinja2, python-docx, openpyxl, LaTeX, and HTML template patterns with code examples.

**`/references/data-processing.md`** — Read when building data extraction and transformation pipelines. Covers SQL patterns, pandas operations, validation checks, and snapshot comparison logic.

**`/references/visualization-design.md`** — Read when creating charts and visualizations for reports. Covers chart selection, styling, embedding, and automated chart generation.

**`/references/distribution-automation.md`** — Read when setting up report delivery. Covers email sending, cloud storage uploads, Slack notifications, scheduling, and monitoring.
