---
name: retail-strategy-operations
description: The Retail Strategy & Operations skill provides comprehensive capabilities for analyzing, planning, and optimizing retail business operations across physical stores, omnichannel environments, and supporting functions.
---

---
name: Retail Strategy & Operations
description: Expert skill for optimizing brick-and-mortar and omnichannel retail operations, including store management, merchandising strategy, inventory optimization, customer experience enhancement, and retail analytics.
---

# Retail Strategy & Operations

## 1. Skill Description and Purpose

The Retail Strategy & Operations skill provides comprehensive capabilities for analyzing, planning, and optimizing retail business operations across physical stores, omnichannel environments, and supporting functions. This skill combines strategic retail planning with operational excellence to maximize profitability, customer satisfaction, and competitive positioning.

### Core Capabilities

**Store Operations Management**: This skill optimizes daily store operations including staffing models, task management, opening/closing procedures, cash handling, and operational compliance. It designs standard operating procedures (SOPs), creates operational checklists, and establishes performance management frameworks that drive consistent execution across single or multi-location retail environments.

**Merchandising Strategy and Execution**: Develops comprehensive merchandising plans encompassing assortment planning, space allocation, visual merchandising standards, and promotional strategies. The skill applies category management principles, analyzes product performance data, and creates planograms that optimize product placement for maximum sales and margin contribution.

**Inventory Management and Optimization**: Implements inventory control methodologies including demand forecasting, safety stock calculations, reorder point optimization, and inventory turnover improvement strategies. The skill balances stockout prevention against overstock costs, designs markdown optimization strategies, and structures inventory allocation across locations.

**Customer Experience Excellence**: Analyzes and enhances the customer journey from awareness through post-purchase engagement. This includes mystery shopping program design, customer feedback analysis, service recovery protocols, and loyalty program optimization to drive customer lifetime value and advocacy.

**Omnichannel Integration**: Bridges online and offline retail channels through unified inventory visibility, buy-online-pickup-in-store (BOPIS) optimization, ship-from-store strategies, and consistent cross-channel customer experiences. The skill addresses the operational complexities of serving customers seamlessly across touchpoints.

### Strategic Value

This skill delivers value when retailers need to improve store profitability, optimize inventory investment, enhance customer experience, implement omnichannel capabilities, or benchmark performance against industry standards. It translates retail data into actionable insights and executable strategies.

### When to Deploy This Skill

- Analyzing store performance and identifying improvement opportunities
- Designing merchandising strategies and planogram layouts
- Optimizing inventory levels and reducing stockouts/overstock
- Developing staff scheduling and workforce management plans
- Creating customer experience improvement initiatives
- Implementing loss prevention and shrinkage control programs
- Establishing retail KPI dashboards and performance management systems
- Planning seasonal promotions and markdown strategies

---

## 2. Required Inputs/Parameters

### Primary Data Requirements

| Parameter | Format | Description | Required |
|-----------|--------|-------------|----------|
| `sales_data` | Transaction-level CSV/Database | Point-of-sale records with SKU, quantity, price, timestamp, store ID, tender type | Yes |
| `inventory_data` | CSV/Database | Current on-hand quantities, receiving records, transfer data by location and SKU | Yes |
| `store_profile` | Structured document | Store characteristics: square footage, format, location demographics, operating hours | Yes |
| `product_master` | Database/CSV | Product catalog with attributes: category, brand, cost, retail, dimensions, velocity class | Yes |
| `labor_data` | Scheduling system export | Employee schedules, hours worked, labor costs, productivity metrics | Conditional |
| `customer_data` | CRM/Loyalty database | Customer profiles, purchase history, loyalty status, contact information | Conditional |

### Secondary Parameters

