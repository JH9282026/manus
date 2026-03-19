# Component Libraries

Comprehensive guide to building, maintaining, and scaling component libraries for design systems.

---

## Component Library Fundamentals

### What Makes a Good Component?

**Five qualities of well-designed components:**

1. **Reusable** — Works in multiple contexts without modification
2. **Composable** — Can be combined with other components
3. **Consistent** — Follows system patterns and conventions
4. **Accessible** — Usable by everyone, including people with disabilities
5. **Documented** — Clear usage guidelines and examples

### Component Anatomy

Every component should have:

**1. Structure** — HTML/JSX markup
**2. Styling** — CSS or CSS-in-JS
**3. Behavior** — JavaScript logic and interactivity
**4. Props/API** — Configurable options
**5. Documentation** — Usage guidelines, examples, accessibility notes
**6. Tests** — Unit tests, integration tests, visual regression tests

---

## Building Atomic Components

### Button Component (Example)

**Variants:**
- Primary (high emphasis)
- Secondary (medium emphasis)
- Tertiary (low emphasis)
- Destructive (dangerous actions)
- Ghost (minimal styling)

**States:**
- Default
- Hover
- Active (pressed)
- Focus (keyboard navigation)
- Disabled
- Loading

**Sizes:**
- Small (32px height)
- Medium (40px height, default)
- Large (48px height)

**Props/API:**
```typescript
interface ButtonProps {
  variant?: 'primary' | 'secondary' | 'tertiary' | 'destructive' | 'ghost';
  size?: 'small' | 'medium' | 'large';
  disabled?: boolean;
  loading?: boolean;
  icon?: ReactNode;
  iconPosition?: 'left' | 'right';
  fullWidth?: boolean;
  onClick?: () => void;
  children: ReactNode;
}
```

**Implementation (React example):**
```jsx
import './Button.css';

export function Button({
  variant = 'primary',
  size = 'medium',
  disabled = false,
  loading = false,
  icon,
  iconPosition = 'left',
  fullWidth = false,
  onClick,
  children,
  ...props
}) {
  const classNames = [
    'ds-button',
    `ds-button--${variant}`,
    `ds-button--${size}`,
    fullWidth && 'ds-button--full-width',
    loading && 'ds-button--loading',
  ].filter(Boolean).join(' ');

  return (
    <button
      className={classNames}
      disabled={disabled || loading}
      onClick={onClick}
      {...props}
    >
      {loading && <Spinner size="small" />}
      {!loading && icon && iconPosition === 'left' && icon}
      <span className="ds-button__text">{children}</span>
      {!loading && icon && iconPosition === 'right' && icon}
    </button>
  );
}
```

**CSS (using design tokens):**
```css
.ds-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--spacing-xs);
  font-family: var(--font-family-base);
  font-weight: var(--font-weight-medium);
  border-radius: var(--border-radius-md);
  border: none;
  cursor: pointer;
  transition: all 0.2s ease;
}

.ds-button--primary {
  background-color: var(--color-action-primary);
  color: var(--color-text-inverse);
}

.ds-button--primary:hover:not(:disabled) {
  background-color: var(--color-action-primary-hover);
}

.ds-button--medium {
  height: 40px;
  padding: 0 var(--spacing-md);
  font-size: var(--font-size-body);
}

.ds-button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.ds-button--loading {
  pointer-events: none;
}
```

**Accessibility:**
- Use semantic `<button>` element
- Ensure sufficient color contrast (4.5:1 for text)
- Provide focus indicator (outline or ring)
- Support keyboard navigation (Enter/Space to activate)
- Announce loading state to screen readers (`aria-busy="true"`)
- Disabled buttons not focusable (native `disabled` attribute)

---

## Component Variant Strategies

### Strategy 1: Boolean Props (Simple)

**Use when:** Few, independent variations

```jsx
<Button primary />
<Button secondary />
<Button large />
<Button primary large />
```

**Pros:**
- Simple API
- Easy to understand

**Cons:**
- Can create invalid combinations (`<Button primary secondary />`)
- Doesn't scale to many variants

### Strategy 2: Variant Prop (Recommended)

**Use when:** Mutually exclusive variations

```jsx
<Button variant="primary" />
<Button variant="secondary" />
<Button variant="primary" size="large" />
```

**Pros:**
- Prevents invalid combinations
- Clear, explicit API
- Scales well

**Cons:**
- Slightly more verbose

### Strategy 3: Compound Variants (Advanced)

