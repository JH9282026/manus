# Advanced SwiftUI Techniques

Advanced patterns and features for sophisticated SwiftUI applications.

---

## Preference Keys

Preference keys allow child views to pass data up to ancestor views, reversing the normal data flow.

### Custom Preference Key

```swift
struct HeightPreferenceKey: PreferenceKey {
    static var defaultValue: CGFloat = 0
    
    static func reduce(value: inout CGFloat, nextValue: () -> CGFloat) {
        value = max(value, nextValue())
    }
}

struct ChildView: View {
    var body: some View {
        Text("Hello")
            .background(
                GeometryReader { geometry in
                    Color.clear
                        .preference(key: HeightPreferenceKey.self, value: geometry.size.height)
                }
            )
    }
}

struct ParentView: View {
    @State private var childHeight: CGFloat = 0
    
    var body: some View {
        VStack {
            ChildView()
            Text("Child height: \(childHeight)")
        }
        .onPreferenceChange(HeightPreferenceKey.self) { value in
            childHeight = value
        }
    }
}
```

### Anchor Preferences for Layout Coordination

```swift
struct BoundsPreferenceKey: PreferenceKey {
    static var defaultValue: Anchor<CGRect>?
    
    static func reduce(value: inout Anchor<CGRect>?, nextValue: () -> Anchor<CGRect>?) {
        value = value ?? nextValue()
    }
}

struct OverlayExample: View {
    var body: some View {
        VStack {
            Text("Target")
                .anchorPreference(key: BoundsPreferenceKey.self, value: .bounds) { $0 }
        }
        .overlayPreferenceValue(BoundsPreferenceKey.self) { preferences in
            GeometryReader { geometry in
                if let anchor = preferences {
                    let rect = geometry[anchor]
                    Rectangle()
                        .stroke(Color.red, lineWidth: 2)
                        .frame(width: rect.width, height: rect.height)
                        .offset(x: rect.minX, y: rect.minY)
                }
            }
        }
    }
}
```

---

## Geometry Reader Advanced Usage

### Scroll Position Tracking

```swift
struct ScrollPositionView: View {
    @State private var scrollOffset: CGFloat = 0
    
    var body: some View {
        ScrollView {
            VStack(spacing: 0) {
                GeometryReader { geometry in
                    Color.clear
                        .preference(
                            key: ScrollOffsetPreferenceKey.self,
                            value: geometry.frame(in: .named("scroll")).minY
                        )
                }
                .frame(height: 0)
                
                ForEach(0..<50) { i in
                    Text("Item \(i)")
                        .frame(height: 50)
                }
            }
        }
        .coordinateSpace(name: "scroll")
        .onPreferenceChange(ScrollOffsetPreferenceKey.self) { value in
            scrollOffset = value
        }
        .overlay(
            Text("Offset: \(scrollOffset, specifier: "%.1f")")
                .padding(),
            alignment: .top
        )
    }
}

struct ScrollOffsetPreferenceKey: PreferenceKey {
    static var defaultValue: CGFloat = 0
    static func reduce(value: inout CGFloat, nextValue: () -> CGFloat) {
        value = nextValue()
    }
}
```

### Parallax Effect

```swift
struct ParallaxView: View {
    var body: some View {
        ScrollView {
            LazyVStack(spacing: 0) {
                ForEach(0..<10) { index in
                    GeometryReader { geometry in
                        let offset = geometry.frame(in: .global).minY
                        
                        Image("background\(index)")
                            .resizable()
                            .aspectRatio(contentMode: .fill)
                            .frame(width: geometry.size.width, height: 300)
                            .offset(y: offset * 0.5) // Parallax factor
                            .clipped()
                    }
                    .frame(height: 300)
                }
            }
        }
    }
}
```

---

## Custom Layout Protocol (iOS 16+)

### Creating a Custom Layout

