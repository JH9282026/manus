# Shopify App Development Guide

Comprehensive guide to building, deploying, and distributing Shopify apps.

---

## App Architecture Patterns

### Embedded Admin Apps

Apps that run within the Shopify Admin interface:

**Technology Stack:**
- Frontend: React with Shopify Polaris components
- Backend: Node.js, Ruby, Python, or PHP
- Authentication: OAuth 2.0
- Communication: Shopify Admin API (REST or GraphQL)

**Setup Process:**

1. Create app in Partner Dashboard
2. Configure app URLs (App URL, Allowed redirection URLs)
3. Set up OAuth flow
4. Implement App Bridge for embedded experience

**Example App Bridge Setup:**

```javascript
import createApp from '@shopify/app-bridge';
import { Redirect } from '@shopify/app-bridge/actions';

const app = createApp({
  apiKey: 'your-api-key',
  host: new URLSearchParams(window.location.search).get('host'),
});

const redirect = Redirect.create(app);

// Redirect to admin page
redirect.dispatch(Redirect.Action.ADMIN_PATH, '/products');
```

### Theme App Extensions

Add functionality directly to merchant storefronts:

**Use Cases:**
- Product reviews and ratings
- Size guides and fit finders
- Wishlist functionality
- Custom product options
- Live chat widgets

**Development Approach:**

```bash
# Create theme app extension
shopify app generate extension

# Select "Theme app extension"
# Choose blocks or app embeds
```

**Extension Structure:**

```
extensions/
└── my-extension/
    ├── blocks/
    │   └── product-reviews.liquid
    ├── assets/
    │   ├── reviews.js
    │   └── reviews.css
    └── locales/
        └── en.default.json
```

### Headless/API-Only Apps

Backend services without UI:

**Use Cases:**
- Inventory synchronization
- Order fulfillment automation
- Data analytics and reporting
- Third-party integrations

**Implementation:**
- Use Admin API for data access
- Implement webhooks for real-time updates
- No OAuth UI required for private apps
- Can run as serverless functions or background workers

## OAuth Implementation

### OAuth Flow Steps

1. **Installation Request:**
   - Merchant clicks "Install App"
   - App redirects to Shopify OAuth page

2. **Permission Grant:**
   - Merchant reviews requested scopes
   - Approves or denies access

3. **Authorization Code:**
   - Shopify redirects back to app with code
   - App exchanges code for access token

4. **Token Storage:**
   - Store access token securely
   - Associate with shop domain

### OAuth Code Example (Node.js)

```javascript
const express = require('express');
const crypto = require('crypto');
const axios = require('axios');

const app = express();
const API_KEY = process.env.SHOPIFY_API_KEY;
const API_SECRET = process.env.SHOPIFY_API_SECRET;
const SCOPES = 'read_products,write_products,read_orders';
const REDIRECT_URI = 'https://yourapp.com/auth/callback';

// Step 1: Initiate OAuth
app.get('/auth', (req, res) => {
  const shop = req.query.shop;
  const nonce = crypto.randomBytes(16).toString('hex');
  
  // Store nonce in session for verification
  req.session.nonce = nonce;
  
  const authUrl = `https://${shop}/admin/oauth/authorize?` +
    `client_id=${API_KEY}&` +
    `scope=${SCOPES}&` +
    `redirect_uri=${REDIRECT_URI}&` +
    `state=${nonce}`;
  
  res.redirect(authUrl);
});

// Step 2: Handle callback
app.get('/auth/callback', async (req, res) => {
  const { shop, code, state, hmac } = req.query;
  
  // Verify HMAC
  const map = Object.assign({}, req.query);
  delete map.hmac;
  const message = Object.keys(map)
    .map(key => `${key}=${map[key]}`)
    .sort()
    .join('&');
  
  const generatedHash = crypto
    .createHmac('sha256', API_SECRET)
    .update(message)
    .digest('hex');
  
  if (generatedHash !== hmac) {
    return res.status(400).send('HMAC validation failed');
  }
  
  // Verify nonce
  if (state !== req.session.nonce) {
    return res.status(400).send('State validation failed');
  }
  
  // Exchange code for access token
  try {
    const response = await axios.post(
      `https://${shop}/admin/oauth/access_token`,
      {
        client_id: API_KEY,
        client_secret: API_SECRET,
        code: code
      }
    );
    
    const accessToken = response.data.access_token;
    
    // Store access token securely (database, encrypted)
    await storeAccessToken(shop, accessToken);
    
    res.redirect('/dashboard');
  } catch (error) {
    res.status(500).send('Token exchange failed');
  }
});
```

### Scope Management

**Request Only Necessary Scopes:**

| Scope | Purpose | When to Request |
|-------|---------|----------------|
| `read_products` | View product data | Product display, search |
| `write_products` | Modify products | Bulk editing, imports |
| `read_orders` | View order data | Analytics, reporting |
| `write_orders` | Modify orders | Fulfillment, editing |
| `read_customers` | View customer data | CRM, segmentation |
| `write_customers` | Modify customers | Data enrichment |
| `read_inventory` | View inventory | Stock monitoring |
| `write_inventory` | Modify inventory | Sync, adjustments |

**Scope Update Process:**
- Changing scopes requires merchant reauthorization
- Implement graceful scope upgrade flow
- Explain why new permissions are needed

## Webhook Implementation

### Webhook Registration

**Via Admin API (GraphQL):**

```graphql
mutation {
  webhookSubscriptionCreate(
    topic: PRODUCTS_CREATE
    webhookSubscription: {
      format: JSON
      callbackUrl: "https://yourapp.com/webhooks/products/create"
    }
  ) {
    webhookSubscription {
      id
      topic
      format
      endpoint {
        __typename
        ... on WebhookHttpEndpoint {
          callbackUrl
        }
      }
    }
    userErrors {
      field
      message
    }
  }
}
```

### Webhook Verification

**Verify HMAC Signature:**

```javascript
const crypto = require('crypto');

