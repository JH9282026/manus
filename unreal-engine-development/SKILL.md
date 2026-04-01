---
name: unreal-engine-development
description: "Develop high-fidelity games using Unreal Engine 5 with C++, Blueprints visual scripting, and cutting-edge rendering technologies. Use for: creating AAA-quality 3D games for PC/console/mobile, implementing photorealistic graphics with Nanite and Lumen, building virtual production environments, designing levels with World Partition, creating interactive experiences with Blueprint visual scripting, programming gameplay systems in C++, optimizing performance with Temporal Super Resolution, developing VR/AR applications, and deploying to PlayStation, Xbox, Nintendo Switch, Windows, macOS, Linux, iOS, and Android platforms."
---

# Unreal Engine Development

Develop cutting-edge games and interactive experiences using Unreal Engine 5's advanced rendering and development tools.

## Overview

Unreal Engine 5 is Epic Games' flagship game engine, renowned for photorealistic graphics, robust tooling, and AAA production capabilities. This skill covers UE5's revolutionary features (Nanite, Lumen, World Partition), Blueprint visual scripting, C++ programming, level design workflows, animation systems, and multi-platform deployment. Unreal Engine powers everything from indie games to blockbuster titles like Fortnite and The Matrix Awakens.

## Development Environment Setup

### Installation and Project Creation

| Component | Purpose | Source |
|-----------|---------|--------|
| Epic Games Launcher | Engine installer and project manager | epicgames.com |
| Unreal Engine 5.x | Core engine (LTS or latest) | Via Launcher |
| Visual Studio 2022 | C++ IDE (Windows) | Community Edition (free) |
| Xcode | C++ IDE (macOS) | Mac App Store |
| Rider for Unreal | Alternative C++ IDE | JetBrains (paid) |

### Project Templates

| Template | Use Case | Starting Content |
|----------|----------|------------------|
| Blank | Custom projects from scratch | Minimal |
| First Person | FPS games | Character, weapons, sample level |
| Third Person | Action/adventure games | Character, camera, animations |
| Top Down | Strategy, RPG games | Camera, character, click-to-move |
| Vehicle | Racing, driving games | Vehicle physics, sample track |
| VR | Virtual reality experiences | VR-specific setup |

### Project Structure

```
MyProject/
├── Content/          # Game assets (meshes, textures, blueprints)
├── Source/           # C++ source code
├── Config/           # Configuration files
├── Plugins/          # Third-party and custom plugins
├── Saved/            # Autosaves, logs, screenshots
└── Intermediate/     # Build artifacts (excluded from version control)
```

## Core Unreal Concepts

### Actor-Component Architecture

Unreal uses Actors (objects in the world) with Components (functionality modules):

- **Actor**: Base class for all placeable objects
- **Pawn**: Actor that can be possessed by a Controller
- **Character**: Pawn with built-in movement and animation
- **Controller**: Possesses Pawns to control them (PlayerController, AIController)
- **Components**: Modular functionality (MeshComponent, CameraComponent, etc.)

### Blueprint Visual Scripting

Node-based programming system for designers and artists:

**Advantages:**
- No coding required
- Rapid prototyping
- Visual debugging
- Designer-friendly
- Real-time iteration

**Blueprint Types:**

| Type | Purpose | Example |
|------|---------|----------|
| Level Blueprint | Level-specific logic | Door triggers, cutscenes |
| Blueprint Class | Reusable actors | Pickups, enemies, weapons |
| Blueprint Interface | Communication between blueprints | Damage system, interaction |
| Blueprint Macro Library | Reusable node groups | Common calculations |
| Blueprint Function Library | Static utility functions | Math helpers, conversions |

### C++ Programming

For performance-critical systems and complex logic:

**When to Use C++:**
- Performance-intensive calculations
- Low-level engine access
- Custom engine modifications
- Large-scale systems
- Multiplayer authoritative logic

**When to Use Blueprints:**
- Rapid prototyping
- Designer-driven content
- UI logic
- Simple gameplay mechanics
- Level scripting

**Hybrid Approach (Recommended):**
C++ for core systems, Blueprints for content and iteration.

## Unreal Engine 5 Revolutionary Features

### Nanite Virtualized Geometry

**What It Is:**
Streaming and rendering technology for massive geometric detail without traditional polygon budgets.

