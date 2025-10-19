# Testing Checklist - Faraday Shield Analyser

## ✅ Pre-Deployment Testing

Use this checklist to verify all features work correctly before releasing the software.

---

## 1. Installation & Setup

- [ ] Clone/download project to new location
- [ ] Run `./run.sh` successfully
- [ ] Virtual environment created automatically
- [ ] All dependencies installed without errors
- [ ] Server starts on port 8000
- [ ] Browser opens to http://localhost:8000

**Expected**: Server starts with welcome message showing:
```
Faraday Shield Analyser
Starting server at http://localhost:8000
Default credentials: admin / admin123
```

---

## 2. Authentication

### Login
- [ ] Access http://localhost:8000
- [ ] See login page with username/password fields
- [ ] Try invalid credentials → Error message displayed
- [ ] Login with admin/admin123 → Success
- [ ] Redirect to main dashboard
- [ ] Username displayed in header

### Logout
- [ ] Click logout button
- [ ] Redirect to login page
- [ ] Cannot access main page without login

**Expected**: Authentication works correctly, sessions maintained

---

## 3. File Upload

### Sample File
- [ ] Locate `sample_experiment.xlsx` in project folder
- [ ] Drag file to upload area
- [ ] File uploads successfully
- [ ] Success message displayed
- [ ] Experiment appears in list

### Drag and Drop
- [ ] Drag sample file over upload area
- [ ] Upload area changes appearance (dragover effect)
- [ ] Drop file
- [ ] File processes successfully

### Click Upload
- [ ] Click upload area
- [ ] File browser opens
- [ ] Select sample_experiment.xlsx
- [ ] File uploads successfully

### Error Handling
- [ ] Try uploading non-Excel file (.txt, .pdf) → Error message
- [ ] Try uploading invalid Excel format → Error message

**Expected**: 
- Valid files upload and parse correctly
- Invalid files show appropriate error messages

---

## 4. Experiment List

- [ ] Sample experiment appears in list
- [ ] Shows experiment name
- [ ] Shows upload date/time
- [ ] Shows uploader username
- [ ] View button visible
- [ ] Delete button visible
- [ ] Hover effects work

**Expected**: Clean list display with all metadata

---

## 5. Data Display

### Table View
- [ ] Click "View" on sample experiment
- [ ] Data table appears
- [ ] All columns displayed:
  - Frequency (MHz)
  - Reference
  - L1, L2, L3, L4
  - L1-Shielding, L2-Shielding, L3-Shielding, L4-Shielding
- [ ] Table is scrollable (vertical and horizontal)
- [ ] Header row sticky (stays visible when scrolling)

### Data Verification
- [ ] Check first row: Frequency = 100 MHz
- [ ] Reference values are negative dBm
- [ ] Location values are more negative than reference
- [ ] Shielding effectiveness values are positive
- [ ] Formula verified: SE = Reference - Location

**Example from first row:**
```
Frequency: 100
Reference: -20
L1: -43.75
L1-Shielding: -20 - (-43.75) = 23.75 dB ✓
```

---

## 6. Data Editing

### Edit Single Cell
- [ ] Click on any data cell
- [ ] Cell becomes editable (input field)
- [ ] Change value (e.g., change -20 to -22)
- [ ] Click outside cell or press Enter
- [ ] Value updates in table

### Save Changes
- [ ] Make several edits to different cells
- [ ] Click "Save Changes" button
- [ ] Success message displayed
- [ ] Refresh page
- [ ] Changes are persisted

### Edit Multiple Cells
- [ ] Edit frequency value
- [ ] Edit reference value
- [ ] Edit location value
- [ ] All changes saved together

**Expected**: All edits saved and persisted correctly

---

## 7. Visualizations

