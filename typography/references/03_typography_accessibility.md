# Typography Accessibility

## Overview

Accessible typography ensures text is readable and usable for all individuals, including those with visual impairments, dyslexia, cognitive challenges, or other disabilities. Following WCAG guidelines and best practices creates inclusive digital experiences.

## WCAG Guidelines for Typography

### 1. Contrast Ratios (WCAG 1.4.3)

**Minimum Requirements (Level AA)**:
- Normal text: 4.5:1 contrast ratio
- Large text (18pt/24px or 14pt/18.66px bold): 3:1 contrast ratio

**Enhanced (Level AAA)**:
- Normal text: 7:1 contrast ratio
- Large text: 4.5:1 contrast ratio

**Testing Tools**:
- WebAIM Color Contrast Checker
- Chrome DevTools
- WAVE Browser Extension
- Contrast Ratio Calculator

**Examples**:
```css
/* Good contrast */
.text-good {
  color: #222222; /* Dark gray */
  background: #FFFFFF; /* White */
  /* Ratio: 16.1:1 */
}

/* Minimum AA */
.text-minimum {
  color: #767676; /* Medium gray */
  background: #FFFFFF;
  /* Ratio: 4.54:1 */
}

/* Fails AA */
.text-fail {
  color: #AAAAAA; /* Light gray */
  background: #FFFFFF;
  /* Ratio: 2.85:1 - Too low */
}
```

### 2. Text Resizing (WCAG 1.4.4)

**Requirement**: Text must be resizable up to 200% without loss of content or functionality.

**Implementation**:
```css
/* Use relative units */
body {
  font-size: 1rem; /* 16px default */
}

h1 {
  font-size: 2.5rem; /* Scales with user settings */
}

/* Avoid fixed pixel sizes for containers */
.container {
  max-width: 70rem; /* Scales with text */
  /* NOT: max-width: 1120px; */
}
```

### 3. Text Spacing (WCAG 1.4.12)

**Requirements** (Level AA):
- Line height: At least 1.5× font size
- Paragraph spacing: At least 2× font size
- Letter spacing: At least 0.12× font size
- Word spacing: At least 0.16× font size

**Implementation**:
```css
body {
  font-size: 1rem;
  line-height: 1.6; /* 1.6× font size */
  letter-spacing: 0.02em; /* 0.12× font size */
  word-spacing: 0.16em; /* 0.16× font size */
}

p + p {
  margin-top: 2em; /* 2× font size */
}
```

### 4. Images of Text (WCAG 1.4.5)

**Requirement**: Use real text instead of images of text (except logos).

**Why**:
- Real text is scalable
- Can be customized by users
- Accessible to screen readers
- Better for SEO

**Exceptions**:
- Logos and branding
- Essential presentation (e.g., screenshots)

## Typeface Selection for Accessibility

### Recommended Characteristics

1. **Clear Letterforms**
   - Distinct characters (l, I, 1 easily distinguishable)
   - Open apertures (c, e, s)
   - Adequate x-height

2. **Sans-Serif for Screens**
   - Arial, Helvetica
   - Verdana
   - Open Sans
   - Roboto
   - Lato

3. **Avoid**:
   - Overly decorative fonts
   - Thin or light weights for body text
   - Fonts with similar-looking characters
   - All caps for long text

### Dyslexia-Friendly Typography

**Characteristics**:
- Larger x-height
- Distinct letter shapes
- Adequate spacing
- Medium weight (not too thin or bold)

**Fonts**:
- OpenDyslexic (specialized)
- Comic Sans (surprisingly effective)
- Verdana
- Arial
- Helvetica

**Best Practices**:
- Avoid justified text
- Use adequate line spacing (1.5-2.0)
- Limit line length (50-70 characters)
- Use clear hierarchy
- Avoid italics for long text

## Font Size Guidelines

### Minimum Sizes

**Body Text**:
- Minimum: 16px (1rem)
- Recommended: 16-18px
- Never below 14px

**Small Text**:
- Minimum: 14px
- Use sparingly
- Ensure higher contrast

**Headings**:
- H1: 2-3× body size
- H2: 1.5-2× body size
- H3: 1.25-1.5× body size

### Responsive Sizing

```css
/* Mobile */
body {
  font-size: 1rem; /* 16px */
}

/* Tablet and up */
@media (min-width: 768px) {
  body {
    font-size: 1.125rem; /* 18px */
  }
}

/* Desktop */
@media (min-width: 1024px) {
  body {
    font-size: 1.25rem; /* 20px */
  }
}
```

