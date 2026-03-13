# Meta Targeting Reference

Complete catalog of Meta advertising targeting options.

---

## Demographics

### Age
- Minimum: 13
- Maximum: 65+
- Granularity: Single year or ranges

### Gender
- All (default)
- Male (1)
- Female (2)

### Relationship Status
- Single (1)
- In a relationship (2)
- Married (3)
- Engaged (4)

### Education Level
- High school (1)
- In college (2)
- College grad (3)
- In grad school (4)
- Master's degree (5)
- Professional degree (6)
- Doctorate degree (7)
- Unspecified (8)

### Education Schools
- Target specific universities
- Search by school name
- Includes alumni and current students

### Work
- **Employers**: Target by company name
- **Job Titles**: Specific roles
- **Industries**: Broad categories
- **Office Type**: Small business, large corporation

### Parents
- All parents
- Parents with toddlers (1-2 years)
- Parents with preschoolers (3-5 years)
- Parents with early school age (6-8 years)
- Parents with preteens (8-12 years)
- Parents with teenagers (13-18 years)

### Life Events
- Away from hometown
- Away from family
- Long-distance relationship
- New job
- New relationship
- Newly engaged (3 months)
- Newly engaged (6 months)
- Newly engaged (1 year)
- Newlywed (3 months)
- Newlywed (6 months)
- Newlywed (1 year)
- Recently moved
- Upcoming birthday

---

## Location Targeting

### Location Types
- **Home**: People whose home is in location
- **Recent**: People recently in location
- **Travel**: People traveling in location

### Geographic Units
- Countries (250+)
- States/Regions
- Cities
- ZIP/Postal codes
- DMA (Designated Market Area)
- Congressional districts
- Radius targeting (10-50 miles)

---

## Interests

### Top Categories

**Business and Industry**
- Business (6003349313498)
- Entrepreneurship (6003348604498)
- Marketing (6003348834498)
- Sales (6003348844498)

**Entertainment**
- Movies (6003139266461)
- Television (6003020834693)
- Music (6003139266461)
- Gaming (6003348604498)

**Family and Relationships**
- Family (6003348604498)
- Parenting (6003348604498)
- Dating (6003348604498)

**Fitness and Wellness**
- Physical fitness (6003107902433)
- Yoga (6003020834693)
- Running (6003139266461)
- Weight training (6003348604498)

**Food and Drink**
- Cooking (6003139266461)
- Restaurants (6003348604498)
- Wine (6003020834693)
- Coffee (6003348604498)

**Hobbies and Activities**
- Photography (6003139266461)
- Arts and crafts (6003348604498)
- Gardening (6003020834693)
- DIY (6003348604498)

**Shopping and Fashion**
- Shopping (6003139266461)
- Fashion (6003348604498)
- Beauty (6003020834693)
- Luxury goods (6003348604498)

**Sports and Outdoors**
- Sports (6003139266461)
- Outdoor recreation (6003348604498)
- Travel (6003020834693)

**Technology**
- Technology (6003139266461)
- Consumer electronics (6003348604498)
- Computers (6003020834693)
- Mobile devices (6003348604498)

---

## Behaviors

### Digital Activities
- Facebook page admins
- Technology early adopters
- Engaged shoppers
- Online spending methods
- Browser used

### Mobile Device User
- All mobile devices
- Android devices
- iOS devices
- Tablets
- Specific device models

### Purchase Behavior
- Engaged shoppers
- Online shoppers
- Purchase behavior (by category)
- Spending methods

### Travel
- Frequent travelers (6002714895372)
- Commuters (6015559470583)
- Currently traveling
- Returned from trip 1 week ago
- International travelers

### Expats
- By country of origin
- Living in specific countries

### Seasonal and Events
- Seasonal buyers
- Event attendees
- Anniversary within 30 days
- Birthday within 7-30 days

---

## Connections

### Page Connections
- People who like your Page
- Friends of people who like your Page
- Exclude people who like your Page

### App Connections
- People who used your app
- Friends of people who used your app
- Exclude people who used your app

### Event Connections
- People who responded to your event
- Exclude people who responded

---

## Custom Audiences

### Customer File
- Email addresses
- Phone numbers
- Mobile Advertiser IDs
- Facebook User IDs
- Instagram User IDs
- First/Last name + location

### Website Traffic
- All website visitors
- Specific pages
- Time on site
- Frequency
- Device type

### App Activity
- All app users
- Specific events
- Time spent
- Purchase value

### Engagement
- Video (3s, 10s, 25%, 50%, 75%, 95%, 100%)
- Lead form
- Instant Experience
- Instagram profile
- Instagram business profile
- Facebook Page
- Event

### Offline Activity
- Store visits
- Phone calls
- In-store purchases

---

## Lookalike Audiences

### Similarity Percentage
- 1% (most similar, smallest)
- 2-10% (broader, less similar)
- Up to 20% in some countries

### Source Requirements
- Minimum 100 people from single country
- Recommended 1,000-50,000 for best results

### Types
- Similarity lookalike (default)
- Value-based lookalike (requires LTV data)
- Multi-country lookalike

---

## Detailed Targeting Expansion

### Expansion Options
- **Off**: Use exact targeting only
- **On**: Meta can expand beyond defined audience
- **Advantage+ Audience**: Full AI optimization

### When Expansion Helps
- Small audience size (<1M)
- Conversion optimization
- Proven campaign performance

---

## Audience Size Guidelines

| Size | Reach | Recommendation |
|------|-------|----------------|
| <1,000 | Too small | Expand targeting |
| 1,000-10,000 | Very specific | Good for retargeting |
| 10,000-100,000 | Specific | Good for niche products |
| 100,000-1M | Moderate | Balanced |
| 1M-10M | Broad | Good for awareness |
| 10M+ | Very broad | Use with strong creative |

---

## Targeting Combinations

### AND Logic (Narrow)
```json
{
  "flexible_spec": [
    {
      "interests": [{"id": "6003139266461"}],
      "behaviors": [{"id": "6002714895372"}]
    }
  ]
}
```
User must match ALL criteria in the object.

### OR Logic (Broad)
```json
{
  "flexible_spec": [
    {"interests": [{"id": "6003139266461"}]},
    {"interests": [{"id": "6003348604498"}]}
  ]
}
```
User can match ANY object.

### Exclusions
```json
{
  "interests": [{"id": "6003139266461"}],
  "excluded_custom_audiences": [{"id": "123456789"}]
}
```
