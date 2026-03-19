# Penetration Testing Methodology

Comprehensive guide to planning, executing, and managing penetration tests using industry-standard frameworks.

---

## Penetration Testing Execution Standard (PTES)

The PTES provides a seven-phase framework for conducting thorough penetration tests with hands-on technical guidelines.

### Phase 1: Pre-Engagement Interactions

**Objective:** Establish clear understanding of scope, objectives, and rules of engagement.

**Key Activities:**

1. **Scope Definition**
   - Identify target systems, networks, and applications
   - Define IP ranges, domains, and URLs in scope
   - Explicitly list out-of-scope items
   - Determine testing windows and blackout periods
   - Establish acceptable testing methods

2. **Goals and Objectives**
   - Define what the test aims to achieve
   - Identify critical assets to protect
   - Determine success criteria
   - Align with business objectives

3. **Legal and Authorization**
   - Obtain written authorization to test
   - Review and sign legal agreements
   - Establish liability and responsibility
   - Define data handling and confidentiality
   - Ensure compliance with regulations

4. **Rules of Engagement**
   - Define testing methodology (black/white/gray-box)
   - Establish communication protocols
   - Set escalation procedures for critical findings
   - Define emergency stop conditions
   - Establish reporting requirements

5. **Resource Planning**
   - Identify required tools and infrastructure
   - Allocate team members and responsibilities
   - Schedule testing timeline
   - Plan for contingencies

**Deliverables:**
- Signed authorization letter
- Statement of Work (SOW)
- Rules of Engagement document
- Project timeline
- Contact list with escalation procedures

### Phase 2: Intelligence Gathering

**Objective:** Collect comprehensive information about the target to inform attack strategies.

**Passive Intelligence Gathering:**

1. **Open Source Intelligence (OSINT)**
   - Search engines (Google dorking)
   - Social media reconnaissance
   - Job postings revealing technologies
   - Public financial reports and press releases
   - Archive.org for historical data

2. **Domain and Network Information**
   - WHOIS lookups for domain registration
   - DNS enumeration (A, MX, NS, TXT records)
   - Subdomain discovery
   - IP range identification (ARIN, RIPE)
   - Autonomous System Number (ASN) lookup

3. **Technology Fingerprinting**
   - Web server identification (headers, error pages)
   - CMS and framework detection
   - Third-party service identification
   - SSL/TLS certificate analysis
   - Technology stack inference

4. **People and Organization**
   - Employee names and roles (LinkedIn)
   - Email address formats
   - Organizational structure
   - Partner and vendor relationships
   - Physical locations

**Active Intelligence Gathering:**

1. **Network Scanning**
   - Ping sweeps to identify live hosts
   - Port scanning (TCP/UDP)
   - Service version detection
   - Operating system fingerprinting
   - Network topology mapping

2. **Service Enumeration**
   - Banner grabbing
   - Service-specific enumeration (SMB, SNMP, LDAP)
   - Application fingerprinting
   - API endpoint discovery
   - Hidden directory and file discovery

3. **Vulnerability Scanning**
   - Automated vulnerability scanners
   - Web application scanners
   - SSL/TLS configuration testing
   - Compliance scanning

**Tools:**
- **Passive:** theHarvester, Shodan, Censys, Maltego, Recon-ng
- **Active:** Nmap, Masscan, Nikto, Dirb, Gobuster, WhatWeb

**Deliverables:**
- Comprehensive target profile
- Network diagrams
- Asset inventory
- Technology stack documentation
- Initial vulnerability list

### Phase 3: Threat Modeling

**Objective:** Analyze gathered intelligence to identify potential attack vectors and prioritize testing efforts.

**Key Activities:**

1. **Asset Identification and Valuation**
   - Catalog all identified assets
   - Assess business criticality
   - Identify sensitive data locations
   - Determine asset dependencies

2. **Attack Surface Analysis**
   - Map all entry points (web apps, APIs, network services)
   - Identify trust boundaries
   - Analyze data flows
   - Identify potential attack paths

3. **Threat Actor Profiling**
   - Define relevant threat actors (external attacker, insider, etc.)
   - Assess threat actor capabilities and motivations
   - Align testing approach with threat scenarios

