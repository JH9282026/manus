---
name: video-analysis-&-visual-intelligence
description: "The Video Analysis & Visual Intelligence skill equips Manus.im AI agents with comprehensive capabilities to process, understand, and manipulate video content at a level approaching human visual perception."
---

---
name: Video Analysis & Visual Intelligence
description: A comprehensive video analysis skill enabling AI agents to perceive, understand, and manipulate video content with human-like visual comprehension—extracting meaning, tracking objects across frames, detecting emotions over time, understanding narrative structure, and performing sophisticated video manipulation tasks.
version: 1.0.0
category: multimedia-intelligence
complexity: advanced
execution_mode: autonomous
---

# Video Analysis & Visual Intelligence

## 1. Skill Description and Purpose

### Overview

The Video Analysis & Visual Intelligence skill equips Manus.im AI agents with comprehensive capabilities to process, understand, and manipulate video content at a level approaching human visual perception. This skill transforms raw video data into structured, actionable intelligence while enabling sophisticated video manipulation operations.

### Core Competencies

This skill encompasses four fundamental pillars of video intelligence:

**Perceptual Understanding**: The ability to "see" video content as humans do—recognizing objects, people, scenes, actions, and their relationships across temporal sequences. This includes understanding visual context, spatial relationships, and the semantic meaning of visual elements.

**Temporal Intelligence**: Understanding how video unfolds over time—tracking changes, detecting events, recognizing narrative structure, and comprehending cause-and-effect relationships across frames. This temporal awareness distinguishes video analysis from static image processing.

**Emotional & Sentiment Analysis**: Detecting and tracking emotional content within videos—facial expressions, body language, vocal tone, atmospheric mood, and overall sentiment. This enables understanding of human emotional states and predicting audience emotional responses.

**Manipulation & Composition**: Extracting, isolating, and compositing video elements—removing objects, inserting new elements, creating seamless compositions, and performing professional-grade video editing operations programmatically.

### Why This Skill Is Valuable

Video has become the dominant medium for communication, entertainment, education, and marketing. This skill enables AI agents to:

- **Automate Content Analysis**: Process hours of video in minutes, extracting insights that would take humans days to compile manually
- **Enable Intelligent Content Creation**: Automatically identify the best moments, extract relevant clips, and create optimized content for different platforms
- **Support Decision Making**: Provide structured data from unstructured video content for business intelligence, marketing analysis, and research
- **Perform Complex Video Operations**: Execute sophisticated editing and composition tasks that traditionally require expert human operators
- **Ensure Accessibility**: Generate captions, descriptions, and alternative formats for inclusive content delivery

### When to Deploy This Skill

Activate this skill when tasks require:

- Understanding what happens within video content (people, objects, actions, events)
- Tracking elements across multiple frames or scenes
- Extracting emotional or sentiment data from video sources
- Isolating and extracting specific objects or scenes from videos
- Compositing video elements into new productions
- Generating video summaries, highlights, or optimized clips
- Analyzing video for quality, engagement potential, or technical specifications
- Creating accessible versions of video content

---

## 2. Required Inputs/Parameters

### Primary Video Input

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `video_source` | string/file | Yes | Video file path, URL, or streaming endpoint. Supported formats: MP4, MOV, AVI, MKV, WebM, FLV, WMV, MPEG, 3GP |
| `video_resolution` | string | No | Expected resolution (e.g., "1080p", "4K", "720p"). Auto-detected if not specified |
| `frame_rate` | integer | No | Frames per second. Auto-detected if not specified |
| `duration_limit` | integer | No | Maximum seconds to process. Processes entire video if not specified |
| `start_timestamp` | string | No | Processing start point in HH:MM:SS format |
| `end_timestamp` | string | No | Processing end point in HH:MM:SS format |

