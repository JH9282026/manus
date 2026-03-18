---
name: svelte-frontend-development
description: "Build fast, reactive web applications using Svelte framework with component-based architecture, reactive stores, minimal boilerplate, and SvelteKit for full-stack development. Use for creating single-page applications, static sites, server-side rendered apps, progressive web apps, lightweight UI components, reactive state management, form handling, animations, and high-performance frontend systems with smaller bundle sizes."
---

# Svelte Frontend Development

Build highly performant, reactive web applications using Svelte's compiler-based approach with minimal boilerplate and intuitive syntax.

## Overview

Svelte is a radical new approach to building user interfaces. Unlike traditional frameworks that do most of their work in the browser, Svelte shifts that work into a compile step that happens when you build your app. This skill covers Svelte fundamentals, component architecture, reactivity system, stores, animations, SvelteKit for full-stack development, and deployment strategies. Svelte excels at creating fast, lightweight applications with excellent developer experience.

## Quick Start: Project Type Selection

| Application Type | Framework Choice | Key Features | Reference |
|-----------------|------------------|--------------|----------|
| Static website | SvelteKit (adapter-static) | SSG, prerendering, routing | `/references/sveltekit-framework.md` |
| Server-rendered app | SvelteKit (adapter-node) | SSR, API routes, dynamic data | `/references/sveltekit-framework.md` |
| Single-page app | Vite + Svelte | Client-side routing, lightweight | `/references/svelte-basics.md` |
| Component library | Svelte + TypeScript | Reusable components, type safety | `/references/components-props.md` |
| Progressive Web App | SvelteKit + service workers | Offline support, installable | `/references/sveltekit-framework.md` |

## Core Principles

### Compiler-Based Approach

**No Virtual DOM**
- Svelte compiles components to highly efficient imperative code
- Updates DOM directly when state changes
- Smaller bundle sizes (no framework runtime)
- Faster performance (no diffing algorithm)

**Build-Time Optimization**
- Dead code elimination at compile time
- Automatic code splitting
- CSS scoping without runtime overhead
- Optimal update code generation

### Reactive by Default

**Automatic Reactivity**
- Assignments trigger updates automatically
- No need for setState, hooks, or observables
- Reactive declarations with `$:` label
- Reactive statements run when dependencies change

**Minimal Boilerplate**
- No class components or lifecycle complexity
- Simple, readable syntax
- Less code to achieve the same results
- Intuitive state management

## Component Structure

### Basic Component Anatomy

**Three Sections**
```svelte
<script>
  // JavaScript logic
  let count = 0;
  
  function increment() {
    count += 1;
  }
</script>

<style>
  /* Scoped CSS */
  button {
    background: blue;
    color: white;
  }
</style>

<!-- HTML template -->
<button on:click={increment}>
  Count: {count}
</button>
```

**Component Features**
- `<script>`: Component logic and state
- `<style>`: Scoped CSS (automatically namespaced)
- Template: HTML with Svelte syntax
- No wrapper div required
- Reactive by default

### Reactivity System

**Reactive Assignments**
```svelte
<script>
  let count = 0;
  
  // This triggers reactivity
  function increment() {
    count += 1;  // Assignment triggers update
  }
  
  // Array/object mutations need reassignment
  let items = [1, 2, 3];
  
  function addItem() {
    items = [...items, items.length + 1];  // Reassignment triggers update
  }
</script>
```

**Reactive Declarations**
```svelte
<script>
  let count = 0;
  
  // Reactive declaration - recalculates when count changes
  $: doubled = count * 2;
  
  // Reactive statement - runs when count changes
  $: console.log('Count is now:', count);
  
  // Reactive block - multiple statements
  $: {
    console.log('Count changed to:', count);
    if (count > 10) {
      alert('Count is high!');
    }
  }
</script>

<p>Count: {count}</p>
<p>Doubled: {doubled}</p>
```

## Template Syntax

### Conditional Rendering

**if/else Blocks**
```svelte
{#if user}
  <p>Welcome, {user.name}!</p>
{:else if loading}
  <p>Loading...</p>
{:else}
  <p>Please log in.</p>
{/if}
```

### List Rendering

**each Blocks**
```svelte
<script>
  let items = [
    { id: 1, name: 'Apple' },
    { id: 2, name: 'Banana' },
    { id: 3, name: 'Cherry' }
  ];
</script>

<!-- Basic each -->
{#each items as item}
  <p>{item.name}</p>
{/each}

<!-- With index -->
{#each items as item, i}
  <p>{i + 1}. {item.name}</p>
{/each}

<!-- With key (for efficient updates) -->
{#each items as item (item.id)}
  <p>{item.name}</p>
{/each}

<!-- With else (empty state) -->
{#each items as item}
  <p>{item.name}</p>
{:else}
  <p>No items found</p>
{/each}
```

