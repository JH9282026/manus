# Quality Score Deep Dive

Comprehensive guide to understanding, diagnosing, and improving Google Ads Quality Score for better ad performance and lower costs.

---

## What Is Quality Score?

Quality Score is Google's rating (1-10 scale) of the quality and relevance of your keywords, ads, and landing pages. It directly impacts:

1. **Ad Rank** - Determines ad position
2. **Cost Per Click (CPC)** - Higher QS = lower CPC
3. **Impression Share** - Higher QS = more ad impressions
4. **Eligibility** - Low QS may prevent ads from showing

### Quality Score Formula

**Ad Rank = Max CPC Bid × Quality Score**

Example:
- Advertiser A: $2 bid × QS 8 = Ad Rank 16
- Advertiser B: $3 bid × QS 5 = Ad Rank 15
- **Result**: Advertiser A wins top position despite lower bid

---

## Quality Score Components

### 1. Expected Click-Through Rate (CTR) - 40% Weight

**What it measures**: Likelihood that your ad will be clicked when shown

**Ratings**:
- **Above Average** - Ad is expected to perform better than other ads for the same keyword
- **Average** - Ad is expected to perform similarly to other ads
- **Below Average** - Ad is expected to perform worse than other ads

**Factors influencing Expected CTR**:
- Historical CTR of the keyword in your account
- Ad copy relevance and appeal
- Ad extensions usage
- Device performance (mobile vs desktop)
- Geographic performance

### 2. Ad Relevance - 30% Weight

**What it measures**: How closely your ad matches the intent behind a user's search

**Ratings**:
- **Above Average** - Ad is highly relevant to the keyword
- **Average** - Ad is moderately relevant
- **Below Average** - Ad may be too general or unrelated

**Factors influencing Ad Relevance**:
- Keyword presence in ad headlines/descriptions
- Ad group theme tightness (5-20 related keywords)
- Message match between keyword and ad copy
- Specificity of ad copy to search query

### 3. Landing Page Experience - 30% Weight

**What it measures**: How relevant and useful your landing page is to users who click your ad

**Ratings**:
- **Above Average** - Landing page provides excellent user experience
- **Average** - Landing page is acceptable
- **Below Average** - Landing page needs improvement

**Factors influencing Landing Page Experience**:
- **Relevance**: Content matches ad message and keyword
- **Transparency**: Clear business information, privacy policy, contact details
- **Navigation**: Easy to find information, clear site structure
- **Load Time**: Page loads in <3 seconds (mobile and desktop)
- **Mobile-Friendliness**: Responsive design, readable text, tap targets
- **Original Content**: Unique, valuable content (not thin/duplicate)
- **Trustworthiness**: Secure (HTTPS), professional design, no intrusive elements

---

## Quality Score Benchmarks

| Quality Score | Performance Level | Typical CPC Impact | Action Required |
|---------------|-------------------|--------------------|-----------------|
| **10** | Exceptional | -50% vs QS 5 | Maintain, use as template |
| **8-9** | Excellent | -30% to -40% vs QS 5 | Minor optimizations |
| **7** | Good | -15% to -25% vs QS 5 | Incremental improvements |
| **5-6** | Average | Baseline | Moderate optimization needed |
| **3-4** | Below Average | +25% to +50% vs QS 5 | Significant optimization required |
| **1-2** | Poor | +100%+ vs QS 5 | Urgent action, consider pausing |

### Industry Benchmarks

| Industry | Average QS | Top Performers QS |
|----------|------------|-------------------|
| E-commerce | 5.5 | 8+ |
| B2B Services | 6.0 | 8+ |
| Legal | 4.5 | 7+ |
| Healthcare | 5.0 | 7+ |
| Finance | 5.5 | 8+ |
| Education | 6.5 | 9+ |

---

## Diagnosing Quality Score Issues

### Step 1: Identify Low QS Keywords

**Google Ads UI**:
1. Navigate to Keywords tab
2. Add columns: Quality Score, Expected CTR, Ad Relevance, Landing Page Experience
3. Filter: Quality Score ≤ 5
4. Sort by Impressions (descending) to prioritize high-volume keywords

