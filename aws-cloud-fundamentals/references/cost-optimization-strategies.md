# AWS Cost Optimization Strategies

Comprehensive guide to reducing and optimizing AWS costs.

---

## Cost Visibility and Monitoring

### AWS Cost Explorer

**Features**:
- Visualize spending patterns
- Forecast future costs
- Identify cost drivers
- Filter by service, region, tag, etc.

**Key reports**:
- Monthly costs by service
- Daily costs for granular analysis
- Reserved Instance utilization and coverage
- Savings Plans utilization and coverage

**Best practices**:
- Review Cost Explorer weekly
- Set up custom reports for key metrics
- Use grouping and filtering effectively
- Export data for deeper analysis

### AWS Budgets

**Budget types**:
- **Cost budgets**: Track spending against threshold
- **Usage budgets**: Monitor service usage (e.g., EC2 hours)
- **Reservation budgets**: Track RI and Savings Plans utilization
- **Savings Plans budgets**: Monitor commitment coverage

**Alert configuration**:
- Set multiple thresholds (50%, 80%, 100%, 120%)
- Email and SNS notifications
- Trigger automated actions (Lambda, Systems Manager)

**Example budget**:
- Monthly budget: $1,000
- Alerts at: $500 (50%), $800 (80%), $1,000 (100%)
- Actions: Email team, notify Slack, trigger Lambda to stop dev instances

### Cost Allocation Tags

**Purpose**: Categorize and track costs by project, team, environment, etc.

**Tag strategy**:
- **Environment**: production, staging, development
- **Project**: project-alpha, project-beta
- **Owner**: team-a, team-b
- **Cost Center**: engineering, marketing, sales
- **Application**: web-app, mobile-api

**Implementation**:
1. Define tagging policy
2. Apply tags to all resources
3. Activate tags in Billing console
4. Use tags in Cost Explorer and reports

**Enforcement**:
- Use AWS Config rules to detect untagged resources
- Implement tag policies in AWS Organizations
- Automate tagging with Lambda or CloudFormation

---

## Compute Cost Optimization

### EC2 Right-Sizing

**Process**:
1. Monitor CloudWatch metrics (CPU, memory, network, disk)
2. Identify underutilized instances (< 40% average utilization)
3. Use AWS Compute Optimizer recommendations
4. Test smaller instance type in non-production
5. Implement change in production
6. Monitor and iterate

**Tools**:
- AWS Compute Optimizer (ML-based recommendations)
- CloudWatch metrics and dashboards
- Third-party tools (CloudHealth, Spot.io)

**Savings**: 20-50% by downsizing overprovisioned instances

### Reserved Instances and Savings Plans

**Reserved Instances**:
- **Standard RI**: Up to 75% savings, 1 or 3 years, specific instance type
- **Convertible RI**: Up to 54% savings, can change instance family
- **Payment options**: All upfront (highest discount), partial upfront, no upfront

**Savings Plans**:
- **Compute Savings Plans**: Up to 66% savings, flexible across instance families, regions, and compute services (EC2, Fargate, Lambda)
- **EC2 Instance Savings Plans**: Up to 72% savings, flexible within instance family in specific region

**Strategy**:
1. Analyze baseline usage (minimum consistent usage)
2. Purchase RIs or Savings Plans for baseline
3. Use On-Demand for variable workloads
4. Review and adjust quarterly

**Example**:
- Baseline: 10 m5.large instances running 24/7
- Purchase: 3-year Compute Savings Plan for 10 instances worth
- Savings: ~$15,000/year vs On-Demand

### Spot Instances

**Characteristics**:
- Up to 90% discount vs On-Demand
- Can be interrupted with 2-minute warning
- Best for fault-tolerant, flexible workloads

**Use cases**:
- Batch processing
- Big data analytics
- CI/CD build servers
- Containerized workloads
- Stateless web servers

**Implementation**:
- Use Spot Fleet or Auto Scaling with mixed instances
- Diversify across instance types and AZs
- Implement graceful shutdown handling
- Use Spot Instance interruption notices

**Tools**:
- EC2 Spot Fleet
- Auto Scaling mixed instances policy
- EKS with Spot instances
- AWS Batch with Spot

### Auto Scaling

**Benefits**:
- Match capacity to demand
- Reduce costs during low-traffic periods
- Improve availability during high-traffic periods

**Scaling policies**:
- **Target tracking**: Maintain specific metric (e.g., 50% CPU)
- **Step scaling**: Scale based on alarm thresholds
- **Scheduled scaling**: Scale at specific times
- **Predictive scaling**: ML-based forecasting

**Example**:
- Baseline: 4 instances (minimum)
- Peak: 20 instances (maximum)
- Target: 60% CPU utilization
- Savings: 60% during off-peak hours

