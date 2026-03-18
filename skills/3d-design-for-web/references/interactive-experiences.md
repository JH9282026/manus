# Interactive 3D Web Experiences

## Overview

Interactive 3D web experiences transform passive viewing into active engagement, allowing users to manipulate, explore, and interact with 3D content directly in their browsers. These experiences range from simple product viewers with rotation controls to complex virtual environments with physics simulations, animations, and real-time user input.

Creating compelling interactive 3D experiences requires understanding user interaction patterns, implementing responsive controls, managing state and animations, and ensuring smooth performance across devices. This guide covers the essential techniques, patterns, and best practices for building engaging interactive 3D web applications.

## User Interaction Patterns

### Camera Controls

Camera controls are the foundation of 3D interaction, allowing users to navigate and explore scenes.

**Orbit Controls (Most Common):**
```javascript
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls';

const controls = new OrbitControls(camera, renderer.domElement);

// Configuration
controls.enableDamping = true;        // Smooth motion
controls.dampingFactor = 0.05;        // Damping intensity
controls.screenSpacePanning = false;  // Pan in camera space
controls.minDistance = 2;             // Zoom limits
controls.maxDistance = 10;
controls.maxPolarAngle = Math.PI / 2; // Prevent going below ground

// Restrict rotation
controls.minAzimuthAngle = -Math.PI / 4;
controls.maxAzimuthAngle = Math.PI / 4;

// Auto-rotate
controls.autoRotate = true;
controls.autoRotateSpeed = 2.0;

// Update in animation loop
function animate() {
  controls.update(); // Required when enableDamping = true
  renderer.render(scene, camera);
  requestAnimationFrame(animate);
}
```

**First-Person Controls:**
```javascript
import { PointerLockControls } from 'three/examples/jsm/controls/PointerLockControls';

const controls = new PointerLockControls(camera, renderer.domElement);

// Activate on click
renderer.domElement.addEventListener('click', () => {
  controls.lock();
});

controls.addEventListener('lock', () => {
  console.log('Controls locked');
});

controls.addEventListener('unlock', () => {
  console.log('Controls unlocked');
});

// Movement with keyboard
const velocity = new THREE.Vector3();
const direction = new THREE.Vector3();
const moveSpeed = 10.0;

const keyboard = {};
window.addEventListener('keydown', (e) => keyboard[e.code] = true);
window.addEventListener('keyup', (e) => keyboard[e.code] = false);

function animate(time, delta) {
  if (controls.isLocked) {
    direction.z = Number(keyboard['KeyW']) - Number(keyboard['KeyS']);
    direction.x = Number(keyboard['KeyA']) - Number(keyboard['KeyD']);
    direction.normalize();
    
    velocity.z = direction.z * moveSpeed * delta;
    velocity.x = direction.x * moveSpeed * delta;
    
    controls.moveForward(velocity.z);
    controls.moveRight(velocity.x);
  }
  
  renderer.render(scene, camera);
  requestAnimationFrame(animate);
}
```

**Trackball Controls:**
```javascript
import { TrackballControls } from 'three/examples/jsm/controls/TrackballControls';

const controls = new TrackballControls(camera, renderer.domElement);
controls.rotateSpeed = 1.0;
controls.zoomSpeed = 1.2;
controls.panSpeed = 0.8;
controls.noZoom = false;
controls.noPan = false;
controls.staticMoving = true;
controls.dynamicDampingFactor = 0.3;
```

### Object Selection and Raycasting

Raycasting detects which 3D objects the user is pointing at or clicking:

```javascript
const raycaster = new THREE.Raycaster();
const mouse = new THREE.Vector2();
let selectedObject = null;

// Update mouse position
function onMouseMove(event) {
  mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
  mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;
}

// Handle click
function onClick(event) {
  raycaster.setFromCamera(mouse, camera);
  const intersects = raycaster.intersectObjects(scene.children, true);
  
  if (intersects.length > 0) {
    const object = intersects[0].object;
    
    // Deselect previous
    if (selectedObject) {
      selectedObject.material.emissive.setHex(0x000000);
    }
    
    // Select new
    selectedObject = object;
    selectedObject.material.emissive.setHex(0x555555);
    
    // Get intersection details
    const point = intersects[0].point;     // 3D position
    const face = intersects[0].face;       // Triangle face
    const distance = intersects[0].distance; // Distance from camera
    
    console.log('Clicked:', object.name, 'at', point);
  }
}

window.addEventListener('mousemove', onMouseMove);
window.addEventListener('click', onClick);
```

