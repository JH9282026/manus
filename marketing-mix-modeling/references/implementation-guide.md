# Marketing Mix Modeling Implementation Guide

Step-by-step guide to planning, executing, and deploying a Marketing Mix Modeling project from inception to ongoing optimization.

---

## Project Planning and Scoping

### Defining Business Objectives

Clear objectives are critical for MMM success. Common objectives:

**Budget Optimization**
- Determine optimal allocation across channels
- Identify overspending and underspending
- Maximize ROI within budget constraints

**Channel Effectiveness Measurement**
- Quantify incremental contribution of each channel
- Understand which channels drive the most sales
- Measure synergies between channels

**Sales Forecasting**
- Predict sales under different marketing scenarios
- Support annual planning and budgeting
- Anticipate impact of market changes

**Strategic Decision Support**
- Evaluate new channel opportunities
- Assess impact of budget cuts or increases
- Inform long-term marketing strategy

**Accountability and Reporting**
- Demonstrate marketing's contribution to business
- Justify marketing investments to CFO/CEO
- Establish performance benchmarks

### Stakeholder Alignment

**Key Stakeholders**
- CMO / VP Marketing: Primary sponsor, uses insights for strategy
- CFO / Finance: Budget owner, needs ROI justification
- Media/Channel Managers: Implement recommendations
- Analytics Team: Builds and maintains model
- Sales Leadership: Understands marketing's contribution to pipeline
- Executive Leadership: Strategic decision-making

**Alignment Activities**
- Kickoff meeting: Present objectives, scope, timeline
- Regular check-ins: Share progress, gather feedback
- Interim presentations: Validate preliminary findings
- Final presentation: Deliver insights and recommendations
- Training sessions: Enable stakeholders to use results

**Managing Expectations**
- MMM provides directional insights, not perfect precision
- Results are estimates with uncertainty ranges
- Model requires ongoing maintenance and updates
- Implementation of recommendations is critical for value
- Cultural change may be needed to adopt data-driven decisions

### Scope Definition

**Geographic Scope**
- National model: Single model for entire country
- Regional models: Separate models for regions (or hierarchical)
- Multi-market: Models for multiple countries

**Time Period**
- Minimum: 2 years of weekly data (104 observations)
- Recommended: 3 years of weekly data (156 observations)
- Longer is better for capturing seasonality and trends

**Channels to Include**
- All measurable marketing channels (online and offline)
- Prioritize channels with significant spend
- Include emerging channels if data available
- Consider grouping small channels

**Business Metrics**
- Primary: Sales revenue or units sold
- Secondary: Brand metrics, customer acquisition, retention
- Product/category level if needed

**Granularity**
- Weekly data is standard (balances detail and stability)
- Daily data for fast-moving categories (e.g., e-commerce)
- Monthly data if weekly not available (less ideal)

### Resource Planning

**Team Composition**
- Project Lead: Oversees project, manages stakeholders
- Data Scientist/Analyst: Builds and validates model
- Data Engineer: Collects and prepares data
- Marketing Analyst: Provides domain expertise
- Business Stakeholder: Ensures business relevance

**Timeline**

Typical MMM project timeline:

**Weeks 1-2: Planning and Scoping**
- Define objectives and scope
- Identify data sources
- Align stakeholders

**Weeks 3-6: Data Collection and Preparation**
- Gather data from all sources
- Clean and harmonize data
- Exploratory data analysis
- Identify gaps and issues

**Weeks 7-10: Model Development**
- Feature engineering (adstock, saturation)
- Build initial models
- Test multiple specifications
- Validate and refine

**Weeks 11-12: Insight Generation and Reporting**
- Calculate ROI and contribution
- Generate response curves
- Run scenario simulations
- Develop recommendations
- Create presentations and reports

**Weeks 13-14: Presentation and Handoff**
- Present to stakeholders
- Gather feedback and iterate
- Document model and process
- Train users
- Plan ongoing maintenance

**Total: 3-4 months for initial model**

**Budget Considerations**
- Internal team time (largest cost)
- Data acquisition (syndicated data, third-party sources)
- Software and tools (if using commercial platforms)
- External consultants (if needed)
- Ongoing maintenance and updates

---

## Data Collection and Preparation

### Data Requirements

**Marketing Data (2-3 years, weekly)**

