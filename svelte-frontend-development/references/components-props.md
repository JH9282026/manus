# Components and Props

Comprehensive guide to creating, composing, and communicating between Svelte components.

---

## Component Basics

### Creating Components

**Simple Component**

```svelte
<!-- Button.svelte -->
<script>
  export let label = 'Click me';
  export let variant = 'primary';
  
  function handleClick() {
    console.log('Button clicked');
  }
</script>

<style>
  button {
    padding: 0.5rem 1rem;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  .primary {
    background: blue;
    color: white;
  }
  
  .secondary {
    background: gray;
    color: white;
  }
</style>

<button class={variant} on:click={handleClick}>
  {label}
</button>
```

**Using Components**

```svelte
<script>
  import Button from './Button.svelte';
</script>

<Button label="Submit" variant="primary" />
<Button label="Cancel" variant="secondary" />
```

### Props

**Declaring Props**

```svelte
<!-- UserCard.svelte -->
<script>
  // Required prop (no default)
  export let user;
  
  // Optional prop with default
  export let showEmail = false;
  
  // Prop with type checking (TypeScript)
  export let age = 0;
  
  // Prop with validation
  export let status = 'active';
  $: if (!['active', 'inactive', 'pending'].includes(status)) {
    console.warn('Invalid status:', status);
  }
</script>

<div class="user-card">
  <h3>{user.name}</h3>
  <p>Age: {age}</p>
  <p>Status: {status}</p>
  {#if showEmail}
    <p>Email: {user.email}</p>
  {/if}
</div>
```

**Passing Props**

```svelte
<script>
  import UserCard from './UserCard.svelte';
  
  let user = {
    name: 'Alice',
    email: 'alice@example.com'
  };
</script>

<!-- Explicit props -->
<UserCard user={user} age={30} status="active" showEmail={true} />

<!-- Shorthand (when variable name matches prop name) -->
<UserCard {user} age={30} status="active" showEmail />

<!-- Spread props -->
<UserCard {...user} age={30} />
```

**Prop Reactivity**

```svelte
<!-- Child.svelte -->
<script>
  export let count;
  
  // Reactive declaration based on prop
  $: doubled = count * 2;
  
  // Reactive statement when prop changes
  $: console.log('Count changed to:', count);
  
  // Prop with setter (runs when prop changes)
  let _user;
  export let user;
  $: if (user !== _user) {
    _user = user;
    console.log('User changed:', user);
  }
</script>

<p>Count: {count}</p>
<p>Doubled: {doubled}</p>
```

### $$props and $$restProps

**Accessing All Props**

```svelte
<script>
  export let name;
  export let age;
  
  // $$props contains all props passed to component
  console.log($$props);  // { name: 'Alice', age: 30, ... }
</script>
```

**Rest Props (Forwarding Unknown Props)**

```svelte
<!-- Wrapper.svelte -->
<script>
  export let variant = 'primary';
  
  // $$restProps contains all props except declared ones
  // Useful for forwarding props to child elements
</script>

<button class={variant} {...$$restProps}>
  <slot />
</button>

<!-- Usage -->
<Wrapper variant="primary" type="submit" disabled>
  Submit
</Wrapper>
<!-- Renders: <button class="primary" type="submit" disabled>Submit</button> -->
```

---

## Component Communication

### Events

**Dispatching Custom Events**

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
  
  function handleSubmit() {
    dispatch('submit', {
      data: { name: 'Alice', age: 30 }
    });
  }
</script>

<button on:click={handleClick}>Send Message</button>
<button on:click={handleSubmit}>Submit</button>
```

**Listening to Custom Events**

```svelte
<!-- Parent.svelte -->
<script>
  import Child from './Child.svelte';
  
  function handleMessage(event) {
    console.log('Received:', event.detail.text);
    console.log('At:', event.detail.timestamp);
  }
  
  function handleSubmit(event) {
    console.log('Form data:', event.detail.data);
  }
</script>

<Child on:message={handleMessage} on:submit={handleSubmit} />
```

**Event Forwarding**

```svelte
<!-- Wrapper.svelte -->
<script>
  import Button from './Button.svelte';
</script>

<!-- Forward click event -->
<Button on:click />

<!-- Forward custom event -->
<Button on:submit />

<!-- Forward all events -->
<Button on:click on:submit on:message />
```

**Event Modifiers with Custom Events**

```svelte
<!-- Child can't use modifiers, but parent can -->
<Child on:message|once={handleMessage} />
```

### Bindings

**Binding to Component Props**

```svelte
<!-- Input.svelte -->
<script>
  export let value = '';
</script>

<input bind:value />

<!-- Parent.svelte -->
<script>
  import Input from './Input.svelte';
  let name = '';
</script>

<Input bind:value={name} />
<p>You typed: {name}</p>
```

**Two-Way Binding Pattern**

```svelte
<!-- Counter.svelte -->
<script>
  export let count = 0;
</script>

