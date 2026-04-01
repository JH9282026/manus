---
name: unity-game-development
description: "Develop cross-platform games using Unity engine with C# scripting, component-based architecture, and modern rendering pipelines. Use for: creating 2D/3D games for mobile/desktop/console/VR/AR platforms, implementing game mechanics with Unity's physics and animation systems, optimizing performance across devices, integrating Unity Asset Store packages, building multiplayer games with Netcode, designing UI with UI Toolkit, creating shaders with Shader Graph, and deploying games to 20+ platforms including iOS, Android, PlayStation, Xbox, Nintendo Switch, and WebGL."
---

# Unity Game Development

Develop cross-platform games using Unity's comprehensive game engine with C# scripting and visual tools.

## Overview

Unity is a production-ready game engine supporting 2D, 3D, VR, and AR development across 20+ platforms. This skill covers Unity's component-based architecture, C# scripting fundamentals, rendering pipelines (URP/HDRP), physics systems, animation workflows, performance optimization, and deployment strategies. Unity combines visual editing with code-driven logic, making it suitable for indie developers through AAA studios.

## Development Environment Setup

### Unity Hub and Editor Installation

| Component | Purpose | Recommendation |
|-----------|---------|----------------|
| Unity Hub | Version manager and project launcher | Install latest stable version |
| Unity Editor | Core development environment | LTS (Long Term Support) version for production |
| Visual Studio / Rider | C# IDE with Unity integration | VS Community (free) or JetBrains Rider |
| Version Control | Git integration for collaboration | Unity Version Control or GitHub Desktop |

### Project Structure Best Practices

```
Assets/
├── Scripts/          # C# game logic
├── Scenes/           # Game levels
├── Prefabs/          # Reusable GameObjects
├── Materials/        # Shaders and materials
├── Audio/            # Sound effects and music
├── Resources/        # Runtime-loaded assets
└── StreamingAssets/  # Platform-specific files
```

## Core Unity Concepts

### Component-Based Architecture

Unity uses GameObjects with attached Components rather than inheritance hierarchies. Every game element is a GameObject with Components defining behavior:

- **Transform**: Position, rotation, scale
- **Renderer**: Visual representation (MeshRenderer, SpriteRenderer)
- **Collider**: Physics collision detection
- **Rigidbody**: Physics simulation
- **Custom Scripts**: Game-specific logic

### Unity Lifecycle Methods

Key C# methods called by Unity engine:

| Method | When Called | Use For |
|--------|-------------|----------|
| `Awake()` | Object initialization, before Start | Setting up references |
| `Start()` | First frame before Update | Initialization requiring other objects |
| `Update()` | Every frame | Input handling, non-physics logic |
| `FixedUpdate()` | Fixed time intervals | Physics calculations |
| `LateUpdate()` | After all Updates | Camera following, final adjustments |
| `OnDestroy()` | Object destruction | Cleanup, unsubscribing events |

## Rendering Pipelines

### Pipeline Selection Guide

| Pipeline | Best For | Performance | Features |
|----------|----------|-------------|----------|
| Built-in | Legacy projects, simple games | Moderate | Basic lighting, older shader model |
| URP (Universal) | Mobile, 2D, cross-platform | High | Optimized, Shader Graph, 2D Lights |
| HDRP (High Definition) | High-end PC/console, photorealism | Demanding | Ray tracing, volumetrics, advanced materials |

Choose URP for most new projects unless targeting high-end graphics on powerful hardware.

## Physics and Collision

### Physics Components

- **Rigidbody**: Enables physics simulation (gravity, forces, velocity)
- **Collider**: Defines collision boundaries (Box, Sphere, Capsule, Mesh)
- **Physics Materials**: Control friction and bounciness
- **Joints**: Connect Rigidbodies (Hinge, Spring, Fixed)

### Collision Detection Strategies

| Method | Trigger | Use Case |
|--------|---------|----------|
| `OnCollisionEnter()` | Physical collision | Damage, impacts, bouncing |
| `OnTriggerEnter()` | Overlap detection | Pickups, zones, checkpoints |
| Raycasting | Line-of-sight checks | Shooting, AI vision, ground detection |

## Animation Systems

### Animator Controller

State machine-based animation system:

1. **Animation Clips**: Individual animations (walk, jump, attack)
2. **States**: Nodes representing animation clips
3. **Transitions**: Conditions for switching between states
4. **Parameters**: Variables controlling transitions (bool, float, int, trigger)
5. **Blend Trees**: Smooth blending between multiple animations

### Animation Techniques

- **Keyframe Animation**: Artist-created animation clips
- **Procedural Animation**: Code-driven movement (IK, physics-based)
- **Root Motion**: Animation drives character movement
- **Animation Events**: Trigger code at specific animation frames

## Scripting Best Practices

### Performance Optimization

- Cache component references in `Awake()` instead of repeated `GetComponent()` calls
- Use object pooling for frequently instantiated/destroyed objects
- Minimize `Update()` logic; use events or coroutines when possible
- Avoid `Find()` methods in runtime; assign references in Inspector
- Use `CompareTag()` instead of string comparison

### Design Patterns for Unity

| Pattern | Purpose | Unity Application |
|---------|---------|-------------------|
| Singleton | Single instance access | GameManager, AudioManager |
| Observer | Event-driven communication | UnityEvents, C# events |
| Object Pool | Reuse objects | Bullets, particles, enemies |
| State Machine | Manage complex behaviors | AI, player states |
| Command | Undo/redo, input buffering | Action systems, replays |

