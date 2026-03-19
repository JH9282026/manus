# 5G Fundamentals

Core concepts, architecture, and capabilities of 5G wireless technology.

---

## What is 5G?

5G (fifth generation) is the latest standard for cellular networks, offering significant improvements over 4G/LTE in speed, latency, capacity, and reliability. Unlike previous generations that primarily focused on faster data speeds, 5G introduces fundamentally new capabilities that enable entirely new classes of applications.

### Evolution from 4G to 5G

**4G/LTE capabilities:**
- Download speeds: 100 Mbps - 1 Gbps
- Latency: 30-50ms
- Device density: ~100,000 devices per km²
- Primary use case: Mobile broadband

**5G improvements:**
- Download speeds: 1-10+ Gbps (10-100x faster)
- Latency: 1-10ms (5-10x lower)
- Device density: 1,000,000 devices per km² (10x more)
- Multiple use cases: Mobile broadband, IoT, mission-critical applications

### Key Differentiators

**Not just faster, but fundamentally different:**
- **Network slicing**: Create virtual networks optimized for specific use cases
- **Edge computing**: Process data at network edge for ultra-low latency
- **Massive connectivity**: Support millions of devices per square kilometer
- **Ultra-reliability**: 99.999% availability for critical applications
- **Precise positioning**: Sub-meter location accuracy

---

## 5G Architecture

### Network Components

**Radio Access Network (RAN):**
- **gNodeB (gNB)**: 5G base station, replaces 4G eNodeB
- **Massive MIMO**: Multiple antennas for beamforming and capacity
- **Beamforming**: Directional signal transmission for efficiency
- **Carrier aggregation**: Combine multiple frequency bands

**Core Network (5G Core / 5GC):**
- **Service-based architecture (SBA)**: Microservices-based design
- **Network functions**: AMF (access management), SMF (session management), UPF (user plane)
- **Network slicing**: Logical separation of network resources
- **Control and user plane separation (CUPS)**: Independent scaling

**Multi-Access Edge Computing (MEC):**
- Compute and storage at network edge
- Ultra-low latency processing (<5ms)
- Local data processing and caching
- Integration with RAN and core network

### Network Slicing

**Concept:**
- Create multiple virtual networks on shared physical infrastructure
- Each slice optimized for specific use case
- Guaranteed resources and QoS per slice
- Isolation between slices for security and performance

**Slice types:**

**eMBB slice (Enhanced Mobile Broadband):**
- High bandwidth, moderate latency
- Use cases: Video streaming, AR/VR, cloud gaming
- Characteristics: 1-10 Gbps, 10-20ms latency

**URLLC slice (Ultra-Reliable Low-Latency Communication):**
- Ultra-low latency, high reliability
- Use cases: Autonomous vehicles, industrial automation, remote surgery
- Characteristics: 1-10ms latency, 99.999% reliability

**mMTC slice (Massive Machine-Type Communication):**
- Massive device connectivity, low power
- Use cases: Smart cities, agriculture sensors, asset tracking
- Characteristics: 1M devices/km², low data rate, long battery life

**Custom slices:**
- Enterprise-specific requirements
- Hybrid characteristics (e.g., high bandwidth + low latency)
- Dedicated resources for mission-critical applications

**Slice lifecycle:**
1. **Design**: Define slice requirements (bandwidth, latency, coverage)
2. **Instantiation**: Allocate resources and configure network functions
3. **Activation**: Make slice available to devices
4. **Operation**: Monitor performance, adjust resources
5. **Decommission**: Release resources when no longer needed

---

## 5G Spectrum Bands

### Low-Band (Sub-1 GHz)

**Frequencies:**
- 600-900 MHz
- Similar to 4G LTE bands

**Characteristics:**
- **Coverage**: Excellent (several kilometers per cell)
- **Penetration**: Good indoor penetration
- **Speed**: 50-250 Mbps (similar to 4G)
- **Latency**: 20-30ms

**Use cases:**
- Wide-area coverage (rural, suburban)
- IoT deployments
- Basic mobile broadband

