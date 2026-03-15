# Azure Networking Guide

Comprehensive guide to Azure networking services and architecture.

---

## Virtual Network (VNet) Fundamentals

### VNet Basics

**Characteristics**:
- Isolated network in Azure
- Define IP address space (CIDR notation)
- Segment into subnets
- Resources in same VNet can communicate by default
- Regional resource (can peer across regions)

**Address space**:
- Private IP ranges (RFC 1918)
- 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16
- Minimum /29 (8 IPs), maximum /8

**Reserved IPs per subnet**:
- .0: Network address
- .1: Default gateway
- .2, .3: Azure DNS
- .255: Broadcast (not used in Azure)

### Subnets

**Purpose**: Segment VNet for organization and security

**Best practices**:
- Create separate subnets for different tiers (web, app, data)
- Use /24 for most subnets (251 usable IPs)
- Reserve address space for future growth
- Use descriptive names

**Special subnets**:
- **GatewaySubnet**: For VPN/ExpressRoute gateways (minimum /27)
- **AzureFirewallSubnet**: For Azure Firewall (minimum /26)
- **AzureBastionSubnet**: For Azure Bastion (minimum /26)

---

## Network Security

### Network Security Groups (NSGs)

**Characteristics**:
- Stateful firewall
- Applied to subnet or NIC
- Inbound and outbound rules
- Priority-based evaluation (100-4096)

**Rule components**:
- Priority (lower number = higher priority)
- Source/Destination (IP, CIDR, service tag, ASG)
- Protocol (TCP, UDP, ICMP, Any)
- Port range
- Action (Allow or Deny)

**Default rules** (cannot be deleted):
- Allow VNet inbound/outbound
- Allow Azure Load Balancer inbound
- Deny all inbound
- Allow internet outbound

**Best practices**:
- Use service tags (e.g., Internet, VirtualNetwork, AzureLoadBalancer)
- Use Application Security Groups for logical grouping
- Leave gaps in priority numbers (100, 110, 120)
- Document rule purposes

### Application Security Groups (ASGs)

**Purpose**: Group VMs logically for NSG rules

**Benefits**:
- No need to specify IP addresses
- Easier to manage as infrastructure scales
- Reusable across multiple NSGs

**Example**:
```
ASG: WebServers (contains web tier VMs)
ASG: AppServers (contains app tier VMs)
ASG: DatabaseServers (contains database VMs)

NSG rule: Allow AppServers → DatabaseServers on port 1433
```

### Azure Firewall

**Features**:
- Fully stateful firewall as a service
- Built-in high availability
- Unrestricted cloud scalability
- Application and network filtering rules
- Threat intelligence-based filtering

**Rule types**:
- **Application rules**: FQDN-based filtering (HTTP/HTTPS)
- **Network rules**: IP address, port, protocol filtering
- **NAT rules**: Inbound DNAT

**Use cases**:
- Centralized network security
- Hub-and-spoke topology
- Outbound filtering
- Threat protection

---

## Load Balancing

### Azure Load Balancer

**Characteristics**:
- Layer 4 (TCP/UDP)
- Public and internal load balancers
- Zone-redundant and zonal options
- Health probes

**SKUs**:
- **Basic**: Free, limited features, no SLA
- **Standard**: Paid, advanced features, 99.99% SLA

**Components**:
- **Frontend IP**: Public or private IP
- **Backend pool**: VMs or VMSS instances
- **Health probes**: TCP, HTTP, HTTPS
- **Load balancing rules**: Distribute traffic
- **Inbound NAT rules**: Port forwarding

**Use cases**:
- Distribute traffic across VMs
- High availability for applications
- Outbound connectivity for private VMs

### Application Gateway

**Characteristics**:
- Layer 7 (HTTP/HTTPS) load balancer
- URL-based routing
- SSL termination
- Web Application Firewall (WAF)
- Autoscaling

**Features**:
- **Path-based routing**: Route based on URL path
- **Multi-site hosting**: Host multiple websites
- **Redirection**: HTTP to HTTPS, URL rewriting
- **Session affinity**: Cookie-based
- **WebSocket and HTTP/2 support**

**WAF**:
- OWASP Core Rule Set
- Protection against SQL injection, XSS, etc.
- Custom rules
- Bot protection

**Use cases**:
- Web applications
- Microservices
- Multi-tenant applications

### Traffic Manager

