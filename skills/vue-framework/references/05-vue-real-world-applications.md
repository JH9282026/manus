# Vue Real-World Applications and Advanced Patterns

## Full-Stack Application Architecture

### Project Structure for Large Applications

```
vue-app/
├── public/
│   ├── favicon.ico
│   └── index.html
├── src/
│   ├── api/                    # API client and services
│   │   ├── client.ts          # Axios/Fetch configuration
│   │   ├── interceptors.ts    # Request/response interceptors
│   │   └── services/
│   │       ├── auth.service.ts
│   │       ├── user.service.ts
│   │       └── product.service.ts
│   ├── assets/                 # Static assets
│   │   ├── images/
│   │   ├── fonts/
│   │   └── styles/
│   │       ├── main.scss
│   │       ├── variables.scss
│   │       └── mixins.scss
│   ├── components/             # Reusable components
│   │   ├── base/              # Base UI components
│   │   ├── common/            # Shared components
│   │   ├── features/          # Feature-specific components
│   │   └── layouts/           # Layout components
│   ├── composables/            # Composition functions
│   │   ├── useAuth.ts
│   │   ├── useApi.ts
│   │   ├── useForm.ts
│   │   └── usePagination.ts
│   ├── config/                 # Configuration files
│   │   ├── constants.ts
│   │   └── env.ts
│   ├── directives/             # Custom directives
│   │   ├── click-outside.ts
│   │   └── tooltip.ts
│   ├── guards/                 # Route guards
│   │   ├── auth.guard.ts
│   │   └── role.guard.ts
│   ├── layouts/                # Page layouts
│   │   ├── DefaultLayout.vue
│   │   ├── AuthLayout.vue
│   │   └── DashboardLayout.vue
│   ├── middleware/             # Middleware functions
│   ├── plugins/                # Vue plugins
│   │   ├── i18n.ts
│   │   └── analytics.ts
│   ├── router/                 # Router configuration
│   │   ├── index.ts
│   │   └── routes/
│   │       ├── auth.routes.ts
│   │       ├── dashboard.routes.ts
│   │       └── public.routes.ts
│   ├── stores/                 # Pinia stores
│   │   ├── auth.store.ts
│   │   ├── user.store.ts
│   │   └── app.store.ts
│   ├── types/                  # TypeScript types
│   │   ├── api.types.ts
│   │   ├── models.types.ts
│   │   └── store.types.ts
│   ├── utils/                  # Utility functions
│   │   ├── validators.ts
│   │   ├── formatters.ts
│   │   └── helpers.ts
│   ├── views/                  # Page components
│   │   ├── auth/
│   │   ├── dashboard/
│   │   └── public/
│   ├── App.vue
│   └── main.ts
├── tests/
│   ├── unit/
│   ├── integration/
│   └── e2e/
├── .env.development
├── .env.production
├── vite.config.ts
├── tsconfig.json
└── package.json
```

### API Client Setup

```typescript
// api/client.ts
import axios, { AxiosInstance, AxiosRequestConfig, AxiosResponse } from 'axios'
import { useAuthStore } from '@/stores/auth.store'

class ApiClient {
  private client: AxiosInstance

  constructor() {
    this.client = axios.create({
      baseURL: import.meta.env.VITE_API_URL,
      timeout: 10000,
      headers: {
        'Content-Type': 'application/json'
      }
    })

    this.setupInterceptors()
  }

  private setupInterceptors() {
    // Request interceptor
    this.client.interceptors.request.use(
      (config) => {
        const authStore = useAuthStore()
        if (authStore.token) {
          config.headers.Authorization = `Bearer ${authStore.token}`
        }
        return config
      },
      (error) => Promise.reject(error)
    )

    // Response interceptor
    this.client.interceptors.response.use(
      (response) => response,
      async (error) => {
        const originalRequest = error.config

        // Handle 401 Unauthorized
        if (error.response?.status === 401 && !originalRequest._retry) {
          originalRequest._retry = true
          
          try {
            const authStore = useAuthStore()
            await authStore.refreshToken()
            return this.client(originalRequest)
          } catch (refreshError) {
            const authStore = useAuthStore()
            authStore.logout()
            return Promise.reject(refreshError)
          }
        }

        return Promise.reject(error)
      }
    )
  }

  async get<T>(url: string, config?: AxiosRequestConfig): Promise<T> {
    const response = await this.client.get<T>(url, config)
    return response.data
  }

  async post<T>(url: string, data?: any, config?: AxiosRequestConfig): Promise<T> {
    const response = await this.client.post<T>(url, data, config)
    return response.data
  }

  async put<T>(url: string, data?: any, config?: AxiosRequestConfig): Promise<T> {
    const response = await this.client.put<T>(url, data, config)
    return response.data
  }

  async delete<T>(url: string, config?: AxiosRequestConfig): Promise<T> {
    const response = await this.client.delete<T>(url, config)
    return response.data
  }
}

export const apiClient = new ApiClient()
```

