# Stores and State Management

Comprehensive guide to managing state in Svelte applications.

---

## Svelte Stores

Stores are reactive containers for values that can be shared across components.

### Writable Store

**Create:**
```javascript
// stores.js
import { writable } from 'svelte/store'

export const count = writable(0)
```

**Use:**
```svelte
<script>
  import { count } from './stores.js'
  
  function increment() {
    count.update(n => n + 1)
  }
  
  function reset() {
    count.set(0)
  }
</script>

<button on:click={increment}>
  Count: {$count}
</button>
<button on:click={reset}>Reset</button>
```

**Methods:**
- `set(value)`: Set new value
- `update(fn)`: Update based on current value
- `subscribe(fn)`: Subscribe to changes

---

## Readable Store

Read-only store with custom logic:

```javascript
import { readable } from 'svelte/store'

export const time = readable(new Date(), (set) => {
  const interval = setInterval(() => {
    set(new Date())
  }, 1000)
  
  return () => clearInterval(interval)
})
```

**Usage:**
```svelte
<script>
  import { time } from './stores.js'
</script>

<p>Current time: {$time.toLocaleTimeString()}</p>
```

---

## Derived Store

Compute values from other stores:

```javascript
import { writable, derived } from 'svelte/store'

export const count = writable(0)
export const doubled = derived(count, $count => $count * 2)

// Multiple sources
export const sum = derived(
  [count, doubled],
  ([$count, $doubled]) => $count + $doubled
)

// Async derived
export const user = derived(
  userId,
  ($userId, set) => {
    fetch(`/api/users/${$userId}`)
      .then(r => r.json())
      .then(set)
    
    return () => {} // Cleanup
  },
  null // Initial value
)
```

---

## Custom Stores

Create stores with custom methods:

```javascript
import { writable } from 'svelte/store'

function createCounter() {
  const { subscribe, set, update } = writable(0)
  
  return {
    subscribe,
    increment: () => update(n => n + 1),
    decrement: () => update(n => n - 1),
    reset: () => set(0)
  }
}

export const counter = createCounter()
```

**Usage:**
```svelte
<script>
  import { counter } from './stores.js'
</script>

<button on:click={counter.increment}>+</button>
<button on:click={counter.decrement}>-</button>
<button on:click={counter.reset}>Reset</button>
<p>Count: {$counter}</p>
```

---

## Store Patterns

### Todo Store

```javascript
import { writable } from 'svelte/store'

function createTodoStore() {
  const { subscribe, update } = writable([])
  
  return {
    subscribe,
    add: (text) => update(todos => [
      ...todos,
      { id: Date.now(), text, completed: false }
    ]),
    toggle: (id) => update(todos =>
      todos.map(todo =>
        todo.id === id ? { ...todo, completed: !todo.completed } : todo
      )
    ),
    remove: (id) => update(todos =>
      todos.filter(todo => todo.id !== id)
    ),
    clear: () => update(() => [])
  }
}

export const todos = createTodoStore()
```

### Authentication Store

```javascript
import { writable, derived } from 'svelte/store'

function createAuthStore() {
  const { subscribe, set } = writable(null)
  
  return {
    subscribe,
    login: async (email, password) => {
      const response = await fetch('/api/login', {
        method: 'POST',
        body: JSON.stringify({ email, password })
      })
      const user = await response.json()
      set(user)
    },
    logout: () => {
      fetch('/api/logout', { method: 'POST' })
      set(null)
    },
    checkAuth: async () => {
      try {
        const response = await fetch('/api/me')
        const user = await response.json()
        set(user)
      } catch {
        set(null)
      }
    }
  }
}

export const auth = createAuthStore()
export const isLoggedIn = derived(auth, $auth => $auth !== null)
```

### Local Storage Store

```javascript
import { writable } from 'svelte/store'

function createLocalStore(key, initialValue) {
  const storedValue = localStorage.getItem(key)
  const store = writable(storedValue ? JSON.parse(storedValue) : initialValue)
  
  store.subscribe(value => {
    localStorage.setItem(key, JSON.stringify(value))
  })
  
  return store
}

export const preferences = createLocalStore('preferences', {
  theme: 'light',
  language: 'en'
})
```

---

## Context API

Share data within component tree without stores:

**Parent:**
```svelte
<script>
  import { setContext } from 'svelte'
  
  const user = { name: 'John', role: 'admin' }
  setContext('user', user)
</script>
```

**Child:**
```svelte
<script>
  import { getContext } from 'svelte'
  
  const user = getContext('user')
</script>

<p>User: {user.name}</p>
```

