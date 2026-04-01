---
name: cryptocurrency-wallet-security
description: "Secure cryptocurrency wallets and protect digital assets from theft, loss, and unauthorized access. Use for implementing wallet security best practices, managing private keys, selecting secure wallet types, protecting against phishing and malware, setting up multi-signature wallets, implementing hardware wallet security, securing seed phrases, configuring two-factor authentication, defending against social engineering, and establishing recovery procedures."
---

# Cryptocurrency Wallet Security

Protect cryptocurrency holdings through comprehensive wallet security practices, private key management, and threat defense strategies.

## Overview

Cryptocurrency wallet security encompasses protecting the private keys that control access to digital assets. Unlike traditional banking, cryptocurrency transactions are irreversible and users bear full responsibility for security. This skill provides frameworks for selecting appropriate wallet types, implementing robust security controls, defending against common attack vectors, and establishing recovery procedures to prevent permanent loss of funds.

## Wallet Type Selection Matrix

**Security vs. Convenience Trade-offs**:

| Wallet Type | Security Level | Convenience | Best Use Case | Typical Holdings |
|-------------|---------------|-------------|---------------|------------------|
| **Hardware Wallet** | Very High | Low | Long-term storage, savings | >$10,000 |
| **Cold Storage (Paper/Metal)** | Very High | Very Low | Long-term hodling, inheritance | >$50,000 |
| **Software Wallet (Desktop)** | Medium | Medium | Regular transactions, trading | $1,000-$10,000 |
| **Mobile Wallet** | Medium | High | Daily spending, payments | $100-$1,000 |
| **Web Wallet (Non-Custodial)** | Medium-Low | High | DeFi interactions, NFTs | $500-$5,000 |
| **Exchange Wallet (Custodial)** | Low-Medium | Very High | Active trading only | Minimal (trading amount) |
| **Multi-Signature Wallet** | Very High | Low | Business, shared funds | Any amount |
| **Smart Contract Wallet** | High | Medium | Advanced features, recovery | $5,000+ |

**Wallet Selection Decision Tree**:

```
How much are you storing?
├─ <$100: Mobile wallet (MetaMask, Trust Wallet)
├─ $100-$1,000: Software wallet (Exodus, Electrum)
├─ $1,000-$10,000: Hardware wallet (Ledger, Trezor)
└─ >$10,000: Multiple hardware wallets + multi-sig

How often do you transact?
├─ Daily: Hot wallet (small amount) + Cold storage (majority)
├─ Weekly: Software wallet + Hardware wallet backup
├─ Monthly: Hardware wallet primary
└─ Rarely: Cold storage (paper/metal wallet)

What's your technical expertise?
├─ Beginner: Reputable hardware wallet (Ledger Nano S Plus)
├─ Intermediate: Hardware wallet + Software wallet combination
└─ Advanced: Multi-sig + Hardware wallets + Air-gapped setup

Business or personal?
├─ Personal: Hardware wallet or software wallet
└─ Business: Multi-signature wallet (Gnosis Safe, Casa)
```

## Private Key Management Framework

### Key Security Hierarchy

**Critical Principle**: Private keys = Complete control over funds. Loss or theft = Permanent loss.

```
Private Key Security Levels:

Level 1: NEVER DO
├─ Store in cloud storage (Google Drive, Dropbox, iCloud)
├─ Email to yourself
├─ Save in browser password manager
├─ Screenshot on phone/computer
├─ Store in plain text file
└─ Share with anyone (even "support")

Level 2: AVOID (High Risk)
├─ Store on internet-connected device
├─ Type into websites (except hardware wallet)
├─ Store in encrypted file on daily-use computer
└─ Keep single copy only

Level 3: ACCEPTABLE (Medium Risk)
├─ Encrypted password manager (offline backup)
├─ Software wallet on dedicated device
├─ Encrypted USB drive (multiple copies)
└─ Written on paper (single secure location)

Level 4: RECOMMENDED (Low Risk)
├─ Hardware wallet (Ledger, Trezor)
├─ Paper wallet (multiple secure locations)
├─ Metal backup (fireproof, waterproof)
└─ Multi-signature setup

Level 5: MAXIMUM SECURITY
├─ Multiple hardware wallets (different manufacturers)
├─ Multi-sig with geographically distributed keys
├─ Metal seed phrase backups (bank vault, safe)
├─ Air-gapped computer for signing
└─ Shamir's Secret Sharing for seed phrase
```

