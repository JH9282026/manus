# Playbooks and Roles

Advanced playbook development, role creation, templates, handlers, and task organization.

---

## Playbook Structure and Syntax

### Multi-Play Playbooks

```yaml
---
# Site-wide deployment playbook
- name: Configure database servers
  hosts: databases
  become: yes
  roles:
    - common
    - postgresql
  
- name: Configure web servers
  hosts: webservers
  become: yes
  roles:
    - common
    - nginx
    - application
  
- name: Configure load balancers
  hosts: loadbalancers
  become: yes
  roles:
    - common
    - haproxy
```

### Play-Level Keywords

```yaml
- name: Advanced play configuration
  hosts: webservers
  become: yes
  become_user: root
  become_method: sudo
  gather_facts: yes
  serial: 2                    # Rolling update: 2 hosts at a time
  max_fail_percentage: 25      # Abort if >25% of hosts fail
  any_errors_fatal: yes        # Stop all hosts if any fails
  connection: ssh
  remote_user: deploy
  vars:
    app_version: "1.2.3"
  vars_files:
    - vars/common.yml
    - vars/{{ env }}.yml
  pre_tasks:
    - name: Pre-deployment checks
      command: /usr/local/bin/pre-check.sh
  roles:
    - webserver
  tasks:
    - name: Deploy application
      copy:
        src: "app-{{ app_version }}.tar.gz"
        dest: /opt/app/
  post_tasks:
    - name: Post-deployment validation
      uri:
        url: http://localhost/health
        status_code: 200
  handlers:
    - name: Restart application
      service:
        name: myapp
        state: restarted
```

---

## Task Control Flow

### Conditionals

```yaml
# Simple when condition
- name: Install Apache on Debian
  apt:
    name: apache2
    state: present
  when: ansible_os_family == "Debian"

# Multiple conditions (AND)
- name: Install on production Ubuntu servers
  apt:
    name: monitoring-agent
    state: present
  when:
    - ansible_distribution == "Ubuntu"
    - environment == "production"
    - ansible_distribution_version is version('20.04', '>=')

# OR conditions
- name: Install on RedHat or CentOS
  yum:
    name: httpd
    state: present
  when: ansible_distribution == "RedHat" or ansible_distribution == "CentOS"

# Complex conditions
- name: Conditional based on registered variable
  command: /usr/bin/check-status
  register: status_result
  changed_when: false

- name: Act on status
  service:
    name: myapp
    state: restarted
  when:
    - status_result.rc == 0
    - "'needs_restart' in status_result.stdout"

# Conditional based on facts
- name: Ensure sufficient memory
  fail:
    msg: "Insufficient memory: {{ ansible_memtotal_mb }}MB"
  when: ansible_memtotal_mb < 4096

# Variable defined check
- name: Use custom config if defined
  template:
    src: custom.conf.j2
    dest: /etc/app/app.conf
  when: custom_config is defined

# File existence check
- name: Check if file exists
  stat:
    path: /etc/app/config.lock
  register: lock_file

- name: Skip if locked
  debug:
    msg: "Deployment locked"
  when: lock_file.stat.exists
```

### Loops

```yaml
# Simple list loop
- name: Install packages
  apt:
    name: "{{ item }}"
    state: present
  loop:
    - nginx
    - postgresql
    - redis-server

# Loop with dictionaries
- name: Create users
  user:
    name: "{{ item.name }}"
    state: present
    groups: "{{ item.groups }}"
    shell: "{{ item.shell | default('/bin/bash') }}"
  loop:
    - { name: 'alice', groups: 'admin,developers', shell: '/bin/zsh' }
    - { name: 'bob', groups: 'developers' }
    - { name: 'charlie', groups: 'operators' }

# Loop with loop_control
- name: Deploy application to multiple environments
  include_tasks: deploy.yml
  loop:
    - dev
    - staging
    - production
  loop_control:
    loop_var: environment
    pause: 30              # Pause 30s between iterations
    label: "{{ environment }}"  # Show only this in output

# Loop over dictionary
- name: Set firewall rules
  firewalld:
    port: "{{ item.value.port }}/tcp"
    permanent: yes
    state: enabled
  loop: "{{ services | dict2items }}"
  vars:
    services:
      web:
        port: 80
      api:
        port: 8080
      admin:
        port: 9000

# Loop with index
- name: Create numbered directories
  file:
    path: "/var/data/shard-{{ item.0 }}"
    state: directory
  loop: "{{ range(0, 10) | list }}"

# Nested loops (with_nested deprecated, use loop with product)
- name: Create user-group combinations
  debug:
    msg: "User {{ item.0 }} in group {{ item.1 }}"
  loop: "{{ users | product(groups) | list }}"
  vars:
    users: ['alice', 'bob']
    groups: ['developers', 'operators']

# Loop until condition
- name: Wait for service to be ready
  uri:
    url: http://localhost:8080/health
    status_code: 200
  register: result
  until: result.status == 200
  retries: 10
  delay: 5
```

