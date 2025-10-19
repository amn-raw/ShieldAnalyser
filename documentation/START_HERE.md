# 🛡️ START HERE - Faraday Shield Analyser

## Welcome! 👋

Thank you for choosing the Faraday Shield Analyser. This document will get you up and running in minutes.

---

## ⚡ Quick Start (3 Steps)

### Step 1: Start the Application
```bash
cd ShieldAnalyser
./run.sh
```

### Step 2: Open in Browser
Navigate to: **http://localhost:8000**

### Step 3: Login
```
Username: admin
Password: admin123
```

**That's it!** You're ready to start analyzing shield data. 🎉

---

## 📁 What's Included

```
ShieldAnalyser/
├── 📄 START_HERE.md          ← You are here!
├── 📖 README.md              ← Main documentation
├── 🚀 QUICK_START.md         ← Quick start guide
├── 📚 USER_GUIDE.md          ← Comprehensive user manual
├── 🔬 PROJECT_SUMMARY.md     ← Technical overview
├── ✅ TESTING_CHECKLIST.md   ← QA testing guide
├── 📋 RELEASE_NOTES.md       ← Version information
│
├── 🐍 main.py                ← Backend application
├── 📊 sample_experiment.xlsx ← Sample data (USE THIS FIRST!)
├── 🔐 creds.json            ← User credentials
├── ⚙️  run.sh                ← Startup script
└── 📦 requirements.txt       ← Dependencies
```

---

## 🎯 First Time User?

### Try This Workflow:

1. **Start the app** using `./run.sh`
2. **Login** with admin/admin123
3. **Upload** `sample_experiment.xlsx` (drag & drop or click)
4. **View** the experiment in the list
5. **Explore** the data table
6. **Check** the two charts:
   - Shielding Effectiveness vs Frequency
   - Actual Values vs Frequency
7. **Edit** a value (click any cell)
8. **Save** your changes
9. **Download** the processed Excel file

**Time to complete**: 5 minutes

---

## 📊 What Does It Do?

### Input
Excel file with your measurements:

| Frequency (MHz) | Reference | L1   | L2   | L3   |
|----------------|-----------|------|------|------|
| 100            | -20       | -45  | -50  | -55  |
| 200            | -22       | -48  | -52  | -58  |

### Processing
Automatically calculates shielding effectiveness:
- **Formula**: SE (dB) = Reference - Location
- **Example**: -20 - (-45) = 25 dB

### Output
1. **Enhanced Data Table** with SE columns
2. **Interactive Charts** showing:
   - Shielding effectiveness by frequency
   - Actual measurements by frequency
3. **Downloadable Excel** with all calculations

---

## 🎨 Features Overview

### 📤 Upload
- Drag & drop Excel files
- Automatic parsing
- Data validation
- Error messages

### 📊 Visualize
- Beautiful line charts
- Multiple locations on one chart
- Interactive tooltips
- Color-coded lines

### ✏️ Edit
- Click any cell to edit
- Save changes with one click
- Changes persist
- Recalculate automatically

### 💾 Export
- Download as Excel
- Includes all calculations
- Professional format
- Ready for reports

### 🔐 Secure
- Username/password login
- Session management
- User tracking
- Configurable access

---

## 📖 Documentation Map

### For Immediate Use
**Read**: `QUICK_START.md`
- 3-minute guide
- Essential steps only
- Get started fast

### For Daily Users
**Read**: `USER_GUIDE.md`
- Comprehensive guide
- All features explained
- Troubleshooting tips
- Best practices

### For Developers/Technical Users
**Read**: `PROJECT_SUMMARY.md`
- Architecture details
- API documentation
- Data structures
- Deployment options

### For Testing/QA
**Read**: `TESTING_CHECKLIST.md`
- Complete test scenarios
- Acceptance criteria
- Bug reporting
- Quality assurance

---

## 🆘 Need Help?

### Quick Fixes

