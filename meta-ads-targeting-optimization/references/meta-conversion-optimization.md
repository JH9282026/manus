# Meta Conversion Optimization

Advanced conversion tracking and optimization strategies for Meta advertising.

---

## Meta Pixel Implementation

### Base Pixel Code

Install on all pages:

```html
<!-- Meta Pixel Code -->
<script>
!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', 'YOUR_PIXEL_ID');
fbq('track', 'PageView');
</script>
<noscript>
<img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id=YOUR_PIXEL_ID&ev=PageView&noscript=1"/>
</noscript>
<!-- End Meta Pixel Code -->
```

### Standard Events

**E-commerce Events**

```javascript
// View Content (Product Page)
fbq('track', 'ViewContent', {
  content_ids: ['SKU123'],
  content_type: 'product',
  content_name: 'Blue T-Shirt',
  content_category: 'Apparel',
  value: 29.99,
  currency: 'USD'
});

// Add to Cart
fbq('track', 'AddToCart', {
  content_ids: ['SKU123'],
  content_type: 'product',
  value: 29.99,
  currency: 'USD'
});

// Initiate Checkout
fbq('track', 'InitiateCheckout', {
  content_ids: ['SKU123', 'SKU456'],
  content_type: 'product',
  value: 79.98,
  currency: 'USD',
  num_items: 2
});

// Add Payment Info
fbq('track', 'AddPaymentInfo', {
  content_ids: ['SKU123', 'SKU456'],
  content_type: 'product',
  value: 79.98,
  currency: 'USD'
});

// Purchase
fbq('track', 'Purchase', {
  content_ids: ['SKU123', 'SKU456'],
  content_type: 'product',
  value: 79.98,
  currency: 'USD',
  num_items: 2
});
```

**Lead Generation Events**

```javascript
// Lead
fbq('track', 'Lead', {
  content_name: 'Newsletter Signup',
  value: 5.00,
  currency: 'USD'
});

// Complete Registration
fbq('track', 'CompleteRegistration', {
  content_name: 'Account Created',
  value: 10.00,
  currency: 'USD',
  status: 'completed'
});
```

**Engagement Events**

```javascript
// Search
fbq('track', 'Search', {
  search_string: 'blue t-shirt',
  content_category: 'Apparel'
});

// Add to Wishlist
fbq('track', 'AddToWishlist', {
  content_ids: ['SKU123'],
  value: 29.99,
  currency: 'USD'
});
```

### Custom Events

```javascript
// Custom event
fbq('trackCustom', 'DownloadWhitepaper', {
  content_name: 'Marketing Guide 2026',
  value: 15.00,
  currency: 'USD'
});

// Custom event with parameters
fbq('trackCustom', 'VideoWatched', {
  video_title: 'Product Demo',
  watch_percentage: 75
});
```

---

## Conversion API (Server-Side Tracking)

### Why Use Conversion API

- **iOS 14+ tracking limitations**
- **Ad blocker bypass**
- **More accurate attribution**
- **Redundancy with pixel**

### Implementation

```python
import requests
import hashlib
import time

def send_conversion_event(pixel_id, access_token, event_data):
    url = f"https://graph.facebook.com/v19.0/{pixel_id}/events"
    
    # Hash user data
    def hash_data(data):
        if data:
            return hashlib.sha256(data.lower().strip().encode()).hexdigest()
        return None
    
    payload = {
        "data": [
            {
                "event_name": event_data["event_name"],
                "event_time": int(time.time()),
                "action_source": "website",
                "event_source_url": event_data["url"],
                "user_data": {
                    "em": [hash_data(event_data.get("email"))],
                    "ph": [hash_data(event_data.get("phone"))],
                    "client_ip_address": event_data.get("ip"),
                    "client_user_agent": event_data.get("user_agent"),
                    "fbc": event_data.get("fbc"),  # Facebook click ID
                    "fbp": event_data.get("fbp")   # Facebook browser ID
                },
                "custom_data": {
                    "value": event_data.get("value"),
                    "currency": event_data.get("currency", "USD"),
                    "content_ids": event_data.get("content_ids", []),
                    "content_type": "product"
                }
            }
        ],
        "access_token": access_token
    }
    
    response = requests.post(url, json=payload)
    return response.json()

# Example usage
event_data = {
    "event_name": "Purchase",
    "url": "https://example.com/checkout/success",
    "email": "customer@example.com",
    "phone": "+12025551234",
    "ip": "192.168.1.1",
    "user_agent": "Mozilla/5.0...",
    "fbc": "fb.1.1234567890.AbCdEfGhIjKlMnOpQrStUvWxYz",
    "fbp": "fb.1.1234567890.1234567890",
    "value": 99.99,
    "currency": "USD",
    "content_ids": ["SKU123"]
}

send_conversion_event(pixel_id, access_token, event_data)
```

---

## Optimization Goals

### Goal Selection Guide

