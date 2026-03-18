# In-App Purchases

Detailed implementation guide for in-app purchases on iOS (StoreKit) and Android (Google Play Billing).

## iOS Implementation (StoreKit 2)

### Setup and Configuration

#### App Store Connect Setup

1. **Create In-App Purchases:**
   - Log in to App Store Connect
   - Select your app
   - Go to "Features" → "In-App Purchases"
   - Click "+" to create new IAP

2. **IAP Types:**
   - **Consumable** — Can be purchased multiple times
   - **Non-Consumable** — One-time purchase
   - **Auto-Renewable Subscription** — Recurring subscription
   - **Non-Renewing Subscription** — Fixed duration

3. **Configure IAP:**
   - Product ID: `com.yourapp.product.id`
   - Reference Name: Internal name
   - Price: Select price tier
   - Localization: Add descriptions for each language

4. **Subscription Groups (for subscriptions):**
   - Create subscription group
   - Add subscriptions to group
   - Set upgrade/downgrade behavior

#### Xcode Configuration

```swift
// 1. Enable In-App Purchase capability
// Xcode → Target → Signing & Capabilities → + Capability → In-App Purchase

// 2. Add StoreKit Configuration File (for testing)
// File → New → File → StoreKit Configuration File
// Add products matching App Store Connect

// 3. Configure scheme to use StoreKit Configuration
// Product → Scheme → Edit Scheme → Run → Options → StoreKit Configuration
```

### StoreKit 2 Implementation

#### Product Management

```swift
import StoreKit

class StoreManager: ObservableObject {
    @Published var products: [Product] = []
    @Published var purchasedProductIDs: Set<String> = []
    
    private var updateListenerTask: Task<Void, Never>?
    
    init() {
        updateListenerTask = listenForTransactions()
        Task {
            await loadProducts()
            await updatePurchasedProducts()
        }
    }
    
    deinit {
        updateListenerTask?.cancel()
    }
    
    // Load products from App Store
    func loadProducts() async {
        do {
            let productIDs = [
                "com.app.premium.monthly",
                "com.app.premium.annual",
                "com.app.removeads",
                "com.app.coins.small",
                "com.app.coins.large"
            ]
            
            products = try await Product.products(for: productIDs)
            print("Loaded \(products.count) products")
        } catch {
            print("Failed to load products: \(error)")
        }
    }
    
    // Purchase product
    func purchase(_ product: Product) async throws -> Transaction? {
        let result = try await product.purchase()
        
        switch result {
        case .success(let verification):
            let transaction = try checkVerified(verification)
            await updatePurchasedProducts()
            await transaction.finish()
            return transaction
            
        case .userCancelled:
            print("User cancelled purchase")
            return nil
            
        case .pending:
            print("Purchase pending (Ask to Buy)")
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
    
    // Update purchased products
    func updatePurchasedProducts() async {
        var purchasedIDs: Set<String> = []
        
        for await result in Transaction.currentEntitlements {
            guard let transaction = try? checkVerified(result) else {
                continue
            }
            
            if transaction.revocationDate == nil {
                purchasedIDs.insert(transaction.productID)
            }
        }
        
        await MainActor.run {
            self.purchasedProductIDs = purchasedIDs
        }
    }
    
    // Listen for transaction updates
    func listenForTransactions() -> Task<Void, Never> {
        return Task.detached {
            for await result in Transaction.updates {
                guard let transaction = try? self.checkVerified(result) else {
                    continue
                }
                
                await self.updatePurchasedProducts()
                await transaction.finish()
            }
        }
    }
    
    // Restore purchases
    func restorePurchases() async {
        do {
            try await AppStore.sync()
            await updatePurchasedProducts()
        } catch {
            print("Failed to restore purchases: \(error)")
        }
    }
}

enum StoreError: Error {
    case failedVerification
}
```

#### Subscription Management