**Optimized Raycasting with BVH:**
```javascript
import { computeBoundsTree, disposeBoundsTree, acceleratedRaycast } from 'three-mesh-bvh';

// Extend Three.js prototypes
THREE.BufferGeometry.prototype.computeBoundsTree = computeBoundsTree;
THREE.BufferGeometry.prototype.disposeBoundsTree = disposeBoundsTree;
THREE.Mesh.prototype.raycast = acceleratedRaycast;

// Build BVH for faster raycasting
mesh.geometry.computeBoundsTree();

// Raycasting is now significantly faster
const intersects = raycaster.intersectObjects(scene.children, true);
```

### Drag and Drop

Implement draggable 3D objects:

```javascript
import { DragControls } from 'three/examples/jsm/controls/DragControls';

const draggableObjects = [mesh1, mesh2, mesh3];
const dragControls = new DragControls(draggableObjects, camera, renderer.domElement);

// Event listeners
dragControls.addEventListener('dragstart', (event) => {
  orbitControls.enabled = false; // Disable orbit during drag
  event.object.material.emissive.setHex(0xaaaaaa);
});

dragControls.addEventListener('drag', (event) => {
  console.log('Dragging:', event.object.position);
});

dragControls.addEventListener('dragend', (event) => {
  orbitControls.enabled = true;
  event.object.material.emissive.setHex(0x000000);
});

// Custom drag plane constraint
dragControls.addEventListener('drag', (event) => {
  event.object.position.y = 0; // Constrain to ground plane
});
```

**Custom Drag Implementation:**
```javascript
class ObjectDragger {
  constructor(camera, objects, domElement) {
    this.camera = camera;
    this.objects = objects;
    this.domElement = domElement;
    this.raycaster = new THREE.Raycaster();
    this.mouse = new THREE.Vector2();
    this.plane = new THREE.Plane();
    this.intersection = new THREE.Vector3();
    this.offset = new THREE.Vector3();
    this.selected = null;
    
    this.setupEventListeners();
  }
  
  setupEventListeners() {
    this.domElement.addEventListener('mousedown', this.onMouseDown.bind(this));
    this.domElement.addEventListener('mousemove', this.onMouseMove.bind(this));
    this.domElement.addEventListener('mouseup', this.onMouseUp.bind(this));
  }
  
  onMouseDown(event) {
    this.updateMouse(event);
    this.raycaster.setFromCamera(this.mouse, this.camera);
    
    const intersects = this.raycaster.intersectObjects(this.objects);
    if (intersects.length > 0) {
      this.selected = intersects[0].object;
      
      // Create drag plane perpendicular to camera
      this.plane.setFromNormalAndCoplanarPoint(
        this.camera.getWorldDirection(this.plane.normal),
        this.selected.position
      );
      
      // Calculate offset
      this.raycaster.ray.intersectPlane(this.plane, this.intersection);
      this.offset.copy(this.intersection).sub(this.selected.position);
    }
  }
  
  onMouseMove(event) {
    if (this.selected) {
      this.updateMouse(event);
      this.raycaster.setFromCamera(this.mouse, this.camera);
      
      if (this.raycaster.ray.intersectPlane(this.plane, this.intersection)) {
        this.selected.position.copy(this.intersection.sub(this.offset));
      }
    }
  }
  
  onMouseUp() {
    this.selected = null;
  }
  
  updateMouse(event) {
    this.mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
    this.mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;
  }
}

const dragger = new ObjectDragger(camera, draggableObjects, renderer.domElement);
```

## Animation and State Management

### Animation Mixer

Manage complex animations from GLTF models:

```javascript
let mixer, actions = {};

gltfLoader.load('/model.glb', (gltf) => {
  const model = gltf.scene;
  scene.add(model);
  
  // Create mixer
  mixer = new THREE.AnimationMixer(model);
  
  // Store all animations
  gltf.animations.forEach((clip) => {
    actions[clip.name] = mixer.clipAction(clip);
  });
  
  // Play default animation
  actions['Idle'].play();
});

// Update in animation loop
const clock = new THREE.Clock();

function animate() {
  const delta = clock.getDelta();
  if (mixer) mixer.update(delta);
  
  renderer.render(scene, camera);
  requestAnimationFrame(animate);
}

// Transition between animations
function playAnimation(name, duration = 0.5) {
  const from = Object.values(actions).find(action => action.isRunning());
  const to = actions[name];
  
  if (from && from !== to) {
    from.fadeOut(duration);
  }
  
  to.reset().fadeIn(duration).play();
}

// Usage
playAnimation('Walk');
```

### Tween Animations

Smooth property animations using GSAP or Tween.js:

**Using GSAP:**
```javascript
import gsap from 'gsap';

// Animate object position
gsap.to(mesh.position, {
  x: 5,
  y: 2,
  z: 0,
  duration: 2,
  ease: 'power2.inOut',
  onUpdate: () => {
    // Called every frame
  },
  onComplete: () => {
    console.log('Animation complete');
  }
});

// Animate camera
gsap.to(camera.position, {
  x: 10,
  y: 5,
  z: 10,
  duration: 3,
  ease: 'power3.inOut'
});

// Animate material properties
gsap.to(material, {
  opacity: 0,
  duration: 1,
  onUpdate: () => {
    material.needsUpdate = true;
  }
});

// Timeline for complex sequences
const timeline = gsap.timeline();
timeline
  .to(mesh.position, { y: 2, duration: 1 })
  .to(mesh.rotation, { y: Math.PI * 2, duration: 2 }, '-=0.5')
  .to(mesh.scale, { x: 2, y: 2, z: 2, duration: 1 });
```

**Using Tween.js:**
```javascript
import TWEEN from '@tweenjs/tween.js';

const tween = new TWEEN.Tween(mesh.position)
  .to({ x: 5, y: 2, z: 0 }, 2000)
  .easing(TWEEN.Easing.Quadratic.InOut)
  .onUpdate(() => {
    // Called every frame
  })
  .onComplete(() => {
    console.log('Complete');
  })
  .start();

// Update in animation loop
function animate() {
  TWEEN.update();
  renderer.render(scene, camera);
  requestAnimationFrame(animate);
}
```

### State Management

Manage application state for complex interactions:

```javascript
class SceneState {
  constructor() {
    this.currentView = 'overview';
    this.selectedProduct = null;
    this.animating = false;
    this.listeners = [];
  }
  
  setState(updates) {
    Object.assign(this, updates);
    this.notify();
  }
  
  subscribe(listener) {
    this.listeners.push(listener);
  }
  
  notify() {
    this.listeners.forEach(listener => listener(this));
  }
}

const state = new SceneState();

// Subscribe to state changes
state.subscribe((newState) => {
  console.log('State changed:', newState);
  
  if (newState.currentView === 'detail') {
    animateCameraToProduct(newState.selectedProduct);
  }
});

// Update state
state.setState({ 
  currentView: 'detail', 
  selectedProduct: product1 
});
```

## Scroll-Based Interactions

Synchronize 3D animations with page scroll:

```javascript
class ScrollAnimation {
  constructor(scene, camera) {
    this.scene = scene;
    this.camera = camera;
    this.scrollY = 0;
    this.setupScrollListener();
  }
  
  setupScrollListener() {
    window.addEventListener('scroll', () => {
      this.scrollY = window.scrollY;
    });
  }
  
  update() {
    // Normalize scroll (0 to 1)
    const maxScroll = document.body.scrollHeight - window.innerHeight;
    const scrollProgress = this.scrollY / maxScroll;
    
    // Animate camera based on scroll
    this.camera.position.y = scrollProgress * 10;
    this.camera.rotation.x = scrollProgress * Math.PI / 4;
    
    // Animate objects
    this.scene.children.forEach((child, index) => {
      if (child.isMesh) {
        child.rotation.y = scrollProgress * Math.PI * 2 + index;
        child.position.x = Math.sin(scrollProgress * Math.PI * 2) * 5;
      }
    });
  }
}

const scrollAnim = new ScrollAnimation(scene, camera);

function animate() {
  scrollAnim.update();
  renderer.render(scene, camera);
  requestAnimationFrame(animate);
}
```

**Scroll Sections with GSAP ScrollTrigger:**
```javascript
import { ScrollTrigger } from 'gsap/ScrollTrigger';
gsap.registerPlugin(ScrollTrigger);

// Animate on scroll into view
gsap.to(mesh.rotation, {
  y: Math.PI * 2,
  scrollTrigger: {
    trigger: '#section1',
    start: 'top center',
    end: 'bottom center',
    scrub: true, // Smooth scrubbing
    markers: true // Debug markers
  }
});

// Pin scene while scrolling
ScrollTrigger.create({
  trigger: '#canvas-container',
  start: 'top top',
  end: '+=2000',
  pin: true,
  onUpdate: (self) => {
    const progress = self.progress;
    camera.position.z = 10 - progress * 5;
  }
});
```

## Touch and Mobile Interactions

Optimize for touch devices:

```javascript
class TouchHandler {
  constructor(domElement, camera, scene) {
    this.domElement = domElement;
    this.camera = camera;
    this.scene = scene;
    this.touches = [];
    this.setupTouchListeners();
  }
  
  setupTouchListeners() {
    this.domElement.addEventListener('touchstart', this.onTouchStart.bind(this));
    this.domElement.addEventListener('touchmove', this.onTouchMove.bind(this));
    this.domElement.addEventListener('touchend', this.onTouchEnd.bind(this));
  }
  
  onTouchStart(event) {
    event.preventDefault();
    this.touches = Array.from(event.touches);
    
    if (this.touches.length === 1) {
      // Single touch - rotation
      this.handleSingleTouch(this.touches[0]);
    } else if (this.touches.length === 2) {
      // Two fingers - pinch zoom
      this.initialPinchDistance = this.getPinchDistance();
      this.initialCameraZ = this.camera.position.z;
    }
  }
  
  onTouchMove(event) {
    event.preventDefault();
    const currentTouches = Array.from(event.touches);
    
    if (currentTouches.length === 1 && this.touches.length === 1) {
      const deltaX = currentTouches[0].clientX - this.touches[0].clientX;
      const deltaY = currentTouches[0].clientY - this.touches[0].clientY;
      
      this.scene.rotation.y += deltaX * 0.01;
      this.scene.rotation.x += deltaY * 0.01;
    } else if (currentTouches.length === 2) {
      const currentDistance = this.getPinchDistance(currentTouches);
      const scale = currentDistance / this.initialPinchDistance;
      this.camera.position.z = this.initialCameraZ / scale;
    }
    
    this.touches = currentTouches;
  }
  
  onTouchEnd(event) {
    this.touches = Array.from(event.touches);
  }
  
  getPinchDistance(touches = this.touches) {
    const dx = touches[0].clientX - touches[1].clientX;
    const dy = touches[0].clientY - touches[1].clientY;
    return Math.sqrt(dx * dx + dy * dy);
  }
  
  handleSingleTouch(touch) {
    // Implement tap detection, object selection, etc.
  }
}

const touchHandler = new TouchHandler(renderer.domElement, camera, scene);
```

## Performance Optimization for Interactions

### Throttling and Debouncing

```javascript
// Throttle: Limit execution frequency
function throttle(func, limit) {
  let inThrottle;
  return function(...args) {
    if (!inThrottle) {
      func.apply(this, args);
      inThrottle = true;
      setTimeout(() => inThrottle = false, limit);
    }
  };
}

// Debounce: Execute after delay
function debounce(func, delay) {
  let timeoutId;
  return function(...args) {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => func.apply(this, args), delay);
  };
}

// Usage
const throttledMouseMove = throttle(onMouseMove, 16); // ~60fps
const debouncedResize = debounce(onWindowResize, 250);

window.addEventListener('mousemove', throttledMouseMove);
window.addEventListener('resize', debouncedResize);
```

### Interaction Layers

Separate interactive objects for efficient raycasting:

```javascript
const interactiveLayer = new THREE.Group();
const staticLayer = new THREE.Group();

scene.add(interactiveLayer);
scene.add(staticLayer);

// Only raycast against interactive objects
function onClick(event) {
  raycaster.setFromCamera(mouse, camera);
  const intersects = raycaster.intersectObjects(interactiveLayer.children, true);
  // Much faster than raycasting entire scene
}
```

## Accessibility Considerations

### Keyboard Navigation

```javascript
class KeyboardControls {
  constructor(scene) {
    this.scene = scene;
    this.focusedIndex = 0;
    this.interactiveObjects = [];
    this.setupKeyboardListeners();
  }
  
  setupKeyboardListeners() {
    window.addEventListener('keydown', (event) => {
      switch(event.key) {
        case 'Tab':
          event.preventDefault();
          this.focusNext(event.shiftKey ? -1 : 1);
          break;
        case 'Enter':
        case ' ':
          event.preventDefault();
          this.activateFocused();
          break;
        case 'Escape':
          this.clearFocus();
          break;
      }
    });
  }
  
  focusNext(direction) {
    this.clearFocus();
    this.focusedIndex = (this.focusedIndex + direction + this.interactiveObjects.length) 
                        % this.interactiveObjects.length;
    this.highlightFocused();
  }
  
  highlightFocused() {
    const object = this.interactiveObjects[this.focusedIndex];
    object.material.emissive.setHex(0x555555);
  }
  
  clearFocus() {
    if (this.interactiveObjects[this.focusedIndex]) {
      this.interactiveObjects[this.focusedIndex].material.emissive.setHex(0x000000);
    }
  }
  
  activateFocused() {
    const object = this.interactiveObjects[this.focusedIndex];
    // Trigger click handler or action
    console.log('Activated:', object.name);
  }
}
```

### Motion Sensitivity

```javascript
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

if (prefersReducedMotion) {
  // Disable auto-rotate
  controls.autoRotate = false;
  
  // Reduce animation speeds
  gsap.globalTimeline.timeScale(0.5);
  
  // Disable parallax effects
  scrollAnimation.enabled = false;
}
```

## Conclusion

Interactive 3D web experiences combine camera controls, object manipulation, animations, and responsive design to create engaging user interfaces. Success requires balancing interactivity with performance, implementing intuitive controls, managing state effectively, and ensuring accessibility across devices.

By mastering raycasting, animation systems, touch handling, and optimization techniques, developers can create immersive 3D experiences that feel natural and responsive while maintaining smooth performance on diverse hardware.
