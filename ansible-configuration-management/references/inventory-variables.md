# Inventory and Variables

Inventory management, variable handling, facts, and secrets management with Ansible Vault.

---

## Static Inventory

### INI Format

```ini
# inventory/hosts

# Individual hosts
web1.example.com
web2.example.com
db1.example.com

# Hosts with variables
web3.example.com ansible_host=192.168.1.10 ansible_port=2222

# Host groups
[webservers]
web1.example.com
web2.example.com
web3.example.com

[databases]
db1.example.com
db2.example.com ansible_host=10.0.1.20

[monitoring]
monitor.example.com ansible_connection=local

# Group of groups
[production:children]
webservers
databases

[staging:children]
staging_web
staging_db

# Group variables
[webservers:vars]
ansible_user=deploy
http_port=80
max_clients=200

[databases:vars]
ansible_user=dbadmin
db_port=5432

[production:vars]
environment=production
backup_enabled=true
monitoring_enabled=true

# Host ranges
[web_cluster]
web[01:10].example.com

[db_cluster]
db-[a:f].example.com

# Numeric ranges with leading zeros
[app_servers]
app[001:100].example.com
```

### YAML Format

```yaml
# inventory/hosts.yml
all:
  children:
    webservers:
      hosts:
        web1.example.com:
        web2.example.com:
        web3.example.com:
          ansible_host: 192.168.1.10
          ansible_port: 2222
      vars:
        ansible_user: deploy
        http_port: 80
        max_clients: 200
    
    databases:
      hosts:
        db1.example.com:
        db2.example.com:
          ansible_host: 10.0.1.20
      vars:
        ansible_user: dbadmin
        db_port: 5432
    
    production:
      children:
        webservers:
        databases:
      vars:
        environment: production
        backup_enabled: true
        monitoring_enabled: true
    
    monitoring:
      hosts:
        monitor.example.com:
          ansible_connection: local
```

### Connection Variables

```ini
# SSH connection parameters
server1 ansible_host=192.168.1.10
server2 ansible_port=2222
server3 ansible_user=admin
server4 ansible_ssh_private_key_file=/path/to/key
server5 ansible_ssh_common_args='-o StrictHostKeyChecking=no'

# Python interpreter
server6 ansible_python_interpreter=/usr/bin/python3

# Become (privilege escalation)
server7 ansible_become=yes
server8 ansible_become_method=sudo
server9 ansible_become_user=root

# Connection type
local_server ansible_connection=local
windows_server ansible_connection=winrm
docker_container ansible_connection=docker
```

---

## Dynamic Inventory

### AWS EC2 Plugin

```yaml
# inventory/aws_ec2.yml
plugin: aws_ec2

# AWS regions to query
regions:
  - us-east-1
  - us-west-2
  - eu-west-1

# Filters to limit instances
filters:
  instance-state-name: running
  tag:Environment: production

# Create groups based on tags
keyed_groups:
  # Group by Environment tag
  - key: tags.Environment
    prefix: env
  # Group by instance type
  - key: instance_type
    prefix: type
  # Group by availability zone
  - key: placement.availability_zone
    prefix: az
  # Group by security group
  - key: security_groups | map(attribute='group_name') | list
    prefix: sg

# Compose custom variables
compose:
  ansible_host: public_ip_address
  ansible_user: "'ec2-user' if platform == 'amazon' else 'ubuntu'"
  environment: tags.Environment
  application: tags.Application

# Use strict mode to fail on errors
strict: False

# Cache settings
cache: yes
cache_plugin: jsonfile
cache_timeout: 3600
cache_connection: /tmp/aws_inventory
```

Usage:

```bash
# List inventory
ansible-inventory -i inventory/aws_ec2.yml --list

# Run playbook
ansible-playbook -i inventory/aws_ec2.yml site.yml

# Target specific group
ansible-playbook -i inventory/aws_ec2.yml site.yml --limit env_production
```

### Azure Plugin

