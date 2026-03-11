# Carbon Accounting and Life Cycle Assessment

## GHG Protocol Implementation

### Step 1: Set Organizational Boundaries
- **Equity share approach**: Account for GHG based on ownership percentage
- **Control approach**: Account for 100% of operations under financial or operational control
- Choose one approach and apply consistently

### Step 2: Set Operational Boundaries
Identify emission sources within each scope:

**Scope 1 Sources**
- Stationary combustion (boilers, furnaces, generators)
- Mobile combustion (company vehicles, fleet)
- Process emissions (chemical reactions, manufacturing)
- Fugitive emissions (refrigerants, gas leaks)

**Scope 2 Sources**
- Purchased electricity (location-based and market-based methods)
- Purchased steam, heating, cooling

**Scope 3 Categories** (15 categories per GHG Protocol)
1. Purchased goods and services
2. Capital goods
3. Fuel and energy-related activities (not Scope 1/2)
4. Upstream transportation and distribution
5. Waste generated in operations
6. Business travel
7. Employee commuting
8. Upstream leased assets
9. Downstream transportation and distribution
10. Processing of sold products
11. Use of sold products
12. End-of-life treatment of sold products
13. Downstream leased assets
14. Franchises
15. Investments

### Step 3: Calculate Emissions
**Formula**: Activity Data × Emission Factor = GHG Emissions (tCO2e)

**Emission Factor Sources**
- EPA Emission Factors Hub
- IPCC Guidelines
- ecoinvent database
- DEFRA conversion factors (UK)
- Industry-specific databases

---

## Life Cycle Assessment (LCA)

### LCA Phases (ISO 14040)

1. **Goal and Scope Definition**
   - Define functional unit (what is being compared)
   - Set system boundaries (cradle-to-gate, cradle-to-grave, cradle-to-cradle)
   - Identify impact categories

2. **Life Cycle Inventory (LCI)**
   - Quantify all inputs and outputs across lifecycle
   - Material extraction, manufacturing, distribution, use, disposal
   - Energy inputs, water use, waste outputs, emissions

3. **Life Cycle Impact Assessment (LCIA)**
   - Translate inventory data to environmental impacts
   - Impact categories: climate change, acidification, eutrophication, ozone depletion
   - Characterization factors convert emissions to impact equivalents

4. **Interpretation**
   - Identify significant findings
   - Sensitivity and uncertainty analysis
   - Recommendations for improvement

### LCA Software Tools
- **openLCA**: Free, open-source LCA software
- **SimaPro**: Industry-standard commercial tool
- **GaBi**: Engineering-focused LCA platform
- **Brightway2**: Python-based open-source framework

---

## Emission Reduction Strategies

### Reduction Hierarchy
1. **Avoid**: Eliminate emission-generating activities
2. **Reduce**: Improve efficiency to lower emissions
3. **Substitute**: Switch to lower-carbon alternatives
4. **Compensate**: Offset remaining emissions (last resort)

### Common Reduction Measures

| Category | Measure | Typical Reduction |
|---|---|---|
| Energy | LED lighting upgrade | 50-70% lighting emissions |
| Energy | HVAC optimization | 15-30% building emissions |
| Energy | Renewable energy purchase | Up to 100% Scope 2 |
| Transport | Fleet electrification | 40-60% fleet emissions |
| Transport | Route optimization | 5-15% transport emissions |
| Supply chain | Supplier engagement | 10-30% Scope 3 |
| Operations | Waste reduction/recycling | 20-40% waste emissions |
