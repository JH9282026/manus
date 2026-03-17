# Design Tokens

Comprehensive guide to design tokens: definition, architecture, implementation, and distribution across platforms.

---

## Design Token Fundamentals

### What Are Design Tokens?

Design tokens are named entities that store visual design attributes (colors, typography, spacing, etc.) as data. They serve as the single source of truth for design decisions, enabling consistency across platforms and products.

**Traditional approach (hard-coded values):**
```css
.button {
  background-color: #0066CC;
  padding: 8px 16px;
  border-radius: 4px;
}
```

**Token-based approach:**
```css
.button {
  background-color: var(--color-action-primary);
  padding: var(--spacing-sm) var(--spacing-md);
  border-radius: var(--border-radius-md);
}
```

**Benefits:**
- Change token value once → updates everywhere
- Semantic naming provides usage guidance
- Platform-agnostic (same tokens for web, iOS, Android)
- Enables theming (light/dark mode, multi-brand)

### Token vs. Style

**Styles (Figma/Sketch):**
- Static values
- No logic or relationships
- Platform-specific

**Tokens (Variables):**
- Can reference other tokens
- Support logic (modes, calculations)
- Platform-agnostic (transform to any format)
- Treat design decisions as data

**Migration path:** Styles → Variables (Figma) → Design Tokens (JSON)

---

## Token Types and Hierarchy

### Primitive Tokens (Tier 1)

**Purpose:** Raw values, brand-specific palette

**Categories:**

**Colors:**
```json
{
  "color": {
    "blue": {
      "100": "#E6F2FF",
      "200": "#CCE5FF",
      "300": "#99CCFF",
      "400": "#66B2FF",
      "500": "#0066CC",
      "600": "#0052A3",
      "700": "#003D7A",
      "800": "#002952",
      "900": "#001429"
    },
    "gray": {
      "100": "#F5F5F5",
      "500": "#808080",
      "900": "#1A1A1A"
    }
  }
}
```

**Spacing:**
```json
{
  "spacing": {
    "0": "0px",
    "1": "4px",
    "2": "8px",
    "3": "12px",
    "4": "16px",
    "6": "24px",
    "8": "32px",
    "12": "48px",
    "16": "64px"
  }
}
```

**Typography:**
```json
{
  "font": {
    "family": {
      "sans": "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif",
      "mono": "'Fira Code', 'Courier New', monospace"
    },
    "size": {
      "xs": "12px",
      "sm": "14px",
      "base": "16px",
      "lg": "18px",
      "xl": "20px",
      "2xl": "24px",
      "3xl": "30px",
      "4xl": "36px"
    },
    "weight": {
      "normal": "400",
      "medium": "500",
      "semibold": "600",
      "bold": "700"
    }
  }
}
```

**Other primitives:**
- Border radius (`2px`, `4px`, `8px`, `16px`, `9999px` for pills)
- Border width (`1px`, `2px`, `4px`)
- Shadows (elevation levels)
- Opacity values (`0.1`, `0.5`, `0.8`, `1`)
- Z-index layers (`0`, `10`, `20`, `30`, `40`, `50`)

### Semantic Tokens (Tier 2)

**Purpose:** Meaningful, context-aware references to primitives

**Naming structure:** `[category]-[property]-[variant]-[state]`

**Color semantics:**
```json
{
  "color": {
    "text": {
      "primary": "{color.gray.900}",
      "secondary": "{color.gray.500}",
      "tertiary": "{color.gray.400}",
      "inverse": "#FFFFFF",
      "link": "{color.blue.500}",
      "link-hover": "{color.blue.700}"
    },
    "background": {
      "primary": "#FFFFFF",
      "secondary": "{color.gray.100}",
      "tertiary": "{color.gray.200}",
      "inverse": "{color.gray.900}"
    },
    "action": {
      "primary": "{color.blue.500}",
      "primary-hover": "{color.blue.700}",
      "primary-active": "{color.blue.800}",
      "secondary": "{color.gray.500}",
      "secondary-hover": "{color.gray.700}"
    },
    "border": {
      "default": "{color.gray.300}",
      "hover": "{color.gray.500}",
      "focus": "{color.blue.500}"
    },
    "feedback": {
      "success": "#10B981",
      "warning": "#F59E0B",
      "error": "#EF4444",
      "info": "{color.blue.500}"
    }
  }
}
```

