# PWA Implementation

## Service Worker Lifecycle

### Registration
```javascript
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/sw.js')
    .then(reg => console.log('SW registered'))
    .catch(err => console.log('SW failed', err));
}
```

### Lifecycle Events
1. **Install** — Cache critical resources
2. **Activate** — Clean up old caches
3. **Fetch** — Intercept network requests

---

## Caching Strategies

| Strategy | Description | Best For |
|----------|------------|----------|
| Cache First | Check cache, fallback to network | Static assets, fonts |
| Network First | Try network, fallback to cache | API responses, dynamic content |
| Stale While Revalidate | Serve cache, update in background | Frequently updated content |
| Cache Only | Only serve from cache | Offline-specific resources |
| Network Only | Never cache | Real-time data, auth |

### Cache First Implementation
```javascript
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(cached => cached || fetch(event.request))
  );
});
```

---

## Web App Manifest

### Required Fields
```json
{
  "name": "App Full Name",
  "short_name": "App",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#ffffff",
  "theme_color": "#000000",
  "icons": [
    { "src": "/icon-192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "/icon-512.png", "sizes": "512x512", "type": "image/png" }
  ]
}
```

### Display Modes
| Mode | Behavior |
|------|----------|
| `fullscreen` | No browser UI, full screen |
| `standalone` | Looks like native app, no URL bar |
| `minimal-ui` | Minimal browser controls |
| `browser` | Standard browser tab |

---

## Offline-First Architecture

### App Shell Pattern
1. Cache HTML shell, CSS, and core JS on install
2. Load content dynamically from network/cache
3. Show cached content immediately, update when network available
4. Provide offline fallback pages for uncached routes

### Storage Options
| API | Use Case | Limit |
|-----|----------|-------|
| Cache API | HTTP responses | ~50MB+ |
| IndexedDB | Structured data | ~50MB+ |
| localStorage | Small key-value | 5-10MB |

---

## Push Notifications

### Implementation Steps
1. Request notification permission
2. Subscribe to push service (get endpoint)
3. Send subscription to server
4. Server sends push via Web Push protocol
5. Service worker receives push event
6. Display notification with Notification API

### Best Practices
- Ask permission contextually (not on page load)
- Provide value explanation before permission prompt
- Allow granular notification preferences
- Include action buttons in notifications
- Handle notification clicks to open relevant content
- Respect user preferences (frequency, timing)

---

## PWA Testing

### Lighthouse PWA Audit
- Installability check
- Service worker validation
- Offline capability test
- HTTPS verification
- Performance scoring
- Accessibility scoring

### Testing Tools
| Tool | Purpose |
|------|---------|
| Chrome DevTools | Service worker debugging, manifest inspection |
| Lighthouse | PWA audit, performance scoring |
| Workbox | Service worker library, caching strategies |
| PWA Builder | Manifest generation, testing |
