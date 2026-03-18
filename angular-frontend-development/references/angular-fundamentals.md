# Angular Fundamentals

Core concepts, architecture, and foundational knowledge for building Angular applications.

---

## Angular Architecture Overview

### The Angular Platform

Angular is a platform and framework for building single-page client applications using HTML, CSS, and TypeScript. It implements core and optional functionality as a set of TypeScript libraries that you import into your applications.

**Core Building Blocks**
- **Modules**: Containers for cohesive blocks of code
- **Components**: Control views (HTML templates)
- **Services**: Shareable business logic
- **Directives**: Modify DOM behavior
- **Pipes**: Transform display values

### NgModules

**Purpose and Structure**

NgModules consolidate components, directives, pipes, and services into cohesive blocks of functionality. Every Angular app has at least one NgModule class, the root module, conventionally named `AppModule`.

**NgModule Metadata Properties**

```typescript
@NgModule({
  declarations: [    // Components, directives, pipes belonging to this module
    AppComponent,
    HeaderComponent
  ],
  imports: [         // Other modules whose exported classes are needed
    BrowserModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [       // Services available to the injector
    AuthService,
    { provide: HTTP_INTERCEPTORS, useClass: AuthInterceptor, multi: true }
  ],
  bootstrap: [       // Root component (only in root module)
    AppComponent
  ],
  exports: [         // Components/directives/pipes available to importing modules
    HeaderComponent
  ]
})
export class AppModule { }
```

**Module Types**

1. **Root Module (AppModule)**
   - Bootstraps the application
   - Imports BrowserModule (only once)
   - Declares root component
   - Imports feature modules

2. **Feature Modules**
   - Organize code by feature area
   - Can be eagerly or lazily loaded
   - Import CommonModule (not BrowserModule)
   - Encapsulate feature-specific functionality

3. **Shared Module**
   - Contains commonly used components, directives, pipes
   - Imported by multiple feature modules
   - Exports Angular modules (CommonModule, FormsModule)
   - Does NOT provide services (use providedIn: 'root' instead)

4. **Core Module**
   - Imported once in AppModule
   - Contains singleton services
   - Guards against re-import with constructor check
   - Houses app-wide components (header, footer)

**Core Module Guard Pattern**

```typescript
export class CoreModule {
  constructor(@Optional() @SkipSelf() parentModule: CoreModule) {
    if (parentModule) {
      throw new Error('CoreModule is already loaded. Import it in AppModule only.');
    }
  }
}
```

### Bootstrapping Process

**Application Startup Sequence**

1. **main.ts**: Entry point
   ```typescript
   platformBrowserDynamic().bootstrapModule(AppModule)
     .catch(err => console.error(err));
   ```

2. **Platform Creation**: Creates browser platform
3. **Module Compilation**: Compiles AppModule
4. **Root Component Creation**: Creates and inserts root component
5. **Change Detection**: Initializes change detection
6. **Application Ready**: App is interactive

**Platform Types**
- `platformBrowserDynamic()`: JIT compilation (development)
- `platformBrowser()`: AOT compilation (production)
- `platformServer()`: Server-side rendering

### Compilation Modes

**Just-in-Time (JIT) Compilation**
- Compiles in the browser at runtime
- Faster development builds
- Larger bundle size (includes compiler)
- Slower initial load
- Used in development (`ng serve`)

**Ahead-of-Time (AOT) Compilation**
- Compiles during build process
- Smaller bundle size (no compiler)
- Faster rendering
- Detects template errors at build time
- Used in production (`ng build --prod`)

**AOT Benefits**
- Faster rendering (pre-compiled templates)
- Fewer asynchronous requests (inlines templates/styles)
- Smaller bundle size (no compiler)
- Early error detection (template errors at build time)
- Better security (no eval or new Function())

---

## TypeScript in Angular

### Essential TypeScript Features

**Decorators**

Decorators are functions that modify classes, properties, methods, or parameters. Angular uses decorators extensively for metadata.

```typescript
// Class decorator
@Component({
  selector: 'app-user',
  templateUrl: './user.component.html'
})
export class UserComponent { }

// Property decorators
@Input() userName: string;
@Output() userSelected = new EventEmitter<User>();
@ViewChild('userForm') form: NgForm;
@ContentChild(TemplateRef) template: TemplateRef<any>;

// Method decorator
@HostListener('click', ['$event'])
onClick(event: MouseEvent) { }

// Parameter decorator
constructor(@Inject(API_URL) private apiUrl: string) { }
```

**Interfaces and Types**

