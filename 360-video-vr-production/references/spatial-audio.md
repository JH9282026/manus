# Spatial Audio for 360° Video

Capturing and mixing audio that matches the immersive visual experience.

---

## Why Spatial Audio Matters

In 360° video, audio must match visual reality. Sounds should come from where viewers expect based on visual cues. Spatial audio:

- Increases immersion significantly
- Provides directional cues that guide attention
- Creates more realistic, believable experience
- Enhances sense of presence

---

## Types of Spatial Audio

### Stereo

**Description**: Traditional left/right audio.

**Characteristics**:
- Doesn't respond to head movement
- Minimum acceptable option
- Easy to produce
- Familiar workflow

**Limitation**: Breaks immersion—sound stays fixed while visual rotates.

### Ambisonic

**Description**: Full 360° sound field capture.

**Characteristics**:
- Responds to head rotation
- True spatial audio
- Requires special microphones
- Platform support varies

**How It Works**: Captures sound from all directions using multiple capsules. Decoded for playback, rotating sound field with viewer's head movement.

### Object-Based Audio

**Description**: Individual sound sources positioned in 3D space.

**Characteristics**:
- Most flexibility in mixing
- Can adjust individual elements
- Requires complex production
- Best quality results

**How It Works**: Each sound element has positional metadata. Rendered in real-time based on viewer orientation.

---

## Ambisonic Microphones

### Recommended Equipment

| Microphone | Price Range | Characteristics |
|------------|-------------|----------------|
| Zoom H3-VR | $350-400 | Affordable, all-in-one recorder, good quality |
| Sennheiser AMBEO VR Mic | $1,500+ | Professional quality, requires separate recorder |
| Rode NT-SF1 | $750-900 | High quality, compact, good value |
| Core Sound TetraMic | $900-1,200 | Compact, studio quality |

### Microphone Selection

**For Most Productions**: Zoom H3-VR
- Built-in recorder
- Reasonable quality
- Affordable
- Easy workflow

**For Professional Productions**: Sennheiser AMBEO or Rode NT-SF1
- Superior quality
- Requires external recorder
- Better low-frequency response
- Higher dynamic range

---

## Recording Spatial Audio

### Microphone Positioning

**Golden Rule**: Position microphone at camera location.

**Rationale**: Viewer's ears should be where their eyes are. Sound perspective must match visual perspective.

**Mounting Options**:
- Attach to camera rig
- Separate stand at exact camera position
- Above or below camera (if camera must be in exact position)

### Recording Best Practices

1. **Match visual and audio perspectives** — mic where camera is
2. **Record room tone** — 30-60 seconds of quiet ambience
3. **Capture wild sound** — environmental audio for post flexibility
4. **Monitor levels remotely** — avoid handling noise
5. **Use windscreens** — outdoor recording essential
6. **Backup recording** — separate recorder if possible

### Technical Settings

| Setting | Recommendation |
|---------|---------------|
| Sample rate | 48kHz minimum, 96kHz preferred |
| Bit depth | 24-bit |
| Format | A-format (raw) for flexibility, B-format for direct use |
| Gain | Conservative—avoid clipping |

---

## Ambisonic Formats

### A-Format vs. B-Format

**A-Format (Raw)**:
- Direct from microphone capsules
- 4 channels matching physical capsules
- Requires conversion to B-format
- Most flexibility in post

**B-Format (Standard)**:
- Converted from A-format
- 4 channels: W (omni), X (front-back), Y (left-right), Z (up-down)
- Standard interchange format
- Ready for decoding

### Channel Order (AmbiX vs. FuMa)

**AmbiX (Modern Standard)**:
- Channel order: W, Y, Z, X
- Normalized coefficients
- YouTube, Facebook, most modern platforms

**FuMa (Legacy)**:
- Channel order: W, X, Y, Z
- Different normalization
- Some older software

**Important**: Match format to platform requirements.

---

## Post-Production Audio Workflow

### 1. Import and Decode

1. Import first-order ambisonic files (4 channels)
2. Decode to proper format for platform
3. Verify channel order (AmbiX vs. FuMa)
4. Check sync with video

### 2. Editing and Mixing

**Software Options**:

| Software | Cost | Strengths |
|----------|------|----------|
| Facebook 360 Spatial Workstation | Free | Comprehensive, well-supported |
| Reaper + ambisonic plugins | Affordable | Flexible, powerful |
| Pro Tools + spatial plugins | Professional | Industry standard DAW |
| DaVinci Resolve Fairlight | Included | Integrated with video editing |

### 3. Adding Sound Design

**Spatial Positioning**:
- Place sounds in 3D space
- Match visual location (if sound has on-screen source)
- Consider head-locked vs. world-locked sounds

**Head-Locked Sounds**:
- Stay fixed relative to viewer (narration, music)
- Don't move when viewer rotates
- Use for non-diegetic elements

**World-Locked Sounds**:
- Fixed position in scene
- Rotate as viewer moves head
- Use for all on-screen sources

### 4. Mixing Considerations

**Balance**:
- Spatial ambience (captured ambisonic)
- Dialogue (often separate recording)
- Sound effects (positioned in space)
- Music (typically head-locked or subtle spatial)

**Attention Guidance**:
- Use spatial cues to guide viewer attention
- Sound from direction makes viewer look there
- Powerful storytelling tool

---

## Platform-Specific Requirements

### YouTube

**Format**: First-order ambisonics, AmbiX channel order
**Channels**: 4 audio channels embedded in video
**Encoding**: AAC, 128kbps or higher per channel
**Metadata**: Spatial audio flag required

### Facebook/Meta

**Format**: First-order ambisonics, AmbiX
**Channels**: 4 channels
**Tools**: Facebook 360 Spatial Workstation for encoding

### Custom Apps/Quest

**Varies by implementation**
- Check specific platform requirements
- May support higher-order ambisonics
- Object-based audio possible

---

## Troubleshooting

### Audio Doesn't Rotate with Head Movement

**Causes**:
- Missing spatial audio metadata
- Wrong channel order
- Platform doesn't support spatial audio

**Solutions**:
- Verify metadata injection
- Check AmbiX vs. FuMa
- Test on known-working platform

### Sound Position Doesn't Match Video

**Causes**:
- Microphone positioned differently than camera
- Rotation offset in post
- Channel order reversed

**Solutions**:
- Verify recording setup
- Apply rotation correction in mixing
- Check channel mapping

### Audio Quality Issues

**Causes**:
- Low sample rate or bit depth
- Compression artifacts
- Wind or handling noise

**Solutions**:
- Record at higher quality settings
- Less aggressive compression on export
- Proper windscreens, careful handling

---

## Facebook 360 Spatial Workstation Workflow

### Setup

1. Download and install (free)
2. Import video file
3. Import ambisonic audio (or extract from video)

### Basic Workflow

1. **Import media** — video and ambisonic audio files
2. **Verify sync** — adjust if needed
3. **Position additional elements** — sound design, dialogue
4. **Monitor in VR** — use headset for accurate preview
5. **Encode output** — export with proper metadata

### Key Features

- Visual positioning of sound sources
- Head-locked vs. world-locked controls
- Ambisonic encoding/decoding
- Platform-specific export presets
- VR preview support
