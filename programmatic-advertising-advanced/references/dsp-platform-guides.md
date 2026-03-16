# DSP Platform Guides

Detailed guides for major demand-side platforms (DSPs).

---

## The Trade Desk

### Platform Overview

**Company**: Independent DSP (publicly traded, NASDAQ: TTD)
**Founded**: 2009
**Headquarters**: Ventura, California
**Market Position**: Largest independent DSP globally

**Key Strengths**
- Most comprehensive inventory access (display, video, CTV, audio, native, DOOH)
- Transparent pricing and reporting
- Advanced targeting and optimization
- Strong data partnerships
- Excellent customer support

**Platform Fee**: 15-20% of media spend (negotiable for large spenders)

### Inventory Access

**Display**
- Google Ad Manager (AdX)
- All major SSPs (Magnite, PubMatic, OpenX, Index Exchange, etc.)
- 500+ billion daily display impressions

**Video**
- YouTube (via Google Ad Manager)
- All major video SSPs
- Premium publishers (Hulu, NBC, CBS, etc. via PMPs)

**Connected TV**
- Roku (programmatic access)
- Samsung Ads
- Vizio
- LG Ads
- Amazon Fire TV (via Amazon Publisher Services)
- 100+ CTV apps and FAST channels

**Audio**
- Spotify
- Pandora
- iHeartRadio
- SiriusXM
- Podcast inventory

**Native**
- Outbrain
- Taboola
- TripleLift
- Sharethrough

**Digital Out-of-Home (DOOH)**
- Vistar Media
- Place Exchange
- Broadsign

### Targeting Capabilities

**First-Party Data**
- Direct upload (CSV, API)
- Integration with data onboarding partners (LiveRamp, Neustar, etc.)
- Customer Match (email, address, phone, MAID)
- Website retargeting (via The Trade Desk pixel)

**Third-Party Data**
- 100+ data providers in marketplace
- Demographic, behavioral, intent, purchase data
- B2B data (Bombora, ZoomInfo, etc.)
- Transparent pricing (CPM or % of media)

**Contextual Targeting**
- Oracle Contextual Intelligence (Grapeshot)
- Peer39
- IAS Context Control
- Custom contextual categories

**Geographic Targeting**
- Country, state, DMA, city, zip code
- Custom geofences (lat/long coordinates)
- Radius targeting (around specific locations)

**Device Targeting**
- Desktop, mobile, tablet, CTV
- Operating system (iOS, Android, etc.)
- Device type (iPhone, Samsung Galaxy, etc.)
- Browser type

**Dayparting**
- Hour of day, day of week
- Custom daypart schedules
- Timezone-specific targeting

### Bidding & Optimization

**Bidding Strategies**
- Fixed CPM (set max bid)
- Optimized CPM (optimize for viewability, completion, etc.)
- CPC (cost per click)
- CPA (cost per acquisition)
- ROAS (return on ad spend)

**Koa (AI Optimization)**
- The Trade Desk's AI engine
- Predicts likelihood to convert
- Optimizes bids in real-time
- Learns from campaign data
- Requires 2-4 week learning period

**Bid Modifiers**
- Daypart modifiers
- Geographic modifiers
- Device modifiers
- Audience modifiers
- Frequency modifiers

### Measurement & Attribution

**Conversion Tracking**
- The Trade Desk pixel (JavaScript)
- Server-to-server (S2S) tracking
- Mobile app tracking (SDK)
- Offline conversion import

**Attribution Models**
- Last-touch
- First-touch
- Linear
- Time decay
- Position-based
- Data-driven (algorithmic)

**Third-Party Integrations**
- Google Analytics
- Adobe Analytics
- Salesforce
- Oracle
- LiveRamp
- Neustar

**Brand Lift Studies**
- Partner with Lucid, Dynata, etc.
- Custom surveys
- Exposed vs. control methodology

### Creative Specifications

**Display**
- Standard IAB sizes (300x250, 728x90, 160x600, 320x50, etc.)
- HTML5, static images (JPG, PNG, GIF)
- Max file size: 200KB (HTML5), 150KB (static)
- Third-party tags supported

