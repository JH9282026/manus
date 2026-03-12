---
name: seo-copywriting-optimization
description: SEO Copywriting & Optimization is the discipline of creating content that satisfies both search engine algorithms and human readers.
---

---
name: SEO Copywriting & Optimization
description: Create search-engine-optimized content that ranks for target keywords while maintaining compelling readability and driving user engagement, conversions, and organic traffic growth.
---

## 1. Skill Description and Purpose

SEO Copywriting & Optimization is the discipline of creating content that satisfies both search engine algorithms and human readers. This skill balances technical optimization requirements—keywords, structure, metadata—with persuasive, engaging writing that keeps visitors on page and drives desired actions.

**Why This Skill is Valuable:**
- Organic search drives 53% of all website traffic across industries
- SEO content creates compounding assets that generate traffic for years
- Reduces dependency on paid advertising for customer acquisition
- Builds domain authority that benefits all site pages
- Captures high-intent traffic at the moment of search
- Provides sustainable competitive advantages difficult for competitors to replicate

**When to Deploy This Skill:**
- Creating new blog posts, articles, and landing pages targeting specific keywords
- Optimizing existing underperforming content for improved rankings
- Writing product and category pages for e-commerce sites
- Developing pillar content and topic cluster architectures
- Creating local SEO content for geographic targeting
- Building FAQ pages and knowledge bases
- Writing meta titles, descriptions, and structured data content
- Optimizing content for featured snippets and SERP features

This skill integrates keyword research interpretation, search intent analysis, on-page optimization techniques, and user experience principles to create content that ranks, engages, and converts.

---

## 2. Required Inputs/Parameters

| Parameter | Required | Format | Description |
|-----------|----------|--------|-------------|
| `primary_keyword` | Yes | String | Main target keyword or phrase with search volume and difficulty data |
| `secondary_keywords` | Yes | Array | Supporting keywords, LSI terms, and related phrases |
| `search_intent` | Yes | Enum | Options: `informational`, `navigational`, `transactional`, `commercial_investigation` |
| `content_type` | Yes | Enum | Options: `blog_post`, `landing_page`, `product_page`, `category_page`, `pillar_page`, `faq`, `guide` |
| `target_word_count` | Yes | Integer | Based on SERP analysis of ranking content |
| `competitor_content_analysis` | Recommended | Array | Top 10 ranking pages with structure, word count, and content gaps |
| `brand_voice_guidelines` | Recommended | Object | Tone, vocabulary, and style preferences |
| `existing_content` | Optional | String | For optimization tasks, the current content to improve |
| `internal_linking_targets` | Optional | Array | Related pages to link to within the content |
| `featured_snippet_opportunity` | Optional | Boolean | Whether to optimize for position zero |
| `local_seo_parameters` | Optional | Object | Geographic targeting, local keywords, NAP data |
| `schema_requirements` | Optional | Enum | Structured data types: `article`, `product`, `faq`, `howto`, `review` |

**Input Quality Standards:**
- Primary keyword should have realistic ranking potential given domain authority
- Search intent classification should be based on SERP analysis, not assumption
- Competitor analysis should identify content gaps and structural patterns

---

## 3. Expected Outputs/Deliverables

**Primary Deliverable:** Fully optimized content piece ready for publication

**Output Components:**

| Component | Description |
|-----------|-------------|
| `meta_title` | 50-60 characters, includes primary keyword, compelling for CTR |
| `meta_description` | 150-160 characters, includes keyword, clear value proposition, call-to-action |
| `url_slug` | Clean, keyword-inclusive, hyphen-separated |
| `h1_headline` | Single H1 incorporating primary keyword naturally |
| `content_outline` | Hierarchical heading structure (H2, H3, H4) with keyword distribution |
| `body_content` | Full article with natural keyword integration, proper density (1-2%), and semantic variations |
| `internal_links` | Contextual links to related site content with varied anchor text |
| `image_optimization` | Alt text recommendations, file naming conventions, caption suggestions |
| `schema_markup` | Structured data code for enhanced SERP display |
| `featured_snippet_optimization` | Formatted content blocks targeting position zero (if applicable) |
| `readability_score` | Target Flesch-Kincaid score with adjustments if needed |
| `optimization_checklist` | Technical SEO verification points |

