# Microsoft Ads API Authentication and Setup Guide

## Introduction

Authentication is the foundational step for integrating with the Microsoft Advertising API (also known as Bing Ads API). This guide provides comprehensive coverage of the authentication process, application registration, OAuth 2.0 implementation, and credential management required to successfully connect to and interact with Microsoft Advertising services.

## Overview of Microsoft Ads API Authentication

### Authentication Requirements

To access the Microsoft Advertising API, you need three key credentials:

1. **Developer Token**: Identifies your application to Microsoft Advertising
2. **OAuth Credentials**: Client ID and Client Secret from Azure Active Directory (now Microsoft Entra ID)
3. **Access and Refresh Tokens**: Obtained through OAuth 2.0 flow for API authorization

### Authentication Flow Summary

```
1. Register Application in Azure/Entra ID
   ↓
2. Obtain Client ID and Client Secret
   ↓
3. Get Developer Token from Microsoft Advertising
   ↓
4. Implement OAuth 2.0 Authorization Flow
   ↓
5. Request User Consent
   ↓
6. Exchange Authorization Code for Tokens
   ↓
7. Use Access Token for API Calls
   ↓
8. Refresh Access Token When Expired
```

## Step 1: Application Registration

### Registering with Microsoft Entra ID (Azure Active Directory)

Microsoft Advertising uses Microsoft's identity platform for authentication. You must register your application to obtain OAuth credentials.

#### Prerequisites

- **Microsoft Account**: Work or School Account (personal Microsoft accounts are no longer supported for app registration)
- **Azure Portal Access**: Access to Azure Active Directory/Entra ID
- **Permissions**: Ability to register applications in your organization's directory

#### Registration Process

