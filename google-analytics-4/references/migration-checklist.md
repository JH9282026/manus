# Migration Checklist: Universal Analytics to Google Analytics 4

Comprehensive guide for transitioning from UA to GA4.

## Pre-Migration Planning

### Assessment Phase

**1. Audit Current UA Implementation**
- Document all tracked events and goals
- List custom dimensions and metrics
- Identify e-commerce tracking setup
- Review custom reports and dashboards
- Note integrations (Google Ads, Search Console, etc.)
- Export historical data for archival

**2. Stakeholder Alignment**
- Identify key stakeholders and users
- Document critical reports and metrics
- Set migration timeline and milestones
- Plan training sessions for team
- Establish success criteria

**3. Technical Requirements**
- Verify website/app access for implementation
- Confirm Google Tag Manager availability
- Check developer resources for custom events
- Assess need for server-side tracking
- Plan for testing environment

## GA4 Property Setup

### Initial Configuration

**1. Create GA4 Property**
```
Admin > Create Property
- Property name: [Your Site] - GA4
- Time zone: [Match UA property]
- Currency: [Match UA property]
- Industry: [Select appropriate]
- Business size: [Select appropriate]
```

**2. Configure Data Streams**

Web Stream:
- URL: https://yoursite.com
- Stream name: Web Data Stream
- Enhanced measurement: Enable all
- Measurement ID: G-XXXXXXXXXX

iOS/Android Streams (if applicable):
- Connect Firebase project
- Configure app details
- Install Firebase SDK

**3. Property Settings**
- Data retention: Set to maximum (14 months)
- Google Signals: Enable for cross-device tracking
- User-ID: Configure if using custom user identification
- Data filters: Set up internal traffic filter

## Event Mapping

### UA Goals to GA4 Conversions

| UA Goal Type | UA Configuration | GA4 Equivalent | GA4 Implementation |
|--------------|------------------|----------------|--------------------|
| Destination | /thank-you | page_view with page_location parameter | Mark page_view as conversion with filter |
| Duration | Session > 3 min | engagement_time_msec > 180000 | Create custom event, mark as conversion |
| Pages/Session | Pages > 5 | page_view count > 5 | Create custom event based on page_view count |
| Event | Category/Action/Label | Custom event | Map to GA4 event with parameters |

### UA Events to GA4 Events

**UA Event Structure**:
```javascript
ga('send', 'event', 'Category', 'Action', 'Label', Value);
```

**GA4 Event Structure**:
```javascript
gtag('event', 'action_name', {
  'event_category': 'Category',
  'event_label': 'Label',
  'value': Value
});
```

**Common Event Mappings**:

| UA Event | GA4 Event | Notes |
|----------|-----------|-------|
| Category: Video, Action: Play | video_start | Use recommended event |
| Category: Form, Action: Submit | form_submit | Use recommended event |
| Category: Download, Action: PDF | file_download | Auto-tracked with enhanced measurement |
| Category: Outbound, Action: Click | click | Auto-tracked with enhanced measurement |
| Category: Ecommerce, Action: Purchase | purchase | Use recommended e-commerce event |

### Custom Dimensions and Metrics

**UA Custom Dimensions** → **GA4 Event Parameters or User Properties**

| UA Custom Dimension | Scope | GA4 Equivalent | Implementation |
|---------------------|-------|----------------|----------------|
| User Type | User | User property: user_type | Set user property |
| Content Category | Hit | Event parameter: content_category | Add to relevant events |
| Author | Hit | Event parameter: author | Add to page_view events |
| Membership Level | User | User property: membership_level | Set user property |

**UA Custom Metrics** → **GA4 Event Parameters**

| UA Custom Metric | GA4 Equivalent | Implementation |
|------------------|----------------|----------------|
| Article Word Count | Event parameter: word_count | Add to page_view or custom event |
| Video Duration | Event parameter: video_duration | Add to video events |
| Product Rating | Event parameter: product_rating | Add to view_item events |

## Implementation

### Dual Tagging Strategy

Run UA and GA4 simultaneously during transition period (recommended 3-6 months).

**Option 1: Separate Tags**
```html
<!-- Universal Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-XXXXXXXXX-X"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'UA-XXXXXXXXX-X');
</script>

<!-- Google Analytics 4 -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

**Option 2: Google Tag Manager (Recommended)**

1. Create GA4 Configuration Tag
   - Tag Type: Google Analytics: GA4 Configuration
   - Measurement ID: G-XXXXXXXXXX
   - Trigger: All Pages

2. Keep existing UA Pageview Tag
   - Tag Type: Universal Analytics
   - Track Type: Pageview
   - Trigger: All Pages

3. Duplicate UA Event Tags for GA4
   - Create GA4 Event tag for each UA event
   - Map parameters appropriately
   - Use same triggers

### E-commerce Migration

**UA Enhanced Ecommerce** → **GA4 E-commerce Events**

```javascript
// UA: Product Impression
ga('ec:addImpression', {
  'id': 'P12345',
  'name': 'Product Name',
  'category': 'Apparel',
  'brand': 'Brand',
  'variant': 'Blue',
  'list': 'Search Results',
  'position': 1,
  'price': '29.99'
});

