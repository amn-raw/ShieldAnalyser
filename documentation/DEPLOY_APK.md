# 📱 Deploy Android APK - Complete Guide

## 🎯 You've Chosen: Real APK Build

Great choice! Here's how to build a professional Android APK using GitHub Actions (cloud build).

---

## 🚀 Quick Start (5 Steps)

### Step 1: Create GitHub Repository

```bash
cd /Users/aman.raw/Desktop/ShieldAnalyser

# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - Faraday Shield Analyser"
```

### Step 2: Create GitHub Repo

**Option A: Using GitHub CLI**
```bash
# Install GitHub CLI if needed
brew install gh

# Login
gh auth login

# Create repo
gh repo create FaradayShieldAnalyser --public --source=. --remote=origin --push
```

**Option B: Using Website**
1. Go to https://github.com/new
2. Repository name: `FaradayShieldAnalyser`
3. Make it Public
4. Don't initialize with README (you have files)
5. Click "Create repository"
6. Follow commands shown:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/FaradayShieldAnalyser.git
   git branch -M main
   git push -u origin main
   ```

### Step 3: Wait for Build

1. Go to your GitHub repository
2. Click "Actions" tab
3. You'll see "Build Android APK" running
4. Wait 20-30 minutes (first build takes longer)
5. Watch progress in real-time!

### Step 4: Download APK

Once build completes:

**Method 1: From Actions Artifacts**
1. Click on the completed workflow
2. Scroll down to "Artifacts"
3. Download "package"
4. Extract ZIP
5. You have your APK!

**Method 2: From Releases**
1. Go to "Releases" tab
2. Latest release will have APK attached
3. Download `shieldanalyser-1.0.0-arm64-v8a-debug.apk`

### Step 5: Install on Phone

1. Transfer APK to your Android phone
2. On phone: Settings → Security → Enable "Unknown Sources"
3. Open file manager
4. Tap the APK
5. Tap "Install"
6. Done! App appears in app drawer

---

## 📋 What Gets Built

**File:** `shieldanalyser-1.0.0-arm64-v8a-debug.apk`
**Size:** ~25-30 MB
**Architectures:** arm64-v8a, armeabi-v7a
**Min Android:** 5.0 (API 21)
**Target Android:** 12.0 (API 31)

**Features:**
- ✅ Native Android app
- ✅ App drawer icon
- ✅ Installable from file
- ✅ All features working
- ✅ Offline capable
- ✅ Professional UI

---

## 🔧 Customizing the Build

### Change App Name

Edit `buildozer.spec`:
```ini
title = Your Custom Name
```

### Change Package Name

Edit `buildozer.spec`:
```ini
package.name = yourappname
package.domain = com.yourcompany
```

### Change Icon

Replace `icon.png` with your own 512x512 PNG

### Change Version

Edit `buildozer.spec`:
```ini
version = 1.0.1
```

---

## 🎨 The Build Process

```
GitHub Actions Workflow
         ↓
   Ubuntu VM Starts
         ↓
   Installs Dependencies
   (Python, Java, Android SDK/NDK)
         ↓
   Runs Buildozer
         ↓
   Compiles Python to Android
         ↓
   Packages into APK
         ↓
   Uploads Artifact
         ↓
   Creates Release
```

**Time:** 
- First build: 25-30 minutes
- Subsequent builds: 15-20 minutes (cached)

---

## 🐛 Troubleshooting

### Build Fails

**Check workflow logs:**
1. Go to Actions tab
2. Click failed workflow
3. Expand steps to see errors

**Common issues:**

**Issue: "buildozer.spec not found"**
- Make sure you pushed buildozer.spec file
- Check file is in root directory

**Issue: "Permission denied"**
- GitHub Actions has all needed permissions
- No action needed from you

**Issue: "Build timeout"**
- First build can take 30+ minutes
- Be patient, it's compiling everything

### APK Won't Install

**"App not installed"**
- Enable Unknown Sources in Settings
- Make sure APK fully downloaded
- Try debug APK first (then release)

**"Parse error"**
- Downloaded file may be corrupted
- Download again
- Make sure it's the .apk file not .zip

### App Crashes

**Check Android version:**
- Minimum: Android 5.0
- Works best: Android 8.0+

**Check logs:**
```bash
# Connect phone to computer
adb logcat | grep python
```

---

## 📱 Testing Your APK

### Before Distribution

Test on:
- [ ] Your phone
- [ ] Different Android version (friend's phone)
- [ ] Low-end device (if possible)
- [ ] Tablet (if targeting tablets)

### What to Test

- [ ] App installs successfully
- [ ] Icon appears in app drawer
- [ ] App opens without crashing
- [ ] Login works
- [ ] Can create experiment
- [ ] Can view charts
- [ ] Can save data
- [ ] Data persists after restart
- [ ] Can download Excel

---

## 🚀 Advanced: Build Release APK

For production/distribution, build a signed release APK:

### Step 1: Create Keystore

```bash
keytool -genkey -v -keystore my-release-key.keystore \
    -alias my-key-alias -keyalg RSA -keysize 2048 -validity 10000
