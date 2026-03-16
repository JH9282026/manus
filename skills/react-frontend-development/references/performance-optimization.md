# React Performance Optimization

Comprehensive guide to identifying and resolving performance bottlenecks in React applications.

---

## Profiling and Measurement

### React DevTools Profiler

1. Open React DevTools
2. Navigate to Profiler tab
3. Click record, interact with app, stop recording
4. Analyze flame graph and ranked chart

**Key Metrics**:
- Commit duration: Time to render and commit changes
- Render count: How many times component rendered
- Self time: Time spent in component itself (excluding children)

### Performance API

```typescript
function measureRender(componentName: string, actualDuration: number) {
  console.log(`${componentName} took ${actualDuration}ms`);
}

<Profiler id="App" onRender={measureRender}>
  <App />
</Profiler>
```

### Chrome DevTools Performance Tab

1. Open DevTools → Performance
2. Record interaction
3. Look for long tasks (>50ms)
4. Identify scripting bottlenecks

## Preventing Unnecessary Re-renders

### React.memo

Memoize functional components:

```typescript
const ExpensiveComponent = React.memo(function ExpensiveComponent({ data }) {
  // Only re-renders if data changes
  return <div>{processData(data)}</div>;
});

// Custom comparison
const MemoizedComponent = React.memo(
  Component,
  (prevProps, nextProps) => {
    return prevProps.id === nextProps.id;
  }
);
```

### useMemo for Expensive Calculations

```typescript
function ProductList({ products, filter }) {
  const filteredProducts = useMemo(() => {
    console.log('Filtering products...');
    return products.filter(p => p.category === filter);
  }, [products, filter]);
  
  return <>{filteredProducts.map(renderProduct)}</>;
}
```

### useCallback for Stable Functions

```typescript
function Parent() {
  const [count, setCount] = useState(0);
  
  // Without useCallback, new function on every render
  const handleClick = useCallback(() => {
    console.log('Clicked');
  }, []);
  
  return <MemoizedChild onClick={handleClick} />;
}
```

### Avoid Inline Objects and Arrays

```typescript
// ❌ Bad - new object every render
<Component style={{ margin: 10 }} />

// ✅ Good - stable reference
const style = { margin: 10 };
<Component style={style} />

// ❌ Bad - new array every render
<List items={[1, 2, 3]} />

// ✅ Good - stable reference
const items = [1, 2, 3];
<List items={items} />
```

## Code Splitting Strategies

### Route-based Splitting

```typescript
const routes = [
  {
    path: '/',
    component: lazy(() => import('./pages/Home')),
  },
  {
    path: '/dashboard',
    component: lazy(() => import('./pages/Dashboard')),
  },
];

function App() {
  return (
    <Suspense fallback={<PageLoader />}>
      <Routes>
        {routes.map(route => (
          <Route key={route.path} {...route} />
        ))}
      </Routes>
    </Suspense>
  );
}
```

### Component-based Splitting

```typescript
// Split heavy components
const Chart = lazy(() => import('./Chart'));
const DataTable = lazy(() => import('./DataTable'));

function Dashboard() {
  return (
    <div>
      <Suspense fallback={<Skeleton />}>
        <Chart data={data} />
      </Suspense>
      <Suspense fallback={<Skeleton />}>
        <DataTable data={data} />
      </Suspense>
    </div>
  );
}
```

### Library Splitting

```typescript
// Split large libraries
const loadMarkdown = () => import('react-markdown');

function MarkdownViewer({ content }) {
  const [Markdown, setMarkdown] = useState(null);
  
  useEffect(() => {
    loadMarkdown().then(mod => setMarkdown(() => mod.default));
  }, []);
  
  if (!Markdown) return <Skeleton />;
  return <Markdown>{content}</Markdown>;
}
```

## Virtualization for Large Lists

### react-window

```typescript
import { FixedSizeList } from 'react-window';

function VirtualList({ items }) {
  const Row = ({ index, style }) => (
    <div style={style}>
      {items[index].name}
    </div>
  );
  
  return (
    <FixedSizeList
      height={600}
      itemCount={items.length}
      itemSize={50}
      width="100%"
    >
      {Row}
    </FixedSizeList>
  );
}
```

### react-virtuoso

```typescript
import { Virtuoso } from 'react-virtuoso';

function InfiniteList({ loadMore }) {
  return (
    <Virtuoso
      data={items}
      endReached={loadMore}
      itemContent={(index, item) => (
        <div>{item.name}</div>
      )}
    />
  );
}
```

## State Management Optimization

### Collocate State

Keep state as close to where it's used as possible:

```typescript
// ❌ Bad - state too high
function App() {
  const [formData, setFormData] = useState({});
  return (
    <div>
      <Header />
      <Form data={formData} onChange={setFormData} />
    </div>
  );
}

// ✅ Good - state colocated
function App() {
  return (
    <div>
      <Header />
      <Form />
    </div>
  );
}

function Form() {
  const [formData, setFormData] = useState({});
  // ...
}
```

### Split Context Providers