<button on:click={() => count -= 1}>-</button>
<span>{count}</span>
<button on:click={() => count += 1}>+</button>

<!-- Parent.svelte -->
<script>
  import Counter from './Counter.svelte';
  let value = 0;
</script>

<Counter bind:count={value} />
<p>Parent sees: {value}</p>
```

**Binding to Component Instance**

```svelte
<!-- Child.svelte -->
<script>
  export function focus() {
    input.focus();
  }
  
  let input;
</script>

<input bind:this={input} />

<!-- Parent.svelte -->
<script>
  import Child from './Child.svelte';
  let childComponent;
  
  function focusChild() {
    childComponent.focus();
  }
</script>

<Child bind:this={childComponent} />
<button on:click={focusChild}>Focus child input</button>
```

---

## Slots

### Basic Slots

**Default Slot**

```svelte
<!-- Card.svelte -->
<div class="card">
  <slot>
    <!-- Fallback content if no slot content provided -->
    <p>No content provided</p>
  </slot>
</div>

<!-- Usage -->
<Card>
  <h2>Title</h2>
  <p>Content goes here</p>
</Card>
```

### Named Slots

**Multiple Slots**

```svelte
<!-- Card.svelte -->
<div class="card">
  <header>
    <slot name="header">
      <h2>Default Header</h2>
    </slot>
  </header>
  
  <main>
    <slot>
      <p>Default content</p>
    </slot>
  </main>
  
  <footer>
    <slot name="footer">
      <p>Default footer</p>
    </slot>
  </footer>
</div>

<!-- Usage -->
<Card>
  <div slot="header">
    <h1>Custom Header</h1>
  </div>
  
  <p>Main content</p>
  <p>More content</p>
  
  <div slot="footer">
    <button>Action</button>
  </div>
</Card>
```

### Slot Props

**Passing Data to Slot Content**

```svelte
<!-- List.svelte -->
<script>
  export let items = [];
</script>

