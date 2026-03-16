---
name: performance-optimization-scaling
description: "Optimize web application performance and implement scaling strategies using caching, CDNs, and load balancing. Use for: implementing caching layers (Redis, Memcached), CDN integration, load balancing strategies, horizontal and vertical scaling, database query optimization, asset optimization, implementing auto-scaling, monitoring performance metrics, reducing latency, and handling high-traffic scenarios."
---

# Performance Optimization & Scaling

Optimize web application performance and implement scalable architectures for high-traffic systems.

## Overview

This skill covers comprehensive performance optimization and scaling strategies including caching, CDN integration, load balancing, and auto-scaling. Learn to identify bottlenecks, implement multi-layer caching, optimize assets, and scale applications to handle millions of users.

## Performance Optimization Layers

| Layer | Optimization Techniques | Impact |
|-------|------------------------|--------|
| Client | Asset minification, lazy loading, code splitting | High |
| CDN | Edge caching, geographic distribution | Very High |
| Application | Code optimization, async processing, connection pooling | High |
| Cache | Redis, Memcached, application cache | Very High |
| Database | Indexing, query optimization, connection pooling | Very High |
| Infrastructure | Load balancing, auto-scaling, CDN | High |

## Caching Strategies

### Multi-Layer Caching

**Layer 1: Browser Cache**
- Cache static assets locally
- Configured via Cache-Control headers
- Fastest (0ms latency)

**Layer 2: CDN Edge Cache**
- Cache at edge locations globally
- Serves users from nearest location
- Very fast (10-50ms latency)

**Layer 3: Application Cache (Redis/Memcached)**
- Cache database queries, computed results
- In-memory, very fast
- Shared across application servers

**Layer 4: Database Query Cache**
- Built-in database caching
- Automatic invalidation

### Cache Invalidation Patterns

**Time-Based (TTL)**
```python
redis.setex("user:123", 3600, user_data)  # 1 hour TTL
```

**Event-Based**
```python
# Invalidate on update
def update_user(user_id, data):
    db.update_user(user_id, data)
    redis.delete(f"user:{user_id}")
```

**Write-Through**
```python
def update_user(user_id, data):
    db.update_user(user_id, data)
    redis.set(f"user:{user_id}", data)
```

**Cache-Aside (Lazy Loading)**
```python
def get_user(user_id):
    cached = redis.get(f"user:{user_id}")
    if cached:
        return cached
    
    user = db.get_user(user_id)
    redis.setex(f"user:{user_id}", 3600, user)
    return user
```

## Content Delivery Networks (CDN)

### CDN Benefits

- **Reduced Latency**: Serve from nearest edge location
- **Bandwidth Savings**: Offload traffic from origin
- **DDoS Protection**: Absorb malicious traffic
- **Global Availability**: Multiple PoPs worldwide
- **SSL/TLS Termination**: Handle encryption at edge

### CDN Configuration

**Cache-Control Headers:**
```
Cache-Control: public, max-age=31536000, immutable
```

**Vary Header:**
```
Vary: Accept-Encoding, Accept
```

**CDN Providers:**
- Cloudflare
- AWS CloudFront
- Fastly
- Akamai
- Azure CDN

### Asset Optimization

**Images:**
- Use modern formats (WebP, AVIF)
- Implement responsive images
- Lazy load below-the-fold images
- Compress images (TinyPNG, ImageOptim)

**JavaScript/CSS:**
- Minify and compress
- Code splitting
- Tree shaking (remove unused code)
- Bundle optimization

**Fonts:**
- Use font-display: swap
- Subset fonts (include only needed characters)
- Use WOFF2 format

## Load Balancing

### Load Balancing Algorithms

**Round Robin**: Distribute requests evenly across servers

**Least Connections**: Send to server with fewest active connections

**IP Hash**: Same client always goes to same server

**Weighted Round Robin**: Distribute based on server capacity

**Least Response Time**: Send to fastest responding server

### Load Balancer Types

**Layer 4 (Transport Layer)**
- Routes based on IP/port
- Faster, less overhead
- No content inspection

**Layer 7 (Application Layer)**
- Routes based on HTTP headers, URL, cookies
- Content-aware routing
- SSL termination

### Implementation

**Nginx Load Balancer:**
```nginx
upstream backend {
    least_conn;
    server backend1:8000 weight=3;
    server backend2:8000 weight=2;
    server backend3:8000 weight=1;
}

server {
    listen 80;
    location / {
        proxy_pass http://backend;
    }
}
```