| Parameter | Format | Default | Description |
|-----------|--------|---------|-------------|
| `analysis_period` | Date range | Last 52 weeks | Timeframe for performance analysis |
| `store_count` | Integer | 1 | Number of stores in scope |
| `retail_format` | Enum | General | Department, specialty, convenience, grocery, etc. |
| `seasonality_profile` | JSON | Industry standard | Seasonal demand patterns by category |
| `target_metrics` | JSON object | Benchmark | Target KPIs for performance evaluation |
| `competitive_context` | Text/Document | None | Competitive landscape and positioning |
| `expansion_plans` | Document | None | New store pipeline and growth strategy |

### Contextual Information

- Retail brand positioning and target customer segments
- Current challenges and strategic priorities
- Technology infrastructure (POS, inventory management, CRM systems)
- Organizational structure and decision-making processes
- Market conditions and competitive pressures

---

## 3. Expected Outputs/Deliverables

### Performance Analytics

**Store Performance Analysis**
- Sales per square foot analysis with benchmarking
- Conversion rate calculation and improvement opportunities
- Average basket size and units per transaction trends
- Traffic patterns and peak hour identification
- Labor productivity metrics (sales per labor hour, transactions per FTE)
- Four-wall profitability analysis by location

**Category and Product Performance**
- Category contribution analysis with margin and velocity metrics
- SKU rationalization recommendations based on performance data
- Assortment productivity assessment (sales/SKU, turns by category)
- Price elasticity insights and promotional effectiveness
- Vendor performance scorecards

### Strategic Plans

**Merchandising Strategy Document**
- Assortment architecture by category and store cluster
- Space allocation recommendations with financial justification
- Planogram designs optimized for sales and margin
- Visual merchandising guidelines and fixture standards
- Promotional calendar with expected lift factors

**Inventory Optimization Plan**
- Demand forecast models by SKU and location
- Safety stock and reorder point calculations
- Inventory allocation strategies for new products
- Markdown optimization schedule and pricing recommendations
- Shrinkage reduction action plan

### Operational Frameworks

**Store Operations Manual**
- Standard operating procedures for daily/weekly/monthly tasks
- Opening and closing checklists
- Cash handling and reconciliation procedures
- Customer service standards and service recovery protocols
- Loss prevention procedures and compliance requirements

**Workforce Management Plan**
- Staffing model based on traffic patterns and service requirements
- Schedule templates optimized for coverage and labor cost
- Role definitions and task allocation guidelines
- Training curriculum and onboarding programs
- Performance management framework with KPIs

### Customer Experience Design

**Customer Journey Map**
- Touchpoint analysis from discovery through post-purchase
- Pain point identification and resolution strategies
- Service standards by touchpoint
- Mystery shopping program design and scorecard
- Loyalty program optimization recommendations

### KPI Dashboards

Comprehensive metrics tracking including:
- Sales metrics: comp sales, sales/sqft, ATV, UPT, conversion
- Inventory metrics: turns, weeks of supply, stockout rate, GMROI
- Labor metrics: sales per labor hour, payroll as % of sales
- Customer metrics: NPS, customer retention, loyalty penetration
- Shrinkage: inventory accuracy, known loss, unknown loss

---

## 4. Example Use Cases

### Use Case 1: Multi-Store Performance Optimization

**Scenario**: A specialty apparel retailer with 45 stores experiences significant performance variation, with top quartile stores achieving 2.3x the sales per square foot of bottom quartile stores.

**Skill Application**:
1. Ingest sales, inventory, labor, and customer data across all locations
2. Cluster stores by performance profile and demographic characteristics
3. Identify key differentiators between high and low performers:
   - Conversion rate variance (18% vs 11%)
   - Staffing coverage during peak hours
   - Inventory depth in key categories
   - Visual merchandising execution scores
4. Develop improvement playbooks for each store cluster
5. Create performance monitoring dashboard with weekly scorecards
6. Project $4.2M annual sales lift from bottom quartile improvement

### Use Case 2: Inventory Optimization Initiative

**Scenario**: A home goods retailer carries $28M in inventory across 12 stores with inventory turns of 2.8x annually. Management targets 3.5x turns while maintaining 96% in-stock rate.