```typescript
// api/services/user.service.ts
import { apiClient } from '../client'
import type { User, UpdateUserDto, PaginatedResponse } from '@/types'

export class UserService {
  static async getUsers(page = 1, limit = 10): Promise<PaginatedResponse<User>> {
    return apiClient.get(`/users?page=${page}&limit=${limit}`)
  }

  static async getUser(id: number): Promise<User> {
    return apiClient.get(`/users/${id}`)
  }

  static async createUser(data: Partial<User>): Promise<User> {
    return apiClient.post('/users', data)
  }

  static async updateUser(id: number, data: UpdateUserDto): Promise<User> {
    return apiClient.put(`/users/${id}`, data)
  }

  static async deleteUser(id: number): Promise<void> {
    return apiClient.delete(`/users/${id}`)
  }
}
```

### Authentication System

```typescript
// stores/auth.store.ts
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { apiClient } from '@/api/client'
import type { User, LoginCredentials, RegisterData } from '@/types'

export const useAuthStore = defineStore('auth', () => {
  // State
  const user = ref<User | null>(null)
  const token = ref<string | null>(localStorage.getItem('token'))
  const refreshToken = ref<string | null>(localStorage.getItem('refreshToken'))
  const loading = ref(false)
  const error = ref<string | null>(null)

  // Getters
  const isAuthenticated = computed(() => !!token.value)
  const userRole = computed(() => user.value?.role || 'guest')
  const userName = computed(() => user.value?.name || 'Guest')

  // Actions
  async function login(credentials: LoginCredentials) {
    loading.value = true
    error.value = null

    try {
      const response = await apiClient.post<{
        user: User
        token: string
        refreshToken: string
      }>('/auth/login', credentials)

      user.value = response.user
      token.value = response.token
      refreshToken.value = response.refreshToken

      localStorage.setItem('token', response.token)
      localStorage.setItem('refreshToken', response.refreshToken)

      return response.user
    } catch (e: any) {
      error.value = e.response?.data?.message || 'Login failed'
      throw e
    } finally {
      loading.value = false
    }
  }

  async function register(data: RegisterData) {
    loading.value = true
    error.value = null

    try {
      const response = await apiClient.post<{
        user: User
        token: string
        refreshToken: string
      }>('/auth/register', data)

      user.value = response.user
      token.value = response.token
      refreshToken.value = response.refreshToken

      localStorage.setItem('token', response.token)
      localStorage.setItem('refreshToken', response.refreshToken)

      return response.user
    } catch (e: any) {
      error.value = e.response?.data?.message || 'Registration failed'
      throw e
    } finally {
      loading.value = false
    }
  }

  async function logout() {
    try {
      await apiClient.post('/auth/logout')
    } finally {
      user.value = null
      token.value = null
      refreshToken.value = null
      localStorage.removeItem('token')
      localStorage.removeItem('refreshToken')
    }
  }

  async function fetchUser() {
    if (!token.value) return

    loading.value = true
    try {
      user.value = await apiClient.get<User>('/auth/me')
    } catch (e) {
      // Token might be invalid
      await logout()
    } finally {
      loading.value = false
    }
  }

  async function refreshAuthToken() {
    if (!refreshToken.value) {
      throw new Error('No refresh token available')
    }

    const response = await apiClient.post<{
      token: string
      refreshToken: string
    }>('/auth/refresh', {
      refreshToken: refreshToken.value
    })

    token.value = response.token
    refreshToken.value = response.refreshToken

    localStorage.setItem('token', response.token)
    localStorage.setItem('refreshToken', response.refreshToken)
  }

  return {
    user,
    token,
    loading,
    error,
    isAuthenticated,
    userRole,
    userName,
    login,
    register,
    logout,
    fetchUser,
    refreshToken: refreshAuthToken
  }
})
```

