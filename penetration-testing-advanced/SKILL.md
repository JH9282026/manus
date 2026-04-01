---
name: penetration-testing-advanced
description: "Conduct advanced penetration testing and red team operations using modern techniques, OWASP methodologies, and AI-powered tools. Use for: simulating real-world attacks, identifying security vulnerabilities, testing Active Directory environments, exploiting web applications, conducting client-side attacks, using agentic AI pentesting, and validating security controls."
---

# Penetration Testing Advanced

Conduct sophisticated penetration testing and red team operations using cutting-edge techniques and AI-powered methodologies.

## Overview

Penetration testing in 2026 has evolved from "scan and patch" to "agentic AI pentesting," where AI tools reason independently and execute complex attack chains. With AI agents like Penligent orchestrating multi-agent systems and the OWASP Top 10 remaining foundational, advanced penetration testing requires both technical expertise and strategic thinking. This skill covers manual testing, automated tools, red team tactics, and AI-powered assessment techniques.

## The Agentic Era of Pentesting

### Traditional vs. Agentic AI

| Aspect | Traditional | Agentic AI |
|--------|-------------|------------|
| **Approach** | Scan and report | Reason and act |
| **Speed** | Hours to days | Minutes |
| **Depth** | Surface vulnerabilities | Exploit chains |
| **Feedback** | Manual analysis | Automated refinement |
| **Scale** | Limited by human time | Continuous testing |

### Agentic AI Capabilities

**Penligent Example:**
- Multi-agent orchestration (Recon Expert, Exploit Specialist, Reporting Analyst)
- Chain-of-Thought (CoT) prompting for deep reasoning
- Tool orchestration (Metasploit, Burp, Nmap)
- Autonomous goal-directed hacking
- Zero-day simulation in minutes

**Benefits:**
- Faster, evidence-driven assessments
- Reduced false positives through safe exploitation
- Continuous security validation
- Scalable testing across infrastructure

## OWASP Top 10 and Web Application Testing

### Critical Vulnerabilities

1. **Broken Access Control**
   - IDOR (Insecure Direct Object References)
   - Missing function-level access control
   - Privilege escalation

2. **Cryptographic Failures**
   - Weak encryption
   - Insecure key management
   - Sensitive data exposure

3. **Injection**
   - SQL injection
   - Command injection
   - LDAP/XML injection
   - SSTI (Server-Side Template Injection)

4. **Insecure Design**
   - Missing security controls
   - Threat modeling gaps
   - Business logic flaws

5. **Security Misconfiguration**
   - Default credentials
   - Unnecessary features enabled
   - Verbose error messages

6. **Vulnerable Components**
   - Outdated libraries
   - Unpatched software
   - Supply chain risks

7. **Authentication Failures**
   - Weak passwords
   - Session fixation
   - Credential stuffing

8. **Software/Data Integrity Failures**
   - Insecure deserialization
   - CI/CD pipeline compromise
   - Auto-update without verification

9. **Logging/Monitoring Failures**
   - Insufficient logging
   - No alerting
   - Delayed detection

10. **Server-Side Request Forgery (SSRF)**
    - Internal network access
    - Cloud metadata exploitation
    - Port scanning

## Advanced Testing Techniques

### Web Application Attacks

**SQL Injection:**
```sql
' OR '1'='1' --
' UNION SELECT NULL, username, password FROM users--
'; DROP TABLE users; --
```

**Cross-Site Scripting (XSS):**
```javascript
<script>alert(document.cookie)</script>
<img src=x onerror=alert('XSS')>
```

**Command Injection:**
```bash
; ls -la
| cat /etc/passwd
`whoami`
```

### Active Directory Exploitation

**Kerberos Attacks:**
- Kerberoasting (service account tickets)
- AS-REP roasting (accounts without pre-auth)
- Golden/Silver ticket attacks
- Pass-the-ticket

**Credential Attacks:**
- Password spraying
- Credential dumping (Mimikatz)
- NTLM relay attacks
- DCSync attacks

**Lateral Movement:**
- BloodHound for path analysis
- PsExec for remote execution
- WMI for stealthy movement
- PowerShell remoting

### Client-Side Attacks

**Phishing:**
- Spear phishing campaigns
- Credential harvesting
- Malicious attachments
- Link manipulation

**Social Engineering:**
- Pretexting
- Baiting
- Tailgating
- Vishing (voice phishing)

## Essential Tools

### Reconnaissance

