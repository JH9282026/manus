# Financial Modeling Fundamentals

Comprehensive guide to building three-statement financial models and fundamental modeling techniques.

---

## Three-Statement Model Construction

### Overview

The three-statement model is the foundation of financial modeling. It integrates the income statement, balance sheet, and cash flow statement to create a dynamic forecast of a company's financial performance. Changes in one statement automatically flow through to the others, creating an interconnected financial picture.

### Why Three Statements?

**Comprehensive View**:
- Income statement shows profitability
- Balance sheet shows financial position
- Cash flow statement shows liquidity

**Interconnected**:
- Net income flows to retained earnings
- Balance sheet changes drive cash flow
- Cash flow determines cash balance

**Foundation for Advanced Models**:
- DCF valuation
- M&A models
- LBO models
- Project finance

---

## Building the Income Statement

### Revenue Forecasting

#### Top-Down Approach

**Market-Based Forecasting**:

1. **Total Addressable Market (TAM)**:
   - Define total market size
   - Research industry reports
   - Consider geographic scope

2. **Market Growth Rate**:
   - Historical growth trends
   - Industry forecasts
   - Economic indicators

3. **Market Share**:
   - Current market share
   - Competitive position
   - Market share trajectory

4. **Revenue Calculation**:
   Revenue = TAM × Market Growth × Market Share

**Example**:
- TAM: $10 billion
- Market growth: 5% annually
- Current market share: 3%
- Year 1 Revenue: $10B × 1.05 × 0.03 = $315M

#### Bottom-Up Approach

**Unit Economics**:

1. **Volume Drivers**:
   - Number of customers
   - Units sold
   - Transactions
   - Users or subscribers

2. **Price Drivers**:
   - Average selling price
   - Price per unit
   - Subscription price
   - Revenue per user

3. **Revenue Calculation**:
   Revenue = Volume × Price

**Example (SaaS Company)**:
- Beginning customers: 1,000
- New customers per month: 100
- Churn rate: 2% per month
- Average revenue per user (ARPU): $50/month
- Monthly revenue = (Beginning + New - Churned) × ARPU

#### Segment-Level Forecasting

**Product Segments**:
- Forecast each product line separately
- Different growth rates and margins
- Sum to total revenue

**Geographic Segments**:
- Forecast each region separately
- Different market dynamics
- Currency considerations

**Customer Segments**:
- Enterprise vs. SMB
- New vs. existing customers
- Different pricing and retention

### Cost of Goods Sold (COGS)

#### Variable Costs

**Direct Materials**:
- Raw materials
- Components
- Packaging
- As percentage of revenue or per unit

**Direct Labor**:
- Production labor
- Manufacturing wages
- Variable with production volume

**Variable Overhead**:
- Utilities (production)
- Supplies
- Shipping and freight

**Calculation**:
COGS = Revenue × COGS %

Or:

COGS = Units Sold × Cost per Unit

#### Fixed Costs in COGS

**Manufacturing Overhead**:
- Factory rent
- Equipment depreciation
- Supervisory salaries
- Quality control

**Allocation**:
- Allocate based on production volume
- Consider capacity utilization
- Adjust for economies of scale

#### Gross Profit and Margin

**Gross Profit**:
Gross Profit = Revenue - COGS

**Gross Margin**:
Gross Margin % = (Gross Profit / Revenue) × 100

**Analysis**:
- Track margin trends
- Compare to industry benchmarks
- Identify margin drivers
- Assess pricing power

### Operating Expenses

#### Sales and Marketing (S&M)

**Components**:
- Sales salaries and commissions
- Marketing programs and advertising
- Trade shows and events
- Marketing technology
- Sales support

**Forecasting Methods**:
- As percentage of revenue (typical: 10-30%)
- Headcount-based (salaries + programs)
- Customer acquisition cost (CAC) based

#### Research and Development (R&D)

**Components**:
- R&D salaries
- Product development
- Engineering costs
- Testing and prototyping
- Technology infrastructure

**Forecasting Methods**:
- As percentage of revenue (typical: 5-20% for tech)
- Headcount-based
- Project-based

#### General and Administrative (G&A)

**Components**:
- Executive salaries
- Finance and accounting
- Human resources
- Legal and compliance
- Facilities (non-production)
- IT (non-product)

**Forecasting Methods**:
- As percentage of revenue (typical: 5-15%)
- Headcount-based
- Fixed amount with inflation adjustment

### EBITDA

