# Model Evaluation, Deployment, and Production Best Practices

## Introduction

Building accurate forecasting models is only half the battle. To deliver business value, models must be properly evaluated, deployed to production, monitored continuously, and maintained over time. This guide covers the complete lifecycle from model validation through production deployment and ongoing management.

## Comprehensive Model Evaluation

### Beyond Basic Metrics

While MAE, RMSE, and MAPE are important, comprehensive evaluation requires multiple perspectives:

#### 1. Accuracy Metrics

**Mean Absolute Error (MAE)**:
```python
MAE = np.mean(np.abs(actual - predicted))
```
- **Interpretation**: Average magnitude of errors in original units
- **Use When**: Easy interpretation needed, outliers shouldn't dominate
- **Limitation**: Doesn't penalize large errors heavily

**Root Mean Squared Error (RMSE)**:
```python
RMSE = np.sqrt(np.mean((actual - predicted)**2))
```
- **Interpretation**: Standard deviation of prediction errors
- **Use When**: Large errors are particularly costly
- **Limitation**: Sensitive to outliers

**Mean Absolute Percentage Error (MAPE)**:
```python
MAPE = np.mean(np.abs((actual - predicted) / actual)) * 100
```
- **Interpretation**: Average percentage error
- **Use When**: Comparing across different scales
- **Limitation**: Undefined for zero values, asymmetric

**Weighted MAPE (wMAPE)**:
```python
wMAPE = np.sum(np.abs(actual - predicted)) / np.sum(np.abs(actual)) * 100
```
- **Interpretation**: Percentage error weighted by actual values
- **Use When**: Avoiding division by small numbers
- **Advantage**: More stable than MAPE

#### 2. Bias Metrics

**Mean Error (Bias)**:
```python
bias = np.mean(predicted - actual)
```
- **Positive**: Systematic over-forecasting
- **Negative**: Systematic under-forecasting
- **Zero**: Unbiased (but may still have large errors)

**Mean Percentage Error (MPE)**:
```python
MPE = np.mean((predicted - actual) / actual) * 100
```
- Shows direction and magnitude of bias as percentage

**Tracking Signal**:
```python
cumulative_error = np.cumsum(actual - predicted)
MAD = np.mean(np.abs(actual - predicted))
tracking_signal = cumulative_error / MAD
```
- **Interpretation**: Cumulative bias relative to average error
- **Rule of Thumb**: Values beyond ±4 indicate significant bias
- **Use**: Monitor for systematic forecast drift

#### 3. Scale-Independent Metrics

**Mean Absolute Scaled Error (MASE)**:
```python
# For non-seasonal data
naive_mae = np.mean(np.abs(np.diff(actual_train)))
MASE = MAE / naive_mae
```
- **Interpretation**: Error relative to naive forecast
- **MASE < 1**: Better than naive
- **MASE > 1**: Worse than naive
- **Advantage**: Works with zero values, symmetric

#### 4. Directional Accuracy

**Prediction of Change Direction**:
```python
def directional_accuracy(actual, predicted):
    actual_direction = np.sign(np.diff(actual))
    predicted_direction = np.sign(np.diff(predicted))
    correct = (actual_direction == predicted_direction).sum()
    return correct / len(actual_direction) * 100

dir_acc = directional_accuracy(actual, predicted)
print(f"Directional Accuracy: {dir_acc:.1f}%")
```
- **Use Case**: When direction matters more than magnitude (e.g., stock prices)

### Forecast Horizon Analysis

Accuracy typically degrades with longer forecast horizons.

```python
def evaluate_by_horizon(actual, predictions_dict):
    """
    Evaluate accuracy at different forecast horizons
    
    predictions_dict: {horizon: predictions}
    e.g., {1: one_step_ahead, 7: seven_steps_ahead}
    """
    results = []
    
    for horizon, preds in predictions_dict.items():
        mae = mean_absolute_error(actual[:len(preds)], preds)
        rmse = np.sqrt(mean_squared_error(actual[:len(preds)], preds))
        
        results.append({
            'Horizon': horizon,
            'MAE': mae,
            'RMSE': rmse
        })
    
    return pd.DataFrame(results)

# Example usage
horizons = {1: h1_preds, 7: h7_preds, 30: h30_preds}
results = evaluate_by_horizon(test_actual, horizons)
print(results)

# Visualize
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
plt.plot(results['Horizon'], results['RMSE'], marker='o')
plt.xlabel('Forecast Horizon (days)')
plt.ylabel('RMSE')
plt.title('Forecast Accuracy by Horizon')
plt.grid(True)
plt.show()
```

