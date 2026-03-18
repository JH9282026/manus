# Private Key Management

Advanced strategies for generating, storing, backing up, and managing cryptocurrency private keys and seed phrases.

---

## Key Generation Best Practices

### Entropy and Randomness

**Secure Random Number Generation**:

```
Hardware Wallet Generation:
├─ Uses True Random Number Generator (TRNG)
├─ Based on physical phenomena (thermal noise, etc.)
├─ Cryptographically secure
├─ Audited by security researchers
└─ Recommended method for most users

Software Wallet Generation:
├─ Uses Cryptographically Secure PRNG (CSPRNG)
├─ Seeded from OS entropy pool
├─ Quality depends on implementation
├─ Verify wallet is reputable and audited
└─ Acceptable for small-medium amounts

Dice Roll Method (Advanced):
├─ Roll dice to generate entropy
├─ Convert rolls to binary/hexadecimal
├─ Use as seed for key derivation
├─ Completely offline and verifiable
└─ Supported by Coldcard, some software wallets

Example (Bitcoin, 256-bit key):
1. Roll 6-sided die 99 times
2. Convert each roll to binary (1-6 → 000-101)
3. Concatenate to get 256+ bits
4. Use as private key or seed
5. Derive addresses using BIP32/39/44
```

**Seed Phrase Standards**:

```
BIP39 (Most Common):
├─ 12 or 24 words from 2048-word list
├─ Each word represents 11 bits
├─ Last word includes checksum
├─ Supported by most wallets
└─ Example: "abandon ability able about above absent absorb abstract absurd abuse access accident"

SLIP39 (Shamir's Secret Sharing):
├─ Split seed into multiple shares
├─ Require M-of-N shares to recover
├─ More complex but more flexible
├─ Supported by Trezor Model T
└─ Example: 5 shares, need any 3 to recover

Electrum Seed:
├─ 12 words with version information
├─ Different wordlist than BIP39
├─ Not compatible with other wallets
├─ Includes wallet type in seed
└─ Electrum-specific
```

### Passphrase (25th Word)

**Implementation**:

```
How It Works:
├─ BIP39 seed + optional passphrase
├─ Passphrase can be any string (no length limit)
├─ Different passphrase = different wallet
├─ No "wrong" passphrase (all are valid)
└─ Provides plausible deniability

Derivation:
Seed Phrase (24 words) + Passphrase → Master Private Key → Addresses

Examples:
├─ Seed alone → Wallet A (decoy, small amount)
├─ Seed + "MySecret123" → Wallet B (real holdings)
├─ Seed + "Trading2024" → Wallet C (trading funds)
└─ Each is a completely different wallet
```

**Use Cases**:

```
1. Duress Protection
   ├─ Seed phrase: $1,000 (decoy)
   ├─ Seed + passphrase: $100,000 (real)
   └─ Under threat, reveal seed only

2. Multi-Purpose Wallets
   ├─ Passphrase A: Long-term savings
   ├─ Passphrase B: Trading account
   ├─ Passphrase C: Experimental/DeFi
   └─ Passphrase D: Business funds

3. Inheritance Planning
   ├─ Seed: In will/safe deposit box
   ├─ Passphrase: Memorized or separate location
   ├─ Executor gets seed, trusted person has passphrase
   └─ Requires coordination to access

4. Travel Security
   ├─ Seed: At home (secure)
   ├─ Passphrase: Memorized
   ├─ Travel with hardware wallet (no passphrase stored)
   └─ If confiscated, funds safe (need passphrase)
```

**Security Considerations**:

```
CRITICAL:
├─ Passphrase must be backed up separately
├─ Losing passphrase = losing funds (no recovery)
├─ No way to know if passphrase is "correct"
└─ Every passphrase is valid (creates different wallet)

Passphrase Strength:
├─ Weak: "password123" (guessable)
├─ Medium: "MyDog'sName2024!" (personal info)
├─ Strong: "correct-horse-battery-staple" (random words)
├─ Very Strong: "Tr0ub4dor&3-xkcd-correct-horse" (mixed)
└─ Recommendation: 4+ random words or 20+ mixed characters

Storage:
├─ DON'T store with seed phrase (defeats purpose)
├─ DO memorize (if strong enough)
├─ DO write separately and store in different location
├─ DO consider splitting (Shamir for passphrase too)
└─ DO test recovery before funding wallet
```

