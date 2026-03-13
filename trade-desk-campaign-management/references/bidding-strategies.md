# The Trade Desk Bidding Strategies

RTB bidding and optimization strategies.

## Real-Time Bidding (RTB)

### How RTB Works
1. User visits website
2. Ad impression becomes available
3. TTD evaluates impression in milliseconds
4. Bid placed based on criteria
5. Highest bid wins impression
6. Ad served to user

### Bid Evaluation Factors
- User demographics
- Browsing history
- Device type
- Geographic location
- Time of day
- Publisher quality
- Viewability likelihood

## Koa AI Optimization

### What is Koa
- The Trade Desk's AI engine
- Optimizes bidding, targeting, placements
- Real-time budget reallocation
- Cross-channel optimization

### How Koa Works
- Analyzes performance signals
- Predicts conversion likelihood
- Adjusts bids dynamically
- Reallocates budget to best-performing channels
- Learns from campaign data

### Koa Best Practices
- Provide seed audience for better learning
- Allow 1-2 weeks for learning phase
- Set clear KPIs
- Use conversion tracking
- Don't make frequent manual changes during learning

## Custom Algorithmic Bidding

### Proprietary Bid Logic
- Incorporate custom data signals
- Customer lifetime value (CLV)
- Seasonal trends
- Business-specific factors

### Bid Adjustments
- Increase bids for high-value impressions
- Decrease bids for low-performing inventory
- Time-based bid adjustments
- Device-based bid modifiers

## Bid Factors in Kokai

### Setting Bid Factors
- Assign higher factors to valuable impressions
- Lower factors to underperforming inventory
- Guide Koa's AI optimization

**Example:**
- Premium website: Bid factor 1.5x
- Mobile app: Bid factor 1.2x
- Low-performing site: Bid factor 0.7x

## AutoAllocator

### What is AutoAllocator
- Automatic budget distribution
- Allocates funds based on performance
- Ensures maximum budget utilization
- Prevents overspending

### When to Use
- Multiple ad groups in campaign
- Want automatic optimization
- Trust algorithmic allocation

### When to Disable
- Need manual budget control
- Testing specific ad groups
- Non-guaranteed campaigns with specific allocation needs

## Bidding Best Practices

- Start with moderate bids, adjust based on performance
- Use Koa AI for optimization
- Set bid factors for known high/low performers
- Monitor bid landscape and competition
- Don't engage in bidding wars
- Focus on efficiency (CPA, ROAS) not just volume
- Allow learning phase before major changes
- Use AutoAllocator for multi-ad-group campaigns
- Implement frequency caps to avoid overbidding
- Leverage first-party data for better bid decisions
