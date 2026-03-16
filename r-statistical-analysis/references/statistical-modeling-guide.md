# Statistical Modeling Guide

Comprehensive guide to statistical modeling, regression analysis, and model diagnostics in R.

---

## Linear Regression

### Simple Linear Regression

```r
# Fit model
model <- lm(y ~ x, data = df)

# View results
summary(model)

# Extract coefficients
coef(model)

# Confidence intervals
confint(model, level = 0.95)

# Predictions
predict(model, newdata = new_df)
predict(model, newdata = new_df, interval = "confidence")
predict(model, newdata = new_df, interval = "prediction")
```

### Multiple Linear Regression

```r
# Multiple predictors
model <- lm(y ~ x1 + x2 + x3, data = df)

# Interaction terms
model <- lm(y ~ x1 * x2, data = df)  # Includes x1, x2, and x1:x2

# Polynomial terms
model <- lm(y ~ poly(x, 2), data = df)  # Quadratic
model <- lm(y ~ poly(x, 3), data = df)  # Cubic

# Categorical variables
model <- lm(y ~ x1 + factor(category), data = df)
```

### Model Diagnostics

```r
# Diagnostic plots
par(mfrow = c(2, 2))
plot(model)

# Individual diagnostic checks
# 1. Residuals vs Fitted - check linearity and homoscedasticity
plot(model, which = 1)

# 2. Normal Q-Q - check normality of residuals
plot(model, which = 2)

# 3. Scale-Location - check homoscedasticity
plot(model, which = 3)

# 4. Residuals vs Leverage - identify influential points
plot(model, which = 5)

# Statistical tests
# Breusch-Pagan test for heteroscedasticity
lmtest::bptest(model)

# Durbin-Watson test for autocorrelation
lmtest::dwtest(model)

# Shapiro-Wilk test for normality
shapiro.test(residuals(model))

# Variance Inflation Factor for multicollinearity
car::vif(model)
```

### Model Selection

```r
# Stepwise selection
full_model <- lm(y ~ x1 + x2 + x3 + x4 + x5, data = df)
step_model <- step(full_model, direction = "both")

# Compare models with ANOVA
model1 <- lm(y ~ x1, data = df)
model2 <- lm(y ~ x1 + x2, data = df)
anova(model1, model2)

# Information criteria
AIC(model1, model2)
BIC(model1, model2)

# Adjusted R-squared
summary(model1)$adj.r.squared
summary(model2)$adj.r.squared
```

---

## Generalized Linear Models (GLM)

### Logistic Regression

```r
# Binary outcome
model <- glm(outcome ~ x1 + x2, family = binomial(link = "logit"), data = df)

# View results
summary(model)

# Odds ratios
exp(coef(model))
exp(confint(model))

# Predictions (probabilities)
predict(model, newdata = new_df, type = "response")

# Model evaluation
# Confusion matrix
predicted_class <- ifelse(predict(model, type = "response") > 0.5, 1, 0)
table(Predicted = predicted_class, Actual = df$outcome)

# ROC curve and AUC
library(pROC)
roc_obj <- roc(df$outcome, predict(model, type = "response"))
plot(roc_obj)
auc(roc_obj)
```

### Poisson Regression

```r
# Count data
model <- glm(count ~ x1 + x2, family = poisson(link = "log"), data = df)

# Check for overdispersion
library(AER)
dispersiontest(model)

# If overdispersed, use negative binomial
library(MASS)
model_nb <- glm.nb(count ~ x1 + x2, data = df)
```

---

## Panel Data Analysis

### Fixed Effects Models

```r
library(plm)

# Pooled OLS
model_pooled <- plm(y ~ x1 + x2, data = panel_df, model = "pooling", index = c("id", "time"))

# Fixed effects (within estimator)
model_fe <- plm(y ~ x1 + x2, data = panel_df, model = "within", index = c("id", "time"))

# Random effects
model_re <- plm(y ~ x1 + x2, data = panel_df, model = "random", index = c("id", "time"))

# Hausman test (FE vs RE)
phtest(model_fe, model_re)

# Test for time-fixed effects
plmtest(model_pooled, effect = "time")

# Test for individual effects
plmtest(model_pooled, effect = "individual")
```

### Two-Way Fixed Effects

```r
# Entity and time fixed effects
model_twoway <- plm(y ~ x1 + x2, data = panel_df, model = "within", effect = "twoways", index = c("id", "time"))

summary(model_twoway)
```

---

## Instrumental Variables Regression

### Two-Stage Least Squares (2SLS)

```r
library(ivreg)

# Endogenous variable: x1
# Instrument: z
model_iv <- ivreg(y ~ x1 + x2 | z + x2, data = df)

summary(model_iv, diagnostics = TRUE)

# First stage
first_stage <- lm(x1 ~ z + x2, data = df)
summary(first_stage)

# Test instrument strength
# F-statistic should be > 10
summary(first_stage)$fstatistic

# Hausman test for endogeneity
summary(model_iv, diagnostics = TRUE)$diagnostics
```

---

## Time Series Analysis

### Stationarity Testing

```r
library(tseries)

# Augmented Dickey-Fuller test
adf.test(time_series)

# KPSS test
kpss.test(time_series)

# Phillips-Perron test
pp.test(time_series)
```