**Video**
- VAST 2.0, 3.0, 4.0, 4.1
- MP4 (H.264 codec)
- Durations: 6s, 15s, 30s, 60s
- Aspect ratios: 16:9 (standard), 9:16 (vertical), 1:1 (square)

**Audio**
- MP3 or AAC
- Durations: 15s, 30s, 60s
- Bitrate: 128 kbps minimum

**Native**
- Title, description, image, CTA
- Image specs vary by publisher
- Dynamic creative supported

### Best Practices

1. **Start with Open Exchange, Graduate to PMPs**
   - Test audiences and creatives on open exchange
   - Identify top-performing publishers
   - Negotiate PMPs with those publishers

2. **Use Koa for Conversion Campaigns**
   - Enable Koa AI optimization
   - Provide 2-4 weeks for learning
   - Requires minimum 50-100 conversions per week

3. **Implement Supply Path Optimization**
   - Review supply path reports
   - Identify duplicate inventory
   - Consolidate to 3-5 preferred SSPs

4. **Leverage First-Party Data**
   - Upload customer lists
   - Create lookalike audiences
   - Retarget website visitors

5. **Monitor Fraud and Brand Safety**
   - Enable IAS or DoubleVerify
   - Use pre-bid blocking
   - Review brand safety reports weekly

---

## Google DV360 (Display & Video 360)

### Platform Overview

**Company**: Google (Alphabet)
**Formerly**: DoubleClick Bid Manager (DBM)
**Market Position**: Largest DSP by spend globally

**Key Strengths**
- Access to Google inventory (YouTube, GDN, etc.)
- Integration with Google ecosystem (Analytics, Ads, etc.)
- Advanced audience targeting (Google data)
- Strong in video and YouTube

**Platform Fee**: 10-15% (negotiable, often lower for large spenders)

### Inventory Access

**Google-Owned Inventory**
- YouTube (exclusive programmatic access)
- Google Display Network (GDN)
- Google Video Partners (CTV apps)
- Gmail ads

**Third-Party Inventory**
- Google Ad Manager (AdX) — largest SSP
- Other SSPs (Magnite, PubMatic, etc.)
- Display, video, native, audio, CTV

### Targeting Capabilities

**Google Audiences**
- Affinity audiences (interests)
- In-market audiences (purchase intent)
- Life events (moving, graduating, getting married, etc.)
- Detailed demographics (age, gender, parental status, household income)
- Custom intent audiences (based on search behavior)

**First-Party Data**
- Customer Match (email lists)
- Website retargeting (via Floodlight tags)
- App retargeting (via SDK)
- Lookalike audiences (Similar Audiences)

**Third-Party Data**
- Limited compared to other DSPs
- Oracle, Liveramp, Neustar integrations

**Contextual Targeting**
- Keyword targeting
- Topic targeting
- Placement targeting (specific sites/apps)
- Content exclusions

### Bidding & Optimization

**Bidding Strategies**
- Fixed CPM
- Viewable CPM (vCPM)
- CPC (cost per click)
- CPA (cost per acquisition)
- Target ROAS

**Smart Bidding**
- Google's AI-powered bidding
- Predicts conversion likelihood
- Optimizes bids in real-time
- Requires conversion tracking and learning period

**Bid Multipliers**
- Daypart, geography, device, audience
- Frequency-based bid adjustments

### Measurement & Attribution

**Floodlight Tags**
- Google's conversion tracking pixel
- Tracks website conversions
- Supports custom variables

**Google Analytics Integration**
- Link DV360 to Google Analytics
- View DV360 data in GA reports
- Create audiences in GA, activate in DV360

**Campaign Manager 360 (CM360)**
- Google's ad server and attribution platform
- Multi-touch attribution
- Cross-channel reporting
- Requires separate license

**Brand Lift Studies**
- Free for qualifying campaigns ($10K+ spend)
- Measures ad recall, awareness, consideration, intent
- Exposed vs. control methodology

### Creative Specifications

Similar to The Trade Desk (standard IAB specs)

**Display**: Standard IAB sizes, HTML5 or static
**Video**: VAST 2.0/3.0/4.0, MP4, 6s-60s
**Audio**: MP3/AAC, 15s-60s
**Native**: Title, description, image, CTA