### Residual Analysis

**Comprehensive Residual Diagnostics**:
```python
import scipy.stats as stats
from statsmodels.graphics.tsaplots import plot_acf

def analyze_residuals(actual, predicted):
    residuals = actual - predicted
    
    fig, axes = plt.subplots(2, 3, figsize=(18, 10))
    
    # 1. Residuals over time
    axes[0, 0].plot(residuals)
    axes[0, 0].axhline(y=0, color='r', linestyle='--')
    axes[0, 0].set_title('Residuals Over Time')
    axes[0, 0].set_xlabel('Time')
    axes[0, 0].set_ylabel('Residual')
    
    # 2. Histogram
    axes[0, 1].hist(residuals, bins=30, edgecolor='black')
    axes[0, 1].set_title('Residual Distribution')
    axes[0, 1].set_xlabel('Residual')
    axes[0, 1].set_ylabel('Frequency')
    
    # 3. Q-Q plot
    stats.probplot(residuals, dist="norm", plot=axes[0, 2])
    axes[0, 2].set_title('Q-Q Plot')
    
    # 4. Residuals vs Fitted
    axes[1, 0].scatter(predicted, residuals, alpha=0.5)
    axes[1, 0].axhline(y=0, color='r', linestyle='--')
    axes[1, 0].set_title('Residuals vs Fitted Values')
    axes[1, 0].set_xlabel('Fitted Values')
    axes[1, 0].set_ylabel('Residuals')
    
    # 5. ACF of residuals
    plot_acf(residuals, lags=40, ax=axes[1, 1])
    axes[1, 1].set_title('ACF of Residuals')
    
    # 6. Scale-location plot
    standardized_residuals = residuals / np.std(residuals)
    axes[1, 2].scatter(predicted, np.sqrt(np.abs(standardized_residuals)), alpha=0.5)
    axes[1, 2].set_title('Scale-Location Plot')
    axes[1, 2].set_xlabel('Fitted Values')
    axes[1, 2].set_ylabel('√|Standardized Residuals|')
    
    plt.tight_layout()
    plt.show()
    
    # Statistical tests
    print("=== Residual Analysis ===")
    print(f"Mean: {np.mean(residuals):.4f} (should be ~0)")
    print(f"Std Dev: {np.std(residuals):.4f}")
    
    # Normality test
    _, p_value = stats.shapiro(residuals[:5000])  # Shapiro-Wilk test
    print(f"\nShapiro-Wilk Test p-value: {p_value:.4f}")
    if p_value > 0.05:
        print("Residuals appear normally distributed")
    else:
        print("Residuals may not be normally distributed")
    
    # Ljung-Box test for autocorrelation
    from statsmodels.stats.diagnostic import acorr_ljungbox
    lb_test = acorr_ljungbox(residuals, lags=[10], return_df=True)
    print(f"\nLjung-Box Test p-value: {lb_test['lb_pvalue'].values[0]:.4f}")
    if lb_test['lb_pvalue'].values[0] > 0.05:
        print("No significant autocorrelation in residuals")
    else:
        print("Significant autocorrelation detected in residuals")

analyze_residuals(test_actual, predictions)
```

**What to Look For**:
- **Random scatter**: Residuals should show no patterns
- **Zero mean**: No systematic bias
- **Constant variance**: Homoscedasticity (no funnel shape)
- **Normal distribution**: For valid confidence intervals
- **No autocorrelation**: Independent errors

### Cross-Validation Strategies

**Time Series Cross-Validation**:
```python
from sklearn.model_selection import TimeSeriesSplit

def time_series_cv(X, y, model, n_splits=5):
    tscv = TimeSeriesSplit(n_splits=n_splits)
    
    scores = {'mae': [], 'rmse': [], 'mape': []}
    
    for fold, (train_idx, test_idx) in enumerate(tscv.split(X)):
        X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
        y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]
        
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        
        scores['mae'].append(mean_absolute_error(y_test, predictions))
        scores['rmse'].append(np.sqrt(mean_squared_error(y_test, predictions)))
        mape = np.mean(np.abs((y_test - predictions) / y_test)) * 100
        scores['mape'].append(mape)
        
        print(f"Fold {fold + 1}: MAE={scores['mae'][-1]:.2f}, "
              f"RMSE={scores['rmse'][-1]:.2f}, MAPE={scores['mape'][-1]:.2f}%")
    
    print(f"\nAverage: MAE={np.mean(scores['mae']):.2f}, "
          f"RMSE={np.mean(scores['rmse']):.2f}, MAPE={np.mean(scores['mape']):.2f}%")
    
    return scores

scores = time_series_cv(X, y, model, n_splits=5)
```