**Calculation**:
EBITDA = Revenue - COGS - Operating Expenses

Or:

EBITDA = Gross Profit - Operating Expenses

**Importance**:
- Key profitability metric
- Excludes non-cash items (D&A)
- Excludes financing and tax effects
- Used in valuation multiples
- Proxy for operating cash flow

**EBITDA Margin**:
EBITDA Margin % = (EBITDA / Revenue) × 100

### Depreciation and Amortization

#### Depreciation

**Source**: Linked from PP&E schedule

**Methods**:

**Straight-Line**:
Annual Depreciation = (Asset Cost - Salvage Value) / Useful Life

**Percentage of Revenue**:
Depreciation = Revenue × Depreciation %

**Percentage of PP&E**:
Depreciation = PP&E (gross) × Depreciation Rate

#### Amortization

**Intangible Assets**:
- Patents
- Trademarks
- Customer relationships
- Technology
- Goodwill (not amortized under US GAAP, tested for impairment)

**Calculation**:
Amortization = Intangible Asset Value / Useful Life

### EBIT (Operating Income)

**Calculation**:
EBIT = EBITDA - Depreciation - Amortization

**Also Called**:
- Operating income
- Operating profit
- Earnings before interest and taxes

### Interest Expense and Income

#### Interest Expense

**Source**: Linked from debt schedule

**Calculation**:
Interest Expense = Average Debt Balance × Interest Rate

**Average Balance**:
Average Debt = (Beginning Debt + Ending Debt) / 2

**Multiple Debt Tranches**:
- Calculate separately for each tranche
- Different interest rates
- Different balances
- Sum total interest expense

#### Interest Income

**Source**: Cash and investments

**Calculation**:
Interest Income = Average Cash Balance × Interest Rate

**Typically**:
- Small relative to interest expense
- Often ignored in models
- Include if material

### Earnings Before Tax (EBT)

**Calculation**:
EBT = EBIT - Interest Expense + Interest Income

**Also Called**:
- Pre-tax income
- Income before taxes

### Income Tax Expense

#### Effective Tax Rate Method

**Calculation**:
Tax Expense = EBT × Effective Tax Rate

**Effective Tax Rate**:
- Historical average
- Statutory rate adjusted for:
  - State and local taxes
  - Foreign tax rates
  - Tax credits
  - Permanent differences

**Typical Rates**:
- US Federal: 21% (as of 2026)
- State: 0-13% (varies by state)
- Combined: 21-34%
- International: varies widely

#### Tax Loss Carryforwards

**Net Operating Losses (NOLs)**:
- Losses from prior years
- Can offset future taxable income
- Reduce tax expense

**Modeling**:
- Track NOL balance
- Reduce by taxable income each year
- Tax expense = 0 until NOLs exhausted
- Then apply normal tax rate

### Net Income

**Calculation**:
Net Income = EBT - Tax Expense

**Also Called**:
- Net profit
- Net earnings
- Bottom line

**Uses**:
- Flows to retained earnings on balance sheet
- Basis for earnings per share (EPS)
- Starting point for cash flow statement

### Earnings Per Share (EPS)

**Basic EPS**:
Basic EPS = Net Income / Weighted Average Shares Outstanding

**Diluted EPS**:
Diluted EPS = Net Income / Fully Diluted Shares Outstanding

**Fully Diluted Shares**:
- Common shares outstanding
- Plus: In-the-money stock options (treasury stock method)
- Plus: Convertible securities
- Plus: Warrants and other dilutive securities

---

## Building the Balance Sheet

### Assets

#### Current Assets

**Cash and Cash Equivalents**:

**Methods**:

1. **Plug Method** (Most Common):
   - Cash is the balancing item
   - Ensures balance sheet balances
   - Calculated last

2. **Minimum Cash Balance**:
   - Set minimum operating cash
   - Excess cash invested or used to pay down debt
   - Shortfalls covered by revolver

3. **Cash Flow Method**:
   - Beginning cash + cash flow = ending cash
   - Requires completed cash flow statement

**Accounts Receivable (AR)**:

**Days Sales Outstanding (DSO) Method**:

AR = (Revenue / 365) × DSO

**Calculation**:
1. Calculate historical DSO
2. Project future DSO (typically stable or improving)
3. Apply to forecasted revenue

**Typical DSO**:
- B2B: 30-60 days
- B2C: 0-15 days (credit cards)
- Enterprise software: 60-90 days

**Inventory**:

**Days Inventory Outstanding (DIO) Method**:

Inventory = (COGS / 365) × DIO

**Calculation**:
1. Calculate historical DIO
2. Project future DIO
3. Apply to forecasted COGS

**Typical DIO**:
- Retail: 30-60 days
- Manufacturing: 60-90 days
- Perishables: 7-14 days

**Other Current Assets**:
- Prepaid expenses
- Short-term investments
- Other receivables
- Typically as % of revenue or flat amount

#### Non-Current Assets

**Property, Plant, and Equipment (PP&E)**:

**Source**: Linked from PP&E schedule

**Net PP&E**:
Net PP&E = Gross PP&E - Accumulated Depreciation

**Intangible Assets**:
- Patents, trademarks, technology
- Customer relationships
- Amortized over useful life
- Net of accumulated amortization

**Goodwill**:
- Arises from acquisitions
- Not amortized (US GAAP)
- Tested for impairment annually
- Typically constant unless new acquisitions

**Other Long-Term Assets**:
- Long-term investments
- Deferred tax assets
- Other assets

### Liabilities

#### Current Liabilities

**Accounts Payable (AP)**:

**Days Payable Outstanding (DPO) Method**:

AP = (COGS / 365) × DPO

**Calculation**:
1. Calculate historical DPO
2. Project future DPO
3. Apply to forecasted COGS

**Typical DPO**:
- Most industries: 30-60 days
- Retail (strong negotiating power): 60-90 days

**Accrued Expenses**:
- Accrued salaries and wages
- Accrued interest
- Accrued taxes
- Other accruals
- Typically as % of revenue or operating expenses

**Short-Term Debt**:
- Debt due within one year
- Current portion of long-term debt
- Linked from debt schedule

**Other Current Liabilities**:
- Deferred revenue (unearned revenue)
- Customer deposits
- Other short-term obligations

#### Non-Current Liabilities

**Long-Term Debt**:

**Source**: Linked from debt schedule

**Components**:
- Term loans
- Bonds
- Notes payable
- Capital leases
- Less: Current portion

**Deferred Tax Liabilities**:
- Timing differences between book and tax accounting
- Typically related to depreciation
- Complex calculation, often simplified in models

**Other Long-Term Liabilities**:
- Pension obligations
- Operating lease liabilities (IFRS 16)
- Other long-term obligations

### Shareholders' Equity

**Common Stock**:
- Par value × shares outstanding
- Typically small amount
- Increases with new issuances

**Additional Paid-In Capital (APIC)**:
- Amount received above par value
- From stock issuances
- Stock-based compensation

**Retained Earnings**:

**Calculation**:
Ending RE = Beginning RE + Net Income - Dividends

**Key Link**: Net income from income statement flows here

**Treasury Stock**:
- Company's own shares repurchased
- Contra-equity account (negative)
- Reduces total equity

**Accumulated Other Comprehensive Income (AOCI)**:
- Foreign currency translation adjustments
- Unrealized gains/losses on investments
- Pension adjustments
- Often immaterial, can be ignored in models

### Balance Sheet Checks

**Fundamental Equation**:
Assets = Liabilities + Shareholders' Equity

**Balance Check**:
Balance Check = Total Assets - Total Liabilities - Total Equity

**Should Equal Zero**

**Conditional Formatting**:
- Highlight cell if not zero
- Red background for errors
- Immediate visual feedback

**Common Causes of Imbalance**:
- Formula errors
- Incorrect links
- Missing items
- Circular reference issues
- Timing mismatches

---

## Building the Cash Flow Statement

### Overview

The cash flow statement reconciles net income (accrual basis) to cash flow (cash basis) and explains the change in cash balance from one period to the next.

**Structure**:
1. Operating Activities
2. Investing Activities
3. Financing Activities
4. Net Change in Cash

### Operating Activities

#### Starting Point: Net Income

**From**: Income statement

#### Non-Cash Adjustments

**Add Back**:
- Depreciation and amortization (non-cash expense)
- Stock-based compensation (non-cash expense)
- Deferred taxes (timing difference)
- Losses on asset sales
- Impairment charges

**Subtract**:
- Gains on asset sales
- Other non-cash income

#### Changes in Working Capital

**Concept**: Changes in current assets and liabilities affect cash

**Increase in Current Assets = Use of Cash**:
- More AR = cash not yet collected
- More inventory = cash tied up

**Decrease in Current Assets = Source of Cash**:
- Less AR = cash collected
- Less inventory = cash freed up

