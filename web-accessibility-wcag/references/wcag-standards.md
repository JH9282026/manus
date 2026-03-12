# Wcag Standards

Detailed reference content for web-accessibility-wcag.

---

## Web Accessibility Fundamentals

### What is Web Accessibility

Web accessibility means designing and developing websites, tools, and technologies so that people with disabilities can perceive, understand, navigate, and interact with the web. It encompasses all disabilities that affect web access, including visual, auditory, physical, speech, cognitive, and neurological disabilities.

### Importance of Accessibility

**Inclusive Design**: Accessibility ensures that approximately 1 billion people worldwide with disabilities can access digital content. Inclusive design benefits everyone by creating flexible, adaptable interfaces that work across diverse contexts and abilities.

**Legal Compliance**: Many countries mandate web accessibility through laws like the Americans with Disabilities Act (ADA), Section 508, European Accessibility Act, and UK Equality Act. Non-compliance can result in lawsuits, fines, and legal action.

**Business Benefits**: Accessible websites reach larger audiences, improve customer satisfaction, and demonstrate corporate social responsibility. Companies with accessible websites often see increased conversions and customer loyalty.

**SEO Benefits**: Many accessibility practices align with SEO best practices. Semantic HTML, proper heading structure, alt text, and transcripts all improve search engine rankings and discoverability.

**Better UX for Everyone**: Accessibility improvements benefit all users. Captions help people in noisy environments, high contrast benefits users in bright sunlight, and keyboard navigation helps power users work more efficiently.

### Disability Types

**Visual Disabilities**: Blindness, low vision, color blindness, and visual processing disorders. Users may rely on screen readers, screen magnifiers, or high-contrast displays.

**Auditory Disabilities**: Deafness, hard of hearing, and auditory processing disorders. Users require captions, transcripts, and visual alternatives to audio content.

**Motor Disabilities**: Limited fine motor control, paralysis, tremors, and repetitive strain injuries. Users may rely on keyboards, voice control, eye tracking, or switch devices.

**Cognitive Disabilities**: Learning disabilities, attention disorders, memory impairments, and intellectual disabilities. Users benefit from clear language, consistent navigation, and predictable interfaces.

**Seizure Disorders**: Photosensitive epilepsy and other seizure conditions triggered by flashing content. Content must avoid rapid flashing and provide warnings for potentially triggering content.

**Speech Disabilities**: Difficulty speaking clearly or at all. Users may not be able to use voice-controlled interfaces and need alternative input methods.

### Accessibility Principles (POUR)

The four principles of web accessibility form the foundation of WCAG:

**Perceivable**: Information and user interface components must be presentable to users in ways they can perceive. This includes providing text alternatives, captions, and adaptable layouts.

**Operable**: User interface components and navigation must be operable. All functionality must be available via keyboard, users must have enough time to read content, and content must not cause seizures.

**Understandable**: Information and user interface operation must be understandable. Content must be readable, navigation must be predictable, and users must be helped to avoid and correct mistakes.

**Robust**: Content must be robust enough to be interpreted reliably by a wide variety of user agents, including assistive technologies. This requires valid code and proper use of accessibility APIs.

---

---

## WCAG Guidelines Overview

### What is WCAG

The Web Content Accessibility Guidelines (WCAG) are internationally recognized standards developed by the World Wide Web Consortium (W3C) Web Accessibility Initiative (WAI). WCAG provides a single shared standard for web content accessibility that meets the needs of individuals, organizations, and governments.

### WCAG Versions

**WCAG 2.0** (December 2008): The foundational version with 12 guidelines organized under the four POUR principles. Still widely referenced but superseded by newer versions.

**WCAG 2.1** (June 2018): Extended WCAG 2.0 with 17 additional success criteria addressing mobile accessibility, low vision, and cognitive disabilities. This is the most commonly required version for legal compliance.

**WCAG 2.2** (October 2023): Added 9 new success criteria focusing on users with cognitive or learning disabilities, users with low vision, and users on mobile devices. Includes requirements for focus appearance, dragging movements, and accessible authentication.

### Conformance Levels

**Level A (Minimum)**: Basic accessibility requirements that must be satisfied. Level A criteria address the most severe barriers that would completely prevent some users from accessing content.

**Level AA (Standard)**: The standard level of accessibility required by most regulations and laws. Level AA addresses significant barriers and is the recommended target for most websites.

**Level AAA (Enhanced)**: The highest level of accessibility. Level AAA is not required for entire sites as it may not be possible for all content types, but should be applied where feasible.

### Success Criteria

Success criteria are testable statements that define accessibility requirements. Each criterion belongs to a specific guideline and conformance level. Criteria are numbered using a three-part system (Principle.Guideline.Criterion), such as 1.4.3 for "Contrast (Minimum)."

Conformance requires meeting all success criteria at the target level and all levels below it. A site claiming Level AA conformance must meet all Level A and Level AA criteria.

