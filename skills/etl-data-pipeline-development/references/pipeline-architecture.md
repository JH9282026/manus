# Pipeline Architecture

Architectural patterns, design principles, and strategies for building scalable, reliable data pipelines.

---

## Pipeline Architecture Patterns

### Traditional ETL Architecture

**Components:**
1. **Source systems**: Operational databases, SaaS applications, files
2. **ETL server**: Dedicated server running ETL jobs
3. **Staging area**: Temporary storage for extracted data
4. **Transformation engine**: Process and transform data
5. **Data warehouse**: Target analytical database

**Data flow:**
- Extract data from sources to staging area
- Transform data on ETL server
- Load transformed data to data warehouse
- Schedule jobs with cron or enterprise scheduler

**Characteristics:**
- Centralized processing on ETL server
- Transformation before loading
- Batch-oriented processing
- Tightly coupled components

**Limitations:**
- ETL server becomes bottleneck
- Difficult to scale horizontally
- Limited flexibility for ad-hoc analysis
- Expensive proprietary tools

### Modern ELT Architecture

**Components:**
1. **Source systems**: Same as traditional
2. **Data integration platform**: Airbyte, Fivetran, Stitch
3. **Data lake/warehouse**: S3 + Athena, Snowflake, BigQuery, Redshift
4. **Transformation layer**: dbt, Spark, SQL-based transformations
5. **Orchestration**: Airflow, Prefect, dbt Cloud

**Data flow:**
- Extract and load raw data to data lake/warehouse
- Transform data using warehouse compute power
- Create curated datasets for analytics
- Version control transformation logic

**Characteristics:**
- Leverage cloud data warehouse scalability
- Raw data available for exploration
- SQL-based transformations (accessible to analysts)
- Separation of ingestion and transformation

**Advantages:**
- Horizontal scalability
- Flexibility to re-transform without re-extracting
- Lower cost (cloud economics)
- Faster time to value

### Lambda Architecture

**Purpose:**
- Combine batch and streaming for comprehensive data processing
- Balance accuracy (batch) with low latency (streaming)

**Layers:**

**1. Batch Layer:**
- Process complete historical dataset
- High latency (hours), high accuracy
- Recompute views from scratch periodically
- Technologies: Spark, Hive, Presto

**2. Speed Layer:**
- Process recent data in real-time
- Low latency (seconds), approximate results
- Compensate for batch layer lag
- Technologies: Kafka Streams, Flink, Spark Streaming

**3. Serving Layer:**
- Merge batch and speed views
- Provide unified query interface
- Technologies: Druid, Cassandra, HBase

**Data flow:**
- All data goes to both batch and speed layers
- Batch layer periodically recomputes complete views
- Speed layer processes incremental data
- Queries combine results from both layers
- Speed layer data discarded after batch layer catches up

**Use cases:**
- Real-time analytics with historical context
- Systems requiring both accuracy and low latency
- Fraud detection, recommendation engines

**Challenges:**
- Maintain two codebases (batch and streaming)
- Complex operational overhead
- Potential inconsistencies between layers

### Kappa Architecture

**Purpose:**
- Simplify Lambda by using only streaming
- Treat batch as a special case of streaming

**Approach:**
- Single stream processing pipeline
- Store all data in event log (Kafka)
- Reprocess by replaying events from log
- No separate batch layer

**Requirements:**
- Event log with long retention (weeks to years)
- Stream processing engine that handles batch-sized replays
- Ability to version and deploy new processing logic

**Data flow:**
- All events written to Kafka topics
- Stream processing jobs consume and process events
- Output to serving databases or data lake
- To reprocess: deploy new version, replay from beginning

**Advantages:**
- Single codebase for all processing
- Simpler architecture and operations
- Easier to reason about and debug

**Disadvantages:**
- Requires long-retention event log (storage cost)
- Reprocessing can be slow for years of data
- Not suitable for all transformation types

