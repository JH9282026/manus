---
name: video-technical-standards
description: Understanding video technical standards is essential for anyone working with video content. These standards govern how video is captured, stored, processed, and delivered across different platforms and devices.
---

# Video Technical Standards (Formats, Codecs, Compression)

## Introduction to Video Technical Standards

Understanding video technical standards is essential for anyone working with video content. These standards govern how video is captured, stored, processed, and delivered across different platforms and devices. Mastery of these technical concepts ensures your video content plays correctly, looks its best, and meets delivery requirements for any platform.

Video technology encompasses multiple interconnected elements: resolution, frame rate, codec, container format, bitrate, color space, and more. Each element affects the others, and optimizing video requires understanding how they interact.

This guide covers the fundamental technical concepts that video professionals must understand, from basic resolution and frame rate to advanced topics like codec selection and platform-specific delivery requirements.

---

## Video Resolution and Aspect Ratios

### Understanding Resolution

Resolution refers to the number of pixels in a video frame, typically expressed as width × height.

**Common Resolutions:**

| Name | Dimensions | Pixels | Common Use |
|------|-----------|--------|------------|
| SD (Standard Definition) | 720 × 480 (NTSC) / 720 × 576 (PAL) | ~350K | Legacy content, DVD |
| HD (720p) | 1280 × 720 | ~0.9M | Web video, broadcast |
| Full HD (1080p) | 1920 × 1080 | ~2M | Standard professional video |
| 2K | 2048 × 1080 | ~2.2M | Digital cinema |
| QHD (1440p) | 2560 × 1440 | ~3.7M | High-end monitors, gaming |
| 4K UHD | 3840 × 2160 | ~8.3M | Premium content, streaming |
| 4K DCI | 4096 × 2160 | ~8.8M | Digital cinema |
| 8K UHD | 7680 × 4320 | ~33M | Future-proof, specialty |

**Resolution Considerations:**
- Higher resolution = more detail but larger files
- Capture at highest practical resolution
- Deliver at appropriate resolution for platform/use
- Downscaling often looks better than upscaling

### Aspect Ratios

Aspect ratio is the proportional relationship between width and height.

**Common Aspect Ratios:**

| Ratio | Decimal | Common Use |
|-------|---------|------------|
| 16:9 | 1.78 | HD/UHD television, YouTube |
| 4:3 | 1.33 | Legacy TV, some presentations |
| 1:1 | 1.0 | Instagram posts, social media |
| 9:16 | 0.56 | TikTok, Instagram Reels, Stories |
| 4:5 | 0.8 | Instagram portrait |
| 21:9 (2.35:1) | 2.35 | Cinematic widescreen |
| 2.39:1 | 2.39 | Anamorphic widescreen |
| 1.85:1 | 1.85 | Theatrical flat widescreen |

**Platform-Specific Aspect Ratios:**

**YouTube:**
- Standard: 16:9
- Shorts: 9:16
- Supports: Various (letterboxed/pillarboxed if different)

**Instagram:**
- Feed: 1:1 (square), 4:5 (portrait), 1.91:1 (landscape)
- Stories/Reels: 9:16
- IGTV: 9:16

**TikTok:**
- Standard: 9:16
- Alternative: 1:1

**Facebook:**
- Feed: 16:9, 1:1, 4:5
- Stories: 9:16

**Handling Aspect Ratio Mismatches:**
- Letterboxing: Black bars top and bottom
- Pillarboxing: Black bars on sides
- Cropping: Remove portions to fit
- Scaling: Stretch (generally not recommended)

---

## Frame Rates

### Understanding Frame Rates

Frame rate (fps - frames per second) determines how many individual frames are displayed per second, affecting motion smoothness and file size.

**Common Frame Rates:**

| Frame Rate | Common Use |
|------------|------------|
| 23.976fps (24p) | Film, cinema, narrative content |
| 24fps | Digital cinema, film emulation |
| 25fps | PAL broadcast (Europe, Australia, etc.) |
| 29.97fps (30p) | NTSC broadcast (North America, Japan) |
| 30fps | Web video, general purpose |
| 50fps | PAL high frame rate |
| 59.94fps (60p) | NTSC high frame rate |
| 60fps | Smooth motion, sports, gaming |
| 120fps | Slow motion, specialty |
| 240fps+ | High-speed slow motion |

### Frame Rate Selection Criteria

**24/23.976fps:**
- Cinematic, film-like motion
- Motion blur creates perceived smoothness
- Smaller file sizes
- Best for: Narrative, documentary, artistic

**30/29.97fps:**
- Slightly smoother than 24fps
- Standard for web content
- Good balance of quality and file size
- Best for: Corporate, YouTube, general purpose

