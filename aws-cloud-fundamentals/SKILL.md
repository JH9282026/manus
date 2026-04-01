---
name: aws-cloud-fundamentals
description: "Master Amazon Web Services (AWS) cloud computing fundamentals including core services (EC2, S3, IAM, VPC, RDS, Lambda), cloud service models (IaaS/PaaS/SaaS), security best practices, pricing models, and Infrastructure as Code. Use for: building AWS cloud infrastructure, deploying applications on AWS, managing AWS resources, implementing AWS security, understanding AWS architecture, preparing for AWS certifications, migrating to AWS, or designing cloud-native solutions on Amazon's platform."
---

# AWS Cloud Fundamentals

Master Amazon Web Services core infrastructure, services, security, and best practices for building scalable cloud applications.

## Overview

AWS is the world's leading cloud computing platform with over 200 services spanning compute, storage, databases, networking, security, and more. This skill covers the foundational services and concepts needed to build, deploy, and manage applications on AWS, including EC2 virtual machines, S3 object storage, IAM security, VPC networking, and serverless computing with Lambda.

## Core AWS Services

### Compute Services

| Service | Use Case | Key Features |
|---------|----------|-------------|
| **EC2** | Virtual servers for any workload | Resizable instances, multiple OS options, pay-as-you-go |
| **Lambda** | Serverless code execution | Event-driven, auto-scaling, pay per execution |
| **Elastic Beanstalk** | Platform for web apps | Automatic deployment, scaling, monitoring |
| **ECS/EKS** | Container orchestration | Docker support, Kubernetes integration |

### Storage Services

| Service | Use Case | Durability |
|---------|----------|------------|
| **S3** | Object storage for files, backups, static sites | 99.999999999% (11 nines) |
| **EBS** | Block storage for EC2 instances | Persistent, high-performance |
| **EFS** | Shared file storage | Elastic, scalable, NFS-compatible |
| **Glacier** | Long-term archival | Low-cost, retrieval delays |

### Database Services

| Service | Type | Best For |
|---------|------|----------|
| **RDS** | Relational (MySQL, PostgreSQL, etc.) | Traditional applications, ACID compliance |
| **DynamoDB** | NoSQL key-value | High-scale, low-latency applications |
| **Aurora** | Relational (MySQL/PostgreSQL compatible) | High performance, auto-scaling |
| **ElastiCache** | In-memory (Redis, Memcached) | Caching, session management |

### Networking Services

**VPC (Virtual Private Cloud)**: Isolated network environment where all AWS resources run. Define subnets, route tables, internet gateways, and security rules.

**Key Components**:
- **Subnets**: Public (internet-accessible) and private (internal only)
- **Security Groups**: Stateful firewalls for instances
- **Network ACLs**: Stateless firewalls for subnets
- **Internet Gateway**: Enables internet access
- **NAT Gateway**: Allows private subnets to access internet

### Security and Identity

**IAM (Identity and Access Management)**: Control who can access what in your AWS account.

**Core Concepts**:
- **Users**: Individual accounts for people
- **Groups**: Collections of users with shared permissions
- **Roles**: Temporary credentials for services or federated users
- **Policies**: JSON documents defining permissions

**Best Practices**:
- Enable MFA on root and admin accounts
- Use least privilege principle
- Create individual IAM users (never share credentials)
- Rotate credentials regularly
- Use roles for EC2 instances and Lambda functions

## Cloud Service Models

### IaaS (Infrastructure as a Service)
**Example**: EC2
- AWS provides: Virtual machines, networking, storage
- You manage: Operating system, applications, data
- Use when: You need full control over infrastructure

### PaaS (Platform as a Service)
**Example**: Elastic Beanstalk, App Runner
- AWS provides: Infrastructure, runtime, scaling
- You manage: Application code, configuration
- Use when: You want to focus on code, not infrastructure

### SaaS (Software as a Service)
**Example**: WorkMail, Chime
- AWS provides: Fully managed application
- You manage: User access, data
- Use when: You need ready-to-use applications

## AWS Pricing and Cost Management

### Pricing Model
- **Pay-as-you-go**: No upfront costs, pay only for what you use
- **Compute**: Charged per hour/second of instance runtime
- **Storage**: Charged per GB stored per month
- **Data Transfer**: Ingress free, egress charged after free tier

### Free Tier
**12 months** for new accounts:
- 750 hours/month of t2.micro or t3.micro EC2
- 5 GB S3 storage
- 750 hours/month of RDS db.t2.micro
- 1 million Lambda requests/month

