#!/usr/bin/env python3
"""
Faraday Shield Analyser - Native Mac App with Embedded WebView
No external browser - true standalone application
"""

import os
import sys
import threading
import time
import webview
from pathlib import Path

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def get_app_data_dir():
    """Get platform-specific application data directory"""
    if sys.platform == "darwin":  # macOS
        app_data = os.path.expanduser('~/Library/Application Support')
        app_dir = os.path.join(app_data, 'FaradayShieldAnalyser')
    else:
        app_data = os.path.expanduser('~/.local/share')
        app_dir = os.path.join(app_data, 'FaradayShieldAnalyser')
    
    os.makedirs(app_dir, exist_ok=True)
    return app_dir

def setup_data_directories():
    """Setup data directories and initialize files"""
    import json
    
    app_dir = get_app_data_dir()
    
    # Initialize experiments.json
    experiments_file = os.path.join(app_dir, 'experiments.json')
    if not os.path.exists(experiments_file):
        with open(experiments_file, 'w') as f:
            json.dump({"experiments": []}, f, indent=2)
    
    # Copy creds.json
    creds_file = os.path.join(app_dir, 'creds.json')
    if not os.path.exists(creds_file):
        default_creds = {
            "users": [
                {"username": "admin", "password": "admin123"},
                {"username": "user", "password": "password123"}
            ]
        }
        with open(creds_file, 'w') as f:
            json.dump(default_creds, f, indent=2)
    
    return app_dir

def start_server():
    """Start the FastAPI server in a separate thread"""
    import uvicorn
    import main as app_main
    
    # Set environment variable for data directory
    os.environ['SHIELD_ANALYSER_DATA_DIR'] = get_app_data_dir()
    
    # Run the server
    uvicorn.run(
        app_main.app,
        host="127.0.0.1",
        port=8000,
        log_level="error",  # Reduce log verbosity
        access_log=False
    )

def main():
    """Main application launcher with embedded webview"""
    print("=" * 60)
    print("🛡️  Faraday Shield Analyser - Native App")
    print("=" * 60)
    
    # Setup data directories
    app_dir = setup_data_directories()
    print(f"📁 Data directory: {app_dir}")
    
    # Start server in background thread
    print("🚀 Starting server...")
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()
    
    # Wait for server to start
    time.sleep(2)
    
    print("✅ Server started")
    print("🖥️  Opening application window...")
    
    # Create native window with embedded webview
    window = webview.create_window(
        title='Faraday Shield Analyser',
        url='http://127.0.0.1:8000',
        width=1400,
        height=900,
        resizable=True,
        fullscreen=False,
        min_size=(800, 600),
        background_color='#667eea'
    )
    
    # Start the webview
    webview.start(debug=False)

if __name__ == "__main__":
    main()

