# Reddit Ads API Authentication and Setup Guide

## Overview
The Reddit Ads API enables programmatic campaign management, audience targeting, and reporting automation. Proper authentication is essential for secure API access.

## Authentication Method: OAuth 2.0

### Prerequisites
- Active Reddit Ads account
- Reddit account with API access
- Developer application credentials

### Step 1: Create Reddit Application
1. Navigate to https://www.reddit.com/prefs/apps/
2. Click "create app" or "create another app"
3. Fill in application details:
   - **Name:** Your application name
   - **Type:** Select "script"
   - **Description:** Optional
   - **Redirect URI:** https://your-domain.com/callback
4. Click "create app"
5. Note your **Client ID** and **Client Secret**

### Step 2: Request Authorization
**Authorization URL:**
```
https://www.reddit.com/api/v1/authorize?
client_id=YOUR_CLIENT_ID&
response_type=code&
state=RANDOM_STRING&
redirect_uri=YOUR_REDIRECT_URI&
duration=permanent&
scope=adsread,history
```

**Scopes:**
- `ads:read` - Read access to ad account data
- `ads:manage` - Write access for campaign management

### Step 3: Exchange Code for Access Token
**Request:**
```bash
curl -X POST https://www.reddit.com/api/v1/access_token \
  -H 'content-type: application/x-www-form-urlencoded' \
  -u CLIENT_ID:CLIENT_SECRET \
  -d 'grant_type=authorization_code&code=AUTH_CODE&redirect_uri=REDIRECT_URI'
```

**Response:**
```json
{
  "access_token": "your_access_token",
  "token_type": "bearer",
  "expires_in": 3600,
  "refresh_token": "your_refresh_token",
  "scope": "adsread history"
}
```

### Step 4: Refresh Access Token
**Request:**
```bash
curl -X POST https://www.reddit.com/api/v1/access_token \
  -u CLIENT_ID:CLIENT_SECRET \
  -d 'grant_type=refresh_token&refresh_token=REFRESH_TOKEN'
```

### Making API Requests
**Base URL:** `https://ads-api.reddit.com/api/v3`

**Headers:**
```
Authorization: Bearer YOUR_ACCESS_TOKEN
Content-Type: application/json
```

**Example Request:**
```bash
curl -X GET https://ads-api.reddit.com/api/v3/accounts \
  -H 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
  -H 'Content-Type: application/json'
```

## Best Practices
- Store credentials securely
- Refresh tokens before expiration
- Implement error handling
- Use HTTPS for all requests
- Monitor rate limits

## Conclusion
Proper authentication setup enables secure, automated access to Reddit Ads API for campaign management and optimization.
