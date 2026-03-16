# Product Analytics Implementation Guide

Step-by-step guide to implementing product analytics from planning through optimization, with code examples and best practices.

---

## Pre-Implementation Planning

### Step 1: Define Your Analytics Strategy

**Identify Your North Star Metric**

The north star metric is the single metric that best predicts long-term success.

**Examples by Product Type:**
- **Slack:** Messages sent by teams
- **Airbnb:** Nights booked
- **Spotify:** Time spent listening
- **Notion:** Collaborative documents created
- **Zoom:** Weekly meeting minutes hosted

**Criteria for North Star Metric:**
- Reflects core value delivered to users
- Measurable and trackable
- Correlates with revenue and retention
- Actionable (team can influence it)

**Exercise: Define Your North Star**
1. What core value does your product provide?
2. What user action best represents that value?
3. Can you measure it reliably?
4. Does it predict retention and revenue?

### Step 2: Map the User Journey

Document the complete user journey from awareness to advocacy.

**Example: SaaS Product Journey**

```
1. Awareness
   └─ Landing page visit
   └─ Blog post read

2. Acquisition
   └─ Signup form viewed
   └─ Account created

3. Activation
   └─ Email verified
   └─ Profile completed
   └─ First core action (aha moment)

4. Engagement
   └─ Daily/weekly usage
   └─ Feature adoption
   └─ Collaboration (invites)

5. Retention
   └─ Return visits
   └─ Habit formation

6. Revenue
   └─ Trial started
   └─ Payment added
   └─ Subscription activated

7. Referral
   └─ Invite sent
   └─ Review left
   └─ Social share
```

**Identify Key Touchpoints:**
For each stage, list the critical events that indicate progress.

### Step 3: Create a Tracking Plan

A tracking plan is a comprehensive document specifying all events, properties, and implementation details.

**Tracking Plan Template:**

| Event Name | Description | Trigger | Properties | Platforms | Priority |
|------------|-------------|---------|------------|-----------|----------|
| Signup Completed | User creates account | Account creation success | `signup_method` (string), `referral_source` (string), `user_id` (string) | Web, iOS, Android | P0 |
| Feature Used | User engages with feature | Feature interaction | `feature_name` (string), `duration_seconds` (number), `success` (boolean) | Web, iOS, Android | P0 |
| Payment Added | User adds payment method | Payment form submission | `payment_method` (string), `plan_type` (string) | Web | P0 |
| Invite Sent | User invites team member | Invite button clicked | `invite_method` (string), `recipient_count` (number) | Web, iOS, Android | P1 |

**Priority Levels:**
- **P0:** Critical for core analytics (implement first)
- **P1:** Important for optimization (implement second)
- **P2:** Nice-to-have for deep analysis (implement later)

**Tools for Tracking Plans:**
- **Spreadsheets:** Google Sheets, Excel (simple, accessible)
- **Avo:** Collaborative tracking plan with type safety
- **Segment Protocols:** Data quality and governance
- **Amplitude Data:** Tracking plan integrated with platform

### Step 4: Establish Naming Conventions

**Event Naming:**
- **Format:** `Object Action` (Title Case)
- **Examples:** `Button Clicked`, `Video Played`, `Purchase Completed`
- **Be specific but not overly granular:** `Signup Button Clicked` not `Homepage Hero CTA Button Clicked`

**Property Naming:**
- **Format:** `snake_case` (lowercase with underscores)
- **Examples:** `user_id`, `plan_type`, `video_duration_seconds`
- **Include units in name:** `duration_seconds`, `price_usd`

**User Property Naming:**
- **Format:** `snake_case`
- **Examples:** `signup_date`, `subscription_tier`, `total_logins`
- **Prefix custom properties:** `custom_industry`, `custom_company_size`

