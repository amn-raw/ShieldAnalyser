# Release Packaging Guide

## 📦 Creating Release Packages

This guide shows how to create distribution packages for all platforms.

---

## 🪟 Windows Release Package

### Build

```bash
# 1. Activate virtual environment
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 2. Build executable
python build_app.py

# Result: dist/FaradayShieldAnalyser.exe (~100 MB)
```

### Package for Distribution

**Option 1: Portable ZIP**
```bash
# Create release folder
mkdir -p release/FaradayShieldAnalyser-Windows
cp dist/FaradayShieldAnalyser.exe release/FaradayShieldAnalyser-Windows/
cp sample_experiment.xlsx release/FaradayShieldAnalyser-Windows/
cp README.md release/FaradayShieldAnalyser-Windows/

# Create zip
cd release
zip -r FaradayShieldAnalyser-Windows-v1.0.zip FaradayShieldAnalyser-Windows/
```

**Option 2: NSIS Installer**

Create `installer.nsi`:
```nsis
!define APP_NAME "Faraday Shield Analyser"
!define COMP_NAME "Your Company"
!define VERSION "1.0.0.0"
!define COPYRIGHT "Copyright © 2025"
!define DESCRIPTION "Faraday Shield Measurement Analysis"
!define INSTALLER_NAME "FaradayShieldAnalyser-Setup-v1.0.exe"
!define MAIN_APP_EXE "FaradayShieldAnalyser.exe"
!define INSTALL_TYPE "SetShellVarContext current"
!define REG_ROOT "HKCU"
!define REG_APP_PATH "Software\Microsoft\Windows\CurrentVersion\App Paths\${MAIN_APP_EXE}"
!define UNINSTALL_PATH "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME}"

VIProductVersion  "${VERSION}"
VIAddVersionKey "ProductName"  "${APP_NAME}"
VIAddVersionKey "CompanyName"  "${COMP_NAME}"
VIAddVersionKey "LegalCopyright"  "${COPYRIGHT}"
VIAddVersionKey "FileDescription"  "${DESCRIPTION}"
VIAddVersionKey "FileVersion"  "${VERSION}"

SetCompressor ZLIB
Name "${APP_NAME}"
Caption "${APP_NAME}"
OutFile "${INSTALLER_NAME}"
BrandingText "${APP_NAME}"
XPStyle on
InstallDir "$PROGRAMFILES\${APP_NAME}"

!include "MUI.nsh"

!define MUI_ABORTWARNING
!define MUI_UNABORTWARNING

!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!define MUI_FINISHPAGE_RUN "$INSTDIR\${MAIN_APP_EXE}"
!insertmacro MUI_PAGE_FINISH
!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES
!insertmacro MUI_LANGUAGE "English"

Section "MainSection" SEC01
    SetOutPath "$INSTDIR"
    SetOverwrite ifnewer
    File "dist\FaradayShieldAnalyser.exe"
    File "sample_experiment.xlsx"
    
    CreateDirectory "$SMPROGRAMS\${APP_NAME}"
    CreateShortCut "$SMPROGRAMS\${APP_NAME}\${APP_NAME}.lnk" "$INSTDIR\${MAIN_APP_EXE}"
    CreateShortCut "$DESKTOP\${APP_NAME}.lnk" "$INSTDIR\${MAIN_APP_EXE}"
SectionEnd

Section -Post
    WriteUninstaller "$INSTDIR\uninstall.exe"
    WriteRegStr ${REG_ROOT} "${REG_APP_PATH}" "" "$INSTDIR\${MAIN_APP_EXE}"
    WriteRegStr ${REG_ROOT} "${UNINSTALL_PATH}" "DisplayName" "${APP_NAME}"
    WriteRegStr ${REG_ROOT} "${UNINSTALL_PATH}" "UninstallString" "$INSTDIR\uninstall.exe"
    WriteRegStr ${REG_ROOT} "${UNINSTALL_PATH}" "DisplayVersion" "${VERSION}"
    WriteRegStr ${REG_ROOT} "${UNINSTALL_PATH}" "Publisher" "${COMP_NAME}"
SectionEnd

Section Uninstall
    Delete "$INSTDIR\${MAIN_APP_EXE}"
    Delete "$INSTDIR\sample_experiment.xlsx"
    Delete "$INSTDIR\uninstall.exe"
    Delete "$SMPROGRAMS\${APP_NAME}\${APP_NAME}.lnk"
    Delete "$DESKTOP\${APP_NAME}.lnk"
    RmDir "$SMPROGRAMS\${APP_NAME}"
    RmDir "$INSTDIR"
    DeleteRegKey ${REG_ROOT} "${REG_APP_PATH}"
    DeleteRegKey ${REG_ROOT} "${UNINSTALL_PATH}"
SectionEnd
```

