---
name: healthcare-administration-management
description: "Manage healthcare facility operations including revenue cycle, quality improvement, staff management, and accreditation. Use for: hospital operations management, revenue cycle optimization, healthcare quality metrics, accreditation preparation (Joint Commission, CMS), patient flow optimization, healthcare workforce management, and clinical operations improvement."
---

# Healthcare Administration & Management

Manage healthcare facility operations including revenue cycle, quality improvement, workforce management, and regulatory accreditation to deliver efficient, high-quality patient care.

## Overview

Healthcare administration balances clinical quality, operational efficiency, financial viability, and regulatory compliance. Administrators manage complex systems where a single process failure can impact patient safety, revenue, and accreditation status simultaneously. This skill covers revenue cycle management, quality improvement frameworks, accreditation preparation, patient flow optimization, and workforce management — the operational backbone of healthcare delivery.

## Healthcare Operations Framework

| Domain | Key Processes | KPIs | Reference |
|--------|--------------|------|-----------|
| Revenue Cycle | Scheduling → Registration → Coding → Billing → Collections | Clean claim rate, days in A/R, net collection rate | `/references/revenue-cycle-quality.md` |
| Quality & Safety | Infection control, medication safety, outcomes tracking | HAI rates, mortality index, readmission rates | `/references/revenue-cycle-quality.md` |
| Patient Flow | ED throughput, bed management, discharge planning | ED wait time, length of stay, bed turnover | `/references/revenue-cycle-quality.md` |
| Workforce | Staffing, credentialing, training, retention | RN turnover rate, vacancy rate, overtime % | `/references/compliance-accreditation.md` |
| Compliance | HIPAA, CMS CoP, state regulations | Audit findings, incident reports | `/references/compliance-accreditation.md` |
| Accreditation | Joint Commission, CMS, specialty | Survey readiness score, corrective actions | `/references/compliance-accreditation.md` |

## Revenue Cycle Management

### Revenue Cycle Process Flow

| Stage | Key Activities | Performance Metric | Target |
|-------|---------------|-------------------|--------|
| Scheduling & Pre-registration | Insurance verification, prior auth | Prior auth completion rate | >95% |
| Registration | Demographics, consent, financial counseling | Registration error rate | <2% |
| Charge capture | Clinical documentation, procedure coding | Charge lag (days) | <3 days |
| Coding | ICD-10/CPT assignment, DRG optimization | Coding accuracy rate | >95% |
| Claim submission | Clean claim review, electronic submission | Clean claim rate | >95% (first pass) |
| Payment posting | ERA/EOB processing, contractual adjustments | Days to post | <3 days |
| Denial management | Denial analysis, appeal, resubmission | Denial rate | <5% |
| Collections | Patient statements, payment plans, bad debt | Net collection rate | >95% |

### Revenue Cycle KPI Dashboard

| Metric | Formula | Good | Excellent | Action If Below |
|--------|---------|------|-----------|-----------------|
| Days in A/R | Total A/R ÷ (Annual net revenue ÷ 365) | <40 days | <30 days | Review claim submission delays |
| Clean claim rate | Clean claims ÷ total claims submitted | >95% | >98% | Audit registration and coding |
| Net collection rate | Payments ÷ (charges − contractual adjustments) | >95% | >98% | Review denial patterns |
| Denial rate | Denied claims ÷ total claims | <5% | <3% | Analyze top denial codes |
| Cost to collect | RCM operating cost ÷ total collections | <3% | <2% | Automate manual processes |
| Point-of-service collections | POS collections ÷ total patient responsibility | >30% | >50% | Train front desk staff |

## Quality Improvement Framework

### Core Quality Metrics

| Category | Metric | Data Source | Reporting |
|----------|--------|------------|-----------|
| Patient safety | Hospital-acquired infections (HAI) | Infection surveillance system | Monthly + CMS reporting |
| Clinical outcomes | Risk-adjusted mortality index | Clinical data, AHRQ tools | Quarterly |
| Readmissions | 30-day all-cause readmission rate | Claims data, EHR | Monthly |
| Patient experience | HCAHPS scores (8 composite measures) | Patient surveys | Quarterly (CMS public) |
| Efficiency | Average length of stay (ALOS) | ADT system | Monthly |
| Medication safety | Adverse drug events per 1,000 patient-days | Incident reporting | Monthly |

### PDSA Improvement Cycle