### Route Guards

```typescript
// guards/auth.guard.ts
import type { NavigationGuardNext, RouteLocationNormalized } from 'vue-router'
import { useAuthStore } from '@/stores/auth.store'

export async function authGuard(
  to: RouteLocationNormalized,
  from: RouteLocationNormalized,
  next: NavigationGuardNext
) {
  const authStore = useAuthStore()

  // Check if route requires authentication
  if (to.meta.requiresAuth) {
    if (!authStore.isAuthenticated) {
      // Redirect to login
      next({
        name: 'Login',
        query: { redirect: to.fullPath }
      })
      return
    }

    // Fetch user if not loaded
    if (!authStore.user) {
      try {
        await authStore.fetchUser()
      } catch (error) {
        next({ name: 'Login' })
        return
      }
    }

    // Check role-based access
    if (to.meta.roles) {
      const roles = to.meta.roles as string[]
      if (!roles.includes(authStore.userRole)) {
        next({ name: 'Unauthorized' })
        return
      }
    }
  }

  // Redirect authenticated users away from auth pages
  if (to.meta.guestOnly && authStore.isAuthenticated) {
    next({ name: 'Dashboard' })
    return
  }

  next()
}
```

```typescript
// router/index.ts
import { createRouter, createWebHistory } from 'vue-router'
import { authGuard } from '@/guards/auth.guard'
import type { RouteRecordRaw } from 'vue-router'

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/views/Home.vue')
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('@/views/auth/Login.vue'),
    meta: { guestOnly: true }
  },
  {
    path: '/dashboard',
    component: () => import('@/layouts/DashboardLayout.vue'),
    meta: { requiresAuth: true },
    children: [
      {
        path: '',
        name: 'Dashboard',
        component: () => import('@/views/dashboard/Overview.vue')
      },
      {
        path: 'profile',
        name: 'Profile',
        component: () => import('@/views/dashboard/Profile.vue')
      },
      {
        path: 'admin',
        name: 'Admin',
        component: () => import('@/views/dashboard/Admin.vue'),
        meta: { roles: ['admin'] }
      }
    ]
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach(authGuard)

export default router
```

### Form Handling with Validation

