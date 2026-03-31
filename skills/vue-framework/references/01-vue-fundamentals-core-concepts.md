# Vue.js Fundamentals and Core Concepts

## Introduction to Vue.js

Vue.js is a progressive JavaScript framework for building user interfaces. Unlike monolithic frameworks, Vue is designed from the ground up to be incrementally adoptable. The core library focuses on the view layer only, making it easy to integrate with other libraries or existing projects.

### Philosophy and Design Principles

**Progressive Framework**
Vue's progressive nature means you can use as much or as little of the framework as needed:
- Drop-in enhancement for static HTML
- Embedded web components
- Single-Page Applications (SPAs)
- Full-stack / Server-Side Rendering (SSR)
- Jamstack / Static Site Generation (SSG)
- Targeting desktop, mobile, WebGL, and terminal

**Approachable and Versatile**
- Familiar HTML-based template syntax
- Component-based architecture
- Reactive data binding
- Flexible and composable

**Performant**
- Virtual DOM implementation
- Optimized re-rendering
- Automatic dependency tracking
- Efficient updates

## Core Concepts

### 1. Reactivity System

Vue's reactivity system is the heart of the framework, automatically tracking dependencies and updating the DOM when data changes.

**Vue 3 Reactivity (Proxy-based)**
```javascript
import { reactive, ref, computed, watch } from 'vue'

// Reactive objects
const state = reactive({
  count: 0,
  message: 'Hello Vue'
})

// Reactive primitives
const count = ref(0)
const doubled = computed(() => count.value * 2)

// Watchers
watch(count, (newValue, oldValue) => {
  console.log(`Count changed from ${oldValue} to ${newValue}`)
})
```

**Key Reactivity APIs**
- `reactive()`: Creates a reactive proxy of an object
- `ref()`: Creates a reactive reference for primitive values
- `computed()`: Creates a computed property that automatically updates
- `watch()`: Watches reactive sources and performs side effects
- `watchEffect()`: Automatically tracks dependencies and re-runs

**Reactivity Fundamentals**
```javascript
// Deep reactivity
const state = reactive({
  nested: {
    count: 0
  }
})
state.nested.count++ // Reactive

// Ref unwrapping
const count = ref(0)
const state = reactive({ count })
console.log(state.count) // 0 (automatically unwrapped)

// toRefs for destructuring
import { toRefs } from 'vue'
const { count, message } = toRefs(state)
```

### 2. Component System

Components are reusable Vue instances with custom names and encapsulated logic.

**Component Definition (Composition API)**
```vue
<script setup>
import { ref, computed } from 'vue'

// Props
const props = defineProps({
  title: String,
  count: {
    type: Number,
    default: 0,
    validator: (value) => value >= 0
  }
})

// Emits
const emit = defineEmits(['update', 'delete'])

// State
const localCount = ref(props.count)

// Computed
const doubled = computed(() => localCount.value * 2)

// Methods
function increment() {
  localCount.value++
  emit('update', localCount.value)
}

// Expose to template
defineExpose({
  increment,
  localCount
})
</script>

<template>
  <div class="counter">
    <h2>{{ title }}</h2>
    <p>Count: {{ localCount }}</p>
    <p>Doubled: {{ doubled }}</p>
    <button @click="increment">Increment</button>
  </div>
</template>

<style scoped>
.counter {
  padding: 20px;
  border: 1px solid #ccc;
}
</style>
```

**Component Definition (Options API)**
```vue
<script>
export default {
  name: 'Counter',
  props: {
    title: String,
    initialCount: {
      type: Number,
      default: 0
    }
  },
  data() {
    return {
      count: this.initialCount
    }
  },
  computed: {
    doubled() {
      return this.count * 2
    }
  },
  methods: {
    increment() {
      this.count++
      this.$emit('update', this.count)
    }
  },
  mounted() {
    console.log('Component mounted')
  }
}
</script>
```

### 3. Template Syntax

Vue uses HTML-based template syntax for declarative rendering.

**Text Interpolation**
```vue
<template>
  <span>Message: {{ msg }}</span>
  <span>Raw HTML: <span v-html="rawHtml"></span></span>
</template>
```