**API Query**:
```sql
SELECT
  ad_group.name,
  ad_group_criterion.keyword.text,
  ad_group_criterion.quality_info.quality_score,
  ad_group_criterion.quality_info.creative_quality_score,
  ad_group_criterion.quality_info.post_click_quality_score,
  ad_group_criterion.quality_info.search_predicted_ctr,
  metrics.impressions,
  metrics.clicks,
  metrics.ctr,
  metrics.average_cpc
FROM keyword_view
WHERE ad_group_criterion.quality_info.quality_score <= 5
  AND metrics.impressions > 100
  AND segments.date DURING LAST_30_DAYS
ORDER BY metrics.impressions DESC
```

### Step 2: Analyze Component Ratings

**Decision Tree**:

```
Low Quality Score (≤5)
├── Expected CTR: Below Average
│   ├── Action: Improve ad copy, add extensions, test new headlines
│   └── Target: Increase CTR by 20-50%
│
├── Ad Relevance: Below Average
│   ├── Action: Tighten ad groups, add keyword to headlines, create SKAGs
│   └── Target: Keyword in at least 1 headline
│
└── Landing Page Experience: Below Average
    ├── Action: Improve page speed, relevance, mobile UX, add content
    └── Target: <3s load time, keyword on page 3-5 times
```

---

## Improving Expected CTR

### Tactic 1: Optimize Ad Copy

**High-CTR Ad Copy Elements**:
1. **Numbers** - "Save 40%", "5-Star Rated", "24/7 Support"
2. **Emotional Triggers** - "Don't Miss Out", "Limited Time", "Exclusive"
3. **Questions** - "Looking for Running Shoes?", "Need Fast Shipping?"
4. **Power Words** - "Free", "Guaranteed", "Proven", "Easy"
5. **Specificity** - "2-Day Shipping" vs "Fast Shipping"

**Before (Low CTR)**:
- Headline: "Running Shoes"
- Description: "We sell running shoes. Visit our website."
- **CTR**: 1.2%

**After (High CTR)**:
- Headline: "Premium Running Shoes - Save 40% Today"
- Description: "Shop 500+ styles. Free shipping & returns. Expert fitting available. Order now!"
- **CTR**: 3.8% (+217%)

### Tactic 2: Add All Relevant Ad Extensions

**CTR Lift by Extension Type**:

| Extension | Avg CTR Lift | Setup Priority |
|-----------|--------------|----------------|
| Sitelink | +10-20% | High |
| Callout | +5-10% | High |
| Structured Snippet | +5-10% | Medium |
| Call | +5-15% | High (mobile) |
| Location | +10% | High (local) |
| Price | +5-10% | Medium |
| Promotion | +10-15% | High (during sales) |
| Image | +5-10% | Medium |

### Tactic 3: Improve Mobile Experience

**Mobile-Specific Optimizations**:
- **Shorter headlines** (15-20 characters) for full display
- **Click-to-call extensions** for immediate action
- **Location extensions** with directions
- **Mobile-preferred ads** (if available in your account)
- **Fast-loading landing pages** (<2s on mobile)

### Tactic 4: Test Ad Variations

**A/B Testing Framework**:
1. Create 2-3 RSAs per ad group
2. Test different:
   - Headline angles (features vs benefits vs offers)
   - CTA urgency ("Shop Now" vs "Order Today" vs "Get Yours")
   - Value propositions (price vs quality vs service)
3. Let run for 2-4 weeks or 1,000+ impressions
4. Pause low-performing ads, create new variants

---

## Improving Ad Relevance

### Tactic 1: Tighten Ad Groups (Single Keyword Ad Groups - SKAGs)

**Before (Low Relevance)**:
```
Ad Group: Shoes
Keywords:
- running shoes
- basketball shoes
- hiking boots
- sandals

Ad Headline: "Shop Shoes Online"
```
**Quality Score**: 3-4 (too broad)

**After (High Relevance)**:
```
Ad Group: Running Shoes - Men's
Keywords:
- men's running shoes
- running shoes for men
- men's trail running shoes

Ad Headline: "Men's Running Shoes - Free Shipping"
```
**Quality Score**: 7-8 (tight theme)

