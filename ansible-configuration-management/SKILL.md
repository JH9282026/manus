---
name: ansible-configuration-management
description: "Automate infrastructure provisioning, configuration management, and application deployment using Ansible. Use for writing playbooks and roles, managing inventory and variables, orchestrating multi-tier deployments, implementing infrastructure as code, automating server configuration, deploying applications across environments, managing cloud resources, and implementing DevOps automation workflows."
---

# Ansible Configuration Management

Automate infrastructure provisioning, configuration management, and application deployment using Ansible's agentless architecture.

## Overview

This skill provides comprehensive guidance on using Ansible for infrastructure automation, including playbook development, role creation, inventory management, variable handling, and deployment orchestration. Ansible uses SSH and Python to manage systems without requiring agents, making it ideal for automating configuration management, application deployment, and infrastructure provisioning across diverse environments.

## Quick Start: Task Selection Guide

| Scenario | Approach | Reference |
|----------|----------|----------|
| First-time Ansible setup | Install Ansible, configure inventory, write simple playbook | `/references/ansible-fundamentals.md` |
| Automate server configuration | Create playbooks with tasks, handlers, templates | `/references/playbooks-roles.md` |
| Manage multiple environments | Use inventory groups, host/group variables | `/references/inventory-variables.md` |
| Deploy multi-tier application | Create roles, use dependencies, orchestrate deployment | `/references/playbooks-roles.md` |
| Implement reusable automation | Develop roles with proper structure and defaults | `/references/automation-best-practices.md` |
| Manage secrets and credentials | Use Ansible Vault for encryption | `/references/inventory-variables.md` |
| Cloud infrastructure provisioning | Use cloud modules (AWS, Azure, GCP) | `/references/ansible-fundamentals.md` |
| Continuous deployment pipeline | Integrate Ansible with CI/CD tools | `/references/automation-best-practices.md` |

## Core Concepts

### Ansible Architecture

**Control Node** — Machine where Ansible is installed and playbooks are executed. Requires Python 3.8+ and SSH access to managed nodes.

**Managed Nodes** — Target systems configured by Ansible. No agent required, only Python 2.7+ or 3.5+ and SSH access.

**Inventory** — Defines managed nodes, groups, and variables. Can be static (INI/YAML files) or dynamic (scripts/plugins querying cloud providers).

**Modules** — Reusable units of code that perform specific tasks (install packages, copy files, manage services). Over 3,000 built-in modules available.

**Playbooks** — YAML files defining automation workflows as ordered lists of tasks executed against inventory hosts.

**Roles** — Structured way to organize playbooks, variables, files, templates, and handlers into reusable components.

### Idempotency Principle

Ansible operations are idempotent — running the same playbook multiple times produces the same result without unintended side effects. Tasks check current state before making changes, ensuring safe repeated execution.

## Playbook Structure

```yaml
---
- name: Configure web servers
  hosts: webservers
  become: yes
  vars:
    http_port: 80
    max_clients: 200
  
  tasks:
    - name: Install Apache
      apt:
        name: apache2
        state: present
        update_cache: yes
    
    - name: Copy configuration file
      template:
        src: apache.conf.j2
        dest: /etc/apache2/apache2.conf
      notify: Restart Apache
    
    - name: Ensure Apache is running
      service:
        name: apache2
        state: started
        enabled: yes
  
  handlers:
    - name: Restart Apache
      service:
        name: apache2
        state: restarted
```

**Key Elements:**
- `hosts` — Target inventory group or pattern
- `become` — Privilege escalation (sudo)
- `vars` — Playbook-level variables
- `tasks` — Ordered list of module executions
- `handlers` — Tasks triggered by notifications, run once at end

## Role Development

Roles provide standardized directory structure for organizing automation code:

```
roles/
└── webserver/
    ├── tasks/
    │   └── main.yml          # Main task list
    ├── handlers/
    │   └── main.yml          # Handler definitions
    ├── templates/
    │   └── config.j2         # Jinja2 templates
    ├── files/
    │   └── script.sh         # Static files
    ├── vars/
    │   └── main.yml          # Role variables
    ├── defaults/
    │   └── main.yml          # Default variables (lowest precedence)
    ├── meta/
    │   └── main.yml          # Role metadata and dependencies
    └── README.md             # Role documentation
```

Use roles in playbooks:

```yaml
---
- name: Deploy application
  hosts: appservers
  roles:
    - common
    - database
    - webserver
    - monitoring
```

## Variable Precedence

Ansible has 22 levels of variable precedence (lowest to highest):

