---
name: "mobile-first-progressive-web-apps"
description: "Design and develop mobile-first websites and Progressive Web Apps (PWAs). Use for: creating responsive mobile layouts, implementing PWA features (offline support, service workers, push notifications, installability), optimizing mobile performance, designing touch-friendly interfaces, implementing mobile navigation patterns, building app-like web experiences, configuring web app manifests, caching strategies, and mobile UX optimization."
---

# Mobile-First & Progressive Web Apps

Design mobile-first responsive experiences and build Progressive Web Apps with offline capabilities, installability, and native-like features.

## Overview

Mobile-first design prioritizes the mobile experience, then progressively enhances for larger screens. PWAs combine web reach with native app capabilities—offline access, push notifications, and home screen installation—using modern web technologies.

## Why Mobile-First Matters

- **60%+ of web traffic** originates from mobile devices
- **Mobile-first indexing**: Google prioritizes mobile versions for ranking
- **Performance by default**: Mobile constraints force efficient, lean code
- **User expectations**: Poor mobile experiences lose 61% of users permanently

## Mobile-First vs Desktop-First

| Aspect | Mobile-First | Desktop-First |
|--------|-------------|---------------|
| Starting Point | 320px screens | 1200px+ screens |
| CSS Approach | `min-width` media queries | `max-width` media queries |
| Content Strategy | Essential content first | Full content, then remove |
| Performance | Optimized by default | Optimization as afterthought |
| Philosophy | Progressive enhancement | Graceful degradation |

## Core Mobile-First Principles

1. **Content Prioritization** — Surface essential content first, use progressive disclosure
2. **Touch-Friendly Design** — Minimum 44x44px touch targets, 8px spacing between elements
3. **Thumb Zone Awareness** — Primary actions in bottom center (easy reach zone)
4. **Performance Obsession** — Target <1.8s FCP, <2.5s LCP, <100ms FID
5. **Simplified Navigation** — Bottom nav for primary actions, hamburger for secondary

## Responsive Design Quick Reference

```css
/* Mobile-first breakpoints */
/* Mobile: base styles (no query needed) */

@media (min-width: 768px) {  /* Tablet */
  .container { max-width: 750px; }
}

@media (min-width: 1024px) { /* Desktop */
  .container { max-width: 960px; }
}

@media (min-width: 1200px) { /* Large desktop */
  .container { max-width: 1140px; }
}
```

## Common Breakpoints

| Category | Width Range | Devices |
|----------|-------------|---------|
| Small Mobile | 320-375px | iPhone SE, small Android |
| Mobile | 376-480px | Standard smartphones |
| Tablet | 481-768px | iPad Mini, portrait tablets |
| Large Tablet | 769-1024px | iPad, landscape tablets |
| Desktop | 1025-1200px | Laptops, small monitors |
| Large Desktop | 1201px+ | Large monitors |

## Mobile Navigation Patterns

| Pattern | Best For | Pros | Cons |
|---------|----------|------|------|
| Bottom Navigation | Primary destinations (3-5 items) | Thumb-friendly, always visible | Limited items |
| Hamburger Menu | Secondary navigation, deep hierarchies | Space-efficient | Low discoverability |
| Tab Bar | Content switching | Clear, persistent | Limited flexibility |
| Priority+ | Mixed importance navigation | Adaptive | Complexity |

## Touch Target Guidelines

- **Minimum size**: 44x44px (Apple HIG) / 48x48dp (Material Design)
- **Spacing**: 8px minimum between targets
- **Primary actions**: Consider 56x56px or larger
- **Thumb zones**: Bottom center = easy, top corners = hard

## PWA vs Native Apps

| Feature | PWA | Native App |
|---------|-----|------------|
| Distribution | Direct from web | App store required |
| Updates | Instant, automatic | User must update |
| Development | Web technologies | Platform-specific |
| Cross-platform | Single codebase | Multiple codebases |
| Device Access | Growing (camera, GPS, notifications) | Full access |
| Offline Support | Service worker caching | Native storage |
| Size | KB to small MB | Large MB to GB |

