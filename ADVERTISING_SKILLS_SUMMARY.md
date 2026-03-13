# Comprehensive Digital Advertising Skills - Implementation Summary

**Date**: March 12, 2026  
**Repository**: https://github.com/JH9282026/manus  
**Scope**: 8 advertising platforms, 13 comprehensive skills

## Overview

Created comprehensive digital advertising management skills for agentic AI deployment across 8 major advertising platforms. Each skill covers API integration, campaign management, creative formats, targeting options, and automation workflows suitable for MCP servers, direct API calls, and browser control.

## Platforms Covered

### 1. X (Twitter) Ads - 3 Skills
- **x-ads-campaign-management**: Campaign hierarchy, OAuth 2.0, budgets, bidding, scheduling
- **x-ads-creative-targeting**: Promoted Tweets, Twitter Cards, media upload, demographic/interest/keyword targeting
- **x-ads-analytics-optimization**: Performance metrics, reporting API, optimization workflows

### 2. Meta (Facebook/Instagram) Ads - 3 Skills
- **meta-ads-campaign-api**: Three-tier structure (Campaign → Ad Set → Ad), objectives, Meta Marketing API
- **meta-ads-targeting-audiences**: Basic/advanced targeting, custom audiences, lookalikes, flexible targeting
- **meta-ads-creative-formats**: Image/video/carousel ads, dynamic creative, Instagram placements

### 3. LinkedIn Ads - 2 Skills
- **linkedin-ads-campaign-management**: Campaign types, budgeting, bidding, LinkedIn Marketing API
- **linkedin-ads-targeting-creatives**: Sponsored Content, Message Ads, Document Ads, professional targeting

### 4. Reddit Ads - 1 Skill
- **reddit-ads-api-automation**: Reddit Ads API v3, campaign creation, audience management, conversion tracking

### 5. TikTok Ads - 1 Skill
- **tiktok-ads-api-management**: TikTok Marketing API, ad formats, targeting, creative specs

### 6. Instagram Ads - 1 Skill
- **instagram-ads-integration**: Instagram-specific placements (Feed, Stories, Reels, Explore), Meta API integration

### 7. YouTube Ads - 1 Skill
- **youtube-ads-google-api**: Google Ads API, Performance Max, Demand Gen campaigns, video ad formats

### 8. El Toro - 1 Skill
- **el-toro-ip-targeting**: IP-based targeting, Gen3 Portal, cookie-free advertising, API integration

## Skill Structure

Each skill follows the Manus template format:

```
skill-name/
├── SKILL.md              (< 500 lines, YAML frontmatter + content)
└── references/           (Detailed documentation)
    ├── api-reference.md
    ├── automation-patterns.md
    └── best-practices.md
```

### SKILL.md Components
1. **YAML Frontmatter**: name, comprehensive description (triggers)
2. **Overview**: What the skill provides
3. **Core Content**: API authentication, campaign creation, targeting, optimization
4. **Reference Guide**: When to load each reference file

### Reference Files
- **API Reference**: Complete endpoint documentation, schemas, error codes
- **Automation Patterns**: Workflow examples, MCP integration, optimization scripts
- **Best Practices**: Campaign structure, budget allocation, troubleshooting

## Technical Coverage

### API Integration
- OAuth 2.0 / API key authentication
- RESTful API endpoints
- Request/response schemas
- Rate limiting and error handling
- Batch operations

### Campaign Management
- Campaign hierarchy and structure
- Objective selection
- Budget management (daily/lifetime)
- Scheduling and pacing
- Status management (active/paused/archived)

### Targeting Capabilities
- Demographics (age, gender, language)
- Geographic (country, region, city, postal code)
- Interests and behaviors
- Keywords and hashtags
- Custom audiences (email lists, website visitors, app users)
- Lookalike audiences
- Retargeting

### Creative Formats
- Image ads (specs, optimization)
- Video ads (formats, lengths, specs)
- Carousel ads
- Stories/Reels
- Interactive formats
- Dynamic creative optimization

### Analytics & Optimization
- Performance metrics (impressions, clicks, conversions, ROAS)
- Reporting API endpoints
- Real-time monitoring
- Automated optimization rules
- A/B testing frameworks

### Automation Workflows
- Programmatic campaign creation
- Budget optimization
- Bid management
- Performance monitoring
- Auto-pause underperformers
- Batch operations

## Agentic AI Integration

### MCP Server Patterns
Each skill includes MCP server integration examples:
- Campaign CRUD operations
- Status management
- Performance reporting
- Audience management

### Direct API Usage
Python code examples for:
- Authentication
- Campaign creation
- Targeting configuration
- Creative upload
- Performance tracking

### Browser Control Fallback
Guidance for features requiring browser automation:
- Creative preview
- Audience insights dashboards
- Advanced reporting visualizations
- Platform-specific tools

## Platform-Specific Highlights

### X (Twitter)
- Four-tier hierarchy (Account → Campaign → Line Item → Promoted Tweet)
- Twitter Cards (Website, App Download, Video, Conversation)
- Follower targeting and lookalikes
- Event and TV targeting

