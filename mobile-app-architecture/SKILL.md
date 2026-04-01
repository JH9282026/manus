---
name: mobile-app-architecture
description: "Design and implement scalable mobile app architectures using MVVM, MVI, Clean Architecture, and layered patterns for maintainable, testable code. Use for: structuring mobile apps, implementing MVVM/MVP/MVI patterns, applying Clean Architecture principles, separating concerns (presentation/domain/data layers), designing repositories and use cases, implementing dependency injection, ensuring testability, and scaling large mobile applications."
---

# Mobile App Architecture

Design scalable, maintainable mobile application architectures using proven patterns and principles.

## Overview

Mobile app architecture defines how an application's code is organized and how components interact. Good architecture ensures maintainability, testability, scalability, and team collaboration. This skill covers architectural patterns (MVVM, MVI, Clean Architecture), layered design, dependency injection, and best practices for structuring mobile applications.

## Architectural Patterns

### MVVM (Model-View-ViewModel)

**Components:**
- **Model:** Data and business logic
- **View:** UI layer (Activities, Fragments, Composables, SwiftUI Views)
- **ViewModel:** Presentation logic, exposes data to View

**Benefits:**
- Clear separation of concerns
- Testable ViewModels (no UI dependencies)
- Reactive data binding
- Survives configuration changes (Android)

**When to use:** Most modern mobile apps, especially with declarative UI frameworks.

### MVI (Model-View-Intent)

**Components:**
- **Model:** UI state (single source of truth)
- **View:** Renders state, emits intents
- **Intent:** User actions/events

**Flow:** Intent → ViewModel processes → State update → View renders

**Benefits:**
- Unidirectional data flow
- Predictable state management
- Time-travel debugging
- Easier to reason about

**When to use:** Complex apps with intricate state management, apps requiring state history.

### MVP (Model-View-Presenter)

**Components:**
- **Model:** Data layer
- **View:** Passive UI (interface)
- **Presenter:** Mediates between Model and View

**Benefits:**
- Testable Presenter
- Clear contracts (interfaces)

**When to use:** Legacy apps, teams familiar with MVP, simpler than MVVM for some use cases.

## Clean Architecture

### Principles

**Separation of Concerns:** Each layer has a single responsibility.

**Dependency Rule:** Dependencies point inward. Inner layers know nothing about outer layers.

**Independence:** Business logic is independent of frameworks, UI, databases.

### Layers

| Layer | Responsibility | Dependencies |
|-------|----------------|--------------|
| **Presentation** | UI, ViewModels | Domain Layer |
| **Domain** | Business logic, Use Cases, Entities | None (pure business rules) |
| **Data** | Repositories, Data Sources, APIs | Domain Layer (interfaces) |

### Domain Layer

**Entities:** Core business objects
```kotlin
data class User(
    val id: String,
    val name: String,
    val email: String
)
```

**Use Cases (Interactors):** Single-purpose business operations
```kotlin
class GetUserUseCase(private val repository: UserRepository) {
    suspend operator fun invoke(userId: String): Result<User> {
        return repository.getUser(userId)
    }
}
```

**Repository Interfaces:** Define data contracts
```kotlin
interface UserRepository {
    suspend fun getUser(id: String): Result<User>
    suspend fun saveUser(user: User): Result<Unit>
}
```

### Data Layer

**Repository Implementations:**
```kotlin
class UserRepositoryImpl(
    private val remoteDataSource: UserRemoteDataSource,
    private val localDataSource: UserLocalDataSource
) : UserRepository {
    override suspend fun getUser(id: String): Result<User> {
        return try {
            val user = remoteDataSource.fetchUser(id)
            localDataSource.cacheUser(user)
            Result.success(user)
        } catch (e: Exception) {
            localDataSource.getUser(id) ?: Result.failure(e)
        }
    }
}
```

**Data Sources:**
- **Remote:** API calls, network requests
- **Local:** Database, SharedPreferences, file storage

### Presentation Layer

**ViewModels:**
```kotlin
class UserViewModel(
    private val getUserUseCase: GetUserUseCase
) : ViewModel() {
    private val _uiState = MutableStateFlow<UiState>(UiState.Loading)
    val uiState: StateFlow<UiState> = _uiState.asStateFlow()
    
    fun loadUser(userId: String) {
        viewModelScope.launch {
            _uiState.value = UiState.Loading
            getUserUseCase(userId).fold(
                onSuccess = { user -> _uiState.value = UiState.Success(user) },
                onFailure = { error -> _uiState.value = UiState.Error(error.message) }
            )
        }
    }
}
```

## Dependency Injection

### Benefits
- Loose coupling
- Testability (easy mocking)
- Flexibility (swap implementations)
- Centralized configuration

### DI Frameworks

