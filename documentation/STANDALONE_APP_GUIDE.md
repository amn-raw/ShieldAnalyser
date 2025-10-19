# Standalone Application Guide

## 🎯 Quick Start - Building Desktop Apps

### For Windows Users

```bash
# 1. Install dependencies
pip install -r requirements_app.txt

# 2. Build the executable
python build_app.py

# 3. Find your app
# Location: dist/FaradayShieldAnalyser.exe
# Size: ~80-120 MB
```

**Usage:**
- Double-click `FaradayShieldAnalyser.exe`
- Browser opens automatically
- Login: admin / admin123
- Data stored in: `%APPDATA%\FaradayShieldAnalyser\`

---

### For macOS Users

```bash
# 1. Install dependencies
pip3 install -r requirements_app.txt

# 2. Build the application
python3 build_app.py

# 3. Find your app
# Location: dist/FaradayShieldAnalyser.app
# Size: ~80-120 MB
```

**Usage:**
- Copy to Applications folder
- Double-click to launch
- Browser opens automatically
- Login: admin / admin123
- Data stored in: `~/Library/Application Support/FaradayShieldAnalyser/`

---

### For Linux Users

```bash
# 1. Install dependencies
pip3 install -r requirements_app.txt

# 2. Build the executable
python3 build_app.py

# 3. Find your app
# Location: dist/FaradayShieldAnalyser
# Size: ~80-120 MB
```

**Usage:**
```bash
chmod +x dist/FaradayShieldAnalyser
./dist/FaradayShieldAnalyser
```

---

## 📱 Android Options

### Option 1: Termux (Easiest)

1. **Install Termux** from F-Droid (https://f-droid.org/)

2. **Setup Python:**
```bash
pkg update
pkg install python
pip install fastapi uvicorn pandas openpyxl python-jose passlib python-multipart
```

3. **Transfer app to phone:**
   - Zip the ShieldAnalyser folder
   - Copy to phone
   - Extract in Termux home directory

4. **Run:**
```bash
cd ShieldAnalyser
python app_launcher.py
```

5. **Open in browser:**
   - Navigate to `http://localhost:8000`

### Option 2: Python for Android (Kivy)

Create native Android app:

```bash
# Install buildozer
pip install buildozer

# Create buildozer.spec
buildozer init

# Build APK
buildozer -v android debug
```

### Option 3: Progressive Web App (PWA)

Deploy to a web server, then:
1. Open in Chrome on Android
2. Tap menu → "Add to Home Screen"
3. Acts like native app

---

## 🎨 What You Get

### Standalone Desktop App Features

✅ **No Installation Required**
- Single executable file
- No Python needed
- No dependencies to install

✅ **Auto-Start Browser**
- Double-click exe/app
- Browser opens automatically
- No command line needed

✅ **Local Data Storage**
- All data stored locally
- Platform-specific locations
- Survives app restart

✅ **Portable**
- Run from USB drive
- No internet required
- Self-contained

✅ **All Features Included**
- Upload/create experiments
- Add/edit/delete data
- View charts (line/bar)
- Download Excel
- Multiple users

---

## 📊 How It Works

### Application Flow

```
1. User double-clicks executable
   ↓
2. App starts FastAPI server (localhost:8000)
   ↓
3. App opens default browser
   ↓
4. User sees login page
   ↓
5. All data saved to app directory
   ↓
6. On exit: Server stops, data persists
```

### Data Storage

**Windows:**
```
C:\Users\YourName\AppData\Roaming\FaradayShieldAnalyser\
├── experiments.json (your experiments)
└── creds.json (user accounts)
```

**macOS:**
```
/Users/YourName/Library/Application Support/FaradayShieldAnalyser/
├── experiments.json
└── creds.json
```

**Linux:**
```
/home/yourname/.local/share/FaradayShieldAnalyser/
├── experiments.json
└── creds.json
```

---

## 🔧 Advanced Build Options

### Custom Icon

1. Create icon file:
   - Windows: 256x256 .ico file
   - macOS: 1024x1024 .icns file
   - Linux: 512x512 .png file

2. Place in project folder as `icon.ico` (or .icns/.png)

3. Build will automatically include it

### No Console Window (Windows)

Edit `build_app.py`, change:
```python
'--console',  # Change to '--windowed'
```

### Smaller File Size

Use UPX compression:
```bash
# Install UPX
# Then PyInstaller will use it automatically
pip install pyinstaller --upgrade
```

---

## 📦 Distribution

### Windows

**Create Installer with NSIS:**

1. Download NSIS from https://nsis.sourceforge.io/
2. Create `installer.nsi`:

```nsis
!define APP_NAME "Faraday Shield Analyser"
!define COMP_NAME "Your Company"
!define VERSION "1.0.0"
!define INSTALLER_NAME "FaradayShieldAnalyser-Setup.exe"

OutFile "${INSTALLER_NAME}"
InstallDir "$PROGRAMFILES\${APP_NAME}"

Section "Install"
    SetOutPath "$INSTDIR"
    File "dist\FaradayShieldAnalyser.exe"
    CreateShortCut "$DESKTOP\${APP_NAME}.lnk" "$INSTDIR\FaradayShieldAnalyser.exe"
SectionEnd
```

3. Build installer:
```bash
makensis installer.nsi
```

### macOS

**Create DMG:**
```bash
hdiutil create -volname "Faraday Shield Analyser" -srcfolder dist/FaradayShieldAnalyser.app -ov -format UDZO FaradayShieldAnalyser.dmg
```

