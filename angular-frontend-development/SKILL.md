---
name: angular-frontend-development
description: "Build enterprise-grade web applications using Angular framework with TypeScript, components, services, dependency injection, RxJS, routing, state management, and testing. Use for creating single-page applications, enterprise dashboards, progressive web apps, component-based architectures, reactive programming patterns, form handling, HTTP communication, authentication flows, and scalable frontend systems."
---

# Angular Frontend Development

Build robust, scalable web applications using the Angular framework with TypeScript, reactive programming, and enterprise-grade architecture patterns.

## Overview

Angular is a comprehensive TypeScript-based framework for building dynamic web applications. This skill covers the complete Angular ecosystem including components, modules, services, dependency injection, RxJS observables, routing, state management, forms, HTTP communication, testing, and deployment strategies. Angular excels at enterprise applications requiring strong typing, maintainability, and scalability.

## Quick Start: Project Type Selection

| Application Type | Architecture Pattern | Key Features | Reference |
|-----------------|---------------------|--------------|----------|
| Enterprise dashboard | Feature modules + lazy loading | NgRx, guards, interceptors | `/references/routing-state-management.md` |
| Progressive Web App | Service workers + offline support | PWA module, caching strategies | `/references/angular-fundamentals.md` |
| Form-heavy application | Reactive forms + validation | FormBuilder, custom validators | `/references/components-modules.md` |
| Real-time data app | RxJS streams + WebSockets | Observables, operators, subjects | `/references/services-dependency-injection.md` |
| Multi-tenant SaaS | Modular architecture + DI | Shared modules, environment configs | `/references/components-modules.md` |

## Core Architecture Principles

### Component-Based Design

**Smart vs. Presentational Components**
- Smart (container) components handle business logic and state management
- Presentational (dumb) components receive data via `@Input()` and emit events via `@Output()`
- Keep components focused on single responsibilities
- Use OnPush change detection for presentational components

**Component Communication Patterns**
- Parent-to-child: `@Input()` properties
- Child-to-parent: `@Output()` EventEmitters
- Sibling components: Shared service with BehaviorSubject
- Distant components: State management (NgRx, Akita, or custom service)

### Dependency Injection Strategy

**Service Scope Selection**

| Scope | Provider Location | Use Case | Lifetime |
|-------|------------------|----------|----------|
| Singleton | `providedIn: 'root'` | App-wide services (auth, config) | Application |
| Feature | Feature module | Feature-specific logic | Feature module |
| Component | Component providers | Component-specific state | Component |
| Lazy module | Lazy-loaded module | Module-isolated services | Module |

**Injection Tokens**
- Use InjectionToken for non-class dependencies (configuration objects, constants)
- Leverage multi-providers for plugin architectures
- Implement factory providers for conditional service creation

### Reactive Programming with RxJS

**Observable Patterns**
- Use `async` pipe in templates to auto-subscribe/unsubscribe
- Implement `takeUntil()` with destroy subject for manual subscriptions
- Leverage `shareReplay()` for expensive operations
- Combine streams with `combineLatest()`, `forkJoin()`, `merge()`

**Common Operators**
- Transformation: `map()`, `switchMap()`, `mergeMap()`, `concatMap()`
- Filtering: `filter()`, `debounceTime()`, `distinctUntilChanged()`
- Combination: `combineLatest()`, `withLatestFrom()`, `zip()`
- Error handling: `catchError()`, `retry()`, `retryWhen()`

## Module Organization

### Feature Module Structure

```
feature/
├── components/          # Feature components
├── services/           # Feature services
├── models/             # TypeScript interfaces/types
├── guards/             # Route guards
├── interceptors/       # HTTP interceptors
├── pipes/              # Custom pipes
├── directives/         # Custom directives
├── feature.module.ts   # Feature module definition
└── feature-routing.module.ts  # Feature routes
```

### Module Types

**Core Module** (singleton, imported once in AppModule)
- Authentication services
- HTTP interceptors
- Global error handlers
- App-wide singleton services

**Shared Module** (imported by feature modules)
- Common components (buttons, cards, modals)
- Common directives and pipes
- Angular Material or UI library modules
- CommonModule, FormsModule, ReactiveFormsModule

**Feature Modules** (lazy-loaded when possible)
- Feature-specific components and services
- Feature routing configuration
- Isolated business logic

## Routing and Navigation

### Route Configuration Patterns

