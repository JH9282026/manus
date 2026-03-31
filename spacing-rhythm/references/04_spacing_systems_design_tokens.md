# Spacing Systems and Design Tokens

## Overview
Spacing systems transform arbitrary visual adjustments into rule-based frameworks, ensuring consistency, scalability, and efficiency in design. Design tokens are the implementation mechanism that bridges design and development, creating a single source of truth for spacing values.

## What is a Spacing System?

A spacing system is a set of predefined rules that dictate how UI elements are measured, sized, and spaced. It provides a limited palette of spacing values that designers and developers use consistently across a product.

### Why Spacing Systems Matter

**Consistency**
- Ensures uniformity across entire product
- Prevents arbitrary spacing decisions
- Creates cohesive user experience
- Maintains brand identity

**Scalability**
- Simplifies design system growth
- Enables rapid prototyping
- Supports multiple products/platforms
- Facilitates design system evolution

**Efficiency**
- Reduces decision fatigue
- Speeds up design process
- Streamlines designer-developer handoff
- Minimizes errors and inconsistencies

**Collaboration**
- Creates shared language between designers and developers
- Simplifies communication
- Enables parallel work
- Reduces back-and-forth revisions

## Building a Spacing System

### Step 1: Choose a Base Unit

The base unit is the foundation of your spacing system.

**Common Base Units**
- **8px**: Most popular, highly divisible, industry standard
- **4px**: Greater granularity, good for dense interfaces
- **5px**: Alternative approach, less common
- **10px**: Simpler math, less flexible

**Selection Criteria**
- Screen resolution compatibility
- Device pixel ratio considerations
- Team familiarity
- Existing design system constraints
- Industry standards and best practices

### Step 2: Create a Spacing Scale

Build a limited set of spacing values based on your base unit.

**8px System Example**
```
space-0: 0px
space-1: 8px
space-2: 16px
space-3: 24px
space-4: 32px
space-5: 40px
space-6: 48px
space-8: 64px
space-10: 80px
space-12: 96px
space-16: 128px
```

**4px System Example**
```
space-0: 0px
space-1: 4px
space-2: 8px
space-3: 12px
space-4: 16px
space-5: 20px
space-6: 24px
space-8: 32px
space-10: 40px
space-12: 48px
```

**Scale Considerations**
- Limit to 8-12 values for simplicity
- Include 0 for no spacing
- Cover micro to macro spacing needs
- Allow for half-steps if necessary

### Step 3: Define Spacing Categories

Organize spacing values by use case.

**Micro Spacing (Within Components)**
- Icon-to-text spacing: 8px
- Button padding: 12px, 16px
- Form field padding: 12px, 16px
- List item padding: 8px, 12px

**Macro Spacing (Between Components)**
- Card margins: 16px, 24px
- Section spacing: 32px, 48px, 64px
- Page margins: 24px, 32px, 48px
- Grid gutters: 16px, 24px, 32px

**Layout Spacing (Page Structure)**
- Container padding: 16px, 24px, 32px
- Column gaps: 24px, 32px
- Row gaps: 24px, 32px, 48px
- Major section breaks: 64px, 80px, 96px

## Design Tokens

Design tokens are named entities that store visual design attributes. For spacing, they store spacing values in a platform-agnostic format.

### What Are Design Tokens?

**Definition**
- Named variables representing design decisions
- Platform-agnostic format (usually JSON or YAML)
- Single source of truth for design values
- Automatically transformed for different platforms

**Benefits**
- Consistency across platforms (web, iOS, Android)
- Easy updates (change once, update everywhere)
- Reduced errors
- Improved collaboration
- Scalable design systems

### Token Naming Conventions

**Semantic Naming**
Describes purpose, not value:
```
space-component-padding-small
space-component-padding-medium
space-component-padding-large
space-section-gap
space-page-margin
```

**T-Shirt Sizing**
Uses size metaphors:
```
space-xs: 4px
space-sm: 8px
space-md: 16px
space-lg: 24px
space-xl: 32px
space-2xl: 48px
space-3xl: 64px
```

**Numeric Naming**
Based on scale or multiplier:
```
space-0: 0px
space-1: 8px
space-2: 16px
space-3: 24px
space-4: 32px
space-6: 48px
space-8: 64px
```

**Best Practice**
- Choose one naming convention and stick to it
- Document naming system clearly
- Consider team familiarity
- Balance clarity with brevity

### Token Structure

**JSON Format Example**
```json
{
  "spacing": {
    "base": {
      "value": "8px",
      "type": "spacing"
    },
    "xs": {
      "value": "4px",
      "type": "spacing"
    },
    "sm": {
      "value": "8px",
      "type": "spacing"
    },
    "md": {
      "value": "16px",
      "type": "spacing"
    },
    "lg": {
      "value": "24px",
      "type": "spacing"
    },
    "xl": {
      "value": "32px",
      "type": "spacing"
    }
  }
}
```

