---
name: vue-framework-advanced
description: "Master advanced Vue.js 3 development with Composition API, reactivity system, performance optimization, and modern tooling. Use for: building scalable Vue 3 applications, implementing composables and custom hooks, optimizing reactivity patterns, integrating TypeScript, state management with Pinia, SSR with Nuxt, advanced component patterns, performance tuning, and migrating from Vue 2 to Vue 3."
---

# Vue.js 3 Advanced Framework

Master advanced Vue.js 3 development with Composition API, reactivity system, and modern architectural patterns.

## Overview

Vue.js 3 represents a complete rewrite of the framework with a focus on performance, TypeScript support, and developer experience. This skill covers advanced patterns including the Composition API, reactive programming, composables, performance optimization, and integration with modern tooling. By 2026, Vue 3 with `<script setup>` syntax has become the industry standard, offering superior performance through compiler optimizations and Vapor Mode.

## When to Use Vue 3

| Scenario | Reason | Key Feature |
|----------|--------|-------------|
| Large-scale applications | Better code organization and reusability | Composition API with composables |
| TypeScript projects | Native TypeScript support with type inference | Written in TypeScript, excellent IDE support |
| Performance-critical apps | Faster rendering and smaller bundles | Proxy-based reactivity, tree-shaking, Vapor Mode |
| Real-time applications | Efficient reactive updates | Optimized reactivity system |
| Enterprise applications | Active maintenance and security patches | Vue 2 EOL in 2023, Vue 3 is the standard |
| SSR/SSG requirements | Built-in server-side rendering | Nuxt 4 integration |

## Composition API Fundamentals

### Core Reactive Primitives

**`ref` vs `reactive`**
- **`ref`**: For primitives (string, number, boolean). Access via `.value` property
- **`reactive`**: For objects and arrays. Returns deeply reactive proxy
- **Rule**: Use `ref` for primitives, `reactive` for complex objects
- **Caveat**: Destructuring `reactive` breaks reactivity—use `toRefs()` to preserve it

**Computed Properties**
```javascript
const total = computed(() => numbers.value.reduce((sum, n) => sum + n, 0))
```

**Watchers**
- `watch()`: Explicit dependency tracking
- `watchEffect()`: Automatic dependency tracking

### Lifecycle Hooks

Composition API equivalents:
- `onMounted()`, `onUnmounted()`, `onUpdated()`
- `onBeforeMount()`, `onBeforeUnmount()`, `onBeforeUpdate()`
- Access lifecycle programmatically within `setup()`

## Advanced Patterns

### Composables (Reusable Logic)

Composables are the Vue 3 equivalent of React hooks—functions that encapsulate and reuse stateful logic.

**Benefits over Mixins:**
- Clear source of properties
- No naming conflicts
- Better TypeScript support
- Easier to compose multiple concerns

**Example Use Cases:**
- Mouse position tracking
- API data fetching
- Form validation
- Authentication state
- WebSocket connections

See `/references/composables-patterns.md` for implementation examples.

### Dependency Injection

**`provide` / `inject`** pattern for passing data to deeply nested components without prop drilling.

**Advanced Use Cases:**
- Plugin-like architecture
- Service injection (Logger, API client)
- Theme/configuration context
- Testing with mocked dependencies

Use Symbols as injection keys to prevent collisions in large projects.

### Teleport and Suspense

**Teleport**: Render components anywhere in the DOM (modals, tooltips)
**Suspense**: Handle async component loading states declaratively

## Performance Optimization

### Compiler Optimizations

- **Static hoisting**: Static content compiled once
- **Patch flag optimization**: Targeted updates for dynamic content
- **Tree-shaking**: Include only used features
- **`<script setup>`**: Inline template compilation for better minification

### Vapor Mode (2026)

Vue 3's Vapor Mode compiles components into high-performance JavaScript that bypasses Virtual DOM overhead entirely, resulting in:
- Faster initial renders
- Reduced memory usage
- Smaller bundle sizes

### Reactivity Best Practices

- Use `shallowRef` and `shallowReactive` for large data structures
- Avoid unnecessary computed properties
- Use `markRaw()` for non-reactive data
- Leverage `readonly()` to prevent mutations

## TypeScript Integration

Vue 3 is written in TypeScript and provides excellent type inference:

- Use `defineComponent()` for type-safe components
- Type props with `PropType<T>`
- Type emits with `defineEmits<{ ... }>()`
- Use `Ref<T>` and `ComputedRef<T>` for type annotations

## State Management with Pinia

Pinia has replaced Vuex as the official state management solution:

**Advantages:**
- Simpler API (no mutations)
- Better TypeScript support
- Modular by design
- DevTools integration
- Composition API friendly

## Server-Side Rendering (Nuxt 4)

Nuxt 4 provides:
- File-based routing
- Auto-imports
- Server-side rendering
- Static site generation
- API routes
- Middleware

## Migration from Vue 2

**Key Breaking Changes:**
- Global API changes (`createApp` instead of `new Vue`)
- Filters removed (use computed or methods)
- `$on`, `$off`, `$once` removed (use mitt or provide/inject)
- Functional components syntax changed
- Async components require `defineAsyncComponent`

**Migration Strategy:**
- Use Vue 2.7 as intermediate step (Composition API backport)
- Migrate incrementally using compatibility build
- Update dependencies and tooling
- Refactor mixins to composables

## Tooling Ecosystem

**Build Tools:**
- **Vite 6+**: Lightning-fast dev server and build tool (recommended)
- **Vue CLI**: Legacy option, being phased out

**DevTools:**
- Vue DevTools for debugging
- State inspection
- Performance profiling
- Component tree visualization

**Testing:**
- Vitest for unit testing
- Cypress or Playwright for E2E
- Vue Test Utils for component testing

## Common Pitfalls

1. **Forgetting `.value`**: `ref` requires `.value` in `<script>`, not in `<template>`
2. **Destructuring reactive objects**: Breaks reactivity unless using `toRefs()`
3. **Mutating props**: Always emit events to parent instead
4. **Overusing watchers**: Prefer computed properties when possible
5. **Not using `<script setup>`**: Missing out on performance benefits

## AI-Enhanced Development

Vue 3's structured syntax is optimized for AI-assisted coding:
- Clear reactivity patterns (`ref`, `reactive`)
- Explicit imports and dependencies
- Type-safe with TypeScript
- Predictable component structure

## Using the Reference Files

### When to Read Each Reference

**`/references/composables-patterns.md`** — Read when implementing reusable logic, creating custom hooks, or refactoring mixins to composables.

**`/references/reactivity-deep-dive.md`** — Read when debugging reactivity issues, optimizing performance, or understanding the proxy-based reactivity system.

**`/references/performance-optimization.md`** — Read when optimizing bundle size, improving render performance, or implementing code-splitting strategies.

**`/references/typescript-integration.md`** — Read when setting up TypeScript in Vue 3, typing complex components, or creating type-safe composables.

## References

- [Composables Patterns](references/composables-patterns.md)
- [Performance Optimization](references/performance-optimization.md)
- [Reactivity Deep Dive](references/reactivity-deep-dive.md)
- [Typescript Integration](references/typescript-integration.md)
