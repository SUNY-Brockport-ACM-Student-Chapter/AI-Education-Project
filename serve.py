"""
Production server script for Azure deployment.
"""
import os
from waitress import serve
from app import create_app

app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    print(f"Starting production server on port {port}")
    serve(app, host='0.0.0.0', port=port) 