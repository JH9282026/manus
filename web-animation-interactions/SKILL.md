---
name: web-animation-interactions
description: "Implement performant web animations and micro-interactions using CSS and JavaScript. Use for: CSS animations, JavaScript animation libraries, scroll-triggered effects, hover interactions, page transitions, loading animations, SVG animation, and performance-optimized motion for websites and web applications."
---

# Web Animation & Interactions

Implement smooth, performant web animations and micro-interactions that enhance user experience without compromising page performance.

## Overview

Web animations guide user attention, provide feedback, communicate state changes, and add personality to interfaces. Done well, they feel invisible — things just "work smoothly." Done poorly, they cause jank, drain batteries, and annoy users. This skill covers CSS animations, JavaScript animation libraries, scroll-triggered effects, SVG animation, performance optimization, and the design principles behind effective web motion.

## Animation Technology Selection

| Technology | Best For | Performance | Learning Curve | Reference |
|-----------|----------|-------------|---------------|-----------|
| CSS Transitions | Simple state changes (hover, focus) | Excellent (GPU) | Easy | `/references/css-animations.md` |
| CSS @keyframes | Looping, multi-step animations | Excellent (GPU) | Easy | `/references/css-animations.md` |
| Web Animations API | Programmatic control of CSS-like animations | Excellent | Medium | `/references/javascript-animation.md` |
| GSAP (GreenSock) | Complex timelines, scroll, SVG, morphing | Excellent | Medium | `/references/javascript-animation.md` |
| Framer Motion | React component animations | Good | Easy (React) | `/references/javascript-animation.md` |
| Lottie | After Effects → web animations | Good | Easy (playback) | `/references/javascript-animation.md` |
| Three.js | 3D web animations | Variable | Steep | `/references/javascript-animation.md` |
| CSS View Transitions API | Page/component transitions | Excellent | Medium | `/references/css-animations.md` |

### Decision Guide

| Scenario | Recommended Approach |
|----------|---------------------|
| Button hover effect | CSS Transition |
| Loading spinner | CSS @keyframes |
| Scroll-triggered reveal | GSAP + ScrollTrigger or Intersection Observer |
| Page route transition | View Transitions API or Framer Motion |
| Complex multi-element timeline | GSAP Timeline |
| Icon animation from After Effects | Lottie |
| SVG path drawing | CSS stroke-dashoffset or GSAP DrawSVG |
| Physics-based drag/spring | Framer Motion or GSAP |

## CSS Animation Patterns

### Performant Properties (GPU-Accelerated)

| Property | Performance | Use For |
|----------|-------------|---------|
| `transform: translate()` | ✅ Excellent | Movement, sliding |
| `transform: scale()` | ✅ Excellent | Grow/shrink effects |
| `transform: rotate()` | ✅ Excellent | Spinning, tilting |
| `opacity` | ✅ Excellent | Fade in/out |
| `filter` | ⚠️ Good (modern browsers) | Blur, brightness |

### Properties to Avoid Animating

| Property | Why | Alternative |
|----------|-----|-------------|
| `width`, `height` | Triggers layout recalculation | Use `transform: scale()` |
| `top`, `left`, `right`, `bottom` | Triggers layout | Use `transform: translate()` |
| `margin`, `padding` | Triggers layout | Use `transform: translate()` |
| `border-radius` | Triggers paint | Avoid animating, or use `clip-path` |
| `box-shadow` | Triggers paint | Use pseudo-element with `opacity` |

### Common CSS Animation Recipes

| Animation | CSS Pattern | Duration | Easing |
|-----------|------------|----------|--------|
| Fade in on load | `opacity: 0 → 1` | 300–500ms | `ease-out` |
| Slide up entry | `translateY(20px) → 0` + fade | 400–600ms | `ease-out` |
| Scale on hover | `scale(1) → scale(1.05)` | 200ms | `ease-in-out` |
| Skeleton loading | `background-position` shimmer | 1.5–2s loop | `linear` |
| Pulse/breathing | `scale(1) → scale(1.05) → scale(1)` | 2s loop | `ease-in-out` |
| Shake (error) | `translateX` oscillation | 400ms | `ease-in-out` |