**Benefits:**
- Import film-quality assets directly (millions of polygons)
- No need for LODs (Level of Detail)
- Automatic detail management
- Consistent visual quality at any distance

**Use Cases:**
- Photorealistic environments
- Highly detailed characters and props
- Architectural visualization
- Open-world games

**Limitations:**
- No support for skeletal meshes (characters)
- No support for World Position Offset (vertex animation)
- Requires modern GPUs

### Lumen Global Illumination

**What It Is:**
Fully dynamic global illumination and reflections system.

**Benefits:**
- Real-time lighting updates (no baking required)
- Accurate indirect lighting
- Dynamic reflections
- Artist-friendly workflow

**Use Cases:**
- Dynamic time-of-day systems
- Destructible environments
- Interactive lighting (flashlights, explosions)
- Rapid iteration

**Performance Modes:**
- **Hardware Ray Tracing:** Highest quality, requires RTX GPUs
- **Software Ray Tracing:** Good quality, broader hardware support
- **Surface Cache:** Fastest, suitable for lower-end hardware

### Temporal Super Resolution (TSR)

**What It Is:**
Upsampling technology that renders at lower resolution while maintaining high visual fidelity.

**Benefits:**
- Render at 1080p, display at 4K
- Significant performance gains (30-50% FPS increase)
- Better quality than traditional upscaling
- No external dependencies (built-in)

**Comparison:**
- Better than TAA (Temporal Anti-Aliasing)
- Comparable to DLSS (NVIDIA) but platform-agnostic
- Works on all GPUs

### World Partition

**What It Is:**
Automatic level streaming system for massive open worlds.

**Benefits:**
- Automatically divides world into grid cells
- Streams only visible/nearby cells
- Supports worlds of unlimited size
- Collaborative editing (multiple users editing same world)

**Use Cases:**
- Open-world games
- Large-scale environments
- MMOs
- Architectural walkthroughs

## Level Design and Environment Art

### Landscape System

Create massive terrains with sculpting and painting tools:

- **Sculpting:** Raise, lower, smooth, flatten terrain
- **Painting:** Apply materials, foliage, detail textures
- **Layers:** Blend multiple materials based on slope, height
- **Splines:** Roads, rivers, paths that conform to terrain

### Modeling Tools

Built-in mesh editing without external software:

| Tool | Purpose |
|------|----------|
| Modeling Mode | Edit meshes directly in editor |
| Boolean Operations | Combine, subtract, intersect meshes |
| UV Editing | Create and adjust texture coordinates |
| Baking | Generate normal maps, ambient occlusion |
| Geometry Scripting | Procedural mesh generation |

### Foliage System

Efficiently place and render vegetation:

- **Foliage Painting:** Brush-based placement
- **Procedural Foliage:** Automatic distribution with rules
- **Instanced Rendering:** Thousands of instances with minimal overhead
- **LOD and Culling:** Automatic optimization

## Animation and Character Systems

### Animation Blueprint

State machine-based animation system:

**Components:**
1. **State Machines:** Manage animation states (idle, walk, run, jump)
2. **Blend Spaces:** Blend animations based on parameters (speed, direction)
3. **Animation Montages:** Play one-shot animations (attacks, emotes)
4. **Animation Notifies:** Trigger events at specific frames (footsteps, effects)
5. **IK (Inverse Kinematics):** Procedural limb adjustment (foot placement)

### Control Rig

Procedural rigging and animation system:

- Runtime character rigging
- Procedural animation
- Facial animation
- Full-body IK

### MetaHuman Creator

Create photorealistic digital humans:

- Cloud-based character creator
- Thousands of customization options
- Realistic skin, hair, eyes
- Ready for Unreal Engine
- Free to use

## Materials and Shaders

### Material Editor

Node-based material creation:

**Common Nodes:**
- **Texture Sample:** Read texture data
- **Lerp:** Blend between values
- **Multiply/Add:** Math operations
- **Fresnel:** Edge highlighting
- **Normal Map:** Surface detail

### Physically Based Rendering (PBR)

Realistic material workflow:

**Material Inputs:**
- **Base Color:** Diffuse color
- **Metallic:** 0 = non-metal, 1 = metal
- **Roughness:** 0 = smooth/shiny, 1 = rough/matte
- **Normal:** Surface detail
- **Emissive:** Self-illumination