*Media Spend*
- TV: National and local spend, GRPs, impressions
- Digital: Paid search, display, social, video (spend, impressions, clicks)
- Radio: National and local spend, GRPs
- Print: Newspaper, magazine spend
- Out-of-Home (OOH): Billboard, transit spend, impressions
- Direct Mail: Spend, volume sent

*Digital Metrics*
- Impressions, clicks, video views
- Reach and frequency
- Cost per click (CPC), cost per thousand (CPM)

*Promotional Activities*
- Discount depth and duration
- Coupon distribution and redemption
- Sales events and promotions
- Free shipping offers

*Pricing*
- Average selling price
- Price changes and promotions
- Competitor pricing (if available)

*Distribution*
- Number of stores/outlets
- Geographic coverage
- Online availability
- Shelf space and placement

**Sales Data**

*Revenue and Units*
- Total sales revenue
- Units sold
- Product/category breakdowns (if modeling at that level)
- Channel breakdowns (retail, e-commerce, etc.)

*Geographic Breakdowns*
- Regional sales (if modeling regionally)
- DMA or market-level sales

**External Data**

*Seasonality*
- Holiday indicators (Thanksgiving, Christmas, etc.)
- School calendar (back-to-school, summer)
- Sporting events (Super Bowl, Olympics)

*Economic Indicators*
- GDP growth
- Consumer confidence index
- Unemployment rate
- Inflation (CPI)
- Gas prices (for relevant categories)

*Competitor Data*
- Competitor advertising spend (from syndicated sources)
- Competitor pricing
- Competitor product launches
- Market share data

*Weather*
- Temperature, precipitation, snowfall
- Relevant for beverages, apparel, home improvement, etc.

### Data Sources

**Internal Sources**
- Finance systems (sales, revenue)
- Marketing platforms (Google Ads, Facebook Ads, etc.)
- Media agencies (TV, radio, print spend and metrics)
- CRM systems (customer data)
- E-commerce platforms (online sales)
- POS systems (retail sales)

**External Sources**
- Nielsen: TV ratings, ad spend, retail sales
- Kantar: Ad spend across channels
- comScore: Digital audience and behavior
- IRI: Retail sales and promotions
- FRED (Federal Reserve Economic Data): Economic indicators
- NOAA: Weather data
- Google Trends: Search interest

### Data Cleaning and Preparation

**Data Quality Checks**

*Completeness*
- Identify missing values
- Assess impact of missingness
- Decide on imputation or exclusion

*Consistency*
- Ensure consistent time periods across all variables
- Align granularity (all weekly or all daily)
- Check for data entry errors

*Accuracy*
- Validate against known values
- Cross-check with multiple sources
- Identify and investigate anomalies

**Handling Missing Data**

*Imputation Methods*
- Forward fill: Use previous value
- Backward fill: Use next value
- Linear interpolation: Interpolate between known values
- Mean/median imputation: Use average value
- Model-based imputation: Predict missing values

*When to Exclude*
- Large blocks of missing data
- Critical variables with missing values
- Periods with data quality issues

**Outlier Detection and Treatment**

*Identification*
- Visual inspection (box plots, scatter plots)
- Statistical methods (Z-scores, IQR method)
- Domain knowledge (known events)

*Treatment*
- Investigate cause (data error vs. real event)
- Correct if data error
- Create indicator variable for real events (e.g., viral moment)
- Winsorize (cap at percentile, e.g., 99th)
- Transform (log transformation reduces outlier impact)

**Data Transformation**

*Standardization*
- Scale variables to comparable units
- Z-score standardization: (X - mean) / std
- Min-max scaling: (X - min) / (max - min)

*Log Transformation*
- Reduces skewness
- Stabilizes variance
- Interprets coefficients as elasticities
- Common for sales and spend variables

**Data Alignment**

*Time Alignment*
- Ensure all variables are on same time basis (week starting Monday, etc.)
- Align fiscal vs. calendar periods
- Handle different reporting periods

*Geographic Alignment*
- Match sales and marketing data to same geographic units
- Aggregate or disaggregate as needed

### Exploratory Data Analysis (EDA)

**Univariate Analysis**

*Summary Statistics*
- Mean, median, standard deviation
- Min, max, percentiles
- Identify range and variability

*Distributions*
- Histograms: Visualize distribution shape
- Box plots: Identify outliers and spread
- Time-series plots: Visualize trends and seasonality

