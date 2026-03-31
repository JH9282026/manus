# Responsive Images and Media

## Responsive Images

### Basic Responsive Image
```css
img {
  max-width: 100%;
  height: auto;
}
```

### Srcset Attribute
```html
<img src="small.jpg"
     srcset="small.jpg 480w, medium.jpg 768w, large.jpg 1024w"
     sizes="(max-width: 768px) 100vw, 50vw"
     alt="Description">
```

### Picture Element
```html
<picture>
  <source media="(min-width: 1024px)" srcset="large.jpg">
  <source media="(min-width: 768px)" srcset="medium.jpg">
  <img src="small.jpg" alt="Description">
</picture>
```

## Responsive Video

### Fluid Video
```css
video {
  max-width: 100%;
  height: auto;
}
```

### Aspect Ratio Container
```css
.video-container {
  aspect-ratio: 16 / 9;
  width: 100%;
}
```

## Performance
- Lazy loading: loading="lazy"
- Modern formats: WebP, AVIF
- Image CDNs for optimization
- Appropriate sizing for device