---

## Backup Strategies

### Physical Backup Methods

**Paper Backup**:

```
Materials:
├─ Archival-quality paper (acid-free)
├─ Permanent ink pen (archival ink)
├─ Laminating pouches
├─ Tamper-evident bags/envelopes
└─ Fireproof document safe

Process:
1. Write seed words clearly (print, not cursive)
2. Number each word (1-24)
3. Include wallet type and date
4. Write multiple copies (2-3)
5. Laminate for water protection
6. Place in tamper-evident envelope
7. Store in fireproof safe
8. Store copies in separate locations

Pros:
├─ Inexpensive
├─ Easy to create
├─ Human-readable
└─ No special equipment needed

Cons:
├─ Vulnerable to fire (even in "fireproof" safe)
├─ Ink can fade over time
├─ Paper degrades
├─ Water damage risk
└─ Easily destroyed

Best For:
├─ Temporary storage
├─ Small-medium amounts
├─ Redundant backup (with metal)
└─ Testing before metal backup
```

**Metal Backup**:

```
Commercial Solutions:

Cryptosteel Capsule ($100):
├─ Stainless steel capsule
├─ Letter tiles slide into slots
├─ Fireproof to 1400°C (2552°F)
├─ Waterproof, corrosion-resistant
├─ Stores 24 words
└─ No tools required

Billfodl ($80):
├─ Stainless steel plates
├─ Letter tiles in grid
├─ Fireproof to 1500°C (2732°F)
├─ Crush-resistant
├─ Stores 24 words
└─ Compact design

Blockplate ($50):
├─ Titanium plate
├─ Stamp or engrave words
├─ Fireproof to 1668°C (3034°F)
├─ Extremely durable
├─ DIY stamping
└─ Most durable option

Cobo Tablet ($40):
├─ Stainless steel grid
├─ Punch dots to encode words
├─ Fireproof, waterproof
├─ Requires decoding (privacy)
├─ Compact
└─ Obscures seed from casual viewing

DIY Metal Backup (<$20):
├─ Stainless steel or titanium plate (hardware store)
├─ Metal stamping kit
├─ Stamp seed words
├─ Same durability as commercial
└─ Requires physical effort

Fire Resistance Testing:
├─ House fire: ~1100°C (2012°F)
├─ Stainless steel melts: ~1400°C (2552°F)
├─ Titanium melts: ~1668°C (3034°F)
└─ All metal backups survive typical house fires
```

**Encrypted Digital Backup**:

```
When Acceptable:
├─ As redundant backup (not primary)
├─ For travel/temporary access
├─ With strong encryption
└─ Never as only backup

Encryption Method:

1. VeraCrypt Container:
   ├─ Create encrypted container
   ├─ Use strong passphrase (20+ characters)
   ├─ Store seed phrase in text file inside
   ├─ Save container to multiple USB drives
   └─ Store USB drives in separate locations

2. GPG Encryption:
   ├─ Generate GPG key pair
   ├─ Encrypt seed phrase file
   ├─ Store encrypted file on USB
   ├─ Backup GPG private key separately
   └─ Requires GPG knowledge

3. Password Manager (Offline):
   ├─ Use offline password manager (KeePassXC)
   ├─ Store seed phrase as secure note
   ├─ Use strong master password
   ├─ Backup database file to USB
   └─ Never sync to cloud

CRITICAL RULES:
├─ NEVER store unencrypted on computer
├─ NEVER upload to cloud (Google Drive, Dropbox, etc.)
├─ NEVER email to yourself
├─ NEVER store in browser password manager
└─ Encryption passphrase must be backed up separately
```

### Geographic Distribution

**Multi-Location Strategy**:

```
3-Location Minimum:

Location 1: Home Safe
├─ Metal backup (primary)
├─ Quick access for recovery
├─ Fireproof safe
└─ Risk: Burglary, fire, natural disaster

Location 2: Bank Safe Deposit Box
├─ Metal backup (secondary)
├─ Highly secure
├─ Fireproof, theft-resistant
└─ Risk: Bank hours, government seizure

Location 3: Trusted Person
├─ Paper backup in sealed envelope
├─ Trusted family member or attorney
├─ Geographic diversity (different city/state)
└─ Risk: Trust, their security practices

Optional Location 4: Second Bank
├─ Different bank, different city
├─ Ultimate redundancy
├─ Protects against single bank issues
└─ Cost: Additional safe deposit box fee

Considerations:
├─ Locations should be geographically diverse
├─ Different risk profiles (home vs. bank vs. person)
├─ Balance security with accessibility
└─ Document locations (in will, with executor)
```

**Shamir's Secret Sharing Distribution**:

```
5-of-8 Shares Example:

Share Distribution:
├─ Share 1: Home safe
├─ Share 2: Office safe
├─ Share 3: Bank safe deposit box #1
├─ Share 4: Bank safe deposit box #2
├─ Share 5: Trusted family member A
├─ Share 6: Trusted family member B
├─ Share 7: Attorney/executor
└─ Share 8: Friend in different country

Recovery Scenarios:
├─ Normal: Collect any 5 shares
├─ House fire: Still have 7 shares available
├─ Bank closure: Still have 6 shares available
├─ Family dispute: Can recover without specific person
└─ Incapacitation: Executor + family can recover

Security:
├─ No single location has enough shares
├─ No single person can access alone
├─ Redundancy against loss/destruction
└─ Requires coordination to recover (prevents impulsive decisions)
```

---

## Multi-Signature Implementations

### Bitcoin Multi-Sig

**Technical Implementation**:

```
P2SH Multi-Sig (Legacy):
├─ Pay-to-Script-Hash
├─ Addresses start with "3"
├─ Widely supported
└─ Higher fees than native SegWit

P2WSH Multi-Sig (SegWit):
├─ Pay-to-Witness-Script-Hash
├─ Addresses start with "bc1q"
├─ Lower fees
├─ Better privacy
└─ Recommended for new setups

P2TR Multi-Sig (Taproot):
├─ Pay-to-Taproot
├─ Addresses start with "bc1p"
├─ Best privacy (looks like single-sig)
├─ Lowest fees
└─ Requires Taproot-compatible wallets
```

**Setup with Electrum**:

```
2-of-3 Multi-Sig Setup:

1. Preparation:
   ├─ 3 hardware wallets (Ledger, Trezor, Coldcard)
   ├─ Electrum wallet software
   ├─ Secure computer
   └─ Backup materials

2. Create Multi-Sig Wallet:
   ├─ Open Electrum
   ├─ File → New/Restore
   ├─ Choose "Multi-signature wallet"
   ├─ Select 2-of-3 configuration
   └─ Add cosigners

3. Add Cosigners:
   ├─ Cosigner 1: Hardware wallet #1
   │   └─ Connect device, select account
   ├─ Cosigner 2: Hardware wallet #2
   │   └─ Connect device, select account
   └─ Cosigner 3: Hardware wallet #3
       └─ Connect device, select account

4. Verify Setup:
   ├─ Electrum generates multi-sig address
   ├─ Verify address on all hardware wallets
   ├─ Save wallet file (encrypted)
   └─ Backup wallet file and cosigner info

5. Transaction Signing:
   ├─ Create transaction in Electrum
   ├─ Sign with hardware wallet #1
   ├─ Sign with hardware wallet #2
   ├─ Broadcast (2 signatures sufficient)
   └─ Hardware wallet #3 not needed (but available)
```

**Key Management**:

