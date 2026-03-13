# Meta Dynamic Ads Guide

Complete guide to setting up and optimizing dynamic product ads on Meta platforms.

---

## What Are Dynamic Ads?

Dynamic ads automatically show the right products to people who have expressed interest on your website, app, or elsewhere on the internet.

**Key Features**:
- Automatic product selection
- Personalized to each user
- Scale to entire catalog
- Cross-sell and upsell

---

## Setup Requirements

### 1. Meta Pixel

Install pixel on all pages:

```html
<script>
!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', 'YOUR_PIXEL_ID');
fbq('track', 'PageView');
</script>
```

### 2. Standard Events

**ViewContent** (Product page)
```javascript
fbq('track', 'ViewContent', {
  content_ids: ['SKU123'],
  content_type: 'product',
  value: 99.99,
  currency: 'USD'
});
```

**AddToCart**
```javascript
fbq('track', 'AddToCart', {
  content_ids: ['SKU123'],
  content_type: 'product',
  value: 99.99,
  currency: 'USD'
});
```

**Purchase**
```javascript
fbq('track', 'Purchase', {
  content_ids: ['SKU123', 'SKU456'],
  content_type: 'product',
  value: 199.98,
  currency: 'USD'
});
```

### 3. Product Catalog

**Create Catalog via API**
```python
import requests

url = f"https://graph.facebook.com/v19.0/{business_id}/owned_product_catalogs"

params = {
    "access_token": access_token,
    "name": "My Product Catalog",
    "vertical": "ecommerce"  # or commerce, travel, real_estate, automotive, home_listings
}

response = requests.post(url, params=params)
catalog_id = response.json()["id"]
```

**Upload Product Feed**

CSV format:
```csv
id,title,description,availability,condition,price,link,image_link,brand,google_product_category
SKU123,"Blue T-Shirt","Comfortable cotton t-shirt",in stock,new,29.99 USD,https://api.totallypromotional.com/Data/Media/Catalog/6/800/67252f6d-eb36-4665-ac12-9008b2e04c32Gildan-Heavy-Cotton-100-Cotton-T-Shirt-TA101C-royal-blue.jpg & Accessories > Clothing
SKU456,"Red Shoes","Running shoes",in stock,new,89.99 USD,https://pbs.twimg.com/media/HCuWCnGaYAAlRtY.jpg & Accessories > Shoes
```

**Upload via API**
```python
url = f"https://graph.facebook.com/v19.0/{catalog_id}/product_feeds"

params = {
    "access_token": access_token,
    "name": "Main Product Feed",
    "schedule": json.dumps({
        "interval": "DAILY",
        "hour": 2
    }),
    "file_url": "https://example.com/product-feed.csv"
}

response = requests.post(url, params=params)
feed_id = response.json()["id"]
```

---

## Product Catalog Optimization

### Required Fields

| Field | Description | Example |
|-------|-------------|----------|
| **id** | Unique product ID | SKU123 |
| **title** | Product name | Blue Cotton T-Shirt |
| **description** | Product details | Comfortable 100% cotton t-shirt |
| **availability** | Stock status | in stock, out of stock, preorder |
| **condition** | Product condition | new, refurbished, used |
| **price** | Price with currency | 29.99 USD |
| **link** | Product page URL | https://example.com/product/123 |
| **image_link** | Main image URL | https://i.ytimg.com/vi/pheCfysFgfM/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLDXlmWd3oPytdk5HLl6KcXVxV--Eg |

### Recommended Fields

| Field | Description | Benefit |
|-------|-------------|----------|
| **brand** | Brand name | Better targeting |
| **google_product_category** | Product category | Improved relevance |
| **product_type** | Your category | Custom segmentation |
| **sale_price** | Discounted price | Show savings |
| **additional_image_link** | More images | Better showcase |
| **color** | Product color | Variant targeting |
| **size** | Product size | Variant targeting |
| **age_group** | Target age | Better targeting |
| **gender** | Target gender | Better targeting |

### Image Requirements

- **Resolution**: 1024 x 1024 px minimum
- **Aspect ratio**: 1:1 (square)
- **Format**: JPG or PNG
- **Background**: White or neutral
- **Quality**: High resolution, well-lit
- **Content**: Product only, no text overlays

---

## Product Sets

Group products for targeted campaigns.

### Create Product Set
```python
url = f"https://graph.facebook.com/v19.0/{catalog_id}/product_sets"

params = {
    "access_token": access_token,
    "name": "Summer Collection",
    "filter": json.dumps({
        "product_type": {"i_contains": "summer"}
    })
}

response = requests.post(url, params=params)
product_set_id = response.json()["id"]
```

### Filter Examples

**By Price Range**
```json
{
  "and": [
    {"price": {"gte": "50.00 USD"}},
    {"price": {"lte": "100.00 USD"}}
  ]
}
```

**By Brand**
```json
{
  "brand": {"eq": "MyBrand"}
}
```

**By Availability**
```json
{
  "availability": {"eq": "in stock"}
}
```

