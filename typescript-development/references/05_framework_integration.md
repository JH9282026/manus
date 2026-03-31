# TypeScript Framework Integration

## Overview

TypeScript has first-class support in major modern frameworks, providing enhanced developer experience, type safety, and better tooling. This guide covers integration with popular frameworks including React, Node.js/Express, Vue, and Angular.

## React with TypeScript

### Project Setup

```bash
# Create new React + TypeScript project
npx create-react-app my-app --template typescript

# Or with Vite (faster)
npm create vite@latest my-app -- --template react-ts
```

### Component Types

#### Function Components

```typescript
import React from 'react';

// Props interface
interface ButtonProps {
  label: string;
  onClick: () => void;
  disabled?: boolean;
  variant?: 'primary' | 'secondary';
}

// Function component with typed props
const Button: React.FC<ButtonProps> = ({ 
  label, 
  onClick, 
  disabled = false,
  variant = 'primary'
}) => {
  return (
    <button 
      onClick={onClick} 
      disabled={disabled}
      className={`btn btn-${variant}`}
    >
      {label}
    </button>
  );
};

export default Button;
```

#### With Children

```typescript
interface CardProps {
  title: string;
  children: React.ReactNode;
}

const Card: React.FC<CardProps> = ({ title, children }) => {
  return (
    <div className="card">
      <h2>{title}</h2>
      <div className="card-content">{children}</div>
    </div>
  );
};
```

### Hooks with TypeScript

#### useState

```typescript
import { useState } from 'react';

function Counter() {
  // Type inferred as number
  const [count, setCount] = useState(0);
  
  // Explicit type for complex state
  const [user, setUser] = useState<User | null>(null);
  
  // With initial value
  const [items, setItems] = useState<Item[]>([]);
  
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}
```

#### useEffect

```typescript
import { useEffect } from 'react';

function UserProfile({ userId }: { userId: string }) {
  const [user, setUser] = useState<User | null>(null);
  
  useEffect(() => {
    let cancelled = false;
    
    async function fetchUser() {
      try {
        const response = await fetch(`/api/users/${userId}`);
        const data = await response.json();
        
        if (!cancelled) {
          setUser(data);
        }
      } catch (error) {
        console.error('Failed to fetch user', error);
      }
    }
    
    fetchUser();
    
    return () => {
      cancelled = true;
    };
  }, [userId]);
  
  if (!user) return <div>Loading...</div>;
  
  return <div>{user.name}</div>;
}
```

#### useRef

```typescript
import { useRef, useEffect } from 'react';

function TextInput() {
  // Ref for DOM element
  const inputRef = useRef<HTMLInputElement>(null);
  
  // Ref for mutable value
  const renderCount = useRef(0);
  
  useEffect(() => {
    renderCount.current += 1;
    inputRef.current?.focus();
  });
  
  return <input ref={inputRef} type="text" />;
}
```

#### Custom Hooks

```typescript
import { useState, useEffect } from 'react';

interface UseFetchResult<T> {
  data: T | null;
  loading: boolean;
  error: Error | null;
}

function useFetch<T>(url: string): UseFetchResult<T> {
  const [data, setData] = useState<T | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<Error | null>(null);
  
  useEffect(() => {
    let cancelled = false;
    
    async function fetchData() {
      try {
        const response = await fetch(url);
        const json = await response.json();
        
        if (!cancelled) {
          setData(json);
          setLoading(false);
        }
      } catch (err) {
        if (!cancelled) {
          setError(err instanceof Error ? err : new Error('Unknown error'));
          setLoading(false);
        }
      }
    }
    
    fetchData();
    
    return () => {
      cancelled = true;
    };
  }, [url]);
  
  return { data, loading, error };
}

// Usage
function UserList() {
  const { data, loading, error } = useFetch<User[]>('/api/users');
  
  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;
  if (!data) return null;
  
  return (
    <ul>
      {data.map(user => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  );
}
```

### Event Handling

```typescript
import React, { ChangeEvent, FormEvent, MouseEvent } from 'react';

function Form() {
  const [value, setValue] = useState('');
  
  // Input change event
  const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
    setValue(e.target.value);
  };
  
  // Form submit event
  const handleSubmit = (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    console.log('Submitted:', value);
  };
  
  // Button click event
  const handleClick = (e: MouseEvent<HTMLButtonElement>) => {
    console.log('Button clicked');
  };
  
  return (
    <form onSubmit={handleSubmit}>
      <input type="text" value={value} onChange={handleChange} />
      <button type="submit" onClick={handleClick}>Submit</button>
    </form>
  );
}
```

