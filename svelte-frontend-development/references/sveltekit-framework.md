# SvelteKit Framework

Comprehensive guide to building full-stack applications with SvelteKit, including routing, data loading, server-side rendering, and deployment.

---

## SvelteKit Overview

### What is SvelteKit?

SvelteKit is the official application framework for Svelte, providing:
- **File-based routing**: Routes defined by file structure
- **Server-side rendering (SSR)**: Render on server for better SEO and performance
- **Static site generation (SSG)**: Pre-render pages at build time
- **API routes**: Build backend endpoints alongside frontend
- **Code splitting**: Automatic code splitting per route
- **Preloading**: Intelligent preloading of route data
- **Adapters**: Deploy to various platforms (Vercel, Netlify, Node, etc.)

### When to Use SvelteKit

**Use SvelteKit for:**
- Multi-page applications
- SEO-critical websites
- Server-side rendering needs
- Full-stack applications
- Static sites with dynamic data
- Progressive enhancement

**Use Vite + Svelte for:**
- Single-page applications (SPAs)
- Client-side only apps
- Embedded widgets
- Simple prototypes

---

## Project Setup

### Creating a SvelteKit Project

```bash
npm create svelte@latest my-app
cd my-app
npm install
npm run dev
```

**Setup Options:**
- Skeleton project or demo app
- TypeScript support
- ESLint, Prettier
- Playwright for testing
- Vitest for unit testing

### Project Structure

```
my-app/
├── src/
│   ├── routes/              # File-based routing
│   │   ├── +page.svelte    # Home page
│   │   ├── +page.js        # Page data loading
│   │   ├── +layout.svelte  # Layout component
│   │   ├── +layout.js      # Layout data loading
│   │   ├── about/
│   │   │   └── +page.svelte
│   │   └── blog/
│   │       ├── +page.svelte
│   │       └── [slug]/
│   │           ├── +page.svelte
│   │           └── +page.js
│   ├── lib/                 # Reusable components and utilities
│   │   ├── components/
│   │   └── utils/
│   ├── app.html            # HTML template
│   └── app.css             # Global styles
├── static/                  # Static assets (served as-is)
│   ├── favicon.png
│   └── robots.txt
├── svelte.config.js        # SvelteKit configuration
├── vite.config.js          # Vite configuration
└── package.json
```

---

## Routing

### File-Based Routing

**Route Mapping**

| File Path | Route | Description |
|-----------|-------|-------------|
| `src/routes/+page.svelte` | `/` | Home page |
| `src/routes/about/+page.svelte` | `/about` | About page |
| `src/routes/blog/+page.svelte` | `/blog` | Blog index |
| `src/routes/blog/[slug]/+page.svelte` | `/blog/:slug` | Dynamic blog post |
| `src/routes/api/users/+server.js` | `/api/users` | API endpoint |

### Pages

**Basic Page**

```svelte
<!-- src/routes/about/+page.svelte -->
<script>
  let title = 'About Us';
</script>

<h1>{title}</h1>
<p>This is the about page.</p>
```

**Page with Data Loading**

```javascript
// src/routes/blog/+page.js
export async function load({ fetch }) {
  const response = await fetch('/api/posts');
  const posts = await response.json();
  
  return {
    posts
  };
}
```

```svelte
<!-- src/routes/blog/+page.svelte -->
<script>
  export let data;
</script>

<h1>Blog Posts</h1>
{#each data.posts as post}
  <article>
    <h2>{post.title}</h2>
    <p>{post.excerpt}</p>
    <a href="/blog/{post.slug}">Read more</a>
  </article>
{/each}
```

### Dynamic Routes

**Single Parameter**

```javascript
// src/routes/blog/[slug]/+page.js
export async function load({ params, fetch }) {
  const response = await fetch(`/api/posts/${params.slug}`);
  const post = await response.json();
  
  if (!post) {
    throw error(404, 'Post not found');
  }
  
  return {
    post
  };
}
```

