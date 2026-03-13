# Taboola API Authentication

OAuth 2.0 Client Credentials implementation guide.

## Getting Access Token

**Endpoint:** `POST https://backstage.taboola.com/backstage/oauth/token`

**Parameters:**
- `client_id`: Your client ID
- `client_secret`: Your client secret
- `grant_type`: `client_credentials`

**Example:**
```bash
curl -X POST 'https://backstage.taboola.com/backstage/oauth/token' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'client_id=YOUR_ID' \
  -d 'client_secret=YOUR_SECRET' \
  -d 'grant_type=client_credentials'
```

**Response:**
```json
{
  "access_token": "abc123...",
  "token_type": "bearer",
  "expires_in": 43200
}
```

## Using Token

Include in Authorization header:
```
Authorization: Bearer YOUR_ACCESS_TOKEN
```

## Token Management

- Tokens expire after 12 hours
- Refresh before expiration
- Implement automatic refresh logic
- Handle 401 errors (expired token)

## Python Example

```python
import requests

def get_token(client_id, client_secret):
    url = 'https://backstage.taboola.com/backstage/oauth/token'
    data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'client_credentials'
    }
    response = requests.post(url, data=data)
    return response.json()['access_token']
```
