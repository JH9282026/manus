# Automation Best Practices

Production automation patterns, performance optimization, testing, CI/CD integration, and troubleshooting.

---

## Project Structure

### Recommended Directory Layout

```
ansible-project/
├── ansible.cfg                 # Ansible configuration
├── inventory/
│   ├── production/
│   │   ├── hosts              # Production inventory
│   │   ├── group_vars/
│   │   │   ├── all.yml
│   │   │   ├── webservers.yml
│   │   │   └── databases.yml
│   │   └── host_vars/
│   │       └── web1.example.com.yml
│   ├── staging/
│   │   ├── hosts
│   │   └── group_vars/
│   └── development/
│       ├── hosts
│       └── group_vars/
├── playbooks/
│   ├── site.yml               # Master playbook
│   ├── webservers.yml         # Web server playbook
│   ├── databases.yml          # Database playbook
│   └── deploy.yml             # Deployment playbook
├── roles/
│   ├── common/                # Common configuration
│   ├── webserver/             # Web server role
│   ├── database/              # Database role
│   └── monitoring/            # Monitoring role
├── group_vars/
│   ├── all.yml                # Global variables
│   └── all/
│       ├── common.yml
│       └── vault.yml          # Encrypted secrets
├── host_vars/
├── library/                   # Custom modules
├── filter_plugins/            # Custom filters
├── files/                     # Static files
├── templates/                 # Jinja2 templates
├── vars/                      # Additional variables
├── requirements.yml           # Ansible Galaxy requirements
├── .gitignore
└── README.md
```

### ansible.cfg Best Practices

```ini
[defaults]
inventory = ./inventory/production/hosts
roles_path = ./roles
host_key_checking = False
retry_files_enabled = False
forks = 50
timeout = 30
log_path = ./logs/ansible.log
nocows = 1
interpreter_python = auto_silent

# Callback plugins for better output
stdout_callback = yaml
bin_ansible_callbacks = True

# Fact caching
gathering = smart
fact_caching = jsonfile
fact_caching_connection = ./facts_cache
fact_caching_timeout = 86400

# Vault
vault_password_file = ~/.ansible/vault_pass

[privilege_escalation]
become = True
become_method = sudo
become_user = root
become_ask_pass = False

[ssh_connection]
ssh_args = -o ControlMaster=auto -o ControlPersist=60s -o ForwardAgent=yes
pipelining = True
control_path = /tmp/ansible-ssh-%%h-%%p-%%r

[diff]
always = True
context = 3
```

---

## Playbook Best Practices

### Naming and Documentation

```yaml
---
# Always use descriptive names
- name: Deploy web application to production
  hosts: webservers
  become: yes
  
  # Document purpose and usage
  # This playbook deploys the web application
  # Usage: ansible-playbook deploy.yml -e "version=1.2.3"
  
  tasks:
    # Every task should have a descriptive name
    - name: Ensure application directory exists
      file:
        path: /opt/myapp
        state: directory
        owner: appuser
        group: appgroup
        mode: '0755'
    
    # Use comments for complex logic
    - name: Deploy application version {{ version }}
      # This task extracts the application archive
      # and creates a symlink to the current version
      unarchive:
        src: "files/myapp-{{ version }}.tar.gz"
        dest: /opt/myapp/releases/
```

### Idempotency

```yaml
# BAD: Not idempotent
- name: Add line to file
  shell: echo "config_value=123" >> /etc/app/config

# GOOD: Idempotent
- name: Ensure configuration value is set
  lineinfile:
    path: /etc/app/config
    regexp: '^config_value='
    line: 'config_value=123'

# BAD: Always changes
- name: Download file
  command: wget http://example.com/file.tar.gz

# GOOD: Only downloads if missing
- name: Download file if not present
  get_url:
    url: http://example.com/file.tar.gz
    dest: /tmp/file.tar.gz
    checksum: sha256:abc123...

# Use changed_when for commands
- name: Check application status
  command: /usr/local/bin/app-status
  register: app_status
  changed_when: false  # This command doesn't change anything
  failed_when: app_status.rc not in [0, 1]
```

### Error Handling

