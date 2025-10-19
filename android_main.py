"""
Android APK Main Entry Point
Starts FastAPI server and opens WebView
"""
import os
import sys
import threading
import time
from pathlib import Path

# Set up data directory for Android
if hasattr(sys, '_MEIPASS'):
    # Running in PyInstaller bundle
    BASE_DIR = Path(sys._MEIPASS)
else:
    BASE_DIR = Path(__file__).parent

# Android app data directory
from android.storage import app_storage_path
DATA_DIR = Path(app_storage_path())
os.makedirs(DATA_DIR, exist_ok=True)

# Set environment variable for main.py to use
os.environ['SHIELD_ANALYSER_DATA_DIR'] = str(DATA_DIR)

# Copy static files if not exists
STATIC_SRC = BASE_DIR / "static"
STATIC_DST = DATA_DIR / "static"
if not STATIC_DST.exists() and STATIC_SRC.exists():
    import shutil
    shutil.copytree(STATIC_SRC, STATIC_DST)

# Import after setting up paths
sys.path.insert(0, str(BASE_DIR))


def start_server():
    """Start FastAPI server in background thread"""
    import uvicorn
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        log_level="warning",
        access_log=False
    )


def main():
    """Main entry point for Android APK"""
    from kivy.app import App
    from kivy.uix.widget import Widget
    from android.runnable import run_on_ui_thread
    from jnius import autoclass
    
    # Start FastAPI server in background
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()
    
    # Wait for server to start
    time.sleep(2)
    
    # Android WebView classes
    WebView = autoclass('android.webkit.WebView')
    WebViewClient = autoclass('android.webkit.WebViewClient')
    WebSettings = autoclass('android.webkit.WebSettings')
    LayoutParams = autoclass('android.view.ViewGroup$LayoutParams')
    LinearLayout = autoclass('android.widget.LinearLayout')
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    
    class ShieldAnalyserApp(App):
        def build(self):
            return Widget()
        
        def on_start(self):
            @run_on_ui_thread
            def create_webview():
                activity = PythonActivity.mActivity
                webview = WebView(activity)
                settings = webview.getSettings()
                settings.setJavaScriptEnabled(True)
                settings.setBuiltInZoomControls(False)
                settings.setDisplayZoomControls(False)
                settings.setDomStorageEnabled(True)
                settings.setDatabaseEnabled(True)
                
                webview.setWebViewClient(WebViewClient())
                
                layout = LinearLayout(activity)
                layout.setOrientation(LinearLayout.VERTICAL)
                layout.addView(
                    webview,
                    LayoutParams.MATCH_PARENT,
                    LayoutParams.MATCH_PARENT
                )
                
                activity.setContentView(layout)
                webview.loadUrl('http://127.0.0.1:8000')
            
            create_webview()
    
    ShieldAnalyserApp().run()


if __name__ == '__main__':
    main()

