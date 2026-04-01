---
name: snapchat-ads-campaign-management
description: "Manage Snapchat advertising campaigns including campaign structure, ad formats, targeting options, bidding strategies, and optimization. Use for setting up Snapchat ad campaigns, configuring ad squads, selecting objectives, implementing demographic and behavioral targeting, managing budgets and bids, optimizing for Gen Z and Millennial audiences, and understanding Snapchat's vertical-first advertising platform."
---

# Snapchat Ads Campaign Management

Manage Snapchat advertising campaigns for Gen Z and Millennial audiences using vertical, full-screen ad formats.

## Overview

Snapchat Ads Manager reaches 400+ million daily active users through vertical, immersive ad experiences. This skill covers campaign structure, ad formats, targeting, bidding, and optimization for Snapchat's unique platform.

## Campaign Structure

Snapchat uses a three-tier hierarchy:

| Level | Purpose | Key Settings |
|-------|---------|--------------|
| Campaign | Objective and budget cap | Objective, spend limit |
| Ad Squad | Targeting, budget, schedule | Demographics, interests, placement, bid, budget |
| Ad | Creative and destination | Snap creative, URL, CTA |

## Campaign Objectives

| Objective | Use Case | Optimization |
|-----------|----------|--------------|
| Awareness | Brand awareness, reach | Impressions |
| App Installs | Mobile app downloads | Installs |
| Drive Traffic | Website visits | Swipe ups |
| Engagement | Story views, AR Lens uses | Engagement |
| Video Views | Video content | 2-second views |
| Conversions | Purchases, signups | Pixel events |
| Catalog Sales | E-commerce | Product sales |

## Ad Formats

### Single Image/Video Ads

**Specs**:
- Aspect Ratio: 9:16 (vertical)
- Resolution: 1080 x 1920 px
- Duration: 3-180 seconds (recommended 3-10s)
- File Size: Max 1 GB (video), 5 MB (image)
- Format: .MP4, .MOV (video); .JPG, .PNG (image)

**Best For**: Product promotion, traffic, conversions

### Story Ads

**Specs**:
- Tile: 360 x 600 px, logo 993 x 284 px
- Content: 3-20 Snaps per Story
- Duration: 3-180 seconds per Snap
- Headline: 55 characters max

**Best For**: Brand storytelling, multi-part narratives

### Collection Ads

**Specs**:
- Hero: 1 image/video (1080 x 1920 px)
- Thumbnails: 2-4 square images (160 x 160 px min)
- Platform: Mobile only

**Best For**: Product catalogs, e-commerce

### Commercials

**Specs**:
- Standard: 3-6 seconds (non-skippable)
- Extended: 7-180 seconds (first 6s non-skippable)
- Format: .MP4, .MOV (H.264)

**Best For**: High-impact brand messages

### AR Lenses

**Specs**:
- Created in Lens Studio or Lens Web Builder
- Max size: 8 MB compressed
- Branding: Logo required (top left/right)

**Best For**: Interactive brand experiences, engagement

### AR Filters

**Specs**:
- Static: 945 x 2048 px, PNG, under 300 KB
- Animated: 720 x 1560 px, GIF, 1-3 seconds

**Best For**: User-generated content, brand awareness

## Targeting Options

### Demographics
- Age: 13-17, 18-20, 21-24, 25-34, 35-49, 50+
- Gender: Male, Female, All
- Location: Country, region, DMA, city, postal code
- Language: 15+ languages
- Device: iOS, Android, specific models

### Interests
- Lifestyle categories (beauty, fashion, sports, etc.)
- Sub-category targeting for precision
- Affinity-based targeting

### Behaviors
- Purchase behavior
- App usage patterns
- Content engagement
- Snapchat activity level

### Audiences
- **Snap Pixel Audiences**: Website visitors, event-based
- **Customer Lists**: Email, phone, MAID (min 1,000 users)
- **Lookalike Audiences**: Similar to existing audiences
- **Engagement Audiences**: Interacted with ads/content

