# React Native Troubleshooting

Common issues and solutions.

---

## Build Issues

### Metro Bundler Cache Issues
```bash
npx react-native start --reset-cache
```

### iOS Pod Install Issues
```bash
cd ios && pod deintegrate && pod install && cd ..
```

### Android Gradle Issues
```bash
cd android && ./gradlew clean && cd ..
```

## Runtime Issues

### "Invariant Violation: requireNativeComponent"
**Solution:** Link native dependencies:
```bash
npx react-native link
```

### Red Screen Errors
- Check console for detailed error messages
- Verify all imports are correct
- Check for typos in component names
- Ensure all dependencies are installed

## Performance Issues

### Slow Navigation
- Use `React.memo` for expensive components
- Implement proper `shouldComponentUpdate`
- Avoid inline functions in render

### Memory Leaks
- Clean up subscriptions in `useEffect` cleanup
- Remove event listeners on unmount
- Cancel pending async operations
