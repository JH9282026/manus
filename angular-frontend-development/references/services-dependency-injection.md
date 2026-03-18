# Services and Dependency Injection

Comprehensive guide to creating services, implementing dependency injection, working with RxJS, and managing HTTP communication in Angular.

---

## Service Creation and Scope

### Creating Services

**Basic Service**
```typescript
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'  // Singleton service, available app-wide
})
export class UserService {
  private users: User[] = [];
  
  getUsers(): User[] {
    return this.users;
  }
  
  addUser(user: User): void {
    this.users.push(user);
  }
}
```

**Generate with CLI**
```bash
ng generate service services/user
# or
ng g s services/user
```

### Service Scope and Providers

**Root Level (Singleton)**
```typescript
@Injectable({
  providedIn: 'root'
})
export class AuthService {
  // Single instance shared across entire app
}
```

**Module Level**
```typescript
// Service
@Injectable()
export class UserService {}

// Module
@NgModule({
  providers: [UserService]  // New instance for this module and its children
})
export class UsersModule {}
```

**Component Level**
```typescript
@Component({
  selector: 'app-user-list',
  templateUrl: './user-list.component.html',
  providers: [UserService]  // New instance for this component and its children
})
export class UserListComponent {}
```

**Lazy Module Level**
```typescript
@Injectable({
  providedIn: 'any'  // Separate instance for each lazy-loaded module
})
export class FeatureService {}
```

### Provider Scope Decision Matrix

| Scope | Provider Location | Use Case | Instances |
|-------|------------------|----------|----------|
| App-wide singleton | `providedIn: 'root'` | Auth, config, logging | 1 |
| Feature singleton | Feature module providers | Feature-specific data | 1 per feature |
| Component instance | Component providers | Component state | 1 per component |
| Lazy module | `providedIn: 'any'` | Lazy module isolation | 1 per lazy module |

---

## Dependency Injection Patterns

### Constructor Injection

**Basic Injection**
```typescript
export class UserListComponent {
  constructor(
    private userService: UserService,
    private router: Router,
    private route: ActivatedRoute
  ) {}
}
```

**Optional Dependencies**
```typescript
import { Optional } from '@angular/core';

export class UserComponent {
  constructor(
    @Optional() private logger: LoggerService
  ) {
    if (this.logger) {
      this.logger.log('UserComponent initialized');
    }
  }
}
```

**Self and SkipSelf**
```typescript
import { Self, SkipSelf } from '@angular/core';

export class ChildComponent {
  constructor(
    @Self() private localService: DataService,      // Only from this component's injector
    @SkipSelf() private parentService: DataService  // Skip this component, use parent's
  ) {}
}
```

### Injection Tokens

**Creating Injection Tokens**
```typescript
import { InjectionToken } from '@angular/core';

// Define token
export const API_URL = new InjectionToken<string>('api.url');
export const APP_CONFIG = new InjectionToken<AppConfig>('app.config');

// Provide value
@NgModule({
  providers: [
    { provide: API_URL, useValue: 'https://api.example.com' },
    { provide: APP_CONFIG, useValue: { apiUrl: 'https://api.example.com', timeout: 5000 } }
  ]
})
export class AppModule {}

// Inject
export class UserService {
  constructor(
    @Inject(API_URL) private apiUrl: string,
    @Inject(APP_CONFIG) private config: AppConfig
  ) {}
}
```

**Default Values with Injection Tokens**
```typescript
export const API_URL = new InjectionToken<string>('api.url', {
  providedIn: 'root',
  factory: () => 'https://api.example.com'  // Default value
});
```

### Provider Types

**Class Provider**
```typescript
// Standard
providers: [UserService]

// Explicit (equivalent)
providers: [{ provide: UserService, useClass: UserService }]

// Alternative implementation
providers: [{ provide: UserService, useClass: MockUserService }]
```

**Value Provider**
```typescript
const API_CONFIG = {
  apiUrl: 'https://api.example.com',
  timeout: 5000
};

providers: [
  { provide: APP_CONFIG, useValue: API_CONFIG }
]
```

**Factory Provider**
```typescript
export function userServiceFactory(
  http: HttpClient,
  config: AppConfig
): UserService {
  return config.useMockData 
    ? new MockUserService() 
    : new UserService(http);
}

providers: [
  {
    provide: UserService,
    useFactory: userServiceFactory,
    deps: [HttpClient, APP_CONFIG]
  }
]
```

**Existing Provider (Alias)**
```typescript
providers: [
  UserService,
  { provide: 'UserServiceAlias', useExisting: UserService }
]
```