```swift
struct FlowLayout: Layout {
    var spacing: CGFloat = 8
    
    func sizeThatFits(proposal: ProposedViewSize, subviews: Subviews, cache: inout ()) -> CGSize {
        let rows = computeRows(proposal: proposal, subviews: subviews)
        let width = proposal.width ?? 0
        let height = rows.reduce(0) { $0 + $1.height + spacing } - spacing
        return CGSize(width: width, height: height)
    }
    
    func placeSubviews(in bounds: CGRect, proposal: ProposedViewSize, subviews: Subviews, cache: inout ()) {
        let rows = computeRows(proposal: proposal, subviews: subviews)
        var y = bounds.minY
        
        for row in rows {
            var x = bounds.minX
            
            for index in row.indices {
                let subview = subviews[index]
                let size = subview.sizeThatFits(.unspecified)
                subview.place(at: CGPoint(x: x, y: y), proposal: .unspecified)
                x += size.width + spacing
            }
            
            y += row.height + spacing
        }
    }
    
    private func computeRows(proposal: ProposedViewSize, subviews: Subviews) -> [(indices: [Int], height: CGFloat)] {
        var rows: [(indices: [Int], height: CGFloat)] = []
        var currentRow: [Int] = []
        var currentX: CGFloat = 0
        var currentHeight: CGFloat = 0
        let maxWidth = proposal.width ?? .infinity
        
        for (index, subview) in subviews.enumerated() {
            let size = subview.sizeThatFits(.unspecified)
            
            if currentX + size.width > maxWidth && !currentRow.isEmpty {
                rows.append((currentRow, currentHeight))
                currentRow = []
                currentX = 0
                currentHeight = 0
            }
            
            currentRow.append(index)
            currentX += size.width + spacing
            currentHeight = max(currentHeight, size.height)
        }
        
        if !currentRow.isEmpty {
            rows.append((currentRow, currentHeight))
        }
        
        return rows
    }
}

// Usage
FlowLayout(spacing: 12) {
    ForEach(tags, id: \.self) { tag in
        Text(tag)
            .padding(.horizontal, 12)
            .padding(.vertical, 6)
            .background(Color.blue)
            .cornerRadius(8)
    }
}
```

---

## View Transitions

### Custom Transitions

```swift
extension AnyTransition {
    static var slideAndFade: AnyTransition {
        .asymmetric(
            insertion: .move(edge: .trailing).combined(with: .opacity),
            removal: .move(edge: .leading).combined(with: .opacity)
        )
    }
    
    static func pivot(anchor: UnitPoint) -> AnyTransition {
        .modifier(
            active: PivotModifier(anchor: anchor, angle: .degrees(90)),
            identity: PivotModifier(anchor: anchor, angle: .zero)
        )
    }
}

struct PivotModifier: ViewModifier {
    let anchor: UnitPoint
    let angle: Angle
    
    func body(content: Content) -> some View {
        content
            .rotationEffect(angle, anchor: anchor)
            .opacity(angle == .zero ? 1 : 0)
    }
}

// Usage
if showView {
    ContentView()
        .transition(.slideAndFade)
}
```

### Matched Geometry Effect

```swift
struct MatchedGeometryExample: View {
    @State private var isExpanded = false
    @Namespace private var animation
    
    var body: some View {
        VStack {
            if isExpanded {
                ExpandedView()
                    .matchedGeometryEffect(id: "card", in: animation)
            } else {
                CompactView()
                    .matchedGeometryEffect(id: "card", in: animation)
            }
        }
        .onTapGesture {
            withAnimation(.spring(response: 0.6, dampingFraction: 0.8)) {
                isExpanded.toggle()
            }
        }
    }
}
```

---

## Environment and Dependency Injection

### Custom Environment Values

```swift
private struct ThemeKey: EnvironmentKey {
    static let defaultValue: Theme = .light
}

extension EnvironmentValues {
    var theme: Theme {
        get { self[ThemeKey.self] }
        set { self[ThemeKey.self] = newValue }
    }
}

extension View {
    func theme(_ theme: Theme) -> some View {
        environment(\.theme, theme)
    }
}

// Usage
ContentView()
    .theme(.dark)

struct SomeView: View {
    @Environment(\.theme) var theme
    
    var body: some View {
        Text("Hello")
            .foregroundColor(theme.textColor)
    }
}
```

