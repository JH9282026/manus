# Display Audience Targeting Strategies

Advanced audience targeting techniques for Google Display Network campaigns.

---

## Audience Targeting Overview

### Targeting vs. Observation Mode

| Mode | Behavior | Use Case |
|------|----------|----------|
| **Targeting** | Ads only show to selected audiences | Narrow reach, high relevance |
| **Observation** | Ads show to all, data collected by audience | Broad reach, performance insights |

**Best Practice**: Start with Observation mode for 2-4 weeks, then switch to Targeting for top-performing audiences.

---

## Affinity Audiences

### What Are Affinity Audiences?

Users with strong, long-term interests in specific topics.

### Top Affinity Categories

| Category | Subcategories | Typical Use |
|----------|---------------|-------------|
| **Sports & Fitness** | Running, yoga, gym, cycling | Athletic apparel, equipment |
| **Food & Dining** | Cooking, fine dining, fast food | Food products, kitchen tools |
| **Technology** | Gadgets, software, gaming | Electronics, apps, services |
| **Travel** | Luxury travel, budget travel, adventure | Travel services, luggage |
| **Home & Garden** | DIY, interior design, gardening | Home improvement, furniture |

### Custom Affinity Audiences

**Create based on**:
- **Interests**: Specific topics (e.g., "marathon training")
- **URLs**: Websites users visit (e.g., "runnersworld.com")
- **Apps**: Mobile apps users use (e.g., "Strava")

**Example**:
```
Audience: "Serious Runners"
Interests: marathon training, trail running, running nutrition
URLs: runnersworld.com, nike.com/running, strava.com
Apps: Strava, Nike Run Club, Runkeeper
```

---

## In-Market Audiences

### What Are In-Market Audiences?

Users actively researching or comparing products/services, showing purchase intent.

### High-Intent Categories

| Category | Purchase Intent | Conversion Potential |
|----------|-----------------|---------------------|
| **Apparel & Accessories** | Shopping for clothing | High |
| **Autos & Vehicles** | Researching car purchase | Very High |
| **Business Services** | Comparing B2B solutions | High |
| **Consumer Electronics** | Shopping for gadgets | High |
| **Home & Garden** | Planning home improvements | High |

### Performance Benchmarks

| Audience Type | Avg CTR | Avg CVR | Avg CPA vs. Affinity |
|---------------|---------|---------|---------------------|
| Affinity | 0.4-0.6% | 0.3-0.5% | Baseline |
| In-Market | 0.6-1.0% | 0.8-1.5% | -30% to -50% |

---

## Custom Intent Audiences

### How to Create

1. **Navigate**: Tools & Settings > Audience Manager > Custom Audiences
2. **Select**: Custom Intent
3. **Add**:
   - **Keywords**: Terms users search for
   - **URLs**: Websites users visit
   - **Apps**: Apps users use
4. **Name**: Descriptive name (e.g., "Running Shoe Shoppers")

### Best Practices

- **Keywords**: 10-50 keywords, focus on purchase intent
- **URLs**: 5-20 competitor or industry websites
- **Apps**: 3-10 relevant mobile apps
- **Combine**: Use all three signals for best performance

### Example: E-commerce Running Shoes

```
Audience: "High-Intent Running Shoe Shoppers"

Keywords:
- buy running shoes
- best running shoes 2026
- running shoes sale
- nike running shoes
- trail running shoes

URLs:
- nike.com/running
- brooksrunning.com
- asics.com
- runningwarehouse.com
- roadrunnersports.com

Apps:
- Strava
- Nike Run Club
- Runkeeper
- MapMyRun
```

---

## Remarketing Audiences

### Standard Remarketing Lists

| List Type | Definition | Membership Duration | Use Case |
|-----------|------------|---------------------|----------|
| **All Visitors** | Anyone who visited site | 30-540 days | General remarketing |
| **Product Viewers** | Viewed specific products | 30-90 days | Product-specific ads |
| **Cart Abandoners** | Added to cart, didn't buy | 7-30 days | Conversion recovery |
| **Past Purchasers** | Completed purchase | 90-540 days | Upsell, cross-sell |
| **High-Value Visitors** | Spent >5 min or viewed >3 pages | 30-90 days | Engaged users |

### Dynamic Remarketing

**Requirements**:
- Google Merchant Center feed OR
- Custom parameters on website

**How it works**:
1. User views Product A on your site
2. User leaves without purchasing
3. User sees ad featuring Product A (+ related products)

**Performance**:
- 2-3x higher CTR than standard remarketing
- 30-50% lower CPA
- Requires product feed setup

### Remarketing List Setup

**Google Ads Tag**:
```html
<!-- Global site tag (gtag.js) - Google Ads -->
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-XXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'AW-XXXXXXXXX');
</script>
```

**Custom Parameters** (for dynamic remarketing):
```javascript
gtag('event', 'page_view', {
  'send_to': 'AW-XXXXXXXXX',
  'ecomm_prodid': 'PRODUCT_ID',
  'ecomm_pagetype': 'product',
  'ecomm_totalvalue': 99.99
});
```

---

## Similar Audiences

### What Are Similar Audiences?

Users with similar characteristics to your existing audiences (remarketing lists, customer lists).

### How to Create

1. **Seed Audience**: Remarketing list with 1,000+ users
2. **Google Creates**: Similar audience automatically
3. **Size**: Typically 10-50x larger than seed audience

