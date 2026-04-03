# Buttons - Detailed Reference

Detailed reference content for component design.

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