```

### Step 2: Update buildozer.spec

```ini
[app]
# ... other settings ...

# (str) The Android arch to build for (choices: armeabi-v7a, arm64-v8a, x86, x86_64)
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
# ... other settings ...
```

### Step 3: Update GitHub Workflow

Add to `.github/workflows/build-android.yml`:

```yaml
- name: Sign APK
  run: |
    jarsigner -verbose -sigalg SHA256withRSA -digestalg SHA-256 \
      -keystore my-release-key.keystore \
      -storepass ${{ secrets.KEYSTORE_PASSWORD }} \
      bin/*.apk my-key-alias
```

### Step 4: Add Secret to GitHub

1. Go to repository Settings
2. Secrets and variables → Actions
3. New repository secret
4. Name: `KEYSTORE_PASSWORD`
5. Value: your keystore password

---

## 📊 Build Status

After pushing to GitHub:

```
✅ Workflow triggered
⏳ Building... (20-30 min)
✅ APK ready!
📦 Download from Artifacts or Releases
```

Check status anytime:
- GitHub → Actions tab
- Green checkmark = Success!
- Red X = Failed (check logs)
- Yellow dot = In progress

---

## 🎉 Distribution Options

### Direct Distribution
- Share APK file
- Users install manually
- No Google account needed
- Free!

### Google Play Store
1. Build signed release APK
2. Create Google Play developer account ($25 one-time)
3. Upload APK
4. Fill store listing
5. Submit for review
6. Published!

### F-Droid (Open Source)
1. Make code public
2. Submit to F-Droid
3. They build and host
4. Free for open source apps

### Own Website
1. Upload APK to your website
2. Provide download link
3. Users download and install
4. Add update notifications

---

## 📝 Post-Build Checklist

After successful build:

- [ ] Download APK
- [ ] Install on your phone
- [ ] Test all features
- [ ] Check app icon
- [ ] Verify app name
- [ ] Test on another device
- [ ] Share with beta testers
- [ ] Gather feedback
- [ ] Fix any issues
- [ ] Build release version
- [ ] Ready to distribute!

---

## 🎯 Expected Timeline

```
Now: Push to GitHub
↓ (2 min)
Build starts automatically
↓ (25 min first time)
Build completes
↓ (1 min)
APK available in Artifacts/Releases
↓ (2 min)
Download APK
↓ (1 min)
Transfer to phone
↓ (1 min)
Install
↓
Ready to use!

Total: ~30 minutes
```

---

## 💡 Pro Tips

### Faster Builds
- Buildozer caches dependencies
- Second build: ~15 minutes
- Use same branch for faster builds

### Multiple Versions
- Tag releases: v1.0, v1.1, etc.
- Keep APKs of each version
- Users can download specific version

### Automated Updates
- Push to main branch
- APK builds automatically
- Download latest from Releases
- Users install over existing app

### Beta Testing
- Share debug APK first
- Get feedback
- Fix issues
- Release signed APK

---

## 🆘 Need Help?

**Build Issues:**
- Check GitHub Actions logs
- Read error messages
- Google the error
- Ask in GitHub Issues

**Installation Issues:**
- Check Android version (min 5.0)
- Enable Unknown Sources
- Redownload APK
- Try on different device

**App Issues:**
- Check adb logcat
- Test on multiple devices
- Report bugs with details

---

## 🎉 You're Almost There!

**Next steps:**

1. **Push to GitHub** (Step 1-2 above)
2. **Wait for build** (~25 min)
3. **Download APK**
4. **Install on phone**
5. **Test and enjoy!**

---

**Ready? Let's push to GitHub!**

```bash
cd /Users/aman.raw/Desktop/ShieldAnalyser
git add .
git commit -m "Ready for APK build"
# Then create GitHub repo and push
```

After that, just wait for the magic to happen! ✨

---

**Questions? Check the GitHub Actions tab to see build progress in real-time!**

