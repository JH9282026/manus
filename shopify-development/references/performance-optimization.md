# Shopify Performance Optimization

Advanced techniques for optimizing Shopify theme and app performance.

---

## Core Web Vitals Optimization

### Largest Contentful Paint (LCP)

**Target: < 2.5 seconds**

LCP measures loading performance of the largest visible content element.

**Optimization Strategies:**

1. **Optimize Hero Images:**
```liquid
{%- assign hero_image = section.settings.image -%}
<img
  src="{{ hero_image | image_url: width: 1920 }}"
  srcset="
    {{ hero_image | image_url: width: 750 }} 750w,
    {{ hero_image | image_url: width: 1100 }} 1100w,
    {{ hero_image | image_url: width: 1500 }} 1500w,
    {{ hero_image | image_url: width: 1920 }} 1920w
  "
  sizes="100vw"
  loading="eager"
  fetchpriority="high"
  width="1920"
  height="{{ 1920 | divided_by: hero_image.aspect_ratio | round }}"
  alt="{{ hero_image.alt | escape }}"
>
```

2. **Preload Critical Resources:**
```liquid
<link rel="preload" as="image" href="{{ hero_image | image_url: width: 1920 }}">
<link rel="preload" as="font" href="{{ 'font.woff2' | asset_url }}" type="font/woff2" crossorigin>
```

3. **Optimize Font Loading:**
```css
@font-face {
  font-family: 'CustomFont';
  src: url('font.woff2') format('woff2');
  font-display: swap; /* Prevent invisible text */
}
```

### First Input Delay (FID)

**Target: < 100 milliseconds**

FID measures interactivity and responsiveness.

**Optimization Strategies:**

1. **Minimize JavaScript Execution:**
- Remove unused JavaScript libraries
- Defer non-critical scripts
- Use native browser features instead of libraries

2. **Code Splitting:**
```javascript
// Load features on demand
const loadQuickView = async () => {
  const { QuickView } = await import('./quick-view.js');
  return new QuickView();
};

document.querySelectorAll('.quick-view-btn').forEach(btn => {
  btn.addEventListener('click', async () => {
    const quickView = await loadQuickView();
    quickView.open();
  });
});
```

3. **Optimize Event Listeners:**
```javascript
// Use event delegation instead of multiple listeners
document.querySelector('.product-grid').addEventListener('click', (e) => {
  if (e.target.matches('.add-to-cart')) {
    handleAddToCart(e.target);
  }
});
```

### Cumulative Layout Shift (CLS)

**Target: < 0.1**

CLS measures visual stability.

**Optimization Strategies:**

1. **Specify Image Dimensions:**
```liquid
{% assign image_height = image.width | divided_by: image.aspect_ratio | round %}
<img
  src="{{ image | image_url: width: 800 }}"
  width="800"
  height="{{ image_height }}"
  alt="{{ image.alt }}"
>
```

2. **Reserve Space for Dynamic Content:**
```css
.product-card {
  min-height: 400px; /* Prevent layout shift when content loads */
}

.skeleton-loader {
  width: 100%;
  height: 300px;
  background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
  background-size: 200% 100%;
  animation: loading 1.5s infinite;
}
```

3. **Avoid Inserting Content Above Existing Content:**
```javascript
// Bad: Inserting at top causes shift
document.querySelector('.content').prepend(newElement);

// Good: Append or use fixed positioning
document.querySelector('.content').append(newElement);
```

## Asset Optimization

### Image Optimization

**Compression Techniques:**

1. **Use Shopify's Image Filters:**
```liquid
{%- # Automatic format conversion and optimization -%}
<img src="{{ product.featured_image | image_url: width: 800, format: 'pjpg' }}" alt="{{ product.title }}">
```