```typescript
// ❌ Bad - single context
const AppContext = createContext({ user, theme, settings });

// ✅ Good - split contexts
const UserContext = createContext(user);
const ThemeContext = createContext(theme);
const SettingsContext = createContext(settings);
```

### Use State Management Libraries

For complex state, use optimized libraries:

```typescript
// Zustand - minimal re-renders
import create from 'zustand';

const useStore = create((set) => ({
  count: 0,
  increment: () => set((state) => ({ count: state.count + 1 })),
}));

// Only re-renders when count changes
function Counter() {
  const count = useStore((state) => state.count);
  return <div>{count}</div>;
}
```

## Bundle Size Optimization

### Analyze Bundle

```bash
# Webpack Bundle Analyzer
npm install --save-dev webpack-bundle-analyzer

# Vite
npm run build -- --mode analyze
```

### Tree Shaking

```typescript
// ❌ Bad - imports entire library
import _ from 'lodash';

// ✅ Good - imports only what's needed
import debounce from 'lodash/debounce';

// ✅ Better - use modern alternatives
import { debounce } from 'es-toolkit';
```

### Dynamic Imports

```typescript
// Load heavy libraries on demand
const loadPDF = async () => {
  const { PDFViewer } = await import('react-pdf');
  return PDFViewer;
};
```

## Image Optimization

### Next.js Image Component

```typescript
import Image from 'next/image';

<Image
  src="/photo.jpg"
  alt="Photo"
  width={500}
  height={300}
  loading="lazy"
  placeholder="blur"
/>
```

### Lazy Loading Images

```typescript
function LazyImage({ src, alt }) {
  const imgRef = useRef<HTMLImageElement>(null);
  const isVisible = useIntersectionObserver(imgRef);
  
  return (
    <img
      ref={imgRef}
      src={isVisible ? src : placeholder}
      alt={alt}
    />
  );
}
```

### Modern Image Formats

```typescript
<picture>
  <source srcSet="image.avif" type="image/avif" />
  <source srcSet="image.webp" type="image/webp" />
  <img src="image.jpg" alt="Fallback" />
</picture>
```

## Debouncing and Throttling

### Debounce Input

```typescript
function SearchInput() {
  const [query, setQuery] = useState('');
  const debouncedQuery = useDebounce(query, 300);
  
  useEffect(() => {
    if (debouncedQuery) {
      searchAPI(debouncedQuery);
    }
  }, [debouncedQuery]);
  
  return <input value={query} onChange={e => setQuery(e.target.value)} />;
}
```

### Throttle Scroll

```typescript
function useThrottle<T>(value: T, delay: number): T {
  const [throttledValue, setThrottledValue] = useState(value);
  const lastRan = useRef(Date.now());
  
  useEffect(() => {
    const handler = setTimeout(() => {
      if (Date.now() - lastRan.current >= delay) {
        setThrottledValue(value);
        lastRan.current = Date.now();
      }
    }, delay - (Date.now() - lastRan.current));
    
    return () => clearTimeout(handler);
  }, [value, delay]);
  
  return throttledValue;
}
```

## Web Workers for Heavy Computation

```typescript
// worker.ts
self.addEventListener('message', (e) => {
  const result = heavyComputation(e.data);
  self.postMessage(result);
});

// Component
function HeavyComponent() {
  const [result, setResult] = useState(null);
  
  useEffect(() => {
    const worker = new Worker(new URL('./worker.ts', import.meta.url));
    
    worker.postMessage(data);
    worker.onmessage = (e) => setResult(e.data);
    
    return () => worker.terminate();
  }, [data]);
  
  return <div>{result}</div>;
}
```

## Concurrent Features (React 18+)

### useTransition

Mark updates as non-urgent:

```typescript
function SearchResults() {
  const [query, setQuery] = useState('');
  const [isPending, startTransition] = useTransition();
  
  const handleChange = (e) => {
    setQuery(e.target.value);
    startTransition(() => {
      // Non-urgent update
      setSearchResults(filterResults(e.target.value));
    });
  };
  
  return (
    <>
      <input value={query} onChange={handleChange} />
      {isPending && <Spinner />}
      <Results />
    </>
  );
}
```

### useDeferredValue

Defer updating part of the UI:

```typescript
function App() {
  const [text, setText] = useState('');
  const deferredText = useDeferredValue(text);
  
  return (
    <>
      <input value={text} onChange={e => setText(e.target.value)} />
      <SlowList text={deferredText} />
    </>
  );
}
```

## Performance Checklist

- [ ] Profile with React DevTools before optimizing
- [ ] Use React.memo for expensive pure components
- [ ] Implement code splitting for routes and heavy components
- [ ] Virtualize long lists (>100 items)
- [ ] Optimize images (lazy loading, modern formats, responsive)
- [ ] Debounce/throttle frequent events (scroll, resize, input)
- [ ] Analyze and reduce bundle size
- [ ] Use production builds for deployment
- [ ] Enable gzip/brotli compression
- [ ] Implement proper caching strategies
- [ ] Use CDN for static assets
- [ ] Monitor with Web Vitals (LCP, FID, CLS)