**Use when:** Variants interact with each other

```jsx
// Different padding for primary vs. secondary at large size
const buttonVariants = {
  base: 'ds-button',
  variants: {
    variant: {
      primary: 'bg-blue text-white',
      secondary: 'bg-gray text-black',
    },
    size: {
      small: 'h-8 px-3 text-sm',
      large: 'h-12 px-6 text-lg',
    },
  },
  compoundVariants: [
    {
      variant: 'primary',
      size: 'large',
      className: 'px-8', // Override padding for primary large
    },
  ],
};
```

**Tools:**
- CVA (Class Variance Authority)
- Stitches
- Tailwind Variants

---

## Composition Patterns

### Pattern 1: Slots (Headless Components)

**Use case:** Flexible content areas

```jsx
<Card
  header={<h3>Title</h3>}
  media={<img src="image.jpg" />}
  content={<p>Description</p>}
  actions={<Button>Action</Button>}
/>
```

**Benefits:**
- Maximum flexibility
- One component, infinite variations

### Pattern 2: Compound Components

**Use case:** Related sub-components with shared state

```jsx
<Tabs defaultValue="tab1">
  <TabList>
    <Tab value="tab1">Tab 1</Tab>
    <Tab value="tab2">Tab 2</Tab>
  </TabList>
  <TabPanel value="tab1">Content 1</TabPanel>
  <TabPanel value="tab2">Content 2</TabPanel>
</Tabs>
```

**Benefits:**
- Semantic, clear structure
- Shared state managed internally
- Flexible composition

### Pattern 3: Render Props

**Use case:** Custom rendering logic

```jsx
<Dropdown
  trigger={(open) => (
    <Button>
      Menu {open ? '▲' : '▼'}
    </Button>
  )}
>
  <MenuItem>Option 1</MenuItem>
  <MenuItem>Option 2</MenuItem>
</Dropdown>
```

**Benefits:**
- Full control over rendering
- Access to internal state

**Cons:**
- More complex API
- Harder for beginners

### Pattern 4: Polymorphic Components

**Use case:** Component that can render as different HTML elements

```jsx
<Button as="a" href="/link">Link Button</Button>
<Button as="button" type="submit">Submit Button</Button>
```

**Implementation:**
```typescript
interface ButtonProps<T extends React.ElementType = 'button'> {
  as?: T;
  // ... other props
}

function Button<T extends React.ElementType = 'button'>({
  as,
  ...props
}: ButtonProps<T>) {
  const Component = as || 'button';
  return <Component {...props} />;
}
```

**Benefits:**
- Semantic HTML
- Reuse styling across different elements

---

## Component Documentation

### Documentation Template

For each component, document:

**1. Overview**
- What is this component?
- When should it be used?

**2. Variants**
- Visual examples of all variants
- When to use each variant

**3. Props/API**
- Table of all props with types, defaults, descriptions

**4. Usage Examples**
- Code examples for common use cases

**5. Accessibility**
- Keyboard navigation
- Screen reader behavior
- ARIA attributes
- Color contrast requirements

**6. Do's and Don'ts**
- Visual examples of correct and incorrect usage

**7. Related Components**
- Links to similar or complementary components

### Example: Button Documentation

**Overview**

Buttons trigger actions or navigate to new pages. Use buttons for actions ("Save," "Delete") and links for navigation ("Learn more," "View details").

**Variants**

- **Primary** — High-emphasis actions ("Save," "Submit," "Buy Now")
- **Secondary** — Medium-emphasis actions ("Cancel," "Back")
- **Tertiary** — Low-emphasis actions ("Skip," "Learn More")
- **Destructive** — Dangerous actions ("Delete," "Remove")

**Props**

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `variant` | `'primary' \| 'secondary' \| 'tertiary' \| 'destructive'` | `'primary'` | Visual style of button |
| `size` | `'small' \| 'medium' \| 'large'` | `'medium'` | Size of button |
| `disabled` | `boolean` | `false` | Whether button is disabled |
| `loading` | `boolean` | `false` | Whether button is in loading state |
| `icon` | `ReactNode` | - | Icon to display |
| `iconPosition` | `'left' \| 'right'` | `'left'` | Position of icon |
| `fullWidth` | `boolean` | `false` | Whether button takes full width of container |
| `onClick` | `() => void` | - | Click handler |

**Usage Examples**

