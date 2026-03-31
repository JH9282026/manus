# Vue Best Practices and Performance Optimization

## Code Organization and Structure

### Component Organization

#### File Structure Best Practices

```
components/
├── base/                    # Base/primitive components
│   ├── BaseButton.vue
│   ├── BaseInput.vue
│   ├── BaseCard.vue
│   └── BaseModal.vue
├── common/                  # Shared components
│   ├── AppHeader.vue
│   ├── AppFooter.vue
│   └── AppSidebar.vue
├── features/                # Feature-specific components
│   ├── user/
│   │   ├── UserProfile.vue
│   │   ├── UserList.vue
│   │   └── UserForm.vue
│   └── product/
│       ├── ProductCard.vue
│       └── ProductList.vue
└── layouts/                 # Layout components
    ├── DefaultLayout.vue
    ├── AuthLayout.vue
    └── DashboardLayout.vue
```

#### Component Naming Conventions

```javascript
// ✅ Good - Multi-word component names
BaseButton.vue
UserProfile.vue
ProductCard.vue

// ❌ Bad - Single-word names
Button.vue
Profile.vue
Card.vue

// ✅ Good - Prefix for single-instance components
TheHeader.vue
TheSidebar.vue
TheFooter.vue

// ✅ Good - Tightly coupled child components
TodoList.vue
TodoListItem.vue
TodoListItemButton.vue

// ✅ Good - Order of words in component names
SearchButtonClear.vue
SearchButtonRun.vue
SearchInputQuery.vue
```

### Script Organization

#### Composition API Organization

```vue
<script setup>
// 1. Imports
import { ref, computed, watch, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import UserService from '@/services/UserService'

// 2. Props
const props = defineProps({
  userId: {
    type: Number,
    required: true
  },
  editable: {
    type: Boolean,
    default: false
  }
})

// 3. Emits
const emit = defineEmits(['update', 'delete'])

// 4. Composables
const router = useRouter()
const userStore = useUserStore()

// 5. Reactive State
const user = ref(null)
const loading = ref(false)
const error = ref(null)

// 6. Computed Properties
const displayName = computed(() => {
  return user.value ? `${user.value.firstName} ${user.value.lastName}` : ''
})

const canEdit = computed(() => {
  return props.editable && userStore.isAuthenticated
})

// 7. Watchers
watch(() => props.userId, async (newId) => {
  await fetchUser(newId)
}, { immediate: true })

// 8. Methods
async function fetchUser(id) {
  loading.value = true
  error.value = null
  
  try {
    user.value = await UserService.getUser(id)
  } catch (e) {
    error.value = e.message
  } finally {
    loading.value = false
  }
}

function handleUpdate(updates) {
  emit('update', { ...user.value, ...updates })
}

function handleDelete() {
  emit('delete', user.value.id)
}

// 9. Lifecycle Hooks
onMounted(() => {
  console.log('Component mounted')
})

// 10. Expose (if needed)
defineExpose({
  fetchUser,
  user
})
</script>
```

#### Options API Organization

```vue
<script>
export default {
  name: 'UserProfile',
  
  components: {
    UserAvatar,
    UserInfo
  },
  
  props: {
    userId: {
      type: Number,
      required: true
    }
  },
  
  emits: ['update', 'delete'],
  
  data() {
    return {
      user: null,
      loading: false,
      error: null
    }
  },
  
  computed: {
    displayName() {
      return this.user ? `${this.user.firstName} ${this.user.lastName}` : ''
    }
  },
  
  watch: {
    userId: {
      handler: 'fetchUser',
      immediate: true
    }
  },
  
  created() {
    // Initialization
  },
  
  mounted() {
    // DOM-dependent initialization
  },
  
  methods: {
    async fetchUser(id) {
      this.loading = true
      this.error = null
      
      try {
        this.user = await UserService.getUser(id)
      } catch (e) {
        this.error = e.message
      } finally {
        this.loading = false
      }
    }
  }
}
</script>
```

## Performance Optimization

### 1. Component Optimization

#### Use v-show vs v-if Appropriately

```vue
<template>
  <!-- ✅ Use v-show for frequent toggles (CSS display) -->
  <div v-show="isVisible">Frequently toggled content</div>
  
  <!-- ✅ Use v-if for conditional rendering (DOM manipulation) -->
  <div v-if="userRole === 'admin'">Admin panel</div>
  
  <!-- ❌ Avoid v-if for frequent toggles -->
  <div v-if="isModalOpen">Modal content</div>
</template>
```

