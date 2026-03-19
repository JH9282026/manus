# Security Testing Fundamentals

Comprehensive foundation for understanding security testing concepts, principles, and frameworks.

---

## What is Security Testing?

Security testing is a systematic process of evaluating systems, applications, and networks to identify vulnerabilities, weaknesses, and potential security risks before malicious actors can exploit them. It encompasses various methodologies ranging from automated vulnerability scanning to manual penetration testing and code review.

### Core Objectives

1. **Identify vulnerabilities** — Discover security weaknesses in systems and applications
2. **Assess exploitability** — Determine if vulnerabilities can be exploited in real-world scenarios
3. **Evaluate business impact** — Understand potential damage from successful attacks
4. **Validate security controls** — Verify effectiveness of existing security measures
5. **Ensure compliance** — Meet regulatory and industry security requirements
6. **Improve security posture** — Provide actionable recommendations for enhancement

### Security Testing vs. Related Disciplines

**Security Testing vs. Vulnerability Assessment:**
- **Vulnerability Assessment:** Automated scanning to identify known vulnerabilities, produces comprehensive lists with potential false positives, focuses on breadth
- **Security Testing:** Includes manual validation, exploitation attempts, and business impact analysis, focuses on depth and real-world exploitability

**Security Testing vs. Penetration Testing:**
- **Security Testing:** Broader term encompassing all security evaluation activities
- **Penetration Testing:** Specific type of security testing that simulates real attacks to exploit vulnerabilities

**Security Testing vs. Quality Assurance (QA):**
- **QA Testing:** Verifies software meets functional requirements and works correctly
- **Security Testing:** Evaluates how software fails under attack and identifies security weaknesses

---

## Types of Security Testing

### 1. Vulnerability Assessment

**Purpose:** Identify and catalog known vulnerabilities in systems and applications

**Methodology:**
- Automated scanning using tools like Nessus, Qualys, Rapid7
- Cross-reference findings with CVE databases
- Generate prioritized vulnerability reports
- Minimal exploitation attempts

**Best for:** Regular security monitoring, compliance scanning, broad coverage

**Frequency:** Continuous or weekly/monthly

### 2. Penetration Testing

**Purpose:** Simulate real-world attacks to exploit vulnerabilities and demonstrate business impact

**Methodology:**
- Manual testing with automated tool support
- Active exploitation of discovered vulnerabilities
- Privilege escalation and lateral movement
- Proof of concept development

**Best for:** Deep security validation, pre-deployment testing, compliance requirements

**Frequency:** Annually, bi-annually, or after major changes

### 3. Security Auditing

**Purpose:** Systematic examination of security policies, procedures, and controls

**Methodology:**
- Review security documentation and policies
- Verify compliance with standards and regulations
- Assess security control implementation
- Interview personnel and review processes

**Best for:** Compliance validation, governance assessment, policy verification

**Frequency:** Annually or as required by regulations

### 4. Security Code Review

**Purpose:** Analyze source code to identify security vulnerabilities and coding flaws

**Methodology:**
- Manual code inspection by security experts
- Static Application Security Testing (SAST) tools
- Review for common vulnerabilities (injection, XSS, etc.)
- Assess adherence to secure coding standards

**Best for:** Pre-release security validation, critical application review

**Frequency:** During development, before major releases

### 5. Security Architecture Review

**Purpose:** Evaluate system design and architecture for security weaknesses

**Methodology:**
- Review system architecture diagrams
- Assess security design patterns
- Identify architectural vulnerabilities
- Evaluate defense-in-depth implementation

**Best for:** New system design, major architectural changes

**Frequency:** During design phase, before implementation

---

## OWASP Top 10 Vulnerabilities (2021) — Detailed

### 1. Broken Access Control

**Description:** Users can access resources or perform actions beyond their authorized permissions.

**Common manifestations:**
- Bypassing access control checks by modifying URLs or parameters
- Viewing or editing someone else's account data
- Accessing API endpoints without proper authorization
- Privilege escalation (acting as admin without being one)
- Insecure Direct Object References (IDOR)

**Testing approach:**
- Test horizontal privilege escalation (accessing peer resources)
- Test vertical privilege escalation (accessing admin functions)
- Manipulate URL parameters and API requests
- Test forced browsing to restricted pages

