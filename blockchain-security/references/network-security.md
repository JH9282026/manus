# Blockchain Network Security

Comprehensive guide to securing blockchain network infrastructure, peer-to-peer communications, and defending against network-layer attacks.

---

## Network Architecture Security

### Node Infrastructure Hardening

**Node Types and Security Profiles**:

| Node Type | Exposure Level | Security Priority | Key Threats |
|-----------|---------------|-------------------|-------------|
| **Full Node** | High | Critical | DDoS, Eclipse, Data corruption |
| **Validator Node** | Very High | Critical | All attacks, Key theft |
| **Light Client** | Medium | Moderate | Fake data, MitM |
| **Archive Node** | Medium | High | Storage attacks, DDoS |
| **RPC Node** | Very High | Critical | API abuse, DDoS, Injection |

**Full Node Security Configuration**:

```bash
# Bitcoin Core Security Hardening

# bitcoin.conf
# Network Security
rpcallowip=127.0.0.1  # Only local RPC access
rpcbind=127.0.0.1     # Bind RPC to localhost only
rpcauth=user:hash     # Strong authentication
maxconnections=125    # Limit connections
maxuploadtarget=5000  # Limit bandwidth (MB/day)

# Privacy
proxy=127.0.0.1:9050  # Use Tor for privacy
listen=0              # Don't accept incoming connections (if not needed)
dnsseed=0             # Don't use DNS seeds

# Performance & DoS Protection
maxmempool=300        # Limit mempool size (MB)
mempoolexpiry=72      # Mempool expiry (hours)
minrelaytxfee=0.0001  # Minimum relay fee (prevents spam)

# Firewall Rules (iptables)
# Allow only necessary ports
iptables -A INPUT -p tcp --dport 8333 -j ACCEPT  # Bitcoin P2P
iptables -A INPUT -p tcp --dport 22 -j ACCEPT    # SSH (from specific IPs)
iptables -A INPUT -j DROP  # Drop all other incoming

# Rate limiting
iptables -A INPUT -p tcp --dport 8333 -m limit --limit 25/minute --limit-burst 100 -j ACCEPT
```

**Ethereum Validator Security**:

```yaml
# Lighthouse (Ethereum Consensus Client) Security Config

# Network Configuration
network: mainnet
http-address: 127.0.0.1  # Local only
http-port: 5052
metrics-address: 127.0.0.1
metrics-port: 5054

# Validator Security
graffiti: ""  # Don't reveal identity
suggested-fee-recipient: 0x...  # Fee recipient address

# Slashing Protection
slashing-protection-db-path: /var/lib/lighthouse/validators/slashing_protection.sqlite

# Performance & DoS Protection
target-peers: 80
max-peers: 100

# Monitoring
validator-monitor-auto: true
validator-monitor-individual-tracking-threshold: 64
```

**Geographic Distribution Strategy**:

```
Node Distribution Best Practices:

1. Multi-Region Deployment
   ├─ Minimum 3 geographic regions
   ├─ Different continents for global networks
   ├─ Avoid concentration in single jurisdiction
   └─ Consider regulatory diversity

2. Hosting Provider Diversity
   ├─ Use multiple cloud providers (AWS, GCP, Azure)
   ├─ Include bare-metal servers
   ├─ Mix of data centers and edge locations
   └─ Avoid single point of failure

3. Network Diversity
   ├─ Different ISPs and ASNs
   ├─ Multiple internet exchange points
   ├─ Redundant connectivity paths
   └─ BGP route diversity

4. Client Software Diversity
   ├─ Run multiple client implementations
   ├─ Ethereum: Mix of Geth, Nethermind, Besu, Erigon
   ├─ Bitcoin: Bitcoin Core, btcd, libbitcoin
   └─ Prevents single-client bugs from affecting entire network
```

---

## DDoS Attack Defense

### Attack Vectors and Mitigation

**Layer 3/4 DDoS (Network/Transport Layer)**:

```
Attack Types:
├─ SYN Flood: Exhaust connection table with half-open connections
├─ UDP Flood: Overwhelm with UDP packets
├─ ICMP Flood: Ping flood attacks
└─ Amplification: DNS, NTP, memcached reflection attacks

Mitigation Stack:

1. Infrastructure Level
   ├─ CDN/DDoS Protection: Cloudflare, Akamai, AWS Shield
   ├─ Anycast Network: Distribute traffic across multiple locations
   ├─ Rate Limiting: Per-IP connection and bandwidth limits
   └─ Blackhole Routing: Drop attack traffic at network edge

2. Operating System Level
   ├─ SYN Cookies: Prevent SYN flood
   ├─ Connection Limits: Limit concurrent connections per IP
   ├─ Kernel Tuning: Optimize network stack
   └─ Firewall Rules: Drop malicious patterns

3. Application Level
   ├─ Connection Throttling: Limit new connections per second
   ├─ Memory Pool Limits: Prevent memory exhaustion
   ├─ Transaction Validation: Reject invalid transactions early
   └─ Peer Reputation: Deprioritize misbehaving peers
```

**Linux Kernel Hardening for DDoS**:

```bash
# /etc/sysctl.conf - Network Stack Tuning

# SYN Flood Protection
net.ipv4.tcp_syncookies = 1
net.ipv4.tcp_max_syn_backlog = 2048
net.ipv4.tcp_synack_retries = 2
net.ipv4.tcp_syn_retries = 5

# Connection Limits
net.core.somaxconn = 1024
net.ipv4.tcp_max_tw_buckets = 1440000
net.ipv4.ip_local_port_range = 1024 65535

# ICMP Protection
net.ipv4.icmp_echo_ignore_all = 0
net.ipv4.icmp_echo_ignore_broadcasts = 1
net.ipv4.icmp_ignore_bogus_error_responses = 1

# IP Spoofing Protection
net.ipv4.conf.all.rp_filter = 1
net.ipv4.conf.default.rp_filter = 1

# Ignore ICMP redirects
net.ipv4.conf.all.accept_redirects = 0
net.ipv6.conf.all.accept_redirects = 0

# Increase buffer sizes
net.core.rmem_max = 134217728
net.core.wmem_max = 134217728
net.ipv4.tcp_rmem = 4096 87380 67108864
net.ipv4.tcp_wmem = 4096 65536 67108864

# Apply changes
sysctl -p
```

**Application-Layer DDoS (Layer 7)**:

```
Blockchain-Specific Attacks:

1. Transaction Spam
   Attack: Flood network with low-fee transactions
   Mitigation:
   ├─ Minimum fee requirements
   ├─ Mempool size limits
   ├─ Fee-based prioritization
   └─ Transaction rate limiting per address

2. Block Propagation Attacks
   Attack: Send large blocks to slow propagation
   Mitigation:
   ├─ Block size limits
   ├─ Compact block relay (Bitcoin)
   ├─ Fast block propagation protocols
   └─ Peer reputation systems

3. RPC API Abuse
   Attack: Expensive RPC calls to exhaust resources
   Mitigation:
   ├─ API rate limiting
   ├─ Authentication and authorization
   ├─ Query complexity limits
   ├─ Caching for expensive queries
   └─ Separate public/private RPC endpoints

4. P2P Protocol Exploitation
   Attack: Malformed messages, excessive requests
   Mitigation:
   ├─ Strict message validation
   ├─ Peer banning for misbehavior
   ├─ Request rate limits per peer
   └─ Resource usage tracking per connection
```

**Rate Limiting Implementation**:

```python
# Example: RPC Rate Limiting with Redis

import redis
import time
from functools import wraps

redis_client = redis.Redis(host='localhost', port=6379, db=0)

def rate_limit(max_requests=100, window=60):
    """Rate limit decorator for RPC endpoints"""
    def decorator(func):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            ip = request.remote_addr
            key = f"rate_limit:{func.__name__}:{ip}"
            
            # Get current request count
            current = redis_client.get(key)
            
            if current is None:
                # First request in window
                redis_client.setex(key, window, 1)
                return func(request, *args, **kwargs)
            
            current = int(current)
            if current >= max_requests:
                # Rate limit exceeded
                return {"error": "Rate limit exceeded"}, 429
            
            # Increment counter
            redis_client.incr(key)
            return func(request, *args, **kwargs)
        
        return wrapper
    return decorator

# Usage
@rate_limit(max_requests=10, window=60)  # 10 requests per minute
def get_balance(request, address):
    # Expensive RPC call
    return blockchain.get_balance(address)
```

