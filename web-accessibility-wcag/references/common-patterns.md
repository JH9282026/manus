# Common Patterns

Detailed reference content for web-accessibility-wcag.

---

## Accessible Forms

### Form Labels

**Visible Labels**: Every form input must have a visible label that clearly describes its purpose. Placeholder text alone is not sufficient as it disappears when users type.

**Label Association**: Associate labels with inputs using `<label for="">` or by wrapping the input in the label element. This enables click-to-focus and screen reader announcements.

**Placeholder Text Limitations**: Placeholders should supplement, not replace, labels. They disappear when users type and often have insufficient contrast.

### Form Validation

**Clear Error Messages**: Error messages must clearly identify the problem and how to fix it. Avoid generic messages like "Invalid input."

**Inline Validation**: Show errors near the relevant field. Use `aria-describedby` to associate error messages with inputs.

**Error Summaries**: For complex forms, provide an error summary at the top of the form linking to each error. Set focus to the summary when the form is submitted with errors.

**Error Prevention**: For significant actions (financial transactions, legal agreements), provide review screens, confirmation dialogs, or undo capabilities.

### Form Structure

**Logical Grouping**: Group related fields together. Use visual proximity and programmatic grouping with `<fieldset>` and `<legend>`.

**Fieldsets and Legends**: Group radio buttons and checkboxes with fieldsets. The legend provides a group label that screen readers announce with each option.

**Required Fields**: Clearly indicate required fields using text labels, not just asterisks or color. Use `aria-required="true"` for programmatic indication.

**Input Types**: Use appropriate HTML5 input types (`email`, `tel`, `number`, `date`) to trigger appropriate keyboards and enable browser validation.

### Form Accessibility

**Keyboard Navigation**: Ensure all form elements are keyboard accessible. Focus should move through fields in logical order.

**Autocomplete**: Use `autocomplete` attributes to help users complete forms faster and reduce errors. This is especially helpful for users with motor or cognitive disabilities.

**Help Text**: Provide clear instructions and help text. Associate help text with inputs using `aria-describedby`.

---

---

## Accessible Media

### Images

**Alt Text**: All informative images need descriptive alt text. Alt text should convey the image's content and function.

**Decorative Images**: Use empty alt attributes (`alt=""`) or CSS backgrounds for purely decorative images.

**Complex Images**: Charts, graphs, and infographics need long descriptions. Use `aria-describedby`, figure/figcaption, or linked long description pages.

**SVG Accessibility**: Add `role="img"` and `aria-label` or `<title>` and `<desc>` elements to accessible SVGs.

### Video Accessibility

**Captions**: All prerecorded video with audio needs synchronized captions. Captions include dialogue, speaker identification, and relevant sound effects.

**Transcripts**: Provide text transcripts as alternatives to video content.

**Audio Descriptions**: Provide audio descriptions for visual content not conveyed through the main audio track.

**Player Controls**: Video players must be keyboard accessible with visible focus indicators.

### Audio Accessibility

**Transcripts**: All prerecorded audio needs text transcripts. Transcripts should include speaker identification and non-speech sounds.

**Captions for Audio**: When audio is presented in a video format, provide captions.

**Audio Controls**: Provide visible controls to pause, stop, and adjust volume. Auto-playing audio must be controllable.

---