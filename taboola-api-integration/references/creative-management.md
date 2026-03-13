# Taboola Creative Management

API operations for Items and Motion Ads.

## List Items

```bash
GET /{account_id}/campaigns/{campaign_id}/items/
```

## Create Item

```bash
POST /{account_id}/campaigns/{campaign_id}/items/
```

**Request Body:**
```json
{
  "url": "https://example.com/landing",
  "thumbnail_url": "https://cdn.example.com/image.jpg",
  "title": "Compelling Headline",
  "description": "Additional description text",
  "cta": "Learn More",
  "is_active": true
}
```

## Bulk Create Items

```bash
POST /{account_id}/campaigns/{campaign_id}/items/mass-create
```

**Request Body:**
```json
{
  "items": [
    {
      "url": "https://example.com/page1",
      "thumbnail_url": "https://cdn.example.com/img1.jpg",
      "title": "Headline 1"
    },
    {
      "url": "https://example.com/page2",
      "thumbnail_url": "https://cdn.example.com/img2.jpg",
      "title": "Headline 2"
    }
  ]
}
```

## Update Item

```bash
PUT /{account_id}/campaigns/{campaign_id}/items/{item_id}
```

**Pause Item:**
```json
{
  "is_active": false
}
```

## Motion Ads

**Create Motion Ad:**
```bash
POST /{account_id}/campaigns/{campaign_id}/motion-ads/
```

**Request Body:**
```json
{
  "url": "https://example.com/landing",
  "title": "Video Ad Title",
  "video_url": "https://cdn.example.com/video.mp4",
  "fallback_url": "https://cdn.example.com/fallback.jpg"
}
```

## Bulk Operations

**Bulk Update:**
```bash
POST /{account_id}/campaigns/{campaign_id}/items/mass-update
```

**Bulk Delete:**
```bash
POST /{account_id}/campaigns/{campaign_id}/items/mass-delete
```