```typescript
// Interface for object shape
interface User {
  id: number;
  name: string;
  email: string;
  role?: 'admin' | 'user';  // Optional with union type
}

// Type alias
type UserId = number | string;
type UserRole = 'admin' | 'user' | 'guest';

// Generic interface
interface ApiResponse<T> {
  data: T;
  status: number;
  message: string;
}

// Usage
const response: ApiResponse<User[]> = await this.http.get<ApiResponse<User[]>>('/api/users');
```

**Access Modifiers**

```typescript
export class UserService {
  public users: User[];           // Accessible everywhere (default)
  private apiUrl: string;         // Only within this class
  protected baseUrl: string;      // This class and subclasses
  readonly maxUsers = 100;        // Cannot be reassigned
  
  // Constructor shorthand
  constructor(
    private http: HttpClient,     // Creates and assigns private property
    public config: AppConfig      // Creates and assigns public property
  ) { }
}
```

**Generics**

```typescript
// Generic service
export class DataService<T> {
  private items: T[] = [];
  
  add(item: T): void {
    this.items.push(item);
  }
  
  getAll(): T[] {
    return this.items;
  }
}

// Usage
const userService = new DataService<User>();
const productService = new DataService<Product>();
```

### TypeScript Configuration

**tsconfig.json Key Settings**

```json
{
  "compilerOptions": {
    "target": "es2020",                    // Output JavaScript version
    "module": "es2020",                    // Module system
    "lib": ["es2020", "dom"],             // Available APIs
    "strict": true,                        // Enable all strict type checking
    "strictNullChecks": true,              // Null and undefined are not assignable
    "noImplicitAny": true,                 // Error on implicit any type
    "esModuleInterop": true,               // Better CommonJS/ES module interop
    "skipLibCheck": true,                  // Skip type checking of declaration files
    "experimentalDecorators": true,        // Enable decorators (required for Angular)
    "emitDecoratorMetadata": true,         // Emit metadata for decorators
    "moduleResolution": "node",            // Module resolution strategy
    "resolveJsonModule": true,             // Import JSON files
    "baseUrl": "./",                       // Base directory for module resolution
    "paths": {                             // Path mapping for imports
      "@app/*": ["src/app/*"],
      "@environments/*": ["src/environments/*"]
    }
  }
}
```

---

## Component Fundamentals

### Component Metadata

**@Component Decorator Properties**

```typescript
@Component({
  selector: 'app-user-profile',           // CSS selector
  templateUrl: './user-profile.component.html',  // External template
  // OR
  template: '<h1>{{ userName }}</h1>',    // Inline template
  
  styleUrls: ['./user-profile.component.css'],   // External styles
  // OR
  styles: ['h1 { color: blue; }'],        // Inline styles
  
  providers: [UserService],                // Component-level services
  changeDetection: ChangeDetectionStrategy.OnPush,  // Change detection strategy
  encapsulation: ViewEncapsulation.Emulated,        // Style encapsulation
  animations: [fadeInAnimation],           // Component animations
  host: {                                  // Host element bindings
    'class': 'user-profile',
    '[class.active]': 'isActive',
    '(click)': 'onClick()'
  },
  exportAs: 'userProfile'                  // Template reference name
})
export class UserProfileComponent { }
```

**Selector Types**

```typescript
// Element selector
selector: 'app-user'              // <app-user></app-user>

// Attribute selector
selector: '[appUser]'             // <div appUser></div>

// Class selector
selector: '.app-user'             // <div class="app-user"></div>

// Multiple selectors
selector: 'app-user, [appUser]'   // Matches either
```

### View Encapsulation

**Encapsulation Modes**

```typescript
// Emulated (default) - Scoped styles using attribute selectors
encapsulation: ViewEncapsulation.Emulated
// Generates: <div _ngcontent-c0>...</div>
// Styles: h1[_ngcontent-c0] { color: blue; }

// None - Global styles (no encapsulation)
encapsulation: ViewEncapsulation.None
// Styles apply globally

// ShadowDom - Native Shadow DOM
encapsulation: ViewEncapsulation.ShadowDom
// Uses browser's Shadow DOM (limited browser support)
```

**When to Use Each Mode**
- **Emulated**: Default, works everywhere, scoped styles
- **None**: Global styles, third-party component styling, CSS frameworks
- **ShadowDom**: True isolation, modern browsers only, web components

---

## Templates and Data Binding

### Binding Syntax

**Interpolation**
```html
<h1>{{ title }}</h1>
<p>{{ user.name }}</p>
<span>{{ 1 + 1 }}</span>
<div>{{ getFullName() }}</div>
```

