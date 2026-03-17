# Synchronization and Mixing

This reference covers techniques for synchronizing Foley to picture and integrating Foley sounds into the final mix.

## Synchronization Fundamentals

### Why Sync Matters

Precise synchronization is the foundation of effective Foley.

**Impact of Poor Sync**:
- Sounds feel disconnected from picture
- Breaks immersion
- Looks unprofessional
- Distracts audience
- Undermines storytelling

**Frame Accuracy**:
- Film/video: 24, 25, 30, or 60 frames per second
- Sync must be frame-accurate
- Even 1-2 frames off is noticeable
- Critical for impacts, footsteps, specific actions

**Perceptual Tolerance**:
- Visual leads audio: Noticeable immediately
- Audio leads visual: Slightly more tolerance (1-2 frames)
- Footsteps: Very sensitive (must be exact)
- Cloth: More forgiving
- Impacts: Must be exact

### Timecode and Frame Rates

**Timecode Format**: HH:MM:SS:FF (Hours:Minutes:Seconds:Frames)

**Common Frame Rates**:
- **24 fps**: Film standard
- **25 fps**: PAL video (Europe)
- **29.97 fps**: NTSC video (Americas, drop-frame)
- **30 fps**: NTSC video (non-drop)
- **23.976 fps**: Film transferred to video
- **60 fps**: High frame rate video

**Drop-Frame vs. Non-Drop**:
- **Drop-frame**: Compensates for 29.97 fps (not exactly 30)
- **Non-drop**: Simpler, but drifts over time
- Important for broadcast
- Ensure DAW matches video

**Matching Frame Rates**:
- DAW session must match video frame rate
- Verify before starting
- Incorrect frame rate causes sync drift
- Check project settings

### Sync Methods

**1. Performed in Sync**
- Foley artist performs while watching picture
- Recorded in sync with video
- Most common method
- Minimal post-sync adjustment

**2. Post-Sync Alignment**
- Perform freely, sync later in editing
- Editor aligns to picture
- More time in post
- Allows focus on performance quality

**3. Timecode Sync**
- Embedded timecode in recording
- Automatic alignment in DAW
- Professional workflow
- Requires timecode-capable equipment

**4. Manual Sync**
- Visual alignment in DAW
- Drag audio to match picture
- Frame-by-frame adjustment
- Most common in post

## Editing Foley for Sync

### Importing and Organization

**File Naming**:
- Descriptive names
- Include scene, take number
- Example: "Scene05_Footsteps_Take03.wav"
- Consistent convention

**Track Organization**:
- Separate tracks for feet, moves, specifics
- Multiple tracks per category if needed
- Color coding
- Clear labeling

**Session Setup**:
- Import video
- Set correct frame rate
- Create Foley tracks
- Set up monitoring

### Selecting Takes

**Criteria**:
- **Sync quality**: How well it matches picture
- **Sound quality**: Clean, appropriate tone
- **Performance**: Best execution
- **Consistency**: Matches other takes/scenes

**Comparing Takes**:
- Listen to all takes
- Watch with picture
- Note strengths and weaknesses
- May combine elements from multiple takes

**Comping**:
- Use best parts of multiple takes
- Seamless transitions
- Crossfades between takes
- Create ideal performance

### Fine-Tuning Sync

**Visual Cues**:
- Foot contact with ground
- Hand touching object
- Door reaching closed position
- Impact moments

**Waveform Analysis**:
- Identify transients (sharp peaks)
- Align transient with visual cue
- Zoom in for precision
- Frame-by-frame adjustment

**Nudging**:
- Move audio earlier or later
- Frame-by-frame (or sub-frame)
- Keyboard shortcuts for efficiency
- Fine-tune until perfect

**Slip Editing**:
- Adjust audio position within clip
- Maintain clip position on timeline
- Useful for fine adjustments
- Preserve overall timing

**Checking Sync**:
- Play with picture repeatedly
- Watch and listen critically
- Check at different playback speeds
- Get second opinion

### Cleanup and Editing

