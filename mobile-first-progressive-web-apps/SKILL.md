---
name: "mobile-first-progressive-web-apps"
description: "Design and develop mobile-first responsive websites and Progressive Web Apps with offline capabilities, push notifications, and native-like experiences. Use for: mobile-first design, PWA development, service worker implementation, responsive design, offline-first architecture, app shell pattern, web app manifest configuration."
---

# Mobile-First & Progressive Web Apps

Design mobile-first experiences and build Progressive Web Apps with offline capabilities and native-like features.

## Overview

Implement mobile-first design strategies and PWA technologies including service workers, app shell architecture, and offline-first patterns. Bridge the gap between web and native applications.

## Quick Start: Approach Selection

| Goal | Approach | Reference |
|------|----------|-----------|
| Responsive website | Mobile-first CSS | `/references/mobile-first-design.md` |
| Installable web app | PWA with manifest | `/references/pwa-implementation.md` |
| Offline functionality | Service workers | `/references/pwa-implementation.md` |
| Push notifications | Push API | `/references/pwa-implementation.md` |
| Performance optimization | Core Web Vitals | `/references/mobile-first-design.md` |

## Mobile-First Design Principles

1. **Content priority** — Most important content first, progressive enhancement
2. **Touch-first** — Minimum 44×44px touch targets, thumb-zone optimization
3. **Performance budget** — Target <3s load on 3G connections
4. **Progressive enhancement** — Base experience works everywhere, enhance for capable devices
5. **Responsive breakpoints** — Design from mobile up: 320px → 768px → 1024px → 1440px

## PWA Requirements Checklist

| Requirement | Implementation |
|-------------|---------------|
| HTTPS | SSL certificate required |
| Service Worker | Register in main JS, handle fetch events |
| Web App Manifest | manifest.json with name, icons, display |
| Responsive | Works on all screen sizes |
| Offline | Service worker caches critical resources |
| Installable | Meets install criteria (manifest + SW) |
| Fast | First Contentful Paint <1.8s |

## Core Web Vitals Targets

| Metric | Good | Needs Improvement | Poor |
|--------|------|-------------------|------|
| LCP (Largest Contentful Paint) | ≤2.5s | ≤4.0s | >4.0s |
| FID (First Input Delay) | ≤100ms | ≤300ms | >300ms |
| CLS (Cumulative Layout Shift) | ≤0.1 | ≤0.25 | >0.25 |
| INP (Interaction to Next Paint) | ≤200ms | ≤500ms | >500ms |

## Using the Reference Files

### When to Read Each Reference

**`/references/mobile-first-design.md`** — Read when implementing responsive layouts, optimizing touch interactions, or improving mobile performance.

**`/references/pwa-implementation.md`** — Read when implementing service workers, caching strategies, push notifications, or offline-first architecture.