**Increase in Current Liabilities = Source of Cash**:
- More AP = cash not yet paid
- More accruals = expenses not yet paid

**Decrease in Current Liabilities = Use of Cash**:
- Less AP = cash paid out
- Less accruals = expenses paid

**Calculation**:

Change in AR = Ending AR - Beginning AR

Cash Flow Impact = -(Change in AR)

**Working Capital Items**:
- Accounts receivable (negative of change)
- Inventory (negative of change)
- Other current assets (negative of change)
- Accounts payable (positive of change)
- Accrued expenses (positive of change)
- Other current liabilities (positive of change)

**Cash Flow from Operations (CFO)**:
CFO = Net Income + Non-Cash Adjustments - Change in NWC

### Investing Activities

**Capital Expenditures (CapEx)**:
- Purchase of PP&E
- Largest investing activity for most companies
- Negative cash flow (use of cash)
- Linked from PP&E schedule

**Acquisitions**:
- Purchase of other businesses
- Negative cash flow
- Typically one-time events

**Asset Sales**:
- Sale of PP&E or businesses
- Positive cash flow
- Proceeds from sale

**Investments**:
- Purchase of securities or equity stakes
- Negative cash flow
- Sale of investments = positive cash flow

**Cash Flow from Investing (CFI)**:
CFI = -CapEx - Acquisitions + Asset Sales - Investments

**Typically Negative**: Most companies invest more than they divest

### Financing Activities

**Debt Issuance**:
- New borrowings
- Positive cash flow (source of cash)
- Linked from debt schedule

**Debt Repayment**:
- Principal repayments
- Negative cash flow (use of cash)
- Linked from debt schedule

**Equity Issuance**:
- Sale of new shares
- Positive cash flow
- IPOs, secondary offerings, PIPE

**Share Repurchases**:
- Buyback of company stock
- Negative cash flow
- Return of capital to shareholders

**Dividends Paid**:
- Cash dividends to shareholders
- Negative cash flow
- Dividend per share × shares outstanding

**Cash Flow from Financing (CFF)**:
CFF = Debt Issuance - Debt Repayment + Equity Issuance - Share Repurchases - Dividends

### Net Change in Cash

**Calculation**:
Net Change in Cash = CFO + CFI + CFF

**Ending Cash Balance**:
Ending Cash = Beginning Cash + Net Change in Cash

**Verification**:
Ending cash from cash flow statement should equal cash on balance sheet

**If Not Equal**: Error in model, need to troubleshoot

---

## Supporting Schedules

### PP&E Schedule

**Purpose**: Track gross PP&E, capital expenditures, depreciation, and net PP&E

**Structure**:

```
Beginning PP&E (Gross)
+ Capital Expenditures
- Asset Disposals
= Ending PP&E (Gross)

Beginning Accumulated Depreciation
+ Depreciation Expense
- Accumulated Depreciation on Disposals
= Ending Accumulated Depreciation

Net PP&E = Gross PP&E - Accumulated Depreciation
```

**Capital Expenditures Forecasting**:

**Methods**:

1. **Percentage of Revenue**:
   CapEx = Revenue × CapEx %
   - Use historical average
   - Adjust for growth stage

2. **Maintenance vs. Growth CapEx**:
   - Maintenance CapEx = Depreciation (replace existing assets)
   - Growth CapEx = Additional investment for growth
   - Total CapEx = Maintenance + Growth

3. **Detailed Build-Up**:
   - Specific projects and investments
   - Timing of expenditures
   - Most accurate but time-consuming

**Depreciation Calculation**:

**Straight-Line Method**:
Annual Depreciation = Gross PP&E / Average Useful Life

**Percentage of Gross PP&E**:
Depreciation = Gross PP&E × Depreciation Rate

**Percentage of Revenue**:
Depreciation = Revenue × Depreciation %

**Links**:
- Net PP&E → Balance Sheet (Non-Current Assets)
- Depreciation → Income Statement (below EBITDA)
- CapEx → Cash Flow Statement (Investing Activities)

### Debt Schedule

**Purpose**: Track debt balances, borrowings, repayments, and interest expense

**Structure**:

```
Beginning Debt Balance
+ New Borrowings
- Mandatory Repayments
- Optional Repayments
= Ending Debt Balance

Average Debt Balance = (Beginning + Ending) / 2
Interest Expense = Average Balance × Interest Rate
```

**Multiple Debt Tranches**:
- Separate schedule for each tranche
- Different interest rates
- Different maturity dates
- Different repayment terms

