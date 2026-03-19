# Meta Ads Campaign API: Best Practices and Troubleshooting

This comprehensive guide covers best practices, common pitfalls, troubleshooting strategies, and optimization techniques for working with the Meta Ads Campaign API.

## API Best Practices

### Authentication and Security

#### Access Token Management

**Use System User Tokens for Production**
- Most reliable for long-term automation
- Not tied to individual user login status
- Non-expiring if properly maintained
- Ideal for server-to-server integrations

**Secure Token Storage**
```python
import os
from cryptography.fernet import Fernet

# Store tokens in environment variables
access_token = os.environ.get('META_ACCESS_TOKEN')

# Or use encryption for stored tokens
def encrypt_token(token, key):
    f = Fernet(key)
    return f.encrypt(token.encode())

def decrypt_token(encrypted_token, key):
    f = Fernet(key)
    return f.decrypt(encrypted_token).decode()
```

**Never Expose Tokens**
- Don't hardcode in source code
- Don't commit to version control
- Don't log in plain text
- Don't expose in client-side code
- Don't include in error messages

**Token Rotation Schedule**
- Rotate tokens every 60-90 days
- Implement automated rotation
- Test rotation process regularly
- Document rotation procedures
- Monitor token expiration

#### App Secret Protection

**Server-Side Only**
- Never expose in client-side code
- Use only for server-to-server communication
- Store securely with encryption
- Implement access controls

**Use for Critical Operations**
- Token exchange
- OAuth authentication
- Webhook verification
- Secure API calls

### Rate Limit Management

#### Understanding Rate Limits

**Limit Types**
- **App-level limits**: Total calls per app per hour
- **User-level limits**: Calls per user token per hour
- **Ad account-level limits**: Calls per ad account per hour

**Calculation**
- Based on rolling 1-hour window
- Considers both call frequency and data volume
- Varies by app permissions and verification status

**Rate Limit Headers**
```python
import requests

response = requests.get(url, params=params)

# Check rate limit headers
usage = response.headers.get('X-Business-Use-Case-Usage')
app_usage = response.headers.get('X-App-Usage')
page_usage = response.headers.get('X-Page-Usage')

print(f"Business Use Case Usage: {usage}")
print(f"App Usage: {app_usage}")
```

#### Rate Limit Best Practices

**Implement Exponential Backoff**
```python
import time
import random

def exponential_backoff(attempt, base_delay=1, max_delay=60):
    delay = min(base_delay * (2 ** attempt) + random.uniform(0, 1), max_delay)
    return delay

def api_call_with_backoff(url, params, max_retries=5):
    for attempt in range(max_retries):
        try:
            response = requests.post(url, data=params)
            
            if response.status_code == 429:  # Rate limit
                delay = exponential_backoff(attempt)
                print(f"Rate limited. Waiting {delay:.2f} seconds...")
                time.sleep(delay)
                continue
            
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.HTTPError as e:
            if attempt == max_retries - 1:
                raise
    
    raise Exception("Max retries exceeded")
```

**Use Batch Requests**
```python
def batch_create_campaigns(campaigns, ad_account_id, access_token):
    batch_requests = []
    
    for campaign in campaigns:
        batch_requests.append({
            'method': 'POST',
            'relative_url': f'act_{ad_account_id}/campaigns',
            'body': f"name={campaign['name']}&objective={campaign['objective']}&status=PAUSED&special_ad_categories=[]"
        })
    
    # Send batch request (max 50 per batch)
    url = 'https://graph.facebook.com/v18.0/'
    params = {
        'batch': json.dumps(batch_requests),
        'access_token': access_token
    }
    
    response = requests.post(url, data=params)
    return response.json()
```

**Implement Request Queuing**
```python
import queue
import threading
import time

class APIRequestQueue:
    def __init__(self, max_requests_per_hour=200):
        self.queue = queue.Queue()
        self.max_requests = max_requests_per_hour
        self.request_times = []
        self.lock = threading.Lock()
    
    def add_request(self, func, *args, **kwargs):
        self.queue.put((func, args, kwargs))
    
    def process_queue(self):
        while True:
            if not self.queue.empty():
                func, args, kwargs = self.queue.get()
                
                # Wait if rate limit reached
                self._wait_if_needed()
                
                # Execute request
                try:
                    result = func(*args, **kwargs)
                    print(f"Request completed: {result}")
                except Exception as e:
                    print(f"Request failed: {e}")
                
                self.queue.task_done()
            else:
                time.sleep(1)
    
    def _wait_if_needed(self):
        with self.lock:
            now = time.time()
            
            # Remove requests older than 1 hour
            self.request_times = [t for t in self.request_times if now - t < 3600]
            
            if len(self.request_times) >= self.max_requests:
                sleep_time = 3600 - (now - self.request_times[0]) + 1
                print(f"Rate limit reached. Waiting {sleep_time:.0f} seconds...")
                time.sleep(sleep_time)
                self.request_times = []
            
            self.request_times.append(now)
```

### Data Validation

#### Input Validation

**Validate Before API Calls**
```python
def validate_campaign_params(name, objective, daily_budget, special_ad_categories):
    errors = []
    
    # Name validation
    if not name or not isinstance(name, str):
        errors.append("Campaign name must be a non-empty string")
    elif len(name) > 400:
        errors.append("Campaign name must be 400 characters or less")
    
    # Objective validation
    valid_objectives = [
        'BRAND_AWARENESS', 'REACH', 'LINK_CLICKS', 'POST_ENGAGEMENT',
        'PAGE_LIKES', 'EVENT_RESPONSES', 'CONVERSIONS', 'PRODUCT_CATALOG_SALES',
        'STORE_VISITS', 'LEAD_GENERATION', 'MESSAGES', 'APP_INSTALLS'
    ]
    if objective not in valid_objectives:
        errors.append(f"Invalid objective. Must be one of: {', '.join(valid_objectives)}")
    
    # Budget validation
    if daily_budget is not None:
        if not isinstance(daily_budget, int) or daily_budget < 100:
            errors.append("Daily budget must be an integer >= 100 (cents)")
    
    # Special ad categories validation
    if not isinstance(special_ad_categories, list):
        errors.append("Special ad categories must be a list")
    
    valid_categories = ['HOUSING', 'EMPLOYMENT', 'CREDIT', 'ISSUES_ELECTIONS_POLITICS']
    for category in special_ad_categories:
        if category not in valid_categories:
            errors.append(f"Invalid special ad category: {category}")