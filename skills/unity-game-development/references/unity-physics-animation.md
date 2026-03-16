# Unity Physics and Animation Systems

Detailed guide to Unity's physics engine and animation workflows.

---

## Physics System Overview

Unity uses NVIDIA PhysX for 3D physics and Box2D for 2D physics. Both provide realistic simulation of forces, collisions, and constraints.

### Physics vs. Physics2D

| Feature | 3D Physics | 2D Physics |
|---------|-----------|------------|
| Component | Rigidbody | Rigidbody2D |
| Colliders | BoxCollider, SphereCollider, etc. | BoxCollider2D, CircleCollider2D, etc. |
| Gravity | Vector3 (x, y, z) | Vector2 (x, y) |
| Use Case | 3D games | 2D platformers, top-down games |

**Important:** Never mix 3D and 2D physics components on the same object.

---

## Rigidbody Component

### Rigidbody Properties

```csharp
public class RigidbodyExample : MonoBehaviour
{
    private Rigidbody rb;
    
    void Awake()
    {
        rb = GetComponent<Rigidbody>();
        
        // Mass affects force response
        rb.mass = 1f;
        
        // Drag simulates air resistance
        rb.drag = 0.5f;
        
        // Angular drag for rotation resistance
        rb.angularDrag = 0.05f;
        
        // Use gravity
        rb.useGravity = true;
        
        // Kinematic rigidbodies don't respond to forces
        rb.isKinematic = false;
        
        // Interpolation for smooth movement
        rb.interpolation = RigidbodyInterpolation.Interpolate;
        
        // Collision detection mode
        rb.collisionDetectionMode = CollisionDetectionMode.Continuous;
    }
}
```

### Collision Detection Modes

| Mode | Performance | Use Case |
|------|-------------|----------|
| Discrete | Fast | Slow-moving objects |
| Continuous | Moderate | Fast-moving objects (bullets) |
| Continuous Dynamic | Slow | Fast objects colliding with static geometry |
| Continuous Speculative | Balanced | General fast-moving objects |

### Constraints

Freeze position or rotation on specific axes:

```csharp
// Freeze rotation on X and Z (common for character controllers)
rb.constraints = RigidbodyConstraints.FreezeRotationX | RigidbodyConstraints.FreezeRotationZ;

// Freeze Y position (2D platformer in 3D)
rb.constraints = RigidbodyConstraints.FreezePositionY;
```

---

## Applying Forces

### Force Modes

```csharp
public class ForceExamples : MonoBehaviour
{
    private Rigidbody rb;
    
    void Awake()
    {
        rb = GetComponent<Rigidbody>();
    }
    
    void FixedUpdate() // Always use FixedUpdate for physics
    {
        // ForceMode.Force: Continuous force, considers mass
        rb.AddForce(Vector3.forward * 10f, ForceMode.Force);
        
        // ForceMode.Acceleration: Continuous force, ignores mass
        rb.AddForce(Vector3.forward * 10f, ForceMode.Acceleration);
        
        // ForceMode.Impulse: Instant force, considers mass (jumping)
        rb.AddForce(Vector3.up * 5f, ForceMode.Impulse);
        
        // ForceMode.VelocityChange: Instant force, ignores mass
        rb.AddForce(Vector3.up * 5f, ForceMode.VelocityChange);
    }
}
```

### Direct Velocity Manipulation

```csharp
// Set velocity directly (use sparingly)
rb.velocity = new Vector3(5f, rb.velocity.y, 0f);

// Add to existing velocity
rb.velocity += Vector3.forward * 2f;

// Angular velocity for rotation
rb.angularVelocity = Vector3.up * 2f;
```

### Torque (Rotational Force)

```csharp
// Apply torque around Y axis
rb.AddTorque(Vector3.up * 10f);

// Apply torque at a point
rb.AddTorqueAtPosition(Vector3.up * 10f, transform.position);
```

---

## Colliders

### Collider Types

