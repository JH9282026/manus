# Wallet Types and Security Models

Comprehensive analysis of cryptocurrency wallet types, their security characteristics, setup procedures, and appropriate use cases.

---

## Hardware Wallets

### Security Architecture

**How Hardware Wallets Work**:

```
Security Model:

1. Key Generation
   ├─ Private keys generated on device (never exposed)
   ├─ True random number generator (TRNG)
   ├─ Seed phrase displayed on device screen only
   └─ Keys never leave secure element

2. Transaction Signing
   ├─ Computer sends unsigned transaction to device
   ├─ Device displays transaction details on screen
   ├─ User verifies and approves on device
   ├─ Device signs transaction with private key
   ├─ Signed transaction sent back to computer
   └─ Private key never exposed to computer

3. Secure Element
   ├─ Tamper-resistant chip (similar to credit cards)
   ├─ Encrypted storage
   ├─ PIN protection (wipes after failed attempts)
   └─ Firmware verification

Protection Against:
├─ Malware on computer (keys never exposed)
├─ Phishing (verify on device screen)
├─ Remote attacks (requires physical access)
└─ Keyloggers (PIN entered on device)
```

### Leading Hardware Wallets

**Ledger Nano S Plus / Nano X**:

```
Specifications:
├─ Secure Element: CC EAL5+ certified
├─ Screen: Yes (verify transactions)
├─ Connectivity: USB-C (S Plus), Bluetooth (X)
├─ Supported Coins: 5,500+
├─ Price: $79 (S Plus), $149 (X)
└─ Open Source: Partially (apps open, OS closed)

Security Features:
├─ PIN protection (8 digits)
├─ Passphrase support (25th word)
├─ Firmware attestation
├─ Secure boot
└─ Anti-tamper mechanisms

Setup Process:
1. Purchase from official Ledger store only
2. Verify packaging is sealed and intact
3. Initialize device (generate new seed or restore)
4. Write down 24-word seed phrase (on provided card)
5. Verify seed phrase (device prompts random words)
6. Set PIN (8 digits)
7. Install Ledger Live software
8. Install apps for desired cryptocurrencies
9. Verify addresses match on device and computer

Best Practices:
├─ Never enter seed phrase on computer
├─ Verify receiving addresses on device screen
├─ Keep firmware updated
├─ Use passphrase for additional security
└─ Store seed phrase in multiple secure locations

Known Issues:
├─ 2020 customer data breach (names, addresses leaked)
├─ Closed-source secure element firmware
└─ Bluetooth on Nano X (disable if not needed)
```

**Trezor Model One / Model T**:

```
Specifications:
├─ Secure Element: No (general-purpose MCU)
├─ Screen: Yes, touchscreen (Model T)
├─ Connectivity: USB-C
├─ Supported Coins: 1,800+
├─ Price: $69 (One), $219 (T)
└─ Open Source: Fully (hardware and software)

Security Features:
├─ PIN protection (up to 50 digits)
├─ Passphrase support
├─ Shamir Backup (Model T)
├─ SD card encryption (Model T)
└─ Open-source auditable code

Advantages:
├─ Fully open-source (community auditable)
├─ Shamir's Secret Sharing (split seed)
├─ Touchscreen (Model T, easier to use)
└─ No Bluetooth (no wireless attack surface)

Disadvantages:
├─ No secure element (vulnerable to physical attacks)
├─ Passphrase required for maximum security
└─ Fewer supported coins than Ledger

Best For:
├─ Privacy advocates (open source)
├─ Users wanting Shamir backup
└─ Bitcoin/Ethereum focus
```

**Coldcard (Bitcoin-Only)**:

```
Specifications:
├─ Secure Element: Yes (Microchip ATECC608A)
├─ Screen: Yes (OLED)
├─ Connectivity: USB, SD card, air-gapped
├─ Supported Coins: Bitcoin only
├─ Price: $147
└─ Open Source: Yes

Security Features:
├─ Air-gapped operation (no USB connection needed)
├─ Duress PIN (decoy wallet)
├─ Brick-me PIN (destroy device)
├─ Secure element + general MCU
├─ Tamper-evident bag
└─ Dice roll entropy for seed generation

Advanced Features:
├─ PSBT (Partially Signed Bitcoin Transactions)
├─ Multisig coordination
├─ SD card for transaction transfer
├─ Encrypted backups
└─ Verifiable firmware

Best For:
├─ Bitcoin maximalists
├─ Maximum security requirements
├─ Air-gapped setups
└─ Advanced users
```

### Hardware Wallet Security Best Practices

**Purchase and Setup**:

```
Purchasing:
├─ Buy ONLY from official manufacturer website
├─ NEVER buy from Amazon, eBay, or third parties
├─ Verify packaging is sealed and intact
├─ Check for tamper-evident seals
└─ Verify device authenticity (manufacturer provides method)

Initial Setup:
├─ Generate new seed (don't use pre-generated)
├─ Write seed phrase on provided card (or metal backup)
├─ NEVER photograph or type seed phrase
├─ Verify seed phrase (device will test you)
├─ Set strong PIN (8+ digits)
└─ Consider adding passphrase (25th word)

Ongoing Use:
├─ Always verify addresses on device screen
├─ Keep firmware updated (verify signatures)
├─ Use official wallet software only
├─ Store device in secure location when not in use
└─ Test recovery process with small amount first
```

**Passphrase (25th Word) Strategy**:

```
How It Works:
├─ 24-word seed + passphrase = different wallet
├─ Each passphrase creates unique wallet
├─ No "wrong" passphrase (all are valid)
└─ Provides plausible deniability

Use Cases:

1. Duress Wallet
   ├─ Seed phrase alone: Small "decoy" amount
   ├─ Seed + passphrase: Real holdings
   └─ Under duress, reveal seed only

2. Multiple Wallets
   ├─ Passphrase A: Long-term holdings
   ├─ Passphrase B: Trading funds
   └─ Passphrase C: Experimental/DeFi

3. Inheritance
   ├─ Seed phrase: In will/safe deposit box
   ├─ Passphrase: Memorized or separate location
   └─ Requires both to access funds

Security Considerations:
├─ Passphrase must be backed up separately
├─ Losing passphrase = losing funds (no recovery)
├─ Use strong, memorable passphrase
└─ Don't store passphrase with seed phrase
```

---

## Software Wallets

### Desktop Wallets

**Electrum (Bitcoin)**:

```
Features:
├─ Lightweight (SPV, doesn't download full blockchain)
├─ Hardware wallet integration
├─ Multi-signature support
├─ Replace-by-fee (RBF)
├─ Cold storage mode
└─ Open source

Security:
├─ Encrypted wallet file
├─ Password protection
├─ Seed phrase backup (12 words)
├─ Watch-only mode
└─ Offline transaction signing

Setup:
1. Download from official electrum.org only
2. Verify GPG signature
3. Install and create new wallet
4. Write down seed phrase (12 words)
5. Set strong password
6. Encrypt wallet file

Best Practices:
├─ Use with hardware wallet for large amounts
├─ Enable 2FA for online wallets
├─ Verify receiving addresses
├─ Keep software updated
└─ Use on dedicated computer if possible
```

**Exodus (Multi-Currency)**:

```
Features:
├─ User-friendly interface
├─ Built-in exchange
├─ 260+ supported assets
├─ Portfolio tracking
├─ Hardware wallet integration (Trezor)
└─ Mobile + desktop sync

Security:
├─ Password protection
├─ 12-word seed phrase
├─ Local key storage (non-custodial)
├─ Encrypted private keys
└─ No account creation required

Limitations:
├─ Closed source (less auditable)
├─ No multi-signature
├─ No advanced features
└─ Built-in exchange has fees

Best For:
├─ Beginners
├─ Multi-currency portfolios
├─ Users wanting simple interface
└─ Medium holdings ($1K-$10K)
```

### Mobile Wallets

**MetaMask (Ethereum/EVM)**:

```
Features:
├─ Browser extension + mobile app
├─ DeFi/dApp integration
├─ Hardware wallet support
├─ Multi-network (Ethereum, BSC, Polygon, etc.)
├─ Token swaps
└─ NFT support

Security:
├─ Password protection
├─ 12-word seed phrase
├─ Biometric unlock (mobile)
├─ Transaction simulation (shows outcome)
└─ Phishing detection

Security Risks:
├─ Browser extension (malware risk)
├─ Phishing attacks (fake websites)
├─ Malicious dApp connections
├─ Unlimited token approvals
└─ Clipboard hijacking

Best Practices:
├─ Use for small amounts only
├─ Revoke unused token approvals (revoke.cash)
├─ Verify contract addresses
├─ Use hardware wallet for signing
├─ Separate browser profile for crypto
└─ Never enter seed phrase on websites
```

**Trust Wallet (Mobile)**:

```
Features:
├─ Multi-chain support (65+ blockchains)
├─ Built-in dApp browser
├─ Staking support
├─ NFT gallery
├─ WalletConnect integration
└─ Binance-owned

Security:
├─ Non-custodial (you control keys)
├─ Biometric authentication
├─ 12-word seed phrase
├─ Encrypted key storage
└─ Security audits

Best For:
├─ Mobile-first users
├─ Multi-chain portfolios
├─ DeFi interactions
└─ Small to medium holdings

Security Considerations:
├─ Mobile device security critical
├─ Backup seed phrase offline
├─ Enable biometric + PIN
├─ Be cautious with dApp connections
└─ Use for daily spending amounts only
```

