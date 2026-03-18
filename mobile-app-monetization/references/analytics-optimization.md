# Analytics and Optimization

Comprehensive guide to mobile app monetization analytics, metrics tracking, and revenue optimization strategies.

## Key Performance Indicators (KPIs)

### Revenue Metrics

#### ARPU (Average Revenue Per User)

```
ARPU = Total Revenue / Total Users

Example:
Total Revenue: $10,000
Total Users: 50,000
ARPU = $10,000 / 50,000 = $0.20
```

**Interpretation:**
- Low ARPU (<$0.10): Focus on monetization improvements
- Medium ARPU ($0.10-$1.00): Optimize conversion and retention
- High ARPU (>$1.00): Scale user acquisition

#### ARPPU (Average Revenue Per Paying User)

```
ARPPU = Total Revenue / Paying Users

Example:
Total Revenue: $10,000
Paying Users: 500
ARPPU = $10,000 / 500 = $20
```

**Benchmarks by Category:**
```
Games: $10-$50
Utilities: $5-$20
Productivity: $20-$100
Content/Streaming: $10-$30
```

#### ARPDAU (Average Revenue Per Daily Active User)

```
ARPDAU = Daily Revenue / Daily Active Users

Example:
Daily Revenue: $500
DAU: 10,000
ARPDAU = $500 / 10,000 = $0.05
```

**Use Case:** Track daily monetization efficiency

#### LTV (Lifetime Value)

```
LTV = ARPU × Average Lifetime (days)

Alternative:
LTV = ARPPU × Conversion Rate × Average Lifetime

Example:
ARPU: $0.20
Average Lifetime: 180 days
LTV = $0.20 × 180 = $36
```

**Cohort-Based LTV:**
```
Month 0: $1.00
Month 1: $0.80 (80% retention)
Month 2: $0.64 (80% retention)
Month 3: $0.51 (80% retention)
...

Total LTV = $1.00 + $0.80 + $0.64 + $0.51 + ... = $5.00
```

### Conversion Metrics

#### Conversion Rate

```
Conversion Rate = Paying Users / Total Users × 100%

Example:
Paying Users: 1,500
Total Users: 50,000
Conversion Rate = 1,500 / 50,000 × 100% = 3%
```

**Benchmarks:**
```
Games: 1-5%
Utilities: 0.5-2%
Productivity: 2-5%
Content: 5-15%
```

#### Trial Conversion Rate

```
Trial Conversion = Paid Subscribers / Trial Starts × 100%

Example:
Paid Subscribers: 300
Trial Starts: 1,000
Trial Conversion = 300 / 1,000 × 100% = 30%
```

**Benchmarks:**
```
No payment required: 10-20%
Payment required: 40-60%
```

#### Subscription Metrics

**Renewal Rate:**
```
Renewal Rate = Renewed Subscriptions / Expiring Subscriptions × 100%

Example:
Renewed: 800
Expiring: 1,000
Renewal Rate = 800 / 1,000 × 100% = 80%
```

**Churn Rate:**
```
Churn Rate = Cancelled Subscriptions / Total Subscribers × 100%

Example:
Cancelled: 200
Total Subscribers: 1,000
Churn Rate = 200 / 1,000 × 100% = 20%
```

**Monthly Recurring Revenue (MRR):**
```
MRR = Active Subscribers × Average Subscription Price

Example:
Active Subscribers: 5,000
Average Price: $9.99
MRR = 5,000 × $9.99 = $49,950
```

### User Acquisition Metrics

#### CAC (Customer Acquisition Cost)

```
CAC = Total Marketing Spend / New Users Acquired

Example:
Marketing Spend: $10,000
New Users: 5,000
CAC = $10,000 / 5,000 = $2.00
```

#### Payback Period

```
Payback Period = CAC / ARPDAU

Example:
CAC: $2.00
ARPDAU: $0.05
Payback Period = $2.00 / $0.05 = 40 days
```

