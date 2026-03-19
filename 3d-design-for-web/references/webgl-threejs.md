# WebGL and Three.js Reference

## WebGL Fundamentals

### What is WebGL?

WebGL (Web Graphics Library) is a JavaScript API that enables rendering interactive 2D and 3D graphics within compatible web browsers without the need for plugins. It leverages the GPU (Graphics Processing Unit) to perform thousands of parallel calculations, making it possible to render complex scenes at high frame rates.

WebGL is based on OpenGL ES 2.0 and provides a low-level interface to the graphics hardware. While powerful, WebGL requires significant boilerplate code and understanding of graphics programming concepts, which is why libraries like Three.js have become essential for practical web development.

### The Graphics Pipeline

WebGL operates through a graphics pipeline that processes 3D data into 2D pixels on the screen:

1. **Vertex Processing**
   - Transforms 3D vertex positions using model, view, and projection matrices
   - Calculates vertex attributes (colors, normals, texture coordinates)
   - Outputs clip-space coordinates

2. **Primitive Assembly**
   - Groups vertices into geometric primitives (triangles, lines, points)
   - Performs clipping against the view frustum

3. **Rasterization**
   - Converts geometric primitives into fragments (potential pixels)
   - Interpolates vertex attributes across the primitive surface

4. **Fragment Processing**
   - Calculates final color for each fragment
   - Applies textures, lighting, and other effects
   - Determines fragment depth

5. **Output Merging**
   - Performs depth testing (z-buffer)
   - Blends fragments with existing framebuffer content
   - Writes final pixel colors

### Shaders: The Heart of WebGL

Shaders are programs that run on the GPU, written in GLSL (OpenGL Shading Language). There are two main types:

**Vertex Shader:**
```glsl
attribute vec3 position;
attribute vec2 uv;

uniform mat4 modelViewMatrix;
uniform mat4 projectionMatrix;

varying vec2 vUv;

void main() {
  vUv = uv;
  gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
}
```

The vertex shader processes each vertex, transforming positions from object space to clip space and passing data to the fragment shader through varying variables.

**Fragment Shader:**
```glsl
precision mediump float;

uniform sampler2D texture;
uniform vec3 lightDirection;

varying vec2 vUv;

void main() {
  vec4 texColor = texture2D(texture, vUv);
  gl_FragColor = texColor;
}
```

The fragment shader determines the final color of each pixel, applying textures, lighting calculations, and other effects.

### WebGL Coordinate Systems

WebGL uses a right-handed coordinate system with specific conventions:

- **Clip Space**: Normalized device coordinates ranging from -1 to 1 in all three axes
- **NDC (Normalized Device Coordinates)**: After perspective division
- **Screen Space**: Final pixel coordinates

Transformations flow through multiple coordinate spaces:
1. **Object/Local Space** → Model Matrix → **World Space**
2. **World Space** → View Matrix → **Camera/View Space**
3. **Camera Space** → Projection Matrix → **Clip Space**
4. **Clip Space** → Perspective Division → **NDC**
5. **NDC** → Viewport Transform → **Screen Space**

## Three.js Architecture

### Core Components

**Scene Graph:**
Three.js uses a hierarchical scene graph where objects can be nested, and transformations propagate down the hierarchy.

```javascript
const scene = new THREE.Scene();
const group = new THREE.Group();

const mesh1 = new THREE.Mesh(geometry, material);
const mesh2 = new THREE.Mesh(geometry, material);

group.add(mesh1);
group.add(mesh2);
scene.add(group);

// Transforming the group affects all children
group.rotation.y = Math.PI / 4;
```

**Cameras:**
Three.js provides multiple camera types:

```javascript
// Perspective Camera (realistic 3D)
const perspectiveCamera = new THREE.PerspectiveCamera(
  75,                                    // Field of view (degrees)
  window.innerWidth / window.innerHeight, // Aspect ratio
  0.1,                                   // Near clipping plane
  1000                                   // Far clipping plane
);

// Orthographic Camera (no perspective distortion)
const orthographicCamera = new THREE.OrthographicCamera(
  -10, 10,  // Left, right
  10, -10,  // Top, bottom
  0.1, 100  // Near, far
);
```

**Renderers:**
The renderer draws the scene from the camera's perspective:

```javascript
const renderer = new THREE.WebGLRenderer({
  canvas: document.querySelector('#canvas'),
  antialias: true,        // Smooth edges
  alpha: true,            // Transparent background
  powerPreference: 'high-performance',
  precision: 'highp',     // Shader precision
  logarithmicDepthBuffer: true // Better depth precision
});

renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.0;
renderer.outputColorSpace = THREE.SRGBColorSpace;
```

