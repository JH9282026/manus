# Reactivity System Deep Dive

Understanding Vue 3's proxy-based reactivity system and optimization techniques.

---

## How Vue 3 Reactivity Works

Vue 3 uses ES6 Proxies to track reactive dependencies, replacing Vue 2's `Object.defineProperty` approach.

**Key Advantages:**
- Automatic detection of property additions/deletions
- Array index and length modifications tracked automatically
- Better performance for large objects
- No need for `Vue.set()` or `Vue.delete()`

---

## Reactive Primitives

### `ref()`

```javascript
import { ref } from 'vue'

const count = ref(0)
console.log(count.value) // 0
count.value++
console.log(count.value) // 1
```

**Internals:**
- Wraps value in an object with `.value` property
- Getter/setter track dependencies and trigger updates
- Automatically unwrapped in templates
- Can hold any value type (primitives, objects, arrays)

**When to Use:**
- Primitives (string, number, boolean)
- Single values that need reactivity
- When you need to reassign entire value

### `reactive()`

```javascript
import { reactive } from 'vue'

const state = reactive({
  count: 0,
  user: { name: 'John' }
})

state.count++ // Reactive
state.user.name = 'Jane' // Reactive (deep)
```

**Internals:**
- Returns a Proxy of the original object
- Deep reactivity by default
- Cannot be reassigned (loses reactivity)
- Only works with objects and arrays

**When to Use:**
- Objects with multiple properties
- When you don't want `.value` syntax
- Form data, configuration objects

### `computed()`

```javascript
import { ref, computed } from 'vue'

const count = ref(0)
const doubled = computed(() => count.value * 2)

console.log(doubled.value) // 0
count.value = 5
console.log(doubled.value) // 10
```

**Internals:**
- Lazy evaluation (only computes when accessed)
- Caches result until dependencies change
- Tracks dependencies automatically
- Read-only by default (can be writable with getter/setter)

**Performance Benefits:**
- Avoids redundant calculations
- Only re-computes when dependencies change
- Better than methods for expensive operations

---

## Reactivity Gotchas

### 1. Destructuring Reactive Objects

**Problem:**
```javascript
const state = reactive({ count: 0 })
const { count } = state // ❌ Loses reactivity
count++ // Won't trigger updates
```

**Solution:**
```javascript
import { toRefs } from 'vue'

const state = reactive({ count: 0 })
const { count } = toRefs(state) // ✅ Preserves reactivity
count.value++ // Triggers updates
```

### 2. Reassigning Reactive Objects

**Problem:**
```javascript
let state = reactive({ count: 0 })
state = reactive({ count: 1 }) // ❌ Loses reactivity for original references
```

**Solution:**
```javascript
const state = ref({ count: 0 })
state.value = { count: 1 } // ✅ Maintains reactivity
```

### 3. Array Mutations

**Vue 3 (Proxy-based):**
```javascript
const arr = reactive([1, 2, 3])
arr[0] = 10 // ✅ Reactive
arr.length = 0 // ✅ Reactive
arr.push(4) // ✅ Reactive
```

**Vue 2 (Object.defineProperty):**
```javascript
const arr = [1, 2, 3]
arr[0] = 10 // ❌ Not reactive
Vue.set(arr, 0, 10) // ✅ Required in Vue 2
```

---

## Advanced Reactivity APIs

### `shallowRef()` and `shallowReactive()`

**Use Case:** Large data structures where deep reactivity is expensive.

```javascript
import { shallowRef, triggerRef } from 'vue'

const state = shallowRef({
  nested: { count: 0 }
})

// Nested properties are NOT reactive
state.value.nested.count++ // Won't trigger updates

// Must replace entire object
state.value = { nested: { count: 1 } } // ✅ Triggers update

// Or manually trigger
state.value.nested.count++
triggerRef(state) // ✅ Force update
```

**Performance Benefit:** Avoids deep proxy wrapping for large objects.

### `readonly()`

```javascript
import { reactive, readonly } from 'vue'

const state = reactive({ count: 0 })
const readonlyState = readonly(state)

readonlyState.count++ // ⚠️ Warning in dev, no-op in production
```

**Use Case:** Prevent mutations in child components.

### `markRaw()`

