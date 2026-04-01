---
name: power-bi-dashboards
description: "Build interactive business intelligence dashboards with Microsoft Power BI. Use for: data modeling, DAX calculations, report design, dashboard creation, Power Query transformations, data refresh scheduling, sharing and collaboration, mobile optimization, custom visuals, row-level security, and integration with Microsoft ecosystem."
---

# Power BI Dashboards

Create interactive business intelligence dashboards and reports using Microsoft Power BI.

## Overview

Power BI is Microsoft's business analytics platform providing interactive visualizations and self-service BI capabilities. This skill covers the complete workflow from data connection and modeling through report creation, dashboard design, and publishing to Power BI Service for collaboration and sharing.

## Power BI Components

### Power BI Desktop

Desktop application for creating reports and data models:
- Connect to data sources
- Transform data with Power Query
- Build data models and relationships
- Create DAX measures and calculated columns
- Design report pages and visualizations

### Power BI Service

Cloud-based platform for sharing and collaboration:
- Publish and share reports and dashboards
- Schedule data refreshes
- Create workspaces for team collaboration
- Set up row-level security
- Configure alerts and subscriptions

### Power BI Mobile

Mobile apps for iOS, Android, and Windows for on-the-go access to dashboards and reports.

## Data Connection and Preparation

### Data Sources

**Files**: Excel, CSV, JSON, XML, PDF, Parquet
**Databases**: SQL Server, Oracle, MySQL, PostgreSQL, Teradata
**Cloud**: Azure SQL, Snowflake, Amazon Redshift, Google BigQuery
**Online Services**: SharePoint, Dynamics 365, Salesforce, Google Analytics
**Other**: Web APIs, OData feeds, R/Python scripts

### Import vs DirectQuery vs Live Connection

| Mode | Description | Use Case |
|------|-------------|----------|
| Import | Data copied into Power BI | Best performance, scheduled refresh |
| DirectQuery | Query data source in real-time | Real-time data, large datasets |
| Live Connection | Connect to Analysis Services | Enterprise semantic models |
| Composite | Mix of Import and DirectQuery | Hybrid scenarios |

### Power Query (M Language)

**Common Transformations**:
- Remove/keep columns
- Filter rows
- Change data types
- Split columns
- Merge queries (joins)
- Append queries (union)
- Pivot/unpivot columns
- Group by and aggregate
- Add custom columns
- Replace values

**Example M Code**:
```m
let
    Source = Excel.Workbook(File.Contents("C:\\Data\\Sales.xlsx")),
    SalesTable = Source{[Name="Sales"]}[Data],
    ChangedType = Table.TransformColumnTypes(SalesTable, {
        {"Date", type date},
        {"Amount", type number}
    }),
    FilteredRows = Table.SelectRows(ChangedType, each [Date] >= #date(2026,1,1)),
    AddedColumn = Table.AddColumn(FilteredRows, "Year", each Date.Year([Date]))
in
    AddedColumn
```

## Data Modeling

### Relationships

**Relationship Types**:
- One-to-Many (most common)
- Many-to-One
- One-to-One
- Many-to-Many (use with caution)

**Cardinality and Cross-Filter Direction**:
- Single direction (default, better performance)
- Both directions (use sparingly, can cause ambiguity)

**Best Practices**:
- Create star schema (fact tables surrounded by dimension tables)
- Use integer keys for relationships
- Avoid bidirectional filters when possible
- Hide foreign key columns from report view

### Calculated Columns vs Measures

**Calculated Columns** (computed row-by-row, stored in model):
```dax
Full Name = [First Name] & " " & [Last Name]
Age = DATEDIFF([Birth Date], TODAY(), YEAR)
```

**Measures** (computed at query time, not stored):
```dax
Total Sales = SUM(Sales[Amount])
Average Order Value = DIVIDE([Total Sales], [Order Count], 0)
```

**When to Use**:
- Calculated Columns: Filtering, grouping, static calculations
- Measures: Aggregations, dynamic calculations, better performance

## DAX (Data Analysis Expressions)

### Basic DAX Functions