**Bivariate Analysis**

*Correlation Analysis*
- Correlation matrix: Identify relationships
- Heatmap visualization
- Identify multicollinearity issues

*Scatter Plots*
- Sales vs. each marketing variable
- Visualize relationships
- Identify non-linearities

**Time-Series Analysis**

*Trend*
- Plot sales over time
- Identify long-term growth or decline
- Fit trend line

*Seasonality*
- Seasonal plots (e.g., sales by month)
- Autocorrelation function (ACF)
- Identify cyclical patterns

*Stationarity*
- Augmented Dickey-Fuller test
- Non-stationary series may need differencing

**Spend Variation Analysis**

*Assess Variation*
- Coefficient of variation: std / mean
- Sufficient variation is critical for model identification
- Channels with constant spend are difficult to model

*Identify Natural Experiments*
- Periods with significant spend changes
- Budget cuts or increases
- Channel tests or pauses
- These provide valuable signal

---

## Feature Engineering

### Adstock Transformation

**Implementation Steps**

1. **Select Adstock Function**
   - Geometric (most common)
   - Delayed geometric
   - Weibull (more flexible)

2. **Define Decay Rate Range**
   - Based on channel type and domain knowledge
   - TV: 0.3-0.7
   - Digital: 0.0-0.3
   - Print: 0.4-0.7

3. **Apply Transformation**
   - For each channel and each decay rate in range
   - Create adstocked variable

4. **Select Optimal Decay Rate**
   - Fit model with each adstocked variable
   - Select decay rate that maximizes model fit (R²)
   - Or use Bayesian approach with prior on decay rate

**Code Example (Python)**
```python
def geometric_adstock(spend, decay_rate):
    adstock = np.zeros(len(spend))
    adstock[0] = spend[0]
    for t in range(1, len(spend)):
        adstock[t] = spend[t] + decay_rate * adstock[t-1]
    return adstock

# Test multiple decay rates
decay_rates = np.arange(0.0, 1.0, 0.1)
best_r2 = 0
best_decay = 0

for decay in decay_rates:
    tv_adstock = geometric_adstock(tv_spend, decay)
    model = fit_model(sales, tv_adstock, other_vars)
    if model.r2 > best_r2:
        best_r2 = model.r2
        best_decay = decay
```

### Saturation Transformation

**Implementation Steps**

1. **Select Saturation Function**
   - Logarithmic: log(spend + 1)
   - Power: spend^α (α < 1)
   - Hill equation: (V_max × spend^S) / (K^S + spend^S)

2. **Apply Transformation**
   - Transform adstocked spend
   - Creates diminishing returns effect

3. **Estimate Parameters**
   - For Hill equation, estimate V_max, K, S
   - Use non-linear optimization or Bayesian estimation

**Code Example (Python)**
```python
from scipy.optimize import curve_fit

def hill_transform(spend, v_max, k, s):
    return (v_max * spend**s) / (k**s + spend**s)

# Fit Hill parameters
params, _ = curve_fit(hill_transform, tv_adstock, sales)
v_max, k, s = params

# Apply transformation
tv_saturated = hill_transform(tv_adstock, v_max, k, s)
```

### Interaction Terms

**Creating Interactions**

*Multiplicative Interactions*
```python
tv_digital_interaction = tv_adstock * digital_adstock
```

*When to Include*
- Strong theoretical basis (e.g., TV amplifies digital)
- Sufficient data variation
- Avoid over-complicating model

**Interpretation**
- Positive coefficient: Synergy (channels amplify each other)
- Negative coefficient: Cannibalization (channels compete)

### Seasonality Variables

**Monthly Dummies**
```python
month_dummies = pd.get_dummies(data['month'], prefix='month', drop_first=True)
```
- 11 dummy variables for 12 months (drop one to avoid multicollinearity)

**Holiday Indicators**
```python
data['is_holiday'] = data['date'].isin(holiday_dates).astype(int)
```

**Fourier Terms**
```python
data['sin_annual'] = np.sin(2 * np.pi * data['week'] / 52)
data['cos_annual'] = np.cos(2 * np.pi * data['week'] / 52)
```

### Trend Variables

**Linear Trend**
```python
data['trend'] = range(len(data))
```

**Polynomial Trend**
```python
data['trend_sq'] = data['trend'] ** 2
```

---

## Model Building

