---
name: etl-data-pipeline-development
description: "Design, build, and maintain ETL (Extract, Transform, Load) data pipelines for moving and transforming data across systems. Use for creating batch or streaming data pipelines, integrating data sources, implementing data transformations, orchestrating workflows, optimizing pipeline performance, handling data quality issues, working with tools like Apache Airflow, Spark, Kafka, or cloud-native services (AWS Glue, Azure Data Factory, Google Dataflow), and building scalable data infrastructure."
---

# ETL Data Pipeline Development

Design, build, and maintain robust ETL pipelines that extract data from multiple sources, transform it according to business rules, and load it into target systems for analytics and operations.

## Overview

ETL data pipeline development encompasses the full lifecycle of data movement and transformation infrastructure. This skill covers pipeline architecture design, tool selection, implementation patterns, orchestration strategies, performance optimization, error handling, monitoring, and best practices for building reliable, scalable data pipelines that support analytics, machine learning, and operational systems.

## Pipeline Type Selection

| Use Case | Pipeline Type | Processing Mode | Recommended Tools | Reference |
|----------|---------------|-----------------|-------------------|----------|
| Daily reporting, analytics refresh | Batch ETL | Scheduled batch | Airflow + Spark, dbt | `/references/etl-fundamentals.md` |
| Real-time dashboards, event processing | Streaming ETL | Continuous stream | Kafka + Flink, Spark Streaming | `/references/etl-fundamentals.md` |
| Cloud data warehouse loading | ELT (Extract-Load-Transform) | Batch or micro-batch | Fivetran, Stitch, dbt | `/references/pipeline-architecture.md` |
| Change data capture, database sync | CDC pipeline | Real-time incremental | Debezium, AWS DMS, Airbyte | `/references/pipeline-architecture.md` |
| Multi-source data integration | Hybrid pipeline | Mixed batch/stream | Airflow + Kafka + Spark | `/references/pipeline-architecture.md` |
| Serverless data processing | Event-driven ETL | On-demand triggers | AWS Lambda + Glue, Cloud Functions | `/references/tools-platforms.md` |

## Core Pipeline Development Process

### 1. Requirements Analysis

**Define data sources and targets:**
- Identify all source systems (databases, APIs, files, streams)
- Document data formats, schemas, access methods
- Determine target systems (data warehouse, lake, operational DB)
- Establish SLAs for data freshness and availability

**Understand transformation requirements:**
- Business logic and calculation rules
- Data quality requirements and validation rules
- Aggregation, enrichment, and joining needs
- Compliance and security requirements (PII handling, encryption)

### 2. Architecture Design

**Choose pipeline pattern:**
- **Batch ETL**: Scheduled full or incremental loads
- **Streaming ETL**: Continuous processing of event streams
- **Lambda architecture**: Batch + streaming for comprehensive coverage
- **Kappa architecture**: Stream-only processing with reprocessing capability
- **ELT**: Load raw data first, transform in target system

**Design data flow:**
- Source → Extraction → Staging → Transformation → Loading → Target
- Include intermediate storage (data lake, staging tables)
- Plan for data lineage and audit trails
- Design idempotent operations for safe retries

### 3. Tool and Technology Selection

**Orchestration layer:**
- Apache Airflow (most popular, Python-based DAGs)
- Prefect (modern alternative with better UI)
- Dagster (software-defined assets approach)
- Cloud-native: AWS Step Functions, Azure Data Factory, Google Cloud Composer

**Processing engine:**
- Apache Spark (large-scale batch and streaming)
- Apache Flink (advanced streaming with state management)
- dbt (SQL-based transformations in data warehouse)
- Pandas/Polars (smaller datasets, Python-native)

**Data integration:**
- Airbyte (open-source, 300+ connectors)
- Fivetran (managed, enterprise connectors)
- Singer taps and targets (lightweight, composable)
- Custom connectors (APIs, databases, files)

### 4. Implementation Best Practices

**Extraction strategies:**
- **Full extraction**: Complete dataset each run (simple but inefficient)
- **Incremental extraction**: Only new/changed records (efficient, requires tracking)
- **CDC (Change Data Capture)**: Database log-based real-time capture
- **API pagination**: Handle rate limits, cursor-based or offset pagination

