# Routing and State Management

Comprehensive guide to Angular routing, navigation, route guards, lazy loading, and state management patterns including NgRx.

---

## Angular Router Fundamentals

### Router Setup

**App Routing Module**
```typescript
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { HomeComponent } from './components/home/home.component';
import { AboutComponent } from './components/about/about.component';
import { NotFoundComponent } from './components/not-found/not-found.component';

const routes: Routes = [
  { path: '', redirectTo: '/home', pathMatch: 'full' },
  { path: 'home', component: HomeComponent },
  { path: 'about', component: AboutComponent },
  { path: '**', component: NotFoundComponent }  // Wildcard route (must be last)
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
```

**Router Outlet**
```html
<!-- app.component.html -->
<nav>
  <a routerLink="/home" routerLinkActive="active">Home</a>
  <a routerLink="/about" routerLinkActive="active">About</a>
</nav>

<router-outlet></router-outlet>
```

### Route Configuration

**Basic Routes**
```typescript
const routes: Routes = [
  // Static path
  { path: 'home', component: HomeComponent },
  
  // Path with parameter
  { path: 'users/:id', component: UserDetailComponent },
  
  // Multiple parameters
  { path: 'posts/:category/:id', component: PostDetailComponent },
  
  // Redirect
  { path: '', redirectTo: '/home', pathMatch: 'full' },
  
  // Wildcard (404)
  { path: '**', component: NotFoundComponent }
];
```

**Route Data and Title**
```typescript
const routes: Routes = [
  {
    path: 'admin',
    component: AdminComponent,
    data: { 
      title: 'Admin Dashboard',
      breadcrumb: 'Admin',
      roles: ['admin']
    }
  }
];

// Access in component
export class AdminComponent implements OnInit {
  constructor(private route: ActivatedRoute) {}
  
  ngOnInit() {
    this.route.data.subscribe(data => {
      console.log(data['title']);  // 'Admin Dashboard'
      console.log(data['roles']);  // ['admin']
    });
  }
}
```

**Child Routes**
```typescript
const routes: Routes = [
  {
    path: 'users',
    component: UsersComponent,
    children: [
      { path: '', component: UserListComponent },
      { path: ':id', component: UserDetailComponent },
      { path: ':id/edit', component: UserEditComponent }
    ]
  }
];

// UsersComponent template needs <router-outlet>
<div class="users-container">
  <h1>Users</h1>
  <router-outlet></router-outlet>  <!-- Child routes render here -->
</div>
```

### Navigation

**RouterLink Directive**
```html
<!-- Basic link -->
<a routerLink="/users">Users</a>

<!-- With parameter -->
<a [routerLink]="['/users', userId]">User Detail</a>

<!-- With query params -->
<a [routerLink]="['/users']" [queryParams]="{page: 1, sort: 'name'}">Users</a>

<!-- With fragment -->
<a [routerLink]="['/about']" fragment="team">About Team</a>

<!-- Active link styling -->
<a routerLink="/users" routerLinkActive="active">Users</a>

<!-- Active with exact match -->
<a routerLink="/" routerLinkActive="active" [routerLinkActiveOptions]="{exact: true}">Home</a>
```

**Programmatic Navigation**
```typescript
export class UserListComponent {
  constructor(private router: Router) {}
  
  // Navigate to route
  goToUser(userId: number) {
    this.router.navigate(['/users', userId]);
  }
  
  // Navigate with query params
  goToUsers() {
    this.router.navigate(['/users'], {
      queryParams: { page: 1, sort: 'name' }
    });
  }
  
  // Navigate relative to current route
  goToEdit() {
    this.router.navigate(['edit'], { relativeTo: this.route });
  }
  
  // Navigate with state
  goToUserWithState(user: User) {
    this.router.navigate(['/users', user.id], {
      state: { user: user }
    });
  }
  
  // Navigate by URL
  goToAbout() {
    this.router.navigateByUrl('/about');
  }
}
```

### Route Parameters

