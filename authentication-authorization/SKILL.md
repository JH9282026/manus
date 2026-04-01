---
name: authentication-authorization
description: "Implement secure authentication and authorization systems using OAuth 2.0, JWT, and RBAC. Use for: user authentication flows, OAuth 2.0 implementation, JWT token management, role-based access control (RBAC), attribute-based access control (ABAC), session management, multi-factor authentication (MFA), single sign-on (SSO), API authentication, and securing user access to resources."
---

# Authentication & Authorization

Implement secure authentication and authorization systems for web applications and APIs.

## Overview

This skill covers modern authentication and authorization patterns including OAuth 2.0, JWT, RBAC, and ABAC. Learn to implement secure login flows, manage user sessions, protect API endpoints, and control access to resources based on user roles and attributes.

## Authentication vs. Authorization

**Authentication**: Verifying WHO the user is
- Login with username/password
- OAuth social login
- Multi-factor authentication
- Biometric verification

**Authorization**: Determining WHAT the user can do
- Role-based access control (RBAC)
- Attribute-based access control (ABAC)
- Permission checks
- Resource ownership verification

## Authentication Methods

| Method | Use Case | Security Level | Complexity |
|--------|----------|----------------|------------|
| Username/Password | Traditional apps | Medium | Low |
| OAuth 2.0 | Third-party login, API access | High | Medium |
| JWT | Stateless API auth | High | Medium |
| Session Cookies | Web applications | Medium-High | Low |
| API Keys | Service-to-service | Medium | Low |
| Multi-Factor (MFA) | High-security apps | Very High | Medium |
| Biometric | Mobile apps | High | High |

## OAuth 2.0 Flows

### Authorization Code Flow (Most Secure)
**Use for**: Web applications, mobile apps

**Steps:**
1. User clicks "Login with Google"
2. Redirect to authorization server
3. User authenticates and grants permission
4. Authorization server redirects back with code
5. Exchange code for access token
6. Use access token to access resources

### Client Credentials Flow
**Use for**: Machine-to-machine, backend services

**Steps:**
1. Client sends client_id and client_secret
2. Authorization server returns access token
3. Client uses token to access API

### Implicit Flow (Deprecated)
**Use for**: Legacy SPAs (not recommended)
**Security Issue**: Token exposed in URL

### PKCE (Proof Key for Code Exchange)
**Use for**: Mobile apps, SPAs
**Benefit**: Prevents authorization code interception

## JWT (JSON Web Tokens)

### Token Structure
```
header.payload.signature
```

**Header:**
```json
{
  "alg": "RS256",
  "typ": "JWT"
}
```

**Payload:**
```json
{
  "sub": "user123",
  "name": "John Doe",
  "roles": ["user", "admin"],
  "exp": 1647349200,
  "iss": "https://auth.example.com"
}
```

### JWT Best Practices

- Use short expiration times (15-30 minutes)
- Implement refresh tokens for long sessions
- Store tokens securely (httpOnly cookies or secure storage)
- Validate signature, issuer, audience, expiration
- Use RS256 (asymmetric) for production
- Never store sensitive data in payload
- Implement token revocation mechanism

## Role-Based Access Control (RBAC)

### RBAC Model

**Roles:**
- Admin: Full system access
- Manager: Department-level access
- User: Basic access
- Guest: Read-only access

**Permissions:**
- users:read
- users:write
- users:delete
- posts:create
- posts:publish

**Role-Permission Mapping:**
```
Admin: users:*, posts:*
Manager: users:read, users:write, posts:*
User: users:read, posts:create
Guest: users:read, posts:read
```

### Implementation Pattern

**Database Schema:**
```sql
CREATE TABLE roles (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE permissions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE role_permissions (
    role_id INT REFERENCES roles(id),
    permission_id INT REFERENCES permissions(id),
    PRIMARY KEY (role_id, permission_id)
);

CREATE TABLE user_roles (
    user_id INT REFERENCES users(id),
    role_id INT REFERENCES roles(id),
    PRIMARY KEY (user_id, role_id)
);
```

