---
name: infrastructure-as-code
description: "Define and manage cloud infrastructure declaratively using Terraform, AWS CloudFormation, Pulumi, and OpenTofu including state management, module design, drift detection, CI/CD integration, and multi-environment promotion. Use for: writing Terraform configurations, designing reusable IaC modules, managing remote state, implementing infrastructure CI/CD pipelines, migrating from manual infrastructure to code, and enforcing policy-as-code with Sentinel or OPA."
---

# Infrastructure as Code

Define, provision, and manage cloud infrastructure declaratively using IaC tools and patterns.

## Overview

This skill covers the practical workflows of Infrastructure as Code — from choosing the right tool through writing maintainable configurations, managing state safely, designing reusable modules, and integrating IaC into CI/CD pipelines. It focuses on production-grade patterns and the decisions that prevent costly mistakes.

## IaC Tool Selection Guide

| Tool | Language | State Management | Multi-Cloud | Learning Curve | Best For |
|------|----------|-----------------|-------------|---------------|----------|
| Terraform (OpenTofu) | HCL | Remote state file | Excellent | Moderate | Multi-cloud, most teams |
| AWS CloudFormation | YAML/JSON | Managed by AWS | AWS only | Moderate | AWS-only shops, native integration |
| Pulumi | Python, TypeScript, Go, C# | Pulumi Cloud or self-managed | Excellent | Higher (general-purpose lang) | Teams preferring real programming languages |
| AWS CDK | TypeScript, Python, Java, Go | CloudFormation under the hood | AWS only (CDK for TF exists) | Moderate–High | AWS + programming language preference |
| Ansible | YAML | Stateless (idempotent tasks) | Multi-cloud | Low | Configuration management, simple provisioning |
| Crossplane | YAML (K8s CRDs) | Kubernetes as control plane | Multi-cloud | High | Kubernetes-native teams |

## Terraform Core Workflow

### Standard Lifecycle

```
terraform init → terraform plan → review → terraform apply → terraform destroy (when done)
```

| Command | Purpose | Safety Notes |
|---------|---------|-------------|
| `terraform init` | Initialize providers, backend, modules | Run after adding providers or modules |
| `terraform plan` | Preview changes without applying | Always review before apply |
| `terraform apply` | Execute the planned changes | Use `-auto-approve` only in CI with reviewed plan |
| `terraform destroy` | Remove all managed resources | Requires confirmation, never auto-approve in prod |
| `terraform import` | Bring existing resources under management | Does not generate config — write it manually |
| `terraform state` | Inspect/modify state | Use `state mv` and `state rm` cautiously |

### State Management Best Practices

| Practice | Implementation | Why |
|----------|---------------|-----|
| Remote backend | S3 + DynamoDB (AWS), GCS (GCP), azurerm (Azure) | Team collaboration, state locking |
| State locking | DynamoDB table for S3 backend | Prevent concurrent modifications |
| State encryption | Enable SSE on S3 bucket | Protect sensitive values in state |
| State isolation | Separate state per environment | Blast radius reduction |
| No manual edits | Never edit `.tfstate` directly | Corruption risk |
| Backup | Enable versioning on state bucket | Recovery from bad applies |

## Module Design Patterns

### Module Structure

```
modules/
└── vpc/
    ├── main.tf          # Resource definitions
    ├── variables.tf     # Input variables with descriptions and types
    ├── outputs.tf       # Output values for consumers
    ├── versions.tf      # Required providers and versions
    └── README.md        # Usage examples
```

### Module Best Practices

1. **Single responsibility** — one module per logical infrastructure unit (VPC, EKS cluster, RDS).
2. **Expose via variables** — make configurable what differs between environments.
3. **Sane defaults** — provide default values for optional variables.
4. **Pin versions** — pin module source versions and provider versions.
5. **Output everything useful** — IDs, ARNs, endpoints for downstream modules.
6. **Document** — include usage examples in README.

## Multi-Environment Strategy

| Strategy | Structure | Pros | Cons |
|----------|-----------|------|------|
| Workspaces | Single config, multiple workspaces | Simple, DRY | Shared state backend, risky |
| Directory per env | `envs/dev/`, `envs/staging/`, `envs/prod/` | Clear isolation | Code duplication |
| Terragrunt | DRY config with inheritance | Minimal duplication, clear hierarchy | Extra tool dependency |
| Variable files | Single config + `dev.tfvars`, `prod.tfvars` | Simple, familiar | Easy to apply wrong vars |

**Recommended:** Directory per environment with shared modules for most teams. Use Terragrunt for complex multi-account setups.

## IaC CI/CD Pipeline

### Pipeline Stages

| Stage | Action | Gate |
|-------|--------|------|
| Lint | `terraform fmt -check`, `tflint` | Fail on format or lint errors |
| Validate | `terraform validate` | Fail on syntax errors |
| Security scan | `tfsec`, `checkov`, or `trivy config` | Fail on HIGH/CRITICAL findings |
| Plan | `terraform plan -out=plan.tfplan` | Generate plan artifact |
| Review | Human review of plan output | Manual approval for prod |
| Apply | `terraform apply plan.tfplan` | Only from reviewed plan |
| Drift detection | Scheduled `terraform plan` (no apply) | Alert on detected drift |

### Policy as Code

| Tool | Works With | Language | Use For |
|------|-----------|----------|---------|
| HashiCorp Sentinel | Terraform Cloud/Enterprise | Sentinel policy language | Enforce org-wide policies |
| OPA / Conftest | Any IaC tool | Rego | Open-source policy enforcement |
| AWS SCP | CloudFormation, any AWS | JSON | Account-level guardrails |
| Checkov | Terraform, CFN, K8s | Python (built-in rules) | Security scanning |

## Common Patterns and Anti-Patterns

| Pattern ✅ | Anti-Pattern ❌ |
|-----------|----------------|
| Remote state with locking | Local state file checked into git |
| Modules for reuse | Copy-pasting resource blocks |
| Plan before apply | `apply -auto-approve` in production |
| Pin provider versions | Unpinned providers (breaking changes) |
| Small, focused state files | Monolithic state with 500+ resources |
| Tagging all resources | Untagged resources (cost/ownership chaos) |
| Secrets in vault/SSM | Secrets hardcoded in `.tf` files |

## Best Practices

1. **Review every plan** — treat `terraform plan` output like a code review diff.
2. **Use remote state from day one** — migrating later is painful.
3. **Tag everything** — owner, environment, project, cost center.
4. **Limit blast radius** — split state by service, not monolithically.
5. **Automate drift detection** — run scheduled plans to catch manual changes.
6. **Version control all IaC** — same review process as application code.

## Using the Reference Files

### When to Read Each Reference

**`/references/fundamentals.md`** — Read when learning HCL syntax, understanding Terraform's resource graph and dependency model, or setting up a new IaC project from scratch.

**`/references/implementation.md`** — Read when writing specific resource configurations, implementing complex module patterns, managing state migrations, or integrating IaC with CI/CD pipelines with exact code examples.

**`/references/best-practices.md`** — Read when designing multi-account IaC architectures, establishing team conventions, implementing policy-as-code, or troubleshooting common Terraform errors and state issues.