```typescript
// composables/useForm.ts
import { ref, reactive, computed } from 'vue'
import type { Ref } from 'vue'

type ValidationRule<T = any> = {
  validator: (value: T) => boolean
  message: string
}

type FieldRules = {
  [key: string]: ValidationRule[]
}

export function useForm<T extends Record<string, any>>(
  initialValues: T,
  rules: FieldRules = {}
) {
  const values = reactive<T>({ ...initialValues })
  const errors = reactive<Record<string, string>>({})
  const touched = reactive<Record<string, boolean>>({})
  const submitting = ref(false)

  const isValid = computed(() => {
    return Object.keys(errors).length === 0
  })

  function validateField(field: keyof T): boolean {
    const fieldRules = rules[field as string]
    if (!fieldRules) return true

    for (const rule of fieldRules) {
      if (!rule.validator(values[field])) {
        errors[field as string] = rule.message
        return false
      }
    }

    delete errors[field as string]
    return true
  }

  function validateAll(): boolean {
    let valid = true
    for (const field in rules) {
      if (!validateField(field as keyof T)) {
        valid = false
      }
    }
    return valid
  }

  function handleBlur(field: keyof T) {
    touched[field as string] = true
    validateField(field)
  }

  function handleChange(field: keyof T, value: any) {
    values[field] = value
    if (touched[field as string]) {
      validateField(field)
    }
  }

  async function handleSubmit(
    onSubmit: (values: T) => Promise<void> | void
  ): Promise<boolean> {
    // Mark all fields as touched
    for (const field in values) {
      touched[field] = true
    }

    if (!validateAll()) {
      return false
    }

    submitting.value = true
    try {
      await onSubmit(values)
      return true
    } catch (error) {
      return false
    } finally {
      submitting.value = false
    }
  }

  function reset() {
    Object.assign(values, initialValues)
    Object.keys(errors).forEach(key => delete errors[key])
    Object.keys(touched).forEach(key => delete touched[key])
  }

  return {
    values,
    errors,
    touched,
    submitting,
    isValid,
    validateField,
    validateAll,
    handleBlur,
    handleChange,
    handleSubmit,
    reset
  }
}
```

```vue
<!-- components/LoginForm.vue -->
<script setup lang="ts">
import { useForm } from '@/composables/useForm'
import { useAuthStore } from '@/stores/auth.store'
import { useRouter } from 'vue-router'

const authStore = useAuthStore()
const router = useRouter()

const { values, errors, touched, submitting, handleBlur, handleChange, handleSubmit } = useForm(
  {
    email: '',
    password: ''
  },
  {
    email: [
      {
        validator: (value) => !!value,
        message: 'Email is required'
      },
      {
        validator: (value) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value),
        message: 'Invalid email format'
      }
    ],
    password: [
      {
        validator: (value) => !!value,
        message: 'Password is required'
      },
      {
        validator: (value) => value.length >= 8,
        message: 'Password must be at least 8 characters'
      }
    ]
  }
)

async function onSubmit() {
  const success = await handleSubmit(async (formValues) => {
    await authStore.login(formValues)
    router.push('/dashboard')
  })
}
</script>

<template>
  <form @submit.prevent="onSubmit" class="login-form">
    <div class="form-group">
      <label for="email">Email</label>
      <input
        id="email"
        type="email"
        :value="values.email"
        @input="handleChange('email', ($event.target as HTMLInputElement).value)"
        @blur="handleBlur('email')"
        :class="{ error: touched.email && errors.email }"
      />
      <span v-if="touched.email && errors.email" class="error-message">
        {{ errors.email }}
      </span>
    </div>

    <div class="form-group">
      <label for="password">Password</label>
      <input
        id="password"
        type="password"
        :value="values.password"
        @input="handleChange('password', ($event.target as HTMLInputElement).value)"
        @blur="handleBlur('password')"
        :class="{ error: touched.password && errors.password }"
      />
      <span v-if="touched.password && errors.password" class="error-message">
        {{ errors.password }}
      </span>
    </div>

    <button type="submit" :disabled="submitting">
      {{ submitting ? 'Logging in...' : 'Login' }}
    </button>

    <div v-if="authStore.error" class="error-message">
      {{ authStore.error }}
    </div>
  </form>
</template>

<style scoped>
.login-form {
  max-width: 400px;
  margin: 0 auto;
}

.form-group {
  margin-bottom: 1rem;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 500;
}

input {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ddd;
  border-radius: 4px;
}

input.error {
  border-color: #f44336;
}

.error-message {
  color: #f44336;
  font-size: 0.875rem;
  margin-top: 0.25rem;
  display: block;
}

button {
  width: 100%;
  padding: 0.75rem;
  background: #1976d2;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
}

button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}
</style>
```

### Data Table with Pagination and Sorting