**Target:** <90 days for sustainable growth

#### ROI (Return on Investment)

```
ROI = (LTV - CAC) / CAC × 100%

Example:
LTV: $36
CAC: $2.00
ROI = ($36 - $2) / $2 × 100% = 1,700%
```

**Target:** ROI > 300% (LTV > 3x CAC)

### Retention Metrics

#### Day N Retention

```
Day N Retention = Users Active on Day N / Users Acquired on Day 0 × 100%

Example:
Day 1: 4,000 / 10,000 = 40%
Day 7: 2,000 / 10,000 = 20%
Day 30: 1,000 / 10,000 = 10%
```

**Benchmarks:**
```
Day 1: 35-45% (good)
Day 7: 15-25% (good)
Day 30: 8-15% (good)
```

#### Cohort Retention

```
Cohort: Users acquired in January 2024

Month 0: 10,000 users (100%)
Month 1: 4,000 users (40%)
Month 2: 2,400 users (24%)
Month 3: 1,680 users (16.8%)
```

### Ad Revenue Metrics

#### eCPM (Effective Cost Per Mille)

```
eCPM = Ad Revenue / Impressions × 1,000

Example:
Ad Revenue: $500
Impressions: 100,000
eCPM = $500 / 100,000 × 1,000 = $5.00
```

#### Fill Rate

```
Fill Rate = Filled Ad Requests / Total Ad Requests × 100%

Example:
Filled: 9,500
Total: 10,000
Fill Rate = 9,500 / 10,000 × 100% = 95%
```

**Target:** >90% fill rate

#### CTR (Click-Through Rate)

```
CTR = Clicks / Impressions × 100%

Example:
Clicks: 500
Impressions: 100,000
CTR = 500 / 100,000 × 100% = 0.5%
```

**Benchmarks:**
```
Banner: 0.5-1%
Interstitial: 1-3%
Native: 1-2%
```

## Analytics Implementation

### Firebase Analytics (iOS)

```swift
import FirebaseAnalytics

class AnalyticsManager {
    // Track purchase
    func trackPurchase(productId: String, price: Double, currency: String) {
        Analytics.logEvent(AnalyticsEventPurchase, parameters: [
            AnalyticsParameterItemID: productId,
            AnalyticsParameterPrice: price,
            AnalyticsParameterCurrency: currency,
            AnalyticsParameterValue: price,
            AnalyticsParameterTransactionID: UUID().uuidString
        ])
    }
    
    // Track subscription start
    func trackSubscriptionStart(productId: String, price: Double, trialDays: Int) {
        Analytics.logEvent("subscription_start", parameters: [
            "product_id": productId,
            "price": price,
            "trial_days": trialDays,
            "subscription_type": "monthly"
        ])
    }
    
    // Track subscription renewal
    func trackSubscriptionRenewal(productId: String, price: Double) {
        Analytics.logEvent("subscription_renewal", parameters: [
            "product_id": productId,
            "price": price
        ])
    }
    
    // Track subscription cancellation
    func trackSubscriptionCancellation(productId: String, reason: String) {
        Analytics.logEvent("subscription_cancel", parameters: [
            "product_id": productId,
            "cancel_reason": reason
        ])
    }
    
    // Track paywall view
    func trackPaywallView(source: String, variant: String) {
        Analytics.logEvent("paywall_view", parameters: [
            "source": source,
            "variant": variant,
            "timestamp": Date().timeIntervalSince1970
        ])
    }
    
    // Track paywall conversion
    func trackPaywallConversion(source: String, productId: String) {
        Analytics.logEvent("paywall_conversion", parameters: [
            "source": source,
            "product_id": productId
        ])
    }
    
    // Track ad impression
    func trackAdImpression(adType: String, network: String, revenue: Double) {
        Analytics.logEvent("ad_impression", parameters: [
            "ad_type": adType,
            "ad_network": network,
            "ad_revenue": revenue,
            "ad_currency": "USD"
        ])
    }
    
    // Track ad click
    func trackAdClick(adType: String, network: String) {
        Analytics.logEvent("ad_click", parameters: [
            "ad_type": adType,
            "ad_network": network
        ])
    }
    
    // Set user properties
    func setUserProperties(isPremium: Bool, subscriptionType: String?) {
        Analytics.setUserProperty(isPremium ? "premium" : "free", forName: "user_type")
        if let subscriptionType = subscriptionType {
            Analytics.setUserProperty(subscriptionType, forName: "subscription_type")
        }
    }
}
```

