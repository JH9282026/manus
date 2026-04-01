---
name: react-native-development
description: "Build cross-platform mobile applications for iOS and Android using React Native with JavaScript/TypeScript, component-based architecture, and native module integration. Use for: creating cross-platform mobile apps, implementing React patterns (hooks, context, state management), integrating native modules, optimizing performance, handling navigation with React Navigation, managing state with Redux/MobX/Zustand, building for both iOS and Android from single codebase, and implementing platform-specific code when needed."
---

# React Native Development

Build cross-platform mobile applications for iOS and Android using React Native and JavaScript/TypeScript.

## Overview

React Native is a framework for building native mobile apps using React and JavaScript. It allows you to write code once and deploy to both iOS and Android, while maintaining native performance and access to platform APIs. This skill covers React Native development patterns, state management, navigation, performance optimization, and native module integration.

## Development Environment Setup

| Component | Requirement | Notes |
|-----------|-------------|-------|
| Node.js | 18.x or later | LTS version recommended |
| Package Manager | npm, yarn, or pnpm | yarn recommended for React Native |
| React Native CLI | Latest | `npx react-native` or global install |
| iOS Development | macOS, Xcode 14+ | Required for iOS builds |
| Android Development | Android Studio, JDK 17 | Required for Android builds |
| Watchman | Latest (macOS/Linux) | File watching for hot reload |

**Setup Commands:**
```bash
# Create new project
npx react-native@latest init MyApp

# Run on iOS
npx react-native run-ios

# Run on Android
npx react-native run-android
```

## Core Concepts

### Component-Based Architecture

React Native uses React components to build UI:

```javascript
import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

const MyComponent = ({ title }) => {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>{title}</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: { padding: 16 },
  title: { fontSize: 24, fontWeight: 'bold' }
});
```

### React Hooks

| Hook | Use Case |
|------|----------|
| `useState` | Local component state |
| `useEffect` | Side effects, lifecycle |
| `useContext` | Access context values |
| `useReducer` | Complex state logic |
| `useCallback` | Memoize callbacks |
| `useMemo` | Memoize expensive computations |
| `useRef` | Persist values, DOM refs |

### State Management Options

| Solution | Use Case | Complexity |
|----------|----------|------------|
| useState/useReducer | Local state | Low |
| Context API | App-wide state | Medium |
| Redux Toolkit | Large apps, complex state | High |
| MobX | Reactive state | Medium |
| Zustand | Simple global state | Low |
| Recoil | Atomic state management | Medium |

## Navigation

### React Navigation

```javascript
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

const Stack = createNativeStackNavigator();

function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen name="Home" component={HomeScreen} />
        <Stack.Screen name="Details" component={DetailsScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

// Navigate
navigation.navigate('Details', { itemId: 42 });
```

### Navigation Types

- **Stack Navigator:** Push/pop screens
- **Tab Navigator:** Bottom tabs
- **Drawer Navigator:** Side drawer menu
- **Material Top Tabs:** Swipeable tabs

## Styling

### StyleSheet API

```javascript
const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center'
  },
  text: {
    fontSize: 16,
    color: '#333'
  }
});
```

### Flexbox Layout

React Native uses Flexbox for layout (default `flexDirection: 'column'`).

### Responsive Design

```javascript
import { Dimensions, Platform } from 'react-native';

const { width, height } = Dimensions.get('window');
const isIOS = Platform.OS === 'ios';
```

## Performance Optimization

### FlatList for Large Lists

```javascript
<FlatList
  data={items}
  keyExtractor={item => item.id}
  renderItem={({ item }) => <ItemCard item={item} />}
  initialNumToRender={10}
  maxToRenderPerBatch={10}
  windowSize={5}
/>
```

### Memoization

```javascript
const MemoizedComponent = React.memo(({ data }) => {
  return <ExpensiveComponent data={data} />;
});

const memoizedValue = useMemo(() => computeExpensiveValue(a, b), [a, b]);
const memoizedCallback = useCallback(() => doSomething(a, b), [a, b]);
```

### Avoid Inline Functions and Styles

```javascript
// ❌ Bad: Creates new function on every render
<Button onPress={() => handlePress()} />

// ✅ Good: Stable reference
const handlePress = useCallback(() => { /* ... */ }, []);
<Button onPress={handlePress} />
```

## Native Modules

### Using Native Modules

```javascript
import { NativeModules } from 'react-native';
const { CalendarModule } = NativeModules;

CalendarModule.createCalendarEvent('Party', 'My House');
```

### Popular Native Libraries

- **React Native Camera:** Camera functionality
- **React Native Maps:** Native maps
- **React Native Gesture Handler:** Advanced gestures
- **React Native Reanimated:** High-performance animations
- **React Native Vector Icons:** Icon sets

## Platform-Specific Code

### Platform Module

```javascript
import { Platform } from 'react-native';

const styles = StyleSheet.create({
  container: {
    paddingTop: Platform.OS === 'ios' ? 20 : 0
  }
});

// Platform-specific values
const value = Platform.select({
  ios: 'iOS value',
  android: 'Android value'
});
```

### Platform-Specific Files

```
MyComponent.ios.js
MyComponent.android.js
```

## Testing

### Jest Unit Testing

```javascript
import { render, fireEvent } from '@testing-library/react-native';

test('button press increments counter', () => {
  const { getByText } = render(<Counter />);
  const button = getByText('Increment');
  
  fireEvent.press(button);
  
  expect(getByText('Count: 1')).toBeTruthy();
});
```

### Detox E2E Testing

```javascript
describe('Login Flow', () => {
  it('should login successfully', async () => {
    await element(by.id('email')).typeText('user@example.com');
    await element(by.id('password')).typeText('password');
    await element(by.id('loginButton')).tap();
    await expect(element(by.text('Welcome'))).toBeVisible();
  });
});
```

## Deployment

### iOS Deployment

1. Configure signing in Xcode
2. Archive app
3. Upload to App Store Connect
4. Submit for review

### Android Deployment

1. Generate signing key
2. Configure gradle for release
3. Build release APK/AAB
4. Upload to Google Play Console

### Over-the-Air Updates

Use CodePush or Expo Updates for JavaScript bundle updates without app store review.

## Best Practices

- Use TypeScript for type safety
- Implement proper error boundaries
- Handle loading and error states
- Use absolute imports for cleaner code
- Follow React Native directory structure
- Optimize images (use WebP, proper resolutions)
- Implement proper accessibility
- Test on real devices, not just simulators

## Using the Reference Files

**`/references/react-patterns-guide.md`** — Read when implementing React hooks, context, custom hooks, or advanced React patterns.

**`/references/navigation-guide.md`** — Read when setting up navigation, implementing deep linking, or handling complex navigation flows.

**`/references/performance-guide.md`** — Read when optimizing app performance, reducing bundle size, or debugging performance issues.

**`/references/troubleshooting.md`** — Read when encountering build errors, runtime issues, or platform-specific problems.

## References

- [Navigation Guide](references/navigation-guide.md)
- [Performance Guide](references/performance-guide.md)
- [React Patterns Guide](references/react-patterns-guide.md)
- [Troubleshooting](references/troubleshooting.md)
