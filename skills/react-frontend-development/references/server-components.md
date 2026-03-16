# React Server Components

Understanding Server Components, Client Components, and the server/client boundary in modern React applications.

---

## Server Components Overview

React Server Components (RSC) enable rendering components on the server with zero client-side JavaScript cost. Introduced in React 18 and fully integrated in Next.js 13+ App Router.

### Key Benefits

- **Zero Bundle Size**: Server Components don't ship JavaScript to the client
- **Direct Backend Access**: Query databases, read files, access secrets
- **Automatic Code Splitting**: Only Client Components are bundled
- **Improved Performance**: Reduced client-side JavaScript, faster initial loads
- **SEO Friendly**: Fully rendered HTML sent to client

### Server vs Client Components

| Feature | Server Component | Client Component |
|---------|-----------------|------------------|
| Default in Next.js App Router | Yes | No (requires `"use client"`) |
| Can use async/await | Yes | No (except in Server Actions) |
| Can access backend directly | Yes | No |
| Can use hooks (useState, useEffect) | No | Yes |
| Can use browser APIs | No | Yes |
| Can receive Server Components as props | Yes | Yes (as children) |
| Bundle size impact | Zero | Included in bundle |

## Server Component Patterns

### Data Fetching in Server Components

```typescript
// app/users/page.tsx
import { db } from '@/lib/database';

export default async function UsersPage() {
  // Direct database access - no API route needed
  const users = await db.user.findMany();
  
  return (
    <div>
      <h1>Users</h1>
      <ul>
        {users.map(user => (
          <li key={user.id}>{user.name}</li>
        ))}
      </ul>
    </div>
  );
}
```

### Parallel Data Fetching

```typescript
async function getData() {
  const [users, posts, comments] = await Promise.all([
    fetch('/api/users'),
    fetch('/api/posts'),
    fetch('/api/comments'),
  ]);
  
  return { users, posts, comments };
}

export default async function Dashboard() {
  const { users, posts, comments } = await getData();
  
  return (
    <div>
      <UserList users={users} />
      <PostList posts={posts} />
      <CommentList comments={comments} />
    </div>
  );
}
```

### Sequential Data Fetching

```typescript
export default async function UserProfile({ params }) {
  const user = await getUser(params.id);
  // Wait for user before fetching posts
  const posts = await getUserPosts(user.id);
  
  return (
    <div>
      <UserHeader user={user} />
      <UserPosts posts={posts} />
    </div>
  );
}
```

## Client Component Patterns

### When to Use Client Components

Use `"use client"` directive when you need:

- **Interactivity**: Event handlers (onClick, onChange)
- **State**: useState, useReducer
- **Effects**: useEffect, useLayoutEffect
- **Browser APIs**: localStorage, window, document
- **Custom Hooks**: Any hook-based logic
- **Class Components**: Legacy class-based components

### Client Component Example

```typescript
// components/Counter.tsx
"use client";

import { useState } from 'react';

export function Counter() {
  const [count, setCount] = useState(0);
  
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>
        Increment
      </button>
    </div>
  );
}
```

### Composing Server and Client Components

```typescript
// app/page.tsx (Server Component)
import { Counter } from '@/components/Counter'; // Client Component
import { UserList } from '@/components/UserList'; // Server Component

export default async function HomePage() {
  const users = await getUsers();
  
  return (
    <div>
      <h1>Home Page</h1>
      <Counter /> {/* Client Component */}
      <UserList users={users} /> {/* Server Component */}
    </div>
  );
}
```

## The Server/Client Boundary

### Passing Props Across Boundary

**Serializable Props Only**:

```typescript
// ✅ Good - serializable data
<ClientComponent 
  user={{ id: 1, name: 'John' }}
  count={42}
  items={['a', 'b', 'c']}
/>

// ❌ Bad - functions not serializable
<ClientComponent 
  onClick={() => console.log('click')}
  callback={someFunction}
/>
```

### Passing Server Components as Children

```typescript
// ClientWrapper.tsx
"use client";

export function ClientWrapper({ children }) {
  const [isOpen, setIsOpen] = useState(false);
  
  return (
    <div>
      <button onClick={() => setIsOpen(!isOpen)}>Toggle</button>
      {isOpen && children}
    </div>
  );
}

// page.tsx (Server Component)
export default async function Page() {
  const data = await fetchData();
  
  return (
    <ClientWrapper>
      {/* This remains a Server Component */}
      <ServerDataDisplay data={data} />
    </ClientWrapper>
  );
}
```

### Importing Client Components in Server Components

```typescript
// ✅ Good - Client Component imported in Server Component
import { ClientButton } from './ClientButton';

export default async function ServerPage() {
  const data = await fetchData();
  return (
    <div>
      <h1>{data.title}</h1>
      <ClientButton />
    </div>
  );
}
```

### Importing Server Components in Client Components

```typescript
// ❌ Bad - Can't import Server Component in Client Component
"use client";
import { ServerComponent } from './ServerComponent';

export function ClientComponent() {
  return <ServerComponent />; // Error!
}

// ✅ Good - Pass as children
"use client";
export function ClientComponent({ children }) {
  return <div>{children}</div>;
}

// Usage in Server Component
<ClientComponent>
  <ServerComponent />
</ClientComponent>
```

## Streaming and Suspense

