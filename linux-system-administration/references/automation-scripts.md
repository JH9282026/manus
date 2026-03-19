# Automation Scripts

Common automation scripts for system administration.

## Backup Script

```bash
#!/bin/bash
BACKUP_DIR="/backups"
DATE=$(date +%Y%m%d)
SOURCE="/var/www"

tar -czf "$BACKUP_DIR/backup-$DATE.tar.gz" "$SOURCE"
find "$BACKUP_DIR" -mtime +7 -delete

# Upload to S3
aws s3 cp "$BACKUP_DIR/backup-$DATE.tar.gz" s3://my-backups/
```

## Log Rotation

```bash
#!/bin/bash
LOG_DIR="/var/log/myapp"
find "$LOG_DIR" -name "*.log" -mtime +7 -exec gzip {} \;
find "$LOG_DIR" -name "*.gz" -mtime +30 -delete
```

## Health Check

```bash
#!/bin/bash
if ! systemctl is-active --quiet nginx; then
    systemctl start nginx
    echo "Nginx restarted" | mail -s "Alert" admin@example.com
fi
```
