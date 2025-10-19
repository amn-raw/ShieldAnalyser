# Quick Start Guide - Faraday Shield Analyser

## 🚀 Get Started in 3 Minutes

### Step 1: Start the Application

```bash
cd ShieldAnalyser
./run.sh
```

Or manually:
```bash
source venv/bin/activate
python main.py
```

### Step 2: Open in Browser

Navigate to: **http://localhost:8000**

### Step 3: Login

```
Username: admin
Password: admin123
```

### Step 4: Upload Sample Data

1. Look for the file `sample_experiment.xlsx` in the project folder
2. Drag and drop it into the upload area, or click to browse

### Step 5: View Results

- ✅ Data table will appear with measurements and calculated shielding effectiveness
- 📈 Two charts will show:
  - Frequency vs Shielding Effectiveness
  - Frequency vs Actual Values
- ✏️ Click any cell to edit values
- 💾 Click "Save Changes" after editing
- ⬇️ Click "Download Excel" to export

---

## 📊 Excel File Format

Your file should look like this:

```
| Frequency (MHz) | Reference | L1   | L2   | L3   |
|----------------|-----------|------|------|------|
| 100            | -20       | -45  | -50  | -55  |
| 200            | -22       | -48  | -52  | -58  |
| 300            | -21       | -46  | -51  | -56  |
```

**Required:**
- First column: Frequencies
- Second column: Reference measurements
- Other columns: Location measurements

**Output:**
The system automatically adds shielding effectiveness columns:
- L1-Shielding = Reference - L1
- L2-Shielding = Reference - L2
- etc.

---

## 🔑 Key Features

1. **Upload Excel** - Drag & drop .xlsx files
2. **Auto-Calculate** - Shielding effectiveness computed automatically
3. **Edit Data** - Click any cell to modify values
4. **Visualize** - Interactive charts with multiple locations
5. **Export** - Download processed data as Excel
6. **Multi-User** - Simple authentication system

---

## 🛠️ Troubleshooting

**Problem: Server won't start**
```bash
# Reinstall dependencies
pip install -r requirements.txt
```

**Problem: Port 8000 in use**
```bash
# Kill existing process
lsof -ti:8000 | xargs kill -9
```

**Problem: Can't upload file**
- Check file format matches example above
- Ensure all cells have numeric values
- Try the sample file first: `sample_experiment.xlsx`

---

## 📝 Quick Tips

✨ **Naming**: Use descriptive column names like "Front_Panel" instead of "L1"

✨ **Units**: All measurements should be in the same unit (typically dBm)

✨ **Backup**: Your data is saved in `experiments.json` - backup this file regularly

✨ **Multiple Users**: Add users in `creds.json`:
```json
{
  "users": [
    {"username": "newuser", "password": "password123"}
  ]
}
```

---

## 📚 Need More Help?

- See **USER_GUIDE.md** for detailed documentation
- See **README.md** for installation and setup
- Check browser console (F12) for error messages

---

## 🎯 Example Workflow

1. **Login** → Use admin/admin123
2. **Upload** → Drop your Excel file
3. **Review** → Check the data table for accuracy
4. **Analyze** → Examine the shielding effectiveness chart
5. **Edit** → Adjust any incorrect values
6. **Save** → Click "Save Changes"
7. **Export** → Download the processed file
8. **Repeat** → Upload more experiments as needed

---

**That's it! You're ready to analyze Faraday shield effectiveness! 🛡️**