```yaml
# inventory/azure_rm.yml
plugin: azure.azcollection.azure_rm

# Authentication (uses Azure CLI credentials by default)
auth_source: auto

# Include specific resource groups
include_vm_resource_groups:
  - production-rg
  - staging-rg

# Exclude powered-off VMs
exclude_host_filters:
  - powerstate != 'running'

# Create groups based on tags
keyed_groups:
  - prefix: tag
    key: tags
  - prefix: azure_loc
    key: location
  - prefix: azure_os
    key: os_profile.system

# Compose variables
compose:
  ansible_host: public_ipv4_addresses[0]
  ansible_user: "'azureuser'"
  environment: tags.environment

# Conditional groups
conditional_groups:
  production: tags.environment == "production"
  webservers: "'web' in tags.role"
  databases: "'db' in tags.role"
```

### GCP Plugin

```yaml
# inventory/gcp_compute.yml
plugin: google.cloud.gcp_compute

# GCP project
projects:
  - my-project-id

# Authentication
auth_kind: serviceaccount
service_account_file: /path/to/credentials.json

# Filters
filters:
  - status = RUNNING
  - labels.environment = production

# Create groups
keyed_groups:
  - key: labels.environment
    prefix: env
  - key: labels.role
    prefix: role
  - key: zone
    prefix: zone

# Compose variables
compose:
  ansible_host: networkInterfaces[0].accessConfigs[0].natIP
  ansible_user: "'ubuntu'"
  environment: labels.environment
```

### Custom Dynamic Inventory Script

```python
#!/usr/bin/env python3
# inventory/custom_inventory.py

import json
import sys

def get_inventory():
    """Return inventory data structure"""
    inventory = {
        'all': {
            'hosts': ['host1.example.com', 'host2.example.com'],
            'vars': {
                'ansible_user': 'admin'
            }
        },
        'webservers': {
            'hosts': ['web1.example.com', 'web2.example.com'],
            'vars': {
                'http_port': 80
            }
        },
        'databases': {
            'hosts': ['db1.example.com'],
            'vars': {
                'db_port': 5432
            }
        },
        '_meta': {
            'hostvars': {
                'web1.example.com': {
                    'ansible_host': '192.168.1.10'
                },
                'web2.example.com': {
                    'ansible_host': '192.168.1.11'
                },
                'db1.example.com': {
                    'ansible_host': '10.0.1.20',
                    'db_type': 'postgresql'
                }
            }
        }
    }
    return inventory

def get_host_vars(host):
    """Return variables for specific host"""
    inventory = get_inventory()
    return inventory['_meta']['hostvars'].get(host, {})

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == '--list':
        print(json.dumps(get_inventory(), indent=2))
    elif len(sys.argv) == 3 and sys.argv[1] == '--host':
        print(json.dumps(get_host_vars(sys.argv[2]), indent=2))
    else:
        print("Usage: {} --list or {} --host <hostname>".format(sys.argv[0], sys.argv[0]))
        sys.exit(1)
```

Make executable and use:

```bash
chmod +x inventory/custom_inventory.py
ansible-playbook -i inventory/custom_inventory.py site.yml
```

---

## Variable Management

### Variable Precedence (Lowest to Highest)

1. Command line values (e.g., `-u my_user`)
2. Role defaults (`roles/x/defaults/main.yml`)
3. Inventory file or script group vars
4. Inventory `group_vars/all`
5. Playbook `group_vars/all`
6. Inventory `group_vars/*`
7. Playbook `group_vars/*`
8. Inventory file or script host vars
9. Inventory `host_vars/*`
10. Playbook `host_vars/*`
11. Host facts / cached set_facts
12. Play vars
13. Play vars_prompt
14. Play vars_files
15. Role vars (`roles/x/vars/main.yml`)
16. Block vars (only for tasks in block)
17. Task vars (only for the task)
18. `include_vars`
19. `set_facts` / registered vars
20. Role (and include_role) params
21. Include params
22. Extra vars (`-e` in CLI, always win)

### Group Variables