**Directives**
```vue
<template>
  <!-- Conditional rendering -->
  <div v-if="type === 'A'">Type A</div>
  <div v-else-if="type === 'B'">Type B</div>
  <div v-else>Not A or B</div>
  
  <!-- Show/hide (CSS display) -->
  <div v-show="isVisible">Visible content</div>
  
  <!-- List rendering -->
  <ul>
    <li v-for="(item, index) in items" :key="item.id">
      {{ index }}: {{ item.name }}
    </li>
  </ul>
  
  <!-- Event handling -->
  <button @click="handleClick">Click me</button>
  <button @click.prevent="handleSubmit">Submit</button>
  <input @keyup.enter="handleEnter">
  
  <!-- Two-way binding -->
  <input v-model="message">
  <input v-model.number="age">
  <input v-model.trim="username">
  
  <!-- Attribute binding -->
  <div :id="dynamicId" :class="{ active: isActive }"></div>
  <img :src="imageSrc" :alt="imageAlt">
  
  <!-- Dynamic arguments -->
  <a :[attributeName]="url">Link</a>
  <button @[eventName]="handler">Button</button>
</template>
```

**Class and Style Bindings**
```vue
<template>
  <!-- Object syntax -->
  <div :class="{ active: isActive, 'text-danger': hasError }"></div>
  <div :style="{ color: activeColor, fontSize: fontSize + 'px' }"></div>
  
  <!-- Array syntax -->
  <div :class="[activeClass, errorClass]"></div>
  <div :style="[baseStyles, overridingStyles]"></div>
  
  <!-- Mixed -->
  <div :class="[{ active: isActive }, errorClass]"></div>
</template>
```

### 4. Lifecycle Hooks

Components have lifecycle hooks for executing code at specific stages.

**Composition API Lifecycle**
```javascript
import { 
  onBeforeMount,
  onMounted,
  onBeforeUpdate,
  onUpdated,
  onBeforeUnmount,
  onUnmounted,
  onErrorCaptured
} from 'vue'

export default {
  setup() {
    onBeforeMount(() => {
      console.log('Before mount')
    })
    
    onMounted(() => {
      console.log('Mounted - DOM is ready')
      // API calls, DOM manipulation, timers
    })
    
    onBeforeUpdate(() => {
      console.log('Before update')
    })
    
    onUpdated(() => {
      console.log('Updated - DOM re-rendered')
    })
    
    onBeforeUnmount(() => {
      console.log('Before unmount')
      // Cleanup: remove event listeners, cancel timers
    })
    
    onUnmounted(() => {
      console.log('Unmounted')
    })
    
    onErrorCaptured((err, instance, info) => {
      console.error('Error captured:', err)
      return false // Prevent propagation
    })
  }
}
```

**Options API Lifecycle**
```javascript
export default {
  beforeCreate() {
    // Before instance initialization
  },
  created() {
    // Instance created, data reactive
  },
  beforeMount() {
    // Before DOM mount
  },
  mounted() {
    // DOM mounted and accessible
  },
  beforeUpdate() {
    // Before DOM update
  },
  updated() {
    // After DOM update
  },
  beforeUnmount() {
    // Before component unmount
  },
  unmounted() {
    // Component unmounted
  }
}
```

### 5. Composition API

The Composition API provides a set of function-based APIs for better code organization and reusability.

**Basic Setup**
```vue
<script setup>
import { ref, reactive, computed, watch, onMounted } from 'vue'

// Reactive state
const count = ref(0)
const user = reactive({
  name: 'John',
  age: 30
})

// Computed properties
const doubleCount = computed(() => count.value * 2)

// Methods
function increment() {
  count.value++
}

// Watchers
watch(count, (newVal, oldVal) => {
  console.log(`Count: ${oldVal} -> ${newVal}`)
})

// Lifecycle
onMounted(() => {
  console.log('Component mounted')
})
</script>
```

**Composables (Reusable Logic)**
```javascript
// composables/useMouse.js
import { ref, onMounted, onUnmounted } from 'vue'

export function useMouse() {
  const x = ref(0)
  const y = ref(0)
  
  function update(event) {
    x.value = event.pageX
    y.value = event.pageY
  }
  
  onMounted(() => {
    window.addEventListener('mousemove', update)
  })
  
  onUnmounted(() => {
    window.removeEventListener('mousemove', update)
  })
  
  return { x, y }
}

// Usage in component
import { useMouse } from './composables/useMouse'

const { x, y } = useMouse()
```

**Advanced Composable Patterns**
```javascript
// composables/useFetch.js
import { ref, watchEffect, toValue } from 'vue'

export function useFetch(url) {
  const data = ref(null)
  const error = ref(null)
  const loading = ref(false)
  
  watchEffect(async () => {
    loading.value = true
    data.value = null
    error.value = null
    
    try {
      const urlValue = toValue(url)
      const res = await fetch(urlValue)
      data.value = await res.json()
    } catch (e) {
      error.value = e
    } finally {
      loading.value = false
    }
  })
  
  return { data, error, loading }
}

// Usage
const url = ref('/api/users')
const { data, error, loading } = useFetch(url)
```