### Tactic 2: Include Keyword in Headlines

**Keyword Insertion Best Practices**:
- **Headline 1**: Include exact keyword or close variant
- **Headline 2-3**: Include keyword modifiers or synonyms
- **Description**: Include keyword 1-2 times naturally

**Example**:
- **Keyword**: "waterproof running shoes"
- **Headline 1**: "Waterproof Running Shoes"
- **Headline 2**: "Stay Dry - Shop Waterproof Runners"
- **Description**: "Find the best waterproof running shoes for all conditions. Free shipping."

### Tactic 3: Use Dynamic Keyword Insertion (DKI) Carefully

**When DKI Works Well**:
```
Ad Group: Nike Running Shoes (Tight Theme)
Keywords:
- nike running shoes
- nike runners
- nike athletic shoes

Headline: "{KeyWord:Nike Shoes} - Official Retailer"
Result: "Nike Running Shoes - Official Retailer" (relevant)
```

**When DKI Fails**:
```
Ad Group: Running Shoes (Broad Theme)
Keywords:
- running shoes
- best running shoes for flat feet
- cheap running shoes under $50

Headline: "{KeyWord:Running Shoes} On Sale"
Result: "Best Running Shoes For Flat... On Sale" (truncated, awkward)
```

### Tactic 4: Create Dedicated Ad Groups for High-Value Keywords

**High-Value Keyword Criteria**:
- High conversion rate (>5%)
- High conversion value (>$100)
- High search volume (>1,000 monthly searches)
- Strategic importance (brand terms, core products)

**Action**: Create Single Keyword Ad Group (SKAG) with:
- 1 keyword (all match types: Exact, Phrase, Broad)
- 2-3 highly relevant RSAs
- Dedicated landing page
- Custom ad extensions

---

## Improving Landing Page Experience

### Tactic 1: Optimize Page Load Speed

**Target**: <3 seconds on mobile, <2 seconds on desktop

**Speed Optimization Checklist**:
- [ ] **Compress images** - Use WebP format, max 100KB per image
- [ ] **Minify CSS/JS** - Remove unnecessary code
- [ ] **Enable browser caching** - Cache static resources
- [ ] **Use CDN** - Serve content from geographically closer servers
- [ ] **Reduce redirects** - Minimize redirect chains
- [ ] **Lazy load images** - Load images as user scrolls
- [ ] **Remove render-blocking resources** - Defer non-critical JS/CSS

**Testing Tools**:
- Google PageSpeed Insights
- GTmetrix
- WebPageTest
- Chrome DevTools (Lighthouse)

**Speed Impact on Quality Score**:

| Load Time | Landing Page Experience Rating | QS Impact |
|-----------|--------------------------------|-----------|
| <2s | Above Average | +1 to +2 QS |
| 2-4s | Average | Neutral |
| 4-6s | Below Average | -1 to -2 QS |
| >6s | Below Average | -2 to -3 QS |

### Tactic 2: Improve Message Match

**Message Match Principle**: Landing page headline should mirror ad headline

**Example**:
- **Ad Headline**: "Waterproof Running Shoes - Free Shipping"
- **Landing Page H1**: "Waterproof Running Shoes" ✓
- **Landing Page H1**: "Running Shoes Collection" ✗ (mismatch)

**Message Match Checklist**:
- [ ] Keyword appears in page title (H1)
- [ ] Keyword appears in first paragraph
- [ ] Keyword appears 3-5 times on page (natural density)
- [ ] Ad offer (e.g., "Free Shipping") is visible above fold
- [ ] Visual elements (images) match ad promise

### Tactic 3: Enhance Mobile Experience

**Mobile Landing Page Best Practices**:

| Element | Requirement | Why It Matters |
|---------|-------------|----------------|
| **Font Size** | ≥16px | Readable without zooming |
| **Tap Targets** | ≥48px × 48px | Easy to tap on mobile |
| **Viewport** | Responsive meta tag | Proper scaling on all devices |
| **Interstitials** | No pop-ups on entry | Google penalizes intrusive interstitials |
| **Horizontal Scroll** | None | Poor UX, Google penalizes |
| **CTA Button** | Above fold, prominent | Easy conversion path |

