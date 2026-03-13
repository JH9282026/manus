# Pinterest Tag Implementation

Comprehensive guide to implementing the Pinterest tag for conversion tracking and audience building.

---

## Overview

The Pinterest tag is a JavaScript code snippet placed on your website to track user actions, measure conversions, and build retargeting audiences. It enables conversion optimization, attribution reporting, and audience creation.

## Tag Types

### Base Code

The foundational tag that loads on every page. Tracks page visits and enables audience building.

```javascript
!function(e){if(!window.pintrk){window.pintrk = function () {
window.pintrk.queue.push(Array.prototype.slice.call(arguments))};var
n=window.pintrk;n.queue=[],n.version="3.0";var
t=document.createElement("script");t.async=!0,t.src=e;var
r=document.getElementsByTagName("script")[0];
r.parentNode.insertBefore(t,r)}}("https://s.pinimg.com/ct/core.js");
pintrk('load', 'YOUR_TAG_ID', {em: '<user_email_address>'});
pintrk('page');
```

**Installation**:
1. Replace `YOUR_TAG_ID` with your unique tag ID from Pinterest Ads Manager
2. Place code in `<head>` section of every page
3. Optional: Include hashed user email for enhanced matching

### Event Codes

Track specific user actions beyond page views.

**Standard Events**:

```javascript
// Add to Cart
pintrk('track', 'addtocart', {
  value: 29.99,
  order_quantity: 1,
  currency: 'USD',
  product_id: 'SKU123'
});

// Checkout
pintrk('track', 'checkout', {
  value: 79.99,
  order_quantity: 2,
  currency: 'USD'
});

// Purchase
pintrk('track', 'checkout', {
  value: 79.99,
  order_quantity: 2,
  currency: 'USD',
  order_id: 'ORDER123'
});

// Signup
pintrk('track', 'signup', {
  lead_type: 'Newsletter'
});

// Lead
pintrk('track', 'lead', {
  lead_type: 'Contact Form'
});

// Search
pintrk('track', 'search', {
  search_query: 'blue shoes'
});

// View Category
pintrk('track', 'viewcategory', {
  category: 'Shoes'
});

// Watch Video
pintrk('track', 'watchvideo', {
  video_title: 'Product Demo'
});
```

**Custom Events**:

```javascript
pintrk('track', 'custom_event_name', {
  custom_parameter: 'value'
});
```

## Event Parameters

### Standard Parameters

| Parameter | Type | Description | Example |
|-----------|------|-------------|----------|
| value | Number | Transaction value | 29.99 |
| currency | String | ISO currency code | 'USD' |
| order_quantity | Number | Number of items | 2 |
| order_id | String | Unique order identifier | 'ORDER123' |
| product_id | String | Product SKU or ID | 'SKU123' |
| product_name | String | Product name | 'Blue Sneakers' |
| product_category | String | Product category | 'Footwear' |
| search_query | String | Search term | 'running shoes' |
| lead_type | String | Type of lead | 'Newsletter' |

### Enhanced Match Parameters

Improve conversion attribution by passing user data (hashed):

```javascript
pintrk('load', 'YOUR_TAG_ID', {
  em: '<hashed_email>',
  ph: '<hashed_phone>',
  ge: '<hashed_gender>',
  db: '<hashed_birthdate>',
  ln: '<hashed_last_name>',
  fn: '<hashed_first_name>',
  ct: '<hashed_city>',
  st: '<hashed_state>',
  zp: '<hashed_zip>',
  country: '<hashed_country>'
});
```

**Hashing Requirements**:
- Use SHA-256 algorithm
- Convert to lowercase before hashing
- Remove whitespace
- For email: hash full email address
- For phone: include country code, remove special characters

## Implementation Methods

### Manual Installation

1. Copy base code from Pinterest Ads Manager > Conversions > Pinterest Tag
2. Paste in `<head>` section of all pages
3. Add event codes on relevant pages (checkout, thank you, etc.)
4. Test using Pinterest Tag Helper Chrome extension

### Google Tag Manager

**Base Code Setup**:
1. Create new Custom HTML tag
2. Paste Pinterest base code
3. Set trigger to "All Pages"
4. Publish container

**Event Tracking Setup**:
1. Create new Custom HTML tag for each event
2. Paste event code
3. Set trigger for specific page or action (e.g., "Thank You Page")
4. Use Data Layer variables for dynamic values
5. Publish container

**Example GTM Event Tag**:
```javascript
<script>
pintrk('track', 'checkout', {
  value: {{Transaction Total}},
  order_quantity: {{Transaction Items}},
  currency: 'USD',
  order_id: {{Transaction ID}}
});
</script>
```

### E-commerce Platform Integrations

**Shopify**:
1. Install Pinterest app from Shopify App Store
2. Connect Pinterest Business account
3. Tag automatically installed
4. Conversion events auto-tracked

**WooCommerce**:
1. Install Pinterest for WooCommerce plugin
2. Connect Pinterest Business account
3. Configure conversion events in plugin settings
4. Tag automatically installed

**BigCommerce**:
1. Install Pinterest app from BigCommerce marketplace
2. Authenticate with Pinterest
3. Tag and events automatically configured

## Conversion Event Setup

After tag implementation, configure conversion events in Pinterest Ads Manager.

### Creating Conversion Events

1. Navigate to Ads Manager > Conversions
2. Click "Create Conversion Event"
3. Select event type (Page Visit, Add to Cart, Checkout, etc.)
4. Define event parameters:
   - **Event Name**: Descriptive name (e.g., "Purchase - Thank You Page")
   - **Conversion Window**: 1, 7, 14, or 30 days
   - **Event Value**: Optional, for ROAS tracking