4. **Attack Vector Prioritization**
   - Rank attack vectors by likelihood and impact
   - Consider ease of exploitation
   - Align with business risk priorities
   - Focus on high-value targets

5. **STRIDE Threat Modeling** (optional framework)
   - **S**poofing identity
   - **T**ampering with data
   - **R**epudiation
   - **I**nformation disclosure
   - **D**enial of service
   - **E**levation of privilege

**Deliverables:**
- Threat model documentation
- Attack tree diagrams
- Prioritized attack vector list
- Risk assessment matrix

### Phase 4: Vulnerability Analysis

**Objective:** Identify and validate exploitable vulnerabilities in target systems.

**Key Activities:**

1. **Vulnerability Identification**
   - Review automated scan results
   - Cross-reference with CVE databases
   - Identify configuration weaknesses
   - Analyze custom application logic
   - Review authentication and authorization mechanisms

2. **Vulnerability Validation**
   - Eliminate false positives through manual testing
   - Confirm exploitability
   - Assess vulnerability context
   - Test compensating controls

3. **Vulnerability Classification**
   - Assign CVSS scores
   - Categorize by OWASP Top 10 or CWE
   - Assess business impact
   - Determine exploitation difficulty

4. **Exploit Research**
   - Search exploit databases (Exploit-DB, Metasploit)
   - Review security advisories
   - Analyze proof-of-concept code
   - Develop custom exploits if needed

5. **Attack Path Planning**
   - Chain vulnerabilities for maximum impact
   - Plan privilege escalation paths
   - Identify lateral movement opportunities
   - Design multi-stage attacks

**Testing Focus Areas:**

**Network Layer:**
- Unencrypted protocols
- Weak authentication
- Network segmentation issues
- Firewall misconfigurations

**Application Layer:**
- Injection vulnerabilities (SQL, command, LDAP)
- Broken authentication and session management
- Cross-Site Scripting (XSS)
- Insecure Direct Object References (IDOR)
- Security misconfigurations

**Infrastructure:**
- Outdated software and missing patches
- Default credentials
- Unnecessary services
- Weak cryptography

**Deliverables:**
- Validated vulnerability list
- CVSS scores and risk ratings
- Exploit availability assessment
- Attack path documentation

### Phase 5: Exploitation

**Objective:** Actively exploit validated vulnerabilities to demonstrate real-world impact.

**Key Activities:**

1. **Initial Access**
   - Execute exploits against identified vulnerabilities
   - Gain foothold on target systems
   - Establish command and control (C2) if applicable
   - Document successful exploitation methods

2. **Privilege Escalation**
   - Enumerate local system for escalation opportunities
   - Exploit kernel vulnerabilities
   - Abuse misconfigurations (sudo, SUID binaries)
   - Leverage weak service permissions
   - Obtain administrative/root access

3. **Lateral Movement**
   - Enumerate network for additional targets
   - Harvest credentials from compromised systems
   - Exploit trust relationships
   - Move to higher-value targets
   - Expand access across network segments

4. **Persistence (if authorized)**
   - Establish backdoors for continued access
   - Create additional user accounts
   - Modify startup scripts
   - Install rootkits or implants
   - Test detection evasion

**Exploitation Best Practices:**

- **Start with least invasive methods** — Minimize system impact
- **Document everything** — Record all commands and actions
- **Take screenshots** — Capture proof of successful exploitation
- **Maintain stealth** (if testing detection) — Avoid triggering alerts
- **Have rollback plan** — Be prepared to restore systems if needed
- **Respect scope** — Never exceed authorized boundaries
- **Communicate critical findings immediately** — Don't wait for final report

**Common Exploitation Techniques:**

**Web Applications:**
- SQL injection for database access
- Command injection for remote code execution
- File upload vulnerabilities for shell access
- XXE (XML External Entity) for file disclosure
- Deserialization attacks

**Network Services:**
- Exploiting unpatched services (EternalBlue, etc.)
- Brute force attacks on weak credentials
- Man-in-the-Middle (MitM) attacks
- SMB relay attacks
- Kerberoasting

