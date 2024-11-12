"""
Initializes the Flask application and sets up the database with SQLAlchemy.

This module is responsible for creating the Flask app instance, loading
configuration settings, initializing the database, and registering
blueprints for routing.

Imports:
- os: Provides a way to use operating system-dependent functionality,
  such as accessing environment variables.
- load_dotenv: A function from the dotenv package that loads environment
  variables from a .env file into the application's environment.
- Flask: The main class for creating a Flask web application.
- SQLALCHEMY_DATABASE_URI: The database URI configuration imported from
  the app's configuration module.
- init_db: A function that initializes the database connection and
  creates the necessary tables.
- all_blueprints: A collection of all blueprints defined in the
  application for routing.
- main_bp: The main blueprint for the application, typically containing
  the core routes.

Usage:
- Call the `create_app()` function to create and configure the Flask
  application instance. This function will load the configuration,
  initialize the database, and register the blueprints.
"""

import os

from dotenv import load_dotenv
from flask import Flask

from app.config import SQLALCHEMY_DATABASE_URI
from app.database import init_db

from .routes import all_blueprints, main_bp

# Load environment variables
load_dotenv()


def create_app():
    """
    Create and configure the Flask application.

    This function initializes the Flask app, loads configuration settings,
    sets up the database connection, and registers blueprints for routing.

    Returns:
        Flask: The configured Flask application instance.
    """
    app = Flask(__name__)

    # Load configuration
    app.config.from_object("app.config")

    # Add a secret key (required for sessions)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "admin")

    # Database configuration - use environment variables
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize database connection
    init_db(app)

    # Register main blueprint without prefix
    app.register_blueprint(main_bp)

    # Register all other blueprints with API prefix
    for blueprint in [bp for bp in all_blueprints if bp != main_bp]:
        app.register_blueprint(blueprint, url_prefix="/api")

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        """
        Closes the database session at the end of the request.

        Args:
            exception: Optional; an exception that occurred during the request.
        """
        # Close the session if it exists
        print(exception)
        if hasattr(app, "session"):
            app.session.close()

    return app
