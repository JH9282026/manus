# Best Practices and Optimization

Advanced techniques, optimization strategies, and best practices for building production-grade ETL pipelines.

---

## Performance Optimization

### Extraction Optimization

**Parallel extraction:**
- Split large tables into chunks
- Extract partitions in parallel
- Use connection pooling to reuse connections

**Example: Parallel extraction by date range**
```python
from concurrent.futures import ThreadPoolExecutor
import pandas as pd

def extract_partition(start_date, end_date):
    query = f"""
        SELECT * FROM sales 
        WHERE order_date >= '{start_date}' 
        AND order_date < '{end_date}'
    """
    return pd.read_sql(query, connection)

# Generate date ranges
date_ranges = [
    ('2024-01-01', '2024-01-08'),
    ('2024-01-08', '2024-01-15'),
    ('2024-01-15', '2024-01-22'),
    # ...
]

# Extract in parallel
with ThreadPoolExecutor(max_workers=5) as executor:
    results = executor.map(lambda r: extract_partition(*r), date_ranges)
    
df = pd.concat(results, ignore_index=True)
```

**Incremental extraction strategies:**

**1. Timestamp-based:**
```sql
SELECT * FROM orders
WHERE updated_at > '2024-01-15 00:00:00'
AND updated_at <= '2024-01-16 00:00:00'
```

**2. Sequence-based:**
```sql
SELECT * FROM orders
WHERE order_id > 1000000
ORDER BY order_id
LIMIT 10000
```

**3. Watermark tracking:**
```python
# Store last extracted value
last_watermark = get_last_watermark('orders', 'updated_at')

# Extract new data
query = f"SELECT * FROM orders WHERE updated_at > '{last_watermark}'"
df = extract_data(query)

# Update watermark
if not df.empty:
    new_watermark = df['updated_at'].max()
    save_watermark('orders', 'updated_at', new_watermark)
```

**Compression during extraction:**
- Compress data before network transfer
- Use gzip, snappy, or lz4 compression
- Balance compression ratio vs. CPU cost

**API extraction optimization:**
- Batch API requests when possible
- Use pagination efficiently (cursor-based preferred)
- Implement exponential backoff for rate limits
- Cache responses when appropriate

### Transformation Optimization

**Pushdown processing:**
- Perform transformations in source/target database when possible
- Leverage database query optimizer
- Reduce data movement

**Example: Pushdown vs. pull-and-transform**
```python
# Bad: Pull all data, then filter
df = pd.read_sql("SELECT * FROM large_table", conn)
df_filtered = df[df['status'] == 'active']

# Good: Filter in database
df = pd.read_sql("SELECT * FROM large_table WHERE status = 'active'", conn)
```

**Spark optimization techniques:**

**1. Avoid shuffles:**
```python
# Bad: Shuffle required
df.repartition(100, 'customer_id').write.parquet('output')

# Good: Use existing partitioning
df.write.partitionBy('date').parquet('output')
```

**2. Broadcast small tables:**
```python
from pyspark.sql.functions import broadcast

# Broadcast small dimension table
df_large.join(broadcast(df_small), 'customer_id')
```

**3. Cache intermediate results:**
```python
df_intermediate = df.filter(col('amount') > 100).cache()

# Use cached dataframe multiple times
df_summary1 = df_intermediate.groupBy('product').sum('amount')
df_summary2 = df_intermediate.groupBy('region').avg('amount')
```

**4. Partition pruning:**
```python
# Ensure partition column in filter
df = spark.read.parquet('s3://bucket/sales')
df_filtered = df.filter(col('date') == '2024-01-15')  # Prunes partitions
```

**Columnar processing:**
- Use columnar formats (Parquet, ORC)
- Read only needed columns
- Leverage column-level compression

**Vectorized operations:**
- Use pandas/numpy vectorized operations instead of loops
- Use Spark's vectorized UDFs (pandas UDFs)