**Transformation patterns:**
- **Staging layer**: Land raw data unchanged for auditability
- **Cleansing**: Handle nulls, duplicates, invalid values
- **Standardization**: Consistent formats, units, naming conventions
- **Enrichment**: Join with reference data, calculate derived fields
- **Aggregation**: Summarize for analytics use cases

**Loading strategies:**
- **Append-only**: Add new records (event logs, time-series)
- **Upsert (merge)**: Insert new, update existing based on key
- **Full refresh**: Truncate and reload (dimension tables)
- **Incremental merge**: Combine new data with existing (fact tables)

### 5. Error Handling and Reliability

**Implement robust error handling:**
- Retry logic with exponential backoff
- Dead letter queues for failed records
- Circuit breakers for failing dependencies
- Graceful degradation when sources unavailable

**Ensure data quality:**
- Schema validation at ingestion
- Data quality checks (completeness, accuracy, consistency)
- Anomaly detection (volume, distribution, outliers)
- Automated alerts for quality issues

**Design for idempotency:**
- Use deterministic transformations
- Implement upsert logic based on unique keys
- Partition data by date/time for safe reruns
- Avoid side effects in transformation logic

### 6. Monitoring and Observability

**Track pipeline health:**
- Execution status (success, failure, running time)
- Data volume metrics (records processed, bytes transferred)
- Data quality metrics (validation pass rate, null percentages)
- Resource utilization (CPU, memory, I/O)

**Implement alerting:**
- Pipeline failures and retries
- SLA violations (data freshness, processing time)
- Data quality threshold breaches
- Resource exhaustion warnings

**Enable debugging:**
- Detailed logging at each pipeline stage
- Data lineage tracking (source to target)
- Sample data inspection at checkpoints
- Version control for pipeline code and configurations

## Common Pipeline Patterns

### Batch Processing Pattern

```python
# Airflow DAG example structure
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'data-team',
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'daily_sales_etl',
    default_args=default_args,
    schedule_interval='0 2 * * *',  # 2 AM daily
    catchup=False,
) as dag:
    
    extract = PythonOperator(
        task_id='extract_sales_data',
        python_callable=extract_from_source,
    )
    
    transform = PythonOperator(
        task_id='transform_sales_data',
        python_callable=apply_transformations,
    )
    
    validate = PythonOperator(
        task_id='validate_data_quality',
        python_callable=run_quality_checks,
    )
    
    load = PythonOperator(
        task_id='load_to_warehouse',
        python_callable=load_to_target,
    )
    
    extract >> transform >> validate >> load
```

### Streaming Processing Pattern

**Kafka + Spark Streaming:**
- Consume events from Kafka topics
- Apply transformations in micro-batches or continuous mode
- Write to target systems (database, data lake, another Kafka topic)
- Handle late-arriving data with watermarks
- Maintain state for aggregations and joins

### ELT Pattern (Modern Data Stack)

**Workflow:**
1. **Extract + Load**: Use Fivetran/Airbyte to sync raw data to warehouse
2. **Transform**: Use dbt to transform data with SQL in the warehouse
3. **Orchestrate**: Use Airflow or dbt Cloud to schedule transformations
4. **Test**: dbt tests for data quality validation
5. **Document**: Auto-generated data lineage and documentation

## Performance Optimization

### Extraction Optimization

- **Parallel extraction**: Split large tables by partition or range
- **Incremental loading**: Use timestamps or sequence numbers
- **Compression**: Reduce network transfer time
- **Connection pooling**: Reuse database connections
- **Batch API calls**: Reduce request overhead

### Transformation Optimization

- **Pushdown processing**: Transform in source/target database when possible
- **Columnar storage**: Use Parquet/ORC for analytical workloads
- **Partitioning**: Organize data by date, region, or other dimensions
- **Caching**: Reuse intermediate results across transformations
- **Broadcast joins**: For small dimension tables in Spark

### Loading Optimization

- **Bulk loading**: Use database-specific bulk load utilities
- **Batch inserts**: Group records into larger batches
- **Disable indexes**: Drop and rebuild for large loads
- **Parallel writes**: Write to multiple partitions simultaneously
- **Upsert optimization**: Use MERGE statements or staging tables