**Reading Route Parameters**
```typescript
export class UserDetailComponent implements OnInit {
  userId: number;
  
  constructor(private route: ActivatedRoute) {}
  
  ngOnInit() {
    // Snapshot (one-time read)
    this.userId = +this.route.snapshot.paramMap.get('id');
    
    // Observable (reactive to changes)
    this.route.paramMap.subscribe(params => {
      this.userId = +params.get('id');
      this.loadUser(this.userId);
    });
  }
}
```

**Reading Query Parameters**
```typescript
export class UserListComponent implements OnInit {
  page: number;
  sort: string;
  
  constructor(private route: ActivatedRoute) {}
  
  ngOnInit() {
    // Snapshot
    this.page = +this.route.snapshot.queryParamMap.get('page') || 1;
    this.sort = this.route.snapshot.queryParamMap.get('sort') || 'name';
    
    // Observable
    this.route.queryParamMap.subscribe(params => {
      this.page = +params.get('page') || 1;
      this.sort = params.get('sort') || 'name';
      this.loadUsers();
    });
  }
}
```

**Accessing Navigation State**
```typescript
export class UserDetailComponent implements OnInit {
  constructor(private router: Router) {}
  
  ngOnInit() {
    const navigation = this.router.getCurrentNavigation();
    if (navigation?.extras.state) {
      const user = navigation.extras.state['user'];
      console.log(user);
    }
  }
}
```

---

## Route Guards

### CanActivate Guard

**Authentication Guard**
```typescript
import { Injectable } from '@angular/core';
import { CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot, Router } from '@angular/router';
import { Observable } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class AuthGuard implements CanActivate {
  constructor(
    private authService: AuthService,
    private router: Router
  ) {}
  
  canActivate(
    route: ActivatedRouteSnapshot,
    state: RouterStateSnapshot
  ): boolean | Observable<boolean> | Promise<boolean> {
    if (this.authService.isLoggedIn()) {
      return true;
    }
    
    // Store attempted URL for redirecting after login
    this.router.navigate(['/login'], {
      queryParams: { returnUrl: state.url }
    });
    return false;
  }
}

// Apply to route
const routes: Routes = [
  {
    path: 'admin',
    component: AdminComponent,
    canActivate: [AuthGuard]
  }
];
```

**Role-Based Guard**
```typescript
@Injectable({ providedIn: 'root' })
export class RoleGuard implements CanActivate {
  constructor(
    private authService: AuthService,
    private router: Router
  ) {}
  
  canActivate(
    route: ActivatedRouteSnapshot,
    state: RouterStateSnapshot
  ): boolean {
    const requiredRoles = route.data['roles'] as string[];
    const userRoles = this.authService.getUserRoles();
    
    const hasRole = requiredRoles.some(role => userRoles.includes(role));
    
    if (hasRole) {
      return true;
    }
    
    this.router.navigate(['/unauthorized']);
    return false;
  }
}

// Apply to route
const routes: Routes = [
  {
    path: 'admin',
    component: AdminComponent,
    canActivate: [AuthGuard, RoleGuard],
    data: { roles: ['admin', 'superuser'] }
  }
];
```

### CanActivateChild Guard

```typescript
@Injectable({ providedIn: 'root' })
export class AdminGuard implements CanActivateChild {
  constructor(private authService: AuthService) {}
  
  canActivateChild(
    route: ActivatedRouteSnapshot,
    state: RouterStateSnapshot
  ): boolean {
    return this.authService.hasRole('admin');
  }
}

// Apply to parent route (protects all children)
const routes: Routes = [
  {
    path: 'admin',
    component: AdminComponent,
    canActivateChild: [AdminGuard],
    children: [
      { path: 'users', component: AdminUsersComponent },
      { path: 'settings', component: AdminSettingsComponent }
    ]
  }
];
```

### CanDeactivate Guard