```python
# Bad: Row-by-row processing
for index, row in df.iterrows():
    df.at[index, 'total'] = row['price'] * row['quantity']

# Good: Vectorized operation
df['total'] = df['price'] * df['quantity']
```

### Loading Optimization

**Bulk loading:**
- Use database-specific bulk load utilities
- Much faster than individual inserts

**PostgreSQL COPY:**
```python
import io
import psycopg2

# Create CSV buffer
buffer = io.StringIO()
df.to_csv(buffer, index=False, header=False)
buffer.seek(0)

# Bulk load with COPY
with psycopg2.connect(conn_string) as conn:
    with conn.cursor() as cur:
        cur.copy_from(buffer, 'target_table', sep=',', columns=df.columns)
    conn.commit()
```

**Batch inserts:**
```python
# Bad: One insert per row
for row in data:
    cursor.execute("INSERT INTO table VALUES (%s, %s)", row)

# Good: Batch inserts
cursor.executemany("INSERT INTO table VALUES (%s, %s)", data)
```

**Disable indexes during load:**
```sql
-- Drop indexes
DROP INDEX idx_customer_id;

-- Load data
COPY sales FROM 's3://bucket/sales.csv';

-- Rebuild indexes
CREATE INDEX idx_customer_id ON sales(customer_id);
```

**Parallel writes:**
- Write to multiple partitions simultaneously
- Use Spark's partitioned writes
- Distribute load across database shards

**Upsert optimization:**

**Staging table approach:**
```sql
-- Load to staging table
COPY staging_sales FROM 's3://bucket/sales.csv';

-- Merge to target
MERGE INTO sales t
USING staging_sales s ON t.order_id = s.order_id
WHEN MATCHED THEN UPDATE SET t.amount = s.amount, t.status = s.status
WHEN NOT MATCHED THEN INSERT VALUES (s.order_id, s.amount, s.status);

-- Clean up
TRUNCATE staging_sales;
```

---

## Data Quality Framework

### Data Quality Dimensions

**1. Completeness:**
- All required data is present
- No unexpected nulls
- All expected records exist

**Checks:**
```python
# Check for nulls in required columns
assert df['customer_id'].notna().all(), "Null customer_ids found"

# Check record count
expected_count = get_source_count()
actual_count = len(df)
assert actual_count >= expected_count * 0.95, f"Missing records: {expected_count - actual_count}"
```

**2. Accuracy:**
- Data correctly represents reality
- Values within expected ranges
- Calculations are correct

**Checks:**
```python
# Range validation
assert (df['age'] >= 0).all() and (df['age'] <= 120).all(), "Invalid ages"

# Cross-field validation
assert (df['end_date'] >= df['start_date']).all(), "End date before start date"

# Referential integrity
valid_customers = set(customers_df['customer_id'])
invalid = df[~df['customer_id'].isin(valid_customers)]
assert len(invalid) == 0, f"Invalid customer_ids: {invalid['customer_id'].tolist()}"
```

**3. Consistency:**
- Data is consistent across systems
- No contradictions
- Standardized formats

**Checks:**
```python
# Format consistency
assert df['email'].str.match(r'^[\w\.-]+@[\w\.-]+\.\w+$').all(), "Invalid email formats"

# Value consistency
assert df['country'].isin(['US', 'CA', 'UK', 'DE']).all(), "Invalid country codes"
```

**4. Timeliness:**
- Data is up-to-date
- Delivered within SLA
- Freshness requirements met

**Checks:**
```python
from datetime import datetime, timedelta

# Check data freshness
max_date = df['updated_at'].max()
age = datetime.now() - max_date
assert age < timedelta(hours=24), f"Data is {age} old, exceeds 24h SLA"
```

**5. Uniqueness:**
- No unexpected duplicates
- Primary keys are unique

**Checks:**
```python
# Check for duplicates
duplicates = df[df.duplicated(subset=['order_id'], keep=False)]
assert len(duplicates) == 0, f"Found {len(duplicates)} duplicate order_ids"
```

### Great Expectations Framework

