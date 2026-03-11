# Census Data Methods and Sources

## U.S. Census Geographic Hierarchy

Understanding census geography is essential for demographic research:

```
Nation
  └── Region (4)
       └── Division (9)
            └── State (50 + DC)
                 └── County (3,143)
                      └── Census Tract (~74,000)
                           └── Block Group (~220,000)
                                └── Block (~11 million)
```

### Geographic Units for Analysis

| Unit | Population Range | Best For |
|---|---|---|
| Metropolitan Statistical Area (MSA) | 50K+ | Regional market analysis |
| County | Varies widely | Local planning |
| Census Tract | 1,200–8,000 | Neighborhood-level analysis |
| Block Group | 600–3,000 | Fine-grained segmentation |
| ZIP Code Tabulation Area (ZCTA) | Varies | Marketing, retail analysis |

---

## American Community Survey (ACS)

### 1-Year vs 5-Year Estimates

| Feature | 1-Year | 5-Year |
|---|---|---|
| Sample size | ~3.5 million | ~15 million |
| Geographic coverage | 65K+ population | All geographies |
| Currency | Most recent | 5-year average |
| Reliability | Higher MOE | Lower MOE |
| Best for | Large areas, recent data | Small areas, precision |

### Margins of Error

- All ACS estimates have associated margins of error (MOE)
- Calculate confidence intervals: estimate ± MOE (90% CI)
- For derived estimates, propagate errors using variance formulas
- Small-area estimates may have MOE exceeding 50% of the estimate — flag and caveat
- Use coefficient of variation (CV = MOE/1.645 ÷ Estimate) to assess reliability
  - CV < 15%: Reliable
  - CV 15-30%: Use with caution
  - CV > 30%: Unreliable for most purposes

---

## Census Data Access Methods

### Census Bureau API
- Base URL: `https://api.census.gov/data/`
- Request API key (free) for higher rate limits
- Specify year, dataset, variables, geography
- Returns JSON format

### data.census.gov
- Interactive web interface for exploring census tables
- Search by topic, table ID, or keyword
- Download in CSV/Excel format
- Provides pre-formatted profiles

### IPUMS (Integrated Public Use Microdata Series)
- Harmonized microdata across census years
- Enables custom tabulations not available in published tables
- Supports longitudinal analysis across decades
- Academic and research applications

---

## Data Quality Considerations

1. **Undercounts**: Census historically undercounts minorities, renters, young adults, and homeless populations
2. **Differential privacy**: 2020 Census introduced noise injection for privacy, affecting small-area data
3. **Response rates**: Declining response rates reduce estimate reliability
4. **Vintage timing**: ACS data reflects collection period, not publication date
5. **Boundary changes**: Geographic boundaries change over time; use crosswalk files for longitudinal analysis
