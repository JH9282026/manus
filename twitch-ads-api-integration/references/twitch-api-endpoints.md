# Twitch API Ad Endpoints Reference

Complete documentation for Twitch API endpoints related to advertising and commercial management.

---

## Authentication

### OAuth 2.0 Setup

**Authorization Flow:**
1. Register application at dev.twitch.tv
2. Obtain Client ID and Client Secret
3. Request user authorization
4. Exchange authorization code for access token
5. Use access token in API requests

**Required Scopes for Ad Endpoints:**
- `channel:edit:commercial` - Start commercials
- `channel:read:ads` - Read ad schedule information
- `channel:manage:ads` - Manage ad settings (snooze)

**Token Format:**
```
Authorization: Bearer <access_token>
Client-Id: <client_id>
```

---

## Start Commercial

### Endpoint Details

**URL:** `POST https://api.twitch.tv/helix/channels/commercial`

**Authentication:** User access token with `channel:edit:commercial` scope

**Rate Limits:** Subject to Twitch API rate limits

### Request

**Headers:**
```
Authorization: Bearer 2gbdx6oar67tqtcmt49t3wpcgycthx
Client-Id: wbmytr93xzw8zbg0p1izqyzzc5mbiz
Content-Type: application/json
```

**Body:**
```json
{
  "broadcaster_id": "141981764",
  "length": 60
}
```

**Parameters:**
- `broadcaster_id` (string, required): ID of partner/affiliate broadcaster
- `length` (integer, required): Commercial length in seconds (max 180)

### Response

**Success (200 OK):**
```json
{
  "data": [{
    "length": 60,
    "message": "",
    "retry_after": 480
  }]
}
```

**Response Fields:**
- `length`: Requested commercial length (capped at 180 if longer requested)
- `message`: Status message (empty if successful)
- `retry_after`: Seconds until next commercial can be run

### Error Responses

**400 Bad Request:**
- Missing `broadcaster_id` or `length`
- Invalid `broadcaster_id`
- Broadcaster not streaming live
- Cooldown period not expired

**401 Unauthorized:**
- Invalid or expired access token
- Missing `channel:edit:commercial` scope
- `broadcaster_id` doesn't match token user ID

**404 Not Found:**
- `broadcaster_id` not found

**429 Too Many Requests:**
- Cooldown period not expired
- Check `retry_after` from previous response

### Example Implementation

**Python:**
```python
import requests

def start_commercial(broadcaster_id, length, access_token, client_id):
    url = "https://api.twitch.tv/helix/channels/commercial"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Client-Id": client_id,
        "Content-Type": "application/json"
    }
    data = {
        "broadcaster_id": broadcaster_id,
        "length": length
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        result = response.json()["data"][0]
        print(f"Commercial started: {result['length']}s")
        print(f"Next commercial in: {result['retry_after']}s")
        return result
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None
```

---

## Get Ad Schedule

### Endpoint Details

**URL:** `GET https://api.twitch.tv/helix/channels/ads`

**Authentication:** User access token with `channel:read:ads` scope

### Request

**Headers:**
```
Authorization: Bearer 2gbdx6oar67tqtcmt49t3wpcgycthx
Client-Id: wbmytr93xzw8zbg0p1izqyzzc5mbiz
```

**Query Parameters:**
- `broadcaster_id` (string, required): Must match user ID in access token

**Example:**
```
GET https://api.twitch.tv/helix/channels/ads?broadcaster_id=141981764
```

### Response

**Success (200 OK):**
```json
{
  "data": [{
    "next_ad_at": "2023-08-01T23:08:18+00:00",
    "last_ad_at": "2023-08-01T23:08:18+00:00",
    "duration": "60",
    "preroll_free_time": "90",
    "snooze_count": "1",
    "snooze_refresh_at": "2023-08-01T23:08:18+00:00"
  }]
}
```

**Response Fields:**
- `next_ad_at`: UTC timestamp of next scheduled ad (RFC3339 format)
- `last_ad_at`: UTC timestamp of last ad break
- `duration`: Length of upcoming ad break in seconds
- `preroll_free_time`: Remaining pre-roll free time in seconds
- `snooze_count`: Number of snoozes available
- `snooze_refresh_at`: UTC timestamp when next snooze becomes available

### Error Responses

**400 Bad Request:**
- Invalid `broadcaster_id`

**401 Unauthorized:**
- Invalid or expired access token
- Missing `channel:read:ads` scope

### Example Implementation

**Python:**
```python
def get_ad_schedule(broadcaster_id, access_token, client_id):
    url = f"https://api.twitch.tv/helix/channels/ads?broadcaster_id={broadcaster_id}"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Client-Id": client_id
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()["data"][0]
        print(f"Next ad: {data['next_ad_at']}")
        print(f"Duration: {data['duration']}s")
        print(f"Snoozes available: {data['snooze_count']}")
        print(f"Pre-roll free time: {data['preroll_free_time']}s")
        return data
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None
```

---

## Snooze Next Ad