### Seed Phrase Protection

**12/24-Word Seed Phrase = Master Key to All Funds**

**Storage Best Practices**:

```
Physical Storage Methods:

1. Metal Backup (BEST for large holdings)
   ├─ Products: Cryptosteel, Billfodl, Blockplate
   ├─ Advantages: Fireproof, waterproof, corrosion-resistant
   ├─ Storage: Bank safe deposit box, home safe
   └─ Cost: $50-$150

2. Paper Backup (GOOD for medium holdings)
   ├─ Method: Write clearly with permanent ink
   ├─ Protection: Laminate, store in waterproof bag
   ├─ Storage: Multiple secure locations
   └─ Risk: Fire, water damage, degradation

3. Encrypted Digital Backup (ACCEPTABLE with precautions)
   ├─ Method: Encrypt with strong passphrase (VeraCrypt)
   ├─ Storage: Offline USB drives (multiple copies)
   ├─ Never: Cloud storage, email, online services
   └─ Risk: Encryption key loss, malware

Multiple Backup Strategy:
├─ Primary: Metal backup in home safe
├─ Secondary: Metal backup in bank safe deposit box
├─ Tertiary: Paper backup with trusted family (sealed envelope)
└─ Verification: Test recovery annually
```

**Seed Phrase Security Rules**:

1. **Never Digital**: Don't type, photograph, or store digitally
2. **Never Share**: No legitimate service will ever ask for seed phrase
3. **Verify Offline**: Write down during wallet setup, verify immediately
4. **Multiple Copies**: Store in 2-3 geographically separate locations
5. **Tamper Evidence**: Use sealed envelopes or tamper-evident bags
6. **Inheritance Planning**: Ensure trusted person can access if incapacitated

### Advanced Key Management

**Shamir's Secret Sharing** (for high-value holdings):

```
Split seed phrase into multiple shares (e.g., 5 shares, need 3 to recover)

Example Setup:
├─ Generate 5 shares from seed phrase
├─ Require any 3 shares to reconstruct seed
├─ Distribution:
│   ├─ Share 1: Home safe
│   ├─ Share 2: Bank safe deposit box
│   ├─ Share 3: Trusted family member
│   ├─ Share 4: Attorney/executor
│   └─ Share 5: Second bank location
└─ Security: No single location has enough to access funds

Supported by:
├─ Trezor Model T (native support)
├─ Ledger (via third-party tools)
└─ Software: SLIP-39 implementation
```

**Multi-Signature Wallets**:

```
Require M-of-N signatures to authorize transactions

Common Configurations:

2-of-3 (Personal/Small Business):
├─ Key 1: Hardware wallet (daily use)
├─ Key 2: Hardware wallet (secure backup)
├─ Key 3: Trusted partner/family member
└─ Benefit: Lose one key, still have access; one key compromised, funds safe

3-of-5 (Business/High Value):
├─ Key 1-3: Company officers (different hardware wallets)
├─ Key 4: Company attorney
├─ Key 5: Cold storage backup
└─ Benefit: Requires consensus, prevents single point of failure

Platforms:
├─ Gnosis Safe (Ethereum, most popular)
├─ Casa (Bitcoin, user-friendly)
├─ Electrum (Bitcoin, advanced)
└─ BitGo (Enterprise, custodial option)
```

## Authentication and Access Control

### Two-Factor Authentication (2FA)

**2FA Method Security Ranking**:

| Method | Security | Pros | Cons | Recommended For |
|--------|----------|------|------|----------------|
| **Hardware Security Key** | Highest | Phishing-resistant, no SIM swap risk | Cost, can be lost | All users (>$1K holdings) |
| **Authenticator App** | High | Offline, no SIM swap risk | Device loss risk | All users |
| **SMS** | Low | Convenient | SIM swap attacks, phishing | Avoid if possible |
| **Email** | Very Low | Universal | Email compromise | Never for crypto |

**Recommended 2FA Setup**:

```
Primary: Hardware Security Key (YubiKey, Titan Key)
├─ Register 2 keys (primary + backup)
├─ Store backup key in secure location
└─ Use for: Exchange accounts, email, password manager

Secondary: Authenticator App (Authy, Google Authenticator)
├─ Use encrypted backup (Authy)
├─ Store backup codes offline
└─ Use for: Wallets, DeFi platforms, secondary accounts

NEVER: SMS-based 2FA for cryptocurrency accounts
├─ Vulnerable to SIM swap attacks
├─ Attackers port your number to their device
└─ Bypass 2FA and drain accounts
```

