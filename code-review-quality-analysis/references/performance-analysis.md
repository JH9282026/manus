# Performance Analysis

Identify and resolve performance bottlenecks in application code.

---

## Algorithm Complexity Review

### Common Inefficiencies

| Pattern | Issue | Optimization |
|---|---|---|
| Nested loops over same data | O(n²) when O(n) possible | Hash maps, single-pass algorithms |
| Repeated database queries in loops | N+1 query problem | Batch queries, eager loading, joins |
| String concatenation in loops | O(n²) memory allocation | StringBuilder, list join |
| Sorting before searching | Unnecessary O(n log n) | Use hash set for O(1) lookup |
| Full table scans | Missing indexes | Add appropriate indexes, query optimization |
| Unbounded result sets | Memory and performance risk | Pagination, limit clauses |

### Big-O Quick Reference

| Operation | Array | Hash Map | Sorted Array | BST |
|---|---|---|---|---|
| Search | O(n) | O(1) avg | O(log n) | O(log n) |
| Insert | O(1) append | O(1) avg | O(n) | O(log n) |
| Delete | O(n) | O(1) avg | O(n) | O(log n) |
| Sort | O(n log n) | N/A | Already sorted | N/A |

---

## Database Performance

### Query Optimization Checklist

- [ ] Examine query execution plans (EXPLAIN ANALYZE)
- [ ] Verify indexes exist for WHERE, JOIN, ORDER BY columns
- [ ] Check for missing indexes on foreign keys
- [ ] Identify full table scans on large tables
- [ ] Look for unnecessary SELECT * (return only needed columns)
- [ ] Review JOIN efficiency (nested loop vs. hash join vs. merge join)
- [ ] Check for N+1 query patterns in application code
- [ ] Evaluate query caching opportunities

### Index Strategy

| Index Type | Use Case | Trade-off |
|---|---|---|
| B-tree (default) | Equality and range queries | Write overhead, storage |
| Hash | Exact match only | No range support |
| GIN/GiST | Full-text search, JSON, arrays | Slower updates |
| Composite | Multi-column queries | Column order matters |
| Partial | Frequently filtered subset | Limited applicability |
| Covering | Include all SELECT columns | Storage cost |

---

## Frontend Performance

### Core Web Vitals

| Metric | Target | Impact |
|---|---|---|
| Largest Contentful Paint (LCP) | < 2.5s | Perceived load speed |
| First Input Delay (FID) | < 100ms | Interactivity responsiveness |
| Cumulative Layout Shift (CLS) | < 0.1 | Visual stability |
| Time to First Byte (TTFB) | < 800ms | Server responsiveness |

### Optimization Techniques

- Code splitting and lazy loading for JavaScript bundles
- Image optimization (WebP/AVIF, responsive images, lazy load)
- Critical CSS inlining and deferred stylesheet loading
- Resource hints (preload, prefetch, preconnect)
- Service worker caching for static assets
- CDN for global content delivery
