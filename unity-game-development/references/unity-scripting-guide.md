# Unity C# Scripting Guide

Comprehensive reference for Unity scripting patterns, best practices, and common implementations.

---

## C# Fundamentals for Unity

### MonoBehaviour Lifecycle

Unity scripts inherit from MonoBehaviour, which provides lifecycle methods called by the engine:

```csharp
public class GameController : MonoBehaviour
{
    // Called when script instance is loaded (before Start)
    void Awake()
    {
        // Initialize references to other components
        // Happens even if script is disabled
    }

    // Called on first frame when script is enabled
    void Start()
    {
        // Initialization that depends on other objects
        // Only called if script is enabled
    }

    // Called every frame
    void Update()
    {
        // Input handling
        // Non-physics game logic
        // Frame-dependent updates
    }

    // Called at fixed time intervals (default 0.02s)
    void FixedUpdate()
    {
        // Physics calculations
        // Rigidbody manipulation
    }

    // Called after all Update methods
    void LateUpdate()
    {
        // Camera following
        // Final position adjustments
    }

    // Called when object is destroyed
    void OnDestroy()
    {
        // Cleanup
        // Unsubscribe from events
    }
}
```

### Component Access Patterns

**Caching Components (Recommended)**

```csharp
public class Player : MonoBehaviour
{
    private Rigidbody rb;
    private Animator animator;
    
    void Awake()
    {
        // Cache once in Awake
        rb = GetComponent<Rigidbody>();
        animator = GetComponent<Animator>();
    }
    
    void Update()
    {
        // Use cached references (fast)
        rb.AddForce(Vector3.forward);
    }
}
```

**Finding Objects (Avoid in Update)**

```csharp
// SLOW - Never do this in Update()
void Update()
{
    GameObject player = GameObject.Find("Player"); // Bad!
}

// BETTER - Do once in Start()
private GameObject player;
void Start()
{
    player = GameObject.FindGameObjectWithTag("Player");
}

// BEST - Assign in Inspector or use dependency injection
[SerializeField] private GameObject player;
```

---

## Common Gameplay Patterns

### Player Movement (Character Controller)

```csharp
public class PlayerMovement : MonoBehaviour
{
    [SerializeField] private float moveSpeed = 5f;
    [SerializeField] private float jumpForce = 5f;
    [SerializeField] private float gravity = -9.81f;
    
    private CharacterController controller;
    private Vector3 velocity;
    private bool isGrounded;
    
    void Awake()
    {
        controller = GetComponent<CharacterController>();
    }
    
    void Update()
    {
        // Ground check
        isGrounded = controller.isGrounded;
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
            velocity.y = Mathf.Sqrt(jumpForce * -2f * gravity);
        }
        
        // Apply gravity
        velocity.y += gravity * Time.deltaTime;
        controller.Move(velocity * Time.deltaTime);
    }
}
```

### Camera Follow System

```csharp
public class CameraFollow : MonoBehaviour
{
    [SerializeField] private Transform target;
    [SerializeField] private Vector3 offset = new Vector3(0, 5, -10);
    [SerializeField] private float smoothSpeed = 0.125f;
    
    void LateUpdate() // Use LateUpdate for camera
    {
        if (target == null) return;
        
        Vector3 desiredPosition = target.position + offset;
        Vector3 smoothedPosition = Vector3.Lerp(transform.position, desiredPosition, smoothSpeed);
        transform.position = smoothedPosition;
        
        transform.LookAt(target);
    }
}
```

### Health System

