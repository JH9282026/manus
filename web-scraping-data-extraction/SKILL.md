---
name: web-scraping-data-extraction
description: The Web Scraping & Data Extraction skill is an advanced, autonomous data acquisition capability designed to programmatically collect, process, and structure information from any publicly accessible web source.
---

---
name: Web Scraping & Data Extraction
description: A comprehensive, production-grade web scraping skill capable of extracting, structuring, cleaning, and validating any publicly available data from the internet while maintaining strict compliance with legal and ethical standards.
---

# Web Scraping & Data Extraction Skill

## 1. Skill Description and Purpose

### Overview

The Web Scraping & Data Extraction skill is an advanced, autonomous data acquisition capability designed to programmatically collect, process, and structure information from any publicly accessible web source. This skill transforms unstructured web content into clean, validated, analysis-ready datasets that can be immediately utilized for business intelligence, market research, lead generation, competitive analysis, and countless other data-driven applications.

### Core Value Proposition

This skill eliminates the manual labor of data collection by automating the entire pipeline from source identification through final delivery. It handles the full complexity of modern web architectures—including JavaScript-rendered content, infinite scroll pagination, anti-bot protections, and dynamic AJAX loading—while maintaining data quality through comprehensive validation and cleaning processes.

### When to Deploy This Skill

**Primary Use Cases:**
- **Lead Generation Campaigns:** Extract contact information, company details, and professional profiles from directories, LinkedIn, business databases, and industry-specific platforms to build targeted prospect lists
- **Competitive Intelligence:** Monitor competitor pricing, product catalogs, marketing content, customer reviews, and market positioning across e-commerce platforms and industry websites
- **Market Research:** Aggregate industry statistics, news articles, trend data, and public sentiment from multiple sources to inform strategic decisions
- **Real Estate Analysis:** Collect property listings, pricing history, agent information, and market statistics from platforms like Zillow, Realtor.com, and local MLS systems
- **Job Market Intelligence:** Scrape job postings, salary data, skills requirements, and hiring trends from Indeed, LinkedIn Jobs, Glassdoor, and specialized job boards
- **Academic & Research Data:** Gather research papers, citations, author information, and publication data from academic databases and repositories
- **Content Aggregation:** Compile news articles, blog posts, forum discussions, and social media content for analysis or republication

**Trigger Conditions:**
- User requests extraction of specific data types from identified web sources
- Need for structured datasets that don't exist in accessible APIs or databases
- Requirement for ongoing monitoring and data refresh cycles
- Multi-source data aggregation projects requiring uniform output formatting

### Technical Capabilities

This skill implements a multi-layered scraping architecture:

1. **Static Content Layer:** HTML parsing via BeautifulSoup/lxml for server-rendered pages
2. **Dynamic Content Layer:** Headless browser automation (Playwright/Selenium) for JavaScript-dependent sites
3. **API Discovery Layer:** Automatic detection and utilization of underlying REST/GraphQL endpoints
4. **Anti-Detection Layer:** Proxy rotation, user-agent cycling, request throttling, and fingerprint randomization
5. **Data Processing Layer:** Cleaning, validation, deduplication, and format transformation pipelines

---

## 2. Required Inputs/Parameters

### Mandatory Parameters

| Parameter | Type | Description | Example |
|-----------|------|-------------|---------|
| `target_urls` | Array[String] | One or more URLs to scrape, can include patterns with wildcards | `["https://example.com/products/*", "https://directory.com/listings"]` |
| `data_schema` | Object | Definition of fields to extract with selectors or descriptions | `{"name": "CSS:.product-title", "price": "XPATH://span[@class='price']"}` |
| `output_format` | Enum | Desired output format | `csv`, `json`, `excel`, `sql`, `parquet` |

