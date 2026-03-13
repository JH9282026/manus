# Advanced Keyword Research

Comprehensive keyword research strategies for Google Ads Search campaigns including competitor analysis, intent mapping, and forecasting.

---

## Keyword Research Framework

### Phase 1: Seed Keyword Generation

#### Brainstorming Sources
1. **Product/Service Names** - Direct offerings
2. **Customer Language** - How customers describe needs (support tickets, sales calls)
3. **Competitor Websites** - Analyze competitor site content, meta tags
4. **Industry Terms** - Trade publications, forums, Reddit, Quora
5. **Google Autocomplete** - Type seed terms, note suggestions
6. **Related Searches** - Bottom of Google SERP

#### Seed Keyword Categories

| Category | Examples | Intent Level |
|----------|----------|-------------|
| Brand | "nike shoes", "adidas running" | High |
| Product | "running shoes", "trail runners" | Medium-High |
| Generic | "athletic footwear", "sports shoes" | Medium |
| Problem/Need | "shoes for plantar fasciitis" | High |
| Comparison | "nike vs adidas running shoes" | High |
| Question | "how to choose running shoes" | Low-Medium |

---

## Keyword Expansion Methods

### Method 1: Google Keyword Planner API

```python
from google.ads.googleads.client import GoogleAdsClient

def get_keyword_ideas(client, customer_id, seed_keywords, location_ids=[2840]):
    keyword_plan_idea_service = client.get_service('KeywordPlanIdeaService')
    
    request = client.get_type('GenerateKeywordIdeasRequest')
    request.customer_id = customer_id
    request.language = 'languageConstants/1000'  # English
    request.geo_target_constants.extend([f'geoTargetConstants/{loc}' for loc in location_ids])
    
    # Seed keywords
    request.keyword_seed.keywords.extend(seed_keywords)
    
    # Optional: URL seed
    # request.url_seed.url = 'https://example.com/running-shoes'
    
    response = keyword_plan_idea_service.generate_keyword_ideas(request=request)
    
    keywords = []
    for idea in response:
        keywords.append({
            'keyword': idea.text,
            'avg_monthly_searches': idea.keyword_idea_metrics.avg_monthly_searches,
            'competition': idea.keyword_idea_metrics.competition.name,
            'low_top_of_page_bid_micros': idea.keyword_idea_metrics.low_top_of_page_bid_micros,
            'high_top_of_page_bid_micros': idea.keyword_idea_metrics.high_top_of_page_bid_micros
        })
    
    return keywords
```

### Method 2: Competitor Keyword Analysis

#### Tools for Competitor Research
- **SEMrush** - Paid competitor keyword data
- **Ahrefs** - Organic + paid keyword overlap
- **SpyFu** - Historical ad copy and keywords
- **Google Ads Auction Insights** - Direct competitors in auctions