---

## Eclipse Attack Prevention

### Attack Mechanism

**Eclipse Attack Execution**:

```
Objective: Isolate victim node from honest network

Step 1: Attacker identifies victim node
├─ Scan network for target nodes
├─ Identify node's IP address and port
└─ Determine node's peer connection limits

Step 2: Attacker monopolizes victim's connections
├─ Attacker controls multiple IP addresses (botnet)
├─ Attacker's nodes connect to victim
├─ Victim accepts connections until limit reached
└─ All victim's peers are attacker-controlled

Step 3: Victim is isolated
├─ Victim only receives data from attacker
├─ Attacker can:
│   ├─ Feed victim false blockchain data
│   ├─ Hide transactions from victim
│   ├─ Perform double-spend against victim
│   └─ Waste victim's mining power on invalid chain
└─ Victim has no connection to honest network
```

**Impact Scenarios**:

```
1. Merchant Double-Spend
   ├─ Attacker eclipses merchant's node
   ├─ Sends payment transaction to merchant
   ├─ Merchant sees confirmations (on attacker's chain)
   ├─ Merchant delivers goods
   ├─ Attacker releases eclipse
   └─ Merchant's node syncs to real chain (no payment)

2. Mining Power Waste
   ├─ Attacker eclipses miner's node
   ├─ Feeds miner outdated or invalid blockchain
   ├─ Miner wastes hash power on wrong chain
   └─ Miner earns no rewards

3. Network Partition
   ├─ Attacker eclipses multiple nodes
   ├─ Creates isolated network segments
   ├─ Enables 51% attack on smaller segment
   └─ Can cause chain splits
```

### Defense Mechanisms

**Connection Diversity**:

```bash
# Bitcoin Core Eclipse Attack Mitigation

# Increase outbound connections
maxconnections=125

# Anchor connections (persistent peers)
anchor=1  # Maintain connections to previously connected peers

# Manual peer addition (trusted nodes)
addnode=trusted-node-1.example.com:8333
addnode=trusted-node-2.example.com:8333
addnode=trusted-node-3.example.com:8333

# Seed nodes for initial connection
seednode=seed.bitcoin.sipa.be
seednode=dnsseed.bluematt.me

# Connection preferences
preferrednode=preferred-peer.example.com:8333  # Prefer specific peers

# Onion routing for privacy and eclipse resistance
proxy=127.0.0.1:9050  # Tor proxy
onlynet=onion         # Only connect via Tor (optional)
```

**Peer Selection Algorithms**:

```python
# Ethereum Peer Selection Strategy

class PeerManager:
    def __init__(self):
        self.max_peers = 50
        self.peer_diversity_targets = {
            'subnet_diversity': 0.8,  # 80% from different /24 subnets
            'asn_diversity': 0.7,      # 70% from different ASNs
            'geo_diversity': 0.6,      # 60% from different countries
            'client_diversity': 0.5    # 50% different client software
        }
    
    def should_accept_peer(self, candidate_peer):
        """Determine if new peer should be accepted"""
        current_peers = self.get_current_peers()
        
        # Check subnet diversity
        same_subnet_count = sum(
            1 for p in current_peers 
            if p.subnet_24 == candidate_peer.subnet_24
        )
        if same_subnet_count / len(current_peers) > 0.2:  # Max 20% from same subnet
            return False
        
        # Check ASN diversity
        same_asn_count = sum(
            1 for p in current_peers 
            if p.asn == candidate_peer.asn
        )
        if same_asn_count / len(current_peers) > 0.3:  # Max 30% from same ASN
            return False
        
        # Prefer peers with good reputation
        if candidate_peer.reputation_score < 0.5:
            return False
        
        # Prefer diverse client software
        same_client_count = sum(
            1 for p in current_peers 
            if p.client_version == candidate_peer.client_version
        )
        if same_client_count / len(current_peers) > 0.5:
            return False
        
        return True
    
    def peer_eviction_strategy(self):
        """Select peer to evict when at max connections"""
        current_peers = self.get_current_peers()
        
        # Protect peers with:
        protected = []
        for peer in current_peers:
            if (
                peer.is_outbound or           # Outbound connections
                peer.uptime > 86400 or        # >24h uptime
                peer.has_useful_blocks or     # Provided useful data
                peer.is_whitelisted           # Manually whitelisted
            ):
                protected.append(peer)
        
        # Evict from unprotected peers
        unprotected = [p for p in current_peers if p not in protected]
        if unprotected:
            # Evict peer with lowest reputation
            return min(unprotected, key=lambda p: p.reputation_score)
        
        return None  # Don't evict if all protected
```

