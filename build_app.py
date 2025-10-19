#!/usr/bin/env python3
"""
Build script for creating standalone executables
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def build_windows():
    """Build Windows executable"""
    print("🪟 Building Windows executable...")
    
    cmd = [
        'pyinstaller',
        '--clean',
        '--onefile',
        '--name=FaradayShieldAnalyser',
        '--add-data=static:static',
        '--add-data=creds.json:.',
        '--add-data=sample_experiment.xlsx:.',
        '--hidden-import=uvicorn.logging',
        '--hidden-import=uvicorn.loops',
        '--hidden-import=uvicorn.loops.auto',
        '--hidden-import=uvicorn.protocols',
        '--hidden-import=uvicorn.protocols.http',
        '--hidden-import=uvicorn.protocols.http.auto',
        '--hidden-import=uvicorn.protocols.websockets',
        '--hidden-import=uvicorn.protocols.websockets.auto',
        '--hidden-import=uvicorn.lifespan',
        '--hidden-import=uvicorn.lifespan.on',
        '--hidden-import=passlib.handlers.bcrypt',
        '--console',
        'app_launcher.py'
    ]
    
    subprocess.run(cmd, check=True)
    print("✅ Windows build complete! Check dist/ directory")

def build_macos():
    """Build macOS application"""
    print("🍎 Building macOS application...")
    
    cmd = [
        'pyinstaller',
        '--clean',
        '--onefile',
        '--windowed',  # macOS app bundle
        '--name=FaradayShieldAnalyser',
        '--add-data=static:static',
        '--add-data=creds.json:.',
        '--add-data=sample_experiment.xlsx:.',
        '--hidden-import=uvicorn.logging',
        '--hidden-import=uvicorn.loops',
        '--hidden-import=uvicorn.loops.auto',
        '--hidden-import=uvicorn.protocols',
        '--hidden-import=uvicorn.protocols.http',
        '--hidden-import=uvicorn.protocols.http.auto',
        '--hidden-import=uvicorn.protocols.websockets',
        '--hidden-import=uvicorn.protocols.websockets.auto',
        '--hidden-import=uvicorn.lifespan',
        '--hidden-import=uvicorn.lifespan.on',
        '--hidden-import=passlib.handlers.bcrypt',
        'app_launcher.py'
    ]
    
    subprocess.run(cmd, check=True)
    print("✅ macOS build complete! Check dist/ directory")

def build_linux():
    """Build Linux executable"""
    print("🐧 Building Linux executable...")
    
    cmd = [
        'pyinstaller',
        '--clean',
        '--onefile',
        '--name=FaradayShieldAnalyser',
        '--add-data=static:static',
        '--add-data=creds.json:.',
        '--add-data=sample_experiment.xlsx:.',
        '--hidden-import=uvicorn.logging',
        '--hidden-import=uvicorn.loops',
        '--hidden-import=uvicorn.loops.auto',
        '--hidden-import=uvicorn.protocols',
        '--hidden-import=uvicorn.protocols.http',
        '--hidden-import=uvicorn.protocols.http.auto',
        '--hidden-import=uvicorn.protocols.websockets',
        '--hidden-import=uvicorn.protocols.websockets.auto',
        '--hidden-import=uvicorn.lifespan',
        '--hidden-import=uvicorn.lifespan.on',
        '--hidden-import=passlib.handlers.bcrypt',
        '--console',
        'app_launcher.py'
    ]
    
    subprocess.run(cmd, check=True)
    print("✅ Linux build complete! Check dist/ directory")

def main():
    """Main build script"""
    print("=" * 60)
    print("🔨 Faraday Shield Analyser - Build Script")
    print("=" * 60)
    print()
    
    # Check if PyInstaller is installed
    try:
        import PyInstaller
    except ImportError:
        print("❌ PyInstaller not found!")
        print("📦 Installing PyInstaller...")
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'pyinstaller'], check=True)
    
    # Detect platform
    platform = sys.platform
    
    print(f"🖥️  Detected platform: {platform}")
    print()
    
    try:
        if platform == "win32":
            build_windows()
        elif platform == "darwin":
            build_macos()
        else:
            build_linux()
        
        print()
        print("=" * 60)
        print("✅ Build completed successfully!")
        print("📁 Executable location: dist/FaradayShieldAnalyser")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ Build failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

