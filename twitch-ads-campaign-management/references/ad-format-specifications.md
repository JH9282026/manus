# Twitch Ad Format Technical Specifications

Complete technical requirements for all Twitch advertising formats available through Amazon Ads.

---

## Premium Video Specifications

### Standard Premium Video

**Placement:** Pre-roll and mid-roll across desktop, mobile, tablet, console, streaming TV

**Video Specifications:**
- **Length:** 6s, 15s, 20s, 30s, 60s (60s has additional fees, mid-roll only)
- **Resolution:** 1920x1080 (first-party serving)
- **Minimum Bitrate:** 4,000 kbps
- **Maximum Bitrate:** 10,000 kbps
- **Recommended Bitrate:** 6,000-8,000 kbps
- **Audio:** -9dB peak audio level
- **File Format:** H.264 (MP4)
- **Frame Rate:** 24-30fps
- **Aspect Ratio:** 16:9
- **Maximum File Size:** 500MB (site served)

**Third-Party Serving (VAST):**

Mandatory video transcodes required:
- 1920x1080 @ 4,000 kbps
- 1280x720 @ 2,200 kbps
- 854x480 @ 1,200 kbps
- 640x360 @ 550 kbps

**Tracking Support:**
- Impressions: Yes
- Clicks: Yes
- Quartiles: Yes (25%, 50%, 75%, 100%)
- Completes: Yes
- VAST 2.0: Supported
- VAST 3.0: Supported
- VAST 4.0: Not supported
- VPAID: Not supported

**Features:**
- 100% above the fold
- Unskippable
- Clickable (except on consoles and streaming devices)
- SureStream delivery (bypasses ad blockers)

---

## Vertical Video Ad Specifications

### 9:16 Vertical Format

**Placement:**
- Desktop: Silent, adjacent to livestream
- Mobile: Unmuted, skippable, full-screen in feed

**Video Specifications:**
- **Length:** 6s, 15s, 20s, 30s
- **Resolution:** 1080x1920 (site served)
- **Aspect Ratio:** 9:16
- **Minimum Bitrate:** 4mbps (site served)
- **Recommended Bitrate:** 8mbps
- **Maximum File Size:** 500MB (site served only)
- **Video Frame Rate:** 23.976 (recommended), 24, 25, or 29.97
- **Video Frame Rate Mode:** Constant
- **Audio:** -9dB peak audio level
- **Minimum Audio Bitrate:** 192kbps
- **Audio Sample Rate:** 44.1kHz or 48kHz
- **Audio Channel:** Minimum 2-channels
- **Supported Video Formats:** H.264, MPEG-2, or MPEG-4
- **Supported Audio Formats:** AAC

**Third-Party Serving:**
- **Resolution:** 360x640
- **Minimum Bitrate:** 2mbps
- **Minimum Audio Bitrate:** 128kbps

**Ad Serving:**
- First-party (site served)
- Third-party (with reduced specs)

**Design Considerations:**
- Optimize for mobile-first viewing
- Design for sound-off (desktop) and sound-on (mobile)
- Use bold, readable text
- Vertical framing for subjects
- Front-load key message

---

## First Impression Takeover Specifications

### Exclusive Daily Placement

**Placement:** Viewer's first watched broadcast of the day

**Video Specifications:**
- **Length:** Up to 30 seconds, unskippable
- **Resolution:** 1920x1080 minimum
- **Minimum Bitrate:** 4,000 kbps
- **Maximum Bitrate:** 10,000 kbps
- **Audio:** -9dB peak audio level
- **File Format:** H.264 (MP4)
- **Frame Rate:** 24-30fps

**Third-Party Serving (VAST):**

Mandatory transcodes:
- 1920x1080 @ 5,500 kbps
- 1280x720 @ 3,100 kbps
- 854x480 @ 1,200 kbps
- 640x360 @ 550 kbps
- 284x160 @ 180 kbps

**Tracking Support:**
- Impressions: Yes
- Clicks: Yes
- Quartiles: Yes
- Completes: Yes

**Availability:**
- Sold on per-day, per-geographic basis
- Exclusive: one advertiser per day per geo
- Premium pricing

---

## Display Ad Specifications

### Stream Display Ads

**Placement:**
- Between live stream and chat
- Directly below live stream

**Specifications:**
- **Format:** IAB standard display sizes
- **File Types:** JPEG, PNG, GIF (static or animated)
- **Maximum File Size:** 150KB per creative
- **Animation:** Maximum 30 seconds loop
- **SSL:** Required (all components must use HTTPS)

**Common Sizes:**
- 300x250 (Medium Rectangle)
- 728x90 (Leaderboard)
- 300x600 (Half Page)
- 160x600 (Wide Skyscraper)

**Features:**
- Clickable
- Above or adjacent to stream content
- Integrated into viewing experience

### Mid-Feed Ads

**Placement:** Within Twitch mobile app feed

**Specifications:**
- **Format:** Mobile-optimized display
- **Orientation:** Portrait and landscape support
- **File Types:** JPEG, PNG
- **Maximum File Size:** 150KB
- **Aspect Ratio:** 1:1 or 16:9
- **SSL:** Required