Build installer:
```bash
makensis installer.nsi
```

---

## 🍎 macOS Release Package

### Build

```bash
# 1. Activate virtual environment
source venv/bin/activate

# 2. Build app
python3 build_app.py

# Result: dist/FaradayShieldAnalyser.app
```

### Create DMG

```bash
# Create DMG
hdiutil create -volname "Faraday Shield Analyser" \
    -srcfolder dist/FaradayShieldAnalyser.app \
    -ov -format UDZO \
    FaradayShieldAnalyser-v1.0.dmg
```

### Sign (Optional)

```bash
# Sign the app
codesign --force --deep --sign "Developer ID Application: Your Name" \
    dist/FaradayShieldAnalyser.app

# Notarize (requires Apple Developer account)
xcrun altool --notarize-app \
    --primary-bundle-id "com.yourcompany.shieldanalyser" \
    --username "your@email.com" \
    --password "@keychain:AC_PASSWORD" \
    --file FaradayShieldAnalyser-v1.0.dmg
```

---

## 🐧 Linux Release Package

### Build

```bash
# 1. Activate virtual environment
source venv/bin/activate

# 2. Build executable
python3 build_app.py

# Result: dist/FaradayShieldAnalyser
```

### Create AppImage

```bash
# Download linuxdeploy
wget https://github.com/linuxdeploy/linuxdeploy/releases/download/continuous/linuxdeploy-x86_64.AppImage
chmod +x linuxdeploy-x86_64.AppImage

# Create AppDir structure
mkdir -p AppDir/usr/bin
mkdir -p AppDir/usr/share/applications
mkdir -p AppDir/usr/share/icons/hicolor/256x256/apps

# Copy executable
cp dist/FaradayShieldAnalyser AppDir/usr/bin/

# Create desktop file
cat > AppDir/usr/share/applications/shieldanalyser.desktop << EOF
[Desktop Entry]
Type=Application
Name=Faraday Shield Analyser
Exec=FaradayShieldAnalyser
Icon=shieldanalyser
Categories=Science;Education;
EOF

# Build AppImage
./linuxdeploy-x86_64.AppImage --appdir AppDir --output appimage
```

### Create DEB Package

```bash
# Create package structure
mkdir -p faraday-shield-analyser_1.0/DEBIAN
mkdir -p faraday-shield-analyser_1.0/usr/bin
mkdir -p faraday-shield-analyser_1.0/usr/share/applications

# Copy files
cp dist/FaradayShieldAnalyser faraday-shield-analyser_1.0/usr/bin/

# Create control file
cat > faraday-shield-analyser_1.0/DEBIAN/control << EOF
Package: faraday-shield-analyser
Version: 1.0
Section: science
Priority: optional
Architecture: amd64
Maintainer: Your Name <your@email.com>
Description: Faraday Shield Measurement Analysis
 A tool for analyzing Faraday shield effectiveness measurements.
EOF

# Build DEB
dpkg-deb --build faraday-shield-analyser_1.0
```

---

## 📱 Android Package (Termux)

### Create Package

```bash
# Run packaging script
chmod +x package_android.sh
./package_android.sh

# Result: ShieldAnalyser-Android.zip
```

