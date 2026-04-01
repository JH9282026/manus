---
name: supply-chain-management
description: "The Supply Chain Management skill enables AI agents to orchestrate the complete flow of goods and information from suppliers through manufacturing and distribution to end customers."
---

# Supply Chain Management

## Overview

This skill provides comprehensive guidance and best practices for this domain.

## 1. Skill Description and Purpose

The Supply Chain Management skill enables AI agents to orchestrate the complete flow of goods and information from suppliers through manufacturing and distribution to end customers. This skill encompasses strategic sourcing, supplier management, demand planning, inventory optimization, logistics coordination, and supply chain risk mitigation.

**Why This Skill Is Valuable:**
- Reduces procurement costs through strategic sourcing and supplier negotiation
- Optimizes inventory levels reducing carrying costs while maintaining service levels
- Improves forecast accuracy reducing stockouts and excess inventory
- Enhances supply chain visibility enabling proactive issue resolution
- Mitigates supply risks through supplier diversification and contingency planning
- Accelerates order-to-delivery cycles improving customer satisfaction
- Enables data-driven supply chain decisions across the network

**When to Use This Skill:**
- Executing procurement activities including RFx processes and contract management
- Analyzing and selecting suppliers based on cost, quality, delivery, and risk
- Planning and optimizing inventory across the supply network
- Forecasting demand using statistical and machine learning methods
- Coordinating logistics including transportation and warehousing
- Managing supplier relationships and performance
- Identifying and mitigating supply chain risks
- Tracking supply chain KPIs and investigating variances

**Core Methodologies Applied:**
- Strategic Sourcing using category management and total cost of ownership (TCO)
- Inventory optimization using EOQ, safety stock models, and ABC-XYZ analysis
- Demand forecasting using time series analysis, causal models, and ML algorithms
- Supplier Relationship Management (SRM) with segmentation and development programs
- Supply chain network optimization using mathematical programming
- Risk management using FMEA and scenario planning

## 2. Required Inputs/Parameters

### Procurement Inputs
| Parameter | Format | Required | Description |
|-----------|--------|----------|-------------|
| spend_data | File | Yes | Historical purchase data by category, supplier, and item |
| supplier_master | File | Yes | Supplier database with contacts, certifications, and locations |
| contract_repository | File | Yes | Active contracts with terms, pricing, and expiration dates |
| category_taxonomy | Object | Yes | Procurement category hierarchy |
| commodity_indices | API | No | Market price indices for key commodities |
| compliance_requirements | Array | Yes | Regulatory and policy requirements (sustainability, diversity) |

### Inventory Inputs
| Parameter | Format | Required | Description |
|-----------|--------|----------|-------------|
| item_master | File | Yes | SKU database with attributes and classifications |
| inventory_positions | File | Yes | Current stock levels by location |
| demand_history | File | Yes | Historical sales/consumption by item and location |
| lead_times | Object | Yes | Supplier and transportation lead times |
| holding_costs | Object | Yes | Inventory carrying cost components |
| service_level_targets | Object | Yes | Fill rate or availability targets by item class |
| storage_constraints | Object | No | Warehouse capacity and handling limitations |

### Demand Planning Inputs
| Parameter | Format | Required | Description |
|-----------|--------|----------|-------------|
| sales_history | File | Yes | Historical shipments or point-of-sale data |
| promotional_calendar | File | No | Planned promotions and marketing events |
| new_product_introductions | Array | No | Upcoming product launches with expected demand |
| seasonality_patterns | Object | No | Known seasonal factors |
| external_factors | File | No | Economic indicators, weather, or market data affecting demand |
| customer_forecasts | File | No | Forecasts provided by key customers |

### Logistics Inputs
| Parameter | Format | Required | Description |
|-----------|--------|----------|-------------|
| network_structure | Object | Yes | Locations (plants, DCs, customers) with capabilities |
| transportation_lanes | File | Yes | Routes with carriers, modes, rates, and transit times |
| shipment_history | File | Yes | Historical shipment data with costs and performance |
| carrier_contracts | File | Yes | Negotiated rates and service commitments |
| customer_delivery_requirements | Object | Yes | Delivery windows, access restrictions, and special requirements |