**Unsaved Changes Guard**
```typescript
export interface CanComponentDeactivate {
  canDeactivate: () => boolean | Observable<boolean>;
}

@Injectable({ providedIn: 'root' })
export class UnsavedChangesGuard implements CanDeactivate<CanComponentDeactivate> {
  canDeactivate(
    component: CanComponentDeactivate
  ): boolean | Observable<boolean> {
    return component.canDeactivate ? component.canDeactivate() : true;
  }
}

// Component implementation
export class UserEditComponent implements CanComponentDeactivate {
  userForm: FormGroup;
  
  canDeactivate(): boolean {
    if (this.userForm.dirty) {
      return confirm('You have unsaved changes. Do you really want to leave?');
    }
    return true;
  }
}

// Apply to route
const routes: Routes = [
  {
    path: 'users/:id/edit',
    component: UserEditComponent,
    canDeactivate: [UnsavedChangesGuard]
  }
];
```

### CanLoad Guard

**Prevent Lazy Module Loading**
```typescript
@Injectable({ providedIn: 'root' })
export class AuthLoadGuard implements CanLoad {
  constructor(private authService: AuthService) {}
  
  canLoad(route: Route): boolean {
    if (this.authService.isLoggedIn()) {
      return true;
    }
    return false;
  }
}

// Apply to lazy route
const routes: Routes = [
  {
    path: 'admin',
    loadChildren: () => import('./admin/admin.module').then(m => m.AdminModule),
    canLoad: [AuthLoadGuard]
  }
];
```

### Resolve Guard

**Pre-fetch Data**
```typescript
@Injectable({ providedIn: 'root' })
export class UserResolver implements Resolve<User> {
  constructor(private userService: UserService) {}
  
  resolve(
    route: ActivatedRouteSnapshot,
    state: RouterStateSnapshot
  ): Observable<User> {
    const id = +route.paramMap.get('id');
    return this.userService.getUser(id);
  }
}

// Apply to route
const routes: Routes = [
  {
    path: 'users/:id',
    component: UserDetailComponent,
    resolve: { user: UserResolver }
  }
];

// Access resolved data in component
export class UserDetailComponent implements OnInit {
  user: User;
  
  constructor(private route: ActivatedRoute) {}
  
  ngOnInit() {
    this.route.data.subscribe(data => {
      this.user = data['user'];
    });
  }
}
```

---

## Lazy Loading

### Feature Module Lazy Loading

**App Routing**
```typescript
const routes: Routes = [
  {
    path: 'users',
    loadChildren: () => import('./users/users.module').then(m => m.UsersModule)
  },
  {
    path: 'admin',
    loadChildren: () => import('./admin/admin.module').then(m => m.AdminModule),
    canLoad: [AuthGuard]
  }
];
```

**Feature Module Routing**
```typescript
// users-routing.module.ts
const routes: Routes = [
  { path: '', component: UserListComponent },
  { path: ':id', component: UserDetailComponent },
  { path: ':id/edit', component: UserEditComponent }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],  // forChild, not forRoot
  exports: [RouterModule]
})
export class UsersRoutingModule {}
```

### Preloading Strategies

**Preload All Modules**
```typescript
import { PreloadAllModules } from '@angular/router';

@NgModule({
  imports: [RouterModule.forRoot(routes, {
    preloadingStrategy: PreloadAllModules
  })],
  exports: [RouterModule]
})
export class AppRoutingModule {}
```

**Custom Preloading Strategy**
```typescript
import { PreloadingStrategy, Route } from '@angular/router';
import { Observable, of } from 'rxjs';

export class CustomPreloadingStrategy implements PreloadingStrategy {
  preload(route: Route, load: () => Observable<any>): Observable<any> {
    // Preload if route data has preload: true
    return route.data && route.data['preload'] ? load() : of(null);
  }
}

// Apply strategy
@NgModule({
  imports: [RouterModule.forRoot(routes, {
    preloadingStrategy: CustomPreloadingStrategy
  })],
  providers: [CustomPreloadingStrategy],
  exports: [RouterModule]
})
export class AppRoutingModule {}

// Mark routes for preloading
const routes: Routes = [
  {
    path: 'users',
    loadChildren: () => import('./users/users.module').then(m => m.UsersModule),
    data: { preload: true }
  }
];
```

---

## State Management with NgRx

### NgRx Setup

