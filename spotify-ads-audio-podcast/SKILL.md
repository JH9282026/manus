---
name: spotify-ads-audio-podcast
description: "Create and manage Spotify audio and podcast advertising campaigns including ad formats, creative specifications, targeting options, and measurement. Use for producing audio ads, podcast ad placement, understanding Spotify Ad Studio, implementing streaming context targeting, optimizing for audio engagement, and measuring audio ad performance across music and podcast inventory."
---

# Spotify Ads Audio and Podcast Advertising

Create and manage audio and podcast advertising campaigns on Spotify's streaming platform.

## Overview

Spotify offers audio and podcast advertising reaching 500+ million users through music streaming and podcast content. This skill covers audio ad creation, targeting strategies, and performance optimization.

## Ad Formats

### Audio Ads (Music)
- **Duration**: Maximum 30 seconds
- **Placement**: Between songs for free users
- **Devices**: Mobile, desktop, tablet, web, gaming consoles, smart TVs, connected speakers, in-car, wearables
- **Companion**: Required companion image (1x1, 600x600 px min)

### Podcast Ads
- **Pre-Roll**: Up to 30 seconds (Ads Manager and Direct IO)
- **Mid-Roll**: Up to 60 seconds (Direct IO only)
- **Placement**: Before or during podcast episodes
- **Engagement**: 81% of listeners take action after hearing podcast ads

### Video Ads
- **Duration**: Up to 30 seconds (standard), up to 60 seconds (long-form, select markets)
- **Placement**: Mobile and desktop
- **Format**: Vertical or horizontal video

## Audio Ad Specifications

### Audio File Requirements
- **Format**: MP3 or WAV (music ads); MP3 (podcast ads Direct IO)
- **File Size**: 50 MB max (music ads); 1 MB max (podcast ads)
- **Sample Rate**: 44.1 kHz
- **Bit Rate**: 192 kbps minimum, 320 kbps maximum
- **Loudness**: -16 LUFS (+/- 1.5 LUFS) integrated average, -2.0 dBTP True Peak limit
- **Channels**: Stereo

### Script Requirements
- **30-Second Ad**: Maximum 65 words
- **60-Second Ad**: Maximum 100 words
- **Tone**: Conversational, authentic
- **CTA**: Must reflect campaign CTA selection

### Companion Image
- **Aspect Ratio**: 1x1 (square)
- **Minimum Dimensions**: 600 x 600 pixels
- **File Size**: Up to 200 KB
- **Format**: JPEG or PNG
- **Purpose**: Displayed when listeners engage with app during ad break

### Canvas (Optional Looping Visual)
- **Aspect Ratio**: 9x16 (vertical)
- **Minimum Height**: 720 pixels
- **Duration**: 3-8 seconds
- **Format**: MP4 or MOV
- **File Size**: 200 KB maximum
- **Purpose**: Full-screen visual for mobile ad breaks

## Creative Best Practices

### Audio Script Writing
- **Hook Immediately**: Capture attention in first 3 seconds
- **Conversational Tone**: Speak naturally, avoid overly promotional language
- **Clear Message**: One key message per ad
- **Strong CTA**: Tell listeners exactly what to do next
- **Brand Mention**: Include brand name 2-3 times
- **Memorable**: Use music, sound effects, or unique voice

### Voice and Production
- **Professional Voiceover**: Clear, engaging delivery
- **Music Bed**: Background music that complements message (optional)
- **Sound Effects**: Enhance storytelling (use sparingly)
- **Mixing**: Balance voice, music, and effects
- **Quality**: Studio-quality recording

### Companion Image Design
- **High-Quality**: Professional photography or design
- **Brand Visible**: Logo and brand name clear
- **Product Focus**: Show product or key visual
- **Text Minimal**: Image should stand alone
- **Mobile-Optimized**: Legible on small screens

## Targeting Options

### Demographics
- **Age**: 18-24, 25-34, 35-44, 45-54, 55-64, 65+
- **Gender**: Male, Female, All
- **Location**: Country, region, DMA, city, postal code

### Streaming Context
- **Playlist Context**: Workout, party, focus, chill, cooking, gaming, etc.
- **Music Genre**: Pop, rock, hip-hop, country, electronic, etc.
- **Podcast Topics**: News, true crime, comedy, business, sports, etc.

### Interests
- **Lifestyle**: Fitness, food, travel, fashion, technology
- **Behaviors**: Commuters, students, parents
- **Real-Time**: Contextual targeting based on current listening

### First-Party Data
- **Customer Lists**: Upload email lists for targeting
- **Website Visitors**: Retarget site visitors (requires Spotify Pixel)
- **Lookalike Audiences**: Reach similar users

