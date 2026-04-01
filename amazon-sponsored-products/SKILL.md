---
name: amazon-sponsored-products
description: "Create and optimize Amazon Sponsored Products campaigns for product advertising on Amazon search results and product pages. Use for keyword targeting, automatic and manual targeting, bid optimization, negative keyword management, product targeting, campaign structure, ACOS optimization, and driving product sales through cost-per-click advertising on Amazon marketplace."
---

# Amazon Sponsored Products

Create keyword-targeted product advertising campaigns on Amazon search results and product detail pages.

## Overview

This skill covers Amazon Sponsored Products campaign creation, keyword targeting strategies, bid optimization, and ACOS (Advertising Cost of Sale) management. Use it for driving product visibility and sales on Amazon through CPC advertising.

## Campaign Types

### Automatic Targeting

**How it works**: Amazon automatically targets keywords and products based on your product listing

**Match Types**:
- **Close Match**: Closely related searches
- **Loose Match**: Loosely related searches
- **Substitutes**: Similar products
- **Complements**: Frequently bought together

**When to use**:
- New products (keyword discovery)
- Limited keyword research time
- Testing new markets

### Manual Targeting

**Keyword Targeting**:
- **Broad Match**: Wide reach, less control
- **Phrase Match**: Moderate reach and control
- **Exact Match**: Highest control, lowest reach

**Product Targeting**:
- Target specific ASINs
- Target categories
- Target brands

**When to use**:
- Established products
- Specific keyword strategy
- Competitive targeting

## Campaign Structure

### Single Product Campaigns

```
Campaign: Product A - Sponsored Products
├── Ad Group: Automatic Targeting
│   └── All match types enabled
├── Ad Group: Branded Keywords (Exact)
│   └── [brand name product], [product model]
├── Ad Group: Generic Keywords (Phrase)
│   └── "product category", "product type"
└── Ad Group: Competitor Targeting
    └── Competitor ASINs, competitor brands
```

### Multi-Product Campaigns

```
Campaign: Category - Sponsored Products
├── Ad Group: Product A
│   └── Product A specific keywords
├── Ad Group: Product B
│   └── Product B specific keywords
└── Ad Group: Product C
    └── Product C specific keywords
```

## Keyword Research

### Sources

1. **Amazon Search Bar** - Autocomplete suggestions
2. **Competitor Listings** - Title, bullets, description keywords
3. **Customer Reviews** - Language customers use
4. **Search Term Report** - Auto campaign discoveries
5. **Third-Party Tools** - Helium 10, Jungle Scout, Cerebro

### Keyword Types

| Type | Examples | Intent | Bid Strategy |
|------|----------|--------|--------------|
| **Branded** | "nike running shoes" | High | High bids |
| **Generic** | "running shoes" | Medium | Medium bids |
| **Long-Tail** | "women's trail running shoes size 8" | High | Medium-high bids |
| **Competitor** | "adidas running shoes" | Medium | Test bids |

## Bidding Strategies

### Bid Adjustment Options

| Strategy | Behavior | Use Case |
|----------|----------|----------|
| **Dynamic Bids - Down Only** | Lower bids for unlikely conversions | Conservative, protect ACOS |
| **Dynamic Bids - Up and Down** | Raise/lower bids based on likelihood | Balanced, maximize sales |
| **Fixed Bids** | No automatic adjustments | Full control, testing |

### Placement Multipliers

| Placement | Default Bid | Multiplier Range | Recommended |
|-----------|-------------|------------------|-------------|
| **Top of Search** | Base bid | 0-900% | +50-200% |
| **Product Pages** | Base bid | 0-900% | +0-50% |

## ACOS Optimization

### ACOS Formula

```
ACOS = (Ad Spend / Ad Revenue) × 100

Example:
Ad Spend: $100
Ad Revenue: $500
ACOS: ($100 / $500) × 100 = 20%
```

### ACOS Targets

| Product Stage | Target ACOS | Strategy |
|---------------|-------------|----------|
| **Launch** | 30-50% | Aggressive, gain visibility |
| **Growth** | 20-30% | Balanced, scale sales |
| **Mature** | 10-20% | Profitable, optimize |
| **Clearance** | 40-60% | Move inventory |

### Break-Even ACOS

```
Break-Even ACOS = Profit Margin %

Example:
Product Price: $50
Product Cost: $30
Profit Margin: ($50 - $30) / $50 = 40%
Break-Even ACOS: 40%
```

## Negative Keywords

### When to Add Negatives

- **Zero sales, high spend** (>$10, 0 orders)
- **Irrelevant searches** (wrong product type)
- **Low conversion rate** (<1% after 50+ clicks)

### Negative Keyword Strategy

**Campaign-Level**:
- Broad negatives (e.g., "free", "cheap", "used")
- Irrelevant product types

**Ad Group-Level**:
- Prevent keyword cannibalization
- Refine targeting within campaign

## Performance Benchmarks

| Metric | Good Benchmark | Excellent |
|--------|----------------|-----------|
| **CTR** | 0.3-0.5% | >0.5% |
| **CVR** | 10-15% | >15% |
| **ACOS** | 20-30% | <20% |
| **CPC** | $0.50-$1.50 | <$0.50 |

## Optimization Workflow

### Weekly Tasks
- Review search term report
- Add high-performing terms as keywords
- Add irrelevant terms as negatives
- Adjust bids on top keywords (±10-20%)

### Monthly Tasks
- Analyze ACOS by campaign/ad group
- Pause low-performing keywords (ACOS >50%, no sales)
- Test new keyword themes
- Review competitor targeting performance

## Using the Reference Files

**`/references/sponsored-products-setup.md`** — Read when creating Sponsored Products campaigns, including campaign structure, targeting options, and initial bid strategies.

**`/references/acos-optimization-strategies.md`** — Read when optimizing ACOS, including bid management, keyword optimization, and profitability analysis.

**`/references/keyword-harvesting.md`** — Read when mining search term reports for new keywords, including harvesting workflows and negative keyword strategies.