### Analysis Configuration

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `analysis_modes` | array | Yes | List of analysis types to perform. Options: `scene_detection`, `object_tracking`, `face_analysis`, `emotion_detection`, `action_recognition`, `speech_transcription`, `audio_analysis`, `narrative_analysis`, `quality_assessment`, `content_categorization` |
| `confidence_threshold` | float | No | Minimum confidence score (0.0-1.0) for detections. Default: 0.7 |
| `sampling_rate` | integer | No | Analyze every Nth frame for efficiency. Default: 1 (every frame) |
| `tracking_persistence` | boolean | No | Maintain object IDs across occlusions. Default: true |
| `multi_language_support` | array | No | Languages for speech recognition. Default: ["en"] |

### Object Detection & Tracking Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `target_objects` | array | No | Specific objects to detect/track (e.g., ["golf clubs", "tennis racket", "person", "car"]). Detects all objects if not specified |
| `object_categories` | array | No | Object categories: `people`, `vehicles`, `animals`, `sports_equipment`, `consumer_goods`, `furniture`, `natural_elements`, `tools` |
| `tracking_algorithm` | string | No | Tracking method: `deep_sort`, `byte_track`, `centroid`, `kalman`. Default: `deep_sort` |
| `bounding_box_format` | string | No | Output format: `xyxy`, `xywh`, `normalized`. Default: `xyxy` |
| `generate_trajectories` | boolean | No | Create movement path data. Default: true |

### Extraction & Manipulation Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `extraction_targets` | array | No | Objects/scenes to extract (e.g., ["golf clubs in frames 100-500", "person with red shirt"]) |
| `extraction_method` | string | No | Technique: `ai_rotoscoping`, `chroma_key`, `luma_key`, `depth_segmentation`, `motion_segmentation`. Default: `ai_rotoscoping` |
| `output_format` | string | No | Extraction output: `video_clip`, `image_sequence`, `transparent_video`, `mask_sequence`. Default: `transparent_video` |
| `preserve_audio` | boolean | No | Include audio in extractions. Default: true |
| `background_replacement` | string | No | New background for extracted elements (color hex, image path, or video path) |

### Composition Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `composition_target` | string | No | Destination video for insertions |
| `insertion_elements` | array | No | Elements to insert with positioning data |
| `match_lighting` | boolean | No | Auto-adjust lighting to match target. Default: true |
| `match_color_grade` | boolean | No | Match color grading of target. Default: true |
| `add_shadows` | boolean | No | Generate realistic shadows. Default: true |
| `motion_blur` | boolean | No | Add motion blur for realism. Default: true |

### Output Configuration

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `output_directory` | string | Yes | Path for output files |
| `output_formats` | array | No | Desired outputs: `json_analysis`, `annotated_video`, `extracted_clips`, `timeline_visualization`, `report_document`. Default: [`json_analysis`] |
| `video_codec` | string | No | Output codec: `h264`, `h265`, `vp9`, `prores`. Default: `h264` |
| `quality_preset` | string | No | Quality level: `draft`, `standard`, `high`, `lossless`. Default: `standard` |

---

## 3. Expected Outputs/Deliverables

### Structured Analysis Data (JSON)

The primary output is a comprehensive JSON document containing:

**Video Metadata Block**:
```json
{
  "video_metadata": {
    "duration_seconds": 145.5,
    "resolution": "1920x1080",
    "frame_rate": 29.97,
    "total_frames": 4362,
    "codec": "h264",
    "bitrate_kbps": 8500,
    "aspect_ratio": "16:9",
    "color_space": "bt709",
    "audio_tracks": 1,
    "file_size_mb": 156.2
  }
}
```

**Scene Detection Results**:
- Scene boundaries with frame numbers and timestamps
- Scene classifications (indoor/outdoor, day/night, location type)
- Scene importance scores (0.0-1.0)
- Transition types between scenes (cut, fade, dissolve, wipe)
- Key frame selections per scene
- Scene clustering data for similar scenes

**Object Detection & Tracking Data**:
- Frame-by-frame object detections with bounding boxes
- Unique object IDs persisting across frames
- Object classification labels with confidence scores
- Movement trajectories (x, y coordinates over time)
- Speed and direction vectors
- Entry/exit frame numbers
- Occlusion events and recovery points
- Object state changes (e.g., "door: closed → open")

