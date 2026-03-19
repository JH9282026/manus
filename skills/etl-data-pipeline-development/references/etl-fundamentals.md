# ETL Fundamentals

Core concepts, patterns, and techniques for Extract, Transform, Load data pipelines.

---

## What is ETL?

ETL (Extract, Transform, Load) is the process of moving data from source systems to target systems while applying transformations to make the data suitable for analytics, reporting, or operational use.

### The Three Phases

**Extract:**
- Read data from source systems (databases, APIs, files, streams)
- Handle various formats (CSV, JSON, XML, Parquet, Avro)
- Manage connection protocols (JDBC, REST, SFTP, S3)
- Implement incremental extraction to minimize load

**Transform:**
- Cleanse data (remove duplicates, handle nulls, fix errors)
- Standardize formats (dates, currencies, units)
- Enrich data (join with reference data, calculate derived fields)
- Aggregate and summarize for analytics
- Apply business rules and logic

**Load:**
- Write data to target systems (data warehouse, data lake, database)
- Choose loading strategy (append, upsert, full refresh)
- Optimize for target system (bulk loading, partitioning)
- Ensure data consistency and integrity

### ETL vs. ELT

**ETL (Extract-Transform-Load):**
- Transform data before loading to target
- Reduces load on target system
- Better for complex transformations
- Traditional approach for data warehouses
- Tools: Informatica, Talend, custom scripts

**ELT (Extract-Load-Transform):**
- Load raw data first, transform in target system
- Leverages power of modern data warehouses (Snowflake, BigQuery, Redshift)
- Faster initial loading
- Flexibility to re-transform without re-extracting
- Modern data stack approach
- Tools: Fivetran, Airbyte, dbt

**When to use each:**
- **ETL**: Legacy systems, limited target capacity, complex pre-processing, data masking required
- **ELT**: Cloud data warehouses, need for raw data access, iterative analytics, modern infrastructure

---

## Batch vs. Streaming Processing

### Batch Processing

**Characteristics:**
- Process data in scheduled intervals (hourly, daily, weekly)
- Handle large volumes of data at once
- Higher latency (minutes to hours)
- Simpler to implement and debug
- Lower infrastructure cost

**Use cases:**
- Daily reporting and analytics
- Historical data analysis
- Data warehouse loading
- Monthly/quarterly aggregations
- Compliance reporting

**Common patterns:**
- **Full load**: Extract entire dataset each run
- **Incremental load**: Extract only new/changed records since last run
- **Delta load**: Identify changes using timestamps or change tracking
- **Snapshot**: Capture point-in-time state of data

**Batch scheduling:**
- Cron-based scheduling (traditional)
- Workflow orchestration (Airflow, Prefect)
- Event-triggered batches (file arrival, API webhook)
- Dependency-based execution (wait for upstream tasks)

### Streaming Processing

**Characteristics:**
- Process data continuously as it arrives
- Low latency (milliseconds to seconds)
- Handle unbounded data streams
- More complex to implement
- Higher infrastructure requirements

**Use cases:**
- Real-time dashboards and monitoring
- Fraud detection and alerting
- IoT sensor data processing
- Clickstream analysis
- Real-time recommendations
- Financial trading systems

**Streaming architectures:**
- **Message queue**: Kafka, RabbitMQ, AWS Kinesis
- **Stream processing**: Spark Streaming, Flink, Kafka Streams
- **Event-driven**: AWS Lambda, Cloud Functions triggered by events

**Streaming concepts:**
- **Windows**: Tumbling (fixed), sliding (overlapping), session (activity-based)
- **Watermarks**: Handle late-arriving data
- **State management**: Maintain aggregations across events
- **Exactly-once semantics**: Ensure no duplicates or data loss

### Micro-batch Processing

**Hybrid approach:**
- Process small batches frequently (every few seconds/minutes)
- Balance between batch simplicity and streaming latency
- Spark Structured Streaming uses this model
- Good for near-real-time use cases without full streaming complexity

---

## Data Extraction Methods

### Full Extraction

**Approach:**
- Extract complete dataset from source every run
- Simple to implement, no change tracking needed
- Inefficient for large datasets
- High load on source systems

**When to use:**
- Small datasets (< 1M rows)
- Source system doesn't support incremental extraction
- Data changes frequently and unpredictably
- Simplicity is priority over efficiency

### Incremental Extraction

**Timestamp-based:**
- Track last extraction time
- Extract records where `updated_at > last_run_time`
- Requires reliable timestamp columns
- May miss updates if timestamp not updated properly

**Sequence-based:**
- Use auto-incrementing IDs or sequence numbers
- Extract records where `id > last_extracted_id`
- Works when records are only inserted, not updated
- Reliable for append-only data

**Change Data Capture (CDC):**
- Monitor database transaction logs
- Capture inserts, updates, deletes in real-time
- Minimal impact on source database
- Requires database-specific tools (Debezium, Oracle GoldenGate)
- Most efficient for large, frequently changing datasets

