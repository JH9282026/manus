# Unity Advanced Topics

Exploration of advanced Unity features and techniques for experienced developers.

---

## Data-Oriented Technology Stack (DOTS)

Unity's high-performance multithreaded framework for massive-scale simulations.

### DOTS Components

**1. Entity Component System (ECS)**
- Entities: Lightweight IDs (not GameObjects)
- Components: Pure data (no behavior)
- Systems: Logic that processes components

**2. C# Job System**
- Multithreaded code execution
- Safe parallel processing
- Automatic dependency management

**3. Burst Compiler**
- Compiles C# to highly optimized native code
- SIMD (Single Instruction Multiple Data) support
- Significant performance gains

### When to Use DOTS

**Good For:**
- Massive entity counts (10,000+)
- CPU-intensive simulations
- Physics-heavy games
- Strategy games with many units
- Particle systems

**Not Good For:**
- Small-scale games
- Rapid prototyping
- Projects requiring frequent GameObject access
- Teams unfamiliar with data-oriented design

### ECS Example

```csharp
using Unity.Entities;
using Unity.Transforms;
using Unity.Mathematics;

// Component (pure data)
public struct MoveSpeed : IComponentData
{
    public float Value;
}

// System (logic)
public partial class MovementSystem : SystemBase
{
    protected override void OnUpdate()
    {
        float deltaTime = Time.DeltaTime;
        
        Entities.ForEach((ref Translation translation, in MoveSpeed speed) =>
        {
            translation.Value.y += speed.Value * deltaTime;
        }).ScheduleParallel();
    }
}

// Entity creation
EntityManager entityManager = World.DefaultGameObjectInjectionWorld.EntityManager;
Entity entity = entityManager.CreateEntity();
entityManager.AddComponentData(entity, new MoveSpeed { Value = 5f });
entityManager.AddComponentData(entity, new Translation { Value = float3.zero });
```

### C# Job System

```csharp
using Unity.Jobs;
using Unity.Collections;

public struct MyJob : IJob
{
    public NativeArray<float> result;
    public float a;
    public float b;
    
    public void Execute()
    {
        result[0] = a + b;
    }
}

// Usage
NativeArray<float> result = new NativeArray<float>(1, Allocator.TempJob);
MyJob job = new MyJob
{
    result = result,
    a = 10,
    b = 20
};

JobHandle handle = job.Schedule();
handle.Complete();

Debug.Log(result[0]); // 30
result.Dispose();
```

### Burst Compiler

```csharp
using Unity.Burst;
using Unity.Jobs;

[BurstCompile]
public struct BurstJob : IJob
{
    public NativeArray<float> data;
    
    public void Execute()
    {
        for (int i = 0; i < data.Length; i++)
        {
            data[i] = math.sqrt(data[i]);
        }
    }
}
```

**Performance Gains:**
- 10-100x faster than standard C#
- Automatic SIMD vectorization
- Optimized math operations

---

## Custom Shaders

### Shader Graph (Visual Shader Editor)

**Advantages:**
- No code required
- Real-time preview
- Node-based workflow
- URP/HDRP compatible

**Use Cases:**
- Custom materials
- Stylized effects
- Procedural textures
- Animated shaders

**Common Nodes:**
- **Sample Texture 2D:** Read texture data
- **Time:** Animated effects
- **Normal Vector:** Lighting calculations
- **Lerp:** Blend between values
- **Multiply/Add:** Math operations

**Example: Dissolve Effect**
1. Sample main texture
2. Sample noise texture
3. Compare noise with dissolve threshold
4. Clip pixels below threshold
5. Add edge color near threshold

### HLSL Shader Code

For maximum control, write shaders in HLSL (High-Level Shading Language).

**Basic Unlit Shader:**
```hlsl
Shader "Custom/BasicUnlit"
{
    Properties
    {
        _MainTex ("Texture", 2D) = "white" {}
        _Color ("Color", Color) = (1,1,1,1)
    }
    
    SubShader
    {
        Tags { "RenderType"="Opaque" }
        
        Pass
        {
            CGPROGRAM
            #pragma vertex vert
            #pragma fragment frag
            #include "UnityCG.cginc"
            
            struct appdata
            {
                float4 vertex : POSITION;
                float2 uv : TEXCOORD0;
            };
            
            struct v2f
            {
                float2 uv : TEXCOORD0;
                float4 vertex : SV_POSITION;
            };
            
            sampler2D _MainTex;
            float4 _MainTex_ST;
            float4 _Color;
            
            v2f vert (appdata v)
            {
                v2f o;
                o.vertex = UnityObjectToClipPos(v.vertex);
                o.uv = TRANSFORM_TEX(v.uv, _MainTex);
                return o;
            }
            
            fixed4 frag (v2f i) : SV_Target
            {
                fixed4 col = tex2D(_MainTex, i.uv) * _Color;
                return col;
            }
            ENDCG
        }
    }
}
```

