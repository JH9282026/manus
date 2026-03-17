# Post-Production

Comprehensive guide to editing, sound design, color correction, visual effects, and exporting stop-motion animation.

## Importing and Organizing Footage

### Image Sequence Import

Stop-motion animation is captured as individual image files (JPEG, PNG, TIFF, RAW). Import these as an image sequence in your editing software.

**DaVinci Resolve**:
1. File > Import > Import Media
2. Navigate to folder containing image sequence
3. Select first image in sequence
4. Right-click > "Change Frame Rate" > Set to your capture frame rate (12, 15, 24 fps)
5. Drag sequence to timeline

**Adobe Premiere Pro**:
1. File > Import
2. Navigate to folder, select first image
3. Check "Image Sequence" box
4. Click Import
5. Drag to timeline

**Adobe After Effects**:
1. File > Import > File
2. Select first image in sequence
3. Check "Force alphabetical order" and "JPEG Sequence" (or PNG, TIFF)
4. Set frame rate in Interpret Footage dialog
5. Add to composition

**Final Cut Pro**:
1. File > Import > Files
2. Select all images in sequence
3. Right-click > "Open as Image Sequence"
4. Set frame rate
5. Add to timeline

### File Organization

**Folder Structure**:
```
project-name/
├── footage/
│   ├── scene-01/
│   │   ├── shot-01/
│   │   │   ├── frame_0001.jpg
│   │   │   ├── frame_0002.jpg
│   │   │   └── ...
│   │   ├── shot-02/
│   │   └── ...
│   ├── scene-02/
│   └── ...
├── audio/
│   ├── dialogue/
│   ├── sound-effects/
│   └── music/
├── exports/
│   ├── drafts/
│   └── final/
└── project-files/
    ├── premiere/
    ├── after-effects/
    └── ...
```

**Naming Conventions**:
- Use consistent, descriptive names
- Include scene and shot numbers
- Use leading zeros for frame numbers (frame_0001, not frame_1)
- Avoid spaces (use hyphens or underscores)

## Editing Workflow

### Assembly Edit

1. **Import All Sequences**: Bring all captured shots into editing software
2. **Rough Assembly**: Arrange shots in story order on timeline
3. **Review Flow**: Watch through, identify pacing issues
4. **Trim Excess**: Remove unnecessary frames at beginning/end of shots
5. **Identify Gaps**: Note missing shots or coverage needed

### Fine Cut

1. **Refine Timing**: Adjust shot lengths for optimal pacing
2. **Add Transitions**: Cuts, fades, dissolves (use sparingly)
3. **Match Action**: Ensure smooth continuity between shots
4. **Rhythm and Pacing**: Vary shot lengths for visual interest
5. **Emotional Beats**: Allow time for audience to absorb moments

### Editing Principles for Stop-Motion

**Timing**:
- Stop-motion often feels slower than live-action
- Trim shots tighter than you think (remove "dead" frames)
- Use quick cuts for energy, longer shots for contemplation
- Match cuts to music beats if applicable

**Continuity**:
- Watch for lighting changes between shots
- Check character positions and poses for consistency
- Ensure props and set pieces don't jump positions
- Match eyelines and screen direction

**Coverage**:
- Wide shots establish location and spatial relationships
- Medium shots show action and character interaction
- Close-ups convey emotion and detail
- Vary shot sizes for visual interest

## Sound Design

### Dialogue Recording

**Pre-Recording (Recommended)**:
1. Record dialogue before animating
2. Import audio into animation software (Dragonframe)
3. Animate lip sync to match recorded dialogue
4. Ensures perfect sync and natural performance

**Post-Recording**:
1. Animate first, record dialogue after
2. Actor matches performance to animation
3. More difficult to achieve natural sync
4. Use when dialogue is improvised or flexible

