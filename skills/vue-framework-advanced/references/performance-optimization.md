# Performance Optimization

Advanced techniques for optimizing Vue 3 application performance.

---

## Bundle Size Optimization

### 1. Tree-Shaking

Vue 3 is designed for optimal tree-shaking. Only import what you use:

```javascript
// ❌ Bad: Imports entire Vue
import Vue from 'vue'

// ✅ Good: Import only what you need
import { ref, computed, watch } from 'vue'
```

**Result:** Unused features are eliminated from production bundle.

### 2. Code Splitting

**Route-based splitting:**
```javascript
const routes = [
  {
    path: '/dashboard',
    component: () => import('./views/Dashboard.vue')
  },
  {
    path: '/profile',
    component: () => import('./views/Profile.vue')
  }
]
```

**Component-based splitting:**
```javascript
import { defineAsyncComponent } from 'vue'

const HeavyComponent = defineAsyncComponent(() =>
  import('./components/HeavyComponent.vue')
)
```

### 3. Dynamic Imports

```javascript
// Load library only when needed
const loadChart = async () => {
  const { Chart } = await import('chart.js')
  return new Chart(/* ... */)
}
```

---

## Render Performance

### 1. `v-once` for Static Content

```vue
<template>
  <div v-once>
    <h1>{{ staticTitle }}</h1>
    <p>{{ staticDescription }}</p>
  </div>
</template>
```

**Effect:** Content rendered once and never updated.

### 2. `v-memo` for Conditional Re-rendering

```vue
<template>
  <div v-memo="[user.id, user.name]">
    <UserCard :user="user" />
  </div>
</template>
```

**Effect:** Re-renders only when `user.id` or `user.name` changes.

### 3. Virtual Scrolling for Large Lists

```vue
<script setup>
import { ref } from 'vue'
import { useVirtualList } from '@vueuse/core'

const items = ref(Array.from({ length: 10000 }, (_, i) => `Item ${i}`))
const { list, containerProps, wrapperProps } = useVirtualList(items, {
  itemHeight: 50
})
</script>

<template>
  <div v-bind="containerProps" style="height: 400px">
    <div v-bind="wrapperProps">
      <div v-for="{ data, index } in list" :key="index">
        {{ data }}
      </div>
    </div>
  </div>
</template>
```

### 4. Lazy Hydration

```javascript
import { defineAsyncComponent } from 'vue'

const LazyComponent = defineAsyncComponent({
  loader: () => import('./HeavyComponent.vue'),
  delay: 200,
  timeout: 3000,
  errorComponent: ErrorComponent,
  loadingComponent: LoadingComponent
})
```

---

## Reactivity Optimization

### 1. Shallow Reactivity

```javascript
import { shallowRef, shallowReactive } from 'vue'

// For large objects
const largeData = shallowRef({
  nested: { /* deep structure */ }
})

// Update entire object to trigger reactivity
largeData.value = { ...largeData.value, updated: true }
```

### 2. `markRaw` for Non-Reactive Data

```javascript
import { reactive, markRaw } from 'vue'

const state = reactive({
  user: { name: 'John' },
  thirdPartyLib: markRaw(new SomeLibrary())
})
```

### 3. Computed Caching

```javascript
// ❌ Bad: Method called on every render
const fullName = () => `${firstName.value} ${lastName.value}`

// ✅ Good: Computed cached until dependencies change
const fullName = computed(() => `${firstName.value} ${lastName.value}`)
```

---

## Compiler Optimizations

### 1. `<script setup>` Syntax

```vue
<!-- ✅ Optimized -->
<script setup>
import { ref } from 'vue'
const count = ref(0)
</script>

<!-- ❌ Less optimized -->
<script>
import { ref } from 'vue'
export default {
  setup() {
    const count = ref(0)
    return { count }
  }
}
</script>
```

**Benefits:**
- Inline template compilation
- Better minification
- Smaller bundle size

### 2. Static Hoisting

Vue 3 compiler automatically hoists static content:

```vue
<template>
  <div>
    <h1>Static Title</h1> <!-- Hoisted -->
    <p>{{ dynamicContent }}</p> <!-- Not hoisted -->
  </div>
</template>
```

### 3. Patch Flags

Compiler adds hints for efficient updates:

```vue
<template>
  <div :class="dynamicClass">{{ text }}</div>
</template>
```

Compiled with patch flags indicating only `class` and `text` need tracking.

---

## Network Optimization

### 1. Prefetching and Preloading

