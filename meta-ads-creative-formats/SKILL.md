---
name: meta-ads-creative-formats
description: "Master ad creative formats for Meta platforms including single image, video, carousel, collection, instant experience, lead ads, dynamic ads, and Stories formats. Covers creative specifications, asset upload via API, dynamic creative optimization, video best practices, and format selection for Facebook, Instagram, Messenger, and Audience Network. Use for: creating image ads, uploading video creatives, building carousel ads, designing collection ads, implementing instant experiences, setting up lead generation forms, configuring dynamic product ads, and optimizing creative performance across Meta platforms."
---

# Meta Ads Creative Formats

Comprehensive guide to ad creative formats across Meta platforms (Facebook, Instagram, Messenger, Audience Network) with API implementation for automated creative deployment.

## Overview

Master all Meta ad formats including image, video, carousel, collection, instant experience, lead ads, and dynamic ads. This skill covers creative specifications, API upload workflows, dynamic creative optimization, and format selection strategies.

## Creative Format Overview

| Format | Best For | Platforms |
|--------|----------|----------|
| **Single Image** | Simple messaging, product showcase | All |
| **Single Video** | Storytelling, demonstrations | All |
| **Carousel** | Multiple products, features | Facebook, Instagram, Audience Network |
| **Collection** | Mobile shopping experience | Facebook, Instagram |
| **Instant Experience** | Immersive full-screen | Facebook, Instagram |
| **Lead Ads** | Lead generation without leaving platform | Facebook, Instagram |
| **Dynamic Ads** | Personalized product retargeting | All |
| **Stories** | Vertical, immersive content | Facebook, Instagram |

## Image Ads

### Upload Image
```python
import requests

# Upload image to ad account
url = f"https://adespresso.com/wp-content/uploads/2021/05/Facebook-advertising-06.png"

with open("ad_image.jpg", "rb") as f:
    files = {"filename": f}
    params = {"access_token": access_token}
    
    response = requests.post(url, files=files, params=params)
    image_hash = response.json()["images"]["filename"]["hash"]
```

### Create Image Ad
```python
creative_data = {
    "name": "Product Image Ad",
    "object_story_spec": {
        "page_id": page_id,
        "link_data": {
            "image_hash": image_hash,
            "link": "https://example.com/product",
            "message": "Discover our new collection!",
            "name": "Shop Now",
            "description": "Limited time offer",
            "call_to_action": {
                "type": "SHOP_NOW",
                "value": {"link": "https://example.com/product"}
            }
        }
    }
}

response = requests.post(
    f"https://graph.facebook.com/v19.0/act_{ad_account_id}/adcreatives",
    params={"access_token": access_token, **creative_data}
)
```

### Image Specifications

| Placement | Recommended Size | Aspect Ratio | Max File Size |
|-----------|------------------|--------------|---------------|
| **Feed** | 1200 x 628 px | 1.91:1 | 30 MB |
| **Stories** | 1080 x 1920 px | 9:16 | 30 MB |
| **Right Column** | 1200 x 628 px | 1.91:1 | 30 MB |
| **Marketplace** | 1200 x 628 px | 1:1 | 30 MB |
| **Reels** | 1080 x 1920 px | 9:16 | 30 MB |

## Video Ads

### Upload Video
```python
import requests

# Initiate upload session
url = f"https://graph.facebook.com/v19.0/act_{ad_account_id}/advideos"

params = {
    "access_token": access_token,
    "upload_phase": "start",
    "file_size": os.path.getsize("ad_video.mp4")
}

response = requests.post(url, params=params)
upload_session_id = response.json()["upload_session_id"]

# Upload video file
with open("ad_video.mp4", "rb") as f:
    files = {"video_file_chunk": f}
    params = {
        "access_token": access_token,
        "upload_phase": "transfer",
        "upload_session_id": upload_session_id
    }
    
    response = requests.post(url, files=files, params=params)

# Finalize upload
params = {
    "access_token": access_token,
    "upload_phase": "finish",
    "upload_session_id": upload_session_id
}

response = requests.post(url, params=params)
video_id = response.json()["id"]
```

### Create Video Ad
```python
creative_data = {
    "name": "Product Video Ad",
    "object_story_spec": {
        "page_id": page_id,
        "video_data": {
            "video_id": video_id,
            "message": "Watch our product in action!",
            "title": "Product Demo",
            "link_description": "Learn more",
            "call_to_action": {
                "type": "LEARN_MORE",
                "value": {"link": "https://example.com"}
            }
        }
    }
}
```

### Video Specifications

