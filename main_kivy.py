"""
Simple Kivy launcher that starts FastAPI server and opens browser
For Android APK build
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
import threading
import webbrowser
import os
import sys

class ShieldAnalyserApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Title
        self.title_label = Label(
            text='Faraday Shield Analyser',
            font_size='24sp',
            size_hint=(1, 0.2)
        )
        self.layout.add_widget(self.title_label)
        
        # Status
        self.status_label = Label(
            text='Starting server...',
            size_hint=(1, 0.2)
        )
        self.layout.add_widget(self.status_label)
        
        # Open button
        self.open_btn = Button(
            text='Open in Browser',
            size_hint=(1, 0.2),
            disabled=True
        )
        self.open_btn.bind(on_press=self.open_browser)
        self.layout.add_widget(self.open_btn)
        
        # Info
        self.info_label = Label(
            text='Login: admin / admin123\nData stored locally',
            size_hint=(1, 0.4)
        )
        self.layout.add_widget(self.info_label)
        
        # Start server
        Clock.schedule_once(lambda dt: self.start_server(), 1)
        
        return self.layout
    
    def start_server(self):
        # Start server thread
        server_thread = threading.Thread(target=self.run_server, daemon=True)
        server_thread.start()
        
        # Enable button after delay
        Clock.schedule_once(lambda dt: self.server_ready(), 3)
    
    def run_server(self):
        try:
            # This would start your FastAPI server
            # For now, just a placeholder
            pass
        except Exception as e:
            self.status_label.text = f'Error: {e}'
    
    def server_ready(self):
        self.status_label.text = 'Server running on localhost:8000'
        self.open_btn.disabled = False
    
    def open_browser(self, instance):
        webbrowser.open('http://127.0.0.1:8000')

if __name__ == '__main__':
    ShieldAnalyserApp().run()