### Best Practices

1. **Leverage Google Audiences**
   - Use in-market audiences for conversion campaigns
   - Use affinity audiences for awareness
   - Test custom intent audiences (based on search)

2. **Integrate with Google Analytics**
   - Create audiences in GA, activate in DV360
   - View DV360 performance in GA reports
   - Use GA conversion goals in DV360

3. **Use YouTube for Video**
   - DV360 has exclusive programmatic access to YouTube
   - Combine YouTube with other video inventory
   - Test TrueView vs. non-skippable

4. **Enable Smart Bidding for Conversions**
   - Use CPA or ROAS bidding for conversion campaigns
   - Provide 2-4 weeks for learning
   - Requires minimum 50 conversions per week

5. **Coordinate with Google Ads**
   - Use DV360 for programmatic, Google Ads for search
   - Share audiences between platforms
   - Unified reporting via Google Analytics

---

## Amazon DSP

### Platform Overview

**Company**: Amazon
**Market Position**: Fast-growing DSP, strong in e-commerce

**Key Strengths**
- Access to Amazon shopping data
- Fire TV and IMDb TV inventory
- Strong for e-commerce advertisers
- Self-serve option with no platform fee

**Platform Fee**: 
- Self-serve: $0 (no platform fee, only media cost)
- Managed service: 15% of media spend

### Inventory Access

