#!/usr/bin/env python3
"""
Faraday Shield Analyser - Native Android App
Uses Kivy framework with embedded webview
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window
from android.permissions import request_permissions, Permission
import threading
import os
import sys

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

class ShieldAnalyserApp(App):
    """Main application class"""
    
    def build(self):
        """Build the app UI"""
        # Request permissions
        request_permissions([
            Permission.INTERNET,
            Permission.WRITE_EXTERNAL_STORAGE,
            Permission.READ_EXTERNAL_STORAGE
        ])
        
        # Set window properties
        Window.clearcolor = (0.4, 0.49, 0.92, 1)  # #667eea
        
        # Create main layout
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Title
        title = Label(
            text='Faraday Shield Analyser',
            font_size='24sp',
            size_hint=(1, 0.2),
            bold=True
        )
        layout.add_widget(title)
        
        # Status label
        self.status_label = Label(
            text='Starting server...',
            size_hint=(1, 0.2)
        )
        layout.add_widget(self.status_label)
        
        # Open browser button
        self.open_button = Button(
            text='Open App',
            size_hint=(1, 0.2),
            background_color=(0.3, 0.8, 0.3, 1),
            disabled=True
        )
        self.open_button.bind(on_press=self.open_browser)
        layout.add_widget(self.open_button)
        
        # Info label
        info = Label(
            text='Your data is stored locally on this device\nLogin: admin / admin123',
            size_hint=(1, 0.4),
            font_size='14sp'
        )
        layout.add_widget(info)
        
        # Start server
        Clock.schedule_once(lambda dt: self.start_server(), 1)
        
        return layout
    
    def start_server(self):
        """Start the FastAPI server"""
        self.status_label.text = 'Starting server...'
        
        # Start server in background thread
        server_thread = threading.Thread(target=self._run_server, daemon=True)
        server_thread.start()
        
        # Wait and enable button
        Clock.schedule_once(lambda dt: self._server_started(), 3)
    
    def _run_server(self):
        """Run the FastAPI server"""
        try:
            import uvicorn
            import main as app_main
            
            # Set up data directory
            from pathlib import Path
            app_dir = Path.home() / 'ShieldAnalyser'
            app_dir.mkdir(exist_ok=True)
            os.environ['SHIELD_ANALYSER_DATA_DIR'] = str(app_dir)
            
            # Initialize files
            import json
            exp_file = app_dir / 'experiments.json'
            if not exp_file.exists():
                exp_file.write_text(json.dumps({"experiments": []}, indent=2))
            
            creds_file = app_dir / 'creds.json'
            if not creds_file.exists():
                default_creds = {
                    "users": [
                        {"username": "admin", "password": "admin123"},
                        {"username": "user", "password": "password123"}
                    ]
                }
                creds_file.write_text(json.dumps(default_creds, indent=2))
            
            # Run server
            uvicorn.run(
                app_main.app,
                host="127.0.0.1",
                port=8000,
                log_level="error",
                access_log=False
            )
        except Exception as e:
            print(f"Server error: {e}")
            self.status_label.text = f'Error: {e}'
    
    def _server_started(self):
        """Server has started"""
        self.status_label.text = 'Server running on localhost:8000'
        self.open_button.disabled = False
    
    def open_browser(self, instance):
        """Open the app in browser"""
        import webbrowser
        webbrowser.open('http://127.0.0.1:8000')

if __name__ == '__main__':
    ShieldAnalyserApp().run()