**Lazy Loading**
```typescript
const routes: Routes = [
  {
    path: 'admin',
    loadChildren: () => import('./admin/admin.module').then(m => m.AdminModule),
    canActivate: [AuthGuard],
    canLoad: [AuthGuard]
  }
];
```

**Route Guards**
- `CanActivate`: Control route access (authentication)
- `CanActivateChild`: Protect child routes
- `CanDeactivate`: Prevent navigation (unsaved changes)
- `CanLoad`: Prevent lazy module loading
- `Resolve`: Pre-fetch data before route activation

**Route Data and Parameters**
- Use route data for static configuration (breadcrumbs, titles)
- Access params via `ActivatedRoute.params` observable
- Query params for optional filters and pagination
- Fragment for in-page navigation

## State Management Approaches

### When to Use Each Pattern

| Pattern | Complexity | Use Case | Learning Curve |
|---------|-----------|----------|----------------|
| Component state | Low | Simple forms, UI toggles | Minimal |
| Service with BehaviorSubject | Low-Medium | Shared data between components | Low |
| NgRx | High | Complex apps, time-travel debugging | Steep |
| Akita | Medium | Structured state without boilerplate | Moderate |
| ComponentStore | Medium | Component-level complex state | Moderate |

**Service-Based State (Simple Apps)**
- Use BehaviorSubject for state storage
- Expose observables (not subjects) to components
- Implement immutable state updates
- Suitable for small to medium applications

**NgRx (Enterprise Apps)**
- Unidirectional data flow
- Actions, reducers, selectors, effects
- DevTools for time-travel debugging
- Best for large teams and complex state

## Forms Strategy

### Reactive Forms vs. Template-Driven

**Use Reactive Forms When:**
- Complex validation logic required
- Dynamic form controls (add/remove fields)
- Unit testing form logic
- Cross-field validation needed
- Form state needs to be managed programmatically

**Use Template-Driven Forms When:**
- Simple forms with basic validation
- Rapid prototyping
- Forms closely tied to template structure

### Reactive Forms Best Practices

**FormBuilder Pattern**
- Use FormBuilder service for cleaner syntax
- Group related controls with FormGroup
- Use FormArray for dynamic lists
- Implement custom validators for business rules

**Validation Strategy**
- Built-in validators: `Validators.required`, `Validators.email`, `Validators.pattern()`
- Custom validators: Implement `ValidatorFn` interface
- Async validators: For server-side validation (username availability)
- Cross-field validation: Implement at FormGroup level

## HTTP Communication

### HttpClient Patterns

**Service Layer Architecture**
- Create dedicated service for each API resource
- Use TypeScript interfaces for request/response types
- Implement error handling with `catchError()`
- Add retry logic for transient failures

**Interceptors**
- Authentication: Add JWT tokens to requests
- Error handling: Global error processing
- Logging: Request/response logging
- Caching: Implement response caching
- Loading indicators: Track pending requests

**Type Safety**
```typescript
interface User {
  id: number;
  name: string;
  email: string;
}

getUser(id: number): Observable<User> {
  return this.http.get<User>(`/api/users/${id}`);
}
```

## Testing Strategy

### Test Types

**Unit Tests (Jasmine + Karma)**
- Test components in isolation
- Mock dependencies with TestBed
- Test services with dependency injection
- Aim for 80%+ code coverage

**Integration Tests**
- Test component interactions
- Test routing and navigation
- Test form submissions
- Use real services when appropriate

**E2E Tests (Protractor/Cypress)**
- Test critical user flows
- Test authentication workflows
- Test form submissions and validation
- Run in CI/CD pipeline

### Testing Best Practices

**Component Testing**
- Use `ComponentFixture` for component testing
- `detectChanges()` to trigger change detection
- Query DOM with `DebugElement` and `By.css()`
- Test `@Input()` and `@Output()` bindings

**Service Testing**
- Use `TestBed.configureTestingModule()` for DI setup
- Mock HTTP requests with `HttpClientTestingModule`
- Test observable streams with marble testing
- Verify subscription cleanup

## Performance Optimization

### Change Detection Optimization

**OnPush Strategy**
- Use for presentational components
- Triggers only on input reference changes
- Manually trigger with `ChangeDetectorRef.markForCheck()`
- Reduces change detection cycles significantly

**TrackBy Functions**
- Use with `*ngFor` for list rendering
- Prevents unnecessary DOM re-renders
- Track by unique identifier (id)

### Bundle Optimization

**Lazy Loading**
- Load feature modules on demand
- Reduces initial bundle size
- Improves Time to Interactive (TTI)

