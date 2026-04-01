# Vue Component Architecture and Design Patterns

## Component Architecture Principles

### Single Responsibility Principle

Each component should have one clear purpose and responsibility.

**Good Example:**
```vue
<!-- UserProfile.vue - Displays user information -->
<template>
  <div class="user-profile">
    <UserAvatar :user="user" />
    <UserInfo :user="user" />
    <UserStats :stats="user.stats" />
  </div>
</template>

<!-- UserAvatar.vue - Handles avatar display -->
<template>
  <img :src="user.avatar" :alt="user.name" class="avatar" />
</template>

<!-- UserInfo.vue - Handles user details -->
<template>
  <div class="user-info">
    <h2>{{ user.name }}</h2>
    <p>{{ user.bio }}</p>
  </div>
</template>
```

**Bad Example:**
```vue
<!-- Monolithic component doing too much -->
<template>
  <div>
    <img :src="user.avatar" />
    <h2>{{ user.name }}</h2>
    <p>{{ user.bio }}</p>
    <div>{{ user.stats }}</div>
    <form @submit="updateUser">...</form>
    <div>{{ user.posts }}</div>
    <div>{{ user.comments }}</div>
  </div>
</template>
```

### Component Composition Patterns

#### 1. Container/Presentational Pattern

Separate data management from presentation.

**Container Component (Smart)**
```vue
<!-- UserListContainer.vue -->
<script setup>
import { ref, onMounted } from 'vue'
import UserList from './UserList.vue'
import { fetchUsers } from '@/api/users'

const users = ref([])
const loading = ref(false)
const error = ref(null)

const loadUsers = async () => {
  loading.value = true
  try {
    users.value = await fetchUsers()
  } catch (e) {
    error.value = e.message
  } finally {
    loading.value = false
  }
}

const handleUserSelect = (user) => {
  // Handle business logic
  console.log('Selected:', user)
}

onMounted(loadUsers)
</script>

<template>
  <UserList 
    :users="users"
    :loading="loading"
    :error="error"
    @select="handleUserSelect"
    @refresh="loadUsers"
  />
</template>
```

**Presentational Component (Dumb)**
```vue
<!-- UserList.vue -->
<script setup>
defineProps({
  users: {
    type: Array,
    required: true
  },
  loading: Boolean,
  error: String
})

const emit = defineEmits(['select', 'refresh'])
</script>

<template>
  <div class="user-list">
    <div v-if="loading">Loading...</div>
    <div v-else-if="error" class="error">{{ error }}</div>
    <div v-else>
      <div 
        v-for="user in users" 
        :key="user.id"
        @click="emit('select', user)"
        class="user-item"
      >
        {{ user.name }}
      </div>
    </div>
    <button @click="emit('refresh')">Refresh</button>
  </div>
</template>
```

#### 2. Compound Components Pattern

Components that work together to form a cohesive interface.

```vue
<!-- Accordion.vue -->
<script setup>
import { provide, ref } from 'vue'

const activeIndex = ref(0)

provide('accordion', {
  activeIndex,
  setActive: (index) => {
    activeIndex.value = index
  }
})
</script>

<template>
  <div class="accordion">
    <slot></slot>
  </div>
</template>

<!-- AccordionItem.vue -->
<script setup>
import { inject, computed } from 'vue'

const props = defineProps({
  index: {
    type: Number,
    required: true
  },
  title: String
})

const accordion = inject('accordion')
const isActive = computed(() => accordion.activeIndex.value === props.index)

const toggle = () => {
  accordion.setActive(props.index)
}
</script>

<template>
  <div class="accordion-item">
    <div class="accordion-header" @click="toggle">
      {{ title }}
    </div>
    <div v-show="isActive" class="accordion-content">
      <slot></slot>
    </div>
  </div>
</template>

<!-- Usage -->
<template>
  <Accordion>
    <AccordionItem :index="0" title="Section 1">
      Content 1
    </AccordionItem>
    <AccordionItem :index="1" title="Section 2">
      Content 2
    </AccordionItem>
  </Accordion>
</template>
```

#### 3. Renderless Components Pattern

Components that provide logic without rendering UI.

```vue
<!-- MouseTracker.vue -->
<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const x = ref(0)
const y = ref(0)

const update = (event) => {
  x.value = event.pageX
  y.value = event.pageY
}

onMounted(() => {
  window.addEventListener('mousemove', update)
})

onUnmounted(() => {
  window.removeEventListener('mousemove', update)
})
</script>

<template>
  <slot :x="x" :y="y"></slot>
</template>

<!-- Usage -->
<template>
  <MouseTracker v-slot="{ x, y }">
    <div>Mouse position: {{ x }}, {{ y }}</div>
  </MouseTracker>
</template>
```

#### 4. Higher-Order Components (HOC) Pattern

Components that wrap other components to add functionality.