**Spacing semantics:**
```json
{
  "spacing": {
    "padding": {
      "xs": "{spacing.1}",
      "sm": "{spacing.2}",
      "md": "{spacing.4}",
      "lg": "{spacing.6}",
      "xl": "{spacing.8}"
    },
    "margin": {
      "xs": "{spacing.1}",
      "sm": "{spacing.2}",
      "md": "{spacing.4}",
      "lg": "{spacing.6}",
      "xl": "{spacing.8}"
    },
    "gap": {
      "xs": "{spacing.1}",
      "sm": "{spacing.2}",
      "md": "{spacing.4}",
      "lg": "{spacing.6}"
    }
  }
}
```

### Component Tokens (Tier 3)

**Purpose:** Component-specific references to semantic tokens

**Button tokens:**
```json
{
  "button": {
    "primary": {
      "background": "{color.action.primary}",
      "background-hover": "{color.action.primary-hover}",
      "background-active": "{color.action.primary-active}",
      "text": "{color.text.inverse}",
      "border-radius": "{border.radius.md}",
      "padding-vertical": "{spacing.padding.sm}",
      "padding-horizontal": "{spacing.padding.md}",
      "font-size": "{font.size.base}",
      "font-weight": "{font.weight.medium}"
    },
    "secondary": {
      "background": "transparent",
      "background-hover": "{color.background.secondary}",
      "text": "{color.action.secondary}",
      "border": "{color.border.default}",
      "border-hover": "{color.border.hover}"
    }
  }
}
```

**Card tokens:**
```json
{
  "card": {
    "background": "{color.background.primary}",
    "border": "{color.border.default}",
    "border-radius": "{border.radius.lg}",
    "padding": "{spacing.padding.lg}",
    "shadow": "{shadow.md}"
  }
}
```

**Benefits of component tokens:**
- Enable component-level theming
- Centralize component styling decisions
- Make it easy to update component appearance globally

---

## Token Naming Conventions

### Naming Best Practices

**1. Semantic over descriptive**

❌ **Poor:** `blue-500`, `gray-300`, `font-large`
- Problem: Changing brand color requires updating all references

✅ **Good:** `color-action-primary`, `color-text-secondary`, `font-size-heading-1`
- Benefit: Change token value, not references

**2. Consistent structure**

Use consistent naming pattern:
```
[category]-[property]-[variant]-[state]

Examples:
color-background-primary
color-background-primary-hover
spacing-padding-large
font-size-body-small
```

**3. Avoid abbreviations**

❌ **Poor:** `clr-bg-pri`, `spc-pd-lg`
✅ **Good:** `color-background-primary`, `spacing-padding-large`

**4. Use kebab-case**

❌ **Poor:** `colorBackgroundPrimary`, `color_background_primary`
✅ **Good:** `color-background-primary`

**5. Avoid platform-specific names**

❌ **Poor:** `ios-blue`, `android-padding`
✅ **Good:** `color-action-primary`, `spacing-padding-medium`

### Token Naming Examples

**Colors:**
- `color-text-primary`
- `color-text-secondary`
- `color-background-primary`
- `color-action-primary`
- `color-action-primary-hover`
- `color-border-default`
- `color-feedback-success`

**Spacing:**
- `spacing-padding-small`
- `spacing-margin-medium`
- `spacing-gap-large`

**Typography:**
- `font-family-base`
- `font-size-heading-1`
- `font-weight-bold`
- `line-height-tight`

**Borders:**
- `border-radius-small`
- `border-width-default`

**Shadows:**
- `shadow-small`
- `shadow-medium`
- `shadow-large`

---

## Multi-Mode Token Architecture

### Use Cases for Modes

**1. Light/Dark themes**
**2. Multi-brand systems**
**3. High-contrast modes (accessibility)**
**4. Seasonal themes**

### Implementing Modes

**Figma Variables (Modes):**

```
Variable: color-background-primary

Modes:
  Light: #FFFFFF
  Dark: #1A1A1A
  High Contrast: #000000
```

**JSON (with mode references):**

```json
{
  "color": {
    "background": {
      "primary": {
        "$type": "color",
        "$value": {
          "light": "#FFFFFF",
          "dark": "#1A1A1A",
          "high-contrast": "#000000"
        }
      }
    }
  }
}
```