**Property Binding**
```html
<!-- Element property -->
<img [src]="imageUrl">
<button [disabled]="isDisabled">Click</button>

<!-- Component property -->
<app-user [user]="currentUser"></app-user>

<!-- Attribute binding (for attributes without DOM properties) -->
<td [attr.colspan]="columnSpan">Data</td>
<button [attr.aria-label]="actionLabel">Action</button>

<!-- Class binding -->
<div [class.active]="isActive">Content</div>
<div [class]="'btn btn-primary'">Button</div>
<div [ngClass]="{'active': isActive, 'disabled': isDisabled}">Content</div>

<!-- Style binding -->
<div [style.color]="textColor">Text</div>
<div [style.width.px]="widthValue">Box</div>
<div [ngStyle]="{'color': textColor, 'font-size': fontSize}">Text</div>
```

**Event Binding**
```html
<!-- Standard events -->
<button (click)="onClick()">Click</button>
<input (input)="onInput($event)">
<form (submit)="onSubmit($event)">

<!-- Custom events -->
<app-user (userSelected)="onUserSelected($event)"></app-user>

<!-- Event object -->
<input (keyup)="onKeyUp($event)">
<div (mousemove)="onMouseMove($event)">Move mouse</div>

<!-- Event filtering -->
<input (keyup.enter)="onEnter()">
<input (keyup.escape)="onEscape()">
<input (keyup.shift.a)="onShiftA()">
```

**Two-Way Binding**
```html
<!-- NgModel (requires FormsModule) -->
<input [(ngModel)]="userName">

<!-- Expanded form -->
<input [ngModel]="userName" (ngModelChange)="userName = $event">

<!-- Custom two-way binding -->
<app-sizer [(size)]="fontSize"></app-sizer>

<!-- Component implementation -->
@Input() size: number;
@Output() sizeChange = new EventEmitter<number>();
```

### Template Reference Variables

```html
<!-- Element reference -->
<input #userInput type="text">
<button (click)="logValue(userInput.value)">Log</button>

<!-- Component reference -->
<app-user #userComponent></app-user>
<button (click)="userComponent.refresh()">Refresh</button>

<!-- Directive reference -->
<form #userForm="ngForm">
  <input name="userName" ngModel>
  <button [disabled]="!userForm.valid">Submit</button>
</form>
```

### Template Expressions

**Allowed Operations**
- Property access: `user.name`
- Method calls: `getFullName()`
- Array/object literals: `[1, 2, 3]`, `{name: 'John'}`
- Operators: `+`, `-`, `*`, `/`, `%`, `&&`, `||`, `!`, `?:`
- Pipe operator: `{{ date | date:'short' }}`

**Forbidden Operations**
- Assignments: `=`, `+=`, `-=`
- `new`, `typeof`, `instanceof`
- Chaining with `;` or `,`
- Increment/decrement: `++`, `--`
- Bitwise operators: `|`, `&`
- Global namespace: `window`, `document`, `console`