```javascript
// withLoading.js
import { h } from 'vue'

export function withLoading(Component) {
  return {
    name: `WithLoading${Component.name}`,
    props: {
      ...Component.props,
      loading: Boolean
    },
    setup(props, { attrs, slots }) {
      return () => {
        if (props.loading) {
          return h('div', { class: 'loading' }, 'Loading...')
        }
        return h(Component, { ...props, ...attrs }, slots)
      }
    }
  }
}

// Usage
import UserList from './UserList.vue'
import { withLoading } from './withLoading'

const UserListWithLoading = withLoading(UserList)
```

### State Management Patterns

#### 1. Local State

For component-specific state.

```vue
<script setup>
import { ref } from 'vue'

const count = ref(0)
const message = ref('')

function increment() {
  count.value++
}
</script>
```

#### 2. Shared State with Composables

For state shared across multiple components.

```javascript
// stores/useCounter.js
import { ref, computed } from 'vue'

const count = ref(0)

export function useCounter() {
  const doubled = computed(() => count.value * 2)
  
  function increment() {
    count.value++
  }
  
  function decrement() {
    count.value--
  }
  
  return {
    count,
    doubled,
    increment,
    decrement
  }
}

// Usage in multiple components
import { useCounter } from '@/stores/useCounter'

const { count, increment } = useCounter()
```

#### 3. Pinia Store Pattern

For application-wide state management.

```javascript
// stores/user.js
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useUserStore = defineStore('user', () => {
  // State
  const user = ref(null)
  const loading = ref(false)
  const error = ref(null)
  
  // Getters
  const isAuthenticated = computed(() => !!user.value)
  const userName = computed(() => user.value?.name || 'Guest')
  
  // Actions
  async function login(credentials) {
    loading.value = true
    error.value = null
    try {
      const response = await api.login(credentials)
      user.value = response.data
    } catch (e) {
      error.value = e.message
      throw e
    } finally {
      loading.value = false
    }
  }
  
  function logout() {
    user.value = null
  }
  
  return {
    user,
    loading,
    error,
    isAuthenticated,
    userName,
    login,
    logout
  }
})

// Usage
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()
await userStore.login({ email, password })
```

### Communication Patterns

#### 1. Props Down, Events Up

Standard parent-child communication.

```vue
<!-- Parent -->
<template>
  <ChildComponent 
    :data="parentData"
    @update="handleUpdate"
  />
</template>

<!-- Child -->
<script setup>
const props = defineProps(['data'])
const emit = defineEmits(['update'])

function updateData(newData) {
  emit('update', newData)
}
</script>
```

#### 2. Event Bus Pattern (Vue 3)

For loosely coupled components.

```javascript
// eventBus.js
import { ref } from 'vue'

class EventBus {
  constructor() {
    this.events = {}
  }
  
  on(event, callback) {
    if (!this.events[event]) {
      this.events[event] = []
    }
    this.events[event].push(callback)
  }
  
  emit(event, data) {
    if (this.events[event]) {
      this.events[event].forEach(callback => callback(data))
    }
  }
  
  off(event, callback) {
    if (this.events[event]) {
      this.events[event] = this.events[event].filter(cb => cb !== callback)
    }
  }
}

export const eventBus = new EventBus()

// Usage
import { eventBus } from '@/utils/eventBus'
import { onUnmounted } from 'vue'

// Component A
eventBus.emit('user-updated', userData)

// Component B
const handleUserUpdate = (data) => {
  console.log('User updated:', data)
}

eventBus.on('user-updated', handleUserUpdate)

onUnmounted(() => {
  eventBus.off('user-updated', handleUserUpdate)
})
```

#### 3. Provide/Inject Pattern

For dependency injection across component trees.

```vue
<!-- App.vue -->
<script setup>
import { provide, ref } from 'vue'

const theme = ref('light')
const toggleTheme = () => {
  theme.value = theme.value === 'light' ? 'dark' : 'light'
}

provide('theme', {
  theme,
  toggleTheme
})
</script>

<!-- Deeply nested component -->
<script setup>
import { inject } from 'vue'

const { theme, toggleTheme } = inject('theme')
</script>
```

### Advanced Component Patterns

#### 1. Dynamic Components

```vue
<script setup>
import { ref, shallowRef } from 'vue'
import ComponentA from './ComponentA.vue'
import ComponentB from './ComponentB.vue'

const currentComponent = shallowRef(ComponentA)
const components = {
  ComponentA,
  ComponentB
}

function switchComponent(name) {
  currentComponent.value = components[name]
}
</script>

<template>
  <component :is="currentComponent" />
  
  <button @click="switchComponent('ComponentA')">Show A</button>
  <button @click="switchComponent('ComponentB')">Show B</button>
</template>
```

#### 2. Async Components

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
  timeout: 3000
})
```

#### 3. Recursive Components

```vue
<!-- TreeNode.vue -->
<script setup>
import { ref } from 'vue'

const props = defineProps({
  node: {
    type: Object,
    required: true
  }
})

const isExpanded = ref(false)
</script>

