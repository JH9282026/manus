# Social Media Data Collection: Tools, APIs, and Best Practices

A comprehensive guide to collecting social media data for research, including platform APIs, third-party tools, and ethical considerations.

## Understanding Social Media Data

### Types of Social Media Data

**1. Content Data**:
- **Posts/Tweets**: Text, images, videos, links
- **Comments**: Replies, threaded discussions
- **Stories**: Ephemeral content (Instagram/Snapchat Stories)
- **Live Streams**: Real-time video content

**2. Engagement Data**:
- **Reactions**: Likes, loves, angry, sad (Facebook)
- **Shares**: Retweets, shares, reposts
- **Comments**: User responses and discussions
- **Saves/Bookmarks**: Content saved for later

**3. User Data**:
- **Profile Information**: Bio, location, website, profile picture
- **Follower/Following**: Network connections
- **Verification Status**: Verified accounts, badges
- **Account Age**: Creation date, activity history

**4. Metadata**:
- **Timestamps**: Post date/time, timezone
- **Location**: Geotags, check-ins
- **Device**: Platform used (iOS, Android, web)
- **Language**: Detected or declared language

**5. Network Data**:
- **Relationships**: Follows, friends, connections
- **Interactions**: Mentions, tags, replies
- **Communities**: Groups, subreddits, hashtag communities

### Data Access Levels

**Public Data**:
- Publicly visible posts and profiles
- Generally accessible for research (check platform ToS)
- Examples: Public tweets, Instagram posts from public accounts

**Private Data**:
- Protected accounts, private groups
- Requires user consent or special access
- Examples: Private Facebook groups, protected Twitter accounts

**Platform-Restricted Data**:
- Data available only through official APIs
- Subject to rate limits and access tiers
- Examples: Engagement metrics, historical data

**Proprietary Data**:
- Data not publicly available
- Requires partnership or purchase
- Examples: Detailed demographics, ad performance data

## Platform APIs

### Twitter/X API

**Overview**:
Twitter's API provides access to tweets, user profiles, trends, and more. As of 2026, Twitter (now X) has restructured its API access.

**Access Tiers**:

| Tier | Cost | Rate Limits | Features |
|------|------|-------------|----------|
| **Free** | $0 | Very limited (1,500 tweets/month) | Basic read access |
| **Basic** | $100/month | 10,000 tweets/month | Read tweets, user data |
| **Pro** | $5,000/month | 1M tweets/month | Advanced search, historical data |
| **Enterprise** | Custom pricing | Custom limits | Full access, dedicated support |
| **Academic Research** | Free (approved institutions) | 10M tweets/month | Full archive access, research-focused |

**Key Endpoints**:

**1. Search Tweets**:
- Endpoint: `GET /2/tweets/search/recent`
- Purpose: Search recent tweets (last 7 days)
- Parameters: `query`, `max_results`, `start_time`, `end_time`

**2. User Timeline**:
- Endpoint: `GET /2/users/:id/tweets`
- Purpose: Get tweets from specific user
- Parameters: `max_results`, `start_time`, `end_time`

**3. User Lookup**:
- Endpoint: `GET /2/users/:id`
- Purpose: Get user profile information
- Returns: Username, bio, follower count, location

**4. Followers/Following**:
- Endpoint: `GET /2/users/:id/followers`
- Purpose: Get user's followers or following list
- Rate Limited: Yes

**Example (Python with Tweepy)**:

```python
import tweepy

# Authenticate
client = tweepy.Client(bearer_token="YOUR_BEARER_TOKEN")

# Search recent tweets
query = "climate change -is:retweet lang:en"
tweets = client.search_recent_tweets(query=query, max_results=100, 
                                      tweet_fields=['created_at', 'public_metrics', 'author_id'])

# Process tweets
for tweet in tweets.data:
    print(f"{tweet.created_at}: {tweet.text}")
    print(f"Likes: {tweet.public_metrics['like_count']}, Retweets: {tweet.public_metrics['retweet_count']}")
```

**Limitations**:
- **Historical Data**: Free/Basic tiers limited to last 7 days; Pro/Enterprise/Academic access full archive
- **Rate Limits**: Strict limits on requests per 15-minute window
- **NSFW Content**: Blocked from third-party apps (as of 2023)
- **Cost**: Significant cost for high-volume research

