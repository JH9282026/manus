# Snapchat AR Lenses and Filters Advertising Guide

A comprehensive guide to creating, deploying, and optimizing Augmented Reality (AR) advertising experiences on Snapchat.

## Understanding AR Advertising on Snapchat

### The AR Opportunity

Augmented Reality is central to Snapchat's platform and advertising ecosystem:

- **Over 75% of daily active users** engage with AR features
- **AR Lenses are used billions of times daily**
- **6.4X higher purchase intent** compared to traditional video ads
- **250+ million Snapchatters** engage with AR shopping features monthly

### AR Lenses vs. AR Filters

Snapchat offers two distinct AR advertising formats:

| Feature | AR Lenses | AR Filters |
|---------|-----------|------------|
| **Timing** | Pre-capture (before taking photo/video) | Post-capture (after taking photo/video) |
| **Interactivity** | Highly interactive, real-time effects | Static graphic overlays |
| **Technology** | Facial recognition, 3D objects, world effects | 2D graphics, text, logos |
| **Complexity** | More complex to create | Simpler to create |
| **Engagement** | Higher engagement, longer interaction time | Quick application, easy sharing |
| **Use Cases** | Product try-ons, games, immersive experiences | Event promotion, branding, announcements |
| **Creation Tools** | Lens Studio (advanced) or Lens Web Builder | Lens Web Builder (simple) |
| **Cost** | Higher production and media costs | Lower production and media costs |

## AR Lenses: Deep Dive

### Types of AR Lenses

#### 1. Face Lenses

**Description**: Effects that track and augment the user's face in real-time.

**Capabilities**:
- Facial feature tracking (eyes, nose, mouth, eyebrows)
- Face morphing and distortion
- Virtual makeup application
- Accessories (glasses, hats, jewelry)
- Animated effects triggered by facial expressions

**Use Cases**:
- **Beauty brands**: Virtual makeup try-on (lipstick, eyeshadow, foundation)
- **Eyewear brands**: Virtual glasses try-on
- **Entertainment**: Movie character transformations
- **Fashion**: Virtual accessories (hats, earrings, headbands)

**Example**: A cosmetics brand creates a Lens allowing users to try on 5 different lipstick shades, with tap-to-change functionality.

#### 2. World Lenses

**Description**: Effects that augment the environment around the user, not their face.

**Capabilities**:
- 3D object placement in real-world space
- Ground plane detection
- Surface tracking
- Environmental effects (particles, weather, lighting)

**Use Cases**:
- **Furniture brands**: Visualize furniture in user's home
- **Automotive**: Place virtual car in driveway
- **Retail**: Visualize products in real-world context
- **Entertainment**: Place branded 3D characters in environment

**Example**: A furniture retailer creates a Lens allowing users to place a virtual sofa in their living room to see how it fits and looks.

#### 3. Marker-Based Lenses

**Description**: Effects triggered by scanning specific images, logos, or QR codes.

**Capabilities**:
- Image recognition and tracking
- Augmented content overlaid on physical markers
- Product packaging activation
- Print ad activation

**Use Cases**:
- **Product packaging**: Scan product to unlock AR experience
- **Print advertising**: Scan magazine ad to activate AR content
- **Event marketing**: Scan event poster for exclusive content
- **Retail displays**: Scan in-store display for product information

**Example**: A beverage brand prints Snapcodes on bottles; scanning unlocks an AR game where users catch falling ingredients.

#### 4. Body Tracking Lenses

**Description**: Effects that track and augment the user's full body or specific body parts (hands, feet).

**Capabilities**:
- Full-body tracking
- Hand tracking and gesture recognition
- Virtual clothing try-on
- Body-based games and interactions

**Use Cases**:
- **Fashion brands**: Virtual clothing try-on
- **Footwear brands**: Virtual shoe try-on
- **Fitness**: Interactive workout experiences
- **Gaming**: Body-controlled AR games

**Example**: A sneaker brand creates a Lens allowing users to virtually try on different shoe styles by pointing the camera at their feet.

