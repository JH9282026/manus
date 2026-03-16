# Next.js Data Fetching and Caching

Comprehensive guide to data fetching patterns, caching strategies, and revalidation in Next.js 15.

---

## Fetch API Extensions

```typescript
// Cached by default
const data = await fetch('https://api.example.com/data');

// Opt out of caching
const data = await fetch('https://api.example.com/data', {
  cache: 'no-store'
});

// Revalidate every 60 seconds
const data = await fetch('https://api.example.com/data', {
  next: { revalidate: 60 }
});

// Tag-based revalidation
const data = await fetch('https://api.example.com/data', {
  next: { tags: ['products'] }
});
```

## Revalidation Strategies

### Time-based Revalidation

```typescript
// Route segment config
export const revalidate = 3600; // 1 hour

// Per-fetch revalidation
fetch(url, { next: { revalidate: 60 } });
```

### On-demand Revalidation

```typescript
import { revalidatePath, revalidateTag } from 'next/cache';

// Revalidate specific path
await revalidatePath('/posts');
await revalidatePath('/posts/[slug]', 'page');

// Revalidate by tag
await revalidateTag('products');
```

## Cache Behavior

### Static Rendering (Default)

```typescript
// Automatically cached at build time
export default async function Page() {
  const data = await fetch('https://api.example.com/data');
  return <div>{data}</div>;
}
```

### Dynamic Rendering

```typescript
// Force dynamic rendering
export const dynamic = 'force-dynamic';

// Or use dynamic functions
import { cookies, headers } from 'next/headers';

export default async function Page() {
  const cookieStore = cookies();
  // Now renders dynamically
}
```

## Request Memoization

Next.js automatically deduplicates fetch requests:

```typescript
async function getUser() {
  return fetch('https://api.example.com/user');
}

// Both calls use same request
const user1 = await getUser();
const user2 = await getUser();
```
