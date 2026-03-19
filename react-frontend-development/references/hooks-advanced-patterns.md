# Advanced React Hooks Patterns

Deep dive into sophisticated hooks usage, custom hook design, and advanced state management patterns.

---

## Custom Hooks Design Principles

### Naming Conventions

All custom hooks must start with `use` to enable React's rules enforcement:

```typescript
// ✅ Good
function useLocalStorage(key: string) { ... }
function useDebounce(value: string, delay: number) { ... }

// ❌ Bad
function getLocalStorage(key: string) { ... }
function debounce(value: string) { ... }
```

### Composing Hooks

Build complex hooks from simpler ones:

```typescript
function useAuth() {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  
  useEffect(() => {
    const unsubscribe = auth.onAuthStateChanged(user => {
      setUser(user);
      setLoading(false);
    });
    return unsubscribe;
  }, []);
  
  return { user, loading };
}

function useProtectedRoute() {
  const { user, loading } = useAuth();
  const navigate = useNavigate();
  
  useEffect(() => {
    if (!loading && !user) {
      navigate('/login');
    }
  }, [user, loading, navigate]);
  
  return { user, loading };
}
```

### Return Value Patterns

**Array Destructuring** (like useState):
```typescript
function useToggle(initial = false): [boolean, () => void] {
  const [value, setValue] = useState(initial);
  const toggle = useCallback(() => setValue(v => !v), []);
  return [value, toggle];
}

const [isOpen, toggleOpen] = useToggle();
```

**Object Destructuring** (more descriptive):
```typescript
function useApi<T>(url: string) {
  const [data, setData] = useState<T | null>(null);
  const [error, setError] = useState<Error | null>(null);
  const [loading, setLoading] = useState(false);
  
  const refetch = useCallback(() => { ... }, [url]);
  
  return { data, error, loading, refetch };
}

const { data, loading, refetch } = useApi('/users');
```

## Advanced useEffect Patterns

### Cleanup Functions

Always clean up side effects to prevent memory leaks:

```typescript
function useWebSocket(url: string) {
  const [messages, setMessages] = useState([]);
  
  useEffect(() => {
    const ws = new WebSocket(url);
    
    ws.onmessage = (event) => {
      setMessages(prev => [...prev, event.data]);
    };
    
    // Cleanup on unmount or URL change
    return () => {
      ws.close();
    };
  }, [url]);
  
  return messages;
}
```

### Async Effects

Handle async operations properly:

```typescript
function useAsyncData(id: string) {
  const [data, setData] = useState(null);
  
  useEffect(() => {
    let cancelled = false;
    
    async function fetchData() {
      const result = await api.get(id);
      if (!cancelled) {
        setData(result);
      }
    }
    
    fetchData();
    
    return () => {
      cancelled = true;
    };
  }, [id]);
  
  return data;
}
```

### Dependency Array Best Practices

**Include all dependencies**:
```typescript
// ❌ Missing dependency
useEffect(() => {
  console.log(userId);
}, []); // userId should be in deps

// ✅ Correct
useEffect(() => {
  console.log(userId);
}, [userId]);
```

**Use functional updates to reduce dependencies**:
```typescript
// ❌ Unnecessary dependency
useEffect(() => {
  setCount(count + 1);
}, [count]);

// ✅ Better
useEffect(() => {
  setCount(c => c + 1);
}, []);
```

## useReducer for Complex State

### When to Use useReducer

- Multiple related state values
- Complex state transitions
- State updates depend on previous state
- Need to pass dispatch down instead of callbacks

### Pattern: State Machine

```typescript
type State = 
  | { status: 'idle' }
  | { status: 'loading' }
  | { status: 'success'; data: any }
  | { status: 'error'; error: Error };

type Action =
  | { type: 'FETCH_START' }
  | { type: 'FETCH_SUCCESS'; payload: any }
  | { type: 'FETCH_ERROR'; error: Error }
  | { type: 'RESET' };

function reducer(state: State, action: Action): State {
  switch (action.type) {
    case 'FETCH_START':
      return { status: 'loading' };
    case 'FETCH_SUCCESS':
      return { status: 'success', data: action.payload };
    case 'FETCH_ERROR':
      return { status: 'error', error: action.error };
    case 'RESET':
      return { status: 'idle' };
    default:
      return state;
  }
}

function useDataFetch(url: string) {
  const [state, dispatch] = useReducer(reducer, { status: 'idle' });
  
  useEffect(() => {
    dispatch({ type: 'FETCH_START' });
    fetch(url)
      .then(res => res.json())
      .then(data => dispatch({ type: 'FETCH_SUCCESS', payload: data }))
      .catch(error => dispatch({ type: 'FETCH_ERROR', error }));
  }, [url]);
  
  return state;
}
```

## useContext Optimization

### Split Contexts to Prevent Re-renders

```typescript
// ❌ Single context causes all consumers to re-render
const AppContext = createContext({ user, theme, settings });

// ✅ Split into separate contexts
const UserContext = createContext(user);
const ThemeContext = createContext(theme);
const SettingsContext = createContext(settings);
```

### Context with useReducer Pattern

```typescript
const StateContext = createContext(null);
const DispatchContext = createContext(null);

function AppProvider({ children }) {
  const [state, dispatch] = useReducer(reducer, initialState);
  
  return (
    <StateContext.Provider value={state}>
      <DispatchContext.Provider value={dispatch}>
        {children}
      </DispatchContext.Provider>
    </StateContext.Provider>
  );
}

// Consumers only re-render when they need to
function useAppState() {
  return useContext(StateContext);
}

function useAppDispatch() {
  return useContext(DispatchContext);
}
```