**When to use:**
- Event-driven systems
- Need for reprocessing with new logic
- Team expertise in streaming
- Can afford long-retention event storage

### Medallion Architecture (Lakehouse)

**Purpose:**
- Organize data lake into layers of increasing quality
- Support both data engineering and analytics use cases

**Layers:**

**Bronze (Raw):**
- Land data exactly as received from sources
- No transformations, preserve original format
- Append-only, immutable
- Partitioned by ingestion date
- Purpose: Audit trail, ability to reprocess

**Silver (Cleansed):**
- Cleaned, validated, deduplicated data
- Standardized formats and schemas
- Filtered for quality
- Partitioned by business dimensions
- Purpose: Reliable source for downstream processing

**Gold (Curated):**
- Business-level aggregates and metrics
- Optimized for query performance
- Denormalized for analytics
- Conformed dimensions and facts
- Purpose: Ready for BI tools and data science

**Implementation:**
- Use Delta Lake, Apache Iceberg, or Apache Hudi for ACID transactions
- Store in cloud object storage (S3, ADLS, GCS)
- Process with Spark, dbt, or SQL engines
- Govern with Unity Catalog, AWS Glue Catalog, or similar

**Data flow:**
- Ingest to Bronze (raw landing zone)
- Transform Bronze → Silver (cleansing, validation)
- Transform Silver → Gold (aggregation, business logic)
- Each layer can be queried independently

**Advantages:**
- Clear separation of concerns
- Incremental quality improvement
- Flexibility to reprocess from raw
- Supports diverse use cases (exploration, reporting, ML)

---

## Change Data Capture (CDC) Patterns

### What is CDC?

**Definition:**
- Capture changes (inserts, updates, deletes) from source databases
- Deliver changes to target systems in near real-time
- Minimal impact on source database performance

**Use cases:**
- Real-time data replication
- Database synchronization
- Event-driven architectures
- Audit and compliance
- Cache invalidation

### CDC Implementation Methods

**1. Log-Based CDC (Best Practice)**

**Approach:**
- Read database transaction logs (binlog, WAL, redo logs)
- Capture all changes without querying tables
- Minimal performance impact on source

**Technologies:**
- Debezium (open-source, supports MySQL, PostgreSQL, MongoDB, SQL Server, Oracle)
- AWS Database Migration Service (DMS)
- Oracle GoldenGate
- Qlik Replicate

**Advantages:**
- Low latency (near real-time)
- Captures all changes including deletes
- No impact on application queries
- No schema changes required

**Disadvantages:**
- Requires database-specific configuration
- Log retention policies must be managed
- Initial snapshot can be large

**2. Trigger-Based CDC**

**Approach:**
- Create database triggers on source tables
- Triggers write changes to shadow/audit tables
- ETL process reads from shadow tables

**Advantages:**
- Works on any database with trigger support
- Can capture additional context (user, timestamp)

**Disadvantages:**
- Performance impact on source database
- Requires schema changes (triggers, shadow tables)
- Maintenance overhead (triggers for each table)
- Can miss changes if triggers fail

**3. Query-Based CDC**

**Approach:**
- Periodically query source tables for changes
- Use timestamp or version columns to identify changes
- Compare with previous snapshot

**Advantages:**
- Simple to implement
- No database configuration required
- Works with any database

**Disadvantages:**
- Cannot capture deletes (unless soft delete flag)
- Performance impact from frequent queries
- Higher latency (polling interval)
- Requires reliable timestamp/version columns

### CDC Data Flow

**1. Initial Snapshot:**
- Capture current state of all tables
- Load to target system
- Establish baseline for incremental changes

**2. Incremental Changes:**
- Capture ongoing changes from transaction log
- Stream to message queue (Kafka)
- Apply to target system in order

**3. Schema Evolution:**
- Detect schema changes (add/drop columns, type changes)
- Propagate to target system
- Handle backward/forward compatibility

### CDC with Debezium

**Architecture:**
- Debezium connectors read database logs
- Emit change events to Kafka topics
- Consumers process events and update targets

