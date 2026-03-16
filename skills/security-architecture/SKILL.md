---
name: security-architecture
description: "Design and implement security architectures using Zero Trust principles, NIST frameworks, and defense-in-depth strategies. Use for: building Zero Trust Architecture, implementing security controls across five pillars (Identity, Devices, Networks, Applications, Data), designing microsegmentation, establishing security governance, and aligning with NIST SP 800-207 standards."
---

# Security Architecture

Design comprehensive security architectures using Zero Trust principles, NIST frameworks, and modern defense strategies.

## Overview

Security architecture in 2026 centers on Zero Trust ("never trust, always verify"), moving from network perimeters to identity and resource-based security. With 10% of large enterprises projected to have mature Zero Trust programs by end of 2026 (up from <1% in 2023) and organizations experiencing 50% fewer breaches with mature implementations, Zero Trust Architecture (ZTA) is essential. This skill covers NIST SP 800-207 framework, five security pillars, and implementation strategies.

## Zero Trust Core Principles

### NIST SP 800-207 Tenets

| Tenet | Description | Implementation |
|-------|-------------|----------------|
| **All resources are assets** | Servers, databases, SaaS, IoT, cloud services | Comprehensive inventory and classification |
| **Secure all communication** | Internal traffic encrypted like external | TLS/mTLS everywhere, no implicit trust |
| **Per-session access** | Authentication per connection | No persistent access, continuous verification |
| **Dynamic policy** | Risk-based access decisions | Context-aware policies (identity, device, behavior) |
| **Monitor asset integrity** | Continuous security posture assessment | Device attestation, patch status, compliance |
| **Dynamic authentication** | Continuous reevaluation | Session monitoring, adaptive access |
| **Collect telemetry** | Comprehensive logging and analysis | SIEM integration, behavioral analytics |

## Five Pillars of Zero Trust

### 1. Identity

**Foundation of Zero Trust:**
- Mandatory MFA for all users
- Automated Identity Governance (IGA)
- Privileged Access Management (PAM)
- Passwordless authentication
- Continuous identity validation

**Implementation:**
- Identity providers (Okta, Azure AD, Ping)
- MFA solutions (Duo, Okta, Microsoft Authenticator)
- PAM platforms (CyberArk, BeyondTrust)
- FIDO2/WebAuthn for passwordless

### 2. Devices

**Endpoint security:**
- Device inventory and tracking
- Endpoint Detection and Response (EDR)
- Device compliance checking
- Mobile Device Management (MDM)
- Device health attestation

**Tools:**
- EDR: CrowdStrike, SentinelOne, Microsoft Defender
- MDM: Intune, Jamf, VMware Workspace ONE
- Device trust: Beyond Identity, Duo Device Trust

### 3. Networks

**Segmentation and inspection:**
- Microsegmentation
- Encrypted communications (TLS 1.3+)
- Software-Defined Networking (SDN)
- DNS security
- Network Detection and Response (NDR)

**Technologies:**
- Microsegmentation: Illumio, VMware NSX, Cisco ACI
- ZTNA: Zscaler, Cloudflare Access, Palo Alto Prisma
- NDR: Darktrace, ExtraHop, Vectra AI

### 4. Applications and Workloads

**Application security:**
- Application-level access controls
- DevSecOps practices
- API security
- Container and serverless security
- Application-aware firewalls

**Solutions:**
- API security: Salt Security, Traceable, Noname
- Container security: Aqua, Sysdig, Prisma Cloud
- WAF: Cloudflare, Akamai, AWS WAF

### 5. Data

**Ultimate asset protection:**
- Data classification
- Data Loss Prevention (DLP)
- Encryption (at rest and in transit)
- Data access governance
- Rights management
- Activity monitoring

**Platforms:**
- DLP: Symantec, Forcepoint, Microsoft Purview
- Encryption: Vormetric, AWS KMS, Azure Key Vault
- CASB: Netskope, McAfee MVISION, Zscaler

## Zero Trust Deployment Models

### 1. Enhanced Identity Governance

**Focus:** Strong identity verification

**Components:**
- Robust IAM
- MFA everywhere
- Conditional access policies
- Identity-based microsegmentation

### 2. Micro-Segmentation

**Focus:** Network-level controls

**Approach:**
- Fine-grained security boundaries
- Per-workload/application policies
- East-west traffic control
- Least privilege network access

### 3. Software-Defined Perimeters (SDP)

**Focus:** "Black cloud" model

**Mechanism:**
- Infrastructure invisible to unauthorized
- Broker-based authentication
- Dynamic access provisioning
- Zero standing privileges

## Implementation Roadmap

### Phase 1: Assessment (Months 1-3)
- Current state analysis
- Asset inventory
- Risk assessment
- Stakeholder alignment
- Roadmap development

### Phase 2: Foundation (Months 4-9)
- Identity infrastructure (MFA, SSO)
- Device management (EDR, MDM)
- Network segmentation planning
- Policy framework development

### Phase 3: Deployment (Months 10-18)
- Microsegmentation implementation
- ZTNA deployment
- Application controls
- Data classification and DLP

### Phase 4: Optimization (Months 19-24)
- AI-driven analytics
- Automated response
- Continuous monitoring
- Policy refinement

## Security Frameworks Integration

### NIST Cybersecurity Framework

**Map ZTA to CSF:**
- **Identify:** Asset inventory, risk assessment
- **Protect:** Access controls, data security
- **Detect:** Continuous monitoring, anomaly detection
- **Respond:** Incident response, containment
- **Recover:** Recovery planning, improvements

### NIST SP 800-53

**Control families:**
- AC (Access Control)
- AU (Audit and Accountability)
- IA (Identification and Authentication)
- SC (System and Communications Protection)

## Key Technologies

### SASE and SSE

**Secure Access Service Edge:**
- Converged networking and security
- Cloud-delivered services
- ZTNA, CASB, SWG, FWaaS
- Vendors: Zscaler, Palo Alto Prisma, Netskope

### XDR Platforms

**Extended Detection and Response:**
- Cross-domain visibility
- Automated correlation
- Unified response
- Vendors: Microsoft Sentinel, Palo Alto Cortex, Trend Micro

### SIEM and SOAR

**Security Operations:**
- Log aggregation and analysis
- Threat detection
- Automated response
- Vendors: Splunk, IBM QRadar, Chronicle

## Metrics and KPIs

| Metric | Target | Purpose |
|--------|--------|---------|
| MFA Adoption | 100% | Measure identity security |
| Device Compliance | >95% | Track endpoint security |
| Mean Time to Detect (MTTD) | <15 min | Measure detection speed |
| Mean Time to Respond (MTTR) | <1 hour | Measure response efficiency |
| Security Incidents | Trend down | Track overall security posture |
| Policy Violations | <1% | Measure compliance |

## Using the Reference Files

**`/references/zero-trust-implementation.md`** — Read when implementing Zero Trust Architecture, following NIST SP 800-207, or deploying ZTA components.

**`/references/microsegmentation-strategies.md`** — Read when designing network segmentation, implementing least privilege access, or controlling east-west traffic.

**`/references/identity-security-deep-dive.md`** — Read when strengthening identity controls, implementing MFA/PAM, or adopting passwordless authentication.

**`/references/security-monitoring-siem.md`** — Read when establishing security operations, implementing SIEM/SOAR, or building detection capabilities.
