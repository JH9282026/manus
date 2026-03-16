# Machine Learning Workflows in R

Comprehensive guide to implementing machine learning models using mlr3 and caret frameworks.

---

## mlr3 Framework

### Setup and Basic Workflow

```r
library(mlr3)
library(mlr3learners)
library(mlr3tuning)
library(mlr3viz)

# Create task
task <- TaskClassif$new(id = "my_task", backend = df, target = "outcome")

# Create learner
learner <- lrn("classif.ranger", predict_type = "prob")

# Train model
learner$train(task)

# Make predictions
predictions <- learner$predict(task)

# Evaluate
predictions$score(msr("classif.acc"))
```

### Available Tasks

```r
# Classification
task_classif <- TaskClassif$new(id = "classif", backend = df, target = "class")

# Regression
task_regr <- TaskRegr$new(id = "regr", backend = df, target = "value")

# Survival
task_surv <- TaskSurv$new(id = "surv", backend = df, time = "time", event = "status")

# View available tasks
mlr_tasks
```

### Learners

```r
# View available learners
mlr_learners

# Classification learners
lrn("classif.log_reg")  # Logistic regression
lrn("classif.ranger")   # Random forest
lrn("classif.xgboost")  # XGBoost
lrn("classif.svm")      # Support vector machine
lrn("classif.naive_bayes")  # Naive Bayes

# Regression learners
lrn("regr.lm")          # Linear regression
lrn("regr.ranger")      # Random forest
lrn("regr.xgboost")     # XGBoost
lrn("regr.svm")         # Support vector machine

# Set hyperparameters
learner <- lrn("classif.ranger", num.trees = 500, mtry = 3)
```

### Resampling and Cross-Validation

```r
# Define resampling strategy
resampling <- rsmp("cv", folds = 10)

# Perform resampling
rr <- resample(task, learner, resampling)

# Aggregate results
rr$aggregate(msr("classif.acc"))

# View individual fold results
rr$score(msr("classif.acc"))

# Other resampling strategies
rsmp("holdout", ratio = 0.8)  # Train-test split
rsmp("repeated_cv", folds = 10, repeats = 3)  # Repeated CV
rsmp("bootstrap", repeats = 30)  # Bootstrap
rsmp("loo")  # Leave-one-out
```

### Performance Measures

```r
# Classification metrics
msr("classif.acc")      # Accuracy
msr("classif.auc")      # Area under ROC curve
msr("classif.ce")       # Classification error
msr("classif.precision")  # Precision
msr("classif.recall")   # Recall
msr("classif.f1")       # F1 score

# Regression metrics
msr("regr.mse")         # Mean squared error
msr("regr.rmse")        # Root mean squared error
msr("regr.mae")         # Mean absolute error
msr("regr.rsq")         # R-squared

# Multiple metrics
measures <- msrs(c("classif.acc", "classif.auc", "classif.f1"))
rr$aggregate(measures)
```

### Hyperparameter Tuning

```r
library(mlr3tuning)
library(paradox)

# Define search space
search_space <- ps(
  num.trees = p_int(lower = 100, upper = 1000),
  mtry = p_int(lower = 1, upper = 10),
  min.node.size = p_int(lower = 1, upper = 20)
)

# Create tuning instance
instance <- TuningInstanceSingleCrit$new(
  task = task,
  learner = learner,
  resampling = rsmp("cv", folds = 5),
  measure = msr("classif.acc"),
  search_space = search_space,
  terminator = trm("evals", n_evals = 50)
)

# Choose tuning method
tuner <- tnr("random_search")  # Random search
# tuner <- tnr("grid_search", resolution = 5)  # Grid search

# Run tuning
tuner$optimize(instance)

# Best hyperparameters
instance$result_learner_param_vals

# Best performance
instance$result_y

# Update learner with best parameters
learner$param_set$values <- instance$result_learner_param_vals
```

### Feature Selection

```r
library(mlr3filters)

# Calculate feature importance
filter <- flt("importance", learner = lrn("classif.ranger"))
filter$calculate(task)

# View scores
filter$scores

# Select top features
task_filtered <- task$clone()
task_filtered$select(filter$scores[1:10, "feature"])

# Available filters
mlr_filters
```

### Pipelines

```r
library(mlr3pipelines)

# Create preprocessing pipeline
pipeline <- po("scale") %>>%
  po("encode") %>>%
  po("learner", lrn("classif.ranger"))

# Convert to learner
learner_pipeline <- as_learner(pipeline)

# Train and predict
learner_pipeline$train(task)
predictions <- learner_pipeline$predict(task)
```

---

## caret Framework

### Basic Workflow

```r
library(caret)

# Train-test split
set.seed(123)
train_index <- createDataPartition(df$outcome, p = 0.8, list = FALSE)
train_data <- df[train_index, ]
test_data <- df[-train_index, ]

# Train model
model <- train(
  outcome ~ .,
  data = train_data,
  method = "rf",
  trControl = trainControl(method = "cv", number = 10)
)

# Make predictions
predictions <- predict(model, newdata = test_data)

# Evaluate
confusionMatrix(predictions, test_data$outcome)
```

### Available Models

```r
# View all available models
names(getModelInfo())

# Common classification models
"rf"          # Random Forest
"xgbTree"     # XGBoost
"svmRadial"   # SVM with radial kernel
"glmnet"      # Elastic Net
"knn"         # K-Nearest Neighbors
"naive_bayes" # Naive Bayes
"nnet"        # Neural Network

# Common regression models
"lm"          # Linear Regression
"rf"          # Random Forest
"xgbTree"     # XGBoost
"svmRadial"   # SVM
"glmnet"      # Elastic Net
```