**Event structure:**
```json
{
  "before": {"id": 1, "name": "Old Name", "status": "active"},
  "after": {"id": 1, "name": "New Name", "status": "active"},
  "op": "u",  // operation: c=create, u=update, d=delete
  "ts_ms": 1634567890123,
  "source": {"db": "mydb", "table": "customers"}
}
```

**Handling events:**
- **Insert (op=c)**: Use "after" values
- **Update (op=u)**: Use "after" values, "before" for audit
- **Delete (op=d)**: Use "before" values, "after" is null

---

## Scalability Patterns

### Horizontal Scaling

**Partition data processing:**
- Split data into independent chunks
- Process chunks in parallel
- Combine results

**Partitioning strategies:**
- **Time-based**: Process each day/hour in parallel
- **Hash-based**: Partition by hash of key (customer ID, order ID)
- **Range-based**: Partition by value ranges

**Implementation:**
- Airflow: Dynamic task generation for each partition
- Spark: Automatic partitioning and parallel processing
- Cloud functions: Process each file/partition independently

### Vertical Scaling

**Increase resource capacity:**
- Larger machines (more CPU, memory)
- Faster storage (SSD, NVMe)
- Better network bandwidth

**When to use:**
- Single-threaded bottlenecks
- Memory-intensive transformations
- Temporary scaling for large batch jobs

**Limitations:**
- Maximum machine size limits
- Higher cost than horizontal scaling
- Single point of failure

### Auto-Scaling

**Dynamic resource allocation:**
- Scale up during peak processing times
- Scale down during idle periods
- Optimize cost and performance

**Cloud implementations:**
- **AWS**: EMR auto-scaling, Glue DPU scaling, ECS/EKS auto-scaling
- **Azure**: Databricks auto-scaling, Data Factory auto-scale
- **GCP**: Dataflow auto-scaling, Dataproc auto-scaling

**Scaling triggers:**
- Queue depth (Kafka lag, SQS messages)
- CPU/memory utilization
- Processing time trends
- Schedule-based (scale up before batch window)

---

## Fault Tolerance and Reliability

### Checkpointing

**Purpose:**
- Save processing state periodically
- Resume from checkpoint on failure
- Avoid reprocessing entire dataset

**Implementation:**
- **Spark**: Checkpoint RDDs and streaming state
- **Flink**: Distributed snapshots of operator state
- **Custom**: Write progress markers to database/file

**Checkpoint strategy:**
- Checkpoint frequency: Balance overhead vs. recovery time
- Checkpoint storage: Reliable storage (S3, HDFS)
- Retention: Keep multiple checkpoints for rollback

### Exactly-Once Semantics

**Challenge:**
- Ensure each record processed exactly once
- Avoid duplicates and data loss
- Critical for financial and compliance use cases

**Approaches:**

**1. Idempotent operations:**
- Design operations to be safely retried
- Use upsert instead of insert
- Include unique transaction IDs

**2. Transactional writes:**
- Use database transactions
- Commit only after successful processing
- Rollback on failure

**3. Two-phase commit:**
- Coordinate commits across multiple systems
- Ensure atomicity across distributed systems

**4. Kafka transactions:**
- Atomic writes to multiple Kafka topics
- Exactly-once processing in Kafka Streams

### Circuit Breaker Pattern

**Purpose:**
- Prevent cascading failures
- Fail fast when dependency is down
- Allow time for recovery

**States:**
- **Closed**: Normal operation, requests pass through
- **Open**: Dependency failing, requests fail immediately
- **Half-Open**: Test if dependency recovered

**Implementation:**
```python
class CircuitBreaker:
    def __init__(self, failure_threshold=5, timeout=60):
        self.failure_count = 0
        self.failure_threshold = failure_threshold
        self.timeout = timeout
        self.state = 'closed'
        self.last_failure_time = None
    
    def call(self, func):
        if self.state == 'open':
            if time.time() - self.last_failure_time > self.timeout:
                self.state = 'half-open'
            else:
                raise Exception("Circuit breaker is open")
        
        try:
            result = func()
            if self.state == 'half-open':
                self.state = 'closed'
                self.failure_count = 0
            return result
        except Exception as e:
            self.failure_count += 1
            self.last_failure_time = time.time()
            if self.failure_count >= self.failure_threshold:
                self.state = 'open'
            raise e
```