```jsx
// Primary button
<Button variant="primary">Save Changes</Button>

// Secondary button with icon
<Button variant="secondary" icon={<ArrowLeft />}>
  Back
</Button>

// Loading state
<Button loading>Saving...</Button>

// Destructive action
<Button variant="destructive">Delete Account</Button>
```

**Accessibility**

- Buttons are keyboard accessible (Tab to focus, Enter/Space to activate)
- Focus indicator visible (blue ring)
- Disabled buttons not focusable
- Loading state announced to screen readers (`aria-busy="true"`)
- Ensure button text is descriptive ("Save" not "Click here")

**Do's and Don'ts**

✅ **Do:**
- Use primary button for main action on page
- Use descriptive button text ("Save Changes" not "Submit")
- Provide loading state for async actions

❌ **Don't:**
- Use multiple primary buttons on same page (creates confusion)
- Use button for navigation (use link instead)
- Disable button without explanation (show error message instead)

---

## Component Testing

### Unit Tests

Test component logic and behavior:

```javascript
import { render, screen, fireEvent } from '@testing-library/react';
import { Button } from './Button';

test('renders button with text', () => {
  render(<Button>Click me</Button>);
  expect(screen.getByText('Click me')).toBeInTheDocument();
});

test('calls onClick when clicked', () => {
  const handleClick = jest.fn();
  render(<Button onClick={handleClick}>Click me</Button>);
  fireEvent.click(screen.getByText('Click me'));
  expect(handleClick).toHaveBeenCalledTimes(1);
});

test('does not call onClick when disabled', () => {
  const handleClick = jest.fn();
  render(<Button disabled onClick={handleClick}>Click me</Button>);
  fireEvent.click(screen.getByText('Click me'));
  expect(handleClick).not.toHaveBeenCalled();
});

test('shows loading spinner when loading', () => {
  render(<Button loading>Click me</Button>);
  expect(screen.getByRole('status')).toBeInTheDocument(); // Spinner has role="status"
});
```

### Visual Regression Tests

Detect unintended visual changes:

**Tools:**
- Chromatic (Storybook integration)
- Percy
- BackstopJS

**Process:**
1. Take screenshot of component in various states
2. Store as baseline
3. On every code change, take new screenshot
4. Compare to baseline
5. Flag differences for review

**Storybook + Chromatic example:**

```javascript
// Button.stories.jsx
export default {
  title: 'Components/Button',
  component: Button,
};

export const Primary = () => <Button variant="primary">Primary</Button>;
export const Secondary = () => <Button variant="secondary">Secondary</Button>;
export const Disabled = () => <Button disabled>Disabled</Button>;
export const Loading = () => <Button loading>Loading</Button>;
```

Chromatic automatically screenshots each story and compares to baseline.

### Accessibility Tests

Ensure components are accessible:

**Automated testing:**

```javascript
import { render } from '@testing-library/react';
import { axe, toHaveNoViolations } from 'jest-axe';
import { Button } from './Button';

expect.extend(toHaveNoViolations);

test('button has no accessibility violations', async () => {
  const { container } = render(<Button>Click me</Button>);
  const results = await axe(container);
  expect(results).toHaveNoViolations();
});
```

**Manual testing:**
- Keyboard navigation (Tab, Enter, Space)
- Screen reader testing (NVDA, VoiceOver)
- Color contrast checking (WebAIM Contrast Checker)
- Zoom testing (200% zoom, verify no loss of functionality)

---

## Component Maintenance

### Versioning Components

**Semantic versioning for component library:**

- **MAJOR (1.0.0 → 2.0.0)** — Breaking changes
  - Removed props
  - Changed prop types
  - Changed component behavior
  - Renamed components

- **MINOR (1.0.0 → 1.1.0)** — New features (backward compatible)
  - New props
  - New variants
  - New components

- **PATCH (1.0.0 → 1.0.1)** — Bug fixes
  - Fix styling issues
  - Fix accessibility issues
  - Fix behavior bugs

**Changelog example:**

```markdown
# Changelog

## [2.0.0] - 2026-03-15

### Breaking Changes
- **Button:** Removed `type` prop (use `variant` instead)
- **Card:** Renamed `image` prop to `media`

### Migration Guide
```jsx
// Before
<Button type="primary">Click</Button>

// After
<Button variant="primary">Click</Button>
```

## [1.5.0] - 2026-03-01

### Added
- **Button:** New `loading` prop for async actions
- **Modal:** New `size` prop (small, medium, large)

### Fixed
- **Input:** Fixed focus ring not visible in dark mode
```

### Deprecation Strategy

**Process:**

