# Microsoft Ads API Best Practices and Troubleshooting

## Introduction

Successful Microsoft Ads API integration requires more than just understanding the technical specifications. This guide covers best practices for development, deployment, and maintenance, along with common issues and their solutions to ensure reliable, efficient, and scalable API implementations.

## Development Best Practices

### Code Organization

#### Separation of Concerns

Organize code into logical modules:

```python
# config.py - Configuration management
import os

class Config:
    CLIENT_ID = os.environ.get('BING_ADS_CLIENT_ID')
    CLIENT_SECRET = os.environ.get('BING_ADS_CLIENT_SECRET')
    DEVELOPER_TOKEN = os.environ.get('BING_ADS_DEVELOPER_TOKEN')
    REDIRECT_URI = os.environ.get('BING_ADS_REDIRECT_URI')
    ACCOUNT_ID = os.environ.get('BING_ADS_ACCOUNT_ID')
    CUSTOMER_ID = os.environ.get('BING_ADS_CUSTOMER_ID')
    ENVIRONMENT = os.environ.get('BING_ADS_ENVIRONMENT', 'production')

# auth.py - Authentication handling
from bingads import AuthorizationData, OAuthWebAuthCodeGrant
import json

class AuthManager:
    def __init__(self, config):
        self.config = config
        self.oauth = OAuthWebAuthCodeGrant(
            client_id=config.CLIENT_ID,
            client_secret=config.CLIENT_SECRET,
            redirection_uri=config.REDIRECT_URI
        )
        self.load_refresh_token()
    
    def load_refresh_token(self):
        try:
            with open('tokens.json', 'r') as f:
                tokens = json.load(f)
                self.oauth.refresh_token = tokens.get('refresh_token')
        except FileNotFoundError:
            pass
    
    def save_refresh_token(self):
        with open('tokens.json', 'w') as f:
            json.dump({'refresh_token': self.oauth.refresh_token}, f)
    
    def get_authorization_data(self):
        return AuthorizationData(
            account_id=self.config.ACCOUNT_ID,
            customer_id=self.config.CUSTOMER_ID,
            developer_token=self.config.DEVELOPER_TOKEN,
            authentication=self.oauth
        )

# services.py - Service client wrappers
from bingads.service_client import ServiceClient

class BingAdsServices:
    def __init__(self, authorization_data):
        self.authorization_data = authorization_data
    
    def get_campaign_service(self):
        return ServiceClient(
            service='CampaignManagementService',
            version=13,
            authorization_data=self.authorization_data
        )
    
    def get_reporting_service(self):
        return ServiceClient(
            service='ReportingService',
            version=13,
            authorization_data=self.authorization_data
        )

# main.py - Application logic
from config import Config
from auth import AuthManager
from services import BingAdsServices

def main():
    config = Config()
    auth_manager = AuthManager(config)
    authorization_data = auth_manager.get_authorization_data()
    services = BingAdsServices(authorization_data)
    
    campaign_service = services.get_campaign_service()
    # Your business logic here
```

#### Configuration Management

**Use Environment Variables:**

```python
import os
from dotenv import load_dotenv

# Load from .env file
load_dotenv()

CLIENT_ID = os.environ.get('BING_ADS_CLIENT_ID')
CLIENT_SECRET = os.environ.get('BING_ADS_CLIENT_SECRET')
```

**.env file (never commit to version control):**

```
BING_ADS_CLIENT_ID=your_client_id
BING_ADS_CLIENT_SECRET=your_client_secret
BING_ADS_DEVELOPER_TOKEN=your_developer_token
BING_ADS_REDIRECT_URI=https://your-app.com/callback
BING_ADS_ACCOUNT_ID=123456789
BING_ADS_CUSTOMER_ID=987654321
BING_ADS_ENVIRONMENT=production
```

**.gitignore:**

```
.env
tokens.json
refresh_token.txt
*.pyc
__pycache__/
```

### Error Handling

#### Comprehensive Exception Handling