**Client-Side:**
- Phishing for credential harvesting
- Malicious document delivery
- Browser exploitation
- Social engineering

**Tools:**
- Metasploit Framework
- SQLmap
- Burp Suite Pro
- Empire/Covenant (C2 frameworks)
- Impacket (Windows exploitation)
- Custom exploit scripts

**Deliverables:**
- Exploitation logs and screenshots
- Proof of concept code
- Compromised system inventory
- Credential harvest documentation
- Attack chain diagrams

### Phase 6: Post-Exploitation

**Objective:** Assess the full extent of compromise and demonstrate business impact.

**Key Activities:**

1. **Impact Assessment**
   - Identify accessible sensitive data
   - Assess potential data exfiltration
   - Evaluate business process disruption
   - Measure scope of compromise
   - Quantify potential financial impact

2. **Data Collection**
   - Enumerate accessible files and databases
   - Identify sensitive information (PII, credentials, IP)
   - Document data classification levels
   - Assess data protection controls
   - **Note:** Do not actually exfiltrate sensitive data

3. **Privilege and Access Analysis**
   - Document achieved privilege levels
   - Map accessible systems and networks
   - Identify additional attack opportunities
   - Assess blast radius of compromise

4. **Persistence and Cleanup**
   - Test persistence mechanisms (if authorized)
   - Document detection evasion techniques
   - Remove all testing artifacts
   - Close backdoors and remove accounts
   - Restore systems to pre-test state

5. **Detection Analysis**
   - Review if attacks were detected
   - Assess security monitoring effectiveness
   - Evaluate incident response capabilities
   - Identify detection gaps

**Post-Exploitation Scenarios:**

**Scenario 1: Data Breach Simulation**
- Locate and document sensitive data
- Demonstrate access to customer records
- Show potential for data exfiltration
- Assess data loss prevention (DLP) controls

**Scenario 2: Ransomware Simulation**
- Demonstrate ability to encrypt files
- Show scope of accessible systems
- Assess backup and recovery capabilities
- Evaluate detection and response time

**Scenario 3: Insider Threat**
- Demonstrate privilege abuse
- Show lateral movement capabilities
- Assess segregation of duties
- Evaluate user activity monitoring

**Deliverables:**
- Business impact assessment
- Sensitive data access documentation
- Compromise scope analysis
- Detection effectiveness report
- Cleanup verification

### Phase 7: Reporting

**Objective:** Communicate findings, risks, and recommendations to stakeholders.

**Report Components:**

1. **Executive Summary**
   - High-level overview of testing
   - Key findings and business risks
   - Overall security posture assessment
   - Critical recommendations
   - Non-technical language for executives

2. **Technical Report**
   - Detailed methodology
   - Comprehensive vulnerability findings
   - Exploitation details and proof of concept
   - Technical remediation guidance
   - CVSS scores and risk ratings

3. **Vulnerability Details** (for each finding)
   - Vulnerability description
   - Affected systems/applications
   - CVSS score and severity rating
   - Business impact assessment
   - Proof of concept/screenshots
   - Detailed remediation steps
   - References (CVE, CWE, OWASP)

4. **Attack Narrative**
   - Step-by-step attack chain
   - Timeline of exploitation
   - Privilege escalation path
   - Lateral movement diagram
   - Final impact achieved

5. **Remediation Roadmap**
   - Prioritized action items
   - Quick wins vs. long-term fixes
   - Estimated effort and timeline
   - Compensating controls
   - Re-testing recommendations

**Reporting Best Practices:**

- **Tailor to audience** — Executive vs. technical versions
- **Prioritize by risk** — Focus on critical and high findings first
- **Provide context** — Explain business impact, not just technical details
- **Be actionable** — Give specific remediation steps
- **Include evidence** — Screenshots, logs, proof of concept
- **Highlight positives** — Acknowledge effective controls
- **Offer support** — Be available for questions and clarification

**Deliverables:**
- Executive summary (2-5 pages)
- Technical report (comprehensive)
- Vulnerability spreadsheet
- Presentation slides for stakeholder briefing
- Raw testing data (logs, screenshots)

