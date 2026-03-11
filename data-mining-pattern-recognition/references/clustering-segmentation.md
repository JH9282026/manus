# Clustering & Segmentation

## K-Means Clustering

### Implementation Workflow

1. **Prepare data**: Standardize all features to same scale (StandardScaler)
2. **Select k**: Use elbow method, silhouette analysis, and domain knowledge
3. **Run algorithm**: Initialize with k-means++ for better convergence
4. **Evaluate**: Check silhouette scores, cluster sizes, and separation
5. **Profile clusters**: Analyze centroid characteristics and distributions
6. **Name segments**: Assign business-meaningful labels
7. **Validate**: Test stability with different random seeds and holdout data

### K-Means Assumptions and Limitations
- Assumes spherical, equally-sized clusters
- Sensitive to initialization (mitigated by k-means++)
- Sensitive to outliers (consider removing or using k-medoids)
- Requires specifying k in advance
- All features contribute equally (consider feature selection)

---

## DBSCAN Clustering

### Parameter Selection

**eps (neighborhood radius)**:
- Use k-distance plot: Plot sorted distance to k-th nearest neighbor
- Look for the "elbow" in the curve
- k typically = 2 × dimensions - 1 (minimum 3)

**min_samples (minimum neighbors)**:
- Rule of thumb: min_samples ≥ dimensions + 1
- Higher values = more conservative (fewer, denser clusters)
- Lower values = more clusters, more noise tolerance

### Advantages Over K-Means
- Does not require specifying number of clusters
- Finds arbitrarily shaped clusters
- Naturally identifies noise points (outliers)
- Robust to outliers in cluster formation

---

## Hierarchical Clustering

### Linkage Methods

| Method | Description | Tendency |
|--------|-------------|----------|
| Single | Minimum distance between clusters | Chain-like, elongated clusters |
| Complete | Maximum distance between clusters | Compact, spherical clusters |
| Average | Mean distance between all pairs | Balanced approach |
| Ward | Minimize within-cluster variance | Compact, equal-sized clusters |

### Dendrogram Interpretation
1. Height of merge = distance at which clusters join
2. Long vertical lines = well-separated clusters
3. Cut the dendrogram horizontally to get desired number of clusters
4. Inconsistency coefficient identifies natural cluster boundaries

---

## Cluster Profiling and Validation

### Profiling Approach

For each cluster, analyze:
1. **Size**: Number and percentage of records
2. **Centroids**: Mean values for each feature
3. **Distribution**: Full distribution of key variables
4. **Distinguishing features**: What makes this cluster unique
5. **Business interpretation**: What type of entity does this represent

### Validation Metrics

| Metric | Range | Interpretation |
|--------|-------|----------------|
| Silhouette Score | -1 to 1 | >0.5 good, >0.7 excellent |
| Calinski-Harabasz | Higher = better | Ratio of between/within variance |
| Davies-Bouldin | Lower = better | Average cluster similarity |
| Dunn Index | Higher = better | Ratio of min inter/max intra |

### Cluster Stability Testing
- Run with multiple random seeds (>10) and check consistency
- Bootstrap resampling: Cluster on samples, measure assignment stability
- Cross-validation: Cluster on training set, predict test set assignments
- Feature perturbation: Add noise to features, check if clusters persist

---

## Gaussian Mixture Models

### When to Use GMMs Over K-Means
- Clusters have different sizes or elliptical shapes
- Soft assignments needed (probability of membership)
- Overlapping clusters expected
- Need statistical model for cluster generation

### Model Selection
- Use BIC (Bayesian Information Criterion) to choose number of components
- Lower BIC = better model fit with complexity penalty
- Try covariance types: full, tied, diagonal, spherical