### Event Handling

**Event Directives**
```svelte
<script>
  function handleClick() {
    console.log('Clicked!');
  }
  
  function handleInput(event) {
    console.log(event.target.value);
  }
</script>

<!-- Basic event -->
<button on:click={handleClick}>Click me</button>

<!-- Inline handler -->
<button on:click={() => console.log('Clicked!')}>Click me</button>

<!-- Event modifiers -->
<button on:click|preventDefault|stopPropagation={handleClick}>Click me</button>

<!-- Input events -->
<input on:input={handleInput} />
<input on:keydown={(e) => console.log(e.key)} />
```

**Event Modifiers**
- `preventDefault`: Calls event.preventDefault()
- `stopPropagation`: Calls event.stopPropagation()
- `passive`: Improves scrolling performance
- `capture`: Fires in capture phase
- `once`: Remove handler after first run
- `self`: Only trigger if event.target is element itself

### Bindings

**Two-Way Binding**
```svelte
<script>
  let name = '';
  let checked = false;
  let selected = '';
  let value = 5;
</script>

<!-- Text input -->
<input bind:value={name} />

<!-- Checkbox -->
<input type="checkbox" bind:checked />

<!-- Select -->
<select bind:value={selected}>
  <option value="a">A</option>
  <option value="b">B</option>
</select>

<!-- Range -->
<input type="range" bind:value min="0" max="10" />

<!-- Textarea -->
<textarea bind:value={name}></textarea>
```

**Component Bindings**
```svelte
<!-- Bind to component prop -->
<ChildComponent bind:value={parentValue} />

<!-- Bind to DOM properties -->
<div bind:clientWidth={width} bind:clientHeight={height}>
  Resize me
</div>
```

## Component Communication

### Props (Parent to Child)

**Declaring Props**
```svelte
<!-- Child.svelte -->
<script>
  export let name;           // Required prop
  export let age = 0;        // Optional with default
  export let user = null;    // Optional object
</script>

<p>{name} is {age} years old</p>

<!-- Parent.svelte -->
<script>
  import Child from './Child.svelte';
</script>

<Child name="Alice" age={30} />
```

**Prop Spreading**
```svelte
<script>
  let props = {
    name: 'Alice',
    age: 30,
    email: 'alice@example.com'
  };
</script>

<Child {...props} />
```

### Events (Child to Parent)

**Dispatching Events**
```svelte
<!-- Child.svelte -->
<script>
  import { createEventDispatcher } from 'svelte';
  
  const dispatch = createEventDispatcher();
  
  function handleClick() {
    dispatch('message', {
      text: 'Hello from child'
    });
  }
</script>

<button on:click={handleClick}>Send Message</button>

<!-- Parent.svelte -->
<script>
  import Child from './Child.svelte';
  
  function handleMessage(event) {
    console.log(event.detail.text);
  }
</script>

<Child on:message={handleMessage} />
```

**Event Forwarding**
```svelte
<!-- Wrapper.svelte -->
<button on:click>
  <slot />
</button>

<!-- Parent.svelte -->
<Wrapper on:click={handleClick}>
  Click me
</Wrapper>
```

## Lifecycle Functions

### Component Lifecycle

**Available Lifecycle Functions**
```svelte
<script>
  import { onMount, onDestroy, beforeUpdate, afterUpdate, tick } from 'svelte';
  
  // Runs after component is first rendered to DOM
  onMount(() => {
    console.log('Component mounted');
    
    // Return cleanup function
    return () => {
      console.log('Cleanup on unmount');
    };
  });
  
  // Runs before component is destroyed
  onDestroy(() => {
    console.log('Component destroyed');
  });
  
  // Runs before DOM is updated
  beforeUpdate(() => {
    console.log('Before update');
  });
  
  // Runs after DOM is updated
  afterUpdate(() => {
    console.log('After update');
  });
  
  // Wait for pending state changes to be applied
  async function handleClick() {
    count += 1;
    await tick();  // Wait for DOM update
    console.log('DOM updated');
  }
</script>
```

## Stores for State Management

### Store Types

**Writable Store**
```javascript
// stores.js
import { writable } from 'svelte/store';

export const count = writable(0);
export const user = writable(null);
```

**Readable Store**
```javascript
import { readable } from 'svelte/store';

export const time = readable(new Date(), (set) => {
  const interval = setInterval(() => {
    set(new Date());
  }, 1000);
  
  return () => clearInterval(interval);
});
```