**Aggregation**:
```dax
Total Revenue = SUM(Sales[Revenue])
Average Price = AVERAGE(Products[Price])
Min Date = MIN(Orders[Order Date])
Max Date = MAX(Orders[Order Date])
Count Rows = COUNTROWS(Sales)
Distinct Customers = DISTINCTCOUNT(Sales[Customer ID])
```

**Logical**:
```dax
Customer Segment = 
IF(
    [Total Sales] > 10000, "VIP",
    IF([Total Sales] > 5000, "Premium", "Standard")
)

Is High Value = [Total Sales] > 10000
```

**Filter Context**:
```dax
Sales Last Year = CALCULATE(
    [Total Sales],
    SAMEPERIODLASTYEAR('Date'[Date])
)

Sales for Product A = CALCULATE(
    [Total Sales],
    Products[Product Name] = "Product A"
)
```

### Time Intelligence

```dax
YTD Sales = TOTALYTD([Total Sales], 'Date'[Date])
MTD Sales = TOTALMTD([Total Sales], 'Date'[Date])
QTD Sales = TOTALQTD([Total Sales], 'Date'[Date])

Sales Previous Month = CALCULATE(
    [Total Sales],
    PREVIOUSMONTH('Date'[Date])
)

Sales Growth = 
DIVIDE(
    [Total Sales] - [Sales Last Year],
    [Sales Last Year],
    0
)
```

### Advanced DAX Patterns

**CALCULATE with Multiple Filters**:
```dax
High Value Recent Sales = 
CALCULATE(
    [Total Sales],
    Sales[Amount] > 1000,
    Sales[Date] >= DATE(2026, 1, 1)
)
```

**FILTER Function**:
```dax
Sales Above Average = 
CALCULATE(
    [Total Sales],
    FILTER(
        Sales,
        Sales[Amount] > [Average Order Value]
    )
)
```

**ALL, ALLEXCEPT, ALLSELECTED**:
```dax
% of Total Sales = 
DIVIDE(
    [Total Sales],
    CALCULATE([Total Sales], ALL(Products))
)

% of Category Sales = 
DIVIDE(
    [Total Sales],
    CALCULATE([Total Sales], ALLEXCEPT(Products, Products[Category]))
)
```

**RANKX**:
```dax
Product Rank = 
RANKX(
    ALL(Products[Product Name]),
    [Total Sales],
    ,
    DESC,
    DENSE
)
```

**Variables**:
```dax
Profit Margin % = 
VAR TotalRevenue = [Total Revenue]
VAR TotalCost = [Total Cost]
VAR Profit = TotalRevenue - TotalCost
RETURN
    DIVIDE(Profit, TotalRevenue, 0)
```

## Visualizations

### Standard Visuals

| Visual | Use Case |
|--------|----------|
| Bar/Column Chart | Compare categories |
| Line Chart | Trends over time |
| Pie/Donut Chart | Part-to-whole (use sparingly) |
| Table/Matrix | Detailed data, cross-tabulation |
| Card | Single KPI value |
| Multi-row Card | Multiple KPIs |
| Gauge | Progress toward goal |
| KPI | Actual vs target with trend |
| Slicer | Interactive filtering |
| Map | Geographic data |
| Scatter Chart | Correlation between measures |
| Treemap | Hierarchical part-to-whole |
| Waterfall | Cumulative effect |
| Funnel | Sequential process stages |

### Custom Visuals

Import from AppSource or create custom visuals using Power BI Visuals SDK.

**Popular Custom Visuals**:
- Chiclet Slicer
- Text Filter
- Hierarchy Slicer
- Sankey Diagram
- Word Cloud
- Gantt Chart
- Bullet Chart

### Formatting Best Practices

- Use consistent color scheme aligned with brand
- Limit colors to 5-7 for categorical data
- Use sequential colors for ordered data
- Ensure sufficient contrast for accessibility
- Add data labels only when necessary
- Use tooltips for additional context
- Keep titles clear and descriptive

## Dashboard Design

### Dashboard vs Report

**Report**: Multi-page detailed analysis with multiple visuals
**Dashboard**: Single-page overview with tiles from multiple reports

### Creating Dashboards

1. Publish reports to Power BI Service
2. Pin visuals or entire report pages to dashboard
3. Add tiles from other sources (web content, images, text, video)
4. Arrange and resize tiles
5. Configure tile details and custom links