**Remediation:**
- Implement proper authorization checks on all endpoints
- Use deny-by-default access control
- Enforce ownership checks for user-specific resources
- Log access control failures and alert on suspicious patterns

### 2. Cryptographic Failures

**Description:** Sensitive data exposed due to weak or missing encryption.

**Common manifestations:**
- Transmitting sensitive data over HTTP instead of HTTPS
- Storing passwords in plain text or with weak hashing
- Using deprecated cryptographic algorithms (MD5, SHA1)
- Hard-coded encryption keys or API secrets
- Missing encryption for data at rest

**Testing approach:**
- Intercept network traffic to identify unencrypted transmissions
- Review database storage for sensitive data encryption
- Analyze cryptographic algorithm implementations
- Search code for hard-coded secrets

**Remediation:**
- Use TLS 1.2+ for all data in transit
- Implement strong encryption for data at rest
- Use bcrypt, Argon2, or PBKDF2 for password hashing
- Implement proper key management systems
- Disable deprecated cryptographic protocols

### 3. Injection

**Description:** Malicious data sent to interpreters as part of commands or queries.

**Common types:**
- **SQL Injection:** Malicious SQL code in database queries
- **Command Injection:** OS commands executed through application input
- **LDAP Injection:** Malicious LDAP statements
- **XPath Injection:** Malicious XPath queries
- **NoSQL Injection:** Attacks against NoSQL databases

**Testing approach:**
- Submit special characters and SQL syntax in input fields
- Test with payloads like `' OR '1'='1`, `; DROP TABLE users--`
- Use automated tools (SQLmap, Burp Suite)
- Test all input vectors (forms, headers, cookies, APIs)

**Remediation:**
- Use parameterized queries (prepared statements)
- Implement input validation and sanitization
- Use ORM frameworks properly
- Apply principle of least privilege for database accounts
- Implement Web Application Firewalls (WAF)

### 4. Insecure Design

**Description:** Security flaws in the fundamental design and architecture.

**Common manifestations:**
- Missing or ineffective security controls by design
- Failure to use security design patterns
- Lack of threat modeling during design phase
- Business logic flaws
- Missing rate limiting or resource controls

**Testing approach:**
- Review architecture and design documentation
- Conduct threat modeling exercises
- Test business logic workflows for abuse cases
- Evaluate security control coverage

**Remediation:**
- Integrate security into design phase (Secure by Design)
- Conduct threat modeling for new features
- Use established secure design patterns
- Implement defense in depth
- Regular security architecture reviews

### 5. Security Misconfiguration

**Description:** Insecure default configurations, incomplete setups, or verbose error messages.

**Common manifestations:**
- Default credentials still active
- Unnecessary features or services enabled
- Directory listing enabled on web servers
- Detailed error messages exposing system information
- Missing security headers (CSP, HSTS, X-Frame-Options)
- Unpatched systems and outdated software

**Testing approach:**
- Scan for default credentials
- Check HTTP security headers
- Test for directory traversal and listing
- Review error messages for information disclosure
- Verify unnecessary services are disabled

**Remediation:**
- Implement secure baseline configurations
- Disable unnecessary features and services
- Change all default credentials
- Implement proper error handling (generic messages)
- Regular security configuration reviews
- Automated configuration management

### 6. Vulnerable and Outdated Components

**Description:** Using components with known vulnerabilities or outdated versions.

**Common manifestations:**
- Outdated frameworks, libraries, or dependencies
- Unsupported or end-of-life software
- Components with known CVEs
- Lack of dependency tracking
- Delayed patching processes

**Testing approach:**
- Inventory all components and versions
- Cross-reference with CVE databases
- Use Software Composition Analysis (SCA) tools
- Check for end-of-life components

**Remediation:**
- Maintain inventory of all components and versions
- Subscribe to security advisories for used components
- Implement automated dependency scanning
- Establish regular patching schedule
- Remove unused dependencies

### 7. Identification and Authentication Failures

**Description:** Weaknesses in authentication mechanisms allowing unauthorized access.

**Common manifestations:**
- Weak password policies
- Missing or ineffective multi-factor authentication
- Credential stuffing vulnerabilities
- Session fixation attacks
- Insecure password recovery mechanisms
- Predictable session identifiers

