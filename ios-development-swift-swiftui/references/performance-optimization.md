# Performance Optimization for SwiftUI

Techniques and strategies for building high-performance SwiftUI applications.

---

## Understanding SwiftUI's Rendering Model

SwiftUI uses a declarative approach where views are value types (structs) that describe the UI. When state changes:

1. SwiftUI recomputes the affected view's `body`
2. Performs structural identity and diffing
3. Updates only the changed parts of the UI hierarchy

**Key insight:** SwiftUI is already optimized, but poor state management or heavy computations in view bodies can cause performance issues.

---

## State Management Optimization

### Granular State

**Problem:** Large state objects cause unnecessary recomputations.

```swift
// ❌ Bad: Entire view rebuilds when any property changes
struct UserProfile: View {
    @State private var user = User() // Large object
    
    var body: some View {
        VStack {
            Text(user.name)
            Text(user.email)
            Text(user.bio)
        }
    }
}

// ✅ Good: Only affected views rebuild
struct UserProfile: View {
    @State private var name: String
    @State private var email: String
    @State private var bio: String
    
    var body: some View {
        VStack {
            Text(name)
            Text(email)
            Text(bio)
        }
    }
}
```

### Extract Subviews

**Problem:** Monolithic views rebuild entirely on any state change.

```swift
// ❌ Bad: Entire list rebuilds when count changes
struct ContentView: View {
    @State private var count = 0
    let items: [Item]
    
    var body: some View {
        VStack {
            Text("Count: \(count)")
            Button("Increment") { count += 1 }
            
            ForEach(items) { item in
                // Complex item view
            }
        }
    }
}

// ✅ Good: Only counter rebuilds
struct ContentView: View {
    let items: [Item]
    
    var body: some View {
        VStack {
            CounterView()
            ItemListView(items: items)
        }
    }
}

struct CounterView: View {
    @State private var count = 0
    
    var body: some View {
        VStack {
            Text("Count: \(count)")
            Button("Increment") { count += 1 }
        }
    }
}
```

---

## List and Collection Performance

### Use Lazy Containers

**Always use lazy containers for large datasets:**

```swift
// ❌ Bad: All 10,000 views created immediately
ScrollView {
    VStack {
        ForEach(0..<10000) { i in
            ItemView(index: i)
        }
    }
}

// ✅ Good: Only visible views created
ScrollView {
    LazyVStack {
        ForEach(0..<10000) { i in
            ItemView(index: i)
        }
    }
}
```

### Stable Identifiers

Provide stable, unique identifiers for list items:

```swift
// ❌ Bad: Array index as ID (unstable on reorder/delete)
ForEach(Array(items.enumerated()), id: \.offset) { index, item in
    ItemRow(item: item)
}

// ✅ Good: Stable unique identifier
ForEach(items, id: \.id) { item in
    ItemRow(item: item)
}

// ✅ Also good: Conforming to Identifiable
struct Item: Identifiable {
    let id: UUID
    var name: String
}

ForEach(items) { item in
    ItemRow(item: item)
}
```

### Avoid Expensive Computations in ForEach

```swift
// ❌ Bad: Filtering happens on every render
var body: some View {
    List {
        ForEach(items.filter { $0.isActive }) { item in
            ItemRow(item: item)
        }
    }
}

// ✅ Good: Computed once, cached
var activeItems: [Item] {
    items.filter { $0.isActive }
}

var body: some View {
    List(activeItems) { item in
        ItemRow(item: item)
    }
}
```

---

## View Body Optimization

### Keep Body Lightweight

The `body` property is called frequently. Keep it declarative and avoid:
- Network requests
- File I/O
- Heavy computations
- Database queries

```swift
// ❌ Bad: Heavy computation in body
var body: some View {
    let processedData = heavyComputation(rawData) // Called on every render!
    return Text(processedData)
}

// ✅ Good: Computation in ViewModel or computed property
class ViewModel: ObservableObject {
    @Published var processedData: String = ""
    
    func processData(_ raw: String) {
        processedData = heavyComputation(raw)
    }
}
```

### Use @ViewBuilder Efficiently

```swift
// ❌ Bad: Complex conditional logic in body
var body: some View {
    if condition1 {
        if condition2 {
            ViewA()
        } else {
            ViewB()
        }
    } else {
        ViewC()
    }
}

// ✅ Good: Extract to computed property or method
@ViewBuilder
var contentView: some View {
    switch (condition1, condition2) {
    case (true, true): ViewA()
    case (true, false): ViewB()
    default: ViewC()
    }
}

var body: some View {
    contentView
}
```

