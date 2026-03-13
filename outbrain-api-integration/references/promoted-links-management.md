# Outbrain Promoted Links Management

API operations for promoted links (ads).

## List Promoted Links

```bash
GET /campaigns/{campaign_id}/promotedLinks
```

**Query Parameters:**
- `enabled`: Filter by status
- `limit`: Number of results
- `offset`: Pagination offset

## Get Promoted Link

```bash
GET /promotedLinks/{promoted_link_id}
```

## Create Promoted Link

```bash
POST /campaigns/{campaign_id}/promotedLinks
```

**Request Body:**
```json
{
  "url": "https://example.com/article",
  "text": "Compelling Headline Text",
  "imageUrl": "https://cdn.example.com/image.jpg",
  "enabled": true,
  "cpc": 0.50
}
```

**Fields:**
- `url`: Landing page URL (required)
- `text`: Headline, max 100 characters (required)
- `imageUrl`: Thumbnail image URL (required)
- `enabled`: Active status (default: true)
- `cpc`: Cost per click bid (optional)

## Update Promoted Link

```bash
PUT /promotedLinks/{promoted_link_id}
```

**Update Headline:**
```json
{
  "text": "New Headline Text"
}
```

**Pause Promoted Link:**
```json
{
  "enabled": false
}
```

## Bulk Operations

**Create Multiple Promoted Links:**
```bash
POST /campaigns/{campaign_id}/promotedLinks/bulk
```

**Request Body:**
```json
{
  "promotedLinks": [
    {
      "url": "https://example.com/page1",
      "text": "Headline 1",
      "imageUrl": "https://cdn.example.com/img1.jpg"
    },
    {
      "url": "https://example.com/page2",
      "text": "Headline 2",
      "imageUrl": "https://cdn.example.com/img2.jpg"
    }
  ]
}
```

## Image Requirements

- Format: JPG, PNG
- Size: 1200x800px recommended
- File size: Under 5MB
- Aspect ratio: 3:2 or 16:9

## Best Practices

- Test multiple headlines per URL
- Use high-quality images
- Monitor performance and pause low performers
- Refresh creatives regularly
- Follow Outbrain editorial guidelines