1. **Announce deprecation** (in changelog, documentation, console warnings)
2. **Provide migration path** (clear instructions on how to update)
3. **Grace period** (1-2 major versions)
4. **Remove** (in next major version)

**Code example:**

```javascript
// Button.jsx
export function Button({ type, variant, ...props }) {
  // Deprecation warning
  if (type) {
    console.warn(
      'Button: `type` prop is deprecated and will be removed in v3.0. Use `variant` instead.'
    );
  }

  // Support both old and new props during transition
  const actualVariant = variant || type || 'primary';

  return <button className={`button--${actualVariant}`} {...props} />;
}
```

### Performance Monitoring

**Metrics to track:**

- **Bundle size** — Total size of component library
- **Component size** — Size of individual components
- **Render performance** — Time to render components
- **Accessibility score** — Automated accessibility audit results

**Tools:**
- Bundlephobia (bundle size analysis)
- Lighthouse (performance and accessibility)
- React DevTools Profiler (render performance)
- Chromatic (visual regression and accessibility)

**Alerts:**
- Bundle size increases >10% (investigate before merging)
- Accessibility score drops (fix before release)
- Render time increases significantly (optimize)

---

## Advanced Component Patterns

### Controlled vs. Uncontrolled Components

**Uncontrolled (component manages own state):**

```jsx
function UncontrolledInput() {
  const [value, setValue] = useState('');
  return <input value={value} onChange={(e) => setValue(e.target.value)} />;
}

// Usage
<UncontrolledInput />
```

**Controlled (parent manages state):**

```jsx
function ControlledInput({ value, onChange }) {
  return <input value={value} onChange={onChange} />;
}

// Usage
function Parent() {
  const [value, setValue] = useState('');
  return <ControlledInput value={value} onChange={(e) => setValue(e.target.value)} />;
}
```

**Hybrid (support both):**

```jsx
function Input({ value: controlledValue, onChange, defaultValue }) {
  const [internalValue, setInternalValue] = useState(defaultValue || '');
  const isControlled = controlledValue !== undefined;
  const value = isControlled ? controlledValue : internalValue;

  const handleChange = (e) => {
    if (!isControlled) {
      setInternalValue(e.target.value);
    }
    onChange?.(e);
  };

  return <input value={value} onChange={handleChange} />;
}

// Usage (controlled)
<Input value={value} onChange={setValue} />

// Usage (uncontrolled)
<Input defaultValue="initial" />
```

**Recommendation:** Support both patterns for flexibility.

### Forwarding Refs

Allow parent components to access child component's DOM node:

```jsx
import { forwardRef } from 'react';

const Input = forwardRef(function Input(props, ref) {
  return <input ref={ref} {...props} />;
});

// Usage
function Parent() {
  const inputRef = useRef();

  const focusInput = () => {
    inputRef.current.focus();
  };

  return (
    <>
      <Input ref={inputRef} />
      <Button onClick={focusInput}>Focus Input</Button>
    </>
  );
}
```

**When to use:**
- Parent needs to focus element
- Parent needs to measure element size
- Parent needs to trigger animations

### Context for Shared State

Share state between related components without prop drilling:

```jsx
const TabsContext = createContext();

function Tabs({ defaultValue, children }) {
  const [activeTab, setActiveTab] = useState(defaultValue);

  return (
    <TabsContext.Provider value={{ activeTab, setActiveTab }}>
      {children}
    </TabsContext.Provider>
  );
}

function Tab({ value, children }) {
  const { activeTab, setActiveTab } = useContext(TabsContext);
  const isActive = activeTab === value;

  return (
    <button
      className={isActive ? 'tab--active' : 'tab'}
      onClick={() => setActiveTab(value)}
    >
      {children}
    </button>
  );
}

function TabPanel({ value, children }) {
  const { activeTab } = useContext(TabsContext);
  if (activeTab !== value) return null;
  return <div>{children}</div>;
}

// Usage
<Tabs defaultValue="tab1">
  <Tab value="tab1">Tab 1</Tab>
  <Tab value="tab2">Tab 2</Tab>
  <TabPanel value="tab1">Content 1</TabPanel>
  <TabPanel value="tab2">Content 2</TabPanel>
</Tabs>
```

**Benefits:**
- No prop drilling
- Clean API
- Shared state managed in one place

---

Building a component library is an iterative process. Start with atomic components, gather feedback, and expand based on real needs. Prioritize quality over quantity — a small library of excellent components is better than a large library of mediocre ones.