### API Extraction

**REST APIs:**
- Pagination strategies: offset-based, cursor-based, page-based
- Rate limiting: respect API limits, implement backoff
- Authentication: API keys, OAuth, JWT tokens
- Error handling: retry transient failures, handle 429 (rate limit)

**GraphQL APIs:**
- Request only needed fields
- Reduce over-fetching
- Handle nested queries and pagination

**Webhooks:**
- Push-based data delivery
- Real-time notifications of changes
- Requires endpoint to receive data
- Implement idempotency for duplicate events

### File Extraction

**File formats:**
- **CSV**: Simple, human-readable, but no schema enforcement
- **JSON**: Flexible, nested structures, larger file size
- **Parquet**: Columnar, compressed, efficient for analytics
- **Avro**: Row-based, schema evolution support, good for streaming
- **XML**: Legacy systems, verbose, complex parsing

**File transfer methods:**
- **SFTP/FTP**: Secure file transfer, batch file delivery
- **Cloud storage**: S3, Azure Blob, GCS with event notifications
- **Shared network drives**: Legacy on-premise systems

---

## Data Transformation Techniques

### Data Cleansing

**Handle missing values:**
- Remove records with critical nulls
- Impute with default values, mean, median, or mode
- Forward-fill or back-fill for time-series
- Flag missing data for downstream awareness

**Remove duplicates:**
- Identify duplicates by primary key or composite key
- Keep first, last, or best record based on criteria
- Deduplicate within batch and across historical data

**Fix data errors:**
- Correct known data entry errors
- Standardize inconsistent values
- Validate against business rules
- Quarantine invalid records for review

### Data Standardization

**Format standardization:**
- Dates: Convert to ISO 8601 or standard format
- Phone numbers: Standardize to E.164 format
- Addresses: Parse and standardize components
- Names: Consistent capitalization, remove extra spaces

**Unit conversion:**
- Currency: Convert to base currency with exchange rates
- Measurements: Standardize to metric or imperial
- Time zones: Convert to UTC or standard zone

**Code mapping:**
- Map source codes to standard codes
- Translate legacy codes to modern equivalents
- Maintain mapping tables for reference

### Data Enrichment

**Lookup enrichment:**
- Join with reference data (customer details, product info)
- Add geographic data (country, region from zip code)
- Append demographic data

**Calculated fields:**
- Derive new fields from existing data
- Calculate metrics (revenue, profit margin, age)
- Create flags and indicators (is_active, is_premium)

**External enrichment:**
- Call external APIs for additional data
- Geocoding addresses to coordinates
- Sentiment analysis on text fields
- Entity extraction from unstructured data

### Data Aggregation

**Summarization:**
- Group by dimensions (date, region, product)
- Calculate aggregates (sum, count, average, min, max)
- Create rollup tables for faster queries

**Time-based aggregation:**
- Daily, weekly, monthly summaries
- Rolling windows (7-day average, 30-day total)
- Year-over-year comparisons

**Dimensional modeling:**
- Create fact tables (transactions, events)
- Build dimension tables (customers, products, dates)
- Implement slowly changing dimensions (SCD Type 1, 2, 3)

---

## Data Loading Strategies

### Append-Only Loading

**Approach:**
- Add new records to target table
- Never update or delete existing records
- Simplest loading strategy

**Use cases:**
- Event logs and audit trails
- Time-series data (sensor readings, stock prices)
- Immutable transaction records

**Implementation:**
- INSERT INTO target SELECT * FROM staging
- Partition by date for efficient queries
- Maintain sort order for query performance

### Upsert (Merge) Loading

**Approach:**
- Insert new records
- Update existing records based on primary key
- Maintain current state of data

**Use cases:**
- Customer master data
- Product catalogs
- Inventory levels
- Any data that changes over time

**Implementation:**
- **MERGE statement** (SQL Server, Oracle, Snowflake):
  ```sql
  MERGE INTO target t
  USING staging s ON t.id = s.id
  WHEN MATCHED THEN UPDATE SET t.col = s.col
  WHEN NOT MATCHED THEN INSERT VALUES (s.col)
  ```
- **INSERT ON CONFLICT** (PostgreSQL):
  ```sql
  INSERT INTO target SELECT * FROM staging
  ON CONFLICT (id) DO UPDATE SET col = EXCLUDED.col
  ```
- **Staging table approach**: Load to staging, then merge to target

### Full Refresh Loading

**Approach:**
- Truncate target table
- Load all data from source
- Replace entire dataset

**Use cases:**
- Small dimension tables
- Reference data that changes completely
- When incremental logic is too complex

**Implementation:**
- TRUNCATE target; INSERT INTO target SELECT * FROM staging
- Or: DROP target; CREATE target AS SELECT * FROM staging
- Use transactions to ensure atomicity

