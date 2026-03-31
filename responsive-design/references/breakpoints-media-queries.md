# Breakpoints and Media Queries

## Standard Breakpoints
- Mobile: < 768px
- Tablet: 768px - 1023px  
- Desktop: 1024px - 1439px
- Large Desktop: \u2265 1440px

## Media Query Syntax
```css
@media (min-width: 768px) {
  /* Tablet and up */
}

@media (min-width: 1024px) and (max-width: 1439px) {
  /* Desktop only */
}

@media (orientation: landscape) {
  /* Landscape orientation */
}
```

## Best Practices
- Use min-width for mobile-first
- Use max-width for desktop-first
- Test between breakpoints
- Consider content, not just devices
- Use em/rem for breakpoints (accessibility)
