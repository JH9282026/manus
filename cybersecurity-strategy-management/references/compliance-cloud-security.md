# Compliance & Cloud Security

## Regulatory Compliance Framework

### GDPR Compliance

**Key Requirements**:
- Lawful basis for processing personal data
- Data subject rights (access, erasure, portability)
- Data Protection Impact Assessments (DPIAs)
- 72-hour breach notification to supervisory authority
- Data Protection Officer (DPO) appointment (when required)
- Records of processing activities
- Cross-border data transfer mechanisms

**Implementation Checklist**:
1. Map all personal data processing activities
2. Establish lawful basis for each processing activity
3. Implement consent management (where applicable)
4. Build data subject request fulfillment process
5. Conduct DPIAs for high-risk processing
6. Implement privacy by design and default
7. Establish breach detection and notification process
8. Document data retention and deletion policies

### HIPAA Compliance

**Key Rules**:
- Privacy Rule: Protects PHI, defines permitted uses/disclosures
- Security Rule: Administrative, physical, technical safeguards
- Breach Notification Rule: Individual and HHS notification requirements

**Security Rule Safeguards**:

| Category | Controls |
|----------|----------|
| Administrative | Risk analysis, workforce training, incident procedures |
| Physical | Facility access, workstation security, device controls |
| Technical | Access control, audit controls, integrity controls, encryption |

### SOC 2 Trust Service Criteria

| Criteria | Focus | Common Controls |
|----------|-------|-----------------|
| Security | Protection against unauthorized access | Firewalls, encryption, MFA, monitoring |
| Availability | System uptime and accessibility | DR/BC plans, redundancy, monitoring |
| Processing Integrity | Data processing accuracy | Input validation, QA, reconciliation |
| Confidentiality | Protection of confidential information | Encryption, access control, classification |
| Privacy | Personal information handling | Consent, collection, use, disclosure controls |

### PCI-DSS v4.0 Requirements

| Requirement | Description |
|-------------|-------------|
| 1 | Install and maintain network security controls |
| 2 | Apply secure configurations to all system components |
| 3 | Protect stored account data |
| 4 | Protect cardholder data with strong cryptography in transit |
| 5 | Protect all systems against malware |
| 6 | Develop and maintain secure systems and software |
| 7 | Restrict access by business need-to-know |
| 8 | Identify users and authenticate access |
| 9 | Restrict physical access to cardholder data |
| 10 | Log and monitor all access |
| 11 | Test security of systems and networks regularly |
| 12 | Support information security with organizational policies |

---

## Cloud Security

### Shared Responsibility Model

| Layer | IaaS | PaaS | SaaS |
|-------|------|------|------|
| Data | Customer | Customer | Customer |
| Applications | Customer | Customer | Provider |
| Runtime/Middleware | Customer | Provider | Provider |
| OS | Customer | Provider | Provider |
| Virtualization | Provider | Provider | Provider |
| Network | Provider | Provider | Provider |
| Physical | Provider | Provider | Provider |

### Cloud Security Architecture

**Identity and Access**:
- Federate identity with organizational IdP (SAML/OIDC)
- Enforce MFA for all cloud console access
- Implement just-in-time privileged access
- Use service accounts with minimal permissions

**Network Security**:
- Implement VPC/VNet segmentation
- Use private endpoints for service-to-service communication
- Deploy WAF for public-facing applications
- Enable flow logs and network monitoring

**Data Protection**:
- Encrypt at rest using cloud-managed or customer-managed keys
- Enforce TLS 1.2+ for all data in transit
- Implement cloud DLP for sensitive data detection
- Configure access logging on all data stores

**Monitoring and Detection**:
- Enable cloud-native logging (CloudTrail, Azure Monitor, Cloud Audit Logs)
- Deploy CSPM for configuration monitoring
- Implement CWPP for workload protection
- Integrate cloud logs with centralized SIEM

### Zero Trust Implementation Roadmap

| Phase | Duration | Focus |
|-------|----------|-------|
| 1 - Foundation | 3-6 months | Identity (MFA, SSO), device inventory, network segmentation |
| 2 - Enhanced | 6-12 months | Microsegmentation, PAM, CASB, endpoint detection |
| 3 - Advanced | 12-18 months | Continuous verification, behavioral analytics, automation |
| 4 - Optimized | 18-24 months | Adaptive policies, AI-driven response, full zero trust |