```python
from bingads.exceptions import (
    OAuthTokenRequestException,
    FaultException,
    TimeoutException
)
from suds import WebFault
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def safe_api_call(func, *args, **kwargs):
    """Wrapper for safe API calls with comprehensive error handling."""
    try:
        return func(*args, **kwargs)
    
    except OAuthTokenRequestException as e:
        logger.error(f"OAuth error: {e.error_description}")
        # Trigger re-authentication
        raise
    
    except FaultException as e:
        logger.error(f"API Fault: {e.message}")
        logger.error(f"Error Code: {e.error_code}")
        logger.error(f"Details: {e.details}")
        raise
    
    except WebFault as e:
        logger.error(f"SOAP Fault: {e}")
        raise
    
    except TimeoutException as e:
        logger.error(f"Timeout: {e}")
        raise
    
    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
        raise

# Usage
campaigns = safe_api_call(
    campaign_service.GetCampaignsByAccountId,
    AccountId=account_id
)
```

#### Retry Logic with Exponential Backoff

```python
import time
from functools import wraps

def retry_with_backoff(max_retries=3, base_delay=1, max_delay=60):
    """Decorator for retry logic with exponential backoff."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except (TimeoutException, WebFault) as e:
                    if attempt == max_retries - 1:
                        raise
                    
                    delay = min(base_delay * (2 ** attempt), max_delay)
                    logger.warning(
                        f"Attempt {attempt + 1} failed: {e}. "
                        f"Retrying in {delay}s..."
                    )
                    time.sleep(delay)
            
            raise Exception(f"Max retries ({max_retries}) exceeded")
        
        return wrapper
    return decorator

# Usage
@retry_with_backoff(max_retries=3)
def get_campaigns():
    return campaign_service.GetCampaignsByAccountId(
        AccountId=account_id
    )
```

### Rate Limiting

#### Implement Rate Limit Handling

```python
import time
from collections import deque
from datetime import datetime, timedelta

class RateLimiter:
    """Simple rate limiter for API calls."""
    
    def __init__(self, max_calls, time_window):
        """
        Args:
            max_calls: Maximum number of calls allowed
            time_window: Time window in seconds
        """
        self.max_calls = max_calls
        self.time_window = time_window
        self.calls = deque()
    
    def wait_if_needed(self):
        """Wait if rate limit would be exceeded."""
        now = datetime.now()
        
        # Remove old calls outside time window
        while self.calls and self.calls[0] < now - timedelta(seconds=self.time_window):
            self.calls.popleft()
        
        # Check if we need to wait
        if len(self.calls) >= self.max_calls:
            sleep_time = (self.calls[0] + timedelta(seconds=self.time_window) - now).total_seconds()
            if sleep_time > 0:
                logger.info(f"Rate limit reached. Waiting {sleep_time:.2f}s...")
                time.sleep(sleep_time)
                self.wait_if_needed()  # Recursive check
        
        # Record this call
        self.calls.append(now)

# Usage
rate_limiter = RateLimiter(max_calls=100, time_window=60)  # 100 calls per minute

def rate_limited_api_call(func, *args, **kwargs):
    rate_limiter.wait_if_needed()
    return func(*args, **kwargs)

campaigns = rate_limited_api_call(
    campaign_service.GetCampaignsByAccountId,
    AccountId=account_id
)
```

### Logging

#### Comprehensive Logging Strategy

```python
import logging
from logging.handlers import RotatingFileHandler
import json

# Configure logging
def setup_logging(log_file='bing_ads_api.log', level=logging.INFO):
    """Setup comprehensive logging."""
    
    # Create logger
    logger = logging.getLogger('bing_ads')
    logger.setLevel(level)
    
    # File handler with rotation
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=10*1024*1024,  # 10MB
        backupCount=5
    )
    file_handler.setLevel(level)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)
    
    # Formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # Add handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

logger = setup_logging()

# Log API calls
def log_api_call(service_name, operation, params, response=None, error=None):
    """Log API call details."""
    log_data = {
        'service': service_name,
        'operation': operation,
        'params': params,
        'timestamp': datetime.now().isoformat()
    }
    
    if response:
        log_data['response'] = str(response)[:500]  # Truncate long responses
    
    if error:
        log_data['error'] = str(error)
        logger.error(f"API Call Failed: {json.dumps(log_data)}")
    else:
        logger.info(f"API Call Success: {json.dumps(log_data)}")

# Usage
try:
    campaigns = campaign_service.GetCampaignsByAccountId(
        AccountId=account_id
    )
    log_api_call(
        'CampaignManagementService',
        'GetCampaignsByAccountId',
        {'AccountId': account_id},
        response=f"{len(campaigns['Campaign'])} campaigns"
    )
except Exception as e:
    log_api_call(
        'CampaignManagementService',
        'GetCampaignsByAccountId',
        {'AccountId': account_id},
        error=e
    )
    raise
```

