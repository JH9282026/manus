# Search Term Mining & Optimization

Advanced strategies for analyzing search term reports to discover new keywords, add negatives, and optimize match type distribution.

---

## What is Search Term Mining?

**Search Term Report** shows the actual queries users typed that triggered your ads, regardless of your keyword match type.

**Why It Matters**:
- Discover high-performing keywords you're not bidding on
- Identify irrelevant queries wasting budget (add as negatives)
- Optimize match type distribution
- Improve Quality Score through better relevance

---

## Accessing Search Term Data

### Google Ads UI
1. Navigate to **Keywords** tab
2. Click **Search Terms** button
3. Set date range (last 30 days recommended)
4. Add columns: Impressions, Clicks, CTR, Conversions, Cost, Conv. Rate

### API Query
```sql
SELECT
  search_term_view.search_term,
  search_term_view.status,
  ad_group.name,
  campaign.name,
  metrics.impressions,
  metrics.clicks,
  metrics.ctr,
  metrics.cost_micros,
  metrics.conversions,
  metrics.cost_per_conversion
FROM search_term_view
WHERE segments.date DURING LAST_30_DAYS
  AND metrics.impressions > 0
ORDER BY metrics.cost_micros DESC
```

---

## Search Term Analysis Framework

### Step 1: Export & Categorize

**Export Criteria**:
- Date range: Last 30 days
- Minimum impressions: 10+
- Sort by: Cost (descending)

**Categories**:
1. **Exact Match** - Search term = keyword (no action needed)
2. **Close Variant** - Similar to keyword (monitor performance)
3. **Relevant Expansion** - Related, good performance (add as keyword)
4. **Irrelevant** - Not related (add as negative)
5. **Low Intent** - Related but wrong intent (add as negative)

### Step 2: Identify New Keyword Opportunities

**Criteria for Adding as Keyword**:
- **Conversions**: \u22651 conversion OR
- **CTR**: >3% (above average) OR
- **Impressions**: >100 (high volume)
- **Relevance**: Directly related to products/services

**Example**:
```
Keyword: \"running shoes\" (Broad Match)
Search Term: \"best trail running shoes for women\"
Performance: 150 impressions, 8 clicks (5.3% CTR), 1 conversion
Action: Add \"trail running shoes for women\" as Phrase Match keyword
```

### Step 3: Identify Negative Keywords

