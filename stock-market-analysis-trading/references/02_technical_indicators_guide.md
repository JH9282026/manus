# Technical Indicators Guide for Stock Trading

## Overview
Technical indicators are mathematical calculations based on price, volume, or open interest data. They help traders identify trends, momentum, volatility, and potential entry/exit points.

## Trend Indicators

### Moving Averages (MA)

**Simple Moving Average (SMA)**
- Average price over specified period
- Equal weight to all prices
- Smooths price data
- Lagging indicator

**Calculation:**
```
SMA = (P1 + P2 + ... + Pn) / n
```

**Common Periods:**
- 20-day: Short-term trend
- 50-day: Medium-term trend
- 200-day: Long-term trend

**Trading Signals:**
- Price above MA: Bullish
- Price below MA: Bearish
- MA crossovers: Trend changes

**Exponential Moving Average (EMA)**
- More weight to recent prices
- More responsive than SMA
- Better for short-term trading

**Calculation:**
```
EMA = (Price - Previous EMA) × Multiplier + Previous EMA
Multiplier = 2 / (Period + 1)
```

**Advantages:**
- Faster response to price changes
- Less lag than SMA
- Better for volatile markets

### Moving Average Convergence Divergence (MACD)

**Components:**
- MACD Line: 12-day EMA - 26-day EMA
- Signal Line: 9-day EMA of MACD
- Histogram: MACD - Signal Line

**Signals:**
- MACD crosses above signal: Bullish
- MACD crosses below signal: Bearish
- Histogram expansion: Trend strengthening
- Histogram contraction: Trend weakening

**Divergence:**
- Bullish: Price makes lower low, MACD makes higher low
- Bearish: Price makes higher high, MACD makes lower high

**Best For:**
- Trend identification
- Momentum shifts
- Divergence trading

### Average Directional Index (ADX)

**Purpose:** Measures trend strength (not direction).

**Components:**
- ADX Line: Trend strength (0-100)
- +DI: Positive directional indicator
- -DI: Negative directional indicator

**Interpretation:**
- ADX < 20: Weak or no trend
- ADX 20-40: Developing trend
- ADX > 40: Strong trend
- ADX > 50: Very strong trend

**Trading Strategy:**
- +DI above -DI: Uptrend
- -DI above +DI: Downtrend
- ADX rising: Trend strengthening
- ADX falling: Trend weakening

## Momentum Indicators

### Relative Strength Index (RSI)

**Purpose:** Measures speed and magnitude of price changes.

**Calculation:**
```
RSI = 100 - [100 / (1 + RS)]
RS = Average Gain / Average Loss (typically 14 periods)
```

**Range:** 0 to 100

**Interpretation:**
- RSI > 70: Overbought (potential sell)
- RSI < 30: Oversold (potential buy)
- RSI 40-60: Neutral zone

**Advanced Signals:**
- Divergence: Price vs. RSI direction mismatch
- Failure swings: RSI reversal patterns
- Centerline crossover: 50 level

**Best Practices:**
- Adjust levels for trending markets (80/20)
- Use with other indicators
- Consider timeframe
- Watch for divergences

### Stochastic Oscillator

**Purpose:** Compares closing price to price range over period.

**Components:**
- %K Line: Fast stochastic
- %D Line: Slow stochastic (3-period SMA of %K)

**Calculation:**
```
%K = [(Close - Lowest Low) / (Highest High - Lowest Low)] × 100
```

**Interpretation:**
- > 80: Overbought
- < 20: Oversold
- %K crosses above %D: Buy signal
- %K crosses below %D: Sell signal

**Advantages:**
- More sensitive than RSI
- Good for range-bound markets
- Clear overbought/oversold levels

**Cautions:**
- Can stay overbought/oversold in trends
- Many false signals in trending markets
- Best in sideways markets

### Commodity Channel Index (CCI)

**Purpose:** Identifies cyclical trends and overbought/oversold conditions.

**Calculation:**
```
CCI = (Typical Price - SMA) / (0.015 × Mean Deviation)
Typical Price = (High + Low + Close) / 3
```

**Interpretation:**
- CCI > +100: Overbought
- CCI < -100: Oversold
- Crossing above -100: Buy signal
- Crossing below +100: Sell signal

**Trading Strategy:**
- Buy when CCI crosses above -100
- Sell when CCI crosses below +100
- Extreme readings (>200, <-200) signal reversals

## Volatility Indicators

### Bollinger Bands

**Components:**
- Middle Band: 20-period SMA
- Upper Band: Middle + (2 × Standard Deviation)
- Lower Band: Middle - (2 × Standard Deviation)

**Interpretation:**
- Price at upper band: Overbought
- Price at lower band: Oversold
- Band width: Volatility measure
- Band squeeze: Low volatility, potential breakout

**Trading Strategies:**
- **Bounce:** Buy at lower band, sell at upper band
- **Breakout:** Trade breaks outside bands
- **Squeeze:** Anticipate volatility expansion

**Bollinger Band Width:**
- Measures distance between bands
- Low width: Low volatility (squeeze)
- High width: High volatility
- Expansion after squeeze: Trend beginning

### Average True Range (ATR)

**Purpose:** Measures market volatility.

