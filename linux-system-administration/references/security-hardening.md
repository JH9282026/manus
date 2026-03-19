# Security Hardening

Hardening Linux servers for production.

## SSH Hardening

```bash
# /etc/ssh/sshd_config
Port 2222
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
AllowUsers user1 user2
MaxAuthTries 3
ClientAliveInterval 300
ClientAliveCountMax 2
```

## Firewall Configuration

```bash
# UFW
ufw default deny incoming
ufw default allow outgoing
ufw allow 2222/tcp
ufw allow 80/tcp
ufw allow 443/tcp
ufw enable
```

## Fail2Ban

```bash
apt install fail2ban

# /etc/fail2ban/jail.local
[sshd]
enabled = true
port = 2222
maxretry = 3
bantime = 3600
```
