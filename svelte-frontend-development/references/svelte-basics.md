# Svelte Basics

Foundational concepts, setup, and core features of the Svelte framework.

---

## What Makes Svelte Different

### Compiler vs. Runtime Framework

**Traditional Frameworks (React, Vue, Angular)**
- Ship framework code to browser
- Virtual DOM diffing at runtime
- Framework overhead in bundle
- Runtime performance cost

**Svelte Approach**
- Compiles components to vanilla JavaScript at build time
- No virtual DOM (direct DOM manipulation)
- No framework runtime in bundle
- Smaller bundles, faster performance

**Bundle Size Comparison**
- React + ReactDOM: ~40KB (minified + gzipped)
- Vue: ~23KB (minified + gzipped)
- Svelte: ~2KB (minified + gzipped) + component code

### Compilation Process

**Build-Time Transformation**

```svelte
<!-- Source: Counter.svelte -->
<script>
  let count = 0;
</script>

<button on:click={() => count += 1}>
  Count: {count}
</button>
```

Compiles to optimized JavaScript that:
- Creates DOM elements
- Sets up event listeners
- Updates only changed parts when count changes
- No framework runtime needed

---

## Project Setup

### Creating a New Project

**Vite + Svelte (SPA)**
```bash
npm create vite@latest my-app -- --template svelte
cd my-app
npm install
npm run dev
```

**Vite + Svelte + TypeScript**
```bash
npm create vite@latest my-app -- --template svelte-ts
cd my-app
npm install
npm run dev
```

**SvelteKit (Full-stack)**
```bash
npm create svelte@latest my-app
cd my-app
npm install
npm run dev
```

### Project Structure (Vite + Svelte)

```
my-app/
├── public/              # Static assets
├── src/
│   ├── lib/            # Reusable components
│   ├── App.svelte      # Root component
│   └── main.js         # Entry point
├── index.html          # HTML template
├── vite.config.js      # Vite configuration
└── package.json
```

### Configuration

**vite.config.js**
```javascript
import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'

export default defineConfig({
  plugins: [svelte()],
  server: {
    port: 3000
  },
  build: {
    target: 'esnext'
  }
})
```

**svelte.config.js**
```javascript
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte'

export default {
  preprocess: vitePreprocess(),
  compilerOptions: {
    // Enable runtime checks in development
    dev: process.env.NODE_ENV !== 'production'
  }
}
```

---

## Component Fundamentals

### Component Structure

**Three Sections**

```svelte
<script>
  // 1. JavaScript logic (runs once when component is created)
  import ChildComponent from './ChildComponent.svelte';
  
  let name = 'World';
  let count = 0;
  
  function handleClick() {
    count += 1;
  }
</script>

<style>
  /* 2. Scoped CSS (only applies to this component) */
  h1 {
    color: blue;
  }
  
  .highlight {
    background: yellow;
  }
</style>

<!-- 3. HTML template -->
<h1 class="highlight">Hello {name}!</h1>
<button on:click={handleClick}>
  Clicked {count} {count === 1 ? 'time' : 'times'}
</button>

<ChildComponent />
```

**Section Details**

1. **`<script>` section**
   - Runs once when component instance is created
   - Define component state (variables)
   - Import dependencies
   - Define functions
   - Export props

2. **`<style>` section**
   - Automatically scoped to component
   - No CSS-in-JS runtime overhead
   - Compiled to efficient CSS
   - Use `:global()` for global styles

3. **Template section**
   - HTML with Svelte syntax
   - Curly braces `{}` for expressions
   - Directives for logic and bindings
   - No wrapper element required

### Module Context

**`<script context="module">`**

```svelte
<script context="module">
  // Runs once when module first loads (shared across all instances)
  let totalInstances = 0;
  
  export function getInstanceCount() {
    return totalInstances;
  }
</script>

<script>
  // Runs for each component instance
  import { onMount } from 'svelte';
  
  onMount(() => {
    totalInstances += 1;
    return () => totalInstances -= 1;
  });
</script>

<p>Total instances: {totalInstances}</p>
```

**Use Cases**
- Shared state across component instances
- Export utilities from component file
- Preload data (in SvelteKit)

---

## Reactivity System

### Reactive Assignments

**How Reactivity Works**

Svelte's reactivity is triggered by **assignments**. The compiler instruments assignments to know when state changes.

```svelte
<script>
  let count = 0;
  
  function increment() {
    count += 1;  // Assignment triggers reactivity
  }
  
  function reset() {
    count = 0;   // Assignment triggers reactivity
  }
</script>

<button on:click={increment}>Count: {count}</button>
<button on:click={reset}>Reset</button>
```