**Installation**
```bash
npm install @ngrx/store @ngrx/effects @ngrx/entity @ngrx/store-devtools
```

**Store Module Setup**
```typescript
import { StoreModule } from '@ngrx/store';
import { EffectsModule } from '@ngrx/effects';
import { StoreDevtoolsModule } from '@ngrx/store-devtools';

@NgModule({
  imports: [
    StoreModule.forRoot({}),
    EffectsModule.forRoot([]),
    StoreDevtoolsModule.instrument({
      maxAge: 25,
      logOnly: environment.production
    })
  ]
})
export class AppModule {}
```

### Actions

**Define Actions**
```typescript
import { createAction, props } from '@ngrx/store';
import { User } from '../models/user.model';

// Load users
export const loadUsers = createAction('[User List] Load Users');
export const loadUsersSuccess = createAction(
  '[User API] Load Users Success',
  props<{ users: User[] }>()
);
export const loadUsersFailure = createAction(
  '[User API] Load Users Failure',
  props<{ error: string }>()
);

// Add user
export const addUser = createAction(
  '[User Form] Add User',
  props<{ user: User }>()
);
export const addUserSuccess = createAction(
  '[User API] Add User Success',
  props<{ user: User }>()
);

// Update user
export const updateUser = createAction(
  '[User Form] Update User',
  props<{ user: User }>()
);

// Delete user
export const deleteUser = createAction(
  '[User List] Delete User',
  props<{ id: number }>()
);
```

### Reducer

**Define State and Reducer**
```typescript
import { createReducer, on } from '@ngrx/store';
import * as UserActions from './user.actions';
import { User } from '../models/user.model';

export interface UserState {
  users: User[];
  loading: boolean;
  error: string | null;
}

export const initialState: UserState = {
  users: [],
  loading: false,
  error: null
};

export const userReducer = createReducer(
  initialState,
  
  // Load users
  on(UserActions.loadUsers, state => ({
    ...state,
    loading: true,
    error: null
  })),
  
  on(UserActions.loadUsersSuccess, (state, { users }) => ({
    ...state,
    users,
    loading: false
  })),
  
  on(UserActions.loadUsersFailure, (state, { error }) => ({
    ...state,
    loading: false,
    error
  })),
  
  // Add user
  on(UserActions.addUserSuccess, (state, { user }) => ({
    ...state,
    users: [...state.users, user]
  })),
  
  // Update user
  on(UserActions.updateUser, (state, { user }) => ({
    ...state,
    users: state.users.map(u => u.id === user.id ? user : u)
  })),
  
  // Delete user
  on(UserActions.deleteUser, (state, { id }) => ({
    ...state,
    users: state.users.filter(u => u.id !== id)
  }))
);
```

**Register Reducer**
```typescript
import { StoreModule } from '@ngrx/store';
import { userReducer } from './store/user.reducer';

@NgModule({
  imports: [
    StoreModule.forFeature('users', userReducer)
  ]
})
export class UsersModule {}
```

### Selectors

**Create Selectors**
```typescript
import { createFeatureSelector, createSelector } from '@ngrx/store';
import { UserState } from './user.reducer';

// Feature selector
export const selectUserState = createFeatureSelector<UserState>('users');

// Memoized selectors
export const selectAllUsers = createSelector(
  selectUserState,
  state => state.users
);

export const selectUsersLoading = createSelector(
  selectUserState,
  state => state.loading
);

export const selectUsersError = createSelector(
  selectUserState,
  state => state.error
);

export const selectUserById = (id: number) => createSelector(
  selectAllUsers,
  users => users.find(user => user.id === id)
);

export const selectActiveUsers = createSelector(
  selectAllUsers,
  users => users.filter(user => user.active)
);
```

### Effects

