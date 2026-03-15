# VPC Networking Guide

Comprehensive guide to AWS Virtual Private Cloud (VPC) networking.

---

## VPC Fundamentals

### What is a VPC?

A Virtual Private Cloud (VPC) is an isolated network within AWS where you launch resources. It provides:
- Complete control over network configuration
- IP address range selection
- Subnet creation
- Route table configuration
- Network gateway management
- Security controls

### Default vs Custom VPC

**Default VPC**:
- Created automatically in each region
- CIDR block: 172.31.0.0/16
- Public subnet in each Availability Zone
- Internet Gateway attached
- Default security group and NACL
- Good for getting started quickly

**Custom VPC**:
- You define CIDR block
- You create subnets
- You configure routing
- Full control over security
- Production workloads

---

## CIDR Blocks and IP Addressing

### CIDR Notation

**Format**: `10.0.0.0/16`
- **10.0.0.0**: Network address
- **/16**: Subnet mask (number of fixed bits)

**Size calculation**:
- /16 = 65,536 IP addresses (2^16)
- /24 = 256 IP addresses (2^8)
- /28 = 16 IP addresses (2^4)

### Allowed CIDR Ranges

**Private IP ranges** (RFC 1918):
- 10.0.0.0/8 (10.0.0.0 - 10.255.255.255)
- 172.16.0.0/12 (172.16.0.0 - 172.31.255.255)
- 192.168.0.0/16 (192.168.0.0 - 192.168.255.255)

**VPC CIDR constraints**:
- Minimum: /28 (16 IPs)
- Maximum: /16 (65,536 IPs)
- Can add secondary CIDR blocks later

### Reserved IP Addresses

AWS reserves 5 IPs in each subnet:
- **10.0.0.0**: Network address
- **10.0.0.1**: VPC router
- **10.0.0.2**: DNS server
- **10.0.0.3**: Reserved for future use
- **10.0.0.255**: Network broadcast (not supported in VPC)

**Example**: 10.0.0.0/24 subnet has 256 IPs, but only 251 usable.

---

## Subnets

### Public vs Private Subnets

**Public Subnet**:
- Has route to Internet Gateway
- Instances can have public IPs
- Directly accessible from internet (if security group allows)
- Use for: Web servers, load balancers, bastion hosts

**Private Subnet**:
- No direct route to Internet Gateway
- Instances have private IPs only
- Access internet via NAT Gateway/Instance
- Use for: Application servers, databases, internal services

### Subnet Design Best Practices

**Multi-AZ deployment**:
```
VPC: 10.0.0.0/16

us-east-1a:
  Public:  10.0.1.0/24
  Private: 10.0.11.0/24

us-east-1b:
  Public:  10.0.2.0/24
  Private: 10.0.12.0/24

us-east-1c:
  Public:  10.0.3.0/24
  Private: 10.0.13.0/24
```

**Sizing strategy**:
- Leave room for growth
- Use /24 for most subnets (251 usable IPs)
- Use /20 or /21 for large subnets (EKS, etc.)
- Reserve CIDR space for future subnets

---

## Internet Connectivity

### Internet Gateway (IGW)

**Purpose**: Enable internet access for VPC

**Characteristics**:
- Horizontally scaled, redundant, highly available
- No bandwidth constraints
- One IGW per VPC
- Free (no charges)

**Setup**:
1. Create and attach IGW to VPC
2. Add route to public subnet route table: `0.0.0.0/0 → IGW`
3. Assign public IP or Elastic IP to instances
4. Configure security groups to allow traffic

### NAT Gateway

**Purpose**: Allow private subnet instances to access internet (outbound only)

**Characteristics**:
- Managed service (AWS handles availability)
- Deployed in public subnet
- Requires Elastic IP
- Charged per hour + data processed
- 45 Gbps bandwidth

**Setup**:
1. Create NAT Gateway in public subnet
2. Allocate Elastic IP
3. Add route to private subnet route table: `0.0.0.0/0 → NAT Gateway`

