---
name: spreadsheet-analysis-manipulation
description: This skill transforms an agentic AI into a world-class spreadsheet expert capable of handling any spreadsheet task from basic cell operations to advanced automation, data modeling, and enterprise-level analytics.
---

---
name: Spreadsheet Analysis & Manipulation
description: A comprehensive spreadsheet expertise skill enabling expert-level operations across Excel, CSV, Google Sheets, and other formats, covering formulas, pivot tables, data visualization, automation, Power Query, Power Pivot, DAX, reporting, dashboards, and integration with external tools.
---

# Spreadsheet Analysis & Manipulation

## 1. Skill Description and Purpose

### Overview

This skill transforms an agentic AI into a world-class spreadsheet expert capable of handling any spreadsheet task from basic cell operations to advanced automation, data modeling, and enterprise-level analytics. The skill encompasses the complete spectrum of spreadsheet operations across multiple platforms including Microsoft Excel, Google Sheets, CSV/TSV files, and OpenDocument formats.

### Core Competencies

**Data Management & Operations**
- Complete workbook and worksheet lifecycle management including creation, organization, protection, and optimization
- Expert-level cell manipulation covering formatting, data entry, validation, and conditional formatting
- Advanced sorting, filtering, and data organization techniques for datasets of any size
- Format conversion between Excel (XLSX, XLSM, XLSB, XLS), CSV, TSV, ODS, and Google Sheets with full data integrity preservation

**Formula Mastery**
- Comprehensive knowledge of 400+ Excel/Google Sheets functions across mathematical, logical, lookup, text, date/time, statistical, financial, and database categories
- Dynamic array formulas (FILTER, SORT, UNIQUE, SEQUENCE, XLOOKUP) for modern Excel 365 environments
- Complex nested formula construction and optimization for performance
- Error handling with IFERROR, IFNA, and defensive formula design patterns

**Advanced Analytics**
- Pivot table creation, configuration, and optimization including calculated fields, grouping, and multi-level hierarchies
- Power Query (Get & Transform) for ETL operations including data import from 50+ source types, transformation steps, and M language scripting
- Power Pivot data modeling with DAX measures, calculated columns, and time intelligence functions
- Statistical analysis including regression, correlation, forecasting, and distribution analysis

**Visualization & Reporting**
- Chart creation across 20+ chart types with professional formatting and best practices
- Interactive dashboard development with slicers, timelines, and form controls
- Conditional formatting rules including data bars, color scales, icon sets, and custom formula-based rules
- Sparklines for in-cell trend visualization

**Automation & Integration**
- Excel VBA macro development for task automation, custom functions, and UserForms
- Google Apps Script for Google Sheets automation and integration with Google Workspace
- Python automation using pandas, openpyxl, and xlwings for programmatic spreadsheet manipulation
- Database connectivity (SQL Server, MySQL, PostgreSQL) and API integration for real-time data

### When to Use This Skill

Deploy this skill when tasks require:
- **Data Analysis**: Cleaning, transforming, aggregating, or analyzing structured tabular data
- **Financial Modeling**: Building financial models, forecasts, budgets, or scenario analyses
- **Reporting**: Creating automated reports, dashboards, or executive summaries
- **Data Integration**: Combining data from multiple sources (databases, APIs, files) into unified views
- **Automation**: Eliminating repetitive manual spreadsheet tasks through macros or scripts
- **Format Conversion**: Converting between spreadsheet formats while preserving data integrity
- **Troubleshooting**: Debugging formula errors, resolving circular references, or optimizing performance

### Value Proposition

This skill delivers:
- **Efficiency**: Automate hours of manual work into seconds of execution
- **Accuracy**: Eliminate human errors through validated formulas and automated processes
- **Scalability**: Handle datasets from hundreds to millions of rows with optimized techniques
- **Insight**: Transform raw data into actionable intelligence through analytics and visualization
- **Interoperability**: Seamlessly work across Excel, Google Sheets, and other platforms

---

## 2. Required Inputs/Parameters

### Primary Input: Spreadsheet Data Source

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `source_type` | enum | Yes | One of: `file_path`, `url`, `google_sheets_id`, `database_query`, `api_endpoint`, `raw_data` |
| `source_location` | string | Yes | File path, URL, spreadsheet ID, connection string, or API URL |
| `source_format` | enum | Conditional | File format: `xlsx`, `xls`, `xlsm`, `xlsb`, `csv`, `tsv`, `ods`, `google_sheets` |
| `encoding` | string | Optional | Character encoding for text files: `utf-8`, `utf-16`, `ascii`, `latin-1` (default: `utf-8`) |
| `delimiter` | string | Optional | For delimited files: `,`, `;`, `\t`, `|`, or custom (default: auto-detect) |
| `header_row` | integer | Optional | Row number containing column headers (default: 1, use 0 for no headers) |
| `data_range` | string | Optional | Specific range to process: `A1:Z100`, `Sheet1!A:D`, or named range |