---

## Image Optimization

### Async Image Loading

```swift
// ✅ Use AsyncImage for remote images
AsyncImage(url: URL(string: imageURL)) { phase in
    switch phase {
    case .empty:
        ProgressView()
    case .success(let image):
        image
            .resizable()
            .aspectRatio(contentMode: .fill)
    case .failure:
        Image(systemName: "photo")
    @unknown default:
        EmptyView()
    }
}
.frame(width: 100, height: 100)
```

### Image Resizing

```swift
// ❌ Bad: Loading full-resolution image
Image("largePhoto")
    .resizable()
    .frame(width: 50, height: 50)

// ✅ Good: Resize image asset or use thumbnail
Image("largePhoto")
    .resizable()
    .renderingMode(.original)
    .interpolation(.high)
    .frame(width: 50, height: 50)
```

**Best practice:** Provide multiple image sizes in asset catalog (@1x, @2x, @3x) and use appropriate resolution.

---

## Animation Performance

### Limit Simultaneous Animations

Too many concurrent animations can drop frame rate below 60fps.

```swift
// ❌ Bad: Animating 100 items simultaneously
ForEach(items) { item in
    ItemView(item: item)
        .scaleEffect(isAnimating ? 1.2 : 1.0)
}
.animation(.spring(), value: isAnimating)

// ✅ Good: Stagger animations or limit scope
ForEach(Array(items.prefix(10).enumerated()), id: \.element.id) { index, item in
    ItemView(item: item)
        .scaleEffect(isAnimating ? 1.2 : 1.0)
        .animation(.spring().delay(Double(index) * 0.05), value: isAnimating)
}
```

### Use Appropriate Animation Curves

```swift
// Fast, simple animations
.animation(.linear(duration: 0.2), value: state)

// Smooth, natural animations
.animation(.easeInOut(duration: 0.3), value: state)

// Bouncy, playful animations (more expensive)
.animation(.spring(response: 0.3, dampingFraction: 0.7), value: state)
```

---

## Profiling with Instruments

### Time Profiler

1. Product → Profile (⌘I) in Xcode
2. Select "Time Profiler"
3. Record while using the app
4. Look for:
   - High CPU usage in view body computations
   - Frequent recomputations of the same view
   - Expensive operations on main thread

### SwiftUI View Body Profiling

1. Product → Profile
2. Select "SwiftUI" template
3. Analyze:
   - View body invocation count
   - Time spent in body computation
   - Unnecessary view updates

### Allocations Instrument

1. Product → Profile
2. Select "Allocations"
3. Monitor:
   - Memory growth over time
   - Leaked objects
   - Excessive allocations in loops

---

## Memory Management

### Avoid Retain Cycles

```swift
// ❌ Bad: Strong reference cycle
class ViewModel: ObservableObject {
    var onComplete: (() -> Void)?
    
    func setup(view: SomeView) {
        onComplete = {
            view.dismiss() // Strong reference to view
        }
    }
}

// ✅ Good: Weak capture
class ViewModel: ObservableObject {
    var onComplete: (() -> Void)?
    
    func setup(view: SomeView) {
        onComplete = { [weak view] in
            view?.dismiss()
        }
    }
}
```

### Task Cancellation

```swift
// ✅ Use .task modifier for automatic cancellation
var body: some View {
    ContentView()
        .task {
            // Automatically cancelled when view disappears
            await loadData()
        }
}

// ✅ Manual task management
struct DataView: View {
    @State private var task: Task<Void, Never>?
    
    var body: some View {
        ContentView()
            .onAppear {
                task = Task {
                    await loadData()
                }
            }
            .onDisappear {
                task?.cancel()
            }
    }
}
```

---

## Best Practices Summary

1. **Use lazy containers** for lists and grids with more than ~20 items
2. **Extract subviews** to limit rebuild scope
3. **Keep state granular** to minimize unnecessary updates
4. **Avoid heavy work in view body** - move to ViewModels or background tasks
5. **Provide stable identifiers** for ForEach
6. **Profile regularly** with Instruments to identify bottlenecks
7. **Use .task modifier** for lifecycle-aware async work
8. **Optimize images** with appropriate resolutions and async loading
9. **Limit concurrent animations** to maintain 60fps
10. **Test on real devices** - simulators don't reflect actual performance