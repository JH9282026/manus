# Unsupervised Learning Techniques

Comprehensive guide to discovering patterns and structures in unlabeled data.

---

## Overview

Unsupervised learning identifies hidden patterns, groupings, and structures in data without predefined labels. Unlike supervised learning, there are no "correct" answers to validate against. Instead, algorithms discover natural organization in data, making them invaluable for exploratory analysis, data compression, and anomaly detection.

## Clustering Algorithms

Clustering groups similar data points together based on feature similarity.

### K-Means Clustering

**Concept:** Partitions data into K clusters by minimizing within-cluster variance.

**How It Works:**
1. Initialize K cluster centroids randomly
2. Assign each point to nearest centroid (Euclidean distance)
3. Recalculate centroids as mean of assigned points
4. Repeat steps 2-3 until convergence (centroids stop moving)

**Strengths:**
- Simple, fast, and scalable to large datasets
- Works well with spherical, evenly-sized clusters
- Easy to interpret and implement
- Efficient with O(n*K*i) complexity (n=samples, i=iterations)

**Limitations:**
- Requires specifying K in advance
- Sensitive to initial centroid placement
- Assumes spherical clusters of similar size
- Struggles with non-convex shapes
- Sensitive to outliers

**Use Cases:**
- Customer segmentation
- Image compression (color quantization)
- Document clustering
- Market basket analysis

**Implementation Tips:**
- Use Elbow Method or Silhouette Score to choose K
- Run multiple times with different initializations (K-Means++)
- Standardize features before clustering
- Consider Mini-Batch K-Means for very large datasets

**Choosing K:**
- Elbow Method: Plot within-cluster sum of squares vs K, look for "elbow"
- Silhouette Score: Measure cluster cohesion and separation
- Domain knowledge: Use business context to guide K selection

### Hierarchical Clustering

**Concept:** Builds a tree-like hierarchy of clusters through iterative merging (agglomerative) or splitting (divisive).

**How It Works (Agglomerative):**
1. Start with each point as its own cluster
2. Merge two closest clusters based on linkage criterion
3. Repeat until single cluster remains
4. Cut dendrogram at desired height to get K clusters

**Linkage Methods:**
- Single: Minimum distance between cluster points (sensitive to outliers)
- Complete: Maximum distance (produces compact clusters)
- Average: Mean distance between all pairs
- Ward: Minimizes within-cluster variance (most common)

**Strengths:**
- No need to specify K in advance
- Produces dendrogram for visualization
- Works with any distance metric
- Captures hierarchical structure in data

**Limitations:**
- Computationally expensive: O(n²log(n)) or O(n³)
- Not suitable for very large datasets
- Sensitive to noise and outliers
- Cannot undo previous merges (greedy)

**Use Cases:**
- Taxonomy creation
- Gene expression analysis
- Social network analysis
- When hierarchical relationships exist

**Implementation Tips:**
- Use Ward linkage for balanced clusters
- Visualize dendrogram to choose cut height
- Consider BIRCH for large datasets
- Standardize features before clustering

### DBSCAN (Density-Based Spatial Clustering)

**Concept:** Groups points that are closely packed together, marking points in low-density regions as outliers.

**How It Works:**
1. Define neighborhood: Points within ε (epsilon) distance
2. Core points: Have at least minPts neighbors
3. Border points: Within ε of core point but not core themselves
4. Noise points: Neither core nor border
5. Expand clusters from core points

**Strengths:**
- Discovers clusters of arbitrary shape
- Robust to outliers (marks them as noise)
- No need to specify number of clusters
- Works well with spatial data

**Limitations:**
- Struggles with varying density clusters
- Sensitive to ε and minPts parameters
- Not suitable for high-dimensional data (curse of dimensionality)
- Computationally expensive without spatial indexing

**Use Cases:**
- Anomaly detection
- Geographic data clustering
- When clusters have irregular shapes
- Noise filtering

**Implementation Tips:**
- Use K-distance graph to choose ε (look for "knee")
- Set minPts = 2*dimensions as starting point
- Use spatial indexing (KD-tree, Ball-tree) for efficiency
- Standardize features, especially with mixed scales

## Dimensionality Reduction

Reduces number of features while preserving important information.

### Principal Component Analysis (PCA)

**Concept:** Linear transformation that projects data onto orthogonal axes (principal components) that capture maximum variance.

**How It Works:**
1. Standardize features to zero mean, unit variance
2. Compute covariance matrix
3. Calculate eigenvectors and eigenvalues
4. Sort eigenvectors by eigenvalues (descending)
5. Project data onto top K eigenvectors

**Strengths:**
- Reduces dimensionality while preserving variance
- Removes multicollinearity
- Speeds up training of downstream models
- Enables visualization in 2D/3D
- Unsupervised, no labels required

**Limitations:**
- Assumes linear relationships
- Principal components are linear combinations (less interpretable)
- Sensitive to feature scaling
- May discard useful information in low-variance components

**Use Cases:**
- Preprocessing for machine learning
- Data visualization
- Noise reduction
- Feature extraction from images

**Implementation Tips:**
- Always standardize features first
- Use scree plot to choose number of components
- Retain components explaining 80-95% of variance
- Consider Kernel PCA for non-linear relationships

**Choosing Number of Components:**
- Cumulative explained variance: Retain components explaining 80-95% variance
- Scree plot: Look for "elbow" in eigenvalue plot
- Cross-validation: Test downstream model performance