### Model Specification

**Basic Model Structure**
```
Sales = β₀ + Σ β_i × Transformed_Marketing_i + Σ γ_j × Control_j + ε
```

Where:
- Transformed_Marketing_i: Adstocked and saturated marketing variables
- Control_j: Seasonality, trend, economic factors, etc.

**Iterative Model Development**

1. **Baseline Model**
   - Sales ~ Trend + Seasonality
   - Establishes base sales without marketing

2. **Add Marketing Variables**
   - Add one channel at a time or all at once
   - Assess coefficient signs and significance

3. **Add Control Variables**
   - Economic factors, competition, weather
   - Improves model fit and attribution accuracy

4. **Refine Transformations**
   - Optimize adstock and saturation parameters
   - Test different functional forms

5. **Add Interactions (if warranted)**
   - Test key interaction terms
   - Assess improvement in fit

### Model Estimation

**Using R**

*OLS Regression*
```r
model <- lm(sales ~ tv_adstock + digital_adstock + radio_adstock + 
            trend + month_dummies + gdp, data = data)
summary(model)
```

*Ridge Regression*
```r
library(glmnet)
X <- model.matrix(sales ~ ., data = data)[,-1]
y <- data$sales
ridge_model <- cv.glmnet(X, y, alpha = 0)  # alpha=0 for Ridge
coef(ridge_model, s = "lambda.min")
```

*Bayesian Regression with brms*
```r
library(brms)
priors <- c(
  prior(normal(0, 10), class = "b", coef = "tv_adstock"),
  prior(normal(0, 10), class = "b", coef = "digital_adstock")
)

bayes_model <- brm(sales ~ tv_adstock + digital_adstock + radio_adstock + 
                   trend + month_dummies + gdp,
                   data = data, prior = priors, 
                   chains = 4, iter = 2000)
summary(bayes_model)
```

**Using Python**

*OLS Regression*
```python
import statsmodels.api as sm

X = data[['tv_adstock', 'digital_adstock', 'radio_adstock', 'trend', 'gdp']]
X = sm.add_constant(X)
y = data['sales']

model = sm.OLS(y, X).fit()
print(model.summary())
```

*Ridge Regression*
```python
from sklearn.linear_model import RidgeCV

ridge = RidgeCV(alphas=[0.01, 0.1, 1, 10, 100])
ridge.fit(X, y)
print(f"Best alpha: {ridge.alpha_}")
print(f"Coefficients: {ridge.coef_}")
```

*Bayesian Regression with PyMC*
```python
import pymc as pm

with pm.Model() as model:
    # Priors
    beta_tv = pm.Normal('beta_tv', mu=0, sigma=10)
    beta_digital = pm.Normal('beta_digital', mu=0, sigma=10)
    sigma = pm.HalfNormal('sigma', sigma=1)
    
    # Likelihood
    mu = beta_tv * tv_adstock + beta_digital * digital_adstock + ...
    sales_obs = pm.Normal('sales', mu=mu, sigma=sigma, observed=sales)
    
    # Inference
    trace = pm.sample(2000, tune=1000, chains=4)
    
pm.summary(trace)
```

### Using Open-Source MMM Frameworks

**Meta Robyn (R)**

```r
library(Robyn)

# Prepare data
data <- read.csv("mmm_data.csv")

# Define model inputs
InputCollect <- robyn_inputs(
  dt_input = data,
  dt_holidays = holidays,
  date_var = "date",
  dep_var = "sales",
  dep_var_type = "revenue",
  prophet_vars = c("trend", "season", "holiday"),
  prophet_country = "US",
  paid_media_spends = c("tv_spend", "digital_spend", "radio_spend"),
  paid_media_vars = c("tv_impressions", "digital_impressions", "radio_grps"),
  context_vars = c("gdp", "competitor_spend"),
  adstock = "geometric",
  window_start = "2021-01-01",
  window_end = "2023-12-31"
)

# Run model
OutputModels <- robyn_run(
  InputCollect = InputCollect,
  iterations = 2000,
  trials = 5
)

# Select best model
OutputCollect <- robyn_outputs(OutputModels)

# Get results
robyn_response(InputCollect, OutputCollect)
robyn_allocator(InputCollect, OutputCollect)
```

**Google LightweightMMM (Python)**