### Optional Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `pagination_config` | Object | Auto-detect | Pagination handling strategy: `{"type": "numbered", "selector": ".next-page", "max_pages": 100}` |
| `rendering_mode` | Enum | `auto` | `static` (HTML only), `dynamic` (headless browser), `auto` (detect automatically) |
| `rate_limit` | Object | `{"requests_per_minute": 30}` | Throttling configuration to respect target servers |
| `proxy_config` | Object | None | Proxy rotation settings: `{"enabled": true, "rotate_every": 10}` |
| `authentication` | Object | None | Login credentials for protected content: `{"type": "form", "username": "...", "password": "..."}` |
| `filters` | Object | None | Conditional extraction rules: `{"min_price": 100, "category": "electronics"}` |
| `deduplication` | Object | `{"enabled": true, "key_fields": ["url"]}` | Duplicate record handling |
| `validation_rules` | Object | None | Data quality checks: `{"email": "valid_format", "phone": "e164_format"}` |
| `retry_config` | Object | `{"max_retries": 3, "backoff": "exponential"}` | Error recovery settings |
| `output_path` | String | Auto-generated | Custom file path for results |
| `incremental_mode` | Boolean | `false` | Only scrape new/changed records since last run |
| `max_records` | Integer | Unlimited | Maximum number of records to extract |
| `timeout_seconds` | Integer | 30 | Request timeout threshold |
| `respect_robots_txt` | Boolean | `true` | Honor robots.txt directives |
| `include_metadata` | Boolean | `true` | Add source URL, timestamp, and extraction metadata to records |

### Data Schema Specification

The `data_schema` parameter accepts multiple selector syntaxes:

```yaml
data_schema:
  # CSS Selector
  product_name: "CSS:h1.product-title"
  
  # XPath Expression
  price: "XPATH://span[@data-testid='price']/text()"
  
  # Regular Expression (applied to page text)
  email: "REGEX:[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}"
  
  # JSON Path (for API responses)
  rating: "JSON:$.data.product.rating.average"
  
  # Natural Language Description (AI-powered extraction)
  description: "NLP:Extract the main product description paragraph"
  
  # Attribute Extraction
  image_url: "CSS:img.main-image@src"
  
  # Nested/Array Extraction
  reviews:
    _container: "CSS:div.review-item"
    author: "CSS:.reviewer-name"
    text: "CSS:.review-text"
    rating: "CSS:.star-rating@data-rating"
```

---

## 3. Expected Outputs/Deliverables

### Primary Output: Structured Dataset

The skill produces a clean, validated dataset in the requested format containing all extracted records with the following quality guarantees:

**Data Quality Standards:**
- **Completeness:** All requested fields populated where data exists; null values clearly marked
- **Accuracy:** Data matches source content with 99%+ fidelity
- **Consistency:** Uniform formatting, encoding (UTF-8), and data types across all records
- **Freshness:** Extraction timestamp included; data represents source state at collection time
- **Uniqueness:** Duplicate records removed based on specified key fields

### Output Format Specifications

**CSV Output:**
```
product_name,price,rating,url,scraped_at
"Widget Pro",29.99,4.5,https://example.com/widget-pro,2026-03-06T14:30:00Z
"Gadget Plus",49.99,4.2,https://example.com/gadget-plus,2026-03-06T14:30:01Z
```

**JSON Output:**
```json
{
  "metadata": {
    "total_records": 150,
    "scraped_at": "2026-03-06T14:30:00Z",
    "source_urls": ["https://example.com/products"],
    "schema_version": "1.0"
  },
  "data": [
    {
      "product_name": "Widget Pro",
      "price": 29.99,
      "rating": 4.5,
      "url": "https://example.com/widget-pro",
      "_metadata": {
        "scraped_at": "2026-03-06T14:30:00Z",
        "page_number": 1
      }
    }
  ]
}
```

**Excel Output:**
- Multiple sheets: `Data`, `Metadata`, `Data Dictionary`, `Extraction Log`
- Proper column formatting (currency, dates, numbers)
- Frozen header row and auto-filters enabled
- Data validation rules applied

### Secondary Outputs

| Deliverable | Description | Format |
|-------------|-------------|--------|
| `extraction_log.json` | Detailed log of all requests, responses, and processing steps | JSON |
| `data_dictionary.md` | Field definitions, data types, and source mapping | Markdown |
| `quality_report.json` | Validation results, error counts, completeness metrics | JSON |
| `failed_urls.txt` | List of URLs that couldn't be scraped with error reasons | Text |
| `screenshots/` | Visual captures of scraped pages (if enabled) | PNG |

