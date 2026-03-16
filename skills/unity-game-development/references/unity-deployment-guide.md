# Unity Deployment and Platform Guide

Comprehensive guide to building and deploying Unity games across multiple platforms.

---

## Platform Build Overview

Unity supports 20+ platforms with a single codebase. Each platform has specific requirements, optimization needs, and deployment processes.

### Supported Platforms

| Category | Platforms |
|----------|----------|
| Desktop | Windows, macOS, Linux |
| Mobile | iOS, Android |
| Console | PlayStation 4/5, Xbox One/Series X|S, Nintendo Switch |
| Web | WebGL |
| VR/AR | Meta Quest, PlayStation VR, HoloLens, ARKit, ARCore |
| Other | tvOS, Stadia (deprecated) |

---

## Build Settings Configuration

### Accessing Build Settings

1. File > Build Settings
2. Select target platform
3. Click "Switch Platform" (recompiles assets)
4. Configure platform-specific settings
5. Click "Build" or "Build and Run"

### Player Settings

Edit > Project Settings > Player

**Common Settings Across Platforms:**
- Company Name
- Product Name
- Version
- Default Icon
- Default Cursor
- Splash Screen

---

## Windows / macOS / Linux Deployment

### Standalone Build Settings

**Windows:**
```
Architecture: x86_64 (64-bit)
Scripting Backend: IL2CPP (better performance) or Mono (faster builds)
API Compatibility Level: .NET Standard 2.1
```

**macOS:**
```
Architecture: Apple Silicon, Intel 64-bit, or Universal
Target macOS Version: 10.13+ recommended
Camera/Microphone Usage: Add descriptions for permissions
```

**Linux:**
```
Architecture: x86_64
Scripting Backend: IL2CPP or Mono
```

### Build Optimization

**Code Stripping:**
- Low: Minimal stripping, larger builds
- Medium: Balanced (recommended)
- High: Aggressive stripping, smallest builds (may break reflection)

**Managed Stripping Level:**
Player Settings > Other Settings > Managed Stripping Level

### Distribution

**Windows:**
- Standalone executable (.exe)
- Steam, Epic Games Store, itch.io, GOG
- Installer creation: Inno Setup, NSIS

**macOS:**
- .app bundle
- Code signing required for distribution
- Notarization required for macOS 10.15+
- Distribution: Mac App Store, Steam, itch.io

**Linux:**
- Executable binary
- Distribution: Steam, itch.io, Snap, Flatpak

---

## iOS Deployment

### Requirements

- Mac computer with Xcode installed
- Apple Developer account ($99/year)
- iOS device for testing (recommended)

### Build Process

1. **Unity Build Settings:**
   ```
   Platform: iOS
   Run in Xcode: Latest Release
   Symlink Unity libraries: Enable (faster builds)
   ```

2. **Player Settings:**
   ```
   Bundle Identifier: com.yourcompany.gamename
   Version: 1.0
   Build Number: 1 (increment for each upload)
   Minimum iOS Version: 12.0+ recommended
   Target SDK: Device SDK
   Architecture: ARM64
   ```

3. **Build to Xcode Project:**
   - Build Settings > Build
   - Select output folder
   - Unity generates Xcode project

4. **Xcode Configuration:**
   - Open .xcodeproj in Xcode
   - Select development team
   - Configure signing & capabilities
   - Set deployment target
   - Build and run on device

### App Store Submission

1. **App Store Connect:**
   - Create app listing
   - Add screenshots, description, keywords
   - Set pricing and availability

2. **Archive Build:**
   - Xcode > Product > Archive
   - Validate app
   - Distribute to App Store

3. **TestFlight:**
   - Beta testing platform
   - Upload build via Xcode
   - Invite testers via email

### iOS Optimization

**Graphics:**
- Use Metal graphics API
- Enable GPU Skinning
- Texture compression: ASTC
- Reduce draw calls to 50-100

**Performance:**
- Target 60 FPS on newer devices, 30 FPS on older
- Use URP for better performance
- Bake lighting where possible
- Limit realtime shadows

**Build Size:**
- Enable App Slicing (automatic per-device optimization)
- Use AssetBundles for downloadable content
- Compress audio (Vorbis)
- Reduce texture sizes

---

## Android Deployment

### Requirements

- Android SDK (installed via Unity Hub)
- JDK (Java Development Kit)
- Android device or emulator

### Build Settings

```
Texture Compression: ASTC (best quality) or ETC2 (compatibility)
Minimum API Level: Android 5.1 (API 22) or higher
Target API Level: Latest (required by Google Play)
Scripting Backend: IL2CPP (better performance, required for 64-bit)
Target Architectures: ARM64 (required), ARMv7 (optional for older devices)
```

### Player Settings

