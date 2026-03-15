# SwiftUI Troubleshooting Guide

Common issues, errors, and their solutions in SwiftUI development.

---

## Preview Issues

### Preview Crashes or Fails to Load

**Symptoms:**
- "Cannot preview in this file"
- Preview crashes immediately
- Xcode hangs when loading preview

**Solutions:**

1. **Clean Build Folder:** Product → Clean Build Folder (⇧⌘K)
2. **Restart Xcode:** Quit and relaunch Xcode
3. **Delete Derived Data:**
   ```bash
   rm -rf ~/Library/Developer/Xcode/DerivedData
   ```
4. **Check Preview Code:**
   - Ensure preview has no parameters or provides default values
   - Verify all dependencies are available
   - Check for infinite loops or heavy computations

5. **Use #Preview macro (iOS 17+):**
   ```swift
   #Preview {
       ContentView()
   }
   ```

### Preview Shows Outdated Content

**Solution:** Click "Resume" button or press ⌥⌘P to refresh preview.

### Preview Requires Device/Simulator

**Cause:** Using APIs not available in preview environment.

**Solution:** Provide mock data or conditional compilation:
```swift
#if DEBUG
let dataService = MockDataService()
#else
let dataService = ProductionDataService()
#endif
```

---

## State Management Issues

### View Not Updating When State Changes

**Cause:** State not properly observed or mutated outside main thread.

**Solutions:**

1. **Ensure property wrapper is correct:**
   ```swift
   // ✅ Correct
   @State private var count = 0
   
   // ❌ Wrong - missing @State
   private var count = 0
   ```

2. **Update on main thread:**
   ```swift
   Task { @MainActor in
       self.data = await fetchData()
   }
   
   // Or
   DispatchQueue.main.async {
       self.data = newData
   }
   ```

3. **For ObservableObject, use @Published:**
   ```swift
   class ViewModel: ObservableObject {
       @Published var items: [Item] = [] // ✅
       var count: Int = 0 // ❌ Won't trigger updates
   }
   ```

### @StateObject vs @ObservedObject Confusion

**Rule:**
- Use `@StateObject` when the view **creates and owns** the object
- Use `@ObservedObject` when the object is **passed from parent**

```swift
// ✅ Correct: View owns the ViewModel
struct ContentView: View {
    @StateObject private var viewModel = ViewModel()
}

// ✅ Correct: ViewModel passed from parent
struct DetailView: View {
    @ObservedObject var viewModel: ViewModel
}

// ❌ Wrong: Using @ObservedObject for owned object
// Will recreate on every view update!
struct ContentView: View {
    @ObservedObject private var viewModel = ViewModel()
}
```

### State Reset on Navigation

**Cause:** View is recreated, losing state.

**Solutions:**

1. **Move state to parent or shared object:**
   ```swift
   @EnvironmentObject var appState: AppState
   ```

2. **Use @StateObject for persistence:**
   ```swift
   @StateObject private var viewModel = ViewModel()
   ```

3. **For NavigationStack, use path binding:**
   ```swift
   @State private var path = NavigationPath()
   NavigationStack(path: $path) { ... }
   ```

---

## Layout Issues

### View Not Appearing or Zero Size

**Causes:**
- Missing frame modifier
- Parent container has zero size
- View is hidden or opacity is 0

**Solutions:**

1. **Provide explicit frame:**
   ```swift
   Rectangle()
       .frame(width: 100, height: 100)
   ```

2. **Use flexible sizing:**
   ```swift
   Rectangle()
       .frame(maxWidth: .infinity, maxHeight: .infinity)
   ```

3. **Check parent container:**
   ```swift
   // ❌ VStack with no content has zero height
   VStack {
       // Empty
   }
   
   // ✅ Provide spacer or content
   VStack {
       Spacer()
   }
   ```

### List or ScrollView Not Scrolling

**Causes:**
- Content smaller than container
- Conflicting gestures
- Frame constraints

**Solutions:**

1. **Ensure content exceeds container:**
   ```swift
   ScrollView {
       VStack {
           ForEach(0..<50) { i in
               Text("Item \(i)")
           }
       }
   }
   .frame(height: 300) // Container height
   ```

2. **Remove conflicting frame modifiers:**
   ```swift
   // ❌ Fixed height prevents scrolling
   ScrollView {
       content
   }
   .frame(height: 200)
   
   // ✅ Max height allows scrolling
   ScrollView {
       content
   }
   .frame(maxHeight: 200)
   ```

### Keyboard Covering TextField