### t-SNE (t-Distributed Stochastic Neighbor Embedding)

**Concept:** Non-linear dimensionality reduction optimized for visualization by preserving local structure.

**How It Works:**
1. Compute pairwise similarities in high-dimensional space
2. Initialize low-dimensional embedding randomly
3. Compute pairwise similarities in low-dimensional space
4. Minimize divergence between high and low-dimensional distributions
5. Use gradient descent to optimize embedding

**Strengths:**
- Excellent for visualization (2D/3D)
- Preserves local structure and clusters
- Reveals non-linear patterns
- Works well with complex, high-dimensional data

**Limitations:**
- Computationally expensive: O(n²)
- Non-deterministic (different runs produce different results)
- Cannot transform new data (no inverse transform)
- Global structure not preserved
- Sensitive to hyperparameters (perplexity)

**Use Cases:**
- Visualizing high-dimensional data
- Exploratory data analysis
- Image and text embeddings visualization
- Cluster discovery

**Implementation Tips:**
- Use PCA to reduce to 50 dimensions first (for speed)
- Tune perplexity (5-50, typically 30)
- Run multiple times with different seeds
- Use for visualization only, not as preprocessing

### UMAP (Uniform Manifold Approximation and Projection)

**Concept:** Modern alternative to t-SNE that preserves both local and global structure.

**Strengths:**
- Faster than t-SNE
- Preserves global structure better
- Can transform new data
- More stable across runs

**Use Cases:**
- Same as t-SNE but with better scalability
- When global structure matters
- Preprocessing for clustering

**Implementation Tips:**
- Tune n_neighbors (2-100, typically 15)
- Adjust min_dist (0.0-0.99) for cluster separation
- Use for both visualization and preprocessing

### Autoencoders

**Concept:** Neural networks that learn compressed representations by reconstructing inputs.

**How It Works:**
1. Encoder: Compresses input to lower-dimensional latent space
2. Decoder: Reconstructs input from latent representation
3. Train to minimize reconstruction error
4. Use latent space as reduced representation

**Strengths:**
- Learns non-linear transformations
- Flexible architecture for different data types
- Can generate new samples (variational autoencoders)
- Scales to large datasets

**Limitations:**
- Requires careful architecture design
- Computationally expensive to train
- Needs large amounts of data
- Black-box nature limits interpretability

**Use Cases:**
- Image compression and denoising
- Anomaly detection (high reconstruction error)
- Feature learning for downstream tasks
- Generative modeling (VAE)

**Implementation Tips:**
- Start with simple architecture (1-2 hidden layers)
- Use ReLU activation in hidden layers
- Bottleneck layer size = desired dimensionality
- Add regularization (dropout, weight decay)

## Association Rule Learning

Discovers relationships between variables in large datasets.

### Apriori Algorithm

**Concept:** Finds frequent itemsets and generates association rules (if X then Y).

**Key Metrics:**
- Support: Frequency of itemset in dataset
- Confidence: Likelihood of Y given X
- Lift: Ratio of observed to expected co-occurrence

**Use Cases:**
- Market basket analysis
- Recommendation systems
- Cross-selling strategies

**Implementation Tips:**
- Set minimum support threshold (0.01-0.1)
- Set minimum confidence threshold (0.5-0.8)
- Filter rules by lift > 1 for positive associations

## Anomaly Detection

Identifies unusual patterns that don't conform to expected behavior.

### Isolation Forest

**Concept:** Isolates anomalies by randomly partitioning data; anomalies require fewer splits.

**Strengths:**
- Fast and scalable
- Works well in high dimensions
- No distance metric required

**Use Cases:**
- Fraud detection
- Network intrusion detection
- Quality control

### One-Class SVM

**Concept:** Learns boundary around normal data; points outside are anomalies.

**Use Cases:**
- When only normal data available for training
- Novelty detection

### Local Outlier Factor (LOF)

**Concept:** Measures local density deviation; points in low-density regions are outliers.

**Use Cases:**
- Spatial anomaly detection
- When anomalies are local, not global

## Clustering Evaluation Metrics

**Internal Metrics (no ground truth):**
- Silhouette Score: Measures cluster cohesion and separation (-1 to 1, higher better)
- Davies-Bouldin Index: Average similarity between clusters (lower better)
- Calinski-Harabasz Index: Ratio of between to within-cluster variance (higher better)

**External Metrics (with ground truth):**
- Adjusted Rand Index: Agreement with true labels (0 to 1)
- Normalized Mutual Information: Shared information (0 to 1)
- Fowlkes-Mallows Index: Geometric mean of precision and recall

## Best Practices

**Data Preprocessing:**
- Standardize features for distance-based methods
- Handle missing values appropriately
- Remove or cap outliers if they're not of interest
- Consider feature engineering for better clustering

**Algorithm Selection:**
- K-Means: Fast, spherical clusters, known K
- Hierarchical: Dendrogram needed, small datasets
- DBSCAN: Arbitrary shapes, noise present, unknown K
- PCA: Linear relationships, interpretability less critical
- t-SNE/UMAP: Visualization, non-linear patterns

**Validation:**
- Use multiple metrics to evaluate clustering quality
- Visualize results when possible (2D/3D projections)
- Validate with domain experts
- Test stability across multiple runs
- Compare with baseline (random clustering)

**Interpretation:**
- Profile clusters by examining feature distributions
- Name clusters based on distinguishing characteristics
- Validate findings with domain knowledge
- Use visualization to communicate results
