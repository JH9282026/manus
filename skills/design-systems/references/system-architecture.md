# Design System Architecture

Comprehensive guide to planning, structuring, and implementing scalable design system architectures.

---

## Architecture Planning

### Pre-Architecture Assessment

Before building a design system, assess your organization's needs:

**Questions to answer:**

1. **Scale** — How many products? How many teams?
   - 1-2 products, 1 team → Simple component library may suffice
   - 3-10 products, 2-5 teams → Full design system recommended
   - 10+ products, 5+ teams → Enterprise design system with governance

2. **Consistency needs** — How important is visual consistency?
   - Consumer brand → Very high (brand recognition)
   - Enterprise B2B → High (professional appearance)
   - Internal tools → Medium (usability over aesthetics)

3. **Platform diversity** — Web only, or web + mobile + desktop?
   - Web only → Simpler token distribution
   - Multi-platform → Need platform-specific token exports

4. **Brand complexity** — Single brand or multi-brand?
   - Single brand → Standard token structure
   - Multi-brand → Multi-mode token architecture required

5. **Team structure** — Centralized or distributed?
   - Centralized → Top-down governance works
   - Distributed → Need federated or hybrid governance

6. **Technical maturity** — Component-based framework or legacy code?
   - Modern (React, Vue, Angular) → Code components feasible
   - Legacy (jQuery, vanilla JS) → Focus on design components and CSS

### Architecture Decision Framework

**Decision: Monorepo vs. Multi-repo**

| Approach | Pros | Cons | Best For |
|----------|------|------|----------|
| **Monorepo** | Single source of truth, easier versioning, atomic changes | Larger repository, requires monorepo tooling | Teams using same tech stack |
| **Multi-repo** | Independent versioning, smaller repos, tech-agnostic | Harder to sync changes, version management complex | Multi-platform, different tech stacks |

**Recommendation:** Monorepo for web-only or single-platform; multi-repo for web + iOS + Android.

**Decision: Design-first vs. Code-first**

| Approach | Process | Pros | Cons | Best For |
|----------|---------|------|------|----------|
| **Design-first** | Design in Figma → Build in code | Designers lead, visual exploration easier | Design-code drift risk | Design-led organizations |
| **Code-first** | Build in code → Document in Figma | Code is source of truth, no drift | Slower visual iteration | Engineering-led organizations |
| **Simultaneous** | Design and code in parallel | Fastest, collaborative | Requires tight coordination | Mature teams with strong processes |

**Recommendation:** Simultaneous for mature teams; design-first for early-stage systems.

**Decision: Token-first vs. Component-first**

| Approach | Process | Pros | Cons | Best For |
|----------|---------|------|------|----------|
| **Token-first** | Define tokens → Build components using tokens | Strong foundation, easier theming | Slower initial progress | Multi-brand, theming requirements |
| **Component-first** | Build components → Extract tokens later | Faster initial progress | Harder to refactor for theming | Single-brand, speed priority |

**Recommendation:** Token-first for any system that may need theming; component-first only if certain theming won't be needed.

---

## Token Architecture Patterns

### Three-Tier Token System

**Tier 1: Primitive Tokens (Brand Layer)**

Raw values specific to brand:

```json
{
  "color": {
    "blue": {
      "100": "#E6F2FF",
      "500": "#0066CC",
      "900": "#003366"
    },
    "gray": {
      "100": "#F5F5F5",
      "500": "#808080",
      "900": "#1A1A1A"
    }
  },
  "spacing": {
    "xs": "4px",
    "sm": "8px",
    "md": "16px",
    "lg": "24px",
    "xl": "32px"
  }
}
```

**Tier 2: Semantic Tokens (System Layer)**

Meaningful references to primitives:

```json
{
  "color": {
    "text": {
      "primary": "{color.gray.900}",
      "secondary": "{color.gray.500}",
      "inverse": "#FFFFFF"
    },
    "background": {
      "primary": "#FFFFFF",
      "secondary": "{color.gray.100}",
      "inverse": "{color.gray.900}"
    },
    "action": {
      "primary": "{color.blue.500}",
      "primary-hover": "{color.blue.900}"
    }
  }
}
```

**Tier 3: Component Tokens (Component Layer)**

Component-specific references to semantic tokens:

```json
{
  "button": {
    "primary": {
      "background": "{color.action.primary}",
      "background-hover": "{color.action.primary-hover}",
      "text": "{color.text.inverse}",
      "padding-vertical": "{spacing.sm}",
      "padding-horizontal": "{spacing.md}",
      "border-radius": "{border.radius.md}"
    }
  }
}
```

**Benefits of three-tier system:**
- Change primitive value → cascades to all semantic and component tokens
- Semantic tokens provide usage guidance
- Component tokens enable component-level theming

### Multi-Mode Token Architecture

**Use case:** Multi-brand or multi-theme products

**Implementation (Figma Variables):**

```
Token: color-background-primary

Modes:
  - Light Mode: #FFFFFF
  - Dark Mode: #1A1A1A
  - Brand A Light: #F5F5F5
  - Brand A Dark: #2A2A2A
  - Brand B Light: #FAFAFA
  - Brand B Dark: #1F1F1F
```

**Switching modes:**
- Single mode switch remaps all tokens
- All components update automatically
- No component instance swapping required

**Code implementation:**

```css
/* CSS Variables with theme classes */
:root {
  --color-background-primary: #FFFFFF;
}

[data-theme="dark"] {
  --color-background-primary: #1A1A1A;
}

[data-brand="brand-a"] {
  --color-background-primary: #F5F5F5;
}
```

```javascript
// JavaScript theme switching
function setTheme(theme) {
  document.documentElement.setAttribute('data-theme', theme);
}

setTheme('dark'); // Switches entire app to dark mode
```

### Token Distribution Pipeline

**Source of truth:** JSON files in version control

**Transformation:** Style Dictionary or similar tool

**Outputs:**
- CSS variables (`variables.css`)
- SCSS variables (`_variables.scss`)
- JavaScript/TypeScript (`tokens.ts`)
- iOS Swift (`Tokens.swift`)
- Android XML (`tokens.xml`)
- Figma Variables (via plugin or API)

**Example Style Dictionary config:**

```javascript
// config.json
{
  "source": ["tokens/**/*.json"],
  "platforms": {
    "css": {
      "transformGroup": "css",
      "buildPath": "dist/css/",
      "files": [{
        "destination": "variables.css",
        "format": "css/variables"
      }]
    },
    "ios": {
      "transformGroup": "ios",
      "buildPath": "dist/ios/",
      "files": [{
        "destination": "Tokens.swift",
        "format": "ios-swift/class.swift"
      }]
    }
  }
}
```

**Automation:**
- Tokens updated in JSON → CI/CD pipeline runs Style Dictionary → Outputs generated → Published to npm/package manager → Teams update dependency

---

## Component Architecture Patterns

### Atomic Design Methodology

**Five levels of component hierarchy:**

**1. Atoms** — Smallest building blocks
- Button, Input, Label, Icon, Typography
- Cannot be broken down further
- Highly reusable

**2. Molecules** — Simple combinations of atoms
- Search field (Input + Button)
- Form field (Label + Input + Error message)
- Icon button (Icon + Button)

**3. Organisms** — Complex combinations of molecules and atoms
- Header (Logo + Navigation + Search field + User menu)
- Card (Image + Heading + Text + Button)
- Form (Multiple form fields + Submit button)

**4. Templates** — Page-level layouts
- Dashboard template
- Article template
- Settings page template

**5. Pages** — Specific instances of templates with real content
- Homepage
- Product detail page
- User profile page

**Benefits:**
- Clear hierarchy and organization
- Promotes reusability
- Easier to maintain (changes to atoms cascade up)

**Limitations:**
- Can be overly rigid
- Not all components fit neatly into categories
- Templates and pages often product-specific (not in core system)

**Recommendation:** Use atoms, molecules, organisms for design system; templates and pages are product-specific.

### Headless Component Pattern

**Problem:** Component variant explosion

Traditional approach creates separate components for each variation:
- `CardWithImage`
- `CardWithVideo`
- `CardWithIcon`
- `CardWithImageAndButton`
- `CardWithVideoAndTwoButtons`
- ... (exponential growth)

**Solution:** Headless components with slots

One flexible component with configurable slots:

```jsx
// Card.jsx (React example)
function Card({ header, media, content, actions }) {
  return (
    <div className="card">
      {header && <div className="card-header">{header}</div>}
      {media && <div className="card-media">{media}</div>}
      {content && <div className="card-content">{content}</div>}
      {actions && <div className="card-actions">{actions}</div>}
    </div>
  );
}

// Usage
<Card
  header={<h3>Product Title</h3>}
  media={<img src="product.jpg" alt="Product" />}
  content={<p>Product description</p>}
  actions={<Button>Add to Cart</Button>}
/>

<Card
  media={<VideoPlayer src="demo.mp4" />}
  content={<p>Watch our demo</p>}
  actions={
    <>
      <Button variant="primary">Sign Up</Button>
      <Button variant="secondary">Learn More</Button>
    </>
  }
/>
```

**Benefits:**
- One component instead of dozens
- Infinite flexibility
- Easier to maintain
- Smaller bundle size

**Implementation in Figma:**
- Use component properties for slot visibility
- Use instance swap properties for slot content
- Create common presets as variants (but underlying component is same)

### Compound Component Pattern

**Use case:** Components with complex internal relationships

**Example: Tabs**

```jsx
// Compound component API
<Tabs defaultValue="tab1">
  <TabList>
    <Tab value="tab1">Profile</Tab>
    <Tab value="tab2">Settings</Tab>
    <Tab value="tab3">Notifications</Tab>
  </TabList>
  <TabPanel value="tab1">
    <ProfileContent />
  </TabPanel>
  <TabPanel value="tab2">
    <SettingsContent />
  </TabPanel>
  <TabPanel value="tab3">
    <NotificationsContent />
  </TabPanel>
</Tabs>
```

**Benefits:**
- Flexible composition
- Clear semantic structure
- Shared state managed internally

**When to use:**
- Components with multiple related sub-components (Tabs, Accordion, Dropdown)
- Complex state management (active tab, expanded panel)
- Need for flexible composition

---

## Design-to-Code Workflows

### Workflow 1: Tokens as Single Source of Truth

**Process:**
1. Define tokens in JSON (version controlled)
2. Transform tokens to platform-specific formats (Style Dictionary)
3. Import tokens into Figma (via plugin or API)
4. Import tokens into code (CSS, JS, Swift, etc.)
5. Build components in both Figma and code using same tokens

**Benefits:**
- Tokens guaranteed to match
- Single source of truth
- Platform-agnostic

**Challenges:**
- Components can still drift (structure, behavior)
- Requires discipline to keep components in sync

**Tools:**
- Style Dictionary (token transformation)
- Figma Tokens plugin (sync tokens to Figma)
- Knapsack (token management platform)

### Workflow 2: Code Components as Source of Truth (UXPin Merge)

**Process:**
1. Build components in code (React, Vue, etc.)
2. Sync code components to UXPin Merge
3. Designers use actual code components in UXPin
4. Developers inspect component props and behavior
5. No handoff needed (designers already using production components)

**Benefits:**
- Perfect design-code parity
- No drift possible (same components)
- Designers prototype with real component behavior

**Challenges:**
- Requires React/Vue component library
- Designers need to understand component props
- Less visual design freedom (constrained by code components)

**Best for:**
- Teams with mature component libraries
- Products where design must match production exactly
- Design systems teams

### Workflow 3: Design Components Generate Code (Framer)

**Process:**
1. Design components in Framer
2. Add interactivity and logic (React-based)
3. Export components to React code
4. Developers integrate exported code into product

**Benefits:**
- Designers can create production-ready components
- Fast iteration (no waiting for developer implementation)
- Code export ensures design-code match

**Challenges:**
- Exported code may need refactoring
- Designers need coding knowledge (React, CSS)
- Not suitable for complex business logic

**Best for:**
- Designer-developer hybrid roles
- Marketing sites and simple web apps
- Teams prioritizing speed over code perfection

### Workflow 4: Parallel Design and Code with Sync Points

**Process:**
1. Design and code teams work in parallel
2. Regular sync meetings (weekly or bi-weekly)
3. Design reviews code implementation
4. Code reviews design updates
5. Discrepancies resolved collaboratively

**Benefits:**
- Fastest initial progress
- Leverages each team's strengths
- Flexible (not locked into specific tools)

**Challenges:**
- Requires strong communication
- Risk of drift if sync points missed
- Manual effort to keep in sync

**Best for:**
- Large teams with dedicated design and engineering
- Complex products with frequent changes
- Teams with strong collaboration culture

---

## Scalability Strategies

### Versioning and Deprecation

**Semantic versioning:**
- MAJOR.MINOR.PATCH (e.g., 2.3.1)
- MAJOR: Breaking changes
- MINOR: New features (backward compatible)
- PATCH: Bug fixes

