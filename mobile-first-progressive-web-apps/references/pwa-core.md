# PWA Core Features

Comprehensive guide to Progressive Web App fundamentals, service workers, offline functionality, and caching strategies.

---

## What is a PWA

Progressive Web Apps use modern web technologies to deliver app-like experiences. They combine the reach of the web with capabilities previously only available to native apps.

### Key Characteristics

- **Progressive** — Work for every user regardless of browser
- **Responsive** — Fit any form factor
- **Connectivity Independent** — Work offline or on low-quality networks
- **App-Like** — Feel like native apps with app-style interactions
- **Fresh** — Always up-to-date via service workers
- **Safe** — Served via HTTPS
- **Discoverable** — Identifiable by search engines
- **Re-engageable** — Support push notifications
- **Installable** — Add to home screen without app stores
- **Linkable** — Shareable via URL

---

## PWA Requirements

### Technical Requirements

1. **HTTPS** — Secure connection required (service workers only work over HTTPS)
2. **Service Worker** — JavaScript worker for offline, caching, background sync
3. **Web App Manifest** — JSON file with app metadata
4. **Responsive Design** — Works across all screen sizes

### Installation Criteria

For PWAs to be installable:
- Served over HTTPS
- Valid web app manifest with required fields
- Registered service worker with fetch handler
- User engagement threshold met (varies by browser)

---

## Service Workers

### What Are Service Workers

Service workers are JavaScript files that run in the background, separate from the main browser thread. They act as a proxy between the web application and the network.

### Key Capabilities

- Intercept network requests
- Cache resources and API responses
- Enable offline functionality
- Handle push notifications
- Perform background synchronization

### Service Worker Lifecycle

1. **Registration** — Main JavaScript registers the service worker
2. **Installation** — Service worker downloads, caches initial resources
3. **Activation** — Old service worker replaced, new one takes control
4. **Fetch Events** — Intercepts network requests
5. **Updates** — New version detected, update cycle begins

### Basic Registration

```javascript
// In main JavaScript file
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/sw.js')
    .then(registration => {
      console.log('SW registered:', registration.scope);
    })
    .catch(error => {
      console.log('SW registration failed:', error);
    });
}
```

### Basic Service Worker

```javascript
// sw.js
const CACHE_NAME = 'app-cache-v1';
const ASSETS = [
  '/',
  '/index.html',
  '/styles.css',
  '/app.js',
  '/offline.html'
];

// Installation - cache assets
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(ASSETS))
  );
});

// Activation - clean old caches
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys => {
      return Promise.all(
        keys.filter(key => key !== CACHE_NAME)
            .map(key => caches.delete(key))
      );
    })
  );
});

// Fetch - serve from cache or network
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(cached => cached || fetch(event.request))
      .catch(() => caches.match('/offline.html'))
  );
});
```

---

## Caching Strategies

### Cache-First (Offline-First)

**Best for**: Static assets, fonts, images that rarely change

```javascript
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(cached => cached || fetch(event.request))
  );
});
```

### Network-First

**Best for**: Dynamic content, API responses, frequently updated data

```javascript
self.addEventListener('fetch', event => {
  event.respondWith(
    fetch(event.request)
      .then(response => {
        const clone = response.clone();
        caches.open('dynamic-cache').then(cache => {
          cache.put(event.request, clone);
        });
        return response;
      })
      .catch(() => caches.match(event.request))
  );
});
```

### Stale-While-Revalidate

**Best for**: Content where freshness matters but speed is important

```javascript
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.open('dynamic').then(cache => {
      return cache.match(event.request).then(cached => {
        const fetched = fetch(event.request).then(response => {
          cache.put(event.request, response.clone());
          return response;
        });
        return cached || fetched;
      });
    })
  );
});
```

### Network-Only

**Best for**: Non-cacheable requests, sensitive data

```javascript
self.addEventListener('fetch', event => {
  event.respondWith(fetch(event.request));
});
```

### Cache-Only

**Best for**: Precached assets that never change

```javascript
self.addEventListener('fetch', event => {
  event.respondWith(caches.match(event.request));
});
```

---

## Workbox Library

Google's Workbox simplifies service worker development.

### Basic Workbox Setup