**YAML Format Example**
```yaml
spacing:
  base:
    value: 8px
    type: spacing
  xs:
    value: 4px
    type: spacing
  sm:
    value: 8px
    type: spacing
  md:
    value: 16px
    type: spacing
  lg:
    value: 24px
    type: spacing
  xl:
    value: 32px
    type: spacing
```

### Token Transformation

Tokens are transformed into platform-specific formats:

**CSS Variables**
```css
:root {
  --space-xs: 4px;
  --space-sm: 8px;
  --space-md: 16px;
  --space-lg: 24px;
  --space-xl: 32px;
}
```

**SCSS Variables**
```scss
$space-xs: 4px;
$space-sm: 8px;
$space-md: 16px;
$space-lg: 24px;
$space-xl: 32px;
```

**JavaScript/TypeScript**
```javascript
export const spacing = {
  xs: '4px',
  sm: '8px',
  md: '16px',
  lg: '24px',
  xl: '32px',
};
```

**iOS (Swift)**
```swift
enum Spacing {
  static let xs: CGFloat = 4
  static let sm: CGFloat = 8
  static let md: CGFloat = 16
  static let lg: CGFloat = 24
  static let xl: CGFloat = 32
}
```

**Android (Kotlin)**
```kotlin
object Spacing {
  val xs = 4.dp
  val sm = 8.dp
  val md = 16.dp
  val lg = 24.dp
  val xl = 32.dp
}
```

## Implementing Spacing Systems

### In Design Tools

**Figma**
1. Create spacing components (rectangles at each spacing value)
2. Set up auto layout with spacing tokens
3. Use plugins like "Design Tokens" or "Tokens Studio"
4. Create spacing documentation page
5. Share with team as library

**Sketch**
1. Create spacing symbols
2. Use shared styles for spacing
3. Leverage plugins for token management
4. Document in separate artboard
5. Publish as library

**Adobe XD**
1. Create spacing components
2. Use component states for different sizes
3. Leverage plugins for design tokens
4. Document in separate artboard
5. Share as cloud library

### In Code

**CSS Custom Properties**
```css
.card {
  padding: var(--space-md);
  margin-bottom: var(--space-lg);
}

.button {
  padding: var(--space-sm) var(--space-md);
  margin-right: var(--space-sm);
}
```

**Tailwind CSS**
```javascript
// tailwind.config.js
module.exports = {
  theme: {
    spacing: {
      'xs': '4px',
      'sm': '8px',
      'md': '16px',
      'lg': '24px',
      'xl': '32px',
      '2xl': '48px',
      '3xl': '64px',
    },
  },
};
```

**React/Styled Components**
```javascript
import { spacing } from './tokens';

const Card = styled.div`
  padding: ${spacing.md};
  margin-bottom: ${spacing.lg};
`;
```

## Token Management Tools

### Style Dictionary
- Open-source tool by Amazon
- Transforms design tokens to multiple platforms
- Highly customizable
- Industry standard

### Tokens Studio (Figma Plugin)
- Manage tokens directly in Figma
- Sync with GitHub, GitLab, or other repos
- Export to multiple formats
- Popular in design community

### Specify
- Design token management platform
- Integrates with design tools and code
- Collaboration features
- Version control

### Zeroheight
- Documentation platform with token support
- Syncs with Figma, Sketch
- Generates code snippets
- Team collaboration features

## Governance and Maintenance

### Establishing Guidelines

**Documentation**
- When to use each spacing value
- Examples of proper usage
- Common patterns and components
- Do's and don'ts

**Review Process**
- Regular audits of spacing usage
- Design reviews for new components
- Code reviews for implementation
- Feedback loops for improvements

### Evolution and Updates

**When to Update**
- User feedback indicates issues
- New platform requirements
- Brand refresh or redesign
- Accessibility improvements needed

**Update Process**
1. Propose changes with rationale
2. Review with design and development teams
3. Update tokens in source of truth
4. Regenerate platform-specific files
5. Update documentation
6. Communicate changes to team
7. Implement in products
8. Monitor for issues

## Best Practices

1. **Start Simple**: Begin with 6-8 spacing values, expand as needed
2. **Document Thoroughly**: Clear documentation prevents misuse
3. **Automate**: Use tools to transform tokens automatically
4. **Version Control**: Track token changes in Git
5. **Test Across Platforms**: Ensure tokens work on all targets
6. **Educate Team**: Train designers and developers on system
7. **Iterate**: Refine based on real-world usage
8. **Maintain Consistency**: Resist ad-hoc spacing additions
9. **Monitor Usage**: Track which tokens are used most
10. **Stay Flexible**: Allow for exceptions when truly necessary

## References

- Design Systems. "Space, Grids, and Layouts" https://www.designsystems.com/space-grids-and-layouts/
- Atlassian Design. "Spacing" https://atlassian.design/foundations/spacing/
- Lullabot. "Designing Rhythm and Proportion" https://www.lullabot.com/articles/designing-rhythm-and-proportion
- UInica. "Vertical Rhythm in UI" https://uinica.com/vertical-rhythm-in-ui-the-hidden-system-that-makes-interfaces-feel-clean-and-readable/