```yaml
# Fail fast on critical errors
- name: Verify prerequisites
  assert:
    that:
      - ansible_memtotal_mb >= 4096
      - ansible_distribution_version is version('20.04', '>=')
    fail_msg: "System does not meet minimum requirements"
    success_msg: "Prerequisites verified"

# Graceful degradation
- name: Install optional monitoring agent
  apt:
    name: monitoring-agent
    state: present
  ignore_errors: yes
  register: monitoring_install

- name: Log monitoring installation failure
  debug:
    msg: "Warning: Monitoring agent installation failed"
  when: monitoring_install.failed

# Retry on transient failures
- name: Download file with retry
  get_url:
    url: http://example.com/file.tar.gz
    dest: /tmp/file.tar.gz
  register: download_result
  until: download_result is succeeded
  retries: 5
  delay: 10

# Block with rescue
- name: Deploy with rollback capability
  block:
    - name: Deploy new version
      include_tasks: deploy.yml
    
    - name: Verify deployment
      uri:
        url: http://localhost/health
        status_code: 200
  
  rescue:
    - name: Rollback on failure
      include_tasks: rollback.yml
    
    - name: Notify team of failure
      debug:
        msg: "Deployment failed, rolled back to previous version"
  
  always:
    - name: Clean up temporary files
      file:
        path: /tmp/deployment-*
        state: absent
```

### Variable Management

```yaml
# Use defaults in roles
# roles/webserver/defaults/main.yml
---
http_port: 80
max_clients: 100
worker_processes: "{{ ansible_processor_vcpus }}"

# Use vars for constants
# roles/webserver/vars/main.yml
---
config_dir: /etc/nginx
log_dir: /var/log/nginx

# Validate required variables
- name: Ensure required variables are defined
  assert:
    that:
      - db_host is defined
      - db_password is defined
      - app_version is defined
    fail_msg: "Required variables not defined"

# Use variable files for environment-specific config
- name: Load environment variables
  include_vars: "{{ environment }}.yml"
  vars:
    environment: "{{ lookup('env', 'ENVIRONMENT') | default('development') }}"
```

---

## Performance Optimization

### Parallelism

```ini
# ansible.cfg
[defaults]
forks = 50  # Increase for large inventories
```

```yaml
# Control parallelism per play
- name: Rolling update
  hosts: webservers
  serial: 5  # Update 5 hosts at a time
  
# Percentage-based serial
- name: Gradual rollout
  hosts: webservers
  serial:
    - 1        # First host
    - 10%      # Then 10% of remaining
    - 25%      # Then 25% of remaining
    - 100%     # Then all remaining
```

### Fact Gathering Optimization

```yaml
# Disable when not needed
- name: Quick playbook
  hosts: all
  gather_facts: no
  tasks:
    - name: Simple task
      ping:

# Gather only needed facts
- name: Selective fact gathering
  hosts: all
  gather_facts: yes
  gather_subset:
    - '!all'
    - '!min'
    - network
    - virtual

# Use fact caching
# ansible.cfg
[defaults]
gathering = smart
fact_caching = jsonfile
fact_caching_connection = /tmp/ansible_facts
fact_caching_timeout = 86400
```

### SSH Optimization

```ini
# ansible.cfg
[ssh_connection]
pipelining = True
ssh_args = -o ControlMaster=auto -o ControlPersist=60s
control_path = /tmp/ansible-ssh-%%h-%%p-%%r
```

Requires disabling `requiretty` in sudoers:

```bash
# /etc/sudoers.d/ansible
Defaults:ansible !requiretty
```

### Async Tasks

```yaml
# Long-running tasks
- name: Run long deployment script
  command: /usr/local/bin/deploy.sh
  async: 3600  # Maximum runtime
  poll: 0      # Fire and forget
  register: deploy_job

# Continue with other tasks
- name: Do other work
  debug:
    msg: "Deployment running in background"

# Check status later
- name: Wait for deployment to complete
  async_status:
    jid: "{{ deploy_job.ansible_job_id }}"
  register: job_result
  until: job_result.finished
  retries: 120
  delay: 30
```

### Mitogen Strategy Plugin

```bash
# Install Mitogen
pip install mitogen
```