| Placement | Resolution | Aspect Ratio | Length | File Size |
|-----------|-----------|--------------|--------|----------|
| **Feed** | 1080 x 1080 px min | 4:5, 1:1, 16:9 | 1s - 241min | 4 GB max |
| **Stories** | 1080 x 1920 px | 9:16 | 1s - 2min | 4 GB max |
| **Reels** | 1080 x 1920 px | 9:16 | 3s - 90s | 4 GB max |
| **In-Stream** | 1080 x 1080 px min | 16:9, 1:1 | 5s - 10min | 4 GB max |

## Carousel Ads

### Create Carousel
```python
creative_data = {
    "name": "Product Carousel",
    "object_story_spec": {
        "page_id": page_id,
        "link_data": {
            "link": "https://example.com",
            "message": "Explore our collection",
            "child_attachments": [
                {
                    "link": "https://pbs.twimg.com/media/HBjTTogXsAA-tUn.png",
                    "image_hash": image_hash_1,
                    "name": "Product 1",
                    "description": "$99.99",
                    "call_to_action": {"type": "SHOP_NOW"}
                },
                {
                    "link": "https://i.ytimg.com/vi/1K_k9s8HKLg/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLAHOahQTWW4UYStr0klSJ0VaEMabw",
                    "image_hash": image_hash_2,
                    "name": "Product 2",
                    "description": "$149.99",
                    "call_to_action": {"type": "SHOP_NOW"}
                },
                {
                    "link": "https://example.com/product3",
                    "video_id": video_id,
                    "name": "Product 3",
                    "description": "$199.99",
                    "call_to_action": {"type": "SHOP_NOW"}
                }
            ],
            "call_to_action": {"type": "SHOP_NOW"}
        }
    }
}
```

### Carousel Specs
- **Cards**: 2-10 cards
- **Image**: 1080 x 1080 px (1:1)
- **Video**: 1:1 aspect ratio
- **Headline**: 40 characters
- **Description**: 20 characters

## Collection Ads

### Create Collection
```python
creative_data = {
    "name": "Product Collection",
    "object_story_spec": {
        "page_id": page_id,
        "template_data": {
            "format": "COLLECTION_VIDEO",  # or COLLECTION_IMAGE
            "link": "https://example.com",
            "message": "Shop the collection",
            "name": "New Arrivals",
            "video_id": cover_video_id,  # Cover media
            "retailer_item_ids": ["SKU001", "SKU002", "SKU003", "SKU004"],  # Product IDs from catalog
            "call_to_action": {"type": "SHOP_NOW"}
        }
    }
}
```

### Collection Requirements
- **Cover**: Image or video
- **Products**: 4+ items from product catalog
- **Instant Experience**: Auto-generated or custom

## Instant Experience (Canvas)

### Create Instant Experience
```python
# Create canvas
canvas_data = {
    "name": "Product Showcase",
    "body_elements": json.dumps([
        {
            "element_type": "HEADER",
            "style": "FIT_TO_WIDTH",
            "photo": {"photo_id": photo_id}
        },
        {
            "element_type": "TEXT",
            "text": "Discover our latest products"
        },
        {
            "element_type": "CAROUSEL",
            "child_elements": [
                {"photo": {"photo_id": photo_id_1}, "link": "https://i.ytimg.com/vi/B820PJnbkNM/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLDRCo7akNBji-2KnZ-zvaxAqbximw"},
                {"photo": {"photo_id": photo_id_2}, "link": "https://i.ytimg.com/vi/w_RP83nbffc/maxresdefault.jpg"}
            ]
        },
        {
            "element_type": "BUTTON",
            "text": "Shop Now",
            "link": "https://example.com"
        }
    ])
}

response = requests.post(
    f"https://graph.facebook.com/v19.0/{page_id}/canvas_elements",
    params={"access_token": access_token, **canvas_data}
)

canvas_id = response.json()["id"]
```

### Use in Ad
```python
creative_data = {
    "object_story_spec": {
        "page_id": page_id,
        "link_data": {
            "link": f"https://www.facebook.com/canvas/{canvas_id}",
            "image_hash": image_hash,
            "message": "Swipe up to explore"
        }
    }
}
```

## Lead Ads

### Create Lead Form
```python
form_data = {
    "name": "Contact Form",
    "privacy_policy_url": "https://example.com/privacy",
    "questions": json.dumps([
        {"type": "FULL_NAME"},
        {"type": "EMAIL"},
        {"type": "PHONE_NUMBER"},
        {
            "type": "CUSTOM",
            "key": "company_size",
            "label": "Company Size",
            "field_type": "MULTIPLE_CHOICE",
            "options": [{"key": "1-10", "value": "1-10"}, {"key": "11-50", "value": "11-50"}]
        }
    ]),
    "thank_you_page": json.dumps({
        "title": "Thank you!",
        "body": "We'll be in touch soon.",
        "button_text": "Download Guide",
        "button_type": "VISIT_WEBSITE",
        "website_url": "https://example.com/guide"
    })
}

response = requests.post(
    f"https://graph.facebook.com/v19.0/{page_id}/leadgen_forms",
    params={"access_token": access_token, **form_data}
)

form_id = response.json()["id"]
```