```swift
extension StoreManager {
    // Check if user has active subscription
    func hasActiveSubscription() async -> Bool {
        for await result in Transaction.currentEntitlements {
            guard let transaction = try? checkVerified(result) else {
                continue
            }
            
            if transaction.productType == .autoRenewable {
                return true
            }
        }
        return false
    }
    
    // Get subscription status
    func getSubscriptionStatus(for productID: String) async -> SubscriptionStatus? {
        guard let product = products.first(where: { $0.id == productID }),
              let subscription = product.subscription else {
            return nil
        }
        
        guard let status = try? await subscription.status.first else {
            return nil
        }
        
        return SubscriptionStatus(
            state: status.state,
            renewalDate: status.renewalInfo.expirationDate,
            willAutoRenew: status.renewalInfo.willAutoRenew,
            isInGracePeriod: status.state == .inGracePeriod,
            isInBillingRetry: status.state == .inBillingRetryPeriod
        )
    }
    
    // Get subscription renewal info
    func getSubscriptionRenewalInfo(for productID: String) async -> RenewalInfo? {
        guard let product = products.first(where: { $0.id == productID }),
              let subscription = product.subscription,
              let status = try? await subscription.status.first else {
            return nil
        }
        
        let renewalInfo = status.renewalInfo
        return RenewalInfo(
            willAutoRenew: renewalInfo.willAutoRenew,
            expirationDate: renewalInfo.expirationDate,
            renewalDate: renewalInfo.renewalDate,
            productID: renewalInfo.currentProductID
        )
    }
}

struct SubscriptionStatus {
    let state: Product.SubscriptionInfo.Status.State
    let renewalDate: Date?
    let willAutoRenew: Bool
    let isInGracePeriod: Bool
    let isInBillingRetry: Bool
}

struct RenewalInfo {
    let willAutoRenew: Bool
    let expirationDate: Date?
    let renewalDate: Date?
    let productID: String
}
```

#### UI Integration

```swift
import SwiftUI

struct StoreView: View {
    @StateObject private var store = StoreManager()
    @State private var isPurchasing = false
    @State private var errorMessage: String?
    
    var body: some View {
        List {
            ForEach(store.products, id: \.id) { product in
                ProductRow(product: product, isPurchased: store.purchasedProductIDs.contains(product.id)) {
                    await purchaseProduct(product)
                }
            }
        }
        .navigationTitle("Store")
        .toolbar {
            ToolbarItem(placement: .navigationBarTrailing) {
                Button("Restore") {
                    Task {
                        await store.restorePurchases()
                    }
                }
            }
        }
        .alert("Error", isPresented: .constant(errorMessage != nil)) {
            Button("OK") {
                errorMessage = nil
            }
        } message: {
            Text(errorMessage ?? "")
        }
    }
    
    func purchaseProduct(_ product: Product) async {
        isPurchasing = true
        defer { isPurchasing = false }
        
        do {
            let transaction = try await store.purchase(product)
            if transaction != nil {
                print("Purchase successful")
            }
        } catch {
            errorMessage = "Purchase failed: \(error.localizedDescription)"
        }
    }
}

struct ProductRow: View {
    let product: Product
    let isPurchased: Bool
    let onPurchase: () async -> Void
    
    var body: some View {
        HStack {
            VStack(alignment: .leading) {
                Text(product.displayName)
                    .font(.headline)
                Text(product.description)
                    .font(.caption)
                    .foregroundColor(.secondary)
            }
            
            Spacer()
            
            if isPurchased {
                Image(systemName: "checkmark.circle.fill")
                    .foregroundColor(.green)
            } else {
                Button(product.displayPrice) {
                    Task {
                        await onPurchase()
                    }
                }
                .buttonStyle(.borderedProminent)
            }
        }
    }
}
```

### Server-Side Receipt Validation

```swift
// Send receipt to your server for validation
func validateReceipt(transaction: Transaction) async throws {
    guard let receiptURL = Bundle.main.appStoreReceiptURL,
          let receiptData = try? Data(contentsOf: receiptURL) else {
        throw ValidationError.noReceipt
    }
    
    let receiptString = receiptData.base64EncodedString()
    
    // Send to your server
    var request = URLRequest(url: URL(string: "https://yourserver.com/validate")!)
    request.httpMethod = "POST"
    request.setValue("application/json", forHTTPHeaderField: "Content-Type")
    
    let body = [
        "receipt": receiptString,
        "transaction_id": transaction.id,
        "product_id": transaction.productID
    ]
    request.httpBody = try JSONSerialization.data(withJSONObject: body)
    
    let (data, response) = try await URLSession.shared.data(for: request)
    
    guard let httpResponse = response as? HTTPURLResponse,
          httpResponse.statusCode == 200 else {
        throw ValidationError.invalidResponse
    }
    
    // Parse server response
    let result = try JSONDecoder().decode(ValidationResult.self, from: data)
    if !result.isValid {
        throw ValidationError.invalidReceipt
    }
}

enum ValidationError: Error {
    case noReceipt
    case invalidResponse
    case invalidReceipt
}

struct ValidationResult: Codable {
    let isValid: Bool
    let expirationDate: Date?
}
```