## Attribute-Based Access Control (ABAC)

**Decision based on:**
- User attributes (department, clearance level)
- Resource attributes (classification, owner)
- Environment attributes (time, location, IP)
- Action attributes (read, write, delete)

**Example Policy:**
```
Allow if:
  user.department == resource.department AND
  user.clearance_level >= resource.classification AND
  action == "read" AND
  time.hour >= 9 AND time.hour <= 17
```

## Session Management

### Session Storage Options

**Server-Side Sessions:**
- Store in database or Redis
- Session ID in cookie
- Secure, can revoke anytime
- Requires server state

**Client-Side Sessions (JWT):**
- All data in token
- Stateless
- Can't revoke easily
- Scalable

### Session Security

- Use httpOnly cookies (prevent XSS)
- Use secure flag (HTTPS only)
- Use SameSite attribute (prevent CSRF)
- Implement session timeout
- Regenerate session ID after login
- Invalidate sessions on logout

## Multi-Factor Authentication (MFA)

### MFA Methods

1. **SMS/Email OTP**: One-time password sent to phone/email
2. **TOTP**: Time-based OTP (Google Authenticator, Authy)
3. **Push Notifications**: Approve login on mobile app
4. **Hardware Tokens**: YubiKey, security keys
5. **Biometric**: Fingerprint, face recognition

### Implementation Flow

1. User enters username/password
2. System validates credentials
3. System generates OTP or sends push notification
4. User enters OTP or approves notification
5. System validates second factor
6. Grant access

## Single Sign-On (SSO)

### SAML 2.0
**Use for**: Enterprise applications

**Flow:**
1. User accesses service provider (SP)
2. SP redirects to identity provider (IdP)
3. User authenticates with IdP
4. IdP sends SAML assertion to SP
5. SP grants access

### OpenID Connect (OIDC)
**Use for**: Modern web/mobile apps

**Built on OAuth 2.0, adds:**
- ID Token (JWT with user info)
- UserInfo endpoint
- Standardized scopes

## Password Security

### Hashing Algorithms

**Recommended:**
- bcrypt (adaptive, slow)
- Argon2 (modern, memory-hard)
- scrypt (memory-hard)

**NOT Recommended:**
- MD5 (broken)
- SHA-1 (broken)
- Plain SHA-256 (too fast)

### Password Policies

- Minimum 8 characters (12+ recommended)
- Require mix of uppercase, lowercase, numbers, symbols
- Check against common password lists
- Implement password strength meter
- Enforce password expiration (90 days)
- Prevent password reuse (last 5 passwords)

## API Authentication

### Bearer Tokens
```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

### API Keys
```
X-API-Key: sk_live_abc123def456
```

### Basic Auth (Not Recommended for Production)
```
Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=
```

## Security Best Practices

- Always use HTTPS/TLS
- Implement rate limiting on auth endpoints
- Log all authentication events
- Monitor for suspicious activity
- Implement account lockout after failed attempts
- Use CAPTCHA to prevent brute force
- Validate redirect URLs (prevent open redirect)
- Implement CSRF protection
- Use secure random number generators
- Never log passwords or tokens

## Using the Reference Files

**`/references/oauth-implementation.md`** — Read when implementing OAuth 2.0 flows, integrating third-party login providers, or building authorization servers.

**`/references/jwt-patterns.md`** — Read when implementing JWT authentication, managing token lifecycle, or handling refresh tokens.

**`/references/rbac-abac-systems.md`** — Read when designing role-based or attribute-based access control systems, managing permissions, or implementing fine-grained authorization.

**`/references/session-security.md`** — Read when implementing session management, securing cookies, or handling user sessions across distributed systems.

## References

- [Jwt Patterns](references/jwt-patterns.md)
- [Oauth Implementation](references/oauth-implementation.md)
- [Rbac Abac Systems](references/rbac-abac-systems.md)
- [Session Security](references/session-security.md)
