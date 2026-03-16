# TypeScript Integration

Comprehensive guide to using TypeScript with Vue 3 for type-safe development.

---

## Why TypeScript with Vue 3?

Vue 3 is written in TypeScript and provides first-class TypeScript support:

- **Better IDE support**: IntelliSense, autocomplete, refactoring
- **Catch errors early**: Type checking at compile time
- **Self-documenting code**: Types serve as inline documentation
- **Safer refactoring**: Compiler catches breaking changes
- **Composition API friendly**: Natural type inference

---

## Project Setup

### Create TypeScript Vue Project

```bash
npm create vue@latest my-app
# Select TypeScript: Yes

cd my-app
npm install
```

### Manual Setup

```bash
npm install -D typescript @vue/tsconfig
npx tsc --init
```

**tsconfig.json:**
```json
{
  "extends": "@vue/tsconfig/tsconfig.dom.json",
  "compilerOptions": {
    "target": "ES2020",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "strict": true,
    "jsx": "preserve",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "esModuleInterop": true,
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "skipLibCheck": true,
    "types": ["vite/client"]
  },
  "include": ["src/**/*.ts", "src/**/*.tsx", "src/**/*.vue"],
  "exclude": ["node_modules"]
}
```

---

## Component Type Annotations

### Basic Component with `<script setup lang="ts">`

```vue
<script setup lang="ts">
import { ref, computed } from 'vue'

const count = ref<number>(0)
const doubled = computed<number>(() => count.value * 2)

function increment(): void {
  count.value++
}
</script>
```

### Typing Props

**Runtime Declaration:**
```vue
<script setup lang="ts">
interface Props {
  title: string
  count?: number
  tags: string[]
  user: {
    id: number
    name: string
  }
}

const props = withDefaults(defineProps<Props>(), {
  count: 0
})
</script>
```

**Alternative with PropType:**
```vue
<script setup lang="ts">
import type { PropType } from 'vue'

interface User {
  id: number
  name: string
}

const props = defineProps({
  user: {
    type: Object as PropType<User>,
    required: true
  },
  tags: {
    type: Array as PropType<string[]>,
    default: () => []
  }
})
</script>
```

### Typing Emits

```vue
<script setup lang="ts">
interface Emits {
  (e: 'update', value: string): void
  (e: 'delete', id: number): void
  (e: 'submit', payload: { name: string; email: string }): void
}

const emit = defineEmits<Emits>()

function handleUpdate() {
  emit('update', 'new value')
}
</script>
```

### Typing Refs

```vue
<script setup lang="ts">
import { ref, type Ref } from 'vue'

interface User {
  id: number
  name: string
}

const user: Ref<User | null> = ref(null)
const count = ref<number>(0) // Type inference works
const name = ref('John') // Inferred as Ref<string>
</script>
```

### Typing Template Refs

```vue
<script setup lang="ts">
import { ref, onMounted } from 'vue'
import type { ComponentPublicInstance } from 'vue'
import ChildComponent from './ChildComponent.vue'

const inputRef = ref<HTMLInputElement | null>(null)
const childRef = ref<ComponentPublicInstance<typeof ChildComponent> | null>(null)

onMounted(() => {
  inputRef.value?.focus()
  childRef.value?.someMethod()
})
</script>

<template>
  <input ref="inputRef" />
  <ChildComponent ref="childRef" />
</template>
```

---

## Composables with TypeScript

### Basic Typed Composable

```typescript
import { ref, type Ref } from 'vue'

interface UseFetchReturn<T> {
  data: Ref<T | null>
  error: Ref<Error | null>
  loading: Ref<boolean>
  refetch: () => Promise<void>
}

export function useFetch<T>(url: string): UseFetchReturn<T> {
  const data = ref<T | null>(null)
  const error = ref<Error | null>(null)
  const loading = ref(false)

  const fetchData = async () => {
    loading.value = true
    error.value = null

    try {
      const response = await fetch(url)
      data.value = await response.json()
    } catch (e) {
      error.value = e as Error
    } finally {
      loading.value = false
    }
  }

  fetchData()

  return { data, error, loading, refetch: fetchData }
}
```

**Usage:**
```vue
<script setup lang="ts">
import { useFetch } from './composables/useFetch'

interface User {
  id: number
  name: string
  email: string
}

const { data, error, loading } = useFetch<User>('/api/user')
</script>
```

### Generic Composable

```typescript
import { ref, type Ref } from 'vue'

export function useLocalStorage<T>(
  key: string,
  defaultValue: T
): Ref<T> {
  const storedValue = localStorage.getItem(key)
  const data = ref<T>(
    storedValue ? JSON.parse(storedValue) : defaultValue
  ) as Ref<T>

  watch(data, (newValue) => {
    localStorage.setItem(key, JSON.stringify(newValue))
  }, { deep: true })

  return data
}
```

---

## Store Typing (Pinia)

### Typed Store