| Phase | Activities | Duration | Output |
|-------|-----------|----------|--------|
| Plan | Identify problem, analyze root cause, design change | 1–2 weeks | Improvement plan with hypothesis |
| Do | Implement change on small scale (pilot) | 2–4 weeks | Pilot results data |
| Study | Analyze pilot data against baseline | 1 week | Statistical comparison |
| Act | Adopt, adapt, or abandon based on results | 1 week | Decision + next cycle plan |

### Root Cause Analysis Tools

| Tool | When to Use | Process |
|------|-------------|---------|
| Fishbone (Ishikawa) diagram | Complex multi-factor problems | Map causes across categories (people, process, equipment, environment) |
| 5 Whys | Simple, single-chain causation | Ask "why" iteratively until root cause found |
| Failure Mode & Effects Analysis | Proactive risk assessment | Rate severity × occurrence × detection for each failure mode |
| Pareto analysis | Prioritizing among many causes | Identify the 20% of causes driving 80% of problems |
| Process mapping | Understanding workflow inefficiencies | Document current state, identify bottlenecks |

## Accreditation Preparation

### Major Accreditation Bodies

| Organization | Scope | Survey Cycle | Key Standards | Reference |
|-------------|-------|-------------|---------------|-----------|
| The Joint Commission (TJC) | Hospitals, ambulatory, behavioral health | Every 3 years (unannounced) | National Patient Safety Goals, EC, IC, HR | `/references/compliance-accreditation.md` |
| CMS (Conditions of Participation) | All Medicare-participating facilities | Varies (complaint-triggered or periodic) | CoPs for hospitals, CAHs, SNFs | `/references/compliance-accreditation.md` |
| DNV Healthcare | Hospitals (ISO 9001-based) | Annual | ISO 9001 + Medicare CoPs | `/references/compliance-accreditation.md` |
| NCQA | Health plans, medical groups | Every 3 years | HEDIS measures, patient experience | `/references/compliance-accreditation.md` |

### Survey Readiness Checklist

| Area | Always-Ready Items | Common Deficiencies |
|------|-------------------|-------------------|
| Environment of Care | Fire drill records, safety inspections, egress clear | Expired fire extinguishers, blocked exits |
| Infection Control | Hand hygiene audits, isolation protocols, sterilization logs | Inconsistent hand hygiene, expired supplies |
| Medication Management | Med storage temps, high-alert drug protocols, reconciliation | Unlabeled medications, missing reconciliation |
| Human Resources | Credential files complete, competency assessments, training records | Expired licenses, missing competency evals |
| Patient Rights | Informed consent, advance directives, complaint process | Missing consents, untrained staff |
| Information Management | EHR downtime procedures, data backup, privacy policies | No downtime plan, incomplete policies |

## Patient Flow Optimization

| Bottleneck | Metric | Intervention | Expected Improvement |
|-----------|--------|-------------|---------------------|
| ED overcrowding | ED wait time, LWBS rate | Full-capacity protocol, rapid triage, vertical flow | -20–30% wait time |
| Bed management | Bed turnover time | Real-time bed tracking, EVS alerts, discharge by 11am goal | -15–25% turnover time |
| Discharge delays | Discharge before noon rate | Discharge planning at admission, multidisciplinary rounds | +20% DBN rate |
| OR utilization | First case on-time start, turnover time | Block scheduling optimization, parallel processing | +10–15% utilization |
| Imaging/lab delays | Turnaround time | STAT protocols, point-of-care testing | -20–40% TAT |

## Best Practices

- **Manage by data, not anecdote** — build dashboards for every operational domain and review weekly
- **Conduct tracer methodology internally** — follow a patient's journey through your facility quarterly to find gaps
- **Automate revenue cycle where possible** — eligibility verification, claim scrubbing, and denial tracking should not be manual
- **Round on staff regularly** — leadership rounding identifies problems before they become incidents
- **Prepare for survey every day** — "survey-ready" is a culture, not a project
- **Connect quality to finance** — CMS value-based purchasing ties quality scores directly to reimbursement

## Using the Reference Files

**`/references/revenue-cycle-quality.md`** — Read when optimizing revenue cycle processes, improving quality metrics, or managing patient flow. Covers billing workflows, denial management, quality improvement methodologies, and throughput optimization.

**`/references/compliance-accreditation.md`** — Read when preparing for accreditation surveys or managing compliance programs. Covers Joint Commission standards, CMS Conditions of Participation, survey readiness, workforce credentialing, and regulatory requirements.