**Best Practices**
- Keep expressions simple
- No side effects (don't modify state)
- Fast execution (called frequently)
- Idempotent (same input = same output)

---

## Built-in Directives

### Structural Directives

**ngIf**
```html
<!-- Basic usage -->
<div *ngIf="isLoggedIn">Welcome back!</div>

<!-- With else -->
<div *ngIf="isLoggedIn; else loginPrompt">Welcome back!</div>
<ng-template #loginPrompt>Please log in.</ng-template>

<!-- With then and else -->
<div *ngIf="isLoggedIn; then loggedIn else loggedOut"></div>
<ng-template #loggedIn>Welcome!</ng-template>
<ng-template #loggedOut>Please log in.</ng-template>

<!-- With as (store result) -->
<div *ngIf="user$ | async as user">
  {{ user.name }}
</div>
```

**ngFor**
```html
<!-- Basic usage -->
<div *ngFor="let user of users">
  {{ user.name }}
</div>

<!-- With index -->
<div *ngFor="let user of users; let i = index">
  {{ i + 1 }}. {{ user.name }}
</div>

<!-- With trackBy (performance) -->
<div *ngFor="let user of users; trackBy: trackByUserId">
  {{ user.name }}
</div>

// Component
trackByUserId(index: number, user: User): number {
  return user.id;
}

<!-- All local variables -->
<div *ngFor="let user of users; 
             let i = index;
             let first = first;
             let last = last;
             let even = even;
             let odd = odd">
  <span [class.first]="first">{{ user.name }}</span>
</div>
```

**ngSwitch**
```html
<div [ngSwitch]="userRole">
  <div *ngSwitchCase="'admin'">Admin Panel</div>
  <div *ngSwitchCase="'user'">User Dashboard</div>
  <div *ngSwitchCase="'guest'">Guest View</div>
  <div *ngSwitchDefault>Unknown Role</div>
</div>
```

### Attribute Directives

**ngClass**
```html
<!-- Object syntax -->
<div [ngClass]="{'active': isActive, 'disabled': isDisabled}">Content</div>

<!-- Array syntax -->
<div [ngClass]="['btn', 'btn-primary', isLarge ? 'btn-lg' : '']">Button</div>

<!-- String syntax -->
<div [ngClass]="'btn btn-primary'">Button</div>

<!-- Method syntax -->
<div [ngClass]="getClasses()">Content</div>

// Component
getClasses() {
  return {
    'active': this.isActive,
    'disabled': this.isDisabled
  };
}
```

**ngStyle**
```html
<!-- Object syntax -->
<div [ngStyle]="{'color': textColor, 'font-size': fontSize + 'px'}">Text</div>

<!-- Method syntax -->
<div [ngStyle]="getStyles()">Text</div>

// Component
getStyles() {
  return {
    'color': this.textColor,
    'font-size': this.fontSize + 'px',
    'font-weight': this.isBold ? 'bold' : 'normal'
  };
}
```

**ngModel**
```html
<!-- Two-way binding -->
<input [(ngModel)]="userName">

<!-- With change event -->
<input [(ngModel)]="userName" (ngModelChange)="onNameChange($event)">

<!-- With validation -->
<input [(ngModel)]="userName" #name="ngModel" required minlength="3">
<div *ngIf="name.invalid && name.touched">
  <div *ngIf="name.errors?.['required']">Name is required</div>
  <div *ngIf="name.errors?.['minlength']">Name must be at least 3 characters</div>
</div>
```

---

## Progressive Web Apps (PWA)

### Adding PWA Support

**Installation**
```bash
ng add @angular/pwa
```

This command:
- Adds `@angular/service-worker` package
- Creates `ngsw-config.json` (service worker configuration)
- Updates `angular.json` to include service worker
- Adds manifest.webmanifest (app manifest)
- Creates app icons
- Updates `index.html` with manifest and theme color

### Service Worker Configuration

**ngsw-config.json**
```json
{
  "index": "/index.html",
  "assetGroups": [
    {
      "name": "app",
      "installMode": "prefetch",
      "resources": {
        "files": [
          "/favicon.ico",
          "/index.html",
          "/*.css",
          "/*.js"
        ]
      }
    },
    {
      "name": "assets",
      "installMode": "lazy",
      "updateMode": "prefetch",
      "resources": {
        "files": [
          "/assets/**",
          "/*.(eot|svg|cur|jpg|png|webp|gif|otf|ttf|woff|woff2|ani)"
        ]
      }
    }
  ],
  "dataGroups": [
    {
      "name": "api",
      "urls": ["/api/**"],
      "cacheConfig": {
        "maxSize": 100,
        "maxAge": "1h",
        "strategy": "freshness"
      }
    }
  ]
}
```

**Caching Strategies**
- **prefetch**: Download during installation
- **lazy**: Download on first request
- **freshness**: Network first, cache fallback
- **performance**: Cache first, network fallback

### App Manifest

**manifest.webmanifest**
```json
{
  "name": "My Angular App",
  "short_name": "NgApp",
  "theme_color": "#1976d2",
  "background_color": "#fafafa",
  "display": "standalone",
  "scope": "./",
  "start_url": "./",
  "icons": [
    {
      "src": "assets/icons/icon-72x72.png",
      "sizes": "72x72",
      "type": "image/png",
      "purpose": "maskable any"
    },
    {
      "src": "assets/icons/icon-512x512.png",
      "sizes": "512x512",
      "type": "image/png",
      "purpose": "maskable any"
    }
  ]
}
```

### Service Worker Updates

**Checking for Updates**
```typescript
import { SwUpdate } from '@angular/service-worker';

export class AppComponent {
  constructor(private swUpdate: SwUpdate) {
    if (this.swUpdate.isEnabled) {
      this.swUpdate.versionUpdates.subscribe(event => {
        if (event.type === 'VERSION_READY') {
          if (confirm('New version available. Load new version?')) {
            window.location.reload();
          }
        }
      });
    }
  }
}
```

**Manual Update Check**
```typescript
checkForUpdates() {
  this.swUpdate.checkForUpdate().then(() => {
    console.log('Checked for updates');
  });
}
```
