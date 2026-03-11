# Cloud Strategy

Develop and execute enterprise cloud migration and optimization strategies.

---

## Cloud Migration Approaches

### The 7 Rs of Cloud Migration

| Strategy | Description | When to Use |
|---|---|---|
| **Rehost** (lift and shift) | Move as-is to cloud infrastructure | Quick migration, minimal change needed |
| **Replatform** (lift and optimize) | Minor optimizations during migration | Moderate benefit, manageable effort |
| **Repurchase** | Replace with SaaS equivalent | SaaS alternative is superior |
| **Refactor/Rearchitect** | Rebuild as cloud-native | Strategic applications, maximum cloud benefit |
| **Retire** | Decommission | Application no longer needed |
| **Retain** | Keep on-premises | Regulatory, latency, or dependency constraints |
| **Relocate** | Move to different cloud region/provider | Data sovereignty, performance optimization |

### Migration Prioritization Framework

Assess each application on:
- **Business criticality** — How important to business operations (1-5)
- **Technical complexity** — Migration difficulty and risk (1-5)
- **Cloud readiness** — Architecture compatibility with cloud (1-5)
- **Business value** — Benefits from cloud migration (1-5)

Plot on a quadrant: **High value + Low complexity = Migrate first**

---

## Cloud Architecture Patterns

### Hybrid Cloud Design

- **Core principle:** Choose the right cloud for the right workload
- **Public cloud** — Variable workloads, new applications, developer environments
- **Private cloud** — Sensitive data, regulatory requirements, predictable workloads
- **Edge** — Low-latency requirements, IoT processing, local data residency
- **Connectivity** — Secure interconnects, consistent networking, unified management

### Multi-Cloud Strategy

| Approach | Advantages | Challenges |
|---|---|---|
| Best-of-breed | Leverage each provider's strengths | Complexity, skills, portability |
| Risk mitigation | Avoid vendor lock-in | Cost duplication, management overhead |
| Geographic | Optimize for regional presence | Inconsistent services, governance |

---

## Cloud Cost Management

### FinOps Framework

1. **Inform** — Visibility into cloud spending by team, project, and service
2. **Optimize** — Right-size instances, use reserved/spot pricing, eliminate waste
3. **Operate** — Real-time budget alerts, automated cost controls, chargeback models

### Cost Optimization Techniques

| Technique | Typical Savings | Effort |
|---|---|---|
| Right-sizing instances | 15-30% | Low |
| Reserved instances/savings plans | 30-50% | Medium |
| Spot/preemptible instances | 60-80% (variable workloads) | Medium |
| Auto-scaling | 20-40% | Medium |
| Storage tiering | 30-50% | Low |
| Idle resource cleanup | 10-20% | Low |
