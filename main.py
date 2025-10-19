import os
import json
import uuid
from datetime import datetime, timedelta
from typing import Optional, List, Dict, Any

import pandas as pd
from fastapi import FastAPI, File, UploadFile, HTTPException, Depends, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import uvicorn

# Initialize FastAPI app
app = FastAPI(title="Faraday Shield Analyser")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Security
security = HTTPBasic()

# Data file - use app data directory if set (for standalone apps)
APP_DATA_DIR = os.getenv('SHIELD_ANALYSER_DATA_DIR', '.')
EXPERIMENTS_FILE = os.path.join(APP_DATA_DIR, "experiments.json")
CREDS_FILE = os.path.join(APP_DATA_DIR, "creds.json")

# Ensure experiments file exists
if not os.path.exists(EXPERIMENTS_FILE):
    with open(EXPERIMENTS_FILE, 'w') as f:
        json.dump({"experiments": []}, f)


# Models
class LoginRequest(BaseModel):
    username: str
    password: str


class ExperimentData(BaseModel):
    name: str
    data: List[Dict[str, Any]]


# Helper functions
def load_credentials():
    """Load credentials from creds.json"""
    try:
        with open(CREDS_FILE, 'r') as f:
            creds = json.load(f)
            return creds.get('users', [])
    except FileNotFoundError:
        return []


def verify_credentials(credentials: HTTPBasicCredentials = Depends(security)):
    """Verify user credentials"""
    users = load_credentials()
    for user in users:
        if user['username'] == credentials.username and user['password'] == credentials.password:
            return credentials.username
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid credentials",
        headers={"WWW-Authenticate": "Basic"},
    )


def load_experiments():
    """Load experiments from JSON file"""
    try:
        with open(EXPERIMENTS_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"experiments": []}


def save_experiments(data):
    """Save experiments to JSON file"""
    with open(EXPERIMENTS_FILE, 'w') as f:
        json.dump(data, f, indent=2)