## Color and Contrast Best Practices

### Text Colors

**Dark Mode**:
```css
.dark-mode {
  background: #1a1a1a;
  color: #e0e0e0; /* Not pure white - reduces eye strain */
}
```

**Light Mode**:
```css
.light-mode {
  background: #ffffff;
  color: #222222; /* Not pure black - softer */
}
```

### Link Styling

**Requirements**:
- Don't rely on color alone
- Provide additional visual cue (underline, icon, etc.)

```css
a {
  color: #0066cc;
  text-decoration: underline;
}

a:hover {
  color: #0052a3;
  text-decoration: underline;
  background-color: #f0f8ff;
}

a:focus {
  outline: 2px solid #0066cc;
  outline-offset: 2px;
}
```

## Spacing for Readability

### Line Height

```css
/* Body text */
body {
  line-height: 1.6; /* 160% */
}

/* Headings */
h1, h2, h3 {
  line-height: 1.2-1.3;
}

/* Small text */
.small-text {
  line-height: 1.5;
}
```

### Line Length

```css
.content {
  max-width: 65ch; /* 65 characters */
  /* Or */
  max-width: 700px;
}
```

### Paragraph Spacing

```css
p {
  margin-bottom: 1.5em;
}

p + p {
  margin-top: 1em;
}
```

## Text Formatting

### Avoid

1. **All Caps for Long Text**
   - Harder to read
   - Screen readers may misinterpret
   - Use sparingly for short labels

2. **Justified Text**
   - Creates uneven word spacing
   - Difficult for dyslexic readers
   - Use left-aligned instead

3. **Excessive Italics**
   - Harder to read
   - Use for emphasis only
   - Avoid for long passages

4. **Excessive Bold**
   - Reduces readability
   - Use for emphasis and headings
   - Don't bold entire paragraphs

### Recommended

1. **Left-Aligned Text**
   - Most readable
   - Predictable line starts
   - Standard for body text

2. **Sentence Case**
   - Most readable
   - Natural reading pattern

3. **Clear Hierarchy**
   - Consistent heading styles
   - Logical structure
   - Proper HTML semantics

## Screen Reader Considerations

### Semantic HTML

```html
<!-- Good -->
<h1>Main Heading</h1>
<h2>Subheading</h2>
<p>Body text</p>

<!-- Bad -->
<div class="heading-large">Main Heading</div>
<div class="heading-medium">Subheading</div>
<div>Body text</div>
```

### ARIA Labels

```html
<button aria-label="Close dialog">×</button>

<span aria-hidden="true">→</span>
<span class="sr-only">Next page</span>
```

### Skip Links

```html
<a href="#main-content" class="skip-link">
  Skip to main content
</a>
```

## Testing for Accessibility

### Manual Testing

1. **Zoom to 200%**: Check if content remains usable
2. **Use keyboard only**: Tab through all interactive elements
3. **Test with screen reader**: NVDA, JAWS, VoiceOver
4. **Check contrast**: Use contrast checker tools
5. **Test with different fonts**: User may override
6. **Disable CSS**: Content should still make sense

### Automated Testing

**Tools**:
- WAVE (Web Accessibility Evaluation Tool)
- axe DevTools
- Lighthouse (Chrome DevTools)
- Pa11y
- ANDI (Accessible Name & Description Inspector)

### User Testing

- Include users with disabilities
- Test with assistive technologies
- Gather feedback on readability
- Iterate based on findings

## Accessibility Checklist

- [ ] Contrast ratios meet WCAG AA (4.5:1 for normal text)
- [ ] Text resizable to 200% without loss of functionality
- [ ] Font size minimum 16px for body text
- [ ] Line height at least 1.5 for body text
- [ ] Line length 50-75 characters
- [ ] No images of text (except logos)
- [ ] Links distinguishable without color alone
- [ ] Semantic HTML used for headings
- [ ] No justified text
- [ ] Limited use of all caps, italics, bold
- [ ] Clear visual hierarchy
- [ ] Adequate spacing between elements
- [ ] Focus indicators visible
- [ ] Content readable with CSS disabled

## Conclusion

Accessible typography is not just about compliance—it's about creating inclusive experiences for all users. By following WCAG guidelines, choosing appropriate typefaces, ensuring sufficient contrast, and testing with real users, you can create typography that is readable, usable, and welcoming to everyone.
