---
name: android-development-kotlin
description: "Build native Android applications using Kotlin and Jetpack Compose with modern declarative UI, state management, and Android ecosystem integration. Use for: creating Android apps with Jetpack Compose, implementing MVVM/MVI architecture, managing state with ViewModel and StateFlow, integrating with Android Jetpack libraries (Room, Navigation, WorkManager), optimizing performance, handling lifecycle, building for phones/tablets/foldables/Wear OS, and following Material Design guidelines."
---

# Android Development with Kotlin and Jetpack Compose

Build modern, performant Android applications using Kotlin and Jetpack Compose's declarative UI framework.

## Overview

Jetpack Compose is Android's modern toolkit for building native UI using Kotlin. It simplifies and accelerates UI development with a declarative approach where you describe what the UI should look like based on data dependencies, and Compose automatically updates when data changes. This skill covers Compose development patterns, state management, architecture, and integration with the Android ecosystem.

## Development Environment Setup

| Component | Requirement | Notes |
|-----------|-------------|-------|
| Operating System | Windows, macOS, Linux, Chrome OS | Any modern OS |
| Android Studio | Hedgehog (2023.1.1) or later | Includes Kotlin, Compose, Emulators |
| JDK | JDK 17 or later | Bundled with Android Studio |
| Minimum SDK | API 21 (Android 5.0) | Compose requires API 21+ |
| Target SDK | Latest stable (API 34+) | Update regularly |
| Gradle | 8.0+ | Managed by Android Studio |

**Initial Setup:**
- Install Android Studio from developer.android.com
- Configure Android SDK and emulators
- Enable Kotlin and Compose in project
- Set up device for USB debugging or use emulator

## Core Jetpack Compose Concepts

### Declarative UI Paradigm

Compose uses a declarative approach where UI is a function of state. When state changes, Compose automatically recomposes affected composables.

### Composable Functions

UI elements are built using `@Composable` functions:

```kotlin
@Composable
fun Greeting(name: String) {
    Text(text = "Hello $name!")
}
```

**Key characteristics:**
- Annotated with `@Composable`
- Can call other composables
- Describe UI structure, not imperative operations
- Recompose when state changes

### State Management in Compose

| State API | Use Case | Scope |
|-----------|----------|-------|
| `remember` | Cache values across recompositions | Single composable |
| `mutableStateOf` | Create observable state | Local state |
| `rememberSaveable` | Survive configuration changes | Activity recreation |
| `ViewModel` | Business logic and UI state | Screen/feature |
| `StateFlow`/`SharedFlow` | Reactive streams | ViewModel to UI |
| `collectAsState()` | Convert Flow to Compose State | Composable |

**Example:**
```kotlin
@Composable
fun Counter() {
    var count by remember { mutableStateOf(0) }
    
    Button(onClick = { count++ }) {
        Text("Count: $count")
    }
}
```

## Architecture Patterns

### MVVM (Model-View-ViewModel)

**Recommended structure for Compose apps:**

- **Model:** Data classes, repositories, data sources
- **View:** Composable functions (UI)
- **ViewModel:** `androidx.lifecycle.ViewModel` managing UI state

**Benefits:** Clear separation, testable ViewModels, lifecycle-aware, survives configuration changes.

### MVI (Model-View-Intent)

**Unidirectional data flow pattern:**

- **Model:** UI state (single source of truth)
- **View:** Composables rendering state
- **Intent:** User actions/events

**Flow:** User Intent → ViewModel processes → State update → UI recomposes

### ViewModel Integration

```kotlin
class MyViewModel : ViewModel() {
    private val _uiState = MutableStateFlow(UiState())
    val uiState: StateFlow<UiState> = _uiState.asStateFlow()
    
    fun onEvent(event: UserEvent) {
        // Handle events, update state
    }
}

@Composable
fun MyScreen(viewModel: MyViewModel = viewModel()) {
    val uiState by viewModel.uiState.collectAsState()
    
    // UI based on uiState
}
```

## Layout and UI Components

### Layout Composables