**Blocked Cross-Validation** (for seasonal data):
```python
def blocked_cv(X, y, model, block_size=12, n_splits=5):
    """
    Cross-validation with blocked folds to preserve seasonal structure
    """
    n = len(X)
    fold_size = n // (n_splits + 1)
    
    scores = []
    
    for i in range(n_splits):
        train_end = fold_size * (i + 1)
        test_start = train_end
        test_end = test_start + fold_size
        
        X_train, y_train = X[:train_end], y[:train_end]
        X_test, y_test = X[test_start:test_end], y[test_start:test_end]
        
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        
        rmse = np.sqrt(mean_squared_error(y_test, predictions))
        scores.append(rmse)
        print(f"Fold {i+1}: RMSE={rmse:.2f}")
    
    print(f"\nAverage RMSE: {np.mean(scores):.2f}")
    return scores
```

## Model Deployment

### Deployment Architecture

**Common Deployment Patterns**:

1. **Batch Prediction**:
   - Generate forecasts on schedule (daily, weekly)
   - Store results in database
   - Suitable for: Inventory planning, capacity planning

2. **Real-Time API**:
   - On-demand predictions via REST API
   - Low latency requirements
   - Suitable for: Dynamic pricing, recommendation systems

3. **Streaming**:
   - Continuous prediction on data streams
   - Near real-time updates
   - Suitable for: Fraud detection, monitoring systems

### Model Serialization

**Saving Models**:
```python
import joblib
import pickle

# Scikit-learn models
joblib.dump(model, 'model.pkl')

# Alternative: pickle
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

# TensorFlow/Keras models
model.save('model.h5')
# or
model.save('model_directory/')  # SavedModel format

# PyTorch models
torch.save(model.state_dict(), 'model.pth')
```

**Loading Models**:
```python
# Scikit-learn
model = joblib.load('model.pkl')

# TensorFlow/Keras
from tensorflow import keras
model = keras.models.load_model('model.h5')

# PyTorch
model = MyModelClass()
model.load_state_dict(torch.load('model.pth'))
model.eval()
```

### REST API Deployment with Flask

```python
from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load model at startup
model = joblib.load('forecast_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data
        data = request.get_json()
        
        # Validate input
        required_fields = ['date', 'features']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing required fields'}), 400
        
        # Prepare features
        features = pd.DataFrame([data['features']])
        features_scaled = scaler.transform(features)
        
        # Make prediction
        prediction = model.predict(features_scaled)[0]
        
        # Get prediction interval (if available)
        if hasattr(model, 'predict_interval'):
            lower, upper = model.predict_interval(features_scaled, alpha=0.05)
        else:
            # Simple approximation
            std_error = 50  # Load from model metadata
            lower = prediction - 1.96 * std_error
            upper = prediction + 1.96 * std_error
        
        response = {
            'date': data['date'],
            'prediction': float(prediction),
            'lower_bound': float(lower),
            'upper_bound': float(upper),
            'model_version': '1.0.0',
            'timestamp': pd.Timestamp.now().isoformat()
        }
        
        return jsonify(response), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/batch_predict', methods=['POST'])
def batch_predict():
    try:
        data = request.get_json()
        
        # Process multiple predictions
        features_list = data['features']
        features_df = pd.DataFrame(features_list)
        features_scaled = scaler.transform(features_df)
        
        predictions = model.predict(features_scaled)
        
        response = {
            'predictions': predictions.tolist(),
            'count': len(predictions),
            'model_version': '1.0.0'
        }
        
        return jsonify(response), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
```

**Testing the API**:
```python
import requests
import json

# Single prediction
url = 'http://localhost:5000/predict'
data = {
    'date': '2024-01-15',
    'features': {
        'lag_1': 100,
        'lag_7': 95,
        'rolling_mean_7': 98,
        'day_of_week': 1
    }
}

response = requests.post(url, json=data)
print(response.json())
```