**Quality Standards:**
- Primary keyword in title, H1, first 100 words, and naturally throughout
- Keyword density between 1-2% without forced repetition
- Clear content hierarchy with descriptive subheadings
- Comprehensive coverage exceeding competitor depth
- Mobile-friendly formatting with short paragraphs and scannable structure
- No keyword stuffing or unnatural phrasing
- E-E-A-T signals (Experience, Expertise, Authoritativeness, Trustworthiness)

---

## 4. Example Use Cases

### Use Case 1: Comprehensive Guide Creation
**Context:** SaaS company targeting "project management best practices" (2,400 monthly searches)
**Inputs:** Keyword data, top 10 SERP analysis showing 3,000-5,000 word guides ranking, competitor content gaps
**Output:** 4,500-word definitive guide with 12 H2 sections, downloadable templates, expert quotes, FAQ schema, and internal links to product features

### Use Case 2: Product Category Page Optimization
**Context:** E-commerce site optimizing "men's running shoes" category page
**Inputs:** Keyword cluster (main + 50 long-tail variations), competitor category page structures, current page performance data
**Output:** Optimized category page with keyword-rich intro content, filterable product grid, buying guide section, FAQ accordion, and product schema markup

### Use Case 3: Local Service Page Creation
**Context:** Plumber creating city-specific landing pages for "emergency plumber [city]"
**Inputs:** 15 target cities, local keyword variations, service areas, customer review data
**Output:** Template-based but unique city pages with local content signals, embedded maps, area-specific testimonials, LocalBusiness schema, and clear contact CTAs

### Use Case 4: Existing Content Refresh
**Context:** Blog post ranking position 15-20 for target keyword, losing traffic over 6 months
**Inputs:** Current content, Google Search Console data, updated competitor analysis, fresh keyword research
**Output:** Content refresh with expanded sections, updated statistics, new heading structure, refreshed internal links, and enhanced featured snippet targeting

### Use Case 5: Featured Snippet Capture
**Context:** Targeting "how to calculate ROI" featured snippet currently held by competitor
**Inputs:** Current snippet format (paragraph/list/table), competitor content structure, search intent analysis
**Output:** Optimized content with direct answer in first 40-60 words, supporting definition box, step-by-step list format, and comparison table—all snippet-eligible formats

---

## 5. Prerequisites or Dependencies

**Required Access:**
- Keyword research data (search volume, difficulty, intent)
- SERP analysis for target keywords
- Brand voice and style guidelines
- CMS or publishing platform access

**Recommended Tools Integration:**
- SEO platforms (Ahrefs, SEMrush, Moz) for keyword and competitor data
- Content optimization tools (Clearscope, Surfer SEO, MarketMuse)
- Readability analyzers (Hemingway, Readable)
- Schema markup generators and validators
- Google Search Console for performance data

**Knowledge Dependencies:**
- On-page SEO fundamentals (title tags, meta descriptions, heading hierarchy)
- Search intent classification methodology
- Google's E-E-A-T quality guidelines
- Technical SEO basics (page speed, mobile-friendliness, Core Web Vitals)
- Content freshness and update signals

**Skill Dependencies:**
- Keyword Research & Analysis capabilities
- Competitive Content Analysis
- Basic HTML understanding for schema implementation
- Analytics Interpretation for optimization decisions

**Technical Requirements:**
- Understanding of CMS SEO capabilities and limitations
- Familiarity with schema.org vocabulary
- Knowledge of image optimization best practices
- Awareness of page speed impact on content decisions

**Common Integration Points:**
- Content management systems for publication
- Analytics platforms for performance tracking
- Rank tracking tools for position monitoring
- Internal linking analysis tools
- Content audit platforms for refresh prioritization
