# Component Examples

## Component: [Name]

### Description
[What it does and when to use]

### Variants
- **Primary**: [Usage]
- **Secondary**: [Usage]
- **Tertiary/Ghost**: [Usage]

### Sizes
- **Small**: [Dimensions, font size]
- **Medium**: [Dimensions, font size] (default)
- **Large**: [Dimensions, font size]

### States
| State | Background | Text | Border | Other |
|-------|------------|------|--------|-------|
| Default | | | | |
| Hover | | | | |
| Focus | | | | Focus ring |
| Active | | | | |
| Disabled | | | | opacity: 0.5 |

### Anatomy
```
┌─────────────────────────┐
│  [icon]  Label Text  │
└─────────────────────────┘
         │
    padding: 12px 20px
```

### Specifications
| Property | Value |
|----------|-------|
| Height | 40px (medium) |
| Padding | 12px 20px |
| Border radius | 8px |
| Font size | 14px |
| Font weight | 500 |
| Transition | 150ms ease |

### Accessibility
- [ ] Minimum 44px touch target
- [ ] 4.5:1 contrast ratio
- [ ] Visible focus state
- [ ] Disabled state announced
```

### Step 4: Design Core Components

**Essential components to define:**

#### Buttons
```markdown
### Buttons

#### Primary Button
| State | Background | Text | Border |
|-------|------------|------|--------|
| Default | Violet-500 | White | None |
| Hover | Violet-400 | White | None |
| Focus | Violet-500 | White | + focus ring |
| Active | Violet-600 | White | None |
| Disabled | Violet-200 | White | None |

#### Secondary Button
| State | Background | Text | Border |
|-------|------------|------|--------|
| Default | White | Violet-600 | Violet-300 |
| Hover | Violet-50 | Violet-600 | Violet-400 |
| Focus | White | Violet-600 | + focus ring |
| Active | Violet-100 | Violet-700 | Violet-500 |
| Disabled | Gray-50 | Gray-400 | Gray-200 |

#### Ghost Button
| State | Background | Text | Border |
|-------|------------|------|--------|
| Default | Transparent | Violet-600 | None |
| Hover | Violet-50 | Violet-600 | None |
| Focus | Transparent | Violet-600 | + focus ring |
| Active | Violet-100 | Violet-700 | None |
| Disabled | Transparent | Gray-400 | None |

#### Destructive Button
| State | Background | Text | Border |
|-------|------------|------|--------|
| Default | Error-500 | White | None |
| Hover | Error-400 | White | None |

#### Button Sizes
| Size | Height | Padding | Font | Icon |
|------|--------|---------|------|------|
| sm | 32px | 8px 16px | 13px | 16px |
| md | 40px | 10px 20px | 14px | 18px |
| lg | 48px | 12px 24px | 16px | 20px |
```

#### Form Inputs
```markdown
### Text Input

#### States
| State | Background | Border | Label | Icon |
|-------|------------|--------|-------|------|
| Default | White | Gray-300 | Gray-600 | Gray-400 |
| Hover | White | Gray-400 | Gray-600 | Gray-500 |
| Focus | White | Violet-500 | Violet-600 | Violet-500 |
| Filled | White | Gray-300 | Gray-600 | Gray-600 |
| Error | White | Error-500 | Error-600 | Error-500 |
| Disabled | Gray-50 | Gray-200 | Gray-400 | Gray-300 |

#### Specifications
| Property | Value |
|----------|-------|
| Height | 44px |
| Padding | 12px 16px |
| Border width | 1px |
| Border radius | 8px |
| Font size | 16px (prevents iOS zoom) |
| Placeholder color | Gray-400 |
| Focus ring | 2px Violet-200 offset 2px |

#### Anatomy
```
 Label Text
┌──────────────────────────────┐
│ [icon] Placeholder text... │
└──────────────────────────────┘
 Helper text or error message
```
```

---


## Example Input/Output

### Example Input

```markdown
**Project**: TaskFlow dashboard
**Design tokens**: Violet primary, Slate neutrals, 8px spacing base
**Key components needed**: Buttons, inputs, cards, navigation
```

### Example Output

```markdown

## Component Library: TaskFlow

