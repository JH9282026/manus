---
name: mobile-first-pwa
description: "Design and build mobile-first websites and Progressive Web Apps (PWAs). Use for: responsive mobile design, PWA architecture, service worker implementation, offline functionality, app manifest configuration, mobile performance optimization, push notifications, and installable web applications."
---

# Mobile-First & PWA Development

Design and build mobile-first responsive websites and Progressive Web Apps that deliver native-like experiences through the browser.

## Overview

Mobile devices account for 60%+ of web traffic. Mobile-first design starts with the smallest screen and progressively enhances for larger devices — the inverse of the traditional desktop-first approach. Progressive Web Apps (PWAs) extend mobile web with offline support, push notifications, and home screen installation. This skill covers mobile-first design methodology, responsive patterns, PWA architecture, service workers, and performance optimization for mobile devices.

## Mobile-First Design Methodology

### Breakpoint Strategy

| Breakpoint | Target | CSS Approach | Design Focus |
|-----------|--------|-------------|-------------|
| 0–479px | Small phones | Base styles (no media query) | Single column, stacked layout |
| 480–767px | Large phones | `@media (min-width: 480px)` | Wider cards, adjusted spacing |
| 768–1023px | Tablets | `@media (min-width: 768px)` | 2-column layouts, side navigation |
| 1024–1279px | Small desktops | `@media (min-width: 1024px)` | Full navigation, multi-column |
| 1280px+ | Large desktops | `@media (min-width: 1280px)` | Max-width container, expanded layouts |

### Mobile-First Design Rules

| Rule | Implementation | Why |
|------|---------------|-----|
| Design small screen first | Start Figma/Sketch at 375px width | Forces priority decisions |
| Content hierarchy before layout | Define content order, then arrange | Most important content first |
| Touch targets ≥48×48px | Buttons, links, interactive elements | Apple HIG and WCAG requirement |
| Thumb-zone awareness | Place primary actions in bottom 40% | One-handed usability |
| System fonts for performance | `-apple-system, system-ui, sans-serif` | Zero font loading delay |
| Reduced motion option | `@media (prefers-reduced-motion)` | Accessibility requirement |

## Responsive Layout Patterns

| Pattern | Description | Best For | Reference |
|---------|-------------|----------|-----------|
| Stacked → Grid | Single column on mobile, grid on desktop | Card layouts, dashboards | `/references/responsive-patterns.md` |
| Off-canvas navigation | Hidden sidebar, slide-in on mobile | Complex navigation, admin UIs | `/references/responsive-patterns.md` |
| Priority+ navigation | Show most important links, overflow to menu | Many nav items | `/references/responsive-patterns.md` |
| Responsive tables | Horizontal scroll or card-style on mobile | Data-heavy content | `/references/responsive-patterns.md` |
| Container queries | Components adapt to parent width, not viewport | Reusable components | `/references/responsive-patterns.md` |
| Fluid typography | `clamp()` for smooth font scaling | All text content | `/references/responsive-patterns.md` |

## PWA Architecture

### PWA Requirements Checklist

| Requirement | Implementation | Purpose |
|------------|---------------|---------|
| HTTPS | SSL certificate on all pages | Security, required for service workers |
| Web App Manifest | `manifest.json` linked in HTML | Installability metadata |
| Service Worker | Registered in main JS | Offline support, caching, push |
| Responsive design | Mobile-first CSS | Works on all screen sizes |
| Offline page | Cached fallback page | Graceful offline experience |
| App icons | 192×192 and 512×512 PNG | Home screen and splash screen |
| Start URL | Defined in manifest | Consistent entry point |

### Web App Manifest Structure

| Field | Value | Required |
|-------|-------|----------|
| name | Full application name | Yes |
| short_name | Abbreviated name (≤12 chars) | Yes |
| start_url | "/" or app entry point | Yes |
| display | "standalone" (no browser chrome) | Yes |
| background_color | Splash screen background | Yes |
| theme_color | Status bar and header color | Yes |
| icons | Array of icon objects with sizes | Yes |
| description | App description | Recommended |
| orientation | "portrait" or "any" | Optional |
| scope | URL scope of the PWA | Recommended |

