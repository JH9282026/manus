# Blockchain Cryptography and Security

## Introduction

Cryptography is the backbone of blockchain security, providing the mathematical foundations for trust, authentication, and immutability in distributed systems. This reference explores the cryptographic primitives, security mechanisms, and best practices that protect blockchain networks.

## Cryptographic Hash Functions

### Properties and Requirements

**Essential Properties:**

1. **Deterministic**: Same input always produces same output
   - Critical for verification
   - Enables consensus across nodes

2. **Quick Computation**: Fast to calculate hash
   - Enables real-time verification
   - Supports high transaction throughput

3. **Pre-image Resistance**: Cannot reverse hash to find input
   - One-way function
   - Protects original data

4. **Avalanche Effect**: Small input change drastically alters output
   - Single bit change affects ~50% of output bits
   - Prevents pattern recognition

5. **Collision Resistance**: Extremely difficult to find two inputs with same hash
   - Computational infeasibility (2^128+ operations)
   - Prevents forgery and tampering

### Common Hash Algorithms

**SHA-256 (Secure Hash Algorithm 256-bit)**
- Used by: Bitcoin, many other blockchains
- Output: 256-bit (64 hexadecimal characters)
- Security: No practical attacks known
- Performance: ~300 MB/s on modern CPUs

**Example:**
```
Input: "Hello, Blockchain!"
SHA-256: 7d8f9c3e2a1b4f6e8d9c2a1b3f4e5d6c7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d

Input: "Hello, Blockchain?" (changed ! to ?)
SHA-256: 3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b
```

**Keccak-256**
- Used by: Ethereum
- Output: 256-bit
- Basis: SHA-3 competition winner
- Difference from SHA-3: Ethereum uses original Keccak, not NIST-standardized SHA-3

**RIPEMD-160**
- Used by: Bitcoin (in address generation)
- Output: 160-bit
- Often used after SHA-256 for additional security

**BLAKE2**
- Used by: Zcash, Nano
- Output: Configurable (BLAKE2b: up to 512-bit)
- Performance: Faster than SHA-256
- Security: Comparable to SHA-3

### Hash Function Applications

**Block Linking:**
```
Block N:
- Previous Hash: Hash of Block N-1
- Transactions: [...]
- Nonce: 12345
- Block Hash: SHA-256(Previous Hash + Transactions + Nonce)

Block N+1:
- Previous Hash: Block Hash of Block N
- ...
```

**Transaction Identification:**
- Each transaction has unique hash (TXID)
- Used for referencing and verification
- Prevents transaction malleability

**Address Generation:**
```
Bitcoin Address Generation:
1. Generate private key (256-bit random number)
2. Derive public key (ECDSA)
3. SHA-256(public key)
4. RIPEMD-160(SHA-256 hash)
5. Add version byte
6. Add checksum (double SHA-256)
7. Base58 encode
```

## Public Key Cryptography

### Elliptic Curve Cryptography (ECC)

**Why ECC?**
- Smaller key sizes vs RSA (256-bit ECC ≈ 3072-bit RSA)
- Faster computation
- Lower bandwidth requirements
- Ideal for blockchain's distributed nature

**Elliptic Curve Equation:**
```
y² = x³ + ax + b (mod p)
```

**Common Curves:**

1. **secp256k1** (Bitcoin, Ethereum)
   - Parameters: a=0, b=7
   - Prime: 2^256 - 2^32 - 977
   - Chosen for efficiency

2. **Ed25519** (Cardano, Polkadot)
   - Edwards curve
   - Faster signature verification
   - Simpler implementation

### Digital Signatures

**ECDSA (Elliptic Curve Digital Signature Algorithm)**

**Key Generation:**
```
1. Generate private key: d (random 256-bit number)
2. Calculate public key: Q = d × G (G is generator point)
3. Public key Q is point on elliptic curve
```

**Signing Process:**
```
1. Hash message: h = SHA-256(message)
2. Generate random k
3. Calculate point: (x, y) = k × G
4. Calculate r = x mod n
5. Calculate s = k^(-1) × (h + r × d) mod n
6. Signature: (r, s)
```

**Verification Process:**
```
1. Hash message: h = SHA-256(message)
2. Calculate u1 = h × s^(-1) mod n
3. Calculate u2 = r × s^(-1) mod n
4. Calculate point: (x, y) = u1 × G + u2 × Q
5. Verify: r = x mod n
```

**Signature Properties:**
- Authenticity: Proves message from private key holder
- Integrity: Detects any message modification
- Non-repudiation: Signer cannot deny signing
- Size: 64-72 bytes (Bitcoin)

### Key Management

**Private Key Security:**
- Never share or expose
- Store offline when possible
- Use hardware wallets for significant holdings
- Implement multi-signature for high-value accounts