**Testing approach:**
- Test password complexity requirements
- Attempt brute force attacks (with rate limiting checks)
- Test session management (fixation, hijacking)
- Evaluate MFA implementation
- Test password reset functionality

**Remediation:**
- Implement strong password policies
- Require multi-factor authentication
- Implement account lockout and rate limiting
- Use secure session management
- Implement CAPTCHA for sensitive operations
- Monitor for credential stuffing attacks

### 8. Software and Data Integrity Failures

**Description:** Code and infrastructure that doesn't protect against integrity violations.

**Common manifestations:**
- Insecure deserialization vulnerabilities
- Unsigned or unverified software updates
- Insecure CI/CD pipelines
- Untrusted CDN sources
- Missing integrity checks for critical data

**Testing approach:**
- Test deserialization of untrusted data
- Review CI/CD pipeline security
- Verify software update mechanisms
- Check for Subresource Integrity (SRI) on CDN resources

**Remediation:**
- Implement digital signatures for software updates
- Use Subresource Integrity for CDN resources
- Secure CI/CD pipelines with proper access controls
- Avoid deserializing untrusted data
- Implement integrity verification for critical data

### 9. Security Logging and Monitoring Failures

**Description:** Insufficient logging and monitoring to detect and respond to security incidents.

**Common manifestations:**
- Missing logs for security-relevant events
- Logs not monitored or reviewed
- Insufficient log detail for investigation
- Logs stored insecurely or without integrity protection
- Missing alerting for suspicious activities

**Testing approach:**
- Review logging coverage for security events
- Test if attacks are logged and detected
- Evaluate log retention and protection
- Assess incident response capabilities

**Remediation:**
- Log all authentication, authorization, and input validation failures
- Implement centralized log management (SIEM)
- Set up real-time alerting for suspicious activities
- Protect logs from tampering
- Regular log review and analysis
- Establish incident response procedures

### 10. Server-Side Request Forgery (SSRF)

**Description:** Application makes requests to unintended locations due to insufficient validation.

**Common manifestations:**
- Fetching URLs provided by users without validation
- Accessing internal resources via external input
- Cloud metadata service exploitation
- Port scanning internal networks
- Bypassing firewalls and access controls

