---
name: snapchat-ads-ar-creative
description: "Create Snapchat AR Lenses, Filters, and interactive ad creatives using Lens Studio and Lens Web Builder. Use for developing AR experiences, designing sponsored Lenses and Filters, implementing face tracking and world effects, creating interactive brand experiences, optimizing AR creative for engagement, and understanding AR ad specifications and best practices."
---

# Snapchat Ads AR Creative

Create interactive AR Lenses and Filters for Snapchat advertising using Lens Studio and Lens Web Builder.

## Overview

Snapchat's AR advertising formats enable brands to create interactive, camera-based experiences. This skill covers AR Lens and Filter creation, technical specifications, and optimization strategies.

## AR Format Types

### AR Lenses
- **Placement**: Pre-capture carousel (before photo/video)
- **Interaction**: Users apply before capturing content
- **Billing**: Per impression (swipe on/over Lens)
- **Best For**: Interactive brand experiences, product try-ons

### AR Filters
- **Placement**: Post-capture carousel (after photo/video)
- **Interaction**: Users apply after capturing content
- **Billing**: Per impression (swipe on/over Filter)
- **Best For**: Branded overlays, user-generated content

## Lens Studio Basics

### Installation
1. Download Lens Studio from lensstudio.snapchat.com
2. Install on Mac or Windows
3. Sign in with Snapchat account
4. Access templates and resources

### Interface Components
- **Preview Panel**: Real-time Lens preview
- **Objects Panel**: Scene hierarchy
- **Resources Panel**: Assets (images, 3D models, audio)
- **Inspector Panel**: Object properties
- **Scene Panel**: Visual scene editor

## Creating Face Lenses

### Face Tracking Setup
```javascript
// Face Mesh Tracking
var faceTracking = script.getSceneObject().getComponent("Component.FaceTracking");
var faceMesh = script.getSceneObject().getComponent("Component.RenderMeshVisual");

// Apply texture to face
faceMesh.mainPass.baseTex = texture;
```

### Common Face Effects
- **Face Paint**: Makeup, face decorations
- **Face Distortion**: Morphing, exaggeration
- **Face Accessories**: Glasses, hats, jewelry
- **Face Replacement**: Character faces, masks

### Best Practices
- Keep polygon count under 10,000
- Optimize textures (2048 x 2048 max)
- Test on multiple face shapes
- Ensure smooth tracking

## Creating World Lenses

### World Tracking Setup
```javascript
// Ground Plane Tracking
var deviceTracking = script.getSceneObject().getComponent("Component.DeviceTracking");
deviceTracking.requestDeviceTrackingMode(DeviceTrackingMode.World);

// Place 3D object in world
var worldObject = scene.createSceneObject("WorldObject");
worldObject.getTransform().setWorldPosition(new vec3(0, 0, -100));
```

### Common World Effects
- **Object Placement**: Furniture, products in environment
- **Portals**: Immersive 3D environments
- **Games**: Interactive AR games
- **Markers**: Image/location-based triggers

## Creating AR Filters

### Static Filter Specs
- **Dimensions**: 945 x 2048 pixels
- **Format**: PNG with transparency
- **File Size**: Under 300 KB
- **Design**: Max 25% screen coverage, center clear

### Animated Filter Specs
- **Dimensions**: 720 x 1560 pixels
- **Format**: GIF
- **Duration**: 1-3 seconds looping
- **File Size**: Under 300 KB

### Design Guidelines
- Place logos/text in top or bottom quarters
- Leave center clear for selfies
- Use high contrast for visibility
- Test on various backgrounds

## Adding Interactivity

### Tap Interactions
```javascript
// Tap to change state
var tapEvent = script.createEvent("TapEvent");
tapEvent.bind(function() {
    material.mainPass.baseColor = new vec4(1, 0, 0, 1);
});
```

### Face Expressions
```javascript
// Trigger on smile
var faceTracking = script.getSceneObject().getComponent("Component.FaceTracking");
if (faceTracking.getFeature("Smile").value > 0.5) {
    // Activate effect
}
```

### Voice Commands
```javascript
// Voice-activated effects
var voiceML = script.getSceneObject().getComponent("Component.VoiceML");
voiceML.onVoiceCommand.add(function(command) {
    if (command === "activate") {
        // Trigger effect
    }
});
```

## Audio Integration

### Adding Sound Effects
- **Format**: MP3 or WAV
- **File Size**: Under 1 MB per clip
- **Duration**: Keep short (1-5 seconds)
- **Trigger**: Tap, face expression, or automatic

```javascript
// Play audio on tap
var audioComponent = script.getSceneObject().getComponent("Component.AudioComponent");
var tapEvent = script.createEvent("TapEvent");
tapEvent.bind(function() {
    audioComponent.play(1); // Play once
});
```

## Branding Requirements

### Logo Placement
- **Position**: Top left or top right corner
- **Size**: Visible but not dominant
- **Placement**: Under UI elements to avoid obstruction
- **Required**: For Face and World Lenses

### Sponsored Tag
- Snapchat automatically adds "SPONSORED" tag
- Appears for first 2 seconds
- Cannot be removed or customized

## Technical Specifications

### Lens Package
- **Format**: .lns file (Lens Studio native)
- **Max Size**: 8 MB compressed
- **Texture Resolution**: 2048 x 2048 max per texture
- **Polygon Count**: Under 10,000 recommended
- **Audio**: MP3/WAV, under 1 MB per clip

### Performance Optimization
- Reduce polygon count
- Compress textures
- Limit particle effects
- Optimize scripts
- Test on low-end devices

## Publishing and Campaign Setup

### Export Lens
1. File > Export Lens
2. Choose export location
3. Lens package (.lns) created
4. Upload to Snapchat Business Organization

### Create Lens Campaign
1. Navigate to Ads Manager
2. Create Campaign (type: LENS)
3. Create Ad Squad (type: LENS)
4. Select Lens from organization folder
5. Set targeting and budget
6. Launch campaign

## Measurement and Optimization

### Key Metrics
- **Impressions**: Swipes on/over Lens
- **Uses**: Lens activations
- **Shares**: Lens shared to Story or friends
- **Play Time**: Average engagement duration
- **Unique Users**: Reach

### Optimization Tips
- Test multiple Lens variations
- Refresh Lenses every 2-4 weeks
- Analyze use patterns (time of day, demographics)
- Optimize for shares (encourage UGC)
- Monitor performance and iterate

## Using the Reference Files

**`/references/lens-studio-advanced.md`** — Read when implementing complex AR effects or custom scripts.

**`/references/ar-creative-examples.md`** — Read when seeking inspiration or understanding successful AR campaigns.

**`/references/ar-performance-optimization.md`** — Read when optimizing Lens performance or troubleshooting issues.