**Overview:**
- Python library for data validation
- Declarative expectations (assertions)
- Automatic documentation
- Integration with pipelines

**Example expectations:**
```python
import great_expectations as ge

# Create expectation suite
df_ge = ge.from_pandas(df)

# Define expectations
df_ge.expect_column_values_to_not_be_null('customer_id')
df_ge.expect_column_values_to_be_unique('order_id')
df_ge.expect_column_values_to_be_between('amount', min_value=0, max_value=1000000)
df_ge.expect_column_values_to_match_regex('email', r'^[\w\.-]+@[\w\.-]+\.\w+$')
df_ge.expect_column_values_to_be_in_set('status', ['pending', 'completed', 'cancelled'])

# Validate
results = df_ge.validate()

if not results['success']:
    # Handle validation failure
    raise ValueError(f"Data quality check failed: {results}")
```

**Expectation suite in YAML:**
```yaml
expectations:
  - expectation_type: expect_table_row_count_to_be_between
    kwargs:
      min_value: 1000
      max_value: 1000000
  
  - expectation_type: expect_column_values_to_not_be_null
    kwargs:
      column: customer_id
  
  - expectation_type: expect_column_values_to_be_unique
    kwargs:
      column: order_id
  
  - expectation_type: expect_column_mean_to_be_between
    kwargs:
      column: amount
      min_value: 50
      max_value: 500
```

### Anomaly Detection

**Statistical anomaly detection:**
```python
import numpy as np

# Detect outliers using IQR method
Q1 = df['amount'].quantile(0.25)
Q3 = df['amount'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df['amount'] < lower_bound) | (df['amount'] > upper_bound)]

if len(outliers) > len(df) * 0.01:  # More than 1% outliers
    alert(f"Unusual number of outliers: {len(outliers)}")
```

**Volume anomaly detection:**
```python
# Compare with historical average
historical_avg = get_historical_row_count_avg('sales', days=30)
current_count = len(df)

if current_count < historical_avg * 0.8 or current_count > historical_avg * 1.2:
    alert(f"Unusual row count: {current_count} vs avg {historical_avg}")
```

**Schema drift detection:**
```python
# Compare current schema with expected
expected_columns = {'order_id', 'customer_id', 'amount', 'status', 'order_date'}
actual_columns = set(df.columns)

missing = expected_columns - actual_columns
extra = actual_columns - expected_columns

if missing:
    raise ValueError(f"Missing columns: {missing}")
if extra:
    alert(f"Unexpected columns: {extra}")
```

---

## Error Handling and Reliability

### Retry Strategies

**Exponential backoff with jitter:**
```python
import time
import random

def retry_with_backoff(func, max_retries=5, base_delay=1):
    for attempt in range(max_retries):
        try:
            return func()
        except TransientError as e:
            if attempt == max_retries - 1:
                raise
            
            # Exponential backoff with jitter
            delay = base_delay * (2 ** attempt) + random.uniform(0, 1)
            print(f"Attempt {attempt + 1} failed, retrying in {delay:.2f}s")
            time.sleep(delay)
        except PermanentError as e:
            # Don't retry permanent errors
            raise
```

**Retry with different strategies:**
```python
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

@retry(
    stop=stop_after_attempt(5),
    wait=wait_exponential(multiplier=1, min=1, max=60),
    retry=retry_if_exception_type(TransientError)
)
def extract_data():
    # Extraction logic
    pass
```

### Dead Letter Queue Pattern

**Implementation:**
```python
import json
from datetime import datetime

def process_records(records):
    successful = []
    failed = []
    
    for record in records:
        try:
            processed = transform(record)
            successful.append(processed)
        except Exception as e:
            # Add to dead letter queue
            failed.append({
                'record': record,
                'error': str(e),
                'timestamp': datetime.now().isoformat(),
                'pipeline': 'sales_etl',
            })
    
    # Load successful records
    if successful:
        load_to_target(successful)
    
    # Write failed records to DLQ
    if failed:
        with open(f's3://bucket/dlq/{datetime.now().date()}.json', 'a') as f:
            for record in failed:
                f.write(json.dumps(record) + '\n')
        
        # Alert if too many failures
        if len(failed) > len(records) * 0.05:  # More than 5% failed
            send_alert(f"High failure rate: {len(failed)}/{len(records)}")
```

