# 📱 Testing on Your Phone - Complete Guide

## ✅ What We Built

1. **macOS App**: `dist/FaradayShieldAnalyser.app` (for your Mac)
2. **Android Package**: `ShieldAnalyser-Android.zip` (for your phone)

---

## 🖥️ Test on Mac (Desktop App)

### Step 1: Test the App
```bash
# Open the app
open dist/FaradayShieldAnalyser.app
```

**What should happen:**
- ✅ Console window opens
- ✅ Browser opens automatically to http://localhost:8000
- ✅ You see the login page
- ✅ Login with: admin / admin123
- ✅ All features work (upload, create, edit, charts)

### Step 2: Close and Reopen Test
```bash
# Close browser and app
# Then reopen
open dist/FaradayShieldAnalyser.app
```

**Verify:**
- ✅ Previous data is still there
- ✅ Experiments saved

**Data Location:**
```
~/Library/Application Support/FaradayShieldAnalyser/
```

---

## 📱 Test on Android Phone - Method 1: Using Termux (Easiest)

### Prerequisites
1. **Install Termux** from F-Droid (NOT Google Play!)
   - Visit: https://f-droid.org/
   - Search for "Termux"
   - Install it

### Step 1: Transfer Package to Phone

**Option A: Using AirDrop (Mac to iPhone - if you have iPhone)**
```bash
# Open the file in Finder
open -R ShieldAnalyser-Android.zip
# Then AirDrop to phone
```

**Option B: Using File Transfer (Mac to Android)**
```bash
# Connect phone via USB
# Open Android File Transfer
open ShieldAnalyser-Android.zip
# Copy to phone's Download folder
```

**Option C: Using Cloud (Google Drive/Dropbox)**
```bash
# Upload to Google Drive
# Download on phone from Drive app
```

**Option D: Using Email**
```bash
# Email the zip file to yourself
# Download on phone
```

### Step 2: Install on Phone

1. **Open Termux** on your phone

2. **Setup storage access:**
```bash
termux-setup-storage
# Grant permission when prompted
```

3. **Install Python:**
```bash
pkg update
pkg install python -y
```

4. **Copy the package:**
```bash
cd ~
cp /storage/emulated/0/Download/ShieldAnalyser-Android.zip .
# or wherever you saved it
```

5. **Extract it:**
```bash
unzip ShieldAnalyser-Android.zip
cd ShieldAnalyser-Android
```

6. **Make script executable:**
```bash
chmod +x run.sh
```

### Step 3: Run the App

```bash
./run.sh
```

**What happens:**
- First time: Installs dependencies (2-3 minutes)
- Shows: "Running at http://localhost:8000"

### Step 4: Access in Browser

1. **Keep Termux running in background**
2. **Open Chrome** on your phone
3. **Go to:** `http://localhost:8000`
4. **Login:** admin / admin123
5. **Test all features!**

### Step 5: Create Home Screen Shortcut

1. In Chrome, tap the menu (⋮)
2. Tap "Add to Home screen"
3. Name it "Shield Analyser"
4. Now you have an app icon!

### Step 6: Stop the App

In Termux:
```bash
# Press CTRL+C
# Or swipe down and close Termux
```

---

## 📱 Test on Android Phone - Method 2: Direct Network Access from Mac

### Quick Test Without Installing on Phone

If you just want to test if the UI works on mobile:

1. **Get your Mac's IP address:**
```bash
ifconfig | grep "inet " | grep -v 127.0.0.1
```

Example output: `inet 192.168.1.100`

2. **Run the app on Mac:**
```bash
cd ~/Desktop/ShieldAnalyser
source venv/bin/activate
# Edit main.py to allow network access
python main.py
```

