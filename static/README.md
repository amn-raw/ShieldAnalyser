# Static Files

This directory contains all static assets served by the application.

## Structure:

```
static/
├── index.html          # Main application UI
├── images/            # Image assets
│   ├── icon.png       # App icon
│   └── app_icon.png   # App icon (duplicate)
├── css/              # CSS files (future)
└── js/               # JavaScript files (future)
```

## Files:

- **index.html** - Complete single-page application with embedded CSS and JavaScript
  - Login system
  - Experiment management
  - Data table with editing
  - Three interactive charts (Chart.js)
  - Responsive design

## Future Organization:

To improve maintainability, consider extracting:
- CSS from index.html → `css/styles.css`
- JavaScript from index.html → `js/app.js`
- Chart code → `js/charts.js`

## Notes:

- All assets are bundled into Mac app and Android APK
- Changes require rebuilding native apps
- Keep images optimized for app size