### Chart 1: Frequency vs Shielding Effectiveness
- [ ] Chart displays below data table
- [ ] X-axis shows frequencies (100-1200 MHz)
- [ ] Y-axis shows shielding effectiveness (dB)
- [ ] 4 lines displayed (L1, L2, L3, L4 shielding)
- [ ] Each line has different color
- [ ] Legend shows all location names
- [ ] Hover over data points shows values
- [ ] Chart is responsive (resizes with window)

### Chart 2: Frequency vs Actual Values
- [ ] Chart displays below first chart
- [ ] X-axis shows frequencies
- [ ] Y-axis shows signal power (dBm)
- [ ] 4 lines for locations (L1, L2, L3, L4)
- [ ] Different colors for each location
- [ ] Tooltips work on hover
- [ ] Chart is responsive

### Chart Interactivity
- [ ] Hover over any point → Tooltip shows exact values
- [ ] Click legend item → Toggle line visibility
- [ ] Resize browser window → Charts resize appropriately

**Expected**: Clear, professional charts with all data points

---

## 8. Download/Export

### Excel Export
- [ ] Click "Download Excel" button
- [ ] File downloads automatically
- [ ] File name includes experiment ID
- [ ] Open downloaded file in Excel/LibreOffice
- [ ] All columns present
- [ ] Original data intact
- [ ] Shielding effectiveness columns included
- [ ] Values match web display

**Expected**: Downloaded file contains complete data

---

## 9. Multiple Experiments

### Upload Second Experiment
- [ ] Upload sample_experiment.xlsx again (or create modified copy)
- [ ] Both experiments appear in list
- [ ] Each has unique ID
- [ ] Can view each independently
- [ ] Data doesn't mix between experiments

### Switch Between Experiments
- [ ] View first experiment
- [ ] View second experiment
- [ ] Tables and charts update correctly
- [ ] No data leakage

**Expected**: Multiple experiments managed independently

---

## 10. Delete Experiments

- [ ] Click "Delete" button on an experiment
- [ ] Confirmation dialog appears
- [ ] Click "Cancel" → Experiment not deleted
- [ ] Click "Delete" again
- [ ] Confirm deletion → Experiment removed
- [ ] Experiment disappears from list
- [ ] If currently viewing, view closes

**Expected**: Safe deletion with confirmation

---

## 11. Data Validation

### Shielding Effectiveness Calculation
Test with known values:

| Frequency | Reference | Location | Expected SE | Actual SE |
|-----------|-----------|----------|-------------|-----------|
| 100 | -20 | -45 | 25 dB | _____ |
| 200 | -22 | -52 | 30 dB | _____ |
| 300 | -21 | -36 | 15 dB | _____ |

- [ ] All calculations match expected values
- [ ] Formula: SE = Ref - Location
- [ ] Positive SE values indicate good shielding

---

## 12. Edge Cases

### Empty States
- [ ] Login with no experiments → "No experiments" message
- [ ] Message clear and informative

### Large Files
- [ ] Create Excel with 100+ rows
- [ ] Upload successfully
- [ ] Table scrolls properly
- [ ] Charts render all data points

### Special Characters
- [ ] Column names with spaces: "Location 1"
- [ ] Column names with symbols: "L1 (Front)"
- [ ] Parses correctly

### Missing Data
- [ ] Excel with some empty cells → Handled gracefully
- [ ] Shows empty or "N/A" in table

---

## 13. Browser Compatibility

Test in multiple browsers:

### Chrome/Chromium
- [ ] All features work
- [ ] Charts render correctly
- [ ] Upload functions properly

### Firefox
- [ ] All features work
- [ ] Charts render correctly
- [ ] Upload functions properly

### Safari
- [ ] All features work
- [ ] Charts render correctly
- [ ] Upload functions properly

### Edge
- [ ] All features work
- [ ] Charts render correctly
- [ ] Upload functions properly

---

## 14. Responsive Design

### Desktop (1920x1080)
- [ ] Layout looks professional
- [ ] All elements visible
- [ ] Charts appropriately sized