**Problem: Server won't start**
```bash
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

**Problem: Can't login**
- Default credentials: admin / admin123
- Check `creds.json` file exists
- Username and password are case-sensitive

**Problem: File won't upload**
- Make sure it's an Excel file (.xlsx or .xls)
- Check the format matches the sample file
- Try uploading `sample_experiment.xlsx` first

**Problem: Charts not showing**
- Make sure experiment has data
- Try refreshing the page (F5)
- Check browser console (F12) for errors

### Still Stuck?
1. Check `USER_GUIDE.md` → Troubleshooting section
2. Review `QUICK_START.md` → Step-by-step instructions
3. Try the sample file → `sample_experiment.xlsx`
4. Check browser console → Press F12

---

## 💡 Tips for Success

1. **Start with Sample Data**
   - Use `sample_experiment.xlsx` to learn the system
   - Understand the format before using your own data

2. **Organize Your Files**
   - Use clear column names (e.g., "Front_Panel" not "L1")
   - Keep frequency ranges consistent
   - Document test conditions

3. **Regular Backups**
   ```bash
   cp experiments.json backup_$(date +%Y%m%d).json
   ```

4. **Add Your Users**
   - Edit `creds.json` to add team members
   - Each user should have unique credentials

5. **Check Calculations**
   - Verify SE = Reference - Location
   - Higher SE values = better shielding
   - Typical range: 20-80 dB

---

## 🎓 Understanding Shielding Effectiveness

### What is it?
Shielding Effectiveness (SE) measures how well a shield reduces electromagnetic fields.

### Formula
```
SE (dB) = Reference Power - Shielded Power
```

### Example
- **Reference**: -20 dBm (signal without shield)
- **Location**: -45 dBm (signal with shield)
- **SE**: -20 - (-45) = **25 dB**

### Interpretation
- **25 dB** = Signal reduced by ~18x
- **40 dB** = Signal reduced by ~100x
- **60 dB** = Signal reduced by ~1000x

**Higher is better!**

---

## 🚀 Common Workflows

### Workflow 1: Single Test Analysis
1. Perform measurements → Create Excel file
2. Upload to system
3. Review calculations
4. Generate report (download Excel)

### Workflow 2: Multiple Test Comparison
1. Upload Test 1
2. Upload Test 2
3. View each separately
4. Compare results manually
5. Export both for reporting

### Workflow 3: Iterative Testing
1. Upload initial test
2. Identify weak spots
3. Make improvements
4. Upload new test
5. Compare results

---

## 🎯 Next Steps

After reading this, you should:

1. ✅ Start the application (`./run.sh`)
2. ✅ Login and upload sample file
3. ✅ Explore all features
4. ✅ Read `USER_GUIDE.md` for details
5. ✅ Prepare your own data
6. ✅ Start analyzing!

---

## 📞 Quick Reference

### Default Credentials
```
Username: admin
Password: admin123
```

### URL
```
http://localhost:8000
```

### Data Location
```
experiments.json  (all experiments)
creds.json       (user credentials)
```

### Sample File
```
sample_experiment.xlsx
```

### Startup Command
```bash
./run.sh
```

### Stop Server
```
Press Ctrl + C
```

---

## 🎉 You're Ready!

Everything you need is included. Follow the steps above and you'll be analyzing Faraday shield data in minutes.

### Recommended Reading Order:
1. **This file** (START_HERE.md) ← Done! ✅
2. **QUICK_START.md** ← Next!
3. **USER_GUIDE.md** ← For deep dive
4. **PROJECT_SUMMARY.md** ← For technical details

---

## ⭐ Quick Tips

- 💡 Use meaningful experiment names
- 📊 Check charts for anomalies
- 💾 Download results regularly
- 🔐 Change default password
- 📖 Bookmark the documentation
- 🧪 Test with sample file first

---

**Let's get started! Run `./run.sh` now! 🚀**

---

## Project Information

- **Version**: 1.0.0
- **Status**: Ready for Production
- **License**: MIT
- **Created**: October 2025

**Happy Analyzing! 🛡️📊✨**

