# Reactivity and Stores

Deep dive into Svelte's reactivity system and state management with stores.

---

## Advanced Reactivity

### Reactive Declarations Deep Dive

**Dependency Tracking**

Svelte automatically tracks dependencies in reactive declarations.

```svelte
<script>
  let a = 1;
  let b = 2;
  
  // Depends on both a and b
  $: sum = a + b;
  
  // Depends on sum (which depends on a and b)
  $: doubled = sum * 2;
  
  // Conditional dependency
  let useA = true;
  $: result = useA ? a : b;  // Depends on useA, a, and b
</script>
```

**Reactive Statement Patterns**

```svelte
<script>
  let items = [];
  let filter = '';
  
  // Reactive filtering
  $: filteredItems = items.filter(item => 
    item.name.toLowerCase().includes(filter.toLowerCase())
  );
  
  // Reactive sorting
  let sortBy = 'name';
  $: sortedItems = [...filteredItems].sort((a, b) => 
    a[sortBy] > b[sortBy] ? 1 : -1
  );
  
  // Side effect when data changes
  $: if (sortedItems.length === 0) {
    console.log('No items match filter');
  }
  
  // Multiple statements in reactive block
  $: {
    console.log('Items changed:', items.length);
    localStorage.setItem('items', JSON.stringify(items));
  }
</script>
```

**Reactive Functions**

```svelte
<script>
  let numbers = [1, 2, 3, 4, 5];
  
  // Reactive computation
  $: statistics = (() => {
    const sum = numbers.reduce((a, b) => a + b, 0);
    const average = sum / numbers.length;
    const max = Math.max(...numbers);
    const min = Math.min(...numbers);
    return { sum, average, max, min };
  })();
  
  // Reactive async operation
  $: dataPromise = (async () => {
    const response = await fetch(`/api/data?count=${numbers.length}`);
    return response.json();
  })();
</script>

<p>Sum: {statistics.sum}</p>
<p>Average: {statistics.average}</p>

{#await dataPromise then data}
  <p>Data: {JSON.stringify(data)}</p>
{/await}
```

### Reactive Gotchas

**Array and Object Mutations**

```svelte
<script>
  let items = [1, 2, 3];
  let user = { name: 'Alice', age: 30 };
  
  // ❌ These don't trigger reactivity
  function badAddItem() {
    items.push(4);  // Mutation, no assignment
  }
  
  function badUpdateUser() {
    user.name = 'Bob';  // Mutation, no assignment
  }
  
  // ✅ These trigger reactivity
  function goodAddItem() {
    items = [...items, 4];  // Reassignment
  }
  
  function goodUpdateUser() {
    user = { ...user, name: 'Bob' };  // Reassignment
  }
  
  // ✅ Alternative: mutate then reassign
  function alternativeAddItem() {
    items.push(4);
    items = items;  // Force reactivity
  }
</script>
```

**Indirect Dependencies**

```svelte
<script>
  let count = 0;
  
  function getCount() {
    return count;
  }
  
  // ❌ Won't react to count changes (indirect dependency)
  $: value = getCount();
  
  // ✅ Direct dependency
  $: value = count;
  
  // ✅ Or inline the function
  $: value = (() => count)();
</script>
```

---

## Stores

### Writable Stores

**Creating Writable Stores**

```javascript
// stores.js
import { writable } from 'svelte/store';

// Basic writable store
export const count = writable(0);

// Store with initial value
export const user = writable({
  name: 'Guest',
  loggedIn: false
});

// Store with custom logic
export const theme = writable('light', (set) => {
  // Called when first subscriber subscribes
  const savedTheme = localStorage.getItem('theme');
  if (savedTheme) {
    set(savedTheme);
  }
  
  // Return cleanup function (called when last subscriber unsubscribes)
  return () => {
    console.log('No more subscribers');
  };
});
```

**Using Writable Stores**