**Best Practices**:
- Use Academic Research tier if eligible (free, high limits)
- Implement rate limit handling (wait when limit reached)
- Use precise queries to reduce unnecessary data collection
- Store tweet IDs, not full tweets, for sharing (hydration required)

### Reddit API

**Overview**:
Reddit's API provides access to posts, comments, subreddits, and user data.

**Access**:
- **Free**: OAuth2 authentication required
- **Rate Limits**: 60 requests/minute (OAuth), 100 requests/10 minutes (unauthenticated)
- **Registration**: Create app at https://www.reddit.com/prefs/apps

**Key Endpoints**:

**1. Subreddit Posts**:
- Endpoint: `GET /r/{subreddit}/new` (or `/hot`, `/top`)
- Purpose: Get posts from subreddit
- Parameters: `limit`, `after` (pagination)

**2. Post Comments**:
- Endpoint: `GET /r/{subreddit}/comments/{post_id}`
- Purpose: Get comments on specific post
- Returns: Nested comment tree

**3. User Profile**:
- Endpoint: `GET /user/{username}/about`
- Purpose: Get user information
- Returns: Karma, account age, profile

**4. Search**:
- Endpoint: `GET /r/{subreddit}/search`
- Purpose: Search posts within subreddit
- Parameters: `q` (query), `sort`, `time`

**Example (Python with PRAW)**:

```python
import praw

# Authenticate
reddit = praw.Reddit(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    user_agent="research_bot/1.0"
)

# Get posts from subreddit
subreddit = reddit.subreddit("technology")
for post in subreddit.hot(limit=100):
    print(f"{post.title} - Score: {post.score}")
    print(f"Comments: {post.num_comments}")
    
    # Get comments
    post.comments.replace_more(limit=0)  # Flatten comment tree
    for comment in post.comments.list()[:10]:  # First 10 comments
        print(f"  - {comment.body[:100]}")
```

**Limitations**:
- **1,000-Post Wall**: API caps at ~1,000 most recent posts per listing (cannot access older posts via standard endpoints)
- **No Date Filtering**: Cannot request posts from specific date range
- **NSFW Block**: NSFW content blocked from third-party apps (as of 2023)
- **Rate Limits**: 60 requests/minute (can be restrictive for large-scale collection)

**Workarounds**:
- **Pushshift Archive**: Historical Reddit data (posts and comments) available via Pushshift API or data dumps
- **Multiple Sorts**: Combine `/new`, `/top`, `/controversial` to get more diverse posts
- **Third-Party APIs**: Services like Data365 offer enhanced Reddit data access

**Best Practices**:
- Use PRAW library (Python Reddit API Wrapper) for easier implementation
- Respect rate limits (PRAW handles this automatically)
- Use Pushshift for historical data (posts older than ~1,000 most recent)
- Be aware of NSFW content restrictions

### Instagram API

**Overview**:
Instagram's API access is highly restricted, primarily for business accounts and approved partners.

**Access Options**:

**1. Instagram Graph API** (for Business/Creator accounts):
- **Purpose**: Manage business accounts, publish content, get insights
- **Access**: Requires Facebook Developer account and app approval
- **Limitations**: Only works with accounts you own or manage

**2. Instagram Basic Display API**:
- **Purpose**: Get user's own profile, photos, videos
- **Access**: OAuth authentication
- **Limitations**: Only user's own content, no public data access

**3. Third-Party Tools**:
- **Purpose**: Public data scraping (within ToS)
- **Examples**: Brandwatch, Sprinklr, Meltwater
- **Limitations**: Limited by Instagram's anti-scraping measures

**Key Endpoints (Graph API)**:

**1. User Insights**:
- Endpoint: `GET /{ig-user-id}/insights`
- Purpose: Get account insights (impressions, reach, engagement)
- Requires: Business account ownership

**2. Media**:
- Endpoint: `GET /{ig-user-id}/media`
- Purpose: Get user's posts
- Returns: Media ID, caption, timestamp, media type

**3. Media Insights**:
- Endpoint: `GET /{ig-media-id}/insights`
- Purpose: Get post-level insights (likes, comments, saves)
- Requires: Business account ownership

**Example (Python with Facebook SDK)**:

```python
from facebook import GraphAPI

# Authenticate
access_token = "YOUR_ACCESS_TOKEN"
graph = GraphAPI(access_token=access_token)

# Get user's media
user_id = "YOUR_IG_USER_ID"
media = graph.get_object(f"{user_id}/media", fields="id,caption,timestamp,like_count,comments_count")

for post in media['data']:
    print(f"{post['timestamp']}: {post['caption'][:50]}")
    print(f"Likes: {post.get('like_count', 'N/A')}, Comments: {post.get('comments_count', 'N/A')}")
```

**Limitations**:
- **No Public Data Access**: Cannot access public posts from accounts you don't own
- **Business Accounts Only**: Most features require business/creator account
- **Approval Required**: App review process for API access
- **Rate Limits**: Strict limits on API calls

**Alternatives**:
- **Manual Collection**: Screenshot and manual data entry (small-scale)
- **Third-Party Tools**: Social listening platforms with Instagram access
- **Influencer Platforms**: Tools like CreatorIQ, Traackr provide influencer data

### Facebook API

**Overview**:
Facebook's API access is restricted, especially after Cambridge Analytica scandal.

**Access Options**:

**1. Graph API** (for Pages you manage):
- **Purpose**: Manage Facebook Pages, get insights
- **Access**: Requires Facebook Developer account
- **Limitations**: Only Pages you own/manage

**2. CrowdTangle** (Meta-owned):
- **Purpose**: Track public content from Pages, Groups, verified profiles
- **Access**: Request access (approval required)
- **Limitations**: Public content only, no personal profiles

**Key Endpoints (Graph API)**:

**1. Page Posts**:
- Endpoint: `GET /{page-id}/posts`
- Purpose: Get posts from Page you manage
- Returns: Post content, engagement metrics

**2. Page Insights**:
- Endpoint: `GET /{page-id}/insights`
- Purpose: Get Page-level insights (reach, engagement, demographics)
- Requires: Page ownership

**Example (CrowdTangle)**:

CrowdTangle provides dashboard and API for tracking public Facebook content.

- **Dashboard**: Web interface for searching and monitoring
- **API**: Programmatic access to public posts
- **Access**: Request at https://crowdtangle.com/

**Limitations**:
- **No Personal Profiles**: Cannot access personal profile data
- **Public Content Only**: Only public posts from Pages, Groups, verified profiles
- **Approval Required**: CrowdTangle access requires approval
- **Restricted Groups**: Limited access to Group data

### LinkedIn API

**Overview**:
LinkedIn's API is highly restricted, primarily for partners and enterprise clients.

**Access**:
- **Limited Public Access**: Very restricted
- **Partner Program**: Requires partnership with LinkedIn
- **Enterprise Solutions**: Sales Navigator, LinkedIn Talent Solutions (paid)

**Limitations**:
- **No Public Data Access**: Cannot scrape or access public profiles via API
- **Anti-Scraping**: LinkedIn actively blocks scraping attempts
- **Legal Risk**: Scraping violates ToS and has led to lawsuits

**Alternatives**:
- **Manual Research**: Manual profile review (small-scale)
- **LinkedIn Sales Navigator**: Paid tool for lead research
- **Third-Party Tools**: Some social listening tools have limited LinkedIn access

### TikTok API

**Overview**:
TikTok's API access is limited, with research-specific access available.

**Access Options**:

**1. TikTok Research API**:
- **Purpose**: Academic and non-profit research
- **Access**: Application required, institutional affiliation
- **Features**: Access to public videos, user data, hashtags

**2. TikTok for Developers**:
- **Purpose**: App integration (login, share)
- **Limitations**: No data access for research

**Key Features (Research API)**:
- Search videos by keyword, hashtag, username
- Get video metadata (views, likes, shares, comments)
- User profile information
- Hashtag and sound data

**Limitations**:
- **Approval Required**: Must apply and be approved
- **Research Use Only**: Cannot be used for commercial purposes
- **Rate Limits**: Limits on requests

**Alternatives**:
- **Third-Party Tools**: Social listening platforms with TikTok access
- **Manual Collection**: Small-scale manual data collection

### YouTube API

**Overview**:
YouTube Data API provides access to videos, channels, comments, and more.

**Access**:
- **Free**: Google Cloud account required
- **Quota**: 10,000 units/day (free tier)
- **Cost**: Additional quota can be purchased

**Key Endpoints**:

**1. Search**:
- Endpoint: `GET /youtube/v3/search`
- Purpose: Search videos, channels, playlists
- Parameters: `q` (query), `type`, `order`, `publishedAfter`

