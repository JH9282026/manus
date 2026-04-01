---
name: shopify-development
description: "Build custom Shopify themes, apps, and storefronts using Liquid, JavaScript, and Shopify APIs. Use for: creating custom themes from Dawn, developing Shopify apps, implementing Online Store 2.0 features, optimizing theme performance, building headless commerce solutions, integrating third-party services, and ensuring accessibility compliance."
---

# Shopify Development

Build high-performance, accessible Shopify themes and apps using modern development practices and Shopify's ecosystem.

## Overview

Shopify development encompasses theme customization, app creation, and storefront optimization using Shopify's technology stack including Liquid templating, JavaScript, CSS, and various APIs. This skill covers both traditional theme development and modern headless commerce approaches, emphasizing performance, accessibility, and merchant experience.

## Development Environment Setup

### Essential Tools

| Tool | Purpose | Installation |
|------|---------|-------------|
| Shopify CLI | Theme development, preview, deployment | `npm install -g @shopify/cli @shopify/theme` |
| VS Code + Extensions | Code editing with Shopify Liquid support | Install Shopify Liquid extension |
| Theme Check | Code quality and best practices validation | Built into Shopify CLI |
| Git | Version control for themes and apps | Standard git installation |

### Dawn Theme Foundation

Start all new theme projects with Shopify's Dawn theme as the foundation. Dawn represents current best practices for Online Store 2.0 development:

- Optimized performance (minimal JavaScript)
- Full accessibility compliance
- Modular section-based architecture
- Mobile-first responsive design

## Theme Development Best Practices

### Architecture and Structure

**Modular Design with Sections and Blocks:**
- Split templates into reusable sections for merchant customization
- Use blocks within sections for granular control
- Enable Sections Everywhere for maximum flexibility
- Keep section logic self-contained and independent

**File Organization:**
- Separate folders: `templates/`, `sections/`, `snippets/`, `assets/`
- Use snippets for reusable code components (max 2 levels of nesting)
- Individual files for single purposes
- Consistent naming conventions (lowercase, hyphens)

### Liquid Templating

**Clean Code Principles:**
- Descriptive variable names that explain purpose
- Leverage built-in Liquid filters before custom JavaScript
- Minimize database queries through efficient object access
- Add comments for complex logic or unique features
- Use `{% liquid %}` tag for multi-line logic blocks

**Performance Optimization:**
- Limit nested snippets to 2 levels maximum
- Cache expensive operations when possible
- Use `{% render %}` instead of `{% include %}` for better isolation
- Avoid unnecessary loops and conditionals

### JavaScript Best Practices

**Code Organization:**
- Extract JavaScript into separate files in `assets/` directory
- Enable browser caching through external file references
- Write modular, independent components that work cohesively
- Use defensive coding for third-party product compatibility

**Performance:**
- Minimize JavaScript usage; rely on modern browser features
- Move non-critical scripts to bottom of body tag
- Implement lazy loading for heavy components
- Minify all production JavaScript

### CSS and Styling

**Modern Approaches:**
- Utilize Sass preprocessor support for variables and nesting
- Output Liquid values into CSS files for dynamic theming
- Write mobile-first responsive styles
- Use utility-first frameworks like Tailwind CSS for consistency

**Optimization:**
- Eliminate unused CSS rules
- Minify stylesheets for production
- Use CSS custom properties for theme settings
- Implement critical CSS for above-the-fold content

## Performance Optimization

### Core Metrics

Target Lighthouse scores:
- Performance: 90+ (Theme Store requirement)
- Accessibility: 90+ (Theme Store requirement)
- Best Practices: 90+
- SEO: 90+

### Optimization Techniques

**Image Optimization:**
- Compress all images before upload
- Use Shopify's image filters for responsive sizing
- Implement lazy loading for below-fold images
- Specify image dimensions to prevent layout shift
- Use modern formats (WebP) with fallbacks

**Asset Management:**
- Minify all CSS and JavaScript
- Use Content Delivery Network (CDN) for static assets
- Implement resource hints (preconnect, prefetch)
- Remove unused fonts and icon libraries

**Code Efficiency:**
- Eliminate JavaScript carousels (poor UX and performance)
- Reduce third-party script dependencies
- Defer non-critical JavaScript execution
- Optimize Liquid rendering with efficient queries

### Testing Tools

- Google PageSpeed Insights
- Lighthouse (Chrome DevTools)
- WebPageTest.org
- Shopify Theme Check (built-in)

## Accessibility Standards

### Implementation Requirements

