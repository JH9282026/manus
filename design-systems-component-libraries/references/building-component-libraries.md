# Building Component Libraries

## Component Design Principles

### Composability
- Build small, focused components that combine into larger patterns
- Prefer composition over inheritance
- Use slots/children for flexible content injection
- Avoid deeply nested component hierarchies

### Consistency
- Follow naming conventions (PascalCase for components, camelCase for props)
- Use consistent prop patterns across components (size: sm/md/lg)
- Apply uniform spacing and alignment rules
- Maintain consistent interaction patterns (hover, focus, active states)

### Accessibility First
- Every component must meet WCAG 2.1 AA minimum
- Include proper ARIA roles, labels, and descriptions
- Support keyboard navigation (Tab, Enter, Space, Escape, Arrow keys)
- Ensure sufficient color contrast (4.5:1 text, 3:1 UI elements)
- Test with screen readers (NVDA, VoiceOver, JAWS)

---

## Component Categories

### Form Components
- **Text Input**: Single-line text entry with validation states
- **Text Area**: Multi-line text entry with character count
- **Select/Dropdown**: Single or multi-select options
- **Checkbox**: Binary or indeterminate state selections
- **Radio Button**: Mutually exclusive selections
- **Toggle/Switch**: On/off boolean controls
- **Date Picker**: Calendar-based date selection
- **File Upload**: Drag-and-drop or click-to-browse

### Navigation Components
- **Top Navigation Bar**: Primary app navigation with logo
- **Side Navigation**: Collapsible sidebar with hierarchy
- **Breadcrumbs**: Location context within hierarchy
- **Tabs**: Content area switching
- **Pagination**: Page-based content navigation
- **Stepper**: Multi-step process indicator

### Feedback Components
- **Alert/Banner**: Inline status messages (info, success, warning, error)
- **Toast/Snackbar**: Temporary notification overlays
- **Modal/Dialog**: Focused user interaction overlays
- **Progress Bar**: Determinate or indeterminate progress
- **Skeleton Loader**: Content placeholder during loading
- **Empty State**: Guidance when no content exists

### Data Display Components
- **Table**: Sortable, filterable data grids
- **Card**: Content container with header, body, actions
- **List**: Ordered or unordered item collections
- **Badge/Tag**: Status indicators or category labels
- **Avatar**: User or entity representation
- **Tooltip**: Contextual information on hover/focus

---

## Component API Design

### Props Naming Conventions

| Pattern | Examples | Purpose |
|---|---|---|
| `variant` | primary, secondary, ghost | Visual style |
| `size` | sm, md, lg, xl | Dimensional scale |
| `disabled` | true/false | Interaction state |
| `loading` | true/false | Async state |
| `error` | true/false or string | Validation state |
| `onChange` | callback function | Event handler |
| `className` | string | Style override escape hatch |

### State Management

Components should handle these states:
- Default / resting
- Hover
- Focus (keyboard)
- Active / pressed
- Disabled
- Loading
- Error / invalid
- Read-only

---

## Design-to-Code Workflow

### Figma to Code Pipeline

1. **Design in Figma**: Use auto-layout, components, and variants
2. **Define tokens**: Export design tokens from Figma using Tokens Studio
3. **Transform tokens**: Use Style Dictionary to generate platform-specific formats
4. **Build components**: Implement React/Vue components using tokens
5. **Document**: Auto-generate docs with Storybook
6. **Test**: Visual regression testing with Chromatic
7. **Publish**: Release as npm package with semantic versioning