## Android Implementation (Google Play Billing)

### Setup and Configuration

#### Google Play Console Setup

1. **Create In-App Products:**
   - Log in to Google Play Console
   - Select your app
   - Go to "Monetize" → "Products" → "In-app products"
   - Click "Create product"

2. **Product Types:**
   - **Consumable** — Can be purchased multiple times
   - **Non-consumable** — One-time purchase
   - **Subscription** — Recurring subscription

3. **Configure Product:**
   - Product ID: `premium_monthly`
   - Name: Display name
   - Description: Product description
   - Price: Set price for each country
   - Status: Active

#### Gradle Configuration

```gradle
// app/build.gradle
dependencies {
    implementation 'com.android.billingclient:billing-ktx:6.0.1'
}
```

### Google Play Billing Implementation

#### Billing Manager

```kotlin
import com.android.billingclient.api.*
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow

class BillingManager(private val context: Context) {
    private lateinit var billingClient: BillingClient
    
    private val _products = MutableStateFlow<List<ProductDetails>>(emptyList())
    val products: StateFlow<List<ProductDetails>> = _products
    
    private val _purchases = MutableStateFlow<List<Purchase>>(emptyList())
    val purchases: StateFlow<List<Purchase>> = _purchases
    
    fun initialize() {
        billingClient = BillingClient.newBuilder(context)
            .setListener { billingResult, purchases ->
                if (billingResult.responseCode == BillingClient.BillingResponseCode.OK && purchases != null) {
                    handlePurchases(purchases)
                }
            }
            .enablePendingPurchases()
            .build()
        
        billingClient.startConnection(object : BillingClientStateListener {
            override fun onBillingSetupFinished(billingResult: BillingResult) {
                if (billingResult.responseCode == BillingClient.BillingResponseCode.OK) {
                    queryProducts()
                    queryPurchases()
                }
            }
            
            override fun onBillingServiceDisconnected() {
                // Retry connection
            }
        })
    }
    
    // Query products
    private fun queryProducts() {
        val productList = listOf(
            QueryProductDetailsParams.Product.newBuilder()
                .setProductId("premium_monthly")
                .setProductType(BillingClient.ProductType.SUBS)
                .build(),
            QueryProductDetailsParams.Product.newBuilder()
                .setProductId("premium_annual")
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
        
        billingClient.queryProductDetailsAsync(params) { billingResult, productDetailsList ->
            if (billingResult.responseCode == BillingClient.BillingResponseCode.OK) {
                _products.value = productDetailsList
            }
        }
    }
    
    // Launch purchase flow
    fun launchPurchaseFlow(activity: Activity, productDetails: ProductDetails, offerToken: String? = null) {
        val productDetailsParamsList = if (productDetails.productType == BillingClient.ProductType.SUBS) {
            listOf(
                BillingFlowParams.ProductDetailsParams.newBuilder()
                    .setProductDetails(productDetails)
                    .setOfferToken(offerToken ?: productDetails.subscriptionOfferDetails?.first()?.offerToken ?: "")
                    .build()
            )
        } else {
            listOf(
                BillingFlowParams.ProductDetailsParams.newBuilder()
                    .setProductDetails(productDetails)
                    .build()
            )
        }
        
        val billingFlowParams = BillingFlowParams.newBuilder()
            .setProductDetailsParamsList(productDetailsParamsList)
            .build()
        
        billingClient.launchBillingFlow(activity, billingFlowParams)
    }
    
    // Handle purchases
    private fun handlePurchases(purchases: List<Purchase>) {
        for (purchase in purchases) {
            if (purchase.purchaseState == Purchase.PurchaseState.PURCHASED) {
                if (!purchase.isAcknowledged) {
                    acknowledgePurchase(purchase)
                }
                grantEntitlement(purchase)
            }
        }
        _purchases.value = purchases
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
    
    // Grant entitlement
    private fun grantEntitlement(purchase: Purchase) {
        // Update app state to reflect purchase
        // e.g., remove ads, unlock premium features
    }
    
    // Query purchases
    private fun queryPurchases() {
        billingClient.queryPurchasesAsync(
            QueryPurchasesParams.newBuilder()
                .setProductType(BillingClient.ProductType.SUBS)
                .build()
        ) { billingResult, purchases ->
            if (billingResult.responseCode == BillingClient.BillingResponseCode.OK) {
                handlePurchases(purchases)
            }
        }
        
        billingClient.queryPurchasesAsync(
            QueryPurchasesParams.newBuilder()
                .setProductType(BillingClient.ProductType.INAPP)
                .build()
        ) { billingResult, purchases ->
            if (billingResult.responseCode == BillingClient.BillingResponseCode.OK) {
                handlePurchases(purchases)
            }
        }
    }
    
    // Check if product is purchased
    fun isPurchased(productId: String): Boolean {
        return _purchases.value.any { it.products.contains(productId) && it.purchaseState == Purchase.PurchaseState.PURCHASED }
    }
}
```

