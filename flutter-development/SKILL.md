---
name: flutter-development
description: "Build cross-platform mobile, web, and desktop applications using Flutter and Dart with declarative UI, widget composition, and native performance. Use for: creating cross-platform apps for iOS/Android/Web/Desktop, implementing Flutter widgets and layouts, managing state with Provider/Riverpod/BLoC, building custom animations, integrating with platform APIs, optimizing performance, and deploying to multiple platforms from single codebase."
---

# Flutter Development

Build beautiful, natively compiled applications for mobile, web, and desktop from a single codebase using Flutter and Dart.

## Overview

Flutter is Google's UI toolkit for building natively compiled applications across mobile, web, and desktop from a single codebase. It uses the Dart programming language and provides a rich set of pre-designed widgets following Material Design and Cupertino (iOS) guidelines. This skill covers Flutter development patterns, state management, performance optimization, and multi-platform deployment.

## Development Environment Setup

| Component | Requirement | Notes |
|-----------|-------------|-------|
| Flutter SDK | 3.16+ (stable channel) | Includes Dart SDK |
| IDE | VS Code or Android Studio | With Flutter/Dart plugins |
| iOS Development | macOS, Xcode 15+ | Required for iOS builds |
| Android Development | Android Studio, JDK 17 | Required for Android builds |
| Chrome | Latest | For web development |

**Setup Commands:**
```bash
# Install Flutter
# Download from flutter.dev

# Verify installation
flutter doctor

# Create new project
flutter create my_app

# Run app
flutter run
```

## Core Flutter Concepts

### Everything is a Widget

Flutter's UI is built entirely from widgets - immutable descriptions of part of the user interface.

```dart
class MyWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Container(
      child: Text('Hello Flutter'),
    );
  }
}
```

### Widget Types

| Type | Use Case | Rebuilds |
|------|----------|----------|
| StatelessWidget | Immutable UI | Never |
| StatefulWidget | Mutable state | When setState() called |
| InheritedWidget | Share data down tree | When data changes |

### Widget Tree

Flutter builds a tree of widgets that describes the UI. When state changes, Flutter rebuilds the affected parts of the tree.

## State Management

### Built-in State Management

```dart
class CounterWidget extends StatefulWidget {
  @override
  _CounterWidgetState createState() => _CounterWidgetState();
}

class _CounterWidgetState extends State<CounterWidget> {
  int _counter = 0;
  
  void _increment() {
    setState(() {
      _counter++;
    });
  }
  
  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Text('Count: $_counter'),
        ElevatedButton(
          onPressed: _increment,
          child: Text('Increment'),
        ),
      ],
    );
  }
}
```

### State Management Solutions

| Solution | Complexity | Use Case | Recommendation |
|----------|------------|----------|----------------|
| setState | Low | Local widget state | Simple apps |
| Provider | Medium | App-wide state | Beginners, simple apps |
| Riverpod | Medium | Modern reactive state | New projects (2026 default) |
| BLoC | High | Enterprise apps | Large teams, strict patterns |
| GetX | Low | All-in-one | Not recommended (maintenance risks) |
| Signals | Medium | Performance-critical | Real-time apps |

### Riverpod Example (Recommended)

```dart
final counterProvider = StateProvider<int>((ref) => 0);

class CounterWidget extends ConsumerWidget {
  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final count = ref.watch(counterProvider);
    
    return Column(
      children: [
        Text('Count: $count'),
        ElevatedButton(
          onPressed: () => ref.read(counterProvider.notifier).state++,
          child: Text('Increment'),
        ),
      ],
    );
  }
}
```

## Layout and Widgets

### Common Layout Widgets

| Widget | Purpose |
|--------|---------|
| Container | Box model (padding, margin, decoration) |
| Row | Horizontal layout |
| Column | Vertical layout |
| Stack | Overlapping widgets |
| ListView | Scrollable list |
| GridView | Grid layout |
| Expanded | Fill available space |
| Flexible | Flexible space allocation |

### Material Design Widgets

- Scaffold: App structure (AppBar, Body, FAB)
- AppBar: Top app bar
- BottomNavigationBar: Bottom navigation
- FloatingActionButton: FAB
- Card: Material card
- Dialog: Modal dialogs

### Cupertino (iOS) Widgets

- CupertinoPageScaffold
- CupertinoNavigationBar
- CupertinoTabScaffold
- CupertinoButton

## Navigation

### Navigator 1.0 (Imperative)

```dart
// Push
Navigator.push(
  context,
  MaterialPageRoute(builder: (context) => DetailScreen()),
);

// Pop
Navigator.pop(context);

// Named routes
Navigator.pushNamed(context, '/details');
```

### Navigator 2.0 (Declarative)

