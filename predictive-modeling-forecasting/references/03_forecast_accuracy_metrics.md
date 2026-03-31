# Forecast Accuracy Metrics and Evaluation

## Overview

Evaluating forecasting accuracy is crucial for selecting models, diagnosing issues, and supporting decision-making. This reference covers the most widely used metrics for assessing forecast performance, with detailed explanations of their strengths, limitations, and appropriate use cases.

## Why Forecast Accuracy Matters

Accurate forecasting evaluation serves multiple critical purposes:

### Model Selection
- Compare different forecasting methods objectively
- Choose the best-performing model for your specific data and context
- Justify model choices to stakeholders
- Establish baseline performance for future improvements

### Problem Diagnosis
- Identify systematic errors (bias)
- Detect patterns in forecast errors
- Understand where and when models fail
- Guide model refinement efforts

### Decision Support
- Quantify uncertainty in forecasts
- Set appropriate safety stocks or buffers
- Assess risk in business decisions
- Communicate forecast reliability to stakeholders

### Ongoing Monitoring
- Track model performance over time
- Detect model drift or degradation
- Trigger retraining when necessary
- Ensure continued business value

## Core Accuracy Metrics

### Mean Absolute Error (MAE)

MAE quantifies the average size of forecast errors, disregarding their direction. It provides a straightforward answer to "on average, how far off are my predictions?"

#### Calculation

1. Calculate the difference between each actual value (yₜ) and its corresponding forecasted value (ŷₜ)
2. Take the absolute value of each difference
3. Sum all absolute differences
4. Divide by the number of forecast periods (n)

**Formula:**
```
MAE = (1/n) × Σ|yₜ - ŷₜ|
```

#### Characteristics

**Units**
- Expressed in the same units as the original data
- Easy to understand and communicate to non-technical audiences
- Example: If forecasting sales in dollars, MAE will be in dollars

**Sensitivity to Outliers**
- Less sensitive to outliers compared to RMSE
- Does not square the errors
- A 1-unit error and a 50-unit error contribute linearly to the total error

**Interpretability**
- Highly intuitive metric
- Directly represents average forecast error magnitude
- Easy to explain to stakeholders

#### When to Use MAE

- Default metric when a simple, robust summary of average error size is needed
- Extreme outlier concerns are not prevalent
- Data includes zeros (MAE handles zeros well)
- Communicating with non-technical stakeholders
- All errors are equally important (no need to penalize large errors more)

#### Limitations

- Does not indicate whether errors are large relative to the values being forecasted
- Being off by 10 units has different implications for an actual value of 50 versus 5,000
- Less optimization-friendly (absolute value function is not differentiable at zero)
- Cannot compare across different scales or datasets

#### Example

```
Actual:    [100, 150, 200, 250, 300]
Forecast:  [110, 140, 210, 240, 290]
Errors:    [10, 10, 10, 10, 10]
MAE = (10 + 10 + 10 + 10 + 10) / 5 = 10
```

### Root Mean Squared Error (RMSE)

RMSE measures the average magnitude of error but penalizes larger errors more heavily than smaller ones because it squares each error before averaging.

#### Calculation

1. Calculate the error (yₜ - ŷₜ) for each time period
2. Square each error
3. Sum all squared errors
4. Divide by the number of forecast periods (n)
5. Take the square root of the result

**Formula:**
```
RMSE = √[(1/n) × Σ(yₜ - ŷₜ)²]
```

#### Characteristics

**Units**
- Same units as the data (like MAE)
- Aids interpretability
- Can be directly compared to MAE

**Sensitivity to Outliers**
- More sensitive to outliers than MAE
- Squaring operation amplifies the impact of large errors
- A single large error can significantly increase RMSE

**Mathematical Properties**
- Differentiable everywhere (unlike MAE)
- Commonly used in optimization algorithms
- Many machine learning models naturally minimize squared error

#### When to Use RMSE

- Large errors incur disproportionately higher costs
- Financial risk assessment (large losses are much worse than small ones)
- Safety-critical applications (large errors could be dangerous)
- Optimizing a model (many algorithms minimize squared error)
- Data includes zeros (RMSE handles zeros well)
- You want to penalize variance in errors

#### Limitations

- Squaring step can make RMSE less intuitive to explain
- Sensitivity to outliers means it should be avoided if unrepresentative outliers are present
- Cannot compare across different scales or datasets
- May be dominated by a few large errors