#### Avoid v-if with v-for

```vue
<template>
  <!-- ❌ Bad - v-if with v-for on same element -->
  <li v-for="user in users" v-if="user.isActive" :key="user.id">
    {{ user.name }}
  </li>
  
  <!-- ✅ Good - Use computed property -->
  <li v-for="user in activeUsers" :key="user.id">
    {{ user.name }}
  </li>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps(['users'])

const activeUsers = computed(() => {
  return props.users.filter(user => user.isActive)
})
</script>
```

#### Use Functional Components for Simple Components

```vue
<!-- Simple presentational component -->
<template>
  <div class="user-badge" :class="type">
    {{ label }}
  </div>
</template>

<script setup>
defineProps({
  type: String,
  label: String
})
</script>

<style scoped>
.user-badge {
  padding: 4px 8px;
  border-radius: 4px;
}
</style>
```

### 2. Reactivity Optimization

#### Use shallowRef and shallowReactive

```javascript
import { ref, shallowRef, reactive, shallowReactive } from 'vue'

// ❌ Deep reactivity for large objects (expensive)
const largeObject = ref({
  deeply: {
    nested: {
      data: [/* thousands of items */]
    }
  }
})

// ✅ Shallow reactivity (only top-level is reactive)
const largeObject = shallowRef({
  deeply: {
    nested: {
      data: [/* thousands of items */]
    }
  }
})

// To trigger updates with shallowRef
largeObject.value = { ...largeObject.value, updated: true }

// ✅ Shallow reactive for objects
const state = shallowReactive({
  foo: 1,
  nested: {
    bar: 2 // Not reactive
  }
})
```

#### Use readonly for Immutable Data

```javascript
import { readonly, ref } from 'vue'

const state = ref({ count: 0 })
const readonlyState = readonly(state)

// ✅ Prevents accidental mutations
// readonlyState.value.count++ // Warning in development
```

#### Optimize Computed Properties

```javascript
import { computed, ref } from 'vue'

// ✅ Good - Simple, cacheable computation
const doubled = computed(() => count.value * 2)

// ❌ Bad - Expensive computation without optimization
const expensiveResult = computed(() => {
  return items.value.map(item => {
    // Complex transformation
  }).filter(item => {
    // Complex filtering
  }).sort((a, b) => {
    // Complex sorting
  })
})

// ✅ Better - Break into smaller computeds
const transformedItems = computed(() => {
  return items.value.map(item => transform(item))
})

const filteredItems = computed(() => {
  return transformedItems.value.filter(item => filter(item))
})

const sortedItems = computed(() => {
  return [...filteredItems.value].sort(compare)
})
```

### 3. List Rendering Optimization

#### Always Use Keys with v-for

```vue
<template>
  <!-- ❌ Bad - No key -->
  <div v-for="item in items">
    {{ item.name }}
  </div>
  
  <!-- ❌ Bad - Index as key (problematic for dynamic lists) -->
  <div v-for="(item, index) in items" :key="index">
    {{ item.name }}
  </div>
  
  <!-- ✅ Good - Unique, stable key -->
  <div v-for="item in items" :key="item.id">
    {{ item.name }}
  </div>
</template>
```

#### Virtual Scrolling for Large Lists

```vue
<script setup>
import { ref, computed } from 'vue'

const props = defineProps({
  items: Array,
  itemHeight: {
    type: Number,
    default: 50
  },
  visibleCount: {
    type: Number,
    default: 20
  }
})

const scrollTop = ref(0)
const containerHeight = computed(() => props.visibleCount * props.itemHeight)

const visibleItems = computed(() => {
  const startIndex = Math.floor(scrollTop.value / props.itemHeight)
  const endIndex = startIndex + props.visibleCount
  
  return props.items.slice(startIndex, endIndex).map((item, index) => ({
    item,
    index: startIndex + index,
    top: (startIndex + index) * props.itemHeight
  }))
})

const totalHeight = computed(() => props.items.length * props.itemHeight)

function handleScroll(event) {
  scrollTop.value = event.target.scrollTop
}
</script>

<template>
  <div 
    class="virtual-scroll-container"
    :style="{ height: containerHeight + 'px' }"
    @scroll="handleScroll"
  >
    <div :style="{ height: totalHeight + 'px', position: 'relative' }">
      <div
        v-for="{ item, index, top } in visibleItems"
        :key="item.id"
        :style="{
          position: 'absolute',
          top: top + 'px',
          height: itemHeight + 'px',
          width: '100%'
        }"
      >
        <slot :item="item" :index="index"></slot>
      </div>
    </div>
  </div>
</template>

<style scoped>
.virtual-scroll-container {
  overflow-y: auto;
}
</style>
```

