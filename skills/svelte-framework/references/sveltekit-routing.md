# SvelteKit Routing

Comprehensive guide to SvelteKit's file-based routing system.

---

## File-Based Routing Basics

SvelteKit uses the filesystem to define routes. Files in `src/routes/` automatically become routes.

### Basic Routes

```
src/routes/
  +page.svelte              # /
  about/
    +page.svelte            # /about
  contact/
    +page.svelte            # /contact
```

### Dynamic Routes

**Single Parameter:**
```
src/routes/
  blog/
    [slug]/
      +page.svelte          # /blog/:slug
```

**Multiple Parameters:**
```
src/routes/
  users/
    [userId]/
      posts/
        [postId]/
          +page.svelte      # /users/:userId/posts/:postId
```

**Optional Parameters:**
```
src/routes/
  [[lang]]/
    +page.svelte            # / or /en or /fr
```

### Rest Parameters

```
src/routes/
  files/
    [...path]/
      +page.svelte          # /files/* (matches any depth)
```

---

## Page Files

### `+page.svelte`

Defines the UI for a route:

```svelte
<script>
  export let data
</script>

<h1>{data.title}</h1>
<p>{data.content}</p>
```

### `+page.js` (Universal Load)

Runs on both server and client:

```javascript
export const load = async ({ fetch, params }) => {
  const response = await fetch(`/api/posts/${params.slug}`)
  const post = await response.json()
  
  return {
    post
  }
}
```

### `+page.server.js` (Server-Only Load)

Runs only on the server (access to secrets, database):

```javascript
import { db } from '$lib/server/database'

export const load = async ({ params, locals }) => {
  const post = await db.posts.findOne({ slug: params.slug })
  
  return {
    post
  }
}
```

---

## Layouts

### `+layout.svelte`

Shared UI for all child routes:

```svelte
<script>
  import Header from '$lib/Header.svelte'
  import Footer from '$lib/Footer.svelte'
</script>

<Header />

<main>
  <slot /> <!-- Child page content -->
</main>

<Footer />
```

### `+layout.js`

Load data for all child routes:

```javascript
export const load = async ({ fetch }) => {
  const response = await fetch('/api/navigation')
  const navigation = await response.json()
  
  return {
    navigation
  }
}
```

### Nested Layouts

```
src/routes/
  +layout.svelte            # Root layout
  dashboard/
    +layout.svelte          # Dashboard layout
    +page.svelte            # /dashboard
    settings/
      +page.svelte          # /dashboard/settings
```

### Layout Groups

Group routes without affecting URL:

```
src/routes/
  (marketing)/
    +layout.svelte
    about/
      +page.svelte          # /about (not /marketing/about)
    contact/
      +page.svelte          # /contact
  (app)/
    +layout.svelte
    dashboard/
      +page.svelte          # /dashboard
```

### Breaking Out of Layouts

```
src/routes/
  +layout.svelte
  admin/
    +layout@.svelte         # @ breaks out to root
    +page.svelte
```

---

## API Routes

### `+server.js`

Define API endpoints:

```javascript
import { json } from '@sveltejs/kit'

export async function GET({ url }) {
  const limit = url.searchParams.get('limit') || 10
  const posts = await fetchPosts(limit)
  
  return json(posts)
}

export async function POST({ request }) {
  const data = await request.json()
  const result = await createPost(data)
  
  return json(result, { status: 201 })
}

export async function PUT({ request, params }) {
  const data = await request.json()
  const result = await updatePost(params.id, data)
  
  return json(result)
}

export async function DELETE({ params }) {
  await deletePost(params.id)
  
  return new Response(null, { status: 204 })
}
```

### Request Helpers

```javascript
export async function POST({ request, cookies, locals }) {
  // Parse JSON body
  const json = await request.json()
  
  // Parse form data
  const formData = await request.formData()
  const name = formData.get('name')
  
  // Access cookies
  const sessionId = cookies.get('session')
  cookies.set('session', newSessionId, { path: '/' })
  
  // Access locals (set by hooks)
  const user = locals.user
  
  return json({ success: true })
}
```

---

## Navigation

### Links

```svelte
<a href="/about">About</a>
<a href="/blog/{post.slug}">Read More</a>
```

### Programmatic Navigation

```svelte
<script>
  import { goto } from '$app/navigation'
  
  function navigate() {
    goto('/dashboard')
  }
  
  function navigateWithOptions() {
    goto('/dashboard', {
      replaceState: true,
      noScroll: true,
      keepFocus: true
    })
  }
</script>
```

### Prefetching

```svelte
<a href="/slow-page" data-sveltekit-preload-data="hover">
  Hover to prefetch
</a>

<a href="/slow-page" data-sveltekit-preload-data="tap">
  Tap to prefetch
</a>
```

---

## Route Parameters

### Accessing Parameters

```svelte
<!-- src/routes/blog/[slug]/+page.svelte -->
<script>
  import { page } from '$app/stores'
  
  $: slug = $page.params.slug
</script>

<h1>Post: {slug}</h1>
```

### In Load Functions

```javascript
export const load = async ({ params }) => {
  const { slug } = params
  // Use slug
}
```

---

## Advanced Routing

### Route Matchers

Validate parameters:

```javascript
// src/params/integer.js
export function match(param) {
  return /^\d+$/.test(param)
}
```

**Usage:**
```
src/routes/
  users/
    [id=integer]/
      +page.svelte          # Only matches numeric IDs
```

### Route Priority

More specific routes take precedence:

```
src/routes/
  blog/
    latest/
      +page.svelte          # /blog/latest (higher priority)
    [slug]/
      +page.svelte          # /blog/:slug
```

---

## Error Handling

### `+error.svelte`

Custom error page:

```svelte
<script>
  import { page } from '$app/stores'
</script>

<h1>{$page.status}: {$page.error.message}</h1>
```

### Throwing Errors

```javascript
import { error } from '@sveltejs/kit'

export const load = async ({ params }) => {
  const post = await fetchPost(params.slug)
  
  if (!post) {
    throw error(404, 'Post not found')
  }
  
  return { post }
}
```

---

## Redirects

```javascript
import { redirect } from '@sveltejs/kit'

export const load = async ({ locals }) => {
  if (!locals.user) {
    throw redirect(307, '/login')
  }
  
  return { user: locals.user }
}
```

---

## Hooks

### `src/hooks.server.js`

Runs on every server request:

```javascript
export async function handle({ event, resolve }) {
  // Add user to locals
  event.locals.user = await getUserFromSession(event.cookies.get('session'))
  
  const response = await resolve(event)
  
  // Add custom headers
  response.headers.set('X-Custom-Header', 'value')
  
  return response
}

export async function handleError({ error, event }) {
  console.error('Error:', error)
  
  return {
    message: 'An error occurred'
  }
}
```

---

## Page Options

### `+page.js` or `+page.server.js`

```javascript
export const ssr = false          // Disable SSR
export const prerender = true     // Pre-render at build time
export const csr = false          // Disable client-side rendering
export const trailingSlash = 'always' // /about/
```

---

## Best Practices

1. **Use `+page.server.js` for sensitive data**: Keep secrets on the server
2. **Leverage layouts**: Share common UI and data loading
3. **Prefetch strategically**: Use `data-sveltekit-preload-data` for better UX
4. **Validate parameters**: Use route matchers for type safety
5. **Handle errors gracefully**: Provide custom error pages
6. **Use layout groups**: Organize routes without affecting URLs
7. **Optimize load functions**: Fetch only necessary data
