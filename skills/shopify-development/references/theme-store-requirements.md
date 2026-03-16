# Shopify Theme Store Requirements

Complete requirements and guidelines for submitting themes to the Shopify Theme Store.

---

## Eligibility Requirements

### Theme Exclusivity

**Shopify Theme Store Exclusive:**
- Themes must be exclusive to Shopify Theme Store
- Cannot be sold on other marketplaces simultaneously
- Cannot be distributed as free themes elsewhere
- Private client work can be adapted but must be substantially different

### Partner Account Requirements

- Active Shopify Partner account in good standing
- Completed partner profile with accurate information
- Valid payment information for revenue sharing
- Agreement to Shopify Partner Program Agreement

## Technical Requirements

### Online Store 2.0 Compliance

**Sections Everywhere:**
- All templates must support sections
- Merchants can add, remove, and reorder sections on any page
- No hardcoded content in templates

**Required Template Files:**
```
templates/
├── 404.json
├── article.json
├── blog.json
├── cart.json
├── collection.json
├── index.json
├── list-collections.json
├── page.json
├── product.json
└── search.json
```

### Required Features

**Essential Functionality:**

1. **Discounts:**
   - Display automatic discounts
   - Show discount codes applied to cart
   - Display sale prices with compare-at prices

2. **Accelerated Checkout:**
   - Support Shop Pay, Apple Pay, Google Pay
   - Dynamic checkout buttons on product pages
   - Express checkout in cart

3. **Faceted Search and Filtering:**
   - Filter by price, vendor, product type, tags
   - Multiple filter selection
   - Clear active filters
   - Filter count indicators

4. **Gift Cards:**
   - Dedicated gift card product template
   - Gift card balance checking
   - Gift card code display

5. **Image Focal Points:**
   - Respect merchant-set focal points
   - Maintain focal point across responsive sizes

6. **Social Sharing:**
   - Share buttons for products and articles
   - Open Graph meta tags
   - Twitter Card meta tags

7. **Country and Language Selection:**
   - Country/region selector
   - Language selector
   - Respect merchant's market settings

8. **Multi-Level Menus:**
   - Support nested menu items (at least 2 levels)
   - Mega menu support recommended

9. **Newsletter Signup:**
   - Email capture form
   - Integration with Shopify customer list

10. **Pickup Availability:**
    - Show local pickup options
    - Display store locations
    - Availability by location

11. **Related Products:**
    - Product recommendations
    - Complementary products
    - Recently viewed items

### Performance Standards

**Lighthouse Scores (Mobile):**
- Performance: 60+ (required), 80+ (recommended)
- Accessibility: 90+ (required)
- Best Practices: 90+ (required)
- SEO: 90+ (required)

**Testing Pages:**
- Homepage
- Collection page
- Product page

**Performance Budget:**
- Total page weight: < 2MB
- JavaScript: < 300KB
- CSS: < 100KB
- Images: Optimized and responsive

### Accessibility Standards

**WCAG 2.1 Level AA Compliance:**

1. **Keyboard Navigation:**
   - All interactive elements keyboard accessible
   - Logical tab order
   - Visible focus indicators
   - Skip to content link

2. **Screen Reader Support:**
   - Semantic HTML structure
   - ARIA labels for icon buttons
   - ARIA live regions for dynamic content
   - Descriptive link text

3. **Visual Accessibility:**
   - Color contrast ratio 4.5:1 for text
   - Color contrast ratio 3:1 for UI components
   - Text resizable up to 200%
   - No information conveyed by color alone

4. **Form Accessibility:**
   - Labels for all form inputs
   - Error messages associated with fields
   - Required field indicators
   - Clear instructions

**Testing Tools:**
- WAVE browser extension
- axe DevTools
- Lighthouse accessibility audit
- Screen reader testing (NVDA, JAWS, VoiceOver)

### Browser and Device Compatibility

**Supported Browsers:**
- Chrome (latest 2 versions)
- Firefox (latest 2 versions)
- Safari (latest 2 versions)
- Edge (latest 2 versions)
- Mobile Safari (iOS 12+)
- Chrome Mobile (Android 8+)

**Responsive Design:**
- Mobile-first approach
- Breakpoints: 320px, 750px, 990px, 1200px
- Touch-friendly interactions (44x44px minimum)
- Horizontal scrolling only where appropriate