**60/59.94fps:**
- Very smooth motion
- Reduces motion blur
- Larger file sizes
- Best for: Sports, gaming, fast action

**High Frame Rates (120fps+):**
- Primarily for slow-motion capture
- Played back at lower rates for smooth slow-mo
- Very large file sizes
- Best for: Action sports, music videos, creative effects

### Frame Rate Considerations

**Consistency:**
- Match frame rate throughout project
- Convert carefully if mixing sources
- Avoid creating dropped or duplicated frames

**Playback Speed Effects:**
- 60fps shot → 24fps playback = 2.5× slow motion
- 120fps shot → 24fps playback = 5× slow motion
- Calculate desired slow-motion factor when shooting

**Platform Requirements:**
- YouTube: Supports up to 60fps
- Broadcast: Typically 25fps (PAL) or 29.97fps (NTSC)
- Streaming services: Usually 24fps for films, 30fps for TV

---

## Video Codecs

### Understanding Codecs

A codec (coder-decoder) is the software that compresses and decompresses video data. Codecs determine how video is encoded into a file and decoded for playback.

**Types of Codecs:**

**Acquisition/Production Codecs:**
- Designed for editing
- Higher quality, less compression
- Faster encoding/decoding
- Examples: ProRes, DNxHD, CineForm

**Distribution/Delivery Codecs:**
- Designed for final delivery
- Higher compression, smaller files
- More processing to encode
- Examples: H.264, H.265/HEVC, VP9, AV1

### Common Codecs

**H.264 (AVC - Advanced Video Coding):**
- Most widely compatible codec
- Good balance of quality and file size
- Hardware support nearly universal
- Used for: Web, streaming, Blu-ray, broadcast
- Best for: Maximum compatibility

**H.265 (HEVC - High Efficiency Video Coding):**
- ~50% better compression than H.264 at same quality
- Higher encoding complexity (slower)
- Growing hardware support
- Licensing complexity
- Best for: 4K+ content, bandwidth-constrained delivery

**VP9:**
- Google's open, royalty-free codec
- Similar efficiency to HEVC
- Used heavily by YouTube
- Good browser support
- Best for: YouTube, web platforms

**AV1:**
- Open, royalty-free codec
- ~30% better than HEVC
- Slow to encode (hardware encoding emerging)
- Growing adoption
- Best for: Future-oriented, streaming efficiency

**ProRes (Apple):**
- High-quality acquisition/editing codec
- Various quality levels (Proxy to 4444 XQ)
- Efficient editing performance
- Best for: Professional editing, master files

**DNxHD/DNxHR (Avid):**
- Professional editing codec
- Various quality levels
- Cross-platform (unlike early ProRes)
- Best for: Professional editing, Avid workflows

**CineForm:**
- Now open standard (GoPro)
- Good editing performance
- Good quality-to-size ratio
- Best for: Editing, intermediate format

### Codec Selection Guidelines

**For Acquisition/Editing:**
- Use ProRes or DNxHD/DNxHR
- Prioritize editing performance
- Accept larger file sizes
- Maintain maximum quality

**For Delivery:**
- Use H.264 for maximum compatibility
- Use H.265/HEVC for 4K or bandwidth concerns
- Use VP9 for YouTube/web optimization
- Use AV1 for future-oriented projects

**Considerations:**
- Platform support requirements
- Hardware encoding/decoding availability
- File size constraints
- Quality requirements
- Encoding time available

---

## Container Formats

### Understanding Containers

Container formats (wrappers) are file formats that hold video, audio, and metadata. The container is separate from the codec—the same codec can be wrapped in different containers.

**Common Container Formats:**

**MP4 (.mp4, .m4v):**
- Most widely compatible container
- Supports H.264, H.265, AAC audio
- Good for: Web delivery, streaming, general use
- Industry standard for distribution

**MOV (.mov):**
- Apple QuickTime format
- Supports ProRes, H.264, H.265, many others
- Good for: Apple ecosystem, professional editing
- Highly flexible container

**MKV (.mkv):**
- Matroska, open container format
- Supports virtually any codec
- Multiple audio/subtitle tracks
- Good for: Archiving, personal use
- Limited professional/platform support

**AVI (.avi):**
- Legacy Microsoft format
- Supports many codecs
- Large files, limited features
- Generally outdated

**WebM (.webm):**
- Open format by Google
- Supports VP8, VP9, AV1
- Good for: Web video, HTML5
- Smaller ecosystem than MP4

**MXF (.mxf):**
- Professional broadcast format
- Supports many codecs
- Extensive metadata support
- Good for: Broadcast, archiving

### Container Selection

**For Web/Streaming:**
- MP4 (H.264) for compatibility
- WebM (VP9/AV1) for web optimization

