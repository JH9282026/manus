# Outbrain Campaign Operations

API operations for campaign management.

## List Marketers

```bash
GET /marketers
```

Returns list of marketer accounts you have access to.

## List Campaigns

```bash
GET /marketers/{marketer_id}/campaigns
```

**Query Parameters:**
- `enabled`: Filter by status (true/false)
- `includeArchived`: Include archived campaigns

## Get Campaign

```bash
GET /campaigns/{campaign_id}
```

## Create Campaign

```bash
POST /marketers/{marketer_id}/campaigns
```

**Request Body:**
```json
{
  "name": "Campaign Name",
  "enabled": true,
  "budgetId": "budget_123",
  "targeting": {
    "platform": ["DESKTOP", "MOBILE"],
    "locations": ["US", "CA"]
  }
}
```

## Update Campaign

```bash
PUT /campaigns/{campaign_id}
```

**Request Body:**
```json
{
  "name": "Updated Campaign Name",
  "enabled": false
}
```

## Budget Management

**List Budgets:**
```bash
GET /marketers/{marketer_id}/budgets
```

**Create Budget:**
```bash
POST /marketers/{marketer_id}/budgets
```

**Request Body:**
```json
{
  "name": "Budget Name",
  "amount": 1000.00,
  "type": "MONTHLY",
  "currency": "USD"
}
```

## Campaign Targeting

**Update Targeting:**
```bash
PUT /campaigns/{campaign_id}
```

**Targeting Options:**
```json
{
  "targeting": {
    "platform": ["DESKTOP", "MOBILE", "TABLET"],
    "locations": ["US", "GB", "CA"],
    "publishers": ["publisher_id_1", "publisher_id_2"]
  }
}
```