### Geometries

Three.js provides built-in geometries and supports custom buffer geometries:

**Built-in Geometries:**
```javascript
const box = new THREE.BoxGeometry(1, 1, 1);
const sphere = new THREE.SphereGeometry(1, 32, 32);
const plane = new THREE.PlaneGeometry(10, 10, 10, 10);
const cylinder = new THREE.CylinderGeometry(1, 1, 2, 32);
const torus = new THREE.TorusGeometry(1, 0.4, 16, 100);
```

**Custom Buffer Geometry:**
```javascript
const geometry = new THREE.BufferGeometry();

// Vertices (x, y, z for each point)
const vertices = new Float32Array([
  -1, -1, 0,
   1, -1, 0,
   0,  1, 0
]);

// Normals (for lighting calculations)
const normals = new Float32Array([
  0, 0, 1,
  0, 0, 1,
  0, 0, 1
]);

// UV coordinates (for texture mapping)
const uvs = new Float32Array([
  0, 0,
  1, 0,
  0.5, 1
]);

geometry.setAttribute('position', new THREE.BufferAttribute(vertices, 3));
geometry.setAttribute('normal', new THREE.BufferAttribute(normals, 3));
geometry.setAttribute('uv', new THREE.BufferAttribute(uvs, 2));

// Optional: indices for shared vertices
const indices = new Uint16Array([0, 1, 2]);
geometry.setIndex(new THREE.BufferAttribute(indices, 1));
```

### Materials

Three.js offers a variety of materials with different rendering characteristics:

**MeshBasicMaterial** (unlit, flat color):
```javascript
const material = new THREE.MeshBasicMaterial({
  color: 0xff0000,
  wireframe: false,
  transparent: true,
  opacity: 0.8
});
```

**MeshStandardMaterial** (PBR - Physically Based Rendering):
```javascript
const material = new THREE.MeshStandardMaterial({
  color: 0xffffff,
  metalness: 0.5,      // 0 = dielectric, 1 = metal
  roughness: 0.5,      // 0 = smooth, 1 = rough
  map: colorTexture,   // Diffuse/albedo map
  normalMap: normalTexture,
  roughnessMap: roughnessTexture,
  metalnessMap: metalnessTexture,
  aoMap: aoTexture,    // Ambient occlusion
  envMap: environmentTexture
});
```

**MeshPhysicalMaterial** (Advanced PBR):
```javascript
const material = new THREE.MeshPhysicalMaterial({
  color: 0xffffff,
  metalness: 0,
  roughness: 0.1,
  transmission: 1,     // Glass-like transparency
  thickness: 0.5,      // Refraction thickness
  clearcoat: 1,        // Clear coat layer
  clearcoatRoughness: 0.1,
  ior: 1.5            // Index of refraction
});
```

**ShaderMaterial** (Custom shaders):
```javascript
const material = new THREE.ShaderMaterial({
  uniforms: {
    time: { value: 0 },
    resolution: { value: new THREE.Vector2() },
    texture1: { value: texture }
  },
  vertexShader: vertexShaderCode,
  fragmentShader: fragmentShaderCode,
  transparent: true,
  side: THREE.DoubleSide
});
```

### Lighting

Three.js supports various light types:

**Ambient Light** (uniform illumination):
```javascript
const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
scene.add(ambientLight);
```

**Directional Light** (sun-like, parallel rays):
```javascript
const directionalLight = new THREE.DirectionalLight(0xffffff, 1);
directionalLight.position.set(5, 10, 5);
directionalLight.castShadow = true;

// Shadow configuration
directionalLight.shadow.mapSize.width = 2048;
directionalLight.shadow.mapSize.height = 2048;
directionalLight.shadow.camera.near = 0.5;
directionalLight.shadow.camera.far = 50;
directionalLight.shadow.camera.left = -10;
directionalLight.shadow.camera.right = 10;
directionalLight.shadow.camera.top = 10;
directionalLight.shadow.camera.bottom = -10;

scene.add(directionalLight);
```

**Point Light** (omnidirectional, like a light bulb):
```javascript
const pointLight = new THREE.PointLight(0xff0000, 1, 100);
pointLight.position.set(0, 5, 0);
pointLight.castShadow = true;
scene.add(pointLight);
```

**Spot Light** (cone-shaped beam):
```javascript
const spotLight = new THREE.SpotLight(0xffffff, 1);
spotLight.position.set(10, 10, 10);
spotLight.angle = Math.PI / 6;
spotLight.penumbra = 0.1;
spotLight.decay = 2;
spotLight.distance = 100;
spotLight.castShadow = true;
scene.add(spotLight);
```