```python
from lightweight_mmm import lightweight_mmm
from lightweight_mmm import preprocessing
import jax.numpy as jnp

# Prepare data
media_data = jnp.array(data[['tv', 'digital', 'radio']].values)
sales = jnp.array(data['sales'].values)
extra_features = jnp.array(data[['trend', 'seasonality']].values)

# Scale data
media_data_scaled, media_scaler = preprocessing.CustomScaler().fit_transform(media_data)

# Initialize model
mmm = lightweight_mmm.LightweightMMM()

# Fit model
mmm.fit(
    media=media_data_scaled,
    total_costs=media_costs,
    target=sales,
    extra_features=extra_features,
    number_warmup=1000,
    number_samples=1000
)

# Get results
mmm.print_summary()

# Response curves
lightweight_mmm.plot.plot_response_curves(mmm, media_scaler)

# Budget optimization
optimized_budget = lightweight_mmm.optimize_media.find_optimal_budgets(
    mmm, media_scaler, total_budget=1000000
)
```

---

## Model Validation

### Statistical Validation

**Model Fit Metrics**

*R-squared*
- Target: 0.7-0.9 for good MMM
- Higher is better, but beware overfitting

*Adjusted R-squared*
- Accounts for number of variables
- Use for comparing models with different variable counts

*MAPE (Mean Absolute Percentage Error)*
- Target: < 10% for good MMM
- Interpretable as average % error

*RMSE (Root Mean Squared Error)*
- In same units as sales
- Lower is better
- Penalizes large errors

**Residual Diagnostics**

*Residual Plots*
```python
import matplotlib.pyplot as plt

residuals = model.resid
fitted = model.fittedvalues

# Residuals vs. fitted
plt.scatter(fitted, residuals)
plt.axhline(0, color='red', linestyle='--')
plt.xlabel('Fitted Values')
plt.ylabel('Residuals')
plt.title('Residuals vs. Fitted')
plt.show()

# Residuals over time
plt.plot(data['date'], residuals)
plt.axhline(0, color='red', linestyle='--')
plt.xlabel('Date')
plt.ylabel('Residuals')
plt.title('Residuals Over Time')
plt.show()

# Histogram of residuals
plt.hist(residuals, bins=30)
plt.xlabel('Residuals')
plt.ylabel('Frequency')
plt.title('Distribution of Residuals')
plt.show()
```

*Autocorrelation Check*
```python
from statsmodels.stats.stattools import durbin_watson

dw = durbin_watson(residuals)
print(f"Durbin-Watson: {dw}")
# Target: ~2.0 (no autocorrelation)
```

**Coefficient Validation**

*Sign Check*
- All marketing coefficients should be positive
- Price coefficients typically negative
- Competitor activity typically negative

*Magnitude Check*
- Calculate implied ROI for each channel
- Compare to industry benchmarks
- Flag unrealistic values (e.g., ROI > 10 or < 0)

*Significance Check*
- Review p-values (target < 0.05 for key variables)
- But don't exclude variables solely based on significance
- Business relevance matters more than statistical significance

### Out-of-Sample Validation

**Hold-Out Test**

```python
# Split data
train_data = data[data['date'] < '2023-10-01']
test_data = data[data['date'] >= '2023-10-01']

# Fit on training data
X_train = train_data[features]
y_train = train_data['sales']
model = sm.OLS(y_train, sm.add_constant(X_train)).fit()

# Predict on test data
X_test = test_data[features]
y_test = test_data['sales']
y_pred = model.predict(sm.add_constant(X_test))

# Calculate error metrics
from sklearn.metrics import mean_absolute_percentage_error, mean_squared_error

mape = mean_absolute_percentage_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"Test MAPE: {mape:.2%}")
print(f"Test RMSE: {rmse:.2f}")

# Plot actual vs. predicted
plt.plot(test_data['date'], y_test, label='Actual')
plt.plot(test_data['date'], y_pred, label='Predicted')
plt.legend()
plt.title('Out-of-Sample Validation')
plt.show()
```

**Cross-Validation**

```python
from sklearn.model_selection import TimeSeriesSplit

tscv = TimeSeriesSplit(n_splits=5)
mape_scores = []

for train_idx, test_idx in tscv.split(X):
    X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
    y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]
    
    model = sm.OLS(y_train, sm.add_constant(X_train)).fit()
    y_pred = model.predict(sm.add_constant(X_test))
    
    mape = mean_absolute_percentage_error(y_test, y_pred)
    mape_scores.append(mape)

print(f"Average CV MAPE: {np.mean(mape_scores):.2%}")
print(f"Std Dev: {np.std(mape_scores):.2%}")
```

