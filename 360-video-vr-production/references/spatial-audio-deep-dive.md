# Spatial Audio Deep Dive

Comprehensive guide to capturing, processing, and delivering immersive audio for 360° and VR content.

---

## Spatial Audio Fundamentals

### What is Spatial Audio?
Audio that responds to head movement, creating the illusion of sound coming from specific locations in 3D space.

### Audio Format Comparison
| Format | Channels | Head Tracking | Best Use |
|--------|----------|---------------|----------|
| Stereo | 2 | No | Background music |
| Binaural | 2 | Rendered | 360 video playback |
| Ambisonics 1st | 4 (W,X,Y,Z) | Yes | Standard VR |
| Ambisonics 2nd | 9 | Yes | Better localization |
| Ambisonics 3rd | 16 | Yes | Premium VR |
| Object-based | Variable | Yes | Interactive VR |

---

## Recording Equipment

### Ambisonic Microphones

#### Zoom H3-VR
- **Format**: Ambisonics A → B format
- **Price**: ~$350
- **Quality**: Good for prosumer
- **Best For**: Budget VR production

#### Rode NT-SF1
- **Format**: Ambisonics A-format
- **Price**: ~$750
- **Quality**: Professional
- **Best For**: Broadcast, film

#### Sennheiser Ambeo VR
- **Format**: Ambisonics A-format
- **Price**: ~$1,300
- **Quality**: High-end
- **Best For**: Professional production

#### Zylia ZM-1
- **Format**: 3rd order ambisonics
- **Price**: ~$600
- **Quality**: High resolution
- **Best For**: Music, immersive audio

### Microphone Placement
- Position at camera height
- Mount on camera rig if possible
- Avoid wind/handling noise
- Monitor during recording

---

## Ambisonics Explained

### A-Format vs B-Format
- **A-Format**: Raw microphone capsule signals
- **B-Format**: Decoded spatial audio (W, X, Y, Z)
- Always convert A → B for processing

### Channel Layout (B-Format)
| Channel | Name | Description |
|---------|------|-------------|
| W | Omni | Overall pressure |
| X | Front-Back | Figure-8 front/back |
| Y | Left-Right | Figure-8 left/right |
| Z | Up-Down | Figure-8 up/down |

### Higher Order Ambisonics (HOA)
- More channels = better spatial resolution
- 2nd order: 9 channels
- 3rd order: 16 channels
- Trade-off: file size vs. quality

---

## Recording Workflow

### Pre-Production
1. Scout location for acoustic challenges
2. Test microphone in environment
3. Plan sync method (timecode, slate)
4. Check wind conditions

### During Recording
1. Slate for sync reference
2. Record at 48kHz/24-bit minimum
3. Monitor all channels
4. Log environmental sounds

### File Management
- Name files consistently
- Note A-format vs B-format
- Include metadata (location, take)
- Backup immediately

---

## Post-Production Workflow

### DAW Setup for Ambisonics

#### Reaper (Recommended)
1. Install ambisonic plugins (IEM, ATK)
2. Set project to multi-channel
3. Configure ambisonics bus
4. Route B-format to encoder

#### Pro Tools
1. Requires ambisonics plugins
2. Use aux tracks for B-format
3. Spatial audio tools: FB360 Workstation

#### Logic Pro
- Limited native support
- Use third-party plugins
- Export to external tools

### Essential Plugins
| Plugin | Purpose | Price |
|--------|---------|-------|
| IEM Plugin Suite | Full ambisonics toolkit | Free |
| FB360 Spatial Workstation | Meta standard | Free |
| dearVR Pro | VR mixing | $249 |
| Audioease 360pan | Panning, encoding | $295 |
| Noise Makers Ambi | Bundle | $199 |

---

## Encoding and Decoding

### A-Format to B-Format
```
Most plugins handle automatically:
- Load A-format recording
- Apply microphone-specific A→B conversion
- Output B-format for processing
```

### B-Format to Binaural
For headphone playback without head tracking:
1. Apply binaural decoder
2. HRTF (Head-Related Transfer Function) applied
3. Output stereo file
4. Works on any headphones

### Platform-Specific Encoding

#### YouTube 360
- Format: 1st order ambisonics
- Channels: 4 (ACN/SN3D)
- Tool: Spatial Media Metadata Injector

#### Meta Quest
- Format: Ambisonics or TBE
- Use FB360 Encoder
- Embed in video container

#### Apple Vision Pro
- Format: Object-based or ambisonics
- Encode using Spatial Audio tools
- HEVC container

---

## Spatial Audio for Video Sync

### Synchronization Methods
1. **Timecode**: Most accurate, requires gear
2. **Slate/clap**: Visual + audio sync point
3. **Waveform matching**: Software alignment
4. **Scratch track**: Guide audio from camera

### Sync Workflow
```
1. Import video (reference audio) and ambisonics
2. Align using sync point or waveform
3. Verify sync at multiple points
4. Lock tracks before mixing
```

### Drift Prevention
- Use same sample rate throughout
- Avoid resampling
- Check for dropped frames
- Monitor sync during long recordings

---

## Mixing for 360/VR

### Sound Design Approach
1. **Bed**: Ambient soundscape (ambisonics)
2. **Objects**: Positioned sounds (point sources)
3. **Music**: Typically stereo or non-diegetic

### Spatialization Techniques
| Technique | Implementation | Use Case |
|-----------|----------------|----------|
| Static positioning | Fixed location in sphere | Environmental sounds |
| Head-locked | Follows viewer | UI sounds, narration |
| Object tracking | Follows video element | Character dialogue |
| Distance modeling | Volume + reverb changes | Depth perception |

### Mixing Best Practices
- Monitor on headphones AND speakers
- Check binaural rendering quality
- Test on target platform
- Consider comfort zone (avoid sounds behind)

---

## Troubleshooting

### Common Issues

#### Audio Rotation Mismatch
**Problem**: Audio doesn't align with video direction
**Solution**: Rotate ambisonics field to match camera front

#### Phase Issues
**Problem**: Hollow or thin sound
**Solution**: Check A→B conversion, verify plugin order

#### Head Tracking Not Working
**Problem**: Audio doesn't respond to head movement
**Solution**: Verify platform metadata, check decoder settings

#### Localization Problems
**Problem**: Can't pinpoint sound sources
**Solution**: Use higher order ambisonics, check HRTF quality

### Quality Checklist
- [ ] Audio synced to video
- [ ] Rotation matches camera orientation
- [ ] Head tracking functional
- [ ] No phase issues
- [ ] Comfortable listening level
- [ ] Tested on target platform/device

---

## Delivery Specifications

### File Format by Platform
| Platform | Audio Format | Sample Rate | Bit Depth |
|----------|--------------|-------------|-----------|
| YouTube | AAC, 4 ch ambisonic | 48kHz | 16-bit |
| Meta Quest | AAC/Opus | 48kHz | 16-bit |
| Vimeo | AAC | 48kHz | 16-bit |
| Custom Web | Opus preferred | 48kHz | Variable |

### Metadata Requirements
- Spatial audio flag in container
- Ambisonic format specification (ACN/SN3D)
- Head tracking enable flag
- Projection type correlation