| Collider | Shape | Performance | Use Case |
|----------|-------|-------------|----------|
| BoxCollider | Cube | Fast | Buildings, crates, walls |
| SphereCollider | Sphere | Fastest | Balls, projectiles, simple characters |
| CapsuleCollider | Capsule | Fast | Characters, pills |
| MeshCollider | Custom mesh | Slow | Complex terrain, detailed objects |
| TerrainCollider | Terrain | Moderate | Unity Terrain |

### Collider Properties

```csharp
public class ColliderSetup : MonoBehaviour
{
    void Start()
    {
        BoxCollider boxCollider = GetComponent<BoxCollider>();
        
        // Trigger colliders don't physically collide
        boxCollider.isTrigger = false;
        
        // Physics material for friction/bounciness
        boxCollider.material = Resources.Load<PhysicMaterial>("BouncyMaterial");
        
        // Adjust collider size/center
        boxCollider.size = new Vector3(1f, 2f, 1f);
        boxCollider.center = new Vector3(0f, 1f, 0f);
    }
}
```

### Physics Materials

Control friction and bounciness:

```
Physic Material Settings:
- Dynamic Friction: 0.6 (friction while moving)
- Static Friction: 0.6 (friction when stationary)
- Bounciness: 0.0 (0 = no bounce, 1 = perfect bounce)
- Friction Combine: Average (how friction combines with other materials)
- Bounce Combine: Average (how bounciness combines)
```

**Common Presets:**
- Ice: Dynamic 0.1, Static 0.1, Bounciness 0.0
- Rubber: Dynamic 0.8, Static 0.9, Bounciness 0.7
- Metal: Dynamic 0.4, Static 0.4, Bounciness 0.3

---

## Collision Detection

### Collision Callbacks

```csharp
public class CollisionHandler : MonoBehaviour
{
    // Called when collision starts
    void OnCollisionEnter(Collision collision)
    {
        Debug.Log("Hit: " + collision.gameObject.name);
        
        // Access collision details
        ContactPoint contact = collision.contacts[0];
        Vector3 hitPoint = contact.point;
        Vector3 hitNormal = contact.normal;
        
        // Apply damage, spawn effects, etc.
    }
    
    // Called every frame while colliding
    void OnCollisionStay(Collision collision)
    {
        // Continuous contact logic
    }
    
    // Called when collision ends
    void OnCollisionExit(Collision collision)
    {
        Debug.Log("Stopped touching: " + collision.gameObject.name);
    }
}
```

### Trigger Callbacks

```csharp
public class TriggerHandler : MonoBehaviour
{
    // Trigger enter (collider must have isTrigger = true)
    void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("Player"))
        {
            // Pickup item, activate checkpoint, etc.
        }
    }
    
    void OnTriggerStay(Collider other)
    {
        // Damage over time, speed boost zone, etc.
    }
    
    void OnTriggerExit(Collider other)
    {
        // Left zone, stop effect, etc.
    }
}
```

### Collision Matrix

Control which layers collide with each other:

1. Edit > Project Settings > Physics
2. Layer Collision Matrix
3. Uncheck boxes to disable collisions between layers

**Example Setup:**
- Player layer collides with: Ground, Enemies, Obstacles
- Player layer ignores: PlayerBullets, Pickups (use triggers)

---

## Raycasting

### Basic Raycast

```csharp
public class RaycastExamples : MonoBehaviour
{
    void Update()
    {
        // Simple raycast
        if (Physics.Raycast(transform.position, transform.forward, 10f))
        {
            Debug.Log("Hit something");
        }
        
        // Raycast with hit info
        RaycastHit hit;
        if (Physics.Raycast(transform.position, transform.forward, out hit, 10f))
        {
            Debug.Log("Hit: " + hit.collider.name);
            Debug.Log("Distance: " + hit.distance);
            Debug.Log("Point: " + hit.point);
            Debug.Log("Normal: " + hit.normal);
            
            // Spawn effect at hit point
            Instantiate(impactEffect, hit.point, Quaternion.LookRotation(hit.normal));
        }
    }
}
```

