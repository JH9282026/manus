---
name: web-design-development
description: "Web Design & Development is a comprehensive digital creation skill that bridges aesthetic design principles with technical implementation to produce functional, accessible, and engaging web experiences."
---

---
name: Web Design & Development
description: Integrated skill for creating user-centered digital experiences through UI/UX design principles, front-end development, responsive design implementation, accessibility compliance, and performance optimization.
---

# Web Design & Development


## Overview

This section provides an overview of the skill.

## Skill Description and Purpose

Web Design & Development is a comprehensive digital creation skill that bridges aesthetic design principles with technical implementation to produce functional, accessible, and engaging web experiences. This skill encompasses the full spectrum of web creation—from user research and wireframing through to coded, responsive, production-ready websites and applications.

### Core Competencies

**UI/UX Design Principles**: Strategic approach to creating intuitive digital experiences:

- **User-Centered Design (UCD)**: Iterative design methodology prioritizing user needs through research, testing, and continuous refinement. Every design decision anchored to identified user goals and behaviors.

- **Information Architecture (IA)**: Organizing, structuring, and labeling content for findability and usability. Includes site mapping, navigation design, and content hierarchy development using card sorting and tree testing methodologies.

- **Interaction Design (IxD)**: Designing meaningful interactions between users and interfaces. Encompasses gesture patterns, state transitions, micro-interactions, feedback systems, and affordance communication.

- **Visual Design**: Applying graphic design principles to digital interfaces—typography, color, spacing, imagery, and iconography—to create cohesive, branded experiences that guide user attention and action.

- **Accessibility Design**: Ensuring experiences are usable by people with diverse abilities. WCAG 2.1 compliance (perceivable, operable, understandable, robust) integrated throughout the design process.

**Front-End Development Fundamentals**: Technical implementation of designed experiences:

- **HTML (Structure)**: Semantic markup creating accessible, SEO-friendly document structures. Proper use of heading hierarchy, landmarks, forms, tables, and ARIA attributes for enhanced accessibility.

- **CSS (Presentation)**: Visual styling including layout systems (Flexbox, Grid), responsive design, animations, transitions, custom properties, and modern features like container queries and cascade layers.

- **JavaScript (Behavior)**: Interactivity implementation including DOM manipulation, event handling, API integration, form validation, and progressive enhancement strategies.

- **Responsive Design**: Fluid layouts adapting to all viewport sizes using mobile-first approach, breakpoint strategy, flexible images, and responsive typography.

### Strategic Applications

This skill addresses business-critical web needs: corporate websites, e-commerce platforms, web applications, landing pages, microsites, portfolios, and digital marketing assets. Well-designed websites increase conversion rates by 200%, reduce bounce rates by 40%, and significantly impact brand perception—94% of first impressions are design-related.

**Value Proposition**: Professional web design directly impacts business outcomes. Page load speed improvements of 1 second can increase conversions by 7%. Mobile optimization captures the 60%+ of traffic from mobile devices. Accessible design expands audience reach to 1+ billion people with disabilities while improving SEO.

---

## Required Inputs/Parameters

### Primary Inputs

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `project_brief` | Object | Yes | Website objectives, target audience, key pages/features, success metrics |
| `brand_guidelines` | Object | Conditional | Visual identity standards for branded projects |
| `content_inventory` | Array | Yes | All text, images, videos, documents to be incorporated |
| `sitemap` | Object | Yes | Page structure, hierarchy, and navigation requirements |
| `functional_requirements` | Array | Yes | Interactive features, integrations, forms, dynamic elements |

### Design Inputs

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `user_personas` | Array | null | Target user profiles with goals, behaviors, pain points |
| `user_journey_maps` | Array | null | Mapped user flows through key site tasks |
| `competitor_analysis` | Object | null | Competitive landscape review with differentiation opportunities |
| `design_direction` | String | "modern" | Style preference: minimal, corporate, creative, bold, elegant |
| `reference_sites` | Array | [] | URLs of inspirational websites for direction |
| `accessibility_level` | String | "AA" | WCAG compliance target: A, AA, AAA |

### Technical Inputs

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `technology_stack` | Object | null | Required frameworks, CMS, hosting environment |
| `browser_support` | Array | ["modern"] | Target browsers: modern, legacy-ie11, all |
| `performance_targets` | Object | null | Core Web Vitals thresholds, load time requirements |
| `integration_requirements` | Array | [] | Third-party services, APIs, analytics platforms |
| `seo_requirements` | Object | null | Meta data, structured data, sitemap generation needs |

### User Research Inputs