**Removing Unwanted Sounds**:
- Breaths (unless intentional)
- Bumps and handling noise
- Extraneous sounds
- Background noise

**Trimming**:
- Remove excess at head and tail
- Tight edits
- No dead space
- Clean starts and stops

**Fades**:
- Fade in at start
- Fade out at end
- Prevents clicks and pops
- Smooth transitions

**Crossfades**:
- Between takes or clips
- Smooth transitions
- Blend seamlessly
- Appropriate length (typically 5-20 ms)

**Noise Reduction** (if needed):
- Use sparingly
- Preserve sound quality
- Better to record clean
- Last resort

### Layering Foley

**Combining Elements**:
- Feet + moves + specifics
- Build complete soundscape
- Each element on separate track
- Balance levels

**Complementary Sounds**:
- Footsteps with clothing rustle
- Door close with latch click
- Object pickup with hand movement
- Natural combinations

**Avoiding Clutter**:
- Don't overdo it
- Every sound should have purpose
- Less is often more
- Serve the story

**Stereo Placement** (in editing):
- Pan to match on-screen position
- Left-right placement
- Movement across stereo field
- Spatial realism

## Mixing Foley

### Integration with Other Elements

Foley must blend seamlessly with dialogue, music, and sound effects.

**The Mix Hierarchy**:
1. **Dialogue**: Usually most important
2. **Music**: Emotional support
3. **Sound effects**: Key story elements
4. **Foley**: Subtle realism
5. **Ambience**: Environmental context

**Foley's Role**:
- Support, don't distract
- Add realism and detail
- Fill in missing sounds
- Enhance immersion
- Usually subtle

### Level Setting

**Starting Point**:
- Set Foley levels conservatively
- Bring up gradually
- Balance with other elements
- Check in context of full mix

**Relative Levels**:
- **Feet**: Moderate level, consistent
- **Moves**: Subtle, background
- **Specifics**: Varies (some prominent, some subtle)

**Ducking Under Dialogue**:
- Reduce Foley when dialogue is present
- Maintain intelligibility
- Automation or sidechain compression
- Subtle reduction (2-4 dB)

**Emphasizing Key Moments**:
- Increase level for important actions
- Draw attention
- Support storytelling
- Automation

**Consistency**:
- Similar sounds at similar levels
- Across scenes and shots
- Maintain continuity
- Reference previous scenes

### Equalization (EQ)

**Purpose**:
- Tonal balance
- Clarity
- Separation from other elements
- Matching to environment

**Common EQ Adjustments**:

**Footsteps**:
- **Low-mid boost** (200-500 Hz): Weight and body
- **High-pass filter** (below 80 Hz): Remove rumble
- **Presence boost** (2-4 kHz): Clarity and detail

**Cloth Movement**:
- **High-pass filter** (below 200 Hz): Remove low-end rumble
- **Gentle high boost** (8-12 kHz): Air and detail
- **Subtle**: Don't make too bright

**Props and Impacts**:
- **Varies by material**
- **Wood**: Warm mids (400-800 Hz)
- **Metal**: Bright highs (4-8 kHz)
- **Glass**: Very bright (8-12 kHz)
- **Adjust to match on-screen material**

**Matching Production Audio**:
- EQ to match dialogue ambience
- Similar tonal quality
- Blend seamlessly
- A/B comparison

**Corrective EQ**:
- Remove unwanted frequencies
- Reduce resonances
- Fix recording issues
- Subtle adjustments

### Compression

**Purpose**:
- Consistent levels
- Control dynamics
- Blend with mix
- Subtle enhancement

**Settings**:
- **Ratio**: 2:1 to 4:1 (gentle)
- **Threshold**: Catch peaks
- **Attack**: Medium to fast (5-20 ms)
- **Release**: Medium (50-200 ms)
- **Gain reduction**: 2-6 dB max

**When to Use**:
- Inconsistent performances
- Blend with compressed dialogue
- Control dynamic range
- Subtle application

**When to Avoid**:
- Over-compression kills realism
- Preserve natural dynamics
- Use sparingly
- Trust good performance