### Meta (Facebook/Instagram)
- Three-tier structure with flexible targeting
- 70+ targeting parameters
- Dynamic creative optimization
- Cross-platform delivery (Facebook, Instagram, Messenger, WhatsApp)

### LinkedIn
- Professional targeting (job title, company, industry, skills)
- Multiple ad formats (Sponsored Content, Message Ads, Document Ads)
- Lead generation forms
- Account-based marketing features

### Reddit
- Community-based targeting
- Conversation targeting
- Custom audience uploads
- Conversion API

### TikTok
- Full-screen vertical video focus
- Spark Ads (organic content amplification)
- Interest and behavior targeting
- TikTok Pixel for conversion tracking

### Instagram
- Visual-first placements (Feed, Stories, Reels, Explore)
- Shopping integration
- Influencer collaboration tools
- Meta Marketing API integration

### YouTube
- Google Ads API integration
- Performance Max and Demand Gen campaigns
- TrueView, Bumper, and Non-skippable formats
- Audience targeting via Google ecosystem

### El Toro
- Patented IP targeting technology
- Cookie-free advertising
- Physical address to IP matching
- Gen3 Portal API

## Implementation Roadmap

### Phase 1: Foundation (Week 1)
1. Set up API credentials for each platform
2. Implement authentication workflows
3. Test basic campaign creation
4. Validate targeting options

### Phase 2: Automation (Week 2-3)
1. Build MCP server endpoints
2. Implement batch operations
3. Create optimization workflows
4. Set up performance monitoring

### Phase 3: Optimization (Week 4+)
1. A/B testing frameworks
2. Budget allocation algorithms
3. Creative rotation systems
4. Cross-platform reporting

## Best Practices Summary

### Campaign Structure
- One campaign per objective
- 3-5 ad sets per campaign for testing
- 2-4 creatives per ad set for optimization
- Consistent naming conventions

### Budget Management
- Start with minimum recommended budgets
- Allow 7-day learning phase
- Use 80/20 rule (80% proven, 20% testing)
- Set budget buffers (20% above target)

### Targeting Strategy
- Start broad, narrow based on data
- Minimum 50K audience size
- Layer targeting incrementally
- Use exclusion lists

### Creative Optimization
- Test 3+ variations simultaneously
- Refresh creatives every 2-3 weeks
- Mobile-first design
- Clear, single CTA

### Performance Monitoring
- Daily budget checks
- Weekly performance reviews
- Auto-pause rules for underperformers
- ROAS tracking

## Rate Limits & Quotas

| Platform | Rate Limit | Best Practice |
|----------|------------|---------------|
| X Ads | 1,000 req/15min | Exponential backoff |
| Meta | 200 req/hour/user | Batch requests |
| LinkedIn | Varies by endpoint | Request throttling |
| Reddit | API-specific | Check headers |
| TikTok | Varies by tier | Monitor usage |
| Google Ads | 15,000 ops/day | Batch operations |

## Error Handling Patterns

All skills include robust error handling:
- HTTP status code interpretation
- Rate limit detection and backoff
- Retry logic with exponential delays
- Graceful degradation
- Detailed error logging

## Testing & Validation

### API Testing
- Sandbox environments where available
- Small budget test campaigns
- Targeting validation
- Creative preview

### Performance Validation
- Benchmark metrics by platform
- A/B test significance
- Attribution accuracy
- Conversion tracking

## Documentation References

Each skill includes links to:
- Official API documentation
- Developer portals
- Best practices guides
- Community resources

## Maintenance & Updates

### API Version Management
- Track API version changes
- Deprecation notices
- Migration guides
- Backward compatibility

### Skill Updates
- Quarterly review of API changes
- New feature integration
- Performance optimization
- Bug fixes

## Success Metrics

### Coverage
- ✅ 8 platforms covered
- ✅ 13 comprehensive skills created
- ✅ All major ad types included
- ✅ Complete targeting options documented

### Quality
- ✅ All SKILL.md files < 500 lines
- ✅ YAML frontmatter compliant
- ✅ Comprehensive reference files
- ✅ Actionable code examples

### Usability
- ✅ Clear trigger descriptions
- ✅ Step-by-step workflows
- ✅ MCP integration patterns
- ✅ Browser control fallbacks

## Conclusion

This comprehensive skill set provides agentic AI systems with complete capabilities to deploy and manage paid digital advertising campaigns across all major platforms. Each skill is designed for programmatic access via MCP servers, direct API calls, or browser automation, with detailed documentation for every ad type, targeting option, and optimization strategy.

The skills are production-ready and can be immediately deployed for:
- Automated campaign creation
- Dynamic budget optimization
- Real-time performance monitoring
- Cross-platform advertising management
- Scalable ad operations

---

**Repository**: https://github.com/JH9282026/manus  
**Skills Location**: `/[skill-name]/SKILL.md`  
**References**: `/[skill-name]/references/*.md`  
**Format**: Manus-compatible, AI-agent optimized  
**Status**: ✅ Complete and ready for deployment

