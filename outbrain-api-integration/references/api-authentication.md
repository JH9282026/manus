# Outbrain API Authentication

Token-based authentication for Outbrain Amplify API.

## Getting Access Token

### Via Web Interface
1. Log into Outbrain account
2. Navigate to account dropdown
3. Select "Amplify API Token"
4. Generate new token

### Via API (Basic Auth)
```bash
curl -u USER:PASSWORD https://api.outbrain.com/amplify/v0.1/login
```

**Response:**
```json
{
  "OB-TOKEN-V1": "your_token_here"
}
```

## Using Token

Include in request header:
```
OB-TOKEN-V1: your_token_here
```

**Example:**
```bash
curl -H "OB-TOKEN-V1: your_token" \
  https://api.outbrain.com/amplify/v0.1/marketers
```

## Token Management

- Tokens valid for 30 days
- Generate new token before expiration
- Store securely
- Don't share tokens

## Rate Limits

- **Authentication**: 2 requests/hour per user
- **Token usage**: 30 requests/second
- **Performance API**: 10 requests/minute per marketer
- **Realtime API**: 50 requests/minute per marketer

## Error Handling

**401 Unauthorized:**
- Invalid token
- Expired token
- Solution: Generate new token

**429 Too Many Requests:**
- Rate limit exceeded
- Solution: Implement backoff, reduce request rate

## Python Example

```python
import requests

class OutbrainAPI:
    def __init__(self, token):
        self.token = token
        self.base_url = 'https://api.outbrain.com/amplify/v0.1'
        self.headers = {'OB-TOKEN-V1': token}
    
    def get_marketers(self):
        url = f'{self.base_url}/marketers'
        response = requests.get(url, headers=self.headers)
        return response.json()
```