**Arrays and Objects**

Mutations don't trigger reactivity; reassignments do.

```svelte
<script>
  let items = [1, 2, 3];
  
  function addItem() {
    // ❌ Won't trigger reactivity
    items.push(4);
    
    // ✅ Triggers reactivity
    items = [...items, 4];
    // or
    items = items.concat(4);
  }
  
  function removeFirst() {
    // ❌ Won't trigger reactivity
    items.shift();
    
    // ✅ Triggers reactivity
    items = items.slice(1);
  }
  
  function updateFirst() {
    // ❌ Won't trigger reactivity
    items[0] = 99;
    
    // ✅ Triggers reactivity
    items[0] = 99;
    items = items;  // Force reactivity
    // or
    items = [99, ...items.slice(1)];
  }
</script>
```

**Object Updates**

```svelte
<script>
  let user = {
    name: 'Alice',
    age: 30
  };
  
  function updateName() {
    // ❌ Won't trigger reactivity
    user.name = 'Bob';
    
    // ✅ Triggers reactivity
    user = { ...user, name: 'Bob' };
  }
  
  function incrementAge() {
    // ✅ Triggers reactivity (property assignment on top-level variable)
    user.age += 1;
    user = user;
  }
</script>
```

### Reactive Declarations

**`$:` Label Syntax**

The `$:` label marks a statement as reactive. It re-runs whenever its dependencies change.

```svelte
<script>
  let count = 0;
  
  // Reactive declaration - recalculates when count changes
  $: doubled = count * 2;
  
  // Reactive statement - runs when count changes
  $: console.log('Count is:', count);
  
  // Reactive block - multiple statements
  $: {
    console.log('Count changed to:', count);
    if (count > 10) {
      console.log('Count is high!');
    }
  }
  
  // Multiple dependencies
  let width = 10;
  let height = 20;
  $: area = width * height;
  
  // Reactive chain
  $: perimeter = 2 * (width + height);
  $: description = `Area: ${area}, Perimeter: ${perimeter}`;
</script>

<p>Count: {count}</p>
<p>Doubled: {doubled}</p>
<p>{description}</p>
```

**Reactive Statement Order**

Reactive statements run in topological order based on dependencies, not source order.

```svelte
<script>
  let a = 1;
  
  // These run in dependency order, not source order
  $: c = b * 2;  // Runs second (depends on b)
  $: b = a * 2;  // Runs first (depends on a)
  
  // a = 1 → b = 2 → c = 4
</script>
```

**Reactive Functions**

```svelte
<script>
  let items = [1, 2, 3, 4, 5];
  let threshold = 3;
  
  // Reactive function call
  $: filtered = items.filter(item => item > threshold);
  
  // Reactive with complex logic
  $: summary = (() => {
    const total = items.reduce((sum, item) => sum + item, 0);
    const average = total / items.length;
    return { total, average };
  })();
</script>

<p>Filtered: {filtered.join(', ')}</p>
<p>Total: {summary.total}, Average: {summary.average}</p>
```

---

## Template Syntax

### Expressions

**Interpolation**

```svelte
<script>
  let name = 'Alice';
  let age = 30;
  let user = { name: 'Bob', email: 'bob@example.com' };
</script>

<!-- Simple expression -->
<p>Hello {name}!</p>

<!-- Arithmetic -->
<p>Next year you'll be {age + 1}</p>

<!-- Object property -->
<p>{user.name} - {user.email}</p>

<!-- Function call -->
<p>{name.toUpperCase()}</p>

<!-- Ternary -->
<p>You are {age >= 18 ? 'an adult' : 'a minor'}</p>
```

**HTML Rendering**

```svelte
<script>
  let htmlString = '<strong>Bold text</strong>';
</script>

<!-- Escaped (safe) -->
<p>{htmlString}</p>  <!-- Displays: <strong>Bold text</strong> -->

<!-- Unescaped (dangerous - only use with trusted content) -->
<p>{@html htmlString}</p>  <!-- Displays: Bold text -->
```

### Logic Blocks

**if/else**

```svelte
<script>
  let user = null;
  let loading = false;
</script>

{#if user}
  <p>Welcome, {user.name}!</p>
{:else if loading}
  <p>Loading...</p>
{:else}
  <p>Please log in.</p>
{/if}
```

**each**