**For Professional Editing:**
- MOV (ProRes) for Apple
- MXF (DNxHD/HR) for Avid
- MOV/MXF for cross-platform

**For Archiving:**
- MKV or MOV with minimal compression
- Include all tracks and metadata

---

## Bitrate and Compression

### Understanding Bitrate

Bitrate is the amount of data used per second of video, measured in bits per second (bps), kilobits (kbps), or megabits (Mbps).

**Types of Bitrate:**

**Constant Bitrate (CBR):**
- Same bitrate throughout video
- Predictable file size
- May waste bits on simple scenes
- Required for some streaming/broadcast

**Variable Bitrate (VBR):**
- Bitrate varies based on scene complexity
- More efficient use of data
- Better quality at same average bitrate
- Unpredictable exact file size

**Average Bitrate (ABR):**
- Targets average bitrate with some variation
- Balance of CBR predictability and VBR efficiency

### Recommended Bitrates

**H.264 Video Bitrates:**

| Resolution | SDR Bitrate | HDR Bitrate |
|------------|-------------|-------------|
| 720p | 5-8 Mbps | N/A |
| 1080p | 8-15 Mbps | 12-20 Mbps |
| 4K UHD | 35-50 Mbps | 50-80 Mbps |

**H.265/HEVC (approximately 40-50% less):**

| Resolution | SDR Bitrate | HDR Bitrate |
|------------|-------------|-------------|
| 720p | 3-5 Mbps | N/A |
| 1080p | 5-10 Mbps | 8-12 Mbps |
| 4K UHD | 20-30 Mbps | 30-50 Mbps |

**Audio Bitrates (AAC):**
- Stereo: 128-320 kbps
- 5.1 Surround: 384-640 kbps
- Dolby Atmos: 448-768 kbps

### Understanding Compression

**Lossy vs. Lossless:**
- Lossy: Permanently discards data (smaller files)
- Lossless: Preserves all data (larger files)
- Most delivery uses lossy compression

**Compression Artifacts:**
- Blocking: Visible square patterns
- Banding: Gradients show distinct steps
- Mosquito noise: Fuzzy edges around objects
- Motion blur: Unintended blurring

**Avoiding Compression Artifacts:**
- Use appropriate bitrate
- Avoid extreme compression
- Pre-process difficult content
- Test output quality

### Two-Pass Encoding

**What is Two-Pass:**
- First pass analyzes video content
- Second pass applies optimal compression
- Better quality at same bitrate vs. one-pass

**When to Use:**
- Final delivery masters
- Quality-critical content
- When encoding time is available

**Trade-offs:**
- Takes approximately twice as long
- Worth the time for important deliverables
- Not necessary for quick previews

---

## Color Space and Bit Depth

### Understanding Color Space

Color space defines the range of colors that can be represented.

**Common Color Spaces:**

**Rec.709:**
- Standard for HD video
- Most common color space
- Limited gamut (covers ~36% of visible colors)
- Used for: HD broadcast, web, most video

**Rec.2020:**
- Standard for UHD/4K video
- Wider gamut than Rec.709
- Required for HDR content
- Used for: 4K HDR content, future-proof mastering

**DCI-P3:**
- Digital cinema color space
- Wider than Rec.709, narrower than Rec.2020
- Used for: Cinema, high-end displays

**sRGB:**
- Web and display standard
- Similar to Rec.709 with different gamma
- Used for: Web images, computer displays

### Understanding Bit Depth

Bit depth determines how many colors/shades can be represented per channel.

**Common Bit Depths:**

**8-bit:**
- 256 levels per channel (16.7 million colors)
- Standard for delivery
- May show banding in gradients
- Sufficient for most viewing

**10-bit:**
- 1,024 levels per channel (1 billion+ colors)
- Required for HDR
- Smoother gradients
- Larger files, more processing

**12-bit:**
- 4,096 levels per channel
- Professional cinema
- Maximum flexibility in grading
- Large files

### Practical Applications

**For Standard Content:**
- Rec.709 color space
- 8-bit color depth
- Standard dynamic range (SDR)

**For HDR Content:**
- Rec.2020 color space
- 10-bit minimum (12-bit for mastering)
- HDR10, HDR10+, or Dolby Vision

**For Grading/Post:**
- Work in higher bit depth than delivery
- Convert to delivery specs in final export
- Maintain maximum quality throughout process

---

## Video File Size Optimization

### Calculating File Size

**Basic Formula:**
File Size (MB) = (Bitrate in Mbps × Duration in seconds) / 8

**Example:**
- 10 Mbps video, 60 seconds = (10 × 60) / 8 = 75 MB