### Performance

| Metric | Seed Audience (Remarketing) | Similar Audience |
|--------|----------------------------|------------------|
| CTR | 1.5% | 0.8% |
| CVR | 3.0% | 1.2% |
| CPA | $50 | $80 |
| Reach | 10,000 | 200,000 |

**Use Case**: Expand reach while maintaining some relevance

---

## Demographic Targeting

### Available Demographics

| Demographic | Options | Use Case |
|-------------|---------|----------|
| **Age** | 18-24, 25-34, 35-44, 45-54, 55-64, 65+ | Age-specific products |
| **Gender** | Male, Female, Unknown | Gender-specific products |
| **Parental Status** | Parent, Not a parent | Family products |
| **Household Income** | Top 10%, 11-20%, 21-30%, etc. | Luxury vs. budget products |

### Layering Demographics

**Example**: Target women aged 25-44 with household income in top 30%

```
Audience: In-Market > Apparel & Accessories > Women's Clothing
+ Demographics:
  - Gender: Female
  - Age: 25-34, 35-44
  - Household Income: Top 10%, 11-20%, 21-30%
```

---

## Audience Layering Strategies

### Strategy 1: Audience + Contextual

**Combine**:
- Audience: In-Market > Running Shoes
- Contextual: Topics > Sports > Running

**Result**: Ads show to in-market users on running-related websites

### Strategy 2: Multiple Audiences

**Combine**:
- Affinity: Sports & Fitness > Running Enthusiasts
- In-Market: Apparel & Accessories > Athletic Apparel

**Result**: Users interested in running AND actively shopping for athletic apparel

### Strategy 3: Remarketing + Similar

**Combine**:
- Remarketing: Cart Abandoners
- Similar Audiences: Similar to Cart Abandoners

**Result**: Re-engage abandoners + reach new users with similar behavior

---

## Audience Exclusions

### Why Exclude Audiences?

- **Avoid ad fatigue**: Exclude recent purchasers
- **Budget efficiency**: Exclude low-value audiences
- **Funnel management**: Exclude bottom-funnel users from awareness campaigns

### Common Exclusions

| Exclusion | Reason | Campaign Type |
|-----------|--------|---------------|
| **Recent Purchasers** | Avoid ad fatigue | All campaigns |
| **Converters (last 30 days)** | Already converted | Acquisition campaigns |
| **Employees** | Internal traffic | All campaigns |
| **Low-Value Visitors** | <10 sec on site | All campaigns |

---

## Audience Performance Analysis

### Key Metrics

| Metric | What It Tells You | Action |
|--------|-------------------|--------|
| **CTR** | Ad relevance to audience | Low CTR = improve ad creative |
| **CVR** | Audience quality | Low CVR = wrong audience or LP |
| **CPA** | Cost efficiency | High CPA = adjust bids or exclude |
| **ROAS** | Revenue efficiency | Low ROAS = exclude or lower bids |

### Optimization Actions

1. **High CTR, Low CVR**: Improve landing page relevance
2. **Low CTR, High CVR**: Improve ad creative
3. **High CPA**: Lower bids or exclude audience
4. **Low Volume**: Expand audience or increase bids

---

## Audience Testing Framework

### Phase 1: Discovery (Weeks 1-4)

- **Mode**: Observation
- **Audiences**: 5-10 different audience types
- **Goal**: Identify top performers

### Phase 2: Optimization (Weeks 5-8)

- **Mode**: Targeting
- **Audiences**: Top 3-5 performers from Phase 1
- **Goal**: Improve efficiency

### Phase 3: Scaling (Weeks 9+)

- **Mode**: Targeting
- **Audiences**: Expand top performers (similar audiences, layering)
- **Goal**: Increase volume while maintaining efficiency

---

## Advanced Audience Tactics

### Customer Match

**Upload customer email lists** to create audiences

**Use Cases**:
- Re-engage past customers
- Exclude current customers
- Create similar audiences

**Requirements**:
- 1,000+ emails
- Hashed (SHA256)
- Compliant with privacy policies

### Life Events

**Target users experiencing major life events**:
- Moving
- Marriage
- Graduation
- Job change

**Use Case**: Products/services relevant to life transitions

### Detailed Demographics

**Target based on**:
- Education level
- Homeownership status
- Employment (company size, industry)

**Use Case**: B2B targeting, luxury products

---

## Audience Targeting Checklist

### Setup
- [ ] Install Google Ads remarketing tag
- [ ] Create remarketing lists (all visitors, product viewers, cart abandoners)
- [ ] Set up custom intent audiences (keywords, URLs, apps)
- [ ] Enable similar audiences
- [ ] Configure demographic targeting

### Testing
- [ ] Start with Observation mode (2-4 weeks)
- [ ] Test 5-10 different audience types
- [ ] Analyze performance by audience
- [ ] Identify top 3-5 performers

### Optimization
- [ ] Switch to Targeting mode for top performers
- [ ] Exclude low-performing audiences
- [ ] Layer audiences for better targeting
- [ ] Create similar audiences from top performers
- [ ] Adjust bids by audience performance

### Ongoing
- [ ] Review audience performance monthly
- [ ] Test new audience types quarterly
- [ ] Update remarketing lists (membership duration)
- [ ] Refresh custom intent audiences (keywords, URLs)