**2. Video Details**:
- Endpoint: `GET /youtube/v3/videos`
- Purpose: Get video metadata (title, description, views, likes)
- Parameters: `id`, `part` (snippet, statistics, contentDetails)

**3. Comments**:
- Endpoint: `GET /youtube/v3/commentThreads`
- Purpose: Get comments on video
- Parameters: `videoId`, `maxResults`, `order`

**4. Channel Details**:
- Endpoint: `GET /youtube/v3/channels`
- Purpose: Get channel information (subscribers, views)
- Parameters: `id`, `part`

**Example (Python with Google API Client)**:

```python
from googleapiclient.discovery import build

# Authenticate
api_key = "YOUR_API_KEY"
youtube = build('youtube', 'v3', developerKey=api_key)

# Search videos
request = youtube.search().list(
    q="climate change",
    type="video",
    part="id,snippet",
    maxResults=50
)
response = request.execute()

for item in response['items']:
    video_id = item['id']['videoId']
    title = item['snippet']['title']
    print(f"{title} - https://youtube.com/watch?v={video_id}")
    
    # Get video statistics
    video_request = youtube.videos().list(
        id=video_id,
        part="statistics"
    )
    video_response = video_request.execute()
    stats = video_response['items'][0]['statistics']
    print(f"Views: {stats['viewCount']}, Likes: {stats.get('likeCount', 'N/A')}")
```

**Quota Costs**:
- Search: 100 units per request
- Video details: 1 unit per request
- Comments: 1 unit per request
- Daily quota: 10,000 units (free)

**Best Practices**:
- Minimize search requests (expensive in quota)
- Batch video detail requests (up to 50 videos per request)
- Cache results to avoid redundant API calls
- Request additional quota if needed (paid)

## Third-Party Data Collection Tools

### Social Listening Platforms

**Enterprise Platforms**:

**1. Brandwatch**:
- **Features**: Multi-platform monitoring, sentiment analysis, influencer identification
- **Platforms**: Twitter, Facebook, Instagram, Reddit, YouTube, news, blogs, forums
- **Pricing**: $1,000-5,000+/month (enterprise)
- **Best For**: Large-scale brand monitoring, competitive intelligence

**2. Sprinklr**:
- **Features**: Social listening, engagement, analytics, AI-powered insights
- **Platforms**: 30+ social channels
- **Pricing**: Custom (enterprise)
- **Best For**: Enterprise social media management and research

**3. Meltwater**:
- **Features**: Media monitoring, social listening, influencer tracking
- **Platforms**: Social media, news, broadcast, print
- **Pricing**: Custom (enterprise)
- **Best For**: PR and media monitoring with social integration

**4. Talkwalker**:
- **Features**: Social listening, image recognition, trend detection
- **Platforms**: 150+ million sources
- **Pricing**: Custom (enterprise)
- **Best For**: Visual social listening, brand monitoring

**Mid-Market Platforms**:

**1. Hootsuite Insights** (powered by Brandwatch):
- **Features**: Social listening, sentiment analysis
- **Platforms**: Major social networks
- **Pricing**: $500-2,000/month
- **Best For**: Mid-sized businesses, integrated with Hootsuite management

**2. Mention**:
- **Features**: Brand monitoring, sentiment analysis, influencer tracking
- **Platforms**: Social media, web, news
- **Pricing**: $25-300/month
- **Best For**: Small to mid-sized businesses, affordable monitoring

**3. Brand24**:
- **Features**: Social media monitoring, sentiment analysis, reporting
- **Platforms**: Social media, web, news, blogs
- **Pricing**: $49-249/month
- **Best For**: Small businesses, budget-conscious monitoring

### Academic and Research Tools

**1. Netlytic**:
- **Features**: Text mining, network visualization, sentiment analysis
- **Platforms**: Twitter, YouTube, Reddit, Instagram
- **Pricing**: Free (limited), $9-99/month
- **Best For**: Academic research, network analysis

**2. NodeXL**:
- **Features**: Social network analysis, visualization (Excel add-in)
- **Platforms**: Twitter, Facebook, YouTube, Flickr
- **Pricing**: Free (basic), $600/year (Pro)
- **Best For**: Network analysis, academic research

