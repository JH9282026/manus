# Advertising Integration

Comprehensive guide to mobile advertising integration, ad networks, mediation, and revenue optimization.

## Ad Network Overview

### Top Ad Networks Comparison

| Network | Fill Rate | eCPM Range | Best Ad Format | Platform | Best For |
|---------|-----------|------------|----------------|----------|----------|
| **Google AdMob** | 95-99% | $2-$15 | All formats | iOS, Android | General apps, high volume |
| **Meta Audience Network** | 90-95% | $5-$25 | Native, Banner | iOS, Android | Social apps, high engagement |
| **Unity Ads** | 95-98% | $10-$40 | Rewarded Video | iOS, Android, Unity | Games |
| **AppLovin** | 95-99% | $8-$30 | Rewarded, Interstitial | iOS, Android | Games, utilities |
| **ironSource** | 95-98% | $5-$20 | Rewarded, Interstitial | iOS, Android | Games |
| **Vungle** | 90-95% | $10-$35 | Video | iOS, Android | Games, video-heavy apps |
| **Chartboost** | 85-90% | $5-$15 | Interstitial | iOS, Android | Games |
| **AdColony** | 90-95% | $8-$25 | Video | iOS, Android | Games, entertainment |

### Ad Format Comparison

| Format | eCPM | User Impact | Implementation | Best Use Case |
|--------|------|-------------|----------------|---------------|
| **Banner** | $0.50-$2 | Low | Easy | Continuous display |
| **Interstitial** | $3-$10 | Medium | Easy | Natural breaks |
| **Rewarded Video** | $10-$50 | Low (opt-in) | Medium | User-initiated rewards |
| **Native** | $2-$8 | Low | Complex | Content integration |
| **Playable** | $15-$40 | Medium | Complex | Game discovery |
| **Offerwall** | $5-$20 | Medium | Medium | Engagement campaigns |

## AdMob Integration

### iOS Implementation

#### Setup

```swift
// 1. Add Google Mobile Ads SDK via CocoaPods
// Podfile:
// pod 'Google-Mobile-Ads-SDK'

// 2. Update Info.plist
// Add GADApplicationIdentifier key with your AdMob App ID
// <key>GADApplicationIdentifier</key>
// <string>ca-app-pub-XXXXXXXXXXXXXXXX~YYYYYYYYYY</string>

// 3. Add App Transport Security exception (if needed)
// <key>NSAppTransportSecurity</key>
// <dict>
//     <key>NSAllowsArbitraryLoads</key>
//     <true/>
// </dict>
```

#### Initialization

```swift
import GoogleMobileAds
import UIKit

@main
class AppDelegate: UIResponder, UIApplicationDelegate {
    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        // Initialize AdMob
        GADMobileAds.sharedInstance().start(completionHandler: nil)
        
        // Optional: Request tracking authorization (iOS 14+)
        if #available(iOS 14, *) {
            ATTrackingManager.requestTrackingAuthorization { status in
                // Handle authorization status
            }
        }
        
        return true
    }
}
```

#### Banner Ads

```swift
import GoogleMobileAds
import UIKit

class BannerViewController: UIViewController {
    var bannerView: GADBannerView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Create banner view
        bannerView = GADBannerView(adSize: GADAdSizeBanner)
        bannerView.adUnitID = "ca-app-pub-XXXXXXXXXXXXXXXX/YYYYYYYYYY"
        bannerView.rootViewController = self
        bannerView.delegate = self
        
        // Add to view
        addBannerViewToView(bannerView)
        
        // Load ad
        bannerView.load(GADRequest())
    }
    
    func addBannerViewToView(_ bannerView: GADBannerView) {
        bannerView.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(bannerView)
        NSLayoutConstraint.activate([
            bannerView.bottomAnchor.constraint(equalTo: view.safeAreaLayoutGuide.bottomAnchor),
            bannerView.centerXAnchor.constraint(equalTo: view.centerXAnchor)
        ])
    }
}

extension BannerViewController: GADBannerViewDelegate {
    func bannerViewDidReceiveAd(_ bannerView: GADBannerView) {
        print("Banner ad loaded successfully")
    }
    
    func bannerView(_ bannerView: GADBannerView, didFailToReceiveAdWithError error: Error) {
        print("Banner ad failed to load: \(error.localizedDescription)")
    }
}
```