```csharp
public class Health : MonoBehaviour
{
    [SerializeField] private float maxHealth = 100f;
    private float currentHealth;
    
    public event Action OnDeath;
    public event Action<float> OnHealthChanged;
    
    void Start()
    {
        currentHealth = maxHealth;
    }
    
    public void TakeDamage(float damage)
    {
        currentHealth -= damage;
        currentHealth = Mathf.Clamp(currentHealth, 0, maxHealth);
        
        OnHealthChanged?.Invoke(currentHealth / maxHealth);
        
        if (currentHealth <= 0)
        {
            Die();
        }
    }
    
    public void Heal(float amount)
    {
        currentHealth += amount;
        currentHealth = Mathf.Clamp(currentHealth, 0, maxHealth);
        OnHealthChanged?.Invoke(currentHealth / maxHealth);
    }
    
    private void Die()
    {
        OnDeath?.Invoke();
        // Handle death logic
    }
}
```

### Object Pooling

```csharp
public class ObjectPool : MonoBehaviour
{
    [SerializeField] private GameObject prefab;
    [SerializeField] private int poolSize = 20;
    
    private Queue<GameObject> pool = new Queue<GameObject>();
    
    void Start()
    {
        for (int i = 0; i < poolSize; i++)
        {
            GameObject obj = Instantiate(prefab);
            obj.SetActive(false);
            pool.Enqueue(obj);
        }
    }
    
    public GameObject GetObject()
    {
        if (pool.Count > 0)
        {
            GameObject obj = pool.Dequeue();
            obj.SetActive(true);
            return obj;
        }
        else
        {
            // Pool exhausted, create new object
            return Instantiate(prefab);
        }
    }
    
    public void ReturnObject(GameObject obj)
    {
        obj.SetActive(false);
        pool.Enqueue(obj);
    }
}
```

---

## Design Patterns

### Singleton Pattern

```csharp
public class GameManager : MonoBehaviour
{
    public static GameManager Instance { get; private set; }
    
    void Awake()
    {
        if (Instance != null && Instance != this)
        {
            Destroy(gameObject);
            return;
        }
        
        Instance = this;
        DontDestroyOnLoad(gameObject);
    }
}

// Usage:
GameManager.Instance.SomeMethod();
```

### Observer Pattern (Events)

```csharp
public class ScoreManager : MonoBehaviour
{
    public static event Action<int> OnScoreChanged;
    
    private int score = 0;
    
    public void AddScore(int points)
    {
        score += points;
        OnScoreChanged?.Invoke(score);
    }
}

public class ScoreUI : MonoBehaviour
{
    void OnEnable()
    {
        ScoreManager.OnScoreChanged += UpdateScoreDisplay;
    }
    
    void OnDisable()
    {
        ScoreManager.OnScoreChanged -= UpdateScoreDisplay;
    }
    
    void UpdateScoreDisplay(int newScore)
    {
        // Update UI
    }
}
```

### State Machine Pattern

```csharp
public interface IState
{
    void Enter();
    void Update();
    void Exit();
}

public class StateMachine
{
    private IState currentState;
    
    public void ChangeState(IState newState)
    {
        currentState?.Exit();
        currentState = newState;
        currentState?.Enter();
    }
    
    public void Update()
    {
        currentState?.Update();
    }
}

public class IdleState : IState
{
    public void Enter() { /* Setup idle */ }
    public void Update() { /* Idle logic */ }
    public void Exit() { /* Cleanup */ }
}
```

---

## ScriptableObjects for Data

### Weapon Data Example

```csharp
[CreateAssetMenu(fileName = "New Weapon", menuName = "Game/Weapon")]
public class WeaponData : ScriptableObject
{
    public string weaponName;
    public int damage;
    public float fireRate;
    public int magazineSize;
    public GameObject projectilePrefab;
    public AudioClip fireSound;
}

// Usage in weapon script:
public class Weapon : MonoBehaviour
{
    [SerializeField] private WeaponData weaponData;
    
    void Fire()
    {
        // Access data from ScriptableObject
        Instantiate(weaponData.projectilePrefab, firePoint.position, firePoint.rotation);
        AudioSource.PlayClipAtPoint(weaponData.fireSound, transform.position);
    }
}
```

---

## Coroutines

### Basic Coroutine Usage

