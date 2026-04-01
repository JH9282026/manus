---
name: imagery-iconography
description: "Select, create, and implement images, illustrations, and icon systems that enhance visual communication. Use for: choosing imagery style, creating icon sets, illustration direction, photo selection, and visual storytelling."
---

# Imagery Iconography

## Description

Imagery & Iconography establishes the visual language for all graphical elements beyond UI components. This includes icon systems, illustrations, photography style, and decorative elements that support brand personality.

## When to Use

- Establishing visual design direction
- Selecting icon library or creating custom icons
- Defining photography/illustration style
- Creating consistency in visual assets
- Building brand visual language

---

## Instructions for AI Agents

### Step 1: Define Icon Strategy

**Icon style decision:**

| Style | Best For | Personality | Examples |
|-------|----------|-------------|---------|
| Outlined | Modern, clean UI | Light, airy, minimal | Heroicons, Feather |
| Filled/Solid | Bold, emphasis | Strong, definitive | Material filled |
| Two-tone | Playful, colorful | Friendly, dynamic | Phosphor duotone |
| Hand-drawn | Creative, casual | Personal, artistic | Custom illustrations |

**Prompt for icon selection:**
```
For [PROJECT] with [PERSONALITY] personality, recommend:

1. Icon style: [Outlined/Filled/Two-tone]
2. Icon library: [Specific library name]
3. Icon weight: [Light/Regular/Bold]
4. Icon sizes: [Standard sizes to use]
5. Icon colors: [How colors apply to icons]
```

### Step 2: Icon Specifications

**Icon system template:**

```markdown
## Icon System: [PROJECT]

### Library
**Primary**: [Library name] - [URL]
**Fallback**: [Secondary library if needed]

### Sizing Scale
| Token | Size | Line Width | Use Case |
|-------|------|------------|----------|
| xs | 16px | 1.5px | Inline with text, badges |
| sm | 20px | 1.5px | Buttons, inputs |
| md | 24px | 2px | Navigation, default |
| lg | 32px | 2px | Feature highlights |
| xl | 48px | 2px | Empty states, features |

### Color Application
| Context | Color | Token |
|---------|-------|-------|
| Default UI | Gray-500 | icon-default |
| Interactive (resting) | Gray-400 | icon-subtle |
| Interactive (hover) | Gray-600 | icon-hover |
| Active/Selected | Primary-500 | icon-active |
| Disabled | Gray-300 | icon-disabled |
| Success | Success-500 | icon-success |
| Warning | Warning-500 | icon-warning |
| Error | Error-500 | icon-error |

### Spacing
- Icon-to-text gap: 8px (sm), 12px (md)
- Touch target: Minimum 44×44px
- Padding around icons: 10px minimum for clickable
```

### Step 3: Illustration Style

**Illustration decisions:**

```markdown
## Illustration Style

### Style Direction
- **Type**: [Flat/3D/Isometric/Hand-drawn/Abstract]
- **Complexity**: [Simple/Moderate/Detailed]
- **Human representation**: [Realistic/Stylized/Abstract/None]
- **Color usage**: [Brand colors/Expanded palette/Monochrome]

### Sources
| Source | URL | License | Use Case |
|--------|-----|---------|----------|
| [Library 1] | [URL] | [License] | [Use] |
| [Library 2] | [URL] | [License] | [Use] |

### Application
- **Hero sections**: Large, complex illustrations
- **Empty states**: Medium, contextual illustrations
- **Onboarding**: Sequential, educational illustrations
- **Features**: Simple, icon-like spot illustrations

### Color Customization
[How to adapt illustration colors to brand palette]
```

### Step 4: Photography Guidelines

**Photography style guide:**

```markdown
## Photography Style

### Direction
- **Subject matter**: [People/Products/Abstract/Lifestyle]
- **Mood**: [Bright/Moody/Natural/Vibrant]
- **Composition**: [Minimal/Busy/Centered/Rule of thirds]
- **Color treatment**: [Natural/Color-graded/Duotone]

### Technical Specifications
| Property | Guideline |
|----------|----------|
| Aspect ratios | 16:9 (hero), 4:3 (cards), 1:1 (avatars) |
| Minimum resolution | 2x display (e.g., 1200px for 600px display) |
| File format | WebP with JPEG fallback |
| Max file size | 200KB for heroes, 50KB for thumbnails |

### Sources
| Source | URL | License |
|--------|-----|---------|
| Unsplash | unsplash.com | Free |
| Pexels | pexels.com | Free |
| [Brand photos] | [Location] | Owned |

### Treatment Guidelines
- Apply [X]% overlay of [Color] for consistency
- Use [Filter name] preset for color grading
- Avoid: [What not to use]
```

