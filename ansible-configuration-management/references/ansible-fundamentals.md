# Ansible Fundamentals

Core concepts, installation, configuration, and module usage for Ansible automation.

---

## Installation and Setup

### Control Node Requirements

- **Operating System**: Linux (RHEL, Debian, Ubuntu, etc.) or macOS
- **Python**: 3.8 or newer (Python 2.7 deprecated)
- **SSH Client**: OpenSSH or compatible
- **Not Supported**: Windows as control node (use WSL2)

### Installation Methods

#### Using pip (Recommended)

```bash
# Install in virtual environment
python3 -m venv ansible-venv
source ansible-venv/bin/activate
pip install ansible

# Verify installation
ansible --version
```

#### Using Package Manager

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository --yes --update ppa:ansible/ansible
sudo apt install ansible

# RHEL/CentOS
sudo yum install epel-release
sudo yum install ansible

# macOS
brew install ansible
```

#### Installing Specific Version

```bash
pip install ansible-core==2.14.2
pip install ansible==7.2.0
```

### Managed Node Requirements

- **Python**: 2.7 or 3.5+ (most modules require Python)
- **SSH Server**: OpenSSH or compatible
- **SFTP/SCP**: For file transfer (or enable `pipelining`)
- **Privilege Escalation**: sudo, su, or similar (if needed)

### SSH Key Setup

```bash
# Generate SSH key on control node
ssh-keygen -t ed25519 -C "ansible-control"

# Copy public key to managed nodes
ssh-copy-id user@managed-node.example.com

# Test connection
ssh user@managed-node.example.com

# Test Ansible connectivity
ansible all -i managed-node.example.com, -m ping -u user
```

---

## Configuration Files

### Configuration Precedence

Ansible searches for configuration in this order:

1. `ANSIBLE_CONFIG` environment variable
2. `ansible.cfg` in current directory
3. `~/.ansible.cfg` in home directory
4. `/etc/ansible/ansible.cfg` system-wide

### Essential Configuration Options

```ini
# ansible.cfg
[defaults]
inventory = ./inventory/hosts
remote_user = ansible
host_key_checking = False
retry_files_enabled = False
forks = 20
timeout = 30
log_path = ./ansible.log

# Privilege escalation
[privilege_escalation]
become = True
become_method = sudo
become_user = root
become_ask_pass = False

# SSH connection
[ssh_connection]
ssh_args = -o ControlMaster=auto -o ControlPersist=60s
pipelining = True
control_path = /tmp/ansible-ssh-%%h-%%p-%%r
```

### Configuration Categories

**Performance Settings:**
- `forks` — Parallel execution (default: 5, increase for large inventories)
- `pipelining` — Reduce SSH operations (requires `requiretty` disabled in sudoers)
- `gathering` — Fact gathering strategy (implicit, explicit, smart)
- `fact_caching` — Cache facts to avoid repeated gathering

**Connection Settings:**
- `remote_user` — Default SSH user
- `timeout` — SSH connection timeout
- `host_key_checking` — Verify SSH host keys (disable for dynamic environments)

**Security Settings:**
- `become_*` — Privilege escalation configuration
- `vault_password_file` — Path to vault password file
- `private_key_file` — SSH private key location

---

## Module System

### Module Categories

**System Modules:**
- `user`, `group` — User and group management
- `service`, `systemd` — Service management
- `cron` — Cron job management
- `hostname`, `timezone` — System configuration

**Package Management:**
- `apt`, `yum`, `dnf` — Package managers
- `pip`, `npm`, `gem` — Language package managers
- `package` — Generic package module (auto-detects package manager)

**File Operations:**
- `copy` — Copy files from control to managed nodes
- `fetch` — Fetch files from managed nodes to control
- `template` — Process Jinja2 templates and copy
- `file` — Set file attributes, create directories, symlinks
- `lineinfile` — Ensure line exists in file
- `blockinfile` — Insert/update/remove text blocks
- `replace` — Replace text using regex

**Command Execution:**
- `command` — Execute commands (no shell processing)
- `shell` — Execute commands through shell
- `raw` — Execute raw SSH commands (no Python required)
- `script` — Transfer and execute script

**Cloud Modules:**
- `amazon.aws.*` — AWS resources (EC2, S3, RDS, etc.)
- `azure.azcollection.*` — Azure resources
- `google.cloud.*` — GCP resources
- `openstack.*` — OpenStack resources

**Network Modules:**
- `uri` — HTTP requests
- `get_url` — Download files
- `git` — Git repository management

**Database Modules:**
- `mysql_*` — MySQL/MariaDB management
- `postgresql_*` — PostgreSQL management
- `mongodb_*` — MongoDB management

### Module Usage Patterns

#### Package Installation

```yaml
# Specific package manager
- name: Install nginx on Debian
  apt:
    name: nginx
    state: present
    update_cache: yes
    cache_valid_time: 3600

