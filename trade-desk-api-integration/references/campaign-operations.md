# The Trade Desk Campaign Operations

API operations for campaign and ad group management.

## Get Campaign

```bash
GET /campaign/{campaignId}
```

Returns full campaign object with all settings.

## Create Campaign

```bash
POST /advertiser/{advertiserId}/campaign
```

**Request Body:**
```json
{
  "CampaignName": "Q1 Campaign",
  "Budget": {
    "Amount": 10000.00,
    "CurrencyCode": "USD"
  },
  "StartDate": "2026-03-01T00:00:00Z",
  "EndDate": "2026-03-31T23:59:59Z",
  "CampaignConversionReportingColumns": [
    {
      "ColumnId": "conversion_id_1"
    }
  ]
}
```

## Update Campaign

```bash
PUT /campaign/{campaignId}
```

**Update Budget:**
```json
{
  "Budget": {
    "Amount": 15000.00
  }
}
```

## Get Ad Group

```bash
GET /adgroup/{adGroupId}
```

Returns ad group configuration including targeting and bidding.

## Create Ad Group

```bash
POST /campaign/{campaignId}/adgroup
```

**Request Body:**
```json
{
  "AdGroupName": "Desktop Display",
  "Budget": {
    "Amount": 5000.00
  },
  "BaseBidCPM": 2.50,
  "MaxBidCPM": 10.00,
  "RTBAttributes": {
    "DeviceTargeting": ["Desktop"],
    "GeoTargeting": {
      "IncludeGeos": ["US", "CA"]
    }
  }
}
```

## Update Ad Group

```bash
PUT /adgroup/{adGroupId}
```

**Update Bid:**
```json
{
  "BaseBidCPM": 3.00,
  "MaxBidCPM": 12.00
}
```

## Automation Tips

**Get Syntax for Replication:**
- Use `GET /campaign/{campaignId}` to retrieve full syntax
- Use `GET /adgroup/{adGroupId}` for ad group syntax
- Copy structure for `POST` operations

**Default Settings:**
- Indicate IO CPM as Flat Free Rate
- Load impressions with buffers
- Apply default rails (brand safety, device, fraud, geo, OS)

**Bulk Operations:**
- Create multiple campaigns/ad groups programmatically
- Use loops for scaling
- Implement error handling for each operation
