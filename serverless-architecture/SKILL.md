---
name: serverless-architecture
description: "Design and implement serverless architectures using AWS Lambda, Azure Functions, Google Cloud Functions, and event-driven patterns including API Gateway integration, function composition, cold start optimization, cost modeling, and observability. Use for: building event-driven applications, designing serverless APIs, implementing function orchestration with Step Functions, optimizing cold starts, managing serverless deployments with SAM/Serverless Framework, and architecting cost-effective serverless solutions."
---

# Serverless Architecture

Design and implement event-driven serverless applications using managed compute and integration services.

## Overview

This skill covers serverless architecture patterns — from choosing the right compute service through designing event-driven workflows, managing cold starts, composing functions, and operating serverless applications in production. It focuses on practical design decisions and trade-offs rather than basic function syntax.

## Serverless Compute Platform Comparison

| Feature | AWS Lambda | Azure Functions | Google Cloud Functions | CloudFlare Workers |
|---------|-----------|----------------|----------------------|--------------------|
| Max execution time | 15 min | 10 min (Consumption), unlimited (Premium) | 9 min (1st gen), 60 min (2nd gen) | 30s (free), 15 min (paid) |
| Memory range | 128 MB – 10 GB | 1.5 GB (Consumption), 14 GB (Premium) | 128 MB – 32 GB | 128 MB |
| Max package size | 250 MB (unzipped), 50 MB (zipped) | No hard limit | 100 MB (1st gen), 32 GB (2nd gen with Artifact Registry) | 10 MB |
| Languages | Python, Node, Java, Go, .NET, Ruby, custom | C#, JS, Python, Java, PowerShell | Node, Python, Go, Java, .NET, Ruby, PHP | JS/TS, Wasm |
| Pricing model | Per request + per GB-second | Per execution + per GB-second | Per invocation + per GB-second | Per request (bundled model) |
| Cold start (typical) | 100ms–2s (managed), ~1s (SnapStart Java) | 1–5s (Consumption), <1s (Premium) | 100ms–2s | <5ms (V8 isolate) |
| Concurrency limit | 1000 default (adjustable) | 200 per instance (Consumption) | 1000 default | Unlimited practical |
| VPC support | Yes (ENI attach) | Yes (VNet integration) | Yes (VPC connector) | No (edge-based) |

## Serverless Architecture Patterns

| Pattern | Description | Use When | AWS Services |
|---------|------------|----------|-------------|
| API Backend | Lambda behind API Gateway | REST/GraphQL APIs | API Gateway + Lambda + DynamoDB |
| Event Processing | Functions triggered by events | Async data processing | S3/SQS/SNS → Lambda |
| Scheduled Tasks | Cron-triggered functions | Periodic jobs, reports | EventBridge Scheduler → Lambda |
| Stream Processing | Real-time data transformation | IoT, clickstream, logs | Kinesis / DynamoDB Streams → Lambda |
| Step Functions Orchestration | State machine coordinating functions | Multi-step workflows, retries | Step Functions + Lambda |
| Fan-out / Fan-in | Parallel execution with aggregation | Batch processing, map-reduce | SNS → SQS → Lambda (parallel) |
| Edge Computing | Functions at CDN edge | Low-latency, geo-distributed | Lambda@Edge, CloudFront Functions |
| Event Sourcing | Append-only event log + projections | Audit trails, CQRS | EventBridge + DynamoDB Streams |

## API Gateway + Lambda Design

### API Gateway Selection

| Type | Protocol | Features | Cost | Best For |
|------|----------|----------|------|----------|
| HTTP API (API Gateway v2) | HTTP | Simple routing, JWT auth, CORS | $1.00/million requests | Most REST APIs |
| REST API (API Gateway v1) | HTTP | Full features, WAF, caching, usage plans | $3.50/million requests | Enterprise APIs needing throttling, API keys |
| WebSocket API | WebSocket | Real-time bidirectional | $1.00/million messages | Chat, live updates, dashboards |
| AppSync | GraphQL | Schema-driven, subscriptions, caching | $4.00/million queries | GraphQL APIs, real-time data |
| Function URL | HTTP | Direct Lambda invocation, no gateway | Free (Lambda cost only) | Internal APIs, webhooks |

### Request/Response Design

- Use **proxy integration** for maximum flexibility (Lambda receives full HTTP event).
- Return proper status codes: 200, 201, 400, 401, 403, 404, 500.
- Set CORS headers in Lambda response (or use API Gateway CORS config).
- Implement request validation at the API Gateway level to reject bad requests before Lambda.
- Use Lambda response streaming for large payloads (>6 MB).