# Generic package module
- name: Install nginx (any OS)
  package:
    name: nginx
    state: present

# Multiple packages
- name: Install multiple packages
  apt:
    name:
      - nginx
      - postgresql
      - redis-server
    state: present
```

#### File Management

```yaml
# Copy static file
- name: Copy configuration file
  copy:
    src: files/app.conf
    dest: /etc/app/app.conf
    owner: root
    group: root
    mode: '0644'
    backup: yes

# Create directory
- name: Ensure directory exists
  file:
    path: /var/app/data
    state: directory
    owner: appuser
    group: appgroup
    mode: '0755'

# Create symlink
- name: Create symlink
  file:
    src: /opt/app/current
    dest: /opt/app/releases/v1.2.3
    state: link

# Modify file content
- name: Set configuration value
  lineinfile:
    path: /etc/app/config.ini
    regexp: '^max_connections ='
    line: 'max_connections = 200'
    backup: yes
```

#### Service Management

```yaml
# Start and enable service
- name: Ensure nginx is running
  service:
    name: nginx
    state: started
    enabled: yes

# Restart service
- name: Restart application
  systemd:
    name: myapp
    state: restarted
    daemon_reload: yes

# Reload service configuration
- name: Reload nginx
  service:
    name: nginx
    state: reloaded
```

#### Command Execution

```yaml
# Simple command (no shell)
- name: Check disk space
  command: df -h /var
  register: disk_space
  changed_when: false

# Shell command (with pipes, redirects)
- name: Get running processes
  shell: ps aux | grep nginx | grep -v grep
  register: nginx_processes
  changed_when: false
  failed_when: false

# Execute script
- name: Run deployment script
  script: scripts/deploy.sh
  args:
    creates: /var/app/deployed.flag

# Raw command (no Python required)
- name: Bootstrap Python
  raw: apt-get install -y python3
  when: ansible_python_interpreter is not defined
```

#### User Management

```yaml
# Create user
- name: Create application user
  user:
    name: appuser
    comment: "Application Service Account"
    uid: 1050
    group: appgroup
    groups: docker,sudo
    shell: /bin/bash
    create_home: yes
    home: /home/appuser

# Add SSH key
- name: Add SSH authorized key
  authorized_key:
    user: appuser
    state: present
    key: "{{ lookup('file', 'files/appuser_id_rsa.pub') }}"
```

---

## Cloud Infrastructure Management

### AWS EC2 Instance Management

```yaml
# Install AWS collection
# ansible-galaxy collection install amazon.aws

- name: Launch EC2 instance
  amazon.aws.ec2_instance:
    name: web-server-01
    key_name: my-keypair
    instance_type: t3.medium
    image_id: ami-0c55b159cbfafe1f0
    region: us-east-1
    vpc_subnet_id: subnet-12345678
    security_group: web-sg
    network:
      assign_public_ip: yes
    tags:
      Environment: production
      Application: web
    state: running
    wait: yes

- name: Create security group
  amazon.aws.ec2_security_group:
    name: web-sg
    description: Web server security group
    region: us-east-1
    vpc_id: vpc-12345678
    rules:
      - proto: tcp
        from_port: 80
        to_port: 80
        cidr_ip: 0.0.0.0/0
      - proto: tcp
        from_port: 443
        to_port: 443
        cidr_ip: 0.0.0.0/0
      - proto: tcp
        from_port: 22
        to_port: 22
        cidr_ip: 10.0.0.0/8

- name: Create and attach EBS volume
  amazon.aws.ec2_vol:
    instance: i-1234567890abcdef0
    volume_size: 100
    volume_type: gp3
    device_name: /dev/sdf
    region: us-east-1
    tags:
      Name: web-data-volume
```

### Azure Resource Management

```yaml
# Install Azure collection
# ansible-galaxy collection install azure.azcollection
# pip install -r ~/.ansible/collections/ansible_collections/azure/azcollection/requirements-azure.txt

- name: Create resource group
  azure.azcollection.azure_rm_resourcegroup:
    name: myResourceGroup
    location: eastus

- name: Create virtual network
  azure.azcollection.azure_rm_virtualnetwork:
    resource_group: myResourceGroup
    name: myVNet
    address_prefixes: "10.0.0.0/16"

- name: Create subnet
  azure.azcollection.azure_rm_subnet:
    resource_group: myResourceGroup
    name: mySubnet
    address_prefix: "10.0.1.0/24"
    virtual_network: myVNet