**Tree Shaking**
- Import only needed modules
- Use production builds (`ng build --prod`)
- Analyze bundle with `webpack-bundle-analyzer`

**Preloading Strategies**
- `PreloadAllModules`: Preload all lazy modules after initial load
- Custom preloading: Selective module preloading
- Network-aware preloading: Based on connection speed

## Build and Deployment

### Build Configurations

**Environment Files**
- `environment.ts`: Development configuration
- `environment.prod.ts`: Production configuration
- Custom environments: Staging, QA, etc.
- Use `fileReplacements` in `angular.json`

**Production Build Optimizations**
- Ahead-of-Time (AOT) compilation
- Tree shaking and dead code elimination
- Minification and uglification
- Differential loading (ES5 + ES2015)

### Deployment Strategies

| Platform | Build Command | Deployment Method | Use Case |
|----------|--------------|-------------------|----------|
| Netlify | `ng build --prod` | Drag-and-drop or Git | Static hosting, JAMstack |
| Vercel | `ng build --prod` | Git integration | Serverless, edge network |
| Firebase Hosting | `ng build --prod` | Firebase CLI | Google ecosystem integration |
| AWS S3 + CloudFront | `ng build --prod` | AWS CLI or CI/CD | Enterprise, custom CDN |
| Docker + Nginx | `ng build --prod` | Container registry | Kubernetes, microservices |

## Angular CLI Commands

### Essential Commands

**Generation**
- `ng generate component <name>`: Create component
- `ng generate service <name>`: Create service
- `ng generate module <name>`: Create module
- `ng generate guard <name>`: Create route guard
- `ng generate interceptor <name>`: Create HTTP interceptor

**Development**
- `ng serve`: Start dev server
- `ng serve --open`: Start and open browser
- `ng serve --port 4300`: Custom port
- `ng serve --proxy-config proxy.conf.json`: API proxy

**Building**
- `ng build`: Development build
- `ng build --prod`: Production build
- `ng build --configuration=staging`: Custom configuration

**Testing**
- `ng test`: Run unit tests
- `ng test --code-coverage`: Generate coverage report
- `ng e2e`: Run E2E tests

## Common Patterns and Solutions

### Authentication Flow

1. **Login Component**: Capture credentials
2. **Auth Service**: Handle authentication logic
3. **HTTP Interceptor**: Add JWT to requests
4. **Auth Guard**: Protect routes
5. **Token Storage**: Store in localStorage/sessionStorage
6. **Token Refresh**: Implement refresh token logic

### Error Handling

**Global Error Handler**
- Implement `ErrorHandler` interface
- Log errors to monitoring service
- Display user-friendly messages
- Provide in CoreModule

**HTTP Error Interceptor**
- Catch HTTP errors globally
- Handle 401 (redirect to login)
- Handle 403 (show unauthorized message)
- Handle 500 (show error page)

### Loading States

**Interceptor-Based**
- Track pending HTTP requests
- Show/hide global loading indicator
- Use loading service with BehaviorSubject

**Component-Based**
- Local loading state for specific operations
- Disable buttons during submission
- Show skeleton screens for content loading

## Migration and Upgrade

### Version Upgrade Strategy

**Angular Update Guide**
- Use `ng update` command
- Follow official update guide at update.angular.io
- Update one major version at a time
- Test thoroughly after each update

**Breaking Changes**
- Review CHANGELOG.md for breaking changes
- Update deprecated APIs
- Run `ng update @angular/core @angular/cli`
- Update third-party dependencies

### AngularJS to Angular Migration

**Hybrid Approach**
- Use `@angular/upgrade` package
- Run AngularJS and Angular side-by-side
- Migrate components incrementally
- Use downgradeComponent/upgradeComponent

## Using the Reference Files

### When to Read Each Reference

**`/references/angular-fundamentals.md`** — Read when setting up new Angular projects, understanding the Angular architecture, working with decorators and metadata, configuring the development environment, or learning core Angular concepts like modules, bootstrapping, and the compilation process.

**`/references/components-modules.md`** — Read when creating components, organizing module structure, implementing component lifecycle hooks, working with templates and data binding, creating custom directives and pipes, or structuring feature modules and shared modules.

**`/references/services-dependency-injection.md`** — Read when creating services, implementing dependency injection patterns, working with RxJS observables, handling HTTP communication, implementing interceptors, or managing application state with services.

**`/references/routing-state-management.md`** — Read when configuring routing, implementing navigation, setting up route guards, working with lazy loading, implementing state management with NgRx or other libraries, or handling complex application state and data flow patterns.