**Recording Setup**:
- **Microphone**: USB condenser mic (Blue Yeti, Audio-Technica AT2020) or XLR with interface
- **Environment**: Quiet room, minimal echo (closet with clothes, blankets for dampening)
- **Software**: Audacity (free), Adobe Audition, Logic Pro, GarageBand
- **Technique**: 6-12 inches from mic, pop filter to reduce plosives (P, B sounds)

**Dialogue Editing**:
1. Remove background noise (noise reduction in Audacity/Audition)
2. Normalize levels (consistent volume)
3. EQ to enhance clarity (boost 2-5 kHz for presence)
4. Compress to even out dynamics
5. Export as WAV or AIFF (uncompressed) for editing

### Sound Effects

**Sources**:
- **Free Libraries**: Freesound.org, BBC Sound Effects, YouTube Audio Library
- **Paid Libraries**: Epidemic Sound, AudioJungle, Soundsnap
- **Foley (DIY)**: Record custom sounds for specific actions
- **Synthesis**: Create sounds in software (whooshes, impacts, sci-fi)

**Common Stop-Motion Sound Effects**:
- **Footsteps**: Match character movement (light taps for small characters, heavier for large)
- **Impacts**: Punches, falls, collisions (exaggerate for cartoon style)
- **Ambience**: Background sounds (wind, birds, room tone)
- **Object Sounds**: Doors, props, vehicles (match on-screen action)
- **Whooshes**: Fast movements, transitions
- **Stingers**: Musical accents for comedic or dramatic moments

**Foley Recording**:
1. Watch animation, note sounds needed
2. Gather props that produce desired sounds
3. Record while watching video (sync to action)
4. Experiment with unexpected objects (creativity encouraged)
5. Record multiple takes, choose best

**Sound Effect Editing**:
1. Trim to exact timing (align with visual action)
2. Layer multiple sounds for richness (footstep = tap + rustle + creak)
3. EQ to fit in mix (remove low frequencies from small objects)
4. Add reverb for environment (small room, large hall, outdoor)
5. Adjust volume for realism and emphasis

### Music

**Sourcing Music**:
- **Original Composition**: Hire composer or create yourself
- **Stock Music**: Epidemic Sound, AudioJungle, Artlist, Pond5
- **Royalty-Free**: YouTube Audio Library, Free Music Archive, Incompetech
- **Licensed**: Purchase rights to existing songs (expensive)

**Music Selection**:
- Match tone and mood of animation
- Consider tempo and rhythm (align with pacing)
- Avoid overpowering dialogue or sound effects
- Use silence strategically (not every moment needs music)

**Music Editing**:
1. Import music to timeline
2. Align musical beats with visual beats (cuts, actions)
3. Fade in/out for smooth transitions
4. Adjust volume to balance with dialogue and effects
5. EQ if needed (reduce frequencies that clash with dialogue)

### Audio Mixing

**Level Balancing**:
- **Dialogue**: Loudest, clearest (typically -12 to -6 dB)
- **Sound Effects**: Support action, don't overpower (-18 to -12 dB)
- **Music**: Background, fills space (-24 to -18 dB)
- **Ambience**: Subtle, barely noticeable (-30 to -24 dB)

**Panning**:
- Position sounds in stereo field (left, center, right)
- Match on-screen position (character on left = sound on left)
- Center dialogue for clarity
- Spread music and ambience for width

**EQ (Equalization)**:
- **Dialogue**: Boost 2-5 kHz for clarity, cut below 80 Hz (rumble)
- **Sound Effects**: Shape to fit (bright, dull, thin, full)
- **Music**: Cut frequencies that clash with dialogue (2-4 kHz)
- **Ambience**: Roll off highs for subtlety

**Compression**:
- Even out volume dynamics
- Make quiet parts louder, loud parts quieter
- Apply to dialogue for consistency
- Use on master track for overall cohesion

**Reverb**:
- Add sense of space and environment
- Small room: short reverb (0.5-1 sec)
- Large hall: long reverb (2-4 sec)
- Outdoor: minimal reverb, add ambience instead
- Match reverb across all sounds in same scene

