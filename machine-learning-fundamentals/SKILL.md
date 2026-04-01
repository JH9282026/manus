---
name: machine-learning-fundamentals
description: "Master core machine learning algorithms, supervised learning, unsupervised learning, and reinforcement learning. Use for classification, regression, clustering, dimensionality reduction, model training, evaluation, feature engineering, and algorithm selection."
---

# Machine Learning Fundamentals

Master core machine learning algorithms and techniques across supervised, unsupervised, and reinforcement learning paradigms.

## Overview

This skill provides comprehensive guidance for machine learning fundamentals covering algorithm selection, model training, evaluation, and optimization. It addresses supervised learning for predictive tasks, unsupervised learning for pattern discovery, and reinforcement learning for decision-making systems.

## Quick Reference

| Scenario | Recommended Approach | Reference File |
|----------|---------------------|----------------|
| Predicting outcomes with labeled data (classification, regression) | Supervised learning algorithms | `/references/supervised-learning.md` |
| Discovering patterns in unlabeled data (clustering, dimensionality reduction) | Unsupervised learning techniques | `/references/unsupervised-learning.md` |
| Training agents through trial-and-error with rewards | Reinforcement learning methods | `/references/reinforcement-learning.md` |
| Preparing and transforming data for model training | Feature engineering and preprocessing | `/references/feature-engineering.md` |
| Evaluating model performance and preventing overfitting | Model evaluation and validation | `/references/model-evaluation.md` |

## Core Principles

1. **Algorithm Selection** - Choose algorithms based on problem type, data characteristics, and performance requirements
2. **Data Quality** - Ensure clean, representative data with proper preprocessing and feature engineering
3. **Generalization** - Build models that perform well on unseen data, not just training data
4. **Evaluation Rigor** - Use appropriate metrics and validation strategies for reliable performance assessment
5. **Iterative Refinement** - Continuously improve through experimentation, hyperparameter tuning, and ensemble methods

## Learning Paradigms

### Supervised Learning
Train models on labeled data to predict outcomes for new inputs. The model learns the mapping between features and targets.

**Key Characteristics:**
- Requires labeled training data with input-output pairs
- Aims to minimize prediction error on validation data
- Supports both classification (discrete labels) and regression (continuous values)

**Common Algorithms:**
- Linear/Logistic Regression for baseline models
- Decision Trees and Random Forests for interpretable, non-linear patterns
- Support Vector Machines for high-dimensional classification
- Gradient Boosting (XGBoost, LightGBM, CatBoost) for tabular data
- Neural Networks for complex, high-capacity modeling

### Unsupervised Learning
Discover hidden patterns and structures in unlabeled data without predefined targets.

**Key Characteristics:**
- Works with unlabeled data
- Identifies natural groupings, associations, or reduced representations
- No "correct" answers to validate against

**Common Algorithms:**
- K-Means and Hierarchical Clustering for grouping similar data
- DBSCAN for density-based clustering with noise handling
- PCA and t-SNE for dimensionality reduction and visualization
- Autoencoders for learning compressed representations

### Reinforcement Learning
Train agents to make sequential decisions by maximizing cumulative rewards through environmental interaction.

**Key Characteristics:**
- Learns through trial-and-error with reward signals
- Balances exploration (trying new actions) and exploitation (using known good actions)
- Suitable for sequential decision-making problems

**Common Algorithms:**
- Q-Learning for discrete action spaces
- Deep Q-Networks (DQN) for high-dimensional state spaces
- Policy Gradient methods for continuous control
- Actor-Critic algorithms for stable, efficient learning

## Model Development Workflow

### Phase 1: Problem Definition and Data Preparation
- Define clear objectives and success metrics
- Collect and explore data to understand distributions and relationships
- Clean data by handling missing values, outliers, and inconsistencies
- Engineer features to capture relevant patterns
- Split data into training, validation, and test sets

### Phase 2: Model Selection and Training
- Select candidate algorithms based on problem type and data characteristics
- Establish baseline performance with simple models
- Train models on training data with appropriate hyperparameters
- Monitor training metrics to detect overfitting or underfitting
- Apply regularization techniques to improve generalization

### Phase 3: Evaluation and Validation
- Evaluate models on validation data using appropriate metrics
- Perform cross-validation for robust performance estimates
- Analyze errors to identify systematic failures
- Compare multiple models using consistent evaluation protocols
- Select best model based on validation performance and business requirements

### Phase 4: Optimization and Deployment
- Tune hyperparameters using grid search, random search, or Bayesian optimization
- Consider ensemble methods to combine multiple models
- Validate final model on held-out test set
- Document model assumptions, limitations, and performance characteristics
- Deploy model with monitoring for performance degradation

## Algorithm Selection Guide

