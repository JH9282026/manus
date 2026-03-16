# Mobile Automation with Appium

Guide to automating native, hybrid, and mobile web applications.

---

## Why Appium

- Cross-platform (iOS and Android)
- Native, hybrid, and web support
- Multiple languages
- No app modification needed
- Open source

---

## Setup

```bash
# Install Appium 2.0
npm install -g appium

# Install drivers
appium driver install xcuitest
appium driver install uiautomator2
```

---

## Desired Capabilities

### Android
```javascript
const capabilities = {
  platformName: 'Android',
  'appium:deviceName': 'Pixel 7',
  'appium:app': '/path/to/app.apk',
  'appium:automationName': 'UiAutomator2'
};
```

### iOS
```javascript
const capabilities = {
  platformName: 'iOS',
  'appium:deviceName': 'iPhone 14',
  'appium:app': '/path/to/app.ipa',
  'appium:automationName': 'XCUITest'
};
```

---

## Locator Strategies

### Accessibility ID (Recommended)
```javascript
await driver.$('~login-button').click();
```

### XPath
```javascript
await driver.$('//android.widget.Button[@text="Login"]').click();
```

### UIAutomator (Android)
```javascript
await driver.$('android=new UiSelector().text("Login")').click();
```

---

## Best Practices

1. Use Accessibility IDs
2. Implement explicit waits
3. Handle app states properly
4. Use cloud devices for scale
5. Implement parallel execution