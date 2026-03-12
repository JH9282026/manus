### VTT (WebVTT - Web Video Text Tracks)

**Overview:**
- HTML5 native caption format
- Enhanced version of SRT
- Supports basic styling and positioning
- Designed for web delivery

**Structure:**
```
WEBVTT

00:00:01.000 --> 00:00:04.000
This is the first caption line.

00:00:04.500 --> 00:00:08.000 line:0 position:50%
<b>Speaker:</b> This is bold and positioned.
```

**Components:**
- "WEBVTT" header
- Timecode (start --> end)
- Optional cue settings (position, size, alignment)
- Caption text with optional HTML-like styling

**Supported By:** HTML5 video, YouTube, Facebook, most modern platforms

**Advantages Over SRT:**
- Positioning control
- Basic styling (bold, italic)
- Speaker identification formatting
- Voice/language tags