**Semantic HTML:**
- Use proper heading hierarchy (h1-h6)
- Implement landmark regions (header, nav, main, footer)
- Use semantic elements (article, section, aside)

**ARIA Attributes:**
- Add aria-label for icon-only buttons
- Implement aria-expanded for collapsible elements
- Use aria-live for dynamic content updates
- Provide aria-describedby for form field hints

**Keyboard Navigation:**
- Ensure all interactive elements are keyboard accessible
- Maintain logical tab order
- Provide visible focus indicators
- Implement skip-to-content links

**Visual Accessibility:**
- Maintain 4.5:1 contrast ratio for text
- Support browser zoom up to 200%
- Avoid color as sole information indicator
- Provide text alternatives for images

## Shopify App Development

### App Types and Use Cases

| App Type | Best For | Technical Approach |
|----------|----------|-------------------|
| Embedded Apps | Admin functionality, merchant tools | React + Polaris UI |
| Theme App Extensions | Storefront features, widgets | Liquid + JavaScript |
| Custom Apps | Private store integrations | Any framework + Shopify API |
| Public Apps | App Store distribution | Full OAuth + webhook handling |

### Development Workflow

**Setup and Authentication:**
1. Create app in Partner Dashboard
2. Configure OAuth scopes (request only necessary permissions)
3. Implement OAuth flow before other functionality
4. Handle app installation and reinstallation properly

**Best Practices:**
- Follow App Design Guidelines for UI consistency
- Minimize performance impact (max 10-point Lighthouse reduction)
- Avoid pop-ups for OAuth or billing (security requirement)
- Enable quick setup without extensive configuration
- Allow plan upgrades/downgrades without support intervention

### App Store Listing Optimization

**Visual Assets:**
- App icon: Bold colors, simple patterns, no text (512x512px)
- Feature video: 2-3 minutes showcasing key functionality
- Screenshots: 3-6 desktop (1600x900px), include UI and features
- Demo store: Live example with contextual instructions

**Content:**
- Name: Brand name first, under 30 characters, unique
- Introduction (100 chars): Highlight benefits and outcomes
- Details (500 chars): Describe functionality and uniqueness
- Feature list: Concise descriptions (80 chars each) focused on merchant value

## Headless Commerce with Shopify

### Storefront API Approach

Build custom storefronts using Shopify's Storefront API:
- GraphQL-based product and cart management
- Framework-agnostic (React, Vue, Next.js, etc.)
- Full control over frontend experience
- Maintain Shopify's backend for commerce operations

### Hydrogen Framework

Shopify's official React-based framework for headless:
- Built-in Shopify integrations
- Optimized for performance and SEO
- Server-side rendering support
- Oxygen hosting platform integration

## Version Control and Deployment

### Git Workflow

**Repository Structure:**
- Connect theme codebase to GitHub repository
- Use branches for feature development
- Implement pull request reviews
- Tag releases for version tracking

**Deployment Strategy:**
- Development theme for testing
- Staging theme for client review
- Production theme for live store
- Use Shopify CLI for automated deployment

### Theme Versioning

- Maintain changelog for theme updates
- Use semantic versioning (MAJOR.MINOR.PATCH)
- Test thoroughly before production deployment
- Keep backup of previous theme version

## Common Challenges and Solutions

### Challenge: Slow Theme Performance

**Solutions:**
- Audit and remove unused JavaScript libraries
- Implement lazy loading for images and videos
- Minimize third-party app scripts
- Optimize Liquid queries to reduce database calls

### Challenge: Mobile Responsiveness Issues

**Solutions:**
- Use mobile-first CSS approach
- Test on real devices, not just browser emulation
- Implement touch-friendly interactive elements (min 44x44px)
- Optimize images for mobile bandwidth

### Challenge: Merchant Customization Limitations

**Solutions:**
- Implement comprehensive theme settings
- Use sections and blocks for layout flexibility
- Provide clear setting labels and help text
- Document customization options in theme documentation

## Using the Reference Files

### When to Read Each Reference

**`/references/liquid-advanced-techniques.md`** — Read when implementing complex product filtering, custom metafield rendering, advanced cart functionality, or dynamic content generation.

**`/references/app-development-guide.md`** — Read when building Shopify apps, implementing OAuth flows, working with webhooks, or preparing App Store submissions.

**`/references/performance-optimization.md`** — Read when theme performance scores are below targets, optimizing for Core Web Vitals, or implementing advanced caching strategies.

**`/references/theme-store-requirements.md`** — Read when preparing themes for Shopify Theme Store submission, ensuring compliance with all technical and design requirements.
