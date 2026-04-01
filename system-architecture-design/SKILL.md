---
name: system-architecture-design
description: "System Architecture Design is an advanced technical skill that creates comprehensive architectural blueprints for software systems."
---

# System Architecture Design

## Overview

This skill provides comprehensive guidance and best practices for this domain.

## 1. Skill Description and Purpose

System Architecture Design is an advanced technical skill that creates comprehensive architectural blueprints for software systems. This skill translates business requirements and technical constraints into scalable, maintainable, and secure system designs that guide development teams and align technical stakeholders.

### Core Capabilities

The skill performs requirements analysis for architectural decisions, designs component structures and communication patterns, selects appropriate technology stacks, defines scalability and reliability strategies, documents API contracts and data flows, creates deployment architectures, and produces Architecture Decision Records (ADRs) that capture design rationale.

### Design Functions

- **Structural Design**: Component decomposition, service boundaries, module organization
- **Behavioral Design**: Communication patterns, event flows, state management
- **Integration Design**: API contracts, message protocols, data exchange patterns
- **Infrastructure Design**: Deployment topology, networking, resource allocation
- **Security Architecture**: Authentication, authorization, data protection, threat modeling
- **Scalability Planning**: Horizontal/vertical scaling, load balancing, caching strategies

### When to Use This Skill

Deploy this skill when organizations need to:
- Design new systems or major platform components
- Modernize legacy systems with contemporary architectures
- Plan microservices decomposition strategies
- Design cloud migration architectures
- Create integration architectures for enterprise systems
- Document existing system architectures
- Evaluate architecture alternatives for technical decisions

### Value Proposition

This skill produces consistent, professional architectural documentation, ensures comprehensive coverage of architectural concerns, accelerates design cycles through pattern application, and improves system quality through early identification of technical risks.

## 2. Required Inputs/Parameters

### Mandatory Inputs

| Parameter | Format | Description |
|-----------|--------|-------------|
| `requirements` | Document | Functional and non-functional requirements (PRD, user stories) |
| `system_context` | Enum | "greenfield", "brownfield", "migration", "integration" |
| `architecture_scope` | Enum | "full_system", "subsystem", "component", "integration" |
| `quality_attributes` | Array | Priority NFRs (e.g., ["scalability", "security", "availability"]) |

### Conditional Inputs

| Parameter | Required When | Format | Description |
|-----------|---------------|--------|-------------|
| `existing_architecture` | Brownfield/Migration | Document/Diagrams | Current system architecture documentation |
| `integration_endpoints` | Integration | Array | External systems and their API specifications |
| `compliance_requirements` | Regulated systems | Document | Security and compliance frameworks (SOC2, HIPAA, PCI) |
| `technology_constraints` | Any | Array | Mandated technologies or exclusions |

### Optional Inputs

| Parameter | Format | Description |
|-----------|--------|-------------|
| `load_projections` | Object | Expected traffic, data volumes, growth rates |
| `team_capabilities` | Array | Team technology expertise for stack selection |
| `budget_constraints` | Object | Infrastructure and licensing budget limitations |
| `timeline` | Object | Development timeline affecting build vs. buy decisions |
| `deployment_environment` | Enum | "cloud_native", "hybrid", "on_premises" |
| `disaster_recovery_requirements` | Object | RTO, RPO, geographic redundancy needs |

## 3. Expected Outputs/Deliverables

### Primary Deliverables

**Architecture Overview Document (PDF/DOCX)**
- Executive summary and design principles
- System context diagram (C4 Level 0)
- Container diagram (C4 Level 1)
- Component diagrams (C4 Level 2)
- Technology stack selection with rationale
- Quality attribute strategies
- Key architectural decisions summary
- Risk assessment and mitigation strategies

**Technical Architecture Specification (Markdown/Wiki)**
- Detailed component specifications
- API contracts (OpenAPI/AsyncAPI)
- Data architecture and schema designs
- Security architecture and threat model
- Integration patterns and protocols
- Error handling and resilience patterns
- Logging, monitoring, and observability design