### Operation Specification

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `operation_type` | enum | Yes | Primary operation category (see operation types below) |
| `operation_details` | object | Yes | Operation-specific parameters |
| `target_sheets` | array | Optional | List of sheet names/indices to operate on (default: all sheets) |
| `preserve_formatting` | boolean | Optional | Maintain original formatting during operations (default: true) |

**Operation Types:**
- `read`: Extract data, metadata, or structure information
- `write`: Create new files or overwrite existing content
- `transform`: Clean, reshape, aggregate, or pivot data
- `analyze`: Perform calculations, statistics, or modeling
- `visualize`: Create charts, conditional formatting, or dashboards
- `automate`: Generate macros, scripts, or scheduled processes
- `validate`: Check data quality, find errors, or audit formulas
- `convert`: Transform between formats or platforms

### Formula Operations Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `formula_type` | enum | Conditional | Function category: `mathematical`, `logical`, `lookup`, `text`, `date_time`, `statistical`, `financial`, `database`, `array`, `custom` |
| `formula_expression` | string | Conditional | Complete formula or formula template with placeholders |
| `apply_to_range` | string | Conditional | Target range for formula application |
| `array_formula` | boolean | Optional | Use dynamic array behavior (default: false) |
| `error_handling` | enum | Optional | Error strategy: `iferror_blank`, `iferror_zero`, `iferror_na`, `propagate`, `custom` |

### Pivot Table Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `source_range` | string | Conditional | Data range for pivot table source |
| `row_fields` | array | Conditional | Fields for row labels |
| `column_fields` | array | Optional | Fields for column labels |
| `value_fields` | array | Conditional | Fields and aggregations: `[{"field": "Sales", "aggregation": "sum"}]` |
| `filter_fields` | array | Optional | Fields for report filters |
| `grouping` | object | Optional | Grouping rules: `{"date_field": {"by": "month"}, "numeric_field": {"start": 0, "end": 100, "interval": 10}}` |
| `calculated_fields` | array | Optional | Custom calculations: `[{"name": "Margin", "formula": "Revenue - Cost"}]` |

### Visualization Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `chart_type` | enum | Conditional | Chart type: `column`, `bar`, `line`, `pie`, `scatter`, `area`, `combo`, `radar`, `bubble`, `waterfall`, `treemap`, `sunburst` |
| `data_range` | string | Conditional | Source data range for chart |
| `chart_title` | string | Optional | Chart title text |
| `axis_config` | object | Optional | Axis configuration: titles, min/max, formatting |
| `series_config` | array | Optional | Series-specific formatting and labels |
| `chart_style` | string | Optional | Predefined style template or custom styling object |
| `conditional_format_rules` | array | Optional | Rules for conditional formatting |

### Automation Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `automation_platform` | enum | Conditional | Target platform: `vba`, `apps_script`, `python`, `r` |
| `automation_task` | string | Conditional | Description of task to automate |
| `trigger_type` | enum | Optional | Trigger: `manual`, `on_open`, `on_edit`, `on_change`, `scheduled` |
| `schedule` | object | Optional | Schedule configuration for time-based triggers |
| `input_parameters` | array | Optional | Parameters the automation accepts |

### Output Configuration

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `output_format` | enum | Yes | Desired output format: `xlsx`, `xlsm`, `csv`, `json`, `html`, `pdf`, `google_sheets` |
| `output_location` | string | Yes | File path, Google Drive folder, or return type |
| `include_metadata` | boolean | Optional | Include operation metadata in output (default: false) |
| `compression` | boolean | Optional | Compress output file (default: false for single files) |

---

## 3. Expected Outputs/Deliverables

### Primary Output Types

**Processed Spreadsheet Files**
- Complete workbooks in requested format (XLSX, XLSM, CSV, etc.) with all transformations applied
- Preserved or enhanced formatting, formulas, and structure
- Optimized file size through removal of unused elements and efficient storage

**Data Extracts**
- Structured data in JSON, CSV, or array format for programmatic consumption
- Schema information including column names, data types, and statistics
- Filtered, aggregated, or transformed datasets ready for downstream processing

**Analysis Results**
- Statistical summaries with measures of central tendency, dispersion, and distribution
- Pivot table outputs with hierarchical aggregations and calculated metrics
- Forecast models with predictions, confidence intervals, and accuracy metrics

