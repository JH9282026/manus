---
name: web-application-security
description: "Secure web applications against OWASP Top 10 vulnerabilities and common attacks. Use for: preventing SQL injection, XSS, CSRF, implementing input validation, securing APIs, handling file uploads safely, preventing authentication bypass, protecting against DDoS, implementing security headers, conducting security audits, and following secure coding practices."
---

# Web Application Security

Protect web applications from OWASP Top 10 vulnerabilities and common security threats.

## Overview

This skill covers comprehensive web application security practices based on OWASP Top 10:2025. Learn to identify, prevent, and mitigate critical security vulnerabilities including injection attacks, broken authentication, security misconfigurations, and more.

## OWASP Top 10:2025

### A01: Broken Access Control

**Risk**: Users can access unauthorized resources or perform unauthorized actions.

**Examples:**
- Accessing other users' data by changing URL parameter
- Viewing/modifying data without proper authorization
- Privilege escalation (user acting as admin)

**Prevention:**
- Deny by default
- Implement server-side access control checks
- Validate user permissions for every request
- Log access control failures
- Invalidate sessions on logout

### A02: Security Misconfiguration

**Risk**: Insecure default configurations, incomplete setups, open cloud storage.

**Examples:**
- Default credentials still active
- Unnecessary features enabled
- Detailed error messages exposing system info
- Missing security headers

**Prevention:**
- Remove default accounts and passwords
- Disable unnecessary features and services
- Implement security headers (CSP, HSTS, X-Frame-Options)
- Keep software updated
- Use automated security scanning

### A03: Software Supply Chain Failures

**Risk**: Compromised dependencies, insecure CI/CD pipelines.

**Examples:**
- Using vulnerable npm packages
- Unsigned software updates
- Compromised build systems

**Prevention:**
- Maintain Software Bill of Materials (SBOM)
- Use only trusted package sources
- Verify package signatures
- Implement dependency scanning
- Secure CI/CD pipelines

### A04: Cryptographic Failures

**Risk**: Weak encryption, exposed sensitive data.

**Examples:**
- Storing passwords in plain text
- Using weak hashing (MD5, SHA-1)
- Transmitting data without TLS
- Hardcoded encryption keys

**Prevention:**
- Use strong algorithms (AES-256, bcrypt, Argon2)
- Always use TLS 1.2+ for data in transit
- Never hardcode secrets
- Use proper key management
- Encrypt sensitive data at rest

### A05: Injection

**Risk**: Untrusted data sent to interpreter as command/query.

**Types:**
- SQL Injection
- NoSQL Injection
- OS Command Injection
- LDAP Injection
- XSS (Cross-Site Scripting)

**Prevention:**
- Use parameterized queries/prepared statements
- Validate and sanitize all input
- Use ORM frameworks properly
- Implement input validation on server side
- Escape output data

### A06: Insecure Design

**Risk**: Fundamental design flaws, missing security controls.

**Examples:**
- No rate limiting on password reset
- Weak security questions
- Missing abuse case scenarios

**Prevention:**
- Conduct threat modeling
- Implement security user stories
- Use secure design patterns
- Perform security reviews during design
- Implement rate limiting

### A07: Authentication Problems

**Risk**: Weak authentication mechanisms.

**Examples:**
- No brute-force protection
- Weak password policies
- Session IDs in URLs
- Missing MFA

**Prevention:**
- Implement MFA
- Use strong password policies
- Add rate limiting on login
- Secure session management
- Implement account lockout

### A08: Software/Data Integrity Failures

**Risk**: Code/data trusted without verification.

**Examples:**
- Auto-updates without signature verification
- Insecure deserialization
- Unsigned CI/CD artifacts

**Prevention:**
- Verify digital signatures
- Use integrity checks (checksums)
- Secure CI/CD pipelines
- Never deserialize untrusted data
- Use dependency lockfiles

### A09: Security Logging/Monitoring Failures

**Risk**: Insufficient logging prevents breach detection.

