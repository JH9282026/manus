---
name: security-testing-penetration
description: "Conduct comprehensive security testing and penetration testing to identify, exploit, and document vulnerabilities in systems, applications, and networks. Use for: planning and executing penetration tests, performing vulnerability assessments, conducting security audits, implementing OWASP and PTES methodologies, using security testing tools (Nmap, Metasploit, Burp Suite, Wireshark), performing black-box/white-box/gray-box testing, exploiting vulnerabilities ethically, documenting security findings, creating remediation strategies, ensuring compliance with PCI DSS/HIPAA/ISO 27001, and reporting security risks to stakeholders."
---

# Security Testing & Penetration Testing

Conduct systematic security assessments to identify, exploit, and document vulnerabilities before malicious actors can exploit them.

## Overview

This skill provides comprehensive frameworks, methodologies, and best practices for penetration testing and security assessments. It covers industry-standard approaches including OWASP, PTES (Penetration Testing Execution Standard), NIST 800-115, and OSSTMM, along with practical guidance on tools, techniques, exploitation, and professional reporting.

Penetration testing simulates real-world cyberattacks to uncover exploitable weaknesses in systems, applications, or networks. Unlike automated vulnerability scanning, penetration testing requires human expertise to confirm exploitability, assess business impact, and provide actionable remediation guidance.

## Quick Start: Test Type Selection

| Scenario | Test Type | Knowledge Level | Primary Focus | Reference |
|----------|-----------|-----------------|---------------|----------|
| External attack simulation | Black-box | No prior knowledge | Internet-facing assets | `/references/penetration-testing-methodology.md` |
| Insider threat simulation | Gray-box | Limited knowledge | Internal network, privilege escalation | `/references/penetration-testing-methodology.md` |
| Comprehensive code review | White-box | Full system access | Application logic, source code | `/references/penetration-testing-methodology.md` |
| Web application security | OWASP Testing | Varies | OWASP Top 10 vulnerabilities | `/references/security-testing-fundamentals.md` |
| Compliance validation | PCI DSS/HIPAA | Defined scope | Regulatory requirements | `/references/security-testing-fundamentals.md` |

## Core Penetration Testing Phases

All comprehensive penetration tests follow a structured methodology:

### 1. Pre-Engagement & Planning

- Define scope, objectives, and rules of engagement
- Identify critical assets and systems to test
- Establish legal agreements and authorization
- Set timeline and communication protocols
- Determine test type (black/white/gray-box)

### 2. Reconnaissance & Information Gathering

**Passive reconnaissance:**
- Collect publicly available data (OSINT)
- Domain information, DNS records, WHOIS data
- Employee details, organizational structure
- Technology stack identification

**Active reconnaissance:**
- Direct interaction with target systems
- Ping sweeps, DNS queries
- Port scanning and service enumeration
- Network mapping

### 3. Scanning & Discovery

- Identify open ports and running services
- Detect operating systems and versions
- Map network topology and traffic patterns
- Identify technologies, frameworks, and CMS platforms
- Build comprehensive attack surface profile

### 4. Vulnerability Assessment & Analysis

- Analyze gathered data for potential vulnerabilities
- Cross-reference with CVE databases (NVD)
- Assess exploitability and severity (CVSS scoring)
- Prioritize vulnerabilities by business impact
- Validate findings to eliminate false positives

### 5. Exploitation & Access

- Attempt to exploit validated vulnerabilities
- Gain initial access to target systems
- Escalate privileges where possible
- Demonstrate real-world business impact
- Document proof of concept for each exploit

### 6. Post-Exploitation

- Assess depth of compromise
- Test lateral movement capabilities
- Simulate data exfiltration scenarios
- Evaluate persistence mechanisms
- Measure potential business damage

### 7. Reporting & Remediation

- Document all findings with evidence
- Provide CVSS scores and risk ratings
- Include proof of concept and screenshots
- Deliver actionable remediation guidance
- Present executive and technical reports

## Industry-Standard Methodologies

### PTES (Penetration Testing Execution Standard)

Seven-phase approach with hands-on technical guidelines:
- Pre-engagement Interactions
- Intelligence Gathering
- Threat Modeling
- Vulnerability Analysis
- Exploitation
- Post Exploitation
- Reporting

Best for: Practical, real-world attack simulation

### NIST SP 800-115

Four-phase government-standard approach:
- Planning
- Discovery
- Attack
- Reporting

Best for: Compliance-focused testing (PCI, HIPAA), rigorous audit trails

### OWASP Testing Framework

Comprehensive web application security testing:
- Information gathering
- Configuration and deployment testing
- Identity and authentication testing
- Authorization and session management
- Input validation and error handling
- Business logic and client-side testing

Best for: Web applications, API security, OWASP Top 10 validation

### OSSTMM (Open Source Security Testing Methodology Manual)

Holistic operational security assessment across five channels:
- Human Security
- Physical Security
- Wireless Communications
- Telecommunications
- Data Networks

Best for: Comprehensive organizational security, ISO 27001 support

## Essential Testing Tools