```svelte
<script>
  import { count, user } from './stores.js';
  
  // Auto-subscription with $ prefix
  // Automatically subscribes on mount, unsubscribes on destroy
  
  function increment() {
    count.update(n => n + 1);
  }
  
  function reset() {
    count.set(0);
  }
  
  function login() {
    user.set({
      name: 'Alice',
      loggedIn: true
    });
  }
  
  function updateName(newName) {
    user.update(u => ({ ...u, name: newName }));
  }
</script>

<p>Count: {$count}</p>
<button on:click={increment}>+1</button>
<button on:click={reset}>Reset</button>

<p>User: {$user.name} ({$user.loggedIn ? 'Logged in' : 'Guest'})</p>
<button on:click={login}>Login</button>
```

**Manual Subscription**

```svelte
<script>
  import { onDestroy } from 'svelte';
  import { count } from './stores.js';
  
  let countValue;
  
  // Manual subscription
  const unsubscribe = count.subscribe(value => {
    countValue = value;
  });
  
  // Clean up subscription
  onDestroy(unsubscribe);
</script>

<p>Count: {countValue}</p>
```

### Readable Stores

**Creating Readable Stores**

```javascript
import { readable } from 'svelte/store';

// Time store that updates every second
export const time = readable(new Date(), (set) => {
  const interval = setInterval(() => {
    set(new Date());
  }, 1000);
  
  return () => clearInterval(interval);
});

// Mouse position store
export const mousePosition = readable({ x: 0, y: 0 }, (set) => {
  function handleMouseMove(event) {
    set({ x: event.clientX, y: event.clientY });
  }
  
  window.addEventListener('mousemove', handleMouseMove);
  
  return () => {
    window.removeEventListener('mousemove', handleMouseMove);
  };
});

// Online status store
export const online = readable(navigator.onLine, (set) => {
  function handleOnline() {
    set(true);
  }
  
  function handleOffline() {
    set(false);
  }
  
  window.addEventListener('online', handleOnline);
  window.addEventListener('offline', handleOffline);
  
  return () => {
    window.removeEventListener('online', handleOnline);
    window.removeEventListener('offline', handleOffline);
  };
});
```

**Using Readable Stores**

```svelte
<script>
  import { time, mousePosition, online } from './stores.js';
</script>

<p>Current time: {$time.toLocaleTimeString()}</p>
<p>Mouse position: {$mousePosition.x}, {$mousePosition.y}</p>
<p>Status: {$online ? 'Online' : 'Offline'}</p>
```

### Derived Stores

**Creating Derived Stores**

```javascript
import { writable, derived } from 'svelte/store';

// Source stores
export const firstName = writable('John');
export const lastName = writable('Doe');
export const age = writable(30);

// Derived from single store
export const doubled = derived(age, $age => $age * 2);

// Derived from multiple stores
export const fullName = derived(
  [firstName, lastName],
  ([$firstName, $lastName]) => `${$firstName} ${$lastName}`
);

// Derived with async operation
export const userData = derived(
  fullName,
  ($fullName, set) => {
    fetch(`/api/users?name=${$fullName}`)
      .then(res => res.json())
      .then(data => set(data));
    
    // Optional: return cleanup function
    return () => {
      // Cancel fetch if needed
    };
  },
  {} // Initial value
);

// Complex derivation
export const statistics = derived(
  [firstName, lastName, age],
  ([$firstName, $lastName, $age]) => ({
    fullName: `${$firstName} ${$lastName}`,
    initials: `${$firstName[0]}${$lastName[0]}`,
    isAdult: $age >= 18,
    category: $age < 18 ? 'minor' : $age < 65 ? 'adult' : 'senior'
  })
);
```

**Using Derived Stores**

```svelte
<script>
  import { firstName, lastName, fullName, statistics } from './stores.js';
</script>

<input bind:value={$firstName} placeholder="First name" />
<input bind:value={$lastName} placeholder="Last name" />

<p>Full name: {$fullName}</p>
<p>Initials: {$statistics.initials}</p>
<p>Category: {$statistics.category}</p>
```

### Custom Stores

**Store Contract**

A store must implement the store contract:
- `subscribe(callback)` method that returns an `unsubscribe` function
- Optionally: `set(value)` and `update(fn)` methods