- **Nmap** — Network scanning and service detection
- **Masscan** — Fast port scanner
- **Shodan** — Internet-connected device search
- **theHarvester** — OSINT gathering
- **Recon-ng** — Web reconnaissance framework

### Web Application Testing

- **Burp Suite** — Intercepting proxy, scanner, intruder
- **OWASP ZAP** — Open-source web app scanner
- **Nikto** — Web server scanner
- **SQLmap** — Automated SQL injection
- **w3af** — Web application attack framework

### Exploitation

- **Metasploit** — Exploitation framework
- **Empire** — Post-exploitation framework
- **Cobalt Strike** — Red team platform
- **BeEF** — Browser exploitation
- **Responder** — LLMNR/NBT-NS poisoner

### Post-Exploitation

- **Mimikatz** — Credential extraction
- **BloodHound** — AD attack path mapping
- **PowerSploit** — PowerShell post-exploitation
- **Impacket** — Network protocol toolkit

### AI-Powered

- **Penligent** — Agentic AI pentesting
- **Nuclei** — Vulnerability scanner with templates
- **AI-enhanced Burp** — ML-powered scanning

## Red Team Methodology

### Phases

1. **Reconnaissance**
   - OSINT gathering
   - Network mapping
   - Service enumeration
   - Vulnerability identification

2. **Initial Access**
   - Phishing campaigns
   - Exploit public-facing apps
   - Supply chain compromise
   - Valid accounts

3. **Execution**
   - Command and scripting
   - User execution
   - Exploitation for client execution

4. **Persistence**
   - Create accounts
   - Boot/logon autostart
   - Scheduled tasks
   - Registry modifications

5. **Privilege Escalation**
   - Exploit vulnerabilities
   - Access token manipulation
   - Valid accounts with higher privileges

6. **Defense Evasion**
   - Obfuscation
   - Disable security tools
   - Indicator removal
   - Rootkits

7. **Credential Access**
   - Credential dumping
   - Brute force
   - Input capture
   - Network sniffing

8. **Discovery**
   - Account discovery
   - Network service scanning
   - System information discovery
   - File and directory discovery

9. **Lateral Movement**
   - Remote services
   - Internal spearphishing
   - Exploitation of remote services

10. **Collection**
    - Data from local system
    - Data from network shared drive
    - Screen capture
    - Clipboard data

11. **Exfiltration**
    - Exfiltration over C2 channel
    - Exfiltration over alternative protocol
    - Data compressed

12. **Impact**
    - Data destruction
    - Service stop
    - Resource hijacking

## Testing Platforms and Labs

### Practice Environments

- **PortSwigger Academy** — Structured web security labs
- **OWASP Juice Shop** — Intentionally vulnerable web app
- **HackTheBox** — Penetration testing labs
- **TryHackMe** — Guided cybersecurity training
- **DVWA** — Damn Vulnerable Web Application

### Certifications

- **OSCP** — Offensive Security Certified Professional
- **OSWE** — Offensive Security Web Expert
- **GPEN** — GIAC Penetration Tester
- **CEH** — Certified Ethical Hacker
- **Web-RTA** — Web Red Team Analyst

## Best Practices

### 1. Scope Definition
- Clear boundaries
- Written authorization
- Rules of engagement
- Emergency contacts

### 2. Methodology
- Systematic approach
- Document everything
- Reproduce findings
- Verify exploitability

### 3. Reporting
- Executive summary
- Technical details
- Risk ratings
- Remediation guidance
- Evidence and screenshots

### 4. Ethics
- Stay within scope
- Minimize impact
- Protect data
- Responsible disclosure

## Metrics

| Metric | Purpose |
|--------|---------|
| Vulnerabilities Found | Measure thoroughness |
| Critical/High Findings | Assess risk level |
| Time to Compromise | Measure security effectiveness |
| Lateral Movement Depth | Test segmentation |
| Data Accessed | Evaluate data protection |
| Detection Rate | Test monitoring effectiveness |

## Using the Reference Files

**`/references/owasp-top-10-exploitation.md`** — Read when testing web applications, exploiting common vulnerabilities, or following OWASP methodology.

**`/references/active-directory-attacks.md`** — Read when testing Windows environments, exploiting AD, or conducting enterprise penetration tests.

**`/references/red-team-tactics.md`** — Read when simulating advanced persistent threats, conducting red team operations, or testing detection capabilities.

**`/references/ai-pentesting-tools.md`** — Read when leveraging AI for security testing, using agentic AI platforms, or automating vulnerability discovery.
