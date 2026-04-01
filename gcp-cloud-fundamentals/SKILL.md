---
name: gcp-cloud-fundamentals
description: "Master Google Cloud Platform (GCP) fundamentals including core services (Compute Engine, Cloud Storage, Cloud SQL, VPC), resource management, security with IAM, pricing models, and Infrastructure as Code with Deployment Manager and Terraform. Use for: building GCP infrastructure, deploying applications on Google Cloud, managing GCP resources, implementing GCP security, understanding GCP architecture, preparing for GCP certifications, migrating to GCP, or designing cloud-native solutions on Google's platform."
---

# GCP Cloud Fundamentals

Master Google Cloud Platform core infrastructure, services, security, and best practices.

## Overview

Google Cloud Platform (GCP) offers 100+ services for compute, storage, databases, networking, machine learning, and more. This skill covers foundational GCP services including Compute Engine, Cloud Storage, Cloud SQL, VPC networking, and IAM security needed to build and deploy applications on Google's global infrastructure.

## Core GCP Services

### Compute Services

| Service | Type | Use Case |
|---------|------|----------|
| **Compute Engine** | IaaS VMs | Custom workloads, full control |
| **App Engine** | PaaS | Web apps, auto-scaling |
| **Cloud Functions** | Serverless | Event-driven, microservices |
| **Cloud Run** | Serverless containers | Containerized apps, auto-scaling |
| **Google Kubernetes Engine (GKE)** | Managed Kubernetes | Container orchestration |

### Storage Services

| Service | Type | Best For |
|---------|------|----------|
| **Cloud Storage** | Object storage | Files, backups, static content |
| **Persistent Disk** | Block storage | VM disks |
| **Filestore** | NFS file storage | Shared file access |
| **Cloud SQL** | Managed relational DB | MySQL, PostgreSQL, SQL Server |
| **Cloud Spanner** | Globally distributed DB | Global consistency, high availability |
| **Bigtable** | NoSQL wide-column | Large analytical workloads |
| **Firestore** | NoSQL document DB | Mobile/web apps, real-time sync |

### Networking

**VPC (Virtual Private Cloud)**: Isolated network for GCP resources

**Key Components**:
- **Subnets**: Regional, can span zones
- **Firewall Rules**: Allow/deny traffic
- **Cloud Load Balancing**: Global and regional load balancers
- **Cloud CDN**: Content delivery network
- **Cloud VPN**: Secure connectivity to on-premises
- **Cloud Interconnect**: Dedicated connectivity

## GCP Resource Hierarchy

```
Organization
  └── Folders
      └── Projects
          └── Resources
```

**Projects**: Fundamental organizing entity, billing boundary

**Folders**: Group projects, apply policies

**Organization**: Root node, company-wide policies

## IAM and Security

### Identity and Access Management

**Principals**: Who (user, service account, group)

**Roles**: What permissions
- **Primitive roles**: Owner, Editor, Viewer (broad)
- **Predefined roles**: Service-specific (recommended)
- **Custom roles**: Fine-grained permissions

**Resources**: Which resources

**Policy**: Binds principals to roles on resources

### Service Accounts

**Purpose**: Identity for applications and VMs

**Types**:
- **User-managed**: You create and manage
- **Default**: Auto-created for services
- **Google-managed**: Used by Google services

**Best practices**:
- Use service accounts for applications
- Grant minimum necessary permissions
- Rotate keys regularly
- Use Workload Identity for GKE

## Compute Engine

### VM Instances

**Machine Types**:
- **General-purpose**: E2, N1, N2, N2D
- **Compute-optimized**: C2, C2D
- **Memory-optimized**: M1, M2, M3
- **Accelerator-optimized**: A2 (GPUs)

**Pricing**:
- **On-demand**: Pay per second
- **Preemptible**: Up to 80% discount, can be terminated
- **Committed use**: 1 or 3 years, up to 57% discount
- **Sustained use**: Automatic discounts for running VMs

### Instance Management

**Startup scripts**: Automate configuration

**Instance templates**: Reusable VM configurations

**Instance groups**:
- **Managed**: Auto-scaling, auto-healing
- **Unmanaged**: Manual management

## Cloud Storage

### Storage Classes

| Class | Use Case | Availability | Min Storage |
|-------|----------|--------------|-------------|
| **Standard** | Frequently accessed | >99.99% | None |
| **Nearline** | Once per month | 99.95% | 30 days |
| **Coldline** | Once per quarter | 99.95% | 90 days |
| **Archive** | Once per year | 99.95% | 365 days |

### Lifecycle Management

**Automate transitions and deletions**:
- Move to Nearline after 30 days
- Move to Coldline after 90 days
- Move to Archive after 365 days
- Delete after specified time

### Access Control

**Uniform bucket-level access**: IAM only (recommended)

**Fine-grained access**: IAM + ACLs

**Signed URLs**: Time-limited access without credentials

## Pricing and Cost Management

### Cost Optimization

**Committed use discounts**: 1 or 3 years, up to 57% savings

**Sustained use discounts**: Automatic for running VMs

**Preemptible VMs**: Up to 80% discount

**Rightsizing recommendations**: GCP suggests optimal VM sizes

**Budget alerts**: Set thresholds, get notifications

## Infrastructure as Code

### Deployment Manager

**YAML or Python templates**:
```yaml
resources:
- name: my-vm
  type: compute.v1.instance
  properties:
    zone: us-central1-a
    machineType: zones/us-central1-a/machineTypes/n1-standard-1
```

### Terraform

**GCP provider**:
```hcl
resource "google_compute_instance" "default" {
  name         = "my-vm"
  machine_type = "n1-standard-1"
  zone         = "us-central1-a"
}
```

## Monitoring and Logging

### Cloud Monitoring

**Metrics**: CPU, memory, disk, network

**Dashboards**: Visualize metrics

**Alerts**: Proactive notifications

**Uptime checks**: Monitor endpoint availability

### Cloud Logging

**Centralized logging**: All GCP services

**Log Explorer**: Query and analyze logs

**Log-based metrics**: Create metrics from logs

**Log sinks**: Export to BigQuery, Cloud Storage, Pub/Sub

## Using the Reference Files

**`/references/compute-engine-guide.md`** — Read when deploying VMs, configuring instance groups, or implementing auto-scaling.

**`/references/cloud-storage-guide.md`** — Read when working with Cloud Storage buckets, implementing lifecycle policies, or optimizing storage costs.

**`/references/networking-guide.md`** — Read when designing VPC architecture, configuring firewall rules, or implementing load balancing.

**`/references/iam-security-guide.md`** — Read when implementing IAM policies, managing service accounts, or securing GCP resources.
