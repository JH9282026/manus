---
name: cloud-cost-optimization
description: "Implement cloud cost optimization strategies using FinOps principles including resource rightsizing, reserved instances, savings plans, spot/preemptible instances, cost allocation tagging, budget alerts, and continuous optimization workflows. Use for: reducing AWS/Azure/GCP spend, rightsizing over-provisioned resources, selecting commitment discount strategies, implementing cost allocation and showback, setting up budget alerts, and building FinOps practices."
---

# Cloud Cost Optimization

Reduce cloud spend systematically using FinOps principles, rightsizing, commitment discounts, and continuous optimization.

## Overview

This skill provides actionable frameworks for controlling and reducing cloud costs across AWS, Azure, and GCP — from quick wins through structural optimization. It covers the FinOps lifecycle, resource rightsizing, commitment discount strategies, cost allocation, and governance automation.

## Cost Optimization Priority Matrix

| Priority | Action | Typical Savings | Effort | Risk |
|----------|--------|----------------|--------|------|
| 1 | Eliminate waste (unused resources) | 15–30% | Low | None |
| 2 | Rightsize over-provisioned resources | 10–25% | Medium | Low |
| 3 | Purchase commitment discounts (RI/SP) | 30–60% vs on-demand | Medium | Medium (lock-in) |
| 4 | Use spot/preemptible for fault-tolerant workloads | 60–90% vs on-demand | Medium | Medium (interruption) |
| 5 | Architect for cost (serverless, auto-scaling) | 20–50% | High | Low |
| 6 | Negotiate enterprise agreements | 5–15% | Low | None |

## Waste Elimination Checklist

| Resource Type | Waste Signal | Action | AWS Tool |
|--------------|-------------|--------|----------|
| EC2 instances | CPU < 5% for 14 days | Terminate or downsize | Compute Optimizer, Cost Explorer |
| EBS volumes | Unattached for 7+ days | Snapshot and delete | Trusted Advisor |
| Elastic IPs | Not associated with running instance | Release | Trusted Advisor |
| Load balancers | Zero healthy targets | Delete | CloudWatch metrics |
| RDS instances | No connections for 7+ days | Snapshot and delete, or stop | Performance Insights |
| S3 buckets | No access for 90+ days | Lifecycle to Glacier or delete | S3 Storage Lens |
| Snapshots | Older than 90 days, no AMI dependency | Delete | Custom Lambda |
| NAT Gateways | Low throughput relative to cost | Consolidate or use VPC endpoints | Cost Explorer |

## Rightsizing Framework

### EC2 Rightsizing Decision Flow

1. **Collect metrics** — CPU, memory, network, disk I/O over 14–30 days.
2. **Identify candidates** — peak CPU < 40% AND peak memory < 60%.
3. **Select target size** — one size down that accommodates peak + 20% headroom.
4. **Validate** — test in staging, monitor for 48 hours after change.
5. **Automate** — schedule monthly rightsizing reviews.

### Instance Family Optimization

| Current | Consider If | Switch To | Savings |
|---------|------------|-----------|--------|
| General purpose (m-series) | CPU-bound, low memory use | Compute optimized (c-series) | 5–15% |
| General purpose (m-series) | Memory-bound, low CPU | Memory optimized (r-series) | Better price-performance |
| Any Intel instance | Workload is compatible | Graviton (ARM) equivalent | 20–30% |
| Previous generation | Any | Current generation | 10–20% + better performance |

## Commitment Discount Strategy

### AWS Savings Plans vs Reserved Instances

| Feature | Savings Plans | Reserved Instances |
|---------|--------------|-------------------|
| Flexibility | Instance family, region, OS, tenancy | Fixed instance type and region |
| Discount depth | Up to 72% | Up to 72% |
| Commitment | $/hour for 1 or 3 years | Instance count for 1 or 3 years |
| Best for | Dynamic workloads, multi-service | Stable, predictable workloads |
| Coverage | EC2, Fargate, Lambda | EC2 only (standard RI) |

### Commitment Purchase Decision

| Coverage Level | Risk Tolerance | Recommended |
|---------------|---------------|-------------|
| 0–50% of baseline | Conservative | Compute Savings Plans (1-year, no upfront) |
| 50–70% of baseline | Moderate | Compute SP (1-year, partial upfront) + RI for steady-state |
| 70–90% of baseline | Aggressive | 3-year SP + RI mix, partial/all upfront |
| Burstable above baseline | Any | On-demand or spot |

## Spot / Preemptible Instance Strategy

| Use Case | Suitability | Strategy |
|----------|------------|----------|
| Batch processing | Excellent | Spot fleets with diversified instance types |
| CI/CD build agents | Excellent | Spot with fallback to on-demand |
| Stateless web tier (behind ASG) | Good | Mixed instances policy (70% spot, 30% on-demand) |
| Dev/test environments | Excellent | 100% spot with auto-restart |
| Databases / stateful | Poor | Use RI or on-demand instead |
| ML training (checkpointable) | Excellent | Spot with checkpointing to S3 |

## Cost Allocation and Tagging

### Required Tag Schema

| Tag Key | Purpose | Example Values |
|---------|---------|---------------|
| `Environment` | Environment identification | prod, staging, dev, sandbox |
| `Team` | Cost ownership | platform, data, frontend |
| `Project` | Project-level cost tracking | project-alpha, migration-2026 |
| `CostCenter` | Finance allocation | CC-1234, engineering |
| `Owner` | Individual accountability | jane.doe@company.com |
| `ManagedBy` | IaC vs manual | terraform, manual, cdk |

### Enforcement Strategy

- Use AWS SCP or Azure Policy to deny resource creation without required tags.
- Run weekly compliance reports showing untagged resources.
- Auto-tag via IaC modules (embed tags in Terraform modules).
- Set up Cost Anomaly Detection alerts for each cost allocation tag.

## Budget and Alert Configuration

| Alert Type | Threshold | Action |
|-----------|-----------|--------|
| Monthly budget forecast | 80% of budget | Email notification |
| Monthly budget actual | 100% of budget | Email + Slack alert |
| Anomaly detection | 20% spike vs. baseline | Investigate immediately |
| Daily spend spike | 150% of trailing 7-day average | Auto-notification |
| RI/SP utilization | < 80% utilization | Review commitments |

## FinOps Maturity Model

| Phase | Focus | Key Actions |
|-------|-------|------------|
| Crawl | Visibility | Tagging, cost dashboards, basic budgets |
| Walk | Optimization | Rightsizing, commitment purchases, waste elimination |
| Run | Operations | Automated governance, showback/chargeback, architectural optimization |

## Best Practices

1. **Tag from day one** — retrofitting tags is expensive and incomplete.
2. **Rightsize before committing** — don't buy reservations for over-provisioned resources.
3. **Start with Savings Plans** — more flexible than RIs for most workloads.
4. **Review monthly** — cloud costs drift; make optimization a recurring process.
5. **Use multiple levers** — combine rightsizing + commitments + spot for maximum savings.
6. **Make costs visible** — dashboards for engineering teams drive behavior change.

## Using the Reference Files

### When to Read Each Reference

**`/references/fundamentals.md`** — Read when learning FinOps principles, understanding cloud pricing models (on-demand, reserved, spot), or setting up cost visibility for the first time.

**`/references/implementation.md`** — Read when executing specific optimization actions like purchasing Savings Plans, configuring auto-scaling policies, setting up Cost Explorer reports, or implementing automated waste cleanup with Lambda.

**`/references/best-practices.md`** — Read when establishing FinOps governance, building organizational cost culture, designing multi-account cost allocation strategies, or preparing executive cost optimization reports.