### Testing

#### Unit Testing

```python
import unittest
from unittest.mock import Mock, patch
from your_module import BingAdsServices

class TestBingAdsServices(unittest.TestCase):
    
    def setUp(self):
        self.mock_auth_data = Mock()
        self.services = BingAdsServices(self.mock_auth_data)
    
    @patch('bingads.service_client.ServiceClient')
    def test_get_campaigns(self, mock_service_client):
        # Setup mock
        mock_service = Mock()
        mock_service.GetCampaignsByAccountId.return_value = {
            'Campaign': [
                Mock(Name='Test Campaign', Id=123)
            ]
        }
        mock_service_client.return_value = mock_service
        
        # Test
        campaign_service = self.services.get_campaign_service()
        campaigns = campaign_service.GetCampaignsByAccountId(
            AccountId=123456
        )
        
        # Assert
        self.assertEqual(len(campaigns['Campaign']), 1)
        self.assertEqual(campaigns['Campaign'][0].Name, 'Test Campaign')

if __name__ == '__main__':
    unittest.main()
```

#### Integration Testing with Sandbox

```python
import unittest
from config import Config
from auth import AuthManager
from services import BingAdsServices

class TestBingAdsIntegration(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Use sandbox environment
        config = Config()
        config.ENVIRONMENT = 'sandbox'
        config.DEVELOPER_TOKEN = 'BBD37VB98'  # Sandbox token
        
        auth_manager = AuthManager(config)
        cls.authorization_data = auth_manager.get_authorization_data()
        cls.services = BingAdsServices(cls.authorization_data)
    
    def test_create_and_delete_campaign(self):
        campaign_service = self.services.get_campaign_service()
        
        # Create campaign
        from bingads.v13.campaignmanagement import Campaign
        campaign = Campaign(
            Name='Integration Test Campaign',
            BudgetType='DailyBudgetStandard',
            DailyBudget=10.00,
            TimeZone='EasternTimeUSCanada',
            CampaignType='Search',
            Status='Paused',
            Languages=['English']
        )
        
        response = campaign_service.AddCampaigns(
            AccountId=self.authorization_data.account_id,
            Campaigns=[campaign]
        )
        
        campaign_id = response.CampaignIds['long'][0]
        self.assertIsNotNone(campaign_id)
        
        # Delete campaign
        campaign_service.DeleteCampaigns(
            AccountId=self.authorization_data.account_id,
            CampaignIds=[campaign_id]
        )

if __name__ == '__main__':
    unittest.main()
```

## Deployment Best Practices

### Environment Management

#### Separate Environments

```python
class EnvironmentConfig:
    """Environment-specific configuration."""
    
    ENVIRONMENTS = {
        'development': {
            'environment': 'sandbox',
            'developer_token': 'BBD37VB98',
            'log_level': logging.DEBUG
        },
        'staging': {
            'environment': 'production',
            'developer_token': os.environ.get('STAGING_DEVELOPER_TOKEN'),
            'log_level': logging.INFO
        },
        'production': {
            'environment': 'production',
            'developer_token': os.environ.get('PROD_DEVELOPER_TOKEN'),
            'log_level': logging.WARNING
        }
    }
    
    @classmethod
    def get_config(cls, env_name):
        return cls.ENVIRONMENTS.get(env_name, cls.ENVIRONMENTS['development'])

# Usage
env = os.environ.get('APP_ENV', 'development')
config = EnvironmentConfig.get_config(env)
```

### Monitoring and Alerting

#### Health Checks

```python
def health_check():
    """Verify API connectivity and authentication."""
    try:
        # Test authentication
        customer_service = ServiceClient(
            service='CustomerManagementService',
            version=13,
            authorization_data=authorization_data
        )
        
        user = customer_service.GetUser()
        
        return {
            'status': 'healthy',
            'user_id': user.Id,
            'timestamp': datetime.now().isoformat()
        }
    
    except Exception as e:
        return {
            'status': 'unhealthy',
            'error': str(e),
            'timestamp': datetime.now().isoformat()
        }

# Run periodically
import schedule

def check_health():
    health = health_check()
    if health['status'] != 'healthy':
        send_alert(f"API Health Check Failed: {health['error']}")

schedule.every(5).minutes.do(check_health)
```