### Incremental Merge Loading

**Approach:**
- Load only new/changed records to staging
- Merge staging with target table
- Efficient for large datasets

**Use cases:**
- Large fact tables
- High-volume transactional data
- When full refresh is too slow

**Implementation:**
- Extract incremental data to staging
- Merge staging into target using upsert logic
- Archive or delete staging data after successful load

### Slowly Changing Dimensions (SCD)

**Type 1 - Overwrite:**
- Update existing record with new values
- No history maintained
- Simple but loses historical context

**Type 2 - Add new row:**
- Insert new record for each change
- Maintain full history
- Use effective dates or version numbers
- Most common for data warehouses

**Type 3 - Add new column:**
- Store current and previous value in separate columns
- Limited history (usually just one previous value)
- Simple queries, but limited flexibility

---

## Data Pipeline Patterns

### Lambda Architecture

**Components:**
- **Batch layer**: Process complete dataset, high latency, accurate
- **Speed layer**: Process recent data, low latency, approximate
- **Serving layer**: Merge batch and speed views for queries

**Advantages:**
- Combines accuracy of batch with speed of streaming
- Fault-tolerant and scalable
- Handles late-arriving data

**Disadvantages:**
- Complex to maintain two processing paths
- Code duplication between batch and streaming
- Higher operational overhead

### Kappa Architecture

**Approach:**
- Single streaming pipeline for all processing
- Reprocess historical data by replaying stream
- Simpler than Lambda (one codebase)

**Requirements:**
- Stream storage with long retention (Kafka)
- Ability to replay events from any point in time
- Streaming engine that can handle batch-sized replays

**Advantages:**
- Simpler architecture, one processing path
- No code duplication
- Easier to maintain and debug

**Disadvantages:**
- Requires stream storage with long retention
- Reprocessing can be slow for large historical datasets
- Not suitable for all use cases

### Medallion Architecture (Bronze-Silver-Gold)

**Layers:**
- **Bronze (Raw)**: Land data as-is from sources, no transformations
- **Silver (Cleansed)**: Cleaned, validated, deduplicated data
- **Gold (Curated)**: Business-level aggregates, ready for analytics

**Advantages:**
- Clear separation of concerns
- Ability to reprocess from raw data
- Incremental quality improvement
- Supports both technical and business users

**Implementation:**
- Use data lake (S3, ADLS, GCS) for storage
- Bronze: Parquet/Avro files, partitioned by ingestion date
- Silver: Cleaned data, partitioned by business dimensions
- Gold: Aggregated tables, optimized for query performance

---

## Idempotency and Reliability

### Idempotent Operations

**Definition:**
- Operation produces same result when executed multiple times
- Critical for safe retries and reprocessing

**Techniques:**
- Use deterministic transformations (no random values, current timestamps)
- Upsert based on unique keys instead of append
- Partition data by date/time for isolated reruns
- Use transaction IDs or request IDs to detect duplicates

### Retry Logic

**Exponential backoff:**
- Retry with increasing delays (1s, 2s, 4s, 8s, ...)
- Prevents overwhelming failing systems
- Add jitter to avoid thundering herd

**Retry limits:**
- Maximum number of retries (e.g., 3-5 attempts)
- Maximum total retry time
- Fail and alert after exhausting retries

**Transient vs. permanent failures:**
- Retry transient failures (network timeout, rate limit)
- Don't retry permanent failures (authentication error, invalid data)
- Classify errors and handle appropriately

### Dead Letter Queues

**Purpose:**
- Store records that fail processing after retries
- Prevent pipeline from blocking on bad data
- Enable manual review and reprocessing

**Implementation:**
- Separate storage for failed records (S3, database table)
- Include error details and context
- Monitor DLQ size and alert on growth
- Periodic review and resolution process

---

## Data Partitioning

### Partitioning Strategies

**Time-based partitioning:**
- Partition by date, hour, or other time unit
- Most common for event data and logs
- Enables efficient time-range queries
- Simplifies data retention and archival

**Hash partitioning:**
- Distribute data evenly across partitions
- Good for parallel processing
- Use for data without natural partitioning key

**Range partitioning:**
- Partition by value ranges (e.g., customer ID ranges)
- Useful for ordered data
- Can lead to uneven partition sizes

**List partitioning:**
- Partition by discrete values (e.g., country, product category)
- Good for categorical dimensions
- Number of partitions limited by number of distinct values

### Partition Pruning

**Benefit:**
- Query only relevant partitions
- Dramatically reduce data scanned
- Improve query performance and reduce cost

**Requirements:**
- Include partition key in WHERE clause
- Use partition-aligned filters
- Avoid functions on partition columns that prevent pruning

**Example:**
```sql
-- Good: Partition pruning works
SELECT * FROM events WHERE date = '2024-01-15'

-- Bad: Partition pruning doesn't work
SELECT * FROM events WHERE YEAR(date) = 2024
```