### Blocks and Error Handling

```yaml
# Block with rescue and always
- name: Deployment with rollback
  block:
    - name: Stop application
      service:
        name: myapp
        state: stopped
    
    - name: Deploy new version
      copy:
        src: "app-{{ new_version }}.tar.gz"
        dest: /opt/app/
    
    - name: Extract application
      unarchive:
        src: "/opt/app/app-{{ new_version }}.tar.gz"
        dest: /opt/app/current
        remote_src: yes
    
    - name: Start application
      service:
        name: myapp
        state: started
    
    - name: Verify deployment
      uri:
        url: http://localhost:8080/health
        status_code: 200
      register: health_check
      failed_when: health_check.status != 200
  
  rescue:
    - name: Rollback on failure
      debug:
        msg: "Deployment failed, rolling back to {{ current_version }}"
    
    - name: Restore previous version
      copy:
        src: "app-{{ current_version }}.tar.gz"
        dest: /opt/app/
    
    - name: Extract previous version
      unarchive:
        src: "/opt/app/app-{{ current_version }}.tar.gz"
        dest: /opt/app/current
        remote_src: yes
    
    - name: Start application
      service:
        name: myapp
        state: started
  
  always:
    - name: Clean up temporary files
      file:
        path: /tmp/deployment-*
        state: absent
    
    - name: Send notification
      debug:
        msg: "Deployment process completed"

# Block with conditional
- name: Production-only tasks
  block:
    - name: Enable monitoring
      service:
        name: monitoring-agent
        state: started
    
    - name: Configure backups
      cron:
        name: "Database backup"
        hour: "2"
        minute: "0"
        job: "/usr/local/bin/backup.sh"
  when: environment == "production"
  become: yes
```

---

## Handlers

Handlers are tasks triggered by notifications, executed once at the end of a play.

```yaml
# Basic handler usage
tasks:
  - name: Update nginx configuration
    template:
      src: nginx.conf.j2
      dest: /etc/nginx/nginx.conf
    notify: Restart nginx
  
  - name: Update site configuration
    template:
      src: site.conf.j2
      dest: /etc/nginx/sites-available/default
    notify:
      - Reload nginx
      - Clear cache

handlers:
  - name: Restart nginx
    service:
      name: nginx
      state: restarted
  
  - name: Reload nginx
    service:
      name: nginx
      state: reloaded
  
  - name: Clear cache
    command: /usr/local/bin/clear-cache.sh

# Handler with listen
tasks:
  - name: Update web config
    template:
      src: web.conf.j2
      dest: /etc/web/web.conf
    notify: Restart web services
  
  - name: Update API config
    template:
      src: api.conf.j2
      dest: /etc/api/api.conf
    notify: Restart web services

handlers:
  - name: Restart nginx
    service:
      name: nginx
      state: restarted
    listen: Restart web services
  
  - name: Restart application
    service:
      name: myapp
      state: restarted
    listen: Restart web services

# Force handler execution
- name: Flush handlers immediately
  meta: flush_handlers

# Handler execution order
handlers:
  - name: Stop application
    service:
      name: myapp
      state: stopped
  
  - name: Update database
    command: /usr/local/bin/migrate-db.sh
  
  - name: Start application
    service:
      name: myapp
      state: started
```

---

## Jinja2 Templates

### Basic Template Usage

```yaml
# Task using template
- name: Configure application
  template:
    src: app.conf.j2
    dest: /etc/app/app.conf
    owner: root
    group: root
    mode: '0644'
    backup: yes
  notify: Restart application
```

### Template Syntax