**CSS (with theme classes):**

```css
:root {
  --color-background-primary: #FFFFFF;
  --color-text-primary: #1A1A1A;
}

[data-theme="dark"] {
  --color-background-primary: #1A1A1A;
  --color-text-primary: #FFFFFF;
}

[data-theme="high-contrast"] {
  --color-background-primary: #000000;
  --color-text-primary: #FFFFFF;
}
```

**JavaScript theme switching:**

```javascript
function setTheme(theme) {
  document.documentElement.setAttribute('data-theme', theme);
  localStorage.setItem('theme', theme);
}

// Auto-detect user preference
const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
const savedTheme = localStorage.getItem('theme');
const theme = savedTheme || (prefersDark ? 'dark' : 'light');
setTheme(theme);
```

### Multi-Brand Architecture

**Scenario:** One design system, multiple brands

**Approach 1: Mode per brand**

```
Variable: color-action-primary

Modes:
  Brand A: #0066CC
  Brand B: #FF6600
  Brand C: #00CC66
```

**Approach 2: Brand-specific token files**

```
tokens/
├── core.json          (Shared tokens)
├── brand-a.json       (Brand A overrides)
├── brand-b.json       (Brand B overrides)
└── brand-c.json       (Brand C overrides)
```

**Build process:**
1. Load core tokens
2. Merge brand-specific overrides
3. Generate platform-specific outputs

---

## Token Distribution

### Storage Format: JSON

**Why JSON?**
- Platform-agnostic
- Human-readable
- Easy to version control
- Transformable to any format

**Example token file:**

```json
{
  "color": {
    "blue": {
      "500": {
        "$type": "color",
        "$value": "#0066CC",
        "$description": "Primary brand blue"
      }
    },
    "action": {
      "primary": {
        "$type": "color",
        "$value": "{color.blue.500}",
        "$description": "Primary action color for buttons and links"
      }
    }
  },
  "spacing": {
    "md": {
      "$type": "dimension",
      "$value": "16px",
      "$description": "Medium spacing"
    }
  }
}
```

**Token metadata:**
- `$type` — Token type (color, dimension, fontFamily, etc.)
- `$value` — Token value (can reference other tokens)
- `$description` — Human-readable description

### Transformation: Style Dictionary

**Installation:**
```bash
npm install style-dictionary
```

**Configuration (`config.json`):**

```json
{
  "source": ["tokens/**/*.json"],
  "platforms": {
    "css": {
      "transformGroup": "css",
      "buildPath": "dist/css/",
      "files": [
        {
          "destination": "variables.css",
          "format": "css/variables"
        }
      ]
    },
    "scss": {
      "transformGroup": "scss",
      "buildPath": "dist/scss/",
      "files": [
        {
          "destination": "_variables.scss",
          "format": "scss/variables"
        }
      ]
    },
    "js": {
      "transformGroup": "js",
      "buildPath": "dist/js/",
      "files": [
        {
          "destination": "tokens.js",
          "format": "javascript/es6"
        }
      ]
    },
    "ios": {
      "transformGroup": "ios",
      "buildPath": "dist/ios/",
      "files": [
        {
          "destination": "Tokens.swift",
          "format": "ios-swift/class.swift",
          "className": "DesignTokens"
        }
      ]
    },
    "android": {
      "transformGroup": "android",
      "buildPath": "dist/android/",
      "files": [
        {
          "destination": "tokens.xml",
          "format": "android/resources"
        }
      ]
    }
  }
}
```

**Build command:**
```bash
style-dictionary build
```

**Output examples:**

**CSS:**
```css
:root {
  --color-blue-500: #0066CC;
  --color-action-primary: #0066CC;
  --spacing-md: 16px;
}
```

**SCSS:**
```scss
$color-blue-500: #0066CC;
$color-action-primary: #0066CC;
$spacing-md: 16px;
```

**JavaScript:**
```javascript
export const colorBlue500 = '#0066CC';
export const colorActionPrimary = '#0066CC';
export const spacingMd = '16px';
```

**iOS Swift:**
```swift
public class DesignTokens {
  public static let colorBlue500 = UIColor(hex: "#0066CC")
  public static let colorActionPrimary = UIColor(hex: "#0066CC")
  public static let spacingMd: CGFloat = 16.0
}
```