```javascript
import { reactive, markRaw } from 'vue'

const state = reactive({
  user: { name: 'John' },
  largeObject: markRaw({ /* huge data */ })
})

// largeObject is NOT reactive
state.largeObject.property = 'value' // Won't trigger updates
```

**Use Case:** Third-party class instances, large immutable data.

### `toRaw()`

```javascript
import { reactive, toRaw } from 'vue'

const state = reactive({ count: 0 })
const raw = toRaw(state)

raw.count++ // Won't trigger updates
```

**Use Case:** Passing data to non-Vue libraries, performance-critical operations.

---

## Watchers

### `watch()`

```javascript
import { ref, watch } from 'vue'

const count = ref(0)

watch(count, (newValue, oldValue) => {
  console.log(`Count changed from ${oldValue} to ${newValue}`)
})

// Watch multiple sources
watch([count, anotherRef], ([newCount, newAnother], [oldCount, oldAnother]) => {
  // ...
})

// Watch reactive object property
watch(
  () => state.count,
  (newValue) => { /* ... */ }
)
```

**Options:**
- `immediate: true` — Run immediately
- `deep: true` — Watch nested properties
- `flush: 'post'` — Run after component updates

### `watchEffect()`

```javascript
import { ref, watchEffect } from 'vue'

const count = ref(0)
const doubled = ref(0)

watchEffect(() => {
  doubled.value = count.value * 2
  console.log(`Doubled: ${doubled.value}`)
})

// Runs immediately and whenever count changes
```

**Differences from `watch()`:**
- Automatic dependency tracking
- Runs immediately by default
- No access to old values
- Simpler for side effects

### `watchPostEffect()` and `watchSyncEffect()`

```javascript
import { watchPostEffect, watchSyncEffect } from 'vue'

// Runs after component updates (access DOM)
watchPostEffect(() => {
  console.log(document.getElementById('el').textContent)
})

// Runs synchronously (use sparingly)
watchSyncEffect(() => {
  // Runs before DOM updates
})
```

---

## Reactivity Transform (Experimental)

**Note:** Deprecated in Vue 3.4, but understanding it helps with migration.

```javascript
// With reactivity transform
let count = $ref(0)
console.log(count) // No .value needed
count++

// Compiles to:
let count = ref(0)
console.log(count.value)
count.value++
```

---

## Performance Optimization

### 1. Use `shallowRef` for Large Objects

```javascript
const largeArray = shallowRef([
  /* thousands of items */
])

// Update entire array instead of mutating
largeArray.value = [...largeArray.value, newItem]
```

### 2. Avoid Unnecessary Computed Properties

**Bad:**
```javascript
const fullName = computed(() => `${firstName.value} ${lastName.value}`)
```

**Good (if only used in template once):**
```vue
<template>
  <div>{{ firstName }} {{ lastName }}</div>
</template>
```

### 3. Use `v-once` for Static Content

```vue
<template>
  <div v-once>{{ staticContent }}</div>
</template>
```

### 4. Debounce Expensive Watchers

```javascript
import { debounce } from 'lodash-es'

watch(
  searchQuery,
  debounce((newQuery) => {
    // Expensive API call
  }, 300)
)
```

---

## Debugging Reactivity

### Track Reactive Dependencies

```javascript
import { watchEffect } from 'vue'

watchEffect(() => {
  console.log('Dependencies:', count.value, user.name)
}, {
  onTrack(e) {
    console.log('Tracked:', e)
  },
  onTrigger(e) {
    console.log('Triggered:', e)
  }
})
```

### Check if Value is Reactive

```javascript
import { isRef, isReactive, isProxy } from 'vue'

console.log(isRef(count)) // true
console.log(isReactive(state)) // true
console.log(isProxy(state)) // true
```

---

## Common Patterns

### 1. Reactive Props

```javascript
import { toRefs } from 'vue'

const props = defineProps(['user'])
const { user } = toRefs(props) // Make props reactive in setup
```

### 2. Reactive Route Params

```javascript
import { computed } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const userId = computed(() => route.params.id)
```

### 3. Reactive Store State

```javascript
import { storeToRefs } from 'pinia'
import { useUserStore } from '@/stores/user'

const store = useUserStore()
const { user, isLoggedIn } = storeToRefs(store) // Reactive refs
```
