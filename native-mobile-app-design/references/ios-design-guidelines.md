# iOS Design Guidelines (HIG)

## Navigation Patterns

### Tab Bar
- 3-5 tabs maximum
- Icons + text labels (required)
- Active tab uses tint color
- Badges for notifications
- Persistent across app (except full-screen content)

### Navigation Controller (Push/Pop)
- Back button in top-left (auto-generated)
- Title in center of navigation bar
- Action buttons in top-right (1-2 max)
- Large titles for top-level views
- Swipe from left edge to go back

### Modal Presentation
- **Sheet**: Partial screen, dismissible by swiping down
- **Full screen**: Requires explicit dismiss action
- **Alert**: Centered dialog for important decisions
- **Action sheet**: Bottom options list

---

## Typography (San Francisco)

| Style | Size | Weight | Use |
|-------|------|--------|-----|
| Large Title | 34pt | Bold | Top-level headers |
| Title 1 | 28pt | Bold | Section headers |
| Title 2 | 22pt | Bold | Sub-section headers |
| Title 3 | 20pt | Semibold | Card titles |
| Headline | 17pt | Semibold | List item titles |
| Body | 17pt | Regular | Primary content |
| Callout | 16pt | Regular | Secondary content |
| Subheadline | 15pt | Regular | Supporting text |
| Footnote | 13pt | Regular | Metadata |
| Caption 1 | 12pt | Regular | Labels |
| Caption 2 | 11pt | Regular | Small labels |

### Dynamic Type
- Support all accessibility text sizes
- Test from xSmall to AX5 (accessibility extra large)
- Use system fonts for automatic scaling
- Truncate or scroll when text exceeds bounds

---

## iOS Components

### Lists (UITableView)
- Grouped style: Sections with headers/footers
- Inset grouped: Rounded section backgrounds
- Swipe actions: Delete, archive, custom
- Pull to refresh at top

### Cards
- Corner radius: 10-14pt
- Light shadow or hairline border
- Content padding: 16pt
- Stack vertically on narrow screens

### Controls
| Control | Use |
|---------|-----|
| Toggle (switch) | Binary on/off settings |
| Segmented control | 2-5 related options |
| Stepper | Increment/decrement numbers |
| Slider | Continuous value selection |
| Date picker | Date and time selection |

---

## iOS Accessibility

- VoiceOver support for all interactive elements
- Accessibility labels on images and custom controls
- Support Dynamic Type throughout
- Color alone never conveys meaning
- Minimum 4.5:1 contrast ratio for text
- Reduce Motion support (prefers-reduced-motion)