**Monitoring and Detection**:

```python
# Eclipse Attack Detection System

import time
from collections import defaultdict

class EclipseDetector:
    def __init__(self):
        self.peer_history = defaultdict(list)
        self.alert_threshold = 0.7  # Alert if 70% peers from same source
    
    def analyze_peer_distribution(self):
        """Detect potential eclipse attack"""
        current_peers = self.get_current_peers()
        
        # Analyze subnet concentration
        subnet_distribution = defaultdict(int)
        for peer in current_peers:
            subnet_distribution[peer.subnet_24] += 1
        
        max_subnet_concentration = max(subnet_distribution.values()) / len(current_peers)
        
        if max_subnet_concentration > self.alert_threshold:
            self.trigger_alert(
                f"High subnet concentration: {max_subnet_concentration:.1%}"
            )
        
        # Analyze ASN concentration
        asn_distribution = defaultdict(int)
        for peer in current_peers:
            asn_distribution[peer.asn] += 1
        
        max_asn_concentration = max(asn_distribution.values()) / len(current_peers)
        
        if max_asn_concentration > self.alert_threshold:
            self.trigger_alert(
                f"High ASN concentration: {max_asn_concentration:.1%}"
            )
        
        # Check for sudden peer turnover
        current_peer_ids = {p.id for p in current_peers}
        if self.peer_history:
            previous_peer_ids = set(self.peer_history[-1])
            turnover_rate = len(current_peer_ids - previous_peer_ids) / len(current_peer_ids)
            
            if turnover_rate > 0.5:  # >50% peers changed
                self.trigger_alert(
                    f"High peer turnover: {turnover_rate:.1%}"
                )
        
        self.peer_history[time.time()] = list(current_peer_ids)
    
    def trigger_alert(self, message):
        """Alert operators of potential eclipse attack"""
        print(f"[ECLIPSE ALERT] {message}")
        # Send notification (email, Slack, PagerDuty, etc.)
        # Optionally: Automatically add trusted peers
        # Optionally: Disconnect suspicious peers
```

---

## Man-in-the-Middle (MitM) Attack Prevention

### Attack Vectors

**Blockchain MitM Scenarios**:

```
1. Wallet-to-Node Communication
   ├─ User's wallet connects to blockchain node
   ├─ Attacker intercepts connection
   ├─ Attacker modifies:
   │   ├─ Transaction recipient addresses
   │   ├─ Transaction amounts
   │   └─ Balance information
   └─ User unknowingly sends funds to attacker

2. Node-to-Node Communication
   ├─ Attacker intercepts P2P messages
   ├─ Can modify or drop:
   │   ├─ Block propagation
   │   ├─ Transaction broadcasts
   │   └─ Peer discovery messages
   └─ Enables eclipse attacks and censorship

3. RPC API Interception
   ├─ Application connects to blockchain RPC
   ├─ Attacker intercepts API calls
   ├─ Returns false data:
   │   ├─ Fake transaction confirmations
   │   ├─ Incorrect balances
   │   └─ Manipulated smart contract states
   └─ Application makes decisions on false data
```

### Encryption and Authentication

**TLS/SSL for RPC Connections**:

```bash
# Generate SSL certificates for Bitcoin RPC

# 1. Generate private key
openssl genrsa -out bitcoin-rpc.key 4096

# 2. Generate certificate signing request
openssl req -new -key bitcoin-rpc.key -out bitcoin-rpc.csr

# 3. Generate self-signed certificate (or use CA)
openssl x509 -req -days 365 -in bitcoin-rpc.csr \
  -signkey bitcoin-rpc.key -out bitcoin-rpc.crt

# 4. Configure Bitcoin Core
# bitcoin.conf
rpcssl=1
rpcsslcertificatechainfile=/path/to/bitcoin-rpc.crt
rpcsslprivatekeyfile=/path/to/bitcoin-rpc.key
rpcallowip=192.168.1.0/24
rpcbind=0.0.0.0
```

**Ethereum RPC over HTTPS**:

```bash
# Nginx reverse proxy for Geth RPC

server {
    listen 443 ssl http2;
    server_name ethereum-rpc.example.com;
    
    # SSL Configuration
    ssl_certificate /etc/ssl/certs/ethereum-rpc.crt;
    ssl_certificate_key /etc/ssl/private/ethereum-rpc.key;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    ssl_prefer_server_ciphers on;
    
    # Security Headers
    add_header Strict-Transport-Security "max-age=31536000" always;
    add_header X-Frame-Options DENY;
    add_header X-Content-Type-Options nosniff;
    
    # Rate Limiting
    limit_req_zone $binary_remote_addr zone=rpc_limit:10m rate=10r/s;
    limit_req zone=rpc_limit burst=20 nodelay;
    
    # Proxy to Geth
    location / {
        proxy_pass http://127.0.0.1:8545;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        
        # Authentication
        auth_basic "Ethereum RPC";
        auth_basic_user_file /etc/nginx/.htpasswd;
    }
}
```

**P2P Encryption (Ethereum DevP2P)**:

```
Ethereum P2P Encryption (RLPx Protocol):

1. Handshake Phase
   ├─ ECDH key exchange (secp256k1)
   ├─ Derive shared secret
   └─ Establish encrypted channel

2. Frame Encryption
   ├─ AES-256 in CTR mode
   ├─ MAC authentication (HMAC-SHA256)
   └─ Forward secrecy

3. Peer Authentication
   ├─ Node ID verification (public key)
   ├─ Signature validation
   └─ Prevents impersonation

Result:
└─ All P2P communication encrypted and authenticated
```

---

## BGP Hijacking Defense

### Attack Mechanism

**BGP Hijack Scenario**:

```
Normal Routing:
User → ISP → Internet → Blockchain Node (AS 64500)

BGP Hijack:
1. Attacker (AS 64501) announces route to Node's IP prefix
2. Attacker's announcement is more specific or appears closer
3. Internet routers update routing tables
4. Traffic destined for Node is routed to Attacker
5. Attacker can:
   ├─ Drop traffic (DoS)
   ├─ Intercept and modify (MitM)
   └─ Redirect to malicious node

Result:
└─ Users connect to attacker instead of legitimate node
```

**Real-World Incidents**:
- **MyEtherWallet (2018)**: BGP hijack redirected users to phishing site, $150K stolen
- **Amazon Route 53 (2018)**: BGP hijack enabled cryptocurrency theft

### Mitigation Strategies

**RPKI (Resource Public Key Infrastructure)**:

```bash
# Configure RPKI validation on router

# Example: BIRD routing daemon
roa4 table r4;
roa6 table r6;

protocol rpki {
    roa4 { table r4; };
    roa6 { table r6; };
    
    remote "rpki.example.com" port 323;
    
    retry keep 90;
    refresh keep 900;
    expire keep 172800;
}

# Filter BGP announcements
filter rpki_filter {
    if (roa_check(r4, net, bgp_path.last) = ROA_INVALID) then {
        print "RPKI Invalid: ", net, " from AS", bgp_path.last;
        reject;
    }
    accept;
}
```

**Multi-Homing and Anycast**:

```
Multi-Homing Strategy:
├─ Announce IP prefix from multiple ASNs
├─ Use different upstream providers
├─ Geographic diversity of announcements
└─ Harder for attacker to hijack all paths

Anycast Deployment:
├─ Same IP announced from multiple locations
├─ Traffic routes to nearest instance
├─ Attacker can only affect local region
└─ Automatic failover if one location hijacked
```

**Monitoring and Detection**:

```python
# BGP Monitoring System

import requests
import time

class BGPMonitor:
    def __init__(self, monitored_prefixes):
        self.prefixes = monitored_prefixes
        self.baseline_asns = {}  # Expected ASNs for each prefix
    
    def check_bgp_routes(self):
        """Monitor BGP announcements for hijacks"""
        for prefix in self.prefixes:
            # Query BGP looking glass or RIS/RouteViews
            current_asns = self.query_bgp_route(prefix)
            
            if prefix not in self.baseline_asns:
                self.baseline_asns[prefix] = current_asns
                continue
            
            # Check for unexpected ASNs
            unexpected = current_asns - self.baseline_asns[prefix]
            if unexpected:
                self.alert_bgp_anomaly(prefix, unexpected)
    
    def query_bgp_route(self, prefix):
        """Query BGP route for prefix"""
        # Use RIPEstat, BGPStream, or similar service
        url = f"https://stat.ripe.net/data/routing-status/data.json?resource={prefix}"
        response = requests.get(url)
        data = response.json()
        
        asns = set()
        for route in data.get('data', {}).get('routes', []):
            asns.add(route['origin'])
        
        return asns
    
    def alert_bgp_anomaly(self, prefix, unexpected_asns):
        """Alert on potential BGP hijack"""
        print(f"[BGP ALERT] Unexpected ASNs announcing {prefix}: {unexpected_asns}")
        # Send alerts, trigger incident response
```

---

## Cryptographic Security

### Key Management Best Practices

**Hardware Security Modules (HSMs)**:

```
HSM Benefits for Blockchain:
├─ Private keys never leave secure hardware
├─ Tamper-resistant key storage
├─ Cryptographic operations in hardware
├─ Audit logging of all key usage
└─ FIPS 140-2 Level 3/4 certification

Use Cases:
├─ Validator signing keys
├─ Multi-signature wallet keys
├─ Exchange hot wallet keys
├─ Smart contract deployment keys
└─ Certificate authority keys

Implementation:
├─ Cloud HSM: AWS CloudHSM, Azure Dedicated HSM
├─ On-Premise: Thales, Utimaco, Gemalto
└─ Integration: PKCS#11, JCE, CNG APIs
```

**Multi-Signature Security**:

```solidity
// Gnosis Safe Multi-Signature Wallet Pattern

contract MultiSigWallet {
    address[] public owners;
    uint256 public required;  // Required signatures
    
    mapping(uint256 => Transaction) public transactions;
    mapping(uint256 => mapping(address => bool)) public confirmations;
    
    struct Transaction {
        address destination;
        uint256 value;
        bytes data;
        bool executed;
    }
    
    modifier onlyOwner() {
        require(isOwner(msg.sender), "Not an owner");
        _;
    }
    
    function submitTransaction(address destination, uint256 value, bytes memory data)
        public
        onlyOwner
        returns (uint256 transactionId)
    {
        transactionId = addTransaction(destination, value, data);
        confirmTransaction(transactionId);
    }
    
    function confirmTransaction(uint256 transactionId)
        public
        onlyOwner
    {
        require(!confirmations[transactionId][msg.sender], "Already confirmed");
        confirmations[transactionId][msg.sender] = true;
        
        if (isConfirmed(transactionId)) {
            executeTransaction(transactionId);
        }
    }
    
    function isConfirmed(uint256 transactionId) public view returns (bool) {
        uint256 count = 0;
        for (uint256 i = 0; i < owners.length; i++) {
            if (confirmations[transactionId][owners[i]]) {
                count++;
            }
        }
        return count >= required;
    }
}
```

**Key Rotation Procedures**:

```
Validator Key Rotation (Ethereum):

1. Preparation Phase
   ├─ Generate new validator keys (offline)
   ├─ Secure backup of new keys
   ├─ Test new keys on testnet
   └─ Schedule rotation during low-activity period

2. Execution Phase
   ├─ Submit BLS key change operation
   ├─ Wait for inclusion in beacon chain
   ├─ Update validator client configuration
   ├─ Restart validator with new keys
   └─ Verify successful attestations

3. Cleanup Phase
   ├─ Securely delete old keys from active systems
   ├─ Archive old keys in cold storage (for slashing protection)
   ├─ Update documentation and key inventory
   └─ Monitor for any issues

Frequency:
├─ Regular rotation: Every 12-24 months
├─ Emergency rotation: If compromise suspected
└─ Compliance rotation: Per regulatory requirements
```

---

## Network Monitoring and Incident Response

### Real-Time Monitoring

**Prometheus + Grafana Stack**:

```yaml
# prometheus.yml - Blockchain Node Monitoring

global:
  scrape_interval: 15s
  evaluation_interval: 15s

scrape_configs:
  - job_name: 'ethereum-node'
    static_configs:
      - targets: ['localhost:6060']  # Geth metrics
    
  - job_name: 'validator'
    static_configs:
      - targets: ['localhost:5054']  # Lighthouse metrics
  
  - job_name: 'node-exporter'
    static_configs:
      - targets: ['localhost:9100']  # System metrics

# Alert Rules
rule_files:
  - 'alerts.yml'

alerting:
  alertmanagers:
    - static_configs:
        - targets: ['localhost:9093']
```

```yaml
# alerts.yml - Blockchain Security Alerts

groups:
  - name: blockchain_security
    interval: 30s
    rules:
      - alert: HighPeerChurn
        expr: rate(p2p_peers_total[5m]) > 10
        for: 5m
        annotations:
          summary: "High peer connection churn detected"
          description: "Possible eclipse attack attempt"
      
      - alert: UnusualTransactionVolume
        expr: rate(txpool_pending[5m]) > 1000
        for: 2m
        annotations:
          summary: "Unusual transaction volume"
          description: "Possible DDoS or spam attack"
      
      - alert: ChainReorganization
        expr: increase(chain_reorg_total[10m]) > 0
        annotations:
          summary: "Blockchain reorganization detected"
          description: "Possible 51% attack or network issue"
      
      - alert: ValidatorMissedAttestations
        expr: validator_missed_attestations > 3
        for: 5m
        annotations:
          summary: "Validator missing attestations"
          description: "Risk of inactivity penalties"
```

**Incident Response Playbook**:

```
Network Attack Response Procedure:

1. Detection (0-5 minutes)
   ├─ Automated alert triggers
   ├─ Verify alert validity
   ├─ Assess severity and scope
   └─ Activate incident response team

2. Containment (5-30 minutes)
   ├─ DDoS Attack:
   │   ├─ Enable DDoS mitigation (Cloudflare, AWS Shield)
   │   ├─ Implement rate limiting
   │   ├─ Block attacking IPs
   │   └─ Scale infrastructure if needed
   │
   ├─ Eclipse Attack:
   │   ├─ Add trusted peer connections
   │   ├─ Disconnect suspicious peers
   │   ├─ Verify blockchain state with multiple sources
   │   └─ Increase peer diversity requirements
   │
   └─ BGP Hijack:
       ├─ Contact upstream providers
       ├─ Announce more specific routes
       ├─ Activate backup connectivity
       └─ Notify users of potential MitM

3. Investigation (Parallel to containment)
   ├─ Collect logs and network captures
   ├─ Identify attack source and method
   ├─ Assess damage and data integrity
   └─ Document timeline and indicators

4. Recovery (30 minutes - 2 hours)
   ├─ Restore normal operations
   ├─ Verify blockchain synchronization
   ├─ Re-enable affected services
   └─ Monitor for recurring attacks

5. Post-Incident (24-48 hours)
   ├─ Root cause analysis
   ├─ Update security controls
   ├─ Improve monitoring and alerts
   ├─ Team debrief and lessons learned
   └─ Public communication (if necessary)
```
