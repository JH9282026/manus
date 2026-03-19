# Technical Workflow for Subtitling

Comprehensive guide to subtitling software, file formats, workflow automation, and technical best practices.

---

## Subtitling Software Ecosystem

### Desktop Applications

#### Subtitle Edit (Free, Open-Source)

**Overview**: Most popular free subtitling software, supports 200+ formats

**Key features**:
- Audio waveform visualization for precise timing
- Video preview with subtitle overlay
- Integrated Whisper AI for automatic transcription
- Comprehensive QA checks (reading speed, duration, gaps, formatting)
- Batch processing and format conversion
- Spell check and translation integration
- Subtitle synchronization tools

**Workflow**:
1. Import video file
2. Generate auto-transcription with Whisper (optional)
3. Create or import subtitle file
4. Use waveform to time subtitles precisely
5. Run QA checks
6. Export in desired format

**Best for**: General subtitling, format conversion, QA, budget-conscious projects

**Platform**: Windows (runs on Linux/Mac with Wine or Mono)

#### Aegisub (Free, Open-Source)

**Overview**: Advanced subtitling tool specializing in styling and effects

**Key features**:
- Advanced SubStation Alpha (ASS/SSA) format support
- Audio spectrum analyzer for precise timing
- Visual typesetting (position subtitles on video frame)
- Lua scripting for automation and effects
- Karaoke timing tools
- Extensive styling options (fonts, colors, animations)

**Workflow**:
1. Import video and audio
2. Create subtitles with timing using audio spectrum
3. Apply advanced styling and positioning
4. Use visual typesetting for precise placement
5. Export in ASS/SSA or convert to other formats

**Best for**: Anime subtitling, fansubbing, projects requiring complex visual effects

**Platform**: Windows, Mac, Linux

#### EZTitles (Commercial)

**Overview**: Professional broadcast-quality subtitling software

**Key features**:
- Support for all major broadcast formats (EBU-STL, SCC, etc.)
- Advanced spotting and timing tools
- Comprehensive QA suite with customizable rules
- Template-based workflow for consistency
- Integration with professional video editing systems
- Multi-user collaboration

**Workflow**:
1. Import video and template (if available)
2. Create or import subtitles
3. Use professional spotting tools for precise timing
4. Apply QA checks with broadcast standards
5. Export in broadcast-ready format

**Best for**: Professional broadcast subtitling, high-volume production, compliance-critical projects

**Platform**: Windows

**Pricing**: Commercial license (contact for pricing)

#### Subtitle Workshop (Free)

**Overview**: User-friendly subtitling tool for beginners

**Key features**:
- Simple, intuitive interface
- Real-time video preview
- Multiple format support
- Basic timing and synchronization tools
- Spell check and text formatting

**Best for**: Beginners, simple projects, quick edits

**Platform**: Windows

### Online Platforms

#### Amara (Web-Based)

**Overview**: Collaborative subtitling platform with accessibility focus

**Key features**:
- Browser-based, no installation required
- Collaborative and crowdsourced subtitling
- Integration with YouTube, Vimeo, and other platforms
- Multiple language support
- Accessibility-focused features
- Community-driven translation

**Workflow**:
1. Upload video or link to online video
2. Create subtitles in browser interface
3. Invite collaborators for translation or review
4. Publish subtitles to integrated platforms

**Best for**: Community projects, non-profit, educational content, crowdsourced translation

**Pricing**: Free for public projects, paid plans for private/commercial use

#### Kapwing (Web-Based)

**Overview**: Video editing platform with subtitle features

**Key features**:
- Auto-captioning with AI
- Subtitle styling templates for social media
- Video editing integration (trim, crop, effects)
- Burned-in subtitle export
- Collaboration features

**Workflow**:
1. Upload video
2. Generate auto-captions
3. Edit and style subtitles
4. Export video with burned-in subtitles or separate subtitle file

**Best for**: Social media content, marketing videos, quick projects

**Pricing**: Free tier with limitations, paid plans for more features

#### Typito (Web-Based)

**Overview**: Branded subtitle creation for marketing content

