---
name: google-analytics-4
description: "Implement and analyze Google Analytics 4 (GA4) for comprehensive web and app analytics. Use for: event-based tracking setup, cross-platform measurement, conversion tracking, audience segmentation, predictive insights, e-commerce analytics, custom event configuration, BigQuery integration, privacy-compliant data collection, migration from Universal Analytics, GA4 property setup, enhanced measurement configuration, and data-driven attribution modeling."
---

# Google Analytics 4

Implement event-based analytics for websites and mobile apps using Google's latest analytics platform.

## Overview

Google Analytics 4 (GA4) represents a fundamental shift from session-based to event-based data collection, enabling unified tracking across web and mobile platforms. GA4 leverages machine learning for predictive insights, offers enhanced privacy controls, and provides deeper integration with Google Ads and BigQuery. This skill covers implementation, configuration, analysis, and optimization of GA4 properties.

## Core Features and Capabilities

### Event-Based Data Model

GA4 tracks every user interaction as a standalone event, providing granular insight into customer journeys:

- **Automatic Events**: Page views, scrolls, outbound clicks, site searches, video engagement, file downloads, form interactions
- **Enhanced Measurement**: Automatically tracks common interactions without manual code changes
- **Custom Events**: Define business-specific events with parameters for detailed tracking
- **Conversion Events**: Mark critical events as conversions for optimization and reporting

### Cross-Platform Tracking

- **Unified Properties**: Combine web and app data in a single property
- **User-Centric Measurement**: Track users across devices and platforms
- **Data Streams**: Configure separate streams for web, iOS, and Android
- **Cross-Domain Tracking**: Measure user journeys across multiple domains

### AI-Powered Insights

- **Predictive Metrics**: Churn probability, purchase likelihood, revenue prediction
- **Automated Insights**: AI identifies trends and anomalies automatically
- **Smart Goals**: Machine learning optimizes for high-value conversions
- **Anomaly Detection**: Alerts for unusual traffic patterns or metric changes

## Implementation Methods

### Setup Process

1. **Create GA4 Property**
   - Navigate to Admin > Create Property
   - Configure property name, time zone, currency, industry, business size
   - Accept terms and conditions

2. **Configure Data Streams**
   - Add Web stream: Enter website URL, enable enhanced measurement
   - Add iOS/Android streams: Connect Firebase project, install SDK
   - Configure stream settings: measurement protocol, data retention, user-ID tracking

3. **Install Tracking Code**

| Method | Use Case | Implementation |
|--------|----------|----------------|
| Google Tag Manager | Recommended for flexibility | Create GA4 Configuration tag, add Measurement ID, fire on all pages |
| Global Site Tag (gtag.js) | Direct implementation | Paste gtag.js code after `<head>` tag |
| CMS Integration | WordPress, Wix, Shopify | Enter Measurement ID in platform settings |
| Firebase SDK | Mobile apps | Connect Firebase project to GA4 property |

### Event Configuration

**Standard Event Structure**:
```
Event Name: purchase
Parameters:
  - transaction_id: "T12345"
  - value: 99.99
  - currency: "USD"
  - items: [{item_id: "SKU123", item_name: "Product"}]
```

**Custom Event Creation**:
- Navigate to Configure > Events > Create Event
- Define event name and matching conditions
- Add or modify parameters
- Mark as conversion if applicable

### Conversion Tracking

- **Mark Events as Conversions**: Configure > Events > Toggle "Mark as conversion"
- **Import from Google Ads**: Link accounts to share conversion data
- **Attribution Models**: Data-driven, last-click, first-click, linear, time-decay, position-based
- **Conversion Paths**: Analyze multi-touch attribution in Advertising section

## Analysis and Reporting

### Report Structure

**Life Cycle Reports**:
- **Acquisition**: User and traffic acquisition, channel performance
- **Engagement**: Events, conversions, pages/screens, landing pages
- **Monetization**: E-commerce purchases, revenue, in-app purchases
- **Retention**: User retention, cohort analysis, lifetime value

**User Reports**:
- **Demographics**: Age, gender, interests, language
- **Tech**: Device category, operating system, browser, screen resolution
- **User Attributes**: Custom dimensions and user properties

### Exploration Analysis

| Technique | Purpose | Use Case |
|-----------|---------|----------|
| Free-Form | Custom data exploration | Ad-hoc analysis with dimensions and metrics |
| Funnel | Conversion path analysis | Checkout process optimization |
| Path Exploration | User journey mapping | Identify common navigation patterns |
| Segment Overlap | Audience comparison | Find overlapping user segments |
| Cohort | Retention analysis | Track user behavior over time |
| User Lifetime | LTV calculation | Predict customer value |

### Audience Building

