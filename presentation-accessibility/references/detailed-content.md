# Presentation Accessibility - Detailed Reference

## Alternative Text for Images and Graphics

### Writing Effective Alt Text

Alternative text (alt text) provides text descriptions of visual content for users who cannot see images. Effective alt text should be:

**Concise**: Typically 125 characters or fewer. Longer descriptions should use extended description features.

**Descriptive**: Convey the essential information the image provides.

**Contextual**: Consider why the image is included and what information it conveys in context.

**Functional**: For buttons or links, describe the action, not the appearance.

### Alt Text Examples

**Informative Images**:
- Poor: "Chart"
- Better: "Bar chart showing Q3 sales by region"
- Best: "Bar chart showing Q3 sales: North $2.1M, South $1.8M, East $2.4M, West $1.5M"

**Functional Images**:
- Poor: "Button"
- Better: "Next slide"
- Best: "Go to next slide"

**Complex Images**:
- Poor: "Organizational chart"
- Better: "Company organizational chart with CEO at top and three divisions below"
- Best: Provide brief alt text plus extended description in notes or appendix

### When to Use Alt Text

**Always Provide Alt Text For**:
- Photographs and illustrations conveying information
- Charts, graphs, and data visualizations
- Diagrams and flowcharts
- Icons with meaning
- Screenshots demonstrating features
- Logos (first occurrence)

**Mark as Decorative**:
- Background patterns or textures
- Decorative borders or dividers
- Purely aesthetic images
- Repeated logos (after first occurrence)
- Stock photos used only for visual interest

### Decorative vs. Informative Images

**Decorative Images**: Serve no informational purpose and should be marked as decorative (empty alt text or decorative flag). Screen readers skip these images.

**Informative Images**: Convey information necessary for understanding the content. These require descriptive alt text.

**Test Question**: If the image were removed, would any information be lost? If yes, it's informative and needs alt text.

---

## Document Structure and Reading Order

### Proper Heading Hierarchy

Headings create the structural outline of a presentation and enable navigation:

**Heading Level Rules**:
- Use Heading 1 for slide titles
- Use Heading 2-6 for content hierarchy
- Never skip heading levels (H1 to H3 without H2)
- Use headings for structure, not styling

**Benefits of Proper Headings**:
- Screen readers announce heading levels
- Users can navigate by heading
- Creates logical content outline
- Improves SEO for web-based presentations

### Logical Reading Order

Reading order determines the sequence in which content is read by screen readers and keyboard navigation:

**Setting Reading Order**:
- Use built-in layouts that establish correct order
- Review and adjust reading order in accessibility tools
- Test with screen readers to verify order

**Reading Order Principles**:
- Title first, then content
- Left to right, top to bottom (for LTR languages)
- Group related elements together
- Place navigation and controls consistently

### Using Built-in Layouts

**Why Built-in Layouts Matter**:
- Automatically establish correct reading order
- Include proper heading structure
- Maintain consistent formatting
- Optimize for accessibility features

**Custom Layout Considerations**:
- Always verify reading order after customization
- Maintain heading hierarchy
- Test with accessibility checkers
- Document reading order for complex slides

---

## Screen Reader Compatibility

### How Screen Readers Work with Presentations

Screen readers are assistive technologies that convert on-screen content to speech or braille output. When encountering presentations:

**Navigation Methods**:
- Moving slide by slide
- Navigating by headings
- Reading content in order
- Accessing slide notes
- Navigating tables cell by cell

**Information Announced**:
- Slide numbers and titles
- Text content in reading order
- Image alt text
- Table structure and headers
- Link destinations

### Testing with Screen Readers

**Common Screen Readers**:
- JAWS (Windows, commercial)
- NVDA (Windows, free)
- VoiceOver (Mac/iOS, built-in)
- Narrator (Windows, built-in)
- TalkBack (Android, built-in)

**Basic Testing Process**:
1. Enable screen reader
2. Open presentation
3. Navigate through all slides
4. Verify all content is announced
5. Test navigation methods
6. Check alt text is read correctly
7. Verify reading order makes sense

### Platform-Specific Considerations

**PowerPoint**:
- Excellent screen reader support
- Built-in accessibility checker
- Selection pane for reading order
- Supports JAWS, NVDA, Narrator