---

## Example Input/Output

### Example Input

```markdown
**Project**: TaskFlow - SaaS project management
**Personality**: Modern, professional, approachable
**Colors**: Violet primary, Slate neutrals
**Audience**: Creative agencies
```

### Example Output

```markdown
## Visual Assets: TaskFlow

---

## Icon System

### Primary Library: Heroicons
- **URL**: https://heroicons.com
- **Style**: Outlined (default), Solid (emphasis)
- **License**: MIT (free for commercial use)

**Why Heroicons**:
- Clean, modern aesthetic matches TaskFlow personality
- Consistent stroke widths
- Excellent coverage of UI needs
- Easy to use with Tailwind/React

### Sizing System

| Token | Size | Stroke | Example Usage |
|-------|------|--------|---------------|
| `icon-xs` | 16px | 1.5px | Inline badges, table cells |
| `icon-sm` | 18px | 1.5px | Buttons, input icons |
| `icon-md` | 20px | 1.5px | Navigation items, lists |
| `icon-lg` | 24px | 2px | Feature cards, headers |
| `icon-xl` | 32px | 2px | Empty states |
| `icon-2xl` | 48px | 2px | Hero features |

### Color System

| Context | Color | Hex | Example |
|---------|-------|-----|----------|
| Default | Slate-500 | #64748B | Navigation icons |
| Subtle | Slate-400 | #94A3B8 | Secondary icons |
| Emphasis | Slate-700 | #334155 | Important icons |
| Interactive | Violet-500 | #8B5CF6 | Active nav, CTAs |
| Interactive Hover | Violet-600 | #7C3AED | Hover state |
| Success | Emerald-500 | #10B981 | Check marks, complete |
| Warning | Amber-500 | #F59E0B | Alerts, attention |
| Error | Red-500 | #EF4444 | Errors, delete |
| Disabled | Slate-300 | #CBD5E1 | Inactive elements |

### Common Icons Mapped

| Action | Icon Name | Variant |
|--------|-----------|----------|
| Home/Dashboard | `home` | outline |
| Projects | `folder` | outline |
| Tasks | `check-circle` | outline |
| Add/Create | `plus` | outline |
| Search | `magnifying-glass` | outline |
| Settings | `cog-6-tooth` | outline |
| User/Profile | `user-circle` | outline |
| Team | `user-group` | outline |
| Calendar | `calendar` | outline |
| Delete | `trash` | outline |
| Edit | `pencil-square` | outline |
| Close | `x-mark` | outline |
| Menu | `bars-3` | outline |
| Chevron | `chevron-right` | outline |
| Check | `check` | solid (for checkboxes) |
| Alert | `exclamation-triangle` | outline |
| Info | `information-circle` | outline |

---

## Illustrations

### Style Direction

**Primary Style**: Flat, minimal with brand colors
**Character**: Abstract/geometric humans (diverse, modern)
**Mood**: Professional but warm and approachable

### Recommended Sources

| Source | Style | URL | License | Best For |
|--------|-------|-----|---------|----------|
| unDraw | Flat, colorable | undraw.co | Free | Empty states, features |
| Humaaans | Mix-match people | humaaans.com | Free | Team imagery |
| Storyset | Animated, colorable | storyset.com | Free | Onboarding |
| Open Peeps | Hand-drawn people | openpeeps.com | Free | Playful accents |

### Color Customization

When using unDraw or similar:
- Set primary color to Violet-500 (`#8B5CF6`)
- Set secondary to Amber-400 (`#FBBF24`) or Violet-300
- Backgrounds: Keep transparent or use Slate-50

### Usage Guidelines

| Context | Size | Style | Examples |
|---------|------|-------|----------|
| Hero sections | Large (400-600px) | Complex, multi-element | Landing page hero |
| Empty states | Medium (200-300px) | Single focus | "No projects yet" |
| Features | Small (150-200px) | Simple, iconic | Feature benefit cards |
| Onboarding | Medium (250-350px) | Step-by-step | Setup wizard |
| Error pages | Medium (300px) | Friendly, apologetic | 404, 500 pages |

