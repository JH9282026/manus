# Performance Tuning

Optimizing Linux system performance.

## Kernel Parameters

```bash
# /etc/sysctl.conf
net.core.somaxconn = 1024
net.ipv4.tcp_max_syn_backlog = 2048
net.ipv4.ip_local_port_range = 10000 65535
vm.swappiness = 10
fs.file-max = 100000
```

## Disk I/O Optimization

```bash
# Use deadline scheduler for SSDs
echo deadline > /sys/block/sda/queue/scheduler

# Disable access time updates
mount -o noatime,nodiratime /dev/sda1 /mnt
```

## Memory Tuning

```bash
# Clear cache
sync; echo 3 > /proc/sys/vm/drop_caches

# Adjust swappiness
sysctl vm.swappiness=10
```
