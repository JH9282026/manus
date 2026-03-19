# Microsoft Ads Campaign Management API Guide

## Introduction

The Microsoft Advertising Campaign Management API provides programmatic access to create, read, update, and delete advertising campaigns, ad groups, ads, keywords, and related entities. This comprehensive guide covers the core concepts, data objects, operations, and best practices for managing Microsoft Advertising campaigns through the API.

## Campaign Management Service Overview

### What is the Campaign Management Service?

The Campaign Management Service is a SOAP-based web service that enables advertisers and developers to:

- Create and manage campaigns, ad groups, and ads
- Set up and optimize keywords and bids
- Configure targeting options (location, device, audience)
- Manage ad extensions
- Implement budget and bidding strategies
- Handle negative keywords and exclusions
- Configure conversion tracking

### Service Endpoint

**Production:**
```
https://campaign.api.bingads.microsoft.com/Api/Advertiser/CampaignManagement/v13/CampaignManagementService.svc
```

**Sandbox:**
```
https://campaign.api.sandbox.bingads.microsoft.com/Api/Advertiser/CampaignManagement/v13/CampaignManagementService.svc
```

### API Version

This guide covers **Version 13** (v13), the current version as of 2026.

## Core Data Objects

### Campaign Object

The Campaign object defines a campaign within Microsoft Advertising.

#### Key Properties

**Basic Information:**
- **Id**: Unique campaign identifier (read-only after creation)
- **Name**: Campaign name (max 128 characters)
- **Status**: Active, Paused, Deleted, or BudgetPaused
- **TimeZone**: Campaign time zone (set at creation, cannot be changed)
- **CampaignType**: Search, Shopping, DynamicSearchAds, Audience, etc.

**Budget Settings:**
- **BudgetType**: DailyBudgetAccelerated, DailyBudgetStandard, or MonthlyBudgetSpendUntilDepleted
- **DailyBudget**: Daily budget amount (required for daily budget types)
- **BudgetId**: Reference to shared budget (optional)

**Bidding:**
- **BiddingScheme**: Defines bidding strategy (ManualCpc, EnhancedCpc, MaximizeConversions, TargetCpa, etc.)
- **CpcBid**: Default CPC bid (for manual bidding)

**Targeting and Settings:**
- **Languages**: Target languages (e.g., "English")
- **Settings**: Array of campaign-level settings
- **TrackingUrlTemplate**: Template for tracking URLs
- **UrlCustomParameters**: Custom parameters for tracking

**Advanced Properties:**
- **AudienceAdsBidAdjustment**: Bid adjustment for audience ads (-90 to 900)
- **MultimediaAdsBidAdjustment**: Bid adjustment for multimedia ads
- **ExperimentId**: Associated experiment ID (for campaign experiments)
- **IsDealCampaign**: Indicates if campaign is for deals
- **IsPolitical**: Indicates if campaign contains political ads

#### Campaign Types

**Search Campaigns:**
- Traditional text ads on Bing search results
- Keyword-based targeting
- Supports responsive search ads and expanded text ads

**Shopping Campaigns:**
- Product ads from merchant catalog
- Product-based targeting
- Requires product feed

**Dynamic Search Ads (DSA):**
- Automatically generated ads based on website content
- No keyword management required
- Website-based targeting

**Audience Campaigns:**
- Display and native ads on Microsoft Audience Network
- Audience-based targeting
- Image and video creatives

**Performance Max:**
- Automated campaign type
- Cross-channel optimization
- Goal-based optimization

### Ad Group Object

Ad groups contain ads and keywords, organized within campaigns.

#### Key Properties

**Basic Information:**
- **Id**: Unique ad group identifier
- **Name**: Ad group name
- **Status**: Active, Paused, or Deleted
- **CampaignId**: Parent campaign ID
- **AdGroupType**: SearchStandard, SearchDynamic, Audience, etc.

**Bidding:**
- **CpcBid**: Cost-per-click bid (inherits from campaign if not set)
- **BiddingScheme**: Inherits from campaign (cannot be set at ad group level as of April 2021)

**Targeting:**
- **Network**: Search network, syndicated search partners, or both
- **Language**: Target language (inherits from campaign)
- **AudienceAdsBidAdjustment**: Bid adjustment for audience ads

**Settings:**
- **Settings**: Ad group-level settings
- **TrackingUrlTemplate**: Tracking template
- **UrlCustomParameters**: Custom tracking parameters

