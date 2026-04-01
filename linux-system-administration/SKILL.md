---
name: linux-system-administration
description: "Master Linux system administration including server management, automation, security hardening, and performance tuning. Use for: managing Linux servers, automating system tasks, implementing security best practices, monitoring system performance, managing users and permissions, configuring services, troubleshooting issues, and deploying production systems."
---

# Linux System Administration

Master Linux server management, automation, security, and performance optimization for production systems.

## Overview

Linux system administration encompasses server management, user administration, security hardening, performance tuning, and automation. This skill covers essential commands, best practices, and advanced techniques for managing production Linux systems.

## Core System Management

### System Information

```bash
# System info
uname -a                    # Kernel version
hostnamectl                 # System hostname and OS
lsb_release -a             # Distribution info
uptime                     # System uptime
cat /proc/cpuinfo          # CPU information
free -h                    # Memory usage
df -h                      # Disk usage
lsblk                      # Block devices

# Hardware info
lscpu                      # CPU architecture
lsmem                      # Memory ranges
lspci                      # PCI devices
lsusb                      # USB devices
```

### Process Management

```bash
# View processes
ps aux                     # All processes
ps -ef                     # Full format
top                        # Interactive process viewer
htop                       # Enhanced top
pstree                     # Process tree

# Process control
kill <PID>                 # Terminate process
kill -9 <PID>              # Force kill
killall <name>             # Kill by name
pkill <pattern>            # Kill by pattern

# Background jobs
command &                  # Run in background
jobs                       # List jobs
fg %1                      # Bring to foreground
bg %1                      # Resume in background
nohup command &            # Run immune to hangups
```

### Service Management (systemd)

```bash
# Service control
systemctl start nginx
systemctl stop nginx
systemctl restart nginx
systemctl reload nginx
systemctl enable nginx     # Start on boot
systemctl disable nginx
systemctl status nginx

# View logs
journalctl -u nginx        # Service logs
journalctl -f              # Follow logs
journalctl --since "1 hour ago"
journalctl -p err          # Error level

# Create service
cat > /etc/systemd/system/myapp.service << 'EOF'
[Unit]
Description=My Application
After=network.target

[Service]
Type=simple
User=appuser
WorkingDirectory=/opt/myapp
ExecStart=/opt/myapp/start.sh
Restart=always

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable myapp
systemctl start myapp
```

## User and Permission Management

### User Administration

```bash
# Create user
useradd -m -s /bin/bash username
passwd username

# Modify user
usermod -aG sudo username  # Add to sudo group
usermod -s /bin/zsh username  # Change shell

# Delete user
userdel -r username        # Remove with home directory

# User info
id username
groups username
finger username
```

### File Permissions

```bash
# Permission types: r(4) w(2) x(1)
chmod 755 file             # rwxr-xr-x
chmod 644 file             # rw-r--r--
chmod +x script.sh         # Add execute

# Ownership
chown user:group file
chown -R user:group directory

# Special permissions
chmod u+s file             # SUID
chmod g+s directory        # SGID
chmod +t directory         # Sticky bit

# ACLs (Access Control Lists)
setfacl -m u:username:rwx file
getfacl file
```

### sudo Configuration

```bash
# Edit sudoers
visudo

# Examples
username ALL=(ALL:ALL) ALL
%admin ALL=(ALL) ALL
username ALL=(ALL) NOPASSWD: /usr/bin/systemctl restart nginx
```

## Security Hardening

### SSH Configuration

```bash
# /etc/ssh/sshd_config
Port 2222                  # Change default port
PermitRootLogin no         # Disable root login
PasswordAuthentication no  # Use keys only
PubkeyAuthentication yes
AllowUsers user1 user2     # Whitelist users

# Restart SSH
systemctl restart sshd

# SSH keys
ssh-keygen -t ed25519 -C "email@example.com"
ssh-copy-id user@server
```

### Firewall (UFW)

```bash
# Enable firewall
ufw enable

# Allow services
ufw allow 22/tcp           # SSH
ufw allow 80/tcp           # HTTP
ufw allow 443/tcp          # HTTPS
ufw allow from 192.168.1.0/24 to any port 22

# Deny
ufw deny 23/tcp

# Status
ufw status verbose
```

### Firewall (iptables)

```bash
# List rules
iptables -L -n -v

# Allow SSH
iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# Allow HTTP/HTTPS
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT

# Drop all other input
iptables -P INPUT DROP

# Save rules
iptables-save > /etc/iptables/rules.v4
```

### Security Updates

