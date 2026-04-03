# Typography System: TaskFlow - Detailed Reference

Detailed reference content for typography.

---

## Typography System: TaskFlow
### Font Selection

**Primary Font: Inter**
- Why: Modern, highly readable, excellent for UI
- Variable font for performance
- Great number legibility (important for dashboards)
- Wide language support

**Alternative: Satoshi** (if more personality needed)
- Slightly more distinctive
- Same excellent readability

**Code Font: JetBrains Mono**
- Excellent for any code/technical content
- Clear number differentiation

### Type Scale (Major Third - 1.25)

| Token | Size | Line Height | Weight | Usage |
|-------|------|-------------|--------|-------|
| `text-display` | 48px | 1.1 | 700 | Marketing hero |
| `text-h1` | 36px | 1.2 | 700 | Page titles |
| `text-h2` | 28px | 1.25 | 600 | Section headings |
| `text-h3` | 22px | 1.3 | 600 | Card headings, modals |
| `text-h4` | 18px | 1.35 | 600 | Subsections |
| `text-lg` | 18px | 1.6 | 400 | Lead paragraphs |
| `text-base` | 16px | 1.6 | 400 | Body text |
| `text-sm` | 14px | 1.5 | 400 | Secondary text, forms |
| `text-xs` | 12px | 1.4 | 400 | Captions, timestamps |

### Complete Style Definitions

#### Headings

```css
/* H1 - Page Titles */
.text-h1 {
  font-family: 'Inter', sans-serif;
  font-size: 36px;
  font-weight: 700;
  line-height: 1.2;
  letter-spacing: -0.02em;
  color: #0F172A; /* Slate-900 */
}

/* H2 - Section Headings */
.text-h2 {
  font-family: 'Inter', sans-serif;
  font-size: 28px;
  font-weight: 600;
  line-height: 1.25;
  letter-spacing: -0.01em;
  color: #0F172A;
}

/* H3 - Card/Modal Headings */
.text-h3 {
  font-family: 'Inter', sans-serif;
  font-size: 22px;
  font-weight: 600;
  line-height: 1.3;
  letter-spacing: 0;
  color: #1E293B; /* Slate-800 */
}

/* H4 - Small Headings */
.text-h4 {
  font-family: 'Inter', sans-serif;
  font-size: 18px;
  font-weight: 600;
  line-height: 1.35;
  color: #1E293B;
}
```

#### Body Text

```css
/* Body - Default */
.text-body {
  font-family: 'Inter', sans-serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 1.6;
  color: #334155; /* Slate-700 */
}

/* Body Small - Secondary */
.text-sm {
  font-family: 'Inter', sans-serif;
  font-size: 14px;
  font-weight: 400;
  line-height: 1.5;
  color: #475569; /* Slate-600 */
}

/* Caption - Tertiary */
.text-caption {
  font-family: 'Inter', sans-serif;
  font-size: 12px;
  font-weight: 400;
  line-height: 1.4;
  color: #64748B; /* Slate-500 */
}
```

#### UI Elements

```css
/* Button Text */
.text-button {
  font-family: 'Inter', sans-serif;
  font-size: 14px;
  font-weight: 500;
  line-height: 1;
  letter-spacing: 0.02em;
}

/* Label */
.text-label {
  font-family: 'Inter', sans-serif;
  font-size: 14px;
  font-weight: 500;
  line-height: 1.4;
  color: #334155;
}

/* Overline */
.text-overline {
  font-family: 'Inter', sans-serif;
  font-size: 11px;
  font-weight: 500;
  line-height: 1.4;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: #64748B;
}

/* Link */
.text-link {
  font-weight: 500;
  color: #7C3AED; /* Violet-600 */
  text-decoration: underline;
  text-underline-offset: 2px;
}
.text-link:hover {
  color: #8B5CF6; /* Violet-500 */
}

/* Code Inline */
.text-code {
  font-family: 'JetBrains Mono', monospace;
  font-size: 14px;
  background: #F1F5F9;
  padding: 0.125em 0.375em;
  border-radius: 4px;
}
```

### Responsive Behavior

| Style | Mobile | Tablet | Desktop |
|-------|--------|--------|----------|
| H1 | 28px | 32px | 36px |
| H2 | 24px | 26px | 28px |
| H3 | 20px | 22px | 22px |
| Body | 16px | 16px | 16px |

```css
/* Fluid H1 */
.text-h1 {
  font-size: clamp(1.75rem, 3vw + 0.5rem, 2.25rem);
}
```

### Usage Guidelines

#### Hierarchy in Practice

```
Page Title (H1)
  Section (H2)
    Subsection (H3)
      Card title (H4)
        Body text
          Caption/meta
```

#### Reading Comfort
- Maximum line width: 65-75 characters
- Minimum body size: 16px
- Paragraph spacing: 1em (16px)
- Section spacing: 2-3em

#### Don't
- Never go below 12px for any text
- Don't use more than 3 font weights on one page
- Avoid centered text for paragraphs >3 lines
- Don't mix too many heading levels in one view
```

---