**With Reactivity:**
```svelte
<script>
  import { setContext } from 'svelte'
  import { writable } from 'svelte/store'
  
  const user = writable({ name: 'John' })
  setContext('user', user)
</script>

<!-- Child -->
<script>
  import { getContext } from 'svelte'
  
  const user = getContext('user')
</script>

<p>User: {$user.name}</p>
```

---

## Store Subscriptions

### Auto-Subscription with `$`

```svelte
<script>
  import { count } from './stores.js'
  
  // $ prefix auto-subscribes and unsubscribes
  $: doubled = $count * 2
</script>

<p>Count: {$count}</p>
<p>Doubled: {doubled}</p>
```

### Manual Subscription

```svelte
<script>
  import { onDestroy } from 'svelte'
  import { count } from './stores.js'
  
  let value
  
  const unsubscribe = count.subscribe(n => {
    value = n
    console.log('Count changed:', n)
  })
  
  onDestroy(unsubscribe)
</script>
```

---

## Advanced Patterns

### Store with Middleware

```javascript
import { writable } from 'svelte/store'

function createStoreWithMiddleware(initialValue, middleware) {
  const { subscribe, set, update } = writable(initialValue)
  
  return {
    subscribe,
    set: (value) => {
      const newValue = middleware(value)
      set(newValue)
    },
    update: (fn) => {
      update(current => {
        const newValue = fn(current)
        return middleware(newValue)
      })
    }
  }
}

// Logger middleware
const logger = (value) => {
  console.log('Store updated:', value)
  return value
}

export const count = createStoreWithMiddleware(0, logger)
```

### Async Store

```javascript
import { writable } from 'svelte/store'

function createAsyncStore(fetchFn) {
  const { subscribe, set } = writable({
    loading: false,
    data: null,
    error: null
  })
  
  return {
    subscribe,
    fetch: async (...args) => {
      set({ loading: true, data: null, error: null })
      
      try {
        const data = await fetchFn(...args)
        set({ loading: false, data, error: null })
      } catch (error) {
        set({ loading: false, data: null, error })
      }
    }
  }
}

export const users = createAsyncStore(async () => {
  const response = await fetch('/api/users')
  return response.json()
})
```

**Usage:**
```svelte
<script>
  import { onMount } from 'svelte'
  import { users } from './stores.js'
  
  onMount(() => users.fetch())
</script>

{#if $users.loading}
  <p>Loading...</p>
{:else if $users.error}
  <p>Error: {$users.error.message}</p>
{:else if $users.data}
  <ul>
    {#each $users.data as user}
      <li>{user.name}</li>
    {/each}
  </ul>
{/if}
```

---

## Store Composition

```javascript
import { writable, derived } from 'svelte/store'

// Base stores
export const firstName = writable('John')
export const lastName = writable('Doe')

// Composed store
export const fullName = derived(
  [firstName, lastName],
  ([$firstName, $lastName]) => `${$firstName} ${$lastName}`
)

// Writable derived (two-way binding)
export const fullNameWritable = {
  subscribe: fullName.subscribe,
  set: (value) => {
    const [first, last] = value.split(' ')
    firstName.set(first)
    lastName.set(last)
  }
}
```

---

## Performance Optimization

### Avoid Unnecessary Subscriptions

```svelte
<!-- ❌ Bad: Creates subscription on every render -->
<script>
  import { count } from './stores.js'
  
  function getCount() {
    let value
    count.subscribe(n => value = n)()
    return value
  }
</script>

<!-- ✅ Good: Use $ prefix -->
<script>
  import { count } from './stores.js'
</script>

<p>Count: {$count}</p>
```

### Selective Updates

```javascript
import { writable, derived } from 'svelte/store'

const user = writable({ name: 'John', age: 30, email: 'john@example.com' })

// Only update when name changes
export const userName = derived(
  user,
  $user => $user.name,
  '',
  (a, b) => a === b // Custom equality check
)
```

---

## Testing Stores

```javascript
import { get } from 'svelte/store'
import { counter } from './stores.js'

test('counter increments', () => {
  counter.reset()
  expect(get(counter)).toBe(0)
  
  counter.increment()
  expect(get(counter)).toBe(1)
  
  counter.decrement()
  expect(get(counter)).toBe(0)
})
```

---

## Best Practices

1. **Use stores for global state**: Component state for local, stores for shared
2. **Create custom stores**: Encapsulate logic and provide clean API
3. **Use derived stores**: Avoid redundant computations
4. **Leverage context API**: For component-tree-scoped state
5. **Auto-subscribe with `$`**: Simpler and prevents memory leaks
6. **Keep stores focused**: Single responsibility principle
7. **Test stores independently**: Easier to maintain and debug