### Reverb and Ambience

**Matching Environment**:
- Foley recorded dry
- Add reverb to match scene location
- Indoor vs. outdoor
- Small room vs. large hall
- Match production audio

**Reverb Types**:
- **Room**: Small spaces
- **Hall**: Large spaces
- **Plate**: Smooth, musical (less common for Foley)
- **Convolution**: Realistic, sampled spaces

**Reverb Parameters**:
- **Decay time**: How long reverb lasts
  - Small room: 0.3-0.8 seconds
  - Medium room: 0.8-1.5 seconds
  - Large hall: 1.5-3+ seconds
- **Pre-delay**: Gap before reverb starts (0-30 ms)
- **EQ**: Shape reverb tone
- **Mix**: Amount of reverb (typically 10-30% for Foley)

**Matching Across Shots**:
- Same scene = same reverb
- Continuity essential
- Save reverb settings
- Consistent application

**Outdoor Scenes**:
- Minimal reverb
- Short decay
- Natural ambience more important
- Don't overdo

**Creative Use**:
- Exaggerate for effect
- Genre-specific (horror: more reverb)
- Support mood
- Collaborate with mixer

### Panning and Stereo Placement

**Matching On-Screen Position**:
- Character on left = pan left
- Character on right = pan right
- Center = center pan
- Follow movement

**Stereo Width**:
- **Narrow**: Intimate, close
- **Wide**: Spacious, distant
- **Mono**: Centered, focused
- Adjust per scene

**Movement Across Field**:
- Automate pan
- Follow character movement
- Smooth transitions
- Realistic spatial movement

**Surround Sound** (5.1, 7.1, Atmos):
- Place sounds in 3D space
- Front, rear, overhead
- Immersive experience
- Specialized mixing

**Mono Compatibility**:
- Check mix in mono
- Ensure clarity
- No phase issues
- Broadcast requirement

### Automation

**Level Automation**:
- Adjust volume over time
- Emphasize key moments
- Duck under dialogue
- Dynamic mix

**Pan Automation**:
- Follow movement
- Left to right
- Smooth transitions
- Realistic motion

**EQ Automation**:
- Change tone over time
- Match changing environments
- Creative effects
- Less common

**Reverb Automation**:
- Adjust reverb amount
- Match changing spaces
- Indoor to outdoor transitions
- Environmental changes

**Plugin Automation**:
- Any parameter can be automated
- Creative possibilities
- Serve the story
- Don't overdo

## Quality Control

### Sync Verification

**Frame-by-Frame Check**:
- Step through critical moments
- Verify exact sync
- Footsteps, impacts, specific actions
- No tolerance for error

**Playback at Different Speeds**:
- Normal speed
- Slow motion (check detail)
- Fast (check overall flow)
- Verify sync holds

**Multiple Viewings**:
- Watch repeatedly
- Fresh eyes/ears
- Catch mistakes
- Refine

**Client/Director Review**:
- Get approval
- Incorporate feedback
- Iterate as needed
- Final sign-off

### Sound Quality Check

**Technical Quality**:
- No distortion or clipping
- No unwanted noise
- Clean recordings
- Appropriate levels

**Tonal Quality**:
- Appropriate frequency balance
- Matches on-screen materials
- Blends with production audio
- Consistent across scenes

**Performance Quality**:
- Convincing sounds
- Appropriate intensity
- Matches character and emotion
- Serves story

**Consistency**:
- Similar sounds across scenes
- Character-specific sounds maintained
- Continuity preserved
- Reference previous work

### Continuity

**Scene-to-Scene**:
- Same character = same sounds
- Same location = same reverb
- Maintain consistency
- Avoid jarring changes

**Episode-to-Episode** (TV):
- Reference previous episodes
- Maintain character sounds
- Consistent approach
- Build library

**Film Series**:
- Maintain across sequels
- Character consistency
- Signature sounds
- Long-term planning

### Final Mix Review

**Full Context**:
- Listen with all elements
- Dialogue, music, SFX, Foley, ambience
- Balanced mix
- Serves story

