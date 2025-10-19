# Building Standalone Applications

## 📦 Overview

This guide shows you how to create standalone executables for Windows, macOS, and instructions for Android.

---

## 🪟 Windows Executable

### Prerequisites
```bash
pip install -r requirements_app.txt
```

### Build Steps

#### Option 1: Using Build Script (Recommended)
```bash
python build_app.py
```

#### Option 2: Manual Build
```bash
pyinstaller --clean --onefile --name=FaradayShieldAnalyser --add-data="static;static" --add-data="creds.json;." --add-data="sample_experiment.xlsx;." --hidden-import=uvicorn.logging --hidden-import=uvicorn.loops.auto --hidden-import=uvicorn.protocols.http.auto --hidden-import=uvicorn.protocols.websockets.auto --hidden-import=uvicorn.lifespan.on --hidden-import=passlib.handlers.bcrypt --console app_launcher.py
```

### Result
- Executable: `dist/FaradayShieldAnalyser.exe`
- Size: ~80-120 MB
- Data Storage: `%APPDATA%\FaradayShieldAnalyser\`

### Usage
1. Double-click `FaradayShieldAnalyser.exe`
2. App opens in your default browser automatically
3. Login with admin/admin123
4. All data saved to AppData folder

---

## 🍎 macOS Application

### Prerequisites
```bash
pip3 install -r requirements_app.txt
```

### Build Steps
```bash
python3 build_app.py
```

### Result
- Application: `dist/FaradayShieldAnalyser.app`
- Size: ~80-120 MB
- Data Storage: `~/Library/Application Support/FaradayShieldAnalyser/`

### Usage
1. Copy `FaradayShieldAnalyser.app` to Applications folder
2. Double-click to launch
3. App opens in your default browser
4. Login with admin/admin123

### Signing (Optional)
For distribution:
```bash
codesign --force --deep --sign "Developer ID Application: Your Name" dist/FaradayShieldAnalyser.app
```

---

## 🐧 Linux Executable

### Prerequisites
```bash
pip3 install -r requirements_app.txt
```

### Build Steps
```bash
python3 build_app.py
```

### Result
- Executable: `dist/FaradayShieldAnalyser`
- Size: ~80-120 MB
- Data Storage: `~/.local/share/FaradayShieldAnalyser/`

### Usage
```bash
chmod +x dist/FaradayShieldAnalyser
./dist/FaradayShieldAnalyser
```

---

## 📱 Android Application

### Option 1: Using Kivy (Recommended)

#### Install BeeWare Briefcase
```bash
pip install briefcase
```

#### Create Android Project
```bash
briefcase create android
briefcase build android
briefcase package android
```

### Option 2: Using Termux

Create a Termux-compatible package:

1. **Install Termux** from F-Droid
2. **Install Python in Termux:**
```bash
pkg install python
pip install fastapi uvicorn pandas openpyxl
```

3. **Copy app to Termux:**
```bash
# On your computer, create a zip
zip -r ShieldAnalyser.zip ShieldAnalyser/

# Transfer to phone and extract in Termux
cd ~
unzip ShieldAnalyser.zip
cd ShieldAnalyser
python app_launcher.py
```

### Option 3: Convert to React Native/Flutter

For a native Android experience, consider:
1. **React Native**: Convert frontend to React Native
2. **Flutter**: Rebuild with Flutter + Dart
3. **Ionic/Capacitor**: Wrap web app in native container

---

## 🌐 Web App (PWA) - Alternative for Android

### Convert to Progressive Web App

Add to `static/index.html`:

```html
<head>
    <link rel="manifest" href="/manifest.json">
    <meta name="theme-color" content="#667eea">