### ScriptableObjects for Data

Use ScriptableObjects for game data instead of static classes:

- Weapon stats, enemy configurations
- Game settings, difficulty levels
- Inventory items, quest data
- Shared data between scenes

## Mobile Development

### Platform-Specific Optimization

| Optimization | Mobile Impact | Implementation |
|--------------|---------------|----------------|
| Texture compression | Reduce memory | ASTC (Android), PVRTC (iOS) |
| Draw call batching | Improve FPS | Static/dynamic batching, SRP Batcher |
| LOD (Level of Detail) | Reduce polygons | LOD Groups for distant objects |
| Occlusion culling | Skip hidden objects | Bake occlusion data |
| Lightmap baking | Avoid realtime lights | Bake static lighting |

### Touch Input Handling

```csharp
// Multi-touch support
if (Input.touchCount > 0) {
    Touch touch = Input.GetTouch(0);
    if (touch.phase == TouchPhase.Began) {
        // Handle touch start
    }
}
```

## Multiplayer and Networking

### Netcode for GameObjects

Unity's official multiplayer solution:

- **NetworkManager**: Handles connections and spawning
- **NetworkObject**: Makes GameObjects network-aware
- **NetworkVariable**: Synchronized variables across clients
- **RPC (Remote Procedure Calls)**: Execute methods on remote machines
- **Client-Server Architecture**: Authoritative server model

## Testing and Debugging

### Unity Profiler

Analyze performance bottlenecks:

- **CPU Usage**: Identify expensive scripts and methods
- **Rendering**: Draw calls, batches, triangles
- **Memory**: Allocation patterns, garbage collection
- **Physics**: Collision detection overhead
- **Audio**: Sound processing load

### Debug Techniques

- `Debug.Log()` for console output
- `Debug.DrawRay()` for visualizing raycasts
- Gizmos for editor visualization
- Unity Test Framework for unit/integration tests
- Play Mode testing in Editor

## Build and Deployment

### Platform Build Settings

| Platform | Requirements | Considerations |
|----------|--------------|----------------|
| Windows/Mac/Linux | Standalone build | Executable size, graphics API |
| iOS | Mac with Xcode, Apple Developer account | App Store guidelines, TestFlight |
| Android | Android SDK, keystore | Google Play, APK/AAB format |
| WebGL | Browser compatibility | File size, streaming assets |
| Console | Platform SDK, dev kit | Certification requirements |

### Build Optimization

- Enable code stripping to reduce build size
- Use AssetBundles for downloadable content
- Implement addressable assets for efficient loading
- Configure compression settings per platform
- Test on target devices early and often

## Unity Ecosystem

### Asset Store Integration

Leverage pre-built assets and tools:

- **3D Models and Animations**: Characters, environments, props
- **Audio**: Music, sound effects, audio tools
- **Editor Extensions**: Productivity tools, workflow enhancers
- **Code Libraries**: Networking, AI, procedural generation
- **Complete Projects**: Learning resources, starter templates

Evaluate quality, performance impact, and licensing before integration.

### Unity Services

- **Unity Analytics**: Player behavior tracking
- **Unity Ads**: Monetization through advertising
- **Unity IAP**: In-app purchase integration
- **Unity Cloud Build**: Automated build pipeline
- **Unity Collaborate**: Version control for small teams

## Learning Progression

### Beginner Path (Weeks 1-4)

1. Complete Unity Essentials Pathway (official learning)
2. Build Roll-a-Ball tutorial
3. Explore Microgames for end-to-end experience
4. Learn C# fundamentals for Unity

### Intermediate Path (Weeks 5-12)

1. Choose specialization (programming, art, or environment design)
2. Complete Junior Programmer Pathway
3. Build 2-3 small complete games
4. Study design patterns and architecture

### Advanced Topics

- DOTS (Data-Oriented Technology Stack) for performance
- Custom shader development with Shader Graph/HLSL
- Advanced multiplayer with dedicated servers
- VR/AR development with XR Interaction Toolkit
- Procedural generation and AI systems

## Using the Reference Files

### When to Read Each Reference

**`/references/unity-scripting-guide.md`** — Read when implementing game logic, working with C# in Unity, or needing code examples for common patterns like player movement, camera control, or inventory systems.

**`/references/unity-rendering-optimization.md`** — Read when experiencing performance issues, optimizing for mobile platforms, or configuring URP/HDRP pipelines for specific visual quality targets.

**`/references/unity-physics-animation.md`** — Read when implementing character controllers, ragdoll physics, complex animation state machines, or procedural animation systems.

**`/references/unity-deployment-guide.md`** — Read when preparing builds for specific platforms, configuring platform-specific settings, or troubleshooting build errors and deployment issues.

**`/references/unity-advanced-topics.md`** — Read when exploring DOTS, custom shaders, advanced multiplayer architectures, or integrating third-party SDKs and services.

## References

- [Unity Advanced Topics](references/unity-advanced-topics.md)
- [Unity Deployment Guide](references/unity-deployment-guide.md)
- [Unity Physics Animation](references/unity-physics-animation.md)
- [Unity Rendering Optimization](references/unity-rendering-optimization.md)
- [Unity Scripting Guide](references/unity-scripting-guide.md)