- name: Create VM
  azure.azcollection.azure_rm_virtualmachine:
    resource_group: myResourceGroup
    name: myVM
    vm_size: Standard_DS1_v2
    admin_username: azureuser
    ssh_password_enabled: false
    ssh_public_keys:
      - path: /home/azureuser/.ssh/authorized_keys
        key_data: "{{ lookup('file', '~/.ssh/id_rsa.pub') }}"
    image:
      offer: UbuntuServer
      publisher: Canonical
      sku: '20.04-LTS'
      version: latest
```

### GCP Resource Management

```yaml
# Install GCP collection
# ansible-galaxy collection install google.cloud
# pip install requests google-auth

- name: Create GCE instance
  google.cloud.gcp_compute_instance:
    name: web-instance
    machine_type: n1-standard-1
    zone: us-central1-a
    project: my-project-id
    auth_kind: serviceaccount
    service_account_file: "/path/to/credentials.json"
    disks:
      - auto_delete: true
        boot: true
        initialize_params:
          source_image: projects/ubuntu-os-cloud/global/images/family/ubuntu-2004-lts
    network_interfaces:
      - network: default
        access_configs:
          - name: External NAT
            type: ONE_TO_ONE_NAT
    tags:
      items:
        - http-server
        - https-server
    state: present
```

---

## Ad-Hoc Commands

Execute one-off tasks without writing playbooks:

```bash
# Ping all hosts
ansible all -m ping

# Check disk space
ansible webservers -m command -a "df -h"

# Install package
ansible dbservers -m apt -a "name=postgresql state=present" --become

# Restart service
ansible all -m service -a "name=nginx state=restarted" --become

# Copy file
ansible webservers -m copy -a "src=/tmp/file.txt dest=/tmp/file.txt"

# Gather facts
ansible localhost -m setup

# Run command on specific host
ansible web1.example.com -m command -a "uptime"

# Use different user
ansible all -m ping -u deploy --become --become-user root

# Limit to subset of hosts
ansible webservers -m ping --limit "web1*"

# Use pattern matching
ansible "web*:&production" -m ping  # Intersection
ansible "web*:!web3*" -m ping       # Exclusion
```

---

## Facts and Variables

### Gathering Facts

Ansible automatically collects system information (facts) from managed nodes:

```yaml
# View all facts
- name: Display all facts
  debug:
    var: ansible_facts

# Use specific facts
- name: Show OS information
  debug:
    msg: "Running {{ ansible_facts['distribution'] }} {{ ansible_facts['distribution_version'] }}"

# Disable fact gathering
- name: Quick playbook
  hosts: all
  gather_facts: no
```

### Useful Facts

- `ansible_facts['hostname']` — Short hostname
- `ansible_facts['fqdn']` — Fully qualified domain name
- `ansible_facts['distribution']` — OS distribution (Ubuntu, CentOS, etc.)
- `ansible_facts['distribution_version']` — OS version
- `ansible_facts['os_family']` — OS family (Debian, RedHat, etc.)
- `ansible_facts['architecture']` — CPU architecture
- `ansible_facts['processor_cores']` — CPU cores
- `ansible_facts['memtotal_mb']` — Total memory in MB
- `ansible_facts['default_ipv4']['address']` — Primary IP address
- `ansible_facts['interfaces']` — Network interfaces
- `ansible_facts['mounts']` — Mounted filesystems

### Custom Facts

Create custom facts on managed nodes:

```bash
# /etc/ansible/facts.d/custom.fact (executable script or JSON/INI file)
#!/bin/bash
echo '{"deployment_version": "1.2.3", "environment": "production"}'
```

Access custom facts:

```yaml
- name: Display custom fact
  debug:
    msg: "Deployment version: {{ ansible_facts['ansible_local']['custom']['deployment_version'] }}"
```

---

## Collections

Ansible Collections bundle modules, plugins, roles, and playbooks.

### Installing Collections

```bash
# Install from Ansible Galaxy
ansible-galaxy collection install community.general
ansible-galaxy collection install amazon.aws
ansible-galaxy collection install azure.azcollection

# Install specific version
ansible-galaxy collection install community.general:5.8.0

# Install from requirements file
ansible-galaxy collection install -r requirements.yml
```

### requirements.yml

```yaml
collections:
  - name: community.general
    version: ">=5.0.0"
  - name: amazon.aws
    version: "5.2.0"
  - name: azure.azcollection
  - name: google.cloud
```

### Using Collection Modules

```yaml
# Fully qualified collection name (FQCN)
- name: Use community module
  community.general.docker_container:
    name: myapp
    image: nginx:latest
    state: started

# Or use collections keyword
- name: Docker tasks
  hosts: all
  collections:
    - community.general
  tasks:
    - name: Start container
      docker_container:
        name: myapp
        image: nginx:latest
```
