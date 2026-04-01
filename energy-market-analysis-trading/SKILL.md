---
name: "energy-market-analysis-trading"
description: "Analyze energy markets and develop trading strategies for power, natural gas, oil, and renewable energy commodities. Use for: power price forecasting, natural gas hedging strategy, ISO/RTO market analysis, renewable energy credit portfolio management, energy trading desk optimization, supply-demand fundamentals, risk management, and environmental market analysis."
---

# Energy Market Analysis & Trading

Analyze energy market fundamentals, develop trading strategies, forecast commodity prices, and manage risk across power, natural gas, oil, and environmental markets.

## Overview

Provide frameworks for energy market analysis covering supply-demand fundamentals, price forecasting, trading strategy development, hedging, and risk management. Cover wholesale electricity markets, natural gas, crude oil, and renewable energy credits.

## Energy Commodity Overview

| Market | Key Drivers | Trading Venues | Contract Types |
|---|---|---|---|
| Power (Electricity) | Load, generation mix, weather | ISO/RTOs, bilateral | Day-ahead, real-time, futures |
| Natural Gas | Storage, production, weather | NYMEX, ICE | Henry Hub futures, basis swaps |
| Crude Oil | OPEC, geopolitics, demand | NYMEX, ICE | WTI, Brent futures |
| Refined Products | Refinery runs, demand, spreads | NYMEX | RBOB gasoline, heating oil |
| RECs/Carbon | Policy, compliance, voluntary | Various registries | RECs, carbon offsets, EUAs |

## Price Forecasting Framework

### Fundamental Analysis Inputs
- **Supply**: Generation capacity, production rates, imports
- **Demand**: Load forecasts, industrial activity, economic indicators
- **Weather**: Temperature forecasts, heating/cooling degree days
- **Storage/Inventory**: Gas storage levels, oil inventories, SPR
- **Transmission/Transport**: Pipeline capacity, congestion, constraints

### Forecasting Methods

| Method | Horizon | Best For |
|---|---|---|
| Statistical models (ARIMA) | Short-term (days-weeks) | Price time series |
| Fundamental models | Medium-term (months-quarters) | Supply-demand balance |
| Monte Carlo simulation | Medium-long term | Scenario/risk analysis |
| Machine learning | Short-medium term | Pattern recognition |
| Expert judgment | Long-term (years) | Structural shifts |

## Risk Management Metrics

| Metric | Definition | Use |
|---|---|---|
| VaR | Maximum loss at confidence level | Position sizing |
| CVaR | Expected loss beyond VaR | Tail risk assessment |
| Greeks (delta, gamma) | Sensitivity to price changes | Options hedging |
| Mark-to-market | Current portfolio value | P&L tracking |
| Stress testing | Loss under extreme scenarios | Capital adequacy |

## Using the Reference Files

### When to Read Each Reference

**`/references/power-gas-markets.md`** — Read when analyzing wholesale electricity markets, natural gas fundamentals, or developing hedging strategies for power or gas.

**`/references/oil-environmental-markets.md`** — Read when analyzing crude oil markets, refined products, renewable energy credits, carbon markets, or environmental compliance.

## Reference Files

This skill includes the following detailed reference materials:

- [Oil Environmental Markets](./references/oil-environmental-markets.md)
- [Power Gas Markets](./references/power-gas-markets.md)
