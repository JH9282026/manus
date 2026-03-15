# Android Troubleshooting Guide

Common issues and solutions for Android development.

---

## Compose Issues

### Recomposition Not Triggering
**Cause:** State not properly observed.

**Solution:**
```kotlin
// ❌ Wrong: Not using State
var count = 0

// ✅ Correct: Using mutableStateOf
var count by remember { mutableStateOf(0) }

// ✅ For ViewModel
val uiState by viewModel.uiState.collectAsState()
```

### "Cannot access database on main thread"
**Solution:** Use coroutines:
```kotlin
viewModelScope.launch {
    val data = database.dao().getData()
}
```

---

## Build Issues

### Dependency Conflicts
**Solution:** Check dependency versions:
```gradle
./gradlew app:dependencies
```

### OutOfMemoryError
**Solution:** Increase heap size in gradle.properties:
```
org.gradle.jvmargs=-Xmx4096m
```

---

## Runtime Issues

### "lateinit property has not been initialized"
**Solution:** Initialize before use or use nullable type:
```kotlin
// Option 1: Initialize
private lateinit var viewModel: MyViewModel

override fun onCreate() {
    viewModel = ViewModelProvider(this)[MyViewModel::class.java]
}

// Option 2: Nullable
private var viewModel: MyViewModel? = null
```

### Memory Leaks
**Solution:** Use LeakCanary and avoid holding Activity references:
```kotlin
// ❌ Bad: Holding Activity reference
class MyWorker(val activity: Activity)

// ✅ Good: Use Application context
class MyWorker(val context: Context)
```
