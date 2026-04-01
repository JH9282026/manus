---
name: stock-market-analysis-trading
description: "This skill enables autonomous execution of sophisticated stock market analysis and trading strategy development across multiple analytical dimensions."
---

# Stock Market Analysis Trading

## Overview

This skill provides comprehensive guidance and best practices for this domain.

## Skill Description and Purpose

This skill enables autonomous execution of sophisticated stock market analysis and trading strategy development across multiple analytical dimensions. The skill synthesizes fundamental analysis of company financials, technical analysis of price action and chart patterns, macroeconomic indicator interpretation, and quantitative risk management into actionable investment recommendations.

**Core Analytical Capabilities:**

**Fundamental Analysis** encompasses deep evaluation of financial statements including income statements, balance sheets, and cash flow statements. The skill calculates and interprets key financial ratios including profitability metrics (ROE, ROA, net margin, gross margin), liquidity ratios (current ratio, quick ratio, cash ratio), leverage metrics (debt-to-equity, interest coverage, debt-to-EBITDA), and efficiency ratios (asset turnover, inventory turnover, receivables turnover). Valuation methodologies include DCF (Discounted Cash Flow) modeling, comparable company analysis using P/E, P/S, P/B, and EV/EBITDA multiples, and dividend discount models for income-generating equities.

**Technical Analysis** applies systematic chart pattern recognition including reversal patterns (head and shoulders, double/triple tops and bottoms, rounding tops/bottoms), continuation patterns (flags, pennants, wedges, rectangles, triangles—ascending, descending, and symmetrical), and complex formations (cup and handle, measured moves). Technical indicator implementation includes trend-following indicators (simple and exponential moving averages, MACD histogram and signal line crossovers), momentum oscillators (RSI with overbought/oversold identification, Stochastic oscillator, Williams %R), volatility measures (Bollinger Bands, Average True Range, standard deviation channels), and volume analysis (OBV, volume profile, accumulation/distribution).

**Macroeconomic Analysis** integrates GDP growth trajectories, inflation metrics (CPI, PPI, PCE), Federal Reserve monetary policy stance including interest rate decisions and quantitative easing/tightening, employment data (non-farm payrolls, unemployment rate, labor force participation), consumer sentiment indices, manufacturing PMI, and yield curve analysis for recession probability assessment.

**Trading Strategy Development** covers day trading setups with intraday momentum and mean reversion, swing trading with multi-day position management, position trading aligned with intermediate trends, and momentum strategies capturing relative strength outperformance. Each strategy incorporates specific entry triggers, position sizing rules, stop-loss placement, and profit-taking methodologies.

**Risk Management Framework** implements portfolio-level Value at Risk (VaR) calculations, position sizing using the Kelly Criterion or fixed-fractional methods, correlation analysis for diversification optimization, sector exposure limits, and drawdown management protocols.

## Required Inputs/Parameters

**Primary Analysis Inputs:**
- **Ticker Symbol(s):** Single equity or portfolio of up to 50 symbols for comparative analysis
- **Analysis Timeframe:** Short-term (1-30 days), intermediate (1-6 months), or long-term (1-5 years)
- **Investment Style:** Growth, value, income, momentum, or blended approach specification
- **Risk Tolerance Level:** Conservative (max 10% portfolio volatility), moderate (10-20%), aggressive (20%+)
- **Capital Allocation:** Total investable capital amount for position sizing calculations

**Fundamental Data Requirements:**
- **Financial Statements:** Minimum 3 years (preferably 5-10 years) of quarterly and annual reports
- **Earnings Data:** EPS history, analyst estimates, earnings surprise history
- **Industry Classification:** Sector and sub-industry for peer comparison selection

**Technical Data Requirements:**
- **Price Data:** OHLCV (Open, High, Low, Close, Volume) data with specified granularity (1-minute to monthly)
- **Chart Timeframe:** Primary analysis timeframe plus higher and lower timeframes for multi-timeframe confirmation
- **Indicator Parameters:** Custom settings for moving average periods, RSI periods, Bollinger Band standard deviations

**Macroeconomic Context:**
- **Market Regime:** Bull market, bear market, or ranging/consolidation identification
- **Economic Cycle Phase:** Expansion, peak, contraction, or trough positioning
- **Interest Rate Environment:** Rising, falling, or stable rate trajectory

**User Preference Parameters:**
- **Holding Period:** Target investment horizon for strategy alignment
- **Dividend Preference:** Income requirement (if any) for yield-focused screening
- **ESG Constraints:** Environmental, social, governance exclusion criteria (optional)
- **Sector Restrictions:** Industries to exclude from consideration (optional)

## Expected Outputs/Deliverables

**Comprehensive Analysis Report:**
- **Executive Summary:** One-paragraph synthesis with clear directional bias (bullish/bearish/neutral) and confidence level (high/medium/low)
- **Fundamental Score:** Quantified rating (1-100) with component breakdowns for financial health, growth prospects, valuation attractiveness, and competitive positioning
- **Technical Score:** Quantified rating incorporating trend strength, momentum readings, pattern quality, and volume confirmation

**Valuation Assessment:**
- **Intrinsic Value Estimate:** DCF-derived fair value with bull/base/bear case scenarios
- **Relative Valuation:** Current multiples versus 5-year averages, sector peers, and market indices
- **Price Target:** 12-month price target with upside/downside percentage and probability weighting

