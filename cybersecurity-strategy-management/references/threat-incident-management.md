# Threat & Incident Management

## Threat Management Program

### Threat Intelligence Lifecycle

1. **Planning** — Define intelligence requirements based on risk profile
2. **Collection** — Gather data from feeds, OSINT, ISACs, dark web monitoring
3. **Processing** — Normalize, correlate, and enrich raw data
4. **Analysis** — Assess relevance, severity, and actionability
5. **Dissemination** — Distribute to stakeholders (SOC, IR, executives)
6. **Feedback** — Refine requirements based on utility

### Threat Actor Categories

| Category | Motivation | Capability | Examples |
|----------|-----------|------------|---------|
| Nation-state (APT) | Espionage, disruption | Very High | APT28, APT41, Lazarus |
| Cybercriminals | Financial gain | Medium-High | Ransomware gangs, BEC |
| Hacktivists | Ideological | Low-Medium | Anonymous, political groups |
| Insiders | Revenge, profit, negligence | Variable | Disgruntled employees |
| Script kiddies | Notoriety | Low | Automated tool users |

### Vulnerability Management Process

1. **Discover** — Scan all assets on regular schedule
2. **Prioritize** — Score by CVSS + asset criticality + exploitability
3. **Remediate** — Patch, mitigate, or accept based on priority
4. **Verify** — Rescan to confirm remediation
5. **Report** — Track metrics (time to remediate, vulnerability density)

**Remediation SLAs**:
| CVSS Score | Severity | Remediation Timeline |
|-----------|----------|---------------------|
| 9.0-10.0 | Critical | 48 hours |
| 7.0-8.9 | High | 7 days |
| 4.0-6.9 | Medium | 30 days |
| 0.1-3.9 | Low | 90 days |

---

## Incident Response Plan

### IR Team Structure

| Role | Responsibility |
|------|---------------|
| IR Commander | Overall incident leadership, decision authority |
| Lead Analyst | Technical investigation, evidence collection |
| Communications Lead | Internal/external communications |
| Legal Counsel | Legal obligations, regulatory notification |
| IT Operations | System containment, recovery |
| Business Liaison | Business impact assessment, stakeholder updates |

### Detailed IR Phases

**Phase 1: Preparation**
- Maintain IR plan and playbooks (review quarterly)
- Ensure tool readiness (SIEM, EDR, forensic tools)
- Conduct tabletop exercises (quarterly) and full simulations (annually)
- Establish communication channels (out-of-band)
- Pre-authorize containment actions for common scenarios

**Phase 2: Detection & Analysis**
- Alert triage workflow (true positive, false positive, suspicious)
- Initial severity classification using defined criteria
- Evidence preservation (memory dumps, disk images, logs)
- Indicator of Compromise (IOC) identification and sharing
- Timeline reconstruction of attacker activity

**Phase 3: Containment**
- Short-term: Isolate affected systems, block malicious IPs/domains
- Long-term: Apply patches, reset credentials, enhance monitoring
- Evidence collection before any destructive containment
- Communication to affected business units

**Phase 4: Eradication**
- Remove malware, backdoors, and persistence mechanisms
- Reset all potentially compromised credentials
- Patch exploited vulnerabilities
- Verify complete removal through scanning and monitoring

**Phase 5: Recovery**
- Restore systems from clean backups
- Rebuild compromised systems from known-good images
- Enhanced monitoring of restored systems (30-90 days)
- Gradual return to normal operations

**Phase 6: Post-Incident**
- Conduct blameless post-mortem within 5 business days
- Document timeline, actions taken, and effectiveness
- Identify gaps in detection, response, and prevention
- Update playbooks, controls, and training
- Report to leadership with improvement recommendations

---

## SOC Operations

### SOC Maturity Levels

| Level | Characteristics |
|-------|----------------|
| Level 1 | Basic SIEM, reactive monitoring, limited coverage |
| Level 2 | 24/7 monitoring, documented playbooks, basic threat intel |
| Level 3 | Proactive hunting, automated response, advanced analytics |
| Level 4 | Threat intelligence-driven, ML-enhanced detection, full automation |
| Level 5 | Predictive, adaptive, integrated with business risk |
