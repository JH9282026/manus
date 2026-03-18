# Components and Modules

Detailed guide to creating, organizing, and managing Angular components and modules for scalable application architecture.

---

## Component Lifecycle

### Lifecycle Hooks Sequence

Angular calls lifecycle hook methods in the following order:

1. **constructor()** — TypeScript class initialization (not an Angular hook)
2. **ngOnChanges()** — When input properties change
3. **ngOnInit()** — After first ngOnChanges, component initialization
4. **ngDoCheck()** — Custom change detection
5. **ngAfterContentInit()** — After content projection initialization
6. **ngAfterContentChecked()** — After every content check
7. **ngAfterViewInit()** — After view initialization
8. **ngAfterViewChecked()** — After every view check
9. **ngOnDestroy()** — Before component destruction

### Lifecycle Hook Details

**ngOnChanges(changes: SimpleChanges)**

```typescript
export class UserComponent implements OnChanges {
  @Input() user: User;
  @Input() role: string;
  
  ngOnChanges(changes: SimpleChanges) {
    // Called before ngOnInit and whenever input properties change
    if (changes['user']) {
      console.log('Previous:', changes['user'].previousValue);
      console.log('Current:', changes['user'].currentValue);
      console.log('First change:', changes['user'].firstChange);
    }
    
    if (changes['role'] && !changes['role'].firstChange) {
      this.updatePermissions();
    }
  }
}
```

**When to use:**
- React to input property changes
- Perform actions when specific inputs change
- Compare previous and current values

**ngOnInit()**

```typescript
export class UserComponent implements OnInit {
  users: User[];
  
  constructor(private userService: UserService) {
    // Constructor: Dependency injection only
    // Do NOT fetch data or perform complex logic here
  }
  
  ngOnInit() {
    // Initialization logic here
    this.loadUsers();
    this.setupForm();
    this.subscribeToEvents();
  }
  
  private loadUsers() {
    this.userService.getUsers().subscribe(users => {
      this.users = users;
    });
  }
}
```

