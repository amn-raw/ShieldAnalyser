# Building True Native Applications

## 🎯 What's Different Now

**Before:**
- Mac app opened external browser
- Android required Termux (terminal-based)

**Now:**
- Mac app has **embedded webview** (true native app)
- Android builds as **native APK** (installable from file)

---

## 🍎 Build Native Mac App (Embedded WebView)

### Prerequisites
```bash
pip install -r requirements_native.txt
```

### Build Command
```bash
python3 build_native_mac.py
```

### What You Get
- **File:** `dist/FaradayShieldAnalyser.app`
- **Size:** ~35 MB
- **Features:**
  - ✅ Native Mac window (no external browser!)
  - ✅ Embedded webview
  - ✅ True standalone application
  - ✅ Can be in Applications folder
  - ✅ Proper Mac app experience

### Usage
```bash
# Just double-click the app!
open dist/FaradayShieldAnalyser.app
```

**What happens:**
- App opens in its own window
- No external browser launches
- Clean, native Mac experience
- Looks like a professional Mac app

---

## 📱 Build Native Android APK

### Option 1: Using Buildozer (On Mac/Linux)

#### Install Buildozer
```bash
# Install dependencies
brew install autoconf automake libtool pkg-config
brew install sdl2 sdl2_image sdl2_ttf sdl2_mixer

# Install Buildozer
pip3 install buildozer cython
```

#### Build APK
```bash
# Initialize (first time only)
buildozer init

# Build debug APK
buildozer -v android debug

# Build release APK
buildozer android release
```

**Output:**
- **File:** `bin/shieldanalyser-1.0.0-arm64-v8a-debug.apk`
- **Size:** ~20-30 MB
- **Install:** Transfer to phone and install

#### Install on Phone
1. Transfer APK to phone (email, USB, etc.)
2. On phone: Settings → Security → Allow Unknown Sources
3. Tap the APK file
4. Tap "Install"
5. Done! App appears in app drawer

---

### Option 2: Using BeeWare Briefcase (Easier)

#### Install Briefcase
```bash
pip3 install briefcase
```

#### Create Android Project
```bash
# Create project
briefcase create android

# Build APK
briefcase build android

# Package APK
briefcase package android

# Or do all at once
briefcase package android
```

**Output:**
- **File:** `android/FaradayShieldAnalyser/app/build/outputs/apk/debug/app-debug.apk`
- **Size:** ~25 MB

---

### Option 3: Using Python for Android (Advanced)

```bash
# Install p4a
pip3 install python-for-android

# Build APK
p4a apk --private . \
    --package=com.shieldanalyser.app \
    --name="Shield Analyser" \
    --version=1.0.0 \
    --bootstrap=sdl2 \
    --requirements=python3,kivy,fastapi,uvicorn,pandas \
    --permission=INTERNET \
    --permission=WRITE_EXTERNAL_STORAGE \
    --orientation=portrait
```

---

## 🚀 Quick Start

### For Mac Native App

```bash
# 1. Install dependencies
pip3 install -r requirements_native.txt

# 2. Build the app
python3 build_native_mac.py

# 3. Test it
open dist/FaradayShieldAnalyser.app

# Result: Native Mac window opens (no browser!)
```

### For Android APK (Easiest Method)

```bash
# 1. Install Briefcase
pip3 install briefcase

# 2. Build APK
briefcase package android

# 3. Find APK in android/FaradayShieldAnalyser/app/build/outputs/apk/

# 4. Transfer to phone and install
```

---

## 📊 Comparison

| Feature | Browser-Based | Native App |
|---------|---------------|------------|
| **Mac Experience** | External browser | Native window |
| **Android Install** | Requires Termux | Standard APK |
| **User Experience** | Web app feel | True native app |
| **Distribution** | ZIP file | APP/APK file |
| **Installation** | Extract & run | Double-click/Install |
| **App Icon** | No | Yes |
| **Offline** | Yes | Yes |
| **Auto-update** | Manual | Can add |

---

## 🎨 Native App Features

### Mac Native App
- ✅ Standalone window
- ✅ Native title bar
- ✅ Resizable
- ✅ Fullscreen support
- ✅ Dock icon
- ✅ Cmd+Q to quit
- ✅ Mac keyboard shortcuts
- ✅ Can be in Applications folder
- ✅ Launch at login (optional)

### Android Native APK
- ✅ App drawer icon
- ✅ Standard install process
- ✅ Android permissions
- ✅ Back button support
- ✅ Recent apps integration
- ✅ Notifications (can add)
- ✅ Google Play compatible
- ✅ Auto-start on boot (optional)

---

## 🐛 Troubleshooting

### Mac Build Issues

**Error: "pywebview not found"**
```bash
pip3 install pywebview
```

**Error: "Webview failed to start"**
```bash
# Install webkit dependencies
brew install python-tk
```

**Black window / blank screen**
- Wait 2-3 seconds for server to start
- Check console for errors

### Android Build Issues

**Error: "buildozer: command not found"**
```bash
pip3 install buildozer
```

**Error: "NDK not found"**
```bash
# Buildozer will download automatically on first build
# Just wait...
```

**APK won't install on phone**
- Enable "Unknown Sources" in Settings → Security
- Make sure APK is fully downloaded
- Try debug APK first, then release

**App crashes on Android**
- Check Android version (min API 21 / Android 5.0)
- Ensure all permissions granted
- Check logcat for errors: `adb logcat | grep python`

---

## 📦 Distribution

### Mac Native App

**As-is:**
- Share the .app file
- Users drag to Applications
- Done!

**DMG Installer:**
```bash
hdiutil create -volname "Faraday Shield Analyser" \
    -srcfolder dist/FaradayShieldAnalyser.app \
    -ov -format UDZO FaradayShieldAnalyser.dmg
```

**Code Signing (for distribution):**
```bash
codesign --force --deep --sign "Developer ID" \
    dist/FaradayShieldAnalyser.app
```

### Android APK

**Direct Install:**
- Transfer APK to phone
- Install from file manager
- Done!

**Google Play Store:**
1. Build release APK
2. Sign with keystore
3. Upload to Play Console
4. Submit for review

**F-Droid:**
1. Open source your code
2. Submit to F-Droid
3. Auto-builds and distributes

---

## 🎯 Recommended Approach

### For Mac Users:
```bash
python3 build_native_mac.py
```
**Result:** True native Mac app with embedded webview

### For Android Users:
```bash
pip3 install briefcase
briefcase package android
```
**Result:** Standard APK file

---

## ✨ What Users Get

### Mac App
1. Download `FaradayShieldAnalyser.app`
2. Drag to Applications
3. Double-click to open
4. **Native window opens** (not browser!)
5. Start analyzing

### Android App
1. Download `shieldanalyser.apk`
2. Tap to install
3. Tap app icon
4. **Native Android app opens**
5. Start analyzing

---

## 🎉 Benefits of Native Apps

**Professional:**
- Looks like real software
- App store compatible
- Better user trust

**User Experience:**
- No browser needed
- Feels native
- Familiar interface
- Standard app behavior

**Distribution:**
- Easy to share
- Standard install
- Version management
- Auto-update capable

---

## 📝 Next Steps

1. **Build native Mac app:**
   ```bash
   python3 build_native_mac.py
   ```

2. **Test it:**
   ```bash
   open dist/FaradayShieldAnalyser.app
   ```

3. **Build Android APK:**
   ```bash
   briefcase package android
   ```

4. **Distribute:**
   - Share .app for Mac
   - Share .apk for Android

---

**You now have TRUE native applications! 🎉**

