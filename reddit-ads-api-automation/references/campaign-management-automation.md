# Reddit Ads API Campaign Management and Automation

## Campaign Management Capabilities

### Creating Campaigns
**Endpoint:** `POST /api/v3/accounts/{account_id}/campaigns`

**Request Body:**
```json
{
  "name": "Q1 2026 Brand Awareness",
  "objective": "REACH",
  "daily_budget": 10000,
  "start_date": "2026-04-01T00:00:00Z",
  "end_date": "2026-06-30T23:59:59Z",
  "status": "ACTIVE"
}
```

**Campaign Objectives:**
- `REACH` - Brand awareness
- `VIDEO_VIEWS` - Video engagement
- `TRAFFIC` - Website visits
- `CONVERSIONS` - Conversion actions
- `APP_INSTALLS` - Mobile app downloads

### Managing Ad Groups
**Endpoint:** `POST /api/v3/campaigns/{campaign_id}/ad_groups`

**Targeting Options:**
- Subreddit targeting
- Interest targeting
- Keyword targeting
- Location targeting
- Device targeting

### Creating Ads
**Endpoint:** `POST /api/v3/ad_groups/{ad_group_id}/ads`

**Ad Formats:**
- Promoted posts
- Image ads
- Video ads
- Carousel ads

## Automation Strategies

### Budget Pacing
**Monitor and adjust budgets automatically:**
```python
def adjust_campaign_budget(campaign_id, performance_data):
    if performance_data['cpa'] < target_cpa:
        increase_budget(campaign_id, multiplier=1.2)
    elif performance_data['cpa'] > target_cpa * 1.5:
        decrease_budget(campaign_id, multiplier=0.8)
```

### Bid Optimization
**Automated bidding based on performance:**
- Monitor CPC, CPM, CPA
- Adjust bids to meet targets
- Pause underperforming ad groups
- Scale high-performing campaigns

### Scheduling
**Dayparting automation:**
- Increase bids during peak hours
- Pause campaigns during low-performing times
- Adjust budgets by day of week

## Conclusion
Reddit Ads API enables comprehensive campaign automation, from creation to optimization, improving efficiency and performance.