### Cross-Validation

```r
# k-fold cross-validation
train_control <- trainControl(method = "cv", number = 10)

# Repeated k-fold
train_control <- trainControl(method = "repeatedcv", number = 10, repeats = 3)

# Leave-one-out
train_control <- trainControl(method = "LOOCV")

# Bootstrap
train_control <- trainControl(method = "boot", number = 25)

# Train with cross-validation
model <- train(
  outcome ~ .,
  data = train_data,
  method = "rf",
  trControl = train_control
)
```

### Hyperparameter Tuning

```r
# Automatic grid search
model <- train(
  outcome ~ .,
  data = train_data,
  method = "rf",
  trControl = trainControl(method = "cv", number = 10),
  tuneLength = 5  # Number of values to try for each parameter
)

# Custom grid
tune_grid <- expand.grid(
  mtry = c(2, 4, 6, 8),
  splitrule = c("gini", "extratrees"),
  min.node.size = c(1, 5, 10)
)

model <- train(
  outcome ~ .,
  data = train_data,
  method = "ranger",
  trControl = trainControl(method = "cv", number = 10),
  tuneGrid = tune_grid
)

# View tuning results
plot(model)
model$bestTune
```

### Preprocessing

```r
# Preprocessing in train()
model <- train(
  outcome ~ .,
  data = train_data,
  method = "rf",
  preProcess = c("center", "scale", "nzv"),
  trControl = trainControl(method = "cv", number = 10)
)

# Available preprocessing methods
# "center" - subtract mean
# "scale" - divide by standard deviation
# "range" - normalize to [0, 1]
# "BoxCox" - Box-Cox transformation
# "YeoJohnson" - Yeo-Johnson transformation
# "pca" - Principal component analysis
# "ica" - Independent component analysis
# "spatialSign" - Spatial sign transformation
# "nzv" - Remove near-zero variance predictors
# "corr" - Remove highly correlated predictors

# Manual preprocessing
preproc <- preProcess(train_data[, -outcome_col], method = c("center", "scale"))
train_transformed <- predict(preproc, train_data)
test_transformed <- predict(preproc, test_data)
```

### Feature Selection

```r
# Recursive feature elimination
control <- rfeControl(functions = rfFuncs, method = "cv", number = 10)
results <- rfe(
  x = train_data[, -outcome_col],
  y = train_data$outcome,
  sizes = c(5, 10, 15, 20),
  rfeControl = control
)

# View results
print(results)
plot(results, type = c("g", "o"))

# Selected features
predictors(results)

# Train model with selected features
model <- train(
  outcome ~ .,
  data = train_data[, c(predictors(results), "outcome")],
  method = "rf",
  trControl = trainControl(method = "cv", number = 10)
)
```

### Model Comparison

```r
# Train multiple models
models <- list(
  rf = train(outcome ~ ., data = train_data, method = "rf", trControl = train_control),
  xgb = train(outcome ~ ., data = train_data, method = "xgbTree", trControl = train_control),
  svm = train(outcome ~ ., data = train_data, method = "svmRadial", trControl = train_control)
)

# Compare resampling results
results <- resamples(models)
summary(results)

# Visualize comparison
bwplot(results)
dotplot(results)

# Statistical comparison
diff_results <- diff(results)
summary(diff_results)
```

### Variable Importance

```r
# Calculate importance
importance <- varImp(model)

# Plot
plot(importance, top = 20)

# Extract values
importance$importance
```

---

## Model Evaluation

### Classification Metrics

```r
# Confusion matrix
confusionMatrix(predictions, test_data$outcome)

# ROC curve and AUC
library(pROC)
roc_obj <- roc(test_data$outcome, predict(model, test_data, type = "prob")[, 2])
plot(roc_obj)
auc(roc_obj)

# Precision-Recall curve
library(PRROC)
pr_obj <- pr.curve(scores.class0 = predict(model, test_data, type = "prob")[, 2],
                   weights.class0 = as.numeric(test_data$outcome) - 1)
plot(pr_obj)
```

### Regression Metrics

```r
# Calculate metrics
postResample(predictions, test_data$outcome)

# Individual metrics
RMSE(predictions, test_data$outcome)
R2(predictions, test_data$outcome)
MAE(predictions, test_data$outcome)

# Residual plots
residuals <- test_data$outcome - predictions
plot(predictions, residuals)
abline(h = 0, col = "red")
```

---

## Advanced Techniques

### Ensemble Methods

```r
library(caretEnsemble)

# Train multiple models
model_list <- caretList(
  outcome ~ .,
  data = train_data,
  trControl = trainControl(method = "cv", number = 10, savePredictions = "final"),
  methodList = c("rf", "xgbTree", "svmRadial")
)

# Stack models
stacked_model <- caretStack(
  model_list,
  method = "glm",
  trControl = trainControl(method = "cv", number = 10)
)

# Predictions
predictions <- predict(stacked_model, newdata = test_data)
```

### Handling Imbalanced Data

```r
# SMOTE (Synthetic Minority Over-sampling Technique)
library(DMwR)
train_balanced <- SMOTE(outcome ~ ., data = train_data, perc.over = 200, perc.under = 200)

# Class weights in training
model <- train(
  outcome ~ .,
  data = train_data,
  method = "rf",
  trControl = trainControl(method = "cv", number = 10),
  weights = ifelse(train_data$outcome == "minority", 2, 1)
)

# Sampling in trainControl
train_control <- trainControl(
  method = "cv",
  number = 10,
  sampling = "up"  # or "down" or "smote"
)
```