```
Package Name: com.yourcompany.gamename
Version: 1.0
Bundle Version Code: 1 (increment for each upload)
Install Location: Automatic
Write Permission: External (SD Card) if needed
```

### Keystore Creation

**Required for Google Play:**

1. Player Settings > Publishing Settings
2. Create new keystore:
   - Keystore password
   - Key alias
   - Key password
3. **IMPORTANT:** Backup keystore file (cannot recover if lost)

### Build Formats

**APK (Android Package):**
- Single file for all devices
- Larger file size
- Good for testing, sideloading

**AAB (Android App Bundle):**
- Google Play's preferred format
- Smaller downloads (device-specific APKs generated)
- Required for apps over 150MB
- Build Settings > Build App Bundle (Google Play)

### Google Play Submission

1. **Google Play Console:**
   - Create app listing
   - Add screenshots, description, category
   - Set content rating
   - Add privacy policy URL

2. **Upload Build:**
   - Production, Beta, or Alpha track
   - Upload AAB file
   - Set version details

3. **Release:**
   - Review and publish
   - Rollout percentage (gradual release)

### Android Optimization

**Graphics:**
- Use Vulkan or OpenGL ES 3
- Texture compression: ASTC or ETC2
- Reduce draw calls to 50-100
- Use URP

**Performance:**
- Target 60 FPS on high-end, 30 FPS on mid-range
- Test on multiple devices (various chipsets)
- Use Android Profiler

**Build Size:**
- Use AAB for automatic optimization
- Compress audio (Vorbis)
- Reduce texture quality for mobile
- Enable code stripping

---

## WebGL Deployment

### Build Settings

```
Compression Format: Gzip (best compatibility) or Brotli (smaller)
Memory Size: 256MB-2GB (depends on game)
Enable Exceptions: None (smallest build)
Code Optimization: Runtime Speed (faster) or Size (smaller)
```

### Player Settings

```
WebGL Template: Default, Minimal, or Custom
Color Space: Linear (better visuals) or Gamma (compatibility)
```

### Build Output

```
Build/
├── index.html
├── Build/
│   ├── game.data.gz
│   ├── game.framework.js.gz
│   ├── game.loader.js
│   └── game.wasm.gz
└── TemplateData/
```

### Hosting Requirements

**Web Server Configuration:**
- Serve .gz files with correct MIME types
- Enable CORS if loading external assets
- HTTPS recommended for full features

**MIME Types (.htaccess for Apache):**
```apache
AddType application/octet-stream .data.gz
AddType application/wasm .wasm.gz
AddType application/javascript .js.gz
AddEncoding gzip .gz
```

### Hosting Platforms

- **itch.io:** Free, easy WebGL hosting
- **GitHub Pages:** Free static hosting
- **Netlify/Vercel:** Free tier available
- **Simmer.io:** Game-specific hosting
- **Custom server:** Full control

### WebGL Limitations

**Not Supported:**
- Multithreading
- Sockets (use WebSockets instead)
- Native plugins
- Some video formats

**Performance:**
- Slower than native platforms
- Limited memory (browser dependent)
- No access to file system
- Mobile WebGL performance varies

### WebGL Optimization

**Build Size:**
- Enable code stripping (High)
- Use Brotli compression
- Reduce texture sizes
- Compress audio aggressively
- Target 50-100MB total build size

**Performance:**
- Reduce draw calls to 50-100
- Use URP
- Bake lighting
- Limit particle effects
- Optimize shaders for WebGL

---

## Console Deployment

### Platform Requirements

**General:**
- Approved developer status with platform holder
- Development kit hardware
- Platform-specific SDK
- NDA and licensing agreements

**PlayStation:**
- PlayStation Partners program
- PS4/PS5 DevKit
- PlayStation SDK

**Xbox:**
- ID@Xbox or Xbox Partner program
- Xbox DevKit or retail console (with Dev Mode)
- GDK (Game Development Kit)

**Nintendo Switch:**
- Nintendo Developer Portal access
- Switch DevKit
- Nintendo SDK

### Certification Process

1. **Technical Requirements:**
   - Platform-specific TRCs/TCRs (Technical Requirements Checklist)
   - Performance targets (frame rate, load times)
   - Memory limits
   - Controller support
   - Suspend/resume handling

2. **Submission:**
   - Upload build to platform portal
   - Submit for certification
   - Address any failures
   - Resubmit if needed

3. **Release:**
   - Set release date
   - Configure store listing
   - Pricing and regions

### Console Optimization

**Performance Targets:**
- 60 FPS for action games
- 30 FPS minimum for all games
- Stable frame rate (no drops)

**Graphics:**
- Use platform-specific graphics APIs
- Leverage hardware features (ray tracing on PS5/Xbox Series X)
- Optimize for fixed hardware