**Final Mix**:
1. Balance all levels (dialogue, effects, music, ambience)
2. Pan sounds to stereo positions
3. Apply EQ to each track
4. Add compression and reverb
5. Listen on multiple systems (headphones, speakers, phone)
6. Adjust until balanced and clear
7. Export master audio (WAV, 48 kHz, 24-bit)

## Color Correction and Grading

### Color Correction (Technical)

Fix technical issues: exposure, white balance, contrast.

**Exposure**:
- Adjust brightness to proper levels
- Recover highlights (bright areas) and shadows (dark areas)
- Use waveform monitor to ensure levels within range

**White Balance**:
- Correct color temperature (remove color casts)
- Use white balance tool (select neutral gray/white in image)
- Or manually adjust temperature slider (warmer/cooler)

**Contrast**:
- Adjust difference between darkest and lightest areas
- Increase for punchy, dramatic look
- Decrease for soft, muted look
- Use curves or levels for precise control

**Consistency**:
- Match shots within same scene (same lighting, color)
- Copy color correction from one shot to similar shots
- Use reference frame to match

### Color Grading (Creative)

Apply creative color choices for mood and style.

**Color Palettes**:
- **Warm** (orange, yellow): Happy, nostalgic, energetic
- **Cool** (blue, teal): Sad, calm, mysterious
- **Desaturated**: Serious, gritty, realistic
- **Saturated**: Vibrant, fantastical, stylized
- **Monochrome**: Timeless, artistic, dramatic

**Common Grades**:
- **Teal and Orange**: Popular cinematic look (skin tones orange, shadows teal)
- **Bleach Bypass**: Desaturated, high contrast (gritty, intense)
- **Vintage**: Faded colors, warm tones, vignette (nostalgic)
- **High Key**: Bright, low contrast (cheerful, optimistic)
- **Low Key**: Dark, high contrast (dramatic, mysterious)

**Grading Workflow**:
1. Apply color correction first (fix technical issues)
2. Choose color palette/mood
3. Adjust overall color balance (temperature, tint)
4. Adjust saturation (vibrant or muted)
5. Apply secondary corrections (isolate and adjust specific colors)
6. Add vignette or other effects if desired
7. Apply grade to all shots in scene
8. Fine-tune individual shots as needed

**Tools**:
- **DaVinci Resolve**: Industry-standard color grading (free version available)
- **Adobe Premiere Pro**: Lumetri Color panel
- **Final Cut Pro**: Color Board and Color Wheels
- **Adobe After Effects**: Color correction effects

## Visual Effects and Compositing

### Rig Removal

**Process**:
1. Shoot clean plate (frame without character, shows background)
2. Import rigged shot and clean plate into After Effects
3. Layer clean plate above rigged shot
4. Mask out rig on clean plate layer, revealing background
5. Refine mask edges (feather for smooth blend)
6. Repeat for all frames (animate mask if rig moves)
7. Export cleaned sequence

**Alternative (Clone Stamp)**:
1. Import rigged shot into Photoshop or After Effects
2. Use Clone Stamp tool to paint over rig with surrounding background
3. Repeat for each frame (tedious for long sequences)
4. Export cleaned sequence

### Green Screen / Chroma Key

**Shooting**:
1. Set up green screen backdrop (fabric or painted)
2. Light green screen evenly (no shadows or hotspots)
3. Separate character from green screen (avoid green spill on character)
4. Animate character in front of green screen
5. Capture frames

**Keying**:
1. Import footage into After Effects or Premiere Pro
2. Apply Keylight effect (After Effects) or Ultra Key (Premiere)
3. Select green color to remove
4. Adjust settings (Screen Gain, Screen Balance) for clean key
5. Use Spill Suppression to remove green tint on character edges
6. Refine matte (erode, choke, feather edges)
7. Add background layer beneath keyed character
8. Color correct character to match background lighting

