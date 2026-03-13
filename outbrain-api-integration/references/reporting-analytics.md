# Outbrain Reporting & Analytics

API endpoints for performance data.

## Performance Reports

**Periodic Content Report:**
```bash
GET /reports/marketers/{marketer_id}/periodicContent
```

**Query Parameters:**
- `from`: Start date (YYYY-MM-DD)
- `to`: End date (YYYY-MM-DD)
- `breakdown`: Dimension (DAILY, CAMPAIGN, CONTENT)
- `limit`: Number of results
- `offset`: Pagination

**Example:**
```bash
GET /reports/marketers/123/periodicContent?from=2026-03-01&to=2026-03-13&breakdown=DAILY
```

**Response:**
```json
{
  "results": [
    {
      "date": "2026-03-01",
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

## Campaign Performance

**Campaign Report:**
```bash
GET /reports/marketers/{marketer_id}/campaigns/{campaign_id}
```

Returns performance metrics for specific campaign.

## Promoted Link Performance

**Content Report:**
```bash
GET /reports/campaigns/{campaign_id}/promotedLinks
```

Returns performance by promoted link.

## Realtime Performance

**Realtime Report:**
```bash
GET /reports/marketers/{marketer_id}/realtime
```

Returns real-time performance data (last 24 hours).

## Key Metrics

- **Impressions**: Ad views
- **Clicks**: User clicks
- **CTR**: Click-through rate
- **Spent**: Total spend
- **CPC**: Cost per click
- **Conversions**: Conversion events
- **CPA**: Cost per acquisition
- **Engagement**: Time on site, pages viewed

## Report Breakdowns

- **DAILY**: Performance by day
- **CAMPAIGN**: Performance by campaign
- **CONTENT**: Performance by promoted link
- **PUBLISHER**: Performance by publisher
- **GEO**: Performance by country

## Rate Limits

- Performance API: 10 requests/minute per marketer
- Realtime API: 50 requests/minute per marketer

## Data Export

Use reports for:
- Performance dashboards
- Data warehouse integration
- Automated optimization
- Custom analytics
- ROI tracking