## Design Requirements

### Visual Design Standards

**Professional Quality:**
- Cohesive visual design system
- Consistent typography hierarchy
- Harmonious color palette
- Professional-quality imagery
- Intentional white space usage

**Flexibility:**
- Layouts work with varying content amounts
- Graceful handling of long product titles
- Support for products with many variants
- Adaptable to different image aspect ratios

### Theme Uniqueness

**Differentiation Requirements:**
- Fundamentally different from existing themes
- Unique design language and aesthetic
- Innovative features or functionality
- Clear target merchant segment

**Not Acceptable:**
- Minor variations of existing themes
- Simple color scheme changes
- Rebranded versions of other themes
- Themes too similar to Dawn or other free themes

### Customization Options

**Theme Settings:**
- Color customization (primary, secondary, backgrounds)
- Typography options (headings, body text)
- Layout variations
- Feature toggles
- Spacing and sizing controls

**Section Settings:**
- Content customization
- Layout options
- Style variations
- Visibility controls

**Clear Organization:**
- Logical grouping of settings
- Descriptive labels and help text
- Sensible defaults
- Preview of changes in theme editor

## Demo Store Requirements

### Content Quality

**Realistic Product Data:**
- 50+ products across multiple collections
- Varied product types (physical, digital, services)
- Complete product information (descriptions, prices, images)
- Multiple variants where appropriate
- Realistic inventory levels

**High-Quality Images:**
- Professional product photography
- Consistent image style
- Appropriate image sizes (2048x2048px recommended)
- Alt text for all images

**Complete Store Setup:**
- Populated blog with 5+ articles
- About page with company information
- Contact page with form
- FAQ or policies pages
- Functional navigation menus

### Feature Demonstration

**Showcase All Features:**
- Every theme feature visible in demo
- Multiple section variations shown
- Different layout options demonstrated
- All customization possibilities illustrated

**Contextual Instructions:**
- Welcome message explaining theme features
- Annotations highlighting unique elements
- Setup guide for merchants
- Links to documentation

### Prohibited Content

**Do Not Include:**
- Lorem ipsum or placeholder text
- Broken links or images
- Copyrighted content without permission
- Offensive or inappropriate material
- Competitor branding or references

## Theme Listing Requirements

### Theme Name

**Naming Guidelines:**
- Unique and memorable
- 30 characters or fewer
- No generic terms ("Shopify Theme", "Best Theme")
- No version numbers
- No special characters except hyphens

### Theme Icon

**Specifications:**
- Size: 512x512px
- Format: PNG with transparency
- Bold, simple design
- Recognizable at small sizes
- No text or Shopify logo
- Unique color scheme

### Feature Media

**Promotional Video (Recommended):**
- Length: 2-3 minutes
- Format: MP4, MOV, or YouTube link
- Professional quality
- Showcase key features
- Demonstrate merchant workflow
- Include captions

**Feature Image (Alternative):**
- Size: 1920x1080px
- Format: JPG or PNG
- High-quality mockup or screenshot
- Clear focal point
- Minimal text overlay

### Screenshots

**Requirements:**
- Quantity: 3-6 screenshots
- Size: 1600x900px (desktop), 750x1334px (mobile)
- Format: JPG or PNG
- Show actual theme interface
- Highlight key features
- Use demo store content
- Include at least one UI screenshot

**Best Practices:**
- First screenshot is most important
- Show homepage, collection, product pages
- Demonstrate unique features
- Use high-quality, realistic content
- Avoid excessive text overlays

### Theme Description

**Introduction (100 characters):**
- Highlight primary benefits
- Mention target merchant type
- Focus on outcomes, not features
- Avoid keyword stuffing

**Details (500 characters):**
- Describe key functionality
- Explain what makes theme unique
- Mention ideal use cases
- Professional tone
- Avoid excessive marketing language

**Feature List:**
- 3-6 key features
- 80 characters per feature
- Focus on merchant value
- Specific and descriptive
- Avoid generic claims

### Industry and Style Tags

**Industry Tags (Choose up to 3):**
- Clothing and fashion
- Health and beauty
- Home and garden
- Sports and recreation
- Toys and games
- Electronics
- Food and drink
- Art and photography
- Jewelry and accessories

**Style Tags (Choose up to 3):**
- Minimal
- Bold
- Elegant
- Modern
- Classic
- Playful
- Sophisticated

