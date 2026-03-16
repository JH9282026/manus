---
name: backend-api-development
description: "Build robust REST and GraphQL APIs with best practices for backend development. Use for: designing API contracts, implementing RESTful services, building GraphQL schemas and resolvers, choosing between REST and GraphQL architectures, creating hybrid API systems, implementing API versioning, handling error responses, optimizing API performance, and ensuring production-ready backend services."
---

# Backend API Development

Build production-ready REST and GraphQL APIs following modern best practices and architectural patterns.

## Overview

This skill provides comprehensive guidance for backend API development, covering both REST and GraphQL architectures. Learn to design API contracts, implement robust endpoints, handle authentication and rate limiting, and deploy scalable backend services. Includes framework selection, security patterns, and performance optimization strategies.

## API Architecture Selection

| Use Case | Architecture | When to Use |
|----------|-------------|-------------|
| Simple CRUD operations | REST | Stable data models, public APIs, browser-friendly endpoints |
| Complex data requirements | GraphQL | Mobile apps, dashboards, varying client needs, multiple data sources |
| Internal microservices | REST + gRPC | High-performance service-to-service communication |
| Real-time updates | GraphQL Subscriptions + WebSockets | Live data feeds, chat, notifications |
| Hybrid systems | REST + GraphQL | REST for internal wiring, GraphQL for client flexibility |

**Key Statistics (2026):**
- 93% of teams use REST for core services
- 50-60% enterprise adoption of GraphQL
- Hybrid architectures report highest satisfaction

## REST API Best Practices

### Resource Design
- Use nouns for paths (`/devices`, `/users`) not verbs (`/createDevice`)
- Group endpoints by resource, not by client
- Implement proper HTTP methods (GET, POST, PUT, PATCH, DELETE)
- Use plural nouns for collections (`/users` not `/user`)

### Response Structure
```json
{
  "data": { /* resource data */ },
  "meta": { "page": 1, "total": 100 },
  "errors": []
}
```

### Status Codes
- 200: Success
- 201: Created
- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Not Found
- 429: Rate Limited
- 500: Server Error

## GraphQL Best Practices

### Schema Design
- Model business domain as a graph
- Use strong typing for all fields
- Design schema before implementation
- Align with business logic and legacy systems

### Query Optimization
- Implement DataLoader for batching
- Use pagination for large datasets
- Limit query depth to prevent abuse
- Provide object identifiers for caching

### Error Handling
GraphQL's strong typing provides automatic error identification with useful messages. Structure errors consistently.

## Technology Stack Recommendations

### Python Backend
- **FastAPI**: Async/OpenAPI-first, 10,000+ req/sec
- **Strawberry**: Modern GraphQL for Python
- **Pydantic**: Data validation and modeling
- **PostgreSQL**: Production database
- **Redis**: Caching and sessions

### Node.js Backend
- **Express**: Mature REST framework
- **Apollo Server**: GraphQL implementation
- **Prisma**: Type-safe ORM
- **PostgreSQL/MongoDB**: Database options

## API-First Design Process

1. **Define Contract**: Specify resources, paths, permissions before coding
2. **Use OpenAPI/GraphQL Schema**: Document API structure
3. **Generate Documentation**: Auto-generate interactive docs
4. **Mock Endpoints**: Test client integration early
5. **Implement**: Build against defined contract

## Security Essentials

- Implement JWT authentication
- Add object-level authorization (prevent BOLA)
- Use machine-readable rate limits
- Validate all input data
- Sanitize error messages (no stack traces in production)
- Enable CORS properly
- Use HTTPS/TLS for all endpoints

## Production Readiness Checklist

- [ ] CI/CD pipeline configured
- [ ] Containerization (Docker)
- [ ] Comprehensive testing (unit, integration, e2e)
- [ ] Logging and monitoring (observability)
- [ ] Database migrations automated
- [ ] Rate limiting implemented
- [ ] API documentation generated
- [ ] Health check endpoints
- [ ] Graceful shutdown handling

## Performance Optimization

- Use async/await for I/O operations
- Implement connection pooling
- Cache frequent queries (Redis)
- Use database indexes strategically
- Implement pagination for large datasets
- Compress responses (GZip)
- Use CDN for static assets

## Using the Reference Files

**`/references/rest-api-patterns.md`** — Read when designing RESTful endpoints, implementing HTTP methods, structuring responses, or handling versioning.

**`/references/graphql-implementation.md`** — Read when building GraphQL schemas, implementing resolvers, optimizing queries, or handling subscriptions.

**`/references/api-security-patterns.md`** — Read when implementing authentication, authorization, rate limiting, or securing API endpoints.

**`/references/testing-deployment.md`** — Read when setting up testing frameworks, CI/CD pipelines, containerization, or production deployment strategies.