**Scheduling:**
- **StartDate**: Ad group start date
- **EndDate**: Ad group end date (optional)

### Keyword Object

Keywords define the search terms that trigger ads.

#### Key Properties

**Basic Information:**
- **Id**: Unique keyword identifier
- **Text**: Keyword text (max 100 characters)
- **AdGroupId**: Parent ad group ID
- **Status**: Active, Paused, or Deleted
- **EditorialStatus**: Active, Disapproved, Inactive, or ActiveLimited

**Bidding:**
- **Bid**: Keyword-level bid (inherits from ad group if not set)
- **BiddingScheme**: Inherits from campaign (cannot be set at keyword level)

**Match Type:**
- **MatchType**: Exact, Phrase, or Broad
  - **Exact**: Keyword must match search query exactly
  - **Phrase**: Search query must contain keyword phrase in order
  - **Broad**: Search query can contain keyword terms in any order, including variations

**Tracking:**
- **DestinationUrl**: Landing page URL (legacy, use FinalUrls instead)
- **FinalUrls**: Array of final landing page URLs
- **FinalMobileUrls**: Mobile-specific landing pages
- **FinalAppUrls**: App deep link URLs
- **FinalUrlSuffix**: Suffix appended to final URL
- **TrackingUrlTemplate**: Tracking template
- **UrlCustomParameters**: Custom tracking parameters

**Dynamic Parameters:**
- **Param1**: Dynamic text substitution parameter 1
- **Param2**: Dynamic text substitution parameter 2
- **Param3**: Dynamic text substitution parameter 3

#### Match Type Strategy

**Exact Match:**
- Highest relevance, lowest volume
- Best for high-intent, specific queries
- Highest conversion rates typically
- Example: Keyword "red shoes" matches "red shoes" only

**Phrase Match:**
- Moderate relevance and volume
- Balances control and reach
- Example: Keyword "red shoes" matches "buy red shoes" or "red shoes for women"

**Broad Match:**
- Lowest relevance, highest volume
- Discovery and reach
- Requires careful negative keyword management
- Example: Keyword "red shoes" matches "crimson footwear" or "burgundy sneakers"

### Ad Objects

Multiple ad types are available, each with specific properties.

#### Responsive Search Ad (Recommended)

**Properties:**
- **Headlines**: Array of 3-15 headline options (max 30 characters each)
- **Descriptions**: Array of 2-4 description options (max 90 characters each)
- **Path1**: Optional URL path 1 (max 15 characters)
- **Path2**: Optional URL path 2 (max 15 characters)
- **FinalUrls**: Landing page URLs
- **FinalMobileUrls**: Mobile landing pages

**How It Works:**
- Microsoft automatically tests combinations
- Optimizes for best-performing combinations
- Adapts to search queries
- Improves CTR and relevance

**Best Practices:**
- Provide maximum number of headlines and descriptions
- Ensure all combinations make sense
- Include keywords in multiple headlines
- Vary messaging and calls-to-action

#### Expanded Text Ad (Legacy)

**Properties:**
- **TitlePart1**: First headline (max 30 characters)
- **TitlePart2**: Second headline (max 30 characters)
- **TitlePart3**: Third headline (max 30 characters, optional)
- **Text**: Description (max 90 characters)
- **TextPart2**: Second description (max 90 characters, optional)
- **Path1**: URL path 1
- **Path2**: URL path 2
- **FinalUrls**: Landing page URLs

**Note**: Expanded Text Ads are being phased out in favor of Responsive Search Ads.

#### Product Ad (Shopping Campaigns)

**Properties:**
- **PromotionalText**: Optional promotional text
- Automatically generated from product feed
- No manual text creation required

#### Dynamic Search Ad

**Properties:**
- **Text**: Description (max 90 characters)
- **Path1**: URL path 1
- **Path2**: URL path 2
- Headlines and URLs automatically generated from website content

## Campaign Management Operations

### Campaign Operations

#### AddCampaigns

Create new campaigns.

**Request:**
```xml
<AddCampaignsRequest>
  <AccountId>123456789</AccountId>
  <Campaigns>
    <Campaign>
      <Name>My Search Campaign</Name>
      <BudgetType>DailyBudgetStandard</BudgetType>
      <DailyBudget>50.00</DailyBudget>
      <Languages>
        <string>English</string>
      </Languages>
      <TimeZone>EasternTimeUSCanada</TimeZone>
      <CampaignType>Search</CampaignType>
      <Status>Paused</Status>
    </Campaign>
  </Campaigns>
</AddCampaignsRequest>
```

