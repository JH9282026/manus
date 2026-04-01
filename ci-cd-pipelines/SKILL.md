---
name: ci-cd-pipelines
description: "Design and implement CI/CD pipelines using GitHub Actions, GitLab CI/CD, Jenkins, and ArgoCD for automated building, testing, security scanning, and deployment of applications. Use for: setting up continuous integration workflows, automating test suites, implementing deployment strategies (blue-green, canary, rolling), configuring artifact registries, managing secrets in pipelines, and establishing release promotion across environments."
---

# CI/CD Pipelines

Design and implement automated build, test, and deployment pipelines for reliable software delivery.

## Overview

This skill covers the design and implementation of CI/CD pipelines — from choosing a platform through structuring pipeline stages, implementing deployment strategies, managing secrets, and establishing promotion workflows across environments. It focuses on production-grade patterns that balance speed with safety.

## CI/CD Platform Selection

| Platform | Hosting | Config Format | Best For | Ecosystem |
|----------|---------|--------------|----------|----------|
| GitHub Actions | SaaS (self-hosted runners available) | YAML (`.github/workflows/`) | GitHub-native teams, open source | GitHub Marketplace |
| GitLab CI/CD | SaaS or self-hosted | YAML (`.gitlab-ci.yml`) | GitLab-native teams, all-in-one DevOps | Built-in registry, security |
| Jenkins | Self-hosted | Groovy (Jenkinsfile) | Enterprise, complex pipelines | 1800+ plugins |
| ArgoCD | Self-hosted (K8s) | YAML (Kubernetes manifests) | GitOps K8s deployments | Kubernetes-native |
| CircleCI | SaaS | YAML (`.circleci/config.yml`) | Fast builds, Docker-native | Orbs marketplace |
| AWS CodePipeline | AWS-managed | JSON/YAML + console | AWS-native projects | CodeBuild, CodeDeploy |

## Pipeline Architecture

### Standard CI/CD Stages

| Stage | Purpose | Typical Tools | Failure Action |
|-------|---------|--------------|----------------|
| Source | Trigger on code change | Git push, PR, tag | N/A |
| Build | Compile, package | Docker build, Maven, npm | Block pipeline |
| Unit Test | Fast isolated tests | Jest, pytest, JUnit | Block pipeline |
| Lint / Format | Code quality check | ESLint, Pylint, gofmt | Block pipeline |
| Security Scan | Vulnerability detection | Snyk, Trivy, Semgrep | Block on HIGH/CRITICAL |
| Integration Test | Cross-service tests | Testcontainers, Docker Compose | Block pipeline |
| Artifact Publish | Store build output | ECR, Docker Hub, Artifactory | Block pipeline |
| Deploy to Staging | Automated deploy | Helm, ArgoCD, ECS deploy | Alert team |
| Smoke Test | Verify deployment health | curl, Playwright, k6 | Auto-rollback |
| Deploy to Prod | Controlled release | Same as staging + approval | Manual gate |
| Post-Deploy | Verify, notify | Datadog, Slack webhook | Alert team |

### GitHub Actions Example Structure

```yaml
name: CI/CD Pipeline
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build-and-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Build
        run: docker build -t app:${{ github.sha }} .
      - name: Unit Tests
        run: docker run app:${{ github.sha }} npm test
      - name: Security Scan
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: app:${{ github.sha }}

  deploy-staging:
    needs: build-and-test
    if: github.ref == 'refs/heads/main'
    environment: staging
    steps:
      - name: Deploy to staging
        run: ./deploy.sh staging ${{ github.sha }}

  deploy-prod:
    needs: deploy-staging
    environment:
      name: production
      # Manual approval required
    steps:
      - name: Deploy to production
        run: ./deploy.sh production ${{ github.sha }}
```

## Deployment Strategies

