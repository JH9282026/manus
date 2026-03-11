# Segmentation Methodologies

## Demographic Segmentation

### B2B Firmographic Variables

| Variable | Categories | Application |
|----------|-----------|-------------|
| Company size | SMB (<100), Mid-market (100-999), Enterprise (1000+) | Pricing tiers, sales model |
| Industry | SIC/NAICS codes | Vertical messaging, use cases |
| Revenue | Revenue bands | Deal size expectations |
| Geography | Region, country, urban/rural | Localization, compliance |
| Technology stack | Tools and platforms used | Integration messaging |
| Growth stage | Startup, growth, mature | Product fit, urgency drivers |

### B2C Demographic Variables

| Variable | Categories | Application |
|----------|-----------|-------------|
| Age/Generation | Gen Z, Millennial, Gen X, Boomer | Channel selection, messaging tone |
| Income | Income brackets | Pricing, product tier |
| Education | Levels | Content complexity |
| Life stage | Student, professional, parent, retiree | Need identification |
| Location | Urban, suburban, rural | Distribution, local marketing |

---

## Behavioral Segmentation

### Purchase Behavior Analysis

**Recency-Frequency-Monetary (RFM) Deep Dive**:

Scoring methodology:
1. Rank all customers by each dimension
2. Divide into quintiles (5 equal groups)
3. Assign scores 1-5 (5 = best)
4. Combine for 125 possible segments
5. Group into actionable macro-segments (typically 8-12)

**Engagement Scoring**:
Create composite engagement scores from:
- Website visits and page depth
- Email opens and clicks
- Content downloads
- Event attendance
- Social media interaction
- Product usage frequency and depth
- Support interactions

### Behavioral Clustering with K-Means

1. Select behavioral features (standardize to same scale)
2. Determine optimal cluster count (elbow method, silhouette score)
3. Run K-means clustering algorithm
4. Profile each cluster by dominant characteristics
5. Validate with domain expertise and business context
6. Name segments with descriptive, memorable labels

---

## Psychographic Segmentation

### Values-Based Segmentation

Group customers by underlying values and motivations:

| Value Dimension | Segments | Messaging Approach |
|----------------|----------|-------------------|
| Achievement | Status-seekers, performers | Results, success stories, exclusivity |
| Security | Risk-averse, planners | Guarantees, testimonials, stability |
| Innovation | Early adopters, experimenters | Novelty, technology, cutting-edge |
| Community | Relationship-driven, collaborators | Social proof, belonging, partnership |
| Independence | Self-reliant, DIY | Customization, control, flexibility |

### Attitudes and Lifestyle Mapping

Use survey instruments to map:
- **Activities** — How they spend time
- **Interests** — What they care about
- **Opinions** — What they believe
- **Values** — What principles guide decisions

---

## Needs-Based Segmentation

### Jobs-to-be-Done Framework

Segment by the jobs customers hire your product to do:

1. **Functional jobs** — Practical tasks to accomplish
2. **Emotional jobs** — How they want to feel
3. **Social jobs** — How they want to be perceived

### Outcome-Driven Innovation (ODI)

1. List all desired outcomes for the job
2. Survey customers on importance and satisfaction
3. Calculate opportunity score: Importance + max(Importance - Satisfaction, 0)
4. Segment by clusters of unmet outcomes
5. Target segments with highest opportunity scores

---

## Predictive Segmentation

### Machine Learning Approaches

| Algorithm | Best For | Interpretability |
|-----------|----------|-----------------|
| K-Means | General clustering | Medium |
| Hierarchical | Nested segments | High |
| DBSCAN | Irregular cluster shapes | Medium |
| Gaussian Mixture | Overlapping segments | Medium |
| Latent Class Analysis | Survey-based segmentation | High |

### Dynamic Segmentation

Build models that automatically reassign customers as their behavior changes:
- Trigger-based reassignment (purchase, inactivity, upgrade)
- Periodic batch rescoring (weekly/monthly)
- Real-time scoring for digital interactions