---

## Cold Storage Solutions

### Paper Wallets

**Creation Process (Bitcoin)**:

```
Secure Paper Wallet Generation:

1. Preparation
   ├─ Use air-gapped computer (never connected to internet)
   ├─ Boot from live USB (Tails, Ubuntu)
   ├─ Disconnect all network connections
   └─ Use trusted paper wallet generator

2. Generation
   ├─ Download generator (bitaddress.org for Bitcoin)
   ├─ Verify source code hash
   ├─ Run offline
   ├─ Generate random private key
   └─ Print private key + public address

3. Printing
   ├─ Use non-networked printer
   ├─ Print multiple copies
   ├─ Consider using BIP38 encryption
   └─ Clear printer memory after

4. Storage
   ├─ Laminate paper (water protection)
   ├─ Store in fireproof safe
   ├─ Multiple geographic locations
   └─ Consider metal backup for long-term

5. Cleanup
   ├─ Shut down computer
   ├─ Destroy live USB (or keep for future use)
   └─ Never use that computer online again (if dedicated)
```

**Security Considerations**:

```
Advantages:
├─ Completely offline (immune to hacking)
├─ No hardware to fail
├─ Inexpensive
└─ Full control

Disadvantages:
├─ Vulnerable to physical damage (fire, water)
├─ Difficult to spend from (must import to software wallet)
├─ Importing exposes key (should only use once)
├─ Printer may store data
└─ Ink can fade over time

Best For:
├─ Long-term storage (years)
├─ Inheritance/gifts
├─ One-time large transfers
└─ Users comfortable with technical process

NOT Recommended For:
├─ Frequent transactions
├─ Beginners
├─ Large amounts (use hardware wallet instead)
└─ Long-term storage (metal backup better)
```

### Metal Seed Backups

**Commercial Solutions**:

```
Cryptosteel Capsule:
├─ Stainless steel capsule
├─ Letter tiles for seed words
├─ Fireproof (up to 1400°C)
├─ Waterproof, corrosion-resistant
├─ Price: ~$100
└─ Capacity: 24 words

Billfodl:
├─ Stainless steel plates
├─ Letter tiles in slots
├─ Fireproof (up to 1500°C)
├─ Crush-resistant
├─ Price: ~$80
└─ Capacity: 24 words

Blockplate:
├─ Titanium plate
├─ Stamp or engrave words
├─ Fireproof (up to 1668°C)
├─ Extremely durable
├─ Price: ~$50
└─ DIY stamping required

Cobo Tablet:
├─ Stainless steel grid
├─ Punch dots to encode words
├─ Fireproof, waterproof
├─ Compact design
├─ Price: ~$40
└─ Requires decoding (more private)
```

**DIY Metal Backup**:

```
Materials:
├─ Stainless steel or titanium plate
├─ Metal stamping kit
├─ Protective eyewear
└─ Secure workspace

Process:
1. Purchase metal plate (hardware store)
2. Clean and prepare surface
3. Stamp seed words clearly
4. Verify readability
5. Store in fireproof safe

Advantages:
├─ Inexpensive ($10-20)
├─ Customizable
├─ No third-party involvement
└─ Extremely durable

Considerations:
├─ Requires physical effort
├─ Permanent (can't erase mistakes)
├─ Stamping must be clear and deep
└─ Store securely (anyone who sees it has access)
```

---

## Multi-Signature Wallets

### Gnosis Safe (Ethereum)

**Architecture**:

```
Smart Contract Wallet:
├─ Funds held in smart contract (not EOA)
├─ Requires M-of-N signatures to execute
├─ Signers can be EOAs or other contracts
├─ Supports hardware wallets as signers
└─ Modular design (plugins for features)

Common Configurations:

2-of-3 Personal:
├─ Signer 1: Hardware wallet (daily use)
├─ Signer 2: Hardware wallet (backup)
├─ Signer 3: Trusted family/friend
└─ Use: Personal savings, family funds

3-of-5 Business:
├─ Signer 1-3: Company officers
├─ Signer 4: Company attorney
├─ Signer 5: Cold storage backup
└─ Use: Company treasury, DAO funds

4-of-7 DAO:
├─ Signers: Elected community members
├─ Rotation: Regular elections
├─ Transparency: All transactions public
└─ Use: Decentralized organization funds
```

**Setup Process**:

```
1. Navigate to app.safe.global
2. Connect wallet (will be first signer)
3. Select network (Ethereum, Polygon, etc.)
4. Choose number of signers and threshold
5. Add signer addresses
6. Review and deploy Safe contract
7. Pay deployment gas fee
8. Share Safe address with other signers
9. Other signers add Safe to their interface

Transaction Flow:
1. Any signer proposes transaction
2. Other signers review and approve
3. Once threshold met, anyone can execute
4. Execution pays gas fee
5. Transaction confirmed on-chain
```

**Security Benefits**:

```
Protection Against:
├─ Single key compromise (need M keys)
├─ Key loss (have N-M backup keys)
├─ Rogue insider (requires consensus)
├─ Coercion (can't act alone)
└─ Mistakes (multiple reviewers)

Additional Features:
├─ Spending limits (daily/per-transaction)
├─ Whitelisted addresses
├─ Time-locked transactions
├─ Recovery mechanisms
└─ Modular plugins (DeFi integrations)
```

### Casa (Bitcoin Multi-Sig)

**Service Model**:

```
Casa Keymaster Plans:

Basic (2-of-3):
├─ Key 1: Mobile device
├─ Key 2: Hardware wallet
├─ Key 3: Casa recovery key
├─ Cost: $120/year
└─ Use: Personal Bitcoin savings

Premium (3-of-5):
├─ Key 1: Mobile device
├─ Key 2-3: Hardware wallets
├─ Key 4: Casa recovery key
├─ Key 5: Lawyer/trusted contact
├─ Cost: $250/year
└─ Use: Significant Bitcoin holdings

Private Client (Custom):
├─ Fully customized setup
├─ Dedicated support
├─ Inheritance planning
├─ Cost: Custom pricing
└─ Use: High net worth individuals
```

**Advantages**:

```
User-Friendly:
├─ Guided setup process
├─ Mobile app interface
├─ Health checks and alerts
└─ 24/7 support

Security:
├─ Geographic key distribution
├─ Casa doesn't have unilateral access
├─ Regular security audits
└─ Inheritance features

Recovery:
├─ Casa recovery key (emergency)
├─ Doesn't require all keys
├─ Guided recovery process
└─ Prevents permanent loss
```

---

## Custodial vs. Non-Custodial

### Custodial Wallets (Exchanges)

**How They Work**:

```
Custodial Model:
├─ Exchange controls private keys
├─ You have account credentials (username/password)
├─ Funds held in exchange's wallets (pooled)
├─ You have IOU (claim on funds)
└─ Exchange must approve withdrawals

Examples:
├─ Coinbase
├─ Binance
├─ Kraken
├─ Gemini
└─ Most centralized exchanges
```

**Advantages**:

```
├─ Easy to use (familiar interface)
├─ Account recovery (forgot password)
├─ Customer support
├─ Insurance (some exchanges)
├─ Fiat on/off ramps
└─ Trading features
```

**Disadvantages**:

```
├─ Not your keys, not your coins
├─ Exchange can freeze account
├─ Exchange can be hacked (history of breaches)
├─ Regulatory seizure risk
├─ Withdrawal limits
├─ KYC/AML requirements
└─ Counterparty risk (exchange insolvency)
```

**When to Use**:

```
Acceptable:
├─ Active trading (small amounts)
├─ Fiat conversion
├─ Temporary holding during transactions
└─ Amounts you can afford to lose

NOT Recommended:
├─ Long-term storage
├─ Large amounts
├─ Savings/retirement funds
└─ Anything you can't afford to lose

Rule of Thumb:
└─ Keep only trading amount on exchange, rest in self-custody
```

### Non-Custodial Wallets

**Self-Custody Model**:

```
You Control:
├─ Private keys (seed phrase)
├─ All transactions
├─ No third-party approval needed
└─ Full sovereignty

Responsibilities:
├─ Secure key storage
├─ Backup management
├─ No account recovery (lose keys = lose funds)
├─ Transaction verification
└─ Security best practices
```

**Comparison Matrix**:

| Aspect | Custodial | Non-Custodial |
|--------|-----------|---------------|
| **Control** | Exchange | You |
| **Security Responsibility** | Exchange | You |
| **Recovery** | Possible (support) | Impossible (lost keys) |
| **Censorship Resistance** | Low | High |
| **Privacy** | Low (KYC) | High |
| **Ease of Use** | High | Medium |
| **Best For** | Trading | Holding |

**Recommendation**:

```
Hybrid Approach:

├─ 5-10%: Exchange (active trading)
├─ 10-20%: Hot wallet (frequent transactions)
└─ 70-85%: Cold storage (long-term holdings)

Security Increases:
Exchange < Hot Wallet < Hardware Wallet < Multi-Sig < Air-Gapped
```