**Amazon-Owned Inventory**
- Fire TV (exclusive programmatic access)
- IMDb TV (Amazon's FAST service)
- Twitch (live streaming)
- Amazon.com (display ads on product pages, search results)
- Kindle

**Third-Party Inventory**
- Display, video, CTV via Amazon Publisher Services (APS)
- Access to major SSPs

### Targeting Capabilities

**Amazon Shopping Data** (Unique Advantage)
- Purchase history (product categories, brands)
- Browsing behavior (products viewed, searched)
- Shopping frequency and recency
- Cart abandonment
- Prime membership status
- Subscribe & Save subscribers

**Demographic Targeting**
- Age, gender, household income
- Parental status
- Geographic targeting

**Behavioral Targeting**
- Streaming content preferences (Fire TV)
- Device usage patterns
- App engagement

**First-Party Data**
- Customer list matching
- Pixel-based retargeting
- Lookalike audiences

### Bidding & Optimization

**Bidding Strategies**
- Fixed CPM
- Dynamic CPM (optimize for clicks or conversions)
- CPC (cost per click)

**Optimization**
- Amazon's AI optimizes bids based on conversion likelihood
- Learns from Amazon shopping behavior
- Particularly effective for e-commerce campaigns

### Measurement & Attribution

**Amazon Attribution**
- Track Amazon product page visits
- Measure add-to-cart events
- Track purchase conversions
- Calculate ROAS
- Identify new-to-brand customers

**Cross-Device Tracking**
- Fire TV exposure to mobile/desktop conversion
- Amazon device graph

**Third-Party Measurement**
- Limited compared to other DSPs
- Supports IAS and DoubleVerify

### Creative Specifications

Similar to other DSPs (standard IAB specs)

**Display**: Standard IAB sizes
**Video**: VAST 2.0/3.0, MP4, 15s-60s
**CTV**: 1080p or 4K, 15s-60s

### Best Practices

1. **Leverage Amazon Shopping Data**
   - Target based on purchase history and browsing behavior
   - Use for competitive conquesting (target competitor's customers)
   - Retarget cart abandoners

2. **Use Amazon Attribution**
   - Track full funnel from ad exposure to Amazon purchase
   - Measure new-to-brand customers
   - Calculate true ROAS

3. **Target Prime Members**
   - Higher engagement and conversion rates
   - More frequent shoppers
   - Higher lifetime value

4. **Create Shoppable Ads**
   - Direct viewers to Amazon product pages
   - Use for Fire TV campaigns
   - Enable "Add to Cart" functionality

5. **Coordinate with Amazon Advertising**
   - Use DSP for awareness and consideration
   - Use Sponsored Products/Brands for conversion
   - Unified reporting via Amazon Advertising console

---

## Xandr (Microsoft Advertising)

### Platform Overview

**Company**: Microsoft (acquired from AT&T in 2021)
**Formerly**: AppNexus
**Market Position**: Premium publisher relationships, strong in video/CTV

**Key Strengths**
- Premium publisher inventory
- Strong in video and CTV
- Microsoft audience data (Bing, LinkedIn, Xbox)
- Advanced programmatic capabilities

**Platform Fee**: 10-15% (negotiable)

### Inventory Access

**Premium Publishers**
- NBC, CBS, Fox, ABC (via direct relationships)
- Hulu (programmatic access)
- Peacock
- Pluto TV
- Premium news publishers (CNN, NYT, WSJ, etc.)

**Third-Party Inventory**
- Display, video, CTV, native
- Access via Xandr's SSP (formerly AppNexus)

### Targeting Capabilities

**Microsoft Audience Data**
- Bing search behavior
- LinkedIn professional data (job title, company, industry, etc.)
- Xbox gaming behavior
- Microsoft 365 usage (aggregated, anonymized)

**First-Party Data**
- Customer list matching
- Website retargeting
- Lookalike audiences

**Third-Party Data**
- Oracle, LiveRamp, Neustar integrations
- B2B data providers

### Bidding & Optimization

**Bidding Strategies**
- Fixed CPM
- Optimized CPM
- CPC, CPA, ROAS

**Optimization**
- Machine learning-based optimization
- Predicts conversion likelihood
- Optimizes bids in real-time

### Measurement & Attribution

**Conversion Tracking**
- Xandr pixel (JavaScript)
- Server-to-server tracking
- Mobile app tracking

**Attribution**
- Multi-touch attribution
- Custom attribution models
- Cross-device attribution

**Third-Party Integrations**
- Google Analytics
- Adobe Analytics
- Salesforce

### Best Practices

1. **Focus on Premium Inventory**
   - Xandr's strength is premium publisher relationships
   - Use for brand campaigns requiring quality placements
   - Negotiate PMPs with premium publishers

2. **Leverage Microsoft Data**
   - Use Bing search data for intent-based targeting
   - Use LinkedIn data for B2B campaigns
   - Target Xbox users for gaming/entertainment campaigns

3. **Use for Video and CTV**
   - Strong inventory in video and CTV
   - Access to premium streaming services
   - Good for brand awareness campaigns

---

## Viant (Adelphic)

### Platform Overview

**Company**: Viant (publicly traded, NASDAQ: DSP)
**Market Position**: People-based DSP, household-level targeting

**Key Strengths**
- Household graph (250+ million US households)
- People-based targeting (not cookie-based)
- Strong first-party data capabilities
- Cross-device targeting

**Platform Fee**: 15-20%

### Inventory Access

**All Channels**
- Display, video, CTV, native, audio
- Access via major SSPs
- Strong in CTV (Roku, Samsung, Vizio, LG)

### Targeting Capabilities

**Household Graph** (Unique Advantage)
- 250+ million US households
- Connects devices to households
- Household-level targeting (not device or cookie)
- Privacy-compliant (people-based, not cookie-based)

**First-Party Data**
- Customer list matching (high match rates)
- Household-level matching
- Lookalike audiences

**Third-Party Data**
- Purchase data (credit card transactions)
- Demographic and behavioral data
- Household-level data

### Bidding & Optimization

**Bidding Strategies**
- Fixed CPM
- Optimized CPM
- CPA, ROAS

**Optimization**
- Household-level optimization
- Cross-device optimization
- Machine learning-based

### Measurement & Attribution

**Household-Level Measurement**
- Track conversions at household level
- Cross-device attribution
- Foot traffic attribution

### Best Practices

1. **Leverage Household Targeting**
   - Target at household level, not device level
   - Better for CTV and cross-device campaigns
   - Higher match rates for first-party data

2. **Use for Cross-Device Campaigns**
   - Viant's household graph connects all devices
   - Coordinate messaging across CTV, mobile, desktop
   - Measure cross-device conversions

3. **Focus on Privacy Compliance**
   - People-based targeting is more privacy-compliant than cookies
   - Good for post-cookie world
   - Less affected by iOS/browser restrictions
