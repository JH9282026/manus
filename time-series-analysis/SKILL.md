---
name: time-series-analysis
description: "Analyze and forecast time-dependent data using ARIMA, SARIMA, exponential smoothing, and Prophet. Use for sales forecasting, demand prediction, stock price analysis, seasonal decomposition, trend analysis, and predictive modeling of temporal patterns."
---

# Time Series Analysis

Analyze temporal data patterns and forecast future values using statistical and machine learning methods.

## Overview

Time series analysis involves studying data points collected over time to identify patterns, trends, and seasonal effects. This skill covers stationarity testing, decomposition, ARIMA modeling, seasonal adjustments, and modern forecasting techniques. Applications include sales forecasting, financial analysis, demand planning, and anomaly detection in temporal data.

## Core Concepts

| Concept | Definition | Importance |
|---------|------------|------------|
| Trend | Long-term increase or decrease | Identifies overall direction |
| Seasonality | Regular, periodic fluctuations | Captures recurring patterns |
| Cyclical | Non-periodic fluctuations | Economic/business cycles |
| Stationarity | Constant statistical properties | Required for many models |
| Autocorrelation | Correlation with lagged values | Identifies dependencies |

## Stationarity

### Why Stationarity Matters

Most time series models assume stationarity:
- Constant mean over time
- Constant variance over time
- Autocovariance depends only on lag, not time

### Testing for Stationarity

**Augmented Dickey-Fuller (ADF) Test**:
```python
from statsmodels.tsa.stattools import adfuller

result = adfuller(time_series)
print(f'ADF Statistic: {result[0]}')
print(f'p-value: {result[1]}')

if result[1] < 0.05:
    print("Series is stationary")
else:
    print("Series is non-stationary")
```

**KPSS Test** (null hypothesis: stationary):
```python
from statsmodels.tsa.stattools import kpss

result = kpss(time_series, regression='c')
print(f'KPSS Statistic: {result[0]}')
print(f'p-value: {result[1]}')
```

### Achieving Stationarity

**Differencing**:
```python
# First difference
diff1 = time_series.diff().dropna()

# Second difference
diff2 = time_series.diff().diff().dropna()

# Seasonal difference
seasonal_diff = time_series.diff(12).dropna()  # For monthly data with yearly seasonality
```

**Transformation**:
```python
import numpy as np

# Log transformation
log_series = np.log(time_series)

# Square root
sqrt_series = np.sqrt(time_series)

# Box-Cox transformation
from scipy.stats import boxcox
transformed, lambda_param = boxcox(time_series)
```

## Time Series Decomposition

### Additive vs. Multiplicative

**Additive**: Y = Trend + Seasonal + Residual
- Use when seasonal variation is constant

**Multiplicative**: Y = Trend × Seasonal × Residual
- Use when seasonal variation increases with trend

### Decomposition in Python

```python
from statsmodels.tsa.seasonal import seasonal_decompose

# Additive decomposition
decomposition = seasonal_decompose(time_series, model='additive', period=12)

# Plot components
import matplotlib.pyplot as plt
fig = decomposition.plot()
plt.show()

# Access components
trend = decomposition.trend
seasonal = decomposition.seasonal
residual = decomposition.resid
```

## ARIMA Models

### Components

**AR (Autoregressive)**: Uses past values
- AR(p): p lagged observations

**I (Integrated)**: Differencing for stationarity
- I(d): d times differenced

**MA (Moving Average)**: Uses past forecast errors
- MA(q): q lagged forecast errors

### Model Notation: ARIMA(p, d, q)

- p: Order of autoregressive part
- d: Degree of differencing
- q: Order of moving average part

### Identifying Parameters

**ACF (Autocorrelation Function)**:
```python
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# ACF plot - helps identify q
plot_acf(time_series, lags=40)
plt.show()

# PACF plot - helps identify p
plot_pacf(time_series, lags=40)
plt.show()
```

**Rules of thumb**:
- ACF cuts off at lag q → MA(q)
- PACF cuts off at lag p → AR(p)
- Both tail off → ARMA(p,q)

### Fitting ARIMA

```python
from statsmodels.tsa.arima.model import ARIMA

# Fit ARIMA model
model = ARIMA(time_series, order=(1, 1, 1))
fitted_model = model.fit()

# Summary
print(fitted_model.summary())

# Diagnostics
fitted_model.plot_diagnostics(figsize=(12, 8))
plt.show()

# Forecast
forecast = fitted_model.forecast(steps=12)
```

### Auto ARIMA

```python
from pmdarima import auto_arima

# Automatically find best parameters
auto_model = auto_arima(
    time_series,
    start_p=0, start_q=0,
    max_p=5, max_q=5,
    seasonal=False,
    stepwise=True,
    suppress_warnings=True,
    error_action='ignore'
)

print(auto_model.summary())
```

## Seasonal ARIMA (SARIMA)

### Model Notation: SARIMA(p,d,q)(P,D,Q)m

- (p,d,q): Non-seasonal parameters
- (P,D,Q): Seasonal parameters
- m: Number of periods per season

### Fitting SARIMA

