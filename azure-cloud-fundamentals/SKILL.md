---
name: azure-cloud-fundamentals
description: "Master Microsoft Azure cloud computing fundamentals including core services (Virtual Machines, Storage, Networking, Azure AD), resource management, security, pricing models, and Infrastructure as Code with ARM templates and Bicep. Use for: building Azure cloud infrastructure, deploying applications on Azure, managing Azure resources, implementing Azure security, understanding Azure architecture, preparing for Azure certifications, migrating to Azure, or designing cloud-native solutions on Microsoft's platform."
---

# Azure Cloud Fundamentals

Master Microsoft Azure core infrastructure, services, security, and best practices for building scalable cloud applications.

## Overview

Microsoft Azure is a comprehensive cloud computing platform offering 200+ services across compute, storage, databases, networking, AI, and more. This skill covers foundational Azure services and concepts needed to build, deploy, and manage applications, including Virtual Machines, Storage Accounts, Virtual Networks, Azure Active Directory, and serverless computing with Azure Functions.

## Core Azure Services

### Compute Services

| Service | Use Case | Key Features |
|---------|----------|-------------|
| **Virtual Machines** | IaaS compute for any workload | Windows/Linux, flexible sizing, availability sets |
| **App Service** | PaaS for web apps and APIs | Auto-scaling, CI/CD, multiple languages |
| **Azure Functions** | Serverless compute | Event-driven, consumption-based pricing |
| **Azure Kubernetes Service (AKS)** | Managed Kubernetes | Container orchestration, integrated monitoring |
| **Container Instances** | Serverless containers | Fast startup, per-second billing |

### Storage Services

| Service | Type | Best For |
|---------|------|----------|
| **Blob Storage** | Object storage | Unstructured data, backups, media files |
| **File Storage** | SMB file shares | Lift-and-shift, shared storage |
| **Queue Storage** | Message queuing | Asynchronous communication |
| **Table Storage** | NoSQL key-value | Structured non-relational data |
| **Disk Storage** | Block storage for VMs | Managed disks, snapshots |

### Database Services

| Service | Type | Best For |
|---------|------|----------|
| **Azure SQL Database** | Relational (SQL Server) | Enterprise applications, ACID compliance |
| **Cosmos DB** | Multi-model NoSQL | Global distribution, low latency |
| **Database for MySQL/PostgreSQL** | Managed open-source | Familiar database engines |
| **Azure Cache for Redis** | In-memory cache | Session state, caching |

### Networking Services

**Virtual Network (VNet)**: Isolated network for Azure resources

**Key Components**:
- **Subnets**: Segment VNet into smaller networks
- **Network Security Groups (NSGs)**: Firewall rules for subnets/NICs
- **Load Balancer**: Distribute traffic across VMs
- **Application Gateway**: Layer 7 load balancer with WAF
- **VPN Gateway**: Secure site-to-site and point-to-site connections
- **ExpressRoute**: Private connection to Azure

### Identity and Security

**Azure Active Directory (Azure AD)**: Cloud-based identity and access management

**Core Features**:
- Single Sign-On (SSO)
- Multi-Factor Authentication (MFA)
- Conditional Access policies
- Role-Based Access Control (RBAC)
- B2B and B2C identity management

**Security Services**:
- **Azure Security Center**: Unified security management
- **Azure Sentinel**: Cloud-native SIEM
- **Key Vault**: Secrets and key management
- **Azure DDoS Protection**: Network protection
- **Azure Firewall**: Managed network security

## Azure Resource Management

### Resource Organization

**Hierarchy**:
```
Management Groups
  └── Subscriptions
      └── Resource Groups
          └── Resources
```

**Resource Groups**:
- Logical containers for resources
- Share same lifecycle
- Apply policies and RBAC at group level
- Resources can only be in one group

**Subscriptions**:
- Billing boundary
- Access control boundary
- Can have multiple subscriptions per organization

**Management Groups**:
- Organize multiple subscriptions
- Apply policies across subscriptions
- Enterprise-scale governance

### Azure Resource Manager (ARM)

**Benefits**:
- Declarative templates (JSON)
- Consistent management layer
- Dependency management
- Tag-based organization
- RBAC integration

**ARM Template Structure**:
```json
{
  "$schema": "...",
  "contentVersion": "1.0.0.0",
  "parameters": {},
  "variables": {},
  "resources": [],
  "outputs": {}
}
```

