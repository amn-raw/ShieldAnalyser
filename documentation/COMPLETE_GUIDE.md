# Faraday Shield Analyser - Complete Guide

## 🎯 What is This?

**Faraday Shield Analyser** is a professional tool for analyzing electromagnetic shielding effectiveness. It helps you:

- 📊 Analyze shield measurements across frequencies
- 📈 Visualize shielding effectiveness with interactive charts
- 💾 Manage multiple experiments
- 📁 Import/export data via Excel
- 🔒 Secure multi-user access

---

## 🚀 Quick Start (3 Steps!)

### 1️⃣ Get the App

**Option A: Download Pre-Built** (Easiest!)
- Windows: Download `FaradayShieldAnalyser.exe`
- macOS: Download `FaradayShieldAnalyser.app`
- Linux: Download `FaradayShieldAnalyser`

**Option B: Build from Source**
```bash
git clone <your-repo>
cd ShieldAnalyser
python build_app.py
```

### 2️⃣ Run the App

**Windows:**
```
Double-click FaradayShieldAnalyser.exe
```

**macOS:**
```
Open FaradayShieldAnalyser.app
```

**Linux:**
```bash
chmod +x FaradayShieldAnalyser
./FaradayShieldAnalyser
```

### 3️⃣ Start Analyzing!

Browser opens automatically → Login with `admin/admin123` → Upload or create experiment → Done! 🎉

---

## 📚 User Guide

### Creating Your First Experiment

#### Method 1: Upload Excel File

1. Click **"Upload Experiment"**
2. Choose your Excel file (format: Frequency | Reference | Location1 | Location2 ...)
3. Enter experiment name
4. Click **Upload**

**Excel Format Example:**

| Frequency (MHz) | Reference | L1 | L2 | L3 |
|-----------------|-----------|----|----|-----|
| 100 | -20 | -40 | -45 | -42 |
| 200 | -22 | -43 | -48 | -45 |
| 300 | -24 | -46 | -51 | -48 |

#### Method 2: Create Manually

1. Click **"Create New Experiment"**
2. Enter experiment name
3. Specify:
   - Number of locations (columns)
   - Number of frequency points (rows)
4. Click **Create**
5. Fill in data manually

### Working with Data

#### Adding Rows
1. Open experiment
2. Click **"Add Row"**
3. Enter frequency and values
4. Click **Save Changes**

#### Adding Columns (Locations)
1. Click **"Add Column"**
2. Enter location name (e.g., "L5")
3. Shielding column created automatically
4. Click **Save Changes**

#### Deleting Rows
1. Click ❌ in row's Actions column
2. Confirm deletion
3. Click **Save Changes**

#### Editing Values
1. Click any cell (except shielding columns)
2. Edit value
3. Shielding recalculates automatically
4. Click **Save Changes**

### Understanding Charts

#### Chart 1: Shielding Effectiveness by Location
- **X-axis**: Locations (L1, L2, L3...)
- **Y-axis**: Shielding Effectiveness (dB)
- **Shows**: How well each location is shielded
- **Higher values = Better shielding**

#### Chart 2: Actual Values by Location
- **X-axis**: Locations
- **Y-axis**: Signal Power (dBm)
- **Shows**: Raw measurement values
- **More negative = Stronger attenuation**

#### Chart 3: Frequency vs Reference
- **X-axis**: Frequency (MHz)
- **Y-axis**: Reference Signal (dBm)
- **Shows**: Reference signal across frequencies
- **Used**: As baseline for shielding calculations

#### Toggle Chart Type
Each chart has **Line** and **Bar** buttons:
- Click to switch between graph types
- Settings saved per chart
- Choose what works best for your data

### Downloading Data

1. Open experiment
2. Click **"Download Excel"**
3. File downloads with all data including calculated shielding

---

## 🔧 Advanced Features

### Multi-User Management

Edit `creds.json`:
```json
{
  "users": [
    {"username": "admin", "password": "admin123"},
    {"username": "engineer1", "password": "pass123"},
    {"username": "engineer2", "password": "pass456"}
  ]
}
```

Location:
- **Standalone**: In app data directory
- **Development**: In project folder

### Full Table View

Click **"Full View"** for expanded table:
- Larger display
- Easier data entry
- Click anywhere outside to close

### Data Persistence