**High Availability**: Deploy NAT Gateway in each AZ for redundancy

### NAT Instance (Legacy)

**Alternative to NAT Gateway**:
- EC2 instance with NAT AMI
- You manage availability and scaling
- Lower cost for small workloads
- Can use as bastion host

**Disadvantages**:
- Single point of failure (unless you build HA)
- Bandwidth limited by instance type
- Requires management and patching

---

## Route Tables

### How Routing Works

**Route table**: Set of rules (routes) determining where network traffic is directed

**Route priority**: Most specific route wins (longest prefix match)

**Example route table**:
| Destination | Target | Purpose |
|-------------|--------|---------|
| 10.0.0.0/16 | local | VPC internal traffic |
| 0.0.0.0/0 | igw-xxx | Internet traffic |

### Main vs Custom Route Tables

**Main route table**:
- Automatically created with VPC
- Applied to subnets without explicit association
- Best practice: Leave main table for private subnets

**Custom route tables**:
- Created for specific routing needs
- Explicitly associated with subnets
- Use for public subnets, VPN connections, etc.

### Route Table Best Practices

1. Create separate route tables for public and private subnets
2. Use descriptive names and tags
3. Document route purposes
4. Minimize number of route tables for simplicity
5. Use VPC endpoints to avoid internet routing for AWS services

---

## Security

### Security Groups

**Characteristics**:
- Stateful firewall (return traffic automatically allowed)
- Applied at instance/ENI level
- Allow rules only (no deny rules)
- Evaluated as a whole (not in order)
- Default: Deny all inbound, allow all outbound

**Rule components**:
- **Type**: Protocol (SSH, HTTP, Custom TCP, etc.)
- **Protocol**: TCP, UDP, ICMP
- **Port range**: 22, 80, 443, 1024-65535, etc.
- **Source/Destination**: IP CIDR, security group ID, prefix list

**Example rules**:
| Type | Protocol | Port | Source | Purpose |
|------|----------|------|--------|---------|
| SSH | TCP | 22 | 203.0.113.0/24 | Admin access |
| HTTP | TCP | 80 | 0.0.0.0/0 | Web traffic |
| MySQL | TCP | 3306 | sg-app | App to DB |

**Best practices**:
- Use security group references instead of IP addresses
- Create separate security groups for each tier (web, app, DB)
- Restrict SSH/RDP to specific IPs
- Use descriptive names and descriptions
- Regularly audit and remove unused rules

### Network ACLs (NACLs)

**Characteristics**:
- Stateless firewall (must allow return traffic explicitly)
- Applied at subnet level
- Allow and deny rules
- Evaluated in order (lowest rule number first)
- Default: Allow all inbound and outbound

**Rule components**:
- **Rule number**: 1-32766 (lower numbers evaluated first)
- **Type**: Protocol
- **Protocol**: TCP, UDP, ICMP, or number
- **Port range**: Port or range
- **Source/Destination**: IP CIDR
- **Allow/Deny**: Action

**Example NACL**:
| Rule # | Type | Protocol | Port | Source | Allow/Deny |
|--------|------|----------|------|--------|------------|
| 100 | HTTP | TCP | 80 | 0.0.0.0/0 | ALLOW |
| 110 | HTTPS | TCP | 443 | 0.0.0.0/0 | ALLOW |
| 120 | SSH | TCP | 22 | 203.0.113.0/24 | ALLOW |
| * | All | All | All | 0.0.0.0/0 | DENY |

