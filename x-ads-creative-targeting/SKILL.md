---
name: x-ads-creative-targeting
description: "Master ad creative formats (Tweets, Cards, Media) and advanced targeting options for X advertising including demographics, interests, keywords, followers, behaviors, custom audiences, and event targeting. Use for: creating promoted tweets, designing Twitter Cards (website, app download, video, conversation), uploading media assets, implementing demographic targeting, interest-based targeting, keyword targeting, follower lookalikes, device/platform targeting, custom audience creation, retargeting campaigns, and creative A/B testing on X platform."
---

# X (Twitter) Ads Creative & Targeting

Master ad creative formats and implement advanced targeting strategies on X platform using the Ads API for programmatic audience definition and creative management.

## Overview

Comprehensive guide to creating ad creatives (Promoted Tweets, Twitter Cards, Media) and implementing precise targeting (demographics, interests, keywords, custom audiences) on X platform for automated campaign deployment.

## Ad Creative Types

| Creative Type | Format | Use Case |
|---------------|--------|----------|
| **Published Tweet** | Existing organic tweet | Promote high-performing content |
| **Draft Tweet** | Ad-only tweet | Campaign-specific messaging |
| **Website Card** | Image + link + CTA | Drive website traffic |
| **App Download Card** | App preview + install button | Mobile app installs |
| **Video Website Card** | Video + link + CTA | Video engagement + traffic |
| **Conversation Card** | Interactive multi-choice | Engagement + data collection |

## Promoted Tweets

### Promote Existing Tweet
```python
promoted_tweet_data = {
    "line_item_id": line_item_id,
    "tweet_ids": ["1234567890123456789"]
}

response = requests.post(
    f"https://ads-api.x.com/12/accounts/{account_id}/promoted_tweets",
    headers=headers,
    json=promoted_tweet_data
)
```

### Create Draft Tweet
Use Twitter API v2 to create tweet, then promote via Ads API.

## Twitter Cards

### Website Card
```python
card_data = {
    "name": "Product Launch Card",
    "website_title": "Revolutionary New Product",
    "website_url": "https://example.com/product",
    "image_media_id": "media_id_123"
}

response = requests.post(
    f"https://ads-api.x.com/12/accounts/{account_id}/cards/website",
    headers=headers,
    json=card_data
)
```

### App Download Card
```python
app_card_data = {
    "name": "App Install Card",
    "app_country_code": "US",
    "iphone_app_id": "123456789",
    "googleplay_app_id": "com.example.app",
    "image_media_id": "media_id_456"
}
```

## Media Upload

### Image Upload
```python
import base64

with open("ad_image.jpg", "rb") as f:
    image_data = base64.b64encode(f.read()).decode()

media_response = requests.post(
    "https://upload.twitter.com/1.1/media/upload.json",
    headers={"Authorization": f"Bearer {access_token}"},
    data={
        "media_data": image_data,
        "media_category": "tweet_image"
    }
)
media_id = media_response.json()["media_id_string"]
```

### Video Upload (Chunked)
For videos > 5MB, use chunked upload: INIT → APPEND → FINALIZE

## Creative Specifications

| Asset Type | Specs |
|------------|-------|
| **Image** | JPG/PNG, max 5MB, 1200x628px (1.91:1) |
| **Video** | MP4/MOV, max 1GB, 2:20 max, 1920x1080 or 1080x1080 |
| **Tweet Text** | 280 characters |
| **Card Title** | 70 characters |
| **Card Description** | 200 characters |

## Targeting Options

### 1. Demographics
```python
targeting = {
    "age_range": ["AGE_25_TO_34", "AGE_35_TO_49"],
    "gender": "MALE",  # or "FEMALE", omit for all
    "languages": ["en", "es", "fr"]
}
```

### 2. Location
```python
# Country
targeting = {
    "locations": [
        {"country": "US"},
        {"country": "CA"}
    ]
}

# Metro/Region
targeting = {
    "locations": [
        {"metro_code": "602"},  # Chicago
        {"region": "US-CA"}     # California
    ]
}

# Postal Code
targeting = {
    "locations": [
        {"postal_code": "US-10001"},
        {"postal_code": "US-90210"}
    ]
}
```

