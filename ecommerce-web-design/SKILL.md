---
name: ecommerce-web-design
description: "Design high-converting e-commerce websites and online stores. Use for: product page design, checkout optimization, shopping cart UX, mobile commerce, category navigation, trust signals, payment integration, and conversion rate optimization for online retail."
---

# E-Commerce Web Design

Design high-converting e-commerce websites that drive sales through optimized product pages, frictionless checkout, and trust-building UX patterns.

## Overview

E-commerce design directly impacts revenue — a 1% improvement in conversion rate on a $10M store equals $100K additional annual revenue. This skill covers the full e-commerce UX: product pages that sell, category navigation that guides discovery, cart and checkout flows that minimize abandonment, mobile-first commerce patterns, and trust signals that convert hesitant buyers. Every design decision is tied to measurable business outcomes.

## Page Type Design Guide

| Page Type | Primary Goal | Key Conversion Element | Avg. Bounce Rate | Reference |
|-----------|-------------|----------------------|-----------------|-----------|
| Homepage | Guide to categories/products | Hero + featured collections | 25–40% | `/references/product-pages.md` |
| Category/Collection | Browse and filter products | Filters + sort + grid layout | 30–50% | `/references/product-pages.md` |
| Product Detail (PDP) | Add to cart | CTA button + images + reviews | 35–55% | `/references/product-pages.md` |
| Cart | Proceed to checkout | Checkout button + upsell | 50–70% abandonment | `/references/checkout-optimization.md` |
| Checkout | Complete purchase | Form flow + payment options | 60–80% abandonment | `/references/checkout-optimization.md` |
| Search results | Find specific products | Relevant results + autocomplete | 20–40% | `/references/product-pages.md` |

## Product Page (PDP) Framework

### Above-the-Fold Elements (Priority Order)

| Element | Placement | Impact on Conversion | Best Practice |
|---------|-----------|---------------------|---------------|
| Product images (5–8) | Left 50–60% | Critical (+40% with zoom) | White background, lifestyle, scale, detail, video |
| Product title | Top right | High | Include key attributes (size, color, material) |
| Price + sale price | Below title | Critical | Show original price with strikethrough if on sale |
| Star rating + review count | Below price | +15–25% conversion | Link to reviews section |
| Variant selector | Below rating | Required for multi-variant | Visual swatches for color, dropdown for size |
| Add to Cart button | Prominent, high contrast | Critical | Full width on mobile, sticky on scroll |
| Availability/shipping | Near CTA | +5–10% conversion | "In stock — ships in 2 days" builds urgency |
| Trust badges | Near CTA | +5–15% conversion | Payment icons, security badge, guarantee |

### Below-the-Fold Content
1. Detailed product description (features + benefits)
2. Size guide or dimensions
3. Customer reviews with photos
4. Related/complementary products
5. FAQ or Q&A section
6. Return/exchange policy summary

## Checkout Optimization

### Checkout Flow Comparison

| Flow Type | Steps | Best For | Conversion Impact |
|-----------|-------|---------|-------------------|
| Single-page checkout | 1 | Simple products, low SKU count | +10–15% vs. multi-step |
| Multi-step (progress bar) | 3–4 | Complex orders, multiple shipping options | Standard, well-understood |
| One-click checkout | 0 (returning customers) | Repeat purchases, subscriptions | +20–30% for returning users |
| Guest checkout | 2–3 | All stores | Required — 35% abandon if forced to register |

### Cart Abandonment Recovery

| Tactic | Timing | Expected Recovery Rate |
|--------|--------|----------------------|
| Exit-intent popup (discount) | On mouse exit | 5–10% of abandoners |
| Abandoned cart email #1 | 1 hour after | 15–20% open rate |
| Abandoned cart email #2 | 24 hours after | 10–15% open rate |
| Abandoned cart email #3 (discount) | 72 hours after | 8–12% open rate |
| SMS reminder | 2–4 hours after (with consent) | 10–15% recovery |
| Retargeting ads | 1–7 days | 3–5% click-through |

### Checkout Form Optimization
- Default to shipping address = billing address (85% of orders)
- Auto-detect card type from first digits
- Use address autocomplete (Google Places API) to reduce typing
- Show order summary throughout checkout (not hidden behind a toggle)
- Offer 3+ payment methods minimum (credit card, PayPal, Apple Pay/Google Pay)
- Show security badges near payment fields

## Mobile Commerce Design

| Pattern | Implementation | Impact |
|---------|---------------|--------|
| Thumb-zone CTA placement | Add-to-cart in bottom 40% of screen | +15% tap rate |
| Sticky add-to-cart bar | Fixed bottom bar on product pages | +10% add-to-cart |
| Swipeable product images | Horizontal carousel with dots | Standard expectation |
| Simplified navigation | Hamburger → full-screen overlay | Reduces cognitive load |
| Bottom sheet cart preview | Slide-up mini-cart on add | Reduces page abandonment |
| Accelerated checkout | Apple Pay, Google Pay | Skips form entry entirely |

## Trust & Conversion Signals

| Signal | Placement | Conversion Impact |
|--------|-----------|-------------------|
| Security badge (SSL, Norton) | Checkout, near payment | +5–15% |
| Money-back guarantee | Product page, checkout | +10–20% |
| Free shipping threshold | Site-wide banner, cart | +15–25% AOV |
| Real customer reviews (with photos) | Product page | +15–25% conversion |
| Live chat availability | Floating widget | +10–15% conversion |
| Social proof ("X bought today") | Product page | +5–10% urgency |
| Clear return policy | Product page, footer | Reduces purchase anxiety |

## Performance Requirements

| Metric | Target | Revenue Impact of Missing Target |
|--------|--------|--------------------------------|
| Page load (LCP) | <2.5 seconds | -7% conversion per additional second |
| Time to interactive | <3.5 seconds | Users can't add to cart |
| Cumulative Layout Shift | <0.1 | Mis-clicks on wrong products |
| Image lazy loading | Below fold only | Reduces initial page weight |
| Core Web Vitals pass | All green | Google organic ranking factor |

## Best Practices

- **Every page is a landing page** — 60%+ of traffic enters on product or category pages, not homepage
- **Show the add-to-cart button without scrolling** — on every device
- **Offer guest checkout** — never force account creation before purchase
- **Use real product photography** — stock photos reduce trust on product pages
- **Display total cost early** — surprise shipping costs are the #1 abandonment reason
- **Test one thing at a time** — A/B test checkout changes with statistical significance before rolling out

## Using the Reference Files

**`/references/product-pages.md`** — Read when designing product detail pages, category pages, or search results. Covers image galleries, variant selectors, cross-sell layouts, and review displays.

**`/references/checkout-optimization.md`** — Read when optimizing cart and checkout flows. Covers form design, payment integration, abandonment recovery, and checkout A/B testing.

**`/references/mobile-commerce.md`** — Read when designing mobile shopping experiences. Covers thumb-zone layouts, mobile navigation, accelerated checkout, and responsive product grids.

**`/references/trust-conversion.md`** — Read when improving conversion rates. Covers trust signal placement, social proof strategies, urgency tactics, and persuasion principles.
