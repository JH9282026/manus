# JavaScript Libraries & Tools

## D3.js
- Data binding: .data() joins data to DOM
- Enter/Update/Exit pattern
- Scales: map data to visual properties
- Axes, transitions, event handling
- Workflow: load data -> SVG -> scales -> binddata -> style -> axes -> interactions

## Chart.js
- Canvas-based, good performance
- Built-in: bar, line, pie, doughnut, radar, scatter
- Responsive by default; plugin system

## Scrollytelling Libraries
- Scrollama: lightweight, Intersection Observer
- GSAP ScrollTrigger: animation-focused

## Performance
- Canvas for 1000+ points; SVG for <1000
- Lazy load below-fold visualizations
- Debounce resize/scroll events
- requestAnimationFrame for animation
- Target 60fps

## Responsive Design
- SVG viewBox for scaling
- Adjust dimensions with window.innerWidth
- Larger touch targets on mobile
- Separate mobile versions for complex charts

## Web Technologies
- SVG: scalable, accessible, <1000 elements
- Canvas: performant, pixel-based, large datasets
- WebGL: 3D, GPU-accelerated (Three.js)