**Derived Store**
```javascript
import { derived } from 'svelte/store';
import { count } from './stores';

export const doubled = derived(count, $count => $count * 2);
```

**Using Stores in Components**
```svelte
<script>
  import { count, user } from './stores';
  
  // Auto-subscription with $ prefix
  // Automatically unsubscribes on component destroy
</script>

<p>Count: {$count}</p>
<button on:click={() => $count += 1}>Increment</button>
<button on:click={() => count.set(0)}>Reset</button>
<button on:click={() => count.update(n => n + 1)}>Update</button>
```

## Styling Approaches

### Scoped Styles

**Component Styles**
```svelte
<style>
  /* Automatically scoped to this component */
  p {
    color: blue;
  }
  
  .highlight {
    background: yellow;
  }
</style>

<p class="highlight">Styled text</p>
```

**Global Styles**
```svelte
<style>
  :global(body) {
    margin: 0;
    font-family: sans-serif;
  }
  
  /* Mix scoped and global */
  .container :global(.external-class) {
    color: red;
  }
</style>
```

### Dynamic Styles

**Class Directive**
```svelte
<script>
  let active = false;
  let important = true;
</script>

<!-- Conditional class -->
<div class:active>Content</div>
<div class:active={active}>Content</div>

<!-- Multiple classes -->
<div class:active class:important>Content</div>

<!-- Dynamic class name -->
<div class="{active ? 'active' : ''}">Content</div>
```

**Style Directive**
```svelte
<script>
  let color = 'blue';
  let size = 16;
</script>

<p style:color style:font-size="{size}px">
  Styled text
</p>
```

## Animations and Transitions

Svelte provides built-in transition and animation directives for smooth UI effects. Use `transition:`, `in:`, and `out:` directives with built-in transitions like `fade`, `fly`, `slide`, and `scale`. The `animate:` directive (e.g., `animate:flip`) handles list reordering animations. All transitions are highly performant and customizable with duration, delay, and easing options.

## SvelteKit Overview

SvelteKit is the official full-stack framework for Svelte, providing file-based routing, SSR, SSG, API routes, and deployment adapters. Routes are defined by file structure in `src/routes/` with `+page.svelte` files. Use `+page.js` or `+page.server.js` for data loading with the `load` function. Dynamic routes use `[param]` syntax. SvelteKit supports layouts (`+layout.svelte`), form actions, and various deployment targets via adapters.

## Performance Optimization

Svelte's compiler provides automatic optimizations including dead code elimination, component-level code splitting, and CSS scoping without runtime overhead. For manual optimization, use keyed `{#each}` blocks for efficient list updates, prefer immutable data patterns for reactivity, lazy load components with dynamic imports, and use stores for shared state to avoid prop drilling.

## TypeScript Support

Svelte has excellent TypeScript support. Use `<script lang="ts">` to enable TypeScript in components. Define interfaces for props, type stores with `Writable<T>`, and type event dispatchers. SvelteKit projects can be initialized with TypeScript support, providing full type safety across routes, load functions, and form actions.

## Testing Strategy

Test Svelte applications with Vitest for unit testing (component logic, stores, utilities), @testing-library/svelte for component testing (rendering, interactions, integration), and Playwright for E2E testing (user flows, routing, form submissions). SvelteKit projects can be initialized with testing setup included.

## Deployment

For Vite + Svelte SPAs, run `npm run build` and deploy the `dist/` folder to static hosting. SvelteKit uses adapters for different platforms: `adapter-static` for static sites (Netlify, Vercel, GitHub Pages), `adapter-node` for Node.js servers, `adapter-vercel` for Vercel serverless, `adapter-netlify` for Netlify functions, and `adapter-cloudflare` for Cloudflare Workers. Configure adapters in `svelte.config.js`.

## Using the Reference Files

### When to Read Each Reference

**`/references/svelte-basics.md`** — Read when setting up new Svelte projects, understanding the compilation process, working with reactive statements, learning template syntax, handling events, or understanding Svelte's core reactivity system and how it differs from other frameworks.

**`/references/reactivity-stores.md`** — Read when managing application state, implementing reactive declarations, working with writable/readable/derived stores, creating custom stores, handling complex state logic, or implementing global state management patterns without external libraries.

**`/references/components-props.md`** — Read when creating reusable components, passing data between components, implementing slots and composition, working with component lifecycle, handling component events, or building component libraries and design systems.

**`/references/sveltekit-framework.md`** — Read when building full-stack applications, implementing file-based routing, working with server-side rendering, creating API endpoints, handling form actions, implementing authentication, or deploying SvelteKit applications to various platforms.