**Multi-Provider**
```typescript
// Define token
export const PLUGIN = new InjectionToken<Plugin[]>('plugin');

// Provide multiple values
providers: [
  { provide: PLUGIN, useClass: PluginA, multi: true },
  { provide: PLUGIN, useClass: PluginB, multi: true },
  { provide: PLUGIN, useClass: PluginC, multi: true }
]

// Inject array
export class PluginManager {
  constructor(@Inject(PLUGIN) private plugins: Plugin[]) {
    // plugins is an array of all provided plugins
  }
}
```

---

## RxJS and Observables

### Observable Basics

**Creating Observables**
```typescript
import { Observable, of, from, interval, fromEvent } from 'rxjs';

// From value
const value$ = of(1, 2, 3);

// From array
const array$ = from([1, 2, 3]);

// From promise
const promise$ = from(fetch('/api/users'));

// Interval
const interval$ = interval(1000);  // Emits every second

// From event
const click$ = fromEvent(document, 'click');

// Custom observable
const custom$ = new Observable(subscriber => {
  subscriber.next(1);
  subscriber.next(2);
  subscriber.complete();
});
```

**Subscribing to Observables**
```typescript
// Basic subscription
this.userService.getUsers().subscribe(users => {
  this.users = users;
});

// With error handling
this.userService.getUsers().subscribe({
  next: users => this.users = users,
  error: err => console.error(err),
  complete: () => console.log('Complete')
});

// Unsubscribe
const subscription = this.userService.getUsers().subscribe(users => {
  this.users = users;
});

// Later
subscription.unsubscribe();
```

### Subjects

**BehaviorSubject (Most Common)**
```typescript
import { BehaviorSubject } from 'rxjs';

export class UserService {
  private currentUserSubject = new BehaviorSubject<User | null>(null);
  currentUser$ = this.currentUserSubject.asObservable();
  
  setCurrentUser(user: User) {
    this.currentUserSubject.next(user);
  }
  
  getCurrentUser(): User | null {
    return this.currentUserSubject.value;  // Synchronous access to current value
  }
}
```

**Subject**
```typescript
import { Subject } from 'rxjs';

export class EventService {
  private eventSubject = new Subject<string>();
  event$ = this.eventSubject.asObservable();
  
  emit(event: string) {
    this.eventSubject.next(event);
  }
}
```

**ReplaySubject**
```typescript
import { ReplaySubject } from 'rxjs';

export class LogService {
  private logSubject = new ReplaySubject<string>(5);  // Buffer last 5 values
  log$ = this.logSubject.asObservable();
  
  log(message: string) {
    this.logSubject.next(message);
  }
}
```

**AsyncSubject**
```typescript
import { AsyncSubject } from 'rxjs';

const subject = new AsyncSubject();
subject.next(1);
subject.next(2);
subject.next(3);
subject.complete();  // Only emits 3 (last value before complete)
```

### Essential RxJS Operators

**Transformation Operators**
```typescript
import { map, switchMap, mergeMap, concatMap, exhaustMap } from 'rxjs/operators';

// map - Transform values
this.users$ = this.userService.getUsers().pipe(
  map(users => users.filter(u => u.active))
);

// switchMap - Cancel previous, switch to new observable
this.searchResults$ = this.searchControl.valueChanges.pipe(
  debounceTime(300),
  switchMap(query => this.searchService.search(query))
);

// mergeMap - Run in parallel
this.allUserDetails$ = this.userIds$.pipe(
  mergeMap(id => this.userService.getUser(id))
);

// concatMap - Sequential execution
this.sequentialResults$ = this.requests$.pipe(
  concatMap(request => this.http.post('/api', request))
);

// exhaustMap - Ignore new until current completes
this.saveClick$ = this.saveButton.clicks$.pipe(
  exhaustMap(() => this.userService.save(this.user))
);
```

**Filtering Operators**
```typescript
import { filter, debounceTime, distinctUntilChanged, take, takeUntil, takeWhile } from 'rxjs/operators';

// filter - Emit only matching values
this.activeUsers$ = this.users$.pipe(
  filter(users => users.length > 0)
);

// debounceTime - Wait for pause in emissions
this.search$ = this.searchControl.valueChanges.pipe(
  debounceTime(300)
);

// distinctUntilChanged - Emit only when value changes
this.uniqueValues$ = this.values$.pipe(
  distinctUntilChanged()
);

// take - Take first N emissions
this.firstThree$ = this.values$.pipe(
  take(3)
);

// takeUntil - Unsubscribe when notifier emits
private destroy$ = new Subject<void>();

ngOnInit() {
  this.data$.pipe(
    takeUntil(this.destroy$)
  ).subscribe(data => this.data = data);
}

ngOnDestroy() {
  this.destroy$.next();
  this.destroy$.complete();
}

// takeWhile - Take while condition is true
this.whileActive$ = this.values$.pipe(
  takeWhile(value => value.active)
);
```