**Google Slides**:
- Good ChromeVox support
- Limited screen reader support in edit mode
- Better support in presentation mode
- Accessibility features in development

**Keynote**:
- Strong VoiceOver support on Mac
- Limited support on other platforms
- Accessibility inspector available
- Export to accessible formats

---

## Accessible Tables and Data Visualization

### Accessible Table Design

**Table Structure**:
- Define header rows and columns
- Use simple table structures (avoid merged cells)
- Include table summaries for complex tables
- Keep tables as simple as possible

**Table Best Practices**:
- One header row maximum
- Avoid nested tables
- Use table headers, not bold text
- Include caption or title
- Consider alternative formats for complex data

**Table Header Designation**:
Screen readers use table headers to provide context when navigating cells. Without proper headers, users hear only cell values without understanding what they represent.

In PowerPoint: Use the Table Design tab to specify header rows.
In Google Slides: Limited table accessibility features; consider alternative formats.
In Keynote: Use simple table structures with clear visual headers.

**Complex Table Alternatives**:
When data requires complex table structures, consider:
- Breaking into multiple simple tables
- Providing data as an appendix document
- Creating accessible Excel versions
- Using data visualization with extended descriptions

### Accessible Charts and Graphs

**Making Charts Accessible**:
- Provide detailed alt text or extended descriptions
- Include data tables as alternatives
- Use patterns and textures with colors
- Add direct labels on data points
- Include legends with text descriptions

**Chart Alt Text Guidelines**:
Alt text for charts should include:
1. Chart type (bar chart, line graph, pie chart)
2. What the chart measures
3. Key data points or trends
4. Source of data (if relevant)
5. Time period covered

**Example Chart Alt Text**:
"Line graph showing company revenue from 2020-2025. Revenue increased steadily from $2.1M in 2020 to $5.8M in 2025, with the steepest growth between 2023-2024. Data source: Annual financial reports."

**Data Visualization Alternatives**:
- Provide raw data in accessible table format
- Include text summaries of key findings
- Offer downloadable data files
- Consider interactive accessible versions

**Pattern Usage in Charts**:
When using patterns with colors:
- Use high-contrast patterns (dots, stripes, crosshatch)
- Ensure patterns are distinguishable in grayscale
- Maintain sufficient pattern density for visibility
- Test with color blindness simulators

---

## Animation and Motion Accessibility

### Motion Sensitivity

Some users experience discomfort, dizziness, or seizures from certain types of motion:

**Problematic Motion Types**:
- Parallax scrolling effects
- Spinning or rotating animations
- Rapid zooming
- Flashing content (more than 3 flashes per second)
- Auto-playing video with motion

**Seizure Risk**: Content flashing more than 3 times per second, especially in red, can trigger photosensitive epilepsy seizures.

### Providing Controls

**User Control Options**:
- Allow users to pause or stop animations
- Provide options to reduce motion
- Enable manual slide advancement
- Offer static alternatives

### Alternatives to Animation

**Static Alternatives**:
- Use sequential slides instead of animations
- Provide printed handouts
- Create PDF versions without animation
- Use simple fade transitions instead of motion

**Accessible Animation When Used**:
- Keep animations subtle and brief
- Use fade or dissolve rather than motion
- Avoid continuous or looping animations
- Test with prefers-reduced-motion settings

---

## Multimedia Accessibility

### Captions and Subtitles for Videos

**Captions vs. Subtitles**:
- Captions: Include dialogue plus sound effects, speaker identification, and music descriptions
- Subtitles: Translate dialogue only, assuming viewer can hear other audio

**Caption Requirements**:
- Synchronized with audio
- Complete and accurate
- Properly positioned (not obscuring content)
- Readable font size and contrast
- Include speaker identification when multiple speakers

**Caption Types**:
- Closed captions: User can toggle on/off
- Open captions: Burned into video, always visible
- Live captions: Generated in real-time (less accurate)

### Audio Descriptions

Audio descriptions provide narration of visual elements during natural pauses in dialogue:

**When Audio Descriptions Are Needed**:
- Videos with important visual information not conveyed in dialogue
- Demonstrations and tutorials
- Visual storytelling elements
- On-screen text or graphics

**Creating Audio Descriptions**:
- Identify key visual information
- Write concise descriptions
- Record narration to fit between dialogue
- Time descriptions carefully

### Transcripts