**Calculation:**
```
True Range = Max of:
- High - Low
- |High - Previous Close|
- |Low - Previous Close|

ATR = Average of True Range over period (typically 14)
```

**Uses:**
- Position sizing
- Stop-loss placement
- Volatility assessment
- Not directional

**Applications:**
- Set stops at 2× ATR from entry
- Adjust position size based on ATR
- Identify volatility breakouts
- Compare volatility across assets

### Standard Deviation

**Purpose:** Measures price dispersion from average.

**Interpretation:**
- Higher SD: Higher volatility
- Lower SD: Lower volatility
- Expanding SD: Increasing volatility
- Contracting SD: Decreasing volatility

**Uses:**
- Volatility forecasting
- Risk assessment
- Bollinger Bands calculation
- Option pricing inputs

## Volume Indicators

### On-Balance Volume (OBV)

**Purpose:** Relates volume to price changes.

**Calculation:**
```
If Close > Previous Close: OBV = Previous OBV + Volume
If Close < Previous Close: OBV = Previous OBV - Volume
If Close = Previous Close: OBV = Previous OBV
```

**Interpretation:**
- Rising OBV: Buying pressure
- Falling OBV: Selling pressure
- OBV confirms price trend
- Divergence signals reversal

**Trading Signals:**
- OBV and price both rising: Strong uptrend
- OBV rising, price falling: Bullish divergence
- OBV falling, price rising: Bearish divergence

### Volume-Weighted Average Price (VWAP)

**Purpose:** Average price weighted by volume.

**Calculation:**
```
VWAP = Σ(Price × Volume) / Σ(Volume)
```

**Uses:**
- Intraday benchmark
- Institutional reference
- Support/resistance level
- Trade execution quality

**Trading Strategy:**
- Price above VWAP: Bullish
- Price below VWAP: Bearish
- VWAP as support/resistance
- Reversion to VWAP trades

### Accumulation/Distribution Line

**Purpose:** Measures cumulative flow of money.

**Calculation:**
```
Money Flow Multiplier = [(Close - Low) - (High - Close)] / (High - Low)
Money Flow Volume = Money Flow Multiplier × Volume
A/D = Previous A/D + Money Flow Volume
```

**Interpretation:**
- Rising A/D: Accumulation
- Falling A/D: Distribution
- Divergence with price: Reversal signal

## Combining Indicators

### Complementary Indicators
Use indicators from different categories.

**Example Combination:**
- Trend: Moving Average
- Momentum: RSI
- Volume: OBV
- Volatility: Bollinger Bands

**Benefits:**
- Confirmation from multiple sources
- Reduced false signals
- Comprehensive market view
- Better risk management

### Avoiding Redundancy
Don't use multiple indicators measuring same thing.

**Redundant Combinations:**
- RSI + Stochastic (both momentum)
- SMA + EMA (both trend)
- Multiple moving averages of similar periods

**Better Approach:**
- One from each category
- Different timeframes
- Complementary information

## Indicator Settings

### Default vs. Custom Settings

**Default Settings:**
- RSI: 14 periods
- MACD: 12, 26, 9
- Bollinger Bands: 20, 2
- Stochastic: 14, 3, 3

**Customization Considerations:**
- Trading timeframe
- Asset volatility
- Market conditions
- Personal preference

**Optimization:**
- Backtest different settings
- Avoid over-optimization
- Keep it simple
- Document changes

## Best Practices

1. **Use Multiple Indicators:** Confirm signals
2. **Understand Calculations:** Know what you're using
3. **Avoid Indicator Overload:** 3-4 maximum
4. **Consider Context:** Market conditions matter
5. **Combine with Price Action:** Indicators support, not replace
6. **Adjust for Timeframe:** Different settings for different timeframes
7. **Watch for Divergences:** Powerful reversal signals
8. **Don't Ignore Volume:** Confirms price movements
9. **Backtest Strategies:** Verify effectiveness
10. **Stay Flexible:** Adapt to changing markets

## Common Mistakes

1. **Too Many Indicators:** Analysis paralysis
2. **Ignoring Price Action:** Over-relying on indicators
3. **Using Conflicting Indicators:** Contradictory signals
4. **Not Understanding Indicators:** Misinterpretation
5. **Chasing Signals:** Acting on every indicator signal
6. **Ignoring Market Context:** Using same indicators in all conditions
7. **Over-Optimization:** Curve-fitting to past data
8. **No Confirmation:** Acting on single indicator
9. **Wrong Timeframe:** Indicator period doesn't match trading style
10. **Forgetting Lag:** Indicators are based on past data

## References

- Investopedia. \"Top 7 Technical Analysis Tools\" https://www.investopedia.com/top-7-technical-analysis-tools-4773275
- Fidelity. \"Technical Indicator Guide\" https://www.fidelity.com/learning-center/trading-investing/technical-analysis/technical-indicator-guide/overview
- Schwab. \"Choosing Technical Indicators\" https://www.schwab.com/learn/story/choosing-technical-indicators-to-analyze-stocks
- Highcharts. \"7 Popular Technical Tools\" https://www.highcharts.com/blog/tutorials/stock-indicators-7-popular-technical-tools/
