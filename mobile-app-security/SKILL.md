---
name: mobile-app-security
description: "Implement comprehensive mobile app security including secure authentication, data encryption, network security, code obfuscation, and protection against common vulnerabilities following OWASP Mobile Top 10. Use for: securing mobile apps, implementing secure authentication/authorization, encrypting data at rest and in transit, preventing injection attacks, securing network communication, implementing certificate pinning, protecting against reverse engineering, handling sensitive data, following OWASP MASVS guidelines, and conducting security testing."
---

# Mobile App Security

Implement comprehensive security measures to protect mobile applications and user data from threats and vulnerabilities.

## Overview

Mobile app security encompasses protecting applications from threats like data breaches, unauthorized access, reverse engineering, and malicious attacks. This skill covers the OWASP Mobile Top 10 vulnerabilities, secure coding practices, authentication, encryption, network security, code protection, and security testing.

## OWASP Mobile Top 10 (2024)

### M1: Improper Credential Usage

**Risk:** Hardcoded credentials, weak authentication, insecure storage of credentials.

**Mitigation:**
- Never hardcode API keys, passwords, or secrets
- Use secure storage (Keychain on iOS, Keystore on Android)
- Implement proper authentication mechanisms
- Use OAuth 2.0 / OpenID Connect for third-party auth
- Rotate credentials regularly

### M2: Inadequate Supply Chain Security

**Risk:** Vulnerable third-party libraries, compromised dependencies.

**Mitigation:**
- Audit dependencies regularly
- Use dependency scanning tools (Snyk, Dependabot)
- Verify library integrity (checksums, signatures)
- Keep dependencies updated
- Minimize third-party dependencies

### M3: Insecure Authentication/Authorization

**Risk:** Weak authentication, broken authorization, session management issues.

**Mitigation:**
- Implement multi-factor authentication (MFA)
- Use biometric authentication (Face ID, Touch ID, fingerprint)
- Enforce strong password policies
- Implement proper session management
- Use secure tokens (JWT with proper validation)
- Implement authorization checks on backend

### M4: Insufficient Input/Output Validation

**Risk:** Injection attacks (SQL, XSS, command injection).

**Mitigation:**
- Validate all user input
- Sanitize output
- Use parameterized queries (prevent SQL injection)
- Implement input length limits
- Whitelist allowed characters
- Encode output properly

### M5: Insecure Communication

**Risk:** Man-in-the-middle attacks, data interception.

**Mitigation:**
- Use HTTPS for all network communication
- Implement certificate pinning
- Validate SSL/TLS certificates
- Use strong cipher suites
- Avoid mixed content (HTTP + HTTPS)

### M6: Inadequate Privacy Controls

**Risk:** Excessive data collection, improper data handling, privacy violations.

**Mitigation:**
- Collect only necessary data (data minimization)
- Implement privacy by design
- Provide clear privacy policies
- Allow users to control their data
- Comply with GDPR, CCPA, etc.
- Anonymize/pseudonymize data when possible

### M7: Insufficient Binary Protections

**Risk:** Reverse engineering, code tampering, repackaging.

**Mitigation:**
- Obfuscate code (ProGuard/R8 for Android, SwiftShield for iOS)
- Implement anti-tampering checks
- Detect rooted/jailbroken devices
- Use code signing
- Implement runtime application self-protection (RASP)

### M8: Security Misconfiguration

**Risk:** Debug mode in production, excessive permissions, insecure defaults.

