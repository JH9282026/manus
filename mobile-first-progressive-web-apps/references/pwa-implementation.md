# PWA Implementation

Comprehensive guide to web app manifests, installation prompts, push notifications, and PWA distribution.

---

## Web App Manifest

The manifest (manifest.json) is a JSON file that provides metadata about the PWA, enabling installation and app-like behavior.

### Complete Manifest Example

```json
{
  "name": "My Progressive Web App",
  "short_name": "MyPWA",
  "description": "A description of my PWA",
  "start_url": "/",
  "scope": "/",
  "display": "standalone",
  "orientation": "portrait-primary",
  "theme_color": "#3367D6",
  "background_color": "#FFFFFF",
  "icons": [
    {
      "src": "/icons/icon-72.png",
      "sizes": "72x72",
      "type": "image/png"
    },
    {
      "src": "/icons/icon-96.png",
      "sizes": "96x96",
      "type": "image/png"
    },
    {
      "src": "/icons/icon-128.png",
      "sizes": "128x128",
      "type": "image/png"
    },
    {
      "src": "/icons/icon-144.png",
      "sizes": "144x144",
      "type": "image/png"
    },
    {
      "src": "/icons/icon-152.png",
      "sizes": "152x152",
      "type": "image/png"
    },
    {
      "src": "/icons/icon-192.png",
      "sizes": "192x192",
      "type": "image/png",
      "purpose": "any maskable"
    },
    {
      "src": "/icons/icon-384.png",
      "sizes": "384x384",
      "type": "image/png"
    },
    {
      "src": "/icons/icon-512.png",
      "sizes": "512x512",
      "type": "image/png"
    }
  ],
  "screenshots": [
    {
      "src": "/screenshots/home.png",
      "sizes": "1280x720",
      "type": "image/png"
    },
    {
      "src": "/screenshots/feature.png",
      "sizes": "1280x720",
      "type": "image/png"
    }
  ],
  "shortcuts": [
    {
      "name": "New Post",
      "short_name": "New",
      "url": "/new",
      "icons": [{ "src": "/icons/new.png", "sizes": "192x192" }]
    }
  ],
  "categories": ["productivity", "utilities"]
}
```

### Manifest Properties

| Property | Required | Description |
|----------|----------|-------------|
| `name` | Yes | Full app name |
| `short_name` | Recommended | Name for home screen (12 chars max) |
| `start_url` | Yes | URL when app launches |
| `display` | Yes | Display mode |
| `icons` | Yes | Array of icon objects |
| `theme_color` | Recommended | Browser UI color |
| `background_color` | Recommended | Splash screen background |
| `description` | Optional | App description |
| `scope` | Optional | Navigation scope |
| `orientation` | Optional | Screen orientation |

### Display Modes

| Mode | Description |
|------|-------------|
| `fullscreen` | Entire screen, no browser UI |
| `standalone` | App-like, with status bar only |
| `minimal-ui` | Minimal browser controls |
| `browser` | Standard browser tab |

### Linking the Manifest

```html
<link rel="manifest" href="/manifest.json">
<meta name="theme-color" content="#3367D6">

<!-- iOS support -->
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="MyPWA">
<link rel="apple-touch-icon" href="/icons/icon-152.png">
```

---

## Custom Install Prompts

Capture the browser's install prompt to show custom UI.

### Implementation

```javascript
let deferredPrompt;

window.addEventListener('beforeinstallprompt', (e) => {
  // Prevent default browser prompt
  e.preventDefault();
  
  // Store event for later use
  deferredPrompt = e;
  
  // Show custom install button
  showInstallButton();
});

function showInstallButton() {
  const installButton = document.getElementById('install-btn');
  installButton.style.display = 'block';
  
  installButton.addEventListener('click', async () => {
    // Show browser prompt
    deferredPrompt.prompt();
    
    // Wait for user response
    const { outcome } = await deferredPrompt.userChoice;
    
    if (outcome === 'accepted') {
      console.log('User accepted install');
    } else {
      console.log('User dismissed install');
    }
    
    // Clear stored prompt
    deferredPrompt = null;
    installButton.style.display = 'none';
  });
}

// Detect when app is installed
window.addEventListener('appinstalled', () => {
  console.log('PWA was installed');
  deferredPrompt = null;
});
```

### Install Prompt Best Practices

- Don't show immediately on page load
- Wait for user engagement
- Explain value proposition before prompting
- Provide custom, branded install UI
- Track install rates

---

## Push Notifications

### Prerequisites

1. Service Worker registered
2. User permission granted
3. HTTPS connection
4. Push server configured

### Request Permission

```javascript
async function requestNotificationPermission() {
  // Check if supported
  if (!('Notification' in window)) {
    console.log('Notifications not supported');
    return false;
  }
  
  // Request permission
  const permission = await Notification.requestPermission();
  
  if (permission === 'granted') {
    await subscribeToPush();
    return true;
  }
  
  return false;
}
```