### Context API

```typescript
import React, { createContext, useContext, useState, ReactNode } from 'react';

interface User {
  id: string;
  name: string;
  email: string;
}

interface AuthContextType {
  user: User | null;
  login: (user: User) => void;
  logout: () => void;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

interface AuthProviderProps {
  children: ReactNode;
}

export const AuthProvider: React.FC<AuthProviderProps> = ({ children }) => {
  const [user, setUser] = useState<User | null>(null);
  
  const login = (user: User) => {
    setUser(user);
  };
  
  const logout = () => {
    setUser(null);
  };
  
  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error('useAuth must be used within AuthProvider');
  }
  return context;
};

// Usage
function Profile() {
  const { user, logout } = useAuth();
  
  if (!user) return <div>Not logged in</div>;
  
  return (
    <div>
      <p>Welcome, {user.name}</p>
      <button onClick={logout}>Logout</button>
    </div>
  );
}
```

## Node.js/Express with TypeScript

### Project Setup

```bash
mkdir my-api && cd my-api
npm init -y
npm install express
npm install --save-dev typescript @types/node @types/express ts-node nodemon
npx tsc --init
```

### Basic Express Server

```typescript
import express, { Request, Response, NextFunction } from 'express';

const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());

// Basic route
app.get('/', (req: Request, res: Response) => {
  res.json({ message: 'Hello World' });
});

// Route with parameters
app.get('/users/:id', (req: Request, res: Response) => {
  const { id } = req.params;
  res.json({ userId: id });
});

// POST route with body
interface CreateUserBody {
  name: string;
  email: string;
}

app.post('/users', (req: Request<{}, {}, CreateUserBody>, res: Response) => {
  const { name, email } = req.body;
  res.json({ id: '1', name, email });
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

### Typed Request/Response

```typescript
import { Request, Response, NextFunction } from 'express';

// Custom request interface
interface AuthRequest extends Request {
  user?: {
    id: string;
    role: string;
  };
}

// Middleware
const authMiddleware = (
  req: AuthRequest, 
  res: Response, 
  next: NextFunction
) => {
  const token = req.headers.authorization;
  
  if (!token) {
    return res.status(401).json({ error: 'Unauthorized' });
  }
  
  // Verify token and attach user
  req.user = { id: '1', role: 'admin' };
  next();
};

// Protected route
app.get('/protected', authMiddleware, (req: AuthRequest, res: Response) => {
  res.json({ user: req.user });
});
```

### Error Handling

```typescript
class AppError extends Error {
  constructor(
    public message: string,
    public statusCode: number = 500
  ) {
    super(message);
  }
}

// Error handling middleware
const errorHandler = (
  err: Error,
  req: Request,
  res: Response,
  next: NextFunction
) => {
  if (err instanceof AppError) {
    return res.status(err.statusCode).json({
      error: err.message
    });
  }
  
  console.error(err);
  res.status(500).json({ error: 'Internal server error' });
};

app.use(errorHandler);
```

### Controller Pattern

```typescript
// user.controller.ts
import { Request, Response, NextFunction } from 'express';
import { UserService } from './user.service';

export class UserController {
  constructor(private userService: UserService) {}
  
  async getUsers(req: Request, res: Response, next: NextFunction) {
    try {
      const users = await this.userService.findAll();
      res.json(users);
    } catch (error) {
      next(error);
    }
  }
  
  async getUser(req: Request, res: Response, next: NextFunction) {
    try {
      const { id } = req.params;
      const user = await this.userService.findById(id);
      
      if (!user) {
        throw new AppError('User not found', 404);
      }
      
      res.json(user);
    } catch (error) {
      next(error);
    }
  }
  
  async createUser(req: Request, res: Response, next: NextFunction) {
    try {
      const user = await this.userService.create(req.body);
      res.status(201).json(user);
    } catch (error) {
      next(error);
    }
  }
}

// user.routes.ts
import { Router } from 'express';
import { UserController } from './user.controller';
import { UserService } from './user.service';

const router = Router();
const userService = new UserService();
const userController = new UserController(userService);

router.get('/users', (req, res, next) => 
  userController.getUsers(req, res, next)
);
router.get('/users/:id', (req, res, next) => 
  userController.getUser(req, res, next)
);
router.post('/users', (req, res, next) => 
  userController.createUser(req, res, next)
);

export default router;
```

## Vue with TypeScript

### Project Setup

```bash
npm create vue@latest my-app
# Select TypeScript option
```

### Component with Composition API

```typescript
<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';