### Circuit Breaker Pattern

**Implementation:**
```python
from enum import Enum
import time

class CircuitState(Enum):
    CLOSED = 1
    OPEN = 2
    HALF_OPEN = 3

class CircuitBreaker:
    def __init__(self, failure_threshold=5, timeout=60, success_threshold=2):
        self.failure_threshold = failure_threshold
        self.timeout = timeout
        self.success_threshold = success_threshold
        self.failure_count = 0
        self.success_count = 0
        self.last_failure_time = None
        self.state = CircuitState.CLOSED
    
    def call(self, func, *args, **kwargs):
        if self.state == CircuitState.OPEN:
            if time.time() - self.last_failure_time > self.timeout:
                self.state = CircuitState.HALF_OPEN
                self.success_count = 0
            else:
                raise Exception("Circuit breaker is OPEN")
        
        try:
            result = func(*args, **kwargs)
            self._on_success()
            return result
        except Exception as e:
            self._on_failure()
            raise e
    
    def _on_success(self):
        if self.state == CircuitState.HALF_OPEN:
            self.success_count += 1
            if self.success_count >= self.success_threshold:
                self.state = CircuitState.CLOSED
                self.failure_count = 0
        else:
            self.failure_count = 0
    
    def _on_failure(self):
        self.failure_count += 1
        self.last_failure_time = time.time()
        
        if self.failure_count >= self.failure_threshold:
            self.state = CircuitState.OPEN

# Usage
breaker = CircuitBreaker()

try:
    data = breaker.call(extract_from_api, url='https://api.example.com/data')
except Exception as e:
    # Use fallback or cached data
    data = get_cached_data()
```

---

## Monitoring and Observability

### Key Metrics to Track

**Pipeline execution metrics:**
- Execution duration (total and per task)
- Success/failure rate
- Retry count
- Queue depth (for streaming)

**Data metrics:**
- Records processed
- Bytes transferred
- Data quality score
- Schema changes detected

**Resource metrics:**
- CPU utilization
- Memory usage
- Disk I/O
- Network throughput

**Business metrics:**
- Data freshness (time since last update)
- SLA compliance
- Cost per pipeline run
- Data coverage (% of expected data received)

### Logging Best Practices

**Structured logging:**
```python
import logging
import json

class StructuredLogger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
    
    def log(self, level, message, **kwargs):
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'level': level,
            'message': message,
            **kwargs
        }
        self.logger.log(getattr(logging, level), json.dumps(log_entry))

# Usage
logger = StructuredLogger('sales_etl')

logger.log('INFO', 'Starting extraction', 
           pipeline='sales_etl', 
           source='postgres', 
           table='orders')

logger.log('INFO', 'Extraction complete', 
           pipeline='sales_etl', 
           records_extracted=10000, 
           duration_seconds=45.2)
```

**Log levels:**
- **DEBUG**: Detailed diagnostic information
- **INFO**: General informational messages (start, complete, counts)
- **WARNING**: Unexpected but handled situations (retries, fallbacks)
- **ERROR**: Errors that don't stop the pipeline
- **CRITICAL**: Errors that stop the pipeline

**What to log:**
- Pipeline start and end
- Each stage (extract, transform, load) start and end
- Record counts at each stage
- Data quality check results
- Errors and exceptions with context
- Performance metrics (duration, throughput)

### Alerting Strategy

**Alert on:**
- Pipeline failures
- SLA violations (data freshness, processing time)
- Data quality threshold breaches
- Unusual data volumes (too high or too low)
- High error rates
- Resource exhaustion

**Alert channels:**
- Email for non-urgent issues
- Slack/Teams for team awareness
- PagerDuty for critical issues requiring immediate action