### Docker Containerization

**Dockerfile**:
```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Copy requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY app.py .
COPY forecast_model.pkl .
COPY scaler.pkl .

# Expose port
EXPOSE 5000

# Run application
CMD ["python", "app.py"]
```

**requirements.txt**:
```
flask==2.3.0
scikit-learn==1.3.0
pandas==2.0.0
numpy==1.24.0
joblib==1.3.0
gunicorn==21.2.0
```

**Build and Run**:
```bash
# Build image
docker build -t forecast-api:v1.0 .

# Run container
docker run -d -p 5000:5000 --name forecast-api forecast-api:v1.0

# Test
curl http://localhost:5000/health
```

## Production Monitoring

### Key Metrics to Monitor

1. **Model Performance**:
   - Forecast accuracy (MAE, RMSE, MAPE)
   - Bias and tracking signal
   - Accuracy by segment/product/region

2. **System Performance**:
   - API response time
   - Throughput (requests per second)
   - Error rates
   - Resource utilization (CPU, memory)

3. **Data Quality**:
   - Missing values
   - Out-of-range values
   - Data freshness
   - Schema changes

4. **Business Metrics**:
   - Forecast consumption rate
   - Override frequency
   - Downstream impact (inventory levels, service levels)

### Monitoring Implementation

```python
import logging
import time
from functools import wraps
import psycopg2
from datetime import datetime

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('forecast_api.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Database connection for logging
def get_db_connection():
    return psycopg2.connect(
        host="localhost",
        database="forecast_monitoring",
        user="user",
        password="password"
    )

# Decorator for monitoring
def monitor_prediction(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        
        try:
            result = func(*args, **kwargs)
            duration = time.time() - start_time
            
            # Log successful prediction
            logger.info(f"Prediction successful. Duration: {duration:.3f}s")
            
            # Store metrics in database
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute(
                """
                INSERT INTO prediction_logs 
                (timestamp, duration, status, prediction_value)
                VALUES (%s, %s, %s, %s)
                """,
                (datetime.now(), duration, 'success', result.get('prediction'))
            )
            conn.commit()
            cur.close()
            conn.close()
            
            return result
        
        except Exception as e:
            duration = time.time() - start_time
            logger.error(f"Prediction failed. Duration: {duration:.3f}s. Error: {str(e)}")
            
            # Log error
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute(
                """
                INSERT INTO prediction_logs 
                (timestamp, duration, status, error_message)
                VALUES (%s, %s, %s, %s)
                """,
                (datetime.now(), duration, 'error', str(e))
            )
            conn.commit()
            cur.close()
            conn.close()
            
            raise
    
    return wrapper

# Apply to prediction function
@monitor_prediction
def make_prediction(features):
    # Prediction logic here
    pass
```

### Alerting System

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class AlertSystem:
    def __init__(self, smtp_server, smtp_port, sender_email, sender_password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password
    
    def send_alert(self, recipient, subject, message):
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = recipient
        msg['Subject'] = subject
        
        msg.attach(MIMEText(message, 'plain'))
        
        try:
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.sender_email, self.sender_password)
            server.send_message(msg)
            server.quit()
            logger.info(f"Alert sent to {recipient}")
        except Exception as e:
            logger.error(f"Failed to send alert: {str(e)}")
    
    def check_and_alert(self, metric_name, current_value, threshold, comparison='greater'):
        """
        Check metric against threshold and send alert if breached
        """
        alert_triggered = False
        
        if comparison == 'greater' and current_value > threshold:
            alert_triggered = True
        elif comparison == 'less' and current_value < threshold:
            alert_triggered = True
        
        if alert_triggered:
            message = f"""
            Alert: {metric_name} threshold breached!
            
            Current Value: {current_value}
            Threshold: {threshold}
            Comparison: {comparison}
            Timestamp: {datetime.now()}
            
            Please investigate immediately.
            """
            
            self.send_alert(
                recipient='ops-team@company.com',
                subject=f'ALERT: {metric_name} Threshold Breached',
                message=message
            )

# Usage
alerter = AlertSystem('smtp.gmail.com', 587, 'alerts@company.com', 'password')

