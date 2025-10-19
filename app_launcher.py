#!/usr/bin/env python3
"""
Faraday Shield Analyser - Standalone Application Launcher
Automatically starts the server and opens the application in the default browser.
"""

import os
import sys
import time
import threading
import webbrowser
from pathlib import Path
import json

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def get_app_data_dir():
    """Get platform-specific application data directory"""
    if sys.platform == "win32":
        app_data = os.getenv('APPDATA')
        app_dir = os.path.join(app_data, 'FaradayShieldAnalyser')
    elif sys.platform == "darwin":  # macOS
        app_data = os.path.expanduser('~/Library/Application Support')
        app_dir = os.path.join(app_data, 'FaradayShieldAnalyser')
    else:  # Linux
        app_data = os.path.expanduser('~/.local/share')
        app_dir = os.path.join(app_data, 'FaradayShieldAnalyser')
    
    # Create directory if it doesn't exist
    os.makedirs(app_dir, exist_ok=True)
    return app_dir

def setup_data_directories():
    """Setup data directories and initialize files"""
    app_dir = get_app_data_dir()
    
    # Initialize experiments.json if it doesn't exist
    experiments_file = os.path.join(app_dir, 'experiments.json')
    if not os.path.exists(experiments_file):
        with open(experiments_file, 'w') as f:
            json.dump({"experiments": []}, f, indent=2)
    
    # Copy creds.json if it doesn't exist
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
    
    print(f"📁 App data directory: {app_dir}")
    print(f"📊 Experiments file: {experiments_file}")
    print(f"🔐 Credentials file: {creds_file}")
    
    return app_dir

def open_browser(port=8000):
    """Open the application in the default web browser after a short delay"""
    time.sleep(2)  # Wait for server to start
    url = f"http://localhost:{port}"
    print(f"🌐 Opening browser at {url}")
    webbrowser.open(url)

def main():
    """Main application launcher"""
    print("=" * 60)
    print("🛡️  Faraday Shield Analyser")
    print("=" * 60)
    print()
    
    # Setup data directories
    app_dir = setup_data_directories()
    
    # Set environment variable for data directory
    os.environ['SHIELD_ANALYSER_DATA_DIR'] = app_dir
    
    # Import and start the FastAPI server
    print("\n🚀 Starting server...")
    
    # Start browser in a separate thread
    browser_thread = threading.Thread(target=open_browser, args=(8000,))
    browser_thread.daemon = True
    browser_thread.start()
    
    # Import and run the main application
    try:
        import main as app_main
        import uvicorn
        
        print("\n✅ Server started successfully!")
        print("📍 Running at http://localhost:8000")
        print("🔐 Default credentials: admin / admin123")
        print("\n⚠️  Press CTRL+C to stop the application")
        print("=" * 60)
        print()
        
        # Run the server
        uvicorn.run(
            app_main.app,
            host="127.0.0.1",  # Only localhost for security
            port=8000,
            log_level="warning"  # Reduce log verbosity
        )
    except KeyboardInterrupt:
        print("\n\n👋 Shutting down...")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nPress Enter to exit...")
        input()

if __name__ == "__main__":
    main()

