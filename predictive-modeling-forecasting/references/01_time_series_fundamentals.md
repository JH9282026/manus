# Time Series Forecasting Fundamentals

## Overview

Time series forecasting is the process of analyzing historical data points collected over time to predict future values. This fundamental approach is essential across industries for demand planning, financial forecasting, resource allocation, and strategic decision-making.

## What is Time Series Data?

Time series data consists of observations recorded sequentially over time at regular intervals. Key characteristics include:

### Temporal Ordering
- **Sequential Nature**: Each observation is associated with a specific time point
- **Chronological Dependency**: Past values influence future outcomes
- **Regular Intervals**: Data collected at consistent time periods (hourly, daily, monthly, etc.)

### Components of Time Series

1. **Trend**: Long-term direction of the data (upward, downward, or stationary)
2. **Seasonality**: Regular, predictable patterns that repeat over fixed periods
3. **Cyclical Patterns**: Longer-term fluctuations not tied to fixed periods
4. **Irregular/Random Component**: Unpredictable variations or noise

## Stationarity: A Critical Concept

### Definition
A stationary time series has statistical properties (mean, variance, autocorrelation) that remain constant over time. Stationarity is crucial because many forecasting models assume or require it.

### Types of Stationarity

**Strict Stationarity**: The joint probability distribution is invariant to time shifts

**Weak Stationarity** (most commonly used):
- Constant mean over time
- Constant variance over time
- Autocovariance depends only on lag, not on time

### Testing for Stationarity

**Augmented Dickey-Fuller (ADF) Test**:
- Null hypothesis: Series has a unit root (non-stationary)
- If p-value ≤ 0.05: Reject null hypothesis → Series is stationary
- If p-value > 0.05: Fail to reject → Series is non-stationary

**Visual Methods**:
- Plot the time series and look for trends or changing variance
- Plot rolling mean and standard deviation
- Examine autocorrelation function (ACF) plots

### Achieving Stationarity

**Differencing**: Subtract each observation from its previous value
- First-order differencing: y'(t) = y(t) - y(t-1)
- Second-order differencing: y''(t) = y'(t) - y'(t-1)
- Seasonal differencing: y'(t) = y(t) - y(t-s), where s is the seasonal period

**Transformation**:
- Log transformation: Stabilizes variance
- Square root transformation: Reduces impact of outliers
- Box-Cox transformation: Generalizes power transformations

**Detrending**:
- Remove trend component through regression
- Apply moving averages
- Use polynomial fitting

## Autocorrelation and Partial Autocorrelation

### Autocorrelation Function (ACF)

Measures the correlation between a time series and its lagged values.

**Interpretation**:
- Shows how observations relate to past observations
- Helps identify moving average (MA) order
- Significant spikes indicate correlation at specific lags
- Gradual decay suggests autoregressive behavior

### Partial Autocorrelation Function (PACF)

Measures the correlation between observations at different lags, controlling for intermediate lags.

**Interpretation**:
- Helps identify autoregressive (AR) order
- Sharp cutoff after lag p suggests AR(p) model
- Used in conjunction with ACF for model identification

### Using ACF and PACF Together

| Pattern | ACF | PACF | Suggested Model |
|---------|-----|------|----------------|
| AR(p) | Gradual decay | Cutoff after lag p | Autoregressive |
| MA(q) | Cutoff after lag q | Gradual decay | Moving Average |
| ARMA(p,q) | Gradual decay | Gradual decay | Mixed model |

## Data Preprocessing for Time Series

### Handling Missing Values

**Forward Fill**: Use the last known value
```python
df.fillna(method='ffill')
```

**Backward Fill**: Use the next known value
```python
df.fillna(method='bfill')
```

**Interpolation**: Estimate missing values based on surrounding data
- Linear interpolation
- Polynomial interpolation
- Spline interpolation

**Mean/Median Imputation**: Replace with statistical measures
- Use with caution as it can distort temporal patterns

### Outlier Detection and Treatment

**Statistical Methods**:
- Z-score: Values beyond ±3 standard deviations
- IQR method: Values beyond Q1 - 1.5×IQR or Q3 + 1.5×IQR