**Key features**:
- Branded subtitle templates
- Styling and animation options
- Video editing features
- Burned-in subtitle export
- Social media optimization

**Best for**: Marketing videos, promotional content, branded social media posts

**Pricing**: Subscription-based

### AI-Powered Transcription Services

#### Whisper (OpenAI)

**Overview**: State-of-the-art open-source speech recognition

**Key features**:
- Highly accurate transcription
- Multilingual support (99 languages)
- Automatic language detection
- Timestamp generation
- Free and open-source

**Integration**:
- Integrated into Subtitle Edit
- Can be run locally or via API
- Python library for custom workflows

**Workflow**:
1. Extract audio from video
2. Run Whisper transcription
3. Generate SRT or VTT file with timestamps
4. Import into subtitling software for refinement

**Limitations**:
- Requires technical setup for local use
- May struggle with heavy accents or poor audio quality
- Requires human review for accuracy

**Best for**: Initial transcription draft, high-volume projects, multilingual content

#### Sonix

**Overview**: Commercial AI transcription and subtitling service

**Key features**:
- Automated transcription and subtitling
- Speaker diarization (identifies different speakers)
- SDH generation (with human review)
- Multi-language support
- Browser-based editor
- Export in multiple formats

**Workflow**:
1. Upload video or audio
2. AI generates transcription with timestamps
3. Edit in browser interface
4. Add SDH elements (sound effects, speaker IDs)
5. Export subtitle file

**Best for**: Professional projects requiring fast turnaround, SDH creation

**Pricing**: Pay-per-minute of audio/video

#### Rev.com

**Overview**: Human transcription and captioning service

**Key features**:
- Human transcription (99% accuracy)
- Professional captioning and subtitling
- SDH and closed captioning
- Fast turnaround (typically 24 hours)
- Quality guarantee

**Workflow**:
1. Upload video
2. Select service (transcription, captions, subtitles)
3. Receive completed file
4. Review and request revisions if needed

**Best for**: High-accuracy requirements, professional projects, when time is available for human service

**Pricing**: Per-minute of audio/video (higher than AI services)

## File Format Deep Dive

### SRT (SubRip Text)

**Technical specifications**:
- Plain text file, UTF-8 encoding recommended
- File extension: `.srt`
- Structure: Sequential numbered blocks

**Block structure**:
```
[sequence number]
[start time] --> [end time]
[subtitle text line 1]
[subtitle text line 2]
[blank line]
```

**Timecode format**: `HH:MM:SS,mmm` (comma as decimal separator)

**Example**:
```
1
00:00:10,500 --> 00:00:13,000
First subtitle line
Second subtitle line

2
00:00:15,000 --> 00:00:18,000
Next subtitle
```

**Unofficial formatting** (supported by many players):
- `<b>bold</b>`
- `<i>italic</i>`
- `<u>underline</u>`
- `<font color="#RRGGBB">colored text</font>`

**Positioning** (unofficial, limited support):
- `{\an8}` - top center
- `{\an2}` - bottom center (default)

**Advantages**:
- Universal compatibility
- Easy to create and edit manually
- Small file size
- Human-readable

**Limitations**:
- No official styling standard
- Limited positioning control
- No metadata support

**Best for**: YouTube, Facebook, general web video, most media players

### WebVTT (Web Video Text Tracks)

**Technical specifications**:
- W3C standard for HTML5 `<track>` element
- UTF-8 encoding required
- File extension: `.vtt`
- Must begin with `WEBVTT` header

**Structure**:
```
WEBVTT

00:00:10.500 --> 00:00:13.000
First subtitle line
Second subtitle line

00:00:15.000 --> 00:00:18.000 align:start position:10%
Next subtitle with positioning
```

**Timecode format**: `HH:MM:SS.mmm` (period as decimal separator)

**Cue settings**:
- `align:start|middle|end` - horizontal alignment
- `position:X%` - horizontal position (0-100%)
- `line:X%` - vertical position
- `size:X%` - width of cue box

**Styling**:
- `<b>bold</b>`
- `<i>italic</i>`
- `<u>underline</u>`
- `<c.classname>styled text</c>` - CSS class styling

