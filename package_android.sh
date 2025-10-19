#!/bin/bash
# Package for Android (Termux)

echo "📱 Packaging Faraday Shield Analyser for Android (Termux)"
echo "=========================================================="
echo ""

# Create a clean package directory
PACKAGE_DIR="ShieldAnalyser-Android"
rm -rf "$PACKAGE_DIR"
mkdir -p "$PACKAGE_DIR"

echo "📦 Copying files..."

# Copy necessary files
cp app_launcher.py "$PACKAGE_DIR/"
cp main.py "$PACKAGE_DIR/"
cp creds.json "$PACKAGE_DIR/"
cp sample_experiment.xlsx "$PACKAGE_DIR/"
cp requirements.txt "$PACKAGE_DIR/"

# Copy static folder
cp -r static "$PACKAGE_DIR/"

# Create a Termux-specific launcher
cat > "$PACKAGE_DIR/run.sh" << 'EOF'
#!/data/data/com.termux/files/usr/bin/bash
# Termux launcher script

echo "🛡️  Faraday Shield Analyser"
echo "==========================="
echo ""

# Check if Python is installed
if ! command -v python &> /dev/null; then
    echo "❌ Python not found!"
    echo "📦 Installing Python..."
    pkg install python -y
fi

# Check if pip packages are installed
echo "📦 Checking dependencies..."
python -c "import fastapi" 2>/dev/null || {
    echo "📦 Installing dependencies..."
    pip install fastapi uvicorn pandas openpyxl python-jose passlib python-multipart
}

# Run the app
echo ""
echo "🚀 Starting application..."
python app_launcher.py
EOF

chmod +x "$PACKAGE_DIR/run.sh"

# Create README for Android
cat > "$PACKAGE_DIR/README-ANDROID.md" << 'EOF'
# Faraday Shield Analyser - Android (Termux)

## Installation

1. **Install Termux** from F-Droid:
   - Download from: https://f-droid.org/en/packages/com.termux/
   - DO NOT use Google Play version (outdated)

2. **Setup Storage Access:**
   ```bash
   termux-setup-storage
   ```
   (Grant permission when prompted)

3. **Copy this folder to Termux:**
   - Copy ShieldAnalyser-Android folder to:
   - `/storage/emulated/0/Download/`

4. **Install in Termux:**
   ```bash
   cd ~/
   cp -r /storage/emulated/0/Download/ShieldAnalyser-Android ./
   cd ShieldAnalyser-Android
   chmod +x run.sh
   ```

## Running the App

```bash
cd ~/ShieldAnalyser-Android
./run.sh
```

The app will:
- Install dependencies (first time only)
- Start the server
- Show URL: http://localhost:8000

Then:
1. Open Chrome on Android
2. Go to: http://localhost:8000
3. Login: admin / admin123

## Quick Access (Optional)

Create a shortcut:
```bash
echo 'cd ~/ShieldAnalyser-Android && ./run.sh' > ~/start-shield.sh
chmod +x ~/start-shield.sh
```

Then just run:
```bash
~/start-shield.sh
```

## Stopping the App

Press `CTRL+C` in Termux

## Data Location

Your experiments are saved in:
```
~/ShieldAnalyser-Android/experiments.json
```

## Troubleshooting

**Port already in use:**
```bash
pkill python
./run.sh
```

**Permissions error:**
```bash
chmod -R 755 ~/ShieldAnalyser-Android
```

**Can't access in browser:**
- Use `http://localhost:8000` (not 127.0.0.1)
- Make sure Termux is running
- Check if server started (look for "Running at" message)

## Updating

1. Replace files in ShieldAnalyser-Android folder
2. Keep your experiments.json and creds.json
3. Run ./run.sh again

---

**Enjoy! 🚀📱**
EOF

# Create a zip package
echo "📦 Creating zip package..."
zip -r ShieldAnalyser-Android.zip "$PACKAGE_DIR/"

echo ""
echo "✅ Android package created!"
echo ""
echo "📦 Package: ShieldAnalyser-Android.zip"
echo "📁 Folder: $PACKAGE_DIR/"
echo ""
echo "📱 Next steps:"
echo "   1. Copy ShieldAnalyser-Android.zip to your Android device"
echo "   2. Install Termux from F-Droid"
echo "   3. Extract and follow README-ANDROID.md"
echo ""