### Design Principles

**Visual Hierarchy**:
- Most important metrics in top-left
- Use size to emphasize importance
- Group related metrics
- Maintain consistent spacing

**Interactivity**:
- Use slicers for filtering
- Enable cross-filtering between visuals
- Add drill-through pages for details
- Configure bookmarks for different views

**Mobile Layout**:
- Create optimized phone layout
- Prioritize key metrics
- Use vertical scrolling
- Test on actual devices

## Advanced Features

### Row-Level Security (RLS)

Define roles to restrict data access:
```dax
[Region] = USERNAME()
[SalesRep] = USERPRINCIPALNAME()
```

### Parameters

**What-If Parameters**: Create scenarios with adjustable values
**Field Parameters**: Dynamic measure/dimension selection

### Dataflows

Reusable ETL logic shared across workspaces:
- Create once, use in multiple datasets
- Centralize data preparation
- Improve governance and consistency

### Paginated Reports

Pixel-perfect reports for printing and PDF export:
- Multi-page reports
- Precise layout control
- Optimized for printing
- Parameter-driven

### Deployment Pipelines

Development > Test > Production workflow for enterprise deployments.

## Performance Optimization

### Data Model Optimization

- Use star schema design
- Remove unnecessary columns
- Use appropriate data types (integers for IDs)
- Avoid calculated columns when measures suffice
- Disable auto date/time hierarchy if not needed
- Use incremental refresh for large tables

### DAX Optimization

- Use variables to avoid recalculation
- Prefer DIVIDE over division operator (handles divide by zero)
- Use SELECTEDVALUE instead of VALUES when expecting single value
- Avoid iterators (SUMX, FILTER) when possible
- Use KEEPFILTERS for additive filters

### Visual Optimization

- Limit visuals per page (6-8 maximum)
- Reduce data points displayed
- Use aggregated data when possible
- Disable interactions between unrelated visuals
- Use bookmarks instead of multiple pages

## Sharing and Collaboration

### Workspaces

- Create workspaces for team collaboration
- Assign roles: Admin, Member, Contributor, Viewer
- Organize content by project or department

### Sharing Options

**Share Dashboard/Report**: Grant access to specific users
**Publish to Web**: Public embedding (no authentication)
**Embed in SharePoint**: Integrate with SharePoint Online
**Embed in Teams**: Add reports to Teams channels
**Embed in Apps**: Use Power BI Embedded for custom applications

### Subscriptions and Alerts

**Subscriptions**: Email snapshots on schedule
**Data Alerts**: Notifications when metrics cross thresholds (dashboards only)

## Integration with Microsoft Ecosystem

### Excel

- Analyze in Excel: Use PivotTables with Power BI datasets
- Export data from visuals to Excel
- Publish Excel workbooks to Power BI

### Teams

- Add Power BI tab to Teams channels
- Share reports in Teams conversations
- Collaborate on reports within Teams

### Power Automate

- Trigger flows based on data alerts
- Export and distribute reports automatically
- Refresh datasets via API

### Azure

- Azure Analysis Services for enterprise models
- Azure Data Lake for data storage
- Azure Synapse Analytics integration

## Best Practices

### Development Workflow

1. Plan data model and requirements
2. Connect and transform data in Power Query
3. Build relationships and data model
4. Create measures and calculations
5. Design report pages
6. Test and validate
7. Publish to Power BI Service
8. Configure refresh and security
9. Share with stakeholders

### Governance

- Establish naming conventions
- Document data sources and transformations
- Implement version control for PBIX files
- Define certification process for datasets
- Monitor usage and performance
- Provide training and support

## Using the Reference Files

### When to Read Each Reference

**`/references/dax-patterns.md`** — Read when creating complex DAX measures, time intelligence calculations, or advanced analytical patterns.

**`/references/data-modeling-guide.md`** — Read when designing data models, optimizing relationships, or implementing star schema architecture.

**`/references/visualization-best-practices.md`** — Read when designing reports and dashboards, selecting appropriate visuals, or optimizing user experience.

## References

- [Data Modeling Guide](references/data-modeling-guide.md)
- [Dax Patterns](references/dax-patterns.md)
- [Visualization Best Practices](references/visualization-best-practices.md)