### Supplier Management Inputs
| Parameter | Format | Required | Description |
|-----------|--------|----------|-------------|
| supplier_scorecard_data | File | Yes | Performance metrics by supplier (quality, delivery, cost, responsiveness) |
| supplier_financial_data | File | No | Financial health indicators for risk assessment |
| supplier_audit_results | File | No | Quality and compliance audit findings |
| supplier_development_plans | File | No | Ongoing improvement initiatives |

## 3. Expected Outputs/Deliverables

### Procurement Outputs
- **Spend Analysis Report**: Spend breakdown by category, supplier, and business unit with consolidation opportunities
- **Sourcing Strategy Documents**: Category strategies with market analysis, supplier landscape, and recommended approach
- **RFx Documents**: Request for Proposal/Quote/Information documents with specifications and evaluation criteria
- **Supplier Evaluation Matrix**: Weighted scoring of supplier proposals across price, quality, capability, and risk factors
- **Contract Recommendations**: Negotiation positions, recommended terms, and contract templates
- **Savings Tracking Report**: Realized and projected procurement savings against targets

### Inventory Outputs
- **Inventory Optimization Model**: Recommended reorder points, order quantities, and safety stocks by item-location
- **ABC-XYZ Classification**: Items segmented by value and demand variability for differentiated management
- **Inventory Health Report**: Analysis of slow-moving, excess, and obsolete inventory with disposition recommendations
- **Stock Policy Recommendations**: Stocking strategies (make-to-stock, make-to-order, consignment) by segment
- **Service Level Analysis**: Fill rates and stockout analysis with root causes and improvement recommendations

### Demand Planning Outputs
- **Demand Forecasts**: Statistical forecasts by item, location, and period with confidence intervals
- **Forecast Accuracy Report**: MAPE, bias, and other accuracy metrics with trend analysis
- **Demand Sensing Alerts**: Early indicators of demand shifts requiring attention
- **Consensus Forecast**: Integrated forecast incorporating statistical baseline and market intelligence
- **Forecast Value-Add Analysis**: Accuracy comparison of statistical forecast versus adjusted forecast

### Logistics Outputs
- **Transportation Optimization Plan**: Optimized routing, mode selection, and carrier assignment minimizing cost within service constraints
- **Shipment Visibility Dashboard**: Real-time tracking of in-transit shipments with exception alerts
- **Carrier Scorecard**: Performance metrics by carrier supporting contract negotiations
- **Network Optimization Analysis**: Recommendations for facility locations, inventory positioning, or flow path changes
- **Freight Audit Results**: Invoice validation findings with discrepancy resolution and recovery

### Supplier Management Outputs
- **Supplier Performance Dashboard**: KPI visualization by supplier with trend analysis and benchmarking
- **Risk Assessment Report**: Supplier risk ratings based on financial, operational, and geopolitical factors
- **Supplier Segmentation Matrix**: Strategic classification (strategic, leverage, bottleneck, routine) guiding relationship approach
- **Supplier Development Roadmap**: Improvement plans for critical suppliers with milestones and success metrics
- **Supply Base Rationalization Recommendations**: Consolidation opportunities balancing efficiency and risk

### Risk Management Outputs
- **Supply Chain Risk Map**: Identified risks with probability, impact, and risk scores
- **Contingency Plans**: Documented response procedures for high-priority risk scenarios
- **Disruption Monitoring Alerts**: Early warning indicators from news, financial, and operational monitoring
- **Business Continuity Assessment**: Impact analysis for potential disruption scenarios with mitigation strategies

**Quality Standards:**
- Demand forecasts must include accuracy metrics and be validated against holdout samples
- Inventory recommendations must balance service level targets against holding cost constraints
- Supplier evaluations must use consistent, documented criteria with audit trail
- Transportation optimizations must respect all delivery constraints and capacity limits
- Risk assessments must be updated quarterly or upon significant events