#### Interstitial Ads

```swift
import GoogleMobileAds

class InterstitialManager: NSObject {
    private var interstitialAd: GADInterstitialAd?
    private var isLoading = false
    
    func loadAd() {
        guard !isLoading else { return }
        isLoading = true
        
        let request = GADRequest()
        GADInterstitialAd.load(
            withAdUnitID: "ca-app-pub-XXXXXXXXXXXXXXXX/YYYYYYYYYY",
            request: request
        ) { [weak self] ad, error in
            self?.isLoading = false
            
            if let error = error {
                print("Failed to load interstitial: \(error.localizedDescription)")
                return
            }
            
            self?.interstitialAd = ad
            self?.interstitialAd?.fullScreenContentDelegate = self
            print("Interstitial ad loaded")
        }
    }
    
    func showAd(from viewController: UIViewController) {
        if let ad = interstitialAd {
            ad.present(fromRootViewController: viewController)
        } else {
            print("Interstitial ad not ready")
            loadAd()
        }
    }
}

extension InterstitialManager: GADFullScreenContentDelegate {
    func adDidDismissFullScreenContent(_ ad: GADFullScreenPresentingAd) {
        print("Interstitial ad dismissed")
        loadAd() // Preload next ad
    }
    
    func ad(_ ad: GADFullScreenPresentingAd, didFailToPresentFullScreenContentWithError error: Error) {
        print("Interstitial ad failed to present: \(error.localizedDescription)")
        loadAd()
    }
}
```

#### Rewarded Ads

```swift
import GoogleMobileAds

class RewardedAdManager: NSObject {
    private var rewardedAd: GADRewardedAd?
    private var isLoading = false
    
    func loadAd() {
        guard !isLoading else { return }
        isLoading = true
        
        let request = GADRequest()
        GADRewardedAd.load(
            withAdUnitID: "ca-app-pub-XXXXXXXXXXXXXXXX/YYYYYYYYYY",
            request: request
        ) { [weak self] ad, error in
            self?.isLoading = false
            
            if let error = error {
                print("Failed to load rewarded ad: \(error.localizedDescription)")
                return
            }
            
            self?.rewardedAd = ad
            self?.rewardedAd?.fullScreenContentDelegate = self
            print("Rewarded ad loaded")
        }
    }
    
    func showAd(from viewController: UIViewController, completion: @escaping (Bool) -> Void) {
        if let ad = rewardedAd {
            ad.present(fromRootViewController: viewController) {
                let reward = ad.adReward
                print("User earned reward: \(reward.amount) \(reward.type)")
                completion(true)
            }
        } else {
            print("Rewarded ad not ready")
            completion(false)
            loadAd()
        }
    }
}

extension RewardedAdManager: GADFullScreenContentDelegate {
    func adDidDismissFullScreenContent(_ ad: GADFullScreenPresentingAd) {
        print("Rewarded ad dismissed")
        loadAd()
    }
    
    func ad(_ ad: GADFullScreenPresentingAd, didFailToPresentFullScreenContentWithError error: Error) {
        print("Rewarded ad failed to present: \(error.localizedDescription)")
        loadAd()
    }
}
```

### Android Implementation

#### Setup

```gradle
// app/build.gradle
dependencies {
    implementation 'com.google.android.gms:play-services-ads:22.5.0'
}
```

```xml
<!-- AndroidManifest.xml -->
<manifest>
    <application>
        <meta-data
            android:name="com.google.android.gms.ads.APPLICATION_ID"
            android:value="ca-app-pub-XXXXXXXXXXXXXXXX~YYYYYYYYYY"/>
    </application>
</manifest>
```

