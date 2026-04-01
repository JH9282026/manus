---
name: mobile-app-monetization
description: "Implement revenue generation strategies for mobile applications across iOS and Android platforms. Use for: in-app purchases, subscription models, advertising integration, freemium strategies, pricing optimization, revenue analytics, payment processing, ad network integration, user retention for monetization, and maximizing lifetime value (LTV)."
---

# Mobile App Monetization

Implement effective revenue generation strategies for mobile applications across iOS and Android platforms.

## Overview

Mobile app monetization encompasses strategies and technologies for generating revenue from mobile applications. This skill covers revenue models, in-app purchases, subscription management, advertising integration, analytics, optimization techniques, and platform-specific implementation details for iOS (App Store) and Android (Google Play).

## Revenue Model Selection

### Model Comparison

| Model | Revenue Potential | User Friction | Implementation | Best For |
|-------|------------------|---------------|----------------|----------|
| **Freemium** | Medium-High | Low | Medium | Games, productivity, social |
| **Subscriptions** | High | Medium | Medium | Content, SaaS, utilities |
| **Paid Download** | Low-Medium | High | Easy | Premium tools, niche apps |
| **In-App Purchases** | High | Low-Medium | Medium | Games, consumables |
| **Advertising** | Low-Medium | Medium | Easy | Free apps, high DAU |
| **Hybrid** | Very High | Medium | Complex | Mature apps, diverse users |

### Freemium Model

**Structure:**
- Free core features
- Premium features behind paywall
- Typically 2-5% conversion rate

**Best Practices:**
- Provide substantial free value
- Clear premium feature differentiation
- Multiple upgrade touchpoints
- Time-limited trials for premium features

**Pricing Tiers:**
```
Free Tier:
- Core functionality
- Limited usage (e.g., 5 projects)
- Ads (optional)
- Basic support

Premium Tier ($9.99/month):
- Unlimited usage
- Advanced features
- No ads
- Priority support
- Cloud sync

Pro Tier ($19.99/month):
- Everything in Premium
- Team collaboration
- Advanced analytics
- API access
- White-label options
```

### Subscription Model

**Subscription Types:**
- **Auto-renewable** — Recurring billing (most common)
- **Non-renewing** — Fixed duration, manual renewal
- **Consumable** — One-time purchase, can be bought multiple times

**Pricing Strategies:**
```
Monthly: $9.99 (baseline)
Annual: $79.99 (33% discount, ~$6.67/month)
Lifetime: $199.99 (20 months equivalent)
```

**Optimization Tactics:**
- Free trial (3-7 days for mobile, 14-30 days for SaaS)
- Introductory pricing (50% off first month)
- Annual discount (20-40% off)
- Family sharing (up to 6 users)
- Grace period for failed payments

### In-App Purchases (IAP)

**Purchase Types:**

**Consumables** — Can be purchased multiple times
- Virtual currency (coins, gems)
- Power-ups, boosters
- Extra lives, energy
- Consumable content

**Non-Consumables** — One-time purchase
- Remove ads
- Unlock features
- Premium content packs
- Character unlocks

**Subscriptions** — Recurring access
- Premium membership
- Content subscriptions
- Service access

### Advertising Model

**Ad Formats:**

| Format | eCPM | User Experience | Best For |
|--------|------|-----------------|----------|
| **Banner** | $0.50-$2 | Low friction | Continuous display |
| **Interstitial** | $3-$10 | Medium friction | Between levels/screens |
| **Rewarded Video** | $10-$50 | High engagement | Opt-in rewards |
| **Native** | $2-$8 | Seamless | Content feeds |
| **Playable** | $15-$40 | High engagement | Game discovery |

**Ad Placement Strategy:**
- **Banner ads** — Bottom of screen, non-intrusive
- **Interstitial ads** — Natural breaks (level complete, app launch)
- **Rewarded video** — User-initiated (extra lives, currency, unlocks)
- **Native ads** — Integrated into content feed

## Platform Implementation

### iOS (App Store)

#### StoreKit 2 (iOS 15+)