**Response:**
```xml
<AddCampaignsResponse>
  <CampaignIds>
    <long>987654321</long>
  </CampaignIds>
</AddCampaignsResponse>
```

**Python SDK Example:**
```python
from bingads.v13.campaignmanagement import Campaign

campaign = Campaign(
    Name="My Search Campaign",
    BudgetType="DailyBudgetStandard",
    DailyBudget=50.00,
    Languages=["English"],
    TimeZone="EasternTimeUSCanada",
    CampaignType="Search",
    Status="Paused"
)

response = campaign_service.AddCampaigns(
    AccountId=account_id,
    Campaigns=[campaign]
)

campaign_id = response.CampaignIds['long'][0]
```

#### GetCampaignsByAccountId

Retrieve all campaigns for an account.

**Request:**
```xml
<GetCampaignsByAccountIdRequest>
  <AccountId>123456789</AccountId>
  <CampaignType>Search Shopping</CampaignType>
  <ReturnAdditionalFields>AdScheduleUseSearcherTimeZone BidStrategyType</ReturnAdditionalFields>
</GetCampaignsByAccountIdRequest>
```

**Python SDK Example:**
```python
campaigns = campaign_service.GetCampaignsByAccountId(
    AccountId=account_id,
    CampaignType="Search Shopping",
    ReturnAdditionalFields="AdScheduleUseSearcherTimeZone BidStrategyType"
)

for campaign in campaigns['Campaign']:
    print(f"Campaign: {campaign.Name}, ID: {campaign.Id}, Status: {campaign.Status}")
```

#### UpdateCampaigns

Modify existing campaigns.

**Python SDK Example:**
```python
# First, get the campaign
campaigns = campaign_service.GetCampaignsByIds(
    AccountId=account_id,
    CampaignIds=[campaign_id]
)

campaign = campaigns['Campaign'][0]

# Modify properties
campaign.DailyBudget = 75.00
campaign.Status = "Active"

# Update
response = campaign_service.UpdateCampaigns(
    AccountId=account_id,
    Campaigns=[campaign]
)
```

#### DeleteCampaigns

Delete campaigns (sets status to Deleted).

**Python SDK Example:**
```python
response = campaign_service.DeleteCampaigns(
    AccountId=account_id,
    CampaignIds=[campaign_id]
)
```

### Ad Group Operations

#### AddAdGroups

Create ad groups within a campaign.

**Python SDK Example:**
```python
from bingads.v13.campaignmanagement import AdGroup

ad_group = AdGroup(
    Name="My Ad Group",
    CampaignId=campaign_id,
    CpcBid=1.50,
    Language="English",
    Network="OwnedAndOperatedAndSyndicatedSearch",
    Status="Paused"
)

response = campaign_service.AddAdGroups(
    CampaignId=campaign_id,
    AdGroups=[ad_group]
)

ad_group_id = response.AdGroupIds['long'][0]
```

#### GetAdGroupsByCampaignId

Retrieve ad groups for a campaign.

**Python SDK Example:**
```python
ad_groups = campaign_service.GetAdGroupsByCampaignId(
    CampaignId=campaign_id
)

for ad_group in ad_groups['AdGroup']:
    print(f"Ad Group: {ad_group.Name}, ID: {ad_group.Id}")
```

### Keyword Operations

#### AddKeywords

Add keywords to an ad group.

**Python SDK Example:**
```python
from bingads.v13.campaignmanagement import Keyword

keywords = [
    Keyword(
        Text="microsoft advertising",
        MatchType="Exact",
        Bid=2.00,
        Status="Active"
    ),
    Keyword(
        Text="bing ads",
        MatchType="Phrase",
        Bid=1.50,
        Status="Active"
    )
]

response = campaign_service.AddKeywords(
    AdGroupId=ad_group_id,
    Keywords=keywords
)

keyword_ids = response.KeywordIds['long']
```

#### GetKeywordsByAdGroupId

Retrieve keywords for an ad group.

**Python SDK Example:**
```python
keywords = campaign_service.GetKeywordsByAdGroupId(
    AdGroupId=ad_group_id
)

for keyword in keywords['Keyword']:
    print(f"Keyword: {keyword.Text}, Match Type: {keyword.MatchType}, Bid: {keyword.Bid}")
```

### Ad Operations

#### AddAds

Create ads within an ad group.