#### Standalone Apps
Data saved automatically to:
- **Windows**: `%APPDATA%\FaradayShieldAnalyser\`
- **macOS**: `~/Library/Application Support/FaradayShieldAnalyser/`
- **Linux**: `~/.local/share/FaradayShieldAnalyser/`

Files:
- `experiments.json` - All experiment data
- `creds.json` - User accounts

#### Development Mode
Data saved to project directory.

### Backup Your Data

**Windows:**
```cmd
copy "%APPDATA%\FaradayShieldAnalyser\experiments.json" backup.json
```

**macOS/Linux:**
```bash
cp ~/Library/Application\ Support/FaradayShieldAnalyser/experiments.json backup.json
```

### Restore Data

Replace `experiments.json` with your backup file.

---

## 📱 Platform-Specific Guides

### Windows

**Installation:**
1. Download `FaradayShieldAnalyser.exe`
2. Place in any folder
3. Double-click to run

**First Run:**
- Windows Defender may show warning
- Click "More info" → "Run anyway"
- This is normal for unsigned apps

**Data Location:**
```
C:\Users\YourName\AppData\Roaming\FaradayShieldAnalyser\
```

**Uninstall:**
- Delete the .exe file
- Delete data folder (optional)

---

### macOS

**Installation:**
1. Download `FaradayShieldAnalyser.app`
2. Copy to Applications folder
3. Double-click to launch

**First Run:**
- macOS may block unsigned apps
- Right-click → Open (first time only)
- Or: System Preferences → Security → Allow

**Data Location:**
```
/Users/YourName/Library/Application Support/FaradayShieldAnalyser/
```

**Uninstall:**
- Move app to Trash
- Delete data folder (optional)

---

### Linux

**Installation:**
1. Download `FaradayShieldAnalyser`
2. Make executable: `chmod +x FaradayShieldAnalyser`
3. Run: `./FaradayShieldAnalyser`

**Data Location:**
```
~/.local/share/FaradayShieldAnalyser/
```

**Create Desktop Shortcut:**
```bash
cat > ~/.local/share/applications/shieldanalyser.desktop << EOF
[Desktop Entry]
Type=Application
Name=Faraday Shield Analyser
Exec=/path/to/FaradayShieldAnalyser
Icon=utilities-system-monitor
Categories=Science;Education;
EOF
```

---

### Android (Termux)

**Setup:**
1. Install Termux from F-Droid
2. Download `ShieldAnalyser-Android.zip`
3. Extract to Termux home
4. Run `./run.sh`

**Access:**
- Open Chrome
- Go to `http://localhost:8000`
- Bookmark for easy access

**Data Location:**
```
~/ShieldAnalyser-Android/experiments.json
```

---

## 🐛 Troubleshooting

### App Won't Start

**Windows:**
- Run as Administrator
- Disable antivirus temporarily
- Check Windows Defender exclusions

**macOS:**
- Remove quarantine: `xattr -cr FaradayShieldAnalyser.app`
- Check Security preferences

**Linux:**
- Verify permissions: `chmod +x FaradayShieldAnalyser`
- Check for missing libraries

### Browser Doesn't Open

**Solution:**
- Manually open browser
- Go to: `http://localhost:8000`

### Port Already in Use

**Error:** "Port 8000 is already in use"

**Solution:**
```bash
# Find process using port
lsof -i :8000  # macOS/Linux
netstat -ano | findstr :8000  # Windows

# Kill process or change port in app_launcher.py
```

### Login Not Working

**Check:**
- Correct username/password
- `creds.json` exists and is valid
- Case sensitivity (usernames are case-sensitive)

**Reset credentials:**
- Edit or delete `creds.json`
- Restart app (recreates default)

### Data Not Saving

**Check:**
- Permissions on data directory
- Disk space available
- `experiments.json` not read-only

**Fix permissions:**
```bash
# macOS/Linux
chmod -R 755 ~/Library/Application\ Support/FaradayShieldAnalyser/

# Windows (run as admin)
icacls "%APPDATA%\FaradayShieldAnalyser" /grant Users:F
```

### Charts Not Displaying

**Solutions:**
- Refresh browser (F5)
- Clear browser cache
- Try different browser
- Check JavaScript enabled

### Excel Upload Fails

**Common Issues:**
- File format must be `.xlsx` (not `.xls`)
- First row must be headers
- Frequency column required
- Reference column required
- No empty rows/columns

### Large Files Slow

**Optimization:**
- Limit to < 1000 frequency points
- Use decimation for display
- Download to Excel for full data

---

## 💡 Tips & Best Practices

### Data Entry

✅ **Do:**
- Use consistent naming (L1, L2, L3...)
- Include units in column headers
- Maintain regular frequency spacing
- Save frequently

❌ **Don't:**
- Mix units (MHz vs GHz)
- Leave gaps in data
- Use special characters in names
- Forget to save changes

### Naming Conventions

**Experiments:**
- Use descriptive names
- Include date: "Shield_Test_2025-10-18"
- Include location: "Lab_A_Test_1"

**Locations:**
- Short names: L1, L2, L3
- Or descriptive: "Top_Left", "Center", "Bottom_Right"

### Performance

**For best performance:**
- Keep experiments < 500 frequency points for display
- Use bar charts for fewer data points (< 20)
- Use line charts for more data points (> 20)
- Download large datasets to Excel

### Data Management

**Regular maintenance:**
- Back up experiments weekly
- Delete old test experiments
- Export important data to Excel
- Keep archives off-system

---

## 📊 Understanding the Physics

### What is Shielding Effectiveness?