function verifyWebhook(req) {
  const hmac = req.get('X-Shopify-Hmac-Sha256');
  const body = req.rawBody; // Raw request body
  
  const hash = crypto
    .createHmac('sha256', process.env.SHOPIFY_API_SECRET)
    .update(body, 'utf8')
    .digest('base64');
  
  return hash === hmac;
}

app.post('/webhooks/products/create', (req, res) => {
  if (!verifyWebhook(req)) {
    return res.status(401).send('Unauthorized');
  }
  
  const product = req.body;
  
  // Process webhook
  console.log('New product created:', product.title);
  
  // Respond quickly (within 5 seconds)
  res.status(200).send('OK');
  
  // Process asynchronously
  processProductCreation(product);
});
```

### Common Webhook Topics

| Topic | Trigger | Use Case |
|-------|---------|----------|
| `products/create` | New product | Sync to external system |
| `products/update` | Product modified | Update cache, reindex |
| `orders/create` | New order | Send notifications |
| `orders/fulfilled` | Order fulfilled | Update analytics |
| `customers/create` | New customer | Add to CRM |
| `app/uninstalled` | App removed | Cleanup, analytics |
| `shop/update` | Shop settings changed | Update configuration |

## Admin API Usage

### GraphQL vs REST

**Use GraphQL When:**
- Need specific fields only (reduce payload)
- Fetching related resources (products + variants + images)
- Bulk operations
- Modern app development

**Use REST When:**
- Simple CRUD operations
- Legacy system integration
- Specific REST-only endpoints

### GraphQL Query Examples

**Fetch Products with Variants:**

```graphql
query {
  products(first: 10) {
    edges {
      node {
        id
        title
        handle
        variants(first: 5) {
          edges {
            node {
              id
              title
              price
              inventoryQuantity
            }
          }
        }
        images(first: 1) {
          edges {
            node {
              url
              altText
            }
          }
        }
      }
    }
  }
}
```

**Create Product:**

```graphql
mutation {
  productCreate(
    input: {
      title: "New Product"
      productType: "Apparel"
      vendor: "My Brand"
      variants: [
        {
          price: "29.99"
          inventoryQuantity: 100
        }
      ]
    }
  ) {
    product {
      id
      title
    }
    userErrors {
      field
      message
    }
  }
}
```

### Rate Limiting

**Shopify API Rate Limits:**
- REST: 2 requests/second (bucket-based)
- GraphQL: Cost-based (1000 points per second)

**Handle Rate Limits:**

```javascript
const axios = require('axios');

