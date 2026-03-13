# Nextdoor Conversion API Guide
## CAPI Implementation
1. Capture ndclid from URL query string
2. Store with user session
3. Send conversion events server-to-server
4. Hash customer data (email, phone)
## Event Types
- PageView, AddToCart, Purchase, Lead, CompleteRegistration
## Benefits
- Bypasses ad blockers
- Offline conversion tracking
- More accurate attribution
