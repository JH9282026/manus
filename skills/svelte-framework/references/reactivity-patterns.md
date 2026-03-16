# Reactivity Patterns

Advanced reactivity patterns and best practices in Svelte.

---

## Understanding Svelte Reactivity

Svelte's reactivity is based on **assignments**. The compiler tracks which variables are used in the template and generates code to update the DOM when those variables change.

**Key Principle:** Reactivity is triggered by assignment (`=`), not mutation.

---

## Basic Reactivity

### Simple Variables

```svelte
<script>
  let count = 0
  
  function increment() {
    count += 1 // Assignment triggers reactivity
  }
</script>

<button on:click={increment}>
  Count: {count}
</button>
```

### Reactive Declarations

```svelte
<script>
  let count = 0
  
  // Computed value
  $: doubled = count * 2
  
  // Side effect
  $: console.log('Count is', count)
  
  // Conditional side effect
  $: if (count > 10) {
    console.log('Count is high!')
  }
</script>
```

---

## Arrays and Objects

### Problem: Mutations Don't Trigger Reactivity

```svelte
<script>
  let items = [1, 2, 3]
  
  function addItem() {
    items.push(4) // ❌ Won't trigger update
  }
</script>
```

### Solution: Reassignment

```svelte
<script>
  let items = [1, 2, 3]
  
  function addItem() {
    items = [...items, 4] // ✅ Triggers update
  }
  
  function removeItem(index) {
    items = items.filter((_, i) => i !== index)
  }
  
  function updateItem(index, value) {
    items = items.map((item, i) => i === index ? value : item)
  }
</script>
```

### Object Updates

```svelte
<script>
  let user = { name: 'John', age: 30 }
  
  function updateName(newName) {
    user.name = newName // ❌ Won't trigger update
  }
  
  function updateNameCorrectly(newName) {
    user = { ...user, name: newName } // ✅ Triggers update
  }
</script>
```

### Alternative: Self-Assignment

```svelte
<script>
  let items = [1, 2, 3]
  
  function addItem() {
    items.push(4)
    items = items // ✅ Triggers update
  }
</script>
```

---

## Svelte 5 Runes

### `$state`

Declare reactive state:

```svelte
<script>
  let count = $state(0)
  let user = $state({ name: 'John', age: 30 })
  let items = $state([1, 2, 3])
</script>
```

**Benefits:**
- Explicit reactivity
- Works with mutations (no reassignment needed)
- Better TypeScript support

**With Mutations:**
```svelte
<script>
  let items = $state([1, 2, 3])
  
  function addItem() {
    items.push(4) // ✅ Works with $state
  }
</script>
```

### `$derived`

Computed values:

```svelte
<script>
  let count = $state(0)
  let doubled = $derived(count * 2)
  let tripled = $derived(count * 3)
  
  // Chained derivations
  let sum = $derived(doubled + tripled)
</script>
```

### `$effect`

Side effects:

```svelte
<script>
  let count = $state(0)
  
  $effect(() => {
    console.log('Count changed:', count)
    document.title = `Count: ${count}`
  })
  
  // Cleanup
  $effect(() => {
    const interval = setInterval(() => {
      count++
    }, 1000)
    
    return () => clearInterval(interval)
  })
</script>
```

### `$props`

Component props:

```svelte
<script>
  let { title, count = 0, onUpdate } = $props()
  
  function handleClick() {
    onUpdate?.(count + 1)
  }
</script>

<h1>{title}</h1>
<button on:click={handleClick}>{count}</button>
```

### `$bindable`

Two-way binding:

```svelte
<!-- Child.svelte -->
<script>
  let { value = $bindable() } = $props()
</script>

<input bind:value />

<!-- Parent.svelte -->
<script>
  let text = $state('')
</script>

<Child bind:value={text} />
<p>Text: {text}</p>
```

---

## Reactive Statements Order

Reactive statements run in the order they appear:

```svelte
<script>
  let count = 0
  
  $: doubled = count * 2
  $: quadrupled = doubled * 2 // Depends on doubled
  
  // ❌ Wrong order
  $: result = intermediate * 2
  $: intermediate = count * 2 // Defined after use
</script>
```

**Best Practice:** Define dependencies before use.

---

## Reactive Context

### Component-Level Reactivity

```svelte
<script context="module">
  // Runs once when module loads
  let globalCount = 0
</script>

<script>
  // Runs for each component instance
  let instanceCount = 0
</script>
```

