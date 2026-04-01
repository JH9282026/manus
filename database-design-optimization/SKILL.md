---
name: database-design-optimization
description: "Design and optimize SQL and NoSQL databases for performance and scalability. Use for: database schema design, choosing between SQL and NoSQL, implementing indexing strategies, query optimization, database normalization and denormalization, partitioning and sharding, connection pooling, caching strategies, handling migrations, and scaling databases for high-traffic applications."
---

# Database Design & Optimization

Design robust database schemas and optimize performance for both SQL and NoSQL databases.

## Overview

This skill provides comprehensive guidance for database design, optimization, and scaling. Learn to choose the right database type, design efficient schemas, implement strategic indexing, optimize queries, and scale databases for production workloads. Covers both relational (SQL) and non-relational (NoSQL) databases.

## Database Type Selection

| Use Case | Database Type | Examples | When to Use |
|----------|--------------|----------|-------------|
| Structured data, ACID compliance | SQL (Relational) | PostgreSQL, MySQL | Financial systems, e-commerce, traditional apps |
| Flexible schema, horizontal scaling | Document Store | MongoDB, CouchDB | Content management, catalogs, user profiles |
| High-speed caching, sessions | Key-Value Store | Redis, Memcached | Caching, session storage, real-time analytics |
| Time-series data | Time-Series DB | InfluxDB, TimescaleDB | IoT, monitoring, metrics |
| Graph relationships | Graph Database | Neo4j, ArangoDB | Social networks, recommendation engines |
| Wide-column data | Column-Family | Cassandra, HBase | Big data, analytics, high write throughput |

## SQL Database Design

### Normalization Levels

**1NF (First Normal Form):**
- Eliminate repeating groups
- Each cell contains single value
- Each record is unique

**2NF (Second Normal Form):**
- Must be in 1NF
- All non-key attributes fully dependent on primary key

**3NF (Third Normal Form):**
- Must be in 2NF
- No transitive dependencies
- Non-key attributes depend only on primary key

**When to Denormalize:**
- Read-heavy workloads
- Complex joins impacting performance
- Data warehouse/analytics scenarios
- Caching layer requirements

### Index Types and Usage

| Index Type | Use Case | Performance | Storage Cost |
|------------|----------|-------------|--------------|
| B-tree | Range queries, sorting, most common | Excellent | Medium |
| Hash | Equality lookups only | Very fast | Low |
| GiST/GIN | Full-text search, arrays, JSON | Good | High |
| BRIN | Very large tables, sequential data | Good | Very low |
| Partial | Subset of rows (e.g., WHERE active=true) | Excellent | Low |
| Composite | Multiple columns queried together | Excellent | Medium-High |

### Indexing Best Practices

- Index foreign keys used in JOINs
- Index columns in WHERE, ORDER BY, GROUP BY clauses
- Use composite indexes for multi-column queries (order matters)
- Avoid over-indexing (slows writes, increases storage)
- Monitor index usage and remove unused indexes
- Use covering indexes to avoid table lookups

## NoSQL Database Design

### Document Store (MongoDB) Patterns

**Embedding vs. Referencing:**

**Embed when:**
- Data accessed together
- One-to-few relationships
- Data doesn't change often

**Reference when:**
- Data accessed independently
- One-to-many or many-to-many relationships
- Data changes frequently

### NoSQL Indexing Strategies

**MongoDB Index Types:**
- Single field indexes
- Compound indexes
- Multikey indexes (arrays)
- Text indexes (full-text search)
- Geospatial indexes (2d, 2dsphere)
- Hashed indexes (sharding)

## Query Optimization

### SQL Query Optimization Techniques

1. **Use EXPLAIN/EXPLAIN ANALYZE**
   - Understand query execution plan
   - Identify sequential scans vs index scans
   - Check for expensive operations

2. **Optimize JOINs**
   - Join on indexed columns
   - Filter early with WHERE clauses
   - Consider join order (smaller tables first)

3. **Avoid SELECT ***
   - Request only needed columns
   - Reduces data transfer and memory usage

4. **Use Pagination**
   - LIMIT/OFFSET for small datasets
   - Cursor-based for large datasets

5. **Batch Operations**
   - Use bulk inserts/updates
   - Reduce round trips to database

### NoSQL Query Optimization

1. **Projection**
   - Return only needed fields
   - Reduces network transfer

2. **Aggregation Pipeline Optimization**
   - Use $match early to filter documents
   - Use indexes for $match and $sort
   - Limit pipeline stages

3. **Avoid Large Documents**
   - Keep documents under 16MB (MongoDB limit)
   - Use references for large embedded data

## Connection Pooling

**Why Connection Pooling:**
- Reuse database connections
- Reduce connection overhead
- Limit concurrent connections
- Improve application performance

## Caching Strategies

### Cache Layers

1. **Application-Level Cache (Redis/Memcached)**
   - Cache query results
   - Cache computed values
   - Session storage

2. **Database Query Cache**
   - Built-in query result caching
   - Automatic invalidation

3. **Materialized Views**
   - Precomputed query results
   - Periodic refresh

### Cache Invalidation Patterns

- **Time-based (TTL)**: Expire after fixed duration
- **Event-based**: Invalidate on data changes
- **Write-through**: Update cache on write
- **Write-behind**: Async cache updates

## Partitioning and Sharding

### Partitioning (Vertical Scaling)

**Horizontal Partitioning (Sharding):**
- Split rows across multiple tables/databases
- Based on partition key (e.g., user_id, date)

**Vertical Partitioning:**
- Split columns across tables
- Separate frequently vs rarely accessed data

### Sharding (Horizontal Scaling)

**Sharding Strategies:**
- **Range-based**: Shard by ID ranges
- **Hash-based**: Hash partition key
- **Geographic**: Shard by region
- **Directory-based**: Lookup table for shard location

**Challenges:**
- Cross-shard queries
- Rebalancing shards
- Maintaining consistency

## Database Migrations

**Best Practices:**
- Version control all migrations
- Test migrations on staging first
- Make migrations reversible
- Avoid data loss (backup first)
- Use transactions when possible
- Plan for zero-downtime migrations

## Performance Monitoring

**Key Metrics:**
- Query execution time
- Connection pool usage
- Cache hit ratio
- Index usage statistics
- Slow query log
- Database size and growth
- Replication lag (if applicable)

**Tools:**
- PostgreSQL: pg_stat_statements, EXPLAIN ANALYZE
- MongoDB: Database Profiler, explain()
- Redis: INFO, MONITOR
- External: Datadog, New Relic, Prometheus

## Using the Reference Files

**`/references/sql-optimization.md`** — Read when optimizing SQL queries, designing schemas, implementing indexes, or troubleshooting performance issues in relational databases.

**`/references/nosql-patterns.md`** — Read when designing NoSQL schemas, choosing data models, implementing indexes in MongoDB/Cassandra, or optimizing document/key-value stores.

**`/references/scaling-strategies.md`** — Read when implementing sharding, partitioning, replication, or scaling databases for high-traffic production environments.

**`/references/migration-patterns.md`** — Read when planning database migrations, schema changes, zero-downtime deployments, or data transformation strategies.