### 4. Async Component Loading

#### Route-Based Code Splitting

```javascript
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    component: () => import('@/views/Home.vue')
  },
  {
    path: '/dashboard',
    component: () => import('@/views/Dashboard.vue'),
    children: [
      {
        path: 'analytics',
        component: () => import('@/views/dashboard/Analytics.vue')
      },
      {
        path: 'reports',
        component: () => import('@/views/dashboard/Reports.vue')
      }
    ]
  }
]
```

#### Component-Based Code Splitting

```javascript
import { defineAsyncComponent } from 'vue'

// Simple async component
const AsyncComponent = defineAsyncComponent(() =>
  import('./components/AsyncComponent.vue')
)

// With loading and error states
const AsyncComponentWithOptions = defineAsyncComponent({
  loader: () => import('./components/HeavyComponent.vue'),
  loadingComponent: LoadingSpinner,
  errorComponent: ErrorDisplay,
  delay: 200,
  timeout: 3000,
  suspensible: false
})
```

### 5. Memoization and Caching

#### Use v-memo for Expensive Renders

```vue
<template>
  <!-- Re-render only when item.id or item.selected changes -->
  <div v-for="item in list" :key="item.id" v-memo="[item.id, item.selected]">
    <ExpensiveComponent :item="item" />
  </div>
</template>
```

#### Use v-once for Static Content

```vue
<template>
  <!-- Render once and never update -->
  <div v-once>
    <h1>{{ staticTitle }}</h1>
    <p>{{ staticDescription }}</p>
  </div>
</template>
```

### 6. Event Handling Optimization

#### Debounce and Throttle

```vue
<script setup>
import { ref } from 'vue'
import { useDebounceFn, useThrottleFn } from '@vueuse/core'

const searchQuery = ref('')
const searchResults = ref([])

// Debounce - Wait for user to stop typing
const debouncedSearch = useDebounceFn(async (query) => {
  searchResults.value = await api.search(query)
}, 500)

function handleInput(event) {
  searchQuery.value = event.target.value
  debouncedSearch(searchQuery.value)
}

// Throttle - Limit execution rate
const throttledScroll = useThrottleFn(() => {
  console.log('Scroll position:', window.scrollY)
}, 200)
</script>

<template>
  <input 
    :value="searchQuery" 
    @input="handleInput"
    placeholder="Search..."
  />
  
  <div @scroll="throttledScroll">
    <!-- Scrollable content -->
  </div>
</template>
```

#### Event Delegation

```vue
<template>
  <!-- ❌ Bad - Multiple event listeners -->
  <div>
    <button v-for="item in items" :key="item.id" @click="handleClick(item)">
      {{ item.name }}
    </button>
  </div>
  
  <!-- ✅ Good - Single event listener with delegation -->
  <div @click="handleDelegatedClick">
    <button v-for="item in items" :key="item.id" :data-id="item.id">
      {{ item.name }}
    </button>
  </div>
</template>

<script setup>
function handleDelegatedClick(event) {
  const button = event.target.closest('button')
  if (button) {
    const itemId = button.dataset.id
    // Handle click
  }
}
</script>
```

## Best Practices

### 1. Props Validation

```javascript
// ✅ Comprehensive prop validation
const props = defineProps({
  // Type check
  title: String,
  
  // Multiple types
  value: [String, Number],
  
  // Required prop with type
  id: {
    type: Number,
    required: true
  },
  
  // With default value
  status: {
    type: String,
    default: 'pending'
  },
  
  // Object/Array default (must use factory function)
  user: {
    type: Object,
    default: () => ({
      name: 'Guest',
      role: 'user'
    })
  },
  
  // Custom validator
  priority: {
    type: String,
    validator: (value) => {
      return ['low', 'medium', 'high'].includes(value)
    }
  },
  
  // Custom type
  callback: {
    type: Function,
    required: true
  }
})
```

