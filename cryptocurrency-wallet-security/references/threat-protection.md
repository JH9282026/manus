# Threat Protection and Defense

Comprehensive guide to identifying, preventing, and responding to cryptocurrency security threats including phishing, malware, social engineering, and physical attacks.

---

## Phishing Attack Defense

### Common Phishing Vectors

**Website Phishing**:

```
Typosquatting:
├─ Real: metamask.io
├─ Fake: metamаsk.io (Cyrillic 'а')
├─ Fake: metamask.com (wrong TLD)
├─ Fake: meta-mask.io (hyphen)
└─ Fake: metarnask.io (rn looks like m)

Homograph Attacks:
├─ Use similar-looking characters
├─ Cyrillic, Greek letters that look like Latin
├─ Example: "а" (Cyrillic) vs "a" (Latin)
└─ Browsers show punycode (xn--) for some

Defense:
├─ Bookmark official sites
├─ Type URLs manually (don't click links)
├─ Verify SSL certificate
├─ Check for HTTPS
├─ Use browser extensions (MetaMask Phishing Detector)
└─ Enable punycode display in browser
```

**Email Phishing**:

```
Common Tactics:

1. Fake Security Alerts:
   Subject: "Urgent: Verify your wallet or lose access"
   ├─ Claims account will be locked
   ├─ Urgent action required
   ├─ Link to fake website
   └─ Asks for seed phrase or password

2. Fake Support:
   From: "support@coinbase.com" (spoofed)
   ├─ Claims to be from exchange
   ├─ Asks to verify account
   ├─ Requests sensitive information
   └─ May include official-looking logos

3. Fake Airdrops:
   Subject: "You've been selected for exclusive airdrop"
   ├─ Claims free tokens
   ├─ Requires wallet connection
   ├─ Malicious smart contract approval
   └─ Drains wallet

4. Tax/Legal Threats:
   Subject: "IRS: Unpaid crypto taxes - immediate action required"
   ├─ Impersonates government agency
   ├─ Threatens legal action
   ├─ Demands payment in crypto
   └─ Creates fear and urgency

Red Flags:
├─ Unsolicited contact
├─ Urgency ("Act now or lose access")
├─ Requests for seed phrase/private key
├─ Spelling/grammar errors
├─ Mismatched sender address
├─ Generic greetings ("Dear user")
└─ Too good to be true offers

Defense:
├─ Never click email links for crypto services
├─ Go directly to official website (bookmark)
├─ Verify sender email address (not just display name)
├─ Hover over links to see real URL
├─ Enable email authentication (SPF, DKIM, DMARC)
├─ Use separate email for crypto accounts
└─ Report phishing to service provider
```

**Social Media Phishing**:

```
Impersonation Accounts:

1. Fake Support:
   ├─ @MetaMaskSupport (fake)
   ├─ Real: MetaMask has NO support on Twitter DMs
   ├─ Responds to complaints/questions
   ├─ Asks to "verify" wallet
   └─ Requests seed phrase

2. Fake Giveaways:
   ├─ "Send 1 ETH, get 2 ETH back"
   ├─ Impersonates celebrities (Elon Musk, Vitalik)
   ├─ Fake verification checkmarks
   ├─ Bot comments ("I received my ETH!")
   └─ Scam address in bio

3. Fake Influencers:
   ├─ Similar username to real influencer
   ├─ Copied profile picture
   ├─ Promotes fake projects
   ├─ Shares malicious links
   └─ Asks for "investment" opportunities

Defense:
├─ Verify account is official (checkmark, follower count)
├─ No legitimate support asks for seed phrase
├─ No legitimate giveaway asks you to send first
├─ Check account creation date
├─ Look for subtle username differences
├─ Never trust DMs from "support"
└─ Report fake accounts
```

**Browser Extension Phishing**:

```
Fake Extensions:

1. Malicious MetaMask Clone:
   ├─ Similar name ("MetaMask Wallet Extension")
   ├─ Copied logo and description
   ├─ Fake reviews (bots)
   ├─ Steals seed phrase during "import"
   └─ Sends to attacker's server

2. Malicious Features:
   ├─ Clipboard hijacking (replaces addresses)
   ├─ Keylogging (captures passwords)
   ├─ Transaction manipulation
   ├─ Automatic approvals
   └─ Data exfiltration

Defense:
├─ Install ONLY from official browser stores
├─ Verify publisher name exactly
├─ Check number of users (millions for real MetaMask)
├─ Read recent reviews carefully
├─ Verify extension ID matches official
├─ Check permissions requested
└─ Use hardware wallet (immune to extension malware)

Official Extension IDs:
├─ MetaMask (Chrome): nkbihfbeogaeaoehlefnkodbefgpgknn
├─ Phantom (Chrome): bfnaelmomeimhlpmgjnjophhpkkoljpa
└─ Verify on official website before installing
```