**Solution:** Use `.scrollDismissesKeyboard()` or adjust content insets:

```swift
ScrollView {
    VStack {
        TextField("Enter text", text: $text)
    }
}
.scrollDismissesKeyboard(.interactively)
```

---

## Navigation Issues

### NavigationLink Not Working

**Causes:**
- Not inside NavigationStack/NavigationView
- Incorrect value type
- Missing navigationDestination

**Solutions:**

1. **Wrap in NavigationStack:**
   ```swift
   NavigationStack {
       List(items) { item in
           NavigationLink(value: item) {
               Text(item.name)
           }
       }
       .navigationDestination(for: Item.self) { item in
           DetailView(item: item)
       }
   }
   ```

2. **Ensure value type matches:**
   ```swift
   // Value type must match navigationDestination
   NavigationLink(value: item) { ... }
   .navigationDestination(for: Item.self) { ... }
   ```

### Sheet Not Dismissing

**Solution:** Use environment dismiss action:

```swift
struct SheetView: View {
    @Environment(\.dismiss) var dismiss
    
    var body: some View {
        Button("Close") {
            dismiss()
        }
    }
}
```

---

## Performance Issues

### Slow List Scrolling

**Solutions:**

1. **Use LazyVStack instead of VStack:**
   ```swift
   ScrollView {
       LazyVStack { // ✅ Not VStack
           ForEach(items) { item in
               ItemRow(item: item)
           }
       }
   }
   ```

2. **Simplify row views:**
   - Reduce view hierarchy depth
   - Avoid heavy computations in body
   - Use `.id()` for stable identifiers

3. **Profile with Instruments:**
   - Product → Profile → SwiftUI template

### High CPU Usage

**Causes:**
- Excessive view recomputations
- Heavy work in view body
- Too many simultaneous animations

**Solutions:**

1. **Extract subviews to limit rebuild scope**
2. **Move computations to ViewModel**
3. **Use `.task` for async work**
4. **Profile with Time Profiler**

---

## Build Errors

### "Type 'X' does not conform to protocol 'View'"

**Cause:** View body doesn't return `some View`.

**Solution:**
```swift
struct MyView: View {
    var body: some View { // ✅ Must return some View
        Text("Hello")
    }
}
```

### "Closure containing control flow statement cannot be used with function builder"

**Cause:** Using if/else without @ViewBuilder.

**Solution:**
```swift
// ❌ Wrong
var content: some View {
    if condition {
        ViewA()
    } else {
        ViewB()
    }
}

// ✅ Correct
@ViewBuilder
var content: some View {
    if condition {
        ViewA()
    } else {
        ViewB()
    }
}
```

### "Cannot convert value of type 'X' to expected argument type 'Binding<X>'"

**Cause:** Passing value instead of binding.

**Solution:**
```swift
// ❌ Wrong
TextField("Name", text: name)

// ✅ Correct
TextField("Name", text: $name) // Use $ for binding
```

---

## Data Persistence Issues

### SwiftData Not Saving

**Solutions:**

1. **Ensure model context is available:**
   ```swift
   @Environment(\.modelContext) var modelContext
   ```

2. **Explicitly save if needed:**
   ```swift
   try? modelContext.save()
   ```

3. **Check model definition:**
   ```swift
   @Model
   class Item {
       var name: String // ✅ Stored property
       
       init(name: String) {
           self.name = name
       }
   }
   ```

### UserDefaults Not Persisting

**Solution:** Use @AppStorage correctly:

```swift
// ✅ Correct
@AppStorage("username") var username: String = ""

// ❌ Wrong - not using @AppStorage
var username: String {
    get { UserDefaults.standard.string(forKey: "username") ?? "" }
    set { UserDefaults.standard.set(newValue, forKey: "username") }
}
```

---

## Common Runtime Errors

### "Publishing changes from background threads is not allowed"

**Cause:** Updating @Published property from background thread.

**Solution:**
```swift
Task { @MainActor in
    self.data = await fetchData()
}
```

### "Modifying state during view update"

**Cause:** Changing state in view body.

**Solution:** Use `.task`, `.onAppear`, or `.onChange`:

```swift
// ❌ Wrong
var body: some View {
    count += 1 // Modifying state in body!
    return Text("\(count)")
}

// ✅ Correct
var body: some View {
    Text("\(count)")
        .onAppear {
            count += 1
        }
}
```

### "Fatal error: No ObservableObject of type X found"

**Cause:** Missing `.environmentObject()` modifier.

**Solution:**
```swift
ContentView()
    .environmentObject(AppSettings())
```