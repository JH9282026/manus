# Web Performance Optimization

## Introduction to Web Performance

Web performance directly impacts user experience, conversion rates, SEO rankings, and business success. Studies show that:

- 53% of mobile users abandon sites that take longer than 3 seconds to load
- A 1-second delay in page load time can reduce conversions by 7%
- Google uses page speed as a ranking factor
- Faster sites have better engagement and lower bounce rates

### Core Web Vitals

Google's Core Web Vitals are key metrics for measuring user experience:

1. **Largest Contentful Paint (LCP)**: Loading performance (< 2.5s)
2. **First Input Delay (FID)**: Interactivity (< 100ms)
3. **Cumulative Layout Shift (CLS)**: Visual stability (< 0.1)

## Loading Performance

### Critical Rendering Path Optimization

#### Minimize Critical Resources

```html
<!-- Inline critical CSS -->
<style>
  /* Above-the-fold styles */
  body { margin: 0; font-family: sans-serif; }
  .header { background: #333; color: white; padding: 1rem; }
</style>

<!-- Defer non-critical CSS -->
<link rel="preload" href="styles.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="styles.css"></noscript>

<!-- Async JavaScript -->
<script src="analytics.js" async></script>

<!-- Defer JavaScript -->
<script src="app.js" defer></script>
```

#### Resource Hints

```html
<!-- DNS Prefetch -->
<link rel="dns-prefetch" href="//fonts.googleapis.com">

<!-- Preconnect -->
<link rel="preconnect" href="https://api.example.com">

<!-- Prefetch (low priority) -->
<link rel="prefetch" href="/next-page.html">

<!-- Preload (high priority) -->
<link rel="preload" href="hero-image.jpg" as="image">
<link rel="preload" href="font.woff2" as="font" type="font/woff2" crossorigin>

<!-- Prerender (speculative) -->
<link rel="prerender" href="/likely-next-page.html">
```

### Image Optimization

#### Modern Image Formats

```html
<!-- WebP with fallback -->
<picture>
  <source srcset="image.avif" type="image/avif">
  <source srcset="image.webp" type="image/webp">
  <img src="image.jpg" alt="Description" loading="lazy">
</picture>

<!-- Responsive images -->
<img
  src="image-800.jpg"
  srcset="
    image-400.jpg 400w,
    image-800.jpg 800w,
    image-1200.jpg 1200w,
    image-1600.jpg 1600w
  "
  sizes="
    (max-width: 600px) 100vw,
    (max-width: 1000px) 80vw,
    1200px
  "
  alt="Responsive image"
  loading="lazy"
  decoding="async"
/>
```

#### Lazy Loading

```html
<!-- Native lazy loading -->
<img src="image.jpg" loading="lazy" alt="Description">

<!-- Intersection Observer for custom lazy loading -->
<img data-src="image.jpg" class="lazy" alt="Description">
```

```javascript
// Intersection Observer lazy loading
const lazyImages = document.querySelectorAll('.lazy');

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

lazyImages.forEach(img => imageObserver.observe(img));
```

#### Image Compression

```bash
# ImageOptim, TinyPNG, or CLI tools

# WebP conversion
cwebp -q 80 input.jpg -o output.webp

# AVIF conversion
avifenc --min 0 --max 63 -a end-usage=q -a cq-level=18 input.jpg output.avif

# Optimize JPEG
jpegoptim --max=85 --strip-all image.jpg

# Optimize PNG
optipng -o7 image.png
```

### Font Optimization

#### Font Loading Strategies

```css
/* Font display strategies */
@font-face {
  font-family: 'CustomFont';
  src: url('font.woff2') format('woff2');
  font-display: swap; /* Show fallback immediately, swap when loaded */
  /* Other options: auto, block, fallback, optional */
}

/* Preload critical fonts */
```

```html
<link rel="preload" href="font.woff2" as="font" type="font/woff2" crossorigin>
```

#### Variable Fonts

```css
@font-face {
  font-family: 'InterVariable';
  src: url('Inter-Variable.woff2') format('woff2');
  font-weight: 100 900; /* Variable weight range */
  font-display: swap;
}

body {
  font-family: 'InterVariable', sans-serif;
  font-weight: 400;
}

h1 {
  font-weight: 700;
}
```

