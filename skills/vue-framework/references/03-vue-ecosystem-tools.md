# Vue Ecosystem and Development Tools

## Core Ecosystem Libraries

### 1. Vue Router

Official routing library for Vue.js applications.

#### Installation and Setup

```bash
npm install vue-router@4
```

```javascript
// router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'

 const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('@/views/About.vue')
  },
  {
    path: '/users/:id',
    name: 'UserProfile',
    component: () => import('@/views/UserProfile.vue'),
    props: true
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router

// main.js
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

const app = createApp(App)
app.use(router)
app.mount('#app')
```

#### Advanced Routing Patterns

**Nested Routes**
```javascript
const routes = [
  {
    path: '/dashboard',
    component: Dashboard,
    children: [
      {
        path: '',
        component: DashboardHome
      },
      {
        path: 'profile',
        component: DashboardProfile
      },
      {
        path: 'settings',
        component: DashboardSettings
      }
    ]
  }
]
```

**Route Guards**
```javascript
// Global guards
router.beforeEach((to, from, next) => {
  const isAuthenticated = checkAuth()
  
  if (to.meta.requiresAuth && !isAuthenticated) {
    next('/login')
  } else {
    next()
  }
})

router.afterEach((to, from) => {
  // Analytics, page title updates, etc.
  document.title = to.meta.title || 'Default Title'
})

// Per-route guards
const routes = [
  {
    path: '/admin',
    component: Admin,
    beforeEnter: (to, from, next) => {
      if (isAdmin()) {
        next()
      } else {
        next('/unauthorized')
      }
    }
  }
]

// Component guards
export default {
  beforeRouteEnter(to, from, next) {
    // Called before route is confirmed
    next(vm => {
      // Access component instance via vm
    })
  },
  beforeRouteUpdate(to, from) {
    // Called when route changes but component is reused
  },
  beforeRouteLeave(to, from) {
    // Called when navigating away
    const answer = window.confirm('Do you really want to leave?')
    if (!answer) return false
  }
}
```

**Dynamic Routing**
```javascript
// Programmatic navigation
import { useRouter, useRoute } from 'vue-router'

const router = useRouter()
const route = useRoute()

// Navigate
router.push('/users/123')
router.push({ name: 'UserProfile', params: { id: 123 } })
router.push({ path: '/users', query: { page: 2 } })

// Replace (no history entry)
router.replace('/home')

// Go back/forward
router.go(-1)
router.back()
router.forward()

// Access route params
const userId = route.params.id
const page = route.query.page
```

**Route Meta Fields**
```javascript
const routes = [
  {
    path: '/admin',
    component: Admin,
    meta: {
      requiresAuth: true,
      roles: ['admin'],
      title: 'Admin Dashboard',
      breadcrumb: 'Admin'
    }
  }
]

// Access in components
const route = useRoute()
console.log(route.meta.title)
```

### 2. Pinia (State Management)

Official state management library for Vue 3.

#### Installation and Setup

```bash
npm install pinia
```

```javascript
// main.js
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'

const pinia = createPinia()
const app = createApp(App)

app.use(pinia)
app.mount('#app')
```

#### Store Patterns

**Setup Stores (Composition API Style)**
```javascript
// stores/user.js
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { api } from '@/services/api'

export const useUserStore = defineStore('user', () => {
  // State
  const user = ref(null)
  const token = ref(localStorage.getItem('token'))
  const loading = ref(false)
  const error = ref(null)
  
  // Getters
  const isAuthenticated = computed(() => !!token.value)
  const userName = computed(() => user.value?.name || 'Guest')
  const userRole = computed(() => user.value?.role || 'user')
  
  // Actions
  async function login(credentials) {
    loading.value = true
    error.value = null
    
    try {
      const response = await api.post('/auth/login', credentials)
      user.value = response.data.user
      token.value = response.data.token
      localStorage.setItem('token', token.value)
    } catch (e) {
      error.value = e.message
      throw e
    } finally {
      loading.value = false
    }
  }
  
  async function logout() {
    try {
      await api.post('/auth/logout')
    } finally {
      user.value = null
      token.value = null
      localStorage.removeItem('token')
    }
  }
  
  async function fetchUser() {
    if (!token.value) return
    
    loading.value = true
    try {
      const response = await api.get('/auth/me')
      user.value = response.data
    } catch (e) {
      error.value = e.message
      // Token might be invalid
      logout()
    } finally {
      loading.value = false
    }
  }
  
  return {
    // State
    user,
    token,
    loading,
    error,
    // Getters
    isAuthenticated,
    userName,
    userRole,
    // Actions
    login,
    logout,
    fetchUser
  }
})
```