**Definition:**
Shielding Effectiveness (SE) measures how well a shield reduces electromagnetic field strength.

**Formula:**
```
SE (dB) = Reference Signal (dBm) - Shielded Signal (dBm)
```

**Interpretation:**
- **0 dB**: No shielding
- **20 dB**: 99% reduction
- **40 dB**: 99.99% reduction
- **60 dB**: 99.9999% reduction

**Example:**
- Reference: -20 dBm
- Location L1: -40 dBm
- Shielding: -20 - (-40) = **20 dB**

### Why Higher is Better?

More negative measured value = stronger attenuation = higher SE = better shield.

### Typical Values

| Application | SE Required |
|-------------|-------------|
| Basic EMI protection | 20-30 dB |
| Commercial equipment | 40-60 dB |
| Sensitive medical | 60-80 dB |
| Military/secure | 80-100 dB |

---

## 🎓 Tutorial: Complete Workflow

### Scenario: Testing New Shield Design

**Step 1: Prepare Data**
- Measure reference signal (no shield)
- Measure at multiple locations with shield
- Record at various frequencies

**Step 2: Create Experiment**
```
Name: "Shield_V2_Test_2025-10-18"
Locations: 4 (corners of shield)
Frequencies: 10 (100 MHz - 1 GHz)
```

**Step 3: Enter Data**
- Upload Excel or enter manually
- Verify all values populated
- Check for obvious errors

**Step 4: Analyze Results**
- Review shielding effectiveness chart
- Identify weak locations (lower SE)
- Compare frequencies (frequency-dependent effects)

**Step 5: Document**
- Download Excel with results
- Screenshot charts
- Note any anomalies
- Save experiment for future reference

**Step 6: Iterate**
- Modify shield design
- Create new experiment
- Compare with previous tests

---

## 🔐 Security Considerations

### User Access

**Default credentials:**
- Username: `admin`
- Password: `admin123`

**⚠️ CHANGE THESE!**

### Password Best Practices

1. Edit `creds.json`
2. Use strong passwords (8+ characters)
3. Don't share accounts
4. Create per-user accounts

### Network Security

**Standalone app:**
- Runs on localhost only (127.0.0.1)
- Not accessible from network
- Safe for single-user desktop use

**Web deployment:**
- Use HTTPS
- Implement proper authentication
- Use environment variables for secrets
- Set up firewall rules

---

## 🚢 Deployment Options

### Desktop Application (Current)

**Pros:**
- No installation
- Offline use
- Fast startup
- Local data

**Use for:**
- Individual engineers
- Lab computers
- Offline analysis

### Web Server Deployment

**Setup:**
```bash
# Install on server
git clone <repo>
cd ShieldAnalyser
pip install -r requirements.txt

# Run with gunicorn (production)
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
```

**Pros:**
- Multi-user access
- Central data storage
- Remote access
- Team collaboration

**Use for:**
- Lab shared systems
- Remote teams
- Multiple simultaneous users

### Cloud Deployment

**Platforms:**
- Heroku
- AWS Elastic Beanstalk
- Google Cloud Run
- Azure App Service

**Benefits:**
- Accessible anywhere
- Scalable
- Automatic backups
- High availability

---

## 📈 Roadmap / Future Features

**Planned:**
- [ ] Statistical analysis (mean, std dev)
- [ ] Frequency sweep animations
- [ ] 3D heatmap visualization
- [ ] Automatic report generation (PDF)
- [ ] Comparison between experiments
- [ ] Import from CSV
- [ ] Database support (PostgreSQL, MySQL)
- [ ] Real-time data capture from instruments
- [ ] API for automation
- [ ] Mobile native apps (iOS/Android)

**Want a feature?** Open an issue!

---

## 📞 Support & Community

### Getting Help

1. **Documentation:** Start with this guide
2. **Examples:** Check `sample_experiment.xlsx`
3. **Issues:** GitHub Issues for bugs
4. **Discussions:** GitHub Discussions for questions

### Reporting Bugs

Include:
- Platform (Windows/macOS/Linux/Android)
- App version
- Steps to reproduce
- Screenshots
- Error messages

### Feature Requests

Open GitHub Issue with:
- Use case
- Expected behavior
- Benefits
- Priority

---

## 📄 License

[Your License Here]

---

## 🙏 Acknowledgments

Built with:
- **FastAPI** - Modern Python web framework
- **Pandas** - Data analysis library
- **Chart.js** - JavaScript charting
- **PyInstaller** - Executable packaging
- **Uvicorn** - ASGI server

---

## 🎉 You're Ready!

**Start analyzing your Faraday shields now!**

1. Download/build the app
2. Launch it
3. Create your first experiment
4. Start measuring!

**Questions?** Check [BUILD_INSTRUCTIONS.md](BUILD_INSTRUCTIONS.md) or [STANDALONE_APP_GUIDE.md](STANDALONE_APP_GUIDE.md)

**Happy shielding! 🛡️⚡**

