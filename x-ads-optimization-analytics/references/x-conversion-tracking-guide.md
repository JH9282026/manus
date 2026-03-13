# X Ads Conversion Tracking Guide

Detailed implementation guide for conversion tracking on X platform.

---

## Conversion Event Types

| Type | Use Case |
|------|----------|
| **PURCHASE** | E-commerce transactions |
| **SIGN_UP** | Account registrations |
| **DOWNLOAD** | File/app downloads |
| **ADD_TO_CART** | Shopping cart additions |
| **CHECKOUT_INITIATED** | Checkout starts |
| **SITE_VISIT** | Key page visits |
| **CUSTOM** | Custom events |

---

## Implementation Steps

### 1. Create Conversion Event via API

```python
import requests

conversion_data = {
    "name": "Product Purchase",
    "type": "PURCHASE",
    "post_view_attribution_window": "30_DAY",
    "post_engagement_attribution_window": "30_DAY"
}

response = requests.post(
    f"https://ads-api.x.com/12/accounts/{account_id}/conversion_events",
    headers={"Authorization": f"Bearer {access_token}"},
    json=conversion_data
)

event_data = response.json()["data"]
pixel_id = event_data["pixel_id"]
event_id = event_data["id"]
```

### 2. Install Base Pixel Code

Place in `<head>` section of all pages:

```html
<script>
!function(e,t,n,s,u,a){e.twq||(s=e.twq=function(){s.exe?s.exe.apply(s,arguments):s.queue.push(arguments);
},s.version='1.1',s.queue=[],u=t.createElement(n),u.async=!0,u.src='https://static.ads-twitter.com/uwt.js',
a=t.getElementsByTagName(n)[0],a.parentNode.insertBefore(u,a))}(window,document,'script');
twq('config','PIXEL_ID');
</script>
```

### 3. Track Conversion Events

**Purchase Event**
```javascript
twq('event', 'tw-PIXEL_ID-EVENT_ID', {
  value: 99.99,
  currency: 'USD',
  conversion_id: 'order_12345',
  num_items: 2,
  description: 'Product purchase'
});
```

**Sign Up Event**
```javascript
twq('event', 'tw-PIXEL_ID-SIGNUP_EVENT_ID', {
  email_address: 'user@example.com'  // Hashed automatically
});
```

**Add to Cart**
```javascript
twq('event', 'tw-PIXEL_ID-CART_EVENT_ID', {
  value: 49.99,
  currency: 'USD',
  content_ids: ['SKU123', 'SKU456'],
  content_type: 'product'
});
```

---

## Attribution Windows

### Post-View Attribution
User saw ad but didn't click, converted later.

**Options**: 1_DAY, 7_DAY, 14_DAY, 30_DAY

### Post-Engagement Attribution
User clicked ad, converted later.

**Options**: 1_DAY, 7_DAY, 14_DAY, 30_DAY

**Recommendation**: 30_DAY for both (industry standard)

---

## Advanced Tracking

### Dynamic Event Values

```javascript
// Get value from page
const orderTotal = document.getElementById('order-total').textContent;
const orderId = document.getElementById('order-id').textContent;

twq('event', 'tw-PIXEL_ID-PURCHASE_EVENT_ID', {
  value: parseFloat(orderTotal),
  currency: 'USD',
  conversion_id: orderId
});
```

### Single Page Applications (SPA)

```javascript
// Track page view on route change
function trackPageView() {
  twq('track', 'PageView');
}

// React Router example
history.listen(() => {
  trackPageView();
});
```

### Server-Side Tracking

```python
import requests
import hashlib

def track_conversion_server_side(pixel_id, event_id, email, value):
    # Hash email
    hashed_email = hashlib.sha256(email.encode()).hexdigest()
    
    payload = {
        "conversions": [{
            "conversion_time": "2026-03-12T10:30:00Z",
            "event_id": event_id,
            "identifiers": [{
                "hashed_email": hashed_email
            }],
            "conversion_value": value,
            "currency": "USD"
        }]
    }
    
    response = requests.post(
        f"https://ads-api.x.com/12/measurement/conversions/{pixel_id}",
        headers=headers,
        json=payload
    )
```

---

## Verification

### Test Pixel Installation

1. Install X Pixel Helper browser extension
2. Visit your website
3. Check for green checkmark (pixel firing)
4. Verify event parameters

### API Verification

```python
# Get conversion event details
response = requests.get(
    f"https://ads-api.x.com/12/accounts/{account_id}/conversion_events/{event_id}",
    headers=headers
)

print(response.json())
```

---

## Troubleshooting

### Pixel Not Firing
- Check browser console for errors
- Verify pixel ID is correct
- Ensure script loads before tracking calls
- Check ad blockers

### Conversions Not Tracking
- Verify attribution windows
- Check event ID matches
- Ensure value/currency format correct
- Wait 24-48 hours for data processing

### Duplicate Conversions
- Use unique `conversion_id` parameter
- Implement deduplication logic
- Check for multiple pixel installations

---

## Privacy & Compliance

### GDPR Compliance

```javascript
// Only fire pixel if user consents
if (userHasConsented()) {
  twq('config', 'PIXEL_ID');
}
```

### Data Hashing

X automatically hashes:
- Email addresses
- Phone numbers
- First/last names

No need to hash client-side.
