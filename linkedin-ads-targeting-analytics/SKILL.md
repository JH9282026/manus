---
name: linkedin-ads-targeting-analytics
description: "Advanced targeting and analytics for LinkedIn advertising including job titles, companies, industries, skills, groups, demographics, matched audiences, lookalike audiences, and campaign analytics via LinkedIn Marketing API. Use for: implementing professional targeting, creating matched audiences, building lookalike audiences, analyzing campaign performance, generating reports, and optimizing LinkedIn ad campaigns for B2B marketing."
---

# LinkedIn Ads Targeting & Analytics

Advanced audience targeting and performance analytics for LinkedIn advertising using the Marketing API for B2B campaign optimization.

## Overview

Comprehensive guide to LinkedIn's professional targeting capabilities and analytics including job-based targeting, company targeting, matched audiences, lookalike audiences, and detailed performance reporting.

## Professional Targeting

### Job Titles
```python
targeting = {
    "include": {
        "and": [
            {
                "or": {
                    "urn:li:adTargetingFacet:titles": [
                        "urn:li:title:100",  # CTO
                        "urn:li:title:9",    # VP Engineering
                        "urn:li:title:2732"  # Software Engineer
                    ]
                }
            }
        ]
    }
}
```

### Job Functions
```python
targeting = {
    "include": {
        "and": [
            {
                "or": {
                    "urn:li:adTargetingFacet:functions": [
                        "urn:li:function:3",   # Marketing
                        "urn:li:function:11",  # Sales
                        "urn:li:function:25"   # IT
                    ]
                }
            }
        ]
    }
}
```

### Seniority Levels
```python
targeting = {
    "include": {
        "and": [
            {
                "or": {
                    "urn:li:adTargetingFacet:seniorities": [
                        "urn:li:seniority:7",  # Director
                        "urn:li:seniority:8",  # VP
                        "urn:li:seniority:9",  # CXO
                        "urn:li:seniority:10"  # Owner/Partner
                    ]
                }
            }
        ]
    }
}
```

## Company Targeting

### Company Names
```python
targeting = {
    "include": {
        "and": [
            {
                "or": {
                    "urn:li:adTargetingFacet:companies": [
                        "urn:li:company:1441",    # Google
                        "urn:li:company:1035",    # Microsoft
                        "urn:li:company:2382910"  # Amazon
                    ]
                }
            }
        ]
    }
}
```

### Company Size
```python
targeting = {
    "include": {
        "and": [
            {
                "or": {
                    "urn:li:adTargetingFacet:staffCountRanges": [
                        "urn:li:staffCountRange:D",  # 51-200
                        "urn:li:staffCountRange:E",  # 201-500
                        "urn:li:staffCountRange:F"   # 501-1000
                    ]
                }
            }
        ]
    }
}
```

### Industries
```python
targeting = {
    "include": {
        "and": [
            {
                "or": {
                    "urn:li:adTargetingFacet:industries": [
                        "urn:li:industry:4",   # Computer Software
                        "urn:li:industry:6",   # Internet
                        "urn:li:industry:96"   # Information Technology
                    ]
                }
            }
        ]
    }
}
```

## Matched Audiences

### Upload Company List
```python
url = "https://api.linkedin.com/rest/dmpSegments"

data = {
    "account": f"urn:li:sponsoredAccount:{account_id}",
    "name": "Target Companies Q2",
    "type": "COMPANY",
    "matchType": "COMPANY_NAME"
}

response = requests.post(url, headers=headers, json=data)
segment_id = response.json()["id"]

# Upload companies
upload_url = f"https://api.linkedin.com/rest/dmpSegments/{segment_id}/uploads"
companies = ["Google", "Microsoft", "Amazon"]

upload_data = {
    "companies": companies
}

requests.post(upload_url, headers=headers, json=upload_data)
```

### Contact List Audience
```python
data = {
    "account": f"urn:li:sponsoredAccount:{account_id}",
    "name": "Customer Email List",
    "type": "USER",
    "matchType": "EMAIL"
}

# Upload hashed emails
import hashlib

emails = ["user1@example.com", "user2@example.com"]
hashed_emails = [hashlib.sha256(email.lower().encode()).hexdigest() for email in emails]
```

## Lookalike Audiences

### Create Lookalike
```python
url = "https://api.linkedin.com/rest/dmpSegments"

data = {
    "account": f"urn:li:sponsoredAccount:{account_id}",
    "name": "Lookalike - Customers",
    "type": "LOOKALIKE",
    "sourceSegment": source_segment_id,
    "expansionTier": "BALANCED"  # NARROW, BALANCED, BROAD
}

response = requests.post(url, headers=headers, json=data)
```

## Campaign Analytics

### Get Campaign Stats
```python
url = "https://api.linkedin.com/rest/adAnalytics"

params = {
    "q": "analytics",
    "pivot": "CAMPAIGN",
    "dateRange.start.day": 1,
    "dateRange.start.month": 3,
    "dateRange.start.year": 2026,
    "dateRange.end.day": 31,
    "dateRange.end.month": 3,
    "dateRange.end.year": 2026,
    "campaigns[0]": campaign_id,
    "fields": "impressions,clicks,costInLocalCurrency,externalWebsiteConversions"
}

response = requests.get(url, headers=headers, params=params)
stats = response.json()
```

### Available Metrics
- impressions
- clicks
- costInLocalCurrency
- externalWebsiteConversions
- leadGenerationMailContactInfoShares
- videoViews
- videoCompletions
- reactions
- comments
- shares
- follows

## Performance Benchmarks

| Metric | Good | Average | Poor |
|--------|------|---------|------|
| **CTR** | >0.5% | 0.3-0.5% | <0.3% |
| **CPC** | <$5 | $5-$10 | >$10 |
| **Conversion Rate** | >2% | 1-2% | <1% |

## Using the Reference Files

**`/references/linkedin-targeting-reference.md`** — Read for complete targeting options, job title IDs, company IDs, and targeting combinations.

**`/references/linkedin-analytics-guide.md`** — Read for analytics API documentation, metric definitions, and reporting best practices.

**`/references/linkedin-audience-strategies.md`** — Read for B2B audience building, account-based marketing tactics, and optimization strategies.