**Characteristics**:
- DNS-based global load balancer
- Distributes traffic across regions
- Multiple routing methods

**Routing methods**:
- **Priority**: Failover to secondary region
- **Weighted**: Distribute traffic by percentage
- **Performance**: Route to closest endpoint
- **Geographic**: Route based on user location
- **Multivalue**: Return multiple healthy endpoints
- **Subnet**: Route based on source IP subnet

**Use cases**:
- Global applications
- Disaster recovery
- A/B testing
- Geographic routing

---

## Hybrid Connectivity

### VPN Gateway

**Types**:
- **Site-to-Site**: Connect on-premises network to Azure
- **Point-to-Site**: Connect individual clients to Azure
- **VNet-to-VNet**: Connect Azure VNets

**SKUs**:
- **Basic**: 10 tunnels, 100 Mbps
- **VpnGw1-5**: 30-100 tunnels, 650 Mbps - 10 Gbps
- **VpnGw1-5AZ**: Zone-redundant versions

**Configuration**:
1. Create Virtual Network Gateway
2. Create Local Network Gateway (on-premises)
3. Create Connection
4. Configure on-premises VPN device

**Use cases**:
- Hybrid cloud connectivity
- Remote access
- Multi-region connectivity

### ExpressRoute

**Characteristics**:
- Private connection to Azure
- Doesn't traverse public internet
- Higher reliability and security
- Consistent latencies
- Up to 100 Gbps bandwidth

**Connectivity models**:
- **CloudExchange co-location**: At cloud exchange facility
- **Point-to-point Ethernet**: Direct connection
- **Any-to-any (IPVPN)**: Integrate Azure into WAN

**Peering types**:
- **Private peering**: Access VNets
- **Microsoft peering**: Access Microsoft 365, Dynamics 365, Azure public services

**Use cases**:
- Large data transfers
- Hybrid cloud architectures
- Disaster recovery
- Compliance requirements

---

## VNet Peering

### Characteristics

- Connect VNets in same or different regions
- Low latency, high bandwidth
- Traffic stays on Microsoft backbone
- No downtime during setup

### Types

**VNet peering**: Same region

**Global VNet peering**: Different regions

### Configuration

**Requirements**:
- Non-overlapping IP address spaces
- Peering must be configured in both VNets

**Options**:
- Allow forwarded traffic
- Allow gateway transit
- Use remote gateways

**Use cases**:
- Hub-and-spoke topology
- Cross-region connectivity
- Resource sharing across VNets

---

## DNS

### Azure DNS

**Features**:
- Host DNS domains in Azure
- Manage records using Azure tools
- Anycast network for fast responses
- RBAC and activity logs

**Record types**:
- A, AAAA, CNAME, MX, NS, PTR, SOA, SRV, TXT

**Use cases**:
- Public DNS hosting
- Alias records for Azure resources
- Integration with Azure services

### Private DNS

**Features**:
- DNS resolution within VNets
- No need for custom DNS solution
- Automatic hostname record management
- Split-horizon DNS support

**Use cases**:
- Name resolution between VNets
- Hybrid scenarios with on-premises
- Service discovery

---

## Network Monitoring

### Network Watcher

**Tools**:
- **IP flow verify**: Check if traffic is allowed/denied
- **Next hop**: Determine next hop for traffic
- **Connection troubleshoot**: Test connectivity between resources
- **Packet capture**: Capture network traffic
- **VPN troubleshoot**: Diagnose VPN issues

**Monitoring**:
- **NSG flow logs**: Log traffic through NSGs
- **Traffic Analytics**: Visualize network traffic patterns
- **Connection Monitor**: Monitor endpoint connectivity

### Azure Monitor

**Network metrics**:
- Bytes in/out
- Packets in/out
- Dropped packets
- Connection count

**Alerts**:
- Set thresholds for metrics
- Proactive notifications
- Integration with Action Groups

---

## Best Practices

1. **Use hub-and-spoke topology** for enterprise networks
2. **Implement NSGs on subnets** for defense in depth
3. **Use Azure Firewall** for centralized security
4. **Enable NSG flow logs** for traffic analysis
5. **Use private endpoints** for PaaS services
6. **Implement ExpressRoute** for production hybrid connectivity
7. **Use Traffic Manager** for global load balancing
8. **Enable DDoS Protection Standard** for public-facing applications
9. **Use Azure Bastion** for secure VM access
10. **Monitor with Network Watcher** and set up alerts
