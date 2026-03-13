# Pinterest Ads API Endpoints Reference

Complete reference for Pinterest Ads API v5 endpoints.

## Base URL
```
https://api.pinterest.com/v5
```

## Authentication Endpoints

### OAuth Token
- **POST** `/oauth/token` - Exchange authorization code for access token
- **POST** `/oauth/token` (refresh) - Refresh expired access token

## Campaign Management

### Campaigns
- **GET** `/ad_accounts/{ad_account_id}/campaigns` - List campaigns
- **POST** `/ad_accounts/{ad_account_id}/campaigns` - Create campaign
- **GET** `/ad_accounts/{ad_account_id}/campaigns/{campaign_id}` - Get campaign
- **PATCH** `/ad_accounts/{ad_account_id}/campaigns/{campaign_id}` - Update campaign
- **DELETE** `/ad_accounts/{ad_account_id}/campaigns/{campaign_id}` - Delete campaign

### Ad Groups
- **GET** `/ad_accounts/{ad_account_id}/ad_groups` - List ad groups
- **POST** `/ad_accounts/{ad_account_id}/ad_groups` - Create ad group
- **GET** `/ad_accounts/{ad_account_id}/ad_groups/{ad_group_id}` - Get ad group
- **PATCH** `/ad_accounts/{ad_account_id}/ad_groups/{ad_group_id}` - Update ad group

### Ads
- **GET** `/ad_accounts/{ad_account_id}/ads` - List ads
- **POST** `/ad_accounts/{ad_account_id}/ads` - Create ad
- **GET** `/ad_accounts/{ad_account_id}/ads/{ad_id}` - Get ad
- **PATCH** `/ad_accounts/{ad_account_id}/ads/{ad_id}` - Update ad

## Creative Management

### Pins
- **POST** `/pins` - Create Pin
- **GET** `/pins/{pin_id}` - Get Pin
- **PATCH** `/pins/{pin_id}` - Update Pin
- **DELETE** `/pins/{pin_id}` - Delete Pin

### Media
- **POST** `/media` - Register media for upload
- **GET** `/media/{media_id}` - Get media status

## Audience Management

### Customer Lists
- **POST** `/ad_accounts/{ad_account_id}/customer_lists` - Create customer list
- **GET** `/ad_accounts/{ad_account_id}/customer_lists` - List customer lists
- **PATCH** `/ad_accounts/{ad_account_id}/customer_lists/{customer_list_id}` - Update customer list

### Audiences
- **POST** `/ad_accounts/{ad_account_id}/audiences` - Create audience
- **GET** `/ad_accounts/{ad_account_id}/audiences` - List audiences

## Conversion Tracking

### Conversion Tags
- **GET** `/ad_accounts/{ad_account_id}/conversion_tags` - List conversion tags
- **POST** `/ad_accounts/{ad_account_id}/conversion_tags` - Create conversion tag
- **GET** `/ad_accounts/{ad_account_id}/conversion_tags/{conversion_tag_id}` - Get conversion tag

### Conversion Events
- **POST** `/ad_accounts/{ad_account_id}/conversion_tags/{tag_id}/events` - Send conversion event

## Analytics and Reporting

### Campaign Analytics
- **GET** `/ad_accounts/{ad_account_id}/campaigns/analytics` - Get campaign analytics

### Ad Group Analytics
- **GET** `/ad_accounts/{ad_account_id}/ad_groups/analytics` - Get ad group analytics

### Ad Analytics
- **GET** `/ad_accounts/{ad_account_id}/ads/analytics` - Get ad analytics

## Rate Limits
- 1000 requests per hour per access token
- 200 requests per minute (burst)
