# Jetpack Compose Patterns Cookbook

Common patterns and code examples for Jetpack Compose development.

---

## State Management Patterns

### ViewModel with StateFlow
```kotlin
class UserViewModel : ViewModel() {
    private val _uiState = MutableStateFlow(UserUiState())
    val uiState: StateFlow<UserUiState> = _uiState.asStateFlow()
    
    fun updateUser(name: String) {
        _uiState.update { it.copy(name = name) }
    }
}

@Composable
fun UserScreen(viewModel: UserViewModel = viewModel()) {
    val uiState by viewModel.uiState.collectAsState()
    
    Column {
        Text(uiState.name)
        Button(onClick = { viewModel.updateUser("New Name") }) {
            Text("Update")
        }
    }
}
```

### Remember and MutableState
```kotlin
@Composable
fun Counter() {
    var count by remember { mutableStateOf(0) }
    
    Column {
        Text("Count: $count")
        Button(onClick = { count++ }) {
            Text("Increment")
        }
    }
}
```

### RememberSaveable for Configuration Changes
```kotlin
@Composable
fun PersistentCounter() {
    var count by rememberSaveable { mutableStateOf(0) }
    
    Button(onClick = { count++ }) {
        Text("Count: $count")
    }
}
```

---

## Layout Patterns

### Scaffold with TopBar and FAB
```kotlin
@Composable
fun MyScreen() {
    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("My App") },
                actions = {
                    IconButton(onClick = { /* action */ }) {
                        Icon(Icons.Default.Settings, "Settings")
                    }
                }
            )
        },
        floatingActionButton = {
            FloatingActionButton(onClick = { /* action */ }) {
                Icon(Icons.Default.Add, "Add")
            }
        }
    ) { paddingValues ->
        Content(Modifier.padding(paddingValues))
    }
}
```

### LazyColumn with Items
```kotlin
@Composable
fun ItemList(items: List<Item>) {
    LazyColumn {
        items(
            items = items,
            key = { it.id }
        ) { item ->
            ItemCard(item)
        }
    }
}
```

---

## Navigation Patterns

### Basic Navigation
```kotlin
@Composable
fun AppNavigation() {
    val navController = rememberNavController()
    
    NavHost(navController, startDestination = "home") {
        composable("home") {
            HomeScreen(
                onNavigateToDetail = { id ->
                    navController.navigate("detail/$id")
                }
            )
        }
        composable(
            route = "detail/{itemId}",
            arguments = listOf(navArgument("itemId") { type = NavType.IntType })
        ) { backStackEntry ->
            DetailScreen(backStackEntry.arguments?.getInt("itemId"))
        }
    }
}
```

---

## Side Effects

### LaunchedEffect
```kotlin
@Composable
fun DataLoader(userId: String) {
    var data by remember { mutableStateOf<Data?>(null) }
    
    LaunchedEffect(userId) {
        data = repository.loadData(userId)
    }
    
    data?.let { DataView(it) }
}
```

### DisposableEffect
```kotlin
@Composable
fun LifecycleAware() {
    DisposableEffect(Unit) {
        val listener = createListener()
        registerListener(listener)
        
        onDispose {
            unregisterListener(listener)
        }
    }
}
```