```ini
# ansible.cfg
[defaults]
strategy_plugins = /path/to/mitogen/ansible_mitogen/plugins/strategy
strategy = mitogen_linear
```

Provides 1.25x-7x performance improvement.

---

## Testing and Validation

### Syntax Checking

```bash
# Check playbook syntax
ansible-playbook playbook.yml --syntax-check

# Check all playbooks
find playbooks/ -name "*.yml" -exec ansible-playbook {} --syntax-check \;
```

### Dry Run (Check Mode)

```bash
# Run in check mode (no changes)
ansible-playbook playbook.yml --check

# Check mode with diff
ansible-playbook playbook.yml --check --diff
```

```yaml
# Force task to run in check mode
- name: Always check this
  command: /usr/bin/validate-config
  check_mode: yes

# Skip task in check mode
- name: Skip in check mode
  command: /usr/bin/dangerous-operation
  when: not ansible_check_mode
```

### Molecule Testing

```bash
# Install Molecule
pip install molecule molecule-docker

# Initialize role with Molecule
molecule init role my_role --driver-name docker

# Test sequence
molecule create    # Create test instance
molecule converge  # Run playbook
molecule verify    # Run tests
molecule destroy   # Clean up

# Full test
molecule test
```

```yaml
# molecule/default/molecule.yml
---
dependency:
  name: galaxy
driver:
  name: docker
platforms:
  - name: ubuntu-20.04
    image: ubuntu:20.04
    pre_build_image: true
  - name: centos-8
    image: centos:8
    pre_build_image: true
provisioner:
  name: ansible
  config_options:
    defaults:
      callbacks_enabled: profile_tasks
verifier:
  name: ansible
```

```yaml
# molecule/default/verify.yml
---
- name: Verify
  hosts: all
  tasks:
    - name: Check nginx is running
      service:
        name: nginx
        state: started
      check_mode: yes
      register: nginx_status
      failed_when: nginx_status.changed
    
    - name: Verify nginx responds
      uri:
        url: http://localhost
        status_code: 200
```

### Ansible Lint

```bash
# Install
pip install ansible-lint

# Lint playbook
ansible-lint playbook.yml

# Lint all playbooks
ansible-lint playbooks/

# Lint with specific rules
ansible-lint -r rules/ playbook.yml
```

```yaml
# .ansible-lint
---
skip_list:
  - '106'  # Role name does not match ^[a-z][a-z0-9_]+$ pattern
  - '204'  # Lines should be no longer than 160 chars

exclude_paths:
  - .cache/
  - .github/
  - molecule/

use_default_rules: true
```

---

## CI/CD Integration

### GitLab CI

```yaml
# .gitlab-ci.yml
stages:
  - validate
  - test
  - deploy

variables:
  ANSIBLE_FORCE_COLOR: "true"
  ANSIBLE_HOST_KEY_CHECKING: "false"

validate:
  stage: validate
  image: cytopia/ansible:latest
  script:
    - ansible-playbook --syntax-check playbooks/*.yml
    - ansible-lint playbooks/
  only:
    - merge_requests
    - main

test:
  stage: test
  image: cytopia/ansible:latest
  script:
    - pip install molecule molecule-docker
    - molecule test
  only:
    - merge_requests
    - main

deploy_staging:
  stage: deploy
  image: cytopia/ansible:latest
  script:
    - ansible-playbook -i inventory/staging playbooks/site.yml
  only:
    - main
  environment:
    name: staging

deploy_production:
  stage: deploy
  image: cytopia/ansible:latest
  script:
    - ansible-playbook -i inventory/production playbooks/site.yml
  only:
    - main
  when: manual
  environment:
    name: production
```

### GitHub Actions

```yaml
# .github/workflows/ansible.yml
name: Ansible CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      
      - name: Install dependencies
        run: |
          pip install ansible ansible-lint
      
      - name: Syntax check
        run: |
          ansible-playbook --syntax-check playbooks/*.yml
      
      - name: Lint
        run: |
          ansible-lint playbooks/
  
  test:
    runs-on: ubuntu-latest
    needs: validate
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      
      - name: Install Molecule
        run: |
          pip install molecule molecule-docker
      
      - name: Run Molecule tests
        run: |
          molecule test
  
  deploy:
    runs-on: ubuntu-latest
    needs: test
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v3
      
      - name: Deploy to staging
        env:
          ANSIBLE_VAULT_PASSWORD: ${{ secrets.ANSIBLE_VAULT_PASSWORD }}
        run: |
          echo "$ANSIBLE_VAULT_PASSWORD" > .vault_pass
          ansible-playbook -i inventory/staging playbooks/site.yml --vault-password-file .vault_pass
```