**Factors Affecting File Size:**
- Resolution (higher = larger)
- Frame rate (higher = larger)
- Bitrate (higher = larger)
- Codec efficiency (newer = smaller)
- Content complexity (more motion = larger at same quality)

### Optimization Strategies

**Resolution Optimization:**
- Deliver at appropriate resolution for use
- Don't upscale for no reason
- Consider viewing device (mobile vs. cinema)

**Frame Rate Optimization:**
- Use appropriate frame rate for content
- 24fps for cinematic content
- 30fps for most web content
- 60fps only when needed

**Codec Selection:**
- Use most efficient codec with required compatibility
- H.265 vs H.264 can halve file size
- AV1 offers further gains

**Encoding Settings:**
- Use VBR for best quality/size ratio
- Two-pass encoding for optimal efficiency
- Tune settings for content type

**Pre-Processing:**
- Deinterlace interlaced content
- Reduce noise before encoding
- Apply appropriate sharpening
- Consider resolution scaling

---

## Export Settings for Different Platforms

### YouTube

**Recommended Settings:**
- Container: MP4
- Codec: H.264 (or VP9 for higher quality)
- Resolution: Up to 8K (4K or 1080p most common)
- Frame rate: Match source (up to 60fps)
- Bitrate: 8 Mbps (1080p), 35-45 Mbps (4K)
- Audio: AAC, 384 kbps stereo

**Important Notes:**
- YouTube re-encodes all uploads
- Upload highest quality practical
- Allow processing time for quality options

### Instagram

**Feed Posts:**
- Container: MP4
- Codec: H.264
- Resolution: 1080 × 1080 (1:1), 1080 × 1350 (4:5)
- Frame rate: 30fps
- Bitrate: 3.5 Mbps
- Max length: 60 seconds

**Reels/Stories:**
- Resolution: 1080 × 1920 (9:16)
- Frame rate: 30fps
- Bitrate: 3.5 Mbps
- Max length: 60 seconds (Reels), 15 seconds (Stories)

### TikTok

**Recommended Settings:**
- Container: MP4 or MOV
- Codec: H.264
- Resolution: 1080 × 1920 (9:16)
- Frame rate: 30fps (24-60fps supported)
- Bitrate: 2-6 Mbps
- Max length: 10 minutes

### Facebook

**Feed Video:**
- Container: MP4 or MOV
- Codec: H.264
- Resolution: Up to 4K (1080p common)
- Frame rate: Up to 60fps
- Bitrate: 8-15 Mbps
- Audio: AAC, 128-384 kbps

### Twitter/X

**Recommended Settings:**
- Container: MP4
- Codec: H.264
- Resolution: 1920 × 1080 max
- Frame rate: 30-60fps
- Bitrate: 5-15 Mbps
- Max length: 2:20 (web), 140 seconds (app)

### LinkedIn

**Recommended Settings:**
- Container: MP4
- Codec: H.264
- Resolution: 1920 × 1080 max
- Aspect ratio: 1:2.4 to 2.4:1
- Frame rate: 30fps
- Max length: 10 minutes

### Broadcast Television

**HD Broadcast:**
- Resolution: 1920 × 1080
- Frame rate: 25fps (PAL) or 29.97fps (NTSC)
- Codec: Various (station-specific)
- Audio: PCM or AC-3

**4K Broadcast:**
- Resolution: 3840 × 2160
- Frame rate: Various
- Codec: HEVC typically
- HDR: HLG or HDR10

---

## Delivery Specifications

### Understanding Delivery Specs

Delivery specifications (specs) are technical requirements provided by broadcasters, streaming platforms, or clients for video deliverables.

**Common Spec Elements:**
- Video codec and settings
- Audio codec and settings
- Resolution and frame rate
- Loudness standards
- File naming conventions
- Metadata requirements
- Quality control (QC) requirements

### Creating Deliverables

**Master File:**
- Highest quality version
- Minimal compression
- ProRes 422 HQ or DNxHR HQX typical
- Full resolution and frame rate
- Used to create other deliverables

**Broadcast Deliverable:**
- Specific format for network
- Usually HD or 4K
- Specific codec (often XDCAM, ProRes, or MXF)
- Closed captions required
- Specific loudness standard

**Streaming Deliverable:**
- H.264 or HEVC codec
- Adaptive bitrate ladder often required
- Multiple resolution versions
- Specific audio configuration

**Archive Deliverable:**
- Highest practical quality
- Uncompressed or lightly compressed
- All tracks (stems) included
- Comprehensive metadata

### Quality Control (QC)

**Automated QC:**
- Tools check technical specifications
- Loudness, levels, format compliance
- Generates error reports
- Examples: Baton, Interra Baton, Vidchecker