### Business Validation

**Stakeholder Review**
- Present preliminary results to marketing team
- Gather feedback on plausibility
- Identify discrepancies with business knowledge
- Iterate model based on feedback

**Benchmark Comparison**
- Compare ROI to industry benchmarks
- Compare to historical performance
- Compare to attribution model results (for digital)
- Investigate large discrepancies

**Scenario Testing**
- Run "what-if" scenarios stakeholders care about
- "What if we cut TV by 50%?"
- "What if we double digital spend?"
- Assess if results are reasonable

---

## Insight Generation and Optimization

### Calculating ROI and Contribution

**Channel Contribution**

```python
# Calculate incremental sales for each channel
for channel in ['tv', 'digital', 'radio']:
    # Predicted sales with channel
    sales_with = model.predict(X)
    
    # Predicted sales without channel (set to zero)
    X_without = X.copy()
    X_without[channel] = 0
    sales_without = model.predict(X_without)
    
    # Incremental sales
    incremental_sales = (sales_with - sales_without).sum()
    contribution_pct = incremental_sales / sales_with.sum() * 100
    
    print(f"{channel}: ${incremental_sales:,.0f} ({contribution_pct:.1f}%)")
```

**ROI Calculation**

```python
# Calculate ROI for each channel
for channel in ['tv', 'digital', 'radio']:
    incremental_revenue = incremental_sales[channel]  # from above
    total_spend = data[f'{channel}_spend'].sum()
    
    roi = (incremental_revenue - total_spend) / total_spend
    roas = incremental_revenue / total_spend
    
    print(f"{channel} ROI: {roi:.2f} ({roi*100:.0f}%)")
    print(f"{channel} ROAS: {roas:.2f}")
```

### Response Curves

**Generating Response Curves**

```python
# For TV channel
tv_spend_range = np.linspace(0, data['tv_spend'].max() * 2, 100)
response = []

for spend in tv_spend_range:
    # Apply adstock and saturation transformations
    adstock = geometric_adstock([spend], decay_rate=0.5)[0]
    saturated = hill_transform(adstock, v_max, k, s)
    
    # Predict incremental sales
    incremental_sales = model.params['tv'] * saturated
    response.append(incremental_sales)

# Plot
plt.plot(tv_spend_range, response)
plt.axvline(data['tv_spend'].mean(), color='red', linestyle='--', label='Current Spend')
plt.xlabel('TV Spend')
plt.ylabel('Incremental Sales')
plt.title('TV Response Curve')
plt.legend()
plt.show()
```

**Marginal ROI Curve**

```python
# Calculate marginal ROI at each spend level
marginal_roi = np.gradient(response, tv_spend_range)

plt.plot(tv_spend_range, marginal_roi)
plt.axhline(1.0, color='red', linestyle='--', label='Break-even')
plt.axvline(data['tv_spend'].mean(), color='green', linestyle='--', label='Current Spend')
plt.xlabel('TV Spend')
plt.ylabel('Marginal ROI')
plt.title('TV Marginal ROI Curve')
plt.legend()
plt.show()
```

### Budget Optimization

**Optimization Problem**

Maximize total incremental sales subject to budget constraint:

```
Maximize: Σ f_i(spend_i)
Subject to: Σ spend_i ≤ Total_Budget
            spend_i ≥ 0
```

Where f_i is the response function for channel i.

**Implementation**

```python
from scipy.optimize import minimize

def total_sales(spend_allocation, response_functions):
    """Calculate total incremental sales for given spend allocation"""
    total = 0
    for i, spend in enumerate(spend_allocation):
        total += response_functions[i](spend)
    return -total  # Negative because we're minimizing

def budget_constraint(spend_allocation, total_budget):
    """Ensure total spend doesn't exceed budget"""
    return total_budget - sum(spend_allocation)

# Define response functions for each channel (from response curves)
response_functions = [tv_response_func, digital_response_func, radio_response_func]

# Initial guess (current allocation)
initial_allocation = [data['tv_spend'].sum(), data['digital_spend'].sum(), data['radio_spend'].sum()]

# Total budget
total_budget = sum(initial_allocation)

# Constraints
constraints = {'type': 'ineq', 'fun': budget_constraint, 'args': (total_budget,)}

# Bounds (non-negative spend)
bounds = [(0, None) for _ in range(len(response_functions))]

# Optimize
result = minimize(
    total_sales,
    initial_allocation,
    args=(response_functions,),
    method='SLSQP',
    bounds=bounds,
    constraints=constraints
)

optimal_allocation = result.x
print("Optimal Allocation:")
for i, channel in enumerate(['TV', 'Digital', 'Radio']):
    print(f"{channel}: ${optimal_allocation[i]:,.0f} (Current: ${initial_allocation[i]:,.0f})")
```