## Cold Start Optimization

| Technique | Impact | Trade-Off |
|-----------|--------|-----------|
| Provisioned Concurrency | Eliminates cold starts | Cost ($) — paying for idle compute |
| SnapStart (Java/Lambda) | Reduces Java cold start to ~200ms | Snapshot/restore behavior quirks |
| Smaller package size | Reduces init time | May need code splitting |
| Avoid VPC unless needed | Eliminates ENI attach delay (~1s) | No VPC resource access |
| Keep runtime warm (ping) | Reduces frequency of cold starts | Adds invocation cost, not guaranteed |
| Choose fast runtimes | Python/Node faster cold starts than Java/.NET | Language constraints |
| Lazy initialization | Defers heavy init until needed | First request per path slower |
| Use Lambda Layers | Shared code cached across functions | 5-layer limit, versioning complexity |

### Cold Start Budget by Use Case

| Use Case | Acceptable Cold Start | Strategy |
|----------|----------------------|----------|
| User-facing API (< 200ms SLA) | 0ms | Provisioned Concurrency |
| User-facing API (< 1s SLA) | < 500ms | SnapStart, small packages |
| Async processing | Any | No optimization needed |
| Internal API | < 2s | Fast runtime, avoid VPC |
| Scheduled jobs | Any | No optimization needed |

## Function Composition with Step Functions

### Common Step Functions Patterns

| Pattern | Use Case | State Types Used |
|---------|----------|------------------|
| Sequential | Multi-step processing pipeline | Task → Task → Task |
| Parallel | Fan-out processing | Parallel (branches) |
| Choice / branching | Conditional logic | Choice + Task |
| Map (dynamic parallel) | Process each item in array | Map + Task |
| Retry with backoff | Handle transient failures | Task with Retry config |
| Wait for callback | Human approval, external API | Task with `.waitForTaskToken` |
| Error handling | Catch and recover | Catch + fallback Task |

### Step Functions vs. Direct Lambda Chaining

- **Use Step Functions when:** workflows need visibility, retries, error handling, human approval, or run longer than 15 minutes.
- **Use direct invocation when:** simple A→B calls with no need for retry or state management.

## Serverless Observability

| Concern | Tool | Key Metrics |
|---------|------|------------|
| Logs | CloudWatch Logs, Datadog | Error rates, custom business metrics |
| Traces | X-Ray, Datadog APM | End-to-end latency, cold start frequency |
| Metrics | CloudWatch Metrics | Duration, invocations, errors, throttles, concurrent executions |
| Alarms | CloudWatch Alarms | Error rate > threshold, throttles > 0, duration > budget |
| Cost | Cost Explorer + tags | Per-function cost, cost per invocation |

## Serverless Cost Model

| Factor | Calculation | Optimization Lever |
|--------|------------|-------------------|
| Invocations | Number of requests × $0.20/million | Reduce unnecessary invocations (deduplication, batching) |
| Duration | GB-seconds × $0.0000166667 | Reduce execution time, right-size memory |
| Memory | Allocated (not used) memory | Right-size to actual peak usage |
| Data transfer | GB out to internet | Cache at edge, compress responses |
| API Gateway | Requests × $1–3.50/million | Use Function URLs for internal calls |

## Best Practices

1. **Design for failure** — every function should handle timeouts, retries, and partial failures.
2. **Keep functions focused** — single responsibility, one function per logical operation.
3. **Use managed services** — DynamoDB, SQS, SNS, EventBridge instead of self-managed infra.
4. **Externalize state** — functions are stateless; persist in DynamoDB, S3, or ElastiCache.
5. **Set concurrency limits** — protect downstream services from Lambda auto-scaling floods.
6. **Right-size memory** — Lambda CPU scales with memory; use AWS Lambda Power Tuning to find optimal.

## Using the Reference Files

### When to Read Each Reference

**`/references/fundamentals.md`** — Read when learning serverless concepts, understanding event-driven architecture principles, or evaluating whether serverless is appropriate for a given workload.

**`/references/implementation.md`** — Read when building specific serverless patterns, writing Lambda function handlers, configuring API Gateway integrations, implementing Step Functions workflows, or deploying with SAM/Serverless Framework.

**`/references/best-practices.md`** — Read when optimizing serverless performance, implementing production observability, designing multi-region serverless architectures, or troubleshooting common issues like cold starts, timeouts, and concurrency limits.