```javascript
// In router
const routes = [
  {
    path: '/dashboard',
    component: () => import(
      /* webpackPrefetch: true */
      './views/Dashboard.vue'
    )
  }
]
```

### 2. Resource Hints

```html
<!-- In index.html -->
<link rel="preconnect" href="https://api.example.com">
<link rel="dns-prefetch" href="https://cdn.example.com">
```

### 3. API Response Caching

```javascript
import { ref } from 'vue'

const cache = new Map()

export function useCachedFetch(url) {
  const data = ref(cache.get(url) || null)
  const loading = ref(!cache.has(url))

  if (!cache.has(url)) {
    fetch(url)
      .then(res => res.json())
      .then(json => {
        cache.set(url, json)
        data.value = json
        loading.value = false
      })
  }

  return { data, loading }
}
```

---

## Image Optimization

### 1. Lazy Loading Images

```vue
<template>
  <img
    v-lazy="imageUrl"
    alt="Description"
  />
</template>

<script setup>
import { directive as vLazy } from 'vue3-lazy'
</script>
```

### 2. Responsive Images

```vue
<template>
  <picture>
    <source
      media="(min-width: 1024px)"
      :srcset="image.large"
    />
    <source
      media="(min-width: 768px)"
      :srcset="image.medium"
    />
    <img :src="image.small" alt="Description" />
  </picture>
</template>
```

### 3. WebP with Fallback

```vue
<template>
  <picture>
    <source :srcset="image.webp" type="image/webp" />
    <img :src="image.jpg" alt="Description" />
  </picture>
</template>
```

---

## State Management Optimization

### 1. Pinia Store Splitting

```javascript
// ❌ Bad: One large store
export const useAppStore = defineStore('app', {
  state: () => ({
    user: {},
    products: [],
    cart: [],
    orders: []
  })
})

// ✅ Good: Multiple focused stores
export const useUserStore = defineStore('user', { /* ... */ })
export const useProductStore = defineStore('products', { /* ... */ })
export const useCartStore = defineStore('cart', { /* ... */ })
```

### 2. Selective State Subscription

```javascript
import { storeToRefs } from 'pinia'
import { useUserStore } from '@/stores/user'

const store = useUserStore()

// ❌ Bad: Subscribe to entire store
const state = reactive(store.$state)

// ✅ Good: Subscribe only to needed properties
const { username, email } = storeToRefs(store)
```

---

## Build Configuration

### Vite Optimization

```javascript
// vite.config.js
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  build: {
    rollupOptions: {
      output: {
        manualChunks: {
          'vendor': ['vue', 'vue-router', 'pinia'],
          'ui': ['@/components/ui']
        }
      }
    },
    chunkSizeWarningLimit: 1000,
    minify: 'terser',
    terserOptions: {
      compress: {
        drop_console: true,
        drop_debugger: true
      }
    }
  }
})
```

---

## Monitoring Performance

### 1. Vue DevTools Performance Tab

- Component render times
- Re-render frequency
- Memory usage

### 2. Browser Performance API

```javascript
import { onMounted } from 'vue'

onMounted(() => {
  const perfData = performance.getEntriesByType('navigation')[0]
  console.log('DOM Content Loaded:', perfData.domContentLoadedEventEnd)
  console.log('Load Complete:', perfData.loadEventEnd)
})
```

### 3. Lighthouse Audits

Run regular Lighthouse audits to track:
- First Contentful Paint (FCP)
- Largest Contentful Paint (LCP)
- Time to Interactive (TTI)
- Cumulative Layout Shift (CLS)

---

## Vapor Mode (2026)

Vue 3's Vapor Mode compiles components without Virtual DOM:

**Benefits:**
- 50-70% smaller runtime
- Faster initial render
- Lower memory usage
- Direct DOM manipulation

**Opt-in per component:**
```vue
<script setup vapor>
import { ref } from 'vue'
const count = ref(0)
</script>
```

**Note:** Not all features supported in Vapor Mode (e.g., Teleport, KeepAlive).

---

## Performance Checklist

- [ ] Use `<script setup>` syntax
- [ ] Implement code splitting for routes
- [ ] Lazy load heavy components
- [ ] Use virtual scrolling for large lists
- [ ] Apply `v-memo` for expensive renders
- [ ] Use `shallowRef`/`shallowReactive` for large data
- [ ] Implement image lazy loading
- [ ] Split Pinia stores by domain
- [ ] Enable production mode optimizations
- [ ] Monitor with Vue DevTools and Lighthouse
- [ ] Consider Vapor Mode for critical components