```json
{
  "persona": {
    "name": "Primary User Persona Name",
    "demographics": {
      "age_range": "25-45",
      "occupation": "Marketing Manager",
      "tech_proficiency": "Intermediate"
    },
    "goals": ["Find information quickly", "Compare options", "Make purchase decisions"],
    "pain_points": ["Cluttered navigation", "Slow loading", "Poor mobile experience"],
    "behaviors": {
      "devices": ["mobile-primary", "desktop-secondary"],
      "browsing_habits": "Quick scanner, uses search"
    }
  }
}
```

---

## Expected Outputs/Deliverables

### Design Deliverables

**Research & Strategy Documents**:
- User persona profiles (2-4 primary personas)
- User journey maps for key conversion paths
- Competitive analysis matrix
- Information architecture sitemap
- Content strategy recommendations

**Wireframes & Prototypes**:
- Low-fidelity wireframes for all page templates
- Responsive wireframes (mobile, tablet, desktop breakpoints)
- Interactive prototype demonstrating key user flows
- Annotation documents explaining functionality

**Visual Design**:
- High-fidelity mockups for all unique page templates
- Responsive design variants (minimum 3 breakpoints)
- Component library/design system documentation
- Icon set and custom graphic elements
- Interaction specifications (hover states, transitions, animations)

### Development Deliverables

**Production Code**:
- Semantic HTML5 markup with proper accessibility attributes
- Modular CSS (following BEM, SMACSS, or chosen methodology)
- JavaScript with progressive enhancement approach
- Responsive implementation across all breakpoints

**Technical Documentation**:
- Code style guide and conventions
- Component documentation with usage examples
- Build process and deployment instructions
- Third-party integration documentation

### Specifications by Deliverable Type

| Deliverable | Format | Specifications |
|-------------|--------|----------------|
| Wireframes | Figma/XD/Sketch | Annotated, responsive variants, linked prototype |
| Mockups | Figma/XD/Sketch | Exportable assets, developer handoff specs |
| Prototype | Figma/InVision | Interactive, clickable, shareable link |
| HTML | .html | W3C valid, semantic, accessible |
| CSS | .css/.scss | Mobile-first, BEM naming, custom properties |
| JavaScript | .js | ES6+, modular, commented |
| Assets | SVG/PNG/WebP | Optimized, multiple resolutions, sprite sheets |

### Quality Standards

**Performance Metrics (Core Web Vitals)**:
- Largest Contentful Paint (LCP): < 2.5 seconds
- First Input Delay (FID): < 100 milliseconds
- Cumulative Layout Shift (CLS): < 0.1
- Time to First Byte (TTFB): < 600 milliseconds
- Total Page Weight: < 3MB (target < 1.5MB)

**Accessibility Compliance**:
- WCAG 2.1 AA compliance minimum
- Color contrast ratio: 4.5:1 normal text, 3:1 large text
- Keyboard navigable (all interactive elements)
- Screen reader compatible (proper ARIA labels, roles)
- Focus indicators visible and clear

**Code Quality**:
- W3C HTML validation (zero errors)
- CSS validation (no deprecated properties)
- Lighthouse score: 90+ across all categories
- Cross-browser tested (Chrome, Firefox, Safari, Edge)

---

## Example Use Cases

### Use Case 1: Corporate Website Redesign

**Scenario**: Professional services firm requires complete website redesign to modernize brand presence and improve lead generation.

**Input Parameters**:
```json
{
  "project_brief": {
    "company": "Strategic Consulting Group",
    "industry": "Management Consulting",
    "objectives": ["Modernize brand perception", "Increase qualified leads by 40%", "Improve mobile experience"],
    "pages": ["Home", "Services (6)", "Industries (4)", "About", "Team", "Insights/Blog", "Contact"],
    "features": ["Service request form", "Newsletter signup", "Resource downloads", "Team directory"]
  },
  "current_issues": ["Dated design", "Poor mobile usability", "High bounce rate", "Slow load times"],
  "target_audience": "C-suite executives, enterprise companies"
}
```

**Process Execution**:
1. Conduct stakeholder interviews and current site audit
2. Analyze competitor websites and industry best practices
3. Develop user personas based on client data and interviews
4. Create information architecture with improved navigation
5. Design wireframes for all page templates with responsive variants
6. Build interactive prototype for stakeholder review
7. Develop high-fidelity visual designs aligned with brand evolution
8. Create component-based design system for consistency
9. Develop front-end with performance optimization
10. Implement accessibility features and conduct WCAG audit
11. Perform cross-browser and device testing
12. Optimize for Core Web Vitals performance

**Output**: Complete website redesign including 15 unique page templates, responsive design system, production-ready code, and comprehensive documentation.

### Use Case 2: E-Commerce Landing Page Optimization

**Scenario**: DTC brand needs high-converting product landing page for paid advertising campaigns.

