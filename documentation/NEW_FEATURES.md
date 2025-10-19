# New Features Added - Faraday Shield Analyser

## 🎉 Latest Updates

### Version 1.1.0 - Enhanced Editing & Visualization

---

## 🆕 New Features

### 1. **Frequency vs Reference Chart** 📉

A new third chart has been added to visualize the reference signal measurements across frequencies.

**Location**: Bottom of the charts section
**Display**: Red line showing reference power values
**Purpose**: Helps identify reference measurement patterns and validate baseline data

---

### 2. **Manual Experiment Creation** ➕

Create experiments from scratch without uploading Excel files.

**How to Use:**
1. Click "➕ Create New Experiment" button
2. Enter experiment name
3. Specify number of locations (test points)
4. Specify number of frequency points
5. Click "Create"

**What It Does:**
- Creates a blank experiment with the specified structure
- Automatically sets up columns:
  - Frequency (MHz)
  - Reference
  - L1, L2, L3... (location columns)
  - L1-Shielding, L2-Shielding... (auto-calculated)
- Initializes default frequency values (100, 200, 300...)
- All values start at 0 for easy editing

**Example:**
- Name: "Test Shield #1"
- Locations: 4
- Frequencies: 10
- Result: Empty table ready for data entry

---

### 3. **Add New Rows** ➕

Dynamically add frequency measurement rows to any experiment.

**How to Use:**
1. Open an experiment
2. Click "➕ Add Row" button
3. New row appears at bottom of table
4. Edit values as needed
5. Click "💾 Save Changes"

**Features:**
- Automatically increments frequency (e.g., if last is 1000, new is 1100)
- All other columns initialized to 0
- Shielding columns auto-calculated when you enter values
- No limit on number of rows

---

### 4. **Add New Location Columns** ➕

Add additional test locations to existing experiments.

**How to Use:**
1. Open an experiment
2. Click "➕ Add Column" button
3. Enter column name (e.g., "L5", "Front_Panel", "Location_5")
4. Click "Add Column"

**What Happens:**
- New location column added
- Corresponding shielding column automatically created
  - Example: "L5" → "L5-Shielding"
- All rows updated with default values (0)
- Shielding effectiveness auto-calculated: Reference - Location
- Charts automatically updated

**Important:**
- Column names must be unique
- Shielding column is always paired with location column
- Can add as many columns as needed

---

### 5. **Delete Rows** 🗑️

Remove unwanted frequency measurement rows.

**How to Use:**
1. Open an experiment
2. Find the row you want to delete
3. Click the 🗑️ button in the "Actions" column
4. Confirm deletion
5. Row is removed
6. Click "💾 Save Changes"

**Safety:**
- Cannot delete the last row (at least one row required)
- Confirmation required before deletion
- Reminder to save changes

---

### 6. **Real-time Shielding Calculation** 🔄

Shielding effectiveness automatically recalculates when you edit values.

**How It Works:**
- Edit Reference value → All shielding columns recalculate
- Edit Location value → That location's shielding recalculates
- Formula: Shielding = Reference - Location
- Updates happen instantly in the table

**Example:**
```
Before Edit:
- Frequency: 100
- Reference: -20
- L1: -40
- L1-Shielding: 20

Edit Reference to -25:
- Frequency: 100
- Reference: -25  ← Changed
- L1: -40
- L1-Shielding: 15  ← Auto-updated!
```

---

## 🎨 UI Improvements

### Modal Dialogs
- Beautiful modal popups for creating experiments
- Modal for adding columns
- Click outside or "X" to close
- Smooth animations

### Action Buttons
- Color-coded buttons (blue for actions, green for success)
- Clear icons for easy identification
- Hover effects for better UX
- Organized layout

### Table Actions Column
- Delete button for each row
- Easy access to row operations
- Clear visual separation

---

## 📊 Workflow Examples

### Workflow 1: Create Experiment from Scratch

1. Click "➕ Create New Experiment"
2. Name: "Shield Test A"
3. Locations: 4, Frequencies: 5
4. Click Create
5. Table appears with 5 rows × 10 columns
6. Edit frequency values: 500, 600, 700, 800, 900
7. Edit reference values: -18, -19, -20, -21, -22
8. Edit location values for L1, L2, L3, L4
9. Shielding columns auto-calculate
10. Click "💾 Save Changes"
11. View three charts showing results

### Workflow 2: Expand Existing Experiment

1. Upload or open existing experiment
2. Click "➕ Add Column"
3. Enter "Side_Panel"
4. New columns added: Side_Panel, Side_Panel-Shielding
5. Edit Side_Panel values for each frequency
6. Shielding auto-calculated
7. Click "💾 Save Changes"
8. Charts update with new location

### Workflow 3: Add More Frequencies

1. Open experiment
2. Click "➕ Add Row" (repeat as needed)
3. Edit frequency values (e.g., 1300, 1400, 1500)
4. Edit reference and location values
5. Review updated charts
6. Click "💾 Save Changes"