### Jenkins Pipeline

```groovy
// Jenkinsfile
pipeline {
    agent any
    
    environment {
        ANSIBLE_FORCE_COLOR = 'true'
        ANSIBLE_HOST_KEY_CHECKING = 'false'
    }
    
    stages {
        stage('Validate') {
            steps {
                sh 'ansible-playbook --syntax-check playbooks/*.yml'
                sh 'ansible-lint playbooks/'
            }
        }
        
        stage('Test') {
            steps {
                sh 'molecule test'
            }
        }
        
        stage('Deploy to Staging') {
            when {
                branch 'main'
            }
            steps {
                withCredentials([file(credentialsId: 'ansible-vault-password', variable: 'VAULT_PASS')]) {
                    sh 'ansible-playbook -i inventory/staging playbooks/site.yml --vault-password-file $VAULT_PASS'
                }
            }
        }
        
        stage('Deploy to Production') {
            when {
                branch 'main'
            }
            steps {
                input message: 'Deploy to production?', ok: 'Deploy'
                withCredentials([file(credentialsId: 'ansible-vault-password', variable: 'VAULT_PASS')]) {
                    sh 'ansible-playbook -i inventory/production playbooks/site.yml --vault-password-file $VAULT_PASS'
                }
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
    }
}
```

---

## Security Best Practices

### Secrets Management

```yaml
# Always use Ansible Vault for secrets
# vars/vault.yml (encrypted)
---
db_password: !vault |
  $ANSIBLE_VAULT;1.1;AES256...
api_key: !vault |
  $ANSIBLE_VAULT;1.1;AES256...

# Never commit unencrypted secrets
# .gitignore
*.vault_pass
*_unencrypted.yml
secrets/
```

### Privilege Escalation

```yaml
# Use become only when necessary
- name: Tasks not requiring root
  hosts: all
  become: no
  tasks:
    - name: Check application status
      command: /usr/local/bin/app-status

# Specific tasks with become
- name: Install package
  apt:
    name: nginx
    state: present
  become: yes

# Become specific user
- name: Run as application user
  command: /usr/local/bin/app-command
  become: yes
  become_user: appuser
```

### Audit Logging

```ini
# ansible.cfg
[defaults]
log_path = /var/log/ansible/ansible.log

# Use callback plugins for detailed logging
callbacks_enabled = log_plays, profile_tasks
```

---

## Troubleshooting

### Verbose Output

```bash
# Levels of verbosity
ansible-playbook playbook.yml -v    # Verbose
ansible-playbook playbook.yml -vv   # More verbose
ansible-playbook playbook.yml -vvv  # Very verbose (includes SSH debug)
ansible-playbook playbook.yml -vvvv # Connection-level debug
```

### Debug Module

```yaml
# Display variable
- name: Show variable value
  debug:
    var: my_variable

# Display message
- name: Show message
  debug:
    msg: "Value is {{ my_variable }}"

# Conditional debug
- name: Debug when condition met
  debug:
    msg: "This is a problem"
  when: some_condition
```

### Step-by-Step Execution

```bash
# Step through playbook
ansible-playbook playbook.yml --step

# Start at specific task
ansible-playbook playbook.yml --start-at-task="Task name"
```

### Common Issues

**SSH Connection Failures:**
```bash
# Test SSH connectivity
ansible all -m ping -vvv

# Check SSH config
ansible all -m setup -a "filter=ansible_ssh_*"
```

**Python Interpreter Issues:**
```yaml
# Specify Python interpreter
- name: Set Python interpreter
  hosts: all
  vars:
    ansible_python_interpreter: /usr/bin/python3
```

**Fact Gathering Failures:**
```yaml
# Disable fact gathering if problematic
- name: Playbook without facts
  hosts: all
  gather_facts: no
```
