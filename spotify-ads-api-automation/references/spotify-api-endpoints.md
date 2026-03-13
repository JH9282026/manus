# Spotify Ads API Endpoints Reference

Complete reference for Spotify Ads API endpoints.

## Base URL
```
https://api.spotify.com/v1/ads
```

## Authentication
- **POST** `https://accounts.spotify.com/api/token` - Get access token

## Campaign Management

### Campaigns
- **GET** `/accounts/{ad_account_id}/campaigns` - List campaigns
- **POST** `/accounts/{ad_account_id}/campaigns` - Create campaign
- **GET** `/accounts/{ad_account_id}/campaigns/{campaign_id}` - Get campaign
- **PATCH** `/accounts/{ad_account_id}/campaigns/{campaign_id}` - Update campaign

### Ad Sets
- **GET** `/accounts/{ad_account_id}/adsets` - List ad sets
- **POST** `/accounts/{ad_account_id}/adsets` - Create ad set
- **GET** `/accounts/{ad_account_id}/adsets/{adset_id}` - Get ad set
- **PATCH** `/accounts/{ad_account_id}/adsets/{adset_id}` - Update ad set

### Ads
- **GET** `/accounts/{ad_account_id}/ads` - List ads
- **POST** `/accounts/{ad_account_id}/ads` - Create ad
- **GET** `/accounts/{ad_account_id}/ads/{ad_id}` - Get ad
- **PATCH** `/accounts/{ad_account_id}/ads/{ad_id}` - Update ad

## Asset Management

### Audio Assets
- **POST** `/accounts/{ad_account_id}/assets/audio` - Create audio asset
- **POST** `/accounts/{ad_account_id}/assets/audio/{asset_id}/confirm` - Confirm upload

### Image Assets
- **POST** `/accounts/{ad_account_id}/assets/image` - Create image asset

## Audience Management

### Audiences
- **POST** `/accounts/{ad_account_id}/audiences` - Create audience
- **GET** `/accounts/{ad_account_id}/audiences` - List audiences

### Pixels
- **POST** `/accounts/{ad_account_id}/pixels` - Create pixel
- **GET** `/accounts/{ad_account_id}/pixels` - List pixels

### Conversions
- **POST** `/accounts/{ad_account_id}/conversions` - Create conversion event

## Analytics and Reporting

### Campaign Analytics
- **GET** `/accounts/{ad_account_id}/campaigns/{campaign_id}/analytics` - Get campaign analytics

### Ad Set Analytics
- **GET** `/accounts/{ad_account_id}/adsets/analytics` - Get ad set analytics

### Reports
- **POST** `/accounts/{ad_account_id}/reports` - Create report
- **GET** `/accounts/{ad_account_id}/reports/{report_id}/download` - Download report

## Rate Limits
- 1000 requests per hour (general)
- 100 requests per hour (reporting endpoints)