**Face Analysis Results**:
- Face detections with bounding boxes per frame
- Facial landmark positions (68-point or 468-point mesh)
- Face tracking IDs for identity consistency
- Expression classifications with confidence scores
- Gaze direction vectors
- Head pose (pitch, yaw, roll)
- Estimated demographics (age range, gender)
- Screen time per identified face
- Face clustering for same-person grouping

**Emotion & Sentiment Data**:
- Per-frame emotion classifications (happiness, sadness, anger, fear, surprise, disgust, neutral)
- Emotion intensity scores (0.0-1.0)
- Emotional arc timeline showing mood progression
- Scene-level atmosphere classifications
- Aggregate sentiment scores (positive/negative/neutral)
- Emotional peak and valley timestamps
- Predicted audience emotional response

**Action Recognition Results**:
- Detected actions with frame ranges
- Action classifications (walking, running, jumping, gesturing, sports actions)
- Body pose estimations (17-point or 33-point skeleton)
- Interaction events (person-person, person-object)
- Action intensity and confidence scores

**Speech & Audio Analysis**:
- Full transcription with word-level timestamps
- Speaker diarization (who spoke when)
- Speaker identification labels
- Audio sentiment per speaker
- Music detection with genre/mood classification
- Sound effect identifications
- Volume dynamics and silence detection
- Audio quality assessment

**Narrative & Content Analysis**:
- Video structure (intro, main content, outro timestamps)
- Story arc identification
- Key moments and highlights with timestamps
- Topic and subject classifications
- Content category (tutorial, vlog, commercial, documentary, etc.)
- Target audience assessment
- Engagement prediction scores
- SEO recommendations (titles, tags, descriptions)

### Annotated Video Output

When requested, produces a video overlay containing:
- Bounding boxes around detected objects with labels
- Face detection boxes with emotion indicators
- Action recognition labels
- Scene boundary markers
- Emotion timeline overlay
- Tracking trajectories visualized
- Timestamp and frame number display

### Extracted Video Elements

For extraction operations:
- **Transparent Video Files**: WebM or MOV with alpha channel containing isolated objects
- **Image Sequences**: PNG sequences with transparency for frame-by-frame elements
- **Mask Sequences**: Grayscale mask videos for compositing workflows
- **Clip Extractions**: Isolated scenes or segments as standalone video files
- **Audio Extractions**: Separated audio tracks when applicable

### Composition Outputs

For manipulation operations:
- **Composited Video**: Final output with inserted elements seamlessly integrated
- **Layer Documentation**: JSON describing all composition layers and their properties
- **Before/After Comparisons**: Side-by-side or sequential comparison outputs
- **Project Files**: Compatible formats for editing software when possible

### Analysis Reports

Formatted documents including:
- Executive summary of video content
- Visual timeline with key moments marked
- Statistical breakdowns (screen time, emotion distribution, object frequency)
- Thumbnail recommendations
- Platform-specific optimization suggestions
- Accessibility compliance assessment

### Quality Standards

All outputs adhere to:
- Minimum 95% accuracy for object detection on standard benchmarks
- Frame-accurate timestamp synchronization (±1 frame tolerance)
- Consistent object ID persistence across 85%+ of tracking scenarios
- Sub-second latency for real-time streaming analysis
- Lossless quality preservation for extracted elements
- Industry-standard codec compliance for video outputs

---

## 4. Example Use Cases

### Use Case 1: Golf Club Extraction for E-Commerce Website

**Scenario**: A golf equipment retailer needs to extract golf clubs from instructional swing videos to create product showcase content with transparent backgrounds.

**Execution Flow**:

1. **Input Configuration**:
   - Video source: Professional golf swing demonstration video
   - Target objects: ["golf club", "golf driver", "golf iron", "putter"]
   - Extraction method: `ai_rotoscoping`
   - Output format: `transparent_video`

2. **Processing Steps**:
   - Analyze video to detect all frames containing golf clubs
   - Track club position throughout swing motion
   - Generate precise segmentation masks for club isolation
   - Apply edge refinement for clean separation from hands and background
   - Preserve motion blur for natural appearance
   - Export as WebM with alpha channel