**Visualizations**
- Embedded charts within spreadsheet files with interactive elements
- Exported chart images (PNG, SVG, PDF) for standalone use
- Dashboard layouts with multiple coordinated visualizations

**Automation Artifacts**
- VBA modules (.bas files) or macro-enabled workbooks (.xlsm)
- Google Apps Script files with deployment configurations
- Python scripts with required dependencies documented
- Execution logs and error reports

### Output Quality Standards

**Data Integrity**
- 100% accuracy in numerical calculations verified through checksums
- Preservation of original data types unless explicitly transformed
- No data loss during format conversions with warnings for unsupported features
- Referential integrity maintained across linked ranges and external references

**Formula Quality**
- Optimized formula construction avoiding volatile functions where possible
- Error handling implemented for all lookup and division operations
- Named ranges used for clarity and maintainability
- Documentation comments for complex formula logic

**Visualization Standards**
- Consistent color schemes aligned with accessibility guidelines (WCAG 2.1 AA)
- Appropriate chart type selection based on data characteristics
- Clear axis labels, legends, and data labels without overlap
- Responsive layouts that maintain readability at different sizes

**Automation Quality**
- Well-commented code with clear function documentation
- Error handling with meaningful error messages
- Logging for debugging and audit trails
- Modular design for maintainability and reusability

### Deliverable Formats

| Deliverable | Format Options | Includes |
|-------------|----------------|----------|
| Processed Workbook | XLSX, XLSM, XLSB, XLS, ODS | Data, formulas, formatting, charts |
| Data Export | CSV, TSV, JSON, XML | Raw data with optional headers |
| Report | PDF, HTML | Formatted content, charts, tables |
| Dashboard | XLSX, HTML, Google Sheets | Interactive visualizations |
| Automation Code | VBA (.bas), JS (.gs), Python (.py) | Documented, tested code |
| Analysis Summary | Markdown, JSON | Statistics, insights, recommendations |

---

## 4. Example Use Cases

### Use Case 1: Financial Modeling and Analysis

**Scenario**: Build a comprehensive financial model for a startup seeking Series A funding, including historical analysis, projections, and scenario modeling.

**Input Requirements**:
- Historical financial data (3 years of income statements, balance sheets, cash flow statements)
- Industry benchmarks and growth assumptions
- Funding scenarios with different valuation and dilution parameters

**Execution Steps**:
1. **Data Import & Validation**: Import historical data from CSV exports, validate data types, check for missing values, reconcile across statements
2. **Structure Creation**: Build model architecture with separate sheets for Assumptions, Revenue Model, Cost Model, P&L, Balance Sheet, Cash Flow, Valuation
3. **Formula Development**: 
   - Revenue projections using `=GROWTH()` and custom growth rate assumptions
   - Cost modeling with fixed/variable breakdowns using `=IF()` conditions
   - Working capital calculations with `=AVERAGE()` of historical days outstanding
   - Cash flow from indirect method with `=SUM()` adjustments
4. **Scenario Analysis**: Implement Data Tables for sensitivity analysis on revenue growth and burn rate
5. **Valuation Calculations**: DCF model with `=NPV()`, `=XIRR()`, and comparable company multiples
6. **Visualization**: Create executive dashboard with key metrics, waterfall charts for value bridges, and scenario comparison charts

**Output**: Macro-enabled workbook (XLSM) with linked sheets, scenario manager, automated sensitivity tables, and investor-ready charts

### Use Case 2: Sales Data Analysis and Reporting

**Scenario**: Analyze 12 months of sales transaction data to identify trends, top performers, and opportunities for growth.

**Input Requirements**:
- Sales transaction log (100,000+ rows) with date, salesperson, product, region, quantity, revenue, cost
- Sales targets by region and product category
- Customer segmentation data

**Execution Steps**:
1. **Data Cleaning**: Remove duplicates with `=COUNTIF()` validation, standardize region names, parse dates with `=DATEVALUE()`
2. **Calculated Fields**: Add margin (`=Revenue-Cost`), margin % (`=Margin/Revenue`), quarter (`=ROUNDUP(MONTH(Date)/3,0)`)
3. **Pivot Analysis**:
   - Sales by Region and Month (matrix view)
   - Top 10 Products by Revenue with YoY comparison
   - Salesperson Performance vs Target
   - Customer Segment Contribution
4. **Trend Analysis**: Apply `=FORECAST.ETS()` for next quarter projections with seasonality detection
5. **Performance Dashboard**: Build interactive dashboard with:
   - Slicers for Region, Product Category, Time Period
   - KPI cards showing Revenue, Margin, YoY Growth
   - Combo chart with revenue bars and margin % line
   - Geographic heat map for regional performance