#### 5. Voice-Activated Lenses

**Description**: Effects triggered or controlled by voice commands or sound.

**Capabilities**:
- Voice command recognition
- Sound-reactive animations
- Music-synced effects
- Speech-to-text integration

**Use Cases**:
- **Music promotion**: Effects that react to specific songs
- **Voice-controlled games**: AR games controlled by voice
- **Interactive storytelling**: Narrative experiences triggered by voice

**Example**: A music artist creates a Lens that activates special effects when users say the song title or play the track.

### AR Lens Technical Specifications

#### General Requirements

- **File Size**: Maximum 8 MB compressed
- **Creation Tools**: Lens Studio (desktop app) or Lens Web Builder (browser-based)
- **Branding**: Logo required (top left or top right corner)
- **Sponsored Label**: Snapchat automatically adds "SPONSORED" slug for 2 seconds
- **Safe Zone**: Keep important content away from top 150px and bottom 150px

#### Performance Requirements

- **Frame Rate**: Maintain 30 FPS minimum on target devices
- **Load Time**: Lens should load in under 3 seconds
- **Device Compatibility**: Test on range of devices (iOS and Android, various models)
- **Battery Impact**: Optimize to minimize battery drain

#### Asset Specifications

**3D Models**:
- Format: FBX, OBJ, or glTF
- Polygon count: Keep under 50,000 triangles for optimal performance
- Textures: Maximum 2048x2048 pixels, use texture atlases when possible

**Images**:
- Format: PNG (with transparency) or JPG
- Resolution: Power of 2 (512x512, 1024x1024, 2048x2048)
- Compression: Optimize for file size without sacrificing quality

**Audio**:
- Format: MP3 or WAV
- Duration: Keep under 30 seconds
- File size: Minimize to reduce overall Lens size

### Creating AR Lenses

#### Option 1: Lens Studio (Advanced)

**Lens Studio** is Snapchat's free desktop application for creating sophisticated AR Lenses.

**Capabilities**:
- Full control over 3D assets, animations, and interactions
- Advanced scripting with JavaScript
- Custom shaders and visual effects
- Physics simulations
- Machine learning integration

**Workflow**:
1. **Download Lens Studio**: Free from Snap's website (Mac and Windows)
2. **Choose Template**: Start with pre-built template or blank project
3. **Import Assets**: Add 3D models, images, audio, animations
4. **Configure Tracking**: Set up face, world, body, or marker tracking
5. **Add Interactivity**: Script behaviors, triggers, and user interactions
6. **Test**: Use Lens Studio's preview or test on device via Snapchat
7. **Optimize**: Reduce file size, improve performance
8. **Export**: Export Lens package to Snapchat Business Organization

**Best For**:
- Complex, custom AR experiences
- Brands with in-house AR developers or agencies
- Unique, differentiated Lens concepts
- High-budget campaigns requiring custom development

**Learning Resources**:
- Lens Studio documentation and tutorials
- Snap's Creator Community
- YouTube tutorials and courses

#### Option 2: Lens Web Builder (Simple)

**Lens Web Builder** is a browser-based tool for creating AR Lenses and Filters quickly without coding.

**Capabilities**:
- Pre-built templates (face filters, location overlays, countdown timers, quizzes)
- Drag-and-drop interface
- Upload existing assets (images, logos, text)
- Basic customization (colors, text, positioning)
- Quick creation (under 10 minutes)

**Templates Available**:
- **AR Face Filters**: Apply makeup, accessories, or effects to faces
- **Location-Based Overlays**: Add branded graphics with location context
- **Countdown Timers**: Create urgency for events or launches
- **Quiz Generators**: Interactive quizzes with branded questions
- **Product Try-On**: Simple virtual try-on experiences

**Workflow**:
1. **Access Lens Web Builder**: Through Snapchat Ads Manager
2. **Select Template**: Choose template matching campaign goal
3. **Upload Assets**: Add logos, images, text, colors
4. **Customize**: Adjust positioning, sizing, colors
5. **Preview**: Test Lens in browser preview
6. **Export**: Save to Lens folder in Business Organization

