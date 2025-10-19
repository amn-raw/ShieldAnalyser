# Faraday Shield Analyser

A comprehensive system to analyze and visualize Faraday shield effectiveness measurements.

## Features

### Data Input & Management
- 📊 Upload and parse Excel files with shield measurements
- ➕ **NEW:** Create experiments manually without Excel files
- ➕ **NEW:** Add rows (frequency points) dynamically
- ➕ **NEW:** Add columns (test locations) dynamically
- 🗑️ **NEW:** Delete rows with confirmation
- ✏️ Manual editing of experiment data with real-time calculations

### Calculations & Processing
- 📈 Automatic shielding effectiveness calculation
- 🔄 **NEW:** Real-time recalculation when values change
- ⚡ Auto-pairing of location and shielding columns

### Visualizations
- 📉 **NEW:** Frequency vs Reference chart
- 📊 Frequency vs Shielding Effectiveness chart
- 📈 Frequency vs Actual Values chart
- 🎨 Interactive, color-coded multi-line charts

### Export & Sharing
- 💾 Export processed data to Excel with all calculations
- 📥 Download includes original data + shielding effectiveness

### User Experience
- 🔐 Simple authentication system
- 🎨 Modern, intuitive UI with modal dialogs
- 🚀 Fast and responsive interface
- ✨ Professional gradient design

## Quick Start Options

### Option 1: Standalone Desktop App (Easiest! 🎉)

**For end users - no installation needed:**

1. **Download** the executable for your platform:
   - Windows: `FaradayShieldAnalyser.exe`
   - macOS: `FaradayShieldAnalyser.app`
   - Linux: `FaradayShieldAnalyser`

2. **Run** the application:
   - Windows: Double-click the `.exe` file
   - macOS: Copy to Applications, double-click
   - Linux: `chmod +x FaradayShieldAnalyser && ./FaradayShieldAnalyser`

3. **Done!** Browser opens automatically, login with `admin/admin123`

📖 **Build your own:** See [BUILD_INSTRUCTIONS.md](BUILD_INSTRUCTIONS.md)

---

### Option 2: Development/Source Code Installation

**For developers or customization:**

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python main.py
```

3. Open your browser and navigate to:
```
http://localhost:8000
```

## Default Credentials

- Username: `admin` / Password: `admin123`
- Username: `user` / Password: `password123`

You can modify credentials in `creds.json`.

## Excel File Format

The input Excel file should have the following format:

| Frequency (MHz) | Reference | L1 | L2 | L3 | ... |
|----------------|-----------|----|----|----|----|
| 100            | -20       | -45| -50| -55| ... |
| 200            | -25       | -48| -52| -58| ... |
| ...            | ...       | ...| ...| ...| ... |

- First column: Frequencies
- Second column: Reference measurements
- Subsequent columns: Location measurements (can be named anything)

## Usage

### Standalone App

1. **Launch** the application (double-click or run from terminal)
2. **Browser opens automatically** at `http://localhost:8000`
3. **Login** with `admin/admin123`

### Development Mode

Start the server:
```bash
./run.sh
# Or: source venv/bin/activate && python main.py
```

### Basic Workflow
1. Login with your credentials
2. **Option A:** Upload an Excel file OR **Option B:** Create new experiment manually
3. View the parsed/created data in the table
4. Edit values manually (auto-calculates shielding effectiveness)
5. Add more rows or columns as needed
6. View the three generated charts (toggle between line/bar charts)
7. Download the processed data with shielding effectiveness calculations

### Creating Experiments Manually
1. Click "➕ Create New Experiment"
2. Enter name, number of locations, and frequency points
3. Edit the generated table with your measurements
4. Shielding effectiveness calculates automatically
5. Add more rows/columns as needed

### Adding Rows & Columns
- **Add Row:** Click "➕ Add Row" to add frequency measurements
- **Add Column:** Click "➕ Add Column" to add test locations (auto-creates shielding column)
- **Delete Row:** Click 🗑️ button on any row to remove it

See `COMPLETE_GUIDE.md` for detailed user guide and `BUILD_INSTRUCTIONS.md` for building standalone apps.

## Data Storage

### Standalone Apps
Data is stored in platform-specific locations:
- **Windows**: `%APPDATA%\FaradayShieldAnalyser\`
- **macOS**: `~/Library/Application Support/FaradayShieldAnalyser/`
- **Linux**: `~/.local/share/FaradayShieldAnalyser/`

### Development Mode
- Experiments are stored in `experiments.json`
- No database required - simple JSON-based storage

## 📱 Mobile Support

### Android (via Termux)

1. Install Termux from F-Droid
2. Run package script: `./package_android.sh`
3. Transfer zip to phone
4. Extract and run in Termux

See [STANDALONE_APP_GUIDE.md](STANDALONE_APP_GUIDE.md) for detailed Android instructions.

## 📦 Building Standalone Apps

Want to build your own executables?

```bash
# Install build dependencies
pip install -r requirements_app.txt

# Build for your platform
python build_app.py

# Find executable in dist/ folder
```

See detailed build instructions:
- [BUILD_INSTRUCTIONS.md](BUILD_INSTRUCTIONS.md) - Complete build guide
- [STANDALONE_APP_GUIDE.md](STANDALONE_APP_GUIDE.md) - User guide for standalone apps
- [RELEASE_PACKAGE.md](RELEASE_PACKAGE.md) - Distribution packaging
- [COMPLETE_GUIDE.md](COMPLETE_GUIDE.md) - Complete user and developer guide

## License

MIT License