## 4. Example Use Cases

### Use Case 1: Strategic Sourcing for Packaging Materials
A CPG company initiates strategic sourcing for $50M annual packaging spend. The agent analyzes spend patterns, maps the supplier market, develops category strategy, creates RFP documents, evaluates supplier responses using weighted criteria, conducts should-cost modeling, recommends negotiation strategies, and manages the contract execution process, achieving 12% cost reduction through specification standardization and volume consolidation.

### Use Case 2: Inventory Optimization for Distribution Network
A retailer struggles with simultaneous stockouts and excess inventory. The agent analyzes demand patterns by SKU-location, segments products using ABC-XYZ analysis, calculates optimal safety stock levels considering demand variability and lead time variability, recommends differentiated replenishment policies, implements inventory analytics dashboards, and reduces inventory investment by 25% while improving fill rates from 92% to 98%.

### Use Case 3: Demand Forecasting System Implementation
A manufacturer implements statistical demand forecasting to replace judgmental methods. The agent analyzes historical demand patterns, identifies appropriate forecasting models by product segment, develops a forecasting hierarchy, implements forecast accuracy tracking, designs consensus forecasting process integrating market intelligence, and improves forecast accuracy from 65% to 85% at the monthly SKU level.

### Use Case 4: Supplier Risk Monitoring Program
A company develops proactive supply risk management following a disruptive supplier bankruptcy. The agent establishes financial health monitoring for critical suppliers, implements news and regulatory monitoring, develops risk scoring methodology, creates tiered response protocols based on risk levels, identifies dual-sourcing opportunities for single-source dependencies, and builds contingency inventory strategies for high-risk materials.

### Use Case 5: Logistics Network Optimization
A company evaluates its distribution network following acquisition. The agent maps current network flows, analyzes transportation costs and service levels, models alternative network configurations using facility location optimization, evaluates scenarios including consolidation and new DC locations, quantifies cost and service tradeoffs, and recommends network redesign delivering 18% logistics cost reduction.

## 5. Prerequisites or Dependencies

### System Access Requirements
- **ERP System**: Read/write access to SAP, Oracle, or equivalent for procurement and inventory transactions
- **Supply Chain Planning System**: Access to SAP IBP, Kinaxis, o9, or equivalent for demand and supply planning
- **Transportation Management System (TMS)**: Access to TMS for shipment optimization and tracking
- **Warehouse Management System (WMS)**: Access to inventory positions and warehouse operations
- **Supplier Portal**: Platform for supplier communication and collaboration
- **Spend Analytics Platform**: Access to spend classification and analysis tools

### Data Requirements
- Historical transaction data for spend analysis and demand forecasting
- Master data for items, suppliers, and locations
- Supplier performance data (quality, delivery, responsiveness metrics)
- Cost data including purchase prices, transportation rates, and inventory carrying costs
- Network data including facility locations, capacities, and transportation lanes
- External data feeds for market prices, risk indicators, and demand drivers

### Methodology Knowledge
- Strategic sourcing and category management
- Inventory management principles (EOQ, safety stock, reorder point)
- Demand forecasting techniques (time series, regression, machine learning)
- Transportation optimization (routing, mode selection, load planning)
- Supplier evaluation and development frameworks
- Supply chain risk management and business continuity

### Integration Dependencies
- Financial systems for cost tracking and payment processing
- Quality systems for supplier performance data
- External market data providers for commodity indices
- Risk monitoring services for supplier financial health
- EDI/API connections for supplier transactions
- Carrier integration for rate shopping and shipment tracking

## References

- [01 Fundamentals Of Supply Chain Management](references/01-fundamentals-of-supply-chain-management.md)
- [02 Supply Chain Optimization Strategies](references/02-supply-chain-optimization-strategies.md)
- [03 Procurement And Supplier Management](references/03-procurement-and-supplier-management.md)
- [04 Technology And Analytics](references/04-technology-and-analytics.md)