**Key Derivation (HD Wallets):**
```
BIP-32 Hierarchical Deterministic Wallets:
1. Master seed (128-256 bits)
2. Master private key derived from seed
3. Child keys derived from parent keys
4. Allows backup of entire wallet with single seed

Derivation Path Example:
m / 44' / 0' / 0' / 0 / 0
│    │     │    │   │   └─ Address index
│    │     │    │   └───── External/Internal
│    │     │    └───────── Account
│    │     └────────────── Coin type (0 = Bitcoin)
│    └──────────────────── Purpose (44 = BIP-44)
└───────────────────────── Master key
```

## Merkle Trees

### Structure and Construction

**Building a Merkle Tree:**
```
                Root Hash
               /          \
         Hash AB          Hash CD
         /    \           /    \
    Hash A  Hash B   Hash C  Hash D
      |       |        |       |
    TX A    TX B     TX C    TX D
```

**Construction Algorithm:**
```python
def build_merkle_tree(transactions):
    # Hash all transactions
    leaves = [hash(tx) for tx in transactions]
    
    # If odd number, duplicate last
    if len(leaves) % 2 == 1:
        leaves.append(leaves[-1])
    
    # Build tree bottom-up
    while len(leaves) > 1:
        new_level = []
        for i in range(0, len(leaves), 2):
            parent = hash(leaves[i] + leaves[i+1])
            new_level.append(parent)
        leaves = new_level
    
    return leaves[0]  # Root hash
```

### Merkle Proofs

**Verification Without Full Data:**
```
To prove TX B is in block:
1. Provide: TX B, Hash A, Hash CD
2. Verify:
   - Hash B = hash(TX B)
   - Hash AB = hash(Hash A + Hash B)
   - Root = hash(Hash AB + Hash CD)
3. Compare Root with block header
```

**Proof Size:**
- For n transactions: log₂(n) hashes needed
- 1,000 transactions: ~10 hashes (320 bytes)
- 1,000,000 transactions: ~20 hashes (640 bytes)
- Enables lightweight clients (SPV)

### Applications

**Bitcoin SPV (Simplified Payment Verification):**
- Download only block headers (~80 bytes each)
- Request Merkle proofs for relevant transactions
- Verify without full blockchain
- Enables mobile wallets

**Ethereum State Trees:**
- Modified Merkle Patricia Trie
- Stores account states
- Enables state proofs
- Supports light clients

## Zero-Knowledge Proofs

### Concept and Properties

**Zero-Knowledge Proof (ZKP):**
Prove knowledge of information without revealing the information itself.

**Properties:**
1. **Completeness**: True statements can be proven
2. **Soundness**: False statements cannot be proven
3. **Zero-Knowledge**: No information leaked beyond validity

### zk-SNARKs

**Zero-Knowledge Succinct Non-Interactive Argument of Knowledge**

**Characteristics:**
- Succinct: Small proof size (~200 bytes)
- Non-interactive: No back-and-forth communication
- Fast verification: Milliseconds
- Trusted setup required: Initial ceremony

**Applications:**
- Zcash: Private transactions
- zkSync: Ethereum Layer 2 scaling
- Tornado Cash: Transaction privacy

**Example Use Case:**
```
Private Transaction:
1. Prove: "I have 10 coins"
2. Without revealing: Which coins, from where
3. Verifier confirms: Proof is valid
4. Transaction proceeds: Coins transferred privately
```

### zk-STARKs

**Zero-Knowledge Scalable Transparent Argument of Knowledge**

**Advantages over zk-SNARKs:**
- No trusted setup
- Quantum resistant
- More scalable

**Disadvantages:**
- Larger proof size (~100 KB)
- Newer, less battle-tested

**Applications:**
- StarkNet: Ethereum Layer 2
- StarkEx: Exchange infrastructure

## Blockchain Security Threats

### Network-Level Attacks

**51% Attack**

**Mechanism:**
1. Attacker controls >50% of network power
2. Mines private chain faster than honest chain
3. Releases longer chain, orphaning honest blocks
4. Can double-spend, censor transactions

**Defense:**
- High network participation
- Proof of Stake slashing
- Checkpoint systems
- Community vigilance

**Real-World Examples:**
- Bitcoin Gold (2018): $18 million stolen
- Ethereum Classic (2019, 2020): Multiple attacks
- Vertcoin (2018): 22 blocks reorganized

**Sybil Attack**

**Mechanism:**
- Attacker creates many fake identities
- Overwhelms network with malicious nodes
- Can eclipse honest nodes, manipulate routing

**Defense:**
- Resource requirements (PoW, PoS)
- Identity verification (PoA)
- Reputation systems
- Network topology analysis

**Eclipse Attack**

**Mechanism:**
1. Attacker controls victim's network connections
2. Isolates victim from honest network
3. Feeds victim false blockchain data
4. Can facilitate double-spending

