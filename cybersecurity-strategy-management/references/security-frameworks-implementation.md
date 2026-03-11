# Security Frameworks & Implementation

## NIST Cybersecurity Framework Implementation

### Identify Function

**Asset Management (ID.AM)**:
- Maintain inventory of all hardware, software, and data assets
- Classify assets by criticality and sensitivity
- Map data flows between systems and external parties
- Document network architecture and communication paths

**Risk Assessment (ID.RA)**:
- Identify threat sources relevant to the organization
- Assess vulnerabilities in systems and processes
- Calculate risk as likelihood × impact for each threat-vulnerability pair
- Prioritize risks using a risk register
- Conduct annual formal risk assessments plus event-triggered reassessments

**Governance (ID.GV)**:
- Establish security policy framework (policies, standards, procedures)
- Define roles and responsibilities (RACI matrix)
- Align security strategy with business objectives
- Ensure board-level security oversight

### Protect Function

**Access Control (PR.AC)**:
- Implement role-based access control (RBAC) or attribute-based (ABAC)
- Enforce multi-factor authentication (MFA) for all privileged access
- Manage privileged accounts with PAM solutions
- Review access quarterly, revoke on role change/departure

**Security Awareness (PR.AT)**:
- Conduct annual security awareness training for all employees
- Run monthly phishing simulations (target <5% click rate)
- Provide role-specific training for IT, developers, executives
- Measure training effectiveness through assessments and behavior change

**Data Security (PR.DS)**:
- Classify data (Public, Internal, Confidential, Restricted)
- Encrypt data at rest (AES-256) and in transit (TLS 1.2+)
- Implement Data Loss Prevention (DLP) for sensitive data
- Establish data retention and destruction policies

---

## ISO 27001 Implementation Roadmap

### Phase 1: Planning (Months 1-3)
1. Obtain management commitment and budget
2. Define ISMS scope and boundaries
3. Establish information security policy
4. Conduct gap assessment against Annex A controls
5. Develop risk assessment methodology

### Phase 2: Risk Assessment (Months 3-5)
1. Identify information assets within scope
2. Identify threats and vulnerabilities for each asset
3. Assess likelihood and impact using consistent criteria
4. Determine risk levels and treatment options
5. Create Statement of Applicability (SoA)

### Phase 3: Implementation (Months 5-10)
1. Implement controls per risk treatment plan
2. Develop required documentation (policies, procedures)
3. Conduct security awareness training
4. Deploy technical controls and monitoring
5. Establish incident management process

### Phase 4: Audit and Certification (Months 10-12)
1. Conduct internal audit of ISMS
2. Hold management review meeting
3. Address nonconformities from internal audit
4. Engage certification body for Stage 1 (documentation review)
5. Complete Stage 2 (implementation audit)

---

## CIS Controls Implementation Groups

### IG1 — Essential Cyber Hygiene (Small/Low-Risk)
- CIS Control 1: Inventory of enterprise assets
- CIS Control 2: Inventory of software assets
- CIS Control 3: Data protection (basic)
- CIS Control 4: Secure configuration
- CIS Control 5: Account management
- CIS Control 6: Access control management
- CIS Control 7: Continuous vulnerability management
- CIS Control 14: Security awareness training

### IG2 — Intermediate (Medium Organizations)
All IG1 controls plus:
- CIS Control 8: Audit log management
- CIS Control 9: Email and web browser protections
- CIS Control 10: Malware defenses
- CIS Control 11: Data recovery
- CIS Control 12: Network infrastructure management
- CIS Control 13: Network monitoring and defense

### IG3 — Advanced (Large/High-Risk)
All IG1 + IG2 controls plus:
- CIS Control 15: Service provider management
- CIS Control 16: Application software security
- CIS Control 17: Incident response management
- CIS Control 18: Penetration testing

---

## Security Governance Framework

### Security Organization Structure

| Role | Responsibility | Reports To |
|------|---------------|------------|
| CISO | Security strategy, program leadership | CEO/CIO/Board |
| Security Architects | Security design, standards | CISO |
| SOC Manager | Security operations, monitoring | CISO |
| GRC Manager | Compliance, risk, audit | CISO |
| Security Engineers | Tool implementation, maintenance | SOC Manager |
| Security Analysts | Monitoring, investigation, response | SOC Manager |

### Security Policy Hierarchy

1. **Security Policy** — Executive-level intent and direction
2. **Standards** — Mandatory requirements (e.g., password complexity)
3. **Procedures** — Step-by-step implementation guides
4. **Guidelines** — Recommended best practices (non-mandatory)
5. **Baselines** — Minimum configuration requirements