**Domain-Specific Rules**:
- Business logic constraints
- Physical impossibilities
- Historical context

**Treatment Options**:
- Remove outliers (if data errors)
- Cap/floor values (winsorization)
- Transform data to reduce impact
- Keep outliers if they represent genuine events

### Feature Engineering

**Lag Features**: Previous time period values
```python
df['lag_1'] = df['value'].shift(1)
df['lag_7'] = df['value'].shift(7)
```

**Rolling Statistics**:
- Moving averages
- Rolling standard deviation
- Rolling min/max

**Time-Based Features**:
- Day of week
- Month of year
- Quarter
- Holiday indicators
- Business day flags

## Evaluation Metrics

### Mean Absolute Error (MAE)
```
MAE = (1/n) × Σ|actual - predicted|
```
- Easy to interpret (same units as data)
- Less sensitive to outliers than MSE

### Mean Squared Error (MSE)
```
MSE = (1/n) × Σ(actual - predicted)²
```
- Penalizes larger errors more heavily
- Commonly used for optimization

### Root Mean Squared Error (RMSE)
```
RMSE = √MSE
```
- Same units as original data
- More interpretable than MSE
- Sensitive to outliers

### Mean Absolute Percentage Error (MAPE)
```
MAPE = (100/n) × Σ|actual - predicted|/|actual|
```
- Scale-independent (percentage)
- Easy to communicate to stakeholders
- Undefined when actual values are zero
- Asymmetric (penalizes over-predictions more)

### Symmetric MAPE (sMAPE)
```
sMAPE = (100/n) × Σ|actual - predicted|/(|actual| + |predicted|)
```
- Addresses asymmetry of MAPE
- Bounded between 0% and 200%

### Akaike Information Criterion (AIC)
```
AIC = 2k - 2ln(L)
```
where k = number of parameters, L = likelihood

- Used for model selection
- Lower values indicate better fit
- Penalizes model complexity

### Bayesian Information Criterion (BIC)
```
BIC = k×ln(n) - 2ln(L)
```
where n = number of observations

- Similar to AIC but stronger penalty for complexity
- Preferred when sample size is large

## Train-Test Split Strategies

### Simple Holdout
- Split data chronologically
- Train on earlier data, test on recent data
- Typical split: 70-80% train, 20-30% test

### Rolling Window (Walk-Forward Validation)
- Train on fixed window size
- Test on next period
- Move window forward and repeat
- Mimics real-world forecasting scenario

### Expanding Window
- Start with initial training set
- Add one observation at a time
- Retrain and forecast next period
- Training set grows over time

### Time Series Cross-Validation
- Multiple train-test splits
- Each split respects temporal order
- Provides more robust performance estimates

## Best Practices

1. **Always Plot Your Data**: Visual inspection reveals patterns, outliers, and anomalies

2. **Check for Stationarity**: Test and transform as needed before modeling

3. **Understand Your Domain**: Business context informs feature engineering and model selection

4. **Start Simple**: Begin with baseline models before complex approaches

5. **Validate Properly**: Use time-aware validation strategies

6. **Monitor Performance**: Track metrics over time and retrain as needed

7. **Document Assumptions**: Record decisions about preprocessing and model choices

8. **Consider Multiple Horizons**: Short-term vs. long-term forecasts may require different approaches

## Common Pitfalls

- **Data Leakage**: Using future information in training
- **Ignoring Seasonality**: Failing to account for periodic patterns
- **Over-differencing**: Making data too stationary and losing information
- **Wrong Metric**: Using inappropriate evaluation criteria for the business problem
- **Overfitting**: Creating overly complex models that don't generalize
- **Ignoring Domain Knowledge**: Purely statistical approaches without business context

## Conclusion

Mastering time series fundamentals provides the foundation for effective forecasting. Understanding stationarity, autocorrelation, proper preprocessing, and evaluation metrics enables practitioners to build robust predictive models. These concepts apply across all forecasting methodologies, from classical statistical approaches to modern machine learning techniques.

The key to successful time series forecasting lies in combining statistical rigor with domain expertise, always validating models properly, and continuously monitoring performance in production environments.