---
name: google-ads-shopping-video
description: "Create and manage Google Shopping campaigns (Product Shopping Ads, Local Inventory Ads) and YouTube Video campaigns (skippable, non-skippable, bumper ads). Use for e-commerce product advertising, Google Merchant Center integration, product feed optimization, video ad creation, YouTube targeting, and multi-format video strategies across YouTube and Google Display Network."
---

# Google Shopping & Video Campaigns

Create product-focused Shopping campaigns and engaging Video campaigns for YouTube and Google Display Network.

## Overview

This skill covers two distinct campaign types: Shopping campaigns for e-commerce product advertising and Video campaigns for YouTube brand awareness and engagement. Use Shopping for direct product sales and Video for storytelling, demonstrations, and brand building.

## Shopping Campaigns

### Requirements

1. **Google Merchant Center Account** - Product catalog management
2. **Product Feed** - Product data (title, price, image, availability)
3. **Website** - E-commerce site with products
4. **Conversion Tracking** - Track purchases

### Shopping Campaign Types

| Type | Use Case | Setup Complexity |
|------|----------|------------------|
| **Standard Shopping** | Manual bid control, product groups | Medium |
| **Smart Shopping** (Deprecated) | Automated, replaced by Performance Max | N/A |
| **Local Inventory Ads** | In-store product availability | High |

### Product Feed Optimization

**Critical Fields**:
- **Title**: Include brand, product type, key attributes (60-150 chars)
- **Description**: Detailed product info (500-5000 chars)
- **Image**: High quality, white background, 800x800px minimum
- **Price**: Accurate, matches website
- **Availability**: In stock, out of stock, preorder
- **GTIN**: Global Trade Item Number (barcode)
- **Brand**: Manufacturer brand name
- **Product Type**: Your category taxonomy
- **Google Product Category**: Google's taxonomy

**Title Optimization**:
```
Bad: "Running Shoes"
Good: "Nike Air Zoom Pegasus 40 Men's Running Shoes - Black/White - Size 10"
```

### Product Groups & Bidding

**Product Group Hierarchy**:
```
All Products
├── Brand
│   ├── Nike
│   ├── Adidas
│   └── Brooks
├── Product Type
│   ├── Running Shoes
│   ├── Trail Shoes
│   └── Racing Flats
└── Custom Labels
    ├── Best Sellers
    ├── High Margin
    └── Clearance
```

**Bidding Strategy**:
- **High-margin products**: Higher bids
- **Best sellers**: Competitive bids
- **Clearance**: Lower bids
- **New products**: Test bids

## Video Campaigns

### Video Ad Formats

| Format | Length | Skippable | Placement | Best For |
|--------|--------|-----------|-----------|----------|
| **Skippable In-Stream** | Any length | After 5s | Before/during videos | Awareness, consideration |
| **Non-Skippable In-Stream** | 15-20s | No | Before/during videos | Brand awareness |
| **Bumper Ads** | 6s | No | Before/during videos | Brand recall |
| **In-Feed Video** | Any length | N/A | YouTube feed, search | Discovery |
| **Outstream** | Any length | N/A | Mobile web/apps | Mobile reach |

### Video Ad Specifications

| Format | Aspect Ratio | Resolution | File Size |
|--------|--------------|------------|-----------|
| Landscape | 16:9 | 1920x1080 | <1GB |
| Square | 1:1 | 1080x1080 | <1GB |
| Vertical | 9:16 | 1080x1920 | <1GB |

### Video Ad Best Practices

**First 5 Seconds**:
- Hook viewer immediately
- Show product/brand
- Clear value proposition

**Call-to-Action**:
- Visible CTA overlay
- Clear next step
- Compelling offer

**Storytelling**:
- Problem-solution format
- Emotional connection
- Brand integration

### YouTube Targeting

| Targeting Type | Options | Use Case |
|----------------|---------|----------|
| **Demographics** | Age, gender, parental status, income | Demographic targeting |
| **Interests** | Affinity, in-market, life events | Interest-based |
| **Placements** | Specific channels, videos | Contextual |
| **Topics** | Video content topics | Broad contextual |
| **Keywords** | Video search terms | Search intent |

## Using the Reference Files

**`/references/shopping-feed-optimization.md`** — Read when optimizing product feeds, including title formulas, image requirements, and feed troubleshooting.

**`/references/video-ad-creation.md`** — Read when creating video ads, including scriptwriting, production tips, and format-specific best practices.
