# Accessibility, Contrast, and WCAG Standards - Color Palette Design

## Introduction

This reference provides comprehensive guidance on designing accessible color systems that meet WCAG (Web Content Accessibility Guidelines) standards. Use this when verifying contrast ratios, building accessible palettes, accommodating color vision deficiencies, or ensuring your color system passes compliance audits.

---

## WCAG Color Requirements Overview

### What WCAG Requires

The Web Content Accessibility Guidelines (WCAG) 2.1 and 2.2 establish minimum standards for color accessibility. These are legally required in many jurisdictions (ADA in the US, EAA in the EU, AODA in Canada).

### Relevant Success Criteria

| Criterion | Level | Requirement |
|-----------|-------|-------------|
| **1.4.1 Use of Color** | A | Color is not the only visual means of conveying information |
| **1.4.3 Contrast (Minimum)** | AA | 4.5:1 for normal text, 3:1 for large text |
| **1.4.6 Contrast (Enhanced)** | AAA | 7:1 for normal text, 4.5:1 for large text |
| **1.4.11 Non-Text Contrast** | AA | 3:1 for UI components and graphical objects |

### Understanding Contrast Ratios

Contrast ratio measures the relative luminance difference between two colors. The scale runs from 1:1 (identical colors) to 21:1 (black on white).

**How it's calculated**:
```
Contrast Ratio = (L1 + 0.05) / (L2 + 0.05)
Where L1 = lighter color relative luminance
      L2 = darker color relative luminance
```

Relative luminance accounts for the human eye's different sensitivity to red, green, and blue light:
```
L = 0.2126 × R + 0.7152 × G + 0.0722 × B
(where R, G, B are linearized sRGB values)
```

---

## Contrast Requirements by Use Case

### Text Contrast

| Text Type | Definition | WCAG AA | WCAG AAA |
|-----------|-----------|---------|----------|
| Normal text | Below 18pt (24px) or below 14pt (18.66px) bold | 4.5:1 | 7:1 |
| Large text | 18pt+ (24px+) or 14pt+ (18.66px+) bold | 3:1 | 4.5:1 |
| Incidental text | Decorative, disabled, or part of inactive UI | No requirement | No requirement |
| Logotypes | Text in logos or brand names | No requirement | No requirement |

### Non-Text Contrast (WCAG 2.1+)

| Element | Minimum Ratio | Examples |
|---------|--------------|----------|
| UI components | 3:1 | Buttons, form inputs, toggle switches |
| Focus indicators | 3:1 | Keyboard focus rings, outlines |
| Graphical objects | 3:1 | Icons, chart elements, infographics |
| State indicators | 3:1 | Selected tabs, active menu items |

### Practical Contrast Targets

For production design systems, target higher ratios than the minimums:

| Use Case | Target Ratio | Why |
|----------|-------------|-----|
| Body text on backgrounds | 7:1+ | Comfortable reading for extended periods |
| Headings on backgrounds | 4.5:1+ | Clear hierarchy even at larger sizes |
| Button text on button fill | 4.5:1+ | Readable across all button variants |
| Placeholder text | 4.5:1 | Controversial — some designers use 3:1 for placeholders |
| Disabled elements | Not required | But should still be recognizable as UI elements |
| Icons with meaning | 3:1+ | Critical for icon-only buttons |
| Chart/graph elements | 3:1+ | Each data series distinguishable |

---

## Color Vision Deficiency (CVD)

### Types and Prevalence

Approximately 8% of men and 0.5% of women have some form of color vision deficiency.

| Type | Prevalence | Affected Colors | Impact |
|------|-----------|----------------|--------|
| **Deuteranopia** (green-blind) | ~1% of males | Red-green confusion | Most common severe CVD |
| **Deuteranomaly** (green-weak) | ~5% of males | Red-green reduced | Most common overall |
| **Protanopia** (red-blind) | ~1% of males | Red-green confusion, red appears dark | Critical for error states |
| **Protanomaly** (red-weak) | ~1% of males | Red-green reduced | Moderate impact |
| **Tritanopia** (blue-blind) | ~0.003% | Blue-yellow confusion | Rare but impacts some palettes |
| **Achromatopsia** (total) | ~0.003% | No color perception | Must rely entirely on non-color cues |