**Mobile Testing Tools**:
- Google Mobile-Friendly Test
- Chrome DevTools (Device Mode)
- BrowserStack (real device testing)

### Tactic 4: Add Trust Signals

**Trust Elements to Include**:

| Trust Signal | Placement | Impact |
|--------------|-----------|--------|
| **SSL Certificate (HTTPS)** | Entire site | Required for QS |
| **Privacy Policy Link** | Footer | Required |
| **Contact Information** | Header/Footer | High |
| **Customer Reviews** | Product pages | High |
| **Security Badges** | Checkout | Medium |
| **Money-Back Guarantee** | Above fold | Medium |
| **Industry Certifications** | Footer | Medium |
| **Social Proof** | Throughout | Medium |

### Tactic 5: Improve Content Quality

**Content Quality Checklist**:
- [ ] **Unique content** - Not duplicated from other pages/sites
- [ ] **Substantial content** - At least 300-500 words
- [ ] **Relevant content** - Directly addresses keyword intent
- [ ] **Scannable** - Use headings, bullet points, short paragraphs
- [ ] **Actionable** - Clear next steps, prominent CTA
- [ ] **Up-to-date** - Current information, recent dates
- [ ] **No thin content** - Avoid pages with only images or minimal text

**Content Structure Example**:
```
H1: Waterproof Running Shoes (keyword)

Intro Paragraph: (100 words, includes keyword 2x)
"Looking for waterproof running shoes? Our collection features..."

H2: Why Choose Waterproof Running Shoes?
- Bullet points (benefits)

H2: Top Waterproof Running Shoe Brands
- Product grid with images

H2: How to Choose the Right Waterproof Running Shoes
- Buying guide (200 words)

CTA: "Shop Waterproof Running Shoes Now" (prominent button)

H2: Customer Reviews
- 5-10 reviews with ratings

FAQ Section:
- 5-10 common questions about waterproof running shoes
```

---

## Quality Score Optimization Workflow

### Week 1: Audit & Prioritize
1. Export all keywords with QS ≤ 5 and >100 impressions
2. Categorize by component issue (CTR, Relevance, Landing Page)
3. Prioritize by impression volume (fix high-volume first)
4. Set QS improvement targets (+2 points minimum)

### Week 2-3: Implement Fixes

**For Expected CTR Issues**:
- Rewrite ad copy (add numbers, emotional triggers, CTAs)
- Add all relevant ad extensions
- Create 2-3 new RSA variants

**For Ad Relevance Issues**:
- Tighten ad groups (split broad groups into themed groups)
- Add keyword to headlines (at least 1 headline)
- Create SKAGs for top 10 keywords

**For Landing Page Issues**:
- Optimize page speed (target <3s)
- Add keyword to H1 and first paragraph
- Improve mobile UX (responsive design, larger tap targets)
- Add trust signals (reviews, guarantees, security badges)

### Week 4: Monitor & Iterate
1. Check QS changes (allow 1-2 weeks for Google to update)
2. Measure CTR, conversion rate, CPA changes
3. Identify remaining low QS keywords
4. Repeat optimization cycle

---

## Quality Score Myths & Facts

### Myth 1: "Quality Score is calculated in real-time"
**Fact**: QS is updated periodically (every few days to weeks), not in real-time. Changes may take 1-2 weeks to reflect.

### Myth 2: "Pausing low QS keywords improves account QS"
**Fact**: Pausing keywords doesn't improve account-level QS. Historical performance remains. Better to fix or delete permanently.

### Myth 3: "Display Network performance affects Search QS"
**Fact**: Search and Display QS are calculated separately. Display performance doesn't impact Search QS.

### Myth 4: "Higher bids improve Quality Score"
**Fact**: Bids don't directly affect QS. However, higher bids → better ad positions → potentially higher CTR → improved QS over time.

### Myth 5: "Quality Score is the same across all devices"
**Fact**: QS can vary by device (mobile vs desktop). Optimize for both separately.

