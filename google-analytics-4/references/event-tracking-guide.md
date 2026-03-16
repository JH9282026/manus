# Event Tracking Guide for Google Analytics 4

Comprehensive guide to implementing and managing events in GA4.

## Event Structure and Naming

### Event Anatomy

Every GA4 event consists of:
- **Event Name**: Descriptive identifier (e.g., `purchase`, `sign_up`, `video_play`)
- **Event Parameters**: Key-value pairs providing context (e.g., `currency: USD`, `value: 99.99`)
- **User Properties**: Persistent attributes about the user (e.g., `user_type: premium`)
- **Timestamp**: Automatically captured event time

### Naming Conventions

**Best Practices**:
- Use lowercase with underscores: `add_to_cart` (not `AddToCart` or `add-to-cart`)
- Be descriptive but concise: `video_complete` (not `v_c` or `user_completed_watching_video`)
- Avoid reserved prefixes: Don't start with `firebase_`, `ga_`, or `google_`
- Maximum 40 characters for event names
- Use consistent naming across platforms (web and app)

**Event Name Examples**:
```
Good: purchase, sign_up, video_start, form_submit, search
Bad: Purchase, signUp, video-start, formSubmit, srch
```

## Automatically Collected Events

### Enhanced Measurement Events

Enabled by default in web data streams:

1. **page_view**: Fires when page loads or browser history changes
2. **scroll**: Fires when user scrolls to 90% of page depth
3. **click**: Fires on outbound link clicks
4. **view_search_results**: Fires when URL contains search parameters
5. **video_start, video_progress, video_complete**: YouTube embedded video tracking
6. **file_download**: Fires on PDF, XLSX, DOCX, TXT, etc. downloads
7. **form_start, form_submit**: Fires on form interactions (2026 feature)

### Mobile App Events

Automatically collected via Firebase SDK:
- `first_open`: First time app is launched
- `session_start`: New session begins
- `app_update`: App is updated to new version
- `app_remove`: App is uninstalled
- `os_update`: Device OS is updated

## Recommended Events

GA4 provides predefined event names with standard parameters for common use cases.

### E-commerce Events

**1. view_item_list**
```javascript
gtag('event', 'view_item_list', {
  item_list_id: 'related_products',
  item_list_name: 'Related Products',
  items: [
    {
      item_id: 'SKU_12345',
      item_name: 'Triblend Android T-Shirt',
      item_category: 'Apparel',
      item_variant: 'Gray',
      price: 29.99,
      quantity: 1
    }
  ]
});
```

**2. select_item**
```javascript
gtag('event', 'select_item', {
  item_list_id: 'related_products',
  items: [{
    item_id: 'SKU_12345',
    item_name: 'Triblend Android T-Shirt'
  }]
});
```

**3. view_item**
```javascript
gtag('event', 'view_item', {
  currency: 'USD',
  value: 29.99,
  items: [{
    item_id: 'SKU_12345',
    item_name: 'Triblend Android T-Shirt',
    item_brand: 'Google',
    item_category: 'Apparel',
    item_variant: 'Gray',
    price: 29.99
  }]
});
```

**4. add_to_cart**
```javascript
gtag('event', 'add_to_cart', {
  currency: 'USD',
  value: 29.99,
  items: [{
    item_id: 'SKU_12345',
    item_name: 'Triblend Android T-Shirt',
    price: 29.99,
    quantity: 1
  }]
});
```

**5. remove_from_cart**
```javascript
gtag('event', 'remove_from_cart', {
  currency: 'USD',
  value: 29.99,
  items: [{
    item_id: 'SKU_12345',
    quantity: 1
  }]
});
```

**6. begin_checkout**
```javascript
gtag('event', 'begin_checkout', {
  currency: 'USD',
  value: 59.98,
  items: [
    {
      item_id: 'SKU_12345',
      item_name: 'Triblend Android T-Shirt',
      price: 29.99,
      quantity: 2
    }
  ]
});
```

**7. add_payment_info**
```javascript
gtag('event', 'add_payment_info', {
  currency: 'USD',
  value: 59.98,
  payment_type: 'Credit Card',
  items: [/* item array */]
});
```