#### Initialization

```kotlin
import com.google.android.gms.ads.MobileAds
import android.app.Application

class MyApplication : Application() {
    override fun onCreate() {
        super.onCreate()
        
        // Initialize AdMob
        MobileAds.initialize(this) { initializationStatus ->
            // Initialization complete
        }
    }
}
```

#### Banner Ads

```kotlin
import com.google.android.gms.ads.AdRequest
import com.google.android.gms.ads.AdView
import com.google.android.gms.ads.AdListener

class BannerActivity : AppCompatActivity() {
    private lateinit var adView: AdView
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_banner)
        
        adView = findViewById(R.id.adView)
        adView.adListener = object : AdListener() {
            override fun onAdLoaded() {
                Log.d("AdMob", "Banner ad loaded")
            }
            
            override fun onAdFailedToLoad(error: LoadAdError) {
                Log.e("AdMob", "Banner ad failed to load: ${error.message}")
            }
        }
        
        val adRequest = AdRequest.Builder().build()
        adView.loadAd(adRequest)
    }
    
    override fun onPause() {
        adView.pause()
        super.onPause()
    }
    
    override fun onResume() {
        super.onResume()
        adView.resume()
    }
    
    override fun onDestroy() {
        adView.destroy()
        super.onDestroy()
    }
}
```

```xml
<!-- res/layout/activity_banner.xml -->
<LinearLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:ads="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">
    
    <!-- Your content -->
    
    <com.google.android.gms.ads.AdView
        android:id="@+id/adView"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_gravity="center"
        ads:adSize="BANNER"
        ads:adUnitId="ca-app-pub-XXXXXXXXXXXXXXXX/YYYYYYYYYY"/>
</LinearLayout>
```

#### Interstitial Ads

```kotlin
import com.google.android.gms.ads.interstitial.InterstitialAd
import com.google.android.gms.ads.interstitial.InterstitialAdLoadCallback

class InterstitialManager(private val context: Context) {
    private var interstitialAd: InterstitialAd? = null
    private var isLoading = false
    
    fun loadAd() {
        if (isLoading) return
        isLoading = true
        
        val adRequest = AdRequest.Builder().build()
        InterstitialAd.load(
            context,
            "ca-app-pub-XXXXXXXXXXXXXXXX/YYYYYYYYYY",
            adRequest,
            object : InterstitialAdLoadCallback() {
                override fun onAdLoaded(ad: InterstitialAd) {
                    isLoading = false
                    interstitialAd = ad
                    Log.d("AdMob", "Interstitial ad loaded")
                    
                    ad.fullScreenContentCallback = object : FullScreenContentCallback() {
                        override fun onAdDismissedFullScreenContent() {
                            Log.d("AdMob", "Interstitial ad dismissed")
                            loadAd()
                        }
                        
                        override fun onAdFailedToShowFullScreenContent(error: AdError) {
                            Log.e("AdMob", "Interstitial ad failed to show: ${error.message}")
                        }
                    }
                }
                
                override fun onAdFailedToLoad(error: LoadAdError) {
                    isLoading = false
                    Log.e("AdMob", "Interstitial ad failed to load: ${error.message}")
                }
            }
        )
    }
    
    fun showAd(activity: Activity) {
        interstitialAd?.show(activity) ?: run {
            Log.d("AdMob", "Interstitial ad not ready")
            loadAd()
        }
    }
}
```

#### Rewarded Ads

