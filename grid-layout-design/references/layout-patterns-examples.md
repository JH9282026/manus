# Layout Patterns & Examples

Concrete layout pattern examples with ASCII diagrams for common page types.

---

## Dashboard Main Layout

```
Desktop:
┌───────┬──────────────────────────────────────┐
│ Side  │  Page Header (12 col)               │
│  bar  ├────────────┬────────────┬────────────┤
│       │   Stat     │    Stat    │   Stat     │
│       │  (4 col)   │  (4 col)   │  (4 col)   │
│       ├────────────┴────────────┴────────────┤
│       │                                        │
│       │   Main Content (12 col)                │
│       │                                        │
└───────┴──────────────────────────────────────┘

Mobile:
┌───────────────┐
│  [☰] Header  │
├───────────────┤
│  Stat (full)  │
├───────────────┤
│  Stat (full)  │
├───────────────┤
│  Main (full)  │
├───────────────┤
│  [Tab Bar]    │
└───────────────┘
```

---

## Task Detail with Side Panel

```
Desktop:
┌───────┬────────────────────┬──────────────┐
│ Side  │   Task List        │  Task Detail   │
│  bar  │   (7 col)          │   (5 col)      │
│       │                    │   Slides in    │
└───────┴────────────────────┴──────────────┘

Mobile: Full-screen overlay
```

---

## Project Card Grid

```
Desktop (4-column card grid):
│ Card (3col) │ Card (3col) │ Card (3col) │ Card (3col) │
│ Card (3col) │ Card (3col) │ Card (3col) │ Card (3col) │

Tablet (2-column):
│ Card (4col) │ Card (4col) │
│ Card (4col) │ Card (4col) │

Mobile (1-column):
│ Card (full)       │
│ Card (full)       │
```

---

## Landing Page Sections

### Hero Section
- Full viewport width, may break the grid for background
- Content centered within 8–10 columns
- Headline + subheadline + CTA group

### Feature Grid
- 3 features: 4+4+4 columns
- 4 features: 3+3+3+3 columns
- 2 features with illustration: 6+6 columns

### Testimonial Section
- Single testimonial: Centered 8 columns
- Multiple testimonials: 4+4+4 card grid
- Carousel: Full width with pagination

### CTA Section
- Centered 6–8 columns
- Background may span full width
- Clear visual hierarchy: headline → body → button

### Footer
- 4-column layout (3+3+3+3)
- Or 3-column (4+4+4)
- Logo and legal spanning full width below

---

## Form Layouts

### Single Column Form (Recommended)
- Max width: 480–560px (~6 columns)
- One field per row for clarity
- Labels above inputs

### Two Column Form
- For short, related fields (First name + Last name)
- 6+6 within the form container
- Never for unrelated fields

### Settings Page
- Label column (4 col) + Input column (8 col)
- Or full-width sections with grouped settings
