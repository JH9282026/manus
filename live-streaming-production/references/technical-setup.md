# Technical Setup for Live Streaming

## Equipment Tiers

### Basic Setup (Solo Streamer)
- Webcam (Logitech C920/C922 or equivalent)
- USB microphone (Blue Yeti, Samson Q2U, or Audio-Technica AT2020)
- Ring light or desk lamp with diffusion
- Stable internet connection (10+ Mbps upload)
- OBS Studio (free) or Streamlabs

### Intermediate Setup (Interviews/Panels)
- Mirrorless camera with HDMI output (Sony a6400, Canon M50)
- Capture card (Elgato HD60 S+, Elgato Cam Link 4K)
- XLR microphone with audio interface (Focusrite Scarlett)
- Key light + fill light (Elgato Key Light, Aputure)
- Green screen (optional)
- Dedicated streaming PC or Mac

### Professional Setup (Events/Multi-Camera)
- Multiple cameras with SDI/HDMI outputs
- Video switcher (Blackmagic ATEM Mini Pro, Roland VR-4HD)
- Wireless microphone systems
- Professional lighting kit
- Hardware encoder or dedicated streaming server
- Wired ethernet connections (for all systems)
- Intercom system for crew communication
- Program and preview monitors

---

## Software Configuration

### OBS Studio Settings

**Video Settings**:
- Base resolution: Match your monitor
- Output resolution: 1920x1080 (standard) or 1280x720 (constrained)
- Downscale filter: Lanczos (best quality)
- FPS: 30 (standard) or 60 (gaming/fast motion)

**Output Settings (Advanced)**:
- Encoder: x264 (CPU) or NVENC (NVIDIA GPU)
- Rate control: CBR (constant bitrate)
- Bitrate: 4500-6000 kbps for 1080p30
- Keyframe interval: 2 seconds
- CPU preset: veryfast (x264) — balance quality/performance
- Audio: AAC, 160 kbps, 48kHz sample rate

### Scene Organization
1. **Starting Soon** — Pre-stream graphic with countdown
2. **Main Camera** — Primary talking head/content view
3. **Screen Share** — Desktop or application capture
4. **Split Screen** — Multi-person layouts
5. **BRB** — Break screen with music
6. **Ending** — Closing graphic with call to action

---

## Audio Configuration

### Microphone Levels
- Peak levels: -12 dB to -6 dB
- Average levels: -18 dB to -12 dB
- Noise gate threshold: -40 dB to -32 dB
- Apply noise suppression filter (RNNoise in OBS)

### Audio Processing Chain
1. Noise suppression (remove background noise)
2. Noise gate (cut audio when not speaking)
3. Compressor (even out volume levels)
4. Limiter (prevent clipping)

---

## Network Requirements

| Stream Quality | Minimum Upload | Recommended Upload |
|---------------|---------------|-------------------|
| 720p 30fps | 5 Mbps | 8 Mbps |
| 1080p 30fps | 8 Mbps | 12 Mbps |
| 1080p 60fps | 10 Mbps | 15 Mbps |
| 4K 30fps | 20 Mbps | 35 Mbps |

### Network Best Practices
- Use wired ethernet (not WiFi)
- Disable automatic updates during streams
- Close unnecessary applications
- Use QoS settings on router to prioritize streaming
- Have mobile hotspot as backup