| Business Goal | Optimization Goal | Billing Event |
|---------------|-------------------|---------------|
| **Website Sales** | OFFSITE_CONVERSIONS (Purchase) | IMPRESSIONS |
| **Lead Generation** | OFFSITE_CONVERSIONS (Lead) | IMPRESSIONS |
| **App Installs** | APP_INSTALLS | IMPRESSIONS |
| **Website Traffic** | LANDING_PAGE_VIEWS | IMPRESSIONS |
| **Engagement** | POST_ENGAGEMENT | IMPRESSIONS |
| **Video Views** | THRUPLAY | IMPRESSIONS |
| **Brand Awareness** | REACH | IMPRESSIONS |

### Value Optimization

**When to Use**:
- E-commerce with varying product prices
- Want to maximize revenue, not just conversions
- Have sufficient conversion volume (50+ per week)

**Setup**:
```python
adset_data = {
    "optimization_goal": "VALUE",
    "billing_event": "IMPRESSIONS",
    "promoted_object": json.dumps({
        "pixel_id": pixel_id,
        "custom_event_type": "PURCHASE"
    })
}
```

**Requirements**:
- Pass `value` parameter in pixel events
- Minimum 50 conversions per week
- Consistent conversion volume

---

## Bidding Strategies

### Lowest Cost (Automatic)

**Best For**: Maximum volume

```python
adset_data = {
    "bid_strategy": "LOWEST_COST_WITHOUT_CAP",
    "optimization_goal": "OFFSITE_CONVERSIONS"
}
```

### Bid Cap

**Best For**: Cost control

```python
adset_data = {
    "bid_strategy": "LOWEST_COST_WITH_BID_CAP",
    "bid_amount": 500,  # $5 max bid
    "optimization_goal": "OFFSITE_CONVERSIONS"
}
```

### Cost Cap

**Best For**: Target CPA

```python
adset_data = {
    "bid_strategy": "COST_CAP",
    "bid_amount": 2500,  # $25 target CPA
    "optimization_goal": "OFFSITE_CONVERSIONS"
}
```

### Minimum ROAS

**Best For**: Profitability

```python
adset_data = {
    "bid_strategy": "LOWEST_COST_WITH_MIN_ROAS",
    "bid_amount": 250,  # 2.5x ROAS minimum
    "optimization_goal": "VALUE"
}
```

---

## Learning Phase

### What is Learning Phase?

- Meta's algorithm learns optimal delivery
- Requires ~50 conversions per week
- Performance may fluctuate
- Avoid edits during learning

### Exiting Learning Phase Faster

**Do**:
- Use broad targeting
- Set adequate budget
- Use automatic bidding
- Let it run uninterrupted

**Don't**:
- Make frequent edits
- Pause/unpause repeatedly
- Change targeting
- Adjust budget >20%

### Learning Limited

**Causes**:
- Audience too small
- Budget too low
- Bid too low
- <50 conversions per week

**Solutions**:
- Broaden targeting
- Increase budget
- Combine ad sets
- Use higher funnel event

---

## Attribution Settings

### Attribution Windows

**Click-Through Attribution**:
- 1-day click
- 7-day click (default)

**View-Through Attribution**:
- 1-day view (default)

**Recommendation**: 7-day click, 1-day view

### Changing Attribution

```python
# Set at ad account level
url = f"https://graph.facebook.com/v19.0/act_{ad_account_id}"

params = {
    "access_token": access_token,
    "attribution_spec": json.dumps([
        {
            "event_type": "CLICK_THROUGH",
            "window_days": 7
        },
        {
            "event_type": "VIEW_THROUGH",
            "window_days": 1
        }
    ])
}

requests.post(url, params=params)
```

---

## Conversion Lift Studies

### Setup Conversion Lift Test

```python
url = f"https://graph.facebook.com/v19.0/act_{ad_account_id}/brandlift_studies"

study_data = {
    "access_token": access_token,
    "name": "Q2 Conversion Lift Study",
    "type": "CONVERSION_LIFT",
    "start_time": "2026-04-01T00:00:00Z",
    "end_time": "2026-04-30T23:59:59Z",
    "campaigns": [campaign_id],
    "objectives": ["PURCHASE"]
}

response = requests.post(url, params=study_data)
```

**Requirements**:
- Minimum budget: $30,000
- Minimum duration: 14 days
- Sufficient conversion volume

---

## Troubleshooting

### Low Conversion Volume

**Solutions**:
1. Optimize for higher-funnel event (AddToCart instead of Purchase)
2. Broaden targeting
3. Increase budget
4. Improve creative
5. Check pixel implementation

### High CPA

**Solutions**:
1. Use Cost Cap bidding
2. Narrow targeting
3. Improve landing page
4. Test new creatives
5. Exclude converters

### Pixel Not Firing

**Checks**:
1. Meta Pixel Helper extension
2. Browser console errors
3. Ad blockers disabled
4. Correct pixel ID
5. Script loads before events
