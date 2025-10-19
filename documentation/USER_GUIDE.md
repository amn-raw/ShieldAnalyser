# Faraday Shield Analyser - User Guide

## Overview

The Faraday Shield Analyser is a web-based application designed to analyze and visualize Faraday shield effectiveness measurements. It provides an intuitive interface for uploading measurement data, calculating shielding effectiveness, and generating comprehensive visualizations.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Using the Application](#using-the-application)
3. [Excel File Format](#excel-file-format)
4. [Features](#features)
5. [Troubleshooting](#troubleshooting)

---

## Getting Started

### Installation

1. Make sure you have Python 3.9 or higher installed on your system.

2. Navigate to the ShieldAnalyser directory:
   ```bash
   cd /path/to/ShieldAnalyser
   ```

3. Run the application using the startup script:
   ```bash
   ./run.sh
   ```

   Or manually:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   python main.py
   ```

4. Open your web browser and navigate to:
   ```
   http://localhost:8000
   ```

### First Login

Use the default credentials:
- **Username**: admin
- **Password**: admin123

You can add or modify user credentials in the `creds.json` file.

---

## Using the Application

### 1. Login

Enter your username and password on the login page. If the credentials are correct, you'll be redirected to the main dashboard.

### 2. Upload Experiment Data

#### Option A: Upload Excel File

1. Click on the upload area or drag and drop your Excel file
2. The file will be automatically parsed and processed
3. Shielding effectiveness will be calculated for each location

#### Option B: Use Sample Data

A sample Excel file (`sample_experiment.xlsx`) is provided for testing. You can upload this file to see how the system works.

### 3. View Experiments

All uploaded experiments are listed in the "Experiments" section. Each experiment shows:
- Experiment name (filename)
- Upload date and time
- Uploader username

Click on any experiment to view its data and visualizations.

### 4. Edit Data

Once an experiment is open:
1. You can edit any cell in the data table by clicking on it
2. After making changes, click "Save Changes" to update the experiment
3. The visualizations will automatically update

### 5. View Visualizations

Two charts are automatically generated for each experiment:

#### Chart 1: Frequency vs Shielding Effectiveness
- Shows how effective the shielding is at different frequencies
- Multiple lines for different locations
- Higher values = better shielding

#### Chart 2: Frequency vs Actual Values
- Shows the actual measured signal power values
- Helps identify measurement patterns and anomalies

### 6. Download Data

Click "Download Excel" to export the experiment data (including calculated shielding effectiveness) as an Excel file.

### 7. Delete Experiments

Click the "Delete" button next to an experiment to remove it from the system.

---

## Excel File Format

### Required Structure

Your Excel file must follow this format:

| Column 1 | Column 2  | Column 3 | Column 4 | ... |
|----------|-----------|----------|----------|-----|
| Frequency (MHz) | Reference | L1 | L2 | ... |
| 100 | -20 | -45 | -50 | ... |
| 200 | -22 | -48 | -52 | ... |
| ... | ... | ... | ... | ... |

### Column Details

1. **First Column - Frequency**
   - Can be named: "Frequency", "Frequency (MHz)", "Freq", etc.
   - Contains frequency values in MHz
   - Example: 100, 200, 300, 400...

2. **Second Column - Reference**
   - Can be named: "Reference", "Ref", "ref", etc.
   - Contains reference signal power measurements (typically in dBm)
   - Example: -20, -22, -21...

3. **Subsequent Columns - Location Measurements**
   - Can be named anything: "L1", "L2", "Location 1", "Point A", etc.
   - Contains signal power measurements at different locations
   - Should typically be lower than reference values (indicating attenuation)

### Important Notes

- All measurements should be in the same unit (typically dBm)
- The file should contain at least one frequency, one reference column, and one location column
- Empty cells or invalid data may cause parsing errors

### Example Data

```
Frequency (MHz)  Reference  L1      L2      L3
100              -20        -43.75  -53.32  -39.56
200              -22        -51.51  -49.12  -44.85
300              -21        -48.32  -47.82  -38.00
400              -23        -48.99  -49.83  -43.14
```

---

## Features

### 1. Automatic Shielding Effectiveness Calculation

**Formula**: Shielding Effectiveness (dB) = Reference - Location Value

For each location column, the system automatically creates a corresponding shielding effectiveness column (e.g., "L1-Shielding").

**Example**:
- Reference: -20 dBm
- L1: -45 dBm
- L1-Shielding: -20 - (-45) = 25 dB

Higher shielding effectiveness values indicate better shielding performance.

### 2. Interactive Data Tables

- Edit any cell by clicking on it
- Changes are saved when you click "Save Changes"
- Recalculate shielding effectiveness automatically

### 3. Real-time Visualizations

- Charts update automatically when data changes
- Multiple locations displayed on the same chart for easy comparison
- Interactive tooltips show exact values

### 4. Experiment Management

- Store multiple experiments
- Each experiment is timestamped
- Track who uploaded each experiment

### 5. Export Functionality

- Download processed data as Excel files
- Includes original data + calculated shielding effectiveness
- File names include experiment ID for easy identification

### 6. Authentication

- Simple username/password authentication
- Configurable credentials via `creds.json`
- Session-based access control

---

## Troubleshooting

### Server Won't Start

**Problem**: Error when running `python main.py`

**Solution**:
1. Make sure you activated the virtual environment:
   ```bash
   source venv/bin/activate
   ```
2. Reinstall dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Check if port 8000 is available:
   ```bash
   lsof -i :8000  # On Mac/Linux
   ```

### Can't Login

**Problem**: "Invalid credentials" error

**Solution**:
1. Check `creds.json` file exists
2. Verify username and password are correct
3. Default credentials: admin/admin123

### Excel File Won't Upload

**Problem**: "Error parsing Excel file"

**Solution**:
1. Verify file format matches the required structure
2. Check that the file has:
   - A frequency column
   - A reference column
   - At least one location column
3. Ensure all data cells contain valid numbers
4. Use the sample file (`sample_experiment.xlsx`) as a template

### Charts Not Displaying

**Problem**: Blank charts or no visualization

**Solution**:
1. Make sure the experiment has valid data
2. Check browser console for JavaScript errors (F12)
3. Try refreshing the page
4. Verify that frequency and location columns are properly detected

### Changes Not Saving

**Problem**: Edits don't persist after clicking "Save Changes"

**Solution**:
1. Check that you're logged in
2. Verify you have write permissions
3. Look for error messages in the browser console
4. Try refreshing and re-opening the experiment

### Port Already in Use

**Problem**: "Address already in use" error

**Solution**:
1. Find and kill the process using port 8000:
   ```bash
   # On Mac/Linux
   lsof -ti:8000 | xargs kill -9
   
   # On Windows
   netstat -ano | findstr :8000
   taskkill /PID <PID> /F
   ```
2. Or change the port in `main.py`:
   ```python
   uvicorn.run(app, host="0.0.0.0", port=8001)  # Change to 8001
   ```

---

## Advanced Configuration

### Adding Users

Edit `creds.json`:
```json
{
  "users": [
    {
      "username": "admin",
      "password": "admin123"
    },
    {
      "username": "newuser",
      "password": "newpassword"
    }
  ]
}
```

### Changing Security Settings

Edit `.env` file (create if it doesn't exist):
```
SECRET_KEY=your-custom-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Backup Data

All experiment data is stored in `experiments.json`. To backup:
```bash
cp experiments.json experiments_backup_$(date +%Y%m%d).json
```

---

## Tips and Best Practices

1. **Naming Conventions**: Use clear, descriptive names for location columns (e.g., "Front_Panel", "Side_Wall") instead of just "L1", "L2"

2. **Regular Backups**: Periodically backup your `experiments.json` file

3. **Data Validation**: Always review uploaded data in the table view before relying on the visualizations

4. **Frequency Range**: Ensure your frequency measurements cover the full range of interest

5. **Reference Measurements**: Take reference measurements in the same conditions as location measurements

6. **Multiple Experiments**: Upload separate experiments for different test conditions or shield configurations

---

## Support

For issues or questions:
1. Check this user guide
2. Review the README.md file
3. Check the browser console for error messages (F12)
4. Review the terminal output where the server is running

---

## Version Information

- Application Version: 1.0.0
- Last Updated: October 2025