```svelte
<!-- src/routes/blog/[slug]/+page.svelte -->
<script>
  export let data;
</script>

<article>
  <h1>{data.post.title}</h1>
  <div>{@html data.post.content}</div>
</article>
```

**Multiple Parameters**

```javascript
// src/routes/[category]/[slug]/+page.js
export async function load({ params }) {
  return {
    category: params.category,
    slug: params.slug
  };
}
```

**Rest Parameters**

```javascript
// src/routes/docs/[...path]/+page.js
// Matches /docs/a, /docs/a/b, /docs/a/b/c, etc.
export async function load({ params }) {
  const path = params.path;  // 'a/b/c'
  return { path };
}
```

**Optional Parameters**

```javascript
// src/routes/[[lang]]/+page.js
// Matches / and /en, /fr, etc.
export async function load({ params }) {
  const lang = params.lang || 'en';
  return { lang };
}
```

### Layouts

**Root Layout**

```svelte
<!-- src/routes/+layout.svelte -->
<script>
  import Header from '$lib/components/Header.svelte';
  import Footer from '$lib/components/Footer.svelte';
</script>

<div class="app">
  <Header />
  
  <main>
    <slot />  <!-- Page content renders here -->
  </main>
  
  <Footer />
</div>

<style>
  .app {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
  }
  
  main {
    flex: 1;
  }
</style>
```

**Nested Layouts**

```svelte
<!-- src/routes/blog/+layout.svelte -->
<div class="blog-layout">
  <aside>
    <nav>
      <a href="/blog">All Posts</a>
      <a href="/blog/categories">Categories</a>
    </nav>
  </aside>
  
  <div class="content">
    <slot />  <!-- Blog pages render here -->
  </div>
</div>
```

**Layout Data Loading**

```javascript
// src/routes/+layout.js
export async function load({ fetch }) {
  const response = await fetch('/api/navigation');
  const navigation = await response.json();
  
  return {
    navigation
  };
}
```

```svelte
<!-- src/routes/+layout.svelte -->
<script>
  export let data;
</script>

<nav>
  {#each data.navigation as item}
    <a href={item.url}>{item.label}</a>
  {/each}
</nav>

<slot />
```

---

## Data Loading

### Load Functions

**Universal Load (`+page.js`)**

Runs on both server and client.

```javascript
// src/routes/products/+page.js
export async function load({ fetch, params, url }) {
  const page = url.searchParams.get('page') || 1;
  
  const response = await fetch(`/api/products?page=${page}`);
  const products = await response.json();
  
  return {
    products,
    page: Number(page)
  };
}
```

**Server Load (`+page.server.js`)**

Runs only on server (access to database, secrets, etc.).

```javascript
// src/routes/admin/+page.server.js
import { db } from '$lib/server/database';

export async function load({ locals }) {
  // Access server-only resources
  const users = await db.users.findMany();
  
  return {
    users
  };
}
```

**Load Function Parameters**

```javascript
export async function load({
  params,        // Route parameters
  url,           // URL object
  route,         // Route info
  fetch,         // Fetch function (use this, not global fetch)
  setHeaders,    // Set response headers
  depends,       // Declare dependencies for invalidation
  parent         // Access parent layout data
}) {
  // ...
}
```

### Accessing Parent Data

```javascript
// src/routes/blog/[slug]/+page.js
export async function load({ params, parent }) {
  const parentData = await parent();
  
  const response = await fetch(`/api/posts/${params.slug}`);
  const post = await response.json();
  
  return {
    post,
    navigation: parentData.navigation  // From parent layout
  };
}
```

### Streaming with Promises

```javascript
// src/routes/dashboard/+page.js
export async function load({ fetch }) {
  // Start both requests in parallel
  const usersPromise = fetch('/api/users').then(r => r.json());
  const statsPromise = fetch('/api/stats').then(r => r.json());
  
  return {
    users: usersPromise,  // Return promise, not awaited value
    stats: statsPromise
  };
}
```