Transcripts provide text versions of all audio and visual content:

**Transcript Contents**:
- Complete dialogue
- Speaker identification
- Sound effects descriptions
- Visual descriptions
- Relevant timing information

**Transcript Benefits**:
- Accessible to deaf and hard of hearing users
- Searchable and indexable
- Usable with braille displays
- Available for offline reference

---

## Keyboard Navigation and Focus Indicators

### Keyboard Accessibility

All interactive elements must be accessible via keyboard:

**Essential Keyboard Functions**:
- Tab: Move to next interactive element
- Shift+Tab: Move to previous interactive element
- Enter/Space: Activate buttons and links
- Arrow keys: Navigate within components
- Escape: Close dialogs or menus

### Focus Indicators

Focus indicators show which element currently has keyboard focus:

**Visible Focus Requirements**:
- Clear visual change when element has focus
- Sufficient contrast with background
- Not relying on color alone
- Consistent across all elements

**Focus Indicator Types**:
- Outline/border (most common)
- Background color change
- Underline (for links)
- Shadow or glow effects

---

## Accessible PDF Exports

### Creating Accessible PDFs from Presentations

**Export Settings**:
- Enable tagged PDF export
- Include document structure
- Preserve headings and lists
- Maintain reading order

**PDF Accessibility Requirements**:
- Document language specified
- Tagged structure (headings, lists, tables)
- Alternative text for images
- Logical reading order
- Bookmarks for navigation
- Accessible forms (if included)

### Testing PDF Accessibility

**Testing Tools**:
- Adobe Acrobat Pro Accessibility Checker
- PAC 3 (PDF Accessibility Checker)
- Common Look PDF Validator
- axe for PDFs

### PDF Remediation

When PDFs export with accessibility issues, remediation may be necessary:

**Common Remediation Tasks**:
- Adding or fixing tags
- Setting reading order
- Adding alt text to images
- Marking decorative elements
- Fixing table structure
- Adding bookmarks

**Remediation Tools**:
- Adobe Acrobat Pro
- CommonLook PDF GlobalAccess
- PDF Accessibility Checker (PAC)
- axe for PDF

**Prevention Over Remediation**: Creating accessible source documents is far more efficient than remediating inaccessible PDFs after export. Invest time in proper source document creation.

---

## Language and Plain Language Principles

### Plain Language Guidelines

**Writing for Accessibility**:
- Use simple, common words
- Keep sentences short (15-20 words average)
- Use active voice
- Define technical terms
- Avoid jargon and acronyms without explanation

**Plain Language Benefits**:
- Easier for non-native speakers
- Better for cognitive disabilities
- Improved comprehension for all audiences
- Faster processing and retention

### Document Language Settings

**Specifying Language**:
- Set document language in presentation software
- Mark language changes within content
- Use correct language for spell-checking
- Enable proper screen reader pronunciation

---

## Accessible Presentation Delivery

### Describing Visual Content Verbally

When presenting, describe visual elements for audience members who cannot see them:

**What to Describe**:
- Charts and graphs (key data points and trends)
- Images and photographs (relevant details)
- Diagrams and flowcharts (structure and relationships)
- On-screen demonstrations (actions being performed)

**Description Techniques**:
- "This bar chart shows..."
- "The diagram illustrates..."
- "On screen, you can see..."
- "The photograph depicts..."

### Providing Materials in Advance

**Advance Materials**:
- Share slides before the presentation
- Provide handouts in accessible formats
- Include transcripts or notes
- Allow time for pre-review

**Benefits of Advance Materials**:
- Users can follow along with assistive technology
- Time to process complex information
- Opportunity to prepare questions
- Reference during and after presentation

### Accommodating Questions

**Inclusive Q&A Practices**:
- Repeat questions before answering
- Provide multiple ways to ask questions (verbal, written, chat)
- Allow extra time for processing
- Offer follow-up via email for complex questions

### Live Presentation Accessibility

**Physical Space Considerations**:
- Ensure wheelchair accessibility to all areas
- Provide accessible seating with clear sightlines
- Position sign language interpreters appropriately
- Ensure adequate lighting for lip-reading
- Minimize background noise

**Real-Time Captioning**:
- CART (Communication Access Real-Time Translation) services
- AI-powered live captioning (Microsoft, Google, Zoom)
- Display captions prominently
- Test captioning technology beforehand