**Python SDK Example (Responsive Search Ad):**
```python
from bingads.v13.campaignmanagement import ResponsiveSearchAd, AssetLink, TextAsset

# Create headline assets
headlines = [
    AssetLink(Asset=TextAsset(Text="Microsoft Advertising")),
    AssetLink(Asset=TextAsset(Text="Bing Ads Platform")),
    AssetLink(Asset=TextAsset(Text="Reach More Customers")),
]

# Create description assets
descriptions = [
    AssetLink(Asset=TextAsset(Text="Powerful advertising platform for businesses.")),
    AssetLink(Asset=TextAsset(Text="Reach customers on Bing, Yahoo, and partner sites.")),
]

# Create responsive search ad
rsa = ResponsiveSearchAd(
    Headlines=headlines,
    Descriptions=descriptions,
    Path1="advertising",
    Path2="platform",
    FinalUrls=["https://example.com/advertising"],
    Status="Active"
)

response = campaign_service.AddAds(
    AdGroupId=ad_group_id,
    Ads=[rsa]
)

ad_id = response.AdIds['long'][0]
```

## Bidding Strategies

### Available Bidding Schemes

#### Manual CPC

**Description**: Advertiser sets bids manually at campaign, ad group, or keyword level.

**Use Cases:**
- Maximum control over bids
- Testing and learning phase
- Niche markets with specific bid requirements

**Limitations (as of May 2024):**
- Restricted to audience display and video campaigns
- Restricted to lodging campaigns
- No longer available for audience native campaigns (auto-converted to Enhanced CPC)

**Python SDK Example:**
```python
from bingads.v13.campaignmanagement import ManualCpcBiddingScheme

campaign.BiddingScheme = ManualCpcBiddingScheme()
```

#### Enhanced CPC (eCPC)

**Description**: Microsoft automatically adjusts manual bids up or down based on conversion likelihood.

**How It Works:**
- Increases bids for searches more likely to convert
- Decreases bids for searches less likely to convert
- Stays close to manual bid on average

**Use Cases:**
- Balancing control with automation
- Improving conversion rates
- Transitioning from manual to automated bidding

**Python SDK Example:**
```python
from bingads.v13.campaignmanagement import EnhancedCpcBiddingScheme

campaign.BiddingScheme = EnhancedCpcBiddingScheme()
```

#### Maximize Clicks

**Description**: Automatically sets bids to get the most clicks within budget.

**Use Cases:**
- Traffic generation
- Brand awareness
- Content promotion

**Considerations:**
- May not optimize for conversion quality
- Best for top-of-funnel campaigns

#### Maximize Conversions

**Description**: Automatically sets bids to get the most conversions within budget.

**Requirements:**
- Conversion tracking implemented
- Sufficient conversion history

**Use Cases:**
- Lead generation
- E-commerce sales
- Conversion-focused campaigns

**Python SDK Example:**
```python
from bingads.v13.campaignmanagement import MaximizeConversionsBiddingScheme

campaign.BiddingScheme = MaximizeConversionsBiddingScheme()
```

#### Target CPA (Cost Per Acquisition)

**Description**: Automatically sets bids to achieve a target cost per conversion.

**Requirements:**
- At least 15 conversions in last 30 days
- Conversion tracking implemented

**Use Cases:**
- Maintaining specific CPA goals
- Scaling while controlling costs
- Performance-based campaigns

**Python SDK Example:**
```python
from bingads.v13.campaignmanagement import TargetCpaBiddingScheme

campaign.BiddingScheme = TargetCpaBiddingScheme(
    TargetCpa=25.00  # Target $25 per conversion
)
```

#### Target ROAS (Return on Ad Spend)

**Description**: Automatically sets bids to achieve a target return on ad spend.

**Requirements:**
- Conversion value tracking
- Sufficient conversion history with values

**Use Cases:**
- E-commerce with varying product values
- Optimizing for revenue, not just conversions
- Profitability-focused campaigns

**Python SDK Example:**
```python
from bingads.v13.campaignmanagement import TargetRoasBiddingScheme

campaign.BiddingScheme = TargetRoasBiddingScheme(
    TargetRoas=4.0  # Target 4:1 return (400%)
)
```

### Bidding Strategy Best Practices

**Campaign-Level Only (Since April 2021):**
- Bid strategies can only be set at campaign level
- Ad groups and keywords inherit campaign's bid strategy
- Attempting to set bid strategy at ad group or keyword level will be ignored