### Firebase Analytics (Android)

```kotlin
import com.google.firebase.analytics.FirebaseAnalytics
import com.google.firebase.analytics.ktx.analytics
import com.google.firebase.analytics.ktx.logEvent
import com.google.firebase.ktx.Firebase

class AnalyticsManager(private val context: Context) {
    private val analytics = Firebase.analytics
    
    // Track purchase
    fun trackPurchase(productId: String, price: Double, currency: String) {
        analytics.logEvent(FirebaseAnalytics.Event.PURCHASE) {
            param(FirebaseAnalytics.Param.ITEM_ID, productId)
            param(FirebaseAnalytics.Param.PRICE, price)
            param(FirebaseAnalytics.Param.CURRENCY, currency)
            param(FirebaseAnalytics.Param.VALUE, price)
            param(FirebaseAnalytics.Param.TRANSACTION_ID, UUID.randomUUID().toString())
        }
    }
    
    // Track subscription start
    fun trackSubscriptionStart(productId: String, price: Double, trialDays: Int) {
        analytics.logEvent("subscription_start") {
            param("product_id", productId)
            param("price", price)
            param("trial_days", trialDays.toLong())
            param("subscription_type", "monthly")
        }
    }
    
    // Track subscription renewal
    fun trackSubscriptionRenewal(productId: String, price: Double) {
        analytics.logEvent("subscription_renewal") {
            param("product_id", productId)
            param("price", price)
        }
    }
    
    // Track subscription cancellation
    fun trackSubscriptionCancellation(productId: String, reason: String) {
        analytics.logEvent("subscription_cancel") {
            param("product_id", productId)
            param("cancel_reason", reason)
        }
    }
    
    // Track paywall view
    fun trackPaywallView(source: String, variant: String) {
        analytics.logEvent("paywall_view") {
            param("source", source)
            param("variant", variant)
            param("timestamp", System.currentTimeMillis())
        }
    }
    
    // Track paywall conversion
    fun trackPaywallConversion(source: String, productId: String) {
        analytics.logEvent("paywall_conversion") {
            param("source", source)
            param("product_id", productId)
        }
    }
    
    // Track ad impression
    fun trackAdImpression(adType: String, network: String, revenue: Double) {
        analytics.logEvent("ad_impression") {
            param("ad_type", adType)
            param("ad_network", network)
            param("ad_revenue", revenue)
            param("ad_currency", "USD")
        }
    }
    
    // Track ad click
    fun trackAdClick(adType: String, network: String) {
        analytics.logEvent("ad_click") {
            param("ad_type", adType)
            param("ad_network", network)
        }
    }
    
    // Set user properties
    fun setUserProperties(isPremium: Boolean, subscriptionType: String?) {
        analytics.setUserProperty("user_type", if (isPremium) "premium" else "free")
        subscriptionType?.let {
            analytics.setUserProperty("subscription_type", it)
        }
    }
}
```

## A/B Testing

### Pricing Tests

**Test Setup:**
```
Control (50%): $9.99/month
Variant A (25%): $7.99/month
Variant B (25%): $12.99/month

Duration: 2 weeks
Sample Size: 10,000 users per variant
```

**Metrics to Track:**
- Conversion rate
- Revenue per user
- Total revenue
- Retention rate
- User feedback