```bash
# Ubuntu/Debian
apt update
apt upgrade
apt dist-upgrade
apt autoremove

# Enable automatic updates
apt install unattended-upgrades
dpkg-reconfigure -plow unattended-upgrades

# CentOS/RHEL
yum update
yum upgrade
```

## Performance Monitoring

### System Monitoring

```bash
# CPU usage
top
mpstat 1                   # CPU stats per second
sar -u 1 10                # CPU usage 10 times

# Memory
free -h
vmstat 1                   # Virtual memory stats
sar -r 1 10                # Memory usage

# Disk I/O
iostat -x 1                # Extended disk stats
iotop                      # I/O by process

# Network
iftop                      # Network bandwidth
nethogs                    # Network by process
ss -tuln                   # Socket statistics
netstat -tuln              # Network connections
```

### Log Analysis

```bash
# System logs
tail -f /var/log/syslog
tail -f /var/log/auth.log
journalctl -xe

# Application logs
tail -f /var/log/nginx/access.log
tail -f /var/log/nginx/error.log

# Search logs
grep "error" /var/log/syslog
grep -r "failed" /var/log/
```

## Automation

### Bash Scripting

```bash
#!/bin/bash

# Variables
NAME="John"
echo "Hello, $NAME"

# Functions
backup_files() {
    local source=$1
    local dest=$2
    tar -czf "$dest/backup-$(date +%Y%m%d).tar.gz" "$source"
}

# Conditionals
if [ -f "/etc/nginx/nginx.conf" ]; then
    echo "Nginx config exists"
fi

# Loops
for file in *.log; do
    gzip "$file"
done

# Error handling
set -e                     # Exit on error
set -u                     # Exit on undefined variable
set -o pipefail            # Exit on pipe failure
```

### Cron Jobs

```bash
# Edit crontab
crontab -e

# Examples
0 2 * * * /path/to/backup.sh           # Daily at 2 AM
*/15 * * * * /path/to/check.sh         # Every 15 minutes
0 0 * * 0 /path/to/weekly.sh           # Weekly on Sunday
@reboot /path/to/startup.sh            # On boot

# System-wide cron
/etc/cron.daily/
/etc/cron.weekly/
/etc/cron.monthly/
```

### Ansible Basics

```yaml
# playbook.yml
---
- name: Configure web servers
  hosts: webservers
  become: yes
  
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
        update_cache: yes
    
    - name: Start nginx
      service:
        name: nginx
        state: started
        enabled: yes
    
    - name: Copy config
      copy:
        src: nginx.conf
        dest: /etc/nginx/nginx.conf
      notify: Restart nginx
  
  handlers:
    - name: Restart nginx
      service:
        name: nginx
        state: restarted
```

## Troubleshooting

### Common Issues

```bash
# Disk full
df -h                      # Check disk usage
du -sh /*                  # Directory sizes
find / -type f -size +100M # Large files

# High CPU
top                        # Identify process
ps aux --sort=-%cpu | head # Top CPU processes
kill -9 <PID>              # Kill process

# High memory
free -h
ps aux --sort=-%mem | head
sync; echo 3 > /proc/sys/vm/drop_caches  # Clear cache

# Network issues
ping google.com
traceroute google.com
dig example.com
nslookup example.com
ss -tuln                   # Check listening ports
```

### System Recovery

```bash
# Boot into single-user mode
# Add 'single' or 'init=/bin/bash' to kernel parameters

# Reset root password
passwd root

# Check filesystem
fsck /dev/sda1

# Repair GRUB
grub-install /dev/sda
update-grub
```

## Backup and Recovery

```bash
# Tar backup
tar -czf backup.tar.gz /path/to/data

# Rsync backup
rsync -avz --delete /source/ /destination/
rsync -avz -e ssh /local/ user@remote:/remote/

# Database backup
mysqldump -u root -p database > backup.sql
pg_dump database > backup.sql

# Automated backup script
#!/bin/bash
BACKUP_DIR="/backups"
DATE=$(date +%Y%m%d)
tar -czf "$BACKUP_DIR/backup-$DATE.tar.gz" /var/www
find "$BACKUP_DIR" -mtime +7 -delete  # Delete old backups
```

## Using the Reference Files

### When to Read Each Reference

**`/references/security-hardening.md`** — Read when securing production servers, implementing security best practices, or conducting security audits.

**`/references/performance-tuning.md`** — Read when optimizing system performance, troubleshooting bottlenecks, or tuning kernel parameters.

**`/references/automation-scripts.md`** — Read when automating system tasks, creating deployment scripts, or implementing infrastructure as code.