**Consistency Rules:**
- Use same casing throughout (don't mix Title Case and snake_case for events)
- Use consistent terminology (`user` vs. `customer`, `plan` vs. `subscription`)
- Document abbreviations (`cta` = call-to-action, `mau` = monthly active users)

---

## Implementation

### Platform-Specific SDK Installation

#### Web (JavaScript)

**Mixpanel:**
```html
<!-- Add to <head> -->
<script type="text/javascript">
(function(f,b){if(!b.__SV){var e,g,i,h;window.mixpanel=b;b._i=[];b.init=function(e,f,c){function g(a,d){var b=d.split(".");2==b.length&&(a=a[b[0]],d=b[1]);a[d]=function(){a.push([d].concat(Array.prototype.slice.call(arguments,0)))}}var a=b;"undefined"!==typeof c?a=b[c]=[]:c="mixpanel";a.people=a.people||[];a.toString=function(a){var d="mixpanel";"mixpanel"!==c&&(d+="."+c);a||(d+=" (stub)");return d};a.people.toString=function(){return a.toString(1)+".people (stub)"};i="disable time_event track track_pageview track_links track_forms track_with_groups add_group set_group remove_group register register_once alias unregister identify name_tag set_config reset opt_in_tracking opt_out_tracking has_opted_in_tracking has_opted_out_tracking clear_opt_in_out_tracking start_batch_senders people.set people.set_once people.unset people.increment people.append people.union people.track_charge people.clear_charges people.delete_user people.remove".split(" ");
for(h=0;h<i.length;h++)g(a,i[h]);var j="set set_once union unset remove delete".split(" ");a.get_group=function(){function b(c){d[c]=function(){call2_args=arguments;call2=[c].concat(Array.prototype.slice.call(call2_args,0));a.push([e,call2])}}for(var d={},e=["get_group"].concat(Array.prototype.slice.call(arguments,0)),c=0;c<j.length;c++)b(j[c]);return d};b._i.push([e,f,c])};b.__SV=1.2;e=f.createElement("script");e.type="text/javascript";e.async=!0;e.src="undefined"!==typeof MIXPANEL_CUSTOM_LIB_URL?MIXPANEL_CUSTOM_LIB_URL:"file:"===f.location.protocol&&"//cdn.mxpnl.com/libs/mixpanel-2-latest.min.js".match(/^\/\//)?"https://cdn.mxpnl.com/libs/mixpanel-2-latest.min.js":"//cdn.mxpnl.com/libs/mixpanel-2-latest.min.js";g=f.getElementsByTagName("script")[0];g.parentNode.insertBefore(e,g)}})(document,window.mixpanel||[]);
</script>

<script>
mixpanel.init('YOUR_PROJECT_TOKEN', {
  debug: true, // Enable for development
  track_pageview: true,
  persistence: 'localStorage'
});
</script>
```

**Amplitude:**
```html
<script type="text/javascript">
!function(){"use strict";!function(e,t){var r=e.amplitude||{_q:[],_iq:{}};if(r.invoked)e.console&&console.error&&console.error("Amplitude snippet has been loaded.");else{r.invoked=!0;var n=t.createElement("script");n.type="text/javascript",n.integrity="sha384-[HASH]",n.crossOrigin="anonymous",n.async=!0,n.src="https://cdn.amplitude.com/libs/analytics-browser-2.0.0-min.js.gz",n.onload=function(){e.amplitude.runQueuedFunctions||console.log("[Amplitude] Error: could not load SDK")};var s=t.getElementsByTagName("script")[0];s.parentNode.insertBefore(n,s);}}(window,document)}();

amplitude.init('YOUR_API_KEY', {
  defaultTracking: {
    sessions: true,
    pageViews: true,
    formInteractions: true,
    fileDownloads: true
  }
});
</script>
```

**PostHog:**
```html
<script>
!function(t,e){var o,n,p,r;e.__SV||(window.posthog=e,e._i=[],e.init=function(i,s,a){function g(t,e){var o=e.split(".");2==o.length&&(t=t[o[0]],e=o[1]),t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}}(p=t.createElement("script")).type="text/javascript",p.async=!0,p.src=s.api_host+"/static/array.js",(r=t.getElementsByTagName("script")[0]).parentNode.insertBefore(p,r);var u=e;for(void 0!==a?u=e[a]=[]:a="posthog",u.people=u.people||[],u.toString=function(t){var e="posthog";return"posthog"!==a&&(e+="."+a),t||(e+=" (stub)"),e},u.people.toString=function(){return u.toString(1)+".people (stub)"},o="capture identify alias people.set people.set_once set_config register register_once unregister opt_out_capturing has_opted_out_capturing opt_in_capturing reset isFeatureEnabled onFeatureFlags getFeatureFlag getFeatureFlagPayload reloadFeatureFlags group updateEarlyAccessFeatureEnrollment getEarlyAccessFeatures getActiveMatchingSurveys getSurveys".split(" "),n=0;n<o.length;n++)g(u,o[n]);e._i.push([i,s,a])},e.__SV=1)}(document,window.posthog||[]);
posthog.init('YOUR_PROJECT_API_KEY', {api_host: 'https://app.posthog.com'})
</script>
```

#### Mobile (React Native)

**Mixpanel:**
```bash
npm install mixpanel-react-native
```

```javascript
import { Mixpanel } from 'mixpanel-react-native';

const trackAutomaticEvents = true;
const mixpanel = new Mixpanel('YOUR_PROJECT_TOKEN', trackAutomaticEvents);
mixpanel.init();

// Track event
mixpanel.track('Button Clicked', {
  button_name: 'Sign Up',
  screen: 'Home'
});

// Identify user
mixpanel.identify('user_123');

// Set user properties
mixpanel.getPeople().set('$email', 'user@example.com');
mixpanel.getPeople().set('plan_type', 'premium');
```

**Amplitude:**
```bash
npm install @amplitude/analytics-react-native
```

```javascript
import { init, track, Identify, identify, setUserId } from '@amplitude/analytics-react-native';

init('YOUR_API_KEY');

// Track event
track('Button Clicked', {
  button_name: 'Sign Up',
  screen: 'Home'
});

// Identify user
setUserId('user_123');

// Set user properties
const identifyObj = new Identify();
identifyObj.set('email', 'user@example.com');
identifyObj.set('plan_type', 'premium');
identify(identifyObj);
```

#### Backend (Python)

**Mixpanel:**
```bash
pip install mixpanel
```

```python
from mixpanel import Mixpanel

mp = Mixpanel('YOUR_PROJECT_TOKEN')

# Track event
mp.track('user_123', 'Purchase Completed', {
    'product_id': 'prod_456',
    'price_usd': 99.99,
    'currency': 'USD'
})

# Set user properties
mp.people_set('user_123', {
    '$email': 'user@example.com',
    'plan_type': 'premium',
    'total_purchases': 5
})

# Increment property
mp.people_increment('user_123', {'total_purchases': 1})
```

**Amplitude:**
```bash
pip install amplitude-analytics
```

```python
from amplitude import Amplitude, BaseEvent, Identify

client = Amplitude('YOUR_API_KEY')

# Track event
event = BaseEvent(
    event_type='Purchase Completed',
    user_id='user_123',
    event_properties={
        'product_id': 'prod_456',
        'price_usd': 99.99,
        'currency': 'USD'
    }
)
client.track(event)

# Set user properties
identify_obj = Identify()
identify_obj.set('email', 'user@example.com')
identify_obj.set('plan_type', 'premium')
identify_obj.add('total_purchases', 1)

client.identify(identify_obj, 'user_123')
```

---

## Event Tracking Patterns

### Pattern 1: Page/Screen Views

**Web (Mixpanel):**
```javascript
// Automatic page tracking
mixpanel.track_pageview();

// Manual page tracking with properties
mixpanel.track('Page Viewed', {
  page_name: 'Pricing',
  page_category: 'Marketing',
  referrer: document.referrer
});
```

**React (Amplitude):**
```javascript
import { useEffect } from 'react';
import { track } from '@amplitude/analytics-browser';
import { useLocation } from 'react-router-dom';

function App() {
  const location = useLocation();

  useEffect(() => {
    track('Page Viewed', {
      page_path: location.pathname,
      page_title: document.title
    });
  }, [location]);

  return <div>...</div>;
}
```

### Pattern 2: Button Clicks

**HTML + JavaScript:**
```html
<button id="signup-btn" onclick="trackSignupClick()">Sign Up</button>

<script>
function trackSignupClick() {
  mixpanel.track('Button Clicked', {
    button_name: 'Sign Up',
    button_location: 'Header',
    page: window.location.pathname
  });
}
</script>
```

**React:**
```javascript
import { track } from '@amplitude/analytics-browser';

function SignupButton() {
  const handleClick = () => {
    track('Button Clicked', {
      button_name: 'Sign Up',
      button_location: 'Header',
      page: window.location.pathname
    });
    
    // Proceed with signup logic
    window.location.href = '/signup';
  };

  return <button onClick={handleClick}>Sign Up</button>;
}
```

### Pattern 3: Form Submissions

```javascript
function handleFormSubmit(event) {
  event.preventDefault();
  
  const formData = new FormData(event.target);
  const email = formData.get('email');
  const plan = formData.get('plan');
  
  // Track form submission
  mixpanel.track('Form Submitted', {
    form_name: 'Signup Form',
    plan_selected: plan,
    page: window.location.pathname
  });
  
  // Identify user
  mixpanel.identify(email);
  mixpanel.people.set({
    '$email': email,
    'plan_type': plan,
    'signup_date': new Date().toISOString()
  });
  
  // Submit form
  // ...
}
```

### Pattern 4: Feature Usage

```javascript
function useFeature(featureName) {
  const startTime = Date.now();
  
  return {
    complete: (success = true) => {
      const duration = (Date.now() - startTime) / 1000;
      
      mixpanel.track('Feature Used', {
        feature_name: featureName,
        duration_seconds: duration,
        success: success
      });
    }
  };
}

// Usage
const feature = useFeature('Export PDF');
try {
  await exportPDF();
  feature.complete(true);
} catch (error) {
  feature.complete(false);
}
```

### Pattern 5: User Identification & Properties

**On Signup:**
```javascript
function onSignupComplete(user) {
  // Mixpanel
  mixpanel.alias(user.id); // Link anonymous ID to user ID
  mixpanel.identify(user.id);
  mixpanel.people.set({
    '$email': user.email,
    '$name': user.name,
    'signup_date': new Date().toISOString(),
    'plan_type': user.plan,
    'referral_source': getReferralSource()
  });
  
  // Track signup event
  mixpanel.track('Signup Completed', {
    signup_method: user.signupMethod,
    referral_source: getReferralSource()
  });
}
```

**On Login:**
```javascript
function onLoginComplete(user) {
  mixpanel.identify(user.id);
  
  // Increment login count
  mixpanel.people.increment('total_logins', 1);
  
  // Update last login
  mixpanel.people.set({
    'last_login': new Date().toISOString()
  });
  
  mixpanel.track('Login Completed', {
    login_method: user.loginMethod
  });
}
```

### Pattern 6: Revenue Tracking

**Mixpanel:**
```javascript
function onPurchaseComplete(purchase) {
  mixpanel.track('Purchase Completed', {
    product_id: purchase.productId,
    product_name: purchase.productName,
    price_usd: purchase.price,
    currency: purchase.currency,
    payment_method: purchase.paymentMethod
  });
  
  // Track revenue
  mixpanel.people.track_charge(purchase.price, {
    '$time': new Date().toISOString(),
    'product_id': purchase.productId
  });
  
  // Update user properties
  mixpanel.people.increment('total_purchases', 1);
  mixpanel.people.increment('lifetime_value', purchase.price);
}
```

**Amplitude:**
```javascript
import { track, revenue } from '@amplitude/analytics-browser';

function onPurchaseComplete(purchase) {
  // Track event
  track('Purchase Completed', {
    product_id: purchase.productId,
    product_name: purchase.productName,
    price_usd: purchase.price,
    currency: purchase.currency,
    payment_method: purchase.paymentMethod
  });
  
  // Track revenue
  const revenueEvent = new revenue.Revenue()
    .setProductId(purchase.productId)
    .setPrice(purchase.price)
    .setQuantity(1)
    .setRevenueType('purchase');
  
  revenue.track(revenueEvent);
}
```

---

## Data Governance

### Event Taxonomy Management

**Mixpanel Lexicon:**
- Centralized event and property definitions
- Edit event names and descriptions retroactively
- Hide deprecated events
- Merge duplicate events

**Amplitude Taxonomy:**
- Hierarchical event categorization
- Planned events vs. unexpected events
- Block/delete events and properties
- Cannot edit historical data (immutable)

**Best Practices:**
1. **Regular audits:** Quarterly review of all events
2. **Deprecation process:** Mark events as deprecated before removal
3. **Documentation:** Maintain descriptions for all events
4. **Ownership:** Assign owners to event categories

### Data Quality Monitoring

**Validation Rules:**
```javascript
function trackEvent(eventName, properties) {
  // Validate event name
  if (!eventName || typeof eventName !== 'string') {
    console.error('Invalid event name:', eventName);
    return;
  }
  
  // Validate required properties
  const requiredProps = getRequiredProperties(eventName);
  for (const prop of requiredProps) {
    if (!(prop in properties)) {
      console.error(`Missing required property "${prop}" for event "${eventName}"`);
      return;
    }
  }
  
  // Validate property types
  for (const [key, value] of Object.entries(properties)) {
    const expectedType = getPropertyType(eventName, key);
    if (typeof value !== expectedType) {
      console.error(`Invalid type for property "${key}": expected ${expectedType}, got ${typeof value}`);
      return;
    }
  }
  
  // Track event
  mixpanel.track(eventName, properties);
}
```

**Automated Alerts:**
- Missing events (expected events not firing)
- Unexpected events (new events not in tracking plan)
- Property type mismatches
- Significant volume changes

---

## Dashboard Creation

### Dashboard Structure

**Executive Dashboard (Weekly Review):**
1. **Growth Metrics**
   - MRR and growth rate (line chart)
   - New customers (bar chart)
   - Churn rate (line chart)

2. **Engagement Metrics**
   - DAU/MAU (line chart)
   - Stickiness ratio (metric)
   - Top features by usage (table)

3. **Health Metrics**
   - NPS score (metric)
   - Support ticket volume (line chart)
   - Error rate (line chart)

**Product Dashboard (Daily Review):**
1. **Acquisition**
   - Signups by source (stacked bar chart)
   - Signup conversion rate (line chart)

2. **Activation**
   - Activation rate (metric)
   - Time to activation (histogram)
   - Onboarding funnel (funnel chart)

3. **Retention**
   - D1/D7/D30 retention (line chart)
   - Cohort retention table

4. **Engagement**
   - DAU (line chart)
   - Sessions per user (histogram)
   - Feature adoption (table)

### Report Types

**1. Funnel Report**

Analyze conversion through multi-step flows.

**Example: Signup Funnel**
```
Step 1: Landing Page Viewed (10,000 users)
  ↓ 40% conversion
Step 2: Signup Form Viewed (4,000 users)
  ↓ 60% conversion
Step 3: Account Created (2,400 users)
  ↓ 75% conversion
Step 4: Email Verified (1,800 users)
  ↓ 50% conversion
Step 5: First Action Completed (900 users)

Overall Conversion: 9%
```

**Insights:**
- Biggest drop-off: Landing → Signup Form (60% drop)
- Opportunity: Improve landing page CTA and value prop

**2. Retention Report**

Track how many users return over time.

**Example: Cohort Retention**

| Cohort | Day 0 | Day 1 | Day 7 | Day 30 |
|--------|-------|-------|-------|--------|
| Jan 2026 | 100% | 45% | 30% | 22% |
| Feb 2026 | 100% | 50% | 35% | 25% |
| Mar 2026 | 100% | 55% | 40% | - |

**Insights:**
- Retention improving month-over-month
- D1 retention increased from 45% to 55%
- Likely due to onboarding improvements

**3. Segmentation Report**

Compare metrics across user segments.

**Example: Engagement by Plan Type**

| Segment | DAU/MAU | Avg Sessions/Week | Retention (D30) |
|---------|---------|-------------------|------------------|
| Free | 15% | 2.5 | 18% |
| Basic | 25% | 5.0 | 35% |
| Premium | 40% | 8.5 | 60% |

**Insights:**
- Premium users 2.7x more engaged than free
- Strong correlation between plan tier and retention
- Opportunity: Convert free users to paid

---

## Optimization Workflows

### Workflow 1: Improve Activation Rate

**Current State:**
- Activation rate: 30%
- Activation definition: User completes 3 core actions

**Analysis:**
1. Build activation funnel
2. Identify biggest drop-off point
3. Segment by acquisition source
4. Analyze successful vs. unsuccessful users

**Hypothesis:**
- Users don't understand value of core actions
- Onboarding doesn't guide users effectively

**Experiment:**
- Add in-app tooltips for core actions
- Implement progress bar in onboarding
- Send email nudges for incomplete actions

**Measurement:**
- Track activation rate weekly
- Compare control vs. experiment groups
- Target: 40% activation rate

### Workflow 2: Reduce Churn

**Current State:**
- Monthly churn: 8%
- Target: 5%

**Analysis:**
1. Segment churned users by characteristics
2. Identify common behaviors before churn
3. Build churn prediction model

**Insights:**
- Users who don't use feature X in first 14 days have 3x churn
- Users with <2 sessions/week churn at 15% rate
- Churned users had 50% lower engagement in last 7 days

**Interventions:**
- Email campaign promoting feature X
- In-app prompts for low-engagement users
- Customer success outreach for at-risk accounts

**Measurement:**
- Track churn rate by cohort
- Measure intervention effectiveness
- Monitor engagement metrics

### Workflow 3: Increase Feature Adoption

**Current State:**
- Feature Y adoption: 20% of active users
- Target: 40%

**Analysis:**
1. Identify user segments with low adoption
2. Analyze feature discovery paths
3. Survey users on awareness and value

**Insights:**
- 60% of users unaware feature exists
- Feature buried in settings menu
- Users who try feature have 2x retention

**Experiments:**
- Add feature to main navigation
- In-app announcement for new users
- Contextual prompts when feature would be useful

**Measurement:**
- Track feature adoption rate
- Measure time to first use
- Monitor retention impact

---

## Advanced Techniques

### Cohort Analysis

Group users by shared characteristics to compare behavior.

**Example: Retention by Acquisition Channel**

```
Organic Search Cohort (Jan 2026):
- Day 1: 60%
- Day 7: 45%
- Day 30: 35%

Paid Ads Cohort (Jan 2026):
- Day 1: 40%
- Day 7: 25%
- Day 30: 18%

Referral Cohort (Jan 2026):
- Day 1: 70%
- Day 7: 55%
- Day 30: 45%
```

**Insight:** Referral users have 2.5x better retention than paid ads. Invest more in referral program.

### Path Analysis

Uncover common user journeys and unexpected patterns.

**Example: Paths to Conversion**

```
Most Common Path (35% of conversions):
Landing Page → Pricing Page → Signup → Trial Started → Payment Added

Second Most Common (20% of conversions):
Blog Post → Feature Page → Signup → Trial Started → Payment Added

Unexpected Path (10% of conversions):
Landing Page → Signup → Trial Started → Pricing Page → Payment Added
```

**Insight:** 10% of users sign up before viewing pricing. Consider offering trial-first signup flow.

### Predictive Analytics

**Churn Prediction:**
Use ML to identify users likely to churn.

**Amplitude Compass:**
- Automatically identifies behaviors correlated with retention/churn
- Provides churn risk score per user
- Suggests interventions

**Custom Model (Python):**
```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Features
features = [
    'days_since_signup',
    'total_sessions',
    'sessions_last_7_days',
    'features_used',
    'last_login_days_ago'
]

# Train model
X_train = df[features]
y_train = df['churned']

model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predict churn risk
X_current = current_users[features]
churn_risk = model.predict_proba(X_current)[:, 1]

# Identify high-risk users
high_risk_users = current_users[churn_risk > 0.7]
```

---

## Troubleshooting

### Common Issues

**Issue: Events not appearing in platform**

**Solutions:**
1. Check SDK initialization (correct API key)
2. Verify network requests in browser DevTools
3. Enable debug mode to see console logs
4. Check for ad blockers or privacy extensions
5. Verify events are firing (add console.log)

**Issue: Duplicate events**

**Solutions:**
1. Check for multiple SDK initializations
2. Ensure event tracking isn't in a loop
3. Debounce rapid-fire events (e.g., scroll)
4. Use event deduplication in platform settings

**Issue: Incorrect user properties**

**Solutions:**
1. Verify identify() called before setting properties
2. Check property data types (string vs. number)
3. Ensure properties set after user creation
4. Use people.set_once() for immutable properties

**Issue: Low data accuracy**

**Solutions:**
1. Implement validation before tracking
2. Use TypeScript for type safety
3. Regular audits of event data
4. Automated testing for critical events

---

## Checklist: Analytics Implementation

**Planning Phase:**
- [ ] North star metric defined
- [ ] User journey mapped
- [ ] Tracking plan created (10-20 core events)
- [ ] Naming conventions established
- [ ] Platform selected

**Implementation Phase:**
- [ ] SDK installed on all platforms
- [ ] Core events instrumented
- [ ] User identification implemented
- [ ] User properties tracked
- [ ] Revenue tracking configured (if applicable)

**Validation Phase:**
- [ ] Events tested in development
- [ ] Data appearing in platform (<1 min latency)
- [ ] Event properties correct
- [ ] User identification working
- [ ] Cross-device tracking functional

**Dashboard Phase:**
- [ ] Executive dashboard created
- [ ] Product dashboard created
- [ ] Key reports built (funnels, retention, cohorts)
- [ ] Alerts configured
- [ ] Team trained on platform

**Optimization Phase:**
- [ ] Weekly review cadence established
- [ ] Insights documented
- [ ] Experiments running
- [ ] Metrics improving
- [ ] Tracking plan updated regularly
