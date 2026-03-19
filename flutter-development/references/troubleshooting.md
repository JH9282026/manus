# Flutter Troubleshooting

Common issues and solutions.

---

## Build Issues

### "Gradle build failed"
```bash
cd android
./gradlew clean
cd ..
flutter clean
flutter pub get
```

### "CocoaPods not installed"
```bash
sudo gem install cocoapods
cd ios
pod install
```

## Runtime Issues

### "setState() called after dispose()"
**Solution:** Check if widget is mounted:
```dart
if (mounted) {
  setState(() {
    // Update state
  });
}
```

### "RenderBox was not laid out"
**Solution:** Wrap in Expanded or set explicit size:
```dart
Expanded(
  child: ListView(...),
)
```

## Performance Issues

### Jank/Dropped Frames
- Use DevTools Performance view
- Check for expensive build methods
- Implement const constructors
- Use RepaintBoundary for complex widgets