```swift
import StoreKit

// Product definition
enum ProductID: String, CaseIterable {
    case premiumMonthly = "com.app.premium.monthly"
    case premiumAnnual = "com.app.premium.annual"
    case removeAds = "com.app.removeads"
}

// Fetch products
func fetchProducts() async throws -> [Product] {
    let products = try await Product.products(for: ProductID.allCases.map { $0.rawValue })
    return products
}

// Purchase product
func purchase(_ product: Product) async throws -> Transaction? {
    let result = try await product.purchase()
    
    switch result {
    case .success(let verification):
        let transaction = try checkVerified(verification)
        await transaction.finish()
        return transaction
    case .userCancelled:
        return nil
    case .pending:
        return nil
    @unknown default:
        return nil
    }
}

// Verify transaction
func checkVerified<T>(_ result: VerificationResult<T>) throws -> T {
    switch result {
    case .unverified:
        throw StoreError.failedVerification
    case .verified(let safe):
        return safe
    }
}

// Restore purchases
func restorePurchases() async throws {
    try await AppStore.sync()
}

// Listen for transactions
func observeTransactions() -> Task<Void, Never> {
    Task.detached {
        for await result in Transaction.updates {
            guard let transaction = try? self.checkVerified(result) else {
                continue
            }
            await self.updatePurchasedProducts()
            await transaction.finish()
        }
    }
}
```

#### Subscription Management

```swift
// Check subscription status
func checkSubscriptionStatus() async -> Bool {
    guard let product = try? await Product.products(for: ["com.app.premium.monthly"]).first else {
        return false
    }
    
    guard let state = await product.subscription?.status.first else {
        return false
    }
    
    switch state.state {
    case .subscribed, .inGracePeriod:
        return true
    case .expired, .revoked, .inBillingRetryPeriod:
        return false
    default:
        return false
    }
}

// Get subscription info
func getSubscriptionInfo() async -> SubscriptionInfo? {
    guard let product = try? await Product.products(for: ["com.app.premium.monthly"]).first,
          let subscription = product.subscription,
          let status = await subscription.status.first else {
        return nil
    }
    
    return SubscriptionInfo(
        isActive: status.state == .subscribed,
        renewalDate: status.renewalInfo.expirationDate,
        willAutoRenew: status.renewalInfo.willAutoRenew,
        isInGracePeriod: status.state == .inGracePeriod
    )
}
```

### Android (Google Play)

#### Google Play Billing Library 5.0+

```kotlin
import com.android.billingclient.api.*

class BillingManager(private val context: Context) {
    private lateinit var billingClient: BillingClient
    
    fun initialize() {
        billingClient = BillingClient.newBuilder(context)
            .setListener { billingResult, purchases ->
                if (billingResult.responseCode == BillingClient.BillingResponseCode.OK && purchases != null) {
                    for (purchase in purchases) {
                        handlePurchase(purchase)
                    }
                }
            }
            .enablePendingPurchases()
            .build()
        
        billingClient.startConnection(object : BillingClientStateListener {
            override fun onBillingSetupFinished(billingResult: BillingResult) {
                if (billingResult.responseCode == BillingClient.BillingResponseCode.OK) {
                    // Ready to query purchases
                    queryProducts()
                }
            }
            
            override fun onBillingServiceDisconnected() {
                // Retry connection
            }
        })
    }
    
    // Query products
    suspend fun queryProducts(): List<ProductDetails> {
        val productList = listOf(
            QueryProductDetailsParams.Product.newBuilder()
                .setProductId("premium_monthly")
                .setProductType(BillingClient.ProductType.SUBS)
                .build(),
            QueryProductDetailsParams.Product.newBuilder()
                .setProductId("remove_ads")
                .setProductType(BillingClient.ProductType.INAPP)
                .build()
        )
        
        val params = QueryProductDetailsParams.newBuilder()
            .setProductList(productList)
            .build()
        
        val result = billingClient.queryProductDetails(params)
        return result.productDetailsList ?: emptyList()
    }
    
    // Launch purchase flow
    fun launchPurchaseFlow(activity: Activity, productDetails: ProductDetails) {
        val productDetailsParamsList = listOf(
            BillingFlowParams.ProductDetailsParams.newBuilder()
                .setProductDetails(productDetails)
                .build()
        )
        
        val billingFlowParams = BillingFlowParams.newBuilder()
            .setProductDetailsParamsList(productDetailsParamsList)
            .build()
        
        billingClient.launchBillingFlow(activity, billingFlowParams)
    }
    
    // Handle purchase
    private fun handlePurchase(purchase: Purchase) {
        if (purchase.purchaseState == Purchase.PurchaseState.PURCHASED) {
            if (!purchase.isAcknowledged) {
                acknowledgePurchase(purchase)
            }
            // Grant entitlement
            grantEntitlement(purchase)
        }
    }
    
    // Acknowledge purchase
    private fun acknowledgePurchase(purchase: Purchase) {
        val params = AcknowledgePurchaseParams.newBuilder()
            .setPurchaseToken(purchase.purchaseToken)
            .build()
        
        billingClient.acknowledgePurchase(params) { billingResult ->
            if (billingResult.responseCode == BillingClient.BillingResponseCode.OK) {
                // Purchase acknowledged
            }
        }
    }
    
    // Query purchases
    suspend fun queryPurchases(): List<Purchase> {
        val params = QueryPurchasesParams.newBuilder()
            .setProductType(BillingClient.ProductType.SUBS)
            .build()
        
        val result = billingClient.queryPurchasesAsync(params)
        return result.purchasesList
    }
}
```