3. **Output Deliverables**:
   - Transparent video of isolated golf club throughout swing
   - Frame-by-frame PNG sequence for still images
   - JSON metadata with club position coordinates per frame
   - Recommended thumbnail frames showing club clearly

4. **Composition Application**:
   - Insert extracted club into product showcase template
   - Match lighting to studio environment
   - Add subtle shadow generation
   - Export final product video

### Use Case 2: Emotional Journey Analysis for Film Production

**Scenario**: A documentary filmmaker needs to analyze audience emotional response patterns in rough cut footage to optimize narrative pacing.

**Execution Flow**:

1. **Input Configuration**:
   - Analysis modes: [`face_analysis`, `emotion_detection`, `narrative_analysis`, `audio_analysis`]
   - Confidence threshold: 0.75
   - Multi-language support: ["en", "es"]

2. **Analysis Outputs**:
   - Emotional arc visualization showing sentiment progression
   - Per-subject emotion tracking for interview segments
   - Identification of emotional peaks and valleys
   - Pacing analysis with scene duration recommendations
   - Voice emotion correlation with facial expressions

3. **Actionable Insights**:
   - Timestamps where emotional impact drops
   - Recommended cuts to maintain engagement
   - Scene reordering suggestions based on emotional flow
   - Music placement recommendations aligned with emotional beats

### Use Case 3: Sports Performance Analysis

**Scenario**: A tennis academy needs to analyze player technique across multiple training session videos.

**Execution Flow**:

1. **Input Configuration**:
   - Target objects: ["tennis racket", "tennis ball", "player"]
   - Analysis modes: [`object_tracking`, `action_recognition`, `face_analysis`]
   - Tracking algorithm: `deep_sort`
   - Generate trajectories: true

2. **Processing**:
   - Track racket position and angle throughout swings
   - Detect and classify action types (serve, forehand, backhand, volley)
   - Analyze body pose during each stroke
   - Calculate ball speed and trajectory
   - Identify technique patterns and anomalies

3. **Outputs**:
   - Stroke-by-stroke breakdown with timestamps
   - Movement trajectory visualizations
   - Comparison data against reference technique models
   - Highlight clips of best and worst executions
   - Statistical performance summary

### Use Case 4: Marketing Video Optimization

**Scenario**: A marketing team needs to analyze competitor video ads to understand effective techniques and optimize their own content.

**Execution Flow**:

1. **Input Configuration**:
   - Analysis modes: [`scene_detection`, `emotion_detection`, `content_categorization`, `speech_transcription`, `quality_assessment`]
   - Output formats: [`json_analysis`, `report_document`, `timeline_visualization`]

2. **Analysis Deliverables**:
   - Scene-by-scene breakdown with effectiveness scores
   - Brand mention frequency and placement
   - Call-to-action timing and prominence
   - Emotional engagement prediction
   - Pacing comparison against industry benchmarks
   - Thumbnail A/B testing recommendations

3. **Optimization Recommendations**:
   - Ideal video length for target platform
   - Optimal hook placement (first 3 seconds analysis)
   - Scene reordering for maximum retention
   - Audio mixing suggestions
   - Caption and accessibility requirements

### Use Case 5: Automated Content Moderation

**Scenario**: A video platform needs to automatically screen uploaded content for policy violations.

**Execution Flow**:

1. **Real-time Analysis**:
   - Object detection for prohibited items
   - Face analysis for age verification contexts
   - Audio analysis for inappropriate language
   - Action recognition for violent or dangerous activities
   - Text detection in video frames

2. **Flagging System**:
   - Confidence-scored violation alerts
   - Timestamp markers for human review
   - Category classification for violation type
   - Automatic blur/mute suggestions
   - Appeal-ready evidence documentation

---


## Extended Content

For additional detailed content, examples, and resources, see:
- [Extended Content](references/detailed-content.md)

## Using the Reference Files

- [Detailed Content](./references/detailed-content.md): Detailed Content