**Combination Operators**
```typescript
import { combineLatest, forkJoin, merge, zip, withLatestFrom } from 'rxjs';

// combineLatest - Emit when any observable emits (after all have emitted once)
this.combined$ = combineLatest([
  this.users$,
  this.roles$,
  this.permissions$
]).pipe(
  map(([users, roles, permissions]) => ({ users, roles, permissions }))
);

// forkJoin - Wait for all to complete, emit last values (like Promise.all)
this.allData$ = forkJoin({
  users: this.userService.getUsers(),
  roles: this.roleService.getRoles(),
  permissions: this.permissionService.getPermissions()
});

// merge - Emit from any observable
this.allEvents$ = merge(
  this.clicks$,
  this.hovers$,
  this.keypresses$
);

// zip - Emit when all observables have emitted at same index
this.zipped$ = zip(this.obs1$, this.obs2$, this.obs3$);

// withLatestFrom - Combine with latest from other observables
this.saveClick$.pipe(
  withLatestFrom(this.formValue$, this.userId$),
  map(([click, formValue, userId]) => ({ formValue, userId }))
);
```

**Error Handling Operators**
```typescript
import { catchError, retry, retryWhen, throwError } from 'rxjs';
import { delay, take } from 'rxjs/operators';

// catchError - Handle errors
this.users$ = this.userService.getUsers().pipe(
  catchError(error => {
    console.error('Error loading users:', error);
    return of([]);  // Return empty array as fallback
  })
);

// retry - Retry on error
this.users$ = this.userService.getUsers().pipe(
  retry(3)  // Retry up to 3 times
);

// retryWhen - Custom retry logic
this.users$ = this.userService.getUsers().pipe(
  retryWhen(errors => errors.pipe(
    delay(1000),  // Wait 1 second between retries
    take(3)       // Retry up to 3 times
  ))
);
```

**Utility Operators**
```typescript
import { tap, delay, shareReplay, finalize } from 'rxjs/operators';

// tap - Side effects without modifying stream
this.users$ = this.userService.getUsers().pipe(
  tap(users => console.log('Users loaded:', users.length)),
  tap(users => this.logService.log('Users loaded'))
);

// delay - Delay emissions
this.delayed$ = this.values$.pipe(
  delay(1000)
);

// shareReplay - Share and replay last N emissions
this.users$ = this.userService.getUsers().pipe(
  shareReplay(1)  // Cache last emission, share among subscribers
);

// finalize - Execute when observable completes or errors
this.data$ = this.dataService.getData().pipe(
  finalize(() => this.loading = false)
);
```

---

## HTTP Communication

### HttpClient Setup

**Import HttpClientModule**
```typescript
import { HttpClientModule } from '@angular/common/http';

@NgModule({
  imports: [HttpClientModule]
})
export class AppModule {}
```

### HTTP Methods

**GET Request**
```typescript
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';

export class UserService {
  private apiUrl = 'https://api.example.com/users';
  
  constructor(private http: HttpClient) {}
  
  // Basic GET
  getUsers(): Observable<User[]> {
    return this.http.get<User[]>(this.apiUrl);
  }
  
  // GET with params
  getUsers(page: number, pageSize: number): Observable<User[]> {
    const params = new HttpParams()
      .set('page', page.toString())
      .set('pageSize', pageSize.toString());
    
    return this.http.get<User[]>(this.apiUrl, { params });
  }
  
  // GET single resource
  getUser(id: number): Observable<User> {
    return this.http.get<User>(`${this.apiUrl}/${id}`);
  }
}
```

**POST Request**
```typescript
// Create user
createUser(user: User): Observable<User> {
  return this.http.post<User>(this.apiUrl, user);
}

// With headers
createUser(user: User): Observable<User> {
  const headers = new HttpHeaders({
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + this.authService.getToken()
  });
  
  return this.http.post<User>(this.apiUrl, user, { headers });
}
```

**PUT Request**
```typescript
// Update user
updateUser(id: number, user: User): Observable<User> {
  return this.http.put<User>(`${this.apiUrl}/${id}`, user);
}
```

**PATCH Request**
```typescript
// Partial update
patchUser(id: number, updates: Partial<User>): Observable<User> {
  return this.http.patch<User>(`${this.apiUrl}/${id}`, updates);
}
```

**DELETE Request**
```typescript
// Delete user
deleteUser(id: number): Observable<void> {
  return this.http.delete<void>(`${this.apiUrl}/${id}`);
}
```

### HTTP Interceptors