**Features:**
- Full-screen clickable
- Native feed integration
- Mobile-only placement

### Super Leaderboard

**Placement:** Top of page, homepage, browse pages

**Specifications:**
- **Size:** 970x90 (IAB standard)
- **File Types:** JPEG, PNG, GIF
- **Maximum File Size:** 150KB
- **Animation:** Maximum 30 seconds loop
- **SSL:** Required

**Features:**
- Wide banner format
- High visibility
- Clickable

### Medium Rectangle

**Placement:** Embedded in search content, browse pages

**Specifications:**
- **Size:** 300x250 (IAB standard)
- **File Types:** JPEG, PNG, GIF
- **Maximum File Size:** 150KB
- **Animation:** Maximum 30 seconds loop
- **Maximum Per Page:** 2
- **SSL:** Required

**Features:**
- Contextual placement
- Search integration
- Clickable

---

## Headliner Specifications

### Premium Homepage Placement

**Placement:**
- Twitch desktop homepage
- Twitch mobile app default landing page

**Specifications:**
- **Format:** Custom high-impact unit
- **Position:** Above the fold
- **File Types:** JPEG, PNG, or video
- **SSL:** Required

**Features:**
- Premium cross-screen placement
- Clickable
- Maximum visibility
- Custom creative requirements (contact Twitch team)

---

## Sponsorship Format Specifications

### Streamables

**Placement:** Twitch Partnered mobile games

**Specifications:**
- **Length:** 30 seconds
- **Format:** Full-screen livestream experience
- **Interaction:** Viewer opt-in
- **Skippable:** No

**Features:**
- Viewer-initiated engagement
- Full-screen immersive experience
- Mobile gaming integration

### Homepage Carousel

**Placement:** Twitch homepage rotating carousel

**Specifications:**
- **Text:** Maximum 240 characters
- **Image:** Custom thumbnail (specs provided by Twitch team)
- **Link:** To livestream channel or content

**Features:**
- Promotes livestream channel content
- Rotating placement
- Homepage visibility

---

## General Technical Requirements

### SSL Compliance

**All ads must be SSL-compliant:**
- All creative components served via HTTPS
- Third-party tracking pixels must use HTTPS
- No mixed content (HTTP and HTTPS)
- All vendor tags must be SSL-compliant

### Unsupported Features

**The following are NOT supported:**
- Skip functions (except Vertical Video on mobile)
- Geo/browser/other targeting on third-party end
- Third-party redirecting
- 4th-party tags
- VAST 4.0
- VPAID
- Auto-play audio on display ads

### Creative Delivery Lead Times

**Standard Timeline:**
- Submit creatives 5-7 business days before campaign start
- Allow 2-3 business days for review and approval
- Plan for potential revision requests
- Rush approvals may not be available

**Approval Process:**
1. Submit creative assets to Twitch team
2. Twitch reviews for compliance with Advertising Guidelines
3. Technical QA testing
4. Approval or revision request
5. Final approval and campaign scheduling

---

## Locales and Availability

### Supported Regions

**North America:**
- United States
- Canada
- Mexico

**South America:**
- Brazil
- Argentina
- Chile

**Europe:**
- United Kingdom
- Germany
- France
- Spain
- Italy
- Netherlands
- Poland
- Sweden
- Norway
- Denmark
- Finland

**Middle East:**
- United Arab Emirates
- Saudi Arabia

**Asia Pacific:**
- Japan
- South Korea
- Australia
- New Zealand
- Taiwan
- Thailand
- Singapore

**Regional Considerations:**
- Ad specs consistent across regions
- Language localization recommended
- Cultural adaptation for creative content
- Regional pricing variations
- Locale-specific compliance requirements

---

## Quality Assurance Checklist

### Pre-Submission Testing

**Video Ads:**
- [ ] Correct resolution and aspect ratio
- [ ] Bitrate within specified range
- [ ] Audio levels at -9dB
- [ ] Proper encoding (H.264 MP4)
- [ ] Frame rate 24-30fps
- [ ] File size under maximum
- [ ] Logo/brand name visible
- [ ] Subtitles included (recommended)
- [ ] Test playback on multiple devices
- [ ] Verify HTTPS delivery

**Display Ads:**
- [ ] Correct dimensions (IAB standard)
- [ ] File size under 150KB
- [ ] Animation under 30 seconds
- [ ] SSL-compliant delivery
- [ ] Clickable CTA clear and functional
- [ ] Logo prominently featured
- [ ] High contrast for visibility
- [ ] Test rendering on dark backgrounds

**Third-Party Tags:**
- [ ] All required transcodes provided
- [ ] VAST 2.0 or 3.0 compliance
- [ ] SSL-compliant tracking pixels
- [ ] No 4th-party tags
- [ ] No unsupported targeting parameters
- [ ] Test tag functionality
- [ ] Verify tracking events fire correctly

### Compliance Verification

- [ ] Adheres to Twitch Advertising Guidelines
- [ ] Complies with Twitch Community Guidelines
- [ ] No prohibited content
- [ ] Accurate and verifiable claims
- [ ] Age-appropriate content
- [ ] Proper disclosures (if applicable)
- [ ] FTC compliance for sponsored content
- [ ] Regional compliance requirements met