---
name: twitch-ads-api-integration
description: "Integrate with Twitch advertising APIs for programmatic campaign management and automation. Access Twitch API endpoints for ad scheduling, Amazon Ads API for campaign data, and Content Transparency Reports. Use for: automating Twitch ad operations, building custom reporting dashboards, integrating Twitch ads with marketing platforms, programmatic campaign management, real-time ad scheduling via API, and developing agentic AI advertising automation for Twitch campaigns."
---

# Twitch Ads API Integration

Programmatic access to Twitch advertising through Twitch API and Amazon Ads API for automated campaign management and reporting.

## Overview

Twitch advertising API access is split between Twitch's own API (for limited ad operations) and Amazon Ads API (for comprehensive campaign management). The Twitch API provides endpoints for starting commercials, checking ad schedules, and snoozing ads. Amazon Ads API offers full campaign management, reporting, and optimization capabilities for Twitch inventory.

**Key Capabilities:**
- Start commercials programmatically (Twitch API)
- Retrieve ad schedules and snooze information
- Create and manage campaigns via Amazon DSP API
- Access performance data and reporting
- Automate bid adjustments and budget management
- Retrieve Content Transparency Reports
- Integrate with marketing automation platforms

## Twitch API Ad Endpoints

### Start Commercial

**Endpoint:** `POST https://api.twitch.tv/helix/channels/commercial`

**Authentication:** User access token with `channel:edit:commercial` scope

**Request Body:**
```json
{
  "broadcaster_id": "141981764",
  "length": 60
}
```

**Parameters:**
- `broadcaster_id` (string, required): Channel ID to run commercial
- `length` (integer, required): Commercial length in seconds (max 180)

**Response:**
```json
{
  "data": [{
    "length": 60,
    "message": "",
    "retry_after": 480
  }]
}
```

**Use Cases:**
- Automated ad break scheduling
- Integration with stream management tools
- Programmatic commercial triggers
- Revenue optimization automation

**Limitations:**
- Only partners and affiliates can run commercials
- Must be streaming live
- Only broadcaster can start (not editors/moderators)
- Cooldown period between commercials (`retry_after` seconds)

Read `/references/twitch-api-endpoints.md` for complete endpoint documentation.

## Amazon Ads API Integration

### API Access

**Requirements:**
- Amazon Ads account
- API access approval
- OAuth 2.0 credentials
- Programmatic access tier

**Authentication:**
- OAuth 2.0 authorization code flow
- Access tokens expire (refresh required)
- Scope-based permissions
- Secure credential storage

### Campaign Management Endpoints

**Create Campaign:**
- POST to campaign creation endpoint
- Define objectives, budget, dates
- Set targeting parameters
- Configure bid strategy

**Update Campaign:**
- PATCH existing campaigns
- Modify budgets, bids, targeting
- Pause/resume campaigns
- Adjust pacing and scheduling

**Retrieve Campaign Data:**
- GET campaign performance
- Filter by date range, status
- Paginated results
- Real-time and historical data

Read `/references/amazon-ads-api-guide.md` for detailed API documentation.

## Reporting & Analytics APIs

### Performance Data Retrieval

**Metrics Available:**
- Impressions, clicks, conversions
- Spend, CPM, CPC, CPA
- ROAS, revenue
- Video completion rates
- Engagement metrics

**Dimensions:**
- Campaign, ad group, creative
- Time period (hourly, daily, weekly)
- Device, placement, geography
- Audience segment

**Report Types:**
- Real-time performance
- Historical analysis
- Custom date ranges
- Scheduled automated reports

### Content Transparency API

**Access Method:**
- Amazon Ads API
- ADSP downloadable reports
- Audio and Video dimension

**Data Retrieved:**
- Content type (game category, etc.)
- Content rating
- Specific stream titles
- Impression volume by content

**Use Cases:**
- Brand safety verification
- Performance by content type
- Contextual targeting optimization
- Compliance reporting

Read `/references/reporting-api-integration.md` for API reporting details.

## Automation Strategies

### Bid Management Automation

**Rule-Based Bidding:**
- Monitor ROAS by segment
- Automatically adjust bids based on performance
- Implement time-based bid adjustments
- Scale winning segments

**Example Logic:**
```python
if segment_roas > target_roas * 1.2:
    increase_bid(segment_id, 0.20)  # +20%
elif segment_roas < target_roas * 0.8:
    decrease_bid(segment_id, 0.20)  # -20%
```

### Budget Optimization

**Automated Reallocation:**
- Shift budget from low to high ROAS campaigns
- Pause underperformers automatically
- Scale winners within constraints
- Maintain overall budget limits

**Pacing Control:**
- Monitor daily spend vs. target
- Adjust bids to control pacing
- Prevent early budget depletion
- Maximize delivery within budget

### Creative Rotation

**Performance-Based Rotation:**
- Track CTR and VCR by creative
- Automatically pause fatigued creatives
- Increase budget to top performers
- Trigger creative refresh alerts

Read `/references/automation-examples.md` for implementation code samples.

## Integration Patterns

### Marketing Platform Integration

**Connect Twitch Ads Data to:**
- Google Analytics (via UTM parameters)
- CRM systems (Salesforce, HubSpot)
- Data warehouses (BigQuery, Snowflake)
- BI tools (Tableau, Power BI, Looker)

**Data Flow:**
1. Retrieve performance data via API
2. Transform and normalize data
3. Load into destination system
4. Enable cross-channel analysis

### Real-Time Dashboards

**Build Custom Dashboards:**
- Pull live performance data
- Visualize KPIs in real-time
- Alert on anomalies
- Enable quick decision-making

**Tech Stack Examples:**
- Python + Plotly/Dash
- React + D3.js
- Tableau with API connector
- Power BI with custom connector

### Agentic AI Automation

**AI-Driven Campaign Management:**
- Machine learning for bid optimization
- Predictive budget allocation
- Automated A/B testing
- Natural language campaign creation

**Implementation Approach:**
- Train models on historical performance
- Define optimization objectives
- Implement automated decision-making
- Monitor and refine AI performance

Read `/references/integration-architecture.md` for system design patterns.

## Using the Reference Files

### When to Read Each Reference

**`/references/twitch-api-endpoints.md`** — Read when implementing Twitch API endpoints for ad scheduling, retrieving ad schedules, or snoozing ads programmatically.

**`/references/amazon-ads-api-guide.md`** — Read when integrating with Amazon Ads API for campaign management, bid adjustments, or accessing Twitch advertising inventory programmatically.

**`/references/reporting-api-integration.md`** — Read when building custom reporting solutions, retrieving performance data, or accessing Content Transparency Reports via API.

**`/references/automation-examples.md`** — Read when implementing automated bid management, budget optimization, or building agentic AI systems for Twitch advertising.

**`/references/integration-architecture.md`** — Read when designing system architecture for Twitch ads integration with marketing platforms, data warehouses, or custom dashboards.

## References

- [Amazon Ads Api Guide](references/amazon-ads-api-guide.md)
- [Automation Examples](references/automation-examples.md)
- [Twitch Api Endpoints](references/twitch-api-endpoints.md)