---

## Advanced Patterns

### Debounced Reactivity

```svelte
<script>
  import { writable } from 'svelte/store'
  
  let searchQuery = ''
  let debouncedQuery = ''
  let timeout
  
  $: {
    clearTimeout(timeout)
    timeout = setTimeout(() => {
      debouncedQuery = searchQuery
    }, 300)
  }
  
  $: if (debouncedQuery) {
    performSearch(debouncedQuery)
  }
</script>

<input bind:value={searchQuery} />
```

### Reactive Classes

```svelte
<script>
  let isActive = false
  let count = 0
</script>

<div class:active={isActive} class:high={count > 10}>
  Content
</div>

<!-- Shorthand when variable name matches class name -->
<div class:active>
  Content
</div>
```

### Reactive Styles

```svelte
<script>
  let color = 'red'
  let size = 20
</script>

<p style:color style:font-size="{size}px">
  Styled text
</p>
```

---

## Reactivity with Stores

### Auto-Subscription

```svelte
<script>
  import { writable } from 'svelte/store'
  
  const count = writable(0)
  
  // $ prefix auto-subscribes and unsubscribes
  $: doubled = $count * 2
</script>

<button on:click={() => $count++}>
  Count: {$count}
</button>
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
  })
  
  onDestroy(unsubscribe)
</script>
```

---

## Reactive Bindings

### Input Bindings

```svelte
<script>
  let text = ''
  let checked = false
  let selected = ''
  let files
</script>

<input bind:value={text} />
<input type="checkbox" bind:checked />
<select bind:value={selected}>
  <option value="a">A</option>
  <option value="b">B</option>
</select>
<input type="file" bind:files />
```

### Component Bindings

```svelte
<!-- Parent.svelte -->
<script>
  import Child from './Child.svelte'
  let childValue = ''
</script>

<Child bind:value={childValue} />
<p>Child value: {childValue}</p>

<!-- Child.svelte -->
<script>
  export let value = ''
</script>

<input bind:value />
```

### Element Bindings

```svelte
<script>
  let element
  let width
  let height
  
  $: if (element) {
    console.log('Element:', element)
  }
</script>

<div bind:this={element} bind:clientWidth={width} bind:clientHeight={height}>
  Size: {width} x {height}
</div>
```

---

## Reactivity Debugging

### Inspect Reactive Updates

```svelte
<script>
  let count = 0
  
  $: console.log('Count updated:', count)
  $: console.trace('Count trace:', count)
</script>
```

### `$inspect` Rune (Svelte 5)

```svelte
<script>
  let count = $state(0)
  
  $inspect(count) // Logs to console when count changes
  $inspect(count).with(console.trace) // Custom logger
</script>
```

---

## Common Pitfalls

### 1. Forgetting Reassignment

```svelte
<!-- ❌ Wrong -->
<script>
  let items = []
  items.push(1) // No update
</script>

<!-- ✅ Correct -->
<script>
  let items = []
  items = [...items, 1]
</script>
```

### 2. Reactive Statement Dependencies

```svelte
<!-- ❌ Wrong: Doesn't track obj.count -->
<script>
  let obj = { count: 0 }
  $: doubled = obj.count * 2 // Won't update when obj.count changes
</script>

<!-- ✅ Correct -->
<script>
  let count = 0
  $: doubled = count * 2
</script>
```

### 3. Async Reactive Statements

```svelte
<!-- ❌ Wrong: Async not supported -->
<script>
  let data
  $: data = await fetch('/api/data')
</script>

<!-- ✅ Correct -->
<script>
  let data
  $: fetch('/api/data').then(r => r.json()).then(d => data = d)
  
  // Or use onMount
  import { onMount } from 'svelte'
  onMount(async () => {
    data = await fetch('/api/data').then(r => r.json())
  })
</script>
```

---

## Migration: Svelte 4 to Svelte 5

### Before (Svelte 4)

```svelte
<script>
  let count = 0
  $: doubled = count * 2
  
  $: {
    console.log('Count:', count)
  }
</script>
```

### After (Svelte 5)

```svelte
<script>
  let count = $state(0)
  let doubled = $derived(count * 2)
  
  $effect(() => {
    console.log('Count:', count)
  })
</script>
```

**Benefits:**
- More explicit
- Better TypeScript support
- Clearer intent
- Works with mutations
