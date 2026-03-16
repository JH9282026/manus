# Composables Patterns

Advanced patterns for creating reusable logic with Vue 3 Composition API.

---

## What Are Composables?

Composables are functions that leverage Vue's Composition API to encapsulate and reuse stateful logic. They are Vue 3's answer to React hooks and provide a superior alternative to Vue 2 mixins.

**Key Characteristics:**
- Functions that use Composition API features (`ref`, `reactive`, `computed`, etc.)
- Return reactive state and methods
- Can be composed together
- Naming convention: `use*` (e.g., `useMouse`, `useFetch`)

---

## Basic Composable Structure

```javascript
import { ref, onMounted, onUnmounted } from 'vue'

export function useMouse() {
  const x = ref(0)
  const y = ref(0)

  function update(event) {
    x.value = event.pageX
    y.value = event.pageY
  }

  onMounted(() => window.addEventListener('mousemove', update))
  onUnmounted(() => window.removeEventListener('mousemove', update))

  return { x, y }
}
```

**Usage in Component:**
```vue
<script setup>
import { useMouse } from './composables/useMouse'

const { x, y } = useMouse()
</script>

<template>
  <div>Mouse position: {{ x }}, {{ y }}</div>
</template>
```

---

## Advanced Patterns

### 1. Async Data Fetching

```javascript
import { ref, watchEffect } from 'vue'

export function useFetch(url) {
  const data = ref(null)
  const error = ref(null)
  const loading = ref(false)

  const fetchData = async () => {
    loading.value = true
    error.value = null
    
    try {
      const response = await fetch(url.value)
      data.value = await response.json()
    } catch (e) {
      error.value = e
    } finally {
      loading.value = false
    }
  }

  watchEffect(() => {
    if (url.value) fetchData()
  })

  return { data, error, loading, refetch: fetchData }
}
```

### 2. Local Storage Sync

```javascript
import { ref, watch } from 'vue'

export function useLocalStorage(key, defaultValue) {
  const storedValue = localStorage.getItem(key)
  const data = ref(storedValue ? JSON.parse(storedValue) : defaultValue)

  watch(data, (newValue) => {
    localStorage.setItem(key, JSON.stringify(newValue))
  }, { deep: true })

  return data
}
```

### 3. Debounced Input

```javascript
import { ref, customRef } from 'vue'

export function useDebouncedRef(value, delay = 300) {
  let timeout
  return customRef((track, trigger) => {
    return {
      get() {
        track()
        return value
      },
      set(newValue) {
        clearTimeout(timeout)
        timeout = setTimeout(() => {
          value = newValue
          trigger()
        }, delay)
      }
    }
  })
}
```

### 4. Event Bus (Alternative to $on/$off)

```javascript
import { ref } from 'vue'

const listeners = new Map()

export function useEventBus() {
  const emit = (event, ...args) => {
    const callbacks = listeners.get(event) || []
    callbacks.forEach(callback => callback(...args))
  }

  const on = (event, callback) => {
    if (!listeners.has(event)) {
      listeners.set(event, [])
    }
    listeners.get(event).push(callback)
  }

  const off = (event, callback) => {
    const callbacks = listeners.get(event) || []
    const index = callbacks.indexOf(callback)
    if (index > -1) callbacks.splice(index, 1)
  }

  return { emit, on, off }
}
```

### 5. Form Validation

```javascript
import { reactive, computed } from 'vue'

export function useForm(initialValues, validationRules) {
  const form = reactive({ ...initialValues })
  const errors = reactive({})
  const touched = reactive({})

  const validate = (field) => {
    const rules = validationRules[field]
    if (!rules) return true

    for (const rule of rules) {
      const error = rule(form[field])
      if (error) {
        errors[field] = error
        return false
      }
    }
    
    delete errors[field]
    return true
  }

  const validateAll = () => {
    let isValid = true
    for (const field in validationRules) {
      if (!validate(field)) isValid = false
    }
    return isValid
  }

  const handleBlur = (field) => {
    touched[field] = true
    validate(field)
  }

  const isValid = computed(() => Object.keys(errors).length === 0)

  return {
    form,
    errors,
    touched,
    isValid,
    validate,
    validateAll,
    handleBlur
  }
}
```

---

## Composing Multiple Composables

Composables can use other composables:

```javascript
import { useFetch } from './useFetch'
import { useLocalStorage } from './useLocalStorage'

export function useCachedFetch(url, cacheKey) {
  const cached = useLocalStorage(cacheKey, null)
  const { data, loading, error } = useFetch(url)

  watch(data, (newData) => {
    if (newData) cached.value = newData
  })

  return {
    data: computed(() => data.value || cached.value),
    loading,
    error
  }
}
```

---

## Best Practices

1. **Naming Convention**: Always prefix with `use` (e.g., `useMouse`, `useFetch`)
2. **Return Reactive Values**: Return `ref` or `reactive` objects, not plain values
3. **Accept Reactive Arguments**: Use `toValue()` or `unref()` to handle both refs and plain values
4. **Cleanup**: Always clean up side effects in `onUnmounted`
5. **Single Responsibility**: Each composable should do one thing well
6. **TypeScript**: Add proper type annotations for better DX
7. **Documentation**: Document parameters, return values, and usage examples

---

## Testing Composables

```javascript
import { describe, it, expect } from 'vitest'
import { useMouse } from './useMouse'

describe('useMouse', () => {
  it('tracks mouse position', async () => {
    const { x, y } = useMouse()
    
    // Simulate mouse move
    const event = new MouseEvent('mousemove', {
      pageX: 100,
      pageY: 200
    })
    window.dispatchEvent(event)
    
    await nextTick()
    expect(x.value).toBe(100)
    expect(y.value).toBe(200)
  })
})
```

---

## Common Composable Libraries

- **VueUse**: Collection of 200+ essential Vue composables
- **@vueuse/core**: Core utilities (mouse, keyboard, network, etc.)
- **@vueuse/motion**: Animation composables
- **@vueuse/gesture**: Touch and gesture composables

---

## Migration from Mixins

**Mixin (Vue 2):**
```javascript
export default {
  data() {
    return { x: 0, y: 0 }
  },
  mounted() {
    window.addEventListener('mousemove', this.update)
  },
  methods: {
    update(e) {
      this.x = e.pageX
      this.y = e.pageY
    }
  }
}
```

**Composable (Vue 3):**
```javascript
export function useMouse() {
  const x = ref(0)
  const y = ref(0)
  
  const update = (e) => {
    x.value = e.pageX
    y.value = e.pageY
  }
  
  onMounted(() => window.addEventListener('mousemove', update))
  onUnmounted(() => window.removeEventListener('mousemove', update))
  
  return { x, y }
}
```

**Benefits:**
- Clear source of `x` and `y`
- No naming conflicts
- Can use multiple mouse trackers
- Better TypeScript support