### Phishing Detection Tools

```
Browser Extensions:

1. MetaMask Phishing Detector:
   ├─ Warns about known phishing sites
   ├─ Community-reported scams
   ├─ Blocks malicious contract interactions
   └─ Free, open-source

2. Pocket Universe:
   ├─ Transaction simulation
   ├─ Shows what will happen before signing
   ├─ Warns about suspicious contracts
   └─ Supports Ethereum, Polygon, etc.

3. Fire (by Chainpatrol):
   ├─ Real-time phishing detection
   ├─ Scam token warnings
   ├─ Malicious dApp alerts
   └─ Community-driven

Website Verification:

1. Check SSL Certificate:
   ├─ Click padlock in address bar
   ├─ Verify certificate owner
   ├─ Check expiration date
   └─ Look for Extended Validation (EV)

2. Use Official Links:
   ├─ CoinGecko/CoinMarketCap for project links
   ├─ Official Twitter/Discord for announcements
   ├─ Never trust Google Ads (often scams)
   └─ Bookmark frequently used sites

3. Contract Verification:
   ├─ Check on Etherscan/block explorer
   ├─ Verify contract is verified (source code)
   ├─ Check contract age and transaction count
   ├─ Look for audit reports
   └─ Compare with official contract address
```

---

## Malware Protection

### Cryptocurrency-Specific Malware

**Clipboard Hijackers**:

```
How It Works:
1. Malware monitors clipboard
2. Detects cryptocurrency address format
3. Replaces with attacker's address
4. User pastes attacker's address unknowingly
5. Sends funds to attacker

Address Formats Targeted:
├─ Bitcoin: 1..., 3..., bc1...
├─ Ethereum: 0x...
├─ Monero: 4..., 8...
└─ Others: Various formats

Defense:
├─ ALWAYS verify full address after pasting
├─ Check first AND last characters (not just first 4)
├─ Use address book for frequent recipients
├─ Send test transaction first
├─ Use hardware wallet (verify on device screen)
└─ Anti-malware software

Example:
You copy: 0x1234...5678
You paste: 0x9999...9999 (attacker's address)
└─ Looks similar at first glance, but different
```

**Keyloggers**:

```
What They Capture:
├─ Passwords
├─ Seed phrases (if typed)
├─ Private keys
├─ 2FA codes
└─ Any keyboard input

Defense:

1. Hardware Wallet (BEST):
   ├─ Seed phrase never typed on computer
   ├─ PIN entered on device
   ├─ Transactions signed on device
   └─ Immune to keyloggers

2. On-Screen Keyboard:
   ├─ Use for sensitive input
   ├─ Windows: osk.exe
   ├─ macOS: Accessibility Keyboard
   └─ Not foolproof (screen capture malware)

3. Password Manager:
   ├─ Auto-fill (no typing)
   ├─ Encrypted storage
   ├─ Master password only typed once
   └─ Use reputable manager (1Password, Bitwarden)

4. Anti-Malware:
   ├─ Real-time protection
   ├─ Regular scans
   ├─ Keep definitions updated
   └─ Malwarebytes, Bitdefender, etc.
```

**Fake Wallet Applications**:

```
Distribution Methods:
├─ Fake app stores
├─ Malicious ads (Google, social media)
├─ Phishing websites
├─ Compromised software repositories
└─ Trojanized legitimate apps

Malicious Behavior:
├─ Steals seed phrase during "import"
├─ Generates weak/predictable keys
├─ Sends funds to attacker
├─ Displays fake balances
└─ Modifies transaction recipients

Defense:

1. Official Sources Only:
   ├─ Download from official website
   ├─ Use official app stores (Apple, Google)
   ├─ Verify publisher name exactly
   └─ Check app permissions

2. Verify Before Installing:
   ├─ Check number of downloads
   ├─ Read recent reviews
   ├─ Verify app signature/hash
   ├─ Compare with official documentation
   └─ Look for verified badge

3. Test with Small Amount:
   ├─ Create new wallet
   ├─ Send small test amount
   ├─ Verify you can send/receive
   ├─ Test recovery process
   └─ Only then transfer larger amounts

Red Flags:
├─ Requests unnecessary permissions
├─ Poor reviews or no reviews
├─ Recently published (for established wallets)
├─ Spelling errors in app description
└─ Asks for seed phrase unexpectedly
```

**Remote Access Trojans (RATs)**:

```
Capabilities:
├─ Full remote control of computer
├─ Screen viewing/recording
├─ Keylogging
├─ File access
├─ Webcam/microphone access
└─ Can approve transactions, access wallets

Infection Vectors:
├─ Malicious email attachments
├─ Fake software downloads
├─ Compromised websites
├─ Social engineering
└─ Pirated software

Defense:

1. Prevention:
   ├─ Don't download unknown software
   ├─ Don't open suspicious email attachments
   ├─ Keep OS and software updated
   ├─ Use reputable antivirus
   └─ Enable firewall

2. Detection:
   ├─ Unusual network activity
   ├─ Unexpected CPU usage
   ├─ Unknown processes running
   ├─ Antivirus alerts
   └─ Unexplained system behavior

3. Mitigation:
   ├─ Use hardware wallet (immune to RATs)
   ├─ Dedicated device for crypto
   ├─ Virtual machine for risky activities
   ├─ Regular malware scans
   └─ Network monitoring
```

### Malware Defense Stack

**Operating System Hardening**:

```
Windows:
├─ Enable Windows Defender
├─ Keep Windows Update enabled
├─ Use standard user account (not admin)
├─ Enable firewall
├─ Disable unnecessary services
├─ Enable BitLocker (disk encryption)
└─ Use Windows Sandbox for untrusted apps

macOS:
├─ Enable Gatekeeper
├─ Keep macOS updated
├─ Enable FileVault (disk encryption)
├─ Use standard user account
├─ Enable firewall
├─ Disable unnecessary sharing services
└─ Use App Store apps when possible

Linux:
├─ Keep system updated (apt update && apt upgrade)
├─ Use AppArmor or SELinux
├─ Enable firewall (ufw)
├─ Encrypt home directory (LUKS)
├─ Use standard user account
├─ Verify package signatures
└─ Minimal software installation
```

**Antivirus/Anti-Malware**:

```
Recommended Solutions:

1. Malwarebytes:
   ├─ Excellent malware detection
   ├─ Real-time protection (Premium)
   ├─ Ransomware protection
   ├─ Free version for scans
   └─ $40/year Premium

2. Bitdefender:
   ├─ High detection rates
   ├─ Low system impact
   ├─ Anti-phishing
   ├─ Ransomware protection
   └─ $40-60/year

3. Windows Defender (Built-in):
   ├─ Free with Windows
   ├─ Good detection rates
   ├─ Real-time protection
   ├─ Regular updates
   └─ Sufficient for most users

4. ClamAV (Linux):
   ├─ Open-source
   ├─ Free
   ├─ Command-line and GUI
   └─ Regular signature updates

Best Practices:
├─ Enable real-time protection
├─ Schedule regular full scans (weekly)
├─ Keep definitions updated
├─ Scan downloads before opening
└─ Don't disable for "performance" (use hardware wallet instead)
```

**Browser Security**:

```
Secure Browser Configuration:

1. Browser Selection:
   ├─ Chrome (most tested for crypto)
   ├─ Firefox (privacy-focused)
   ├─ Brave (crypto-native, built-in wallet)
   └─ Avoid: Internet Explorer, outdated browsers

2. Essential Extensions:
   ├─ uBlock Origin (ad blocker)
   ├─ HTTPS Everywhere (force HTTPS)
   ├─ Privacy Badger (tracker blocker)
   └─ MetaMask Phishing Detector

3. Security Settings:
   ├─ Enable "Safe Browsing"
   ├─ Block pop-ups
   ├─ Disable auto-fill for passwords
   ├─ Clear cookies regularly
   └─ Use separate profile for crypto

4. Extension Hygiene:
   ├─ Minimize installed extensions
   ├─ Review permissions regularly
   ├─ Remove unused extensions
   ├─ Only install from official stores
   └─ Verify publisher before installing
```

---

## Social Engineering Defense

### Common Tactics

**Impersonation**:

```
Exchange Support Impersonation:

Scenario:
1. You tweet: "@Coinbase why is my withdrawal delayed?"
2. Fake account replies: "@CoinbaseSupport: DM us to resolve"
3. You DM, they ask for account details
4. They send phishing link or ask for 2FA code
5. Account compromised

Defense:
├─ Legitimate support NEVER DMs first
├─ Legitimate support NEVER asks for password/2FA
├─ Always contact through official channels
├─ Verify account is official (checkmark, followers)
└─ Report fake accounts

Wallet Developer Impersonation:

Scenario:
1. You post in Discord: "MetaMask not working"
2. DM from "MetaMask Support": "We can help"
3. They send link to "verify" wallet
4. Fake website asks for seed phrase
5. Wallet drained

Defense:
├─ Official support happens in public channels
├─ Never share seed phrase with anyone
├─ Verify URLs carefully
├─ Check Discord roles (official support has role)
└─ Report impersonators to moderators
```

