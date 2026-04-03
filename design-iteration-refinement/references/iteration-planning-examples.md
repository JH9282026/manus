# Iteration Planning Examples

Concrete examples of iteration plans with before/after changes and score tracking.

---

## Example: TaskFlow V2 → V3 Iteration Plan

### Goal
Move from 7.74/10 to 8.5+/10

### Priority Matrix

#### Do First (High Impact, Low Effort)
1. **Fix typography line-heights** | +0.1 impact | 1 hour
   - Body: 1.5 → 1.6
   - Headings: 1.2 → 1.3

2. **Standardize shadows** | +0.05 impact | 30 min
   - Define: shadow-sm, shadow-md, shadow-lg
   - Apply consistently to all cards

3. **Enhance focus states** | +0.1 impact | 1 hour
   - Add visible focus ring (3px violet-200)
   - Ensure all interactive elements covered

#### Schedule (High Impact, High Effort)
4. **Mobile task list redesign** | +0.15 impact | 3 hours
   - Convert to swipeable cards
   - Larger touch targets (48px)
   - Pull to refresh

5. **Empty states with personality** | +0.1 impact | 2 hours
   - Add illustrations
   - Friendly copy
   - Clear CTAs

#### Quick Wins
6. **Border radius consistency** | +0.02 | 15 min
7. **Button hover state refinement** | +0.02 | 15 min

---

### Scope Decision

**V3 Scope** (This iteration — Target: 8.5/10):
- Typography line-heights ✓
- Shadow standardization ✓
- Focus states ✓
- Mobile task list ✓
- Quick wins ✓

**V4 Scope** (Next iteration — Target: 9.0/10):
- Empty states
- Micro-interactions
- Final accessibility audit
- Edge case handling

---

### Expected Score Impact

| Category | V2 Score | V3 Expected | Change |
|----------|----------|-------------|--------|
| Visual Design | 7.6 | 8.2 | +0.6 |
| UX | 8.0 | 8.2 | +0.2 |
| Consistency | 7.7 | 8.5 | +0.8 |
| Responsiveness | 7.7 | 8.3 | +0.6 |
| Accessibility | 7.7 | 8.5 | +0.8 |
| Brand & Polish | 7.5 | 7.8 | +0.3 |

**Projected V3 Score**: 8.3/10

---

## Before/After Examples

### Typography Line-Heights

**Before:**
```css
body { line-height: 1.5; }
h1 { line-height: 1.1; }
h2 { line-height: 1.1; }
```

**After:**
```css
body { line-height: 1.6; }
h1 { line-height: 1.2; }
h2 { line-height: 1.25; }
h3 { line-height: 1.3; }
```

Impact: Improved readability, especially in dense content areas.

### Shadow Standardization

**Before:** Mix of values across cards
```css
/* Card A */ box-shadow: 0 1px 3px rgba(0,0,0,0.1);
/* Card B */ box-shadow: 0 2px 4px rgba(0,0,0,0.15);
/* Card C */ box-shadow: 0 1px 2px rgba(0,0,0,0.08);
```

**After:** Consistent scale
```css
--shadow-sm: 0 1px 2px rgba(0,0,0,0.05);
--shadow-md: 0 4px 6px rgba(0,0,0,0.07);
--shadow-lg: 0 10px 15px rgba(0,0,0,0.1);

.card { box-shadow: var(--shadow-md); }
```

### Mobile Task List Redesign

**Before:**
```
┌────────────────────┐
│ ○ Task name      > │  ← Small touch target
│   Due today       │
└────────────────────┘
```

**After:**
```
┌───────────────────────┐
│  ┌───┐                │
│  │   │  Task name     │  ← 48px touch target
│  │ ○ │                │
│  │   │  Acme • Today   │
│  └───┘                │
└───────────────────────┘
    ↑ Swipe left to complete/delete
```