**Output**: Interactive Excel dashboard (XLSX) with pivot tables, charts, and executive summary sheet

### Use Case 3: Inventory Management and Tracking

**Scenario**: Create an automated inventory management system with reorder alerts, stock valuation, and supplier performance tracking.

**Input Requirements**:
- Current inventory levels by SKU and location
- Historical sales velocity data
- Supplier lead times and pricing
- Safety stock requirements

**Execution Steps**:
1. **Data Structure**: Create relational tables for Products, Suppliers, Inventory, Transactions, Reorder Points
2. **Formulas Implementation**:
   - Economic Order Quantity: `=SQRT((2*Annual_Demand*Order_Cost)/Holding_Cost)`
   - Reorder Point: `=Average_Daily_Sales*Lead_Time_Days+Safety_Stock`
   - Stock Valuation (FIFO): Nested `INDEX/MATCH` with cumulative quantity tracking
   - Days of Supply: `=Current_Stock/Average_Daily_Sales`
3. **Conditional Formatting**: 
   - Red highlight for items below reorder point
   - Yellow for items within 7 days of stockout
   - Data bars for stock level visualization
4. **Automation (VBA)**:
   ```vba
   Sub CheckReorderAlerts()
       Dim ws As Worksheet, rng As Range, cell As Range
       Set ws = ThisWorkbook.Sheets("Inventory")
       Set rng = ws.Range("F2:F" & ws.Cells(Rows.Count, 1).End(xlUp).Row)
       For Each cell In rng
           If cell.Value < cell.Offset(0, 1).Value Then
               SendReorderEmail cell.Offset(0, -5).Value, cell.Value
           End If
       Next cell
   End Sub
   ```
5. **Reporting**: Weekly inventory status report auto-generated and emailed

**Output**: Macro-enabled workbook with automated alerts, real-time stock tracking, and supplier scorecards

### Use Case 4: Marketing Campaign Performance Analysis

**Scenario**: Consolidate multi-channel marketing data to analyze campaign ROI, attribution, and optimize budget allocation.

**Input Requirements**:
- Campaign data from Google Ads, Facebook Ads, Email platforms (CSV exports)
- Website analytics with conversion tracking
- Revenue attribution data
- Budget allocations by channel

**Execution Steps**:
1. **Data Consolidation (Power Query)**:
   - Import and append data from multiple CSV sources
   - Standardize column names and date formats
   - Create calculated columns for derived metrics (CTR, CPC, CPA, ROAS)
   - Handle missing values and outliers
2. **Attribution Modeling**:
   - First-touch attribution using `=MINIFS()` for first campaign touchpoint
   - Last-touch with `=MAXIFS()` 
   - Linear attribution with equal credit distribution
   - Time-decay model with custom weighting formula
3. **Analysis Formulas**:
   - ROAS: `=Revenue/Ad_Spend`
   - Customer Acquisition Cost: `=Total_Spend/New_Customers`
   - Conversion Rate: `=Conversions/Clicks`
   - Incremental Revenue: A/B test calculations
4. **Budget Optimization**: Solver model to maximize conversions given budget constraints
5. **Dashboard Elements**:
   - Channel performance comparison (grouped bar chart)
   - Funnel visualization (impressions → clicks → conversions → revenue)
   - Time series with trend lines for key metrics
   - Attribution model comparison table

**Output**: Power Query-connected workbook with automated refresh, optimization model, and monthly reporting template

### Use Case 5: HR Analytics Dashboard

**Scenario**: Build a comprehensive HR analytics dashboard tracking headcount, turnover, diversity, compensation, and engagement metrics.

**Input Requirements**:
- Employee master data (demographics, department, hire date, salary, performance ratings)
- Historical headcount snapshots
- Survey response data
- Industry benchmarks

**Execution Steps**:
1. **Data Preparation**:
   - Calculate tenure: `=DATEDIF(Hire_Date, TODAY(), "Y")`
   - Age brackets: `=IFS(Age<30, "Under 30", Age<40, "30-39", Age<50, "40-49", TRUE, "50+")`
   - Turnover flags: Identify terminations within period
2. **Metric Calculations**:
   - Headcount trends with `=COUNTIFS()` by date ranges
   - Turnover rate: `=Terminations/Average_Headcount*100`
   - Diversity ratios by department and level
   - Compa-ratio: `=Salary/Midpoint`
   - Engagement scores with percentile rankings