### Don'ts
- Don't use illustrations with conflicting color schemes
- Don't mix illustration styles (flat with 3D)
- Don't use overly detailed illustrations in small sizes
- Don't use dated or clipart-style illustrations

---

## Photography

### When to Use Photos

| Use Photos | Use Illustrations |
|------------|------------------|
| Testimonials (real people) | Feature explanations |
| Team page | Empty states |
| Case studies | Onboarding |
| Real product usage | Abstract concepts |

### Photo Style Guidelines

**Mood**: Natural, professional, collaborative
**Subjects**: 
- Teams working together
- Creative professionals in modern offices
- Laptops/workspaces (tasteful, not cluttered)
- Diversity in representation

**Avoid**:
- Overly staged stock photos
- Outdated office environments
- Cliché handshake/meeting images
- Low quality or pixelated images

### Technical Specs

| Use Case | Aspect Ratio | Min Width | Max Size |
|----------|--------------|-----------|----------|
| Hero | 16:9 | 1920px | 300KB |
| Card thumbnail | 16:9 | 640px | 80KB |
| Avatar | 1:1 | 200px | 30KB |
| Testimonial | 1:1 | 400px | 50KB |

### Photo Sources

| Source | URL | Quality | License |
|--------|-----|---------|----------|
| Unsplash | unsplash.com | High | Free |
| Pexels | pexels.com | High | Free |
| UI Faces | uifaces.co | Avatars | Free |

### Photo Treatment

For consistency:
1. Slight desaturation (90% saturation)
2. Subtle warm tone boost
3. Optional: Violet overlay at 5-10% for hero images

---

## Decorative Elements

### Gradients

**Primary Gradient**:
```css
background: linear-gradient(135deg, #8B5CF6 0%, #A78BFA 50%, #C4B5FD 100%);
```

**Subtle Background**:
```css
background: linear-gradient(180deg, #F5F3FF 0%, #FFFFFF 100%);
```

### Shapes & Patterns

- Subtle dot grid pattern for backgrounds
- Rounded blob shapes for decorative accents
- Soft geometric shapes (circles, rounded squares)

### Usage

- Landing page hero backgrounds
- Feature section dividers
- Card hover states (subtle)
- Modal headers
```

---

## Prompts Library

### Icon Library Selection
```
Recommend an icon library for [PROJECT TYPE] with [PERSONALITY]:

1. Top 3 library recommendations with pros/cons
2. Recommended style (outlined/filled)
3. Size system to use
4. Color application strategy
```

### Illustration Source
```
Find illustration resources for [PROJECT] that:
- Match [PERSONALITY] mood
- Support [PRIMARY COLOR] customization
- Include [SUBJECTS NEEDED]
- Are [LICENSE TYPE] licensed
```

---

## Resources

### Icon Libraries

| Library | URL | Style | License |
|---------|-----|-------|----------|
| Heroicons | heroicons.com | Outline/Solid | MIT |
| Phosphor | phosphoricons.com | Multiple weights | MIT |
| Lucide | lucide.dev | Outline | MIT |
| Tabler | tabler.io/icons | Outline | MIT |
| Feather | feathericons.com | Outline | MIT |

### Illustration Libraries

| Library | URL | Customizable | License |
|---------|-----|--------------|----------|
| unDraw | undraw.co | Yes (color) | Free |
| Humaaans | humaaans.com | Yes (full) | Free |
| DrawKit | drawkit.com | Yes | Free/Paid |
| Storyset | storyset.com | Yes (color) | Free |

---

## Success Criteria

### Minimum Requirements
- [ ] Icon library selected with rationale
- [ ] Size scale defined
- [ ] Color application documented
- [ ] Illustration source identified
- [ ] Photography guidelines established

### Quality Indicators
- [ ] Consistent visual language
- [ ] Icons support all UI needs
- [ ] Illustrations match brand personality
- [ ] Clear guidelines for team use

---

## Related Skills

- **Previous**: `color_palettes.md` - Colors for icons/illustrations
- **Next**: `component_design.md` - Icons in components
- **Related**: `design_documentation.md` - Full asset documentation

## Using the Reference Files

- [Icon Design Principles](./references/icon-design-principles.md): Icon Design Principles
- [Photography For Design](./references/photography-for-design.md): Photography For Design
- [Visual Asset Management](./references/visual-asset-management.md): Visual Asset Management
