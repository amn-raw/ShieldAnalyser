# Faraday Shield Analyser

A comprehensive system to analyze and visualize Faraday shield effectiveness measurements.

## 🚀 Quick Start

### For End Users:

**macOS Native App:**
```bash
open dist/FaradayShieldAnalyser.app
# Login: admin / admin123
```

**Android (via Termux):**
- Use the pre-packaged Termux version
- Install Termux from F-Droid
- See `PHONE_TESTING_QUICK_REFERENCE.txt` for instructions
- Note: Native APK build requires extensive restructuring (FastAPI → Kivy/WebView)

### For Developers:

```bash
# Setup
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

# Run
python main.py
# Open http://localhost:8000
```

## ✨ Features

- 📊 **Data Management**: Upload Excel files or create experiments manually
- 📈 **Visualizations**: Interactive line and bar charts
- ➕ **Dynamic Editing**: Add/remove rows and columns in real-time
- 🔄 **Auto-calculations**: Shielding effectiveness calculated automatically
- 💾 **Excel Export**: Download results with all calculations
- 🔐 **Multi-user**: Simple authentication system
- 🖥️ **Native Apps**: True Mac app (no browser!) + Android APK

## 📦 Installation

### Option 1: Use Pre-built Apps (Recommended)

**Mac:**
- Download `FaradayShieldAnalyser.app`
- Drag to Applications folder
- Double-click to run
- No installation needed!

**Android:**
- Push this repo to GitHub
- GitHub Actions builds APK automatically
- Download and install APK
- See `documentation/DEPLOY_APK.md`

### Option 2: Run from Source

```bash
# Clone repository
git clone <your-repo-url>
cd ShieldAnalyser

# Setup virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run
python main.py
```

## 🎯 Usage

1. **Login**: Default credentials: admin / admin123
2. **Create Experiment**:
   - Upload Excel file, OR
   - Create manually (specify locations and frequency points)
3. **Edit Data**: Click cells to edit, auto-calculates shielding
4. **View Charts**: Three interactive charts (line/bar toggle)
5. **Download**: Export to Excel with all calculations

## 📱 Building Native Apps

### Mac Native App

```bash
pip install -r requirements_native.txt
python3 build_native_mac.py
# Result: dist/FaradayShieldAnalyser.app
```

### Android (Termux Method - Recommended)

```bash
# Package for Termux
./package_android.sh

# Transfer ShieldAnalyser-Android.zip to phone
# Follow PHONE_TESTING_QUICK_REFERENCE.txt
```

**Note:** Building a native Android APK requires restructuring the app architecture
(FastAPI web server → Android native app). The Termux method provides full
functionality and is the recommended approach for Android.

## 📚 Documentation

All documentation is in the `documentation/` folder:

- **Quick Start**: `documentation/QUICK_START.md`
- **User Guide**: `documentation/COMPLETE_GUIDE.md`
- **Mac App Build**: `documentation/BUILD_NATIVE_APPS.md`
- **Android APK**: `documentation/DEPLOY_APK.md`
- **Testing**: `documentation/TESTING_COMPLETE_SUMMARY.md`

## 🏗️ Project Structure

```
ShieldAnalyser/
├── main.py                    # FastAPI backend
├── static/
│   └── index.html            # Frontend UI
├── app_native_mac.py         # Mac native app launcher
├── buildozer.spec            # Android APK config
├── .github/workflows/        # CI/CD for APK build
├── creds.json               # User credentials
├── sample_experiment.xlsx   # Sample data
└── documentation/           # All documentation
```

## 🔧 Configuration

### User Credentials

Edit `creds.json`:
```json
{
  "users": [
    {"username": "admin", "password": "admin123"},
    {"username": "user", "password": "password123"}
  ]
}
```

### Data Storage

- **Development**: `experiments.json` in project folder
- **Mac App**: `~/Library/Application Support/FaradayShieldAnalyser/`
- **Android**: App-specific storage directory

## 🧪 Testing

Run the test launcher:
```bash
python test_launcher.py
```

For phone testing, see `documentation/TEST_ON_PHONE_GUIDE.md`

## 📊 Excel File Format

Input Excel should have:
- Column 1: Frequency (MHz)
- Column 2: Reference measurements
- Columns 3+: Location measurements (L1, L2, etc.)

Example:
| Frequency (MHz) | Reference | L1 | L2 | L3 |
|----------------|-----------|----|----|-----|
| 100            | -20       | -45| -50| -55 |
| 200            | -25       | -48| -52| -58 |

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📄 License

MIT License - see LICENSE file for details

## 🙏 Acknowledgments

- **FastAPI** - Modern Python web framework
- **Pandas** - Data analysis
- **Chart.js** - Interactive charts
- **PyInstaller** - Executable packaging
- **Buildozer** - Android APK builds

## 🆘 Support

- 📖 Documentation: See `documentation/` folder
- 🐛 Issues: GitHub Issues
- 💬 Discussions: GitHub Discussions

---

**Built with ❤️ for electromagnetic shielding analysis**