```
2-of-3 Key Distribution:

Scenario A (Personal):
├─ Key 1: Daily-use hardware wallet (at home)
├─ Key 2: Backup hardware wallet (bank safe)
├─ Key 3: Trusted family member (different city)
└─ Can lose one key and still access funds

Scenario B (Business):
├─ Key 1: CEO hardware wallet
├─ Key 2: CFO hardware wallet
├─ Key 3: Company attorney
└─ Requires two officers to approve transactions

3-of-5 Key Distribution:

Scenario C (High Security):
├─ Key 1: Personal hardware wallet (daily use)
├─ Key 2: Backup hardware wallet (home safe)
├─ Key 3: Bank safe deposit box #1
├─ Key 4: Bank safe deposit box #2
├─ Key 5: Trusted executor (sealed envelope)
└─ Can lose two keys and still access funds
```

### Ethereum Multi-Sig (Gnosis Safe)

**Smart Contract Multi-Sig**:

```
Architecture:
├─ Funds held in smart contract (not EOA)
├─ Contract enforces M-of-N signature requirement
├─ Signers can be EOAs or other contracts
├─ Modular design (add features via modules)
└─ Supports hardware wallets as signers

Advantages over Bitcoin Multi-Sig:
├─ More flexible (can change signers, threshold)
├─ Advanced features (spending limits, time locks)
├─ Supports any ERC-20 token
├─ Can interact with DeFi protocols
└─ Upgradeable (via modules)

Disadvantages:
├─ Smart contract risk (bugs, exploits)
├─ Higher gas costs
├─ More complex to set up
└─ Requires understanding of Ethereum
```

**Advanced Features**:

```
Spending Limits:
├─ Daily limit: $10,000 (single signer)
├─ Above limit: Requires M-of-N signatures
└─ Reduces need for multi-sig on small transactions

Whitelisted Addresses:
├─ Pre-approved addresses (single signer)
├─ Unknown addresses (require multi-sig)
└─ Reduces risk of sending to wrong address

Time Locks:
├─ Propose transaction
├─ Wait 24-48 hours
├─ Execute if no objections
└─ Allows time to detect and prevent malicious transactions

Recovery Modules:
├─ Social recovery (friends/family can help recover)
├─ Time-locked recovery (after inactivity period)
├─ Guardian system (trusted contacts)
└─ Prevents permanent loss if keys lost

DeFi Integration:
├─ Stake directly from multi-sig
├─ Provide liquidity
├─ Interact with protocols
└─ All with multi-sig security
```

---

## Advanced Key Management

### Air-Gapped Signing

**Setup**:

```
Hardware Requirements:
├─ Computer #1: Online (watch-only wallet)
├─ Computer #2: Offline (signing wallet)
├─ USB drives or QR codes for data transfer
└─ Webcam (for QR code scanning)

Software:
├─ Electrum (Bitcoin)
├─ Sparrow Wallet (Bitcoin)
├─ Coldcard (hardware wallet with SD card)
└─ QR code libraries

Process:

1. Setup Phase:
   ├─ Generate seed on offline computer
   ├─ Export public keys (xpub)
   ├─ Transfer xpub to online computer (USB/QR)
   ├─ Create watch-only wallet on online computer
   └─ Verify addresses match

2. Transaction Creation:
   ├─ Create unsigned transaction on online computer
   ├─ Export as PSBT (Partially Signed Bitcoin Transaction)
   ├─ Transfer to offline computer (USB/QR/SD card)
   └─ Offline computer never connects to internet

3. Transaction Signing:
   ├─ Import PSBT on offline computer
   ├─ Review transaction details
   ├─ Sign with private key
   ├─ Export signed transaction
   └─ Transfer back to online computer

4. Broadcasting:
   ├─ Import signed transaction on online computer
   ├─ Broadcast to network
   ├─ Monitor confirmation
   └─ Offline computer never exposed
```

**Security Benefits**:

```
Protection Against:
├─ Malware (offline computer never infected)
├─ Remote attacks (no network connection)
├─ Keyloggers (no internet to exfiltrate data)
├─ Phishing (can't access fake websites)
└─ Most software-based attacks

Best For:
├─ Very large holdings (>$100K)
├─ Long-term storage
├─ Institutional custody
└─ Maximum security requirements

Trade-offs:
├─ Complex setup
├─ Inconvenient for frequent transactions
├─ Requires technical knowledge
└─ Dedicated hardware needed
```

