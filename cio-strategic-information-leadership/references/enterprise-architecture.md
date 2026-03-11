# Enterprise Architecture

Design and govern enterprise architecture using TOGAF and industry frameworks.

---

## TOGAF Architecture Development Method (ADM)

### ADM Phases

| Phase | Focus | Key Deliverables |
|---|---|---|
| Preliminary | Framework setup | Architecture principles, governance model |
| A: Architecture Vision | Strategic direction | Vision document, stakeholder map |
| B: Business Architecture | Business capabilities | Capability model, process maps |
| C: Information Systems | Data and applications | Data models, application portfolio |
| D: Technology Architecture | Infrastructure | Technology standards, reference architecture |
| E: Opportunities & Solutions | Transition planning | Gap analysis, solution building blocks |
| F: Migration Planning | Implementation roadmap | Project portfolio, sequencing plan |
| G: Implementation Governance | Execution oversight | Compliance reviews, architecture waivers |
| H: Architecture Change Management | Continuous management | Change requests, architecture updates |

---

## Application Rationalization

### Application Assessment Framework

Evaluate each application on two dimensions:
- **Business value** (high/low) — strategic importance, user dependency, revenue impact
- **Technical health** (high/low) — maintainability, security posture, technology currency

**Rationalization Actions:**

| | High Technical Health | Low Technical Health |
|---|---|---|
| **High Business Value** | Invest — modernize, extend | Transform — refactor or replace |
| **Low Business Value** | Maintain — minimize investment | Retire — decommission |

### Integration Patterns

| Pattern | Use Case | Complexity |
|---|---|---|
| API-led connectivity | Modern application integration | Medium |
| Event-driven (pub/sub) | Real-time, loosely coupled | Medium-High |
| ETL/batch | Data warehousing, reporting | Low-Medium |
| iPaaS | SaaS-to-SaaS integration | Low |
| ESB | Legacy enterprise integration | High |

---

## Architecture Governance

### Architecture Review Board (ARB)

**Purpose:** Ensure technology decisions align with enterprise architecture standards and strategy.

**Membership:** CIO (chair), Enterprise Architect, Security Architect, Business representatives, Infrastructure lead

**Review triggers:**
- New application or platform introduction
- Major technology change or upgrade
- Architecture deviation request (waiver)
- Significant integration requirement
- Technology investment over threshold ($100K+)

**Review outcomes:** Approve, approve with conditions, defer, reject