**CSS styling**:
```
WEBVTT

STYLE
::cue {
  background-color: rgba(0,0,0,0.8);
  color: white;
  font-family: Arial, sans-serif;
}

00:00:10.500 --> 00:00:13.000
Subtitle text
```

**Advantages**:
- Official W3C standard
- Advanced styling and positioning
- CSS integration
- Metadata support

**Limitations**:
- More complex than SRT
- Not all players support advanced features

**Best for**: HTML5 video, web streaming, Vimeo, modern platforms

### TTML/DFXP (Timed Text Markup Language)

**Technical specifications**:
- W3C standard, XML-based
- File extension: `.ttml`, `.dfxp`, `.xml`
- UTF-8 encoding

**Structure** (simplified):
```xml
<?xml version="1.0" encoding="UTF-8"?>
<tt xmlns="http://www.w3.org/ns/ttml" xml:lang="en">
  <head>
    <styling>
      <style xml:id="defaultStyle" tts:fontFamily="Arial" tts:fontSize="100%" tts:color="white"/>
    </styling>
  </head>
  <body>
    <div>
      <p begin="00:00:10.500" end="00:00:13.000" style="defaultStyle">
        First subtitle line<br/>Second subtitle line
      </p>
      <p begin="00:00:15.000" end="00:00:18.000" style="defaultStyle">
        Next subtitle
      </p>
    </div>
  </body>
</tt>
```

**Timecode formats**:
- `HH:MM:SS.mmm` (milliseconds)
- `HH:MM:SS:FF` (frames)

**Styling capabilities**:
- Font family, size, weight, style
- Color (text and background)
- Position and alignment
- Opacity and visibility
- Text decoration and effects

**Advantages**:
- Comprehensive styling
- Metadata support
- Multiple language tracks in single file
- Extensible (XML-based)

**Limitations**:
- Complex structure
- Not human-readable/editable
- Larger file size
- Requires specialized tools

**Best for**: Netflix, professional streaming platforms, broadcast

### SCC (Scenarist Closed Captions)

**Technical specifications**:
- Based on CEA-608 broadcast standard
- File extension: `.scc`
- Hexadecimal encoding
- Frame rate: 29.97 fps (NTSC) only

**Structure**:
```
Scenarist_SCC V1.0

00:00:10:15	94ae 94ad 9420 4920 6c6f 7665 2073 7562 7469 746c 6573 942c 942f

00:00:15:00	94ae 94ad 9420 5468 6579 2061 7265 2061 6d61 7a69 6e67 942c 942f
```

**Characteristics**:
- Two-byte hexadecimal codes represent characters and commands
- Limited character set (Latin alphabet, basic punctuation)
- Line length: 37 characters maximum
- Supports positioning and basic styling

**Advantages**:
- Broadcast standard in North America
- Precise frame-accurate timing
- Supported by professional video editing software

**Limitations**:
- Not human-readable
- Limited to 29.97 fps
- Limited character set (no Unicode)
- Requires specialized software to create/edit

**Best for**: Broadcast television (US), DVD, Adobe Premiere, Final Cut Pro

### Format Conversion

**Tools**:
- Subtitle Edit: Supports 200+ formats, batch conversion
- FFmpeg: Command-line tool for format conversion
- Online converters: SubtitleTools.com, GoTranscript

**Considerations**:
- Formatting may be lost in conversion (italics, colors, positioning)
- Timecode format differences (comma vs. period, frames vs. milliseconds)
- Character encoding (always use UTF-8 when possible)
- Validate output after conversion

## Workflow Automation

### Batch Processing

**Use cases**:
- Converting multiple files to different format
- Applying consistent styling across episodes
- Synchronizing subtitles with adjusted video timing
- Running QA checks on multiple files

**Tools**:
- Subtitle Edit: Batch convert, batch fix common errors
- FFmpeg: Command-line batch processing
- Python scripts: Custom automation with libraries like `pysrt`, `webvtt-py`

**Example workflow** (Subtitle Edit):
1. Load multiple subtitle files
2. Select batch operation (convert format, fix common errors, adjust timing)
3. Configure settings
4. Execute batch operation
5. Review results

### API Integration