### Graceful Degradation

**Strategy:**
- Continue operating with reduced functionality
- Use cached or stale data when source unavailable
- Skip non-critical enrichments

**Examples:**
- Load customer data without optional enrichments
- Use yesterday's exchange rates if API is down
- Process core fields, skip derived calculations

---

## Data Lineage and Metadata

### Data Lineage Tracking

**Purpose:**
- Understand data origin and transformations
- Impact analysis for changes
- Debugging and troubleshooting
- Compliance and audit requirements

**Lineage levels:**

**1. Table-level lineage:**
- Which source tables feed which target tables
- Simplest to implement and visualize

**2. Column-level lineage:**
- Which source columns map to which target columns
- More detailed, useful for impact analysis

**3. Row-level lineage:**
- Track individual record transformations
- Most detailed, highest overhead

**Lineage capture methods:**
- **Query parsing**: Analyze SQL to extract lineage
- **Instrumentation**: Explicitly log lineage in pipeline code
- **Metadata APIs**: Use tool-specific lineage APIs (dbt, Airflow)

**Lineage tools:**
- Apache Atlas (open-source metadata management)
- DataHub (LinkedIn's open-source data catalog)
- Amundsen (Lyft's data discovery platform)
- Commercial: Alation, Collibra, Informatica

### Metadata Management

**Metadata types:**

**Technical metadata:**
- Schema (column names, types, constraints)
- Statistics (row counts, data distribution)
- Partitioning and indexing information
- Storage location and format

**Business metadata:**
- Business definitions and descriptions
- Data ownership and stewardship
- Data classification (PII, confidential)
- Business rules and calculations

**Operational metadata:**
- Pipeline run history
- Data freshness and latency
- Data quality metrics
- Usage statistics

**Metadata storage:**
- **Data catalog**: Centralized metadata repository
- **Schema registry**: Kafka Schema Registry, AWS Glue Schema Registry
- **Data warehouse**: Information schema, system tables

---

## Pipeline Orchestration Strategies

### Dependency Management

**Task dependencies:**
- Define execution order (task A before task B)
- Handle branching (conditional execution)
- Manage fan-out and fan-in patterns

**Data dependencies:**
- Wait for upstream data availability
- Check for file arrival or table update
- Validate data quality before proceeding

**External dependencies:**
- Wait for external system availability
- Check API rate limits
- Coordinate with other pipelines

### Scheduling Strategies

**Time-based scheduling:**
- Cron expressions for regular intervals
- Specific times (daily at 2 AM)
- Timezone considerations

**Event-based scheduling:**
- Trigger on file arrival (S3 event, SFTP)
- Trigger on database change (CDC event)
- Trigger on API webhook

**Dependency-based scheduling:**
- Start when upstream tasks complete
- Wait for data availability sensors
- Cross-DAG dependencies

**Backfilling:**
- Reprocess historical data
- Fill gaps from pipeline failures
- Apply new logic to past data

### Workflow Patterns

**Sequential:**
- Tasks execute one after another
- Simple, easy to understand
- Longer total execution time

**Parallel:**
- Independent tasks execute simultaneously
- Faster total execution time
- Requires sufficient resources

**Fan-out/Fan-in:**
- One task triggers multiple parallel tasks
- Parallel tasks converge to single downstream task
- Common for processing partitions

**Conditional branching:**
- Execute different paths based on conditions
- Skip tasks based on data availability
- Handle different scenarios (weekday vs. weekend)

**Dynamic task generation:**
- Generate tasks at runtime based on data
- Process variable number of partitions
- Adapt to changing requirements