**Technical Trading Plan:**
- **Pattern Identification:** Current chart formations with completion targets and failure levels
- **Support/Resistance Map:** Key price levels with volume confirmation strength ratings
- **Indicator Dashboard:** Current readings for RSI, MACD, moving average relationships, and Bollinger Band position
- **Entry Zones:** Optimal price ranges for position initiation with trigger conditions
- **Stop-Loss Levels:** Initial protective stops and trailing stop methodology
- **Profit Targets:** Primary, secondary, and stretch targets with risk/reward ratios

**Risk Metrics:**
- **Position Size Recommendation:** Share quantity or dollar amount based on account size and risk parameters
- **Maximum Loss Exposure:** Dollar and percentage risk per trade and portfolio impact
- **Correlation Analysis:** How position affects overall portfolio diversification
- **Volatility Assessment:** Historical and implied volatility context

**Sector & Market Context:**
- **Sector Relative Strength:** Performance versus S&P 500 and sector rotation positioning
- **Market Breadth Assessment:** Advance/decline analysis, new highs/lows, percentage above moving averages
- **Sentiment Indicators:** Put/call ratios, VIX levels, investor surveys synthesis

## Example Use Cases

**Use Case 1: Growth Stock Deep Dive**
A technology sector investor requests comprehensive analysis of NVIDIA (NVDA) for potential portfolio addition. The skill executes fundamental analysis examining revenue growth trajectories in data center and AI segments, gross margin expansion, R&D investment intensity, and competitive moat assessment. Technical analysis identifies the current trend phase, key moving average support levels, RSI momentum readings, and cup-and-handle or ascending triangle formations. Macroeconomic overlay considers interest rate sensitivity for growth stocks, semiconductor cycle positioning, and AI infrastructure spending forecasts. Output includes a 12-month price target, optimal entry zone between the 50-day and 100-day moving average, 8% stop-loss recommendation, and position size of 3% of portfolio given high-beta characteristics.

**Use Case 2: Dividend Income Portfolio Construction**
A retiree seeks construction of a 15-stock dividend portfolio emphasizing income stability and capital preservation. The skill screens for dividend aristocrats with 25+ years of consecutive increases, payout ratios below 60%, debt-to-equity under 1.0, and current yields above 3%. Technical analysis filters for stocks in established uptrends or near support levels. Sector diversification ensures no more than 20% allocation to any single sector. Output includes ranked recommendations with yield, growth rate, payout safety score, and suggested allocation weights totaling 100%.

**Use Case 3: Swing Trading Setup Identification**
An active trader requests daily scan for swing trading opportunities in the S&P 500. The skill identifies stocks breaking out of consolidation patterns with volume confirmation, pulling back to rising 20-day moving averages, or showing RSI divergences at support levels. Each setup includes specific entry price, stop-loss level (typically below recent swing low), target prices at measured move objectives, and risk/reward ratio minimum of 2:1. Output delivers a watchlist of 5-10 actionable setups ranked by probability and risk/reward profile.

**Use Case 4: Market Regime Assessment**
An investment committee requests quarterly market outlook incorporating all analytical dimensions. The skill analyzes S&P 500 technical structure (trend, breadth, momentum), sector rotation patterns (cyclicals versus defensives), macroeconomic indicators (yield curve, PMI, employment trends), and sentiment extremes (VIX, put/call, investor surveys). Output provides market regime classification, sector overweight/underweight recommendations, and tactical asset allocation adjustments for the coming quarter.

**Use Case 5: Earnings Trade Evaluation**
A trader evaluates pre-earnings positioning for Microsoft (MSFT). The skill examines historical earnings surprise patterns, typical post-earnings price moves, current implied volatility versus historical realized volatility, analyst estimate dispersion, and technical setup into the report. Output recommends directional position, options strategy consideration if appropriate, position size reflecting earnings event risk, and specific stop-loss accounting for typical earnings-related gaps.

## Prerequisites or Dependencies

**Data Access Requirements:**
- Real-time or delayed equity price feeds (15-minute delay acceptable for swing/position trading)
- Fundamental data provider access (financial statements, ratios, estimates)—sources include Yahoo Finance, Alpha Vantage, Financial Modeling Prep, or premium providers like Bloomberg or Refinitiv
- Economic calendar and macroeconomic data series (FRED database integration recommended)
- Charting capability with technical indicator calculation libraries

**Technical Infrastructure:**
- Python environment with pandas, numpy, and scipy for quantitative calculations
- Technical analysis libraries: TA-Lib, pandas-ta, or custom indicator implementations
- Visualization capabilities for chart generation (matplotlib, plotly)
- Backtesting framework for strategy validation (optional but recommended)

**Knowledge Prerequisites:**
- Understanding of financial statement structure and accounting principles
- Familiarity with technical analysis concepts and chart interpretation
- Awareness of market microstructure (order types, execution, slippage)
- Recognition of personal risk tolerance and investment objectives

**Regulatory Awareness:**
- Pattern Day Trader rules (PDT) for accounts under $25,000 executing 4+ day trades in 5 business days
- Wash sale rules affecting loss harvesting strategies
- Margin requirements and maintenance margin levels
- Insider trading restrictions and material non-public information (MNPI) compliance

**Execution Capabilities:**
- Brokerage account with appropriate trading permissions (stocks, possibly options)
- Order management system or broker API integration for automated execution (if applicable)
- Risk management tools for stop-loss implementation and position monitoring

## References

- [01 Technical Analysis Fundamentals](references/01_technical_analysis_fundamentals.md)
- [02 Technical Indicators Guide](references/02_technical_indicators_guide.md)
- [03 Fundamental Analysis Basics](references/03_fundamental_analysis_basics.md)
- [04 Trading Strategies Risk Management](references/04_trading_strategies_risk_management.md)