**Criteria for Adding as Negative**:
- **Zero conversions** AND high spend (>$50) OR
- **Clearly irrelevant** (e.g., \"free\", \"DIY\", \"jobs\") OR
- **Wrong intent** (e.g., \"how to make\" for e-commerce)

**Example**:
```
Keyword: \"running shoes\" (Broad Match)
Search Term: \"how to clean running shoes\"
Performance: 80 impressions, 12 clicks, 0 conversions, $24 cost
Action: Add \"how to clean\" as Phrase Match negative
```

---

## Search Term Mining Workflow

### Weekly Workflow (30 minutes)

#### Week 1: High-Spend Review
1. Export search terms, sort by Cost (descending)
2. Review top 50 search terms by spend
3. Add 5-10 new keywords (high-performing terms)
4. Add 10-20 negative keywords (irrelevant terms)

#### Week 2: Conversion Review
1. Export search terms with conversions
2. Identify converting terms not in keyword list
3. Add as Exact or Phrase Match keywords
4. Increase bids on high-ROAS terms

#### Week 3: Volume Review
1. Export search terms, sort by Impressions (descending)
2. Review high-volume, low-CTR terms
3. Add irrelevant high-volume terms as negatives
4. Improve ad copy for relevant high-volume terms

#### Week 4: Match Type Optimization
1. Analyze match type distribution
2. Identify Broad Match keywords triggering too many irrelevant terms
3. Shift to Phrase or Exact Match
4. Add negatives to tighten Broad Match targeting

---

## Match Type Optimization

### Match Type Performance Analysis

| Match Type | Avg CTR | Avg CVR | Avg CPA | Volume | Control |
|------------|---------|---------|---------|--------|---------|
| **Exact** | 4.5% | 3.5% | $45 | Low | Highest |
| **Phrase** | 3.2% | 2.8% | $55 | Medium | Medium |
| **Broad** | 1.8% | 1.5% | $75 | High | Lowest |

### When to Use Each Match Type

**Exact Match** `[keyword]`:
- **Use for**: High-intent, proven keywords
- **Pros**: Maximum control, highest relevance
- **Cons**: Limited reach, may miss variations
- **Example**: `[buy nike running shoes]`

**Phrase Match** `"keyword"`:
- **Use for**: Moderate reach with control
- **Pros**: Captures variations, good balance
- **Cons**: Some irrelevant matches possible
- **Example**: `"running shoes for women"`

**Broad Match** `keyword`:
- **Use for**: Discovery, maximum reach
- **Pros**: Finds new keywords, high volume
- **Cons**: Many irrelevant matches, requires heavy negative list
- **Example**: `running shoes`

### Match Type Migration Strategy

**Phase 1: Broad Match Discovery** (Weeks 1-4)
- Launch with Broad Match keywords
- Aggressive negative keyword management
- Identify high-performing search terms

**Phase 2: Phrase Match Refinement** (Weeks 5-8)
- Add top performers as Phrase Match
- Continue Broad Match for discovery
- Build comprehensive negative list

**Phase 3: Exact Match Optimization** (Weeks 9+)
- Add proven converters as Exact Match
- Increase bids on Exact Match (lower CPA)
- Maintain Phrase/Broad for ongoing discovery

---

## Negative Keyword Strategy

### Negative Keyword Types

#### 1. Universal Negatives (Apply to All Campaigns)
- free
- cheap
- DIY
- how to
- jobs
- careers
- salary
- course
- training
- download
- torrent
- cracked

#### 2. Industry-Specific Negatives

**E-commerce**:
- used
- rental
- repair
- parts
- wholesale
- bulk (unless you sell bulk)

**B2B Services**:
- residential (if B2B only)
- small business (if enterprise only)
- freelance
- intern
- volunteer

**Local Services**:
- online (if local only)
- virtual (if in-person only)
- remote (if on-site only)

#### 3. Competitor Negatives
- Add competitor brand names if you don't want to bid on them
- Example: Selling Nike? Add \"adidas\", \"reebok\" as negatives

### Negative Keyword Match Types

| Match Type | Syntax | Blocks | Example |
|------------|--------|--------|---------|
| **Broad** | `free` | Any query with \"free\" | \"free running shoes\", \"running shoes free shipping\" |
| **Phrase** | `\"free shipping\"` | Queries with \"free shipping\" in order | \"free shipping running shoes\" |
| **Exact** | `[free shoes]` | Only \"free shoes\" | \"free shoes\" only |

**Best Practice**: Use **Phrase** or **Broad** match for negatives (broader coverage)

---

## Search Term Segmentation

### By Intent

| Intent | Search Term Examples | Action |
|--------|---------------------|--------|
| **Transactional** | \"buy\", \"order\", \"purchase\", \"near me\" | High bids, product pages |
| **Commercial** | \"best\", \"top\", \"review\", \"vs\" | Medium bids, comparison pages |
| **Informational** | \"how to\", \"what is\", \"guide\" | Low bids or negative, content pages |
| **Navigational** | Brand names, \"login\", \"website\" | Brand campaigns only |

### By Funnel Stage

**Top of Funnel (Awareness)**:
- Search terms: \"what is\", \"how to\", \"guide\"
- Action: Low bids, content landing pages, or add as negatives

**Middle of Funnel (Consideration)**:
- Search terms: \"best\", \"top\", \"review\", \"comparison\"
- Action: Medium bids, comparison pages, remarketing

**Bottom of Funnel (Decision)**:
- Search terms: \"buy\", \"price\", \"discount\", \"near me\"
- Action: High bids, product pages, aggressive remarketing

---

## Advanced Search Term Analysis

### 1. Search Term Clustering

**Purpose**: Group similar search terms to identify themes

**Method**:
1. Export search terms
2. Use text clustering (Python, Excel)
3. Identify common themes (product types, features, brands)
4. Create dedicated ad groups for high-volume themes

**Example**:
```
Cluster 1: \"waterproof running shoes\"
- waterproof running shoes
- waterproof trail running shoes
- water resistant running shoes
- running shoes for rain

Action: Create \"Waterproof Running Shoes\" ad group
```

### 2. Search Term Performance Tiers

**Tier 1: High Performers** (Add as Exact Match)
- Conversion rate >5%
- Cost per conversion <target CPA
- Volume >10 conversions/month

**Tier 2: Moderate Performers** (Add as Phrase Match)
- Conversion rate 2-5%
- Cost per conversion near target CPA
- Volume 1-10 conversions/month

**Tier 3: Low Performers** (Monitor or Negative)
- Conversion rate <2%
- Cost per conversion >target CPA
- High spend, low conversions

### 3. Search Term Cannibalization

**Issue**: Multiple keywords triggering the same search term

**Example**:
```
Search Term: \"nike running shoes\"
Triggered by:
- Keyword 1: \"running shoes\" (Broad Match)
- Keyword 2: \"nike shoes\" (Phrase Match)
- Keyword 3: [nike running shoes] (Exact Match)

Problem: Competing against yourself, unclear performance attribution
```

**Solution**:
1. Add \"nike\" as negative to \"running shoes\" keyword
2. Ensure Exact Match keyword has highest bid
3. Use Phrase/Broad for discovery only

---

## Search Term Mining Tools

### Built-in Google Ads Tools
- **Search Terms Report** - Primary tool
- **Keyword Planner** - Expansion ideas
- **Auction Insights** - Competitor analysis

### Third-Party Tools
- **SEMrush** - Competitor search terms
- **SpyFu** - Historical search term data
- **Optmyzr** - Automated search term mining
- **WordStream** - Search term analysis

### Custom Scripts
```javascript
// Google Ads Script: Auto-add high-performing search terms as keywords
function main() {
  var searchTerms = AdsApp.searchTerms()
    .withCondition('Conversions > 2')
    .withCondition('ConversionRate > 0.05')
    .withCondition('Impressions > 100')
    .forDateRange('LAST_30_DAYS')
    .get();
  
  while (searchTerms.hasNext()) {
    var searchTerm = searchTerms.next();
    var adGroup = searchTerm.getAdGroup();
    
    // Add as Phrase Match keyword
    adGroup.newKeywordBuilder()
      .withText('\"' + searchTerm.getText() + '\"')
      .build();
    
    Logger.log('Added keyword: ' + searchTerm.getText());
  }
}
```

---

## Search Term Mining Checklist

### Weekly Tasks
- [ ] Export search terms report (last 7 days)
- [ ] Review top 20 search terms by spend
- [ ] Add 3-5 new keywords (high performers)
- [ ] Add 5-10 negative keywords (irrelevant terms)
- [ ] Check for search term cannibalization

### Monthly Tasks
- [ ] Comprehensive search term review (last 30 days)
- [ ] Analyze match type performance
- [ ] Update negative keyword lists
- [ ] Identify new ad group themes
- [ ] Review search term intent distribution
- [ ] Optimize bids based on search term performance

### Quarterly Tasks
- [ ] Full account search term audit
- [ ] Rebuild negative keyword lists
- [ ] Analyze seasonal search term trends
- [ ] Update match type strategy
- [ ] Review competitor search terms (if available)