**Options Stores**
```javascript
export const useCounterStore = defineStore('counter', {
  state: () => ({
    count: 0,
    name: 'Counter'
  }),
  
  getters: {
    doubleCount: (state) => state.count * 2,
    doublePlusOne() {
      return this.doubleCount + 1
    }
  },
  
  actions: {
    increment() {
      this.count++
    },
    async fetchCount() {
      const response = await api.get('/count')
      this.count = response.data
    }
  }
})
```

**Store Composition**
```javascript
// stores/cart.js
import { defineStore } from 'pinia'
import { useUserStore } from './user'
import { useProductStore } from './product'

export const useCartStore = defineStore('cart', () => {
  const userStore = useUserStore()
  const productStore = useProductStore()
  
  const items = ref([])
  
  const total = computed(() => {
    return items.value.reduce((sum, item) => {
      const product = productStore.getProductById(item.productId)
      return sum + (product?.price || 0) * item.quantity
    }, 0)
  })
  
  async function addItem(productId, quantity = 1) {
    if (!userStore.isAuthenticated) {
      throw new Error('Must be logged in')
    }
    
    const existingItem = items.value.find(i => i.productId === productId)
    if (existingItem) {
      existingItem.quantity += quantity
    } else {
      items.value.push({ productId, quantity })
    }
    
    await syncWithServer()
  }
  
  return { items, total, addItem }
})
```

**Plugins**
```javascript
// Persistence plugin
import { createPinia } from 'pinia'

function piniaPersistedState(context) {
  const { store } = context
  
  // Load from localStorage
  const saved = localStorage.getItem(store.$id)
  if (saved) {
    store.$patch(JSON.parse(saved))
  }
  
  // Save on change
  store.$subscribe((mutation, state) => {
    localStorage.setItem(store.$id, JSON.stringify(state))
  })
}

const pinia = createPinia()
pinia.use(piniaPersistedState)
```

### 3. VueUse

Collection of essential Vue composition utilities.

```bash
npm install @vueuse/core
```

**Common Utilities**
```javascript
import {
  useLocalStorage,
  useMouse,
  useWindowSize,
  useOnline,
  useFetch,
  useDebounce,
  useThrottle,
  useIntersectionObserver,
  useEventListener
} from '@vueuse/core'

// Local storage
const theme = useLocalStorage('theme', 'light')
theme.value = 'dark' // Automatically synced

// Mouse position
const { x, y } = useMouse()

// Window size
const { width, height } = useWindowSize()

// Online status
const online = useOnline()

// Fetch data
const { data, error, isFetching } = useFetch('/api/users').json()

// Debounce
const input = ref('')
const debounced = useDebounce(input, 500)

// Intersection observer
const target = ref(null)
const { stop } = useIntersectionObserver(
  target,
  ([{ isIntersecting }]) => {
    if (isIntersecting) {
      console.log('Element is visible')
    }
  }
)

// Event listener
useEventListener(window, 'resize', () => {
  console.log('Window resized')
})
```

### 4. Vite

Next-generation frontend build tool.

#### Configuration