### Threshold Signatures (MPC)

**Multi-Party Computation**:

```
How It Works:
├─ Private key never exists in complete form
├─ Split into shares during generation
├─ Shares distributed to multiple parties
├─ Signing requires M-of-N shares
└─ Shares combined cryptographically (not physically)

Advantages over Multi-Sig:
├─ Single signature on-chain (looks like regular transaction)
├─ Better privacy (can't tell it's multi-party)
├─ Lower fees (one signature vs. multiple)
├─ Works on any blockchain (not just those with multi-sig)
└─ More flexible key management

Disadvantages:
├─ More complex cryptography
├─ Newer technology (less battle-tested)
├─ Requires specialized software
└─ Coordination needed for signing

Providers:
├─ Fireblocks (institutional)
├─ Qredo (institutional)
├─ ZenGo (consumer wallet)
└─ Taurus (institutional)
```

**Use Cases**:

```
Institutional Custody:
├─ Bank holds one share
├─ Client holds one share
├─ Third-party holds one share
├─ Require 2-of-3 to sign
└─ No single party has full key

Exchange Hot Wallets:
├─ Multiple servers hold shares
├─ Require M-of-N to sign withdrawals
├─ Compromising one server insufficient
└─ Better security than single-key hot wallet

Consumer Wallets:
├─ User device holds share
├─ Cloud backup holds share
├─ Recovery contact holds share
├─ Require 2-of-3 to sign
└─ Lose device, still can recover
```

### Hardware Security Modules (HSMs)

**Enterprise Key Management**:

```
HSM Characteristics:
├─ Tamper-resistant hardware
├─ FIPS 140-2 Level 3/4 certified
├─ Keys never leave device
├─ Cryptographic operations in hardware
├─ Audit logging
└─ High availability

Use Cases:
├─ Exchange hot wallets
├─ Institutional custody
├─ Payment processors
├─ Validator signing keys
└─ High-volume transaction signing

Providers:
├─ AWS CloudHSM
├─ Azure Dedicated HSM
├─ Thales Luna HSM
├─ Utimaco HSM
└─ Gemalto SafeNet

Cost:
├─ Cloud HSM: $1-3/hour (~$1,000-2,000/month)
├─ On-premise: $10,000-50,000+ (one-time)
└─ Enterprise-only (not for individuals)
```

---

## Key Rotation and Migration

### When to Rotate Keys

```
Scheduled Rotation:
├─ Every 12-24 months (best practice)
├─ After major software updates
├─ When changing custody arrangements
└─ Compliance requirements

Emergency Rotation:
├─ Suspected key compromise
├─ Device theft or loss
├─ Employee departure (business)
├─ Divorce or relationship change
└─ Legal disputes

Technology Upgrade:
├─ Moving to hardware wallet
├─ Upgrading to multi-sig
├─ Changing wallet software
└─ Adopting new security features
```

### Migration Process

```
Safe Key Migration:

1. Preparation:
   ├─ Set up new wallet completely
   ├─ Verify new wallet works (test transaction)
   ├─ Backup new seed phrase
   ├─ Verify backups
   └─ Choose low-fee time (weekends for Bitcoin/Ethereum)

2. Transfer:
   ├─ Send small test amount first
   ├─ Verify receipt in new wallet
   ├─ Wait for confirmations
   ├─ Transfer remaining funds
   └─ Verify all funds received

3. Verification:
   ├─ Confirm all assets transferred
   ├─ Check for any remaining balances
   ├─ Verify transaction fees were reasonable
   └─ Save transaction hashes

4. Old Wallet Cleanup:
   ├─ Wait 30 days (ensure no issues)
   ├─ Securely destroy old seed phrase
   ├─ Wipe old devices
   ├─ Update documentation
   └─ Inform relevant parties (if business)

CRITICAL:
├─ NEVER destroy old seed until funds confirmed in new wallet
├─ ALWAYS send test transaction first
├─ VERIFY new wallet backup before transferring large amounts
└─ KEEP old wallet accessible for 30 days minimum
```