```svelte
<!-- src/routes/dashboard/+page.svelte -->
<script>
  export let data;
</script>

{#await data.users}
  <p>Loading users...</p>
{:then users}
  <UserList {users} />
{/await}

{#await data.stats}
  <p>Loading stats...</p>
{:then stats}
  <Statistics {stats} />
{/await}
```

---

## Form Actions

### Server Actions

**Basic Form Action**

```javascript
// src/routes/contact/+page.server.js
import { fail } from '@sveltejs/kit';

export const actions = {
  default: async ({ request }) => {
    const data = await request.formData();
    const name = data.get('name');
    const email = data.get('email');
    const message = data.get('message');
    
    // Validation
    if (!name || !email || !message) {
      return fail(400, {
        error: 'All fields are required',
        name,
        email,
        message
      });
    }
    
    // Process form (send email, save to database, etc.)
    await sendEmail({ name, email, message });
    
    return {
      success: true
    };
  }
};
```

```svelte
<!-- src/routes/contact/+page.svelte -->
<script>
  export let form;
</script>

<form method="POST">
  {#if form?.success}
    <p class="success">Message sent successfully!</p>
  {/if}
  
  {#if form?.error}
    <p class="error">{form.error}</p>
  {/if}
  
  <input name="name" value={form?.name || ''} required />
  <input name="email" type="email" value={form?.email || ''} required />
  <textarea name="message" value={form?.message || ''} required></textarea>
  
  <button type="submit">Send</button>
</form>
```

**Named Actions**

```javascript
// src/routes/todos/+page.server.js
export const actions = {
  create: async ({ request }) => {
    const data = await request.formData();
    const text = data.get('text');
    
    await db.todos.create({ text, done: false });
    
    return { success: true };
  },
  
  delete: async ({ request }) => {
    const data = await request.formData();
    const id = data.get('id');
    
    await db.todos.delete({ where: { id } });
    
    return { success: true };
  },
  
  toggle: async ({ request }) => {
    const data = await request.formData();
    const id = data.get('id');
    const done = data.get('done') === 'true';
    
    await db.todos.update({ where: { id }, data: { done: !done } });
    
    return { success: true };
  }
};
```

```svelte
<!-- src/routes/todos/+page.svelte -->
<script>
  export let data;
</script>

<!-- Create todo -->
<form method="POST" action="?/create">
  <input name="text" required />
  <button type="submit">Add</button>
</form>

<!-- Todo list -->
{#each data.todos as todo}
  <div>
    <form method="POST" action="?/toggle">
      <input type="hidden" name="id" value={todo.id} />
      <input type="hidden" name="done" value={todo.done} />
      <button type="submit">{todo.done ? '✓' : '○'}</button>
    </form>
    
    <span>{todo.text}</span>
    
    <form method="POST" action="?/delete">
      <input type="hidden" name="id" value={todo.id} />
      <button type="submit">Delete</button>
    </form>
  </div>
{/each}
```

### Progressive Enhancement

**use:enhance**

```svelte
<script>
  import { enhance } from '$app/forms';
  
  let loading = false;
</script>

<form 
  method="POST" 
  use:enhance={() => {
    loading = true;
    
    return async ({ result, update }) => {
      loading = false;
      await update();
    };
  }}
>
  <input name="text" required />
  <button type="submit" disabled={loading}>
    {loading ? 'Submitting...' : 'Submit'}
  </button>
</form>
```

---

## API Routes

### Server Endpoints

**GET Endpoint**

```javascript
// src/routes/api/posts/+server.js
import { json } from '@sveltejs/kit';
import { db } from '$lib/server/database';

export async function GET({ url }) {
  const page = Number(url.searchParams.get('page')) || 1;
  const limit = 10;
  
  const posts = await db.posts.findMany({
    skip: (page - 1) * limit,
    take: limit
  });
  
  return json(posts);
}
```

**POST Endpoint**

