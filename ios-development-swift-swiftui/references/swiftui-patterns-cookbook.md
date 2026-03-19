# SwiftUI Patterns Cookbook

Common patterns and code examples for SwiftUI development.

---

## State Management Patterns

### Observable Pattern (iOS 17+)

```swift
import Observation

@Observable
class UserViewModel {
    var username: String = ""
    var isLoggedIn: Bool = false
    
    func login() async {
        // Async login logic
        isLoggedIn = true
    }
}

struct ProfileView: View {
    @State private var viewModel = UserViewModel()
    
    var body: some View {
        VStack {
            Text(viewModel.username)
            Button("Login") {
                Task {
                    await viewModel.login()
                }
            }
        }
    }
}
```

### ObservableObject Pattern (Legacy)

```swift
class CounterViewModel: ObservableObject {
    @Published var count: Int = 0
    
    func increment() {
        count += 1
    }
}

struct CounterView: View {
    @StateObject private var viewModel = CounterViewModel()
    
    var body: some View {
        VStack {
            Text("Count: \(viewModel.count)")
            Button("Increment", action: viewModel.increment)
        }
    }
}
```

### Binding Pattern

```swift
struct ParentView: View {
    @State private var isOn: Bool = false
    
    var body: some View {
        ToggleView(isOn: $isOn)
    }
}

struct ToggleView: View {
    @Binding var isOn: Bool
    
    var body: some View {
        Toggle("Switch", isOn: $isOn)
    }
}
```

### Environment Object Pattern

```swift
class AppSettings: ObservableObject {
    @Published var theme: Theme = .light
}

@main
struct MyApp: App {
    @StateObject private var settings = AppSettings()
    
    var body: some Scene {
        WindowGroup {
            ContentView()
                .environmentObject(settings)
        }
    }
}

struct SettingsView: View {
    @EnvironmentObject var settings: AppSettings
    
    var body: some View {
        Picker("Theme", selection: $settings.theme) {
            // Picker options
        }
    }
}
```

---

## Navigation Patterns

### NavigationStack with Value-Based Navigation

```swift
enum Destination: Hashable {
    case detail(Item)
    case settings
}

struct ContentView: View {
    @State private var path = NavigationPath()
    
    var body: some View {
        NavigationStack(path: $path) {
            List(items) { item in
                NavigationLink(value: item) {
                    ItemRow(item: item)
                }
            }
            .navigationDestination(for: Item.self) { item in
                DetailView(item: item)
            }
            .navigationDestination(for: Destination.self) { destination in
                switch destination {
                case .detail(let item):
                    DetailView(item: item)
                case .settings:
                    SettingsView()
                }
            }
        }
    }
}
```

### Programmatic Navigation

```swift
struct RootView: View {
    @State private var path: [Route] = []
    
    var body: some View {
        NavigationStack(path: $path) {
            Button("Go to Detail") {
                path.append(.detail)
            }
            .navigationDestination(for: Route.self) { route in
                routeView(for: route)
            }
        }
    }
    
    func routeView(for route: Route) -> some View {
        switch route {
        case .detail:
            return AnyView(DetailView())
        case .settings:
            return AnyView(SettingsView())
        }
    }
}
```

### Sheet Presentation

```swift
struct MainView: View {
    @State private var showingSheet = false
    @State private var selectedItem: Item?
    
    var body: some View {
        Button("Show Sheet") {
            showingSheet = true
        }
        .sheet(isPresented: $showingSheet) {
            SheetView()
        }
        .sheet(item: $selectedItem) { item in
            DetailSheet(item: item)
        }
    }
}
```

---

## List and Collection Patterns

### LazyVStack with Performance Optimization

```swift
struct OptimizedListView: View {
    let items: [Item]
    
    var body: some View {
        ScrollView {
            LazyVStack(spacing: 12) {
                ForEach(items) { item in
                    ItemRow(item: item)
                        .id(item.id) // Stable identifier
                }
            }
            .padding()
        }
    }
}
```

### List with Swipe Actions

```swift
struct SwipeableList: View {
    @State private var items: [Item]
    
    var body: some View {
        List {
            ForEach(items) { item in
                ItemRow(item: item)
                    .swipeActions(edge: .trailing) {
                        Button(role: .destructive) {
                            delete(item)
                        } label: {
                            Label("Delete", systemImage: "trash")
                        }
                    }
                    .swipeActions(edge: .leading) {
                        Button {
                            favorite(item)
                        } label: {
                            Label("Favorite", systemImage: "star")
                        }
                        .tint(.yellow)
                    }
            }
        }
    }
}
```

### Searchable List

```swift
struct SearchableView: View {
    @State private var searchText = ""
    let items: [Item]
    
    var filteredItems: [Item] {
        if searchText.isEmpty {
            return items
        }
        return items.filter { $0.name.localizedCaseInsensitiveContains(searchText) }
    }
    
    var body: some View {
        NavigationStack {
            List(filteredItems) { item in
                ItemRow(item: item)
            }
            .searchable(text: $searchText, prompt: "Search items")
            .navigationTitle("Items")
        }
    }
}
```