```yaml
# group_vars/all.yml - Variables for all hosts
---
ansible_user: deploy
ansible_python_interpreter: /usr/bin/python3
ntp_servers:
  - 0.pool.ntp.org
  - 1.pool.ntp.org

# group_vars/webservers.yml
---
http_port: 80
https_port: 443
max_clients: 200
worker_processes: 4

# group_vars/databases.yml
---
db_port: 5432
max_connections: 100
shared_buffers: 256MB

# group_vars/production.yml
---
environment: production
backup_enabled: true
monitoring_enabled: true
log_level: warning

# group_vars/staging.yml
---
environment: staging
backup_enabled: false
monitoring_enabled: false
log_level: debug
```

### Host Variables

```yaml
# host_vars/web1.example.com.yml
---
ansible_host: 192.168.1.10
server_id: 1
max_clients: 300  # Override group var

# host_vars/db1.example.com.yml
---
ansible_host: 10.0.1.20
db_type: postgresql
db_version: 14
max_connections: 200  # Override group var
```

### Organizing Variables

```
inventory/
├── hosts                    # Main inventory file
├── group_vars/
│   ├── all.yml             # Variables for all hosts
│   ├── all/                # Split all vars into multiple files
│   │   ├── common.yml
│   │   ├── users.yml
│   │   └── packages.yml
│   ├── webservers.yml
│   ├── databases.yml
│   ├── production.yml
│   └── staging.yml
└── host_vars/
    ├── web1.example.com.yml
    ├── web2.example.com.yml
    └── db1.example.com.yml
```

### Variable Files in Playbooks

```yaml
# Load variables from files
- name: Configure application
  hosts: webservers
  vars_files:
    - vars/common.yml
    - vars/{{ environment }}.yml
    - vars/secrets.yml
  tasks:
    - name: Use variables
      debug:
        msg: "Environment: {{ environment }}, DB: {{ db_host }}"

# Include variables dynamically
- name: Load OS-specific variables
  include_vars: "{{ ansible_os_family }}.yml"

# Include variables with conditions
- name: Load environment variables
  include_vars:
    file: "{{ item }}"
  with_first_found:
    - "{{ environment }}.yml"
    - "default.yml"
```

### Registered Variables

```yaml
# Register command output
- name: Check application status
  command: /usr/local/bin/app-status
  register: app_status
  changed_when: false

- name: Display status
  debug:
    var: app_status

# Use registered variable
- name: Restart if needed
  service:
    name: myapp
    state: restarted
  when: "'needs_restart' in app_status.stdout"

# Register with loop
- name: Check multiple services
  service_facts:
  register: service_facts

- name: Show service status
  debug:
    msg: "{{ item }} is {{ service_facts.ansible_facts.services[item].state }}"
  loop:
    - nginx
    - postgresql
    - redis
```

### Set Facts

```yaml
# Set fact for later use
- name: Calculate memory allocation
  set_fact:
    app_memory: "{{ (ansible_memtotal_mb * 0.6) | int }}"

- name: Configure application
  template:
    src: app.conf.j2
    dest: /etc/app/app.conf
  vars:
    memory_limit: "{{ app_memory }}M"

# Set multiple facts
- name: Set deployment facts
  set_fact:
    deployment_time: "{{ ansible_date_time.iso8601 }}"
    deployment_user: "{{ ansible_user_id }}"
    deployment_host: "{{ inventory_hostname }}"

# Cacheable facts (persist across plays)
- name: Set cacheable fact
  set_fact:
    last_deployment: "{{ ansible_date_time.iso8601 }}"
    cacheable: yes
```

---

## Ansible Vault

### Creating Encrypted Files

```bash
# Create new encrypted file
ansible-vault create secrets.yml
# Opens editor to enter content, then prompts for password

# Create with password file
ansible-vault create --vault-password-file ~/.vault_pass secrets.yml

# Create with inline password
echo 'my_vault_password' | ansible-vault create --vault-password-file /dev/stdin secrets.yml
```

### Encrypting Existing Files

```bash
# Encrypt existing file
ansible-vault encrypt vars/passwords.yml

# Encrypt multiple files
ansible-vault encrypt vars/db_passwords.yml vars/api_keys.yml

# Encrypt with specific password file
ansible-vault encrypt --vault-password-file ~/.vault_pass vars/secrets.yml
```