**Authentication Interceptor**
```typescript
import { Injectable } from '@angular/core';
import { HttpInterceptor, HttpRequest, HttpHandler, HttpEvent } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable()
export class AuthInterceptor implements HttpInterceptor {
  constructor(private authService: AuthService) {}
  
  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    // Clone request and add authorization header
    const token = this.authService.getToken();
    
    if (token) {
      const authReq = req.clone({
        headers: req.headers.set('Authorization', `Bearer ${token}`)
      });
      return next.handle(authReq);
    }
    
    return next.handle(req);
  }
}

// Register in module
@NgModule({
  providers: [
    {
      provide: HTTP_INTERCEPTORS,
      useClass: AuthInterceptor,
      multi: true
    }
  ]
})
export class CoreModule {}
```

**Error Interceptor**
```typescript
import { Injectable } from '@angular/core';
import { HttpInterceptor, HttpRequest, HttpHandler, HttpEvent, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';

@Injectable()
export class ErrorInterceptor implements HttpInterceptor {
  constructor(
    private router: Router,
    private notificationService: NotificationService
  ) {}
  
  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    return next.handle(req).pipe(
      catchError((error: HttpErrorResponse) => {
        if (error.status === 401) {
          // Unauthorized - redirect to login
          this.router.navigate(['/login']);
        } else if (error.status === 403) {
          // Forbidden
          this.notificationService.error('You do not have permission to perform this action');
        } else if (error.status === 500) {
          // Server error
          this.notificationService.error('Server error. Please try again later.');
        }
        
        return throwError(() => error);
      })
    );
  }
}
```

**Loading Interceptor**
```typescript
import { Injectable } from '@angular/core';
import { HttpInterceptor, HttpRequest, HttpHandler, HttpEvent } from '@angular/common/http';
import { Observable } from 'rxjs';
import { finalize } from 'rxjs/operators';

@Injectable()
export class LoadingInterceptor implements HttpInterceptor {
  private activeRequests = 0;
  
  constructor(private loadingService: LoadingService) {}
  
  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    if (this.activeRequests === 0) {
      this.loadingService.show();
    }
    
    this.activeRequests++;
    
    return next.handle(req).pipe(
      finalize(() => {
        this.activeRequests--;
        if (this.activeRequests === 0) {
          this.loadingService.hide();
        }
      })
    );
  }
}
```

**Caching Interceptor**
```typescript
import { Injectable } from '@angular/core';
import { HttpInterceptor, HttpRequest, HttpHandler, HttpEvent, HttpResponse } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { tap } from 'rxjs/operators';

@Injectable()
export class CachingInterceptor implements HttpInterceptor {
  private cache = new Map<string, HttpResponse<any>>();
  
  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    // Only cache GET requests
    if (req.method !== 'GET') {
      return next.handle(req);
    }
    
    // Check cache
    const cachedResponse = this.cache.get(req.url);
    if (cachedResponse) {
      return of(cachedResponse);
    }
    
    // Make request and cache response
    return next.handle(req).pipe(
      tap(event => {
        if (event instanceof HttpResponse) {
          this.cache.set(req.url, event);
        }
      })
    );
  }
}
```

### Error Handling Patterns

**Service-Level Error Handling**
```typescript
export class UserService {
  constructor(
    private http: HttpClient,
    private errorHandler: ErrorHandlerService
  ) {}
  
  getUsers(): Observable<User[]> {
    return this.http.get<User[]>(this.apiUrl).pipe(
      catchError(error => this.errorHandler.handleError(error))
    );
  }
}

@Injectable({ providedIn: 'root' })
export class ErrorHandlerService {
  handleError(error: HttpErrorResponse): Observable<never> {
    let errorMessage = 'An error occurred';
    
    if (error.error instanceof ErrorEvent) {
      // Client-side error
      errorMessage = `Error: ${error.error.message}`;
    } else {
      // Server-side error
      errorMessage = `Error Code: ${error.status}\nMessage: ${error.message}`;
    }
    
    console.error(errorMessage);
    return throwError(() => new Error(errorMessage));
  }
}
```

**Component-Level Error Handling**
```typescript
export class UserListComponent implements OnInit {
  users: User[] = [];
  error: string | null = null;
  loading = false;
  
  constructor(private userService: UserService) {}
  
  ngOnInit() {
    this.loadUsers();
  }
  
  loadUsers() {
    this.loading = true;
    this.error = null;
    
    this.userService.getUsers().subscribe({
      next: users => {
        this.users = users;
        this.loading = false;
      },
      error: err => {
        this.error = 'Failed to load users. Please try again.';
        this.loading = false;
        console.error(err);
      }
    });
  }
}
```