```kotlin
import com.google.android.gms.ads.rewarded.RewardedAd
import com.google.android.gms.ads.rewarded.RewardedAdLoadCallback

class RewardedAdManager(private val context: Context) {
    private var rewardedAd: RewardedAd? = null
    private var isLoading = false
    
    fun loadAd() {
        if (isLoading) return
        isLoading = true
        
        val adRequest = AdRequest.Builder().build()
        RewardedAd.load(
            context,
            "ca-app-pub-XXXXXXXXXXXXXXXX/YYYYYYYYYY",
            adRequest,
            object : RewardedAdLoadCallback() {
                override fun onAdLoaded(ad: RewardedAd) {
                    isLoading = false
                    rewardedAd = ad
                    Log.d("AdMob", "Rewarded ad loaded")
                    
                    ad.fullScreenContentCallback = object : FullScreenContentCallback() {
                        override fun onAdDismissedFullScreenContent() {
                            Log.d("AdMob", "Rewarded ad dismissed")
                            loadAd()
                        }
                        
                        override fun onAdFailedToShowFullScreenContent(error: AdError) {
                            Log.e("AdMob", "Rewarded ad failed to show: ${error.message}")
                        }
                    }
                }
                
                override fun onAdFailedToLoad(error: LoadAdError) {
                    isLoading = false
                    Log.e("AdMob", "Rewarded ad failed to load: ${error.message}")
                }
            }
        )
    }
    
    fun showAd(activity: Activity, onRewarded: (Int, String) -> Unit) {
        rewardedAd?.show(activity) { rewardItem ->
            Log.d("AdMob", "User earned reward: ${rewardItem.amount} ${rewardItem.type}")
            onRewarded(rewardItem.amount, rewardItem.type)
        } ?: run {
            Log.d("AdMob", "Rewarded ad not ready")
            loadAd()
        }
    }
}
```

## Ad Mediation

### What is Ad Mediation?

Ad mediation allows you to use multiple ad networks through a single SDK, automatically selecting the highest-paying network for each ad request.

**Benefits:**
- Higher fill rates (99%+)
- Increased eCPM (20-50% lift)
- Automatic optimization
- Single SDK integration
- Waterfall and bidding support

### AdMob Mediation Setup

#### iOS Setup

```ruby
# Podfile
pod 'Google-Mobile-Ads-SDK'
pod 'GoogleMobileAdsMediationFacebook'
pod 'GoogleMobileAdsMediationUnity'
pod 'GoogleMobileAdsMediationAppLovin'
pod 'GoogleMobileAdsMediationVungle'
```

#### Android Setup

```gradle
// app/build.gradle
dependencies {
    implementation 'com.google.android.gms:play-services-ads:22.5.0'
    implementation 'com.google.ads.mediation:facebook:6.16.0.0'
    implementation 'com.google.ads.mediation:unity:4.9.2.0'
    implementation 'com.google.ads.mediation:applovin:12.1.0.0'
    implementation 'com.google.ads.mediation:vungle:7.1.0.0'
}
```

#### AdMob Dashboard Configuration

1. **Create Mediation Group:**
   - Go to AdMob → Mediation
   - Click "Create mediation group"
   - Select ad format and platform

2. **Add Ad Sources:**
   - Add AdMob Network (always included)
   - Add third-party networks (Facebook, Unity, etc.)
   - Enter network credentials and ad unit IDs

3. **Set eCPM Floors:**
   - Set minimum eCPM for each network
   - Higher eCPM networks get priority
   - Use historical data to optimize

4. **Configure Waterfall:**
   - Networks ordered by eCPM (highest first)
   - If top network fails, next network tries
   - Continues until ad is filled

### Bidding vs Waterfall

**Waterfall (Traditional):**
- Networks called sequentially
- Based on historical eCPM
- Slower (multiple network calls)
- May miss highest bidder

**Bidding (Modern):**
- Networks bid in real-time
- Highest bidder wins
- Faster (parallel requests)
- Maximizes revenue

**Hybrid Approach:**
- Bidding networks compete first
- Waterfall networks as fallback
- Best of both worlds

## Ad Placement Strategy

### Banner Ads

**Best Practices:**
- Place at bottom of screen
- Don't cover important content
- Refresh every 30-60 seconds
- Use adaptive banners for better fill

