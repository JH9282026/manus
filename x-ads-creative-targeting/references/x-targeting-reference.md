# X Ads Targeting Complete Reference

## Demographic Targeting

### Age Ranges
- `AGE_13_TO_17`
- `AGE_18_TO_24`
- `AGE_25_TO_34`
- `AGE_35_TO_49`
- `AGE_50_TO_54`
- `AGE_55_PLUS`

### Gender
- `MALE`
- `FEMALE`
- Omit for all genders

### Languages (ISO 639-1 codes)
- `en` - English
- `es` - Spanish
- `fr` - French
- `de` - German
- `ja` - Japanese
- `pt` - Portuguese
- `ar` - Arabic
- `ko` - Korean
- And 40+ more languages

## Geographic Targeting

### Country Codes (ISO 3166-1)
```python
targeting = {
    "locations": [
        {"country": "US"},  # United States
        {"country": "GB"},  # United Kingdom
        {"country": "CA"},  # Canada
        {"country": "AU"},  # Australia
        {"country": "DE"},  # Germany
        {"country": "FR"},  # France
        {"country": "JP"},  # Japan
        {"country": "BR"}   # Brazil
    ]
}
```

### Metro Codes (DMA)
Major US markets:
- `501` - New York
- `602` - Chicago
- `803` - Los Angeles
- `623` - Dallas-Fort Worth
- `506` - Boston
- `504` - Philadelphia
- `807` - San Francisco
- `819` - Seattle

### Regions
State/province codes:
- `US-CA` - California
- `US-NY` - New York
- `US-TX` - Texas
- `US-FL` - Florida
- `CA-ON` - Ontario
- `GB-ENG` - England

## Interest Categories

### Technology
- `15` - Technology
- `127` - Consumer electronics
- `241` - Mobile
- `242` - Computers
- `243` - Software

### Business
- `6` - Business
- `47` - Entrepreneurship
- `48` - Marketing
- `49` - Sales

### Entertainment
- `8` - Entertainment
- `56` - Movies
- `57` - Music
- `58` - Television
- `59` - Gaming

### Sports
- `26` - Sports
- `149` - Football
- `150` - Basketball
- `151` - Baseball
- `152` - Soccer

### Lifestyle
- `25` - Lifestyle
- `141` - Fashion
- `142` - Beauty
- `143` - Food
- `144` - Travel

## Behavior Targeting

### Device Types
- `IPHONE`
- `IPAD`
- `ANDROID_PHONE`
- `ANDROID_TABLET`
- `DESKTOP`

### Platform Versions
- `iOS_13.0` and above
- `Android_10.0` and above

### Network Activity
- `NEW_USERS` - Joined in last 30 days
- `ENGAGED_USERS` - Active in last 7 days
- `ENGAGED_WITH_TWEETS` - Engaged with tweets recently

## Custom Audience Types

### Tailored Audiences
```python
# Email list
audience_data = {
    "name": "Customer Emails",
    "list_type": "EMAIL"
}

# Phone numbers
audience_data = {
    "name": "Customer Phones",
    "list_type": "PHONE_NUMBER"
}

# Twitter User IDs
audience_data = {
    "name": "Twitter Followers",
    "list_type": "TWITTER_ID"
}

# Mobile Advertising IDs
audience_data = {
    "name": "App Users",
    "list_type": "MOBILE_ADVERTISING_ID"
}
```

### Web Event Tags (Pixel)
```python
# Create pixel
tag_data = {
    "name": "Website Visitors"
}

response = requests.post(
    f"https://ads-api.x.com/12/accounts/{account_id}/web_event_tags",
    headers=headers,
    json=tag_data
)

pixel_id = response.json()["data"]["id"]
pixel_code = response.json()["data"]["embed_code"]

# Install pixel_code on website
# Then create audience from pixel events
```

## Keyword Targeting

### Match Types
```python
# Broad match - matches variations
{"keyword": "running shoes"}

# Phrase match - exact phrase
{"keyword": '"running shoes"'}

# Unordered match - all words, any order
{"keyword": "shoes running"}
```

### Negative Keywords
```python
targeting = {
    "keywords": [
        {"keyword": "premium shoes"}
    ],
    "negative_keywords": [
        {"keyword": "cheap"},
        {"keyword": "free"},
        {"keyword": "discount"}
    ]
}
```

## Follower Targeting

### Target Followers
```python
# Get user ID from username
response = requests.get(
    f"https://api.twitter.com/2/users/by/username/{username}",
    headers={"Authorization": f"Bearer {token}"}
)
user_id = response.json()["data"]["id"]

# Target followers
targeting = {
    "followers_of_users": [user_id]
}
```

### Lookalike Audiences
```python
# Similar to your followers
targeting = {
    "similar_to_followers_of_users": [your_account_id]
}

# Similar to competitor followers
targeting = {
    "similar_to_followers_of_users": [competitor_account_id]
}
```

## Event Targeting

### Trending Events
```python
# Get available events
response = requests.get(
    f"https://ads-api.x.com/12/accounts/{account_id}/targeting_criteria/events",
    headers=headers
)

# Target specific event
targeting = {
    "events": ["event_id_123"]
}
```

### TV Targeting
```python
# Target TV show viewers
targeting = {
    "tv_shows": ["show_id_789"],
    "tv_genres": ["SPORTS", "NEWS"]
}
```

## Targeting Combinations

### Example 1: Tech-Savvy Millennials in US
```python
targeting = {
    "age_range": ["AGE_25_TO_34", "AGE_35_TO_49"],
    "interests": ["15", "127"],  # Technology, Consumer electronics
    "locations": [{"country": "US"}],
    "languages": ["en"]
}
```

### Example 2: Mobile Gamers Excluding Existing Customers
```python
targeting = {
    "interests": ["59"],  # Gaming
    "platform": ["IPHONE", "ANDROID_PHONE"],
    "excluded_tailored_audiences": [existing_customer_audience_id]
}
```

### Example 3: High-Intent Shoppers
```python
targeting = {
    "keywords": [
        {"keyword": "buy now"},
        {"keyword": "purchase"},
        {"keyword": "order"}
    ],
    "interests": ["141"],  # Fashion
    "locations": [{"country": "US"}]
}
```

## Audience Size Estimation

```python
def estimate_audience_size(account_id, targeting, access_token):
    headers = {"Authorization": f"Bearer {access_token}"}
    
    response = requests.get(
        f"https://ads-api.x.com/12/accounts/{account_id}/reach_estimate",
        headers=headers,
        params={"targeting_criteria": json.dumps(targeting)}
    )
    
    estimate = response.json()["data"]
    
    return {
        "users": estimate["users"],
        "audience_size": estimate["audience_size"],  # SMALL, MEDIUM, LARGE
        "min_reach": estimate.get("min_reach"),
        "max_reach": estimate.get("max_reach")
    }
```

## Targeting Best Practices

### Start Broad, Then Narrow
1. Begin with broad targeting (country + age)
2. Analyze performance data
3. Layer additional targeting (interests, keywords)
4. Refine based on results

### Audience Size Guidelines
- **Too Small** (< 50K): Unstable delivery, high CPMs
- **Optimal** (500K - 5M): Best performance
- **Too Broad** (> 50M): Less relevant, lower engagement

### Testing Strategy
1. **Broad vs. Narrow**: Test wide audience vs. highly targeted
2. **Interest Stacking**: Test single interest vs. multiple
3. **Geo Variations**: Test different markets
4. **Device Split**: Test mobile vs. desktop separately