```typescript
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

interface User {
  id: number
  name: string
  email: string
}

export const useUserStore = defineStore('user', () => {
  const user = ref<User | null>(null)
  const isLoggedIn = computed(() => user.value !== null)

  async function login(email: string, password: string): Promise<void> {
    const response = await fetch('/api/login', {
      method: 'POST',
      body: JSON.stringify({ email, password })
    })
    user.value = await response.json()
  }

  function logout(): void {
    user.value = null
  }

  return { user, isLoggedIn, login, logout }
})
```

**Usage with Type Safety:**
```vue
<script setup lang="ts">
import { storeToRefs } from 'pinia'
import { useUserStore } from '@/stores/user'

const store = useUserStore()
const { user, isLoggedIn } = storeToRefs(store)

// TypeScript knows user is User | null
const userName = user.value?.name
</script>
```

---

## Router Typing

### Typed Routes

```typescript
import { createRouter, createWebHistory, type RouteRecordRaw } from 'vue-router'

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    name: 'home',
    component: () => import('./views/Home.vue')
  },
  {
    path: '/user/:id',
    name: 'user',
    component: () => import('./views/User.vue'),
    props: true
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
```

### Typed Route Params

```vue
<script setup lang="ts">
import { useRoute } from 'vue-router'

const route = useRoute()

// Type assertion for params
const userId = route.params.id as string

// Or with validation
const userIdNumber = Number(route.params.id)
if (isNaN(userIdNumber)) {
  // Handle invalid ID
}
</script>
```

---

## Advanced Types

### Component Instance Type

```typescript
import type { ComponentPublicInstance } from 'vue'
import MyComponent from './MyComponent.vue'

type MyComponentInstance = ComponentPublicInstance<typeof MyComponent>
```

### Slot Types

```vue
<script setup lang="ts">
interface Slots {
  default(props: { item: string; index: number }): any
  header(): any
}

defineSlots<Slots>()
</script>

<template>
  <div>
    <slot name="header" />
    <slot :item="item" :index="i" />
  </div>
</template>
```

### Provide/Inject Types

```typescript
// types.ts
import type { InjectionKey, Ref } from 'vue'

export interface User {
  id: number
  name: string
}

export const UserKey: InjectionKey<Ref<User>> = Symbol('user')
```

**Provider:**
```vue
<script setup lang="ts">
import { ref, provide } from 'vue'
import { UserKey, type User } from './types'

const user = ref<User>({ id: 1, name: 'John' })
provide(UserKey, user)
</script>
```

**Consumer:**
```vue
<script setup lang="ts">
import { inject } from 'vue'
import { UserKey } from './types'

const user = inject(UserKey)
// TypeScript knows user is Ref<User> | undefined
</script>
```

---

## Utility Types

### Extract Component Props Type

```typescript
import type { ComponentProps } from 'vue-component-type-helpers'
import MyComponent from './MyComponent.vue'

type MyComponentProps = ComponentProps<typeof MyComponent>
```

### Extract Emits Type

```typescript
import type { ComponentEmits } from 'vue-component-type-helpers'
import MyComponent from './MyComponent.vue'

type MyComponentEmits = ComponentEmits<typeof MyComponent>
```

---

## Common Patterns

### Form Handling

```vue
<script setup lang="ts">
import { reactive } from 'vue'

interface FormData {
  name: string
  email: string
  age: number
}

interface FormErrors {
  name?: string
  email?: string
  age?: string
}

const form = reactive<FormData>({
  name: '',
  email: '',
  age: 0
})

const errors = reactive<FormErrors>({})

function validate(): boolean {
  errors.name = form.name ? undefined : 'Name is required'
  errors.email = form.email.includes('@') ? undefined : 'Invalid email'
  errors.age = form.age > 0 ? undefined : 'Age must be positive'
  
  return !errors.name && !errors.email && !errors.age
}

async function submit(): Promise<void> {
  if (!validate()) return
  
  await fetch('/api/submit', {
    method: 'POST',
    body: JSON.stringify(form)
  })
}
</script>
```

### API Response Typing

```typescript
interface ApiResponse<T> {
  data: T
  status: number
  message: string
}

interface User {
  id: number
  name: string
}

async function fetchUser(id: number): Promise<User> {
  const response = await fetch(`/api/users/${id}`)
  const json: ApiResponse<User> = await response.json()
  return json.data
}
```

---

## Troubleshooting

### "Cannot find module" for .vue files

Create `env.d.ts`:
```typescript
/// <reference types="vite/client" />

declare module '*.vue' {
  import type { DefineComponent } from 'vue'
  const component: DefineComponent<{}, {}, any>
  export default component
}
```

### Type errors with third-party libraries

Install type definitions:
```bash
npm install -D @types/library-name
```

Or create manual declarations:
```typescript
// types/library-name.d.ts
declare module 'library-name' {
  export function someFunction(): void
}
```

---

## Best Practices

1. **Enable strict mode** in `tsconfig.json`
2. **Use type inference** when possible (avoid redundant annotations)
3. **Define interfaces** for complex data structures
4. **Use generics** for reusable composables
5. **Type all props and emits** explicitly
6. **Avoid `any`** — use `unknown` if type is truly unknown
7. **Use `InjectionKey`** for provide/inject
8. **Create shared types** in a `types/` directory
