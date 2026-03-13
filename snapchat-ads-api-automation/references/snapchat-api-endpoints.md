# Snapchat Marketing API Endpoints Reference

Complete reference for Snapchat Marketing API endpoints.

## Base URL
```
https://adsapi.snapchat.com/v1
```

## Authentication
- **POST** `https://accounts.snapchat.com/login/oauth2/access_token` - Get access token

## Campaign Management

### Campaigns
- **GET** `/adaccounts/{ad_account_id}/campaigns` - List campaigns
- **POST** `/adaccounts/{ad_account_id}/campaigns` - Create campaigns (bulk)
- **GET** `/campaigns/{campaign_id}` - Get campaign
- **PUT** `/campaigns/{campaign_id}` - Update campaign

### Ad Squads
- **GET** `/campaigns/{campaign_id}/adsquads` - List ad squads
- **POST** `/campaigns/{campaign_id}/adsquads` - Create ad squads (bulk)
- **GET** `/adsquads/{adsquad_id}` - Get ad squad
- **PUT** `/adsquads/{adsquad_id}` - Update ad squad

### Ads
- **GET** `/adsquads/{adsquad_id}/ads` - List ads
- **POST** `/adsquads/{adsquad_id}/ads` - Create ads (bulk)
- **GET** `/ads/{ad_id}` - Get ad
- **PUT** `/ads/{ad_id}` - Update ad

## Creative Management

### Media
- **POST** `/adaccounts/{ad_account_id}/media` - Create media
- **GET** `/media/{media_id}` - Get media

### Creatives
- **POST** `/adaccounts/{ad_account_id}/creatives` - Create creatives (bulk)
- **GET** `/creatives/{creative_id}` - Get creative
- **PUT** `/creatives/{creative_id}` - Update creative

## Audience Management

### Segments (Audiences)
- **POST** `/adaccounts/{ad_account_id}/segments` - Create segment
- **GET** `/adaccounts/{ad_account_id}/segments` - List segments
- **GET** `/segments/{segment_id}` - Get segment

### Pixels
- **POST** `/adaccounts/{ad_account_id}/pixels` - Create pixel
- **GET** `/adaccounts/{ad_account_id}/pixels` - List pixels

## Reporting

### Campaign Stats
- **GET** `/campaigns/{campaign_id}/stats` - Get campaign statistics
- **GET** `/adsquads/{adsquad_id}/stats` - Get ad squad statistics
- **GET** `/ads/{ad_id}/stats` - Get ad statistics

## Rate Limits
- 1000 requests per hour
- 100 requests per minute (burst)
