"""
Initializes the Flask app and sets up the database with SQLAlchemy.

This module is responsible for creating and configuring the Flask application,
initializing the database, and registering all the necessary blueprints.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
import logging
from logging.handlers import RotatingFileHandler


# Load environment variables from .env file
load_dotenv()

# Initialize SQLAlchemy instance
db = SQLAlchemy()


def create_app():
    """
    Create and configure an instance of the Flask application.

    This function sets up the Flask app, initializes the database,
    registers all blueprints, and creates all database tables.

    Returns:
        Flask: A configured Flask application instance.
    """
    app = Flask(__name__)

    # Load configuration
    app.config.from_object("app.config")

    # Initialize the database with the app
    db.init_app(app)

    # Set up logging
    if not app.debug:
        if not os.path.exists("logs"):
            os.mkdir("logs")
        file_handler = RotatingFileHandler(
            "logs/acm_education.log", maxBytes=10240, backupCount=10
        )
        file_handler.setFormatter(
            logging.Formatter(
                "%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]"
            )
        )
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
        app.logger.setLevel(logging.INFO)
        app.logger.info("ACM Education startup")

    # Import and register blueprints
    from .routes import all_blueprints

    for bp in all_blueprints:
        app.register_blueprint(bp, url_prefix="/api" if bp.name != "main_bp" else "/")

    # Create all database tables
    with app.app_context():
        db.create_all()

    return app