**Different Playback Systems**:
- Studio monitors
- Headphones
- TV speakers
- Phone/tablet
- Ensure quality across platforms

**Loudness Standards**:
- Broadcast: -23 LUFS (ATSC A/85)
- Streaming: -14 to -16 LUFS (varies by platform)
- Film: Calibrated theater levels
- Meet specifications

**Deliverables**:
- Stems (separate Foley tracks)
- Full mix
- Appropriate file formats
- Documentation

## Advanced Mixing Techniques

### Multiband Processing

**Concept**: Process different frequency ranges independently

**Applications**:
- Control specific frequency issues
- Enhance clarity
- Blend with other elements
- Surgical processing

**Example**:
- Compress only low frequencies (control footstep weight)
- Enhance only high frequencies (cloth detail)
- Reduce specific mid-range (avoid dialogue conflict)

### Sidechain Compression

**Concept**: Compress Foley based on another signal (usually dialogue)

**Purpose**:
- Automatic ducking under dialogue
- Maintain intelligibility
- Dynamic mix
- Hands-off approach

**Setup**:
- Compressor on Foley track
- Sidechain input from dialogue
- Adjust threshold and ratio
- Subtle reduction (2-4 dB)

### Parallel Processing

**Concept**: Blend processed and unprocessed signals

**Applications**:
- Parallel compression (blend compressed and dry)
- Parallel reverb (blend wet and dry)
- Maintain natural sound while adding processing
- More control

**Technique**:
- Duplicate track or use aux send
- Process duplicate heavily
- Blend with original
- Adjust balance

### M/S Processing

**Concept**: Process mid (center) and side (stereo) independently

**Applications**:
- Widen or narrow stereo image
- Enhance center clarity
- Creative stereo effects
- Surround preparation

**Technique**:
- M/S encoder plugin
- Process mid and side separately
- Decode back to stereo
- Adjust balance

### Stem Mixing

**Concept**: Mix Foley to stems (submixes) before final mix

**Stems**:
- Feet stem
- Moves stem
- Specifics stem
- Or combined Foley stem

**Advantages**:
- Easier final mix adjustments
- Flexibility for re-versioning
- Organized workflow
- Industry standard for film

**Deliverables**:
- Individual stems
- Full Foley mix
- Documentation

## Troubleshooting

### Problem: Foley Sounds Disconnected

**Causes**:
- Poor sync
- Wrong reverb
- Inappropriate levels
- Tonal mismatch

**Solutions**:
- Re-check sync frame-by-frame
- Match reverb to scene
- Adjust levels in context
- EQ to match environment

### Problem: Foley Too Loud/Distracting

**Causes**:
- Levels too high
- Wrong sounds for scene
- Over-performance

**Solutions**:
- Reduce levels
- Duck under dialogue
- Re-record with subtler performance
- Remove unnecessary sounds

### Problem: Foley Too Quiet/Ineffective

**Causes**:
- Levels too low
- Masked by other elements
- Poor recording quality

**Solutions**:
- Increase levels
- EQ for clarity
- Compress for consistency
- Re-record if quality is poor

### Problem: Inconsistent Sound Across Scenes

**Causes**:
- Different props used
- Different reverb settings
- Different performance approach

**Solutions**:
- Use same props for same character/scene
- Save and reuse reverb settings
- Reference previous scenes
- Maintain consistency notes

### Problem: Sync Drift Over Time

**Causes**:
- Frame rate mismatch
- Sample rate mismatch
- Timecode issues

**Solutions**:
- Verify frame rate settings
- Check sample rate (audio and video)
- Re-sync from timecode
- Consult with editor

## Conclusion

Precise synchronization and thoughtful mixing are what transform recorded Foley sounds into seamless, immersive audio that enhances the viewing experience. By mastering frame-accurate sync, understanding the role of Foley in the overall mix, and applying appropriate processing and spatial placement, Foley editors and mixers ensure that every footstep, rustle, and impact feels natural and supports the story. The best Foley is invisible—perfectly synchronized, appropriately balanced, and completely integrated into the final soundtrack.