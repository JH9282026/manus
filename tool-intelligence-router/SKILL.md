---
name: tool-intelligence-router
description: "Route tasks to the optimal tool or service based on requirements, constraints, and context. Use for: tool selection logic, capability matching, multi-tool orchestration, fallback routing, cost-performance optimization, API gateway routing, and intelligent task delegation across heterogeneous tool ecosystems."
---

# Tool Intelligence Router

Route tasks to the optimal tool, API, or service based on capability matching, performance requirements, cost constraints, and context.

## Overview

Modern workflows involve dozens of specialized tools, APIs, and services. Choosing the right tool for each task — and gracefully handling failures — is critical for reliability and efficiency. This skill provides frameworks for building intelligent routing logic that matches task requirements to tool capabilities, manages fallbacks, optimizes for cost and latency, and orchestrates multi-tool workflows.

## Routing Decision Framework

| Factor | Weight | Evaluation Method | Reference |
|--------|--------|-------------------|-----------|
| Capability match | Critical | Does the tool support the required operation? | `/references/tool-catalog.md` |
| Input compatibility | Critical | Can the tool accept the input format/size? | `/references/tool-catalog.md` |
| Output quality | High | Does the tool meet quality requirements? | `/references/routing-algorithms.md` |
| Latency requirements | High | Can the tool respond within time budget? | `/references/optimization-strategies.md` |
| Cost per operation | Medium | What's the unit economics? | `/references/optimization-strategies.md` |
| Reliability/uptime | Medium | What's the tool's availability SLA? | `/references/routing-algorithms.md` |
| Rate limits | Medium | Can the tool handle current throughput? | `/references/integration-patterns.md` |
| Data privacy | High | Does routing comply with data policies? | `/references/routing-algorithms.md` |

## Routing Algorithm Selection

| Algorithm | Complexity | Best For | Trade-off |
|-----------|-----------|----------|-----------|
| Rule-based (if/else) | Low | Small tool sets (<10), clear boundaries | Brittle, doesn't adapt |
| Weighted scoring | Medium | Multi-factor decisions, configurable | Requires weight tuning |
| Decision tree | Medium | Hierarchical decisions with clear criteria | Can become deep/complex |
| Capability matching | Medium | Heterogeneous tool ecosystem | Needs capability schema |
| ML-based routing | High | High-volume, pattern-rich routing | Needs training data |
| Cost-optimizer | Medium | Budget-constrained environments | May sacrifice quality |
| Cascade/fallback chain | Low–Medium | Reliability-focused routing | Higher latency on fallbacks |

### Weighted Scoring Implementation

| Step | Action | Example |
|------|--------|---------|
| 1. Define criteria | List factors that matter | Capability, speed, cost, quality |
| 2. Assign weights | Distribute 100 points across criteria | Capability: 40, Speed: 25, Cost: 20, Quality: 15 |
| 3. Score each tool | Rate each tool per criterion (0–10) | Tool A: Capability=9, Speed=7, Cost=5, Quality=8 |
| 4. Calculate weighted score | Sum(weight × score) for each tool | Tool A: 40×9 + 25×7 + 20×5 + 15×8 = 755 |
| 5. Select highest score | Route to winner | Tool A wins if 755 is highest |
| 6. Apply constraints | Eliminate disqualified tools first | If input >10MB and Tool B max is 5MB, exclude Tool B |

## Tool Capability Schema

### Capability Definition Structure

| Field | Purpose | Example Values |
|-------|---------|---------------|
| tool_id | Unique identifier | `openai-gpt4`, `anthropic-claude`, `local-llama` |
| operations | Supported operation types | `text-generation`, `image-analysis`, `code-execution` |
| input_formats | Accepted input types | `text`, `json`, `image/png`, `audio/mp3` |
| max_input_size | Maximum input size | `128KB`, `10MB`, `100MB` |
| output_formats | Produced output types | `text`, `json`, `image/png` |
| latency_p50 | Median response time | `200ms`, `2s`, `30s` |
| latency_p99 | 99th percentile response time | `5s`, `30s`, `120s` |
| cost_per_call | Unit cost | `$0.001`, `$0.03`, `$0.50` |
| rate_limit | Max calls per time window | `100/min`, `1000/hour` |
| availability | Uptime SLA | `99.9%`, `99.99%` |
| quality_score | Benchmark performance | `0.85`, `0.92` (0–1 scale) |