**Architecture Decision Records (Markdown)**
- ADRs for each significant decision
- Context, decision, consequences structure
- Alternatives considered with trade-off analysis
- Links to supporting research

**Infrastructure Architecture (Diagrams + Terraform/CloudFormation)**
- Cloud resource topology
- Networking and security groups
- Auto-scaling configurations
- Database and storage architecture
- CI/CD pipeline architecture
- Infrastructure as code templates

**Sequence and Flow Diagrams (PlantUML/Mermaid)**
- Critical path sequence diagrams
- Data flow diagrams
- State machine diagrams
- Event flow diagrams

### Quality Standards

- All diagrams must follow C4 model or equivalent standard notation
- API specifications must be machine-readable (OpenAPI 3.0+)
- ADRs must include alternatives considered
- Security architecture must address OWASP Top 10
- Scalability design must include capacity calculations
- All technology selections must include rationale

## 4. Example Use Cases

### Use Case 1: E-commerce Platform Architecture

A retail company needs architecture for a new e-commerce platform handling 10M daily active users. The skill designs a microservices architecture with event-driven order processing, distributed caching strategy, multi-region deployment for global availability, and integration patterns for payment processors and inventory systems.

### Use Case 2: Legacy Modernization Architecture

An insurance company needs to modernize a monolithic claims processing system. The skill designs a strangler fig migration strategy, identifies service boundaries using domain-driven design, creates API gateway architecture for legacy integration, and defines data migration patterns maintaining business continuity.

### Use Case 3: Real-time Analytics Platform

A fintech company needs architecture for real-time fraud detection. The skill designs stream processing architecture using Kafka and Flink, defines feature store architecture for ML models, creates low-latency scoring service design, and specifies observability architecture for system monitoring.

### Use Case 4: Multi-tenant SaaS Architecture

A B2B SaaS startup needs architecture supporting multi-tenancy. The skill designs tenant isolation strategies, database sharding approaches, resource allocation and throttling mechanisms, and white-label customization architecture.

### Use Case 5: IoT Platform Architecture

A manufacturing company needs architecture for industrial IoT platform. The skill designs edge computing architecture, time-series data ingestion patterns, device management and OTA update systems, and analytics pipeline architecture.

## 5. Prerequisites or Dependencies

### Required Access and Permissions

- Complete requirements documentation
- Existing system documentation (if applicable)
- Infrastructure access for current-state analysis
- Stakeholder access for clarification

### Tool Dependencies

- Diagramming tools (Draw.io, Lucidchart, Excalidraw)
- API specification tools (Swagger Editor, Stoplight)
- Infrastructure design tools (Cloudcraft, AWS Architecture Tool)
- Documentation platforms (Confluence, Notion)
- Version control for architecture artifacts

### Domain Knowledge Requirements

- Distributed systems patterns and anti-patterns
- Cloud platform services (AWS, GCP, Azure)
- Database technologies (SQL, NoSQL, time-series)
- Message queue and event streaming systems
- Container orchestration (Kubernetes)
- Security architecture frameworks

### Collaboration Requirements

- Engineering leadership review
- Security team threat model review
- Infrastructure/DevOps validation
- Product alignment on trade-offs
- Cross-team dependency coordination

### Limitations and Constraints

- Architecture designs require engineering validation
- Cost estimates require pricing verification
- Performance projections require load testing validation
- Security assessments may require penetration testing
- Capacity planning requires real usage data for accuracy

## Using the Reference Files

- [01 Fundamentals Of System Architecture](./references/01-fundamentals-of-system-architecture.md): 01 Fundamentals Of System Architecture
- [02 Microservices Design Patterns](./references/02-microservices-design-patterns.md): 02 Microservices Design Patterns
- [03 Cloud Native Architecture](./references/03-cloud-native-architecture.md): 03 Cloud Native Architecture
- [04 Enterprise Integration Patterns](./references/04-enterprise-integration-patterns.md): 04 Enterprise Integration Patterns