| Strategy | How It Works | Risk Level | Rollback Speed | Best For |
|----------|-------------|------------|---------------|----------|
| Rolling update | Replace instances gradually | Medium | Slow (re-deploy old) | Standard stateless apps |
| Blue-Green | Run two identical environments, switch traffic | Low | Instant (switch back) | Zero-downtime, database-compatible changes |
| Canary | Route small % traffic to new version | Low | Fast (route to old) | High-traffic apps, gradual validation |
| Recreate | Stop old, start new | High | Slow | Dev/test, stateful apps with downtime window |
| Feature flags | Deploy code inactive, enable per-flag | Lowest | Instant (disable flag) | Trunk-based development, A/B testing |
| GitOps (ArgoCD) | Git repo = desired state, controller syncs | Low | Git revert | Kubernetes workloads |

### Canary Deployment Checklist

1. Deploy new version alongside old.
2. Route 5% of traffic to canary.
3. Monitor error rates, latency, and business metrics for 15–30 minutes.
4. If healthy, increase to 25% → 50% → 100%.
5. If unhealthy, route 100% back to old version.
6. Automate progression with Flagger, Argo Rollouts, or AWS CodeDeploy.

## Pipeline Security

### Secrets Management

| Approach | Platform Support | Security Level |
|----------|-----------------|----------------|
| Platform secrets (encrypted) | GitHub Secrets, GitLab CI Variables | Good — encrypted at rest |
| External vault | HashiCorp Vault, AWS Secrets Manager | Best — centralized, audited |
| OIDC federation | GitHub → AWS, GitLab → GCP | Best — no stored credentials |
| Environment-scoped secrets | GitHub Environments, GitLab Protected Variables | Good — env isolation |

### Pipeline Hardening Rules

1. Never echo secrets in logs — use masking (`::add-mask::` in GitHub Actions).
2. Pin action/image versions by SHA, not mutable tags.
3. Use read-only checkout tokens where possible.
4. Limit who can modify pipeline files (CODEOWNERS, branch protection).
5. Scan pipeline configuration for misconfigurations (Semgrep, actionlint).
6. Use OIDC for cloud credentials instead of long-lived access keys.

## Artifact Management

| Artifact Type | Registry | Versioning |
|--------------|----------|------------|
| Docker images | ECR, Docker Hub, GHCR, Harbor | `git-sha`, `semver`, `latest` |
| npm packages | npm registry, GitHub Packages | semver |
| Python packages | PyPI, private Artifactory | semver |
| Helm charts | OCI registry, ChartMuseum | semver |
| Binaries / JARs | Artifactory, Nexus, S3 | semver + build number |

## Pipeline Metrics to Track

| Metric | Target | Why It Matters |
|--------|--------|---------------|
| Lead time for changes | < 1 day | Speed of delivery |
| Deployment frequency | Multiple per day | Team throughput |
| Change failure rate | < 15% | Quality of releases |
| Mean time to recovery (MTTR) | < 1 hour | Incident response speed |
| Build duration | < 10 minutes | Developer feedback loop |
| Test pass rate | > 98% | Test suite reliability |

## Best Practices

1. **Fail fast** — run fastest checks (lint, unit tests) first.
2. **Parallelize** — run independent stages concurrently.
3. **Immutable artifacts** — build once, deploy the same artifact everywhere.
4. **Environment parity** — staging should mirror production.
5. **Automate everything except production approval** — human gate for prod only.
6. **Cache aggressively** — cache dependencies, Docker layers, and build outputs.

## Using the Reference Files

### When to Read Each Reference

**`/references/fundamentals.md`** — Read when learning CI/CD concepts, understanding pipeline terminology, or setting up your first pipeline from scratch.

**`/references/implementation.md`** — Read when building specific pipeline configurations for GitHub Actions, GitLab CI, or Jenkins, including exact YAML/Groovy examples, caching strategies, and matrix builds.

**`/references/best-practices.md`** — Read when optimizing pipeline performance, implementing advanced deployment strategies (canary, blue-green), establishing security hardening, or designing multi-environment promotion workflows.