### Advanced Raycasting

```csharp
// Raycast with layer mask (only hit specific layers)
int layerMask = LayerMask.GetMask("Enemy", "Environment");
if (Physics.Raycast(origin, direction, out hit, maxDistance, layerMask))
{
    // Only hits objects on Enemy or Environment layers
}

// Raycast ignoring triggers
if (Physics.Raycast(origin, direction, out hit, maxDistance, layerMask, QueryTriggerInteraction.Ignore))
{
    // Ignores trigger colliders
}

// RaycastAll (returns all hits)
RaycastHit[] hits = Physics.RaycastAll(origin, direction, maxDistance);
foreach (RaycastHit hit in hits)
{
    // Process each hit
}

// SphereCast (thick raycast)
if (Physics.SphereCast(origin, radius, direction, out hit, maxDistance))
{
    // Useful for character ground detection
}
```

### Ground Detection

```csharp
public bool IsGrounded()
{
    float rayLength = 0.1f;
    return Physics.Raycast(transform.position, Vector3.down, rayLength);
}

// More robust ground check
public bool IsGroundedRobust()
{
    float sphereRadius = 0.3f;
    float maxDistance = 0.2f;
    Vector3 spherePosition = transform.position;
    
    return Physics.SphereCast(spherePosition, sphereRadius, Vector3.down, out RaycastHit hit, maxDistance);
}
```

---

## Character Controller

Alternative to Rigidbody for character movement (no physics simulation).

### Character Controller Setup

```csharp
public class CharacterMovement : MonoBehaviour
{
    [SerializeField] private float moveSpeed = 5f;
    [SerializeField] private float jumpHeight = 2f;
    [SerializeField] private float gravity = -9.81f;
    
    private CharacterController controller;
    private Vector3 velocity;
    
    void Awake()
    {
        controller = GetComponent<CharacterController>();
    }
    
    void Update()
    {
        // Ground check
        bool isGrounded = controller.isGrounded;
        if (isGrounded && velocity.y < 0)
        {
            velocity.y = -2f; // Small downward force
        }
        
        // Movement input
        float x = Input.GetAxis("Horizontal");
        float z = Input.GetAxis("Vertical");
        
        Vector3 move = transform.right * x + transform.forward * z;
        controller.Move(move * moveSpeed * Time.deltaTime);
        
        // Jump
        if (Input.GetButtonDown("Jump") && isGrounded)
        {
            velocity.y = Mathf.Sqrt(jumpHeight * -2f * gravity);
        }
        
        // Apply gravity
        velocity.y += gravity * Time.deltaTime;
        controller.Move(velocity * Time.deltaTime);
    }
}
```

### Character Controller vs. Rigidbody

| Feature | Character Controller | Rigidbody |
|---------|---------------------|------------|
| Physics simulation | No | Yes |
| Performance | Faster | Slower |
| Collision response | Manual | Automatic |
| Slopes | Built-in handling | Requires scripting |
| Use case | Player characters | Physics objects, vehicles |

---

## Animation System

### Animator Controller

State machine for managing animations.

**Components:**
1. **States:** Nodes representing animation clips
2. **Transitions:** Arrows connecting states with conditions
3. **Parameters:** Variables controlling transitions (bool, float, int, trigger)
4. **Layers:** Multiple animation layers (base, upper body, etc.)
5. **Blend Trees:** Smooth blending between animations

### Setting Up Animator

