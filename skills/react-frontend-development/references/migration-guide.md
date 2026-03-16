# React Migration Guide

Strategies for upgrading React applications, migrating from legacy patterns, and adopting new features.

---

## Migrating from Class Components to Hooks

### Class Component Pattern

```typescript
class UserProfile extends React.Component<Props, State> {
  state = {
    user: null,
    loading: true,
  };
  
  componentDidMount() {
    this.fetchUser();
  }
  
  componentDidUpdate(prevProps: Props) {
    if (prevProps.userId !== this.props.userId) {
      this.fetchUser();
    }
  }
  
  componentWillUnmount() {
    this.cancelRequest();
  }
  
  fetchUser = async () => {
    const user = await api.getUser(this.props.userId);
    this.setState({ user, loading: false });
  };
  
  render() {
    const { user, loading } = this.state;
    if (loading) return <Spinner />;
    return <div>{user.name}</div>;
  }
}
```

### Equivalent Functional Component

```typescript
function UserProfile({ userId }: Props) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  
  useEffect(() => {
    let cancelled = false;
    
    async function fetchUser() {
      const user = await api.getUser(userId);
      if (!cancelled) {
        setUser(user);
        setLoading(false);
      }
    }
    
    fetchUser();
    
    return () => {
      cancelled = true;
    };
  }, [userId]);
  
  if (loading) return <Spinner />;
  return <div>{user.name}</div>;
}
```

### Lifecycle Method Equivalents

| Class Component | Hooks Equivalent |
|----------------|------------------|
| `constructor` | `useState` initialization |
| `componentDidMount` | `useEffect(() => {}, [])` |
| `componentDidUpdate` | `useEffect(() => {}, [deps])` |
| `componentWillUnmount` | `useEffect` cleanup function |
| `shouldComponentUpdate` | `React.memo` |
| `getDerivedStateFromProps` | `useState` + `useEffect` |
| `getSnapshotBeforeUpdate` | No direct equivalent |
| `componentDidCatch` | No hooks equivalent (use Error Boundary) |

## Migrating from Create React App to Vite

### Why Migrate?

- **Faster dev server**: Vite uses native ESM, no bundling in dev
- **Faster builds**: esbuild is 10-100x faster than webpack
- **Better DX**: Instant HMR, better error messages
- **Modern**: Built for modern browsers, better tree-shaking

### Migration Steps

**1. Install Vite and dependencies**:

```bash
npm install -D vite @vitejs/plugin-react
```

**2. Create `vite.config.ts`**:

```typescript
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
  },
  resolve: {
    alias: {
      '@': '/src',
    },
  },
});
```

**3. Move `index.html` to root**:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>My App</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>
```

**4. Update `package.json` scripts**:

```json
{
  "scripts": {
    "dev": "vite",
    "build": "tsc && vite build",
    "preview": "vite preview"
  }
}
```

**5. Update environment variables**:

```typescript
// CRA
process.env.REACT_APP_API_URL

// Vite
import.meta.env.VITE_API_URL
```

**6. Update imports**:

```typescript
// CRA - no extension needed
import Component from './Component';

// Vite - explicit extensions
import Component from './Component.tsx';
```

**7. Remove CRA dependencies**:

```bash
npm uninstall react-scripts
rm -rf public/index.html
```

## Migrating to React 18

### Update Root Rendering

```typescript
// React 17
import ReactDOM from 'react-dom';
ReactDOM.render(<App />, document.getElementById('root'));

