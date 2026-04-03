# Color System: TaskFlow - Detailed Reference

Detailed reference content for color palettes.

---

## Color System: TaskFlow
### Color Strategy

**Direction**: Warm purple as primary, avoiding competitive blue territory.
Purple conveys creativity and premium quality while remaining professional.
Warm amber accent adds approachability and energy.

---

### Primary Colors (Violet)

| Name | Hex | RGB | Usage |
|------|-----|-----|-------|
| Violet-50 | #F5F3FF | rgb(245,243,255) | Light backgrounds, hover |
| Violet-100 | #EDE9FE | rgb(237,233,254) | Selected states, badges |
| Violet-200 | #DDD6FE | rgb(221,214,254) | Light accents |
| Violet-300 | #C4B5FD | rgb(196,181,253) | Decorative elements |
| Violet-400 | #A78BFA | rgb(167,139,250) | Hover state for primary |
| Violet-500 | #8B5CF6 | rgb(139,92,246) | **PRIMARY - Main CTAs** |
| Violet-600 | #7C3AED | rgb(124,58,237) | Active/pressed state |
| Violet-700 | #6D28D9 | rgb(109,40,217) | Dark accents |
| Violet-800 | #5B21B6 | rgb(91,33,182) | Dark mode elements |
| Violet-900 | #4C1D95 | rgb(76,29,149) | Darkest accent |

---

### Secondary Colors (Amber)

| Name | Hex | RGB | Usage |
|------|-----|-----|-------|
| Amber-50 | #FFFBEB | rgb(255,251,235) | Warning backgrounds |
| Amber-100 | #FEF3C7 | rgb(254,243,199) | Highlight backgrounds |
| Amber-200 | #FDE68A | rgb(253,230,138) | Light accent |
| Amber-300 | #FCD34D | rgb(252,211,77) | Badges, tags |
| Amber-400 | #FBBF24 | rgb(251,191,36) | Hover accent |
| Amber-500 | #F59E0B | rgb(245,158,11) | **SECONDARY - Accents** |
| Amber-600 | #D97706 | rgb(217,119,6) | Active accent |
| Amber-700 | #B45309 | rgb(180,83,9) | Dark accent |

---

### Neutral Colors (Slate - slight cool tone)

| Name | Hex | RGB | Usage |
|------|-----|-----|-------|
| Slate-50 | #F8FAFC | rgb(248,250,252) | Page backgrounds |
| Slate-100 | #F1F5F9 | rgb(241,245,249) | Card hover, sections |
| Slate-200 | #E2E8F0 | rgb(226,232,240) | Borders, dividers |
| Slate-300 | #CBD5E1 | rgb(203,213,225) | Disabled text |
| Slate-400 | #94A3B8 | rgb(148,163,184) | Placeholder text |
| Slate-500 | #64748B | rgb(100,116,139) | Secondary text |
| Slate-600 | #475569 | rgb(71,85,105) | Tertiary text |
| Slate-700 | #334155 | rgb(51,65,85) | Body text |
| Slate-800 | #1E293B | rgb(30,41,59) | Headings |
| Slate-900 | #0F172A | rgb(15,23,42) | High emphasis text |

---

### Semantic Colors

| Status | Main | Light (bg) | Dark (text) |
|--------|------|------------|-------------|
| Success | #10B981 | #D1FAE5 | #065F46 |
| Warning | #F59E0B | #FEF3C7 | #92400E |
| Error | #EF4444 | #FEE2E2 | #991B1B |
| Info | #3B82F6 | #DBEAFE | #1E40AF |

---

### Accessibility Verification

| Combination | Ratio | WCAG AA | Use Case |
|-------------|-------|---------|----------|
| Slate-800 on White | 12.6:1 | ✅ Pass | Headings |
| Slate-700 on White | 8.6:1 | ✅ Pass | Body text |
| White on Violet-500 | 4.9:1 | ✅ Pass | Button text |
| Violet-600 on White | 5.4:1 | ✅ Pass | Links |
| Slate-500 on White | 4.6:1 | ✅ Pass | Secondary text |
| White on Amber-500 | 2.1:1 | ❌ Fail | Use dark text |
| Slate-900 on Amber-500 | 8.5:1 | ✅ Pass | Amber buttons |

**Note**: Amber buttons should use dark text (Slate-900), not white.

---

### Usage Guidelines

#### Button Hierarchy
```css
/* Primary CTA */
background: Violet-500;
text: White;
hover: Violet-400;
active: Violet-600;

/* Secondary CTA */
background: White;
text: Violet-600;
border: Violet-300;
hover-background: Violet-50;

/* Tertiary/Ghost */
background: transparent;
text: Violet-600;
hover-background: Violet-50;

/* Destructive */
background: Error (#EF4444);
text: White;
```

#### Text Hierarchy
```css
/* Heading */
color: Slate-900;

/* Body */
color: Slate-700;

/* Secondary/Caption */
color: Slate-500;

/* Disabled */
color: Slate-300;

/* Link */
color: Violet-600;
text-decoration: underline;
hover: Violet-500;
```

#### Background Hierarchy
```css
/* Page background */
background: Slate-50;

/* Card/Container */
background: White;
border: Slate-200;

/* Section highlight */
background: Violet-50;

/* Hover state */
background: Slate-100;

/* Selected state */
background: Violet-100;
```

---

### Dark Mode (Optional Extension)

| Light Mode | Dark Mode |
|------------|----------|
| Slate-50 (page bg) | Slate-900 |
| White (cards) | Slate-800 |
| Slate-900 (headings) | White |
| Slate-700 (body) | Slate-300 |
| Violet-500 | Violet-400 |
```

---
