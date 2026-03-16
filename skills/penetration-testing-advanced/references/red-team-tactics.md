# Red Team Tactics

Advanced persistent threat simulation techniques.

## Initial Access

### Phishing
- Spear phishing emails
- Credential harvesting sites
- Malicious attachments
- Watering hole attacks

### Exploit Public-Facing
- Web application vulnerabilities
- VPN vulnerabilities
- Email server exploits

## Persistence

### Windows
- Registry Run keys
- Scheduled tasks
- WMI event subscriptions
- Service creation

### Linux
- Cron jobs
- .bashrc modifications
- Systemd services
- SSH keys

## Privilege Escalation

### Windows
- Token impersonation
- UAC bypass
- Kernel exploits
- Service misconfigurations

### Linux
- SUID binaries
- Sudo misconfigurations
- Kernel exploits
- Cron job abuse

## Defense Evasion

### Techniques
- Process injection
- DLL sideloading
- Obfuscation
- Living off the land (LOLBins)
- Disable security tools

### Tools
- Veil (payload generation)
- Invoke-Obfuscation (PowerShell)
- Donut (shellcode generation)

## Lateral Movement

### Methods
- PsExec
- WMI
- PowerShell remoting
- RDP
- SMB

### Tools
- Impacket suite
- CrackMapExec
- Evil-WinRM

## Exfiltration

### Channels
- DNS tunneling
- HTTPS
- Cloud storage
- Steganography

### Tools
- DNScat2
- Rclone
- Steghide