// React 18
import { createRoot } from 'react-dom/client';
const root = createRoot(document.getElementById('root')!);
root.render(<App />);
```

### Adopt Concurrent Features

**useTransition**:

```typescript
function SearchResults() {
  const [query, setQuery] = useState('');
  const [isPending, startTransition] = useTransition();
  
  const handleChange = (e) => {
    setQuery(e.target.value);
    startTransition(() => {
      setResults(filterResults(e.target.value));
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

**useDeferredValue**:

```typescript
function App() {
  const [text, setText] = useState('');
  const deferredText = useDeferredValue(text);
  
  return (
    <>
      <input value={text} onChange={e => setText(e.target.value)} />
      <SlowList text={deferredValue} />
    </>
  );
}
```

### Automatic Batching

React 18 automatically batches all state updates:

```typescript
// React 17 - two renders
setCount(c => c + 1);
setFlag(f => !f);

// React 18 - one render (automatic batching)
setCount(c => c + 1);
setFlag(f => !f);
```

Opt out if needed:

```typescript
import { flushSync } from 'react-dom';

flushSync(() => {
  setCount(c => c + 1);
});
// DOM updated
flushSync(() => {
  setFlag(f => !f);
});
// DOM updated again
```

## Migrating to Next.js App Router

### Pages Router vs App Router

| Feature | Pages Router | App Router |
|---------|-------------|------------|
| File location | `pages/` | `app/` |
| Routing | File-based | Folder-based |
| Data fetching | `getServerSideProps`, `getStaticProps` | `async` components, `fetch` |
| Layouts | `_app.tsx` | `layout.tsx` |
| Loading states | Custom | `loading.tsx` |
| Error handling | `_error.tsx` | `error.tsx` |
| Default | Client Components | Server Components |

### Incremental Migration

Both routers can coexist:

```
app/
  layout.tsx
  page.tsx
  dashboard/
    page.tsx
pages/
  api/
    users.ts
  legacy-page.tsx
```

### Converting Pages to App Router

**Pages Router**:

```typescript
// pages/users/[id].tsx
import { GetServerSideProps } from 'next';

export const getServerSideProps: GetServerSideProps = async ({ params }) => {
  const user = await getUser(params.id);
  return { props: { user } };
};

export default function UserPage({ user }) {
  return <div>{user.name}</div>;
}
```

**App Router**:

```typescript
// app/users/[id]/page.tsx
interface PageProps {
  params: { id: string };
}

export default async function UserPage({ params }: PageProps) {
  const user = await getUser(params.id);
  return <div>{user.name}</div>;
}
```

### Data Fetching Migration

**getServerSideProps → Server Component**:

```typescript
// Before
export const getServerSideProps = async () => {
  const data = await fetchData();
  return { props: { data } };
};

// After
export default async function Page() {
  const data = await fetchData();
  return <div>{data}</div>;
}
```

**getStaticProps → fetch with cache**:

```typescript
// Before
export const getStaticProps = async () => {
  const data = await fetchData();
  return { props: { data }, revalidate: 60 };
};

// After
export default async function Page() {
  const data = await fetch('...', { next: { revalidate: 60 } });
  return <div>{data}</div>;
}
```

**API Routes → Route Handlers**:

```typescript
// pages/api/users.ts
export default function handler(req, res) {
  if (req.method === 'GET') {
    res.json({ users: [] });
  }
}

// app/api/users/route.ts
export async function GET() {
  return Response.json({ users: [] });
}
```

## Migrating State Management

### Redux to Zustand

**Redux**:

```typescript
// store.ts
const counterSlice = createSlice({
  name: 'counter',
  initialState: { value: 0 },
  reducers: {
    increment: state => { state.value += 1; },
  },
});

// Component
const count = useSelector(state => state.counter.value);
const dispatch = useDispatch();
dispatch(increment());
```

**Zustand**:

```typescript
// store.ts
import create from 'zustand';

const useStore = create((set) => ({
  count: 0,
  increment: () => set((state) => ({ count: state.count + 1 })),
}));

// Component
const count = useStore((state) => state.count);
const increment = useStore((state) => state.increment);
increment();
```

### Context to Jotai

**Context**:

```typescript
const CountContext = createContext(0);

function Provider({ children }) {
  const [count, setCount] = useState(0);
  return (
    <CountContext.Provider value={{ count, setCount }}>
      {children}
    </CountContext.Provider>
  );
}

const { count, setCount } = useContext(CountContext);
```

**Jotai**:

```typescript
import { atom, useAtom } from 'jotai';

const countAtom = atom(0);

// Component
const [count, setCount] = useAtom(countAtom);
```

## TypeScript Migration

### Adding TypeScript to Existing Project

**1. Install TypeScript**:

```bash
npm install -D typescript @types/react @types/react-dom
```

**2. Create `tsconfig.json`**:

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "jsx": "react-jsx",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true
  },
  "include": ["src"]
}
```

**3. Rename files**:

```bash
# Rename .js to .tsx (components)
mv src/App.js src/App.tsx

# Rename .js to .ts (utilities)
mv src/utils.js src/utils.ts
```

**4. Add types incrementally**:

```typescript
// Start with any
function Component(props: any) { ... }

// Add proper types
interface Props {
  name: string;
  age: number;
}

function Component({ name, age }: Props) { ... }
```

## Performance Migration

### Lazy Loading

```typescript
// Before - all imported upfront
import Dashboard from './Dashboard';
import Settings from './Settings';

// After - lazy loaded
const Dashboard = lazy(() => import('./Dashboard'));
const Settings = lazy(() => import('./Settings'));

<Suspense fallback={<Loading />}>
  <Dashboard />
</Suspense>
```

### Code Splitting

```typescript
// Before - large bundle
import { HeavyLibrary } from 'heavy-library';

// After - dynamic import
const loadLibrary = async () => {
  const { HeavyLibrary } = await import('heavy-library');
  return HeavyLibrary;
};
```

## Common Migration Pitfalls

### Stale Closures

```typescript
// ❌ Problem
function Component() {
  const [count, setCount] = useState(0);
  
  useEffect(() => {
    const interval = setInterval(() => {
      setCount(count + 1); // Stale closure
    }, 1000);
    return () => clearInterval(interval);
  }, []);
}

// ✅ Solution
function Component() {
  const [count, setCount] = useState(0);
  
  useEffect(() => {
    const interval = setInterval(() => {
      setCount(c => c + 1); // Functional update
    }, 1000);
    return () => clearInterval(interval);
  }, []);
}
```

### Missing Dependencies

```typescript
// ❌ Problem
useEffect(() => {
  fetchData(userId);
}, []); // Missing userId dependency

// ✅ Solution
useEffect(() => {
  fetchData(userId);
}, [userId]);
```

### Infinite Loops

```typescript
// ❌ Problem
useEffect(() => {
  setData(processData(data));
}, [data]); // Infinite loop

// ✅ Solution
const processedData = useMemo(() => processData(data), [data]);
```
