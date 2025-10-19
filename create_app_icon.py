#!/usr/bin/env python3
"""
Create app icon for Faraday Shield Analyser
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_icon():
    """Create a simple but professional app icon"""
    
    # Create different sizes
    sizes = [
        (1024, 1024),  # macOS
        (512, 512),    # Android
        (256, 256),    # Windows
        (128, 128),
        (64, 64),
        (32, 32)
    ]
    
    for size in sizes:
        # Create image with gradient background
        img = Image.new('RGB', size, color='white')
        draw = ImageDraw.Draw(img)
        
        # Draw gradient background
        for i in range(size[1]):
            ratio = i / size[1]
            # Gradient from #667eea to #764ba2
            r = int(102 + (118 - 102) * ratio)
            g = int(126 + (75 - 126) * ratio)
            b = int(234 + (162 - 234) * ratio)
            draw.line([(0, i), (size[0], i)], fill=(r, g, b))
        
        # Draw shield shape
        w, h = size
        shield_width = int(w * 0.6)
        shield_height = int(h * 0.7)
        x_center = w // 2
        y_top = int(h * 0.15)
        
        # Shield outline (white)
        points = [
            (x_center, y_top),  # Top point
            (x_center + shield_width//2, y_top + shield_height//6),  # Top right
            (x_center + shield_width//2, y_top + shield_height//2),  # Right
            (x_center, y_top + shield_height),  # Bottom point
            (x_center - shield_width//2, y_top + shield_height//2),  # Left
            (x_center - shield_width//2, y_top + shield_height//6),  # Top left
        ]
        
        # Draw filled shield
        draw.polygon(points, fill='white', outline='white')
        
        # Draw inner shield (smaller, colored)
        inner_scale = 0.85
        inner_points = [
            (x_center, int(y_top + shield_height * (1-inner_scale) * 0.5)),
            (x_center + int(shield_width//2 * inner_scale), int(y_top + shield_height//6 + (shield_height//6) * (1-inner_scale))),
            (x_center + int(shield_width//2 * inner_scale), int(y_top + shield_height//2)),
            (x_center, int(y_top + shield_height * inner_scale)),
            (x_center - int(shield_width//2 * inner_scale), int(y_top + shield_height//2)),
            (x_center - int(shield_width//2 * inner_scale), int(y_top + shield_height//6 + (shield_height//6) * (1-inner_scale))),
        ]
        draw.polygon(inner_points, fill=(102, 126, 234), outline=(80, 100, 200))
        
        # Draw "F" letter in the center
        try:
            # Try to use a nice font
            font_size = int(size[0] * 0.35)
            font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", font_size)
        except:
            # Fallback to default
            font = ImageFont.load_default()
        
        text = "F"
        # Get text size
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        text_x = x_center - text_width // 2
        text_y = y_top + shield_height // 3 - text_height // 2
        
        # Draw text with shadow
        draw.text((text_x + 2, text_y + 2), text, fill=(0, 0, 0, 128), font=font)
        draw.text((text_x, text_y), text, fill='white', font=font)
        
        # Save different formats
        if size == (1024, 1024):
            # macOS requires .icns (we'll save PNG and convert separately)
            img.save('app_icon_1024.png')
            print(f"✅ Created app_icon_1024.png ({size[0]}x{size[1]})")
        elif size == (512, 512):
            img.save('app_icon.png')
            print(f"✅ Created app_icon.png ({size[0]}x{size[1]})")
        elif size == (256, 256):
            img.save('app_icon_256.png')
            print(f"✅ Created app_icon_256.png ({size[0]}x{size[1]})")
        
        # Also save for Android drawable folders
        if size == (512, 512):
            img.save('icon.png')
            print(f"✅ Created icon.png for Android")

if __name__ == '__main__':
    print("🎨 Creating app icons...")
    print()
    
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        print("❌ Pillow not installed")
        print("📦 Installing Pillow...")
        import subprocess
        subprocess.run(['pip3', 'install', 'Pillow'], check=True)
        from PIL import Image, ImageDraw, ImageFont
    
    create_icon()
    print()
    print("✅ All icons created!")
    print()
    print("Files created:")
    print("  - app_icon.png (512x512) - Main icon")
    print("  - app_icon_1024.png (1024x1024) - High res")
    print("  - app_icon_256.png (256x256) - Standard")
    print("  - icon.png (512x512) - Android")