**Testing approach:**
- Test URL parameters with internal IP addresses
- Attempt to access cloud metadata endpoints
- Try to access internal services
- Test with various URL schemes (file://, gopher://, etc.)

**Remediation:**
- Validate and sanitize all user-supplied URLs
- Implement allowlist of permitted domains
- Disable unnecessary URL schemes
- Segment network to limit internal access
- Implement network-level controls

---

## Security Testing Principles

### Defense in Depth

Implement multiple layers of security controls so that if one fails, others still provide protection.

**Layers:**
1. Perimeter security (firewalls, IDS/IPS)
2. Network security (segmentation, VLANs)
3. Host security (hardening, antivirus)
4. Application security (input validation, authentication)
5. Data security (encryption, access controls)

### Principle of Least Privilege

Grant minimum necessary permissions for users, applications, and services to perform their functions.

**Implementation:**
- Role-based access control (RBAC)
- Just-in-time privilege elevation
- Regular access reviews
- Separation of duties

### Fail Securely

Ensure that when systems fail, they fail in a secure state rather than exposing vulnerabilities.

**Examples:**
- Default deny for access control
- Generic error messages (no information disclosure)
- Secure session termination on errors
- Graceful degradation without security compromise

### Security by Design

Integrate security considerations from the earliest stages of system design and development.

**Practices:**
- Threat modeling during design
- Security requirements in specifications
- Secure coding standards
- Security testing in CI/CD pipelines

---

## Compliance Frameworks and Standards

### PCI DSS (Payment Card Industry Data Security Standard)

**Requirement 11:** Security Testing Requirements
- 11.3.1: External penetration testing at least annually
- 11.3.2: Internal penetration testing at least annually
- 11.3.3: Exploitable vulnerabilities found must be corrected
- 11.3.4: Testing after significant infrastructure changes

**Scope:** Cardholder Data Environment (CDE) and connected systems

**Testing requirements:**
- Industry-accepted methodologies (PTES, OWASP, NIST)
- Both application and network-layer testing
- Qualified internal resources or external third parties

### HIPAA (Health Insurance Portability and Accountability Act)

**Security Rule Requirements:**
- Regular security risk assessments
- Vulnerability scanning and penetration testing
- Protection of electronic Protected Health Information (ePHI)
- Technical safeguards evaluation

**Testing focus:**
- Access controls to ePHI
- Encryption of data in transit and at rest
- Audit controls and logging
- Integrity controls

### ISO 27001 (Information Security Management)

**Control A.12.6:** Technical Vulnerability Management
- Regular vulnerability assessments
- Penetration testing for critical systems
- Timely remediation of identified vulnerabilities
- Continuous improvement of security controls

**Testing integration:**
- Part of Information Security Management System (ISMS)
- Risk-based approach to testing frequency
- Documentation and evidence requirements

### GDPR (General Data Protection Regulation)

**Article 32:** Security of Processing
- Regular testing and evaluation of security measures
- Appropriate technical and organizational measures
- Risk-based security controls

**Testing considerations:**
- Protection of personal data
- Data breach prevention
- Privacy by design validation

### NIST Cybersecurity Framework

**Identify → Protect → Detect → Respond → Recover**

**Testing alignment:**
- **Identify:** Asset and vulnerability identification
- **Protect:** Validate protective controls
- **Detect:** Test detection capabilities
- **Respond:** Evaluate incident response
- **Recover:** Test recovery procedures

---

## Common Vulnerability Scoring System (CVSS)

### CVSS v3.1 Metrics

**Base Metrics (inherent vulnerability characteristics):**
- **Attack Vector (AV):** Network, Adjacent, Local, Physical
- **Attack Complexity (AC):** Low, High
- **Privileges Required (PR):** None, Low, High
- **User Interaction (UI):** None, Required
- **Scope (S):** Unchanged, Changed
- **Confidentiality Impact (C):** None, Low, High
- **Integrity Impact (I):** None, Low, High
- **Availability Impact (A):** None, Low, High

**Temporal Metrics (change over time):**
- Exploit Code Maturity
- Remediation Level
- Report Confidence

**Environmental Metrics (organization-specific):**
- Modified Base Metrics
- Confidentiality/Integrity/Availability Requirements

### CVSS Score Ranges

| Score | Severity | Typical Characteristics |
|-------|----------|------------------------|
| 9.0-10.0 | Critical | Remote code execution, complete system compromise |
| 7.0-8.9 | High | Significant data exposure, privilege escalation |
| 4.0-6.9 | Medium | Information disclosure, limited impact |
| 0.1-3.9 | Low | Minor information leakage, difficult to exploit |

### Using CVSS in Practice

1. **Calculate base score** using vulnerability characteristics
2. **Adjust for temporal factors** (exploit availability, patches)
3. **Apply environmental context** (asset criticality, compensating controls)
4. **Prioritize remediation** based on final score and business impact
5. **Track over time** as exploits mature and patches become available

---

## Security Testing in SDLC

### Shift-Left Security

Integrate security testing early and throughout the development lifecycle.

**Requirements Phase:**
- Security requirements definition
- Threat modeling
- Risk assessment

**Design Phase:**
- Security architecture review
- Design pattern validation
- Attack surface analysis

**Development Phase:**
- Secure code review
- Static Application Security Testing (SAST)
- Unit testing with security cases

**Testing Phase:**
- Dynamic Application Security Testing (DAST)
- Interactive Application Security Testing (IAST)
- Penetration testing

**Deployment Phase:**
- Configuration security review
- Infrastructure security testing
- Pre-production penetration testing

**Operations Phase:**
- Continuous vulnerability scanning
- Regular penetration testing
- Security monitoring and incident response

### DevSecOps Integration

**Automated Security Testing:**
- SAST in code commits
- DAST in CI/CD pipelines
- Dependency scanning for vulnerabilities
- Container security scanning
- Infrastructure as Code (IaC) security validation

**Continuous Monitoring:**
- Real-time vulnerability detection
- Security metrics dashboards
- Automated alerting
- Compliance monitoring

**Rapid Remediation:**
- Automated patching where possible
- Fast-track security fixes
- Rollback capabilities
- Post-deployment verification