**Deprecation process:**
1. **Announce deprecation** (in release notes, Slack, email)
2. **Add deprecation warnings** (console warnings in code, banners in Figma)
3. **Provide migration guide** (how to update to new component)
4. **Grace period** (1-2 major versions before removal)
5. **Remove deprecated component** (in next major version)

**Example deprecation timeline:**
- v2.0: Introduce new `Button` component, deprecate old `LegacyButton`
- v2.1-2.9: Both components available, warnings for `LegacyButton` usage
- v3.0: Remove `LegacyButton`, only new `Button` available

### Performance Optimization

**Code splitting:**
- Don't bundle entire component library
- Import only components used
- Use tree-shaking (ES modules)

```javascript
// Bad: Imports entire library
import { Button, Card, Modal } from 'design-system';

// Good: Imports only what's needed
import Button from 'design-system/Button';
import Card from 'design-system/Card';
```

**Lazy loading:**
- Load heavy components only when needed
- Use React.lazy() or similar

```javascript
const Modal = React.lazy(() => import('design-system/Modal'));

function App() {
  return (
    <Suspense fallback={<Loading />}>
      {showModal && <Modal />}
    </Suspense>
  );
}
```

**CSS optimization:**
- Use CSS-in-JS with critical CSS extraction
- Or use utility-first CSS (Tailwind) with PurgeCSS
- Minimize unused styles

### Multi-Platform Strategy

**Shared token layer:**
- Tokens defined once (JSON)
- Transformed to platform-specific formats
- Ensures visual consistency across platforms

**Platform-specific components:**
- Web: React, Vue, Angular, Svelte
- iOS: SwiftUI or UIKit
- Android: Jetpack Compose or XML
- React Native: Shared with web (if using React)

**Shared documentation:**
- Single documentation site for all platforms
- Platform-specific code examples
- Shared design principles and usage guidelines

**Example structure:**
```
design-system/
├── tokens/              (Shared JSON tokens)
├── packages/
│   ├── web-react/       (React components)
│   ├── web-vue/         (Vue components)
│   ├── ios/             (SwiftUI components)
│   └── android/         (Compose components)
└── docs/                (Shared documentation)
```

---

## Migration Strategies

### Migrating to a Design System

**Scenario:** Existing product(s) without design system

**Approach 1: Big Bang (Not Recommended)**
- Rebuild entire product with design system
- High risk, long timeline, blocks other work

**Approach 2: Gradual Migration (Recommended)**

**Phase 1: Foundation (Months 1-2)**
- Define design tokens
- Build atomic components (buttons, inputs, typography)
- Document usage guidelines
- Set up infrastructure (repo, CI/CD, documentation site)

**Phase 2: Pilot (Month 3)**
- Choose one product or feature area
- Migrate to design system components
- Gather feedback, iterate on components
- Refine processes

**Phase 3: Expansion (Months 4-6)**
- Build more complex components (cards, modals, forms)
- Migrate additional product areas
- Train teams on design system usage

**Phase 4: Consolidation (Months 7-12)**
- Migrate remaining product areas
- Deprecate old components
- Establish governance and contribution processes
- Measure adoption and impact

**Coexistence strategy:**
- Old and new components coexist during migration
- Use CSS namespacing to avoid conflicts (`.ds-button` vs `.legacy-button`)
- Gradually replace old components
- Track migration progress (% of components migrated)

### Migrating Between Design Systems

**Scenario:** Replacing one design system with another (e.g., Material UI → Custom system)

**Approach:**

1. **Map components** — Create mapping between old and new components
   - Old `MuiButton` → New `Button`
   - Old `MuiCard` → New `Card`
   - Identify components without direct equivalent

2. **Create adapter layer** (optional) — Temporary compatibility layer
   ```javascript
   // Adapter wraps new component with old API
   export function MuiButton(props) {
     return <Button {...convertProps(props)} />;
   }
   ```

3. **Migrate incrementally** — One component type at a time
   - Week 1: Migrate all buttons
   - Week 2: Migrate all inputs
   - Week 3: Migrate all cards
   - ...

4. **Remove adapter layer** — Once migration complete, remove adapters

---

Design system architecture is the foundation for scalability, consistency, and efficiency. Invest time in planning architecture upfront to avoid costly refactoring later.
