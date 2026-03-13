# Taboola Campaign Operations

API operations for campaign management.

## List Campaigns

```bash
GET /{account_id}/campaigns/
```

**Query Parameters:**
- `is_active`: Filter by status (true/false)
- `approval_state`: APPROVED, PENDING, REJECTED

## Create Campaign

```bash
POST /{account_id}/campaigns/
```

**Request Body:**
```json
{
  "name": "Campaign Name",
  "branding_text": "Brand Name",
  "pricing_model": "CPC",
  "cpc": 0.50,
  "daily_cap": 100.00,
  "spending_limit": 3000.00,
  "bid_strategy": "FIXED",
  "country_targeting": {
    "type": "INCLUDE",
    "value": ["US", "CA"]
  }
}
```

## Update Campaign

```bash
PUT /{account_id}/campaigns/{campaign_id}
```

**Partial Update:**
```bash
PATCH /{account_id}/campaigns/{campaign_id}
```

## Bulk Operations

**Bulk Update:**
```bash
POST /{account_id}/campaigns/mass-update
```

```json
{
  "campaign_ids": ["123", "456"],
  "update": {
    "daily_cap": 150.00
  }
}
```

**Duplicate Campaign:**
```bash
POST /{account_id}/campaigns/{id}/duplicate
```

## Targeting Configuration

**Update Geographic Targeting:**
```json
{
  "country_targeting": {
    "type": "INCLUDE",
    "value": ["US", "GB", "CA"]
  }
}
```

**Update Platform Targeting:**
```json
{
  "platform_targeting": {
    "type": "INCLUDE",
    "value": ["DESK", "PHON"]
  }
}
```
