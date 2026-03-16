# BigQuery Integration for Google Analytics 4

Leverage BigQuery for advanced GA4 data analysis and custom reporting.

## Overview

GA4 offers free daily export of raw event data to Google BigQuery, enabling SQL-based analysis, custom reporting, and machine learning applications. This integration provides access to unsampled data with full event-level detail.

## Setup and Configuration

### Enable BigQuery Export

1. Navigate to Admin > Property > BigQuery Links
2. Click "Link" and select or create BigQuery project
3. Choose export options:
   - **Daily Export**: Free, exports once per day
   - **Streaming Export**: Real-time export (requires BigQuery subscription)
   - **Include Advertising Identifiers**: Optional, for remarketing
4. Select dataset location (must match GA4 property location)
5. Confirm and enable export

### Dataset Structure

GA4 creates tables in BigQuery:
- `events_YYYYMMDD`: Daily event tables
- `events_intraday_YYYYMMDD`: Intraday tables (updated throughout day)
- `events_*`: Wildcard for querying all dates

## Schema Overview

### Event Table Structure

```sql
SELECT
  event_date,           -- Date in YYYYMMDD format
  event_timestamp,      -- Microseconds since epoch
  event_name,           -- Name of the event
  event_params,         -- Array of event parameters
  user_id,              -- User ID (if set)
  user_pseudo_id,       -- Client ID
  user_properties,      -- Array of user properties
  device,               -- Device information struct
  geo,                  -- Geographic information struct
  traffic_source,       -- Acquisition source struct
  ecommerce,            -- E-commerce data struct
  items                 -- Array of items (e-commerce)
FROM
  `project.dataset.events_*`
WHERE
  _TABLE_SUFFIX BETWEEN '20260301' AND '20260315'
```

### Key Fields

**Event Parameters** (ARRAY of STRUCT):
```sql
event_params.key        -- Parameter name
event_params.value.string_value
event_params.value.int_value
event_params.value.float_value
event_params.value.double_value
```

**User Properties** (ARRAY of STRUCT):
```sql
user_properties.key     -- Property name
user_properties.value.string_value
user_properties.value.int_value
user_properties.value.float_value
user_properties.value.set_timestamp_micros
```

**Device** (STRUCT):
```sql
device.category         -- mobile, desktop, tablet
device.mobile_brand_name
device.mobile_model_name
device.operating_system
device.browser
device.language
```

**Geo** (STRUCT):
```sql
geo.continent
geo.country
geo.region
geo.city
```

**Traffic Source** (STRUCT):
```sql
traffic_source.source
traffic_source.medium
traffic_source.name     -- Campaign name
```

## Common SQL Queries

### Basic Event Analysis

**Count Events by Type**:
```sql
SELECT
  event_name,
  COUNT(*) as event_count
FROM
  `project.dataset.events_*`
WHERE
  _TABLE_SUFFIX BETWEEN '20260301' AND '20260315'
GROUP BY
  event_name
ORDER BY
  event_count DESC
```

**Daily Active Users**:
```sql
SELECT
  event_date,
  COUNT(DISTINCT user_pseudo_id) as daily_active_users
FROM
  `project.dataset.events_*`
WHERE
  _TABLE_SUFFIX BETWEEN '20260301' AND '20260315'
GROUP BY
  event_date
ORDER BY
  event_date
```

### Parameter Extraction

**Extract Specific Event Parameter**:
```sql
SELECT
  user_pseudo_id,
  event_name,
  (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'page_location') as page_url,
  (SELECT value.int_value FROM UNNEST(event_params) WHERE key = 'engagement_time_msec') as engagement_time
FROM
  `project.dataset.events_*`
WHERE
  _TABLE_SUFFIX = FORMAT_DATE('%Y%m%d', CURRENT_DATE())
  AND event_name = 'page_view'
LIMIT 1000
```

**Create Helper Function for Parameters**:
```sql
CREATE TEMP FUNCTION get_param_value(params ARRAY<STRUCT<key STRING, value STRUCT<string_value STRING, int_value INT64, float_value FLOAT64, double_value FLOAT64>>>, param_key STRING)
RETURNS STRING AS (
  (SELECT value.string_value FROM UNNEST(params) WHERE key = param_key)
);

SELECT
  event_name,
  get_param_value(event_params, 'page_title') as page_title,
  get_param_value(event_params, 'page_location') as page_url
FROM
  `project.dataset.events_*`
WHERE
  _TABLE_SUFFIX = FORMAT_DATE('%Y%m%d', CURRENT_DATE())
  AND event_name = 'page_view'
LIMIT 100
```

