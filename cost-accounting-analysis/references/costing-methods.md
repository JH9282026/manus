# Costing Methods

## Introduction

Costing methods are systematic approaches used by organizations to accumulate, assign, and analyze costs associated with producing goods or delivering services. The choice of costing method depends on factors such as the nature of the production process, product diversity, cost structure, and the level of cost accuracy required for decision-making.

This reference provides comprehensive coverage of the major costing methodologies used in practice, including their principles, applications, advantages, and limitations.

## Job Order Costing

### Overview

Job order costing is used when products or services are unique, customized, or produced in distinct batches. Each job or order is treated as a separate cost object, and costs are accumulated specifically for that job.

### Key Characteristics

- **Unique Products**: Each job has distinct specifications and requirements
- **Cost Accumulation**: Costs are tracked by individual job or batch
- **Direct Tracing**: Direct materials and direct labor are traced to specific jobs
- **Overhead Allocation**: Manufacturing overhead is allocated using predetermined rates
- **Job Cost Sheet**: A document that accumulates all costs for a specific job

### Process Flow

1. **Order Receipt**: Customer places an order or management authorizes a job
2. **Job Number Assignment**: Unique identifier assigned to track costs
3. **Materials Requisition**: Materials are withdrawn from inventory and charged to the job
4. **Labor Time Tracking**: Direct labor hours are recorded and charged to the job
5. **Overhead Application**: Overhead is applied using predetermined rate × actual activity
6. **Job Completion**: Total costs are calculated and transferred to finished goods
7. **Cost Analysis**: Unit cost is determined by dividing total job cost by units produced

### Predetermined Overhead Rate

**Calculation**:
```
Predetermined Overhead Rate = Estimated Total Manufacturing Overhead / Estimated Total Allocation Base
```

**Common Allocation Bases**:
- Direct labor hours
- Direct labor cost
- Machine hours
- Direct materials cost

**Application**:
```
Overhead Applied to Job = Predetermined Overhead Rate × Actual Allocation Base for Job
```

### Over- and Under-Applied Overhead

**Causes**:
- Actual overhead differs from estimated overhead
- Actual activity level differs from estimated activity level

**Treatment**:
- **Small amounts**: Adjust Cost of Goods Sold
- **Large amounts**: Prorate among Work-in-Process, Finished Goods, and Cost of Goods Sold

### Industries and Applications

- **Construction**: Buildings, infrastructure projects
- **Custom Manufacturing**: Specialized machinery, custom furniture
- **Printing**: Custom print jobs, publications
- **Professional Services**: Legal cases, consulting projects, advertising campaigns
- **Healthcare**: Patient treatments, surgical procedures
- **Shipbuilding**: Custom vessels
- **Aerospace**: Custom aircraft components

### Advantages

- Provides detailed cost information for each job
- Enables accurate pricing for custom work
- Facilitates profitability analysis by job
- Supports cost control through job-level monitoring
- Helps identify cost overruns early

### Limitations

- More complex and costly to maintain than process costing
- Requires detailed tracking systems
- Overhead allocation may be arbitrary
- Can be inaccurate if predetermined rates are not well-estimated

## Process Costing

### Overview

Process costing is used when homogeneous products are produced in a continuous flow through a series of processes or departments. Costs are accumulated by process or department and then averaged over all units produced.

### Key Characteristics

- **Homogeneous Products**: Identical or very similar units
- **Continuous Production**: Ongoing production flow
- **Cost Accumulation**: By process or department
- **Cost Averaging**: Costs divided equally among all units
- **Sequential Processing**: Products flow through multiple departments

### Process Flow

1. **Cost Accumulation**: Costs are collected by department/process
2. **Equivalent Units Calculation**: Partially completed units converted to equivalent whole units
3. **Cost per Equivalent Unit**: Total costs divided by equivalent units
4. **Cost Assignment**: Costs assigned to completed units and ending work-in-process
5. **Transfer to Next Department**: Costs flow with products to subsequent processes

### Equivalent Units of Production

**Concept**: Partially completed units expressed in terms of completed units.

**Example**: 100 units that are 60% complete = 60 equivalent units

**Methods**:

#### Weighted-Average Method
- Combines beginning inventory costs with current period costs
- Does not distinguish between work from prior period and current period
- Simpler to calculate