**Vertex Displacement:**
```hlsl
v2f vert (appdata v)
{
    v2f o;
    
    // Displace vertices based on sine wave
    float displacement = sin(v.vertex.y + _Time.y) * 0.1;
    v.vertex.xyz += v.normal * displacement;
    
    o.vertex = UnityObjectToClipPos(v.vertex);
    o.uv = TRANSFORM_TEX(v.uv, _MainTex);
    return o;
}
```

### Shader Optimization

**Mobile Optimization:**
- Minimize texture samples
- Avoid complex math in fragment shader
- Use lower precision (half, fixed)
- Reduce shader variants

**Desktop Optimization:**
- Batch similar materials
- Use GPU instancing
- Minimize state changes

---

## Advanced Multiplayer

### Netcode for GameObjects (NGO)

Unity's official multiplayer framework.

**Architecture:**
- Client-Server model
- Authoritative server
- Client prediction and reconciliation

**Core Concepts:**

**1. NetworkManager:**
```csharp
using Unity.Netcode;

public class GameNetworkManager : MonoBehaviour
{
    void Start()
    {
        NetworkManager.Singleton.OnServerStarted += OnServerStarted;
        NetworkManager.Singleton.OnClientConnectedCallback += OnClientConnected;
    }
    
    public void StartHost()
    {
        NetworkManager.Singleton.StartHost();
    }
    
    public void StartClient()
    {
        NetworkManager.Singleton.StartClient();
    }
    
    void OnServerStarted()
    {
        Debug.Log("Server started");
    }
    
    void OnClientConnected(ulong clientId)
    {
        Debug.Log($"Client {clientId} connected");
    }
}
```

**2. NetworkObject:**
```csharp
public class Player : NetworkBehaviour
{
    private NetworkVariable<int> health = new NetworkVariable<int>(100);
    
    public override void OnNetworkSpawn()
    {
        if (IsOwner)
        {
            // Only owner executes this
        }
        
        if (IsServer)
        {
            // Only server executes this
        }
    }
    
    void Update()
    {
        if (!IsOwner) return;
        
        // Only owner can control
        float move = Input.GetAxis("Vertical");
        transform.Translate(Vector3.forward * move * Time.deltaTime);
    }
}
```

**3. NetworkVariable:**
```csharp
private NetworkVariable<int> score = new NetworkVariable<int>(
    0,
    NetworkVariableReadPermission.Everyone,
    NetworkVariableWritePermission.Server
);

void Start()
{
    score.OnValueChanged += OnScoreChanged;
}

void OnScoreChanged(int oldValue, int newValue)
{
    Debug.Log($"Score changed from {oldValue} to {newValue}");
}

[ServerRpc]
void AddScoreServerRpc(int points)
{
    score.Value += points;
}
```

**4. RPC (Remote Procedure Calls):**
```csharp
// Client calls, server executes
[ServerRpc]
void ShootServerRpc(Vector3 direction)
{
    // Server-authoritative shooting
    SpawnBullet(direction);
}

// Server calls, clients execute
[ClientRpc]
void PlaySoundClientRpc()
{
    AudioSource.PlayClipAtPoint(shootSound, transform.position);
}

// Usage
if (Input.GetButtonDown("Fire"))
{
    ShootServerRpc(transform.forward);
}
```

### Dedicated Server

**Headless Build:**
```
Build Settings:
- Server Build: Enabled
- Headless Mode: Enabled (no graphics)
```

**Server Hosting:**
- Self-hosted (VPS, dedicated server)
- Cloud hosting (AWS, Google Cloud, Azure)
- Game server hosting (Multiplay, PlayFab)

**Matchmaking:**
- Unity Matchmaker
- Custom matchmaking service
- Third-party solutions (PlayFab, Photon)

---

## Procedural Generation

### Perlin Noise

```csharp
public class TerrainGenerator : MonoBehaviour
{
    public int width = 256;
    public int height = 256;
    public float scale = 20f;
    
    void Start()
    {
        Terrain terrain = GetComponent<Terrain>();
        terrain.terrainData = GenerateTerrain(terrain.terrainData);
    }
    
    TerrainData GenerateTerrain(TerrainData terrainData)
    {
        terrainData.heightmapResolution = width + 1;
        terrainData.size = new Vector3(width, 50, height);
        terrainData.SetHeights(0, 0, GenerateHeights());
        return terrainData;
    }
    
    float[,] GenerateHeights()
    {
        float[,] heights = new float[width, height];
        
        for (int x = 0; x < width; x++)
        {
            for (int y = 0; y < height; y++)
            {
                heights[x, y] = CalculateHeight(x, y);
            }
        }
        
        return heights;
    }
    
    float CalculateHeight(int x, int y)
    {
        float xCoord = (float)x / width * scale;
        float yCoord = (float)y / height * scale;
        
        return Mathf.PerlinNoise(xCoord, yCoord);
    }
}
```

### Dungeon Generation