### E-commerce Analysis

**Revenue by Date**:
```sql
SELECT
  event_date,
  COUNT(DISTINCT (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'transaction_id')) as transactions,
  SUM((SELECT value.double_value FROM UNNEST(event_params) WHERE key = 'value')) as revenue
FROM
  `project.dataset.events_*`
WHERE
  _TABLE_SUFFIX BETWEEN '20260301' AND '20260315'
  AND event_name = 'purchase'
GROUP BY
  event_date
ORDER BY
  event_date
```

**Product Performance**:
```sql
SELECT
  item.item_id,
  item.item_name,
  item.item_category,
  SUM(item.quantity) as total_quantity,
  SUM(item.item_revenue) as total_revenue
FROM
  `project.dataset.events_*`,
  UNNEST(items) as item
WHERE
  _TABLE_SUFFIX BETWEEN '20260301' AND '20260315'
  AND event_name = 'purchase'
GROUP BY
  item.item_id,
  item.item_name,
  item.item_category
ORDER BY
  total_revenue DESC
LIMIT 50
```

**Shopping Behavior Funnel**:
```sql
WITH user_events AS (
  SELECT
    user_pseudo_id,
    COUNTIF(event_name = 'view_item') as viewed_items,
    COUNTIF(event_name = 'add_to_cart') as added_to_cart,
    COUNTIF(event_name = 'begin_checkout') as began_checkout,
    COUNTIF(event_name = 'purchase') as purchased
  FROM
    `project.dataset.events_*`
  WHERE
    _TABLE_SUFFIX BETWEEN '20260301' AND '20260315'
  GROUP BY
    user_pseudo_id
)
SELECT
  COUNT(DISTINCT user_pseudo_id) as total_users,
  COUNT(DISTINCT CASE WHEN viewed_items > 0 THEN user_pseudo_id END) as users_viewed,
  COUNT(DISTINCT CASE WHEN added_to_cart > 0 THEN user_pseudo_id END) as users_added_cart,
  COUNT(DISTINCT CASE WHEN began_checkout > 0 THEN user_pseudo_id END) as users_began_checkout,
  COUNT(DISTINCT CASE WHEN purchased > 0 THEN user_pseudo_id END) as users_purchased
FROM
  user_events
```

### User Behavior Analysis

**Session Duration**:
```sql
WITH session_data AS (
  SELECT
    user_pseudo_id,
    (SELECT value.int_value FROM UNNEST(event_params) WHERE key = 'ga_session_id') as session_id,
    MIN(event_timestamp) as session_start,
    MAX(event_timestamp) as session_end
  FROM
    `project.dataset.events_*`
  WHERE
    _TABLE_SUFFIX BETWEEN '20260301' AND '20260315'
  GROUP BY
    user_pseudo_id,
    session_id
)
SELECT
  AVG((session_end - session_start) / 1000000) as avg_session_duration_seconds,
  APPROX_QUANTILES((session_end - session_start) / 1000000, 100)[OFFSET(50)] as median_session_duration
FROM
  session_data
WHERE
  session_id IS NOT NULL
```

**User Retention Cohort**:
```sql
WITH first_visit AS (
  SELECT
    user_pseudo_id,
    MIN(PARSE_DATE('%Y%m%d', event_date)) as cohort_date
  FROM
    `project.dataset.events_*`
  WHERE
    _TABLE_SUFFIX BETWEEN '20260101' AND '20260315'
  GROUP BY
    user_pseudo_id
),
user_activity AS (
  SELECT
    user_pseudo_id,
    PARSE_DATE('%Y%m%d', event_date) as activity_date
  FROM
    `project.dataset.events_*`
  WHERE
    _TABLE_SUFFIX BETWEEN '20260101' AND '20260315'
  GROUP BY
    user_pseudo_id,
    activity_date
)
SELECT
  fv.cohort_date,
  DATE_DIFF(ua.activity_date, fv.cohort_date, DAY) as days_since_first_visit,
  COUNT(DISTINCT ua.user_pseudo_id) as active_users
FROM
  first_visit fv
JOIN
  user_activity ua ON fv.user_pseudo_id = ua.user_pseudo_id
GROUP BY
  fv.cohort_date,
  days_since_first_visit
ORDER BY
  fv.cohort_date,
  days_since_first_visit
```