| Platform | Framework | Notes |
|----------|-----------|-------|
| Android | Hilt (Dagger) | Recommended, compile-time |
| Android | Koin | Runtime, simpler |
| iOS | Swinject | Popular Swift DI |
| Flutter | get_it, injectable | Service locator pattern |
| React Native | InversifyJS | IoC container |

### Manual DI (Simple Apps)

```kotlin
class AppContainer {
    private val api = ApiService()
    private val database = AppDatabase.getInstance()
    
    val userRepository: UserRepository = UserRepositoryImpl(
        remoteDataSource = UserRemoteDataSource(api),
        localDataSource = UserLocalDataSource(database.userDao())
    )
    
    fun provideUserViewModel(): UserViewModel {
        return UserViewModel(GetUserUseCase(userRepository))
    }
}
```

## Modularization

### Benefits
- Faster build times (parallel compilation)
- Clear boundaries
- Reusability
- Team scalability

### Module Types

| Type | Purpose | Example |
|------|---------|---------|
| **App** | Main application module | app |
| **Feature** | Self-contained features | feature-auth, feature-profile |
| **Core** | Shared utilities | core-network, core-database |
| **Domain** | Business logic | domain |
| **Data** | Data layer | data |

### Module Structure Example

```
app/
feature/
  ├── auth/
  ├── profile/
  └── settings/
core/
  ├── network/
  ├── database/
  └── ui/
domain/
data/
```

## Data Flow Patterns

### Unidirectional Data Flow (UDF)

**Flow:** User Action → ViewModel → State Update → UI Render

**Benefits:**
- Predictable
- Easier debugging
- State history

### Repository Pattern

**Purpose:** Abstract data sources, provide clean API to domain layer.

**Implementation:**
```kotlin
interface ProductRepository {
    fun getProducts(): Flow<List<Product>>
    suspend fun getProduct(id: String): Product?
    suspend fun saveProduct(product: Product)
}

class ProductRepositoryImpl(
    private val api: ProductApi,
    private val dao: ProductDao
) : ProductRepository {
    override fun getProducts(): Flow<List<Product>> {
        return dao.getProducts().map { entities ->
            entities.map { it.toDomain() }
        }
    }
    
    override suspend fun getProduct(id: String): Product? {
        return dao.getProduct(id)?.toDomain()
            ?: api.fetchProduct(id).also { dao.insert(it.toEntity()) }
    }
}
```

## Error Handling

### Result/Either Pattern

```kotlin
sealed class Result<out T> {
    data class Success<T>(val data: T) : Result<T>()
    data class Error(val exception: Exception) : Result<Nothing>()
}

// Usage
suspend fun getUser(id: String): Result<User> {
    return try {
        val user = api.fetchUser(id)
        Result.Success(user)
    } catch (e: Exception) {
        Result.Error(e)
    }
}
```

## Testing Strategy

### Unit Tests
- Test Use Cases in isolation
- Test ViewModels with mocked repositories
- Test Repository logic with mocked data sources

### Integration Tests
- Test Repository with real database
- Test API integration

### UI Tests
- Test user flows
- Test UI state rendering

## Best Practices

1. **Single Responsibility:** Each class/module has one reason to change
2. **Dependency Inversion:** Depend on abstractions, not concretions
3. **Interface Segregation:** Many specific interfaces > one general interface
4. **Keep Domain Pure:** No framework dependencies in domain layer
5. **Use Dependency Injection:** Avoid manual object creation
6. **Favor Composition:** Over inheritance
7. **Immutable Data:** Use immutable data classes for state
8. **Reactive Streams:** Use Flow/LiveData/Combine for reactive data

## Common Pitfalls

- **God Objects:** ViewModels doing too much
- **Tight Coupling:** Direct dependencies instead of interfaces
- **Framework Leakage:** Android/iOS APIs in domain layer
- **Anemic Domain:** Domain layer with no logic
- **Over-Engineering:** Clean Architecture for simple apps

## Architecture Decision Factors

| Factor | Simple App | Medium App | Large/Enterprise App |
|--------|------------|------------|---------------------|
| Pattern | MVVM | MVVM + Repository | Clean Architecture + MVVM/MVI |
| Layers | 2 (UI, Data) | 3 (UI, Domain, Data) | 3+ with modularization |
| DI | Manual | Hilt/Koin | Hilt with modules |
| Modularization | Single module | Feature modules | Multi-module with core libs |

## Using the Reference Files

**`/references/mvvm-implementation.md`** — Read when implementing MVVM pattern, structuring ViewModels, or handling UI state.

**`/references/clean-architecture-guide.md`** — Read when applying Clean Architecture, designing use cases, or structuring layers.

**`/references/dependency-injection.md`** — Read when setting up DI, configuring Hilt/Koin, or managing dependencies.

**`/references/testing-architecture.md`** — Read when writing unit tests for architecture components, mocking dependencies, or testing use cases.
