# Predictive Modeling for HR

Comprehensive guide to building, validating, and deploying predictive models for HR outcomes including turnover, hiring success, performance, and workforce planning.

---

## Predictive Modeling Process

### Step 1: Define Business Problem

**Clarify Objective:**
- What are you trying to predict?
- Why does it matter to the business?
- What decisions will be informed by predictions?
- What is the cost of being wrong?

**Examples:**
- **Turnover Prediction:** Identify employees at risk of leaving in next 6 months to enable retention interventions
- **Hiring Success:** Predict which candidates will be high performers to improve hiring decisions
- **Performance Forecasting:** Anticipate future performance to guide development and succession planning

**Success Criteria:**
- How accurate does the model need to be?
- What is acceptable false positive/negative rate?
- What ROI is expected?

### Step 2: Gather and Prepare Data

**Data Collection:**
- Identify all relevant data sources (HRIS, performance management, surveys, etc.)
- Extract historical data (minimum 2 years recommended)
- Include outcome variable (e.g., who left vs. stayed)
- Collect predictor variables (tenure, performance, compensation, etc.)

**Data Cleaning:**
- Handle missing values (imputation, deletion, or flagging)
- Remove duplicates
- Correct errors and inconsistencies
- Standardize formats (dates, names, categories)

**Feature Engineering:**
Create meaningful variables from raw data:
- **Derived Variables:** Compensation change %, time since last promotion
- **Aggregations:** Average performance rating over 3 years
- **Categorical Encoding:** Convert text categories to numbers (one-hot encoding, label encoding)
- **Interaction Terms:** Combinations of variables (tenure x performance)
- **Time-Based Features:** Seasonality, trends, time since event

**Example Features for Turnover Prediction:**
- Tenure (months)
- Performance rating (1-5)
- Compensation percentile within role
- Compensation change % in last year
- Time since last promotion (months)
- Manager effectiveness score (from survey)
- Engagement score (from survey)
- Number of job changes in last 2 years
- Commute distance (miles)
- Market demand for role (external data)

**Data Splitting:**
- **Training Set (70%):** Used to build model
- **Validation Set (15%):** Used to tune model parameters
- **Test Set (15%):** Used to evaluate final model performance
- **Important:** Ensure no data leakage between sets

### Step 3: Select Modeling Approach

**Common Algorithms for HR Predictions:**

**Logistic Regression:**
- **Use Case:** Binary outcomes (will leave yes/no, will succeed yes/no)
- **Pros:** Simple, interpretable, probability scores
- **Cons:** Assumes linear relationships, may miss complex patterns
- **Best For:** Starting point, when interpretability is critical

**Decision Trees:**
- **Use Case:** Classification (turnover, hiring success)
- **Pros:** Easy to interpret, handles non-linear relationships, no scaling needed
- **Cons:** Can overfit, unstable (small data changes = big tree changes)
- **Best For:** Exploratory analysis, when interpretability matters

**Random Forest:**
- **Use Case:** Classification and regression
- **Pros:** High accuracy, handles non-linearity, reduces overfitting vs. single tree
- **Cons:** Less interpretable, computationally intensive
- **Best For:** When accuracy is priority over interpretability

**Gradient Boosting (XGBoost, LightGBM):**
- **Use Case:** Classification and regression
- **Pros:** Often highest accuracy, handles missing data well
- **Cons:** Can overfit, requires careful tuning, less interpretable
- **Best For:** Competitions, when maximum accuracy needed

**Neural Networks:**
- **Use Case:** Complex pattern recognition, large datasets
- **Pros:** Can model very complex relationships
- **Cons:** Requires large data, computationally intensive, "black box"
- **Best For:** Large organizations with lots of data