</head>
```

Create `static/manifest.json`:
```json
{
  "name": "Faraday Shield Analyser",
  "short_name": "Shield Analyser",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#ffffff",
  "theme_color": "#667eea",
  "icons": [
    {
      "src": "/icon-192.png",
      "sizes": "192x192",
      "type": "image/png"
    },
    {
      "src": "/icon-512.png",
      "sizes": "512x512",
      "type": "image/png"
    }
  ]
}
```

Deploy to web hosting, then:
1. Open on Android Chrome
2. Tap "Add to Home Screen"
3. App installs like native app

---

## 📊 Data Storage Locations

### Windows
```
%APPDATA%\FaradayShieldAnalyser\
├── experiments.json
└── creds.json
```

### macOS
```
~/Library/Application Support/FaradayShieldAnalyser/
├── experiments.json
└── creds.json
```

### Linux
```
~/.local/share/FaradayShieldAnalyser/
├── experiments.json
└── creds.json
```

### Android (Termux)
```
~/ShieldAnalyser/
├── experiments.json
└── creds.json
```

---

## 🔧 Customization

### Change App Icon

1. **Create icon file:**
   - Windows: `icon.ico` (256x256)
   - macOS: `icon.icns` (1024x1024)
   - Linux: `icon.png` (512x512)

2. **Add to build command:**
```bash
pyinstaller ... --icon=icon.ico ...
```

### Change App Name

Edit `app_launcher.py`:
```python
# Change directory names
app_dir = os.path.join(app_data, 'YourAppName')
```

### Remove Console Window (Windows)

Change in build command:
```bash
--windowed  # instead of --console
```

---

## 📦 Distribution

### Windows

**Option 1: Installer (NSIS)**
```bash
# Install NSIS
# Create installer script
makensis installer.nsi
```

**Option 2: Portable ZIP**
```bash
# Just zip the exe
zip FaradayShieldAnalyser-Windows.zip dist/FaradayShieldAnalyser.exe README.md
```

### macOS

**Option 1: DMG**
```bash
hdiutil create -volname "Faraday Shield Analyser" -srcfolder dist/FaradayShieldAnalyser.app -ov -format UDZO FaradayShieldAnalyser.dmg
```

**Option 2: PKG Installer**
```bash
productbuild --component dist/FaradayShieldAnalyser.app /Applications FaradayShieldAnalyser.pkg
```

### Linux

**Option 1: AppImage**
```bash
# Use linuxdeploy
linuxdeploy --appdir AppDir --executable dist/FaradayShieldAnalyser --create-desktop-file --output appimage
```

**Option 2: DEB Package**
```bash
# Create debian package structure
dpkg-deb --build faraday-shield-analyser
```

### Android

**Option 1: APK**
```bash
briefcase package android
# Output: android/FaradayShieldAnalyser-1.0.apk
```

**Option 2: Google Play**
1. Build signed APK/AAB
2. Upload to Google Play Console
3. Submit for review

---

## 🐛 Troubleshooting

### Build Fails - Missing Modules

**Solution:**
```bash
pip install --upgrade pip
pip install -r requirements_app.txt
```

### App Doesn't Start

**Windows:**
- Check Windows Defender/Antivirus
- Run as Administrator

**macOS:**
- System Preferences → Security → Allow app
- Remove quarantine: `xattr -cr FaradayShieldAnalyser.app`

**Linux:**
- Check permissions: `chmod +x FaradayShieldAnalyser`

### Port Already in Use

**Solution:** Edit `app_launcher.py`:
```python
uvicorn.run(app_main.app, host="127.0.0.1", port=8001)  # Change port
```

### Data Not Saving

**Check permissions:**
```bash
# Windows
icacls "%APPDATA%\FaradayShieldAnalyser" /grant Users:F

# macOS/Linux
chmod -R 755 ~/Library/Application\ Support/FaradayShieldAnalyser/
```

---

## 📏 Build Size Optimization

### Reduce Size

**Option 1: Use upx compression**
```bash
pyinstaller ... --upx-dir=/path/to/upx ...
```

**Option 2: Exclude unused modules**
```bash
pyinstaller ... --exclude-module matplotlib --exclude-module tkinter ...
```

**Option 3: Use python-slim**
```bash
# Build with minimal Python installation
```

---

## 🚀 Quick Build Commands

### Windows
```bash
python build_app.py
```

### macOS
```bash
python3 build_app.py
```

### Linux
```bash
python3 build_app.py
```

### Android (using Briefcase)
```bash
briefcase create android
briefcase build android
briefcase run android  # Test
briefcase package android  # Create APK
```

---

## 📝 Testing Checklist

- [ ] App launches without errors
- [ ] Browser opens automatically
- [ ] Login works
- [ ] Upload Excel file
- [ ] Create experiment manually
- [ ] Add/edit/delete rows
- [ ] Add columns
- [ ] Charts display correctly
- [ ] Save changes persist
- [ ] Download Excel works
- [ ] Data survives app restart
- [ ] Multiple users can login

---

## 🎉 Release Checklist

- [ ] Build all platforms
- [ ] Test on clean systems
- [ ] Create installers/packages
- [ ] Write release notes
- [ ] Update version numbers
- [ ] Sign executables (Windows/macOS)
- [ ] Create distribution packages
- [ ] Upload to distribution platforms
- [ ] Update documentation
- [ ] Announce release

---

**Ready to build! Choose your platform and run the build script. 🚀**