```vue
<script setup lang="ts">
import { ref, computed, watch } from 'vue'
import { UserService } from '@/api/services/user.service'
import type { User, PaginatedResponse } from '@/types'

const users = ref<User[]>([])
const loading = ref(false)
const error = ref<string | null>(null)

const currentPage = ref(1)
const pageSize = ref(10)
const totalItems = ref(0)
const sortBy = ref<keyof User>('id')
const sortOrder = ref<'asc' | 'desc'>('asc')
const searchQuery = ref('')

const totalPages = computed(() => Math.ceil(totalItems.value / pageSize.value))

const sortedAndFilteredUsers = computed(() => {
  let result = [...users.value]

  // Filter
  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase()
    result = result.filter(
      (user) =>
        user.name.toLowerCase().includes(query) ||
        user.email.toLowerCase().includes(query)
    )
  }

  // Sort
  result.sort((a, b) => {
    const aVal = a[sortBy.value]
    const bVal = b[sortBy.value]

    if (aVal < bVal) return sortOrder.value === 'asc' ? -1 : 1
    if (aVal > bVal) return sortOrder.value === 'asc' ? 1 : -1
    return 0
  })

  return result
})

async function fetchUsers() {
  loading.value = true
  error.value = null

  try {
    const response = await UserService.getUsers(currentPage.value, pageSize.value)
    users.value = response.data
    totalItems.value = response.total
  } catch (e: any) {
    error.value = e.message
  } finally {
    loading.value = false
  }
}

function handleSort(column: keyof User) {
  if (sortBy.value === column) {
    sortOrder.value = sortOrder.value === 'asc' ? 'desc' : 'asc'
  } else {
    sortBy.value = column
    sortOrder.value = 'asc'
  }
}

function goToPage(page: number) {
  if (page >= 1 && page <= totalPages.value) {
    currentPage.value = page
  }
}

watch([currentPage, pageSize], fetchUsers, { immediate: true })
</script>

<template>
  <div class="data-table">
    <div class="table-header">
      <input
        v-model="searchQuery"
        type="text"
        placeholder="Search users..."
        class="search-input"
      />
    </div>

    <div v-if="loading" class="loading">Loading...</div>
    <div v-else-if="error" class="error">{{ error }}</div>
    <div v-else>
      <table>
        <thead>
          <tr>
            <th @click="handleSort('id')">
              ID
              <span v-if="sortBy === 'id'">{{ sortOrder === 'asc' ? '↑' : '↓' }}</span>
            </th>
            <th @click="handleSort('name')">
              Name
              <span v-if="sortBy === 'name'">{{ sortOrder === 'asc' ? '↑' : '↓' }}</span>
            </th>
            <th @click="handleSort('email')">
              Email
              <span v-if="sortBy === 'email'">{{ sortOrder === 'asc' ? '↑' : '↓' }}</span>
            </th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="user in sortedAndFilteredUsers" :key="user.id">
            <td>{{ user.id }}</td>
            <td>{{ user.name }}</td>
            <td>{{ user.email }}</td>
            <td>
              <button @click="$emit('edit', user)">Edit</button>
              <button @click="$emit('delete', user.id)">Delete</button>
            </td>
          </tr>
        </tbody>
      </table>

      <div class="pagination">
        <button @click="goToPage(currentPage - 1)" :disabled="currentPage === 1">
          Previous
        </button>
        <span>Page {{ currentPage }} of {{ totalPages }}</span>
        <button @click="goToPage(currentPage + 1)" :disabled="currentPage === totalPages">
          Next
        </button>
      </div>
    </div>
  </div>
</template>
```

## Conclusion

Building real-world Vue applications requires understanding of:

1. **Architecture**: Proper project structure and organization
2. **API Integration**: Robust API client with interceptors and error handling
3. **Authentication**: Secure auth system with token refresh
4. **Routing**: Protected routes with guards and role-based access
5. **Forms**: Comprehensive form handling with validation
6. **Data Management**: Efficient data fetching, caching, and state management
7. **Type Safety**: TypeScript integration for better developer experience

These patterns and practices form the foundation for scalable, maintainable Vue applications.