### 3. Interests
```python
# Get available interests
response = requests.get(
    f"https://ads-api.x.com/12/accounts/{account_id}/targeting_criteria/interests",
    headers=headers
)

# Apply interest targeting
targeting = {
    "interests": [
        "15",   # Technology
        "127",  # Consumer electronics
        "241"   # Mobile
    ]
}
```

### 4. Keywords
```python
# Broad match
targeting = {
    "keywords": [
        {"keyword": "artificial intelligence"},
        {"keyword": "machine learning"}
    ]
}

# Phrase match
targeting = {
    "keywords": [
        {"keyword": '"AI technology"'}  # Exact phrase
    ]
}

# Negative keywords
targeting = {
    "negative_keywords": [
        {"keyword": "free"},
        {"keyword": "cheap"}
    ]
}
```

### 5. Follower Targeting
```python
# Target followers of specific accounts
targeting = {
    "followers_of_users": [
        "783214",      # @Twitter
        "17874544"     # @OpenAI
    ]
}

# Lookalike audiences
targeting = {
    "similar_to_followers_of_users": ["your_account_id"]
}
```

### 6. Behavior Targeting
```python
# Device & Platform
targeting = {
    "platform": ["IPHONE", "ANDROID_PHONE"],
    "platform_versions": ["13.0"],  # iOS 13+
    "devices": ["IPHONE_14_PRO"]
}

# Network Activity
targeting = {
    "network_activation_duration": "30_DAYS",  # New users
    "user_engagement": "ENGAGED_WITH_TWEETS"
}
```

### 7. Custom Audiences
```python
# Create tailored audience
audience_data = {
    "name": "Customer Email List Q1",
    "list_type": "EMAIL"
}

response = requests.post(
    f"https://ads-api.x.com/12/accounts/{account_id}/tailored_audiences",
    headers=headers,
    json=audience_data
)
audience_id = response.json()["data"]["id"]

# Upload users
users_data = {
    "users": [
        {"email": "user1@example.com"},
        {"email": "user2@example.com"}
    ]
}

requests.post(
    f"https://ads-api.x.com/12/accounts/{account_id}/tailored_audiences/{audience_id}/users",
    headers=headers,
    json=users_data
)
```

## Targeting Combinations

### AND Logic (Narrow)
```python
targeting = {
    "age_range": ["AGE_25_TO_34"],
    "gender": "FEMALE",
    "interests": ["15"],  # Technology
    "locations": [{"country": "US"}],
    "keywords": [{"keyword": "AI"}]
}
# User must match ALL criteria
```

### Exclusion Targeting
```python
targeting = {
    "interests": ["15"],  # Include tech
    "excluded_tailored_audiences": [existing_customer_audience_id],
    "negative_keywords": [{"keyword": "competitor"}]
}
```

## Audience Size Guidelines

- **Minimum**: 50,000 users for stable delivery
- **Optimal**: 500,000+ for best performance
- **Maximum**: No hard limit, but narrower = better relevance

## Reach Estimation
```python
response = requests.get(
    f"https://ads-api.x.com/12/accounts/{account_id}/reach_estimate",
    headers=headers,
    params={"targeting_criteria": json.dumps(targeting)}
)
estimate = response.json()["data"]
print(f"Estimated reach: {estimate['users']}")
```

## Creative Testing

### A/B Testing
```python
# Create multiple promoted tweets for same line item
creatives = [
    {"tweet_id": "tweet_1", "line_item_id": line_item_id},
    {"tweet_id": "tweet_2", "line_item_id": line_item_id},
    {"tweet_id": "tweet_3", "line_item_id": line_item_id}
]

for creative in creatives:
    requests.post(
        f"https://ads-api.x.com/12/accounts/{account_id}/promoted_tweets",
        headers=headers,
        json=creative
    )
```

### Dynamic Creative Optimization
- X automatically optimizes delivery to best-performing creatives
- Minimum 3 creatives per line item recommended
- Monitor performance after 1,000 impressions per creative

## Using the Reference Files

**`/references/x-creative-specs.md`** — Read for detailed creative specifications, image/video requirements, card types, and asset optimization guidelines.

**`/references/x-targeting-reference.md`** — Read for complete targeting options reference, audience building strategies, and targeting combination examples.

**`/references/x-creative-best-practices.md`** — Read for creative testing frameworks, performance benchmarks, and optimization strategies.