### Adding Digital Elements

**Backgrounds**:
- Replace or enhance backgrounds with digital images or video
- Use parallax (move background slower than foreground) for depth
- Match lighting and color between character and background

**Effects**:
- **Particles**: Dust, sparks, magic, snow (use particle generators)
- **Glows**: Lightsabers, magic, eyes (use glow effects)
- **Motion Graphics**: Titles, credits, animated text
- **Explosions**: Practical (cotton, LEDs) or digital (stock footage, 3D)

**Compositing Workflow**:
1. Layer elements (background, character, effects, foreground)
2. Match lighting and color across all layers
3. Add shadows if needed (character shadow on background)
4. Apply depth of field (blur background or foreground)
5. Add camera shake or movement for realism
6. Render final composite

### Frame Blending and Smoothing

**Frame Blending**:
- Software creates intermediate frames between captured frames
- Smooths motion, increases effective frame rate
- Use sparingly (can create ghosting or artifacts)
- Available in After Effects, Premiere Pro, DaVinci Resolve

**Optical Flow**:
- Advanced frame blending using motion analysis
- Creates more realistic intermediate frames
- Use for slow-motion effects or smoothing jerky motion
- Computationally intensive (slow rendering)

**When to Use**:
- Smoothing slightly jerky animation
- Creating slow-motion from normal speed footage
- Increasing frame rate for specific platforms (24 fps to 30 fps)

**When to Avoid**:
- Intentionally choppy, stylized animation
- Fast, complex motion (creates artifacts)
- When authentic stop-motion aesthetic is desired

## Titles and Credits

### Opening Titles

**Styles**:
- **Simple Text**: Clean, minimal (title and creator name)
- **Animated Text**: Kinetic typography, motion graphics
- **Integrated**: Title appears in scene (on sign, object)
- **Stop-Motion Titles**: Animate physical letters or objects

**Information to Include**:
- Film title
- Creator name(s)
- Optional: "A film by...", production company, year

### End Credits

**Information to Include**:
- Cast (voice actors, if applicable)
- Crew (director, animator, editor, sound designer, composer, etc.)
- Special thanks
- Music credits (song titles, artists, licensing info)
- Sound effects credits (libraries used)
- Software and tools used (optional)
- Copyright notice

**Format**:
- Scrolling credits (traditional)
- Static cards (one per role or group)
- Animated credits (creative, playful)

### Design Tips

- **Readability**: Use clear, legible fonts (avoid overly decorative)
- **Contrast**: Ensure text stands out from background
- **Timing**: Allow enough time to read (3-5 seconds per card)
- **Style**: Match tone of film (playful, serious, elegant)
- **Music**: Continue or add music during credits

## Exporting and Delivery

### Export Settings by Platform

**YouTube / Vimeo**:
- **Format**: MP4 (H.264 codec)
- **Resolution**: 1920x1080 (1080p) or 3840x2160 (4K)
- **Frame Rate**: Match source (24, 30, or 60 fps)
- **Bitrate**: 8-12 Mbps (1080p), 35-45 Mbps (4K)
- **Audio**: AAC, 320 kbps, 48 kHz

**Instagram**:
- **Format**: MP4 (H.264)
- **Resolution**: 1080x1080 (square), 1080x1350 (portrait), 1920x1080 (landscape)
- **Frame Rate**: 30 fps
- **Duration**: Up to 60 seconds (feed), 15 seconds (stories), 60 minutes (IGTV)
- **Bitrate**: 5-8 Mbps
- **Audio**: AAC, 128 kbps

**TikTok**:
- **Format**: MP4 (H.264)
- **Resolution**: 1080x1920 (vertical)
- **Frame Rate**: 30 fps
- **Duration**: Up to 10 minutes
- **Bitrate**: 5-8 Mbps
- **Audio**: AAC, 128 kbps

