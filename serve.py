"""
Production server script for Azure deployment.
"""
import os
import logging
from waitress import serve
from app import create_app

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    try:
        # Create the Flask application
        app = create_app()
        
        # Get port from environment variable or default to 5000
        port = int(os.environ.get('PORT', 5000))
        
        # Log startup information
        logger.info(f"Starting server on port {port}")
        logger.info(f"Environment: {os.environ.get('FLASK_ENV', 'production')}")
        logger.info(f"Database URI: {app.config.get('SQLALCHEMY_DATABASE_URI', 'Not configured')}")
        
        # Start the server
        serve(app, host='127.0.0.1', port=port)
        
    except Exception as e:
        logger.error(f"Failed to start server: {str(e)}", exc_info=True)
        raise

if __name__ == '__main__':
    main() 