#### Performance Monitoring

```python
import time
from functools import wraps

def monitor_performance(func):
    """Decorator to monitor function performance."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        
        try:
            result = func(*args, **kwargs)
            duration = time.time() - start_time
            
            logger.info(
                f"{func.__name__} completed in {duration:.2f}s"
            )
            
            # Alert if slow
            if duration > 30:  # 30 seconds threshold
                send_alert(
                    f"{func.__name__} took {duration:.2f}s (slow performance)"
                )
            
            return result
        
        except Exception as e:
            duration = time.time() - start_time
            logger.error(
                f"{func.__name__} failed after {duration:.2f}s: {e}"
            )
            raise
    
    return wrapper

@monitor_performance
def generate_daily_report():
    # Report generation logic
    pass
```

## Common Issues and Troubleshooting

### Authentication Issues

#### Issue: "Invalid Client" Error

**Symptoms:**
```json
{
  "error": "invalid_client",
  "error_description": "Client authentication failed"
}
```

**Causes:**
- Incorrect client_id or client_secret
- Client secret expired
- Application not registered properly

**Solutions:**
1. Verify credentials in Azure AD
2. Generate new client secret if expired
3. Check application registration status
4. Ensure client_id and client_secret match exactly

#### Issue: "Invalid Grant" Error

**Symptoms:**
```json
{
  "error": "invalid_grant",
  "error_description": "The provided authorization code is invalid or expired"
}
```

**Causes:**
- Authorization code already used
- Authorization code expired (>5 minutes)
- Refresh token expired or revoked

**Solutions:**
1. Request new authorization code
2. Exchange code immediately after receiving
3. Re-authenticate user if refresh token invalid
4. Ensure refresh token is saved and loaded correctly

#### Issue: Refresh Token Not Working

**Symptoms:**
- Refresh token request fails
- User must re-authenticate frequently

**Causes:**
- Refresh token not saved after token exchange
- Refresh token expired (90 days of inactivity)
- Using old refresh token instead of new one

**Solutions:**
1. Always save the latest refresh token from token responses
2. Implement automated token refresh before expiration
3. Monitor refresh token usage and expiration

```python
def refresh_access_token(oauth):
    """Refresh access token and save new refresh token."""
    try:
        # Request new tokens
        oauth.request_oauth_tokens_by_refresh_token(oauth.refresh_token)
        
        # Save new refresh token
        with open('tokens.json', 'w') as f:
            json.dump({
                'refresh_token': oauth.refresh_token,
                'updated_at': datetime.now().isoformat()
            }, f)
        
        logger.info("Access token refreshed successfully")
    
    except OAuthTokenRequestException as e:
        logger.error(f"Token refresh failed: {e.error_description}")
        # Trigger re-authentication
        raise
```

### API Call Issues

#### Issue: "EntityNotFound" Error

**Symptoms:**
```
FaultException: Entity not found
```

**Causes:**
- Incorrect entity ID
- Entity deleted
- Wrong account/customer ID

**Solutions:**
1. Verify entity ID is correct
2. Check entity still exists
3. Ensure using correct account_id and customer_id
4. Use GetCampaignsByAccountId to list available entities

#### Issue: Rate Limit Exceeded (HTTP 429)

**Symptoms:**
- HTTP 429 Too Many Requests
- API calls failing intermittently

**Solutions:**
1. Implement rate limiting (see Rate Limiting section)
2. Add exponential backoff retry logic
3. Batch operations when possible
4. Distribute requests over time

```python
def handle_rate_limit(func, *args, **kwargs):
    """Handle rate limit errors with retry."""
    max_retries = 5
    
    for attempt in range(max_retries):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            if '429' in str(e) or 'rate limit' in str(e).lower():
                wait_time = 2 ** attempt  # Exponential backoff
                logger.warning(
                    f"Rate limited. Waiting {wait_time}s before retry..."
                )
                time.sleep(wait_time)
            else:
                raise
    
    raise Exception("Rate limit retries exceeded")
```

#### Issue: Timeout Errors

**Symptoms:**
- TimeoutException
- Operations taking too long

**Solutions:**
1. Increase timeout values
2. Use bulk operations for large datasets
3. Break large operations into smaller batches
4. Use asynchronous operations when available