**Film Festivals**:
- **Format**: ProRes 422 HQ or DNxHD (high quality, large file size)
- **Resolution**: 1920x1080 or higher
- **Frame Rate**: 24 fps (cinematic standard)
- **Audio**: Uncompressed WAV or AIFF, 48 kHz, 24-bit
- Check specific festival requirements (vary by festival)

**Broadcast / TV**:
- **Format**: ProRes 422 HQ, DNxHD, or as specified by broadcaster
- **Resolution**: 1920x1080 (HD) or 3840x2160 (4K)
- **Frame Rate**: 29.97 fps (NTSC) or 25 fps (PAL)
- **Audio**: Stereo or 5.1 surround, 48 kHz, 24-bit
- **Specifications**: Follow broadcaster's technical requirements exactly

**Archive / Master**:
- **Format**: ProRes 4444 or uncompressed (maximum quality)
- **Resolution**: Highest captured (match source)
- **Frame Rate**: Match source
- **Audio**: Uncompressed WAV, 48 kHz, 24-bit
- **Purpose**: Long-term storage, future re-exports

### Export Workflow

1. **Final Review**: Watch entire film, check for errors
2. **Audio Check**: Ensure levels are balanced, no clipping
3. **Color Check**: View on calibrated monitor if possible
4. **Export Settings**: Choose appropriate settings for platform
5. **Render**: Export video file
6. **Quality Check**: Watch exported file, ensure no issues
7. **Backup**: Save master file and project files to multiple locations
8. **Deliver**: Upload to platform or send to client/festival

### File Management and Backup

**Backup Strategy**:
- **3-2-1 Rule**: 3 copies, 2 different media types, 1 off-site
  - Example: Original on computer, backup on external drive, cloud backup
- **Backup Frequency**: After each session, weekly, or daily for active projects
- **What to Backup**:
  - Original captured frames (image sequences)
  - Project files (Premiere, After Effects, etc.)
  - Audio files (dialogue, effects, music)
  - Exported videos (drafts and finals)
  - Assets (graphics, titles, reference images)

**Storage Solutions**:
- **External Hard Drives**: Affordable, portable (2-5 TB recommended)
- **NAS (Network Attached Storage)**: Centralized, accessible from multiple devices
- **Cloud Storage**: Google Drive, Dropbox, Backblaze (off-site backup)
- **Archive**: Burn to Blu-ray or store on dedicated archive drives (long-term)

**File Naming**:
- Use descriptive, consistent names
- Include version numbers (v01, v02, v03)
- Include date (YYYYMMDD format)
- Example: `my-film_final_v03_20260317.mp4`

## Post-Production Checklist

**Import and Organization**:
- [ ] Import all image sequences
- [ ] Organize footage by scene and shot
- [ ] Create project folder structure
- [ ] Back up original files

**Editing**:
- [ ] Assemble rough cut
- [ ] Refine timing and pacing
- [ ] Add transitions (if needed)
- [ ] Check continuity
- [ ] Review with fresh eyes or test audience

**Sound Design**:
- [ ] Record or import dialogue
- [ ] Add sound effects
- [ ] Add music
- [ ] Mix audio (levels, panning, EQ, reverb)
- [ ] Export master audio

**Color Correction and Grading**:
- [ ] Correct exposure and white balance
- [ ] Match shots within scenes
- [ ] Apply creative color grade
- [ ] Review on multiple displays

**Visual Effects**:
- [ ] Remove rigs and supports
- [ ] Add digital elements (if needed)
- [ ] Composite green screen (if used)
- [ ] Add titles and credits

**Export**:
- [ ] Choose export settings for platform
- [ ] Render final video
- [ ] Quality check exported file
- [ ] Create multiple versions if needed (social media, festival, archive)

**Delivery and Backup**:
- [ ] Upload to platform or send to client
- [ ] Back up master file
- [ ] Back up project files and assets
- [ ] Archive project (external drive, cloud, Blu-ray)
- [ ] Celebrate completion!
