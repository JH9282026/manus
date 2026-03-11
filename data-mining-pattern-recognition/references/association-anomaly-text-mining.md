# Association Rules, Anomaly Detection & Text Mining

## Association Rule Mining

### Apriori Algorithm

**Process**:
1. Set minimum support threshold
2. Find all frequent individual items (1-itemsets)
3. Generate candidate 2-itemsets from frequent 1-itemsets
4. Prune candidates below minimum support
5. Repeat: generate k+1 itemsets from frequent k-itemsets
6. Stop when no more frequent itemsets found
7. Generate rules from frequent itemsets
8. Filter rules by minimum confidence and lift

**Practical Tips**:
- Start with higher support, lower gradually to find useful rules
- Very low support generates explosion of rules (computational cost)
- Filter by lift > 1.5 for practically meaningful associations
- Check rule direction (A→B vs B→A may have different confidence)

### FP-Growth Algorithm
- More efficient than Apriori for large datasets
- Builds FP-tree structure (compressed database representation)
- Avoids costly candidate generation step
- Same output as Apriori but significantly faster

### Interpreting Association Rules

| Rule Example | Support | Confidence | Lift | Interpretation |
|-------------|---------|-----------|------|----------------|
| {bread, butter} → {milk} | 0.05 | 0.65 | 2.1 | Strong positive association |
| {laptop} → {mouse} | 0.03 | 0.45 | 3.5 | Very strong cross-sell opportunity |
| {diapers} → {beer} | 0.01 | 0.30 | 1.8 | Moderate but noteworthy |

### Applications
- **Retail**: Market basket analysis, product placement, cross-selling
- **Web**: Page navigation patterns, recommendation engines
- **Healthcare**: Symptom co-occurrence, drug interaction patterns
- **Manufacturing**: Failure pattern co-occurrence

---

## Anomaly Detection

### Isolation Forest

**How it works**:
- Randomly select feature and split value
- Anomalies are isolated in fewer splits (shorter path length)
- Score based on average path length across many trees
- Contamination parameter sets expected anomaly proportion

**Best practices**:
- Set contamination to expected anomaly rate (if known)
- Default contamination: 0.1 (10%) — adjust based on domain
- Works well with high-dimensional data
- Does not require labeled anomaly data

### Local Outlier Factor (LOF)

**How it works**:
- Compares local density of a point to its neighbors
- LOF score > 1 indicates lower density than neighbors (anomaly)
- Effective for detecting local anomalies within clusters

**Parameters**:
- n_neighbors: 20 (default), higher = smoother, lower = more sensitive
- Contamination: Expected proportion of anomalies

### Autoencoder-Based Detection

**Architecture**:
- Encoder compresses input to low-dimensional representation
- Decoder reconstructs input from compressed representation
- Train on normal data only
- High reconstruction error = anomaly

**When to use**:
- Complex, high-dimensional data
- Need to learn non-linear patterns
- Large enough training data (>10K normal samples)

---

## Text Mining

### Text Preprocessing Pipeline

1. **Tokenization** — Split text into words/tokens
2. **Lowercasing** — Standardize case
3. **Stop word removal** — Remove common words (the, is, at)
4. **Stemming/Lemmatization** — Reduce to root form
5. **N-gram creation** — Capture multi-word phrases
6. **Vectorization** — Convert to numeric representation

### Topic Modeling

**Latent Dirichlet Allocation (LDA)**:
- Discovers latent topics in document collection
- Each document is a mixture of topics
- Each topic is a distribution over words
- Choose number of topics using coherence score

**Non-Negative Matrix Factorization (NMF)**:
- Factorizes TF-IDF matrix into topic and document matrices
- Generally produces more interpretable topics than LDA
- Faster computation for moderate-sized corpora

### Sentiment Analysis Approaches

| Approach | Method | Best For |
|----------|--------|----------|
| Lexicon-based | VADER, TextBlob | Quick analysis, social media |
| ML classifier | Naive Bayes, SVM | Domain-specific sentiment |
| Transformer | BERT, RoBERTa | High accuracy, nuanced text |

---

## Dimensionality Reduction

### PCA (Principal Component Analysis)
- Linear method, preserves global structure
- Choose components explaining 80-95% of variance
- Interpretable through component loadings
- Fast, scalable to large datasets

### t-SNE
- Non-linear, preserves local neighborhood structure
- Best for visualization (2D/3D only)
- Perplexity parameter (5-50) controls neighborhood size
- Results vary between runs (not deterministic without seed)
- Do not interpret distances between clusters literally

### UMAP
- Non-linear, preserves both local and global structure
- Faster than t-SNE, scales better
- n_neighbors controls local vs. global balance
- min_dist controls point clustering tightness
- More reliable cluster separation than t-SNE
