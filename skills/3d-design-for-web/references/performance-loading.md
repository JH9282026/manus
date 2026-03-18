# Performance and Loading Strategies for 3D Web

## Overview

Performance optimization and efficient loading strategies are critical for 3D web experiences. Unlike traditional web content, 3D applications involve large assets, complex rendering pipelines, and continuous GPU computation. Poor performance leads to stuttering animations, long load times, and frustrated users who abandon the experience.

This guide covers comprehensive strategies for optimizing 3D web performance, implementing efficient loading patterns, monitoring metrics, and ensuring smooth experiences across diverse devices and network conditions.

## Loading Strategies

### Progressive Loading

Display content incrementally rather than waiting for everything to load:

```javascript
class ProgressiveLoader {
  constructor(scene) {
    this.scene = scene;
    this.loadingManager = new THREE.LoadingManager();
    this.setupLoadingHandlers();
  }
  
  setupLoadingHandlers() {
    this.loadingManager.onStart = (url, loaded, total) => {
      this.showLoadingScreen();
    };
    
    this.loadingManager.onProgress = (url, loaded, total) => {
      const progress = (loaded / total) * 100;
      this.updateProgressBar(progress);
      console.log(`Loading: ${progress.toFixed(1)}%`);
    };
    
    this.loadingManager.onLoad = () => {
      this.hideLoadingScreen();
      this.startExperience();
    };
    
    this.loadingManager.onError = (url) => {
      console.error(`Error loading: ${url}`);
      this.showErrorMessage(`Failed to load ${url}`);
    };
  }
  
  async loadInStages() {
    // Stage 1: Critical assets (placeholder geometry)
    await this.loadPlaceholders();
    this.hideLoadingScreen();
    this.startExperience();
    
    // Stage 2: High-priority assets
    await this.loadHighPriority();
    
    // Stage 3: Background loading of remaining assets
    this.loadRemainingAssets();
  }
  
  async loadPlaceholders() {
    // Simple geometry as placeholders
    const geometry = new THREE.BoxGeometry(1, 1, 1);
    const material = new THREE.MeshBasicMaterial({ color: 0xcccccc });
    const placeholder = new THREE.Mesh(geometry, material);
    this.scene.add(placeholder);
  }
  
  async loadHighPriority() {
    // Load visible/important models first
    const loader = new GLTFLoader(this.loadingManager);
    const model = await loader.loadAsync('/models/hero.glb');
    this.scene.add(model.scene);
  }
  
  loadRemainingAssets() {
    // Load in background without blocking
    requestIdleCallback(() => {
      this.loadSecondaryModels();
      this.loadEnvironmentMaps();
      this.loadAdditionalTextures();
    });
  }
  
  showLoadingScreen() {
    document.getElementById('loading-screen').style.display = 'flex';
  }
  
  hideLoadingScreen() {
    const loadingScreen = document.getElementById('loading-screen');
    loadingScreen.style.opacity = '0';
    setTimeout(() => {
      loadingScreen.style.display = 'none';
    }, 500);
  }
  
  updateProgressBar(progress) {
    const bar = document.getElementById('progress-bar');
    bar.style.width = `${progress}%`;
    document.getElementById('progress-text').textContent = `${progress.toFixed(0)}%`;
  }
  
  showErrorMessage(message) {
    document.getElementById('error-message').textContent = message;
    document.getElementById('error-screen').style.display = 'flex';
  }
  
  startExperience() {
    // Initialize animations, interactions, etc.
  }
}

const loader = new ProgressiveLoader(scene);
loader.loadInStages();
```

### Lazy Loading

Load assets only when needed:

```javascript
class LazyAssetLoader {
  constructor() {
    this.cache = new Map();
    this.loader = new GLTFLoader();
  }
  
  async loadWhenVisible(modelPath, container) {
    // Use Intersection Observer
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(async (entry) => {
        if (entry.isIntersecting) {
          await this.loadModel(modelPath, container);
          observer.unobserve(entry.target);
        }
      });
    }, {
      rootMargin: '100px' // Start loading before visible
    });
    
    observer.observe(container);
  }
  
  async loadOnInteraction(modelPath, trigger) {
    // Load when user interacts
    const loadHandler = async () => {
      await this.loadModel(modelPath);
      trigger.removeEventListener('click', loadHandler);
    };
    
    trigger.addEventListener('click', loadHandler);
  }
  
  async loadModel(path, container) {
    if (this.cache.has(path)) {
      return this.cache.get(path);
    }
    
    const gltf = await this.loader.loadAsync(path);
    this.cache.set(path, gltf);
    
    if (container) {
      container.add(gltf.scene);
    }
    
    return gltf;
  }
  
  async preload(paths) {
    // Preload during idle time
    return new Promise((resolve) => {
      requestIdleCallback(async () => {
        await Promise.all(paths.map(path => this.loadModel(path)));
        resolve();
      });
    });
  }
}

const lazyLoader = new LazyAssetLoader();

// Load when scrolled into view
lazyLoader.loadWhenVisible('/models/product.glb', document.getElementById('product-section'));

// Load on user interaction
lazyLoader.loadOnInteraction('/models/details.glb', document.getElementById('view-details-btn'));

// Preload during idle time
lazyLoader.preload(['/models/model1.glb', '/models/model2.glb']);
```

### Code Splitting

Split Three.js modules to reduce initial bundle:

```javascript
// Dynamic imports for code splitting
async function initScene() {
  // Load core Three.js
  const THREE = await import('three');
  
  // Load controls only when needed
  const { OrbitControls } = await import('three/examples/jsm/controls/OrbitControls');
  
  // Load loaders on demand
  const { GLTFLoader } = await import('three/examples/jsm/loaders/GLTFLoader');
  const { DRACOLoader } = await import('three/examples/jsm/loaders/DRACOLoader');
  
  // Initialize scene
  const scene = new THREE.Scene();
  // ...
}

// Load post-processing only if needed
async function enablePostProcessing() {
  const { EffectComposer, RenderPass, BloomEffect } = await import('postprocessing');
  // Setup post-processing
}
```

**Webpack Configuration:**
```javascript
// webpack.config.js
module.exports = {
  optimization: {
    splitChunks: {
      chunks: 'all',
      cacheGroups: {
        three: {
          test: /[\\/]node_modules[\\/]three[\\/]/,
          name: 'three',
          priority: 10
        },
        vendor: {
          test: /[\\/]node_modules[\\/]/,
          name: 'vendors',
          priority: 5
        }
      }
    }
  }
};
```

### Streaming Large Scenes

Stream scene data in chunks:

```javascript
class SceneStreamer {
  constructor(scene, camera) {
    this.scene = scene;
    this.camera = camera;
    this.chunks = new Map();
    this.loadedChunks = new Set();
    this.chunkSize = 50; // Units
  }
  
  getChunkKey(position) {
    const x = Math.floor(position.x / this.chunkSize);
    const z = Math.floor(position.z / this.chunkSize);
    return `${x},${z}`;
  }
  
  async update() {
    const cameraChunk = this.getChunkKey(this.camera.position);
    const chunksToLoad = this.getVisibleChunks(cameraChunk);
    
    // Load visible chunks
    for (const chunkKey of chunksToLoad) {
      if (!this.loadedChunks.has(chunkKey)) {
        await this.loadChunk(chunkKey);
      }
    }
    
    // Unload distant chunks
    for (const chunkKey of this.loadedChunks) {
      if (!chunksToLoad.includes(chunkKey)) {
        this.unloadChunk(chunkKey);
      }
    }
  }
  
  getVisibleChunks(centerChunk) {
    const [cx, cz] = centerChunk.split(',').map(Number);
    const chunks = [];
    const radius = 2; // Load 2 chunks in each direction
    
    for (let x = cx - radius; x <= cx + radius; x++) {
      for (let z = cz - radius; z <= cz + radius; z++) {
        chunks.push(`${x},${z}`);
      }
    }
    
    return chunks;
  }
  
  async loadChunk(chunkKey) {
    const [x, z] = chunkKey.split(',').map(Number);
    const chunkData = await fetch(`/chunks/${chunkKey}.json`).then(r => r.json());
    
    const chunkGroup = new THREE.Group();
    chunkGroup.name = chunkKey;
    
    // Load chunk objects
    for (const obj of chunkData.objects) {
      const mesh = await this.createMeshFromData(obj);
      chunkGroup.add(mesh);
    }
    
    this.scene.add(chunkGroup);
    this.chunks.set(chunkKey, chunkGroup);
    this.loadedChunks.add(chunkKey);
  }
  
  unloadChunk(chunkKey) {
    const chunk = this.chunks.get(chunkKey);
    if (chunk) {
      chunk.traverse((child) => {
        if (child.geometry) child.geometry.dispose();
        if (child.material) child.material.dispose();
      });
      this.scene.remove(chunk);
      this.chunks.delete(chunkKey);
      this.loadedChunks.delete(chunkKey);
    }
  }
  
  async createMeshFromData(data) {
    // Create mesh from chunk data
    const geometry = new THREE.BoxGeometry(data.size.x, data.size.y, data.size.z);
    const material = new THREE.MeshStandardMaterial({ color: data.color });
    const mesh = new THREE.Mesh(geometry, material);
    mesh.position.set(data.position.x, data.position.y, data.position.z);
    return mesh;
  }
}

const streamer = new SceneStreamer(scene, camera);

// Update in animation loop
function animate() {
  streamer.update();
  renderer.render(scene, camera);
  requestAnimationFrame(animate);
}
```

