---
name: healthcare-compliance-regulations
description: "Navigate healthcare regulatory compliance including HIPAA, FDA, and industry-specific requirements. Use for: HIPAA Privacy and Security Rule compliance, FDA regulatory submissions, healthcare data protection, patient privacy, medical device regulations, clinical trial compliance, healthcare audit preparation, and regulatory risk assessment."
---

# Healthcare Compliance & Regulations

Navigate healthcare regulatory frameworks including HIPAA, FDA regulations, and industry-specific compliance requirements to protect patient data and meet legal obligations.

## Overview

Healthcare is one of the most heavily regulated industries globally. Non-compliance carries severe consequences: HIPAA violations cost $100 to $50,000 per incident (up to $1.5M/year per category), FDA violations can result in product recalls and criminal prosecution, and data breaches erode patient trust. This skill covers HIPAA Privacy and Security Rules, FDA regulatory pathways, compliance program design, risk assessment, and audit preparation.

## Regulatory Framework Overview

| Regulation | Scope | Primary Requirement | Enforcement | Reference |
|-----------|-------|---------------------|-------------|-----------|
| HIPAA Privacy Rule | PHI use and disclosure | Minimum necessary standard, patient rights | OCR (HHS) fines, $100–$50K/violation | `/references/hipaa-privacy-security.md` |
| HIPAA Security Rule | ePHI safeguards | Administrative, physical, technical safeguards | OCR fines, corrective action plans | `/references/hipaa-privacy-security.md` |
| HITECH Act | Breach notification, EHR | Notify within 60 days, meaningful use | State AG + OCR enforcement | `/references/hipaa-privacy-security.md` |
| FDA 21 CFR Part 820 | Medical device quality | Quality Management System (QMS) | Warning letters, recalls, injunctions | `/references/fda-regulatory-compliance.md` |
| FDA 510(k) | Device premarket clearance | Substantial equivalence demonstration | Clearance required before marketing | `/references/fda-regulatory-compliance.md` |
| FDA PMA | High-risk device approval | Clinical evidence of safety/efficacy | Approval required before marketing | `/references/fda-regulatory-compliance.md` |
| GDPR (healthcare data) | EU patient data | Explicit consent, data minimization | Up to €20M or 4% global revenue | `/references/hipaa-privacy-security.md` |
| State privacy laws | Varies by state | Additional patient protections | State AG enforcement | `/references/hipaa-privacy-security.md` |

## HIPAA Compliance Framework

### Protected Health Information (PHI) Identifiers

| Category | Identifiers | Action Required |
|----------|-------------|-----------------|
| Direct identifiers | Name, SSN, medical record number, photos | De-identify or encrypt; minimum necessary use |
| Geographic | Address (below state level), ZIP code | Remove or generalize to 3-digit ZIP |
| Date-related | Birth date, admission/discharge dates, death date | Generalize to year or age range |
| Contact | Phone, fax, email, URLs, IP addresses | Remove or encrypt |
| Unique identifiers | License numbers, device IDs, biometric | Remove or encrypt |

### HIPAA Security Rule Safeguards

| Safeguard Type | Key Requirements | Implementation Examples |
|---------------|------------------|----------------------|
| **Administrative** | Risk analysis, workforce training, incident response | Annual risk assessment, mandatory training, incident response plan |
| **Physical** | Facility access, workstation security, device controls | Badge access, screen locks, device encryption, media destruction |
| **Technical** | Access control, audit controls, transmission security | Role-based access, audit logging, TLS encryption, MFA |

### HIPAA Risk Assessment Process

| Step | Activity | Output |
|------|----------|--------|
| 1. Scope | Identify all systems that create, store, or transmit ePHI | System inventory |
| 2. Identify threats | Catalog potential threat sources and events | Threat catalog |
| 3. Identify vulnerabilities | Assess existing controls and gaps | Vulnerability list |
| 4. Determine likelihood | Rate probability of each threat-vulnerability pair | Likelihood ratings (High/Med/Low) |
| 5. Determine impact | Assess consequence of each exploitation | Impact ratings |
| 6. Calculate risk | Likelihood × Impact for each scenario | Risk matrix |
| 7. Recommend controls | Propose mitigations for High and Critical risks | Remediation plan |
| 8. Document | Record methodology, findings, and decisions | Risk assessment report |