**Alert example:**
```python
def check_and_alert(df, pipeline_name):
    issues = []
    
    # Check data volume
    expected_min = 1000
    if len(df) < expected_min:
        issues.append(f"Low record count: {len(df)} < {expected_min}")
    
    # Check data quality
    null_rate = df['customer_id'].isna().sum() / len(df)
    if null_rate > 0.01:  # More than 1% nulls
        issues.append(f"High null rate in customer_id: {null_rate:.2%}")
    
    # Check freshness
    max_date = df['order_date'].max()
    age = datetime.now().date() - max_date
    if age.days > 1:
        issues.append(f"Stale data: most recent order is {age.days} days old")
    
    if issues:
        send_alert(
            title=f"Data Quality Issues in {pipeline_name}",
            message='\n'.join(issues),
            severity='warning'
        )
```

---

## Security and Compliance

### Secrets Management

**Never hardcode credentials:**
```python
# Bad
conn = psycopg2.connect(
    host='db.example.com',
    user='admin',
    password='hardcoded_password'  # NEVER DO THIS
)

# Good: Use environment variables
import os
conn = psycopg2.connect(
    host=os.environ['DB_HOST'],
    user=os.environ['DB_USER'],
    password=os.environ['DB_PASSWORD']
)

# Better: Use secrets manager
import boto3

def get_secret(secret_name):
    client = boto3.client('secretsmanager')
    response = client.get_secret_value(SecretId=secret_name)
    return json.loads(response['SecretString'])

db_creds = get_secret('prod/database/credentials')
conn = psycopg2.connect(**db_creds)
```

### Data Encryption

**Encryption in transit:**
- Use TLS/SSL for all connections
- Verify certificates
- Use VPN or private networks when possible

**Encryption at rest:**
```python
# S3 server-side encryption
s3_client.put_object(
    Bucket='my-bucket',
    Key='data/sales.parquet',
    Body=data,
    ServerSideEncryption='AES256'  # or 'aws:kms'
)

# Snowflake encryption (automatic)
# All data encrypted by default
```

### PII Handling

**Tokenization:**
```python
import hashlib

def tokenize_pii(value, salt):
    """One-way hash for PII"""
    return hashlib.sha256(f"{value}{salt}".encode()).hexdigest()

# Tokenize email addresses
df['email_token'] = df['email'].apply(lambda x: tokenize_pii(x, SECRET_SALT))
df = df.drop('email', axis=1)  # Remove original PII
```

**Masking:**
```python
def mask_credit_card(cc_number):
    """Mask all but last 4 digits"""
    return '*' * (len(cc_number) - 4) + cc_number[-4:]

df['cc_masked'] = df['credit_card'].apply(mask_credit_card)
```

**Data classification:**
```python
# Tag columns by sensitivity
COLUMN_CLASSIFICATION = {
    'customer_id': 'public',
    'email': 'pii',
    'ssn': 'sensitive_pii',
    'credit_card': 'sensitive_pii',
    'order_amount': 'public',
}

# Apply appropriate handling based on classification
for col, classification in COLUMN_CLASSIFICATION.items():
    if classification == 'sensitive_pii':
        df[col] = df[col].apply(encrypt_field)
    elif classification == 'pii':
        df[col] = df[col].apply(tokenize_pii)
```

### Audit Logging

**Track data access:**
```python
def log_data_access(user, table, action, row_count):
    audit_log = {
        'timestamp': datetime.now().isoformat(),
        'user': user,
        'table': table,
        'action': action,
        'row_count': row_count,
        'ip_address': get_client_ip(),
    }
    
    # Write to audit log table
    write_to_audit_log(audit_log)

# Usage
df = extract_customer_data()
log_data_access(
    user=current_user,
    table='customers',
    action='extract',
    row_count=len(df)
)
```

---

## Testing Strategies

### Unit Testing