---

## Quality Score Impact on Costs

### CPC Reduction by QS Improvement

| QS Change | Estimated CPC Reduction | Example: $5 CPC → |
|-----------|-------------------------|-------------------|
| 3 → 5 | -20% | $4.00 |
| 5 → 7 | -20% | $4.00 |
| 5 → 8 | -35% | $3.25 |
| 5 → 10 | -50% | $2.50 |
| 7 → 10 | -30% | $3.50 |

### ROI Impact Example

**Scenario**: E-commerce campaign, 10,000 clicks/month

**Before Optimization**:
- Average QS: 5
- Average CPC: $2.50
- Monthly Cost: $25,000
- Conversions: 200 (2% CVR)
- CPA: $125

**After Optimization** (QS 5 → 8):
- Average QS: 8
- Average CPC: $1.63 (-35%)
- Monthly Cost: $16,300 (-35%)
- Conversions: 250 (2.5% CVR, improved relevance)
- CPA: $65.20 (-48%)

**Result**: $8,700/month savings + 25% more conversions

---

## Advanced Quality Score Strategies

### Strategy 1: QS-Based Bid Adjustments

**Automated Rule**:
- IF QS ≥ 8, THEN increase bid by 20%
- IF QS ≤ 4, THEN decrease bid by 30% or pause

**Rationale**: Invest more in high-QS keywords (lower CPC, better ROI), reduce spend on low-QS keywords.

### Strategy 2: Historical QS Tracking

**Why Track Historical QS**:
- Google Ads UI only shows current QS
- Historical tracking reveals trends and optimization impact

**How to Track**:
1. Weekly export of keyword QS data
2. Store in database or spreadsheet
3. Visualize trends over time
4. Correlate QS changes with optimization actions

**API Query for Historical Tracking**:
```sql
SELECT
  segments.date,
  ad_group_criterion.keyword.text,
  ad_group_criterion.quality_info.quality_score,
  metrics.impressions,
  metrics.ctr
FROM keyword_view
WHERE segments.date DURING LAST_90_DAYS
ORDER BY segments.date DESC
```

### Strategy 3: Competitor QS Benchmarking

**Auction Insights Analysis**:
1. Run Auction Insights report for top keywords
2. Identify competitors with higher impression share
3. Analyze their ad copy, extensions, landing pages
4. Infer their QS advantages (better CTR, relevance, LP)
5. Implement similar tactics

**Competitive QS Indicators**:
- **Higher impression share at lower estimated bids** → Likely higher QS
- **Top of page rate** → Strong QS and/or high bids
- **Outranking share** → Combination of QS and bid strategy

---

## Quality Score Checklist

### Monthly QS Audit
- [ ] Export all keywords with QS data
- [ ] Identify keywords with QS ≤ 5 and >100 impressions
- [ ] Categorize by component issue (CTR, Relevance, LP)
- [ ] Prioritize by impression volume
- [ ] Set improvement targets (+2 QS minimum)

### Expected CTR Optimization
- [ ] Rewrite low-CTR ad copy
- [ ] Add all relevant ad extensions
- [ ] Test 2-3 new RSA variants per ad group
- [ ] Optimize for mobile (shorter headlines, click-to-call)

### Ad Relevance Optimization
- [ ] Tighten ad groups (5-20 related keywords)
- [ ] Include keyword in at least 1 headline
- [ ] Create SKAGs for top 10 keywords
- [ ] Use DKI for tightly themed ad groups

### Landing Page Optimization
- [ ] Test page speed (<3s target)
- [ ] Add keyword to H1 and first paragraph
- [ ] Ensure mobile-friendly (responsive, no horizontal scroll)
- [ ] Add trust signals (reviews, guarantees, HTTPS)
- [ ] Improve content quality (300+ words, unique, relevant)
- [ ] Ensure message match (ad headline = page H1)

### Monitoring
- [ ] Track QS changes weekly
- [ ] Measure CTR, CVR, CPA impact
- [ ] Identify remaining low QS keywords
- [ ] Repeat optimization cycle