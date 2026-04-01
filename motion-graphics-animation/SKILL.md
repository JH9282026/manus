---
name: motion-graphics-animation
description: "Create professional motion graphics and animations for video, broadcast, and digital media. Use for: title sequences, logo animations, explainer videos, lower thirds, kinetic typography, data visualization animation, broadcast graphics, social media animations, and UI motion design."
---

# Motion Graphics & Animation

Create professional motion graphics for broadcast, digital media, explainer videos, and brand content using animation principles and industry-standard tools.

## Overview

Motion graphics combine graphic design with animation to communicate ideas visually through movement. Unlike character animation, motion graphics focus on abstract shapes, typography, data, icons, and branded elements. This skill covers the creative and technical workflow: from concept and storyboarding through animation principles, software techniques, and export optimization for every delivery platform.

## Project Type Selection Guide

| Project Type | Duration | Complexity | Tools | Deliverables | Reference |
|-------------|----------|-----------|-------|-------------|-----------|
| Logo reveal/animation | 3–5 sec | Low–Medium | After Effects, Cinema 4D | MP4, GIF, Lottie | `/references/animation-principles.md` |
| Lower third | 5–10 sec | Low | After Effects | MP4 with alpha | `/references/software-techniques.md` |
| Title sequence | 15–60 sec | High | After Effects, Cinema 4D | ProRes 4444 | `/references/design-styles.md` |
| Explainer video | 60–120 sec | High | After Effects, Illustrator | MP4 1080p/4K | `/references/workflow-optimization.md` |
| Kinetic typography | 15–60 sec | Medium | After Effects | MP4, social crops | `/references/animation-principles.md` |
| Data visualization animation | 10–60 sec | Medium–High | After Effects, D3.js | MP4 or web embed | `/references/design-styles.md` |
| Social media animation | 5–15 sec | Low–Medium | After Effects, Canva | MP4, GIF, square/vertical | `/references/workflow-optimization.md` |
| UI animation prototype | Variable | Medium | After Effects, Principle, Figma | GIF, Lottie, prototype | `/references/software-techniques.md` |

## Animation Principles for Motion Graphics

### The 12 Principles (Applied to MoGraph)

| Principle | Application in Motion Graphics | Priority |
|-----------|-------------------------------|----------|
| Ease in/ease out | Apply to every movement — never use linear keyframes | Critical |
| Anticipation | Small pull-back before a move (scale down before up) | High |
| Follow-through & overlap | Elements don't stop simultaneously — stagger arrivals | High |
| Staging | Guide eye to focal point, dim/blur secondary elements | High |
| Timing & spacing | Fast = energetic, slow = elegant — match brand tone | Critical |
| Exaggeration | Overshoot on bouncy animations, slight rotation on slides | Medium |
| Secondary action | Subtle shadow, particle trail, or glow on primary motion | Medium |
| Squash & stretch | For playful/cartoon styles — scale X/Y on impact | Style-dependent |

### Keyframe Technique Quick Reference

| Motion Feel | Ease Type | Graph Shape | When to Use |
|------------|-----------|-------------|-------------|
| Natural/default | Ease Ease (F9) | S-curve | Most general motion |
| Snappy/energetic | Fast out, slow in | Sharp ease-in | UI interactions, modern brands |
| Elegant/slow | Slow out, slow in | Wide S-curve | Luxury brands, cinematic |
| Bouncy | Overshoot expression | Oscillating curve | Playful, youthful brands |
| Mechanical/robotic | Linear | Straight line | Intentional only — tech/futuristic |

## Design Style Framework

| Style | Characteristics | Tools | Best For | Reference |
|-------|----------------|-------|----------|-----------|
| Flat/2D | Bold colors, sharp edges, no shadows | Illustrator → After Effects | Explainers, corporate, startups | `/references/design-styles.md` |
| Isometric | 3D look from 2D assets, 30° angles | Illustrator → After Effects | Tech, data, architecture | `/references/design-styles.md` |
| 3D/Cinema 4D | True 3D models, lighting, materials | Cinema 4D, Blender → AE | Premium brands, product launch | `/references/design-styles.md` |
| Liquid/morphing | Organic blob shapes, smooth transitions | After Effects shape layers | Creative agencies, music | `/references/design-styles.md` |
| Kinetic type | Typography as primary design element | After Effects text animators | Quotes, podcasts, social content | `/references/animation-principles.md` |
| Line art/hand-drawn | Illustrated, sketchy, stroke animations | Illustrator → AE (trim paths) | Education, storytelling | `/references/design-styles.md` |
| Retro/vintage | Grain, halftone, limited color palette | After Effects + textures | Nostalgia, food/beverage brands | `/references/design-styles.md` |