### Quality Metrics Included

```json
{
  "total_records_extracted": 1500,
  "total_records_after_dedup": 1423,
  "fields_completeness": {
    "product_name": 100.0,
    "price": 98.5,
    "rating": 87.2,
    "description": 95.1
  },
  "validation_results": {
    "emails_valid": 412,
    "emails_invalid": 8,
    "phones_formatted": 380
  },
  "extraction_duration_seconds": 245,
  "pages_processed": 75,
  "errors_encountered": 3
}
```

---

## 4. Example Use Cases

### Use Case 1: B2B Lead Generation from Business Directories

**Scenario:** Extract decision-maker contacts from a business directory for a sales outreach campaign targeting SaaS companies in the Bay Area.

**Input Configuration:**
```yaml
target_urls:
  - "https://businessdirectory.com/search?industry=saas&location=san-francisco"
data_schema:
  company_name: "CSS:h2.company-title"
  website: "CSS:a.company-website@href"
  contact_name: "CSS:.contact-person-name"
  contact_title: "CSS:.contact-title"
  email: "REGEX:[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}"
  phone: "CSS:.phone-number"
  address: "CSS:.address-block"
  employee_count: "CSS:.company-size"
  linkedin_url: "CSS:a[href*='linkedin.com']@href"
pagination_config:
  type: "numbered"
  max_pages: 50
output_format: "excel"
validation_rules:
  email: "valid_format"
  phone: "us_format"
```

**Expected Output:** Excel file with 500+ qualified leads including company info, contact details, and LinkedIn profiles, with validated email addresses and formatted phone numbers.

---

### Use Case 2: E-commerce Competitive Price Monitoring

**Scenario:** Track competitor pricing for 200 products across Amazon, Walmart, and Target to inform pricing strategy.

**Input Configuration:**
```yaml
target_urls:
  - "https://amazon.com/dp/{product_ids}"
  - "https://walmart.com/ip/{product_ids}"
  - "https://target.com/p/{product_ids}"
product_ids: ["B08N5WRWNW", "B09V3KXJPB", ...]  # 200 SKUs
data_schema:
  product_name: "NLP:Extract the main product title"
  current_price: "CSS:[data-price], .price-current"
  original_price: "CSS:.was-price, .list-price"
  availability: "CSS:.availability-status"
  seller: "CSS:.seller-name"
  rating: "CSS:.star-rating"
  review_count: "CSS:.review-count"
  shipping_info: "CSS:.shipping-details"
rendering_mode: "dynamic"  # Required for JS-rendered prices
output_format: "json"
include_metadata: true
```

**Expected Output:** JSON dataset with current pricing across all three retailers, price differentials calculated, and availability status enabling real-time pricing decisions.

---

### Use Case 3: Real Estate Market Analysis

**Scenario:** Aggregate property listings from Zillow, Redfin, and Realtor.com for a specific metro area to analyze market trends.

**Input Configuration:**
```yaml
target_urls:
  - "https://zillow.com/austin-tx/sold/?searchQueryState={encoded_params}"
  - "https://redfin.com/city/austin/TX/recently-sold"
  - "https://realtor.com/realestateandhomes-sold/Austin_TX"
data_schema:
  address: "CSS:.property-address"
  price: "CSS:.price"
  bedrooms: "CSS:.beds"
  bathrooms: "CSS:.baths"
  sqft: "CSS:.sqft"
  lot_size: "CSS:.lot-size"
  year_built: "CSS:.year-built"
  property_type: "CSS:.property-type"
  listing_date: "CSS:.list-date"
  sold_date: "CSS:.sold-date"
  days_on_market: "CSS:.dom"
  price_per_sqft: "CALC:price/sqft"
  agent_name: "CSS:.agent-name"
  agent_phone: "CSS:.agent-phone"
  coordinates: "JSON:$.property.location"
pagination_config:
  type: "infinite_scroll"
  scroll_delay_ms: 2000
  max_scrolls: 100
output_format: "parquet"
deduplication:
  key_fields: ["address", "sold_date"]
```