| Composable | Purpose | Performance Notes |
|------------|---------|------------------|
| `Column` | Vertical arrangement | Use `LazyColumn` for large lists |
| `Row` | Horizontal arrangement | Use `LazyRow` for large lists |
| `Box` | Stacked/overlaid elements | Good for overlays |
| `LazyColumn` | Vertical scrolling list | Only renders visible items |
| `LazyRow` | Horizontal scrolling list | Only renders visible items |
| `LazyVerticalGrid` | Grid layout | Efficient for large grids |
| `Scaffold` | Material Design screen structure | Includes TopBar, BottomBar, FAB |

### Modifiers

Modifiers decorate and configure composables. Order matters:

```kotlin
Text(
    text = "Hello",
    modifier = Modifier
        .padding(16.dp)
        .background(Color.Blue)
        .clickable { /* action */ }
)
```

**Common modifiers:** `.padding()`, `.size()`, `.fillMaxWidth()`, `.background()`, `.clickable()`, `.clip()`, `.border()`

### Material Design Components

- **Material 3 (Material You):** Latest design system
- **Components:** Button, Card, TextField, TopAppBar, NavigationBar, FloatingActionButton, Dialog, Snackbar
- **Theming:** Color schemes, typography, shapes

## Performance Optimization

### Minimize Recomposition

**Principles:**
- Keep state as low as possible in the tree
- Use `remember` to cache expensive computations
- Avoid creating new objects in composables
- Use `derivedStateOf` for computed state

```kotlin
// ✅ Good: Derived state
val filteredItems by remember(items, query) {
    derivedStateOf { items.filter { it.contains(query) } }
}

// ❌ Bad: Recomputes on every recomposition
val filteredItems = items.filter { it.contains(query) }
```

### Lazy Lists Performance

**Best practices:**
- Use `LazyColumn`/`LazyRow` for lists
- Provide stable keys: `key = { item.id }`
- Use `contentType` for heterogeneous lists
- Avoid nested lazy lists

```kotlin
LazyColumn {
    items(
        items = itemList,
        key = { it.id },
        contentType = { it.type }
    ) { item ->
        ItemCard(item)
    }
}
```

### Stability and Immutability

Compose optimizes recomposition for stable, immutable types:

```kotlin
// ✅ Stable: Data class with val properties
data class User(val id: Int, val name: String)

// ❌ Unstable: Mutable properties
data class User(var id: Int, var name: String)

// Use @Stable or @Immutable annotations when needed
@Immutable
data class UiState(val items: List<Item>)
```

## Navigation

### Jetpack Navigation Compose

```kotlin
val navController = rememberNavController()

NavHost(navController, startDestination = "home") {
    composable("home") { HomeScreen(navController) }
    composable(
        route = "detail/{itemId}",
        arguments = listOf(navArgument("itemId") { type = NavType.IntType })
    ) { backStackEntry ->
        val itemId = backStackEntry.arguments?.getInt("itemId")
        DetailScreen(itemId)
    }
}

// Navigate
navController.navigate("detail/123")
```

### Type-Safe Navigation (Kotlin Serialization)

```kotlin
@Serializable
data class DetailRoute(val itemId: Int)

NavHost(navController, startDestination = HomeRoute) {
    composable<HomeRoute> { HomeScreen() }
    composable<DetailRoute> { backStackEntry ->
        val route: DetailRoute = backStackEntry.toRoute()
        DetailScreen(route.itemId)
    }
}
```

## Data Persistence

### Room Database

**Modern Android persistence:**

```kotlin
@Entity
data class Task(
    @PrimaryKey val id: Int,
    val title: String,
    val isCompleted: Boolean
)

@Dao
interface TaskDao {
    @Query("SELECT * FROM task")
    fun getAllTasks(): Flow<List<Task>>
    
    @Insert
    suspend fun insert(task: Task)
    
    @Delete
    suspend fun delete(task: Task)
}

@Database(entities = [Task::class], version = 1)
abstract class AppDatabase : RoomDatabase() {
    abstract fun taskDao(): TaskDao
}
```

### DataStore (Preferences)

Replacement for SharedPreferences:

```kotlin
val Context.dataStore: DataStore<Preferences> by preferencesDataStore("settings")

val THEME_KEY = stringPreferencesKey("theme")

// Write
suspend fun saveTheme(theme: String) {
    context.dataStore.edit { preferences ->
        preferences[THEME_KEY] = theme
    }
}

// Read
val themeFlow: Flow<String> = context.dataStore.data
    .map { preferences -> preferences[THEME_KEY] ?: "light" }
```

## Android Jetpack Integration

### Key Jetpack Libraries

| Library | Purpose |
|---------|----------|
| Lifecycle | Lifecycle-aware components |
| ViewModel | UI state management |
| Room | SQLite database abstraction |
| Navigation | In-app navigation |
| WorkManager | Background tasks |
| Hilt | Dependency injection |
| Paging | Large dataset pagination |
| CameraX | Camera functionality |

### Dependency Injection with Hilt

```kotlin
@HiltAndroidApp
class MyApplication : Application()

@AndroidEntryPoint
class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent { MyApp() }
    }
}

@HiltViewModel
class MyViewModel @Inject constructor(
    private val repository: Repository
) : ViewModel() {
    // ViewModel logic
}
```

## Testing

### Composable Testing

```kotlin
@Test
fun myTest() {
    composeTestRule.setContent {
        MyComposable()
    }
    
    composeTestRule
        .onNodeWithText("Hello")
        .assertIsDisplayed()
        .performClick()
}
```

### ViewModel Testing

```kotlin
@Test
fun `test user event updates state`() = runTest {
    val viewModel = MyViewModel(fakeRepository)
    
    viewModel.onEvent(UserEvent.LoadData)
    
    val state = viewModel.uiState.value
    assertEquals(expected, state.data)
}
```

## Material Design and Theming

### Material 3 Theme

```kotlin
@Composable
fun MyAppTheme(
    darkTheme: Boolean = isSystemInDarkTheme(),
    content: @Composable () -> Unit
) {
    val colorScheme = if (darkTheme) {
        darkColorScheme()
    } else {
        lightColorScheme()
    }
    
    MaterialTheme(
        colorScheme = colorScheme,
        typography = Typography,
        content = content
    )
}
```

### Dynamic Color (Android 12+)

```kotlin
val colorScheme = when {
    Build.VERSION.SDK_INT >= Build.VERSION_CODES.S -> {
        if (darkTheme) dynamicDarkColorScheme(context)
        else dynamicLightColorScheme(context)
    }
    darkTheme -> darkColorScheme()
    else -> lightColorScheme()
}
```

## Best Practices

### Code Quality

- Follow Kotlin coding conventions
- Use meaningful, descriptive names
- Leverage Kotlin's null safety
- Use coroutines for async operations
- Avoid blocking the main thread

### Accessibility

- Provide content descriptions: `Modifier.semantics { contentDescription = "..." }`
- Support TalkBack screen reader
- Ensure sufficient touch target sizes (48dp minimum)
- Test with accessibility scanner
- Support dynamic font scaling

### Security

- Use HTTPS for network communication
- Implement certificate pinning for sensitive apps
- Store sensitive data in EncryptedSharedPreferences or Keystore
- Validate all user input
- Use ProGuard/R8 for code obfuscation
- Implement biometric authentication

### Performance

- Profile with Android Profiler
- Use Baseline Profiles for startup optimization
- Implement proper image loading (Coil, Glide)
- Avoid memory leaks (use LeakCanary)
- Optimize APK size with App Bundles

## Deployment

### Google Play Store

1. **Prepare Release:**
   - Generate signed APK/AAB
   - Configure ProGuard/R8
   - Test thoroughly on multiple devices

2. **Play Console:**
   - Create app listing
   - Upload screenshots and assets
   - Set pricing and distribution
   - Submit for review

3. **App Signing:**
   - Use Play App Signing (recommended)
   - Manage signing keys securely

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

## References

- [Compose Patterns Cookbook](references/compose-patterns-cookbook.md)
- [Jetpack Libraries Guide](references/jetpack-libraries-guide.md)
- [Performance Optimization](references/performance-optimization.md)
- [Troubleshooting Guide](references/troubleshooting-guide.md)
