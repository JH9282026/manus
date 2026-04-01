---
name: spreadsheet-analysis-manipulation
description: "Analyze and manipulate data in spreadsheets using advanced formulas, pivot tables, and automation. Use for: data cleaning, complex formulas, VLOOKUP/INDEX-MATCH, pivot table analysis, conditional formatting, data validation, macro automation, Power Query, cross-sheet references, and dashboard creation in Excel and Google Sheets."
---

# Spreadsheet Analysis & Manipulation

Perform advanced data analysis, cleaning, and automation in Excel and Google Sheets using formulas, pivot tables, and scripting.

## Overview

Spreadsheets remain the most widely used data analysis tool in business. This skill covers advanced formula techniques, pivot table analysis, data cleaning workflows, automation with macros/Apps Script, and dashboard creation. It focuses on non-obvious techniques that go beyond basic spreadsheet use — the patterns that save hours of manual work and produce reliable, auditable analysis.

## Formula Selection Guide

| Task | Excel Formula | Google Sheets Formula | Reference |
|------|--------------|----------------------|-----------|
| Lookup value in table | `INDEX(MATCH())` or `XLOOKUP` | `INDEX(MATCH())` or `XLOOKUP` | `/references/advanced-formulas.md` |
| Conditional sum | `SUMIFS()` | `SUMIFS()` | `/references/advanced-formulas.md` |
| Conditional count | `COUNTIFS()` | `COUNTIFS()` | `/references/advanced-formulas.md` |
| Dynamic array filter | `FILTER()` | `FILTER()` | `/references/advanced-formulas.md` |
| Unique values | `UNIQUE()` | `UNIQUE()` | `/references/advanced-formulas.md` |
| Text extraction | `TEXTSPLIT()`, `LEFT/MID/RIGHT` | `SPLIT()`, `REGEXEXTRACT()` | `/references/advanced-formulas.md` |
| Date calculations | `NETWORKDAYS()`, `EDATE()` | `NETWORKDAYS()`, `EDATE()` | `/references/advanced-formulas.md` |
| Error handling | `IFERROR()`, `IFNA()` | `IFERROR()`, `IFNA()` | `/references/advanced-formulas.md` |
| Multi-condition logic | `IFS()`, `SWITCH()` | `IFS()`, `SWITCH()` | `/references/advanced-formulas.md` |
| Array manipulation | `SORT()`, `SORTBY()`, `SEQUENCE()` | `SORT()`, `SORTBY()`, `SEQUENCE()` | `/references/advanced-formulas.md` |

## Lookup Formula Decision Tree

| Scenario | Best Formula | Why |
|----------|-------------|-----|
| Simple left-to-right lookup | `XLOOKUP` (Excel 365+) | Replaces VLOOKUP, no column index needed |
| Lookup in any direction | `INDEX(MATCH())` | Works left, right, up, down |
| Multiple criteria lookup | `INDEX(MATCH(1,(A=X)*(B=Y),0))` (Ctrl+Shift+Enter) | Handles compound conditions |
| Return multiple results | `FILTER()` | Dynamic array, returns all matches |
| Approximate match (ranges) | `XLOOKUP(,,,,1)` or `VLOOKUP(,,TRUE)` | Tax brackets, commission tiers |
| Legacy compatibility | `VLOOKUP` | Works in all Excel versions |

## Data Cleaning Workflow

| Step | Operation | Formula/Tool | Common Issues Solved |
|------|-----------|-------------|---------------------|
| 1. Remove duplicates | Deduplicate rows | Data → Remove Duplicates / `UNIQUE()` | Repeated records |
| 2. Trim whitespace | Clean text fields | `TRIM()`, `CLEAN()` | Leading/trailing spaces breaking lookups |
| 3. Standardize text | Consistent case/format | `UPPER()`, `LOWER()`, `PROPER()` | Mixed case in categories |
| 4. Fix dates | Convert text to dates | `DATEVALUE()`, Text to Columns | Dates stored as text strings |
| 5. Handle blanks | Fill or flag empty cells | `IF(ISBLANK())`, Go To Special → Blanks | Missing data |
| 6. Validate data | Check ranges/formats | Data Validation rules | Invalid entries |
| 7. Split/combine fields | Parse or merge columns | `TEXTSPLIT()` / `TEXTJOIN()` | Combined name/address fields |
| 8. Type conversion | Ensure correct data types | Multiply by 1, `VALUE()`, `TEXT()` | Numbers stored as text |