**Multiple Conditions**
```json
{
  "and": [
    {"brand": {"eq": "MyBrand"}},
    {"availability": {"eq": "in stock"}},
    {"price": {"gte": "20.00 USD"}}
  ]
}
```

---

## Dynamic Ad Templates

### Single Image Template
```python
creative_data = {
    "name": "Dynamic Single Image",
    "object_story_spec": {
        "page_id": page_id,
        "template_data": {
            "format": "SINGLE_IMAGE",
            "link": "https://example.com",
            "message": "{{product.name}} - Only {{product.price}}",
            "name": "Shop Now",
            "call_to_action": {"type": "SHOP_NOW"},
            "retailer_item_ids": ["0"]  # Placeholder
        }
    },
    "product_set_id": product_set_id
}
```

### Carousel Template
```python
creative_data = {
    "name": "Dynamic Carousel",
    "object_story_spec": {
        "page_id": page_id,
        "template_data": {
            "format": "CAROUSEL",
            "link": "https://example.com",
            "message": "Check out these products",
            "call_to_action": {"type": "SHOP_NOW"},
            "retailer_item_ids": ["0"]  # Placeholder
        }
    },
    "product_set_id": product_set_id
}
```

### Collection Template
```python
creative_data = {
    "name": "Dynamic Collection",
    "object_story_spec": {
        "page_id": page_id,
        "template_data": {
            "format": "COLLECTION_VIDEO",
            "link": "https://example.com",
            "message": "Explore our collection",
            "video_id": cover_video_id,
            "call_to_action": {"type": "SHOP_NOW"},
            "retailer_item_ids": ["0"]
        }
    },
    "product_set_id": product_set_id
}
```

---

## Retargeting Strategies

### Broad Audience Retargeting
```python
# Target anyone who visited website in last 30 days
audience_data = {
    "name": "Website Visitors 30d",
    "rule": json.dumps({
        "inclusions": {
            "operator": "or",
            "rules": [
                {
                    "event_sources": [{"id": pixel_id, "type": "pixel"}],
                    "retention_seconds": 2592000,  # 30 days
                    "filter": {
                        "operator": "and",
                        "filters": [
                            {"field": "event", "operator": "eq", "value": "PageView"}
                        ]
                    }
                }
            ]
        }
    }),
    "prefill": True
}
```

### Product Viewers
```python
# Target people who viewed specific products
audience_data = {
    "name": "Product Viewers 14d",
    "rule": json.dumps({
        "inclusions": {
            "operator": "or",
            "rules": [
                {
                    "event_sources": [{"id": pixel_id, "type": "pixel"}],
                    "retention_seconds": 1209600,  # 14 days
                    "filter": {
                        "operator": "and",
                        "filters": [
                            {"field": "event", "operator": "eq", "value": "ViewContent"}
                        ]
                    }
                }
            ]
        }
    }),
    "prefill": True,
    "product_set_id": product_set_id
}
```

### Cart Abandoners
```python
# Target people who added to cart but didn't purchase
audience_data = {
    "name": "Cart Abandoners 7d",
    "rule": json.dumps({
        "inclusions": {
            "operator": "or",
            "rules": [
                {
                    "event_sources": [{"id": pixel_id, "type": "pixel"}],
                    "retention_seconds": 604800,  # 7 days
                    "filter": {
                        "operator": "and",
                        "filters": [
                            {"field": "event", "operator": "eq", "value": "AddToCart"}
                        ]
                    }
                }
            ]
        },
        "exclusions": {
            "operator": "or",
            "rules": [
                {
                    "event_sources": [{"id": pixel_id, "type": "pixel"}],
                    "retention_seconds": 604800,
                    "filter": {
                        "operator": "and",
                        "filters": [
                            {"field": "event", "operator": "eq", "value": "Purchase"}
                        ]
                    }
                }
            ]
        }
    }),
    "prefill": True,
    "product_set_id": product_set_id
}
```

### Cross-Sell to Purchasers
```python
# Target past purchasers with related products
audience_data = {
    "name": "Past Purchasers 60d",
    "rule": json.dumps({
        "inclusions": {
            "operator": "or",
            "rules": [
                {
                    "event_sources": [{"id": pixel_id, "type": "pixel"}],
                    "retention_seconds": 5184000,  # 60 days
                    "filter": {
                        "operator": "and",
                        "filters": [
                            {"field": "event", "operator": "eq", "value": "Purchase"}
                        ]
                    }
                }
            ]
        }
    }),
    "prefill": True,
    "product_set_id": related_product_set_id  # Different product set
}
```

---

## Optimization Tips

### Feed Quality
- Update feed daily
- Remove out-of-stock items
- Accurate pricing
- High-quality images
- Detailed descriptions

### Product Set Strategy
- Create sets by category
- Price-based sets
- Seasonal collections
- Best sellers
- New arrivals

### Bidding
- Start with automatic bidding
- Use value optimization for ROAS
- Set minimum ROAS targets
- Adjust based on product margins

### Creative Testing
- Test single image vs carousel
- Different messaging angles
- With/without sale prices
- Lifestyle vs product-only images