---

## Async/Await Patterns

### Task Modifier for Async Loading

```swift
struct AsyncDataView: View {
    @State private var data: [Item] = []
    @State private var isLoading = false
    @State private var error: Error?
    
    var body: some View {
        Group {
            if isLoading {
                ProgressView()
            } else if let error = error {
                ErrorView(error: error)
            } else {
                List(data) { item in
                    ItemRow(item: item)
                }
            }
        }
        .task {
            await loadData()
        }
    }
    
    func loadData() async {
        isLoading = true
        defer { isLoading = false }
        
        do {
            data = try await APIService.fetchItems()
        } catch {
            self.error = error
        }
    }
}
```

### Refreshable Content

```swift
struct RefreshableList: View {
    @State private var items: [Item] = []
    
    var body: some View {
        List(items) { item in
            ItemRow(item: item)
        }
        .refreshable {
            await loadItems()
        }
    }
    
    func loadItems() async {
        items = try? await APIService.fetchItems()
    }
}
```

---

## Custom ViewModifiers

### Reusable Card Style

```swift
struct CardModifier: ViewModifier {
    func body(content: Content) -> some View {
        content
            .padding()
            .background(Color(.systemBackground))
            .cornerRadius(12)
            .shadow(color: .black.opacity(0.1), radius: 5, x: 0, y: 2)
    }
}

extension View {
    func cardStyle() -> some View {
        modifier(CardModifier())
    }
}

// Usage
Text("Hello")
    .cardStyle()
```

### Conditional Modifier

```swift
extension View {
    @ViewBuilder
    func `if`<Transform: View>(
        _ condition: Bool,
        transform: (Self) -> Transform
    ) -> some View {
        if condition {
            transform(self)
        } else {
            self
        }
    }
}

// Usage
Text("Hello")
    .if(isHighlighted) { view in
        view.foregroundColor(.red)
    }
```

---

## Form and Input Patterns

### Validated Form

```swift
struct RegistrationForm: View {
    @State private var email = ""
    @State private var password = ""
    @State private var confirmPassword = ""
    
    var isValid: Bool {
        !email.isEmpty &&
        password.count >= 8 &&
        password == confirmPassword
    }
    
    var body: some View {
        Form {
            Section("Account") {
                TextField("Email", text: $email)
                    .textContentType(.emailAddress)
                    .keyboardType(.emailAddress)
                    .autocapitalization(.none)
                
                SecureField("Password", text: $password)
                    .textContentType(.newPassword)
                
                SecureField("Confirm Password", text: $confirmPassword)
                    .textContentType(.newPassword)
            }
            
            Section {
                Button("Register") {
                    register()
                }
                .disabled(!isValid)
            }
        }
    }
}
```

---

## Animation Patterns

### Implicit Animation

```swift
struct AnimatedButton: View {
    @State private var isExpanded = false
    
    var body: some View {
        RoundedRectangle(cornerRadius: isExpanded ? 50 : 8)
            .fill(Color.blue)
            .frame(width: isExpanded ? 200 : 100, height: 50)
            .animation(.spring(response: 0.3), value: isExpanded)
            .onTapGesture {
                isExpanded.toggle()
            }
    }
}
```

### Explicit Animation with Transaction

```swift
struct ExplicitAnimationView: View {
    @State private var scale: CGFloat = 1.0
    
    var body: some View {
        Circle()
            .scaleEffect(scale)
            .onTapGesture {
                withAnimation(.easeInOut(duration: 0.5)) {
                    scale = scale == 1.0 ? 1.5 : 1.0
                }
            }
    }
}
```

---

## SwiftData Integration

### Model Definition

```swift
import SwiftData

@Model
class Task {
    var title: String
    var isCompleted: Bool
    var createdAt: Date
    
    @Relationship(deleteRule: .cascade)
    var subtasks: [Subtask]
    
    init(title: String, isCompleted: Bool = false) {
        self.title = title
        self.isCompleted = isCompleted
        self.createdAt = Date()
        self.subtasks = []
    }
}
```

### Query and CRUD Operations

```swift
struct TaskListView: View {
    @Environment(\.modelContext) private var modelContext
    @Query(sort: \Task.createdAt, order: .reverse) private var tasks: [Task]
    
    var body: some View {
        List {
            ForEach(tasks) { task in
                TaskRow(task: task)
            }
            .onDelete(perform: deleteTasks)
        }
        .toolbar {
            Button("Add", systemImage: "plus") {
                addTask()
            }
        }
    }
    
    func addTask() {
        let newTask = Task(title: "New Task")
        modelContext.insert(newTask)
    }
    
    func deleteTasks(at offsets: IndexSet) {
        for index in offsets {
            modelContext.delete(tasks[index])
        }
    }
}
```

### Filtered Query

```swift
struct CompletedTasksView: View {
    @Query(filter: #Predicate<Task> { $0.isCompleted })
    private var completedTasks: [Task]
    
    var body: some View {
        List(completedTasks) { task in
            TaskRow(task: task)
        }
    }
}
```