**Transcription APIs**:
- OpenAI Whisper API
- Google Cloud Speech-to-Text
- Amazon Transcribe
- Microsoft Azure Speech Services

**Translation APIs**:
- Google Cloud Translation
- Microsoft Azure Translator
- DeepL API
- Amazon Translate

**Workflow example** (automated transcription and translation):
1. Upload video to cloud storage
2. Trigger transcription API
3. Receive transcript with timestamps
4. Convert to subtitle format (SRT/VTT)
5. Send to translation API for target languages
6. Generate translated subtitle files
7. Human review and refinement

### Python Scripting

**Libraries**:
- `pysrt`: Parse and manipulate SRT files
- `webvtt-py`: Parse and manipulate WebVTT files
- `pycaption`: Multi-format subtitle library
- `ffmpeg-python`: Python wrapper for FFmpeg

**Example script** (adjust subtitle timing):
```python
import pysrt

# Load subtitle file
subs = pysrt.open('input.srt')

# Shift all subtitles by 2 seconds
subs.shift(seconds=2)

# Save adjusted file
subs.save('output.srt', encoding='utf-8')
```

**Example script** (validate reading speed):
```python
import pysrt

def check_reading_speed(subtitle_file, max_cps=17):
    subs = pysrt.open(subtitle_file)
    violations = []
    
    for sub in subs:
        duration = (sub.end - sub.start).total_seconds()
        characters = len(sub.text_without_tags)
        cps = characters / duration if duration > 0 else 0
        
        if cps > max_cps:
            violations.append({
                'index': sub.index,
                'cps': cps,
                'text': sub.text
            })
    
    return violations

violations = check_reading_speed('subtitles.srt')
for v in violations:
    print(f"Subtitle {v['index']}: {v['cps']:.1f} CPS - {v['text']}")
```

## Quality Assurance Automation

### Automated QA Checks

**Reading speed**:
- Calculate CPS for each subtitle
- Flag subtitles exceeding threshold (17-20 CPS)
- Report average and maximum CPS

**Duration**:
- Check minimum duration (1 second)
- Check maximum duration (7 seconds)
- Flag violations

**Gaps**:
- Verify minimum gap between subtitles (2 frames)
- Identify overlapping subtitles
- Check for excessive gaps (may indicate missing subtitles)

**Line length**:
- Check characters per line (42-47 maximum)
- Verify maximum two lines per subtitle
- Flag single-word lines (orphans)

**Formatting**:
- Verify proper line breaks (not mid-word)
- Check for double spaces
- Validate punctuation (no double periods, etc.)
- Ensure proper capitalization

**Synchronization**:
- Check for subtitles starting before video begins
- Check for subtitles extending beyond video end
- Verify chronological order (no time overlaps)

**Encoding**:
- Verify UTF-8 encoding
- Check for unsupported characters
- Validate file structure (proper format syntax)

### QA Tools

**Subtitle Edit QA features**:
- Fix common errors (batch operation)
- Check reading speed
- Verify duration and gaps
- Spell check
- Style consistency check

**EZTitles QA suite**:
- Comprehensive rule-based checks
- Customizable QA profiles
- Detailed error reports
- Batch QA for multiple files

**Custom QA scripts**:
- Python scripts for project-specific checks
- Integration with CI/CD pipelines
- Automated reporting

### Platform-Specific Validation

**Netflix**:
- Netflix Timed Text Style Guide validator
- Checks compliance with Netflix standards
- Validates TTML structure and metadata

**YouTube**:
- Automatic validation on upload
- Flags formatting issues
- Provides error messages for corrections

**Broadcast**:
- Compliance with FCC regulations (US)
- EBU standards validation (Europe)
- Frame-accurate timing verification

---

## Summary

Effective subtitling workflows combine appropriate software tools, proper file format selection, automation where beneficial, and rigorous quality assurance. Understanding the technical aspects—from software capabilities to file format specifications to automated QA—enables subtitlers to work efficiently while maintaining high quality. Whether using free tools like Subtitle Edit for general projects or professional software like EZTitles for broadcast work, mastering the technical workflow is essential for professional subtitling.