### Dependency Injection Pattern

```swift
protocol DataService {
    func fetchData() async throws -> [Item]
}

class ProductionDataService: DataService {
    func fetchData() async throws -> [Item] {
        // Real API call
    }
}

class MockDataService: DataService {
    func fetchData() async throws -> [Item] {
        // Mock data
    }
}

private struct DataServiceKey: EnvironmentKey {
    static let defaultValue: DataService = ProductionDataService()
}

extension EnvironmentValues {
    var dataService: DataService {
        get { self[DataServiceKey.self] }
        set { self[DataServiceKey.self] = newValue }
    }
}

// In App
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
                .environment(\.dataService, ProductionDataService())
        }
    }
}

// In Preview
#Preview {
    ContentView()
        .environment(\.dataService, MockDataService())
}
```

---

## Advanced Gestures

### Simultaneous Gestures

```swift
struct SimultaneousGestureView: View {
    @State private var offset = CGSize.zero
    @State private var scale: CGFloat = 1.0
    
    var body: some View {
        Rectangle()
            .fill(Color.blue)
            .frame(width: 200, height: 200)
            .scaleEffect(scale)
            .offset(offset)
            .gesture(
                SimultaneousGesture(
                    DragGesture()
                        .onChanged { value in
                            offset = value.translation
                        },
                    MagnificationGesture()
                        .onChanged { value in
                            scale = value
                        }
                )
            )
    }
}
```

### Gesture Sequencing

```swift
struct SequencedGestureView: View {
    @State private var isLongPressing = false
    @State private var offset = CGSize.zero
    
    var longPressThenDrag: some Gesture {
        SequenceGesture(
            LongPressGesture(minimumDuration: 0.5)
                .onEnded { _ in
                    isLongPressing = true
                },
            DragGesture()
                .onChanged { value in
                    offset = value.translation
                }
                .onEnded { _ in
                    isLongPressing = false
                    offset = .zero
                }
        )
    }
    
    var body: some View {
        Circle()
            .fill(isLongPressing ? Color.red : Color.blue)
            .frame(width: 100, height: 100)
            .offset(offset)
            .gesture(longPressThenDrag)
    }
}
```

---

## Canvas and TimelineView

### Custom Drawing with Canvas

```swift
struct WaveformView: View {
    let samples: [Float]
    
    var body: some View {
        Canvas { context, size in
            let path = createWaveformPath(samples: samples, size: size)
            context.stroke(path, with: .color(.blue), lineWidth: 2)
        }
    }
    
    func createWaveformPath(samples: [Float], size: CGSize) -> Path {
        var path = Path()
        let stepX = size.width / CGFloat(samples.count)
        
        for (index, sample) in samples.enumerated() {
            let x = CGFloat(index) * stepX
            let y = size.height / 2 + CGFloat(sample) * size.height / 2
            
            if index == 0 {
                path.move(to: CGPoint(x: x, y: y))
            } else {
                path.addLine(to: CGPoint(x: x, y: y))
            }
        }
        
        return path
    }
}
```

### Animated Timeline

```swift
struct AnimatedClockView: View {
    var body: some View {
        TimelineView(.animation) { timeline in
            Canvas { context, size in
                let now = timeline.date.timeIntervalSinceReferenceDate
                let angle = Angle.degrees(now.remainder(dividingBy: 60) * 6)
                
                var path = Path()
                path.move(to: CGPoint(x: size.width / 2, y: size.height / 2))
                path.addLine(to: CGPoint(
                    x: size.width / 2 + cos(angle.radians - .pi / 2) * 80,
                    y: size.height / 2 + sin(angle.radians - .pi / 2) * 80
                ))
                
                context.stroke(path, with: .color(.blue), lineWidth: 3)
            }
        }
        .frame(width: 200, height: 200)
    }
}
```