**Android XML:**
```xml
<resources>
  <color name="color_blue_500">#0066CC</color>
  <color name="color_action_primary">#0066CC</color>
  <dimen name="spacing_md">16dp</dimen>
</resources>
```

### Distribution: Package Management

**Publish tokens as npm package:**

```json
// package.json
{
  "name": "@company/design-tokens",
  "version": "1.0.0",
  "main": "dist/js/tokens.js",
  "files": [
    "dist/"
  ]
}
```

**Install in projects:**
```bash
npm install @company/design-tokens
```

**Use in code:**
```javascript
import { colorActionPrimary, spacingMd } from '@company/design-tokens';
```

**Use in CSS:**
```css
@import '@company/design-tokens/dist/css/variables.css';

.button {
  background-color: var(--color-action-primary);
  padding: var(--spacing-md);
}
```

---

## Advanced Token Strategies

### Calculated Tokens

**Use case:** Derive values from other tokens

**Example: Spacing scale**

```json
{
  "spacing": {
    "base": {
      "$type": "dimension",
      "$value": "8px"
    },
    "xs": {
      "$type": "dimension",
      "$value": "calc({spacing.base} * 0.5)"  // 4px
    },
    "sm": {
      "$type": "dimension",
      "$value": "{spacing.base}"  // 8px
    },
    "md": {
      "$type": "dimension",
      "$value": "calc({spacing.base} * 2)"  // 16px
    },
    "lg": {
      "$type": "dimension",
      "$value": "calc({spacing.base} * 3)"  // 24px
    }
  }
}
```

**Benefit:** Change base value, entire scale updates

### Contextual Tokens

**Use case:** Tokens that change based on context

**Example: Responsive spacing**

```css
:root {
  --spacing-section: 32px;
}

@media (min-width: 768px) {
  :root {
    --spacing-section: 64px;
  }
}

@media (min-width: 1024px) {
  :root {
    --spacing-section: 96px;
  }
}
```

**Usage:**
```css
.section {
  padding: var(--spacing-section);
}
```

### Composite Tokens

**Use case:** Tokens that combine multiple values

**Example: Typography tokens**

```json
{
  "typography": {
    "heading-1": {
      "$type": "typography",
      "$value": {
        "fontFamily": "{font.family.sans}",
        "fontSize": "{font.size.4xl}",
        "fontWeight": "{font.weight.bold}",
        "lineHeight": "1.2",
        "letterSpacing": "-0.02em"
      }
    }
  }
}
```

**CSS output:**
```css
.heading-1 {
  font-family: var(--font-family-sans);
  font-size: var(--font-size-4xl);
  font-weight: var(--font-weight-bold);
  line-height: 1.2;
  letter-spacing: -0.02em;
}
```

---

## Token Governance

### Token Approval Process

**For new tokens:**

1. **Proposal** — Team member proposes new token
2. **Review** — Design system team evaluates
   - Is this a new primitive or semantic token?
   - Does it align with existing token structure?
   - Is it generalizable (not product-specific)?
3. **Decision:**
   - **Approve** → Add to token library
   - **Use existing** → Point to existing token that serves same purpose
   - **Reject** → Explain why it doesn't belong in system

### Token Deprecation

**Process:**

1. **Mark as deprecated** (add `$deprecated: true` to token)
2. **Provide replacement** (add `$replacedBy` reference)
3. **Announce** (changelog, Slack, email)
4. **Grace period** (1-2 major versions)
5. **Remove** (in next major version)

**Example:**

```json
{
  "color": {
    "primary": {
      "$type": "color",
      "$value": "#0066CC",
      "$deprecated": true,
      "$replacedBy": "color.action.primary",
      "$description": "Deprecated: Use color.action.primary instead"
    }
  }
}
```

### Token Documentation

**Each token should document:**

- **Name** — Token identifier
- **Value** — Current value (and mode variations if applicable)
- **Type** — Color, dimension, typography, etc.
- **Description** — What is this token for?
- **Usage** — When to use (and when not to use)
- **Examples** — Visual examples of token in use

**Documentation tools:**
- Zeroheight
- Supernova
- Knapsack
- Custom documentation site

---

Design tokens are the foundation of scalable, consistent design systems. Invest in token architecture early to enable theming, multi-platform support, and effortless design updates across your entire product ecosystem.
