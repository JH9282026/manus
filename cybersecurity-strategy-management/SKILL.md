---
name: "cybersecurity-strategy-management"
description: "Implement cybersecurity frameworks, manage threats, design incident response plans, and establish security governance to protect organizational assets and enable secure digital transformation. Use for: security strategy development, NIST/ISO 27001 implementation, threat assessment, incident response planning, SOC operations, zero trust architecture, cloud security, compliance (GDPR, HIPAA, SOC 2, PCI-DSS), and security awareness programs."
---

# Cybersecurity Strategy & Management

Deliver comprehensive cybersecurity strategy, governance, and operational capabilities across the complete security lifecycle.

## Overview

Enable organizations to protect critical assets, achieve regulatory compliance, and build cybersecurity capabilities proportionate to their risk profile. Cover strategy development, framework implementation, threat management, incident response, and continuous security improvement.

## Security Framework Selection

| Framework | Best For | Scope | Maturity Model |
|-----------|----------|-------|----------------|
| NIST CSF | US organizations, general purpose | Identify, Protect, Detect, Respond, Recover | Tiered (Partial to Adaptive) |
| ISO 27001/27002 | International certification | 14 control domains, 114 controls | Certification-based |
| CIS Controls | Practical implementation priority | 18 critical controls | Implementation groups (IG1-IG3) |
| SOC 2 | SaaS/service providers | Trust Service Criteria (5 categories) | Type I / Type II audit |
| NIST 800-53 | US federal/government | 20 control families, 1000+ controls | Low/Moderate/High baselines |

## NIST Cybersecurity Framework Functions

| Function | Purpose | Key Activities |
|----------|---------|----------------|
| **Identify** | Understand assets and risks | Asset inventory, risk assessment, governance |
| **Protect** | Implement safeguards | Access control, training, data security, maintenance |
| **Detect** | Identify security events | Monitoring, detection processes, anomaly identification |
| **Respond** | Take action on incidents | Response planning, communications, analysis, mitigation |
| **Recover** | Restore capabilities | Recovery planning, improvements, communications |

## Security Maturity Assessment

| Level | Description | Characteristics |
|-------|-------------|----------------|
| 1 - Initial | Ad hoc, reactive | No formal program, tribal knowledge |
| 2 - Developing | Some policies, inconsistent | Basic controls, incomplete coverage |
| 3 - Defined | Documented, standardized | Formal program, consistent processes |
| 4 - Managed | Measured, risk-informed | Metrics-driven, proactive threat management |
| 5 - Optimized | Adaptive, continuous improvement | Threat intelligence-driven, automated response |

## Incident Response Quick Reference

### IR Phase Summary

| Phase | Actions | Key Outputs |
|-------|---------|-------------|
| Preparation | Plans, tools, training, exercises | IR plan, playbooks, team roster |
| Detection | Monitor, alert, triage, classify | Incident ticket, severity classification |
| Containment | Isolate, preserve evidence, limit spread | Containment actions, forensic images |
| Eradication | Remove threat, patch, harden | Root cause identified, threat eliminated |
| Recovery | Restore systems, validate, monitor | Systems restored, enhanced monitoring |
| Lessons Learned | Review, document, improve | Post-incident report, updated playbooks |

### Incident Severity Classification

| Severity | Definition | Response Time | Escalation |
|----------|-----------|---------------|------------|
| Critical (P1) | Active breach, data exfiltration | Immediate | CISO + Executive team |
| High (P2) | Confirmed intrusion, malware spread | <1 hour | Security leadership |
| Medium (P3) | Suspicious activity, policy violation | <4 hours | SOC manager |
| Low (P4) | Minor anomaly, false positive potential | <24 hours | SOC analyst |

## Zero Trust Architecture Principles

1. **Never trust, always verify** — Authenticate and authorize every access request
2. **Assume breach** — Design as if attackers are already inside
3. **Least privilege** — Grant minimum access needed for each task
4. **Microsegmentation** — Isolate workloads and limit lateral movement
5. **Continuous verification** — Re-evaluate trust throughout the session
6. **Encrypt everything** — Protect data in transit and at rest

## Using the Reference Files

### When to Read Each Reference

**`/references/security-frameworks-implementation.md`** — Read when implementing NIST CSF, ISO 27001, CIS Controls, or building security governance structures.

**`/references/threat-incident-management.md`** — Read when building threat management programs, designing incident response plans, developing SOC operations, or conducting security assessments.

**`/references/compliance-cloud-security.md`** — Read when addressing GDPR, HIPAA, SOC 2, PCI-DSS compliance, implementing cloud security, or designing zero trust architecture.