| Problem Type | Data Characteristics | Recommended Algorithms |
|--------------|---------------------|------------------------|
| Binary Classification | Small dataset, linear patterns | Logistic Regression, SVM |
| Binary Classification | Large dataset, non-linear | Random Forest, Gradient Boosting, Neural Networks |
| Multi-class Classification | Tabular data | XGBoost, LightGBM, Random Forest |
| Multi-class Classification | Image/text data | Convolutional/Recurrent Neural Networks |
| Regression | Linear relationships | Linear Regression, Ridge, Lasso |
| Regression | Non-linear relationships | Random Forest, Gradient Boosting, Neural Networks |
| Clustering | Known number of clusters | K-Means |
| Clustering | Unknown clusters, noise present | DBSCAN, Hierarchical Clustering |
| Dimensionality Reduction | Linear relationships | PCA |
| Dimensionality Reduction | Non-linear manifolds | t-SNE, UMAP, Autoencoders |
| Sequential Decision-Making | Discrete actions, small state space | Q-Learning, SARSA |
| Sequential Decision-Making | Continuous actions, complex states | Deep RL (DQN, PPO, A3C) |

## Using the Reference Files

**`/references/supervised-learning.md`** — Detailed coverage of classification and regression algorithms including Linear/Logistic Regression, Decision Trees, Random Forests, SVM, Gradient Boosting, and Neural Networks with implementation guidance.

**`/references/unsupervised-learning.md`** — Comprehensive guide to clustering algorithms (K-Means, Hierarchical, DBSCAN), dimensionality reduction techniques (PCA, t-SNE, UMAP), and association rule learning.

**`/references/reinforcement-learning.md`** — In-depth exploration of RL concepts including Markov Decision Processes, Q-Learning, Deep Q-Networks, Policy Gradients, Actor-Critic methods, and practical applications.

**`/references/feature-engineering.md`** — Techniques for data preprocessing, feature extraction, transformation, selection, and encoding categorical variables to improve model performance.

**`/references/model-evaluation.md`** — Evaluation metrics for classification (accuracy, precision, recall, F1, ROC-AUC) and regression (MSE, RMSE, MAE, R²), cross-validation strategies, and techniques to prevent overfitting.

## Best Practices

- Start with simple baseline models before trying complex algorithms
- Always split data properly to prevent data leakage and overfitting
- Use cross-validation for robust performance estimates on small datasets
- Monitor both training and validation metrics to detect overfitting early
- Apply feature scaling (standardization, normalization) for distance-based algorithms
- Handle class imbalance with resampling, class weights, or appropriate metrics
- Document all preprocessing steps and transformations for reproducibility
- Validate assumptions of chosen algorithms (e.g., linearity, independence)
- Consider computational cost and interpretability alongside accuracy
- Test final model on completely held-out test data only once

## Common Pitfalls to Avoid

- Training and testing on the same data (data leakage)
- Ignoring class imbalance in classification problems
- Over-relying on accuracy when classes are imbalanced
- Applying feature scaling after train-test split instead of before
- Tuning hyperparameters on test data instead of validation data
- Using too many features relative to sample size (curse of dimensionality)
- Ignoring domain knowledge in feature engineering
- Failing to handle missing data appropriately
- Not checking for multicollinearity in linear models
- Deploying models without monitoring for distribution shift

## Key Frameworks and Libraries

**Python Ecosystem:**
- scikit-learn for classical ML algorithms and preprocessing
- XGBoost, LightGBM, CatBoost for gradient boosting
- TensorFlow and PyTorch for deep learning
- pandas and NumPy for data manipulation
- matplotlib and seaborn for visualization

**R Ecosystem:**
- caret for unified ML interface
- randomForest, xgboost for tree-based methods
- glmnet for regularized linear models
- ggplot2 for visualization

## Performance Optimization

**Hyperparameter Tuning:**
- Grid Search for exhaustive search over small parameter spaces
- Random Search for efficient exploration of large parameter spaces
- Bayesian Optimization for sample-efficient tuning
- Automated ML (AutoML) tools for end-to-end optimization

**Ensemble Methods:**
- Bagging (Bootstrap Aggregating) to reduce variance
- Boosting to reduce bias and improve weak learners
- Stacking to combine diverse model types
- Voting classifiers for robust predictions

**Regularization:**
- L1 (Lasso) for feature selection and sparsity
- L2 (Ridge) for handling multicollinearity
- Elastic Net for combined L1/L2 regularization
- Dropout for neural network regularization

## Evaluation Metrics Summary

**Classification:**
- Accuracy: Overall correctness (use with balanced classes)
- Precision: Correctness of positive predictions
- Recall: Coverage of actual positives
- F1 Score: Harmonic mean of precision and recall
- ROC-AUC: Discrimination ability across thresholds
- Confusion Matrix: Detailed breakdown of predictions

**Regression:**
- Mean Squared Error (MSE): Average squared prediction error
- Root Mean Squared Error (RMSE): MSE in original units
- Mean Absolute Error (MAE): Average absolute error
- R² Score: Proportion of variance explained
- Mean Absolute Percentage Error (MAPE): Percentage-based error

**Clustering:**
- Silhouette Score: Cluster cohesion and separation
- Davies-Bouldin Index: Average similarity between clusters
- Calinski-Harabasz Index: Ratio of between-cluster to within-cluster variance
- Adjusted Rand Index: Agreement with ground truth (if available)