**Debt Types**:

**Term Loan**:
- Fixed maturity
- Scheduled repayments (amortization)
- Fixed or floating interest rate

**Revolver (Line of Credit)**:
- Flexible borrowing up to limit
- Acts as plug for cash shortfalls
- Repaid when cash available
- Commitment fee on unused portion

**Bonds**:
- Fixed maturity
- Interest-only payments (coupon)
- Principal repaid at maturity
- Fixed interest rate

**Revolver Mechanics**:

**Draw Logic**:
```
IF(Cash Balance < Minimum Cash, 
   Draw Amount = Minimum Cash - Cash Balance,
   Draw Amount = 0)
```

**Repayment Logic**:
```
IF(Cash Balance > Minimum Cash,
   Repayment = MIN(Excess Cash, Revolver Balance),
   Repayment = 0)
```

**Using MAX/MIN Functions**:
```
Revolver Draw = MAX(0, Minimum Cash - Cash Before Revolver)
Revolver Repayment = MIN(Revolver Balance, MAX(0, Cash Before Revolver - Minimum Cash))
```

**Links**:
- Debt Balance → Balance Sheet (Current and Long-Term Debt)
- Interest Expense → Income Statement
- Borrowings and Repayments → Cash Flow Statement (Financing Activities)

### Working Capital Schedule

**Purpose**: Calculate working capital items based on operational drivers

**Accounts Receivable**:
```
Days Sales Outstanding (DSO) = (AR / Revenue) × 365
AR = (Revenue / 365) × DSO
```

**Inventory**:
```
Days Inventory Outstanding (DIO) = (Inventory / COGS) × 365
Inventory = (COGS / 365) × DIO
```

**Accounts Payable**:
```
Days Payable Outstanding (DPO) = (AP / COGS) × 365
AP = (COGS / 365) × DPO
```

**Net Working Capital (NWC)**:

**Operating NWC**:
NWC = AR + Inventory - AP

**Total NWC**:
NWC = Current Assets - Current Liabilities

**Change in NWC**:
Change in NWC = Ending NWC - Beginning NWC

**Cash Flow Impact**:
Cash Flow Impact = -(Change in NWC)

**Interpretation**:
- Increase in NWC = Use of cash (cash tied up in operations)
- Decrease in NWC = Source of cash (cash released from operations)

**Links**:
- AR, Inventory, AP → Balance Sheet
- Change in NWC → Cash Flow Statement (Operating Activities)

---

## Handling Circularity

### Understanding Circular References

**Definition**: A circular reference occurs when a formula directly or indirectly refers to its own cell.

**In Financial Models**:
- Interest expense depends on debt balance
- Debt balance depends on cash flow
- Cash flow depends on interest expense
- Creates circular loop

**Example**:
1. Interest Expense = Average Debt × Interest Rate
2. Net Income = EBIT - Interest Expense - Taxes
3. Cash Flow = Net Income + Adjustments
4. Ending Cash = Beginning Cash + Cash Flow
5. Ending Debt = Beginning Debt - Excess Cash (if any)
6. Average Debt = (Beginning Debt + Ending Debt) / 2
7. Back to step 1 (circular!)

### Solutions to Circularity

#### Solution 1: Iterative Calculation (Excel Setting)

**Enable Iterative Calculation**:
- File → Options → Formulas
- Check "Enable iterative calculation"
- Set Maximum Iterations (e.g., 100)
- Set Maximum Change (e.g., 0.001)

**How It Works**:
- Excel recalculates circular formulas multiple times
- Converges to a solution
- Stops when change is below threshold or max iterations reached

**Pros**:
- Simple to implement
- No formula changes needed
- Accurate solution

**Cons**:
- Can slow down model
- May not converge if poorly designed
- Not transparent to users
- Can mask errors

#### Solution 2: Circular Switch

**Concept**: Use a switch to break circularity when needed

**Implementation**:

1. **Create Switch Cell**: 
   - Cell with 0 or 1
   - 0 = Circularity off
   - 1 = Circularity on

2. **Modify Formulas**:
   ```
   Interest Expense = IF(Circular Switch = 1, 
                         Average Debt × Interest Rate,
                         Prior Period Interest Expense)
   ```

3. **Usage**:
   - Build model with switch = 0 (no circularity)
   - Turn switch to 1 when ready
   - Enable iterative calculation

**Pros**:
- Control over circularity
- Can build model without circularity issues
- Transparent

