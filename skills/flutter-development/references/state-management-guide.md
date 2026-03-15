# State Management Guide

Comprehensive guide to Flutter state management.

---

## Provider Pattern

```dart
class Counter with ChangeNotifier {
  int _count = 0;
  int get count => _count;
  
  void increment() {
    _count++;
    notifyListeners();
  }
}

// Provide
ChangeNotifierProvider(
  create: (_) => Counter(),
  child: MyApp(),
)

// Consume
Consumer<Counter>(
  builder: (context, counter, child) {
    return Text('${counter.count}');
  },
)
```

## Riverpod Pattern

```dart
final counterProvider = StateNotifierProvider<CounterNotifier, int>((ref) {
  return CounterNotifier();
});

class CounterNotifier extends StateNotifier<int> {
  CounterNotifier() : super(0);
  
  void increment() => state++;
}

// Usage
final count = ref.watch(counterProvider);
```

## BLoC Pattern

```dart
class CounterBloc extends Bloc<CounterEvent, int> {
  CounterBloc() : super(0) {
    on<IncrementEvent>((event, emit) => emit(state + 1));
  }
}

// Usage
BlocProvider(
  create: (_) => CounterBloc(),
  child: BlocBuilder<CounterBloc, int>(
    builder: (context, count) {
      return Text('$count');
    },
  ),
)
```