// GA4: view_item_list
gtag('event', 'view_item_list', {
  item_list_id: 'search_results',
  item_list_name: 'Search Results',
  items: [{
    item_id: 'P12345',
    item_name: 'Product Name',
    item_category: 'Apparel',
    item_brand: 'Brand',
    item_variant: 'Blue',
    price: 29.99,
    index: 1
  }]
});
```

```javascript
// UA: Product Click
ga('ec:addProduct', {
  'id': 'P12345',
  'name': 'Product Name'
});
ga('ec:setAction', 'click', {list: 'Search Results'});

// GA4: select_item
gtag('event', 'select_item', {
  item_list_id: 'search_results',
  item_list_name: 'Search Results',
  items: [{
    item_id: 'P12345',
    item_name: 'Product Name'
  }]
});
```

```javascript
// UA: Purchase
ga('ec:addProduct', {
  'id': 'P12345',
  'name': 'Product Name',
  'price': '29.99',
  'quantity': 1
});
ga('ec:setAction', 'purchase', {
  'id': 'T12345',
  'revenue': '29.99',
  'tax': '2.00',
  'shipping': '5.00'
});

// GA4: purchase
gtag('event', 'purchase', {
  transaction_id: 'T12345',
  value: 29.99,
  tax: 2.00,
  shipping: 5.00,
  currency: 'USD',
  items: [{
    item_id: 'P12345',
    item_name: 'Product Name',
    price: 29.99,
    quantity: 1
  }]
});
```

## Testing and Validation

### Pre-Launch Testing

**1. Debug View Validation**
- Enable debug mode (Chrome extension or debug_mode parameter)
- Navigate to Configure > DebugView
- Perform key user actions
- Verify events fire with correct parameters
- Check user properties are set correctly

**2. Real-Time Reports**
- Navigate to Reports > Realtime
- Perform test transactions
- Verify events appear in real-time
- Check conversion events are tracked

**3. Comparison Testing**
- Run UA and GA4 simultaneously for 1-2 weeks
- Compare key metrics:
  - Users (expect slight differences due to methodology)
  - Sessions (GA4 may show fewer due to midnight reset)
  - Pageviews (should be similar)
  - Events (GA4 will show more due to auto-tracking)
  - Conversions (should match goal completions)

### Common Discrepancies

| Metric | Expected Difference | Reason |
|--------|---------------------|--------|
| Users | GA4 may be 5-10% lower | Different user identification methodology |
| Sessions | GA4 may be 10-15% lower | Sessions reset at midnight in GA4 |
| Bounce Rate | Not directly comparable | GA4 uses engagement rate instead |
| Pageviews | Should be similar | May differ if SPA tracking differs |
| Events | GA4 will be higher | Auto-tracked events included |

## Report Recreation

### Standard Reports Mapping

| UA Report | GA4 Equivalent | Location |
|-----------|----------------|----------|
| Audience > Overview | User attributes | Reports > User > Overview |
| Acquisition > All Traffic | Traffic acquisition | Reports > Acquisition > Traffic acquisition |
| Behavior > Site Content | Pages and screens | Reports > Engagement > Pages and screens |
| Conversions > Goals | Conversions | Reports > Engagement > Conversions |
| Ecommerce > Overview | Monetization overview | Reports > Monetization > Overview |

### Custom Report Migration

**UA Custom Report** → **GA4 Exploration**

1. Identify dimensions and metrics in UA report
2. Create new Exploration in GA4
3. Add equivalent dimensions and metrics
4. Apply filters and segments
5. Choose appropriate visualization
6. Save and share with team

**Example: Content Performance Report**

UA Custom Report:
- Dimensions: Page, Page Title
- Metrics: Pageviews, Unique Pageviews, Avg. Time on Page, Bounce Rate

GA4 Exploration:
- Technique: Free-form
- Dimensions: Page path and screen class, Page title and screen name
- Metrics: Views, Users, Average engagement time, Engagement rate
- Visualization: Table

## Integration Migration

### Google Ads

**1. Link GA4 to Google Ads**
- Admin > Product Links > Google Ads Links
- Select Google Ads account
- Enable auto-tagging
- Import conversions

**2. Conversion Import**
- Mark GA4 events as conversions
- In Google Ads: Tools > Conversions > New Conversion
- Select Import > Google Analytics 4
- Choose conversions to import

**3. Audience Sharing**
- Create audiences in GA4
- Enable audience sharing in property settings
- Audiences appear in Google Ads within 24-48 hours

### Google Search Console

- Admin > Product Links > Search Console Links
- Select Search Console property
- Choose web stream
- Confirm linking

### BigQuery

- Admin > Product Links > BigQuery Links
- Select or create BigQuery project
- Enable daily export (free)
- Optionally enable streaming export

## Data Archival

### Export UA Data

**1. Standard Reports**
- Export key reports to Google Sheets or CSV
- Save monthly/quarterly snapshots
- Document metric definitions

**2. Custom Reports**
- Export all custom reports
- Save report configurations
- Document filters and segments

**3. BigQuery Export (GA360 only)**
- Ensure historical data is exported
- Verify export completeness
- Document schema and table structure

**4. API Export**
Use Google Analytics Reporting API to extract historical data:
```python
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import RunReportRequest