```python
# Increase timeout
reporting_service_manager = ReportingServiceManager(
    authorization_data=authorization_data,
    poll_interval_in_milliseconds=10000,  # 10 seconds
    environment='production',
    timeout_in_milliseconds=7200000  # 2 hours
)
```

### Data Issues

#### Issue: Incomplete Report Data

**Symptoms:**
- Missing rows in reports
- Data doesn't match UI

**Causes:**
- ReturnOnlyCompleteData set incorrectly
- Time period includes current day
- Data still processing

**Solutions:**
1. Set ReturnOnlyCompleteData=True for historical data
2. Exclude current day from time range
3. Wait for data processing to complete (24-48 hours for some metrics)
4. Use appropriate time zone settings

#### Issue: Bulk Upload Failures

**Symptoms:**
- Bulk file upload fails
- Partial entity creation

**Causes:**
- Invalid CSV format
- Missing required fields
- Data validation errors

**Solutions:**
1. Validate CSV format before upload
2. Check all required fields are present
3. Review error file from upload response
4. Test with small batch first

```python
# Download and review error file
result_file_path = bulk_service_manager.upload_file(
    upload_parameters=upload_parameters,
    file_path='upload.csv',
    result_file_directory='results',
    result_file_name='upload_results.csv'
)

# Parse results for errors
import pandas as pd
results = pd.read_csv(result_file_path)
errors = results[results['Status'] == 'Error']

if not errors.empty:
    logger.error(f"Upload errors:\n{errors[['Type', 'Status', 'Error']]}")
```

## Performance Optimization

### Batch Operations

```python
# Instead of individual API calls
for keyword in keywords:
    campaign_service.AddKeywords(
        AdGroupId=ad_group_id,
        Keywords=[keyword]
    )  # Multiple API calls

# Use batch operation
campaign_service.AddKeywords(
    AdGroupId=ad_group_id,
    Keywords=keywords  # Single API call
)
```

### Caching

```python
from functools import lru_cache
from datetime import datetime, timedelta

class CachedBingAdsClient:
    def __init__(self, campaign_service):
        self.campaign_service = campaign_service
        self.cache = {}
        self.cache_ttl = timedelta(minutes=15)
    
    def get_campaigns(self, account_id, force_refresh=False):
        cache_key = f"campaigns_{account_id}"
        
        if not force_refresh and cache_key in self.cache:
            cached_data, cached_time = self.cache[cache_key]
            if datetime.now() - cached_time < self.cache_ttl:
                logger.info("Returning cached campaigns")
                return cached_data
        
        # Fetch from API
        campaigns = self.campaign_service.GetCampaignsByAccountId(
            AccountId=account_id
        )
        
        # Cache result
        self.cache[cache_key] = (campaigns, datetime.now())
        
        return campaigns
```

### Parallel Processing

```python
from concurrent.futures import ThreadPoolExecutor, as_completed

def process_account(account_id):
    """Process single account."""
    # Your processing logic
    return result

def process_multiple_accounts(account_ids, max_workers=5):
    """Process multiple accounts in parallel."""
    results = {}
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_account = {
            executor.submit(process_account, account_id): account_id
            for account_id in account_ids
        }
        
        for future in as_completed(future_to_account):
            account_id = future_to_account[future]
            try:
                result = future.result()
                results[account_id] = result
                logger.info(f"Processed account {account_id}")
            except Exception as e:
                logger.error(f"Error processing account {account_id}: {e}")
                results[account_id] = None
    
    return results
```

## Security Best Practices

### Credential Security

1. **Never hardcode credentials**
2. **Use environment variables or secret management services**
3. **Rotate credentials regularly**
4. **Implement least privilege access**
5. **Audit credential usage**

### Data Security

1. **Encrypt sensitive data at rest**
2. **Use HTTPS for all communications**
3. **Sanitize log output (no credentials or PII)**
4. **Implement data retention policies**
5. **Regular security audits**

### Access Control

1. **Implement role-based access control**
2. **Monitor API usage**
3. **Set up alerts for unusual activity**
4. **Regular access reviews**

## Conclusion

Successful Microsoft Ads API integration requires attention to code organization, error handling, rate limiting, logging, testing, and security. By following these best practices and understanding common issues and their solutions, developers can build robust, reliable, and maintainable API integrations. Regular monitoring, comprehensive error handling, and proactive troubleshooting ensure long-term success and minimize disruptions to automated advertising workflows.