---

## NIST SP 800-115 Methodology

The NIST Special Publication 800-115 provides a four-phase approach emphasizing planning, documentation, and compliance.

### Phase 1: Planning

**Objectives:**
- Define testing scope and objectives
- Identify resources and constraints
- Develop testing strategy
- Obtain necessary approvals

**Key Activities:**
- Stakeholder interviews
- Asset identification and prioritization
- Threat and risk assessment
- Rules of engagement development
- Legal and compliance review
- Resource allocation

**Outputs:**
- Test plan document
- Scope statement
- Authorization letters
- Resource allocation plan

### Phase 2: Discovery

**Objectives:**
- Gather information about target environment
- Identify potential vulnerabilities
- Map attack surface

**Key Activities:**
- Network discovery and mapping
- Port and service scanning
- Vulnerability scanning
- Operating system and application fingerprinting
- Wireless network discovery
- Social engineering reconnaissance

**Outputs:**
- Network diagrams
- Asset inventory
- Vulnerability scan reports
- Technology stack documentation

### Phase 3: Attack

**Objectives:**
- Validate vulnerabilities through exploitation
- Demonstrate business impact
- Test security controls

**Key Activities:**
- Vulnerability exploitation
- Privilege escalation
- Password cracking
- Social engineering attacks
- Wireless attacks
- Physical security testing (if in scope)

**Outputs:**
- Exploitation logs
- Proof of concept demonstrations
- Compromised system documentation
- Security control effectiveness assessment

### Phase 4: Reporting

**Objectives:**
- Document findings and recommendations
- Communicate risks to stakeholders
- Provide remediation guidance

**Key Activities:**
- Findings analysis and prioritization
- Report writing (executive and technical)
- Remediation recommendations
- Stakeholder presentations
- Re-testing planning

**Outputs:**
- Comprehensive penetration test report
- Executive briefing
- Remediation roadmap
- Lessons learned documentation

**NIST 800-115 Strengths:**
- Excellent for compliance and audit requirements
- Comprehensive documentation standards
- Suitable for government and regulated industries
- Emphasizes planning and risk management

---

## OWASP Web Security Testing Guide (WSTG)

Specialized methodology for web application security testing.

### Testing Categories

**1. Information Gathering (WSTG-INFO)**
- Conduct search engine discovery
- Fingerprint web server
- Review webserver metafiles
- Enumerate applications on webserver
- Review webpage comments and metadata
- Identify application entry points
- Map execution paths through application

**2. Configuration and Deployment Management (WSTG-CONF)**
- Test network infrastructure configuration
- Test application platform configuration
- Test file extensions handling
- Review old backup and unreferenced files
- Enumerate infrastructure and application admin interfaces
- Test HTTP methods
- Test HTTP Strict Transport Security
- Test RIA cross domain policy

**3. Identity Management (WSTG-IDNT)**
- Test role definitions
- Test user registration process
- Test account provisioning process
- Test account enumeration and guessable user account

**4. Authentication (WSTG-ATHN)**
- Test credentials transported over encrypted channel
- Test default credentials
- Test weak lock out mechanism
- Test bypassing authentication schema
- Test remember password functionality
- Test browser cache weaknesses
- Test weak password policy
- Test weak security question/answer
- Test weak password change or reset functionalities
- Test weaker authentication in alternative channel

**5. Authorization (WSTG-ATHZ)**
- Test directory traversal/file include
- Test bypassing authorization schema
- Test privilege escalation
- Test insecure direct object references

**6. Session Management (WSTG-SESS)**
- Test session management schema
- Test cookies attributes
- Test session fixation
- Test exposed session variables
- Test Cross Site Request Forgery (CSRF)
- Test logout functionality
- Test session timeout
- Test session puzzling

**7. Input Validation (WSTG-INPV)**
- Test reflected Cross Site Scripting
- Test stored Cross Site Scripting
- Test HTTP verb tampering
- Test HTTP parameter pollution
- Test SQL injection
- Test LDAP injection
- Test XML injection
- Test SSI injection
- Test XPath injection
- Test IMAP/SMTP injection
- Test code injection
- Test command injection
- Test format string injection
- Test incubated vulnerability
- Test HTTP splitting/smuggling
- Test HTTP incoming requests
- Test host header injection
- Test server-side template injection

