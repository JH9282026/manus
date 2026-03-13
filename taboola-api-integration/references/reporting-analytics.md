# Taboola Reporting & Analytics

API endpoints for performance data.

## Campaign Summary Report

```bash
GET /{account_id}/reports/campaign-summary/dimensions/{dimension}
```

**Dimensions:**
- `campaign_day_breakdown` - Daily performance
- `campaign_site_breakdown` - By publisher
- `campaign_country_breakdown` - By country
- `campaign_platform_breakdown` - By platform

**Query Parameters:**
- `start_date`: YYYY-MM-DD
- `end_date`: YYYY-MM-DD
- `campaign`: Campaign ID filter

**Example:**
```bash
GET /{account_id}/reports/campaign-summary/dimensions/campaign_day_breakdown?start_date=2026-03-01&end_date=2026-03-13&campaign=123456
```

**Response:**
```json
{
  "results": [
    {
      "date": "2026-03-01",
      "campaign": "123456",
      "impressions": 10000,
      "clicks": 50,
      "ctr": 0.005,
      "spent": 25.00,
      "cpc": 0.50,
      "conversions": 2,
      "cpa": 12.50
    }
  ]
}
```

## Top Campaign Content Report

```bash
GET /{account_id}/reports/top-campaign-content/dimensions/item_breakdown
```

Returns performance by creative (Item or Motion Ad).

## Realtime Reports

**Realtime Campaign Report:**
```bash
GET /{account_id}/reports/realtime-campaign/dimensions/{dimension}
```

**Dimensions:**
- `campaign` - By campaign
- `site` - By publisher
- `country` - By country

**Realtime Ads Report:**
```bash
GET /{account_id}/reports/realtime-ads/dimensions/item
```

Returns real-time performance by creative.

## Key Metrics

- **Impressions**: Ad views
- **Clicks**: User clicks
- **CTR**: Click-through rate
- **Spent**: Total spend
- **CPC**: Cost per click
- **Conversions**: Conversion events
- **CPA**: Cost per acquisition
- **ROAS**: Return on ad spend

## Data Export

Use reports for:
- Performance dashboards
- Data warehouse integration
- Automated optimization
- Custom analytics