```csharp
public class CoroutineExamples : MonoBehaviour
{
    void Start()
    {
        StartCoroutine(DelayedAction());
        StartCoroutine(RepeatAction());
    }
    
    IEnumerator DelayedAction()
    {
        Debug.Log("Starting");
        yield return new WaitForSeconds(2f);
        Debug.Log("2 seconds later");
    }
    
    IEnumerator RepeatAction()
    {
        while (true)
        {
            Debug.Log("Repeating every second");
            yield return new WaitForSeconds(1f);
        }
    }
    
    // Stop coroutine
    void StopRepeating()
    {
        StopCoroutine(RepeatAction());
    }
}
```

### Fade Effect Coroutine

```csharp
IEnumerator FadeOut(CanvasGroup canvasGroup, float duration)
{
    float startAlpha = canvasGroup.alpha;
    float elapsed = 0f;
    
    while (elapsed < duration)
    {
        elapsed += Time.deltaTime;
        canvasGroup.alpha = Mathf.Lerp(startAlpha, 0f, elapsed / duration);
        yield return null; // Wait one frame
    }
    
    canvasGroup.alpha = 0f;
}
```

---

## Input Handling

### New Input System

```csharp
using UnityEngine.InputSystem;

public class PlayerInput : MonoBehaviour
{
    private PlayerInputActions inputActions;
    
    void Awake()
    {
        inputActions = new PlayerInputActions();
    }
    
    void OnEnable()
    {
        inputActions.Player.Enable();
        inputActions.Player.Jump.performed += OnJump;
    }
    
    void OnDisable()
    {
        inputActions.Player.Jump.performed -= OnJump;
        inputActions.Player.Disable();
    }
    
    void Update()
    {
        Vector2 moveInput = inputActions.Player.Move.ReadValue<Vector2>();
        // Use moveInput for movement
    }
    
    void OnJump(InputAction.CallbackContext context)
    {
        // Jump logic
    }
}
```

---

## Performance Optimization Tips

### Avoid Expensive Operations in Update

```csharp
// BAD - Expensive operations every frame
void Update()
{
    GameObject[] enemies = GameObject.FindGameObjectsWithTag("Enemy");
    string message = "Health: " + health; // String concatenation
}

// GOOD - Cache and optimize
private GameObject[] enemies;
private StringBuilder sb = new StringBuilder();

void Start()
{
    enemies = GameObject.FindGameObjectsWithTag("Enemy");
}

void Update()
{
    sb.Clear();
    sb.Append("Health: ");
    sb.Append(health);
}
```

### Use CompareTag Instead of String Comparison

```csharp
// BAD
if (other.gameObject.tag == "Player") { }

// GOOD
if (other.CompareTag("Player")) { }
```

### Minimize Garbage Collection

```csharp
// BAD - Creates garbage every frame
void Update()
{
    Vector3 direction = new Vector3(x, y, z); // Allocates memory
}

// GOOD - Reuse variables
private Vector3 direction;
void Update()
{
    direction.Set(x, y, z); // No allocation
}
```

---

## Unity-Specific C# Features

### Serialization Attributes

```csharp
public class SerializationExample : MonoBehaviour
{
    // Visible in Inspector
    [SerializeField] private int privateField;
    
    // Hidden from Inspector
    [HideInInspector] public int publicField;
    
    // Tooltip in Inspector
    [Tooltip("Speed of the player")]
    public float speed;
    
    // Range slider in Inspector
    [Range(0, 100)]
    public int health;
    
    // Header in Inspector
    [Header("Movement Settings")]
    public float jumpHeight;
}
```

### Property Drawers

```csharp
[System.Serializable]
public class MinMaxRange
{
    public float min;
    public float max;
}

public class Example : MonoBehaviour
{
    [SerializeField] private MinMaxRange damageRange;
}
```

This scripting guide covers the essential patterns and practices for Unity C# development. Refer to Unity's official documentation for API-specific details and advanced features.