**Manual QC:**
- Human review of content
- Catches creative issues automation misses
- Full playback review
- Documentation of issues

---

## Transcoding and Encoding

### Understanding Transcoding

Transcoding is converting video from one format to another—changing codec, resolution, bitrate, or other parameters.

**When Transcoding:**
- Converting camera formats for editing
- Creating deliverables from master
- Converting between platforms
- Compressing for web delivery

### Encoding Best Practices

**Maintain Quality:**
- Start from highest quality source
- Avoid multiple generations of lossy encoding
- Use appropriate bitrate for quality level
- Preview before batch processing

**Optimize Settings:**
- Match encoder settings to content
- Use appropriate presets as starting points
- Customize for specific needs
- Test encoding settings before full batch

**Hardware vs. Software Encoding:**

**Hardware Encoding (GPU):**
- Much faster encoding
- Slightly lower quality at same bitrate
- Good for real-time applications
- Intel Quick Sync, NVIDIA NVENC, AMD VCE

**Software Encoding (CPU):**
- Higher quality at same bitrate
- Slower encoding
- More flexible settings
- Better for final deliverables

### Popular Encoding Tools

**FFmpeg:**
- Free, open-source
- Command-line based
- Extremely powerful and flexible
- Industry standard for automation

**HandBrake:**
- Free, open-source
- User-friendly GUI
- Good presets
- Based on FFmpeg

**Adobe Media Encoder:**
- Adobe integration
- Watch folders
- Multiple output presets
- Professional workflow

**Apple Compressor:**
- Apple ecosystem integration
- Final Cut Pro integration
- Good quality
- Mac only

**DaVinci Resolve:**
- Built into editing/grading software
- Professional quality
- Extensive format support
- Free version available

---

## Proxy Workflows

### Understanding Proxies

Proxies are lower-resolution, lower-bitrate copies of source footage used during editing, with the original high-quality files used for final output.

**Why Use Proxies:**
- Edit high-resolution footage on limited hardware
- Improve editing responsiveness
- Enable remote editing (smaller files to transfer)
- Work with challenging codecs (R3D, BRAW, etc.)

### Creating Proxies

**Resolution:**
- Typically 1/4 or 1/2 original resolution
- 1920 × 1080 proxies for 4K source
- 960 × 540 proxies for bandwidth-limited scenarios

**Codec:**
- ProRes Proxy or ProRes LT
- DNxHD 36 or similar
- H.264 (less ideal but smaller)
- Match frame rate to original

**Process:**
1. Import original media
2. Create proxies with consistent settings
3. Link proxies in editing software
4. Edit using proxies
5. Relink to originals for final output

### Proxy Workflow in Different NLEs

**Adobe Premiere Pro:**
- Create proxies directly in project
- Toggle between proxy and original
- Automatic relinking for export

**DaVinci Resolve:**
- Generate optimized media
- Proxy mode in project settings
- Relink for final delivery

**Final Cut Pro:**
- Create proxy media on import
- Switch between original and proxy
- Use original quality for export

---

## Video Streaming Protocols

### Understanding Streaming

Streaming delivers video over the internet, allowing playback to begin before the entire file is downloaded.

**Progressive Download vs. Streaming:**
- Progressive: File downloads linearly, playback can start early
- Streaming: Server sends only needed portions, adapts to conditions

### Common Protocols

**HTTP Live Streaming (HLS):**
- Apple's adaptive bitrate protocol
- Most widely supported
- Uses .m3u8 playlists
- Segments video into small chunks
- Supports multiple quality levels

**DASH (Dynamic Adaptive Streaming over HTTP):**
- International standard
- Codec-agnostic
- Similar to HLS in function
- Used by YouTube, Netflix

**RTMP (Real-Time Messaging Protocol):**
- Adobe protocol
- Used primarily for ingest (sending to platforms)
- Low latency
- Being replaced by newer protocols

**WebRTC:**
- Real-time communication protocol
- Ultra-low latency
- Used for video calls, live streaming
- Browser-native support

### Adaptive Bitrate Streaming

**How It Works:**
1. Video encoded at multiple quality levels (bitrate ladder)
2. Server monitors viewer's bandwidth
3. Automatically switches between quality levels
4. Provides best experience for connection

**Bitrate Ladder Example:**
| Resolution | Bitrate | Use |
|------------|---------|-----|
| 1920 × 1080 | 8 Mbps | High bandwidth |
| 1280 × 720 | 4 Mbps | Medium bandwidth |
| 854 × 480 | 2 Mbps | Low bandwidth |
| 640 × 360 | 800 kbps | Very low bandwidth |

---

## Archiving and Storage

### Archiving Best Practices

