---
name: app-store-optimization
description: "Optimize mobile app visibility and conversion in app stores through keyword research, metadata optimization, visual assets, ratings management, and A/B testing. Use for: improving app store rankings, conducting keyword research, optimizing app titles and descriptions, creating compelling screenshots and videos, managing ratings and reviews, implementing A/B testing, localizing app listings, analyzing ASO metrics, and increasing organic downloads for iOS App Store and Google Play."
---

# App Store Optimization (ASO)

Optimize mobile app visibility and conversion rates in app stores to drive organic downloads.

## Overview

App Store Optimization (ASO) is the process of improving an app's visibility in app stores (Apple App Store, Google Play) and increasing conversion rates from impressions to downloads. ASO is the mobile equivalent of SEO and is crucial for organic user acquisition. This skill covers keyword research, metadata optimization, visual assets, ratings management, A/B testing, and analytics.

## Why ASO Matters

**Statistics:**
- 70% of App Store users use search to discover apps
- 65% of downloads happen directly after a search
- Top 3 search results get 70% of clicks
- Proper ASO can increase downloads by 2-3x

**Benefits:**
- Increased organic visibility
- Lower user acquisition costs
- Higher quality users (intent-driven)
- Sustainable growth
- Competitive advantage

## ASO Components

### 1. Keyword Research

**Goal:** Identify high-traffic, relevant keywords with manageable competition.

**Process:**
1. Brainstorm seed keywords (app functionality, problem solved)
2. Analyze competitor keywords
3. Use ASO tools (App Annie, Sensor Tower, Mobile Action)
4. Evaluate keyword metrics:
   - Search volume
   - Competition/difficulty
   - Relevance to app

**Keyword Types:**
- **Head terms:** 1-2 words, high volume, high competition (e.g., "fitness")
- **Long-tail:** 3+ words, lower volume, better conversion (e.g., "home workout for beginners")

### 2. App Title/Name

**Importance:** Most influential factor for search ranking.

**Best Practices:**

| Platform | Character Limit | Best Practice |
|----------|----------------|---------------|
| **iOS** | 30 characters | Brand + primary keyword |
| **Google Play** | 30 characters | Brand + primary keyword |

**Examples:**
- ✅ "Calm: Sleep & Meditation"
- ✅ "Duolingo: Language Lessons"
- ❌ "MyApp" (no keywords)
- ❌ "Best Fitness Workout Exercise Gym App" (keyword stuffing)

**Tips:**
- Include primary keyword
- Keep brand recognizable
- Avoid keyword stuffing
- Test variations with A/B testing

### 3. Subtitle (iOS) / Short Description (Google Play)

**iOS Subtitle:**
- 30 characters
- Appears below app name in search results
- Indexed for search
- Use for secondary keywords

**Google Play Short Description:**
- 80 characters
- Appears in search results
- Indexed for search
- Compelling value proposition

### 4. Description

**iOS:**
- 4,000 characters
- NOT indexed for search (use for conversion)
- Focus on benefits, features, social proof

**Google Play:**
- 4,000 characters
- IS indexed for search
- Include keywords naturally (2-3% density)
- First 3 lines visible without expanding

**Structure:**
1. **Hook:** Compelling opening (problem/solution)
2. **Features:** Bullet points of key features
3. **Benefits:** How it improves user's life
4. **Social Proof:** Awards, press, user testimonials
5. **Call to Action:** Encourage download

### 5. Keywords Field (iOS Only)

- 100 characters
- Hidden from users
- Comma-separated, no spaces
- Don't repeat keywords from title/subtitle
- Include synonyms, alternate spellings, competitors

**Example:** "exercise,workout,gym,training,fitness,health,wellness"

### 6. Visual Assets

**App Icon:**
- First impression
- Recognizable at small sizes
- Consistent with brand
- A/B test variations
- Avoid text (hard to read at small sizes)

**Screenshots:**
- Most influential for conversion
- Show app in action
- Highlight key features
- Use text overlays to explain benefits
- First 2-3 screenshots most important (visible without scrolling)
- Optimize for different device sizes

**Best Practices:**
- Show UI in context
- Highlight unique features
- Use captions/annotations
- Show happy users (if applicable)
- Maintain visual consistency

**Preview Video (Optional but Recommended):**
- 15-30 seconds
- Autoplay (muted) in App Store
- Show app functionality
- Use captions (most watch muted)
- Compelling first 3 seconds

### 7. Category Selection

**Primary Category:**
- Choose most relevant category
- Affects discoverability in category browsing
- Consider competition (niche category may be easier to rank)

**Secondary Category (iOS):**
- Additional discoverability opportunity

### 8. Ratings and Reviews