**Equivalent Units Calculation**:
```
Equivalent Units = Units Completed + (Ending WIP Units × % Complete)
```

#### FIFO Method
- Separates beginning inventory costs from current period costs
- Focuses on current period work
- More complex but provides better cost control information

**Equivalent Units Calculation**:
```
Equivalent Units = (Beginning WIP Units × % to Complete) + Units Started and Completed + (Ending WIP Units × % Complete)
```

### Production Cost Report

A comprehensive report for each department showing:

1. **Physical Flow of Units**: Beginning inventory, units started, units completed, ending inventory
2. **Equivalent Units**: Calculation for materials and conversion costs
3. **Cost per Equivalent Unit**: Total costs divided by equivalent units
4. **Cost Reconciliation**: Costs accounted for (completed units + ending WIP)

### Industries and Applications

- **Oil Refining**: Gasoline, diesel, petrochemicals
- **Chemical Manufacturing**: Industrial chemicals, pharmaceuticals
- **Food Processing**: Beverages, packaged foods, dairy products
- **Textiles**: Fabric production, garment manufacturing
- **Paper Manufacturing**: Paper products
- **Cement Production**: Cement and concrete
- **Electronics**: Semiconductor manufacturing, component production

### Advantages

- Simpler and less expensive than job order costing
- Suitable for mass production environments
- Provides average cost per unit
- Easier to implement and maintain
- Requires less detailed tracking

### Limitations

- Provides only average costs, not specific job costs
- May mask inefficiencies in specific batches
- Less useful for pricing custom products
- Assumes all units are identical
- Equivalent units calculations can be complex

## Activity-Based Costing (ABC)

### Overview

Activity-Based Costing is a refined costing method that assigns overhead costs to products based on the activities they consume rather than using volume-based allocation. ABC recognizes that different products consume resources in different proportions.

### Fundamental Concepts

**Activity**: A task or unit of work with a specific purpose (e.g., machine setup, quality inspection, order processing)

**Cost Driver**: A factor that causes or "drives" the cost of an activity (e.g., number of setups, number of inspections, number of orders)

**Activity Cost Pool**: A group of overhead costs associated with a specific activity

**Activity Rate**: Cost per unit of the cost driver

### ABC Implementation Process

#### Step 1: Identify Activities
Analyze operations to identify significant activities that consume resources:
- Unit-level activities (performed for each unit)
- Batch-level activities (performed for each batch)
- Product-level activities (performed to support a product line)
- Facility-level activities (performed to support the organization)

#### Step 2: Assign Costs to Activity Cost Pools
Trace overhead costs to the activities that generate them:
- Direct tracing when possible
- Driver tracing using resource drivers
- Allocation when necessary

#### Step 3: Identify Cost Drivers
Select appropriate cost drivers for each activity:
- Should have a strong cause-and-effect relationship
- Should be measurable
- Data should be readily available

#### Step 4: Calculate Activity Rates
```
Activity Rate = Total Cost in Activity Cost Pool / Total Cost Driver Activity
```

#### Step 5: Assign Costs to Cost Objects
```
Cost Assigned = Activity Rate × Cost Driver Usage by Cost Object
```

### Cost Hierarchy

**Unit-Level Activities**:
- Performed for each unit produced
- Costs vary with production volume
- Examples: Direct materials, direct labor, machine operations
- Traditional costing handles these well

**Batch-Level Activities**:
- Performed for each batch regardless of batch size
- Costs vary with number of batches, not units
- Examples: Machine setups, purchase orders, inspections
- Often misallocated in traditional systems

**Product-Level Activities**:
- Performed to support a specific product line
- Costs vary with number of products, not volume
- Examples: Product design, engineering changes, product marketing
- Typically allocated arbitrarily in traditional systems

**Facility-Level Activities**:
- Performed to support the organization overall
- Do not vary with products or volume
- Examples: Building maintenance, plant management, property taxes
- Cannot be meaningfully traced to products

### ABC vs. Traditional Costing

| Aspect | Traditional Costing | Activity-Based Costing |
|--------|-------------------|------------------------|
| **Overhead Allocation** | Volume-based (labor hours, machine hours) | Activity-based (multiple drivers) |
| **Cost Pools** | Few, often department-based | Many, activity-based |
| **Accuracy** | Less accurate for diverse products | More accurate cost assignment |
| **Complexity** | Simpler | More complex |
| **Cost** | Lower implementation cost | Higher implementation cost |
| **Information** | Limited insight into cost drivers | Detailed activity information |
| **Best For** | Homogeneous products, low overhead | Diverse products, high overhead |