**Master Preservation:**
- Keep original camera files
- Keep editing project files
- Keep high-quality masters
- Document workflow and settings

**Archive Formats:**
- ProRes 4444 or DNxHR 444 for maximum quality
- Uncompressed for ultimate preservation
- Include all tracks and elements

**Storage Media:**
- RAID arrays for active projects
- LTO tape for long-term archive
- Cloud storage for offsite backup
- Multiple copies in different locations

### Storage Calculations

**Estimating Storage Needs:**

**Raw Footage (per hour):**
| Format | Approximate Size |
|--------|------------------|
| 1080p H.264 (20 Mbps) | ~9 GB/hour |
| 4K H.264 (100 Mbps) | ~45 GB/hour |
| 4K ProRes 422 | ~110 GB/hour |
| 4K ProRes 4444 | ~220 GB/hour |
| 4K RAW | ~180-500 GB/hour |

**Project Planning:**
- Calculate raw footage duration
- Add 20-50% for renders, exports, versions
- Consider proxy files
- Plan for archive copies

### Backup Strategies

**3-2-1 Rule:**
- 3 copies of data
- 2 different media types
- 1 offsite location

**Verification:**
- Verify backups regularly
- Test restore procedures
- Monitor storage health
- Replace aging media

---

## Common Technical Issues

### Playback Problems

**Stuttering/Dropped Frames:**
- Cause: Insufficient CPU/GPU, slow storage
- Solution: Use proxy workflow, upgrade hardware, optimize storage

**Codec Not Recognized:**
- Cause: Missing codec, unsupported format
- Solution: Install codec pack, transcode to compatible format

**Color Appears Wrong:**
- Cause: Color space mismatch
- Solution: Verify color management, apply correct LUT

### Export Issues

**File Won't Play:**
- Cause: Wrong codec/container combination
- Solution: Use standard combinations (H.264 in MP4)

**Quality Lower Than Expected:**
- Cause: Insufficient bitrate, wrong settings
- Solution: Increase bitrate, use two-pass, check settings

**File Too Large:**
- Cause: Excessive bitrate, inefficient codec
- Solution: Reduce bitrate, use more efficient codec

**Audio Out of Sync:**
- Cause: Frame rate mismatch, conversion error
- Solution: Verify frame rates match, check audio sample rate

---

## Best Practices

### Workflow Best Practices

1. **Organize Media**: Consistent folder structure and naming
2. **Use Proxies**: When working with high-resolution footage
3. **Work Non-Destructively**: Keep originals intact
4. **Document Settings**: Record important technical decisions
5. **Verify Output**: Always check exports before delivery

### Quality Best Practices

1. **Start High, Finish Appropriate**: Capture highest quality, deliver appropriate quality
2. **Minimize Generations**: Each encode degrades quality
3. **Match Specs**: Follow delivery specifications exactly
4. **Test Before Batch**: Verify settings on sample before processing all
5. **QC Everything**: Watch final output completely

### Efficiency Best Practices

1. **Use Presets**: Create and save common settings
2. **Batch Process**: Process multiple files together when possible
3. **Hardware Encoding**: For speed when quality allows
4. **Optimize Storage**: Fast storage for editing, archive for storage
5. **Automate Routine Tasks**: Use watch folders, scripts

---

## Tools and Resources

### Encoding Tools

- **FFmpeg**: Free, command-line, extremely powerful
- **HandBrake**: Free, GUI, consumer-friendly
- **Adobe Media Encoder**: Professional, Adobe integration
- **Apple Compressor**: Professional, Apple integration
- **Shutter Encoder**: Free, GUI, many formats

### Analysis Tools

- **MediaInfo**: Detailed technical metadata
- **FFprobe**: Command-line analysis (part of FFmpeg)
- **VLC**: Playback and basic analysis
- **DaVinci Resolve**: Professional analysis tools

### Learning Resources

- **Frame.io Creative Guide**: Video workflow resource
- **Streaming Learning Center**: Compression and streaming
- **Codec landscape**: Comprehensive codec information
- **Documentation**: FFmpeg, HandBrake, Adobe official docs

---

## Interlaced vs. Progressive Video

### Understanding Interlacing

Interlacing was developed for early television, displaying odd and even lines of each frame alternately to reduce bandwidth while maintaining perceived motion smoothness.

**Interlaced (i):**
- Displays two fields per frame (odd lines, then even lines)
- Written as 1080i, 480i, etc.
- Each field contains half the vertical resolution
- Creates combing artifacts during motion
- Legacy broadcast standard

**Progressive (p):**
- Displays complete frames sequentially
- Written as 1080p, 720p, etc.
- No interlacing artifacts
- Modern standard for most content

