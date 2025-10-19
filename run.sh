#!/bin/bash

# Faraday Shield Analyser Startup Script

echo "=================================================="
echo "     Faraday Shield Analyser"
echo "=================================================="
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo ""
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate
echo ""

# Install dependencies
echo "Checking dependencies..."
pip install -r requirements.txt --quiet
echo ""

# Start the application
echo "Starting application..."
echo ""
echo "=================================================="
echo "  Server running at http://localhost:8000"
echo "  Default credentials:"
echo "    Username: admin"
echo "    Password: admin123"
echo "=================================================="
echo ""
python main.py