**Best For**:
- Quick, simple AR experiences
- Budget-conscious campaigns
- Event-based or time-sensitive promotions
- Brands without AR development resources

### AR Lens Campaign Setup

#### Step 1: Create AR Lens

Create Lens using Lens Studio or Lens Web Builder, then export to your Snapchat Business Organization's Lens folder.

#### Step 2: Build Campaign in Ads Manager

**Campaign Level**:
- **Objective**: Typically "Awareness & Engagement" (optimized for Lens uses)
- **Campaign Name**: Follow naming convention (e.g., "Brand_ARLens_TryOn_Q1-2026")

**Ad Squad Level**:
- **Placement**: Select "Camera" for AR Lenses (pre-capture carousel)
- **Targeting**: Demographics, interests, location (same as other ad types)
- **Optimization Goal**: 
  - **Uses**: Optimize for Lens uses (most common)
  - **Impressions**: Optimize for Lens impressions in carousel
  - **Swipes**: Optimize for swipe-ups (if Lens includes CTA)
  - **Conversions**: Optimize for Pixel events (if Lens drives to website)
- **Bidding**: 
  - **Auto-bid**: Let Snapchat optimize bid automatically
  - **Max bid**: Set maximum cost per result
  - **Target cost**: Maintain average cost per result
- **Budget**: 
  - Minimum: $5/day
  - Recommended: $50-100/day for meaningful reach
- **Schedule**: Set start and end dates

**Ad Level**:
- **Ad Format**: Select "AR Lens"
- **Creative**: Choose Lens from Lens folder
- **Call-to-Action**: Optional (can add swipe-up CTA to drive traffic or conversions)
- **Attachment**: Can attach Lens to Snap Ads or Commercial Ads for broader reach

#### Step 3: Publish Campaign

Review all settings, then publish. Snapchat reviews Lens for policy compliance (typically 24-48 hours).

### AR Lens Optimization Strategies

#### Engagement Optimization

**Goal**: Maximize Lens uses and sharing.

**Tactics**:
- **Simplicity**: Make Lens easy to understand and use (no complex instructions)
- **Instant Gratification**: Effect should be immediately visible and impressive
- **Shareability**: Create effects users want to share with friends
- **Variety**: Offer multiple options (e.g., 5 lipstick shades, not just 1)
- **Interactivity**: Include tap-to-change, facial expression triggers, or voice activation
- **Humor**: Funny or playful effects drive higher engagement

**Example**: A beauty brand's Lens with 5 lipstick shades (tap to change) sees 3X more uses than a Lens with only 1 shade.

#### Conversion Optimization

**Goal**: Drive website visits, purchases, or app installs from Lens users.

**Tactics**:
- **Integrated CTA**: Include swipe-up CTA within Lens experience
- **Product Showcase**: Feature actual products users can purchase
- **Exclusive Offers**: Provide discount code or exclusive access via Lens
- **Retargeting**: Create custom audience of Lens users, retarget with conversion ads
- **Pixel Tracking**: Track conversions from Lens users with Snap Pixel

**Example**: A furniture brand's Lens allows users to place virtual sofa in their home, then swipe up to purchase with 15% discount code.

#### Brand Awareness Optimization

**Goal**: Maximize impressions and brand recall.

**Tactics**:
- **Prominent Branding**: Include logo and brand colors (but not overwhelming)
- **Brand Association**: Create effects that align with brand identity
- **Broad Targeting**: Reach large audience with demographics + interests
- **Frequency**: Allow users to see Lens multiple times (higher frequency cap)
- **Organic Amplification**: Encourage sharing to extend reach beyond paid impressions

**Example**: A beverage brand creates a Lens with branded 3D mascot that dances when users smile, driving high engagement and brand recall.

### AR Lens Performance Metrics

#### Key Metrics to Track