**1. Navigate to Azure Portal:**
- Go to [Azure Portal](https://portal.azure.com)
- Sign in with your Work or School Account
- Navigate to "Azure Active Directory" or "Microsoft Entra ID"
- Select "App registrations"

**2. Create New Registration:**
- Click "New registration"
- Provide application details:
  - **Name**: Meaningful application name (e.g., "My Bing Ads Integration")
  - **Supported account types**: Select "Accounts in any organizational directory and personal Microsoft accounts"
  - **Redirect URI**: 
    - For web applications: Your application's callback URL (e.g., `http://localhost:31544` for local development)
    - For public/native applications: `https://login.microsoftonline.com/common/oauth2/nativeclient`

**3. Note Application (Client) ID:**
- After registration, you'll see the application's Overview page
- Copy the **Application (client) ID** — this is your `client_id`
- Save this value securely

**4. Create Client Secret:**
- In your app's page, navigate to "Certificates & secrets"
- Click "New client secret"
- Provide a description (e.g., "Production Secret")
- Select expiration period:
  - 6 months
  - 12 months
  - 24 months
  - Custom
- Click "Add"
- **IMPORTANT**: Copy the secret **Value** immediately — it's only shown once
- This is your `client_secret`
- Store securely (use environment variables or secret management service)

**5. Configure Redirect URIs:**
- Navigate to "Authentication" in your app settings
- Add or modify redirect URIs as needed
- For web apps: Add your production callback URL
- For development: Add localhost URLs
- Save changes

**6. API Permissions (Optional but Recommended):**
- Navigate to "API permissions"
- Click "Add a permission"
- Select "APIs my organization uses"
- Search for "Microsoft Advertising" (Application ID: `d42ffc93-c136-491d-b4fd-6f18168c68fd`)
- Select appropriate permissions
- Grant admin consent if required by your organization

### Handling Common Registration Issues

#### AADSTS650052 Error

**Problem**: Microsoft Advertising application ID is missing from your tenant

**Solution**:
- Contact your Azure AD administrator
- Administrator must add Microsoft Advertising service principal to tenant
- Use Microsoft Graph API to add the application:

```http
POST https://graph.microsoft.com/v1.0/servicePrincipals
Content-Type: application/json

{
  "appId": "d42ffc93-c136-491d-b4fd-6f18168c68fd"
}
```

#### Personal Account Limitations

**Problem**: Personal Microsoft accounts can't register apps in Azure AD

**Solution**:
- Use a Work or School Account
- Create an Azure AD tenant if you don't have one
- Register application within that tenant

### Alternative: Google OAuth Registration

If authenticating users via Google OAuth 2.0 (less common for Microsoft Ads):

**1. Google Cloud Console:**
- Navigate to [Google Cloud Console](https://console.cloud.google.com)
- Create or select a project
- Go to "APIs & Services" > "Credentials"

**2. Create OAuth Client:**
- Click "Create Credentials" > "OAuth client ID"
- Select application type (Web application, Desktop app, etc.)
- Configure authorized redirect URIs
- Copy Client ID and Client Secret

## Step 2: Obtaining Developer Token

### What is a Developer Token?

The developer token is a unique identifier for your application that Microsoft Advertising uses to track API usage and enforce rate limits.

### How to Get Developer Token

**1. Sign in to Microsoft Advertising:**
- Go to [Microsoft Advertising Developer Portal](https://developers.ads.microsoft.com)
- Sign in with Super Admin credentials
- Navigate to "Account" tab

**2. Request Token:**
- Select the user to associate with the developer token
- Click "Request Token"
- Token will be generated and displayed
- Copy and save the token securely

**3. Token Types:**

*Universal Token (Default since July 2019):*
- Single token works for all users
- Recommended for most applications
- Simplifies token management
- No need for separate tokens per user

*User-Specific Token (Legacy):*
- Separate token per user
- Rarely needed for new applications
- More complex management

### Sandbox Developer Token

For testing and development:

**Sandbox Token**: `BBD37VB98`

- Use this token for sandbox environment testing
- No approval required
- Limited to sandbox accounts
- Switch to production token for live campaigns

### Developer Portal Update (2025)

**Important**: A new Developer Portal page will replace the current one starting **May 31, 2025**. Ensure you:
- Familiarize yourself with the new interface
- Update any documentation or processes
- Verify token access in the new portal

## Step 3: OAuth 2.0 Authorization Flow

### OAuth 2.0 Overview

Microsoft Advertising API uses OAuth 2.0 for secure authorization. This allows your application to access user data without handling passwords.

### Authorization Flow Steps

#### Step 3.1: Request User Consent

**Authorization URL Structure:**

```
https://login.microsoftonline.com/common/oauth2/v2.0/authorize?
  client_id={YOUR_CLIENT_ID}
  &response_type=code
  &redirect_uri={YOUR_REDIRECT_URI}
  &scope=offline_access%20https://ads.microsoft.com/msads.manage
  &state={RANDOM_STATE_STRING}
```

**Parameters:**

- **client_id**: Your Application (client) ID from Azure AD
- **response_type**: Always `code` for authorization code flow
- **redirect_uri**: Must match one registered in Azure AD (URL-encoded)
- **scope**: 
  - `offline_access`: Enables refresh token
  - `https://ads.microsoft.com/msads.manage`: Permission to manage Microsoft Ads
- **state**: Random string to prevent CSRF attacks (verify on callback)

**For Active Directory Tenants:**

Replace `common` with your Tenant ID or domain:

```
https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/authorize?...
```

**User Experience:**

1. User is redirected to Microsoft login page
2. User signs in with Microsoft Advertising credentials
3. User sees consent screen requesting permissions
4. User grants or denies access
5. User is redirected back to your `redirect_uri`

#### Step 3.2: Handle Authorization Response

**Success Response:**

User is redirected to:

```
https://your-redirect-uri.com/callback?
  code={AUTHORIZATION_CODE}
  &state={STATE_VALUE}
```

**Your Application Should:**

1. Verify `state` parameter matches what you sent
2. Extract the `code` parameter
3. **Important**: Authorization code expires in ~5 minutes
4. Immediately exchange code for tokens

**Error Response:**

```
https://your-redirect-uri.com/callback?
  error={ERROR_CODE}
  &error_description={DESCRIPTION}
  &state={STATE_VALUE}
```

Common errors:
- `access_denied`: User denied consent
- `invalid_request`: Malformed request
- `unauthorized_client`: Client not authorized

#### Step 3.3: Exchange Authorization Code for Tokens

**Token Request:**

```http
POST https://login.microsoftonline.com/common/oauth2/v2.0/token
Content-Type: application/x-www-form-urlencoded

client_id={YOUR_CLIENT_ID}
&client_secret={YOUR_CLIENT_SECRET}
&code={AUTHORIZATION_CODE}
&redirect_uri={YOUR_REDIRECT_URI}
&grant_type=authorization_code
```

**Parameters:**

- **client_id**: Your Application (client) ID
- **client_secret**: Your client secret from Azure AD
- **code**: Authorization code from previous step
- **redirect_uri**: Same URI used in authorization request
- **grant_type**: Always `authorization_code`

**Success Response:**

```json
{
  "token_type": "Bearer",
  "expires_in": 3600,
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh_token": "M.R3_BAY.CdG3l...",
  "scope": "https://ads.microsoft.com/msads.manage"
}
```

**Token Details:**

- **access_token**: Use for API calls (valid for ~1 hour)
- **refresh_token**: Use to get new access tokens (valid for up to 90 days)
- **expires_in**: Access token lifetime in seconds (typically 3600)
- **token_type**: Always "Bearer"

**Error Response:**

```json
{
  "error": "invalid_grant",
  "error_description": "The provided authorization code is invalid or expired"
}
```

### Token Refresh Flow

Access tokens expire after ~1 hour. Use refresh token to obtain new access token without user interaction.

**Refresh Request:**

```http
POST https://login.microsoftonline.com/common/oauth2/v2.0/token
Content-Type: application/x-www-form-urlencoded

client_id={YOUR_CLIENT_ID}
&client_secret={YOUR_CLIENT_SECRET}
&refresh_token={REFRESH_TOKEN}
&grant_type=refresh_token
```

**Parameters:**

- **client_id**: Your Application (client) ID
- **client_secret**: Your client secret
- **refresh_token**: Current refresh token
- **grant_type**: Always `refresh_token`

**Success Response:**

```json
{
  "token_type": "Bearer",
  "expires_in": 3600,
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh_token": "M.R3_BAY.NewRefreshToken..."
}
```

**Important**: 
- Response includes a **new refresh token**
- Always save the latest refresh token
- Old refresh token may become invalid
- Refresh tokens expire after 90 days of inactivity

### Token Storage Best Practices

**Security Considerations:**

1. **Never store tokens in:**
   - Client-side code (JavaScript)
   - Version control (Git)
   - Plain text files
   - Logs or error messages

2. **Recommended storage:**
   - Encrypted database
   - Secure key management service (Azure Key Vault, AWS Secrets Manager)
   - Environment variables (for development only)
   - Server-side session storage

3. **Token handling:**
   - Encrypt tokens at rest
   - Use HTTPS for all token transmission
   - Implement token rotation
   - Set appropriate token expiration
   - Log token usage (not token values)

## Step 4: Making Authenticated API Calls

### Using Access Token

**HTTP Header:**

```http
GET https://api.bingads.microsoft.com/Api/Advertiser/CampaignManagement/v13/Campaigns
Authorization: Bearer {ACCESS_TOKEN}
DeveloperToken: {YOUR_DEVELOPER_TOKEN}
CustomerId: {CUSTOMER_ID}
AccountId: {ACCOUNT_ID}
```

**Required Headers:**

- **Authorization**: Bearer token with access token
- **DeveloperToken**: Your developer token
- **CustomerId**: Microsoft Advertising customer ID
- **AccountId**: Microsoft Advertising account ID (optional for some operations)

### Finding Customer and Account IDs

**Method 1: From Microsoft Advertising Web UI**

- Sign in to [Microsoft Advertising](https://ads.microsoft.com)
- Look at the URL: `https://ui.ads.microsoft.com/campaign/...?cid={CUSTOMER_ID}&aid={ACCOUNT_ID}`
- **cid**: Customer ID
- **aid**: Account ID

**Method 2: Programmatically via API**

```python
# Step 1: Get User Information
user = customer_service.GetUser()
user_id = user.Id

# Step 2: Search for Accounts
accounts = customer_service.SearchAccounts(
    Predicates=None,
    Ordering=None,
    PageInfo=None
)

# Extract Customer ID and Account ID
for account in accounts['AdvertiserAccount']:
    customer_id = account.ParentCustomerId
    account_id = account.Id
    print(f"Customer ID: {customer_id}, Account ID: {account_id}")
```

### Using Microsoft Advertising SDKs

SDKs simplify authentication by abstracting OAuth details.

**Python SDK Example:**

```python
from bingads import AuthorizationData, OAuthWebAuthCodeGrant
from bingads.service_client import ServiceClient

# OAuth credentials
oauth = OAuthWebAuthCodeGrant(
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
    redirection_uri='YOUR_REDIRECT_URI'
)

# Load refresh token if available
try:
    oauth.refresh_token = load_refresh_token()  # Your function
except:
    # First time: get authorization URL
    authorization_url = oauth.get_authorization_endpoint()
    print(f"Visit: {authorization_url}")
    
    # User visits URL and authorizes
    # You receive authorization code
    code = input("Enter authorization code: ")
    
    # Exchange code for tokens
    oauth.request_oauth_tokens_by_authorization_code(code)
    
    # Save refresh token
    save_refresh_token(oauth.refresh_token)  # Your function

# Create authorization data
authorization_data = AuthorizationData(
    account_id='YOUR_ACCOUNT_ID',
    customer_id='YOUR_CUSTOMER_ID',
    developer_token='YOUR_DEVELOPER_TOKEN',
    authentication=oauth
)

# Create service client
campaign_service = ServiceClient(
    service='CampaignManagementService',
    version=13,
    authorization_data=authorization_data
)

# Make API calls
campaigns = campaign_service.GetCampaignsByAccountId(
    AccountId=authorization_data.account_id
)
```

## Multi-Factor Authentication (MFA)

### MFA Requirement

**Effective Date**: June 2022

**Requirement**: Multi-factor authentication is **mandatory** for all Bing Ads API access.

**Technical Enforcement**: Began in early October 2022.

### Implementation Considerations

**For Users:**
- Enable MFA on Microsoft Advertising account
- Use authenticator app or SMS verification
- Complete MFA during OAuth login flow

**For Developers:**
- No code changes required for standard OAuth flow
- MFA is handled during user consent step
- Ensure your application handles longer authentication times
- Test authentication flow with MFA-enabled accounts

**Potential Issues:**
- Automated scripts may need user interaction for MFA
- Service accounts should have MFA configured
- Consider using service principals for fully automated scenarios

## Environment Configuration

### Sandbox vs. Production

**Sandbox Environment:**

- **Purpose**: Testing and development
- **Developer Token**: `BBD37VB98`
- **Endpoint**: Sandbox-specific endpoints
- **Data**: Test data only, no real campaigns
- **No charges**: Safe for experimentation

**Production Environment:**

- **Purpose**: Live campaigns and real data
- **Developer Token**: Your approved production token
- **Endpoint**: Production API endpoints
- **Data**: Real campaigns and billing
- **Charges apply**: Real budget and costs

**SDK Configuration:**

```python
from bingads import ServiceClient, AuthorizationData
from bingads.v13.bulk import BulkServiceManager

# Sandbox
authorization_data.environment = 'sandbox'

# Production (default)
authorization_data.environment = 'production'
```

### Rate Limiting and Quotas

**API Rate Limits:**

- Vary by service and operation
- Typically measured in requests per minute/hour
- Exceeded limits result in HTTP 429 errors

**Best Practices:**

1. Implement exponential backoff for retries
2. Cache responses when appropriate
3. Batch operations when possible
4. Monitor rate limit headers in responses
5. Distribute requests over time

**Handling Rate Limits:**

```python
import time
from requests.exceptions import HTTPError

def api_call_with_retry(func, max_retries=3):
    for attempt in range(max_retries):
        try:
            return func()
        except HTTPError as e:
            if e.response.status_code == 429:
                wait_time = 2 ** attempt  # Exponential backoff
                print(f"Rate limited. Waiting {wait_time}s...")
                time.sleep(wait_time)
            else:
                raise
    raise Exception("Max retries exceeded")
```

## Error Handling and Troubleshooting

### Common Authentication Errors

**1. Invalid Client Credentials**

```json
{
  "error": "invalid_client",
  "error_description": "Client authentication failed"
}
```

**Causes:**
- Incorrect client_id or client_secret
- Client secret expired
- Application not properly registered

**Solutions:**
- Verify credentials in Azure AD
- Generate new client secret if expired
- Check application registration status

**2. Invalid Grant**

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
- Request new authorization code
- Exchange code immediately after receiving
- Re-authenticate user if refresh token invalid

**3. Unauthorized Client**

```json
{
  "error": "unauthorized_client",
  "error_description": "The client is not authorized to request an authorization code"
}
```

**Causes:**
- Redirect URI mismatch
- Application not approved for requested scope
- Incorrect tenant configuration

**Solutions:**
- Verify redirect URI matches registration exactly
- Check application permissions in Azure AD
- Ensure correct tenant ID in authorization URL

### Debugging Tips

**1. Enable Detailed Logging:**

```python
import logging

logging.basicConfig(level=logging.DEBUG)
```

**2. Inspect Token Contents:**

Access tokens are JWTs. Decode (don't verify signature) to inspect:

```python
import base64
import json

def decode_jwt(token):
    parts = token.split('.')
    payload = parts[1]
    # Add padding if needed
    payload += '=' * (4 - len(payload) % 4)
    decoded = base64.urlsafe_b64decode(payload)
    return json.loads(decoded)

token_data = decode_jwt(access_token)
print(json.dumps(token_data, indent=2))
```

**3. Test with Postman or cURL:**

```bash
curl -X POST https://login.microsoftonline.com/common/oauth2/v2.0/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "client_id=YOUR_CLIENT_ID" \
  -d "client_secret=YOUR_CLIENT_SECRET" \
  -d "code=AUTHORIZATION_CODE" \
  -d "redirect_uri=YOUR_REDIRECT_URI" \
  -d "grant_type=authorization_code"
```

## Security Best Practices

### Credential Management

1. **Use Environment Variables:**

```python
import os

client_id = os.environ.get('BING_ADS_CLIENT_ID')
client_secret = os.environ.get('BING_ADS_CLIENT_SECRET')
developer_token = os.environ.get('BING_ADS_DEVELOPER_TOKEN')
```

2. **Use Secret Management Services:**

- Azure Key Vault
- AWS Secrets Manager
- HashiCorp Vault
- Google Secret Manager

3. **Rotate Credentials Regularly:**

- Generate new client secrets before expiration
- Update applications with new credentials
- Revoke old credentials after migration

### Network Security

1. **Always Use HTTPS:**
   - All OAuth and API calls must use HTTPS
   - Never send credentials over HTTP

2. **Validate SSL Certificates:**
   - Don't disable SSL verification
   - Use trusted certificate authorities

3. **Implement IP Whitelisting:**
   - Restrict API access to known IP addresses
   - Use firewall rules

### Application Security

1. **Validate State Parameter:**
   - Prevent CSRF attacks
   - Generate random state for each authorization request
   - Verify state matches on callback

2. **Implement Token Expiration Handling:**
   - Check token expiration before API calls
   - Automatically refresh when needed
   - Handle refresh failures gracefully

3. **Audit and Monitoring:**
   - Log authentication events
   - Monitor for unusual activity
   - Set up alerts for failed authentications
   - Regular security audits

## Conclusion

Successful Microsoft Ads API authentication requires careful setup of Azure AD application registration, obtaining a developer token, and implementing OAuth 2.0 authorization flow. By following this guide, you can securely authenticate your application, manage tokens effectively, and maintain robust security practices. Proper error handling, token refresh management, and adherence to security best practices ensure reliable and secure API integration. With authentication properly configured, you're ready to leverage the full power of the Microsoft Advertising API for campaign management, reporting, and optimization.