**Expected Output:** Parquet file with 5,000+ property records including calculated price/sqft, geocoordinates for mapping, and agent contact info—ready for statistical analysis and visualization.

---

### Use Case 4: Job Market Skills Analysis

**Scenario:** Analyze in-demand skills and salary ranges for "Data Engineer" roles to inform career development or hiring strategies.

**Input Configuration:**
```yaml
target_urls:
  - "https://indeed.com/jobs?q=data+engineer&l=remote"
  - "https://linkedin.com/jobs/search/?keywords=data%20engineer"
  - "https://glassdoor.com/Job/data-engineer-jobs-SRCH_KO0,13.htm"
data_schema:
  job_title: "CSS:.job-title"
  company: "CSS:.company-name"
  location: "CSS:.job-location"
  salary_min: "REGEX:\\$([0-9,]+)\\s*-"
  salary_max: "REGEX:-\\s*\\$([0-9,]+)"
  job_type: "CSS:.job-type"
  experience_level: "NLP:Extract required years of experience"
  skills_required: "NLP:Extract all technical skills mentioned (return as array)"
  education_required: "NLP:Extract education requirements"
  posting_date: "CSS:.post-date"
  job_url: "CSS:a.job-link@href"
filters:
  posted_within_days: 30
output_format: "csv"
```

**Expected Output:** CSV with 2,000+ job postings, normalized salary ranges, extracted skills arrays enabling frequency analysis (e.g., "Python appears in 85% of listings"), and experience requirements—supporting data-driven career or hiring decisions.

---

### Use Case 5: Review Sentiment Aggregation

**Scenario:** Collect customer reviews for a product across multiple platforms to perform sentiment analysis and identify common complaints.

**Input Configuration:**
```yaml
target_urls:
  - "https://amazon.com/product-reviews/{asin}"
  - "https://bestbuy.com/site/reviews/{sku}"
  - "https://walmart.com/reviews/product/{product_id}"
data_schema:
  reviewer_name: "CSS:.reviewer-name"
  review_title: "CSS:.review-title"
  review_text: "CSS:.review-body"
  rating: "CSS:.star-rating@data-rating"
  review_date: "CSS:.review-date"
  verified_purchase: "CSS:.verified-badge"
  helpful_votes: "CSS:.helpful-count"
  source_platform: "CONST:{source_url_domain}"
pagination_config:
  type: "next_button"
  selector: "a.next-page"
  max_pages: 20
output_format: "json"
```

**Expected Output:** JSON dataset with 1,000+ reviews across platforms, standardized rating scale (1-5), and review text ready for NLP sentiment analysis and topic modeling.

---

## 5. Prerequisites and Dependencies

### Required Tools and Libraries

| Category | Tools | Purpose |
|----------|-------|---------|
| **HTTP Clients** | `requests`, `httpx`, `aiohttp` | Making HTTP requests with session management |
| **HTML Parsing** | `beautifulsoup4`, `lxml`, `html5lib` | Parsing and navigating HTML/XML documents |
| **Browser Automation** | `playwright`, `selenium`, `puppeteer` | Rendering JavaScript-dependent pages |
| **Data Processing** | `pandas`, `polars` | Data manipulation, cleaning, and transformation |
| **Output Formats** | `openpyxl`, `pyarrow`, `sqlalchemy` | Writing Excel, Parquet, and SQL outputs |
| **Validation** | `email-validator`, `phonenumbers`, `validators` | Data quality validation |
| **Anti-Detection** | `fake-useragent`, `rotating-proxies` | Avoiding bot detection |
| **Concurrency** | `asyncio`, `concurrent.futures`, `celery` | Parallel request handling |

### System Requirements

- **Python Version:** 3.9+
- **Memory:** Minimum 4GB RAM (8GB+ recommended for large datasets)
- **Storage:** Sufficient disk space for output files and browser cache
- **Network:** Stable internet connection; proxy service subscription for high-volume scraping
- **Browser:** Chromium/Chrome installation for headless browser operations

### External Service Dependencies