### Instance Scheduling

**Strategy**: Stop non-production instances outside business hours

**Savings calculation**:
- Development environment: 10 instances, 24/7 = 7,200 hours/month
- With scheduling (8 hours/day, 5 days/week): ~160 hours/month
- Savings: 78% on those instances

**Implementation**:
- AWS Instance Scheduler (CloudFormation solution)
- Lambda with EventBridge rules
- Third-party tools (CloudHealth, Skeddly)
- Tag-based automation

**Example schedule**:
- Dev/Test: 8 AM - 6 PM, Monday-Friday
- Staging: 6 AM - 10 PM, Monday-Friday
- Production: 24/7 (no scheduling)

---

## Storage Cost Optimization

### S3 Storage Classes and Lifecycle Policies

**Cost comparison** (per GB/month):
- S3 Standard: $0.023
- S3 Intelligent-Tiering: $0.023 + monitoring fee
- S3 Standard-IA: $0.0125
- S3 One Zone-IA: $0.01
- S3 Glacier Instant Retrieval: $0.004
- S3 Glacier Flexible Retrieval: $0.0036
- S3 Glacier Deep Archive: $0.00099

**Lifecycle policy example**:
```
Day 0-30: S3 Standard
Day 31-90: S3 Standard-IA
Day 91-365: S3 Glacier Flexible Retrieval
Day 366+: S3 Glacier Deep Archive
```

**Savings**: 80-95% for archival data

### EBS Volume Optimization

**Strategies**:
1. **Delete unattached volumes**: Identify with AWS Config or CLI
2. **Snapshot old volumes**: Delete volume, keep snapshot (cheaper)
3. **Use gp3 instead of gp2**: Same performance, 20% cheaper
4. **Right-size volumes**: Reduce oversized volumes
5. **Delete old snapshots**: Implement lifecycle policies

**Cost comparison**:
- gp3: $0.08/GB/month
- gp2: $0.10/GB/month
- io2: $0.125/GB/month + IOPS charges
- Snapshots: $0.05/GB/month (incremental)

**Snapshot lifecycle**:
- Daily snapshots: Keep 7 days
- Weekly snapshots: Keep 4 weeks
- Monthly snapshots: Keep 12 months
- Delete older snapshots

### EFS Cost Optimization

**Storage classes**:
- Standard: $0.30/GB/month
- Infrequent Access (IA): $0.025/GB/month

**Lifecycle management**:
- Automatically move files to IA after 7, 14, 30, 60, or 90 days
- Savings: 92% for infrequently accessed files

**Best practices**:
- Enable lifecycle management
- Use Intelligent-Tiering
- Monitor access patterns
- Consider S3 for archival data

---

## Database Cost Optimization

### RDS Optimization

**Right-sizing**:
- Monitor CloudWatch metrics (CPU, memory, IOPS)
- Use Performance Insights
- Downsize overprovisioned instances
- Use burstable instances (db.t3) for variable workloads

**Reserved Instances**:
- Up to 69% savings vs On-Demand
- 1-year or 3-year commitment
- All upfront, partial upfront, or no upfront

**Storage optimization**:
- Use gp3 instead of gp2 (20% cheaper)
- Enable storage autoscaling
- Delete old snapshots
- Use cross-region snapshot copy only when necessary

**Multi-AZ considerations**:
- Disable Multi-AZ for dev/test environments
- Use read replicas for read scaling (cheaper than larger instance)

### DynamoDB Optimization

**Capacity modes**:
- **On-Demand**: Pay per request, no capacity planning
- **Provisioned**: Reserve capacity, up to 76% cheaper

**Strategy**:
- Use provisioned for predictable workloads
- Use on-demand for unpredictable or spiky workloads
- Enable auto-scaling for provisioned capacity

**Table design**:
- Use single-table design to reduce costs
- Implement TTL to automatically delete old data
- Use DynamoDB Streams only when needed
- Archive old data to S3 with DynamoDB export

**Reserved capacity**:
- Up to 76% savings vs on-demand
- 1-year or 3-year commitment
- Applies to provisioned capacity

---

## Network Cost Optimization

### Data Transfer Costs

**Pricing**:
- Data IN: Free
- Data OUT to internet: $0.09/GB (first 10 TB)
- Data OUT to CloudFront: $0.02/GB
- Data between regions: $0.02/GB
- Data within same AZ: Free
- Data between AZs: $0.01/GB in/out

**Optimization strategies**:
1. **Use CloudFront**: Cheaper egress than direct S3/EC2
2. **Keep traffic within same region**: Avoid cross-region transfer
3. **Use VPC endpoints**: Free transfer to S3/DynamoDB from EC2
4. **Compress data**: Reduce transfer volume
5. **Use Direct Connect**: Cheaper for large, consistent transfers

