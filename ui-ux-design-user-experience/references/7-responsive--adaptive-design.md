
### Mobile-First Design

**What Is It?**
Designing for mobile screens first, then progressively enhancing for larger screens.

**Why Mobile-First?**
- Forces content prioritization
- Better performance on mobile devices
- Easier to scale up than scale down
- Mobile traffic exceeds desktop globally

**Process:**
1. Design for smallest screen
2. Identify core content and features
3. Add complexity for larger screens
4. Test across device sizes

### Breakpoints

**Common Breakpoints:**
- Mobile: 320-480px
- Tablet: 481-768px
- Laptop: 769-1024px
- Desktop: 1025-1200px
- Large Desktop: 1201px+

**Strategy:**
- Design for content, not devices
- Let content determine breakpoints
- Test on real devices when possible

### Flexible Grids

- **Fluid Grids**: Percentage-based widths, scale proportionally
- **CSS Grid**: Two-dimensional layout system
- **Flexbox**: One-dimensional layout, flexible distribution
- **Responsive Grid**: Fixed columns with fluid gutters

### Responsive Images

**Techniques:**
- `srcset` and `sizes` attributes for multiple resolutions
- `<picture>` element for art direction
- CSS `object-fit` for container fitting

**Optimization:**
- Use modern formats (WebP, AVIF)
- Lazy loading for below-fold images
- Responsive image CDNs (Cloudinary, Imgix)

### Progressive Enhancement

Build core functionality first, then add advanced features for capable browsers:
1. Semantic HTML (baseline functionality)
2. CSS for presentation (enhanced visuals)
3. JavaScript for interactivity (advanced features)

---