```javascript
// vite.config.js
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'

export default defineConfig({
  plugins: [vue()],
  
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
      '@components': path.resolve(__dirname, './src/components'),
      '@utils': path.resolve(__dirname, './src/utils')
    }
  },
  
  server: {
    port: 3000,
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, '')
      }
    }
  },
  
  build: {
    rollupOptions: {
      output: {
        manualChunks: {
          'vendor': ['vue', 'vue-router', 'pinia'],
          'ui': ['@/components/ui']
        }
      }
    },
    chunkSizeWarningLimit: 1000
  },
  
  optimizeDeps: {
    include: ['vue', 'vue-router', 'pinia']
  }
})
```

**Environment Variables**
```bash
# .env
VITE_API_URL=http://localhost:8000
VITE_APP_TITLE=My App

# .env.production
VITE_API_URL=https://api.production.com
```

```javascript
// Access in code
const apiUrl = import.meta.env.VITE_API_URL
const isDev = import.meta.env.DEV
const isProd = import.meta.env.PROD
```

## Development Tools

### 1. Vue DevTools

Browser extension for debugging Vue applications.

**Features:**
- Component tree inspection
- State management debugging (Pinia/Vuex)
- Event tracking
- Performance profiling
- Route inspection
- Time-travel debugging

**Usage:**
```javascript
// Enable in production (not recommended)
app.config.devtools = true

// Custom inspector
import { setupDevtoolsPlugin } from '@vue/devtools-api'

setupDevtoolsPlugin({
  id: 'my-plugin',
  label: 'My Plugin',
  app
}, (api) => {
  api.addInspector({
    id: 'my-inspector',
    label: 'My Inspector',
    icon: 'tab'
  })
})
```

### 2. ESLint and Prettier

**ESLint Configuration**
```javascript
// .eslintrc.js
module.exports = {
  root: true,
  env: {
    node: true,
    browser: true,
    es2021: true
  },
  extends: [
    'plugin:vue/vue3-recommended',
    'eslint:recommended',
    '@vue/typescript/recommended',
    'prettier'
  ],
  parserOptions: {
    ecmaVersion: 2021
  },
  rules: {
    'vue/multi-word-component-names': 'off',
    'vue/require-default-prop': 'error',
    'vue/require-prop-types': 'error',
    '@typescript-eslint/no-unused-vars': 'warn'
  }
}
```

**Prettier Configuration**
```json
// .prettierrc
{
  "semi": false,
  "singleQuote": true,
  "tabWidth": 2,
  "trailingComma": "none",
  "printWidth": 100,
  "arrowParens": "avoid"
}
```

### 3. TypeScript Integration

**Setup**
```bash
npm install -D typescript @vue/tsconfig
```

```json
// tsconfig.json
{
  "extends": "@vue/tsconfig/tsconfig.web.json",
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["./src/*"]
    },
    "strict": true,
    "jsx": "preserve"
  },
  "include": ["src/**/*.ts", "src/**/*.tsx", "src/**/*.vue"],
  "exclude": ["node_modules"]
}
```

**Component with TypeScript**
```vue
<script setup lang="ts">
import { ref, computed } from 'vue'

interface User {
  id: number
  name: string
  email: string
}

interface Props {
  user: User
  count?: number
}

const props = withDefaults(defineProps<Props>(), {
  count: 0
})

const emit = defineEmits<{
  update: [user: User]
  delete: [id: number]
}>()

const localUser = ref<User>(props.user)
const displayName = computed<string>(() => localUser.value.name.toUpperCase())

function updateUser(updates: Partial<User>) {
  localUser.value = { ...localUser.value, ...updates }
  emit('update', localUser.value)
}
</script>
```

### 4. Testing Tools

**Vitest Configuration**
```javascript
// vitest.config.js
import { defineConfig } from 'vitest/config'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  test: {
    globals: true,
    environment: 'jsdom',
    coverage: {
      provider: 'c8',
      reporter: ['text', 'json', 'html']
    }
  }
})
```