### What's Included

- All Python source files
- Static web files
- Sample data
- Termux run script
- Android-specific README

### Distribution

Users install:
1. Termux from F-Droid
2. Extract zip to Termux home
3. Run `./run.sh`

---

## 📋 Release Checklist

### Pre-Release Testing

- [ ] Test on clean Windows 10/11
- [ ] Test on clean macOS (latest)
- [ ] Test on Ubuntu 20.04/22.04
- [ ] Test Android (Termux)
- [ ] Verify all features work
- [ ] Test with large datasets
- [ ] Check data persistence
- [ ] Verify Excel export/import
- [ ] Test all chart types
- [ ] Check login system

### Build Checklist

- [ ] Update version numbers
- [ ] Update README.md
- [ ] Update CHANGELOG.md
- [ ] Build Windows EXE
- [ ] Build macOS APP
- [ ] Build Linux binary
- [ ] Create Android package
- [ ] Create installers/packages
- [ ] Test all builds

### Documentation

- [ ] User guide complete
- [ ] Installation instructions
- [ ] Troubleshooting guide
- [ ] API documentation
- [ ] Release notes

### Distribution

- [ ] Create GitHub release
- [ ] Upload all packages
- [ ] Update website
- [ ] Announce on social media
- [ ] Send to testers

---

## 📊 Release Package Contents

### Windows Package

```
FaradayShieldAnalyser-Windows-v1.0.zip
├── FaradayShieldAnalyser.exe (100 MB)
├── README.md
├── LICENSE.txt
└── sample_experiment.xlsx
```

### macOS Package

```
FaradayShieldAnalyser-v1.0.dmg (90 MB)
└── FaradayShieldAnalyser.app
    └── (app bundle contents)
```

### Linux Package

```
FaradayShieldAnalyser-Linux-v1.0.tar.gz
├── FaradayShieldAnalyser (95 MB)
├── README.md
├── LICENSE.txt
├── sample_experiment.xlsx
└── install.sh
```

### Android Package

```
ShieldAnalyser-Android.zip (2 MB)
├── app_launcher.py
├── main.py
├── static/
├── run.sh
├── README-ANDROID.md
└── sample_experiment.xlsx
```

---

## 🚀 Automated Build Script

Create `build_all.sh`:

```bash
#!/bin/bash
VERSION="1.0"

echo "Building all platforms for v$VERSION"

# Build Windows (on Windows or Wine)
python build_app.py
mv dist/FaradayShieldAnalyser.exe releases/FaradayShieldAnalyser-Windows-v$VERSION.exe

# Build macOS (on macOS)
python3 build_app.py
hdiutil create -volname "Faraday Shield Analyser" -srcfolder dist/FaradayShieldAnalyser.app -ov -format UDZO releases/FaradayShieldAnalyser-macOS-v$VERSION.dmg

# Build Linux
python3 build_app.py
mv dist/FaradayShieldAnalyser releases/FaradayShieldAnalyser-Linux-v$VERSION

# Build Android
./package_android.sh
mv ShieldAnalyser-Android.zip releases/ShieldAnalyser-Android-v$VERSION.zip

echo "✅ All builds complete in releases/"
```

---

## 🎉 Distribution Platforms

### GitHub Releases

```bash
# Create release
gh release create v1.0 \
    releases/FaradayShieldAnalyser-Windows-v1.0.exe \
    releases/FaradayShieldAnalyser-macOS-v1.0.dmg \
    releases/FaradayShieldAnalyser-Linux-v1.0 \
    releases/ShieldAnalyser-Android-v1.0.zip \
    --title "Faraday Shield Analyser v1.0" \
    --notes "Initial release"
```

### Website

Host on:
- GitHub Pages
- Netlify
- Own domain

### App Stores

- **Windows**: Microsoft Store
- **macOS**: Mac App Store (requires Developer account)
- **Linux**: Snap Store, Flathub
- **Android**: Google Play, F-Droid

---

**Ready to release! 🚀**