## After Effects Core Workflow

### Project Setup

| Setting | Standard | High-Quality | Social Media |
|---------|----------|-------------|--------------|
| Resolution | 1920×1080 | 3840×2160 | 1080×1080 or 1080×1920 |
| Frame rate | 30fps | 24fps (cinematic) or 60fps (smooth) | 30fps |
| Color depth | 8bpc | 16bpc or 32bpc | 8bpc |
| Duration | Project-dependent | — | 5–60 seconds |
| Background | Solid color or transparent | — | Platform-dependent |

### Essential Techniques

| Technique | Purpose | Tool/Feature |
|-----------|---------|-------------|
| Pre-composition | Organize and nest layers | Pre-compose (Ctrl/Cmd+Shift+C) |
| Expressions | Automate repetitive animation | `loopOut()`, `wiggle()`, `valueAtTime()` |
| Shape layer animation | Animate vector graphics natively | Trim paths, merge paths, repeater |
| Track mattes | Reveal/hide with masks | Alpha matte, luma matte |
| Adjustment layers | Apply effects globally | Add above content layers |
| Master properties | Reusable templates with editable fields | Essential Graphics panel |
| Mocha tracking | Advanced planar tracking | Built-in or Mocha Pro |

### Commonly Used Expressions

| Expression | Effect | Usage |
|-----------|--------|-------|
| `loopOut("cycle")` | Repeats animation infinitely | Rotating icons, pulsing elements |
| `wiggle(freq, amp)` | Random organic movement | Camera shake, handheld feel |
| `ease(time, t1, t2, v1, v2)` | Smooth interpolation | Custom easing curves |
| `valueAtTime(time - delay)` | Offset animation timing | Staggered reveals |
| `Math.round(effect("Slider")("Slider"))` | Animate counting numbers | Data visualization, counters |

## Export Specifications

| Destination | Format | Codec | Resolution | Frame Rate |
|-------------|--------|-------|-----------|------------|
| YouTube/Vimeo | MP4 | H.264 (High Profile) | 1080p or 4K | 24–30fps |
| Instagram Feed | MP4 | H.264 | 1080×1080 or 1080×1350 | 30fps |
| Instagram Stories/Reels | MP4 | H.264 | 1080×1920 | 30fps |
| Broadcast/TV | MOV | ProRes 422 HQ | 1080p or 4K | 23.976/29.97fps |
| Web (with alpha) | MOV | ProRes 4444 or WebM VP9 | Project size | 30fps |
| Web animation | Lottie JSON | — | Vector | 30–60fps |
| GIF (limited use) | GIF | — | ≤600px wide | 15fps |

## Best Practices

- **Never use linear keyframes** — always add easing; linear motion looks robotic and unpolished
- **Stagger everything** — offset element timing by 2–4 frames for organic feel
- **Match animation style to brand** — a law firm doesn't bounce, a children's app doesn't creep
- **Design in Illustrator, animate in After Effects** — keep assets as vectors for infinite scaling
- **Use the Graph Editor** — the curve editor is where good animation becomes great animation
- **Create templates** — build Essential Graphics templates for repeatable content (lower thirds, titles)

## Using the Reference Files

**`/references/animation-principles.md`** — Read when designing animation curves, timing, or applying motion design principles. Covers the 12 principles applied to MoGraph, keyframe techniques, and kinetic typography.

**`/references/design-styles.md`** — Read when choosing a visual style or art direction. Covers flat, isometric, 3D, liquid, retro, and line art styles with technique guides.

**`/references/software-techniques.md`** — Read when working in After Effects or other tools. Covers expressions, shape layers, tracking, compositing, and tool-specific workflows.

**`/references/workflow-optimization.md`** — Read when managing production efficiency. Covers project organization, render settings, template creation, and multi-format export workflows.