## FDA Regulatory Pathways

### Device Classification & Pathway Selection

| Class | Risk Level | Examples | Regulatory Pathway | Timeline | Reference |
|-------|-----------|---------|-------------------|----------|-----------|
| Class I | Low | Bandages, tongue depressors | Exempt or 510(k) | N/A or 3–6 months | `/references/fda-regulatory-compliance.md` |
| Class II | Moderate | Blood pressure cuffs, pregnancy tests | 510(k) clearance | 3–12 months | `/references/fda-regulatory-compliance.md` |
| Class III | High | Pacemakers, hip implants | PMA approval | 1–3 years | `/references/fda-regulatory-compliance.md` |
| De Novo | Novel, low-moderate risk | New device types without predicate | De Novo classification | 6–12 months | `/references/fda-regulatory-compliance.md` |
| SaMD | Software as Medical Device | Clinical decision support, diagnostics | 510(k), De Novo, or PMA | Varies | `/references/fda-regulatory-compliance.md` |

### 510(k) Submission Components
1. Cover letter and CDRH presubmission correspondence
2. Device description and intended use
3. Substantial equivalence comparison to predicate device
4. Performance testing data (bench, animal, clinical as needed)
5. Biocompatibility data (ISO 10993)
6. Software documentation (IEC 62304 if applicable)
7. Labeling, including instructions for use
8. Sterilization validation (if applicable)
9. Electromagnetic compatibility (IEC 60601 if applicable)

## Compliance Program Design

### Essential Program Components

| Component | Purpose | Frequency |
|-----------|---------|-----------|
| Written policies and procedures | Document compliance requirements | Review annually |
| Compliance officer appointment | Designated accountability | Permanent role |
| Workforce training | Ensure awareness and competence | Annual + new hire |
| Risk assessments | Identify and prioritize risks | Annual minimum |
| Internal auditing | Verify compliance, identify gaps | Quarterly or semi-annual |
| Incident response plan | Structured breach/violation response | Test annually |
| Vendor management (BAAs) | Extend compliance to business associates | At contract signing, review annually |
| Documentation and record retention | Prove compliance, support audits | 6 years (HIPAA), varies for FDA |

### Business Associate Agreement (BAA) Checklist
- ☐ Define permitted uses and disclosures of PHI
- ☐ Require appropriate safeguards
- ☐ Require breach notification within 60 days
- ☐ Ensure BA's subcontractors comply
- ☐ Allow covered entity to terminate if BA violates terms
- ☐ Require return or destruction of PHI at termination
- ☐ Authorize covered entity audits of BA practices

## Audit Preparation

| Audit Type | Triggered By | Scope | Preparation Timeline |
|-----------|-------------|-------|---------------------|
| OCR HIPAA audit | Random selection or complaint | Privacy, Security, Breach Notification | Ongoing readiness |
| State AG investigation | Breach report or complaint | State privacy laws + HIPAA | Immediate response |
| FDA inspection (QSR) | Pre-approval, routine, or for-cause | Quality system, manufacturing | Ongoing + pre-inspection readiness |
| Internal audit | Scheduled or risk-triggered | Full compliance program | 2–4 weeks preparation |

## Best Practices

- **Conduct annual risk assessments** — HIPAA requires it, and it's the foundation of all security decisions
- **Encrypt everything** — encrypt ePHI at rest and in transit; encryption is a safe harbor for breach notification
- **Train everyone, every year** — human error causes the majority of HIPAA breaches
- **Document, document, document** — if it's not written down, it didn't happen for audit purposes
- **Get BAAs before sharing PHI** — never share patient data with vendors without a signed BAA
- **Assume you will be audited** — maintain audit-ready documentation at all times

## Using the Reference Files

**`/references/hipaa-privacy-security.md`** — Read when implementing HIPAA Privacy Rule controls, Security Rule safeguards, breach notification procedures, or de-identification strategies. Covers the full HIPAA compliance framework.

**`/references/fda-regulatory-compliance.md`** — Read when navigating FDA device classification, 510(k) submissions, PMA applications, QMS requirements, or SaMD regulations. Covers regulatory pathway selection and submission requirements.