---

---

## WCAG 2.1 and 2.2 Guidelines

### Perceivable

**Text Alternatives (1.1)**: All non-text content must have text alternatives that serve the equivalent purpose. Images need alt text, complex graphics need long descriptions, and purely decorative elements should be hidden from assistive technologies.

**Time-Based Media (1.2)**: Prerecorded audio needs transcripts, prerecorded video needs captions and audio descriptions, and live content needs real-time captions. Level AAA requires sign language interpretation.

**Adaptable (1.3)**: Information, structure, and relationships must be programmatically determinable or available in text. Content must be presentable in different ways without losing meaning. WCAG 2.1 added requirements for identifying input purpose.

**Distinguishable (1.4)**: Content must be easily distinguishable from backgrounds and other content. This includes color contrast ratios (4.5:1 for normal text, 3:1 for large text at Level AA), audio control, text resizing up to 200%, and reflow for responsive layouts. WCAG 2.2 added focus appearance requirements.

### Operable

**Keyboard Accessible (2.1)**: All functionality must be available via keyboard without requiring specific timing. Users must be able to move focus away from any component, and keyboard shortcuts must be provided in accessible ways. WCAG 2.1 added character key shortcuts requirements.

**Enough Time (2.2)**: Users must have enough time to read and use content. Time limits must be adjustable, moving content must be pauseable, and auto-updating content must be controllable.

**Seizures and Physical Reactions (2.3)**: Content must not flash more than three times per second. WCAG 2.1 added criteria for motion animation that can be disabled.

**Navigable (2.4)**: Users must be able to navigate, find content, and determine where they are. This includes skip links, page titles, logical focus order, descriptive link text, multiple ways to find pages, visible focus indicators, and clear headings and labels. WCAG 2.2 enhanced focus appearance requirements.

**Input Modalities (2.5)**: WCAG 2.1 added requirements for pointer gestures, pointer cancellation, label in name, motion actuation, and target size. WCAG 2.2 added dragging movements and target size minimum criteria.

### Understandable

**Readable (3.1)**: The language of the page and parts of the page must be programmatically determinable. Level AAA includes requirements for unusual words, abbreviations, reading level, and pronunciation.

**Predictable (3.2)**: Web pages must appear and operate in predictable ways. Components should not change context on focus or input without warning. Navigation must be consistent across pages.

**Input Assistance (3.3)**: Users must be helped to avoid and correct mistakes. Errors must be identified and described, labels and instructions must be provided, and suggestions for correction should be offered. WCAG 2.2 added accessible authentication and redundant entry criteria.

### Robust

**Compatible (4.1)**: Content must be compatible with current and future user agents and assistive technologies. This requires proper parsing (valid HTML), ensuring elements have complete start and end tags, and that all interactive elements have accessible names, roles, and values. Status messages must be programmatically determinable.

---

---

## Screen Reader Optimization

### How Screen Readers Work

Screen readers parse the accessibility tree built from HTML and ARIA, then output content through text-to-speech or braille displays. They announce element names, roles, states, and relationships. Reading order follows DOM order, and navigation uses headings, landmarks, and links.

### Screen Reader Testing

**NVDA**: Free, open-source screen reader for Windows. Widely used and excellent for development testing.

**JAWS**: Commercial Windows screen reader, popular in professional environments. Most full-featured but requires purchase.

**VoiceOver**: Built into macOS and iOS. Essential for testing Apple platform accessibility.

**TalkBack**: Android's built-in screen reader. Important for mobile accessibility testing.

**Narrator**: Built into Windows. Useful for basic testing but less commonly used by end users.

### Semantic HTML

**Headings**: Use heading levels (h1-h6) hierarchically to structure content. Screen reader users navigate by headings to scan page content quickly.

**Landmarks**: Use semantic elements (`<header>`, `<nav>`, `<main>`, `<aside>`, `<footer>`) or ARIA landmarks to define page regions.

**Lists**: Use `<ul>`, `<ol>`, and `<dl>` for list content. Screen readers announce list type and item count.

**Tables**: Use proper table markup with `<th>`, `scope`, and `<caption>` for data tables. Avoid tables for layout.

**Forms**: Associate labels with inputs using `<label for="">` or wrapping. Group related fields with `<fieldset>` and `<legend>`.

### Alt Text Best Practices

**Descriptive**: Describe the image content and function. Focus on what information the image conveys.

**Concise**: Keep alt text brief—typically under 125 characters. Long descriptions can use `aria-describedby` or long description pages.

**Context-Appropriate**: Alt text should vary based on the image's purpose in context. The same image may need different alt text in different contexts.

**Decorative Images**: Use empty alt (`alt=""`) or CSS backgrounds for purely decorative images. These should be hidden from assistive technology.

### Screen Reader-Only Content

**Visually Hidden Text**: Use CSS techniques (clip, absolute positioning off-screen) to provide additional context for screen reader users without affecting visual design.