### Subscribe to Push

```javascript
async function subscribeToPush() {
  const registration = await navigator.serviceWorker.ready;
  
  const subscription = await registration.pushManager.subscribe({
    userVisibleOnly: true,
    applicationServerKey: urlBase64ToUint8Array(VAPID_PUBLIC_KEY)
  });
  
  // Send subscription to server
  await fetch('/api/push/subscribe', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(subscription)
  });
}

// Helper function
function urlBase64ToUint8Array(base64String) {
  const padding = '='.repeat((4 - base64String.length % 4) % 4);
  const base64 = (base64String + padding)
    .replace(/-/g, '+')
    .replace(/_/g, '/');
  const rawData = window.atob(base64);
  const outputArray = new Uint8Array(rawData.length);
  for (let i = 0; i < rawData.length; ++i) {
    outputArray[i] = rawData.charCodeAt(i);
  }
  return outputArray;
}
```

### Handle Push in Service Worker

```javascript
self.addEventListener('push', event => {
  const data = event.data.json();
  
  const options = {
    body: data.body,
    icon: '/icons/icon-192.png',
    badge: '/icons/badge-72.png',
    vibrate: [100, 50, 100],
    data: {
      url: data.url
    },
    actions: [
      { action: 'view', title: 'View' },
      { action: 'dismiss', title: 'Dismiss' }
    ]
  };
  
  event.waitUntil(
    self.registration.showNotification(data.title, options)
  );
});

self.addEventListener('notificationclick', event => {
  event.notification.close();
  
  if (event.action === 'view' || !event.action) {
    event.waitUntil(
      clients.openWindow(event.notification.data.url)
    );
  }
});
```

### Notification Best Practices

- **Ask permission thoughtfully** — In context, after user engagement
- **Relevant content** — Personalized, valuable notifications
- **Timing** — Respect time zones and user preferences
- **Frequency** — Quality over quantity
- **Actionable** — Include clear actions
- **Easy opt-out** — Make unsubscribing simple

### Notification Design

| Element | Guidelines |
|---------|------------|
| Title | Concise, compelling (50 chars max) |
| Body | Brief, informative (100 chars max) |
| Icon | 192x192px, recognizable app icon |
| Badge | 72x72px, monochrome |
| Actions | Up to 2 action buttons |

---

## App Store Distribution

### Google Play Store (TWA)

Trusted Web Activities (TWA) package PWAs for Google Play.

**Requirements**:
- Valid PWA with passing Lighthouse audit
- Digital Asset Links file for verification
- Android Studio for building

**Steps**:
1. Create TWA project in Android Studio
2. Configure asset links
3. Build signed APK/AAB
4. Submit to Google Play

### Microsoft Store

PWAs can be submitted directly to Microsoft Store.

**Steps**:
1. Use PWABuilder to generate package
2. Create Microsoft Partner Center account
3. Submit .msix package
4. Pass certification

### Apple App Store

Requires native wrapper (limited PWA features).

**Options**:
- Capacitor wrapper
- React Native WebView
- Native Swift wrapper

**Limitations**:
- No push notifications in iOS PWAs
- Limited background sync
- Restricted storage access

---

## PWA Development Tools

### PWA Builders

| Tool | Description |
|------|-------------|
| PWABuilder (Microsoft) | Generate PWA assets and packages |
| Workbox (Google) | Service worker libraries |
| Create React App | Built-in PWA template |
| Next.js (next-pwa) | Automatic PWA setup |
| Vue CLI (@vue/pwa) | PWA plugin |
| Angular (@angular/pwa) | Built-in PWA schematic |

### Asset Generators

- **PWABuilder** — Complete asset generation
- **RealFaviconGenerator** — Icons for all platforms
- **Maskable.app** — Test maskable icons

### Testing Tools

| Tool | Purpose |
|------|--------|
| Lighthouse | PWA audit, performance, accessibility |
| Chrome DevTools | Service worker debugging, manifest validation |
| WebPageTest | Performance analysis |
| BrowserStack | Cross-device testing |

---

## PWA Checklist

### Core Requirements

- [ ] Served over HTTPS
- [ ] Valid web app manifest
- [ ] Service worker with fetch handler
- [ ] Responsive design
- [ ] Works offline

### Performance

- [ ] First Contentful Paint < 1.8s
- [ ] Largest Contentful Paint < 2.5s
- [ ] Time to Interactive < 3.8s
- [ ] Cumulative Layout Shift < 0.1

### User Experience

- [ ] Custom install prompt
- [ ] Offline fallback page
- [ ] Push notifications (if applicable)
- [ ] Splash screen configured
- [ ] Theme color set

### Cross-Platform

- [ ] Works in Chrome, Firefox, Safari, Edge
- [ ] iOS-specific meta tags
- [ ] Android manifest icons (maskable)
- [ ] Tested on real devices