```svelte
<script>
  let items = [
    { id: 1, name: 'Apple', price: 1.99 },
    { id: 2, name: 'Banana', price: 0.99 },
    { id: 3, name: 'Cherry', price: 2.99 }
  ];
</script>

<!-- Basic each -->
{#each items as item}
  <p>{item.name}: ${item.price}</p>
{/each}

<!-- With index -->
{#each items as item, i}
  <p>{i + 1}. {item.name}: ${item.price}</p>
{/each}

<!-- With key (important for efficient updates) -->
{#each items as item (item.id)}
  <p>{item.name}: ${item.price}</p>
{/each}

<!-- Destructuring -->
{#each items as { id, name, price }}
  <p>{name}: ${price}</p>
{/each}

<!-- With else (empty state) -->
{#each items as item}
  <p>{item.name}</p>
{:else}
  <p>No items found</p>
{/each}
```

**await**

```svelte
<script>
  async function fetchUser(id) {
    const response = await fetch(`/api/users/${id}`);
    return response.json();
  }
  
  let userPromise = fetchUser(1);
</script>

{#await userPromise}
  <p>Loading user...</p>
{:then user}
  <p>Welcome, {user.name}!</p>
{:catch error}
  <p>Error: {error.message}</p>
{/await}

<!-- Short form (no loading state) -->
{#await userPromise then user}
  <p>Welcome, {user.name}!</p>
{/await}
```

**key**

Force component recreation when value changes.

```svelte
<script>
  let userId = 1;
</script>

<!-- Component recreated when userId changes -->
{#key userId}
  <UserProfile id={userId} />
{/key}
```

---

## Event Handling

### Event Directives

**Basic Events**

```svelte
<script>
  function handleClick() {
    console.log('Clicked!');
  }
  
  function handleInput(event) {
    console.log('Input value:', event.target.value);
  }
  
  function handleSubmit(event) {
    event.preventDefault();
    console.log('Form submitted');
  }
</script>

<!-- Click event -->
<button on:click={handleClick}>Click me</button>

<!-- Inline handler -->
<button on:click={() => console.log('Clicked!')}>Click me</button>

<!-- Input event -->
<input on:input={handleInput} />

<!-- Form submit -->
<form on:submit={handleSubmit}>
  <button type="submit">Submit</button>
</form>
```

**Event Modifiers**

```svelte
<!-- preventDefault -->
<form on:submit|preventDefault={handleSubmit}>
  <button type="submit">Submit</button>
</form>

<!-- stopPropagation -->
<div on:click={() => console.log('Outer')}>
  <button on:click|stopPropagation={() => console.log('Inner')}>
    Click me
  </button>
</div>

<!-- Multiple modifiers -->
<a href="/" on:click|preventDefault|stopPropagation={handleClick}>
  Link
</a>

<!-- once - remove handler after first run -->
<button on:click|once={handleClick}>Click once</button>

<!-- passive - improves scrolling performance -->
<div on:scroll|passive={handleScroll}>Scrollable content</div>

<!-- capture - fire in capture phase -->
<div on:click|capture={handleClick}>Content</div>

<!-- self - only trigger if event.target is element itself -->
<div on:click|self={handleClick}>
  <button>Won't trigger parent handler</button>
</div>
```

**Component Events**

```svelte
<!-- Forward DOM event -->
<button on:click>
  Click me
</button>

<!-- Parent can listen -->
<ChildComponent on:click={handleClick} />
```

### Custom Events

**Dispatching Events**

```svelte
<!-- Child.svelte -->
<script>
  import { createEventDispatcher } from 'svelte';
  
  const dispatch = createEventDispatcher();
  
  function handleClick() {
    dispatch('message', {
      text: 'Hello from child',
      timestamp: Date.now()
    });
  }
</script>

<button on:click={handleClick}>Send Message</button>

<!-- Parent.svelte -->
<script>
  import Child from './Child.svelte';
  
  function handleMessage(event) {
    console.log('Received:', event.detail.text);
    console.log('At:', event.detail.timestamp);
  }
</script>

<Child on:message={handleMessage} />
```

---

## Bindings

### Input Bindings

**Text Input**

```svelte
<script>
  let name = '';
  let message = '';
</script>

<input bind:value={name} placeholder="Name" />
<textarea bind:value={message} placeholder="Message"></textarea>

<p>Name: {name}</p>
<p>Message: {message}</p>
```

**Numeric Input**