### Workflow 4: Clean Up Data

1. Review experiment data
2. Identify erroneous rows
3. Click 🗑️ on bad rows
4. Confirm deletion
5. Click "💾 Save Changes"
6. Export clean data

---

## 🔧 Technical Details

### Auto-calculation Logic
```javascript
// When Reference or Location changes
Reference: -20 dBm
Location: -45 dBm
Shielding = Reference - Location = -20 - (-45) = 25 dB
```

### Column Pairing
- Every location column gets a shielding column
- Naming: `{LocationName}-Shielding`
- Examples:
  - L1 → L1-Shielding
  - Front_Panel → Front_Panel-Shielding
  - Location_5 → Location_5-Shielding

### Default Values
- New rows: Frequency increments by 100 MHz
- New columns: All values = 0
- Easy to spot what needs editing

---

## ⚡ Benefits

### For Researchers
- Create experiments without Excel
- Quick prototyping of test configurations
- Easy to add measurement points
- Real-time validation

### For Lab Technicians
- Add data as measurements are taken
- No need to pre-plan exact structure
- Delete erroneous measurements easily
- Immediate feedback on shielding effectiveness

### For Engineers
- Flexible experiment design
- Expand tests as needed
- Compare multiple locations easily
- Professional visualizations

---

## 📖 Usage Tips

### Best Practices

1. **Start Small, Expand Later**
   - Create with minimum locations/frequencies
   - Add more as needed
   - More flexible than planning everything upfront

2. **Use Descriptive Names**
   - "Front_Panel" better than "L1"
   - "Top_Corner" better than "L5"
   - Makes charts and data more readable

3. **Validate as You Go**
   - Check shielding calculations immediately
   - View charts after each change
   - Catch errors early

4. **Save Frequently**
   - After adding rows/columns
   - After entering data
   - Before making major changes

5. **Use Delete Carefully**
   - Confirm you're deleting the right row
   - Remember to save after deletion
   - No undo feature (yet)

---

## 🐛 Known Behaviors

### Expected Behavior
- Shielding columns are auto-calculated (can't edit directly)
- Deleting requires confirmation
- At least one row always required
- Column names must be unique

### Tips
- If shielding doesn't update, check reference value
- If can't delete row, it might be the last one
- If column won't add, name might be duplicate
- Always save before closing experiment

---

## 🆚 Comparison: Old vs New

| Feature | Before | Now |
|---------|--------|-----|
| Create Experiment | Excel only | Excel OR manual |
| Add Rows | Edit Excel, re-upload | Click button |
| Add Columns | Edit Excel, re-upload | Click button |
| Delete Rows | Edit Excel, re-upload | Click button |
| Charts | 2 charts | 3 charts (+ Reference) |
| Shielding Calc | On upload only | Real-time |
| Flexibility | Low | High |

---

## 🎯 Quick Reference

### Button Guide
- **➕ Create New Experiment**: Start from scratch
- **➕ Add Row**: Add frequency measurement
- **➕ Add Column**: Add location measurement
- **💾 Save Changes**: Persist all edits
- **⬇️ Download Excel**: Export data
- **🗑️**: Delete row

### Keyboard Shortcuts
- **Tab**: Move between cells
- **Enter**: Move to next row
- **Esc**: Close modal dialogs

---

## 📞 Need Help?

### Common Questions

**Q: Can I edit shielding columns?**
A: No, they're auto-calculated. Edit Reference or Location instead.

**Q: What if I accidentally delete a row?**
A: Confirmation is required. If you confirmed, just re-add or reload without saving.

**Q: Can I rename columns?**
A: Not directly. Add new column, copy data, delete old (via save/download/re-upload).

**Q: Maximum rows/columns?**
A: No hard limit, but very large tables may be slow.

**Q: Do charts update automatically?**
A: Yes! Charts update whenever you add/edit/delete.

---

## 🚀 Future Enhancements

Potential future features:
- Undo/Redo functionality
- Bulk edit multiple cells
- Import CSV files
- Copy/paste rows
- Rename columns
- Reorder columns
- Formula builder
- Templates for common setups

---

## 📝 Changelog

### v1.1.0 (Latest)
- ➕ Added Frequency vs Reference chart
- ➕ Added manual experiment creation
- ➕ Added add row functionality
- ➕ Added add column functionality
- ➕ Added delete row functionality
- 🔄 Added real-time shielding recalculation
- 🎨 Improved UI with modal dialogs
- 📊 Enhanced table with actions column

### v1.0.0
- Initial release
- Excel upload
- Data table view
- 2 charts
- Edit cells
- Download Excel

---

**Enjoy the new features! 🎉**

For full documentation, see:
- `USER_GUIDE.md` - Complete user manual
- `QUICK_START.md` - Quick start guide
- `START_HERE.md` - Welcome guide