**Deployment:**
- Reuse existing 4G infrastructure
- Cost-effective for carriers
- Foundation for nationwide 5G coverage

### Mid-Band (1-6 GHz)

**Frequencies:**
- 2.5-3.7 GHz (most common)
- C-band (3.7-4.2 GHz) in US

**Characteristics:**
- **Coverage**: Good (hundreds of meters per cell)
- **Penetration**: Moderate indoor penetration
- **Speed**: 100 Mbps - 1 Gbps
- **Latency**: 10-20ms

**Use cases:**
- Urban and suburban coverage
- General 5G services
- Balance of coverage and capacity

**Deployment:**
- Sweet spot for most 5G deployments
- Good balance of coverage and performance
- Primary band for most carriers globally

### High-Band / mmWave (24-100 GHz)

**Frequencies:**
- 24-29 GHz, 37-40 GHz (US)
- 26 GHz, 28 GHz (global)

**Characteristics:**
- **Coverage**: Limited (100-200 meters per cell)
- **Penetration**: Poor (blocked by walls, trees, rain)
- **Speed**: 1-10+ Gbps
- **Latency**: 1-10ms

**Use cases:**
- Dense urban areas (stadiums, airports, city centers)
- Fixed wireless access (home broadband)
- High-capacity hotspots

**Deployment:**
- Requires dense cell deployment (small cells)
- Line-of-sight or near-line-of-sight needed
- Expensive to deploy widely
- Best for high-capacity, localized areas

**Technical challenges:**
- **Propagation loss**: Signal weakens quickly with distance
- **Blockage**: Easily blocked by obstacles
- **Beam management**: Requires sophisticated beamforming
- **Device complexity**: More antennas, higher power consumption

---

## Core 5G Capabilities

### Enhanced Mobile Broadband (eMBB)

**Definition:**
- Significantly faster data speeds than 4G
- Support for bandwidth-intensive applications

**Performance targets:**
- **Peak download**: 20 Gbps (theoretical), 1-10 Gbps (real-world)
- **Peak upload**: 10 Gbps (theoretical), 500 Mbps - 1 Gbps (real-world)
- **User experience**: 100 Mbps - 1 Gbps consistently
- **Latency**: 10-20ms

**Enabling technologies:**
- **Massive MIMO**: 64-256 antennas for increased capacity
- **Carrier aggregation**: Combine multiple frequency bands
- **Higher-order modulation**: 256-QAM, 1024-QAM for more bits per symbol
- **Wider channels**: Up to 100 MHz in mid-band, 400 MHz in mmWave

**Use cases:**
- 4K/8K video streaming
- Cloud gaming
- AR/VR applications
- High-speed mobile broadband
- Fixed wireless access (home internet)

### Ultra-Reliable Low-Latency Communication (URLLC)

**Definition:**
- Mission-critical applications requiring high reliability and low latency
- Guaranteed performance for safety-critical use cases

**Performance targets:**
- **Latency**: 1-10ms (end-to-end)
- **Reliability**: 99.999% (five nines)
- **Availability**: 99.999%
- **Packet loss**: <0.001%

**Enabling technologies:**
- **Mini-slots**: Shorter transmission intervals for lower latency
- **Grant-free transmission**: Reduce scheduling delay
- **Redundant transmission**: Multiple paths for reliability
- **Edge computing**: Process data locally to minimize latency

**Use cases:**
- **Autonomous vehicles**: V2V, V2I communication for collision avoidance
- **Industrial automation**: Real-time control of robots and machinery
- **Remote surgery**: Haptic feedback for robotic surgery
- **Smart grid**: Real-time monitoring and control
- **Public safety**: Emergency services communication

**Latency breakdown:**
- **Radio access**: 1-5ms
- **Core network**: 1-3ms
- **Edge processing**: 1-2ms
- **Application**: Variable
- **Total**: 5-10ms (target <10ms)

### Massive Machine-Type Communication (mMTC)

