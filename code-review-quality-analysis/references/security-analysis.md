# Security Analysis

## OWASP Top 10 Checks

| Vulnerability | Detection Method | Remediation |
|---------------|------------------|-------------|
| A01 Broken Access Control | Auth flow review, IDOR checks | Implement proper authorization |
| A02 Cryptographic Failures | Crypto implementation review | Use standard libraries |
| A03 Injection | Input validation review | Parameterized queries, sanitization |
| A04 Insecure Design | Architecture review | Threat modeling |
| A05 Security Misconfiguration | Config review | Secure defaults |
| A06 Vulnerable Components | Dependency scanning | Update dependencies |
| A07 Auth Failures | Session management review | MFA, secure session handling |
| A08 Software Integrity | Build pipeline review | Code signing, SBOM |
| A09 Logging Failures | Logging review | Comprehensive audit logging |
| A10 SSRF | Request handling review | URL validation, allowlists |

---

## Common Vulnerability Patterns

### Injection Vulnerabilities

**SQL Injection**
```python
# Vulnerable
query = f"SELECT * FROM users WHERE id = {user_id}"

# Secure
cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
```

**XSS (Cross-Site Scripting)**
```javascript
// Vulnerable
element.innerHTML = userInput;

// Secure
element.textContent = userInput;
```

### Authentication Issues
- Weak password requirements
- Missing brute force protection
- Insecure session management
- Missing MFA for sensitive operations
- Credential exposure in logs

### Data Exposure
- Sensitive data in URLs
- Unencrypted storage
- Excessive data in responses
- Missing data masking
- Insecure data transmission

---

## Dependency Scanning

### Vulnerability Databases
- CVE (Common Vulnerabilities and Exposures)
- NVD (National Vulnerability Database)
- GitHub Security Advisories
- Snyk Vulnerability DB

### Scanning Tools

| Language | Tool | Usage |
|----------|------|-------|
| Python | safety, pip-audit | pip-audit check |
| JavaScript | npm audit | npm audit |
| Java | OWASP Dependency-Check | mvn dependency-check |
| Go | govulncheck | govulncheck ./... |

---

## Security Review Checklist

### Authentication
- [ ] Password strength requirements
- [ ] Secure password storage (bcrypt, argon2)
- [ ] Session timeout configuration
- [ ] MFA implementation
- [ ] Account lockout after failed attempts

### Authorization
- [ ] Role-based access control
- [ ] Resource-level permissions
- [ ] Principle of least privilege
- [ ] Authorization on all endpoints

### Data Protection
- [ ] Encryption at rest
- [ ] Encryption in transit (TLS)
- [ ] Sensitive data handling
- [ ] PII protection
- [ ] Secure key management

### Input Validation
- [ ] All inputs validated
- [ ] Whitelist validation where possible
- [ ] Output encoding
- [ ] File upload restrictions