### Create Lead Ad
```python
creative_data = {
    "name": "Lead Gen Ad",
    "object_story_spec": {
        "page_id": page_id,
        "link_data": {
            "image_hash": image_hash,
            "link": f"https://www.facebook.com/leadgen/{form_id}",
            "message": "Get your free guide",
            "call_to_action": {"type": "SIGN_UP"}
        }
    }
}
```

## Dynamic Ads

### Product Catalog Setup
```python
# Create catalog
catalog_data = {
    "name": "Product Catalog",
    "vertical": "ecommerce"  # or commerce, travel, real_estate
}

response = requests.post(
    f"https://graph.facebook.com/v19.0/{business_id}/owned_product_catalogs",
    params={"access_token": access_token, **catalog_data}
)

catalog_id = response.json()["id"]

# Create product set
product_set_data = {
    "name": "All Products",
    "filter": json.dumps({"retailer_id": {"is_any": ["*"]}})
}

response = requests.post(
    f"https://graph.facebook.com/v19.0/{catalog_id}/product_sets",
    params={"access_token": access_token, **product_set_data}
)

product_set_id = response.json()["id"]
```

### Create Dynamic Ad Template
```python
creative_data = {
    "name": "Dynamic Product Ad",
    "object_story_spec": {
        "page_id": page_id,
        "template_data": {
            "format": "SINGLE_IMAGE",  # or CAROUSEL
            "link": "https://example.com",
            "message": "{{product.name}} - {{product.price}}",
            "call_to_action": {"type": "SHOP_NOW"},
            "retailer_item_ids": ["0"]  # Placeholder
        }
    },
    "product_set_id": product_set_id
}
```

## Dynamic Creative Optimization (DCO)

### Create DCO Ad
```python
# Upload multiple assets
images = [upload_image("img1.jpg"), upload_image("img2.jpg"), upload_image("img3.jpg")]
videos = [upload_video("vid1.mp4"), upload_video("vid2.mp4")]

# Create ad with asset feed
creative_data = {
    "name": "DCO Ad",
    "object_story_spec": {
        "page_id": page_id
    },
    "asset_feed_spec": {
        "images": [{"hash": h} for h in images],
        "videos": [{"video_id": v} for v in videos],
        "bodies": [
            {"text": "Discover amazing products"},
            {"text": "Shop the latest collection"},
            {"text": "Limited time offer"}
        ],
        "titles": [
            {"text": "New Arrivals"},
            {"text": "Best Sellers"}
        ],
        "descriptions": [
            {"text": "Free shipping on orders over $50"},
            {"text": "30-day returns"}
        ],
        "link_urls": [
            {"website_url": "https://example.com"}
        ],
        "call_to_action_types": ["SHOP_NOW", "LEARN_MORE"]
    }
}
```

### DCO Limits
- **Images**: Up to 10
- **Videos**: Up to 10
- **Titles**: Up to 5
- **Descriptions**: Up to 5
- **Bodies**: Up to 5

## Call-to-Action Buttons

| CTA Type | Use Case |
|----------|----------|
| **SHOP_NOW** | E-commerce |
| **LEARN_MORE** | Information |
| **SIGN_UP** | Registration |
| **DOWNLOAD** | App/file download |
| **BOOK_NOW** | Appointments |
| **CONTACT_US** | Inquiries |
| **GET_QUOTE** | Services |
| **APPLY_NOW** | Applications |
| **SUBSCRIBE** | Newsletters |
| **WATCH_MORE** | Video content |

## Text Guidelines

| Element | Limit | Best Practice |
|---------|-------|---------------|
| **Primary Text** | 125 characters | Front-load key message |
| **Headline** | 40 characters | Clear, action-oriented |
| **Description** | 30 characters | Value proposition |
| **Link Description** | 30 characters | Additional context |

**Text in Image**: Keep under 20% for optimal delivery

## Using the Reference Files

**`/references/meta-creative-specs.md`** — Read for complete creative specifications, all placement dimensions, file format requirements, and technical guidelines.

**`/references/meta-creative-best-practices.md`** — Read for creative testing strategies, performance optimization, design principles, and platform-specific recommendations.

**`/references/meta-dynamic-ads-guide.md`** — Read for product catalog setup, feed optimization, dynamic creative templates, and retargeting strategies.

## References

- [Meta Creative Best Practices](references/meta-creative-best-practices.md)
- [Meta Creative Specs](references/meta-creative-specs.md)
- [Meta Dynamic Ads Guide](references/meta-dynamic-ads-guide.md)