**Sign Language Interpretation**:
- Book interpreters in advance
- Brief interpreters on terminology
- Position interpreters where deaf audience can see both interpreter and presenter
- Provide materials to interpreters beforehand

### Virtual Presentation Accessibility

**Video Conference Accessibility**:
- Enable live captions when available
- Use speaker view for deaf participants reading lips
- Share slides directly (not just screen share)
- Record sessions for later access
- Provide chat alternatives for audio participation

**Accessible Screen Sharing**:
- Use high contrast slides
- Zoom in on small text
- Describe visual content being shared
- Pause for questions more frequently
- Monitor chat for accessibility requests

---

## Platform-Specific Accessibility Features

### PowerPoint Accessibility

**Built-in Accessibility Checker**:
- Review > Check Accessibility
- Identifies issues with suggestions
- Covers images, reading order, tables, contrast
- Provides detailed explanations

**Key Accessibility Features**:
- Alt text editor
- Selection pane for reading order
- Slide title checking
- Table header designation
- Automatic captions (PowerPoint 365)
- Accessibility templates

**Best Practices for PowerPoint**:
- Use built-in layouts
- Check accessibility before sharing
- Use Slide Master for consistency
- Export to accessible PDF

### Keynote Accessibility

**Accessibility Features**:
- VoiceOver compatibility
- Accessibility descriptions for media
- Accessibility inspector
- Export to accessible formats

**Keynote Limitations**:
- Less robust than PowerPoint for accessibility
- Limited accessibility checker
- Windows compatibility concerns
- Fewer accessibility-focused templates

### Google Slides Accessibility

**Accessibility Features**:
- Alt text for images
- Link to associated notes
- Screen reader support (ChromeVox)
- Automatic captions in presentations

**Google Slides Limitations**:
- No built-in accessibility checker
- Limited reading order control
- Fewer accessibility features than PowerPoint
- Third-party tools needed for comprehensive checking

---

## Testing for Accessibility

### Manual Testing Methods

**Keyboard Testing**:
1. Unplug or disable mouse
2. Navigate entire presentation using keyboard only
3. Verify all content is reachable
4. Check focus indicators are visible
5. Test all interactive elements

**Visual Testing**:
- Zoom to 200% and verify readability
- View in grayscale to check contrast
- Use color blindness simulators
- Test in various lighting conditions

**Screen Reader Testing**:
- Listen to entire presentation with screen reader
- Verify reading order makes sense
- Check alt text is appropriate
- Test navigation methods

### Automated Testing Tools

**Built-in Tools**:
- PowerPoint Accessibility Checker
- Adobe Acrobat Accessibility Checker
- Microsoft Accessibility Insights

**Third-Party Tools**:
- WAVE (for web-based presentations)
- axe (browser extension)
- Color Contrast Analyzer
- PAC 3 (for PDFs)

---

## Accessibility Checklist for Presentations

### Before Creating

- [ ] Understand audience accessibility needs
- [ ] Choose accessible template
- [ ] Plan logical structure
- [ ] Gather accessible media assets

### During Creation

- [ ] Use built-in layouts
- [ ] Add alt text to all images
- [ ] Check color contrast
- [ ] Use accessible fonts and sizes
- [ ] Create logical reading order
- [ ] Add captions to videos
- [ ] Use descriptive link text
- [ ] Structure tables properly

### Before Sharing

- [ ] Run accessibility checker
- [ ] Test with keyboard navigation
- [ ] Test with screen reader
- [ ] Review reading order
- [ ] Check exported formats

### During Delivery

- [ ] Describe visual content verbally
- [ ] Face audience when speaking
- [ ] Provide materials in advance
- [ ] Accommodate questions inclusively

---

## Best Practices for Accessible Presentations

### Design Best Practices

1. **Start with accessibility in mind** from the beginning of the design process
2. **Use high contrast** between text and backgrounds
3. **Choose readable fonts** at adequate sizes
4. **Limit text per slide** to essential information
5. **Use consistent layouts** throughout the presentation
6. **Provide alternative text** for all meaningful images
7. **Structure content logically** with clear headings
8. **Test with accessibility tools** throughout development

### Content Best Practices