2. **Responsive Images:**
```liquid
<picture>
  <source
    media="(max-width: 749px)"
    srcset="
      {{ image | image_url: width: 375 }} 375w,
      {{ image | image_url: width: 750 }} 750w
    "
    sizes="100vw"
  >
  <source
    media="(min-width: 750px)"
    srcset="
      {{ image | image_url: width: 800 }} 800w,
      {{ image | image_url: width: 1200 }} 1200w,
      {{ image | image_url: width: 1600 }} 1600w
    "
    sizes="50vw"
  >
  <img
    src="{{ image | image_url: width: 800 }}"
    alt="{{ image.alt }}"
    loading="lazy"
  >
</picture>
```

3. **Lazy Loading Implementation:**
```liquid
{% for product in collection.products %}
  {% assign loading = 'lazy' %}
  {% if forloop.index <= 4 %}
    {% assign loading = 'eager' %}
  {% endif %}
  
  <img
    src="{{ product.featured_image | image_url: width: 400 }}"
    loading="{{ loading }}"
    alt="{{ product.title }}"
  >
{% endfor %}
```

### CSS Optimization

**Critical CSS Extraction:**

1. **Inline Critical CSS:**
```liquid
<style>
  /* Critical above-the-fold styles */
  body { margin: 0; font-family: sans-serif; }
  .header { background: #000; color: #fff; }
  .hero { min-height: 500px; }
</style>

<link rel="stylesheet" href="{{ 'theme.css' | asset_url }}" media="print" onload="this.media='all'">
```

2. **Remove Unused CSS:**
```bash
# Use PurgeCSS to remove unused styles
npx purgecss --css theme.css --content *.liquid --output optimized.css
```

3. **CSS Minification:**
```css
/* Before: 50KB */
.product-card {
  display: flex;
  flex-direction: column;
  padding: 1rem;
}

/* After minification: 35KB */
.product-card{display:flex;flex-direction:column;padding:1rem}
```

### JavaScript Optimization

**Code Splitting and Lazy Loading:**

```javascript
// Load modules on interaction
const initializeCart = () => {
  import('./cart.js').then(module => {
    module.initCart();
  });
};

// Trigger on first cart interaction
document.querySelector('.cart-icon').addEventListener('click', initializeCart, { once: true });
```

**Debouncing and Throttling:**

```javascript
// Debounce search input
const debounce = (func, delay) => {
  let timeoutId;
  return (...args) => {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => func(...args), delay);
  };
};

const searchInput = document.querySelector('#search');
searchInput.addEventListener('input', debounce((e) => {
  performSearch(e.target.value);
}, 300));

// Throttle scroll events
const throttle = (func, limit) => {
  let inThrottle;
  return (...args) => {
    if (!inThrottle) {
      func(...args);
      inThrottle = true;
      setTimeout(() => inThrottle = false, limit);
    }
  };
};

window.addEventListener('scroll', throttle(() => {
  updateScrollPosition();
}, 100));
```

## Caching Strategies

### Browser Caching

**Leverage Asset Versioning:**

```liquid
{%- # Shopify automatically versions assets -%}
<link rel="stylesheet" href="{{ 'theme.css' | asset_url }}">
{%- # Outputs: theme.css?v=123456789 -%}
```

### Service Worker Caching

**Implement Progressive Web App (PWA):**

```javascript
// service-worker.js
const CACHE_NAME = 'shopify-theme-v1';
const urlsToCache = [
  '/',
  '/collections/all',
  '/cart',
  '/assets/theme.css',
  '/assets/theme.js'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(urlsToCache))
  );
});

self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request)
      .then(response => response || fetch(event.request))
  );
});
```

### API Response Caching

**Cache Shopify API Responses:**

```javascript
const cache = new Map();
const CACHE_DURATION = 5 * 60 * 1000; // 5 minutes

async function fetchProductWithCache(productId) {
  const cacheKey = `product-${productId}`;
  const cached = cache.get(cacheKey);
  
  if (cached && Date.now() - cached.timestamp < CACHE_DURATION) {
    return cached.data;
  }
  
  const response = await fetch(`/products/${productId}.js`);
  const data = await response.json();
  
  cache.set(cacheKey, {
    data,
    timestamp: Date.now()
  });
  
  return data;
}
```