## Advertising Integration

### Ad Network Selection

**Top Ad Networks:**

| Network | Strengths | eCPM | Best For |
|---------|-----------|------|----------|
| **AdMob** | Google integration, high fill rate | Medium | General apps |
| **Meta Audience Network** | High eCPM, targeting | High | Social apps |
| **Unity Ads** | Gaming focus, rewarded video | High | Games |
| **AppLovin** | Machine learning, high eCPM | High | Games, utilities |
| **ironSource** | Mediation, analytics | Medium-High | Games |
| **Vungle** | Video ads, creative tools | High | Games |

### AdMob Integration (iOS)

```swift
import GoogleMobileAds

class AdManager: NSObject {
    private var interstitialAd: GADInterstitialAd?
    private var rewardedAd: GADRewardedAd?
    
    // Initialize AdMob
    func initialize() {
        GADMobileAds.sharedInstance().start(completionHandler: nil)
    }
    
    // Load banner ad
    func createBannerAd(in view: UIView) -> GADBannerView {
        let bannerView = GADBannerView(adSize: GADAdSizeBanner)
        bannerView.adUnitID = "ca-app-pub-XXXXXXXXXXXXXXXX/YYYYYYYYYY"
        bannerView.rootViewController = view.window?.rootViewController
        bannerView.load(GADRequest())
        return bannerView
    }
    
    // Load interstitial ad
    func loadInterstitialAd() {
        let request = GADRequest()
        GADInterstitialAd.load(
            withAdUnitID: "ca-app-pub-XXXXXXXXXXXXXXXX/YYYYYYYYYY",
            request: request
        ) { [weak self] ad, error in
            if let error = error {
                print("Failed to load interstitial: \(error.localizedDescription)")
                return
            }
            self?.interstitialAd = ad
            self?.interstitialAd?.fullScreenContentDelegate = self
        }
    }
    
    // Show interstitial ad
    func showInterstitialAd(from viewController: UIViewController) {
        if let ad = interstitialAd {
            ad.present(fromRootViewController: viewController)
        } else {
            print("Interstitial ad not ready")
            loadInterstitialAd()
        }
    }
    
    // Load rewarded ad
    func loadRewardedAd() {
        let request = GADRequest()
        GADRewardedAd.load(
            withAdUnitID: "ca-app-pub-XXXXXXXXXXXXXXXX/YYYYYYYYYY",
            request: request
        ) { [weak self] ad, error in
            if let error = error {
                print("Failed to load rewarded ad: \(error.localizedDescription)")
                return
            }
            self?.rewardedAd = ad
            self?.rewardedAd?.fullScreenContentDelegate = self
        }
    }
    
    // Show rewarded ad
    func showRewardedAd(from viewController: UIViewController, completion: @escaping (Bool) -> Void) {
        if let ad = rewardedAd {
            ad.present(fromRootViewController: viewController) {
                let reward = ad.adReward
                print("User earned reward: \(reward.amount) \(reward.type)")
                completion(true)
            }
        } else {
            print("Rewarded ad not ready")
            completion(false)
            loadRewardedAd()
        }
    }
}

// Delegate methods
extension AdManager: GADFullScreenContentDelegate {
    func adDidDismissFullScreenContent(_ ad: GADFullScreenPresentingAd) {
        // Reload ad
        if ad is GADInterstitialAd {
            loadInterstitialAd()
        } else if ad is GADRewardedAd {
            loadRewardedAd()
        }
    }
    
    func ad(_ ad: GADFullScreenPresentingAd, didFailToPresentFullScreenContentWithError error: Error) {
        print("Ad failed to present: \(error.localizedDescription)")
    }
}
```

### Ad Mediation


---

**Note:** This file was automatically condensed to meet the 500-line requirement. Additional content has been moved to the references/ folder.

## References

- [Advertising Integration](references/advertising-integration.md)
- [Analytics Optimization](references/analytics-optimization.md)
- [In App Purchases](references/in-app-purchases.md)
- [Revenue Models](references/revenue-models.md)