```csharp
public class PlayerAnimator : MonoBehaviour
{
    private Animator animator;
    
    void Awake()
    {
        animator = GetComponent<Animator>();
    }
    
    void Update()
    {
        // Set parameters
        float speed = Input.GetAxis("Vertical");
        animator.SetFloat("Speed", speed);
        
        // Trigger one-shot animations
        if (Input.GetButtonDown("Jump"))
        {
            animator.SetTrigger("Jump");
        }
        
        // Boolean parameters
        bool isGrounded = CheckGrounded();
        animator.SetBool("IsGrounded", isGrounded);
        
        // Integer parameters
        int weaponType = GetCurrentWeapon();
        animator.SetInteger("WeaponType", weaponType);
    }
}
```

### Blend Trees

Smooth blending between multiple animations based on parameters.

**1D Blend Tree (Speed):**
- Idle (speed = 0)
- Walk (speed = 0.5)
- Run (speed = 1.0)

**2D Blend Tree (Directional Movement):**
- Parameters: MoveX, MoveY
- Animations: WalkForward, WalkBack, StrafeLeft, StrafeRight

### Animation Events

Trigger code at specific animation frames.

**Setup:**
1. Open Animation window
2. Select animation clip
3. Add Event marker at desired frame
4. Assign function name

```csharp
public class AnimationEventHandler : MonoBehaviour
{
    // Called by animation event
    public void OnFootstep()
    {
        // Play footstep sound
        AudioSource.PlayClipAtPoint(footstepSound, transform.position);
    }
    
    public void OnAttackHit()
    {
        // Deal damage to enemies in range
        Collider[] hits = Physics.OverlapSphere(attackPoint.position, attackRadius);
        foreach (Collider hit in hits)
        {
            if (hit.CompareTag("Enemy"))
            {
                hit.GetComponent<Health>().TakeDamage(attackDamage);
            }
        }
    }
}
```

### Root Motion

Animation drives character movement instead of script.

**Enable:**
1. Animator component > Apply Root Motion = true
2. Animation clip must have root motion data

**Use Cases:**
- Cinematic character movement
- Attack lunges
- Dodge rolls

**Script Control:**
```csharp
void OnAnimatorMove()
{
    // Custom root motion handling
    Vector3 movement = animator.deltaPosition;
    controller.Move(movement);
}
```

### Inverse Kinematics (IK)

Procedurally adjust limb positions (foot placement, hand reaching).

```csharp
public class IKControl : MonoBehaviour
{
    private Animator animator;
    [SerializeField] private Transform rightHandTarget;
    
    void Awake()
    {
        animator = GetComponent<Animator>();
    }
    
    void OnAnimatorIK(int layerIndex)
    {
        if (rightHandTarget != null)
        {
            // Set right hand position and rotation
            animator.SetIKPositionWeight(AvatarIKGoal.RightHand, 1f);
            animator.SetIKRotationWeight(AvatarIKGoal.RightHand, 1f);
            animator.SetIKPosition(AvatarIKGoal.RightHand, rightHandTarget.position);
            animator.SetIKRotation(AvatarIKGoal.RightHand, rightHandTarget.rotation);
        }
    }
}
```

---

## Physics Best Practices

### Do:
- Use FixedUpdate() for physics calculations
- Cache Rigidbody references in Awake()
- Use appropriate collision detection modes
- Leverage layer collision matrix
- Use triggers for non-physical interactions
- Apply forces instead of directly setting velocity

### Don't:
- Mix 3D and 2D physics components
- Use MeshColliders for moving objects (expensive)
- Call physics methods in Update() (use FixedUpdate())
- Ignore Time.fixedDeltaTime for physics calculations
- Create too many Rigidbodies (performance cost)

### Animation Best Practices

### Do:
- Use Blend Trees for smooth transitions
- Leverage Animation Events for precise timing
- Organize Animator with layers and sub-state machines
- Cache Animator references
- Use Animator parameters efficiently

### Don't:
- Create overly complex Animator Controllers
- Use string names for parameters (use Animator.StringToHash)
- Forget to set transition conditions
- Ignore animation compression settings
- Overuse root motion (can conflict with gameplay code)

This guide covers the essential physics and animation systems in Unity. Experiment with these concepts to create responsive, realistic game mechanics.