**Definition:**
- Support for massive numbers of IoT devices
- Optimized for low-power, low-data-rate devices

**Performance targets:**
- **Device density**: 1,000,000 devices per km²
- **Battery life**: 10+ years on single battery
- **Data rate**: 1-100 kbps per device
- **Latency**: Seconds to minutes (not time-critical)

**Enabling technologies:**
- **NB-IoT** (Narrowband IoT): Low-power, wide-area connectivity
- **LTE-M**: Enhanced machine-type communication
- **Grant-free access**: Reduce signaling overhead
- **Power-saving modes**: Extended discontinuous reception (eDRX), power-saving mode (PSM)

**Use cases:**
- **Smart cities**: Streetlights, parking sensors, waste management
- **Agriculture**: Soil sensors, livestock tracking, irrigation control
- **Utilities**: Smart meters, grid monitoring
- **Logistics**: Asset tracking, fleet management
- **Environmental monitoring**: Air quality, water quality, weather

**Device characteristics:**
- Low cost (<$5 per module target)
- Low power consumption (10+ year battery life)
- Simple functionality (sensors, actuators)
- Infrequent communication (hourly, daily)

---

## Multi-Access Edge Computing (MEC)

### MEC Architecture

**Concept:**
- Bring compute and storage to network edge
- Process data close to users and devices
- Reduce latency and backhaul traffic

**Deployment locations:**
- **Far edge**: At or near base stations (gNodeB)
- **Near edge**: At aggregation points (regional data centers)
- **Cloud**: Centralized data centers (for comparison)

**Latency comparison:**
- **Cloud**: 50-100ms
- **Near edge**: 10-20ms
- **Far edge**: 1-5ms
- **Device**: 0ms (local processing)

### MEC Use Cases

**Real-time analytics:**
- Video analytics (object detection, tracking)
- Anomaly detection in sensor data
- Predictive maintenance

**Content delivery:**
- Video streaming (cache popular content)
- Gaming (reduce latency)
- AR/VR (offload rendering)

**IoT data processing:**
- Aggregate and filter sensor data
- Local decision making
- Reduce cloud traffic and cost

**Location-based services:**
- Indoor navigation
- Proximity marketing
- Asset tracking

### MEC Benefits

**Ultra-low latency:**
- Process data locally (<5ms)
- Critical for real-time applications
- Enable new use cases (autonomous vehicles, industrial control)

**Reduced backhaul:**
- Process data at edge, send only results to cloud
- Reduce network congestion
- Lower bandwidth costs

**Privacy and compliance:**
- Keep sensitive data local
- Meet data residency requirements
- Reduce exposure to network threats

**Context awareness:**
- Access to network information (location, QoS)
- Optimize based on local conditions
- Personalize user experience

---

## 5G vs. Other Technologies

### 5G vs. 4G/LTE

| Feature | 4G/LTE | 5G |
|---------|--------|----|
| Peak download speed | 1 Gbps | 10+ Gbps |
| Typical speed | 10-50 Mbps | 100 Mbps - 1 Gbps |
| Latency | 30-50ms | 1-10ms |
| Device density | 100,000/km² | 1,000,000/km² |
| Reliability | 99.9% | 99.999% |
| Network slicing | No | Yes |
| Edge computing | Limited | Native support |
| Primary use case | Mobile broadband | Broadband + IoT + Critical apps |

### 5G vs. Wi-Fi 6/6E

| Feature | Wi-Fi 6/6E | 5G |
|---------|------------|----|
| Coverage | 50-100m indoor | Kilometers (outdoor) |
| Mobility | Limited (handoff issues) | Seamless (designed for mobility) |
| Deployment | Unlicensed spectrum | Licensed spectrum |
| QoS guarantees | Best-effort | Guaranteed (network slicing) |
| Device density | ~200 devices | 1,000,000/km² |
| Latency | 10-20ms | 1-10ms |
| Security | WPA3 | 3GPP security (SIM-based) |
| Use case | Indoor, fixed | Indoor + outdoor, mobile |