<ul>
  {#each items as item, index}
    <li>
      <slot item={item} index={index}>
        <!-- Fallback -->
        {item.name}
      </slot>
    </li>
  {/each}
</ul>

<!-- Usage -->
<script>
  import List from './List.svelte';
  
  let users = [
    { id: 1, name: 'Alice', email: 'alice@example.com' },
    { id: 2, name: 'Bob', email: 'bob@example.com' }
  ];
</script>

<List items={users} let:item let:index>
  <strong>{index + 1}.</strong>
  {item.name} ({item.email})
</List>
```

**Named Slots with Props**

```svelte
<!-- Table.svelte -->
<script>
  export let data = [];
  export let columns = [];
</script>

<table>
  <thead>
    <tr>
      {#each columns as column}
        <th>
          <slot name="header" column={column}>
            {column.label}
          </slot>
        </th>
      {/each}
    </tr>
  </thead>
  <tbody>
    {#each data as row}
      <tr>
        {#each columns as column}
          <td>
            <slot name="cell" row={row} column={column}>
              {row[column.key]}
            </slot>
          </td>
        {/each}
      </tr>
    {/each}
  </tbody>
</table>

<!-- Usage -->
<Table {data} {columns}>
  <div slot="header" let:column>
    <strong>{column.label}</strong>
  </div>
  
  <div slot="cell" let:row let:column>
    {#if column.key === 'email'}
      <a href="mailto:{row.email}">{row.email}</a>
    {:else}
      {row[column.key]}
    {/if}
  </div>
</Table>
```

### Slot Forwarding

```svelte
<!-- Wrapper.svelte -->
<div class="wrapper">
  <slot />
</div>

<!-- Container.svelte -->
<div class="container">
  <Wrapper>
    <slot />  <!-- Forward slot to Wrapper -->
  </Wrapper>
</div>

<!-- Usage -->
<Container>
  <p>This content goes through Container to Wrapper</p>
</Container>
```

---

## Component Lifecycle

### Lifecycle Functions

**onMount**

```svelte
<script>
  import { onMount } from 'svelte';
  
  let data = [];
  
  onMount(async () => {
    // Runs after component is first rendered to DOM
    const response = await fetch('/api/data');
    data = await response.json();
    
    // Return cleanup function (runs on component destroy)
    return () => {
      console.log('Component unmounted');
    };
  });
</script>
```

**onDestroy**

```svelte
<script>
  import { onMount, onDestroy } from 'svelte';
  
  let interval;
  
  onMount(() => {
    interval = setInterval(() => {
      console.log('Tick');
    }, 1000);
  });
  
  onDestroy(() => {
    // Clean up interval
    if (interval) {
      clearInterval(interval);
    }
  });
</script>
```

**beforeUpdate and afterUpdate**

```svelte
<script>
  import { beforeUpdate, afterUpdate } from 'svelte';
  
  let count = 0;
  
  beforeUpdate(() => {
    // Runs before DOM is updated
    console.log('Before update, count:', count);
  });
  
  afterUpdate(() => {
    // Runs after DOM is updated
    console.log('After update, count:', count);
  });
</script>

<button on:click={() => count += 1}>
  Count: {count}
</button>
```

**tick**

```svelte
<script>
  import { tick } from 'svelte';
  
  let count = 0;
  let element;
  
  async function handleClick() {
    count += 1;
    
    // Wait for DOM to update
    await tick();
    
    // Now DOM is updated
    console.log('Element text:', element.textContent);
  }
</script>

<button on:click={handleClick}>
  <span bind:this={element}>Count: {count}</span>
</button>
```

---

## Component Composition Patterns

### Render Props Pattern (Slot Props)

```svelte
<!-- DataProvider.svelte -->
<script>
  export let url;
  
  let data = null;
  let loading = true;
  let error = null;
  
  async function load() {
    loading = true;
    try {
      const response = await fetch(url);
      data = await response.json();
    } catch (e) {
      error = e.message;
    } finally {
      loading = false;
    }
  }
  
  $: if (url) load();
</script>

<slot {data} {loading} {error} />

<!-- Usage -->
<DataProvider url="/api/users" let:data let:loading let:error>
  {#if loading}
    <p>Loading...</p>
  {:else if error}
    <p>Error: {error}</p>
  {:else if data}
    {#each data as user}
      <p>{user.name}</p>
    {/each}
  {/if}
</DataProvider>
```

### Higher-Order Component Pattern

```svelte
<!-- withAuth.svelte -->
<script>
  import { getContext } from 'svelte';
  
  export let component;
  export let requiredRole = 'user';
  
  const auth = getContext('auth');
  
  $: hasAccess = $auth.user && $auth.user.role === requiredRole;
</script>

{#if hasAccess}
  <svelte:component this={component} {...$$restProps} />
{:else}
  <p>Access denied</p>
{/if}

<!-- Usage -->
<script>
  import withAuth from './withAuth.svelte';
  import AdminPanel from './AdminPanel.svelte';
</script>

<svelte:component this={withAuth} component={AdminPanel} requiredRole="admin" />
```

### Compound Components

```svelte
<!-- Tabs.svelte -->
<script>
  import { setContext } from 'svelte';
  import { writable } from 'svelte/store';
  
  export let activeTab = 0;
  
  const active = writable(activeTab);
  setContext('tabs', {
    active,
    setActive: (index) => active.set(index)
  });
</script>

<div class="tabs">
  <slot />
</div>

<!-- TabList.svelte -->
<script>
  import { getContext } from 'svelte';
  const { active } = getContext('tabs');
</script>

<div class="tab-list">
  <slot active={$active} />
</div>

<!-- Tab.svelte -->
<script>
  import { getContext } from 'svelte';
  
  export let index;
  
  const { active, setActive } = getContext('tabs');
  $: isActive = $active === index;
</script>

<button 
  class:active={isActive}
  on:click={() => setActive(index)}
>
  <slot />
</button>

<!-- TabPanel.svelte -->
<script>
  import { getContext } from 'svelte';
  
  export let index;
  
  const { active } = getContext('tabs');
  $: isActive = $active === index;
</script>

{#if isActive}
  <div class="tab-panel">
    <slot />
  </div>
{/if}

<!-- Usage -->
<script>
  import Tabs from './Tabs.svelte';
  import TabList from './TabList.svelte';
  import Tab from './Tab.svelte';
  import TabPanel from './TabPanel.svelte';
</script>

<Tabs>
  <TabList>
    <Tab index={0}>Tab 1</Tab>
    <Tab index={1}>Tab 2</Tab>
    <Tab index={2}>Tab 3</Tab>
  </TabList>
  
  <TabPanel index={0}>
    <p>Content 1</p>
  </TabPanel>
  <TabPanel index={1}>
    <p>Content 2</p>
  </TabPanel>
  <TabPanel index={2}>
    <p>Content 3</p>
  </TabPanel>
</Tabs>
```

---

## TypeScript Support

### Typed Components

```svelte
<script lang="ts">
  interface User {
    id: number;
    name: string;
    email: string;
  }
  
  export let user: User;
  export let showEmail: boolean = false;
  
  function handleClick(): void {
    console.log('Clicked');
  }
</script>

<div>
  <h3>{user.name}</h3>
  {#if showEmail}
    <p>{user.email}</p>
  {/if}
</div>
```

### Typed Events

```svelte
<script lang="ts">
  import { createEventDispatcher } from 'svelte';
  
  interface Events {
    submit: { data: FormData };
    cancel: never;
  }
  
  const dispatch = createEventDispatcher<Events>();
  
  function handleSubmit() {
    dispatch('submit', { data: new FormData() });
  }
</script>
```

### Typed Slots

```svelte
<script lang="ts">
  interface Item {
    id: number;
    name: string;
  }
  
  export let items: Item[];
</script>

{#each items as item}
  <slot item={item} />
{/each}
```
