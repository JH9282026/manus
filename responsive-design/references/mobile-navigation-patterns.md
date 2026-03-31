# Mobile Navigation Patterns

## Hamburger Menu

### HTML Structure
```html
<button class="menu-toggle" aria-label="Toggle menu">
  <span></span>
  <span></span>
  <span></span>
</button>
<nav class="main-nav">
  <ul>
    <li><a href="#">Home</a></li>
    <li><a href="#">About</a></li>
    <li><a href="#">Contact</a></li>
  </ul>
</nav>
```

### CSS
```css
.main-nav {
  display: none;
}

.main-nav.open {
  display: block;
}

@media (min-width: 768px) {
  .menu-toggle {
    display: none;
  }
  
  .main-nav {
    display: block;
  }
}
```

## Off-Canvas Menu
- Navigation slides in from side
- Overlay or push content
- Smooth transitions

## Bottom Navigation
- Fixed navigation at bottom
- Common in mobile apps
- Easy thumb access

## Priority+ Navigation
- Show important items
- Hide others in "More" menu
- Adapts to available space

## Best Practices
- Touch-friendly targets (44x44px)
- Clear visual feedback
- Accessible (keyboard, screen readers)
- Fast and smooth animations
- Close button clearly visible