**Examples:**
- Not logging authentication failures
- Missing audit trails
- No alerting on suspicious activity

**Prevention:**
- Log all authentication events
- Log access control failures
- Centralize logs (SIEM)
- Implement real-time alerting
- Protect log integrity

### A10: Mishandling Exceptional Conditions

**Risk**: Errors expose sensitive information or leave system insecure.

**Examples:**
- Stack traces in production
- Detailed error messages to users

**Prevention:**
- Generic error messages in production
- Log detailed errors internally
- Proper exception handling
- Fail securely

## Common Attack Vectors

### SQL Injection

**Vulnerable Code:**
```python
query = f"SELECT * FROM users WHERE username = '{username}'"
```

**Secure Code:**
```python
query = "SELECT * FROM users WHERE username = %s"
cursor.execute(query, (username,))
```

### Cross-Site Scripting (XSS)

**Types:**
- Stored XSS: Malicious script stored in database
- Reflected XSS: Script in URL parameter
- DOM-based XSS: Client-side script manipulation

**Prevention:**
- Escape all output
- Use Content Security Policy (CSP)
- Validate and sanitize input
- Use frameworks with auto-escaping

### Cross-Site Request Forgery (CSRF)

**Attack**: Trick user into executing unwanted actions.

**Prevention:**
- Use CSRF tokens
- SameSite cookie attribute
- Verify Origin/Referer headers
- Require re-authentication for sensitive actions

### XML External Entity (XXE)

**Attack**: Exploit XML parsers to access files or execute code.

**Prevention:**
- Disable external entity processing
- Use less complex data formats (JSON)
- Validate XML input
- Keep XML processors updated

## Security Headers

### Content Security Policy (CSP)
```
Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'
```

### HTTP Strict Transport Security (HSTS)
```
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
```

### X-Frame-Options
```
X-Frame-Options: DENY
```

### X-Content-Type-Options
```
X-Content-Type-Options: nosniff
```

### X-XSS-Protection
```
X-XSS-Protection: 1; mode=block
```

## Input Validation

### Validation Rules

- Validate on server side (never trust client)
- Whitelist allowed characters
- Validate data type, length, format
- Reject unexpected input
- Sanitize before processing

### File Upload Security

- Validate file type (check magic bytes, not just extension)
- Limit file size
- Store uploads outside web root
- Generate random filenames
- Scan for malware
- Serve with correct Content-Type

## Secure Coding Practices

- Principle of least privilege
- Defense in depth
- Fail securely
- Keep security simple
- Don't rely on security through obscurity
- Separate data from code
- Use secure defaults
- Minimize attack surface

## Security Testing

### Tools

- **SAST**: Static Application Security Testing (SonarQube, Checkmarx)
- **DAST**: Dynamic Application Security Testing (OWASP ZAP, Burp Suite)
- **SCA**: Software Composition Analysis (Snyk, Dependabot)
- **Penetration Testing**: Manual security testing

### Security Checklist

- [ ] Input validation on all user input
- [ ] Output encoding to prevent XSS
- [ ] Parameterized queries to prevent SQL injection
- [ ] CSRF protection on state-changing operations
- [ ] Secure session management
- [ ] Strong authentication mechanisms
- [ ] Proper authorization checks
- [ ] Security headers implemented
- [ ] HTTPS enforced
- [ ] Secrets not hardcoded
- [ ] Dependencies up to date
- [ ] Security logging enabled
- [ ] Error handling doesn't leak info
- [ ] File uploads secured
- [ ] Rate limiting implemented

## Using the Reference Files

**`/references/owasp-top10-details.md`** — Read for detailed explanations of each OWASP Top 10 vulnerability with code examples and mitigation strategies.

**`/references/injection-prevention.md`** — Read when implementing protection against SQL injection, XSS, command injection, and other injection attacks.

**`/references/security-testing.md`** — Read when setting up security testing, using SAST/DAST tools, or conducting penetration testing.

**`/references/secure-coding-guide.md`** — Read for comprehensive secure coding practices, code review checklists, and security patterns.