#### Example

```
Actual:    [100, 150, 200, 250, 300]
Forecast:  [110, 140, 210, 240, 290]
Errors:    [10, 10, 10, 10, 10]
Squared:   [100, 100, 100, 100, 100]
RMSE = √(500 / 5) = √100 = 10
```

#### Comparing MAE and RMSE

- If MAE and RMSE are similar, errors are relatively uniform
- If RMSE is significantly higher than MAE, there are some large errors
- RMSE ≥ MAE always (equality only when all errors are identical)
- The ratio RMSE/MAE indicates error distribution:
  - Ratio = 1: All errors are the same magnitude
  - Ratio > 1: Variability in error sizes
  - Ratio >> 1: Presence of significant outliers

### Mean Absolute Percentage Error (MAPE)

MAPE converts forecast errors into percentages of the actual values, making it scale-independent.

#### Calculation

1. Calculate the error (yₜ - ŷₜ) for each time period
2. Divide each error by the actual value (yₜ)
3. Take the absolute value of each percentage error
4. Sum all absolute percentage errors
5. Divide by the number of forecast periods (n) and multiply by 100%

**Formula:**
```
MAPE = (100%/n) × Σ|yₜ - ŷₜ| / |yₜ|
```

#### Characteristics

**Units**
- Expressed as a percentage
- Easily understood by stakeholders regardless of data's original units
- Example: MAPE of 6.83% means forecasts are off by approximately 6.83% on average

**Scale-Independence**
- Allows direct comparison of forecast quality across different series
- Can compare forecasting a product selling 50 units/day vs. 5,000 units/day
- Useful for portfolio-level accuracy assessment

**Interpretability**
- Intuitive percentage format
- Easy to communicate to business stakeholders
- Commonly used in business reporting

#### When to Use MAPE

- Comparing forecast quality across series with different scales
- Communicating with business stakeholders who think in percentages
- Actual values are not zero or near-zero
- Relative errors are more important than absolute errors
- Benchmarking against industry standards (many industries report MAPE)

#### Limitations

**Zero or Near-Zero Actual Values**
- MAPE is undefined when actual values (yₜ) are zero
- Division by zero creates infinite or undefined errors
- Very small actual values lead to misleadingly large percentage errors
- Makes MAPE unsuitable for intermittent demand patterns

**Asymmetry**
- MAPE penalizes negative errors (over-forecasts) more heavily than positive errors (under-forecasts)
- Example: 
  - Actual = 100, Forecast = 110 → Error = 10%
  - Actual = 100, Forecast = 90 → Error = 10%
  - But if Actual = 90, Forecast = 100 → Error = 11.1%
- Can lead models to favor under-prediction
- Creates bias in model selection

**Meaningful Zero Requirement**
- Percentage errors assume the unit of measurement has a meaningful zero
- Not appropriate for temperature forecasts on Fahrenheit or Celsius scales
- Only suitable for ratio scales (where zero means "none")

#### Example

```
Actual:    [100, 150, 200, 250, 300]
Forecast:  [110, 140, 210, 240, 290]
Errors:    [10, 10, 10, 10, 10]
Pct Errors:[10%, 6.67%, 5%, 4%, 3.33%]
MAPE = (10 + 6.67 + 5 + 4 + 3.33) / 5 = 5.8%
```

## Comparison Table

| Metric | Units | Outlier Sensitivity | Cross-scale Comparison | Handles Zeros | Interpretability | Optimization-Friendly | Best Use Case |
|--------|-------|---------------------|------------------------|---------------|------------------|----------------------|---------------|
| **MAE** | Same as data | Lower | No | Yes | Very intuitive | Less so | Simple, robust summary; no extreme outliers |
| **RMSE** | Same as data | Higher | No | Yes | Moderately intuitive | Yes | Large errors costly; model optimization |
| **MAPE** | Percentage | Depends on scale | Yes | No | Very intuitive | Less so | Cross-scale comparison; no zeros |

## Advanced Metrics

### Symmetric Mean Absolute Percentage Error (sMAPE)

Addresses some limitations of MAPE by using the average of actual and forecast in the denominator.

**Formula:**
```
sMAPE = (100%/n) × Σ|yₜ - ŷₜ| / [(|yₜ| + |ŷₜ|) / 2]
```