### Advanced Targeting
- **Snapchat Lifestyle Categories**: 100+ predefined segments
- **Third-Party Data**: Oracle Data Cloud integration
- **Geo-fencing**: Target specific locations
- **Audience Exclusions**: Exclude converters, competitors

## Bidding Strategies

### Auto-Bid
- Snapchat optimizes bids automatically
- Best for: New campaigns, maximizing results

### Max Bid
- Set maximum cost per result
- Best for: Cost control, experienced advertisers

### Target Cost
- Maintain average cost per result
- Best for: Consistent CPA, scale

## Budget Management

**Minimum Budgets**:
- Daily: $5 USD
- Lifetime: $20 USD

**Budget Types**:
- Daily: Spend per day
- Lifetime: Total campaign spend

## Creative Best Practices

### Universal Requirements
- **Aspect Ratio**: 9:16 (vertical) for all formats
- **Resolution**: 1080 x 1920 px recommended
- **Safe Zone**: Keep content away from top/bottom 150 px
- **Audio**: Design for sound-on (60% watch with audio)
- **Branding**: Subtle, not dominant

### Video Best Practices
- Hook in first 2 seconds
- Mobile-shot aesthetic performs better
- Use captions for accessibility
- Keep messaging concise
- Include clear CTA

### Image Best Practices
- High-quality, well-lit photography
- Minimal text overlay
- Bold, eye-catching visuals
- Authentic, user-generated style

## Optimization Strategies

### Performance Monitoring
- Check metrics daily during first week
- Monitor: Impressions, swipe-up rate, conversions, CPA
- Adjust bids and budgets based on performance

### Creative Optimization
- Test 3-5 creative variations per ad squad
- Refresh creative every 2-4 weeks
- Use vertical video over static images
- A/B test CTAs and messaging

### Targeting Optimization
- Analyze performance by demographic segment
- Refine based on conversion data
- Expand with lookalike audiences
- Exclude low-performing segments

### Budget Optimization
- Allocate more to high-performing ad squads
- Pause underperformers after 7 days
- Scale budgets gradually (20% every 3-5 days)

## Snapchat Pixel Implementation

### Install Pixel

```html
<!-- Snapchat Pixel Code -->
<script type='text/javascript'>
(function(e,t,n){if(e.snaptr)return;var a=e.snaptr=function()
{a.handleRequest?a.handleRequest.apply(a,arguments):a.queue.push(arguments)};
a.queue=[];var s='script';r=t.createElement(s);r.async=!0;
r.src=n;var u=t.getElementsByTagName(s)[0];
u.parentNode.insertBefore(r,u);})(window,document,
'https://sc-static.net/scevent.min.js');

snaptr('init', 'YOUR_PIXEL_ID', {
'user_email': '__INSERT_USER_EMAIL__'
});

snaptr('track', 'PAGE_VIEW');
</script>
```

### Track Events

```javascript
// Purchase
snaptr('track', 'PURCHASE', {
  'price': 99.99,
  'currency': 'USD',
  'transaction_id': 'ORDER123'
});

// Add to Cart
snaptr('track', 'ADD_CART', {
  'price': 49.99,
  'currency': 'USD'
});

// Sign Up
snaptr('track', 'SIGN_UP');
```

## Measurement and Reporting

### Key Metrics
- **Impressions**: Ad views
- **Swipe-Up Rate**: Percentage who swiped up
- **Video Views**: 2-second views
- **Conversions**: Pixel events
- **ROAS**: Return on ad spend

### Attribution Windows
- 1-day, 7-day, or 28-day post-view
- 1-day, 7-day, or 28-day post-swipe

## Using the Reference Files

**`/references/snapchat-ad-specs.md`** — Read when preparing creative assets or verifying technical requirements.

**`/references/snapchat-targeting-guide.md`** — Read when setting up targeting or refining audience strategies.

**`/references/snapchat-pixel-setup.md`** — Read when implementing conversion tracking or troubleshooting pixel issues.

**`/references/snapchat-optimization-tactics.md`** — Read when optimizing campaigns or improving performance.
