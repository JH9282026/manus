# Flutter Widget Catalog

Common widgets and their usage.

---

## Layout Widgets

### Container
```dart
Container(
  padding: EdgeInsets.all(16),
  margin: EdgeInsets.symmetric(vertical: 8),
  decoration: BoxDecoration(
    color: Colors.blue,
    borderRadius: BorderRadius.circular(8),
  ),
  child: Text('Hello'),
)
```

### Row and Column
```dart
Row(
  mainAxisAlignment: MainAxisAlignment.spaceBetween,
  crossAxisAlignment: CrossAxisAlignment.center,
  children: [
    Icon(Icons.star),
    Text('Rating'),
    Text('4.5'),
  ],
)
```

### ListView
```dart
ListView.builder(
  itemCount: items.length,
  itemBuilder: (context, index) {
    return ListTile(
      title: Text(items[index].title),
      subtitle: Text(items[index].subtitle),
    );
  },
)
```