## Database Query Optimization

### Efficient Liquid Queries

**Minimize Object Access:**

```liquid
{%- # Bad: Multiple queries -%}
{% for product in collection.products %}
  {{ product.title }}
  {{ product.vendor }}
  {{ product.price }}
{% endfor %}

{%- # Good: Single query with assignment -%}
{% assign products = collection.products %}
{% for product in products %}
  {{ product.title }}
  {{ product.vendor }}
  {{ product.price }}
{% endfor %}
```

**Use Limits Appropriately:**

```liquid
{%- # Only fetch what you need -%}
{% assign featured_products = collection.products | limit: 4 %}

{%- # Pagination for large sets -%}
{% paginate collection.products by 24 %}
  {% for product in collection.products %}
    {%- # Process products -%}
  {% endfor %}
{% endpaginate %}
```

### Avoid N+1 Queries

```liquid
{%- # Bad: Queries in loop -%}
{% for product in collection.products %}
  {% for variant in product.variants %}
    {{ variant.price }}
  {% endfor %}
{% endfor %}

{%- # Good: Preload related data -%}
{% assign products_with_variants = collection.products %}
{% for product in products_with_variants %}
  {% assign variants = product.variants %}
  {% for variant in variants %}
    {{ variant.price }}
  {% endfor %}
{% endfor %}
```

## Third-Party Script Management

### Async and Defer Loading

```liquid
{%- # Defer non-critical scripts -%}
<script src="{{ 'analytics.js' | asset_url }}" defer></script>

{%- # Async for independent scripts -%}
<script src="https://cdn.example.com/widget.js" async></script>
```

### Script Loading Strategies

**Load Scripts on Interaction:**

```javascript
// Load chat widget only when user shows intent
let chatLoaded = false;

const loadChat = () => {
  if (chatLoaded) return;
  
  const script = document.createElement('script');
  script.src = 'https://cdn.chat.com/widget.js';
  document.body.appendChild(script);
  chatLoaded = true;
};

// Trigger on scroll, mouse movement, or timeout
window.addEventListener('scroll', loadChat, { once: true });
window.addEventListener('mousemove', loadChat, { once: true });
setTimeout(loadChat, 5000);
```

### Tag Manager Optimization

```javascript
// Load Google Tag Manager efficiently
window.dataLayer = window.dataLayer || [];

const loadGTM = () => {
  (function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
  new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
  j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
  'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
  })(window,document,'script','dataLayer','GTM-XXXXXX');
};

// Load after page is interactive
if (document.readyState === 'complete') {
  loadGTM();
} else {
  window.addEventListener('load', loadGTM);
}
```

## Mobile Performance

### Mobile-First Optimization

**Responsive Images for Mobile:**

```liquid
<img
  src="{{ image | image_url: width: 375 }}"
  srcset="
    {{ image | image_url: width: 375 }} 375w,
    {{ image | image_url: width: 750 }} 750w,
    {{ image | image_url: width: 1100 }} 1100w
  "
  sizes="(max-width: 749px) 100vw, (max-width: 999px) 50vw, 33vw"
  alt="{{ image.alt }}"
>
```

**Touch-Optimized Interactions:**

```css
/* Larger touch targets for mobile */
.button {
  min-height: 44px;
  min-width: 44px;
  padding: 12px 24px;
}

/* Prevent tap highlight flash */
* {
  -webkit-tap-highlight-color: transparent;
}

/* Smooth scrolling on iOS */
.scrollable {
  -webkit-overflow-scrolling: touch;
}
```

### Network-Aware Loading

```javascript
// Detect connection speed and adjust loading
if ('connection' in navigator) {
  const connection = navigator.connection;
  
  if (connection.effectiveType === '4g') {
    // Load high-quality images
    loadHighQualityImages();
  } else {
    // Load optimized images
    loadOptimizedImages();
  }
  
  if (connection.saveData) {
    // User has data saver enabled
    disableAutoplay();
    loadMinimalAssets();
  }
}
```