### Code Splitting

#### Dynamic Imports

```javascript
// Route-based code splitting
const routes = [
  {
    path: '/dashboard',
    component: () => import('./views/Dashboard.vue')
  },
  {
    path: '/profile',
    component: () => import('./views/Profile.vue')
  }
];

// Component-based code splitting
const HeavyComponent = lazy(() => import('./HeavyComponent'));

// Conditional loading
if (condition) {
  import('./module.js').then(module => {
    module.init();
  });
}
```

#### Webpack Configuration

```javascript
// webpack.config.js
module.exports = {
  optimization: {
    splitChunks: {
      chunks: 'all',
      cacheGroups: {
        vendor: {
          test: /[\\/]node_modules[\\/]/,
          name: 'vendors',
          priority: 10
        },
        common: {
          minChunks: 2,
          priority: 5,
          reuseExistingChunk: true
        }
      }
    },
    runtimeChunk: 'single'
  }
};
```

## Runtime Performance

### JavaScript Optimization

#### Debouncing and Throttling

```javascript
// Debounce: Wait for pause in events
function debounce(func, wait) {
  let timeout;
  return function executedFunction(...args) {
    const later = () => {
      clearTimeout(timeout);
      func(...args);
    };
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
  };
}

// Usage
const handleSearch = debounce((query) => {
  fetchResults(query);
}, 300);

input.addEventListener('input', (e) => handleSearch(e.target.value));

// Throttle: Limit execution rate
function throttle(func, limit) {
  let inThrottle;
  return function(...args) {
    if (!inThrottle) {
      func.apply(this, args);
      inThrottle = true;
      setTimeout(() => inThrottle = false, limit);
    }
  };
}

// Usage
const handleScroll = throttle(() => {
  console.log('Scroll position:', window.scrollY);
}, 200);

window.addEventListener('scroll', handleScroll);
```

#### Web Workers

```javascript
// main.js
const worker = new Worker('worker.js');

worker.postMessage({ data: largeDataset });

worker.onmessage = (e) => {
  console.log('Result:', e.data);
};

// worker.js
self.onmessage = (e) => {
  const result = processData(e.data);
  self.postMessage(result);
};

function processData(data) {
  // Heavy computation
  return data.map(item => item * 2);
}
```

#### RequestAnimationFrame

```javascript
// Smooth animations
function animate() {
  // Update animation
  element.style.transform = `translateX(${position}px)`;
  
  if (position < targetPosition) {
    position += speed;
    requestAnimationFrame(animate);
  }
}

requestAnimationFrame(animate);

// Batch DOM reads and writes
function updateLayout() {
  // Read
  const height = element.offsetHeight;
  
  // Write
  requestAnimationFrame(() => {
    element.style.height = `${height * 2}px`;
  });
}
```

### CSS Performance

#### Efficient Selectors

```css
/* Good: Simple, specific selectors */
.button { }
.card-title { }
#header { }

/* Bad: Overly complex selectors */
div > div > div > p { }
body div.container ul li a { }
* { } /* Universal selector */
```

#### CSS Containment

```css
.card {
  contain: layout style paint;
  /* Isolates element for better performance */
}

.sidebar {
  contain: size layout;
  /* Size won't affect other elements */
}
```

#### GPU Acceleration

```css
/* Use transform and opacity for animations */
.element {
  transform: translateX(0);
  transition: transform 0.3s ease;
}

.element:hover {
  transform: translateX(100px);
}

/* Avoid animating layout properties */
/* Bad */
.element {
  transition: left 0.3s ease;
}

.element:hover {
  left: 100px; /* Triggers layout */
}
```

## Caching Strategies

### HTTP Caching

```nginx
# nginx configuration
location ~* \.(jpg|jpeg|png|gif|ico|css|js|woff2)$ {
  expires 1y;
  add_header Cache-Control "public, immutable";
}

location ~* \.(html)$ {
  expires -1;
  add_header Cache-Control "no-cache, no-store, must-revalidate";
}
```

### Service Worker Caching