### Biometric Security

**Fingerprint/Face ID for Mobile Wallets**:

```
Advantages:
├─ Convenient for frequent access
├─ Biometric data stored in secure enclave (iPhone, Android)
├─ Prevents shoulder surfing
└─ Quick transaction approval

Limitations:
├─ Not a replacement for seed phrase backup
├─ Device-specific (lose device = need seed phrase)
├─ Can be bypassed if device compromised
└─ Privacy concerns with biometric data

Best Practice:
├─ Enable for daily transactions (small amounts)
├─ Require additional PIN for large transactions
├─ Always maintain seed phrase backup
└─ Use hardware wallet for large holdings
```

## Threat Defense Strategies

### Phishing Attack Prevention

**Common Phishing Vectors**:

```
1. Fake Wallet Websites
   ├─ Attack: Typosquatting (metamask.com → metamаsk.com)
   ├─ Result: Download malware, enter seed phrase on fake site
   └─ Defense: Bookmark official sites, verify URLs carefully

2. Email Phishing
   ├─ Attack: "Verify your wallet" or "Security alert" emails
   ├─ Result: Click malicious link, enter credentials
   └─ Defense: Never click email links, go directly to official site

3. Social Media Impersonation
   ├─ Attack: Fake support accounts ("MetaMask Support")
   ├─ Result: Share seed phrase with "support"
   └─ Defense: No legitimate support will EVER ask for seed phrase

4. Airdrop Scams
   ├─ Attack: "Claim free tokens" requires wallet connection
   ├─ Result: Malicious contract drains wallet
   └─ Defense: Use burner wallet for unknown airdrops

5. Fake Browser Extensions
   ├─ Attack: Malicious MetaMask/wallet extension
   ├─ Result: Steals private keys, signs malicious transactions
   └─ Defense: Only install from official stores, verify publisher
```

**Phishing Defense Checklist**:

```markdown
Before Entering Credentials or Seed Phrase:

- [ ] Verify exact URL (check for typos, homoglyphs)
- [ ] Check for HTTPS and valid SSL certificate
- [ ] Confirm official domain (use bookmarks, not search)
- [ ] Verify sender email address (not just display name)
- [ ] Question urgency ("Act now!" is red flag)
- [ ] Never enter seed phrase on any website
- [ ] Use hardware wallet for transaction signing
- [ ] Verify contract address before approving

Red Flags:
- Unsolicited contact claiming to be support
- Requests for seed phrase, private key, or password
- Urgent action required ("Account will be locked")
- Too good to be true offers ("Free crypto")
- Spelling/grammar errors in official communications
- Mismatched sender email and display name
```

### Malware Protection

**Cryptocurrency-Targeting Malware**:

```
1. Clipboard Hijackers
   ├─ Attack: Replace copied wallet address with attacker's
   ├─ Result: Send funds to wrong address
   └─ Defense: Always verify full address before sending

2. Keyloggers
   ├─ Attack: Record keystrokes (passwords, seed phrases)
   ├─ Result: Steal credentials and private keys
   └─ Defense: Use hardware wallet, on-screen keyboard for sensitive input

3. Screen Capture Malware
   ├─ Attack: Screenshot seed phrases, QR codes
   ├─ Result: Steal wallet access
   └─ Defense: Cover screen when viewing seed phrase, use hardware wallet

4. Fake Wallet Apps
   ├─ Attack: Malicious wallet app in app store
   ├─ Result: Steal seed phrase during "setup"
   └─ Defense: Verify publisher, check reviews, use official links

5. Remote Access Trojans (RATs)
   ├─ Attack: Full remote control of device
   ├─ Result: Access wallets, approve transactions
   └─ Defense: Never install unknown software, use hardware wallet
```

**Malware Defense Stack**:

```
Operating System Level:
├─ Keep OS updated (Windows Update, macOS updates)
├─ Enable firewall
├─ Use standard user account (not admin) for daily use
└─ Enable full disk encryption

Antivirus/Anti-Malware:
├─ Install reputable antivirus (Malwarebytes, Bitdefender)
├─ Enable real-time protection
├─ Regular full system scans
└─ Keep definitions updated

Browser Security:
├─ Use reputable browser (Chrome, Firefox, Brave)
├─ Install ad blocker (uBlock Origin)
├─ Disable unnecessary extensions
├─ Clear cache/cookies regularly
└─ Use separate browser profile for crypto

Network Security:
├─ Avoid public Wi-Fi for crypto transactions
├─ Use VPN on untrusted networks
├─ Enable router firewall
└─ Change default router password

Hardware Wallet (BEST DEFENSE):
├─ Private keys never leave device
├─ Immune to computer malware
├─ Verify transaction details on device screen
└─ Use for all significant holdings
```

### Social Engineering Defense

**Common Social Engineering Tactics**:

```
1. Impersonation
   ├─ Tactic: Pretend to be exchange support, wallet developer
   ├─ Request: "Verify your account" or "Security check"
   └─ Defense: Contact support through official channels only

2. Urgency/Fear
   ├─ Tactic: "Your account will be locked in 24 hours"
   ├─ Request: Immediate action, bypass normal procedures
   └─ Defense: Slow down, verify independently

3. Authority
   ├─ Tactic: Claim to be law enforcement, tax authority
   ├─ Request: Payment in crypto, account access
   └─ Defense: Verify through official channels, consult attorney

4. Reciprocity
   ├─ Tactic: "I'll send you 1 BTC, you send back 2 BTC"
   ├─ Request: Send crypto first
   └─ Defense: If it sounds too good to be true, it is

5. Trust Exploitation
   ├─ Tactic: Build relationship over time, then request "help"
   ├─ Request: "Borrow" crypto, "investment opportunity"
   └─ Defense: Never send crypto to people you haven't met in person
```

**Social Engineering Defense Rules**:

1. **Verify Independently**: Always contact through official channels
2. **No Seed Phrase Sharing**: EVER, for ANY reason
3. **Slow Down**: Urgency is a red flag
4. **Question Authority**: Verify credentials independently
5. **No Unsolicited Help**: Legitimate support doesn't reach out first
6. **Trust but Verify**: Even with known contacts (account compromise)

## Operational Security Best Practices

### Transaction Security

**Pre-Transaction Checklist**:

```markdown
Before Sending Cryptocurrency:

- [ ] Verify recipient address (full address, not just first/last chars)
- [ ] Send small test transaction first (for large amounts)
- [ ] Check network fees (avoid overpaying)
- [ ] Verify correct network (ETH mainnet vs. BSC, etc.)
- [ ] Double-check amount (decimal places)
- [ ] Confirm transaction details on hardware wallet screen
- [ ] Save transaction hash for records
- [ ] Wait for sufficient confirmations

For Smart Contract Interactions:

- [ ] Verify contract address (use official source)
- [ ] Check contract on block explorer (verified source code)
- [ ] Review token approvals (use Revoke.cash to check)
- [ ] Understand what you're signing (read transaction details)
- [ ] Use burner wallet for unknown/risky contracts
- [ ] Set approval limits (not unlimited)
```

**Address Verification Methods**:

```
1. Full Address Comparison
   ├─ Compare entire address character-by-character
   ├─ Don't rely on first/last 4 characters only
   └─ Use multiple sources (email, website, direct message)

2. QR Code Scanning
   ├─ Scan QR code instead of typing
   ├─ Verify address after scanning (malware can replace)
   └─ Use camera on separate device if possible

3. Address Book
   ├─ Save frequently used addresses
   ├─ Verify once, use repeatedly
   └─ Review periodically for changes

4. ENS/Domain Names (Ethereum)

---

**Note:** This file was automatically condensed to meet the 500-line requirement. Additional content has been moved to the references/ folder.

## Using the Reference Files

- [./references/private-key-management.md](./references/private-key-management.md): Private Key Management
- [./references/recovery-backup.md](./references/recovery-backup.md): Recovery Backup
- [./references/threat-protection.md](./references/threat-protection.md): Threat Protection
- [./references/wallet-types-security.md](./references/wallet-types-security.md): Wallet Types Security

## References

- [Private Key Management](references/private-key-management.md)
- [Recovery Backup](references/recovery-backup.md)
- [Threat Protection](references/threat-protection.md)
- [Wallet Types Security](references/wallet-types-security.md)