### Traffic Source Analysis

**Acquisition Performance**:
```sql
SELECT
  traffic_source.source,
  traffic_source.medium,
  COUNT(DISTINCT user_pseudo_id) as users,
  COUNT(DISTINCT (SELECT value.int_value FROM UNNEST(event_params) WHERE key = 'ga_session_id')) as sessions,
  COUNTIF(event_name = 'purchase') as conversions,
  SUM(CASE WHEN event_name = 'purchase' THEN (SELECT value.double_value FROM UNNEST(event_params) WHERE key = 'value') END) as revenue
FROM
  `project.dataset.events_*`
WHERE
  _TABLE_SUFFIX BETWEEN '20260301' AND '20260315'
GROUP BY
  traffic_source.source,
  traffic_source.medium
ORDER BY
  revenue DESC
```

**Landing Page Performance**:
```sql
WITH landing_pages AS (
  SELECT
    user_pseudo_id,
    (SELECT value.int_value FROM UNNEST(event_params) WHERE key = 'ga_session_id') as session_id,
    ARRAY_AGG((SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'page_location') ORDER BY event_timestamp LIMIT 1)[OFFSET(0)] as landing_page
  FROM
    `project.dataset.events_*`
  WHERE
    _TABLE_SUFFIX BETWEEN '20260301' AND '20260315'
    AND event_name = 'page_view'
  GROUP BY
    user_pseudo_id,
    session_id
)
SELECT
  landing_page,
  COUNT(*) as sessions,
  COUNT(DISTINCT user_pseudo_id) as users
FROM
  landing_pages
WHERE
  landing_page IS NOT NULL
GROUP BY
  landing_page
ORDER BY
  sessions DESC
LIMIT 50
```

## Advanced Analysis Techniques

### Attribution Modeling

**Last Non-Direct Click Attribution**:
```sql
WITH user_touchpoints AS (
  SELECT
    user_pseudo_id,
    (SELECT value.int_value FROM UNNEST(event_params) WHERE key = 'ga_session_id') as session_id,
    event_timestamp,
    traffic_source.source,
    traffic_source.medium,
    event_name
  FROM
    `project.dataset.events_*`
  WHERE
    _TABLE_SUFFIX BETWEEN '20260301' AND '20260315'
),
conversions AS (
  SELECT
    user_pseudo_id,
    event_timestamp as conversion_time
  FROM
    user_touchpoints
  WHERE
    event_name = 'purchase'
),
last_touchpoint AS (
  SELECT
    c.user_pseudo_id,
    c.conversion_time,
    ARRAY_AGG(STRUCT(ut.source, ut.medium) ORDER BY ut.event_timestamp DESC LIMIT 1)[OFFSET(0)] as last_touch
  FROM
    conversions c
  JOIN
    user_touchpoints ut ON c.user_pseudo_id = ut.user_pseudo_id AND ut.event_timestamp < c.conversion_time
  WHERE
    NOT (ut.source = 'direct' AND ut.medium = '(none)')
  GROUP BY
    c.user_pseudo_id,
    c.conversion_time
)
SELECT
  last_touch.source,
  last_touch.medium,
  COUNT(*) as attributed_conversions
FROM
  last_touchpoint
GROUP BY
  last_touch.source,
  last_touch.medium
ORDER BY
  attributed_conversions DESC
```

### Predictive Analytics