**HAProxy:**
```
frontend http_front
    bind *:80
    default_backend http_back

backend http_back
    balance roundrobin
    server server1 10.0.1.10:8000 check
    server server2 10.0.1.11:8000 check
    server server3 10.0.1.12:8000 check
```

## Horizontal vs. Vertical Scaling

### Vertical Scaling (Scale Up)

**Definition**: Increase resources of single server

**Pros:**
- Simple implementation
- No code changes
- Maintains data consistency

**Cons:**
- Hardware limits
- Single point of failure
- Expensive at scale

### Horizontal Scaling (Scale Out)

**Definition**: Add more servers

**Pros:**
- Nearly unlimited scalability
- Better fault tolerance
- Cost-effective at scale

**Cons:**
- Complex implementation
- Requires stateless design
- Data distribution challenges

## Auto-Scaling

### Metrics-Based Scaling

**CPU-Based:**
```yaml
# Kubernetes HPA
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: app-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: app
  minReplicas: 3
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
```

**Request-Based:**
- Scale based on requests per second
- Queue length
- Response time

### Predictive Scaling

- Analyze historical patterns
- Scale before traffic spike
- Machine learning-based

## Database Optimization

### Query Optimization

- Use EXPLAIN to analyze queries
- Add indexes on frequently queried columns
- Avoid N+1 queries
- Use pagination for large datasets
- Implement query caching

### Connection Pooling

**Benefits:**
- Reuse connections
- Reduce connection overhead
- Limit concurrent connections

**Configuration:**
```python
engine = create_engine(
    "postgresql://user:pass@localhost/db",
    pool_size=20,
    max_overflow=10,
    pool_timeout=30
)
```

### Read Replicas

- Separate read and write traffic
- Scale reads horizontally
- Reduce load on primary database

## Performance Monitoring

### Key Metrics

**Application Metrics:**
- Response time (p50, p95, p99)
- Requests per second
- Error rate
- Throughput

**Infrastructure Metrics:**
- CPU usage
- Memory usage
- Disk I/O
- Network bandwidth

**User Experience Metrics:**
- Time to First Byte (TTFB)
- First Contentful Paint (FCP)
- Largest Contentful Paint (LCP)
- Cumulative Layout Shift (CLS)
- Time to Interactive (TTI)

### Monitoring Tools

- **APM**: New Relic, Datadog, AppDynamics
- **Infrastructure**: Prometheus, Grafana
- **Logs**: ELK Stack, Splunk
- **Real User Monitoring**: Google Analytics, Sentry
- **Synthetic Monitoring**: Pingdom, UptimeRobot

## Async Processing

### Background Jobs

**Use Cases:**
- Email sending
- Image processing
- Report generation
- Data imports

**Tools:**
- Celery (Python)
- Sidekiq (Ruby)
- Bull (Node.js)
- RabbitMQ, Redis Queue

### Message Queues

**Benefits:**
- Decouple services
- Handle traffic spikes
- Retry failed jobs
- Prioritize tasks

**Providers:**
- RabbitMQ
- Apache Kafka
- AWS SQS
- Redis

## Compression

### HTTP Compression

**Gzip:**
```nginx
gzip on;
gzip_types text/plain text/css application/json application/javascript;
gzip_min_length 1000;
```

**Brotli:**
- Better compression than Gzip
- Supported by modern browsers

### Database Compression

- Compress large text fields
- Use appropriate data types
- Archive old data

## Rate Limiting

**Prevent abuse and ensure fair usage**

**Implementation:**
```python
from redis import Redis

redis = Redis()

def check_rate_limit(user_id, limit=100, window=3600):
    key = f"rate_limit:{user_id}"
    current = redis.get(key)
    
    if current is None:
        redis.setex(key, window, 1)
        return True
    
    if int(current) < limit:
        redis.incr(key)
        return True
    
    return False
```

## Using the Reference Files

**`/references/caching-strategies.md`** — Read when implementing multi-layer caching, choosing cache invalidation patterns, or optimizing cache hit ratios.

**`/references/cdn-optimization.md`** — Read when integrating CDNs, configuring edge caching, or optimizing asset delivery globally.

**`/references/load-balancing-scaling.md`** — Read when implementing load balancers, auto-scaling, or designing horizontally scalable architectures.

**`/references/performance-monitoring.md`** — Read when setting up performance monitoring, analyzing metrics, or troubleshooting performance bottlenecks.
