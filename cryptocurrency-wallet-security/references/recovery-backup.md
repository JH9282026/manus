# Recovery and Backup Procedures

Comprehensive guide to wallet recovery, backup verification, disaster recovery planning, and cryptocurrency inheritance strategies.

---

## Wallet Recovery Procedures

### Seed Phrase Recovery

**Standard Recovery Process**:

```
Preparation:
├─ Obtain seed phrase from secure backup
├─ Verify backup is complete (12 or 24 words)
├─ Ensure words are from BIP39 wordlist
├─ Have wallet software ready
└─ Secure, private environment

Recovery Steps:

1. Download Wallet Software:
   ├─ Use official website only
   ├─ Verify download hash/signature
   ├─ Install on secure device
   └─ Preferably offline/air-gapped

2. Select "Restore" or "Import":
   ├─ Choose "Restore from seed phrase"
   ├─ Select correct word count (12/24)
   ├─ Enter words in exact order
   └─ Verify each word carefully

3. Enter Seed Phrase:
   ├─ Type each word exactly
   ├─ Watch for autocomplete suggestions
   ├─ Verify spelling (BIP39 wordlist)
   └─ Some wallets verify checksum automatically

4. Set New Password:
   ├─ Create strong password for wallet file
   ├─ Different from old password
   ├─ Store securely
   └─ This encrypts local wallet file only

5. Verify Recovery:
   ├─ Check addresses match expected
   ├─ Verify balances appear
   ├─ Check transaction history
   └─ Test sending small amount

6. Secure New Wallet:
   ├─ Backup new wallet file
   ├─ Enable 2FA if applicable
   ├─ Update security settings
   └─ Consider transferring to new seed (if compromised)
```

**Derivation Path Issues**:

```
Common Problem:
├─ Seed phrase correct, but balances don't appear
├─ Cause: Wrong derivation path
└─ Solution: Try different paths

Bitcoin Derivation Paths:
├─ BIP44 (Legacy): m/44'/0'/0'/0
├─ BIP49 (SegWit): m/49'/0'/0'/0
├─ BIP84 (Native SegWit): m/84'/0'/0'/0
└─ Try all three if unsure

Ethereum Derivation Paths:
├─ Standard: m/44'/60'/0'/0
├─ Ledger Live: m/44'/60'/0'/0/0
├─ Ledger Legacy: m/44'/60'/0'
└─ MetaMask: m/44'/60'/0'/0/0

Troubleshooting:
1. Try different wallet software
2. Check derivation path settings
3. Use wallet that supports custom paths
4. Consult original wallet documentation
5. Use blockchain explorer to search addresses
```

**Passphrase Recovery**:

```
With Passphrase (25th Word):

Scenario 1: Have Both Seed and Passphrase
├─ Enter seed phrase
├─ Enter passphrase when prompted
├─ Wallet derives correct addresses
└─ Funds accessible

Scenario 2: Have Seed, Forgot Passphrase
├─ Seed alone accesses different wallet
├─ If passphrase forgotten, funds LOST
├─ No recovery possible
├─ Try common passphrases you might have used
└─ Consider brute-force (if simple passphrase)

Scenario 3: Have Passphrase, Lost Seed
├─ Passphrase useless without seed
├─ Funds LOST
└─ No recovery possible

CRITICAL:
├─ Passphrase must be backed up separately
├─ No way to verify "correct" passphrase
├─ Every passphrase is valid (different wallet)
└─ Test recovery before funding wallet
```

### Hardware Wallet Recovery

**Ledger Recovery**:

```
Recovery Process:

1. Obtain Replacement Device:
   ├─ Purchase new Ledger (official store)
   ├─ Or use existing device
   └─ Verify authenticity

2. Initialize Device:
   ├─ Connect to computer
   ├─ Install Ledger Live
   ├─ Select "Restore from recovery phrase"
   └─ Choose 12, 18, or 24 words

3. Enter Seed Phrase:
   ├─ Use device buttons to select each word
   ├─ Verify on device screen
   ├─ Device validates checksum
   └─ Set new PIN

4. Install Apps:
   ├─ Install apps for your cryptocurrencies
   ├─ Bitcoin, Ethereum, etc.
   └─ Addresses will match original

5. Verify Recovery:
   ├─ Check addresses in Ledger Live
   ├─ Compare with old addresses
   ├─ Verify balances appear
   └─ Test small transaction

Passphrase Recovery:
├─ Enable passphrase in settings
├─ Enter passphrase when accessing
├─ Creates separate accounts
└─ Must remember passphrase
```

**Trezor Recovery**:

```
Recovery Process:

1. Initialize Device:
   ├─ Connect Trezor
   ├─ Go to trezor.io/start
   ├─ Select "Recover wallet"
   └─ Choose word count

2. Enter Seed Phrase:
   ├─ Type words on computer (Trezor One)
   ├─ Or use touchscreen (Trezor Model T)
   ├─ Device validates checksum
   └─ Set new PIN

3. Advanced Recovery (More Secure):
   ├─ Words entered in random order
   ├─ Protects against keyloggers
   ├─ Device shows position, you enter word
   └─ Recommended for Trezor One

4. Shamir Backup Recovery (Model T):
   ├─ Enter required number of shares
   ├─ Device combines shares
   ├─ Reconstructs seed
   └─ Set new PIN

5. Verify Recovery:
   ├─ Check addresses match
   ├─ Verify balances
   └─ Test transaction
```

