#!/usr/bin/env python3
"""
Quick test script to verify app launcher works
"""

import os
import sys
import tempfile

def test_app_data_dir():
    """Test that app data directory is created correctly"""
    print("Testing app data directory creation...")
    
    # Import the launcher
    import app_launcher
    
    # Test get_app_data_dir
    app_dir = app_launcher.get_app_data_dir()
    print(f"✅ App directory: {app_dir}")
    
    if os.path.exists(app_dir):
        print("✅ Directory exists")
    else:
        print("❌ Directory doesn't exist")
        return False
    
    return True

def test_data_setup():
    """Test that data files are initialized"""
    print("\nTesting data file setup...")
    
    import app_launcher
    
    app_dir = app_launcher.setup_data_directories()
    
    experiments_file = os.path.join(app_dir, 'experiments.json')
    creds_file = os.path.join(app_dir, 'creds.json')
    
    if os.path.exists(experiments_file):
        print("✅ experiments.json exists")
    else:
        print("❌ experiments.json missing")
        return False
    
    if os.path.exists(creds_file):
        print("✅ creds.json exists")
    else:
        print("❌ creds.json missing")
        return False
    
    return True

def test_imports():
    """Test that all required imports work"""
    print("\nTesting imports...")
    
    try:
        import fastapi
        print("✅ fastapi")
    except ImportError:
        print("❌ fastapi not installed")
        return False
    
    try:
        import uvicorn
        print("✅ uvicorn")
    except ImportError:
        print("❌ uvicorn not installed")
        return False
    
    try:
        import pandas
        print("✅ pandas")
    except ImportError:
        print("❌ pandas not installed")
        return False
    
    try:
        import openpyxl
        print("✅ openpyxl")
    except ImportError:
        print("❌ openpyxl not installed")
        return False
    
    return True

def main():
    print("=" * 60)
    print("🧪 Testing Faraday Shield Analyser Launcher")
    print("=" * 60)
    print()
    
    tests = [
        ("Imports", test_imports),
        ("App Data Dir", test_app_data_dir),
        ("Data Setup", test_data_setup),
    ]
    
    results = []
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result))
        except Exception as e:
            print(f"❌ Error in {name}: {e}")
            results.append((name, False))
    
    print("\n" + "=" * 60)
    print("📊 Test Results")
    print("=" * 60)
    
    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {name}")
    
    print()
    
    all_passed = all(result for _, result in results)
    
    if all_passed:
        print("✅ All tests passed! Ready to build.")
        print("\nNext step: Run 'python build_app.py'")
    else:
        print("❌ Some tests failed. Please fix issues first.")
        print("\nTip: Run 'pip install -r requirements_app.txt'")
    
    return all_passed

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