**Impact:**
- Higher ratings = better visibility
- Reviews provide social proof
- Influence conversion rate

**Strategies:**
- Prompt for reviews at optimal moments (after positive experience)
- Respond to all reviews (shows you care)
- Address negative feedback
- Fix issues mentioned in reviews
- Use iOS/Android in-app review prompts

**iOS Review Prompt:**
```swift
import StoreKit

SKStoreReviewController.requestReview()
```

**Android Review Prompt:**
```kotlin
val manager = ReviewManagerFactory.create(context)
val request = manager.requestReviewFlow()
request.addOnCompleteListener { task ->
    if (task.isSuccessful) {
        val reviewInfo = task.result
        manager.launchReviewFlow(activity, reviewInfo)
    }
}
```

## Platform Differences

| Aspect | iOS App Store | Google Play |
|--------|---------------|-------------|
| **Title** | 30 chars | 30 chars |
| **Subtitle/Short Desc** | 30 chars (subtitle) | 80 chars (short desc) |
| **Description Indexed** | No | Yes |
| **Keyword Field** | Yes (100 chars) | No |
| **Backlinks** | Not a factor | Ranking factor |
| **Update Frequency** | Affects ranking | Affects ranking |
| **Screenshots in Search** | Yes | Only for branded searches |

## A/B Testing

**What to Test:**
- App icon
- Screenshots
- Preview video
- Short description (Google Play)

**Tools:**
- **iOS:** Product Page Optimization (in App Store Connect)
- **Android:** Store Listing Experiments (in Play Console)

**Best Practices:**
- Test one element at a time
- Run tests for at least 7 days
- Ensure statistical significance
- Implement winning variants

## Localization

**Benefits:**
- Reach non-English speaking markets
- Increase downloads by 20-40% per language
- Competitive advantage in local markets

**What to Localize:**
- App name (if appropriate)
- Subtitle/short description
- Description
- Keywords
- Screenshots (with localized text)
- Preview video

**Priority Languages:**
- Spanish, Chinese (Simplified), Japanese, German, French, Portuguese, Russian, Korean

## ASO Tools

| Tool | Features | Pricing |
|------|----------|---------|
| **App Annie** | Market data, keyword research, competitor analysis | Paid |
| **Sensor Tower** | ASO, market intelligence, ad intelligence | Paid |
| **Mobile Action** | Keyword tracking, ASO optimization | Paid |
| **AppTweak** | ASO, market intelligence | Paid |
| **TheTool** | Keyword research, ASO | Freemium |
| **App Radar** | ASO, keyword tracking | Freemium |

## Metrics to Track

**Visibility Metrics:**
- Keyword rankings
- Category rankings
- Impressions
- Search visibility score

**Conversion Metrics:**
- Conversion rate (impressions → downloads)
- Page views
- Downloads
- Install rate

**Engagement Metrics:**
- Ratings
- Reviews
- Retention rate
- Uninstall rate

## ASO Workflow

### 1. Research Phase
- Competitor analysis
- Keyword research
- Market analysis

### 2. Optimization Phase
- Optimize metadata
- Create/update visual assets
- Implement keywords

### 3. Testing Phase
- A/B test variations
- Monitor metrics
- Iterate based on data

### 4. Maintenance Phase
- Track keyword rankings
- Monitor competitor changes
- Update for seasonal trends
- Respond to reviews
- Regular updates (signals active development)

## Best Practices

1. **Focus on Relevance:** Choose keywords that accurately describe your app
2. **Monitor Competitors:** Learn from successful apps in your category
3. **Update Regularly:** Fresh content signals active development
4. **Respond to Reviews:** Shows you care about users
5. **Test Continuously:** A/B test to optimize conversion
6. **Localize:** Expand to international markets
7. **Track Metrics:** Data-driven decisions
8. **Avoid Black Hat:** No fake reviews, keyword stuffing, misleading screenshots
9. **Optimize for Conversion:** Visibility is useless without downloads
10. **Be Patient:** ASO is a long-term strategy

## Common Mistakes

- Keyword stuffing
- Ignoring visual assets
- Not responding to reviews
- Choosing wrong category
- Not localizing
- Neglecting A/B testing
- Focusing only on rankings (not conversion)
- Copying competitors blindly
- Not tracking metrics

## Using the Reference Files

**`/references/keyword-research-guide.md`** — Read when conducting keyword research, using ASO tools, or analyzing competitor keywords.

**`/references/visual-assets-guide.md`** — Read when creating app icons, screenshots, or preview videos for maximum conversion.

**`/references/aso-tools-comparison.md`** — Read when choosing ASO tools, understanding tool features, or setting up ASO tracking.
