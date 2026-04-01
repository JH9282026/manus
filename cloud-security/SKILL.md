---
name: cloud-security
description: "Design and implement cloud security architectures including IAM policies, network segmentation, encryption at rest and in transit, Zero Trust models, compliance frameworks (SOC 2, HIPAA, PCI-DSS), security monitoring, CSPM, and incident response. Use for: hardening AWS/Azure/GCP environments, configuring least-privilege IAM, implementing network security groups, encrypting data, setting up SIEM and alerting, achieving compliance certifications, and responding to cloud security incidents."
---

# Cloud Security

Design and implement comprehensive security architectures for AWS, Azure, and GCP cloud environments.

## Overview

This skill provides actionable frameworks for securing cloud infrastructure across the shared responsibility model — covering identity and access management, network security, data protection, compliance, monitoring, and incident response. It focuses on practical implementation patterns rather than theoretical concepts.

## Shared Responsibility Model Quick Reference

| Layer | Customer Responsibility | Cloud Provider Responsibility |
|-------|------------------------|------------------------------|
| Data | Classification, encryption, access control | Physical storage security |
| Applications | Code security, patching, configuration | N/A (unless managed service) |
| Identity | IAM policies, MFA, credential rotation | Identity service availability |
| Network | Security groups, NACLs, VPN, firewall rules | Physical network, DDoS base |
| OS / Runtime | Patching, hardening, AV | Hypervisor, host OS (for managed) |
| Physical | N/A | Data center, hardware, power |

## IAM Security Framework

### Least Privilege Implementation

| Principle | Implementation | AWS Example |
|-----------|---------------|-------------|
| No wildcard actions | Specify exact API actions | `s3:GetObject` not `s3:*` |
| Resource scoping | Restrict to specific ARNs | `arn:aws:s3:::my-bucket/*` |
| Condition constraints | Add context-based conditions | `aws:SourceIp`, `aws:MultiFactorAuthPresent` |
| Time-bound access | Use temporary credentials | STS AssumeRole, session duration |
| Permission boundaries | Cap maximum possible permissions | IAM permission boundary policy |

### IAM Security Checklist

1. Enable MFA on all human accounts (enforce with SCP/policy).
2. Eliminate long-lived access keys — use IAM roles and temporary credentials.
3. Implement SSO with identity provider (Okta, Azure AD, Google Workspace).
4. Review IAM Access Analyzer findings weekly.
5. Use service control policies (SCPs) at the organization level.
6. Separate workload accounts from identity accounts (AWS Organizations / Azure Management Groups).
7. Tag all IAM roles with owner, purpose, and expiry date.

## Network Security Architecture

### Defense in Depth Layers

| Layer | AWS | Azure | GCP |
|-------|-----|-------|-----|
| Perimeter | AWS WAF, Shield, CloudFront | Azure Front Door, WAF, DDoS Protection | Cloud Armor, Cloud CDN |
| VPC / VNet | VPC, Internet Gateway | Virtual Network, NSG | VPC, Firewall Rules |
| Subnet isolation | Public/private subnets, NACLs | Subnet + NSG | Subnet + firewall rules |
| Instance level | Security groups (stateful) | NSG (stateful) | Firewall rules (stateful) |
| Service mesh | App Mesh, PrivateLink | Private Link, Service Endpoints | Private Service Connect |
| DNS security | Route 53 DNSSEC | Azure DNS + Private DNS | Cloud DNS DNSSEC |

### Network Segmentation Best Practices

- Isolate workloads into separate VPCs/VNets by environment (dev, staging, prod).
- Use private subnets for all backend services — no direct internet access.
- Route egress traffic through NAT Gateway or proxy for logging and filtering.
- Implement VPC peering or transit gateway with explicit route tables.
- Use PrivateLink / Private Endpoints for accessing cloud services without traversing the internet.

## Data Protection

### Encryption Decision Matrix

| Data State | Method | AWS Service | Key Management |
|-----------|--------|------------|----------------|
| At rest (storage) | AES-256 server-side | S3 SSE, EBS encryption, RDS encryption | KMS (CMK or AWS-managed) |
| At rest (database) | TDE or application-level | RDS TDE, DynamoDB encryption | KMS CMK |
| In transit (external) | TLS 1.2+ | ALB/NLB TLS termination, ACM certificates | ACM auto-renewal |
| In transit (internal) | mTLS or TLS | Service mesh, VPN, PrivateLink | Internal CA or ACM PCA |
| In use (processing) | Confidential computing | Nitro Enclaves | Enclave-managed |
| Key management | HSM-backed KMS | CloudHSM, KMS | Customer-managed CMK |