### Material Instances

Parameter-driven material variations:

- Create master material with parameters
- Derive instances with different values
- Real-time parameter changes
- Efficient (no shader recompilation)

## Gameplay Framework

### Game Mode and Game State

**Game Mode (Server-only):**
- Defines game rules
- Spawns players
- Handles win/loss conditions
- Manages game flow

**Game State (Replicated):**
- Stores game-wide state
- Score, time remaining, match phase
- Accessible to all clients

### Player Controller and Player State

**Player Controller:**
- Handles player input
- Possesses Pawns
- Client-server communication

**Player State:**
- Stores player-specific data
- Score, name, team
- Replicated to all clients

### Pawn and Character

**Pawn:**
- Can be possessed by Controller
- Receives input
- Basic movement

**Character:**
- Extends Pawn
- Built-in CharacterMovementComponent
- Capsule collision
- Animation support

## Multiplayer and Networking

### Replication

Automatic synchronization between server and clients:

**Replicated Variables:**
```cpp
UPROPERTY(Replicated)
int32 Health;

UPROPERTY(ReplicatedUsing=OnRep_Score)
int32 Score;

void OnRep_Score()
{
    // Called when Score changes on client
}
```

**Remote Procedure Calls (RPCs):**
- **Server RPC:** Client calls, server executes
- **Client RPC:** Server calls, clients execute
- **Multicast RPC:** Server calls, all clients execute

### Network Optimization

- **Relevancy:** Only replicate actors near players
- **Update Frequency:** Control replication rate
- **Compression:** Reduce bandwidth usage
- **Prediction:** Client-side prediction for responsiveness

## Performance Optimization

### Profiling Tools

| Tool | Purpose |
|------|----------|
| Stat FPS | Frame rate display |
| Stat Unit | CPU/GPU/Frame time |
| Stat SceneRendering | Rendering statistics |
| GPU Visualizer | Detailed GPU profiling |
| Unreal Insights | Comprehensive profiling suite |

### Optimization Techniques

**Rendering:**
- Use Nanite for static meshes
- Enable TSR for upsampling
- Implement LODs for non-Nanite meshes
- Cull distant objects
- Optimize draw calls

**Lighting:**
- Use Lumen for dynamic lighting
- Bake lighting for static scenes (if not using Lumen)
- Limit shadow-casting lights
- Use lightmaps for static objects

**Physics:**
- Simplify collision meshes
- Use simple colliders (box, sphere, capsule)
- Disable physics on distant objects
- Limit physics simulation frequency

## Build and Deployment

### Platform Support

| Platform | Requirements |
|----------|-------------|
| Windows | DirectX 11/12, Vulkan |
| macOS | Metal API |
| Linux | Vulkan |
| PlayStation 4/5 | Platform SDK, dev kit |
| Xbox One/Series X|S | GDK, dev kit |
| Nintendo Switch | Nintendo SDK, dev kit |
| iOS | Xcode, Apple Developer account |
| Android | Android SDK |

### Packaging

1. **Project Settings:** Configure platform-specific settings
2. **Cook Content:** Process assets for target platform
3. **Package:** Create distributable build
4. **Test:** Verify on target hardware

### Distribution

- **Steam:** PC distribution
- **Epic Games Store:** PC distribution (reduced fees for UE games)
- **Console Stores:** PlayStation Store, Xbox Store, Nintendo eShop
- **Mobile Stores:** App Store, Google Play

## Using the Reference Files

### When to Read Each Reference

**`/references/unreal-blueprint-guide.md`** — Read when creating gameplay logic with visual scripting, implementing game mechanics without code, or learning Blueprint best practices and common patterns.

**`/references/unreal-cpp-programming.md`** — Read when writing C++ gameplay code, creating custom engine features, optimizing performance-critical systems, or integrating third-party libraries.

**`/references/unreal-rendering-features.md`** — Read when configuring Nanite and Lumen, creating materials and shaders, optimizing graphics performance, or implementing advanced rendering techniques.

**`/references/unreal-multiplayer-networking.md`** — Read when implementing multiplayer functionality, setting up dedicated servers, optimizing network performance, or debugging replication issues.

**`/references/unreal-optimization-deployment.md`** — Read when profiling performance bottlenecks, preparing builds for specific platforms, optimizing for console/mobile, or troubleshooting deployment issues.
