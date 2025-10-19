#!/usr/bin/env python3
"""
Build script for native macOS application with embedded webview
"""

import os
import sys
import subprocess

def build_native_mac():
    """Build native macOS application"""
    print("=" * 70)
    print("🍎 Building Native macOS Application")
    print("=" * 70)
    print()
    
    cmd = [
        'pyinstaller',
        '--clean',
        '--onefile',
        '--windowed',
        '--name=FaradayShieldAnalyser',
        '--icon=app_icon.icns',  # Add icon if available
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
        '--hidden-import=webview',
        '--osx-bundle-identifier=com.shieldanalyser.app',
        'app_native_mac.py'
    ]
    
    # Remove icon argument if file doesn't exist
    if not os.path.exists('app_icon.icns'):
        cmd = [arg for arg in cmd if not arg.startswith('--icon=')]
    
    try:
        subprocess.run(cmd, check=True)
        print()
        print("=" * 70)
        print("✅ Native Mac App Built Successfully!")
        print("=" * 70)
        print()
        print("📁 Location: dist/FaradayShieldAnalyser.app")
        print("🎯 This is a TRUE native Mac app:")
        print("   ✓ No external browser")
        print("   ✓ Embedded webview")
        print("   ✓ Standalone window")
        print("   ✓ Mac-native experience")
        print()
        print("🚀 To test:")
        print("   open dist/FaradayShieldAnalyser.app")
        print()
    except subprocess.CalledProcessError as e:
        print()
        print("❌ Build failed!")
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    build_native_mac()