5. Save event

### Conversion Windows

| Window | Description | Use Case |
|--------|-------------|----------|
| 1 Day | Conversions within 24 hours | Short sales cycle |
| 7 Days | Conversions within 7 days | Standard e-commerce |
| 14 Days | Conversions within 14 days | Longer consideration |
| 30 Days | Conversions within 30 days | High-ticket items |

## Audience Building

Use tag data to create retargeting audiences.

### Site Visitor Audiences

**All Visitors**:
- Includes anyone who visited your site
- Minimum 100 users to activate
- Retention: 180 days

**Page-Specific Visitors**:
- Target visitors of specific pages
- Use URL contains, equals, or starts with rules
- Example: URL contains "/products/shoes"

**Event-Based Audiences**:
- Target users who completed specific events
- Example: Added to cart but didn't purchase
- Combine multiple event rules

### Audience Rules

**URL Rules**:
- **Contains**: URL contains specific string
- **Equals**: URL exactly matches
- **Starts with**: URL begins with string
- **Does not contain**: Exclude URLs

**Event Rules**:
- **Event occurred**: User completed event
- **Event did not occur**: User didn't complete event
- **Event value**: Filter by transaction value
- **Time period**: Visitors within X days

**Combination Rules**:
```
Visited /products/shoes
AND Added to Cart
AND NOT Purchased
Within last 30 days
```

## Tag Verification

### Pinterest Tag Helper

1. Install Pinterest Tag Helper Chrome extension
2. Navigate to your website
3. Click extension icon
4. Verify:
   - Base code loads on all pages
   - Event codes fire on correct pages
   - Parameters pass correctly
   - No errors or warnings

### Manual Testing

1. Open browser developer console (F12)
2. Navigate to Network tab
3. Filter for "ct.pinterest.com"
4. Trigger events (add to cart, checkout, etc.)
5. Verify network requests fire with correct parameters

### Pinterest Events Manager

1. Navigate to Ads Manager > Conversions > Events Manager
2. View real-time event activity
3. Check event volume and parameters
4. Verify events match expected behavior

## Troubleshooting

### Common Issues

**Tag Not Loading**:
- Verify base code in `<head>` section
- Check for JavaScript errors in console
- Ensure tag ID is correct
- Verify no ad blockers interfering

**Events Not Firing**:
- Confirm event code on correct pages
- Check trigger conditions (GTM)
- Verify event name matches conversion event
- Test with Tag Helper extension

**Low Match Rates**:
- Implement enhanced match parameters
- Hash user data correctly (SHA-256, lowercase)
- Pass email on base code load
- Verify data format (phone with country code, etc.)

**Duplicate Events**:
- Check for multiple tag installations
- Verify GTM triggers not overlapping
- Ensure platform integration not conflicting with manual tag

### Debugging Tips

1. Use Pinterest Tag Helper for real-time validation
2. Check browser console for JavaScript errors
3. Verify network requests in developer tools
4. Test in incognito mode to avoid cache issues
5. Compare Events Manager data with expected volume

## Advanced Implementation

### Dynamic Product Catalogs

Pass product data for dynamic retargeting:

```javascript
pintrk('track', 'pagevisit', {
  product_id: 'SKU123',
  product_name: 'Blue Sneakers',
  product_category: 'Footwear',
  product_price: 79.99,
  product_currency: 'USD'
});
```

### Multi-Currency Support

Pass currency dynamically based on user location:

```javascript
var userCurrency = getUserCurrency(); // Your function
pintrk('track', 'checkout', {
  value: getConvertedValue(79.99, userCurrency),
  currency: userCurrency,
  order_quantity: 1
});
```

### Server-Side Conversion API

Supplement browser-based tracking with server-side events for improved accuracy:

```python
import requests
import hashlib
import json

def send_conversion_event(event_name, user_email, value, currency):
    url = "https://ct.pinterest.com/v3/"
    
    # Hash user email
    hashed_email = hashlib.sha256(user_email.lower().encode()).hexdigest()
    
    payload = {
        "event_name": event_name,
        "action_source": "web",
        "event_time": int(time.time()),
        "user_data": {
            "em": [hashed_email]
        },
        "custom_data": {
            "value": value,
            "currency": currency
        }
    }
    
    headers = {
        "Content-Type": "application/json",
        "X-Pinterest-Access-Token": "YOUR_ACCESS_TOKEN"
    }
    
    response = requests.post(url, json=payload, headers=headers)
    return response.json()
```

## Compliance and Privacy

### GDPR Compliance

- Obtain user consent before loading Pinterest tag
- Provide opt-out mechanism
- Include Pinterest in privacy policy
- Use consent management platform (CMP)

**Conditional Tag Loading**:
```javascript
if (userHasConsented()) {
  // Load Pinterest tag
  pintrk('load', 'YOUR_TAG_ID');
  pintrk('page');
}
```

### CCPA Compliance

- Honor "Do Not Sell My Personal Information" requests
- Provide opt-out link in privacy policy
- Disable tag for opted-out users

### Data Retention

- Pinterest retains conversion data for 2 years
- Audience data retained for 180 days (site visitors)
- Customer list data retained until manually deleted

## Best Practices

1. **Install base code on all pages** for complete user journey tracking
2. **Use enhanced match** to improve attribution accuracy
3. **Test thoroughly** before launching campaigns
4. **Monitor Events Manager** regularly for data quality
5. **Implement server-side tracking** for critical conversions
6. **Document tag implementation** for team reference
7. **Review privacy compliance** with legal team
8. **Update tag** when Pinterest releases new versions
9. **Create audiences early** to build sufficient size before campaigns
10. **Use descriptive event names** for easy identification