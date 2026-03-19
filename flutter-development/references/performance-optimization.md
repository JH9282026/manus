# Flutter Performance Optimization

Techniques for high-performance Flutter apps.

---

## Build Optimization

### Use const Constructors
```dart
// ✅ Good
const Text('Hello');
const Padding(padding: EdgeInsets.all(8));

// ❌ Bad
Text('Hello');
Padding(padding: EdgeInsets.all(8));
```

### Extract Widgets
```dart
// ✅ Good: Separate widget
class HeaderWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Text('Header');
  }
}

// ❌ Bad: Inline
Widget build(BuildContext context) {
  return Column(
    children: [
      Text('Header'), // Rebuilds with parent
    ],
  );
}
```

## List Performance

### Use ListView.builder
```dart
ListView.builder(
  itemCount: 1000,
  itemBuilder: (context, index) {
    return ListTile(title: Text('Item $index'));
  },
)
```

### Add Keys
```dart
ListView.builder(
  itemBuilder: (context, index) {
    return ListTile(
      key: ValueKey(items[index].id),
      title: Text(items[index].title),
    );
  },
)
```

## Image Optimization

```dart
Image.network(
  url,
  cacheWidth: 200,
  cacheHeight: 200,
)
```
