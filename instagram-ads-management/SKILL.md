---
name: instagram-ads-management
description: "Instagram advertising through Meta Marketing API including Feed ads, Stories ads, Reels ads, Explore ads, and Shopping ads. Covers creative formats, targeting options, and Instagram-specific best practices. Use for: creating Instagram ad campaigns, optimizing for Instagram placements, implementing Stories and Reels ads, and leveraging Instagram shopping features via Meta Marketing API."
---

# Instagram Ads Management

Instagram advertising campaign management through Meta Marketing API with platform-specific optimization strategies.

## Overview

Comprehensive guide to Instagram advertising through Meta's Marketing API. Instagram ads are created using the same API as Facebook ads but with Instagram-specific placements, formats, and best practices.

## Instagram Placements

### Available Placements
```python
targeting = {
    "publisher_platforms": ["instagram"],
    "instagram_positions": [
        "stream",        # Feed
        "story",         # Stories
        "explore",       # Explore
        "reels",         # Reels
        "profile_feed",  # Profile
        "search"         # Search results
    ]
}
```

## Creative Formats

### Feed Ads
- **Aspect Ratio**: 1:1 (square) or 4:5 (portrait)
- **Resolution**: 1080 x 1080 px (1:1) or 1080 x 1350 px (4:5)
- **Video**: Up to 60 seconds

### Stories Ads
- **Aspect Ratio**: 9:16 (vertical)
- **Resolution**: 1080 x 1920 px
- **Video**: Up to 60 seconds
- **Safe Zone**: Center 1080 x 1420 px

### Reels Ads
- **Aspect Ratio**: 9:16 (vertical)
- **Resolution**: 1080 x 1920 px
- **Video**: 9-30 seconds (15 seconds optimal)
- **Sound**: Required

## Instagram Shopping

### Shopping Ads
```python
creative_data = {
    "object_story_spec": {
        "instagram_actor_id": instagram_account_id,
        "link_data": {
            "link": "https://example.com/product",
            "message": "Shop our latest collection",
            "call_to_action": {"type": "SHOP_NOW"}
        }
    },
    "product_set_id": product_set_id
}
```

## Best Practices

### Feed Optimization
- Use high-quality, visually appealing images
- Square (1:1) or portrait (4:5) formats
- Minimal text on images
- Strong visual storytelling

### Stories Optimization
- Vertical (9:16) format
- First 3 seconds critical
- Interactive elements (polls, questions)
- Authentic, less polished content

### Reels Optimization
- Trending audio
- Fast-paced editing
- Entertainment value
- 9-15 seconds optimal length

## Using the Reference Files

**`/references/instagram-creative-specs.md`** — Read for complete creative specifications for all Instagram placements.

**`/references/instagram-best-practices.md`** — Read for platform-specific optimization strategies and content guidelines.

## References

- [Instagram Creative Specs](references/instagram-creative-specs.md)