---

## VR/AR Deployment

### VR Platforms

**Meta Quest (Standalone):**
- Android-based build
- Oculus SDK integration
- Submit to Meta Quest Store

**PC VR (SteamVR, Oculus Rift):**
- Windows build
- OpenXR or platform-specific SDK
- Distribute via Steam, Oculus Store

**PlayStation VR:**
- PlayStation build with VR support
- PlayStation VR SDK

### AR Platforms

**ARKit (iOS):**
- iOS build with ARKit support
- Requires A9 chip or newer

**ARCore (Android):**
- Android build with ARCore support
- Requires ARCore-compatible device

**HoloLens:**
- UWP (Universal Windows Platform) build
- Mixed Reality Toolkit (MRTK)

### VR/AR Optimization

**Performance:**
- Target 72-90 FPS (VR sickness prevention)
- Minimize latency
- Use foveated rendering if available
- Optimize for mobile (Quest)

**Design:**
- Comfort settings (teleport, snap turning)
- UI design for 3D space
- Hand tracking or controller support

---

## Build Automation

### Unity Cloud Build

**Features:**
- Automated builds on commit
- Multi-platform builds
- Build history and versioning
- Distribution to testers

**Setup:**
1. Unity Dashboard > Cloud Build
2. Connect repository (GitHub, GitLab, Bitbucket)
3. Configure build targets
4. Set build triggers (manual, on commit, scheduled)

### Command Line Builds

```bash
# Windows
Unity.exe -quit -batchmode -projectPath "C:/MyProject" -buildWindows64Player "C:/Builds/MyGame.exe"

# macOS
/Applications/Unity/Unity.app/Contents/MacOS/Unity -quit -batchmode -projectPath "/Users/me/MyProject" -buildOSXUniversalPlayer "/Users/me/Builds/MyGame.app"

# Linux
/opt/Unity/Editor/Unity -quit -batchmode -projectPath "/home/user/MyProject" -buildLinux64Player "/home/user/Builds/MyGame"
```

### CI/CD Integration

**GitHub Actions:**
```yaml
name: Build Unity Project
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: game-ci/unity-builder@v2
        with:
          targetPlatform: StandaloneWindows64
```

**GitLab CI, Jenkins, CircleCI:**
Similar integrations available via Unity Build Automation.

---

## Post-Release Support

### Analytics Integration

- Unity Analytics (built-in)
- Google Analytics for Games
- Custom analytics solutions

**Track:**
- Player progression
- Crash reports
- Performance metrics
- Monetization events

### Update Strategies

**Patch Updates:**
- Bug fixes
- Minor improvements
- Increment build number

**Content Updates:**
- New levels, characters
- Use AssetBundles or Addressables
- Downloadable content (DLC)

**Major Updates:**
- New features
- Increment version number
- Marketing push

### Crash Reporting

- Unity Cloud Diagnostics
- Crashlytics (Firebase)
- Sentry
- Platform-specific tools (Xcode, Google Play Console)

---

## Common Build Issues

### Build Errors

**"Scripts have compiler errors"**
- Fix all script errors before building
- Check Console for details

**"Unable to parse Build/il2cppOutput/UnityClassRegistration.cpp"**
- IL2CPP build issue
- Try switching to Mono temporarily
- Update Unity version

**"Build failed with errors"**
- Check Editor.log for details
- Verify platform SDK installation

### Platform-Specific Issues

**iOS: "Code signing failed"**
- Verify Apple Developer account
- Check provisioning profiles
- Ensure correct Bundle Identifier

**Android: "Keystore not found"**
- Verify keystore path
- Check keystore password
- Ensure keystore file exists

**WebGL: "Out of memory"**
- Increase memory size in Player Settings
- Optimize assets
- Reduce build size

---

## Best Practices

### Version Control

- Use Git, Perforce, or Plastic SCM
- .gitignore for Unity projects:
  ```
  /Library/
  /Temp/
  /Obj/
  /Build/
  /Builds/
  *.apk
  *.unitypackage
  ```
- Commit before major builds
- Tag releases (v1.0, v1.1, etc.)

### Build Organization

```
Builds/
├── Windows/
│   ├── v1.0/
│   └── v1.1/
├── macOS/
├── Linux/
├── iOS/
├── Android/
└── WebGL/
```

### Testing

- Test on target devices, not just Editor
- Test all platforms before release
- Beta testing programs (TestFlight, Google Play Beta)
- QA checklist for each platform

### Documentation

- Build instructions for team members
- Platform-specific notes
- Known issues and workarounds
- Version history and changelogs

Deployment is a critical phase of game development. Plan ahead, test thoroughly, and follow platform guidelines for successful releases.