| Tool | Category | Primary Use | Skill Level |
|------|----------|-------------|-------------|
| Nmap | Network Scanning | Port scanning, service detection, OS fingerprinting | Beginner |
| Metasploit | Exploitation | Vulnerability exploitation, payload delivery | Intermediate |
| Burp Suite | Web Application | HTTP interception, web vulnerability scanning | Intermediate |
| Wireshark | Network Analysis | Packet capture, traffic analysis, protocol inspection | Intermediate |
| Kali Linux | OS Platform | Pre-configured testing environment (600+ tools) | Beginner |
| OWASP ZAP | Web Application | Automated web app scanning, API testing | Beginner |
| Nikto | Web Scanning | Web server vulnerability scanning | Beginner |
| SQLmap | Database | SQL injection testing and exploitation | Intermediate |
| John the Ripper | Password Cracking | Password strength testing | Intermediate |
| Aircrack-ng | Wireless | WiFi security assessment | Advanced |

## OWASP Top 10 Critical Vulnerabilities (2021)

Prioritize testing for these common high-impact vulnerabilities:

1. **Broken Access Control** — Unauthorized access to resources
2. **Cryptographic Failures** — Weak encryption, exposed sensitive data
3. **Injection** — SQL, command, LDAP injection attacks
4. **Insecure Design** — Fundamental security flaws in architecture
5. **Security Misconfiguration** — Default credentials, unnecessary features
6. **Vulnerable and Outdated Components** — Unpatched libraries, frameworks
7. **Identification and Authentication Failures** — Weak authentication mechanisms
8. **Software and Data Integrity Failures** — Insecure CI/CD, deserialization
9. **Security Logging and Monitoring Failures** — Insufficient detection capabilities
10. **Server-Side Request Forgery (SSRF)** — Unvalidated remote requests

## Test Execution Best Practices

### Maintain Ethical Standards

- Obtain explicit written authorization before testing
- Stay within defined scope at all times
- Avoid causing system damage or data loss
- Protect confidentiality of discovered vulnerabilities
- Follow responsible disclosure practices

### Document Everything

- Record all commands, tools, and techniques used
- Capture screenshots and logs as evidence
- Note timestamps for all activities
- Document both successful and failed attempts
- Maintain detailed chain of exploitation

### Validate Findings

- Confirm exploitability of identified vulnerabilities
- Eliminate false positives through manual verification
- Test vulnerabilities in isolated environments when possible
- Assess real-world business impact
- Prioritize based on CVSS scores and context

### Communicate Effectively

- Provide regular status updates during testing
- Alert stakeholders immediately for critical findings
- Deliver both technical and executive-level reports
- Include clear remediation guidance
- Offer re-testing after fixes are implemented

## Compliance and Regulatory Requirements

### PCI DSS Requirement 11.3

- Annual internal and external penetration testing
- Testing after significant infrastructure changes
- Industry-accepted methodologies required
- Coverage of Cardholder Data Environment (CDE)
- Both application and network-layer testing

### HIPAA Security Rule

- Regular security assessments required
- Vulnerability scanning and penetration testing
- Protection of electronic Protected Health Information (ePHI)
- Risk analysis and management
- Documentation of security measures

### ISO 27001

- Systematic security testing as part of ISMS
- Regular vulnerability assessments
- Penetration testing for critical systems
- Continuous improvement of security controls
- Evidence-based security management

## Risk Assessment and Prioritization

### CVSS Scoring Framework

| CVSS Score | Severity | Priority | Typical Response Time |
|------------|----------|----------|----------------------|
| 9.0 - 10.0 | Critical | P0 | Immediate (24 hours) |
| 7.0 - 8.9 | High | P1 | Urgent (1 week) |
| 4.0 - 6.9 | Medium | P2 | Moderate (1 month) |
| 0.1 - 3.9 | Low | P3 | Planned (3 months) |

### Business Impact Assessment

Consider beyond technical severity:
- Potential financial loss
- Regulatory compliance impact
- Reputational damage risk
- Data sensitivity and volume
- System criticality to operations
- Ease of exploitation
- Likelihood of attack

## Remediation Verification

### Re-Testing Process

1. **Review remediation actions** — Verify fixes address root causes
2. **Re-test specific vulnerabilities** — Confirm vulnerabilities are resolved
3. **Test for regression** — Ensure fixes didn't introduce new issues
4. **Validate security controls** — Confirm proper implementation
5. **Update documentation** — Record verification results
6. **Issue clearance report** — Provide formal sign-off

### Continuous Security Improvement

- Schedule regular penetration tests (annually minimum)
- Implement continuous vulnerability scanning
- Monitor for new CVEs affecting your stack
- Update security controls based on findings
- Train development teams on secure coding
- Integrate security into SDLC processes

## Using the Reference Files

### When to Read Each Reference

**`/references/security-testing-fundamentals.md`** — Read when you need foundational knowledge of security testing concepts, vulnerability types, OWASP Top 10 details, security principles, compliance frameworks, or understanding the difference between vulnerability assessment and penetration testing.

**`/references/penetration-testing-methodology.md`** — Read when planning or executing a penetration test, implementing PTES/NIST/OWASP methodologies, conducting reconnaissance, performing threat modeling, or structuring a comprehensive security assessment.

**`/references/tools-techniques.md`** — Read when selecting security testing tools, learning tool-specific techniques, performing network scanning, web application testing, exploitation, password cracking, wireless security testing, or setting up a testing environment.

**`/references/reporting-remediation.md`** — Read when documenting security findings, creating penetration test reports, writing executive summaries, providing remediation guidance, prioritizing vulnerabilities, communicating with stakeholders, or conducting re-testing and verification.

## References

- [Penetration Testing Methodology](references/penetration-testing-methodology.md)
- [Reporting Remediation](references/reporting-remediation.md)
- [Security Testing Fundamentals](references/security-testing-fundamentals.md)
- [Tools Techniques](references/tools-techniques.md)