### Cost Optimization
- Set up billing alerts via CloudWatch
- Use Reserved Instances for predictable workloads (up to 75% savings)
- Use Spot Instances for fault-tolerant workloads (up to 90% savings)
- Right-size instances based on actual usage
- Delete unused resources (EBS volumes, snapshots, Elastic IPs)

## Security Best Practices

### Account Security
1. **Secure Root Account**: Enable MFA, don't use for daily operations
2. **Create Admin IAM User**: Use for administrative tasks with MFA enabled
3. **Enable CloudTrail**: Log all API calls for auditing
4. **Enable AWS Config**: Track resource configuration changes
5. **Set Billing Alerts**: Prevent unexpected charges

### Resource Security
1. **Encrypt Data**: Use encryption at rest (KMS) and in transit (TLS/SSL)
2. **Network Segmentation**: Use VPCs, security groups, and NACLs
3. **Least Privilege**: Grant minimum necessary permissions
4. **Regular Audits**: Review IAM policies, security groups, and access logs
5. **Patch Management**: Keep OS and applications updated

## Infrastructure as Code

### AWS CloudFormation
Define infrastructure using YAML or JSON templates:
- **Stacks**: Manage resources as a single unit
- **Templates**: Reusable infrastructure definitions
- **Change Sets**: Preview changes before applying
- **Drift Detection**: Identify manual changes

### AWS CDK (Cloud Development Kit)
Define infrastructure using programming languages (TypeScript, Python, Java):
- Higher-level abstractions than CloudFormation
- Synthesizes to CloudFormation templates
- Better for complex, dynamic infrastructure

## AWS CLI and Automation

The AWS CLI enables command-line management of all AWS services:

```bash
# Configure credentials
aws configure

# List EC2 instances
aws ec2 describe-instances

# Upload to S3
aws s3 cp file.txt s3://my-bucket/

# Create IAM user
aws iam create-user --user-name john
```

**Use for**: Automation, scripting, CI/CD pipelines, faster operations than console.

## Common Architecture Patterns

### Three-Tier Web Application
- **Presentation**: CloudFront + S3 (static content)
- **Application**: EC2/ECS in Auto Scaling Group behind ALB
- **Data**: RDS Multi-AZ with read replicas

### Serverless Application
- **API**: API Gateway + Lambda
- **Storage**: DynamoDB + S3
- **Authentication**: Cognito
- **Monitoring**: CloudWatch

### Hybrid Cloud
- **Connectivity**: VPN or Direct Connect
- **Storage**: Storage Gateway
- **Compute**: Outposts for on-premises AWS

## Monitoring and Logging

### CloudWatch
- **Metrics**: Monitor resource performance (CPU, memory, disk)
- **Logs**: Centralized log aggregation
- **Alarms**: Trigger notifications or auto-scaling
- **Dashboards**: Visualize metrics

### CloudTrail
- **API Logging**: Record all AWS API calls
- **Compliance**: Meet audit requirements
- **Security Analysis**: Detect unauthorized access

## Global Infrastructure

### Regions and Availability Zones
- **Regions**: Geographic locations (e.g., us-east-1, eu-west-1)
- **Availability Zones**: Isolated data centers within a region (typically 3+ per region)
- **Edge Locations**: CDN endpoints for CloudFront (200+ globally)

**Design for High Availability**: Deploy across multiple AZs, use Multi-AZ RDS, implement auto-scaling.

## Using the Reference Files

### When to Read Each Reference

**`/references/ec2-deep-dive.md`** — Read when launching EC2 instances, selecting instance types, configuring storage, or implementing auto-scaling.

**`/references/s3-storage-guide.md`** — Read when working with S3 buckets, implementing lifecycle policies, configuring static website hosting, or optimizing storage costs.

**`/references/iam-security-guide.md`** — Read when creating IAM policies, implementing least privilege access, setting up cross-account access, or troubleshooting permissions.

**`/references/vpc-networking-guide.md`** — Read when designing VPC architecture, configuring subnets and route tables, implementing network security, or connecting to on-premises networks.

**`/references/serverless-patterns.md`** — Read when building serverless applications with Lambda, API Gateway, and DynamoDB, or implementing event-driven architectures.

**`/references/cost-optimization-strategies.md`** — Read when analyzing AWS bills, implementing cost controls, selecting pricing models, or optimizing resource usage.
