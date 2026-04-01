---
name: amazon-advertising-api
description: "Automate Amazon Advertising using Amazon Ads API for programmatic campaign management across Sponsored Products, Sponsored Brands, and Sponsored Display. Use for bulk operations, automated reporting, bid management, campaign creation at scale, API authentication, portfolio management, and building custom Amazon Ads tools for sellers and agencies."
---

# Amazon Advertising API

Programmatically manage Amazon Advertising campaigns using Amazon Ads API for automation and custom integrations.

## Overview

This skill covers Amazon Ads API authentication, campaign management, bulk operations, and reporting automation. Use it for managing large Amazon Ads accounts, building custom tools, and integrating with external systems.

## API Access

### Requirements

- **Amazon Advertising Account** (Seller or Vendor)
- **API Access** (request via Amazon Advertising Console)
- **OAuth 2.0 Credentials**
- **Profile ID** (marketplace-specific)

### Supported Campaign Types

| Campaign Type | API Support | Complexity |
|---------------|-------------|------------|
| **Sponsored Products** | Full | Medium |
| **Sponsored Brands** | Full | Medium |
| **Sponsored Display** | Full | Medium |
| **Amazon DSP** | Limited | High |

## API Versions

### Sponsored Products API

**Versions**:
- **v2**: Legacy, still supported
- **v3**: Current, recommended

**Key Operations**:
- Campaign CRUD
- Ad group management
- Keyword targeting
- Product targeting
- Negative keywords
- Bid management

### Sponsored Brands API

**Operations**:
- Campaign management
- Keyword targeting
- Creative management (headlines, logos)
- Store Spotlight configuration

### Reporting API

**Report Types**:
- Campaign performance
- Keyword performance
- Search term reports
- Product targeting reports
- Placement reports

## Common Use Cases

| Use Case | Complexity | Value |
|----------|------------|-------|
| **Automated Reporting** | Low | High - Daily dashboards |
| **Bid Automation** | Medium | High - Rule-based bidding |
| **Bulk Campaign Creation** | Medium | High - Launch 100s of campaigns |
| **Keyword Harvesting** | Medium | High - Auto-add search terms |
| **Budget Pacing** | High | High - Optimize spend |

## Authentication

### OAuth 2.0 Flow

1. **Register Application** in Amazon Advertising Console
2. **Get Client ID and Secret**
3. **Request Authorization Code** (user consent)
4. **Exchange for Access Token**
5. **Refresh Token** (expires every hour)

### API Endpoints

**North America**: `https://advertising-api.amazon.com`
**Europe**: `https://advertising-api-eu.amazon.com`
**Far East**: `https://advertising-api-fe.amazon.com`

## Automation Examples

### Bid Automation

**Rule**: If ACOS > 30% for 7 days, decrease bid by 10%

```python
# Pseudocode
for keyword in keywords:
    if keyword.acos > 0.30 and keyword.days_high_acos >= 7:
        new_bid = keyword.bid * 0.90
        update_keyword_bid(keyword.id, new_bid)
```

### Keyword Harvesting

**Rule**: If search term has 2+ orders and ACOS < 25%, add as keyword

```python
# Pseudocode
for search_term in search_term_report:
    if search_term.orders >= 2 and search_term.acos < 0.25:
        add_keyword(search_term.text, match_type='PHRASE')
        add_negative_keyword(search_term.text, match_type='EXACT', campaign='Auto')
```

## Rate Limits

| Operation | Rate Limit |
|-----------|------------|
| **API Calls** | 200 requests/second |
| **Report Requests** | 100/minute |
| **Bulk Operations** | 1,000 entities/request |

## Using the Reference Files

**`/references/amazon-ads-api-setup.md`** — Read when setting up API access, including OAuth configuration, profile selection, and authentication troubleshooting.

**`/references/api-automation-workflows.md`** — Read when building automation scripts, including bid management, keyword harvesting, and reporting automation.