### Deinterlacing

When working with interlaced content, deinterlacing converts to progressive format:

**Methods:**
- **Bob**: Displays each field as full frame (doubles frame rate)
- **Weave**: Combines fields (causes combing on motion)
- **Blend**: Averages fields (causes blur)
- **Adaptive**: Analyzes motion, applies appropriate method
- **IVTC (Inverse Telecine)**: Recovers original 24p from 30i

**Best Practices:**
- Deinterlace before editing when possible
- Use high-quality adaptive algorithms
- Match output frame rate appropriately
- Preview results before batch processing

---

## Video Metadata

### Types of Video Metadata

**Technical Metadata:**
- Resolution, frame rate, codec
- Color space, bit depth
- Duration, file size
- Creation date, modification date

**Descriptive Metadata:**
- Title, description
- Keywords, tags
- Cast, crew credits
- Copyright information

**Administrative Metadata:**
- Rights management
- File provenance
- Version information
- Processing history

### Metadata Importance

**For Organization:**
- Searchable archives
- Asset management
- Version tracking
- Content discovery

**For Delivery:**
- Platform requirements
- Copyright embedding
- Accessibility information
- Technical compliance

### Metadata Tools

- **ExifTool**: Read/write metadata across formats
- **MediaInfo**: Detailed technical analysis
- **Adobe Bridge**: Visual metadata management
- **DAM Systems**: Enterprise asset management

---

## Variable Frame Rate (VFR) Handling

### Understanding VFR

Variable Frame Rate means the frame rate changes throughout the video, common in:
- Smartphone recordings
- Screen recordings
- Game capture
- Some action cameras

### VFR Problems

- Audio sync drift
- Editing software issues
- Inconsistent playback
- Export problems

### VFR Solutions

**Convert to Constant Frame Rate:**
1. Identify actual frame rate range
2. Choose target CFR (usually highest or 30fps)
3. Transcode with frame rate conversion
4. Verify audio remains in sync

**Tools:**
- HandBrake: CFR conversion option
- FFmpeg: -r flag for frame rate
- Shutter Encoder: Frame rate control

---

## HDR Video Standards

### Understanding HDR

High Dynamic Range (HDR) expands the range of brightness and colors in video, creating more realistic and impactful images.

**Key HDR Elements:**
- Wider brightness range (up to 10,000 nits peak)
- Wider color gamut (Rec.2020)
- Higher bit depth (10-bit minimum)
- Specialized transfer functions

### HDR Formats

**HDR10:**
- Open standard, no licensing fees
- Static metadata (same settings for entire video)
- 10-bit color depth
- Widely supported
- Base HDR format

**HDR10+:**
- Samsung/Amazon backed
- Dynamic metadata (scene-by-scene adjustment)
- No licensing fees
- Growing support

**Dolby Vision:**
- Premium HDR format
- Dynamic metadata
- Up to 12-bit color
- Licensing required
- Highest quality, most complex

**HLG (Hybrid Log-Gamma):**
- Backward compatible with SDR displays
- Broadcast-friendly
- No metadata required
- Used for live broadcast

### HDR Workflow Considerations

**Capture:**
- Shoot in LOG or RAW for maximum flexibility
- Monitor with HDR display during production
- Expose for highlights

**Post-Production:**
- Grade in HDR-capable software
- Use HDR reference monitor
- Create SDR version (trim pass)
- Verify on consumer HDR displays

**Delivery:**
- Match platform HDR requirements
- Include required metadata
- Provide SDR fallback when needed

---

## Multi-Camera and Multi-Format Workflows

### Handling Multiple Sources

Modern productions often use multiple cameras and formats:
- A-camera and B-camera setups
- Different camera brands
- Drone footage
- Smartphone footage
- Screen recordings

### Workflow Strategies

**Normalize on Ingest:**
1. Transcode all footage to common format
2. Match resolution and frame rate
3. Apply basic color normalization
4. Organize consistently

**Edit Natively, Transcode on Export:**
1. Edit with native formats
2. Use optimized media if needed
3. Conform everything in export
4. May have longer export times

### Format Matching

**Resolution Matching:**
- Upscale lower resolution to match highest
- Use quality upscaling algorithms
- Or crop/letterbox higher resolution

**Frame Rate Matching:**
- Convert to common frame rate
- Consider pulldown/pullup effects
- 24p and 30p mixing requires care

**Color Matching:**
- Apply camera-specific LUTs
- Manual color matching in grade
- Match using scopes

---

## Timecode and Synchronization

### Understanding Timecode

Timecode is a standardized time reference used to identify video frames:

**Format:** HH:MM:SS:FF (Hours:Minutes:Seconds:Frames)