```jinja2
{# templates/app.conf.j2 #}
# Application Configuration
# Generated by Ansible on {{ ansible_date_time.iso8601 }}

# Server settings
server_name = {{ inventory_hostname }}
server_ip = {{ ansible_default_ipv4.address }}
environment = {{ environment }}

# Database connection
db_host = {{ db_host }}
db_port = {{ db_port | default(5432) }}
db_name = {{ db_name }}
db_user = {{ db_user }}
db_password = {{ db_password }}

# Application settings
max_connections = {{ max_connections | default(100) }}
worker_processes = {{ ansible_processor_vcpus }}
memory_limit = {{ (ansible_memtotal_mb * 0.8) | int }}M

# Feature flags
{% if enable_caching %}
cache_enabled = true
cache_ttl = {{ cache_ttl | default(3600) }}
{% else %}
cache_enabled = false
{% endif %}

# Conditional sections
{% if environment == 'production' %}
debug = false
log_level = warning
{% else %}
debug = true
log_level = debug
{% endif %}

# Loops
{% for host in groups['databases'] %}
db_replica_{{ loop.index }} = {{ hostvars[host]['ansible_default_ipv4']['address'] }}
{% endfor %}

# List processing
allowed_hosts = {{ allowed_hosts | join(',') }}

# Filters
uppercase_name = {{ app_name | upper }}
lowercase_env = {{ environment | lower }}
default_value = {{ optional_var | default('default_value') }}
mandatory_value = {{ required_var | mandatory }}
```

### Advanced Template Features

```jinja2
{# Macros #}
{% macro render_server(name, ip, port) %}
server {{ name }} {
    address {{ ip }}:{{ port }};
}
{% endmacro %}

{% for server in backend_servers %}
{{ render_server(server.name, server.ip, server.port) }}
{% endfor %}

{# Conditionals with elif #}
{% if ansible_distribution == 'Ubuntu' %}
package_manager = apt
{% elif ansible_distribution == 'CentOS' %}
package_manager = yum
{% elif ansible_distribution == 'Fedora' %}
package_manager = dnf
{% else %}
package_manager = unknown
{% endif %}

{# Tests #}
{% if database_host is defined %}
db_host = {{ database_host }}
{% endif %}

{% if port is number %}
port = {{ port }}
{% endif %}

{% if services is iterable %}
{% for service in services %}
service_{{ loop.index }} = {{ service }}
{% endfor %}
{% endif %}

{# Filters #}
formatted_date = {{ ansible_date_time.date | regex_replace('-', '/') }}
json_data = {{ complex_var | to_json }}
yaml_data = {{ complex_var | to_yaml }}
base64_encoded = {{ secret | b64encode }}
hashed_password = {{ password | password_hash('sha512') }}
random_password = {{ lookup('password', '/dev/null length=32 chars=ascii_letters,digits') }}

{# Math operations #}
total_memory = {{ ansible_memtotal_mb }}
available_memory = {{ (ansible_memtotal_mb * 0.8) | int }}
max_workers = {{ [ansible_processor_vcpus * 2, 32] | min }}
```

---

## Role Development

### Role Directory Structure

```
roles/
└── webserver/
    ├── README.md              # Role documentation
    ├── defaults/
    │   └── main.yml          # Default variables (lowest precedence)
    ├── files/
    │   ├── script.sh         # Static files
    │   └── config.json
    ├── handlers/
    │   └── main.yml          # Handler definitions
    ├── meta/
    │   └── main.yml          # Role metadata and dependencies
    ├── tasks/
    │   ├── main.yml          # Main task list
    │   ├── install.yml       # Task includes
    │   ├── configure.yml
    │   └── deploy.yml
    ├── templates/
    │   ├── nginx.conf.j2     # Jinja2 templates
    │   └── site.conf.j2
    ├── tests/
    │   ├── inventory         # Test inventory
    │   └── test.yml          # Test playbook
    └── vars/
        └── main.yml          # Role variables (high precedence)
```

### Role Creation

```bash
# Create role skeleton
ansible-galaxy init webserver

# Create role in specific directory
ansible-galaxy init --init-path roles/ webserver
```

### Role Metadata (meta/main.yml)

```yaml
---
galaxy_info:
  author: Your Name
  description: Web server configuration role
  company: Your Company
  license: MIT
  min_ansible_version: 2.9
  platforms:
    - name: Ubuntu
      versions:
        - focal
        - jammy
    - name: EL
      versions:
        - 8
        - 9
  galaxy_tags:
    - web
    - nginx
    - deployment

dependencies:
  - role: common
    vars:
      common_packages:
        - curl
        - wget
  - role: firewall
    vars:
      firewall_allowed_ports:
        - 80
        - 443
```

### Role Variables (defaults/main.yml)