**Test transformation functions:**
```python
import pytest
import pandas as pd

def clean_phone_number(phone):
    """Remove non-numeric characters from phone number"""
    return ''.join(c for c in phone if c.isdigit())

def test_clean_phone_number():
    assert clean_phone_number('(555) 123-4567') == '5551234567'
    assert clean_phone_number('555.123.4567') == '5551234567'
    assert clean_phone_number('5551234567') == '5551234567'

def test_calculate_total():
    df = pd.DataFrame({
        'price': [10.0, 20.0, 30.0],
        'quantity': [2, 3, 1]
    })
    
    result = calculate_total(df)
    expected = pd.Series([20.0, 60.0, 30.0])
    
    pd.testing.assert_series_equal(result, expected)
```

### Integration Testing

**Test end-to-end pipeline:**
```python
import pytest
from unittest.mock import Mock, patch

@pytest.fixture
def test_database():
    # Set up test database
    conn = create_test_db()
    load_test_data(conn)
    yield conn
    # Tear down
    conn.close()

def test_sales_pipeline(test_database):
    # Run pipeline with test data
    result = run_sales_pipeline(
        source=test_database,
        target='test_warehouse'
    )
    
    # Verify results
    assert result['status'] == 'success'
    assert result['records_processed'] == 100
    
    # Verify data in target
    target_data = read_from_target('test_warehouse', 'sales')
    assert len(target_data) == 100
    assert target_data['total_amount'].sum() == 15000.0
```

### Data Testing

**Compare output with expected:**
```python
def test_aggregation_logic():
    # Input data
    input_df = pd.DataFrame({
        'date': ['2024-01-01', '2024-01-01', '2024-01-02'],
        'product': ['A', 'B', 'A'],
        'amount': [100, 200, 150]
    })
    
    # Expected output
    expected_df = pd.DataFrame({
        'date': ['2024-01-01', '2024-01-02'],
        'total_amount': [300, 150]
    })
    
    # Run transformation
    result_df = aggregate_daily_sales(input_df)
    
    # Compare
    pd.testing.assert_frame_equal(
        result_df.sort_values('date').reset_index(drop=True),
        expected_df.sort_values('date').reset_index(drop=True)
    )
```

---

## CI/CD for Data Pipelines

### Version Control

**What to version control:**
- Pipeline code (DAGs, scripts)
- SQL queries and dbt models
- Configuration files
- Schema definitions
- Test cases
- Documentation

**What NOT to version control:**
- Credentials and secrets
- Large data files
- Temporary files
- Environment-specific configs (use templates instead)

### Continuous Integration

**GitHub Actions example:**
```yaml
name: ETL Pipeline CI

on:
  pull_request:
    branches: [main]
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v2
      
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest pytest-cov
      
      - name: Run linting
        run: |
          pip install flake8
          flake8 pipelines/ --max-line-length=100
      
      - name: Run unit tests
        run: |
          pytest tests/unit --cov=pipelines
      
      - name: Run integration tests
        run: |
          pytest tests/integration
      
      - name: Validate DAGs
        run: |
          python -m pipelines.validate_dags
```

### Continuous Deployment

**Deployment stages:**
1. **Dev**: Automatic deployment on commit to dev branch
2. **Staging**: Automatic deployment on merge to main
3. **Production**: Manual approval required

**Deployment script:**
```bash
#!/bin/bash

ENVIRONMENT=$1  # dev, staging, prod

# Validate environment
if [[ ! "$ENVIRONMENT" =~ ^(dev|staging|prod)$ ]]; then
    echo "Invalid environment: $ENVIRONMENT"
    exit 1
fi

# Run tests
pytest tests/
if [ $? -ne 0 ]; then
    echo "Tests failed, aborting deployment"
    exit 1
fi

# Deploy DAGs to Airflow
rsync -av dags/ airflow@${ENVIRONMENT}-airflow:/opt/airflow/dags/

# Deploy dbt models
cd dbt_project
dbt deps
dbt run --target ${ENVIRONMENT}

# Smoke test
python scripts/smoke_test.py --env ${ENVIRONMENT}

echo "Deployment to ${ENVIRONMENT} complete"
```
