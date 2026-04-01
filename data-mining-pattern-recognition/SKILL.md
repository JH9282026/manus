---
name: "data-mining-pattern-recognition"
description: "Discover hidden patterns, relationships, and anomalies in large datasets using statistical analysis and machine learning to extract actionable insights. Use for: customer segmentation via clustering, association rule mining, anomaly/fraud detection, dimensionality reduction, text mining, sequence pattern analysis, and knowledge discovery from structured and unstructured data."
---

# Data Mining & Pattern Recognition

Extract meaningful patterns, relationships, and knowledge from large, complex datasets using statistical methods and machine learning algorithms.

## Overview

Transform vast quantities of raw data into actionable knowledge by identifying regularities, anomalies, clusters, associations, and trends. Apply supervised and unsupervised learning approaches guided by data characteristics, business objectives, and interpretability requirements.

## Mining Technique Selection

| Objective | Technique | Algorithm | Output |
|-----------|-----------|-----------|--------|
| Find customer groups | Clustering | K-Means, DBSCAN, Hierarchical | Segment assignments + profiles |
| Find purchase patterns | Association rules | Apriori, FP-Growth | If-then rules with support/confidence |
| Detect outliers/fraud | Anomaly detection | Isolation Forest, LOF, Autoencoder | Anomaly scores + flagged records |
| Reduce complexity | Dimensionality reduction | PCA, t-SNE, UMAP | Reduced feature set, visualizations |
| Find sequential patterns | Sequence mining | GSP, PrefixSpan | Frequent sequences |
| Extract text patterns | Text mining | TF-IDF, LDA, NMF | Topics, keywords, themes |
| Predict outcomes | Supervised learning | Random Forest, XGBoost | Predictions + feature importance |

## Clustering Deep Dive

### Algorithm Selection

| Algorithm | Shape | Scalability | Parameters | Noise Handling |
|-----------|-------|-------------|------------|----------------|
| K-Means | Spherical | Excellent | k (cluster count) | Poor |
| DBSCAN | Arbitrary | Good | eps, min_samples | Excellent |
| Hierarchical | Arbitrary | Poor (large data) | Distance, linkage | Poor |
| Gaussian Mixture | Elliptical | Good | n_components | Moderate |
| HDBSCAN | Arbitrary | Good | min_cluster_size | Excellent |

### Determining Optimal Clusters

| Method | Approach | Interpretation |
|--------|----------|----------------|
| Elbow Method | Plot inertia vs. k | Look for "elbow" bend |
| Silhouette Score | Average silhouette (0-1) | Higher = better separation |
| Gap Statistic | Compare to random reference | Largest gap = optimal k |
| Domain knowledge | Business-meaningful groupings | Must be actionable |

## Association Rule Mining

### Key Metrics

| Metric | Formula | Interpretation |
|--------|---------|----------------|
| Support | freq(A∪B) / N | How often items appear together |
| Confidence | support(A∪B) / support(A) | Probability of B given A |
| Lift | confidence / support(B) | Strength beyond random co-occurrence |

**Interpretation**: Lift > 1 = positive association, Lift = 1 = independent, Lift < 1 = negative association

### Minimum Thresholds

- **Support**: 0.01-0.05 (1-5% of transactions)
- **Confidence**: 0.5-0.8 (50-80% conditional probability)
- **Lift**: >1.5 for meaningful association

## Anomaly Detection Framework

| Method | Type | Best For |
|--------|------|----------|
| Z-score | Statistical | Univariate, normal distribution |
| IQR-based | Statistical | Univariate, any distribution |
| Isolation Forest | ML (unsupervised) | High-dimensional, mixed types |
| Local Outlier Factor | Density-based | Local anomalies in clusters |
| Autoencoder | Deep learning | Complex patterns, large datasets |
| DBSCAN noise points | Clustering-based | Spatial/density anomalies |

## Pattern Validation Checklist

1. **Statistical significance** — Is the pattern unlikely to occur by chance?
2. **Effect size** — Is the pattern large enough to matter?
3. **Business relevance** — Does the pattern align with domain knowledge?
4. **Stability** — Does the pattern hold across different time periods or samples?
5. **Actionability** — Can the organization act on this pattern?
6. **Novelty** — Is this genuinely new insight or already known?

## Using the Reference Files

### When to Read Each Reference

**`/references/clustering-segmentation.md`** — Read when performing cluster analysis, profiling segments, or validating cluster quality.

**`/references/association-anomaly-text-mining.md`** — Read when mining association rules, detecting anomalies/fraud, performing text mining, or applying dimensionality reduction techniques.

## Reference Files

This skill includes the following detailed reference materials:

- [Association Anomaly Text Mining](./references/association-anomaly-text-mining.md)
- [Clustering Segmentation](./references/clustering-segmentation.md)