**Churn Prediction Features**:
```sql
WITH user_metrics AS (
  SELECT
    user_pseudo_id,
    COUNT(DISTINCT PARSE_DATE('%Y%m%d', event_date)) as days_active,
    COUNT(DISTINCT (SELECT value.int_value FROM UNNEST(event_params) WHERE key = 'ga_session_id')) as total_sessions,
    AVG((SELECT value.int_value FROM UNNEST(event_params) WHERE key = 'engagement_time_msec')) as avg_engagement_time,
    COUNTIF(event_name = 'purchase') as purchase_count,
    SUM(CASE WHEN event_name = 'purchase' THEN (SELECT value.double_value FROM UNNEST(event_params) WHERE key = 'value') END) as total_revenue,
    MAX(PARSE_DATE('%Y%m%d', event_date)) as last_active_date
  FROM
    `project.dataset.events_*`
  WHERE
    _TABLE_SUFFIX BETWEEN '20260201' AND '20260315'
  GROUP BY
    user_pseudo_id
)
SELECT
  user_pseudo_id,
  days_active,
  total_sessions,
  avg_engagement_time,
  purchase_count,
  total_revenue,
  DATE_DIFF(CURRENT_DATE(), last_active_date, DAY) as days_since_last_visit,
  CASE
    WHEN DATE_DIFF(CURRENT_DATE(), last_active_date, DAY) > 30 THEN 'Churned'
    WHEN DATE_DIFF(CURRENT_DATE(), last_active_date, DAY) > 14 THEN 'At Risk'
    ELSE 'Active'
  END as user_status
FROM
  user_metrics
```

## Performance Optimization

### Query Optimization Tips

1. **Use Partitioning**: Always filter by `_TABLE_SUFFIX` to limit scanned data
2. **Avoid SELECT ***: Specify only needed columns
3. **Use UNNEST Efficiently**: Extract parameters in subqueries or CTEs
4. **Leverage Clustering**: BigQuery clusters GA4 tables by `user_pseudo_id`
5. **Cache Results**: Use temporary tables for repeated queries

### Cost Management

**Check Query Cost Before Running**:
```sql
-- Use BigQuery UI's query validator to see estimated bytes processed
-- Cost = $5 per TB processed (as of 2026)
```

**Optimize with Materialized Views**:
```sql
CREATE MATERIALIZED VIEW `project.dataset.daily_metrics`
AS
SELECT
  event_date,
  COUNT(DISTINCT user_pseudo_id) as users,
  COUNT(*) as events,
  COUNTIF(event_name = 'purchase') as purchases
FROM
  `project.dataset.events_*`
GROUP BY
  event_date
```

## Integration with Data Studio / Looker Studio

### Connect BigQuery to Looker Studio

1. Open Looker Studio (formerly Data Studio)
2. Create new data source
3. Select BigQuery connector
4. Choose project, dataset, and table/view
5. Configure fields and aggregations
6. Create visualizations

### Custom SQL in Looker Studio

```sql
SELECT
  event_date,
  traffic_source.source,
  COUNT(DISTINCT user_pseudo_id) as users,
  COUNTIF(event_name = 'purchase') as conversions
FROM
  `project.dataset.events_*`
WHERE
  _TABLE_SUFFIX BETWEEN @DS_START_DATE AND @DS_END_DATE
GROUP BY
  event_date,
  traffic_source.source
```

## Machine Learning with BigQuery ML

### Predict Purchase Probability

```sql
-- Create training data
CREATE OR REPLACE TABLE `project.dataset.user_features` AS
WITH user_behavior AS (
  SELECT
    user_pseudo_id,
    COUNT(DISTINCT PARSE_DATE('%Y%m%d', event_date)) as days_active,
    COUNT(DISTINCT (SELECT value.int_value FROM UNNEST(event_params) WHERE key = 'ga_session_id')) as sessions,
    COUNTIF(event_name = 'view_item') as product_views,
    COUNTIF(event_name = 'add_to_cart') as cart_adds,
    COUNTIF(event_name = 'purchase') > 0 as purchased
  FROM
    `project.dataset.events_*`
  WHERE
    _TABLE_SUFFIX BETWEEN '20260201' AND '20260228'
  GROUP BY
    user_pseudo_id
)
SELECT * FROM user_behavior;

-- Train model
CREATE OR REPLACE MODEL `project.dataset.purchase_prediction_model`
OPTIONS(
  model_type='LOGISTIC_REG',
  input_label_cols=['purchased']
) AS
SELECT
  days_active,
  sessions,
  product_views,
  cart_adds,
  purchased
FROM
  `project.dataset.user_features`;

-- Make predictions
SELECT
  user_pseudo_id,
  predicted_purchased,
  predicted_purchased_probs[OFFSET(1)].prob as purchase_probability
FROM
  ML.PREDICT(MODEL `project.dataset.purchase_prediction_model`,
    (SELECT * FROM `project.dataset.user_features`))
ORDER BY
  purchase_probability DESC
LIMIT 1000;
```