**Skill Application**:
1. Analyze SKU-level velocity and profitability across locations
2. Identify slow-moving inventory (22% of SKUs generating 3% of sales)
3. Calculate optimal stock levels by SKU and location using demand variability
4. Design markdown strategy for aging inventory ($2.1M at risk)
5. Restructure replenishment parameters:
   - Reduce safety stock on consistent sellers
   - Implement more frequent ordering for high-velocity items
   - Rationalize 1,200 SKUs with insufficient contribution
6. Achieve inventory reduction of $4.8M while improving in-stock to 97%

### Use Case 3: Omnichannel Implementation

**Scenario**: A regional sporting goods retailer launches BOPIS (buy-online-pickup-in-store) and seeks to optimize store operations for fulfillment while maintaining customer experience.

**Skill Application**:
1. Analyze online order patterns and geographic distribution
2. Design store fulfillment workflows:
   - Pick path optimization within stores
   - Staging area requirements and design
   - Customer notification and pickup procedures
3. Calculate labor impact and staffing adjustments
4. Create inventory allocation rules for online-eligible stock
5. Develop KPIs: fulfillment time, BOPIS conversion, pickup experience scores
6. Design ship-from-store protocols for inventory optimization
7. Project 15% sales lift from omnichannel customers with higher lifetime value

### Use Case 4: Seasonal Planning and Promotional Strategy

**Scenario**: A gift retailer generates 45% of annual sales during Q4 holiday season and requires optimized seasonal planning for merchandising, inventory, and staffing.

**Skill Application**:
1. Analyze historical seasonal performance patterns by category
2. Develop demand forecast incorporating trend and promotional factors
3. Create seasonal assortment plan with new item introduction timing
4. Design promotional calendar with event themes and discount structures
5. Calculate inventory requirements and receipt flow by week
6. Build staffing plan with seasonal hiring timeline and training schedule
7. Create visual merchandising timeline with floor set schedules
8. Establish contingency plans for above/below plan scenarios

---

## 5. Prerequisites or Dependencies

### Data Infrastructure Requirements

- **Point-of-Sale System**: Transaction-level sales data with SKU detail, minimum 52 weeks history
- **Inventory Management System**: Real-time or daily inventory position by location and SKU
- **Traffic Counting**: Store traffic data for conversion rate calculation (recommended)
- **Labor Management System**: Scheduling and time tracking data
- **Customer Data Platform**: Loyalty/CRM data for customer analytics (recommended)

### Technical Dependencies

- Statistical analysis for demand forecasting and performance analytics
- Optimization algorithms for inventory and assortment planning
- Visualization capabilities for planograms and dashboards
- Report generation for operational documents and strategic plans
- Geospatial analysis for store clustering and market analysis

### Domain Knowledge Prerequisites

- Understanding of retail financial model (gross margin, contribution, four-wall profit)
- Familiarity with retail calendar and seasonal patterns
- Knowledge of merchandising principles and category management
- Understanding of retail technology ecosystem (POS, OMS, WMS)
- Awareness of industry benchmarks by retail format

### Organizational Requirements

- Access to cross-functional stakeholders (merchandising, operations, finance)
- Clarity on strategic priorities and growth objectives
- Understanding of competitive positioning and brand standards
- Decision rights for operational and assortment changes

### Tool Integrations

| Tool Category | Common Platforms | Integration Method |
|---------------|------------------|-------------------|
| POS Systems | Oracle Retail, NCR, Shopify POS | API, database, file export |
| Inventory Management | Manhattan, Blue Yonder, NetSuite | API, EDI, database |
| Workforce Management | Kronos, Legion, Deputy | API, file integration |
| CRM/Loyalty | Salesforce, Oracle, custom | API, database query |
| Traffic Analytics | RetailNext, ShopperTrak | API, dashboard export |
| Planogramming | JDA, Nielsen, Blue Yonder | File import/export |

### Compliance Considerations

- PCI-DSS compliance for payment data handling
- Privacy regulations (GDPR, CCPA) for customer data
- Labor law compliance for scheduling and workforce planning
- Product safety and regulatory requirements by category
- Accessibility requirements for store design recommendations
