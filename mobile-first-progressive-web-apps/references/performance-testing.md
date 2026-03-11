# Performance & Testing

Comprehensive guide to mobile performance optimization, Core Web Vitals, testing strategies, and debugging tools.

---

## Mobile Performance Importance

### Why Performance Matters

- **Mobile networks** — Often slower, less reliable than desktop
- **Device constraints** — Limited CPU, memory, battery
- **User expectations** — Fast, responsive experiences expected
- **SEO impact** — Core Web Vitals are ranking factors
- **Conversion rates** — Every second delay costs conversions

### Performance Impact

| Load Time | Bounce Rate Impact |
|-----------|--------------------|
| 1-3 seconds | 32% increase |
| 1-5 seconds | 90% increase |
| 1-6 seconds | 106% increase |
| 1-10 seconds | 123% increase |

---

## Core Web Vitals

### Metrics Overview

| Metric | Description | Good | Needs Work | Poor |
|--------|-------------|------|------------|------|
| FCP (First Contentful Paint) | First content rendered | <1.8s | 1.8-3.0s | >3.0s |
| LCP (Largest Contentful Paint) | Largest element rendered | <2.5s | 2.5-4.0s | >4.0s |
| FID (First Input Delay) | Response to first interaction | <100ms | 100-300ms | >300ms |
| CLS (Cumulative Layout Shift) | Visual stability | <0.1 | 0.1-0.25 | >0.25 |
| TTI (Time to Interactive) | Fully interactive | <3.8s | 3.8-7.3s | >7.3s |
| TBT (Total Blocking Time) | Main thread blocking | <200ms | 200-600ms | >600ms |

### Measuring Core Web Vitals

```javascript
// Using web-vitals library
import { getCLS, getFID, getLCP, getFCP, getTTFB } from 'web-vitals';

function sendToAnalytics(metric) {
  console.log(metric.name, metric.value);
  // Send to your analytics service
}

getCLS(sendToAnalytics);
getFID(sendToAnalytics);
getLCP(sendToAnalytics);
getFCP(sendToAnalytics);
getTTFB(sendToAnalytics);
```

---

## Optimization Techniques

### JavaScript Optimization

```html
<!-- Critical JS inline -->
<script>
  // Critical above-the-fold JS
</script>

<!-- Non-critical JS deferred -->
<script src="non-critical.js" defer></script>

<!-- Analytics async -->
<script src="analytics.js" async></script>
```

**Strategies**:
- Minimize bundle size
- Code split by route
- Tree shake unused code
- Lazy load components
- Use web workers for heavy computation

### CSS Optimization

```html
<!-- Critical CSS inline -->
<style>
  /* Above-the-fold styles */
</style>

<!-- Non-critical CSS deferred -->
<link rel="preload" href="styles.css" as="style" 
      onload="this.onload=null;this.rel='stylesheet'">
```

**Strategies**:
- Inline critical CSS
- Remove unused CSS
- Minimize and compress
- Use efficient selectors

### Image Optimization

```html
<!-- Modern formats with fallbacks -->
<picture>
  <source type="image/avif" srcset="image.avif">
  <source type="image/webp" srcset="image.webp">
  <img src="image.jpg" alt="Description" loading="lazy">
</picture>

<!-- Responsive images -->
<img srcset="small.jpg 480w,
             medium.jpg 768w,
             large.jpg 1200w"
     sizes="(max-width: 480px) 100vw,
            (max-width: 768px) 50vw,
            33vw"
     src="medium.jpg"
     alt="Description"
     loading="lazy"
     decoding="async">
```

**Strategies**:
- Use modern formats (WebP, AVIF)
- Implement responsive images
- Lazy load below-the-fold images
- Specify dimensions to prevent CLS
- Use CDN for delivery

### Network Optimization

```html
<!-- Preconnect to critical origins -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="dns-prefetch" href="https://analytics.example.com">

<!-- Preload critical resources -->
<link rel="preload" href="critical.css" as="style">
<link rel="preload" href="hero.webp" as="image">
```

**Strategies**:
- Enable compression (Gzip, Brotli)
- Use HTTP/2 or HTTP/3
- Implement CDN
- Minimize HTTP requests
- Cache effectively

---

## Mobile-Specific Optimizations

### Reduce Network Dependency

- Service worker caching
- Offline functionality
- Prefetch likely next pages
- Cache API responses

### Reduce CPU Usage

- Minimize JavaScript execution
- Use CSS animations over JS
- Avoid layout thrashing
- Debounce scroll/resize handlers

### Reduce Memory Usage

- Lazy load images
- Clean up event listeners
- Use efficient data structures
- Avoid memory leaks

### Battery Considerations

- Reduce animation on low battery
- Minimize network requests
- Avoid constant polling
- Use efficient background sync

---

## Testing Strategies

### Real Device Testing

Essential for accurate touch, performance, and gesture testing.