### Differencing

```r
# First difference
diff_series <- diff(time_series, differences = 1)

# Seasonal difference
seasonal_diff <- diff(time_series, lag = 12)

# Check stationarity after differencing
adf.test(diff_series)
```

### ARIMA Models

```r
library(forecast)

# Auto ARIMA (automatic model selection)
model_auto <- auto.arima(time_series)
summary(model_auto)

# Manual ARIMA specification
model_arima <- arima(time_series, order = c(1, 1, 1))

# Seasonal ARIMA
model_sarima <- arima(time_series, order = c(1, 1, 1), seasonal = list(order = c(1, 1, 1), period = 12))

# Forecasting
forecast_values <- forecast(model_auto, h = 12)
plot(forecast_values)

# Model diagnostics
checkresiduals(model_auto)
```

### Vector Autoregression (VAR)

```r
library(vars)

# Prepare multivariate time series
mts <- cbind(series1, series2, series3)

# Select lag order
VARselect(mts, lag.max = 10)

# Fit VAR model
model_var <- VAR(mts, p = 2)  # 2 lags
summary(model_var)

# Impulse response functions
irf_result <- irf(model_var, n.ahead = 10)
plot(irf_result)

# Forecast error variance decomposition
fevd_result <- fevd(model_var, n.ahead = 10)
plot(fevd_result)

# Granger causality test
causality(model_var, cause = "series1")
```

### Cointegration Analysis

```r
library(urca)

# Johansen test
jo_test <- ca.jo(mts, type = "trace", ecdet = "const", K = 2)
summary(jo_test)

# Engle-Granger test
po_test <- ca.po(mts, demean = "constant")
summary(po_test)
```

---

## Mixed Effects Models

### Linear Mixed Models

```r
library(lme4)

# Random intercept model
model_ri <- lmer(y ~ x1 + x2 + (1 | group), data = df)
summary(model_ri)

# Random slope model
model_rs <- lmer(y ~ x1 + x2 + (x1 | group), data = df)

# Random intercept and slope
model_ris <- lmer(y ~ x1 + x2 + (1 + x1 | group), data = df)

# Nested random effects
model_nested <- lmer(y ~ x1 + (1 | group1/group2), data = df)

# Model comparison
anova(model_ri, model_rs, model_ris)

# Intraclass correlation
performance::icc(model_ri)
```

### Generalized Linear Mixed Models

```r
# Logistic mixed model
model_glmm <- glmer(outcome ~ x1 + x2 + (1 | group), family = binomial, data = df)

# Poisson mixed model
model_poisson <- glmer(count ~ x1 + x2 + (1 | group), family = poisson, data = df)
```

---

## Survival Analysis

### Kaplan-Meier Curves

```r
library(survival)
library(survminer)

# Create survival object
surv_obj <- Surv(time = df$time, event = df$event)

# Fit Kaplan-Meier
km_fit <- survfit(surv_obj ~ group, data = df)

# Plot
ggsurvplot(km_fit, data = df, pval = TRUE, conf.int = TRUE)

# Summary
summary(km_fit)
```

### Cox Proportional Hazards Model

```r
# Fit Cox model
cox_model <- coxph(Surv(time, event) ~ x1 + x2 + x3, data = df)
summary(cox_model)

# Hazard ratios
exp(coef(cox_model))
exp(confint(cox_model))

# Test proportional hazards assumption
cox.zph(cox_model)

# Plot Schoenfeld residuals
ggcoxzph(cox.zph(cox_model))
```

---

## Model Validation Techniques

### Cross-Validation

```r
library(caret)

# k-fold cross-validation
train_control <- trainControl(method = "cv", number = 10)
model_cv <- train(y ~ x1 + x2, data = df, method = "lm", trControl = train_control)
print(model_cv)

# Leave-one-out cross-validation
train_control_loocv <- trainControl(method = "LOOCV")
model_loocv <- train(y ~ x1 + x2, data = df, method = "lm", trControl = train_control_loocv)

# Repeated k-fold
train_control_rep <- trainControl(method = "repeatedcv", number = 10, repeats = 3)
model_rep <- train(y ~ x1 + x2, data = df, method = "lm", trControl = train_control_rep)
```

### Bootstrap Validation

```r
# Bootstrap confidence intervals
library(boot)

# Define statistic function
boot_stat <- function(data, indices) {
  d <- data[indices, ]
  model <- lm(y ~ x1 + x2, data = d)
  return(coef(model))
}

# Run bootstrap
boot_results <- boot(data = df, statistic = boot_stat, R = 1000)

# Bootstrap confidence intervals
boot.ci(boot_results, type = "bca", index = 1)  # For first coefficient
```

### Train-Test Split

```r
# Simple split
set.seed(123)
train_indices <- sample(1:nrow(df), 0.8 * nrow(df))
train_data <- df[train_indices, ]
test_data <- df[-train_indices, ]

# Fit on training data
model <- lm(y ~ x1 + x2, data = train_data)

# Evaluate on test data
predictions <- predict(model, newdata = test_data)
test_rmse <- sqrt(mean((test_data$y - predictions)^2))
test_r2 <- cor(test_data$y, predictions)^2

cat("Test RMSE:", test_rmse, "\n")
cat("Test R²:", test_r2, "\n")
```