**8. add_shipping_info**
```javascript
gtag('event', 'add_shipping_info', {
  currency: 'USD',
  value: 59.98,
  shipping_tier: 'Ground',
  items: [/* item array */]
});
```

**9. purchase**
```javascript
gtag('event', 'purchase', {
  transaction_id: 'T_12345',
  value: 64.98,
  tax: 4.00,
  shipping: 5.00,
  currency: 'USD',
  coupon: 'SUMMER_SALE',
  items: [
    {
      item_id: 'SKU_12345',
      item_name: 'Triblend Android T-Shirt',
      item_category: 'Apparel',
      price: 29.99,
      quantity: 2
    }
  ]
});
```

**10. refund**
```javascript
gtag('event', 'refund', {
  transaction_id: 'T_12345',
  value: 64.98,
  currency: 'USD',
  items: [{
    item_id: 'SKU_12345',
    quantity: 2
  }]
});
```

### Lead Generation Events

**generate_lead**
```javascript
gtag('event', 'generate_lead', {
  currency: 'USD',
  value: 50.00,
  lead_source: 'contact_form'
});
```

**sign_up**
```javascript
gtag('event', 'sign_up', {
  method: 'Google'
});
```

**login**
```javascript
gtag('event', 'login', {
  method: 'email'
});
```

### Engagement Events

**search**
```javascript
gtag('event', 'search', {
  search_term: 'android t-shirt'
});
```

**share**
```javascript
gtag('event', 'share', {
  method: 'Twitter',
  content_type: 'article',
  item_id: 'article_123'
});
```

**view_promotion**
```javascript
gtag('event', 'view_promotion', {
  promotion_id: 'SUMMER_SALE',
  promotion_name: 'Summer Sale',
  creative_name: 'banner_1',
  creative_slot: 'hero_banner'
});
```

**select_promotion**
```javascript
gtag('event', 'select_promotion', {
  promotion_id: 'SUMMER_SALE',
  promotion_name: 'Summer Sale'
});
```

## Custom Events

### When to Create Custom Events

Create custom events when:
- No recommended event fits your use case
- You need to track business-specific interactions
- You want to measure unique user behaviors
- Standard events don't capture necessary parameters

### Custom Event Implementation

**Via gtag.js**:
```javascript
gtag('event', 'custom_event_name', {
  parameter_1: 'value_1',
  parameter_2: 'value_2',
  value: 10.00  // Optional monetary value
});
```

**Via Google Tag Manager**:
1. Create new tag: Tag Type = Google Analytics: GA4 Event
2. Configuration Tag: Select your GA4 Configuration tag
3. Event Name: Enter custom event name
4. Event Parameters: Add parameter rows
5. Triggering: Define when event should fire

### Custom Event Examples

**Video Engagement**:
```javascript
gtag('event', 'video_milestone', {
  video_title: 'Product Demo',
  video_duration: 120,
  milestone_reached: 50,  // 50% completion
  video_provider: 'Vimeo'
});
```

**Content Engagement**:
```javascript
gtag('event', 'article_read', {
  article_title: 'How to Use GA4',
  article_category: 'Analytics',
  read_time_seconds: 180,
  scroll_depth: 100
});
```

**Tool Usage**:
```javascript
gtag('event', 'calculator_used', {
  calculator_type: 'mortgage',
  loan_amount: 300000,
  interest_rate: 3.5,
  result_calculated: true
});
```

## Event Parameters

### Standard Parameters

GA4 recognizes these parameters across all events:
- `currency`: ISO 4217 currency code (e.g., USD, EUR, GBP)
- `value`: Monetary value of the event
- `items`: Array of item objects for e-commerce
- `transaction_id`: Unique identifier for purchases
- `coupon`: Coupon code applied
- `shipping`: Shipping cost
- `tax`: Tax amount

### Custom Parameters

**Limits**:
- 25 custom parameters per event
- 100 characters maximum per parameter value
- 50 event-scoped custom dimensions per property
- 25 user-scoped custom dimensions per property

**Registration**:
Custom parameters must be registered as custom dimensions in GA4:
1. Navigate to Configure > Custom Definitions
2. Click "Create custom dimension"
3. Select scope: Event or User
4. Enter parameter name (must match exactly)
5. Provide description and display name

