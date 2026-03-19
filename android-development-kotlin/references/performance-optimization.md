# Android Performance Optimization

Techniques for building high-performance Android apps.

---

## Recomposition Optimization

### Stability
```kotlin
// ✅ Stable: Immutable data class
@Immutable
data class User(val id: Int, val name: String)

// ❌ Unstable: Mutable properties
data class User(var id: Int, var name: String)

// Use derivedStateOf for computed values
@Composable
fun FilteredList(items: List<Item>, query: String) {
    val filtered by remember(items, query) {
        derivedStateOf { items.filter { it.name.contains(query) } }
    }
    
    LazyColumn {
        items(filtered) { item ->
            ItemRow(item)
        }
    }
}
```

### Skip Unnecessary Recompositions
```kotlin
// ✅ Extract stable subcomposables
@Composable
fun ParentView() {
    var count by remember { mutableStateOf(0) }
    
    Column {
        Counter(count) { count++ }
        StaticContent() // Won't recompose when count changes
    }
}

@Composable
fun StaticContent() {
    Text("This doesn't change")
}
```

---

## LazyList Performance

### Keys and ContentType
```kotlin
LazyColumn {
    items(
        items = itemList,
        key = { it.id }, // Stable unique key
        contentType = { it.type } // For heterogeneous lists
    ) { item ->
        when (item) {
            is HeaderItem -> HeaderCard(item)
            is ContentItem -> ContentCard(item)
        }
    }
}
```

### Avoid Nested Scrolling
```kotlin
// ❌ Bad: Nested LazyColumns
LazyColumn {
    item {
        LazyColumn { /* nested */ }
    }
}

// ✅ Good: Single LazyColumn with different item types
LazyColumn {
    items(section1) { Section1Item(it) }
    items(section2) { Section2Item(it) }
}
```

---

## Image Loading

### Coil for Compose
```kotlin
AsyncImage(
    model = ImageRequest.Builder(LocalContext.current)
        .data(imageUrl)
        .crossfade(true)
        .size(Size.ORIGINAL)
        .build(),
    contentDescription = "Image",
    modifier = Modifier.size(200.dp)
)
```

---

## Profiling

### Android Profiler
- CPU Profiler: Identify expensive operations
- Memory Profiler: Detect leaks and excessive allocations
- Network Profiler: Monitor API calls
- Energy Profiler: Battery usage

### Baseline Profiles
Improve app startup time:
```gradle
dependencies {
    implementation "androidx.profileinstaller:profileinstaller:1.3.1"
}
```