# Check forecast accuracy
current_mape = 15.5
threshold_mape = 10.0
alerter.check_and_alert('MAPE', current_mape, threshold_mape, comparison='greater')
```

## Model Retraining and Versioning

### Automated Retraining Pipeline

```python
import schedule
import time
from datetime import datetime
import mlflow

class ModelRetrainingPipeline:
    def __init__(self, model_class, data_source):
        self.model_class = model_class
        self.data_source = data_source
        self.current_model = None
        self.current_performance = None
    
    def fetch_latest_data(self):
        """Fetch latest data from source"""
        # Implementation depends on data source
        pass
    
    def train_new_model(self, data):
        """Train a new model on latest data"""
        X_train, X_test, y_train, y_test = self.prepare_data(data)
        
        # Start MLflow run
        with mlflow.start_run():
            model = self.model_class()
            model.fit(X_train, y_train)
            
            # Evaluate
            predictions = model.predict(X_test)
            mae = mean_absolute_error(y_test, predictions)
            rmse = np.sqrt(mean_squared_error(y_test, predictions))
            
            # Log metrics
            mlflow.log_metric('mae', mae)
            mlflow.log_metric('rmse', rmse)
            
            # Log model
            mlflow.sklearn.log_model(model, 'model')
            
            return model, {'mae': mae, 'rmse': rmse}
    
    def should_deploy_new_model(self, new_performance):
        """Decide if new model should replace current model"""
        if self.current_performance is None:
            return True
        
        # Deploy if new model is at least 5% better
        improvement = (self.current_performance['rmse'] - new_performance['rmse']) / self.current_performance['rmse']
        
        return improvement > 0.05
    
    def deploy_model(self, model):
        """Deploy model to production"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        model_path = f'models/model_{timestamp}.pkl'
        
        joblib.dump(model, model_path)
        
        # Update symlink to latest model
        import os
        if os.path.exists('models/latest_model.pkl'):
            os.remove('models/latest_model.pkl')
        os.symlink(model_path, 'models/latest_model.pkl')
        
        logger.info(f"Model deployed: {model_path}")
    
    def retrain_and_deploy(self):
        """Complete retraining and deployment pipeline"""
        logger.info("Starting model retraining...")
        
        try:
            # Fetch data
            data = self.fetch_latest_data()
            
            # Train new model
            new_model, new_performance = self.train_new_model(data)
            
            # Decide whether to deploy
            if self.should_deploy_new_model(new_performance):
                self.deploy_model(new_model)
                self.current_model = new_model
                self.current_performance = new_performance
                logger.info(f"New model deployed. RMSE: {new_performance['rmse']:.2f}")
            else:
                logger.info("New model did not meet deployment criteria")
        
        except Exception as e:
            logger.error(f"Retraining failed: {str(e)}")
            # Send alert
            alerter.send_alert(
                recipient='ml-team@company.com',
                subject='Model Retraining Failed',
                message=f"Error: {str(e)}"
            )

# Schedule retraining
pipeline = ModelRetrainingPipeline(RandomForestRegressor, 'database')

# Run weekly on Sunday at 2 AM
schedule.every().sunday.at("02:00").do(pipeline.retrain_and_deploy)

while True:
    schedule.run_pending()
    time.sleep(3600)  # Check every hour
```

## Best Practices Summary

### Evaluation
1. Use multiple metrics to assess different aspects
2. Analyze residuals thoroughly
3. Validate across different time periods and segments
4. Compare against simple baselines
5. Evaluate at different forecast horizons

### Deployment
1. Containerize models for consistency
2. Implement proper error handling
3. Version all models and track lineage
4. Use CI/CD pipelines for automated deployment
5. Implement gradual rollouts (canary deployments)

### Monitoring
1. Track both model and system performance
2. Set up automated alerts for anomalies
3. Monitor data quality continuously
4. Log all predictions for audit trails
5. Create dashboards for stakeholders

### Maintenance
1. Retrain models regularly with fresh data
2. A/B test new models before full deployment
3. Document all changes and decisions
4. Maintain model registry with metadata
5. Plan for model deprecation and rollback

## Conclusion

Successful forecasting in production requires rigorous evaluation, robust deployment infrastructure, continuous monitoring, and proactive maintenance. By following these best practices, organizations can ensure their forecasting models deliver consistent value and adapt to changing conditions over time. The key is treating model deployment not as a one-time event but as an ongoing process of improvement and refinement.