**When to use**:
- Additional layer of security (defense in depth)
- Block specific IP addresses (security groups can't deny)
- Subnet-level controls

**Best practices**:
- Use security groups as primary control
- Use NACLs for additional protection
- Leave rule number gaps (100, 110, 120) for future insertions
- Remember to allow ephemeral ports for return traffic

### Security Groups vs NACLs

| Feature | Security Group | Network ACL |
|---------|----------------|-------------|
| **Level** | Instance/ENI | Subnet |
| **State** | Stateful | Stateless |
| **Rules** | Allow only | Allow and Deny |
| **Evaluation** | All rules | In order |
| **Default** | Deny inbound | Allow all |

---

## VPC Peering

### What is VPC Peering?

Network connection between two VPCs enabling private communication using private IPs.

**Characteristics**:
- No single point of failure
- No bandwidth bottleneck
- Traffic stays on AWS network
- Can peer across regions and accounts
- Non-transitive (A↔B and B↔C doesn't mean A↔C)

### Setup Process

1. **Create peering connection**: Requester VPC sends request
2. **Accept request**: Accepter VPC accepts
3. **Update route tables**: Add routes in both VPCs
4. **Update security groups**: Allow traffic from peer VPC CIDR

**Example routes**:
- VPC A (10.0.0.0/16) route table: `10.1.0.0/16 → pcx-xxx`
- VPC B (10.1.0.0/16) route table: `10.0.0.0/16 → pcx-xxx`

### Limitations

- CIDR blocks cannot overlap
- No transitive peering
- No edge-to-edge routing (can't route through VPC to on-premises)
- Maximum 125 peering connections per VPC

---

## VPN Connections

### Site-to-Site VPN

**Purpose**: Connect on-premises network to VPC

**Components**:
- **Virtual Private Gateway (VGW)**: VPN concentrator on AWS side
- **Customer Gateway (CGW)**: VPN device on customer side
- **VPN Connection**: IPsec tunnel between VGW and CGW

**Setup**:
1. Create Virtual Private Gateway and attach to VPC
2. Create Customer Gateway (specify public IP of on-prem device)
3. Create VPN Connection
4. Download configuration file
5. Configure on-premises VPN device
6. Update route tables

**Characteristics**:
- Encrypted traffic over internet
- Up to 1.25 Gbps per tunnel
- Two tunnels for redundancy
- Charged per hour + data transfer

### AWS Direct Connect

**Purpose**: Dedicated network connection from on-premises to AWS

**Benefits**:
- More consistent network performance
- Reduced bandwidth costs
- Higher throughput (1 Gbps or 10 Gbps)
- Private connectivity (doesn't traverse internet)

**Use cases**:
- Large data transfers
- Real-time data feeds
- Hybrid cloud architectures

---

## VPC Endpoints

### Why VPC Endpoints?

**Problem**: Accessing AWS services (S3, DynamoDB) from private subnet requires NAT Gateway and internet routing.

**Solution**: VPC Endpoints provide private connection to AWS services without internet.

**Benefits**:
- No NAT Gateway needed (cost savings)
- Better security (traffic doesn't leave AWS network)
- Lower latency
- No bandwidth constraints

### Interface Endpoints (PrivateLink)

**Characteristics**:
- Elastic Network Interface (ENI) with private IP
- Powered by AWS PrivateLink
- Supports most AWS services
- Charged per hour + data processed

**Supported services**: EC2, SNS, SQS, CloudWatch, KMS, etc.

**Setup**:
1. Create interface endpoint
2. Select VPC and subnets
3. Configure security groups
4. Access service via endpoint DNS name

### Gateway Endpoints

**Characteristics**:
- Route table entry (not an ENI)
- Free (no charges)
- Only for S3 and DynamoDB

**Setup**:
1. Create gateway endpoint
2. Select VPC and route tables
3. Endpoint automatically adds route to selected route tables

**Route added**: `pl-xxx (S3 prefix list) → vpce-xxx`

---

## VPC Flow Logs

### What are Flow Logs?

Capture information about IP traffic going to and from network interfaces in VPC.

**Capture levels**:
- VPC level (all ENIs in VPC)
- Subnet level (all ENIs in subnet)
- ENI level (specific network interface)

**Destinations**:
- CloudWatch Logs
- S3 bucket
- Kinesis Data Firehose

### Log Format

**Default format**:
```
<version> <account-id> <interface-id> <srcaddr> <dstaddr> <srcport> <dstport> <protocol> <packets> <bytes> <start> <end> <action> <log-status>
```

**Example**:
```
2 123456789012 eni-abc123 203.0.113.5 10.0.0.15 49152 80 6 10 5000 1620000000 1620000060 ACCEPT OK
```

**Fields**:
- **srcaddr/dstaddr**: Source and destination IPs
- **srcport/dstport**: Source and destination ports
- **protocol**: IANA protocol number (6=TCP, 17=UDP, 1=ICMP)
- **action**: ACCEPT or REJECT
- **log-status**: OK, NODATA, SKIPDATA

### Use Cases

1. **Troubleshooting connectivity**: Why can't instance A reach instance B?
2. **Security analysis**: Detect unusual traffic patterns
3. **Compliance**: Network traffic auditing
4. **Cost optimization**: Identify high-traffic sources

### Analyzing Flow Logs

**Common queries**:

**Top talkers** (most traffic):
```sql
SELECT srcaddr, SUM(bytes) as total_bytes
FROM flow_logs
GROUP BY srcaddr
ORDER BY total_bytes DESC
LIMIT 10
```

**Rejected connections** (security group blocks):
```sql
SELECT srcaddr, dstaddr, dstport, COUNT(*) as attempts
FROM flow_logs
WHERE action = 'REJECT'
GROUP BY srcaddr, dstaddr, dstport
ORDER BY attempts DESC
```

---

## Advanced VPC Features

### IPv6 Support

**Characteristics**:
- All IPv6 addresses are public
- AWS assigns /56 CIDR block to VPC
- You assign /64 CIDR block to each subnet
- Dual-stack (IPv4 and IPv6) supported

**Setup**:
1. Associate IPv6 CIDR block with VPC
2. Associate IPv6 CIDR block with subnets
3. Update route tables (`::/0 → IGW`)
4. Update security groups
5. Assign IPv6 addresses to instances

### VPC Sharing (AWS RAM)

**Purpose**: Share subnets with other AWS accounts in same organization

**Benefits**:
- Centralized network management
- Reduced VPC sprawl
- Shared services (Active Directory, monitoring)

**How it works**:
- Owner account creates and shares subnets
- Participant accounts launch resources in shared subnets
- Each account manages own resources and security groups

### Transit Gateway

**Purpose**: Connect multiple VPCs and on-premises networks through central hub

**Benefits**:
- Simplifies network topology
- Reduces number of connections (hub-and-spoke vs mesh)
- Centralized routing
- Supports thousands of VPCs

**Use cases**:
- Large organizations with many VPCs
- Complex hybrid cloud architectures
- Centralized egress/ingress

---

## Troubleshooting Connectivity

### Systematic Approach

1. **Verify route tables**: Does route exist for destination?
2. **Check security groups**: Are required ports allowed?
3. **Check NACLs**: Are inbound and outbound rules correct?
4. **Verify instance**: Is service running? Is OS firewall configured?
5. **Check VPC Flow Logs**: Is traffic being rejected?

### Common Issues

**Cannot connect to instance from internet**:
- Instance in private subnet (no IGW route)
- No public IP or Elastic IP assigned
- Security group doesn't allow inbound traffic
- NACL blocking traffic
- Route table missing IGW route

**Cannot connect between instances in same VPC**:
- Security groups not allowing traffic
- NACLs blocking traffic
- Instances in different subnets with no route
- OS-level firewall blocking

**Cannot access S3 from private subnet**:
- No NAT Gateway (if not using VPC endpoint)
- NAT Gateway in wrong subnet
- Route table not pointing to NAT Gateway
- VPC endpoint policy too restrictive

### VPC Reachability Analyzer

**Purpose**: Automated network diagnostics tool

**Features**:
- Analyzes path between source and destination
- Identifies configuration issues
- No packet sending required (static analysis)
- Checks route tables, security groups, NACLs, etc.

**Use when**: Troubleshooting connectivity issues, validating network configuration