1. Role defaults (`roles/x/defaults/main.yml`)
2. Inventory file/script group vars
3. Inventory group_vars/all
4. Playbook group_vars/all
5. Inventory group_vars/*
6. Playbook group_vars/*
7. Inventory file/script host vars
8. Inventory host_vars/*
9. Playbook host_vars/*
10. Host facts and cached set_facts
11. Play vars
12. Play vars_prompt
13. Play vars_files
14. Role vars (`roles/x/vars/main.yml`)
15. Block vars
16. Task vars
17. Include_vars
18. Set_facts / registered vars
19. Role params
20. Include params
21. Extra vars (`-e` command line)

Use role defaults for customizable values, role vars for internal constants, and extra vars for runtime overrides.

## Inventory Management

### Static Inventory (INI format)

```ini
[webservers]
web1.example.com
web2.example.com

[databases]
db1.example.com ansible_port=5432
db2.example.com ansible_port=5432

[production:children]
webservers
databases

[production:vars]
ansible_user=deploy
ansible_python_interpreter=/usr/bin/python3
```

### Dynamic Inventory

Use scripts or plugins to query cloud providers, CMDBs, or other sources:

```bash
# AWS EC2 dynamic inventory
ansible-playbook -i aws_ec2.yml playbook.yml
```

```yaml
# aws_ec2.yml plugin configuration
plugin: aws_ec2
regions:
  - us-east-1
  - us-west-2
keyed_groups:
  - key: tags.Environment
    prefix: env
  - key: instance_type
    prefix: type
```

## Common Patterns

### Conditional Execution

```yaml
- name: Install package on Debian systems
  apt:
    name: nginx
    state: present
  when: ansible_os_family == "Debian"

- name: Install package on RedHat systems
  yum:
    name: nginx
    state: present
  when: ansible_os_family == "RedHat"
```

### Loops

```yaml
- name: Create multiple users
  user:
    name: "{{ item.name }}"
    state: present
    groups: "{{ item.groups }}"
  loop:
    - { name: 'alice', groups: 'admin,developers' }
    - { name: 'bob', groups: 'developers' }
    - { name: 'charlie', groups: 'operators' }
```

### Error Handling

```yaml
- name: Attempt risky operation
  command: /usr/bin/risky-command
  register: result
  ignore_errors: yes

- name: Handle failure
  debug:
    msg: "Command failed, proceeding with fallback"
  when: result.failed
```

### Delegation and Local Actions

```yaml
- name: Update load balancer
  command: /usr/local/bin/update-lb {{ inventory_hostname }}
  delegate_to: localhost
  run_once: true
```

## Ansible Vault for Secrets

Encrypt sensitive data:

```bash
# Create encrypted file
ansible-vault create secrets.yml

# Edit encrypted file
ansible-vault edit secrets.yml

# Encrypt existing file
ansible-vault encrypt vars/passwords.yml

# Run playbook with vault password
ansible-playbook site.yml --ask-vault-pass

# Use password file
ansible-playbook site.yml --vault-password-file ~/.vault_pass
```

Encrypted variables file:

```yaml
# secrets.yml (encrypted)
db_password: supersecret123
api_key: abc123xyz789
```

Reference in playbook:

```yaml
- name: Configure application
  hosts: appservers
  vars_files:
    - secrets.yml
  tasks:
    - name: Set database password
      lineinfile:
        path: /etc/app/config.ini
        line: "db_password={{ db_password }}"
```

## Testing and Validation

### Syntax Check

```bash
ansible-playbook playbook.yml --syntax-check
```

### Dry Run (Check Mode)

```bash
ansible-playbook playbook.yml --check
```

### Diff Mode

```bash
ansible-playbook playbook.yml --check --diff
```

### Molecule for Role Testing

Molecule provides testing framework for Ansible roles:

```bash
# Initialize new role with Molecule
molecule init role my_role

# Run test sequence
molecule test

# Test sequence: lint → destroy → create → converge → verify → destroy
```

## Performance Optimization

### Parallelism

```ini
# ansible.cfg
[defaults]
forks = 50              # Parallel processes (default: 5)
```

### Pipelining

```ini
# ansible.cfg
[ssh_connection]
pipelining = True       # Reduce SSH operations
```

### Fact Caching

```ini
# ansible.cfg
[defaults]
gathering = smart       # Only gather facts when needed
fact_caching = jsonfile
fact_caching_connection = /tmp/ansible_facts
fact_caching_timeout = 3600
```

### Disable Fact Gathering

```yaml
- name: Quick playbook
  hosts: all
  gather_facts: no      # Skip when facts not needed
  tasks:
    - name: Simple task
      ping:
```

## Integration Patterns

### CI/CD Integration

```yaml
# GitLab CI example
deploy_production:
  stage: deploy
  script:
    - ansible-playbook -i inventory/production site.yml
  only:
    - main
  when: manual
```

### Terraform Integration

Use Terraform for infrastructure provisioning, Ansible for configuration:

```hcl
# Terraform generates Ansible inventory
resource "local_file" "ansible_inventory" {
  content = templatefile("inventory.tpl", {
    web_ips = aws_instance.web[*].public_ip
    db_ips  = aws_instance.db[*].private_ip
  })
  filename = "${path.module}/inventory/hosts"
}

resource "null_resource" "ansible_provisioning" {
  provisioner "local-exec" {
    command = "ansible-playbook -i inventory/hosts site.yml"
  }
  depends_on = [local_file.ansible_inventory]
}
```

### AWX/Ansible Tower

Enterprise features:
- Web UI for playbook execution
- Role-based access control
- Job scheduling and workflows
- Credential management
- REST API for automation
- Audit logging and reporting

## Using the Reference Files

### When to Read Each Reference

**`/references/ansible-fundamentals.md`** — Read when setting up Ansible for the first time, understanding core concepts, installing and configuring Ansible, working with modules, or managing cloud infrastructure.

**`/references/playbooks-roles.md`** — Read when writing playbooks, developing roles, using templates and handlers, implementing complex task logic, or organizing automation code for reusability.

**`/references/inventory-variables.md`** — Read when managing inventory (static or dynamic), working with variables and facts, implementing group/host variables, using Ansible Vault for secrets, or managing multiple environments.

**`/references/automation-best-practices.md`** — Read when implementing production automation, optimizing performance, testing and validating playbooks, implementing CI/CD integration, following security best practices, or troubleshooting Ansible issues.