| Service | Purpose | When Required |
|---------|---------|---------------|
| **Proxy Provider** | IP rotation to avoid rate limiting | High-volume scraping, sites with aggressive bot detection |
| **CAPTCHA Solver** | Automated CAPTCHA resolution | Sites with CAPTCHA challenges (use sparingly) |
| **Geocoding API** | Address validation and coordinate lookup | Real estate and location-based scraping |
| **Email Verification** | Validate extracted email addresses | Lead generation campaigns |

### Legal and Compliance Prerequisites

**Before executing any scraping operation, verify:**

1. **Robots.txt Compliance:** Parse and respect directives at `{target_domain}/robots.txt`
2. **Terms of Service Review:** Confirm scraping is not explicitly prohibited
3. **Data Protection Laws:**
   - GDPR (EU): Lawful basis for processing personal data
   - CCPA (California): Consumer data handling requirements
   - PIPEDA (Canada): Consent and purpose limitations
4. **Rate Limiting:** Configure appropriate delays (minimum 1-2 seconds between requests to same domain)
5. **Data Retention Policy:** Define how long scraped data will be stored and how it will be secured

### Pre-Execution Checklist

```markdown
- [ ] Target URLs are publicly accessible (no authentication required unless credentials provided)
- [ ] Data schema fields are mapped to valid selectors
- [ ] Output directory has write permissions
- [ ] Rate limits are configured appropriately for target sites
- [ ] Proxy configuration is valid (if high-volume scraping)
- [ ] robots.txt has been checked and respected
- [ ] Legal review completed for target sites and data types
- [ ] Deduplication keys are defined to prevent duplicates
- [ ] Validation rules are specified for critical fields
- [ ] Error handling and retry logic are configured
```

### Skill Invocation Protocol

1. **Validate inputs:** Confirm all required parameters are provided and properly formatted
2. **Compliance check:** Verify robots.txt and ToS compliance for all target domains
3. **Initialize scrapers:** Set up HTTP clients, browser instances, and proxy rotation
4. **Execute extraction:** Process URLs according to pagination and rate-limit configurations
5. **Process data:** Clean, validate, deduplicate, and transform extracted records
6. **Generate outputs:** Write primary dataset and secondary deliverables
7. **Quality report:** Produce metrics on completeness, validation results, and errors
8. **Cleanup:** Close browser instances, release connections, archive logs

---

## Appendix: Quick Reference

### Common Selector Patterns

| Data Type | CSS Selector Pattern | XPath Pattern |
|-----------|---------------------|---------------|
| Email | `a[href^="mailto:"]` | `//a[starts-with(@href,'mailto:')]` |
| Phone | `.phone, [itemprop="telephone"]` | `//*[@itemprop='telephone']` |
| Price | `[data-price], .price, .cost` | `//*[contains(@class,'price')]` |
| Address | `[itemprop="address"], .address` | `//*[@itemprop='address']` |
| Image | `img.product-image@src` | `//img[contains(@class,'product')]/@src` |
| Link | `a.item-link@href` | `//a[contains(@class,'item')]/@href` |

### Rate Limit Guidelines by Site Type

| Site Category | Recommended Rate | Notes |
|---------------|------------------|-------|
| Small business sites | 5-10 req/min | Be very gentle |
| Medium commercial sites | 20-30 req/min | Standard rate |
| Large e-commerce | 30-60 req/min | May have anti-bot |
| News/media sites | 20-40 req/min | Respect peak hours |
| Government/public data | 10-20 req/min | Often rate-limited |
| Social platforms | Use official APIs | Scraping often prohibited |

### Error Code Reference

| Code | Meaning | Resolution |
|------|---------|------------|
| 403 | Forbidden/Blocked | Rotate proxy, adjust headers |
| 429 | Rate Limited | Reduce request frequency |
| 503 | Service Unavailable | Retry with backoff |
| CAPTCHA | Bot detection triggered | Use CAPTCHA solver or manual intervention |
| TIMEOUT | Request timed out | Increase timeout, retry |
| PARSE_ERROR | Selector not found | Verify selector accuracy |