**Hemisphere Light** (sky and ground colors):
```javascript
const hemisphereLight = new THREE.HemisphereLight(
  0x87ceeb, // Sky color
  0x8b4513, // Ground color
  0.6       // Intensity
);
scene.add(hemisphereLight);
```

### Textures

**Loading Textures:**
```javascript
const textureLoader = new THREE.TextureLoader();
const texture = textureLoader.load(
  '/textures/diffuse.jpg',
  (texture) => {
    console.log('Texture loaded');
  },
  (progress) => {
    console.log(`Loading: ${(progress.loaded / progress.total * 100).toFixed(2)}%`);
  },
  (error) => {
    console.error('Error loading texture:', error);
  }
);

// Texture configuration
texture.wrapS = THREE.RepeatWrapping;
texture.wrapT = THREE.RepeatWrapping;
texture.repeat.set(2, 2);
texture.minFilter = THREE.LinearMipmapLinearFilter;
texture.magFilter = THREE.LinearFilter;
texture.anisotropy = renderer.capabilities.getMaxAnisotropy();
texture.colorSpace = THREE.SRGBColorSpace;
```

**Cube Textures (Environment Maps):**
```javascript
const cubeTextureLoader = new THREE.CubeTextureLoader();
const environmentMap = cubeTextureLoader.load([
  '/textures/px.jpg', // Positive X
  '/textures/nx.jpg', // Negative X
  '/textures/py.jpg', // Positive Y
  '/textures/ny.jpg', // Negative Y
  '/textures/pz.jpg', // Positive Z
  '/textures/nz.jpg'  // Negative Z
]);

scene.environment = environmentMap;
scene.background = environmentMap;
```

## WebGPU and Three.js

### WebGPU Overview

WebGPU is the next-generation graphics API for the web, offering:
- **Better Performance**: 2-10x faster for compute-intensive tasks
- **Compute Shaders**: GPU-accelerated general computation
- **Modern Architecture**: Designed for contemporary GPU hardware
- **Lower Overhead**: More efficient command submission

### Browser Support (2026)

- **Chrome/Edge**: v113+ (stable)
- **Firefox**: v141+ (Windows), v145+ (macOS)
- **Safari**: v26+ (macOS, iOS, iPadOS, visionOS)

### Migration from WebGL to WebGPU

**Basic Migration:**
```javascript
// WebGL (old)
import * as THREE from 'three';
const renderer = new THREE.WebGLRenderer();

// WebGPU (new)
import * as THREE from 'three/webgpu';
const renderer = new THREE.WebGPURenderer();
await renderer.init(); // Required async initialization
```

**When to Migrate:**
- New projects without legacy constraints
- Applications with 50,000+ particles
- High draw call scenarios (100+ per frame)
- Need for compute shaders (physics, simulations)
- Complex shader pipelines

**When to Stay with WebGL:**
- Legacy browser support required
- Simple scenes running smoothly
- No new features planned
- Smaller bundle size needed (WebGL-only builds)

### Three Shader Language (TSL)

TSL is a node-based material system that compiles to both WGSL (WebGPU) and GLSL (WebGL):

```javascript
import { 
  MeshStandardNodeMaterial, 
  uniform, 
  texture, 
  vec3, 
  mix,
  positionLocal,
  normalLocal
} from 'three/nodes';

const material = new MeshStandardNodeMaterial();

// Node-based material definition
material.colorNode = texture(colorTexture);
material.roughnessNode = uniform(0.5);
material.metalnessNode = uniform(0.2);

// Custom position modification
material.positionNode = positionLocal.add(
  normalLocal.mul(uniform(0.1))
);
```

**Compute Shaders with TSL:**
```javascript
import { Fn, storage, instanceIndex, vec3 } from 'three/nodes';

const computeParticles = Fn(() => {
  const positions = storage(positionBuffer, 'vec3', count);
  const velocities = storage(velocityBuffer, 'vec3', count);
  
  const index = instanceIndex;
  const pos = positions.element(index);
  const vel = velocities.element(index);
  
  // Physics update
  vel.addAssign(vec3(0, -0.01, 0)); // Gravity
  pos.addAssign(vel);
  
  // Boundary check
  if (pos.y.lessThan(0)) {
    pos.y = 0;
    vel.y = vel.y.mul(-0.8); // Bounce with damping
  }
})();

// Execute compute shader
renderer.compute(computeParticles);
```

### Performance Comparison

**WebGPU Advantages:**
- **Particle Systems**: 2-5x faster for 50,000+ particles
- **Instanced Rendering**: More efficient buffer management
- **Compute Shaders**: Enable GPU physics and simulations
- **Complex Shaders**: Better pipeline optimization