| Metric | Definition | Benchmark |
|--------|------------|----------|
| **Impressions** | Times Lens appeared in carousel | Varies by budget |
| **Uses** | Times users activated Lens | 5-15% of impressions |
| **Average Play Time** | Average duration users engaged with Lens | 15-30 seconds |
| **Shares** | Times users shared Lens content | 10-20% of uses |
| **Swipe-Ups** | Times users swiped up on CTA (if included) | 2-5% of uses |
| **Conversions** | Pixel events from Lens users (if tracked) | Varies by objective |
| **Cost Per Use** | Total spend / total uses | $0.10-0.50 |
| **Cost Per Share** | Total spend / total shares | $0.50-2.00 |

#### Analyzing Performance

**High Impressions, Low Uses**:
- **Issue**: Lens not appealing or unclear in carousel
- **Solution**: Improve thumbnail/preview, simplify concept, test different Lens

**High Uses, Low Play Time**:
- **Issue**: Lens not engaging after initial activation
- **Solution**: Add interactivity, variety, or surprise elements

**High Uses, Low Shares**:
- **Issue**: Effect not shareable or impressive enough
- **Solution**: Make effect more visually striking, funny, or unique

**High Uses, Low Conversions**:
- **Issue**: Weak connection between Lens and conversion goal
- **Solution**: Integrate CTA more naturally, offer incentive, improve landing page

## AR Filters: Deep Dive

### Types of AR Filters

#### Static Filters

**Description**: Non-animated graphic overlays applied after capturing content.

**Specifications**:
- **Resolution**: 945 x 2048 pixels
- **Format**: PNG (with transparency)
- **File Size**: Under 300 KB

**Use Cases**:
- Event branding (conferences, festivals, weddings)
- Location-based promotions (city, venue, store)
- Announcements (product launches, sales, news)
- Seasonal campaigns (holidays, seasons)

**Example**: A music festival creates a Filter with festival logo, dates, and decorative graphics for attendees to use.

#### Animated Filters

**Description**: Animated graphic overlays with motion.

**Specifications**:
- **Resolution**: 720 x 1560 pixels
- **Format**: GIF
- **Duration**: 1-3 seconds (looping)
- **Frame Rate**: 2-15 FPS
- **File Size**: Optimize for quick loading

**Use Cases**:
- Dynamic branding (animated logos, moving elements)
- Countdown timers (for events or launches)
- Interactive elements (tap-to-animate)

**Example**: A brand creates an animated Filter with logo that pulses and sparkles.

### Sponsored AR Filters

**Sponsored AR Filters** are paid placements that appear in the post-capture Filter carousel, reaching users after they've taken a photo or video.

#### Benefits of Sponsored AR Filters

- **Low Barrier to Entry**: Can be created in under 10 minutes with Lens Web Builder
- **Cost-Effective**: Lower production and media costs than AR Lenses
- **Broad Reach**: Appear in Filter carousel for targeted audience
- **Brand Integration**: Users apply branded Filter to their content
- **Organic Amplification**: Users share branded content with friends
- **Mid-Funnel Signals**: Can include CTA to capture conversion intent

#### Creating Sponsored AR Filters

**Using Lens Web Builder**:
1. Access Lens Web Builder in Ads Manager
2. Select "AR Filter" template
3. Upload brand assets (logo, graphics, text)
4. Customize positioning, colors, sizing
5. Preview Filter
6. Export to Lens folder

**Design Best Practices**:
- **Subtle Branding**: Logo should be visible but not overwhelming
- **Complementary Design**: Filter should enhance user's content, not obscure it
- **Clear Text**: If including text, ensure it's readable at small sizes
- **Safe Zones**: Keep important elements away from top/bottom 150px
- **Transparency**: Use transparent backgrounds to blend with user content

#### Sponsored AR Filter Campaign Setup

**Campaign Level**:
- **Objective**: "Awareness & Engagement"