**Custom Store Examples**

```javascript
import { writable } from 'svelte/store';

// Counter store with custom methods
function createCounter() {
  const { subscribe, set, update } = writable(0);
  
  return {
    subscribe,
    increment: () => update(n => n + 1),
    decrement: () => update(n => n - 1),
    reset: () => set(0)
  };
}

export const counter = createCounter();

// Todo store
function createTodoStore() {
  const { subscribe, update } = writable([]);
  
  return {
    subscribe,
    add: (text) => update(todos => [...todos, { id: Date.now(), text, done: false }]),
    remove: (id) => update(todos => todos.filter(t => t.id !== id)),
    toggle: (id) => update(todos => todos.map(t => 
      t.id === id ? { ...t, done: !t.done } : t
    )),
    clear: () => update(todos => todos.filter(t => !t.done))
  };
}

export const todos = createTodoStore();

// Local storage store
function createLocalStore(key, initialValue) {
  const stored = localStorage.getItem(key);
  const { subscribe, set, update } = writable(stored ? JSON.parse(stored) : initialValue);
  
  return {
    subscribe,
    set: (value) => {
      localStorage.setItem(key, JSON.stringify(value));
      set(value);
    },
    update: (fn) => {
      update(value => {
        const newValue = fn(value);
        localStorage.setItem(key, JSON.stringify(newValue));
        return newValue;
      });
    }
  };
}

export const settings = createLocalStore('settings', {
  theme: 'light',
  language: 'en'
});
```

**Using Custom Stores**

```svelte
<script>
  import { counter, todos, settings } from './stores.js';
</script>

<!-- Counter -->
<p>Count: {$counter}</p>
<button on:click={counter.increment}>+</button>
<button on:click={counter.decrement}>-</button>
<button on:click={counter.reset}>Reset</button>

<!-- Todos -->
<input on:keydown={(e) => {
  if (e.key === 'Enter') {
    todos.add(e.target.value);
    e.target.value = '';
  }
}} />

{#each $todos as todo}
  <div>
    <input type="checkbox" checked={todo.done} on:change={() => todos.toggle(todo.id)} />
    <span>{todo.text}</span>
    <button on:click={() => todos.remove(todo.id)}>Delete</button>
  </div>
{/each}

<button on:click={todos.clear}>Clear completed</button>

<!-- Settings -->
<select bind:value={$settings.theme}>
  <option value="light">Light</option>
  <option value="dark">Dark</option>
</select>
```

### Store Best Practices

**When to Use Stores**

✅ **Use stores for:**
- Global application state
- Shared state between unrelated components
- State that persists across route changes
- Complex state logic
- State that needs to be accessed outside components

❌ **Don't use stores for:**
- Local component state
- Props that can be passed down
- Temporary UI state
- Form state (unless shared)

**Store Organization**

```javascript
// stores/auth.js
import { writable, derived } from 'svelte/store';

const user = writable(null);
const token = writable(null);

export const auth = {
  user: { subscribe: user.subscribe },
  token: { subscribe: token.subscribe },
  isAuthenticated: derived([user, token], ([$user, $token]) => !!$user && !!$token),
  
  login: async (credentials) => {
    const response = await fetch('/api/login', {
      method: 'POST',
      body: JSON.stringify(credentials)
    });
    const data = await response.json();
    user.set(data.user);
    token.set(data.token);
  },
  
  logout: () => {
    user.set(null);
    token.set(null);
  }
};
```

**Store Composition**

```javascript
import { writable, derived } from 'svelte/store';

// Base stores
const items = writable([]);
const filter = writable('');
const sortBy = writable('name');

// Composed derived store
export const displayItems = derived(
  [items, filter, sortBy],
  ([$items, $filter, $sortBy]) => {
    let result = $items;
    
    // Filter
    if ($filter) {
      result = result.filter(item => 
        item.name.toLowerCase().includes($filter.toLowerCase())
      );
    }
    
    // Sort
    result = [...result].sort((a, b) => 
      a[$sortBy] > b[$sortBy] ? 1 : -1
    );
    
    return result;
  }
);

export const itemStore = {
  subscribe: displayItems.subscribe,
  setItems: items.set,
  setFilter: filter.set,
  setSortBy: sortBy.set
};
```

