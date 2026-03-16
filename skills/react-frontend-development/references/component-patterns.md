# React Component Patterns

Advanced component design patterns for building scalable, maintainable React applications.

---

## Compound Components

Components that work together to form a complete UI, sharing implicit state.

### Pattern Implementation

```typescript
const TabsContext = createContext(null);

function Tabs({ children, defaultValue }) {
  const [activeTab, setActiveTab] = useState(defaultValue);
  
  return (
    <TabsContext.Provider value={{ activeTab, setActiveTab }}>
      <div className="tabs">{children}</div>
    </TabsContext.Provider>
  );
}

function TabList({ children }) {
  return <div className="tab-list">{children}</div>;
}

function Tab({ value, children }) {
  const { activeTab, setActiveTab } = useContext(TabsContext);
  const isActive = activeTab === value;
  
  return (
    <button
      className={isActive ? 'active' : ''}
      onClick={() => setActiveTab(value)}
    >
      {children}
    </button>
  );
}

function TabPanel({ value, children }) {
  const { activeTab } = useContext(TabsContext);
  if (activeTab !== value) return null;
  return <div className="tab-panel">{children}</div>;
}

Tabs.List = TabList;
Tabs.Tab = Tab;
Tabs.Panel = TabPanel;

// Usage
<Tabs defaultValue="profile">
  <Tabs.List>
    <Tabs.Tab value="profile">Profile</Tabs.Tab>
    <Tabs.Tab value="settings">Settings</Tabs.Tab>
  </Tabs.List>
  <Tabs.Panel value="profile">Profile content</Tabs.Panel>
  <Tabs.Panel value="settings">Settings content</Tabs.Panel>
</Tabs>
```

## Render Props Pattern

Share code between components using a prop whose value is a function.

```typescript
interface MouseTrackerProps {
  render: (state: { x: number; y: number }) => React.ReactNode;
}

function MouseTracker({ render }: MouseTrackerProps) {
  const [position, setPosition] = useState({ x: 0, y: 0 });
  
  useEffect(() => {
    const handleMove = (e: MouseEvent) => {
      setPosition({ x: e.clientX, y: e.clientY });
    };
    window.addEventListener('mousemove', handleMove);
    return () => window.removeEventListener('mousemove', handleMove);
  }, []);
  
  return <>{render(position)}</>;
}

// Usage
<MouseTracker render={({ x, y }) => (
  <div>Mouse at {x}, {y}</div>
)} />
```

**Note**: Custom hooks are now preferred over render props for logic reuse.

## Higher-Order Components (HOC)

Function that takes a component and returns a new component with additional props or behavior.

```typescript
function withAuth<P extends object>(
  Component: React.ComponentType<P>
) {
  return function AuthenticatedComponent(props: P) {
    const { user, loading } = useAuth();
    
    if (loading) return <Spinner />;
    if (!user) return <Navigate to="/login" />;
    
    return <Component {...props} user={user} />;
  };
}

// Usage
const ProtectedDashboard = withAuth(Dashboard);
```

**Modern Alternative**: Use hooks or wrapper components instead of HOCs.

## Container/Presentational Pattern

Separate data fetching and logic from UI rendering.

### Container Component

```typescript
function UserListContainer() {
  const { data, loading, error } = useQuery('/api/users');
  
  if (loading) return <Spinner />;
  if (error) return <ErrorMessage error={error} />;
  
  return <UserList users={data} />;
}
```

### Presentational Component

```typescript
interface UserListProps {
  users: User[];
}

function UserList({ users }: UserListProps) {
  return (
    <ul>
      {users.map(user => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  );
}
```

## Controlled vs Uncontrolled Components

### Controlled Components

Form data handled by React state:

```typescript
function ControlledInput() {
  const [value, setValue] = useState('');
  
  return (
    <input
      value={value}
      onChange={e => setValue(e.target.value)}
    />
  );
}
```

### Uncontrolled Components

Form data handled by the DOM:

```typescript
function UncontrolledInput() {
  const inputRef = useRef<HTMLInputElement>(null);
  
  const handleSubmit = () => {
    console.log(inputRef.current?.value);
  };
  
  return <input ref={inputRef} />;
}
```

**Recommendation**: Use controlled components for most cases. Use uncontrolled for file inputs or when integrating with non-React code.

## Prop Getter Pattern

Provide props objects that users spread onto elements.

```typescript
function useDropdown() {
  const [isOpen, setIsOpen] = useState(false);
  
  const getToggleProps = () => ({
    onClick: () => setIsOpen(!isOpen),
    'aria-expanded': isOpen,
    'aria-haspopup': true,
  });
  
  const getMenuProps = () => ({
    hidden: !isOpen,
    role: 'menu',
  });
  
  return { isOpen, getToggleProps, getMenuProps };
}

// Usage
function Dropdown() {
  const { isOpen, getToggleProps, getMenuProps } = useDropdown();
  
  return (
    <div>
      <button {...getToggleProps()}>Toggle</button>
      <ul {...getMenuProps()}>
        <li>Item 1</li>
        <li>Item 2</li>
      </ul>
    </div>
  );
}
```