9. **Write in plain language** accessible to all reading levels
10. **Use bulleted lists** for easier scanning
11. **Avoid walls of text** by breaking up content
12. **Provide multiple formats** (slides, handouts, transcripts)
13. **Include summaries** of key points
14. **Define acronyms and jargon** on first use
15. **Use inclusive language** throughout

### Technical Best Practices

16. **Use built-in slide layouts** for proper structure
17. **Set document language** correctly
18. **Create accessible PDFs** when exporting
19. **Test on multiple platforms** and devices
20. **Maintain accessibility when updating** presentations

---

## Common Accessibility Mistakes to Avoid

### Visual Design Mistakes

1. **Low color contrast**: Using light text on light backgrounds or insufficient contrast ratios
2. **Small font sizes**: Using fonts below 24 points for body text
3. **Relying on color alone**: Using only color to convey meaning without secondary indicators
4. **Busy backgrounds**: Using images or patterns that reduce text readability
5. **Decorative fonts**: Using script or novelty fonts that are difficult to read

### Content Mistakes

6. **Missing alt text**: Leaving images without alternative descriptions
7. **Vague link text**: Using "click here" instead of descriptive links
8. **Wall of text**: Overcrowding slides with too much text
9. **Missing slide titles**: Creating slides without descriptive titles
10. **Complex tables**: Using merged cells or nested tables unnecessarily

### Technical Mistakes

11. **Ignoring reading order**: Not checking or correcting reading order
12. **Skipping heading levels**: Jumping from H1 to H3 without H2
13. **Inaccessible PDFs**: Exporting without tagged structure
14. **Uncaptioned videos**: Including video content without captions
15. **Auto-playing media**: Using auto-play without user controls

### Delivery Mistakes

16. **Not describing visuals**: Failing to verbally describe on-screen content
17. **Talking too fast**: Not allowing time for processing
18. **Not repeating questions**: Answering questions without repeating them
19. **Last-minute materials**: Not providing materials in advance
20. **Single format only**: Not offering alternative formats

---

## Legal and Compliance Considerations

### United States

**Americans with Disabilities Act (ADA)**: Requires accessible communication in employment, public accommodations, and government services. Applies to presentations in most professional contexts.

**Section 508**: Federal agencies must ensure electronic and information technology is accessible. Applies to government presentations and contractors.

**Section 504**: Programs receiving federal funding must provide equal access to individuals with disabilities.

### International Standards

**European Union**: European Accessibility Act and Web Accessibility Directive require accessible digital content from public sector bodies.

**United Kingdom**: Equality Act 2010 requires reasonable accommodations for disabilities.

**Canada**: Accessibility for Ontarians with Disabilities Act (AODA) and Accessible Canada Act set accessibility requirements.

**Australia**: Disability Discrimination Act requires accessible services and information.

### Industry Standards

**WCAG**: Web Content Accessibility Guidelines serve as the de facto international standard, referenced by most legal requirements.

**ISO 30071**: International standard for digital accessibility processes.

**EN 301 549**: European standard for ICT accessibility requirements.

---

## Tools and Resources for Accessibility

### Accessibility Checkers

- **PowerPoint Accessibility Checker**: Built into Microsoft Office
- **Adobe Acrobat Accessibility Checker**: For PDF verification
- **WAVE**: Web accessibility evaluation tool
- **axe DevTools**: Browser-based accessibility testing
- **PAC 3**: PDF Accessibility Checker

### Color and Contrast Tools

- **WebAIM Contrast Checker**: Online contrast ratio calculator
- **Colour Contrast Analyser**: Desktop application
- **Color Oracle**: Color blindness simulator
- **Coblis**: Color blindness simulator

### Screen Readers

- **NVDA**: Free Windows screen reader
- **JAWS**: Commercial Windows screen reader
- **VoiceOver**: Built into Mac and iOS
- **Narrator**: Built into Windows
- **TalkBack**: Built into Android

### Learning Resources

- **WebAIM**: Web Accessibility In Mind (webaim.org)
- **Deque University**: Accessibility training courses
- **A11y Project**: Community-driven accessibility resources
- **W3C WAI**: Web Accessibility Initiative resources
- **Microsoft Accessibility**: Microsoft accessibility documentation

### Caption and Transcription Services

- **Rev**: Professional captioning services
- **3Play Media**: Captioning and audio description
- **Otter.ai**: Automated transcription
- **YouTube Auto-captions**: Free but requires editing

---
