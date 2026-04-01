---
name: ios-development-swift-swiftui
description: "Build native iOS applications using Swift and SwiftUI with modern declarative UI patterns, state management, and Apple ecosystem integration. Use for: creating iOS apps with SwiftUI, implementing MVVM architecture, managing state with @State/@Observable, integrating with Apple frameworks (SwiftData, TipKit, WidgetKit), optimizing performance, handling navigation and lifecycle, building for iPhone/iPad/Apple Watch/Vision Pro, and following Apple Human Interface Guidelines."
---

# iOS Development with Swift and SwiftUI

Build modern, performant iOS applications using Swift and SwiftUI's declarative UI framework.

## Overview

SwiftUI is Apple's modern toolkit for building native user interfaces across all Apple platforms using Swift. It employs a declarative programming model where you describe what the UI should look like for a given state, and SwiftUI automatically handles updates when data changes. This skill covers SwiftUI development patterns, state management, performance optimization, and integration with the Apple ecosystem.

## Development Environment Setup

| Component | Requirement | Notes |
|-----------|-------------|-------|
| macOS | Latest stable version | Required for Xcode |
| Xcode | 15.0+ | Includes Swift 5.9+, SwiftUI, Simulators |
| Apple Developer Account | Free or Paid | Paid required for App Store distribution |
| Target iOS Version | iOS 17+ recommended | Use iOS 15+ for broader compatibility |
| Hardware | Apple Silicon or Intel Mac | M-series Macs offer better performance |

**Initial Setup:**
- Install Xcode from Mac App Store
- Configure signing certificates and provisioning profiles
- Set up simulators for target devices (iPhone, iPad, Apple Watch, Vision Pro)
- Enable Developer Mode on physical test devices

## Core SwiftUI Concepts

### Declarative UI Paradigm

SwiftUI uses a declarative approach where UI is a function of state. When state changes, SwiftUI automatically recomputes and updates the affected views.

### Composable Functions

Views are built using `@Composable` functions (structs conforming to `View` protocol) that return `some View`. Break complex UIs into small, focused, reusable components.

### Property Wrappers for State Management

| Property Wrapper | Use Case | Ownership | Lifecycle |
|------------------|----------|-----------|----------|
| `@State` | Local view state | View owns | View lifetime |
| `@Binding` | Two-way connection to parent state | Parent owns | Passed from parent |
| `@StateObject` | Create and own ObservableObject | View owns | Persists across view updates |
| `@ObservedObject` | Reference external ObservableObject | External | Injected from outside |
| `@EnvironmentObject` | App-wide shared state | App/ancestor | Injected via environment |
| `@Environment` | System-provided values | System | Platform-managed |
| `@Observable` (iOS 17+) | Modern observation for classes | Varies | Automatic change tracking |

**Best Practice:** Use `@Observable` macro for iOS 17+ projects. For view-owned models, use `@StateObject`. For injected models, use `@ObservedObject`.

## Architecture Patterns

### MVVM (Model-View-ViewModel)

**Recommended structure:**
- **Model:** Data structures and business logic (often `struct` for value semantics)
- **View:** SwiftUI views (declarative UI)
- **ViewModel:** `@Observable` class or `ObservableObject` managing UI state and business logic

**Benefits:** Clear separation of concerns, testable ViewModels, reactive UI updates.

### View Composition

- Extract subviews into separate structs when views exceed ~50 lines
- Use `ViewModifier` for reusable styling patterns
- Prefer value types (`struct`) for models to leverage SwiftUI's efficient diffing
- Keep view bodies lightweight and declarative

## Layout and UI Components

### Layout Containers

| Container | Purpose | Performance Notes |
|-----------|---------|------------------|
| `VStack` | Vertical arrangement | Use `LazyVStack` for large lists |
| `HStack` | Horizontal arrangement | Use `LazyHStack` for large lists |
| `ZStack` | Layered/stacked elements | Good for overlays |
| `LazyVGrid`/`LazyHGrid` | Grid layouts | Only renders visible items |
| `List` | Scrollable list | Built-in performance optimization |
| `ScrollView` | Custom scrolling | Combine with Lazy stacks |

### Modifiers

Modifiers decorate and configure views. They are chainable and order-dependent:

```swift
Text("Hello")
    .padding()
    .background(Color.blue)
    .cornerRadius(8)
```

**Common modifiers:** `.padding()`, `.frame()`, `.background()`, `.foregroundStyle()`, `.font()`, `.clipShape()`, `.shadow()`, `.opacity()`

## Performance Optimization

### Minimize Recomputations

- Keep state variables focused and granular
- Avoid passing large or frequently changing data unnecessarily
- Extract static content into separate view structs
- Use `.id()` modifier for stable list item identification

### Lazy Loading

For large datasets, always use lazy containers:
- `LazyVStack`, `LazyHStack` for scrolling content
- `LazyVGrid`, `LazyHGrid` for grids
- These render only visible items, dramatically improving performance

### Avoid Heavy Work in View Body

The `body` property should be pure and lightweight. Move expensive operations to:
- ViewModels (for business logic)
- `.task` modifier (for async work tied to view lifecycle)
- `.onAppear` (for side effects when view appears)
- Background tasks (for heavy computation)

### Profiling