## State Reducer Pattern

Allow users to control internal state changes.

```typescript
type Action = { type: 'increment' } | { type: 'decrement' };

function useCounter(reducer?: (state: number, action: Action) => number) {
  const defaultReducer = (state: number, action: Action) => {
    switch (action.type) {
      case 'increment': return state + 1;
      case 'decrement': return state - 1;
      default: return state;
    }
  };
  
  const [count, dispatch] = useReducer(reducer || defaultReducer, 0);
  
  return {
    count,
    increment: () => dispatch({ type: 'increment' }),
    decrement: () => dispatch({ type: 'decrement' }),
  };
}

// Usage with custom reducer
const customReducer = (state, action) => {
  if (action.type === 'increment' && state >= 10) {
    return state; // Prevent incrementing past 10
  }
  return defaultReducer(state, action);
};

const { count, increment } = useCounter(customReducer);
```

## Polymorphic Components

Components that can render as different HTML elements.

```typescript
type PolymorphicProps<E extends React.ElementType> = {
  as?: E;
  children: React.ReactNode;
} & React.ComponentPropsWithoutRef<E>;

function Box<E extends React.ElementType = 'div'>(
  { as, children, ...props }: PolymorphicProps<E>
) {
  const Component = as || 'div';
  return <Component {...props}>{children}</Component>;
}

// Usage
<Box>Default div</Box>
<Box as="section">Section element</Box>
<Box as="button" onClick={() => {}}>Button element</Box>
```

## Composition Patterns

### Slot Pattern

```typescript
interface CardProps {
  header?: React.ReactNode;
  footer?: React.ReactNode;
  children: React.ReactNode;
}

function Card({ header, footer, children }: CardProps) {
  return (
    <div className="card">
      {header && <div className="card-header">{header}</div>}
      <div className="card-body">{children}</div>
      {footer && <div className="card-footer">{footer}</div>}
    </div>
  );
}

// Usage
<Card
  header={<h2>Title</h2>}
  footer={<button>Action</button>}
>
  Content
</Card>
```

### Children as Function

```typescript
interface DataProviderProps<T> {
  data: T[];
  children: (data: T[]) => React.ReactNode;
}

function DataProvider<T>({ data, children }: DataProviderProps<T>) {
  return <>{children(data)}</>;
}

// Usage
<DataProvider data={users}>
  {(users) => (
    <ul>
      {users.map(user => <li key={user.id}>{user.name}</li>)}
    </ul>
  )}
</DataProvider>
```

## Error Boundaries

Catch JavaScript errors in component tree and display fallback UI.

```typescript
class ErrorBoundary extends React.Component<
  { children: React.ReactNode; fallback: React.ReactNode },
  { hasError: boolean }
> {
  state = { hasError: false };
  
  static getDerivedStateFromError() {
    return { hasError: true };
  }
  
  componentDidCatch(error: Error, errorInfo: React.ErrorInfo) {
    console.error('Error caught:', error, errorInfo);
  }
  
  render() {
    if (this.state.hasError) {
      return this.props.fallback;
    }
    return this.props.children;
  }
}

// Usage
<ErrorBoundary fallback={<ErrorMessage />}>
  <App />
</ErrorBoundary>
```

**Note**: Error boundaries only catch errors in class components. For hooks, use error handling libraries or try/catch in event handlers.

## Lazy Loading Patterns

### Route-based Code Splitting

```typescript
const Home = lazy(() => import('./pages/Home'));
const About = lazy(() => import('./pages/About'));

function App() {
  return (
    <Suspense fallback={<PageLoader />}>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </Suspense>
  );
}
```

### Component-based Code Splitting

```typescript
const HeavyChart = lazy(() => import('./HeavyChart'));

function Dashboard() {
  const [showChart, setShowChart] = useState(false);
  
  return (
    <div>
      <button onClick={() => setShowChart(true)}>Show Chart</button>
      {showChart && (
        <Suspense fallback={<Spinner />}>
          <HeavyChart />
        </Suspense>
      )}
    </div>
  );
}
```

## Forwarding Refs

Pass refs through components to child elements.

```typescript
interface InputProps {
  label: string;
}

const Input = forwardRef<HTMLInputElement, InputProps>(
  ({ label, ...props }, ref) => {
    return (
      <label>
        {label}
        <input ref={ref} {...props} />
      </label>
    );
  }
);

// Usage
function Form() {
  const inputRef = useRef<HTMLInputElement>(null);
  
  useEffect(() => {
    inputRef.current?.focus();
  }, []);
  
  return <Input ref={inputRef} label="Name" />;
}
```

## Portal Pattern

Render children into a DOM node outside the parent hierarchy.

```typescript
function Modal({ isOpen, onClose, children }) {
  if (!isOpen) return null;
  
  return createPortal(
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={e => e.stopPropagation()}>
        {children}
      </div>
    </div>,
    document.getElementById('modal-root')!
  );
}
```