**Analysis:**
```
Control:
- Conversion: 3%
- ARPU: $0.30
- Total Revenue: $3,000

Variant A:
- Conversion: 4.5%
- ARPU: $0.36
- Total Revenue: $3,600 (+20%)

Variant B:
- Conversion: 2%
- ARPU: $0.26
- Total Revenue: $2,600 (-13%)

Winner: Variant A (lower price, higher conversion)
```

### Paywall Tests

**Test Variables:**
- Paywall design
- Copy and messaging
- Feature highlights
- Social proof
- Pricing display
- CTA button text

**Example Test:**
```
Control:
- "Upgrade to Premium"
- List of features
- "Start Free Trial" button

Variant A:
- "Join 1M+ Premium Users"
- Benefits-focused copy
- "Try Premium Free" button

Variant B:
- "Unlock All Features"
- Comparison table
- "Get Premium Now" button

Measure:
- Paywall → Trial conversion
- Trial → Paid conversion
- Overall conversion rate
```

### Ad Placement Tests

**Test Setup:**
```
Control:
- Banner at bottom
- Interstitial every 3 minutes
- Rewarded video on demand

Variant A:
- No banner
- Interstitial every 5 minutes
- Rewarded video on demand

Variant B:
- Banner at bottom
- Interstitial every 3 minutes
- Rewarded video + offerwall

Measure:
- ARPDAU
- Retention (D1, D7)
- Session length
- User complaints
```

## Funnel Analysis

### Subscription Funnel

```
10,000 App Installs
    ↓ (40% view paywall)
4,000 Paywall Views
    ↓ (25% start trial)
1,000 Trial Starts
    ↓ (40% convert to paid)
400 Paid Subscribers

Overall Conversion: 4%
```

**Optimization Opportunities:**
- Increase paywall views (onboarding, feature gates)
- Improve paywall conversion (design, copy, pricing)
- Increase trial conversion (engagement, reminders)

### Purchase Funnel

```
10,000 Users
    ↓ (50% engage with premium features)
5,000 Feature Engagement
    ↓ (40% view paywall)
2,000 Paywall Views
    ↓ (10% initiate purchase)
200 Purchase Initiated
    ↓ (80% complete purchase)
160 Purchases Completed

Overall Conversion: 1.6%
```

**Drop-off Analysis:**
- Feature engagement → Paywall: 60% drop-off
- Paywall → Purchase: 90% drop-off
- Purchase → Completion: 20% drop-off

**Optimization:**
- Add more premium feature touchpoints
- Improve paywall design and messaging
- Simplify purchase flow
- Reduce payment friction

## Cohort Analysis

### Revenue Cohorts

```
January 2024 Cohort (10,000 users)

Month 0: $10,000 (100 paying users, $100 ARPPU)
Month 1: $8,000 (80 paying users, 80% retention)
Month 2: $6,400 (64 paying users, 80% retention)
Month 3: $5,120 (51 paying users, 80% retention)
...

Total LTV: $50,000 / 10,000 = $5.00 per user
```

### Retention Cohorts

```
Cohort: January 2024 (10,000 users)

Day 1: 4,000 (40%)
Day 7: 2,000 (20%)
Day 30: 1,000 (10%)
Day 90: 500 (5%)
Day 180: 300 (3%)
```

## Optimization Strategies

### Pricing Optimization

**Dynamic Pricing:**
- Adjust prices based on user behavior
- Offer discounts to high-intent users
- Test regional pricing

**Psychological Pricing:**
- $9.99 vs $10.00
- Anchor with higher-priced tier
- Show savings ("Save 33%")

**Promotional Pricing:**
- Limited-time offers
- Seasonal discounts
- First-time user discounts

### Conversion Optimization

**Paywall Optimization:**
- Clear value proposition
- Social proof ("Join 1M+ users")
- Highlight savings
- Multiple CTAs
- Easy dismissal

**Onboarding Optimization:**
- Show value early
- Personalized experience
- Feature discovery
- Paywall at right moment

**Trial Optimization:**
- Longer trial