### NAT Gateway Costs

**Pricing**:
- Per hour: $0.045
- Per GB processed: $0.045

**Alternatives**:
1. **VPC endpoints**: Free for S3 and DynamoDB
2. **NAT instance**: Cheaper for low traffic (but less reliable)
3. **Public subnets**: For resources that can be public

**Savings example**:
- NAT Gateway: $32/month + $45/TB
- VPC endpoints for S3/DynamoDB: Free
- Savings: $32/month + data processing fees

### Load Balancer Optimization

**Cost comparison**:
- Application Load Balancer: $0.0225/hour + $0.008/LCU
- Network Load Balancer: $0.0225/hour + $0.006/NLCU
- Classic Load Balancer: $0.025/hour + $0.008/GB

**Optimization**:
- Use ALB for multiple applications (host-based routing)
- Consolidate load balancers where possible
- Delete unused load balancers
- Use NLB for high-throughput, low-latency needs

---

## Serverless Cost Optimization

### Lambda Optimization

**Memory allocation**:
- More memory = more CPU = faster execution
- Test different memory settings
- Use AWS Lambda Power Tuning tool
- Optimal memory often reduces total cost

**Invocation reduction**:
- Batch processing (SQS, Kinesis)
- Implement caching (API Gateway, ElastiCache)
- Use Step Functions for orchestration (cheaper than multiple Lambda invocations)

**Duration optimization**:
- Optimize code performance
- Minimize cold starts (provisioned concurrency for critical functions)
- Use compiled languages for CPU-intensive tasks
- Reduce deployment package size

### API Gateway Optimization

**HTTP API vs REST API**:
- HTTP API: $1.00 per million requests
- REST API: $3.50 per million requests
- Use HTTP API when possible (71% cheaper)

**Caching**:
- Enable caching to reduce backend invocations
- Cache sizes: 0.5 GB to 237 GB
- Cost: $0.02/hour for 0.5 GB cache
- Savings: Reduce Lambda invocations and database queries

---

## Monitoring and Governance

### AWS Cost Anomaly Detection

**Features**:
- ML-based anomaly detection
- Automatic alerts for unusual spending
- Root cause analysis
- Integration with AWS Budgets

**Setup**:
1. Create cost monitor
2. Define alert threshold (e.g., $100)
3. Configure SNS notifications
4. Review anomalies and take action

### AWS Trusted Advisor

**Cost optimization checks**:
- Idle RDS instances
- Underutilized EC2 instances
- Unassociated Elastic IPs
- Low utilization EBS volumes
- Idle load balancers
- Underutilized Redshift clusters

**Access**:
- Basic checks: All accounts
- Full checks: Business or Enterprise support

### AWS Organizations and SCPs

**Centralized management**:
- Consolidated billing (volume discounts)
- Reserved Instance sharing
- Savings Plans sharing
- Centralized cost allocation tags

**Service Control Policies**:
- Prevent expensive instance types
- Restrict regions (avoid expensive regions)
- Enforce tagging requirements
- Prevent public S3 buckets

**Example SCP** (prevent large instances):
```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Deny",
    "Action": "ec2:RunInstances",
    "Resource": "arn:aws:ec2:*:*:instance/*",
    "Condition": {
      "StringNotLike": {
        "ec2:InstanceType": ["t3.*", "t2.*", "m5.*"]
      }
    }
  }]
}
```

---

## Cost Optimization Checklist

### Monthly Tasks
- [ ] Review Cost Explorer for trends and anomalies
- [ ] Check AWS Budgets alerts
- [ ] Review Trusted Advisor recommendations
- [ ] Identify and delete unused resources
- [ ] Review and optimize largest cost drivers

### Quarterly Tasks
- [ ] Right-size EC2 instances based on utilization
- [ ] Review and adjust Reserved Instances and Savings Plans
- [ ] Analyze data transfer costs and optimize
- [ ] Review storage lifecycle policies
- [ ] Audit IAM policies and remove unused permissions

### Annual Tasks
- [ ] Comprehensive cost review and optimization
- [ ] Evaluate Reserved Instance and Savings Plans renewals
- [ ] Review architecture for cost efficiency
- [ ] Update tagging strategy
- [ ] Benchmark costs against industry standards

### Continuous Tasks
- [ ] Tag all new resources
- [ ] Implement auto-scaling for variable workloads
- [ ] Use Spot instances for fault-tolerant workloads
- [ ] Enable lifecycle policies for S3 and EBS snapshots
- [ ] Monitor and respond to cost anomalies