### Streaming Server Components

```typescript
import { Suspense } from 'react';

async function SlowComponent() {
  await new Promise(resolve => setTimeout(resolve, 3000));
  return <div>Slow data loaded</div>;
}

export default function Page() {
  return (
    <div>
      <h1>Page Title</h1>
      <Suspense fallback={<div>Loading...</div>}>
        <SlowComponent />
      </Suspense>
    </div>
  );
}
```

### Multiple Suspense Boundaries

```typescript
export default function Dashboard() {
  return (
    <div>
      <Suspense fallback={<Skeleton />}>
        <UserProfile />
      </Suspense>
      
      <Suspense fallback={<Skeleton />}>
        <RecentActivity />
      </Suspense>
      
      <Suspense fallback={<Skeleton />}>
        <Analytics />
      </Suspense>
    </div>
  );
}
```

## Server Actions

Server Actions allow calling server code from Client Components.

### Defining Server Actions

```typescript
// app/actions.ts
"use server";

import { db } from '@/lib/database';
import { revalidatePath } from 'next/cache';

export async function createUser(formData: FormData) {
  const name = formData.get('name') as string;
  const email = formData.get('email') as string;
  
  await db.user.create({
    data: { name, email }
  });
  
  revalidatePath('/users');
}
```

### Using Server Actions in Client Components

```typescript
"use client";

import { createUser } from '@/app/actions';
import { useFormStatus } from 'react-dom';

function SubmitButton() {
  const { pending } = useFormStatus();
  return (
    <button type="submit" disabled={pending}>
      {pending ? 'Creating...' : 'Create User'}
    </button>
  );
}

export function UserForm() {
  return (
    <form action={createUser}>
      <input name="name" required />
      <input name="email" type="email" required />
      <SubmitButton />
    </form>
  );
}
```

### Server Actions with useTransition

```typescript
"use client";

import { useTransition } from 'react';
import { deletePost } from '@/app/actions';

export function DeleteButton({ postId }) {
  const [isPending, startTransition] = useTransition();
  
  return (
    <button
      onClick={() => startTransition(() => deletePost(postId))}
      disabled={isPending}
    >
      {isPending ? 'Deleting...' : 'Delete'}
    </button>
  );
}
```

## Caching and Revalidation

### Fetch Caching

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
```

### Route Segment Config

```typescript
// app/page.tsx
export const dynamic = 'force-dynamic'; // Disable caching
export const revalidate = 3600; // Revalidate every hour

export default async function Page() {
  const data = await fetchData();
  return <div>{data}</div>;
}
```

### Manual Revalidation

```typescript
import { revalidatePath, revalidateTag } from 'next/cache';

// Revalidate specific path
await revalidatePath('/users');

// Revalidate by tag
await fetch('https://api.example.com/data', {
  next: { tags: ['users'] }
});
await revalidateTag('users');
```

## Data Fetching Patterns

### Deduplication

Next.js automatically deduplicates fetch requests:

```typescript
// Both components fetch same URL - only one request made
async function Header() {
  const user = await fetch('/api/user').then(r => r.json());
  return <div>{user.name}</div>;
}

async function Sidebar() {
  const user = await fetch('/api/user').then(r => r.json());
  return <div>{user.email}</div>;
}
```

### Preloading Data

```typescript
import { preload } from 'react-dom';

export default function Page() {
  preload('/api/data', { as: 'fetch' });
  return <DataComponent />;
}
```

## Error Handling

### Error Boundaries for Server Components

```typescript
// app/error.tsx
"use client";

export default function Error({
  error,
  reset,
}: {
  error: Error;
  reset: () => void;
}) {
  return (
    <div>
      <h2>Something went wrong!</h2>
      <p>{error.message}</p>
      <button onClick={reset}>Try again</button>
    </div>
  );
}
```

### Loading States

```typescript
// app/loading.tsx
export default function Loading() {
  return <div>Loading...</div>;
}
```

## Best Practices

### Keep Client Components Small

```typescript
// ❌ Bad - entire page is client component
"use client";

export default function Page() {
  const [count, setCount] = useState(0);
  return (
    <div>
      <Header />
      <Sidebar />
      <button onClick={() => setCount(count + 1)}>{count}</button>
      <Footer />
    </div>
  );
}

// ✅ Good - only interactive part is client component
export default function Page() {
  return (
    <div>
      <Header />
      <Sidebar />
      <Counter /> {/* Small client component */}
      <Footer />
    </div>
  );
}
```

### Move Client Components Down the Tree

```typescript
// ✅ Good - Client Component as leaf
export default async function Page() {
  const data = await fetchData();
  
  return (
    <div>
      <ServerComponent data={data} />
      <AnotherServerComponent />
      <InteractiveButton /> {/* Client Component */}
    </div>
  );
}
```

### Use Server Actions for Mutations

```typescript
// ✅ Good - Server Action for mutation
"use server";

export async function updateUser(userId: string, data: UserData) {
  await db.user.update({
    where: { id: userId },
    data,
  });
  revalidatePath(`/users/${userId}`);
}

// ❌ Avoid - Client-side API call
"use client";
export function updateUser(userId: string, data: UserData) {
  return fetch(`/api/users/${userId}`, {
    method: 'PUT',
    body: JSON.stringify(data),
  });
}
```