### Activity-Based Management (ABM)

ABM uses ABC information for operational and strategic improvements:

**Operational ABM**:
- Increase efficiency of activities
- Reduce costs of activities
- Eliminate non-value-added activities

**Strategic ABM**:
- Product pricing decisions
- Product mix decisions
- Customer profitability analysis
- Process redesign
- Outsourcing decisions

### Industries and Applications

- **Manufacturing**: Complex products with diverse overhead consumption
- **Healthcare**: Hospital services, patient treatments
- **Financial Services**: Banking products, insurance policies
- **Telecommunications**: Service offerings
- **Logistics**: Distribution and warehousing
- **Government**: Public services

### Advantages

- More accurate product costs, especially for diverse products
- Identifies cost drivers and non-value-added activities
- Supports better pricing and product mix decisions
- Enhances cost management and reduction efforts
- Provides insights for process improvement
- Improves customer profitability analysis

### Limitations

- More expensive to implement and maintain
- Requires significant data collection and analysis
- May require specialized software
- Can be complex to explain and understand
- Requires ongoing maintenance and updates
- Some costs still require arbitrary allocation

## Standard Costing

### Overview

Standard costing establishes predetermined cost benchmarks for materials, labor, and overhead, then compares actual costs to these standards to identify variances and support cost control.

### Types of Standards

**Ideal Standards**:
- Assume perfect efficiency and optimal conditions
- Rarely achieved in practice
- Can demotivate employees
- Useful for identifying maximum potential

**Attainable Standards**:
- Allow for normal inefficiencies and realistic conditions
- Challenging but achievable with reasonable effort
- Most commonly used
- Balance motivation and realism

**Current Standards**:
- Based on current actual performance
- Reflect existing efficiency levels
- Easy to achieve
- Provide little motivation for improvement

### Setting Standards

**Direct Materials Standards**:
- **Price Standard**: Expected cost per unit of material
  - Based on supplier quotes, contracts, market prices
  - Adjusted for purchase discounts, freight, handling
- **Quantity Standard**: Expected amount of material per unit of output
  - Based on engineering specifications, bills of materials
  - Includes allowance for normal waste and spoilage

**Direct Labor Standards**:
- **Rate Standard**: Expected wage rate per hour
  - Based on union contracts, wage surveys, skill requirements
  - Includes fringe benefits
- **Efficiency Standard**: Expected labor hours per unit of output
  - Based on time and motion studies, historical data
  - Includes allowance for breaks, setup time, normal delays

**Manufacturing Overhead Standards**:
- **Variable Overhead Rate**: Expected variable overhead per unit of activity
- **Fixed Overhead Rate**: Budgeted fixed overhead divided by normal capacity
- Based on flexible budgets and expected activity levels

### Variance Analysis

Standard costing enables detailed variance analysis (covered in separate reference document).

### Applications

- Manufacturing environments with repetitive processes
- Budgeting and planning
- Performance evaluation
- Cost control systems
- Pricing decisions
- Inventory valuation

### Advantages

- Simplifies bookkeeping and inventory valuation
- Facilitates budgeting and planning
- Enables variance analysis and cost control
- Supports performance evaluation
- Provides benchmarks for continuous improvement
- Reduces clerical costs

### Limitations

- Standards can become outdated quickly
- May not reflect current market conditions
- Can create behavioral issues if used punitively
- Requires regular review and updating
- May not be suitable for rapidly changing environments
- Variance analysis can be time-consuming

## Target Costing

### Overview

Target costing is a market-driven approach that determines the maximum allowable cost for a product based on competitive market prices and desired profit margins.

### Process

1. **Determine Target Price**: Based on market research and competitive analysis
2. **Determine Target Profit**: Based on company's required return on investment
3. **Calculate Target Cost**: Target Price - Target Profit = Target Cost
4. **Estimate Current Cost**: Based on current design and processes
5. **Calculate Cost Gap**: Current Cost - Target Cost = Cost Gap
6. **Close the Gap**: Through value engineering and cost reduction initiatives

### Value Engineering