Users can:
- Mount DMG
- Drag app to Applications
- Launch from Applications

### Linux

**Create AppImage:**
```bash
# Install linuxdeploy
wget https://github.com/linuxdeploy/linuxdeploy/releases/download/continuous/linuxdeploy-x86_64.AppImage
chmod +x linuxdeploy-x86_64.AppImage

# Create AppImage
./linuxdeploy-x86_64.AppImage --appdir AppDir --executable dist/FaradayShieldAnalyser --create-desktop-file --output appimage
```

---

## 🧪 Testing Your Build

### Pre-Distribution Checklist

**Test on Clean System:**
- [ ] Install on computer without Python
- [ ] Double-click to launch
- [ ] Browser opens automatically
- [ ] Login works
- [ ] Upload sample Excel
- [ ] Create new experiment
- [ ] Add/edit data
- [ ] View charts
- [ ] Save changes
- [ ] Close app
- [ ] Reopen app
- [ ] Data is still there
- [ ] Download Excel works

**Test Scenarios:**
- [ ] Fresh install
- [ ] Upgrade from previous version
- [ ] Multiple users
- [ ] Large data files (1000+ rows)
- [ ] Network offline
- [ ] Anti-virus enabled
- [ ] Limited user permissions

---

## 🚀 Quick Build & Test

```bash
# 1. Build
python build_app.py

# 2. Test locally
cd dist
./FaradayShieldAnalyser  # or .exe on Windows

# 3. Verify browser opens
# 4. Test all features
# 5. Check data location
```

**Expected Results:**
- ✅ App starts in < 5 seconds
- ✅ Browser opens automatically
- ✅ No errors in console
- ✅ All features work
- ✅ Data persists after restart

---

## 📱 Android Deployment Guide

### Using Termux (Simplest)

**Step 1: Create Package**
```bash
# On your computer
cd ShieldAnalyser
zip -r ShieldAnalyser-Android.zip *.py *.json static/ sample_experiment.xlsx
```

**Step 2: Install on Android**
```bash
# On Android in Termux
pkg install python
pip install fastapi uvicorn pandas openpyxl python-jose passlib python-multipart
cd ~
# Copy zip to phone, then:
unzip ShieldAnalyser-Android.zip -d ShieldAnalyser
cd ShieldAnalyser
```

**Step 3: Create Shortcut**
```bash
# Create run script
echo 'cd ~/ShieldAnalyser && python app_launcher.py' > ~/run-shield-analyser.sh
chmod +x ~/run-shield-analyser.sh
```

**Step 4: Run**
```bash
~/run-shield-analyser.sh
# Open browser to localhost:8000
```

### Using Kivy (Native App)

**Step 1: Install Buildozer**
```bash
pip install buildozer
```

**Step 2: Create buildozer.spec**
```bash
buildozer init
```

**Step 3: Edit buildozer.spec**
```ini
[app]
title = Faraday Shield Analyser
package.name = shieldanalyser
package.domain = com.yourcompany
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,xlsx
requirements = python3,kivy,fastapi,uvicorn,pandas,openpyxl
```

**Step 4: Build**
```bash
buildozer -v android debug
```

**Step 5: Install**
```bash
buildozer android deploy run
```

---

## 💡 Tips & Tricks

### Tip 1: Portable Version

Create portable version that runs from USB:
1. Build executable
2. Copy to USB drive with folder structure
3. Include README with instructions
4. Users can run from any computer

### Tip 2: Auto-Update

Add update checker:
```python
def check_for_updates():
    # Check version from server
    # Download new version if available
    # Prompt user to update
```

### Tip 3: Backup Data

Add backup feature:
```python
def backup_data():
    # Copy experiments.json to backup folder
    # Include timestamp in filename
```

### Tip 4: Multi-Language

Add language support:
```python
# Add language selection
# Load translations from JSON
# Switch UI language
```

---

## 🐛 Common Issues & Solutions

### Issue: "Application can't be opened" (macOS)

**Solution:**
```bash
# Remove quarantine
xattr -cr FaradayShieldAnalyser.app

# Or: System Preferences → Security → Allow
```

### Issue: "Windows protected your PC"

**Solution:**
- Click "More info"
- Click "Run anyway"
- Or: Sign the executable with certificate

### Issue: "Port 8000 already in use"

**Solution:**
```python
# Edit app_launcher.py
uvicorn.run(app_main.app, host="127.0.0.1", port=8001)
```

### Issue: Data not saving

**Solution:**
```bash
# Check permissions
# Windows:
icacls "%APPDATA%\FaradayShieldAnalyser" /grant Users:F

# macOS/Linux:
chmod -R 755 ~/Library/Application\ Support/FaradayShieldAnalyser/
```

---

## 📊 File Sizes

| Platform | Size | Notes |
|----------|------|-------|
| Windows EXE | ~100 MB | Includes Python runtime |
| macOS APP | ~90 MB | Native app bundle |
| Linux Binary | ~95 MB | Static executable |
| Android APK | ~40 MB | With Kivy framework |
| Termux ZIP | ~2 MB | Requires Python on device |

---

## 🎉 You're Ready!

**Next Steps:**
1. Choose your platform
2. Run `python build_app.py`
3. Find executable in `dist/` folder
4. Test on clean system
5. Distribute to users!

**For Android:**
1. Use Termux method (easiest)
2. Or build native APK with Kivy
3. Or deploy as PWA

---

**Happy Building! 🚀📱🖥️**