**8. Error Handling (WSTG-ERRH)**
- Test improper error handling
- Test stack traces

**9. Cryptography (WSTG-CRYP)**
- Test weak transport layer security
- Test padding oracle
- Test sensitive information sent via unencrypted channels
- Test weak encryption

**10. Business Logic (WSTG-BUSL)**
- Test business logic data validation
- Test ability to forge requests
- Test integrity checks
- Test for process timing
- Test number of times a function can be used limits
- Test circumvention of work flows
- Test defenses against application misuse
- Test upload of unexpected file types
- Test upload of malicious files

**11. Client-Side (WSTG-CLNT)**
- Test DOM-based Cross Site Scripting
- Test JavaScript execution
- Test HTML injection
- Test client-side URL redirect
- Test CSS injection
- Test client-side resource manipulation
- Test cross origin resource sharing
- Test Cross Site Flashing
- Test clickjacking
- Test WebSockets
- Test web messaging
- Test browser storage

### OWASP Testing Approach

1. **Review and analyze application** — Understand functionality and architecture
2. **Create test cases** — Based on WSTG categories relevant to application
3. **Execute tests** — Manual and automated testing
4. **Document findings** — Record vulnerabilities with evidence
5. **Verify fixes** — Re-test after remediation

---

## Test Type Selection Guide

### Black-Box Testing

**Definition:** Tester has no prior knowledge of target systems.

**Advantages:**
- Simulates external attacker perspective
- Unbiased assessment
- Tests external security posture
- Identifies publicly exposed vulnerabilities

**Disadvantages:**
- Time-consuming reconnaissance phase
- May miss internal vulnerabilities
- Limited depth in time-constrained tests

**Best for:**
- External penetration tests
- Internet-facing application testing
- Simulating opportunistic attackers

### White-Box Testing

**Definition:** Tester has full knowledge and access to target systems.

**Advantages:**
- Comprehensive coverage
- Faster testing (no reconnaissance needed)
- Can test internal logic and code
- Identifies complex vulnerabilities

**Disadvantages:**
- May not reflect real-world attack scenarios
- Requires significant documentation review
- Can be overwhelming with too much information

**Best for:**
- Pre-deployment security validation
- Code review and architecture assessment
- Comprehensive security audits
- Compliance testing

### Gray-Box Testing

**Definition:** Tester has limited knowledge (e.g., user-level access).

**Advantages:**
- Balances realism and efficiency
- Simulates insider threats
- More thorough than black-box
- More realistic than white-box

**Disadvantages:**
- Requires careful scope definition
- May still miss some vulnerabilities

**Best for:**
- Insider threat simulation
- Post-authentication testing
- Privilege escalation testing
- Most real-world scenarios

---

## Specialized Testing Types

### Red Team Engagement

**Objective:** Simulate advanced persistent threat (APT) to test detection and response.

**Characteristics:**
- Long-duration engagement (weeks to months)
- Stealth and evasion focus
- Multi-vector attacks (technical, physical, social)
- Tests blue team (defenders) capabilities
- Realistic adversary simulation

**Deliverables:**
- Attack timeline and techniques used
- Detection gaps identified
- Blue team performance assessment
- Recommendations for improvement

### Purple Team Exercise

**Objective:** Collaborative security improvement through red team and blue team cooperation.

**Characteristics:**
- Red team shares techniques in real-time
- Blue team improves detection and response
- Iterative learning process
- Focus on capability building

**Benefits:**
- Accelerated security improvement
- Knowledge transfer
- Improved collaboration
- Practical training

### Bug Bounty Testing

**Objective:** Crowdsourced vulnerability discovery through incentivized testing.

**Characteristics:**
- Continuous testing by multiple researchers
- Pay-per-vulnerability model
- Defined scope and rules
- Managed through platforms (HackerOne, Bugcrowd)

**Best for:**
- Ongoing security validation
- Diverse testing perspectives
- Cost-effective vulnerability discovery