## Multi-Tool Orchestration Patterns

| Pattern | Description | Use Case | Reference |
|---------|-------------|----------|-----------|
| Sequential chain | Tool A output → Tool B input | Extract → Transform → Load | `/references/integration-patterns.md` |
| Parallel fan-out | Same input → multiple tools → aggregate | Multi-model ensemble, redundancy | `/references/integration-patterns.md` |
| Cascade/waterfall | Try Tool A → if fail, try Tool B → Tool C | Degradation-resistant routing | `/references/integration-patterns.md` |
| Router + specialist | Router decides which specialist to call | Task classification → domain expert | `/references/routing-algorithms.md` |
| Splitter + merger | Split task into subtasks → route each → merge results | Complex multi-step workflows | `/references/integration-patterns.md` |
| Circuit breaker | Stop routing to failed tool temporarily | Prevent cascading failures | `/references/integration-patterns.md` |

### Cascade/Fallback Implementation

| Priority | Tool | Condition to Try | Condition to Fail Over |
|----------|------|-------------------|----------------------|
| 1 (primary) | Premium API | Always try first | Timeout >5s, error response, rate limited |
| 2 (secondary) | Alternative API | Primary failed | Same failure conditions |
| 3 (fallback) | Local model | Both APIs failed | — (always available, lower quality) |
| 4 (graceful degradation) | Cached result | All tools failed | Return stale data with warning |

## Cost Optimization Strategies

| Strategy | Savings | Implementation |
|----------|---------|---------------|
| Tiered routing | 30–60% | Use cheap tool for simple tasks, expensive for complex |
| Caching | 20–50% | Cache responses for identical/similar inputs |
| Batch processing | 10–30% | Aggregate requests to reduce per-call overhead |
| Off-peak scheduling | 10–20% | Route non-urgent tasks to cheaper time windows |
| Model distillation | 40–70% | Train smaller model to mimic expensive model for common cases |
| Precomputation | Variable | Pre-generate answers for predictable queries |

## Monitoring and Observability

| Metric | What to Track | Alert Threshold |
|--------|---------------|-----------------|
| Route distribution | % of requests per tool | Any tool >80% (over-concentration) |
| Fallback rate | % of requests hitting fallback tools | >10% sustained |
| Latency by route | P50, P95, P99 per tool | P99 > 2× SLA target |
| Error rate by tool | Failed requests / total | >5% for any tool |
| Cost per request | Average cost by route | >20% above budget |
| Quality scores | User feedback, accuracy metrics | Degradation trend |

## Best Practices

- **Always have a fallback** — no single tool should be a single point of failure
- **Measure before optimizing** — instrument routing decisions before tuning weights
- **Separate routing logic from tool integration** — routing rules change more often than API clients
- **Use feature flags** — enable gradual rollout of new tools or routing changes
- **Cache aggressively** — identical inputs should return cached results, not burn API credits
- **Log every routing decision** — you need audit trail for debugging and optimization

## Using the Reference Files

**`/references/tool-catalog.md`** — Read when mapping available tools and their capabilities. Covers capability schemas, tool comparison matrices, and selection criteria.

**`/references/routing-algorithms.md`** — Read when implementing routing logic. Covers decision trees, scoring algorithms, ML-based routing, and quality-aware selection.

**`/references/integration-patterns.md`** — Read when building multi-tool orchestration. Covers sequential chains, parallel fan-out, circuit breakers, and error handling patterns.

**`/references/optimization-strategies.md`** — Read when optimizing routing for cost or performance. Covers caching strategies, tiered routing, batch processing, and monitoring setup.