## Performance Optimization

### Render Loop Optimization

```javascript
class OptimizedRenderLoop {
  constructor(renderer, scene, camera) {
    this.renderer = renderer;
    this.scene = scene;
    this.camera = camera;
    this.clock = new THREE.Clock();
    this.frameId = null;
    this.targetFPS = 60;
    this.frameInterval = 1000 / this.targetFPS;
    this.lastFrameTime = 0;
  }
  
  start() {
    this.animate(0);
  }
  
  stop() {
    if (this.frameId) {
      cancelAnimationFrame(this.frameId);
      this.frameId = null;
    }
  }
  
  animate(currentTime) {
    this.frameId = requestAnimationFrame(this.animate.bind(this));
    
    // Frame rate limiting
    const elapsed = currentTime - this.lastFrameTime;
    if (elapsed < this.frameInterval) return;
    
    this.lastFrameTime = currentTime - (elapsed % this.frameInterval);
    
    // Delta time for frame-rate independent animations
    const delta = this.clock.getDelta();
    
    // Update logic
    this.update(delta);
    
    // Render
    this.renderer.render(this.scene, this.camera);
  }
  
  update(delta) {
    // Update animations, physics, etc.
  }
}

const renderLoop = new OptimizedRenderLoop(renderer, scene, camera);
renderLoop.start();

// Pause when tab not visible
document.addEventListener('visibilitychange', () => {
  if (document.hidden) {
    renderLoop.stop();
  } else {
    renderLoop.start();
  }
});
```

### Frustum Culling

Automatic in Three.js, but can be optimized:

```javascript
// Disable frustum culling for always-visible objects
skybox.frustumCulled = false;

// Manual culling for complex scenes
const frustum = new THREE.Frustum();
const cameraViewProjectionMatrix = new THREE.Matrix4();

function updateVisibility() {
  camera.updateMatrixWorld();
  camera.matrixWorldInverse.copy(camera.matrixWorld).invert();
  cameraViewProjectionMatrix.multiplyMatrices(
    camera.projectionMatrix,
    camera.matrixWorldInverse
  );
  frustum.setFromProjectionMatrix(cameraViewProjectionMatrix);
  
  scene.traverse((object) => {
    if (object.isMesh) {
      object.visible = frustum.intersectsObject(object);
    }
  });
}
```

### Object Pooling

Reuse objects instead of creating/destroying:

```javascript
class ObjectPool {
  constructor(factory, initialSize = 10) {
    this.factory = factory;
    this.available = [];
    this.inUse = new Set();
    
    // Pre-create objects
    for (let i = 0; i < initialSize; i++) {
      this.available.push(this.factory());
    }
  }
  
  acquire() {
    let object;
    
    if (this.available.length > 0) {
      object = this.available.pop();
    } else {
      object = this.factory();
    }
    
    this.inUse.add(object);
    return object;
  }
  
  release(object) {
    if (this.inUse.has(object)) {
      this.inUse.delete(object);
      this.available.push(object);
      
      // Reset object state
      object.position.set(0, 0, 0);
      object.rotation.set(0, 0, 0);
      object.scale.set(1, 1, 1);
      object.visible = false;
    }
  }
  
  clear() {
    this.available.forEach(obj => {
      if (obj.geometry) obj.geometry.dispose();
      if (obj.material) obj.material.dispose();
    });
    this.available = [];
    this.inUse.clear();
  }
}

// Usage for particle system
const particlePool = new ObjectPool(() => {
  const geometry = new THREE.SphereGeometry(0.1, 8, 8);
  const material = new THREE.MeshBasicMaterial({ color: 0xffffff });
  return new THREE.Mesh(geometry, material);
}, 100);

// Spawn particle
const particle = particlePool.acquire();
particle.position.set(x, y, z);
particle.visible = true;
scene.add(particle);

// Return to pool when done
setTimeout(() => {
  scene.remove(particle);
  particlePool.release(particle);
}, 2000);
```

### Texture and Material Caching

```javascript
class AssetCache {
  constructor() {
    this.textures = new Map();
    this.materials = new Map();
    this.geometries = new Map();
    this.textureLoader = new THREE.TextureLoader();
  }
  
  getTexture(path) {
    if (!this.textures.has(path)) {
      const texture = this.textureLoader.load(path);
      this.textures.set(path, texture);
    }
    return this.textures.get(path);
  }
  
  getMaterial(key, factory) {
    if (!this.materials.has(key)) {
      this.materials.set(key, factory());
    }
    return this.materials.get(key);
  }
  
  getGeometry(key, factory) {
    if (!this.geometries.has(key)) {
      this.geometries.set(key, factory());
    }
    return this.geometries.get(key);
  }
  
  dispose() {
    this.textures.forEach(texture => texture.dispose());
    this.materials.forEach(material => material.dispose());
    this.geometries.forEach(geometry => geometry.dispose());
    
    this.textures.clear();
    this.materials.clear();
    this.geometries.clear();
  }
}

const cache = new AssetCache();

// Reuse cached assets
const texture = cache.getTexture('/textures/diffuse.jpg');
const material = cache.getMaterial('standard-red', () => 
  new THREE.MeshStandardMaterial({ color: 0xff0000 })
);
```

## Performance Monitoring

### Stats and Metrics

```javascript
import Stats from 'stats-gl';

const stats = new Stats({
  logsPerSecond: 20,
  samplesLog: 100,
  samplesGraph: 10,
  precision: 2,
  horizontal: true,
  minimal: false,
  mode: 0 // 0: fps, 1: ms, 2: mb
});

document.body.appendChild(stats.dom);

function animate() {
  stats.begin();
  
  // Render logic
  renderer.render(scene, camera);
  
  stats.end();
  requestAnimationFrame(animate);
}

// Custom performance tracking
class PerformanceMonitor {
  constructor() {
    this.metrics = {
      fps: 0,
      frameTime: 0,
      drawCalls: 0,
      triangles: 0,
      geometries: 0,
      textures: 0
    };
    this.frameTimes = [];
    this.lastTime = performance.now();
  }
  
  update(renderer) {
    const currentTime = performance.now();
    const frameTime = currentTime - this.lastTime;
    this.lastTime = currentTime;
    
    this.frameTimes.push(frameTime);
    if (this.frameTimes.length > 60) {
      this.frameTimes.shift();
    }
    
    const avgFrameTime = this.frameTimes.reduce((a, b) => a + b) / this.frameTimes.length;
    
    this.metrics.fps = Math.round(1000 / avgFrameTime);
    this.metrics.frameTime = avgFrameTime.toFixed(2);
    this.metrics.drawCalls = renderer.info.render.calls;
    this.metrics.triangles = renderer.info.render.triangles;
    this.metrics.geometries = renderer.info.memory.geometries;
    this.metrics.textures = renderer.info.memory.textures;
  }
  
  getReport() {
    return `
      FPS: ${this.metrics.fps}
      Frame Time: ${this.metrics.frameTime}ms
      Draw Calls: ${this.metrics.drawCalls}
      Triangles: ${this.metrics.triangles.toLocaleString()}
      Geometries: ${this.metrics.geometries}
      Textures: ${this.metrics.textures}
    `;
  }
}

const monitor = new PerformanceMonitor();

function animate() {
  monitor.update(renderer);
  console.log(monitor.getReport());
  
  renderer.render(scene, camera);
  requestAnimationFrame(animate);
}
```