interface User {
  id: number;
  name: string;
  email: string;
}

// Reactive state
const users = ref<User[]>([]);
const loading = ref(true);
const searchQuery = ref('');

// Computed property
const filteredUsers = computed(() => {
  return users.value.filter(user =>
    user.name.toLowerCase().includes(searchQuery.value.toLowerCase())
  );
});

// Methods
async function fetchUsers() {
  try {
    const response = await fetch('/api/users');
    users.value = await response.json();
  } catch (error) {
    console.error('Failed to fetch users', error);
  } finally {
    loading.value = false;
  }
}

// Lifecycle hook
onMounted(() => {
  fetchUsers();
});
</script>

<template>
  <div>
    <input v-model="searchQuery" placeholder="Search users..." />
    
    <div v-if="loading">Loading...</div>
    
    <ul v-else>
      <li v-for="user in filteredUsers" :key="user.id">
        {{ user.name }} - {{ user.email }}
      </li>
    </ul>
  </div>
</template>
```

### Props and Emits

```typescript
<script setup lang="ts">
interface Props {
  title: string;
  count?: number;
  items: string[];
}

interface Emits {
  (e: 'update', value: number): void;
  (e: 'delete', id: string): void;
}

const props = withDefaults(defineProps<Props>(), {
  count: 0
});

const emit = defineEmits<Emits>();

function handleUpdate() {
  emit('update', props.count + 1);
}

function handleDelete(id: string) {
  emit('delete', id);
}
</script>
```

## Angular with TypeScript

Angular is built with TypeScript by default.

### Component

```typescript
import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';

interface User {
  id: string;
  name: string;
  email: string;
}

@Component({
  selector: 'app-user-list',
  templateUrl: './user-list.component.html',
  styleUrls: ['./user-list.component.css']
})
export class UserListComponent implements OnInit {
  @Input() users: User[] = [];
  @Output() userSelected = new EventEmitter<User>();
  
  selectedUser: User | null = null;
  
  ngOnInit(): void {
    console.log('Component initialized');
  }
  
  selectUser(user: User): void {
    this.selectedUser = user;
    this.userSelected.emit(user);
  }
}
```

### Service

```typescript
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

interface User {
  id: string;
  name: string;
  email: string;
}

@Injectable({
  providedIn: 'root'
})
export class UserService {
  private apiUrl = '/api/users';
  
  constructor(private http: HttpClient) {}
  
  getUsers(): Observable<User[]> {
    return this.http.get<User[]>(this.apiUrl);
  }
  
  getUser(id: string): Observable<User> {
    return this.http.get<User>(`${this.apiUrl}/${id}`);
  }
  
  createUser(user: Omit<User, 'id'>): Observable<User> {
    return this.http.post<User>(this.apiUrl, user);
  }
}
```

## Best Practices

### 1. Strict Type Checking

Always enable strict mode in all frameworks:

```json
{
  "compilerOptions": {
    "strict": true,
    "noImplicitAny": true,
    "strictNullChecks": true
  }
}
```

### 2. Proper Type Definitions

Install type definitions for all libraries:

```bash
npm install --save-dev @types/react @types/node @types/express
```

### 3. Avoid Type Assertions

Use type guards instead of assertions:

```typescript
// Bad
const user = data as User;

// Good
function isUser(data: unknown): data is User {
  return (
    typeof data === 'object' &&
    data !== null &&
    'id' in data &&
    'name' in data
  );
}

if (isUser(data)) {
  // data is User here
}
```

### 4. Use Generics for Reusable Components

```typescript
interface ListProps<T> {
  items: T[];
  renderItem: (item: T) => React.ReactNode;
}

function List<T>({ items, renderItem }: ListProps<T>) {
  return (
    <ul>
      {items.map((item, index) => (
        <li key={index}>{renderItem(item)}</li>
      ))}
    </ul>
  );
}
```

### 5. Environment Variables

```typescript
// env.d.ts
interface ImportMetaEnv {
  readonly VITE_API_URL: string;
  readonly VITE_API_KEY: string;
}

interface ImportMeta {
  readonly env: ImportMetaEnv;
}

// Usage
const apiUrl = import.meta.env.VITE_API_URL;
```

## Conclusion

TypeScript integration with modern frameworks provides significant benefits in terms of type safety, developer experience, and code maintainability. By following framework-specific patterns and best practices, you can build robust, scalable applications with confidence. The key is to leverage TypeScript's type system fully while respecting each framework's conventions and idioms.
