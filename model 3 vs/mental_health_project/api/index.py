"""
Vercel Entry Point — Mental Health Monitoring System
Vercel needs the Flask 'app' object to be importable from api/index.py
"""

import sys
import os

# Add the mental_health_project root to Python path
# so that 'utils', 'model', 'config' imports work correctly
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)

# Import the Flask app object from the actual app file
from app.app_enhanced import app

# Vercel needs this exact variable name: 'app'
# No need for app.run() — Vercel handles that automatically
