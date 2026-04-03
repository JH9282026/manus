# Change Implementation Patterns

Detailed CSS specifications and design token updates for common iteration changes.

---

## Focus State Implementation

**Standard focus ring:**
```css
:focus-visible {
  outline: none;
  box-shadow: 0 0 0 3px var(--violet-200);
}

.btn:focus-visible {
  box-shadow: 0 0 0 3px var(--violet-200);
}

.input:focus {
  border-color: var(--violet-500);
  box-shadow: 0 0 0 3px var(--violet-100);
}
```

**For dark backgrounds:**
```css
.dark :focus-visible {
  box-shadow: 0 0 0 3px var(--violet-400);
}
```

---

## Shadow Scale Definition

```css
:root {
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.07),
               0 2px 4px -2px rgba(0, 0, 0, 0.05);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.08),
               0 4px 6px -4px rgba(0, 0, 0, 0.04);
  --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1),
               0 8px 10px -6px rgba(0, 0, 0, 0.05);
}
```

**Application guide:**
| Element | Shadow Level |
|---------|-------------|
| Subtle cards | shadow-sm |
| Standard cards, dropdowns | shadow-md |
| Modals, popovers | shadow-lg |
| Floating elements, toasts | shadow-xl |

---

## Border Radius Standardization

```css
:root {
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-xl: 16px;
  --radius-full: 9999px;
}
```

**Application:**
| Element | Radius |
|---------|--------|
| Buttons | radius-md (8px) |
| Inputs | radius-md (8px) |
| Cards | radius-lg (12px) |
| Modals | radius-xl (16px) |
| Avatars, badges | radius-full |

---

## Button Hover Refinement

```css
.btn-primary {
  transition: all 0.15s ease;
}

.btn-primary:hover {
  background: var(--primary-dark);
  transform: translateY(-1px);
  box-shadow: var(--shadow-md);
}

.btn-primary:active {
  transform: translateY(0);
  box-shadow: var(--shadow-sm);
}
```

---

## Skeleton Loader Pattern

```css
.skeleton {
  background: linear-gradient(
    90deg,
    var(--gray-100) 25%,
    var(--gray-200) 50%,
    var(--gray-100) 75%
  );
  background-size: 200% 100%;
  animation: skeleton-pulse 1.5s ease-in-out infinite;
  border-radius: var(--radius-md);
}

@keyframes skeleton-pulse {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}
```

**Skeleton variants:**
- Text line: `height: 16px; width: 80%; margin-bottom: 8px;`
- Avatar: `height: 40px; width: 40px; border-radius: 50%;`
- Card: `height: 200px; width: 100%;`
- Button: `height: 40px; width: 120px;`

---

## Responsive Touch Target Fix

```css
/* Ensure minimum touch targets on touch devices */
@media (pointer: coarse) {
  .btn,
  .nav-link,
  .list-item-action {
    min-height: 48px;
    min-width: 48px;
    display: flex;
    align-items: center;
  }

  /* Increase checkbox/radio hit area */
  .checkbox-wrapper,
  .radio-wrapper {
    padding: 12px;
    margin: -12px;
  }
}
```