```yaml
---
# Web server configuration
webserver_package: nginx
webserver_service: nginx
webserver_port: 80
webserver_ssl_port: 443

# Application settings
app_name: myapp
app_version: latest
app_user: www-data
app_group: www-data
app_root: /var/www/{{ app_name }}

# Performance tuning
worker_processes: "{{ ansible_processor_vcpus }}"
worker_connections: 1024
keepalive_timeout: 65

# SSL configuration
ssl_enabled: false
ssl_certificate: /etc/ssl/certs/server.crt
ssl_certificate_key: /etc/ssl/private/server.key

# Logging
access_log: /var/log/nginx/access.log
error_log: /var/log/nginx/error.log
log_level: warn
```

### Role Tasks (tasks/main.yml)

```yaml
---
# Main task file for webserver role

- name: Include OS-specific variables
  include_vars: "{{ ansible_os_family }}.yml"

- name: Install web server
  include_tasks: install.yml

- name: Configure web server
  include_tasks: configure.yml

- name: Deploy application
  include_tasks: deploy.yml
  when: deploy_app | default(false)

- name: Ensure web server is running
  service:
    name: "{{ webserver_service }}"
    state: started
    enabled: yes
```

### Task Includes (tasks/install.yml)

```yaml
---
- name: Install web server package
  package:
    name: "{{ webserver_package }}"
    state: present
  register: install_result

- name: Install additional packages
  package:
    name: "{{ item }}"
    state: present
  loop:
    - "{{ ssl_package }}"
    - "{{ compression_package }}"
  when: ssl_enabled or compression_enabled

- name: Create application user
  user:
    name: "{{ app_user }}"
    group: "{{ app_group }}"
    system: yes
    create_home: no
    shell: /bin/false
```

### Role Handlers (handlers/main.yml)

```yaml
---
- name: Restart web server
  service:
    name: "{{ webserver_service }}"
    state: restarted

- name: Reload web server
  service:
    name: "{{ webserver_service }}"
    state: reloaded

- name: Validate configuration
  command: "{{ webserver_package }} -t"
  changed_when: false

- name: Clear cache
  file:
    path: "{{ app_root }}/cache"
    state: absent
```

### Using Roles in Playbooks

```yaml
---
# Simple role usage
- name: Configure web servers
  hosts: webservers
  roles:
    - webserver

# Role with variables
- name: Configure web servers
  hosts: webservers
  roles:
    - role: webserver
      vars:
        webserver_port: 8080
        ssl_enabled: true

# Role with tags
- name: Configure web servers
  hosts: webservers
  roles:
    - role: webserver
      tags: ['web', 'deployment']

# Role with conditionals
- name: Configure web servers
  hosts: webservers
  roles:
    - role: webserver
      when: install_webserver | default(true)

# Mixed tasks and roles
- name: Full deployment
  hosts: webservers
  pre_tasks:
    - name: Update package cache
      apt:
        update_cache: yes
  
  roles:
    - common
    - webserver
    - monitoring
  
  post_tasks:
    - name: Verify deployment
      uri:
        url: http://localhost/health
        status_code: 200
```

### Role Dependencies

Define in `meta/main.yml`:

```yaml
dependencies:
  - role: common
  - role: firewall
    vars:
      firewall_rules:
        - port: 80
        - port: 443
  - role: ssl
    when: ssl_enabled
```

Dependencies are executed before the role itself, in the order listed.

---

## Include and Import

### Include vs Import

**Import** (static):
- Processed at playbook parse time
- Cannot use loops
- Cannot use conditionals on tasks inside
- Better performance
- Use for static content

**Include** (dynamic):
- Processed at runtime
- Can use loops and conditionals
- More flexible
- Use for dynamic content

### Import Tasks

```yaml
# main.yml
- name: Main playbook
  hosts: all
  tasks:
    - import_tasks: pre-checks.yml
    - import_tasks: installation.yml
    - import_tasks: configuration.yml
```

### Include Tasks

```yaml
# Dynamic inclusion with loop
- name: Configure multiple applications
  include_tasks: configure-app.yml
  loop:
    - app1
    - app2
    - app3
  loop_control:
    loop_var: app_name

# Conditional inclusion
- name: Include OS-specific tasks
  include_tasks: "{{ ansible_os_family }}.yml"
```

### Import/Include Playbooks

```yaml
# site.yml - Master playbook
---
- import_playbook: database.yml
- import_playbook: webservers.yml
- import_playbook: loadbalancers.yml

# Conditional import
- import_playbook: production.yml
  when: environment == "production"
```

### Import/Include Roles

```yaml
# Static import
- name: Import role
  import_role:
    name: webserver

# Dynamic include
- name: Include role conditionally
  include_role:
    name: monitoring
  when: enable_monitoring

# Include role with tasks_from
- name: Run specific role tasks
  include_role:
    name: webserver
    tasks_from: deploy
```