**Defense:**
- Diverse peer connections
- Trusted peer lists
- Network monitoring
- Tor/VPN usage

### Transaction-Level Attacks

**Double-Spending**

**Race Attack:**
- Send two conflicting transactions simultaneously
- One to merchant, one to self
- Hope merchant accepts unconfirmed transaction

**Defense:**
- Wait for confirmations
- Use payment processors
- Monitor mempool

**Finney Attack:**
- Miner pre-mines transaction to self
- Spends same coins with merchant
- Releases pre-mined block

**Defense:**
- Wait for multiple confirmations
- Less effective with faster block times

**Transaction Malleability**

**Issue:**
- Transaction ID can be modified before confirmation
- Same transaction, different TXID
- Can confuse wallets, exchanges

**Solution:**
- SegWit (Segregated Witness) in Bitcoin
- Separates signature data
- Makes TXID immutable

### Smart Contract Vulnerabilities

**Reentrancy Attack**

**Famous Example: The DAO Hack (2016)**
- $60 million stolen from Ethereum DAO
- Exploited recursive calling
- Led to Ethereum hard fork

**Vulnerable Code:**
```solidity
function withdraw(uint amount) public {
    require(balances[msg.sender] >= amount);
    msg.sender.call.value(amount)("");  // External call
    balances[msg.sender] -= amount;     // State update after call
}
```

**Attack:**
```solidity
function() payable {
    if (target.balance > 0) {
        target.withdraw(amount);  // Recursive call
    }
}
```

**Fix: Checks-Effects-Interactions Pattern:**
```solidity
function withdraw(uint amount) public {
    require(balances[msg.sender] >= amount);  // Check
    balances[msg.sender] -= amount;           // Effect
    msg.sender.call.value(amount)("");        // Interaction
}
```

**Integer Overflow/Underflow**

**Issue:**
```solidity
uint8 balance = 255;
balance += 1;  // Overflows to 0

uint8 balance = 0;
balance -= 1;  // Underflows to 255
```

**Solution:**
- Solidity 0.8.0+: Automatic overflow checks
- Earlier versions: Use SafeMath library

## Cryptographic Best Practices

### For Developers

**Key Generation:**
- Use cryptographically secure random number generators
- Never use predictable seeds
- Ensure sufficient entropy

**Signature Implementation:**
- Use established libraries (OpenSSL, libsecp256k1)
- Don't implement crypto from scratch
- Keep libraries updated

**Hash Function Selection:**
- Use SHA-256 or SHA-3 for general purposes
- Consider BLAKE2 for performance
- Avoid deprecated algorithms (MD5, SHA-1)

### For Users

**Wallet Security:**
- Use hardware wallets for large holdings
- Enable 2FA on exchanges
- Verify addresses carefully
- Use multi-signature for high-value accounts

**Transaction Safety:**
- Double-check recipient addresses
- Verify transaction details before signing
- Wait for sufficient confirmations
- Be cautious of phishing attempts

**Backup and Recovery:**
- Securely store seed phrases
- Use metal backups for long-term storage
- Never store seeds digitally
- Test recovery process

## Post-Quantum Cryptography

### Quantum Threat

**Shor's Algorithm:**
- Quantum algorithm for factoring
- Breaks RSA, ECDSA in polynomial time
- Requires large-scale quantum computer
- Timeline: 10-30 years (estimates vary)

**Impact on Blockchain:**
- Current signatures vulnerable
- Addresses safe until coins spent
- Need transition to quantum-resistant algorithms

### Quantum-Resistant Alternatives

**Lattice-Based Cryptography:**
- Based on hard lattice problems
- NIST standardized: CRYSTALS-Dilithium
- Larger signatures (~2-3 KB)
- Fast verification

**Hash-Based Signatures:**
- Based on hash function security
- NIST standardized: SPHINCS+
- Very large signatures (~8-50 KB)
- Stateless (no key state management)

**Code-Based Cryptography:**
- Based on error-correcting codes
- Large public keys
- Fast encryption/decryption

**Multivariate Cryptography:**
- Based on multivariate polynomial equations
- Small signatures
- Slow key generation

### Transition Strategies

**Hybrid Approach:**
- Use both classical and quantum-resistant signatures
- Secure if either is unbroken
- Larger transaction sizes

**Gradual Migration:**
- Introduce quantum-resistant addresses
- Allow time for ecosystem adoption
- Maintain backward compatibility

**Hard Fork:**
- Network-wide upgrade
- All addresses migrate
- Requires community consensus

## Conclusion

Cryptography is the foundation of blockchain security, providing the mathematical guarantees that enable trustless systems. Understanding these cryptographic primitives—hash functions, digital signatures, Merkle trees, and zero-knowledge proofs—is essential for anyone working with blockchain technology. As quantum computing advances, the blockchain community must prepare for the transition to post-quantum cryptography, ensuring long-term security for decentralized systems.