**Survival Analysis (Cox Proportional Hazards):**
- **Use Case:** Time-to-event prediction (when will employee leave?)
- **Pros:** Handles censored data (employees who haven't left yet), provides time dimension
- **Cons:** More complex, requires specialized knowledge
- **Best For:** Turnover prediction when timing matters

**Selection Criteria:**
- **Data Size:** Neural networks need more data than logistic regression
- **Interpretability:** Decision trees and logistic regression more interpretable than neural networks
- **Accuracy:** Gradient boosting and random forest often most accurate
- **Speed:** Logistic regression fastest, neural networks slowest
- **Maintenance:** Simpler models easier to maintain and update

**Recommendation:** Start with logistic regression or decision tree for interpretability, then try random forest or gradient boosting for accuracy improvement.

### Step 4: Train Model

**Training Process:**
1. Feed training data into algorithm
2. Algorithm learns patterns and relationships
3. Model parameters are optimized to minimize prediction error
4. Validate on validation set and tune hyperparameters
5. Iterate until satisfactory performance

**Hyperparameter Tuning:**
- Adjust model settings to optimize performance
- Examples: tree depth, learning rate, regularization strength
- Use validation set to evaluate different hyperparameter combinations
- Techniques: Grid search, random search, Bayesian optimization

**Avoiding Overfitting:**
- **Overfitting:** Model performs well on training data but poorly on new data
- **Prevention:**
  - Use cross-validation
  - Regularization (penalize model complexity)
  - Limit model complexity (tree depth, number of features)
  - Ensemble methods (random forest, boosting)
  - More training data

### Step 5: Validate Model

**Performance Metrics:**

**For Classification (e.g., will leave yes/no):**
- **Accuracy:** % of predictions that are correct (can be misleading if classes imbalanced)
- **Precision:** Of predicted positives, % that are actually positive (minimize false positives)
- **Recall (Sensitivity):** Of actual positives, % that are predicted positive (minimize false negatives)
- **F1 Score:** Harmonic mean of precision and recall (balance both)
- **AUC-ROC:** Area under receiver operating characteristic curve (overall model quality, 0.5 = random, 1.0 = perfect)
- **Confusion Matrix:** Table showing true positives, false positives, true negatives, false negatives

**Example: Turnover Prediction**
- **Accuracy:** 85% of predictions correct
- **Precision:** 70% of predicted leavers actually leave (30% false alarms)
- **Recall:** 60% of actual leavers are predicted (40% missed)
- **AUC-ROC:** 0.82 (good discrimination)

**For Regression (e.g., predicted performance rating):**
- **Mean Absolute Error (MAE):** Average absolute difference between predicted and actual
- **Root Mean Squared Error (RMSE):** Square root of average squared differences (penalizes large errors more)
- **R-squared:** % of variance explained by model (0 = no explanatory power, 1 = perfect)

**Cross-Validation:**
- Split data into k folds (e.g., 5 or 10)
- Train on k-1 folds, validate on remaining fold
- Repeat k times, rotating validation fold
- Average performance across all folds
- Provides more robust estimate of model performance

**Bias Audit:**
- Check for disparate impact across protected classes (gender, race, age)
- Ensure model doesn't systematically disadvantage any group
- Example: Does turnover model predict higher risk for women than men with same characteristics?
- Mitigation: Remove biased features, adjust model, use fairness-aware algorithms

### Step 6: Interpret Model

**Feature Importance:**
- Which variables are most predictive?
- Helps understand what drives outcome
- Guides interventions (focus on changeable important factors)

**Example: Turnover Prediction Feature Importance**
1. Manager effectiveness score (most important)
2. Compensation percentile
3. Time since last promotion
4. Engagement score
5. Tenure

**Partial Dependence Plots:**
- Show relationship between feature and prediction
- Example: How does turnover risk change as manager effectiveness score increases?

**SHAP (SHapley Additive exPlanations):**
- Explains individual predictions
- Shows contribution of each feature to specific prediction
- Example: "Employee X has 75% turnover risk because: low manager score (+30%), below-market comp (+20%), long time since promotion (+15%), low engagement (+10%)"

**Model Transparency:**
- Document model methodology, features, performance
- Explain to stakeholders how model works
- Provide guidance on how to use predictions
- Clarify limitations and appropriate use cases

### Step 7: Deploy Model

**Scoring:**
- Apply model to current employee data
- Generate predictions (probabilities, risk scores, ratings)
- Update regularly (monthly or quarterly)

**Integration:**
- Embed predictions in HRIS or analytics platform
- Provide dashboards for managers and HR
- Automate alerts for high-risk employees
- Link to intervention workflows

**Monitoring:**
- Track model performance over time
- Compare predictions to actual outcomes
- Monitor for model drift (performance degradation)
- Refresh model periodically (annually or when drift detected)

**Governance:**
- Clear ownership and accountability
- Approval process for model changes
- Documentation and version control
- Audit trail for predictions and decisions

### Step 8: Act on Insights

**Intervention Design:**
- What actions will be taken based on predictions?
- Who is responsible for interventions?
- How will effectiveness be measured?

**Example: Turnover Prediction Interventions**
- **High Risk (>70% probability):** Manager conversation, compensation review, role adjustment, development plan
- **Medium Risk (40-70%):** Check-in conversation, engagement survey follow-up
- **Low Risk (<40%):** No immediate action, continue monitoring

**Feedback Loop:**
- Track which interventions are effective
- Refine intervention strategies based on results
- Improve model with new data and outcomes
- Continuous learning and optimization

---

## Turnover Prediction Model (Detailed Example)

### Business Problem
Reduce regrettable turnover by identifying at-risk employees early and enabling proactive retention interventions.

### Data Collection

**Outcome Variable:**
- **Voluntary Turnover:** 1 if employee left voluntarily in next 6 months, 0 if stayed
- **Timeframe:** Predict 6 months ahead
- **Historical Data:** 3 years of employee data

**Predictor Variables:**

*Demographic:*
- Age, gender, location, commute distance

*Employment:*
- Tenure (months), job level, department, role
- Hire source (referral, job board, agency)

*Compensation:*
- Base salary, salary percentile within role
- Salary change % in last year
- Bonus received (yes/no), bonus amount
- Equity granted (yes/no)

*Performance:*
- Current performance rating (1-5)
- Average performance rating (last 3 years)
- Performance trend (improving, stable, declining)
- Goal achievement rate

*Career:*
- Time since last promotion (months)
- Number of promotions in tenure
- Internal job changes (lateral moves)

*Engagement:*
- Overall engagement score (1-10)
- Manager effectiveness score (1-10)
- Career development satisfaction (1-10)
- Work-life balance score (1-10)

*External:*
- Market demand for role (high/medium/low)
- Unemployment rate in location

**Sample Size:** 5,000 employees, 500 left voluntarily (10% turnover rate)

### Data Preparation

**Handling Missing Data:**
- Engagement scores missing for 20% of employees (didn't complete survey)
- Approach: Create "missing" flag variable, impute with median

**Feature Engineering:**
- **Compensation Gap:** (Market 50th percentile - Current salary) / Market 50th percentile
- **Promotion Velocity:** Number of promotions / Tenure in years
- **Engagement Decline:** Current engagement - Previous year engagement
- **High Performer:** 1 if performance rating >= 4, 0 otherwise

**Encoding Categorical Variables:**
- Department: One-hot encoding (create binary variable for each department)
- Hire source: Label encoding (1=referral, 2=job board, 3=agency)

**Data Splitting:**
- Training: 3,500 employees (70%)
- Validation: 750 employees (15%)
- Test: 750 employees (15%)

### Model Training

**Algorithm:** Random Forest (chosen for balance of accuracy and interpretability)

**Hyperparameters:**
- Number of trees: 100
- Max tree depth: 10
- Min samples per leaf: 20
- Features per split: sqrt(total features)

**Training:**
- Train on 3,500 employees
- Tune hyperparameters using validation set
- Final model trained on training + validation (4,250 employees)

### Model Validation

**Performance on Test Set (750 employees):**
- **Accuracy:** 87%
- **Precision:** 72% (of predicted leavers, 72% actually left)
- **Recall:** 65% (of actual leavers, 65% were predicted)
- **F1 Score:** 0.68
- **AUC-ROC:** 0.84 (good discrimination)

**Confusion Matrix:**
|  | Predicted Stay | Predicted Leave |
|---|---|---|
| **Actually Stayed** | 620 (True Negative) | 55 (False Positive) |
| **Actually Left** | 26 (False Negative) | 49 (True Positive) |

**Interpretation:**
- Model correctly identifies 65% of leavers (49 of 75)
- 28% false alarm rate (55 of 675 stayers incorrectly flagged)
- Misses 35% of leavers (26 of 75)

**Business Impact:**
- Without model: 10% turnover rate, 500 leavers per year
- With model: Identify 325 at-risk employees (65% of 500)
- If interventions retain 30%: Save 98 employees
- Cost savings: 98 employees x $50K turnover cost = $4.9M

### Feature Importance

**Top 10 Predictive Features:**
1. Manager effectiveness score (25% importance)
2. Engagement score (18%)
3. Compensation gap (12%)
4. Time since last promotion (10%)
5. Performance rating (8%)
6. Tenure (6%)
7. Work-life balance score (5%)
8. Career development satisfaction (4%)
9. Commute distance (3%)
10. Market demand for role (3%)

**Insights:**
- Manager relationship is #1 driver of turnover
- Compensation matters, but less than engagement and manager
- Career progression (promotions) is critical
- Actionable: Focus retention efforts on manager training, compensation equity, career development

### Deployment

**Scoring:**
- Score all employees monthly
- Generate turnover risk score (0-100%)
- Categorize: High risk (>70%), Medium (40-70%), Low (<40%)

**Dashboard:**
- Manager dashboard showing team members' risk scores
- HR dashboard showing high-risk employees across organization
- Drill-down to see feature contributions (why is this person at risk?)

**Alerts:**
- Automated email to manager when employee moves to high risk
- Monthly report to HR leadership on turnover risk trends

**Interventions:**
- **High Risk:** Mandatory manager conversation, HR review, compensation analysis, role/development discussion
- **Medium Risk:** Manager check-in, engagement survey follow-up
- **Low Risk:** Continue monitoring

### Monitoring and Refresh

**Performance Tracking:**
- Monthly: Compare predictions to actual turnover
- Quarterly: Recalculate accuracy, precision, recall
- Alert if performance drops below threshold (AUC < 0.75)

**Model Refresh:**
- Annually: Retrain model with latest data
- Ad-hoc: If significant performance drift or business changes
- Version control: Track model versions and performance

**Continuous Improvement:**
- Gather feedback from managers on prediction accuracy
- Track intervention effectiveness
- Incorporate new data sources (e.g., collaboration patterns, skills data)
- Experiment with new algorithms

---

## Hiring Success Prediction Model

### Business Problem
Improve quality of hire by predicting which candidates will be high performers, reducing mis-hires and time-to-productivity.

### Data Collection

**Outcome Variable:**
- **High Performer:** 1 if performance rating >= 4 after 12 months, 0 otherwise
- **Timeframe:** Predict performance 12 months after hire
- **Historical Data:** 2,000 hires over 3 years with 12+ month tenure

**Predictor Variables:**

*Resume/Application:*
- Education level (high school, bachelor's, master's, PhD)
- Years of relevant experience
- Number of previous jobs
- Average tenure at previous jobs
- Industry experience (yes/no)
- Skills match score (% of required skills)

*Assessments:*
- Cognitive ability test score (0-100)
- Personality assessment scores (Big Five)
- Technical skills assessment score (0-100)
- Work sample test score (0-100)

*Interview:*
- Interview scores from each interviewer (1-5)
- Average interview score
- Interview score variance (consistency across interviewers)
- Behavioral interview score
- Technical interview score

*Hiring Process:*
- Hire source (referral, job board, agency, campus)
- Time-to-hire (days)
- Number of interview rounds
- Hiring manager experience (years)

**Sample Size:** 2,000 hires, 600 high performers (30% high performer rate)

### Model Training

**Algorithm:** Gradient Boosting (XGBoost) for maximum accuracy

**Performance:**
- **Accuracy:** 78%
- **Precision:** 65% (of predicted high performers, 65% actually are)
- **Recall:** 70% (of actual high performers, 70% are predicted)
- **AUC-ROC:** 0.81

### Feature Importance

**Top Predictors:**
1. Work sample test score (22%)
2. Average interview score (18%)
3. Technical skills assessment (15%)
4. Cognitive ability test (12%)
5. Years of relevant experience (10%)
6. Hire source (8%)
7. Skills match score (6%)
8. Education level (5%)

**Insights:**
- Work sample tests are best predictor (simulate actual job)
- Interview scores matter, but less than objective assessments
- Referrals perform better than other sources
- Education level is weak predictor (experience matters more)

### Deployment

**Scoring:**
- Score candidates during hiring process
- Generate "predicted performance" score (0-100)
- Provide to hiring manager before final decision

**Decision Support:**
- Not automated decision (human makes final call)
- Prediction is one input among many
- Helps identify high-potential candidates
- Flags candidates who may struggle

**Impact:**
- 15% improvement in quality of hire (more high performers hired)
- 20% reduction in time-to-productivity
- $500K annual savings from reduced mis-hires

---

## Performance Forecasting Model

### Business Problem
Identify high-potential employees for succession planning and target development resources effectively.

### Data Collection

**Outcome Variable:**
- **Future Performance Rating:** Performance rating 12 months from now (1-5 scale)
- **Historical Data:** 3 years of performance data for 3,000 employees

**Predictor Variables:**
- Historical performance ratings (last 3 years)
- Performance trend (improving, stable, declining)
- Goal achievement rate
- 360-degree feedback scores
- Skills assessment scores
- Training completion rate
- Manager effectiveness score
- Tenure, job level, department

### Model Training

**Algorithm:** Linear Regression (predicting continuous outcome)

**Performance:**
- **R-squared:** 0.62 (explains 62% of variance in future performance)
- **RMSE:** 0.45 (average error of 0.45 rating points)

### Feature Importance

**Top Predictors:**
1. Current performance rating (35%)
2. Performance trend (20%)
3. Goal achievement rate (15%)
4. 360-degree feedback scores (12%)
5. Manager effectiveness (10%)

### Deployment

**Use Cases:**
- **Succession Planning:** Identify high-potential employees for leadership pipeline
- **Development:** Target development resources to employees with highest growth potential
- **Retention:** Proactively retain high-performers before they become flight risks

---

## Best Practices

### 1. Start Simple
- Begin with logistic regression or decision tree
- Establish baseline performance
- Add complexity only if needed

### 2. Prioritize Interpretability
- Stakeholders need to understand and trust model
- Black-box models (neural networks) harder to explain
- Feature importance and SHAP values help interpretation

### 3. Validate Rigorously
- Use holdout test set, not just training performance
- Cross-validation for robust estimates
- Monitor performance over time

### 4. Audit for Bias
- Check for disparate impact across demographics
- Remove biased features if necessary
- Regular bias audits (quarterly or annually)

### 5. Combine with Human Judgment
- Models inform, don't replace human decisions
- Provide context and recommendations, not just scores
- Allow for exceptions and overrides

### 6. Iterate and Improve
- Models degrade over time (concept drift)
- Refresh annually or when performance drops
- Incorporate new data sources and features
- Learn from prediction errors

### 7. Measure Business Impact
- Track ROI of predictive analytics
- Calculate cost savings (reduced turnover, better hires)
- Measure changes in key outcomes
- Share success stories with leadership

---

## Common Pitfalls

1. **Insufficient Data:** Need enough historical data and outcomes (minimum 200-500 samples)
2. **Data Leakage:** Using future information to predict past (inflates performance)
3. **Overfitting:** Model too complex, performs well on training but poorly on new data
4. **Ignoring Bias:** Models can perpetuate existing biases if not audited
5. **No Action:** Building model without plan for how to use predictions
6. **Black Box:** Model too complex to explain to stakeholders
7. **Set and Forget:** Not monitoring or refreshing model over time
8. **Replacing Judgment:** Over-relying on model, ignoring human context
