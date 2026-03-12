# Mathematical Modeling Techniques

## Regression Models

### Linear Regression
- **Simple**: y = β₀ + β₁x + ε
- **Multiple**: y = β₀ + β₁x₁ + β₂x₂ + ... + ε
- **Assumptions**: Linearity, independence, homoscedasticity, normality of residuals
- **Diagnostics**: Residual plots, Q-Q plots, VIF for multicollinearity

### Polynomial and Nonlinear Regression
- **Polynomial**: y = β₀ + β₁x + β₂x² + ... + βₙxⁿ
- **Exponential**: y = ae^(bx)
- **Power law**: y = axᵇ
- **Logistic growth**: y = K/(1 + e^(-r(x-x₀)))

### Model Selection Criteria
| Criterion | Formula | Use |
|-----------|---------|-----|
| R² | 1 - SS_res/SS_tot | Explained variance |
| Adjusted R² | 1 - (1-R²)(n-1)/(n-p-1) | Penalizes complexity |
| AIC | 2k - 2ln(L) | Model comparison |
| BIC | k·ln(n) - 2ln(L) | Favors simpler models |
| RMSE | √(Σ(y-ŷ)²/n) | Prediction error |

---

## Differential Equation Models

### Ordinary Differential Equations (ODEs)
- **First order**: dy/dt = f(t,y) — exponential growth/decay
- **Second order**: d²y/dt² = f(t,y,dy/dt) — oscillations, mechanics
- **Systems**: dx/dt = f(x,y), dy/dt = g(x,y) — interacting populations

### Classic ODE Models
| Model | Equation | Application |
|-------|----------|-------------|
| Exponential growth | dN/dt = rN | Unrestricted population |
| Logistic growth | dN/dt = rN(1-N/K) | Carrying capacity |
| SIR model | dS/dt=-βSI, dI/dt=βSI-γI | Epidemiology |
| Lotka-Volterra | dx/dt=αx-βxy, dy/dt=δxy-γy | Predator-prey |
| Newton's cooling | dT/dt=-k(T-Tₐ) | Heat transfer |

### Numerical Solution Methods
| Method | Order | Stability | Use Case |
|--------|-------|-----------|----------|
| Euler | 1st | Conditional | Teaching, simple problems |
| RK4 (Runge-Kutta) | 4th | Good | General purpose |
| Adams-Bashforth | Multi-step | Good | Long integrations |
| Implicit methods | Various | Unconditional | Stiff systems |

---

## Time Series Models

### Components
- **Trend**: Long-term direction
- **Seasonality**: Repeating patterns at fixed intervals
- **Cyclical**: Longer-term fluctuations
- **Noise**: Random variation

### Model Types
| Model | Best For | Complexity |
|-------|----------|-----------|
| Moving average | Smoothing, short-term | Low |
| Exponential smoothing | Trend + seasonality | Medium |
| ARIMA | Stationary series | Medium |
| SARIMA | Seasonal patterns | Medium-High |
| VAR | Multi-variable systems | High |
| Prophet | Business forecasting | Medium |

---

## Statistical Hypothesis Testing

### Test Selection Guide
| Data Type | Comparison | Test |
|-----------|-----------|------|
| Continuous, 2 groups | Means | t-test |
| Continuous, 3+ groups | Means | ANOVA |
| Categorical | Proportions | Chi-square |
| Continuous | Correlation | Pearson/Spearman |
| Non-normal | Distribution | Mann-Whitney, Kruskal-Wallis |
