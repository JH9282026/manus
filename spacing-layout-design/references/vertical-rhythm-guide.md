# Vertical Rhythm Guide

Detailed guidance on establishing and maintaining vertical rhythm in UI design.

---

## What Is Vertical Rhythm?

Vertical rhythm is the consistent vertical spacing pattern created by aligning text and elements to a baseline grid. It creates a sense of order and visual harmony, similar to musical rhythm.

---

## Baseline Grid Setup

- **Base line-height**: 24px (for 16px body text × 1.5 line-height)
- **Grid unit**: 8px (allows both 8px and 24px alignment)
- All element heights and vertical spacing should be multiples of 8px

---

## Text Vertical Rhythm

```css
/* Body text */
body { font-size: 1rem; line-height: 1.6; }  /* 16px / 25.6px */

/* Headings */
h1 { font-size: 2.25rem; line-height: 1.2; margin-top: 0; margin-bottom: 2rem; }
h2 { font-size: 1.5rem; line-height: 1.25; margin-top: 2rem; margin-bottom: 1rem; }
h3 { font-size: 1.25rem; line-height: 1.3; margin-top: 2rem; margin-bottom: 1rem; }

/* Paragraphs */
p + p { margin-top: 1rem; }  /* 16px */

/* Lists */
ul, ol { margin: 1rem 0; }
li + li { margin-top: 0.5rem; }  /* 8px */
```

---

## Element Height Standards

All interactive elements should align to 8px increments:

| Element | Height | Grid Units |
|---------|--------|------------|
| Button sm | 32px | 4 × 8px |
| Button md | 40px | 5 × 8px |
| Button lg | 48px | 6 × 8px |
| Input field | 44px | Touch-friendly |
| Nav item | 40px | 5 × 8px |
| Table row | 48px | 6 × 8px |
| Avatar sm | 32px | 4 × 8px |
| Avatar md | 40px | 5 × 8px |
| Avatar lg | 48px | 6 × 8px |
| Toolbar | 56px | 7 × 8px |
| Header | 64px | 8 × 8px |

---

## Section Rhythm Pattern

Establish consistent vertical rhythm for page sections:

```
| 96px | ← Page top padding
|------|
| Page Title (H1)
| 32px |
|------|
| Section content
| 64px |
|------|
| Section content
| 64px |
|------|
| 96px | ← Page bottom padding
```

---

## Content Sections Rhythm

```css
.section-title {
  margin-bottom: 1.5rem;   /* 24px - space-6 */
}
.section-content > * + * {
  margin-top: 1rem;        /* 16px - space-4 */
}
```

---

## Common Rhythm Mistakes

1. **Inconsistent heading margins** — Use the same top/bottom margin for each heading level
2. **Breaking the grid** — Using odd pixel values (13px, 17px) that don't align
3. **Ignoring line-height** — Line-height affects total element height
4. **Collapsing margins confusion** — Adjacent vertical margins collapse in CSS; account for this
5. **Mixed units** — Mixing px and rem inconsistently; prefer rem for scalability