### Laptop (1366x768)
- [ ] Layout adjusts well
- [ ] No horizontal scrolling (except table)
- [ ] Charts readable

### Tablet (768x1024)
- [ ] Layout responsive
- [ ] Touch interactions work
- [ ] Charts scale down

---

## 15. Performance

### Load Time
- [ ] Page loads in < 2 seconds
- [ ] Charts render quickly
- [ ] Smooth animations

### File Processing
- [ ] Small file (12 rows) uploads instantly
- [ ] Medium file (100 rows) uploads in < 5 seconds
- [ ] Large file (1000 rows) uploads in < 30 seconds

### Editing
- [ ] Cell edits are instant
- [ ] Save operation completes quickly
- [ ] No lag in UI

---

## 16. Error Handling

### Server Errors
- [ ] Stop server while logged in
- [ ] Try to upload file → Connection error handled
- [ ] Try to save changes → Error message displayed

### Invalid Data
- [ ] Upload Excel with text in numeric columns → Error message
- [ ] Upload Excel with missing columns → Clear error
- [ ] Upload completely empty Excel → Handled gracefully

### Network Issues
- [ ] Slow connection → Loading indicators shown
- [ ] Failed upload → Retry option available

---

## 17. Security

### Authentication
- [ ] Cannot access /api/experiments without login
- [ ] Cannot access /api/upload without login
- [ ] Invalid credentials rejected
- [ ] Session expires after logout

### File Upload
- [ ] Only Excel files accepted
- [ ] File size reasonable (no 1GB files)
- [ ] Malicious files rejected

---

## 18. Data Persistence

### Restart Server
- [ ] Upload experiment
- [ ] Stop server (Ctrl+C)
- [ ] Start server again
- [ ] Login
- [ ] Experiment still in list
- [ ] Data intact

### Edit and Restart
- [ ] Edit experiment
- [ ] Save changes
- [ ] Restart server
- [ ] Changes persisted

**Expected**: All data saved in experiments.json

---

## 19. User Experience

### Clarity
- [ ] Button labels clear ("Save Changes", "Download Excel")
- [ ] Error messages helpful
- [ ] Success messages confirm actions
- [ ] Instructions easy to follow

### Visual Feedback
- [ ] Buttons have hover effects
- [ ] Upload area changes on drag-over
- [ ] Loading states for async operations
- [ ] Smooth transitions

### Workflow
- [ ] Login → Upload → View → Edit → Save → Download
- [ ] Each step intuitive
- [ ] No confusion about what to do next

---

## 20. Documentation

- [ ] README.md complete and accurate
- [ ] USER_GUIDE.md comprehensive
- [ ] QUICK_START.md easy to follow
- [ ] PROJECT_SUMMARY.md detailed
- [ ] Sample file included
- [ ] Comments in code helpful

---

## 📝 Test Results Summary

**Date Tested**: ________________

**Tester**: ____________________

**Overall Status**: ⭐⭐⭐⭐⭐

### Issues Found:
1. ___________________________________
2. ___________________________________
3. ___________________________________

### Recommendations:
1. ___________________________________
2. ___________________________________
3. ___________________________________

### Ready for Release?
- [ ] Yes, all tests passed
- [ ] Yes, with minor issues noted
- [ ] No, major issues found

---

## 🎯 Acceptance Criteria

System is ready for release if:
- ✅ All core features work (upload, view, edit, download)
- ✅ Authentication functions properly
- ✅ Calculations are accurate
- ✅ Charts display correctly
- ✅ Data persists across restarts
- ✅ No critical errors or crashes
- ✅ Documentation complete

---

## 📞 Support Information

If any test fails:
1. Check browser console (F12) for errors
2. Check server terminal output
3. Review USER_GUIDE.md for expected behavior
4. Verify file formats match examples
5. Try with fresh sample_experiment.xlsx

---

**Testing Complete! 🎉**