**When to use Wi-Fi 6:**
- Indoor coverage (office, home, campus)
- Fixed devices
- Lower cost (unlicensed spectrum)
- Existing Wi-Fi infrastructure

**When to use 5G:**
- Wide-area coverage
- Mobile devices
- Guaranteed QoS needed
- Mission-critical applications

### 5G vs. LoRaWAN/Sigfox (LPWAN)

| Feature | LoRaWAN/Sigfox | 5G (mMTC) |
|---------|----------------|----------|
| Range | 2-15 km | 1-10 km (NB-IoT) |
| Data rate | 0.3-50 kbps | 1-100 kbps |
| Latency | Seconds | Seconds (mMTC), ms (URLLC) |
| Battery life | 10+ years | 10+ years |
| Deployment | Private or public | Carrier network |
| Cost | Low | Moderate |
| Mobility | Limited | Full support |
| Ecosystem | Smaller | Large (cellular) |

**When to use LPWAN:**
- Very long range needed
- Extremely low cost
- Private network control
- Simple use cases (sensors)

**When to use 5G mMTC:**
- Need for mobility
- Integration with other 5G services
- Carrier-managed network
- Larger ecosystem and support

---

## 5G Standards and Releases

### 3GPP Releases

**Release 15 (2018):**
- First 5G standard
- Non-standalone (NSA) mode (uses 4G core)
- Standalone (SA) mode (5G core)
- eMBB focus

**Release 16 (2020):**
- URLLC enhancements
- Industrial IoT features
- V2X (vehicle-to-everything) communication
- Positioning improvements
- Integrated access and backhaul (IAB)

**Release 17 (2022):**
- Further URLLC improvements
- NR-Light (reduced capability devices)
- Sidelink enhancements (device-to-device)
- Satellite integration
- Extended reality (XR) optimizations

**Release 18 (2024):**
- 5G-Advanced (evolution toward 6G)
- AI/ML integration
- Ambient IoT (ultra-low-power devices)
- Immersive communication
- Network energy efficiency

### Deployment Modes

**Non-Standalone (NSA):**
- 5G radio (gNodeB) with 4G core (EPC)
- Faster deployment (reuse 4G infrastructure)
- Limited 5G features (no network slicing)
- Dual connectivity (4G + 5G)

**Standalone (SA):**
- 5G radio (gNodeB) with 5G core (5GC)
- Full 5G features (network slicing, edge computing)
- Independent of 4G
- Required for URLLC and advanced features

**Migration path:**
1. 4G LTE (existing)
2. 5G NSA (quick 5G deployment)
3. 5G SA (full 5G capabilities)
4. 5G-Advanced (Release 18+)

---

## 5G Security

### Security Enhancements over 4G

**Stronger encryption:**
- 256-bit encryption (vs. 128-bit in 4G)
- Improved key derivation
- Protection against eavesdropping

**Enhanced authentication:**
- Mutual authentication (network and device)
- Protection against fake base stations
- Subscriber privacy (encrypted IMSI)

**Network slicing security:**
- Isolation between slices
- Slice-specific security policies
- Prevent cross-slice attacks

**Edge security:**
- Secure MEC platform
- Application isolation
- Encrypted communication

### Security Challenges

**Expanded attack surface:**
- More devices (IoT)
- More network functions (virtualized)
- More interfaces (APIs)

**Supply chain security:**
- Equipment from multiple vendors
- Software-defined networking
- Need for trusted components

**Privacy concerns:**
- Location tracking
- Data collection from IoT devices
- Network analytics and monitoring

### Security Best Practices

**Device security:**
- Secure boot and attestation
- Regular firmware updates
- Strong authentication (SIM, eSIM)
- Encryption of data at rest and in transit

**Network security:**
- Network slicing for isolation
- Firewalls and intrusion detection
- DDoS protection
- Regular security audits

**Application security:**
- End-to-end encryption
- Secure APIs
- Access control and authorization
- Security testing and validation