**Skip Links**: Provide skip links to bypass navigation. These should be visually hidden but become visible on focus.

**Additional Context**: Add screen reader-only text to clarify links like "Read more" by adding context like "about accessibility testing."

---

---

## Color Contrast and Visual Design

### Color Contrast Requirements

**WCAG AA (Standard)**: Normal text requires 4.5:1 contrast ratio. Large text (18pt/24px regular or 14pt/18.5px bold) requires 3:1 ratio. User interface components and graphics require 3:1 ratio.

**WCAG AAA (Enhanced)**: Normal text requires 7:1 contrast ratio. Large text requires 4.5:1 ratio. Not required for all content but recommended where possible.

### Color Contrast Tools

**WebAIM Contrast Checker**: Web-based tool for checking color combinations against WCAG requirements.

**Colour Contrast Analyser**: Desktop application that can sample colors from any application or screen area.

**Browser DevTools**: Chrome, Firefox, and Edge DevTools include built-in contrast checking in their accessibility inspection tools.

### Color Usage

**Don't Rely on Color Alone**: Never use color as the only means of conveying information. Error states, required fields, and status indicators need additional visual cues.

**Use Patterns and Icons**: Supplement color with patterns, icons, underlines, or text labels. Charts and graphs should use patterns or labels in addition to color.

**Colorblind-Friendly Palettes**: Choose colors that remain distinguishable to users with color vision deficiency. Avoid problematic combinations like red/green or blue/yellow.

### Visual Design Considerations

**Font Size**: Body text should be at least 16px. Allow users to resize text up to 200% without loss of content or functionality.

**Line Height**: Use adequate line height (1.5 for body text) to improve readability and support cognitive accessibility.

**Letter Spacing**: Avoid excessive letter spacing that reduces readability. Ensure text remains readable when spacing is increased.

**Text Alignment**: Left-aligned text is most readable for languages read left to right. Justified text can create uneven spacing that hinders readability.

---

---

## Legal Requirements and Standards

### Legal Frameworks

**ADA (Americans with Disabilities Act)**: US civil rights law that courts have interpreted to apply to websites. No explicit web standards but WCAG 2.1 AA is the commonly accepted benchmark.

**Section 508**: US federal law requiring federal agencies to make electronic information accessible. References WCAG 2.0 Level AA.

**European Accessibility Act**: EU directive requiring accessibility for various products and services including websites.

**UK Equality Act**: Requires reasonable adjustments to ensure disabled people can access services, including websites.

### WCAG as Legal Standard

WCAG 2.1 Level AA has become the de facto legal standard for web accessibility. Most accessibility lawsuits reference WCAG criteria, and regulatory frameworks increasingly mandate WCAG compliance.

### Accessibility Statements

Accessibility statements should include: scope of accessibility commitment, conformance level targeted, known limitations, contact information for accessibility feedback, and date of most recent assessment.

### Consequences of Non-Compliance

Non-compliance risks include: lawsuits (increasingly common in the US), regulatory fines, reputation damage, and lost customers. The cost of remediation typically exceeds the cost of building accessibility from the start.

---

---

## Accessibility Best Practices

### Semantic HTML

Use proper HTML elements for their intended purposes. Heading hierarchy, landmark elements, lists, tables, and forms should all use appropriate semantic markup. Valid HTML provides a strong accessibility foundation.

### Progressive Enhancement

Build core functionality that works for everyone, then enhance for capable browsers. Ensure basic content and functionality work without JavaScript, CSS, or advanced features.

### Responsive and Mobile Accessibility

**Touch Targets**: Ensure touch targets are at least 44x44 pixels for easy activation. WCAG 2.2 requires 24x24 pixel minimum for Level AA.

**Mobile Navigation**: Mobile navigation patterns must be keyboard accessible and work with mobile screen readers.

**Mobile Forms**: Forms should use appropriate input types and be optimized for mobile keyboard entry.

### Performance and Accessibility

**Fast Loading**: Slow sites are inaccessible. Users with cognitive disabilities may lose context, and assistive technology users may experience timeouts.

**Reduced Motion**: Respect `prefers-reduced-motion` media query. Provide controls to pause, stop, or reduce animation.

### Documentation and Training

**Accessibility Guidelines**: Maintain documented accessibility standards and design patterns.

**Developer Training**: Train developers on accessibility requirements, testing techniques, and assistive technology use.

**Design System Documentation**: Include accessibility requirements in design system documentation.

**Ongoing Education**: Accessibility knowledge requires continuous updating as standards and technologies evolve.

---

---

## Conclusion

Web accessibility is not just a compliance requirement but a fundamental aspect of quality web design. By understanding WCAG guidelines, implementing proper semantic HTML and ARIA, ensuring keyboard accessibility, and testing with assistive technologies, designers and developers can create inclusive experiences that work for everyone. Accessibility benefits all users and should be integrated into every phase of the design and development process.