---

## Context API

### Using Context for Component Trees

**Setting Context**

```svelte
<!-- Parent.svelte -->
<script>
  import { setContext } from 'svelte';
  import { writable } from 'svelte/store';
  
  // Set context with a key
  setContext('theme', {
    current: 'light',
    toggle: () => {
      // Toggle logic
    }
  });
  
  // Context can be a store
  const user = writable({ name: 'Alice' });
  setContext('user', user);
</script>

<slot />
```

**Getting Context**

```svelte
<!-- Child.svelte (any depth) -->
<script>
  import { getContext } from 'svelte';
  
  const theme = getContext('theme');
  const user = getContext('user');
</script>

<p>Theme: {theme.current}</p>
<p>User: {$user.name}</p>
<button on:click={theme.toggle}>Toggle theme</button>
```

**Context Best Practices**

```javascript
// contexts/theme.js
import { writable } from 'svelte/store';
import { setContext, getContext } from 'svelte';

const THEME_KEY = Symbol('theme');

export function setThemeContext() {
  const theme = writable('light');
  
  const context = {
    subscribe: theme.subscribe,
    toggle: () => theme.update(t => t === 'light' ? 'dark' : 'light'),
    set: theme.set
  };
  
  setContext(THEME_KEY, context);
  return context;
}

export function getThemeContext() {
  return getContext(THEME_KEY);
}
```

**Usage**

```svelte
<!-- App.svelte -->
<script>
  import { setThemeContext } from './contexts/theme.js';
  setThemeContext();
</script>

<slot />

<!-- Child.svelte -->
<script>
  import { getThemeContext } from './contexts/theme.js';
  const theme = getThemeContext();
</script>

<button on:click={theme.toggle}>
  Current theme: {$theme}
</button>
```

---

## Advanced Patterns

### Store Middleware

```javascript
import { writable } from 'svelte/store';

function createMiddlewareStore(initialValue, middleware = []) {
  const { subscribe, set, update } = writable(initialValue);
  
  const enhancedSet = (value) => {
    let processedValue = value;
    for (const fn of middleware) {
      processedValue = fn(processedValue);
    }
    set(processedValue);
  };
  
  const enhancedUpdate = (fn) => {
    update(value => {
      let newValue = fn(value);
      for (const middleware of middleware) {
        newValue = middleware(newValue);
      }
      return newValue;
    });
  };
  
  return {
    subscribe,
    set: enhancedSet,
    update: enhancedUpdate
  };
}

// Usage
const logger = (value) => {
  console.log('Store updated:', value);
  return value;
};

const validator = (value) => {
  if (value < 0) throw new Error('Value must be positive');
  return value;
};

export const count = createMiddlewareStore(0, [validator, logger]);
```

### Async Stores

```javascript
import { writable, derived } from 'svelte/store';

function createAsyncStore(fetchFn) {
  const loading = writable(false);
  const error = writable(null);
  const data = writable(null);
  
  async function load(...args) {
    loading.set(true);
    error.set(null);
    
    try {
      const result = await fetchFn(...args);
      data.set(result);
    } catch (e) {
      error.set(e.message);
    } finally {
      loading.set(false);
    }
  }
  
  return {
    subscribe: derived([data, loading, error], ([$data, $loading, $error]) => ({
      data: $data,
      loading: $loading,
      error: $error
    })).subscribe,
    load
  };
}

// Usage
export const users = createAsyncStore(async () => {
  const response = await fetch('/api/users');
  return response.json();
});
```

```svelte
<script>
  import { onMount } from 'svelte';
  import { users } from './stores.js';
  
  onMount(() => {
    users.load();
  });
</script>

{#if $users.loading}
  <p>Loading...</p>
{:else if $users.error}
  <p>Error: {$users.error}</p>
{:else if $users.data}
  {#each $users.data as user}
    <p>{user.name}</p>
  {/each}
{/if}
```