## PWA Requirements

1. **HTTPS** — Secure connection required
2. **Service Worker** — Enables offline, caching, background sync
3. **Web App Manifest** — JSON file with app metadata
4. **Responsive Design** — Works across all screen sizes

## Service Worker Caching Strategies

| Strategy | Use Case | Behavior |
|----------|----------|----------|
| Cache-First | Static assets, fonts | Check cache first, network fallback |
| Network-First | Dynamic content, APIs | Network first, cache fallback |
| Stale-While-Revalidate | Frequently updated content | Serve cached, update in background |
| Network-Only | Non-cacheable requests | Always fetch from network |
| Cache-Only | Precached assets | Only serve from cache |

## Web App Manifest Essentials

```json
{
  "name": "App Full Name",
  "short_name": "AppName",
  "start_url": "/",
  "display": "standalone",
  "theme_color": "#3367D6",
  "background_color": "#FFFFFF",
  "icons": [
    { "src": "/icons/192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "/icons/512.png", "sizes": "512x512", "type": "image/png" }
  ]
}
```

**Display Modes**: `fullscreen` | `standalone` | `minimal-ui` | `browser`

## Performance Targets

| Metric | Good | Needs Work | Poor |
|--------|------|------------|------|
| First Contentful Paint (FCP) | <1.8s | 1.8-3.0s | >3.0s |
| Largest Contentful Paint (LCP) | <2.5s | 2.5-4.0s | >4.0s |
| Cumulative Layout Shift (CLS) | <0.1 | 0.1-0.25 | >0.25 |
| First Input Delay (FID) | <100ms | 100-300ms | >300ms |
| Time to Interactive (TTI) | <3.8s | 3.8-7.3s | >7.3s |

## PWA Checklist

- [ ] Served over HTTPS
- [ ] Responsive across devices
- [ ] Works offline (service worker + caching)
- [ ] Valid web app manifest with icons
- [ ] Fast first load on 3G (<3s)
- [ ] Cross-browser compatible
- [ ] Custom install prompt implemented
- [ ] Offline fallback page

## Tools and Frameworks

| Category | Tools |
|----------|-------|
| Service Workers | Workbox (Google), vanilla SW |
| PWA Builders | PWABuilder (Microsoft), Next.js, Nuxt.js |
| Testing | Lighthouse, Chrome DevTools, WebPageTest |
| Cross-Device | BrowserStack, Sauce Labs, LambdaTest |
| Performance | PageSpeed Insights, WebPageTest |

## Common Mistakes to Avoid

**Mobile Design**:
- Touch targets below 44x44px
- Text smaller than 16px base
- Horizontal scrolling on mobile
- Hover-dependent interactions without touch alternatives

**PWA**:
- No offline fallback (blank page when offline)
- Aggressive permission requests on first visit
- Not updating service worker caches
- Missing custom install prompt

## Using the Reference Files

### When to Read Each Reference

**`/references/mobile-first-design.md`** — Read when implementing mobile-first design principles, content prioritization strategies, typography guidelines, or spacing systems.

**`/references/responsive-breakpoints.md`** — Read when setting up responsive layouts, choosing between responsive and adaptive approaches, or implementing media query strategies.

**`/references/mobile-ux-touch.md`** — Read when designing mobile navigation, implementing touch gestures, creating mobile forms, or optimizing for thumb zones.

**`/references/pwa-core.md`** — Read when implementing service workers, understanding PWA architecture, setting up offline functionality, or implementing caching strategies.

**`/references/pwa-implementation.md`** — Read when configuring web app manifests, implementing install prompts, setting up push notifications, or distributing PWAs to app stores.

**`/references/performance-testing.md`** — Read when optimizing mobile performance, running Lighthouse audits, debugging on real devices, or measuring Core Web Vitals.