**Ad Squad Level**:
- **Placement**: Select "AR Filter" (post-capture carousel)
- **Targeting**: Demographics, location, interests
- **Optimization Goal**: Impressions or Uses
- **Bidding**: Auto-bid or Max bid
- **Budget**: Minimum $5/day, recommended $20-50/day

**Ad Level**:
- **Ad Format**: "AR Filter"
- **Creative**: Select Filter from Lens folder
- **CTA**: Optional swipe-up CTA

### AR Filter Use Cases

#### Event Marketing

**Scenario**: A conference wants to increase social media visibility and attendee engagement.

**Strategy**:
- Create Sponsored AR Filter with conference logo, hashtag, and dates
- Target users within geo-fence of conference venue
- Run campaign during conference dates
- Encourage attendees to use Filter when sharing conference content

**Results**: Attendees apply branded Filter to their Snaps, amplifying conference visibility to their networks.

#### Product Launch

**Scenario**: A tech company is launching a new smartphone.

**Strategy**:
- Create Sponsored AR Filter with product image, launch date, and "Pre-Order Now" CTA
- Target tech enthusiasts and early adopters nationally
- Run campaign 2 weeks before launch
- Include swipe-up CTA to pre-order page

**Results**: Generates awareness and pre-orders while users share branded content.

#### Local Business Promotion

**Scenario**: A restaurant wants to drive foot traffic and social media mentions.

**Strategy**:
- Create Sponsored AR Filter with restaurant logo and "Check us out!" text
- Target users within 5-mile radius of restaurant location
- Run ongoing campaign with modest daily budget
- Encourage customers to use Filter when posting about their visit

**Results**: Customers share branded content, providing social proof and attracting new visitors.

## AR Advertising Best Practices

### Creative Best Practices

1. **Simplicity**: Make AR experience intuitive and easy to use
2. **Instant Impact**: Effect should be immediately impressive
3. **Brand Alignment**: Ensure AR experience aligns with brand identity
4. **Mobile-First**: Design for mobile viewing and interaction
5. **Performance**: Optimize for fast loading and smooth performance
6. **Variety**: Offer multiple options or variations within experience
7. **Shareability**: Create effects users want to share with friends
8. **Accessibility**: Ensure experience works for diverse users and environments

### Targeting Best Practices

1. **Audience Fit**: Target users likely to engage with AR (younger demographics, tech-savvy)
2. **Interest Alignment**: Target interests relevant to AR experience (beauty for makeup try-on, fashion for clothing)
3. **Location Relevance**: Use geo-targeting for location-specific experiences
4. **Retargeting**: Retarget AR users with conversion-focused ads

### Budget and Bidding Best Practices

1. **Sufficient Budget**: Allocate enough budget for meaningful reach ($50-100/day minimum for Lenses)
2. **Auto-Bid for Testing**: Start with auto-bid to gather performance data
3. **Optimize Over Time**: Adjust bids based on performance (cost per use, cost per share)
4. **Seasonal Allocation**: Increase budget during peak times (holidays, events)

### Measurement Best Practices

1. **Track Full Funnel**: Measure awareness (impressions), engagement (uses, play time), and conversions (swipe-ups, Pixel events)
2. **Benchmark Performance**: Compare to industry benchmarks and past campaigns
3. **Audience Insights**: Analyze which demographics engage most with AR
4. **Iterative Optimization**: Continuously test and refine based on data

## Conclusion

AR Lenses and Filters offer powerful opportunities for brands to create immersive, engaging, and shareable advertising experiences on Snapchat. Success requires:

1. **Choosing the right format**: Lenses for complex, interactive experiences; Filters for simple, branded overlays
2. **Creating compelling experiences**: Simple, instantly impressive, and shareable
3. **Strategic targeting**: Reaching users likely to engage with AR
4. **Proper measurement**: Tracking engagement and conversion metrics
5. **Continuous optimization**: Testing and refining based on performance data

By leveraging Snapchat's AR capabilities and following these best practices, brands can drive engagement, awareness, and conversions through innovative augmented reality advertising.