```javascript
// src/routes/api/posts/+server.js
import { json, error } from '@sveltejs/kit';
import { db } from '$lib/server/database';

export async function POST({ request, locals }) {
  // Check authentication
  if (!locals.user) {
    throw error(401, 'Unauthorized');
  }
  
  const data = await request.json();
  
  // Validation
  if (!data.title || !data.content) {
    throw error(400, 'Title and content are required');
  }
  
  const post = await db.posts.create({
    data: {
      title: data.title,
      content: data.content,
      authorId: locals.user.id
    }
  });
  
  return json(post, { status: 201 });
}
```

**Dynamic API Routes**

```javascript
// src/routes/api/posts/[id]/+server.js
import { json, error } from '@sveltejs/kit';
import { db } from '$lib/server/database';

export async function GET({ params }) {
  const post = await db.posts.findUnique({
    where: { id: params.id }
  });
  
  if (!post) {
    throw error(404, 'Post not found');
  }
  
  return json(post);
}

export async function PUT({ params, request }) {
  const data = await request.json();
  
  const post = await db.posts.update({
    where: { id: params.id },
    data
  });
  
  return json(post);
}

export async function DELETE({ params }) {
  await db.posts.delete({
    where: { id: params.id }
  });
  
  return new Response(null, { status: 204 });
}
```

---

## Hooks

### Server Hooks

**hooks.server.js**

```javascript
// src/hooks.server.js
import { redirect } from '@sveltejs/kit';

export async function handle({ event, resolve }) {
  // Run before every request
  
  // Get session from cookie
  const sessionId = event.cookies.get('session');
  
  if (sessionId) {
    const user = await getUserFromSession(sessionId);
    event.locals.user = user;
  }
  
  // Protect admin routes
  if (event.url.pathname.startsWith('/admin')) {
    if (!event.locals.user || event.locals.user.role !== 'admin') {
      throw redirect(303, '/login');
    }
  }
  
  const response = await resolve(event);
  
  // Run after request
  return response;
}

export async function handleError({ error, event }) {
  // Log errors
  console.error('Error:', error);
  
  return {
    message: 'An error occurred'
  };
}
```

### Client Hooks

**hooks.client.js**

```javascript
// src/hooks.client.js
export async function handleError({ error, event }) {
  // Log client-side errors
  console.error('Client error:', error);
  
  return {
    message: 'An error occurred'
  };
}
```

---

## Deployment

### Adapters

**Install Adapter**

```bash
# Vercel
npm install -D @sveltejs/adapter-vercel

# Netlify
npm install -D @sveltejs/adapter-netlify

# Node.js
npm install -D @sveltejs/adapter-node

# Static (SSG)
npm install -D @sveltejs/adapter-static

# Cloudflare
npm install -D @sveltejs/adapter-cloudflare
```

**Configure Adapter**

```javascript
// svelte.config.js
import adapter from '@sveltejs/adapter-vercel';

export default {
  kit: {
    adapter: adapter()
  }
};
```

### Static Site Generation

```javascript
// svelte.config.js
import adapter from '@sveltejs/adapter-static';

export default {
  kit: {
    adapter: adapter({
      pages: 'build',
      assets: 'build',
      fallback: null
    }),
    prerender: {
      entries: ['*']
    }
  }
};
```

**Prerendering Specific Pages**

```javascript
// src/routes/blog/+page.js
export const prerender = true;
```

### Environment Variables

```javascript
// .env
DATABASE_URL=postgresql://...
API_KEY=secret123

// Access in server code
import { env } from '$env/dynamic/private';
console.log(env.DATABASE_URL);

// Public env vars (exposed to client)
// .env
PUBLIC_API_URL=https://api.example.com

// Access in any code
import { PUBLIC_API_URL } from '$env/static/public';
```

### Build and Deploy

```bash
# Build for production
npm run build

# Preview production build
npm run preview

# Deploy (depends on adapter)
# Vercel: vercel deploy
# Netlify: netlify deploy
# Node: node build/index.js
```