```python
from statsmodels.tsa.statespace.sarimax import SARIMAX

# Fit SARIMA model
model = SARIMAX(
    time_series,
    order=(1, 1, 1),
    seasonal_order=(1, 1, 1, 12),  # 12 for monthly data
    enforce_stationarity=False,
    enforce_invertibility=False
)

fitted_model = model.fit()

# Forecast
forecast = fitted_model.forecast(steps=12)
```

## Exponential Smoothing

### Simple Exponential Smoothing

For data with no trend or seasonality:
```python
from statsmodels.tsa.holtwinters import SimpleExpSmoothing

model = SimpleExpSmoothing(time_series)
fitted_model = model.fit(smoothing_level=0.2)
forecast = fitted_model.forecast(steps=12)
```

### Holt's Linear Trend

For data with trend but no seasonality:
```python
from statsmodels.tsa.holtwinters import Holt

model = Holt(time_series)
fitted_model = model.fit(smoothing_level=0.8, smoothing_trend=0.2)
forecast = fitted_model.forecast(steps=12)
```

### Holt-Winters

For data with trend and seasonality:
```python
from statsmodels.tsa.holtwinters import ExponentialSmoothing

model = ExponentialSmoothing(
    time_series,
    seasonal_periods=12,
    trend='add',
    seasonal='add'
)

fitted_model = model.fit()
forecast = fitted_model.forecast(steps=12)
```

## Prophet (Facebook)

### Advantages

- Handles missing data and outliers
- Automatic seasonality detection
- Intuitive parameter tuning
- Works well with daily data

### Basic Usage

```python
from prophet import Prophet
import pandas as pd

# Prepare data (requires 'ds' and 'y' columns)
df = pd.DataFrame({
    'ds': time_series.index,
    'y': time_series.values
})

# Fit model
model = Prophet()
model.fit(df)

# Create future dataframe
future = model.make_future_dataframe(periods=365)

# Forecast
forecast = model.predict(future)

# Plot
model.plot(forecast)
model.plot_components(forecast)
```

### Advanced Features

```python
# Add custom seasonality
model = Prophet()
model.add_seasonality(name='monthly', period=30.5, fourier_order=5)

# Add holidays
holidays = pd.DataFrame({
    'holiday': 'holiday_name',
    'ds': pd.to_datetime(['2024-01-01', '2024-12-25']),
    'lower_window': 0,
    'upper_window': 1,
})
model = Prophet(holidays=holidays)

# Add regressors
model = Prophet()
model.add_regressor('temperature')
model.add_regressor('promotion')
```

## Model Evaluation

### Metrics

```python
from sklearn.metrics import mean_squared_error, mean_absolute_error, mean_absolute_percentage_error
import numpy as np

# RMSE
rmse = np.sqrt(mean_squared_error(y_true, y_pred))

# MAE
mae = mean_absolute_error(y_true, y_pred)

# MAPE
mape = mean_absolute_percentage_error(y_true, y_pred)

# MASE (Mean Absolute Scaled Error)
def mase(y_true, y_pred, y_train):
    n = len(y_train)
    d = np.abs(np.diff(y_train)).sum() / (n - 1)
    errors = np.abs(y_true - y_pred)
    return errors.mean() / d
```

### Cross-Validation

**Time Series Split**:
```python
from sklearn.model_selection import TimeSeriesSplit

tscv = TimeSeriesSplit(n_splits=5)

for train_idx, test_idx in tscv.split(time_series):
    train = time_series[train_idx]
    test = time_series[test_idx]
    
    # Fit and evaluate model
    model = ARIMA(train, order=(1,1,1))
    fitted = model.fit()
    forecast = fitted.forecast(steps=len(test))
    
    # Calculate metrics
    rmse = np.sqrt(mean_squared_error(test, forecast))
    print(f"RMSE: {rmse}")
```

## Best Practices

### Data Preparation

1. **Check for missing values** — Interpolate or forward-fill appropriately
2. **Handle outliers** — Investigate and treat anomalies
3. **Ensure regular frequency** — Resample if necessary
4. **Plot the data** — Visual inspection reveals patterns

### Model Selection

1. **Start simple** — Try simple models before complex ones
2. **Check residuals** — Should be white noise (no patterns)
3. **Compare multiple models** — Use AIC, BIC for comparison
4. **Validate on holdout set** — Test on unseen data

### Forecasting

1. **Understand uncertainty** — Provide confidence intervals
2. **Monitor performance** — Track forecast accuracy over time
3. **Update regularly** — Retrain with new data
4. **Consider external factors** — Add regressors when relevant

## Using the Reference Files

### When to Read Each Reference

**`/references/arima-comprehensive.md`** — Read when building ARIMA/SARIMA models, diagnosing model fit, or optimizing parameters.

**`/references/prophet-advanced.md`** — Read when using Prophet for forecasting, adding custom seasonality, or incorporating external regressors.

**`/references/forecasting-techniques.md`** — Read when comparing forecasting methods, handling multiple seasonalities, or implementing ensemble forecasts.

**`/references/time-series-case-studies.md`** — Read when starting a forecasting project or looking for domain-specific examples.

## References

- [Arima Comprehensive](references/arima-comprehensive.md)
- [Forecasting Techniques](references/forecasting-techniques.md)
- [Prophet Advanced](references/prophet-advanced.md)
- [Time Series Case Studies](references/time-series-case-studies.md)
