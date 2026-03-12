# Mobile UX & Performance

## Mobile Form Design

### Input Optimization
- Use appropriate input types (`tel`, `email`, `number`, `date`)
- Set `autocomplete` attributes for auto-fill
- Use `inputmode` for virtual keyboard optimization
- Show/hide password toggle
- Inline validation with clear error messages

### Form UX Patterns
| Pattern | Benefit |
|---------|---------|
| Single column layout | Reduces cognitive load |
| Floating labels | Saves vertical space |
| Progressive disclosure | Shows fields as needed |
| Auto-advance | Move to next field automatically |
| Smart defaults | Pre-fill common values |

---

## Mobile Navigation UX

### Bottom Navigation
- 3-5 items maximum
- Icons + labels (not icons alone)
- Active state clearly visible
- Persistent across all screens
- Most important items in center/right

### Gesture Navigation
- Swipe back: Return to previous screen
- Pull to refresh: Update content
- Swipe to dismiss: Remove items
- Pinch to zoom: Image/map detail
- Always provide button alternatives

---

## Performance Optimization

### Critical Rendering Path
1. **Inline critical CSS** — Above-fold styles in `<head>`
2. **Defer JavaScript** — `defer` or `async` attributes
3. **Preload key resources** — `<link rel="preload">`
4. **Lazy load images** — `loading="lazy"` attribute
5. **Font optimization** — `font-display: swap`, preload fonts

### Resource Hints
| Hint | Purpose | Example |
|------|---------|---------|
| `preload` | Load critical resource early | Fonts, hero images |
| `prefetch` | Load next-page resources | Next navigation target |
| `preconnect` | Establish early connection | CDN, API domains |
| `dns-prefetch` | Resolve DNS early | Third-party domains |

### JavaScript Optimization
- Code split by route/component
- Tree shake unused code
- Compress with Brotli (preferred) or gzip
- Use web workers for heavy computation
- Avoid layout thrashing (batch DOM reads/writes)

### Image Optimization Checklist
- [ ] Serve modern formats (WebP/AVIF)
- [ ] Responsive images with srcset
- [ ] Lazy load below-fold images
- [ ] Proper dimensions set (prevent CLS)
- [ ] Compress to quality 80-85%
- [ ] Use CDN for delivery