## Pivot Table Analysis Framework

### Pivot Table Layout Decisions

| Analysis Type | Rows | Columns | Values | Filter |
|--------------|------|---------|--------|--------|
| Sales by region | Region, Sub-region | Quarter | Sum of Revenue | Year |
| Product performance | Product category | Month | Avg. of Units, Sum of Revenue | Region |
| Employee metrics | Department, Employee | — | Count, Average, Sum | Date range |
| Cohort analysis | Signup month | Activity month | Count of Users | Segment |
| Funnel analysis | Stage | — | Count, Conversion % (calculated) | Channel |

### Pivot Table Best Practices
- **Prepare source data:** one row per record, no merged cells, no blank rows, consistent headers
- **Use named tables** as source (Ctrl+T in Excel) — pivot auto-expands with new data
- **Add calculated fields** for derived metrics (e.g., Revenue per Unit = Revenue / Units)
- **Group dates** by month/quarter/year — don't pivot on raw dates
- **Show values as** — use "% of Column Total", "Running Total", or "Difference From" for insight
- **Refresh after data changes** — pivot tables don't auto-update (right-click → Refresh)

## Automation Approaches

| Approach | Platform | Complexity | Best For | Reference |
|----------|----------|-----------|----------|-----------|
| Excel Macros (VBA) | Excel desktop | Medium | Repetitive formatting, report generation | `/references/automation-scripting.md` |
| Google Apps Script | Google Sheets | Medium | Data import, email triggers, API calls | `/references/automation-scripting.md` |
| Power Query (M) | Excel 365/desktop | Medium | Data import, transformation, ETL | `/references/automation-scripting.md` |
| LAMBDA functions | Excel 365, Google Sheets | Low–Medium | Reusable custom formulas | `/references/advanced-formulas.md` |
| Office Scripts | Excel Online | Medium | Cloud-based automation | `/references/automation-scripting.md` |
| Named functions | Google Sheets | Low | Team-shared custom formulas | `/references/advanced-formulas.md` |

### Power Query Common Patterns
1. **Import and merge** — combine multiple files (CSVs, Excel workbooks) into one table
2. **Unpivot columns** — convert wide data to tall format for analysis
3. **Custom columns** — add calculated fields during transformation
4. **Group and aggregate** — summarize before loading to sheet
5. **Append queries** — stack datasets from multiple sources

## Dashboard Design in Spreadsheets

| Component | Chart Type | When to Use |
|-----------|-----------|-------------|
| KPI summary | Single number + sparkline | Highlight 3–5 key metrics |
| Trend over time | Line chart | Show progression |
| Composition | Stacked bar or pie (≤5 segments) | Show parts of whole |
| Comparison | Clustered bar chart | Compare categories |
| Distribution | Histogram | Show data spread |
| Interactive filter | Data validation dropdown + FILTER() | Let users slice data |

## Best Practices

- **Use structured tables** (Ctrl+T) — they auto-expand, have named references, and work with pivots
- **Never hardcode values** — put assumptions in labeled cells and reference them
- **Use named ranges** for important references — `=Revenue_Target` is clearer than `=$B$2`
- **Protect formulas** — lock formula cells and only allow input in data entry cells
- **Document your logic** — add a "Notes" sheet explaining assumptions and data sources
- **Version your files** — save dated copies before major changes; use Track Changes for collaboration

## Using the Reference Files

**`/references/advanced-formulas.md`** — Read when building complex formulas. Covers XLOOKUP, dynamic arrays, array formulas, LAMBDA functions, and text manipulation patterns.

**`/references/pivot-analysis.md`** — Read when building pivot tables or analyzing summarized data. Covers layout strategies, calculated fields, grouping, slicers, and pivot chart creation.

**`/references/data-visualization.md`** — Read when creating charts or dashboards. Covers chart selection, formatting, conditional formatting, sparklines, and interactive dashboard design.

**`/references/automation-scripting.md`** — Read when automating repetitive tasks. Covers VBA macros, Google Apps Script, Power Query, and Office Scripts with practical code examples.