### Scenario Analysis

**"What-If" Scenarios**

```python
scenarios = {
    "Current": {'tv': 1000000, 'digital': 500000, 'radio': 200000},
    "Cut TV 50%": {'tv': 500000, 'digital': 500000, 'radio': 200000},
    "Double Digital": {'tv': 1000000, 'digital': 1000000, 'radio': 200000},
    "Optimized": dict(zip(['tv', 'digital', 'radio'], optimal_allocation))
}

results = []
for scenario_name, spend in scenarios.items():
    # Prepare features with scenario spend
    X_scenario = X.copy()
    for channel in ['tv', 'digital', 'radio']:
        # Apply transformations
        adstock = geometric_adstock([spend[channel]], decay_rates[channel])[0]
        saturated = saturation_functions[channel](adstock)
        X_scenario[channel] = saturated
    
    # Predict sales
    predicted_sales = model.predict(X_scenario).sum()
    total_spend = sum(spend.values())
    roi = (predicted_sales - total_spend) / total_spend
    
    results.append({
        'Scenario': scenario_name,
        'Total Spend': total_spend,
        'Predicted Sales': predicted_sales,
        'ROI': roi
    })

results_df = pd.DataFrame(results)
print(results_df)
```

---

## Reporting and Communication

### Executive Summary

**Key Components**

1. **Objective and Scope**
   - What was analyzed
   - Time period and channels covered

2. **Model Performance**
   - R² and MAPE
   - Validation results
   - Confidence in estimates

3. **Key Findings**
   - Top-performing channels
   - Underperforming channels
   - Synergies and interactions
   - Baseline vs. incremental sales

4. **Recommendations**
   - Budget reallocation suggestions
   - Expected impact
   - Implementation priorities

5. **Next Steps**
   - Implementation plan
   - Testing agenda
   - Model refresh schedule

### Visualizations

**Sales Decomposition Waterfall**

```python
import plotly.graph_objects as go

contributions = {
    'Base Sales': 10000000,
    'TV': 2000000,
    'Digital': 1500000,
    'Radio': 500000,
    'Promotions': 1000000
}

fig = go.Figure(go.Waterfall(
    orientation="v",
    measure=["absolute", "relative", "relative", "relative", "relative", "total"],
    x=list(contributions.keys()) + ['Total Sales'],
    y=list(contributions.values()) + [sum(contributions.values())],
    connector={"line": {"color": "rgb(63, 63, 63)"}},
))

fig.update_layout(
    title="Sales Decomposition",
    showlegend=False
)

fig.show()
```

**Channel ROI Comparison**

```python
channels = ['TV', 'Digital', 'Radio', 'Print']
roi_values = [1.8, 2.5, 1.2, 0.9]

fig = go.Figure(go.Bar(
    x=channels,
    y=roi_values,
    marker_color=['green' if roi > 1 else 'red' for roi in roi_values]
))

fig.add_hline(y=1.0, line_dash="dash", line_color="black", annotation_text="Break-even")
fig.update_layout(
    title="ROI by Channel",
    xaxis_title="Channel",
    yaxis_title="ROI"
)

fig.show()
```

**Response Curves Dashboard**

```python
from plotly.subplots import make_subplots

fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=('TV', 'Digital', 'Radio', 'Print')
)

for i, channel in enumerate(['TV', 'Digital', 'Radio', 'Print']):
    row = i // 2 + 1
    col = i % 2 + 1
    
    fig.add_trace(
        go.Scatter(x=spend_range[channel], y=response[channel], name=channel),
        row=row, col=col
    )
    
    # Add current spend line
    fig.add_vline(
        x=current_spend[channel],
        line_dash="dash",
        line_color="red",
        row=row, col=col
    )

fig.update_layout(height=800, title_text="Response Curves by Channel")
fig.show()
```