#### UI Integration (Jetpack Compose)

```kotlin
@Composable
fun StoreScreen(billingManager: BillingManager) {
    val products by billingManager.products.collectAsState()
    val purchases by billingManager.purchases.collectAsState()
    val context = LocalContext.current
    
    LazyColumn {
        items(products) { product ->
            ProductItem(
                product = product,
                isPurchased = billingManager.isPurchased(product.productId),
                onPurchase = {
                    billingManager.launchPurchaseFlow(
                        context as Activity,
                        product
                    )
                }
            )
        }
    }
}

@Composable
fun ProductItem(
    product: ProductDetails,
    isPurchased: Boolean,
    onPurchase: () -> Unit
) {
    Card(
        modifier = Modifier
            .fillMaxWidth()
            .padding(8.dp)
    ) {
        Row(
            modifier = Modifier.padding(16.dp),
            verticalAlignment = Alignment.CenterVertically
        ) {
            Column(modifier = Modifier.weight(1f)) {
                Text(
                    text = product.name,
                    style = MaterialTheme.typography.titleMedium
                )
                Text(
                    text = product.description,
                    style = MaterialTheme.typography.bodySmall
                )
            }
            
            if (isPurchased) {
                Icon(
                    imageVector = Icons.Default.CheckCircle,
                    contentDescription = "Purchased",
                    tint = Color.Green
                )
            } else {
                Button(onClick = onPurchase) {
                    Text(product.oneTimePurchaseOfferDetails?.formattedPrice ?: "Subscribe")
                }
            }
        }
    }
}
```

### Server-Side Verification

```kotlin
// Send purchase token to server for verification
suspend fun verifyPurchase(purchase: Purchase): Boolean {
    val client = OkHttpClient()
    val json = JSONObject().apply {
        put("purchase_token", purchase.purchaseToken)
        put("product_id", purchase.products.first())
        put("package_name", purchase.packageName)
    }
    
    val request = Request.Builder()
        .url("https://yourserver.com/verify")
        .post(json.toString().toRequestBody("application/json".toMediaType()))
        .build()
    
    return withContext(Dispatchers.IO) {
        try {
            val response = client.newCall(request).execute()
            response.isSuccessful
        } catch (e: Exception) {
            false
        }
    }
}
```

## Testing

### iOS Testing

**Sandbox Testing:**
1. Create sandbox tester account in App Store Connect
2. Sign out of App Store on device
3. Run app and make purchase
4. Sign in with sandbox account when prompted

**StoreKit Configuration File:**
- Test locally without server
- Instant purchase completion
- No real money involved

### Android Testing

**License Testing:**
1. Add test account in Google Play Console
2. Install app from internal testing track
3. Make test purchases (no charge)

**Test Cards:**
- Google provides test credit cards
- No real charges
- Instant purchase completion

## Best Practices

1. **Always validate receipts server-side**
2. **Handle all purchase states** (pending, cancelled, failed)
3. **Provide restore purchases option**
4. **Cache product information**
5. **Handle network failures gracefully**
6. **Test thoroughly with sandbox/test accounts**
7. **Monitor purchase analytics**
8. **Comply with platform policies**
9. **Provide clear refund policy**
10. **Support family sharing (iOS)**