### Design Strategies for CVD

**Never rely on color alone** (WCAG 1.4.1):
- Add icons to status messages (✓ success, ⚠ warning, ✕ error)
- Use patterns or textures in charts and graphs
- Include text labels alongside color indicators
- Use shape differences (filled vs. outlined, solid vs. dashed)

**Safe color combinations**:
- Blue and orange (distinguishable by most CVD types)
- Blue and yellow (high contrast across all CVD types)
- Dark blue and light gray (safe neutral pairing)
- Avoid: Red-green pairs without additional differentiation
- Avoid: Green-brown or green-gray pairs

**Testing approach**:
1. Simulate deuteranopia and protanopia for all color-dependent UI
2. Verify that meaning is preserved without color
3. Check that adjacent colors in charts/graphs remain distinguishable
4. Test focus states and selected states under simulation

---

## Building Accessible Palettes

### Step 1: Establish Contrast-Safe Neutrals

Your neutral scale is the backbone of accessibility. Define it with contrast ratios in mind:

| Token | Hex Example | Use | Contrast vs White | Contrast vs Gray-900 |
|-------|------------|-----|-------------------|----------------------|
| Gray-50 | #F8FAFC | Page background | 1.07:1 | 15.4:1 |
| Gray-100 | #F1F5F9 | Card background | 1.16:1 | 14.2:1 |
| Gray-200 | #E2E8F0 | Borders, dividers | 1.41:1 | 11.6:1 |
| Gray-300 | #CBD5E1 | Disabled text bg | 1.84:1 | 8.9:1 |
| Gray-400 | #94A3B8 | Placeholder text | 3.28:1 | 5.0:1 |
| Gray-500 | #64748B | Secondary text | 5.39:1 | 3.1:1 |
| Gray-600 | #475569 | Body text | 7.45:1 | 2.2:1 |
| Gray-700 | #334155 | Primary text | 10.09:1 | 1.6:1 |
| Gray-800 | #1E293B | Headings | 13.44:1 | 1.2:1 |
| Gray-900 | #0F172A | Maximum contrast | 16.46:1 | 1:1 |

### Step 2: Verify Primary Color Accessibility

For every primary/accent color, determine:
- Which neutral backgrounds it can safely sit on as text
- Which text colors can sit on it as a background
- Whether it meets the 3:1 minimum as a UI component color

**Primary color checklist**:
```
Primary-500 on White    → Must be ≥ 4.5:1 for text use
White on Primary-500    → Must be ≥ 4.5:1 for button text
Primary-500 on Gray-100 → Must be ≥ 3:1 for UI components
Primary-700 on White    → Should be ≥ 7:1 for body text links
```

### Step 3: Semantic Colors with Accessibility

| Semantic | Light Theme Text Color | Dark Background | Light Background | Alt Indicator |
|----------|----------------------|-----------------|------------------|---------------|
| Success | #15803D (green-700) | #22C55E | #DCFCE7 | ✓ checkmark icon |
| Warning | #A16207 (yellow-700) | #EAB308 | #FEF9C3 | ⚠ triangle icon |
| Error | #B91C1C (red-700) | #EF4444 | #FEE2E2 | ✕ or ! icon |
| Info | #1D4ED8 (blue-700) | #3B82F6 | #DBEAFE | ℹ info icon |

Use the 700-shade for text on light backgrounds — it typically achieves 4.5:1+ on white.

---

## Dark Mode Accessibility

### Unique Challenges

Dark mode introduces specific contrast issues:

- **White text on dark backgrounds**: Pure white (#FFFFFF) on pure black (#000000) is 21:1 — too harsh for extended reading. Use off-white (#E2E8F0) on dark gray (#1E293B) for comfortable contrast (~11:1).
- **Vibrant colors on dark backgrounds**: Saturated colors that work on white may fail contrast on dark gray. Shift to lighter tints (300-400 range).
- **Semantic colors**: Red-500 on dark gray may pass contrast, but red-500 on black may be too vibrant. Test each combination.

### Dark Mode Contrast Strategy

| Element | Light Mode | Dark Mode | Notes |
|---------|-----------|-----------|-------|
| Body text | Gray-700 on White | Gray-200 on Gray-900 | Both achieve ~10:1 |
| Secondary text | Gray-500 on White | Gray-400 on Gray-900 | Both achieve ~5:1 |
| Primary accent | Primary-600 on White | Primary-300 on Gray-900 | Shift to lighter tint |
| Borders | Gray-200 | Gray-700 | Same relative contrast |
| Card surface | White | Gray-800 | Elevation through lightness |

---

## Testing Tools and Workflow

### Automated Testing Tools

| Tool | Type | Best For |
|------|------|----------|
| **WebAIM Contrast Checker** | Web | Quick manual checks of two colors |
| **Stark** | Figma/Sketch plugin | In-design contrast checking and CVD simulation |
| **axe DevTools** | Browser extension | Full-page automated accessibility audit |
| **Lighthouse** | Chrome built-in | Automated contrast scanning |
| **Colour Contrast Analyser (CCA)** | Desktop app | Eyedropper-based testing on any screen |
| **Polypane** | Browser | Side-by-side CVD simulation |
| **Who Can Use** | Web | Shows contrast + CVD simulation together |

### Testing Workflow

1. **During design**: Use Stark or Figma's built-in contrast checker for every text/background combination
2. **During development**: Run axe DevTools on every page to catch contrast issues
3. **Before release**: Full Lighthouse audit + manual CVD simulation review
4. **Ongoing**: Automated CI/CD checks with axe-core or pa11y

### Manual Testing Checklist

```
□ All body text meets 4.5:1 on its background
□ All large text/headings meet 3:1 on their background
□ All interactive elements (buttons, links, inputs) meet 3:1
□ Focus indicators meet 3:1 against adjacent colors
□ Error, success, and warning states are distinguishable without color
□ Charts and data visualizations work in grayscale
□ Dark mode combinations independently verified
□ CVD simulation shows no information loss
□ Disabled states are visually distinct from active states
```

---

## Common Accessibility Failures and Fixes

| Failure | Example | Fix |
|---------|---------|-----|
| Light gray text on white | #9CA3AF on #FFFFFF (2.7:1) | Darken to #6B7280 (4.6:1) |
| Colored text on colored bg | Blue link on blue-tinted card | Use darker blue or add underline |
| Placeholder too light | #CBD5E1 placeholder (1.8:1) | Use #6B7280 or add visible label |
| Icon-only button no contrast | Gray icon on gray bg | Ensure 3:1 minimum for the icon |
| Red/green only differentiation | Red=error, green=success | Add icons and text labels |
| Focus ring matches background | Blue focus on blue button | Use white or offset ring |
| Chart colors indistinguishable | 5 similar hues in pie chart | Use patterns, labels, or high-contrast palette |

---

## APCA (Advanced Perceptual Contrast Algorithm)

APCA is the next-generation contrast algorithm being considered for WCAG 3.0. Key differences from current WCAG 2.x:

- **Polarity-aware**: Distinguishes dark-on-light from light-on-dark (they are not perceptually equal)
- **Font-size aware**: Contrast requirements scale with font size and weight
- **More accurate**: Better correlates with actual human perception

**APCA Lightness Contrast (Lc) targets**:
| Use Case | Minimum Lc Value |
|----------|------------------|
| Body text (16px, 400 weight) | Lc 75 |
| Large text (24px+, 700 weight) | Lc 45 |
| Non-text UI elements | Lc 30 |
| Placeholder/disabled | Lc 30 |

**Current recommendation**: Design to WCAG 2.x AA standards (legally required), but also test with APCA for forward-compatibility.

---

## Key Takeaways

1. WCAG AA is the legal minimum — target higher ratios for comfortable reading
2. Non-text contrast (3:1 for UI elements) is often overlooked but equally important
3. Never use color as the sole means of conveying information
4. Test with CVD simulation, not just contrast ratios
5. Dark mode requires independent contrast verification — don't assume light mode values transfer
6. Automate contrast testing in your CI/CD pipeline to catch regressions
7. APCA is coming — designing above WCAG 2.x minimums prepares you for WCAG 3.0