**Mitigation:**
- Disable debugging in production builds
- Request minimum necessary permissions
- Secure default configurations
- Remove unused features/code
- Implement proper error handling (don't expose stack traces)

### M9: Insecure Data Storage

**Risk:** Sensitive data stored insecurely, accessible to attackers.

**Mitigation:**
- Encrypt sensitive data at rest
- Use platform secure storage (Keychain, Keystore)
- Avoid storing sensitive data in logs
- Clear sensitive data from memory after use
- Implement secure deletion

### M10: Insufficient Cryptography

**Risk:** Weak encryption, broken crypto, improper key management.

**Mitigation:**
- Use strong, standard algorithms (AES-256, RSA-2048+)
- Avoid custom crypto implementations
- Proper key management (don't hardcode keys)
- Use platform crypto APIs
- Implement proper random number generation

## Secure Authentication

### Best Practices

**Password-Based:**
- Enforce strong password policies (length, complexity)
- Use bcrypt/scrypt/Argon2 for password hashing
- Implement account lockout after failed attempts
- Support password reset securely

**Token-Based (JWT):**
```kotlin
// Validate JWT properly
fun validateToken(token: String): Boolean {
    try {
        val jwt = JWT.decode(token)
        // Verify signature
        // Check expiration
        // Validate claims
        return true
    } catch (e: Exception) {
        return false
    }
}
```

**Biometric Authentication:**

iOS (Face ID / Touch ID):
```swift
import LocalAuthentication

let context = LAContext()
var error: NSError?

if context.canEvaluatePolicy(.deviceOwnerAuthenticationWithBiometrics, error: &error) {
    context.evaluatePolicy(.deviceOwnerAuthenticationWithBiometrics, 
                          localizedReason: "Authenticate to access") { success, error in
        if success {
            // Authenticated
        }
    }
}
```

Android (Fingerprint / Face):
```kotlin
val biometricPrompt = BiometricPrompt(this, executor,
    object : BiometricPrompt.AuthenticationCallback() {
        override fun onAuthenticationSucceeded(result: BiometricPrompt.AuthenticationResult) {
            // Authenticated
        }
    })

val promptInfo = BiometricPrompt.PromptInfo.Builder()
    .setTitle("Biometric Authentication")
    .setNegativeButtonText("Cancel")
    .build()

biometricPrompt.authenticate(promptInfo)
```

## Data Encryption

### Encryption at Rest

**iOS (Keychain):**
```swift
let query: [String: Any] = [
    kSecClass as String: kSecClassGenericPassword,
    kSecAttrAccount as String: "userToken",
    kSecValueData as String: tokenData,
    kSecAttrAccessible as String: kSecAttrAccessibleWhenUnlockedThisDeviceOnly
]

SecItemAdd(query as CFDictionary, nil)
```

**Android (EncryptedSharedPreferences):**
```kotlin
val masterKey = MasterKey.Builder(context)
    .setKeyScheme(MasterKey.KeyScheme.AES256_GCM)
    .build()

val sharedPreferences = EncryptedSharedPreferences.create(
    context,
    "secure_prefs",
    masterKey,
    EncryptedSharedPreferences.PrefKeyEncryptionScheme.AES256_SIV,
    EncryptedSharedPreferences.PrefValueEncryptionScheme.AES256_GCM
)

sharedPreferences.edit().putString("token", token).apply()
```

### Encryption in Transit

**HTTPS Only:**
```xml
<!-- Android Network Security Config -->
<network-security-config>
    <base-config cleartextTrafficPermitted="false">
        <trust-anchors>
            <certificates src="system" />
        </trust-anchors>
    </base-config>
</network-security-config>
```

**Certificate Pinning:**
```kotlin
// OkHttp Certificate Pinning
val certificatePinner = CertificatePinner.Builder()
    .add("api.example.com", "sha256/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=")
    .build()

val client = OkHttpClient.Builder()
    .certificatePinner(certificatePinner)
    .build()
```

## Code Protection

### Obfuscation

**Android (ProGuard/R8):**
```proguard
# proguard-rules.pro
-keep class com.example.app.models.** { *; }
-keepclassmembers class * {
    @com.google.gson.annotations.SerializedName <fields>;
}
-dontwarn okhttp3.**
```

**iOS (SwiftShield):**
```bash
swiftshield -automatic -project-root /path/to/project
```

### Root/Jailbreak Detection

**Android:**
```kotlin
fun isDeviceRooted(): Boolean {
    val paths = arrayOf(
        "/system/app/Superuser.apk",
        "/sbin/su",
        "/system/bin/su",
        "/system/xbin/su"
    )
    return paths.any { File(it).exists() }
}
```

**iOS:**
```swift
func isJailbroken() -> Bool {
    let paths = [
        "/Applications/Cydia.app",
        "/Library/MobileSubstrate/MobileSubstrate.dylib",
        "/bin/bash",
        "/usr/sbin/sshd",
        "/etc/apt"
    ]
    return paths.contains { FileManager.default.fileExists(atPath: $0) }
}
```

### Anti-Debugging

**Android:**
```kotlin
fun isDebuggerAttached(): Boolean {
    return Debug.isDebuggerConnected() || Debug.waitingForDebugger()
}
```

## Secure Network Communication

### Best Practices

1. **Use HTTPS exclusively**
2. **Implement certificate pinning**
3. **Validate SSL certificates**
4. **Use strong TLS versions (TLS 1.2+)**
5. **Disable insecure cipher suites**
6. **Implement timeout policies**
7. **Validate server responses**

### API Security

**Authentication:**
- Use OAuth 2.0 / OpenID Connect
- Implement API key rotation
- Use short-lived access tokens
- Implement refresh token mechanism

**Authorization:**
- Validate permissions on backend
- Implement role-based access control (RBAC)
- Never trust client-side authorization

## Secure Data Handling

### Sensitive Data

**What is Sensitive:**
- Passwords, PINs
- Authentication tokens
- Personal information (PII)
- Financial data
- Health data
- Location data

**Best Practices:**
- Encrypt at rest and in transit
- Minimize storage duration
- Clear from memory after use
- Don't log sensitive data
- Implement secure deletion
- Use secure storage APIs

### Logging

```kotlin
// ❌ Bad: Logging sensitive data
Log.d("Auth", "User password: $password")

// ✅ Good: No sensitive data in logs
Log.d("Auth", "Authentication attempt")

// Disable logging in production
if (BuildConfig.DEBUG) {
    Log.d("Debug", "Debug info")
}
```

## Security Testing

### Static Analysis

**Tools:**
- **Android:** Android Lint, FindBugs, SonarQube
- **iOS:** Xcode Static Analyzer, SwiftLint
- **Cross-platform:** MobSF (Mobile Security Framework)

### Dynamic Analysis

**Tools:**
- **Android:** Frida, Drozer
- **iOS:** Frida, Objection
- **Network:** Burp Suite, OWASP ZAP, Charles Proxy

### Penetration Testing

**OWASP MASTG (Mobile Application Security Testing Guide):**
- Comprehensive testing methodology
- Platform-specific test cases
- Tools and techniques

### Automated Security Scanning

- Integrate security scanning in CI/CD
- Use tools like Snyk, WhiteSource, Checkmarx
- Scan dependencies for vulnerabilities

## Compliance and Standards

### OWASP MASVS (Mobile Application Security Verification Standard)

**Levels:**
- **MASVS-L1:** Standard security (all apps)
- **MASVS-L2:** Defense in depth (apps handling sensitive data)
- **MASVS-R:** Resiliency against reverse engineering

### Regulatory Compliance

- **GDPR:** EU data protection
- **CCPA:** California privacy law
- **HIPAA:** Health data (US)
- **PCI DSS:** Payment card data
- **SOC 2:** Security controls

## Best Practices Summary

1. **Follow OWASP Mobile Top 10**
2. **Encrypt sensitive data** (at rest and in transit)
3. **Implement secure authentication** (MFA, biometrics)
4. **Use HTTPS exclusively** with certificate pinning
5. **Validate all input** and sanitize output
6. **Obfuscate code** and implement anti-tampering
7. **Minimize permissions** and data collection
8. **Keep dependencies updated**
9. **Conduct regular security testing**
10. **Implement security in SDLC** (not as afterthought)

## Using the Reference Files

**`/references/owasp-mobile-top-10.md`** — Read for detailed explanations of each OWASP Mobile Top 10 vulnerability with examples and mitigations.

**`/references/secure-coding-practices.md`** — Read when implementing secure coding patterns, handling sensitive data, or following platform-specific security guidelines.

**`/references/security-testing-guide.md`** — Read when conducting security testing, using security tools, or implementing security in CI/CD.

## References

- [Compliance Guide](references/compliance-guide.md)
- [Owasp Mobile Top 10](references/owasp-mobile-top-10.md)
- [Secure Coding Practices](references/secure-coding-practices.md)
- [Security Testing Guide](references/security-testing-guide.md)