## Campaign Setup (Spotify Ad Studio)

### Step 1: Campaign Objective
- **Awareness**: Maximize reach and impressions
- **Consideration**: Drive website visits and engagement
- **Conversions**: Drive purchases and signups

### Step 2: Targeting
- Select demographics, location, interests
- Choose streaming context (playlist, genre, podcast topics)
- Add first-party audiences (optional)

### Step 3: Budget and Schedule
- **Minimum Budget**: $250 USD
- **Budget Type**: Total campaign budget
- **Schedule**: Start and end dates
- **Pacing**: Even or accelerated

### Step 4: Creative
- Upload audio file (or use AI script generator)
- Upload companion image
- Add optional canvas
- Set advertiser name and tagline
- Choose call-to-action

### Step 5: Review and Launch
- Review all settings
- Submit for approval (typically 24-48 hours)
- Launch campaign

## AI-Powered Creative Tools

### Spotify AI Script Generator
- **Input**: Product description, key message, tone
- **Output**: 30-second script
- **Voiceover**: AI-generated voiceover (multiple voice options)
- **Cost**: Free (included in Spotify Ad Studio)
- **Customization**: Edit script and regenerate

### Benefits
- Fast creative production
- Professional-quality voiceover
- Multiple variations for testing
- No additional cost

## Measurement and Optimization

### Key Metrics
- **Impressions**: Number of times ad played
- **Reach**: Unique listeners
- **Frequency**: Average impressions per listener
- **Listen-Through Rate**: Percentage who listened to full ad
- **Click-Through Rate**: Clicks on companion image
- **Conversions**: Pixel-tracked actions
- **Brand Lift**: Measured via Spotify Brand Lift studies

### Attribution
- **Click Attribution**: 1-day, 7-day, or 28-day windows
- **View Attribution**: 1-day or 7-day windows
- **Cross-Device**: Spotify tracks logged-in users across devices

### Optimization Tips
- **Test Multiple Creatives**: Run 2-3 audio variations
- **Refresh Creative**: Update every 4-6 weeks
- **Optimize Targeting**: Refine based on performance data
- **Adjust Budget**: Allocate more to high-performing segments
- **Monitor Frequency**: Keep below 3-4 impressions per user per week

## Programmatic Advertising

### Spotify Ad Exchange (SAX)
- **Access**: Real-time bidding for audio, video, display
- **Platforms**: Google Display & Video 360, Magnite, The Trade Desk
- **Inventory**: Music streaming (podcast support planned)
- **Regions**: US, Canada, Europe, Australia, New Zealand, India, Singapore, Brazil, Mexico

### Programmatic Guaranteed
- **Direct Buys**: Reserve inventory with publishers
- **Formats**: Audio, video, display
- **Integration**: Google Ad Manager
- **Benefits**: Guaranteed impressions, premium placements

## Spotify Pixel Implementation

### Install Pixel
```html
<script>
!function(s,p,o,t,i,f,y){s[i]||(s[i]=function(){(s[i].q=s[i].q||[]).push(arguments)},
(f=p.createElement(o)).async=1,f.src=t,
(y=p.getElementsByTagName(o)[0]).parentNode.insertBefore(f,y))}
(window,document,'script','https://pixel.spotify.com/v1/pixel.js','sp');

sp('init', 'PIXEL_ID');
sp('track', 'PageView');
</script>
```

### Track Conversions
```javascript
// Purchase
sp('track', 'Purchase', {
  value: 99.99,
  currency: 'USD',
  transaction_id: 'ORDER123'
});

// Add to Cart
sp('track', 'AddToCart', {
  value: 49.99,
  currency: 'USD'
});
```

## Using the Reference Files

**`/references/spotify-audio-production.md`** — Read when producing audio ads or optimizing audio quality.

**`/references/spotify-targeting-strategies.md`** — Read when setting up targeting or refining audience strategies.

**`/references/spotify-creative-examples.md`** — Read when seeking inspiration or understanding successful audio campaigns.

**`/references/spotify-measurement-guide.md`** — Read when analyzing performance or setting up conversion tracking.

## References

- [01 Spotify Advertising Platform Overview](references/01_spotify_advertising_platform_overview.md)
- [02 Podcast Advertising Fundamentals](references/02_podcast_advertising_fundamentals.md)
- [03 Creating Effective Podcast Ads](references/03_creating_effective_podcast_ads.md)
- [04 Podcast Marketing Strategies](references/04_podcast_marketing_strategies.md)
- [05 Measurement Optimization Roi](references/05_measurement_optimization_roi.md)