## Performance Monitoring

### Real User Monitoring (RUM)

```javascript
// Track Core Web Vitals
import {getCLS, getFID, getLCP} from 'web-vitals';

function sendToAnalytics(metric) {
  const body = JSON.stringify(metric);
  
  // Use `navigator.sendBeacon()` if available, falling back to `fetch()`
  if (navigator.sendBeacon) {
    navigator.sendBeacon('/analytics', body);
  } else {
    fetch('/analytics', {body, method: 'POST', keepalive: true});
  }
}

getCLS(sendToAnalytics);
getFID(sendToAnalytics);
getLCP(sendToAnalytics);
```

### Performance Budgets

**Set and Monitor Budgets:**

```json
{
  "budgets": [
    {
      "resourceType": "script",
      "budget": 300
    },
    {
      "resourceType": "image",
      "budget": 500
    },
    {
      "resourceType": "total",
      "budget": 1000
    },
    {
      "metric": "interactive",
      "budget": 3000
    },
    {
      "metric": "first-contentful-paint",
      "budget": 1500
    }
  ]
}
```

### Lighthouse CI Integration

```yaml
# .github/workflows/lighthouse.yml
name: Lighthouse CI

on: [pull_request]

jobs:
  lighthouse:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run Lighthouse CI
        uses: treosh/lighthouse-ci-action@v8
        with:
          urls: |
            https://test-store.myshopify.com
            https://test-store.myshopify.com/collections/all
            https://test-store.myshopify.com/products/example
          uploadArtifacts: true
          temporaryPublicStorage: true
```

## Advanced Optimization Techniques

### Resource Hints

```liquid
{%- # DNS prefetch for external domains -%}
<link rel="dns-prefetch" href="https://cdn.shopify.com">
<link rel="dns-prefetch" href="https://fonts.googleapis.com">

{%- # Preconnect for critical third-party origins -%}
<link rel="preconnect" href="https://cdn.shopify.com" crossorigin>

{%- # Prefetch next likely navigation -%}
<link rel="prefetch" href="{{ collection.url }}">

{%- # Preload critical resources -%}
<link rel="preload" as="style" href="{{ 'theme.css' | asset_url }}">
<link rel="preload" as="script" href="{{ 'theme.js' | asset_url }}">
```

### HTTP/2 Server Push

```liquid
{%- # Shopify automatically uses HTTP/2 -%}
{%- # Optimize by reducing number of requests -%}
<link rel="stylesheet" href="{{ 'theme.css' | asset_url }}">
<script src="{{ 'theme.js' | asset_url }}" defer></script>
```

### Intersection Observer for Lazy Loading

```javascript
// Lazy load images when they enter viewport
const imageObserver = new IntersectionObserver((entries, observer) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const img = entry.target;
      img.src = img.dataset.src;
      img.classList.remove('lazy');
      observer.unobserve(img);
    }
  });
});

document.querySelectorAll('img.lazy').forEach(img => {
  imageObserver.observe(img);
});
```

### Request Animation Frame for Smooth Animations

```javascript
// Smooth scroll animation
function smoothScroll(target) {
  const targetPosition = target.offsetTop;
  const startPosition = window.pageYOffset;
  const distance = targetPosition - startPosition;
  const duration = 1000;
  let start = null;
  
  function animation(currentTime) {
    if (start === null) start = currentTime;
    const timeElapsed = currentTime - start;
    const run = ease(timeElapsed, startPosition, distance, duration);
    window.scrollTo(0, run);
    if (timeElapsed < duration) requestAnimationFrame(animation);
  }
  
  function ease(t, b, c, d) {
    t /= d / 2;
    if (t < 1) return c / 2 * t * t + b;
    t--;
    return -c / 2 * (t * (t - 2) - 1) + b;
  }
  
  requestAnimationFrame(animation);
}
```