## Service Worker Strategies

### Caching Strategies

| Strategy | Behavior | Best For | Freshness |
|----------|----------|----------|-----------|
| Cache First | Check cache → fallback to network | Static assets (CSS, JS, images) | Stale until updated |
| Network First | Try network → fallback to cache | API data, dynamic content | Fresh when online |
| Stale While Revalidate | Serve cache immediately → update cache from network | Frequently updated assets | Mostly fresh |
| Cache Only | Only serve from cache | Offline-critical static content | Never updated |
| Network Only | Always go to network | Real-time data, authentication | Always fresh |

### Service Worker Lifecycle

| Phase | Event | Action |
|-------|-------|--------|
| Install | `install` | Pre-cache critical assets (app shell) |
| Activate | `activate` | Clean up old caches |
| Fetch | `fetch` | Intercept network requests, apply caching strategy |
| Push | `push` | Handle push notification |
| Sync | `sync` | Background sync when connection restored |

### What to Cache (Priority)

| Priority | Asset Type | Strategy | Reason |
|----------|-----------|----------|--------|
| Critical | App shell HTML | Cache First | Enables instant load |
| Critical | Core CSS and JS | Cache First | App must function |
| High | Fonts | Cache First | Prevents layout shift |
| High | Key images (logo, icons) | Cache First | Branding consistency |
| Medium | API responses | Stale While Revalidate | Balance freshness and speed |
| Low | User-generated content | Network First | Freshness more important |
| Offline | Fallback page | Cache Only | Graceful offline experience |

## Mobile Performance Optimization

| Metric | Target | Impact | Technique |
|--------|--------|--------|-----------|
| LCP (Largest Contentful Paint) | <2.5s | Core Web Vital | Optimize hero image, preload critical resources |
| FID / INP | <200ms | Core Web Vital | Minimize main thread work, defer non-critical JS |
| CLS | <0.1 | Core Web Vital | Set explicit image dimensions, avoid dynamic injection |
| TTI (Time to Interactive) | <3.5s | Usability | Code-split, lazy load below-fold |
| Total page weight | <500KB initial | Load time on 3G | Compress, tree-shake, lazy load |
| JavaScript size | <150KB compressed | Parse time on mobile CPUs | Split bundles, defer non-critical |

### Mobile-Specific Optimizations
- **Preconnect to critical origins** — `<link rel="preconnect" href="https://api.example.com">`
- **Lazy load images** — native `loading="lazy"` attribute
- **Use responsive images** — `srcset` and `sizes` attributes for proper resolution
- **Minimize third-party scripts** — each script adds DNS lookup + download + parse
- **Compress images to WebP/AVIF** — 25–50% smaller than JPEG at same quality
- **Implement skeleton screens** — perceived performance while loading

## Push Notification Implementation

| Component | Purpose | Implementation |
|-----------|---------|---------------|
| Permission request | Get user consent | `Notification.requestPermission()` — trigger on meaningful action, not page load |
| Subscription | Register with push service | `registration.pushManager.subscribe()` with VAPID key |
| Server-side send | Deliver notification payload | Web Push library (web-push npm, pywebpush) |
| Service worker handler | Display notification | `self.addEventListener('push', ...)` |
| Click handler | Open app on notification tap | `self.addEventListener('notificationclick', ...)` |

## Best Practices

- **Design for the slowest device** — test on a mid-range Android phone on 3G, not your M3 MacBook
- **Cache the app shell** — HTML structure + core CSS + core JS should be available offline
- **Request push permission contextually** — explain value before asking; never on first visit
- **Test install flow** — verify the "Add to Home Screen" banner appears and app opens correctly
- **Monitor service worker updates** — broken service workers can make your site unusable
- **Use Lighthouse CI** — automate PWA and performance auditing in your deployment pipeline

## Using the Reference Files

**`/references/responsive-patterns.md`** — Read when implementing responsive layouts. Covers CSS Grid and Flexbox patterns, container queries, navigation patterns, and responsive component libraries.

**`/references/mobile-ux-performance.md`** — Read when optimizing mobile experience. Covers touch interactions, service worker implementation, caching strategies, push notifications, and performance budgets.