Systematic approach to reducing costs while maintaining or improving functionality:
- Simplify product design
- Reduce number of components
- Use less expensive materials
- Improve manufacturing processes
- Eliminate non-value-added features
- Standardize components across products

### Applications

- New product development
- Highly competitive markets
- Price-sensitive customers
- Industries with rapid technological change
- Consumer electronics, automobiles, appliances

### Advantages

- Market-oriented approach
- Encourages cost consciousness early in design
- Promotes cross-functional collaboration
- Supports competitive pricing
- Drives innovation and efficiency

### Limitations

- May compromise product quality or features
- Can be difficult to achieve target costs
- Requires strong supplier relationships
- May create pressure on design and engineering teams
- Not suitable for all products or markets

## Lean Accounting

### Overview

Lean accounting aligns accounting practices with lean manufacturing principles, focusing on value streams, eliminating waste in accounting processes, and providing simple, relevant information.

### Key Principles

- **Value Stream Focus**: Organize accounting around value streams rather than departments
- **Simplification**: Eliminate complex, wasteful accounting transactions
- **Visual Management**: Use visual performance measures and dashboards
- **Continuous Improvement**: Apply kaizen to accounting processes
- **Decision Support**: Provide relevant information for lean decision-making

### Value Stream Costing

- Accumulate costs by value stream rather than by product
- Minimize cost allocations
- Report actual costs rather than standard costs
- Simplify inventory valuation
- Focus on value stream profitability

### Performance Measures

- **Operational Measures**: Cycle time, first-pass yield, on-time delivery
- **Financial Measures**: Value stream revenue, costs, and profitability
- **Capacity Measures**: Available capacity, productive capacity, non-productive capacity

### Advantages

- Aligns with lean operations
- Reduces accounting complexity and waste
- Provides timely, relevant information
- Supports lean decision-making
- Encourages continuous improvement

### Limitations

- Requires organizational commitment to lean principles
- May not meet external reporting requirements
- Can be challenging to implement
- Requires cultural change
- May not be suitable for all organizations

## Throughput Accounting

### Overview

Throughput accounting, based on Theory of Constraints, focuses on maximizing throughput (sales minus totally variable costs) while managing operating expenses and investment.

### Key Metrics

**Throughput (T)**: Sales Revenue - Totally Variable Costs (typically only direct materials)

**Operating Expenses (OE)**: All other costs to operate the system

**Investment (I)**: Money tied up in the system (inventory, equipment)

**Performance Measures**:
- Net Profit = T - OE
- Return on Investment = (T - OE) / I
- Throughput per Constraint Unit

### Decision-Making

- Maximize throughput per unit of the constraint
- Minimize operating expenses
- Minimize investment
- Focus on bottleneck management

### Advantages

- Simple and easy to understand
- Focuses on system constraints
- Supports Theory of Constraints methodology
- Avoids arbitrary cost allocations
- Encourages system thinking

### Limitations

- Oversimplifies cost behavior
- May not provide sufficient cost detail
- Not widely accepted for external reporting
- Requires understanding of Theory of Constraints
- May not suit all organizational contexts

## Selecting the Appropriate Costing Method

### Decision Factors

1. **Nature of Production**:
   - Unique products → Job Order Costing
   - Homogeneous products → Process Costing
   - Diverse products with complex overhead → Activity-Based Costing

2. **Cost Structure**:
   - High overhead, diverse products → ABC
   - Low overhead, simple operations → Traditional methods

3. **Information Needs**:
   - Detailed product costs → Job Order or ABC
   - Average costs sufficient → Process Costing
   - Cost control focus → Standard Costing

4. **Competitive Environment**:
   - Price-driven markets → Target Costing
   - Lean operations → Lean Accounting

5. **Resources Available**:
   - Limited resources → Simpler methods
   - Sophisticated IT systems → ABC or advanced methods

6. **Industry Norms**:
   - Consider standard practices in your industry

### Hybrid Approaches

Many organizations use combinations of methods:
- Job order costing with ABC for overhead allocation
- Process costing with standard costing for control
- Target costing during design, then standard costing for production

## Conclusion

Selecting and implementing appropriate costing methods is crucial for accurate cost information and effective decision-making. Each method has strengths and limitations, and the choice should align with the organization's operations, cost structure, competitive environment, and information needs. Many organizations benefit from using multiple methods or hybrid approaches tailored to their specific circumstances.