**When to use:**
- Initialize component data
- Fetch data from services
- Set up subscriptions
- Complex initialization logic
- Access input properties (they're set by this point)

**ngDoCheck()**

```typescript
export class UserListComponent implements DoCheck {
  @Input() users: User[];
  private previousLength: number;
  
  ngDoCheck() {
    // Custom change detection
    // Called very frequently - keep logic lightweight
    if (this.users && this.users.length !== this.previousLength) {
      console.log('User list length changed');
      this.previousLength = this.users.length;
      this.updateStatistics();
    }
  }
}
```

**When to use:**
- Detect changes Angular doesn't catch automatically
- Monitor array/object mutations
- Custom change detection logic
- **Warning**: Called very frequently, keep logic minimal

**ngAfterContentInit()**

```typescript
export class TabGroupComponent implements AfterContentInit {
  @ContentChildren(TabComponent) tabs: QueryList<TabComponent>;
  
  ngAfterContentInit() {
    // Content projection is initialized
    console.log('Tabs:', this.tabs.length);
    this.tabs.first.activate();
  }
}
```

**When to use:**
- Access projected content (ng-content)
- Initialize after content is available
- Set up content-based logic

**ngAfterViewInit()**

```typescript
export class UserFormComponent implements AfterViewInit {
  @ViewChild('nameInput') nameInput: ElementRef;
  @ViewChildren(InputComponent) inputs: QueryList<InputComponent>;
  
  ngAfterViewInit() {
    // View is fully initialized
    this.nameInput.nativeElement.focus();
    
    // Safe to access view children
    this.inputs.forEach(input => input.validate());
  }
}
```

**When to use:**
- Access view children and DOM elements
- Initialize third-party libraries that need DOM
- Manipulate view after rendering
- **Warning**: Don't update component properties here (causes ExpressionChangedAfterItHasBeenCheckedError)

**ngOnDestroy()**

```typescript
export class UserComponent implements OnInit, OnDestroy {
  private destroy$ = new Subject<void>();
  private intervalId: number;
  
  ngOnInit() {
    // Subscription with takeUntil
    this.userService.getUsers()
      .pipe(takeUntil(this.destroy$))
      .subscribe(users => this.users = users);
    
    // Timer/interval
    this.intervalId = window.setInterval(() => this.refresh(), 5000);
  }
  
  ngOnDestroy() {
    // Clean up subscriptions
    this.destroy$.next();
    this.destroy$.complete();
    
    // Clear timers
    if (this.intervalId) {
      clearInterval(this.intervalId);
    }
    
    // Remove event listeners
    // Close connections
    // Release resources
  }
}
```

**When to use:**
- Unsubscribe from observables
- Clear timers and intervals
- Remove event listeners
- Clean up resources
- Prevent memory leaks

### Lifecycle Best Practices

**Constructor vs. ngOnInit**
- **Constructor**: Dependency injection only, no complex logic
- **ngOnInit**: Initialization logic, data fetching, subscriptions

**Memory Leak Prevention**
```typescript
// Pattern 1: takeUntil with destroy subject
private destroy$ = new Subject<void>();

ngOnInit() {
  this.dataService.getData()
    .pipe(takeUntil(this.destroy$))
    .subscribe(data => this.data = data);
}

ngOnDestroy() {
  this.destroy$.next();
  this.destroy$.complete();
}

// Pattern 2: async pipe (auto-unsubscribes)
data$ = this.dataService.getData();
// Template: {{ data$ | async }}

// Pattern 3: Manual subscription tracking
private subscriptions = new Subscription();

ngOnInit() {
  this.subscriptions.add(
    this.dataService.getData().subscribe(data => this.data = data)
  );
}

ngOnDestroy() {
  this.subscriptions.unsubscribe();
}
```

---

## Component Communication

### Parent to Child: @Input()

**Basic Input**
```typescript
// Child component
export class UserCardComponent {
  @Input() user: User;
  @Input() showDetails = false;  // Default value
}

// Parent template
<app-user-card [user]="currentUser" [showDetails]="true"></app-user-card>
```

**Input with Setter**
```typescript
export class UserCardComponent {
  private _user: User;
  
  @Input()
  set user(value: User) {
    this._user = value;
    this.loadUserDetails();  // Side effect when input changes
  }
  
  get user(): User {
    return this._user;
  }
}
```

**Input Alias**
```typescript
export class UserCardComponent {
  @Input('userData') user: User;  // External name: userData, internal: user
}

// Usage
<app-user-card [userData]="currentUser"></app-user-card>
```

**Required Inputs (Angular 16+)**
```typescript
export class UserCardComponent {
  @Input({ required: true }) user: User;
}
```

### Child to Parent: @Output()

**Basic Output**
```typescript
// Child component
export class UserCardComponent {
  @Output() userSelected = new EventEmitter<User>();
  @Output() deleteRequested = new EventEmitter<number>();
  
  onSelect() {
    this.userSelected.emit(this.user);
  }
  
  onDelete() {
    this.deleteRequested.emit(this.user.id);
  }
}

// Parent template
<app-user-card 
  [user]="user"
  (userSelected)="onUserSelected($event)"
  (deleteRequested)="onDeleteUser($event)">
</app-user-card>

// Parent component
export class UserListComponent {
  onUserSelected(user: User) {
    console.log('Selected:', user);
  }
  
  onDeleteUser(userId: number) {
    this.deleteUser(userId);
  }
}
```

**Output Alias**
```typescript
export class UserCardComponent {
  @Output('selected') userSelected = new EventEmitter<User>();
}

// Usage
<app-user-card (selected)="onUserSelected($event)"></app-user-card>
```

### Two-Way Binding: @Input() + @Output()

**Custom Two-Way Binding**
```typescript
// Child component
export class CounterComponent {
  @Input() count: number = 0;
  @Output() countChange = new EventEmitter<number>();  // Must be: propertyName + 'Change'
  
  increment() {
    this.count++;
    this.countChange.emit(this.count);
  }
  
  decrement() {
    this.count--;
    this.countChange.emit(this.count);
  }
}

// Parent template
<app-counter [(count)]="totalCount"></app-counter>

// Expanded form (equivalent)
<app-counter [count]="totalCount" (countChange)="totalCount = $event"></app-counter>
```

### Sibling Communication: Shared Service

**Shared Service**
```typescript
@Injectable({ providedIn: 'root' })
export class UserSelectionService {
  private selectedUserSubject = new BehaviorSubject<User | null>(null);
  selectedUser$ = this.selectedUserSubject.asObservable();
  
  selectUser(user: User) {
    this.selectedUserSubject.next(user);
  }
  
  clearSelection() {
    this.selectedUserSubject.next(null);
  }
}

// Component A (emitter)
export class UserListComponent {
  constructor(private selectionService: UserSelectionService) {}
  
  onUserClick(user: User) {
    this.selectionService.selectUser(user);
  }
}

// Component B (receiver)
export class UserDetailsComponent implements OnInit {
  selectedUser$: Observable<User | null>;
  
  constructor(private selectionService: UserSelectionService) {}
  
  ngOnInit() {
    this.selectedUser$ = this.selectionService.selectedUser$;
  }
}

// Template
<div *ngIf="selectedUser$ | async as user">
  {{ user.name }}
</div>
```

### ViewChild and ContentChild

**@ViewChild - Access Child Component**
```typescript
export class ParentComponent implements AfterViewInit {
  @ViewChild(ChildComponent) child: ChildComponent;
  @ViewChild('userForm') form: NgForm;
  @ViewChild('nameInput', { read: ElementRef }) nameInput: ElementRef;
  
  ngAfterViewInit() {
    // Access child component methods
    this.child.refresh();
    
    // Access form
    console.log(this.form.valid);
    
    // Access DOM element
    this.nameInput.nativeElement.focus();
  }
}
```

**@ViewChildren - Access Multiple Children**
```typescript
export class ParentComponent implements AfterViewInit {
  @ViewChildren(ChildComponent) children: QueryList<ChildComponent>;
  
  ngAfterViewInit() {
    this.children.forEach(child => child.initialize());
    
    // React to changes
    this.children.changes.subscribe(() => {
      console.log('Children changed');
    });
  }
}
```

**@ContentChild - Access Projected Content**
```typescript
// Parent component
export class TabGroupComponent implements AfterContentInit {
  @ContentChild(TabComponent) firstTab: TabComponent;
  @ContentChildren(TabComponent) tabs: QueryList<TabComponent>;
  
  ngAfterContentInit() {
    this.firstTab.activate();
  }
}

// Usage
<app-tab-group>
  <app-tab title="Tab 1">Content 1</app-tab>
  <app-tab title="Tab 2">Content 2</app-tab>
</app-tab-group>
```

---

## Content Projection

### Single-Slot Projection

**Basic ng-content**
```typescript
// Card component
@Component({
  selector: 'app-card',
  template: `
    <div class="card">
      <ng-content></ng-content>
    </div>
  `
})
export class CardComponent {}

// Usage
<app-card>
  <h2>Title</h2>
  <p>Content goes here</p>
</app-card>
```

### Multi-Slot Projection

**Named Slots**
```typescript
// Card component with slots
@Component({
  selector: 'app-card',
  template: `
    <div class="card">
      <div class="card-header">
        <ng-content select="[card-header]"></ng-content>
      </div>
      <div class="card-body">
        <ng-content select="[card-body]"></ng-content>
      </div>
      <div class="card-footer">
        <ng-content select="[card-footer]"></ng-content>
      </div>
    </div>
  `
})
export class CardComponent {}

// Usage
<app-card>
  <div card-header>
    <h2>Card Title</h2>
  </div>
  <div card-body>
    <p>Card content</p>
  </div>
  <div card-footer>
    <button>Action</button>
  </div>
</app-card>
```

**Select by Component**
```typescript
@Component({
  selector: 'app-panel',
  template: `
    <div class="panel">
      <ng-content select="app-panel-header"></ng-content>
      <ng-content select="app-panel-body"></ng-content>
    </div>
  `
})
export class PanelComponent {}

// Usage
<app-panel>
  <app-panel-header>Header</app-panel-header>
  <app-panel-body>Body</app-panel-body>
</app-panel>
```

### Conditional Content Projection

**ng-template with ngTemplateOutlet**
```typescript
@Component({
  selector: 'app-list',
  template: `
    <div *ngFor="let item of items">
      <ng-container *ngTemplateOutlet="itemTemplate; context: { $implicit: item }"></ng-container>
    </div>
    
    <!-- Default template if none provided -->
    <ng-template #defaultTemplate let-item>
      {{ item.name }}
    </ng-template>
  `
})
export class ListComponent {
  @Input() items: any[];
  @ContentChild(TemplateRef) itemTemplate: TemplateRef<any>;
}

// Usage
<app-list [items]="users">
  <ng-template let-user>
    <div class="user-card">
      <h3>{{ user.name }}</h3>
      <p>{{ user.email }}</p>
    </div>
  </ng-template>
</app-list>
```

---

## Custom Directives

### Attribute Directive

**Basic Attribute Directive**
```typescript
import { Directive, ElementRef, HostListener, Input } from '@angular/core';

@Directive({
  selector: '[appHighlight]'
})
export class HighlightDirective {
  @Input() appHighlight = 'yellow';  // Default color
  @Input() defaultColor = 'transparent';
  
  constructor(private el: ElementRef) {}
  
  @HostListener('mouseenter') onMouseEnter() {
    this.highlight(this.appHighlight);
  }
  
  @HostListener('mouseleave') onMouseLeave() {
    this.highlight(this.defaultColor);
  }
  
  private highlight(color: string) {
    this.el.nativeElement.style.backgroundColor = color;
  }
}

// Usage
<p appHighlight="lightblue">Hover over me</p>
<p [appHighlight]="color" [defaultColor]="'white'">Dynamic color</p>
```

**Directive with Renderer2 (Safer)**
```typescript
import { Directive, ElementRef, Renderer2, HostListener } from '@angular/core';

@Directive({
  selector: '[appHighlight]'
})
export class HighlightDirective {
  constructor(
    private el: ElementRef,
    private renderer: Renderer2
  ) {}
  
  @HostListener('mouseenter') onMouseEnter() {
    this.renderer.setStyle(this.el.nativeElement, 'backgroundColor', 'yellow');
    this.renderer.addClass(this.el.nativeElement, 'highlighted');
  }
  
  @HostListener('mouseleave') onMouseLeave() {
    this.renderer.removeStyle(this.el.nativeElement, 'backgroundColor');
    this.renderer.removeClass(this.el.nativeElement, 'highlighted');
  }
}
```

### Structural Directive

**Custom *ngIf Alternative**
```typescript
import { Directive, Input, TemplateRef, ViewContainerRef } from '@angular/core';

@Directive({
  selector: '[appUnless]'
})
export class UnlessDirective {
  private hasView = false;
  
  constructor(
    private templateRef: TemplateRef<any>,
    private viewContainer: ViewContainerRef
  ) {}
  
  @Input() set appUnless(condition: boolean) {
    if (!condition && !this.hasView) {
      this.viewContainer.createEmbeddedView(this.templateRef);
      this.hasView = true;
    } else if (condition && this.hasView) {
      this.viewContainer.clear();
      this.hasView = false;
    }
  }
}

// Usage
<div *appUnless="isLoggedIn">
  Please log in.
</div>
```

**Permission Directive**
```typescript
@Directive({
  selector: '[appHasPermission]'
})
export class HasPermissionDirective implements OnInit {
  @Input() appHasPermission: string;
  
  constructor(
    private templateRef: TemplateRef<any>,
    private viewContainer: ViewContainerRef,
    private authService: AuthService
  ) {}
  
  ngOnInit() {
    this.authService.hasPermission(this.appHasPermission).subscribe(hasPermission => {
      if (hasPermission) {
        this.viewContainer.createEmbeddedView(this.templateRef);
      } else {
        this.viewContainer.clear();
      }
    });
  }
}

// Usage
<button *appHasPermission="'admin'">Delete User</button>
```

---

## Custom Pipes

### Pure Pipe (Default)

**Basic Transform Pipe**
```typescript
import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'exponential'
})
export class ExponentialPipe implements PipeTransform {
  transform(value: number, exponent = 1): number {
    return Math.pow(value, exponent);
  }
}

// Usage
{{ 2 | exponential:3 }}  <!-- Output: 8 -->
```

**String Manipulation Pipe**
```typescript
@Pipe({
  name: 'truncate'
})
export class TruncatePipe implements PipeTransform {
  transform(value: string, limit = 50, ellipsis = '...'): string {
    if (!value) return '';
    if (value.length <= limit) return value;
    return value.substring(0, limit) + ellipsis;
  }
}

// Usage
{{ longText | truncate:100:'...' }}
```

**Filter Pipe**
```typescript
@Pipe({
  name: 'filter'
})
export class FilterPipe implements PipeTransform {
  transform(items: any[], searchText: string, property: string): any[] {
    if (!items || !searchText) return items;
    
    searchText = searchText.toLowerCase();
    return items.filter(item => {
      return item[property].toLowerCase().includes(searchText);
    });
  }
}

// Usage
<div *ngFor="let user of users | filter:searchText:'name'">
  {{ user.name }}
</div>
```

### Impure Pipe

**Impure Filter Pipe (Updates on Every Change)**
```typescript
@Pipe({
  name: 'filter',
  pure: false  // Impure pipe - runs on every change detection
})
export class FilterPipe implements PipeTransform {
  transform(items: any[], searchText: string): any[] {
    if (!items || !searchText) return items;
    return items.filter(item => item.name.includes(searchText));
  }
}
```

**Warning**: Impure pipes run on every change detection cycle. Use sparingly as they can impact performance.

### Async Pipe Pattern

**Observable in Template**
```typescript
export class UserListComponent {
  users$: Observable<User[]>;
  
  constructor(private userService: UserService) {
    this.users$ = this.userService.getUsers();
  }
}

// Template
<div *ngIf="users$ | async as users; else loading">
  <div *ngFor="let user of users">
    {{ user.name }}
  </div>
</div>
<ng-template #loading>Loading...</ng-template>
```

---

## Module Organization Patterns

### Core Module Pattern

**core.module.ts**
```typescript
import { NgModule, Optional, SkipSelf } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HTTP_INTERCEPTORS } from '@angular/common/http';

// Services
import { AuthService } from './services/auth.service';
import { LoggerService } from './services/logger.service';

// Interceptors
import { AuthInterceptor } from './interceptors/auth.interceptor';
import { ErrorInterceptor } from './interceptors/error.interceptor';

// Guards
import { AuthGuard } from './guards/auth.guard';

// Components
import { HeaderComponent } from './components/header/header.component';
import { FooterComponent } from './components/footer/footer.component';

@NgModule({
  declarations: [
    HeaderComponent,
    FooterComponent
  ],
  imports: [
    CommonModule
  ],
  exports: [
    HeaderComponent,
    FooterComponent
  ],
  providers: [
    AuthService,
    LoggerService,
    AuthGuard,
    {
      provide: HTTP_INTERCEPTORS,
      useClass: AuthInterceptor,
      multi: true
    },
    {
      provide: HTTP_INTERCEPTORS,
      useClass: ErrorInterceptor,
      multi: true
    }
  ]
})
export class CoreModule {
  constructor(@Optional() @SkipSelf() parentModule: CoreModule) {
    if (parentModule) {
      throw new Error('CoreModule is already loaded. Import it in AppModule only.');
    }
  }
}
```

### Shared Module Pattern

**shared.module.ts**
```typescript
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

// Third-party modules
import { MaterialModule } from './material.module';

// Components
import { ButtonComponent } from './components/button/button.component';
import { CardComponent } from './components/card/card.component';
import { ModalComponent } from './components/modal/modal.component';

// Directives
import { HighlightDirective } from './directives/highlight.directive';
import { AutofocusDirective } from './directives/autofocus.directive';

// Pipes
import { TruncatePipe } from './pipes/truncate.pipe';
import { SafeHtmlPipe } from './pipes/safe-html.pipe';

@NgModule({
  declarations: [
    ButtonComponent,
    CardComponent,
    ModalComponent,
    HighlightDirective,
    AutofocusDirective,
    TruncatePipe,
    SafeHtmlPipe
  ],
  imports: [
    CommonModule,
    FormsModule,
    ReactiveFormsModule,
    MaterialModule
  ],
  exports: [
    // Angular modules
    CommonModule,
    FormsModule,
    ReactiveFormsModule,
    
    // Third-party modules
    MaterialModule,
    
    // Custom components
    ButtonComponent,
    CardComponent,
    ModalComponent,
    
    // Directives
    HighlightDirective,
    AutofocusDirective,
    
    // Pipes
    TruncatePipe,
    SafeHtmlPipe
  ]
})
export class SharedModule {}
```

### Feature Module Pattern

**users/users.module.ts**
```typescript
import { NgModule } from '@angular/core';
import { SharedModule } from '../shared/shared.module';
import { UsersRoutingModule } from './users-routing.module';

// Components
import { UserListComponent } from './components/user-list/user-list.component';
import { UserDetailComponent } from './components/user-detail/user-detail.component';
import { UserFormComponent } from './components/user-form/user-form.component';

// Services
import { UserService } from './services/user.service';

@NgModule({
  declarations: [
    UserListComponent,
    UserDetailComponent,
    UserFormComponent
  ],
  imports: [
    SharedModule,
    UsersRoutingModule
  ],
  providers: [
    UserService  // Feature-scoped service
  ]
})
export class UsersModule {}
```

**users/users-routing.module.ts**
```typescript
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { UserListComponent } from './components/user-list/user-list.component';
import { UserDetailComponent } from './components/user-detail/user-detail.component';
import { UserFormComponent } from './components/user-form/user-form.component';

const routes: Routes = [
  {
    path: '',
    component: UserListComponent
  },
  {
    path: 'new',
    component: UserFormComponent
  },
  {
    path: ':id',
    component: UserDetailComponent
  },
  {
    path: ':id/edit',
    component: UserFormComponent
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class UsersRoutingModule {}
```