<template>
  <div class="tree-node">
    <div @click="isExpanded = !isExpanded">
      {{ node.name }}
    </div>
    <div v-if="isExpanded && node.children" class="children">
      <TreeNode 
        v-for="child in node.children" 
        :key="child.id"
        :node="child"
      />
    </div>
  </div>
</template>
```

#### 4. Teleport Pattern

Render components in different DOM locations.

```vue
<!-- Modal.vue -->
<template>
  <Teleport to="body">
    <div v-if="isOpen" class="modal-overlay">
      <div class="modal">
        <slot></slot>
        <button @click="close">Close</button>
      </div>
    </div>
  </Teleport>
</template>

<script setup>
defineProps(['isOpen'])
const emit = defineEmits(['close'])

function close() {
  emit('close')
}
</script>
```

### Performance Optimization Patterns

#### 1. Lazy Loading

```javascript
// Route-based lazy loading
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

// Component-based lazy loading
const HeavyComponent = defineAsyncComponent(() =>
  import('./components/HeavyComponent.vue')
)
```

#### 2. Virtual Scrolling

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
    default: 10
  }
})

const scrollTop = ref(0)

const visibleItems = computed(() => {
  const start = Math.floor(scrollTop.value / props.itemHeight)
  const end = start + props.visibleCount
  return props.items.slice(start, end).map((item, index) => ({
    item,
    index: start + index
  }))
})

const totalHeight = computed(() => props.items.length * props.itemHeight)
const offsetY = computed(() => Math.floor(scrollTop.value / props.itemHeight) * props.itemHeight)

function handleScroll(event) {
  scrollTop.value = event.target.scrollTop
}
</script>

<template>
  <div class="virtual-scroll" @scroll="handleScroll">
    <div :style="{ height: totalHeight + 'px' }">
      <div :style="{ transform: `translateY(${offsetY}px)` }">
        <div 
          v-for="{ item, index } in visibleItems" 
          :key="index"
          :style="{ height: itemHeight + 'px' }"
        >
          <slot :item="item" :index="index"></slot>
        </div>
      </div>
    </div>
  </div>
</template>
```

#### 3. Memoization with Computed

```vue
<script setup>
import { ref, computed } from 'vue'

const items = ref([])
const filter = ref('')

// Expensive computation cached
const filteredItems = computed(() => {
  return items.value.filter(item => 
    item.name.toLowerCase().includes(filter.value.toLowerCase())
  )
})

// Multiple dependent computeds
const sortedItems = computed(() => {
  return [...filteredItems.value].sort((a, b) => a.name.localeCompare(b.name))
})
</script>
```

### Testing Patterns

#### 1. Component Testing Setup

```javascript
import { mount } from '@vue/test-utils'
import { describe, it, expect } from 'vitest'
import Counter from './Counter.vue'

describe('Counter', () => {
  it('increments count when button clicked', async () => {
    const wrapper = mount(Counter)
    
    expect(wrapper.text()).toContain('Count: 0')
    
    await wrapper.find('button').trigger('click')
    
    expect(wrapper.text()).toContain('Count: 1')
  })
  
  it('accepts initial count prop', () => {
    const wrapper = mount(Counter, {
      props: {
        initialCount: 5
      }
    })
    
    expect(wrapper.text()).toContain('Count: 5')
  })
})
```

#### 2. Testing with Pinia

```javascript
import { setActivePinia, createPinia } from 'pinia'
import { useUserStore } from '@/stores/user'

describe('User Store', () => {
  beforeEach(() => {
    setActivePinia(createPinia())
  })
  
  it('logs in user', async () => {
    const store = useUserStore()
    
    await store.login({ email: 'test@example.com', password: '123' })
    
    expect(store.isAuthenticated).toBe(true)
    expect(store.user).toBeDefined()
  })
})
```

## Best Practices

### Component Organization

1. **File Structure**
```
components/
├── base/           # Base UI components
├── common/         # Shared components
├── features/       # Feature-specific components
└── layouts/        # Layout components
```

2. **Naming Conventions**
- PascalCase for component files: `UserProfile.vue`
- Multi-word component names: `BaseButton.vue`, not `Button.vue`
- Prefix base components: `BaseButton`, `BaseInput`
- Prefix single-instance components: `TheHeader`, `TheSidebar`

3. **Component Size**
- Keep components under 200 lines
- Extract complex logic to composables
- Split large components into smaller ones

### Props and Events

1. **Props Validation**
- Always validate props
- Provide default values
- Use TypeScript for better type safety

2. **Event Naming**
- Use kebab-case for event names
- Prefix with action: `update:modelValue`, `submit:form`
- Be specific: `user:created`, not just `created`

### Performance

1. **Use `v-once` for static content**
2. **Use `v-memo` for expensive renders**
3. **Implement virtual scrolling for long lists**
4. **Lazy load routes and heavy components**
5. **Use `shallowRef` for large objects**

## Conclusion

Effective Vue component architecture relies on understanding and applying appropriate design patterns. By following these patterns and best practices, you can build maintainable, scalable, and performant Vue applications. The key is choosing the right pattern for your specific use case and maintaining consistency throughout your codebase.