3. **Advanced Analysis**:
   - Turnover prediction model using historical patterns
   - Salary equity analysis with regression (LINEST)
   - Flight risk scoring based on tenure, performance, and compensation
4. **Dashboard Design**:
   - Org health scorecard with traffic light indicators
   - Headcount waterfall chart (hires, terms, transfers)
   - Diversity dashboard with stacked bar charts
   - Compensation analysis scatter plot (salary vs performance)
   - Engagement heat map by department

**Output**: Protected HR dashboard with role-based access, automated monthly updates, and executive summary generator

---

## 5. Prerequisites and Dependencies

### Software Requirements

**Microsoft Excel**
- Excel 2016 or later for full feature compatibility (Power Query, Power Pivot)
- Excel 365 recommended for dynamic arrays (FILTER, SORT, UNIQUE, XLOOKUP)
- Enable "Power Pivot" add-in for data modeling features
- Enable "Developer" tab for macro development

**Google Sheets**
- Google account with Sheets access
- Apps Script editor access for automation
- Add-on installation permissions for extended functionality

**Python Environment** (for automation)
```
pandas>=1.5.0
openpyxl>=3.0.10
xlwings>=0.27.0 (Windows/Mac only)
xlrd>=2.0.1 (for legacy .xls files)
xlsxwriter>=3.0.3
```

**R Environment** (for automation)
```r
install.packages(c("readxl", "writexl", "openxlsx", "tidyverse"))
```

### Data Requirements

**Format Specifications**
- Excel files must be valid OOXML or BIFF format (not corrupted)
- CSV files should use consistent delimiters and encoding throughout
- Date formats must be parseable (ISO 8601 preferred: YYYY-MM-DD)
- Numeric data should not contain locale-specific formatting (commas in numbers)

**Data Quality Standards**
- Headers in first row (or specified header row)
- Consistent data types within columns
- No completely empty rows within data range
- Merged cells should be avoided in data regions

**Size Limitations**
- Excel: 1,048,576 rows × 16,384 columns per worksheet
- Google Sheets: 10 million cells per spreadsheet
- CSV: No inherent limits (memory-dependent)
- Power Query: 1 billion rows (performance degrades above 100 million)

### Access and Permissions

**File System Access**
- Read permission for source files
- Write permission for output directory
- Execute permission for automation scripts

**Cloud Services**
- Google Sheets: OAuth 2.0 authentication with appropriate scopes
- SharePoint/OneDrive: Microsoft Graph API credentials
- Database connections: Valid connection strings with credentials

**Network Requirements**
- Internet access for external data sources (APIs, web queries)
- Firewall allowance for database connections
- Proxy configuration if required

### Knowledge Dependencies

**Prerequisite Understanding**
- Basic spreadsheet concepts (cells, ranges, formulas, sheets)
- Data types (text, numbers, dates, booleans)
- Tabular data structure (rows as records, columns as fields)

**Recommended Background**
- SQL fundamentals for Power Query and database integration
- Basic statistics for analysis functions
- Programming basics for VBA/Apps Script automation
- Data modeling concepts for Power Pivot

### Tool-Specific Configuration

**Excel Settings**
- Calculation mode: Automatic (unless manual specified for performance)
- Macro security: Enable macros for trusted locations
- Add-ins: Power Query, Power Pivot, Solver, Analysis ToolPak

**Google Sheets Settings**
- Locale settings affect date/number formatting
- Apps Script: Enable Google Apps Script API in cloud console
- Triggers: Authorize trigger permissions for automation

**Environment Variables**
```bash
# For Python automation
EXCEL_PATH=/path/to/excel  # Excel installation (xlwings)
GOOGLE_APPLICATION_CREDENTIALS=/path/to/credentials.json

# For database connections
DB_HOST=server_address
DB_PORT=port_number
DB_USER=username
DB_PASSWORD=password
```

### Error Handling Protocols

**Common Error Recovery**
- Formula errors: Apply IFERROR wrappers with appropriate fallback values
- Missing data: Document handling strategy (skip, default value, interpolate)
- Type mismatches: Implement conversion with VALUE(), DATEVALUE(), TEXT()
- Circular references: Enable iterative calculation or restructure formulas

**Validation Checkpoints**
- Pre-processing: Validate input file integrity and format
- Mid-processing: Verify intermediate calculations with checksums
- Post-processing: Confirm output completeness and accuracy
- Cross-validation: Compare results against known benchmarks when available

---

*This skill enables comprehensive spreadsheet operations at an expert level, suitable for autonomous execution by Manus.im AI agents across financial, operational, analytical, and reporting tasks.*