```javascript
// service-worker.js
const CACHE_NAME = 'v1';
const urlsToCache = [
  '/',
  '/styles.css',
  '/app.js',
  '/logo.png'
];

// Install
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(urlsToCache))
  );
});

// Fetch
self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        // Cache hit - return response
        if (response) {
          return response;
        }
        
        // Clone request
        const fetchRequest = event.request.clone();
        
        return fetch(fetchRequest).then(response => {
          // Check if valid response
          if (!response || response.status !== 200 || response.type !== 'basic') {
            return response;
          }
          
          // Clone response
          const responseToCache = response.clone();
          
          caches.open(CACHE_NAME)
            .then(cache => {
              cache.put(event.request, responseToCache);
            });
          
          return response;
        });
      })
  );
});

// Activate
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cacheName => {
          if (cacheName !== CACHE_NAME) {
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});
```

## Monitoring and Measurement

### Performance APIs

```javascript
// Navigation Timing
const perfData = performance.getEntriesByType('navigation')[0];
console.log('DNS lookup:', perfData.domainLookupEnd - perfData.domainLookupStart);
console.log('TCP connection:', perfData.connectEnd - perfData.connectStart);
console.log('Request time:', perfData.responseStart - perfData.requestStart);
console.log('Response time:', perfData.responseEnd - perfData.responseStart);
console.log('DOM processing:', perfData.domComplete - perfData.domLoading);

// Resource Timing
const resources = performance.getEntriesByType('resource');
resources.forEach(resource => {
  console.log(`${resource.name}: ${resource.duration}ms`);
});

// User Timing
performance.mark('start-task');
// ... perform task
performance.mark('end-task');
performance.measure('task-duration', 'start-task', 'end-task');

const measure = performance.getEntriesByName('task-duration')[0];
console.log('Task took:', measure.duration, 'ms');

// Core Web Vitals
import { getCLS, getFID, getLCP } from 'web-vitals';

getCLS(console.log);
getFID(console.log);
getLCP(console.log);
```

### Lighthouse CI

```yaml
# .lighthouserc.json
{
  "ci": {
    "collect": {
      "numberOfRuns": 3,
      "url": [
        "http://localhost:3000/",
        "http://localhost:3000/about"
      ]
    },
    "assert": {
      "assertions": {
        "categories:performance": ["error", {"minScore": 0.9}],
        "categories:accessibility": ["error", {"minScore": 0.9}],
        "first-contentful-paint": ["error", {"maxNumericValue": 2000}],
        "largest-contentful-paint": ["error", {"maxNumericValue": 2500}],
        "cumulative-layout-shift": ["error", {"maxNumericValue": 0.1}]
      }
    },
    "upload": {
      "target": "temporary-public-storage"
    }
  }
}
```

## Best Practices Checklist

### Loading
- ✅ Minimize HTTP requests
- ✅ Enable compression (gzip/brotli)
- ✅ Optimize images (WebP/AVIF, lazy loading)
- ✅ Minify CSS, JavaScript, HTML
- ✅ Use CDN for static assets
- ✅ Implement code splitting
- ✅ Defer non-critical JavaScript
- ✅ Inline critical CSS
- ✅ Preload critical resources
- ✅ Use HTTP/2 or HTTP/3

### Runtime
- ✅ Minimize JavaScript execution time
- ✅ Avoid layout thrashing
- ✅ Use CSS containment
- ✅ Implement virtual scrolling for long lists
- ✅ Debounce/throttle event handlers
- ✅ Use Web Workers for heavy computation
- ✅ Optimize animations (transform/opacity)
- ✅ Reduce DOM size

### Caching
- ✅ Implement service worker
- ✅ Set appropriate cache headers
- ✅ Use versioned URLs for assets
- ✅ Implement offline support

### Monitoring
- ✅ Track Core Web Vitals
- ✅ Set performance budgets
- ✅ Monitor real user metrics (RUM)
- ✅ Regular Lighthouse audits
- ✅ Implement error tracking

## Conclusion

Web performance optimization is crucial for user experience and business success. Key strategies include:

1. **Loading**: Optimize critical rendering path, images, and fonts
2. **Runtime**: Efficient JavaScript and CSS, GPU acceleration
3. **Caching**: HTTP caching and service workers
4. **Monitoring**: Track metrics and set budgets
5. **Continuous**: Performance is an ongoing process

By implementing these techniques and regularly monitoring performance, you can create fast, responsive web experiences that delight users and drive business results.