## useMemo and useCallback Deep Dive

### When to Use useMemo

**Expensive calculations**:
```typescript
const sortedAndFilteredItems = useMemo(() => {
  return items
    .filter(item => item.category === category)
    .sort((a, b) => a.price - b.price);
}, [items, category]);
```

**Referential equality for dependencies**:
```typescript
const config = useMemo(() => ({
  apiKey: key,
  endpoint: url
}), [key, url]);

useEffect(() => {
  // Won't re-run unless config actually changes
  initializeApi(config);
}, [config]);
```

### When to Use useCallback

**Passing callbacks to memoized children**:
```typescript
const MemoizedChild = React.memo(Child);

function Parent() {
  const handleClick = useCallback(() => {
    doSomething();
  }, []);
  
  return <MemoizedChild onClick={handleClick} />;
}
```

**Callbacks in dependency arrays**:
```typescript
const fetchData = useCallback(() => {
  return api.get(url);
}, [url]);

useEffect(() => {
  fetchData().then(setData);
}, [fetchData]);
```

### React Compiler Considerations

With React Compiler (v1.0+), manual memoization is often unnecessary:

```typescript
// Before React Compiler
const value = useMemo(() => expensiveCalc(a, b), [a, b]);

// With React Compiler - automatically optimized
const value = expensiveCalc(a, b);
```

Only use manual memoization when:
- Profiling shows actual performance issues
- Working with very large datasets
- Preventing expensive child re-renders

## useRef Advanced Patterns

### Storing Previous Values

```typescript
function usePrevious<T>(value: T): T | undefined {
  const ref = useRef<T>();
  
  useEffect(() => {
    ref.current = value;
  }, [value]);
  
  return ref.current;
}

function Component({ count }) {
  const prevCount = usePrevious(count);
  
  return <div>Now: {count}, Before: {prevCount}</div>;
}
```

### Tracking Component Mount State

```typescript
function useIsMounted() {
  const isMounted = useRef(false);
  
  useEffect(() => {
    isMounted.current = true;
    return () => {
      isMounted.current = false;
    };
  }, []);
  
  return isMounted;
}

function Component() {
  const isMounted = useIsMounted();
  
  const fetchData = async () => {
    const data = await api.get('/data');
    if (isMounted.current) {
      setData(data);
    }
  };
}
```

### Stable Callback Refs

```typescript
function useEventCallback<T extends (...args: any[]) => any>(fn: T): T {
  const ref = useRef(fn);
  
  useEffect(() => {
    ref.current = fn;
  });
  
  return useCallback((...args) => ref.current(...args), []) as T;
}
```

## Custom Hooks Library

### useDebounce

```typescript
function useDebounce<T>(value: T, delay: number): T {
  const [debouncedValue, setDebouncedValue] = useState(value);
  
  useEffect(() => {
    const handler = setTimeout(() => {
      setDebouncedValue(value);
    }, delay);
    
    return () => clearTimeout(handler);
  }, [value, delay]);
  
  return debouncedValue;
}
```

### useLocalStorage

```typescript
function useLocalStorage<T>(key: string, initialValue: T) {
  const [storedValue, setStoredValue] = useState<T>(() => {
    try {
      const item = window.localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch (error) {
      return initialValue;
    }
  });
  
  const setValue = (value: T | ((val: T) => T)) => {
    try {
      const valueToStore = value instanceof Function ? value(storedValue) : value;
      setStoredValue(valueToStore);
      window.localStorage.setItem(key, JSON.stringify(valueToStore));
    } catch (error) {
      console.error(error);
    }
  };
  
  return [storedValue, setValue] as const;
}
```

### useMediaQuery

```typescript
function useMediaQuery(query: string): boolean {
  const [matches, setMatches] = useState(() => 
    window.matchMedia(query).matches
  );
  
  useEffect(() => {
    const mediaQuery = window.matchMedia(query);
    const handler = (e: MediaQueryListEvent) => setMatches(e.matches);
    
    mediaQuery.addEventListener('change', handler);
    return () => mediaQuery.removeEventListener('change', handler);
  }, [query]);
  
  return matches;
}
```

### useIntersectionObserver

```typescript
function useIntersectionObserver(
  ref: RefObject<Element>,
  options?: IntersectionObserverInit
) {
  const [isIntersecting, setIsIntersecting] = useState(false);
  
  useEffect(() => {
    const element = ref.current;
    if (!element) return;
    
    const observer = new IntersectionObserver(
      ([entry]) => setIsIntersecting(entry.isIntersecting),
      options
    );
    
    observer.observe(element);
    return () => observer.disconnect();
  }, [ref, options]);
  
  return isIntersecting;
}
```

## Hooks Testing Strategies

### Testing Custom Hooks

```typescript
import { renderHook, act } from '@testing-library/react';

test('useCounter increments', () => {
  const { result } = renderHook(() => useCounter());
  
  expect(result.current.count).toBe(0);
  
  act(() => {
    result.current.increment();
  });
  
  expect(result.current.count).toBe(1);
});
```

### Testing Hooks with Context

```typescript
const wrapper = ({ children }) => (
  <ThemeProvider>{children}</ThemeProvider>
);

const { result } = renderHook(() => useTheme(), { wrapper });
```