- **Predictive Audiences**: Likely to purchase, likely to churn (7-day prediction)
- **Custom Audiences**: Define based on events, parameters, user properties
- **Suggested Audiences**: Pre-built segments (purchasers, engaged users, new users)
- **Export to Google Ads**: Use audiences for remarketing and optimization

## Privacy and Compliance

### Privacy Features

- **Consent Mode**: Adjust tracking based on user consent choices
- **Data Modeling**: Fill gaps in observed data when consent is not given
- **IP Anonymization**: GA4 does not log IP addresses by default
- **Data Retention**: Configure retention period (2-14 months)
- **Data Deletion**: Request user data deletion for GDPR compliance
- **Geographic Restrictions**: Exclude data collection from specific regions

### Data Controls

- **User-ID Tracking**: Enable for cross-device measurement
- **Google Signals**: Collect data from signed-in Google users
- **Advertising Features**: Control remarketing and advertising reporting
- **Data Sharing Settings**: Configure sharing with Google products and services

## Integration and Advanced Features

### BigQuery Export

- **Free Integration**: Export raw event data to BigQuery daily
- **Streaming Export**: Real-time data export (requires BigQuery subscription)
- **Custom Analysis**: SQL queries for advanced segmentation and modeling
- **Machine Learning**: Build predictive models on raw GA4 data

### Google Ads Integration

- **Conversion Import**: Share GA4 conversions with Google Ads
- **Audience Sharing**: Export audiences for remarketing campaigns
- **Attribution Comparison**: Compare GA4 and Google Ads attribution
- **Campaign Tagging**: UTM parameters for campaign tracking

### Measurement Protocol

- **Server-Side Tracking**: Send events directly to GA4 from servers
- **Offline Conversions**: Import offline events (phone orders, in-store purchases)
- **Custom Implementations**: Track events from IoT devices or custom applications

## Migration from Universal Analytics

### Key Differences

| Universal Analytics | Google Analytics 4 |
|---------------------|--------------------|
| Session-based | Event-based |
| Pageviews as primary metric | Events as primary metric |
| Views and filters | Data streams and comparisons |
| Goals (20 max) | Conversions (30 max) |
| E-commerce tracking | Enhanced e-commerce events |
| Custom dimensions/metrics | Event parameters and user properties |

### Migration Strategy

1. **Dual Tracking**: Run GA4 alongside Universal Analytics during transition
2. **Event Mapping**: Map UA goals and events to GA4 events
3. **Custom Dimension Migration**: Convert to event parameters or user properties
4. **Historical Data**: Export UA data before sunset (no automatic migration)
5. **Report Recreation**: Rebuild custom reports and dashboards in GA4
6. **Team Training**: Educate stakeholders on new interface and metrics

## Performance Optimization

### Data Quality

- **Debug View**: Real-time event validation during implementation
- **Data Filters**: Exclude internal traffic, developer traffic, unwanted referrals
- **Event Naming**: Use consistent, descriptive naming conventions
- **Parameter Limits**: Max 25 parameters per event, 100 characters per parameter value

### Reporting Performance

- **Sampling**: Understand when reports use sampled data (>10M events)
- **Exploration Limits**: 10 explorations per property, 200 rows per exploration
- **Custom Dimensions**: Limit to 50 event-scoped, 25 user-scoped dimensions
- **Cardinality**: Avoid high-cardinality dimensions (>500 unique values)

## Troubleshooting Common Issues

### Data Collection Issues

- **No Data Appearing**: Verify Measurement ID, check tag firing in Tag Assistant
- **Duplicate Events**: Check for multiple GA4 tags firing on same page
- **Missing Events**: Verify enhanced measurement settings, check event parameters
- **Cross-Domain Tracking**: Configure linker parameters in gtag.js or GTM

### Reporting Discrepancies

- **Google Ads vs. GA4**: Different attribution windows and models
- **Real-Time vs. Standard Reports**: Real-time data may differ from processed data
- **Session Differences**: GA4 sessions reset at midnight, UA sessions do not
- **User Counts**: GA4 uses different user identification methodology

## Using the Reference Files

### When to Read Each Reference

**`/references/event-tracking-guide.md`** — Read when implementing custom events, configuring e-commerce tracking, or setting up conversion events with parameters.

**`/references/exploration-techniques.md`** — Read when performing advanced analysis, building custom funnels, analyzing user paths, or creating cohort reports.

**`/references/bigquery-integration.md`** — Read when exporting raw data to BigQuery, writing SQL queries for custom analysis, or building machine learning models on GA4 data.

**`/references/migration-checklist.md`** — Read when migrating from Universal Analytics, mapping UA events to GA4, or planning dual-tracking implementation.