**Cons**:
- Requires formula modifications
- More complex
- Still requires iterative calculation when on

#### Solution 3: Manual Iteration

**Concept**: Break circularity by using prior period values

**Implementation**:

```
Interest Expense = Beginning Debt × Interest Rate
```

Instead of:

```
Interest Expense = Average Debt × Interest Rate
```

**Pros**:
- No circular reference
- No iterative calculation needed
- Fast and simple

**Cons**:
- Less accurate (uses beginning instead of average)
- Timing mismatch
- May be material for large debt balances

#### Solution 4: Separate Calculation

**Concept**: Calculate interest separately, then link

**Implementation**:

1. **First Pass**: Calculate cash flow without interest
2. **Calculate Debt**: Based on first-pass cash flow
3. **Calculate Interest**: Based on debt
4. **Second Pass**: Recalculate cash flow with interest
5. **Iterate**: Repeat until convergence

**Pros**:
- No circular reference in Excel
- Full control over iteration
- Transparent

**Cons**:
- Complex to build
- Manual iteration required
- Time-consuming

### Best Practices for Circularity

**Minimize Circularity**:
- Design model to avoid when possible
- Use beginning balances instead of average when immaterial
- Simplify debt structure if possible

**Document Circularity**:
- Note where circular references exist
- Explain why necessary
- Document solution method

**Test Convergence**:
- Verify model converges to stable solution
- Check that results are reasonable
- Test with different scenarios

**Provide Instructions**:
- Explain iterative calculation settings
- Document circular switch usage
- Warn users about potential issues

---

## Model Periodicity

### Annual Models

**Use Cases**:
- DCF valuations
- LBO models
- Long-term strategic planning
- 5-10 year forecasts

**Advantages**:
- Simpler to build
- Less data required
- Faster calculation
- Easier to present

**Disadvantages**:
- Less granular
- Misses intra-year dynamics
- Timing issues
- Less useful for short-term planning

### Quarterly Models

**Use Cases**:
- Equity research
- Credit analysis
- M&A models
- Near-term forecasting

**Advantages**:
- More granular
- Captures seasonality
- Better for near-term accuracy
- Aligns with reporting

**Disadvantages**:
- More complex
- More data required
- Slower calculation
- Larger file size

### Monthly Models

**Use Cases**:
- Detailed operational planning
- Cash flow management
- Restructuring
- Project finance

**Advantages**:
- Highly granular
- Detailed cash flow tracking
- Operational insights
- Early warning signals

**Disadvantages**:
- Very complex
- Significant data requirements
- Slow calculation
- Difficult to maintain

### Hybrid Models

**Concept**: Different periodicity for different time periods

**Example**:
- Years 1-2: Monthly or quarterly
- Years 3-5: Annual
- Terminal value: Perpetuity

**Advantages**:
- Granularity where needed
- Simplicity for distant periods
- Balanced complexity

**Implementation**:
- Separate sections for different periods
- Aggregation formulas to roll up
- Careful with timing and links

---

## Model Testing and Validation

### Balance Sheet Validation

**Balance Check**:
- Assets = Liabilities + Equity
- Should be zero difference
- Flag any discrepancy

**Cash Flow Check**:
- Ending cash from CF statement = Cash on balance sheet
- Verify reconciliation

**Retained Earnings Check**:
- Beginning RE + Net Income - Dividends = Ending RE
- Verify flow from income statement

### Reasonableness Checks

**Margin Analysis**:
- Gross margin within industry range
- EBITDA margin reasonable
- Net margin consistent with business model

**Growth Rates**:
- Revenue growth achievable
- Not exceeding market growth significantly (unless justified)
- Consistent with historical performance

**Ratios**:
- Debt/EBITDA within reasonable range
- Interest coverage adequate
- Return on equity reasonable
- Working capital ratios consistent

### Scenario Testing

**Test Multiple Scenarios**:
- Base case
- Upside case
- Downside case

**Verify**:
- Model doesn't break
- Results are logical
- Relationships hold

### Sensitivity Testing

**Test Extreme Values**:
- Very high growth
- Very low growth
- High costs
- Low costs

**Check for Errors**:
- Divide by zero
- Negative values where inappropriate
- Circular reference issues
- Formula errors

### Historical Validation

**Compare to Actuals**:
- If historical data available
- Check forecast accuracy
- Understand variances
- Refine assumptions

**Benchmark**:
- Compare to industry peers
- Check if metrics are in line
- Identify outliers
- Justify differences