**Input Parameters**:
```json
{
  "project_brief": {
    "product": "Premium skincare serum",
    "objective": "Maximize conversion rate for paid social traffic",
    "traffic_source": "Instagram and Facebook ads",
    "target_conversion": "Add to cart",
    "price_point": "$89"
  },
  "content_materials": {
    "product_images": ["hero", "ingredients", "before_after", "lifestyle"],
    "testimonials": 12,
    "features": ["Clinical results", "Ingredient breakdown", "Usage instructions"],
    "trust_elements": ["Money-back guarantee", "Free shipping", "Reviews"]
  }
}
```

**Process Execution**:
1. Analyze high-converting landing pages in beauty/skincare vertical
2. Map user journey from ad click to conversion
3. Design mobile-first layout (80%+ traffic from mobile)
4. Implement persuasion architecture (social proof, urgency, trust)
5. Create fast-loading page (target LCP < 1.5s)
6. Build with A/B testing framework integration
7. Optimize for social platform tracking pixels

**Output**: High-performance landing page with A/B testing variants, analytics integration, and conversion tracking implementation.

### Use Case 3: Web Application Dashboard Design

**Scenario**: SaaS company needs intuitive dashboard interface for their analytics platform.

**Input Parameters**:
```json
{
  "project_brief": {
    "application": "Marketing analytics dashboard",
    "users": "Marketing managers and analysts",
    "key_tasks": ["Monitor KPIs", "Generate reports", "Analyze trends", "Export data"],
    "complexity": "Data-heavy with multiple visualization types"
  },
  "functional_requirements": {
    "widgets": ["Charts", "Tables", "Cards", "Filters"],
    "interactions": ["Drag-drop customization", "Date range selection", "Export functions"],
    "data_refresh": "Real-time and scheduled"
  }
}
```

**Output**: Complete dashboard design system with 30+ components, interactive prototype, front-end implementation, and accessibility-compliant data visualizations.

---

## Prerequisites or Dependencies

### Design Tool Requirements

**Primary Design Software** (one required):
- Figma (collaborative, web-based, industry-leading)
- Adobe XD (Adobe ecosystem integration)
- Sketch (macOS, extensive plugin ecosystem)
- InVision Studio (prototyping-focused)

**Supporting Design Tools**:
- Whimsical / Miro (wireframing, flowcharts)
- Maze / UserTesting (usability testing)
- Hotjar / FullStory (user behavior analytics)
- Zeplin / Avocode (design handoff)

### Development Environment

**Core Technologies**:
- Text editor/IDE (VS Code, WebStorm, Sublime Text)
- Git version control
- Node.js runtime environment
- Package managers (npm, yarn)
- Browser developer tools

**Front-End Stack Options**:

| Approach | Technologies | Best For |
|----------|-------------|----------|
| Vanilla | HTML, CSS, JavaScript | Simple sites, maximum control |
| CSS Framework | Tailwind, Bootstrap | Rapid development, consistency |
| React | React, Next.js, Gatsby | Complex applications, SPAs |
| Vue | Vue.js, Nuxt | Progressive enhancement |
| Static Site | 11ty, Hugo, Jekyll | Content sites, blogs |

### Testing & QA Tools

- Browser testing: BrowserStack, LambdaTest, CrossBrowserTesting
- Accessibility: axe DevTools, WAVE, Lighthouse
- Performance: WebPageTest, GTmetrix, PageSpeed Insights
- Validation: W3C Validator, CSS Validator

### Knowledge Prerequisites

**Essential Design Knowledge**:
- UI design patterns and conventions
- UX research methodologies
- Information architecture principles
- Responsive design strategies
- Accessibility guidelines (WCAG 2.1)

**Essential Technical Knowledge**:
- HTML5 semantic elements and attributes
- CSS layout (Flexbox, Grid), responsive techniques
- JavaScript fundamentals (DOM, events, async)
- Web performance optimization
- Browser compatibility considerations

**Recommended Knowledge**:
- CSS preprocessors (Sass, Less)
- JavaScript frameworks/libraries
- Build tools (Webpack, Vite, Parcel)
- CMS platforms (WordPress, Webflow, Contentful)
- API integration patterns

### Asset Dependencies

- Brand assets (logos, colors, typography files)
- Content (copy, images, videos) or placeholder content
- Third-party service credentials (analytics, forms, CDN)
- Hosting environment specifications
- Domain and SSL certificate access

## Using the Reference Files

- [01 Web Design Fundamentals](./references/01-web-design-fundamentals.md): 01 Web Design Fundamentals
- [02 Modern Css Techniques](./references/02-modern-css-techniques.md): 02 Modern Css Techniques
- [03 Responsive Web Design](./references/03-responsive-web-design.md): 03 Responsive Web Design
- [04 Web Accessibility Standards](./references/04-web-accessibility-standards.md): 04 Web Accessibility Standards
- [05 Web Performance Optimization](./references/05-web-performance-optimization.md): 05 Web Performance Optimization