client = BetaAnalyticsDataClient()

request = RunReportRequest(
    property=f"properties/UA-PROPERTY-ID",
    dimensions=[{"name": "date"}, {"name": "pagePath"}],
    metrics=[{"name": "screenPageViews"}, {"name": "sessions"}],
    date_ranges=[{"start_date": "2020-01-01", "end_date": "2026-03-15"}],
)

response = client.run_report(request)
# Process and save response
```

## Training and Documentation

### Team Training Plan

**Week 1: Introduction**
- GA4 overview and key differences from UA
- New interface navigation
- Event-based model explanation

**Week 2: Reporting**
- Standard reports walkthrough
- Exploration techniques
- Custom report creation

**Week 3: Analysis**
- Audience building
- Conversion tracking
- Attribution analysis

**Week 4: Advanced Features**
- BigQuery integration
- Predictive metrics
- Debug View and troubleshooting

### Documentation Checklist

- [ ] Event naming conventions
- [ ] Custom parameter definitions
- [ ] User property documentation
- [ ] Conversion event list
- [ ] Audience definitions
- [ ] Report access and permissions
- [ ] Troubleshooting guide
- [ ] FAQ for common questions

## Post-Migration

### Monitoring Phase (First 30 Days)

**Week 1**
- Daily data quality checks
- Verify all events firing correctly
- Monitor conversion tracking
- Address any implementation issues

**Week 2-4**
- Compare GA4 vs UA metrics
- Validate custom events and parameters
- Test audience creation and export
- Gather user feedback

**Month 2-3**
- Optimize event tracking based on insights
- Create additional custom reports
- Expand BigQuery analysis
- Train additional team members

### Optimization Opportunities

**1. Enhanced Tracking**
- Implement scroll depth tracking
- Add video engagement events
- Track form field interactions
- Measure content engagement

**2. Advanced Analysis**
- Build predictive audiences
- Create custom funnels
- Analyze user paths
- Implement cohort analysis

**3. Integration Expansion**
- Connect additional Google products
- Set up Data Studio dashboards
- Implement server-side tracking
- Explore Firebase integration

## Migration Timeline

### Recommended 12-Week Plan

**Weeks 1-2: Planning**
- Audit UA implementation
- Document requirements
- Create migration plan
- Assign responsibilities

**Weeks 3-4: Setup**
- Create GA4 property
- Configure data streams
- Set up basic tracking
- Implement dual tagging

**Weeks 5-6: Event Migration**
- Map UA events to GA4
- Implement custom events
- Configure conversions
- Set up e-commerce tracking

**Weeks 7-8: Testing**
- Debug View validation
- Comparison testing
- Fix implementation issues
- Validate data quality

**Weeks 9-10: Reporting**
- Recreate custom reports
- Build explorations
- Create audiences
- Set up integrations

**Weeks 11-12: Training & Launch**
- Conduct team training
- Create documentation
- Monitor data quality
- Gather feedback

## Troubleshooting Common Issues

### Data Collection Issues

**Problem**: No data appearing in GA4
- Verify Measurement ID is correct
- Check tag firing in GTM Preview or browser console
- Ensure data stream is active
- Check for ad blockers or privacy extensions

**Problem**: Events not firing
- Verify event name and parameters in Debug View
- Check trigger conditions in GTM
- Ensure GA4 Configuration tag loads first
- Review JavaScript console for errors

**Problem**: Duplicate events
- Check for multiple GA4 tags on page
- Verify not sending from both gtag.js and GTM
- Review trigger conditions for overlaps

### Reporting Discrepancies

**Problem**: User counts don't match UA
- Expected due to different methodology
- GA4 uses more sophisticated user identification
- Consider 5-10% variance normal

**Problem**: Session counts lower in GA4
- GA4 sessions reset at midnight
- UA sessions can span midnight
- Expected difference of 10-15%

**Problem**: Conversion counts don't match goals
- Verify event is marked as conversion
- Check conversion event parameters
- Ensure transaction_id prevents duplicates
- Allow 24-48 hours for processing

## Success Criteria

### Migration Complete When:

- [ ] All critical events tracking correctly
- [ ] Conversion events validated and matching expectations
- [ ] Key reports recreated in GA4
- [ ] Team trained on GA4 interface and reporting
- [ ] Integrations (Google Ads, Search Console) configured
- [ ] Data quality validated for 30+ days
- [ ] Documentation complete and accessible
- [ ] Stakeholders comfortable with GA4 data
- [ ] UA property archived with historical data exported
- [ ] Monitoring and optimization plan in place
