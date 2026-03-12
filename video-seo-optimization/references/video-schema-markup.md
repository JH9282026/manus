# Video Schema Markup

Detailed reference content for the Video Seo Optimization skill.

---

## Video Schema Markup


### What Is Video Schema?

Schema markup is structured data that helps search engines understand video content:
- Enables rich snippets in search results
- Provides video details (duration, thumbnail, upload date)
- Helps Google index video content properly


### Implementing Video Schema

**Required Properties**:
- `name`: Video title
- `description`: Video description
- `thumbnailUrl`: Thumbnail image URL
- `uploadDate`: Date video was uploaded

**Recommended Properties**:
- `duration`: Video length (ISO 8601 format)
- `contentUrl`: Direct URL to video file
- `embedUrl`: URL for embedding
- `interactionStatistic`: View counts
- `expires`: If content has expiration


### Schema Example (JSON-LD)

```json
{
  "@context": "https://schema.org",
  "@type": "VideoObject",
  "name": "How to Tie a Windsor Knot",
  "description": "Step-by-step tutorial for tying a perfect Windsor knot.",
  "thumbnailUrl": "https://i.ytimg.com/vi/zpe1-BWJqz8/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLAtYVhjfNPzZ_uI62azBYY0vZoxDg",
  "uploadDate": "2025-01-15T08:00:00+08:00",
  "duration": "PT4M30S",
  "contentUrl": "https://example.com/video.mp4",
  "embedUrl": "https://www.youtube.com/embed/VIDEO_ID"
}
```


### Video Sitemaps

**Purpose**: Tell search engines about video content on your site

**When to Use**:
- Self-hosted videos
- YouTube videos embedded on your site
- Large video libraries

**Sitemap Format**:
```xml
<url>
  <loc>https://i.ytimg.com/vi/ubFTkoJkNX4/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLDjM5m5FFyW8M7WDyddSTpKUd667w</loc>
  <video:video>
    <video:thumbnail_loc>thumbnail.jpg</video:thumbnail_loc>
    <video:title>Video Title</video:title>
    <video:description>Description</video:description>
    <video:content_loc>video.mp4</video:content_loc>
  </video:video>
</url>
```