## Scroll Animation Patterns

| Pattern | Trigger | Implementation | Reference |
|---------|---------|---------------|-----------|
| Reveal on scroll | Element enters viewport | Intersection Observer + CSS class | `/references/interaction-patterns.md` |
| Parallax | Scroll position | `transform: translateY` tied to scroll | `/references/interaction-patterns.md` |
| Progress indicator | Scroll depth | Width tied to `scrollY / scrollHeight` | `/references/interaction-patterns.md` |
| Sticky + animate | Element becomes sticky | `position: sticky` + Intersection Observer | `/references/interaction-patterns.md` |
| Scroll-linked animation | Continuous during scroll | CSS `animation-timeline: scroll()` or GSAP ScrollTrigger | `/references/interaction-patterns.md` |

### Intersection Observer Setup
- **threshold:** 0.1–0.2 (trigger when 10–20% visible)
- **rootMargin:** "0px 0px -100px 0px" (trigger slightly before entering view)
- **Pattern:** Add `.is-visible` class → CSS handles the animation
- **Unobserve after triggering** for one-shot animations (saves performance)

## Micro-Interaction Design Principles

| Principle | Implementation | Example |
|-----------|---------------|---------|
| Immediate feedback | <100ms response to user input | Button press state change |
| Natural motion | Use ease-out for entries, ease-in for exits | Card appearing, modal closing |
| Purposeful | Every animation should serve a function | Don't animate for decoration |
| Consistent timing | Similar actions take similar durations | All cards reveal at same speed |
| Interruptible | User can cancel mid-animation | Dismissing a notification during entry |

### Duration Guidelines

| Action | Duration | Rationale |
|--------|----------|-----------|
| Micro-interaction (hover, click) | 100–200ms | Must feel instant |
| Element transition (expand, slide) | 200–400ms | Perceptible but quick |
| Page/view transition | 300–500ms | Enough to orient the user |
| Complex animation (modal, drawer) | 300–600ms | Full motion arc |
| Decorative/ambient | 1–3s | Background, non-blocking |

## Performance Optimization

| Technique | Impact | Implementation |
|-----------|--------|---------------|
| Use `will-change` sparingly | Promotes to GPU layer | Add only on elements about to animate |
| Prefer `transform` and `opacity` | Avoids layout/paint | Replace margin/width animations |
| Use `requestAnimationFrame` | Syncs with display refresh | For JS-driven animations |
| Debounce scroll handlers | Prevents layout thrash | `requestAnimationFrame` wrapper |
| Reduce animated element count | Linear performance cost | Animate containers, not children |
| Test on low-end devices | Catches jank early | Use Chrome DevTools CPU throttle |
| Respect `prefers-reduced-motion` | Accessibility requirement | `@media (prefers-reduced-motion: reduce)` |

## Best Practices

- **Always respect `prefers-reduced-motion`** — disable or simplify animations for users who request it
- **Animate only `transform` and `opacity`** unless you have a specific reason not to
- **Keep total animation time under 500ms** for functional transitions — longer = sluggish
- **Use GSAP for complex timelines** — managing staggered, sequenced animations in raw CSS/JS is error-prone
- **Test at 60fps** — use Chrome DevTools Performance panel to verify no dropped frames
- **Design the animation last** — get the interaction working, then add motion polish

## Using the Reference Files

**`/references/css-animations.md`** — Read when implementing CSS transitions, keyframe animations, or the View Transitions API. Covers performant property animation, easing functions, and CSS-only patterns.

**`/references/javascript-animation.md`** — Read when using GSAP, Framer Motion, Lottie, or Web Animations API. Covers timeline orchestration, library setup, and framework integration.

**`/references/interaction-patterns.md`** — Read when designing scroll animations, micro-interactions, or page transitions. Covers Intersection Observer, scroll-linked patterns, and motion design principles.

**`/references/performance-optimization.md`** — Read when animations cause jank or need optimization. Covers GPU compositing, `will-change`, reduced motion, and profiling tools.