### Viewing and Editing Encrypted Files

```bash
# View encrypted file
ansible-vault view secrets.yml

# Edit encrypted file
ansible-vault edit secrets.yml

# Decrypt file (creates unencrypted version)
ansible-vault decrypt secrets.yml

# Re-encrypt with new password
ansible-vault rekey secrets.yml
```

### Encrypted Variables File

```yaml
# vars/secrets.yml (encrypted)
---
db_password: supersecret123
api_key: abc123xyz789
aws_access_key: AKIAIOSFODNN7EXAMPLE
aws_secret_key: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
ssl_certificate_key: |
  -----BEGIN PRIVATE KEY-----
  MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC...
  -----END PRIVATE KEY-----
```

### Using Vault in Playbooks

```yaml
# Load encrypted variables
- name: Deploy application
  hosts: webservers
  vars_files:
    - vars/common.yml
    - vars/secrets.yml  # Encrypted file
  tasks:
    - name: Configure database connection
      template:
        src: db.conf.j2
        dest: /etc/app/db.conf
      vars:
        db_password: "{{ db_password }}"  # From encrypted file
```

Run with vault password:

```bash
# Prompt for password
ansible-playbook site.yml --ask-vault-pass

# Use password file
ansible-playbook site.yml --vault-password-file ~/.vault_pass

# Use password from environment
export ANSIBLE_VAULT_PASSWORD_FILE=~/.vault_pass
ansible-playbook site.yml
```

### Inline Encrypted Variables

```yaml
# Encrypt single variable
# ansible-vault encrypt_string 'supersecret' --name 'db_password'

# vars/main.yml
---
db_host: db.example.com
db_user: appuser
db_password: !vault |
  $ANSIBLE_VAULT;1.1;AES256
  66386439653966653231363934373366643962636339313931353634363338653034626462353630
  3737373936346662313062613832653932653931653939660a626566653834373836303738373564
  39656439353830383566363963653838316235613533653762393765343831656536626562626264
  6330303866383039650a353638643435666633633964366338653034313366343366383435383630
  3339
```

Encrypt string:

```bash
# Interactive
ansible-vault encrypt_string
# Enter string, Ctrl+D twice

# With prompt
ansible-vault encrypt_string 'supersecret' --name 'db_password'

# From stdin
echo -n 'supersecret' | ansible-vault encrypt_string --stdin-name 'db_password'
```

### Multiple Vault Passwords

```bash
# Use vault IDs for different passwords
ansible-vault create --vault-id dev@prompt secrets_dev.yml
ansible-vault create --vault-id prod@prompt secrets_prod.yml

# Run playbook with multiple vault passwords
ansible-playbook site.yml \
  --vault-id dev@~/.vault_pass_dev \
  --vault-id prod@~/.vault_pass_prod
```

### Vault Password Script

```python
#!/usr/bin/env python3
# vault-password.py
import os
import sys

# Retrieve password from environment, secret manager, etc.
password = os.environ.get('VAULT_PASSWORD')
if not password:
    sys.stderr.write('VAULT_PASSWORD environment variable not set\n')
    sys.exit(1)

print(password)
```

Use:

```bash
chmod +x vault-password.py
export VAULT_PASSWORD='my_secret_password'
ansible-playbook site.yml --vault-password-file ./vault-password.py
```

---

## Host and Group Patterns

```bash
# All hosts
ansible all -m ping

# Specific host
ansible web1.example.com -m ping

# Group
ansible webservers -m ping

# Multiple groups (OR)
ansible webservers:databases -m ping

# Intersection (AND)
ansible webservers:&production -m ping

# Exclusion (NOT)
ansible webservers:!staging -m ping

# Wildcard
ansible "web*.example.com" -m ping

# Regex
ansible "~web[0-9]+" -m ping

# Range
ansible "web[1:5]" -m ping

# Complex patterns
ansible "webservers:&production:!web3.example.com" -m ping

# Limit in playbook
ansible-playbook site.yml --limit webservers
ansible-playbook site.yml --limit @retry_hosts.txt
```