## Data Quality Framework

### Validation Checks

| Check Type | Purpose | Example |
|------------|---------|----------|
| Schema validation | Ensure expected columns and types | Column 'revenue' exists and is numeric |
| Completeness | Check for required fields | No nulls in 'customer_id' |
| Uniqueness | Verify primary keys | 'order_id' has no duplicates |
| Referential integrity | Validate foreign keys | All 'customer_id' exist in customer table |
| Range validation | Check value boundaries | 'age' between 0 and 120 |
| Format validation | Verify patterns | 'email' matches email regex |
| Consistency | Cross-field validation | 'end_date' >= 'start_date' |
| Volume validation | Detect anomalies | Record count within 20% of average |

### Quality Check Implementation

**Great Expectations framework:**
- Define expectations (assertions about data)
- Run validation suites in pipeline
- Generate data quality reports
- Fail pipeline or alert on violations

**dbt tests:**
- Built-in tests (unique, not_null, accepted_values, relationships)
- Custom SQL-based tests
- Run as part of transformation workflow

## Security and Compliance

### Data Protection

- **Encryption in transit**: TLS/SSL for all data transfers
- **Encryption at rest**: Encrypt sensitive data in storage
- **PII handling**: Tokenization, masking, or hashing of personal data
- **Access control**: Role-based permissions for pipeline resources
- **Secrets management**: Use vaults (AWS Secrets Manager, HashiCorp Vault)

### Compliance Considerations

- **Data lineage**: Track data origin and transformations for audits
- **Retention policies**: Implement data lifecycle management
- **Right to deletion**: Support GDPR/CCPA deletion requests
- **Audit logging**: Record all data access and modifications
- **Data classification**: Tag and handle data by sensitivity level

## Testing Strategies

### Unit Testing

- Test individual transformation functions
- Mock data sources and targets
- Validate business logic correctness
- Use pytest, unittest, or language-specific frameworks

### Integration Testing

- Test end-to-end pipeline with sample data
- Validate data flow through all stages
- Check integration with actual systems (dev/staging)
- Verify error handling and retry logic

### Data Testing

- Compare output against expected results
- Validate row counts and aggregations
- Check data quality metrics
- Test edge cases and boundary conditions

## Deployment and CI/CD

### Version Control

- Store all pipeline code in Git
- Use branching strategy (feature branches, main/production)
- Code review process for changes
- Tag releases for production deployments

### Continuous Integration

- Automated testing on commits
- Linting and code quality checks
- Build and package pipeline artifacts
- Integration tests in isolated environment

### Continuous Deployment

- Deploy to dev/staging environments automatically
- Manual approval for production deployments
- Blue-green or canary deployments for zero downtime
- Rollback capability for failed deployments

## Using the Reference Files

### When to Read Each Reference

**`/references/etl-fundamentals.md`** — Read when you need deep understanding of ETL concepts, batch vs. streaming processing models, data pipeline patterns, extraction methods, transformation techniques, loading strategies, or when designing your first pipeline.

**`/references/pipeline-architecture.md`** — Read when designing pipeline architecture, choosing between ETL/ELT/CDC patterns, implementing Lambda or Kappa architectures, designing for scalability and fault tolerance, or planning data flow and staging strategies.

**`/references/tools-platforms.md`** — Read when selecting tools and technologies, comparing orchestration platforms (Airflow, Prefect, Dagster), choosing processing engines (Spark, Flink, dbt), evaluating data integration tools (Airbyte, Fivetran), or working with cloud-native services (AWS Glue, Azure Data Factory, Google Dataflow).

**`/references/best-practices-optimization.md`** — Read when optimizing pipeline performance, implementing data quality frameworks, designing error handling and retry logic, setting up monitoring and alerting, ensuring security and compliance, or troubleshooting common pipeline issues.

## References

- [Best Practices Optimization](references/best-practices-optimization.md)
- [Etl Fundamentals](references/etl-fundamentals.md)
- [Pipeline Architecture](references/pipeline-architecture.md)
- [Tools Platforms](references/tools-platforms.md)
