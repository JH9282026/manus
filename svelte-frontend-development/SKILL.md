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

### Built-in Transitions

**Transition Directives**
```svelte
<script>
  import { fade, fly, slide, scale } from 'svelte/transition';
  let visible = true;
</script>

{#if visible}
  <div transition:fade>Fades in and out</div>
  <div transition:fly={{ y: 200, duration: 500 }}>Flies in and out</div>
  <div transition:slide>Slides in and out</div>
  <div transition:scale>Scales in and out</div>
{/if}
```

**Separate In/Out Transitions**
```svelte
<script>
  import { fade, fly } from 'svelte/transition';
</script>

{#if visible}
  <div in:fly={{ y: 200 }} out:fade>
    Different in/out transitions
  </div>
{/if}
```

### Animations

**Animate Directive**
```svelte
<script>
  import { flip } from 'svelte/animate';
  import { quintOut } from 'svelte/easing';
  
  let items = [1, 2, 3, 4, 5];
  
  function shuffle() {
    items = items.sort(() => Math.random() - 0.5);
  }
</script>

<button on:click={shuffle}>Shuffle</button>

{#each items as item (item)}
  <div animate:flip={{ duration: 500, easing: quintOut }}>
    {item}
  </div>
{/each}
```

## SvelteKit Overview

### When to Use SvelteKit

**SvelteKit Benefits**
- File-based routing
- Server-side rendering (SSR)
- Static site generation (SSG)
- API routes
- Code splitting
- Preloading
- Deployment adapters

**Project Structure**
```
src/
├── routes/              # File-based routing
│   ├── +page.svelte    # Home page
│   ├── about/
│   │   └── +page.svelte
│   └── blog/
│       ├── +page.svelte
│       └── [slug]/
│           └── +page.svelte
├── lib/                 # Reusable components
└── app.html            # HTML template
```

### Routing Basics

**Page Routes**
- `src/routes/+page.svelte` → `/`
- `src/routes/about/+page.svelte` → `/about`
- `src/routes/blog/[slug]/+page.svelte` → `/blog/:slug`

**Loading Data**
```javascript
// +page.js or +page.server.js
export async function load({ params, fetch }) {
  const response = await fetch(`/api/posts/${params.slug}`);
  const post = await response.json();
  
  return {
    post
  };
}
```

## Performance Optimization

### Bundle Size Optimization

**Automatic Optimizations**
- Dead code elimination
- Component-level code splitting
- CSS scoping without runtime
- No virtual DOM overhead

**Manual Optimizations**
- Lazy load components with dynamic imports
- Use stores for shared state (avoid prop drilling)
- Minimize reactive statements
- Use `{#key}` blocks to force re-renders only when needed

### Rendering Performance

**Keyed Each Blocks**
```svelte
<!-- Without key - slower updates -->
{#each items as item}
  <Item {item} />
{/each}

<!-- With key - efficient updates -->
{#each items as item (item.id)}
  <Item {item} />
{/each}
```

**Immutable Data**
```svelte
<script>
  // Prefer immutable updates
  function addItem() {
    items = [...items, newItem];  // Good
    // items.push(newItem);        // Won't trigger reactivity
  }
</script>
```

## TypeScript Support

### TypeScript in Svelte

**Component with TypeScript**
```svelte
<script lang="ts">
  interface User {
    id: number;
    name: string;
    email: string;
  }
  
  export let user: User;
  
  let count: number = 0;
  
  function increment(): void {
    count += 1;
  }
</script>

<p>{user.name}</p>
<button on:click={increment}>Count: {count}</button>
```

**Typed Stores**
```typescript
import { writable, type Writable } from 'svelte/store';

interface User {
  id: number;
  name: string;
}

export const user: Writable<User | null> = writable(null);
```

## Testing Strategy

### Testing Approaches

**Unit Testing (Vitest)**
- Test component logic
- Test store behavior
- Test utility functions

**Component Testing (@testing-library/svelte)**
- Test component rendering
- Test user interactions
- Test component integration

**E2E Testing (Playwright)**
- Test complete user flows
- Test routing and navigation
- Test form submissions

## Deployment

### Build and Deploy

**Vite + Svelte (SPA)**
```bash
npm run build
# Deploy dist/ folder to static hosting
```

**SvelteKit Adapters**

| Adapter | Platform | Use Case |
|---------|----------|----------|
| adapter-static | Netlify, Vercel, GitHub Pages | Static sites (SSG) |
| adapter-node | Node.js servers, Docker | Server-side rendering |
| adapter-vercel | Vercel | Serverless + edge |
| adapter-netlify | Netlify | Serverless functions |
| adapter-cloudflare | Cloudflare Workers | Edge computing |

## Using the Reference Files

### When to Read Each Reference

**`/references/svelte-basics.md`** — Read when setting up new Svelte projects, understanding the compilation process, working with reactive statements, learning template syntax, handling events, or understanding Svelte's core reactivity system and how it differs from other frameworks.

**`/references/reactivity-stores.md`** — Read when managing application state, implementing reactive declarations, working with writable/readable/derived stores, creating custom stores, handling complex state logic, or implementing global state management patterns without external libraries.

**`/references/components-props.md`** — Read when creating reusable components, passing data between components, implementing slots and composition, working with component lifecycle, handling component events, or building component libraries and design systems.

**`/references/sveltekit-framework.md`** — Read when building full-stack applications, implementing file-based routing, working with server-side rendering, creating API endpoints, handling form actions, implementing authentication, or deploying SvelteKit applications to various platforms.