## Pricing Guidelines

### Price Tiers

**Shopify Theme Store Pricing:**
- $140 - $180: Basic themes
- $180 - $220: Standard themes
- $220 - $280: Advanced themes
- $280 - $350: Premium themes

**Pricing Factors:**
- Feature complexity
- Design sophistication
- Customization options
- Target merchant segment
- Competitive positioning

### Revenue Sharing

**Shopify's Commission:**
- 0% for first $1M in sales
- 15% after $1M in sales
- Paid monthly via Partner Dashboard
- Transparent reporting

## Support and Documentation

### Required Documentation

**Theme Documentation:**
- Setup guide
- Feature explanations
- Customization instructions
- Troubleshooting tips
- FAQ section

**Support Channels:**
- Email support address
- Response time commitment (24-48 hours recommended)
- Support hours/timezone
- Documentation URL

### Ongoing Maintenance

**Update Requirements:**
- Bug fixes within reasonable timeframe
- Compatibility with new Shopify features
- Security updates as needed
- Performance improvements

**Version Control:**
- Semantic versioning (MAJOR.MINOR.PATCH)
- Changelog for each update
- Backward compatibility when possible
- Migration guides for breaking changes

## Submission Process

### Pre-Submission Checklist

**Technical:**
- [ ] All required features implemented
- [ ] Lighthouse scores meet requirements
- [ ] Accessibility audit passed
- [ ] Cross-browser testing complete
- [ ] Mobile responsiveness verified
- [ ] Theme Check validation passed

**Design:**
- [ ] Unique and professional design
- [ ] Comprehensive customization options
- [ ] Consistent visual language
- [ ] Flexible layouts

**Demo Store:**
- [ ] 50+ realistic products
- [ ] High-quality images
- [ ] Complete content
- [ ] All features demonstrated

**Listing:**
- [ ] Compelling theme name
- [ ] Professional icon
- [ ] Feature video or image
- [ ] 3-6 screenshots
- [ ] Clear descriptions
- [ ] Appropriate tags

**Documentation:**
- [ ] Setup guide created
- [ ] Support email configured
- [ ] Documentation URL provided

### Submission Steps

1. **Prepare Theme:**
   - Complete all development
   - Test thoroughly
   - Create demo store

2. **Create Listing:**
   - Log in to Partner Dashboard
   - Navigate to Themes
   - Click "Submit theme"
   - Upload theme files

3. **Complete Information:**
   - Add theme name and description
   - Upload icon and screenshots
   - Set pricing
   - Add documentation links

4. **Submit for Review:**
   - Review all information
   - Submit theme
   - Wait for Shopify review (typically 2-4 weeks)

5. **Address Feedback:**
   - Respond to reviewer comments
   - Make requested changes
   - Resubmit if necessary

### Review Process

**What Shopify Reviews:**
- Technical compliance
- Performance and accessibility
- Design quality and uniqueness
- Demo store quality
- Listing accuracy
- Documentation completeness

**Possible Outcomes:**
- Approved: Theme goes live on Theme Store
- Revisions Requested: Make changes and resubmit
- Rejected: Theme does not meet requirements

**Timeline:**
- Initial review: 2-4 weeks
- Resubmission review: 1-2 weeks
- Updates to live themes: 3-5 business days

## Post-Launch Best Practices

### Marketing Your Theme

**Optimization:**
- Monitor theme analytics in Partner Dashboard
- Respond to merchant reviews
- Update screenshots based on feedback
- Refine description for clarity

**Promotion:**
- Share on social media
- Create tutorial content
- Engage with Shopify community
- Offer launch promotions (with Shopify approval)

### Maintaining Quality

**Regular Updates:**
- Fix bugs promptly
- Add new features based on feedback
- Improve performance continuously
- Stay current with Shopify platform updates

**Customer Support:**
- Respond to support requests quickly
- Maintain helpful documentation
- Create video tutorials
- Build community around theme

### Monitoring Success

**Key Metrics:**
- Theme sales and revenue
- Merchant reviews and ratings
- Support ticket volume and resolution time
- Theme performance scores
- Merchant retention rate

**Continuous Improvement:**
- Analyze merchant feedback
- Study competitor themes
- Test new features
- Iterate on design
- Optimize for conversions