**Example Custom Parameters**:
```javascript
gtag('event', 'form_submit', {
  form_name: 'contact_us',
  form_location: 'footer',
  user_type: 'returning_customer',
  form_fields_completed: 5
});
```

## User Properties

User properties are attributes that describe segments of your user base.

### Setting User Properties

**Via gtag.js**:
```javascript
gtag('set', 'user_properties', {
  account_type: 'premium',
  signup_date: '2026-01-15',
  preferred_category: 'electronics'
});
```

**Via Google Tag Manager**:
1. Create GA4 Configuration tag
2. Add User Properties in Fields to Set
3. Property Name: account_type
4. Value: {{Account Type Variable}}

### User Property Best Practices

- Use for persistent user attributes (not event-specific data)
- Maximum 25 user-scoped custom dimensions
- Update when user attributes change
- Avoid high-cardinality values (user IDs, timestamps)
- Examples: subscription_tier, customer_segment, lifetime_value_bucket

## Conversion Events

### Marking Events as Conversions

1. Navigate to Configure > Events
2. Find the event in the list
3. Toggle "Mark as conversion"
4. Event will appear in Conversions report within 24 hours

### Conversion Best Practices

- Limit to 30 conversion events per property
- Mark only meaningful business outcomes
- Use consistent conversion values for optimization
- Include transaction_id for purchase conversions to prevent duplicates
- Test conversions in Debug View before marking

### Conversion Value

Assign monetary value to conversions for ROI analysis:
```javascript
gtag('event', 'sign_up', {
  value: 25.00,  // Estimated value of a signup
  currency: 'USD'
});
```

## Event Debugging

### Debug View

Real-time event validation:
1. Navigate to Configure > DebugView
2. Enable debug mode:
   - **Chrome Extension**: Install Google Analytics Debugger
   - **gtag.js**: Add `debug_mode: true` parameter
   - **GTM**: Enable Preview mode
3. Perform actions on your site
4. Verify events appear with correct parameters

### Common Issues

**Event Not Firing**:
- Check tag firing in GTM Preview or browser console
- Verify trigger conditions are met
- Ensure GA4 Configuration tag loads before event tags

**Missing Parameters**:
- Verify parameter names match exactly (case-sensitive)
- Check for JavaScript errors preventing parameter population
- Ensure variables are defined before event fires

**Duplicate Events**:
- Check for multiple GA4 tags on the page
- Verify event isn't firing from both gtag.js and GTM
- Review trigger conditions for overlaps

## Event Limits and Quotas

### Collection Limits

- **Events per session**: No limit
- **Event name length**: 40 characters
- **Parameter name length**: 40 characters
- **Parameter value length**: 100 characters
- **Parameters per event**: 25
- **User properties**: 25 per property
- **Distinct event names**: 500 per property

### Reporting Limits

- **Custom dimensions**: 50 event-scoped, 25 user-scoped
- **Custom metrics**: 50 event-scoped
- **Conversion events**: 30 per property
- **Audiences**: 100 per property

## Advanced Event Tracking

### Server-Side Event Tracking

Send events from your server using Measurement Protocol:

```python
import requests

url = 'https://www.google-analytics.com/mp/collect'
params = {
    'measurement_id': 'G-XXXXXXXXXX',
    'api_secret': 'YOUR_API_SECRET'
}

payload = {
    'client_id': 'user_12345',
    'events': [{
        'name': 'purchase',
        'params': {
            'transaction_id': 'T_12345',
            'value': 99.99,
            'currency': 'USD',
            'items': [{
                'item_id': 'SKU_123',
                'item_name': 'Product Name',
                'price': 99.99,
                'quantity': 1
            }]
        }
    }]
}

response = requests.post(url, params=params, json=payload)
```

### Event Modification

Modify or create events in GA4 interface:
1. Navigate to Configure > Events
2. Click "Create event"
3. Define matching conditions (e.g., event_name equals "page_view")
4. Add or modify parameters
5. Optionally copy to new event name

**Use Cases**:
- Add missing parameters to existing events
- Create new events based on parameter values
- Standardize event names across platforms
- Enrich events with additional context