#### Competitor Analysis Process
1. **Identify top 5-10 competitors** (direct product/service overlap)
2. **Extract their top keywords** (focus on high-volume, high-intent)
3. **Analyze keyword gaps** (keywords they rank for, you don't)
4. **Evaluate ad copy** (messaging, offers, CTAs)
5. **Assess landing pages** (conversion elements, UX)

---

## Search Intent Classification

### Intent Types

| Intent Type | Characteristics | Example Keywords | Funnel Stage |
|-------------|-----------------|------------------|-------------|
| **Informational** | Learning, research | "how to", "what is", "guide" | Top (Awareness) |
| **Navigational** | Finding specific site/brand | "nike website", "amazon login" | Top-Middle |
| **Commercial** | Comparing options | "best", "top", "vs", "review" | Middle (Consideration) |
| **Transactional** | Ready to buy | "buy", "price", "discount", "near me" | Bottom (Decision) |

### Intent Mapping Exercise

**Example: Running Shoes Business**

| Keyword | Intent | Funnel Stage | Bid Strategy |
|---------|--------|--------------|-------------|
| "how to choose running shoes" | Informational | Top | Low bid, content landing page |
| "best running shoes 2026" | Commercial | Middle | Medium bid, comparison page |
| "buy nike running shoes" | Transactional | Bottom | High bid, product page |
| "running shoes near me" | Transactional | Bottom | High bid, store locator |
| "nike vs adidas running shoes" | Commercial | Middle | Medium bid, comparison content |

---

## Keyword Clustering

### Why Cluster Keywords?
- **Improved relevance** - Tighter ad group themes
- **Better Quality Scores** - Keyword-ad-landing page alignment
- **Easier management** - Logical campaign structure
- **Scalability** - Systematic expansion

### Clustering Methods

#### Method 1: Manual Clustering (Small Lists)
1. Export keyword list to spreadsheet
2. Group by product/service category
3. Sub-group by intent or modifier
4. Create ad groups for each cluster (5-20 keywords)

#### Method 2: Automated Clustering (Large Lists)

**Python Example using Semantic Similarity**:
```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import pandas as pd

def cluster_keywords(keywords, n_clusters=10):
    # Vectorize keywords
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(keywords)
    
    # K-means clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = kmeans.fit_predict(X)
    
    # Create DataFrame
    df = pd.DataFrame({'keyword': keywords, 'cluster': clusters})
    
    return df.groupby('cluster')['keyword'].apply(list).to_dict()

# Example usage
keywords = ['running shoes', 'trail running shoes', 'nike running shoes', ...]
clustered = cluster_keywords(keywords, n_clusters=5)
```

### Cluster Validation

**Good Cluster** (Tight Theme):
- "men's running shoes"
- "running shoes for men"
- "best men's running shoes"
- "buy men's running shoes"

**Bad Cluster** (Too Broad):
- "running shoes"
- "basketball shoes"
- "hiking boots"
- "sandals"

---

## Keyword Metrics & Prioritization

### Key Metrics

| Metric | What It Means | How to Use |
|--------|---------------|------------|
| **Search Volume** | Avg monthly searches | Prioritize 100-10,000 range for most businesses |
| **Competition** | Low/Medium/High | Balance volume with competition |
| **Top of Page Bid** | Estimated CPC for top position | Budget planning, ROI forecasting |
| **Keyword Difficulty** | SEO ranking difficulty (0-100) | Correlates with PPC competition |

### Prioritization Framework

#### Tier 1: High Priority (Launch First)
- **Volume**: 500-5,000 monthly searches
- **Intent**: Transactional or Commercial
- **Competition**: Low to Medium
- **Relevance**: Exact product/service match
- **Example**: "buy running shoes online", "running shoes sale"

#### Tier 2: Medium Priority (Launch Week 2-4)
- **Volume**: 100-500 or 5,000-20,000 monthly searches
- **Intent**: Commercial
- **Competition**: Medium to High
- **Relevance**: Close product/service match
- **Example**: "best running shoes", "running shoes for flat feet"

#### Tier 3: Low Priority (Test After 1 Month)
- **Volume**: <100 or >20,000 monthly searches
- **Intent**: Informational or Navigational
- **Competition**: Very High or Very Low
- **Relevance**: Tangential or broad
- **Example**: "how to run faster", "running"

---

## Long-Tail Keyword Strategy

### What Are Long-Tail Keywords?
- **3+ words** in length
- **Lower search volume** (10-500 monthly searches)
- **Higher intent** and specificity
- **Lower competition** and CPC
- **Higher conversion rates** (often 2-3x short-tail)

### Long-Tail Benefits

| Metric | Short-Tail ("shoes") | Long-Tail ("women's trail running shoes size 8") |
|--------|----------------------|--------------------------------------------------|
| Search Volume | 100,000/month | 50/month |
| CPC | $3.50 | $1.20 |
| Conversion Rate | 1.5% | 4.5% |
| Competition | Very High | Low |

### Finding Long-Tail Keywords

1. **Google Autocomplete** - Type seed + modifiers (color, size, brand, location)
2. **"People Also Ask"** - Questions in Google SERP
3. **Related Searches** - Bottom of Google results
4. **Answer The Public** - Question-based keyword tool
5. **Customer Search Data** - Site search logs, support tickets

### Long-Tail Modifiers

| Modifier Type | Examples |
|---------------|----------|
| **Color** | red, blue, black, white |
| **Size** | small, large, 10, XL |
| **Gender** | men's, women's, unisex |
| **Age** | kids, toddler, adult |
| **Material** | leather, mesh, synthetic |
| **Feature** | waterproof, lightweight, cushioned |
| **Brand** | nike, adidas, brooks |
| **Price** | cheap, affordable, premium |
| **Location** | near me, in [city], [state] |
| **Time** | 2026, new, latest |

---

## Negative Keyword Research

### Why Negative Keywords Matter
- **Reduce wasted spend** - Block irrelevant clicks
- **Improve CTR** - Show ads to qualified users only
- **Increase Quality Score** - Better relevance signals
- **Lower CPA** - Higher conversion rate from qualified traffic

### Negative Keyword Sources

#### 1. Search Terms Report
- **Frequency**: Review weekly
- **Process**: Export search terms, filter by 0 conversions + high spend
- **Action**: Add irrelevant terms as negatives

#### 2. Predictive Negatives (Add at Launch)

**Universal Negatives** (Most Businesses):
- free
- cheap
- DIY
- how to
- jobs
- careers
- salary
- resume
- course
- training
- images
- clip art
- download

**E-commerce Negatives**:
- used
- rental
- repair
- parts
- wholesale
- bulk (unless you sell bulk)

**B2B Service Negatives**:
- residential (if B2B only)
- small business (if enterprise only)
- freelance
- intern

#### 3. Competitor Brand Names
- Add competitor brands as negatives if you don't want to bid on them
- Example: If you sell Nike, add "adidas", "reebok" as negatives (or vice versa)

### Negative Keyword Match Types

| Match Type | Syntax | Blocks |
|------------|--------|--------|
| **Broad** | `free` | Any query containing "free" in any order |
| **Phrase** | `"free shipping"` | Queries with "free shipping" in that order |
| **Exact** | `[free shoes]` | Only the exact query "free shoes" |

**Best Practice**: Use **Phrase** or **Broad** match for negatives (more coverage)

---

## Keyword Forecasting

### Google Ads Keyword Planner Forecasting

```python
def forecast_keywords(client, customer_id, keywords, daily_budget_micros=50000000):
    keyword_plan_service = client.get_service('KeywordPlanService')
    
    # Create keyword plan (forecast container)
    keyword_plan = create_keyword_plan(client, customer_id)
    
    # Add campaign to plan
    campaign = add_keyword_plan_campaign(client, customer_id, keyword_plan, daily_budget_micros)
    
    # Add ad group
    ad_group = add_keyword_plan_ad_group(client, customer_id, campaign)
    
    # Add keywords
    add_keyword_plan_keywords(client, customer_id, ad_group, keywords)
    
    # Generate forecast
    response = keyword_plan_service.generate_forecast_metrics(
        keyword_plan=keyword_plan
    )
    
    forecast = {
        'impressions': response.campaign_forecast_metrics.impressions,
        'clicks': response.campaign_forecast_metrics.clicks,
        'cost_micros': response.campaign_forecast_metrics.cost_micros,
        'ctr': response.campaign_forecast_metrics.ctr,
        'average_cpc': response.campaign_forecast_metrics.average_cpc
    }
    
    return forecast
```

### Forecast Interpretation

| Forecast Metric | What It Tells You | Action |
|-----------------|-------------------|--------|
| **Impressions** | Potential reach | If <1,000/day, add more keywords |
| **Clicks** | Expected traffic | Ensure landing page can handle volume |
| **Cost** | Budget requirement | Adjust budget or keyword list |
| **CTR** | Expected click rate | If <2%, improve ad copy |
| **Avg CPC** | Cost per click | Compare to target CPA for ROI |

---

## Seasonal Keyword Planning

### Identifying Seasonal Trends

**Google Trends Analysis**:
1. Enter seed keyword
2. Set date range to 5 years
3. Identify seasonal peaks/valleys
4. Plan campaigns 4-6 weeks before peak

### Seasonal Keyword Examples

| Industry | Peak Season | Seasonal Keywords |
|----------|-------------|-------------------|
| **Retail** | Nov-Dec | "black friday", "christmas gifts", "holiday sale" |
| **Tax Services** | Jan-Apr | "tax preparation", "file taxes", "tax refund" |
| **HVAC** | Jun-Aug (cooling), Dec-Feb (heating) | "air conditioning repair", "furnace installation" |
| **Fitness** | Jan (New Year) | "gym membership", "weight loss", "fitness goals" |
| **Education** | Aug-Sep | "back to school", "school supplies", "tutoring" |

### Seasonal Campaign Strategy

1. **Pre-Season (4-6 weeks before)**
   - Launch awareness campaigns
   - Lower bids, broader keywords
   - Build remarketing lists

2. **Peak Season**
   - Increase bids 20-50%
   - Add seasonal modifiers to keywords
   - Tighten to high-intent keywords
   - Extend ad schedules (24/7)

3. **Post-Season**
   - Reduce bids gradually
   - Shift to clearance/next-season messaging
   - Analyze performance for next year

---

## Keyword Organization Best Practices

### Campaign Structure by Keyword Type

```
Account: Running Shoe Store
├── Campaign: Brand - Exact Match
│   ├── Ad Group: [Brand Name]
│   │   └── Keywords: [nike running shoes], [nike runners]
│   └── Ad Group: [Brand + Product]
│       └── Keywords: [nike air zoom], [nike pegasus]
│
├── Campaign: Generic - High Intent
│   ├── Ad Group: Buy Intent
│   │   └── Keywords: "buy running shoes", "running shoes for sale"
│   └── Ad Group: Near Me
│       └── Keywords: "running shoes near me", "running store near me"
│
├── Campaign: Generic - Broad Discovery
│   └── Ad Group: General Running Shoes
│       └── Keywords: running shoes, trail running shoes (Broad Match)
│
└── Campaign: Competitor
    ├── Ad Group: Competitor A
    │   └── Keywords: "adidas running shoes", "adidas ultraboost"
    └── Ad Group: Competitor B
        └── Keywords: "brooks running shoes", "brooks ghost"
```

### Naming Conventions

**Campaign Names**:
- `[Channel] - [Type] - [Match Type] - [Geo]`
- Example: `Search - Brand - Exact - US`

**Ad Group Names**:
- `[Product/Category] - [Modifier]`
- Example: `Running Shoes - Men's`

**Keyword Labels** (for tracking):
- `Tier-1-High-Intent`
- `Long-Tail`
- `Seasonal-Q4`
- `Competitor`

---

## Keyword Research Tools Comparison

| Tool | Best For | Cost | Key Features |
|------|----------|------|-------------|
| **Google Keyword Planner** | Google Ads forecasting | Free (requires Google Ads account) | Search volume, CPC estimates, forecasts |
| **SEMrush** | Competitor analysis | $119.95/month | Competitor keywords, ad copy, position tracking |
| **Ahrefs** | SEO + PPC overlap | $99/month | Keyword difficulty, SERP analysis, content gaps |
| **SpyFu** | Historical competitor data | $39/month | Competitor ad history, keyword overlap |
| **Ubersuggest** | Budget-friendly alternative | $29/month | Keyword suggestions, content ideas |
| **Answer The Public** | Question-based keywords | Free (limited) | Visual keyword maps, questions |
| **Google Trends** | Seasonal trends | Free | Trend analysis, geographic interest |

---

## Keyword Research Checklist

### Initial Research
- [ ] Brainstorm 20-50 seed keywords
- [ ] Expand using Keyword Planner (target 200-500 keywords)
- [ ] Classify keywords by intent (Informational, Commercial, Transactional)
- [ ] Cluster keywords into ad groups (5-20 keywords per group)
- [ ] Prioritize into Tier 1, 2, 3 based on volume, intent, competition
- [ ] Research 50-100 negative keywords
- [ ] Analyze top 5 competitors' keywords
- [ ] Identify seasonal trends (if applicable)

### Ongoing Optimization (Monthly)
- [ ] Review search terms report
- [ ] Add high-performing search terms as keywords
- [ ] Add irrelevant search terms as negatives
- [ ] Expand long-tail keyword list
- [ ] Update seasonal keywords
- [ ] Re-forecast budget needs
- [ ] Analyze keyword Quality Scores
- [ ] Test new keyword clusters