def calculate_shielding_effectiveness(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate shielding effectiveness for each location column.
    Shielding Effectiveness = Reference - Location Value
    All shielding columns are placed at the right end of the table.
    """
    result_df = df.copy()
    
    # Find reference column (case insensitive)
    ref_col = None
    for col in df.columns:
        if 'reference' in col.lower() or 'ref' in col.lower():
            ref_col = col
            break
    
    if ref_col is None:
        raise ValueError("Reference column not found")
    
    # Collect shielding columns
    shielding_cols = {}
    
    # Calculate shielding effectiveness for each location column
    for col in df.columns:
        if col != ref_col and col not in ['Frequency', 'Frequency (MHz)', 'Freq', 'freq']:
            # Calculate shielding effectiveness
            se_col_name = f"{col}-Shielding"
            shielding_cols[se_col_name] = result_df[ref_col] - result_df[col]
    
    # Reorder columns: keep original columns, then add all shielding columns at the end
    original_cols = list(df.columns)
    for se_col_name, se_values in shielding_cols.items():
        result_df[se_col_name] = se_values
    
    # Reorder to put all shielding columns at the end
    non_shielding_cols = [col for col in result_df.columns if '-Shielding' not in col]
    shielding_col_names = [col for col in result_df.columns if '-Shielding' in col]
    result_df = result_df[non_shielding_cols + shielding_col_names]
    
    return result_df


def parse_excel_file(file_path: str) -> Dict[str, Any]:
    """Parse Excel file and extract data"""
    try:
        df = pd.read_excel(file_path)
        
        # Calculate shielding effectiveness
        df_with_se = calculate_shielding_effectiveness(df)
        
        # Convert to list of dictionaries
        data = df_with_se.to_dict('records')
        
        # Get column names
        columns = list(df_with_se.columns)
        
        return {
            "data": data,
            "columns": columns,
            "original_columns": list(df.columns)
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error parsing Excel file: {str(e)}")


# API Routes
@app.get("/")
async def read_root():
    """Serve the main HTML page"""
    return FileResponse("static/index.html")


@app.post("/api/login")
async def login(login_req: LoginRequest):
    """Login endpoint"""
    users = load_credentials()
    for user in users:
        if user['username'] == login_req.username and user['password'] == login_req.password:
            return {"status": "success", "message": "Login successful", "username": login_req.username}
    
    raise HTTPException(status_code=401, detail="Invalid credentials")


@app.post("/api/upload")
async def upload_file(
    file: UploadFile = File(...),
    username: str = Depends(verify_credentials)
):
    """Upload and parse Excel file"""
    if not file.filename.endswith(('.xlsx', '.xls')):
        raise HTTPException(status_code=400, detail="Only Excel files are allowed")
    
    # Save uploaded file temporarily
    temp_file = f"temp_{uuid.uuid4()}.xlsx"
    try:
        with open(temp_file, "wb") as f:
            content = await file.read()
            f.write(content)
        
        # Parse the file
        parsed_data = parse_excel_file(temp_file)
        
        # Create experiment entry
        experiment = {
            "id": str(uuid.uuid4()),
            "name": file.filename,
            "uploaded_by": username,
            "uploaded_at": datetime.now().isoformat(),
            "data": parsed_data["data"],
            "columns": parsed_data["columns"],
            "original_columns": parsed_data["original_columns"]
        }
        
        # Save to experiments
        experiments = load_experiments()
        experiments["experiments"].append(experiment)
        save_experiments(experiments)
        
        return {
            "status": "success",
            "message": "File uploaded and parsed successfully",
            "experiment": experiment
        }
    finally:
        # Clean up temp file
        if os.path.exists(temp_file):
            os.remove(temp_file)


@app.get("/api/experiments")
async def get_experiments(username: str = Depends(verify_credentials)):
    """Get all experiments"""
    experiments = load_experiments()
    return experiments


@app.get("/api/experiments/{experiment_id}")
async def get_experiment(experiment_id: str, username: str = Depends(verify_credentials)):
    """Get a specific experiment"""
    experiments = load_experiments()
    for exp in experiments["experiments"]:
        if exp["id"] == experiment_id:
            return exp
    
    raise HTTPException(status_code=404, detail="Experiment not found")


@app.put("/api/experiments/{experiment_id}")
async def update_experiment(
    experiment_id: str,
    update_data: Dict[str, Any],
    username: str = Depends(verify_credentials)
):
    """Update experiment data"""
    print(f"Updating experiment {experiment_id}")
    print(f"Received data keys: {update_data.keys()}")
    print(f"Columns in update: {update_data.get('columns', 'NOT PROVIDED')}")
    
    experiments = load_experiments()
    
    for i, exp in enumerate(experiments["experiments"]):
        if exp["id"] == experiment_id:
            # Update the data
            experiments["experiments"][i]["data"] = update_data.get("data", exp["data"])
            # Update columns if provided
            if "columns" in update_data:
                experiments["experiments"][i]["columns"] = update_data["columns"]
                print(f"Updated columns to: {update_data['columns']}")
            else:
                print("WARNING: No columns in update data!")
            
            experiments["experiments"][i]["modified_at"] = datetime.now().isoformat()
            experiments["experiments"][i]["modified_by"] = username
            
            save_experiments(experiments)
            
            # Verify save
            saved_exp = experiments["experiments"][i]
            print(f"Saved columns: {saved_exp.get('columns', 'NO COLUMNS')}")
            
            return {
                "status": "success", 
                "message": "Experiment updated successfully",
                "columns": saved_exp.get("columns", [])
            }
    
    raise HTTPException(status_code=404, detail="Experiment not found")


@app.delete("/api/experiments/{experiment_id}")
async def delete_experiment(experiment_id: str, username: str = Depends(verify_credentials)):
    """Delete an experiment"""
    experiments = load_experiments()
    
    experiments["experiments"] = [exp for exp in experiments["experiments"] if exp["id"] != experiment_id]
    save_experiments(experiments)
    
    return {"status": "success", "message": "Experiment deleted successfully"}


@app.get("/api/experiments/{experiment_id}/download")
async def download_experiment(experiment_id: str, username: str = Depends(verify_credentials)):
    """Download experiment as Excel file"""
    experiments = load_experiments()
    
    for exp in experiments["experiments"]:
        if exp["id"] == experiment_id:
            # Create DataFrame from experiment data
            df = pd.DataFrame(exp["data"])
            
            # Save to Excel
            output_file = f"experiment_{experiment_id}.xlsx"
            df.to_excel(output_file, index=False, sheet_name='Measurements')
            
            return FileResponse(
                output_file,
                media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                filename=f"{exp['name'].replace('.xlsx', '')}_processed.xlsx"
            )
    
    raise HTTPException(status_code=404, detail="Experiment not found")


@app.post("/api/experiments/create")
async def create_experiment(
    experiment_data: ExperimentData,
    username: str = Depends(verify_credentials)
):
    """Create a new experiment manually"""
    experiment = {
        "id": str(uuid.uuid4()),
        "name": experiment_data.name,
        "uploaded_by": username,
        "uploaded_at": datetime.now().isoformat(),
        "data": experiment_data.data,
        "columns": list(experiment_data.data[0].keys()) if experiment_data.data else []
    }
    
    experiments = load_experiments()
    experiments["experiments"].append(experiment)
    save_experiments(experiments)
    
    return {
        "status": "success",
        "message": "Experiment created successfully",
        "experiment": experiment
    }


# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")


if __name__ == "__main__":
    # Create static directory if it doesn't exist
    os.makedirs("static", exist_ok=True)
    
    print("=" * 60)
    print("Faraday Shield Analyser")
    print("=" * 60)
    print("\nStarting server at http://localhost:8000")
    print("\nDefault credentials:")
    print("  Username: admin")
    print("  Password: admin123")
    print("\nPress CTRL+C to stop the server")
    print("=" * 60)
    
    uvicorn.run(app, host="0.0.0.0", port=8000)