**Avoid:**
- Multiple banners on same screen
- Banners at top (blocks content)
- Too frequent refreshes (<30s)

### Interstitial Ads

**Best Placements:**
- Between game levels
- After completing a task
- When navigating between screens
- App launch (after 3-5 seconds)

**Frequency Caps:**
```
Max 1 per 3 minutes
Max 3 per session
Max 10 per day
```

**Avoid:**
- During gameplay
- During user input
- Too frequently (annoys users)
- On app launch (immediate)

### Rewarded Video Ads

**Best Placements:**
- Extra lives in games
- Virtual currency rewards
- Unlock premium content
- Skip waiting time
- Hints or power-ups

**Reward Values:**
```
Small reward: 10-50 coins
Medium reward: 50-100 coins
Large reward: 100-500 coins

Extra life: 1 life
Time skip: 30-60 minutes
Hint: 1 hint
```

**Best Practices:**
- Make rewards valuable
- Clear value proposition
- Optional (never forced)
- Limit per day (5-10)

## Revenue Optimization

### A/B Testing

**Test Variables:**
- Ad placement
- Ad frequency
- Ad format
- Reward values
- Mediation settings

**Example Test:**
```
Control Group (50%):
- Interstitial every 3 minutes
- Banner at bottom

Variant A (25%):
- Interstitial every 5 minutes
- Banner at bottom

Variant B (25%):
- Interstitial every 3 minutes
- No banner

Measure:
- ARPDAU
- Retention (D1, D7)
- Session length
- User feedback
```

### User Segmentation

**Segment by Engagement:**
```
New Users (Day 0-1):
- Minimal ads
- Focus on retention
- Show value first

Engaged Users (Day 2-7):
- Standard ad frequency
- Introduce rewarded videos
- Offer ad removal

Retained Users (Day 8+):
- Full ad frequency
- Optimize for revenue
- Personalized offers

Paying Users:
- No ads (or minimal)
- Respect their investment
- Offer premium ad-free experience
```

### eCPM Optimization

**Factors Affecting eCPM:**
- User geography (Tier 1 > Tier 2 > Tier 3)
- Ad format (Rewarded > Interstitial > Banner)
- Time of day (peak hours higher)
- Day of week (weekdays > weekends)
- Seasonality (holidays higher)
- User demographics (age, gender, interests)

**Optimization Tactics:**
- Use mediation for higher fill rates
- Enable bidding for real-time competition
- Set appropriate eCPM floors
- Test different ad formats
- Optimize ad placements
- Target high-value users

## Analytics and Monitoring

### Key Metrics

**Ad Performance:**
```
Impressions: Total ads shown
Clicks: Total ad clicks
CTR: Clicks / Impressions
eCPM: Revenue / Impressions * 1000
Fill Rate: Filled Requests / Total Requests
```

**Revenue Metrics:**
```
ARPDAU: Daily Ad Revenue / DAU
Ad Revenue %: Ad Revenue / Total Revenue
Revenue per Session: Ad Revenue / Total Sessions
```

**User Impact:**
```
Retention (D1, D7, D30)
Session Length
Sessions per User
Churn Rate
```

### Monitoring Tools

- **AdMob Dashboard** — Real-time metrics
- **Firebase Analytics** — User behavior
- **Google Analytics** — Detailed insights
- **Third-party tools** — Adjust, AppsFlyer

## Best Practices

1. **User Experience First** — Don't sacrifice UX for revenue
2. **Test Thoroughly** — A/B test placements and frequency
3. **Use Mediation** — Maximize fill rate and eCPM
4. **Monitor Metrics** — Track ARPDAU, retention, eCPM
5. **Respect Users** — Offer ad-free option
6. **Comply with Policies** — Follow platform guidelines
7. **Optimize Continuously** — Regular testing and iteration
8. **Segment Users** — Different strategies for different users
9. **Balance Revenue and Retention** — Don't over-monetize
10. **Provide Value** — Rewarded ads should offer real value
