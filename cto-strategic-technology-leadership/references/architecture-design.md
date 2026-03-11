# Architecture Design

Enterprise architecture, cloud strategy, and platform design.

---

## Enterprise Architecture Layers

### TOGAF Framework
1. **Business Architecture**: Processes, organization
2. **Data Architecture**: Data models, flows
3. **Application Architecture**: Systems, integrations
4. **Technology Architecture**: Infrastructure, platforms

### Architecture Principles
- Business-driven, not technology-driven
- Reuse before buy before build
- API-first integration
- Security by design
- Cloud-native when possible

---

## Cloud Strategy

### Cloud Models
| Model | Use Case |
|-------|----------|
| IaaS | Lift-and-shift, flexibility |
| PaaS | Application development |
| SaaS | Commodity functions |
| Serverless | Event-driven, variable load |

### Multi-Cloud Considerations
- Avoid vendor lock-in
- Best-of-breed services
- Complexity management
- Cost optimization
- Skills requirements

### Migration Approaches
| Strategy | Description | When to Use |
|----------|-------------|-------------|
| Rehost | Lift-and-shift | Quick migration |
| Replatform | Minor optimization | PaaS benefits |
| Refactor | Rebuild cloud-native | Strategic apps |
| Replace | SaaS adoption | Commodity functions |
| Retire | Decommission | Obsolete systems |

---

## Modern Application Architecture

### Microservices
- Independent deployment
- Domain-driven design
- API-based communication
- Polyglot persistence

### Event-Driven
- Loose coupling
- Async processing
- Scalability
- Event sourcing

---

## Integration Patterns

### API Strategy
- API gateway for external
- Service mesh for internal
- GraphQL for flexible queries
- REST for standard CRUD
- gRPC for performance

### Data Integration
- Event streaming (Kafka)
- ETL/ELT pipelines
- API-based real-time
- CDC for databases