### 6. Props and Events

**Props Definition and Validation**
```javascript
// Composition API
const props = defineProps({
  // Basic type check
  title: String,
  likes: Number,
  isPublished: Boolean,
  commentIds: Array,
  author: Object,
  callback: Function,
  
  // Multiple types
  propA: [String, Number],
  
  // Required prop
  propB: {
    type: String,
    required: true
  },
  
  // With default value
  propC: {
    type: Number,
    default: 100
  },
  
  // Object/array defaults
  propD: {
    type: Object,
    default: () => ({ message: 'hello' })
  },
  
  // Custom validator
  propE: {
    type: String,
    validator: (value) => {
      return ['success', 'warning', 'danger'].includes(value)
    }
  }
})
```

**Events**
```javascript
// Define emits
const emit = defineEmits({
  // No validation
  click: null,
  
  // With validation
  submit: (payload) => {
    return payload.email && payload.password
  }
})

// Emit events
emit('click')
emit('submit', { email: 'test@example.com', password: '123' })

// Parent component
<ChildComponent 
  @click="handleClick"
  @submit="handleSubmit"
/>
```

### 7. Slots

Slots allow parent components to pass template content to child components.

**Basic Slots**
```vue
<!-- Child component -->
<template>
  <div class="container">
    <header>
      <slot name="header"></slot>
    </header>
    <main>
      <slot></slot> <!-- Default slot -->
    </main>
    <footer>
      <slot name="footer"></slot>
    </footer>
  </div>
</template>

<!-- Parent component -->
<template>
  <Container>
    <template #header>
      <h1>Page Title</h1>
    </template>
    
    <p>Main content goes here</p>
    
    <template #footer>
      <p>Footer content</p>
    </template>
  </Container>
</template>
```

**Scoped Slots**
```vue
<!-- Child component -->
<template>
  <ul>
    <li v-for="item in items" :key="item.id">
      <slot :item="item" :index="index"></slot>
    </li>
  </ul>
</template>

<!-- Parent component -->
<template>
  <ItemList :items="items">
    <template #default="{ item, index }">
      <span>{{ index }}: {{ item.name }}</span>
    </template>
  </ItemList>
</template>
```

### 8. Provide/Inject

Provide and inject enable dependency injection for passing data through component trees.

```javascript
// Parent/Ancestor component
import { provide, ref } from 'vue'

const theme = ref('dark')
const updateTheme = (newTheme) => {
  theme.value = newTheme
}

provide('theme', theme)
provide('updateTheme', updateTheme)

// Child/Descendant component
import { inject } from 'vue'

const theme = inject('theme')
const updateTheme = inject('updateTheme')

// With default value
const theme = inject('theme', 'light')
```

## Vue 3 vs Vue 2

### Major Differences

**Performance Improvements**
- Faster mounting and patching
- Smaller bundle size
- Better memory usage
- Optimized reactivity system

**Composition API**
- Better TypeScript support
- More flexible code organization
- Easier logic reuse
- Better type inference

**New Features**
- Multiple root elements (Fragments)
- Teleport component
- Suspense component
- Better TypeScript integration

**Breaking Changes**
- Global API changes (createApp instead of new Vue)
- v-model changes
- Filters removed
- $listeners merged into $attrs

## Best Practices

### Component Design
1. Keep components small and focused
2. Use composition for reusable logic
3. Prefer Composition API for complex components
4. Use props for parent-to-child communication
5. Use events for child-to-parent communication

### Reactivity
1. Use `ref()` for primitives, `reactive()` for objects
2. Avoid losing reactivity when destructuring
3. Use `computed()` for derived state
4. Be careful with async operations in watchers

### Performance
1. Use `v-show` for frequent toggles, `v-if` for conditional rendering
2. Always use `:key` with `v-for`
3. Avoid `v-if` with `v-for` on the same element
4. Use `shallowRef` and `shallowReactive` for large data structures
5. Implement virtual scrolling for long lists

### Code Organization
1. Use composables for shared logic
2. Keep template logic simple
3. Extract complex computed logic
4. Use TypeScript for better type safety
5. Follow consistent naming conventions

## Conclusion

Vue.js provides a powerful yet approachable framework for building modern web applications. Understanding these core concepts—reactivity, components, template syntax, lifecycle hooks, and the Composition API—forms the foundation for building robust Vue applications. The framework's progressive nature allows developers to adopt features incrementally while maintaining excellent performance and developer experience.