### Design Tokens Reference
- Primary: Violet-500 (#8B5CF6)
- Border radius: 8px (default), 12px (cards)
- Spacing unit: 8px
- Shadow: 0 1px 3px rgba(0,0,0,0.1)

---


## Buttons

### Primary Button

**Visual**
```
┌──────────────────┐
│ 🔵 Button Text   │  <- Violet-500 bg, white text
└──────────────────┘
```

**States**
| State | Background | Text | Other |
|-------|------------|------|-------|
| Default | `#8B5CF6` | `#FFFFFF` | |
| Hover | `#A78BFA` | `#FFFFFF` | cursor: pointer |
| Focus | `#8B5CF6` | `#FFFFFF` | ring: 2px #DDD6FE |
| Active | `#7C3AED` | `#FFFFFF` | transform: scale(0.98) |
| Disabled | `#DDD6FE` | `#FFFFFF` | opacity: 0.6, cursor: not-allowed |
| Loading | `#8B5CF6` | - | spinner + "Loading..." |

**Sizes**
| Size | Height | Padding | Font | Min Width |
|------|--------|---------|------|-----------|
| sm | 32px | 8px 12px | 13px/500 | 64px |
| md | 40px | 10px 16px | 14px/500 | 80px |
| lg | 48px | 12px 24px | 16px/500 | 96px |

**CSS**
```css
.btn-primary {
  background: #8B5CF6;
  color: white;
  border: none;
  border-radius: 8px;
  padding: 10px 16px;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: all 150ms ease;
}
.btn-primary:hover {
  background: #A78BFA;
}
.btn-primary:focus {
  outline: none;
  box-shadow: 0 0 0 2px white, 0 0 0 4px #DDD6FE;
}
.btn-primary:active {
  background: #7C3AED;
  transform: scale(0.98);
}
.btn-primary:disabled {
  background: #DDD6FE;
  opacity: 0.6;
  cursor: not-allowed;
}
```

---


## Input Field

### Text Input

**Visual**
```
 Email Address
┌────────────────────────────┐
│ ✉️  you@example.com       │
└────────────────────────────┘
 We'll never share your email.
```

**States**
| State | Border | Shadow | Icon |
|-------|--------|--------|------|
| Default | Gray-300 | none | Gray-400 |
| Hover | Gray-400 | none | Gray-500 |
| Focus | Violet-500 | ring 2px Violet-100 | Violet-500 |
| Error | Error-500 | ring 2px Error-100 | Error-500 |
| Disabled | Gray-200 | none | Gray-300 |

**Specifications**
```css
.input {
  width: 100%;
  height: 44px;
  padding: 0 12px 0 40px; /* left padding for icon */
  border: 1px solid #CBD5E1;
  border-radius: 8px;
  font-size: 16px;
  color: #334155;
  background: white;
  transition: all 150ms ease;
}
.input:focus {
  border-color: #8B5CF6;
  box-shadow: 0 0 0 3px #EDE9FE;
  outline: none;
}
.input.error {
  border-color: #EF4444;
  box-shadow: 0 0 0 3px #FEE2E2;
}
```

---


## Card

### Standard Card

**Visual**
```
┌───────────────────────────────┐
│                               │
│  Card Title            [⋮]   │
│                               │
│  Card content goes here.     │
│  This is the body text.      │
│                               │
│  [Action]  [Secondary]       │
│                               │
└───────────────────────────────┘
```

**Variants**
| Variant | Background | Border | Shadow |
|---------|------------|--------|--------|
| Default | White | Gray-200 | sm |
| Elevated | White | None | lg |
| Interactive | White | Gray-200 | sm → lg on hover |
| Selected | Violet-50 | Violet-300 | sm |

**Specifications**
```css
.card {
  background: white;
  border: 1px solid #E2E8F0;
  border-radius: 12px;
  padding: 20px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}
.card-interactive:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  border-color: #CBD5E1;
}
.card-selected {
  background: #F5F3FF;
  border-color: #C4B5FD;
}
```

---


## Navigation

### Sidebar Nav Item

**States**
```
Default:    [icon] Projects        <- Gray-600 text
Hover:      [■■■■■■■■■■■]          <- Gray-100 bg
Active:     [🟣 Projects 🟣]        <- Violet-50 bg, Violet-600 text
```

| State | Background | Text | Icon | Indicator |
|-------|------------|------|------|----------|
| Default | Transparent | Gray-600 | Gray-400 | None |
| Hover | Gray-100 | Gray-700 | Gray-500 | None |
| Active | Violet-50 | Violet-700 | Violet-500 | Left bar Violet-500 |
| Disabled | Transparent | Gray-300 | Gray-200 | None |

```css
.nav-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 16px;
  border-radius: 8px;
  color: #475569;
  text-decoration: none;
  transition: all 150ms ease;
}
.nav-item:hover {
  background: #F1F5F9;
  color: #334155;
}
.nav-item.active {
  background: #F5F3FF;
  color: #6D28D9;
}
.nav-item.active::before {
  content: '';
  position: absolute;
  left: 0;
  width: 3px;
  height: 24px;
  background: #8B5CF6;
  border-radius: 0 2px 2px 0;
}
```

---


## Badges & Tags

### Status Badge

**Variants**
| Status | Background | Text | Icon |
|--------|------------|------|------|
| Success | #D1FAE5 | #065F46 | ✓ |
| Warning | #FEF3C7 | #92400E | ! |
| Error | #FEE2E2 | #991B1B | × |
| Info | #DBEAFE | #1E40AF | i |
| Neutral | #F1F5F9 | #475569 | |
| Purple | #EDE9FE | #5B21B6 | |

```css
.badge {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 4px 10px;
  border-radius: 9999px;
  font-size: 12px;
  font-weight: 500;
}
.badge-success {
  background: #D1FAE5;
  color: #065F46;
}
```

---