```dart
MaterialApp.router(
  routerConfig: GoRouter(
    routes: [
      GoRoute(
        path: '/',
        builder: (context, state) => HomeScreen(),
      ),
      GoRoute(
        path: '/details/:id',
        builder: (context, state) {
          final id = state.pathParameters['id'];
          return DetailScreen(id: id);
        },
      ),
    ],
  ),
);

// Navigate
context.go('/details/123');
```

## Performance Optimization

### Build Method Optimization

```dart
// ✅ Good: Extract widgets
class MyWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        HeaderWidget(),
        ContentWidget(),
      ],
    );
  }
}

// ❌ Bad: Everything in one build
class MyWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        // 100 lines of nested widgets
      ],
    );
  }
}
```

### Const Constructors

```dart
// ✅ Use const for immutable widgets
const Text('Hello');
const Icon(Icons.home);

// Reduces rebuilds
```

### ListView.builder for Large Lists

```dart
ListView.builder(
  itemCount: items.length,
  itemBuilder: (context, index) {
    return ListTile(title: Text(items[index]));
  },
);
```

## Animations

### Implicit Animations

```dart
AnimatedContainer(
  duration: Duration(seconds: 1),
  width: _isExpanded ? 200 : 100,
  height: _isExpanded ? 200 : 100,
  color: _isExpanded ? Colors.blue : Colors.red,
);
```

### Explicit Animations

```dart
class MyAnimation extends StatefulWidget {
  @override
  _MyAnimationState createState() => _MyAnimationState();
}

class _MyAnimationState extends State<MyAnimation>
    with SingleTickerProviderStateMixin {
  late AnimationController _controller;
  late Animation<double> _animation;
  
  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      duration: Duration(seconds: 2),
      vsync: this,
    );
    _animation = Tween<double>(begin: 0, end: 300).animate(_controller);
    _controller.forward();
  }
  
  @override
  Widget build(BuildContext context) {
    return AnimatedBuilder(
      animation: _animation,
      builder: (context, child) {
        return Container(width: _animation.value, height: _animation.value);
      },
    );
  }
  
  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }
}
```

## Platform Integration

### Platform Channels

```dart
static const platform = MethodChannel('com.example.app/battery');

Future<int> getBatteryLevel() async {
  try {
    final int result = await platform.invokeMethod('getBatteryLevel');
    return result;
  } catch (e) {
    return -1;
  }
}
```

### Platform-Specific Code

```dart
import 'dart:io' show Platform;

if (Platform.isIOS) {
  // iOS-specific code
} else if (Platform.isAndroid) {
  // Android-specific code
}
```

## Testing

### Unit Tests

```dart
test('Counter increments', () {
  final counter = Counter();
  counter.increment();
  expect(counter.value, 1);
});
```

### Widget Tests

```dart
testWidgets('Counter increments smoke test', (WidgetTester tester) async {
  await tester.pumpWidget(MyApp());
  
  expect(find.text('0'), findsOneWidget);
  
  await tester.tap(find.byIcon(Icons.add));
  await tester.pump();
  
  expect(find.text('1'), findsOneWidget);
});
```

### Integration Tests

```dart
void main() {
  IntegrationTestWidgetsFlutterBinding.ensureInitialized();
  
  testWidgets('Full app test', (tester) async {
    app.main();
    await tester.pumpAndSettle();
    
    // Test user flows
  });
}
```

## Deployment

### iOS Deployment
1. Configure signing in Xcode
2. Build release: `flutter build ios --release`
3. Archive and upload to App Store Connect

### Android Deployment
1. Generate signing key
2. Configure `android/app/build.gradle`
3. Build release: `flutter build appbundle --release`
4. Upload to Google Play Console

### Web Deployment
```bash
flutter build web --release
# Deploy contents of build/web to hosting
```

## Best Practices

- Use const constructors wherever possible
- Extract widgets to keep build methods small
- Implement proper error handling
- Use async/await for asynchronous operations
- Follow Effective Dart style guide
- Implement proper accessibility
- Test on real devices
- Use DevTools for debugging and profiling

## Using the Reference Files

**`/references/widget-catalog.md`** — Read when looking for specific widgets, understanding widget properties, or implementing common UI patterns.

**`/references/state-management-guide.md`** — Read when choosing a state management solution, implementing Provider/Riverpod/BLoC, or managing complex state.

**`/references/performance-optimization.md`** — Read when optimizing app performance, reducing jank, or profiling with DevTools.

**`/references/troubleshooting.md`** — Read when encountering build errors, runtime issues, or platform-specific problems.
- Use async/await for asynchronous operations
- Follow Effective Dart style guide
- Implement proper accessibility
- Test on real devices
- Use DevTools for debugging and profiling