**WebGL Advantages:**
- **Broader Support**: Works on older browsers
- **Smaller Bundle**: WebGL-only builds are lighter
- **Mature Ecosystem**: More examples and resources

## Advanced Three.js Techniques

### Custom Render Targets

```javascript
const renderTarget = new THREE.WebGLRenderTarget(512, 512, {
  minFilter: THREE.LinearFilter,
  magFilter: THREE.LinearFilter,
  format: THREE.RGBAFormat,
  type: THREE.FloatType
});

// Render to texture
renderer.setRenderTarget(renderTarget);
renderer.render(scene, camera);
renderer.setRenderTarget(null); // Back to screen

// Use rendered texture
const material = new THREE.MeshBasicMaterial({
  map: renderTarget.texture
});
```

### Instanced Rendering

```javascript
const geometry = new THREE.BoxGeometry(1, 1, 1);
const material = new THREE.MeshStandardMaterial({ color: 0x00ff00 });
const count = 10000;

const instancedMesh = new THREE.InstancedMesh(geometry, material, count);

const matrix = new THREE.Matrix4();
const color = new THREE.Color();

for (let i = 0; i < count; i++) {
  // Set position, rotation, scale
  matrix.setPosition(
    Math.random() * 100 - 50,
    Math.random() * 100 - 50,
    Math.random() * 100 - 50
  );
  instancedMesh.setMatrixAt(i, matrix);
  
  // Set per-instance color
  color.setHex(Math.random() * 0xffffff);
  instancedMesh.setColorAt(i, color);
}

instancedMesh.instanceMatrix.needsUpdate = true;
instancedMesh.instanceColor.needsUpdate = true;

scene.add(instancedMesh);
```

### Animation System

```javascript
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader';

const loader = new GLTFLoader();
let mixer;

loader.load('/models/animated.glb', (gltf) => {
  const model = gltf.scene;
  scene.add(model);
  
  // Create animation mixer
  mixer = new THREE.AnimationMixer(model);
  
  // Play all animations
  gltf.animations.forEach((clip) => {
    const action = mixer.clipAction(clip);
    action.play();
  });
  
  // Or play specific animation
  const walkAction = mixer.clipAction(gltf.animations[0]);
  walkAction.setLoop(THREE.LoopRepeat);
  walkAction.play();
});

// Update in animation loop
const clock = new THREE.Clock();

function animate() {
  const delta = clock.getDelta();
  if (mixer) mixer.update(delta);
  
  renderer.render(scene, camera);
  requestAnimationFrame(animate);
}
```

## Best Practices

### Performance Optimization

1. **Minimize Draw Calls**: Use instancing and batching
2. **Dispose Resources**: Always clean up geometries, materials, textures
3. **Optimize Shaders**: Use appropriate precision, minimize varyings
4. **Frustum Culling**: Automatically enabled, but be aware of it
5. **Level of Detail**: Swap models based on distance
6. **Texture Atlasing**: Combine textures to reduce binds
7. **Shadow Optimization**: Limit shadow-casting lights, appropriate map sizes

### Memory Management

```javascript
function disposeObject(object) {
  if (object.geometry) object.geometry.dispose();
  
  if (object.material) {
    if (Array.isArray(object.material)) {
      object.material.forEach(material => material.dispose());
    } else {
      object.material.dispose();
    }
  }
  
  if (object.texture) object.texture.dispose();
  if (object.renderTarget) object.renderTarget.dispose();
}

// Recursive disposal
function disposeHierarchy(object) {
  object.traverse((child) => {
    disposeObject(child);
  });
}
```

### Debugging

```javascript
// Check renderer statistics
console.log(renderer.info);
// Output: { memory: { geometries, textures }, render: { calls, triangles, ... } }

// Enable WebGL debugging
const renderer = new THREE.WebGLRenderer({
  canvas: canvas,
  context: canvas.getContext('webgl2', { 
    powerPreference: 'high-performance',
    failIfMajorPerformanceCaveat: true 
  })
});

// Check for WebGL errors
const gl = renderer.getContext();
const error = gl.getError();
if (error !== gl.NO_ERROR) {
  console.error('WebGL Error:', error);
}
```

## Conclusion

WebGL and Three.js provide a powerful foundation for creating 3D web experiences. Understanding the underlying graphics pipeline, shader programming, and Three.js architecture enables developers to build performant, visually stunning applications. With WebGPU emerging as the next-generation API and Three.js providing seamless migration paths, the future of 3D web graphics is brighter than ever.

Mastery comes from understanding both the high-level abstractions Three.js provides and the low-level WebGL/WebGPU concepts that power them. This knowledge enables informed optimization decisions and unlocks advanced techniques for creating cutting-edge 3D web experiences.