**Create Effects**
```typescript
import { Injectable } from '@angular/core';
import { Actions, createEffect, ofType } from '@ngrx/effects';
import { of } from 'rxjs';
import { map, mergeMap, catchError } from 'rxjs/operators';
import { UserService } from '../services/user.service';
import * as UserActions from './user.actions';

@Injectable()
export class UserEffects {
  loadUsers$ = createEffect(() =>
    this.actions$.pipe(
      ofType(UserActions.loadUsers),
      mergeMap(() =>
        this.userService.getUsers().pipe(
          map(users => UserActions.loadUsersSuccess({ users })),
          catchError(error => of(UserActions.loadUsersFailure({ error: error.message })))
        )
      )
    )
  );
  
  addUser$ = createEffect(() =>
    this.actions$.pipe(
      ofType(UserActions.addUser),
      mergeMap(({ user }) =>
        this.userService.createUser(user).pipe(
          map(user => UserActions.addUserSuccess({ user })),
          catchError(error => of(UserActions.loadUsersFailure({ error: error.message })))
        )
      )
    )
  );
  
  constructor(
    private actions$: Actions,
    private userService: UserService
  ) {}
}
```

**Register Effects**
```typescript
import { EffectsModule } from '@ngrx/effects';
import { UserEffects } from './store/user.effects';

@NgModule({
  imports: [
    EffectsModule.forFeature([UserEffects])
  ]
})
export class UsersModule {}
```

### Using NgRx in Components

**Dispatch Actions and Select State**
```typescript
import { Component, OnInit } from '@angular/core';
import { Store } from '@ngrx/store';
import { Observable } from 'rxjs';
import * as UserActions from './store/user.actions';
import * as UserSelectors from './store/user.selectors';
import { User } from './models/user.model';

@Component({
  selector: 'app-user-list',
  template: `
    <div *ngIf="loading$ | async">Loading...</div>
    <div *ngIf="error$ | async as error">{{ error }}</div>
    
    <div *ngFor="let user of users$ | async">
      {{ user.name }}
      <button (click)="deleteUser(user.id)">Delete</button>
    </div>
    
    <button (click)="addUser()">Add User</button>
  `
})
export class UserListComponent implements OnInit {
  users$: Observable<User[]>;
  loading$: Observable<boolean>;
  error$: Observable<string | null>;
  
  constructor(private store: Store) {}
  
  ngOnInit() {
    // Select state
    this.users$ = this.store.select(UserSelectors.selectAllUsers);
    this.loading$ = this.store.select(UserSelectors.selectUsersLoading);
    this.error$ = this.store.select(UserSelectors.selectUsersError);
    
    // Dispatch action
    this.store.dispatch(UserActions.loadUsers());
  }
  
  addUser() {
    const newUser: User = { id: 0, name: 'New User', email: 'new@example.com' };
    this.store.dispatch(UserActions.addUser({ user: newUser }));
  }
  
  deleteUser(id: number) {
    this.store.dispatch(UserActions.deleteUser({ id }));
  }
}
```

### NgRx Entity

**Entity Adapter**
```typescript
import { EntityState, EntityAdapter, createEntityAdapter } from '@ngrx/entity';
import { User } from '../models/user.model';

export interface UserState extends EntityState<User> {
  loading: boolean;
  error: string | null;
}

export const userAdapter: EntityAdapter<User> = createEntityAdapter<User>({
  selectId: (user: User) => user.id,
  sortComparer: (a: User, b: User) => a.name.localeCompare(b.name)
});

export const initialState: UserState = userAdapter.getInitialState({
  loading: false,
  error: null
});

export const userReducer = createReducer(
  initialState,
  
  on(UserActions.loadUsersSuccess, (state, { users }) =>
    userAdapter.setAll(users, { ...state, loading: false })
  ),
  
  on(UserActions.addUserSuccess, (state, { user }) =>
    userAdapter.addOne(user, state)
  ),
  
  on(UserActions.updateUser, (state, { user }) =>
    userAdapter.updateOne({ id: user.id, changes: user }, state)
  ),
  
  on(UserActions.deleteUser, (state, { id }) =>
    userAdapter.removeOne(id, state)
  )
);

// Entity selectors
const { selectAll, selectEntities, selectIds, selectTotal } = userAdapter.getSelectors();

export const selectAllUsers = selectAll;
export const selectUserEntities = selectEntities;
export const selectUserIds = selectIds;
export const selectUserTotal = selectTotal;
```