---

## Backup Verification

### Testing Recovery Process

**Annual Recovery Drill**:

```
Why Test Recovery:
├─ Verify backup is readable
├─ Ensure you remember process
├─ Catch errors before emergency
├─ Verify all backups are accessible
└─ Practice reduces stress during real recovery

Test Procedure:

1. Preparation (1 hour):
   ├─ Schedule dedicated time
   ├─ Gather all backup materials
   ├─ Prepare test device/wallet
   ├─ Document the process
   └─ No distractions

2. Backup Retrieval (15 minutes):
   ├─ Access each backup location
   ├─ Home safe: Check metal/paper backup
   ├─ Bank: Retrieve from safe deposit box
   ├─ Trusted person: Verify they still have it
   └─ Document any access issues

3. Backup Verification (15 minutes):
   ├─ Check physical condition
   ├─ Verify all words are readable
   ├─ Check for damage (rust, fading, etc.)
   ├─ Verify word count (12/24)
   └─ Ensure words are from BIP39 wordlist

4. Recovery Test (30 minutes):
   ├─ Use test wallet or new device
   ├─ Enter seed phrase
   ├─ Verify addresses match
   ├─ Check balances appear
   ├─ Test sending small amount
   └─ Document any issues

5. Passphrase Test (if applicable):
   ├─ Verify passphrase backup accessible
   ├─ Test seed + passphrase recovery
   ├─ Verify correct wallet appears
   └─ Document passphrase location

6. Documentation (15 minutes):
   ├─ Record test date
   ├─ Note any issues found
   ├─ Update recovery instructions
   ├─ Schedule next test (1 year)
   └─ Store documentation securely

7. Cleanup:
   ├─ Wipe test device/wallet
   ├─ Return backups to secure locations
   ├─ Update any damaged backups
   └─ Verify all materials secured
```

**Backup Integrity Checklist**:

```
Physical Backup Inspection:

Metal Backup:
├─ [ ] No rust or corrosion
├─ [ ] All letters clearly stamped/engraved
├─ [ ] No missing tiles/letters
├─ [ ] Container intact (if applicable)
└─ [ ] Stored in fireproof/waterproof location

Paper Backup:
├─ [ ] Ink not faded
├─ [ ] Paper not degraded
├─ [ ] Lamination intact (if applicable)
├─ [ ] All words clearly readable
├─ [ ] No water damage
├─ [ ] Stored in protective envelope/bag
└─ [ ] In fireproof safe or equivalent

Encrypted Digital Backup:
├─ [ ] USB drive functional
├─ [ ] Can decrypt file
├─ [ ] Encryption password remembered/accessible
├─ [ ] Multiple copies exist
└─ [ ] Stored offline

Seed Phrase Verification:
├─ [ ] Correct word count (12/24)
├─ [ ] All words from BIP39 wordlist
├─ [ ] Words numbered/ordered
├─ [ ] Checksum valid (if tested)
└─ [ ] Matches across all backups
```

### Backup Update Procedures

**When to Update Backups**:

```
Required Updates:
├─ Created new wallet (new seed phrase)
├─ Added passphrase to existing wallet
├─ Changed multi-sig configuration
├─ Backup damaged or degraded
└─ Moved to new wallet type

Optional Updates:
├─ Annual refresh (replace paper with metal)
├─ Changed backup locations
├─ Added redundant backups
└─ Improved backup method

Update Process:

1. Create New Backup:
   ├─ Prepare new backup materials
   ├─ Write/stamp seed phrase
   ├─ Verify accuracy
   └─ Test recovery

2. Distribute New Backups:
   ├─ Place in secure locations
   ├─ Update documentation
   └─ Inform trusted parties (if applicable)

3. Destroy Old Backups:
   ├─ ONLY after verifying new backups work
   ├─ Shred paper backups
   ├─ Destroy metal backups (melt, grind)
   ├─ Wipe digital backups (secure erase)
   └─ Document destruction

4. Update Documentation:
   ├─ Record new backup locations
   ├─ Update recovery instructions
   ├─ Inform executor/trusted parties
   └─ Update will (if applicable)
```

---

## Disaster Recovery Planning

### Disaster Scenarios

**House Fire**:

```
Risk:
├─ Home safe may not protect against extreme heat
├─ Paper backups destroyed
├─ Hardware wallets melted
└─ Computer/phone destroyed

Mitigation:

1. Fireproof Storage:
   ├─ Metal seed backup (survives most fires)
   ├─ Fireproof safe (rated 1-2 hours)
   ├─ Bank safe deposit box (off-site)
   └─ Multiple locations

2. Off-Site Backups:
   ├─ Bank safe deposit box
   ├─ Trusted family member (different city)
   ├─ Second property
   └─ Attorney's office