```javascript
import { precacheAndRoute } from 'workbox-precaching';
import { registerRoute } from 'workbox-routing';
import { StaleWhileRevalidate, CacheFirst, NetworkFirst } from 'workbox-strategies';

// Precache static assets
precacheAndRoute(self.__WB_MANIFEST);

// Cache images with CacheFirst
registerRoute(
  ({ request }) => request.destination === 'image',
  new CacheFirst({
    cacheName: 'images',
    plugins: [
      new ExpirationPlugin({
        maxEntries: 50,
        maxAgeSeconds: 30 * 24 * 60 * 60, // 30 days
      }),
    ],
  })
);

// Cache API responses with NetworkFirst
registerRoute(
  ({ url }) => url.pathname.startsWith('/api/'),
  new NetworkFirst({
    cacheName: 'api-cache',
    networkTimeoutSeconds: 3,
  })
);

// Cache pages with StaleWhileRevalidate
registerRoute(
  ({ request }) => request.mode === 'navigate',
  new StaleWhileRevalidate({
    cacheName: 'pages',
  })
);
```

---

## Offline Functionality

### Offline-First Approach

Design applications to work offline first, treating network connectivity as an enhancement.

### Core Principles

1. App functions without connectivity
2. Data syncs when connection available
3. Local storage for user data
4. Queue actions for later execution

### Offline Strategies

| Strategy | Implementation |
|----------|----------------|
| Cache static assets | HTML, CSS, JS cached during installation |
| Cache API responses | Store frequently accessed data locally |
| Offline fallback page | Custom page when content unavailable |
| Background sync | Queue actions, sync when online |

### Storage Options

| Storage | Use Case | Size Limit |
|---------|----------|------------|
| Cache API | HTTP responses | Varies (generous) |
| IndexedDB | Structured data, large datasets | Varies (large) |
| localStorage | Simple key-value pairs | ~5MB |
| sessionStorage | Session-only data | ~5MB |

### Offline UX Best Practices

- **Offline indicator** — Clearly communicate offline status
- **Cached content labels** — Indicate potentially stale content
- **Sync status** — Show pending sync items
- **Error messages** — Explain limitations when offline

---

## App Shell Architecture

The app shell is the minimal HTML, CSS, and JavaScript required to power the user interface.

### Benefits

- Instant loading on repeat visits
- Reliable performance
- Consistent UI during content loading
- Reduced network dependency

### Implementation

```javascript
// Precache app shell
const APP_SHELL = [
  '/',
  '/shell.html',
  '/styles/app.css',
  '/scripts/app.js',
  '/images/logo.svg'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open('app-shell-v1')
      .then(cache => cache.addAll(APP_SHELL))
  );
});
```

### Structure

```
App Shell (cached)
├── Header
├── Navigation
├── Content container (empty)
├── Footer
└── Loading indicators

Dynamic Content (loaded from network/cache)
├── Main content
├── User data
└── Real-time updates
```

---

## Background Sync

Queue user actions and sync when connectivity returns.

### Registration

```javascript
// Request background sync
async function queueSync(data) {
  // Store data in IndexedDB
  await storeInDB(data);
  
  // Register sync
  const registration = await navigator.serviceWorker.ready;
  await registration.sync.register('sync-messages');
}
```

### Service Worker Handler

```javascript
self.addEventListener('sync', event => {
  if (event.tag === 'sync-messages') {
    event.waitUntil(syncMessages());
  }
});

async function syncMessages() {
  const messages = await getFromDB();
  
  for (const message of messages) {
    try {
      await fetch('/api/messages', {
        method: 'POST',
        body: JSON.stringify(message)
      });
      await removeFromDB(message.id);
    } catch (error) {
      // Will retry on next sync
      throw error;
    }
  }
}
```

---

## Service Worker Best Practices

### Version Management

- Version your service worker and caches
- Clear old caches on activation
- Use semantic versioning for cache names

### Cache Management

- Set cache limits and expiration
- Don't cache indefinitely
- Remove outdated assets

### Error Handling

- Gracefully handle network failures
- Provide offline fallback pages
- Log errors for debugging

### Testing

- Test offline scenarios thoroughly
- Verify caching behavior across updates
- Use Chrome DevTools Application tab
- Test service worker updates