**Advantages:**
- More symmetric than MAPE (treats over- and under-forecasts more equally)
- Bounded between 0% and 200%
- Less sensitive to small actual values

**Limitations:**
- Still undefined when both actual and forecast are zero
- Less intuitive interpretation than MAPE
- Not as widely used or understood

### Mean Absolute Scaled Error (MASE)

Compares forecast accuracy to a naive benchmark (typically a seasonal naive forecast).

**Formula:**
```
MASE = MAE / MAE_naive
```

Where MAE_naive is the MAE of a naive forecast (e.g., using the previous period's value).

**Advantages:**
- Scale-independent like MAPE
- Handles zeros well (unlike MAPE)
- Symmetric (treats over- and under-forecasts equally)
- Provides context by comparing to a baseline

**Interpretation:**
- MASE < 1: Forecast is better than naive method
- MASE = 1: Forecast is as good as naive method
- MASE > 1: Forecast is worse than naive method

**When to Use:**
- Comparing accuracy across different time series
- Data includes zeros or near-zero values
- Want to benchmark against a simple baseline

### Mean Percentage Error (MPE)

Similar to MAPE but does not take absolute values, allowing detection of bias.

**Formula:**
```
MPE = (100%/n) × Σ(yₜ - ŷₜ) / yₜ
```

**Purpose:**
- Detect systematic over-forecasting (positive MPE) or under-forecasting (negative MPE)
- Complement accuracy metrics with bias assessment
- Identify if errors cancel out or accumulate

**Interpretation:**
- MPE = 0: No systematic bias (errors cancel out)
- MPE > 0: Systematic under-forecasting
- MPE < 0: Systematic over-forecasting

**Best Practice:**
- Always pair an accuracy metric (MAE, RMSE, MAPE) with a bias metric (MPE)
- Low MAPE with high |MPE| indicates consistent directional bias
- Low MAPE with low MPE indicates well-calibrated forecasts

## Forecast Errors vs. Residuals

It's important to distinguish between these two concepts:

### Residuals
- Calculated on the **training** data
- Based on **one-step** forecasts
- Used for model diagnostics and fitting
- Can be misleading for assessing true forecast performance

### Forecast Errors
- Calculated on the **test** data (data not used in model fitting)
- Can involve **multi-step** forecasts
- Provide reliable indication of real-world performance
- Should be used for model selection and reporting

**Best Practice:** Always evaluate accuracy on test data (out-of-sample) to assess how well a model will perform on new, unseen data.

## Validation Strategies

### Train-Test Split

**Approach:**
- Split data into training and test sets
- Maintain temporal order (no random shuffling)
- Typical split: 70-80% training, 20-30% testing

**Advantages:**
- Simple and fast
- Mimics real-world scenario of forecasting into the future

**Limitations:**
- Single test period may not be representative
- Doesn't assess performance across different time periods

### Time Series Cross-Validation

**Approach:**
- Multiple train-test splits respecting temporal order
- Each split uses a different forecast origin
- Aggregates performance across all splits

**Types:**

**Rolling Window (Fixed Size)**
- Training window size remains constant
- Window "rolls" forward through time
- Example: Always use 12 months to forecast next month

**Expanding Window (Growing Size)**
- Training window grows with each split
- Uses all available historical data up to forecast origin
- Example: Use months 1-12, then 1-13, then 1-14, etc.

**Advantages:**
- More robust assessment of model performance
- Evaluates performance across different time periods
- Reduces risk of overfitting to a single test period

**Limitations:**
- Computationally more expensive
- Requires more data

## Choosing the Right Metric

### Decision Framework

**Step 1: Check for Zeros**
- If actual values include zeros or near-zeros → Avoid MAPE, consider MAE, RMSE, or MASE
- If no zeros → All metrics are viable

**Step 2: Consider Error Cost Structure**
- If large errors are much more costly → Use RMSE
- If all errors are equally costly → Use MAE
- If relative errors matter more → Use MAPE (if no zeros)

**Step 3: Assess Comparison Needs**
- If comparing across different scales → Use MAPE (if no zeros) or MASE
- If comparing within same scale → MAE or RMSE are fine

**Step 4: Consider Stakeholder Understanding**
- For non-technical audiences → MAPE (percentages) or MAE (same units)
- For technical audiences → Any metric with proper explanation

**Step 5: Use Multiple Metrics**
- Combine accuracy metric (MAE, RMSE, MAPE) with bias metric (MPE)
- Report both MAE and RMSE to understand error distribution
- Provides more complete picture of forecast performance

### Industry Benchmarks

Typical MAPE ranges by industry (rough guidelines):

- **Retail/Consumer Goods:** 5-10% (good), 10-20% (acceptable), >20% (needs improvement)
- **Manufacturing:** 3-8% (good), 8-15% (acceptable), >15% (needs improvement)
- **Financial Services:** 2-5% (good), 5-10% (acceptable), >10% (needs improvement)
- **Energy/Utilities:** 1-3% (good), 3-7% (acceptable), >7% (needs improvement)

Note: These are general guidelines and can vary significantly based on specific context, forecast horizon, and data characteristics.

## Practical Implementation

### Python Example

```python
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error

def calculate_metrics(actual, forecast):
    """
    Calculate MAE, RMSE, MAPE, and MPE for forecast evaluation.
    
    Parameters:
    actual: array-like, actual values
    forecast: array-like, forecasted values
    
    Returns:
    dict with MAE, RMSE, MAPE, MPE
    """
    actual = np.array(actual)
    forecast = np.array(forecast)
    
    # MAE
    mae = mean_absolute_error(actual, forecast)
    
    # RMSE
    rmse = np.sqrt(mean_squared_error(actual, forecast))
    
    # MAPE (handle zeros)
    mask = actual != 0
    if mask.sum() > 0:
        mape = np.mean(np.abs((actual[mask] - forecast[mask]) / actual[mask])) * 100
    else:
        mape = np.nan
    
    # MPE (handle zeros)
    if mask.sum() > 0:
        mpe = np.mean((actual[mask] - forecast[mask]) / actual[mask]) * 100
    else:
        mpe = np.nan
    
    return {
        'MAE': mae,
        'RMSE': rmse,
        'MAPE': mape,
        'MPE': mpe,
        'RMSE/MAE': rmse / mae if mae != 0 else np.nan
    }

# Example usage
actual = [100, 150, 200, 250, 300]
forecast = [110, 140, 210, 240, 290]

metrics = calculate_metrics(actual, forecast)
for metric, value in metrics.items():
    print(f"{metric}: {value:.2f}")
```

### R Example

```r
library(forecast)

# Calculate accuracy metrics
actual <- c(100, 150, 200, 250, 300)
forecast_values <- c(110, 140, 210, 240, 290)

# Using forecast package
accuracy_metrics <- accuracy(forecast_values, actual)
print(accuracy_metrics)

# Manual calculation
mae <- mean(abs(actual - forecast_values))
rmse <- sqrt(mean((actual - forecast_values)^2))
mape <- mean(abs((actual - forecast_values) / actual)) * 100
mpe <- mean((actual - forecast_values) / actual) * 100

cat(sprintf("MAE: %.2f\n", mae))
cat(sprintf("RMSE: %.2f\n", rmse))
cat(sprintf("MAPE: %.2f%%\n", mape))
cat(sprintf("MPE: %.2f%%\n", mpe))
```

## Best Practices Summary

1. **Always use out-of-sample (test) data** for accuracy evaluation
2. **Report multiple metrics** for a complete picture (e.g., MAE + RMSE + MPE)
3. **Consider your specific context** when choosing metrics (cost of errors, presence of zeros, stakeholder understanding)
4. **Use time series cross-validation** for robust assessment
5. **Monitor metrics over time** to detect model drift
6. **Compare to baselines** (naive forecasts, simple models) to demonstrate value
7. **Document your metric choices** and their rationale
8. **Be aware of metric limitations** and interpret results accordingly

## Further Reading

- "Forecasting: Principles and Practice" by Rob J Hyndman and George Athanasopoulos (Chapter 3: The forecaster's toolbox)
- "Another look at measures of forecast accuracy" by Rob J Hyndman and Anne B Koehler (2006)
- "Forecast evaluation" by Diebold, Francis X. (2015)
- "Time Series Analysis: Forecasting and Control" by George E. P. Box et al.

## Practical Resources

- Python: scikit-learn metrics module, forecast package
- R: forecast package (accuracy function), Metrics package
- Online calculators: Various forecast accuracy calculators available
- Kaggle competitions: M5 Forecasting for real-world examples and benchmarks
