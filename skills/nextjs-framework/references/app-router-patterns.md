# Next.js App Router Advanced Patterns

Advanced routing patterns, parallel routes, intercepting routes, and route groups.

---

## Parallel Routes

Render multiple pages in the same layout simultaneously.

```
app/
  @analytics/
    page.tsx
  @team/
    page.tsx
  layout.tsx
  page.tsx
```

```typescript
// app/layout.tsx
export default function Layout({
  children,
  analytics,
  team,
}: {
  children: React.ReactNode;
  analytics: React.ReactNode;
  team: React.ReactNode;
}) {
  return (
    <>
      {children}
      {analytics}
      {team}
    </>
  );
}
```

## Intercepting Routes

Intercept routes to show content in a modal while preserving URL.

```
app/
  @modal/
    (.)photo/[id]/
      page.tsx
  photo/[id]/
    page.tsx
```

```typescript
// app/@modal/(.)photo/[id]/page.tsx
export default function PhotoModal({ params }: { params: { id: string } }) {
  return (
    <Modal>
      <Photo id={params.id} />
    </Modal>
  );
}
```

## Route Groups

Organize routes without affecting URL structure.

```
app/
  (marketing)/
    about/page.tsx
    contact/page.tsx
  (shop)/
    products/page.tsx
    cart/page.tsx
```

## Dynamic Route Segments

```typescript
// app/blog/[slug]/page.tsx
export default async function Post({ params }: { params: { slug: string } }) {
  const post = await getPost(params.slug);
  return <article>{post.content}</article>;
}

// Catch-all routes: app/shop/[...slug]/page.tsx
// Optional catch-all: app/shop/[[...slug]]/page.tsx
```