Use Instruments to identify bottlenecks:
- Time Profiler for CPU usage
- Allocations for memory issues
- SwiftUI view body profiling

## Navigation and Lifecycle

### Navigation (iOS 16+)

**NavigationStack** is the modern approach:

```swift
NavigationStack {
    List(items) { item in
        NavigationLink(value: item) {
            ItemRow(item: item)
        }
    }
    .navigationDestination(for: Item.self) { item in
        DetailView(item: item)
    }
}
```

### Modal Presentation

- `.sheet(isPresented:)` for modal sheets
- `.fullScreenCover(isPresented:)` for full-screen modals
- `.alert(isPresented:)` for alerts
- `.confirmationDialog(isPresented:)` for action sheets

### Lifecycle Modifiers

| Modifier | Use Case |
|----------|----------|
| `.task` | Async work tied to view lifecycle (auto-cancels) |
| `.onAppear` | Side effects when view appears |
| `.onDisappear` | Cleanup when view disappears |
| `.onChange(of:)` | React to specific value changes |

## Data Persistence

### SwiftData (iOS 17+)

Modern persistence framework with seamless SwiftUI integration:

```swift
@Model
class Item {
    var name: String
    var timestamp: Date
}

@Query var items: [Item]
@Environment(\.modelContext) var modelContext
```

**Benefits:** Type-safe, automatic SwiftUI updates, migration support.

### UserDefaults

For simple key-value storage:
- Use `@AppStorage` property wrapper for automatic SwiftUI binding
- Suitable for preferences, settings, small data

### Keychain

For sensitive data (passwords, tokens):
- Use Security framework or third-party wrappers
- Never store credentials in UserDefaults or files

## Testing and Debugging

### Preview System

Use `#Preview` macro (iOS 17+) or `PreviewProvider` for live previews:

```swift
#Preview {
    ContentView()
        .modelContainer(for: Item.self)
}
```

**Preview configurations:**
- Different device sizes
- Light/dark mode
- Dynamic type sizes
- Localization

### Unit Testing

- Test ViewModels in isolation (no SwiftUI dependencies)
- Use dependency injection for testability
- Mock data sources and services

### UI Testing

Use XCTest UI testing framework:
- Test user flows and interactions
- Verify accessibility identifiers
- Automate regression testing

## Apple Ecosystem Integration

### Cross-Platform Development

SwiftUI works across:
- iOS/iPadOS (iPhone, iPad)
- macOS (Mac apps)
- watchOS (Apple Watch)
- visionOS (Apple Vision Pro)
- tvOS (Apple TV)

**Adaptive design:** Use `@Environment(\.horizontalSizeClass)` and platform checks for responsive layouts.

### Modern Frameworks

| Framework | Purpose |
|-----------|----------|
| SwiftData | Data persistence and modeling |
| TipKit | In-app tips and onboarding |
| WidgetKit | Home screen and Lock screen widgets |
| App Intents | Siri shortcuts and automation |
| StoreKit | In-app purchases and subscriptions |
| CloudKit | iCloud sync and storage |

## Best Practices

### Code Quality

- Follow Swift API Design Guidelines
- Use meaningful, descriptive names
- Avoid force unwrapping (`!`) - use `if let` or `guard let`
- Leverage Swift's type safety and optionals
- Document complex logic with comments

### Accessibility

- Use semantic views (Button, Label, etc.)
- Provide accessibility labels and hints
- Support Dynamic Type
- Test with VoiceOver
- Ensure sufficient color contrast

### Human Interface Guidelines

Follow Apple's HIG for:
- Consistent navigation patterns
- Platform-appropriate UI components
- Proper spacing and typography
- Color and visual design
- Gesture conventions

### Security

- Use App Transport Security (HTTPS only)
- Implement biometric authentication (Face ID, Touch ID)
- Secure sensitive data in Keychain
- Validate user input
- Follow principle of least privilege for permissions

## Deployment

### App Store Submission

1. Configure app metadata in App Store Connect
2. Prepare screenshots and preview videos
3. Set up pricing and availability
4. Archive and upload build via Xcode
5. Submit for review

### TestFlight

Use TestFlight for beta testing:
- Internal testing (up to 100 testers)
- External testing (up to 10,000 testers)
- Collect feedback and crash reports

### Continuous Integration

Set up CI/CD with:
- Xcode Cloud (Apple's native solution)
- GitHub Actions
- Fastlane for automation

## Using the Reference Files

### When to Read Each Reference

**`/references/swiftui-patterns-cookbook.md`** — Read when implementing specific UI patterns, handling complex state management scenarios, or looking for code examples for common SwiftUI tasks.

**`/references/performance-optimization.md`** — Read when experiencing performance issues, optimizing list rendering, reducing view recomputations, or profiling with Instruments.

**`/references/advanced-techniques.md`** — Read when implementing custom view modifiers, preference keys, geometry readers, custom animations, or advanced SwiftUI features.

**`/references/troubleshooting-guide.md`** — Read when encountering common SwiftUI errors, debugging state issues, fixing preview crashes, or resolving build problems.

## References

- [Advanced Techniques](references/advanced-techniques.md)
- [Performance Optimization](references/performance-optimization.md)
- [Swiftui Patterns Cookbook](references/swiftui-patterns-cookbook.md)
- [Troubleshooting Guide](references/troubleshooting-guide.md)
