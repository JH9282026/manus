# MLOps Monitoring Dashboards

## Prometheus Metrics

```python
from prometheus_client import Counter, Histogram, Gauge, start_http_server

# Define metrics
predictions_total = Counter('model_predictions_total', 'Total predictions')
prediction_latency = Histogram('model_prediction_latency_seconds', 'Prediction latency')
model_accuracy = Gauge('model_accuracy', 'Current model accuracy')
data_drift_score = Gauge('data_drift_score', 'Data drift score')

# Instrument code
@prediction_latency.time()
def predict(features):
    predictions_total.inc()
    result = model.predict(features)
    return result

# Start metrics server
start_http_server(8000)
```

## Grafana Dashboard Configuration

```json
{
  "dashboard": {
    "title": "ML Model Monitoring",
    "panels": [
      {
        "title": "Prediction Latency",
        "targets": [
          {
            "expr": "rate(model_prediction_latency_seconds_sum[5m]) / rate(model_prediction_latency_seconds_count[5m])"
          }
        ]
      },
      {
        "title": "Predictions per Second",
        "targets": [
          {
            "expr": "rate(model_predictions_total[1m])"
          }
        ]
      }
    ]
  }
}
```