async function makeShopifyRequest(url, options) {
  try {
    const response = await axios(url, options);
    return response.data;
  } catch (error) {
    if (error.response?.status === 429) {
      // Rate limited
      const retryAfter = error.response.headers['retry-after'] || 2;
      console.log(`Rate limited. Retrying after ${retryAfter}s`);
      
      await new Promise(resolve => setTimeout(resolve, retryAfter * 1000));
      return makeShopifyRequest(url, options);
    }
    throw error;
  }
}
```

## App Billing

### Billing Models

**Recurring Charges:**
- Monthly subscription
- Automatic renewal
- Can offer free trial period

**One-Time Charges:**
- Single payment
- For specific features or services

**Usage Charges:**
- Based on app usage metrics
- Capped amount per billing cycle

### Implementing Recurring Billing (GraphQL)

```graphql
mutation {
  appSubscriptionCreate(
    name: "Premium Plan"
    returnUrl: "https://yourapp.com/billing/confirm"
    test: true
    lineItems: [
      {
        plan: {
          appRecurringPricingDetails: {
            price: { amount: 29.99, currencyCode: USD }
            interval: EVERY_30_DAYS
          }
        }
      }
    ]
  ) {
    appSubscription {
      id
    }
    confirmationUrl
    userErrors {
      field
      message
    }
  }
}
```

**Billing Flow:**
1. Create subscription charge
2. Redirect merchant to `confirmationUrl`
3. Merchant approves charge
4. Shopify redirects to `returnUrl`
5. Activate subscription in app

## App Store Submission

### Pre-Submission Checklist

**Technical Requirements:**
- [ ] OAuth implementation complete
- [ ] HTTPS on all URLs
- [ ] Webhook verification implemented
- [ ] GDPR compliance (data deletion, access)
- [ ] Performance impact < 10 Lighthouse points
- [ ] Error handling and logging
- [ ] Mobile-responsive UI

**Content Requirements:**
- [ ] App name (unique, under 30 chars)
- [ ] App icon (512x512px, no text)
- [ ] Feature video or image
- [ ] 3-6 screenshots (1600x900px)
- [ ] Demo store with realistic data
- [ ] Introduction (100 chars)
- [ ] Details (500 chars)
- [ ] Feature list (3-6 features)
- [ ] Pricing clearly stated
- [ ] Privacy policy URL
- [ ] Support URL

### App Listing Optimization

**App Name Best Practices:**
- Start with brand name
- Include primary function
- Keep under 30 characters
- Example: "BrandName - Email Marketing"

**Screenshot Guidelines:**
- Show actual app interface
- Highlight key features
- Use real data, not placeholders
- Include captions explaining features
- First screenshot is most important

**Feature Video Tips:**
- 2-3 minutes maximum
- Show app in action
- Demonstrate key workflows
- Include voiceover or captions
- Professional quality

### GDPR Compliance

**Required Webhooks:**

1. **customers/data_request:**
   - Provide customer data within 30 days
   - Include all stored information

2. **customers/redact:**
   - Delete customer data within 30 days
   - Remove from all systems

3. **shop/redact:**
   - Delete shop data after 48 hours
   - Triggered when app is uninstalled

**Implementation Example:**

```javascript
app.post('/webhooks/customers/data_request', async (req, res) => {
  const { shop_domain, customer } = req.body;
  
  // Gather all customer data
  const customerData = await getCustomerData(shop_domain, customer.id);
  
  // Send to merchant or customer
  await sendDataRequest(customerData);
  
  res.status(200).send('OK');
});

app.post('/webhooks/customers/redact', async (req, res) => {
  const { shop_domain, customer } = req.body;
  
  // Delete customer data
  await deleteCustomerData(shop_domain, customer.id);
  
  res.status(200).send('OK');
});

app.post('/webhooks/shop/redact', async (req, res) => {
  const { shop_domain } = req.body;
  
  // Delete all shop data after 48 hours
  setTimeout(async () => {
    await deleteShopData(shop_domain);
  }, 48 * 60 * 60 * 1000);
  
  res.status(200).send('OK');
});
```

## Testing and Quality Assurance

### Development Store Testing

**Create Development Store:**
1. Log in to Partner Dashboard
2. Navigate to Stores
3. Create development store
4. Install app for testing

**Test Scenarios:**
- Fresh installation
- Reinstallation after uninstall
- Scope changes and reauthorization
- Billing flow (use test mode)
- Webhook delivery and processing
- Performance impact on storefront
- Mobile responsiveness
- Error handling

### Performance Testing

**Lighthouse Testing:**

```bash
# Install Lighthouse
npm install -g lighthouse

# Test storefront before app installation
lighthouse https://test-store.myshopify.com --output html --output-path ./before.html

# Install app

# Test storefront after app installation
lighthouse https://test-store.myshopify.com --output html --output-path ./after.html

# Compare scores (should be < 10 point difference)
```

### Load Testing

Test app under realistic load:

```javascript
// Using artillery.io
const artillery = require('artillery');

// config.yml
module.exports = {
  config: {
    target: 'https://yourapp.com',
    phases: [
      { duration: 60, arrivalRate: 10 },
      { duration: 120, arrivalRate: 50 },
      { duration: 60, arrivalRate: 10 }
    ]
  },
  scenarios: [
    {
      flow: [
        { get: { url: '/dashboard' } },
        { post: { url: '/api/products', json: { title: 'Test' } } }
      ]
    }
  ]
};
```

## Deployment and Monitoring

### Deployment Platforms

**Recommended Platforms:**
- Heroku (easy setup, auto-scaling)
- AWS (flexible, scalable)
- Google Cloud Platform (integrated services)
- DigitalOcean (cost-effective)
- Vercel/Netlify (serverless, frontend)

### Monitoring and Logging

**Essential Metrics:**
- API response times
- Error rates
- Webhook processing times
- Database query performance
- Memory and CPU usage

**Logging Tools:**
- Sentry (error tracking)
- LogRocket (session replay)
- Datadog (infrastructure monitoring)
- New Relic (application performance)

**Example Error Tracking:**

```javascript
const Sentry = require('@sentry/node');

Sentry.init({
  dsn: process.env.SENTRY_DSN,
  environment: process.env.NODE_ENV,
  tracesSampleRate: 1.0
});

app.use(Sentry.Handlers.requestHandler());
app.use(Sentry.Handlers.errorHandler());

app.get('/api/products', async (req, res) => {
  try {
    const products = await fetchProducts();
    res.json(products);
  } catch (error) {
    Sentry.captureException(error);
    res.status(500).json({ error: 'Internal server error' });
  }
});
```