**Urgency and Fear**:

```
Common Urgency Tactics:

1. "Account will be locked in 24 hours"
   ├─ Creates panic
   ├─ Bypasses rational thinking
   ├─ Pressures immediate action
   └─ Legitimate services give more time

2. "Suspicious activity detected"
   ├─ Implies account compromise
   ├─ Urges "verification"
   ├─ Links to phishing site
   └─ Real alerts come through official app/email

3. "Limited time offer - act now"
   ├─ FOMO (fear of missing out)
   ├─ Prevents due diligence
   ├─ Often fake airdrops/investments
   └─ Legitimate projects don't pressure

Defense:
├─ Slow down - urgency is a red flag
├─ Verify independently (official website/app)
├─ Don't click links in urgent messages
├─ Contact support through official channels
└─ If it's urgent, it's probably a scam
```

**Authority Exploitation**:

```
Fake Authority Figures:

1. Law Enforcement:
   ├─ "FBI: Your crypto is involved in illegal activity"
   ├─ Demands immediate payment/transfer
   ├─ Threatens arrest
   └─ Real law enforcement doesn't work this way

2. Tax Authorities:
   ├─ "IRS: Unpaid crypto taxes - pay now or face penalties"
   ├─ Demands payment in crypto
   ├─ Threatens legal action
   └─ IRS doesn't demand crypto payment

3. Exchange Executives:
   ├─ Impersonates CEO/founder
   ├─ Offers "exclusive" investment opportunity
   ├─ Asks for funds to be sent
   └─ Executives don't DM random users

Defense:
├─ Verify through official channels
├─ Government agencies don't demand crypto
├─ Consult attorney if legal threat
├─ Don't trust caller ID (can be spoofed)
└─ Hang up and call official number
```

**Trust and Reciprocity**:

```
Long-Con Scams:

1. Romance Scams:
   ├─ Build relationship over weeks/months
   ├─ Eventually ask for "help" with crypto
   ├─ "Investment opportunity" or "emergency"
   ├─ Victim sends crypto, scammer disappears
   └─ $1+ billion lost annually

2. Fake Mentorship:
   ├─ "Crypto expert" offers to teach
   ├─ Builds trust with small wins
   ├─ Eventually asks for larger "investment"
   ├─ Fake trading platform shows profits
   └─ Can't withdraw, funds stolen

3. Pig Butchering:
   ├─ Scammer "accidentally" messages you
   ├─ Builds friendship/romance
   ├─ Introduces to "profitable" crypto trading
   ├─ Fake platform shows huge returns
   ├─ Encourages larger investments
   └─ Eventually can't withdraw, all funds lost

Defense:
├─ Never send crypto to people you haven't met
├─ Be skeptical of unsolicited contact
├─ Verify trading platforms independently
├─ If returns seem too good, they are
└─ Consult trusted friend/family before large transfers
```

### Social Engineering Red Flags

```
Warning Signs:

├─ Unsolicited contact (DM, email, call)
├─ Urgency ("Act now or lose access")
├─ Requests for seed phrase/private key
├─ Requests for passwords or 2FA codes
├─ Too good to be true offers
├─ Pressure to act quickly
├─ Requests to keep secret
├─ Unusual payment methods
├─ Poor grammar/spelling (sometimes)
└─ Emotional manipulation

Golden Rules:

1. No legitimate service asks for seed phrase
2. No legitimate support DMs you first
3. No legitimate investment guarantees returns
4. No legitimate giveaway asks you to send first
5. When in doubt, verify independently
```

---

## Physical Security

### Device Security

**Mobile Device Protection**:

```
iPhone:
├─ Enable Face ID/Touch ID
├─ Set strong passcode (6+ digits)
├─ Enable "Erase Data" after 10 failed attempts
├─ Disable lock screen notifications (privacy)
├─ Enable Find My iPhone
├─ Keep iOS updated
├─ Use encrypted backups
└─ Don't jailbreak

Android:
├─ Enable fingerprint/face unlock
├─ Set strong PIN/password
├─ Enable device encryption
├─ Keep Android updated
├─ Use Google Play Protect
├─ Enable Find My Device
├─ Avoid rooting
└─ Use reputable manufacturer (Samsung, Google)

Wallet App Security:
├─ Enable app-level biometric lock
├─ Set transaction PIN
├─ Enable transaction confirmations
├─ Backup seed phrase offline
└─ Use separate device for large holdings
```

**Computer Security**:

```
Dedicated Crypto Computer (Ideal):
├─ Used ONLY for cryptocurrency
├─ No email, social media, gaming
├─ Minimal software installed
├─ No pirated software
├─ Regular malware scans
├─ Full disk encryption
└─ Physical security (locked room)

General Computer:
├─ Full disk encryption (BitLocker, FileVault)
├─ Strong password/PIN
├─ Automatic screen lock (5 minutes)
├─ Firewall enabled
├─ Antivirus/anti-malware
├─ Keep OS and software updated
├─ Use standard user account
└─ Separate browser profile for crypto
```

### Hardware Wallet Physical Security

```
Storage:
├─ Home safe (fireproof, waterproof)
├─ Bank safe deposit box
├─ Hidden location (not obvious)
└─ Separate from seed phrase backup

Tamper Detection:
├─ Check for physical damage
├─ Verify holographic seals (if present)
├─ Check firmware integrity
├─ Use passphrase for additional security
└─ Assume compromised if tampered

Travel:
├─ Don't carry large amounts
├─ Use passphrase (device alone is useless)
├─ Consider leaving device at home
├─ Use watch-only wallet for monitoring
└─ Be aware of border searches

Loss/Theft:
├─ Device alone can't access funds (need PIN)
├─ Recover using seed phrase
├─ Transfer funds to new wallet immediately
├─ Assume device compromised
└─ Report theft (for insurance)
```

### $5 Wrench Attack Defense

```
"Give me your crypto or I'll hit you with this wrench"

Physical Coercion Defense:

1. Plausible Deniability:
   ├─ Seed phrase alone: Small "decoy" amount
   ├─ Seed + passphrase: Real holdings
   ├─ Under duress, reveal seed only
   └─ Attacker gets decoy, you keep real funds

2. Duress PIN (Coldcard):
   ├─ Normal PIN: Access real wallet
   ├─ Duress PIN: Access decoy wallet
   ├─ Optionally wipes device
   └─ Attacker doesn't know difference

3. Multi-Sig:
   ├─ You control 1 of 3 keys
   ├─ Can't access funds alone
   ├─ Attacker gets nothing
   └─ Requires coordination with others

4. Time Locks:
   ├─ Withdrawals require 24-48 hour delay
   ├─ Gives time to alert authorities
   ├─ Can cancel pending transactions
   └─ Attacker can't get immediate access

5. Operational Security:
   ├─ Don't discuss holdings publicly
   ├─ Don't display wealth
   ├─ Use privacy coins for sensitive transactions
   ├─ Separate addresses for public/private
   └─ Consider personal security (if high net worth)

Reality:
├─ Best defense is not being a target
├─ Don't advertise holdings
├─ Physical security > all technical measures
└─ Consider professional security if necessary
```

---

## Network Security

### Public Wi-Fi Risks

```
Threats:
├─ Man-in-the-Middle attacks
├─ Packet sniffing
├─ Fake Wi-Fi hotspots
├─ Session hijacking
└─ Malware distribution

Defense:

1. Avoid Public Wi-Fi for Crypto:
   ├─ Use mobile data instead
   ├─ Tether to phone if needed
   └─ Wait until secure network

2. If Must Use Public Wi-Fi:
   ├─ Use VPN (NordVPN, ExpressVPN, Mullvad)
   ├─ Verify network name with staff
   ├─ Use HTTPS only (check padlock)
   ├─ Don't access sensitive accounts
   └─ Use hardware wallet (verify on device)

3. VPN Configuration:
   ├─ Enable kill switch
   ├─ Use strong encryption (AES-256)
   ├─ Choose reputable provider
   ├─ Avoid free VPNs (sell data)
   └─ Connect before accessing crypto
```

### Home Network Security

```
Router Hardening:

1. Change Default Credentials:
   ├─ Default admin password is public knowledge
   ├─ Use strong, unique password
   └─ Change default username if possible

2. Firmware Updates:
   ├─ Check for updates monthly
   ├─ Enable automatic updates if available
   └─ Replace if no longer supported

3. Encryption:
   ├─ Use WPA3 (or WPA2 if WPA3 unavailable)
   ├─ Strong Wi-Fi password (20+ characters)
   ├─ Disable WPS (vulnerable)
   └─ Hide SSID (minor security through obscurity)

4. Network Segmentation:
   ├─ Guest network for visitors
   ├─ IoT network for smart devices
   ├─ Main network for computers/phones
   └─ Crypto devices on separate VLAN (advanced)

5. Firewall:
   ├─ Enable router firewall
   ├─ Disable UPnP (security risk)
   ├─ Close unnecessary ports
   └─ Enable logging
```
