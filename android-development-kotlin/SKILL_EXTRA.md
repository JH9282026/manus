# Additional Content

This file contains content moved from SKILL.md to keep it under 500 lines.

---

### Continuous Integration

- GitHub Actions
- GitLab CI/CD
- Bitrise
- Fastlane for automation

## Platform-Specific Features

### Adaptive Layouts

```kotlin
@Composable
fun AdaptiveLayout() {
    val windowSizeClass = calculateWindowSizeClass(this)
    
    when (windowSizeClass.widthSizeClass) {
        WindowWidthSizeClass.Compact -> CompactLayout()
        WindowWidthSizeClass.Medium -> MediumLayout()
        WindowWidthSizeClass.Expanded -> ExpandedLayout()
Use WindowManager library for foldable devices:

```kotlin
val windowLayoutInfo = rememberWindowLayoutInfo()
val foldingFeature = windowLayoutInfo.displayFeatures
    .filterIsInstance<FoldingFeature>()
    .firstOrNull()
```

## Using the Reference Files

### When to Read Each Reference

**`/references/compose-patterns-cookbook.md`** — Read when implementing specific UI patterns, handling complex state management, or looking for code examples for common Compose tasks.

**`/references/jetpack-libraries-guide.md`** — Read when integrating Android Jetpack libraries (Room, Navigation, WorkManager, Hilt, Paging), understanding their APIs, or implementing specific features.

**`/references/performance-optimization.md`** — Read when experiencing performance issues, optimizing recomposition, improving list rendering, or profiling with Android Profiler.

**`/references/troubleshooting-guide.md`** — Read when encountering common Compose errors, debugging state issues, fixing build problems, or resolving runtime crashes.