**3. 4CAT**:
- **Features**: Multi-platform data collection and analysis
- **Platforms**: Twitter, Reddit, 4chan, Instagram, TikTok, Telegram
- **Pricing**: Free (open-source)
- **Best For**: Academic research, digital methods

**4. TAGS (Twitter Archiving Google Sheets)**:
- **Features**: Collect tweets into Google Sheets
- **Platforms**: Twitter
- **Pricing**: Free
- **Best For**: Simple Twitter data collection, small-scale research

### Influencer Research Platforms

**1. CreatorIQ**:
- **Features**: Influencer discovery, analytics, campaign management
- **Platforms**: Instagram, YouTube, TikTok, Twitter
- **Pricing**: Custom (enterprise)
- **Best For**: Influencer marketing campaigns

**2. Traackr**:
- **Features**: Influencer discovery, relationship management, performance tracking
- **Platforms**: Instagram, YouTube, Twitter, Facebook, blogs
- **Pricing**: Custom (enterprise)
- **Best For**: Influencer relationship management

**3. Upfluence**:
- **Features**: Influencer search, analytics, campaign management
- **Platforms**: Instagram, YouTube, TikTok, Twitter, Pinterest, blogs
- **Pricing**: $500-2,000+/month
- **Best For**: E-commerce influencer marketing

**4. HypeAuditor**:
- **Features**: Influencer analytics, audience quality, fraud detection
- **Platforms**: Instagram, YouTube, TikTok, Twitter
- **Pricing**: $299-999/month
- **Best For**: Influencer vetting, audience authenticity

## Data Collection Best Practices

### Ethical Data Collection

**1. Respect Privacy**:
- Only collect publicly available data
- Do not attempt to access private accounts or content
- Anonymize data when reporting findings
- Do not attempt to identify individuals from pseudonymous accounts

**2. Comply with Terms of Service**:
- Read and follow platform ToS
- Respect rate limits and access restrictions
- Do not use unauthorized scraping methods
- Attribute data sources appropriately

**3. Obtain Consent When Required**:
- For private data or direct quotes, obtain consent
- For research involving human subjects, follow IRB protocols
- Disclose research purpose when contacting users

**4. Data Security**:
- Store data securely (encryption, access controls)
- Limit access to authorized personnel
- Delete data when no longer needed
- Comply with data protection regulations (GDPR, CCPA)

### Legal and Regulatory Compliance

**GDPR (Europe)**:
- **Applies to**: EU residents' data
- **Requirements**: Lawful basis, data minimization, right to erasure, transparency
- **Penalties**: Up to 4% of global revenue or €20 million

**CCPA (California)**:
- **Applies to**: California residents' data
- **Requirements**: Right to know, right to delete, right to opt out
- **Penalties**: $2,500-7,500 per violation

**Platform Terms of Service**:
- **Violation Consequences**: API access revoked, legal action
- **Key Restrictions**: No scraping, respect rate limits, no data sale

**Research Ethics (IRB)**:
- **When Required**: Research involving human subjects at academic institutions
- **Process**: Submit research protocol for IRB review and approval
- **Considerations**: Informed consent, risk assessment, data protection

### Technical Best Practices

**1. Rate Limit Handling**:
- Respect API rate limits
- Implement exponential backoff when limits reached
- Use libraries that handle rate limiting automatically (e.g., Tweepy, PRAW)

**2. Error Handling**:
- Implement robust error handling (network errors, API errors)
- Log errors for debugging
- Retry failed requests with backoff

**3. Data Storage**:
- Use appropriate data structures (databases for large datasets)
- Implement data versioning and backups
- Document data schema and collection parameters

**4. Data Quality**:
- Implement deduplication
- Filter spam and bots
- Validate data completeness
- Document data cleaning steps

**5. Reproducibility**:
- Document collection methodology
- Save collection parameters (queries, date ranges, filters)
- Version control code
- Share data (when permitted) or provide access instructions

## Conclusion

Effective social media data collection requires:

1. **Platform knowledge**: Understand API capabilities and limitations
2. **Tool selection**: Choose appropriate tools for research scale and budget
3. **Ethical practice**: Respect privacy, comply with regulations, follow ToS
4. **Technical rigor**: Implement robust collection, storage, and quality checks
5. **Documentation**: Document methodology for reproducibility and transparency

By combining official APIs, third-party tools, and ethical best practices, researchers can collect high-quality social media data for actionable insights while respecting user privacy and platform policies.