**Choosing the Right Strategy:**
1. **Start with Manual CPC or Enhanced CPC** for new campaigns
2. **Gather conversion data** (at least 15-30 conversions)
3. **Test automated strategies** (Maximize Conversions, Target CPA)
4. **Monitor performance** for 2-4 weeks
5. **Optimize targets** based on results

**Conversion Requirements:**
- Automated bidding requires conversion tracking
- Minimum 15 conversions in 30 days for Target CPA
- More data = better optimization

## Budget Management

### Budget Types

**Daily Budget Standard:**
- Spreads budget evenly throughout the day
- May spend up to 2x daily budget on high-traffic days
- Monthly spend won't exceed daily budget × days in month

**Daily Budget Accelerated:**
- Spends budget as quickly as possible
- Ads shown until budget depleted
- May exhaust budget early in the day

**Monthly Budget Spend Until Depleted:**
- Monthly budget cap
- Spends until monthly budget exhausted
- No daily pacing

### Shared Budgets

Multiple campaigns can share a single budget.

**Benefits:**
- Simplified budget management
- Automatic allocation across campaigns
- Prevents over-spending

**Python SDK Example:**
```python
from bingads.v13.campaignmanagement import Budget

# Create shared budget
budget = Budget(
    Amount=500.00,
    BudgetType="DailyBudgetStandard",
    Name="Shared Search Budget"
)

response = campaign_service.AddBudgets([budget])
budget_id = response.BudgetIds['long'][0]

# Assign to campaign
campaign.BudgetId = budget_id
campaign.BudgetType = None  # Must be None when using shared budget
```

## Negative Keywords

Negative keywords prevent ads from showing for specific search terms.

### Negative Keyword Levels

**Campaign-Level Negative Keywords:**
- Apply to all ad groups in campaign
- Broad reach for exclusions

**Ad Group-Level Negative Keywords:**
- Apply only to specific ad group
- Granular control

**Shared Negative Keyword Lists:**
- Reusable across multiple campaigns
- Centralized management

### Adding Negative Keywords

**Python SDK Example:**
```python
from bingads.v13.campaignmanagement import NegativeKeyword

negative_keywords = [
    NegativeKeyword(
        Text="free",
        MatchType="Broad"
    ),
    NegativeKeyword(
        Text="cheap",
        MatchType="Broad"
    )
]

response = campaign_service.AddNegativeKeywordsToEntities(
    EntityNegativeKeywords=[
        {
            'EntityId': campaign_id,
            'EntityType': 'Campaign',
            'NegativeKeywords': negative_keywords
        }
    ]
)
```

## Best Practices

### Campaign Structure

1. **Organize by theme**: Group related keywords and ads
2. **Separate brand and non-brand**: Different strategies and budgets
3. **Use single keyword ad groups (SKAGs)**: Maximum relevance and control
4. **Limit ad groups per campaign**: 7-10 for manageability
5. **Separate match types**: Test performance by match type

### Keyword Management

1. **Start with exact and phrase match**: Higher relevance
2. **Add broad match gradually**: Discovery and reach
3. **Use negative keywords aggressively**: Prevent wasted spend
4. **Monitor search terms report**: Identify new keywords and negatives
5. **Maintain keyword-ad relevance**: Include keywords in ad copy

### Ad Copy Optimization

1. **Use responsive search ads**: Better performance through automation
2. **Include keywords in headlines**: Improves relevance and CTR
3. **Clear call-to-action**: Tell users what to do
4. **Highlight unique value**: Differentiate from competitors
5. **Test multiple variations**: Continuous improvement

### Bidding Optimization

1. **Start conservative**: Lower bids initially, increase based on performance
2. **Use bid adjustments**: Device, location, time-of-day
3. **Monitor and adjust regularly**: Weekly reviews minimum
4. **Leverage automated bidding**: When sufficient conversion data available
5. **Set appropriate targets**: Realistic CPA or ROAS goals

## Conclusion

The Microsoft Ads Campaign Management API provides comprehensive programmatic control over advertising campaigns. Understanding the core data objects (campaigns, ad groups, keywords, ads), available operations, and bidding strategies enables effective automation and optimization. By following best practices for campaign structure, keyword management, and bidding, advertisers can maximize performance and ROI through API-driven campaign management. The shift to campaign-level bidding strategies and the emphasis on automated bidding reflect Microsoft's focus on machine learning-driven optimization, requiring advertisers to provide quality conversion data and trust the algorithms for best results.