### Actionable Recommendations

**Recommendation Template**

For each recommendation:

1. **Action**: Specific change to make
2. **Rationale**: Why this change is recommended (data-driven)
3. **Expected Impact**: Quantified benefit (revenue, ROI improvement)
4. **Implementation**: How to execute
5. **Timeline**: When to implement
6. **Risk/Considerations**: Potential downsides or caveats

**Example Recommendation**

> **Recommendation 1: Increase Digital Spend by 30%**
> 
> **Rationale**: Digital has the highest ROI (2.5) and is operating below saturation point. Response curve shows significant headroom for additional investment.
> 
> **Expected Impact**: 
> - Incremental revenue: $750K
> - Additional spend: $150K
> - Incremental ROI: 4.0
> - Overall marketing ROI improvement: +0.3
> 
> **Implementation**: 
> - Reallocate $150K from Print (lowest ROI at 0.9)
> - Focus on high-performing digital channels (Paid Search, Social)
> - Maintain current creative and targeting
> 
> **Timeline**: Implement in Q2 2024
> 
> **Considerations**: 
> - Monitor for saturation as spend increases
> - Ensure sufficient creative assets for increased volume
> - Track performance weekly to validate model predictions

---

## Ongoing Maintenance and Updates

### Model Refresh Schedule

**Weekly/Monthly Updates**
- Update data with latest period
- Re-run model with fixed parameters
- Generate updated forecasts
- Monitor prediction accuracy

**Quarterly Re-estimation**
- Re-estimate all parameters
- Validate model performance
- Update response curves
- Refresh budget recommendations

**Annual Rebuild**
- Comprehensive model review
- Add new channels or variables
- Test new methodologies
- Full validation and stakeholder review

### Performance Monitoring

**Tracking Metrics**
- Prediction accuracy (MAPE) over time
- Coefficient stability (are they changing significantly?)
- Residual patterns (new systematic errors?)
- Business outcomes (are recommendations working?)

**Alert Triggers**
- MAPE increases above threshold (e.g., 15%)
- Coefficients change dramatically
- Residuals show new patterns
- Major market changes or disruptions

### Continuous Improvement

**Incorporate New Data**
- Add new channels as they launch
- Include new external factors
- Refine existing variables

**Integrate Experiments**
- Use incrementality test results to calibrate model
- Validate model predictions with experiments
- Update priors based on experimental evidence

**Methodology Enhancements**
- Adopt new statistical techniques
- Leverage new tools and platforms
- Incorporate stakeholder feedback

**Documentation**
- Maintain detailed model documentation
- Document all changes and updates
- Create user guides for stakeholders
- Build institutional knowledge

---

## Common Pitfalls and How to Avoid Them

### Data Quality Issues

**Problem**: Incomplete, inconsistent, or inaccurate data

**Solution**:
- Establish data quality checks early
- Validate data against multiple sources
- Document data issues and resolutions
- Build relationships with data owners

### Insufficient Spend Variation

**Problem**: Channels with constant spend are difficult to model

**Solution**:
- Use longer time periods to capture variation
- Leverage geographic variation if available
- Conduct intentional spend tests
- Use Bayesian priors to stabilize estimates

### Multicollinearity

**Problem**: Correlated channels make it hard to isolate effects

**Solution**:
- Combine highly correlated channels
- Use regularization (Ridge, Elastic Net)
- Incorporate experimental data for calibration
- Use Bayesian priors to constrain coefficients

### Overfitting

**Problem**: Model fits training data too well, poor out-of-sample performance

**Solution**:
- Use cross-validation
- Apply regularization
- Prefer simpler models
- Validate on hold-out data

### Stakeholder Misalignment

**Problem**: Results not trusted or adopted

**Solution**:
- Involve stakeholders early and often
- Validate results with business knowledge
- Communicate uncertainty and limitations
- Provide actionable, specific recommendations
- Demonstrate value through pilot implementations

### Ignoring Model Limitations

**Problem**: Treating model as perfect truth

**Solution**:
- Communicate uncertainty ranges
- Acknowledge limitations (correlation vs. causation)
- Validate with experiments
- Use model as decision support, not sole decision-maker
- Continuously monitor and update