## Pricing and Cost Management

### Pricing Models

**Pay-As-You-Go**: No upfront cost, pay for what you use

**Reserved Instances**: 1-year or 3-year commitment, up to 72% savings

**Spot VMs**: Unused capacity at discounted rates, can be evicted

**Azure Hybrid Benefit**: Use existing Windows/SQL licenses on Azure

### Cost Management Tools

**Azure Cost Management + Billing**:
- Cost analysis and reporting
- Budgets and alerts
- Cost allocation by tags
- Recommendations for optimization

**Azure Advisor**:
- Personalized best practices
- Cost, security, reliability, performance recommendations
- Free service

**Pricing Calculator**: Estimate costs before deployment

## Security Best Practices

### Identity Security

1. **Enable MFA**: For all users, especially admins
2. **Use Azure AD**: Centralized identity management
3. **Implement Conditional Access**: Context-aware access policies
4. **Use Managed Identities**: Eliminate credentials in code
5. **Apply Least Privilege**: RBAC with minimum permissions

### Network Security

1. **Use NSGs**: Control inbound/outbound traffic
2. **Implement Azure Firewall**: Centralized network security
3. **Enable DDoS Protection**: Protect against attacks
4. **Use Private Endpoints**: Keep traffic on Azure backbone
5. **Segment Networks**: Isolate workloads with subnets

### Data Security

1. **Encrypt at Rest**: Use Azure Storage Service Encryption
2. **Encrypt in Transit**: Use TLS/SSL for all connections
3. **Use Key Vault**: Manage secrets, keys, certificates
4. **Enable Soft Delete**: Protect against accidental deletion
5. **Implement Backup**: Azure Backup for VMs and data

## Infrastructure as Code

### ARM Templates

**Deployment**:
```bash
az deployment group create \
  --resource-group myResourceGroup \
  --template-file template.json \
  --parameters parameters.json
```

**Best Practices**:
- Use parameters for reusability
- Modularize with linked templates
- Version control templates
- Use Azure DevOps or GitHub Actions for CI/CD

### Bicep

**Modern alternative to ARM templates**:
- Simpler syntax
- Better tooling support
- Compiles to ARM templates
- Type safety and IntelliSense

**Example**:
```bicep
param location string = resourceGroup().location
param vmName string

resource vm 'Microsoft.Compute/virtualMachines@2021-03-01' = {
  name: vmName
  location: location
  properties: {
    // VM configuration
  }
}
```

## Monitoring and Management

### Azure Monitor

**Components**:
- **Metrics**: Numerical time-series data
- **Logs**: Text-based log data
- **Application Insights**: Application performance monitoring
- **Alerts**: Proactive notifications
- **Dashboards**: Visualize metrics and logs

**Log Analytics**:
- Query logs with Kusto Query Language (KQL)
- Centralized log storage
- Integration with Azure Sentinel

### Azure Automation

**Use Cases**:
- Start/stop VMs on schedule
- Update management
- Configuration management
- Process automation

**Runbooks**: PowerShell or Python scripts for automation

## High Availability and Disaster Recovery

### Availability Options

**Availability Sets**:
- Protect against hardware failures
- 99.95% SLA
- Fault domains and update domains

**Availability Zones**:
- Physically separate datacenters
- 99.99% SLA
- Zone-redundant services

**Region Pairs**:
- Paired regions for disaster recovery
- Automatic replication for some services
- Planned updates staggered

### Backup and Recovery

**Azure Backup**:
- VM backups
- SQL Server backups
- File and folder backups
- Long-term retention

**Azure Site Recovery**:
- Disaster recovery as a service
- Replicate VMs to secondary region
- Orchestrated failover and failback

## Using the Reference Files

### When to Read Each Reference

**`/references/virtual-machines-guide.md`** — Read when deploying VMs, selecting VM sizes, configuring availability, or implementing auto-scaling.

**`/references/storage-accounts-guide.md`** — Read when working with Blob, File, Queue, or Table storage, implementing lifecycle policies, or optimizing storage costs.

**`/references/networking-guide.md`** — Read when designing VNet architecture, configuring NSGs, implementing load balancing, or setting up hybrid connectivity.

**`/references/azure-ad-security.md`** — Read when implementing identity management, configuring RBAC, setting up Conditional Access, or managing application identities.