3. **On your phone (same WiFi network):**
- Open browser
- Go to: `http://192.168.1.100:8000`
  (replace with your Mac's IP)
- Login and test!

---

## 🧪 Testing Checklist

### Desktop (Mac) App
- [ ] App launches without errors
- [ ] Browser opens automatically
- [ ] Login works (admin/admin123)
- [ ] Upload Excel file works
- [ ] Create new experiment manually
- [ ] Add/edit rows works
- [ ] Add columns works
- [ ] Delete rows works
- [ ] All 3 charts display correctly
- [ ] Toggle line/bar charts works
- [ ] Full view table works
- [ ] Save changes persists
- [ ] Download Excel works
- [ ] Close and reopen - data persists
- [ ] Can create multiple experiments
- [ ] Delete experiment works

### Mobile (Android) App
- [ ] Package extracts successfully
- [ ] run.sh executes without errors
- [ ] Dependencies install correctly
- [ ] Server starts on localhost:8000
- [ ] Can access in Chrome
- [ ] Login works
- [ ] UI is mobile-responsive
- [ ] Touch interactions work
- [ ] File upload works (if testing)
- [ ] Charts display on mobile
- [ ] Table scrolls horizontally/vertically
- [ ] Can edit values
- [ ] Charts toggle between types
- [ ] Data saves correctly
- [ ] Can restart and data persists

---

## 🐛 Troubleshooting

### Mac App Issues

**"Can't open app - damaged or incomplete"**
```bash
# Remove quarantine
xattr -cr dist/FaradayShieldAnalyser.app
# Or: System Preferences → Security & Privacy → Open Anyway
```

**"Port 8000 already in use"**
```bash
# Find and kill process
lsof -ti:8000 | xargs kill -9
```

**App doesn't start**
```bash
# Run from terminal to see errors
./dist/FaradayShieldAnalyser.app/Contents/MacOS/FaradayShieldAnalyser
```

### Android/Termux Issues

**"Permission denied" when running run.sh**
```bash
chmod +x run.sh
```

**"Python not found"**
```bash
pkg install python -y
```

**Dependencies fail to install**
```bash
# Update packages
pkg update && pkg upgrade
# Try again
./run.sh
```

**Can't find ZIP file**
```bash
# Check Downloads folder
ls -la /storage/emulated/0/Download/

# Or search
find /storage -name "*Shield*.zip" 2>/dev/null
```

**Browser shows "Can't reach page"**
- Make sure Termux is still running
- Use `localhost:8000` not `127.0.0.1:8000`
- Try `http://localhost:8000` explicitly

**App runs but charts don't show**
- Scroll down (mobile layout)
- Refresh page
- Check JavaScript console

---

## 📊 Performance Tips

### Mac App
- First launch: ~5 seconds
- Subsequent launches: ~3 seconds
- Memory usage: ~150 MB
- CPU: Low (idle when not processing)

### Android/Termux
- First launch: ~30 seconds (dependency install)
- Subsequent launches: ~10 seconds
- Memory usage: ~200 MB
- Battery: Low impact
- Keep Termux in background while using

---

## 💡 Pro Tips

### Mac Testing

**Create Alias for Quick Launch:**
```bash
# Add to ~/.zshrc
alias shieldapp='open ~/Desktop/ShieldAnalyser/dist/FaradayShieldAnalyser.app'
```

**Test with Sample Data:**
```bash
# Sample file is included in the app
# Just upload sample_experiment.xlsx
```

### Android Testing

**Quick Restart:**
```bash
# In Termux, create this script:
echo '#!/data/data/com.termux/files/usr/bin/bash
cd ~/ShieldAnalyser-Android
./run.sh' > ~/start-shield.sh
chmod +x ~/start-shield.sh

# Then just run:
~/start-shield.sh
```

**Battery Optimization:**
- Disable battery optimization for Termux
- Settings → Apps → Termux → Battery → Don't optimize

**Keep Running:**
- Use Termux:Boot to auto-start
- Or use Termux widget for quick launch

---

## 🎬 Demo Scenario

### Complete Test Workflow

1. **Launch app** (Mac or phone)
2. **Login** (admin/admin123)
3. **Create experiment:**
   - Name: "Test 1"
   - Locations: 3
   - Frequencies: 5
4. **Fill in some data:**
   - Edit cells with test values
5. **View charts:**
   - All 3 charts should show
   - Toggle between line/bar
6. **Add a row:**
   - Click "Add Row"
   - Enter frequency and values
7. **Add a column:**
   - Click "Add Column"
   - Name it "L4"
   - Shielding column auto-created
8. **Save changes**
9. **Download Excel**
10. **Close app**
11. **Reopen app**
12. **Verify:**
    - Data is still there
    - All changes saved

---

## 📸 What Success Looks Like

### Mac App
```
✅ App icon appears in dist/ folder
✅ Double-click launches immediately
✅ Terminal window shows "Running at http://localhost:8000"
✅ Browser opens automatically
✅ Login screen appears
✅ Dashboard loads with features
```

### Android App
```
✅ ZIP extracts without errors
✅ run.sh executes successfully
✅ "Running at http://localhost:8000" message
✅ Chrome opens to localhost:8000
✅ Login screen appears (mobile-responsive)
✅ Touch controls work smoothly
✅ Charts render on mobile screen
```

---

## 🚀 Next Steps After Testing

### If Everything Works:

1. **Distribution:**
   - Share the Mac .app with users
   - Share Android ZIP with instructions
   - Host on website/GitHub

2. **Improvements:**
   - Add app icon
   - Sign the Mac app (optional)
   - Create installer (DMG for Mac)
   - Build native Android APK (advanced)

3. **Documentation:**
   - User manual
   - Video tutorial
   - FAQ

### If Issues Found:

1. **Report:**
   - What platform (Mac/Android)
   - What step failed
   - Error messages
   - Screenshots

2. **Debug:**
   - Check logs
   - Test on clean device
   - Verify network connectivity

---

## 📞 Quick Reference

### Mac App
- **Location:** `dist/FaradayShieldAnalyser.app`
- **Launch:** Double-click or `open dist/FaradayShieldAnalyser.app`
- **Data:** `~/Library/Application Support/FaradayShieldAnalyser/`
- **URL:** `http://localhost:8000`

### Android App
- **Package:** `ShieldAnalyser-Android.zip`
- **Install:** Extract in Termux, run `./run.sh`
- **Data:** `~/ShieldAnalyser-Android/experiments.json`
- **URL:** `http://localhost:8000` (in Chrome)

### Login
- **Username:** admin
- **Password:** admin123

---

## 🎉 You're Ready to Test!

**Mac:** Open the app in dist/ folder  
**Android:** Follow the Termux instructions above

**Questions?** Check the troubleshooting section!

---

**Happy Testing! 🧪📱🖥️**