### Secrets Management

- Store secrets in dedicated vaults: AWS Secrets Manager, Azure Key Vault, GCP Secret Manager.
- Rotate secrets automatically on a schedule (30–90 days for credentials).
- Never hardcode secrets in source code, environment variables on disk, or container images.
- Use IAM roles to authorize secret access — no API keys for secret retrieval.

## Compliance Framework Mapping

| Framework | Focus | Key Cloud Controls |
|-----------|-------|-------------------|
| SOC 2 Type II | Trust principles (security, availability) | Access controls, logging, change management |
| HIPAA | Protected health information | Encryption, BAA, access logs, audit trails |
| PCI-DSS | Cardholder data | Network segmentation, encryption, vulnerability scanning |
| GDPR | EU personal data | Data residency, DPA, right to erasure, consent |
| FedRAMP | US government data | Authorized cloud regions, FIPS 140-2 encryption |
| ISO 27001 | ISMS framework | Risk assessment, controls, continuous monitoring |

## Security Monitoring and Detection

### CSPM and SIEM Architecture

| Component | AWS Tool | Purpose |
|-----------|---------|----------|
| Cloud trail logging | CloudTrail | API activity audit log |
| Config compliance | AWS Config | Resource configuration tracking |
| Threat detection | GuardDuty | ML-based anomaly detection |
| Vulnerability scanning | Inspector | EC2 and container vulnerability assessment |
| SIEM aggregation | Security Hub + OpenSearch | Centralized findings dashboard |
| Alerting | EventBridge + SNS | Real-time notification pipeline |

### Critical Alerts to Configure

1. Root account login or API usage.
2. IAM policy changes outside of CI/CD pipeline.
3. Security group changes allowing 0.0.0.0/0 ingress.
4. S3 bucket policy changes to public access.
5. KMS key deletion scheduled.
6. GuardDuty HIGH severity findings.
7. Unusual cross-region API activity.

## Zero Trust Architecture Principles

1. **Never trust, always verify** — authenticate and authorize every request.
2. **Least privilege access** — grant minimum permissions for minimum time.
3. **Assume breach** — design controls assuming the perimeter is already compromised.
4. **Micro-segmentation** — isolate workloads so lateral movement is blocked.
5. **Continuous verification** — re-evaluate trust based on context (device, location, behavior).

## Incident Response Playbook

| Phase | Actions | Tools |
|-------|---------|-------|
| Detection | Alert fires, triage severity | GuardDuty, SIEM, CloudTrail |
| Containment | Isolate affected resources, revoke credentials | Security groups, IAM, NACL |
| Investigation | Analyze logs, determine blast radius | CloudTrail, VPC Flow Logs, S3 access logs |
| Eradication | Remove malicious resources, patch vulnerability | SSM, Inspector, Config remediation |
| Recovery | Restore from clean backups, re-enable services | Backups, ASG, deployment pipeline |
| Post-mortem | Document root cause, update runbooks | Incident report template |

## Best Practices

1. **Automate security** — use IaC to enforce security configurations (no manual console changes).
2. **Enable logging everywhere** — CloudTrail, VPC Flow Logs, S3 access logs, WAF logs.
3. **Encrypt by default** — enable default encryption on all storage services.
4. **Scan continuously** — run CSPM tools daily, not just at audit time.
5. **Practice incident response** — run tabletop exercises quarterly.
6. **Separate accounts** — use multi-account strategy (security, logging, workload accounts).

## Using the Reference Files

### When to Read Each Reference

**`/references/fundamentals.md`** — Read when learning the shared responsibility model, understanding cloud-native security primitives, or setting up a new cloud account with baseline security controls.

**`/references/implementation.md`** — Read when implementing specific security controls like IAM policies, network architectures, encryption configurations, or compliance-ready logging pipelines with exact code and CLI examples.

**`/references/best-practices.md`** — Read when conducting security reviews, preparing for compliance audits, designing multi-account security architectures, or establishing security governance processes.