```csharp
public class DungeonGenerator : MonoBehaviour
{
    public int roomCount = 10;
    public Vector2Int roomSizeMin = new Vector2Int(5, 5);
    public Vector2Int roomSizeMax = new Vector2Int(10, 10);
    
    private List<Room> rooms = new List<Room>();
    
    void Start()
    {
        GenerateDungeon();
    }
    
    void GenerateDungeon()
    {
        for (int i = 0; i < roomCount; i++)
        {
            int width = Random.Range(roomSizeMin.x, roomSizeMax.x);
            int height = Random.Range(roomSizeMin.y, roomSizeMax.y);
            int x = Random.Range(0, 100);
            int y = Random.Range(0, 100);
            
            Room newRoom = new Room(x, y, width, height);
            
            bool overlaps = false;
            foreach (Room room in rooms)
            {
                if (newRoom.Intersects(room))
                {
                    overlaps = true;
                    break;
                }
            }
            
            if (!overlaps)
            {
                rooms.Add(newRoom);
                CreateRoom(newRoom);
                
                if (rooms.Count > 1)
                {
                    ConnectRooms(rooms[rooms.Count - 2], newRoom);
                }
            }
        }
    }
    
    void CreateRoom(Room room)
    {
        // Instantiate floor tiles, walls, etc.
    }
    
    void ConnectRooms(Room roomA, Room roomB)
    {
        // Create corridor between rooms
    }
}

public class Room
{
    public int x, y, width, height;
    
    public Room(int x, int y, int width, int height)
    {
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
    }
    
    public bool Intersects(Room other)
    {
        return x < other.x + other.width &&
               x + width > other.x &&
               y < other.y + other.height &&
               y + height > other.y;
    }
}
```

---

## AI and Pathfinding

### NavMesh (Navigation Mesh)

**Setup:**
1. Window > AI > Navigation
2. Select walkable objects
3. Mark as "Navigation Static"
4. Bake NavMesh

**NavMeshAgent:**
```csharp
using UnityEngine.AI;

public class EnemyAI : MonoBehaviour
{
    private NavMeshAgent agent;
    private Transform player;
    
    void Start()
    {
        agent = GetComponent<NavMeshAgent>();
        player = GameObject.FindGameObjectWithTag("Player").transform;
    }
    
    void Update()
    {
        agent.SetDestination(player.position);
        
        // Check if reached destination
        if (!agent.pathPending && agent.remainingDistance < 0.5f)
        {
            // Attack player
        }
    }
}
```

**Dynamic Obstacles:**
```csharp
public class DynamicObstacle : MonoBehaviour
{
    void Start()
    {
        NavMeshObstacle obstacle = gameObject.AddComponent<NavMeshObstacle>();
        obstacle.carving = true;
        obstacle.shape = NavMeshObstacleShape.Box;
    }
}
```

### Behavior Trees

Hierarchical AI decision-making structure.

**Node Types:**
- **Selector:** Executes children until one succeeds
- **Sequence:** Executes children until one fails
- **Action:** Performs specific task
- **Condition:** Checks state

**Example (Pseudo-code):**
```
Selector
├── Sequence (Attack)
│   ├── Condition: Player in range
│   └── Action: Attack player
├── Sequence (Chase)
│   ├── Condition: Player visible
│   └── Action: Move to player
└── Action: Patrol
```

---

## Third-Party SDK Integration

### Common SDKs

**Analytics:**
- Unity Analytics
- Google Analytics for Games
- GameAnalytics

**Monetization:**
- Unity Ads
- AdMob (Google)
- IronSource

**Social:**
- Facebook SDK
- Google Play Games Services
- Game Center (iOS)

**Backend:**
- Firebase
- PlayFab
- Photon

### Integration Example: Firebase

```csharp
using Firebase;
using Firebase.Analytics;

public class FirebaseManager : MonoBehaviour
{
    void Start()
    {
        FirebaseApp.CheckAndFixDependenciesAsync().ContinueWith(task =>
        {
            if (task.Result == DependencyStatus.Available)
            {
                FirebaseAnalytics.SetAnalyticsCollectionEnabled(true);
                Debug.Log("Firebase initialized");
            }
        });
    }
    
    public void LogEvent(string eventName)
    {
        FirebaseAnalytics.LogEvent(eventName);
    }
}
```

---

## Performance Profiling

### Deep Profiling

Enable in Profiler window for detailed call stacks.

**Warning:** Significant performance overhead, use sparingly.

### Memory Profiler

Package Manager > Memory Profiler

**Features:**
- Snapshot comparison
- Memory leak detection
- Object reference tracking
- Texture memory usage

### Frame Debugger

Window > Analysis > Frame Debugger

**Use Cases:**
- Identify redundant draw calls
- Visualize rendering order
- Debug shader issues
- Optimize batching

Advanced Unity development requires deep understanding of engine internals, performance optimization, and specialized systems. Experiment with these topics to push Unity's capabilities to the limit.