### Performance Budgets

```javascript
class PerformanceBudget {
  constructor(budgets) {
    this.budgets = budgets;
    this.warnings = [];
  }
  
  check(renderer) {
    this.warnings = [];
    
    const info = renderer.info;
    
    if (info.render.calls > this.budgets.drawCalls) {
      this.warnings.push(`Draw calls (${info.render.calls}) exceed budget (${this.budgets.drawCalls})`);
    }
    
    if (info.render.triangles > this.budgets.triangles) {
      this.warnings.push(`Triangles (${info.render.triangles}) exceed budget (${this.budgets.triangles})`);
    }
    
    if (info.memory.textures > this.budgets.textures) {
      this.warnings.push(`Textures (${info.memory.textures}) exceed budget (${this.budgets.textures})`);
    }
    
    if (this.warnings.length > 0) {
      console.warn('Performance budget exceeded:', this.warnings);
    }
    
    return this.warnings.length === 0;
  }
}

const budget = new PerformanceBudget({
  drawCalls: 100,
  triangles: 200000,
  textures: 50
});

function animate() {
  budget.check(renderer);
  renderer.render(scene, camera);
  requestAnimationFrame(animate);
}
```

## Device-Specific Optimization

### Adaptive Quality

```javascript
class AdaptiveQuality {
  constructor(renderer, scene) {
    this.renderer = renderer;
    this.scene = scene;
    this.targetFPS = 60;
    this.currentQuality = 'high';
    this.fpsHistory = [];
  }
  
  update(currentFPS) {
    this.fpsHistory.push(currentFPS);
    if (this.fpsHistory.length > 60) {
      this.fpsHistory.shift();
    }
    
    const avgFPS = this.fpsHistory.reduce((a, b) => a + b) / this.fpsHistory.length;
    
    if (avgFPS < this.targetFPS * 0.8 && this.currentQuality !== 'low') {
      this.lowerQuality();
    } else if (avgFPS > this.targetFPS * 0.95 && this.currentQuality !== 'high') {
      this.raiseQuality();
    }
  }
  
  lowerQuality() {
    if (this.currentQuality === 'high') {
      this.currentQuality = 'medium';
      this.applyMediumQuality();
    } else if (this.currentQuality === 'medium') {
      this.currentQuality = 'low';
      this.applyLowQuality();
    }
    console.log('Quality lowered to:', this.currentQuality);
  }
  
  raiseQuality() {
    if (this.currentQuality === 'low') {
      this.currentQuality = 'medium';
      this.applyMediumQuality();
    } else if (this.currentQuality === 'medium') {
      this.currentQuality = 'high';
      this.applyHighQuality();
    }
    console.log('Quality raised to:', this.currentQuality);
  }
  
  applyHighQuality() {
    this.renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    this.renderer.shadowMap.enabled = true;
    this.scene.traverse((obj) => {
      if (obj.isLOD) obj.update(camera); // Use high LOD
    });
  }
  
  applyMediumQuality() {
    this.renderer.setPixelRatio(1.5);
    this.renderer.shadowMap.enabled = true;
  }
  
  applyLowQuality() {
    this.renderer.setPixelRatio(1);
    this.renderer.shadowMap.enabled = false;
  }
}

const adaptiveQuality = new AdaptiveQuality(renderer, scene);
```

## Conclusion

Performance and loading optimization are ongoing processes requiring monitoring, testing, and iteration. By implementing progressive loading, lazy loading strategies, render loop optimization, and adaptive quality systems, developers can create 3D web experiences that load quickly and run smoothly across diverse devices and network conditions.

The key is balancing visual quality with performance constraints, measuring real-world metrics, and continuously optimizing based on user data and device capabilities.