**Component Testing**
```javascript
import { mount } from '@vue/test-utils'
import { describe, it, expect, vi } from 'vitest'
import UserProfile from './UserProfile.vue'

describe('UserProfile', () => {
  it('renders user information', () => {
    const wrapper = mount(UserProfile, {
      props: {
        user: {
          id: 1,
          name: 'John Doe',
          email: 'john@example.com'
        }
      }
    })
    
    expect(wrapper.text()).toContain('John Doe')
    expect(wrapper.text()).toContain('john@example.com')
  })
  
  it('emits update event', async () => {
    const wrapper = mount(UserProfile, {
      props: { user: { id: 1, name: 'John', email: 'john@example.com' } }
    })
    
    await wrapper.find('button.edit').trigger('click')
    await wrapper.find('input[name="name"]').setValue('Jane')
    await wrapper.find('form').trigger('submit')
    
    expect(wrapper.emitted('update')).toBeTruthy()
    expect(wrapper.emitted('update')[0]).toEqual([{
      id: 1,
      name: 'Jane',
      email: 'john@example.com'
    }])
  })
})
```

**E2E Testing with Playwright**
```javascript
import { test, expect } from '@playwright/test'

test('user can login', async ({ page }) => {
  await page.goto('http://localhost:3000/login')
  
  await page.fill('input[name="email"]', 'test@example.com')
  await page.fill('input[name="password"]', 'password123')
  await page.click('button[type="submit"]')
  
  await expect(page).toHaveURL('http://localhost:3000/dashboard')
  await expect(page.locator('h1')).toContainText('Dashboard')
})
```

## UI Component Libraries

### 1. Vuetify

Material Design component framework.

```bash
npm install vuetify@next
```

```javascript
import { createApp } from 'vue'
import { createVuetify } from 'vuetify'
import 'vuetify/styles'

const vuetify = createVuetify()
const app = createApp(App)

app.use(vuetify)
app.mount('#app')
```

### 2. Element Plus

Desktop-focused component library.

```bash
npm install element-plus
```

### 3. Naive UI

Modern Vue 3 component library.

```bash
npm install naive-ui
```

### 4. PrimeVue

Rich set of UI components.

```bash
npm install primevue primeicons
```

## Build and Deployment

### Production Build

```bash
# Build for production
npm run build

# Preview production build
npm run preview
```

### Optimization Strategies

**Code Splitting**
```javascript
// Route-based splitting
const routes = [
  {
    path: '/dashboard',
    component: () => import('./views/Dashboard.vue')
  }
]

// Component-based splitting
const HeavyComponent = defineAsyncComponent(() =>
  import('./components/HeavyComponent.vue')
)
```

**Tree Shaking**
```javascript
// Import only what you need
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'

// Avoid
import * as Vue from 'vue'
```

**Asset Optimization**
```javascript
// vite.config.js
export default {
  build: {
    assetsInlineLimit: 4096, // 4kb
    cssCodeSplit: true,
    minify: 'terser',
    terserOptions: {
      compress: {
        drop_console: true,
        drop_debugger: true
      }
    }
  }
}
```

## Best Practices

### Project Structure

```
src/
├── assets/          # Static assets
├── components/      # Reusable components
│   ├── base/       # Base UI components
│   ├── common/     # Common components
│   └── features/   # Feature components
├── composables/     # Composition functions
├── layouts/         # Layout components
├── plugins/         # Vue plugins
├── router/          # Router configuration
├── stores/          # Pinia stores
├── styles/          # Global styles
├── types/           # TypeScript types
├── utils/           # Utility functions
├── views/           # Page components
├── App.vue
└── main.ts
```

### Performance Monitoring

```javascript
// Performance tracking
import { onMounted } from 'vue'

onMounted(() => {
  const perfData = window.performance.timing
  const pageLoadTime = perfData.loadEventEnd - perfData.navigationStart
  console.log('Page load time:', pageLoadTime)
})
```

## Conclusion

The Vue ecosystem provides a comprehensive set of tools and libraries for building modern web applications. From routing and state management to development tools and UI libraries, the ecosystem offers solutions for every aspect of application development. Understanding and effectively utilizing these tools is essential for productive Vue development.