**Device Categories to Test**:
- Budget Android phones (1-2GB RAM)
- Mid-range Android (3-4GB RAM)
- Flagship Android
- iPhone SE (smallest iOS)
- iPhone Pro (flagship iOS)
- iPad (tablet)

### Emulators and Simulators

| Tool | Platform | Use Case |
|------|----------|----------|
| Android Studio Emulator | Android | Development, testing |
| Xcode iOS Simulator | iOS | Development, testing |
| Chrome DevTools Device Mode | All | Quick iteration |

### Cloud Testing Services

| Service | Features |
|---------|----------|
| BrowserStack | Real devices, screenshots, debugging |
| Sauce Labs | Automated testing, CI/CD integration |
| LambdaTest | Cross-browser, responsive testing |

---

## Debugging Tools

### Chrome DevTools

**Application Tab**:
- Service worker status and debugging
- Manifest validation
- Cache storage inspection
- IndexedDB inspection
- Clear storage

**Network Tab**:
- Throttle network (3G, offline)
- Analyze request waterfall
- Check cache status
- Identify slow requests

**Performance Tab**:
- Record runtime performance
- Identify long tasks
- Analyze layout shifts
- Profile JavaScript execution

**Lighthouse Tab**:
- PWA audit
- Performance analysis
- Accessibility check
- SEO audit
- Best practices

### Remote Debugging

**Android**:
1. Enable USB debugging on device
2. Connect via USB
3. Navigate to chrome://inspect
4. Click "Inspect" on target page

**iOS**:
1. Enable Web Inspector in Safari settings
2. Connect device via USB
3. Open Safari on macOS
4. Develop menu → Select device

---

## Performance Testing Tools

### Lighthouse

Automated auditing for PWA, performance, accessibility.

```bash
# CLI usage
npm install -g lighthouse
lighthouse https://example.com --view

# With specific categories
lighthouse https://example.com --only-categories=performance,pwa
```

### WebPageTest

Detailed performance analysis with filmstrip view.

**Features**:
- Multiple locations
- Real browsers
- Filmstrip view
- Waterfall analysis
- Core Web Vitals

### PageSpeed Insights

Google's performance analysis tool.

**Features**:
- Field data (real users)
- Lab data (simulated)
- Core Web Vitals
- Optimization suggestions

---

## Testing Checklist

### Responsive Testing

- [ ] Test all breakpoints
- [ ] Portrait and landscape orientations
- [ ] Various viewport sizes
- [ ] Different pixel densities

### Touch Testing

- [ ] Touch targets 44px minimum
- [ ] Gesture interactions work
- [ ] No hover-dependent functionality
- [ ] Pull-to-refresh works

### Offline Testing

- [ ] App loads offline
- [ ] Offline fallback page works
- [ ] Cached content displays
- [ ] Sync resumes when online

### Network Testing

- [ ] Works on 3G networks
- [ ] Handles intermittent connectivity
- [ ] Graceful degradation on slow networks
- [ ] CDN assets load correctly

### Performance Testing

- [ ] FCP < 1.8s on 3G
- [ ] LCP < 2.5s
- [ ] CLS < 0.1
- [ ] TTI < 3.8s

### Cross-Browser Testing

- [ ] Chrome Android
- [ ] Safari iOS
- [ ] Samsung Internet
- [ ] Firefox Mobile
- [ ] Edge Mobile

### PWA Testing

- [ ] Lighthouse PWA audit passes
- [ ] Install prompt appears
- [ ] App installs successfully
- [ ] Splash screen displays
- [ ] Standalone mode works

---

## Common Performance Issues

### Issue: Slow LCP

**Causes**:
- Large hero images
- Render-blocking CSS/JS
- Slow server response

**Solutions**:
- Optimize images
- Preload LCP image
- Inline critical CSS
- Use CDN

### Issue: High CLS

**Causes**:
- Images without dimensions
- Dynamically injected content
- Web fonts causing FOIT/FOUT

**Solutions**:
- Set width/height on images
- Reserve space for dynamic content
- Use font-display: optional

### Issue: Poor FID/TBT

**Causes**:
- Long JavaScript tasks
- Heavy third-party scripts
- Main thread blocking

**Solutions**:
- Code split JavaScript
- Defer non-critical scripts
- Use web workers
- Optimize event handlers

---

## Resources

### Tools

- [Lighthouse](https://developers.google.com/web/tools/lighthouse)
- [WebPageTest](https://www.webpagetest.org/)
- [PageSpeed Insights](https://pagespeed.web.dev/)
- [BrowserStack](https://www.browserstack.com/)

### Documentation

- [web.dev](https://web.dev/) — Google Web Fundamentals
- [MDN Web Docs](https://developer.mozilla.org/) — PWA documentation
- [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/) — iOS guidelines
- [Material Design](https://material.io/) — Android guidelines