**Types:**
- **Drop-Frame**: Accounts for 29.97fps timing
- **Non-Drop-Frame**: Linear count (may drift from real time)
- **Record Run**: Continuous during recording
- **Free Run**: Continuous regardless of recording state

### Timecode Uses

**Synchronization:**
- Sync multiple cameras
- Sync external audio
- Maintain frame-accurate editing

**Logging:**
- Identify specific moments
- Reference in notes
- Communication about content

**Broadcast:**
- Required for professional delivery
- QC and compliance checking
- Archive reference

### Jam Sync

Synchronizing timecode between devices:
1. Set master timecode source
2. Connect and sync all devices
3. Verify sync before recording
4. Re-jam periodically for long shoots

---

## Platform-Specific Encoding Templates

### YouTube Encoding Template

**High Quality 1080p:**
```
Resolution: 1920 × 1080
Frame Rate: Match source (24/30/60fps)
Codec: H.264 (High Profile)
Bitrate: 10-12 Mbps VBR
Audio: AAC 320 kbps stereo
Container: MP4
```

**4K HDR:**
```
Resolution: 3840 × 2160
Frame Rate: Match source
Codec: H.265/HEVC (Main 10)
Bitrate: 40-50 Mbps VBR
Color: Rec.2020, HDR10 or HLG
Audio: AAC 384 kbps
Container: MP4
```

### Instagram Encoding Template

**Feed Video:**
```
Resolution: 1080 × 1350 (4:5)
Frame Rate: 30fps
Codec: H.264
Bitrate: 3.5 Mbps
Audio: AAC 128 kbps
Max Duration: 60 seconds
Container: MP4
```

**Reels:**
```
Resolution: 1080 × 1920 (9:16)
Frame Rate: 30fps
Codec: H.264
Bitrate: 4-6 Mbps
Audio: AAC 128 kbps
Max Duration: 90 seconds
Container: MP4
```

### TikTok Encoding Template

```
Resolution: 1080 × 1920 (9:16)
Frame Rate: 30fps preferred
Codec: H.264
Bitrate: 4-6 Mbps
Audio: AAC 128 kbps
Max Duration: 10 minutes
Container: MP4
```

### Broadcast Delivery Template

**HD Broadcast (US):**
```
Resolution: 1920 × 1080
Frame Rate: 29.97fps (59.94i)
Codec: XDCAM HD422 or ProRes 422
Bitrate: 50 Mbps
Audio: PCM 48kHz 24-bit
Loudness: -24 LUFS (ATSC A/85)
Container: MXF or MOV
```

---

## Troubleshooting Common Issues

### Video Won't Import

**Possible Causes:**
- Unsupported codec
- Corrupted file header
- Incorrect file extension
- Software limitation

**Solutions:**
- Install required codec pack
- Transcode to widely-supported format
- Try different editing software
- Check file integrity with MediaInfo

### Export Quality is Poor

**Possible Causes:**
- Bitrate too low
- Wrong codec settings
- Scaling artifacts
- Over-compression

**Solutions:**
- Increase bitrate (50-100% higher)
- Use appropriate codec for resolution
- Export at source resolution
- Use two-pass encoding

### Colors Look Wrong

**Possible Causes:**
- Color space mismatch
- Missing color profile
- Display calibration issues
- Export settings incorrect

**Solutions:**
- Verify input/output color space settings
- Apply correct gamma/transfer function
- Calibrate display
- Check for "full range" vs "legal range" settings

### Audio Issues

**Possible Causes:**
- Sample rate mismatch
- Codec incompatibility
- Channels incorrect
- Sync drift

**Solutions:**
- Convert audio to 48kHz
- Use widely-compatible audio codec (AAC)
- Verify stereo/mono settings
- Check for VFR in source video

---

## Conclusion

Understanding video technical standards is essential for anyone producing professional video content. From resolution and frame rate fundamentals to advanced codec selection and platform-specific delivery, mastering these concepts ensures your content plays correctly and looks its best everywhere.

Key principles to remember:

- **Capture at the highest practical quality** and deliver at appropriate specifications
- **Choose codecs based on use case**: Production codecs for editing, delivery codecs for distribution
- **Understand your delivery platform**: Each has specific requirements
- **Optimize for the viewing context**: Mobile screens need different treatment than cinema
- **Always verify output**: Check deliverables before sending

As video technology evolves with new codecs (AV1), higher resolutions (8K), and new delivery methods (streaming improvements), these fundamental principles remain constant. Understanding the relationships between resolution, frame rate, codec, bitrate, and color ensures you can adapt to any technical requirement.

Professional video work requires attention to these technical details. While creative excellence captures attention, technical excellence ensures audiences can actually experience your work as intended.