```svelte
<script>
  let age = 0;
  let price = 0;
</script>

<!-- bind:value automatically converts to number for type="number" -->
<input type="number" bind:value={age} />
<input type="range" bind:value={price} min="0" max="100" />

<p>Age: {age} (type: {typeof age})</p>
<p>Price: ${price}</p>
```

**Checkbox**

```svelte
<script>
  let agreed = false;
  let flavors = [];
</script>

<!-- Single checkbox -->
<label>
  <input type="checkbox" bind:checked={agreed} />
  I agree to the terms
</label>

<!-- Multiple checkboxes (array) -->
<label>
  <input type="checkbox" bind:group={flavors} value="vanilla" />
  Vanilla
</label>
<label>
  <input type="checkbox" bind:group={flavors} value="chocolate" />
  Chocolate
</label>
<label>
  <input type="checkbox" bind:group={flavors} value="strawberry" />
  Strawberry
</label>

<p>Selected: {flavors.join(', ')}</p>
```

**Radio Buttons**

```svelte
<script>
  let size = 'medium';
</script>

<label>
  <input type="radio" bind:group={size} value="small" />
  Small
</label>
<label>
  <input type="radio" bind:group={size} value="medium" />
  Medium
</label>
<label>
  <input type="radio" bind:group={size} value="large" />
  Large
</label>

<p>Selected size: {size}</p>
```

**Select**

```svelte
<script>
  let selected = '';
  let multiple = [];
  
  let options = [
    { id: 1, name: 'Apple' },
    { id: 2, name: 'Banana' },
    { id: 3, name: 'Cherry' }
  ];
</script>

<!-- Single select -->
<select bind:value={selected}>
  <option value="">Choose...</option>
  {#each options as option}
    <option value={option.id}>{option.name}</option>
  {/each}
</select>

<!-- Multiple select -->
<select bind:value={multiple} multiple>
  {#each options as option}
    <option value={option.id}>{option.name}</option>
  {/each}
</select>

<p>Selected: {selected}</p>
<p>Multiple: {multiple.join(', ')}</p>
```

### Element Bindings

**DOM Properties**

```svelte
<script>
  let width;
  let height;
  let scrollY;
</script>

<div bind:clientWidth={width} bind:clientHeight={height}>
  Resize me
</div>

<svelte:window bind:scrollY />

<p>Width: {width}px, Height: {height}px</p>
<p>Scroll position: {scrollY}px</p>
```

**Element Reference**

```svelte
<script>
  import { onMount } from 'svelte';
  
  let inputElement;
  
  onMount(() => {
    inputElement.focus();
  });
</script>

<input bind:this={inputElement} />
```

### Component Bindings

**Bind to Component Props**

```svelte
<!-- Child.svelte -->
<script>
  export let value = '';
</script>

<input bind:value />

<!-- Parent.svelte -->
<script>
  import Child from './Child.svelte';
  let parentValue = '';
</script>

<Child bind:value={parentValue} />
<p>Parent sees: {parentValue}</p>
```

---

## Special Elements

### `<svelte:self>`

Allow component to recursively contain itself.

```svelte
<!-- TreeNode.svelte -->
<script>
  export let node;
</script>

<div>
  <p>{node.name}</p>
  {#if node.children}
    {#each node.children as child}
      <svelte:self node={child} />
    {/each}
  {/if}
</div>
```

### `<svelte:component>`

Dynamically render components.

```svelte
<script>
  import ComponentA from './ComponentA.svelte';
  import ComponentB from './ComponentB.svelte';
  
  let selected = 'A';
  
  $: component = selected === 'A' ? ComponentA : ComponentB;
</script>

<select bind:value={selected}>
  <option value="A">Component A</option>
  <option value="B">Component B</option>
</select>

<svelte:component this={component} />
```

### `<svelte:window>`

Bind to window events and properties.

```svelte
<script>
  let scrollY;
  let innerWidth;
  
  function handleKeydown(event) {
    console.log('Key pressed:', event.key);
  }
</script>

<svelte:window
  bind:scrollY
  bind:innerWidth
  on:keydown={handleKeydown}
  on:resize={() => console.log('Resized')}
/>

<p>Scroll: {scrollY}px, Width: {innerWidth}px</p>
```

### `<svelte:body>`

Bind to document.body events.

```svelte
<svelte:body on:mouseenter={() => console.log('Mouse entered')} />
```

### `<svelte:head>`

Insert elements into document head.

```svelte
<svelte:head>
  <title>My Page Title</title>
  <meta name="description" content="Page description" />
  <link rel="stylesheet" href="/styles.css" />
</svelte:head>
```