### 2. Emit Validation

```javascript
// ✅ Define and validate emits
const emit = defineEmits({
  // No validation
  click: null,
  
  // With validation
  submit: (payload) => {
    if (!payload.email || !payload.password) {
      console.warn('Invalid submit payload')
      return false
    }
    return true
  },
  
  // Type checking
  update: (value) => typeof value === 'string'
})
```

### 3. Composable Best Practices

```javascript
// composables/useUser.js
import { ref, computed, readonly } from 'vue'
import { api } from '@/services/api'

export function useUser(userId) {
  // Private state
  const user = ref(null)
  const loading = ref(false)
  const error = ref(null)
  
  // Public computed
  const displayName = computed(() => {
    return user.value ? `${user.value.firstName} ${user.value.lastName}` : ''
  })
  
  // Public methods
  async function fetchUser() {
    loading.value = true
    error.value = null
    
    try {
      user.value = await api.getUser(userId.value)
    } catch (e) {
      error.value = e
    } finally {
      loading.value = false
    }
  }
  
  async function updateUser(updates) {
    try {
      user.value = await api.updateUser(userId.value, updates)
    } catch (e) {
      error.value = e
      throw e
    }
  }
  
  // Return public API
  return {
    // Readonly state
    user: readonly(user),
    loading: readonly(loading),
    error: readonly(error),
    // Computed
    displayName,
    // Methods
    fetchUser,
    updateUser
  }
}
```

### 4. Error Handling

```vue
<script setup>
import { ref, onErrorCaptured } from 'vue'

const error = ref(null)

// Capture errors from child components
onErrorCaptured((err, instance, info) => {
  error.value = {
    message: err.message,
    info
  }
  
  // Log to error tracking service
  console.error('Error captured:', err)
  
  // Return false to prevent propagation
  return false
})

// Global error handler (in main.js)
app.config.errorHandler = (err, instance, info) => {
  console.error('Global error:', err)
  // Send to error tracking service
}
</script>

<template>
  <div v-if="error" class="error">
    <h3>Something went wrong</h3>
    <p>{{ error.message }}</p>
  </div>
  <slot v-else></slot>
</template>
```

### 5. TypeScript Best Practices

```vue
<script setup lang="ts">
import { ref, computed } from 'vue'

// Define interfaces
interface User {
  id: number
  name: string
  email: string
  role: 'admin' | 'user' | 'guest'
}

interface Props {
  userId: number
  editable?: boolean
}

interface Emits {
  (e: 'update', user: User): void
  (e: 'delete', id: number): void
}

// Type-safe props
const props = withDefaults(defineProps<Props>(), {
  editable: false
})

// Type-safe emits
const emit = defineEmits<Emits>()

// Type-safe refs
const user = ref<User | null>(null)
const users = ref<User[]>([])

// Type-safe computed
const userName = computed<string>(() => user.value?.name ?? 'Unknown')

// Type-safe functions
function updateUser(updates: Partial<User>): void {
  if (user.value) {
    user.value = { ...user.value, ...updates }
    emit('update', user.value)
  }
}
</script>
```

### 6. Security Best Practices

```vue
<template>
  <!-- ❌ Dangerous - XSS vulnerability -->
  <div v-html="userInput"></div>
  
  <!-- ✅ Safe - Escaped by default -->
  <div>{{ userInput }}</div>
  
  <!-- ✅ Safe - Sanitize before using v-html -->
  <div v-html="sanitizedHtml"></div>
</template>

<script setup>
import DOMPurify from 'dompurify'
import { computed } from 'vue'

const props = defineProps(['userInput'])

const sanitizedHtml = computed(() => {
  return DOMPurify.sanitize(props.userInput)
})
</script>
```

## Conclusion

Following these best practices and optimization techniques will help you build performant, maintainable, and scalable Vue applications. Focus on:

1. **Code Organization**: Consistent structure and naming
2. **Performance**: Optimize reactivity, rendering, and loading
3. **Type Safety**: Use TypeScript and prop validation
4. **Error Handling**: Implement comprehensive error boundaries
5. **Security**: Sanitize user input and follow security guidelines

Regularly profile your application, measure performance, and optimize based on real-world usage patterns.