### Endpoint Details

**URL:** `POST https://api.twitch.tv/helix/channels/ads/schedule/snooze`

**Authentication:** User access token with `channel:manage:ads` scope

**Functionality:** Delays next automatic mid-roll ad by 5 minutes

### Request

**Headers:**
```
Authorization: Bearer 2gbdx6oar67tqtcmt49t3wpcgycthx
Client-Id: wbmytr93xzw8zbg0p1izqyzzc5mbiz
```

**Query Parameters:**
- `broadcaster_id` (string, required): Must match user ID in access token

**Example:**
```
POST https://api.twitch.tv/helix/channels/ads/schedule/snooze?broadcaster_id=123
```

### Response

**Success (200 OK):**
```json
{
  "data": [{
    "snooze_count": "1",
    "snooze_refresh_at": "2023-08-01T23:08:18+00:00",
    "next_ad_at": "2023-08-01T23:08:18+00:00"
  }]
}
```

**Response Fields:**
- `snooze_count`: Remaining snoozes available
- `snooze_refresh_at`: UTC timestamp when next snooze becomes available
- `next_ad_at`: Updated UTC timestamp of next scheduled ad

### Error Responses

**400 Bad Request:**
- Channel not currently live
- Invalid `broadcaster_id`
- No upcoming scheduled ad break

**429 Too Many Requests:**
- No snoozes remaining

### Example Implementation

**Python:**
```python
def snooze_next_ad(broadcaster_id, access_token, client_id):
    url = f"https://api.twitch.tv/helix/channels/ads/schedule/snooze?broadcaster_id={broadcaster_id}"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Client-Id": client_id
    }
    
    response = requests.post(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()["data"][0]
        print(f"Ad snoozed! Next ad: {data['next_ad_at']}")
        print(f"Snoozes remaining: {data['snooze_count']}")
        return data
    elif response.status_code == 429:
        print("No snoozes remaining")
        return None
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None
```

---

## Complete Integration Example

**Automated Ad Management System:**

```python
import requests
import time
from datetime import datetime, timedelta

class TwitchAdManager:
    def __init__(self, broadcaster_id, access_token, client_id):
        self.broadcaster_id = broadcaster_id
        self.access_token = access_token
        self.client_id = client_id
        self.base_url = "https://api.twitch.tv/helix"
    
    def _headers(self):
        return {
            "Authorization": f"Bearer {self.access_token}",
            "Client-Id": self.client_id,
            "Content-Type": "application/json"
        }
    
    def get_ad_schedule(self):
        url = f"{self.base_url}/channels/ads?broadcaster_id={self.broadcaster_id}"
        response = requests.get(url, headers=self._headers())
        if response.status_code == 200:
            return response.json()["data"][0]
        return None
    
    def start_commercial(self, length=60):
        url = f"{self.base_url}/channels/commercial"
        data = {
            "broadcaster_id": self.broadcaster_id,
            "length": length
        }
        response = requests.post(url, headers=self._headers(), json=data)
        if response.status_code == 200:
            return response.json()["data"][0]
        return None
    
    def snooze_ad(self):
        url = f"{self.base_url}/channels/ads/schedule/snooze?broadcaster_id={self.broadcaster_id}"
        response = requests.post(url, headers=self._headers())
        if response.status_code == 200:
            return response.json()["data"][0]
        return None
    
    def auto_manage_ads(self, target_interval_minutes=15):
        """
        Automatically manage ad breaks to maintain pre-roll free time
        """
        schedule = self.get_ad_schedule()
        if not schedule:
            return
        
        preroll_free_time = int(schedule["preroll_free_time"])
        
        # If pre-roll free time is running low, run an ad
        if preroll_free_time < 300:  # Less than 5 minutes
            print("Pre-roll free time low, starting commercial...")
            result = self.start_commercial(60)
            if result:
                print(f"Commercial started. Next in {result['retry_after']}s")
        else:
            print(f"Pre-roll free time: {preroll_free_time}s - OK")

# Usage
manager = TwitchAdManager(
    broadcaster_id="YOUR_BROADCASTER_ID",
    access_token="YOUR_ACCESS_TOKEN",
    client_id="YOUR_CLIENT_ID"
)

# Run ad management loop
while True:
    manager.auto_manage_ads()
    time.sleep(300)  # Check every 5 minutes
```

---

## Best Practices

### Error Handling

- Always check response status codes
- Handle rate limits gracefully (429 errors)
- Implement exponential backoff for retries
- Log errors for debugging
- Provide user-friendly error messages

### Token Management

- Securely store access tokens
- Implement token refresh logic
- Handle token expiration
- Never expose tokens in client-side code
- Use environment variables for credentials

### Rate Limiting

- Respect Twitch API rate limits
- Implement request throttling
- Cache responses when appropriate
- Use webhooks/EventSub for real-time updates instead of polling

### Monitoring

- Log all API requests and responses
- Track success/failure rates
- Monitor for anomalies
- Set up alerts for errors
- Regular health checks
